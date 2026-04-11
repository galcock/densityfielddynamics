# L8: Independent χ Condensate Energy at Turn-On — K1-7 Loophole Test

**Task.** Determine whether ρ_χ(T ≈ m_χ) = (16/19) ρ_matter(T) follows from an *independent* DFD calculation, or whether K1-7's partition argument requires a fine-tuned input.

Equivalently: is ρ_χ / ρ_baryon = 16/3 at T = 96 keV a prediction, or a tuning?

---

## 1. Misalignment calculation (standard axion-like)

**Oscillation onset.** χ begins coherent oscillation when 3H(T_osc) ≈ m_χ:

  H(T_osc) ≈ m_χ/3 = 32 keV

In radiation domination, H ≈ T² / M_P (with M_P ≈ 2.4×10¹⁸ GeV = 2.4×10²⁷ eV reduced). Solving:

  T_osc² ≈ m_χ M_P / 3 ≈ (32×10³ eV)(2.4×10²⁷ eV) ≈ 7.7×10³¹ eV²
  T_osc ≈ 8.8×10¹⁵ eV ≈ 8.8 PeV

(Using non-reduced M_Pl ≈ 1.2×10¹⁹ GeV gives T_osc ≈ 2×10¹⁶ eV ≈ 20 PeV. Take T_osc ≈ 10¹⁶ eV.)

So χ has been redshifting as matter (ρ ∝ a⁻³ ∝ T³, modulo g*) from T ≈ 10¹⁶ eV down to 96 keV — a factor ≈ 10¹¹ in temperature, i.e. ≈ 10³³ in energy density.

**Initial energy density.**
  ρ_χ(T_osc) = (1/2) m_χ² χ₀²,   χ₀ = f_a θ_i

**Redshift to T = 96 keV.**
  ρ_χ(96 keV) = ρ_χ(T_osc) × (96 keV / T_osc)³ ≈ ρ_χ(T_osc) × (10⁻¹¹)³ = 10⁻³³ ρ_χ(T_osc)

## 2. Matter budget at T = 96 keV

Baryon-to-photon ratio η_b ≈ 6×10⁻¹⁰, n_γ ≈ 0.24 T³, so n_b ≈ 1.4×10⁻¹⁰ T³. With m_b ≈ 0.94 GeV:

  ρ_b(96 keV) ≈ 1.4×10⁻¹⁰ × (96×10³)⁴ × (0.94×10⁹)/(96×10³) eV⁴
             ≈ 1.4×10⁻¹⁰ × 8.5×10¹⁹ × 9.8×10³ eV⁴
             ≈ 1.2×10¹⁴ eV⁴

(Cross-check: ρ_γ ≈ (π²/15) T⁴ ≈ 5.6×10¹⁹ eV⁴; ρ_b/ρ_γ ≈ 2×10⁻⁶, consistent with matter-radiation equality at T ≈ 1 eV.)

**Target.** ρ_χ(96 keV) = (16/3) ρ_b(96 keV) ≈ 6.4×10¹⁴ eV⁴.

## 3. Required misalignment amplitude

Invert:
  ρ_χ(T_osc) = 6.4×10¹⁴ × 10³³ eV⁴ = 6.4×10⁴⁷ eV⁴
  χ₀² = 2 ρ_χ(T_osc)/m_χ² = 2 × 6.4×10⁴⁷ / (96×10³)² ≈ 1.4×10³⁸ eV²
  χ₀ ≈ 1.2×10¹⁹ eV ≈ 12 GeV

With the α-tower f_a = α⁵ M̄_P ≈ 5×10⁷ GeV:
  **θ_i = χ₀/f_a ≈ 2.4×10⁻⁷**

(The briefing's 0.6 GeV / 10⁻⁸ used T_osc ≈ 1.7 TeV from H = T²/M_P with reduced M_P but without the factor of 3; the corrected value is slightly larger but the qualitative picture is identical: θ_i ≪ 1 with no DFD origin.)

## 4. Natural-origin check for θ_i ≈ 10⁻⁷

**(a) Inflationary quantum fluctuations.** δχ ~ H_inf/(2π), so δθ_i ~ H_inf/(2π f_a). For H_inf ≲ 10¹³ GeV and f_a ≈ 5×10⁷ GeV, δθ_i ≳ 3×10⁴ — catastrophically larger than 10⁻⁷. Fluctuations *overshoot* by 11 orders of magnitude and homogenise θ_i to an O(1) random draw on each Hubble patch.

**(b) Anthropic / stochastic selection.** Would require P(θ_i < 10⁻⁷) ~ 10⁻⁷ suppression — not a prediction.

**(c) Topological CS-index quantisation.** θ_i = 2π(k_max − n)/(k_max + 2). Nearest rational to 10⁻⁷ at k_max ~ 62 requires (k_max − n) ~ 10⁻⁶, i.e. non-integer: no lattice point lands there.

**Verdict on misalignment.** There is no DFD mechanism that independently fixes θ_i to the value required. The 16/3 ratio is *not* a prediction of the misalignment channel — it is a one-parameter fit.

## 5. Scaling check — can a different (m_χ, f_a) save it?

ρ_χ(T_osc) ∝ m_χ² f_a² θ_i², and the dilution factor (T_BBN/T_osc)³ ∝ m_χ⁻³/² (radiation era), so

  ρ_χ(96 keV) ∝ m_χ^(1/2) f_a² θ_i²

Fixing the target (6.4×10¹⁴ eV⁴) and f_a = 5×10⁷ GeV:
  m_χ^(1/2) θ_i² ≈ 6×10²³ eV^(1/2)

- θ_i = 1 → m_χ ≈ 4×10⁸ eV ≈ 400 MeV (4000× too heavy; off-tower)
- θ_i = 0.1 → m_χ ≈ 40 GeV (off-tower)
- m_χ = 96 keV (α-tower) → θ_i ≈ 2×10⁻⁷ (tuned)

The α-tower rung m_χ = 96 keV and the matter-budget target are *numerically incompatible* unless θ_i is tuned.

## 6. Alternative production channels

### (a) Gravitational preheating from scalaron decay
Scalaron mass in DFD ≈ M_s ~ 10¹³ GeV (f(R) inflation rung). Branching ratio to χ of O(1) would give ρ_χ ~ ρ_inf ~ (10¹⁶ GeV)⁴ at reheating, then redshift as matter (once m_χ dominates) or radiation (before). If χ is relativistic until T ~ 96 keV, χ is *dark radiation*, not matter, and the partition fails by equation-of-state mismatch. If it becomes non-relativistic earlier (T ~ m_χ ~ 10⁵ eV), ρ_χ/ρ_rad is set by g*_χ/g*_SM ~ 1/106.75, not 16/19. **Does not independently give 16/19.**

### (b) Direct CP² Kähler potential
A non-minimal Kähler term K ⊃ |χ|² R/M_P² sources ρ_χ ~ H² M_P² at horizon crossing, giving Ω_χ ~ (H_inf/M_P)² × const. This is generically O(10⁻¹⁰) for GUT-scale inflation — too small by 4 orders for the target, and parametrically independent of the 16/3 DOF ratio.

### (c) Kinetic-term quantum corrections
One-loop Spin(10) corrections to Z_χ shift the canonically-normalised amplitude by O(α ln(Λ/μ)) ~ few percent. Cannot generate the O(10⁷) enhancement needed to reach the target from a natural θ_i ~ 1, and anyway does not carry a 16/3 factor.

### (d) Thermal production via χ-ψ coupling
If χ thermalises and decouples relativistically, ρ_χ(T)/ρ_SM(T) = g*_χ/g*_SM = 2/106.75 ≈ 0.019. After χ becomes non-relativistic, this ratio grows by m_χ/T, reaching 16/19 ≈ 0.84 when T = m_χ × (16/19)/0.019 ≈ 44 m_χ — i.e. roughly T ≈ 4 MeV for m_χ = 96 keV. But at 4 MeV, χ is still relativistic (T ≫ m_χ), so the calculation is self-inconsistent. The "16/19 at T ≈ m_χ" coincidence does *not* emerge from thermal relic kinematics.

### (e) Common-condensate DOF partition (K1-7's own proposal)
K1-7 assumes a *shared* scalar reservoir that fractionates 16 (Spin(10) adjoint-ish) : 3 (color) at turn-on. The DOF count does give 16/19 : 3/19 by construction — but the *total* reservoir energy ρ_total(96 keV) must still be set by an independent calculation, and the same misalignment problem applies to ρ_total: one needs χ₀_total tuned to match the measured ρ_b. The DOF partition is mathematically automatic; the overall normalisation to Ω_b is not.

## 7. Verdict

**The 16/19 loophole does not close.** No DFD mechanism surveyed independently fixes ρ_χ(96 keV) = (16/19) ρ_matter(96 keV):

| Channel | Scale of ρ_χ(96 keV) | Carries 16/19 factor? | Matches target? |
|---|---|---|---|
| Misalignment (α-tower f_a, m_χ) | requires θ_i ≈ 2×10⁻⁷ | No | Only if tuned |
| Scalaron gravitational preheat | g*-weighted, O(1/107) | No | No (wrong order + wrong EoS) |
| Kähler/curvature coupling | (H_inf/M_P)² × const | No | No (~10⁴ too small) |
| Kinetic-term quantum corr. | O(α) shift | No | No (perturbative only) |
| Thermal relic | g*/g*_SM | No | No (kinematically inconsistent) |
| K1-7 DOF partition | (inherits total ρ) | Yes (by construction) | Only if total is tuned |

**Conclusion for K1-7's loophole.** The "16 vs 3" partition is a valid *bookkeeping identity* if one posits a common reservoir of the right total magnitude, but that total magnitude is **not** independently predicted by DFD: whichever production channel one picks (misalignment, gravitational, Kähler, thermal), the amplitude lands far from the baryon budget without a tuned initial condition. The α-tower rung m_χ ≈ 96 keV does *not* in itself fix ρ_χ at BBN; an additional input (θ_i, reheat temperature, or Kähler coefficient) must be supplied, and once supplied it is no longer a prediction.

**Recommendation.** K1-7 should be treated as an internal-consistency check, not a first-principles derivation. The 16/19 ratio is compatible with the data only through a one-parameter fit (effectively θ_i ≈ 2×10⁻⁷ or equivalent Kähler tuning). Any v3.4 writeup should either (i) acknowledge this as a tuning, (ii) supply a topological quantisation that lands exactly on θ_i ≈ 2×10⁻⁷ (none found), or (iii) identify a new DFD-specific channel whose natural scale is ρ_b at BBN (none identified in this audit).

---

**Numerical cross-checks used**
- M_P (reduced) = 2.4×10²⁷ eV; M_Pl = 1.22×10²⁸ eV.
- H(T) = T²/M_P in RD; T_osc ≈ √(m_χ M_P/3) ≈ 8.8×10¹⁵ eV for m_χ = 96 keV.
- ρ_b(T) = η_b n_γ(T) m_b with n_γ ≈ 0.24 T³.
- Dilution (T_BBN/T_osc)³ with constant g*_s gives ≈ 10⁻³³ (g*_s ratio corrections < factor 2).
- f_a = α⁵ M̄_P ≈ 5×10⁷ GeV (α-tower rung).

**Margin on θ_i requirement:** 2×10⁻⁷ (this calc) vs 10⁻⁸ (briefing) — a factor ≈ 20 from the T_osc/H(T) convention. Either way, θ_i ≪ 1 by 7–8 orders of magnitude, and the conclusion (no natural origin) is unchanged.
