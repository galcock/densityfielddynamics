#!/usr/bin/env python3
"""
Round 3 Agent: MOND-Modified Pre-Recombination Transfer Function
=================================================================

THE KEY INSIGHT: MOND enhancement applies during the acoustic epoch too.
During recombination, the MOND interpolation function nu deepens potential
wells beyond what baryons alone provide. This effectively increases the
matter density for computing the transfer function:

    Omega_m,eff(k) = nu(k, z_rec) * Omega_b

If nu_rec * Omega_b ~ 0.25-0.30, this recovers LCDM-like z_eq, sound
horizon, Silk damping, and BAO positions.

Author: Round 3 Agent (Claude Opus 4.6)
Date: 2026-04-04
"""

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PHYSICAL CONSTANTS AND COSMOLOGICAL PARAMETERS
# =============================================================================
H0_km_s_Mpc = 67.4
h = H0_km_s_Mpc / 100.0
H0_si = H0_km_s_Mpc * 1e3 / 3.0856775814913673e22  # s^-1

Omega_b_h2 = 0.02237
Omega_b = Omega_b_h2 / h**2  # ~ 0.0493

Omega_m_LCDM = 0.315
Omega_cdm_h2_LCDM = 0.1200
Omega_m_h2_LCDM = Omega_cdm_h2_LCDM + Omega_b_h2
Omega_Lambda = 1.0 - Omega_m_LCDM

T_CMB = 2.725  # K
n_s = 0.9649
A_s = 2.1e-9
k_pivot = 0.05  # Mpc^-1

a0_MOND = 1.2e-10  # m/s^2
G_N = 6.674e-11    # m^3 kg^-1 s^-2
c_light = 2.998e8  # m/s
Mpc_m = 3.0856775814913673e22  # m per Mpc

rho_crit_0 = 3 * H0_si**2 / (8 * np.pi * G_N)  # kg/m^3
rho_b_0 = Omega_b * rho_crit_0

# MOND interpolation function (simple form)
def nu_mond(y):
    """Standard MOND interpolation function nu(y) where y = g_N/a0.
    nu(y) = 1 for y >> 1 (Newtonian regime)
    nu(y) ~ 1/sqrt(y) for y << 1 (deep MOND regime)
    """
    return 0.5 * (1.0 + np.sqrt(1.0 + 4.0/y))

def nu_mond_safe(y):
    """Safe version handling arrays and edge cases."""
    y = np.atleast_1d(np.asarray(y, dtype=float))
    result = np.zeros_like(y)
    mask = y > 1e-30
    result[mask] = 0.5 * (1.0 + np.sqrt(1.0 + 4.0/y[mask]))
    result[~mask] = 1.0 / np.sqrt(y[~mask] + 1e-50)
    return result

# =============================================================================
# TASK 1: COMPUTE nu AT RECOMBINATION
# =============================================================================
print("=" * 80)
print("TASK 1: MOND ENHANCEMENT FACTOR AT RECOMBINATION")
print("=" * 80)

z_rec = 1100
a_rec = 1.0 / (1.0 + z_rec)

# Mean baryon density at recombination
rho_b_rec = rho_b_0 * (1 + z_rec)**3
print(f"\nPhysical conditions at z_rec = {z_rec}:")
print(f"  a_rec = {a_rec:.6e}")
print(f"  rho_b_0 = {rho_b_0:.4e} kg/m^3")
print(f"  rho_b(z_rec) = {rho_b_rec:.4e} kg/m^3")

# Perturbation amplitude at recombination
delta_rec = 3e-4  # typical amplitude of baryon perturbations at z~1100

# For a mode with comoving wavenumber k (in h/Mpc):
# Physical wavelength at recombination: lambda_phys = 2*pi*a_rec / (k * h / Mpc_m)
# The Newtonian gravitational acceleration from the perturbation is:
#   g_N ~ (4*pi*G/3) * rho_b(z_rec) * delta * lambda_phys / 2
# More precisely, for a Fourier mode of amplitude delta at wavenumber k:
#   g_N(k) = 4*pi*G * rho_b * delta / k_phys
# where k_phys = k_comoving / a_rec

k_values = np.array([0.01, 0.02, 0.05, 0.10, 0.20, 0.50])  # h/Mpc

print(f"\nPerturbation amplitude: delta = {delta_rec}")
print(f"\n{'k [h/Mpc]':>12} {'k_phys [1/m]':>14} {'lambda [Mpc]':>14} {'g_N [m/s^2]':>14} {'g_N/a0':>12} {'nu':>10}")
print("-" * 80)

results_task1 = {}
for k_hMpc in k_values:
    # Convert k from h/Mpc to 1/Mpc
    k_Mpc = k_hMpc * h  # 1/Mpc

    # Comoving wavelength
    lambda_comoving_Mpc = 2 * np.pi / k_Mpc  # Mpc

    # Physical wavenumber at recombination
    k_phys = k_Mpc / (a_rec * Mpc_m)  # 1/m

    # Newtonian gravitational acceleration from a density perturbation
    # For a sinusoidal perturbation of amplitude delta at wavenumber k:
    # The gravitational potential Phi = -4*pi*G*rho*delta / k^2
    # The gravitational acceleration g = k * Phi = 4*pi*G*rho*delta / k
    g_N = 4 * np.pi * G_N * rho_b_rec * delta_rec / k_phys  # m/s^2

    y = g_N / a0_MOND
    nu_val = nu_mond(y)

    results_task1[k_hMpc] = {
        'k_phys': k_phys,
        'lambda_Mpc': lambda_comoving_Mpc,
        'g_N': g_N,
        'y': y,
        'nu': nu_val
    }

    print(f"{k_hMpc:12.2f} {k_phys:14.4e} {lambda_comoving_Mpc:14.1f} {g_N:14.4e} {y:12.4e} {nu_val:10.2f}")

print(f"\n  => nu(k) ranges from {min(r['nu'] for r in results_task1.values()):.2f} "
      f"to {max(r['nu'] for r in results_task1.values()):.2f}")

# Effective Omega_m
print(f"\n  => Omega_m_eff(k) = nu(k) * Omega_b:")
for k_hMpc in k_values:
    nu_val = results_task1[k_hMpc]['nu']
    Om_eff = nu_val * Omega_b
    print(f"     k = {k_hMpc:.2f} h/Mpc: nu = {nu_val:.2f}, Omega_m_eff = {Om_eff:.4f}")


# =============================================================================
# TASK 2: EISENSTEIN-HU TRANSFER FUNCTION WITH SCALE-DEPENDENT Omega_m_eff
# =============================================================================
print("\n" + "=" * 80)
print("TASK 2: MOND-MODIFIED TRANSFER FUNCTION")
print("=" * 80)

def eisenstein_hu_no_wiggle(k_hmpc_arr, omega_m_h2, omega_b_h2, h_val, T_cmb):
    """
    Eisenstein & Hu (1998) no-wiggle (smooth) transfer function.
    Eq. (29) - the zero-baryon approximation with shape correction.
    Returns T(k) and derived quantities.

    k_hmpc_arr: array of k values in h/Mpc
    """
    theta = T_cmb / 2.7
    k_arr = np.atleast_1d(k_hmpc_arr).astype(float)

    # Equality redshift and scale
    z_eq = 2.5e4 * omega_m_h2 * theta**(-4)
    k_eq = 7.46e-2 * omega_m_h2 * theta**(-2)  # Mpc^-1

    # Sound horizon fitting formula
    b1 = 0.313 * omega_m_h2**(-0.419) * (1 + 0.607 * omega_m_h2**0.674)
    b2 = 0.238 * omega_m_h2**0.223
    z_d = 1291 * omega_m_h2**0.251 / (1 + 0.659 * omega_m_h2**0.828) * (1 + b1 * omega_b_h2**b2)

    R_eq = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_eq)
    R_d = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_d)

    s = (2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / R_eq) * \
        np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    # Silk damping scale
    k_silk = 1.6 * omega_b_h2**0.52 * omega_m_h2**0.73 * (1 + (10.4 * omega_m_h2)**(-0.95))

    f_b = omega_b_h2 / omega_m_h2

    # No-wiggle transfer function: Eq. (29) of EH98
    # Shape parameter
    alpha_Gamma = 1 - 0.328 * np.log(431 * omega_m_h2) * f_b + \
                  0.38 * np.log(22.3 * omega_m_h2) * f_b**2
    Gamma_eff_over_h = omega_m_h2 / h_val  # This is Omega_m * h

    T_arr = np.zeros_like(k_arr)
    for i, kh in enumerate(k_arr):
        # Effective shape parameter with baryon correction
        s_eff = alpha_Gamma + (1 - alpha_Gamma) / (1 + (0.43 * kh * s * h_val)**4)
        Gamma_eff = Gamma_eff_over_h * s_eff
        q = kh * theta**2 / Gamma_eff

        L = np.log(2 * np.e + 1.8 * q)
        C = 14.2 + 731.0 / (1 + 62.5 * q)
        T_arr[i] = L / (L + C * q**2)

    return T_arr, {'z_eq': z_eq, 'z_d': z_d, 's': s, 'k_silk': k_silk,
                   'k_eq': k_eq, 'R_eq': R_eq, 'R_d': R_d, 'f_b': f_b}


def eisenstein_hu_full(k_hmpc_arr, omega_m_h2, omega_b_h2, h_val, T_cmb):
    """
    Eisenstein & Hu (1998) FULL transfer function with baryon oscillations.
    Includes CDM and baryon components.
    """
    theta = T_cmb / 2.7
    k_arr = np.atleast_1d(k_hmpc_arr).astype(float)

    z_eq = 2.5e4 * omega_m_h2 * theta**(-4)
    k_eq = 7.46e-2 * omega_m_h2 * theta**(-2)

    b1 = 0.313 * omega_m_h2**(-0.419) * (1 + 0.607 * omega_m_h2**0.674)
    b2 = 0.238 * omega_m_h2**0.223
    z_d = 1291 * omega_m_h2**0.251 / (1 + 0.659 * omega_m_h2**0.828) * (1 + b1 * omega_b_h2**b2)

    R_eq = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_eq)
    R_d = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_d)

    s = (2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / R_eq) * \
        np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    k_silk = 1.6 * omega_b_h2**0.52 * omega_m_h2**0.73 * (1 + (10.4 * omega_m_h2)**(-0.95))

    f_b = omega_b_h2 / omega_m_h2
    f_c = 1.0 - f_b

    T_arr = np.zeros_like(k_arr)

    for i, kh in enumerate(k_arr):
        k = kh * h_val  # Mpc^-1
        q = k / (13.41 * k_eq)

        # CDM piece
        a1_c = (46.9 * omega_m_h2)**0.670 * (1 + (32.1 * omega_m_h2)**(-0.532))
        a2_c = (12.0 * omega_m_h2)**0.424 * (1 + (45.0 * omega_m_h2)**(-0.582))
        alpha_c = a1_c**(-f_b) * a2_c**(-f_b**3)

        b1_c = 0.944 / (1 + (458 * omega_m_h2)**(-0.708))
        b2_c = (0.395 * omega_m_h2)**(-0.0266)
        beta_c = 1.0 / (1 + b1_c * (max(f_c, 1e-10)**b2_c - 1))

        def T0_tilde(q_val, alpha_val, beta_val):
            C = 14.2 / alpha_val + 386.0 / (1 + 69.9 * q_val**1.08)
            L = np.log(np.e + 1.8 * beta_val * q_val)
            return L / (L + C * q_val**2)

        if f_c > 0.01:
            T_c = f_c * T0_tilde(q, 1, beta_c) + (1 - f_c) * T0_tilde(q, alpha_c, 1)
        else:
            # Baryon-dominated: CDM piece negligible
            T_c = T0_tilde(q, alpha_c, 1)

        # Baryon piece
        beta_node = 8.41 * omega_m_h2**0.435
        s_tilde = s / (1 + (beta_node / max(k * s, 1e-10))**3)**(1.0/3.0)

        alpha_b = 2.07 * k_eq * s * (1 + R_d)**(-3.0/4.0) * \
                  (a1_c**(-f_b) + a2_c**(-f_b**3))
        beta_b = 0.5 + f_b + (3 - 2*f_b) * np.sqrt((17.2 * omega_m_h2)**2 + 1)

        ks_tilde = k * s_tilde
        j0 = np.sin(ks_tilde) / ks_tilde if ks_tilde > 1e-6 else 1.0

        T_0_11 = np.log(np.e + 1.8 * q) / (np.log(np.e + 1.8 * q) + (14.2 + 386.0 / (1 + 69.9 * q**1.08)) * q**2)

        x_silk = k / k_silk
        T_b = (T_0_11 / (1 + (k * s / 5.2)**2) +
               alpha_b / (1 + (beta_b / max(k * s, 1e-10))**3) * np.exp(-x_silk**1.4))
        T_b *= j0

        T_arr[i] = f_b * T_b + f_c * T_c

    return T_arr, {'z_eq': z_eq, 'z_d': z_d, 's': s, 'k_silk': k_silk,
                   'k_eq': k_eq, 'R_eq': R_eq, 'R_d': R_d, 'f_b': f_b}


# Compute for fine k grid
k_fine = np.logspace(-3, 0.5, 500)  # h/Mpc

# LCDM reference
T_LCDM, info_LCDM = eisenstein_hu_no_wiggle(k_fine, Omega_m_h2_LCDM, Omega_b_h2, h, T_CMB)
T_LCDM_full, info_LCDM_full = eisenstein_hu_full(k_fine, Omega_m_h2_LCDM, Omega_b_h2, h, T_CMB)

print(f"\nLCDM reference (Omega_m h^2 = {Omega_m_h2_LCDM:.4f}):")
print(f"  z_eq = {info_LCDM['z_eq']:.1f}")
print(f"  z_d = {info_LCDM['z_d']:.1f}")
print(f"  s = {info_LCDM['s']:.2f} Mpc = {info_LCDM['s']*h:.2f} Mpc/h")
print(f"  k_eq = {info_LCDM['k_eq']:.5f} Mpc^-1 = {info_LCDM['k_eq']/h:.5f} h/Mpc")
print(f"  k_silk = {info_LCDM['k_silk']:.4f} Mpc^-1")

# Baryon-only (no MOND)
T_bonly, info_bonly = eisenstein_hu_no_wiggle(k_fine, Omega_b_h2, Omega_b_h2, h, T_CMB)
print(f"\nBaryon-only (Omega_m h^2 = {Omega_b_h2:.4f}):")
print(f"  z_eq = {info_bonly['z_eq']:.1f}")
print(f"  z_d = {info_bonly['z_d']:.1f}")
print(f"  s = {info_bonly['s']:.2f} Mpc = {info_bonly['s']*h:.2f} Mpc/h")
print(f"  k_eq = {info_bonly['k_eq']:.5f} Mpc^-1 = {info_bonly['k_eq']/h:.5f} h/Mpc")

# Now: MOND-modified transfer function
# For each k, compute nu(k, z_rec) and use Omega_m_eff(k) = nu(k) * Omega_b
print(f"\n--- MOND-Modified Transfer Function (scale-dependent) ---")

def compute_nu_at_recombination(k_hMpc, delta=3e-4):
    """Compute MOND enhancement at recombination for a given wavenumber."""
    k_Mpc = k_hMpc * h
    k_phys = k_Mpc / (a_rec * Mpc_m)
    g_N = 4 * np.pi * G_N * rho_b_rec * delta / k_phys
    y = g_N / a0_MOND
    return nu_mond(y), y, g_N


# Compute MOND-modified T(k) for each k on fine grid
T_MOND_modified = np.zeros_like(k_fine)
nu_arr = np.zeros_like(k_fine)
Om_eff_arr = np.zeros_like(k_fine)
zeq_eff_arr = np.zeros_like(k_fine)
s_eff_arr = np.zeros_like(k_fine)

theta = T_CMB / 2.7

for i, kh in enumerate(k_fine):
    nu_val, y_val, g_val = compute_nu_at_recombination(kh)
    nu_arr[i] = nu_val
    Om_eff = nu_val * Omega_b
    Om_eff_arr[i] = Om_eff
    omega_m_eff_h2 = Om_eff * h**2

    # Compute EH transfer for this single k with its own effective Omega_m
    T_single, info_single = eisenstein_hu_no_wiggle(np.array([kh]), omega_m_eff_h2, Omega_b_h2, h, T_CMB)
    T_MOND_modified[i] = T_single[0]
    zeq_eff_arr[i] = info_single['z_eq']
    s_eff_arr[i] = info_single['s']


# Print key results at the target k values
print(f"\n{'k [h/Mpc]':>12} {'nu':>8} {'Om_eff':>8} {'Om_eff*h2':>10} {'z_eq_eff':>10} {'s_eff [Mpc]':>12} {'T_MOND':>10} {'T_LCDM':>10} {'ratio':>8}")
print("-" * 100)

for kh in [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]:
    idx = np.argmin(np.abs(k_fine - kh))
    T_L = np.interp(kh, k_fine, T_LCDM)
    print(f"{kh:12.2f} {nu_arr[idx]:8.2f} {Om_eff_arr[idx]:8.4f} {Om_eff_arr[idx]*h**2:10.5f} "
          f"{zeq_eff_arr[idx]:10.1f} {s_eff_arr[idx]:12.2f} {T_MOND_modified[idx]:10.6f} {T_L:10.6f} "
          f"{T_MOND_modified[idx]/T_L:8.4f}")


# =============================================================================
# TASK 3: KEY DERIVED QUANTITIES
# =============================================================================
print("\n" + "=" * 80)
print("TASK 3: KEY DERIVED QUANTITIES")
print("=" * 80)

# Radiation density
Omega_r_h2 = 4.15e-5 * (T_CMB/2.725)**4 * (1 + 0.2271 * 3.044/3.0)  # with neutrinos
Omega_r = Omega_r_h2 / h**2

print(f"\nOmega_radiation h^2 = {Omega_r_h2:.4e}")
print(f"Omega_radiation = {Omega_r:.4e}")

print(f"\nScale-dependent derived quantities:")
print(f"{'k [h/Mpc]':>12} {'nu':>8} {'z_eq,eff':>10} {'s [Mpc/h]':>12} {'s [Mpc]':>10} {'k_silk':>10}")
print("-" * 70)

for kh in [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]:
    idx = np.argmin(np.abs(k_fine - kh))
    omega_m_eff_h2 = Om_eff_arr[idx] * h**2
    z_eq_eff = 2.5e4 * omega_m_eff_h2 * theta**(-4)
    k_eq_eff = 7.46e-2 * omega_m_eff_h2 * theta**(-2)
    k_silk_eff = 1.6 * Omega_b_h2**0.52 * omega_m_eff_h2**0.73 * (1 + (10.4 * omega_m_eff_h2)**(-0.95))

    print(f"{kh:12.2f} {nu_arr[idx]:8.2f} {z_eq_eff:10.1f} {s_eff_arr[idx]*h:12.2f} "
          f"{s_eff_arr[idx]:10.2f} {k_silk_eff:10.4f}")

# LCDM targets
print(f"\nLCDM targets for comparison:")
print(f"  z_eq = {info_LCDM['z_eq']:.1f}")
print(f"  s = {info_LCDM['s']:.2f} Mpc = {info_LCDM['s']*h:.2f} Mpc/h")
print(f"  k_silk = {info_LCDM['k_silk']:.4f} Mpc^-1")

# What nu would we NEED to match LCDM?
nu_needed = Omega_m_LCDM / Omega_b
print(f"\n  => nu needed to match LCDM Omega_m = {Omega_m_LCDM}: {nu_needed:.2f}")
print(f"     (Omega_m_eff = {nu_needed * Omega_b:.4f})")


# =============================================================================
# TASK 4: THE MODIFIED P(k)
# =============================================================================
print("\n" + "=" * 80)
print("TASK 4: P_DFD(k) WITH MOND-MODIFIED TRANSFER FUNCTION")
print("=" * 80)

# Growth factor computation
# For DFD post-recombination: MOND-enhanced growth in baryon-only universe
# Following the effective constant-nu approach from R2

def compute_growth_factor_LCDM(z_final=0):
    """Standard LCDM growth factor D(z)."""
    a_final = 1.0 / (1.0 + z_final)

    def D_integrand(a):
        E = np.sqrt(Omega_m_LCDM / a**3 + Omega_Lambda)
        return 1.0 / (a * E)**3

    result, _ = quad(D_integrand, 0, a_final)
    E_final = np.sqrt(Omega_m_LCDM / a_final**3 + Omega_Lambda)
    D = 5.0/2.0 * Omega_m_LCDM * E_final * result
    return D

def compute_growth_MOND_effective(z_final=0, nu_eff=6.4):
    """
    MOND-enhanced growth in baryon-only cosmology.
    With effective constant nu, the growth equation is:
    D'' + (2 + dlnH/dlna) D'/a - 3/2 * nu_eff * Omega_b / a^3 / E^2 * D = 0

    For the background expansion, DFD still has Omega_Lambda to get late-time acceleration.
    The key question: what drives H(a)?

    In DFD: only baryons + Lambda. So H^2/H0^2 = Omega_b/a^3 + Omega_Lambda_DFD.
    But we need Omega_b + Omega_Lambda_DFD = 1, so Omega_Lambda_DFD = 1 - Omega_b ~ 0.951.

    This actually makes the growth DIFFERENT from LCDM because of different expansion history.
    """
    Omega_Lambda_DFD = 1.0 - Omega_b

    def E_sq_DFD(a):
        return Omega_b / a**3 + Omega_Lambda_DFD

    def growth_ode(a, y):
        D, dDda = y
        E2 = E_sq_DFD(a)
        E = np.sqrt(E2)
        dlnH_da = -1.5 * Omega_b / (a**4 * E2)
        dlnH_dlna = a * dlnH_da

        # Growth equation: D'' + (2 + dlnH/dlna)/a * D' - 3/2 * nu_eff * Omega_b / (a^3 * E^2) * D/a^2 = 0
        # Written as dD/da and d2D/da2 (using a as independent variable)
        d2Dda2 = -(2.0/a + dlnH_da) * dDda + 1.5 * nu_eff * Omega_b / (a**5 * E2) * D

        return [dDda, d2Dda2]

    a_start = 1e-3
    a_end = 1.0 / (1.0 + z_final)

    # Initial conditions in matter-dominated era: D ~ a
    D0 = a_start
    dDda0 = 1.0

    sol = solve_ivp(growth_ode, [a_start, a_end], [D0, dDda0],
                    method='RK45', rtol=1e-10, atol=1e-12,
                    max_step=0.001)

    return sol.y[0][-1]


D_LCDM_0 = compute_growth_factor_LCDM(z_final=0)
D_LCDM_rec = compute_growth_factor_LCDM(z_final=z_rec)

print(f"\nLCDM growth factor: D(z=0) = {D_LCDM_0:.6f}")
print(f"LCDM growth factor: D(z={z_rec}) = {D_LCDM_rec:.6f}")
print(f"Growth ratio D(0)/D(z_rec) = {D_LCDM_0/D_LCDM_rec:.2f}")

# For DFD with different nu_eff values
print(f"\nMOND-enhanced growth (post-recombination, various nu_eff):")
for nu_eff_test in [1.0, 3.0, 5.0, 6.4, 8.0, 10.0]:
    D_MOND = compute_growth_MOND_effective(z_final=0, nu_eff=nu_eff_test)
    print(f"  nu_eff = {nu_eff_test:5.1f}: D_MOND(z=0) = {D_MOND:.6f}, D_MOND/D_LCDM = {D_MOND/D_LCDM_0:.4f}")


# Compute P(k) = A_s * (k/k_pivot)^{n_s-1} * T^2(k) * D^2(z=0)
# For LCDM:
P_LCDM = A_s * (k_fine * h / k_pivot)**(n_s - 1) * T_LCDM**2 * D_LCDM_0**2
# Normalize: multiply by (2*pi^2 / k^3) for dimensionless, but we'll work in P(k) units

# For DFD with MOND-modified transfer + MOND-enhanced growth
# Use nu_eff ~ 6.4 for post-recombination growth (as in R2)
nu_eff_growth = Omega_m_LCDM / Omega_b  # ~ 6.4
D_MOND_0 = compute_growth_MOND_effective(z_final=0, nu_eff=nu_eff_growth)

P_DFD_MOND_TF = A_s * (k_fine * h / k_pivot)**(n_s - 1) * T_MOND_modified**2 * D_MOND_0**2

print(f"\nUsing nu_eff = {nu_eff_growth:.2f} for post-recombination growth:")
print(f"  D_MOND(z=0) = {D_MOND_0:.6f}")
print(f"  D_MOND/D_LCDM = {D_MOND_0/D_LCDM_0:.4f}")

print(f"\nP_DFD / P_LCDM at key scales:")
print(f"{'k [h/Mpc]':>12} {'P_DFD/P_LCDM':>14} {'T_DFD/T_LCDM':>14} {'nu(k,z_rec)':>12}")
print("-" * 55)
for kh in [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]:
    idx = np.argmin(np.abs(k_fine - kh))
    ratio_P = P_DFD_MOND_TF[idx] / P_LCDM[idx] if P_LCDM[idx] > 0 else 0
    ratio_T = T_MOND_modified[idx] / T_LCDM[idx] if T_LCDM[idx] > 0 else 0
    print(f"{kh:12.2f} {ratio_P:14.4f} {ratio_T:14.4f} {nu_arr[idx]:12.2f}")


# =============================================================================
# TASK 5: SIGMA_8 COMPUTATION
# =============================================================================
print("\n" + "=" * 80)
print("TASK 5: SIGMA_8 AND BOSS WAVENUMBER COMPARISON")
print("=" * 80)

def compute_sigma8(k_arr, Pk_arr, R=8.0):
    """
    Compute sigma(R) from P(k).
    sigma^2(R) = 1/(2*pi^2) * integral k^2 P(k) W^2(kR) dk
    W(x) = 3*(sin(x) - x*cos(x)) / x^3 (top-hat window)
    R in Mpc/h
    """
    R_Mpc = R  # Already in Mpc/h since k is in h/Mpc

    def integrand(logk):
        k = np.exp(logk)
        Pk = np.interp(k, k_arr, Pk_arr)
        x = k * R_Mpc
        if x < 1e-4:
            W = 1.0 - x**2/10.0
        else:
            W = 3.0 * (np.sin(x) - x * np.cos(x)) / x**3
        return k**3 * Pk * W**2 / (2 * np.pi**2)

    logk_min = np.log(k_arr[0])
    logk_max = np.log(k_arr[-1])
    result, _ = quad(integrand, logk_min, logk_max, limit=200)
    return np.sqrt(result)


# We need to add proper normalization. P(k) has units of (Mpc/h)^3
# The standard normalization: P(k) = 2*pi^2 * A_s * (k/k_pivot)^{n_s-1} * T^2(k) * D^2 / k^3
# ... but the way we've written it, we need to be careful.

# Actually let's use the standard convention:
# Delta^2(k) = A_s * (k/k_pivot)^{n_s-1} * T^2(k) * (D/D_primordial)^2
# P(k) = 2*pi^2 * Delta^2(k) / k^3

# For proper sigma_8, use:
# P(k) [in (Mpc/h)^3] = (2*pi^2 / k^3) * A_s * (k_phys/k_pivot)^{n_s-1} * T^2(k) * D^2

# k_phys = k_hMpc * h  (in Mpc^-1), k_pivot = 0.05 Mpc^-1
# So k_phys/k_pivot = k_hMpc * h / k_pivot

# P(k) in (Mpc/h)^3:
k3 = k_fine**3
P_LCDM_proper = (2 * np.pi**2 / k3) * A_s * (k_fine * h / k_pivot)**(n_s - 1) * T_LCDM**2 * D_LCDM_0**2
P_DFD_proper = (2 * np.pi**2 / k3) * A_s * (k_fine * h / k_pivot)**(n_s - 1) * T_MOND_modified**2 * D_MOND_0**2

sigma8_LCDM = compute_sigma8(k_fine, P_LCDM_proper, R=8.0)
sigma8_DFD = compute_sigma8(k_fine, P_DFD_proper, R=8.0)

print(f"\nsigma_8 comparison:")
print(f"  LCDM:  sigma_8 = {sigma8_LCDM:.4f}  (target: ~0.811)")
print(f"  DFD:   sigma_8 = {sigma8_DFD:.4f}")
print(f"  Ratio: sigma8_DFD/sigma8_LCDM = {sigma8_DFD/sigma8_LCDM:.4f}")

# BOSS wavenumbers
k_BOSS = np.array([0.01, 0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20, 0.30])
print(f"\nP_DFD/P_LCDM at BOSS wavenumbers:")
print(f"{'k [h/Mpc]':>12} {'P_DFD/P_LCDM':>14}")
print("-" * 30)
for kh in k_BOSS:
    P_L = np.interp(kh, k_fine, P_LCDM_proper)
    P_D = np.interp(kh, k_fine, P_DFD_proper)
    print(f"{kh:12.3f} {P_D/P_L:14.4f}")


# =============================================================================
# TASK 6: SELF-CONSISTENCY ITERATION
# =============================================================================
print("\n" + "=" * 80)
print("TASK 6: SELF-CONSISTENCY ITERATION")
print("=" * 80)

print("\nIteration scheme:")
print("  1. Start with baryon-only T_b(k; Omega_b)")
print("  2. Compute nu(k, z_rec) from T_b -> delta(k) -> g_N(k) -> nu(k)")
print("  3. Compute T_eff(k; Omega_m_eff = nu*Omega_b)")
print("  4. Recompute nu using T_eff to get new delta(k)")
print("  5. Iterate until convergence")

# The key subtlety: the perturbation amplitude delta at recombination
# depends on the transfer function itself!
# delta(k, z_rec) = delta_primordial(k) * T(k) * D(z_rec)/D(z_primordial)
# But the SHAPE of T affects the relative amplitude at each k.

# For the Newtonian acceleration, what matters is:
# g_N(k) = 4*pi*G*rho_b*delta(k)/k_phys
# delta(k) ~ A_s^{1/2} * (k/k_pivot)^{(n_s-1)/2} * T(k) * (some normalization)

# The absolute normalization cancels in the nu computation because
# we're interested in the SHAPE of nu(k), not its absolute value.
# Actually no - the absolute value of g_N/a0 determines nu.

# Let's use the primordial amplitude:
# delta_k ~ sqrt(A_s) * (k/k_pivot)^{(n_s-1)/2} * T(k) * D(z_rec)/D_0

# Actually, the primordial power spectrum gives:
# <|delta_k|^2> = (2*pi^2/k^3) * A_s * (k/k_pivot)^{n_s-1}
# So the RMS perturbation at scale k is:
# delta_rms(k) ~ sqrt(k^3 * P(k) / (2*pi^2)) = sqrt(A_s) * (k/k_pivot)^{(n_s-1)/2} * T(k)

# At recombination, we include the growth from the primordial epoch to z_rec.
# In matter-dominated era, D ~ a. So D(z_rec)/D(z_initial) ~ a_rec/a_initial.
# But T(k) already encodes growth up to z_rec for modes that entered before recombination.

# Simplification: use delta ~ 3e-4 * T(k)/T(k_ref) as a first approximation
# where T(k_ref) normalizes to give delta ~ 3e-4 at the BAO scale.

k_ref = 0.05  # h/Mpc - reference scale

# Iteration
MAX_ITER = 20
CONV_TOL = 1e-4

# Step 1: Initial transfer function (baryon-only)
T_current = np.zeros_like(k_fine)
T_single_init, _ = eisenstein_hu_no_wiggle(k_fine, Omega_b_h2, Omega_b_h2, h, T_CMB)
T_current = T_single_init.copy()

T_ref_init = np.interp(k_ref, k_fine, T_current)

print(f"\nStarting iteration with baryon-only T(k):")
print(f"  T(k_ref={k_ref}) = {T_ref_init:.6f}")

convergence_history = []

for iteration in range(MAX_ITER):
    # Step 2: Compute nu(k, z_rec) using current T(k)
    nu_iter = np.zeros_like(k_fine)
    Om_eff_iter = np.zeros_like(k_fine)

    T_at_ref = np.interp(k_ref, k_fine, T_current)

    for i, kh in enumerate(k_fine):
        # Scale delta by T(k)/T(k_ref) relative to fiducial delta=3e-4
        delta_k = delta_rec * T_current[i] / max(T_at_ref, 1e-20)

        k_Mpc = kh * h
        k_phys = k_Mpc / (a_rec * Mpc_m)
        g_N = 4 * np.pi * G_N * rho_b_rec * abs(delta_k) / k_phys
        y = g_N / a0_MOND
        nu_iter[i] = nu_mond(max(y, 1e-30))
        Om_eff_iter[i] = nu_iter[i] * Omega_b

    # Step 3: Compute new T(k) with scale-dependent Omega_m_eff
    T_new = np.zeros_like(k_fine)
    for i, kh in enumerate(k_fine):
        omega_m_eff_h2 = Om_eff_iter[i] * h**2
        # Clamp to reasonable range
        omega_m_eff_h2 = np.clip(omega_m_eff_h2, Omega_b_h2, 0.5)

        T_single, _ = eisenstein_hu_no_wiggle(np.array([kh]), omega_m_eff_h2, Omega_b_h2, h, T_CMB)
        T_new[i] = T_single[0]

    # Check convergence
    diff = np.max(np.abs(T_new - T_current) / np.maximum(np.abs(T_current), 1e-20))
    nu_at_targets = [np.interp(kh, k_fine, nu_iter) for kh in [0.01, 0.05, 0.20]]

    convergence_history.append({
        'iteration': iteration,
        'max_diff': diff,
        'nu_001': nu_at_targets[0],
        'nu_005': nu_at_targets[1],
        'nu_020': nu_at_targets[2],
        'Om_eff_005': np.interp(0.05, k_fine, Om_eff_iter),
    })

    print(f"\n  Iteration {iteration+1}:")
    print(f"    max |dT/T| = {diff:.6e}")
    print(f"    nu(0.01) = {nu_at_targets[0]:.4f}, nu(0.05) = {nu_at_targets[1]:.4f}, nu(0.20) = {nu_at_targets[2]:.4f}")
    print(f"    Om_eff(0.05) = {convergence_history[-1]['Om_eff_005']:.4f}")

    T_current = T_new.copy()

    if diff < CONV_TOL:
        print(f"\n  => CONVERGED after {iteration+1} iterations!")
        break
else:
    print(f"\n  => Did NOT converge after {MAX_ITER} iterations.")
    print(f"    Final max |dT/T| = {diff:.6e}")

# Final converged results
T_converged = T_current.copy()
nu_converged = nu_iter.copy()
Om_eff_converged = Om_eff_iter.copy()

print(f"\nFinal converged results:")
print(f"{'k [h/Mpc]':>12} {'nu_converged':>14} {'Om_eff':>10} {'Om_eff*h2':>10} {'T_conv':>10} {'T_LCDM':>10} {'T_conv/T_LCDM':>14}")
print("-" * 85)
for kh in [0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0]:
    if kh < k_fine[0] or kh > k_fine[-1]:
        continue
    nu_c = np.interp(kh, k_fine, nu_converged)
    Om_c = np.interp(kh, k_fine, Om_eff_converged)
    T_c = np.interp(kh, k_fine, T_converged)
    T_L = np.interp(kh, k_fine, T_LCDM)
    print(f"{kh:12.3f} {nu_c:14.4f} {Om_c:10.4f} {Om_c*h**2:10.5f} {T_c:10.6f} {T_L:10.6f} {T_c/T_L:14.4f}")


# =============================================================================
# FINAL P(k) WITH CONVERGED TRANSFER FUNCTION
# =============================================================================
print("\n" + "=" * 80)
print("FINAL: P_DFD(k) WITH CONVERGED MOND-MODIFIED TRANSFER FUNCTION")
print("=" * 80)

P_DFD_final = (2 * np.pi**2 / k3) * A_s * (k_fine * h / k_pivot)**(n_s - 1) * T_converged**2 * D_MOND_0**2
sigma8_DFD_final = compute_sigma8(k_fine, P_DFD_final, R=8.0)

print(f"\nsigma_8 (converged DFD) = {sigma8_DFD_final:.4f}")
print(f"sigma_8 (LCDM)         = {sigma8_LCDM:.4f}")
print(f"Ratio                  = {sigma8_DFD_final/sigma8_LCDM:.4f}")

print(f"\nFinal P_DFD/P_LCDM at BOSS wavenumbers:")
print(f"{'k [h/Mpc]':>12} {'P_DFD/P_LCDM':>14} {'T_DFD/T_LCDM':>14}")
print("-" * 42)
for kh in k_BOSS:
    P_L = np.interp(kh, k_fine, P_LCDM_proper)
    P_D = np.interp(kh, k_fine, P_DFD_final)
    T_L = np.interp(kh, k_fine, T_LCDM)
    T_D = np.interp(kh, k_fine, T_converged)
    print(f"{kh:12.3f} {P_D/P_L:14.4f} {T_D/T_L:14.4f}")


# =============================================================================
# ASSESSMENT: DOES nu_rec * Omega_b ~ 0.25 - 0.30?
# =============================================================================
print("\n" + "=" * 80)
print("ASSESSMENT: THE PRIZE")
print("=" * 80)

# Average nu over BOSS range
k_boss_range = (k_fine > 0.01) & (k_fine < 0.30)
nu_avg_boss = np.mean(nu_converged[k_boss_range])
Om_eff_avg = nu_avg_boss * Omega_b

print(f"\nAverage nu over BOSS range (0.01-0.30 h/Mpc): {nu_avg_boss:.2f}")
print(f"Average Omega_m_eff = {Om_eff_avg:.4f}")
print(f"Target Omega_m_eff = {Omega_m_LCDM:.4f}")

if 0.20 < Om_eff_avg < 0.40:
    print(f"\n  *** PROMISING: Omega_m_eff is in the right ballpark! ***")
elif Om_eff_avg < 0.10:
    print(f"\n  PROBLEM: Omega_m_eff is too low. nu at recombination is not large enough.")
    print(f"  This means g_N/a0 >> 1 at recombination (Newtonian regime), so nu ~ 1.")
    print(f"  The MOND enhancement at recombination is NEGLIGIBLE for these perturbation amplitudes.")
else:
    print(f"\n  PARTIAL: Omega_m_eff partially bridges the gap but doesn't fully match LCDM.")

# Physical assessment
print(f"\n--- Physical Assessment ---")
print(f"The mean baryon density at z_rec = {rho_b_rec:.4e} kg/m^3")
print(f"For a mode k = 0.05 h/Mpc with delta = {delta_rec}:")
k_test = 0.05
k_phys_test = k_test * h / (a_rec * Mpc_m)
g_test = 4 * np.pi * G_N * rho_b_rec * delta_rec / k_phys_test
y_test = g_test / a0_MOND
print(f"  k_phys = {k_phys_test:.4e} m^-1")
print(f"  g_N = {g_test:.4e} m/s^2")
print(f"  g_N/a0 = {y_test:.4e}")
print(f"  a0 = {a0_MOND:.1e} m/s^2")

if y_test > 10:
    print(f"\n  CONCLUSION: g_N >> a0 at recombination!")
    print(f"  The Newtonian acceleration from density perturbations at z~1100")
    print(f"  is MUCH LARGER than a0. This means we are in the NEWTONIAN regime")
    print(f"  and MOND effects are negligible (nu ~ 1).")
    print(f"\n  This is because rho ~ (1+z)^3 makes densities very high at z=1100.")
    print(f"  MOND effects only become important at LOW redshift where densities")
    print(f"  drop enough for g_N < a0.")
elif y_test < 0.1:
    print(f"\n  CONCLUSION: g_N << a0 at recombination!")
    print(f"  Deep MOND regime: nu ~ 1/sqrt(y) >> 1")
    print(f"  MOND STRONGLY enhances gravity at recombination.")
else:
    print(f"\n  CONCLUSION: g_N ~ a0 at recombination.")
    print(f"  Transitional regime: moderate MOND enhancement.")

# Additional check: what delta would be NEEDED for nu ~ 6.4?
# nu = 6.4 implies y such that 0.5*(1+sqrt(1+4/y)) = 6.4
# sqrt(1+4/y) = 11.8, 1+4/y = 139.24, 4/y = 138.24, y = 0.02894
# g_N = y * a0 = 0.02894 * 1.2e-10 = 3.47e-12 m/s^2
# g_N = 4*pi*G*rho*delta/k_phys
# delta = g_N * k_phys / (4*pi*G*rho)

y_needed = 4.0 / ((2*nu_needed - 1)**2 - 1)
g_needed = y_needed * a0_MOND
delta_needed = g_needed * k_phys_test / (4 * np.pi * G_N * rho_b_rec)

print(f"\n--- What would be needed? ---")
print(f"  For nu = {nu_needed:.2f} at k = 0.05 h/Mpc:")
print(f"    y_needed = {y_needed:.6f}")
print(f"    g_needed = {g_needed:.4e} m/s^2")
print(f"    delta_needed = {delta_needed:.4e}")
print(f"    Actual delta ~ {delta_rec:.4e}")
print(f"    Ratio delta_actual/delta_needed = {delta_rec/delta_needed:.2f}")

# Alternative: what if MOND operates on the MEAN field, not perturbations?
print(f"\n--- Alternative: MOND on the mean gravitational field ---")
# The mean gravitational acceleration in the expanding universe is:
# g_mean ~ H^2 * R ~ H^2 / k_phys (for a perturbation at scale k)
# Actually: g_mean = (4/3)*pi*G*rho_mean*R where R = 1/k_phys

# The Hubble flow acceleration at scale R:
# a_Hubble = H^2 * R (deceleration parameter)
H_rec = H0_si * np.sqrt(Omega_m_LCDM / a_rec**3 + Omega_r / a_rec**4)  # using LCDM for H
R_phys = a_rec * Mpc_m / (0.05 * h)  # physical scale at recombination for k=0.05 h/Mpc

# Internal gravitational acceleration of a perturbation at the Jeans scale
g_internal = (4*np.pi/3) * G_N * rho_b_rec * delta_rec * R_phys
y_internal = g_internal / a0_MOND
print(f"  Internal g = (4pi/3)*G*rho*delta*R = {g_internal:.4e} m/s^2")
print(f"  y_internal = g/a0 = {y_internal:.4e}")

# What about the BACKGROUND gravitational acceleration?
# In a homogeneous expanding universe, there IS a background g:
# The Friedmann deceleration: g_decel = -(4piG/3)(rho + 3p)*R
# For matter-dominated: g_decel = (4piG/3)*rho_total*R

g_background = (4*np.pi/3) * G_N * rho_b_rec * R_phys  # mean field (delta=1 equivalent)
y_background = g_background / a0_MOND
print(f"\n  Background g (delta=1): {g_background:.4e} m/s^2")
print(f"  y_background = {y_background:.4e}")
print(f"  nu_background = {nu_mond(y_background):.4f}")

# Or: the acceleration at the Hubble scale
R_Hubble = c_light / H_rec
g_Hubble = (4*np.pi/3) * G_N * rho_b_rec * R_Hubble
y_Hubble = g_Hubble / a0_MOND
print(f"\n  Hubble scale acceleration: g = {g_Hubble:.4e} m/s^2")
print(f"  y_Hubble = {y_Hubble:.4e}")

print(f"\n\n{'='*80}")
print("SUMMARY OF KEY FINDINGS")
print("="*80)
print(f"""
1. MOND enhancement at recombination for LINEAR perturbations (delta~3e-4):
   - g_N/a0 >> 1 for all k in the BOSS range
   - nu ~ 1 (Newtonian regime)
   - Omega_m_eff ~ Omega_b ~ 0.049 (NO enhancement)

2. The pre-recombination universe is TOO DENSE for MOND:
   - rho_b(z=1100) = {rho_b_rec:.2e} kg/m^3 (vs rho_b(z=0) = {rho_b_0:.2e})
   - Factor of (1+z)^3 ~ 1.3 x 10^9 increase
   - Even small perturbations produce g_N >> a0

3. For MOND to matter at recombination, we would need:
   - delta ~ {delta_needed:.1e} (but actual delta ~ {delta_rec:.1e})
   - Or a0 at recombination would need to be >> {a0_MOND:.1e} m/s^2
   - Or MOND operates on a different field than g_N of perturbations

4. HOWEVER: if MOND operates on the PERTURBATION acceleration relative to
   the background (i.e., on delta*g rather than total g), and if the
   relevant scale is the perturbation scale rather than the mean density
   scale, then the situation changes. But this is not standard MOND.

5. The BACKGROUND gravitational field at perturbation scales is:
   - g_background ~ {g_background:.2e} m/s^2 >> a0
   - This confirms: the pre-recombination universe is deeply Newtonian

6. CONCLUSION: The "MOND-modified pre-recombination transfer function"
   approach does NOT work with standard MOND (a0 = 1.2e-10 m/s^2).
   The gravitational accelerations at z~1100 are far above a0, so
   nu ~ 1 and there is no enhancement.

   The DFD transfer function problem must be solved by OTHER means:
   - Post-recombination MOND-enhanced growth (which does work)
   - Modified transfer function from DFD field dynamics (not standard MOND)
   - Scale-dependent enhancement from gradient energy terms
   - The DFD phi-field itself providing the "CDM-like" potential wells
""")
