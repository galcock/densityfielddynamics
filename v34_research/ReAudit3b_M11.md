# ReAudit 3b — Independent re-verification of M11 (KK overlap → β)

**Auditor:** ReAudit3b agent (independent of M11 and Audit3)
**Date:** 2026-04-07
**Target:** `v34_research/M11_kk_overlap.md` claim
  c_ψ/M_P = (α/2π)·ψ₀·Tr(Q²)·index(D_V) = 0.0950
  ⇒ β = (c_ψ/2)·Δψ = 0.73° at Δψ = 0.27.

This document re-derives each factor from scratch, then states the verdict.

---

## (a) ψ₀ = 1/√(2π²) — VERIFIED

ψ is the harmonic 3-form on S³ (b₃(S³)=1). Up to a constant, ψ = c·dvol_{S³}.
The L²-normalization on the unit S³ is ∫_{S³} ψ₀² dvol = 1. With vol(S³) = 2π²
and ψ₀ constant on S³, ψ₀²·(2π²) = 1, so

  ψ₀ = 1/√(2π²) ≈ 0.22508.   ✓

Note: this is the *coefficient* of the unit volume form, i.e. a 0-form-equivalent
scalar. M11 uses it correctly as a multiplicative number in the dimensionally
reduced 4-d vertex.

## (b) Tr(Q²) = 9 — VERIFIED *under M11's own embedding*, but with a caveat

M11 takes V = O(9) ⊕ O⁵ on CP². Crucially, O(9) here means the line bundle
O_{CP²}(9), i.e. the 9th tensor power of the hyperplane bundle — it is **rank 1**,
not "9 line bundles of degree 1." So V is a rank-6 bundle (1 charged + 5 neutral),
not rank 14.

The single charged Weyl carries Q = 3 under the M11 embedding O(3k) ↔ k. Hence

  Tr Q² = 1·3² + 5·0² = **9**.   ✓ (under O(3k)↔k)

Caveat: this is *not* derived; it is a *postulate* of the embedding. If one
instead used the alternative reading Q(O(k)) = k (so Q=9 for O(9)), Tr Q² = 81
and c_ψ/M_P jumps by ×9. M11 does not justify O(3k)↔k from a deeper SM embedding
beyond pointing at Audit3's discussion. Treat this factor as a **convention,
not a derivation**.

## (c) index(D_V) on CP² — **INCORRECT**: M11 used Â instead of Td

This is the load-bearing error. Recall:

- CP² is **not** spin (w₂(CP²) ≠ 0). It is spin-c.
- The relevant operator is the **spin-c Dirac operator** twisted by a line bundle.
- Atiyah–Singer for the spin-c Dirac operator on a complex manifold X gives
    index(D⁺ ⊗ L) = ∫_X ch(L) · **Td(X)**,
  where Td(X) is the **Todd class**, not the Â-genus. The Â-genus only equals
  Td(X) on a true spin manifold (where Td = Â² on the holomorphic side, etc.);
  on a non-spin Kähler manifold the spin-c Dirac index is the holomorphic Euler
  characteristic χ(X, L) = ∫ ch(L)·Td(X) (Hirzebruch–Riemann–Roch).

For CP² with hyperplane class H, ∫_{CP²} H² = 1:

  c₁(CP²) = 3H,  c₂(CP²) = 3H².
  Td(CP²) = 1 + c₁/2 + (c₁² + c₂)/12
         = 1 + (3/2) H + (9H² + 3H²)/12
         = 1 + (3/2) H + **H²**.

  ch(O(k)) = 1 + kH + (k²/2) H².

  ch(O(k))·Td(CP²) |_{H²} = k²/2 + (3/2)·k + 1.

For k = 9:

  index(D⁺ ⊗ O(9)) = 81/2 + 27/2 + 1 = 108/2 + 1 = **55**.

Cross-check with HRR for line bundles on CP²:
  χ(CP², O(k)) = (k+1)(k+2)/2  for k ≥ 0.
For k = 9: (10·11)/2 = **55**.   ✓ (independent confirmation)

For O(0) = O the trivial line bundle:
  χ(CP², O) = (1·2)/2 = 1, not −1/8.

So the spin-c twisted Dirac indices on CP² are:

| bundle | M11 (Â-based) | correct (Td/HRR) |
|--------|---------------|------------------|
| O(9)   | 81/2 − 1/8 = 40.375 | 55  |
| O(0)   | −1/8                | 1   |
| O(9) ⊕ O⁵ total | 39.75      | 55 + 5·1 = 60 |

**M11's "40.375" is not the spin-c Dirac index of O(9) on CP². It is
∫ ch(O(9))·Â(CP²)|_top, which is a different (and non-integer) characteristic
number that has no direct interpretation as a count of zero modes on the
non-spin manifold CP².**

The integer 60 on the right column is precisely the integer that the α paper
uses for its "Dirac index 60 on CP² with V = O(9)⊕O⁵" — and that is *not* an
accident: 55 + 5 = 60 is the correct HRR computation for V = O(9) ⊕ O⁵.

## Recomputing c_ψ with the correct index

Two consistent ways to combine the factors:

### Option 1: Q²-weighted (M11's intended structure, corrected index)

Only the charged O(9) contributes; index(O(9)) = 55:

  c_ψ/M_P = (α/2π)·ψ₀·Tr(Q²)·index(O(9))
        = 1.16142e−3 · 0.22508 · 9 · 55
        = **0.1294**

  β = (c_ψ/2)·Δψ:
    Δψ = 0.27 → β = 0.01747 rad = **1.001°**
    Δψ = 1.0  → β = 0.0647 rad   = **3.71°**

### Option 2: Full bundle (use total index 60 instead of charged piece × Q²)

  c_ψ/M_P = (α/2π)·ψ₀·index(V)
        = 1.16142e−3 · 0.22508 · 60
        = **0.01568**

  β at Δψ=0.27 → 0.00212 rad = **0.121°**
  β at Δψ=1.0  → 0.00784 rad  = **0.449°**

Note Option 1 and Option 2 differ by a factor of (Tr Q²·index(O(9))) / index(V)
= (9·55)/60 = 8.25. They are **not** the same physics: Option 1 treats the
ψFF̃ vertex as Q²-weighted (correct for an EM anomaly), Option 2 treats it as
the bare topological index of the full bundle (which would be appropriate for an
α-like β-function coefficient, not a triangle anomaly with two photon legs).

The physically correct one for ψFF̃ is **Option 1** (the triangle requires two
EM insertions, hence Q² weighting). M11 had this structure right; the only
arithmetic error was Â vs Td.

## (d) M11's actual numerical claim, re-derived

  M11: c_ψ/M_P = 1.1614e−3 · 0.22508 · 9 · 40.375 = 0.0950   (their value)
  Correct: c_ψ/M_P = 1.1614e−3 · 0.22508 · 9 · 55      = 0.1294

The error is a factor 55/40.375 = 1.362, or +36%. This is **not** a factor of
2 and **not** a factor of π. It is the difference between Â(CP²)|_{H²} = −1/8
(which M11 erroneously used in place of Td(CP²)|_{H²}) and Td(CP²)|_{H²} = +1.
The shift is +9/8 in the H² coefficient, i.e. (81/2+1) − (81/2−1/8) = 9/8 →
55 vs 40.375.

## (e) β prediction(s) and comparison with observation

| variant                                | c_ψ/M_P | β(Δψ=0.27) | β(Δψ=1) |
|----------------------------------------|---------|------------|---------|
| M11 as written (Â, Tr Q²)              | 0.0950  | 0.735°     | 2.72°   |
| Corrected (Td, Tr Q²) — Option 1       | 0.1294  | 1.001°     | 3.71°   |
| Corrected, full bundle — Option 2      | 0.0157  | 0.121°     | 0.449°  |
| Planck/ACT/SPT central                 | —       | 0.30°      | 0.30°   |

- Option 1 with Δψ=0.27 lands at **1.0°**, ~3.3× the observed central value
  and well outside the 4σ band (0.30 ± 0.11 → 4σ ≈ 0.74°).
- With Δψ=1 (the "natural unit"), Option 1 gives **3.7°**, ~12× too large.
- Option 2 (Δψ=0.27) gives **0.12°**, ~2.5× too small (about 1.6σ low).
- Option 2 (Δψ=1) gives **0.45°**, ~1.4σ high — this is the closest match,
  but it requires both (i) using the un-weighted index 60 (which is the wrong
  combinatorics for a Q²·F·F̃ vertex) and (ii) using Δψ = 1.

To reproduce the observed β = 0.30° one needs:

  Option 1: Δψ = 0.30°/1.001° × 0.27 = **0.0809** (about 30% of M11's H1–H4
  central, well outside the H1–H4 band).

  Option 2: Δψ = 0.30°/0.121° × 0.27 = **0.668** (~2.5× the H1–H4 central,
  outside the band on the other side).

  With Option 2 and Δψ=1: β = 0.449° (1.4σ high). Acceptable if Δψ is allowed
  to float to ~0.67.

In **no** combination of (correct index, M11's Tr Q² structure, M11's Δψ band)
does the prediction land on β_obs = 0.30° without tuning Δψ.

## (f) Diagnosis

Going through the user's three diagnostic options:

(i) **"M11 is correct and β = 0.73° is DFD's prediction":** NO. M11 uses Â
   instead of Td on a non-spin Kähler manifold. The Â-genus does not give the
   spin-c Dirac index on CP². The correct index is 55 (or 60 for the full
   V), not 40.375.

(ii) **"M11 has a factor-of-2 or π error":** PARTIALLY. There is no factor-of-2
   or π. The actual error is the substitution of Â(CP²)|_{H²} = −1/8 for
   Td(CP²)|_{H²} = +1, a correction of +9/8 in the H² coefficient and a 36%
   upward shift in c_ψ. Importantly the error goes the *wrong* way for hitting
   β_obs: the corrected c_ψ is *larger*, making the tension with Planck/ACT/SPT
   *worse* under M11's intended Q²-weighted formula and Δψ=0.27.

(iii) **"Depends on undetermined Δψ as a free parameter masquerading as
   prediction":** YES, this is the load-bearing issue. Even setting aside the
   Â-vs-Td error, the prediction β = (c_ψ/2)·Δψ is linear in Δψ, and Δψ is
   *not* derived in M11 — it is imported from H1–H4 with a quoted central of
   0.27 and a wide systematic band. M11's claim of "closed-form, parameter-free"
   is overstated: it is closed-form *given Δψ*, but Δψ itself is the free
   parameter that determines whether β lands at 0.12°, 0.30°, 0.73°, 1.0°, or
   3.7°. M11 explicitly notes (§6) that landing on β_obs requires Δψ ≈ 0.11
   (under their numbers) — i.e., Δψ is being silently re-fit. Under the
   *corrected* index, the required Δψ is even smaller (≈ 0.08) or much larger
   (≈ 0.67), depending on which combinatorics one chooses for the triangle.

## (g) Comparison with Audit3_M11_twist.md

Audit3 found M11 inconsistent at the level of *bundle choice*: the α paper's
"index 60" and M11's "Tr Q²·index = 363.375" cannot both be the right count on
the same O(9)⊕O⁵ bundle, because 60 and 363.375 differ by Tr Q² and a
sign-of-Â convention. Audit3's verdict was "INCONSISTENT — pick one twist and
recompute both α and β on it end-to-end."

ReAudit3b adds a sharper, *internal* finding: even on its own terms M11
miscomputes the index. Specifically:

- The α paper's "60" is the **correct** spin-c twisted Dirac index of
  O(9)⊕O⁵ on CP² via HRR (= 55 + 5).
- M11's "40.375" for O(9) alone is **wrong**: the right number is 55.
- M11's "39.75" for the full V is also **wrong**: the right number is 60,
  matching the α paper.

So the bundle is consistent between the two papers — what is inconsistent is
that M11 used the wrong characteristic class (Â) to extract its index, which
both (a) makes M11's number 40.375 disagree with the α paper's 60 and (b)
makes the resulting c_ψ depend on a fictitious "−1/8" correction that does not
arise on a non-spin manifold. Audit3 correctly diagnosed the disagreement;
ReAudit3b identifies *which side* is in error: M11.

If M11 is corrected to use Td (HRR), and the Q² weighting is retained, then:

  c_ψ/M_P = (α/2π)·ψ₀·9·55 = 0.1294,
  β(Δψ=0.27) = 1.0°,

which agrees with neither the α paper's "60-only" reading nor with the
observed β = 0.30°. So Audit3's "Option A" (keep O(9)⊕O⁵, accept that β =
0.73° is DFD's prediction and the 2.4σ tension is real) actually becomes
"β ≈ 1.0°" once M11 is arithmetically repaired — and the tension with
Planck/ACT/SPT deepens to ~6σ.

## (h) Verdict

**M11's "closed-form" β = 0.73° is not a parameter-free DFD prediction.**

1. Factor (a) ψ₀ = 1/√(2π²) is correct.
2. Factor (b) Tr Q² = 9 is a *convention* (the O(3k)↔k embedding), not a
   derivation; it should not be presented as forced by the bundle.
3. Factor (c) index(D_V) = 40.375 is **wrong**. The spin-c Dirac index of
   O(9) on CP² is 55 (HRR: (9+1)(9+2)/2 = 55), and of O(9)⊕O⁵ is 60. M11
   substituted the Â-genus for the Todd class on a non-spin manifold.
4. Repaired with Td and the Q²-weighted triangle structure, c_ψ/M_P = 0.1294
   and β(Δψ=0.27) = 1.0°. With the un-weighted full-bundle index, c_ψ/M_P =
   0.0157 and β(Δψ=0.27) = 0.121°.
5. β is linear in Δψ. Hitting β_obs = 0.30° requires Δψ ≈ 0.08 (Option 1,
   corrected) or Δψ ≈ 0.67 (Option 2, corrected) — neither value is derived
   in M11 or H1–H4; both are outside the H1–H4 central. Under the natural
   unit Δψ = 1 the predictions are 3.71° and 0.45° respectively.

The honest classification is **(ii) + (iii)**: M11 has an arithmetic error
(Â vs Td → 36% in c_ψ) *and* its "prediction" depends on an undetermined Δψ
that is being silently tuned. The β = 0.73° headline is neither derived nor
robust: a small bundle change moves it by 8×, a Δψ change moves it linearly,
and the index error moves it by 36%. None of these are truly fixed by the
geometry as M11 claims.

## (i) What would make this a real prediction

1. Fix the index calculation: use HRR / Td(CP²) = 1 + (3/2)H + H², giving
   index(O(k)) = (k+1)(k+2)/2 on CP².
2. Pin down the triangle combinatorics on first principles — is it Q²-weighted
   (Option 1) or full-bundle (Option 2)? This is the difference between an
   "EM anomaly with two photon legs" reading and an "axion-like overall
   topological coupling" reading. The two readings differ by ~8× in c_ψ.
3. Derive Δψ from the same internal geometry rather than importing it from
   H1–H4 with a wide band. As long as Δψ is a free parameter, β is a one-
   parameter fit, not a prediction.
4. Reconcile with the α paper's index = 60 explicitly. If both α and β are
   driven by the same chiral kernel of D_V on CP², the same Td-based count
   must appear in both derivations.

Until those four steps are done, β = 0.73° (and its corrected sibling 1.0°)
should be presented as a *contingent* number, not a closed-form DFD output.

---

**Files referenced:**
- /Users/garyalcock/claudecode/densityfielddynamics/v34_research/M11_kk_overlap.md
- /Users/garyalcock/claudecode/densityfielddynamics/v34_research/Audit3_M11_twist.md
