# M10: Post-Inflation Equipartition Attack on Ω_χ/Ω_b = 16/3

## The attack

DFD inflation is Starobinsky R² with scalaron σ. After inflation σ reheats both sectors via the gravitational portal (universal coupling, no preference). If thermal equipartition is reached at reheat temperature T_rh, then at that moment

  ρ_χ / ρ_b = g*_χ(T_rh) / g*_b(T_rh)

so the predicted late-time ratio Ω_χ/Ω_b = 16/3 ≈ 5.333 must be reproduced by a *DOF count*, not by a topological winding. If no consistent counting yields 16/3, the equipartition picture is incompatible with DFD's central prediction — and either equipartition fails (sectors decouple) or 16/3 is not the right number.

This note works the count.

## Step 1: Standard Model effective DOF count

g*(T) for relativistic species is

  g* = Σ_bosons g_i + (7/8) Σ_fermions g_i

At T ≫ m_top (full SM relativistic):
- Quarks: 6 flavors × 3 colors × 2 spin × 2 (particle+antiparticle) = 72 fermionic DOF
- Charged leptons: 3 × 2 × 2 = 12
- Neutrinos: 3 × 2 (LH only, ν+ν̄) = 6
- Gluons: 8 × 2 = 16 bosonic
- W±, Z: 3 × 3 = 9 (massive vector)
- Photon: 2
- Higgs: 1
Total bosonic = 16 + 9 + 2 + 1 = 28
Total fermionic = 72 + 12 + 6 = 90
g*_SM = 28 + (7/8)(90) = 28 + 78.75 = **106.75**

At BBN (T ~ 1 MeV, e± and ν still relativistic, photons):
- γ: 2
- e±: 4 fermionic
- ν, ν̄ × 3: 6 fermionic
g*_BBN = 2 + (7/8)(10) = 2 + 8.75 = **10.75** ✓

## Step 2: Try to engineer g*_χ / g*_b = 16/3

We need g*_χ / g*_b = 16/3 exactly. Equivalently g*_χ = (16/3) g*_b.

### Attempt A: χ sector = 1 real scalar, baryon sector ≡ "baryons only"

If χ is a single real scalar: g*_χ = 1 (cold) or 1 at temperature.
"Baryon sector" interpreted as Ω_b carriers needs DOF that ultimately become baryons. Naive baryon count = nucleons = neutrons + protons = 4 fermionic DOF (n, p × 2 spin) → (7/8)(4) = 3.5.
Ratio 1/3.5 = 0.286. Nowhere near 16/3.

### Attempt B: χ sector = scalar + 3 Goldstones (b₃ = 1 hypothesis)

χ + 3 NG bosons → g*_χ = 4 (all real scalars).
Need g*_b = 4 × 3/16 = 0.75. Impossible (must be integer-valued in 1/8 units, and ≥ 1).

### Attempt C: Reverse — χ sector larger than baryon sector

If g*_χ = 16k and g*_b = 3k for integer k:
- k=1: g*_χ=16, g*_b=3. Baryonic 3 DOF could be (7/8)(...) — but 3 is not a multiple of 7/8 with small integer numerator. 3 = (7/8)(24/7), no integer source. Nearest: 1 boson + (7/8)(2) = 2.75; 1 + (7/8)(4) = 4.5. Cannot hit 3 exactly.
- k=2: g*_χ=32, g*_b=6. g*_b=6 requires e.g. 6 bosonic DOF (3 massive vectors? 3×2=6 ✓ for 3 unbroken gauge bosons), or (7/8)(48/7)... Only the 6-boson route works. g*_χ=32 from 32 real scalars? No DFD motivation.
- k=3: g*_χ=48, g*_b=9. g*_b=9 = W+Z DOF (massive electroweak vectors). g*_χ=48 has no natural origin.

### Attempt D: Use g*_b = 10.75 (BBN value)

Then g*_χ = (16/3)(10.75) = 57.33... Not an integer in eighths. Specifically, 16×10.75/3 = 172/3 ≈ 57.33, not expressible as n_B + (7/8) n_F for non-negative integers.

### Attempt E: Use g*_b = 106.75 (full SM at reheat)

g*_χ = (16/3)(106.75) = 1708/3 ≈ 569.33. Not in eighths (3 ∤ 1708×8 in the right way: 1708/3 has no closed eighth representation).

### Attempt F: Allow temperature mismatch (T_χ ≠ T_b)

Then ρ_χ/ρ_b = (g*_χ/g*_b)(T_χ/T_b)⁴. To recover 16/3 we need 4 free parameters (g*_χ, g*_b, and a temperature ratio raised to the fourth) — the relation becomes an *adjustment*, not a *prediction*. This forfeits the equipartition argument.

## Step 3: Algebraic non-existence proof

Requirement: ∃ non-negative integers (n_B^χ, n_F^χ, n_B^b, n_F^b) with

  [n_B^χ + (7/8) n_F^χ] / [n_B^b + (7/8) n_F^b] = 16/3

Multiply: 3(8 n_B^χ + 7 n_F^χ) = 16(8 n_B^b + 7 n_F^b)
  24 n_B^χ + 21 n_F^χ = 128 n_B^b + 112 n_F^b

Reduce mod 3: 0 + 0 ≡ 2 n_B^b + 1 n_F^b (mod 3) → 2 n_B^b + n_F^b ≡ 0 (mod 3).
This *does* admit solutions (e.g., n_B^b=0, n_F^b=3: 21 n_F^χ + 24 n_B^χ = 336 → n_F^χ=16, n_B^χ=0; or n_B^χ=14, n_F^χ=0).

So algebraically the ratio 16/3 is realizable. Two minimal solutions:

**Solution 1:** χ sector = 16 fermionic DOF; b sector = 3 fermionic DOF.
  Check: (7/8)(16)/(7/8)(3) = 16/3 ✓
  But "3 fermionic DOF" is impossible for a single Dirac species (must come in 4s) or Weyl pair (2s). 3 is not realizable from physical fermions.

**Solution 2:** χ sector = 14 bosonic DOF; b sector = (7/8)(...) → from 24 n_B^b + 21 n_F^b = 24·14 = 336, with n_B^χ=14, n_F^χ=0: need 128 n_B^b + 112 n_F^b = 336 → no non-negative solution (336/112=3, so n_B^b=0, n_F^b=3, but then (7/8)·3 = 21/8 — wait, recheck: 128(0)+112(3)=336 ✓; but 3 fermionic DOF still unphysical).

**Solution 3:** Scale up. n_F^b = 6 (one Dirac), then RHS = 672. Need 24 n_B^χ + 21 n_F^χ = 672. n_F^χ=32 → 672-672=0, n_B^χ=0. Or n_B^χ=28, n_F^χ=0. So:
  - χ sector = 32 fermionic DOF (e.g., 8 Weyl fermions or 4 Dirac), b sector = 1 Dirac fermion.
  - Or χ sector = 28 bosonic DOF, b sector = 1 Dirac fermion.

Both are achievable as integers, but neither matches DFD's actual χ-sector content (1 real scalar χ, possibly + 3 Goldstones from b₃=1 → at most 4 bosonic DOF).

## Step 4: Verdict

The DFD χ sector contains, by construction:
- 1 real scalar χ (the dust field), bosonic DOF = 1
- Possibly 3 Goldstones from b₃(SU(2)) = 1, bosonic DOF = 3
- Total maximum: g*_χ = 4

The baryonic sector at reheat is the full SM: g*_b ≈ 106.75 (or 10.75 at BBN).

Equipartition prediction: ρ_χ/ρ_b ≤ 4/10.75 ≈ 0.37 (if reheat happens late) or 4/106.75 ≈ 0.037 (if early).

**Required by DFD: 16/3 ≈ 5.33.**

**Discrepancy: factor of ~14 to ~140 too small.**

No DFD-consistent DOF assignment yields 16/3 from equipartition. The integer solutions that *do* yield 16/3 (32 fermionic χ DOF; or 28 bosonic χ DOF) require a χ sector vastly larger than DFD allows.

## Step 5: Implication for DFD

Two possible readings:

**(a) Equipartition does NOT hold.** This is consistent with DFD's actual story: Ω_χ/Ω_b = 16/3 comes from the *topological winding* (b₃ = 1 path-integral count) or the conserved current J_χ (cf. J1_01, J1_02). Reheat is NOT thermal between sectors; the χ sector is populated by gravitational production of a single light scalar with an initial condition fixed by topology, not by g* counting. The scalaron decays preferentially to the SM (or only to the SM at tree level) and χ is sourced by a separate, non-thermal channel.

This is the orthodox DFD line and survives this attack.

**(b) Equipartition DOES hold and 16/3 is wrong.** Then the DFD prediction is falsified at the ~factor-14 level — Ω_χ/Ω_b would be ~0.04, not 5.33, contradicting Planck (which observationally requires Ω_dm/Ω_b ≈ 5.4). This reading is impossible because *observation* gives 5.4, so equipartition cannot be the operative mechanism regardless of which theory we use.

## Step 6: What this attack actually constrains

The attack falsifies a strawman: "16/3 from thermal counting." DFD never claimed this. The 16/3 derivations on file (H6, J1_01, J1_02, J1_03) all proceed from path-integral / topological / conserved-current arguments, not from g* ratios. The equipartition route is *ruled out by arithmetic*, which is actually a useful result: it forecloses an alternative microphysical interpretation of 16/3 that one might naively try.

**Forecloses:** "16/3 = thermal DOF ratio after universal scalaron reheat."
**Leaves intact:** topological/winding/path-integral derivations of 16/3.
**New constraint on DFD model-building:** the scalaron cannot reheat the χ sector thermally; the χ sector must be populated non-thermally (gravitational particle production into the zero mode + topological initial condition), and this non-thermal channel must be parametrically *enhanced* over the thermal one by the required factor.

## Quantitative non-thermal requirement

For Ω_χ/Ω_b = 16/3 with g*_χ ≤ 4, g*_b = 106.75:
  (ρ_χ/ρ_b)_thermal ≤ 4/106.75 = 0.0375
  (ρ_χ/ρ_b)_required = 5.333
  Enhancement factor needed: 5.333 / 0.0375 ≈ **142**

The non-thermal production of χ must dominate the thermal channel by ~2 orders of magnitude. This is quantitatively consistent with cold gravitational production of a light scalar during inflation (where the inflaton energy density dumps mostly into the SM but leaves a coherent χ background fixed by horizon-crossing amplitude), but it requires verification within DFD that the χ initial amplitude χ_0 ~ H_inf gives the right relic.

## Conclusion

| Question | Answer |
|---|---|
| Does any DFD-consistent g* count give 16/3? | **No.** |
| Does any integer DOF count give 16/3? | Yes (e.g., 32_F vs 6_F), but not with DFD's χ content. |
| Does this falsify DFD's 16/3? | **No** — it falsifies the equipartition interpretation, which DFD never adopted. |
| What does it require of DFD? | The χ sector must be populated *non-thermally* with an enhancement of ~142 over the thermal channel. |
| Is that consistent with gravitational production of a light scalar? | Plausibly yes; needs explicit verification of χ_0 ~ H_inf relic calculation. |

**Attack status: deflected.** Equipartition is not the DFD mechanism. The arithmetic non-existence of a DFD-consistent thermal count is a *feature* — it confirms that 16/3 cannot be reverse-engineered from g* ratios and must come from the topological/path-integral route already on file.

## Cross-references
- H6_16_over_3_path_integral.md — path-integral derivation
- H9_counting_vs_production.md — counting vs production distinction
- J1_01_16_over_3_conserved_current.md — conserved current
- J1_02_16_over_3_path_integral_direct.md — direct path integral
- J1_03_16_over_3_initial_condition.md — initial condition
- L9_so10_branching.md — sector branching after GUT breaking
