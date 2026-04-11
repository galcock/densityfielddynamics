#!/usr/bin/env python3
"""
Full QCD running of the b-quark mass from M_Planck down to mu = 1.27 GeV.

2-loop RG running of alpha_s with threshold matching at m_t, m_b, m_c.
1-loop mass anomalous dimension (gamma_0 = 8, universal).

Purpose: Compute the total running factor R = m_b(1.27 GeV) / m_b(M_P),
then extract A_b^bare from the DFD mass formula
    m_b(m_b) = A_b^bare * alpha * v / sqrt(2)
with the physical value m_b(m_b) = 4180 MeV.

Author: Claude (computation for DFD research)
Date: 2026-03-23
"""

import math

# ============================================================
# PHYSICAL CONSTANTS
# ============================================================
M_P = 1.22089e19       # Planck mass (GeV)
M_Z = 91.1876          # Z boson mass (GeV)
m_t = 172.76           # top quark pole mass (GeV) - threshold
m_b_MSbar = 4.18       # b quark MS-bar mass at m_b (GeV) - threshold
m_c_MSbar = 1.27       # c quark MS-bar mass at m_c (GeV) - threshold
alpha_s_MZ = 0.1179    # alpha_s(M_Z), PDG 2024
alpha_em = 1.0/137.035999084   # fine structure constant
v_higgs = 246.22       # Higgs VEV (GeV)

# Target scale
mu_low = 1.27          # GeV (= m_c, bottom of N_f=4 region)


# ============================================================
# BETA FUNCTION COEFFICIENTS
# ============================================================
def beta_coeffs(nf):
    """Return (beta_0, beta_1) for N_f active flavors.
    Convention: d(alpha_s)/d(ln mu^2) = -beta_0/(2*pi)*alpha_s^2 - beta_1/(4*pi^2)*alpha_s^3 - ...
    beta_0 = (11*N_c - 2*N_f) / 3
    beta_1 = (34*N_c^2 - (10*N_c + 6*C_F)*N_f) / 3  with N_c=3, C_F=4/3
           = (102 - 38*N_f/3)
    """
    Nc = 3
    CF = 4.0/3.0
    b0 = (11*Nc - 2*nf) / 3.0
    b1 = (34*Nc**2 - nf*(10*Nc + 6*CF)) / 3.0
    return b0, b1


def gamma_0():
    """1-loop quark mass anomalous dimension coefficient.
    gamma_m = gamma_0 * alpha_s / (4*pi) + ...
    gamma_0 = 8  (= 6*C_F = 6*4/3 = 8, universal, independent of N_f at 1-loop)
    """
    return 8.0


# ============================================================
# 2-LOOP RUNNING OF alpha_s
# ============================================================
def run_alpha_s_2loop(alpha_s_0, mu_0, mu_f, nf, n_steps=10000):
    """Run alpha_s from mu_0 to mu_f using 2-loop RGE via numerical ODE (RK4).

    d(alpha_s)/d(ln mu) = -beta_0/(2*pi)*alpha_s^2 - beta_1/(4*pi^2)*alpha_s^3

    Note: d/d(ln mu) = 2 * d/d(ln mu^2), so:
    d(alpha_s)/d(ln mu) = -beta_0/pi * alpha_s^2 - beta_1/(2*pi^2) * alpha_s^3

    Wait - let's be careful with conventions.

    Standard: mu * d(alpha_s)/d(mu) = beta(alpha_s)
    beta(alpha_s) = -2*alpha_s * [beta_0 * (alpha_s/(4*pi)) + beta_1 * (alpha_s/(4*pi))^2 + ...]

    So: d(alpha_s)/d(ln mu) = -2*alpha_s * [beta_0*alpha_s/(4*pi) + beta_1*(alpha_s/(4*pi))^2]
                             = -beta_0/(2*pi) * alpha_s^2 - beta_1/(8*pi^2) * alpha_s^3
    """
    b0, b1 = beta_coeffs(nf)

    t0 = math.log(mu_0)
    tf = math.log(mu_f)
    dt = (tf - t0) / n_steps

    a = alpha_s_0
    t = t0

    def beta_func(a_s):
        return -b0/(2*math.pi) * a_s**2 - b1/(8*math.pi**2) * a_s**3

    # RK4 integration
    for _ in range(n_steps):
        k1 = dt * beta_func(a)
        k2 = dt * beta_func(a + k1/2)
        k3 = dt * beta_func(a + k2/2)
        k4 = dt * beta_func(a + k3)
        a = a + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        t += dt

    return a


def run_alpha_s_1loop_analytic(alpha_s_0, mu_0, mu_f, nf):
    """1-loop analytic formula for comparison.
    alpha_s(mu) = alpha_s(mu_0) / [1 + beta_0/(2*pi) * alpha_s(mu_0) * ln(mu/mu_0)]
    """
    b0, _ = beta_coeffs(nf)
    L = math.log(mu_f / mu_0)
    return alpha_s_0 / (1 + b0/(2*math.pi) * alpha_s_0 * L)


# ============================================================
# THRESHOLD MATCHING (1-loop decoupling)
# ============================================================
def match_alpha_s_down(alpha_s_above, nf_above):
    """Match alpha_s when crossing a threshold downward (decoupling a heavy quark).
    At 1-loop: alpha_s is continuous across the threshold.
    At 2-loop there are O(alpha_s^2) corrections, but they are tiny.
    We use continuous matching (standard at 1-loop accuracy in the matching).
    """
    return alpha_s_above


def match_alpha_s_up(alpha_s_below, nf_below):
    """Match alpha_s when crossing a threshold upward.
    Continuous at 1-loop.
    """
    return alpha_s_below


# ============================================================
# MASS RUNNING FACTOR
# ============================================================
def mass_running_ratio(alpha_s_i, alpha_s_f, nf):
    """Compute m(mu_f)/m(mu_i) using 1-loop mass anomalous dimension.

    m(mu_f)/m(mu_i) = [alpha_s(mu_f)/alpha_s(mu_i)]^{gamma_0/(2*beta_0)}

    where gamma_0 = 8 (universal 1-loop mass anomalous dimension)
    and beta_0 = (11*3 - 2*N_f)/3
    """
    b0, _ = beta_coeffs(nf)
    g0 = gamma_0()
    exponent = g0 / (2.0 * b0)
    ratio = (alpha_s_f / alpha_s_i) ** exponent
    return ratio, exponent


# ============================================================
# MAIN COMPUTATION
# ============================================================
def main():
    print("=" * 72)
    print("FULL QCD RUNNING: M_Planck -> 1.27 GeV")
    print("2-loop alpha_s running, 1-loop mass anomalous dimension")
    print("=" * 72)

    # ----------------------------------------------------------
    # STEP 1: Run alpha_s from M_Z up to M_P  (N_f = 5 from M_Z to m_t, then N_f = 6)
    # ----------------------------------------------------------
    print("\n--- STEP 1: Determine alpha_s at all scales ---\n")

    # M_Z -> m_t (N_f = 5)
    alpha_s_mt_below = run_alpha_s_2loop(alpha_s_MZ, M_Z, m_t, nf=5)
    print(f"alpha_s(M_Z)   = {alpha_s_MZ:.6f}   [input, PDG 2024]")
    print(f"alpha_s(m_t-)  = {alpha_s_mt_below:.6f}   [N_f=5, 2-loop running]")

    # Match at m_t: N_f = 5 -> 6
    alpha_s_mt_above = match_alpha_s_up(alpha_s_mt_below, nf_below=5)
    print(f"alpha_s(m_t+)  = {alpha_s_mt_above:.6f}   [matched, N_f -> 6]")

    # m_t -> M_P (N_f = 6)
    alpha_s_MP = run_alpha_s_2loop(alpha_s_mt_above, m_t, M_P, nf=6)
    print(f"alpha_s(M_P)   = {alpha_s_MP:.8f}   [N_f=6, 2-loop running]")
    print(f"  = 1/{1.0/alpha_s_MP:.2f}")

    # 1-loop comparison
    alpha_s_MP_1loop = run_alpha_s_1loop_analytic(alpha_s_mt_above, m_t, M_P, nf=6)
    print(f"alpha_s(M_P) [1-loop analytic] = {alpha_s_MP_1loop:.8f}")

    # ----------------------------------------------------------
    # STEP 2: Run alpha_s from M_Z down to 1.27 GeV
    # ----------------------------------------------------------
    print()

    # M_Z -> m_b (N_f = 5)
    alpha_s_mb = run_alpha_s_2loop(alpha_s_MZ, M_Z, m_b_MSbar, nf=5)
    print(f"alpha_s(m_b)   = {alpha_s_mb:.6f}   [N_f=5, 2-loop running]")

    # Match at m_b: N_f = 5 -> 4
    alpha_s_mb_below = match_alpha_s_down(alpha_s_mb, nf_above=5)
    print(f"alpha_s(m_b-)  = {alpha_s_mb_below:.6f}   [matched, N_f -> 4]")

    # m_b -> m_c (N_f = 4)
    alpha_s_mc = run_alpha_s_2loop(alpha_s_mb_below, m_b_MSbar, m_c_MSbar, nf=4)
    print(f"alpha_s(m_c)   = {alpha_s_mc:.6f}   [N_f=4, 2-loop running]")

    # Match at m_c: N_f = 4 -> 3
    alpha_s_mc_below = match_alpha_s_down(alpha_s_mc, nf_above=4)
    print(f"alpha_s(m_c-)  = {alpha_s_mc_below:.6f}   [matched, N_f -> 3]")

    # ----------------------------------------------------------
    # STEP 3: Compute mass running ratios in each region
    # ----------------------------------------------------------
    print("\n--- STEP 2: Mass running ratios in each region ---\n")

    # Region 1: M_P -> m_t (N_f = 6)
    R1, exp1 = mass_running_ratio(alpha_s_MP, alpha_s_mt_above, nf=6)
    b0_6 = beta_coeffs(6)[0]
    print(f"Region M_P -> m_t  (N_f=6):  beta_0 = {b0_6:.4f},  gamma_0/(2*beta_0) = {gamma_0()/(2*b0_6):.6f}")
    print(f"  alpha_s ratio = {alpha_s_mt_above/alpha_s_MP:.6f}")
    print(f"  R1 = [alpha_s(m_t)/alpha_s(M_P)]^{exp1:.6f} = {R1:.6f}")

    # Region 2: m_t -> m_b (N_f = 5)
    # Need alpha_s at m_t from N_f=5 side and at m_b
    R2, exp2 = mass_running_ratio(alpha_s_mt_below, alpha_s_mb, nf=5)
    b0_5 = beta_coeffs(5)[0]
    print(f"\nRegion m_t -> m_b  (N_f=5):  beta_0 = {b0_5:.4f},  gamma_0/(2*beta_0) = {gamma_0()/(2*b0_5):.6f}")
    print(f"  alpha_s ratio = {alpha_s_mb/alpha_s_mt_below:.6f}")
    print(f"  R2 = [alpha_s(m_b)/alpha_s(m_t)]^{exp2:.6f} = {R2:.6f}")

    # Region 3: m_b -> m_c (N_f = 4)
    R3, exp3 = mass_running_ratio(alpha_s_mb_below, alpha_s_mc, nf=4)
    b0_4 = beta_coeffs(4)[0]
    print(f"\nRegion m_b -> m_c  (N_f=4):  beta_0 = {b0_4:.4f},  gamma_0/(2*beta_0) = {gamma_0()/(2*b0_4):.6f}")
    print(f"  alpha_s ratio = {alpha_s_mc/alpha_s_mb_below:.6f}")
    print(f"  R3 = [alpha_s(m_c)/alpha_s(m_b)]^{exp3:.6f} = {R3:.6f}")

    # Total running factor: m(1.27 GeV) / m(M_P)
    R_total = R1 * R2 * R3
    print(f"\n--- STEP 3: Total running factor ---")
    print(f"\nR_total = R1 * R2 * R3 = {R1:.6f} * {R2:.6f} * {R3:.6f}")
    print(f"R_total = {R_total:.6f}")
    print(f"1/R_total = {1.0/R_total:.6f}")

    # ----------------------------------------------------------
    # STEP 4: Also compute m_b(m_b) from m_b(m_c = 1.27 GeV)
    # Actually, let's compute m_b(m_b) / m_b(M_P) directly
    # ----------------------------------------------------------
    # Running from M_P to m_b:
    # Region 1: M_P -> m_t (N_f = 6)  -> R1 (already computed)
    # Region 2: m_t -> m_b (N_f = 5)  -> R2 (already computed)
    R_MP_to_mb = R1 * R2
    print(f"\nR(M_P -> m_b) = R1 * R2 = {R_MP_to_mb:.6f}")
    print(f"  This is m_b(m_b) / m_b(M_P)")

    # ----------------------------------------------------------
    # STEP 5: Extract A_b^bare from DFD formula
    # ----------------------------------------------------------
    print("\n--- STEP 4: DFD bare Yukawa extraction ---\n")

    # DFD formula: m_b(M_P) = A_b^bare * alpha * v / sqrt(2)
    # Physical: m_b(m_b) = R_MP_to_mb * m_b(M_P)
    # So: m_b(m_b) = R_MP_to_mb * A_b^bare * alpha * v / sqrt(2)
    # Solving: A_b^bare = m_b(m_b) / (R_MP_to_mb * alpha * v / sqrt(2))

    m_b_phys = 4.18  # GeV, m_b(m_b) in MS-bar

    factor = alpha_em * v_higgs / math.sqrt(2)
    print(f"alpha_em = {alpha_em:.10f}")
    print(f"v / sqrt(2) = {v_higgs/math.sqrt(2):.4f} GeV")
    print(f"alpha * v / sqrt(2) = {factor:.6f} GeV = {factor*1000:.4f} MeV")

    # Bare Yukawa at M_P
    m_b_at_MP = m_b_phys / R_MP_to_mb
    print(f"\nm_b(M_P) = m_b(m_b) / R(M_P->m_b) = {m_b_phys:.4f} / {R_MP_to_mb:.6f}")
    print(f"m_b(M_P) = {m_b_at_MP:.6f} GeV = {m_b_at_MP*1000:.4f} MeV")

    A_b_bare = m_b_phys / (R_MP_to_mb * factor)
    print(f"\nA_b^bare = m_b(m_b) / (R * alpha * v/sqrt(2))")
    print(f"A_b^bare = {m_b_phys:.4f} / ({R_MP_to_mb:.6f} * {factor:.6f})")
    print(f"A_b^bare = {A_b_bare:.6f}")
    print(f"1/A_b^bare = {1.0/A_b_bare:.6f}")

    # Also try with running from M_P to m_c (= 1.27 GeV):
    m_b_at_mc = m_b_phys * R3  # running from m_b down to m_c
    # Actually m_b(m_c)/m_b(m_b) = R3 if we ran from m_b to m_c
    # But R3 was computed as [alpha_s(m_c)/alpha_s(m_b)]^exponent
    # For mass: m(m_c) = m(m_b) * R3
    print(f"\nm_b(m_c = 1.27 GeV) = m_b(m_b) * R3 = {m_b_phys:.4f} * {R3:.6f}")
    print(f"m_b(1.27 GeV) = {m_b_at_mc:.4f} GeV = {m_b_at_mc*1000:.2f} MeV")

    # ----------------------------------------------------------
    # STEP 6: Alternative: Use Yukawa y_b = sqrt(2)*m_b/v
    # ----------------------------------------------------------
    print("\n--- STEP 5: Yukawa coupling values ---\n")

    y_b_at_mb = math.sqrt(2) * m_b_phys / v_higgs
    print(f"y_b(m_b) = sqrt(2) * m_b(m_b) / v = {y_b_at_mb:.6f}")

    y_b_at_MP = math.sqrt(2) * m_b_at_MP / v_higgs
    print(f"y_b(M_P) = sqrt(2) * m_b(M_P) / v = {y_b_at_MP:.8f}")

    # In DFD: y_b(M_P) = A_b^bare * alpha_em * sqrt(2) * sqrt(2) / (sqrt(2))
    # Actually: m = y * v / sqrt(2), so y = sqrt(2)*m/v
    # DFD: m(M_P) = A_b^bare * alpha * v/sqrt(2)
    # So: y_b(M_P) = sqrt(2) * A_b^bare * alpha * v/sqrt(2) / v = A_b^bare * alpha
    y_b_DFD = A_b_bare * alpha_em
    print(f"y_b(M_P) from DFD = A_b^bare * alpha = {y_b_DFD:.8f}")
    print(f"Consistency check: {abs(y_b_at_MP - y_b_DFD)/y_b_at_MP:.2e} relative error")

    # ----------------------------------------------------------
    # STEP 7: Check recognizable numbers
    # ----------------------------------------------------------
    print("\n--- STEP 6: Pattern recognition for A_b^bare ---\n")
    print(f"A_b^bare = {A_b_bare:.8f}")
    print(f"A_b^bare / pi = {A_b_bare/math.pi:.8f}")
    print(f"A_b^bare * pi = {A_b_bare*math.pi:.8f}")
    print(f"A_b^bare^2 = {A_b_bare**2:.8f}")
    print(f"sqrt(A_b^bare) = {math.sqrt(A_b_bare):.8f}")
    print(f"ln(A_b^bare) = {math.log(A_b_bare):.8f}")
    print(f"A_b^bare / alpha_em = {A_b_bare/alpha_em:.4f}")
    print(f"A_b^bare * 137 = {A_b_bare*137:.6f}")
    print(f"A_b^bare * 12 = {A_b_bare*12:.6f}")
    print(f"A_b^bare * 60 = {A_b_bare*60:.6f}")
    print(f"A_b^bare * 120 = {A_b_bare*120:.6f}")

    # Check simple fractions
    print("\nSimple fraction check:")
    for num in range(1, 30):
        for den in range(1, 30):
            frac = num / den
            if abs(frac - A_b_bare) / A_b_bare < 0.01:
                print(f"  {num}/{den} = {frac:.6f}  (error: {abs(frac-A_b_bare)/A_b_bare*100:.2f}%)")

    # Check A_5 group order = 60
    print(f"\nA_5 related:")
    print(f"  A_b^bare / 60 = {A_b_bare/60:.8f}")
    print(f"  A_b^bare / (60/pi) = {A_b_bare/(60/math.pi):.8f}")

    # ----------------------------------------------------------
    # SUMMARY TABLE
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("SUMMARY TABLE")
    print("=" * 72)
    print(f"{'Scale':>20s}  {'alpha_s':>12s}  {'N_f':>4s}")
    print("-" * 42)
    print(f"{'M_P = 1.22e19 GeV':>20s}  {alpha_s_MP:12.8f}  {'6':>4s}")
    print(f"{'m_t = 172.76 GeV':>20s}  {alpha_s_mt_above:12.6f}  {'6->5':>4s}")
    print(f"{'M_Z = 91.19 GeV':>20s}  {alpha_s_MZ:12.6f}  {'5':>4s}")
    print(f"{'m_b = 4.18 GeV':>20s}  {alpha_s_mb:12.6f}  {'5->4':>4s}")
    print(f"{'m_c = 1.27 GeV':>20s}  {alpha_s_mc:12.6f}  {'4->3':>4s}")

    print(f"\n{'Region':>25s}  {'N_f':>4s}  {'gamma_0/(2*beta_0)':>18s}  {'R_i':>10s}")
    print("-" * 65)
    print(f"{'M_P -> m_t':>25s}  {'6':>4s}  {gamma_0()/(2*beta_coeffs(6)[0]):>18.6f}  {R1:>10.6f}")
    print(f"{'m_t -> m_b':>25s}  {'5':>4s}  {gamma_0()/(2*beta_coeffs(5)[0]):>18.6f}  {R2:>10.6f}")
    print(f"{'m_b -> m_c':>25s}  {'4':>4s}  {gamma_0()/(2*beta_coeffs(4)[0]):>18.6f}  {R3:>10.6f}")

    print(f"\nTotal R(M_P -> m_b) = {R_MP_to_mb:.6f}")
    print(f"Total R(M_P -> m_c) = {R_total:.6f}")
    print(f"m_b(M_P) = {m_b_at_MP*1000:.4f} MeV")
    print(f"A_b^bare = {A_b_bare:.6f}")

    return {
        'alpha_s_MP': alpha_s_MP,
        'alpha_s_mt': alpha_s_mt_above,
        'alpha_s_mb': alpha_s_mb,
        'alpha_s_mc': alpha_s_mc,
        'R1': R1, 'R2': R2, 'R3': R3,
        'R_total': R_total,
        'R_MP_to_mb': R_MP_to_mb,
        'm_b_at_MP': m_b_at_MP,
        'A_b_bare': A_b_bare,
    }


if __name__ == "__main__":
    results = main()
