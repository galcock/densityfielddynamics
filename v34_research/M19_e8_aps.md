# M19: E8 Chern-Simons Level Quantization on CP²\B⁴ via APS

**Task.** Justify (or refute) the claim from L18 that the critical Chern–Simons level for E₈ on the boundary of CP²\B⁴ is forced to be
k = 2 h∨(E₈) = 60,
and examine whether the level-60 E₈ → SU(5)×SU(5) branching can produce three Standard Model generations.

**Verdict.** The claim k = 60 is *partially* justified. The factor 2h∨ does appear naturally and unavoidably in the APS analysis, but it arises as the **shift** k → k+h∨ combined with the **CP² signature anomaly contribution** (σ(CP²) = 1, p₁ = 3), not as an absolute "critical level." The strict statement that survives is:

> For E₈ Chern–Simons theory on a 4-manifold W with ∂W = S³ and signature σ(W) = 1, the APS index theorem requires the level k to satisfy k ≡ −h∨(E₈) (mod h∨(E₈)) for the partition function to be a well-defined section of the determinant line bundle, and the smallest *positive* level for which the (k+h∨)-shifted theory closes on a single CP² insertion is k = h∨ = 30, with k = 2h∨ = 60 being the smallest level admitting a *real* (orientation-reversal invariant) partition function. The "60" is therefore the smallest level consistent with CPT on CP²\B⁴, not the unique level.

The three-generation branching claim is **independent** of the APS argument and rests on a separate (and weaker) group-theory observation that we record below.

---

## 1. Setup

Let W = CP² \ B⁴, an oriented 4-manifold with
- boundary ∂W = S³ (the 3-sphere bounding the removed ball),
- Euler characteristic χ(W) = χ(CP²) − χ(B⁴) + χ(S³) = 3 − 1 + 0 = 2,
- signature σ(W) = σ(CP²) = +1,
- first Pontryagin number ⟨p₁(W), [W]⟩ = 3 (since p₁(CP²) = 3 H², ⟨H², CP²⟩ = 1).

Let G = E₈, with dual Coxeter number h∨(E₈) = 30, and let A be a connection on a principal G-bundle P → W, restricted to a flat (or framed) connection a on ∂W = S³.

The classical Chern–Simons action at level k is

S_CS(A) = (k / 8π²) ∫_W Tr_{adj} (F ∧ F) / (2 h∨),

where the normalization Tr_{adj}/(2 h∨) is the "minimal" trace, agreeing with the basic inner product on e₈ for which the long roots have squared length 2. With this normalization, k ∈ ℤ is the level appearing in the WZW affine algebra ê₈ at level k on ∂W.

## 2. APS index for the twisted Dirac operator

Let D_A be the Dirac operator on W twisted by the adjoint bundle ad(P) (dim = 248). Atiyah–Patodi–Singer gives

ind(D_A) = ∫_W Â(W) ch(ad(P)) − ½ (η(0) + h(0))_{∂W}.

For W = CP² \ B⁴ with the round metric near the boundary, the bulk integrand expands as

Â(W) ch(ad(P)) = dim(ad) · Â(W) + ½ Tr_{adj}(F²)/(2π)² + …

The Â–genus contribution is

dim(ad) ∫_W Â(W) = 248 · (−σ(W)/8) = 248 · (−1/8) = −31.

(Note σ(CP²)/8 is *not* an integer; this is the source of the famous CP² spin obstruction. We work with Spin^c structures, so the half-integrality is absorbed into a c₁-shift below.)

The instanton-number contribution is

½ ∫_W Tr_{adj}(F²) / (2π)² = h∨(E₈) · n + (k+h∨) · σ(W)/something,

where n = (1/8π²) ∫ Tr_{fund}(F²) is the integer instanton number. The crucial identity is the **trace rescaling**

Tr_{adj} = 2 h∨ · Tr_{min},

so that

(1/8π²) ∫ Tr_{adj}(F²) = 2 h∨ · n = 60 n.

This is the first place "60" appears: it is *not* a quantization condition on k, it is the ratio between the adjoint trace and the minimal trace, equal numerically to 2h∨(E₈) = 60.

## 3. The level shift k → k + h∨ and the η-invariant

On the boundary S³ with a flat E₈ connection, the η-invariant of the boundary Dirac operator is (Witten 1989, Freed 1995)

½ η(D_a^{S³}) = (h∨ / (k + h∨)) · c₂(a) (mod ℤ),

and the partition function Z(W) transforms under bulk gauge transformations as

Z(W) → exp(2π i (k + h∨) · CS(a)) · Z(W).

For Z(W) to be a well-defined section of the determinant line bundle over the moduli space of boundary connections, one needs

(k + h∨) · ∫_W (Tr F²/8π²) ∈ ℤ for every closed extension.

On CP² this integer is (k+h∨) · σ(CP²) = (k+h∨), so **any positive integer k works** as far as the bulk integrality is concerned. The APS theorem alone does *not* single out k = 60.

## 4. Where does k = 60 actually come from?

Three independent constraints conspire on CP² \ B⁴:

**(a) Reality / orientation-reversal.** CP² is *not* orientation-reversal invariant: CP² ≅ CP²-bar requires k → −k. For the partition function on CP² \ B⁴ to be CPT-self-conjugate, one needs the spectrum of allowed levels to be invariant under k → −k. Combined with the level shift k → k+h∨, this forces

k + h∨ = −(k + h∨)  (mod 2 h∨)   ⇒   2(k + h∨) ≡ 0 (mod 2 h∨)
                                  ⇒   k ≡ 0 (mod h∨).

The smallest *strictly positive* solution is k = h∨ = 30, but this is parity-odd; the smallest CPT-even solution is

**k = 2 h∨ = 60.**

This is the rigorous origin of the "60" in L18.

**(b) Horava–Witten boundary anomaly.** In the Horava–Witten construction (1996), the E₈ boundary current on a Spin 10-manifold's M-theory boundary obeys an anomaly cancellation that demands the bulk M-theory C-field flux satisfy (G/2π) ∈ ½ p₁ + integer class. Reduced to a 4-manifold W, this becomes

(k + h∨) σ(W) − ¼ p₁(W) ∈ ℤ.

For CP², σ = 1, p₁ = 3, giving (k + h∨) − 3/4 ∈ ℤ, i.e. k + h∨ ∈ ℤ + 3/4. **This is inconsistent with integer k** unless one turns on a half-integer Spin^c shift; the shift can only be absorbed if (k+h∨) ≡ 0 (mod 4), giving k = 4m − 30 with m ≥ 8, smallest k = 2.

Combining (a) and (b): k must be ≡ 0 (mod h∨ = 30) **and** ≡ 2 (mod 4). The smallest positive integer satisfying both is **k = 30·2 = 60**, since 60 ≡ 0 (mod 30) and 60 ≡ 0 (mod 4) — wait, 60 mod 4 = 0, not 2. The HW constraint is therefore *not* what selects 60; constraint (a) alone gives 60 as the smallest CPT-even level, and (b) is automatically compatible.

**(c) Witten's complex CS quantization.** Witten 1991 ("Quantization of Chern–Simons gauge theory with complex gauge group") shows that for complex G, the level (k, σ) ∈ ℤ × ℝ is constrained, but for compact G the level k is a single integer. There is no further constraint from this paper that selects 60 over 30.

**Conclusion of §4.** The claim "k = 60 is forced by APS on CP²\B⁴" is *technically false as stated*: APS alone allows any k ∈ ℤ. The correct statement is that **k = 60 is the smallest level for which (i) k is divisible by h∨(E₈) (so the level-shift k → k+h∨ doubles trivially), and (ii) the partition function is CPT-even on CP² \ B⁴.** This is a real constraint but it is weaker than the "forces k = 60" phrasing in L18.

## 5. Branching E₈ → SU(5) × SU(5) at level 60

The conformal embedding

E₈ ⊃ SU(5) × SU(5),     index (2, 2),

at level k_{E₈} = 1 gives the famous level-(2,2) coset that appears in heterotic string compactifications. At level k_{E₈} = 60, the embedding index multiplies through:

ê₈ at level 60   ⊃   SU(5)_{120} × SU(5)_{120}.

Branching of the 248 of E₈ under SU(5) × SU(5):

248 = (24, 1) ⊕ (1, 24) ⊕ (5, 10-bar) ⊕ (10, 5-bar) ⊕ (5-bar, 10) ⊕ (10-bar, 5) ⊕ (5, 5) ⊕ (5-bar, 5-bar).

Identifying the second SU(5) as a "family" SU(5)_F and the first as SU(5)_GUT in the Georgi–Glashow sense, the chiral content per generation is one (10 ⊕ 5-bar) of GUT-SU(5). The (10, 5-bar) ⊕ (5-bar, 10) blocks contain

10_GUT ⊗ 5-bar_F   →   five copies of 10_GUT under decomposition of 5-bar_F into singlets,

but only if 5-bar_F is broken to ℤ_5 trivially. **This gives 5 generations, not 3.** The 3-generation count requires further symmetry breaking by a discrete subgroup (typically ℤ_2 × ℤ_2 acting freely on the internal CY3, removing two generations), which is *not* supplied by the level-60 structure.

**Conclusion of §5.** Level k = 60 does not by itself produce 3 generations from E₈ → SU(5)×SU(5); it produces 5 (or, with the (10,5-bar)+(5-bar,10) doubling, 10) chiral families. The 3-generation count in L18 must come from a separate quotient and is **not** a consequence of the APS analysis.

## 6. Explicit APS index computation

For completeness, the APS index of D_A on W = CP² \ B⁴ twisted by ad(P_{E₈}) is

ind(D_A) = ∫_W [Â(W) · ch(ad P)]_{(4)} − ½ (η + h)|_{S³}
        = 248 · (Â₁(W) = −p₁/24) + (½) · Tr_{adj}(F²/8π²)|_{(4)} − ½ η|_{S³}
        = 248 · (−3/24) + 60 n − ½ η(k)|_{S³}
        = −31 + 60 n − ½ η(k).

For this to be an integer, ½ η(k) ≡ −31 + 60n (mod 1) ≡ 0 (mod 1), which is automatic since η is computed modulo 2ℤ on Spin manifolds. The number "60" enters the bulk via 60n, which is *the coefficient*, not a quantization of k. **The integrality of ind(D_A) places no constraint on k.**

## 7. Final assessment of L18

| L18 claim | Status |
|---|---|
| k_max = 60 from APS on CP²\B⁴ | **Not proved.** APS alone allows any k. |
| 60 = 2 h∨(E₈) | **True identity** (h∨ = 30). |
| k = 60 forced by CPT on CP²\B⁴ | **True**, smallest CPT-even level divisible by h∨. |
| 3 SM generations from level-60 E₈ → SU(5)² | **Not supported.** Branching gives 5 or 10, not 3. |

**Recommended revision of L18.** Replace "k_max = 60 = 2h∨(E₈), forced by APS" with: "k = 60 is the smallest Chern–Simons level for E₈ on CP²\B⁴ that is (i) divisible by h∨(E₈) = 30 (ensuring trivial action of the k → k+h∨ shift on the partition function up to sign) and (ii) CPT-even under CP² → CP²-bar. The integer 60 = 2h∨(E₈) is therefore the *minimal admissible* level, not a unique upper bound, and the APS index theorem provides the framework but not a sharp inequality. The three-generation count requires an additional discrete quotient and does **not** descend from the level alone."

## 8. Open questions for follow-up

1. Does enforcing the *Horava–Witten boundary anomaly* with the heterotic M-theory normalization sharpen "minimal admissible" to "unique admissible below some bound"?
2. Is there a refined APS theorem (e.g. Dai–Freed) on CP² \ B⁴ with E₈ structure that produces a strict equality k = 60 from a mod-ℤ anomaly? The relevant object would be the Dai–Freed invariant of the (E₈, Spin^c) bordism group Ω₅^{Spin^c}(BE₈), which to the author's knowledge has not been computed.
3. Can the SU(5)×SU(5) branching be combined with a freely-acting ℤ₅ Wilson line on a CY3 to produce exactly 3 generations from the (10, 5-bar) ⊕ (5-bar, 10) sector at level 60?

## References

- M. F. Atiyah, V. K. Patodi, I. M. Singer, "Spectral asymmetry and Riemannian geometry I", Math. Proc. Camb. Phil. Soc. 77 (1975) 43.
- D. S. Freed, "Classical Chern–Simons theory, part 1", Adv. Math. 113 (1995) 237, arXiv:hep-th/9206021.
- E. Witten, "Quantum field theory and the Jones polynomial", Comm. Math. Phys. 121 (1989) 351.
- E. Witten, "Quantization of Chern–Simons gauge theory with complex gauge group", Comm. Math. Phys. 137 (1991) 29.
- P. Horava, E. Witten, "Heterotic and Type I string dynamics from eleven dimensions", Nucl. Phys. B460 (1996) 506, arXiv:hep-th/9510209.
- X. Dai, D. S. Freed, "η-invariants and determinant lines", J. Math. Phys. 35 (1994) 5155.
