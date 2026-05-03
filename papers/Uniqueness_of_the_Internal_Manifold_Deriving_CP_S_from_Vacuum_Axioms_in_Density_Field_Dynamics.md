---
source_pdf: Uniqueness_of_the_Internal_Manifold_Deriving_CP_S_from_Vacuum_Axioms_in_Density_Field_Dynamics.pdf
title: "Uniqueness of the Internal Manifold:"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Uniqueness of the Internal Manifold:
Deriving CP 2 × S 3 from Vacuum Axioms
in Density Field Dynamics
GARY THOMAS ALCOCK
(Dated: March 31, 2026)
Abstract. We prove that CP 2 × S 3 is the unique internal manifold for the spectral completion of Density Field Dynamics (DFD), under six physically motivated axioms on the
ψ-vacuum. The axioms encode chirality (an empirical fact about nature), multiplicative vacuum composition (a direct consequence of DFD’s core postulate P1), ground-state stability,
and minimality. They do not reference the Standard Model gauge group, fermion content,
or any coupling constant. The gauge group SU(3) × SU(2) × U(1), three generations, and
α−1 = 137.036 emerge as derived consequences. The product structure K = KC × KG is
not assumed but forced by the logical incompatibility of the chirality requirement (w2 ̸= 0)
with Lie-group parallelizability (w2 = 0) on a single connected manifold.

1. Introduction
Density Field Dynamics [1] is a scalar refractive-index theory of gravity defined by two
postulates:
P1. The optical refractive index of the vacuum is n = eψ , where ψ(x, t) is a scalar field
on flat R3,1 .
P2. Test bodies move under the conservative potential Φ = −c2 ψ/2.
The DFD microsector—which derives α = 1/137, the fermion mass spectrum, and the
MOND interpolation function µ(x) = x/(1+x)—requires a spectral completion on a product
geometry M = R3,1 × K, where K is a compact internal manifold.
Previous versions of DFD postulated K = CP 2 × S 3 . This paper derives it from six
physically motivated axioms.
2. The Six Vacuum Axioms
Axiom 1 (Spectral completion). The ψ-vacuum admits a UV completion via a spectral
action
(1)

SB = Tr f (D2 /Λ2 )

on a product geometry M = R3,1 × K, where K is a compact Riemannian manifold, D is
the Dirac operator on M , Λ is a UV cutoff, and f is a positive test function.
Motivation. The Chamseddine–Connes spectral action [2] is the canonical trace functional
in noncommutative geometry that produces both the Einstein–Hilbert gravitational action
and gauge kinetic terms from a single principle. DFD’s postulates P1–P2 emerge as the
weak-field limit of its a4 Seeley–DeWitt coefficient.
Date: March 31, 2026.
1

2

GARY THOMAS ALCOCK

Axiom 2 (Kähler chirality). At least one irreducible factor of K (in the de Rham decomposition) is a compact, simply-connected, Kähler–Einstein manifold with w2 ̸= 0 (spinc but
not spin).
Motivation. Nature violates parity [3]. Chiral fermions in 4D require a nonzero spinc Dirac
index on the internal space. The Hirzebruch–Riemann–Roch theorem—which computes
this
√ index∗as an integral of Chern characters—requires the Dirac operator to decompose as
2(∂¯ + ∂¯ ). This decomposition takes its cleanest canonical form in the Kähler setting,
where the spinc Dirac operator and the Dolbeault operator coincide. The condition w2 ̸= 0
(spinc -not-spin) ensures the index is non-trivially chiral: in the specific classification relevant
here (compact simply-connected positive-curvature Kähler–Einstein manifolds of complex
dimension ≤ 2), the spin candidates have vanishing chiral index, while the spinc -not-spin
candidate CP 2 does not.
Axiom 3 (Topological composition). At least one irreducible factor of K is a compact,
simply-connected Lie group manifold.
Motivation. DFD’s postulate P1 implies multiplicative composition of vacuum sectors:
ntotal = n1 ·n2 . This composition is associative, has an identity (n = 1, i.e., ψ = 0), and every
element has an inverse (n → 1/n). In the spectral completion (V1), the internal degrees of
freedom at each spacetime point form a fiber. For the vacuum composition law to be fiberwise consistent—meaning that the composition of two vacuum configurations at the same
spacetime point yields a valid vacuum configuration—the fiber must carry a group structure.
A compact connected manifold admitting a continuous associative multiplication with identity and inverses is a topological group; since the underlying space is a finite-dimensional
manifold, Hilbert’s fifth theorem [11] implies that it is a Lie group. Simple-connectedness
ensures the group is its own universal cover, so the composition has no topological ambiguity. V3 is the DFD-specific bridge from the multiplicative vacuum-composition law in P1
to an internal topological carrier of that composition. It is well-motivated within DFD but
remains an axiom, not a tautology; in a different theory without multiplicative refractive
composition, V3 would not apply.
Axiom 4 (Stability). K is compact and simply-connected. Every irreducible factor in its
de Rham decomposition is Einstein with positive Ricci curvature.
Motivation. The Einstein condition Ric = λ g (λ > 0) is the critical point of the spectral
action at fixed volume—the vacuum ground state. A non-Einstein K would be unstable
under Ricci flow and would relax to the Einstein point.
Axiom 5 (Minimality of dimension). dim(K) is the minimum compatible with Axioms 1–4
and the existence of chiral zero modes (nonzero spinc Dirac index).
Motivation. Each additional dimension introduces potential moduli that must be stabilized.
The minimal-dimension vacuum has the cleanest low-energy spectrum.
Axiom 6 (Minimality of topology). At fixed dimension, K has the minimum second Betti
number b2 (K) compatible with Axioms 1–5.

UNIQUENESS OF THE INTERNAL MANIFOLD

3

Motivation. Each independent 2-cycle supports an independent harmonic 2-form, hence
an independent gauge modulus. Minimizing b2 ensures the vacuum carries no unnecessary
internal flux degrees of freedom.
Remark 2.1 (Axiom content). Axioms 1–6 do not reference the Standard Model gauge group,
fermion representations, hypercharge assignments, or any coupling constant. Their physical
sources are:
• V1: the spectral action framework—standard in noncommutative geometry [2];
• V2: parity violation—an empirical fact [3], combined with the mathematical requirement that the spinc Dirac index factorizes cleanly (Kähler condition);
• V3: fiber-wise consistency of the multiplicative vacuum-composition law n = eψ —a
direct consequence of DFD’s postulate P1 combined with the spectral completion V1;
• V4: vacuum ground-state stability—a standard physical requirement;
• V5, V6: parsimony applied to dimension and topology—standard in physics.
3. Derivation
3.1. Step 0: Product structure is forced.
Lemma 3.1 (Forced product decomposition). The factors required by Axioms 2 and 3 must
be distinct irreducible components of K. In particular, K is not irreducible.
Proof. All compact simply-connected Lie groups are parallelizable: they admit a global frame
of left-invariant vector fields, so T G ∼
= G × Rn is trivial. Therefore w1 (G) = w2 (G) = 0 for
any compact simply-connected Lie group G.
Axiom 2 requires w2 ̸= 0 on the Kähler–chirality factor. Since w2 = 0 on any Lie group factor, the Kähler–chirality factor cannot be the Lie group factor. They are distinct irreducible
components.
By Axiom 4, K is compact and simply-connected. The de Rham decomposition theorem [9]
guarantees that K splits uniquely (up to order) as a Riemannian product of irreducible
factors:
(2)

K = K1 × K2 × · · · × Kr .

At least one factor (call it KC ) satisfies Axiom 2, and at least one distinct factor (call it KG )
satisfies Axiom 3.
□
3.2. Step 1: The chirality factor is CP 2 .
Lemma 3.2 (Classification of Kähler–chirality factors). Let X be a compact, simply-connected,
Kähler–Einstein manifold with positive scalar curvature and w2 (X) ̸= 0. Then dimR (X) ≥ 4,
and the unique such manifold of minimal real dimension with b2 = 1 is X = CP 2 .
Proof. Real dimension 2 (complex dimension 1). The compact simply-connected Kähler 1folds are the Riemann surfaces of genus 0, i.e., CP 1 ∼
= S 2 . But S 2 is spin (w2 (S 2 ) = 0), so
it violates w2 ̸= 0. Excluded.
Real dimension 4 (complex dimension 2). The compact simply-connected Kähler–Einstein
surfaces with c1 > 0 are classified. By Tian [4] and Tian–Yau [5], the del Pezzo surfaces
admitting Kähler–Einstein metrics are determined by the Matsushima–Lichnerowicz obstruction [6, 7] (the automorphism group must be reductive) and the Tian–Yau α-invariant:

4

GARY THOMAS ALCOCK

Surface

b2

KE metric?

w2

Status

CP 2
1 ✓ (Fubini–Study) H ̸= 0
Admitted
CP 1 × CP 1
2
✓ (product)
0
Spin; excluded by w2 ̸= 0
CP 2 #CP 2
2
× (Matsushima)
̸= 0
No KE metric exists
2
2
3
× (Matsushima)
̸= 0
No KE metric exists
CP #2CP
2
2
CP #kCP , k = 3, . . . , 8 k+1
✓ (Tian–Yau)
̸= 0
Excluded by V6 (b2 > 1)
The critical exclusion: CP 2 #CP 2 does not admit a Kähler–Einstein metric. This
is the Matsushima–Lichnerowicz theorem [6, 7]: a necessary condition for a compact Kähler
manifold to admit a Kähler–Einstein metric with c1 > 0 is that its automorphism group
be reductive. The automorphism group Aut(F1 ) of F1 = CP 2 #CP 2 (the first Hirzebruch
surface) contains a unipotent radical and is therefore not reductive. No Kähler–Einstein
metric exists.
Remark 3.3 (Page metric exclusion). The Page metric [10] on CP 2 #CP 2 is Einstein but
not Kähler. Axiom 2 requires Kähler–Einstein, so the Page metric is excluded at the axiom
level, not by post hoc selection.
The del Pezzo surfaces CP 2 #kCP 2 for k = 3, . . . , 8 do admit Kähler–Einstein metrics [4],
but they have b2 = k + 1 ≥ 4, and are excluded by Axiom 6: CP 2 has b2 = 1, which is
strictly less.
Therefore CP 2 is the unique manifold satisfying Axiom 2 in real dimension 4 with minimal b2 .
□
Corollary 3.4. The Kähler–chirality factor in K is KC = CP 2 (dim = 4).
3.3. Step 2: The group factor is S 3 .
Lemma 3.5 (Classification of minimal Lie group factors). The unique compact simplyconnected Lie group of minimal positive dimension is SU(2) ∼
= S 3 (dim = 3).
Proof. The compact simply-connected Lie groups are classified by Cartan. Their dimensions
begin:
Group
SU(2)
SU(3)
Sp(4) ∼
= Spin(5)
G2

Rank Dimension
1
2
2
2

3
8
10
14

No compact simply-connected Lie group exists in dimension 1 (U(1) ∼
= S 1 is not simplyconnected) or dimension 2 (no Lie algebra of dimension 2 is both semisimple and compact;
the only 2-dimensional Lie algebras are the abelian R2 and the solvable aff(1), neither yielding
a compact simply-connected group). Therefore SU(2) ∼
= S 3 is the unique compact simplyconnected Lie group of minimum positive dimension.
□
Corollary 3.6. By Axioms 3 and 5, the Lie group factor is KG = S 3 (dim = 3).

UNIQUENESS OF THE INTERNAL MANIFOLD

5

3.4. Step 3: K = CP 2 × S 3 and nothing else.
Theorem 3.7 (Uniqueness of the internal manifold). Under Axioms 1–6, K = CP 2 × S 3 .
Proof. By Lemma 3.1, K has at least two irreducible factors: KC (satisfying Axiom 2) and
KG (satisfying Axiom 3).
By Corollary 3.4, KC = CP 2 (dimension 4).
By Corollary 3.6, KG = S 3 (dimension 3).
By Axiom 5 (minimize dim(K)):
(3)

dim(K) ≥ dim(KC ) + dim(KG ) = 4 + 3 = 7.

Any additional irreducible factor K3 would satisfy dim(K3 ) ≥ 1, giving dim(K) ≥ 8 > 7,
violating minimality.
Could the chirality factor have dim > 4? The next Kähler–Einstein spinc -not-spin option
is CP 3 (dim = 6), giving dim(K) ≥ 6 + 3 = 9 > 7. Excluded by Axiom 5.
Could the Lie group factor have dim > 3? The next option is SU(3) (dim = 8), giving
dim(K) ≥ 4 + 8 = 12 > 7. Excluded by Axiom 5.
Could a non-product 7-manifold satisfy all axioms? No. Axiom 3 requires a Lie group
factor; Axiom 2 requires a Kähler factor with w2 ̸= 0. All compact simply-connected Lie
groups are parallelizable, hence w2 = 0. These two requirements are incompatible on a single
connected manifold. The product decomposition K = KC × KG is forced (Lemma 3.1).
Verification of all axioms on K = CP 2 × S 3 :
• V1: CP 2 × S 3 is compact, Riemannian, spinc ; the spectral action is well-defined. ✓
• V2: CP 2 is Kähler–Einstein (Fubini–Study, Ric = 6g), with w2 = H ̸= 0. ✓
• V3: S 3 ∼
= SU(2) is a compact simply-connected Lie group. ✓
• V4: CP 2 is Einstein (Ric = 6g), S 3 is Einstein (Ric = 2g), both with positive Ricci
curvature. K is simply-connected (product of simply-connected spaces). ✓
• V5: dim(K) = 7, the minimum possible. ✓
• V6: b2 (K) = b2 (CP 2 )+b2 (S 3 ) = 1+0 = 1, the minimum possible for any K satisfying
V1–V5. ✓
Chiral zero-mode existence (consistency check). The spinc Dirac index on CP 2 × S 3 is
nonzero. By Künneth factorization [1, Theorem F.9], the index factors over the product.
With the canonical spinc structure on CP 2 and minimal-energy flux configuration on S 3 ,
the index equals 3, confirming chiral zero modes exist. This is a consistency check on the
derived manifold, not an input to the selection.
Therefore K = CP 2 × S 3 is the unique solution to Axioms 1–6.

□

4. What Emerges
Once K = CP 2 × S 3 is derived rather than postulated, the entire DFD microsector follows
with zero continuous free parameters:

6

GARY THOMAS ALCOCK

Output

Mechanism

Ref. in [1]

SU(3)×SU(2)×U(1)
Ngen = 3
α−1 = 137.036
µ(x) =√x/(1+x)
a0 = 2 α cH0
θ̄ = 0 (Strong CP)
Proton stability
9 fermion masses

Minimal (3, 2, 1) partition
|k3 · k2 · q1 | = |1·1·3|
Chern–Simons at kmax = 60
S 3 composition law
Scaling stationarity
Mapping torus dim = 8 (even)
π3 (S 3 ) = Z winding
Spinc exponents + A5 prefactors

Prop. XVII.1
Thm. F.13
Thm. K.1
Thm. N.8
Thm. N.14
Thm. L.3
Thm. F.17
App. K

5. Honest Assessment of Axiom Content
The six axioms do not reference the Standard Model, but they are not content-free:
• V2 imports an empirical fact: parity violation. This is observational input,
not SM-theoretical input. Any vacuum theory must accommodate it. The Kähler
requirement within V2 is motivated by the spectral action framework (V1): the index
computation factorizes cleanly in the Kähler setting.
• V3 is DFD-specific: V3 bridges the multiplicative vacuum-composition law in
P1 to an internal topological carrier of that composition via the fiber-wise consistency requirement of the spectral completion (V1). It is not a universal physical
requirement—it is specific to theories with n = eψ multiplicative refractive composition. Within DFD, it is well-motivated but remains an axiom, not a tautology.
• V6 serves as a tiebreaker: V6 is invoked only to exclude del Pezzo surfaces with
k ≥ 3 that admit Kähler–Einstein metrics. Without V6, CP 2 would still be the
preferred chirality factor by V5 (all competitors have the same dimension but more
topology), but V6 makes the exclusion explicit rather than implicit.
The derivation is not assumption-free. It is assumption-minimal : six qualitative physical
requirements produce a unique topological answer from which 30+ quantitative predictions
follow.
6. Conclusion
Theorem (Uniqueness of the internal manifold). Under Axioms V1–V6, the internal manifold in the spectral completion of DFD is uniquely K = CP 2 × S 3 .
The key mathematical ingredients are:
(1) Incompatibility lemma: Lie groups are parallelizable (w2 = 0), so V2 (w2 ̸= 0)
and V3 (Lie group) force a product decomposition. This is derived, not assumed.
(2) Matsushima–Lichnerowicz obstruction: CP 2 #CP 2 does not admit a Kähler–
Einstein metric, killing the only non-trivial competitor to CP 2 in dimension 4. This
is a classical theorem [6], not a new postulate.
(3) Cartan classification: SU(2) ∼
= S 3 is the unique compact simply-connected Lie
group of minimum positive dimension. This is textbook.
(4) Dimensional arithmetic: 4 + 3 = 7 leaves no room for additional factors.
Section XVIII.B.d of [1] stated: “The only genuinely open theoretical question is the origin
of the CP 2 × S 3 topology itself.”

UNIQUENESS OF THE INTERNAL MANIFOLD

7

Under V1–V6, the answer is: six physical requirements on the ψ-vacuum—spectral completion, Kähler chirality, multiplicative composition, ground-state stability, and two minimality
conditions—admit exactly one solution. Whether those six axioms are themselves derivable
from deeper principles is a separate question; what this paper establishes is that they suffice
to uniquely determine K, eliminating the postulational status of the internal manifold.
References
[1] G. Alcock, “Density Field Dynamics:
A Complete Unified Theory,” v3.3 (April 2026),
doi:10.5281/zenodo.18066593.
[2] A. H. Chamseddine and A. Connes, “The spectral action principle,” Commun. Math. Phys. 186, 731
(1997).
[3] C. S. Wu, E. Ambler, R. W. Hayward, D. D. Hoppes, and R. P. Hudson, “Experimental test of parity
conservation in beta decay,” Phys. Rev. 105, 1413 (1957).
[4] G. Tian, “On Calabi’s conjecture for complex surfaces with positive first Chern class,” Invent. Math.
101, 101–172 (1990).
[5] G. Tian and S.-T. Yau, “Kähler–Einstein metrics on complex surfaces with c1 > 0,” Commun. Math.
Phys. 112, 175–203 (1987).
[6] Y. Matsushima, “Sur la structure du groupe d’homéomorphismes analytiques d’une certaine variété
kählérienne,” Nagoya Math. J. 11, 145–150 (1957).
[7] A. Lichnerowicz, “Sur les transformations analytiques des variétés kählériennes compactes,” C. R. Acad.
Sci. Paris 244, 3011–3013 (1957).
[8] N. Hitchin, “Compact four-dimensional Einstein manifolds,” J. Diff. Geom. 9, 435–441 (1974).
[9] G. de Rham, “Sur la réductibilité d’un espace de Riemann,” Comment. Math. Helv. 26, 328–344 (1952).
[10] D. N. Page, “A compact rotating gravitational instanton,” Phys. Lett. B 79, 235–238 (1978).
[11] D. Montgomery and L. Zippin, Topological Transformation Groups (Interscience, New York, 1955).
Independent Researcher, Los Angeles, CA, USA
Email address: gary@gtacompanies.com

