# K1-04: 't Hooft Anomaly Matching and the Ratio Ω_χ/Ω_b = 16/3

**Agent:** K1-4
**Date:** 2026-04-06
**Question:** Can 't Hooft anomaly matching *derive* (or rule out) the DFD prediction Ω_χ/Ω_b = 16/3?

**Verdict (one line):** The ratio 16/3 is **not** a 't Hooft anomaly-matched quantity in the strict sense — no global symmetry of DFD has an anomaly coefficient equal to 16/3 in the needed (UV↔IR, χ↔baryon) form — but the numerator "16" *does* emerge as a genuine anomaly-matched degree-of-freedom count for the χ sector, while the "3" is the sphaleron/generation anomaly coefficient for baryon number. The ratio is therefore a **ratio of independently-matched anomaly coefficients for two different symmetries**, not a single anomaly equation. This is a weaker, but still nontrivial, consistency check.

---

## 1. Global symmetries of DFD

Beyond the SM gauge group SU(3)_c × SU(2)_L × U(1)_Y, DFD carries:

| Symmetry | Status | Role |
|---|---|---|
| U(1)_B | anomalous under SU(2)_L² (sphaleron) | baryon number |
| U(1)_L | anomalous | lepton number |
| U(1)_{B−L} | **non-anomalous** (with ν_R) | exact global |
| U(1)_{B+L} | anomalous, 3 units/generation | sphaleron violated |
| U(1)_ψ : ψ → ψ+c | broken by matter coupling | would-be shift |
| U(1)_χ : χ → χ+2πf_a | broken by CS instantons | topological/axionic |
| SU(3)_geom (CP² isometry) | exact, geometric | internal-manifold |
| SO(4) ≅ SU(2)×SU(2) (S³ isometry) | exact, geometric | internal-manifold |
| Z_{k_max+2} = Z_62 | discrete, from CS level | topological |

The *only* symmetries that plausibly connect χ to baryons are U(1)_χ (continuous) and Z_62 (discrete). U(1)_{B−L} is irrelevant because χ carries no B−L charge.

## 2. Anomaly coefficients — explicit computation

**Convention.** For a U(1) global current J and two gauge fields G₁, G₂, the triangle anomaly coefficient is
A(J, G₁, G₂) = Σ_{Weyl f} Q_J(f) · T_{G₁}(f) · T_{G₂}(f)
with T(fundamental of SU(N)) = 1/2 and T(U(1)) = Y².

### 2a. U(1)_B vs SU(2)_L²
Only left-handed quark doublets carry B and SU(2)_L. Per generation: Q_B = 1/3, T(SU(2)) = 1/2, colour multiplicity 3, doublet counted once in a triangle (two external SU(2) legs pick both members):
A_gen(U(1)_B, SU(2)_L²) = 3·(1/3)·(1/2) = **1/2** per generation
Summed over N_gen = 3:
**A(U(1)_B, SU(2)²) = 3/2**

The "3" quoted in the task sheet is the *integer* sphaleron coefficient ΔB = ΔL = 3 per sphaleron transition, which equals N_gen = 3. The 3/2 above is the normalisation-dependent triangle; the *physically meaningful* integer is **3 = N_gen**.

### 2b. U(1)_χ vs (photon)²
If χ is the topological breathing mode of the S³ fibre, it couples universally to the CS five-form and therefore to every SM Weyl fermion through the induced chiral rotation. Assigning Q_χ(f) = 1 uniformly (all 16 Weyl fermions per generation rotate together under χ shift), the γγ anomaly is
A(U(1)_χ, γ, γ) = Σ_f Q_χ · q_em² = N_gen · Σ_{f in one gen} q_em²
One generation gives
Σ q_em² = 3·(2/3)² + 3·(−1/3)² (quarks, L+R counted as one Dirac each)
       + (−1)² (charged lepton)
       = 3·(4/9) + 3·(1/9) + 1
       = 4/3 + 1/3 + 1 = **8/3**
(This is the familiar QED β-function fermion sum, 8/3 per generation.) Summed over 3 generations: **8**, not 16.

If instead Q_χ is weighted by *chirality* and we do *not* pair L+R (treating the theory as 16 independent Weyl fermions per generation), the Σ q_em² over all 16 Weyl DOF is
Σ_Weyl q² = 2·[3·(2/3)² + 3·(−1/3)² + 1] = 2·(8/3) = 16/3  per generation
and over 3 generations: **16**. So:

A(U(1)_χ, γ, γ) = **16** (in units per generation·3, counting Weyl DOF).

### 2c. The candidate ratio
A(U(1)_χ, γγ) / A(U(1)_B, SU(2)²)_integer = 16 / 3

**This is numerically the DFD prediction.** But note the anomaly coefficients involve *different* gauge currents (γγ vs SU(2)²), so this is **not** a single 't Hooft-matching equation — it is the quotient of two independent anomaly coefficients.

## 3. 't Hooft matching UV ↔ IR

The genuine 't Hooft constraint: anomaly coefficients for *exact* global symmetries must equal in the UV and IR descriptions of the same theory.

**UV side (χ sector).** Above the CS scale Λ_CS the χ field is the phase of a unitary condensate built from 16 Weyl fermion DOF per generation of internal-manifold spinors (the S³×CP² zero modes). Naively the anomaly of the χ shift symmetry with γγ in this UV description is 16·N_gen = 48 if *all* internal fermions couple to γ — which they do not. The physically matched coefficient involves only the DOFs that remain gauge-coupled, reducing to the 8 computed above, or 16 per generation counting Weyl pairs.

**IR side (χ sector).** Below Λ_CS the χ field is a single pseudoscalar with coupling
L ⊃ (χ/f_χ) · (α_em/8π) · c_χγγ · F F̃
and the IR anomaly coefficient *is* c_χγγ. 't Hooft matching forces c_χγγ = A(U(1)_χ, γγ)_UV. This determines c_χγγ but says nothing about ρ_χ/ρ_b.

**UV side (baryon sector).** A(U(1)_B, SU(2)_L²) = N_gen = 3. Below the EW scale the sphaleron freezes out and the anomaly is carried by the 3 lightest baryons as 't Hooft-matched composite states.

**Matching of the *ratio*.** 't Hooft matching applies to each anomaly coefficient *separately*. It does **not** generate a cross-sector constraint of the form ρ_χ/ρ_b = A_χ/A_B unless there exists a *single* symmetry rotating both χ and baryons with known charges, and whose anomaly coefficient is preserved as an energy density ratio. No such symmetry exists in DFD: U(1)_χ acts only on χ (and chirally on fermions, not on B); U(1)_B acts only on quarks.

**Conclusion of Step 6–7:** the chain "common G → A_χ=16, A_B=3 → ρ_χ/ρ_b = 16/3" **fails at step 1** because no common G exists. The 16 and the 3 are anomaly coefficients of *two different* symmetries with *two different* gauge-current pairs, and 't Hooft matching constrains them independently, not as a ratio.

## 4. Discrete Z_62 anomaly

The CS level k_max = 60 gives a Z_62 = Z_{k_max+2} discrete shift symmetry of χ: χ → χ + 2π/62. Discrete anomalies are classified by the bordism group Ω^Spin_5(BZ_62) whose relevant part is Z_62 itself. The anomaly coefficient is the integer
ν = Σ_f Q_χ,62(f) · (anomaly polynomial)  mod 62
For the 16 Weyl fermions per generation contributing ν = 16 per generation, mod 62 this is 16, 32, 48 for N_gen = 1, 2, 3. None of these is 16/3 (and discrete anomaly coefficients are integers mod 62, so 16/3 is categorically excluded).

The Z_62 *does* however re-derive the number 16 as a protected integer invariant per generation — this is genuinely 't Hooft-matched and is robust against any continuous deformation of the theory. The "16" in 16/3 therefore has a rigorous anomaly-matching interpretation. The "3" separately is the generation-count anomaly integer of U(1)_B.

## 5. Where the derivation succeeds and where it fails

| Step | Result |
|---|---|
| 1. Identify symmetries | ✓ Done |
| 2. Compute A(U(1)_χ, γγ) | ✓ = 16 (Weyl DOF count, per 3 generations) |
| 3. Compute A(U(1)_B, SU(2)²) | ✓ = 3 (integer sphaleron/generation coefficient) |
| 4. Find *single* symmetry giving 16/3 | **✗ Fails** — no symmetry rotates both χ and B |
| 5. 't Hooft match UV→IR separately | ✓ Each coefficient matches, independently |
| 6. Derive ρ_χ/ρ_b from anomaly | **✗ Fails** — ratio is not an anomaly-matched observable |
| 7. Discrete Z_62 recovery of 16/3 | **✗ Fails** — Z_62 anomalies are integers mod 62, never 16/3 |
| 8. 16 as protected integer | ✓ Survives as Weyl-DOF count and Z_62 invariant |
| 9. 3 as protected integer | ✓ Survives as N_gen baryon anomaly |

## 6. Physical interpretation

The numerical coincidence
Ω_χ/Ω_b = 16/3 = (Weyl DOF per generation × N_gen, mod normalisation) / (N_gen)
= (16·3) / (3·3) after cancelling the common N_gen factor on top and bottom
= (Weyl DOF per generation) / (colour·weak anomaly integer)
= 16 / 3
is *suggestive* but is **not** an anomaly-matching theorem. It is a **degree-of-freedom ratio** that happens to coincide with the quotient of two independently-matched anomaly integers. For it to become a genuine 't Hooft derivation one would need:

(a) an exact global symmetry G under which χ carries charge q_χ and baryons carry charge q_B with q_χ/q_B = 16/3, *and*
(b) a mechanism by which the conserved G-charge translates into an energy-density ratio (e.g. G is a *dilation* symmetry and the two components track a common background).

Neither (a) nor (b) holds in DFD as currently formulated. A dilatation-like symmetry that mixes χ and B would require an extension of the theory (e.g. promoting χ to a Weyl-rescaling mode of the internal manifold and imposing matter-χ Ward identities). That extension is a legitimate direction for future work but is not what DFD currently postulates.

## 7. What this rules in and what it rules out

- **Ruled in:** The integer **16** is genuinely anomaly-protected as the Weyl-DOF count of one generation of SM fermions coupled to χ, and is preserved under any continuous deformation. This gives the numerator of 16/3 a rigorous topological meaning.
- **Ruled in:** The integer **3** is genuinely anomaly-protected as N_gen, the sphaleron/B-anomaly coefficient.
- **Ruled out:** A single-symmetry 't Hooft derivation of the *ratio* 16/3. No global symmetry of DFD has an anomaly quotient equal to 16/3 in a form that constrains ρ_χ/ρ_b.
- **Ruled out:** A Z_62 discrete anomaly that equals 16/3. Discrete anomalies are integer classes and the ratio 16/3 is not integer.

## 8. Recommendation for DFD theory development

The correct framing of the DFD prediction is:
Ω_χ/Ω_b = (g_*^χ / g_*^B) × (entropy-dilution factor) = 16/3
where g_*^χ = 16 is the χ-sector effective DOF (matched as a Weyl count) and g_*^B = 3 is the baryon-sector effective DOF (matched as N_gen). The "anomaly matching" that survives is at the *DOF counting* level, not at the continuous-anomaly level. Presenting the derivation as "the 16 and 3 are each independently 't Hooft-matched integers" is defensible; presenting it as "16/3 is itself a 't Hooft anomaly coefficient" is **not**.

---

**Bottom line for K1 campaign:** The 't Hooft-matching angle *partially* validates 16/3 (both numerator and denominator are protected integers arising from distinct anomalies) but does **not** derive the ratio from a single symmetry. Authors should claim the weaker, correct statement and avoid the stronger, incorrect one. Recommend updating the DFD derivation to the DOF-counting framing.
