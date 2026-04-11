#!/usr/bin/env python3
"""
QCD Running of the b-quark Yukawa Coupling
===========================================

Computes the QCD running factor for Model B's b-quark mass prediction.

Model B gives n_b = 1 geometrically, so:
    m_b^{bare} = A_b * alpha * v/sqrt(2) = A_b * 1270 MeV

The observed m_b(m_b) = 4180 MeV (MS-bar), requiring A_b ~ 3.29.

This script computes whether QCD running from mu = v/sqrt(2) = 174 GeV
down to mu = alpha * v/sqrt(2) = 1.27 GeV can produce A_b ~ 3.29.

Uses the standard RG running of the quark mass:
    m(mu1)/m(mu2) = [alpha_s(mu1)/alpha_s(mu2)]^{d_m}
where d_m = gamma_m^(0) / (2 * beta_0) is the 1-loop mass anomalous
dimension exponent.
"""

import math
import numpy as np

# =====================================================================
# Physical constants
# =====================================================================
alpha_em = 1.0 / 137.035999084   # fine structure constant
v_higgs = 246211.0                # Higgs VEV in MeV (246.211 GeV)
v_over_sqrt2 = v_higgs / math.sqrt(2)  # ~174,100 MeV
alpha_s_MZ = 0.1179              # strong coupling at M_Z
M_Z = 91187.6                    # Z mass in MeV (91.1876 GeV)
m_b_obs = 4180.0                 # m_b(m_b) MS-bar in MeV
m_c = 1270.0                     # m_c(m_c) MS-bar in MeV (threshold)
m_t = 172500.0                   # top quark pole mass in MeV

# Model B parameters
mu_high = v_over_sqrt2            # 174,100 MeV
mu_low = alpha_em * v_over_sqrt2  # ~1270 MeV
n_b = 1                          # geometric exponent

print("=" * 70)
print("QCD RUNNING OF b-QUARK YUKAWA: MODEL B ANALYSIS")
print("=" * 70)
print(f"\nPhysical parameters:")
print(f"  alpha_em          = 1/{1/alpha_em:.6f}")
print(f"  v/sqrt(2)         = {v_over_sqrt2:.1f} MeV = {v_over_sqrt2/1000:.2f} GeV")
print(f"  alpha * v/sqrt(2) = {mu_low:.1f} MeV = {mu_low/1000:.4f} GeV")
print(f"  alpha_s(M_Z)      = {alpha_s_MZ}")
print(f"  m_b(m_b) [obs]    = {m_b_obs} MeV")

# =====================================================================
# QCD beta function coefficients
# =====================================================================
# beta_0 = (33 - 2*n_f) / (12*pi)
# beta_1 = (153 - 19*n_f) / (24*pi^2)
# For the Yukawa/mass running:
# gamma_m^(0) = 8 / (4*pi) = 2/pi  (but conventionally gamma_0 = 8)
# The mass anomalous dimension at 1-loop: gamma_m = gamma_0 * alpha_s/(4*pi)
# gamma_0 = 8 (in SU(3) fundamental rep: 2*C_F*3 = 8 with C_F=4/3...
#   actually gamma_0 = 6*C_F = 6*(4/3) = 8)

def beta_0(nf):
    """1-loop QCD beta function coefficient: beta_0 = (33 - 2*nf)/(12*pi)"""
    return (33 - 2 * nf) / (12 * math.pi)

def beta_1(nf):
    """2-loop QCD beta function coefficient"""
    return (153 - 19 * nf) / (24 * math.pi**2)

# Mass anomalous dimension coefficients
# gamma_0 = 8  (1-loop, for quark mass in QCD)
# gamma_1 = (404/3 - 40*nf/9) / (4*pi)  -- but we need it in the right normalization
gamma_0 = 8.0  # 1-loop mass anomalous dimension coefficient

def gamma_1(nf):
    """2-loop mass anomalous dimension coefficient"""
    return (404.0/3.0 - 40.0*nf/9.0)

# The 1-loop running mass ratio:
# m(mu1)/m(mu2) = [alpha_s(mu1)/alpha_s(mu2)]^{gamma_0/(2*beta_0_coeff)}
# where beta_0_coeff = (33 - 2*nf)/3  (the coefficient in the convention
#   d(alpha_s)/d(ln mu^2) = -beta_0_coeff * alpha_s^2 / (4*pi))
#
# More precisely, d_m = gamma_0 / (2 * b_0) where b_0 = (33-2*nf)/3
# in the convention beta(g) = -b_0 * g^3/(16*pi^2) - ...

def d_m_1loop(nf):
    """1-loop mass anomalous dimension exponent d_m = gamma_0/(2*b_0)"""
    b0 = (33 - 2*nf) / 3.0
    return gamma_0 / (2.0 * b0)

# =====================================================================
# alpha_s running (1-loop and 2-loop)
# =====================================================================

def alpha_s_1loop(mu, alpha_s_ref, mu_ref, nf):
    """1-loop running of alpha_s.
    alpha_s(mu) = alpha_s(mu_ref) / (1 + alpha_s(mu_ref)*b0*ln(mu^2/mu_ref^2)/(4*pi))
    where b0 = (33-2*nf)/3
    """
    b0 = (33 - 2*nf) / 3.0
    L = math.log(mu**2 / mu_ref**2)
    return alpha_s_ref / (1.0 + alpha_s_ref * b0 * L / (4.0 * math.pi))

def alpha_s_2loop(mu, alpha_s_ref, mu_ref, nf):
    """2-loop running of alpha_s using iterative solution.
    Uses the 2-loop beta function:
    beta = -b0*alpha_s^2/(2*pi) - b1*alpha_s^3/(4*pi^2)
    where b0 = (33-2*nf)/6, b1 = (153-19*nf)/12

    We solve numerically using RK4.
    """
    b0 = (33.0 - 2*nf) / 6.0
    b1 = (153.0 - 19*nf) / 12.0

    def beta_func(t, a_s):
        """da_s/dt where t = ln(mu/mu_ref)"""
        return -a_s**2 / math.pi * (b0 + b1 * a_s / (2*math.pi))

    t_target = math.log(mu / mu_ref)
    n_steps = 10000
    dt = t_target / n_steps
    a_s = alpha_s_ref
    t = 0.0

    for _ in range(n_steps):
        k1 = beta_func(t, a_s)
        k2 = beta_func(t + dt/2, a_s + dt*k1/2)
        k3 = beta_func(t + dt/2, a_s + dt*k2/2)
        k4 = beta_func(t + dt, a_s + dt*k3)
        a_s += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0
        t += dt

    return a_s

# =====================================================================
# Step-by-step running with flavor thresholds
# =====================================================================
# mu = 174 GeV: nf=6 (top is active)  -- actually top threshold ~ 172.5 GeV
# mu = 172.5 GeV down to ~4.18 GeV: nf=5
# mu = 4.18 GeV down to ~1.27 GeV: nf=4
# mu = 1.27 GeV: nf=3 below, but we stop here

print("\n" + "=" * 70)
print("STEP 1: RUN alpha_s FROM M_Z TO RELEVANT SCALES")
print("=" * 70)

# Run alpha_s from M_Z up to mu_high = 174 GeV (nf=5, then cross top threshold)
# First: M_Z -> m_t with nf=5
alpha_s_mt_1L = alpha_s_1loop(m_t, alpha_s_MZ, M_Z, 5)
alpha_s_mt_2L = alpha_s_2loop(m_t, alpha_s_MZ, M_Z, 5)
print(f"\nalpha_s at m_t = {m_t/1000:.1f} GeV:")
print(f"  1-loop: {alpha_s_mt_1L:.6f}")
print(f"  2-loop: {alpha_s_mt_2L:.6f}")

# m_t -> mu_high with nf=6
alpha_s_high_1L = alpha_s_1loop(mu_high, alpha_s_mt_1L, m_t, 6)
alpha_s_high_2L = alpha_s_2loop(mu_high, alpha_s_mt_2L, m_t, 6)
print(f"\nalpha_s at mu_high = v/sqrt(2) = {mu_high/1000:.2f} GeV:")
print(f"  1-loop: {alpha_s_high_1L:.6f}")
print(f"  2-loop: {alpha_s_high_2L:.6f}")

# Run alpha_s from M_Z down to m_b with nf=5
alpha_s_mb_1L = alpha_s_1loop(m_b_obs, alpha_s_MZ, M_Z, 5)
alpha_s_mb_2L = alpha_s_2loop(m_b_obs, alpha_s_MZ, M_Z, 5)
print(f"\nalpha_s at m_b = {m_b_obs/1000:.2f} GeV:")
print(f"  1-loop: {alpha_s_mb_1L:.6f}")
print(f"  2-loop: {alpha_s_mb_2L:.6f}")
print(f"  (PDG value: ~0.2268)")

# Run alpha_s from m_b down to m_c with nf=4
alpha_s_mc_1L = alpha_s_1loop(m_c, alpha_s_mb_1L, m_b_obs, 4)
alpha_s_mc_2L = alpha_s_2loop(m_c, alpha_s_mb_2L, m_b_obs, 4)
print(f"\nalpha_s at m_c = {m_c/1000:.2f} GeV:")
print(f"  1-loop: {alpha_s_mc_1L:.6f}")
print(f"  2-loop: {alpha_s_mc_2L:.6f}")
print(f"  (PDG value: ~0.39)")

# Run alpha_s to mu_low = 1.27 GeV with nf=4
# (mu_low ~ m_c, so alpha_s(mu_low) ~ alpha_s(m_c))
alpha_s_low_1L = alpha_s_mc_1L  # mu_low ~ m_c
alpha_s_low_2L = alpha_s_mc_2L
print(f"\nalpha_s at mu_low = {mu_low/1000:.4f} GeV:")
print(f"  1-loop: {alpha_s_low_1L:.6f}")
print(f"  2-loop: {alpha_s_low_2L:.6f}")

# =====================================================================
# Step 2: Compute mass running factor
# =====================================================================
print("\n" + "=" * 70)
print("STEP 2: QCD MASS RUNNING FACTOR")
print("=" * 70)

# The running factor for the Yukawa coupling / running mass from
# mu_high = 174 GeV down to mu_low = 1.27 GeV.
#
# At 1-loop, the running mass ratio across a region with fixed nf is:
#   m(mu1)/m(mu2) = [alpha_s(mu1)/alpha_s(mu2)]^{d_m(nf)}
# where d_m(nf) = gamma_0 / (2 * (33-2*nf)/3) = 12 / (33-2*nf)
#
# gamma_0 = 8 => d_m = 8 / (2*(33-2*nf)/3) = 12/(33-2*nf)

print(f"\nMass anomalous dimension exponent d_m = 12/(33-2*nf):")
for nf in [3, 4, 5, 6]:
    print(f"  nf={nf}: d_m = 12/{33-2*nf} = {12.0/(33-2*nf):.6f}")

# Segment 1: mu_high (174 GeV) -> m_t (172.5 GeV) with nf=6
# This is a tiny interval, nearly unity
d_m_6 = 12.0 / (33 - 12)
ratio_seg1_1L = (alpha_s_mt_1L / alpha_s_high_1L) ** d_m_6
ratio_seg1_2L = (alpha_s_mt_2L / alpha_s_high_2L) ** d_m_6
print(f"\nSegment 1: mu={mu_high/1000:.1f} GeV -> {m_t/1000:.1f} GeV (nf=6)")
print(f"  d_m(6)   = {d_m_6:.6f}")
print(f"  alpha_s ratio = {alpha_s_mt_1L/alpha_s_high_1L:.6f} (1-loop)")
print(f"  Running factor (1-loop): {ratio_seg1_1L:.6f}")
print(f"  Running factor (2-loop): {ratio_seg1_2L:.6f}")

# Segment 2: m_t (172.5 GeV) -> m_b (4.18 GeV) with nf=5
d_m_5 = 12.0 / (33 - 10)
alpha_s_mb_from_mt_1L = alpha_s_1loop(m_b_obs, alpha_s_mt_1L, m_t, 5)
alpha_s_mb_from_mt_2L = alpha_s_2loop(m_b_obs, alpha_s_mt_2L, m_t, 5)
# But we already have alpha_s_mb from M_Z; use consistent values
ratio_seg2_1L = (alpha_s_mb_1L / alpha_s_mt_1L) ** d_m_5
ratio_seg2_2L = (alpha_s_mb_2L / alpha_s_mt_2L) ** d_m_5
print(f"\nSegment 2: {m_t/1000:.1f} GeV -> {m_b_obs/1000:.2f} GeV (nf=5)")
print(f"  d_m(5)   = {d_m_5:.6f}")
print(f"  alpha_s ratio = {alpha_s_mb_1L/alpha_s_mt_1L:.6f} (1-loop)")
print(f"  Running factor (1-loop): {ratio_seg2_1L:.6f}")
print(f"  Running factor (2-loop): {ratio_seg2_2L:.6f}")

# Segment 3: m_b (4.18 GeV) -> mu_low (1.27 GeV) with nf=4
d_m_4 = 12.0 / (33 - 8)
ratio_seg3_1L = (alpha_s_mc_1L / alpha_s_mb_1L) ** d_m_4
ratio_seg3_2L = (alpha_s_mc_2L / alpha_s_mb_2L) ** d_m_4
print(f"\nSegment 3: {m_b_obs/1000:.2f} GeV -> {mu_low/1000:.4f} GeV (nf=4)")
print(f"  d_m(4)   = {d_m_4:.6f}")
print(f"  alpha_s ratio = {alpha_s_mc_1L/alpha_s_mb_1L:.6f} (1-loop)")
print(f"  Running factor (1-loop): {ratio_seg3_1L:.6f}")
print(f"  Running factor (2-loop): {ratio_seg3_2L:.6f}")

# Total running factor
R_total_1L = ratio_seg1_1L * ratio_seg2_1L * ratio_seg3_1L
R_total_2L = ratio_seg1_2L * ratio_seg2_2L * ratio_seg3_2L
print(f"\n{'='*70}")
print(f"TOTAL RUNNING FACTOR  m(mu_low) / m(mu_high):")
print(f"  1-loop: R = {R_total_1L:.6f}")
print(f"  2-loop: R = {R_total_2L:.6f}")
print(f"{'='*70}")

# =====================================================================
# Step 3: Interpretation for Model B
# =====================================================================
print("\n" + "=" * 70)
print("STEP 3: MODEL B INTERPRETATION")
print("=" * 70)

print(f"\nModel B bare mass formula:")
print(f"  m_b^bare = A_b * alpha^{{n_b}} * v/sqrt(2)")
print(f"  With n_b = 1: m_b^bare = A_b * {alpha_em:.6e} * {v_over_sqrt2:.1f} MeV")
print(f"                         = A_b * {alpha_em * v_over_sqrt2:.2f} MeV")

print(f"\nTarget: m_b(m_b) = {m_b_obs} MeV")
print(f"  => A_b = {m_b_obs:.0f} / {alpha_em * v_over_sqrt2:.2f} = {m_b_obs / (alpha_em * v_over_sqrt2):.4f}")

print(f"\nBUT: The Yukawa is defined at the high scale mu_high = {mu_high/1000:.1f} GeV.")
print(f"Running it down to mu_low = {mu_low/1000:.2f} GeV amplifies the mass by R.")
print(f"So the 'bare' Yukawa at the high scale gives a LARGER running mass at low scale.")
print(f"\nActually, m(mu_low) = R * m(mu_high), with R > 1 when running DOWN")
print(f"(since alpha_s grows at low energies, the running mass increases).")
print(f"\nSo if the DFD formula gives m at the high scale mu_high:")
print(f"  m(mu_high) = A_b * alpha * v/sqrt(2)")
print(f"  m(mu_low)  = R * A_b * alpha * v/sqrt(2)")
print(f"\nTo match m_b(m_b) = 4180 MeV, we need:")
print(f"  R * A_b * {alpha_em * v_over_sqrt2:.2f} = {m_b_obs}")
print(f"  A_b = {m_b_obs} / (R * {alpha_em * v_over_sqrt2:.2f})")

# But wait -- m_b(m_b) is defined at mu = m_b = 4.18 GeV, not at mu_low = 1.27 GeV.
# The DFD scale is mu_low, so we need to run from mu_high to mu = m_b.
# Then compare with m_b(m_b).

print(f"\n{'='*70}")
print(f"CORRECTION: m_b(m_b) is defined at mu = m_b, not at mu_low")
print(f"{'='*70}")

# Running from mu_high to m_b only (segments 1+2):
R_to_mb_1L = ratio_seg1_1L * ratio_seg2_1L
R_to_mb_2L = ratio_seg1_2L * ratio_seg2_2L
print(f"\nRunning factor from {mu_high/1000:.1f} GeV to {m_b_obs/1000:.2f} GeV:")
print(f"  1-loop: R_mb = {R_to_mb_1L:.6f}")
print(f"  2-loop: R_mb = {R_to_mb_2L:.6f}")

# If DFD sets Yukawa at mu_high, then physical m_b(m_b) = R_mb * y_b(mu_high) * v/sqrt(2)
# Wait -- this isn't quite right either. The DFD formula m = A * alpha^n * v/sqrt(2)
# is claimed for the PHYSICAL mass. The question is whether QCD running provides
# the factor A_b ~ 3.29.

# Let's think about it differently:
# If DFD at the high scale gives y_b(mu_high) * v/sqrt(2) = alpha * v/sqrt(2) = 1270 MeV
# (with A_b=1), then running down to m_b gives:
# m_b(m_b) = R_mb * 1270 MeV

m_predicted_1L = R_to_mb_1L * alpha_em * v_over_sqrt2
m_predicted_2L = R_to_mb_2L * alpha_em * v_over_sqrt2
print(f"\nIf A_b = 1 at high scale, DFD gives m_b(mu_high) = {alpha_em * v_over_sqrt2:.2f} MeV")
print(f"Running to m_b scale:")
print(f"  m_b(m_b) predicted (1-loop): {m_predicted_1L:.2f} MeV")
print(f"  m_b(m_b) predicted (2-loop): {m_predicted_2L:.2f} MeV")
print(f"  m_b(m_b) observed:           {m_b_obs:.2f} MeV")
print(f"\nEffective A_b from QCD running alone: {m_predicted_2L / (alpha_em * v_over_sqrt2):.4f}")
print(f"Needed A_b without running:           {m_b_obs / (alpha_em * v_over_sqrt2):.4f}")
print(f"Remaining prefactor needed:           {m_b_obs / m_predicted_2L:.4f}")

# =====================================================================
# Step 4: Full running to 1.27 GeV
# =====================================================================
print(f"\n{'='*70}")
print(f"STEP 4: FULL RUNNING TO mu_low = 1.27 GeV")
print(f"{'='*70}")

m_at_low_1L = R_total_1L * alpha_em * v_over_sqrt2
m_at_low_2L = R_total_2L * alpha_em * v_over_sqrt2
print(f"\nIf A_b = 1, running from {mu_high/1000:.1f} GeV to {mu_low/1000:.2f} GeV:")
print(f"  m_b(1.27 GeV) predicted (1-loop): {m_at_low_1L:.2f} MeV")
print(f"  m_b(1.27 GeV) predicted (2-loop): {m_at_low_2L:.2f} MeV")
print(f"\nEffective A_b from full QCD running: {R_total_2L:.4f}")

# =====================================================================
# Step 5: Comparison with pi
# =====================================================================
print(f"\n{'='*70}")
print(f"STEP 5: COMPARISON WITH A_b = pi")
print(f"{'='*70}")

A_b_pi = math.pi
m_pi_high = A_b_pi * alpha_em * v_over_sqrt2
m_pi_mb_1L = R_to_mb_1L * m_pi_high
m_pi_mb_2L = R_to_mb_2L * m_pi_high
m_pi_low_1L = R_total_1L * m_pi_high
m_pi_low_2L = R_total_2L * m_pi_high

print(f"\nWith A_b = pi = {math.pi:.6f}:")
print(f"  m_b(mu_high) = pi * alpha * v/sqrt(2) = {m_pi_high:.2f} MeV")
print(f"  m_b(m_b) after running (1-loop): {m_pi_mb_1L:.2f} MeV")
print(f"  m_b(m_b) after running (2-loop): {m_pi_mb_2L:.2f} MeV")
print(f"  m_b(1.27 GeV) after running (1-loop): {m_pi_low_1L:.2f} MeV")
print(f"  m_b(1.27 GeV) after running (2-loop): {m_pi_low_2L:.2f} MeV")
print(f"  Observed m_b(m_b) = {m_b_obs} MeV")
print(f"  Ratio predicted/observed (at m_b, 2-loop): {m_pi_mb_2L/m_b_obs:.4f}")

# =====================================================================
# Step 6: What A_b is needed?
# =====================================================================
print(f"\n{'='*70}")
print(f"STEP 6: REQUIRED A_b VALUES")
print(f"{'='*70}")

A_b_needed_no_running = m_b_obs / (alpha_em * v_over_sqrt2)
A_b_needed_with_running_1L = m_b_obs / (R_to_mb_1L * alpha_em * v_over_sqrt2)
A_b_needed_with_running_2L = m_b_obs / (R_to_mb_2L * alpha_em * v_over_sqrt2)

print(f"\nTo reproduce m_b(m_b) = {m_b_obs} MeV with m = A_b * alpha * v/sqrt(2):")
print(f"  Without QCD running:          A_b = {A_b_needed_no_running:.4f}")
print(f"  With 1-loop QCD running:      A_b = {A_b_needed_with_running_1L:.4f}")
print(f"  With 2-loop QCD running:      A_b = {A_b_needed_with_running_2L:.4f}")
print(f"\n  pi = {math.pi:.4f}")
print(f"  pi is {'CONSISTENT' if abs(A_b_needed_with_running_2L - math.pi) / math.pi < 0.15 else 'NOT consistent'} with A_b (2-loop)")
print(f"  Ratio A_b_needed / pi = {A_b_needed_with_running_2L / math.pi:.4f}")

# =====================================================================
# Step 7: Model A comparison
# =====================================================================
print(f"\n{'='*70}")
print(f"STEP 7: MODEL A COMPARISON")
print(f"{'='*70}")

A_b_modelA = 1.0 / 42.0
m_b_modelA = A_b_modelA * v_over_sqrt2
print(f"\nModel A: n_b = 0, A_b = 1/42 = {A_b_modelA:.6f}")
print(f"  m_b = (1/42) * v/sqrt(2) = {m_b_modelA:.2f} MeV")
print(f"  Observed: {m_b_obs} MeV")
print(f"  Ratio: {m_b_modelA/m_b_obs:.4f}")

# =====================================================================
# Step 8: Detailed alpha_s profile
# =====================================================================
print(f"\n{'='*70}")
print(f"STEP 8: alpha_s PROFILE (2-loop)")
print(f"{'='*70}")

scales = [1.27, 2.0, 3.0, 4.18, 5.0, 10.0, 30.0, 50.0, 91.2, 174.1]
print(f"\n  {'mu (GeV)':>10}  {'alpha_s':>10}  {'nf':>4}")
print(f"  {'-'*10}  {'-'*10}  {'-'*4}")

for mu_GeV in scales:
    mu_MeV = mu_GeV * 1000
    if mu_MeV > m_t:
        nf = 6
        a_s = alpha_s_2loop(mu_MeV, alpha_s_mt_2L, m_t, 6)
    elif mu_MeV > m_b_obs:
        nf = 5
        a_s = alpha_s_2loop(mu_MeV, alpha_s_MZ, M_Z, 5)
    elif mu_MeV > m_c:
        nf = 4
        a_s = alpha_s_2loop(mu_MeV, alpha_s_mb_2L, m_b_obs, 4)
    else:
        nf = 4  # at threshold
        a_s = alpha_s_mc_2L
    print(f"  {mu_GeV:10.2f}  {a_s:10.6f}  {nf:4d}")

# =====================================================================
# Summary
# =====================================================================
print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"""
Model B with n_b = 1:
  Bare scale: alpha * v/sqrt(2) = {alpha_em * v_over_sqrt2:.2f} MeV

QCD running factor (mu_high -> m_b, 2-loop): R = {R_to_mb_2L:.4f}
QCD running factor (mu_high -> mu_low, 2-loop): R = {R_total_2L:.4f}

Without QCD running: A_b needed = {A_b_needed_no_running:.4f}  (= {m_b_obs:.0f}/{alpha_em*v_over_sqrt2:.0f})
With QCD running to m_b: A_b needed = {A_b_needed_with_running_2L:.4f}

QCD running alone (A_b=1) gives m_b(m_b) = {m_predicted_2L:.0f} MeV vs {m_b_obs:.0f} observed.
Running provides a factor of ~{R_to_mb_2L:.2f}, reducing the needed A_b from
{A_b_needed_no_running:.2f} to {A_b_needed_with_running_2L:.2f}.

Comparison with pi = {math.pi:.4f}:
  A_b = pi WITH running gives m_b(m_b) = {m_pi_mb_2L:.0f} MeV (obs: {m_b_obs})
  Discrepancy: {abs(m_pi_mb_2L - m_b_obs)/m_b_obs * 100:.1f}%

CONCLUSION: QCD running from v/sqrt(2) to m_b provides a factor R ~ {R_to_mb_2L:.2f}.
This is substantial but NOT sufficient to explain A_b ~ 3.29 from A_b = 1.
The running reduces the needed prefactor from ~3.29 to ~{A_b_needed_with_running_2L:.2f}.
A prefactor A_b = pi = {math.pi:.4f} {'IS' if abs(A_b_needed_with_running_2L - math.pi)/math.pi < 0.15 else 'is NOT'} within {abs(A_b_needed_with_running_2L - math.pi)/math.pi*100:.0f}% of the needed value.
""")
