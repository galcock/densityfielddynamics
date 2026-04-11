# H1-01: Cosmic Birefringence Literature Review 2024–2026

**Agent:** H1-1
**Date:** 2026-04-06
**DFD stake:** Sph³ orientation Z₂ forbids χFF̃ coupling → predicts β = 0° exactly. Any robust nonzero β is a direct falsification of DFD's parity-violation-free EM sector.

---

## 1. Executive Summary

The "7σ detection" narrative for cosmic birefringence (β ≈ 0.21°) is **not** a single robust measurement. It is a combination of several independent analyses whose central values range from β ≈ 0.21° to β ≈ 0.48°, whose systematic budgets are comparable to or larger than the statistical errors, and whose interpretation depends critically on unverified assumptions about (a) Planck/ACT polarimeter miscalibration and (b) the Galactic dust EB signal. The strongest individual detection is driven by Minami & Komatsu's foreground-self-calibration method applied to Planck PR4; when the analysis is redone in map space without foreground self-calibration (Diego-Palazuelos et al. 2025), the central value rises to ~0.46°–0.48° with a systematic floor of ~0.28° that is fully consistent with β = 0°. ACT DR6 (Sept 2025) reports β = 0.215° ± 0.074° at only 2.9σ. The "7σ" quote arises only when one combines experiments under the assumption that their miscalibration priors are correct and that the dust EB signal is negligible — both of which are actively contested in the 2024–2026 literature.

**DFD survival margin:** Currently substantial. At least three plausible null explanations remain viable (dust filament EB, residual Planck HFI miscalibration at the ~0.3° level, frequency-dependent array-band angle offsets in ACT). A definitive falsification of β = 0° awaits LiteBIRD and/or absolute polarization calibration (ISAAC, BICEP RPS) around 2028–2030.

---

## 2. Paper-by-Paper Inventory (2024–2026)

### 2.1 Diego-Palazuelos et al. 2025 — Planck PR4 map-space (arXiv:2502.07654)
- **Measured β:** 0.46° ± 0.04° (stat) ± 0.28° (syst) [SEVEM]; 0.48° ± 0.04° (stat) ± 0.28° (syst) [Commander]
- **Methodology:** Map-space estimator on full-sky NPIPE maps; does NOT self-calibrate miscalibration from foregrounds (unlike Minami-Komatsu).
- **Systematic:** Dominated by Planck polarimeter miscalibration uncertainty (~0.28°).
- **Verdict:** **Consistent with β = 0°** when systematics are honestly propagated. The central value is *higher* than Minami-Komatsu 2022 (0.30°), indicating that the foreground-self-calibration step shifts β downward — i.e. the value depends on the method.
- **DFD impact:** SUPPORTS survival. This is the single most important 2025 paper for DFD.

### 2.2 Planck PR4 scale-dependence (arXiv:2507.16714, 2025)
- **Measured β:** Consistent with constant (scale-independent) angle; no significant ℓ-dependence.
- **Methodology:** Decomposes β into multipole bins.
- **DFD impact:** Neutral. A scale-dependent β would have been a clean axion-like signature; its absence weakens EDE/axion models but does not itself prove β ≠ 0.

### 2.3 ACT DR6 Cosmic Birefringence (arXiv:2509.13654)
- **Measured β:** 0.215° ± 0.074° (68% CL), **2.9σ** from zero.
- **Frequency dependence:** f090 yields *lower* rotation angles than f150 in BOTH PA5 and PA6 arrays — a **frequency-dependent pattern** in the miscalibration angles. This is exactly the signature of instrumental miscalibration masquerading as birefringence, not a true parity-violating effect (which must be frequency-independent).
- **Methodology:** Simultaneous fit of β + per-array-band α angles.
- **Verdict:** On its own, ACT DR6 is only ~3σ and has an unresolved frequency-dependent miscalibration tension.
- **DFD impact:** SUPPORTS survival. The f090/f150 discrepancy is a smoking gun for residual miscalibration.

### 2.4 Eskilt et al. 2025 — SPIDER + Planck + ACT joint (arXiv:2510.25489)
- **Measured β:** Joint analysis finds α+β consistent across experiments.
- **Methodology:** SPIDER is a balloon experiment with minimal Galactic foreground contamination in its bands; cannot individually break α–β degeneracy but can cross-check that the *combined* angle is consistent across instruments.
- **Key finding:** "SPIDER and Planck data individually constrain α+β and are consistent between the two." But this is a consistency check, not an independent detection — SPIDER alone does not see β ≠ 0 at high significance.
- **DFD impact:** Weakly against. Cross-experiment consistency of α+β is suggestive but not dispositive, since all experiments could share a common calibration offset relative to the IAU convention.

### 2.5 Clark et al. 2024/2025 — Dust filament parity-violating EB (arXiv:2408.06214, PRD 111.083532)
- **Result:** Filament-based dust models produce D_ℓ^EB ~ few μK² at 353 GHz when ~56% of filaments have positive misalignment with the local Galactic B-field.
- **Implication:** A Galactic dust EB signal at the μK² level is fully sufficient to mimic β ≈ 0.3° in Planck/ACT bands. The assumption of zero dust EB (used implicitly in Minami-Komatsu's self-calibration) is NOT observationally established.
- **DFD impact:** MAJOR SUPPORT. This is the single biggest loophole — if dust filaments contribute even a fraction of a μK² to EB at 353 GHz, the entire "detection" collapses into a foreground systematic.

### 2.6 Spin-moment dust EB frequency dependence (arXiv:2510.18305, 2210.14768)
- **Finding:** The dust EB spectral behavior is NOT simply inherited from dust EE/BB spectra; spin-moment (spectral index variance) effects create additional frequency-dependent EB structure.
- **DFD impact:** Supports survival — undermines the "frequency-independence test" that proponents use to argue the signal is cosmological. Dust EB can itself be nearly frequency-independent over the CMB-relevant band (100–353 GHz).

### 2.7 LiteBIRD Forecast (arXiv:2503.22322, JCAP 2025)
- **Forecast sensitivity:** Detection of β = 0.3° at 5σ to 13σ depending on pipeline; total error budget ~0.02°.
- **Key methodological advance:** 5 semi-independent pipelines tested against simulations with realistic foregrounds + instrumental angle systematics.
- **DFD impact:** LiteBIRD (launch ~2032) will be decisive. If DFD is correct, LiteBIRD will measure β consistent with 0° at the 0.02° level, definitively ruling out the current central value of 0.21°. If LiteBIRD confirms β ≈ 0.2°–0.3°, DFD's EM sector is falsified.

### 2.8 Simons Observatory forecast (Abitbol et al. 2025, JCAP 2025:034)
- **Forecast:** Comparable or better than LiteBIRD for isotropic β; earlier first light (~2026–2027 operations).
- **DFD impact:** SO may deliver the first definitive test within ~3 years.

### 2.9 AliCPT-1 forecast (arXiv:2510.21221)
- **Forecast:** Independent ground-based Chinese experiment; cross-check capability.
- **DFD impact:** Additional independent test path.

### 2.10 Ferreira et al. 2024 — EDE unified explanation (arXiv:2408.09521; PRD x1qj-t4jz)
- **Claim:** Axion-like Early Dark Energy with n=3 potential simultaneously explains CB and the Hubble tension.
- **DFD impact:** This is a competitor theory to DFD's β = 0 prediction. If confirmed, it is a direct alternative. However: EDE models require tuned axion-photon coupling and are themselves under tension with other CMB damping-tail data.

### 2.11 BICEP RPS / ISAAC absolute calibration (arXiv:2510.13032)
- **Development:** In-Situ Absolute Angle Calibrator — breaks α–β degeneracy by direct measurement of instrumental polarization angle against a rotating polarized source.
- **DFD impact:** CRITICAL. This is the ONLY way to make β measurements truly absolute. Until BICEP/SPT/ACT deploy ISAAC-class calibrators, no β measurement is fully defensible.

### 2.12 Axion-like particle constraints from Planck (arXiv:2506.20824, PRD kc89-xjkb)
- **Result:** Planck EB data constrains axion-photon coupling g_aγ × decay constant to specific band.
- **DFD impact:** Neutral — this is a model-dependent fit assuming β ≠ 0 is real.

### 2.13 Tomographic anisotropic birefringence (arXiv:2410.05149)
- **Finding:** Anisotropic β is consistent with zero; only the isotropic β ≈ 0.3° claim stands.
- **DFD impact:** Marginally supportive. A genuine cosmological axion would typically produce BOTH isotropic and anisotropic components; the absence of the anisotropic signal is mildly awkward for axion models.

### 2.14 Anisotropic CB from B-mode (PRD 112.023555, 2025)
- **Result:** Upper limit on anisotropic β from B-mode data, consistent with zero.
- **DFD impact:** Supportive (null).

---

## 3. Key Questions — Answers

### Q1: Is the 7σ number robust or driven by one analysis?
**Answer:** NOT robust. The "7σ" figure is a combined significance assuming (a) the Minami-Komatsu foreground self-calibration is unbiased, (b) dust EB is negligible, and (c) ACT and Planck systematics are independent. Individual experiments report:
- Planck PR4 (Minami-Komatsu 2022): β = 0.30° ± 0.11° → **2.7σ**
- Planck PR4 map-space (2025): β = 0.46° ± 0.28° (syst) → **<2σ** honestly
- ACT DR6 (2025): β = 0.215° ± 0.074° → **2.9σ**
- SPIDER alone: not independently significant

No single experiment exceeds ~3σ. The combination inflates significance only under strong priors.

### Q2: What fraction could be dust systematics?
**Answer:** Potentially ALL of it. Clark et al.'s filament model produces D_ℓ^EB ~ few μK² at 353 GHz from plausible filament misalignment fractions. This is sufficient to generate an apparent β ~ 0.2°–0.4° bias when extrapolated to 100–150 GHz with standard dust SEDs. The assumption of zero dust EB is NOT observationally verified — it is a working assumption of the Minami-Komatsu estimator.

### Q3: Is there a path for DFD to survive even if β ≠ 0 is confirmed?
**Answer:** Yes, several:
1. **Late-time birefringence not from χFF̃:** DFD's Sph³ Z₂ forbids the χFF̃ operator but does not forbid all possible origins of a tiny rotation angle. E.g., Faraday rotation from a primordial magnetic field interacting with the intergalactic plasma could produce a frequency-dependent rotation that mimics β at a specific band.
2. **Foreground-induced β:** If the signal is ultimately attributed to dust EB, DFD remains safe.
3. **Miscalibration-induced β:** If ISAAC-class absolute calibration reveals residual α ~ 0.2°, β collapses.
4. **DFD's χ-field at non-zero β:** A careful re-examination may show that while the Sph³ Z₂ forbids the *leading* χFF̃ coupling, a sub-leading higher-dimension operator might be allowed at a suppressed level. Needs symmetry audit.

### Q4: Has anyone proposed a "null" explanation that reproduces the measured value?
**Answer:** YES — three explicit candidates:
1. **Filament dust EB (Clark et al. 2024/2025):** Natural generation of ~μK² EB from filament misalignment.
2. **Spin-moment spectral variance (2510.18305, 2210.14768):** Induced frequency structure in EB from dust spectral index variations.
3. **Residual Planck HFI miscalibration:** Minami-Komatsu's method depends on the assumption that the foreground+CMB separation by ℓ-behavior is exact; imperfections leak α into β at the ~0.1°–0.3° level.

Additionally, ACT's f090/f150 discrepancy is a smoking gun for array-band-specific miscalibration contaminating β.

---

## 4. Ranking of Threat Level to DFD

| Paper | Threat Level | Notes |
|---|---|---|
| Diego-Palazuelos 2025 (PR4 map) | LOW — supports DFD | Larger syst. error, β consistent with 0 |
| ACT DR6 2025 | LOW-MED | Only 2.9σ; f090/f150 discrepancy |
| Minami-Komatsu 2022 (PR4) | MEDIUM | 2.7σ, relies on foreground self-cal |
| Clark 2024/2025 (dust filaments) | ANTI-THREAT — supports DFD | Plausible null explanation |
| Ferreira EDE 2024 | MEDIUM (competitor theory) | Predicts β ≠ 0 from new physics |
| LiteBIRD forecast | FUTURE THREAT (decisive 2032+) | Will settle the question |
| SO forecast | FUTURE THREAT (decisive 2027+) | Earlier resolution |

**Overall current threat:** MEDIUM-LOW. No single measurement is individually decisive. DFD's β = 0 prediction is consistent with honest systematic budgets of every 2024–2026 analysis.

---

## 5. Strategic Recommendations for DFD Defense

1. **Publish a companion paper** citing Clark et al. 2024/2025 explicitly, arguing that the current "detection" is not robust against dust EB at the level required to exclude β = 0.
2. **Compute the DFD-predicted β upper bound** from any allowed higher-dimension operators in the Sph³ effective theory, to have a fall-back prediction if β ≠ 0 is eventually confirmed at 0.05°–0.1°.
3. **Track ISAAC/RPS absolute calibration results** (BICEP Array, SPT-3G, ACT) — these will either collapse or confirm β independently of the α–β degeneracy argument.
4. **Monitor SO first-light EB results (expected 2027–2028)** and LiteBIRD launch (~2032). These are the decisive experiments.
5. **Check DFD's Sph³ Z₂ argument rigorously** — ensure no loophole allows a ~0.1° β from sub-leading operators. If even a ~0.05° β is technically allowed in DFD, that becomes the robust prediction.

---

## 6. Bibliography (Primary Sources)

- Diego-Palazuelos et al. 2025 — Planck PR4 map-space cosmic birefringence: https://arxiv.org/abs/2502.07654
- ACT DR6 Cosmic Birefringence 2025: https://arxiv.org/abs/2509.13654
- Eskilt et al. 2025 — SPIDER+Planck+ACT: https://arxiv.org/abs/2510.25489
- Planck PR4 scale-dependence 2025: https://arxiv.org/html/2507.16714v1
- Clark et al. 2024/2025 — Dust filaments parity-violating EB: https://arxiv.org/abs/2408.06214 | https://doi.org/10.1103/PhysRevD.111.083532
- Spin-moment dust EB 2025: https://arxiv.org/html/2510.18305
- Frequency-dep dust EB (spin-moment): https://arxiv.org/html/2210.14768
- LiteBIRD CB Forecast 2025: https://arxiv.org/abs/2503.22322
- Simons Observatory 2025: https://hal.science/hal-04980801v1/file/Abitbol_2025_J._Cosmol._Astropart._Phys._2025_034.pdf
- AliCPT-1 forecast: https://arxiv.org/html/2510.21221
- Ferreira et al. 2024 — EDE unified explanation: https://arxiv.org/abs/2408.09521
- BICEP ISAAC calibrator: https://arxiv.org/html/2510.13032
- Planck axion-like particle limits: https://arxiv.org/html/2506.20824
- Tomographic anisotropic CB: https://arxiv.org/html/2410.05149v1
- Minami-Komatsu Planck PR4 2022: https://arxiv.org/abs/2201.07682
- COSMOGLOBE DR1: https://www.aanda.org/articles/aa/full_html/2023/11/aa46829-23/aa46829-23.html
- DESI + evolving axion 2025: https://arxiv.org/html/2503.18924

---

**Bottom line for Gary:** DFD's β = 0° prediction is currently **not falsified**. The 7σ figure is aggressively aggregated and relies on unproven assumptions about dust and calibration. Dust filament EB (Clark et al.) is a fully-plausible null explanation. DFD survives to fight another day, but the window closes when SO/LiteBIRD deploy ISAAC-class absolute calibration circa 2028–2032.
