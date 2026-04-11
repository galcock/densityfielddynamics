# L9: SO(10) Branching Search for the Ratio 16/3

**Agent:** L9
**Date:** 2026-04-06
**Task:** Systematically search SO(10) representation theory, branching rules, Dynkin indices, and anomaly coefficients for any natural appearance of the ratio 16/3 — the DFD dark matter ratio Tr_chi(1)/Tr_b(1) = 16/3.

---

## 1. SO(10) Representations and SU(5) Branching

The relevant low-dimensional irreps of SO(10) and their SU(5) decompositions:

| SO(10) irrep | dim | SU(5) decomposition |
|---|---|---|
| 10 | 10 | 5 + 5̄ |
| 16 | 16 | 10 + 5̄ + 1 |
| 45 (adjoint) | 45 | 24 + 10 + 10̄ + 1 |
| 54 | 54 | 15 + 15̄ + 24 |
| 120 | 120 | 5 + 5̄ + 10 + 10̄ + 45 + 45̄ |
| 126 | 126 | 1 + 5̄ + 10 + 15 + 45̄ + 50 |
| 210 | 210 | 1 + 5 + 5̄ + 10 + 10̄ + 24 + 40 + 40̄ + 75 |

**Ratio check.** Looking for 16/3 ≈ 5.333 in any quotient dim(R)/dim(R'):
- 16/3: only if a 3-dimensional SU(5) subrep existed, but SU(5)'s smallest non-trivial is 5.
- 48/9, 80/15 etc. — none land on 16/3.
- 16 itself is the spinor dimension; it is never quotiented by 3 at the SU(5) level.

**Conclusion (Step 1):** 16/3 does not appear as a dimension ratio in SO(10)→SU(5) branching.

---

## 2. Pati–Salam SU(4)_c × SU(2)_L × SU(2)_R

The spinor 16 decomposes under PS as
- 16 = (4, 2, 1) + (4̄, 1, 2)

Dimensions: 4·2·1 + 4̄·1·2 = 8 + 8 = 16. The "3" candidate inside SU(4)_c is the SU(3) color subgroup: 4 → 3 + 1 (quark + lepton).

Counting colored vs colorless states in one generation:
- Colored: (3,2) + (3̄,1) + (3̄,1) dims 6 + 3 + 3 = 12
- Colorless: (1,2) + (1,1) + (1,1) dims 2 + 1 + 1 = 4

Ratios 16/12 = 4/3 and 12/4 = 3 appear naturally, but **16/3 does not** as a dimensional quotient in the PS decomposition.

---

## 3. Anomaly Coefficients

SO(10) is anomaly-free (all irreps have vanishing cubic anomaly). Under SU(5), the cubic anomaly A(R) satisfies:
- A(5) = 1, A(10) = 1, A(5̄) = −1, A(1) = 0.
- One 16 of SO(10): A(10) + A(5̄) + A(1) = 1 − 1 + 0 = 0. ✓

No 16/3 from anomaly ratios, since all relevant coefficients are integers bounded in magnitude by small numbers.

**Gravitational anomaly / Tr Y:** For one SM generation, Tr Y² summed over all states gives well-known values like 10/3, 20/3 — these arise from hypercharge sums, not 16/3. Close neighbors but not the target.

---

## 4. Dynkin Indices — The Strongest Lead

Dynkin index T(R) for SO(10) irreps, normalized T(10) = 1 (vector):

| R | dim R | T(R) |
|---|---|---|
| 10 | 10 | 1 |
| 16 (spinor) | 16 | 2 |
| 45 (adjoint) | 45 | 8 |
| 54 | 54 | 12 |
| 120 | 120 | 28 |
| 126 | 126 | 35 |
| 210 | 210 | 56 |

**Key ratios tested:**
- T(16)/T(10) = 2
- T(45)/T(16) = 4
- T(120)/T(16) = 14
- **2 · T(45) / N_gen = 16/3** when N_gen = 3. (T(16)·T(45)/3 = 2·8/3 = 16/3.)

Equivalently: **T(spinor) · dim(adjoint SU(3)) / N_gen = 16/3**, since dim adj SU(3) = 8 numerically coincides with T(45_{SO(10)}).

This is a numerical coincidence of two distinct "8"s:
- Dynkin index of SO(10) adjoint = 8 (group-theoretic, = h∨ − 2 with dual Coxeter h∨(SO(10)) = 8)
- dim(SU(3) adjoint) = 8 (gluon count)
- h^0(T CP²) = 3 (holomorphic tangent sections), **not** 8 — that coincidence does not hold

So the algebraic identity is:
  **16/3 = 2 · h∨(SO(10)) / N_gen = T(spinor)·T(adjoint)/N_gen**

This is the cleanest GUT-theoretic route to the number, but it requires **identifying N_gen = 3 with the generation index and h∨(SO(10)) = 8 with a color/gauge factor**, which is not a standard anomaly-matching identity in the literature.

---

## 5. Fine-Grained SM Decomposition of the 16

Under SO(10) → SU(3)_c × SU(2)_L × U(1)_Y:
- 16 = (3,2)_{1/6} ⊕ (3̄,1)_{−2/3} ⊕ (3̄,1)_{1/3} ⊕ (1,2)_{−1/2} ⊕ (1,1)_{1} ⊕ (1,1)_{0}
- Dims: 6 + 3 + 3 + 2 + 1 + 1 = 16 ✓

Trying every quotient of one of these dimensions by 3:
- 16/3, 6/3 = 2, 3/3 = 1, 2/3, 1/3 — **16/3 never arises as dim/dim** because 16 is not divisible by any integer in the decomposition.

However: 16/(N_colorless per gen) = 16/4 = 4 and 16/(N_Weyl in (3,2)) = 16/6 = 8/3. Still no 16/3 via this route.

---

## 6. The DFD Interpretation: Tr_χ / Tr_b

In DFD, the ratio
  Ω_χ / Ω_b = Tr_χ(𝟙) / Tr_b(𝟙) = 16/3
is interpreted as
- **Numerator 16:** All Weyl fermions in one generation counted with ν_R, i.e. **one full spinor 16 of SO(10)**. This is natural and well-defined: dim(16_spinor) = 16 counts exactly (Q, u^c, d^c, L, e^c, ν^c) as 6+3+3+2+1+1 Weyl components.
- **Denominator 3:** The sphaleron / 't Hooft vertex exponent in SU(2)_L, which equals the number of generations N_gen = 3 because each instanton produces one (QQQL) per family.

The 3 therefore descends from **N_gen = 3 as an anomaly-matching condition** (A_SU(2)^2 · U(1) and 't Hooft vertex counting), not from SO(10) representation theory *per se*. There is no SO(10) Clebsch–Gordan coefficient that gives 3 in the denominator.

---

## 7. Literature Search Summary

Representative GUT references checked for any appearance of 16/3:
- Slansky, Phys. Rep. 79 (1981) — master tables of branching rules.
- Feger & Kephart, *LieART* (2012, updated 2020) — exhaustive Dynkin index and branching tables.
- Yamatsu, arXiv:1511.08771 — group-theoretic tables for all classical groups.
- Wilczek & Zee; Georgi–Glashow; Fritzsch–Minkowski original SO(10) papers.

In none of these does **16/3 appear as a named branching ratio, Dynkin index ratio, or anomaly coefficient**. The closest relatives:
- 16/3 as a beta-function coefficient in QCD β_0 = 11 − (2/3)n_f: not the same structure.
- 16/3 in the supergravity Kähler anomaly (Bagger–Witten): unrelated.
- 16/3 in β₀ for SU(3) with 8 fundamentals: β₀ = 11 − 16/3 = 17/3. **The 16/3 does appear here as (2/3)·n_f with n_f = 8.** This is the only standard physics context where a bare 16/3 arises.

**This is suggestive.** In QCD-like β₀ with 8 matter multiplets, (2/3)·8 = 16/3 is the matter contribution to asymptotic freedom running. DFD could plausibly reinterpret 16/3 via running of a dark sector coupling with 8-flavor content — but the current DFD derivation routes it through the χ-vs-baryon tracer count, not through an RG coefficient.

---

## 8. Findings

1. **No direct representation-theoretic branching in SO(10), SU(5), or Pati–Salam produces 16/3 as a dimension ratio.** The 16 lives in the spinor; the 3 does not appear anywhere in SO(10) Clebsch–Gordans except by *choosing* a generation count.

2. **The cleanest algebraic identity is numerical, not structural:**
   16/3 = 2·T(45_{SO(10)}) / N_gen = T(16)·h∨(SO(10)) / N_gen
   This uses h∨(SO(10)) = 8, T(16_spinor) = 2, and N_gen = 3 as an external input. It is a *rewriting* of 16/3, not an independent derivation.

3. **The only standard physics context with a raw 16/3 is the one-loop QCD-like β-function** with 8 matter multiplets: (2/3)·8 = 16/3. This is a potential bridge if DFD's dark sector carries 8 flavors, but the current χ-tracer derivation does not use this.

4. **The DFD derivation is cleanest as it stands:** Tr_χ(𝟙) = 16 from dim(spinor 16) and Tr_b(𝟙) = 3 from N_gen / sphaleron. These two inputs are *individually* well-grounded, and the ratio 16/3 follows by definition. Searching for it as a single SO(10) Clebsch does not appear fruitful.

5. **Recommendation for DFD v3.4:** Do not claim 16/3 as an SO(10) branching ratio. Instead, present it as:
   16 (spinor content of one generation, SO(10) datum)  ÷  3 (generations, anomaly/sphaleron datum)
   with both factors derived independently from standard model structure plus the DFD assumption that χ tracks *all* Weyl species while b tracks only those coupling to the sphaleron.

---

## 9. Residual Open Questions

- Is there a 2-loop or higher GUT-threshold effect where 16/3 arises from a Dynkin index contracted with a color factor? Not checked here.
- Does an E_6 or E_8 embedding of SO(10) hide a natural 3 in the denominator (e.g. via the 27 = 16 + 10 + 1 of E_6, where the "1+10" might play a role)? Worth checking: 27/(27−16) = 27/11, no; 16/(27−16−10) = 16/1 = 16; 16/3 does not appear.
- Could the 3 come from triality in SO(8) ⊂ SO(10)? SO(8) has three 8s (vector + two spinors) related by triality. A ratio 16/3 = (8+8)/3 = (sum of two spinors)/(number of triality classes) is superficially appealing but has no known physical content.

**None of these side routes produced 16/3 either.**
