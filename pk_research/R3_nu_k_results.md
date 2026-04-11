# R3: Scale-Dependent MOND Enhancement Factor nu(k)

## Summary of Key Results

**The fundamental finding:** All three methods for computing y(k) give y ~ 10^{-4} to 10^{-3}, placing the baryon-only universe DEEP in the MOND regime (y << 1) at ALL cosmological scales. This produces nu ~ 28-82, far exceeding the nu ~ 3.5 needed at k ~ 0.1 h/Mpc or nu ~ 6.4 needed at large scales.

**The DFD power spectrum OVERSHOOTS LCDM by 1-2 orders of magnitude** at the sigma_8 scales, regardless of which method is used.

---

## 1. Setup

### Parameters Used
- Omega_b = 0.049, Omega_m = 0.315, h = 0.674
- A_s = 2.1e-9, n_s = 0.965, k_pivot = 0.05 Mpc^-1
- a0 = 1.2e-10 m/s^2
- rho_bar_b = 4.18e-28 kg/m^3
- D(z=0, Omega_m) = 0.787, D(z=0, Omega_b) = 0.461

### Transfer Function
- LCDM: Eisenstein-Hu no-wiggle (Omega_m = 0.315)
- Baryon-only: BBKS with Silk damping, using Gamma = Omega_b*h (baryon-only shape parameter)
- Silk damping scale: k_Silk ~ 8 Mpc^-1, producing strong exponential suppression at k > 0.1 h/Mpc

### Bare Power Spectrum Ratio P_baryon / P_LCDM

The ratio has a surprising structure:

| k (h/Mpc) | P_b/P_LCDM | Explanation |
|-----------|-----------|-------------|
| 0.001 | 12.6 | Enhanced! (Omega_m/Omega_b)^2 * (D_b/D_L)^2 ~ 14 |
| 0.01  | 3.4  | Transfer function starting to differ |
| 0.05  | 0.45 | Silk damping beginning |
| 0.1   | 0.079 | Strong Silk suppression |
| 0.2   | 0.0023 | Very strong suppression |
| 0.5   | 2.7e-9 | Essentially zero |

**Key point:** At large scales, P_baryon > P_LCDM because smaller Omega means larger delta for the same primordial potential (Poisson equation: delta ~ Phi * k^2 / (G*rho)). The suppression only kicks in at k > 0.02 h/Mpc due to Silk damping.

---

## 2. y(k) Results by Method

### Method A: Mode-by-mode
Each mode's own Newtonian acceleration: g_N(k) = (4*pi*G*rho_b) * delta_rms(k) / k_phys

| k (h/Mpc) | delta_rms | g_N (m/s^2) | y_A | nu_A |
|-----------|----------|------------|-----|------|
| 0.001 | 1.56e-3 | 2.51e-14 | 2.09e-4 | 69.7 |
| 0.01  | 6.21e-2 | 9.95e-14 | 8.29e-4 | 35.2 |
| 0.05  | 1.94e-1 | 6.23e-14 | 5.19e-4 | 44.4 |
| 0.1   | 1.56e-1 | 2.51e-14 | 2.09e-4 | 69.6 |
| 0.2   | 4.30e-2 | 3.45e-15 | 2.88e-5 | 186.9 |

nu_A is NON-MONOTONIC in k because delta_rms peaks near k ~ 0.02 h/Mpc then falls due to Silk damping.

### Method B: Global RMS gradient (single y_eff)
sigma_g = 1.60e-13 m/s^2  -->  y_eff = 1.34e-3  -->  nu_eff = 27.87

This applies uniformly to all k.

### Method C: Running integral (modes with q < k)
sigma_g(<k) accumulates from large to small scales:

| k (h/Mpc) | sigma_g(<k) | y_C | nu_C |
|-----------|-----------|-----|------|
| 0.001 | 1.83e-14 | 1.52e-4 | 81.6 |
| 0.01  | 1.02e-13 | 8.53e-4 | 34.7 |
| 0.05  | 1.55e-13 | 1.30e-3 | 28.3 |
| 0.1   | 1.60e-13 | 1.33e-3 | 27.9 |
| 0.2   | 1.60e-13 | 1.34e-3 | 27.9 |

**Method C saturates at k ~ 0.1 h/Mpc** because Silk damping kills all power at smaller scales, so no more acceleration accumulates.

At k > 0.1 h/Mpc, Methods B and C converge (both give nu ~ 27.9), because the running integral has reached its asymptotic value.

---

## 3. P_DFD(k) / P_LCDM(k)

| k (h/Mpc) | P_b/P_L | ratio_A | ratio_B | ratio_C |
|-----------|---------|---------|---------|---------|
| 0.001 | 12.6    | 60988   | 9758    | 83544   |
| 0.01  | 3.4     | 4262    | 2667    | 4142    |
| 0.05  | 0.45    | 882     | 347     | 358     |
| 0.1   | 0.079   | 385     | 61.7    | 61.9    |
| 0.15  | 0.014   | 180     | 11.0    | 11.0    |
| 0.2   | 0.0023  | 79.4    | 1.77    | 1.77    |
| 0.3   | 3.9e-5  | 12.4    | 0.030   | 0.030   |

**ALL methods overshoot LCDM at the sigma_8 scale (k ~ 0.1-0.2 h/Mpc).** Methods B and C give ratio ~ 62 at k = 0.1, and ~ 1.8 at k = 0.2. The crossover (ratio = 1) happens near k ~ 0.2 h/Mpc for Methods B/C.

---

## 4. sigma_8

| Method | sigma_8 | sigma_8 / sigma_8_LCDM |
|--------|---------|----------------------|
| LCDM reference | 0.834 | 1.00 |
| Baryon bare (no MOND) | 0.247 | 0.30 |
| Method A (mode-by-mode) | 13.20 | 15.8 |
| Method B (global RMS) | 6.87 | 8.2 |
| Method C (running) | huge | divergent |

Method C gives a divergent sigma_8 because it has huge nu at very small k (where P_b is already large), creating enormous P_DFD at large scales.

**All methods give sigma_8 >> 0.81.** The MOND enhancement is TOO STRONG.

---

## 5. What y is Needed?

For nu = [1 + sqrt(1 + 4/y)]/2:

| nu_needed | y_needed | Context |
|-----------|----------|---------|
| 1.50 | 1.35 | k = 0.05 (P_b/P_L = 0.45) |
| 3.55 | 0.111 | k = 0.1 (P_b/P_L = 0.079) |
| 6.43 | 0.029 | Omega_m/Omega_b = 6.43 (large-scale limit) |
| 8.39 | 0.016 | k = 0.15 |
| 20.97 | 0.0024 | k = 0.2 |

### What the Methods Actually Give

At k = 0.1 h/Mpc:
- Need: y = 0.111, nu = 3.55
- Method A: y = 2.09e-4, nu = 69.6  (y is 530x too small)
- Method B: y = 1.34e-3, nu = 27.9  (y is 83x too small)
- Method C: y = 1.33e-3, nu = 27.9  (y is 83x too small)

### What a_star Would Be Needed?

To get the right nu at k = 0.1, the effective MOND acceleration scale would need to be:

- Method A: a_star = 2.27e-13 = 0.0019 * a0
- Method B: a_star = 1.45e-12 = 0.012 * a0
- Method C: a_star = 1.44e-12 = 0.012 * a0

**The required a_star is 100-500x SMALLER than a0.** This means the Newtonian accelerations from cosmological perturbations are so tiny (g ~ 10^{-14} to 10^{-13} m/s^2) that we are very deep in the MOND regime, giving too much enhancement.

---

## 6. Critical Analysis

### The Core Problem

The Newtonian gravitational acceleration from cosmological density perturbations is:

g_N ~ (4*pi*G*rho_b) * delta / k_phys ~ 3.5e-37 * delta * (Mpc/k)

At k = 0.1 h/Mpc and delta_rms ~ 0.16:
g_N ~ 3.5e-37 * 0.16 * 4.58e22 ~ 2.5e-14 m/s^2

Compare to a0 = 1.2e-10 m/s^2:
y = g_N / a0 ~ 2e-4

This is EXTREMELY deep in the MOND regime. For y = 2e-4:
nu ~ 1/sqrt(y) ~ 70

But we only need nu ~ 3.5. The standard MOND formula gives FAR too much enhancement.

### Why This Happens

1. **Cosmological perturbations are tiny:** delta ~ 10^{-1} at best, and g_N ~ 10^{-14} m/s^2
2. **a0 = 1.2e-10 is tuned for GALAXIES:** where g_N ~ 10^{-10} at the edge
3. **The ratio is ~10^{-4}:** putting us in the y << 1 deep MOND regime
4. **nu ~ 1/sqrt(y) ~ 100:** giving enhancement factors of ~10^4

### Possible Resolutions

1. **DFD uses a DIFFERENT a_star in cosmology vs galaxies:** The effective threshold could be a_star ~ 10^{-12} m/s^2 in the cosmological context, perhaps set by the Hubble parameter: a_star ~ c*H0 ~ 6.5e-10 >> a0. Then y ~ g/cH0 ~ 4e-5, which is still too small.

2. **The nu function is modified at very small y:** Perhaps nu saturates at large enhancement, e.g., nu_max ~ 6.4 = Omega_m/Omega_b. This would be a NEW prediction of DFD.

3. **The cosmological MOND regime is NOT the simple nu(y) interpolation:** The full DFD field equations may give a different effective nu in the linear perturbation regime, perhaps involving the background field gradient rather than the perturbation gradient.

4. **The relevant acceleration is NOT from perturbations alone:** The Hubble flow acceleration a_H = H^2 * R provides a large Newtonian reference scale. At scale R = 2*pi/k, a_H = H^2 * (2*pi*Mpc/k*h) which at k = 0.1 gives a_H ~ 5e-10 >> a0, putting us in the Newtonian regime for the BACKGROUND.

5. **The EFE (External Field Effect):** The large-scale Hubble flow provides an "external field" that suppresses the MOND enhancement. This could set y ~ a_H/a0 ~ 5, giving nu ~ 1, which would mean NO enhancement -- then DFD cannot produce the right P(k).

---

## 7. Conclusion

The naive application of nu(y) = [1 + sqrt(1+4/y)]/2 to the cosmological power spectrum gives:

- **y ~ 10^{-4} to 10^{-3}** at all relevant scales (deep MOND regime)
- **nu ~ 28 to 82** depending on method and scale
- **P_DFD/P_LCDM ~ 60-600** at k = 0.1 h/Mpc (massive overshoot)
- **sigma_8 ~ 7-13** vs target of ~0.81

**No method for computing y(k) gives nu ~ 5-6 at the sigma_8 scale.** All give nu >> 6 because cosmological accelerations are far below a0.

**The key question for DFD becomes:** What is the correct way to define the effective acceleration scale in the cosmological context? The simple perturbation-based acceleration is far too small. Either:
1. The background Hubble acceleration regularizes y upward, or
2. The DFD field equations produce a different nu(k) in cosmology, or
3. There is a nu_max saturation mechanism, or
4. The EFE from the Hubble expansion sets y ~ O(1) and the P(k) enhancement comes from a different mechanism entirely (e.g., modified growth rather than modified Poisson).

---

## Files
- Script: `R3_nu_k_solver.py`
- Numerical data: `R3_nu_k_data.npz`
