#!/usr/bin/env python3
"""
run_all.py -- Master Runner for DFD Psi-Bubble Numerical Simulations
=====================================================================

Runs all simulation modules and produces all figures and tables.

Usage:
    cd DFD_Research_Output/simulations/
    python run_all.py

Or from anywhere:
    python /path/to/run_all.py

Outputs:
    - radial_*.png            : 1D radial solution plots
    - asymmetric_*.png        : l=1 perturbation plots
    - em_mode_*.png           : EM mode structure plots
    - sweep_*.png             : Parameter sweep plots
    - self_consistency_*.png  : Convergence study plots
    - performance_table.png   : Summary performance table
    - performance_table.txt   : Text version of performance table

Dependencies:
    numpy, scipy, matplotlib (standard scientific Python stack)
"""

import os
import sys
import time
import numpy as np

# Ensure we run from the simulations directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

# Imports
from constants import (c, G, kappa_DFD, R_inner, R_outer,
                       eps_r_ferrite, mu_r_ferrite)


def banner(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def main():
    t_start = time.time()

    banner("DFD PSI-BUBBLE NUMERICAL SIMULATION SUITE")
    print(f"  Working directory: {SCRIPT_DIR}")
    print(f"  Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\n  DFD coupling constant kappa = {kappa_DFD:.4e} m/J")
    print(f"  Reference shell: R_inner={R_inner} m, R_outer={R_outer} m")
    print(f"  Ferrite: eps_r={eps_r_ferrite}, mu_r={mu_r_ferrite}")

    all_files = []

    # -------------------------------------------------------
    # 1. RADIAL SOLVER
    # -------------------------------------------------------
    banner("1. RADIAL SOLVER (Spherical Symmetry)")
    from radial_solver import solve_radial_psi, plot_radial_solution

    test_cases = [
        (1e6,  1.0,    'earth_orbit'),
        (1e9,  1.0,    'earth_orbit'),
        (1e9,  1e12,   'earth_orbit'),
        (1e12, 1e12,   'earth_orbit'),
        (1e9,  1e12,   'deep_space'),
    ]

    for E, N, env in test_cases:
        print(f"\n  E = {E:.0e} J, N_coh = {N:.0e}, env = {env}")
        result = solve_radial_psi(E_stored=E, N_coh=N, environment=env)
        print(f"    Force on shell: {result['force_on_shell']:.4e} N")
        print(f"    Max |accel|:    {np.max(np.abs(result['acceleration'])):.4e} m/s^2")
        fname = plot_radial_solution(result,
            save_prefix=os.path.join(SCRIPT_DIR, f'radial_{env}'))
        all_files.append(fname)

    # -------------------------------------------------------
    # 2. ASYMMETRIC SOLVER (l=1 thrust)
    # -------------------------------------------------------
    banner("2. ASYMMETRIC SOLVER (l=1 Dipole Thrust)")
    from asymmetric_solver import solve_asymmetric, plot_asymmetric_solution

    asym_cases = [
        (1e6,  1.0,    'earth_orbit', 0.1),
        (1e9,  1.0,    'earth_orbit', 0.1),
        (1e9,  1e12,   'earth_orbit', 0.1),
        (1e12, 1e12,   'earth_orbit', 0.1),
        (1e9,  1e12,   'earth_orbit', 0.5),   # high asymmetry
        (1e9,  1e12,   'deep_space',  0.1),
    ]

    for E, N, env, asym in asym_cases:
        print(f"\n  E = {E:.0e} J, N_coh = {N:.0e}, env = {env}, asym = {asym}")
        result = solve_asymmetric(E_stored=E, N_coh=N, asymmetry=asym,
                                  environment=env)
        print(f"    Thrust:         {result['thrust_N']:.4e} N")
        print(f"    Thrust/Energy:  {result['thrust_per_energy']:.4e} N/J")
        fname = plot_asymmetric_solution(result,
            save_prefix=os.path.join(SCRIPT_DIR, f'asymmetric_{env}_a{asym}'))
        all_files.append(fname)

    # -------------------------------------------------------
    # 3. EM MODE CALCULATOR
    # -------------------------------------------------------
    banner("3. EM ROTATING MODE CALCULATOR")
    from em_modes import (find_resonant_frequencies, em_field_profile,
                          normalize_energy_density, extract_multipole_components,
                          plot_em_modes)

    for l_mode in [1, 2]:
        freqs = find_resonant_frequencies(l=l_mode, n_modes=3)
        print(f"\n  TE_{l_mode} resonant frequencies:")
        for i, omega in enumerate(freqs):
            f_Hz = omega / (2 * np.pi)
            print(f"    Mode {i+1}: f = {f_Hz:.3e} Hz, omega = {omega:.3e} rad/s")

        if freqs:
            m_mode = min(l_mode, 1)  # rotating mode
            r_arr, theta_arr, u_2d, f_r, a_theta = em_field_profile(
                freqs[0], l=l_mode, m=m_mode,
                R1=R_inner, R2=R_outer,
                eps_r=eps_r_ferrite, mu_r=mu_r_ferrite)

            u_2d_norm = normalize_energy_density(r_arr, theta_arr, u_2d, 1e9)
            u_0, u_1 = extract_multipole_components(r_arr, theta_arr, u_2d_norm)

            print(f"    Monopole max: {np.max(u_0):.3e} J/m^3")
            print(f"    Dipole max:   {np.max(np.abs(u_1)):.3e} J/m^3")
            print(f"    Dipole/Monopole ratio: {np.max(np.abs(u_1))/max(np.max(u_0),1e-30):.3f}")

            fname = plot_em_modes(r_arr, theta_arr, u_2d_norm, f_r, freqs,
                                  l=l_mode, m=m_mode, R1=R_inner, R2=R_outer,
                                  save_prefix=os.path.join(SCRIPT_DIR, 'em_mode'))
            all_files.append(fname)

    # -------------------------------------------------------
    # 4. PARAMETER SWEEPS
    # -------------------------------------------------------
    banner("4. PARAMETER SWEEPS")
    from parameter_sweep import run_all_sweeps

    sweep_files = run_all_sweeps(SCRIPT_DIR)
    all_files.extend(sweep_files)

    # -------------------------------------------------------
    # 5. SELF-CONSISTENCY CHECK
    # -------------------------------------------------------
    banner("5. SELF-CONSISTENCY ITERATION")
    from self_consistency import self_consistency_loop, convergence_study

    # Single detailed run
    print("\n  Detailed self-consistency run: E=1GJ, N_coh=1e12")
    sc_result = self_consistency_loop(
        E_stored=1e9, N_coh=1e12, max_iter=15, tol=1e-14, verbose=True)

    # Full convergence study
    fname = convergence_study(SCRIPT_DIR)
    all_files.append(fname)

    # -------------------------------------------------------
    # 6. PERFORMANCE TABLE
    # -------------------------------------------------------
    banner("6. PERFORMANCE PREDICTION TABLE")
    from performance_table import (compute_performance_table,
                                   print_performance_table,
                                   save_performance_table)

    results = compute_performance_table(verbose=True)
    print_performance_table(results)
    fname_txt, fname_fig = save_performance_table(results, SCRIPT_DIR)
    all_files.extend([fname_txt, fname_fig])

    # -------------------------------------------------------
    # Summary
    # -------------------------------------------------------
    t_end = time.time()
    banner("SIMULATION COMPLETE")
    print(f"  Total runtime: {t_end - t_start:.1f} seconds")
    print(f"  Output files ({len(all_files)}):")
    for f in sorted(all_files):
        print(f"    {f}")
    print()


if __name__ == '__main__':
    main()
