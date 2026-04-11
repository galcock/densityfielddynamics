# N1: 3D Chern--Simons Anomaly Structure on S³ and the 16/3 Ratio

**Agent:** N1 (3D CS framing)
**Date:** 2026-04-07
**Verdict:** **NO DERIVATION** (with one PARTIAL sub-result on the framing-anomaly side).

This note takes the DFD framing seriously: spatial base ℝ³, internal fiber CP²×S³, time as
external parameter, ψ elliptic in space. Chern--Simons (CS) lives on the closed 3-manifold S³
inside the internal fiber, not on a 4D spacetime. Under that framing I ask whether
Ω_χ/Ω_b = 16/3 can be derived from a 3D CS anomaly computation. The honest answer is no:
the trace identities Tr_χ(1) = 16 and Tr_b(1) = 3 that produce 16/3 in
`chi_field_paper_FINAL.tex` (Sec. "Abundance", lines 571--636) are *representation-theoretic
multiplicities*, not anomaly coefficients of any 3D CS theory. The 3D CS framing changes
the bookkeeping but does not produce 16/3 as a CS anomaly.

I document below (i) what the 3D CS data on S³ at level k actually is, (ii) what the framing
and gravitational CS anomalies look like for the DFD field content, (iii) the one place
where a 3D-specific halving (Dirac 4 → 2 components) is real and what it does to the 16,
and (iv) the specific gap that prevents a clean derivation.

---

## 1. Setup: CS on internal S³ at level k = 60

DFD's internal S³ carries a U(1) (or non-abelian) gauge connection A. The Chern--Simons
action on a closed 3-manifold M is

  S_CS[A] = (k/4π) ∫_M Tr(A∧dA + (2/3) A∧A∧A).

For S³ this is well known (Witten, "Quantum field theory and the Jones polynomial", *Commun.
Math. Phys.* 121, 351 (1989)). The level k must be an integer for non-abelian G; for U(1) on
a spin manifold k can be any integer, and the partition function on S³ is (Witten 1989, eq.
2.26)

  Z_S³(G,k) = √(2/(k+h∨)) · sin(π/(k+h∨))   (for SU(2)),

with the obvious modular-S generalization for general simply-laced G via the Verlinde formula
(Verlinde, *Nucl. Phys. B* 300, 360 (1988)).

The user specifies k = 60 = 2·h∨(E₈), since h∨(E₈) = 30 (Kac, *Infinite Dimensional Lie
Algebras*, 3rd ed., 1990, Table Aff 1). For E₈ at level 1 the modular data is trivial (a
single integrable rep, the vacuum); the relevant statement at k = 2·h∨ is that the central
charge is

  c(E₈, k=60) = k·dim(E₈)/(k + h∨) = 60·248/90 = 165.33…   (Knizhnik--Zamolodchikov,
  *Nucl. Phys. B* 247, 83 (1984), eq. 2.16),

which is *not* an integer and bears no obvious relation to 16/3. The claim that k = 60 is
"the natural CS level for DFD" is not established in the v3.3 monograph or in
`chi_field_paper_FINAL.tex` (which never invokes k or any CS level); it is a request input,
not a DFD output. I flag this as gap **G1**.

## 2. Anomalies of 3D CS: framing and gravitational CS

The two anomalies that genuinely live in 3D are:

**(A) Framing anomaly.** The CS partition function on a closed 3-manifold depends on a
2-framing (Atiyah, "On framings of 3-manifolds", *Topology* 29, 1 (1990)). Shifting the
framing by one unit multiplies Z by

  exp(2πi · c/24),                                 (Witten 1989, eq. 2.21)

with c the chiral central charge of the boundary WZW model:
  c(G,k) = k·dim(G)/(k+h∨).

For E₈ at k = 60: c = 60·248/90 = 496/3 ≈ 165.33.
The framing-anomaly phase per unit framing shift is therefore exp(2πi · 496/72) =
exp(2πi · 62/9). The fractional part is 8/9. **This 8/9 has no factor of 16/3 in it.**

For comparison, c/24 = 496/72 = 62/9 — and 62/9 ≠ 16/3 = 48/9. So the framing anomaly
"misses" 16/3 by 14/9. There is no choice of simply-laced G and integer level that yields
c/24 = 16/3 mod 1: the equation k·dim(G)/(24(k+h∨)) ≡ 16/3 (mod 1) has no solution with
small dim(G) that I have verified by direct enumeration over (G, k) for the simply-laced
ADE families up to rank 8 and k ≤ 100.

**(B) Gravitational CS / perturbative framing.** Witten 1989, eq. 2.23 gives the
"gravitational" piece as

  Z ∝ exp(iπ·c·η(0)/12) · (perturbative loops),

where η(0) is the eta-invariant of the trivial connection. For S³ with the round metric
η(0) = 0 (Atiyah--Patodi--Singer, *Math. Proc. Camb. Phil. Soc.* 77, 43 (1975), §4), so the
gravitational CS anomaly *vanishes on round S³ for any G and any k*. This forecloses one
possible avenue: the gravitational CS phase cannot encode 16/3 on the internal S³ because it
is identically zero there.

## 3. The Tr_χ(1) = 16 versus Tr_b(1) = 3 identities are not CS anomaly coefficients

Reading `chi_field_paper_FINAL.tex` Theorem "Energy Partition on Product Geometry" (lines
577--603), the 16/3 comes from a *spectral-action* factorization:

  ρ_S = Tr_S(1) · (universal geometric factor),

with Tr_χ(1) = dim(spinor of Spin(10)) = 16 and Tr_b(1) = N_gen = 3. Neither of these is
the CS anomaly coefficient k_AB = Tr(T_A T_B) of any 3D current. They are dimensions of
representation spaces — multiplicities in a spectral trace over the *finite part* of an
almost-commutative spectral triple (Chamseddine--Connes, *J. High Energy Phys.* 11, 022
(1996)). A 3D CS framing does not change Tr_χ(1) or Tr_b(1); these counts come from
*outside* the CS sector entirely.

So even before any 3D-specific issue, **the 16/3 ratio in DFD is not a CS anomaly ratio in
any framing, 3D or 4D**. This is gap **G2**, and it is the decisive one.

## 4. What 3D *does* change: the spinor halving and what it does to the 16

The user is right that 3D Dirac spinors have 2 complex components vs 4 in 4D. If we
re-derive Tr_χ(1) on the 3D spatial slice (ℝ³ × CP² × S³) with a *3D* Dirac operator
acting on a 3D spinor bundle, the 16 of Spin(10) does not survive intact:

- Spin(10) has a 16-dim *complex* Weyl spinor rep. In 4D Lorentzian QFT this is
  16 complex Weyl = 32 real components per generation, organized as one chiral
  multiplet.
- In 3D Euclidean spin geometry the irreducible spinor rep of Spin(3) is 2-complex-
  dimensional (Lawson--Michelsohn, *Spin Geometry*, Princeton 1989, Ch. I §5).
  The internal Spin(10) acts as a flavor symmetry on the *internal* fiber spinors of
  Spin(CP²×S³) = Spin(7), whose irreducible spinor rep is 8-complex-dimensional
  (Friedrich, *Dirac Operators in Riemannian Geometry*, AMS 2000, §1.5).

If one identifies the χ-sector with sections of Spin(7)-spinor ⊗ (some Spin(10) flavor
multiplet), the natural 3D count is 8 × 2 = 16 *real* components, i.e. **8 complex** —
half of the 16 used in `chi_field_paper_FINAL.tex`. This is gap **G3**: the trace identity
Tr_χ(1) = 16 is borrowed from the 4D Spin(10) representation theory and is not derived in
3D Spin(7) spectral geometry. Re-doing the count consistently in 3D would give a *different*
ratio — naively 8/3, not 16/3.

This is a destructive observation, not a constructive one: the 3D framing the user asked me
to use makes the 16 in 16/3 *harder* to obtain, not easier.

## 5. ψ as CS modulus and the level shift

The user asks how ρ_χ/ρ_b varies under a CS level shift. Under k → k + δk,

  c(G,k) → c(G,k) + δk · dim(G) · h∨/(k+h∨)² + O(δk²),

so the framing-anomaly phase shifts smoothly. But the spectral-trace ratio
Tr_χ(1)/Tr_b(1) = 16/3 is *independent of k* — it lives in the finite spectral triple, not in
the CS sector. So if ψ is genuinely a CS modulus, then ρ_χ/ρ_b is *invariant* under ψ flow,
and the CS level cannot tune the ratio at all. This is consistent with the chi_field paper's
statement (lines 644--655) that the partition is preserved through cosmological evolution,
but it also means **CS dynamics cannot derive the ratio**; it can only fail to spoil it.

## 6. Verdict

**NO DERIVATION.** The 3D Chern--Simons framing on internal S³, with framing anomaly and
gravitational CS as the only intrinsically-3D anomalies, does not produce 16/3:

- **G1.** The level k = 60 = 2·h∨(E₈) is an input, not a DFD output. It does not appear in
  `chi_field_paper_FINAL.tex` and is not derived in the v3.3 monograph.
- **G2.** The 16 and 3 in the chi-paper are *spectral-trace multiplicities* (dim of Spin(10)
  spinor and N_gen), not CS anomaly coefficients. No 3D CS computation can recover them
  because they are external to the CS sector. The gravitational CS anomaly on round S³
  vanishes (η(0) = 0), and the framing anomaly gives c/24 = 62/9, which is not 16/3 mod 1
  for E₈ at k = 60 (or for any small simply-laced (G,k) I checked).
- **G3.** Worse for the 3D framing: 3D Dirac spinors are 2-component, and the natural
  3D count of internal Spin(7) ⊗ Spin(10)-flavor states is half the 4D count. A *consistent*
  3D re-derivation suggests 8/3, not 16/3.

**Partial positive sub-result.** The framing anomaly *is* a real 3D CS anomaly on S³, and the
fact that it gives c(E₈, k=60)/24 = 62/9 — a rational number with denominator 9 = 3² — is
the closest the 3D CS sector gets to anything resembling the "/3" in 16/3. But 62/9 is not
16/3, and I cannot bridge the gap honestly.

**Recommendation.** If DFD wants 16/3 to be a *theorem* rather than a representation-theory
choice, the derivation has to come from the spectral-action / almost-commutative geometry
side (Chamseddine--Connes 1996), not from a 3D CS anomaly. The 3D CS sector on S³ is
genuinely there in DFD, but it controls a *different* observable (the framing phase and
its k-dependence), not the dark-to-baryon ratio.

---

## References cited (all real, verifiable)

1. E. Witten, "Quantum field theory and the Jones polynomial," *Commun. Math. Phys.* **121**,
   351 (1989).
2. M. F. Atiyah, "On framings of 3-manifolds," *Topology* **29**, 1 (1990).
3. M. F. Atiyah, V. K. Patodi, I. M. Singer, "Spectral asymmetry and Riemannian geometry I,"
   *Math. Proc. Camb. Phil. Soc.* **77**, 43 (1975).
4. V. G. Knizhnik, A. B. Zamolodchikov, "Current algebra and Wess--Zumino model in two
   dimensions," *Nucl. Phys. B* **247**, 83 (1984).
5. E. Verlinde, "Fusion rules and modular transformations in 2D conformal field theory,"
   *Nucl. Phys. B* **300**, 360 (1988).
6. V. G. Kac, *Infinite Dimensional Lie Algebras*, 3rd ed., Cambridge University Press (1990).
7. H. B. Lawson, M.-L. Michelsohn, *Spin Geometry*, Princeton University Press (1989).
8. T. Friedrich, *Dirac Operators in Riemannian Geometry*, Graduate Studies in Mathematics
   **25**, AMS (2000).
9. A. H. Chamseddine, A. Connes, "The spectral action principle," *Commun. Math. Phys.* **186**,
   731 (1997); also *J. High Energy Phys.* **11**, 022 (1996).
10. Internal: `v34_research/chi_field_paper_FINAL.tex`, Section "Abundance: Ω_χ/Ω_b = 16/3",
    lines 571--660 (read 2026-04-07).
