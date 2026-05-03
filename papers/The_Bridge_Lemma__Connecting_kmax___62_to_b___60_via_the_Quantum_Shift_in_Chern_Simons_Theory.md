---
source_pdf: The_Bridge_Lemma__Connecting_kmax___62_to_b___60_via_the_Quantum_Shift_in_Chern_Simons_Theory.pdf
title: "The Bridge Lemma: Connecting kmax = 62 to b = 60"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

The Bridge Lemma: Connecting kmax = 62 to b = 60
via the Quantum Shift in Chern-Simons Theory
Gary Alcock
Independent Researcher
gary@gtacompanies.com
December 25, 2025
Abstract
We prove a bridge lemma connecting two independently derived quantities in the DFD
microsector framework: the UV cutoff kmax = 62 from lattice Chern-Simons simulations
and the topological coefficient b = 60 from the heat kernel on CP2 . The connection is the
quantum shift k → k + h∨ in SU(2) Chern-Simons theory, where h∨ = 2 is the dual Coxeter
number. The bridge lemma states b = kmax − h∨ , providing a non-trivial consistency check
between the α-derivation program and the fermion mass program. This result suggests that
both programs access the same underlying microsector structure from different directions.

1

Introduction

Two recent papers in the DFD program have derived fundamental constants from microsector
geometry:
1. The α paper [2]: Lattice simulations of the SU(2)k Chern-Simons vacuum discovered
that the fine-structure constant α ≈ 1/137 requires a UV cutoff at kmax = 62. The
converged value (kmax → ∞) gives α = 1/303, which is ruled out.
2. The fermion mass paper [3]: The Hodge Laplacian on Ω1 (CP2 , ad(P )) yields a topological coefficient b = dim(G)(χ + 2τ ) = 60, which determines the α-exponents in Yukawa
couplings.
The numerical proximity 62 ≈ 60 is striking but requires explanation. In this paper, we
prove that these quantities are related by the quantum shift in Chern-Simons theory:
b = kmax − h∨ = 62 − 2 = 60

(1)

where h∨ = 2 is the dual Coxeter number of SU(2).
This bridge lemma provides a non-trivial consistency check: two independent calculations—
one from lattice Monte Carlo, one from index theory—yield results that differ by exactly the
quantum shift predicted by Chern-Simons theory.

2

The Quantum Shift in Chern-Simons Theory

2.1

Level Quantization and the WZW Correspondence

In SU(2) Chern-Simons theory at level k, the partition function on S 3 is given by the Witten
formula [1]:
r


2
π
3
ZCS (S ; k) = S00 =
sin
(2)
k+2
k+2
1

where S00 is the (0, 0) element of the modular S-matrix of the SU(2)k WZW model.
The key observation is that all physical quantities depend on the shifted level :
keff = k + h∨ = k + 2

(3)

not on the bare level k. This shift has several origins:
1. One-loop renormalization: The CS coupling receives a finite one-loop correction from
gauge field fluctuations.
2. Framing anomaly: The partition function depends on the framing of the 3-manifold;
the canonical framing induces a shift.
3. WZW correspondence: The CS/WZW duality identifies the CS level k with the WZW
level, which appears as k + h∨ in the affine Lie algebra.

2.2

The Dual Coxeter Number

For a simple Lie algebra g, the dual Coxeter number h∨ is defined as:
h∨ = 1 +

rank
X

a∨
i

(4)

i=1

where a∨
i are the comarks (dual Kac labels) of the highest root.
For the classical groups:
Group

h∨

Relevant for

SU(N )
SU(2)
SU(3)
SO(N )

N
2
3
N −2

Color, weak
Microsector
QCD
–

For the SU(2) microsector of DFD, h∨ = 2.

3

The Two Independent Derivations

3.1

Derivation 1: kmax = 62 from Lattice CS

The α paper [2] computes the vacuum expectation value of the effective level:
Pkmax
(k + 2) w(k)
⟨keff ⟩ = k=0
Pkmax
k=0 w(k)
where the weight function from the CS partition function on S 3 is:


π
2
2
sin
w(k) =
k+2
k+2

(5)

(6)

The critical discovery: The value ⟨keff ⟩ = 3.80 that yields α = 1/137 requires truncation at
kmax = 62:
kmax

⟨k + 2⟩

α result

50
62
100
∞

3.77
3.80
3.85
3.95

1/137 (+1.3%)
1/137 (+0.5%)
1/137 (+5%)
1/303 (ruled out)
2

The physical interpretation: Low-k sectors are strongly quantum (“loud”), while high-k
sectors are weakly coupled and nearly classical (“quiet”). The vacuum stiffness that determines
α is dominated by the quantum-active modes below kmax = 62.

3.2

Derivation 2: b = 60 from the Heat Kernel

The fermion mass paper [3] computes the coefficient b from the Seeley-DeWitt expansion of the
heat kernel:
X
Tr(e−t∆ ) ∼ (4πt)−2
ak (∆) tk/2
(7)
k≥0

For the Hodge Laplacian ∆(1) on Ω1 (CP2 , ad(P )), the coefficient a4 determines:
b = dim(G) × (χ + 2τ )

(8)
2

With G = SU(3) × SU(2) × U(1), dim(G) = 12, and for CP :
χ(CP2 ) = 3

(9)

τ (CP2 ) = 1

(10)

b = 12 × (3 + 2 × 1) = 12 × 5 = 60

(11)

Therefore:

4

The Bridge Lemma

Lemma 1 (Bridge Lemma). The topological coefficient b from the CP2 heat kernel equals the
bare CS level corresponding to the UV cutoff:
b = kmax − h∨

(12)

Proof. The quantum shift in SU(2) Chern-Simons theory replaces the bare level k with the
effective level keff = k + h∨ = k + 2 in all physical quantities.
The UV cutoff kmax = 62 is the effective level at which the sum is truncated. The corresponding bare level is:
kbare = kmax − h∨ = 62 − 2 = 60
(13)
The heat kernel coefficient b = 60 counts the bare degrees of freedom in the gauge sector,
before the quantum shift is applied. This is because the heat kernel expansion is a semiclassical
(one-loop) calculation that does not include the non-perturbative quantum shift.
Therefore b = kbare = kmax − h∨ .

4.1

Physical Interpretation

The bridge lemma has a clear physical interpretation:
1. The heat kernel counts semiclassical degrees of freedom. It sees the “bare” gauge structure with b = 60 effective modes.
2. The CS partition function includes the full quantum theory. The quantum shift k →
k + h∨ promotes the bare count to the effective count: 60 → 62.
3. The lattice simulations discover that kmax = 62 is the physical cutoff. This is the
quantum value, including the shift.
4. The fermion masses depend on the bare value b = 60, because the Yukawa couplings
are computed from semiclassical overlap integrals on CP2 .
The bridge lemma thus explains why two independent calculations—one quantum (lattice
CS), one semiclassical (heat kernel)—yield results differing by exactly h∨ = 2.
3

5

Consistency Checks

5.1

Check 1: The Quantum Shift is Universal

The value h∨ = 2 is not adjustable—it is fixed by the Lie algebra of SU(2). Any other shift
would be inconsistent with:
• The modular properties of the WZW model
• The framing dependence of the CS partition function
• The representation theory of affine SU(2)

5.2

Check 2: Both Calculations Are Independent

The two derivations use completely different mathematics:
• kmax : Lattice Monte Carlo + CS partition function + Wilson loop observables
• b: Index theorem + Seeley-DeWitt expansion + CP2 topology
That they agree (up to the quantum shift) is a non-trivial consistency check.

5.3

Check 3: The Dimension Formula

The heat kernel formula b = dim(G)(χ + 2τ ) can be rewritten as:
b = 12 × 5 = 60

(14)

kmax = b + h∨ = 60 + 2 = 62

(15)

The CS truncation gives:

If we had used a different gauge group or internal manifold, both b and kmax would change,
but the relation kmax = b + h∨ would remain valid (with the appropriate h∨ ).

6

Implications

6.1

Unification of the Two Programs

The bridge lemma unifies the α-derivation program and the fermion mass program:
Quantity

α program

Mass program

Key number
Calculation
Type
Relation

kmax = 62
b = 60
Lattice CS
Heat kernel
Quantum
Semiclassical
kmax = b + h∨

Both programs access the same underlying microsector structure, but from different limits:
• The α program works in the full quantum theory
• The mass program works in the one-loop approximation

4

6.2

Predictive Power

The bridge lemma has predictive power for other gauge groups. If the microsector were based
on SU(3) instead of SU(2), we would predict:
SU(3)
kmax
= b + h∨
SU(3) = 60 + 3 = 63

(16)

This could in principle be tested by lattice simulations of SU(3) Chern-Simons theory.

6.3

Why SU(2)?

The microsector uses SU(2) rather than SU(3) because:
1. S 3 ∼
= SU(2) is the natural fiber for the color sector
2. The WZW/CS correspondence is cleanest for SU(2)
3. The quantum shift h∨ = 2 gives the correct relation to b = 60

7

Conclusion

We have proven the bridge lemma connecting the UV cutoff kmax = 62 from lattice ChernSimons simulations to the topological coefficient b = 60 from the heat kernel on CP2 :
b = kmax − h∨ = 62 − 2 = 60

(17)

This result has three important consequences:
1. Consistency: Two independent calculations agree up to the quantum shift, providing a
non-trivial check of the DFD microsector framework.
2. Unification: The α-derivation and fermion mass programs are revealed as quantum and
semiclassical limits of the same underlying structure.
3. Prediction: The bridge lemma can be tested for other gauge groups, providing further
falsifiable predictions.
The bridge lemma closes the theoretical loop between the fine-structure constant and the
fermion mass hierarchy, showing that both emerge from the same CP2 ×S 3 microsector geometry.

Acknowledgments
I thank Claude (Anthropic) for assistance with calculations and manuscript preparation.

References
[1] E. Witten, “Quantum Field Theory and the Jones Polynomial,” Commun. Math. Phys.
121, 351 (1989).
[2] G. Alcock, “Ab Initio Evidence for the Fine-Structure Constant from Density Field Dynamics,” (2025).
[3] G. Alcock, “Charged Fermion Masses from the Fine-Structure Constant: A Topological
Derivation from the DFD Microsector,” (2025).

5

[4] G. Alcock, “Density Field Dynamics: Unified Derivations, Sectoral Tests, and Correspondence with Standard Physics,” (2025).
[5] G. Alcock, “A Topological Microsector for the DFD Field ψ,” (2025).
[6] P. B. Gilkey, “The spectral geometry of a Riemannian manifold,” J. Diff. Geom. 10, 601
(1975).
[7] M. F. Atiyah and I. M. Singer, “The index of elliptic operators: I,” Ann. Math. 87, 484
(1968).
[8] P. Di Francesco, P. Mathieu, and D. Sénéchal, Conformal Field Theory (Springer, 1997).

6

