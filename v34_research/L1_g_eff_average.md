# L1 Report: Direction-Averaged ⟨G_eff/G⟩ vs 16/3

**Task:** Compute ⟨G_eff/G⟩ from v3.3 Eq. G-eff (section_cosmology.tex line 727) using
μ(x) = x/(1+x) at the EFE-corrected cosmological acceleration. Check whether it equals
16/3 exactly.

**Bottom line: NO. The direction-averaged ⟨G_eff/G⟩ at the EFE-corrected cosmological
x is ≈ 1.16, not 16/3 ≈ 5.333. The 5.4× structure overshoot quoted at line 697 is NOT
analytically 16/3 from this closure. The ≈1.2 number the paper already quotes is
reproduced exactly by the formula.**

---

## 1. Exact text quoted from v3.3 section_cosmology.tex

### 1a. The "5.4×" passage (lines 689–706)

> Proof-of-concept: N-body structure formation.
> A particle-mesh simulation (64³ grid, 200 Mpc/h box) comparing
> ΛCDM (Ω_m = 0.30), Newtonian-baryons (Ω_b = 0.049), and
> DFD-baryons (Ω_b = 0.049, μ(x) = x/(1+x)) on identical initial
> conditions demonstrates the key point: Newtonian-baryons produces
> negligible structure (δ_rms = 1.5×10⁻⁴), confirming the standard
> objection; DFD produces 43.8× more structure (δ_rms = 6.4×10⁻³),
> establishing that nonlinear gravity overcomes the baryonic deficit.
> The 5.4× overshoot relative to ΛCDM is physically expected:
> cosmological perturbation accelerations (x ≈ 4×10⁻⁴) lie deep in
> the MOND regime where the raw μ-function enhances gravity by
> ~400× without the cosmological External Field Effect (EFE) from
> the Hubble flow (a_ext ~ cH₀ ≈ 6 a₀). With the EFE, the effective
> enhancement drops from ~400 to ~1.2, which should bring DFD into
> quantitative agreement.

Key numbers the paper itself asserts:
- Bare δ_rms ratio DFD/ΛCDM = 6.4×10⁻³ / (≈ ΛCDM) = **5.4×** (N-body output)
- Bare enhancement without EFE: **~400×** (from x ≈ 4×10⁻⁴, μ ≈ x ⇒ 1/μ ≈ 2500… paper rounds)
- EFE-corrected enhancement: **~1.2×**
- a_ext ~ cH₀ ≈ **6 a₀**, so the EFE-dominated x̄ ≈ 6

### 1b. The G_eff formula (line 727)

> G_eff(a, k̂) = G / { μ₀ [1 + L₀ (k̂·ĝ)²] }

(Eq. G-eff, boxed.)

### 1c. Supporting definitions (line 729)

> For μ(x) = x/(1+x): μ₀ = x̄/(1+x̄) and L₀ = 1/(1+x̄)².
> On cosmological scales (x̄ « 1), G_eff → G/x̄, enhancing growth;
> on small scales (x̄ » 1), G_eff → G, recovering standard gravity.

(Note the paper defines L₀ = 1/(1+x̄)², NOT the x̄/(1+x̄)² form one gets from
L = x μ'(x). We use the paper's literal formula throughout.)

### 1d. EFE parameter

Paper gives `a_ext ~ cH₀ ≈ 6 a₀`, i.e. x̄_EFE ≈ 6.
The bare cosmological value (no EFE) is stated as x ≈ 4×10⁻⁴.

---

## 2. Direction average — closed form

From Eq. (G-eff) with μ₀, L₀ constants and direction integral over θ between k̂ and ĝ:

⟨G_eff/G⟩ = (1/2) ∫_{-1}^{1} dc / [μ₀ (1 + L₀ c²)]
          = (1/μ₀) · arctan(√L₀) / √L₀          ... (*)

Substituting the paper's definitions μ₀ = x̄/(1+x̄), L₀ = 1/(1+x̄)²:

√L₀ = 1/(1+x̄)
arctan(√L₀) = arctan(1/(1+x̄))

⟨G_eff/G⟩ = [(1+x̄)/x̄] · (1+x̄) · arctan(1/(1+x̄))
          = **[(1+x̄)² / x̄] · arctan(1/(1+x̄))**         ... (**)

This is the exact closed form for v3.3's closure with μ(x) = x/(1+x).

---

## 3. Numerical evaluation at the EFE-corrected cosmological x

**Case A — Paper's stated EFE value x̄ = 6 (a_ext ≈ 6 a₀):**
- μ₀ = 6/7 = 0.8571
- L₀ = 1/49 = 0.02041
- ⟨G_eff/G⟩ = (49/6) · arctan(1/7) = 8.1667 · 0.14189 = **1.1588**

This reproduces the "~1.2" the paper quotes to 2 significant figures. ✓

**Case B — Task's alternative x̄ = 1/(2√α) with α = 1/137:**
- x̄ = √137/2 = 5.8523
- μ₀ = 5.8523/6.8523 = 0.8541
- L₀ = 1/(6.8523)² = 0.02130
- ⟨G_eff/G⟩ = **1.1627**

Effectively identical to Case A (as expected — both give x̄ ≈ 6).

**Case C — Bare cosmological x̄ = 4×10⁻⁴ (no EFE):**
- μ₀ ≈ 4×10⁻⁴
- L₀ ≈ 1
- ⟨G_eff/G⟩ = (1/μ₀) · arctan(1)/1 = (π/4)/μ₀ ≈ 1963
- N-body quotes ~400× — the two disagree, because the N-body enhancement is
  1/μ at the **particle acceleration** scale, not the direction-averaged
  linear G_eff. Consistent with "roughly 400" the paper gives as an order-of-magnitude.

---

## 4. Comparison with 16/3

16/3 = **5.3333**.
Computed ⟨G_eff/G⟩ at EFE-corrected x̄ ≈ 6: **1.159**.

**Ratio: 16/3 / 1.159 = 4.60. They are not equal, and no simple rational
multiplier connects them.**

Inverting Eq. (**) to ask "what x̄ gives ⟨G_eff/G⟩ = 16/3?" yields
**x̄ ≈ 0.1844** — nowhere near either the bare cosmological value (4×10⁻⁴)
or the EFE-corrected value (6). There is no choice of cosmological x̄
consistent with the paper's own EFE that produces 16/3.

---

## 5. What is the 5.4× then?

Re-reading line 697 carefully: the 5.4× is the N-body output ratio
δ_rms(DFD) / δ_rms(ΛCDM) at z = 0 at 64³ resolution with the EFE
**not yet implemented**. The paper explicitly flags it as an
**uncorrected** (no-EFE) number and predicts that adding the EFE will
suppress the linear enhancement factor from ~400 to ~1.2 — which, since
growth scales roughly as √(G_eff/G)·t, would drag the nonlinear δ_rms
ratio from 43.8 downward toward unity, removing the 5.4× overshoot.

In other words: **the paper's own internal logic treats 5.4× as a
simulation artifact to be removed by the EFE, not as a number to be
derived**. The closed form above confirms this quantitatively —
with the EFE switched on, ⟨G_eff/G⟩ is 1.16, not 5.33.

The coincidence 5.4 ≈ Ω_c/Ω_b = 0.265/0.049 = 5.41 that K1-1 spotted is
**NOT reproduced by the direction average of Eq. (G-eff)**. If it is a
real feature of the underlying dynamics, it does not live in the
v3.3 linear closure as written. Either:
(i) it is numerical coincidence from the 64³ proof-of-concept
    (the paper's own position — supported by this calculation), or
(ii) it emerges from some nonlinear/z-dependent effect that the
    linear, constant-x̄ average in Eq. (G-eff) cannot capture.

Either way, **16/3 is not analytically derived here**. The breakthrough
scenario envisioned in the task background does not materialize from
the v3.3 closure.

---

## 6. Closed-form result (for the record)

With μ(x) = x/(1+x) and v3.3's stated L₀ = 1/(1+x̄)²:

⟨G_eff/G⟩(x̄) = [(1+x̄)² / x̄] · arctan(1/(1+x̄))

Asymptotics:
- x̄ → ∞: → 1  (Newton)
- x̄ → 0: → (1/x̄) · (π/4) = π/(4x̄)  (deep MOND, direction-averaged)
- x̄ = 6: ≈ 1.159  ← EFE-corrected cosmological value
- x̄ = 0.1844: = 16/3  (required for the K1-1 coincidence — NOT physically
                        motivated in v3.3)

## 7. Conclusion

- v3.3 line 697's 5.4× is **not** analytically equal to 16/3 via
  the direction-averaged G_eff closure.
- The closure's exact EFE-corrected average ⟨G_eff/G⟩ = 1.159, matching
  the paper's own "~1.2" claim.
- To obtain 16/3 from this formula would require x̄ ≈ 0.184, which
  contradicts the paper's stated EFE (x̄ ≈ 6).
- The Ω_c/Ω_b ≈ 5.43 coincidence remains unexplained by the v3.3
  linear perturbation machinery. The most defensible current
  interpretation is the paper's original one: 5.4× is a transient
  simulation artifact to be absorbed by the EFE, not a derivation
  of 16/3.

**16/3 is NOT derived from the μ-crossover mechanism at the level of
Eq. (G-eff). The breakthrough does not hold.**
