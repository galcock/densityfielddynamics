"""
asymmetric_solver.py -- Asymmetric Perturbation Solver (l=1 Spherical Harmonic)
================================================================================

Extends the radial solver to include the l=1 dipole perturbation that produces
net directed thrust.

PHYSICS:
    For a psi-bubble with an ASYMMETRIC electromagnetic energy distribution,
    we expand in spherical harmonics:

        psi(r, theta) = psi_0(r) + psi_1(r) * cos(theta) + ...

    where psi_0(r) is the spherically symmetric background (from radial_solver)
    and psi_1(r) is the l=1 dipole perturbation.

    Similarly for the EM energy density:
        u_EM(r, theta) = u_0(r) + u_1(r) * cos(theta) + ...

    The l=1 radial equation is:
        (1/r^2) d/dr [r^2 d(psi_1)/dr] - 2*psi_1/r^2 = kappa * N * u_1(r) * mu'

    where the -2*psi_1/r^2 term comes from l(l+1)/r^2 with l=1.

    The NET THRUST FORCE along the z-axis is:
        F_z = -(4*pi/3) * integral[ r^2 * u_1(r) * dpsi_0/dr ] dr
              (plus cross terms involving psi_1 and u_0)

    This is the key result: asymmetric EM loading produces net directed force.
"""

import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from constants import (c, G, kappa_DFD, a0_MOND, N_coh_default,
                       R_inner, R_outer, eps0, mu0)
from radial_solver import solve_radial_psi, mu_MOND


# ============================================================
# Asymmetric EM energy density: l=1 component
# ============================================================
def u_EM_dipole(r, E_stored, R1, R2, asymmetry=0.1):
    """
    The l=1 (dipole) component of the EM energy density.

    We model a shell where the EM energy is shifted toward one pole:
        u(r, theta) = u_0(r) [1 + asymmetry * cos(theta)]

    The l=1 projection is:
        u_1(r) = asymmetry * u_0(r)

    Parameters:
        asymmetry : fractional dipole asymmetry (0 to 1)
                    Physical realization: offset the ferrite shell,
                    or use a rotating EM mode with broken symmetry.
    """
    V_shell = (4.0 / 3.0) * np.pi * (R2**3 - R1**3)
    u_0 = np.where((r >= R1) & (r <= R2), E_stored / V_shell, 0.0)
    u_1 = asymmetry * u_0
    return u_1


# ============================================================
# ODE system for l=1 perturbation
# ============================================================
def ode_l1(r, y, params):
    """
    BVP ODE for the l=1 radial perturbation equation.

    y[0] = psi_1(r)
    y[1] = dpsi_1/dr

    Equation:
        d^2(psi_1)/dr^2 + (2/r) d(psi_1)/dr - 2*psi_1/r^2 = source_1(r)

    where source_1 = kappa * N * u_1(r) * mu_eff
    and mu_eff accounts for the MOND derivative coupling.
    """
    psi_1 = y[0]
    dpsi_1 = y[1]

    N_coh = params['N_coh']
    u1_func = params['u1_func']
    dpsi0_func = params['dpsi0_func']

    u1 = u1_func(r)
    dpsi0 = dpsi0_func(r)

    # MOND derivative coupling:
    # mu(x) = x/(1+x), so mu'(x) = 1/(1+x)^2
    # The linearized l=1 equation gets mu evaluated at the background gradient
    mu_val = mu_MOND(dpsi0)

    # Source term for l=1
    source = kappa_DFD * N_coh * u1 * mu_val

    # l=1 radial equation: d^2/dr^2 + (2/r) d/dr - l(l+1)/r^2 = source
    # with l=1: l(l+1) = 2
    safe_r = np.where(r > 1e-10, r, 1e-10)
    d2psi1 = source - (2.0 / safe_r) * dpsi_1 + (2.0 / safe_r**2) * psi_1

    return np.vstack([dpsi_1, d2psi1])


def bc_l1(ya, yb, params):
    """
    Boundary conditions for l=1:
        At r_min: psi_1 ~ r  (regular at origin) => psi_1 / r -> const, so psi_1(r_min) ~ 0
        At r_max: psi_1 ~ 1/r^2  (decaying dipole) => psi_1(r_max) ~ 0
    """
    return np.array([
        ya[0],    # psi_1(r_min) = 0
        yb[0],    # psi_1(r_max) = 0
    ])


# ============================================================
# Thrust calculator
# ============================================================
def compute_thrust(r, psi_0, dpsi_0, psi_1, dpsi_1, u_0, u_1, N_coh):
    """
    Compute the net z-directed thrust from the l=1 perturbation.

    The thrust arises from the cross-coupling between the asymmetric
    EM field and the gravitational potential gradient:

        F_z = -(4*pi/3) * c^2 * N_coh * integral[
            r^2 * (u_1 * dpsi_0 + u_0 * dpsi_1) * mu
        ] dr

    The (4*pi/3) comes from the angular integration of cos(theta)
    over the sphere: integral sin(theta) cos^2(theta) dtheta dphi = 4*pi/3

    Returns:
        F_z : net thrust [N]
    """
    mu_vals = mu_MOND(dpsi_0)
    dr = np.gradient(r)

    # Cross terms: u_1 * dpsi_0/dr  and  u_0 * dpsi_1/dr
    integrand = r**2 * (u_1 * dpsi_0 + u_0 * dpsi_1) * mu_vals

    F_z = -(4.0 * np.pi / 3.0) * N_coh * kappa_DFD * c**2 * np.sum(integrand * dr)

    return F_z


# ============================================================
# Main asymmetric solver
# ============================================================
def solve_asymmetric(E_stored, asymmetry=0.1, R1=R_inner, R2=R_outer,
                     N_coh=N_coh_default, r_min=0.01, r_max=50.0,
                     N_grid=500, environment='earth_orbit'):
    """
    Solve for the l=1 dipole perturbation and compute net thrust.

    Steps:
    1. Solve the radial (l=0) background using radial_solver
    2. Compute the l=1 source from asymmetric EM distribution
    3. Solve the l=1 ODE
    4. Compute thrust from cross-coupling

    Returns:
        dict with: r, psi_0, psi_1, dpsi_0, dpsi_1, u_0, u_1,
                   thrust_N, thrust_per_energy, radial_result
    """
    # Step 1: Solve background
    rad = solve_radial_psi(E_stored=E_stored, R1=R1, R2=R2, N_coh=N_coh,
                           r_min=r_min, r_max=r_max, N_grid=N_grid,
                           environment=environment)

    r = rad['r']
    psi_0 = rad['psi']
    dpsi_0 = rad['dpsi_dr']
    u_0 = rad['u_EM']

    # Step 2: l=1 EM source
    u_1 = u_EM_dipole(r, E_stored, R1, R2, asymmetry=asymmetry)

    # Interpolation functions for the BVP solver
    u1_func = interp1d(r, u_1, kind='linear', bounds_error=False, fill_value=0.0)
    dpsi0_func = interp1d(r, dpsi_0, kind='linear', bounds_error=False, fill_value=0.0)

    params = {
        'N_coh': N_coh,
        'u1_func': u1_func,
        'dpsi0_func': dpsi0_func,
    }

    # Step 3: Solve l=1 BVP
    r_grid = np.linspace(r_min, r_max, N_grid)
    y_init = np.zeros((2, N_grid))

    def ode_wrapped(rv, yv):
        return ode_l1(rv, yv, params)

    def bc_wrapped(ya, yb):
        return bc_l1(ya, yb, params)

    sol = solve_bvp(ode_wrapped, bc_wrapped, r_grid, y_init,
                    tol=1e-8, max_nodes=5000)

    if not sol.success:
        print(f"WARNING: l=1 BVP solver did not converge: {sol.message}")

    psi_1 = sol.sol(r)[0]
    dpsi_1 = sol.sol(r)[1]

    # Step 4: Compute thrust
    F_z = compute_thrust(r, psi_0, dpsi_0, psi_1, dpsi_1, u_0, u_1, N_coh)

    return {
        'r': r,
        'psi_0': psi_0,
        'psi_1': psi_1,
        'dpsi_0': dpsi_0,
        'dpsi_1': dpsi_1,
        'u_0': u_0,
        'u_1': u_1,
        'thrust_N': F_z,
        'thrust_per_energy': F_z / E_stored if E_stored > 0 else 0.0,
        'asymmetry': asymmetry,
        'radial_result': rad,
        'params': rad['params'],
    }


# ============================================================
# Plotting
# ============================================================
def plot_asymmetric_solution(result, save_prefix='asymmetric'):
    """Plot the l=1 perturbation and thrust calculation."""
    r = result['r']
    psi_1 = result['psi_1']
    dpsi_1 = result['dpsi_1']
    u_1 = result['u_1']
    p = result['params']
    R1, R2 = p['R1'], p['R2']

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle(
        f'DFD Asymmetric (l=1) Perturbation\n'
        f'E = {p["E_stored"]:.1e} J, N_coh = {p["N_coh"]:.1e}, '
        f'asymmetry = {result["asymmetry"]:.2f}, '
        f'Thrust = {result["thrust_N"]:.3e} N',
        fontsize=12
    )

    # Panel 1: psi_1(r)
    ax = axes[0]
    ax.plot(r, psi_1, 'b-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$\psi_1(r)$')
    ax.set_title('Dipole Potential Perturbation')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: dpsi_1/dr
    ax = axes[1]
    ax.plot(r, dpsi_1, 'r-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$d\psi_1/dr$')
    ax.set_title('Dipole Gradient')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: u_1(r)
    ax = axes[2]
    ax.plot(r, u_1, 'g-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel(r'$u_1(r)$ [J/m$^3$]')
    ax.set_title('Dipole EM Energy Density')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    E = p['E_stored']
    fname = f'{save_prefix}_E{E:.0e}_N{p["N_coh"]:.0e}.png'
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")
    return fname


# ============================================================
# Quick test
# ============================================================
if __name__ == '__main__':
    import os
    os.chdir('/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/simulations')

    print("=" * 60)
    print("DFD Asymmetric Solver -- Quick Test")
    print("=" * 60)

    for E in [1e6, 1e9]:
        for N in [1.0, 1e12]:
            print(f"\nE_stored = {E:.1e} J, N_coh = {N:.1e}")
            result = solve_asymmetric(E_stored=E, N_coh=N, asymmetry=0.1)
            print(f"  Thrust = {result['thrust_N']:.4e} N")
            print(f"  Thrust/Energy = {result['thrust_per_energy']:.4e} N/J")
            plot_asymmetric_solution(result, save_prefix='asymmetric')
