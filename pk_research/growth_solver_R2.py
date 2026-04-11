#!/usr/bin/env python3
"""
Round 2 Agent: Self-consistent nonlinear growth equation solver for DFD.

Solves three models:
  Model 1: Pure p-Laplacian (unregulated MOND gravity)
  Model 2: Partially regulated (EFE interpolation with parameter alpha)
  Model 3: Self-consistent with temporal damping term

Computes D(k), P_DFD(k), sigma_8 for each model.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# Physical constants (SI)
# =============================================================================
G_N = 6.674e-11          # m^3 kg^-1 s^-2
c_light = 2.998e8        # m/s
a0_MOND = 1.2e-10        # m/s^2
H0_SI = 2.18e-18         # s^-1  (67.4 km/s/Mpc)
H0_km = 67.4             # km/s/Mpc
Mpc_m = 3.0857e22        # meters per Mpc

Omega_b = 0.049
Omega_Lambda = 0.685
Omega_m = 0.315           # for LCDM comparison
Omega_r = 9.15e-5         # radiation (approx)

rho_crit = 3.0 * H0_SI**2 / (8.0 * np.pi * G_N)  # kg/m^3
rho_b0 = Omega_b * rho_crit  # baryon density today

z_rec = 1100
a_rec = 1.0 / (1.0 + z_rec)

# Primordial spectrum parameters (Planck 2018)
A_s = 2.1e-9
n_s = 0.965

# k values in h/Mpc
k_values_hMpc = np.array([0.01, 0.02, 0.05, 0.10, 0.15, 0.20])
# Convert to 1/Mpc (physical)
h = H0_km / 100.0
k_values_Mpc = k_values_hMpc * h  # 1/Mpc
k_values_SI = k_values_Mpc / Mpc_m  # 1/m

print("=" * 80)
print("ROUND 2: Self-Consistent Nonlinear Growth Equation Solver")
print("=" * 80)

# =============================================================================
# Hubble function for baryon-only + Lambda cosmology
# =============================================================================
def H_DFD(a):
    """Hubble rate in DFD: baryons + radiation + Lambda, NO CDM."""
    return H0_SI * np.sqrt(Omega_r / a**4 + Omega_b / a**3 + Omega_Lambda)

def H_LCDM(a):
    """Hubble rate in LCDM: matter + radiation + Lambda."""
    return H0_SI * np.sqrt(Omega_r / a**4 + Omega_m / a**3 + Omega_Lambda)

# =============================================================================
# Baryon transfer function (Eisenstein & Hu 1998 zero-baryon approx + BAO)
# =============================================================================
def baryon_transfer_function(k_hMpc):
    """
    Approximate baryon transfer function T_b(k).
    Uses a simplified Silk damping + BAO model.
    k in h/Mpc.
    """
    # Silk damping scale
    k_silk = 1.6 * (Omega_b * h**2)**0.52 * (Omega_m * h**2)**0.73 * \
             (1.0 + (10.4 * Omega_m * h**2)**(-0.95))  # h/Mpc

    # Sound horizon at recombination
    z_eq = 2.5e4 * Omega_m * h**2  # matter-radiation equality
    R_eq = 31500.0 * Omega_b * h**2 * (2.7255 / 2.7255)**(-4) / (z_eq + 1)  # baryon-photon ratio at eq

    # Simplified baryon transfer
    q = k_hMpc / (13.41 * (Omega_m * h**2))

    # Silk damping envelope
    T_silk = np.exp(-(k_hMpc / k_silk)**1.4)

    # BAO oscillation (simplified)
    s = 147.0  # Mpc, sound horizon ~ 147 Mpc
    s_hMpc = s * h
    j0 = np.sinc(k_hMpc * s_hMpc / np.pi)  # sinc = sin(x)/x

    # Combined: damped oscillation envelope
    T_b = T_silk * (j0**2 + (1 - j0**2) * np.exp(-0.5 * (k_hMpc / 0.1)**2))

    # Normalize to ~1 at low k
    T_b = np.clip(T_b, 1e-6, 1.0)

    return T_b

# =============================================================================
# LCDM growth factor (for comparison)
# =============================================================================
def solve_LCDM_growth():
    """Solve linear LCDM growth: D'' + 2H D' = (3/2)H^2 Omega_m D / a^3"""

    def deriv(lna, y):
        a = np.exp(lna)
        H = H_LCDM(a)
        dH_dlna = -0.5 * H0_SI**2 * (4*Omega_r/a**4 + 3*Omega_m/a**3) / (2*H)

        D, dD_dlna = y
        # Growth equation in terms of ln(a)
        # D'' + (2 + H'/H) D' = (3/2) Omega_m H0^2 / (a^3 H^2) D
        coeff = 2.0 + dH_dlna / H
        source = 1.5 * Omega_m * H0_SI**2 / (a**3 * H**2)

        dD2_dlna2 = -coeff * dD_dlna + source * D
        return [dD_dlna, dD2_dlna2]

    lna_rec = np.log(a_rec)
    lna_span = [lna_rec, 0.0]
    lna_eval = np.linspace(lna_rec, 0.0, 5000)

    y0 = [a_rec, a_rec]  # growing mode: D ~ a in matter domination

    sol = solve_ivp(deriv, lna_span, y0, t_eval=lna_eval, method='RK45',
                    rtol=1e-10, atol=1e-14)

    D_final = sol.y[0, -1]
    D_rec = sol.y[0, 0]

    return D_final / D_rec, sol

D_LCDM_ratio, sol_LCDM = solve_LCDM_growth()
print(f"\nLCDM growth factor D(z=0)/D(z_rec) = {D_LCDM_ratio:.4f}")

# =============================================================================
# Initial conditions
# =============================================================================
def delta_initial(k_hMpc):
    """Initial density perturbation at recombination."""
    T_b = baryon_transfer_function(k_hMpc)
    # Primordial power: P ~ A_s * (k/k_pivot)^(n_s - 1)
    k_pivot = 0.05  # h/Mpc (Planck pivot)
    P_prim = A_s * (k_hMpc / k_pivot)**(n_s - 1)

    # delta ~ sqrt(P_prim) * T_b * D_rec
    # In matter domination, D(z_rec) ~ a_rec ~ 1/1101
    delta_0 = np.sqrt(P_prim) * T_b * a_rec
    return delta_0

# =============================================================================
# MOND interpolation function
# =============================================================================
def nu_MOND(y):
    """Standard MOND interpolation: nu(y) = [1 + sqrt(1 + 4/y)] / 2"""
    if y <= 0:
        return 1e6  # deep MOND limit
    return 0.5 * (1.0 + np.sqrt(1.0 + 4.0 / y))

# =============================================================================
# MODEL 1: Pure p-Laplacian (deep MOND, unregulated)
# =============================================================================
def solve_model1(k_hMpc, k_SI):
    """
    delta'' + 2H delta' = A_0 * (a/a0_ref)^{-3/2} * delta^{1/2} * k^{1/2}

    In EdS deep MOND: the gravitational acceleration in MOND regime is
    g_MOND = sqrt(g_N * a0) = sqrt(4*pi*G*rho_b*delta * (2*pi*a/k)^{-1} * a0)

    The source term: (4*pi*G*rho_b0/a^3) * delta * nu(y)
    In deep MOND (y<<1): nu ~ sqrt(1/y) so source ~ sqrt(4*pi*G*rho_b0 * a0 / a^3) * sqrt(delta) * sqrt(k/(2*pi*a))

    Let's be more careful with the p-Laplacian source:
    Source = (3/2) H0^2 Omega_b / a^3 * delta * nu(y)
    In deep MOND: nu ~ (a0 / g_N)^{1/2} where g_N = (4*pi*G*rho_b*delta)/(k/a) * something

    Simplification: use the scaling A * a^{-9/4} * delta^{1/2} * k^{1/2}
    from the p-Laplacian analysis (Agent 8/11).
    """

    # Physical source coefficient
    # From deep MOND: g_eff = sqrt(g_N * a0)
    # g_N = (4*pi*G * rho_b0/a^3 * delta) * (2*pi*a/k)  [Newtonian potential gradient / k]
    # Actually: nabla^2 Phi_N = 4*pi*G*rho_b*delta, so k^2 Phi_N = 4*pi*G*rho_b*delta
    # g_N = k * Phi_N / a = 4*pi*G*rho_b*delta / (k*a)... no.
    #
    # More carefully: Poisson in comoving coords
    # k^2 Phi = -4*pi*G*rho_b0*delta/a  (comoving Poisson)
    # The acceleration per unit mass: -k Phi / a = 4*pi*G*rho_b0*delta*a / (k*a^2)
    #   wait, let's use the standard:
    #   delta'' + 2H delta' = 4*pi*G*rho_b*delta (Newtonian, in proper time)
    #
    # In MOND deep regime, replace 4*pi*G*rho_b*delta with:
    #   sqrt(4*pi*G*rho_b*delta * a0 * k / a)  (from p-Laplacian)
    # Actually the p-Laplacian gives:
    #   div(|grad Phi|^{-1/2} grad Phi) = 4*pi*G*rho (in MOND)
    #   => k^{3/2} |Phi|^{1/2} ~ 4*pi*G*rho_b*delta
    #   => Phi ~ (4*pi*G*rho_b*delta)^2 / k^3
    #   force = k*Phi = (4*pi*G*rho_b*delta)^2 / k^2
    #   Hmm, this doesn't match the sqrt form.
    #
    # Let me use the Agent 11 result directly:
    # delta'' + 2H delta' = C * (G * rho_b * a0)^{1/2} * delta^{1/2} * (k/a)^{1/2}
    # where C is an O(1) numerical factor.

    C_pLap = np.sqrt(4.0 * np.pi)  # geometric factor ~ sqrt(4*pi)

    def deriv(lna, y):
        a = np.exp(lna)
        H = H_DFD(a)
        dH_dlna_over_H = -0.5 * (4*Omega_r/a**4 + 3*Omega_b/a**3) * H0_SI**2 / (H**2)

        delta, ddelta_dlna = y

        if delta <= 0:
            delta = 1e-30

        rho_b = rho_b0 / a**3

        # Source: sqrt(G * rho_b * a0) * sqrt(delta) * sqrt(k_SI / a)
        source_coeff = C_pLap * np.sqrt(G_N * rho_b * a0_MOND) * np.sqrt(max(delta, 1e-30)) * np.sqrt(k_SI / a)

        # Convert to ln(a) derivatives:
        # delta'' (cosmic time) = H^2 [d^2 delta/d(lna)^2 + dH/dlna/H * d delta/dlna]
        # So: H^2 d^2delta/dlna^2 + H^2(2 + dH/dlna/H) ddelta/dlna = source_coeff * delta
        # Wait, source is acceleration not force*delta. Let me redo.
        #
        # Equation in cosmic time: d^2 delta/dt^2 + 2H d delta/dt = S
        # where S = source_coeff (which already accounts for delta dependence)
        #
        # In ln(a): H^2 d^2 delta/dlna^2 + H^2(2 + dlnH/dlna) ddelta/dlna = S

        # Actually S here has units of 1/s^2 * delta^{1/2}
        # Let me get the units right
        # [G rho_b a0]^{1/2} = [m^3 kg^-1 s^-2 * kg/m^3 * m/s^2]^{1/2} = [s^-4 * m / m]^{1/2}...
        # [G rho_b] = s^-2, [a0] = m/s^2, [G rho_b a0] = m s^-4, sqrt = m^{1/2} s^{-2}
        # [k_SI/a] = m^{-1}, sqrt = m^{-1/2}
        # product: s^{-2} * delta^{1/2}  -- good, this is an acceleration term with right units

        S = source_coeff  # units of s^{-2} when multiplied by delta factors correctly

        ddelta2_dlna2 = -(2.0 + dH_dlna_over_H) * ddelta_dlna + S / H**2

        return [ddelta_dlna, ddelta2_dlna2]

    delta_0 = delta_initial(k_hMpc)
    ddelta_dlna_0 = delta_0  # growing mode: d delta/d lna = delta (delta ~ a)

    lna_rec = np.log(a_rec)
    lna_eval = np.linspace(lna_rec, 0.0, 10000)

    try:
        sol = solve_ivp(deriv, [lna_rec, 0.0], [delta_0, ddelta_dlna_0],
                        t_eval=lna_eval, method='RK45', rtol=1e-8, atol=1e-15,
                        max_step=0.01)

        if sol.success:
            D_ratio = sol.y[0, -1] / sol.y[0, 0]
            return D_ratio, sol.y[0, -1], sol
        else:
            return np.nan, np.nan, None
    except Exception as e:
        print(f"  Model 1 failed for k={k_hMpc}: {e}")
        return np.nan, np.nan, None


# =============================================================================
# MODEL 2: Partially regulated (EFE interpolation)
# =============================================================================
def solve_model2(k_hMpc, k_SI, alpha):
    """
    delta'' + 2H delta' = (3/2) H^2 Omega_b * nu_eff(y) * delta / a^3

    y = (4*pi*G*rho_b(a)/3) * delta * (2*pi*a/k_SI) / a0
    nu_eff = alpha * nu_MOND(y) + (1-alpha)
    """

    def deriv(lna, state):
        a = np.exp(lna)
        H = H_DFD(a)
        dH_dlna_over_H = -0.5 * (4*Omega_r/a**4 + 3*Omega_b/a**3) * H0_SI**2 / (H**2)

        delta, ddelta_dlna = state

        if delta <= 0:
            delta = 1e-30

        rho_b = rho_b0 / a**3

        # Compute y = internal acceleration / a0
        # g_internal = (4*pi*G/3) * rho_b * delta * lambda_phys
        # lambda_phys = 2*pi*a / k_SI (physical wavelength)
        g_internal = (4.0 * np.pi * G_N / 3.0) * rho_b * abs(delta) * (2.0 * np.pi * a / k_SI)
        y = g_internal / a0_MOND

        nu_M = nu_MOND(y)
        nu_eff = alpha * nu_M + (1.0 - alpha)

        # Source term: (3/2) * (H0^2 * Omega_b / a^3) * nu_eff * delta
        # In ln(a) coords: source/H^2
        source_over_H2 = 1.5 * H0_SI**2 * Omega_b / (a**3 * H**2) * nu_eff * delta

        ddelta2_dlna2 = -(2.0 + dH_dlna_over_H) * ddelta_dlna + source_over_H2

        return [ddelta_dlna, ddelta2_dlna2]

    delta_0 = delta_initial(k_hMpc)
    ddelta_dlna_0 = delta_0

    lna_rec = np.log(a_rec)
    lna_eval = np.linspace(lna_rec, 0.0, 10000)

    try:
        sol = solve_ivp(deriv, [lna_rec, 0.0], [delta_0, ddelta_dlna_0],
                        t_eval=lna_eval, method='RK45', rtol=1e-8, atol=1e-15,
                        max_step=0.01)

        if sol.success:
            D_ratio = sol.y[0, -1] / sol.y[0, 0]
            return D_ratio, sol.y[0, -1], sol
        else:
            return np.nan, np.nan, None
    except Exception as e:
        print(f"  Model 2 (alpha={alpha}) failed for k={k_hMpc}: {e}")
        return np.nan, np.nan, None


# =============================================================================
# MODEL 3: Self-consistent with temporal damping
# =============================================================================
def solve_model3(k_hMpc, k_SI, omega_t_factor):
    """
    delta'' + 2H delta' + omega_t^2 delta = (3/2) H^2 Omega_b * nu_MOND(y) * delta / a^3

    The temporal sector contributes a mass-like term omega_t^2 that prevents runaway.
    omega_t^2 ~ (a0 / c) * H * factor  from the temporal K function.

    We parameterize: omega_t^2 = omega_t_factor * a0 * H / c
    """

    def deriv(lna, state):
        a = np.exp(lna)
        H = H_DFD(a)
        dH_dlna_over_H = -0.5 * (4*Omega_r/a**4 + 3*Omega_b/a**3) * H0_SI**2 / (H**2)

        delta, ddelta_dlna = state

        if delta <= 0:
            delta = 1e-30

        rho_b = rho_b0 / a**3

        # Compute y
        g_internal = (4.0 * np.pi * G_N / 3.0) * rho_b * abs(delta) * (2.0 * np.pi * a / k_SI)
        y = g_internal / a0_MOND

        nu_M = nu_MOND(y)

        # Source term
        source_over_H2 = 1.5 * H0_SI**2 * Omega_b / (a**3 * H**2) * nu_M * delta

        # Temporal damping: omega_t^2 / H^2 * delta
        # omega_t^2 = factor * a0 * H / c  (units: s^-2 since a0/c = s^-1, H = s^-1)
        omega_t2 = omega_t_factor * a0_MOND * H / c_light
        damping = omega_t2 / H**2 * delta

        ddelta2_dlna2 = -(2.0 + dH_dlna_over_H) * ddelta_dlna + source_over_H2 - damping

        return [ddelta_dlna, ddelta2_dlna2]

    delta_0 = delta_initial(k_hMpc)
    ddelta_dlna_0 = delta_0

    lna_rec = np.log(a_rec)
    lna_eval = np.linspace(lna_rec, 0.0, 10000)

    try:
        sol = solve_ivp(deriv, [lna_rec, 0.0], [delta_0, ddelta_dlna_0],
                        t_eval=lna_eval, method='RK45', rtol=1e-8, atol=1e-15,
                        max_step=0.01)

        if sol.success:
            D_ratio = sol.y[0, -1] / sol.y[0, 0]
            return D_ratio, sol.y[0, -1], sol
        else:
            return np.nan, np.nan, None
    except Exception as e:
        print(f"  Model 3 (omega_t_factor={omega_t_factor}) failed for k={k_hMpc}: {e}")
        return np.nan, np.nan, None


# =============================================================================
# Compute sigma_8
# =============================================================================
def compute_sigma8(k_array_hMpc, Pk_array):
    """
    sigma_8 = sqrt( 1/(2*pi^2) * int dk k^2 P(k) W^2(k*R8) )
    where W(x) = 3(sin(x) - x*cos(x))/x^3, R8 = 8 h^{-1} Mpc
    """
    R8 = 8.0  # h^{-1} Mpc

    # Need dense k grid for integration
    # Interpolate P(k) in log space
    if len(k_array_hMpc) < 3:
        return np.nan

    log_k = np.log(k_array_hMpc)
    log_P = np.log(np.maximum(Pk_array, 1e-30))

    # Extrapolate to broader range for proper sigma_8
    k_dense = np.logspace(np.log10(0.001), np.log10(1.0), 1000)

    # Use power law extrapolation outside range
    slope_low = (log_P[1] - log_P[0]) / (log_k[1] - log_k[0])
    slope_high = (log_P[-1] - log_P[-2]) / (log_k[-1] - log_k[-2])

    P_dense = np.zeros_like(k_dense)
    for i, kk in enumerate(k_dense):
        lk = np.log(kk)
        if lk <= log_k[0]:
            P_dense[i] = np.exp(log_P[0] + slope_low * (lk - log_k[0]))
        elif lk >= log_k[-1]:
            P_dense[i] = np.exp(log_P[-1] + slope_high * (lk - log_k[-1]))
        else:
            P_dense[i] = np.exp(np.interp(lk, log_k, log_P))

    def W_tophat(x):
        """Top-hat window function."""
        result = np.where(x < 1e-6, 1.0, 3.0 * (np.sin(x) - x * np.cos(x)) / x**3)
        return result

    x = k_dense * R8
    W = W_tophat(x)

    integrand = k_dense**2 * P_dense * W**2 / (2.0 * np.pi**2)
    sigma8_sq = np.trapz(integrand, k_dense)

    return np.sqrt(max(sigma8_sq, 0))


# =============================================================================
# LCDM P(k) for comparison (simple model)
# =============================================================================
def Pk_LCDM(k_hMpc):
    """LCDM power spectrum (approximate)."""
    # Use Eisenstein & Hu full transfer function approximation
    T_b = baryon_transfer_function(k_hMpc)
    # For LCDM, use full matter transfer function (not just baryons)
    # Approximate: T_m ~ T_b / Omega_b * Omega_m for CDM-dominated
    # Actually use a proper CDM+baryon transfer function

    Gamma = Omega_m * h * np.exp(-Omega_b * (1.0 + np.sqrt(2*h) / Omega_m))
    q = k_hMpc / Gamma
    T_CDM = np.log(1 + 2.34*q) / (2.34*q) * \
            (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)

    # Primordial
    k_pivot = 0.05
    P_prim = A_s * (k_hMpc / k_pivot)**(n_s - 1)

    # LCDM power spectrum (normalized)
    P = P_prim * T_CDM**2 * D_LCDM_ratio**2 * (k_hMpc / k_pivot)

    return P

# =============================================================================
# Run all models
# =============================================================================
print("\n" + "=" * 80)
print("MODEL 1: Pure p-Laplacian (unregulated deep MOND)")
print("=" * 80)

D_model1 = []
delta_final_m1 = []
for i, (k_h, k_si) in enumerate(zip(k_values_hMpc, k_values_SI)):
    D, df, sol = solve_model1(k_h, k_si)
    D_model1.append(D)
    delta_final_m1.append(df)
    d0 = delta_initial(k_h)
    print(f"  k = {k_h:.2f} h/Mpc: delta_i = {d0:.3e}, delta_f = {df:.3e}, "
          f"D = {D:.4e}")

D_model1 = np.array(D_model1)

# Power spectrum for Model 1
T_b_arr = np.array([baryon_transfer_function(k) for k in k_values_hMpc])
k_pivot = 0.05
P_prim_arr = A_s * (k_values_hMpc / k_pivot)**(n_s - 1)
Pk_model1 = P_prim_arr * T_b_arr**2 * D_model1**2 * k_values_hMpc
sigma8_m1 = compute_sigma8(k_values_hMpc, Pk_model1)
print(f"\n  sigma_8 (Model 1) = {sigma8_m1:.4f}")

# LCDM comparison
Pk_LCDM_arr = np.array([Pk_LCDM(k) for k in k_values_hMpc])
sigma8_LCDM = compute_sigma8(k_values_hMpc, Pk_LCDM_arr)
print(f"  sigma_8 (LCDM) = {sigma8_LCDM:.4f}")

print(f"\n  P_DFD / P_LCDM ratios:")
for i, k_h in enumerate(k_values_hMpc):
    ratio = Pk_model1[i] / max(Pk_LCDM_arr[i], 1e-30)
    print(f"    k = {k_h:.2f}: {ratio:.4e}")


# =============================================================================
print("\n" + "=" * 80)
print("MODEL 2: Partially regulated (EFE interpolation)")
print("=" * 80)

alpha_values = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]

results_model2 = {}
for alpha in alpha_values:
    print(f"\n  --- alpha = {alpha:.1f} ---")
    D_m2 = []
    delta_final_m2 = []
    for i, (k_h, k_si) in enumerate(zip(k_values_hMpc, k_values_SI)):
        D, df, sol = solve_model2(k_h, k_si, alpha)
        D_m2.append(D)
        delta_final_m2.append(df)
        print(f"    k = {k_h:.2f}: D = {D:.4e}, delta_f = {df:.3e}")

    D_m2 = np.array(D_m2)
    Pk_m2 = P_prim_arr * T_b_arr**2 * D_m2**2 * k_values_hMpc
    sig8 = compute_sigma8(k_values_hMpc, Pk_m2)
    print(f"    sigma_8 = {sig8:.4f}")

    results_model2[alpha] = {
        'D': D_m2.copy(),
        'Pk': Pk_m2.copy(),
        'sigma8': sig8,
        'delta_final': np.array(delta_final_m2)
    }


# =============================================================================
print("\n" + "=" * 80)
print("MODEL 3: Self-consistent with temporal damping")
print("=" * 80)

# omega_t_factor values to scan
# omega_t^2 = factor * a0 * H / c
# a0/c ~ 4e-19 s^-1, H ~ 2e-18 s^-1
# so omega_t^2 ~ factor * 8e-37 s^-2
# H^2 ~ 5e-36 s^-2
# ratio: omega_t^2/H^2 ~ factor * 0.16
# Need factor ~ 1-10 to get significant effect

omega_t_factors = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

results_model3 = {}
for wt_factor in omega_t_factors:
    print(f"\n  --- omega_t_factor = {wt_factor:.1f} ---")
    D_m3 = []
    delta_final_m3 = []
    for i, (k_h, k_si) in enumerate(zip(k_values_hMpc, k_values_SI)):
        D, df, sol = solve_model3(k_h, k_si, wt_factor)
        D_m3.append(D)
        delta_final_m3.append(df)
        print(f"    k = {k_h:.2f}: D = {D:.4e}, delta_f = {df:.3e}")

    D_m3 = np.array(D_m3)
    Pk_m3 = P_prim_arr * T_b_arr**2 * D_m3**2 * k_values_hMpc
    sig8 = compute_sigma8(k_values_hMpc, Pk_m3)
    print(f"    sigma_8 = {sig8:.4f}")

    results_model3[wt_factor] = {
        'D': D_m3.copy(),
        'Pk': Pk_m3.copy(),
        'sigma8': sig8,
        'delta_final': np.array(delta_final_m3)
    }


# =============================================================================
# Summary output
# =============================================================================
print("\n" + "=" * 80)
print("SUMMARY OF RESULTS")
print("=" * 80)

print(f"\nLCDM reference: sigma_8 = {sigma8_LCDM:.4f}, D(z=0)/D(z_rec) = {D_LCDM_ratio:.2f}")
print(f"Observed: sigma_8 = 0.811 +/- 0.006 (Planck 2018)")

print(f"\nModel 1 (Pure p-Laplacian): sigma_8 = {sigma8_m1:.4f}")

print(f"\nModel 2 (Partially regulated):")
print(f"  {'alpha':>8s}  {'sigma_8':>10s}  {'D(k=0.10)':>12s}  {'P_DFD/P_LCDM(0.10)':>20s}")
for alpha in alpha_values:
    r = results_model2[alpha]
    idx_010 = 3  # k=0.10 index
    ratio = r['Pk'][idx_010] / max(Pk_LCDM_arr[idx_010], 1e-30)
    print(f"  {alpha:8.1f}  {r['sigma8']:10.4f}  {r['D'][idx_010]:12.4e}  {ratio:20.4e}")

print(f"\nModel 3 (Temporal damping):")
print(f"  {'omega_t_f':>8s}  {'sigma_8':>10s}  {'D(k=0.10)':>12s}  {'P_DFD/P_LCDM(0.10)':>20s}")
for wt in omega_t_factors:
    r = results_model3[wt]
    idx_010 = 3
    ratio = r['Pk'][idx_010] / max(Pk_LCDM_arr[idx_010], 1e-30)
    print(f"  {wt:8.1f}  {r['sigma8']:10.4f}  {r['D'][idx_010]:12.4e}  {ratio:20.4e}")

# Find the best-fit alpha for sigma_8 ~ 0.81
print(f"\n--- Best-fit search ---")
target_sigma8 = 0.811
best_alpha = None
best_diff = 1e10
for alpha in alpha_values:
    diff = abs(results_model2[alpha]['sigma8'] - target_sigma8)
    if diff < best_diff:
        best_diff = diff
        best_alpha = alpha
print(f"Model 2: Closest to sigma_8 = 0.811 is alpha = {best_alpha} "
      f"with sigma_8 = {results_model2[best_alpha]['sigma8']:.4f}")

best_wt = None
best_diff = 1e10
for wt in omega_t_factors:
    diff = abs(results_model3[wt]['sigma8'] - target_sigma8)
    if diff < best_diff:
        best_diff = diff
        best_wt = wt
print(f"Model 3: Closest to sigma_8 = 0.811 is omega_t_factor = {best_wt} "
      f"with sigma_8 = {results_model3[best_wt]['sigma8']:.4f}")


# =============================================================================
# Full k-dependent results table
# =============================================================================
print("\n" + "=" * 80)
print("FULL GROWTH FACTOR TABLE: D(k, z=0) / D(k, z_rec)")
print("=" * 80)

print(f"\n{'k (h/Mpc)':>12s}  {'Model1':>12s}  ", end='')
for alpha in [0.0, 0.5, 1.0]:
    print(f"{'M2(a='+str(alpha)+')':>12s}  ", end='')
for wt in [0.0, 1.0, 5.0]:
    print(f"{'M3(w='+str(wt)+')':>12s}  ", end='')
print(f"{'LCDM':>12s}")

for i, k_h in enumerate(k_values_hMpc):
    print(f"{k_h:12.2f}  {D_model1[i]:12.4e}  ", end='')
    for alpha in [0.0, 0.5, 1.0]:
        print(f"{results_model2[alpha]['D'][i]:12.4e}  ", end='')
    for wt in [0.0, 1.0, 5.0]:
        print(f"{results_model3[wt]['D'][i]:12.4e}  ", end='')
    print(f"{D_LCDM_ratio:12.4e}")


# =============================================================================
# P(k) ratio table
# =============================================================================
print("\n" + "=" * 80)
print("POWER SPECTRUM RATIO P_DFD(k) / P_LCDM(k)")
print("=" * 80)

print(f"\n{'k (h/Mpc)':>12s}  {'Model1':>12s}  ", end='')
for alpha in [0.0, 0.5, 1.0]:
    print(f"{'M2(a='+str(alpha)+')':>12s}  ", end='')
for wt in [0.0, 1.0, 5.0]:
    print(f"{'M3(w='+str(wt)+')':>12s}  ", end='')
print()

for i, k_h in enumerate(k_values_hMpc):
    r1 = Pk_model1[i] / max(Pk_LCDM_arr[i], 1e-30)
    print(f"{k_h:12.2f}  {r1:12.4e}  ", end='')
    for alpha in [0.0, 0.5, 1.0]:
        r = results_model2[alpha]['Pk'][i] / max(Pk_LCDM_arr[i], 1e-30)
        print(f"{r:12.4e}  ", end='')
    for wt in [0.0, 1.0, 5.0]:
        r = results_model3[wt]['Pk'][i] / max(Pk_LCDM_arr[i], 1e-30)
        print(f"{r:12.4e}  ", end='')
    print()

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
