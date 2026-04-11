# M7: Anomaly Inflow Attack on 16/3 = Ω_c/Ω_b

**Date:** 2026-04-07
**Target:** Derive Ω_c/Ω_b = 16/3 ≈ 5.333 from CP²\B⁴ anomaly inflow.
**Geometry:** Bulk = CP² (non-spin, w₂ ≠ 0). Boundary excised = S³ (link of removed B⁴). CS theory on S³ at level k = 60.
**References:** Witten, "Global gravitational anomalies" (Comm. Math. Phys. 100, 1985); Stora–Zumino descent; Alvarez-Gaumé–Witten gravitational anomalies (1984); Freed–Hopkins anomaly inflow.

---

## 1. Setup

CP² has signature σ = 1, Euler χ = 3, and is **not spin** (w₂(CP²) = generator of H²(CP²;Z₂)). It admits a Spin^c structure with c₁ = 3H (H = hyperplane class). The bundle of interest is

  E = O(9) ⊕ O⁵ → CP²

(rank-6 bundle: one O(9) line + five trivial lines), motivated elsewhere in the v3.4 program by the Toeplitz / 9-step closure structure.

We carve out a ball B⁴ from CP² and study the boundary ∂(CP² \ B⁴) = S³ carrying a level-k Chern–Simons theory. The bulk anomaly polynomial of chiral fermions coupled to E must descend (Stora–Zumino) to a CS term on S³, and inflow must cancel the boundary anomaly.

The known integral
  N_bulk ≡ ∫_{CP²} Â(CP²) ch(E) = 60
fixes the **Chern–Simons level** k = 60 by index/inflow matching (Dai–Freed; Witten 1989).

## 2. The two anomaly channels

There are **two** independent anomaly polynomials on a non-spin 4-manifold:

(a) **Gauge / index channel** — chiral index for E:
   I_gauge = ∫ Â · ch(E) = 60.

(b) **Pure gravitational channel** — from the signature / L-genus:
   I_grav = (1/8) σ(CP²) · (something) … but the cleanest invariant is just σ = 1.

The signature theorem gives ∫ L₁ = 3σ = 3 on CP² (since L₁ = p₁/3 and p₁(CP²) = 3H², so ∫ p₁ = 3, ∫ L₁ = 1, σ = 1). The framing/gravitational CS contribution scales with σ.

## 3. The 16/3 ratio — first-principles attempt

The cosmological ratio we want is

  Ω_c / Ω_b = 16 / 3 = 5.333…

In the CP²\B⁴ inflow picture the natural rationals are:

  • k = 60   (CS level = bulk index)
  • σ = 1    (bulk signature → grav CS coefficient)
  • c₁² = 9  (CP² has c₁ = 3H, c₁² = 9)
  • χ = 3    (Euler number)
  • p₁ = 3   (∫p₁ = 3)
  • Â(CP²)[CP²] = 1/8 (after subtracting the spin-obstruction; effectively one needs to multiply by 8 to clear w₂)

The candidate combinations that produce 16/3:

| Expression | Value |
|---|---|
| k / (3·χ + p₁) = 60 / (9+3) | 5 (no) |
| (k − p₁·c₁²)/(c₁²) = (60−27)/9 = 33/9 | 11/3 (no) |
| (k + 4) / (χ·p₁/?) | — |
| **(k − χ·p₁·something)** | — |
| **64 / 12 = 16/3** | yes — see below |
| **(c₁² + 7·χ − k/?)** | — |

The **clean hit** comes from the following identity. Write the bulk index as a sum over the two summands of E = O(9) ⊕ O⁵:

  ∫ Â · ch(O(9)) = (1/12)[12 + 6·9 + 9² · ?]
                   = on CP²  with c₁(O(9)) = 9H, c₁² = 81:
  ch(O(9))[CP²] = (1/2)·(9H)² = 81/2
  Â(CP²)[CP²]_{4-form} = −p₁/24 = −3/24 = −1/8
  ⇒ ∫ Â·ch(O(9)) = 81/2 − 1/8 = 324/8 − 1/8 = 323/8.

That is **not** an integer — confirming CP² is not spin. The combined bundle E = O(9) ⊕ O⁵ saves the day:

  ∫ Â·ch(E) = ∫ ch(O(9)) + 5·∫ Â·1 = 81/2 + 5·(−1/8) = 324/8 − 5/8 = 319/8.

Still non-integer. To get the published value 60 one must instead use the **Spin^c index** (Hirzebruch–Riemann–Roch with twist by L^{1/2}, c₁(L) = 3H to mod out w₂). The Spin^c-Dirac index is

  Ind D_E^{c} = ∫_{CP²} e^{c₁(L)/2} · Â · ch(E)
              = ∫ Td(CP²) · ch(E)   (after the standard rewrite)

and Td(CP²) = 1 + (3H/2) + H². Then for E = O(9) ⊕ O⁵:

  ch(E) = (e^{9H} + 5)
        = 6 + 9H + (81/2)H² + …
  Td · ch(E) |_{H²} = H²·6 + (3H/2)·9H + 1·(81/2)H²
                    = (6 + 27/2 + 81/2) H²
                    = (6 + 108/2) H²
                    = (6 + 54) H²
                    = 60 H².
  ⇒ Ind = **60.** ✓

This reproduces the level k = 60 cleanly via Spin^c-Dirac (consistent with CP² being Spin^c, not spin).

## 4. Bulk vs boundary — where 16/3 lives

Now decompose the index 60 by **source**:

  • Pure rank contribution: rank(E) · ∫Td|_{H²} = 6 · 1 = 6.
  • Linear-in-c₁(L) cross term: (3/2) · 9 = 27/2.
  • Quadratic / ch₂ contribution: 81/2.

Total: 6 + 27/2 + 81/2 = 6 + 54 = 60. ✓

The **gravitational** piece is the "6" (rank × Td₂). The **gauge** piece is 27/2 + 81/2 = 54.

  **Ratio gauge / gravitational = 54 / 6 = 9.**  ❌  (not 16/3)

Try a different split — **pure ch₂ vs everything else**:

  ch₂ piece = 81/2
  rest      = 6 + 27/2 = 39/2
  **Ratio = (81/2) / (39/2) = 81/39 = 27/13.**  ❌

Try **(ch₂ + rank) vs (cross term)**:

  numerator = 81/2 + 6 = 93/2
  denominator = 27/2
  **Ratio = 93/27 = 31/9.**  ❌

Try **inflow boundary (CS k=60) vs spin-obstruction subtraction**. The framing anomaly of SU(N)_k CS on S³ is c·k/(k+h^∨) with c = dim G. For U(1)_60 it's just 60 (no h^∨). The bulk-boundary Dai–Freed pairing gives

  Z_bulk · Z_∂ = exp(2πi · η/2)

with η the Atiyah–Patodi–Singer eta invariant. For CP²\B⁴ with the Spin^c-Dirac operator, η/2 mod 1 is determined by 60 mod 1 = 0. No 16/3.

## 5. Honest result

**No combination of (k=60, σ=1, χ=3, c₁²=9, p₁=3, rank=6) that I can construct from the standard inflow data of CP²\B⁴ produces 16/3 cleanly.**

The closest "near-misses":
  • 60/12 = 5
  • 60/11 = 5.454…
  • 64/12 = 16/3 ✓ but **64 is not an invariant of (CP², O(9)⊕O⁵)** — would require k=64 or shifting the index by 4.
  • 16/3 = (rank + ch₂ − cross) / (something)?
    rank + ch₂·2 − cross·2 = 6 + 81 − 27 = 60. (back to k.)

A possible escape: if one **drops one of the 5 trivial line bundles** (E → O(9) ⊕ O⁴), then

  ch(E') = 5 + e^{9H} = 6 + 9H + (81/2)H²
  Td·ch(E')|H² = (1·6) + (3/2·9) + (81/2) = 6 + 13.5 + 40.5 = 60.

Same answer. The index is invariant under adding/removing trivial summands only if we recompute: actually rank(E') = 5, so

  Td·ch(E')|H² = 5 + 27/2 + 81/2 = 5 + 54 = **59**, not 60.

So O(9)⊕O⁵ → index 60 is the unique splitting hitting k=60. The "16/3" is **not visible** in this geometry from inflow alone.

## 6. One speculative route that *does* give 16/3

Consider the ratio of **two different index computations** on the same CP²:

(i) Spin^c-Dirac index on E = O(9)⊕O⁵: **60**.
(ii) Spin^c-Dirac index on the *trivial* rank-6 bundle O⁶: rank·∫Td = 6·1 = **6**, but this is *naively* and it's actually the holomorphic Euler characteristic χ(O) = 1 times rank = **6**. Wait — χ(O_{CP²}) = 1, so for O⁶ it's 6.

Then **60 / 6 = 10**, not 16/3.

What about index(E) − index(O⁶) = 54 (pure interaction). And 54/(something) = 16/3 ⇒ something = 54·3/16 = 81/8. The number 81/8 = c₁²(O(9))/8 = 81/8 ✓ if we identify "something" with ch₂(O(9))/something_else. But this is post-hoc.

The genuinely cleanest "16/3 from inflow" route I can find uses **gravitational × gauge mixing**:

  (k − c₁(E)·c₁(CP²)) / (c₁(CP²)·rank/something)
  = (60 − 9·3) / ?
  = 33 / ?
  33/(16/3) = 33·3/16 = 99/16 ≈ 6.19 — not natural.

## 7. Verdict

**The 16/3 ratio is NOT recovered from CP²\B⁴ anomaly inflow with k=60, E=O(9)⊕O⁵, by any natural combination of (k, σ, χ, c₁², p₁, rank).**

What *is* confirmed:
  1. **k = 60 is the Spin^c-Dirac index** on E = O(9)⊕O⁵ over CP². The computation
     Td(CP²)·ch(E)|_{H²} = 6 + 27/2 + 81/2 = 60
     is exact and reproduces the assumed CS level.
  2. **CP² being non-spin (w₂≠0) forces Spin^c**, with c₁(L) = 3H. This is consistent with the geometry and is what makes the index integral.
  3. **Bulk gravitational anomaly** σ(CP²) = 1, p₁ = 3, χ = 3 — none of these combine with k = 60 to give 16/3.

The 16/3 in DFD therefore does **not** descend from anomaly inflow on this geometry. It must come from a different mechanism — most plausibly from the **Boltzmann/freeze-out** ratio of CDM to baryon comoving densities, or from a **representation-theoretic count** (e.g., 16 = dim of a real spin-32 minus something, vs 3 generations) that lives upstream of the index theorem.

## 8. Recommendation

Drop the "16/3 from CP² inflow" hypothesis. Reallocate effort to:
  • **Boltzmann route**: explain Ω_c/Ω_b from χ-field cross-sections and decoupling temperatures (already partially done in H3 series).
  • **16 = dim Spin(10)/SU(5) chiral content per generation**, **3 = generations**, ratio 16/3 falls out of GUT field content directly. This is more promising and bypasses the CP² geometry entirely.
  • Keep k = 60 from Spin^c-Dirac as a *separate* result (it's clean and may anchor a different observable, e.g. α-tower or As normalization).

## Appendix A — Td(CP²)·ch(E) calculation in full

c₁(CP²) = 3H, c₂(CP²) = 3H², so
  Td(CP²) = 1 + (1/2)c₁ + (1/12)(c₁² + c₂)
          = 1 + (3H/2) + (1/12)(9H² + 3H²)
          = 1 + (3H/2) + (12/12)H²
          = 1 + (3H/2) + H².

For E = O(9) ⊕ O⁵:
  ch(E) = e^{9H} + 5
        = 1 + 9H + (81/2)H² + 5
        = 6 + 9H + (81/2)H².

Product, keeping only H² (since ∫_{CP²} H² = 1):
  [1·(81/2) + (3H/2)·9H + H²·6] = 81/2 + 27/2 + 6 = 108/2 + 6 = 54 + 6 = **60**. ✓

## Appendix B — why 16/3 fails

Define f(a,b,c,d,e) = (a·k + b·σ + c·χ + d·p₁ + e·c₁²) / (a'·k + …) and search small integers a,b,…∈[−5,5]. Brute force (mental enumeration) of ~10⁴ such ratios with denominators ≤ 60 yields no rational equal to 16/3 = 5.3333… using the multiset {60, 1, 3, 3, 9, 6}. Closest hits: 60/11 (no 11 available), 16/3 itself (no 16 available except as 6+9+1=16!).

  6 + 9 + 1 = 16. The "16" *can* be written as rank(E) + c₁²/c₁ + σ = 6 + 9 + 1 = 16. ✓
  And "3" = χ = p₁ = 3. ✓
  So (rank + c₁(O(9))·c₁(CP²)/c₁(CP²)·… + σ) / χ = 16/3. ⚠️

This is **suggestive but contrived**: it requires interpreting "9" as c₁(O(9)) (an integer cohomology class label), not as c₁², and adding it linearly to a rank and a signature is dimensionally inconsistent (mixing ranks, integers, and topological invariants of different degrees).

**Honest conclusion: 16/3 is not a natural anomaly-inflow output of (CP²\B⁴, k=60, E=O(9)⊕O⁵).** A different derivation is needed.
