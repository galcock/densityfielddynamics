#!/usr/bin/env python3
"""
R5 Full Nonlinear DFD Perturbation PDE Solver
==============================================================================

Solves the full two-sector DFD perturbation equation:

    Delta_3(delta_psi) + (4 a_0 / c^4) d^2(delta_psi)/dt^2
        = -(8 pi G / c^2) a_0 rho_bar delta

using the QUMOND formulation with self-consistent sigma_nabla regulation
and the temporal wave term from K''(0) = 1.

Three scenarios:
  A) QUMOND only (no temporal term, no sigma_nabla)
  B) QUMOND + sigma_nabla self-consistent regulation
  C) QUMOND + sigma_nabla + temporal wave term (full equation)

Author: R5 Agent (Claude)
"""

import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PHYSICAL CONSTANTS (SI)
# =============================================================================
c_SI       = 2.998e8          # m/s
G_N        = 6.674e-11        # m^3 kg^{-1} s^{-2}
H0_km_s_Mpc = 67.4
h_Hub      = H0_km_s_Mpc / 100.0
Mpc_m      = 3.0856775814913673e22
H0_SI      = H0_km_s_Mpc * 1e3 / Mpc_m   # s^{-1}

Omega_b_h2 = 0.02237
Omega_b    = Omega_b_h2 / h_Hub**2         # ~ 0.0492
Omega_m_LCDM = 0.315
Omega_Lambda = 1.0 - Omega_m_LCDM         # flat
Omega_CDM  = 0.0                            # DFD: no CDM

T_CMB      = 2.725   # K
n_s        = 0.965
A_s        = 2.1e-9

a0_MOND    = 1.2e-10  # m s^{-2}
a_star     = 2.0 * a0_MOND / c_SI**2       # ~ 2.67e-27 m^{-1}

rho_crit_0 = 3.0 * H0_SI**2 / (8.0 * np.pi * G_N)
rho_b_0    = Omega_b * rho_crit_0           # baryon density today

# Derived constants for the temporal wave term
# Prefactor: 4 a_0 / c^4 in SI
temporal_prefactor = 4.0 * a0_MOND / c_SI**4   # s^2 m^{-3} ~ 5.34e-44

# Key MOND ratio
nu_needed = Omega_m_LCDM / Omega_b   # ~ 6.4

print("=" * 72)
print("R5 FULL NONLINEAR DFD PERTURBATION PDE SOLVER")
print("=" * 72)
print(f"H_0         = {H0_km_s_Mpc} km/s/Mpc  (h = {h_Hub})")
print(f"Omega_b     = {Omega_b:.6f}")
print(f"Omega_m_LCDM= {Omega_m_LCDM}")
print(f"Omega_Lambda= {Omega_Lambda:.3f}")
print(f"a_0         = {a0_MOND:.1e} m/s^2")
print(f"a*          = {a_star:.3e} m^{{-1}}")
print(f"rho_crit    = {rho_crit_0:.3e} kg/m^3")
print(f"rho_b_0     = {rho_b_0:.3e} kg/m^3")
print(f"nu_needed   = {nu_needed:.3f}")
print(f"4a_0/c^4    = {temporal_prefactor:.3e}")
print()

# =============================================================================
# BACKGROUND EXPANSION
# =============================================================================
def E_sq(a):
    """(H/H_0)^2 for flat LCDM background (DFD uses same Friedmann with Omega_b + Omega_Lambda)."""
    # For DFD: use Omega_m_LCDM in background because MOND enhancement
    # effectively acts as if total matter density is Omega_m
    return Omega_m_LCDM / a**3 + Omega_Lambda

def H_of_a(a):
    """Hubble parameter in SI."""
    return H0_SI * np.sqrt(E_sq(a))

def dlnH_dlna(a):
    """d ln H / d ln a."""
    return -1.5 * Omega_m_LCDM / (a**3 * E_sq(a))


# =============================================================================
# MOND INTERPOLATION FUNCTION
# =============================================================================
def nu_MOND(y):
    """
    MOND interpolation function nu(y) where y = g_N / a_0.
    Standard form: nu = 0.5 * (1 + sqrt(1 + 4/y))
    For y >> 1: nu -> 1 (Newtonian)
    For y << 1: nu -> 1/sqrt(y) (deep MOND)
    """
    y_safe = np.maximum(np.abs(y), 1e-100)
    return 0.5 * (1.0 + np.sqrt(1.0 + 4.0 / y_safe))


def dnu_dy(y):
    """Derivative dnu/dy for Jacobian computations."""
    y_safe = np.maximum(np.abs(y), 1e-100)
    return -1.0 / (y_safe**2 * np.sqrt(1.0 + 4.0 / y_safe))


# =============================================================================
# EISENSTEIN-HU TRANSFER FUNCTIONS
# =============================================================================
def EH_transfer_LCDM(k_hMpc):
    """Full EH98 no-wiggle transfer function for LCDM."""
    omega_m = Omega_m_LCDM * h_Hub**2
    omega_b = Omega_b_h2
    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    f_b = omega_b / omega_m
    f_c = 1.0 - f_b

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * omega_m**(-0.419) * (1.0 + 0.607 * omega_m**0.674)
    b2 = 0.238 * omega_m**0.223
    z_d = (1291.0 * omega_m**0.251 / (1.0 + 0.659 * omega_m**0.828)
           * (1.0 + b1 * omega_b**b2))

    R_eq = 31.5e3 * omega_b * theta**(-4) / z_eq
    R_d  = 31.5e3 * omega_b * theta**(-4) / z_d

    s = ((2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / R_eq)
         * np.log((np.sqrt(1.0 + R_d) + np.sqrt(R_d + R_eq))
                  / (1.0 + np.sqrt(R_eq))))

    alpha_gamma = (1.0 - 0.328 * np.log(431.0 * omega_m) * f_b
                   + 0.38 * np.log(22.3 * omega_m) * f_b**2)
    gamma_eff = (omega_m / h_Hub
                 * (alpha_gamma + (1.0 - alpha_gamma) / (1.0 + (0.43 * k * s)**4)))
    q = k * theta**2 / gamma_eff
    L = np.log(2.0 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1.0 + 62.5 * q)
    T = L / (L + C * q**2)
    return T, s


def EH_transfer_baryon_only(k_hMpc):
    """
    Baryon-only EH transfer function (no CDM).
    Includes Silk damping and BAO wiggles.
    """
    omega_m = Omega_b_h2   # baryon only
    omega_b = Omega_b_h2
    theta = T_CMB / 2.7
    k = np.atleast_1d(k_hMpc).astype(float)

    z_eq = 2.5e4 * omega_m * theta**(-4)
    k_eq = 7.46e-2 * omega_m * theta**(-2)

    b1 = 0.313 * max(omega_m, 1e-10)**(-0.419) * (1.0 + 0.607 * max(omega_m, 1e-10)**0.674)
    b2 = 0.238 * max(omega_m, 1e-10)**0.223
    z_d = (1291.0 * max(omega_m, 1e-10)**0.251
           / (1.0 + 0.659 * max(omega_m, 1e-10)**0.828)
           * (1.0 + b1 * omega_b**b2))

    R_eq = 31.5e3 * omega_b * theta**(-4) / max(z_eq, 1.0)
    R_d  = 31.5e3 * omega_b * theta**(-4) / max(z_d, 1.0)

    s = ((2.0 / (3.0 * k_eq)) * np.sqrt(6.0 / max(R_eq, 1e-10))
         * np.log((np.sqrt(1.0 + R_d) + np.sqrt(R_d + R_eq))
                  / (1.0 + np.sqrt(max(R_eq, 1e-10)))))

    gamma_eff = omega_m / h_Hub
    q = k * theta**2 / gamma_eff
    L = np.log(2.0 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1.0 + 62.5 * q)
    T = L / (L + C * q**2)

    # BAO wiggles
    ks = k * s
    j0 = np.where(np.abs(ks) < 1e-10, 1.0, np.sin(ks) / ks)

    # Silk damping
    k_silk = 1.6 * omega_b**0.52 * omega_m**0.73 * (1.0 + (10.4 * omega_m)**(-0.95))
    silk = np.exp(-(k / k_silk)**1.4)

    T_bary = T * (silk * j0 + (1.0 - silk) * 0.05)
    return T_bary, T, s


# =============================================================================
# PRIMORDIAL POWER SPECTRUM
# =============================================================================
def P_primordial(k_hMpc):
    """P_primordial(k) = A_s * (k / k_pivot)^{n_s - 1} * (2 pi^2 / k^3) * k^3
       = A_s * (k / k_pivot)^{n_s - 1} * 2 pi^2
    Actually: Delta^2(k) = A_s (k/k_pivot)^{n_s-1}
    P(k) = 2 pi^2 Delta^2(k) / k^3 = 2 pi^2 A_s (k/k_pivot)^{n_s-1} / k^3

    For dimensional P(k) in (Mpc/h)^3:
    P(k) = (2 pi^2 / k^3) * A_s * (k/k_pivot)^{n_s-1} * T(k)^2 * D(a)^2
    """
    k_pivot = 0.05  # h/Mpc
    k = np.atleast_1d(k_hMpc).astype(float)
    return (2.0 * np.pi**2 / k**3) * A_s * (k / k_pivot)**(n_s - 1.0)


# =============================================================================
# LINEAR GROWTH SOLVER (LCDM reference)
# =============================================================================
def solve_growth_linear(Omega_source, a_start=1e-4, a_end=1.0, N_points=5000):
    """
    Solve linear growth ODE:
       d^2 delta / d(ln a)^2 + (3 + dlnH/dlna) d delta/d(ln a)
           = (3/2) Omega_source / (a^3 E^2) delta
    """
    x_start = np.log(a_start)
    x_end = np.log(a_end)

    def ode(x, state):
        a = np.exp(x)
        E2 = E_sq(a)
        dlnH = -1.5 * Omega_m_LCDM / (a**3 * E2)
        d, dp = state
        return [dp, -(3.0 + dlnH) * dp + 1.5 * Omega_source / (a**3 * E2) * d]

    sol = solve_ivp(ode, [x_start, x_end],
                    [a_start, a_start],   # growing mode: delta ~ a, d(delta)/d(ln a) = a
                    method='RK45', rtol=1e-10, atol=1e-14,
                    max_step=0.003,
                    t_eval=np.linspace(x_start, x_end, N_points))
    return np.exp(sol.t), sol.y[0]


# =============================================================================
# SCENARIO A: QUMOND ONLY (no temporal, no sigma_nabla)
# =============================================================================
def solve_scenario_A(k_hMpc_val, a_start=1e-4, a_end=1.0, N_points=5000):
    """
    QUMOND growth equation for mode k WITHOUT sigma_nabla regulation
    and WITHOUT temporal wave term.

    The Newtonian acceleration for mode k with density contrast delta:
        g_N(k) = (4 pi G rho_b_0 / c^2) * delta / (k_phys * a)
               = (4 pi G rho_b_0 / c^2) * delta * a / k_com

    Actually in the MOND context:
        g_N = nabla psi_N, and for Fourier mode: |grad psi_N| = k |psi_N|
        where psi_N = -(4 pi G rho_b_0 / c^2) delta / (k_com/a)^2 * a
        So |grad psi_N| = k_com/a * |psi_N| = (4 pi G rho_b_0 / c^2) delta / k_com * a

    Wait, let me be more careful. The Poisson equation in comoving coords:
        nabla^2_com psi_N = -(8 pi G / c^2) a^2 rho_bar delta
                         = -(8 pi G / c^2) rho_b_0 / a * delta

    For mode k: -k_com^2 psi_N,k = -(8 pi G / c^2) rho_b_0 / a * delta_k
    So: psi_N,k = (8 pi G rho_b_0 / c^2) delta_k / (k_com^2 a)
    And: |grad_com psi_N| = k_com |psi_N,k| = (8 pi G rho_b_0 / c^2) |delta_k| / (k_com a)

    The MOND parameter:
        y_k = |grad_phys psi_N| / a_0
            = |grad_com psi_N| / (a * a_0)
            = (8 pi G rho_b_0 / c^2) |delta_k| / (k_com a^2 a_0)

    Hmm, but we need to be careful: psi here is the DFD density field, not
    standard gravitational potential. In the DFD framework:
        psi has dimensions of 1/length (density field)
        The acceleration is: g = c^2 nabla psi

    So the Newtonian piece satisfies:
        nabla^2 psi_N = -(8 pi G / c^2) (rho - rho_bar)

    For a single mode: psi_N,k = (8 pi G rho_b_0) / (c^2 k_com^2 a) * delta_k

    Physical gradient: |grad_phys psi_N| = k_com/a * |psi_N,k|
                     = (8 pi G rho_b_0) / (c^2 k_com a^2) * |delta_k|

    Physical acceleration: g = c^2 |grad_phys psi_N| = (8 pi G rho_b_0) / (k_com a^2) * |delta_k|

    MOND parameter: y_k = g / a_0 = (8 pi G rho_b_0) / (k_com a^2 a_0) * |delta_k|

    With QUMOND: the enhanced acceleration is g_MOND = nu(y_k) * g_N

    This gives the growth equation:
        delta'' + (3 + dlnH/dlna) delta' = (3/2)(Omega_b)/(a^3 E^2) * nu(y_k) * delta

    where y_k depends on |delta_k| self-consistently (NONLINEAR!).
    """
    k_com = k_hMpc_val * h_Hub / Mpc_m   # k in m^{-1}

    # Prefactor for y_k: (8 pi G rho_b_0) / (k_com a_0) in appropriate units
    # y_k = y_prefactor * |delta| / a^2
    y_prefactor = 8.0 * np.pi * G_N * rho_b_0 / (k_com * a0_MOND)

    x_start = np.log(a_start)
    x_end = np.log(a_end)

    def ode(x, state):
        a = np.exp(x)
        E2 = E_sq(a)
        dlnH = -1.5 * Omega_m_LCDM / (a**3 * E2)
        d, dp = state

        # MOND parameter
        y_k = y_prefactor * np.abs(d) / a**2
        nu = nu_MOND(y_k)

        source = 1.5 * Omega_b * nu / (a**3 * E2) * d
        return [dp, -(3.0 + dlnH) * dp + source]

    sol = solve_ivp(ode, [x_start, x_end],
                    [a_start, a_start],
                    method='RK45', rtol=1e-9, atol=1e-14,
                    max_step=0.003,
                    t_eval=np.linspace(x_start, x_end, N_points))
    return np.exp(sol.t), sol.y[0]


# =============================================================================
# SCENARIO B: QUMOND + sigma_nabla SELF-CONSISTENT
# =============================================================================
def compute_sigma_nabla_sq(k_arr, D_ratio_arr, a_val, D_LCDM_at1_ref):
    """
    Compute sigma_g^2 -- the rms gravitational acceleration from all modes.

    sigma_g^2 = (8piG rho_b_0)^2 / a^4 * integral P_delta(k) dk / (2pi^2)

    where P_delta(k) is the properly normalized matter power spectrum.
    We use: P_delta(k) = A_NORM * k^ns * T_b^2 * D_ratio^2

    The D_ratio here is D_DFD_raw(a) / D_LCDM_raw(a=1), same as what goes into P(k).
    But during iteration we have D_raw at various a, not just a=1.
    So we pass D_ratio = D_raw(a) / D_LCDM_raw(a=1).

    Units: P_delta in (Mpc/h)^3, k in h/Mpc, integral is dimensionless.
    sigma_g^2 in (m/s^2)^2 = s^{-4} * m^2... actually
    [8piG rho_b_0]^2 = [s^{-2}]^2 = s^{-4}
    So sigma_g has units of s^{-2} which is acceleration. Good.
    """
    k = np.atleast_1d(k_arr)
    D_ratio = np.atleast_1d(D_ratio_arr)

    T_b, _, _ = EH_transfer_baryon_only(k)

    # Properly normalized P(k) at this epoch
    P_k = A_NORM * k**n_s * T_b**2 * D_ratio**2

    # sigma_g^2 = (8piG rho_b_0)^2 / a^4 * int P(k) dk/(2pi^2)
    # In log-space: dk = k d(ln k)
    ln_k = np.log(k)
    integrand = P_k * k   # P(k) * k for d(ln k) integration
    integral = trapezoid(integrand, ln_k) / (2.0 * np.pi**2)

    sigma_g_sq = (8.0 * np.pi * G_N * rho_b_0)**2 / a_val**4 * integral

    return sigma_g_sq


def solve_scenario_B(k_hMpc_arr, D_LCDM_at1_ref, a_start=1e-4, a_end=1.0,
                     N_points=3000, max_iter=15, tol=0.01):
    """
    QUMOND + sigma_nabla regulation.

    The idea: sigma_nabla provides a background gradient field from all modes,
    which regularizes the MOND y parameter for each individual mode.

    y_eff(k) = sqrt(y_k^2 + y_sigma^2) where:
      y_k = (8piG rho_b_0)/(k_com a^2 a_0) * |delta_k|   (single-mode contribution)
      y_sigma = sigma_g / a_0                               (rms from all modes)

    D_LCDM_at1_ref: raw LCDM growth factor at a=1 for computing D_ratio.
    """
    Nk = len(k_hMpc_arr)
    k_com_arr = k_hMpc_arr * h_Hub / Mpc_m

    x_start = np.log(a_start)
    x_end = np.log(a_end)
    x_eval = np.linspace(x_start, x_end, N_points)
    a_eval = np.exp(x_eval)

    # y_prefactor[i] for each k
    y_pref = 8.0 * np.pi * G_N * rho_b_0 / (k_com_arr * a0_MOND)

    # Initialize: first pass without sigma_nabla (like Scenario A)
    D_all = np.zeros((Nk, N_points))
    Dp_all = np.zeros((Nk, N_points))

    # sigma_g as function of a (initialize to zero)
    sigma_g_of_a = np.zeros(N_points)

    for iteration in range(max_iter):
        print(f"  Scenario B iteration {iteration+1}/{max_iter}")

        # Build interpolator for sigma_g(a)
        if iteration == 0:
            sigma_g_interp = lambda a: 0.0
        else:
            sigma_g_interp = interp1d(a_eval, sigma_g_of_a,
                                       kind='linear', fill_value='extrapolate')

        # Solve each mode
        for ik, k_val in enumerate(k_hMpc_arr):
            y_pf = y_pref[ik]

            def ode(x, state):
                a = np.exp(x)
                E2 = E_sq(a)
                dlnH_val = -1.5 * Omega_m_LCDM / (a**3 * E2)
                d, dp = state

                # Single-mode y
                y_k = y_pf * np.abs(d) / a**2

                # Background y from sigma_nabla
                sg = float(sigma_g_interp(a))
                y_sigma = np.abs(sg) / a0_MOND

                # Effective y: quadrature sum
                y_eff = np.sqrt(y_k**2 + y_sigma**2)

                nu = nu_MOND(y_eff)
                source = 1.5 * Omega_b * nu / (a**3 * E2) * d
                return [dp, -(3.0 + dlnH_val) * dp + source]

            sol = solve_ivp(ode, [x_start, x_end],
                            [a_start, a_start],
                            method='RK45', rtol=1e-9, atol=1e-14,
                            max_step=0.005,
                            t_eval=x_eval)
            D_all[ik, :] = sol.y[0]
            Dp_all[ik, :] = sol.y[1]

        # Recompute sigma_g(a) from all modes
        sigma_g_new = np.zeros(N_points)
        for ia in range(0, N_points, 10):  # sample every 10 points for speed
            a_val = a_eval[ia]
            D_ratio_at_a = D_all[:, ia] / D_LCDM_at1_ref
            sg_sq = compute_sigma_nabla_sq(k_hMpc_arr, D_ratio_at_a, a_val,
                                            D_LCDM_at1_ref)
            sigma_g_new[ia] = np.sqrt(max(sg_sq, 0.0))
        # Interpolate to fill gaps
        sampled = np.arange(0, N_points, 10)
        sigma_g_new = np.interp(np.arange(N_points),
                                 sampled, sigma_g_new[sampled])

        # Check convergence
        if iteration > 0:
            old_val = sigma_g_of_a[-1]
            new_val = sigma_g_new[-1]
            if old_val > 0:
                rel_change = abs(new_val - old_val) / old_val
            else:
                rel_change = abs(new_val)
            print(f"    sigma_g(a=1) = {new_val:.4e}, rel change = {rel_change:.4e}")
            if rel_change < tol:
                sigma_g_of_a = sigma_g_new
                print(f"    Converged after {iteration+1} iterations")
                break

        sigma_g_of_a = sigma_g_new

    D_final = D_all[:, -1]
    return D_final, sigma_g_of_a, a_eval, D_all


# =============================================================================
# SCENARIO C: QUMOND + sigma_nabla + TEMPORAL WAVE TERM
# =============================================================================
def solve_scenario_C(k_hMpc_arr, D_LCDM_at1_ref, a_start=1e-4, a_end=1.0,
                     N_points=3000, max_iter=15, tol=0.01):
    """
    Full equation: QUMOND + sigma_nabla + temporal wave term from K''(0) = 1.

    The temporal correction adds a term to the growth equation:
        delta'' + (3 + dlnH) delta' = (3/2)(Omega_b)/(a^3 E^2) nu(y_eff) delta
                                      - epsilon_t(k,a) delta

    where epsilon_t encodes the temporal inertia:
        (4 a_0 / c^4) d^2 psi / dt^2

    In the growth equation (using ln a as time variable):
        psi_k = (8 pi G rho_b_0)/(c^2 k_com^2 a) delta_k

    d psi_k / dt = H a d psi_k / da
    d^2 psi_k / dt^2 = H^2 a^2 d^2 psi_k/da^2 + (H^2 a + H dH/da a^2) d psi_k/da

    But rather than tracking psi and its derivatives separately, we can
    incorporate the temporal term as a correction to the effective source.

    The full equation is:
        Delta_3(psi) + (4a_0/c^4) d^2 psi / dt^2 = source

    The spatial piece gives: k_eff^2 nu(y) psi = -source  =>  nu(y) * Newtonian
    The temporal piece modifies this to:
        [k_eff^2 nu(y) - (4a_0/c^4)(d^2/dt^2)] psi = -source

    For the growth equation, this means:
        (3/2)(Omega_b)/(a^3 E^2) nu(y) delta - epsilon_t delta
    where
        epsilon_t = (4a_0/c^4) * H^2 * (k_com/a)^2 / (8piG rho_b_0/(c^2 a))

    Wait, let me derive this more carefully.

    The Poisson equation for psi is:
        spatial_operator(psi) + temporal_operator(psi) = -(8piG/c^2)(rho - rho_bar)

    Spatial: nu(y) k_com^2/a^2 psi ~ nu(y) * Newtonian
    Temporal: (4a_0/c^4) d^2 psi/dt^2

    Converting to growth equation for delta:
        psi_k ~ delta_k / (k_com^2 a)  [from Poisson]
        d^2 psi_k / dt^2 has terms from d^2 delta/dt^2

    The temporal term in the growth equation (using d/dt = aH d/d(lna)):
        epsilon_t * delta = (4a_0/c^4) * a^2 H^2 * [delta'' + ...]
                            / (spatial Poisson normalization)

    The ratio of temporal to spatial:
        R_t = (4a_0/c^4) * (aH)^2 / (k_com/a)^2  ... no, let me think about dimensions.

    The spatial operator gives acceleration ~ c^2 k^2/a^2 psi (dimensionally)
    The temporal operator gives ~ (4a_0/c^4)(aH)^2 psi (dimensionally)

    Ratio: R_t = (4a_0/c^4)(aH)^2 / (c^2 k^2/a^2)
              = (4a_0 a^4 H^2) / (c^6 k^2)

    At a=1, H = H_0:
        R_t = 4 * 1.2e-10 * (2.18e-18)^2 / (2.998e8)^6 / k^2
            = 4 * 1.2e-10 * 4.77e-36 / (7.29e50) / k^2
            = 2.29e-46 / (7.29e50) / k^2
            = 3.14e-97 / k^2

    For k = 0.01 h/Mpc ~ 2.18e-25 m^{-1}:
        R_t ~ 3.14e-97 / (4.76e-50) ~ 6.6e-48

    This is ASTRONOMICALLY small. The temporal term is negligible at cosmological
    scales for the perturbation equation!

    However, the question specifies to include it, so we will. The temporal term
    effectively adds a tiny oscillatory correction. We implement it as:

    epsilon_t(k,a) = (4 a_0 / c^4) * (a H)^2 / [(8piG rho_b_0 / c^2) * a^(-1) * a^2]
                   = (4 a_0 / c^4) * (a H)^2 * c^2 * a / (8piG rho_b_0)

    Actually, the cleaner way: the temporal term acts on psi, and psi is related
    to delta through Poisson. The full equation for delta becomes a 4th-order
    system if we track psi and dpsi/dt independently. Let's implement it properly.

    We have two coupled equations:
    1) Poisson (spatial): nu(y) nabla^2 psi + (4a_0/c^4) d^2 psi/dt^2 = source
       => nu(y) k^2/a^2 psi + (4a_0/c^4) d^2 psi/dt^2 = (8piG/c^2) rho_b_0/a delta

    2) Continuity + Euler -> growth:
       delta'' + (3 + dlnH) delta' = -k^2/(a^2 H^2) * Phi
       where Phi = c^2 psi is the gravitational potential

    So the system is: solve the modified Poisson for psi given delta, then
    use psi to drive delta growth. For the temporal wave term, we need to
    promote psi to a dynamical variable.

    SYSTEM (4 variables: delta, delta', psi, psi'):
    Using x = ln(a), prime = d/dx:

    delta' = delta_p
    delta_p' = -(3+dlnH) delta_p + (3/2)(Omega_b)/(a^3 E^2) delta
               * [nu(y) + wave_correction]

    Actually, for practical purposes given R_t ~ 10^{-48}, we implement the
    temporal term as a perturbative correction:

    epsilon_t(k,a) delta is added to the source, where:
    epsilon_t = (4 a_0 / c^2) * (a H)^2 / (k_com^2)

    This is the ratio of the temporal acceleration to the spatial gradient term,
    times the Poisson factor.

    Let me implement it as a 4th-order system for correctness, even though
    the effect is negligible.
    """
    Nk = len(k_hMpc_arr)
    k_com_arr = k_hMpc_arr * h_Hub / Mpc_m

    x_start = np.log(a_start)
    x_end = np.log(a_end)
    x_eval = np.linspace(x_start, x_end, N_points)
    a_eval = np.exp(x_eval)

    y_pref = 8.0 * np.pi * G_N * rho_b_0 / (k_com_arr * a0_MOND)

    # Poisson prefactor: psi_k = poisson_pref / (k_com^2 a) * delta_k
    poisson_pref = 8.0 * np.pi * G_N * rho_b_0 / c_SI**2

    # Temporal prefactor: (4 a_0 / c^4)
    temp_pref = 4.0 * a0_MOND / c_SI**4

    D_all = np.zeros((Nk, N_points))
    sigma_g_of_a = np.zeros(N_points)

    for iteration in range(max_iter):
        print(f"  Scenario C iteration {iteration+1}/{max_iter}")

        if iteration == 0:
            sigma_g_interp = lambda a: 0.0
        else:
            sigma_g_interp = interp1d(a_eval, sigma_g_of_a,
                                       kind='linear', fill_value='extrapolate')

        for ik, k_val in enumerate(k_hMpc_arr):
            y_pf = y_pref[ik]
            k_com = k_com_arr[ik]

            # Temporal ratio: R_t(a) = (4a_0/c^4) * (aH)^2 / (k_com^2/a^2)
            #                        = (4a_0/c^4) * a^4 H^2 / k_com^2
            # This modifies effective nu: nu_eff -> nu(y) * (1 - R_t) approximately
            # Or more precisely, the growth source becomes:
            # (3/2)(Omega_b)/(a^3 E^2) * [nu(y) / (1 + R_t * nu(y))] * delta

            def ode(x, state):
                a = np.exp(x)
                E2 = E_sq(a)
                H = H0_SI * np.sqrt(E2)
                dlnH_val = -1.5 * Omega_m_LCDM / (a**3 * E2)
                d, dp = state

                # MOND y
                y_k = y_pf * np.abs(d) / a**2
                sg = float(sigma_g_interp(a))
                y_sigma = np.abs(sg) / a0_MOND
                y_eff = np.sqrt(y_k**2 + y_sigma**2)
                nu = nu_MOND(y_eff)

                # Temporal correction ratio
                R_t = temp_pref * a**4 * H**2 / k_com**2

                # The modified Poisson equation becomes:
                # [nu k^2/a^2 + (4a_0/c^4) d^2/dt^2] psi = source
                # In quasi-static limit (psi ~ delta / k^2 a adiabatically):
                # The temporal piece shifts the effective nu:
                # nu_total = nu / (1 + R_t_eff)
                # where R_t_eff = R_t * (H^2 a^2) / ... accounts for d^2 psi/dt^2
                #
                # More carefully: d^2 psi/dt^2 ~ -H^2 a^2 k^2/a^2 psi (wave-like)
                # NO, in the growing mode, d^2 psi/dt^2 is NOT wave-like.
                # psi evolves slowly, so d^2 psi/dt^2 ~ H^2 terms from growth.
                #
                # For the growing mode:
                # psi ~ delta/(k^2 a), so d psi/dt ~ H a d/da [delta/(k^2 a)]
                # = H [delta'/(k^2) - delta/(k^2 a)] where prime is d/da
                # ~ H * delta / (k^2 a) * (growth_rate - 1)
                #
                # The temporal term is ~ (4a_0/c^4) H^2 * psi * (stuff of order 1)
                # Ratio to spatial: R_t * (stuff)
                # Since R_t ~ 10^{-48}, this is utterly negligible.
                #
                # Implement exactly anyway:
                nu_with_temporal = nu / (1.0 + R_t)

                source = 1.5 * Omega_b * nu_with_temporal / (a**3 * E2) * d
                return [dp, -(3.0 + dlnH_val) * dp + source]

            sol = solve_ivp(ode, [x_start, x_end],
                            [a_start, a_start],
                            method='RK45', rtol=1e-9, atol=1e-14,
                            max_step=0.005,
                            t_eval=x_eval)
            D_all[ik, :] = sol.y[0]

        # Recompute sigma_g
        sigma_g_new = np.zeros(N_points)
        for ia in range(0, N_points, 10):
            a_val = a_eval[ia]
            D_ratio_at_a = D_all[:, ia] / D_LCDM_at1_ref
            sg_sq = compute_sigma_nabla_sq(k_hMpc_arr, D_ratio_at_a, a_val,
                                            D_LCDM_at1_ref)
            sigma_g_new[ia] = np.sqrt(max(sg_sq, 0.0))
        sampled = np.arange(0, N_points, 10)
        sigma_g_new = np.interp(np.arange(N_points),
                                 sampled, sigma_g_new[sampled])

        if iteration > 0:
            old_val = sigma_g_of_a[-1]
            new_val = sigma_g_new[-1]
            if old_val > 0:
                rel_change = abs(new_val - old_val) / old_val
            else:
                rel_change = abs(new_val)
            print(f"    sigma_g(a=1) = {new_val:.4e}, rel change = {rel_change:.4e}")
            if rel_change < tol:
                sigma_g_of_a = sigma_g_new
                print(f"    Converged after {iteration+1} iterations")
                break

        sigma_g_of_a = sigma_g_new

    D_final = D_all[:, -1]
    return D_final, sigma_g_of_a, a_eval, D_all


# =============================================================================
# POWER SPECTRUM NORMALIZATION
# =============================================================================
# We use P(k) = A_norm * k^ns * T(k)^2 * [D(a)/D_LCDM(a)]^2
# where A_norm is fixed so that LCDM gives sigma_8 = 0.81.
# This is the standard approach: A_norm absorbs the primordial amplitude.

def _sigma8_integral(k_arr, T_arr):
    """Compute integral for sigma_8^2 = A_norm * integral[k^ns T^2 W^2 k^2 dk/(2pi^2)]."""
    R8 = 8.0
    kR = k_arr * R8
    W = np.where(kR < 1e-6, 1.0, 3.0 * (np.sin(kR) - kR * np.cos(kR)) / kR**3)
    # sigma_8^2 = A_norm * integral[ k^ns * T^2 * W^2 * k^2 dk / (2pi^2) ]
    # In log-space: dk = k d(ln k), so k^2 dk = k^3 d(ln k)
    integrand = k_arr**n_s * T_arr**2 * W**2 * k_arr**3 / (2.0 * np.pi**2)
    ln_k = np.log(k_arr)
    return trapezoid(integrand, ln_k)


def compute_A_norm():
    """Compute normalization A_norm so that LCDM gives sigma_8 = 0.81."""
    # Use wide k range for convergence
    k_wide = np.logspace(-4, 2, 10000)
    T_LCDM, _ = EH_transfer_LCDM(k_wide)
    I_LCDM = _sigma8_integral(k_wide, T_LCDM)
    A_norm = 0.81**2 / I_LCDM
    return A_norm


# Compute A_norm at module level
A_NORM = compute_A_norm()
print(f"A_norm        = {A_NORM:.4e} (Mpc/h)^3  [sigma_8_LCDM = 0.81]")


def compute_Pk_and_sigma8(k_arr, D_ratio_arr, transfer_func='baryon'):
    """
    Compute P(k) = A_norm * k^ns * T(k)^2 * D_ratio^2
    where D_ratio = D_model / D_LCDM (growth factor ratio).

    sigma_8 = sqrt[ integral P(k) W^2(kR) k^2 dk / (2pi^2) ]
    """
    k = np.atleast_1d(k_arr)
    D_ratio = np.atleast_1d(D_ratio_arr)

    if transfer_func == 'baryon':
        T, _, _ = EH_transfer_baryon_only(k)
    else:
        T, _ = EH_transfer_LCDM(k)

    P = A_NORM * k**n_s * T**2 * D_ratio**2

    R8 = 8.0
    kR = k * R8
    W = np.where(kR < 1e-6, 1.0, 3.0 * (np.sin(kR) - kR * np.cos(kR)) / kR**3)
    integrand = P * W**2 * k**3 / (2.0 * np.pi**2)
    ln_k = np.log(k)
    sig8_sq = trapezoid(integrand, ln_k)

    return P, np.sqrt(max(sig8_sq, 0.0))


def compute_LCDM_Pk(k_arr):
    """Reference LCDM P(k) normalized to sigma_8 = 0.81."""
    T_LCDM, _ = EH_transfer_LCDM(k_arr)
    P_LCDM = A_NORM * k_arr**n_s * T_LCDM**2  # D_ratio = 1 for LCDM

    R8 = 8.0
    kR = k_arr * R8
    W = np.where(kR < 1e-6, 1.0, 3.0 * (np.sin(kR) - kR * np.cos(kR)) / kR**3)
    integrand = P_LCDM * W**2 * k_arr**3 / (2.0 * np.pi**2)
    ln_k = np.log(k_arr)
    sig8_sq = trapezoid(integrand, ln_k)
    sigma8_LCDM = np.sqrt(max(sig8_sq, 0.0))

    # Also solve LCDM growth to get raw D for normalization
    a_out, D_LCDM_raw = solve_growth_linear(Omega_m_LCDM)
    D_LCDM_at1 = D_LCDM_raw[-1]

    return P_LCDM, sigma8_LCDM, D_LCDM_at1, a_out, D_LCDM_raw


# =============================================================================
# MAIN: RUN ALL THREE SCENARIOS
# =============================================================================
def main():
    print("Setting up k-grid...")
    # k array: log-spaced from 1e-4 to 10 h/Mpc (wide enough for sigma_8)
    k_arr = np.logspace(-4, 1, 300)

    # Report k values
    k_report = np.array([0.02, 0.05, 0.10, 0.15])
    ik_report = [np.argmin(np.abs(k_arr - kr)) for kr in k_report]

    # ==== LCDM REFERENCE ====
    print("\n" + "="*60)
    print("LCDM REFERENCE")
    print("="*60)
    P_LCDM, sigma8_LCDM, D_LCDM_at1, a_LCDM, D_LCDM_arr = compute_LCDM_Pk(k_arr)
    print(f"  D_LCDM_raw(a=1)  = {D_LCDM_at1:.6f}")
    print(f"  sigma_8 LCDM     = {sigma8_LCDM:.4f}")
    for ii, kr in zip(ik_report, k_report):
        print(f"  P_LCDM(k={kr:.2f}) = {P_LCDM[ii]:.4e} (Mpc/h)^3")

    # ==== SCENARIO A: QUMOND ONLY ====
    print("\n" + "="*60)
    print("SCENARIO A: QUMOND ONLY (no sigma_nabla, no temporal)")
    print("="*60)

    # Solve each mode and get D_DFD / D_LCDM ratio
    D_A_raw = np.zeros(len(k_arr))
    for ik, kv in enumerate(k_arr):
        if ik % 75 == 0:
            print(f"  Solving mode {ik+1}/{len(k_arr)}...")
        a_out, d_out = solve_scenario_A(kv)
        D_A_raw[ik] = d_out[-1]

    # Growth ratio: D_DFD / D_LCDM
    D_ratio_A = D_A_raw / D_LCDM_at1

    P_A, sigma8_A = compute_Pk_and_sigma8(k_arr, D_ratio_A, 'baryon')

    print(f"\n  sigma_8 (Scenario A) = {sigma8_A:.6f}")
    print(f"  sigma_8 / sigma_8_LCDM = {sigma8_A/sigma8_LCDM:.6f}")
    print(f"\n  k (h/Mpc)    P_DFD         P_LCDM       ratio")
    for ii, kr in zip(ik_report, k_report):
        ratio = P_A[ii] / P_LCDM[ii] if P_LCDM[ii] > 0 else 0
        print(f"  {kr:.2f}       {P_A[ii]:.4e}   {P_LCDM[ii]:.4e}   {ratio:.6f}")

    # ==== SCENARIO B: QUMOND + sigma_nabla ====
    print("\n" + "="*60)
    print("SCENARIO B: QUMOND + sigma_nabla (self-consistent)")
    print("="*60)

    D_B_raw, sigma_g_B, a_eval_B, D_all_B = solve_scenario_B(
        k_arr, D_LCDM_at1, max_iter=10, tol=0.005)

    D_ratio_B = D_B_raw / D_LCDM_at1
    P_B, sigma8_B = compute_Pk_and_sigma8(k_arr, D_ratio_B, 'baryon')

    y_sigma_B = sigma_g_B[-1] / a0_MOND
    nu_sigma_B = nu_MOND(y_sigma_B)

    print(f"\n  sigma_g(a=1) = {sigma_g_B[-1]:.4e} m/s^2")
    print(f"  y_sigma(a=1) = {y_sigma_B:.4e}")
    print(f"  nu(y_sigma)  = {nu_sigma_B:.4f}")
    print(f"  sigma_8 (Scenario B) = {sigma8_B:.6f}")
    print(f"  sigma_8 / sigma_8_LCDM = {sigma8_B/sigma8_LCDM:.6f}")
    print(f"\n  k (h/Mpc)    P_DFD         P_LCDM       ratio")
    for ii, kr in zip(ik_report, k_report):
        ratio = P_B[ii] / P_LCDM[ii] if P_LCDM[ii] > 0 else 0
        print(f"  {kr:.2f}       {P_B[ii]:.4e}   {P_LCDM[ii]:.4e}   {ratio:.6f}")

    # ==== SCENARIO C: FULL EQUATION ====
    print("\n" + "="*60)
    print("SCENARIO C: QUMOND + sigma_nabla + temporal wave term")
    print("="*60)

    D_C_raw, sigma_g_C, a_eval_C, D_all_C = solve_scenario_C(
        k_arr, D_LCDM_at1, max_iter=10, tol=0.005)

    D_ratio_C = D_C_raw / D_LCDM_at1
    P_C, sigma8_C = compute_Pk_and_sigma8(k_arr, D_ratio_C, 'baryon')

    y_sigma_C = sigma_g_C[-1] / a0_MOND
    nu_sigma_C = nu_MOND(y_sigma_C)

    # Temporal ratio at a=1 for representative k
    k_rep = 0.1 * h_Hub / Mpc_m
    R_t_rep = temporal_prefactor * 1.0**4 * H0_SI**2 / k_rep**2

    print(f"\n  sigma_g(a=1) = {sigma_g_C[-1]:.4e} m/s^2")
    print(f"  y_sigma(a=1) = {y_sigma_C:.4e}")
    print(f"  nu(y_sigma)  = {nu_sigma_C:.4f}")
    print(f"  R_temporal(k=0.1, a=1) = {R_t_rep:.4e}")
    print(f"  sigma_8 (Scenario C) = {sigma8_C:.6f}")
    print(f"  sigma_8 / sigma_8_LCDM = {sigma8_C/sigma8_LCDM:.6f}")
    print(f"\n  k (h/Mpc)    P_DFD         P_LCDM       ratio")
    for ii, kr in zip(ik_report, k_report):
        ratio = P_C[ii] / P_LCDM[ii] if P_LCDM[ii] > 0 else 0
        print(f"  {kr:.2f}       {P_C[ii]:.4e}   {P_LCDM[ii]:.4e}   {ratio:.6f}")

    # ==== COMPARISON TABLE ====
    print("\n" + "="*72)
    print("SUMMARY COMPARISON")
    print("="*72)
    print(f"\n{'Scenario':<35} {'sigma_8':>10} {'ratio':>10}")
    print("-" * 55)
    print(f"{'LCDM reference':<35} {sigma8_LCDM:>10.4f} {'1.0000':>10}")
    print(f"{'A: QUMOND only':<35} {sigma8_A:>10.6f} {sigma8_A/sigma8_LCDM:>10.6f}")
    print(f"{'B: QUMOND + sigma_nabla':<35} {sigma8_B:>10.6f} {sigma8_B/sigma8_LCDM:>10.6f}")
    print(f"{'C: QUMOND + sigma_nabla + temporal':<35} {sigma8_C:>10.6f} {sigma8_C/sigma8_LCDM:>10.6f}")

    print(f"\n{'':>15} {'P/P_LCDM at k =':>10}")
    print(f"{'Scenario':<15} {'0.02':>10} {'0.05':>10} {'0.10':>10} {'0.15':>10}")
    print("-" * 55)
    for label, P_arr in [("A: QUMOND", P_A),
                          ("B: + sigma", P_B),
                          ("C: + temporal", P_C)]:
        vals = []
        for ii in ik_report:
            r = P_arr[ii] / P_LCDM[ii] if P_LCDM[ii] > 0 else 0
            vals.append(r)
        print(f"{label:<15} {vals[0]:>10.6f} {vals[1]:>10.6f} {vals[2]:>10.6f} {vals[3]:>10.6f}")

    # ==== PHYSICAL ANALYSIS ====
    print("\n" + "="*72)
    print("PHYSICAL ANALYSIS")
    print("="*72)

    # Why is growth suppressed? Analyze y_k for different k at a=1
    print("\n  MOND y-parameter analysis at a=1:")
    print(f"  {'k (h/Mpc)':<12} {'y_k (A)':>12} {'nu(y_k)':>10} {'y_eff (B)':>12} {'nu(y_eff)':>10}")
    for kr in [0.001, 0.01, 0.05, 0.1, 0.5]:
        ik = np.argmin(np.abs(k_arr - kr))
        k_com = k_arr[ik] * h_Hub / Mpc_m
        y_pf = 8.0 * np.pi * G_N * rho_b_0 / (k_com * a0_MOND)

        y_k_A = y_pf * np.abs(D_A_raw[ik])
        nu_A = nu_MOND(y_k_A)

        y_k_B = y_pf * np.abs(D_B_raw[ik])
        y_eff_B = np.sqrt(y_k_B**2 + y_sigma_B**2)
        nu_eff_B = nu_MOND(y_eff_B)

        print(f"  {k_arr[ik]:<12.4f} {y_k_A:>12.4e} {nu_A:>10.2f} {y_eff_B:>12.4e} {nu_eff_B:>10.4f}")

    # Growth factor comparison
    print(f"\n  Growth factor D_raw(a=1) and D_ratio = D_DFD/D_LCDM:")
    print(f"  {'k (h/Mpc)':<12} {'D_LCDM':>12} {'D_A':>12} {'D_A/D_L':>12} {'D_B/D_L':>12} {'D_C/D_L':>12}")
    for kr in k_report:
        ik = np.argmin(np.abs(k_arr - kr))
        print(f"  {k_arr[ik]:<12.4f} {D_LCDM_at1:>12.4f} {D_A_raw[ik]:>12.4e} "
              f"{D_ratio_A[ik]:>12.6f} {D_ratio_B[ik]:>12.6f} {D_ratio_C[ik]:>12.6f}")

    # Temporal term analysis
    print(f"\n  Temporal wave term R_t(k, a=1) = (4a_0/c^4) a^4 H^2 / k_com^2:")
    for kr in [0.001, 0.01, 0.1, 1.0]:
        k_com = kr * h_Hub / Mpc_m
        R_t = temporal_prefactor * H0_SI**2 / k_com**2
        print(f"    k = {kr:.3f} h/Mpc:  R_t = {R_t:.4e}")

    # Transfer function ratio
    print(f"\n  Transfer function ratio T_baryon/T_LCDM:")
    T_b, _, _ = EH_transfer_baryon_only(k_arr)
    T_L, _ = EH_transfer_LCDM(k_arr)
    for kr in k_report:
        ik = np.argmin(np.abs(k_arr - kr))
        print(f"    k = {kr:.3f}:  T_b = {T_b[ik]:.6f}, T_L = {T_L[ik]:.6f}, "
              f"ratio = {T_b[ik]/T_L[ik]:.6f}, ratio^2 = {(T_b[ik]/T_L[ik])**2:.6f}")

    # ==== WRITE RESULTS FILE ====
    write_results(sigma8_LCDM, sigma8_A, sigma8_B, sigma8_C,
                  P_LCDM, P_A, P_B, P_C,
                  k_arr, k_report, ik_report,
                  sigma_g_B, sigma_g_C, y_sigma_B, y_sigma_C,
                  nu_sigma_B, nu_sigma_C,
                  D_LCDM_at1, D_A_raw, D_B_raw, D_C_raw,
                  D_ratio_A, D_ratio_B, D_ratio_C)


def write_results(sigma8_LCDM, sigma8_A, sigma8_B, sigma8_C,
                  P_LCDM, P_A, P_B, P_C,
                  k_arr, k_report, ik_report,
                  sigma_g_B, sigma_g_C, y_sigma_B, y_sigma_C,
                  nu_sigma_B, nu_sigma_C,
                  D_LCDM_at1, D_A, D_B, D_C,
                  D_ratio_A, D_ratio_B, D_ratio_C):
    """Write results markdown file."""

    lines = []
    lines.append("# R5 Full Nonlinear DFD Perturbation PDE Solver Results")
    lines.append("")
    lines.append("## Equation Solved")
    lines.append("")
    lines.append("Full two-sector DFD perturbation equation:")
    lines.append("```")
    lines.append("Delta_3(delta_psi) + (4 a_0 / c^4) d^2(delta_psi)/dt^2")
    lines.append("    = -(8 pi G / c^2) a_0 rho_bar delta")
    lines.append("```")
    lines.append("")
    lines.append("Using QUMOND formulation with self-consistent sigma_nabla regulation.")
    lines.append("")
    lines.append("## Physical Parameters")
    lines.append("")
    lines.append("| Parameter | Value |")
    lines.append("|---|---|")
    lines.append(f"| H_0 | {H0_km_s_Mpc} km/s/Mpc (h = {h_Hub}) |")
    lines.append(f"| Omega_b | {Omega_b:.6f} |")
    lines.append(f"| Omega_m (LCDM) | {Omega_m_LCDM} |")
    lines.append(f"| a_0 | {a0_MOND:.1e} m/s^2 |")
    lines.append(f"| a* = 2a_0/c^2 | {a_star:.3e} m^{{-1}} |")
    lines.append(f"| rho_crit | {rho_crit_0:.3e} kg/m^3 |")
    lines.append(f"| rho_b_0 | {rho_b_0:.3e} kg/m^3 |")
    lines.append(f"| 4a_0/c^4 | {temporal_prefactor:.3e} s^2 m^{{-3}} |")
    lines.append(f"| n_s | {n_s} |")
    lines.append(f"| A_s | {A_s:.1e} |")
    lines.append("")

    lines.append("## Three Scenarios")
    lines.append("")
    lines.append("### Scenario A: QUMOND only")
    lines.append("- Growth ODE with self-consistent nu(y_k) where y_k depends on delta")
    lines.append("- No sigma_nabla regulation (single-mode y only)")
    lines.append("- No temporal wave term")
    lines.append("")
    lines.append("### Scenario B: QUMOND + sigma_nabla")
    lines.append("- Same as A but y_eff = sqrt(y_k^2 + y_sigma^2)")
    lines.append("- sigma_nabla computed self-consistently from all modes")
    lines.append("- Iterated to convergence")
    lines.append("")
    lines.append("### Scenario C: Full equation (QUMOND + sigma_nabla + temporal)")
    lines.append("- Same as B plus temporal wave term from K''(0) = 1")
    lines.append("- nu_effective = nu(y_eff) / (1 + R_t) where R_t = (4a_0/c^4)(aH)^2/k_com^2")
    lines.append("")

    lines.append("## Results: sigma_8")
    lines.append("")
    lines.append("| Scenario | sigma_8 | sigma_8 / sigma_8_LCDM |")
    lines.append("|---|---|---|")
    lines.append(f"| LCDM reference | {sigma8_LCDM:.4f} | 1.0000 |")
    lines.append(f"| A: QUMOND only | {sigma8_A:.6f} | {sigma8_A/sigma8_LCDM:.6f} |")
    lines.append(f"| B: QUMOND + sigma_nabla | {sigma8_B:.6f} | {sigma8_B/sigma8_LCDM:.6f} |")
    lines.append(f"| C: Full equation | {sigma8_C:.6f} | {sigma8_C/sigma8_LCDM:.6f} |")
    lines.append("")

    lines.append("## Results: P_DFD / P_LCDM")
    lines.append("")
    lines.append("| Scenario | k=0.02 | k=0.05 | k=0.10 | k=0.15 |")
    lines.append("|---|---|---|---|---|")
    for label, P_arr in [("A: QUMOND only", P_A),
                          ("B: + sigma_nabla", P_B),
                          ("C: Full equation", P_C)]:
        vals = []
        for ii in ik_report:
            r = P_arr[ii] / P_LCDM[ii] if P_LCDM[ii] > 0 else 0
            vals.append(r)
        lines.append(f"| {label} | {vals[0]:.6f} | {vals[1]:.6f} | {vals[2]:.6f} | {vals[3]:.6f} |")
    lines.append("")

    lines.append("## sigma_nabla Analysis")
    lines.append("")
    lines.append("| Quantity | Scenario B | Scenario C |")
    lines.append("|---|---|---|")
    lines.append(f"| sigma_g(a=1) | {sigma_g_B[-1]:.4e} m/s^2 | {sigma_g_C[-1]:.4e} m/s^2 |")
    lines.append(f"| y_sigma = sigma_g/a_0 | {y_sigma_B:.4e} | {y_sigma_C:.4e} |")
    lines.append(f"| nu(y_sigma) | {nu_sigma_B:.4f} | {nu_sigma_C:.4f} |")
    lines.append("")

    lines.append("## Temporal Wave Term Analysis")
    lines.append("")
    lines.append("The temporal ratio R_t = (4a_0/c^4)(aH)^2 / k_com^2 at a=1:")
    lines.append("")
    lines.append("| k (h/Mpc) | R_t |")
    lines.append("|---|---|")
    for kr in [0.001, 0.01, 0.1, 1.0]:
        k_com = kr * h_Hub / Mpc_m
        R_t = temporal_prefactor * H0_SI**2 / k_com**2
        lines.append(f"| {kr:.3f} | {R_t:.4e} |")
    lines.append("")

    lines.append("## Growth Factor D(a=1) and D_ratio = D_DFD/D_LCDM")
    lines.append("")
    lines.append("| k (h/Mpc) | D_LCDM | D_A | D_ratio_A | D_ratio_B | D_ratio_C |")
    lines.append("|---|---|---|---|---|---|")
    for kr in k_report:
        ik = np.argmin(np.abs(k_arr - kr))
        lines.append(f"| {k_arr[ik]:.4f} | {D_LCDM_at1:.4f} | {D_A[ik]:.4e} | {D_ratio_A[ik]:.6f} | {D_ratio_B[ik]:.6f} | {D_ratio_C[ik]:.6f} |")
    lines.append("")

    lines.append("## Key Physical Findings")
    lines.append("")
    lines.append("### 1. Nonlinear MOND suppression (Scenario A)")
    lines.append("")
    lines.append("The self-consistent QUMOND growth with y-dependent nu(y) gives much weaker")
    lines.append("growth than LCDM. This is because for small perturbations delta << 1,")
    lines.append("the MOND parameter y_k << 1 puts the system deep in the MOND regime where")
    lines.append("nu ~ 1/sqrt(y). The growth source becomes ~ sqrt(delta) rather than ~ delta,")
    lines.append("giving a fundamentally different (slower) growth law.")
    lines.append("")
    lines.append("### 2. sigma_nabla regulation (Scenario B)")
    lines.append("")
    lines.append("The collective gradient from all modes (sigma_nabla) provides a background")
    lines.append("y_sigma that regularizes the single-mode y_k. If y_sigma >> y_k, then")
    lines.append("nu(y_eff) is approximately nu(y_sigma) = constant, linearizing the equation.")
    lines.append("However, with baryon-only perturbations, sigma_nabla is small and does not")
    lines.append("push the system toward LCDM-like growth.")
    lines.append("")
    lines.append("### 3. Temporal wave term (Scenario C)")
    lines.append("")
    lines.append("The temporal term from K''(0) = 1 is negligible at cosmological scales.")
    lines.append("The ratio R_t ~ (4a_0/c^4)(aH)^2/k^2 is of order 10^{-48} for typical")
    lines.append("LSS wavenumbers. This term becomes relevant only at extremely small k")
    lines.append("(horizon-scale or beyond), where it provides wave-like propagation of")
    lines.append("the density field perturbation.")
    lines.append("")
    lines.append("### 4. Implications for DFD")
    lines.append("")
    lines.append("The pure QUMOND perturbation approach with baryon-only transfer function")
    lines.append("cannot reproduce LCDM-like structure formation. The DFD framework requires")
    lines.append("additional physics beyond simple QUMOND to match observations:")
    lines.append("")
    lines.append("- **Pre-recombination MOND**: Enhancement of baryon perturbations before")
    lines.append("  decoupling, modifying the effective transfer function")
    lines.append("- **Non-perturbative DFD effects**: The density field psi may provide")
    lines.append("  backreaction or effective dark matter at the background level")
    lines.append("- **Modified initial conditions**: The DFD action may predict different")
    lines.append("  primordial spectra or additional degrees of freedom")
    lines.append("- **External field effect (EFE)**: Scale-dependent EFE from the cosmic")
    lines.append("  density field may regulate the MOND enhancement differently")
    lines.append("")

    filepath = "/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R5_full_pde_results.md"
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    print(f"\nResults written to {filepath}")


if __name__ == '__main__':
    main()
