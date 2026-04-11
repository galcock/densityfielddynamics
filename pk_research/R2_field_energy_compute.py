#!/usr/bin/env python3
"""
Round 2 Agent: Field Energy as Effective Dark Matter
Rigorous computation of:
  1. W(y) for mu(x) = x/(1+x)
  2. Field energy density rho_W
  3. Cosmic average <rho_W> using baryon P(k)
  4. Power spectrum of rho_W
  5. Self-sourcing bootstrap amplification
"""

import numpy as np
from scipy.integrate import quad, simps
from scipy.special import gamma as gamma_func

# ============================================================
# PHYSICAL CONSTANTS AND COSMOLOGICAL PARAMETERS
# ============================================================
G_N = 6.674e-11      # m^3 kg^-1 s^-2
c = 2.998e8           # m/s
h_hub = 0.674
H0 = h_hub * 100e3 / 3.086e22  # s^-1
a0_MOND = 1.2e-10    # m/s^2
a_star = 2 * a0_MOND / c**2    # m^-1
rho_crit = 3 * H0**2 / (8 * np.pi * G_N)  # kg/m^3

Omega_b = 0.0493
Omega_CDM = 0.261
Omega_m_LCDM = 0.315
rho_b0 = Omega_b * rho_crit
rho_CDM = Omega_CDM * rho_crit

print("=" * 70)
print("FUNDAMENTAL SCALES")
print("=" * 70)
print(f"a_0  = {a0_MOND:.2e} m/s^2")
print(f"a*   = {a_star:.4e} m^-1")
print(f"a*^2/(8piG) = {a_star**2/(8*np.pi*G_N):.4e} kg/m^3")
print(f"rho_crit = {rho_crit:.4e} kg/m^3")
print(f"rho_b0   = {rho_b0:.4e} kg/m^3")
print(f"rho_CDM  = {rho_CDM:.4e} kg/m^3")
print(f"Ratio a*^2/(8piG*rho_crit) = {a_star**2/(8*np.pi*G_N*rho_crit):.4e}")
print()

# ============================================================
# TASK 1: W(y) for mu(x) = x/(1+x)
# ============================================================
print("=" * 70)
print("TASK 1: KINETIC FUNCTION W(y)")
print("=" * 70)

def W_exact(y):
    """W(y) = y - 2*sqrt(y) + 2*ln(1+sqrt(y)) for mu(x)=x/(1+x)"""
    sy = np.sqrt(y)
    return y - 2*sy + 2*np.log(1 + sy)

def W_prime(y):
    """W'(y) = sqrt(y)/(1+sqrt(y)) = mu(sqrt(y))"""
    sy = np.sqrt(y)
    return sy / (1 + sy)

def mu_simple(x):
    return x / (1 + x)

# Verify
y_test = np.array([0.01, 0.1, 1.0, 10.0, 100.0])
print("y        | W(y)      | W'(y)=mu  | W_deep    | W_newt")
print("-" * 65)
for y in y_test:
    x = np.sqrt(y)
    W_deep = (2./3.) * y**1.5  # deep MOND limit
    W_newt = y                  # Newtonian limit
    print(f"{y:8.2f} | {W_exact(y):9.5f} | {W_prime(y):9.5f} | {W_deep:9.5f} | {W_newt:9.5f}")

# Asymptotic analysis
print("\nAsymptotic expansions:")
print("Deep MOND (y << 1): W ~ (2/3) y^{3/2}")
print("Newtonian (y >> 1): W ~ y - 2*sqrt(y) + 2*ln(sqrt(y))")
print()

# ============================================================
# TASK 2: FIELD ENERGY DENSITY
# ============================================================
print("=" * 70)
print("TASK 2: FIELD ENERGY DENSITY rho_W")
print("=" * 70)

prefactor = a_star**2 / (8 * np.pi * G_N)  # kg/m^3
print(f"Prefactor a*^2/(8piG) = {prefactor:.4e} kg/m^3")
print(f"This is {prefactor/rho_crit:.4e} * rho_crit")
print(f"This is {prefactor/rho_b0:.4e} * rho_b0")
print()

# rho_W for different gradient values
print("Gradient regimes:")
print(f"{'x=|grad psi|/a*':>20s} | {'W(x^2)':>12s} | {'rho_W (kg/m^3)':>14s} | {'rho_W/rho_crit':>14s}")
print("-" * 75)
for x in [1e-6, 1e-4, 1e-2, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    y = x**2
    Wy = W_exact(y)
    rho_W = prefactor * Wy
    print(f"{x:20.6f} | {Wy:12.6e} | {rho_W:14.6e} | {rho_W/rho_crit:14.6e}")

print()

# ============================================================
# TASK 2b: COSMIC AVERAGE FIELD ENERGY
# ============================================================
print("=" * 70)
print("TASK 2b: COSMIC AVERAGE <rho_W>")
print("=" * 70)

# Eisenstein-Hu baryon-only transfer function (simplified)
def T_baryon(k_hmpc):
    """Baryon-only transfer function from Eisenstein-Hu 1998.
    k in h/Mpc units."""
    Omega_b_h2 = 0.02237
    T_CMB = 2.725
    theta = T_CMB / 2.7
    
    # Sound horizon
    z_eq = 2.5e4 * Omega_b_h2 * theta**(-4)
    k_eq = 7.46e-2 * Omega_b_h2 * theta**(-2)  # h/Mpc
    
    # Silk damping scale
    R_d = 31.5 * Omega_b_h2 * theta**(-4) * (1000.)**(-1)
    z_d = 1060.  # Approximate
    k_silk = 1.6 * (Omega_b_h2)**0.52 * (Omega_b_h2)**0.73 * (1 + (10.4*Omega_b_h2)**(-0.95))
    
    # Simple fitting form for baryon transfer
    q = k_hmpc / (13.41 * k_eq)
    T0 = np.log(2*np.e + 1.8*q) / (np.log(2*np.e + 1.8*q) + (14.2 + 386./(1+69.9*q**1.08))*q**2)
    
    # Add baryon oscillations and Silk damping
    s = 44.5 * np.log(9.83/Omega_b_h2) / np.sqrt(1 + 10*(Omega_b_h2)**0.75)  # Mpc/h
    k_silk_val = 1.6 * (Omega_b_h2)**0.52   # approximate Silk scale
    
    # Baryon transfer with oscillations
    j0 = np.sinc(k_hmpc * s / np.pi)  # sinc = sin(x)/(x)
    T_b = T0 * j0 * np.exp(-(k_hmpc/k_silk_val)**1.4)
    
    return T_b

# Primordial power spectrum P(k) = A_s * (k/k_pivot)^(n_s - 1) * (2*pi^2/k^3)
A_s = 2.1e-9
n_s = 0.9649
k_pivot = 0.05  # h/Mpc

def P_psi_linear(k_hmpc):
    """Power spectrum of psi perturbations from baryonic P(k).
    In the linear regime: delta_psi_k = (8piG/(c^2 * k^2 * mu_eff)) * rho_bar * delta_k.
    So P_psi(k) = [(8piG rho_bar)/(c^2 k^2 mu_eff)]^2 * P_delta(k)
    """
    # Linear matter P(k) for baryon-only
    Pk_primordial = A_s * (k_hmpc / k_pivot)**(n_s - 1) * (2 * np.pi**2 / k_hmpc**3)
    Tb = T_baryon(k_hmpc)
    P_delta = Pk_primordial * Tb**2
    
    # Convert from delta to psi: grad psi = (8piG rho_bar)/(c^2 mu_eff) * ...
    # Actually in Fourier: k * psi_k = (8piG/(c^2 mu_eff)) * rho_bar * delta_k / k
    # So psi_k = (8piG rho_bar)/(c^2 mu_eff k^2) * delta_k
    # And grad(psi)_k = i*k*psi_k, so |grad psi_k|^2 = k^2 |psi_k|^2
    
    # P_{|grad psi|}(k) = k^2 * P_psi(k) = [(8piG rho_bar)/(c^2 mu_eff)]^2 / k^2 * P_delta(k)
    
    mu_eff = 0.898  # from agent24: mu_0 + L_0/3
    coupling = (8 * np.pi * G_N * rho_b0) / (c**2 * mu_eff)  # units: m^-2
    
    # Need to convert k from h/Mpc to 1/m
    k_m = k_hmpc * h_hub / (3.086e22)  # 1/m
    
    P_grad_psi = coupling**2 / k_m**2 * P_delta
    
    return P_grad_psi, P_delta

# Compute sigma_grad^2 = <|grad psi|^2> = integral k^2 P_psi(k) dk/(2pi^2)
# But P_{grad_psi}(k) already includes k^2 P_psi(k), so:
# sigma_grad^2 = integral P_{grad_psi}(k) * k^2 dk / (2pi^2)  -- NO
# Actually: <|grad psi|^2> = integral_0^inf (k^2 P_psi(k)) * k^2 dk/(2pi^2)
# = integral_0^inf P_{grad_psi}(k) * k^2 dk/(2pi^2)
# Wait, let me be careful with dimensions.

# P(k) has dimensions of (volume), so P(k) * k^3 ~ dimensionless
# <delta^2> = integral P(k) * k^2 dk / (2pi^2)  [dimensionless, as delta is]
# <|grad psi|^2> = integral k^2 * P_psi(k) * k^2 dk / (2pi^2) [has dims of (grad psi)^2 = 1/m^2]

# Actually let's be more careful. In Fourier:
# psi(x) = integral d^3k/(2pi)^3 psi_k e^{ikx}
# grad psi(x) = integral d^3k/(2pi)^3 (ik) psi_k e^{ikx}
# <|grad psi|^2> = integral d^3k/(2pi)^3 k^2 P_psi(k) = integral k^2 P_psi(k) * 4pi k^2 dk / (2pi)^3
#                = integral k^4 P_psi(k) dk / (2pi^2)

# P_psi(k) = [(8piG rho_bar)/(c^2 mu_eff)]^2 / k^4 * P_delta(k)
# So <|grad psi|^2> = [(8piG rho_bar)/(c^2 mu_eff)]^2 * integral P_delta(k) dk/(2pi^2) -- NO, dims wrong

# Let me redo properly. P_delta(k) has units [h/Mpc]^{-3} (comoving volume).
# <delta^2> = integral P_delta(k) k^2 dk / (2pi^2) [dimensionless]
# 
# psi_k = (8piG rho_bar)/(c^2 mu_eff k^2) delta_k  where k is in physical 1/m
# P_psi(k) = [(8piG rho_bar)/(c^2 mu_eff)]^2 / k^4 * P_delta(k)
# <|grad psi|^2> = integral k^2 P_psi(k) * k^2 dk / (2pi^2)
#                = [(8piG rho_bar)/(c^2 mu_eff)]^2 * integral P_delta(k) * k^2 dk/(2pi^2)  ... wrong
# NO. k^2 * P_psi = k^2 * C^2/k^4 * P_delta = C^2/k^2 * P_delta
# integral (C^2/k^2 * P_delta) * k^2 dk / (2pi^2) = C^2 integral P_delta(k) k^2 dk /(2pi^2) -- but this diverges

# The issue is that P_delta(k) grows at small k (red spectrum). Let's just compute numerically.

print("\nNumerical computation of <|grad psi|^2>:")
print()

mu_eff = 0.898
coupling_phys = (8 * np.pi * G_N * rho_b0) / (c**2 * mu_eff)  # m^{-2}
print(f"Coupling constant C = 8piG rho_b/(c^2 mu_eff) = {coupling_phys:.4e} m^-2")

# Compute in h/Mpc units, then convert
# k in h/Mpc -> k_phys = k * h / (Mpc in meters) = k * h / 3.086e22
Mpc_m = 3.086e22
hmpc_to_m = h_hub / Mpc_m  # conversion: k[h/Mpc] * this = k[1/m]

# sigma^2_delta = integral P_delta(k) k^2 dk/(2pi^2) in h/Mpc units
# sigma^2_grad_psi = C^2 * integral P_delta(k_phys) dk_phys / (2pi^2)  ... 
# Hmm this is getting complicated. Let me just do it numerically.

k_arr = np.logspace(-4, 1, 5000)  # h/Mpc
dk = np.diff(np.log(k_arr))

# P_delta in (Mpc/h)^3
P_delta_arr = np.zeros_like(k_arr)
for i, k in enumerate(k_arr):
    P_delta_arr[i] = A_s * (k / k_pivot)**(n_s - 1) * (2 * np.pi**2 / k**3) * T_baryon(k)**2

# sigma^2_delta
integrand_sigma_delta = P_delta_arr * k_arr**2 / (2 * np.pi**2) * k_arr  # k^2 * P(k) * k * dk_lnk / (2pi^2)
sigma_delta_sq = np.trapz(integrand_sigma_delta, np.log(k_arr))
print(f"sigma_delta^2 (baryon, linear, z=0) = {sigma_delta_sq:.4e}")
print(f"sigma_delta = {np.sqrt(sigma_delta_sq):.4f}")

# Now <|grad psi|^2> in physical units
# psi_k(k_phys) = C / k_phys^2 * delta_k
# P_psi(k_phys) = C^2 / k_phys^4 * P_delta(k_phys) [in physical units, m^3]
# <|grad psi|^2> = integral k_phys^2 * P_psi(k_phys) * k_phys^2 dk_phys/(2pi^2)
#                = C^2 * integral P_delta(k_phys) / k_phys^2 * k_phys^2 dk_phys/(2pi^2)  -- still wrong

# Let me be VERY explicit.
# <|grad psi|^2> = (1/(2pi)^3) * integral d^3k |k|^2 |psi_k|^2
# = integral k^4 |psi_k|^2 * dk/(2pi^2)  [using isotropy and dk notation for d(ln k) * k]
# Wait no: integral 4pi k^2 dk * k^2 |psi_k|^2 / (2pi)^3 = integral k^4 * P_psi(k) * dk / (2pi^2)
# NO. P_psi(k) = V * |psi_k|^2, and <|psi(x)|^2> = integral P_psi(k) * k^2 dk/(2pi^2)
# So <|grad psi(x)|^2> = integral k^2 P_psi(k) * k^2 dk/(2pi^2)

# In comoving h/Mpc units:
# psi_k = C_com / k_com^2 * delta_k  where C_com = coupling in comoving units
# k_com in h/Mpc, convert: k_phys = k_com * hmpc_to_m
# C_phys such that psi_k = C_phys / k_phys^2 * delta_k
# C_phys = coupling_phys [m^-2] (already physical)
# But P_delta is in (Mpc/h)^3 comoving units

# Let's just do everything in SI.
# P_delta(k_phys) = P_delta_com(k_com) * (Mpc/h)^3 where k_phys = k_com * h/Mpc
# = P_delta_com(k_com) / hmpc_to_m^3

# sigma^2_{grad psi} = coupling_phys^2 * integral_0^inf [P_delta(k_phys)/k_phys^2] * k_phys^2 dk_phys/(2pi^2)
# Wait: P_psi(k) = C^2/k^4 * P_delta(k), so k^2*P_psi = C^2/k^2 * P_delta
# Then integral k^2 * [C^2/k^2 * P_delta] * k^2 dk / (2pi^2) = C^2 * integral k^2 P_delta dk/(2pi^2) -- NO!
# integral [k^2 P_psi(k)] * k^2 dk/(2pi^2) = integral [C^2 P_delta(k) / k^2] * k^2 dk/(2pi^2)
# = C^2 * integral P_delta(k) * k^2 dk/(2pi^2)  ??? 
# Hmm, no: <|grad psi|^2> = integral k^2 * P_psi(k) * (k^2 dk)/(2pi^2)
# ... I keep confusing myself. Let me use the standard formula:
# sigma^2_X = integral_0^inf P_X(k) * k^2 dk/(2pi^2)   where P_X = power spectrum of X
# For X = grad_i(psi), P_{grad_i psi}(k) = k_i^2 P_psi(k), summed over i: k^2 P_psi(k)
# So <|grad psi|^2> = integral k^2 P_psi(k) * k^2 dk/(2pi^2)

# P_psi(k_com) in (Mpc/h)^3 = C_com^2/k_com^4 * P_delta(k_com) where C_com accounts for units
# Let's compute: C_com = (8piG rho_b)/(c^2 mu_eff) / hmpc_to_m^2 ... 
# No, the psi field equation in comoving:
# k_phys^2 * mu_eff * psi_k = (8piG/c^2) * rho_b * delta_k
# psi_k = (8piG rho_b)/(c^2 mu_eff k_phys^2) * delta_k
# = (8piG rho_b)/(c^2 mu_eff (k_com * h/Mpc_m)^2) * delta_k
# So P_psi(k_com) = [(8piG rho_b)/(c^2 mu_eff)]^2 / (k_com * h/Mpc_m)^4 * P_delta(k_com)

# <|grad psi|^2> in physical = integral (k_com * h/Mpc_m)^2 * P_psi(k_com) * (k_com * h/Mpc_m)^2 d(k_com * h/Mpc_m) / (2pi^2)
# = integral C^2/(k_com*h/Mpc_m)^2 * P_delta * (k_com*h/Mpc_m)^2 * h/Mpc_m dk_com / (2pi^2)
# = C^2 * (h/Mpc_m) * integral P_delta(k_com) * k_com^2 dk_com / (k_com^2 * (h/Mpc_m)^2 * 2pi^2)

# I'm going in circles. Let me just directly compute sigma_grad_psi^2 in physical units step by step.

sigma_grad_sq = 0.0
for i in range(len(k_arr)-1):
    k_com = 0.5*(k_arr[i] + k_arr[i+1])  # h/Mpc
    dk_com = k_arr[i+1] - k_arr[i]
    k_phys = k_com * hmpc_to_m  # 1/m
    
    # P_delta at this k (in (Mpc/h)^3)
    Pd = A_s * (k_com / k_pivot)**(n_s - 1) * (2 * np.pi**2 / k_com**3) * T_baryon(k_com)**2
    # Convert P_delta to physical units: m^3
    Pd_phys = Pd / hmpc_to_m**3  # (Mpc/h)^3 / (h/Mpc in m^-1)^3 = m^3
    
    # P_{grad psi}(k_phys) = k_phys^2 * P_psi(k_phys) = k_phys^2 * C^2/k_phys^4 * Pd_phys
    # = C^2/k_phys^2 * Pd_phys  [units: m^-4 * m^-2 * m^3 = m^-3 * m^2 = m^-1 ... hmm]
    
    # Actually <|grad psi|^2> = integral_0^inf k^2 P_psi(k) * 4pi k^2 dk / (2pi)^3
    # = integral_0^inf k^2 P_psi(k) * k^2 dk / (2pi^2)
    # P_psi has units of [psi]^2 * volume = 1 * m^3 (psi is dimensionless)
    # k^2 P_psi * k^2 dk / (2pi^2) has units m^-2 * m^3 * m^-2 * m^-1 / 1 = m^-2 GOOD (grad psi has units 1/m)
    
    P_psi_phys = coupling_phys**2 / k_phys**4 * Pd_phys  # m^-4 * m^3 = m^{-4} * m^3 ... 
    # coupling_phys: m^{-2}
    # C^2 = m^{-4}
    # C^2/k^4 * Pd = m^{-4}/m^{-4} * m^3 = m^3. Units of P_psi: m^3. Good.
    
    # k^2 * P_psi = m^{-2} * m^3 = m. Then:
    # integral (k^2 P_psi) * k^2 dk/(2pi^2) = m * m^{-2} * m^{-1} = m^{-2}. Good.
    
    integrand = k_phys**2 * P_psi_phys * k_phys**2 / (2 * np.pi**2)  # units: m^{-2} * m^{-1}
    sigma_grad_sq += integrand * (dk_com * hmpc_to_m)  # units: m^{-2}

print(f"\n<|grad psi|^2> = {sigma_grad_sq:.4e} m^-2")
print(f"<|grad psi|^2> / a*^2 = {sigma_grad_sq / a_star**2:.4e}")
sigma_grad = np.sqrt(sigma_grad_sq)
print(f"sigma_grad = sqrt(<|grad psi|^2>) = {sigma_grad:.4e} m^-1")
print(f"sigma_grad / a* = {sigma_grad / a_star:.4e}")

x_rms = sigma_grad / a_star
print(f"\nRMS x = sigma_grad / a* = {x_rms:.4e}")
print(f"This means the average cosmological gradient is in the {'MOND' if x_rms < 1 else 'Newtonian'} regime")
print()

# ============================================================
# TASK 2c: <rho_W> USING GAUSSIAN STATISTICS
# ============================================================
print("=" * 70)
print("TASK 2c: AVERAGE FIELD ENERGY <rho_W>")
print("=" * 70)

y_rms = sigma_grad_sq / a_star**2  # = <y> for the gradient

# For a Gaussian grad psi field with variance sigma_grad^2:
# <|grad psi|^2> = sigma_grad^2  (by definition)
# 
# In deep MOND (y << 1): W(y) ~ (2/3) y^{3/2}
# <W(y)> ~ (2/3) <y^{3/2}> 
#
# For y = |grad psi|^2/a*^2 with Gaussian grad psi (3 components):
# |grad psi|^2 = sum_i (partial_i psi)^2
# Each component has variance sigma_1^2 = sigma_grad^2/3
# |grad psi|^2 ~ sigma_1^2 * chi^2_3
# y = |grad psi|^2/a*^2 ~ (sigma_grad^2/(3*a*^2)) * chi^2_3

sigma_1_sq = sigma_grad_sq / 3  # variance of each gradient component
y_scale = sigma_1_sq / a_star**2  # scale parameter for y distribution

# y / (2 * y_scale) ~ chi^2_3 / 2 ~ Gamma(3/2, 1)
# PDF of y: f(y) = y^{1/2} exp(-y/(2*y_scale)) / (2*y_scale)^{3/2} / Gamma(3/2)

# <W(y)> = integral_0^inf W(y) f(y) dy
# For general W, need numerical integration.

# If we're in Newtonian regime (y_rms >> 1): <W> ~ <y> = y_rms
# If in deep MOND (y_rms << 1): <W> ~ (2/3) <y^{3/2}>

# For chi^2_3 distribution, <(chi^2_3)^p> = 2^p Gamma(p+3/2)/Gamma(3/2)
# <y^{3/2}> = (2*y_scale)^{3/2} * <(chi^2_3/2)^{3/2}> 
#            = (2*y_scale)^{3/2} * Gamma(3)/Gamma(3/2) / 2^{3/2}
#            = y_scale^{3/2} * 2^{3/2} * Gamma(3)/Gamma(3/2) / 2^{3/2}
#            = y_scale^{3/2} * Gamma(3)/Gamma(3/2)
#            = y_scale^{3/2} * 2 / (sqrt(pi)/2)
#            = y_scale^{3/2} * 4/sqrt(pi)

# Let me just compute numerically using the chi^2_3 distribution
from scipy.stats import chi2

def compute_avg_W(y_scale_param, N_samples=1000000):
    """Compute <W(y)> where y = |grad psi|^2/a*^2 follows a scaled chi^2_3."""
    if y_scale_param < 1e-30:
        return 0.0
    # y = 2 * y_scale * (chi2_3 / 2) = y_scale * chi2_3 ... no
    # |grad psi|^2 = sum_i xi_i^2 where xi_i ~ N(0, sigma_1^2)
    # y = |grad psi|^2 / a*^2 = sum_i (xi_i/a*)^2
    # xi_i/a* ~ N(0, sigma_1/a*), so (xi_i/a*)^2 has variance (sigma_1/a*)^2
    # y ~ (sigma_1/a*)^2 * chi^2_3 = y_scale * chi^2_3 ... wait
    # Actually: if X_i ~ N(0, sigma), then sum X_i^2 ~ sigma^2 * chi^2_n
    # So y ~ (sigma_1/a*)^2 * chi^2_3 = y_scale * chi^2_3
    
    # Numerical integration
    def integrand(chi2_val):
        y = y_scale_param * chi2_val
        return W_exact(y) * chi2.pdf(chi2_val, df=3)
    
    result, error = quad(integrand, 0, 100, limit=200)
    return result

avg_W = compute_avg_W(y_scale)
avg_rho_W = prefactor * avg_W

print(f"y_scale = sigma_1^2/a*^2 = {y_scale:.4e}")
print(f"<W(y)> = {avg_W:.6e}")
print(f"<rho_W> = (a*^2/8piG) * <W> = {avg_rho_W:.4e} kg/m^3")
print(f"<rho_W> / rho_crit = {avg_rho_W/rho_crit:.4e}")
print(f"<rho_W> / rho_b = {avg_rho_W/rho_b0:.4e}")
print(f"<rho_W> / rho_CDM = {avg_rho_W/rho_CDM:.4e}")
print()

# Also compute for the Newtonian and deep MOND limits
avg_y = 3 * y_scale  # <chi^2_3> = 3
avg_W_newt = avg_y  # Newtonian limit: W ~ y
avg_W_deep = (2./3.) * y_scale**1.5 * gamma_func(3) / gamma_func(1.5) * 1  # need proper moment

# Exact moment: <y^{3/2}> = integral y^{3/2} f(y) dy = (2*y_scale)^{3/2} * Gamma(3)/Gamma(3/2) / 2^{3/2}
# Actually for y ~ y_scale * chi^2_3:
# <y^p> = y_scale^p * <(chi^2_3)^p> = y_scale^p * 2^p * Gamma(p + 3/2) / Gamma(3/2)
avg_y_3half = y_scale**1.5 * 2**1.5 * gamma_func(3.0) / gamma_func(1.5)
avg_W_deep_exact = (2./3.) * avg_y_3half

print(f"For comparison:")
print(f"  Newtonian limit: <W> ~ <y> = {avg_W_newt:.4e}")
print(f"  Deep MOND limit: <W> ~ (2/3)<y^{{3/2}}> = {avg_W_deep_exact:.4e}")
print()

# ============================================================
# TASK 3: COMPARISON TO Omega_CDM
# ============================================================
print("=" * 70)
print("TASK 3: COMPARISON TO CDM")
print("=" * 70)

print(f"rho_CDM = Omega_CDM * rho_crit = {rho_CDM:.4e} kg/m^3")
print(f"<rho_W> = {avg_rho_W:.4e} kg/m^3")
print(f"Ratio <rho_W> / rho_CDM = {avg_rho_W/rho_CDM:.4e}")
print()

# Even if we use the background Hubble gradient:
a_H = c * H0  # Hubble acceleration
grad_psi_H = 2 * a_H / c**2  # gradient from Hubble flow
x_H = grad_psi_H / a_star
y_H = x_H**2
W_H = W_exact(y_H)
rho_W_hubble = prefactor * W_H

print(f"Background Hubble acceleration: a_H = cH_0 = {a_H:.4e} m/s^2")
print(f"|grad psi|_Hubble = 2a_H/c^2 = {grad_psi_H:.4e} m^-1")
print(f"x_Hubble = {x_H:.4f}")
print(f"y_Hubble = {y_H:.4f}")
print(f"W(y_Hubble) = {W_H:.4f}")
print(f"rho_W(Hubble) = {rho_W_hubble:.4e} kg/m^3")
print(f"rho_W(Hubble)/rho_crit = {rho_W_hubble/rho_crit:.4e}")
print()

print("CONCLUSION: The direct field energy density is approximately")
print(f"{avg_rho_W/rho_crit:.1e} of critical density, which is")
print(f"{avg_rho_W/rho_CDM:.1e} of the CDM density.")
print("This is utterly negligible as a dark matter substitute.")
print()

# ============================================================
# TASK 4: POWER SPECTRUM OF rho_W
# ============================================================
print("=" * 70)
print("TASK 4: POWER SPECTRUM OF rho_W")
print("=" * 70)

print("""
The energy density rho_W(x) = (a*^2/8piG) * W(|grad psi(x)|^2/a*^2) is a
nonlinear functional of grad psi. Its power spectrum involves mode coupling.

For the deep MOND regime where W(y) ~ (2/3) y^{3/2}:
  rho_W(x) ~ (a*^2/8piG) * (2/3) * [|grad psi|^2/a*^2]^{3/2}
           = (2/3) / (8piG * a*) * |grad psi(x)|^3

This is a CUBIC function of |grad psi|, making it a highly nonlinear tracer.

The power spectrum of rho_W involves the 6-point correlation function of
grad psi (since rho_W ~ |grad psi|^3). For Gaussian grad psi:

  P_{rho_W}(k) = integral d^3q1 d^3q2 K(q1, q2, k-q1-q2) * 
                  P_{grad}(q1) P_{grad}(q2) P_{grad}(|k-q1-q2|)

This is a TRIPLE convolution -- computationally intensive but tractable.
""")

# For a rough estimate, note that |rho_W(x)| ~ |grad psi|^3 / a*
# The power spectrum of |grad psi|^3 can be estimated as:
# P_{|g|^3}(k) ~ sigma_g^4 * P_{|g|}(k) * correction
# where the correction accounts for higher-order correlations.

# More simply: the Fourier transform of a power of a Gaussian field
# For f = g^n where g is Gaussian:
# P_f(k) involves n-th order convolution of P_g

# In Newtonian regime: W ~ y = x^2, so rho_W ~ |grad psi|^2
# P_{|g|^2}(k) = 2 * integral P_g(q) P_g(|k-q|) d^3q / (2pi)^3  [Wick's theorem]

# This is the standard one-loop power spectrum convolution.
# Let's compute it for the Newtonian case:

print("Computing P_{rho_W}(k) in Newtonian limit (W ~ y):")
print("rho_W ~ (a*^2/8piG) * |grad psi|^2/a*^2 = |grad psi|^2/(8piG)")
print()

# P_psi(k) in comoving (h/Mpc)^3
def P_psi_comoving(k_hmpc):
    """P_psi(k) in (Mpc/h)^3 comoving"""
    if k_hmpc < 1e-6:
        return 0.0
    Pd = A_s * (k_hmpc / k_pivot)**(n_s - 1) * (2 * np.pi**2 / k_hmpc**3) * T_baryon(k_hmpc)**2
    k_phys = k_hmpc * hmpc_to_m
    return coupling_phys**2 / k_phys**4 * Pd / hmpc_to_m**3  # (Mpc/h)^3

# For |grad psi|^2, the power spectrum is:
# P_{g^2}(k) = 2 * integral P_g(q) P_g(|k-q|) d^3q/(2pi)^3
# where g_i = partial_i psi, and |g|^2 = sum g_i^2
# P_{|g|^2}(k) = 2 * integral [sum_i q_i^2 P_psi(q)] [sum_j (k-q)_j^2 P_psi(|k-q|)] d^3q/(2pi)^3
# With isotropic P_psi: P_{|g|^2}(k) = 2 * integral q^2 P_psi(q) * |k-q|^2 P_psi(|k-q|) * 
#   [sum_ij q_i(k-q)_j delta_ij ... ] 
# Actually for |g|^2 = sum_i g_i^2:
# <|g|^2(x) |g|^2(x')> = sum_{ij} <g_i^2(x) g_j^2(x')>
# = sum_{ij} [<g_i(x)g_j(x')>^2 * 2 * delta_{ij} + <g_i^2><g_j^2>]  (connected part only for P)
# Connected: 2 * sum_i <g_i(x)g_i(x')>^2 + cross terms
# This simplifies for isotropic fields to:
# P_{|g|^2}(k) = 2 integral d^3q/(2pi)^3 [sum_i q_i(k-q)_i]^2 / (q^2 |k-q|^2) * q^2 P_psi(q) * |k-q|^2 P_psi(|k-q|)

# This is quite involved. Let me just estimate the amplitude.

# Amplitude of P_{rho_W}: 
# rho_W = (1/8piG) |grad psi|^2 in Newtonian limit
# delta_{rho_W} = rho_W / <rho_W> - 1 ~ 2 * delta_{|grad psi|/sigma_grad}
# So P_{delta_rho_W}(k) is related to P_psi by mode coupling

# Simple estimate: at scale k, the fluctuation in rho_W is:
# delta_rho_W(k) ~ 2 * <|grad psi|> * delta(grad psi)_k ~ 2 * sigma_grad * k * psi_k
# P_{delta_rho_W}(k) ~ 4 * sigma_grad^2 * k^2 * P_psi(k)

# This gives a BLUE spectrum (extra k^2 relative to P_psi).
# Since P_psi ~ P_delta / k^4, we get P_{delta_rho_W} ~ P_delta / k^2 * sigma_grad^2

# The CDM P(k) goes as k at large scales and k^{-3} at small scales (in 3D).
# P_delta ~ k^{n_s} * T^2(k) ~ k for large scales, k^{-3} past turnover.
# P_{delta_rho_W} ~ P_delta * sigma_grad^2 / k^2 ~ k^{n_s-2} at large scales

# This is a RED spectrum, not matching CDM. But the amplitude is:
rho_W_avg = avg_rho_W
delta_rho_W_over_rho_crit = rho_W_avg / rho_crit  # background level

print(f"Background field energy: <rho_W> = {rho_W_avg:.4e} kg/m^3")
print(f"Omega_W = <rho_W>/rho_crit = {delta_rho_W_over_rho_crit:.4e}")
print()
print("Even if P_{rho_W} had the right SHAPE, its AMPLITUDE is suppressed by")
print(f"(Omega_W/Omega_CDM)^2 = ({delta_rho_W_over_rho_crit:.1e}/{Omega_CDM})^2 = {(delta_rho_W_over_rho_crit/Omega_CDM)**2:.1e}")
print("relative to CDM. This makes it completely irrelevant for structure formation.")
print()

# ============================================================
# TASK 5: SELF-SOURCING BOOTSTRAP
# ============================================================
print("=" * 70)
print("TASK 5: SELF-SOURCING BOOTSTRAP")
print("=" * 70)

print("""
Modified field equation with self-sourcing:
  div[mu(x) grad psi] = -(8piG/c^2)(rho_m + rho_psi)

where rho_psi = (a*^2/8piG) W(|grad psi|^2/a*^2).

The bootstrap ratio is:
  epsilon = rho_psi / rho_matter = (a*^2 W(y)) / (8piG rho_matter)

For a perturbation at scale k with amplitude delta:
  |grad psi| ~ (8piG rho_b delta)/(c^2 mu_eff k) 
  x = |grad psi|/a* = (8piG rho_b delta)/(c^2 mu_eff k a*)
""")

# Bootstrap ratio for different scales
print(f"{'k (h/Mpc)':>12} {'delta':>8} {'x':>12} {'W(x^2)':>12} {'epsilon':>12}")
print("-" * 60)

for k_val in [0.001, 0.01, 0.1, 1.0]:
    for delta_val in [0.01, 0.1, 1.0]:
        k_phys_val = k_val * hmpc_to_m
        grad_psi_val = (8 * np.pi * G_N * rho_b0 * delta_val) / (c**2 * mu_eff * k_phys_val)
        x_val = grad_psi_val / a_star
        y_val = x_val**2
        W_val = W_exact(y_val)
        rho_psi_val = prefactor * W_val
        rho_m_val = rho_b0 * delta_val
        epsilon_val = rho_psi_val / rho_m_val if rho_m_val > 0 else 0
        print(f"{k_val:12.3f} {delta_val:8.2f} {x_val:12.4e} {W_val:12.4e} {epsilon_val:12.4e}")

print()

# Geometric series amplification
print("Bootstrap amplification (geometric series):")
print("If epsilon << 1, total amplification = 1/(1-epsilon) ~ 1 + epsilon")
print()

# For the most favorable case (largest scale, largest perturbation):
k_fav = 0.001
delta_fav = 1.0
k_phys_fav = k_fav * hmpc_to_m
grad_psi_fav = (8 * np.pi * G_N * rho_b0 * delta_fav) / (c**2 * mu_eff * k_phys_fav)
x_fav = grad_psi_fav / a_star
W_fav = W_exact(x_fav**2)
rho_psi_fav = prefactor * W_fav
eps_fav = rho_psi_fav / (rho_b0 * delta_fav)

print(f"Most favorable case: k={k_fav} h/Mpc, delta={delta_fav}")
print(f"  epsilon = {eps_fav:.4e}")
print(f"  Amplification = {1/(1-eps_fav):.6f}")
print(f"  Extra matter fraction = {eps_fav:.4e}")
print()

# The fundamental suppression factor
print("=" * 70)
print("FUNDAMENTAL SUPPRESSION ANALYSIS")
print("=" * 70)
print()
print("The field energy scale is set by a*^2/(8piG).")
print(f"a*^2/(8piG) = {prefactor:.4e} kg/m^3")
print(f"rho_crit = {rho_crit:.4e} kg/m^3")
print(f"Ratio = {prefactor/rho_crit:.4e}")
print()
print("This can be understood as:")
print(f"  a*^2/(8piG) = (2a_0/c^2)^2 / (8piG)")
print(f"  = 4 a_0^2 / (8piG c^4)")
print(f"  = a_0^2 / (2piG c^4)")
print()
a0_over_cH = a0_MOND / (c * H0)
print(f"  a_0 / (cH_0) = {a0_over_cH:.4f}")
print(f"  So a_0 ~ {a0_over_cH:.1f} * cH_0")
print()
print(f"  rho_crit = 3H_0^2/(8piG)")
print(f"  a*^2/(8piG) / rho_crit = (2a_0/c^2)^2 / (3H_0^2)")
print(f"  = 4 a_0^2 / (3 c^4 H_0^2)")
print(f"  = 4/3 * (a_0/(cH_0))^2 / c^2")
ratio_analytic = 4./3. * (a0_MOND / (c * H0))**2 / c**2
print(f"  = 4/3 * {a0_over_cH**2:.4f} / c^2")
print(f"  = {ratio_analytic:.4e}")
print()
print("The suppression is by c^{-2} (in natural units where a_0 ~ cH_0).")
print("This is the relativistic suppression: field energy ~ v^2/c^2 * gravitational energy.")
print("Since gravity is WEAK (Phi/c^2 ~ 10^{-5} on cosmological scales),")
print("the field energy is suppressed by ~ (Phi/c^2)^2 ~ 10^{-10} relative to matter.")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
1. W(y) = y - 2*sqrt(y) + 2*ln(1+sqrt(y)) for mu(x)=x/(1+x)
   Deep MOND: W ~ (2/3) y^{{3/2}}
   Newtonian: W ~ y

2. Field energy density scale: a*^2/(8piG) = {prefactor:.2e} kg/m^3
   This is {prefactor/rho_crit:.1e} * rho_crit

3. Cosmic average: <rho_W> = {avg_rho_W:.2e} kg/m^3
   = {avg_rho_W/rho_crit:.1e} * rho_crit
   = {avg_rho_W/rho_CDM:.1e} * rho_CDM

4. The power spectrum of rho_W is irrelevant because its AMPLITUDE
   is suppressed by ~10^{{-18}} relative to CDM.

5. Self-sourcing bootstrap: epsilon ~ {eps_fav:.1e} even in the most
   favorable case. The geometric amplification is 1 + O(10^{{-18}}).

CONCLUSION: The DIRECT field energy in DFD's psi gradients is
~10^{{18}} orders of magnitude too small to act as dark matter.
The mechanism for reproducing CDM-like effects in DFD must come
from the PHANTOM DARK MATTER effect (nonlinear mu enhancement)
and/or the temporal dust branch, NOT from field energy self-sourcing.
""")
