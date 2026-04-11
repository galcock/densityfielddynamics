# N3 Report: Does the elliptic ψ-structure force Ω_χ/Ω_b = 16/3 as a kernel ratio?

**Task.** DFD's ψ-field equation is *elliptic on a t = const slice* — the
quasi-static MOND-type Poisson equation

  ∇·[μ(|∇ψ|/a*) ∇ψ] = −(8πG/c²)(ρ_b − ρ̄_b),     (DFD-1)

(section_formalism.tex, eqs. around lines 274–293; reproduced verbatim in
v3.3). There is no ψ̇-wave operator in this sector — the temporal completion
in Appendix Q lives in a separate K(|ψ̇−ψ̇₀|) functional that decouples in the
quasi-static limit. So on each cosmological time slice, ψ is *instantaneously
determined* by ρ_b through (DFD-1). Time enters only as a parameter through
ρ_b(x,t).

The question for this round: does this elliptic structure mean that χ
("DFD dark matter") is **not a relic** at all, but a *kernel response* of
ψ to the baryon distribution? If so, Ω_χ/Ω_b should follow as a Green's
function functional of (DFD-1), not from cosmological history. And then
16/3 either falls out of that functional or it doesn't.

**Bottom line: NO. The elliptic ψ-sector does NOT yield Ω_χ/Ω_b = 16/3 as a
spatially-averaged kernel ratio. The kernel ratio is *not even a fixed
number* — it depends explicitly on ⟨|∇ψ|/a*⟩, i.e. on the matter
distribution, and at the cosmologically relevant value (the same EFE-corrected
x̄ ≈ 6 used in L1) it sits at ⟨ρ_χ/ρ_b⟩ ≈ 0.16, *off by ~30× from 16/3
and on the wrong side of unity*. The 16/3 number is not a property of the
DFD elliptic kernel.**

This is the same conclusion L1 reached for ⟨G_eff/G⟩, and it is *forced* by
the same closed form. The two numbers (1.16 vs. 5.33) and (0.16 vs. 5.33) are
two different functionals of the same kernel; neither produces 16/3 at
the EFE-corrected x̄.

---

## 1. χ as kernel response, not relic — the framing

Let a_DFD ≡ (c²/2)∇ψ be the DFD acceleration field obtained from (DFD-1).
A *Newtonian observer* who didn't know about DFD would interpret the same
acceleration field as being sourced by some "total matter" density ρ_tot
via standard Poisson:

  ∇·a_DFD = −4πG ρ_tot.            (NEWT)

The deficit ρ_tot − ρ_b is what the Newtonian observer calls "dark matter".
In DFD, by construction, this deficit is *not* a relic species — it is the
back-reaction of the elliptic ψ-equation. Define

  ρ_χ(x) ≡ ρ_tot(x) − ρ_b(x) = −(1/4πG) ∇·a_DFD(x) − ρ_b(x).   (DFD-χ)

This is an *operator* applied to ρ_b: ρ_χ = K[ρ_b] where K is the
nonlinear elliptic Green's functional of (DFD-1) followed by a divergence.
There is no time integration, no freeze-out, no misalignment. *That is the
content of the user's framing,* and it is correct: in a strictly elliptic
ψ-sector with quasi-static dynamics, χ is a kernel object, not a relic.

So the meaningful question is: what is ⟨ρ_χ⟩/⟨ρ_b⟩ for this kernel?

---

## 2. The kernel ratio in closed form

Take the divergence of the DFD field equation directly. Using
a_DFD = (c²/2)∇ψ and (DFD-1):

  ∇·[μ ∇ψ] = −(8πG/c²)(ρ_b − ρ̄_b)
  ⇒ ∇·[(2μ/c²) a_DFD] = −(8πG/c²)(ρ_b − ρ̄_b)
  ⇒ ∇·[μ a_DFD] = −4πG (ρ_b − ρ̄_b).      (DFD-2)

Compare with the Newtonian relation ∇·a_DFD = −4πG ρ_tot (eq. NEWT). For a
spatially constant μ (or after spatial averaging — see §3 below):

  μ ∇·a_DFD ≈ −4πG (ρ_b − ρ̄_b)
  ⇒ ρ_tot ≈ (1/μ)(ρ_b − ρ̄_b)
  ⇒ ρ_χ ≈ (1/μ − 1) ρ_b − (ρ̄_b/μ).

Take the spatial average ⟨·⟩ over the box, with ⟨ρ_b − ρ̄_b⟩ = 0 by
construction. Naively the LHS averages to zero. The trick is that the
ratio of fluctuations does not. Use the linear-perturbation form: write
ρ_b = ρ̄_b(1 + δ_b), and similarly ρ_χ = ρ̄_χ(1 + δ_χ) at linear order.
Then (DFD-2) and (NEWT) together give the *amplitude* relation

  ρ̄_χ δ_χ = ρ̄_b δ_b · (1/μ̃ − 1),     (KERNEL)

where μ̃ is the direction-and-mode-averaged μ at the relevant scale.
This is the Green's-function ratio the user asked for: it relates the
DFD-induced "dark matter overdensity" to the baryon overdensity through
*one and only one* number, the inverse of the DFD μ-function evaluated at
the cosmological gradient scale.

The mean energy-density ratio Ω_χ/Ω_b can then *only* be obtained from
(KERNEL) under one extra assumption: that δ_χ ≈ δ_b on average (i.e. that
the χ response tracks baryons mode-by-mode at the scale that dominates
the variance). Under that assumption:

  Ω_χ/Ω_b = ρ̄_χ/ρ̄_b = ⟨1/μ̃⟩ − 1.        (RATIO)

This is the elliptic-kernel prediction, written purely in terms of the
DFD μ-function and the cosmological gradient scale. *It is not 16/3 by
construction; it is whatever ⟨1/μ̃⟩ − 1 happens to be.*

---

## 3. Numerical evaluation — same x̄ as L1

Use the v3.3 paper's own EFE-corrected cosmological gradient scale,
x̄ ≈ 6 (a_ext ≈ cH₀ ≈ 6 a₀; section_cosmology.tex line ~727). With the
v3.3 closure μ(x) = x/(1+x):

  μ(6) = 6/7 = 0.8571
  1/μ(6) = 7/6 = 1.1667
  Ω_χ/Ω_b = 1/μ − 1 = **1/6 ≈ 0.1667**.

That is the prediction of (RATIO) at the EFE-corrected cosmological
gradient. Compare to the target 16/3 = 5.333:

  ratio = 5.333 / 0.1667 = **32×**.

The kernel response is too small by more than an order of magnitude, and
in fact predicts *less* dark matter than baryons, not more. This is
consistent with L1's ⟨G_eff/G⟩ = 1.159 at the same x̄: both functionals are
saying that *with the EFE on*, the DFD μ-correction is mild, not the
factor-of-five enhancement that 16/3 would require.

For completeness, do the inversion: what x̄ gives Ω_χ/Ω_b = 16/3?

  1/μ̃ − 1 = 16/3 ⇒ 1/μ̃ = 19/3 ⇒ μ̃ = 3/19 = 0.1579
  μ(x) = x/(1+x) = 3/19 ⇒ x = 3/16 = **0.1875**.

So 16/3 emerges *only* at x̄ ≈ 0.1875. Note that this value is essentially
identical to the x̄ ≈ 0.1844 that L1 reported as required for ⟨G_eff/G⟩
to equal 16/3 (the slight difference is because the two functionals
respond slightly differently — one is the direction-averaged G_eff, the
other is the inverse μ at the dominant mode). **Both functionals point to
the same forbidden x̄ ≈ 0.18**, which is two orders of magnitude away from
the v3.3 EFE-corrected value x̄ ≈ 6 and four orders of magnitude away from
the bare cosmological value 4×10⁻⁴.

There is no consistent choice of cosmological gradient scale within the
v3.3 closure that produces 16/3 from the elliptic kernel.

---

## 4. Cross-check with L1: are 1.159 and 0.167 the same kernel viewed twice?

L1 computed F₁(x̄) ≡ ⟨G_eff/G⟩ = [(1+x̄)²/x̄] · arctan(1/(1+x̄)).
Here we computed F₂(x̄) ≡ Ω_χ/Ω_b = 1/μ(x̄) − 1 = 1/x̄.

These are *different functionals* of the same μ-function:

| x̄    | F₁ = ⟨G_eff/G⟩ | F₂ = 1/x̄ | F₁/F₂ |
|------|------|------|------|
| 0.1875 | 5.41  | 5.33 | 1.015 |
| 0.184  | 5.50  | 5.43 | 1.013 |
| 1     | 1.571 | 1.00 | 1.571 |
| 6     | 1.159 | 0.167 | 6.94 |
| ∞     | 1     | 0     | ∞    |

Two observations:

(a) **At the forbidden x̄ ≈ 0.18, F₁ and F₂ agree to within 1.5%**. This
   is not a coincidence: in the deep-MOND limit x̄ ≪ 1, F₁ → π/(4x̄) and
   F₂ → 1/x̄, and π/4 ≈ 0.785 ≈ 1 to leading order. Both functionals
   *would* give ≈16/3 if you were allowed to put x̄ at 0.18. Neither does
   at the physical x̄ = 6.

(b) **At the physical x̄ = 6, F₁ ≫ F₂**. The direction-averaged ⟨G_eff/G⟩
   stays "hot" (1.159) longer than the inverse-μ kernel (0.167) because
   the arctan integral has a Newtonian floor of 1 at x̄ → ∞, while 1/x̄ − 1
   → −1. The two functionals diverge in the *Newtonian* regime, which is
   the regime the EFE puts us in.

The take-away from the cross-check: 16/3 is not "hiding in a different
functional of the same G_eff kernel". Both natural functionals
(direction-averaged G_eff, and the elliptic-kernel ρ_χ/ρ_b ratio) give
small numbers at the EFE-corrected x̄, and both would *only* give 16/3 at
an x̄ that the paper's own EFE forbids.

---

## 5. Why the elliptic framing doesn't rescue 16/3

The user's intuition — that an elliptic ψ-sector turns χ into a
*kernel object* rather than a *relic* — is correct at the structural level.
What the calculation in §§2–3 shows is that this re-framing **doesn't help**:

1. The kernel exists (eq. KERNEL) and has a clean closed form (eq. RATIO).
2. The kernel ratio depends only on the dimensionless gradient scale x̄.
3. The v3.3 paper's own EFE pins x̄ ≈ 6 cosmologically.
4. At x̄ ≈ 6, the kernel produces ρ_χ/ρ_b ≈ 1/6, not 16/3.
5. To get 16/3 you need x̄ ≈ 0.19, which contradicts the paper's EFE.

In other words: the elliptic re-framing **moves the failure** from
"4D anomaly matching at the production epoch" to "the v3.3 μ-function at
the EFE-corrected gradient scale". It does not eliminate it. The
arithmetic obstruction is the same one L1 found: at x̄ = 6, μ ≈ 1, so all
μ-derived enhancement factors collapse toward unity, and 16/3 becomes
unreachable from any natural functional of (DFD-1).

The only ways out (none of which are accomplished here):

(i) **Reject the EFE.** Use the bare cosmological x̄ ≈ 4×10⁻⁴ instead.
    Then 1/μ ≈ 2500 and Ω_χ/Ω_b would be enormous, not 16/3 either.
    (This was the original objection that motivated the EFE in the first
    place — see L1 §3 Case C.)

(ii) **Replace μ.** Some non-x/(1+x) crossover function might give exactly
    16/3 at exactly x̄ = 6. But then the crossover function is being
    *fit* to reproduce 16/3, which is the opposite of deriving it from
    the kernel.

(iii) **Make x̄ scale-dependent.** Allow x̄ to take the small-scale
    value (0.18) for some smoothing scale that dominates the χ-response,
    while the EFE pins large-scale x̄ ≈ 6. This is a real possibility
    but it requires a *separate* calculation showing why the χ kernel is
    dominated by modes where x̄ ≈ 0.18 — and the L17/L18 R²-dominance work
    in this directory hasn't produced that calculation.

(iv) **Abandon (DFD-1) for the χ sector.** Give χ its own field equation
    rather than treating it as a Green's-function image of ρ_b. But that
    is *exactly* the relic interpretation the user's framing was trying
    to escape from.

None of (i)–(iv) constitutes a derivation. The honest reading is that
the elliptic kernel provides a cleaner *structure* for thinking about
ρ_χ but does not provide the *number* 16/3.

---

## 6. Closed-form summary (audit-ready)

DFD elliptic field equation (v3.3, section_formalism.tex eq. boxed):
  ∇·[μ(|∇ψ|/a*) ∇ψ] = −(8πG/c²)(ρ_b − ρ̄_b)

Definition of χ as kernel response (this report, eq. DFD-χ):
  ρ_χ ≡ −(1/4πG) ∇·a_DFD − ρ_b,    a_DFD ≡ (c²/2) ∇ψ

Linear-perturbation kernel ratio (eq. RATIO):
  Ω_χ/Ω_b = 1/μ(x̄) − 1 = 1/x̄    for μ(x) = x/(1+x)

Numerical values at v3.3's EFE-corrected x̄:
  x̄ = 6  ⇒  Ω_χ/Ω_b = 1/6 ≈ 0.167
  Target 16/3 ≈ 5.333  ⇒  required x̄ = 3/16 ≈ 0.1875

Cross-check vs L1:
  L1's required x̄ for 16/3 from ⟨G_eff/G⟩: 0.184
  N3's required x̄ for 16/3 from 1/μ − 1:   0.1875
  Both are ~32× smaller than the EFE value x̄ ≈ 6.

---

## 7. Conclusion

- The elliptic ψ-equation does admit a clean kernel definition of ρ_χ
  in which χ is not a relic but a Green's-function back-reaction to ρ_b.
- The resulting kernel ratio is Ω_χ/Ω_b = 1/μ(x̄) − 1, a one-parameter
  family in x̄.
- At v3.3's stated EFE-corrected x̄ ≈ 6 the kernel gives 0.167, not
  5.333. The discrepancy is ~32× and on the wrong side of unity.
- 16/3 is *not* hiding in a different functional of the L1 kernel. Both
  the direction-averaged G_eff functional and the elliptic-kernel ρ_χ
  functional collapse toward small numbers at x̄ = 6 because μ(6) ≈ 1.
- The required x̄ ≈ 0.18 is identical (to within ~2%) for both
  functionals, but is forbidden by the same EFE the paper uses to fix
  cosmological growth.
- The elliptic re-framing does not produce 16/3. It clarifies the
  structure of the obstruction but does not eliminate it.

**Negative result. No positive numerical claim that needs re-auditing.**
The 16/3 ratio is not derivable from the v3.3 elliptic ψ-kernel under
the paper's own EFE assumption. Any future attempt should target one of
the four loopholes in §5, with explicit attention to whichever scale
dominates the χ-response variance.
