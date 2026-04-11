# Agent 04: Observational P(k) Constraints for DFD
## Literature Research on BOSS DR12, eBOSS DR16, and Related Surveys

Date: 2026-04-04

---

## 1. BOSS DR12 P(k) Measurements

### Survey Parameters
- **LOWZ sample**: 361,762 galaxies, effective redshift z_eff = 0.32
- **CMASS sample**: 777,202 galaxies, effective redshift z_eff = 0.57
- Three redshift bins (z1, z2, z3) with effective redshifts at z ~ 0.32, 0.51, 0.61
- Effective volume: ~18.7 Gpc^3, effective area: 9,329 sq. deg.

### k-Range and Binning
- Power spectrum measured over k = 0.01 - 0.4 h/Mpc (raw measurement range)
- Typical analysis fitting range: k = 0.02 - 0.30 h/Mpc
- Full-shape analyses typically use k_max = 0.15-0.25 h/Mpc depending on the multipole
- Monopole: k_min = 0.02 h/Mpc; Quadrupole: k_min = 0.04 h/Mpc
- Bin width: Delta_k = 0.005 h/Mpc (high resolution) or 0.01 h/Mpc

### Precision of P(k) Monopole
- **k < 0.13 h/Mpc: better than 1% precision** on the monopole
- k ~ 0.1 h/Mpc: statistical errors approximately 2-5% per bin
- k ~ 0.2 h/Mpc: errors grow to approximately 5-10% per bin
- k ~ 0.3 h/Mpc: errors approximately 10-20% per bin
- Systematic errors (star-galaxy separation, fiber collisions, observing conditions) are subdominant to statistical errors for k < 0.2 h/Mpc

### Key Cosmological Constraints from BOSS DR12 Full-Shape
- f(z_LOWZ) * sigma_8(z_LOWZ) = 0.485 +/- 0.044
- f(z_CMASS) * sigma_8(z_CMASS) = 0.436 +/- 0.022
- Fixed-background: f*sigma_8 = 0.447 +/- 0.028 (6% accuracy)
- Full-shape analysis: H0 = 69.6 +1.1/-1.3 km/s/Mpc, sigma_8 = 0.692 +0.035/-0.041

---

## 2. eBOSS DR16 Results

### Tracers and Redshift Coverage
- **Luminous Red Galaxies (LRGs)**: z ~ 0.6 - 1.0
- **Emission Line Galaxies (ELGs)**: z ~ 0.6 - 1.1
- **Quasars (QSOs)**: z_eff ~ 1.48
- **Lyman-alpha forest**: z ~ 2.0 - 3.5

### Power Spectrum Constraints
- ELG analysis: Omega_m = 0.257 +0.031/-0.045, sigma_8 = 0.571 +0.052/-0.076
- QSO analysis at z_eff = 1.48 using EFT-based full-shape analysis

### BAO Precision (Combined BOSS + eBOSS)
- **z < 1: 0.70% aggregate precision** on expansion history
- **z > 1: 1.19% aggregate precision** on expansion history
- 15 distinct high-precision BAO measurements across all tracers
- Lyman-alpha at z=2.35: D_H/r_d = 9.20 +/- 0.36, D_M/r_d = 36.3 +/- 1.8

### Comparison to BOSS DR12
- eBOSS extends BOSS to higher redshifts (z > 0.6)
- Consistent with BOSS at overlapping redshifts
- Combined dataset provides sub-percent BAO constraints

---

## 3. sigma_8 and S8 Constraints (Current Best Values)

### S8 = sigma_8 * sqrt(Omega_m / 0.3)

#### CMB Measurements
| Probe | S8 | sigma_8 |
|-------|-----|---------|
| Planck 2018 | 0.832 +/- 0.013 | 0.811 +/- 0.006 |
| ACT DR6 | 0.875 +/- 0.023 | -- |
| Combined CMB (Planck+ACT+SPT) | 0.836 +/- 0.013 | -- |
| CMB Lensing (ACT+SPT+Planck) | 0.828 +/- 0.012 | -- |

#### Weak Lensing Surveys
| Probe | S8 |
|-------|-----|
| DES Y3 (3x2pt) | 0.776 +/- 0.017 |
| DES Y6 (3x2pt) | 0.789 +/- 0.012 |
| DES Y6 (Shear only) | 0.783 +0.019/-0.015 |
| KiDS-1000 | 0.759 +0.024/-0.021 |
| KiDS Legacy | 0.815 +0.016/-0.021 |
| HSC Y3 (Shear) | 0.776 +0.032/-0.033 |
| HSC Y3 (DESI calibration) | 0.805 +/- 0.018 |

#### Other Probes
| Probe | S8 |
|-------|-----|
| eROSITA clusters | 0.86 +/- 0.01 |
| SPT-3G Clusters | 0.795 +/- 0.029 |
| Planck SZ (Chandra+WL) | 0.78 +/- 0.02 |
| DESI DR1 + Lensing | 0.808 +/- 0.017 |
| Galaxy-Galaxy Lensing (HSCxBOSS) | 0.8294 +/- 0.0110 |
| Peculiar Velocities | 0.819 +/- 0.030 |

### Target for DFD
- **If DFD matches Planck**: sigma_8 ~ 0.811, S8 ~ 0.832
- **If DFD predicts lower value**: S8 ~ 0.78-0.80 would be FAVORED by weak lensing data
- The "sweet spot" for DFD would be S8 in the range 0.79-0.83

---

## 4. The S8 Tension: Opportunity for DFD

### Current Status (2026 Review, arXiv:2602.12238)

The tension landscape has evolved significantly:
- **DES measurements** show 2.4-2.7 sigma tension with Planck
- **KiDS Legacy** has shifted UPWARD to S8 = 0.815, now consistent with Planck at <1 sigma
- **HSC Y3** recalibrated values also moved higher
- Overall assessment: "heterogeneous landscape" -- survey-specific systematics may contribute substantially

### Can DFD Exploit This?

**YES -- this is a significant opportunity.** Key points:

1. **A lower sigma_8 is genuinely preferred by some data.** DES Y3 and DES Y6 both prefer S8 ~ 0.78, which is 2-3 sigma below Planck. If DFD naturally predicts a 3-5% suppression in sigma_8 relative to pure LCDM, this would be PREFERRED by DES data.

2. **Modified gravity models can produce scale-dependent growth suppression.** In theories where gravity is weaker than GR on certain scales, structure formation is suppressed, leading to a lower sigma_8. DFD's density-field approach could naturally produce this.

3. **The tension is NOT fully resolved.** The 2026 review shows a "bifurcation" -- some probes agree with Planck, some are lower. New physics remains viable.

4. **Target range**: DFD should aim for S8 = 0.79-0.83 (sigma_8 = 0.77-0.82). This range is consistent with ALL major probes within 2 sigma.

---

## 5. P(k) Shape: Allowed Deviations from LCDM

### Constraints on Broadband P(k) Shape

This is a critical question. Based on the literature:

#### Statistical Precision of P(k) Measurements
- **k = 0.01-0.05 h/Mpc**: Cosmic variance limited. Errors ~5-15% per bin. Total shape constraint at ~5% level.
- **k = 0.05-0.15 h/Mpc**: Best-measured regime. Errors ~1-5% per bin. Shape constrained at ~2-3% level.
- **k = 0.15-0.30 h/Mpc**: Errors grow. ~5-15% per bin. But systematic uncertainties from nonlinear modeling also grow.

#### Is 30% Deviation Allowed?

**NO -- 30% broadband deviation is NOT allowed in the well-measured regime (k = 0.05-0.15 h/Mpc).**

However, the question is nuanced:
- A **uniform 30% offset** in P(k) amplitude would be ruled out at high significance
- A **scale-dependent** deviation that is small at k < 0.1 h/Mpc and grows to ~30% at k > 0.2 h/Mpc could be partially hidden in nonlinear modeling uncertainties
- At k > 0.2 h/Mpc, theoretical modeling uncertainties (nonlinear bias, fingers-of-god, counterterms) provide ~10-20% "absorption capacity" for deviations

#### Realistic Allowed Deviations (P(k)_DFD / P(k)_LCDM)
| k range (h/Mpc) | Allowed deviation | Notes |
|------------------|-------------------|-------|
| 0.01 - 0.05 | < 5-10% | Cosmic variance limited but well-constrained shape |
| 0.05 - 0.10 | < 3-5% | Best-measured regime |
| 0.10 - 0.15 | < 5-8% | Still well constrained |
| 0.15 - 0.20 | < 8-15% | Nonlinear effects growing |
| 0.20 - 0.30 | < 15-25% | Absorbed by EFT counterterms |

**CRITICAL IMPLICATION FOR DFD**: The success criterion of "30% deviation allowed" is too generous for k < 0.15 h/Mpc. DFD must match LCDM to better than ~5% in the range k = 0.05-0.15 h/Mpc. The 30% criterion may only apply at k > 0.2 h/Mpc where nonlinear effects dominate.

---

## 6. BAO Feature Constraints

### BAO Peak Position
- **Precision: sub-percent (0.7-1.2%)** from combined BOSS + eBOSS
- The BAO scale (sound horizon r_s ~ 147 Mpc) is measured to ~0.3% from Planck CMB
- Galaxy surveys constrain D_V/r_s or D_A/r_s and D_H/r_s ratios to ~1%
- **DFD MUST preserve the BAO peak position to ~1%** -- this is non-negotiable

### BAO Amplitude (Wiggle Amplitude)
- The BAO wiggles are damped by nonlinear structure formation (Silk damping scale Sigma_nl ~ 5-10 Mpc/h)
- The amplitude of BAO wiggles in the galaxy power spectrum is ~5-10% of the smooth broadband power
- Pre-reconstruction: wiggle amplitude damped by factor ~exp(-k^2 Sigma_nl^2 / 2)
- Post-reconstruction: amplitude partially restored
- **Constraint on BAO amplitude**: Less stringent than peak position. Deviations of ~20-30% in wiggle amplitude are within current modeling uncertainties
- **DFD SHOULD preserve approximate BAO amplitude** but exact matching is not critical

### BAO Scale Requirements for DFD
1. Peak position: match to ~1% (i.e., sound horizon calculation must be correct)
2. Peak width: controlled by damping scale, ~10-20% tolerance
3. Peak amplitude: ~20-30% tolerance (hidden in nonlinear damping uncertainties)

---

## 7. Modified Gravity Constraints from P(k) Analyses

### f(R) Gravity (Hu-Sawicki Model)

From BOSS full-shape analysis (Alvarez et al. 2025, PRD 111, L021301):
- **|f_R0| < 5.89 x 10^-6** (68% CL)
- **|f_R0| < 1.53 x 10^-5** (95% CL)
- Analysis range: k = 0.02 - 0.17 h/Mpc
- Key finding: models with |f_R0| = 10^-6 produce P(k) differences indistinguishable from LCDM noise
- "Highly unlikely these constraints will be significantly improved by future galaxy spectroscopic catalogs"

### Phenomenological Modified Gravity (mu-Sigma Framework)

From DESI 2024 (arXiv:2411.12026):
- **mu_0 = 0.11 +0.44/-0.54** (DESI alone) -- consistent with GR (mu_0 = 0)
- **mu_0 = 0.05 +/- 0.22** (DESI + CMB + DES Y3 + SNe)
- **Sigma_0 = 0.008 +/- 0.045** (combined) -- GR prediction is Sigma_0 = 0
- **eta_0 = 0.09 +0.36/-0.60** (gravitational slip)
- Analysis range: k = 0.02 - 0.20 h/Mpc, Delta_k = 0.005 h/Mpc
- All parameters consistent with GR at current precision

### What This Means for DFD
- Current data constrain mu (the ratio of the effective gravitational constant to Newton's G) to ~0.05 +/- 0.22 (combined)
- This means **the effective gravitational coupling can deviate from GR by up to ~20% at 1-sigma**
- DFD must predict deviations in the mu-Sigma framework that are within these bounds
- If DFD predicts mu_0 ~ 0.05-0.10, this is perfectly consistent with current data

### Complementary Constraints
- Weak lensing: |f_R0| < 1.51 x 10^-5
- Cluster observations: |f_R0| < 4.79 x 10^-6
- Astrophysical bounds: |f_R0| < 10^-8 (much tighter, from stellar/galactic scales)

---

## 8. Summary: What DFD Must Match

### Hard Constraints (Must satisfy)
1. **BAO peak position**: to ~1% accuracy
2. **P(k) shape at k = 0.05-0.15 h/Mpc**: deviation < 5% from LCDM
3. **P(k) amplitude (sigma_8)**: must be in range sigma_8 = 0.77-0.85
4. **Growth rate f*sigma_8**: must match BOSS measurements at z=0.32 and z=0.57 within ~6%

### Soft Constraints (Strong preference)
5. **P(k) shape at k = 0.01-0.05 h/Mpc**: deviation < 10%
6. **BAO wiggle amplitude**: match to ~30%
7. **Modified gravity parameters**: mu_0 within +/- 0.22 of zero

### Opportunities (Where DFD could improve on LCDM)
8. **S8 tension**: DFD predicting S8 ~ 0.79-0.81 would be FAVORED by DES data while being consistent with Planck at ~2 sigma
9. **Scale-dependent growth**: if DFD produces mild suppression at k > 0.1 h/Mpc, this could help explain the S8 tension
10. **The 30% success criterion**: only realistic for k > 0.2 h/Mpc; for k < 0.15 h/Mpc the criterion should be tightened to ~5%

### Revised Success Criteria Recommendation
| k range (h/Mpc) | Maximum allowed |P(k)_DFD/P(k)_LCDM - 1| |
|------------------|-------------------------------------------------|
| 0.01 - 0.05 | 10% |
| 0.05 - 0.15 | 5% |
| 0.15 - 0.25 | 15% |
| 0.25 - 0.30 | 25% |
| BAO peak position | 1% |

---

## Key References

- Gil-Marin et al. 2017 (MNRAS 465, 1757): BOSS DR12 RSD from P(k) and bispectrum
- D'Amico et al. 2022 (PRD 105, 043517): BOSS DR12 full-shape LCDM constraints
- Beutler & McDonald 2021 (JCAP 11, 031): Unified galaxy P(k) from 6dFGS, BOSS, eBOSS
- Alvarez et al. 2025 (PRD 111, L021301): First scale-dependent modified gravity constraints from BOSS full-shape P(k)
- Aviles & Niz 2024 (JCAP 03, 049): fkPT methodology for modified gravity P(k)
- DESI Collaboration 2024 (arXiv:2411.12026): Modified gravity constraints from DESI 2024
- DESI Collaboration 2024 (arXiv:2404.03002): DESI BAO cosmological constraints
- Asgari et al. 2021: KiDS-1000 cosmic shear
- DES Collaboration 2022: DES Y3 results
- Wright et al. 2025: KiDS Legacy analysis
- Amon & Efstathiou 2022 (arXiv:2209.06217): "The Sigma-8 Tension is a Drag"
- Haridasu et al. 2026 (arXiv:2602.12238): Status of the S8 Tension: A 2026 Review
