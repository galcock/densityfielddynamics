"""
self_consistency.py -- Self-Consistency Iteration Loop
======================================================

Implements the iterative self-consistency check for the DFD psi-bubble.

PHYSICS:
    The EM fields and the gravitational potential psi are coupled:

    1. EM fields in the shell depend on material properties eps(r), mu(r)
    2. Material properties are modified by the gravitational potential psi
       (through DFD's metric-matter coupling)
    3. psi is sourced by the EM energy density u_EM

    This creates a self-consistency loop:

    Step 0: Start with unperturbed material properties
    Step 1: Compute EM fields -> u_EM(r)
    Step 2: Solve DFD equation: psi(r) from u_EM(r)
    Step 3: Compute modified material properties:
            eps_eff(r) = eps_r * (1 + 2*psi(r))   [gravitational redshift correction]
            mu_eff(r)  = mu_r  * (1 + 2*psi(r))   [magnetic permeability correction]
    Step 4: Recompute EM fields with modified eps, mu
    Step 5: Iterate until convergence

    The convergence criterion is:
        max |psi^(n+1)(r) - psi^(n)(r)| < tolerance

    CRITICAL QUESTION: Does this iteration converge?
    - For weak fields (kappa * u * R^2 << 1): YES, perturbative regime
    - For strong fields: may diverge -> indicates onset of nonlinear instability
    - The divergence threshold gives the maximum useful stored energy
"""

import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from constants import (c, G, kappa_DFD, R_inner, R_outer,
                       eps_r_ferrite, mu_r_ferrite, N_coh_default)
from radial_solver import solve_radial_psi, u_EM_profile


# ============================================================
# Modified material properties under gravitational potential
# ============================================================
def modified_material_properties(r, psi, R1, R2, eps_r0, mu_r0):
    """
    Compute the effective material properties modified by the gravitational
    potential psi(r).

    In DFD, the metric g_00 = -(1 + 2*psi) modifies the local physics:
        - Effective permittivity: eps_eff = eps_r * (1 + 2*psi)
          (because the local speed of light is c_local = c * sqrt(1+2*psi))
        - Effective permeability: mu_eff = mu_r * (1 + 2*psi)

    For a superconductor, the London penetration depth is also modified:
        lambda_L_eff = lambda_L / sqrt(1 + 2*psi)

    These corrections are tiny for realistic psi (~ 10^-30 to 10^-10)
    but the iteration tests whether the system is self-consistent.

    Parameters:
        r       : radial coordinate array
        psi     : gravitational potential (dimensionless)
        R1, R2  : shell boundaries
        eps_r0  : unperturbed relative permittivity
        mu_r0   : unperturbed relative permeability

    Returns:
        eps_eff(r), mu_eff(r) : modified properties (arrays)
    """
    in_shell = (r >= R1) & (r <= R2)

    # Metric correction factor
    metric_factor = 1.0 + 2.0 * psi

    # Ensure physical (positive) values
    metric_factor = np.clip(metric_factor, 0.01, 10.0)

    eps_eff = np.where(in_shell, eps_r0 * metric_factor, 1.0)
    mu_eff = np.where(in_shell, mu_r0 * metric_factor, 1.0)

    return eps_eff, mu_eff


def compute_modified_energy_density(r, E_stored, R1, R2, eps_eff, mu_eff):
    """
    Recompute the EM energy density with modified material properties.

    For a cavity mode with fixed total energy E_stored:
        u_EM(r) ~ 1/V_eff  where V_eff depends on eps, mu

    The energy density in a dielectric/magnetic medium is:
        u = (eps_0 * eps_r * |E|^2 + |B|^2 / (mu_0 * mu_r)) / 2

    For a fixed-frequency mode, modifying eps, mu changes the field distribution.
    To first order, the energy density scales as:
        u_modified ~ u_original * (eps_eff * mu_eff) / (eps_r0 * mu_r0)

    (This is a simplified model; a full treatment would re-solve Maxwell's equations.)
    """
    V_shell = (4.0 / 3.0) * np.pi * (R2**3 - R1**3)
    in_shell = (r >= R1) & (r <= R2)

    # Base uniform energy density
    u_base = np.where(in_shell, E_stored / V_shell, 0.0)

    # Modification factor: ratio of effective to unperturbed product
    eps_r0 = eps_r_ferrite
    mu_r0 = mu_r_ferrite

    ratio = np.where(in_shell,
                     (eps_eff * mu_eff) / (eps_r0 * mu_r0),
                     1.0)

    u_modified = u_base * ratio

    # Renormalize to maintain total stored energy
    dr = np.gradient(r)
    total = np.sum(u_modified * 4.0 * np.pi * r**2 * dr)
    if total > 0:
        u_modified *= E_stored / total

    return u_modified


# ============================================================
# Self-Consistency Iteration
# ============================================================
def self_consistency_loop(E_stored, N_coh=N_coh_default, R1=R_inner, R2=R_outer,
                          max_iter=20, tol=1e-12, r_min=0.01, r_max=50.0,
                          N_grid=500, environment='earth_orbit',
                          verbose=True):
    """
    Run the self-consistency iteration loop.

    Returns:
        dict with: converged (bool), iterations, psi_history,
                   convergence_history, final_result, material_history
    """
    if verbose:
        print(f"\nSelf-Consistency Loop: E={E_stored:.1e} J, N_coh={N_coh:.1e}")
        print(f"  R1={R1:.2f} m, R2={R2:.2f} m, env={environment}")

    # Initialize
    eps_r_current = eps_r_ferrite
    mu_r_current = mu_r_ferrite

    psi_history = []
    convergence_history = []
    material_history = []
    force_history = []

    psi_prev = None

    for iteration in range(max_iter):
        if verbose:
            print(f"  Iteration {iteration + 1}:")

        # Solve the DFD equation with current material properties
        result = solve_radial_psi(E_stored=E_stored, R1=R1, R2=R2,
                                  N_coh=N_coh, r_min=r_min, r_max=r_max,
                                  N_grid=N_grid, environment=environment)

        r = result['r']
        psi = result['psi']
        dpsi = result['dpsi_dr']

        psi_history.append(psi.copy())
        force_history.append(result['force_on_shell'])

        # Check convergence
        if psi_prev is not None:
            diff = np.max(np.abs(psi - psi_prev))
            convergence_history.append(diff)
            if verbose:
                print(f"    max |delta psi| = {diff:.4e}")
                print(f"    force on shell  = {result['force_on_shell']:.4e} N")

            if diff < tol:
                if verbose:
                    print(f"  CONVERGED after {iteration + 1} iterations!")
                return {
                    'converged': True,
                    'iterations': iteration + 1,
                    'psi_history': psi_history,
                    'convergence_history': convergence_history,
                    'force_history': force_history,
                    'material_history': material_history,
                    'final_result': result,
                    'r': r,
                }
        else:
            convergence_history.append(np.max(np.abs(psi)))
            if verbose:
                print(f"    max |psi| = {np.max(np.abs(psi)):.4e}")
                print(f"    force on shell = {result['force_on_shell']:.4e} N")

        psi_prev = psi.copy()

        # Update material properties based on psi
        eps_eff, mu_eff = modified_material_properties(
            r, psi, R1, R2, eps_r_ferrite, mu_r_ferrite)

        material_history.append({
            'eps_eff_max': np.max(eps_eff),
            'eps_eff_min': np.min(eps_eff[(r >= R1) & (r <= R2)]) if np.any((r >= R1) & (r <= R2)) else 1.0,
            'mu_eff_max': np.max(mu_eff),
        })

        # Check for divergence
        if len(convergence_history) > 2:
            if convergence_history[-1] > convergence_history[-2] * 10:
                if verbose:
                    print(f"  DIVERGING after {iteration + 1} iterations!")
                return {
                    'converged': False,
                    'iterations': iteration + 1,
                    'psi_history': psi_history,
                    'convergence_history': convergence_history,
                    'force_history': force_history,
                    'material_history': material_history,
                    'final_result': result,
                    'r': r,
                    'divergence_detected': True,
                }

    if verbose:
        print(f"  Did not converge in {max_iter} iterations.")

    return {
        'converged': False,
        'iterations': max_iter,
        'psi_history': psi_history,
        'convergence_history': convergence_history,
        'force_history': force_history,
        'material_history': material_history,
        'final_result': result,
        'r': r,
        'divergence_detected': False,
    }


# ============================================================
# Convergence study across energy scales
# ============================================================
def convergence_study(save_dir='.'):
    """
    Run self-consistency for a range of stored energies and report
    whether the iteration converges or diverges.
    """
    print("=" * 60)
    print("Self-Consistency Convergence Study")
    print("=" * 60)

    E_range = np.logspace(3, 15, 13)  # 1 kJ to 1 PJ
    N_coh_values = [1.0, 1e12]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax_idx, N_coh in enumerate(N_coh_values):
        ax = axes[ax_idx]
        converged_E = []
        diverged_E = []

        for E in E_range:
            result = self_consistency_loop(
                E_stored=E, N_coh=N_coh, max_iter=10, tol=1e-14,
                N_grid=300, verbose=False)

            if result['converged']:
                converged_E.append(E)
            else:
                diverged_E.append(E)

            # Plot convergence history
            if len(result['convergence_history']) > 1:
                iters = range(1, len(result['convergence_history']) + 1)
                style = '-' if result['converged'] else '--'
                ax.semilogy(list(iters), result['convergence_history'],
                            f'o{style}', markersize=4,
                            label=f'E={E:.0e} J')

        ax.set_xlabel('Iteration')
        ax.set_ylabel(r'max $|\Delta\psi|$')
        ax.set_title(f'Self-Consistency Convergence\n$N_{{coh}}$ = {N_coh:.0e}')
        ax.legend(fontsize=7, ncol=2)
        ax.grid(True, alpha=0.3)

        if converged_E:
            ax.annotate(f'Converged: E <= {max(converged_E):.0e} J',
                        xy=(0.05, 0.95), xycoords='axes fraction',
                        fontsize=9, color='green', va='top')
        if diverged_E:
            ax.annotate(f'Diverged: E >= {min(diverged_E):.0e} J',
                        xy=(0.05, 0.88), xycoords='axes fraction',
                        fontsize=9, color='red', va='top')

    plt.tight_layout()
    fname = f'{save_dir}/self_consistency_convergence.png'
    plt.savefig(fname)
    plt.close()
    print(f"Saved: {fname}")
    return fname


# ============================================================
# Quick test
# ============================================================
if __name__ == '__main__':
    convergence_study('/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/simulations')
