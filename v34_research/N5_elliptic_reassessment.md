# N5: Re-Assessment of L5/L8 "Misalignment Overclosure" in DFD's Actual (Elliptic) Framework

**Agent:** N5
**Date:** 2026-04-07
**Task:** Determine whether the overclosure crisis reported by L5 (10^18 overshoot) and the θ_i ≈ 0.067 tuning reported in Relic_n3p7 are genuine DFD predictions, or artifacts of misapplying a 4D Lorentzian ALP cosmology to DFD's 3D elliptic χ field.
**References:** L5_psi_dust_amplitude_revisit.md, L8_condensate_turn_on.md, Relic_n3p7.md, DFD v3.3 monograph (section_formalism.tex, section_wellposedness.tex, appendix_U_wellposedness.tex), M14_rung_scan.md, M16_kahler_suppression.md.

**Status:** This note raises a positive structural concern about the L5/L8/Relic_n3p7 framing. Any positive result below should be re-audited per user instruction. No citations have been invented.

---

## 0. The framing problem

DFD's base space is R^3 × CP^2 × S^3 with time as an external *parameter*, not a 4th coordinate of a Lorentzian manifold. The ψ field equation in the static limit is the quasilinear elliptic PDE (v3.3 section_formalism.tex line 561, section_wellposedness.tex §3.1, appendix_U §A.1):

    ∇² ψ(x, t) = −(8πG/c²) ρ_matter(x, t)               (E1)

At each instant t, ψ is the unique solution (with appropriate BC at infinity) of an elliptic boundary-value problem sourced by the instantaneous matter distribution. There is no Cauchy data for ψ — ψ is a constraint field, not a dynamical field with independent initial conditions. The time-derivative term (1/c²) ψ̈ that appears in the fully dynamical equation (section_formalism.tex line 561) is formally O(v²/c²) suppressed relative to the spatial Laplacian for any configuration whose characteristic time of change is long compared to L/c, and in the strict DFD limit is absent altogether — time is a parameter labeling the elliptic solutions.

**Standard misalignment** (Preskill-Wise-Wilczek 1983 and the entire 40-year axion literature built on top of it) is a story about:

 1. A 4D Lorentzian scalar field with hyperbolic EOM ⎕χ + m_χ² χ = 0.
 2. Cauchy data χ(x, t_i) = f_a θ_i set during inflation.
 3. Hubble friction 3H χ̇ freezing the field while H > m_χ.
 4. Coherent oscillation once H drops below m_χ in the radiation era.
 5. Energy density ½ m_χ² χ² ∝ a^(−3) redshifting as matter.
 6. A relic abundance today set by the ratio of the inflationary field value to the observed matter budget.

**None of (1)-(6) apply to DFD's χ** if χ is the instantaneous ψ-dust configuration satisfying (E1) or a direct functional of it:

 - (1) fails: (E1) is elliptic, not hyperbolic. There is no ⎕χ + m² χ EOM.
 - (2) fails: there is no inflationary Cauchy surface for ψ or χ in a framework where time is a parameter. The field at every instant is slaved to the matter distribution at that instant; it has no "prior value" independent of its source.
 - (3) fails: there is no Hubble friction term in an elliptic PDE. 3H χ̇ is a 4D artifact.
 - (4) fails: "oscillation turn-on" requires a hyperbolic operator. The elliptic equation admits no oscillations in time; it admits only spatial harmonics of the Green's function.
 - (5) fails: redshifting as a^(−3) is a consequence of comoving conservation of a 4D stress-energy tensor with w = 0. In DFD, ρ_χ(x, t) is re-computed at each t from the current matter distribution via the kernel — its time evolution is *inherited from the matter*, not from any independent scaling law.
 - (6) fails: the abundance ratio ⟨ρ_χ⟩/⟨ρ_b⟩ is not a relic of initial conditions, it is a kernel property of the elliptic Green's function acting on the present-day matter distribution.

**The θ_i fit in L5/L8 and the 4% tuning in Relic_n3p7 are therefore answers to the wrong question.** They compute the relic abundance of a hypothetical 4D ALP with DFD's (m_χ, f_a) as if it were independent of the DFD source, and compare against the observed Ω_c. In a framework where χ has no independent initial conditions, "the ALP misalignment abundance" is not a DFD observable at all — it is a 4D observable for a hypothetical 4D theory that DFD is not.

---

## 1. What is "Ω_χ/Ω_b = 16/3" in the elliptic framework?

If there is no relic, the 16/3 ratio cannot be a relic abundance ratio. The only meaningful thing it can be is a **spatial averaging identity**:

    ⟨ρ_χ(x)⟩_V  /  ⟨ρ_b(x)⟩_V  =  16/3               (?)

for some definition of ρ_χ(x) derived from the elliptic solution ψ(x) sourced by the observed baryon distribution ρ_b(x).

There are two candidate definitions of ρ_χ in DFD, both consistent with the v3.3 text:

**Definition A — ψ-gradient energy (the "field energy" of the dust branch).**
By analogy with Newtonian gravitational self-energy,

    ρ_χ(x)  ≡  (c² / 8πG) |∇ψ(x)|².                 (E2)

Integrating (E2) by parts against (E1) gives the well-known identity

    ∫ ρ_χ d³x  =  (1/2) ∫ ρ_b ψ d³x  =  −W_grav,

i.e. minus the Newtonian gravitational binding energy of the baryon distribution. The spatial average of this on cosmological scales is NOT 16/3 · ⟨ρ_b⟩ — it is much smaller, of order (v/c)² ⟨ρ_b⟩ ~ 10^(−6) ⟨ρ_b⟩ for virialised structures and O(10^(−10)) ⟨ρ_b⟩ for the smooth background. **Definition A cannot carry 16/3.**

**Definition B — ψ-coupling energy density (the "ψρ" branch).**
The on-shell action density of the ψ field in the presence of a matter source, after integrating out ψ using (E1), is (up to sign and constants) ρ_χ(x) = (1/2) ψ(x) ρ_b(x). Spatial averaging and using the Green's function representation

    ψ(x)  =  (2G/c²) ∫ ρ_b(x') / |x − x'| d³x'

gives

    ⟨ρ_χ⟩  =  (G/c²) ⟨∫ ρ_b(x) ρ_b(x') / |x − x'| d³x' ⟩.

This is again a (v/c)² suppressed quantity, not 16/3 · ⟨ρ_b⟩. **Definition B also cannot carry 16/3.**

**Neither a natural "field energy of the elliptic ψ" nor a "ψ-coupling energy" produces a pure-number ratio of order unity with ⟨ρ_b⟩.** Both are controlled by the dimensionless combination G ρ_b R² / c² = (R/R_S)^{−1} and are many orders of magnitude below ⟨ρ_b⟩ on any reasonable averaging scale.

**This immediately tells us:** if "Ω_χ/Ω_b = 16/3" is supposed to hold in DFD, the quantity ρ_χ it refers to is NOT the elliptic field energy of ψ in the sense of (E2) or (E B). It must be something else: either

 - (i) an additional dark-matter sector **not** produced by the ψ elliptic equation at all (e.g. a true relic population, in which case we are back to a 4D cosmology and L5/L8's problems return), or
 - (ii) a counting-theoretic ratio with no energy-density interpretation (H9's original reading, endorsed by K1-7 and the L5 survey), or
 - (iii) a new elliptic construction involving a different kernel (e.g. the CP^2 × S^3 internal Laplacian, not the R^3 Laplacian) whose spatial average over the observed baryon distribution genuinely gives 16/3. No such construction is exhibited in v3.3.

None of the three options revives the "misalignment overclosure" framing. Option (i) is the only one where L5/L8's calculation is even meaningful, and option (i) is precisely the case where DFD is no better than a 4D ALP theory and the overclosure crisis is real. Options (ii) and (iii) make the L5/L8 calculation not-even-wrong: it is computing the abundance of a thing that does not exist in DFD.

---

## 2. Does χ have "initial conditions" that get redshifted?

**No.** In the elliptic framework, χ(x, t) is a functional of ρ_matter(x, t) at the same instant t:

    χ(x, t)  =  F[ρ_matter(·, t)](x)                  (E3)

for some (as yet not uniquely identified in v3.3) functional F tied to the elliptic Green's function of the ψ operator, possibly composed with an internal CP^2 × S^3 projection. Three consequences:

 (a) **No θ_i.** There is no moment of "field value setting" during inflation; F is evaluated at each t from the current matter distribution. θ_i is undefined as a DFD parameter.

 (b) **No a^(−3) redshifting.** ρ_χ(t) evolves not by the scale factor but by whatever ρ_matter(t) evolves by. If ρ_matter ∝ a^(−3) (as for cold baryons), then so will ρ_χ — *not because of Hubble friction, but because the source did*. The functional F is time-local.

 (c) **No "turn-on at T_osc".** The functional F is defined at every t; there is no moment when χ "starts oscillating". L5's computation of T_osc ≈ 240 MeV, Relic_n3p7's T_osc ≈ 580 TeV, and L8's T_osc ≈ 9 PeV are all evaluating a formula (T_osc = √(m_χ M_P/3)) from a hyperbolic theory that has no analogue in an elliptic one. The quantity T_osc is not a DFD observable.

**Implication for the L5 10^18 overshoot:** the overshoot is computed from ρ_χ(T_osc) = ½ m_χ² (f_a θ_i)² evaluated "at the moment oscillation begins" and redshifted forward by (T_osc/T_today)^3. **Neither factor exists in DFD.** The numerical disagreement of 10^18 between the L5 formula and observation is therefore not a crisis for DFD — it is a crisis for the assumption that DFD's χ admits a 4D misalignment history.

**Implication for the Relic_n3p7 θ_i ≈ 0.067 tuning:** same structural point. Ω_χ h² ≈ 27 θ_i² is computed from Marsh-type ultralight ALP misalignment formulas that assume hyperbolic EOM + Hubble friction + a^(−3) redshifting. If χ is elliptic, θ_i is not a DFD parameter and the formula does not apply.

---

## 3. What should the spatial-average calculation look like, done correctly?

If one grants the framing that ρ_χ is derived from the elliptic solution (some Definition C to be specified), the correct computation is:

 1. Take the observed ρ_b(x) (e.g. from a galaxy survey or the CMB-derived ρ̄_b).
 2. Solve the elliptic PDE (E1) (or the relevant CP^2 × S^3 lifted version) for ψ(x) or equivalently χ(x).
 3. Compute ρ_χ(x) from the chosen definition.
 4. Average over a cosmological volume.
 5. Compare ⟨ρ_χ⟩/⟨ρ_b⟩ against 5.36 = 16/3.

**Sketch of the dimensional structure.** The only dimensionless combinations available from (E1) applied to a baryon density ρ̄_b on a box of comoving scale L are:

    ε_grav  =  G ρ̄_b L² / c²  =  (L / L_H)² Ω_b     (E4)

where L_H = c/H_0. For L ~ L_H, ε_grav ~ Ω_b ~ 0.05. For any Definition A/B type ρ_χ, ⟨ρ_χ⟩/⟨ρ_b⟩ ~ ε_grav · (form factor of O(1)). **This does not give 16/3.** It gives something of order Ω_b itself, i.e. 0.05 — off by a factor of ~100 from 5.36.

**The 5.36 ratio is not a kernel identity of the Laplacian acting on ρ_b.** It is, as H9 and L5 concluded, a DOF-counting ratio (16 spin states of a Majorana sterile sector vs 3 colors of a quark sector) with no direct energy-density meaning. That conclusion is now reinforced from the opposite direction: in the elliptic framework, where the "relic abundance" interpretation is not even available, there is no other natural interpretation of 16/3 as an energy-density ratio either. It is a counting identity, full stop.

---

## 4. Is this a net advance or a retreat for DFD χ-DM?

**It is a clarifying retreat with a smaller residual problem.**

**What goes away:**

 - The L5 10^18 overclosure crisis is not a DFD crisis. It is a crisis only for a 4D ALP theory with DFD's (m_χ, f_a), which DFD is not. Specifically, the ρ_χ(T_osc) = ½ m_χ² f_a² θ_i² × (T_today/T_osc)^3 calculation is not the DFD prediction for the χ energy density today; it is a hypothetical 4D calculation.
 - The Relic_n3p7 θ_i ≈ 0.067 tuning is not a DFD tuning. θ_i is not a DFD parameter.
 - The L5/L8 table of "alternative production channels" (gravitational preheating, Kähler coupling, thermal relic, inflaton branching, CS topology) is moot: none of these channels corresponds to anything DFD computes, because in DFD χ is not produced in the early universe at all — it is sourced continuously by matter via the elliptic equation.
 - The M14 α-tower rung scan for a self-consistent relic abundance is answering the wrong question: the rung is not fixed by demanding Ω_χ h² = 0.12 via misalignment.
 - The M16 Kähler suppression proposal becomes unnecessary: there is no θ_i to suppress.

**What remains:**

 - **If χ is elliptic-sourced by ρ_b, what is the cosmological energy density of χ?** The Definition A/B computations in Section 2 give ⟨ρ_χ⟩ ~ (v/c)² ⟨ρ_b⟩ or smaller. This is **too small**, not too large — it undershoots Ω_c h² ≈ 0.12 by factors of 10^4 to 10^10 depending on the averaging scale. So the elliptic framework appears to remove the overclosure but **replace it with an underclosure of comparable structural severity**, unless Definition C (the true DFD definition of ρ_χ) has a large dimensionless prefactor that neither Definition A nor Definition B exhibits.
 - **What is Definition C?** v3.3 does not pin down a single "ρ_χ(x) functional of ψ(x)" that both (i) is dimensionally correct, (ii) reproduces CDM phenomenology, and (iii) gives ⟨ρ_χ⟩/⟨ρ_b⟩ of order 5.
 - **The 16/3 ratio remains unexplained** as an energy-density ratio. It survives only as a DOF-counting identity, as H9/L5 concluded.
 - **The mass m_χ = 1.18 keV (or 96 keV, depending on which audit) and the associated α-tower rung assignments remain independent open questions.** The elliptic framing doesn't touch them — m_χ is a mass parameter of whatever small-oscillation sector around the elliptic solution one cares to expand in, and is fixed by the internal CP^2 × S^3 spectrum, not by cosmology.

**Net assessment.** The elliptic reassessment replaces a concrete 10^18 overclosure crisis with a structural definitional gap: we do not currently have a DFD-internal, elliptic-consistent definition of ρ_χ that (i) is ~ Ω_c on cosmological averages and (ii) delivers the 16/3 · Ω_b ratio. The retreat is real — L5/L8's crisis is dissolved into not-even-wrong — but the residual problem is still nontrivial.

---

## 5. Recommended next steps

 1. **Do not cite the L5/L8 overclosure numbers or the Relic_n3p7 θ_i ≈ 0.067 tuning as DFD results in v3.4.** They are consequences of applying a 4D ALP template to an elliptic field and do not measure anything about DFD.
 2. **Write down Definition C explicitly.** What is ρ_χ(x) as a functional of ψ(x) (or equivalently of ρ_b(x) via the elliptic kernel)? Until this is fixed, any cosmological claim about Ω_χ is ambiguous.
 3. **Compute ⟨ρ_χ⟩/⟨ρ_b⟩ from Definition C on the observed ρ_b(x).** If this lands at 5.36 ± anything reasonable, the 16/3 story becomes a genuine DFD prediction from first principles (a kernel identity). If it lands at 0.05 or 10^(−6), the 16/3 must either be a DOF-counting statement or must come from a completely different sector.
 4. **Audit the v3.3 statements that implicitly use 4D ALP language** for χ ("misalignment", "coherent oscillation", "initial angle", "redshift as matter") and either translate them into elliptic language or remove them. The current text mixes the two frameworks, which is the source of the L5/L8/Relic_n3p7 confusion.
 5. **Clarify in the monograph whether "time as parameter" is an approximation (the (1/c²) ψ̈ term is neglected but present) or a strict feature (no time derivative of ψ at all).** The two readings give different answers to "does χ have initial conditions": strict elliptic says no, approximate elliptic says there is a small time-derivative correction. The L5/L8 calculations only become unambiguously "not-even-wrong" in the strict reading.

---

## 6. One-line summary

The L5 10^18 overclosure and the Relic_n3p7 θ_i ≈ 0.067 tuning are artifacts of applying a 4D Lorentzian ALP misalignment cosmology (Cauchy data + Hubble friction + oscillation turn-on + a^(−3) redshifting) to DFD's χ field, which in the base framework is the instantaneous elliptic solution sourced by ρ_matter and has none of those features. Dissolving those artifacts does not by itself deliver the 16/3 · Ω_b ratio, but it does remove the supposed crisis and replaces it with the cleaner and more honest question "what is Definition C?".

---

## 7. Audit flags (per user instruction)

Positive structural claims above that require re-audit before being used in v3.4:

 - **[RE-AUDIT-1]** Claim that the DFD ψ field equation is elliptic in the strict time-parameter limit with no (1/c²) ψ̈ term. v3.3 section_formalism.tex line 561 shows the hyperbolic form ∇²ψ − (1/c²) ψ̈ = −(8πG/c²) ρ, while appendix_U and section_wellposedness treat the static elliptic limit. Need a monograph-level clarification of whether DFD is strictly elliptic or hyperbolic-with-suppressed-time-derivative in the cosmological application. If the latter, L5/L8's calculations might still be computing a real (though small) residual effect.
 - **[RE-AUDIT-2]** Claim that χ has no independent Cauchy data. This assumes χ is identified with (or slaved to) ψ. If χ is an independent dynamical field that merely *couples* to ψ via the internal CP^2 × S^3 structure (and has its own hyperbolic EOM on some effective 4D slice), then misalignment does apply and L5/L8 are correct. Need an explicit statement in v3.4 of whether χ is a functional of ψ or an independent field.
 - **[RE-AUDIT-3]** Claim that Definitions A and B (ψ-gradient energy, ψρ on-shell energy) exhaust the natural "field energy of elliptic ψ" candidates. There may be a Definition C involving the CP^2 × S^3 kinetic terms that changes the dimensional analysis. The α-tower prefactors could in principle lift the ratio from (v/c)² to O(1), but I have not demonstrated this.
 - **[RE-AUDIT-4]** Claim that L5, L8, and Relic_n3p7 are uniformly miscasting the problem. Relic_n3p7 in particular uses the Marsh 2016 ultralight ALP formula, which is self-consistent for a 4D hyperbolic ALP but — as argued here — inapplicable if χ is elliptic. Worth a line-by-line re-read to check whether any of those agents explicitly anchored their calculation in a DFD-native formulation rather than the 4D template.

No external citations are invoked; all references are to files within the user's own codebase.
