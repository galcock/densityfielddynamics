"""
em_modes.py -- Rotating Mode EM Field Calculator for Ferrite Shell
==================================================================

Calculates the electromagnetic fields in a spherical ferrite shell for the
lowest rotating (m != 0) modes.

PHYSICS:
    We solve the vector Helmholtz equation inside a spherical dielectric/magnetic
    shell with inner radius R1, outer radius R2:

        curl curl E = omega^2 * eps * mu * E

    For TE modes in a spherical shell with l=1, m=1 (rotating dipole mode):
        The fields rotate around the z-axis, creating a non-zero angular momentum
        and an asymmetric energy distribution.

    For a spherical shell with step-function eps_r, mu_r:
    - Region I   (r < R1):    eps_r=1, mu_r=1  (vacuum/superconductor interior)
    - Region II  (R1 < r < R2): eps_r, mu_r     (ferrite)
    - Region III (r > R2):    eps_r=1, mu_r=1  (vacuum exterior -- bounded by SC)

    We use the standard spherical Bessel function decomposition.

    The eigenvalue equation determines the resonant frequency omega.
    The energy density for the rotating mode provides the asymmetric source
    for the psi-solver.
"""

import numpy as np
from scipy.special import spherical_jn, spherical_yn
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from constants import (c, eps0, mu0, eps_r_ferrite, mu_r_ferrite,
                       R_inner, R_outer)


# ============================================================
# Spherical Bessel functions and their derivatives
# ============================================================
def j_l(l, x):
    """Spherical Bessel function of the first kind, j_l(x)."""
    return spherical_jn(l, x)

def y_l(l, x):
    """Spherical Bessel function of the second kind, y_l(x)."""
    return spherical_yn(l, x)

def j_l_prime(l, x):
    """Derivative of j_l: d/dx [x * j_l(x)] / x = j_l + x * j_l'."""
    return spherical_jn(l, x, derivative=True)

def y_l_prime(l, x):
    """Derivative of y_l."""
    return spherical_yn(l, x, derivative=True)


# ============================================================
# Eigenvalue equation for TE modes in spherical shell
# ============================================================
def eigenvalue_equation_TE(omega, l, R1, R2, eps_r, mu_r):
    """
    The eigenvalue (resonance) condition for TE_l modes in a spherical
    dielectric/magnetic shell.

    For a shell with perfectly conducting boundaries at R1 (inner SC) and R2 (outer SC):
        E_tangential = 0 at r = R1 and r = R2

    For TE modes, the radial function f(r) satisfies:
        d/dr[r * f(r)] = 0  at r = R1, R2
        where the fields are written as E ~ f(r) * vector_harmonics

    The wavenumber inside the ferrite is:
        k = omega * sqrt(eps_r * mu_r) / c

    The eigenvalue condition for a conducting shell with ferrite filling:
        j_l'(k*R1) * y_l'(k*R2) - j_l'(k*R2) * y_l'(k*R1) = 0

    where the prime denotes d/d(kr) of [kr * z_l(kr)] / kr.

    For simplicity we use the condition on the Ricatti-Bessel functions:
        [x * j_l(x)]' evaluated at x = k*R  =>  j_l(kR) + kR * j_l'(kR)
    """
    k = omega * np.sqrt(eps_r * mu_r) / c

    x1 = k * R1
    x2 = k * R2

    # Avoid numerical issues with very small arguments
    if abs(x1) < 1e-15 or abs(x2) < 1e-15:
        return 1e10

    # Ricatti-Bessel derivative: d/dx [x * j_l(x)] = j_l(x) + x * j_l'(x)
    rj1 = j_l(l, x1) + x1 * j_l_prime(l, x1)
    ry1 = y_l(l, x1) + x1 * y_l_prime(l, x1)
    rj2 = j_l(l, x2) + x2 * j_l_prime(l, x2)
    ry2 = y_l(l, x2) + x2 * y_l_prime(l, x2)

    # Eigenvalue condition: boundary matching
    return rj1 * ry2 - rj2 * ry1


def find_resonant_frequencies(l=1, R1=R_inner, R2=R_outer,
                               eps_r=eps_r_ferrite, mu_r=mu_r_ferrite,
                               n_modes=5):
    """
    Find the lowest n_modes resonant frequencies for TE_l modes.

    We scan in omega and look for sign changes of the eigenvalue equation.
    """
    # Characteristic frequency scale: c / (R2 * sqrt(eps_r * mu_r))
    omega_scale = c / (R2 * np.sqrt(eps_r * mu_r))

    # Scan from a small fraction to many times the characteristic frequency
    omega_scan = np.linspace(0.01 * omega_scale, 20.0 * omega_scale, 10000)
    f_scan = np.array([eigenvalue_equation_TE(w, l, R1, R2, eps_r, mu_r)
                       for w in omega_scan])

    # Find sign changes
    sign_changes = np.where(np.diff(np.sign(f_scan)))[0]

    frequencies = []
    for idx in sign_changes[:n_modes * 3]:  # check more than needed
        try:
            omega_root = brentq(eigenvalue_equation_TE,
                                omega_scan[idx], omega_scan[idx + 1],
                                args=(l, R1, R2, eps_r, mu_r),
                                xtol=1e-12)
            # Verify it's not a spurious root
            if omega_root > 0:
                frequencies.append(omega_root)
        except (ValueError, RuntimeError):
            continue

    # Remove duplicates (within tolerance)
    unique_freq = []
    for f in sorted(frequencies):
        if not unique_freq or abs(f - unique_freq[-1]) / f > 1e-6:
            unique_freq.append(f)

    return unique_freq[:n_modes]


# ============================================================
# Field profiles for a given mode
# ============================================================
def em_field_profile(omega, l, m, R1, R2, eps_r, mu_r, N_r=500, N_theta=200):
    """
    Compute the EM field energy density u(r, theta) for a TE_{l,m} mode
    at resonant frequency omega.

    For the rotating mode (m != 0), the time-averaged energy density is:
        u(r, theta) = (eps * |E|^2 + mu * |H|^2) / 2

    For m=1, l=1:
        E ~ f(r) * sin(theta)  (rotating dipole in phi)
        The energy density has both r and theta dependence:
        u(r, theta) ~ |f(r)|^2 * [some function of theta involving P_l^m]

    For a rotating mode, the phi-averaged energy density retains theta dependence
    through the associated Legendre functions.

    Returns:
        r_arr, theta_arr, u_2d (energy density on r-theta grid)
        u_r (radially-averaged angular profile)
        u_theta (angularly-averaged radial profile)
    """
    k = omega * np.sqrt(eps_r * mu_r) / c
    k_vac = omega / c

    r_arr = np.linspace(0.01, R2 * 2.0, N_r)
    theta_arr = np.linspace(0.01, np.pi - 0.01, N_theta)

    # Radial function in the ferrite shell
    # f(r) = A * j_l(k*r) + B * y_l(k*r)  for R1 < r < R2
    # BC: d/d(kr) [kr * f(kr)] = 0 at r = R1
    #     => j_l(kR1) + kR1*j_l'(kR1) = -B/A * [y_l(kR1) + kR1*y_l'(kR1)]

    x1 = k * R1
    rj1_val = j_l(l, x1) + x1 * j_l_prime(l, x1)
    ry1_val = y_l(l, x1) + x1 * y_l_prime(l, x1)

    if abs(ry1_val) > 1e-30:
        B_over_A = -rj1_val / ry1_val
    else:
        B_over_A = 0.0

    def f_radial(r):
        """Radial eigenfunction (unnormalized)."""
        result = np.zeros_like(r, dtype=float)
        # Inside shell (ferrite)
        in_shell = (r >= R1) & (r <= R2)
        kr = k * r[in_shell]
        result[in_shell] = j_l(l, kr) + B_over_A * y_l(l, kr)
        # Evanescent outside (simplified -- in reality BC enforces zero at SC walls)
        # For plotting, we set fields to zero outside the shell
        return result

    # Angular function for |m| = 1, l = 1:
    # P_1^1(cos theta) = -sin(theta)
    # |Y_1^1|^2 ~ sin^2(theta)  (ignoring normalization -- we'll normalize total energy)
    def angular_factor(theta):
        if l == 1 and abs(m) == 1:
            return np.sin(theta)**2
        elif l == 1 and m == 0:
            return np.cos(theta)**2
        elif l == 2 and abs(m) == 1:
            return np.sin(theta)**2 * np.cos(theta)**2
        elif l == 2 and abs(m) == 2:
            return np.sin(theta)**4
        else:
            # Generic: use sin^(2|m|)(theta) as approximation
            return np.sin(theta)**(2 * abs(m))

    # Build 2D energy density (unnormalized)
    R, THETA = np.meshgrid(r_arr, theta_arr, indexing='ij')
    f_r = f_radial(r_arr)
    a_theta = angular_factor(theta_arr)

    # u(r,theta) ~ |f(r)|^2 * angular(theta)
    # Use eps_r, mu_r inside the shell for the energy density
    u_2d = np.outer(f_r**2, a_theta)

    # Apply material properties
    eps_profile = np.where((r_arr >= R1) & (r_arr <= R2), eps_r, 1.0)
    u_2d *= eps_profile[:, np.newaxis]  # weight by permittivity

    return r_arr, theta_arr, u_2d, f_r, a_theta


def normalize_energy_density(r_arr, theta_arr, u_2d, E_total):
    """
    Normalize the 2D energy density so that the total stored energy
    equals E_total.

    integral u(r,theta) * 2*pi*r^2 * sin(theta) dr dtheta = E_total
    """
    dr = np.gradient(r_arr)
    dtheta = np.gradient(theta_arr)

    # Volume integral
    integrand = np.zeros_like(u_2d)
    for i in range(len(r_arr)):
        for j in range(len(theta_arr)):
            integrand[i, j] = u_2d[i, j] * 2.0 * np.pi * r_arr[i]**2 * np.sin(theta_arr[j])

    total = np.sum(integrand * np.outer(dr, dtheta))

    if total > 0:
        return u_2d * (E_total / total)
    else:
        return u_2d


def extract_multipole_components(r_arr, theta_arr, u_2d):
    """
    Extract the l=0 and l=1 radial components from the 2D energy density.

    u_0(r) = (1/2) * integral u(r,theta) * sin(theta) dtheta
    u_1(r) = (3/2) * integral u(r,theta) * cos(theta) * sin(theta) dtheta

    These feed into the radial and asymmetric solvers respectively.
    """
    dtheta = np.gradient(theta_arr)
    sin_theta = np.sin(theta_arr)
    cos_theta = np.cos(theta_arr)

    u_0 = np.zeros(len(r_arr))
    u_1 = np.zeros(len(r_arr))

    for i in range(len(r_arr)):
        u_0[i] = 0.5 * np.sum(u_2d[i, :] * sin_theta * dtheta)
        u_1[i] = 1.5 * np.sum(u_2d[i, :] * cos_theta * sin_theta * dtheta)

    return u_0, u_1


# ============================================================
# Plotting
# ============================================================
def plot_em_modes(r_arr, theta_arr, u_2d, f_r, frequencies, l, m,
                  R1, R2, save_prefix='em_mode'):
    """Plot the EM mode structure."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle(
        f'EM Rotating Mode (l={l}, m={m})\n'
        f'R1={R1:.1f} m, R2={R2:.1f} m, '
        f'f_res = {frequencies[0]/(2*np.pi):.3e} Hz',
        fontsize=12
    )

    # Panel 1: Radial eigenfunction
    ax = axes[0]
    ax.plot(r_arr, f_r, 'b-', linewidth=1.5)
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Ferrite shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel('f(r) [arb. units]')
    ax.set_title('Radial Eigenfunction')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: 2D energy density (r-theta map)
    ax = axes[1]
    # Convert to Cartesian for polar-like plot
    R, THETA = np.meshgrid(r_arr, theta_arr, indexing='ij')
    X = R * np.sin(THETA)
    Z = R * np.cos(THETA)

    # Clip to shell region for better visualization
    shell_mask = (R >= R1 * 0.8) & (R <= R2 * 1.2)
    u_plot = np.where(shell_mask, u_2d, 0)
    u_plot = np.where(u_plot > 0, u_plot, np.nan)

    cs = ax.pcolormesh(X, Z, u_plot, shading='auto', cmap='hot')
    plt.colorbar(cs, ax=ax, label='u [arb.]')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('z [m]')
    ax.set_title('Energy Density u(r, theta)')
    ax.set_aspect('equal')

    # Panel 3: Multipole decomposition
    ax = axes[2]
    u_0, u_1 = extract_multipole_components(r_arr, theta_arr, u_2d)
    ax.plot(r_arr, u_0, 'b-', linewidth=1.5, label=r'$u_0(r)$ (monopole)')
    ax.plot(r_arr, u_1, 'r--', linewidth=1.5, label=r'$u_1(r)$ (dipole)')
    ax.axvspan(R1, R2, alpha=0.15, color='orange', label='Shell')
    ax.set_xlabel('r [m]')
    ax.set_ylabel('u [arb.]')
    ax.set_title('Multipole Components')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = f'{save_prefix}_l{l}_m{m}.png'
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
    print("EM Mode Calculator -- Finding resonant frequencies")
    print("=" * 60)

    for l_mode in [1, 2]:
        freqs = find_resonant_frequencies(l=l_mode, n_modes=3)
        print(f"\nTE_{l_mode} modes:")
        for i, omega in enumerate(freqs):
            f_Hz = omega / (2 * np.pi)
            wavelength = c / f_Hz
            print(f"  Mode {i+1}: f = {f_Hz:.3e} Hz, lambda = {wavelength:.3f} m, "
                  f"omega = {omega:.3e} rad/s")

    # Plot the lowest rotating mode (l=1, m=1)
    freqs = find_resonant_frequencies(l=1, n_modes=3)
    if freqs:
        r_arr, theta_arr, u_2d, f_r, a_theta = em_field_profile(
            freqs[0], l=1, m=1, R1=R_inner, R2=R_outer,
            eps_r=eps_r_ferrite, mu_r=mu_r_ferrite
        )
        plot_em_modes(r_arr, theta_arr, u_2d, f_r, freqs,
                      l=1, m=1, R1=R_inner, R2=R_outer,
                      save_prefix='em_mode')
    else:
        print("No resonant frequencies found for l=1. Check parameter ranges.")
