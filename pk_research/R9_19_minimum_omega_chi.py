#!/usr/bin/env python3
"""
R9 Agent 19: Minimum Omega_chi for P(k) Shape Compatibility
=============================================================

KEY QUESTION: What is the MINIMUM Omega_chi needed so that the combined
DFD power spectrum (chi transfer function + MOND growth) matches
observational constraints from BOSS/Planck?

APPROACH:
- Scan Omega_chi from 0.00 to 0.30 in steps of 0.01
- For each: compute EH transfer function T(k; Omega_b + Omega_chi)
- Compute growth factor with MOND-enhanced baryons filling the CDM gap
- Build full P_DFD(k) and compare to LCDM/BOSS
- Find minimum Omega_chi satisfying shape + amplitude + BAO constraints

KEY PHYSICS (from R2 campaign):
The MOND enhancement is an EFFECTIVE constant nu that makes baryons
cluster as if there were more gravitating matter. The growth equation is
LINEAR with Omega_eff = Omega_chi + Omega_b * nu_MOND.
For self-consistency: nu_MOND = (Omega_m_target - Omega_chi) / Omega_b.

The transfer function is the BINDING constraint: it depends on how much
pressureless matter exists pre-recombination. MOND only affects post-
recombination growth, not the transfer function shape.

So the question becomes: at what Omega_chi does the EH transfer function
become close enough to LCDM that the remaining shape differences are
within observational tolerance?

Author: R9 Agent 19 (Claude)
"""

import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================
H0_km_s_Mpc = 67.4
h = H0_km_s_Mpc / 100.0
H0_si = H0_km_s_Mpc * 1e3 / 3.0856775814913673e22

Omega_b_h2 = 0.02237
Omega_b = Omega_b_h2 / h**2          # ~ 0.0493
Omega_CDM_LCDM = 0.266               # CDM density in LCDM
Omega_m_LCDM = 0.315                 # Total matter in LCDM
Omega_Lambda = 0.685

T_CMB = 2.725
n_s = 0.965
A_s = 2.1e-9

a0_MOND = 1.2e-10   # m/s^2
G_N = 6.674e-11
Mpc_m = 3.0856775814913673e22

rho_crit_0 = 3 * H0_si**2 / (8 * np.pi * G_N)

# Targets
SIGMA8_TARGET = 0.811
SIGMA8_TOL = 0.08
SHAPE_TOL = 0.30        # 30% max deviation in P(k)/P_LCDM(k)
BAO_TOL = 0.01          # 1% BAO position

k_grid = np.logspace(-3, 0.5, 2000)  # 0.001 to ~3.16 h/Mpc
k_diag = np.array([0.02, 0.05, 0.10, 0.15])


# =============================================================================
# EISENSTEIN-HU TRANSFER FUNCTION
# =============================================================================
def EH_transfer(k_hMpc, Omega_chi):
    """
    EH98 no-wiggle transfer function for baryons + chi (pressureless).
    omega_m = (Omega_b + Omega_chi) * h^2
    """
    omega_chi = Omega_chi * h**2
    omega_b = Omega_b_h2
    omega_m = omega_b + omega_chi
    if omega_m < 1e-8:
        omega_m = omega_b

    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    f_b = omega_b / omega_m

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * omega_m**(-0.419) * (1 + 0.607 * omega_m**0.674)
    b2 = 0.238 * omega_m**0.223
    z_d = (1291 * omega_m**0.251 / (1 + 0.659 * omega_m**0.828)
           * (1 + b1 * omega_b**b2))

    R_eq = 31.5e3 * omega_b * theta**(-4) / z_eq
    R_d = 31.5e3 * omega_b * theta**(-4) / z_d

    s = ((2.0 / (3 * k_eq)) * np.sqrt(6 / R_eq)
         * np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq))
                  / (1 + np.sqrt(R_eq))))

    alpha_gamma = (1 - 0.328 * np.log(431 * omega_m) * f_b
                   + 0.38 * np.log(22.3 * omega_m) * f_b**2)
    gamma_eff = (omega_m / h
                 * (alpha_gamma + (1 - alpha_gamma)
                    / (1 + (0.43 * k * s)**4)))
    q = k * theta**2 / gamma_eff
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731 / (1 + 62.5 * q)
    T = L / (L + C * q**2)

    return T, s


def EH_transfer_baryon_only(k_hMpc):
    """Pure baryon transfer with Silk damping."""
    omega_m = Omega_b_h2
    omega_b = Omega_b_h2
    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * max(omega_m, 1e-10)**(-0.419) * (1 + 0.607 * max(omega_m, 1e-10)**0.674)
    b2 = 0.238 * max(omega_m, 1e-10)**0.223
    z_d = (1291 * max(omega_m, 1e-10)**0.251
           / (1 + 0.659 * max(omega_m, 1e-10)**0.828)
           * (1 + b1 * omega_b**b2))

    R_eq = 31.5e3 * omega_b * theta**(-4) / max(z_eq, 1)
    R_d = 31.5e3 * omega_b * theta**(-4) / max(z_d, 1)

    s = ((2.0 / (3 * k_eq)) * np.sqrt(6 / max(R_eq, 1e-10))
         * np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq))
                  / (1 + np.sqrt(max(R_eq, 1e-10)))))

    gamma_eff = omega_m / h
    q = k * theta**2 / gamma_eff
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731 / (1 + 62.5 * q)
    T = L / (L + C * q**2)

    k_silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1 + (10.4 * omega_m)**(-0.95))
    silk = np.exp(-(k / k_silk)**1.4)
    ks = k * s
    j0 = np.where(np.abs(ks) < 1e-10, 1.0, np.sin(ks) / ks)
    T_bary = T * (silk * j0 + (1 - silk) * 0.05)

    return T_bary, s


# =============================================================================
# TRANSFER FUNCTION SELECTION
# =============================================================================
def get_transfer(k_hMpc, Omega_chi):
    """
    Get the DFD transfer function for given Omega_chi.
    For Omega_chi = 0: pure baryon (Silk damped)
    For Omega_chi > 0: EH with chi acting as CDM
    """
    if Omega_chi < 1e-6:
        T, s = EH_transfer_baryon_only(k_hMpc)
        return T, s
    else:
        return EH_transfer(k_hMpc, Omega_chi)


# =============================================================================
# GROWTH FACTOR
# =============================================================================
def solve_growth(Omega_source, a_start=1e-4, a_end=1.0):
    """
    Standard linear growth: d'' + (3+dlnH)d' = 1.5*Omega_source/(a^3 E^2) * d
    Background expansion always uses Omega_m_LCDM (flat LCDM).
    """
    def ode(x, state):
        a = np.exp(x)
        E2 = Omega_m_LCDM / a**3 + Omega_Lambda
        dlnH = -1.5 * Omega_m_LCDM / (a**3 * E2)
        return [state[1],
                -(3 + dlnH) * state[1]
                + 1.5 * Omega_source / (a**3 * E2) * state[0]]

    sol = solve_ivp(ode, [np.log(a_start), np.log(a_end)],
                    [a_start, 1.0], method='RK45', rtol=1e-10, atol=1e-14,
                    max_step=0.005,
                    t_eval=np.linspace(np.log(a_start), np.log(a_end), 3000))
    return sol.y[0][-1]


def compute_growth_DFD(Omega_chi):
    """
    DFD growth factor for given Omega_chi.

    Post-recombination: chi gravitates normally, baryons get MOND enhancement.
    Omega_eff = Omega_chi + Omega_b * nu_MOND

    MOND provides whatever enhancement is needed to match the LCDM growth:
    nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b

    This is the "Model A" from the R2 campaign: MOND acts as an effective
    constant gravitational enhancement on baryons.

    The key constraint is: nu_MOND must be physically achievable.
    - nu = 1: Newtonian (no MOND)
    - nu ~ 6.4: needed for pure baryon (Omega_chi = 0) to match LCDM growth
    - nu ~ 1 + epsilon: chi does nearly all the work

    For any Omega_chi, the effective matter density is:
    Omega_eff = Omega_chi + Omega_b * nu_MOND = Omega_m_LCDM
    => Growth matches LCDM by construction.

    So growth is NOT the constraint -- the transfer function shape is!
    """
    nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b
    Omega_eff = Omega_chi + Omega_b * nu_MOND  # = Omega_m_LCDM

    D = solve_growth(Omega_eff)
    D_LCDM = solve_growth(Omega_m_LCDM)

    return D / D_LCDM, nu_MOND, Omega_eff


# =============================================================================
# POWER SPECTRUM AND OBSERVABLES
# =============================================================================
def compute_Pk(k_hMpc, T_k, D_ratio=1.0):
    """P(k) = A_s * (k/k_pivot)^(n_s-1) * T(k)^2 * D_ratio^2 * k_h"""
    k_pivot = 0.05  # Mpc^-1
    k_Mpc = k_hMpc * h
    return A_s * (k_Mpc / k_pivot)**(n_s - 1) * T_k**2 * k_hMpc * D_ratio**2


def compute_sigma8(k_hMpc, Pk):
    """sigma8 from P(k)."""
    R = 8.0
    kR = k_hMpc * R
    W = np.where(kR < 1e-6, 1.0, 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3)
    integrand = k_hMpc**2 * Pk * W**2 / (2 * np.pi**2)
    lnk = np.log(k_hMpc)
    sigma8_sq = trapezoid(integrand * k_hMpc, lnk)
    return np.sqrt(abs(sigma8_sq))


# =============================================================================
# MAIN SCAN
# =============================================================================
def run_scan():
    print("=" * 80)
    print("R9 AGENT 19: MINIMUM Omega_chi FOR P(k) SHAPE COMPATIBILITY")
    print("=" * 80)
    print()
    print("KEY INSIGHT: MOND fixes the growth factor (sigma8) for ANY Omega_chi.")
    print("The BINDING CONSTRAINT is the transfer function shape,")
    print("which depends on pre-recombination pressureless matter = Omega_b + Omega_chi.")
    print()

    # LCDM reference
    T_LCDM, s_LCDM = EH_transfer(k_grid, Omega_CDM_LCDM)
    Pk_LCDM_raw = compute_Pk(k_grid, T_LCDM, 1.0)
    sigma8_raw = compute_sigma8(k_grid, Pk_LCDM_raw)
    A_norm = (SIGMA8_TARGET / sigma8_raw)**2
    Pk_LCDM = Pk_LCDM_raw * A_norm
    sigma8_LCDM = compute_sigma8(k_grid, Pk_LCDM)

    print(f"LCDM reference: sigma_8 = {sigma8_LCDM:.4f}")
    print(f"Sound horizon s_LCDM = {s_LCDM:.2f} Mpc/h")
    print()

    # Scan
    Omega_chi_values = np.arange(0.00, 0.305, 0.01)
    results = []

    print(f"{'Oc':>6} {'Om':>6} {'nu_M':>6} {'sig8':>7} "
          f"{'r02':>7} {'r05':>7} {'r10':>7} {'r15':>7} "
          f"{'maxdev':>7} {'s/s_L':>6} {'sig':>4} {'shp':>4} {'bao':>4} {'ALL':>4}")
    print("-" * 100)

    for Omega_chi in Omega_chi_values:
        # Transfer function
        T_DFD, s_DFD = get_transfer(k_grid, Omega_chi)

        # Growth: MOND ensures D/D_LCDM = 1 by construction
        D_ratio, nu_MOND, Omega_eff = compute_growth_DFD(Omega_chi)

        # P(k)
        Pk_DFD = compute_Pk(k_grid, T_DFD, D_ratio) * A_norm
        sigma8 = compute_sigma8(k_grid, Pk_DFD)

        # Shape ratios at diagnostic k
        ratios = []
        for kd in k_diag:
            idx = np.argmin(np.abs(k_grid - kd))
            r = Pk_DFD[idx] / Pk_LCDM[idx] if Pk_LCDM[idx] > 0 else np.nan
            ratios.append(r)

        # Max shape deviation in 0.01 < k < 0.15 h/Mpc
        mask = (k_grid > 0.01) & (k_grid < 0.15)
        ratio_arr = Pk_DFD[mask] / np.maximum(Pk_LCDM[mask], 1e-300)
        max_dev = np.max(np.abs(ratio_arr - 1.0))

        # Sound horizon shift (proxy for BAO)
        s_ratio = s_DFD / s_LCDM

        # Pass/fail
        pass_sig = abs(sigma8 - SIGMA8_TARGET) < SIGMA8_TOL
        pass_shape = max_dev < SHAPE_TOL
        pass_bao = abs(s_ratio - 1.0) < BAO_TOL

        all_pass = pass_sig and pass_shape and pass_bao

        results.append(dict(
            Omega_chi=Omega_chi, Omega_m=Omega_b + Omega_chi,
            nu_MOND=nu_MOND, sigma8=sigma8, D_ratio=D_ratio,
            ratios=ratios, max_dev=max_dev, s_DFD=s_DFD, s_ratio=s_ratio,
            pass_sig=pass_sig, pass_shape=pass_shape, pass_bao=pass_bao,
            all_pass=all_pass))

        sig_s = "Y" if pass_sig else "-"
        shp_s = "Y" if pass_shape else "-"
        bao_s = "Y" if pass_bao else "-"
        all_s = "YES" if all_pass else "---"

        print(f"{Omega_chi:6.3f} {Omega_b+Omega_chi:6.4f} {nu_MOND:6.2f} "
              f"{sigma8:7.4f} "
              f"{ratios[0]:7.4f} {ratios[1]:7.4f} {ratios[2]:7.4f} {ratios[3]:7.4f} "
              f"{max_dev:7.4f} {s_ratio:6.4f} "
              f"{sig_s:>4} {shp_s:>4} {bao_s:>4} {all_s:>4}")

    return results, Pk_LCDM, s_LCDM


# =============================================================================
# ANALYSIS
# =============================================================================
def analyze(results, s_LCDM):
    print()
    print("=" * 80)
    print("DETAILED ANALYSIS")
    print("=" * 80)

    # Find minimum passing
    passing = [r for r in results if r['all_pass']]

    if passing:
        best = min(passing, key=lambda x: x['Omega_chi'])
        print(f"\nMINIMUM Omega_chi (all criteria): {best['Omega_chi']:.3f}")
        print(f"  = {best['Omega_chi']/Omega_CDM_LCDM*100:.1f}% of LCDM CDM")
        print(f"  nu_MOND needed: {best['nu_MOND']:.2f}")
        print(f"  sigma8: {best['sigma8']:.4f}")
        print(f"  max shape deviation: {best['max_dev']:.4f} ({best['max_dev']*100:.1f}%)")
        print(f"  BAO shift: {abs(best['s_ratio']-1)*100:.2f}%")
    else:
        print("\nNO Omega_chi passes ALL criteria!")

    # Individual criterion analysis
    print("\n--- Individual criteria ---")

    # sigma8
    sig_pass = [r for r in results if r['pass_sig']]
    if sig_pass:
        best_sig = min(sig_pass, key=lambda x: x['Omega_chi'])
        print(f"sigma8 first satisfied at Omega_chi = {best_sig['Omega_chi']:.3f} "
              f"(sigma8 = {best_sig['sigma8']:.4f})")
    else:
        closest = min(results, key=lambda x: abs(x['sigma8'] - SIGMA8_TARGET))
        print(f"sigma8 NEVER satisfied. Closest: {closest['sigma8']:.4f} "
              f"at Omega_chi = {closest['Omega_chi']:.3f}")

    # Shape
    shp_pass = [r for r in results if r['pass_shape']]
    if shp_pass:
        best_shp = min(shp_pass, key=lambda x: x['Omega_chi'])
        print(f"Shape (<30%) first satisfied at Omega_chi = {best_shp['Omega_chi']:.3f} "
              f"(max_dev = {best_shp['max_dev']:.4f})")
    else:
        closest = min(results, key=lambda x: x['max_dev'])
        print(f"Shape NEVER satisfied. Best: max_dev = {closest['max_dev']:.4f} "
              f"at Omega_chi = {closest['Omega_chi']:.3f}")

    # BAO
    bao_pass = [r for r in results if r['pass_bao']]
    if bao_pass:
        best_bao = min(bao_pass, key=lambda x: x['Omega_chi'])
        print(f"BAO (<1%) first satisfied at Omega_chi = {best_bao['Omega_chi']:.3f} "
              f"(shift = {abs(best_bao['s_ratio']-1)*100:.2f}%)")
    else:
        closest = min(results, key=lambda x: abs(x['s_ratio'] - 1.0))
        print(f"BAO NEVER satisfied. Best: shift = {abs(closest['s_ratio']-1)*100:.2f}% "
              f"at Omega_chi = {closest['Omega_chi']:.3f}")

    # Relaxed criteria analysis
    print()
    print("--- Relaxed criteria analysis ---")
    for tol_label, shape_tol in [("10%", 0.10), ("20%", 0.20), ("30%", 0.30),
                                  ("50%", 0.50), ("100%", 1.00)]:
        ok = [r for r in results if r['max_dev'] < shape_tol]
        if ok:
            best_r = min(ok, key=lambda x: x['Omega_chi'])
            print(f"  Shape < {tol_label}: min Omega_chi = {best_r['Omega_chi']:.3f} "
                  f"({best_r['Omega_chi']/Omega_CDM_LCDM*100:.1f}% of CDM)")
        else:
            print(f"  Shape < {tol_label}: never satisfied")

    # Transfer function is the binding constraint
    print()
    print("=" * 80)
    print("PHYSICAL INTERPRETATION")
    print("=" * 80)
    print()
    print("The transfer function T(k) depends on omega_m = (Omega_b + Omega_chi) h^2.")
    print("MOND only affects POST-recombination growth, not pre-recombination physics.")
    print("Therefore, the transfer function shape is the BINDING CONSTRAINT.")
    print()
    print("The EH shape parameter Gamma = Omega_m h controls the turnover scale.")
    print(f"  LCDM:    Gamma = {Omega_m_LCDM * h:.4f}")
    for Oc in [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.266]:
        Om = Omega_b + Oc
        gamma = Om * h
        print(f"  Oc={Oc:.3f}: Gamma = {gamma:.4f} "
              f"({gamma/(Omega_m_LCDM*h)*100:.1f}% of LCDM)")

    print()
    print("The turnover scale k_eq ~ Omega_m h^2 / T_CMB^2:")
    for Oc in [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.266]:
        Om = Omega_b + Oc
        omega_m = Om * h**2
        theta = T_CMB / 2.7
        k_eq = 7.46e-2 * omega_m * theta**(-2)
        k_eq_LCDM = 7.46e-2 * Omega_m_LCDM * h**2 * theta**(-2)
        print(f"  Oc={Oc:.3f}: k_eq = {k_eq:.4f} h/Mpc "
              f"({k_eq/k_eq_LCDM*100:.1f}% of LCDM)")

    # Physical implications
    print()
    print("=" * 80)
    print("CHI PRODUCTION IMPLICATIONS")
    print("=" * 80)
    print()

    # Find the binding constraint minimum
    if passing:
        min_Oc = min(passing, key=lambda x: x['Omega_chi'])['Omega_chi']
    elif shp_pass:
        min_Oc = min(shp_pass, key=lambda x: x['Omega_chi'])['Omega_chi']
    else:
        # Extrapolate: what shape tolerance would we need?
        print("Even at 30% tolerance, no Omega_chi works.")
        print("Checking what tolerance IS achievable at each Omega_chi:")
        for r in results:
            if r['Omega_chi'] in [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.266]:
                print(f"  Omega_chi = {r['Omega_chi']:.3f}: "
                      f"max deviation = {r['max_dev']*100:.1f}%, "
                      f"sigma8 = {r['sigma8']:.4f}")
        min_Oc = 0.266

    frac = min_Oc / Omega_CDM_LCDM * 100
    nu_need = (Omega_m_LCDM - min_Oc) / Omega_b

    print(f"\nMinimum Omega_chi ~ {min_Oc:.3f} ({frac:.1f}% of LCDM CDM)")
    print(f"Required nu_MOND = {nu_need:.2f}")
    print(f"rho_chi = {min_Oc * rho_crit_0:.3e} kg/m^3")
    print()

    if min_Oc < 0.05:
        verdict = "MINOR component. MOND does most work. EASY production."
    elif min_Oc < 0.15:
        verdict = "MODERATE component. Both chi and MOND contribute. INTERMEDIATE production."
    elif min_Oc < 0.22:
        verdict = "MAJORITY component. Chi dominates. SUBSTANTIAL production needed."
    else:
        verdict = "NEARLY ALL CDM must be chi. MOND alone insufficient for shape."

    print(f"VERDICT: {verdict}")

    return passing


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print()
    results, Pk_LCDM, s_LCDM = run_scan()
    passing = analyze(results, s_LCDM)

    print()
    print("=" * 80)
    print("R9 AGENT 19 COMPLETE")
    print("=" * 80)
