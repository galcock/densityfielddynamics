#!/usr/bin/env python3
"""
R6 DEFINITIVE DFD P(k) SOLVER
==============================
Complete calculation including ALL identified mechanisms from 66 agents.

Mechanisms included:
  1. MOND-modified transfer function (self-consistent nu at recombination)
  2. Post-recombination MOND-enhanced growth with sigma_nabla regulation
  3. Mode coupling P_b * P_b (Agent 13)
  4. Psi-screen k-remapping and volume boost
  5. Nonlinear 3-Laplacian analysis
  6. Galaxy bias correction

Author: R6 Final Agent (Claude)
Date: 2026-04-05
"""

import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.interpolate import interp1d
from scipy.signal import fftconvolve
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================
H0_km_s_Mpc = 67.4
h = H0_km_s_Mpc / 100.0
H0_si = H0_km_s_Mpc * 1e3 / 3.0856775814913673e22  # s^-1
c_light = 2.998e8  # m/s

Omega_b_h2 = 0.02237
Omega_b = Omega_b_h2 / h**2   # ~0.0492
Omega_m_LCDM = 0.315
Omega_Lambda = 0.685

T_CMB = 2.725  # K
n_s = 0.965
A_s = 2.1e-9

a0_MOND = 1.2e-10  # m/s^2
G_N = 6.674e-11    # m^3/(kg s^2)
Mpc_m = 3.0856775814913673e22  # m
c_si = c_light

a_star = 2 * a0_MOND / c_light**2  # ~2.67e-27 m^-1

rho_crit_0 = 3 * H0_si**2 / (8 * np.pi * G_N)  # kg/m^3
rho_b_0 = Omega_b * rho_crit_0

# Recombination parameters
z_rec = 1089.0
a_rec = 1.0 / (1 + z_rec)

# Derived
nu_needed = Omega_m_LCDM / Omega_b  # ~6.40

print("=" * 80)
print("R6 DEFINITIVE DFD P(k) SOLVER")
print("=" * 80)
print(f"  H0 = {H0_km_s_Mpc} km/s/Mpc, h = {h}")
print(f"  Omega_b = {Omega_b:.6f}, Omega_b h^2 = {Omega_b_h2}")
print(f"  Omega_m (LCDM) = {Omega_m_LCDM}, Omega_Lambda = {Omega_Lambda}")
print(f"  a0 = {a0_MOND:.2e} m/s^2, a* = {a_star:.3e} m^-1")
print(f"  nu_needed = Omega_m/Omega_b = {nu_needed:.3f}")
print(f"  rho_b_0 = {rho_b_0:.4e} kg/m^3")
print(f"  z_rec = {z_rec}, a_rec = {a_rec:.6e}")

# =============================================================================
# EXPANSION FUNCTIONS
# =============================================================================
def E_sq(a):
    """(H/H0)^2 using LCDM background (DFD modifies gravity, not expansion)"""
    return Omega_m_LCDM / a**3 + Omega_Lambda

def E_sq_baryon(a):
    """(H/H0)^2 for baryon-only universe (used in some comparisons)"""
    return Omega_b / a**3 + Omega_Lambda

# =============================================================================
# EISENSTEIN-HU TRANSFER FUNCTIONS
# =============================================================================
def EH_transfer(k_hMpc, omega_m, omega_b):
    """
    Eisenstein-Hu 1998 no-wiggle transfer function.
    omega_m = Omega_m * h^2, omega_b = Omega_b * h^2
    Returns T(k), sound_horizon
    """
    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    f_b = omega_b / max(omega_m, 1e-15)
    f_c = 1 - f_b

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * max(omega_m, 1e-10)**(-0.419) * (1 + 0.607 * max(omega_m, 1e-10)**0.674)
    b2 = 0.238 * max(omega_m, 1e-10)**0.223
    z_d = (1291 * max(omega_m, 1e-10)**0.251 /
           (1 + 0.659 * max(omega_m, 1e-10)**0.828) *
           (1 + b1 * max(omega_b, 1e-15)**b2))

    R_eq = 31.5e3 * omega_b * theta**(-4) / max(z_eq, 1)
    R_d = 31.5e3 * omega_b * theta**(-4) / max(z_d, 1)

    s = (2.0 / (3 * max(k_eq, 1e-15))) * np.sqrt(6 / max(R_eq, 1e-10)) * np.log(
        (np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(max(R_eq, 1e-10))))

    # No-wiggle (Eq 29-31 of EH98)
    alpha_gamma = 1 - 0.328 * np.log(431 * omega_m) * f_b + 0.38 * np.log(22.3 * omega_m) * f_b**2
    gamma_eff = omega_m / h * (alpha_gamma + (1 - alpha_gamma) / (1 + (0.43 * k * s)**4))

    # Prevent division by zero
    gamma_eff = np.maximum(gamma_eff, 1e-20)
    q = k * theta**2 / gamma_eff
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731 / (1 + 62.5 * q)
    T = L / (L + C * q**2)

    return np.squeeze(T), s


def EH_transfer_LCDM(k_hMpc):
    """LCDM transfer function"""
    return EH_transfer(k_hMpc, Omega_m_LCDM * h**2, Omega_b_h2)


def EH_transfer_baryon_only(k_hMpc):
    """
    Baryon-only transfer function with Silk damping and BAO wiggles.
    """
    omega_m = Omega_b_h2  # baryon-only
    omega_b = Omega_b_h2
    T_smooth, s = EH_transfer(k_hMpc, omega_m, omega_b)

    k = np.atleast_1d(k_hMpc).astype(float)

    # BAO wiggles
    ks = k * s
    j0 = np.where(np.abs(ks) < 1e-10, 1.0, np.sin(ks) / ks)

    # Silk damping
    k_silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1 + (10.4 * omega_m)**(-0.95))
    silk = np.exp(-(k / k_silk)**1.4)

    T_bary = T_smooth * (silk * j0 + (1 - silk) * 0.05)

    return np.squeeze(T_bary), T_smooth, s


# =============================================================================
# STEP 1: MOND-MODIFIED TRANSFER FUNCTION (Self-consistent iteration)
# =============================================================================
def compute_y_rec(k_hMpc, delta_rec=3e-4):
    """
    Compute the MOND interpolation parameter y at recombination.
    y = g_N / a_0 where g_N is the Newtonian gravitational acceleration
    from baryon perturbation delta at wavenumber k.

    g_N = 4*pi*G*rho_b(z_rec) * delta / k_phys
    k_phys = k_comoving / a_rec
    """
    k = np.atleast_1d(k_hMpc).astype(float)

    # Physical wavenumber at recombination
    k_com_si = k * h / Mpc_m  # comoving k in m^-1
    k_phys = k_com_si / a_rec  # physical k at recombination

    # Baryon density at recombination
    rho_b_rec = rho_b_0 / a_rec**3

    # Newtonian acceleration from perturbation
    # g_N ~ 4*pi*G*rho_b * delta * (2*pi/k) for a mode of wavenumber k
    # More precisely: g_N = 4*pi*G*rho_b*delta / k (from Poisson equation)
    g_N = 4 * np.pi * G_N * rho_b_rec * delta_rec / k_phys

    y = g_N / a0_MOND

    return np.squeeze(y)


def compute_nu_from_y(y):
    """MOND interpolation function: nu(y) = [1 + sqrt(1 + 4/y)] / 2"""
    y = np.atleast_1d(y).astype(float)
    # For very small y (deep MOND): nu ~ 1/sqrt(y)
    # For large y (Newtonian): nu ~ 1
    nu = 0.5 * (1 + np.sqrt(1 + 4 / np.maximum(y, 1e-50)))
    return np.squeeze(nu)


def compute_MOND_transfer_self_consistent(k_arr, n_iter=50):
    """
    Self-consistent MOND-modified transfer function.

    The idea: MOND enhances gravity at recombination, so the effective
    Omega_m seen by baryons is larger. We iterate:
      1. Compute y(k) from baryon perturbation
      2. Get nu(y) = MOND enhancement
      3. Omega_m_eff(k) = min(nu(k) * Omega_b, Omega_m_LCDM)
      4. Compute T(k) from EH with Omega_m_eff
      5. Update delta(k) = T(k) * delta_primordial and repeat

    From R5 Boltzmann: converges in ~30 iterations.
    """
    k = np.atleast_1d(k_arr).astype(float)
    n_k = len(k)

    # Initial guess: baryon-only transfer function
    T_current, _, s_b = EH_transfer_baryon_only(k)
    T_current_smooth = T_current.copy()

    # Primordial amplitude reference (delta ~ 3e-4 at recombination for k ~ 0.05)
    delta_0 = 3e-4  # representative primordial perturbation at recombination

    # Store convergence history
    nu_history = []

    for iteration in range(n_iter):
        # Current delta at each k (relative to primordial)
        # delta(k) ~ T(k) * delta_0 * (k/k_pivot)^((n_s-1)/2)
        # For self-consistency, we track the ratio T_DFD/T_baryon
        delta_k = T_current * delta_0

        # Compute y(k) at recombination
        y_k = compute_y_rec(k, np.abs(delta_k))

        # MOND interpolation
        nu_k = compute_nu_from_y(y_k)

        # Effective Omega_m: capped at LCDM value
        # (MOND can't create more than the equivalent of CDM)
        Omega_m_eff_k = np.minimum(nu_k * Omega_b, Omega_m_LCDM)

        # Compute transfer function with scale-dependent Omega_m_eff
        T_new = np.zeros(n_k)
        s_new = np.zeros(n_k)
        for i in range(n_k):
            omega_m_eff = Omega_m_eff_k[i] * h**2
            T_new[i], s_new[i] = EH_transfer(k[i:i+1], omega_m_eff, Omega_b_h2)

        # Damping for stability
        alpha = 0.3 if iteration < 10 else 0.5
        T_current = alpha * T_new + (1 - alpha) * T_current

        nu_history.append(nu_k.copy())

    # Final values
    y_final = compute_y_rec(k, np.abs(T_current * delta_0))
    nu_final = compute_nu_from_y(y_final)
    Omega_m_eff_final = np.minimum(nu_final * Omega_b, Omega_m_LCDM)

    # Sound horizon (use median Omega_m_eff for representative value)
    _, s_dfd = EH_transfer(np.array([0.01]),
                           np.median(Omega_m_eff_final) * h**2, Omega_b_h2)

    return T_current, nu_final, Omega_m_eff_final, s_dfd


# =============================================================================
# STEP 2: POST-RECOMBINATION MOND GROWTH
# =============================================================================
def solve_growth_linear(Omega_source, a_start=1e-4, a_end=1.0):
    """Solve linear growth: delta'' + friction*delta' = source*delta"""
    def ode(x, state):
        a = np.exp(x)
        E2 = Omega_m_LCDM / a**3 + Omega_Lambda
        dlnH = -1.5 * Omega_m_LCDM / (a**3 * E2)
        return [state[1],
                -(3 + dlnH) * state[1] + 1.5 * Omega_source / (a**3 * E2) * state[0]]

    sol = solve_ivp(ode, [np.log(a_start), np.log(a_end)],
                    [a_start, 1.0], method='RK45', rtol=1e-10, atol=1e-14,
                    max_step=0.005)
    return sol.y[0][-1] / a_start  # growth factor D normalized to a_start


def solve_MOND_growth_regulated(k_hMpc, sigma_nabla_bg=0.0, a_start=None, a_end=1.0):
    """
    Solve the MOND growth ODE with self-consistent nu and sigma_nabla regulation.

    delta'' + [3/a + dlnH/da] delta' = (3 Omega_b nu_eff) / (2 a^5 E^2) delta

    where nu_eff depends on y = y_mode + y_background
    y_mode = (4*pi*G*rho_b*a^3 * |delta| * 2*pi*a/k) / (3 * a0 * a^2)
           = (4*pi*G*rho_b_0 * |delta| * 2*pi) / (3 * a0 * k_phys * a^2)

    sigma_nabla regulation adds a background y contribution from all modes.
    """
    if a_start is None:
        a_start = a_rec

    k_com = k_hMpc * h / Mpc_m  # comoving k in m^-1

    def ode(x, state):
        a = np.exp(x)
        E2 = Omega_m_LCDM / a**3 + Omega_Lambda
        dlnH = -1.5 * Omega_m_LCDM / (a**3 * E2)
        d, dp = state

        # Newtonian acceleration for this mode
        # g_N = 4*pi*G*rho_b(a) * |delta| / k_phys
        # rho_b(a) = rho_b_0 / a^3, k_phys = k_com / a
        g_N_mode = 4 * np.pi * G_N * rho_b_0 * abs(d) / (k_com * a**2)

        # Background contribution from sigma_nabla
        # sigma_nabla contributes an additional acceleration
        g_bg = sigma_nabla_bg * a0_MOND  # background y -> acceleration

        y_total = (g_N_mode + g_bg) / a0_MOND

        nu = 0.5 * (1 + np.sqrt(1 + 4 / max(y_total, 1e-50)))

        source = 1.5 * Omega_b * nu / (a**3 * E2) * d
        return [dp, -(3 + dlnH) * dp + source]

    # Initial conditions at a_start
    # delta(a_rec) ~ a_rec (growing mode), delta'(a_rec) = 1
    d0 = a_start
    dp0 = 1.0

    sol = solve_ivp(ode, [np.log(a_start), np.log(a_end)],
                    [d0, dp0], method='RK45', rtol=1e-9, atol=1e-14,
                    max_step=0.01)

    D_MOND = sol.y[0][-1] / d0
    return D_MOND


def compute_growth_factors(k_arr, sigma_nabla_bg=0.0):
    """
    Compute growth factors for all k values.
    Returns D_MOND(k) / D_Newton ratio at each k.
    """
    # Reference: Newtonian growth with Omega_b only
    D_Newton = solve_growth_linear(Omega_b, a_start=a_rec)

    # Reference: LCDM growth
    D_LCDM = solve_growth_linear(Omega_m_LCDM, a_start=a_rec)

    D_MOND_arr = np.zeros(len(k_arr))
    for i, k in enumerate(k_arr):
        D_MOND_arr[i] = solve_MOND_growth_regulated(k, sigma_nabla_bg, a_start=a_rec)

    return D_MOND_arr, D_Newton, D_LCDM


# =============================================================================
# STEP 3: MODE COUPLING CORRECTION (Agent 13)
# =============================================================================
def mode_coupling_convolution(k_arr, Pk_arr, beta=None):
    """
    Compute the mode-coupling (self-convolution) term: P_b * P_b.

    P_mc(k) = beta * integral P_b(q) * P_b(|k-q|) d^3q / (2*pi)^3

    For 1D convolution in log-spaced k:
    P_mc(k) = beta / (2*pi^2) * integral q^2 * P_b(q) * P_b(k) dq
             (simplified for isotropic case)

    More precisely, the folding integral:
    P_mc(k) = beta * k / (4*pi^2) * integral_0^inf dq q P_b(q)
              * integral_{|k-q|}^{k+q} dp P_b(p)

    We use the discrete convolution approximation.
    """
    if beta is None:
        # Agent 13: beta = 1/(pi * sigma_b^2)
        # sigma_b^2 = integral k^2 P_b dk / (2*pi^2)
        integrand = k_arr**2 * Pk_arr / (2 * np.pi**2)
        sigma_b_sq = trapezoid(integrand, k_arr)
        if sigma_b_sq > 0:
            beta = 1.0 / (np.pi * sigma_b_sq)
        else:
            beta = 0.0

    # Compute convolution on uniform log-k grid
    n = len(k_arr)
    dk = np.gradient(k_arr)

    # P_mc(k_i) ~ beta * sum_j k_j^2 * P(k_j) * P(k_i) * dk_j / (2*pi^2)
    # This is the leading (factorized) term; the full integral is more complex
    # but this captures the amplitude correctly

    # Actually do the proper 1D convolution:
    # For each k, integrate over q: P(q) * P(|k-q|) * q^2 dq
    # Using interpolation for P(|k-q|)
    log_k = np.log(k_arr)
    P_interp = interp1d(log_k, np.log(np.maximum(Pk_arr, 1e-100)),
                        kind='linear', fill_value=-100, bounds_error=False)

    P_mc = np.zeros(n)
    for i in range(n):
        ki = k_arr[i]
        # Integration over q from k_min to k_max
        q_arr = k_arr
        dq = dk

        # |k - q| -- for each q, compute the relevant k
        k_minus_q = np.abs(ki - q_arr)
        k_minus_q = np.maximum(k_minus_q, k_arr[0])
        k_minus_q = np.minimum(k_minus_q, k_arr[-1])

        P_at_kmq = np.exp(P_interp(np.log(k_minus_q)))

        integrand = q_arr**2 * Pk_arr * P_at_kmq * dq
        P_mc[i] = beta * ki / (4 * np.pi**2) * np.sum(integrand)

    return P_mc, beta


# =============================================================================
# STEP 4: PSI-SCREEN K-REMAPPING
# =============================================================================
def psi_screen_correction(k_arr, Pk_arr, z_survey=0.5):
    """
    Psi-screen k-remapping and volume correction.

    The DFD psi field modifies the metric, causing:
    1. k-space remapping: k_obs = k_true * f_k
       where f_k = exp(Delta_psi(z))
    2. Volume factor: f_V from the modified distance-redshift relation

    From Agent 19 / R5 analysis:
    - f_k ~ 1.12-1.20 at z ~ 0.5-1.0
    - f_V ~ 1.4-1.8

    P_obs(k) = P_true(k / f_k) * f_V
    """
    # Psi-screen parameters (from DFD field equations)
    # Delta_psi depends on z; use analytic estimate
    # For a representative survey at z_survey:
    a_survey = 1.0 / (1 + z_survey)

    # f_k from psi-screen remapping
    # Based on DFD potential: Delta_psi ~ (Omega_b/Omega_Lambda) * (1/a - 1)
    # Calibrated to give f_k ~ 1.15 at z = 0.5
    Delta_psi = 0.14 * (1.0 / a_survey - 1)  # ~0.14 at z=0.5
    f_k = np.exp(Delta_psi)

    # Volume factor: from modified angular diameter distance
    # f_V = (d_A^DFD / d_A^LCDM)^3 ~ (1 + Delta_psi)^3
    # But more conservatively, from R5: f_V ~ 1.5 at z = 0.5
    f_V = (1 + Delta_psi)**2  # ~1.3 at z=0.5 (conservative)

    # Apply remapping
    # P_obs(k) = P_true(k/f_k) * f_V
    log_P = interp1d(np.log(k_arr), np.log(np.maximum(Pk_arr, 1e-100)),
                     kind='linear', fill_value='extrapolate')

    k_remapped = k_arr / f_k
    # Only remap where k_remapped is within bounds
    valid = (k_remapped >= k_arr[0]) & (k_remapped <= k_arr[-1])
    P_obs = np.zeros_like(Pk_arr)
    P_obs[valid] = np.exp(log_P(np.log(k_remapped[valid]))) * f_V
    P_obs[~valid] = Pk_arr[~valid] * f_V  # extrapolate at edges

    return P_obs, f_k, f_V


# =============================================================================
# STEP 5: NONLINEAR 3-LAPLACIAN ANALYSIS
# =============================================================================
def nonlinear_3laplacian_ratio(k_hMpc, delta=3e-4):
    """
    Compare nonlinear 3-Laplacian to linearized QUMOND.

    Linearized QUMOND: psi_lin = nu(y) * psi_N
      where psi_N = (4*pi*G*rho_b*delta) / (k^2 * c^2)

    Nonlinear 3-Laplacian (deep MOND):
      psi_NL ~ sqrt(a_star * |source|) / k
      where source = 4*pi*G*rho_b*delta / c^2

    Ratio: psi_NL / psi_N = sqrt(a_star * source) * k / source
           = sqrt(a_star / source) * k
           = sqrt(a_star * k^2 * c^2 / (4*pi*G*rho_b*delta)) * k / k
           = k * sqrt(a_star * c^2 / (4*pi*G*rho_b*delta))

    This is k-dependent!

    For the ratio psi_NL/psi_N vs nu_lin:
    nu_lin = psi_lin / psi_N is computed from y.
    """
    k = np.atleast_1d(k_hMpc).astype(float)
    k_si = k * h / Mpc_m  # in m^-1

    # Source term at recombination
    rho_b_rec = rho_b_0 / a_rec**3
    source = 4 * np.pi * G_N * rho_b_rec * delta / c_si**2  # m^-2

    # Newtonian potential
    psi_N = source / k_si**2  # dimensionless (actually m^-2 / m^-2 but let's track ratios)

    # Nonlinear 3-Laplacian potential (deep MOND limit)
    psi_NL = np.sqrt(a_star * source) / k_si

    ratio_NL_to_N = psi_NL / psi_N  # = k * sqrt(a_star / source)

    # Linearized QUMOND: nu(y) * psi_N
    g_N_rec = 4 * np.pi * G_N * rho_b_rec * delta / (k_si / a_rec)
    y_rec = g_N_rec / a0_MOND
    nu_lin = compute_nu_from_y(y_rec)

    ratio_lin_to_N = nu_lin

    # Effective enhancement from 3-Laplacian vs linearized
    ratio_NL_to_lin = ratio_NL_to_N / ratio_lin_to_N

    return ratio_NL_to_N, ratio_lin_to_N, ratio_NL_to_lin


# =============================================================================
# STEP 6: GALAXY BIAS
# =============================================================================
def galaxy_bias_DFD(k_arr):
    """
    DFD galaxy bias correction.
    From phantom DM halos: b_DFD ~ 1.2-1.5 * b_LCDM

    In DFD, the MOND-enhanced potential creates phantom mass concentrations
    that enhance galaxy clustering beyond the underlying matter P(k).

    Scale-dependent: stronger at smaller scales.
    """
    # b(k) = b_0 + b_1 * (k/k_pivot)^alpha
    b_0 = 1.3   # baseline bias enhancement
    b_1 = 0.2   # scale-dependent term
    k_pivot = 0.1  # h/Mpc
    alpha = 0.3

    b_k = b_0 + b_1 * (k_arr / k_pivot)**alpha

    return b_k


# =============================================================================
# SIGMA_8 COMPUTATION
# =============================================================================
def compute_sigma8(k_arr, Pk_arr, R=8.0):
    """sigma_8 from P(k)"""
    kR = k_arr * R
    W = np.where(kR < 1e-6, 1.0, 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3)
    integrand = k_arr**2 * Pk_arr * W**2 / (2 * np.pi**2)
    return np.sqrt(trapezoid(integrand, k_arr))


# =============================================================================
# PRIMORDIAL POWER SPECTRUM
# =============================================================================
def P_primordial(k_arr, k_pivot=0.05):
    """P_prim(k) = A_s * (k/k_pivot)^(n_s-1) * (2*pi^2/k^3)"""
    # Actually for matter power spectrum: P(k) = A_s * (k/k_pivot)^(n_s) * T(k)^2 * D^2
    # The k^n_s factor comes from the primordial + Poisson equation
    return A_s * (k_arr / k_pivot)**(n_s - 1)


# =============================================================================
# MAIN CALCULATION
# =============================================================================
def main():
    # k grid
    n_k = 200
    k_arr = np.logspace(np.log10(0.001), np.log10(1.0), n_k)
    k_report = np.array([0.01, 0.02, 0.05, 0.10, 0.15, 0.20])

    results = {}

    # =========================================================================
    # LCDM REFERENCE
    # =========================================================================
    print("\n" + "=" * 60)
    print("LCDM REFERENCE")
    print("=" * 60)

    T_lcdm, s_lcdm = EH_transfer_LCDM(k_arr)
    D_LCDM = solve_growth_linear(Omega_m_LCDM, a_start=a_rec)

    # Unnormalized P(k) = k^n_s * T^2
    Pk_LCDM_unnorm = k_arr**n_s * T_lcdm**2
    sig8_raw = compute_sigma8(k_arr, Pk_LCDM_unnorm)
    norm_LCDM = (0.81 / sig8_raw)**2
    Pk_LCDM = Pk_LCDM_unnorm * norm_LCDM

    sig8_LCDM = compute_sigma8(k_arr, Pk_LCDM)
    print(f"  T_LCDM(0.1) = {np.interp(0.1, k_arr, T_lcdm):.4f}")
    print(f"  Sound horizon s_LCDM = {s_lcdm:.2f} Mpc/h")
    print(f"  D_LCDM(z_rec -> z=0) = {D_LCDM:.2f}")
    print(f"  sigma_8 = {sig8_LCDM:.4f}")
    print(f"  Normalization factor = {norm_LCDM:.4e}")

    results['LCDM'] = {
        'sigma8': sig8_LCDM,
        'Pk': Pk_LCDM.copy(),
        'T': T_lcdm.copy(),
        'D': D_LCDM,
        's': s_lcdm
    }

    # =========================================================================
    # BARYON-ONLY REFERENCE (pure GR, no MOND)
    # =========================================================================
    print("\n" + "=" * 60)
    print("BARYON-ONLY REFERENCE (GR, no MOND)")
    print("=" * 60)

    T_baryon, T_baryon_smooth, s_baryon = EH_transfer_baryon_only(k_arr)
    D_baryon = solve_growth_linear(Omega_b, a_start=a_rec)

    # Same normalization as LCDM (same primordial spectrum)
    Pk_baryon = k_arr**n_s * T_baryon**2 * (D_baryon / D_LCDM)**2 * norm_LCDM
    sig8_baryon = compute_sigma8(k_arr, Pk_baryon)

    print(f"  T_baryon(0.1) = {np.interp(0.1, k_arr, T_baryon):.6f}")
    print(f"  Sound horizon s_baryon = {s_baryon:.2f} Mpc/h")
    print(f"  D_baryon = {D_baryon:.4f}")
    print(f"  D_baryon/D_LCDM = {D_baryon/D_LCDM:.6f}")
    print(f"  sigma_8 = {sig8_baryon:.6f}")

    results['baryon_only'] = {
        'sigma8': sig8_baryon,
        'Pk': Pk_baryon.copy(),
        'T': T_baryon.copy(),
        'D': D_baryon,
        's': s_baryon
    }

    # =========================================================================
    # MECHANISM 1: MOND-MODIFIED TRANSFER FUNCTION ONLY
    # =========================================================================
    print("\n" + "=" * 60)
    print("MECHANISM 1: MOND-Modified Transfer Function")
    print("  (self-consistent nu at recombination, Newtonian growth)")
    print("=" * 60)

    T_mond_tf, nu_rec, Omega_eff_rec, s_mond = compute_MOND_transfer_self_consistent(k_arr)

    # Use Newtonian growth (Omega_b only) -- transfer function is the only enhancement
    Pk_M1 = k_arr**n_s * T_mond_tf**2 * (D_baryon / D_LCDM)**2 * norm_LCDM
    sig8_M1 = compute_sigma8(k_arr, Pk_M1)

    print(f"  nu at k=0.01: {np.interp(0.01, k_arr, nu_rec):.3f}")
    print(f"  nu at k=0.05: {np.interp(0.05, k_arr, nu_rec):.3f}")
    print(f"  nu at k=0.10: {np.interp(0.10, k_arr, nu_rec):.3f}")
    print(f"  nu at k=0.20: {np.interp(0.20, k_arr, nu_rec):.3f}")
    print(f"  Omega_eff at k=0.10: {np.interp(0.10, k_arr, Omega_eff_rec):.4f}")
    print(f"  Sound horizon s_DFD = {s_mond:.2f} Mpc/h")
    print(f"  sigma_8 = {sig8_M1:.6f}")

    results['M1_transfer'] = {
        'sigma8': sig8_M1,
        'Pk': Pk_M1.copy(),
        'T': T_mond_tf.copy(),
        'nu_rec': nu_rec.copy(),
        'Omega_eff': Omega_eff_rec.copy(),
        's': s_mond
    }

    # =========================================================================
    # MECHANISM 1+2: MOND Transfer + MOND Growth
    # =========================================================================
    print("\n" + "=" * 60)
    print("MECHANISMS 1+2: MOND Transfer + MOND Growth")
    print("  (self-consistent transfer + post-recombination MOND growth)")
    print("=" * 60)

    # Compute MOND growth factors at each k
    print("  Computing MOND growth factors (this takes a moment)...")
    D_MOND_arr = np.zeros(n_k)
    for i in range(n_k):
        D_MOND_arr[i] = solve_MOND_growth_regulated(k_arr[i], sigma_nabla_bg=0.0)
    D_MOND_ratio = D_MOND_arr / D_baryon  # ratio to Newtonian baryon growth

    # With sigma_nabla background regulation
    # First compute sigma_nabla from the unregulated solution
    Pk_unreg = k_arr**n_s * T_mond_tf**2 * (D_MOND_arr / D_LCDM)**2 * norm_LCDM
    integrand_sn = k_arr**4 * Pk_unreg / (2 * np.pi**2)  # k^2 * k^2 P(k) for gradient
    sigma_nabla_sq = trapezoid(integrand_sn, k_arr)
    sigma_nabla = np.sqrt(max(sigma_nabla_sq, 0))
    print(f"  sigma_nabla (unregulated) = {sigma_nabla:.4f}")

    # Now recompute with regulation
    # y_bg = sigma_nabla * some_factor (the background gradient field)
    # For regulation: y_bg ~ sigma_nabla / a_star_dimless
    # Keep it as a dimensionless background y contribution
    y_bg = sigma_nabla * 0.1  # regulation strength (tunable)
    print(f"  Computing regulated growth with y_bg = {y_bg:.4f}...")

    D_MOND_reg = np.zeros(n_k)
    for i in range(n_k):
        D_MOND_reg[i] = solve_MOND_growth_regulated(k_arr[i], sigma_nabla_bg=y_bg)
    D_MOND_ratio_reg = D_MOND_reg / D_baryon

    Pk_M12 = k_arr**n_s * T_mond_tf**2 * (D_MOND_arr / D_LCDM)**2 * norm_LCDM
    sig8_M12 = compute_sigma8(k_arr, Pk_M12)

    Pk_M12_reg = k_arr**n_s * T_mond_tf**2 * (D_MOND_reg / D_LCDM)**2 * norm_LCDM
    sig8_M12_reg = compute_sigma8(k_arr, Pk_M12_reg)

    print(f"  D_MOND/D_baryon at k=0.01: {np.interp(0.01, k_arr, D_MOND_ratio):.3f}")
    print(f"  D_MOND/D_baryon at k=0.05: {np.interp(0.05, k_arr, D_MOND_ratio):.3f}")
    print(f"  D_MOND/D_baryon at k=0.10: {np.interp(0.10, k_arr, D_MOND_ratio):.3f}")
    print(f"  D_MOND/D_baryon at k=0.20: {np.interp(0.20, k_arr, D_MOND_ratio):.3f}")
    print(f"  sigma_8 (unregulated) = {sig8_M12:.6f}")
    print(f"  sigma_8 (regulated)   = {sig8_M12_reg:.6f}")

    results['M12_transfer_growth'] = {
        'sigma8': sig8_M12,
        'sigma8_reg': sig8_M12_reg,
        'Pk': Pk_M12.copy(),
        'Pk_reg': Pk_M12_reg.copy(),
        'D_ratio': D_MOND_ratio.copy(),
        'D_ratio_reg': D_MOND_ratio_reg.copy()
    }

    # =========================================================================
    # MECHANISM 1+2+3: Add Mode Coupling
    # =========================================================================
    print("\n" + "=" * 60)
    print("MECHANISMS 1+2+3: + Mode Coupling (Agent 13)")
    print("=" * 60)

    P_mc, beta_mc = mode_coupling_convolution(k_arr, Pk_M12)
    Pk_M123 = Pk_M12 + P_mc
    sig8_M123 = compute_sigma8(k_arr, Pk_M123)

    P_mc_reg, beta_mc_reg = mode_coupling_convolution(k_arr, Pk_M12_reg)
    Pk_M123_reg = Pk_M12_reg + P_mc_reg
    sig8_M123_reg = compute_sigma8(k_arr, Pk_M123_reg)

    print(f"  Mode coupling beta = {beta_mc:.4e}")
    print(f"  P_mc/P_DFD at k=0.10: {np.interp(0.1, k_arr, P_mc)/max(np.interp(0.1, k_arr, Pk_M12), 1e-100):.4f}")
    print(f"  sigma_8 (unreg) = {sig8_M123:.6f}")
    print(f"  sigma_8 (reg)   = {sig8_M123_reg:.6f}")

    results['M123_plus_mc'] = {
        'sigma8': sig8_M123,
        'sigma8_reg': sig8_M123_reg,
        'Pk': Pk_M123.copy(),
        'Pk_reg': Pk_M123_reg.copy(),
        'beta': beta_mc
    }

    # =========================================================================
    # MECHANISM 1+2+3+4: Add Psi-Screen
    # =========================================================================
    print("\n" + "=" * 60)
    print("MECHANISMS 1+2+3+4: + Psi-Screen Remapping")
    print("=" * 60)

    Pk_M1234, f_k, f_V = psi_screen_correction(k_arr, Pk_M123)
    sig8_M1234 = compute_sigma8(k_arr, Pk_M1234)

    Pk_M1234_reg, _, _ = psi_screen_correction(k_arr, Pk_M123_reg)
    sig8_M1234_reg = compute_sigma8(k_arr, Pk_M1234_reg)

    print(f"  f_k = {f_k:.4f} (k-space stretch)")
    print(f"  f_V = {f_V:.4f} (volume factor)")
    print(f"  sigma_8 (unreg) = {sig8_M1234:.6f}")
    print(f"  sigma_8 (reg)   = {sig8_M1234_reg:.6f}")

    results['M1234_plus_psi'] = {
        'sigma8': sig8_M1234,
        'sigma8_reg': sig8_M1234_reg,
        'Pk': Pk_M1234.copy(),
        'Pk_reg': Pk_M1234_reg.copy(),
        'f_k': f_k,
        'f_V': f_V
    }

    # =========================================================================
    # FULL MODEL: All mechanisms + galaxy bias
    # =========================================================================
    print("\n" + "=" * 60)
    print("FULL MODEL: All Mechanisms + Galaxy Bias")
    print("=" * 60)

    b_k = galaxy_bias_DFD(k_arr)
    Pk_full = Pk_M1234 * b_k**2
    sig8_full = compute_sigma8(k_arr, Pk_full)

    Pk_full_reg = Pk_M1234_reg * b_k**2
    sig8_full_reg = compute_sigma8(k_arr, Pk_full_reg)

    print(f"  b(k=0.1) = {np.interp(0.1, k_arr, b_k):.3f}")
    print(f"  b(k=0.2) = {np.interp(0.2, k_arr, b_k):.3f}")
    print(f"  sigma_8 (unreg, with bias) = {sig8_full:.6f}")
    print(f"  sigma_8 (reg, with bias)   = {sig8_full_reg:.6f}")

    results['full_model'] = {
        'sigma8': sig8_full,
        'sigma8_reg': sig8_full_reg,
        'Pk': Pk_full.copy(),
        'Pk_reg': Pk_full_reg.copy(),
        'b_k': b_k.copy()
    }

    # =========================================================================
    # STEP 6: NONLINEAR 3-LAPLACIAN ANALYSIS
    # =========================================================================
    print("\n" + "=" * 60)
    print("NONLINEAR 3-LAPLACIAN vs LINEARIZED QUMOND")
    print("=" * 60)

    ratio_NL, ratio_lin, ratio_NL_to_lin = nonlinear_3laplacian_ratio(k_arr)

    for kk in [0.01, 0.05, 0.10, 0.20]:
        idx = np.argmin(np.abs(k_arr - kk))
        print(f"  k = {kk:.2f}: psi_NL/psi_N = {ratio_NL[idx]:.3e}, "
              f"nu_lin = {ratio_lin[idx]:.3f}, "
              f"NL/lin = {ratio_NL_to_lin[idx]:.3e}")

    results['3laplacian'] = {
        'ratio_NL_to_N': ratio_NL.copy(),
        'ratio_lin_to_N': ratio_lin.copy(),
        'ratio_NL_to_lin': ratio_NL_to_lin.copy()
    }

    # =========================================================================
    # HYPOTHETICAL: Constant nu growth + MOND transfer (best case w/o 3-Lap)
    # =========================================================================
    print("\n" + "=" * 60)
    print("HYPOTHETICAL: Constant-nu Growth (nu=6.4) + MOND Transfer")
    print("  (maximum growth possible from simple MOND enhancement)")
    print("=" * 60)

    D_const_nu = solve_growth_linear(Omega_m_LCDM, a_start=a_rec)
    Pk_hyp_constnu = k_arr**n_s * T_mond_tf**2 * (D_const_nu / D_LCDM)**2 * norm_LCDM
    sig8_hyp = compute_sigma8(k_arr, Pk_hyp_constnu)

    # With psi-screen
    Pk_hyp_psi, _, _ = psi_screen_correction(k_arr, Pk_hyp_constnu)
    sig8_hyp_psi = compute_sigma8(k_arr, Pk_hyp_psi)

    # With psi-screen + bias
    sig8_hyp_full = compute_sigma8(k_arr, Pk_hyp_psi * b_k**2)

    print(f"  D_const_nu/D_LCDM = {D_const_nu/D_LCDM:.4f}")
    print(f"  sigma_8 (MOND transfer + const-nu growth) = {sig8_hyp:.6f}")
    print(f"  sigma_8 (+ psi-screen) = {sig8_hyp_psi:.6f}")
    print(f"  sigma_8 (+ psi-screen + bias) = {sig8_hyp_full:.6f}")

    results['hyp_constnu'] = {
        'sigma8': sig8_hyp,
        'sigma8_psi': sig8_hyp_psi,
        'sigma8_full': sig8_hyp_full,
        'Pk': Pk_hyp_constnu.copy()
    }

    # =========================================================================
    # HYPOTHETICAL: LCDM transfer + MOND growth
    # =========================================================================
    print("\n" + "=" * 60)
    print("HYPOTHETICAL: LCDM Transfer + MOND Growth")
    print("  (what if MOND perfectly reproduced the LCDM transfer function?)")
    print("=" * 60)

    Pk_hyp_lcdm_tf = k_arr**n_s * T_lcdm**2 * (D_MOND_arr / D_LCDM)**2 * norm_LCDM
    sig8_hyp_lcdm = compute_sigma8(k_arr, Pk_hyp_lcdm_tf)

    print(f"  sigma_8 (LCDM transfer + MOND growth) = {sig8_hyp_lcdm:.6f}")

    results['hyp_lcdm_tf'] = {
        'sigma8': sig8_hyp_lcdm,
        'Pk': Pk_hyp_lcdm_tf.copy()
    }

    # =========================================================================
    # SUMMARY TABLE
    # =========================================================================
    print("\n" + "=" * 80)
    print("SUMMARY: sigma_8 FROM EACH COMBINATION OF MECHANISMS")
    print("=" * 80)

    combos = [
        ("LCDM reference", sig8_LCDM),
        ("Baryon-only (GR, no MOND)", sig8_baryon),
        ("M1: MOND transfer only", sig8_M1),
        ("M1+2: MOND transfer + MOND growth", sig8_M12),
        ("M1+2 (regulated)", sig8_M12_reg),
        ("M1+2+3: + mode coupling", sig8_M123),
        ("M1+2+3 (regulated)", sig8_M123_reg),
        ("M1+2+3+4: + psi-screen", sig8_M1234),
        ("M1+2+3+4 (regulated)", sig8_M1234_reg),
        ("Full: + galaxy bias", sig8_full),
        ("Full (regulated)", sig8_full_reg),
        ("Hyp: const-nu growth + MOND TF", sig8_hyp),
        ("Hyp: const-nu + psi + bias", sig8_hyp_full),
        ("Hyp: LCDM TF + MOND growth", sig8_hyp_lcdm),
    ]

    print(f"\n  {'Model':<45} {'sigma_8':>10} {'sigma_8/0.81':>12} {'Gap':>8}")
    print("  " + "-" * 75)
    for name, sig in combos:
        gap = sig - 0.81
        print(f"  {name:<45} {sig:10.6f} {sig/0.81:12.4f} {gap:+8.4f}")

    # =========================================================================
    # P_DFD / P_LCDM RATIO TABLE
    # =========================================================================
    print("\n" + "=" * 80)
    print("P_DFD(k) / P_LCDM(k) AT KEY WAVENUMBERS")
    print("=" * 80)

    models_to_report = [
        ("Baryon-only", results['baryon_only']['Pk']),
        ("M1: MOND TF", results['M1_transfer']['Pk']),
        ("M1+2: +growth", results['M12_transfer_growth']['Pk']),
        ("M1+2+3: +MC", results['M123_plus_mc']['Pk']),
        ("M1+2+3+4: +psi", results['M1234_plus_psi']['Pk']),
        ("Full", results['full_model']['Pk']),
        ("Hyp: const-nu", results['hyp_constnu']['Pk']),
    ]

    header = f"  {'Model':<20}"
    for kk in k_report:
        header += f" {'k='+str(kk):>10}"
    print(header)
    print("  " + "-" * (20 + 11 * len(k_report)))

    for name, pk in models_to_report:
        row = f"  {name:<20}"
        for kk in k_report:
            ratio = np.interp(kk, k_arr, pk) / np.interp(kk, k_arr, Pk_LCDM)
            row += f" {ratio:10.4e}"
        print(row)

    # =========================================================================
    # BAO ANALYSIS
    # =========================================================================
    print("\n" + "=" * 80)
    print("BAO PEAK POSITIONS")
    print("=" * 80)
    print(f"  LCDM sound horizon: s = {s_lcdm:.2f} Mpc/h")
    print(f"  Baryon-only sound horizon: s = {s_baryon:.2f} Mpc/h")
    print(f"  DFD (MOND TF) sound horizon: s ~ {s_mond:.2f} Mpc/h")
    print(f"  BAO peak: k_BAO ~ pi/s")
    print(f"    LCDM: k_BAO ~ {np.pi/s_lcdm:.4f} h/Mpc")
    print(f"    Baryon: k_BAO ~ {np.pi/s_baryon:.4f} h/Mpc")
    print(f"    DFD: k_BAO ~ {np.pi/s_mond:.4f} h/Mpc")

    # =========================================================================
    # DEFICIT ANALYSIS
    # =========================================================================
    print("\n" + "=" * 80)
    print("DEFICIT ANALYSIS: WHAT'S NEEDED TO REACH sigma_8 = 0.81")
    print("=" * 80)

    best_sig = sig8_full
    if best_sig > 0:
        needed_boost = (0.81 / best_sig)**2
        print(f"\n  Best physical model sigma_8 = {best_sig:.6f}")
        print(f"  Need P(k) boost of {needed_boost:.2f}x uniformly to reach 0.81")
        print(f"  Need amplitude boost of {np.sqrt(needed_boost):.2f}x")
    else:
        print(f"  Best sigma_8 = {best_sig:.6f} -- effectively zero")

    # Decompose the deficit
    print("\n  Deficit decomposition (at k = 0.1 h/Mpc):")
    T_lcdm_01 = np.interp(0.1, k_arr, T_lcdm)
    T_dfd_01 = np.interp(0.1, k_arr, T_mond_tf)
    D_MOND_01 = np.interp(0.1, k_arr, D_MOND_arr)

    print(f"    Transfer function: (T_DFD/T_LCDM)^2 = {(T_dfd_01/T_lcdm_01)**2:.6f}")
    print(f"    Growth: (D_MOND/D_LCDM)^2 = {(D_MOND_01/D_LCDM)**2:.6f}")
    print(f"    Combined: {(T_dfd_01/T_lcdm_01)**2 * (D_MOND_01/D_LCDM)**2:.6f}")
    print(f"    Mode coupling boost: {np.interp(0.1, k_arr, Pk_M123)/max(np.interp(0.1, k_arr, Pk_M12), 1e-100):.4f}")
    print(f"    Psi-screen boost: {f_V:.4f}")
    print(f"    Bias boost: {np.interp(0.1, k_arr, b_k)**2:.4f}")

    # =========================================================================
    # 3-LAPLACIAN ENHANCED MODEL
    # =========================================================================
    print("\n" + "=" * 60)
    print("3-LAPLACIAN ENHANCED SCENARIO")
    print("  If nonlinear 3-Laplacian gives additional enhancement")
    print("=" * 60)

    # The 3-Laplacian analysis shows the ratio depends on k and delta.
    # For the deep MOND regime at recombination:
    # psi_NL/psi_N is MUCH larger than nu_lin at high k but smaller at low k.
    # At k = 0.1: ratio_NL_to_lin tells us the relative enhancement.

    # If 3-Laplacian dominates, the effective nu would be:
    # nu_3L(k) = psi_NL(k) / psi_N(k) instead of nu_lin
    nu_3L = ratio_NL.copy()
    nu_3L = np.minimum(nu_3L, 1000)  # cap at reasonable value

    # Recompute transfer function with 3-Laplacian nu
    Omega_eff_3L = np.minimum(nu_3L * Omega_b, Omega_m_LCDM)
    T_3L = np.zeros(n_k)
    for i in range(n_k):
        omega_m_eff = max(Omega_eff_3L[i] * h**2, Omega_b_h2)
        T_3L[i], _ = EH_transfer(k_arr[i:i+1], omega_m_eff, Omega_b_h2)

    Pk_3L = k_arr**n_s * T_3L**2 * norm_LCDM  # with LCDM-equivalent growth
    sig8_3L = compute_sigma8(k_arr, Pk_3L)

    # With all mechanisms
    Pk_3L_full, _, _ = psi_screen_correction(k_arr, Pk_3L)
    Pk_3L_full *= b_k**2
    sig8_3L_full = compute_sigma8(k_arr, Pk_3L_full)

    print(f"  nu_3L at k=0.01: {np.interp(0.01, k_arr, nu_3L):.3e}")
    print(f"  nu_3L at k=0.05: {np.interp(0.05, k_arr, nu_3L):.3e}")
    print(f"  nu_3L at k=0.10: {np.interp(0.10, k_arr, nu_3L):.3e}")
    print(f"  nu_3L at k=0.20: {np.interp(0.20, k_arr, nu_3L):.3e}")
    print(f"  Omega_eff_3L at k=0.10: {np.interp(0.10, k_arr, Omega_eff_3L):.4f}")
    print(f"  sigma_8 (3-Laplacian TF only) = {sig8_3L:.6f}")
    print(f"  sigma_8 (3-Laplacian + all mechanisms) = {sig8_3L_full:.6f}")

    results['3laplacian_model'] = {
        'sigma8': sig8_3L,
        'sigma8_full': sig8_3L_full,
        'nu_3L': nu_3L.copy(),
        'T': T_3L.copy(),
        'Pk': Pk_3L.copy()
    }

    # =========================================================================
    # WHAT NU_EFF PROFILE IS NEEDED?
    # =========================================================================
    print("\n" + "=" * 60)
    print("REQUIRED NU_EFF PROFILE FOR sigma_8 = 0.81")
    print("=" * 60)

    # For P_DFD = P_LCDM at each k:
    # T_DFD(k)^2 * D_DFD^2 = T_LCDM(k)^2 * D_LCDM^2
    # If D_DFD = D_LCDM (constant nu growth):
    # T_DFD(k) = T_LCDM(k) => Omega_m_eff(k) = Omega_m_LCDM
    # nu_needed(k) = Omega_m_LCDM / Omega_b = 6.4

    # But if D_DFD != D_LCDM, we need T_DFD to compensate.
    # With MOND growth D_MOND(k), we need:
    # T_needed(k) = T_LCDM(k) * D_LCDM / D_MOND(k)

    # First, with constant-nu growth (D=D_LCDM):
    print("\n  With constant-nu growth (D_DFD = D_LCDM):")
    print(f"    Need Omega_m_eff = {Omega_m_LCDM:.4f} at all k")
    print(f"    Need nu_eff = {nu_needed:.3f} at all k")
    print(f"    This is the 'CDM-equivalent' MOND enhancement")

    # With MOND growth:
    print("\n  With self-consistent MOND growth D_MOND(k):")
    for kk in k_report:
        D_M = np.interp(kk, k_arr, D_MOND_arr)
        T_L = np.interp(kk, k_arr, T_lcdm)
        T_D = np.interp(kk, k_arr, T_mond_tf)
        T_needed = T_L * D_LCDM / max(D_M, 1e-10)
        # What Omega_m_eff gives this T?
        # T_EH depends on Omega_m_eff in a complex way
        # Approximate: T ~ 1/(1 + (k/k_eq)^2) where k_eq ~ Omega_m_eff
        ratio = T_needed / max(T_D, 1e-10)
        print(f"    k={kk:.2f}: T_needed/T_MOND = {ratio:.2e}, "
              f"D_MOND/D_LCDM = {D_M/D_LCDM:.4f}")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    print(f"""
  TARGET: sigma_8 = 0.81 (Planck 2018)

  LCDM reference: sigma_8 = {sig8_LCDM:.4f}

  DFD results by mechanism combination:
    Baryon-only (no MOND):          sigma_8 = {sig8_baryon:.6f}  ({sig8_baryon/0.81:.4e} of target)
    MOND transfer function only:    sigma_8 = {sig8_M1:.6f}  ({sig8_M1/0.81:.4e} of target)
    + MOND growth:                  sigma_8 = {sig8_M12:.6f}  ({sig8_M12/0.81:.4e} of target)
    + Mode coupling:                sigma_8 = {sig8_M123:.6f}  ({sig8_M123/0.81:.4e} of target)
    + Psi-screen:                   sigma_8 = {sig8_M1234:.6f}  ({sig8_M1234/0.81:.4e} of target)
    + Galaxy bias (FULL):           sigma_8 = {sig8_full:.6f}  ({sig8_full/0.81:.4e} of target)

  Hypothetical best cases:
    Const-nu + MOND TF + all:       sigma_8 = {sig8_hyp_full:.6f}  ({sig8_hyp_full/0.81:.4e} of target)
    LCDM TF + MOND growth:          sigma_8 = {sig8_hyp_lcdm:.6f}  ({sig8_hyp_lcdm/0.81:.4e} of target)
    3-Laplacian + all:               sigma_8 = {sig8_3L_full:.6f}  ({sig8_3L_full/0.81:.4e} of target)

  REMAINING GAP:
    Best physical: sigma_8 = {sig8_full:.6f}
    Target:        sigma_8 = 0.8100
    Gap:           {0.81 - sig8_full:+.6f} (factor {0.81/max(sig8_full,1e-10):.1f}x in sigma_8, {(0.81/max(sig8_full,1e-10))**2:.0f}x in P(k))
""")

    # =========================================================================
    # Return all results for report generation
    # =========================================================================
    return results, k_arr, k_report, Pk_LCDM


# =============================================================================
# RUN
# =============================================================================
if __name__ == '__main__':
    results, k_arr, k_report, Pk_LCDM = main()

    # Save a machine-readable summary
    print("\n\n" + "=" * 80)
    print("COMPUTATION COMPLETE")
    print("=" * 80)
