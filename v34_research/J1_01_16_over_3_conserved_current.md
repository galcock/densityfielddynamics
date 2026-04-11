# J1-1: Search for a Conserved Current Locking Ω_χ/Ω_b = 16/3

**Agent:** J1-1
**Date:** 2026-04-07
**Problem:** H6/H9 proved Tr_χ(1)/Tr_b(1) = 16/3 is a DOF identity but Ω_χ/Ω_b is an energy-density ratio. Closing the gap requires a conserved current that locks n_χ/g_χ = n_b/g_b through EW breaking and confinement.
**Verdict:** **NEGATIVE.** No conserved current within SM + CP²×S³ topology produces 16/3 as an energy-density lock. The closest literature analogues (SU(9) dark GUT, relaxation mechanism) either give the wrong ratio or abandon symmetry for RG scaling.

---

## Attack 1: SO(10) fermion number F = 16 per generation

**Claim under test:** F counts all 16 Weyl species equally; B counts the 3 quark colors. Ratio F/B = 16/3 per generation. Can F and B act as two independent conserved charges whose ratio fixes Ω_χ/Ω_b?

**Result: FAILS.** Three fatal problems:

1. **F is not independent of B+L.** For the 16 of SO(10), F = B + L + (right-handed-neutrino count). For each SM generation without ν_R, F = 15 (not 16). With ν_R, F = 16 but then F = B + L exactly, so F/B = (B+L)/B = 1 + L/B = 1 + 3/3 = 2 per generation, not 16/3. The "16" is only the *dimension* of the SO(10) spinor, not a charge carried per baryon.

2. **Sphalerons violate F.** Every sphaleron event has Δ(B+L) = 2N_f = 6, which means ΔF = 6. So F is *not* conserved through the EW phase transition — exactly the epoch where H9 requires the lock to form.

3. **F does not distinguish χ from SM.** Both sectors are built from the same SO(10) 16, so F cannot act as a χ/b-discriminating charge. It acts equally on both and gives no ratio.

**Conclusion:** Fermion-number counting gives 16 as a dimension of a representation, but this does not translate into a conserved Noether charge that separates χ from baryons in the ratio 16/3.

---

## Attack 2: Internal S³ winding current W ∈ π₃(S³) = ℤ

**Claim under test:** Smooth field configurations on the internal S³ carry a conserved integer winding W. If χ zero modes carry W = 16 while baryons carry W = 3, then conservation of W forces n_χ × 3 = n_b × 16 up to decoupling, giving 16/3.

**Result: FAILS.** Three fatal problems:

1. **S³ winding counts field configurations, not particles.** π₃(S³) is the homotopy of *maps* S³ → S³, equivalent to the Skyrmion number for a sigma-model target. DFD's S³ is the *fiber*, not the target. There is no sigma-model field living on S³ whose Skyrmion number could be identified with a particle count.

2. **Zero modes do not carry winding.** Kaluza-Klein zero modes on S³ are harmonic spinors — they are constant (up to phase) on the S³ and therefore have W = 0 identically. The 16 vs 3 counting comes from the *number* of zero modes, not from any individual mode carrying topological charge 16 or 3.

3. **Conservation of W is vacuous.** In DFD, S³ is fixed as the internal manifold. W is a property of field configurations, and the vacuum (with W = 0 for all fields) saturates conservation trivially. There is no ΔW = ±1 instanton sector that could transfer "winding" from χ to b in the way sphalerons transfer B+L.

**Conclusion:** π₃(S³) gives no usable conservation law for particle counting.

---

## Attack 3: Kaluza-Klein level current

**Claim under test:** Zero modes (SM + χ) carry KK number 0; non-zero modes carry KK number ≥ 1. A conserved "KK number mod N" could distinguish 16-mode sectors from 3-mode sectors.

**Result: FAILS.**

1. KK number on S³ is the eigenvalue of the S³ Laplacian, labeled by (j, m). It is only *approximately* conserved — vertices in the 4D effective theory mix levels whenever the 4D momentum is comparable to 1/R_{S³}.
2. Even if exactly conserved, KK-number gives a hierarchy of mass scales (m_n = n/R), not a ratio of number densities among zero modes. Both χ and b live at KK level 0 in DFD.
3. There is no natural mod-N grading at the zero-mode level. All 16 χ + 3 b modes have KK number 0.

**Conclusion:** KK-level conservation does not discriminate χ from b at the zero-mode level, which is where the 16/3 ratio must live.

---

## Attack 4: Discrete Z_N isometries of CP²×S³

**Claim under test:** Iso(CP²) × Iso(S³) = SU(3) × SO(4). A discrete subgroup gives exact Z_N symmetries that could produce a Z_16 × Z_3 structure locking the ratio.

**Result: FAILS.**

1. **Continuous symmetries don't discretize to Z_16.** SU(3) ⊃ Z_3 (center) only, not Z_16. SO(4) = SU(2)×SU(2) ⊃ Z_2 × Z_2. The maximum discrete subgroup of the isometry group at the center is Z_3 × Z_2 × Z_2 = Z_12 at best, and the "16" cannot appear.
2. **Z_3 center of SU(3) gives the 3, not the ratio.** The Z_3 center of SU(3)_color is what makes baryons color singlets (three quarks). This is already used in DFD to get the "3" of 16/3. There is no independent Z_16 factor to pair with it.
3. **The 16 comes from *representation theory*, not isometry.** As shown in H6, the 16 is the rank of the Dirac spinor bundle over CP² × S³ (= 2^{dim/2} = 2^{(4+3)/2} rounded appropriately, with explicit computation giving 16). This is a bundle fact, not an isometry group fact, and it yields no Noether charge.

**Conclusion:** The discrete isometry structure of CP²×S³ does not contain a Z_16 factor that could supply the missing current.

---

## Attack 5: GUT coupling unification / beta function ratio (the literature hit)

**Finding in the literature:** [Cabrera, Harigaya, Sundrum 2024, arXiv:2410.22412](https://arxiv.org/html/2410.22412v1) "Predicting the Dark Matter-Baryon Abundance Ratio" explicitly uses **Q_N = 16/3** and achieves ρ_DM/ρ_B within 10% of the observed value.

**But the mechanism is NOT a conserved current.** Direct reading of the paper:

> "Q_N = (4/3) Σ_ψ n_ψ C(R₁,ψ) d(R₂,ψ)" — this is a sum over colored fermions weighted by Casimirs and representation dimensions.
>
> "Λ_QCD(φ) ∝ (Λ_N(φ))^{Q_N / β_3}" — Q_N/β_3 is a ratio of beta function coefficients.

**Q_N = 16/3 in this paper is a beta function coefficient**, not a Noether charge. The mechanism is a *relaxation* (moduli-scanner) mechanism where a modulus φ scans the dark confinement scale relative to Λ_QCD, and the RG running carries Q_N as its exponent. The ratio ρ_DM/ρ_B emerges dynamically, not by conservation.

**This tells us something important for DFD:** The literature's only successful "16/3" is a *beta function identity*, not a charge identity. It requires:
- A scanner modulus (not present in DFD unless identified with the scalaron)
- A dark confining gauge group (not present in DFD — χ is not confined in any known DFD construction)
- RG running from a UV unification scale

None of the three ingredients are currently in DFD.

**A closer analogue:** [Bai, Berger, Korwar 2024, arXiv:2411.16860](https://arxiv.org/html/2411.16860) "Comparable Dark Matter and Baryon Energy Densities from Dark Grand Unification" uses SU(9) dark GUT with a conserved U(1) current **D − (B−L)** and gets ρ_D/ρ_B ≈ 5 (not 16/3). This is the closest genuine "conserved current" mechanism in the literature. It fails the DFD target by ≈6% and requires a mirror dark QCD sector with Sp(4)_D confinement — again not in DFD.

---

## What the literature says about "F is conserved"

The claim in the task prompt that "F is conserved by all SM interactions" is **technically true at tree level** (every SM vertex has an even number of fermion fields, so ΔF = 0), but:

- F = B + L, so it is *not independent* of the B+L current already violated by sphalerons.
- F is anomalous under SU(2)_L: ∂_μ j^μ_F = (N_f/(16π²)) Tr(W W̃), same as B+L.
- At the EW phase transition, sphalerons erase any pre-existing F asymmetry down to the equilibrium value set by B−L.

So F is *not* a new conserved current. It is B+L wearing a different label.

---

## Does any known mechanism work?

Three candidates from the broader literature, none of which apply to DFD as currently formulated:

| Mechanism | Conserved current | Ratio produced | Works for DFD? |
|---|---|---|---|
| Asymmetric DM via sphalerons | B−L | O(1), tunable via masses | No — requires m_χ ≈ 5 GeV, DFD predicts m_χ different |
| Dark GUT SU(9) (Bai et al. 2024) | D−(B−L) | ≈5 | No — DFD has no dark QCD |
| Relaxation scanner (Cabrera et al. 2024) | None (RG mechanism) | Q_N/β_3 = 16/3 | No — DFD has no scanner modulus + dark gauge |
| B+L (sphaleron-violated) | Not conserved | N/A | No |
| F = SO(10) fermion number | = B+L, not independent | 2 per gen, not 16/3 | No |
| π₃(S³) winding | Trivially 0 on zero modes | N/A | No |
| Z_N isometry of CP²×S³ | Z_3 × Z_2² max | Gives the "3" only | Partial, missing "16" |
| KK number | Approximate, zero for both | N/A | No |

---

## Definitive conclusion

**No conserved current within current DFD machinery (SM + CP²×S³ + scalaron) can lock Ω_χ/Ω_b = 16/3.**

The 16/3 is real as a DOF/spectral-trace identity (H6) but is structurally incapable of controlling an energy-density ratio without one of the following additions to DFD:

1. **A dark confining gauge group** (à la SU(9) dark GUT) that gives χ a Λ_χ close to Λ_QCD via GUT unification. This would supply both a conserved dark baryon number D and a mass scale m_χ ≈ m_p. **Cost:** adds a new gauge sector, violating DFD's "SM + χ only" minimality.

2. **A scanner modulus coupled to both sectors via beta-function ratio 16/3** (à la Cabrera et al. relaxation). This identifies 16/3 as Q_N/β_3. **Cost:** requires dark gauge + a light scanner, and the 16/3 becomes a beta function coincidence rather than a topological identity.

3. **A gauged B−L with χ carrying a specific B−L charge** such that the sphaleron equilibrium condition forces n_χ/n_b = 16/3. **Cost:** requires assigning χ an ad hoc B−L charge; the 16/3 would then come from anomaly cancellation coefficients, not the S³ fiber counting.

**None of these preserves the H6/H9 spectral-trace origin of 16/3.** In all three cases, the "16/3" that appears in Ω_χ/Ω_b is a *different* 16/3 from the one in Tr_χ(1)/Tr_b(1).

**Recommendation for J1 campaign:** Stop looking for a conserved current. The 16/3 identity is a DOF counting that is structurally orthogonal to energy-density ratios. Pivot to one of:

- **Accept that 16/3 is not a Ω_χ/Ω_b prediction** and downgrade H6/H9 to "the DOF ratio is 16/3, matching the energy ratio ≈5.36 as a coincidence of O(1) factors."
- **Introduce a new ingredient** (dark gauge, scanner modulus, or gauged B−L) and accept the loss of minimality.
- **Prove a no-go theorem** that no minimal extension can close the gap, and treat the ≈5.36 agreement as unexplained within DFD.

---

## Sources

- [Cabrera, Harigaya, Sundrum, "Predicting the Dark Matter-Baryon Abundance Ratio," arXiv:2410.22412 (2024)](https://arxiv.org/html/2410.22412v1) — Q_N = 16/3 as beta function coefficient in relaxation mechanism
- [Bai, Berger, Korwar, "Comparable Dark Matter and Baryon Energy Densities from Dark Grand Unification," arXiv:2411.16860, JHEP 03 (2026) 135](https://arxiv.org/html/2411.16860) — SU(9) dark GUT with D−(B−L) conserved current, ρ_D/ρ_B ≈ 5
- [Agashe, Sundrum, "Baryon Number in Warped GUTs"](https://www.researchgate.net/publication/231072928_Baryon_Number_in_Warped_GUTs_Model_Building_and_Dark_Matter_Related_Phenomenology) — warped compactification and baryon number
- [Davoudiasl, Mohapatra, "Unified origin for baryonic visible matter and antibaryonic dark matter"](https://pubmed.ncbi.nlm.nih.gov/21231286/) — asymmetric DM from B−L
- [Fileviez Pérez et al., "Gauged Baryon Number and Dibaryonic Dark Matter," arXiv:2011.13887](https://arxiv.org/abs/2011.13887) — gauged U(1)_B with residual Z_3
- [Skyrme theory topology review, π₃(S³) and baryon number](https://link.springer.com/article/10.1140/epjc/s10052-017-4655-6) — winding numbers act as charges only for sigma-model target spaces, not KK fibers
