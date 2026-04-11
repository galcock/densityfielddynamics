#!/usr/bin/env python3
"""
DFD v3.0 Charged-Fermion Mass Dictionary — Verification Script

Mass law:
  m_f = A_f * alpha^(n_f) * v/sqrt(2)

Constants:
  alpha = 1/137.036
  v/sqrt(2) = 174.1 GeV

This script recomputes the predicted masses and errors for the v3.0 dictionary.
"""
from __future__ import annotations
import math

alpha = 1/137.036
v_over_sqrt2_MeV = 174.1e3

sqrt2 = math.sqrt(2)

entries = [
    ("e",   2/3,   2.5,    0.511),
    ("mu",  1.0,   1.5,  105.66),
    ("tau", sqrt2, 1.0, 1776.86),
    ("u",   8/3,   2.5,    2.16),
    ("c",   1.0,   1.0, 1270.0),
    ("t",   1.0,   0.0, 172760.0),
    ("d",   6.0,   2.5,    4.67),
    ("s",   6/7,   1.5,   93.0),
    ("b",   1/42,  0.0, 4180.0),
]

def pred(Af, nf):
    return Af * (alpha**nf) * v_over_sqrt2_MeV

abs_pct = []
print("="*80)
print("DFD v3.0 MASS DICTIONARY VERIFICATION")
print("="*80)
print(f"alpha = {alpha}")
print(f"v/sqrt(2) = {v_over_sqrt2_MeV/1e3:.1f} GeV")
print("m = Af * alpha^nf * v/sqrt(2)")
print()
print(f"{'Fermion':<6} {'Af':>10} {'nf':>6} {'pred (MeV)':>14} {'obs (MeV)':>12} {'%err':>9}")
print("-"*80)
for name, Af, nf, obs in entries:
    mp = pred(Af, nf)
    perr = (mp/obs - 1.0)*100
    abs_pct.append(abs(perr))
    print(f"{name:<6} {Af:>10.6g} {nf:>6.2f} {mp:>14.6g} {obs:>12.6g} {perr:>+8.3f}%")
print("-"*80)
mean_abs = sum(abs_pct)/len(abs_pct)
print(f"Mean absolute % error: {mean_abs:.3f}%")
