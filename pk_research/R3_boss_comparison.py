#!/usr/bin/env python3
"""
Round 3: DFD Power Spectrum Prediction vs BOSS DR12 Constraints
================================================================

Computes P_DFD(k) = nu^2(k) * P_baryon(k) and compares to LCDM/BOSS.

Key fix: The EH no-wiggle formula fails for f_b = 1 (alpha_gamma < 0).
For baryon-only (Omega_m = Omega_b), we must use the FULL EH baryon
transfer function or a Sugiyama-corrected BBKS form.

Six parts:
  1. P_baryon(k) from baryon-only transfer function
  2. nu_required(k) = sqrt(P_LCDM / P_baryon)
  3. nu_predicted(k) from QUMOND mode-by-mode calculation
  4. Comparison: nu_required vs nu_predicted
  5. sigma_8, BAO peak, P_DFD/P_LCDM ratios
  6. Effective Omega_m from MOND-enhanced recombination

Author: Round 3 Agent (Claude)
"""

import numpy as np
from scipy.integrate import quad, solve_ivp
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CONSTANTS AND PARAMETERS
# =============================================================================
h_val = 0.674
Omega_b_h2 = 0.02237
Omega_b = Omega_b_h2 / h_val**2          # 0.0492
T_CMB = 2.725                              # K
n_s = 0.965
A_s = 2.1e-9
k_pivot = 0.05                             # Mpc^-1

# LCDM
Omega_m_LCDM = 0.315
Omega_cdm_h2 = 0.1200
Omega_m_h2_LCDM = Omega_cdm_h2 + Omega_b_h2  # 0.1424
Omega_Lambda = 1.0 - Omega_m_LCDM

# MOND
a0 = 1.2e-10          # m/s^2
G_N = 6.674e-11       # m^3 kg^-1 s^-2
Mpc_m = 3.0856775815e22  # m per Mpc
H0_si = h_val * 100 * 1e3 / Mpc_m  # s^-1
rho_crit = 3 * H0_si**2 / (8 * np.pi * G_N)
rho_b0 = Omega_b * rho_crit

# k grid (h/Mpc)
k_grid = np.logspace(-3, 0, 500)

print("=" * 72)
print("ROUND 3: DFD POWER SPECTRUM vs BOSS DR12")
print("=" * 72)
print(f"h = {h_val}, Omega_b = {Omega_b:.4f}, Omega_m(LCDM) = {Omega_m_LCDM}")
print(f"A_s = {A_s}, n_s = {n_s}, a0 = {a0} m/s^2")
print()


# =============================================================================
# TRANSFER FUNCTIONS
# =============================================================================

def BBKS_transfer(k_hmpc, omega_m_h2, omega_b_h2, h):
    """
    BBKS transfer function with Sugiyama (1995) shape correction.
    Valid for any baryon fraction. k in h/Mpc.
    """
    k = np.atleast_1d(k_hmpc).astype(float)
    theta = T_CMB / 2.7

    # Sugiyama shape parameter
    Gamma = omega_m_h2 / h * np.exp(-omega_b_h2 * (1 + np.sqrt(2*h) / (omega_m_h2/h)))

    q = k * theta**2 / Gamma
    T = np.log(1 + 2.34*q) / (2.34*q) * \
        (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    return np.squeeze(T)


def EH_no_wiggle(k_hmpc, omega_m_h2, omega_b_h2, h):
    """
    EH98 no-wiggle transfer function.
    Falls back to BBKS for f_b > 0.5 where the formula is unreliable.
    """
    f_b = omega_b_h2 / omega_m_h2
    if f_b > 0.5:
        return BBKS_transfer(k_hmpc, omega_m_h2, omega_b_h2, h)

    k = np.atleast_1d(k_hmpc).astype(float)
    theta = T_CMB / 2.7

    s = 44.5 * np.log(9.83 / omega_m_h2) / np.sqrt(1 + 10 * omega_b_h2**0.75)
    alpha_gamma = 1 - 0.328 * np.log(431 * omega_m_h2) * f_b + \
                  0.38 * np.log(22.3 * omega_m_h2) * f_b**2
    Gamma_eff = omega_m_h2 / h * (alpha_gamma + (1 - alpha_gamma) / \
                (1 + (0.43 * k * s)**4))

    q = k * theta**2 / Gamma_eff
    L0 = np.log(2 * np.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1 + 62.5 * q)
    T = L0 / (L0 + C0 * q**2)
    return np.squeeze(np.abs(T))


def EH_baryon_acoustic(omega_m_h2, omega_b_h2, h):
    """
    Compute key acoustic parameters from the EH98 formalism.
    Returns z_eq, z_d, s (sound horizon in Mpc/h), k_silk.
    """
    theta = T_CMB / 2.7
    z_eq = 2.5e4 * omega_m_h2 * theta**(-4)
    k_eq = 7.46e-2 * omega_m_h2 * theta**(-2)

    b1_d = 0.313 * omega_m_h2**(-0.419) * (1 + 0.607 * omega_m_h2**0.674)
    b2_d = 0.238 * omega_m_h2**0.223
    z_d = 1291 * omega_m_h2**0.251 / (1 + 0.659 * omega_m_h2**0.828) * \
          (1 + b1_d * omega_b_h2**b2_d)

    R_d = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_d)
    R_eq = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_eq)

    s = (2 / (3 * k_eq)) * np.sqrt(6 / R_eq) * \
        np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    k_silk = 1.6 * omega_b_h2**0.52 * omega_m_h2**0.73 * \
             (1 + (10.4 * omega_m_h2)**(-0.95))

    return z_eq, z_d, s, k_silk


# =============================================================================
# PART 1: COMPUTE TRANSFER FUNCTIONS AND P_baryon
# =============================================================================
print("=" * 72)
print("PART 1: Transfer Functions and P_baryon(k)")
print("=" * 72)

# LCDM
T_LCDM = EH_no_wiggle(k_grid, Omega_m_h2_LCDM, Omega_b_h2, h_val)
z_eq_LCDM, z_d_LCDM, s_LCDM, k_silk_LCDM = \
    EH_baryon_acoustic(Omega_m_h2_LCDM, Omega_b_h2, h_val)

# Baryon-only (Omega_m = Omega_b)
omega_m_h2_bary = Omega_b_h2
T_baryon = BBKS_transfer(k_grid, omega_m_h2_bary, Omega_b_h2, h_val)
z_eq_bary, z_d_bary, s_bary, k_silk_bary = \
    EH_baryon_acoustic(omega_m_h2_bary, Omega_b_h2, h_val)

# Apply Silk damping envelope to baryon-only transfer function
# Silk damping: exp(-(k/k_silk)^1.4) suppresses power on small scales
# For baryon-only universe, ALL matter is coupled to photons before decoupling
T_baryon_damped = T_baryon * np.exp(-(k_grid * h_val / k_silk_bary)**1.4)

print(f"Baryon-only universe:")
print(f"  z_eq = {z_eq_bary:.0f}  (LCDM: {z_eq_LCDM:.0f})")
print(f"  z_drag = {z_d_bary:.0f}  (LCDM: {z_d_LCDM:.0f})")
print(f"  Sound horizon s = {s_bary:.1f} Mpc/h  (LCDM: {s_LCDM:.1f} Mpc/h)")
print(f"  BAO fundamental k_BAO ~ pi/s = {np.pi/s_bary:.4f} h/Mpc  "
      f"(LCDM: {np.pi/s_LCDM:.4f} h/Mpc)")
print(f"  Silk damping k_silk = {k_silk_bary:.4f} Mpc^-1  "
      f"(LCDM: {k_silk_LCDM:.4f} Mpc^-1)")
print()

# Check T values at key k
print(f"Transfer function comparison:")
print(f"{'k (h/Mpc)':<12} {'T_LCDM':>10} {'T_bary':>10} {'T_bary_damp':>12} {'T_L/T_b':>10}")
print("-" * 56)
for kk in [0.005, 0.01, 0.05, 0.1, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_grid - kk))
    tl = T_LCDM[idx]
    tb = T_baryon[idx]
    tbd = T_baryon_damped[idx]
    print(f"{k_grid[idx]:<12.4f} {tl:>10.4f} {tb:>10.4f} {tbd:>12.6f} {tl/tb:>10.2f}")
print()


# =============================================================================
# GROWTH FACTORS
# =============================================================================
def growth_factor(Omega_m_val, z_eval=0):
    """Linear growth factor D(z) via ODE. Returns raw value."""
    Omega_L = 1.0 - Omega_m_val

    def deriv(lna, y):
        a = np.exp(lna)
        E2 = Omega_m_val / a**3 + Omega_L
        dlnH = -1.5 * Omega_m_val / (a**3 * E2)
        D, dD = y
        ddD = -(2 + dlnH) * dD + 1.5 * Omega_m_val / (a**3 * E2) * D
        return [dD, ddD]

    a_init = 1e-4
    a_end = 1.0 / (1 + z_eval)
    sol = solve_ivp(deriv, [np.log(a_init), np.log(a_end)],
                    [a_init, 1.0], rtol=1e-10, atol=1e-12)
    return sol.y[0, -1]


D_LCDM_raw = growth_factor(Omega_m_LCDM, 0)
D_baryon_raw = growth_factor(Omega_b, 0)
D_norm_baryon = D_baryon_raw / D_LCDM_raw

print(f"Growth factors (z=0, Newtonian):")
print(f"  D_LCDM(raw) = {D_LCDM_raw:.4f}, normalized to 1.0")
print(f"  D_baryon = {D_baryon_raw:.4f}, ratio = {D_norm_baryon:.4f}")
print()


# =============================================================================
# POWER SPECTRA (using Silk-damped baryon transfer function)
# =============================================================================
def Pk_unnorm(k_hmpc, T_k):
    """Unnormalized P(k) ~ k^{n_s-1} T^2(k)."""
    k_Mpc = k_hmpc * h_val
    return (k_Mpc / k_pivot)**(n_s - 1) * T_k**2


def sigma_R(R, k_arr, Pk_arr):
    """sigma(R). R in Mpc/h, k in h/Mpc."""
    lnk_arr = np.log(k_arr)
    lnPk_arr = np.log(np.maximum(Pk_arr, 1e-100))
    def integrand(lnk_val):
        kk = np.exp(lnk_val)
        Pk = np.exp(np.interp(lnk_val, lnk_arr, lnPk_arr))
        x = kk * R
        W = 3 * (np.sin(x) - x * np.cos(x)) / x**3 if x > 1e-6 else 1.0
        return kk**3 * Pk * W**2 / (2 * np.pi**2)
    result, _ = quad(integrand, lnk_arr[0], lnk_arr[-1], limit=300)
    return np.sqrt(max(result, 0))


# Normalize to sigma_8(LCDM) = 0.811
Pk_LCDM_unnorm = Pk_unnorm(k_grid, T_LCDM)
sig8_unnorm = sigma_R(8.0, k_grid, Pk_LCDM_unnorm)
sigma8_target = 0.811
norm_const = (sigma8_target / sig8_unnorm)**2

Pk_LCDM = norm_const * Pk_LCDM_unnorm

# Baryon-only with Silk damping and reduced growth
Pk_baryon = norm_const * Pk_unnorm(k_grid, T_baryon_damped) * D_norm_baryon**2

sig8_LCDM = sigma_R(8.0, k_grid, Pk_LCDM)
sig8_baryon = sigma_R(8.0, k_grid, Pk_baryon)

print(f"Normalized power spectra:")
print(f"  norm_const = {norm_const:.4e}")
print(f"  sigma_8(LCDM) = {sig8_LCDM:.4f}")
print(f"  sigma_8(baryon, Silk-damped) = {sig8_baryon:.6f}")
print(f"  P_LCDM/P_baryon at k=0.1: "
      f"{np.interp(0.1, k_grid, Pk_LCDM)/np.interp(0.1, k_grid, Pk_baryon):.1f}")
print()


# =============================================================================
# PART 2: nu_required(k)
# =============================================================================
print("=" * 72)
print("PART 2: Required MOND Enhancement nu_required(k)")
print("=" * 72)

nu_required = np.sqrt(Pk_LCDM / np.maximum(Pk_baryon, 1e-30))

k_report = [0.005, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.50, 1.0]
print(f"{'k (h/Mpc)':<12} {'nu_req':>10} {'P_LCDM':>14} {'P_baryon':>14} {'ratio':>10}")
print("-" * 62)
for kk in k_report:
    idx = np.argmin(np.abs(k_grid - kk))
    pl = Pk_LCDM[idx]
    pb = Pk_baryon[idx]
    print(f"{k_grid[idx]:<12.4f} {nu_required[idx]:>10.2f} "
          f"{pl:>14.4e} {pb:>14.4e} {pl/pb:>10.1f}")
print()


# =============================================================================
# PART 3: nu_predicted(k) from QUMOND
# =============================================================================
print("=" * 72)
print("PART 3: QUMOND Predicted nu(k)")
print("=" * 72)

Delta2_baryon = k_grid**3 * Pk_baryon / (2 * np.pi**2)
delta_rms = np.sqrt(np.maximum(Delta2_baryon, 0))

k_phys = k_grid * h_val / Mpc_m  # m^-1
g_N_mode = 4 * np.pi * G_N * rho_b0 * delta_rms * (2 * np.pi / k_phys)
y_mode = g_N_mode / a0

def nu_QUMOND(y):
    y_safe = np.maximum(y, 1e-30)
    return 0.5 * (1 + np.sqrt(1 + 4.0/y_safe))

nu_predicted = nu_QUMOND(y_mode)

print(f"{'k (h/Mpc)':<12} {'delta_rms':>10} {'y(k)':>12} {'nu_pred':>10} {'nu_req':>10}")
print("-" * 56)
for kk in k_report:
    idx = np.argmin(np.abs(k_grid - kk))
    print(f"{k_grid[idx]:<12.4f} {delta_rms[idx]:>10.2e} "
          f"{y_mode[idx]:>12.4e} {nu_predicted[idx]:>10.2f} {nu_required[idx]:>10.2f}")
print()


# =============================================================================
# PART 4: COMPARISON
# =============================================================================
print("=" * 72)
print("PART 4: Comparison nu_predicted vs nu_required")
print("=" * 72)

ratio_nu = nu_predicted / nu_required

print(f"{'k (h/Mpc)':<12} {'nu_pred':>10} {'nu_req':>10} {'pred/req':>10} {'status':>22}")
print("-" * 66)
for kk in k_report:
    idx = np.argmin(np.abs(k_grid - kk))
    r = ratio_nu[idx]
    if r > 1.1:
        status = "EXCESS power"
    elif r < 0.9:
        status = "DEFICIT"
    else:
        status = "~MATCH (within 10%)"
    print(f"{k_grid[idx]:<12.4f} {nu_predicted[idx]:>10.2f} {nu_required[idx]:>10.2f} "
          f"{r:>10.3f} {status:>22}")

# Crossover
for target_r in [0.5, 1.0, 2.0]:
    idx_c = np.argmin(np.abs(ratio_nu - target_r))
    print(f"\n  nu_pred/nu_req = {target_r:.1f} at k ~ {k_grid[idx_c]:.4f} h/Mpc")
print()


# =============================================================================
# PART 5: sigma_8, BAO, P_DFD/P_LCDM
# =============================================================================
print("=" * 72)
print("PART 5: sigma_8, BAO, and Power Ratio")
print("=" * 72)

Pk_DFD = nu_predicted**2 * Pk_baryon
sig8_DFD = sigma_R(8.0, k_grid, Pk_DFD)

print(f"sigma_8 values:")
print(f"  sigma_8(LCDM)    = {sig8_LCDM:.4f}")
print(f"  sigma_8(baryon)  = {sig8_baryon:.4f}")
print(f"  sigma_8(DFD)     = {sig8_DFD:.4f}")
print(f"  sigma_8(DFD)/sigma_8(LCDM) = {sig8_DFD/sig8_LCDM:.4f}")
print()

# BAO
print(f"BAO scales:")
print(f"  LCDM: s = {s_LCDM:.1f} Mpc/h => k_BAO = {np.pi/s_LCDM:.4f} h/Mpc")
print(f"  Baryon-only: s = {s_bary:.1f} Mpc/h => k_BAO = {np.pi/s_bary:.4f} h/Mpc")
print(f"  BOSS DR12 measures r_d = 147.8 Mpc (comoving)")
print(f"  In h/Mpc units: r_d*h = {147.8 * h_val:.1f} Mpc/h")
print()

# P_DFD/P_LCDM
print(f"Power spectrum ratios P_DFD/P_LCDM:")
print(f"{'k (h/Mpc)':<12} {'P_DFD/P_LCDM':>15}")
print("-" * 29)
for kk in [0.02, 0.05, 0.10, 0.15, 0.20]:
    idx = np.argmin(np.abs(k_grid - kk))
    r = Pk_DFD[idx] / Pk_LCDM[idx]
    print(f"{k_grid[idx]:<12.4f} {r:>15.4f}")
print()


# =============================================================================
# PART 6: EFFECTIVE Omega_m FROM MOND AT RECOMBINATION
# =============================================================================
print("=" * 72)
print("PART 6: Effective Omega_m from MOND at Recombination")
print("=" * 72)

z_rec = 1100
rho_rec = rho_b0 * (1 + z_rec)**3

D_rec_raw = growth_factor(Omega_b, z_rec)
D_0_raw = growth_factor(Omega_b, 0)
D_ratio_rec = D_rec_raw / D_0_raw

delta_rms_rec = delta_rms * D_ratio_rec
g_rec = 4 * np.pi * G_N * rho_rec * delta_rms_rec * (2 * np.pi / k_phys)
y_rec = g_rec / a0
nu_rec_arr = nu_QUMOND(y_rec)
Omega_m_eff_rec = nu_rec_arr * Omega_b

print(f"At z = {z_rec}: rho/rho_0 = {(1+z_rec)**3:.2e}, D_rec/D_0 = {D_ratio_rec:.6f}")
print()

print(f"{'k (h/Mpc)':<12} {'delta_rec':>10} {'y_rec':>12} {'nu_rec':>10} {'Om_eff':>10}")
print("-" * 56)
for kk in k_report:
    idx = np.argmin(np.abs(k_grid - kk))
    print(f"{k_grid[idx]:<12.4f} {delta_rms_rec[idx]:>10.2e} "
          f"{y_rec[idx]:>12.4e} {nu_rec_arr[idx]:>10.3f} "
          f"{Omega_m_eff_rec[idx]:>10.4f}")
print()

# What nu_rec NEEDED to match LCDM?
nu_rec_match = Omega_m_h2_LCDM / Omega_b_h2
print(f"To match LCDM: nu_rec = Omega_m_h2/Omega_b_h2 = {nu_rec_match:.3f}")
print(f"  => Omega_m,eff = {nu_rec_match * Omega_b:.4f} (LCDM: {Omega_m_LCDM})")
print()

# Scan nu_rec values
print("Transfer function with Omega_m,eff = nu_rec * Omega_b:")
print(f"{'nu_rec':>6} {'Om_eff':>8} {'z_eq':>8} {'s(Mpc/h)':>10} "
      f"{'k_BAO':>8} {'T/T_L(0.1)':>11} {'sig8_rat':>10}")
print("-" * 63)

for nu_r in [1, 2, 3, 4, 5, 6, 6.4, 7, 10]:
    Om_eff = nu_r * Omega_b
    Om_eff_h2 = Om_eff * h_val**2

    T_eff = EH_no_wiggle(k_grid, Om_eff_h2, Omega_b_h2, h_val)
    z_eq_eff, _, s_eff, _ = EH_baryon_acoustic(Om_eff_h2, Omega_b_h2, h_val)

    T_at_01 = np.interp(0.1, k_grid, T_eff)
    T_LCDM_at_01 = np.interp(0.1, k_grid, T_LCDM)

    Pk_eff = Pk_unnorm(k_grid, T_eff)
    sig8_eff = sigma_R(8.0, k_grid, Pk_eff)
    sig8_LCDM_u = sigma_R(8.0, k_grid, Pk_LCDM_unnorm)

    print(f"{nu_r:>6.1f} {Om_eff:>8.4f} {z_eq_eff:>8.0f} "
          f"{s_eff:>10.1f} {np.pi/s_eff:>8.4f} "
          f"{T_at_01/T_LCDM_at_01:>11.4f} {sig8_eff/sig8_LCDM_u:>10.4f}")
print()


# =============================================================================
# MATCHED TRANSFER FUNCTION ANALYSIS
# =============================================================================
print("=" * 72)
print("MATCHED: DFD with constant nu = 6.4 (Omega_m,eff = LCDM)")
print("=" * 72)

Om_match_h2 = nu_rec_match * Omega_b * h_val**2
T_match = EH_no_wiggle(k_grid, Om_match_h2, Omega_b_h2, h_val)
z_eq_m, z_d_m, s_m, ks_m = EH_baryon_acoustic(Om_match_h2, Omega_b_h2, h_val)

print(f"nu = {nu_rec_match:.3f}, Omega_m,eff = {nu_rec_match*Omega_b:.4f}")
print(f"  z_eq = {z_eq_m:.0f} (LCDM: {z_eq_LCDM:.0f})")
print(f"  z_drag = {z_d_m:.0f} (LCDM: {z_d_LCDM:.0f})")
print(f"  s = {s_m:.2f} Mpc/h (LCDM: {s_LCDM:.2f} Mpc/h)")
print(f"  k_BAO = {np.pi/s_m:.4f} h/Mpc (LCDM: {np.pi/s_LCDM:.4f} h/Mpc)")
print()

# With constant nu = 6.4:
# Growth: D_DFD solves same ODE as D_LCDM (nu*Omega_b = Omega_m_LCDM)
# Transfer: T(k) computed with Omega_m,eff = Omega_m_LCDM
# => P_DFD = P_LCDM exactly (up to f_b differences in the transfer function)
Pk_DFD_matched = norm_const * Pk_unnorm(k_grid, T_match)
sig8_matched = sigma_R(8.0, k_grid, Pk_DFD_matched)

print(f"sigma_8(DFD, matched) = {sig8_matched:.4f}")
print()

print(f"P_DFD_matched / P_LCDM:")
print(f"{'k (h/Mpc)':<12} {'ratio':>10}")
print("-" * 24)
for kk in [0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.50]:
    idx = np.argmin(np.abs(k_grid - kk))
    print(f"{k_grid[idx]:<12.4f} {Pk_DFD_matched[idx]/Pk_LCDM[idx]:>10.4f}")
print()

# The key: with Omega_m,eff*h^2 = Omega_m*h^2 AND the same f_b ratio
# in the formula (since f_b = Omega_b/(nu*Omega_b) = 1/nu ~ Omega_b/Omega_m),
# the transfer functions are IDENTICAL.
print(f"Baryon fractions:")
print(f"  DFD: f_b = Omega_b/Omega_m,eff = 1/nu = {1/nu_rec_match:.4f}")
print(f"  LCDM: f_b = Omega_b/Omega_m = {Omega_b/Omega_m_LCDM:.4f}")
print(f"  Difference: {abs(1/nu_rec_match - Omega_b/Omega_m_LCDM)/Omega_b*Omega_m_LCDM*100:.2f}%")
print()


# =============================================================================
# THE CRITICAL QUESTION: Can MOND at recombination provide nu ~ 6.4?
# =============================================================================
print("=" * 72)
print("CRITICAL: Can MOND provide nu ~ 6.4 at recombination?")
print("=" * 72)

# The mode-by-mode y parameter at z=1100 depends on:
# 1. rho(z_rec) ~ rho_0 * (1+z)^3 -- very large
# 2. delta(z_rec) ~ delta_0 * D(z_rec)/D(0) -- very small
# 3. lambda = 2*pi/k -- depends on scale
# g_N = 4*pi*G*rho*delta*lambda/(2*pi) = 4*pi*G*rho*delta/k

# At recombination, the combination is:
# y = g/a0 = (4*pi*G*rho_rec*delta_rec*(2*pi/k)) / a0

# But there's a DIFFERENT way to think about it: the background acceleration
# At the horizon scale, g ~ H^2 * d_H ~ H * c ~ a0 at certain z
# The critical redshift where H(z) ~ a0/c is:
# H(z) ~ H0 * sqrt(Omega_m * (1+z)^3) ~ a0/c
# (1+z)^3 ~ (a0/(c*H0))^2 / Omega_m
a0_over_cH0 = a0 / (2.998e8 * H0_si)
print(f"a0/(c*H0) = {a0_over_cH0:.4f}")
z_mond_bg = (a0_over_cH0**2 / Omega_b)**(1/3) - 1
print(f"Background MOND transition (g_bg = a0): z ~ {z_mond_bg:.1f}")
print(f"  At z > {z_mond_bg:.0f}: background gravity > a0 (Newtonian)")
print(f"  At z < {z_mond_bg:.0f}: background gravity < a0 (MOND regime)")
print()

# For PERTURBATIONS, the relevant acceleration is the perturbation gravity:
# g_pert = 4*pi*G*rho*delta*R where R ~ 1/k
# This scales differently: g_pert / a0 depends on k AND delta

# The key realization: at recombination, y >> 1 for most k because
# rho_rec >> rho_0, even though delta is tiny. The (1+z)^3 factor WINS.
# This means MOND is in the NEWTONIAN regime at recombination!

# HOWEVER: the DFD framework uses the FIELD equation, not the
# particle-level MOND formula. The field equation operates on the
# gravitational POTENTIAL, not individual particle accelerations.

# In the DFD field equation: del . [nu(|grad Phi_N|/a0) grad Phi_N] = 4*pi*G*rho
# For a perturbation: Phi_N ~ G * rho * delta / k^2
# |grad Phi_N| ~ k * Phi_N ~ G * rho * delta / k

# y_field = |grad Phi_N| / (a0 * l_characteristic)
# This is DIFFERENT from the mode-by-mode y computed above

# For the background (homogeneous): Phi_N_bg ~ G * rho * H^{-2}
# |grad Phi_N_bg| ~ G * rho / H ~ (3/2) * Omega_m * H
# y_bg = (3/2) * Omega_m * H / a0 * c  ...

# Actually: for the background,
# g_bg = (1/2) * Omega_m * H^2 * R_H = c * Omega_m * H / 2
g_bg_now = 2.998e8 * Omega_b * H0_si / 2
g_bg_rec = 2.998e8 * Omega_b * H0_si * np.sqrt(Omega_b * (1+z_rec)**3) / 2
y_bg_now = g_bg_now / a0
y_bg_rec = g_bg_rec / a0
print(f"Background gravitational acceleration / a0:")
print(f"  z=0: y_bg = {y_bg_now:.4f}  => DEEP MOND")
print(f"  z={z_rec}: y_bg = {y_bg_rec:.1f}  => {'NEWTONIAN' if y_bg_rec > 1 else 'MOND'}")
print()

# KEY RESULT: at z=1100, y_bg ~ 100-1000 => solidly Newtonian!
# MOND effects are negligible at recombination for the background.
# For perturbations: y_pert = delta * y_bg, so y_pert << 1 if delta << 1/y_bg
# Since delta ~ 10^-5 and y_bg ~ 100: y_pert ~ 10^-3, which IS deep MOND!

# But wait: the MOND field equation is about the TOTAL field, not perturbations.
# The interpolating function evaluates |grad Phi_total|/a0, not |grad delta_Phi|/a0.
# So the background field is Newtonian, and small perturbations ride on top.

# For linearized perturbations around a Newtonian background:
# nu(y_bg) * delta_Phi + (d_nu/dy) * (grad_delta_Phi . grad_Phi_bg) / (a0 * |grad Phi_bg|) = ...
# Since y_bg >> 1 and nu(y>>1) ~ 1, the perturbation equation reduces to Newtonian!

# THE CONCLUSION: MOND cannot enhance perturbation growth at recombination
# because the BACKGROUND is in the Newtonian regime.

print("CONCLUSION ON RECOMBINATION MOND:")
print("-" * 40)
print(f"  At z={z_rec}, y_background ~ {y_bg_rec:.0f} >> 1")
print(f"  The universe is in the NEWTONIAN regime at recombination.")
print(f"  Linearized perturbations around a Newtonian background")
print(f"  have nu_eff ~ 1 (no MOND enhancement).")
print(f"  The transfer function CANNOT be fixed by MOND at recombination.")
print()
print(f"  MOND kicks in AFTER z ~ {z_mond_bg:.0f} when background gravity < a0.")
print(f"  This is the epoch when growth enhancement occurs.")
print(f"  But the SHAPE of T(k) is set at recombination, not later.")
print()


# =============================================================================
# WHAT DOES DFD ACTUALLY NEED?
# =============================================================================
print("=" * 72)
print("WHAT DFD NEEDS TO MATCH OBSERVATIONS")
print("=" * 72)

print(f"""
The fundamental challenge for DFD:

1. The transfer function T(k) is set at recombination (z ~ 1100).
   At this epoch, MOND is INACTIVE because the background gravity >> a0.
   Therefore T(k) is the standard baryon-only (no CDM) transfer function.

2. With Omega_m = Omega_b = 0.049:
   - z_eq = {z_eq_bary:.0f} (need {z_eq_LCDM:.0f})
   - Sound horizon = {s_bary:.1f} Mpc/h (need {s_LCDM:.1f} Mpc/h)
   - No CDM driving potential: T(k) drops much faster at high k

3. After recombination (z < {z_mond_bg:.0f}), MOND activates and can
   enhance growth by factor nu(k). But nu only multiplies the AMPLITUDE,
   not the SHAPE of T(k).

4. To match LCDM with nu^2 * P_baryon = P_LCDM, DFD needs:
   - nu_required ~ {np.mean(nu_required[(k_grid>0.01)&(k_grid<0.1)]):.1f} at BOSS scales (0.01-0.1 h/Mpc)
   - nu must compensate for BOTH the smaller T(k) AND the smaller D(z)
   - nu must have the RIGHT k-dependence to reshape T(k) to match LCDM

5. The QUMOND mode-by-mode prediction gives:
   - nu_predicted too large at large scales (k < 0.01)
   - Uncertain at small scales due to Silk damping
   - y << 1 everywhere at z=0: deep MOND regime, nu ~ 1/sqrt(y)

6. POSSIBLE RESOLUTIONS:
   a) The DFD scalar field provides additional metric perturbation (psi)
      that acts like a CDM gravitational potential even at recombination
   b) The DFD field equation has a DIFFERENT interpolating function
      that saturates at nu ~ 6.4 rather than growing without bound
   c) Non-perturbative MOND effects (the field equation is nonlinear)
      generate an effective CDM-like contribution to the Poisson equation
   d) The observed power spectrum includes bias, RSD, and nonlinear
      corrections that mask the bare DFD prediction
""")


# =============================================================================
# QUANTITATIVE SUMMARY TABLE
# =============================================================================
print("=" * 72)
print("QUANTITATIVE SUMMARY")
print("=" * 72)

# Constant-nu model: what constant nu matches sigma_8?
# sigma_8(DFD) = nu * sigma_8(baryon) = 0.811
# nu = 0.811 / sigma_8(baryon)
nu_for_sig8 = sigma8_target / sig8_baryon
print(f"Constant nu for sigma_8 = 0.811: nu = {nu_for_sig8:.2f}")
print(f"  Compare to Omega_m/Omega_b = {Omega_m_LCDM/Omega_b:.2f}")
print()

# But this constant nu doesn't fix the SHAPE
# P_DFD(k)/P_LCDM(k) = nu^2 * P_baryon(k)/P_LCDM(k) = nu^2 * (T_bary/T_LCDM)^2 * D_bary^2
# = nu^2 * D_bary^2 * (T_bary/T_LCDM)^2

print(f"Shape mismatch: T_baryon/T_LCDM at key scales:")
print(f"{'k (h/Mpc)':<12} {'T_bary/T_LCDM':>14} {'nu_shape_needed':>16}")
print("-" * 44)
for kk in [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]:
    idx = np.argmin(np.abs(k_grid - kk))
    tb = T_baryon_damped[idx]
    tl = T_LCDM[idx]
    rat = tb / tl
    # nu^2 * D_baryon^2 * (T_b/T_L)^2 = 1 => nu = T_L/(T_b * D_baryon)
    nu_shape = tl / (tb * D_norm_baryon) if tb > 1e-20 else float('inf')
    print(f"{k_grid[idx]:<12.4f} {rat:>14.6f} {nu_shape:>16.2f}")

print()
print("If nu is scale-INDEPENDENT, P_DFD/P_LCDM varies by orders of magnitude")
print("across k. DFD requires a STRONGLY scale-dependent nu to match LCDM shape.")
print()


# =============================================================================
# PLOTS
# =============================================================================
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(3, 2, figsize=(14, 16))
    fig.suptitle('Round 3: DFD Power Spectrum vs BOSS DR12',
                 fontsize=14, fontweight='bold')

    # 1. Transfer functions
    ax = axes[0, 0]
    ax.loglog(k_grid, T_LCDM, 'b-', lw=2, label=r'$T_{\Lambda CDM}$')
    ax.loglog(k_grid, T_baryon, 'r-', lw=2, label=r'$T_{baryon}$ (BBKS)')
    ax.loglog(k_grid, T_baryon_damped, 'r--', lw=2, label=r'$T_{baryon}$ + Silk')
    ax.loglog(k_grid, T_match, 'g:', lw=2,
              label=rf'$T(\Omega_{{m,eff}})$, $\nu$={nu_rec_match:.1f}')
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel('T(k)')
    ax.set_title('Transfer Functions')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.grid(True, alpha=0.3)

    # 2. Power spectra
    ax = axes[0, 1]
    ax.loglog(k_grid, Pk_LCDM, 'b-', lw=2, label=r'$P_{\Lambda CDM}$')
    ax.loglog(k_grid, Pk_baryon, 'r-', lw=2, label=r'$P_{baryon}$')
    ax.loglog(k_grid, Pk_DFD, 'm--', lw=2, label=r'$P_{DFD}$ (QUMOND)')
    ax.loglog(k_grid, Pk_DFD_matched, 'g:', lw=2,
              label=rf'$P_{{DFD}}$ ($\nu$={nu_rec_match:.1f})')
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel(r'P(k) [arb.]')
    ax.set_title('Power Spectra')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.grid(True, alpha=0.3)

    # 3. nu_required vs nu_predicted
    ax = axes[1, 0]
    ax.loglog(k_grid, nu_required, 'b-', lw=2, label=r'$\nu_{required}$')
    ax.loglog(k_grid, nu_predicted, 'r-', lw=2, label=r'$\nu_{predicted}$ (QUMOND)')
    ax.axhline(nu_rec_match, color='gray', ls='--', alpha=0.6,
               label=rf'$\Omega_m/\Omega_b = {nu_rec_match:.1f}$')
    ax.fill_between(k_grid, nu_required*0.8, nu_required*1.2,
                    alpha=0.1, color='blue')
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel(r'$\nu(k)$')
    ax.set_title(r'Required vs Predicted $\nu(k)$')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.set_ylim(1, 1e4)
    ax.grid(True, alpha=0.3)

    # 4. y parameter
    ax = axes[1, 1]
    ax.loglog(k_grid, y_mode, 'r-', lw=2, label='y(k) at z=0')
    ax.loglog(k_grid, y_rec, 'b-', lw=2, label=f'y(k) at z={z_rec}')
    ax.axhline(1, color='gray', ls='--', alpha=0.5, label='y=1')
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel(r'$y = g_N/a_0$')
    ax.set_title('MOND Acceleration Parameter')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.grid(True, alpha=0.3)

    # 5. P_DFD/P_LCDM
    ax = axes[2, 0]
    ax.semilogx(k_grid, Pk_DFD/Pk_LCDM, 'r-', lw=2, label='QUMOND mode-by-mode')
    ax.semilogx(k_grid, Pk_DFD_matched/Pk_LCDM, 'g-', lw=2,
                label=rf'Matched ($\nu$={nu_rec_match:.1f})')
    ax.axhline(1, color='gray', ls='--', alpha=0.5)
    ax.fill_between(k_grid, 0.9, 1.1, alpha=0.1, color='blue')
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel(r'$P_{DFD}/P_{\Lambda CDM}$')
    ax.set_title('Power Ratio')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.set_ylim(0, 5)
    ax.grid(True, alpha=0.3)

    # 6. Shape mismatch
    ax = axes[2, 1]
    shape_ratio = T_baryon_damped / (T_LCDM + 1e-30)
    ax.semilogx(k_grid, shape_ratio, 'r-', lw=2, label=r'$T_{baryon}/T_{\Lambda CDM}$')
    ax.semilogx(k_grid, 1.0/nu_required, 'm--', lw=1.5,
                label=r'$1/\nu_{required}$ (including growth)')
    ax.axhline(1, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('k [h/Mpc]'); ax.set_ylabel('Ratio')
    ax.set_title('Shape Mismatch: T_baryon vs T_LCDM')
    ax.legend(fontsize=9); ax.set_xlim(1e-3, 1); ax.set_ylim(0, 2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = '/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R3_boss_comparison.png'
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved to {outpath}")
except ImportError:
    print("\nMatplotlib not available.")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
