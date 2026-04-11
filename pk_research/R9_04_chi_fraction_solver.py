#!/usr/bin/env python3
"""
R9 Agent 4: Chi Fraction Solver
================================
What if chi provides only a FRACTION of Omega_CDM, with MOND phantom DM
providing the rest through post-recombination nonlinear growth?

Scenario: Omega_chi + MOND phantom = Omega_CDM_total = 0.266
- chi provides pre-recombination potential wells (fixes transfer function shape)
- MOND provides post-recombination enhanced growth (fixes sigma_8 amplitude)

We compute P(k) for Omega_chi = {0.05, 0.10, 0.15, 0.20, 0.266}
using Eisenstein-Hu transfer with mixed (chi + baryon) content,
plus MOND-enhanced post-recombination growth.

Author: R9 Agent 4 (Claude)
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
Omega_b = Omega_b_h2 / h**2
Omega_CDM_LCDM = 0.266       # CDM density in LCDM
Omega_m_LCDM = 0.315         # Total matter in LCDM
Omega_Lambda = 0.685

T_CMB = 2.725
n_s = 0.965
A_s = 2.1e-9

a0_MOND = 1.2e-10
G_N = 6.674e-11
Mpc_m = 3.0856775814913673e22

rho_crit_0 = 3 * H0_si**2 / (8 * np.pi * G_N)

# Target values from LCDM/Planck
SIGMA8_TARGET = 0.811
K_BAO_TARGET = 0.0628  # h/Mpc -- BAO scale ~ 100 h^-1 Mpc

# =============================================================================
# SCENARIOS: different chi fractions
# =============================================================================
OMEGA_CHI_VALUES = [0.05, 0.10, 0.15, 0.20, 0.266]

# =============================================================================
# EXPANSION HISTORY
# =============================================================================
def E_sq(a, Omega_m=Omega_m_LCDM):
    """H^2(a)/H0^2 -- we keep total Omega_m = 0.315 for expansion"""
    return Omega_m / a**3 + Omega_Lambda

def dlnH_dlna(a, Omega_m=Omega_m_LCDM):
    return -1.5 * Omega_m / (a**3 * E_sq(a, Omega_m))

# =============================================================================
# EISENSTEIN-HU TRANSFER FUNCTION (with variable chi content)
# =============================================================================
def EH_transfer_mixed(k_hMpc, Omega_chi):
    """
    EH98 transfer function for a universe with baryons + chi.

    chi acts like CDM for transfer function purposes (pressureless,
    gravitationally coupled pre-recombination).

    omega_m = (Omega_b + Omega_chi) * h^2
    omega_b = Omega_b * h^2
    f_b = omega_b / omega_m  (baryon fraction of gravitating matter)
    f_c = omega_chi / omega_m (chi fraction -- acts like CDM)
    """
    omega_chi = Omega_chi * h**2
    omega_b = Omega_b_h2
    omega_m = omega_b + omega_chi

    # For expansion, we still use total Omega_m = 0.315
    # But for the transfer function, the relevant matter is what couples
    # pre-recombination: baryons + chi

    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    f_b = omega_b / omega_m
    f_c = 1 - f_b  # chi fraction

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * omega_m**(-0.419) * (1 + 0.607 * omega_m**0.674)
    b2 = 0.238 * omega_m**0.223
    z_d = 1291 * omega_m**0.251 / (1 + 0.659 * omega_m**0.828) * (1 + b1 * omega_b**b2)

    R_eq = 31.5e3 * omega_b * theta**(-4) / z_eq
    R_d = 31.5e3 * omega_b * theta**(-4) / z_d

    s = (2.0/(3*k_eq)) * np.sqrt(6/R_eq) * np.log(
        (np.sqrt(1+R_d) + np.sqrt(R_d+R_eq)) / (1 + np.sqrt(R_eq)))

    # No-wiggle transfer function (EH98 Eq 29-31)
    alpha_gamma = 1 - 0.328*np.log(431*omega_m)*f_b + 0.38*np.log(22.3*omega_m)*f_b**2
    gamma_eff = omega_m/h * (alpha_gamma + (1-alpha_gamma)/(1+(0.43*k*s)**4))
    q = k * theta**2 / gamma_eff
    L = np.log(2*np.e + 1.8*q)
    C = 14.2 + 731/(1+62.5*q)
    T = L / (L + C*q**2)

    return T, s, z_eq, k_eq


def EH_transfer_LCDM(k_hMpc):
    """Standard LCDM transfer function for comparison."""
    return EH_transfer_mixed(k_hMpc, Omega_CDM_LCDM)


def EH_transfer_baryon_only(k_hMpc):
    """Pure baryon transfer function (Omega_chi = 0)."""
    omega_m = Omega_b_h2
    omega_b = Omega_b_h2
    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * max(omega_m, 1e-10)**(-0.419) * (1 + 0.607 * max(omega_m, 1e-10)**0.674)
    b2 = 0.238 * max(omega_m, 1e-10)**0.223
    z_d = 1291 * max(omega_m, 1e-10)**0.251 / (1 + 0.659 * max(omega_m, 1e-10)**0.828) * (1 + b1 * omega_b**b2)

    R_eq = 31.5e3 * omega_b * theta**(-4) / max(z_eq, 1)
    R_d = 31.5e3 * omega_b * theta**(-4) / max(z_d, 1)

    s = (2.0/(3*k_eq)) * np.sqrt(6/max(R_eq, 1e-10)) * np.log(
        (np.sqrt(1+R_d) + np.sqrt(R_d+R_eq)) / (1 + np.sqrt(max(R_eq, 1e-10))))

    gamma_eff = omega_m / h
    q = k * theta**2 / gamma_eff
    L = np.log(2*np.e + 1.8*q)
    C = 14.2 + 731/(1+62.5*q)
    T = L / (L + C*q**2)

    # Silk damping
    k_silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1 + (10.4*omega_m)**(-0.95))
    silk = np.exp(-(k/k_silk)**1.4)

    ks = k * s
    j0 = np.where(np.abs(ks) < 1e-10, 1.0, np.sin(ks)/ks)
    T_bary = T * (silk * j0 + (1 - silk) * 0.05)

    return T_bary, s


# =============================================================================
# GROWTH FACTOR SOLVERS
# =============================================================================
def solve_growth_linear(Omega_source, a_start=1e-4, a_end=1.0):
    """Standard linear growth with constant Omega_source."""
    def ode(x, state):
        a = np.exp(x)
        E2 = Omega_m_LCDM/a**3 + Omega_Lambda
        dlnH = -1.5*Omega_m_LCDM/(a**3*E2)
        return [state[1], -(3+dlnH)*state[1] + 1.5*Omega_source/(a**3*E2)*state[0]]

    sol = solve_ivp(ode, [np.log(a_start), np.log(a_end)],
                    [a_start, 1.0], method='RK45', rtol=1e-10, atol=1e-14,
                    max_step=0.005, t_eval=np.linspace(np.log(a_start), np.log(a_end), 3000))
    return np.exp(sol.t), sol.y[0]


def solve_growth_chi_plus_MOND(Omega_chi, nu_MOND, a_start=1e-4, a_end=1.0):
    """
    Growth with chi (linear, like CDM) + MOND enhancement on baryons.

    The source term has two contributions:
    1. chi: gravitates normally, Omega_chi contribution
    2. baryons: enhanced by MOND factor nu_MOND

    Total effective: Omega_chi + Omega_b * nu_MOND

    For self-consistency: we need Omega_chi + Omega_b * nu_MOND ~ Omega_m_LCDM
    => nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b

    But nu_MOND is scale-dependent in full MOND. We parameterize:
    nu_MOND(k) = nu_base * (1 + (k/k_MOND)^alpha)^(-beta)
    where nu_base = (Omega_m - Omega_chi) / Omega_b
    """
    Omega_eff = Omega_chi + Omega_b * nu_MOND
    return solve_growth_linear(Omega_eff, a_start, a_end)


def solve_growth_MOND_scale_dep(Omega_chi, k_hMpc, a_start=1e-4, a_end=1.0):
    """
    Scale-dependent MOND growth.

    At large scales (k << k_MOND): MOND is strong, nu ~ (Omega_m - Omega_chi)/Omega_b
    At small scales (k >> k_MOND): MOND weakens (EFE from larger structures)

    This gives a SCALE-DEPENDENT growth that modifies the transfer function shape.

    k_MOND ~ a0 / (H0 * c) ~ characteristic MOND scale
    In practice, k_MOND ~ 0.01-0.1 h/Mpc (cluster scales where MOND effects kick in)
    """
    # MOND transition scale -- where a_MOND = a0
    # g = H0^2 * a0_MOND / (k * H0) ... this is approximate
    # We set k_MOND based on where MOND effects become order unity
    k_MOND = 0.05  # h/Mpc -- transition scale

    # nu needed to fill the gap
    nu_needed_local = (Omega_m_LCDM - Omega_chi) / Omega_b

    # Scale-dependent suppression: MOND is less effective at small scales
    # due to external field effect from larger structures
    scale_factor = 1.0 / (1.0 + (k_hMpc / k_MOND)**1.5)

    nu_eff = 1.0 + (nu_needed_local - 1.0) * scale_factor

    Omega_eff = Omega_chi + Omega_b * nu_eff
    return solve_growth_linear(Omega_eff, a_start, a_end), nu_eff


# =============================================================================
# POWER SPECTRUM COMPUTATION
# =============================================================================
def compute_Pk(k_hMpc, T_k, D_ratio=1.0):
    """
    P(k) = A_s * (k/k_pivot)^(n_s-1) * T(k)^2 * D_ratio^2 * (k * h)

    Normalized to match LCDM sigma_8 when T = T_LCDM and D_ratio = 1.
    """
    k_pivot = 0.05  # Mpc^-1
    k_Mpc = k_hMpc * h
    Pk = A_s * (k_Mpc / k_pivot)**(n_s - 1) * T_k**2 * k_hMpc * D_ratio**2
    return Pk


def compute_sigma8(k_hMpc, Pk):
    """
    sigma_8 = sqrt( integral of k^2 P(k) W(kR)^2 / (2 pi^2) dk )
    with R = 8 h^-1 Mpc, W = top-hat window.
    """
    R = 8.0  # h^-1 Mpc
    kR = k_hMpc * R
    W = np.where(kR < 1e-6, 1.0, 3*(np.sin(kR) - kR*np.cos(kR))/kR**3)

    integrand = k_hMpc**2 * Pk * W**2 / (2 * np.pi**2)

    # Use log-spaced integration
    lnk = np.log(k_hMpc)
    integrand_lnk = integrand * k_hMpc  # dk = k dlnk

    sigma8_sq = trapezoid(integrand_lnk, lnk)
    return np.sqrt(abs(sigma8_sq))


def find_BAO_peak(k_hMpc, ratio):
    """Find the k position of first BAO wiggle (peak in P/P_smooth)."""
    # Look for first peak in the ratio between k=0.03 and k=0.15
    mask = (k_hMpc > 0.03) & (k_hMpc < 0.20)
    k_sub = k_hMpc[mask]
    r_sub = ratio[mask]

    if len(r_sub) < 10:
        return np.nan

    # Find peaks (local maxima)
    peaks = []
    for i in range(1, len(r_sub)-1):
        if r_sub[i] > r_sub[i-1] and r_sub[i] > r_sub[i+1]:
            peaks.append(i)

    if peaks:
        return k_sub[peaks[0]]
    return np.nan


# =============================================================================
# MAIN COMPUTATION
# =============================================================================
def run_all_scenarios():
    """Compute P(k) for all chi fraction scenarios."""

    k = np.logspace(-3, 0.5, 2000)  # k in h/Mpc

    # Reference: LCDM
    T_LCDM, s_LCDM, _, _ = EH_transfer_LCDM(k)
    _, D_LCDM = solve_growth_linear(Omega_m_LCDM)
    D_LCDM_0 = D_LCDM[-1]

    Pk_LCDM = compute_Pk(k, T_LCDM, 1.0)

    # Normalize: find the constant that gives sigma_8 = 0.811
    sigma8_raw = compute_sigma8(k, Pk_LCDM)
    norm = (SIGMA8_TARGET / sigma8_raw)**2
    Pk_LCDM *= norm
    sigma8_LCDM = compute_sigma8(k, Pk_LCDM)

    print("=" * 80)
    print("R9 AGENT 4: CHI FRACTION ANALYSIS")
    print("=" * 80)
    print(f"\nReference LCDM: sigma_8 = {sigma8_LCDM:.4f}, s_BAO = {s_LCDM:.2f} Mpc/h")
    print(f"LCDM growth D(a=1) = {D_LCDM_0:.6f}")
    print()

    # Also compute pure baryon reference
    T_bary, s_bary = EH_transfer_baryon_only(k)
    _, D_bary = solve_growth_linear(Omega_b)
    D_bary_ratio = D_bary[-1] / D_LCDM_0
    Pk_bary = compute_Pk(k, T_bary, D_bary_ratio) * norm
    sigma8_bary = compute_sigma8(k, Pk_bary)

    print(f"Pure baryon (no chi, no MOND): sigma_8 = {sigma8_bary:.4f}")
    print(f"  D_bary/D_LCDM = {D_bary_ratio:.4f}")
    print()

    results = {}

    # =========================================================================
    # SCENARIO SET 1: Chi + constant MOND enhancement (no scale dependence)
    # =========================================================================
    print("=" * 80)
    print("SCENARIO SET 1: Chi provides transfer function + MOND provides constant growth")
    print("  T(k) from EH with Omega_chi, Growth from Omega_chi + Omega_b * nu_MOND")
    print("  nu_MOND chosen so total Omega_eff = Omega_m_LCDM")
    print("=" * 80)

    for Omega_chi in OMEGA_CHI_VALUES:
        nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b
        Omega_eff = Omega_chi + Omega_b * nu_MOND  # = Omega_m_LCDM by construction

        T_chi, s_chi, z_eq_chi, k_eq_chi = EH_transfer_mixed(k, Omega_chi)

        # Growth: use effective Omega_m = Omega_chi + Omega_b * nu_MOND = 0.315
        _, D_chi = solve_growth_linear(Omega_eff)
        D_ratio = D_chi[-1] / D_LCDM_0

        Pk_chi = compute_Pk(k, T_chi, D_ratio) * norm
        sigma8_chi = compute_sigma8(k, Pk_chi)

        ratio = Pk_chi / Pk_LCDM
        ratio_safe = np.where(Pk_LCDM > 0, ratio, 0)

        # BAO position
        k_BAO = find_BAO_peak(k, ratio_safe)

        # Compute shape metric: mean |log(P_chi/P_LCDM)| for k in [0.01, 0.3]
        mask_shape = (k > 0.01) & (k < 0.3)
        shape_dev = np.mean(np.abs(np.log10(np.clip(ratio_safe[mask_shape], 1e-10, 1e10))))

        # Power at key scales
        idx_01 = np.argmin(np.abs(k - 0.1))
        idx_001 = np.argmin(np.abs(k - 0.01))

        results[f'S1_chi{Omega_chi:.2f}'] = {
            'Omega_chi': Omega_chi,
            'nu_MOND': nu_MOND,
            'sigma8': sigma8_chi,
            'D_ratio': D_ratio,
            's_BAO': s_chi,
            'shape_dev': shape_dev,
            'P_ratio_k01': ratio_safe[idx_01],
            'P_ratio_k001': ratio_safe[idx_001],
        }

        f_chi = Omega_chi / Omega_CDM_LCDM
        print(f"\nOmega_chi = {Omega_chi:.3f} (f_chi = {f_chi:.2f} of CDM)")
        print(f"  nu_MOND = {nu_MOND:.3f}, Omega_eff = {Omega_eff:.4f}")
        print(f"  sigma_8 = {sigma8_chi:.4f} (target: {SIGMA8_TARGET:.3f})")
        print(f"  sigma_8 / target = {sigma8_chi/SIGMA8_TARGET:.4f}")
        print(f"  D/D_LCDM = {D_ratio:.4f}")
        print(f"  s_BAO = {s_chi:.2f} Mpc/h (LCDM: {s_LCDM:.2f})")
        print(f"  <|log10(P/P_LCDM)|> [0.01-0.3] = {shape_dev:.4f}")
        print(f"  P/P_LCDM at k=0.01 = {ratio_safe[idx_001]:.4f}")
        print(f"  P/P_LCDM at k=0.1  = {ratio_safe[idx_01]:.4f}")

    # =========================================================================
    # SCENARIO SET 2: Chi + scale-dependent MOND
    # =========================================================================
    print("\n" + "=" * 80)
    print("SCENARIO SET 2: Chi transfer + SCALE-DEPENDENT MOND growth")
    print("  MOND enhancement is strong at large scales, weak at small scales")
    print("  nu(k) = 1 + (nu_max - 1) / (1 + (k/k_MOND)^1.5)")
    print("  k_MOND = 0.05 h/Mpc")
    print("=" * 80)

    k_MOND = 0.05  # h/Mpc

    # Pre-compute growth factors on a coarse Omega_eff grid, then interpolate
    Omega_eff_grid = np.linspace(Omega_b * 0.9, Omega_m_LCDM * 1.1, 80)
    D_grid = np.zeros(len(Omega_eff_grid))
    for ig, Oeff in enumerate(Omega_eff_grid):
        _, D_tmp = solve_growth_linear(Oeff)
        D_grid[ig] = D_tmp[-1] / D_LCDM_0
    D_interp = interp1d(Omega_eff_grid, D_grid, kind='cubic', fill_value='extrapolate')

    for Omega_chi in OMEGA_CHI_VALUES:
        nu_max = (Omega_m_LCDM - Omega_chi) / Omega_b

        T_chi, s_chi, _, _ = EH_transfer_mixed(k, Omega_chi)

        # Scale-dependent growth via interpolation
        scale_factor = 1.0 / (1.0 + (k / k_MOND)**1.5)
        nu_eff_arr = 1.0 + (nu_max - 1.0) * scale_factor
        Omega_eff_k = Omega_chi + Omega_b * nu_eff_arr
        D_ratios = D_interp(Omega_eff_k)

        Pk_chi = compute_Pk(k, T_chi, D_ratios) * norm
        sigma8_chi = compute_sigma8(k, Pk_chi)

        ratio = Pk_chi / Pk_LCDM
        ratio_safe = np.where(Pk_LCDM > 0, ratio, 0)

        mask_shape = (k > 0.01) & (k < 0.3)
        shape_dev = np.mean(np.abs(np.log10(np.clip(ratio_safe[mask_shape], 1e-10, 1e10))))

        idx_01 = np.argmin(np.abs(k - 0.1))
        idx_001 = np.argmin(np.abs(k - 0.01))

        results[f'S2_chi{Omega_chi:.2f}'] = {
            'Omega_chi': Omega_chi,
            'nu_MOND_max': nu_max,
            'sigma8': sigma8_chi,
            's_BAO': s_chi,
            'shape_dev': shape_dev,
            'P_ratio_k01': ratio_safe[idx_01],
            'P_ratio_k001': ratio_safe[idx_001],
            'nu_eff_k01': nu_eff_arr[idx_01],
            'nu_eff_k001': nu_eff_arr[idx_001],
        }

        f_chi = Omega_chi / Omega_CDM_LCDM
        print(f"\nOmega_chi = {Omega_chi:.3f} (f_chi = {f_chi:.2f})")
        print(f"  nu_MOND(k=0.01) = {nu_eff_arr[idx_001]:.3f}, nu_MOND(k=0.1) = {nu_eff_arr[idx_01]:.3f}")
        print(f"  sigma_8 = {sigma8_chi:.4f} (target: {SIGMA8_TARGET:.3f})")
        print(f"  sigma_8 / target = {sigma8_chi/SIGMA8_TARGET:.4f}")
        print(f"  <|log10(P/P_LCDM)|> = {shape_dev:.4f}")
        print(f"  P/P_LCDM at k=0.01 = {ratio_safe[idx_001]:.4f}")
        print(f"  P/P_LCDM at k=0.1  = {ratio_safe[idx_01]:.4f}")

    # =========================================================================
    # SCENARIO SET 3: Optimal search -- minimize chi needed
    # =========================================================================
    print("\n" + "=" * 80)
    print("SCENARIO SET 3: MINIMUM CHI SEARCH")
    print("  Find minimum Omega_chi that achieves:")
    print("  (a) sigma_8 within 5% of target")
    print("  (b) shape deviation < 0.1 dex across 0.01-0.3 h/Mpc")
    print("=" * 80)

    # Fine grid search
    chi_grid = np.linspace(0.01, 0.266, 50)
    sigma8_grid_S1 = np.zeros(len(chi_grid))
    shape_grid_S1 = np.zeros(len(chi_grid))
    sigma8_grid_S2 = np.zeros(len(chi_grid))
    shape_grid_S2 = np.zeros(len(chi_grid))

    for j, Omega_chi in enumerate(chi_grid):
        T_chi, _, _, _ = EH_transfer_mixed(k, Omega_chi)

        # S1: constant MOND
        nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b
        Omega_eff = Omega_chi + Omega_b * nu_MOND
        _, D_chi = solve_growth_linear(Omega_eff)
        D_ratio = D_chi[-1] / D_LCDM_0
        Pk_chi = compute_Pk(k, T_chi, D_ratio) * norm
        sigma8_grid_S1[j] = compute_sigma8(k, Pk_chi)
        ratio = Pk_chi / Pk_LCDM
        mask_shape = (k > 0.01) & (k < 0.3)
        shape_grid_S1[j] = np.mean(np.abs(np.log10(np.clip(ratio[mask_shape], 1e-10, 1e10))))

        # S2: scale-dependent MOND (using pre-computed interpolator)
        nu_max = (Omega_m_LCDM - Omega_chi) / Omega_b
        sf = 1.0 / (1.0 + (k / k_MOND)**1.5)
        nu_eff_scan = 1.0 + (nu_max - 1.0) * sf
        Oeff_scan = Omega_chi + Omega_b * nu_eff_scan
        D_ratios = D_interp(Oeff_scan)
        Pk_chi2 = compute_Pk(k, T_chi, D_ratios) * norm
        sigma8_grid_S2[j] = compute_sigma8(k, Pk_chi2)
        ratio2 = Pk_chi2 / Pk_LCDM
        shape_grid_S2[j] = np.mean(np.abs(np.log10(np.clip(ratio2[mask_shape], 1e-10, 1e10))))

    # Find thresholds
    sigma8_ok_S1 = np.abs(sigma8_grid_S1 / SIGMA8_TARGET - 1) < 0.05
    shape_ok_S1 = shape_grid_S1 < 0.1
    both_ok_S1 = sigma8_ok_S1 & shape_ok_S1

    sigma8_ok_S2 = np.abs(sigma8_grid_S2 / SIGMA8_TARGET - 1) < 0.05
    shape_ok_S2 = shape_grid_S2 < 0.1
    both_ok_S2 = sigma8_ok_S2 & shape_ok_S2

    print("\nScenario 1 (constant MOND growth):")
    if np.any(sigma8_ok_S1):
        idx_min_s8 = np.where(sigma8_ok_S1)[0][0]
        print(f"  Min Omega_chi for sigma_8 within 5%: {chi_grid[idx_min_s8]:.4f}")
    else:
        print(f"  sigma_8 range: [{sigma8_grid_S1.min():.4f}, {sigma8_grid_S1.max():.4f}]")

    if np.any(shape_ok_S1):
        idx_min_shape = np.where(shape_ok_S1)[0][0]
        print(f"  Min Omega_chi for shape < 0.1 dex: {chi_grid[idx_min_shape]:.4f}")
    else:
        print(f"  Shape deviation range: [{shape_grid_S1.min():.4f}, {shape_grid_S1.max():.4f}]")

    if np.any(both_ok_S1):
        idx_both = np.where(both_ok_S1)[0][0]
        print(f"  Min Omega_chi for BOTH criteria: {chi_grid[idx_both]:.4f}")
        print(f"    => f_chi = {chi_grid[idx_both]/Omega_CDM_LCDM:.3f} of CDM")
    else:
        print(f"  No Omega_chi satisfies both criteria simultaneously")

    print("\nScenario 2 (scale-dependent MOND growth):")
    if np.any(sigma8_ok_S2):
        idx_min_s8 = np.where(sigma8_ok_S2)[0][0]
        print(f"  Min Omega_chi for sigma_8 within 5%: {chi_grid[idx_min_s8]:.4f}")
    else:
        print(f"  sigma_8 range: [{sigma8_grid_S2.min():.4f}, {sigma8_grid_S2.max():.4f}]")

    if np.any(shape_ok_S2):
        idx_min_shape = np.where(shape_ok_S2)[0][0]
        print(f"  Min Omega_chi for shape < 0.1 dex: {chi_grid[idx_min_shape]:.4f}")
    else:
        print(f"  Shape deviation range: [{shape_grid_S2.min():.4f}, {shape_grid_S2.max():.4f}]")

    if np.any(both_ok_S2):
        idx_both = np.where(both_ok_S2)[0][0]
        print(f"  Min Omega_chi for BOTH criteria: {chi_grid[idx_both]:.4f}")
        print(f"    => f_chi = {chi_grid[idx_both]/Omega_CDM_LCDM:.3f} of CDM")
    else:
        print(f"  No Omega_chi satisfies both criteria simultaneously")

    # =========================================================================
    # DETAILED DIAGNOSTICS
    # =========================================================================
    print("\n" + "=" * 80)
    print("DETAILED DIAGNOSTICS: P(k)/P_LCDM at key scales")
    print("=" * 80)

    k_diag = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]

    print(f"\n{'Omega_chi':>10} | " + " | ".join([f"k={ki:.3f}" for ki in k_diag]))
    print("-" * (12 + 10 * len(k_diag)))

    # Pure LCDM
    print(f"{'LCDM':>10} | " + " | ".join([f"  1.000 " for _ in k_diag]))

    for Omega_chi in OMEGA_CHI_VALUES:
        T_chi, _, _, _ = EH_transfer_mixed(k, Omega_chi)
        Pk_chi = compute_Pk(k, T_chi, 1.0) * norm  # D_ratio=1 for constant MOND
        ratio = Pk_chi / Pk_LCDM

        vals = []
        for ki in k_diag:
            idx = np.argmin(np.abs(k - ki))
            vals.append(f"  {ratio[idx]:.3f} ")
        print(f"  {Omega_chi:.3f}   | " + " | ".join(vals))

    # Pure baryon
    Pk_bary_test = compute_Pk(k, T_bary, 1.0) * norm
    ratio_bary = Pk_bary_test / Pk_LCDM
    vals = []
    for ki in k_diag:
        idx = np.argmin(np.abs(k - ki))
        vals.append(f"  {ratio_bary[idx]:.3f} ")
    print(f"{'bary only':>10} | " + " | ".join(vals))

    # =========================================================================
    # KEY FINDING: The transfer function shape is the bottleneck
    # =========================================================================
    print("\n" + "=" * 80)
    print("KEY ANALYSIS: Transfer function vs Growth")
    print("=" * 80)

    print("\nThe two ingredients for matching LCDM P(k):")
    print("  1. TRANSFER FUNCTION SHAPE: T^2(k) -- set at recombination")
    print("  2. GROWTH AMPLITUDE: D^2 -- set by post-recombination evolution")
    print()
    print("MOND can fix the growth amplitude (nu ~ few => D matches LCDM)")
    print("But MOND cannot fix the transfer function shape after recombination.")
    print("The shape was set at z ~ 1100 by the matter content.")
    print()

    # Compare T^2 ratios
    print("T^2(k) / T^2_LCDM(k) at k = 0.1 h/Mpc:")
    for Omega_chi in OMEGA_CHI_VALUES:
        T_chi, _, _, _ = EH_transfer_mixed(k, Omega_chi)
        idx = np.argmin(np.abs(k - 0.1))
        T2_ratio = (T_chi[idx] / T_LCDM[idx])**2
        print(f"  Omega_chi = {Omega_chi:.3f}: T^2 ratio = {T2_ratio:.4f}")

    T_bary_ratio = (T_bary / T_LCDM)**2
    idx = np.argmin(np.abs(k - 0.1))
    print(f"  Baryon only:         T^2 ratio = {T_bary_ratio[idx]:.4f}")

    # =========================================================================
    # SUMMARY TABLE
    # =========================================================================
    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)
    print(f"\n{'Model':>25} | {'sigma8':>8} | {'sig8/tgt':>8} | {'shape':>8} | {'P/P_L(0.1)':>10}")
    print("-" * 70)

    print(f"{'LCDM':>25} | {SIGMA8_TARGET:>8.4f} | {'1.0000':>8} | {'0.0000':>8} | {'1.0000':>10}")
    print(f"{'Pure baryon':>25} | {sigma8_bary:>8.4f} | {sigma8_bary/SIGMA8_TARGET:>8.4f} | {'---':>8} | {'---':>10}")

    for key in sorted(results.keys()):
        r = results[key]
        label = key.replace('S1_', 'Const: ').replace('S2_', 'ScaleDep: ')
        print(f"{label:>25} | {r['sigma8']:>8.4f} | {r['sigma8']/SIGMA8_TARGET:>8.4f} | {r['shape_dev']:>8.4f} | {r['P_ratio_k01']:>10.4f}")

    return results, chi_grid, sigma8_grid_S1, shape_grid_S1, sigma8_grid_S2, shape_grid_S2


if __name__ == '__main__':
    results, chi_grid, s8_S1, shape_S1, s8_S2, shape_S2 = run_all_scenarios()
