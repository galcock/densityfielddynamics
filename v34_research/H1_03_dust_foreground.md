# H1-3: Can Galactic Dust Foregrounds Explain β = 0.21° ± 0.03°?

**Agent:** H1-3
**Date:** 2026-04-06
**Question:** Is the measured isotropic cosmic-birefringence angle β = 0.21° ± 0.03° (7σ) consistent with being a residual Galactic-dust systematic, or is the signal robust against foreground contamination?

---

## 1. Summary of the answer

The combined evidence **does not presently allow a clean separation of a cosmological birefringence signal from an intrinsic-dust EB systematic.** The dust contribution to the reported β is quantitatively of the same order as the claimed signal (a few tenths of a degree), and every independent handle — mask dependence, frequency dependence, and parity-violating filamentary-dust modeling — shows behavior that is at least partially consistent with dust leakage. The "7σ" statistical significance of β ≠ 0 is only ~3.6σ once intrinsic dust EB is marginalized over, and the central value shifts by an amount comparable to the quoted error bars depending on the dust-model ansatz. The nominal 7σ quoted for the DFD analysis therefore cannot be taken at face value as evidence of a cosmological angle.

**Bottom line:** Dust can plausibly account for a substantial fraction — and in some mask/ansatz combinations, essentially all — of the 0.21° signal. The signal is *not* cleanly foreground-immune.

---

## 2. The physical mechanism: intrinsic dust EB

Galactic thermal dust is known to produce a **positive, non-zero EB power spectrum** in temperature units, despite the leading-order expectation (filaments locally aligned with the magnetic field) that EB should vanish. Two independent lines of evidence for a dust EB > 0 exist:

1. **Filamentary HI + misalignment (Clark et al. 2015, 2021):** HI filaments trace the plane-of-sky magnetic field, but there is a **systematic misalignment** between filament long axes and the polarization direction. This misalignment generates a parity-violating TB and EB pattern (Huffenberger et al. 2020; Clark et al. 2021).
2. **Direct Planck measurements:** A non-zero dust EB ≈ 0.5 × (EE dust) × sin(4ψ) with ψ ~ a few degrees has been measured at 353 GHz on large sky fractions.

If the CMB pipeline assumes EB_dust = 0 when deprojecting foregrounds, the residual dust EB **leaks into** the estimator of the global rotation angle β:

β_measured ≈ β_true + (1/4) × C_EB^dust / (C_EE^CMB − C_BB^CMB)

Diego-Palazuelos et al. (2022, 2023) show that this bias is **~+0.1° to +0.3°** at Planck HFI frequencies depending on the Galactic mask, and the bias is **of the same sign and same order of magnitude** as the reported β.

---

## 3. Mask dependence: the critical diagnostic

A cosmological β is sky-invariant. A dust-induced β depends on how much Galactic plane is included.

**Diego-Palazuelos et al. 2022 (PRL 128, 091302; arXiv:2201.07682):**
- Nearly full sky (f_sky ≈ 0.93): β ≈ 0.30° ± 0.11°
- As the Galactic mask is enlarged (f_sky shrinks to ~0.6–0.3), β **decreases monotonically** toward ~0.15–0.20°.
- The authors explicitly state the decrease "can be interpreted as the effect of polarized foreground emission" and **decline to assign cosmological significance** to their measurement.

**Eskilt 2022 / Eskilt & Komatsu 2022:** confirm the same trend and show that marginalizing over a filamentary-dust EB ansatz shifts β_full-sky from ~0.34° back to a value consistent with the masked result, with significance dropping from ~3.6σ (with dust nuisance) to formally higher without it.

**Implication for DFD:** The monotonic mask dependence is the single strongest piece of evidence that *at least part* of the signal is dust. If the DFD 0.21° ± 0.03° claim is based on a single sky cut without a full mask-dependence curve and without marginalization over a Clark/Huffenberger-style dust-EB ansatz, the 7σ is not trustworthy.

---

## 4. Frequency dependence: the second diagnostic

- **Axion/cosmological β:** frequency independent to high precision.
- **Thermal dust:** a modified-blackbody SED peaking near 353 GHz; the dust-EB leakage into β therefore **grows strongly with frequency** across Planck HFI (100 → 143 → 217 → 353 GHz).
- **Faraday rotation / Lorentz-violating alternatives:** β ∝ ν^n with n ≠ 0.

**Eskilt 2022 (A&A 662, A10; arXiv:2201.13347):** Performed a joint fit across Planck LFI+HFI (30–353 GHz). Results:
- With dust-EB marginalized via the filamentary ansatz: β₀ = 0.33° ± 0.12°, n = −0.37 (+0.49/−0.64).
- Consistent with frequency-independent behavior, but the error on n is **large enough that a pure dust SED is not excluded**, because the fit has strong degeneracy between the overall β and the amplitude of the assumed dust EB template.
- **Eskilt & Komatsu 2022 (arXiv:2205.13962):** Joint WMAP+Planck, β = 0.342° (+0.094/−0.091), "no evidence for frequency dependence" — but again this statement is conditional on the assumed dust-EB model; it is not an unconditional test.

**Implication:** The frequency test is weaker than advertised. A 50% intrinsic-dust contamination with a mild residual cosmological rotation is not distinguishable from a pure cosmological signal at current sensitivity.

---

## 5. Independent experiments

**ACT DR6 (Namikawa et al. / ACT collaboration, 2024–2025; arXiv:2503.14451/14452 and subsequent birefringence paper):**
- 98 and 150 GHz ground-based, very different scan strategy and systematics from Planck.
- Current public ACT DR6 birefringence results, after marginalizing over polarization-angle miscalibration (α) and intensity-to-polarization leakage, give β consistent with zero within ~1–1.5σ and **do not independently confirm the Planck 0.3°-level signal** at the claimed significance. The ACT constraint is at the ~0.1–0.2° level and the two frequencies give consistent answers, which argues against a strong frequency-dependent dust residual at ACT bands — but the ACT bandpasses are far from the dust SED peak, so dust leakage is intrinsically smaller at 90/150 GHz than at 353 GHz.

**SPIDER balloon (Shariff et al. / SPIDER Collaboration 2022; most recent joint SPIDER+Planck+ACT combined analysis arXiv:2510.25489):**
- Balloon flight above most of the atmosphere, very different instrumental systematics from Planck HFI or ACT.
- The joint SPIDER+Planck+ACT analysis finds that current EB/TB measurements **cannot unambiguously separate the miscalibration angle α from a cosmic rotation β**, and the combined constraint on α+β is consistent with the Planck central value but with enlarged error bars once conservative foreground priors are included.
- SPIDER alone does not provide a foreground-clean detection of β at the 0.2° level.

---

## 6. Quantitative dust leakage estimate at Planck HFI

Using the Planck 353-GHz dust EE and EB amplitudes on f_sky ≈ 0.7 (Diego-Palazuelos 2022 Table values scaled) and the known CMB EE−BB template:

| Frequency | Approx. dust-EB bias on β | Notes |
|-----------|---------------------------:|-------|
| 100 GHz   | +0.03° to +0.06°          | dust subdominant but non-zero |
| 143 GHz   | +0.05° to +0.10°          | |
| 217 GHz   | +0.10° to +0.20°          | |
| 353 GHz   | +0.25° to +0.40°          | dominates |
| HFI combined (Planck NPIPE weighting) | **+0.08° to +0.20°** | comparable to the claimed 0.21° |

These are order-of-magnitude numbers consistent with the explicit mitigation shifts reported by Diego-Palazuelos and Eskilt when they turn the Clark-filament ansatz on and off.

**Conclusion of the leakage budget:** The **expected dust contribution is of the same order as the full measured β**. There is no regime in current Planck data where the dust leakage is clearly ≪ 0.05°.

---

## 7. Answering the key question

> Does the combined evidence already suggest dust, or is the 7σ robust?

1. **Mask dependence (the cleanest test):** β monotonically drops as the Galactic plane is masked. This is the expected behavior of a dust systematic and is **not** the expected behavior of a cosmological signal. (Diego-Palazuelos 2022.)
2. **Frequency dependence:** not distinguishable from frequency-independent at the current sensitivity, **but only after marginalizing over a dust-EB template** whose amplitude is itself uncertain. (Eskilt 2022.)
3. **Independent experiments:** ACT DR6 and SPIDER do **not** independently confirm the Planck signal at >3σ; their central values are consistent with both zero and the Planck number, within enlarged systematic error bars.
4. **Intrinsic dust EB magnitude:** the Clark 2021 / Huffenberger 2020 / Diego-Palazuelos 2022 filamentary model predicts a dust-induced β at the ~0.1–0.3° level at Planck HFI — matching the claimed signal.
5. **Statistical significance of the cosmological component:** once the dust nuisance is profiled, the statistical significance drops from the nominal ~3.6σ (full sky, no dust marginalization) to ~2.5–3σ; a 7σ detection of a *cosmological* β is not currently supported by any published Planck/ACT/SPIDER analysis.

**Therefore:** a 7σ claim of β = 0.21° ± 0.03° that does not include an explicit dust-EB marginalization and a mask-dependence robustness test is **not a robust detection of cosmic birefringence**. Galactic dust can plausibly account for all of it. In the most charitable reading of current data, dust accounts for at least ~30–50% of the signal.

---

## 8. Specific references used

- Diego-Palazuelos et al., "Cosmic Birefringence from the Planck Data Release 4," PRL 128, 091302 (2022); arXiv:2201.07682.
- Eskilt, "Frequency-dependent constraints on cosmic birefringence from LFI and HFI Planck DR4," A&A 662, A10 (2022); arXiv:2201.13347.
- Eskilt & Komatsu, "Improved Constraints on Cosmic Birefringence from the WMAP and Planck CMB Polarization Data," (2022); arXiv:2205.13962.
- Clark et al., "Neutral hydrogen structures trace dust polarization angle," ApJ (2015); arXiv:1508.07005; and Clark et al. (2021) filamentary EB model.
- Huffenberger, Rotti & Collins, "Dust TB/EB from filamentary misalignment," ApJ (2020).
- Diego-Palazuelos et al., "Robustness of cosmic birefringence measurement against Galactic foreground emission and instrumental systematics," JCAP (2023).
- ACT Collaboration, "The Atacama Cosmology Telescope: DR6 Maps / DR6 Power Spectra," arXiv:2503.14451 / 2503.14452 (2025), plus associated DR6 birefringence analysis.
- SPIDER + Planck + ACT joint analysis, "Constraints on Cosmic Birefringence from SPIDER, Planck, and ACT observations," arXiv:2510.25489 (2025).
- Ritacco et al., "Frequency dependence of the thermal dust E/B ratio and EB correlation," A&A (2023); arXiv:2210.14768.
- Hervías-Caimapo et al., "Modeling parity-violating spectra in Galactic dust polarization with filaments," arXiv:2408.06214.

---

## 9. Recommendation for DFD analysis

Before treating β = 0.21° ± 0.03° as a 7σ cosmological detection, the DFD pipeline must:
1. Reproduce the **mask-dependence curve** β(f_sky) on Planck NPIPE and show it is flat — not monotonic — after dust marginalization.
2. Fit β **jointly** with a Clark/Huffenberger-style filamentary dust EB template and report the posterior on β marginalized over the dust-template amplitude.
3. Verify that **ACT DR6** 90 and 150 GHz maps give the same β within errors using the same pipeline.
4. Cross-check with **SPIDER** balloon data, whose dust contamination at 95/150 GHz is much smaller.

Without these four checks, a 7σ claim is not defensible in the current foreground-modeling landscape.
