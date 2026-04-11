# Audit 3 — Can DFD use different bundle twists for α vs β (cosmic birefringence)?

**Auditor:** Audit3 agent
**Date:** 2026-04-07
**Target claims:**
- α = 1/137 from Dirac index 60 on CP² with V = O(9)⊕O⁵ (Ab initio α paper).
- β = (α/2π)·ψ₀·Tr(Q²)·index(D_V)·Δψ/2 from M11 (`v34_research/M11_kk_overlap.md`).
- M11 would need index ≈ 16 to hit β_obs = 0.30°, but the canonical α twist gives 60 → β = 0.73°.

**Question:** Can DFD consistently use O(9)⊕O⁵ for the α channel and a *different* effective index (16) for the β channel, by projecting out EM-neutral pieces with a Q²-weighted anomaly?

---

## 1. Is the EM charge of each component fixed by a single SM embedding?

M11 adopts the embedding **O(3k) ↔ Q = k**, which gives:

| Component | rank | k | Q (EM) | idx = k²/2 − 1/8 |
|-----------|------|---|--------|-------------------|
| O(9)      | 1    | 3 | **3**  | 40.375            |
| O(1)      | 1    | 0 | **0**  | 0 − 1/8 = −0.125  |
| O(1)      | 1    | 0 | 0      | −0.125            |
| O(1)      | 1    | 0 | 0      | −0.125            |
| O(1)      | 1    | 0 | 0      | −0.125            |
| O(1)      | 1    | 0 | 0      | −0.125            |

Under this single embedding, the five O(1) singlets are **EM-neutral**: they carry k = 0,
so Q(O(1)) = 0. They are the "ν_R-like" sterile pieces. They contribute to the
*topological* (ungauged) index but not to anything the U(1)_EM gauge field can see.

**Consequence:** the five O(1) singlets automatically drop out of **both** the U(1)_EM
β-function **and** the ψFF̃ triangle, because both are driven by the same Q-weighted
trace over the chiral spectrum. There is no degree of freedom to let them contribute
to one channel but not the other — they are invisible to A_μ by construction.

So: under M11's own charge assignment, the Q² projection does **not** create a gap
between the α-relevant index and the β-relevant index. Both channels see exactly the
same charged sub-bundle (O(9) only).

## 2. Q²-weighted index on the canonical twist

Using Q_i from M11's O(3k) ↔ k embedding:

  Σ_i Q_i² · idx(D_i) = 3² · 40.375 + 5 · 0² · (−0.125) = **363.375**

This is not 16. It is not 60. It is the same "363.375" that M11 already wrote as
`Tr Q² · index(O(9)) = 9 × 40.375`. The Q² weighting *replaces* the bare index 60, it
does not coexist with it — and it does so uniformly across both α and β.

**Can realistic SM charges (Q_u = 2/3, Q_d = −1/3, Q_e = −1, Q_ν = 0) rescue it?**
Only if one reinterprets the O(9)⊕O⁵ bundle as carrying a *full SM generation* of
chiralities, which is *not* what either paper does. Both papers treat O(9) as a single
charged Weyl with Q = 3 (or, under the alternate reading in §2 of the α paper, as the
carrier of the entire topological count 60). There is no intermediate reading in
which the *same* O(9) carries Q² = 9 for β but integer multiplicity 60 for α.

Concretely, if one *tried* to decompose O(9) into an SM-like content of
{3·(2/3)² + 3·(1/3)² + 1} = 8/3 per Weyl and multiplied by some generation count to
match 60, the resulting Q² weighting would be fractional and would land near
60·(8/3)/15 ≈ 10.7, not 16. There is no canonical rational SM decomposition that
produces the needed 16.

## 3. The deeper problem: α and β are both driven by the chiral index

The α derivation uses β₀^EM = (2/3)·Σ Q²·N_c, which at one loop in DFD closes on the
same chiral index that M11 uses. In mathematical terms:

- α channel: topological coefficient of the U(1)_EM β-function ∝ Σ Q²·index(D_V).
- β channel: ψFF̃ anomaly coefficient ∝ ψ₀ · Σ Q² · index(D_V).

These are **the same sum**. The only differences are the overall constants (α/2π, ψ₀,
Δψ/2) — all of which are fixed by independent physics. You cannot plug index = 60 into
α and index = 16 into β while using a single bundle: the bundle determines the chiral
kernel of D_V, and the kernel is what both anomalies count.

## 4. What *would* let DFD have index 60 for α and 16 for β?

Only a **physical splitting of the bundle into disjoint charge sectors** where:
(a) α sees the full bundle because its coefficient is topological (integer lift of the
full spin-c index), and
(b) β sees only a charged sub-bundle because the ψFF̃ vertex requires non-zero Q.

Under M11's O(3k) ↔ k embedding, (a) and (b) *are* the same count, because the
neutral pieces already contribute 0 to (b) and (if one is being careful about the
spin-c integer lift) they contribute the full −5/8 offset to (a). The difference
between 60 (α paper) and 40.375 (M11 O(9) alone) is exactly the spin-c integer lift
convention, not a physical projection.

To get 16, M11 proposes a **different bundle** entirely: O(5)⊕O⁵. This is not the
O(9)⊕O⁵ bundle with some neutrals projected out — it is a genuinely different twist
with a different holomorphic structure on CP². Under the same O(3k) ↔ k embedding,
O(5) doesn't even have an integer EM charge (k = 5/3), and the L9 motivation (O(5) ⊂
O(9) as a Z₂ subgroup) refers to a geometric subgroup of the structure group, not to
a Q²-projection.

## 5. Verdict

**INCONSISTENT.**

The α paper's index-60 count and M11's Tr Q²·index = 9·40.375 = 363.375 do **not**
describe two different projections of the same bundle — they are two different
*normalization conventions* applied to the same chiral kernel. A Q²-weighted
projection does not convert 60 into 16; under M11's own O(3k) ↔ k charge embedding it
converts 60 into 363.375, and the EM-neutral O(1) pieces are invisible to **both**
channels simultaneously.

Therefore DFD cannot consistently run:
- O(9)⊕O⁵ with index 60 for the α = 1/137 derivation, **and**
- O(9)⊕O⁵ with effective index 16 for β = 0.30°,
using "project onto EM-charged subbundle" as the mechanism. The EM projection is
already built into M11's Tr Q² factor, and it does not give 16.

The two internally consistent options are:

**Option A — keep O(9)⊕O⁵ everywhere.** Then M11's β = 0.73° stands, and the only
free lever is Δψ. Landing on β_obs = 0.30° requires Δψ ≈ 0.11, down from the H1–H4
central value 0.27. This is inside the quoted Δψ systematic band but it is *not* a
parameter-free prediction anymore — it is a one-parameter fit.

**Option B — replace the twist with O(5)⊕O⁵ everywhere.** This gives β = 0.30°
cleanly, but then the α paper's index-60 count has to be re-derived on the new
bundle. Under O(3k) ↔ k, O(5) is not even a valid charged line bundle; under the
alternative "integer lift of AS index" reading, O(5)⊕O⁵ gives an integer closer to 16
than to 60, which *breaks* the α derivation unless α is also recomputed on the new
twist. Neither paper does this recomputation.

**What's missing** to upgrade to CONSISTENT: a first-principles derivation on a
single bundle that (i) reproduces the α = 1/137 topological coefficient, (ii)
produces Tr Q²·index ≈ 16 or equivalent for the ψFF̃ vertex, and (iii) ties the two
through the same charge embedding. No document in the current `/v34_research/` or
the α PDF supplies this. Until it does, the two results use the *same* bundle in
name but *incompatible* counts in practice.

## 6. Recommended action

1. Pick one twist and recompute both α and β on it end-to-end. O(5)⊕O⁵ is the
   natural candidate because it matches observed β at Δψ = 0.27.
2. If the α = 1/137 derivation fails on O(5)⊕O⁵, the α paper's index-60 must be
   reinterpreted (e.g. as a sum over multiple generations or a different spin-c
   convention) so it also emerges from the same bundle.
3. Alternatively, accept that β = 0.73° is the sharp M11 prediction on the canonical
   O(9)⊕O⁵ twist and treat the Planck/ACT/SPT value as a ~2.4σ tension requiring
   Δψ revision, not a match.

## 7. Bottom line

Different bundle twists for α vs β are **not** a legitimate degree of freedom in DFD
as currently written. The Q² projection that would nominally separate them collapses
the neutral pieces in both channels identically, and the residual difference between
60 and 16 requires a genuinely different bundle, not a sub-projection of the same
bundle. **β = 0.30° from "O(5)⊕O⁵ for the birefringence only, O(9)⊕O⁵ for α" is not
consistent; the M11 sharp prediction on the α-paper twist remains β ≈ 0.73°.**
