---
source_pdf: Mach_s_Principle_in_Density_Field_Dynamics__An_Interpretive_and_Phenomenological_Consolidation.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Mach’s Principle in Density Field Dynamics:
An Interpretive and Phenomenological Consolidation
Gary Alcock1, ∗
1

Independent Researcher, Los Angeles, CA, USA
(Dated: April 2026)

Density Field Dynamics (DFD) [9], a scalar refractive theory of gravity on flat R3 with matter
acceleration a = (c2 /2)∇ψ, contains a sharp, empirically testable structural
identity: the galactic
√
transition acceleration a⋆ is tied to the cosmic Hubble rate by a⋆ = 2 α cH0 , where α is the finestructure constant. The empirical coincidence a0 ∼ cH0 has been flagged in the MOND literature
for decades without derivation; DFD promotes it to a consequence of S 3 topology, pinning the
local galactic crossover
√ scale to the cosmic expansion rate. The program-grade epoch-by-epoch
extension a⋆ (z) = 2 α cH(z) predicts a drift in the radial-acceleration-relation normalization with
redshift, of magnitude a⋆ (z=1)/a⋆ (0) ≃ 1.79 in a ΛCDM parameterization of H(z) (used purely as
an observational parameterization, not an ontological commitment) and ≃ 2.83 in DFD’s matteronly ψ-screen cosmology. This is falsifiable by JWST and DESI high-redshift galactic kinematic
samples and is the headline handle of the paper.
We situate this prediction in Machian language. The Newtonian-limit Green’s function on flat R3
makes local gravitational response an explicit linear functional of the cosmic density fluctuation, realizing Mach 3 in its weak form; we note explicitly that this functional is formally indistinguishable
from Newtonian gravity and that DFD-specific Machian content enters only through the nonlinear regime and the global determination of a⋆ . The external-field-effect structure of [9] provides
secondary environment-dependent phenomenology at the cluster-galaxy level, program-grade in numerical magnitude. We distinguish theorem-grade from program-grade claims throughout. Against
the Bondi–Samuel [12] taxonomy, DFD satisfies Mach 3, Mach 10, and effectively Mach 8; partially
satisfies Mach 1, Mach 2, Mach 6; fails Mach 4, Mach 5, Mach 7, Mach 9. We do not claim that
DFD proves Mach’s principle. DFD rejects Mach 9 at the ontological level but retains a Machian
correspondence at the level of observables: the operationally preferred frame, the ψ rest frame, is
dynamically determined by cosmic matter, while the flat-R3 kinematic substrate remains absolute.

CONTENTS

I. Introduction

2

II. DFD structure relevant to Mach’s principle

2

III. The gravitational response functional
A. Linearization and the Newtonian Green’s
function
B. Cosmic and local decomposition
C. Deep-MOND regime: nonlinear response
D. Inertial mass in the loading background
√
IV. The structural identity a⋆ = 2 α cH0
A. The cosmic origin of a⋆
B. Numerical check

3
3
3
4
4
4
4
5

V. Bondi–Samuel taxonomy
5
A. Mach 0: the cosmic frame
5
B. Mach 1: G as a dynamical field
6
C. Mach 2: an isolated body has no inertia
6
D. Mach 3: local inertial frames are determined
by cosmic matter
6
E. Mach 4: spatial closure
6
F. Mach 5: zero total energy-momentum
6

∗ gary@gtacompanies.com

G. Mach 6: inertial mass from global matter
H. Mach 7: no space without matter
I. Mach 8: Ω = 4πGρ̄/3H 2 is of order unity
J. Mach 9: no absolute elements
K. Mach 10: unobservability of rigid motions
L. Summary

6
6
6
7
7
7

VI. The preferred-frame question
A. The ψ rest frame as a dynamical object
B. Comparison with absolute-space theories
C. Residual absolute content

7
7
8
8

VII. Comparison with Brans–Dicke

8

VIII. Empirical Machian predictions
A. Redshift evolution of a⋆
B. Environment-dependent inertia
C. Wide binaries: supporting example, not
headline falsifier

8
8
9
10

IX. Falsifiers

10

X. Conclusion

11

References

11

2
I.

INTRODUCTION

Mach’s principle is the idea that the inertia of local
matter is determined by the total matter content of the
universe. Mach’s criticism of Newton’s bucket experiment [1] rejected absolute space and attributed centrifugal effects to the relative motion of the water with respect to “the fixed stars and other heavenly bodies.”
Einstein took this seriously in the construction of general relativity [2] but later concluded that GR does not
realize Mach’s principle in any straightforward sense, a
verdict reinforced by the existence of vacuum solutions
(Schwarzschild, Minkowski, Kerr) in which the metric is
nontrivial despite the absence of matter [3].
The question of whether any theory of gravity can be
genuinely Machian has divided the community for a century. Barbour and Bertotti [4, 5] developed relational dynamics as a framework in which Mach’s principle is built
in from the start. Sciama’s inertial induction model [6]
attempted to compute local inertia as a gravitational effect of distant matter. Brans and Dicke’s scalar-tensor
theory [7] was explicitly motivated by Mach’s principle
and produces a Newton constant that depends on the
local scalar field value. Yet each of these faces genuine difficulties: relational dynamics has no empirically
successful realization, Sciama’s induction requires a preferred frame, and Brans–Dicke in the observationally viable large-ω limit is effectively indistinguishable from GR
and therefore inherits GR’s Machian ambiguity.
Density Field Dynamics [9] takes a different approach.
The theory is formulated on flat Euclidean R3 with time
as an external parameter. A scalar field ψ(x, t) called
the loading sets the optical refractive index n = eψ and
determines matter acceleration through
a=

c2
∇ψ.
2

The static field equation is
 


|∇ψ|
8πG
∇· µ
∇ψ = − 2 ρm ,
a⋆
c

(1)

through Eq. (3), and an environment-dependent inertial
response through the external-field-effect (EFE) treatment of the unified theory [9]. The purpose of the paper
is to organize these elements into a Machian reading, tag
which Bondi–Samuel [12] propositions they satisfy, and
extract the empirical predictions that are sharpest in that
language. Mach’s principle does not generate DFD. It
is a downstream interpretation of already-derived DFD
content, and we treat it as such throughout. The benefit is that the predictions that emerge from this reading,
particularly the redshift evolution of a⋆ , survive even for
a reader who does not accept the Machian framing, since
they are structural consequences of Eq. (3).
A note on grade. Within DFD [9], claims are tiered
as Theorem, Derived, or Conjectured / Program. We respect that discipline here. The Newtonian inertia functional (Section III) is theorem-grade: it is elementary
linear PDE theory applied to Eq. (2) in the
√ µ → 1 limit.
The epoch-by-epoch promotion a⋆ (z) = 2 α cH(z) (Section VIII) is program-grade: it follows from Eq. (3) only
under the additional cosmological assumption that the
identity holds at every epoch, which in turn depends on
the ψ-screen cosmology of [9]. The EFE prediction for
cluster-vs-field rotation curves (Section VIII B) is also
program-grade: the EFE structure is in the unified theory, but the quantitative percent-level estimate given
here is an order-of-magnitude scaling, not a derivation.
Section II sketches the DFD structure needed for what
follows. Section III constructs the Green’s function
and derives the inertia functional. Section IV reinterprets Eq. (3) as a Machian statement. Section V evaluates DFD against the Bondi–Samuel taxonomy [12].
Section VI addresses the preferred-frame tension. Section VII contrasts with Brans–Dicke. Section VIII
presents three empirical Machian predictions. Section IX
lists the falsifiers. Section X concludes.

II.

(2)

with µ(x) = x/(1 + x) derived from S 3 topology [9], a⋆
an acceleration scale tied to the cosmic expansion by the
structural identity
√
a⋆ = 2 α cH0 ,
(3)
and ρm ordinary matter density. This is structurally the
AQUAL equation of Bekenstein and Milgrom [10], placed
on flat space with ψ primitive and the four-dimensional
metric derived.
The thesis of this paper is narrower than “DFD proves
Mach’s principle” and broader than “DFD is incidentally
Machian.” We claim that DFD has an operationally
Machian sector, inherited from its already-established
flat-space scalar refractive structure, and that this sector
admits a clean Green’s-function description in the Newtonian limit, a structurally cosmic galactic transition scale

DFD STRUCTURE RELEVANT TO MACH’S
PRINCIPLE

For completeness we record the DFD elements used
below.
The scalar loading field ψ(x, t) is dimensionless and
defined on flat Euclidean three-space. It sets the optical
refractive index n = eψ , so light propagates according to
the eikonal of ds̃2 = −c2 dt2 /n2 +dx2 . Matter is governed
by the physical metric with gtt = −c2 e−ψ , giving redshift
1 + z = eψ/2 , and by Eq. (1) for acceleration. The two
metric structures coincide on the spherically symmetric
exterior in the µ → 1 regime but are distinct objects in
general.
The interpolation function µ(x) = x/(1 + x) is derived
from the S 3 -composition law of refractive loading [9]. It
has limits µ(x) → 1 for x ≫ 1 (Newtonian) and µ(x) → x
for x ≪ 1 (deep-MOND, radial
acceleration relation).
√
The crossover scale a⋆ = 2 α cH0 ≈ 1.2 × 10−10 m s−2
matches Milgrom’s a0 phenomenologically and is derived

3
in the unified theory rather than fitted. The dimensionless argument of µ is |a|/a⋆ , where a = (c2 /2)∇ψ; in the
ψ formulation this reads c2 |∇ψ|/(2a⋆ ). The compressed
notation µ(|∇ψ|/a⋆ ) appearing in some DFD references
is understood in this convention.
Matter density ρm ≥ 0 is the only source on the righthand side of Eq. (2). There is no dark matter, no cosmological constant, no new field. The “dark” phenomenology at galactic and cosmic scales arises entirely from the
nonlinear response of ψ to ordinary matter together with
the optical effects of the resulting refractive-index distribution on light propagation (the ψ-screen cosmology of
[9]).

B.

Cosmic and local decomposition

Write the total density as
ρm (x, t) = ρ̄(t) + δρ(x, t),

where ρ̄(t) is the spatial average over a horizon volume
and δρ is the local deviation. The loading decomposes as
ψ(x, t) = ψ̄(t) + δψ(x, t),

THE GRAVITATIONAL RESPONSE
FUNCTIONAL

We construct the Green’s function for the linearized
field equation and exhibit local gravitational acceleration as an integral functional of the cosmic density fluctuation. This is a statement about the source of gravitational acceleration, not about the origin of rest-mass
inertia in the anti-Newtonian sense. The distinction matters for the Machian reading and we keep it explicit.
A.

Linearization and the Newtonian Green’s
function

In the Newtonian regime |∇ψ| ≫ a⋆ we have µ → 1
and Eq. (2) reduces to
∇2 ψ = −

8πG
ρm .
c2

(4)

This is Poisson’s equation with source coefficient 8πG/c2
rather than the Newtonian 4πG, because ψ couples to
acceleration through Eq. (1) with the factor c2 /2. The
Green’s function for the Laplacian on R3 with vanishing
boundary condition at infinity is the standard
G(x, x′ ) = −

1
.
4π|x − x′ |

The loading field is therefore
Z
2G
ρm (x′ ) 3 ′
ψ(x) = 2
d x.
c
|x − x′ |
Substituting into Eq. (1) gives
Z
x − x′ 3 ′
a(x) = −G ρm (x′ )
d x.
|x − x′ |3

(5)

(6)

(7)

This is the Newtonian gravitational acceleration. In the
µ → 1 limit DFD reduces to Newton, as it must, and
the Newtonian picture of inertia emerges with the gravitational force from all other matter fully specified by
Eq. (7).

(9)

with ψ̄ set by the cosmic boundary condition and δψ
satisfying
∇2 δψ = −

III.

(8)

8πG
δρ.
c2

(10)

The cosmic ψ̄(t) determines absolute clock rates and the
local optical environment; δψ determines local accelerations. Matter accelerates only in response to gradients:
∇ψ̄ = 0 by the homogeneity of the cosmic background,
so
a(x) =

c2
∇δψ(x).
2

(11)

Theorem III.1 (Gravitational response functional,
Newtonian regime). In the µ → 1 regime, the gravitational acceleration of a test particle at position x in the
DFD framework is the linear functional
Z
x − x′ 3 ′
d x
(12)
a(x) = −G δρ(x′ )
|x − x′ |3
of the cosmic matter-density fluctuation δρ. The homogeneous cosmic background ρ̄ drops out of the acceleration
because ∇ψ̄ = 0. The gravitational response at any point
is therefore sourced entirely by departures from cosmic
homogeneity.
Proof. Immediate from Eqs. (1), (10), and the identity
∇(1/|x − x′ |) = −(x − x′ )/|x − x′ |3 . The integral converges for any δρ with compact support or adequate decay at infinity.
Theorem III.1 is the Machian translation of the Newtonian limit of DFD: the gravitational response felt locally is a computable functional of cosmic δρ. This is the
Mach 3 content (inertial frames affected by the cosmic
distribution of matter) in the weak form that the Newtonian limit can support. It is not a derivation of rest-mass
inertia in the stronger anti-Newtonian sense: the inertial
term mc2 in the matter action survives the ψ → 0 limit,
so a test particle’s resistance to non-gravitational forces
does not vanish when the cosmic gravitational source is
removed. The content of Theorem III.1 is therefore:
• What is established: the gravitational acceleration at x is an explicit linear functional of δρ over
the past light cone, and the homogeneous background drops out.

4
• What is not established: that rest-mass inertia
vanishes when cosmic matter is removed. This is
Mach 2, which DFD only partially satisfies (Section V).
We flag this distinction here because conflating the two is
the most common overreach in Machian readings of scalar
theories, and we do not want it in ours. We go further: at
the level of formal structure, Eq. (7) is indistinguishable
from Newtonian gravity. The Green’s-function identity
we have written down does not by itself separate DFD
from Newton. The genuinely DFD-specific Machian content enters only when the Newtonian regime is extended:
(i) through the nonlinear response at |a| ≲ a⋆ , which replaces Eq. (7) with the AQUAL response of Eq. (13); and
(ii) through the global determination of a⋆ by the cosmic
Hubble rate via Eq. (3), discussed in Section IV. Theorem III.1 is the Mach 3 content that survives into the
Newtonian limit. It is necessary for the overall Machian
reading but not by itself sufficient to distinguish DFD
from Newton.

C.

Deep-MOND regime: nonlinear response

In the deep-MOND regime |∇ψ| ≪ a⋆ we have µ → x
and Eq. (2) becomes the quasi-linear

 2
8πG
c |∇ψ|
∇ψ = − 2 ρm .
(13)
∇·
2a⋆
c
This does not admit a linear Green’s function, but the inertia functional remains well-defined as a nonlinear operator a[ρm ]. For spherically symmetric sources of enclosed
mass M (r) the solution is
|∇ψ|2 =

4GM (r)a⋆
,
c4 r 2

(14)

giving
c2
|a(r)| = |∇ψ| =
2

r

GM (r)a⋆
,
r2

(15)

which reproduces the baryonic Tully–Fisher relation [14]
with a normalization fixed by a⋆ , not fitted. In the nonlinear regime, the inertial response remains an explicit
functional of the cosmic matter distribution, now through
the nonlinear operator inverse of Eq. (13). The Machian
content is preserved and sharpened: in the deep-MOND
regime, the crossover scale a⋆ is literally the cosmic Hubble rate times a topological constant (Section IV), so the
inertia functional’s nonlinear structure is set cosmically.

D.

Inertial mass in the loading background

The physical metric of DFD has gtt = −c2 e−ψ . A test
particle’s proper time is dτ = e−ψ/2 dt. The particle’s

action in the weak-field limit is
Z
S = −mc2 e−ψ/2 dt + O(v 2 /c2 ).

(16)

Expanding in small ψ,
S ⊃ −mc2


Z 
ψ ψ2
1− +
+ · · · dt,
2
8

(17)

which gives an effective Newtonian Lagrangian L =
1
2
2
2 mv − mΦ with Φ = −c ψ/2, consistent with Eq. (1).
The rest-mass term −mc2 is independent of ψ at leading order. However, the frequency of any internal clock
(e.g., an atomic transition) is set by ψ̄, so measurable
mass ratios across cosmic epochs depend on the cosmic
loading history. This is the DFD realization of Mach 1
(“the gravitational constant is a dynamical field”) in a
weakened form: fundamental masses in natural units are
fixed, but the ratio of a laboratory atomic frequency to
c2 evolves with ψ̄(t). We return to this in Section VIII.

IV.

√
THE STRUCTURAL IDENTITY a⋆ = 2 α cH0

The single sharpest Machian statement in DFD is
Eq. (3). It ties the local acceleration scale at which
galactic dynamics depart from Newtonian behavior to
the cosmic expansion rate. This subsection reinterprets
the derivation in Appendix N of the unified theory [9] as
a Machian result.
a. Scope note. For the purposes of this paper,
Eq. (3) is treated as an input identity established in [9].
We sketch its cosmic-boundary origin below for completeness and because that origin is what makes the identity
Machian rather than coincidental, but our phenomenological predictions (Sections VIII, IX) do not require the
reader to endorse the full derivation chain of [9], which
separately involves the α−1 = 137.036 derivation from
Chern–Simons quantization on S 3 , the µ(x) = x/(1 + x)
composition law, and the larger CP 2 × S 3 topological
framework. A reader who accepts Eq. (3) as given and
grants that it licenses epoch-by-epoch extrapolation obtains the full observational content of this paper. The
upstream derivation chain is a separate matter adjudicated in the unified review.

A.

The cosmic origin of a⋆

The interpolation function µ(x) = x/(1 + x) is derived from a composition axiom on S 3 : when two loading contributions combine, their effect on the refractive
environment follows a saturation-union law. This fixes
the functional form uniquely and produces the scale a⋆
as the unique acceleration where the response transitions
from linear to logarithmic. The value of a⋆ is set by the
cosmic boundary condition on ψ̄.

5

2

a(0) = G

(a)

(x0) x0/|x0|3 d 3x0

1

test
particle

0
1
2
3

2

0

x (arbitrary units)

3

y (arbitrary units)

y (arbitrary units)

3

2

2

Vanishing-matter limit
(b) m = 0 everywhere

1

test
particle

0
1
2

a=0

0

no preferred frame

3

2

0

x (arbitrary units)

2

FIG. 1. Machian content of DFD. (a) Local acceleration at a test particle’s location is an integral functional of the cosmic
matter distribution. Blue arrows schematically weight each source by the Newtonian kernel 1/|x′ |2 ; in DFD this is an exact
statement (Theorem III.1). (b) In the vanishing-matter limit ρm → 0, the loading field ψ → 0 identically, and no preferred
frame survives. DFD’s “absolute” flat-R3 substrate is dynamical in this Machian sense.

At the homogeneous cosmic level, integrating Eq. (2)
over a horizon-sized volume with density ρ̄ and using the
Friedmann-like relation H02 = (8πG/3)ρ̄c in DFD’s optical cosmology [9] yields
√
(18)
a⋆ = 2 α cH0 .
√
The factor of α is fixed by the Chern–Simons level
structure on S 3 that also produces the fine-structure constant α−1 = 137.036 [9]. The factor of 2 arises from the
normalization of Eq. (1).

becomes a consequence of the theory’s topology, and this
is what licenses the
√ program-grade epoch-by-epoch promotion a⋆ (z) = 2 α cH(z) discussed in Section VIII.

Proposition IV.1 (Cosmic origin of the galactic transition scale). In DFD, the acceleration scale a⋆ at which
individual galactic rotation curves transition from Newtonian to deep-MOND behavior is fixed by the cosmic Hubble rate H0 through Eq. (18). A change in the global
expansion rate would change the local transition scale by
the same factor.

× 72.09 km s−1 Mpc−1

(19)

−10

(20)

Proposition IV.1 is the quantitative Machian statement available in DFD. The empirical coincidence
a0 ∼ cH0 has been noted in the MOND literature for
decades [11, 17, 18], and Milgrom himself has repeatedly
flagged the similarity between the galactic transition acceleration and the cosmic acceleration scale as suggestive of a deep connection. What DFD contributes is not
the observation of the coincidence; it is the promotion of
that coincidence to a derived structural identity through
the S 3 -topology derivation of a⋆ in Appendix N of [9].
Within MOND, a0 remains an empirical parameter and
the coincidence with cH0 is unexplained. Within GR,
there is no a0 at all. Within Brans–Dicke, there is no analog of a0 . DFD is the framework in which the coincidence

B.

Numerical check

Using H0 = 72.09 km s−1 Mpc−1 from DFD’s cosmological closure [9] and α−1 = 137.036:
p
a⋆ = 2 1/137.036 × 3 × 108 m s−1
= 1.19 × 10

−2

ms

.

Milgrom’s empirical a0 = 1.2 × 10−10 m s−2 from SPARC
fits [15]. Agreement at the percent level with zero free
parameters.
V.

BONDI–SAMUEL TAXONOMY

Bondi and Samuel [12] enumerated eleven distinct
propositions that have at various times been called
“Mach’s principle.” A responsible claim that a theory is
Machian must specify which propositions hold and which
do not. We apply the taxonomy to DFD.
A.

Mach 0: the cosmic frame

Mach 0: The universe, as represented by the average
motion of distant galaxies, does not rotate relative to local

6
inertial frames.
This is an empirical statement about our universe and
is not a property of a theory. DFD is consistent with
Mach 0 in the same trivial sense that GR is. Status:
consistent (empirical).

is controversial as a Machian requirement: Bondi and
Samuel themselves flagged it as tangential. Current cosmological data favor spatial flatness.

F.
B.

Mach 1: G as a dynamical field

Mach 1: Newton’s gravitational constant G is a dynamical field.
In DFD the gravitational constant is fixed by the topological identity GℏH02 /c5 = α57 [9]. Since H0 evolves
with cosmic time and α is a topological constant, the implied identification makes G a function of cosmic epoch in
the same way H0 is. This is a weakened form of Mach 1:
G is not an independent dynamical field, but it does depend on the cosmological state through a derived identity. Status: partially satisfied.

C.

Mach 2: an isolated body has no inertia

Mach 2: An isolated body in otherwise empty space has
no inertia.
In DFD, removing all matter sets ρm = 0 everywhere.
The homogeneous solution of Eq. (2) with zero source on
R3 and vanishing boundary conditions is ψ = 0 identically. The optical refractive index is n = 1 everywhere,
and the matter acceleration a = (c2 /2)∇ψ = 0 identically. An isolated body in this limit experiences no
gravitational acceleration, but this is not quite Mach 2:
the inertia in the sense of “resistance to acceleration by
non-gravitational forces” is set by the rest-mass term in
the action, which survives the ψ → 0 limit. So DFD is
closer to Mach 2 than GR is (because the gravitational
response vanishes, not just becomes undetermined), but
it does not literally make inertia vanish. Status: partially satisfied.

D.

Mach 3: local inertial frames are determined by
cosmic matter

Mach 3: Local inertial frames are affected by the cosmic motion and distribution of matter.
Theorem III.1 is the exact statement of Mach 3 in
DFD. Local inertial response is a computable integral
over the cosmic matter distribution. Status: satisfied
rigorously.

E.

Mach 4: spatial closure

Mach 4: The universe is spatially closed.
DFD is formulated on flat R3 , which is not compact.
The universe is not spatially closed in the substrate. Status: not satisfied. We note, however, that Mach 4

Mach 5: zero total energy-momentum

Mach 5: The total energy, angular momentum, and
linear momentum of the universe are zero.
In DFD,
global energy of the ψ field is
R
(c4 /8πG) |∇ψ|2 d3 x, which is manifestly nonnegative and nonzero for any nonempty matter distribution.
Mach 5 fails. Status: not satisfied. This is a property
shared with most theories; Mach 5 was never taken as a
strong constraint.

G.

Mach 6: inertial mass from global matter

Mach 6: Inertial mass is affected by the global distribution of matter.
In DFD, inertial mass in natural units (the rest-mass
term mc2 ) is not affected by the global distribution. But
the ratio of a laboratory-measured mass (e.g., via atomic
spectroscopy) to the cosmic reference frequency is set by
ψ̄(t), so operationally measured masses evolve with cosmic history. This is a weakened form of Mach 6. Status:
partially satisfied.

H.

Mach 7: no space without matter

Mach 7: If you take away all matter, there is no more
space.
DFD has flat R3 as the fundamental arena regardless
of matter content. Status: not satisfied.

I.

Mach 8: Ω = 4πGρ̄/3H 2 is of order unity

Mach 8: The dimensionless combination Ω
4πGρ̄/3H 2 is a definite number, of order unity.
In DFD’s cosmological closure, the combination
ΩDFD ≡

4πGρ̄
∼ O(1)
3H02

=

(21)

√
holds as a consequence of the a⋆ = 2 α cH0 identity
combined with the empirical observation that galactic
kinematics sit at a ∼ a⋆ . The ψ-screen cosmology of [9]
further fixes the effective matter-energy composition so
that the observed late-time acceleration is reinterpreted
as an optical bias, with Ωm ≈ 1 in the underlying matter
budget. We do not claim Ω ∼ O(1) as a direct theorem of the local field equation; it is a consistency condition within DFD’s cosmological closure, which itself
is program-grade in [9]. Status: effectively satisfied
within DFD cosmological closure.

7
J.

Mach 9: no absolute elements

Mach 9: The theory contains no absolute elements.
DFD’s flat R3 substrate is absolute in the sense that
its geometry is not dynamical. This is the single clearest
failure of DFD against a standard Machian requirement.
Status: not satisfied in the substrate metric. Section VI addresses the defense: while the substrate is absolute, the operationally meaningful frame (the ψ rest
frame) is dynamically determined by matter content, so
Mach 9 is satisfied at the level of physically observable
structure.

K.

Mach 10: unobservability of rigid motions

Mach 10: Overall rigid rotations and translations of a
system are unobservable.
DFD is translation- and rotation-invariant on flat R3 .
A rigid translation or rotation of the entire matter distribution (including the cosmic background) produces the
same physical configuration. Status: satisfied.

L.

Summary

Table I summarizes the results.
TABLE I. DFD’s status on the Bondi–Samuel Machian propositions.
Prop.

Statement

Status

Mach 0 Cosmic non-rotation
empirical
Mach 1 G dynamical
partial
Mach 2 Isolated body inertial
partial
Mach 3 Inertial frames cosmic
satisfied
Mach 4 Spatial closure
no
Mach 5 Zero total energy
no
Mach 6 Mass from global matter
partial
Mach 7 No space without matter
no
Mach 8 Ω ∼ O(1)
effective (closure)
Mach 9 No absolute elements
no (substrate)
Mach 10 Rigid motions unobservable satisfied

DFD is not uniformly Machian. It is rigorously
Machian on the propositions that carry empirical content (Mach 3, Mach 8) and on the structural identities
(Mach 10). It fails on the metaphysical propositions
(Mach 4, Mach 5, Mach 7, Mach 9 at the substrate level)
that would require a geometrically dynamical spacetime.
For comparison, GR satisfies only Mach 4 and Mach 10
unambiguously and is contested or partial on Mach 1 and
Mach 3. Brans–Dicke adds partial satisfaction of Mach 1.
DFD strictly dominates both on the empirically contentful propositions.

VI.

THE PREFERRED-FRAME QUESTION

The strongest objection to calling DFD a Machian theory is the absolute character of flat R3 . This section addresses the objection.

A.

The ψ rest frame as a dynamical object

The substrate metric of DFD is δij dxi dxj , an absolute
quantity. To prevent confusion at the outset, we distinguish two different “frame” concepts:
• The kinematic frame structure is the affine
structure on the flat substrate. It exists as long as
the substrate exists, which is always. An observer
can always label events with Cartesian coordinates,
measure distances, and define straight-line trajectories. This is the “stage” that DFD shares with
Newtonian and aether theories.
• The operationally preferred frame is the frame
in which ∇ψ = 0 on average (the ψ rest frame),
coinciding on cosmological scales with the cosmic
microwave background rest frame [9]. This is the
frame physical observers actually measure: it is the
frame in which clock rates are uniform, refractive
index is isotropic, and accelerations of free test bodies vanish. This frame is determined by the cosmic
matter distribution through the field equation (2).
The Machian defense of DFD is about the second
frame, not the first. We do not claim DFD eliminates
kinematic structure; that claim would belong to a fully
relational theory (Barbour). We claim that the operationally preferred frame, the one physics is actually done
in, is dynamically determined by cosmic matter rather
than being an externally imposed primitive of the theory.
Change the matter distribution, and the ψ configuration
changes, and the operationally preferred frame changes
with it. In the limit ρm → 0 everywhere, ψ → 0 everywhere, and the operationally preferred frame becomes
degenerate: no physical observable distinguishes one inertial frame from another. The kinematic structure of R3
persists, but without a ψ field sourced by matter, nothing
in the theory picks out one inertial frame as privileged.
This is distinct from Newtonian mechanics, where absolute space is the preferred frame independent of matter.
In DFD, the preferred frame is a dynamical shadow of the
cosmic matter distribution. It is, in the Machian sense,
“determined by the distant stars.”
Proposition VI.1 (Dynamical preferred frame). In
DFD, the CMB-aligned rest frame is not a primitive element of the theory but is determined by the cosmic matter
distribution through the field equation (2). In the limit
of vanishing cosmic matter, the operationally preferred
frame becomes undefined and all inertial frames become
observationally equivalent. The kinematic structure of

8
the flat-R3 substrate persists but carries no observable
content in this limit.
Proposition VI.1 is the Machian defense of DFD. The
substrate provides a stage, and the stage is absolute in
the Mach 9 sense; we do not dispute this. What we
claim is narrower: the “frame” that physical observers
use is set by the contents of the stage, not by the stage
itself. Frame degeneracy in the no-matter limit is not
the same as the absence of kinematic structure, and we
do not claim the latter. This position is weaker than
Barbour’s best-matching relationalism [4], which eliminates even the stage, but stronger than GR’s treatment,
in which the metric is dynamical but its generic solutions
(including Minkowski as a vacuum) define operationally
preferred frames without reference to matter.
To state the position in one sentence: DFD rejects
Mach 9 at the ontological level but retains a Machian
correspondence at the level of observables. This is the
position the paper defends, no weaker and no stronger.

B.

Comparison with absolute-space theories

Newtonian gravity in its standard formulation has absolute space and absolute time, both independent of matter. Aether theories of electrodynamics postulated a preferred frame (the aether rest frame) that was likewise independent of matter. These are genuinely non-Machian.
DFD resembles these theories in having a fixed spatial
manifold, but the resemblance is misleading. In Newtonian gravity the inertial frames are defined with respect
to absolute space; in DFD the inertial frames are defined
with respect to ψ, which is sourced by matter. Remove
matter from Newtonian gravity and absolute space persists with all its inertial structure. Remove matter from
DFD and the theory’s physical content collapses to trivial
Lorentz invariance on a featureless background.

C.

Residual absolute content

The honest accounting requires acknowledging what
remains absolute. The dimension of the substrate (three
spatial, one temporal) is fixed. The topology (R3 , or
more precisely the larger structure CP 2 × S 3 × R3 × R
in the full theory of [9]) is fixed. The flat metric on
the substrate is fixed. These are absolute elements in
Mach 9’s sense. A fully relational theory would have to
make even the dimension and topology emergent, and no
such theory currently exists in a viable empirical form.
DFD’s claim is that among empirically viable theories,
its remaining absolute content is minimal, and the dynamical content is as Machian as possible consistent with
reproducing known phenomenology. This is a defensible
but not irresistible position.

VII.

COMPARISON WITH BRANS–DICKE

Brans–Dicke theory [7] was the first serious attempt to
build a Machian theory of gravity. The action is


Z
√
ω
1
SBD =
d4 x −g ϕR − g µν ∂µ ϕ ∂ν ϕ + Smatter ,
16π
ϕ
(22)
with ϕ a scalar field playing a role analogous to G−1 .
The Machian motivation was that ϕ should be sourced
by cosmic matter, so that the effective Newton constant
at any point is determined by the matter distribution.
Empirically, current solar-system tests require ω ≳
40000 [13], which drives Brans–Dicke toward GR. In this
large-ω limit the scalar field becomes effectively constant
and Brans–Dicke’s Machian content evaporates: the theory becomes observationally indistinguishable from GR,
and therefore no more Machian than GR is.
The structural differences from DFD are three.
Primitive object. Brans–Dicke has a dynamical
scalar ϕ coupled to the four-metric gµν , which is also
dynamical. DFD has only a scalar ψ on a fixed flat substrate; the four-metric is derived.
Field equation. Brans–Dicke couples ϕ linearly to
the trace of the stress-energy tensor through a wave
equation. DFD couples ψ nonlinearly to matter density
through the AQUAL equation (2) with the µ function
derived from topology.
Acceleration scale. Brans–Dicke has no characteristic acceleration and no galactic-scale anomaly in the
weak-field
limit. DFD has the transition scale a⋆ =
√
2 α cH0 , which is responsible for all galactic “dark matter” phenomenology without any dark matter.
The Machian content of DFD is quantitatively
stronger than Brans–Dicke’s in the following sense: in
Brans–Dicke at large ω, the local value of G depends
weakly on the cosmic matter distribution (suppressed by
1/ω); in DFD, the entire local inertial structure at low
acceleration depends on a⋆ , which is fully determined
by H0 . Where Brans–Dicke’s Machianism is vestigial,
DFD’s is operational.
VIII.

EMPIRICAL MACHIAN PREDICTIONS

We now derive three predictions that isolate the
Machian content of DFD from GR, standard MOND, and
Brans–Dicke.
A.

Redshift evolution of a⋆

The structural identity Eq. (3) is a relation between
local physics (a⋆ , measurable from galactic kinematics)
and cosmic physics (H0 , the expansion rate today). A
natural program-grade extension is to promote this identity epoch-by-epoch:
√
a⋆ (z) = 2 α cH(z).
(23)

9
Eq. (23) is not a direct consequence of the local field
equation (2). It requires the additional assumption that
the derivation of a⋆ given in Appendix N of [9], which
uses the cosmic horizon-scale integration of Eq. (2) at
z = 0, goes through unchanged at each earlier epoch
with H0 replaced by H(z). This is plausible within the
DFD cosmological framework but is program-grade content, not a theorem. We proceed with Eq. (23) as a
working hypothesis and treat observational tests of it as
tests of that promotion rather than of DFD itself. At
redshift z, the appropriate Hubble rate is the one at that
epoch. A note on ontology is needed here. DFD does not
accept the ΛCDM ontology: the ψ-screen cosmology of
[9] reinterprets the apparent late-time acceleration as an
optical bias and dispenses with dark energy. The numerical values we compute below from the ΛCDM functional
form of H(z) are therefore not ontological commitments.
We use ΛCDM purely as a well-constrained observational
parameterization of the Hubble rate through the redshift
range accessible to current surveys, in the same spirit
that a particle physicist might use the Standard Model
as a functional parameterization of collider cross sections
without endorsing every aspect of its interpretation. The
DFD matter-only evolution (1 + z)3/2 is also shown, and
the observational discriminator is the measured a⋆ (z),
not the chosen H(z) parameterization.
In
=
0.315, H(z)
=
p ΛCDM with Ωm
3
H0 Ωm (1 + z) + ΩΛ , giving
a⋆ (z)
≈ 1.79
a⋆ (0) ΛCDM

at z = 1.

(24)

In DFD’s ψ-screen cosmology the underlying matter content is effectively Ωm → 1 with no dark energy, so
H(z)/H0 = (1 + z)3/2 and
√
a⋆ (z)
= 2 2 ≈ 2.83
a⋆ (0) DFD

at z = 1.

(25)

Either way, a⋆ evolves with redshift at order unity across
the cosmologically accessible range. Figure 2 shows both
curves with the radial acceleration relation shifted accordingly.
Two important remarks.
Sign. a⋆ increases with redshift. This means the
MOND transition at high z happens at larger accelerations, and therefore at smaller radii for a galaxy of given
mass. High-redshift galaxies should look more Newtonian and less MONDian in the observable regime, because the crossover is pushed to inner radii.
Not a standard MOND prediction. Standard
MOND treats a0 as a fundamental constant. Milgrom
has speculated [18] that a0 might evolve with cosmic
epoch but has not derived the functional form. DFD
derives Eq. (23) as a structural identity, with no free parameters.
Observational status. High-redshift galactic kinematics are now accessible through near-infrared integralfield spectroscopy with the James Webb Space Telescope [19, 20] and through wide-field surveys such as

DESI [21]. A fit of the radial acceleration relation as
a function of redshift, looking for a drift in the transition acceleration with z, is the cleanest test. A measured
a⋆ (z) that is independent of redshift at the percent level
out to z ∼ 1 would falsify the Machian structural identity.
Proposition VIII.1 (a⋆ redshift scaling, program–
grade).
Under the program-grade promotion a⋆ (z) =
√
2 α cH(z) (Eq. (23)), the galactic transition acceleration evolves with cosmic epoch. This predicts a drift
in the radial-acceleration-relation normalization between
low-redshift and high-redshift galaxy samples: DFD with
this promotion predicts a non-null drift, standard MOND
(taking a0 constant) predicts a null, and GR+ ΛCDM
has no a0 parameter at all and so makes no corresponding prediction in this form. The non-null test discriminates DFD with the promotion from standard MOND;
the program-grade status of the promotion is the correct
interpretation of the test result.
B.

Environment-dependent inertia

In DFD, a galaxy’s internal dynamics depend on its
external ψ environment through the external field effect (EFE) treatment in Appendix V of [9], which inherits the AQUAL-type EFE structure of Bekenstein–
Milgrom [10, 17] applied to the DFD field equation. We
adopt the unified-paper notation directly: the total loading decomposes as ψtotal = ψint + ψext , and the interpolation function µ acts on the total-field argument |atot |/a⋆
where atot = (c2 /2)∇ψtotal . A non-negligible ∇ψext
pushes the effective µ at a given point toward 1 (more
Newtonian), relative to the isolated-galaxy value.
This is phenomenology, not new derivation; the EFE
content is already in [9]. What the Machian reading
adds is the interpretation: EFE is the Mach 3 signature visible at scales where neighboring structure contributes appreciably to ∇ψext . In cluster environments,
where the cluster-scale ψ gradient is comparable to a⋆ ,
the prediction is that rotation curves of cluster-member
galaxies sit closer to the Newtonian limit at fixed baryonic mass than rotation curves of matched field galaxies. A quantitative prediction requires solving Eq. (2)
with the cluster-plus-galaxy mass distribution; an orderof-magnitude scaling gives a fractional correction of order
|∇ψext |/(|∇ψint | + a⋆ ), which for typical cluster environments is at the several-percent level at galactic outskirts.
We flag this estimate as program-grade: the sign and the
existence of the effect follow from the EFE framework
in [9], but the numerical magnitude requires an honest
full-geometry solve that is not performed here.
Observational status. Cluster SPARC samples combined with field samples, selected at matched baryonic
mass, can isolate this effect. The SPARC database [16]
has galaxies in both environments but has not been reanalyzed for the Machian environment dependence. This
is a priority follow-up.

10

6
5

10 8

(a) JWST
DFD / DESI
-screen
( m =1)
accessible

Standard CDM
Standard MOND (null)

4
3

2.83

2

1.79

10 9

aobs (m s 2)

a (z) /a (0) = H(z)/H0

7

1
0.0 0.5 1.0 1.5 2.0 2.5 3.0

Redshift z

(b) z=0 (today)

z=1, CDM
z=1, DFD
Newtonian

10 10
10 11
10 12
a (0)

10 13

10 13 10 12 10 11 10 10 10 9 10 8

abar (m s 2)

√
FIG. 2. (a) Predicted evolution of the galactic transition acceleration a⋆ (z) = 2 α cH(z) in DFD, normalized to today.
Standard ΛCDM (red dashed) gives a⋆ (z=1)/a⋆ (0) ≈ 1.79; DFD’s ψ-screen cosmology with effective Ωm → 1 (blue solid) gives
≈ 2.83. Standard MOND treats a0 as a fundamental constant (black dotted,
p null hypothesis). (b) Consequent shift of the
radial acceleration relation at z = 1: deep-MOND accelerations increase by a⋆ (z)/a⋆ (0) at fixed baryonic acceleration abar .
JWST and DESI kinematic samples discriminate among the three hypotheses.

C.

Wide binaries: supporting example, not
headline falsifier

Wide binary stars at separations r ≳ 7 000 AU have
internal accelerations below a⋆ and sit in the MOND
regime of DFD. The external field effect from the Milky
Way (|∇ψext | ∼ 2a⋆ at the solar radius) partially
screens the MONDian behavior. Solving Eq. (2) in
the external-field-dominated limit with approximately
aligned gradients, the orbital velocity of the binary satisfies v 2 /r = (GM/r2 )/µext with µext = (|∇ψext |/a⋆ )/(1 +
|∇ψext |/a⋆ ) ≈ 0.67 at the solar radius, giving a velocity
enhancement over Newtonian of ≈ 1.22, or about 22%.
This matches the standard MOND expectation in this
regime.
We include this as a supporting example rather than a
headline Machian test, for two reasons. First, the prediction coincides with standard MOND at the leading order
accessible to GAIA DR3, so a positive detection does
not discriminate DFD from MOND, only MOND-class
theories from pure Newtonian behavior. Second, the observational situation is contested [22–25]: the result depends on selection cuts, quality flags, and contamination
treatment, and the community has not converged. The
Machian content that is DFD-specific enters only at subleading order: the quantitative value of a⋆ is fixed by
H0 in DFD but is a free parameter in standard MOND,
so a sufficiently precise wide-binary measurement combined with an independent H0 measurement would test
the DFD structural identity. This requires precision beyond the current GAIA DR3 samples. We therefore defer
wide binaries to a supporting role and keep the a⋆ (z) red-

shift evolution (Section VIII A) as the Machian headline.

IX.

FALSIFIERS

The Machian reading of DFD makes the following predictions, ordered by how tightly they discriminate between DFD with Machian content and the alternatives.
F1. a⋆ does not evolve with redshift (headline).
If high-redshift galactic kinematics from JWST or DESI
show an a⋆ that is constant to better than a few percent
out to z ∼ 1, the program-grade promotion Eq. (23) is
falsified and the structural identity Eq. (3) is reduced
to a coincidence holding only today. This decouples the
Machian reading from the empirical content of DFD.
F2. Cluster-member galaxies show no environmental signature. If at fixed baryonic mass and
gas fraction, the radial acceleration relation for clustermember galaxies is identical to the isolated-field relation
at better than the scale in Section VIII B, the EFE-based
Machian reading is falsified. This is weaker than F1
because the sign and existence of the effect are robust
within the DFD EFE framework; only the Machian interpretation of the shift is tested.
F3. Inertial anisotropy. In principle, a sufficiently
anisotropic cosmic matter distribution would produce an
anisotropic gravitational response at the observer’s location. Current anisotropies are too small to be detected;
if future experiments detected isotropy of the gravitational response to a precision below the expected cosmic
quadrupole, DFD’s Machian reading would be in tension.
F4. Direct dark matter detection. A new particle

11

Density Field Dynamics contains an operationally
Machian sector. The Newtonian-limit gravitational response is an explicit linear functional of the cosmic density fluctuation (Theorem III.1), realizing Mach 3 in
its weak form. The galactic transition scale is tied to
the cosmic
√ expansion rate by the structural identity
a⋆ = 2 α cH0 (Section IV), which is the empirically
sharpest Machian statement in the theory. The externalfield-effect structure in [9] gives environment-dependent
inertial response consistent with Mach 3 at the phenomenological level. DFD satisfies Mach 3, Mach 8, and
Mach 10 rigorously, partially satisfies Mach 1, Mach 2,
and Mach 6, and fails Mach 4, Mach 5, Mach 7, and
Mach 9. The failure on Mach 9 is real: flat R3 is absolute as a substrate. The defense (Section VI) is that the

operationally meaningful frame, the ψ rest frame, is dynamically determined by cosmic matter. This is weaker
than relationalism but stronger than GR’s Machian content.
We have been explicit throughout about what is
theorem-grade and what is program-grade.
Theorem III.1 is theorem-grade.
The
epoch-by-epoch
promo√
tion a⋆ (z) = 2 α cH(z) (Proposition VIII.1) is programgrade. The cluster-vs-field percent-level EFE estimate is
program-grade. We do not claim derivations we have not
performed.
The headline Machian test is the redshift evolution of
a⋆ , falsifiable by JWST and DESI kinematic surveys.
Cluster environmental dependence is a secondary test
with existing SPARC data. Wide binaries are a supporting example, not a discriminator against standard
MOND.
This is a consolidation paper, not a foundational one.
Mach’s principle does not generate DFD. DFD contains
enough operationally Machian structure to be worth
reading in this language, and that reading produces
sharpened empirical handles. On Newton’s bucket, DFD
answers that the water climbs the wall because the ψ
field, sourced by cosmic matter, defines the optical environment in which the water’s acceleration is measured.
This is not Newton’s absolute-space answer and it is
not Barbour’s relational answer. It is the answer that a
theory with a flat substrate, a matter-sourced refractive
field, and a derived galactic transition scale can honestly
give.

[1] E. Mach, The Science of Mechanics: A Critical and Historical Account of Its Development, Open Court, Chicago
(1893).
[2] A. Einstein, Prinzipielles zur allgemeinen Relativitätstheorie, Ann. Phys. 360, 241 (1918).
[3] H. Bondi, Cosmology, Cambridge University Press
(1952).
[4] J. B. Barbour and B. Bertotti, Mach’s principle and the
structure of dynamical theories, Proc. R. Soc. London A
382, 295 (1982).
[5] J. B. Barbour, Absolute or Relative Motion?, Vol. 1,
Cambridge University Press (1989).
[6] D. W. Sciama, On the origin of inertia, Mon. Not. R.
Astron. Soc. 113, 34 (1953).
[7] C. Brans and R. H. Dicke, Mach’s principle and a relativistic theory of gravitation, Phys. Rev. 124, 925 (1961).
[8] J. A. Wheeler, Mach’s principle as boundary condition
for Einstein’s equations, in Gravitation and Relativity,
H.-Y. Chiu and W. F. Hoffmann, eds., Benjamin, New
York (1964).
[9] G. Alcock, Density Field Dynamics:
A Complete Unified Theory, v3.4, Zenodo (April 2026),
doi:10.5281/zenodo.18066593 (concept DOI, alwayslatest).
[10] J. Bekenstein and M. Milgrom, Does the missing mass
problem signal the breakdown of Newtonian gravity?, Astrophys. J. 286, 7 (1984).

[11] M. Milgrom, A modification of the Newtonian dynamics
as a possible alternative to the hidden mass hypothesis,
Astrophys. J. 270, 365 (1983).
[12] H. Bondi and J. Samuel, The Lense–Thirring effect and
Mach’s principle, Phys. Lett. A 228, 121 (1997).
[13] B. Bertotti, L. Iess, and P. Tortora, A test of general
relativity using radio links with the Cassini spacecraft,
Nature 425, 374 (2003).
[14] S. S. McGaugh, J. M. Schombert, G. D. Bothun, and
W. J. G. de Blok, The baryonic Tully–Fisher relation,
Astrophys. J. Lett. 533, L99 (2000).
[15] S. S. McGaugh, F. Lelli, and J. M. Schombert, Radial
acceleration relation in rotationally supported galaxies,
Phys. Rev. Lett. 117, 201101 (2016).
[16] F. Lelli, S. S. McGaugh, and J. M. Schombert, SPARC:
Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves, Astron. J. 152, 157
(2016).
[17] B. Famaey and S. S. McGaugh, Modified Newtonian
Dynamics (MOND): Observational Phenomenology and
Relativistic Extensions, Living Rev. Relativ. 15, 10
(2012).
[18] M. Milgrom, The shape of “dark matter” halos of disk
galaxies according to MOND, Astrophys. J. Lett. 571,
L81 (2002).
[19] A. de Graaff et al., A remarkably high-mass, rotating
galaxy at z ≈ 7 observed with JWST, arXiv:2404.05683

consistent with CDM phenomenology would collapse the
entire DFD explanatory program, including the Machian
reading. This is a global falsifier of DFD, not specific to
the Machian content.
F5. H0 and a⋆ evolve differently. If independent
measurements of H(z) and a⋆ (z) show inconsistent evolution, the program-grade promotion Eq. (23) fails. This
is a refinement of F1 and is the cleanest quantitative test
of the Machian structural identity in its epoch-by-epoch
form.

X.

CONCLUSION

12
(2024).
[20] H. Übler et al., GA-NIFS: JWST/NIRSpec IFU observations of a redshift z ≈ 5.6 galaxy revealing fast rotation,
arXiv:2312.03589 (2024).
[21] DESI
Collaboration,
DESI
2024
results,
arXiv:2404.03002 (2024).
[22] I. Banik, C. Pittordis, W. Sutherland, B. Famaey, R.
Ibata, S. Mieske, and H. Zhao, Strong constraints on
the gravitational law from Gaia DR3 wide binaries, Mon.

Not. R. Astron. Soc. 527, 4573 (2024).
[23] C. Pittordis and W. Sutherland, Wide binaries from Gaia
EDR3: preference for GR over MOND?, Open J. Astrophys. 6, 4 (2023).
[24] X. Hernandez, Internal kinematics of Gaia DR3 wide
binaries: anomalous behaviour in the low acceleration
regime, Mon. Not. R. Astron. Soc. 525, 1401 (2023).
[25] K.-H. Chae, Breakdown of the Newton-Einstein standard
gravity at low acceleration in internal dynamics of wide
binary stars, Astrophys. J. 952, 128 (2023).

