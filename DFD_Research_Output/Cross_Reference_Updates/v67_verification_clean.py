#!/usr/bin/env python3
"""
DFD v67 Charged-Fermion Mass Dictionary — Clean Verification & Parameter Elimination Test

Two computations:
  (A) Original v67 dictionary: alpha = 1/137.036, v/sqrt(2) = 174.1 GeV (from G_F)
  (B) Derived-v dictionary:    v = M_P * alpha^8 * sqrt(2*pi)
      => v/sqrt(2) = M_P * alpha^8 * sqrt(pi)
      Uses the same alpha.

Also tests:
  (C) Sensitivity to alpha: compare alpha = 1/137.036  vs  alpha = 1/137.035999854

Mass law:  m_f = A_f * alpha^n_f * (v/sqrt(2))
"""
from __future__ import annotations
import math

# ── Physical constants ──────────────────────────────────────────────────────
M_P_GeV = 1.220890e19          # Planck mass in GeV (PDG 2024)
G_F_GeV2 = 1.1663788e-5       # Fermi constant in GeV^-2 (PDG 2024)

# Two alpha values to compare
alpha_approx = 1.0 / 137.036                  # standard approximation used in v67
alpha_DFD    = 1.0 / 137.035999854            # DFD-derived value

sqrt2 = math.sqrt(2)

# ── v67 dictionary entries: (name, A_f, n_f, observed_mass_MeV) ─────────
entries = [
    ("e",   2/3,     2.5,      0.511),
    ("mu",  1.0,     1.5,    105.66),
    ("tau", sqrt2,   1.0,   1776.86),
    ("u",   8/3,     2.5,      2.16),
    ("c",   1.0,     1.0,   1270.0),
    ("t",   1.0,     0.0, 172760.0),
    ("d",   6.0,     2.5,      4.67),
    ("s",   6/7,     1.5,     93.0),
    ("b",   1/42,    0.0,   4180.0),
]


def compute_masses(alpha, v_over_sqrt2_MeV):
    """Return list of (name, Af, nf, pred_MeV, obs_MeV, pct_err)."""
    results = []
    for name, Af, nf, obs in entries:
        pred = Af * (alpha ** nf) * v_over_sqrt2_MeV
        pct = (pred / obs - 1.0) * 100
        results.append((name, Af, nf, pred, obs, pct))
    return results


def print_table(label, results):
    """Pretty-print a results table."""
    abs_pcts = [abs(r[5]) for r in results]
    mean_abs = sum(abs_pcts) / len(abs_pcts)
    max_abs  = max(abs_pcts)
    print(f"\n{'=' * 86}")
    print(f"  {label}")
    print(f"{'=' * 86}")
    print(f"  {'Fermion':<6} {'Af':>12} {'nf':>6} {'Pred (MeV)':>16} {'Obs (MeV)':>12} {'%err':>10}")
    print(f"  {'-' * 80}")
    for name, Af, nf, pred, obs, pct in results:
        print(f"  {name:<6} {Af:>12.6g} {nf:>6.2f} {pred:>16.6g} {obs:>12.6g} {pct:>+9.3f}%")
    print(f"  {'-' * 80}")
    print(f"  Mean |%err| = {mean_abs:.3f}%    Max |%err| = {max_abs:.3f}%")
    return mean_abs


def compare_tables(label, res_A, res_B):
    """Show how each mass shifts between two computations."""
    print(f"\n{'=' * 86}")
    print(f"  {label}")
    print(f"{'=' * 86}")
    print(f"  {'Fermion':<6} {'Pred_A (MeV)':>16} {'Pred_B (MeV)':>16} {'Shift':>10}")
    print(f"  {'-' * 70}")
    for a, b in zip(res_A, res_B):
        name = a[0]
        shift = (b[3] / a[3] - 1.0) * 100
        print(f"  {name:<6} {a[3]:>16.6g} {b[3]:>16.6g} {shift:>+9.4f}%")


# ══════════════════════════════════════════════════════════════════════════════
# (A) ORIGINAL v67: alpha = 1/137.036,  v/sqrt(2) = 174.1 GeV
# ══════════════════════════════════════════════════════════════════════════════
alpha = alpha_approx
v_over_sqrt2_A = 174.1e3   # MeV

print("*" * 86)
print("  DFD v67 MASS DICTIONARY — FULL VERIFICATION")
print("*" * 86)
print(f"\n  alpha (approx)  = 1/{1/alpha_approx:.6f}  =  {alpha_approx:.16e}")
print(f"  alpha (DFD)     = 1/{1/alpha_DFD:.9f}  =  {alpha_DFD:.16e}")
print(f"  Difference      = {(alpha_DFD/alpha_approx - 1)*1e9:.2f} ppb")

res_A = compute_masses(alpha, v_over_sqrt2_A)
mean_A = print_table("(A) Original v67:  alpha=1/137.036, v/sqrt(2)=174.1 GeV", res_A)


# ══════════════════════════════════════════════════════════════════════════════
# (B) DERIVED v:  v = M_P * alpha^8 * sqrt(2*pi)
#     => v/sqrt(2) = M_P * alpha^8 * sqrt(pi)
# ══════════════════════════════════════════════════════════════════════════════
v_derived_GeV = M_P_GeV * (alpha ** 8) * math.sqrt(2 * math.pi)
v_over_sqrt2_B = M_P_GeV * (alpha ** 8) * math.sqrt(math.pi) * 1e3  # in MeV

print(f"\n{'─' * 86}")
print(f"  DERIVED VEV CALCULATION:  v = M_P * alpha^8 * sqrt(2*pi)")
print(f"{'─' * 86}")
print(f"  M_P           = {M_P_GeV:.6e} GeV")
print(f"  alpha^8       = {alpha**8:.16e}")
print(f"  sqrt(2*pi)    = {math.sqrt(2*math.pi):.16f}")
print(f"  sqrt(pi)      = {math.sqrt(math.pi):.16f}")
print(f"")
print(f"  v_derived     = {v_derived_GeV:.6f} GeV")
print(f"  v_derived/sqrt(2) = {v_over_sqrt2_B/1e3:.6f} GeV")
print(f"")
print(f"  v_standard (from G_F) = 246.22 GeV  =>  v/sqrt(2) = 174.1 GeV")
print(f"  v_derived             = {v_derived_GeV:.4f} GeV")
print(f"  Fractional shift in v = {(v_derived_GeV/246.22 - 1)*100:+.4f}%")
print(f"  Fractional shift in v/sqrt(2) = {(v_over_sqrt2_B/1e3/174.1 - 1)*100:+.4f}%")

res_B = compute_masses(alpha, v_over_sqrt2_B)
mean_B = print_table("(B) Derived v:  v/sqrt(2) = M_P * alpha^8 * sqrt(pi)", res_B)

compare_tables("SHIFT: (A) -> (B)  [effect of replacing G_F input with derived v]", res_A, res_B)


# ══════════════════════════════════════════════════════════════════════════════
# (C) ALPHA SENSITIVITY:  1/137.036  vs  1/137.035999854
# ══════════════════════════════════════════════════════════════════════════════
res_C = compute_masses(alpha_DFD, v_over_sqrt2_A)
mean_C = print_table("(C) DFD alpha:  alpha=1/137.035999854, v/sqrt(2)=174.1 GeV", res_C)

compare_tables("SHIFT: (A) -> (C)  [effect of using DFD-derived alpha]", res_A, res_C)


# ══════════════════════════════════════════════════════════════════════════════
# (D) BOTH SUBSTITUTIONS:  derived alpha AND derived v
# ══════════════════════════════════════════════════════════════════════════════
v_over_sqrt2_D = M_P_GeV * (alpha_DFD ** 8) * math.sqrt(math.pi) * 1e3  # MeV
v_derived_DFD  = M_P_GeV * (alpha_DFD ** 8) * math.sqrt(2 * math.pi)

res_D = compute_masses(alpha_DFD, v_over_sqrt2_D)
mean_D = print_table("(D) Both derived:  alpha=DFD, v=M_P*alpha^8*sqrt(2pi)", res_D)

compare_tables("SHIFT: (A) -> (D)  [both substitutions combined]", res_A, res_D)


# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print(f"\n{'*' * 86}")
print(f"  SUMMARY")
print(f"{'*' * 86}")
print(f"")
print(f"  (A) Original v67 (alpha=1/137.036, v/sqrt2=174.1 GeV) :  mean |err| = {mean_A:.3f}%")
print(f"  (B) Derived v   (v = M_P*alpha^8*sqrt(2pi))           :  mean |err| = {mean_B:.3f}%")
print(f"  (C) DFD alpha   (alpha=1/137.035999854)                :  mean |err| = {mean_C:.3f}%")
print(f"  (D) Both derived (DFD alpha + derived v)               :  mean |err| = {mean_D:.3f}%")
print(f"")
print(f"  v from G_F:     v/sqrt(2) = 174.100 GeV")
print(f"  v derived:      v/sqrt(2) = {v_over_sqrt2_B/1e3:.3f} GeV  (shift {(v_over_sqrt2_B/1e3/174.1 - 1)*100:+.3f}%)")
print(f"  v derived(DFD): v/sqrt(2) = {v_over_sqrt2_D/1e3:.3f} GeV  (shift {(v_over_sqrt2_D/1e3/174.1 - 1)*100:+.3f}%)")
print(f"")
print(f"  Alpha choice (approx vs DFD): {(alpha_DFD/alpha_approx - 1)*1e9:.1f} ppb  =>  irrelevant at 1% level")
print(f"")

# Key question: is the claim "one free parameter can be eliminated" honest?
v_shift_pct = abs(v_over_sqrt2_B/1e3 / 174.1 - 1) * 100
err_shift = abs(mean_B - mean_A)
print(f"  PARAMETER ELIMINATION ASSESSMENT:")
print(f"  ──────────────────────────────────")
if v_shift_pct < 5 and mean_B < 5:
    if mean_B < mean_A + 1:
        print(f"  The derived v shifts by {v_shift_pct:.2f}% from the G_F value.")
        print(f"  Mean error changes from {mean_A:.3f}% to {mean_B:.3f}%.")
        print(f"  VERDICT: The claim is HONEST — the derived v is close enough that the")
        print(f"           mass dictionary works with zero free parameters (only M_P and alpha).")
    else:
        print(f"  The derived v shifts by {v_shift_pct:.2f}%, degrading mean error by {err_shift:.3f}%.")
        print(f"  VERDICT: MARGINAL — the substitution works but noticeably degrades fit quality.")
else:
    print(f"  The derived v shifts by {v_shift_pct:.2f}% from G_F value, mean error = {mean_B:.3f}%.")
    print(f"  VERDICT: PROBLEMATIC — the substitution significantly degrades the dictionary.")

print()
