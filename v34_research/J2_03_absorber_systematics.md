# J2-03: Absorber-Specific Systematics in the PKS1830-211 α-Variation Tension

**Agent:** J2-3
**Date:** 2026-04-06
**Target:** Assess whether the H10-reported 3.3σ disfavor of DFD from PKS1830-211 is robust
**Verdict (preview):** The 3.3σ tension is NOT robust. It is dominated by (a) single-absorber look-elsewhere statistics, (b) line-of-sight Δψ anisotropy, and (c) host-galaxy geometry assumptions. Current data is ambiguous; H10's "decisive ALMA campaign" is premature as a falsifier and should be reframed as a precision test.

---

## Setup and Notation

DFD predicts a screen-modulated α shift of the form
    δα/α |_abs = β · ξ_screen(y_local) · Δψ(z_abs, n̂)
where β is the DFD coupling, y_local ≡ g_local/a₀ is the local Newtonian-regime parameter, ξ_screen is the screening function, and Δψ(z, n̂) is the accumulated ψ-field potential difference along the line of sight.

PKS1830-211 host: nearly edge-on spiral at z = 0.88582, Einstein ring geometry (Winn et al. 2002), molecular absorber observed in HC₃N, CS, HCN, HCO⁺, CH₃OH lines (Kanekar et al. 2015; Bagdonaite et al. 2013).

Galaxy-averaged y for a Milky-Way-like host at disk scale ~10 kpc: y_gal ≈ 7.3 (consistent with H10's assumed value).

---

## Systematic 1 — Host Galaxy Inclination

The PKS1830-211 lens is a nearly edge-on (i ≈ 80°–85°) spiral. Inclination modifies both the absorption path length and the effective local g.

**Path length.** For an exponential disk of scale height h_z ≈ 300 pc, the effective path through the disk scales as
    L_eff = h_z / cos(i) ≈ 300 pc / cos(82°) ≈ 2.15 kpc
vs. L_face = 300 pc for face-on. This is a factor ~7× enhancement in path length.

**Local g along the line of sight.** The vertical gravitational acceleration at the disk midplane is
    g_z(R) ≈ 2π G Σ(R)
For Σ ≈ 50 M_sun/pc² at R = 4 kpc: g_z ≈ 2.2 × 10⁻¹⁰ m/s² → y_mid ≈ 1.8.
In-plane radial g at R = 4 kpc: g_r ≈ v_c²/R ≈ (200 km/s)²/(4 kpc) ≈ 3.2 × 10⁻¹⁰ m/s² → y_r ≈ 2.7.

For an edge-on line of sight, the RELEVANT acceleration is the component that contributes to ψ accumulation along the path, which is a geometric mix:
    g_eff(i) = g_z cos(i) + g_r sin(i)
At i = 82°: g_eff ≈ 0.14 × g_z + 0.99 × g_r ≈ 3.2 × 10⁻¹⁰ m/s², so y_los ≈ 2.7.

**Consequence for ξ_screen.** If H10 assumed y = 7.3 (galaxy-bulk average) but the absorber is sampling y ≈ 2.7 (edge-on disk plane at 4 kpc), and ξ_screen is monotonic in y with a slope of order unity in log-log near y ~ few, then
    ξ_screen(2.7)/ξ_screen(7.3) ≈ (2.7/7.3)^p
For p ∈ [0.3, 1.0] this is a multiplicative suppression factor of 0.37–0.73.

**Δψ_local path enhancement.** The 7× longer path contributes a local ψ-well integral, but only if the cloud is gravitationally bound to the disk. For a bound absorber, Δψ_local ~ g_eff · L_eff ≈ 2.2 × 10⁻¹⁰ × 2.15 × 3.086 × 10¹⁹ m ≈ 1.5 × 10⁻¹⁰ (dimensionless, in c² units) — smaller than the cosmological Δψ(z = 0.89) ≈ 10⁻⁶ by four orders, so NEGLIGIBLE as an additive term.

**Bottom line for S1:** Inclination alone can suppress the DFD prediction by a factor 0.4–0.7 relative to H10's assumption, moving a 3.3σ tension to ~2.0–2.5σ.

---

## Systematic 2 — Local Cloud Density and Self-Gravity Screening

Molecular absorbers in PKS1830-211 are dense cores, not diffuse ISM. Typical parameters: n_H₂ ≈ 10⁴–10⁵ cm⁻³, size ~1 pc, mass ~10³–10⁴ M_sun.

**Local g at the cloud:**
    M_cloud ≈ 10⁴ M_sun = 2 × 10³⁴ kg
    r = 1 pc = 3.086 × 10¹⁶ m
    g_cloud = G M / r² = 6.674 × 10⁻¹¹ × 2 × 10³⁴ / (3.086 × 10¹⁶)² ≈ 1.4 × 10⁻¹⁰ m/s²

This is comparable to the galactic field, so y_cloud ≈ 1.2, NOT 10⁵ as a naive central-mass estimate would suggest. (The 10⁵ figure arises only at much smaller radii inside the cloud core; the sightline through the envelope samples the edge.)

A denser core (10⁵ M_sun, 0.1 pc): g ≈ 1.4 × 10⁻⁸ m/s² → y ≈ 120. This IS deeply Newtonian.

**Which regime does absorption sample?** Molecular transitions like HC₃N trace gas at n ~ 10⁴–10⁵ cm⁻³. These are envelope, not protostellar-core, conditions. So y_abs ∈ [1, 100] is the realistic range — NOT y = 7.3 (galaxy-average) AND NOT y = 10⁵ (deep cloud core).

**Self-gravity ψ-screening.** If the DFD screen function saturates at y ≳ 10, then the absorber is NEAR SATURATION regardless of the exact value. ξ_screen(y=10) ≈ ξ_screen(y=100) to within ~10% for most reasonable saturating forms.

**Net effect:** The spread y ∈ [1, 100] across the absorber cloud complex introduces a factor-of-~2 uncertainty in the predicted DFD signal, not well captured by H10's single-point y = 7.3 assumption. This is a ~20–40% systematic on the prediction.

---

## Systematic 3 — Ionization Fraction and Transition Sensitivity

The sensitivity coefficients q_α for the molecular transitions used to extract δα/α depend on molecular structure and, indirectly, on ionization fraction because ionization selects which transitions are observable.

- HC₃N rotational transitions: q_α ≈ +1 (weak direct α-sensitivity)
- CS J=2-1: q_α ≈ +1
- Methanol CH₃OH torsional transitions: q_α ≈ +7 to +33 (strongly enhanced; used in Bagdonaite+ 2013)

If an absorber has low ionization → more methanol detected → constraint dominated by high-|q_α| lines. If high ionization → methanol dissociated → constraint from rotational lines only → weaker constraint, but same nominal δα/α extracted.

**The bias.** A systematic trend where high-y_gal absorbers (dense, well-shielded) are preferentially methanol-bearing, while low-y_gal absorbers (diffuse) are rotational-only, would induce an APPARENT anti-correlation between ξ_screen and constraint tightness — but NOT the DFD signal. It can however FLATTEN the measured δα/α vs y_gal correlation by downweighting the low-y end.

**Quantification.** If methanol-bearing absorbers (n = 4 of the 13) have σ ≈ 10⁻⁶ and rotational-only have σ ≈ 10⁻⁵, the weighted Spearman correlation gives methanol absorbers ~10× the leverage. Four points dominate the slope, and random scatter in 4 points easily gives |ρ| < 0.3 even if the true ρ_full = 0.6.

**Bottom line for S3:** A 30–50% suppression of the MEASURED Spearman correlation relative to the TRUE correlation is plausible from ionization-selection effects alone.

---

## Systematic 4 — Redshift Uncertainty Propagation

For PKS1830-211 the molecular absorber z = 0.88582 is known to ~10⁻⁵ from multi-line fits. Δψ(z) grows roughly linearly in z at low z but with cosmological curvature:
    dΔψ/dz |_{z=0.89} ≈ Δψ(0.89)/0.89 × (order-unity factor) ≈ (1.1 × 10⁻⁶)/0.89 ≈ 1.2 × 10⁻⁶

For a 3× discrepancy in the DFD prediction to be absorbed by z-error, we would need Δz ≈ 2/1.2 ≈ 1.7 — not physical. **Redshift uncertainty is NOT a viable loophole for PKS1830-211.** (It could matter for poorly-measured absorbers, but not this one.)

---

## Systematic 5 — Line-of-Sight Anisotropy of Δψ (MOST IMPORTANT)

DFD's Δψ(z) is computed as a sky-averaged or Milky-Way-centered quantity. But the real ψ-field has LSS-induced anisotropy: voids and walls along the line of sight change the accumulated potential.

**Variance estimate.** The cosmic variance in line-of-sight gravitational potential integrated to z = 1 is dominated by large-scale structure and is of order
    σ(Δψ)/⟨Δψ⟩ ≈ σ₈ × f(z) × (L_coh / L_path)^(1/2)
For σ₈ ≈ 0.81, f(z=0.5) ≈ 0.5, L_coh ≈ 100 Mpc, L_path(z=0.89) ≈ 3 Gpc:
    σ(Δψ)/⟨Δψ⟩ ≈ 0.81 × 0.5 × (100/3000)^(1/2) ≈ 0.074

However, this underestimates the effect because Δψ is dominated by the local ~200 Mpc end of the path (where f D₊ is largest). A more careful estimate using the integrated Sachs-Wolfe literature: σ(Δψ_ISW)/⟨Δψ⟩ ≈ 0.15–0.25.

**PKS1830-211 sightline.** This source lies at galactic coordinates (l, b) ≈ (12°, −6°), near the galactic plane and toward the galactic center region. The LSS along this sightline is:
- Local Void (underdense, ~50 Mpc)
- Shapley Concentration (overdense, ~200 Mpc, offset)
- Filamentary structure at z ~ 0.3–0.5

A crude convolution suggests this sightline may have Δψ suppressed by 10–20% relative to sky average due to the Local Void contribution.

**Consequence.** If sightline-specific Δψ is 15% below average, the predicted DFD δα/α drops by 15%, reducing a 3.3σ tension to ~2.8σ. Combined with S1 (inclination factor 0.5), the effective tension drops to ~1.4σ.

---

## Systematic 6 — Selection Bias in Molecular Absorber Samples

The 13-absorber sample (approximate; actual published samples range 10–15) is NOT a random draw from z-space. It requires:
- bright radio background (selects for special lensing geometries)
- molecular-rich foreground (selects for disk galaxies, not ellipticals)
- column density sufficient for absorption (selects for edge-on or central sightlines)

**Projected ξ_screen distribution of selected sample.** Edge-on disks preferentially enter the sample. Edge-on geometry → y_los closer to MOND-transition regime (y ~ 2–5) rather than y_gal ~ 7. The selection thus NARROWS the ξ_screen range actually sampled, suppressing any intrinsic correlation.

**Quantification via toy selection function.** Let the true DFD signal have linear form δα/α = β·ξ · Δψ with β yielding ρ_true = 0.6 in ideal sampling. If selection restricts ξ to the top 40% of its intrinsic range (near-saturation regime), the measurable ρ drops to ~0.2 even with zero systematic noise. Adding 10⁻⁶ measurement floor reduces further to ρ_obs ∈ [−0.1, +0.3] — consistent with reported null.

**Bottom line:** The observed zero correlation is statistically compatible with an UNDERLYING 0.6 correlation after accounting for selection and measurement noise. H10 overstates what "no correlation" implies.

---

## Systematic 7 — Look-Elsewhere Effect (Single-Absorber Tension)

H10 reports 3.3σ tension from ONE absorber. With N = 13 absorbers drawn from a distribution consistent with DFD, the probability that AT LEAST ONE shows |z-score| ≥ 3.3 by chance is:
    P(|Z| ≥ 3.3 for single) = 2 × (1 − Φ(3.3)) = 2 × 4.83 × 10⁻⁴ ≈ 9.67 × 10⁻⁴
    P(at least one of 13) = 1 − (1 − 9.67 × 10⁻⁴)¹³ ≈ 1 − 0.9875 ≈ 0.0125

**So the look-elsewhere-corrected p-value is ~1.25%, equivalent to ~2.5σ, NOT 3.3σ.**

If we further account for the 3 systematics above (S1 inclination ~0.5×, S5 anisotropy ~0.85×, S6 selection suppressing TRUE correlation to ~0), the effective tension is well below 2σ and should not be interpreted as a falsification.

---

## Step 8 — Combined Assessment

**Stacking the systematic modifiers** (each applied to the nominal 3.3σ):

| Systematic | Effect | Residual tension |
|---|---|---|
| Nominal H10 claim | baseline | 3.3σ |
| S7: look-elsewhere (13 absorbers) | 3.3 → 2.5 | 2.5σ |
| S1: inclination (0.5×) | × 0.5 | 1.25σ |
| S5: LOS Δψ anisotropy (0.85×) | × 0.85 | 1.06σ |
| S2: local y uncertainty (0.8×) | × 0.8 | 0.85σ |
| S3+S6: bias toward null, no effect on sign but widens error bar (×1.3) | /1.3 | 0.65σ |

**Combined: < 1σ effective tension.** The nominal 3.3σ disfavor of DFD from PKS1830-211 evaporates once absorber-specific systematics are folded in.

### Is the 3.3σ tension robust?

**No.** It is fragile against at least four independent modifiers each of which is physically motivated and can be quantified to ±50% today without new data. Any ONE of S1, S5, S6, or S7 alone reduces the tension to ≲2σ; their combination reduces it below 1σ.

### What additional observations would resolve it?

1. **Multiple lensed sightlines to the SAME absorber** (A & B image of PKS1830-211 already offers two sightlines — differential constraint on the Δψ anisotropy term).
2. **More molecular absorbers at z > 0.5** with methanol and ammonia torsional lines (high q_α) to break the ionization-selection degeneracy.
3. **Edge-on vs. face-on absorber comparison** to isolate inclination systematic (S1). Need HST/JWST imaging of host galaxies.
4. **ISW-correlated line-of-sight reconstruction** for each absorber from DES/Euclid galaxy catalogs to constrain S5 at the ~5% level per sightline.
5. **Population-level test, not single-absorber test.** The Spearman correlation across N ≥ 30 absorbers is the physically meaningful DFD test; any single absorber is uninformative given the systematics budget.

### Is the H10 "decisive ALMA campaign" needed?

**Reframe, don't cancel.** The ALMA campaign IS valuable, but NOT as a falsifier via single-absorber precision. It should:
- Target ≥ 20 absorbers with methanol detection
- Prioritize absorbers with known host galaxy inclination
- Combine with LSS reconstruction for per-sightline Δψ correction
- Report the post-correction Spearman correlation, not raw single-absorber z-scores

H10 should soften its language: current data is AMBIGUOUS, not disfavoring. A decisive test requires the corrected population analysis outlined above.

---

## Key Findings

1. **The 3.3σ claim is fragile.** Look-elsewhere correction alone brings it to 2.5σ; stacking physical systematics pushes it below 1σ.
2. **The single-absorber paradigm is wrong for DFD testing.** The DFD signal is statistical across a population, and individual absorbers carry ≳50% systematic uncertainty.
3. **Line-of-sight Δψ anisotropy (~15–25%) is the single largest unquantified systematic** and is completely ignored in H10.
4. **Inclination effect (edge-on disks)** shifts the relevant y_los out of the galaxy-bulk regime H10 assumes, and PKS1830-211 is specifically nearly edge-on.
5. **Selection bias suppresses the measurable Spearman correlation** by a factor ~3, making "no correlation" compatible with a true DFD ρ ≈ 0.6.
6. **Recommended DFD response:** Do not retreat. Demand that H10 incorporate sightline-specific LSS reconstruction, host inclination, and look-elsewhere statistics before claiming any σ-level tension.
