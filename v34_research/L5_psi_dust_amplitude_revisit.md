# L5: ψ-Dust Branch Amplitude Revisit

**Agent:** L5
**Date:** 2026-04-06
**Task:** Revisit the ψ-dust condensate amplitude question, testing K1-7's late-partition loophole and exploring whether any production mechanism naturally yields ρ_χ/ρ_b = 16/3 at the χ turn-on.

**Prior verdict (H6, H9, J1-2, K1-5, K1-7):** Temporal dust branch amplitude is ~10⁻¹⁹ or ~5×10⁻⁴, **not** 16/3 × Ω_b ≈ 0.26.

---

## 1. When does χ start oscillating?

χ is frozen by Hubble friction while H > m_χ/3 and begins coherent oscillation at

  H(T_osc) ≈ m_χ/3 ,   with   H(T) ≈ 1.66 √g_eff · T²/M_P .

Solving for T_osc with m_χ = 96 keV, g_eff ~ 60:

  T_osc² ≈ (m_χ/3) · M_P / (1.66 √g_eff)
  T_osc ≈ √(m_χ M_P / (5 √g_eff))
  T_osc ≈ √(9.6×10⁴ eV · 2.4×10²⁸ eV / 40)
  T_osc ≈ √(5.8×10³¹ eV²)
  **T_osc ≈ 2.4×10⁸ eV ≈ 240 MeV** (near QCD crossover)

Between T_osc (240 MeV) and T ≈ m_χ (96 keV), **χ redshifts as matter**: ρ_χ ∝ a⁻³. Baryons are already matter-like (rest-mass dominated) over this range as well. So the ratio ρ_χ/ρ_b is frozen once set at T_osc.

**This means the K1-7 loophole — "partition happens when both sectors are matter-like" — is satisfied, provided we set the ratio at T_osc ≈ 240 MeV, not at T ≈ 96 keV.** The redshift dilution argument that killed earlier attempts (for high-T partition) does not apply here. The question reduces to: **does any physical mechanism produce ρ_χ(T_osc)/ρ_b(T_osc) = 16/3?**

---

## 2. Initial condensate energy density (misalignment)

Standard misalignment:

  ρ_χ(T_osc) = ½ m_χ² χ₀² ,   χ₀ = f_a θ_i .

With the current v3.4 assignment f_a = M̄_P α⁵ ≈ 5×10⁷ GeV = 5×10¹⁶ eV, m_χ = 96 keV = 9.6×10⁴ eV, θ_i ~ 1:

  ρ_χ(T_osc) = ½ (9.6×10⁴)² (5×10¹⁶)² eV⁴
  ≈ ½ · 9.2×10⁹ · 2.5×10³³ eV⁴
  ≈ **1.2×10⁴³ eV⁴**

Baryon density at T_osc = 240 MeV. Using ρ_b(T) = Ω_b · (T/T_0)³ · ρ_crit,0 (since baryons are already matter):

  ρ_crit,0 ≈ 8×10⁻¹¹ eV⁴
  (T_osc/T_0)³ = (2.4×10⁸ / 2.35×10⁻⁴)³ = (1.02×10¹²)³ ≈ 1.06×10³⁶
  ρ_b(T_osc) ≈ 0.05 · 8×10⁻¹¹ · 1.06×10³⁶
  ≈ **4.2×10²⁴ eV⁴**

**Ratio:** ρ_χ(T_osc)/ρ_b(T_osc) ≈ 1.2×10⁴³ / 4.2×10²⁴ ≈ **3×10¹⁸** — catastrophically **too large** by 18 orders of magnitude.

This is a real signal: the α-tower rung f_a = α⁵ M̄_P overshoots the DM abundance by 18 orders of magnitude if θ_i ~ 1. This recapitulates the standard overclosure problem for axion-like particles with f_a ≫ 10¹² GeV: the misalignment abundance scales as f_a² m_χ^(1/2) and explodes for large f_a. The prior agents' "10⁻¹⁹" number was computing ρ_χ/ρ_crit,0 at **today**, apparently with a dilution/suppression factor they interpreted as killing the 16/3 prediction. In fact the raw misalignment integral is 18 orders too **large**, not too small — meaning the α-tower rung and standard misalignment are incompatible no matter which direction one pushes. (This also explains why requiring θ_i to match gives θ_i ~ 8×10⁴, as computed in the task prompt — physically impossible.)

**Verdict on standard misalignment: FAIL in both directions.** f_a = α⁵ M̄_P is wrong for misalignment DM with m_χ = 96 keV.

---

## 3. Alternative f_a: the M_R rung

Setting ρ_χ(T_osc)/ρ_b(T_osc) = 16/3 ≈ 5.33 and solving for f_a with θ_i = 1:

  f_a² = (16/3) · 2 · ρ_b(T_osc) / m_χ²
  f_a² ≈ 10.67 · 4.2×10²⁴ / 9.2×10⁹ eV²
  f_a² ≈ 4.9×10¹⁵ eV²
  **f_a ≈ 7×10⁷ eV ≈ 70 MeV**

This is **nothing like M_R = M_P α³ ≈ 4.7×10¹² GeV**. The task prompt's arithmetic (which landed on f_a ≈ 4×10¹² GeV) used ρ_b ≈ 5×10³³ eV⁴, which corresponds to **ρ_crit(T_osc) ≈ M_P² H²**, not ρ_b. The factor Ω_b ≈ 0.05 **and** the fact that baryons track T³ (not T⁴) between T_osc and today both matter.

Re-doing the prompt's own check with the correct ρ_b: f_a = M_R gives

  ρ_χ(T_osc) / ρ_b(T_osc) ≈ ½ (9.6×10⁴)² (4.7×10²¹)² / 4.2×10²⁴
  ≈ ½ · 9.2×10⁹ · 2.2×10⁴³ / 4.2×10²⁴
  ≈ **2.4×10²⁸**

Also overshoots by 28 orders of magnitude. f_a = M_R is **worse**, not better.

Going the other way: f_a ≈ 70 MeV is far below every α-rung in the tower (α⁹ M̄_P ≈ 10⁻³ GeV, α¹⁰ M̄_P ≈ 10⁻⁵ GeV). No natural rung sits at 70 MeV. The rung nearest 70 MeV is α⁸ M̄_P ≈ 140 MeV (order-of-magnitude). If f_a = α⁸ M̄_P were used, m_χ = √158 · Λ²/f_a would change as well, and the whole tower relabels.

**Verdict on rung-swap: no self-consistent α-tower assignment reproduces 16/3 via misalignment.**

---

## 4. Alternative production mechanisms

### 4a. Gravitational production / scalaron decay

Starobinsky inflation ends with scalaron (R² field) decaying. The gravitational production channel for a scalar χ of mass m_χ gives

  n_χ/s ~ (m_χ/M_P)² · (T_rh/m_χ) · (dimensionless coupling)

For m_χ = 96 keV, T_rh ≈ 10¹³ GeV:

  n_χ/s ~ (10⁻²⁴)² · (10²²/1) ~ 10⁻²⁶ (per unit coupling)
  ρ_χ/s = m_χ · n_χ/s ≈ 10⁻⁵·10⁻²⁶ = 10⁻³¹ GeV

Compare ρ_b/s ≈ m_p · η_b ≈ 1 GeV · 6×10⁻¹⁰ ≈ 6×10⁻¹⁰ GeV. Ratio:

  ρ_χ/ρ_b ~ 10⁻³¹ / 6×10⁻¹⁰ ~ **2×10⁻²²**

Too small by 21 orders of magnitude. **FAIL.**

### 4b. Direct inflaton → χ coupling

If the inflaton dumps a fraction ε of its energy into χ during reheating, then

  ρ_χ(T_rh) = ε · ρ_inf , ρ_b eventually comes from the (1−ε) part via leptogenesis with efficiency η ~ 10⁻⁹.

Setting ρ_χ/ρ_b = 16/3 at matter-radiation handoff:

  ρ_χ/ρ_b = ε · (m_χ/T_rh) / [η_b · (m_p/T_rh)]    [tracking matter vs radiation]

This gives a *tuning* relationship between ε, η_b, m_χ/m_p. Plugging numbers:

  16/3 = ε · (10⁻⁵/10¹³) / [6×10⁻¹⁰ · (1/10¹³)]
  16/3 = ε · 10⁻¹⁸ / 6×10⁻²³
  16/3 = ε · 1.7×10⁴
  **ε ≈ 3×10⁻⁴**

A 0.03% branching of the inflaton into χ would reproduce the ratio. But this is a **tunable input parameter**, not a theorem. The H6 path-integral derivation claimed 16/3 is dictated by the Majorana counting (16 spinor DOF / 3 sterile-neutrino pieces), which has no relationship to ε. Matching this to an inflaton branching ratio would be numerological.

### 4c. Topological / Chern-Simons vacuum energy

The DFD v3.4 framework assigns a ψ-sector topological susceptibility χ_top = Λ⁴ with Λ = α⁸ M̄_P ≈ 18 GeV. The induced condensate energy from CS vacua is

  ρ_top ≈ χ_top = Λ⁴ ≈ (18 GeV)⁴ ≈ 10⁵ GeV⁴ ≈ 10⁴⁷ eV⁴

At T_osc ≈ 240 MeV this has been redshifted as matter (a⁻³) from a₀ ≈ (Λ/T_osc)⁻¹ ≈ 10⁻² (i.e. χ_top set at T ≈ Λ, dilution factor (Λ/T_osc)³ ≈ 10⁵):

  ρ_top(T_osc) ≈ 10⁴⁷ / 10⁵ ≈ 10⁴² eV⁴

Compare to ρ_b(T_osc) ≈ 4×10²⁴ eV⁴ → ratio ~ 10¹⁸. Still 18 orders too large — same disease as misalignment because ρ_top scales as Λ⁴ = f_a⁴·(m_χ/f_a)² with the same f_a overshoot.

### 4d. "Counting-only" normalization (H9's original claim)

H9's claim was that 16/3 is not an energy-density ratio at all, but a **counting ratio** of degrees of freedom (sterile Majorana spinor components vs baryon number carriers). Under this reading, 16/3 · Ω_b does not set ρ_χ today; it sets a **DOF-weighted occupation** ratio, which only becomes an energy ratio if both sectors have the same per-DOF thermal energy. Since χ is a cold condensate (not thermal) and baryons are non-relativistic rest-mass, the per-DOF energies differ by many orders of magnitude and the "16/3" loses its physical interpretation as a density ratio.

**This was the consensus J1–J2 / K1–K7 conclusion, and this L5 pass confirms it:** every production mechanism that produces the right *order of magnitude* for χ cold dark matter (Ω_χ h² ≈ 0.12) fails to produce 16/3 · Ω_b as a theorem. Every mechanism that contains a parameter knob can be *tuned* to 16/3, but none derives it.

---

## 5. The K1-7 loophole: does it survive?

K1-7 proposed: "If the condensate partition happens at T ≈ m_χ, both sectors are already matter-like and 16/3 survives dilution."

Two problems:

1. **χ actually starts oscillating at T_osc ≈ 240 MeV, not T ≈ 96 keV.** So the partition — if we mean "the moment ρ_χ is set" — happens at 240 MeV, not at the χ mass. The loophole's premise (partition at T ≈ m_χ) is false for standard misalignment.

2. **Even granting the loophole's premise, no production mechanism lands on 16/3.** Sections 2–4 show every candidate misses by 18+ orders of magnitude without tuning. Matter-era partition protects the ratio *once it is set*, but doesn't *create* the value 16/3.

**The K1-7 loophole does not resurrect 16/3 · Ω_b as a ψ-dust amplitude prediction.** The numerical consensus of H6/H9/J1-J2/K1-5/K1-7 stands.

---

## 6. The 18-orders-of-magnitude overshoot deserves attention

One genuinely new observation from this pass: with f_a = α⁵ M̄_P and θ_i = 1, the **raw misalignment abundance of χ overshoots Ω_DM by ~10¹⁸**, not undershoots. Prior agents reporting "10⁻¹⁹" were, I believe, computing something else (possibly ρ_χ(t_0)/ρ_crit,0 with a suppression factor, or applying a Z₂ sector volume suppression).

This has two implications:

- **If χ is to be CDM at all**, the α-tower rung for f_a must be lower (toward α⁸–α⁹ M̄_P ≈ GeV–MeV) OR θ_i must be extremely small (< 10⁻⁹), OR m_χ must be much smaller, OR a late-time entropy dilution by factor ~10¹⁸ must be invoked. None of these are in the current v3.4 paper.

- **This is a harder problem than the 16/3 amplitude question.** Before worrying about whether the dust branch amplitude is 16/3 or 5×10⁻⁴, v3.4 needs to address why misalignment with the stated f_a and m_χ does not overclose the universe by 18 orders.

I flag this as **the most important finding of this revisit**. The 16/3 question is a distraction compared to the overclosure problem lurking in the same calculation.

---

## 7. Final verdict

1. **K1-7's loophole is invalid.** χ oscillation turns on at T_osc ≈ 240 MeV, not T ≈ m_χ, so the "late partition while both sectors are matter-like" premise fails.
2. **No production mechanism** (misalignment with any rung, gravitational production, inflaton branching, CS topology) naturally yields ρ_χ/ρ_b = 16/3. Inflaton branching can be *tuned* to it (ε ≈ 3×10⁻⁴) but that is parameter-fitting, not a theorem.
3. **The prior consensus stands:** ψ-dust branch amplitude is NOT 16/3 · Ω_b. Treat 16/3 as a DOF-counting ratio without energy-density interpretation.
4. **NEW — critical finding:** with v3.4's stated f_a = α⁵ M̄_P and m_χ = 96 keV, standard misalignment overshoots Ω_DM by ~10¹⁸. This is an overclosure crisis that should be addressed before the 16/3 question is revisited again.

**Recommendation for v3.4 paper revision:** remove any claim that the dust branch amplitude is 16/3 · Ω_b; address the overclosure gap via one of (a) different f_a rung assignment, (b) non-misalignment production, or (c) late-time dilution mechanism. The current text is internally inconsistent.
