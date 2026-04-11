#!/usr/bin/env python3
"""
R3_nu_k_solver.py
=================
Compute the scale-dependent MOND enhancement factor nu(k) for the DFD power spectrum.

Three methods for y(k):
  A) Mode-by-mode: y_k from each Fourier mode's own acceleration
  B) RMS gradient (sigma_nabla): single y_eff from collective gradient of all modes
  C) Scale-dependent y(k): running integral of accelerations from modes with q < k

Outputs:
  - nu(k) for each method
  - P_DFD(k) / P_LCDM(k)
  - sigma_8 for each method
  - Required y for nu ~ 5-6 and comparison with computed values
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# Constants
# =============================================================================
c_light  = 2.998e8         # m/s
G_N      = 6.674e-11       # m^3 kg^-1 s^-2
Mpc_m    = 3.086e22        # meters per Mpc
h        = 0.674
H0_si    = 100 * h * 1e3 / Mpc_m   # s^-1

# Cosmology
Omega_m   = 0.315
Omega_b   = 0.049
Omega_bh2 = 0.02237
Omega_mh2 = Omega_m * h**2
n_s       = 0.965
A_s       = 2.1e-9
k_pivot   = 0.05            # Mpc^-1

# MOND
a0 = 1.2e-10               # m/s^2

# Derived
rho_crit  = 3 * H0_si**2 / (8 * np.pi * G_N)
rho_bar_b = Omega_b * rho_crit
c_H0      = c_light / H0_si / Mpc_m * h   # c/H0 in Mpc/h ~ 2998

print(f"rho_crit  = {rho_crit:.4e} kg/m^3")
print(f"rho_bar_b = {rho_bar_b:.4e} kg/m^3")
print(f"c/H0      = {c_H0:.1f} Mpc/h")

# =============================================================================
# Transfer functions
# =============================================================================

def T_EH_nowiggle(k_hMpc, omega_m, omega_b):
    """Eisenstein & Hu (1998) no-wiggle transfer function. k in h/Mpc."""
    k = np.asarray(k_hMpc, dtype=float)
    theta_cmb = 2.7255 / 2.7
    fb = omega_b / omega_m

    s = 44.5 * np.log(9.83 / omega_m) / np.sqrt(1 + 10 * omega_b**0.75)

    alpha_gamma = 1 - 0.328 * np.log(431 * omega_m) * fb + 0.38 * np.log(22.3 * omega_m) * fb**2

    gamma_eff = omega_m / h * (alpha_gamma + (1 - alpha_gamma) / (1 + (0.43 * k * s)**4))
    gamma_eff = np.maximum(gamma_eff, 1e-10)  # prevent negative/zero

    q = k * theta_cmb**2 / gamma_eff

    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1 + 62.5 * q)
    T = L / (L + C * q**2)

    return T


def T_baryon_silk(k_hMpc):
    """
    Baryon transfer function with Silk damping.

    For a baryon-only universe, the transfer function is dominated by
    Silk damping on small scales. The E&H formula breaks for Omega_m = Omega_b,
    so we use a physically motivated model:

    T_b(k) = T_LCDM_baryon_component(k) with proper Silk damping.

    Key physics: baryons couple to photons before decoupling, then undergo
    Silk damping at k > k_Silk ~ 0.1 h/Mpc. The baryon transfer function
    oscillates (BAO) and is damped exponentially:

    T_b(k) ~ j_0(k*r_s) * exp(-(k/k_Silk)^2)

    where r_s is the sound horizon and k_Silk is the Silk damping scale.

    We use the E&H98 baryon transfer function (their Eq. 17-24).
    """
    k = np.asarray(k_hMpc, dtype=float)

    # Use the FULL E&H98 formula for the baryon transfer function component
    # with the actual cosmological parameters (Omega_m = 0.315)
    # but then we only USE the baryon piece of the power spectrum.

    # Parameters for the full universe
    omega_m = Omega_mh2
    omega_b = Omega_bh2
    fb = omega_b / omega_m
    fc = 1 - fb

    theta_cmb = 2.7255 / 2.7

    # Equality redshift
    z_eq = 2.5e4 * omega_m * theta_cmb**(-4)
    k_eq = 7.46e-2 * omega_m * theta_cmb**(-2)  # Mpc^-1 ... convert to h/Mpc

    # Sound horizon
    b1 = 0.313 * omega_m**(-0.419) * (1 + 0.607 * omega_m**0.674)
    b2 = 0.238 * omega_m**0.223
    z_d = 1291 * omega_m**0.251 / (1 + 0.659 * omega_m**0.828) * (1 + b1 * omega_b**b2)

    R_eq = 31.5e3 * omega_b * theta_cmb**(-4) / z_eq
    R_d  = 31.5e3 * omega_b * theta_cmb**(-4) / z_d

    s_EH = 2.0 / (3.0 * k_eq) * np.sqrt(6 / R_eq) * np.log(
        (np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))  # h/Mpc ... actually Mpc

    # Silk damping scale
    k_Silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1 + (10.4 * omega_m)**(-0.95))  # Mpc^-1

    # Convert to h/Mpc
    s = s_EH  # already in Mpc, need in Mpc/h for k in h/Mpc? Let me check units.
    # k_eq is in Mpc^-1 from formula, s_EH should be in Mpc.
    # k is in h/Mpc, so k*s should use s in Mpc/h
    s_hMpc = s / h  # Mpc/h -- NO: s is in Mpc, k in h/Mpc, k*s has units h...
    # Actually k [h/Mpc] * s [Mpc] = h * (dimensionless). That's wrong.
    # We need k [Mpc^-1] * s [Mpc] = dimensionless.
    # k_Mpc = k_hMpc * h

    k_Mpc = k * h  # Mpc^-1

    # Baryon transfer function (simplified E&H style with Silk damping)
    # Use the no-wiggle formula for the FULL matter, then apply baryon suppression

    # Actually, let's use a simpler but correct approach:
    # The baryon transfer function in a baryon-only universe is just the
    # E&H baryon component, with Silk damping.
    #
    # T_b(k) ~ [sin(k*r_s)/(k*r_s)] * exp(-(k/k_silk)^p)
    #
    # But more practically: in DFD, what matters is the power spectrum of baryons
    # BEFORE MOND acts. The baryons fall into the same potential wells as in LCDM
    # but without CDM. So:
    #
    # At k < k_eq ~ 0.01 Mpc^-1: T_b ~ T_LCDM (modes entered after equality, grew together)
    # At k > k_Silk: T_b ~ exp(-k^2/k_Silk^2) (Silk damping)
    # In between: BAO oscillations modulated by Silk damping
    #
    # For the BARYON-ONLY universe, the key difference from LCDM is:
    # 1. No CDM potential wells to fall into after decoupling
    # 2. Silk damping erases small-scale perturbations
    # 3. Post-decoupling growth is suppressed (baryons can't grow until they decouple)

    # Simple Silk-damped baryon transfer function:
    # T_b(k) = T_0(k) * exp(-(k/k_Silk)^1.4)
    # where T_0 is the large-scale (CDM-like) transfer function

    # Use the no-wiggle formula with FULL matter parameters for T_0
    T0 = T_EH_nowiggle(k, omega_m, omega_b)

    # Silk damping (k_Silk is in Mpc^-1, need to convert)
    k_Silk_hMpc = k_Silk / h  # h/Mpc

    # The baryon fraction suppression + Silk damping
    # In a baryon-only universe without CDM wells, baryons oscillate then damp
    # The effective transfer: T_b ~ T_0 * exp(-(k/k_silk)^1.4) * [BAO envelope]

    # Silk scale
    Sigma_Silk = 8.38  # Mpc (approximate Silk damping length for these params)
    # More precisely: Sigma_Silk ~ 1/k_Silk * sqrt(2)
    Sigma_Silk = np.sqrt(2) / k_Silk  # Mpc

    T_b = T0 * np.exp(-(k_Mpc * Sigma_Silk)**1.4)

    return T_b


def T_baryon_physical(k_hMpc):
    """
    Physically motivated baryon-only transfer function.

    Uses the Eisenstein-Hu BARYON transfer function (their Tb, Eq 17-21)
    but simplified to the no-wiggle envelope for numerical stability.

    The key difference from LCDM: without CDM, baryons after decoupling
    have NO potential wells to fall into. The transfer function is:
    - Same as LCDM at very large scales (superhorizon)
    - Suppressed by (Omega_b/Omega_m)^2 in the Poisson equation mapping
    - Silk damped at k > k_Silk

    For computing DFD P(k), the baryon spectrum IS the input; MOND then
    enhances it. So we want:

    P_baryon(k) = P_primordial(k) * T_b^2(k) * D_b^2(z=0)

    where T_b accounts for baryon physics and D_b is the baryon growth factor.
    """
    k = np.asarray(k_hMpc, dtype=float)
    k_Mpc = k * h

    # E&H parameters
    omega_m = Omega_bh2  # baryon-only universe!
    omega_b = Omega_bh2
    theta_cmb = 2.7255 / 2.7

    # Equality redshift (baryon-photon equality for baryon-only universe)
    z_eq = 2.5e4 * omega_m * theta_cmb**(-4)

    # Sound horizon
    b1_param = 0.313 * omega_m**(-0.419) * (1 + 0.607 * omega_m**0.674)
    b2_param = 0.238 * omega_m**0.223
    z_d = 1291 * omega_m**0.251 / (1 + 0.659 * omega_m**0.828) * (1 + b1_param * omega_b**b2_param)

    # Baryon-to-photon ratio
    R_d = 31.5e3 * omega_b * theta_cmb**(-4) / z_d

    # Sound horizon at drag
    k_eq = 7.46e-2 * omega_m * theta_cmb**(-2)  # Mpc^-1
    R_eq = 31.5e3 * omega_b * theta_cmb**(-4) / z_eq
    s_Mpc = 2.0 / (3.0 * k_eq) * np.sqrt(6.0 / R_eq) * np.log(
        (np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    # Silk damping
    k_Silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1 + (10.4 * omega_m)**(-0.95))  # Mpc^-1

    # For baryon-only: use BBKS-style transfer function with correct Gamma
    # Gamma_eff for baryon-only universe
    Gamma = omega_m / h  # shape parameter

    q = k_Mpc / Gamma  # dimensionless

    # BBKS transfer function (Bardeen et al. 1986)
    T_BBKS = np.log(1 + 2.34 * q) / (2.34 * q) * (
        1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)

    # Apply Silk damping
    T_b = T_BBKS * np.exp(-(k_Mpc / k_Silk)**1.4)

    # Handle k=0
    T_b = np.where(k > 0, T_b, 1.0)

    return T_b


def T_lcdm(k_hMpc):
    """Standard LCDM transfer function."""
    return T_EH_nowiggle(k_hMpc, Omega_mh2, Omega_bh2)


# =============================================================================
# Growth factor
# =============================================================================
def growth_factor(Om, z=0):
    """Carroll, Press & Turner (1992) approximation."""
    a = 1.0 / (1.0 + z)
    Ol = 1.0 - Om
    Ez2 = Om * (1+z)**3 + Ol
    Omz = Om * (1+z)**3 / Ez2
    Olz = Ol / Ez2
    D = 2.5 * Omz / (Omz**(4.0/7.0) - Olz + (1 + Omz/2.0) * (1 + Olz/70.0))
    D *= a
    return D

D0_lcdm = growth_factor(Omega_m, 0)
D0_baryononly = growth_factor(Omega_b, 0)

print(f"\nD(z=0, Omega_m={Omega_m}) = {D0_lcdm:.4f}")
print(f"D(z=0, Omega_b={Omega_b}) = {D0_baryononly:.4f}")


# =============================================================================
# Power spectrum builder
# =============================================================================
def make_Pk(k_hMpc, T_func, Omega_poisson, D_growth):
    """
    P(k) = (8*pi^2/25) * (c/H0)^4 * A_s * (k_Mpc/k_pivot)^{ns-1} * k * T^2 * D^2 / Omega^2

    k in h/Mpc. Returns P in (Mpc/h)^3.
    """
    k = np.asarray(k_hMpc, dtype=float)
    k_Mpc = k * h
    T = T_func(k)

    P = (8.0 * np.pi**2 / 25.0) * c_H0**4 * A_s
    P *= (k_Mpc / k_pivot)**(n_s - 1)
    P *= k * T**2 * D_growth**2 / Omega_poisson**2
    return P


# =============================================================================
# Build k grid and power spectra
# =============================================================================
Nk = 3000
k_arr = np.logspace(-4, 1, Nk)  # h/Mpc

# LCDM power spectrum (reference)
P_lcdm_arr = make_Pk(k_arr, T_lcdm, Omega_m, D0_lcdm)

# Baryon-only power spectrum
# Key choice: what Omega goes in the Poisson denominator?
# For a baryon-only universe: Omega_poisson = Omega_b
# Growth factor: in baryon-only cosmology, growth is much suppressed
P_baryon_arr = make_Pk(k_arr, T_baryon_physical, Omega_b, D0_baryononly)

# Check sigma8
def W_tophat(x):
    x = np.asarray(x, dtype=float)
    r = np.ones_like(x)
    m = np.abs(x) > 1e-6
    xm = x[m]
    r[m] = 3.0 * (np.sin(xm) - xm * np.cos(xm)) / xm**3
    return r

def sigma_R(k, Pk, R):
    x = k * R
    W = W_tophat(x)
    integrand = k**2 * Pk * W**2 / (2 * np.pi**2)
    return np.sqrt(np.trapz(integrand, k))

sigma8_lcdm = sigma_R(k_arr, P_lcdm_arr, 8.0)
sigma8_baryon_bare = sigma_R(k_arr, P_baryon_arr, 8.0)

print(f"\nsigma_8 (LCDM)       = {sigma8_lcdm:.4f}")
print(f"sigma_8 (baryon bare) = {sigma8_baryon_bare:.6f}")

# Transfer function diagnostics
print("\nTransfer functions:")
print(f"  {'k':<8} {'T_b':<12} {'T_lcdm':<12} {'T_b/T_l':<10} {'P_b/P_L':<12}")
for kv in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_arr - kv))
    Tb = T_baryon_physical(kv)
    Tl = T_lcdm(kv)
    ratio_P = P_baryon_arr[idx] / P_lcdm_arr[idx]
    print(f"  {kv:<8.3f} {Tb:<12.6f} {Tl:<12.6f} {Tb/Tl:<10.4f} {ratio_P:<12.4e}")


# =============================================================================
# Acceleration prefactor
# =============================================================================
prefactor = 4 * np.pi * G_N * rho_bar_b  # = 1.5 * Omega_b * H0^2
print(f"\n4*pi*G*rho_b = {prefactor:.4e} s^-2")


# =============================================================================
# MOND function
# =============================================================================
def nu_mond(y):
    y = np.maximum(np.asarray(y, dtype=float), 1e-30)
    return 0.5 * (1 + np.sqrt(1 + 4.0/y))


# =============================================================================
# METHOD A: Mode-by-mode y(k)
# =============================================================================
print("\n" + "="*70)
print("METHOD A: Mode-by-mode")
print("="*70)

# delta_rms(k) = sqrt(k^3 P(k) / 2pi^2) = sqrt(Delta^2(k))
Delta2_b = k_arr**3 * P_baryon_arr / (2 * np.pi**2)
delta_rms = np.sqrt(np.maximum(Delta2_b, 0))

# g_N = prefactor * delta / k_phys
k_phys = k_arr * h / Mpc_m   # m^-1
g_N_A = prefactor * delta_rms / k_phys
y_A = g_N_A / a0
nu_A = nu_mond(y_A)

print(f"  {'k':<8} {'delta_rms':<11} {'g_N':<13} {'y':<12} {'nu':<8} {'nu^2':<8}")
for kv in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    i = np.argmin(np.abs(k_arr - kv))
    print(f"  {kv:<8.3f} {delta_rms[i]:<11.4e} {g_N_A[i]:<13.4e} {y_A[i]:<12.4e} "
          f"{nu_A[i]:<8.3f} {nu_A[i]**2:<8.1f}")


# =============================================================================
# METHOD B: Global RMS gradient
# =============================================================================
print("\n" + "="*70)
print("METHOD B: Global RMS gradient")
print("="*70)

# sigma_g^2 = prefactor^2 * int dk/(2pi^2) P(k)  [with unit conversion]
# int dk_phys P_phys = int dk * P * (Mpc/h)^2 / (2pi^2)  ... wait let me be careful.
#
# sigma_g^2 = int d^3k/(2pi)^3 * |g(k)|^2
#           = int dk k^2/(2pi^2) * P_g(k)
#           = int dk k^2/(2pi^2) * (prefactor/k_phys)^2 * P_delta_phys(k)
#   ... where everything needs consistent units.
#
# Let's work entirely in physical units:
# k_phys = k_hMpc * h / Mpc   [m^-1]
# P_phys = P_hMpc3 * (Mpc/h)^3  [m^3]
# dk_phys = dk * h/Mpc  [m^-1]
#
# sigma_g^2 = prefactor^2 * int dk_phys/(2pi^2) * P_delta_phys(k_phys)
#           = prefactor^2 * int dk * (h/Mpc) / (2pi^2) * P * (Mpc/h)^3
#           = prefactor^2 * (Mpc/h)^2 / (2pi^2) * int dk * P

conv = (Mpc_m / h)**2 / (2 * np.pi**2)
int_P = np.trapz(P_baryon_arr, k_arr)
sigma_g_B = prefactor * np.sqrt(int_P * conv)
y_B_val = sigma_g_B / a0
nu_B_val = nu_mond(y_B_val)

print(f"  int dk P(k)  = {int_P:.4e} (Mpc/h)^2")
print(f"  sigma_g      = {sigma_g_B:.4e} m/s^2")
print(f"  y_eff        = {y_B_val:.4e}")
print(f"  nu_eff       = {nu_B_val:.4f}")
print(f"  nu_eff^2     = {nu_B_val**2:.2f}")

y_B = np.full_like(k_arr, y_B_val)
nu_B = np.full_like(k_arr, nu_B_val)


# =============================================================================
# METHOD C: Running integral y(k)
# =============================================================================
print("\n" + "="*70)
print("METHOD C: Running integral")
print("="*70)

cumint = np.zeros(Nk)
for i in range(1, Nk):
    cumint[i] = cumint[i-1] + 0.5 * (P_baryon_arr[i] + P_baryon_arr[i-1]) * (k_arr[i] - k_arr[i-1])

sigma_g_C = prefactor * np.sqrt(np.maximum(cumint * conv, 0))
y_C = sigma_g_C / a0
y_C = np.maximum(y_C, 1e-30)
nu_C = nu_mond(y_C)

print(f"  {'k':<8} {'sigma_g(<k)':<13} {'y':<12} {'nu':<8} {'nu^2':<8}")
for kv in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    i = np.argmin(np.abs(k_arr - kv))
    print(f"  {kv:<8.3f} {sigma_g_C[i]:<13.4e} {y_C[i]:<12.4e} "
          f"{nu_C[i]:<8.3f} {nu_C[i]**2:<8.1f}")


# =============================================================================
# P_DFD / P_LCDM
# =============================================================================
print("\n" + "="*70)
print("P_DFD(k) / P_LCDM(k)")
print("="*70)

P_DFD_A = nu_A**2 * P_baryon_arr
P_DFD_B = nu_B_val**2 * P_baryon_arr
P_DFD_C = nu_C**2 * P_baryon_arr

ratio_A = P_DFD_A / P_lcdm_arr
ratio_B = P_DFD_B / P_lcdm_arr
ratio_C = P_DFD_C / P_lcdm_arr

print(f"\n  {'k':<8} {'P_b/P_L':<12} {'nu_A':<8} {'nu_B':<8} {'nu_C':<8} "
      f"{'ratio_A':<10} {'ratio_B':<10} {'ratio_C':<10}")
print("  " + "-"*76)
for kv in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0]:
    i = np.argmin(np.abs(k_arr - kv))
    br = P_baryon_arr[i] / P_lcdm_arr[i]
    print(f"  {kv:<8.3f} {br:<12.4e} {nu_A[i]:<8.2f} {nu_B_val:<8.2f} {nu_C[i]:<8.2f} "
          f"{ratio_A[i]:<10.4f} {ratio_B[i]:<10.4f} {ratio_C[i]:<10.4f}")


# =============================================================================
# sigma_8
# =============================================================================
print("\n" + "="*70)
print("SIGMA_8")
print("="*70)

sigma8_A = sigma_R(k_arr, P_DFD_A, 8.0)
sigma8_B = sigma_R(k_arr, P_DFD_B, 8.0)
sigma8_C = sigma_R(k_arr, P_DFD_C, 8.0)

print(f"  sigma_8 (LCDM):            {sigma8_lcdm:.4f}")
print(f"  sigma_8 (baryon bare):     {sigma8_baryon_bare:.6f}")
print(f"  sigma_8 (Method A):        {sigma8_A:.4f}")
print(f"  sigma_8 (Method B):        {sigma8_B:.4f}")
print(f"  sigma_8 (Method C):        {sigma8_C:.4f}")
print(f"  sigma_8 target:            ~0.81")

# Ratios
print(f"\n  sigma8_A / sigma8_LCDM = {sigma8_A/sigma8_lcdm:.4f}")
print(f"  sigma8_B / sigma8_LCDM = {sigma8_B/sigma8_lcdm:.4f}")
print(f"  sigma8_C / sigma8_LCDM = {sigma8_C/sigma8_lcdm:.4f}")


# =============================================================================
# Part 5: What nu is needed and what y gives it
# =============================================================================
print("\n" + "="*70)
print("PART 5: REQUIRED nu AND y AT SIGMA_8 SCALES")
print("="*70)

print("\ny -> nu table:")
for nu_t in [2, 3, 4, 5, 5.5, 6, 6.4, 8, 10, 20, 50, 100]:
    y_req = 4.0 / ((2*nu_t - 1)**2 - 1)
    print(f"  nu = {nu_t:6.1f} => y = {y_req:.6f}")

# What each method predicts at k = 0.1 h/Mpc
print("\nDetailed comparison at sigma_8 scales:")
for kv in [0.05, 0.1, 0.15, 0.2]:
    i = np.argmin(np.abs(k_arr - kv))
    br = P_baryon_arr[i] / P_lcdm_arr[i]
    nu_need = 1.0 / np.sqrt(br)
    y_need = 4.0 / ((2*nu_need - 1)**2 - 1)

    print(f"\n  k = {kv} h/Mpc:")
    print(f"    P_b/P_LCDM  = {br:.4e}")
    print(f"    nu_needed   = {nu_need:.3f}")
    print(f"    y_needed    = {y_need:.6f}")
    print(f"    Method A:   y = {y_A[i]:.4e}, nu = {nu_A[i]:.3f}, ratio = {ratio_A[i]:.4f}")
    print(f"    Method B:   y = {y_B_val:.4e}, nu = {nu_B_val:.3f}, ratio = {ratio_B[i]:.4f}")
    print(f"    Method C:   y = {y_C[i]:.4e}, nu = {nu_C[i]:.3f}, ratio = {ratio_C[i]:.4f}")


# =============================================================================
# What a_star is needed to match?
# =============================================================================
print("\n" + "="*70)
print("WHAT a_star WOULD BE NEEDED?")
print("="*70)

for kv in [0.1, 0.2]:
    i = np.argmin(np.abs(k_arr - kv))
    br = P_baryon_arr[i] / P_lcdm_arr[i]
    nu_need = 1.0 / np.sqrt(br)
    y_need = 4.0 / ((2*nu_need - 1)**2 - 1)

    print(f"\nAt k = {kv} h/Mpc: need nu = {nu_need:.3f}, y = {y_need:.6f}")
    for name, yval in [("A", y_A[i]), ("B", y_B_val), ("C", y_C[i])]:
        g_val = yval * a0
        a_star = g_val / y_need if y_need > 0 else np.inf
        print(f"  Method {name}: g = {g_val:.4e}, a_star_needed = {a_star:.4e} "
              f"= {a_star/a0:.3e} * a0")


# =============================================================================
# KEY INSIGHT: The (Omega_b/Omega_m) factor
# =============================================================================
print("\n" + "="*70)
print("KEY INSIGHT: THE AMPLITUDE RATIO")
print("="*70)

print(f"""
The bare ratio P_baryon / P_LCDM has TWO sources of suppression:

1. Poisson equation: delta ~ Phi * k^2 / (4piG*rho*a^2)
   P_delta ~ 1/Omega^2, so P_b/P_L ~ (Omega_m/Omega_b)^2 = {(Omega_m/Omega_b)**2:.1f} ENHANCEMENT
   Wait -- baryons have SMALLER Omega, so for same Phi: delta is LARGER.
   But we want P_delta(baryon only) vs P_delta(LCDM with CDM+baryons).

   The real ratio is:
   P_b / P_LCDM = (T_b/T_LCDM)^2 * (D_b/D_LCDM)^2 * (Omega_m/Omega_b)^2

   The (Omega_m/Omega_b)^2 = {(Omega_m/Omega_b)**2:.1f} comes from the normalization:
   P(k) ~ A_s * T^2 * D^2 * k / Omega^2 (from Poisson equation inversion)

   Smaller Omega means delta is bigger for same primordial potential.
   So baryons are actually ENHANCED at large scales!

   But the transfer function ratio T_b/T_LCDM kills this at small scales.
   And the growth factor ratio D_b/D_LCDM = {D0_baryononly/D0_lcdm:.4f} adds suppression.

2. Transfer function: T_baryon has Silk damping, CDM does not.
   At k > 0.1 h/Mpc, T_b is strongly suppressed.

3. Growth factor: D(Omega_b) = {D0_baryononly:.4f} vs D(Omega_m) = {D0_lcdm:.4f}
   Ratio = {D0_baryononly/D0_lcdm:.4f}, so D^2 ratio = {(D0_baryononly/D0_lcdm)**2:.4f}

Net large-scale ratio:
  (Omega_m/Omega_b)^2 * (D_b/D_L)^2 = {(Omega_m/Omega_b)**2 * (D0_baryononly/D0_lcdm)**2:.4f}
  (with T_b/T_L ~ 1 at large scales)
""")

# Verify
print("Verification of large-scale ratio:")
i_ls = np.argmin(np.abs(k_arr - 0.001))
print(f"  Predicted: {(Omega_m/Omega_b)**2 * (D0_baryononly/D0_lcdm)**2 * (T_baryon_physical(0.001)/T_lcdm(0.001))**2:.4f}")
print(f"  Actual P_b/P_L at k=0.001: {P_baryon_arr[i_ls]/P_lcdm_arr[i_ls]:.4f}")


# =============================================================================
# FINAL SUMMARY TABLE
# =============================================================================
print("\n" + "="*70)
print("FINAL COMPREHENSIVE TABLE")
print("="*70)

header = (f"{'k(h/Mpc)':<10} {'P_b(Mpc/h)^3':<14} {'P_L(Mpc/h)^3':<14} {'P_b/P_L':<10} "
          f"{'nu_need':<8} {'y_A':<11} {'nu_A':<7} {'y_C':<11} {'nu_C':<7} "
          f"{'DFD_A/L':<9} {'DFD_C/L':<9}")
print(header)
print("-"*len(header))
for kv in [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0, 5.0]:
    i = np.argmin(np.abs(k_arr - kv))
    br = P_baryon_arr[i] / P_lcdm_arr[i]
    nu_req = 1.0 / np.sqrt(br) if br > 0 else np.inf
    print(f"{kv:<10.3f} {P_baryon_arr[i]:<14.4e} {P_lcdm_arr[i]:<14.4e} {br:<10.4e} "
          f"{nu_req:<8.2f} {y_A[i]:<11.4e} {nu_A[i]:<7.2f} {y_C[i]:<11.4e} {nu_C[i]:<7.2f} "
          f"{ratio_A[i]:<9.3f} {ratio_C[i]:<9.3f}")

print(f"\nMethod B: y_eff = {y_B_val:.4e}, nu_eff = {nu_B_val:.3f}, applies uniformly")

# =============================================================================
# Save data
# =============================================================================
np.savez('/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R3_nu_k_data.npz',
         k=k_arr, P_baryon=P_baryon_arr, P_lcdm=P_lcdm_arr,
         y_A=y_A, y_B=y_B, y_C=y_C,
         nu_A=nu_A, nu_B=nu_B, nu_C=nu_C,
         ratio_A=ratio_A, ratio_B=ratio_B, ratio_C=ratio_C,
         delta_rms=delta_rms, g_N_A=g_N_A, sigma_g_C=sigma_g_C,
         sigma8_lcdm=sigma8_lcdm, sigma8_baryon=sigma8_baryon_bare,
         sigma8_A=sigma8_A, sigma8_B=sigma8_B, sigma8_C=sigma8_C)

print("\nData saved to R3_nu_k_data.npz")
print("Done.")
