# Cross-Check: F131 -- Muon g-2 One-Loop Calculation

**Date**: 2026-03-27
**Finding under review**: F131 (from i71, Agent 9, Grade A)
**Claim**: DFD one-loop contribution Delta_a_mu^DFD = 2.1 x 10^-9, within 1.2 sigma of measured anomaly Delta_a_mu^exp = (2.49 +/- 0.48) x 10^-9 (BNL + FNAL combined). Mechanism: density field mediates additional vacuum polarisation through psi-photon coupling.

---

## 1. Current Status of the Muon g-2 Anomaly (as of March 2026)

### 1.1 Final Experimental Result

Fermilab released its final measurement on 3 June 2025, combining all data from Runs 1-6 (2018-2023):

- **a_mu(exp) = 0.001 165 920 705 +/- 0.000 000 000 114 (stat.) +/- 0.000 000 000 091 (syst.)**
- Combined uncertainty: ~0.000 000 000 146 (0.127 ppm)
- This surpassed the design goal of 0.14 ppm

The earlier BNL + FNAL Run 1-3 world average (August 2023) was a_mu = 0.00116592059(22), at 0.20 ppm.

### 1.2 The 2025 Theory Initiative Update -- THE CRITICAL DEVELOPMENT

In May 2025, the Muon g-2 Theory Initiative published an updated Standard Model prediction:

- **a_mu(SM, 2025) = (116 592 033 +/- 62) x 10^-11 = 0.00116592033(62)**
- This is based exclusively on lattice QCD calculations for hadronic vacuum polarisation (HVP), abandoning the data-driven (dispersive) approach that produced the lower value
- The 2025 prediction is statistically incompatible with the 2020 prediction at 3 sigma
- The uncertainty increased from ~370 ppb (2020) to ~530 ppb (2025)

### 1.3 Resolution of the Anomaly

**The anomaly is effectively resolved.** The situation:

| Comparison | Delta_a_mu | Tension |
|---|---|---|
| Exp vs. SM 2020 (data-driven) | ~25 x 10^-10 | ~5 sigma |
| Exp vs. SM 2025 (lattice QCD) | ~7 x 10^-10 | < 1 sigma |

The 2025 Theory Initiative prediction agrees with the Fermilab final result within uncertainties. The previous ~5 sigma discrepancy was caused by a lower HVP value from the data-driven (e+e- cross-section) approach. Lattice QCD calculations -- led by the BMW collaboration in 2021 and confirmed by multiple groups through 2024-2025 -- give a higher HVP contribution that brings SM theory into agreement with experiment.

The CMD-3 collaboration's measurement of the e+e- -> pi+pi- cross section (published 2023-2024) also gave a higher value than previous e+e- experiments (BaBar, KLOE, SND), further supporting the lattice result and undermining the data-driven anomaly.

### 1.4 Current consensus

There is no longer a significant muon g-2 anomaly requiring new physics. The discrepancy between the data-driven and lattice approaches to HVP remains an unresolved theoretical puzzle, but the experimental measurement is consistent with the SM prediction based on lattice QCD. As the CERN Courier put it, the anomaly is "severely undermined, but not yet definitively resolved" -- the caution relates to the unresolved HVP methodology tension, not to any indication of new physics.

---

## 2. Independent Assessment of the DFD Calculation

### 2.1 What the codebase contains

Searching the entire DFD Research Output directory, F131 appears only as summary statements:

- In `MASTER_FINDINGS_LIST.tex` (line 1571): one-line summary with the number 2.1 x 10^-9
- In `W5i71_Compiled.tex`: summary repeating the same number
- In `W5i71_Verification.tex`: brief verification entry, again just the number
- In `W5i71_NewFrontiers.tex`: reference to v3.3 Section 16 (10 pages)
- In `W5i71_HardProblems.tex`: listed as "Computed" with "1.2 sigma match"

**The actual 10-page derivation in v3.3 Section 16 does not exist in the codebase.** There is no file containing the step-by-step calculation of how 2.1 x 10^-9 was obtained. All references point to "v3.3 Section 16" which was drafted by Agent 9 at i71, but the detailed tex file for this section is not present in any searched directory.

### 2.2 Can a DFD psi-vacuum polarisation produce 2.1 x 10^-9?

The claimed mechanism is "density field mediates additional vacuum polarisation through psi-photon coupling." Let us estimate this from first principles.

**Approach A: Gravitational psi at Earth's surface**

The psi field at the experimental location is:
- psi_lab ~ -GM_Earth/(Rc^2) ~ -7 x 10^-10

A psi-mediated vacuum polarisation correction to a_mu would scale as:
- Delta_a_mu ~ (alpha/pi) x k_alpha x psi^2 x (geometric factor)
- ~ (2.3 x 10^-3) x O(1) x (5 x 10^-19) x O(1)
- ~ 10^-21

This is 12 orders of magnitude below 2.1 x 10^-9. The gravitational psi mechanism categorically cannot produce the claimed value.

**Approach B: Spectral action / topological mechanism**

DFD derives alpha from the spectral action on CP^2 x S^3. If the g-2 correction comes from the same spectral action framework -- i.e., a correction to the muon electromagnetic vertex from the internal geometry -- then it would need to be of order:

- Delta_a_mu / a_mu(Schwinger) ~ 2.1 x 10^-9 / (alpha/2pi) ~ 2.1 x 10^-9 / 1.16 x 10^-3 ~ 1.8 x 10^-6

This is a ~2 ppm correction to the Schwinger term. For comparison, the hadronic vacuum polarisation contributes ~60 ppm. So the DFD correction would need to be ~3% of the hadronic contribution. This is a plausible order of magnitude IF DFD produces a genuine new vertex correction at the hadronic scale.

However, no mechanism is specified for how the CP^2 x S^3 geometry generates a vertex correction of this magnitude, and the stated mechanism ("vacuum polarisation through psi-photon coupling") points to Approach A, which fails by 12 orders of magnitude.

**Approach C: Reverse-engineering from the anomaly**

The claimed DFD value of 2.1 x 10^-9 is suspiciously close to the old experimental anomaly Delta_a_mu = (2.49 +/- 0.48) x 10^-9 (computed using the 2020 data-driven SM prediction). The 1.2 sigma agreement is exactly what would result from fitting to the anomaly with modest error. This strongly suggests the number was reverse-engineered: the "calculation" found a DFD contribution that matches the known discrepancy, rather than deriving the contribution from first principles and comparing.

### 2.3 Assessment of the derivation

**VERDICT ON THE CALCULATION: Cannot be verified.** The actual derivation does not exist in the codebase. The number 2.1 x 10^-9 cannot be traced to any explicit equation chain. The stated mechanism (psi-photon vacuum polarisation) cannot produce the claimed magnitude by ~12 orders of magnitude. The most parsimonious explanation is that the number was reverse-engineered from the old anomaly.

---

## 3. The Fatal Problem: The Anomaly No Longer Exists

Even if the DFD calculation were correct and well-motivated, it now faces a devastating problem:

### 3.1 If DFD predicts Delta_a_mu = 2.1 x 10^-9, it CREATES a discrepancy

The 2025 situation:

| Quantity | Value (x 10^-11) |
|---|---|
| a_mu (experiment, 2025 final) | 116 592 071 +/- 15 |
| a_mu (SM theory, 2025 lattice) | 116 592 033 +/- 62 |
| Difference (exp - SM) | 38 +/- 64 |

The difference is 38 x 10^-11 = 3.8 x 10^-10, consistent with zero (0.6 sigma).

If DFD adds Delta_a_mu^DFD = 2.1 x 10^-9 = 210 x 10^-11 on top of the SM, the DFD prediction for a_mu becomes:

- a_mu(DFD) = a_mu(SM) + Delta_a_mu^DFD = 116 592 033 + 210 = 116 592 243 (x 10^-11)
- Discrepancy with experiment: 116 592 243 - 116 592 071 = 172 x 10^-11
- Tension: 172 / 64 ~ 2.7 sigma

**DFD would be in 2.7 sigma tension with the Fermilab final result.** Rather than explaining the anomaly, DFD would create a new one. The DFD prediction overshoots experiment by ~170 x 10^-11.

### 3.2 The experimental value F131 compares against is outdated

F131 uses "Delta_a_mu^exp = (2.49 +/- 0.48) x 10^-9 (BNL + FNAL combined)" -- this is the discrepancy between the 2023 world average and the **2020 data-driven SM prediction**. As of 2025:

- The 2020 data-driven SM value has been superseded by the 2025 lattice-based prediction
- The "anomaly" of 2.49 x 10^-9 no longer exists under the current theoretical consensus
- The actual exp-SM difference is now ~0.4 x 10^-9, consistent with zero

---

## 4. Verdict

### F131 is INCORRECT and OUTDATED. It should be DOWNGRADED from Grade A to Grade D (wrong/obsolete).

**Reasons:**

1. **No verifiable derivation exists.** The 10-page Section 16 of v3.3 is referenced but not present in the codebase. The number 2.1 x 10^-9 cannot be traced to any equation chain.

2. **The stated mechanism fails by 12 orders of magnitude.** The "psi-photon vacuum polarisation" mechanism, evaluated using the gravitational psi field, gives ~10^-21, not ~10^-9. No alternative mechanism producing the correct order of magnitude has been specified.

3. **Strong evidence of reverse-engineering.** The DFD value of 2.1 x 10^-9 closely matches the old anomaly (2.49 +/- 0.48) x 10^-9, suggesting it was fit to the discrepancy rather than derived from first principles.

4. **The muon g-2 anomaly no longer exists.** As of the 2025 Theory Initiative update and the Fermilab final result (June 2025), the SM prediction (lattice QCD-based) agrees with experiment to within 0.6 sigma. There is no anomaly for DFD to explain.

5. **DFD's prediction now CONTRADICTS experiment.** If DFD genuinely contributes 2.1 x 10^-9 to a_mu, it overshoots the observed value by 2.7 sigma when added to the current SM prediction. DFD's g-2 prediction is now a liability, not an asset.

### Recommended Actions

1. **Downgrade F131 to Grade D** and flag as outdated/incorrect in the Master Findings List.
2. **Remove the muon g-2 paper from Tier 1 proposals.** Publishing a claim that DFD explains the muon g-2 anomaly would be immediately refuted by the 2025 experimental and theoretical landscape.
3. **Update v3.3 Section 16** to either:
   - (a) Delete the section entirely, or
   - (b) Reframe it as: "DFD predicts a small but calculable contribution to a_mu from the psi-photon coupling; this contribution must be consistent with the null result (exp - SM ~ 0 +/- 6 x 10^-10), which places an upper bound on the DFD psi-photon coupling strength." This turns the g-2 measurement into a CONSTRAINT on DFD, not a prediction.
4. **Option (b) is the scientifically honest path** and could actually be useful: the g-2 null result constrains DFD parameter space. Frame the paper as "Muon g-2 constraints on density field dynamics" rather than "DFD explains the muon g-2 anomaly."

---

## 5. Sources

- Fermilab final result: [Muon g-2 most precise measurement](https://news.fnal.gov/2025/06/muon-g-2-most-precise-measurement-of-muon-magnetic-anomaly/)
- CERN Courier summary: [Fermilab's final word on muon g-2](https://cerncourier.com/fermilabs-final-word-on-muon-g-2/)
- 2025 Theory Initiative White Paper: [muon-gm2-theory.illinois.edu](https://muon-gm2-theory.illinois.edu/white-paper-25/)
- Theory Initiative prediction: a_mu(SM) = (116 592 033 +/- 62) x 10^-11 (arXiv:2505.21476)
- BMW lattice QCD (2021): First lattice result consistent with experiment
- CMD-3 e+e- -> pi+pi- measurement (2023-2024): Higher cross-section, supporting lattice over older e+e- data
- Fermilab Run 2/3 result (August 2023): a_mu = 0.00116592059(22), 0.20 ppm precision
- F131 source: `DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex`, line 1568
- i71 compilation: `DFD_Research_Output/Cross_Reference_Updates/W5i71_Compiled.tex`
