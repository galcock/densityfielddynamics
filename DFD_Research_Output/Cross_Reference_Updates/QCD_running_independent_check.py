#!/usr/bin/env python3
"""
INDEPENDENT VERIFICATION: QCD running of b-quark mass
=====================================================

Method: Exact 1-loop mass running formula:
  m(mu_low)/m(mu_high) = [alpha_s(mu_low)/alpha_s(mu_high)]^{d_m}
  d_m = gamma_0/(2*beta_0),  gamma_0 = 8

Combined with 2-loop alpha_s evolution via RK4 numerical integration.

This is a DIFFERENT method from step-by-step Euler integration of the
coupled (alpha_s, m) system. We compute alpha_s at each threshold first,
then use the exact analytic ratio formula for mass running in each segment.

Tests multiple DFD interpretations:
  (A) Running from M_P to 1.27 GeV (user request)
  (B) Running from v/sqrt(2) = 174 GeV to m_b = 4.18 GeV
  (C) Running from v/sqrt(2) = 174 GeV to 1.27 GeV

Author: Independent verification agent (Claude Opus 4.6)
Date: 2026-03-23
"""

import math

# ===========================================================================
# Physical constants
# ===========================================================================
M_Z     = 91.1876          # Z boson mass [GeV]
a_s_MZ  = 0.1179           # alpha_s(M_Z) PDG 2024
M_P     = 1.220890e19      # Planck mass [GeV]
m_t     = 173.0            # top quark pole mass [GeV]
m_b_phys= 4.18             # b quark MS-bar mass m_b(m_b) [GeV]
m_c     = 1.27             # c quark MS-bar mass m_c(m_c) [GeV]
v_higgs = 246.22           # Higgs VEV [GeV]
v_sqrt2 = v_higgs / math.sqrt(2)  # = 174.104 GeV
alpha_em= 1.0 / 137.035999084

# Derived DFD scales
alpha_v  = alpha_em * v_sqrt2   # = 1.2705 GeV  (DFD electromagnetic mass scale)

# ===========================================================================
# QCD coefficients
# ===========================================================================
def beta0_coeff(nf):
    """beta_0 = 11 - 2*Nf/3 in the convention where
    mu^2 d(alpha_s)/d(mu^2) = -beta_0 * alpha_s^2/(2*pi) - ..."""
    return 11.0 - 2.0*nf/3.0

def d_m(nf):
    """Mass anomalous dimension exponent = gamma_0/(2*beta_0), gamma_0=8."""
    return 8.0 / (2.0 * beta0_coeff(nf))

# ===========================================================================
# 2-loop alpha_s running via RK4
# ===========================================================================
def alpha_s_2loop(mu, mu_ref, alpha_ref, nf, n_steps=20000):
    """
    2-loop RG evolution of alpha_s using RK4.

    d(alpha_s)/d(ln mu^2) = -b0*alpha_s^2 - b1*alpha_s^3

    where b0 = (33-2*Nf)/(12*pi), b1 = (153-19*Nf)/(24*pi^2).
    """
    b0 = (33.0 - 2.0*nf) / (12.0 * math.pi)
    b1 = (153.0 - 19.0*nf) / (24.0 * math.pi**2)

    L = 2.0 * math.log(mu / mu_ref)  # ln(mu^2/mu_ref^2)
    dt = L / n_steps
    a = alpha_ref

    for _ in range(n_steps):
        def f(x):
            return -b0 * x**2 - b1 * x**3
        k1 = f(a)
        k2 = f(a + 0.5*dt*k1)
        k3 = f(a + 0.5*dt*k2)
        k4 = f(a + dt*k3)
        a += dt/6.0 * (k1 + 2*k2 + 2*k3 + k4)

    return a

# ===========================================================================
# STEP 1: Compute alpha_s at all relevant scales
# ===========================================================================
print("=" * 75)
print("INDEPENDENT VERIFICATION: QCD Running of b-quark mass")
print("Method: Exact 1-loop mass ratio + 2-loop alpha_s (RK4, 20k steps)")
print("=" * 75)

print("\n--- STEP 1: alpha_s at all scales (2-loop RK4) ---\n")

# From M_Z upward to m_t (Nf=5)
a_s_mt = alpha_s_2loop(m_t, M_Z, a_s_MZ, nf=5)
print(f"  alpha_s(M_Z  = {M_Z:.4f} GeV) = {a_s_MZ:.6f}  [INPUT]")
print(f"  alpha_s(m_t  = {m_t:.1f} GeV)   = {a_s_mt:.6f}  [Nf=5]")

# From m_t upward to v/sqrt(2) (Nf=6, tiny step since 173->174)
a_s_v = alpha_s_2loop(v_sqrt2, m_t, a_s_mt, nf=6)
print(f"  alpha_s(v/r2 = {v_sqrt2:.3f} GeV) = {a_s_v:.6f}  [Nf=6]")

# From m_t upward to M_P (Nf=6)
a_s_MP = alpha_s_2loop(M_P, m_t, a_s_mt, nf=6)
print(f"  alpha_s(M_P  = {M_P:.3e} GeV) = {a_s_MP:.8f}  [Nf=6]")

# From M_Z downward to m_b (Nf=5)
a_s_mb = alpha_s_2loop(m_b_phys, M_Z, a_s_MZ, nf=5)
print(f"  alpha_s(m_b  = {m_b_phys:.2f} GeV)  = {a_s_mb:.6f}  [Nf=5]")

# From m_b downward to m_c (Nf=4)
a_s_mc = alpha_s_2loop(m_c, m_b_phys, a_s_mb, nf=4)
print(f"  alpha_s(m_c  = {m_c:.2f} GeV)  = {a_s_mc:.6f}  [Nf=4]")

# Cross-checks against PDG benchmarks
print(f"\n  Cross-checks vs PDG:")
print(f"    alpha_s(m_t) = {a_s_mt:.4f}  (PDG ~0.1082)")
print(f"    alpha_s(m_b) = {a_s_mb:.4f}  (PDG ~0.2268)")
a_s_mtau = alpha_s_2loop(1.777, m_b_phys, a_s_mb, nf=4)
print(f"    alpha_s(m_tau=1.777) = {a_s_mtau:.4f}  (PDG ~0.325)")

# ===========================================================================
# STEP 2: Mass running factors for each segment
# ===========================================================================
print(f"\n--- STEP 2: Mass running factors (1-loop mass formula) ---\n")

segments = {
    "M_P -> m_t":   (6, a_s_MP, a_s_mt,  "M_P",  "m_t"),
    "m_t -> m_b":   (5, a_s_mt, a_s_mb,   "m_t",  "m_b"),
    "m_b -> m_c":   (4, a_s_mb, a_s_mc,   "m_b",  "m_c"),
}

# Also compute v/sqrt(2) -> m_b segment
segments_v = {
    "v/r2 -> m_t":  (6, a_s_v,  a_s_mt,  "v/r2", "m_t"),
    "m_t -> m_b":   (5, a_s_mt, a_s_mb,   "m_t",  "m_b"),
    "m_b -> m_c":   (4, a_s_mb, a_s_mc,   "m_b",  "m_c"),
}

print(f"  {'Segment':<20} {'Nf':>3} {'d_m':>10} {'a_s(high)':>12} {'a_s(low)':>12} {'ratio':>10} {'R_i':>10}")
print(f"  {'-'*80}")

R_factors = {}
for label, (nf, a_high, a_low, h, l) in segments.items():
    dm = d_m(nf)
    ratio = a_low / a_high
    R = ratio ** dm
    R_factors[label] = R
    print(f"  {label:<20} {nf:>3} {dm:>10.6f} {a_high:>12.8f} {a_low:>12.6f} {ratio:>10.4f} {R:>10.6f}")

R_v_factors = {}
for label, (nf, a_high, a_low, h, l) in segments_v.items():
    dm = d_m(nf)
    ratio = a_low / a_high
    R = ratio ** dm
    R_v_factors[label] = R

# ===========================================================================
# STEP 3: Total running factors for different scenarios
# ===========================================================================
print(f"\n--- STEP 3: Total running factors ---\n")

# (A) M_P -> 1.27 GeV (all 3 segments with M_P start)
R_MP_to_mc = R_factors["M_P -> m_t"] * R_factors["m_t -> m_b"] * R_factors["m_b -> m_c"]
print(f"  (A) M_P -> m_c = 1.27 GeV:")
print(f"      R = {R_factors['M_P -> m_t']:.6f} x {R_factors['m_t -> m_b']:.6f} x {R_factors['m_b -> m_c']:.6f}")
print(f"      R_total = {R_MP_to_mc:.6f}")

# (B) M_P -> m_b = 4.18 GeV (2 segments)
R_MP_to_mb = R_factors["M_P -> m_t"] * R_factors["m_t -> m_b"]
print(f"\n  (B) M_P -> m_b = 4.18 GeV:")
print(f"      R = {R_factors['M_P -> m_t']:.6f} x {R_factors['m_t -> m_b']:.6f}")
print(f"      R_total = {R_MP_to_mb:.6f}")

# (C) v/sqrt(2) -> 1.27 GeV
R_v_to_mc = R_v_factors["v/r2 -> m_t"] * R_v_factors["m_t -> m_b"] * R_v_factors["m_b -> m_c"]
print(f"\n  (C) v/sqrt(2) = 174 GeV -> 1.27 GeV:")
print(f"      R = {R_v_factors['v/r2 -> m_t']:.6f} x {R_v_factors['m_t -> m_b']:.6f} x {R_v_factors['m_b -> m_c']:.6f}")
print(f"      R_total = {R_v_to_mc:.6f}")

# (D) v/sqrt(2) -> m_b = 4.18 GeV
R_v_to_mb = R_v_factors["v/r2 -> m_t"] * R_v_factors["m_t -> m_b"]
print(f"\n  (D) v/sqrt(2) = 174 GeV -> m_b = 4.18 GeV:")
print(f"      R = {R_v_factors['v/r2 -> m_t']:.6f} x {R_v_factors['m_t -> m_b']:.6f}")
print(f"      R_total = {R_v_to_mb:.6f}")

# (E) Just m_t -> m_b (Nf=5 only)
R_mt_to_mb = R_factors["m_t -> m_b"]
print(f"\n  (E) m_t -> m_b (Nf=5 only): R = {R_mt_to_mb:.6f}")

# ===========================================================================
# STEP 4: DFD Model B interpretation
# ===========================================================================
print(f"\n{'='*75}")
print(f"STEP 4: DFD MODEL B INTERPRETATION")
print(f"{'='*75}")

print(f"\n  DFD base scale:  alpha * v/sqrt(2) = {alpha_v:.6f} GeV = {alpha_v*1000:.4f} MeV")
print(f"  Target:          m_b(m_b) = {m_b_phys*1000:.0f} MeV")
print(f"  Needed ratio:    R_target = {m_b_phys*1000:.0f} / (sqrt(2) * {alpha_v*1000:.4f})")
R_target = m_b_phys / (math.sqrt(2) * alpha_v)
print(f"                           = {R_target:.6f}")

print(f"\n  Comparison of R_target with computed running factors:")
for label, R in [("(A) M_P -> 1.27", R_MP_to_mc),
                 ("(B) M_P -> m_b",  R_MP_to_mb),
                 ("(C) v/r2 -> 1.27", R_v_to_mc),
                 ("(D) v/r2 -> m_b",  R_v_to_mb)]:
    ratio = R / R_target
    pct = abs(ratio - 1.0) * 100
    match = "MATCH" if pct < 5 else "NO MATCH"
    print(f"    {label:<20}: R = {R:.4f}, ratio to target = {ratio:.4f} ({pct:.1f}% off) [{match}]")

# ===========================================================================
# STEP 5: Extract bare prefactor A_b for each scenario
# ===========================================================================
print(f"\n{'='*75}")
print(f"STEP 5: BARE PREFACTOR A_b FOR EACH SCENARIO")
print(f"{'='*75}")
print(f"\n  Formula: m_b = A_b * alpha * v/sqrt(2) * R_QCD")
print(f"  => A_b = m_b / (alpha * v/sqrt(2) * R_QCD) = {m_b_phys:.2f} / ({alpha_v:.6f} * R)")

for label, R in [("(A) M_P -> 1.27", R_MP_to_mc),
                 ("(B) M_P -> m_b",  R_MP_to_mb),
                 ("(C) v/r2 -> 1.27", R_v_to_mc),
                 ("(D) v/r2 -> m_b",  R_v_to_mb)]:
    A_b = m_b_phys / (alpha_v * R)
    ratio_sqrt2 = A_b / math.sqrt(2)
    ratio_pi    = A_b / math.pi
    print(f"\n    {label}:  R = {R:.4f}")
    print(f"      A_b = {A_b:.6f}")
    print(f"      A_b / sqrt(2) = {ratio_sqrt2:.4f}  (= 1.0 if Dirac factor)")
    print(f"      A_b / pi      = {ratio_pi:.4f}")

# ===========================================================================
# STEP 6: Alternative — what if the DFD formula is at a DIFFERENT scale?
# ===========================================================================
print(f"\n{'='*75}")
print(f"STEP 6: WHAT SCALE GIVES R_QCD = 2.327 (with A_b = sqrt(2))? ")
print(f"{'='*75}")

# If A_b = sqrt(2), we need R_QCD = 2.327
# The running from scale mu to m_b gives m(m_b)/m(mu)
# We need to find which mu gives the right R

# Let's compute m(m_b)/m(mu) for a range of mu values
# Using the exact ratio formula, running from mu DOWN to m_b

print(f"\n  Target: R = {R_target:.4f}")
print(f"\n  Running from various scales down to m_b = 4.18 GeV:")
print(f"  {'mu [GeV]':>12} {'Nf path':>15} {'R(mu->m_b)':>12} {'A_b needed':>12} {'A_b/sqrt(2)':>12}")
print(f"  {'-'*65}")

test_scales = [1.27, 2.0, 3.0, 4.18, 10.0, 91.2, 174.1, 1000, 1e6, 1e10, 1e15, 1e19]
for mu in test_scales:
    if mu <= m_c:
        # Below m_c: run Nf=3 from mu to m_c, then Nf=4 m_c to m_b, then done
        # But endpoint is m_b, and mu < m_b, so mass ratio < 1 (mass decreases going up)
        # Actually this is running UP from mu to m_b: m(m_b)/m(mu)
        # Since mu < m_b, alpha_s(m_b) < alpha_s(mu), so ratio < 1, R < 1
        # This means mass at m_b is LESS than at mu -- doesn't make physical sense for
        # the problem as stated. Skip.
        R_test = R_v_to_mc / R_factors["m_b -> m_c"]  # = R from v to m_b... no
        # Actually let's just compute directly
        # From mu=1.27 to m_c with Nf=3: but mu=m_c=1.27, so R=1
        # Then m_c to m_b with Nf=4: R = (a_s_mb/a_s_mc)^d_m(4)
        R_mc_to_mb = (a_s_mb / a_s_mc) ** d_m(4)
        R_test = R_mc_to_mb
        nf_path = "4"
    elif mu <= m_b_phys:
        a_s_mu = alpha_s_2loop(mu, m_b_phys, a_s_mb, nf=4)  # running down from m_b
        # Mass ratio m(m_b)/m(mu) = (a_s_mb/a_s_mu)^d_m(4)
        R_test = (a_s_mb / a_s_mu) ** d_m(4)
        nf_path = "4"
    elif mu <= m_t:
        a_s_mu = alpha_s_2loop(mu, M_Z, a_s_MZ, nf=5)
        R_mu_to_mb = (a_s_mb / a_s_mu) ** d_m(5)
        R_test = R_mu_to_mb
        nf_path = "5"
    elif mu <= v_sqrt2:
        a_s_mu = alpha_s_2loop(mu, m_t, a_s_mt, nf=6)
        R_mu_to_mt = (a_s_mt / a_s_mu) ** d_m(6)
        R_mt_mb = (a_s_mb / a_s_mt) ** d_m(5)
        R_test = R_mu_to_mt * R_mt_mb
        nf_path = "6,5"
    else:
        a_s_mu = alpha_s_2loop(mu, m_t, a_s_mt, nf=6)
        R_mu_to_mt = (a_s_mt / a_s_mu) ** d_m(6)
        R_mt_mb = (a_s_mb / a_s_mt) ** d_m(5)
        R_test = R_mu_to_mt * R_mt_mb
        nf_path = "6,5"

    A_b_test = m_b_phys / (alpha_v * R_test)
    print(f"  {mu:>12.4g} {nf_path:>15} {R_test:>12.4f} {A_b_test:>12.4f} {A_b_test/math.sqrt(2):>12.4f}")

# ===========================================================================
# STEP 7: The CORRECT interpretation from the user's problem
# ===========================================================================
print(f"\n{'='*75}")
print(f"STEP 7: USER'S SPECIFIC QUESTION")
print(f"{'='*75}")

print(f"""
  The user asks: does running from M_P to 1.27 GeV give R_total ~ 2.33?

  ANSWER: NO.

  The QCD running factor (mass enhancement) from M_P down to 1.27 GeV is:
    R(M_P -> 1.27 GeV) = {R_MP_to_mc:.4f}

  This is NOT close to 2.327.

  The running factor from M_P down to m_b = 4.18 GeV is:
    R(M_P -> m_b) = {R_MP_to_mb:.4f}

  This is also not 2.33.

  The target R_target = m_b / (sqrt(2) * alpha * v/sqrt(2)) = {R_target:.4f}
  is what's needed if A_b = sqrt(2).

  The running factor that IS close to 2.33 is from v/sqrt(2) -> m_b:
    R(v/r2 -> m_b) = {R_v_to_mb:.4f}  (ratio to target: {R_v_to_mb/R_target:.3f})

  Even this is off by {abs(R_v_to_mb/R_target - 1)*100:.1f}%.
""")

# ===========================================================================
# STEP 8: Summary table
# ===========================================================================
print(f"{'='*75}")
print(f"FINAL SUMMARY TABLE")
print(f"{'='*75}")
print(f"""
  Physical inputs:
    alpha_s(M_Z) = {a_s_MZ}
    alpha_em = 1/{1/alpha_em:.6f}
    v = {v_higgs:.2f} GeV,  v/sqrt(2) = {v_sqrt2:.3f} GeV
    alpha * v/sqrt(2) = {alpha_v:.6f} GeV = {alpha_v*1000:.4f} MeV

  alpha_s at thresholds (2-loop RK4):
    alpha_s(M_P)  = {a_s_MP:.8f}
    alpha_s(m_t)  = {a_s_mt:.6f}
    alpha_s(v/r2) = {a_s_v:.6f}
    alpha_s(M_Z)  = {a_s_MZ:.6f}
    alpha_s(m_b)  = {a_s_mb:.6f}
    alpha_s(m_c)  = {a_s_mc:.6f}

  Mass anomalous dimension exponents d_m = gamma_0/(2*beta_0):
    Nf=6: d_m = 4/7     = {d_m(6):.6f}
    Nf=5: d_m = 12/23   = {d_m(5):.6f}
    Nf=4: d_m = 12/25   = {d_m(4):.6f}
    Nf=3: d_m = 4/9     = {d_m(3):.6f}

  Running factors (mass enhancement going from high to low scale):
    R(M_P -> m_t)  [Nf=6] = {R_factors['M_P -> m_t']:.6f}
    R(m_t -> m_b)  [Nf=5] = {R_factors['m_t -> m_b']:.6f}
    R(m_b -> m_c)  [Nf=4] = {R_factors['m_b -> m_c']:.6f}

    R(M_P -> m_b)          = {R_MP_to_mb:.6f}
    R(M_P -> m_c)          = {R_MP_to_mc:.6f}
    R(v/r2 -> m_b)         = {R_v_to_mb:.6f}
    R(v/r2 -> m_c)         = {R_v_to_mc:.6f}

  DFD target (A_b = sqrt(2)):
    R_needed = m_b/(sqrt(2)*alpha*v/sqrt(2)) = {R_target:.6f}

  CONCLUSION:
    The QCD running from M_P to 1.27 GeV gives R = {R_MP_to_mc:.2f}, NOT 2.33.
    The running from v/sqrt(2) to m_b gives R = {R_v_to_mb:.2f}, closest to target 2.33.
    With A_b = sqrt(2) and R(v/r2->m_b) = {R_v_to_mb:.2f}:
      m_b(predicted) = sqrt(2) * {alpha_v*1000:.1f} MeV * {R_v_to_mb:.4f}
                     = {math.sqrt(2)*alpha_v*1000*R_v_to_mb:.1f} MeV
      m_b(observed)  = 4180 MeV
      Discrepancy    = {abs(math.sqrt(2)*alpha_v*R_v_to_mb - m_b_phys)/m_b_phys*100:.1f}%
""")
