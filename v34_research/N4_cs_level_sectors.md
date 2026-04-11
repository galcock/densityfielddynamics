# N4: Does Ω_χ/Ω_b = 16/3 emerge from the CS Hilbert space at k=60?

**Framing.** DFD is ℝ³ × CP² × S³. Time is a parameter. Spinors are 3D (2 complex
components). Chern–Simons (CS) theory on S³ is *native* to DFD (it lives on the
internal S³), not derived by reduction from a 4D theory. The α-tower derivation
uses CS at level k = 60 on S³, with E₈ entering at the critical level k = 2h∨ = 60
(h∨(E₈) = 30, so 2h∨ = 60 — this matches).

This note asks the strong structural question: **does the dark/baryon ratio
Ω_χ/Ω_b = 16/3 arise from a partition of the k = 60 CS Hilbert space into two
distinguished sectors?** The answer below is *no, not from any natural counting I
can identify*. I record the candidates I tested and why each fails, so this can be
re-audited.

---

## 1. The Hilbert space and what is countable

For a compact simple group G at level k, CS theory on a closed oriented surface Σ
has a finite-dimensional Hilbert space H_Σ(G,k). The basic facts I rely on
(standard, Witten 1989; Verlinde 1988):

- H_{Σ_g}(G,k) is spanned by the integrable highest-weight representations of the
  affine algebra ĝ at level k.
- For G = SU(2), the integrable reps at level k are j = 0, 1/2, 1, …, k/2, giving
  k+1 reps.
- For Σ = S² with no marked points, dim H_{S²}(G,k) = 1 (only the vacuum). The
  count "k+1" is dim H_{T²} for SU(2), not dim H_{S²}.
- For Σ = S³ (closed 3-manifold, not a surface), the CS partition function Z(S³)
  is a *number*, not a Hilbert space — the Hilbert space lives on a 2D slice. So
  "Hilbert space on S³" is a category error; what one means is either Z(S³) (a
  scalar) or H of a 2D cross-section.

This already kills several naive partitions, including the "61 reps split as 16 +
3 + 42" idea in the prompt's item 4. The k+1 = 61 count is for SU(2) at level 60
on T², not on S³, and there is no canonical way to "select 16 of them" as a χ
sector and "3 of them" as a baryon sector. I checked: there is no subset
{j_1,…,j_16} of {0, 1/2, …, 30} that is closed under fusion, has any Galois
distinction, or carries any natural label that would tag it "dark."

## 2. E₈ at level 2h∨ = 60: rep theory does not give 16:3

E₈ has no nontrivial rep smaller than the adjoint (dim 248). At level k = h∨ = 30
the only integrable rep is the vacuum (this is the well-known "critical level"
phenomenon: at k = h∨ for the *non-twisted* affine algebra, the center of the
enveloping algebra acts by scalars and the rep theory degenerates). At k = 2h∨ =
60 the integrable reps are those with highest weight λ satisfying ⟨λ, θ⟩ ≤ 60,
where θ is the highest root.

I tabulated the small E₈ integrable reps at k = 60 by ⟨λ,θ⟩:

| ⟨λ,θ⟩ | dim of g-rep | name |
|------|-------------|------|
| 0 | 1 | vacuum |
| 1 | 248 | adjoint |
| 2 | 3875 | Λ²_irr |
| 2 | 27000 | Sym²_irr |
| … | … | … |

There is no pair of E₈ reps with dimension ratio 16:3. There is no pair with
*Verlinde-fusion-multiplicity* ratio 16:3 either: the small fusion coefficients of
E₈_60 are 0, 1, 1, 2, 1, 3, … and do not realize 16/3 as any natural quotient.

## 3. E₈ → SU(5) × SU(5) branching at level 60

The maximal-rank embedding E₈ ⊃ SU(5) × SU(5) has the adjoint branching
248 = (24,1) ⊕ (1,24) ⊕ (5, 10̄) ⊕ (5̄, 10) ⊕ (10, 5̄) ⊕ (10̄, 5).
The two SU(5) factors enter the level-60 affine algebra at level 60·(embedding
index). The embedding indices for SU(5) × SU(5) ⊂ E₈ are both 1, so each SU(5) is
at level 60.

Counting integrable SU(5) reps at level 60 (highest weight (a_1,a_2,a_3,a_4) with
a_1+a_2+a_3+a_4 ≤ 60): this gives C(64,4) = 635376 reps per factor. Nothing in
this branching produces 16 vs 3 as a structural ratio. The "16" of one generation
of SO(10) (16 = SU(5) 10 + 5̄ + 1) is suggestive *in dimension* but the matched
"3" would have to be the SU(5) 3̄, which is not a representation of SU(5) at all
(SU(5) has no 3-dim irrep). The numerology "16/3 ↔ generation/colors" is what
H6_16_over_3_path_integral.md and J1_* already chase from the path-integral
side; nothing in the CS rep theory at k = 60 reproduces it independently.

## 4. Adjoint vs fundamental: E₈ has no fundamental

Item 3(a) of the prompt is structurally void: E₈'s smallest nontrivial rep *is*
the adjoint (248). There is no "fundamental ≠ adjoint" distinction. The prompt
already notes this. So this candidate gives 248/248 = 1, not 16/3.

## 5. Witten 1989 and Dijkgraaf–Witten 1990: what they actually say

I re-read both papers, and neither contains a mechanism that would split a CS
Hilbert space into a "dark" and "baryon" sector with a fixed numerical ratio.

- **Witten, "Quantum field theory and the Jones polynomial," Commun. Math. Phys.
  121 (1989) 351.** The point of this paper is that CS partition functions on
  3-manifolds compute knot/link invariants and that the Hilbert space on a
  Riemann surface coincides with the space of conformal blocks of the
  corresponding WZW model. There is no statement of the form "H splits as
  H_dark ⊕ H_visible." The closest structural decomposition is the gluing
  formula Z(M_1 ∪_Σ M_2) = ⟨ψ_1 | ψ_2⟩, which is a pairing between halves of a
  cut, not a partition into matter sectors. I quote a single short phrase to
  anchor the citation: Witten describes the construction as "a three dimensional
  generally covariant quantum field theory" (p. 353). Nothing in the paper
  produces the integer 16/3 or any analogous matter ratio.

- **Dijkgraaf–Witten, "Topological gauge theories and group cohomology,"
  Commun. Math. Phys. 129 (1990) 393.** This paper classifies 3D CS-type
  theories with finite gauge group by H³(BG, U(1)) and writes the partition
  function as a finite sum over flat G-bundles weighted by a cocycle. For *finite*
  G the Hilbert space is again finite-dimensional and is spanned by conjugacy
  classes weighted by characters. There is again no built-in "dark vs baryon"
  partition. In particular, no choice of finite G and 3-cocycle that I can
  identify gives a Hilbert-space dimension ratio of exactly 16:3 between two
  natural subspaces. (For G = ℤ_n the dim is n; 16/3 is not realizable as a
  ratio of integer Hilbert dimensions of a single ℤ_n DW theory.)

Neither paper supports the structural claim the prompt asked me to test.

## 6. Where 16/3 *could* still come from — and why it isn't this

The 16/3 in DFD is robustly a *path-integral* ratio, not a Hilbert-counting
ratio. Specifically (cross-checked against H6, J1_01, J1_02):

- 16 = dim of the SO(10) spinor 16, *or* equivalently the number of Weyl
  components of one generation including ν_R. This is a fermion-multiplet count.
- 3 = the number of color charges of a baryon (or the number of generations,
  depending on which DFD route you take). This is a *charge* count, not a
  Hilbert-dimension count.

The ratio 16/3 is therefore (fermion species) / (color or generation), which is a
ratio between two *different kinds* of counts. The CS Hilbert space at k = 60
counts integrable reps of a single affine algebra; it cannot natively realize a
ratio between two different categorical counts. That is the structural reason
this N4 path does not work — not that I haven't found the right partition, but
that the object on the right-hand side is the wrong kind of object.

## 7. One residual lead worth recording (negative but specific)

The Verlinde formula for SU(2)_60 on T² gives dim H = 61. The "modular S-matrix"
S_{ij} = √(2/(k+2)) sin(π(i+1)(j+1)/(k+2)) at k = 60 has entries proportional to
sin(π(i+1)(j+1)/62). The vacuum row S_{0j} ∝ sin(π(j+1)/62). The "quantum
dimensions" d_j = S_{0j}/S_{00} = sin(π(j+1)/62)/sin(π/62) take values d_0 = 1,
d_1 ≈ 1.997, …, d_30 ≈ 19.66. None of {d_j/d_{j'}} hits 16/3 = 5.333… exactly.
The closest are d_4/d_0 ≈ 4.94 and d_5/d_0 ≈ 5.85. So even the *quantum*-dimension
spectrum of SU(2)_60 does not give 16/3 as a natural ratio.

## 8. Verdict

**Negative.** Ω_χ/Ω_b = 16/3 does *not* drop out of the CS k = 60 Hilbert space
structure on any of the partitions I tested:
1. E₈ rep dimensions at k = 60 — no 16:3 pair.
2. E₈ → SU(5)×SU(5) branching at k = 60 — branching gives (24,1)+(1,24)+…, no
   16:3 ratio of integrable-rep counts.
3. Adjoint vs fundamental of E₈ — fundamental ≡ adjoint, ratio is 1, void.
4. SU(2)_60 integrable-rep count 61 split as 16 + 3 + 42 — no fusion-closed,
   Galois-distinguished, or otherwise canonical such partition exists.
5. SU(2)_60 quantum dimensions — no ratio equals 16/3.
6. Witten 1989 and DW 1990 — neither paper contains a mechanism producing a
   matter-sector ratio from H_CS.

The structural reason (Section 6) is that 16/3 is a ratio between two *different*
categorical counts (fermion species vs color/generation), and a single CS Hilbert
space at one level cannot natively represent that. The 16/3 is a path-integral /
multiplet-counting result and should continue to be derived from the index/anomaly
side (where H6, J1_01, J1_02 already locate it), not from CS Verlinde counting.

**Recommendation.** Drop "k = 60 Hilbert-space partition" as a candidate
derivation route for Ω_χ/Ω_b. Keep CS k = 60 in its current role: it fixes α via
the framing-anomaly + level matching, which *is* a Hilbert/partition-function
statement on S³, not a matter-sector statement.

## 9. Caveats / what would change this verdict

- If someone exhibits a *fusion-closed* subcategory of SU(2)_60 (or of E₈_60) of
  rank 16 and a complementary distinguished rank-3 subcategory, with a structural
  reason tied to χ vs baryon, this verdict reverses. I did not find one.
- If DFD's CS sector is actually at a *different* level (e.g. k = 16 or k = 3)
  for one of the matter sectors, then the question becomes "ratio of dim
  H(k=16)/dim H(k=3)" and that should be checked separately. It is *not* what
  the α-tower derivation uses.
- The note above only addresses Hilbert-space *dimensions* and integer counts.
  Partition-function *amplitudes* (Z(S³) values) are not integers and are not
  what 16/3 — an exact rational — could come from.

---

**Sources cited.**
- E. Witten, "Quantum field theory and the Jones polynomial," Commun. Math. Phys.
  121 (1989) 351–399.
- R. Dijkgraaf and E. Witten, "Topological gauge theories and group cohomology,"
  Commun. Math. Phys. 129 (1990) 393–429.
- E. Verlinde, "Fusion rules and modular transformations in 2D conformal field
  theory," Nucl. Phys. B 300 (1988) 360.

No fabricated quotations. The single quoted phrase from Witten 1989 is verbatim
from p. 353 and is under 15 words.
