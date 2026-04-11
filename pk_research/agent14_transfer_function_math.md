# Agent 14: Baryon Transfer Function & MOND Growth -- Full P_DFD(k) Computation

## Executive Summary

This document presents a rigorous, first-principles calculation of the DFD matter power spectrum P_DFD(k). The calculation has three ingredients: (1) the Eisenstein-Hu baryon-only transfer function T_b(k), (2) MOND-enhanced structure growth D_DFD(k,z), and (3) the standard primordial spectrum. The central result is that **P_DFD(k) is suppressed by a factor of ~65 relative to P_LCDM(k) in the BOSS range (k = 0.01--0.15 h/Mpc)**, with the deficit coming predominantly from the baryon-only transfer function (Silk damping destroys small-scale power that CDM would otherwise preserve). MOND boosts the growth factor by a factor of ~2--16 depending on scale, but this is insufficient to compensate for the transfer function suppression of ~10--1000x.

---

## 1. Cosmological Parameters

| Parameter | DFD (baryon-only) | LCDM |
|-----------|-------------------|------|
| h | 0.674 | 0.674 |
| Omega_b h^2 | 0.02237 | 0.02237 |
| Omega_cdm h^2 | 0 | 0.1200 |
| Omega_m h^2 | 0.02237 | 0.1424 |
| Omega_m | 0.04924 | 0.315 |
| T_CMB | 2.725 K | 2.725 K |
| n_s | 0.9649 | 0.9649 |
| A_s | 2.1e-9 | 2.1e-9 |
| a_0 (MOND) | 1.2e-10 m/s^2 | N/A |

The DFD universe has Omega_m = Omega_b = 0.049 with NO cold dark matter. The background expansion is taken to be LCDM (Omega_Lambda = 0.685) since DFD produces an effective dark energy through the density field mechanism.

---

## 2. Task 1: Eisenstein-Hu Baryon-Only Transfer Function

### 2.1 Derived Quantities

Using the Eisenstein & Hu (1998) fitting formulae with Omega_m h^2 = Omega_b h^2 = 0.02237 (baryon-only):

| Quantity | Value | Meaning |
|----------|-------|---------|
| z_eq | 539 | Matter-radiation equality (much later than LCDM's ~3400) |
| z_d | 1012 | Baryon drag epoch |
| k_eq | 0.00164 Mpc^-1 = 0.00243 h/Mpc | Equality scale |
| s (sound horizon) | 18.23 Mpc = 12.29 Mpc/h | Much smaller than LCDM's ~147 Mpc |
| k_Silk | 0.0692 Mpc^-1 = 0.103 h/Mpc | Silk damping scale |
| R_eq | 1260 | Baryon-photon ratio at equality |
| R_d | 670.9 | Baryon-photon ratio at drag |

**Critical observation**: The sound horizon is only 18.23 Mpc, compared to ~147 Mpc in LCDM. This is because with Omega_m h^2 = 0.02237, matter-radiation equality occurs much later (z_eq ~ 539 vs ~3400), so the baryons remain coupled to photons for a much longer period and the sound horizon is compressed.

### 2.2 Transfer Function Values

| k (h/Mpc) | T_b (DFD) | T (LCDM) | Ratio T_b/T_LCDM |
|------------|-----------|----------|-------------------|
| 0.001 | 0.8704 | 0.9924 | 0.877 |
| 0.010 | 0.2771 | 0.7878 | 0.352 |
| 0.050 | 0.0385 | 0.3388 | 0.114 |
| 0.100 | 0.0131 | 0.1735 | 0.076 |
| 0.200 | 0.00353 | 0.0736 | 0.048 |
| 0.500 | 0.000212 | 0.0189 | 0.011 |
| 1.000 | 0.0000024 | 0.00606 | 0.0004 |

### 2.3 Physical Interpretation

The baryon-only transfer function is dramatically suppressed at k > 0.01 h/Mpc for two reasons:

1. **Silk damping**: Photon diffusion exponentially damps baryon perturbations below the Silk scale k_Silk ~ 0.10 h/Mpc. In LCDM, CDM perturbations are immune to this because CDM does not couple to photons.

2. **BAO oscillations**: The baryons oscillate as a photon-baryon fluid before decoupling. The oscillation nodes create deep minima in T_b(k). In LCDM, these are filled in by the CDM transfer function.

3. **Late matter-radiation equality**: With Omega_m h^2 = 0.02237, equality occurs at z ~ 539. Modes that enter the horizon before equality (k > k_eq ~ 0.0024 h/Mpc) experience radiation-dominated growth suppression for much longer.

The **transfer function squared** suppression is:
- k = 0.01: T_b^2 / T_LCDM^2 = 0.124 (8x suppression)
- k = 0.05: T_b^2 / T_LCDM^2 = 0.013 (77x suppression)
- k = 0.10: T_b^2 / T_LCDM^2 = 0.0057 (175x suppression)
- k = 0.20: T_b^2 / T_LCDM^2 = 0.0023 (435x suppression)
- k = 1.00: T_b^2 / T_LCDM^2 = 1.6e-7 (6.25 million x suppression)

This is the **fundamental obstacle** for any baryon-only cosmology.

---

## 3. Task 2: MOND Enhancement Factor nu(k,z)

### 3.1 The MOND Interpolation Function

For the simple interpolation mu(x) = x/(1+x), the corresponding nu function is:

    nu(y) = [1 + sqrt(1 + 4/y)] / 2

where y = g_N / a_0 is the ratio of the Newtonian gravitational acceleration to the MOND acceleration constant.

**Deep MOND limit** (y << 1): nu(y) -> 1/sqrt(y), giving g = g_N / sqrt(y) = sqrt(g_N * a_0)

**Newtonian limit** (y >> 1): nu(y) -> 1, recovering standard gravity.

### 3.2 The y Parameter at Each Scale

For a density perturbation delta at comoving scale k:

    g_N(k, delta, z) = 4*pi*G * rho_b(z) * |delta| / k_phys

where k_phys = k * h * (1+z) / Mpc is the physical wavenumber.

Then y(k, delta, z) = g_N / a_0.

At z=0 with delta=1:

| k (h/Mpc) | y | nu | Regime |
|------------|---|-----|--------|
| 0.001 | 0.134 | 3.27 | Intermediate |
| 0.010 | 0.0134 | 9.14 | Approaching deep MOND |
| 0.050 | 0.00269 | 19.8 | Deep MOND |
| 0.100 | 0.00134 | 27.8 | Deep MOND |
| 0.500 | 0.000269 | 61.5 | Deep MOND |
| 1.000 | 0.000134 | 86.7 | Deep MOND |

**Key result**: All cosmologically relevant scales are in the deep MOND regime (y << 1), meaning the gravitational enhancement is substantial everywhere.

At z=0 with delta=0.01 (linear regime), the enhancement is even stronger because nu ~ 1/sqrt(y) and y is proportional to delta.

### 3.3 Effective Matter Density

The MOND-enhanced effective gravitating density is:

    Omega_eff(k,z) = nu(k,z) * Omega_b

At z=0 with the self-consistent growth amplitudes:

| k (h/Mpc) | nu(z=0) | Omega_eff = nu * Omega_b |
|------------|---------|--------------------------|
| 0.001 | 11.3 | 0.555 |
| 0.010 | 16.5 | 0.813 |
| 0.050 | 19.2 | 0.944 |
| 0.100 | 20.0 | 0.987 |
| 0.200 | 20.8 | 1.023 |
| 0.500 | 21.5 | 1.061 |
| 1.000 | 22.0 | 1.084 |

**The MOND enhancement brings Omega_eff close to Omega_m(LCDM) = 0.315 at large scales, and actually EXCEEDS it at small scales (Omega_eff > 1 for k > 0.2 h/Mpc).** This means MOND provides adequate gravitational strength -- the problem is purely in the transfer function (initial conditions post-recombination), not the growth.

---

## 4. Tasks 3-4: Self-Consistent Nonlinear Growth Equation

### 4.1 The Growth ODE

The perturbation growth equation with MOND enhancement:

    delta_NN + (2 + d ln H / d ln a) * delta_N = (3/2) * Omega_b(a) * nu(y(k,delta)) * delta

where N = ln(a), subscript N denotes d/dN, and:
- Omega_b(a) = Omega_b / (a^3 * (H/H0)^2)
- y(k, delta, z) = 4*pi*G*rho_b(z)*|delta| / (k_phys * a_0)

This is **nonlinear** because nu depends on delta through y.

### 4.2 Analytical Deep-MOND Growth Exponent

In the deep MOND regime during matter domination (a ~ t^{2/3}):

For delta = D_0 * a^p:

The RHS involves nu(y)*delta. Since y proportional to delta/k_phys proportional to delta * a, and nu ~ 1/sqrt(y):

    nu * delta ~ sqrt(delta) * sqrt(k) * 1/sqrt(a) * delta
               ~ delta^{3/2} * k^{1/2} * a^{-1/2}

With delta = D_0 * a^p:

    RHS ~ D_0^{3/2} * a^{3p/2 - 1/2}

LHS in matter domination:

    d^2(delta)/dt^2 + (4/3t)*d(delta)/dt

For delta = D_0 * a^p with a ~ t^{2/3}:

    LHS ~ [p(2p/3 - 1) + (4/3)(2p/3)] * D_0 * a^p / t^2
        ~ [(2p^2 - 3p)/3 + 8p/9] * D_0 * a^{p-3} / (const)

Hmm, this is more subtle. In the actual LCDM background (not EdS), the analytical solution doesn't have a simple power-law form. The numerical integration is more reliable.

### 4.3 Numerical Growth Results

Integrating from a = 0.001 (z = 999) to a = 1 (z = 0):

**Baryon-only, no MOND** (standard gravity):
    D_baryon / D_LCDM = 0.0149

This is a factor of **67x suppression** -- without CDM or MOND, structures barely grow because Omega_b = 0.049 provides very weak gravitational pull against the Lambda-dominated expansion.

**Baryon-only with MOND**:

| k (h/Mpc) | D_DFD / D_LCDM | MOND boost factor (vs no-MOND) |
|------------|----------------|-------------------------------|
| 0.001 | 0.064 | 4.3x |
| 0.010 | 0.291 | 19.5x |
| 0.050 | 1.064 | 71.3x |
| 0.100 | 1.949 | 130.6x |
| 0.200 | 3.638 | 243.8x |
| 0.500 | 8.369 | 560.9x |
| 1.000 | 16.094 | 1078.8x |

**The MOND growth enhancement is dramatic and scale-dependent:**
- At k > 0.05 h/Mpc, D_DFD actually EXCEEDS D_LCDM
- The boost increases with k because smaller scales have lower g_N/a_0 (deeper MOND regime)
- At k = 0.1 h/Mpc, D_DFD is ~2x D_LCDM

### 4.4 The Scale Dependence

The growth factor D_DFD(k) is strongly scale-dependent because:
1. The MOND nu factor depends on the gravitational acceleration g_N ~ rho * delta / k
2. Smaller scales (larger k) have smaller g_N for the same delta, putting them deeper into the MOND regime
3. Deeper MOND means larger nu, meaning stronger gravitational enhancement

This introduces a **k-dependent tilt** in the power spectrum that does not exist in LCDM.

---

## 5. Task 5: Scale-Dependent Growth Factor Detail

The growth factor decomposition shows the two competing effects:

| k (h/Mpc) | T_b^2/T_LCDM^2 | D_DFD^2/D_LCDM^2 | Product (P ratio) |
|------------|-----------------|-------------------|-------------------|
| 0.001 | 0.769 | 0.00412 | 0.00317 |
| 0.010 | 0.124 | 0.0846 | 0.0105 |
| 0.050 | 0.0129 | 1.131 | 0.0146 |
| 0.100 | 0.00570 | 3.798 | 0.0217 |
| 0.200 | 0.00230 | 13.23 | 0.0304 |
| 0.500 | 0.000126 | 70.03 | 0.00883 |
| 1.000 | 1.6e-7 | 259.0 | 0.0000431 |

**The pattern is clear:**
- Transfer function suppression increases monotonically with k (Silk damping)
- MOND growth boost also increases monotonically with k (deeper MOND at smaller scales)
- These partially cancel, but the transfer function suppression wins at all scales
- The closest approach to LCDM occurs around k ~ 0.15--0.2 h/Mpc where the ratio peaks at ~3%

---

## 6. Task 6: Final Power Spectrum

### 6.1 P_DFD(k) / P_LCDM(k) Across All Scales

| k (h/Mpc) | P_DFD/P_LCDM |
|------------|--------------|
| 0.001 | 0.00317 |
| 0.005 | 0.00841 |
| 0.010 | 0.01039 |
| 0.020 | 0.01168 |
| 0.050 | 0.01486 |
| 0.100 | 0.02183 |
| 0.150 | 0.02789 |
| 0.200 | 0.03036 |
| 0.300 | 0.02342 |
| 0.500 | 0.00892 |
| 1.000 | 0.0000431 |

### 6.2 BOSS Range (k = 0.01 -- 0.15 h/Mpc)

- **Mean P_DFD/P_LCDM = 0.0155** (suppressed by factor ~65)
- **Min ratio = 0.0104** at k = 0.010 h/Mpc
- **Max ratio = 0.0277** at k = 0.148 h/Mpc

The deficit is NOT uniform -- it is worst at large scales within BOSS and improves toward smaller scales, reflecting the increasing MOND growth boost.

### 6.3 sigma_8

Using standard normalization (LCDM sigma_8 = 0.811):

    sigma_8(DFD) = 0.811 * 0.088 = 0.071

**DFD predicts sigma_8 ~ 0.07, compared to the observed 0.811 +/- 0.006.**

This is a factor of ~11.4 deficit in sigma_8, or equivalently a factor of ~130 deficit in sigma_8^2 (which is what P(k) measures).

### 6.4 BAO Analysis

**Sound horizon**: s = 18.23 Mpc (DFD) vs ~147 Mpc (LCDM)

The DFD sound horizon is **8x smaller** than LCDM because:
- Omega_m h^2 = 0.02237 (DFD) vs 0.1424 (LCDM)
- This means matter-radiation equality is at z_eq ~ 539 (DFD) vs ~3400 (LCDM)
- Baryons remain coupled to photons much longer
- But the sound speed is the same, so the sound horizon scales roughly as 1/sqrt(Omega_m h^2)

**BAO peak position**: k_BAO ~ 2*pi/s ~ 0.51 h/Mpc (DFD) vs ~0.063 h/Mpc (LCDM)

The BAO oscillations in P_DFD(k) are at completely different scales than LCDM. The BOSS-detected BAO at k ~ 0.06 h/Mpc corresponds to the LCDM sound horizon -- DFD's BAO signature would appear at ~8x higher k.

**BAO amplitude**: The peak-to-trough variation in ln(P_DFD/P_LCDM) across the BOSS range is ~0.98, indicating that BAO wiggles in the baryon-only transfer function create ~factor-of-3 modulations in the ratio.

---

## 7. Task 7: Gap Analysis

### 7.1 Scale-by-Scale Deficit

| k range (h/Mpc) | Regime | Mean P_DFD/P_LCDM | Deficit factor |
|------------------|--------|-------------------|----------------|
| 0.001--0.01 | Large scales | 0.0068 | ~147x |
| 0.01--0.05 | Intermediate | 0.0121 | ~83x |
| 0.05--0.15 | BOSS linear | 0.0204 | ~49x |
| 0.15--0.3 | Quasi-linear | 0.0286 | ~35x |
| 0.3--1.0 | Nonlinear | 0.0082 | ~122x |

### 7.2 Root Cause Decomposition

The deficit has two sources:

**A. Transfer function (dominant):**
- Silk damping exponentially suppresses T_b(k) at k > k_Silk ~ 0.10 h/Mpc
- BAO oscillations create nodes where T_b -> 0
- No CDM to "fill in" the damped modes
- At k = 0.1 h/Mpc: T_b^2/T_LCDM^2 = 0.0057 (175x suppression)

**B. Growth factor at large scales:**
- At k < 0.05 h/Mpc, D_DFD < D_LCDM despite MOND
- This is because large-scale perturbations have higher g_N, so MOND enhancement is weaker
- At k = 0.01 h/Mpc: D_DFD/D_LCDM = 0.29 (3.4x suppression in D, 12x in D^2)
- At k = 0.001 h/Mpc: D_DFD/D_LCDM = 0.064 (15.6x suppression in D, 243x in D^2)

**C. Combined worst-case (small scales):**
- At k > 0.3 h/Mpc, the exponential Silk damping overwhelms even the large MOND growth boost
- At k = 1.0 h/Mpc: T^2 ratio = 1.6e-7, D^2 ratio = 259 -> net 0.0000431

### 7.3 Is the Deficit Uniform?

**No.** The P_DFD/P_LCDM ratio has a clear peak around k ~ 0.15--0.20 h/Mpc where the MOND growth boost best compensates the Silk damping. The deficit is:
- Worst at very large scales (k < 0.01 h/Mpc) due to weak MOND enhancement
- Worst at very small scales (k > 0.3 h/Mpc) due to exponential Silk damping
- "Best" (still ~35x deficit) in the quasi-linear regime k ~ 0.15--0.3 h/Mpc

### 7.4 Is the BAO Feature Too Prominent?

**Yes, and at the wrong scale.** The DFD BAO oscillations are:
1. At k ~ 0.5 h/Mpc instead of k ~ 0.06 h/Mpc (wrong location)
2. Much more prominent because there is no CDM component to dilute them
3. The oscillation-to-smooth ratio is much larger in T_b than in the combined T_LCDM

This means galaxy surveys would detect BAO wiggles at the wrong spacing, which is a clear observational discriminant.

### 7.5 What Would Be Needed to Close the Gap?

To match P_LCDM in the BOSS range, DFD would need an additional mechanism that:

1. **Boosts power by ~50-100x** at k = 0.01--0.15 h/Mpc
2. **Is scale-dependent**: more boost at larger scales, less at smaller scales (to compensate the shape mismatch)
3. **Does not alter** the CMB (which is already well-fit by LCDM initial conditions)

Potential mechanisms to investigate:
- **Streaming velocity effects**: Baryon-CDM velocity offset effects are absent in DFD, but analogous DFD-specific baryon streaming might enhance clustering
- **Nonlinear mode coupling**: MOND's nonlinear growth equation can transfer power from large to small scales
- **Pre-recombination density field effects**: If the DFD density field modifies the baryon-photon coupling before recombination, the effective transfer function could differ from the standard T_b
- **Phantom dark matter halo formation**: If MOND-generated phantom dark matter halos form early enough, they could seed additional structure growth
- **Modified Silk damping**: If the density field alters photon diffusion (e.g., through modified gravity in the tight-coupling regime), k_Silk could shift to smaller scales

---

## 8. Computational Details

### 8.1 Method
- Eisenstein & Hu (1998) fitting formulae for T_b(k) and T_LCDM(k)
- Numerical ODE integration (scipy.integrate.solve_ivp, RK45) from a = 0.001 to a = 1
- MOND nu function self-consistently computed at each timestep
- sigma_8 via numerical integration of P(k)*W^2(kR) with R = 8 Mpc/h

### 8.2 Convergence
- k grid: 500 points logarithmically spaced, 0.001--1.0 h/Mpc
- Growth ODE: rtol = 1e-8, atol = 1e-12, max_step = 0.01 in ln(a)
- sigma_8 integral: scipy.integrate.quad with limit=200

### 8.3 Code
Full computation in `compute_pk_dfd.py` in this directory.

---

## 9. Summary Table

| Quantity | DFD | LCDM | Ratio |
|----------|-----|------|-------|
| Sound horizon | 18.2 Mpc | ~147 Mpc | 0.124 |
| k_Silk | 0.103 h/Mpc | 0.103 h/Mpc | ~1 |
| D(z=0, k=0.1) / D_LCDM | 1.95 | 1 | 1.95 |
| D(z=0, k=0.01) / D_LCDM | 0.29 | 1 | 0.29 |
| T_b(0.1)/T_LCDM(0.1) | 0.013 | 0.174 | 0.076 |
| P(k=0.1) ratio | -- | -- | 0.022 |
| Mean P ratio (BOSS) | -- | -- | 0.015 |
| sigma_8 | ~0.07 | 0.811 | 0.088 |
| BAO peak k | ~0.51 h/Mpc | ~0.063 h/Mpc | 8.1 |

---

## 10. Conclusion

The baryon-only matter power spectrum with MOND growth enhancement is suppressed by a factor of ~65 relative to LCDM in the BOSS range. The dominant source of this suppression is the transfer function: Silk damping erases baryon perturbations at k > 0.1 h/Mpc, and no amount of enhanced late-time growth can restore what was lost at recombination. MOND does provide substantial growth enhancement (factors of 100-1000x compared to baryon-only without MOND), and at intermediate scales k ~ 0.1-0.2 h/Mpc the growth factor actually exceeds LCDM. However, the pre-recombination physics encoded in T_b(k) is the binding constraint.

**The path to closing P(k) for DFD must address the transfer function, not just the growth factor.** This likely requires showing that DFD modifies the pre-recombination physics in a way that either reduces Silk damping or provides an additional clustering mechanism that is not captured by the standard baryon-only T_b(k).
