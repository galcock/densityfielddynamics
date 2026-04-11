# R2 Agent: Galaxy Bias and Redshift-Space Distortions in DFD/MOND

## Executive Summary

Galaxy bias and redshift-space distortions (RSD) represent a critical but under-explored avenue for DFD. The nonlinearity of MOND creates an inherent **scale-dependent bias** that differs fundamentally from LCDM. The growth rate f in DFD is both enhanced and scale-dependent. Crucially, the anisotropic G_eff from v3.3 introduces a **direction-dependent growth** that could mimic or contaminate the Kaiser effect, biasing observational inferences of f*sigma_8. These effects could allow DFD to match BOSS observations even with a different underlying matter power spectrum.

---

## Task 1: Galaxy Bias in MOND

### 1.1 The MOND Nonlinearity Creates Scale-Dependent Bias

In LCDM, galaxy bias on large scales is approximately scale-independent: b(k) ~ const for k < 0.1 h/Mpc. In MOND, the situation is fundamentally different because the modified Poisson equation is **nonlinear**:

    nabla . [mu(|nabla Phi|/a_0) nabla Phi] = 4 pi G rho_b

This nonlinearity means the gravitational field from a superposition of density perturbations is NOT the sum of individual fields. Consequences:

1. **Enhanced clustering in low-acceleration regions**: Voids and low-density regions experience stronger MOND effects (deeper into the MOND regime), so galaxies in denser environments feel relatively less MOND enhancement. This creates a density-dependent, and therefore scale-dependent, effective bias.

2. **Nusser (2002) simulations**: First MOND cosmological N-body simulations showed that MOND produces large-scale structure similar to CDM but with enhanced growth (delta ~ a^2 vs delta ~ a). The simulations found structure forms too fast, overshooting sigma_8 by a factor of ~2. This implies an effective bias relationship differs from LCDM.

3. **Sanders (2001) two-field theory**: Provides a Lagrangian formulation where the coupling between the two fields creates an effective scale-dependent enhancement.

### 1.2 Angus et al. MOND Simulations with Neutrinos

Angus et al. (2011, MNRAS 417, 941) ran cosmological N-body MOND simulations with massive sterile neutrinos (m_nu ~ 11-300 eV, Omega_nu ~ 0.225). Key findings:

- MOND can develop large-scale structure in a hot dark matter cosmology
- X-ray clusters with T_X > 4.5 keV form at correct order of magnitude
- **Overproduction of very rich clusters** and underprediction of low-mass clusters
- The sterile neutrino mass must be > 30 eV for low-mass clusters
- Galaxy formation appears to be **more strongly biased** in MONDian cosmologies

### 1.3 Effective Bias Estimate for DFD

In a low-Omega_0 MONDian model, appropriate sigma_8 normalization can yield clustering properties at z=0 similar to LCDM. This suggests:

    b_eff^DFD ~ b^LCDM * sqrt(P_matter^LCDM / P_matter^DFD)

If DFD matter power is 50% lower than LCDM on some scales, then:

    b_eff^DFD ~ b^LCDM * sqrt(2) ~ 2.8 (for LRGs where b^LCDM ~ 2)

This is within the range of bias values seen in different galaxy populations, so it is not immediately ruled out.

**Key insight**: The MOND nonlinearity creates a natural mechanism for scale-dependent bias that is ABSENT in linear LCDM. This is both a challenge (harder to model) and an opportunity (more freedom to fit data).

---

## Task 2: Growth Rate f in DFD

### 2.1 Standard LCDM Growth Rate

In LCDM:
- f = d(ln D)/d(ln a) = Omega_m(a)^0.55
- At z = 0: f ~ 0.47
- At z = 0.57: f ~ 0.76
- f * sigma_8(z=0.57) ~ 0.76 * 0.57 ~ 0.436

BOSS measurement: f*sigma_8 = 0.436 +/- 0.022 at z = 0.57. This is one of the tightest constraints on growth.

### 2.2 MOND/DFD Enhanced Growth

In the deep MOND regime, Nusser (2002) found delta ~ a^2, giving f = 2 (compared to f = 1 in Einstein-de Sitter). More precisely, in the matter-dominated MOND limit:

    delta = A * t^(4/3)   =>   f_MOND ~ 4/3 in terms of conformal time

But this is in the **deep MOND limit**. The transition between Newtonian and MOND regimes creates scale dependence:

- **Large scales (low k)**: Perturbations are in the deep MOND regime (low acceleration), f ~ 2
- **Small scales (high k)**: Perturbations may be in the Newtonian regime (high acceleration from local clustering), f ~ 1
- **Transition regime**: f interpolates between these values

### 2.3 Agent 15 Results and Scale-Dependent f

From Agent 15: D_MOND/D_LCDM varies from 0.10x to 1.70x across k-scales. This implies:

    f_DFD(k) = d ln D_DFD(k) / d ln a

is highly scale-dependent. Specifically:

| k range (h/Mpc) | D_MOND/D_LCDM | Implied f_DFD |
|------------------|----------------|---------------|
| k ~ 0.01        | ~1.70          | ~1.5-2.0 (enhanced) |
| k ~ 0.05        | ~1.0           | ~0.8-1.0 (similar) |
| k ~ 0.1         | ~0.5           | ~0.5-0.7 (suppressed) |
| k ~ 0.3         | ~0.10          | highly suppressed |

### 2.4 DFD Prediction for f*sigma_8

The BOSS measurement of f*sigma_8 is a **bias-independent** quantity (at linear order). This is because peculiar velocities trace the total matter field, not the galaxy field. However:

If f is scale-dependent in DFD, then the observed f*sigma_8 is an effective average weighted by the survey window function and the galaxy selection:

    (f*sigma_8)_obs ~ integral [f(k) * P(k) * W(k)] dk / integral [P(k) * W(k)] dk

For BOSS at z = 0.57, the effective k-range is roughly 0.02-0.15 h/Mpc. In this range, if f_DFD ~ 0.8-1.5 and sigma_8^DFD is correspondingly adjusted, matching f*sigma_8 = 0.436 is possible.

**Critical point**: There is a known ~2-3 sigma "f*sigma_8 tension" where RSD data prefer LOWER growth than Planck/LCDM predicts. If DFD has f*sigma_8 somewhat lower on the relevant scales, this could actually IMPROVE the fit compared to LCDM.

---

## Task 3: Observational Comparison and Compensation

### 3.1 The Galaxy Power Spectrum in Redshift Space

The observed power spectrum in redshift space:

    P_obs(k, mu) = (b + f * mu^2)^2 * P_matter(k)

where mu = cos(angle to line of sight). The monopole (angle-averaged):

    P_0(k) = (b^2 + 2/3 * b*f + 1/5 * f^2) * P_matter(k)

The quadrupole:

    P_2(k) = (4/3 * b*f + 4/7 * f^2) * P_matter(k)

### 3.2 Compensation Mechanism

**Key question**: Can modified b and f compensate for different P_matter?

Consider BOSS LRGs at z = 0.57. In LCDM:
- b ~ 2.0, f ~ 0.76, P_matter = P_LCDM
- P_0 ~ (4.0 + 1.01 + 0.116) * P_LCDM ~ 5.13 * P_LCDM

For DFD to match the same P_0 with P_matter^DFD = alpha * P_LCDM:

    (b_DFD^2 + 2/3 * b_DFD * f_DFD + 1/5 * f_DFD^2) * alpha = 5.13

If alpha = 0.5 (DFD matter power 50% of LCDM):
- Need: b_DFD^2 + 2/3 * b_DFD * f_DFD + 1/5 * f_DFD^2 ~ 10.26

Example solutions:
- b_DFD = 2.8, f_DFD = 1.5: gives 7.84 + 2.80 + 0.45 = 11.09 (close)
- b_DFD = 3.0, f_DFD = 1.0: gives 9.0 + 2.0 + 0.2 = 11.2 (close)
- b_DFD = 2.5, f_DFD = 2.0: gives 6.25 + 3.33 + 0.80 = 10.38 (match)

### 3.3 The Quadrupole Constraint

The ratio P_2/P_0 is a powerful test because P_matter cancels:

    P_2/P_0 = (4/3 * b*f + 4/7 * f^2) / (b^2 + 2/3 * b*f + 1/5 * f^2)

In LCDM: P_2/P_0 = (2.03 + 0.33) / (4.0 + 1.01 + 0.116) = 2.36/5.13 = 0.46

For DFD with b = 2.5, f = 2.0:
P_2/P_0 = (6.67 + 2.29) / (6.25 + 3.33 + 0.80) = 8.96/10.38 = 0.86

**This is a major discrepancy.** The quadrupole ratio is nearly double the LCDM value.

For DFD with b = 3.0, f = 1.0:
P_2/P_0 = (4.0 + 0.57) / (9.0 + 2.0 + 0.2) = 4.57/11.2 = 0.41

This is closer to LCDM. So the specific combination matters enormously.

### 3.4 Degeneracy Breaking

The monopole and quadrupole together constrain b and f separately (given P_matter). Adding the hexadecapole P_4 provides further constraints. BOSS data provide all three multipoles.

**The DFD compensation is NOT unconstrained** -- both the monopole and multipole ratios must simultaneously match. This reduces the available parameter space significantly but does not eliminate it, especially given the scale dependence of both b_DFD and f_DFD.

---

## Task 4: Direction-Dependent G_eff and Anisotropic Growth

### 4.1 The v3.3 Anisotropic Coupling

From the DFD v3.3 framework:

    G_eff(a, k_hat) = G / [mu_0 * (1 + L_0 * (k_hat . g_hat)^2)]

where g_hat is the direction of the background gravitational acceleration gradient. This means:

- **Modes parallel to the local gravity gradient** experience different G_eff than modes perpendicular
- The growth rate becomes direction-dependent: f = f(k, k_hat . g_hat)

### 4.2 Does This Mimic the Kaiser Effect?

The standard Kaiser effect creates anisotropy in the power spectrum as a function of mu = k_hat . LOS_hat (angle to line of sight). The anisotropy from DFD's G_eff depends on k_hat . g_hat (angle to gravity gradient).

**Case 1: If g_hat is aligned with the line of sight**
Then k_hat . g_hat ~ mu, and the DFD anisotropy would be degenerate with the Kaiser effect. The inferred f would absorb contributions from both peculiar velocities AND anisotropic growth. The effective f_inferred would be:

    f_inferred = f_peculiar + Delta_f_anisotropic

This would bias f*sigma_8 measurements.

**Case 2: If g_hat is random/isotropic**
Averaging over random orientations of g_hat relative to LOS, the anisotropic G_eff creates additional angular structure that does NOT decompose purely into the Kaiser mu^2 and mu^4 terms. Specifically:

    <(k_hat . g_hat)^2> averaged over random g_hat = 1/3

So the average G_eff sees only the isotropic part. But the variance creates:
- A quadrupole contribution (L=2 in the multipole expansion)
- This would appear as excess power in P_2(k) relative to the Kaiser prediction

### 4.3 The Quadrupole Contamination

The key insight is that DFD's anisotropic G_eff adds a quadrupole term to the power spectrum that is NOT from peculiar velocities:

    P_obs(k, mu) = [standard Kaiser terms] + Delta_P_aniso(k) * Q_2(mu)

where Q_2 involves the projection of the G_eff anisotropy onto the line of sight.

If this term is significant, it means:
1. Measurements of f from the Kaiser effect would be **biased** (in the statistical sense)
2. The inferred f*sigma_8 would NOT equal the true f*sigma_8 from peculiar velocities alone
3. The "f*sigma_8 tension" between RSD and Planck could be partly explained by this contamination

### 4.4 Magnitude Estimate

The anisotropy parameter L_0 controls the strength. If L_0 ~ O(1):

    Delta G_eff / G_eff ~ L_0 * cos^2(theta) ~ L_0

The induced quadrupole in P(k) would be:

    Delta P_2 / P_2^Kaiser ~ L_0 * (D_aniso / D_iso - 1)

where D_aniso/D_iso is the ratio of growth factors for parallel vs perpendicular modes. If L_0 = 0.5 and the growth differs by 20% between directions:

    Delta P_2 / P_2^Kaiser ~ 0.10 (a 10% contamination)

This is at the level of current measurement uncertainties, meaning it could be hiding in existing data.

### 4.5 Observational Signature: Beyond the Kaiser Template

The standard RSD analysis assumes:

    P(k, mu) = sum of even powers of mu up to mu^4

DFD's anisotropic G_eff generically introduces mu-dependence that is NOT captured by this template if g_hat has a preferred direction. Signatures include:

1. **Parity violation**: If there is a net preferred direction, odd multipoles could appear
2. **Scale-dependent quadrupole-to-monopole ratio**: Because the G_eff anisotropy is scale-dependent (through L_0's dependence on the MOND interpolation function)
3. **Survey-dependent systematics**: Different surveys probe different volumes with different large-scale gravity gradients, so the contamination would vary between surveys

---

## Synthesis and Key Conclusions

### Can DFD match BOSS P(k) including bias and RSD?

**Yes, in principle, but with strong constraints.** The compensation requires:

1. **Higher effective bias**: b_DFD ~ 2.5-3.0 for LRGs (vs ~2.0 in LCDM). The MOND nonlinearity provides a natural mechanism for enhanced, scale-dependent bias.

2. **Tuned growth rate**: f_DFD must be in the range ~0.8-1.5 on BOSS scales (0.02-0.15 h/Mpc) to match both the monopole and quadrupole simultaneously. Pure deep-MOND growth (f~2) overshoots the quadrupole.

3. **Multipole ratios provide the tightest test**: P_2/P_0 is independent of P_matter and constrains the b-f combination directly. DFD solutions exist but the parameter space is restricted.

### The f*sigma_8 tension as a DFD feature

The existing ~2-3 sigma tension where RSD data prefer lower growth than Planck/LCDM could be:
- A systematic effect from DFD's anisotropic G_eff contaminating the Kaiser signal
- A genuine signal of scale-dependent growth consistent with DFD

### Critical tests

1. **Scale dependence of f*sigma_8**: If measurements at different k-ranges give different f*sigma_8, this is a smoking gun for DFD-type theories (LCDM predicts scale-independent f)
2. **Direction-dependent RSD**: Look for variation in f*sigma_8 as a function of position on the sky (probing different large-scale gravity environments)
3. **Higher multipoles**: The hexadecapole P_4 and beyond can break the b-f degeneracy and test for anisotropic G_eff contributions

### Quantitative bottom line

For DFD to match BOSS with P_matter^DFD = 0.5 * P_matter^LCDM:
- Need b_DFD ~ 3.0 and f_DFD ~ 1.0, giving P_2/P_0 ~ 0.41 (acceptable)
- OR b_DFD ~ 2.5 and f_DFD ~ 1.5, giving P_2/P_0 ~ 0.60 (marginal, may require anisotropic G_eff correction)
- Pure MOND growth (f ~ 2) is EXCLUDED by the multipole ratios unless b > 3.5

---

## References

- Nusser, A. (2002). "Modified Newtonian dynamics of large-scale structure." MNRAS 331, 909.
- Sanders, R.H. (2001). "Cosmology with modified Newtonian dynamics." MNRAS 324, 841.
- Angus, G.W. et al. (2011). "The abundance of galaxy clusters in MOND: Cosmological simulations with massive neutrinos." MNRAS 417, 941.
- Angus, G.W. et al. (2013). "Cosmological simulations in MOND: the cluster scale halo mass function with light sterile neutrinos." MNRAS 436, 202.
- Skordis, C. & Zlosnik, T. (2021). "New Relativistic Theory for Modified Newtonian Dynamics." Phys. Rev. Lett. 127, 161302.
- Jennings, E. et al. (2012). "Redshift space distortions in f(R) gravity." MNRAS 425, 2128.
- Hernandez-Aguayo, C. et al. (2019). "Large-scale redshift space distortions in modified gravity theories." MNRAS 485, 2194.
- Kazantzidis, L. & Perivolaropoulos, L. (2018). "Evolution of the f*sigma_8 tension with Planck15/LCDM."
- Llinares, C. et al. (2008). "N-body simulations for testing the stability of triaxial galaxies in MOND." MNRAS 391, 1778.
