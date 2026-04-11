# K1-7: Vacuum Structure / Symmetry Breaking Derivation of Ω_χ/Ω_b = 16/3

**Agent:** K1-7
**Task:** Attempt to derive Ω_χ/Ω_b = 16/3 from vacuum structure or symmetry breaking pattern of DFD.
**Status:** NEGATIVE RESULT with one viable loophole identified.

---

## 1. Framing

Symmetry-breaking phase transitions fix order parameters (EW: v = 246 GeV; QCD: Λ ≈ 200 MeV). The question is whether any SSB event in DFD naturally produces the *energy-density* ratio Ω_χ/Ω_b = 16/3 ≈ 5.333.

DFD symmetry-breaking ladder (UV → IR):

| Scale | Event | Relevant order parameter |
|---|---|---|
| Λ_UV ~ M_P | Spectral cutoff / unification | g_UV → G_SM |
| M_R ~ M_P α³ ~ 10¹² GeV | B−L breaking (heavy ν) | M_R |
| v = 246 GeV | Electroweak | Higgs VEV |
| Λ_QCD ~ 200 MeV | Confinement | m_p |
| m_χ ≈ 96 keV | χ matter-onset | χ oscillation turn-on |

At each scale, some symmetry is broken and some ratio is fixed. We look for the scale at which n_χ/n_b OR ρ_χ/ρ_b is pinned to 16/3.

---

## 2. Number-density cogenesis (linear)

Assume a common CP-violating mechanism at T_EW simultaneously seeds baryon asymmetry and χ asymmetry, with production rates proportional to a group-theoretic counting factor. DFD's χ field lives in a 16-dimensional representation (Spin(10) spinor) while baryons live in SU(3)_c (3 colors). If the cogenesis current is LINEAR in the respective couplings:

    n_χ / n_b  =  g_χ / g_b  =  16 / 3       (at T = T_EW)

The question is whether this number-density ratio propagates to an *energy-density* ratio of the same value today.

---

## 3. Redshift to today

At T_EW both species are ultra-relativistic (T ≫ m_b ≫ m_χ). Once asymmetries are frozen into conserved number densities, each dilutes as a⁻³, so the ratio n_χ/n_b = 16/3 is preserved to all later times. Today both species are non-relativistic:

    ρ_χ / ρ_b  =  (m_χ / m_b) · (n_χ / n_b)
              =  (9.6×10⁻⁵ GeV / 0.938 GeV) · (16/3)
              =  1.024×10⁻⁴ · 5.333
              =  5.46 × 10⁻⁴

Target is 5.333. **This is off by a factor of 10⁴.** Linear cogenesis fails by exactly (m_b / m_χ).

---

## 4. What it would take to rescue this

The mass-ratio shortfall requires m_χ,eff ≈ m_b at the epoch where the ratio is locked. Three candidate rescues:

### 4a. Higgs-portal effective mass
A portal λ_Hχ χ² |H|² with λ_Hχ ≈ 16.5 would give m_χ,eff ≈ 1 GeV after EWSB. But:
- DFD's action contains no such operator — χ is protected by its topological origin as a Spin(10) spinor component of the internal manifold; a direct |H|²χ² coupling would violate the symmetry that keeps m_χ = 96 keV radiatively stable.
- λ_Hχ = O(10) is non-perturbative for a portal and would already be excluded by invisible Higgs width.

**Rejected.**

### 4b. ψ-field effective mass
A ψχ coupling could in principle boost m_χ,eff. But ⟨ψ⟩ at T_EW is Planck-suppressed (ψ is the background density field), so any ψχ² coupling contributes Δm_χ ≲ (T_EW)² / M_P ~ 10⁻⁴ eV. Orders of magnitude too small.

**Rejected.**

### 4c. Freeze-out at a scale where m_b(T) = m_χ(T)
At T ≫ Λ_QCD the "baryon" is a current-quark triplet with m_q ~ few MeV, not 1 GeV. The constituent mass arises at confinement. So at high T, baryon number is carried by quarks with effective mass ~ T (relativistic) or ~ m_q (non-relativistic below ~MeV). This does not bring m_b down to m_χ = 96 keV either; the quark masses are still 10× too big.

**Rejected.**

---

## 5. The one loophole: energy-density cogenesis

Everything above assumed the cogenesis mechanism produces a *number* asymmetry. Suppose instead the mechanism produces an *energy-density* imbalance directly (e.g., both sectors are sourced by the same CP-violating condensate energy, partitioned according to their DOF counting). Then:

    ρ_χ / ρ_b  =  g_χ / g_b  =  16 / 3                             (at T = T_freeze)

and because both sectors redshift as *matter* (a⁻³) from that point onward, the ratio is preserved *exactly* to today — IF the freeze-out happens when both are already matter-like.

This requires freeze-out at T ≲ m_χ = 96 keV (so that χ has already turned on as matter). The baryon asymmetry was set much earlier at T_EW, but its *energy density* only becomes ρ_b = m_b n_b at T ≲ m_b ~ 1 GeV, and then redshifts as a⁻³ thereafter. Similarly ρ_χ = m_χ n_χ below T ~ m_χ.

So both ρ_b and ρ_χ scale as a⁻³ from the moment each becomes non-relativistic. If the *partitioning* of some common condensate energy into χ-matter and b-matter occurs at or below T ~ m_χ, the ratio 16/3 can be set directly as an energy-density ratio without any m_χ/m_b suppression.

**Candidate DFD mechanism:** the χ field turns on as matter at T_χ ~ 96 keV. At this epoch, the pre-existing baryon energy density ρ_b (already matter-like since confinement) is present as a background. If χ's condensate at turn-on carries an energy set by the DFD internal-manifold DOF counting (16 units, spinor of Spin(10)) and the existing baryon density represents the 3-unit color counting, the ratio is locked:

    ρ_χ(T_χ) / ρ_b(T_χ)  =  16 / 3

and since both then dilute identically, this is what we observe today.

**However:** this is circular unless the *absolute* baryon density at T_χ is independently predicted to equal (3/16) × ρ_χ(T_χ). In standard cosmology, η_B is set at the EW scale by sphalerons and depends on CP phases, not on color counting. There is no known mechanism that forces ρ_b(T = 96 keV) = (3/16) × ρ_χ(T = 96 keV) from first principles.

The 16/3 can be *consistent* with DFD's DOF counting, but it is not *derived* from the symmetry-breaking pattern alone — an extra input (the synchronization of the baryon yield to the χ condensate scale) is required.

---

## 6. Verdict

**Negative with one structural loophole.**

1. Linear number-density cogenesis at T_EW gives n_χ/n_b = 16/3 but ρ_χ/ρ_b ≈ 5.5×10⁻⁴, off by 10⁴.
2. Portal / ψ-field rescues of m_χ,eff are excluded by DFD's own structure and by Higgs invisible-width bounds.
3. No SSB scale in DFD makes m_b,eff = m_χ,eff.
4. The only self-consistent path is **energy-density cogenesis at T ≲ m_χ**, where DOF counting (16 vs 3) partitions a common condensate. This is compatible with 16/3 but requires an independent assumption tying the pre-existing baryon density to the χ turn-on scale; it is not a pure SSB derivation.

**The symmetry-breaking cascade of DFD does NOT, by itself, fix Ω_χ/Ω_b = 16/3.** The 16/3 ratio is a DOF-counting statement, not a vacuum-structure statement, and therefore more naturally lives in the path-integral / initial-condition / anomaly-matching analyses (H6, J1-01, J1-02, J1-03, K1-04) than in an EWSB- or QCD-like symmetry-breaking derivation.

Recommended handoff: the energy-density cogenesis loophole (§5) should be checked against the χ turn-on dynamics in H5_mchi_direct_derivation.md to see whether the condensate energy at T = m_χ is independently fixed to equal (16/19) of the total matter budget.

---

## 7. Summary equation

    Ω_χ / Ω_b  =  (m_χ n_χ) / (m_b n_b)

Two-handle problem:
- Number handle: cogenesis can give n_χ/n_b = 16/3 (viable group-theoretic statement).
- Mass handle: no SSB pattern in DFD equates m_χ and m_b.

Therefore: SSB alone is insufficient. The 16/3 must come from counting (path-integral / anomaly / initial-condition), not from symmetry breaking.
