#!/usr/bin/env python3
"""
R7: DFD N-body Particle-Mesh Simulation -- NO IMPOSED EFE
============================================================

CRITICAL DIFFERENCE from R5:
  R5 imposed a_ext = c*H(z) added in quadrature -> x_bar ~ 2.73, nearly Newtonian.
  THIS simulation computes mu ONLY from self-consistent particle field gradients.
  No external field. Jeans swindle via (rho - rho_bar) source subtraction.

Physics:
  Newtonian: nabla^2 Phi = (3/2) Omega_b H0^2 / a * delta
  MOND:      div[mu(|nabla Phi|/(a*a0)) nabla Phi] = same source
  mu(x) = x/(1+x), where x = |g_phys|/a0 and g_phys = -nabla Phi / a

Supercomoving variables (Gadget convention):
  x = comoving position (Mpc/h)
  p = a * v_pec  (momentum, km/s)
  EOM with scale factor a as time variable:
    dx/da = p / (a^3 H)
    dp/da = -nabla(Phi) / (a * H)
  where H = 100 E(a) km/s/(Mpc/h)

Author: R7 Agent (Claude)
"""

import numpy as np
import time

# =============================================================================
# CONSTANTS AND PARAMETERS
# =============================================================================
c_SI = 2.99792458e8
G_SI = 6.67430e-11
Mpc_m = 3.0856775814913673e22
H0_km_s_Mpc = 67.4
h = H0_km_s_Mpc / 100.0
H0_SI = H0_km_s_Mpc * 1e3 / Mpc_m

Omega_b = 0.049
Omega_Lambda = 0.685
Omega_m_bg = 0.315  # for background expansion

a0_SI = 1.2e-10  # m/s^2
a_star = 2.0 * a0_SI / c_SI**2  # m^-1

L_box = 500.0  # Mpc/h
N_grid = 64
N_part_1d = N_grid
N_part = N_part_1d**3
dx = L_box / N_grid  # Mpc/h

z_init = 49.0
z_final = 0.0
N_steps = 100
SEED = 42
z_outputs = [10.0, 5.0, 2.0, 1.0, 0.5, 0.0]

# H0 in code units: 100 km/s/(Mpc/h) always
H0_code = 100.0

# Conversion: grad(Phi) in (km/s)^2/(Mpc/h) to physical m/s^2
# (km/s)^2 / (Mpc/h) = 1e6 m^2/s^2 / (Mpc_m/h m) = 1e6 * h / Mpc_m m/s^2
conv_to_ms2 = 1e6 * h / Mpc_m

print("=" * 70)
print("R7: DFD N-body Particle-Mesh -- NO IMPOSED EFE")
print("=" * 70)
print(f"Box: {L_box} Mpc/h, Grid: {N_grid}^3, Particles: {N_part}")
print(f"a0 = {a0_SI:.2e} m/s^2, a* = {a_star:.3e} m^-1")
print(f"dx = {dx:.2f} Mpc/h, z: {z_init} -> {z_final}, {N_steps} steps")
print(f"conv_to_ms2 = {conv_to_ms2:.4e}")
print()


def E_of_a(a):
    return np.sqrt(Omega_m_bg * a**(-3) + Omega_Lambda)


# =============================================================================
# TRANSFER FUNCTION
# =============================================================================
def transfer_EH_baryons(k_h_Mpc):
    """EH98 baryon transfer function."""
    Ob = Omega_b
    Om = Omega_b  # baryon-only
    Theta27 = 2.725 / 2.7

    z_eq = 2.5e4 * Om * h**2 * Theta27**(-4)
    z_drag = (1291.0 * (Om * h**2)**0.251 /
              (1.0 + 0.659 * (Om * h**2)**0.828) *
              (1.0 + 0.313 * (Om * h**2)**(-0.419) * (Ob * h**2)**0.674))

    R_eq = 31.5e3 * Ob * h**2 * Theta27**(-4) / (z_eq / 1e3)
    R_drag = 31.5e3 * Ob * h**2 * Theta27**(-4) / (z_drag / 1e3)

    s = ((2.0 / (3.0 * np.sqrt(6.0 / R_eq))) * np.sqrt(1 + R_drag) *
         np.log((np.sqrt(1 + R_drag) + np.sqrt(R_drag + R_eq)) / (1 + np.sqrt(R_eq))))

    k = np.maximum(np.atleast_1d(k_h_Mpc).copy(), 1e-10)
    q = k * Theta27**2 / (Om * h**2)
    k_silk = (1.6 * (Ob * h**2)**0.52 * (Om * h**2)**0.73 *
              (1.0 + (10.4 * Om * h**2)**(-0.95)))

    T_b = np.sinc(k * s / np.pi) / (1.0 + (k / k_silk)**1.4) / (1.0 + (k * s / 5.2)**2)
    L0 = np.log(2.0 * np.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    T0 = L0 / (L0 + C0 * q**2)

    return np.squeeze(np.maximum(np.abs(T_b), T0 * 0.1))


# =============================================================================
# INITIAL CONDITIONS
# =============================================================================
def generate_ICs():
    """Generate Zel'dovich ICs. Positions in Mpc/h, momentum p = a*v in km/s."""
    print(f"Generating ICs at z = {z_init}...")
    rng = np.random.RandomState(SEED)

    # k-grid
    kx = np.fft.fftfreq(N_grid, d=dx) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing='ij')
    K2 = KX**2 + KY**2 + KZ**2
    K2[0, 0, 0] = 1.0
    K = np.sqrt(K2)

    T_k = transfer_EH_baryons(K.ravel()).reshape(K.shape)
    P_k = (K / 0.05)**0.965 * T_k**2
    P_k[0, 0, 0] = 0

    # Normalize: target sigma_8(z_init) for baryon-only
    a_init = 1.0 / (1.0 + z_init)
    target_s8 = 0.12 * a_init  # baryon-only LCDM ~ 0.12 at z=0

    dk3 = (2 * np.pi / L_box)**3
    R8 = 8.0
    kR = K * R8
    W8 = np.where(kR > 1e-6, 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3, 1.0)
    s2_raw = np.sum(P_k * W8**2) * dk3 / (2 * np.pi)**3
    P_k *= target_s8**2 / max(s2_raw, 1e-50)

    # Random field
    amp = rng.rayleigh(1.0, (N_grid, N_grid, N_grid))
    phase = rng.uniform(0, 2 * np.pi, (N_grid, N_grid, N_grid))
    delta_k = amp * np.exp(1j * phase) * np.sqrt(P_k * (N_grid / L_box)**3)
    delta_k[0, 0, 0] = 0

    delta = np.real(np.fft.ifftn(delta_k))
    target_var = np.sum(P_k) * dk3 / (2 * np.pi)**3
    if np.var(delta) > 0:
        delta *= np.sqrt(target_var / np.var(delta))

    print(f"  delta_rms = {np.std(delta):.6f}, target sigma_8 = {target_s8:.6f}")

    # Zel'dovich displacements
    delta_k = np.fft.fftn(delta)
    delta_k[0, 0, 0] = 0

    disp_x = np.real(np.fft.ifftn(-1j * KX / K2 * delta_k)) * dx  # Mpc/h
    disp_y = np.real(np.fft.ifftn(-1j * KY / K2 * delta_k)) * dx
    disp_z = np.real(np.fft.ifftn(-1j * KZ / K2 * delta_k)) * dx

    # Grid positions + displacement
    ix = np.arange(N_grid)
    X0, Y0, Z0 = np.meshgrid(ix, ix, ix, indexing='ij')
    pos_x = ((X0 + 0.5) * dx + disp_x).ravel() % L_box
    pos_y = ((Y0 + 0.5) * dx + disp_y).ravel() % L_box
    pos_z = ((Z0 + 0.5) * dx + disp_z).ravel() % L_box

    # Momentum p = a * v_pec
    # v_pec = a * H * f * disp_physical = a * H * f * disp_comoving
    # In code units: H(a_init) = 100*E(a_init) km/s/(Mpc/h)
    H_init = H0_code * E_of_a(a_init)
    f_growth = Omega_b**0.55  # growth rate
    # v_pec = a_init * H_init * f * disp in km/s (since disp in Mpc/h, H in km/s/(Mpc/h))
    v_fac = a_init * H_init * f_growth

    mom_x = a_init * v_fac * disp_x.ravel()  # p = a * v_pec, km/s
    mom_y = a_init * v_fac * disp_y.ravel()
    mom_z = a_init * v_fac * disp_z.ravel()

    print(f"  Max disp: {np.max(np.abs(disp_x)):.4f} Mpc/h")
    print(f"  Max v_pec: {np.max(np.abs(mom_x/a_init)):.2f} km/s")

    return pos_x, pos_y, pos_z, mom_x, mom_y, mom_z


# =============================================================================
# CIC DEPOSIT & INTERPOLATION
# =============================================================================
def cic_deposit(pos_x, pos_y, pos_z):
    """CIC deposit. Returns overdensity delta on grid."""
    density = np.zeros((N_grid, N_grid, N_grid))
    px = pos_x / dx - 0.5
    py = pos_y / dx - 0.5
    pz = pos_z / dx - 0.5

    ix = np.floor(px).astype(int)
    iy = np.floor(py).astype(int)
    iz = np.floor(pz).astype(int)
    fx, fy, fz = px - ix, py - iy, pz - iz

    for dix in [0, 1]:
        wx = (1 - fx) if dix == 0 else fx
        for diy in [0, 1]:
            wy = (1 - fy) if diy == 0 else fy
            for diz in [0, 1]:
                wz = (1 - fz) if diz == 0 else fz
                np.add.at(density, ((ix+dix) % N_grid, (iy+diy) % N_grid, (iz+diz) % N_grid),
                          wx * wy * wz)

    return density / (N_part / N_grid**3) - 1.0


def cic_interp(field_x, field_y, field_z, pos_x, pos_y, pos_z):
    """CIC interpolation of grid fields to particles."""
    px = pos_x / dx - 0.5
    py = pos_y / dx - 0.5
    pz = pos_z / dx - 0.5

    ix = np.floor(px).astype(int)
    iy = np.floor(py).astype(int)
    iz = np.floor(pz).astype(int)
    fx, fy, fz = px - ix, py - iy, pz - iz

    ax_p = np.zeros(N_part)
    ay_p = np.zeros(N_part)
    az_p = np.zeros(N_part)

    for dix in [0, 1]:
        wx = (1 - fx) if dix == 0 else fx
        for diy in [0, 1]:
            wy = (1 - fy) if diy == 0 else fy
            for diz in [0, 1]:
                wz = (1 - fz) if diz == 0 else fz
                jx = (ix + dix) % N_grid
                jy = (iy + diy) % N_grid
                jz = (iz + diz) % N_grid
                w = wx * wy * wz
                ax_p += w * field_x[jx, jy, jz]
                ay_p += w * field_y[jx, jy, jz]
                az_p += w * field_z[jx, jy, jz]

    return ax_p, ay_p, az_p


# =============================================================================
# POISSON SOLVERS
# =============================================================================
# Precompute k-grid
_kx = np.fft.fftfreq(N_grid, d=dx) * 2 * np.pi
_KX, _KY, _KZ = np.meshgrid(_kx, _kx, _kx, indexing='ij')
_K2 = _KX**2 + _KY**2 + _KZ**2
_K2[0, 0, 0] = 1.0


def solve_newtonian(delta, prefactor):
    """Solve nabla^2 Phi = prefactor * delta via FFT.
    Note: FFT Laplacian eigenvalue is -k^2, so Phi_k = -source_k / k^2."""
    return np.real(np.fft.ifftn(-np.fft.fftn(prefactor * delta) / _K2))


def solve_mond(delta, prefactor, a_now, tol=1e-3, max_iter=50, omega=0.5):
    """
    Solve div[mu(g/a0) nabla Phi] = prefactor * delta
    where g = |nabla Phi| / a in physical units.

    Fixed-point iteration: at each step, solve lap(Phi_new) = source / mu_mean
    using mean mu from current iterate.
    """
    source = prefactor * delta
    source_k = np.fft.fftn(source)

    # Start from Newtonian (note the minus sign from FFT Laplacian)
    phi = np.real(np.fft.ifftn(-source_k / _K2))

    for iteration in range(max_iter):
        gx = (np.roll(phi, -1, 0) - np.roll(phi, 1, 0)) / (2 * dx)
        gy = (np.roll(phi, -1, 1) - np.roll(phi, 1, 1)) / (2 * dx)
        gz = (np.roll(phi, -1, 2) - np.roll(phi, 1, 2)) / (2 * dx)

        grad_mag = np.sqrt(gx**2 + gy**2 + gz**2 + 1e-60)

        # Physical acceleration: g_phys = |grad(Phi)| * conv_to_ms2 / a
        g_phys = grad_mag * conv_to_ms2 / a_now
        x_mond = g_phys / a0_SI
        mu = x_mond / (1.0 + x_mond)

        mu_mean = max(np.mean(mu), 1e-15)

        phi_new = np.real(np.fft.ifftn(-source_k / (mu_mean * _K2)))

        rel_change = np.sqrt(np.mean((phi_new - phi)**2)) / max(np.sqrt(np.mean(phi_new**2)), 1e-50)
        phi = (1 - omega) * phi + omega * phi_new

        if rel_change < tol and iteration > 2:
            break

    # Final diagnostics
    gx = (np.roll(phi, -1, 0) - np.roll(phi, 1, 0)) / (2 * dx)
    gy = (np.roll(phi, -1, 1) - np.roll(phi, 1, 1)) / (2 * dx)
    gz = (np.roll(phi, -1, 2) - np.roll(phi, 1, 2)) / (2 * dx)
    grad_mag = np.sqrt(gx**2 + gy**2 + gz**2 + 1e-60)
    g_phys = grad_mag * conv_to_ms2 / a_now
    x_mond = g_phys / a0_SI
    mu = x_mond / (1.0 + x_mond)

    return phi, iteration, np.mean(x_mond), np.sqrt(np.mean(x_mond**2)), np.mean(mu)


# =============================================================================
# MEASUREMENTS
# =============================================================================
def measure(pos_x, pos_y, pos_z):
    """Compute P(k) and sigma_8."""
    delta = cic_deposit(pos_x, pos_y, pos_z)
    delta_k = np.fft.fftn(delta)

    # P(k) binning
    pk3d = np.abs(delta_k / N_grid**3)**2 * L_box**3
    K = np.sqrt(_KX**2 + _KY**2 + _KZ**2)

    k_fund = 2 * np.pi / L_box
    k_nyq = np.pi * N_grid / L_box
    k_bins = np.arange(k_fund, k_nyq, k_fund)
    n_bins = len(k_bins) - 1

    pk_b = np.zeros(n_bins)
    k_c = np.zeros(n_bins)
    counts = np.zeros(n_bins, dtype=int)

    Kf = K.ravel()
    Pf = pk3d.ravel()
    for i in range(n_bins):
        m = (Kf >= k_bins[i]) & (Kf < k_bins[i+1])
        if np.sum(m) > 0:
            pk_b[i] = np.mean(Pf[m])
            k_c[i] = np.mean(Kf[m])
            counts[i] = np.sum(m)

    pk_b -= L_box**3 / N_part  # shot noise
    valid = counts > 0

    # sigma_8 from smoothed field
    R8 = 8.0
    kR = K * R8
    W8 = np.where(kR > 1e-6, 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3, 1.0)
    delta_smooth = np.real(np.fft.ifftn(delta_k * W8))
    sigma8 = np.std(delta_smooth)

    return k_c[valid], pk_b[valid], sigma8, np.std(delta)


# =============================================================================
# SIMULATION
# =============================================================================
def run_simulation(mode='MOND'):
    """Run PM simulation with supercomoving KDK leapfrog."""
    is_mond = (mode == 'MOND')
    print(f"\n{'='*70}")
    print(f"RUNNING {mode} SIMULATION")
    print(f"{'='*70}")

    pos_x, pos_y, pos_z, mom_x, mom_y, mom_z = generate_ICs()

    a_init = 1.0 / (1.0 + z_init)
    a_final = 1.0
    a_arr = np.logspace(np.log10(a_init), np.log10(a_final), N_steps + 1)

    results = {}
    t_start = time.time()

    def get_accel(px, py, pz, a_now):
        """Get grid acceleration -nabla(Phi) and MOND diagnostics."""
        delta = cic_deposit(px, py, pz)
        pf = 1.5 * Omega_b * H0_code**2 / a_now  # (km/s)^2/(Mpc/h)^2

        if is_mond:
            phi, n_iter, x_mean, x_rms, mu_mean = solve_mond(delta, pf, a_now)
        else:
            phi = solve_newtonian(delta, pf)
            x_mean = x_rms = 0.0
            mu_mean = 1.0

        # -nabla(Phi) in (km/s)^2/(Mpc/h)
        ax = -(np.roll(phi, -1, 0) - np.roll(phi, 1, 0)) / (2 * dx)
        ay = -(np.roll(phi, -1, 1) - np.roll(phi, 1, 1)) / (2 * dx)
        az = -(np.roll(phi, -1, 2) - np.roll(phi, 1, 2)) / (2 * dx)
        return ax, ay, az, x_mean, x_rms, mu_mean

    # Initial force
    ax_g, ay_g, az_g, x_mean, x_rms, mu_mean = get_accel(pos_x, pos_y, pos_z, a_arr[0])
    if is_mond:
        print(f"  Initial: x_mean={x_mean:.4e}, mu_mean={mu_mean:.6f}")

    # KDK Leapfrog with a as time variable
    # dx/da = p / (a^3 H)     [Mpc/h per unit a]
    # dp/da = F / (a H)       [km/s per unit a, where F = -nabla Phi in (km/s)^2/(Mpc/h)]
    # Note: F/a has units (km/s)^2/(Mpc/h), and p has units km/s
    # dp/da = F/(a*H) has units (km/s)^2/(Mpc/h) / (km/s/(Mpc/h)) = km/s. Correct!
    # dx/da = p/(a^3*H) has units km/s / (km/s/(Mpc/h)) = Mpc/h. Correct!

    for step in range(N_steps):
        a_old = a_arr[step]
        a_new = a_arr[step + 1]
        da = a_new - a_old
        a_mid = np.sqrt(a_old * a_new)

        H_old = H0_code * E_of_a(a_old)
        H_new = H0_code * E_of_a(a_new)
        H_mid = H0_code * E_of_a(a_mid)

        # KICK (half): dp = F/(a*H) * da/2
        ax_p, ay_p, az_p = cic_interp(ax_g, ay_g, az_g, pos_x, pos_y, pos_z)
        kick_fac = da / (2.0 * a_old * H_old)  # (Mpc/h)/(km/s) ... hmm
        # Actually: F has units (km/s)^2/(Mpc/h)
        # kick_fac * F = da/(a*H) * F = [(km/s)^2/(Mpc/h)] / [km/s/(Mpc/h)] = km/s. Good!
        mom_x += ax_p * kick_fac
        mom_y += ay_p * kick_fac
        mom_z += az_p * kick_fac

        # DRIFT: dx = p/(a^3*H) * da
        drift_fac = da / (a_mid**3 * H_mid)
        # p in km/s, drift_fac in 1/(km/s/(Mpc/h)) per a^2 ...
        # p * drift_fac = km/s * da/(a^3 * H) = km/s / (a^2 * km/s/(Mpc/h)) = Mpc/h. Good!
        pos_x = (pos_x + mom_x * drift_fac) % L_box
        pos_y = (pos_y + mom_y * drift_fac) % L_box
        pos_z = (pos_z + mom_z * drift_fac) % L_box

        # New force at a_new
        ax_g, ay_g, az_g, x_mean, x_rms, mu_mean = get_accel(pos_x, pos_y, pos_z, a_new)

        # KICK (second half)
        ax_p, ay_p, az_p = cic_interp(ax_g, ay_g, az_g, pos_x, pos_y, pos_z)
        kick_fac2 = da / (2.0 * a_new * H_new)
        mom_x += ax_p * kick_fac2
        mom_y += ay_p * kick_fac2
        mom_z += az_p * kick_fac2

        # Output check
        z_new = 1.0 / a_new - 1.0
        for z_out in z_outputs:
            a_out = 1.0 / (1.0 + z_out)
            if a_old < a_out <= a_new and z_out not in results:
                k_pk, pk_vals, sigma8, delta_rms = measure(pos_x, pos_y, pos_z)
                entry = {'sigma8': sigma8, 'delta_rms': delta_rms, 'k': k_pk, 'pk': pk_vals}
                if is_mond:
                    entry.update({'x_mean': x_mean, 'x_rms': x_rms, 'mu_mean': mu_mean})
                results[z_out] = entry

                if is_mond:
                    print(f"  z={z_out:.1f}: sigma8={sigma8:.6f}, x_mean={x_mean:.4e}, "
                          f"mu={mu_mean:.6f}, delta_rms={delta_rms:.6f}")
                else:
                    print(f"  z={z_out:.1f}: sigma8={sigma8:.6f}, delta_rms={delta_rms:.6f}")

        if (step + 1) % 20 == 0:
            elapsed = time.time() - t_start
            v_rms = np.sqrt(np.mean(mom_x**2 + mom_y**2 + mom_z**2)) / a_new
            extra = f", x_mean={x_mean:.4e}, mu={mu_mean:.6f}" if is_mond else ""
            print(f"  Step {step+1}/{N_steps}, z={z_new:.2f}, "
                  f"v_rms={v_rms:.2f} km/s{extra}, {elapsed:.1f}s")

    # Final at z=0
    if 0.0 not in results:
        k_pk, pk_vals, sigma8, delta_rms = measure(pos_x, pos_y, pos_z)
        entry = {'sigma8': sigma8, 'delta_rms': delta_rms, 'k': k_pk, 'pk': pk_vals}
        if is_mond:
            entry.update({'x_mean': x_mean, 'x_rms': x_rms, 'mu_mean': mu_mean})
        results[0.0] = entry

    print(f"\n{mode} complete in {time.time()-t_start:.1f}s")
    return results


# =============================================================================
# MAIN
# =============================================================================
if __name__ == '__main__':
    mond_results = run_simulation('MOND')
    newton_results = run_simulation('Newton')

    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"\n{'z':>5} | {'s8_MOND':>10} {'s8_Newt':>10} {'M/N':>7} | "
          f"{'x_mean':>10} {'mu_mean':>10} {'d_rms_M':>10} {'d_rms_N':>10}")
    print("-" * 90)

    for z in sorted(z_outputs):
        m = mond_results.get(z, {})
        n = newton_results.get(z, {})
        sm = m.get('sigma8', 0)
        sn = n.get('sigma8', 0)
        ratio = sm / max(sn, 1e-30)
        xm = m.get('x_mean', 0)
        mm = m.get('mu_mean', 0)
        dm = m.get('delta_rms', 0)
        dn = n.get('delta_rms', 0)
        print(f"{z:5.1f} | {sm:10.6f} {sn:10.6f} {ratio:7.3f} | "
              f"{xm:10.4e} {mm:10.6f} {dm:10.6f} {dn:10.6f}")

    print("\n" + "=" * 70)
    print("KEY FINDINGS")
    print("=" * 70)

    m0 = mond_results.get(0.0, {})
    n0 = newton_results.get(0.0, {})
    x_z0 = m0.get('x_mean', 0)
    s8m = m0.get('sigma8', 0)
    s8n = n0.get('sigma8', 0)
    mu_z0 = m0.get('mu_mean', 0)

    print(f"\nSelf-consistent x_bar at z=0: {x_z0:.4e}")
    print(f"  R3 analytic: ~0.43 | R5 with EFE: ~2.73 | Expected: 0.1-0.5")
    in_range = 0.001 < x_z0 < 1.0
    print(f"  => {'REASONABLE' if in_range else 'OUTSIDE EXPECTED'}")

    print(f"\nsigma_8(z=0): MOND={s8m:.6f}, Newton={s8n:.6f}")
    if s8n > 0:
        print(f"  MOND/Newton = {s8m/s8n:.3f}")
    print(f"  mu_mean(z=0) = {mu_z0:.6f}")

    # Save markdown
    outpath = '/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R7_nbody_no_efe_results.md'
    with open(outpath, 'w') as f:
        f.write("# R7: DFD N-body Particle-Mesh -- NO Imposed EFE\n\n")
        f.write("## Simulation Parameters\n\n")
        f.write(f"- Box: {L_box} Mpc/h comoving\n")
        f.write(f"- Grid: {N_grid}^3 = {N_grid**3} cells\n")
        f.write(f"- Particles: {N_part_1d}^3 = {N_part}\n")
        f.write(f"- z: {z_init} -> {z_final}, {N_steps} log-spaced steps in a\n")
        f.write(f"- MOND: a_0 = {a0_SI:.2e} m/s^2, a* = {a_star:.3e} m^-1\n")
        f.write(f"- Cosmology: H0={H0_km_s_Mpc}, Omega_b={Omega_b}, Omega_Lambda={Omega_Lambda}\n")
        f.write(f"- Background expansion: Omega_m_bg={Omega_m_bg}\n")
        f.write(f"- Seed: {SEED}\n\n")

        f.write("## Method\n\n")
        f.write("Particle-mesh with CIC deposit/interpolation. Supercomoving KDK leapfrog\n")
        f.write("using scale factor a as time variable (Gadget convention):\n")
        f.write("- p = a * v_pec (momentum)\n")
        f.write("- dx/da = p / (a^3 H)\n")
        f.write("- dp/da = -nabla(Phi) / (a H)\n\n")
        f.write("MOND solver: fixed-point iteration. At each step, compute mu from current\n")
        f.write("potential, then solve lap(Phi_new) = source/mu_mean via FFT.\n\n")
        f.write("**NO external field imposed.** mu is computed purely from self-consistent\n")
        f.write("particle field gradients.\n\n")

        f.write("## Results\n\n")
        f.write("| z | sigma8_MOND | sigma8_Newton | MOND/Newton | x_mean | mu_mean | delta_rms_MOND | delta_rms_Newton |\n")
        f.write("|---|-------------|---------------|-------------|--------|---------|----------------|------------------|\n")

        for z in sorted(z_outputs):
            m = mond_results.get(z, {})
            n = newton_results.get(z, {})
            sm = m.get('sigma8', 0)
            sn = n.get('sigma8', 0)
            ratio = sm / max(sn, 1e-30)
            xm = m.get('x_mean', 0)
            mm = m.get('mu_mean', 0)
            dm = m.get('delta_rms', 0)
            dn = n.get('delta_rms', 0)
            f.write(f"| {z:.1f} | {sm:.6f} | {sn:.6f} | {ratio:.3f} | "
                    f"{xm:.4e} | {mm:.6f} | {dm:.6f} | {dn:.6f} |\n")

        f.write(f"\n## Key Findings\n\n")
        f.write(f"### Self-consistent MOND parameter\n\n")
        f.write(f"- **x_mean(z=0) = {x_z0:.4e}** (= g_rms / a_0)\n")
        f.write(f"- R3 analytic prediction: ~0.43\n")
        f.write(f"- R5 N-body WITH imposed EFE: ~2.73\n")
        f.write(f"- Expected range without EFE: 0.1 - 0.5\n\n")

        f.write(f"### Structure formation\n\n")
        f.write(f"- **MOND sigma_8(z=0) = {s8m:.6f}**\n")
        f.write(f"- Newton sigma_8(z=0) = {s8n:.6f}\n")
        if s8n > 0:
            f.write(f"- Enhancement ratio: {s8m/s8n:.3f}\n\n")

        f.write(f"### Physical regime\n\n")
        f.write(f"- **mu_mean(z=0) = {mu_z0:.6f}**\n")
        if mu_z0 < 0.01:
            f.write(f"- System is DEEP in the MOND regime (mu << 1)\n")
        elif mu_z0 < 0.5:
            f.write(f"- System is in the MOND transition regime\n")
        else:
            f.write(f"- System is in the quasi-Newtonian regime\n")
        f.write(f"\n")

        f.write("## Power Spectra at z=0\n\n")
        km = m0.get('k', np.array([]))
        pm = m0.get('pk', np.array([]))
        kn = n0.get('k', np.array([]))
        pn = n0.get('pk', np.array([]))
        if len(km) > 0 and len(kn) > 0:
            f.write("| k (h/Mpc) | P_MOND | P_Newton | ratio |\n")
            f.write("|-----------|--------|----------|-------|\n")
            for i in range(min(len(km), len(kn), 20)):
                r = pm[i] / pn[i] if pn[i] > 0 else 0
                f.write(f"| {km[i]:.4f} | {pm[i]:.4e} | {pn[i]:.4e} | {r:.3f} |\n")

        f.write("\n## Physical Interpretation\n\n")
        f.write("Without the EFE, cosmological gravitational fields determine the MOND\n")
        f.write("parameter self-consistently. Since g_cosmo ~ delta * (3/2) Omega_b H0^2 R\n")
        f.write("~ 10^-15 m/s^2 is much weaker than a_0 = 1.2e-10 m/s^2, the Newtonian\n")
        f.write("starting point has x = g/a_0 ~ 10^-5, deep in the MOND regime.\n\n")
        f.write("The MOND solver enhances the potential by ~1/mu, which increases the field\n")
        f.write("gradients, raising x. The self-consistent solution finds the equilibrium\n")
        f.write("where x = g_MOND/a_0 and mu(x) = x/(1+x) produce a consistent Phi.\n\n")
        f.write("**Key result:** The self-consistent x without EFE reveals how strongly\n")
        f.write("MOND modifies cosmological structure formation when the only gravitational\n")
        f.write("fields are those from the density perturbations themselves.\n")

    print(f"\nResults saved to {outpath}")
    print("Done!")
