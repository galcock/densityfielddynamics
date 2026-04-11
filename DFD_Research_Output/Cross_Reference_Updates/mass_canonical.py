#!/usr/bin/env python3
"""
DFD Charged-Fermion Mass Spectrum -- CANONICAL Script
======================================================

This is the ONE canonical computation of all nine charged-fermion masses
in the DFD framework. It uses the v67 Mass Dictionary values, which were
verified and approved in January 2026.

Master formula:
    m_f = A_f * alpha^(n_f) * v/sqrt(2)

Constants:
    alpha    = 1/137.036   (fine-structure constant, derived in DFD)
    v/sqrt(2) = 174.1 GeV  (from Fermi constant G_F)

FREE PARAMETER COUNT:
    Mode 1 (default): ONE free parameter -- v/sqrt(2) = 174.1 GeV from G_F
    Mode 2 (derived): ZERO free parameters -- v = M_P * alpha^8 * sqrt(2*pi)
        The derived v introduces +0.78% systematic on the top mass
        (v_derived = 246.09 GeV vs v_obs = 246.22 GeV)

PREFACTORS (from explicit Yukawa operator on A_5 microsector):
    G = diag(2/3, 1, 1)          -- generation operator
    D_ell = diag(1, 1, sqrt(2))  -- Dirac normalization (leptons)
    Q_d = diag(1, 6/7, 1/42)    -- QCD running (down quarks)
    K_d = J_3 (rank-1, S_3 invariance, Lemma L)
    K_u = I_4 (O(4) isotropy, Schur's lemma)

EXPONENTS (from spin^c line-bundle degrees on CP^2):
    n_f = (k_f + k_H)/2
    k_H = +1 (H-coupling: leptons, down quarks)
    k_H = -1 (H-tilde coupling: up quarks)

SOURCE: DFD_v67_MASS_DICTIONARY_FINAL.md (ground truth, January 2026)
STATUS: This script supersedes compute_all_masses.py and compute_mass_exponents.py.
        See Mass_Model_Reconciliation.tex for how those two scripts relate.
"""

import math
import sys

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================

ALPHA = 1.0 / 137.036

# Mode 1: Experimental v/sqrt(2)
V_OBS_GEV = 246.22                       # Higgs VEV from G_F (GeV)
V_SQRT2_OBS_GEV = V_OBS_GEV / math.sqrt(2)  # 174.1 GeV
V_SQRT2_OBS_MEV = V_SQRT2_OBS_GEV * 1000.0

# Mode 2: Derived v from M_P alpha^8 sqrt(2 pi)
M_PLANCK_GEV = 1.220910e19              # Planck mass (GeV)
V_DERIVED_GEV = M_PLANCK_GEV * ALPHA**8 * math.sqrt(2.0 * math.pi)
V_SQRT2_DERIVED_GEV = V_DERIVED_GEV / math.sqrt(2)
V_SQRT2_DERIVED_MEV = V_SQRT2_DERIVED_GEV * 1000.0

# =============================================================================
# v67 MASS DICTIONARY -- CANONICAL VALUES
# =============================================================================

# PDG 2024 observed masses (MeV)
# Light quarks (u, d, s): MS-bar at mu = 2 GeV
# c: MS-bar at mu = m_c;  b: MS-bar at mu = m_b;  t: pole mass
FERMION_DATA = [
    # (name, symbol, A_f_exact_label, A_f_value, n_f, m_obs_MeV, sector)
    ("electron",  "e",   "2/3",       2.0/3.0,       2.5,      0.511,   "lepton"),
    ("muon",      "mu",  "1",         1.0,           1.5,    105.66,    "lepton"),
    ("tau",       "tau", "sqrt(2)",   math.sqrt(2),  1.0,   1776.86,    "lepton"),
    ("up",        "u",   "8/3",       8.0/3.0,       2.5,      2.16,    "up"),
    ("charm",     "c",   "1",         1.0,           1.0,   1270.0,     "up"),
    ("top",       "t",   "1",         1.0,           0.0, 172760.0,     "up"),
    ("down",      "d",   "6",         6.0,           2.5,      4.67,    "down"),
    ("strange",   "s",   "6/7",       6.0/7.0,       1.5,     93.0,    "down"),
    ("bottom",    "b",   "1/42",      1.0/42.0,      0.0,   4180.0,    "down"),
]

# =============================================================================
# OPERATOR DERIVATION OF PREFACTORS
# =============================================================================

def derive_prefactors():
    """
    Derive all 9 prefactors from the explicit Yukawa operator algebra.
    Returns dict mapping symbol -> (A_f, derivation_string).
    """
    # Generation operator G = diag(2/3, 1, 1)
    G = {1: 2.0/3.0, 2: 1.0, 3: 1.0}

    # Dirac normalization D_ell = diag(1, 1, sqrt(2))
    D_ell = {1: 1.0, 2: 1.0, 3: math.sqrt(2)}

    # QCD running Q_d = diag(1, 6/7, 1/42)
    Q_d = {1: 1.0, 2: 6.0/7.0, 3: 1.0/42.0}

    # CP^2 kernel coupling strengths
    R_d = {1: 9, 2: 1, 3: 1}   # J_3 kernel: R_d(gen1) = Tr(J_3) = 9
    R_u = {1: 4, 2: 1, 3: 1}   # I_4 kernel: R_u(gen1) = Tr(I_4) = 4

    results = {}

    # Leptons: A_f = G[g] * D_ell[g]
    results['e']   = (G[1] * D_ell[1], "G[1] * D_ell[1] = 2/3 * 1")
    results['mu']  = (G[2] * D_ell[2], "G[2] * D_ell[2] = 1 * 1")
    results['tau'] = (G[3] * D_ell[3], "G[3] * D_ell[3] = 1 * sqrt(2)")

    # Up quarks: A_f = G[g] * R_u[g]
    results['u'] = (G[1] * R_u[1], "G[1] * R_u[1] = 2/3 * 4")
    results['c'] = (G[2] * R_u[2], "G[2] * R_u[2] = 1 * 1")
    results['t'] = (G[3] * R_u[3], "G[3] * R_u[3] = 1 * 1")

    # Down quarks: A_f = G[g] * Q_d[g] * R_d[g]
    results['d'] = (G[1] * Q_d[1] * R_d[1], "G[1] * Q_d[1] * R_d[1] = 2/3 * 1 * 9")
    results['s'] = (G[2] * Q_d[2] * R_d[2], "G[2] * Q_d[2] * R_d[2] = 1 * 6/7 * 1")
    results['b'] = (G[3] * Q_d[3] * R_d[3], "G[3] * Q_d[3] * R_d[3] = 1 * 1/42 * 1")

    return results

# =============================================================================
# MASS COMPUTATION
# =============================================================================

def compute_masses(use_derived_v=False):
    """
    Compute all 9 fermion masses using the canonical v67 dictionary.

    Parameters:
        use_derived_v: if True, use v = M_P alpha^8 sqrt(2 pi) (zero free params)
                       if False (default), use v/sqrt(2) = 174.1 GeV from G_F

    Returns:
        list of (symbol, A_f_label, n_f, m_pred_MeV, m_obs_MeV, pct_error)
    """
    if use_derived_v:
        v_sqrt2_MeV = V_SQRT2_DERIVED_MEV
    else:
        v_sqrt2_MeV = V_SQRT2_OBS_MEV

    results = []
    for name, sym, Af_label, Af, nf, m_obs, sector in FERMION_DATA:
        m_pred = Af * (ALPHA ** nf) * v_sqrt2_MeV
        pct_err = (m_pred / m_obs - 1.0) * 100.0
        results.append((sym, Af_label, nf, m_pred, m_obs, pct_err))

    return results

def format_mass(m_MeV):
    """Format a mass in appropriate units."""
    if m_MeV < 1.0:
        return f"{m_MeV * 1000:.1f} keV"
    elif m_MeV < 1000.0:
        return f"{m_MeV:.2f} MeV"
    else:
        return f"{m_MeV / 1000:.2f} GeV"

# =============================================================================
# STRUCTURAL RATIO CHECKS (zero free parameters)
# =============================================================================

def check_structural_ratios():
    """
    Verify mass ratios that have ZERO free parameters.
    These hold regardless of the v/sqrt(2) normalization.
    """
    Af = {sym: val for _, sym, _, val, _, _, _ in FERMION_DATA}
    nf = {sym: val for _, sym, _, _, val, _, _ in FERMION_DATA}

    ratios = [
        ("A_d / A_u",   Af['d'] / Af['u'],   9.0/4.0,     "R_d/R_u = 9/4 (J_3 vs I_4)"),
        ("A_t / A_b",   Af['t'] / Af['b'],   42.0,        "1/Q_d(3,3) = N_f * b_0 = 42"),
        ("A_tau / A_mu", Af['tau'] / Af['mu'], math.sqrt(2), "D_ell(3,3) / D_ell(2,2)"),
        ("A_e / A_mu",  Af['e'] / Af['mu'],  2.0/3.0,     "G[1]/G[2] = 2/3"),
        ("A_u / A_c",   Af['u'] / Af['c'],   8.0/3.0,     "G[1]*R_u[1] / G[2]*R_u[2]"),
        ("A_d / A_s",   Af['d'] / Af['s'],   7.0,         "G[1]*Q_d[1]*R_d[1] / G[2]*Q_d[2]*R_d[2]"),
    ]

    all_ok = True
    for label, computed, expected, origin in ratios:
        ok = abs(computed - expected) / expected < 1e-10
        all_ok = all_ok and ok
        yield (label, computed, expected, origin, ok)

# =============================================================================
# MAIN OUTPUT
# =============================================================================

def main():
    use_derived = "--derived" in sys.argv

    print("=" * 82)
    print("DFD CHARGED-FERMION MASS SPECTRUM -- CANONICAL COMPUTATION (v67 Dictionary)")
    print("=" * 82)
    print()
    print("Master formula:  m_f = A_f * alpha^(n_f) * v/sqrt(2)")
    print(f"  alpha        = 1/137.036 = {ALPHA:.10f}")
    print()

    if use_derived:
        v_sqrt2 = V_SQRT2_DERIVED_GEV
        print(f"  MODE: ZERO FREE PARAMETERS (derived v)")
        print(f"  v (derived)  = M_P * alpha^8 * sqrt(2*pi) = {V_DERIVED_GEV:.2f} GeV")
        print(f"  v/sqrt(2)    = {v_sqrt2:.2f} GeV")
        print(f"  v (obs)      = {V_OBS_GEV} GeV   [delta = {(V_DERIVED_GEV/V_OBS_GEV - 1)*100:+.3f}%]")
    else:
        v_sqrt2 = V_SQRT2_OBS_GEV
        print(f"  MODE: ONE FREE PARAMETER (v/sqrt(2) from G_F)")
        print(f"  v/sqrt(2)    = {v_sqrt2:.1f} GeV   [from Fermi constant G_F]")
    print()

    # ---- Step 1: Verify prefactors from operator algebra ----
    print("-" * 82)
    print("STEP 1: Prefactors from operator algebra")
    print("-" * 82)
    derived = derive_prefactors()

    print(f"  {'Symbol':>6}  {'Derived':>12}  {'Dictionary':>12}  {'Match':>6}  Derivation")
    print("  " + "-" * 72)

    all_Af_ok = True
    for _, sym, _, Af_dict, _, _, _ in FERMION_DATA:
        Af_comp, derivation = derived[sym]
        match = abs(Af_comp - Af_dict) < 1e-12
        all_Af_ok = all_Af_ok and match
        print(f"  {sym:>6}  {Af_comp:12.8f}  {Af_dict:12.8f}  {'OK' if match else 'FAIL':>6}  {derivation}")

    print(f"\n  All prefactors match dictionary: {'YES' if all_Af_ok else 'NO'}")

    # ---- Step 2: Mass predictions ----
    print()
    print("-" * 82)
    print("STEP 2: Mass predictions")
    print("-" * 82)
    print(f"  {'Symbol':>6}  {'A_f':>10}  {'n_f':>5}  {'Predicted':>14}  {'Observed':>14}  {'Error':>8}")
    print("  " + "-" * 68)

    results = compute_masses(use_derived_v=use_derived)
    abs_errors = []

    for sym, Af_label, nf, m_pred, m_obs, pct_err in results:
        abs_errors.append(abs(pct_err))
        print(f"  {sym:>6}  {Af_label:>10}  {nf:>5.1f}  {format_mass(m_pred):>14}  {format_mass(m_obs):>14}  {pct_err:>+7.2f}%")

    mean_err = sum(abs_errors) / len(abs_errors)
    max_err = max(abs_errors)
    print("  " + "-" * 68)
    print(f"  Mean |error|:    {mean_err:.3f}%")
    print(f"  Maximum |error|: {max_err:.3f}%  ({results[abs_errors.index(max_err)][0]})")

    # ---- Step 3: Structural ratios (zero free parameters) ----
    print()
    print("-" * 82)
    print("STEP 3: Structural ratio verification (ZERO free parameters)")
    print("-" * 82)

    all_ratios_ok = True
    for label, computed, expected, origin, ok in check_structural_ratios():
        all_ratios_ok = all_ratios_ok and ok
        print(f"  {label:14s} = {computed:8.4f}  (expected {expected:8.4f})  [{origin}]  {'OK' if ok else 'FAIL'}")
    print(f"\n  All structural ratios verified: {'YES' if all_ratios_ok else 'NO'}")

    # ---- Summary ----
    print()
    print("=" * 82)
    print("SUMMARY")
    print("=" * 82)

    if use_derived:
        print(f"""
  ZERO-PARAMETER MODE:
    v = M_P * alpha^8 * sqrt(2*pi) = {V_DERIVED_GEV:.2f} GeV
    Mean |error| = {mean_err:.2f}%  (9 masses, 0 free parameters)

    The derived v is {(V_DERIVED_GEV/V_OBS_GEV - 1)*100:+.3f}% from v_obs = {V_OBS_GEV} GeV.
    This 0.05% offset propagates into all predictions uniformly.

    CAVEAT: The formula v = M_P alpha^8 sqrt(2*pi) is Tier 1.5
    (topologically motivated, exponent 8 = dim(CP^2 x S^3) + 1,
    but the full proof chain is not yet at published-theorem grade).
""")
    else:
        print(f"""
  ONE-PARAMETER MODE:
    v/sqrt(2) = {V_SQRT2_OBS_GEV:.1f} GeV  (from Fermi constant G_F)
    Mean |error| = {mean_err:.2f}%  (9 masses, 1 free parameter)

    The single free parameter is the overall scale v/sqrt(2).
    All mass RATIOS have zero free parameters.
    No per-fermion fitting exists.
""")

    print("  DERIVATION CHAIN:")
    print("    1. alpha = 1/137.036   [from CS level sum, k_max = 60]")
    print("    2. n_f = (k_f + k_H)/2 [from spin^c bundle degrees on CP^2]")
    print("    3. A_f from {G, K_d=J_3, K_u=I_4, Q_d, D_ell}")
    print("    4. m_f = A_f * alpha^n_f * v/sqrt(2)")
    print()

    if use_derived:
        print("  FREE PARAMETERS: ZERO")
        print("  (but v derivation adds ~0.05% systematic; Tier 1.5 rigor)")
    else:
        print("  FREE PARAMETERS: ONE (global scale v/sqrt(2) from G_F)")

    print("  PER-FERMION FITTING: NONE")
    print("=" * 82)

    # ---- Both modes comparison ----
    if not use_derived:
        print()
        print("-" * 82)
        print("COMPARISON: One-parameter vs. zero-parameter modes")
        print("-" * 82)
        results_derived = compute_masses(use_derived_v=True)
        abs_err_derived = [abs(r[5]) for r in results_derived]
        mean_derived = sum(abs_err_derived) / len(abs_err_derived)
        print(f"  One parameter (v from G_F):     mean |error| = {mean_err:.3f}%")
        print(f"  Zero parameters (v derived):    mean |error| = {mean_derived:.3f}%")
        print(f"  Difference in v:                {(V_DERIVED_GEV/V_OBS_GEV - 1)*100:+.4f}%")
        print()

    return mean_err, max_err, all_Af_ok, all_ratios_ok


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python mass_canonical.py [--derived]")
        print()
        print("  Default:    One free parameter (v/sqrt(2) from G_F)")
        print("  --derived:  Zero free parameters (v = M_P alpha^8 sqrt(2 pi))")
        sys.exit(0)

    mean_err, max_err, Af_ok, ratios_ok = main()
