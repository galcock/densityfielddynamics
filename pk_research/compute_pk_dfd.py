#!/usr/bin/env python3
"""
Agent 14: Rigorous computation of P_DFD(k) for Density Field Dynamics.
Computes:
  1. Eisenstein-Hu baryon-only transfer function T_b(k)
  2. MOND enhancement factor nu(k,z)
  3. Self-consistent nonlinear growth factor D_DFD(k,z)
  4. Final P_DFD(k) and comparison with LCDM
"""

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import interp1d

# ============================================================
# COSMOLOGICAL PARAMETERS
# ============================================================
h = 0.674
Omega_b_h2 = 0.02237
Omega_b = Omega_b_h2 / h**2  # baryon-only universe
Omega_m_h2 = Omega_b_h2       # no CDM!
Omega_m = Omega_b              # baryon = total matter
T_CMB = 2.725                  # K
n_s = 0.9649
A_s = 2.1e-9
k_pivot = 0.05  # Mpc^-1

# MOND
a0 = 1.2e-10  # m/s^2
G_N = 6.674e-11  # m^3 kg^-1 s^-2
c_light = 2.998e8  # m/s
H0 = h * 100 * 1e3 / (3.086e22)  # s^-1
rho_crit = 3 * H0**2 / (8 * np.pi * G_N)  # kg/m^3
rho_b0 = Omega_b * rho_crit  # kg/m^3

# LCDM parameters for comparison
Omega_m_LCDM = 0.315
Omega_cdm_h2_LCDM = 0.1200
Omega_b_h2_LCDM = 0.02237
Omega_m_h2_LCDM = Omega_cdm_h2_LCDM + Omega_b_h2_LCDM

print("=" * 70)
print("COSMOLOGICAL PARAMETERS")
print("=" * 70)
print(f"h = {h}")
print(f"Omega_b h^2 = {Omega_b_h2}")
print(f"Omega_b = {Omega_b:.6f}")
print(f"Omega_m (DFD) = {Omega_m:.6f} (baryon-only)")
print(f"Omega_m (LCDM) = {Omega_m_LCDM}")
print(f"T_CMB = {T_CMB} K")
print(f"rho_b0 = {rho_b0:.4e} kg/m^3")
print(f"a0 = {a0} m/s^2")
print()

# ============================================================
# TASK 1: EISENSTEIN-HU BARYON TRANSFER FUNCTION
# ============================================================
# Following Eisenstein & Hu 1998 (ApJ 496, 605), Section 3

def eisenstein_hu_baryon_only(k_hmpc, omega_m_h2, omega_b_h2, h_val, T_cmb):
    """
    Eisenstein & Hu (1998) baryon-only transfer function T_b(k).
    k in h/Mpc.
    This uses the zero-baryon + baryon envelope formula.
    For baryon-only (Omega_b = Omega_m), we use the full baryon transfer function.
    """
    # Derived quantities
    theta = T_cmb / 2.7

    # Equality redshift and scale
    z_eq = 2.5e4 * omega_m_h2 * theta**(-4)
    k_eq = 7.46e-2 * omega_m_h2 * theta**(-2)  # Mpc^-1

    # Sound horizon
    b1 = 0.313 * omega_m_h2**(-0.419) * (1 + 0.607 * omega_m_h2**0.674)
    b2 = 0.238 * omega_m_h2**0.223
    z_d = 1291 * omega_m_h2**0.251 / (1 + 0.659 * omega_m_h2**0.828) * (1 + b1 * omega_b_h2**b2)

    # Baryon-to-photon ratio
    R_eq = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_eq)
    R_d = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_d)

    # Sound horizon at drag epoch
    s = (2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / R_eq) * \
        np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    # Silk damping scale
    k_silk = 1.6 * omega_b_h2**0.52 * omega_m_h2**0.73 * (1 + (10.4 * omega_m_h2)**(-0.95))

    print(f"\nEisenstein-Hu derived quantities:")
    print(f"  z_eq = {z_eq:.1f}")
    print(f"  z_d = {z_d:.1f}")
    print(f"  k_eq = {k_eq:.5f} Mpc^-1 = {k_eq/h_val:.5f} h/Mpc")
    print(f"  s = {s:.2f} Mpc = {s*h_val:.2f} Mpc/h")
    print(f"  k_silk = {k_silk:.4f} Mpc^-1 = {k_silk/h_val:.4f} h/Mpc")
    print(f"  R_eq = {R_eq:.4f}")
    print(f"  R_d = {R_d:.4f}")

    # Baryon fraction
    f_b = omega_b_h2 / omega_m_h2  # = 1 for baryon-only

    # Now compute T_b(k) for each k
    T_b = np.zeros_like(k_hmpc)

    for i, kh in enumerate(k_hmpc):
        k = kh * h_val  # Convert to Mpc^-1
        q = k / (13.41 * k_eq)

        # Zero-baryon transfer function T_0
        # Eq. (17) - the "master formula" without baryon features
        C_val = 14.2 + 386.0 / (1 + 69.9 * q**1.08)
        T_0 = np.log(np.e + 1.8 * q) / (np.log(np.e + 1.8 * q) + C_val * q**2)

        # Baryon transfer function with oscillations
        # Eq. (11-12) from EH98

        # Alpha_b: Eq. (14)
        a1_coeff = (46.9 * omega_m_h2)**0.670 * (1 + (32.1 * omega_m_h2)**(-0.532))
        a2_coeff = (12.0 * omega_m_h2)**0.424 * (1 + (45.0 * omega_m_h2)**(-0.582))
        alpha_b = 2.07 * k_eq * s * (1 + R_d)**(-3.0/4.0) * \
                  (a1_coeff**(-f_b) + a2_coeff**(-f_b**3))
        # For f_b = 1, this simplifies

        # Beta_b: Eq. (24)
        beta_node = 8.41 * omega_m_h2**0.435
        beta_b = 0.5 + f_b + (3 - 2*f_b) * np.sqrt((17.2 * omega_m_h2)**2 + 1)

        # Silk damping: Eq. (15)
        # s_tilde
        s_tilde = s / (1 + (beta_node / (k * s))**3)**(1.0/3.0)

        # Baryon piece: Eq. (21)
        j0_ks = np.sin(k * s_tilde) / (k * s_tilde) if k * s_tilde > 1e-6 else 1.0

        # T_b: Eq. (21)
        # For the baryon-only case, T_b = [T_0(1,1,q) / (1 + (k*s/5.2)^2)] * j_0(k*s_tilde) + alpha_b * ...
        x_silk = k / k_silk

        # Full baryon transfer function
        T_b[i] = T_0 / (1 + (k * s / 5.2)**2) + \
                 alpha_b / (1 + (beta_b / (k * s))**3) * np.exp(-x_silk**1.4)
        T_b[i] *= j0_ks + (1 - j0_ks) * np.exp(-(k * s / 5.4)**2 / 2)

    return T_b, s, k_silk, z_d


def eisenstein_hu_full_LCDM(k_hmpc, omega_m_h2, omega_b_h2, h_val, T_cmb):
    """Full LCDM transfer function (CDM+baryon) from EH98."""
    theta = T_cmb / 2.7
    z_eq = 2.5e4 * omega_m_h2 * theta**(-4)
    k_eq = 7.46e-2 * omega_m_h2 * theta**(-2)

    b1 = 0.313 * omega_m_h2**(-0.419) * (1 + 0.607 * omega_m_h2**0.674)
    b2 = 0.238 * omega_m_h2**0.223
    z_d = 1291 * omega_m_h2**0.251 / (1 + 0.659 * omega_m_h2**0.828) * (1 + b1 * omega_b_h2**b2)

    R_eq = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_eq)
    R_d = 31.5e3 * omega_b_h2 * theta**(-4) * (1000 / z_d)

    s = (2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / R_eq) * \
        np.log((np.sqrt(1 + R_d) + np.sqrt(R_d + R_eq)) / (1 + np.sqrt(R_eq)))

    f_b = omega_b_h2 / omega_m_h2
    f_c = 1 - f_b

    T_full = np.zeros_like(k_hmpc)

    for i, kh in enumerate(k_hmpc):
        k = kh * h_val
        q = k / (13.41 * k_eq)

        # CDM transfer function piece
        a1_c = (46.9 * omega_m_h2)**0.670 * (1 + (32.1 * omega_m_h2)**(-0.532))
        a2_c = (12.0 * omega_m_h2)**0.424 * (1 + (45.0 * omega_m_h2)**(-0.582))
        alpha_c = a1_c**(-f_b) * a2_c**(-f_b**3)

        b1_c = 0.944 / (1 + (458 * omega_m_h2)**(-0.708))
        b2_c = (0.395 * omega_m_h2)**(-0.0266)
        beta_c = 1.0 / (1 + b1_c * ((f_c)**b2_c - 1))

        def T0_tilde(q_val, alpha_val, beta_val):
            C = 14.2 / alpha_val + 386.0 / (1 + 69.9 * q_val**1.08)
            return np.log(np.e + 1.8 * beta_val * q_val) / (np.log(np.e + 1.8 * beta_val * q_val) + C * q_val**2)

        T_c = f_c * T0_tilde(q, 1, beta_c) + (1 - f_c) * T0_tilde(q, alpha_c, 1)

        # Baryon piece
        k_silk = 1.6 * omega_b_h2**0.52 * omega_m_h2**0.73 * (1 + (10.4 * omega_m_h2)**(-0.95))
        beta_node = 8.41 * omega_m_h2**0.435
        s_tilde = s / (1 + (beta_node / (k * s))**3)**(1.0/3.0)

        alpha_b = 2.07 * k_eq * s * (1 + R_d)**(-3.0/4.0) * \
                  (a1_c**(-f_b) + a2_c**(-f_b**3))
        beta_b = 0.5 + f_b + (3 - 2*f_b) * np.sqrt((17.2 * omega_m_h2)**2 + 1)

        j0 = np.sin(k * s_tilde) / (k * s_tilde) if k * s_tilde > 1e-6 else 1.0
        T_0_11 = np.log(np.e + 1.8 * q) / (np.log(np.e + 1.8 * q) + (14.2 + 386.0 / (1 + 69.9 * q**1.08)) * q**2)

        T_b = (T_0_11 / (1 + (k * s / 5.2)**2) +
               alpha_b / (1 + (beta_b / (k * s))**3) * np.exp(-(k / k_silk)**1.4))

        T_full[i] = f_b * T_b + f_c * T_c

    return T_full


# k grid
k_array = np.logspace(np.log10(0.001), np.log10(1.0), 500)  # h/Mpc

print("=" * 70)
print("TASK 1: EISENSTEIN-HU BARYON-ONLY TRANSFER FUNCTION")
print("=" * 70)

T_b_array, s_sound, k_silk_val, z_drag = eisenstein_hu_baryon_only(
    k_array, Omega_m_h2, Omega_b_h2, h, T_CMB)

# LCDM for comparison
T_LCDM_array = eisenstein_hu_full_LCDM(
    k_array, Omega_m_h2_LCDM, Omega_b_h2_LCDM, h, T_CMB)

print(f"\nTransfer function values at selected k (h/Mpc):")
for kk in [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_array - kk))
    print(f"  k = {kk:.3f}: T_b(DFD) = {T_b_array[idx]:.6f}, T(LCDM) = {T_LCDM_array[idx]:.6f}, ratio = {T_b_array[idx]/T_LCDM_array[idx]:.4f}")

# ============================================================
# TASK 2: MOND ENHANCEMENT FACTOR nu(k,z)
# ============================================================
print()
print("=" * 70)
print("TASK 2: MOND ENHANCEMENT FACTOR nu(y)")
print("=" * 70)

def nu_MOND(y):
    """MOND interpolation function nu(y) for mu(x) = x/(1+x).
    y = g_N / a0.
    """
    return 0.5 * (1 + np.sqrt(1 + 4.0 / y))

def nu_MOND_safe(y):
    """Handle both scalar and array, with deep-MOND limit for small y."""
    y = np.atleast_1d(np.float64(y))
    result = np.zeros_like(y)
    deep = y < 1e-6
    normal = ~deep
    result[deep] = 1.0 / np.sqrt(y[deep])  # deep MOND limit
    result[normal] = 0.5 * (1 + np.sqrt(1 + 4.0 / y[normal]))
    return result

# Newtonian gravitational acceleration for a perturbation at scale k
# g_N(k, delta, z) = (4*pi*G*rho_b(z)/3) * delta * (2*pi/k_phys)
# where k_phys = k * h / a in proper units

def y_parameter(k_hmpc, delta, z):
    """
    Compute y = g_N / a0 for perturbation of amplitude delta at scale k (h/Mpc).

    g_N = G * M / r^2 where M = (4/3)*pi*rho_b*r^3 and r = pi/k_phys
    So g_N = (4/3)*pi*G*rho_b * (pi/k_phys) * delta

    More precisely, for a Fourier mode: the gravitational acceleration is
    g_N = 4*pi*G*rho_b * delta / k_phys  (in proper coordinates)

    k_phys = k_comoving / a = k * h * (1+z) / (Mpc in meters)
    """
    Mpc = 3.086e22  # meters
    a = 1.0 / (1 + z)
    rho_b_z = rho_b0 / a**3  # physical baryon density
    k_phys = k_hmpc * h * (1 + z) / Mpc  # m^-1

    # Poisson equation in Fourier space: k^2 * Phi = 4*pi*G*rho*delta*a^2
    # g = k * Phi / a = 4*pi*G*rho*delta*a / k
    # In proper coords: g_N = 4*pi*G*rho_b_z * delta / k_phys
    g_N = 4 * np.pi * G_N * rho_b_z * np.abs(delta) / k_phys

    return g_N / a0


# Test at z=0 with linear delta ~ 1
print(f"\ny parameter at z=0, delta=1:")
for kk in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0]:
    y_val = y_parameter(kk, 1.0, 0.0)
    nu_val = nu_MOND_safe(y_val)
    print(f"  k = {kk:.3f} h/Mpc: y = {y_val:.4e}, nu = {nu_val[0]:.4f}")

print(f"\ny parameter at z=0, delta=0.01 (linear regime):")
for kk in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0]:
    y_val = y_parameter(kk, 0.01, 0.0)
    nu_val = nu_MOND_safe(y_val)
    print(f"  k = {kk:.3f} h/Mpc: y = {y_val:.4e}, nu = {nu_val[0]:.4f}")

# ============================================================
# TASK 3 & 4: SELF-CONSISTENT GROWTH WITH MOND
# ============================================================
print()
print("=" * 70)
print("TASK 3-4: SELF-CONSISTENT MOND GROWTH EQUATION")
print("=" * 70)

# Growth equation: delta'' + 2H*delta' = (3/2)*H^2*Omega_b*nu(y)*delta / a^3
# Use a as the time variable, with ' = d/da
#
# Let delta = D*delta_0, then:
# a^2*H^2*D'' + (3a*H^2 + a^2*H*H')*D' = (3/2)*H_0^2*Omega_b*nu(y)*D/a^3
#
# Actually, let's use ln(a) = N as the variable.
# delta_N = d delta / d N = a * d delta / da
# delta_NN = d^2 delta / d N^2
#
# Growth eq in N:
# delta_NN + (2 + d ln H / d N) * delta_N = (3/2) * Omega_m(a) * nu(y(delta)) * delta

# For LCDM background (which DFD uses for expansion):
Omega_Lambda = 1 - Omega_m_LCDM  # Using LCDM background expansion
# Note: in DFD, the expansion history is driven by what looks like dark energy
# but the matter perturbation growth is enhanced by MOND

def H_ratio_sq(a):
    """(H/H0)^2 for LCDM expansion history."""
    return Omega_m_LCDM / a**3 + Omega_Lambda

def dlogH_dN(a):
    """d ln H / d ln a"""
    H2 = H_ratio_sq(a)
    dH2_da = -3 * Omega_m_LCDM / a**4
    return 0.5 * a * dH2_da / H2

def Omega_m_of_a(a):
    """Omega_m(a) for LCDM background."""
    return Omega_m_LCDM / (a**3 * H_ratio_sq(a))

# ANALYTICAL SOLUTION for deep-MOND power-law growth during matter domination
print("\n--- Analytical Deep-MOND Growth Exponent ---")
print("In matter domination with deep MOND (nu ~ 1/sqrt(y)):")
print("  delta'' + 2H*delta' = (3/2)*H^2*Omega_b * (1/sqrt(y)) * delta")
print("  where y = (4*pi*G*rho_b*delta)/(k_phys*a0) * (1/k_phys)")
print("")
print("  Let delta = D0 * a^p. In matter domination: a ~ t^{2/3}, H = 2/(3t)")
print("")
print("  y = 4*pi*G*rho_b0/(a^3) * delta * a / (k*H0/a * a0)")
print("    ... after simplification:")
print("  y ~ delta * a^(-1) * (const/k)")
print("")
print("  nu*delta ~ sqrt(k/const) * delta/sqrt(delta) * sqrt(a) * delta")
print("           = sqrt(k/const) * sqrt(delta) * sqrt(a)")
print("")
print("  For delta = D0*a^p:")
print("  RHS ~ a^{p/2 + 1/2}")
print("  LHS: p(p-1)*a^{p-2} + 2*(p)*a^{p-1} terms...")
print("")

# Let me do this more carefully
# In EdS: H = H0 * a^{-3/2}, H^2 = H0^2 * a^{-3}
# Using N = ln(a): delta_NN + (1/2)*delta_N = (3/2)*nu(y)*delta  [for Omega_m=1 EdS]
# But we have Omega_b << 1 even in EdS...
# Actually in a baryon-only EdS: Omega_m = Omega_b ~ 0.049, not 1
# The background isn't EdS, it's Lambda-dominated

# Let's do the numerical integration properly
def growth_ode_MOND(N, state, k_hmpc, use_MOND=True):
    """
    ODE for growth factor with MOND enhancement.
    N = ln(a), state = [delta, delta_N]

    delta_NN + (2 + d ln H / d N) * delta_N = (3/2) * Omega_m(a) * nu_eff * delta

    For DFD: nu_eff = nu(y(k, delta, z)) where the extra gravity comes from MOND
    but Omega_m in the source term is Omega_b (baryons are the only matter)
    """
    delta, delta_N = state
    a = np.exp(N)
    z = 1.0/a - 1.0

    # Background
    E2 = H_ratio_sq(a)  # (H/H0)^2
    dlnH = dlogH_dN(a)

    if use_MOND and np.abs(delta) > 1e-15:
        # MOND enhancement
        y_val = y_parameter(k_hmpc, np.abs(delta), z)
        nu_val = float(nu_MOND_safe(y_val)[0])
    else:
        nu_val = 1.0

    # Source term: use Omega_b for the actual matter density
    # The gravitational pull is enhanced by nu, so:
    # effective source = (3/2) * (Omega_b / (a^3 * E2)) * nu * delta
    # But wait - in MOND the enhancement applies to the gravitational force,
    # which already includes all baryonic matter. So:
    Omega_b_a = Omega_b / (a**3 * E2)

    source = 1.5 * Omega_b_a * nu_val * delta

    delta_NN = source - (2 + dlnH) * delta_N

    return [delta_N, delta_NN]


def growth_ode_LCDM(N, state):
    """Standard LCDM growth ODE."""
    delta, delta_N = state
    a = np.exp(N)
    E2 = H_ratio_sq(a)
    dlnH = dlogH_dN(a)
    Omega_m_a = Omega_m_LCDM / (a**3 * E2)
    source = 1.5 * Omega_m_a * delta
    delta_NN = source - (2 + dlnH) * delta_N
    return [delta_N, delta_NN]


# Integrate from high redshift to z=0
a_init = 1e-3  # a = 0.001, z = 999
N_init = np.log(a_init)
N_final = 0.0  # a = 1, z = 0

# Initial conditions: growing mode in matter domination
# delta ~ a during matter domination for standard gravity
# delta_N = d(delta)/d(ln a) = a * d(delta)/da = delta (for delta ~ a)
delta_init = a_init  # normalized so D(a_init) = a_init
delta_N_init = a_init  # growing mode: delta_N = delta

# LCDM growth
print("\n--- Computing LCDM growth factor ---")
N_span = np.linspace(N_init, N_final, 5000)
sol_LCDM = solve_ivp(growth_ode_LCDM, [N_init, N_final],
                       [delta_init, delta_N_init],
                       t_eval=N_span, method='RK45', rtol=1e-10, atol=1e-12)

D_LCDM_z0 = sol_LCDM.y[0, -1]
print(f"D_LCDM(z=0) [unnormalized] = {D_LCDM_z0:.6f}")
print(f"D_LCDM(z=0) / a_init = {D_LCDM_z0/a_init:.6f}")

# MOND growth for each k
print("\n--- Computing MOND-enhanced growth for each k ---")
k_growth = np.logspace(np.log10(0.001), np.log10(1.0), 100)
D_DFD_z0 = np.zeros_like(k_growth)

for i, kk in enumerate(k_growth):
    def ode_k(N, state):
        return growth_ode_MOND(N, state, kk, use_MOND=True)

    sol = solve_ivp(ode_k, [N_init, N_final],
                    [delta_init, delta_N_init],
                    t_eval=[N_final], method='RK45', rtol=1e-8, atol=1e-12,
                    max_step=0.01)
    D_DFD_z0[i] = sol.y[0, -1]

# Normalize: D_LCDM(z=0) = 1 conventionally, so divide by D_LCDM_z0
D_LCDM_norm = D_LCDM_z0 / D_LCDM_z0  # = 1
D_DFD_norm = D_DFD_z0 / D_LCDM_z0  # relative to LCDM

print(f"\nGrowth factor D_DFD(k, z=0) / D_LCDM(z=0):")
for kk in [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_growth - kk))
    print(f"  k = {kk:.3f} h/Mpc: D_DFD/D_LCDM = {D_DFD_norm[idx]:.6f}")

# The ratio D_DFD / D_LCDM tells us the MOND boost
# For baryon-only gravity without MOND: source ~ Omega_b instead of Omega_m
# So growth is suppressed by factor ~ (Omega_b/Omega_m)^{0.55} ~ 0.17
# MOND must compensate for this

# What is the standard baryon-only growth WITHOUT MOND?
print("\n--- Baryon-only growth WITHOUT MOND (standard gravity) ---")
def growth_ode_baryon_only(N, state):
    """Baryon-only growth without MOND."""
    delta, delta_N = state
    a = np.exp(N)
    E2 = H_ratio_sq(a)
    dlnH = dlogH_dN(a)
    Omega_b_a = Omega_b / (a**3 * E2)
    source = 1.5 * Omega_b_a * delta
    delta_NN = source - (2 + dlnH) * delta_N
    return [delta_N, delta_NN]

sol_baryononly = solve_ivp(growth_ode_baryon_only, [N_init, N_final],
                            [delta_init, delta_N_init],
                            t_eval=[N_final], method='RK45', rtol=1e-10, atol=1e-12)
D_baryon_only = sol_baryononly.y[0, -1]
print(f"D_baryon_only(z=0) / D_LCDM(z=0) = {D_baryon_only/D_LCDM_z0:.6f}")
print(f"This is the growth suppression from having only baryons (no CDM, no MOND)")

# ============================================================
# TASK 5: EFFECTIVE nu AND SCALE-DEPENDENT BOOST
# ============================================================
print()
print("=" * 70)
print("TASK 5: EFFECTIVE MOND BOOST vs SCALE")
print("=" * 70)

# The MOND nu factor at z=0 for the final delta values
nu_at_z0 = np.zeros_like(k_growth)
y_at_z0 = np.zeros_like(k_growth)
for i, kk in enumerate(k_growth):
    delta_final = D_DFD_z0[i] / D_LCDM_z0  # normalized delta
    y_val = y_parameter(kk, delta_final, 0.0)
    y_at_z0[i] = y_val
    nu_at_z0[i] = float(nu_MOND_safe(y_val)[0])

print(f"\nMOND parameters at z=0:")
for kk in [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_growth - kk))
    print(f"  k = {kk:.3f}: y = {y_at_z0[idx]:.4e}, nu = {nu_at_z0[idx]:.4f}, "
          f"Omega_eff = nu*Omega_b = {nu_at_z0[idx]*Omega_b:.4f}")

# ============================================================
# TASK 6: FINAL P_DFD(k) AND P_LCDM(k)
# ============================================================
print()
print("=" * 70)
print("TASK 6: POWER SPECTRA P_DFD(k) AND P_LCDM(k)")
print("=" * 70)

# Interpolate growth factor to full k grid
D_DFD_interp = interp1d(np.log(k_growth), D_DFD_norm, kind='cubic', fill_value='extrapolate')
D_DFD_full = D_DFD_interp(np.log(k_array))

# P(k) = A_s * (k/k_pivot)^{n_s - 1} * T^2(k) * D^2(z=0) * (2*pi^2 / k^3)
# Note: k_pivot is in Mpc^-1, k_array is in h/Mpc
# Convert k to Mpc^-1 for primordial spectrum

k_Mpc = k_array * h  # Mpc^-1

# Dimensionless primordial spectrum: Delta^2_R(k) = A_s * (k/k_pivot)^{n_s-1}
# P(k) = (2*pi^2 / k^3) * Delta^2(k)
# Delta^2(k) = A_s * (k/k_pivot)^{n_s-1} * T^2(k) * D^2(z)

# But for fair comparison, we need the same normalization convention
# Let's compute Delta^2(k) = (k^3 / (2*pi^2)) * P(k)

Delta2_primordial = A_s * (k_Mpc / k_pivot)**(n_s - 1)

# DFD power spectrum
Delta2_DFD = Delta2_primordial * T_b_array**2 * D_DFD_full**2
P_DFD = 2 * np.pi**2 / k_Mpc**3 * Delta2_DFD

# LCDM power spectrum (D_LCDM = 1 by normalization)
Delta2_LCDM = Delta2_primordial * T_LCDM_array**2 * 1.0**2
P_LCDM = 2 * np.pi**2 / k_Mpc**3 * Delta2_LCDM

# Convert P(k) to (Mpc/h)^3 units
P_DFD_hmpc = P_DFD / h**3
P_LCDM_hmpc = P_LCDM / h**3

print(f"\nPower spectrum values P(k) in (Mpc/h)^3:")
print(f"{'k (h/Mpc)':<12} {'P_DFD':<16} {'P_LCDM':<16} {'Ratio':<12}")
for kk in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_array - kk))
    ratio = P_DFD_hmpc[idx] / P_LCDM_hmpc[idx]
    print(f"  {kk:<10.3f} {P_DFD_hmpc[idx]:<16.2f} {P_LCDM_hmpc[idx]:<16.2f} {ratio:<12.6f}")

# BOSS range analysis
print(f"\n--- BOSS Range k = 0.01-0.15 h/Mpc ---")
boss_mask = (k_array >= 0.01) & (k_array <= 0.15)
k_boss = k_array[boss_mask]
ratio_boss = P_DFD_hmpc[boss_mask] / P_LCDM_hmpc[boss_mask]
print(f"Mean P_DFD/P_LCDM in BOSS range: {np.mean(ratio_boss):.6f}")
print(f"Min  P_DFD/P_LCDM in BOSS range: {np.min(ratio_boss):.6f} at k={k_boss[np.argmin(ratio_boss)]:.4f}")
print(f"Max  P_DFD/P_LCDM in BOSS range: {np.max(ratio_boss):.6f} at k={k_boss[np.argmax(ratio_boss)]:.4f}")

# sigma_8 computation
print(f"\n--- sigma_8 Computation ---")
def sigma_R_squared(R, k_arr, Pk_arr):
    """
    sigma^2(R) = (1/(2*pi^2)) * integral dk k^2 P(k) W^2(kR)
    where W(x) = 3*(sin(x) - x*cos(x)) / x^3 is the top-hat window
    R in Mpc/h, k in h/Mpc, P in (Mpc/h)^3
    """
    def integrand(logk):
        k = np.exp(logk)
        P = np.interp(k, k_arr, Pk_arr)
        x = k * R
        if x < 1e-4:
            W = 1 - x**2 / 10
        else:
            W = 3 * (np.sin(x) - x * np.cos(x)) / x**3
        return k**3 * P * W**2 / (2 * np.pi**2)

    result, _ = quad(integrand, np.log(k_arr[0]), np.log(k_arr[-1]), limit=200)
    return result

R8 = 8.0  # Mpc/h
sigma8_DFD_sq = sigma_R_squared(R8, k_array, P_DFD_hmpc)
sigma8_LCDM_sq = sigma_R_squared(R8, k_array, P_LCDM_hmpc)

sigma8_DFD = np.sqrt(sigma8_DFD_sq)
sigma8_LCDM = np.sqrt(sigma8_LCDM_sq)

print(f"sigma_8 (DFD)  = {sigma8_DFD:.6f}")
print(f"sigma_8 (LCDM) = {sigma8_LCDM:.6f}")
print(f"sigma_8 ratio  = {sigma8_DFD/sigma8_LCDM:.6f}")
print(f"Observed sigma_8 ~ 0.811 +/- 0.006")

# BAO peak analysis
print(f"\n--- BAO Peak Analysis ---")
# BAO peak is at k ~ 2*pi / s_sound
k_BAO = 2 * np.pi / (s_sound * h)  # convert s from Mpc to Mpc/h then invert
print(f"Sound horizon s = {s_sound:.2f} Mpc = {s_sound*h:.2f} Mpc/h")
print(f"BAO fundamental k = 2*pi/s = {k_BAO:.4f} h/Mpc")

# Look for BAO oscillation features
# Ratio P_DFD / P_smooth to see BAO wiggles
# Simple: compute ratio of DFD to a smooth version
from scipy.signal import savgol_filter
if len(k_boss) > 20:
    # Compute ratio to see oscillations
    log_ratio = np.log(P_DFD_hmpc[boss_mask] / P_LCDM_hmpc[boss_mask])
    print(f"BAO oscillation amplitude in DFD/LCDM ratio:")
    print(f"  Peak-to-trough in BOSS range: {np.max(log_ratio) - np.min(log_ratio):.4f} (in ln)")

# ============================================================
# TASK 7: GAP ANALYSIS
# ============================================================
print()
print("=" * 70)
print("TASK 7: GAP ANALYSIS - WHERE DOES P_DFD FALL SHORT?")
print("=" * 70)

ratio_full = P_DFD_hmpc / P_LCDM_hmpc

print(f"\nP_DFD / P_LCDM across k ranges:")
ranges = [(0.001, 0.01, "Large scales"),
          (0.01, 0.05, "Intermediate"),
          (0.05, 0.15, "BOSS linear"),
          (0.15, 0.3, "Quasi-linear"),
          (0.3, 1.0, "Nonlinear")]

for kmin, kmax, label in ranges:
    mask = (k_array >= kmin) & (k_array <= kmax)
    if np.any(mask):
        avg = np.mean(ratio_full[mask])
        print(f"  {label} ({kmin}-{kmax} h/Mpc): mean ratio = {avg:.6f}")

# Decompose the suppression into transfer function and growth contributions
T_ratio_sq = (T_b_array / T_LCDM_array)**2
D_ratio_sq = D_DFD_full**2 / 1.0**2  # LCDM is normalized to 1

print(f"\nDecomposition of P_DFD/P_LCDM = T_b^2/T_LCDM^2 * D_DFD^2/D_LCDM^2:")
print(f"{'k (h/Mpc)':<12} {'T^2 ratio':<16} {'D^2 ratio':<16} {'Product':<12}")
for kk in [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
    idx = np.argmin(np.abs(k_array - kk))
    idx_g = np.argmin(np.abs(k_growth - kk))
    T2r = T_ratio_sq[idx]
    D2r = D_DFD_norm[idx_g]**2
    print(f"  {kk:<10.3f} {T2r:<16.6f} {D2r:<16.6f} {T2r*D2r:<12.6f}")

# How much boost is needed?
print(f"\nRequired MOND boost to match LCDM:")
print(f"  Growth factor ratio D_LCDM/D_baryon_only = {D_LCDM_z0/D_baryon_only:.4f}")
print(f"  This means MOND must boost growth by factor ~{D_LCDM_z0/D_baryon_only:.1f}")
print(f"  Transfer function suppression at k=0.1: T_b/T_LCDM = {T_b_array[np.argmin(np.abs(k_array-0.1))]/T_LCDM_array[np.argmin(np.abs(k_array-0.1))]:.4f}")
print(f"  So total suppression from transfer function alone: {(T_b_array[np.argmin(np.abs(k_array-0.1))]/T_LCDM_array[np.argmin(np.abs(k_array-0.1))])**2:.6f}")

print(f"\n{'='*70}")
print(f"SUMMARY OF KEY NUMBERS")
print(f"{'='*70}")
print(f"Sound horizon: s = {s_sound:.2f} Mpc")
print(f"Silk scale: k_silk = {k_silk_val:.4f} Mpc^-1 = {k_silk_val/h:.4f} h/Mpc")
print(f"Drag redshift: z_d = {z_drag:.1f}")
print(f"sigma_8(DFD)  = {sigma8_DFD:.6f}")
print(f"sigma_8(LCDM) = {sigma8_LCDM:.6f}")
print(f"D_baryon_only/D_LCDM = {D_baryon_only/D_LCDM_z0:.6f}")
print(f"Mean D_DFD/D_LCDM (with MOND) = {np.mean(D_DFD_norm):.6f}")
print(f"Mean P_DFD/P_LCDM (BOSS range) = {np.mean(ratio_boss):.6f}")

# Output data for the markdown report
np.savetxt('/tmp/pk_dfd_data.csv',
           np.column_stack([k_array, P_DFD_hmpc, P_LCDM_hmpc,
                           T_b_array, T_LCDM_array, D_DFD_full]),
           header='k_hMpc, P_DFD, P_LCDM, T_b_DFD, T_LCDM, D_DFD_norm',
           delimiter=',')

print("\nData saved to /tmp/pk_dfd_data.csv")
print("COMPUTATION COMPLETE")
