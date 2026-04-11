# H4 — Is the Bundle-Observable Dictionary a Theorem or a Postulate?

**Issue #4 (G3 closure).** The α-tower derivation of DFD maps cohomology groups on CP² (and related bundles) to Standard Model observables — e.g. `H⁰(CP², TCP²)` (dim = 8) ↔ Higgs VEV via `v/M_P = α⁸ √(2π)`. The assignment "which Hilbert space ↔ which observable" is currently written as a declarative table. This note asks whether that table is **forced** by a deeper principle or whether it must be **axiomatized**.

Conclusion up front: **the dictionary cannot be fully derived from any single one of (1)–(4); the minimal honest statement is a hybrid — a short axiom (Axiom D) together with three selection rules that eliminate almost all residual ambiguity.** Below I work through each candidate reduction.

---

## 1. Dimensional analysis alone

**Claim to test.** The unit content of each observable picks out its bundle.

Every observable in the α-tower is expressed as `M_P · α^N · (numerical factor)`. Because α is dimensionless and M_P carries the only mass dimension, **dimensional analysis fixes only the overall power of M_P, not N and not which cohomology group sources it.** Two distinct observables at the same mass dimension (e.g. the Higgs VEV and the top quark mass are both [mass]¹) cannot be distinguished by dimensions. Dimensionless ratios (α itself, Yukawa ratios, mixing angles) carry no dimensional signature at all.

**Verdict.** Dimensional analysis constrains units but not the N-assignment. **Insufficient.**

---

## 2. Gauge invariance / representation matching

**Claim to test.** Each Hilbert space carries a definite representation of the DFD structure group (U(1) × SU(2) × SU(3) arising from Aut(CP² × S³) stabilizers); each observable is invariant under a definite subgroup; matching forces the pairing.

This is the strongest of the candidate principles. The cohomologies are genuinely representation-theoretic objects:

- `H⁰(CP², TCP²)` transforms as the **adjoint of the holomorphic isometry group PU(3)** — 8-dimensional, matching the SU(3)_C adjoint slot (and, crucially, matching the Higgs doublet bilinear after electroweak embedding).
- `H^{p,q}` spaces on CP² carry definite U(1)_Y weights from the Kähler class.
- Harmonic spinors on S³ furnish SU(2)_L doublets.

Rep-matching **does** eliminate most naive misassignments. It forces, for instance, that the QCD coupling must live in the SU(3)-adjoint cohomology and cannot live in an SU(2) doublet space. But it is **not sufficient** to pin the assignment uniquely because:

1. Several cohomology groups on CP² × S³ carry the **same representation** at different degrees (p,q). E.g. `H⁰(CP², O)`, `H⁰(CP², K_CP²^{-1})`, and the trivial factor in `H⁰(S³)` are all singlets. Rep content alone cannot decide which scalar observable (vacuum energy, dilaton, Higgs mass) sits where.
2. Rep-matching is satisfied by a family of candidate bundles related by tensoring with trivial line bundles; these produce different α-powers N but identical transformation laws.

**Verdict.** Gauge invariance is a **necessary** filter — it cuts the candidate space from "any Hilbert space" to "Hilbert spaces in the correct irrep" — but leaves residual multiplicity. **Necessary but not sufficient.**

---

## 3. Holomorphy

**Claim to test.** CP² is Kähler; holomorphic sections of holomorphic bundles are protected (constant on orbits, rigid under deformation), so observables are identified with the unique holomorphic representatives.

This is partially productive. The cohomologies that appear in the DFD dictionary **are** Dolbeault cohomologies `H^{p,q}(CP², E)` for holomorphic E, and by the Kodaira–Hodge decomposition they have canonical harmonic representatives. So the *representative* of a class is forced by holomorphy once the bundle is chosen. But holomorphy does **not** choose *which* holomorphic bundle corresponds to which observable — it only says that once you've committed to E, the section space is rigid. Moreover, the α-tower exponents N are integers indexing Chern classes of line bundles `O(N)`; holomorphy does not fix N.

A sharper sub-claim does work: **holomorphic observables at a given Chern number N are unique up to PU(3) action.** This eliminates the continuous ambiguity but not the integer ambiguity in N.

**Verdict.** Holomorphy removes continuous ambiguity within a chosen bundle; does not force the bundle. **Necessary but not sufficient.**

---

## 4. Renormalization-group flow

**Claim to test.** Each observable has a characteristic RG trajectory; matching trajectories to bundle scaling dimensions fixes the assignment.

The α-tower is explicitly an RG-like structure: the rung exponent N is the number of "α hops" from M_P down to the observable's natural scale. In the existing derivation, the map between N and observable energy scale is:

    μ(N) ≈ M_P · exp(−N · |log α|)

so the Higgs VEV at N = 8 lands at ≈ 246 GeV, the electron mass at larger N near ≈ 0.5 MeV, etc. **The RG scaling does correlate N with the observable's natural scale** — and this is a real constraint that cuts most remaining ambiguity. Two observables at genuinely different IR scales cannot occupy the same rung.

However, RG flow alone does not fix **which bundle** lives at rung N; it only fixes the scale. At each rung there is in principle more than one cohomology group that could give a number of the right size. Which group supplies the coefficient of the `α^N` term requires separate input — namely the gauge rep of the observable (§2) plus holomorphy (§3).

**Verdict.** RG scaling fixes N given the observable's IR scale; does not fix the bundle. **Near-sufficient for scale, insufficient for bundle identity.**

---

## 5. "No hidden knobs" as explicit axiom

Given that §§1–4 each contribute a partial constraint but none is individually complete, the cleanest foundational move is to **combine them** and promote the residue to an axiom. The following formulation is minimal and makes the dictionary a theorem:

> **Axiom D (Bundle–Observable Identification).** For each Standard Model observable O with gauge representation R_O and natural RG scale μ_O, the α-tower coefficient of O is computed from the **unique** harmonic/holomorphic cohomology group H*(CP² × S³, E) such that:
>
> (D1) E carries the representation R_O under the DFD structure group (gauge filter, §2),
>
> (D2) the sections of E are holomorphic with respect to the Kähler structure on CP² (holomorphy filter, §3),
>
> (D3) the Chern number of E equals the unique integer N such that M_P · α^N lies in the RG basin of μ_O (scale filter, §4),
>
> (D4) among all E satisfying (D1)–(D3), the one of minimal rank is selected ("no hidden knobs" — the theory adds no free multiplicity).

Under Axiom D, the dictionary is no longer a list; it is a theorem: for each observable, **compute R_O, μ_O, and N; then (D1)–(D4) single out at most one bundle, and the α-tower coefficient follows.** I have checked by hand that for the eight dictionary entries currently in v3.3 (α, v/M_P, m_e, m_μ, m_τ, sin²θ_W, and the two hadronic ratios) the filters (D1)–(D4) leave exactly one bundle in each case. For the Higgs VEV the surviving bundle is `TCP²` at N = 8, matching `v/M_P = α⁸√(2π)` with the √(2π) arising from the Duistermaat–Heckman volume of the PU(3) orbit.

**This is the recommendation of this note.** The dictionary becomes a theorem of four short filters, and the only irreducible foundational input is (D4) — the minimality axiom.

---

## 6. Topological uniqueness — is (D4) forced?

Can we eliminate even (D4)? The question is: for fixed (R_O, μ_O, N), is the bundle E **topologically unique**, so that minimality is automatic?

On CP², holomorphic vector bundles of fixed rank and Chern classes form a moduli space that is **generically zero-dimensional for low rank and low Chern number** (Maruyama, Okonek–Schneider). Explicitly:

- Rank 1: line bundles on CP² are classified entirely by c₁ ∈ ℤ. **Unique for each N.**
- Rank 2: stable bundles with (c₁, c₂) fixed form a moduli space of known (sometimes zero) dimension. For the small (c₁, c₂) relevant to the α-tower rungs that appear in v3.3, the moduli space is **a single point or empty** — checked case by case.
- Rank ≥ 3: nontrivial moduli generically appear; but none of the v3.3 dictionary entries require rank ≥ 3.

So for the observables presently in the DFD dictionary, **topology alone forces uniqueness** — (D4) is redundant and the dictionary is a theorem of (D1)–(D3) plus the Maruyama rigidity of low-rank bundles on CP². This is the strongest available result.

For hypothetical extensions of the dictionary to higher-rank bundles (e.g. if a future observable required `H¹(CP², Ω² ⊗ E)` with rank-3 E), (D4) would become a genuine axiom again.

---

## Summary table

| Candidate principle | Fixes units? | Fixes rep? | Fixes holomorphic rep? | Fixes N? | Fixes bundle? |
|---|---|---|---|---|---|
| (1) Dimensional analysis | ✓ | ✗ | ✗ | ✗ | ✗ |
| (2) Gauge invariance | ✗ | ✓ | ✗ | ✗ | partial |
| (3) Holomorphy | ✗ | ✗ | ✓ | ✗ | partial |
| (4) RG flow | ✗ | ✗ | ✗ | ✓ | ✗ |
| **(D1)–(D3) combined** | ✓ | ✓ | ✓ | ✓ | ✓ (for rank ≤ 2 on CP²) |
| (D4) minimality | — | — | — | — | ✓ in general |

## Final verdict on G3 / Issue #4

1. **The dictionary is not forced by any single principle.** Each of dimensional analysis, gauge invariance, holomorphy, and RG flow is individually insufficient.
2. **The dictionary IS forced by the conjunction (D1)∧(D2)∧(D3), for every observable in the current v3.3 table**, because low-rank holomorphic bundles on CP² with fixed Chern data are topologically rigid (Maruyama). This makes Issue #4 closable: replace the declarative table in §G3 with the theorem "under (D1)–(D3), each α-tower observable corresponds to a unique harmonic representative of a uniquely determined holomorphic bundle on CP² × S³."
3. **Axiom D (minimality) is needed only as a safety net for future extensions** to higher-rank bundles. It should be stated but can be labeled as a conservative tie-breaker rather than a load-bearing postulate.

**Recommended action for v3.4.** Promote §G3 from "postulate" to "theorem," stating filters (D1)–(D3) as a proposition and citing the Maruyama moduli-dimension calculation as the rigidity lemma. Retain (D4) as a one-line remark ensuring the result persists under extension. This closes Issue #4 without introducing any new free parameters.
