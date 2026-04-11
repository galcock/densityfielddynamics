# L2: Analytical Audit of the "5.4× Structure-Growth Overshoot"

**Agent:** L2
**Date:** 2026-04-06
**Source:** `Density_Field_Dynamics__A_Complete_Unified_Theory__v3_3/section_cosmology.tex`, lines 688-705
**Question:** Is the 5.4× a first-principles analytical result, and does 5.4 = 16/3 exactly?

---

## 1. What v3.3 actually claims

Verbatim setup from section_cosmology.tex lines 688-705 (the "Proof-of-concept: N-body structure formation" paragraph):

- **Method:** particle-mesh simulation
- **Grid:** 64³
- **Box:** 200 Mpc/h
- **Runs compared on *identical* ICs:**
  - ΛCDM with Ω_m = 0.30
  - Newtonian-baryons with Ω_b = 0.049
  - DFD-baryons with Ω_b = 0.049 and μ(x) = x/(1+x)
- **Reported outputs:**
  - δ_rms (Newton-baryons) = 1.5×10⁻⁴
  - δ_rms (DFD-baryons)   = 6.4×10⁻³  →  43.8× over Newton-baryons
  - δ_rms (ΛCDM) implied  ≈ 6.4×10⁻³ / 5.4 ≈ 1.19×10⁻³
- **EFE treatment:** None in this run. The text explicitly says "without the cosmological External Field Effect (EFE) from the Hubble flow (a_ext ~ cH₀ ≈ 6 a₀)."
- **Analytic commentary given in v3.3:**
  - "x ≈ 4×10⁻⁴ ... deep in the MOND regime where the raw μ-function enhances gravity by ~400×"
  - "With the EFE, the effective enhancement drops from ~400 to ~1.2"
- **Status statement in v3.3:** "This is a proof-of-concept at 64³ resolution; production-quality results require ≥256³ with the EFE implemented."

So v3.3 itself presents 5.4 as a **numerical simulation output**, not a theorem.

---

## 2. First-principles linearized growth with μ(x)=x/(1+x)

The DFD linear growth operator from Eqs. (eq:growth-Geff)-(eq:G-eff) of the same section is

    δ̈_k + 2H δ̇_k = 4π G_eff(a, k̂) ρ̄ δ_k,

    G_eff/G = 1 / [ μ₀ · ( 1 + L₀ (k̂·ĝ)² ) ],

with, for μ(x)=x/(1+x):

    μ₀ = x̄/(1+x̄),     L₀ = 1/(1+x̄)².

At x̄ = 4×10⁻⁴ (the text's cosmological operating point):

    μ₀ ≈ 4.00×10⁻⁴,
    L₀ ≈ 1 − 2x̄ ≈ 0.9992,
    1/μ₀ ≈ 2500  (the "raw" enhancement before direction averaging)
    direction-averaged ⟨1+L₀(k̂·ĝ)²⟩ = 1 + L₀/3 ≈ 4/3,
    ⇒ ⟨G_eff/G⟩ ≈ (3/4)·(1/μ₀) ≈ 1875.

v3.3's "~400×" quote is neither 1/μ₀ (=2500) nor the direction average (=1875); it is what you get if you further include a parallel-to-gradient projection: G_eff/G along ĝ = 1/[μ₀(1+L₀)] ≈ 1/(2μ₀) ≈ 1250, still not 400. The 400 number must implicitly absorb extra suppression (e.g., screen-gradient geometry, a finite-box cutoff of long-wavelength modes, or a quasi-linear dressing) not written in the section. That is already a sign we are not doing a clean analytic derivation.

### 2.1 Growth-rate ratio for identical initial conditions

For matter-domination (EdS) with an effective coupling ε ≡ (G_eff/G)·(Ω_source/Ω_m),

    δ ∝ a^p,     p_± = [−1 ± √(1 + 24 ε)] / 4.

ΛCDM (ε_ΛCDM = 1): p = 1, δ_ΛCDM ∝ a.

DFD-baryons (Ω_b = 0.049, Ω_m_ΛCDM = 0.30, same a(t)):

    ε_DFD = 1875 × (0.049/0.30) ≈ 306,
    p_DFD = (−1 + √(1 + 7345))/4 ≈ (−1 + 85.7)/4 ≈ 21.2.

So from identical linear ICs at a_i and identical final a_f = 1, the **linear analytic ratio is**

    δ_DFD / δ_ΛCDM = (a_f/a_i)^(p_DFD − 1) = (1/a_i)^20.2.

For a typical PM initial time a_i ≈ 0.02 (z_i = 50), that is (50)^20.2 ≈ 10³⁴. The DFD overshoot over ΛCDM from pure linearized MOND growth is **34 orders of magnitude**, not 5.4×. Even taking a generous a_i = 0.1, one gets 10^20. There is no tuning of x̄ inside the deep-MOND regime that gets this number down to O(5).

### 2.2 Why the simulation gives 5.4, not 10³⁴

The simulation has several strong saturation mechanisms the linearized formula ignores:

1. **Nonlinear saturation of μ(x).** As soon as δ grows enough that local accelerations exceed a₀, x shoots above 1, μ₀ → 1, and the enhancement collapses from 1875 to 1. This is fast: once any mode reaches δ ~ O(1), it quenches its own enhancement. 64³ PM at box 200 Mpc/h is dynamically shallow enough that most modes saturate early.
2. **Finite dynamic range.** Nyquist k_Nyq = π · 64 / 200 ≈ 1.0 h/Mpc. A 64³ PM code has only ~20 usable k-bins; the highest-G_eff modes are missing entirely.
3. **No EFE in the run.** The text itself flags this; an a_ext ≈ 6 a₀ cosmological EFE turns 1/μ₀ from ~2500 down to the quoted ~1.2, i.e., the true "intended" DFD gravity on cosmological scales is within ~20% of Newton, not 10³×.
4. **Timestep / softening** choices in a PM code of this size dominate δ_rms at the 10⁻³ level anyway.

So 5.4 is **not** a first-principles MOND-linear-growth number. The first-principles MOND-linear-growth number is astronomically larger, and the simulation result is small only because saturation + limited resolution + absence of EFE clamp the nonlinear evolution down by ~33 orders of magnitude.

---

## 3. Is 5.4 = 16/3?

16/3 = 5.3333…

Reported in v3.3: 5.4.

Relative deviation: (5.4 − 16/3)/(16/3) = 0.0667/5.333 = **1.25%**.

This is inside plausible PM noise (δ_rms values reported to 2 significant figures), so 16/3 is *numerically compatible* with 5.4. But there is **no analytic pathway** from the linearized DFD growth operator to 16/3 for this quantity:

- The 16/3 that Gary uses elsewhere (see `H6_16_over_3_path_integral.md`, `J1_0{1,2,3}_16_over_3_*.md`) is the **path-integral tower constant** governing α-tower / action normalization. It has the form 16/3 = 2⁴/3 arising from dimensional-regularization of a 4-form topological term. It is a *microphysical* constant, not a *structure-growth* ratio.
- The only 4/3 that naturally appears in the growth operator is the direction average ⟨1+L₀ cos²θ⟩ = 4/3 (with L₀→1). Squaring that gives 16/9, not 16/3. Multiplying it by an isotropy factor of 3 (three independent k̂ directions) gives 4, not 16/3. No combination I can construct from μ₀, L₀, Ω_b/Ω_m yields 16/3 without additional tuned factors.
- Even if one asserts δ² ∝ G_eff and computes a quasi-static ratio, the Ω_b/Ω_m ratio 0.049/0.30 = 0.1633 is already close to 1/6, and 1/6 · 1875 ≈ 306; there is no natural (0.1633)·(something) = 16/3 unless you pick the "something" to make it work.

**Conclusion on 16/3:** the numerical match 5.4 ≈ 16/3 is a coincidence at the 1.25% level, well inside the systematic uncertainty of a 64³ PM run reported to two sig figs. Calling it "16/3 exactly" would be retrofitting; there is no derivation that produces 16/3 for this observable from the DFD linear growth equation.

---

## 4. Answer to the L2 prompt

1. **Is 5.4 an exact analytical result?** **No.** It is a single-run 64³ particle-mesh number, with no EFE, reported to two significant figures. v3.3 itself labels the whole passage "Proof-of-concept" and requires ≥256³ + EFE for production quality.

2. **What does the linearized MOND growth equation with μ(x)=x/(1+x) actually predict?** At x̄=4×10⁻⁴ the direction-averaged G_eff/G ≈ 1875, giving an EdS growth exponent p ≈ 21 vs. ΛCDM's p=1 and a ratio δ_DFD/δ_ΛCDM of 10²⁰–10³⁴ depending on a_i. Pure linearized MOND growth *cannot* produce 5.4; the analytic prediction is catastrophic runaway, which is exactly why the text emphasizes that the cosmological EFE is mandatory and why naive DFD-without-EFE is not a physical cosmology.

3. **Is 5.4 = 16/3 exactly?** No. 5.4 − 16/3 = 0.067 (1.25% off). They are numerically close, but (a) 5.4 only has 2 sig figs so "exact" is meaningless, and (b) no analytic chain from the DFD growth operator yields 16/3 for this ratio. The 16/3 constant that appears elsewhere in the monograph is a path-integral / α-tower normalization and is dimensionally unrelated to a structure-growth overshoot.

4. **Formula, if any?** The closest clean formula, assuming the simulation's saturation effectively replaces 1/μ₀ with the EFE-dressed enhancement 1+ε_EFE and that δ²_DFD/δ²_ΛCDM ≈ (1+ε_EFE)·(Ω_b/Ω_m), is

       δ²_DFD / δ²_ΛCDM ≈ (1 + ε_EFE) · Ω_b/Ω_m.

   Solving for ε_EFE from the measured 5.4 gives 1+ε_EFE ≈ 5.4/0.163 ≈ 33, i.e. an effective dressed enhancement of ~33. That is neither 400 (no EFE), nor 1.2 (full cosmological EFE a_ext = 6 a₀), nor 16/3 · Ω_m/Ω_b. It is a simulation-specific number with no theorem behind it.

---

## 5. Recommendation for v3.4

- Demote "5.4×" from a numerical claim in the cosmology section to a footnote: "A 64³ PM proof-of-concept without EFE gives a δ_rms overshoot of order unity; see L2 audit."
- Do **not** tie 16/3 to this quantity. 16/3 is a path-integral constant; conflating it with a PM simulation ratio is a category error that will be flagged immediately on review.
- The production task is what v3.3 already flags: 256³ + EFE + a proper linear-theory check that reproduces σ₈(z) on LSS scales. Until that is in hand, the correct statement is "DFD admits a dust branch and a linear growth operator; quantitative agreement with ΛCDM structure growth is a program item."

---

## 6. Files consulted

- `/Users/garyalcock/claudecode/densityfielddynamics/Density_Field_Dynamics__A_Complete_Unified_Theory__v3_3/section_cosmology.tex` (lines 680-760, the proof-of-concept passage and the forward perturbation skeleton with G_eff)
- Search over v3.3 tree for "5.4" confirms section_cosmology.tex:697 is the only occurrence of this structure-growth claim; other "5.4" hits are unrelated (strong-field b_crit ≈ 5.44 GM/c², an appendix table entry, etc.).
- Related 16/3 context: `v34_research/H6_16_over_3_path_integral.md`, `v34_research/J1_01_16_over_3_conserved_current.md`, `v34_research/J1_02_16_over_3_path_integral_direct.md`, `v34_research/J1_03_16_over_3_initial_condition.md` (path-integral / α-tower use of 16/3; none is a structure-growth calculation).
