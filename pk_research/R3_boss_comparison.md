# Round 3: DFD Power Spectrum Prediction vs BOSS DR12

## Summary

This analysis computes the DFD prediction P_DFD(k) = nu^2(k) * P_baryon(k) and compares it directly to the LCDM power spectrum normalized to BOSS DR12 constraints (sigma_8 = 0.811).

## Part 1: Baryon-Only Transfer Function

With Omega_m = Omega_b = 0.049 (no CDM), the Eisenstein-Hu / BBKS transfer function gives:

| Parameter | Baryon-only | LCDM | Ratio |
|-----------|-------------|------|-------|
| z_eq | 539 | 3430 | 0.16x |
| z_drag | 1012 | 1021 | ~same |
| Sound horizon s | 18.2 Mpc/h | 14.4 Mpc/h | 1.26x |
| k_BAO (pi/s) | 0.172 h/Mpc | 0.217 h/Mpc | 0.79x |
| k_Silk | 0.069 Mpc^-1 | 0.090 Mpc^-1 | 0.77x |

The baryon-only transfer function falls much faster than LCDM:

| k (h/Mpc) | T_bary/T_LCDM |
|-----------|---------------|
| 0.005 | 0.28 |
| 0.01 | 0.15 |
| 0.05 | 0.03 |
| 0.10 | 0.01 |
| 0.50 | 0.000002 |

The baryon-only Newtonian growth factor is D_baryon/D_LCDM = 0.616 (38% smaller).

Combined: sigma_8(baryon-only, Newtonian) = 0.0174. Power is suppressed by factor ~22,500x at k = 0.1 h/Mpc relative to LCDM.

## Part 2: Required MOND Enhancement

The MOND enhancement nu_required(k) = sqrt(P_LCDM/P_baryon) needed to match LCDM:

| k (h/Mpc) | nu_required |
|-----------|-------------|
| 0.005 | 5.8 |
| 0.01 | 11.0 |
| 0.02 | 21.4 |
| 0.05 | 55.6 |
| 0.10 | 151 |
| 0.15 | 376 |
| 0.20 | 984 |

**This is STRONGLY scale-dependent**, growing from ~6 at k=0.005 to >1000 at k=0.2 h/Mpc. A constant nu ~ 6.4 (= Omega_m/Omega_b) is NOT sufficient -- it only works if the transfer function is ALSO corrected.

## Part 3: QUMOND Predicted Enhancement

The mode-by-mode QUMOND calculation with y(k) = g_N(k)/a0 gives:

| k (h/Mpc) | delta_rms | y(k) | nu_predicted |
|-----------|-----------|------|--------------|
| 0.005 | 8.2e-3 | 1.4e-3 | 27 |
| 0.01 | 1.0e-2 | 8.9e-4 | 34 |
| 0.05 | 8.1e-3 | 1.4e-4 | 86 |
| 0.10 | 4.0e-3 | 3.4e-5 | 173 |
| 0.15 | 1.8e-3 | 1.0e-5 | 317 |
| 0.20 | 7.1e-4 | 3.0e-6 | 581 |

All scales are in the deep MOND regime (y << 1) at z=0.

## Part 4: Comparison

| k (h/Mpc) | nu_pred | nu_req | pred/req | Status |
|-----------|---------|--------|----------|--------|
| 0.005 | 27.3 | 5.8 | 4.7 | EXCESS |
| 0.01 | 34.1 | 11.0 | 3.1 | EXCESS |
| 0.02 | 47.1 | 21.4 | 2.2 | EXCESS |
| 0.05 | 86.3 | 55.6 | 1.6 | EXCESS |
| **0.10** | **172.9** | **151.4** | **1.1** | **~MATCH** |
| 0.15 | 316.8 | 376.1 | 0.84 | DEFICIT |
| 0.20 | 580.5 | 984.3 | 0.59 | DEFICIT |

**Crossover at k ~ 0.12 h/Mpc**: below this, DFD has too much power; above, too little.

## Part 5: Key Observables

### sigma_8
- sigma_8(LCDM) = 0.811
- sigma_8(baryon-only) = 0.017
- sigma_8(DFD, QUMOND) = 1.044 (29% too high)

### P_DFD/P_LCDM
| k (h/Mpc) | P_DFD/P_LCDM |
|-----------|--------------|
| 0.02 | 4.86 |
| 0.05 | 2.41 |
| 0.10 | 1.30 |
| 0.15 | 0.71 |
| 0.20 | 0.35 |

### BAO
- LCDM: r_d = 14.4 Mpc/h (k_BAO = 0.217 h/Mpc)
- Baryon-only: r_d = 18.2 Mpc/h (k_BAO = 0.172 h/Mpc)
- BOSS DR12 measures r_d = 147.8 Mpc ~ 99.6 Mpc/h

## Part 6: MOND at Recombination

### The Key Question
Can MOND enhance gravity during recombination to effectively increase Omega_m?

### Answer: NO

At z = 1100, the **background** gravitational acceleration satisfies y_bg ~ 1089 >> 1. The universe is solidly in the **Newtonian regime** at recombination. This is because:

- Background: g_bg = (1/2) Omega_b H^2 d_H = Omega_b H c / 2
- At z=1100: H(z) ~ 10^6 times larger than today, so g_bg >> a0
- The MOND transition (y_bg = 1) occurs at z ~ 0, NOT at z ~ 1100

For linearized perturbations around this Newtonian background, nu(y_bg >> 1) ~ 1. The MOND interpolating function has NO EFFECT on perturbation physics at recombination.

### Self-Consistent Perturbation Analysis

| k (h/Mpc) | y_rec | nu_rec | Omega_m,eff |
|-----------|-------|--------|-------------|
| 0.005 | 3470 | 1.000 | 0.049 |
| 0.01 | 2204 | 1.000 | 0.049 |
| 0.05 | 338 | 1.003 | 0.049 |
| 0.10 | 84 | 1.012 | 0.050 |
| 0.15 | 25 | 1.039 | 0.051 |

Even using perturbation-level y values, nu_rec ~ 1 for all BOSS scales.

### The Matched Transfer Function

IF (hypothetically) constant nu = 6.4 applied at recombination, then Omega_m,eff*h^2 = 0.1424 = Omega_m_LCDM*h^2, and:
- z_eq = 3430 (matches LCDM exactly)
- s = 14.45 Mpc/h (matches LCDM exactly)
- sigma_8 = 0.811 (matches LCDM exactly)
- P_DFD/P_LCDM = 1.000 at ALL k (perfect match)
- f_b = 1/nu = 0.157 vs LCDM f_b = 0.156 (0.5% difference)

This would require the DFD scalar field (psi) to provide a non-gravitational enhancement that mimics CDM at recombination.

## Critical Findings

### The Transfer Function Shape Problem

The central challenge: nu(k) only enhances the AMPLITUDE of P_baryon(k), but the SHAPE (T_baryon vs T_LCDM) is set at recombination when MOND is inactive. To match LCDM, DFD needs:

1. **A mechanism that operates at recombination** to modify T(k) -- MOND alone cannot do this
2. **OR** a strongly scale-dependent nu(k) that precisely compensates the shape difference

The QUMOND mode-by-mode nu(k) is scale-dependent, but with the WRONG k-dependence:
- Too much power at k < 0.12 h/Mpc
- Too little at k > 0.12 h/Mpc

### Possible Resolutions for DFD

1. **DFD scalar field (psi)**: The psi field in DFD may provide additional metric perturbations that act like a CDM gravitational potential even at recombination, before MOND activates
2. **Modified interpolating function**: A nu(y) that saturates at ~6.4 rather than diverging as 1/sqrt(y)
3. **Nonlinear field equation effects**: The nonlinearity of the MOND field equation may generate effective contributions not captured by mode-by-mode analysis
4. **Pre-recombination psi growth**: If psi grows during radiation domination (it is not pressure-supported), it could establish a CDM-like potential well before recombination

### The f_b = 1 Distinction

In DFD, ALL matter is baryonic (f_b = 1), but when computing T(k) with Omega_m,eff = nu * Omega_b, the effective baryon fraction is f_b = 1/nu ~ 0.157, which nearly matches LCDM's f_b = 0.156. This is a remarkable coincidence (or not -- it follows from matching Omega_m*h^2).

Consequence: DFD with constant nu = 6.4 predicts BAO wiggles with nearly identical amplitude to LCDM, because f_b enters the EH formula in the same way.

## Numerical Results Summary

| Quantity | LCDM | DFD (QUMOND) | DFD (matched nu=6.4) |
|----------|------|-------------|---------------------|
| sigma_8 | 0.811 | 1.044 | 0.811 |
| z_eq | 3430 | 539 | 3430 |
| r_d (Mpc/h) | 14.4 | 18.2 | 14.4 |
| P(k=0.1)/P_LCDM | 1.0 | 1.30 | 1.00 |
| nu_eff(k=0.1) | -- | 173 | 6.4 |

## Files

- Script: `R3_boss_comparison.py`
- Plot: `R3_boss_comparison.png`
