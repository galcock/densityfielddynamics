# R5: MOND-Modified Boltzmann Solver Results

## Overview

This analysis implements a simplified MOND-modified Boltzmann solver to compute
the DFD transfer function including pre-recombination MOND effects. The solver
integrates the coupled baryon-photon acoustic oscillator equations with
MOND-enhanced gravitational potentials, then self-consistently iterates to
convergence.

**Key Question:** Does the MOND interpolation function nu(y) at recombination
provide enough gravitational enhancement to replace CDM in the transfer function?

**Answer: No -- a factor of ~3x shortfall persists.**

---

## 1. Physical Setup

### Cosmological Parameters
| Parameter | Value |
|-----------|-------|
| Omega_b | 0.0492 |
| Omega_m (LCDM) | 0.315 |
| h | 0.674 |
| T_CMB | 2.7255 K |
| n_s | 0.9649 |
| A_s | 2.1e-9 |
| a0_MOND | 1.2e-10 m/s^2 |
| z_rec | 1089 |

### The Problem
In LCDM, CDM provides deep gravitational potential wells that:
- Set z_eq ~ 3400 (matter-radiation equality)
- Give sound horizon s ~ 147 Mpc (~ 14.4 Mpc/h)
- Control Silk damping through the matter content
- Position BAO peaks correctly

With Omega_b alone (no CDM), everything goes wrong:
- z_eq drops to ~539
- Sound horizon inflates to ~18.2 Mpc/h
- Silk damping is catastrophically severe
- BAO peaks shift to wrong positions

### The MOND Hypothesis
MOND enhances gravity when g_N < a_0. At recombination, perturbations are
small (delta ~ 10^{-4} to 10^{-5}), so the Newtonian acceleration from each
mode is g_N << a_0, placing them deep in the MOND regime where:

    nu(y) = [1 + sqrt(1 + 4/y)] / 2    with y = g_N/a_0

If nu ~ 6.4, then Omega_m,eff = nu * Omega_b ~ 0.315 = Omega_m(LCDM).

---

## 2. MOND Enhancement at Recombination (Task 1)

Using the baryon-only transfer function and primordial perturbation amplitudes:

| k [h/Mpc] | delta(k, z_rec) | g_N [m/s^2] | y = g/a0 | nu(y) | Omega_eff |
|------------|-----------------|-------------|----------|-------|-----------|
| 0.001 | 1.14e-06 | 2.18e-11 | 0.182 | 2.90 | 0.143 |
| 0.005 | 1.45e-05 | 5.57e-11 | 0.464 | 2.05 | 0.101 |
| 0.010 | 1.81e-05 | 3.48e-11 | 0.290 | 2.42 | 0.119 |
| 0.020 | 1.71e-05 | 1.64e-11 | 0.137 | 3.25 | 0.160 |
| 0.050 | 9.42e-06 | 3.61e-12 | 0.030 | 6.29 | 0.310 |
| 0.100 | 3.33e-06 | 6.38e-13 | 0.005 | 14.2 | 0.700 |
| 0.200 | 1.77e-07 | 1.70e-14 | 1.4e-4 | 84.5 | 4.16 |
| 0.500 | 2.79e-07 | 1.07e-14 | 8.9e-5 | 106 | 5.24 |

**Initial assessment:** The raw (non-self-consistent) calculation shows nu
increasing strongly with k, from ~2 at large scales to ~100 at small scales.
However, these large nu values at high k reflect the severe Silk damping of
the baryon-only transfer function, which makes delta tiny, pushing y to very
small values. This is not self-consistent.

---

## 3. Self-Consistent Iteration (Task 3)

The self-consistent algorithm:
1. Start with baryon-only T(k) from Eisenstein-Hu
2. Compute delta(k, z_rec) from primordial spectrum + T(k)
3. Compute y(k) = g_N(k)/a_0 and nu(k)
4. Set Omega_m,eff(k) = nu(k) * Omega_b
5. Recompute T(k) with scale-dependent Omega_m,eff
6. Iterate with damping (alpha = 0.3) until convergence

**Convergence:** 29 iterations, max_change < 5e-4

### Converged Results

| Quantity | LCDM | Baryon-only | DFD (MOND) |
|----------|------|-------------|------------|
| z_eq | 3445 | 539 | 1020 |
| s [Mpc/h] | 14.4 | 18.2 | 17.3 |
| k_BAO [h/Mpc] | 0.218 | 0.172 | 0.181 |
| sigma_8 | 0.811 | --- | 0.149 |

**Critical result:** MOND moves z_eq from 539 to 1020, but the target is 3445.
The sound horizon improves from 18.2 to 17.3 Mpc/h, but needs to reach 14.4.

### Self-Consistent nu(k)

| k [h/Mpc] | nu (converged) | nu (required) | Ratio |
|------------|---------------|---------------|-------|
| 0.01 | 1.72 | 6.40 | 0.269 |
| 0.02 | 1.68 | 6.40 | 0.263 |
| 0.05 | 1.74 | 6.40 | 0.272 |
| 0.10 | 1.86 | 6.40 | 0.291 |
| 0.20 | 2.18 | 6.40 | 0.340 |
| 0.50 | 2.70 | 6.40 | 0.422 |

**The self-consistent enhancement is remarkably flat at nu ~ 1.7-2.7, achieving
only 27-42% of the required nu ~ 6.4.**

---

## 4. Transfer Function Comparison (Task 4)

| k [h/Mpc] | T_LCDM | T_baryon | T_DFD | T_DFD/T_LCDM |
|------------|--------|----------|-------|--------------|
| 0.01 | 0.790 | 0.274 | 0.425 | 0.537 |
| 0.02 | 0.612 | 0.132 | 0.232 | 0.379 |
| 0.05 | 0.339 | 0.039 | 0.084 | 0.247 |
| 0.10 | 0.174 | 0.012 | 0.034 | 0.196 |
| 0.20 | 0.069 | 0.001 | 0.011 | 0.156 |
| 0.50 | 0.015 | ~0 | 0.002 | 0.169 |

MOND roughly doubles the baryon-only transfer function, but it remains a factor
of 2-6x below LCDM across all scales.

---

## 5. Post-Recombination Growth (Task 5)

| Model | D(z=0)/D(z_rec) | D_DFD/D_LCDM |
|-------|------------------|--------------|
| LCDM | 358,248 | 1.000 |
| DFD Model A (constant nu=6.4) | 358,248 | 1.000 |
| DFD sigma_nabla (k=0.01) | 9,189 | 0.026 |
| DFD sigma_nabla (k=0.05) | 12,337 | 0.034 |
| DFD sigma_nabla (k=0.10) | 15,126 | 0.042 |
| DFD sigma_nabla (k=0.50) | 29,844 | 0.083 |

**Model A** (constant nu = Omega_m/Omega_b) exactly reproduces LCDM growth
by construction. The **sigma_nabla model** with y-dependent nu gives growth
factors 12-40x too small, consistent with the R2 finding that the nonlinear
MOND equation with y-dependent nu is far too weak.

---

## 6. Power Spectrum (Task 6)

### P_DFD/P_LCDM Ratio

| k [h/Mpc] | Model A | sigma_nabla |
|------------|---------|-------------|
| 0.01 | 0.289 | 0.0002 |
| 0.02 | 0.143 | 0.0001 |
| 0.05 | 0.061 | 0.0001 |
| 0.10 | 0.038 | 0.0001 |
| 0.20 | 0.024 | 0.0001 |
| 0.50 | 0.028 | 0.0002 |

### sigma_8
| Model | sigma_8 | Ratio to LCDM |
|-------|---------|--------------|
| LCDM | 0.811 | 1.000 |
| DFD Model A | 0.149 | 0.183 |
| DFD sigma_nabla | 0.008 | 0.009 |

Model A gives sigma_8 = 0.149, about 5.4x too low. The deficit comes
entirely from the transfer function (growth matches LCDM). The sigma_nabla
model is catastrophically suppressed.

---

## 7. BAO Analysis (Task 7)

### Sound Horizon
| Model | s [Mpc/h] | s_DFD/s_LCDM |
|-------|-----------|-------------|
| LCDM | 14.44 | 1.000 |
| DFD (MOND) | 17.32 | 1.200 |
| Baryon-only | 18.23 | 1.263 |

MOND reduces the sound horizon by 5% from the baryon-only case, but it
remains 20% larger than LCDM. The BAO peak at k = pi/s shifts from
0.218 (LCDM) to 0.181 (DFD), a 17% offset.

### Scale-Dependent z_eq and s

| k [h/Mpc] | Omega_eff h^2 | z_eq | s [Mpc/h] |
|------------|--------------|------|-----------|
| 0.01 | 0.038 | 925 | 17.5 |
| 0.05 | 0.039 | 936 | 17.5 |
| 0.10 | 0.042 | 1003 | 17.3 |
| 0.20 | 0.049 | 1177 | 17.0 |
| 0.50 | 0.061 | 1469 | 16.6 |

The MOND effect is mildly scale-dependent, with Omega_eff increasing at
higher k (smaller scales), but the variation is modest.

---

## 8. ODE Acoustic Oscillator (Task 8)

Direct integration of the tight-coupling oscillator equation with prescribed
nu values:

| k [h/Mpc] | nu=1.0 | nu=3.0 | nu=6.4 | nu=10 |
|------------|--------|--------|--------|-------|
| 0.01 | 6.45 | 10.6 | 21.3 | 39.2 |
| 0.05 | -0.90 | -1.21 | -1.77 | -2.04 |
| 0.10 | -0.12 | -0.12 | -0.071 | 0.083 |
| 0.50 | -3.8e-8 | -1.8e-7 | -5.9e-6 | -6.4e-5 |

At k = 0.01 (super-horizon modes), stronger nu gives stronger growth
(delta ~ nu). At k = 0.05-0.1, modes are oscillating; stronger nu shifts
the oscillation phase and amplitude. At k = 0.5, Silk damping dominates
regardless of nu.

---

## 9. Gap Analysis

### The Fundamental Shortfall

The self-consistent MOND enhancement at recombination is nu ~ 1.7-2.7,
while nu ~ 6.4 is needed. This is a factor of **~3x shortfall**.

### Why nu is Only ~2 Instead of ~6

The physical reason: the MOND interpolation function nu(y) gives large
enhancements only when y = g_N/a_0 << 1. At recombination:

    g_N = 4*pi*G * rho_b(z_rec) * delta / k_phys

At the crucial scales (k ~ 0.01-0.1 h/Mpc), the self-consistent delta
is large enough that y ~ 0.1-0.5 -- **not deep enough in the MOND regime**.

The self-consistent loop creates a feedback: MOND enhances gravity, which
increases the transfer function, which increases delta, which increases y,
which REDUCES nu. The system converges with y ~ 0.1-0.3, giving nu ~ 2.

### Possible Resolutions

1. **Collective/sigma_nabla effect:** The aggregate gradient field from ALL
   modes contributes to y. If the RMS gradient sigma_nabla is large, y could
   be pushed higher, reducing nu further. But this goes the WRONG direction.

2. **Pre-recombination field energy:** The DFD density field itself carries
   energy that contributes to the Friedmann equation. If this acts like an
   effective CDM component, it could provide the missing factor of ~3.

3. **Modified MOND function:** A steeper interpolation function (e.g.,
   nu(y) = 1 + (a_0/g_N)^alpha with alpha > 1) could provide larger
   enhancement at moderate y.

4. **Non-perturbative effects:** The linearised MOND analysis may miss
   nonlinear mode coupling that enhances small-scale power.

5. **Temporal/integration effects:** The MOND enhancement accumulates
   over the entire pre-recombination epoch, not just at z_rec. The
   time-integrated effect could be larger than the instantaneous nu.

6. **Two-field mechanism (from v3.3):** The DFD framework has two
   gravitational sectors. The combined effect may exceed the single-field
   MOND prediction used here.

---

## 10. Summary of Numerical Results

| Metric | LCDM | DFD (MOND) | Deficit Factor |
|--------|------|------------|---------------|
| z_eq | 3445 | 1020 | 3.4x |
| s [Mpc/h] | 14.4 | 17.3 | 0.83x (20% too large) |
| k_BAO [h/Mpc] | 0.218 | 0.181 | 0.83x |
| T(k=0.1) | 0.174 | 0.034 | 5.1x |
| sigma_8 | 0.811 | 0.149 | 5.4x |
| nu_eff (median) | -- | 1.89 | 3.4x below 6.4 |

### Bottom Line

Standard MOND with the simple interpolation function applied to the
pre-recombination baryon-photon fluid provides a factor of ~2 enhancement
over the baryon-only case, but falls short of the required factor of ~6.4
by about 3x. The self-consistent feedback loop (MOND increases delta which
increases y which decreases nu) prevents the system from reaching deep
enough into the MOND regime.

**This is the central challenge for DFD cosmology.** The framework needs
an additional mechanism -- most likely the density field's own energy
contribution to the Friedmann equation -- to bridge the remaining factor
of ~3.

---

## Files

- **Solver:** `pk_research/R5_mond_boltzmann.py`
- **Data:** `pk_research/R5_boltzmann_data.json`
- **Results:** `pk_research/R5_boltzmann_results.md` (this file)

---

*Generated by R5 Agent (Claude Opus 4.6), 2026-04-05*
