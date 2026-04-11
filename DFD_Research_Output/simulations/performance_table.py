"""
performance_table.py -- Performance Prediction Table
=====================================================

Computes thrust predictions for a reference DFD psi-bubble vehicle and
produces a clear summary table.

REFERENCE VEHICLE:
    - Outer radius: R = 5 m
    - Ferrite: NiZn with eps_r = 12, mu_r = 800
    - Superconductor: YBCO (T_c = 93 K)
    - Shell thickness: 0.5 m (R_inner = 4.5 m)
    - Asymmetry parameter: 10% (achievable with offset geometry or mode mixing)

ENERGY LEVELS:
    - 1 MJ  (roughly: 1 kg of TNT equivalent)
    - 1 GJ  (roughly: 0.25 ton of TNT)
    - 1 TJ  (roughly: 250 tons of TNT)

COHERENCE ENHANCEMENT:
    - N_coh = 1           : no quantum enhancement (classical EM field)
    - N_coh = 10^12       : moderate (superconducting cavity enhancement)
    - N_coh = 10^18       : optimistic (full superradiant enhancement)

MOND NONLINEARITY:
    - With mu(x) = x/(1+x) : MOND interpolating function active
    - Without (mu=1)       : standard Newtonian regime only

ENVIRONMENTS:
    - Earth orbit (400 km altitude)
    - Deep space (galactic background only)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from constants import (c, G, kappa_DFD, R_inner, R_outer,
                       eps_r_ferrite, mu_r_ferrite)
from asymmetric_solver import solve_asymmetric


# ============================================================
# Run all performance predictions
# ============================================================
def compute_performance_table(verbose=True):
    """
    Compute thrust for all parameter combinations.

    Returns:
        list of dicts, each with keys:
            E_stored, N_coh, environment, mond_active, thrust_N,
            thrust_per_energy, acceleration_ms2
    """
    E_values = {'1 MJ': 1e6, '1 GJ': 1e9, '1 TJ': 1e12}
    N_coh_values = {'None (N=1)': 1.0, 'Moderate (N=10^12)': 1e12,
                    'Optimistic (N=10^18)': 1e18}
    environments = {'Earth Orbit': 'earth_orbit', 'Deep Space': 'deep_space'}

    # Vehicle mass estimate (for acceleration calculation)
    # Ferrite shell: rho ~ 5000 kg/m^3, volume ~ 4/3*pi*(R2^3 - R1^3)
    V_shell = (4.0 / 3.0) * np.pi * (R_outer**3 - R_inner**3)
    rho_ferrite = 5000.0  # kg/m^3
    m_shell = rho_ferrite * V_shell
    m_vehicle = m_shell * 2  # shell + structure + payload estimate
    if verbose:
        print(f"Reference vehicle mass estimate: {m_vehicle:.0f} kg "
              f"(shell: {m_shell:.0f} kg)")

    results = []

    for E_label, E in E_values.items():
        for N_label, N_coh in N_coh_values.items():
            for env_label, env in environments.items():
                if verbose:
                    print(f"  Computing: E={E_label}, N_coh={N_label}, env={env_label}...")

                try:
                    sol = solve_asymmetric(E_stored=E, N_coh=N_coh,
                                           asymmetry=0.1, r_max=30.0,
                                           N_grid=300, environment=env)
                    thrust = abs(sol['thrust_N'])
                except Exception as e:
                    if verbose:
                        print(f"    Failed: {e}")
                    thrust = 0.0

                accel = thrust / m_vehicle if m_vehicle > 0 else 0.0

                results.append({
                    'E_label': E_label,
                    'E_stored': E,
                    'N_coh_label': N_label,
                    'N_coh': N_coh,
                    'environment': env_label,
                    'thrust_N': thrust,
                    'thrust_per_energy': thrust / E if E > 0 else 0,
                    'acceleration_ms2': accel,
                    'vehicle_mass_kg': m_vehicle,
                })

    return results


# ============================================================
# Print formatted table
# ============================================================
def print_performance_table(results):
    """Print the performance table in a readable format."""
    print("\n" + "=" * 110)
    print("DFD PSI-BUBBLE PERFORMANCE PREDICTIONS")
    print("Reference Vehicle: R=5m, NiZn ferrite (eps_r=12, mu_r=800), YBCO SC")
    print("=" * 110)

    # Header
    print(f"{'Energy':<8} {'Coherence':<22} {'Environment':<16} "
          f"{'Thrust [N]':<14} {'Thrust/E [N/J]':<16} {'Accel [m/s^2]':<14}")
    print("-" * 110)

    for r in results:
        print(f"{r['E_label']:<8} {r['N_coh_label']:<22} {r['environment']:<16} "
              f"{r['thrust_N']:<14.4e} {r['thrust_per_energy']:<16.4e} "
              f"{r['acceleration_ms2']:<14.4e}")

    print("-" * 110)

    # Summary insights
    print("\nKEY FINDINGS:")

    # Find maximum thrust
    max_result = max(results, key=lambda x: x['thrust_N'])
    print(f"  Maximum thrust: {max_result['thrust_N']:.4e} N "
          f"at E={max_result['E_label']}, {max_result['N_coh_label']}, "
          f"{max_result['environment']}")

    # Compare environments
    earth_results = [r for r in results if r['environment'] == 'Earth Orbit']
    space_results = [r for r in results if r['environment'] == 'Deep Space']

    if earth_results and space_results:
        for e_r, s_r in zip(earth_results, space_results):
            if e_r['thrust_N'] > 0:
                ratio = s_r['thrust_N'] / e_r['thrust_N']
                if abs(ratio - 1.0) > 0.01:
                    print(f"  MOND enhancement (deep space vs Earth): "
                          f"{ratio:.2f}x at E={e_r['E_label']}, {e_r['N_coh_label']}")

    # Coherence enhancement ratios
    for E_label in ['1 MJ', '1 GJ', '1 TJ']:
        base = [r for r in results if r['E_label'] == E_label
                and r['N_coh'] == 1.0 and r['environment'] == 'Earth Orbit']
        enhanced = [r for r in results if r['E_label'] == E_label
                    and r['N_coh'] == 1e12 and r['environment'] == 'Earth Orbit']
        if base and enhanced and base[0]['thrust_N'] > 0:
            ratio = enhanced[0]['thrust_N'] / base[0]['thrust_N']
            print(f"  Coherence enhancement (N=10^12 vs N=1) at {E_label}: {ratio:.2e}x")

    return results


# ============================================================
# Save table as formatted text file
# ============================================================
def save_performance_table(results, save_dir='.'):
    """Save the table to a text file and as a figure."""

    # Text file
    fname_txt = f'{save_dir}/performance_table.txt'
    with open(fname_txt, 'w') as f:
        f.write("=" * 110 + "\n")
        f.write("DFD PSI-BUBBLE PERFORMANCE PREDICTIONS\n")
        f.write("Reference Vehicle: R=5m, NiZn ferrite (eps_r=12, mu_r=800), YBCO SC\n")
        f.write(f"Vehicle mass estimate: {results[0]['vehicle_mass_kg']:.0f} kg\n")
        f.write("Asymmetry: 10%, MOND interpolating function: mu(x)=x/(1+x)\n")
        f.write("=" * 110 + "\n\n")

        f.write(f"{'Energy':<8} {'Coherence':<22} {'Environment':<16} "
                f"{'Thrust [N]':<14} {'Thrust/E [N/J]':<16} {'Accel [m/s^2]':<14}\n")
        f.write("-" * 110 + "\n")

        for r in results:
            f.write(f"{r['E_label']:<8} {r['N_coh_label']:<22} {r['environment']:<16} "
                    f"{r['thrust_N']:<14.4e} {r['thrust_per_energy']:<16.4e} "
                    f"{r['acceleration_ms2']:<14.4e}\n")

    print(f"Saved text table: {fname_txt}")

    # Figure version
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('off')

    # Build table data
    col_labels = ['Energy', 'Coherence', 'Environment', 'Thrust [N]',
                  'Thrust/E [N/J]', 'Accel [m/s^2]']
    table_data = []
    for r in results:
        table_data.append([
            r['E_label'],
            r['N_coh_label'],
            r['environment'],
            f"{r['thrust_N']:.3e}",
            f"{r['thrust_per_energy']:.3e}",
            f"{r['acceleration_ms2']:.3e}",
        ])

    table = ax.table(cellText=table_data, colLabels=col_labels,
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.4)

    # Style header
    for j in range(len(col_labels)):
        table[0, j].set_facecolor('#4472C4')
        table[0, j].set_text_props(color='white', fontweight='bold')

    # Alternate row colors
    for i in range(1, len(table_data) + 1):
        color = '#D6E4F0' if i % 2 == 0 else 'white'
        for j in range(len(col_labels)):
            table[i, j].set_facecolor(color)

    ax.set_title('DFD Psi-Bubble Performance Predictions\n'
                 'Reference: R=5m, NiZn ferrite, YBCO SC, 10% asymmetry',
                 fontsize=14, fontweight='bold', pad=20)

    fname_fig = f'{save_dir}/performance_table.png'
    plt.savefig(fname_fig, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Saved figure table: {fname_fig}")

    return fname_txt, fname_fig


# ============================================================
# Quick test
# ============================================================
if __name__ == '__main__':
    print("=" * 60)
    print("DFD Performance Table Generator")
    print("=" * 60)

    results = compute_performance_table(verbose=True)
    print_performance_table(results)
    save_performance_table(results,
        '/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/simulations')
