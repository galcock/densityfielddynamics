"""
radial_solver.py -- 1D Radial Solver for the DFD Psi-Bubble in Spherical Symmetry
================================================================================

Solves the coupled DFD + EM system in a ferrite-superconductor spherical shell.

GOVERNING EQUATION (spherical, azimuthal symmetry):

    (1/r^2) d/dr [r^2 dpsi/dr] = kappa_DFD * N_coh * u_EM(r) * mu_MOND(x)

where:
    psi(r)    = dimensionless gravitational potential (metric component g_00 ~ -(1+2psi))
    u_EM(r)   = electromagnetic energy density [J/m^3]
    kappa_DFD = 4*pi*G / c^4  (fundamental DFD coupling)
    N_coh     = quantum coherence enhancement factor
    mu_MOND(x)= MOND interpolating function, x = |grad psi| / a0_MOND * c^2
                simple form: mu(x) = x / (1 + x)

BOUNDARY CONDITIONS:
    dpsi/dr -> 0  as r -> 0  (regularity)
    psi -> psi_bg  as r -> R_far  (match to background)

The acceleration on a test mass at radius r is:
    a(r) = -(c^2 / 2) dpsi/dr        [in the Newtonian limit, c^2 dpsi/dr -> -g]
    More precisely: a(r) = -c^2 dpsi/dr

The net force on the shell is obtained from the stress-energy integral.
"""

import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from constants import (c, G, kappa_DFD, a0_MOND, N_coh_default,
                       R_inner, R_outer, eps_r_ferrite, mu_r_ferrite,
                       eps0, mu0, psi_background_earth, psi_background_deep_space)


# ============================================================
# MOND interpolating function
# ============================================================
def mu_MOND(grad_psi, a0=a0_MOND):
    """
    Simple MOND interpolating function.
    x = |grad_psi| * c^2 / a0
    mu(x) = x / (1 + x)

    In the Newtonian regime (x >> 1): mu -> 1  (standard gravity)
    In the deep-MOND regime (x << 1): mu -> x  (enhanced coupling)
    """
    x = np.abs(grad_psi) * c**2 / a0
    # Avoid division by zero
    return np.where(x > 1e-30, x / (1.0 + x), 1e-30)


# ============================================================
# EM energy density profile in the shell
# ============================================================
def u_EM_profile(r, E_stored, R1, R2, mode='uniform'):
    """
    Electromagnetic energy density in the ferrite shell.

    Parameters:
        r        : radial coordinate array [m]
        E_stored : total stored EM energy [J]
        R1, R2   : inner and outer radii of ferrite shell [m]
        mode     : 'uniform' or 'resonant'

    For 'uniform': energy spread uniformly in the shell volume.
    For 'resonant': energy concentrated near inner surface (standing wave).
    """
    V_shell = (4.0 / 3.0) * np.pi * (R2**3 - R1**3)

    if mode == 'uniform':
        u = np.where((r >= R1) & (r <= R2), E_stored / V_shell, 0.0)
    elif mode == 'resonant':
        # Standing-wave pattern: u ~ sin^2(pi*(r-R1)/(R2-R1))
        # Normalized so integral over shell = E_stored
        in_shell = (r >= R1) & (r <= R2)
        pattern = np.where(in_shell,
                           np.sin(np.pi * (r - R1) / (R2 - R1))**2,
                           0.0)
        # Numerical normalization
        dr = np.gradient(r)
        integral = np.sum(pattern * 4.0 * np.pi * r**2 * dr)
        if integral > 0:
            u = pattern * E_stored / integral
        else:
            u = np.zeros_like(r)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    return u


# ============================================================
# ODE system for BVP
# ============================================================
def ode_system(r, y, params):
    """
    BVP ODE system for the radial DFD equation.

    y[0] = psi(r)
    y[1] = dpsi/dr

    d(psi)/dr = y[1]
    d(y[1])/dr = source - (2/r)*y[1]

    where source = kappa_DFD * N_coh * u_EM(r) * mu_MOND(y[1])
    """
    psi = y[0]
    dpsi = y[1]

    N_coh = params['N_coh']
    u_EM_func = params['u_EM_func']

    u = u_EM_func(r)

    # MOND factor
    mu_val = mu_MOND(dpsi)

    # Source term: Poisson-like equation in DFD
    # (1/r^2) d/dr(r^2 dpsi/dr) = kappa * N * u * mu
    # => d^2psi/dr^2 + (2/r) dpsi/dr = kappa * N * u * mu
    # => d^2psi/dr^2 = kappa * N * u * mu - (2/r) dpsi/dr
    source = kappa_DFD * N_coh * u * mu_val

    # Handle r=0 carefully (L'Hopital: (2/r)*dpsi/dr -> (2/3)*d^2psi/dr^2 at r=0)
    safe_r = np.where(r > 1e-10, r, 1e-10)
    d2psi = source - (2.0 / safe_r) * dpsi

    return np.vstack([dpsi, d2psi])


def bc_residuals(ya, yb, params):
    """
    Boundary conditions:
        At r_min (near 0): dpsi/dr = 0  (regularity)
        At r_max:          psi = psi_background  (match far field)
    """
    psi_bg = params['psi_bg']
    return np.array([
        ya[1],           # dpsi/dr = 0 at r_min
        yb[0] - psi_bg   # psi = psi_bg at r_max
    ])


# ============================================================
# Main solver
# ============================================================
def solve_radial_psi(E_stored, R1=R_inner, R2=R_outer, N_coh=N_coh_default,
                     r_min=0.01, r_max=50.0, N_grid=500,
                     em_mode='uniform', environment='earth_orbit',
                     r_orbit=None):
    """
    Solve for psi(r) in the spherically symmetric DFD psi-bubble.

    Parameters:
        E_stored    : total stored EM energy in the shell [J]
        R1, R2      : inner/outer ferrite shell radii [m]
        N_coh       : quantum coherence enhancement factor
        r_min, r_max: domain bounds [m]
        N_grid      : number of grid points
        em_mode     : 'uniform' or 'resonant'
        environment : 'earth_orbit' or 'deep_space'
        r_orbit     : orbital radius [m] (for earth_orbit; default 400 km altitude)

    Returns:
        dict with keys: r, psi, dpsi_dr, acceleration, u_EM, force_on_shell, params
    """
    # Set up grid
    r = np.linspace(r_min, r_max, N_grid)

    # EM energy density
    u_EM = u_EM_profile(r, E_stored, R1, R2, mode=em_mode)
    u_EM_func = interp1d(r, u_EM, kind='linear', bounds_error=False, fill_value=0.0)

    # Background potential
    if environment == 'earth_orbit':
        if r_orbit is None:
            r_orbit = 6.771e6  # ~400 km altitude
        psi_bg, dpsi_bg = psi_background_earth(r_orbit)
    elif environment == 'deep_space':
        psi_bg, dpsi_bg = psi_background_deep_space()
    else:
        psi_bg, dpsi_bg = 0.0, 0.0

    params = {
        'N_coh': N_coh,
        'u_EM_func': u_EM_func,
        'psi_bg': psi_bg,
        'E_stored': E_stored,
        'R1': R1,
        'R2': R2,
        'environment': environment,
    }

    # Initial guess: linear interpolation from 0 to psi_bg
    y_init = np.zeros((2, N_grid))
    y_init[0, :] = psi_bg  # constant guess for psi
    y_init[1, :] = 0.0     # zero gradient guess

    # Solve BVP
    def ode_wrapped(r_val, y_val):
        return ode_system(r_val, y_val, params)

    def bc_wrapped(ya, yb):
        return bc_residuals(ya, yb, params)

    sol = solve_bvp(ode_wrapped, bc_wrapped, r, y_init, tol=1e-8, max_nodes=5000)

    if not sol.success:
        print(f"WARNING: BVP solver did not converge: {sol.message}")
        print("  Returning best available solution.")

    # Extract solution on a fine grid
    r_fine = np.linspace(r_min, r_max, 2000)
    psi_fine = sol.sol(r_fine)[0]
    dpsi_fine = sol.sol(r_fine)[1]

    # Acceleration: a(r) = -c^2 * dpsi/dr
    # (positive a means outward acceleration for negative dpsi/dr)
    acceleration = -c**2 * dpsi_fine

    # EM energy on fine grid
    u_EM_fine = u_EM_func(r_fine)

    # Force on shell: integrate pressure over shell volume
    # The DFD "gravitational pressure" on the shell material is:
    #   f_grav(r) = -rho(r) * c^2 * dpsi/dr
    # For the EM field energy acting as source:
    #   f_r(r) = -u_EM(r) / c^2 * c^2 * dpsi/dr * N_coh * mu_MOND(dpsi)
    #          = -u_EM(r) * dpsi/dr * N_coh * mu_MOND(dpsi)
    # But more directly, the net force on the shell is:
    #   F = integral of (gradient of psi) * (energy density / c^2) * 4*pi*r^2 dr
    # This gives the "weight" of the EM field in the modified spacetime.

    # For a symmetric shell, net force = 0. But we compute the outward
    # radial "gravitational force density" for later use in asymmetric cases.
    mu_vals = mu_MOND(dpsi_fine)
    force_density = -u_EM_fine * dpsi_fine * N_coh * mu_vals

    # Integrate over shell to get radial force per steradian
    dr_fine = np.gradient(r_fine)
    shell_mask = (r_fine >= R1) & (r_fine <= R2)
    force_integral = np.sum(force_density[shell_mask] *
                            4.0 * np.pi * r_fine[shell_mask]**2 *
                            dr_fine[shell_mask])

    return {
        'r': r_fine,
        'psi': psi_fine,
        'dpsi_dr': dpsi_fine,
        'acceleration': acceleration,
        'u_EM': u_EM_fine,
        'force_density': force_density,
        'force_on_shell': force_integral,
        'params': params,
        'sol': sol,
    }


# ============================================================
# Plotting
# ============================================================
def plot_radial_solution(result, save_prefix='radial'):
    """
    Produce publication-quality plots of the radial solution.
    """
    r = result['r']
    psi = result['psi']
    dpsi = result['dpsi_dr']
    acc = result['acceleration']
    u_EM = result['u_EM']
    fd = result['force_density']
    p = result['params']

    R1, R2 = p['R1'], p['R2']
    E = p['E_stored']

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        f'DFD Psi-Bubble Radial Solution\n'
        f'E_stored = {E:.1e} J, N_coh = {p["N_coh"]:.1e}, '
        f'env = {p["environment"]}',
        fontsize=13
    )

    # Panel 1: psi(r)
    ax = axes[0, 0]
    ax.plot(r, psi, 'b-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$\psi(r)$ [dimensionless]')
    ax.set_title('Gravitational Potential')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: dpsi/dr
    ax = axes[0, 1]
    ax.plot(r, dpsi, 'r-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$d\psi/dr$ [m$^{-1}$]')
    ax.set_title('Potential Gradient')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: acceleration
    ax = axes[1, 0]
    ax.plot(r, acc, 'g-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$a(r)$ [m/s$^2$]')
    ax.set_title('Gravitational Acceleration')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 4: EM energy density and force density
    ax = axes[1, 1]
    ax2 = ax.twinx()
    l1, = ax.plot(r, u_EM, 'b-', linewidth=1.5, label=r'$u_{EM}$')
    l2, = ax2.plot(r, fd, 'r--', linewidth=1.5, label='Force density')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$u_{EM}$ [J/m$^3$]', color='b')
    ax2.set_ylabel('Force density [N/m$^3$]', color='r')
    ax.set_title('EM Energy & Force Density')
    ax.legend(handles=[l1, l2], loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = f'{save_prefix}_E{E:.0e}_N{p["N_coh"]:.0e}.png'
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")
    return fname


# ============================================================
# Quick test
# ============================================================
if __name__ == '__main__':
    print("=" * 60)
    print("DFD Radial Solver -- Quick Test")
    print("=" * 60)

    # Test with 1 GJ stored energy and moderate coherence
    for E in [1e6, 1e9]:
        for N in [1.0, 1e12]:
            print(f"\nE_stored = {E:.1e} J, N_coh = {N:.1e}")
            result = solve_radial_psi(E_stored=E, N_coh=N)
            print(f"  Force on shell = {result['force_on_shell']:.4e} N")
            print(f"  Max |acceleration| = {np.max(np.abs(result['acceleration'])):.4e} m/s^2")
            print(f"  psi at center = {result['psi'][0]:.6e}")
            print(f"  psi at edge   = {result['psi'][-1]:.6e}")
            plot_radial_solution(result,
                save_prefix='/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/simulations/radial')
