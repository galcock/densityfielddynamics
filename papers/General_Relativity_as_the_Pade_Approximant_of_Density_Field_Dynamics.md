---
source_pdf: General_Relativity_as_the_Pade_Approximant_of_Density_Field_Dynamics.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

General Relativity as the Padé Approximant of Density Field Dynamics:
Refractive gravity on flat space and its relation to Schwarzschild geometry
Gary Alcock1
1

Independent Researcher∗
(Dated: April 15, 2026)

We show that general relativity arises as the simplest rational truncation of Density Field Dynamics (DFD) in the gravitational clock-rate sector. Define the lapse-squared scalar L(u) ≡ c2 /|gtt |, a
clock-rate / redshift observable, with u ≡ GM/(ϱc2 ). The isotropic-coordinate Schwarzschild form
of GR gives LGR (u) = [(1+u/2)/(1−u/2)]2 , while DFD’s exterior solution gives LDFD (u) = exp(2u).
The exact identity

2
LGR (u) = P1,1 (exp(u))
extends to a Padé hierarchy in which [Pm,m (exp(u))]2 = exp(2u) + O(u2m+1 ) for every m ≥ 1, with
each finite-m truncation carrying a Padé pole that recedes to infinity only as m → ∞. GR is the
m = 1 slot; DFD is the entire-function limit. The Schwarzschild horizon at r = 2GM/c2
is the Padé pole of the m = 1 truncation; DFD’s exponential has no finite pole and its µ → 1
exterior ψ(r) = 2GM/(c2 r) is everywhere finite, with r = 2GM/c2 appearing as a photon sphere
rather than a horizon. The two theories agree through O(u2 ) by construction — consistent with all
gravitational-redshift and clock observations to date and reproducing the post-Newtonian parameter
β = 1 — and first differ at O(u3 ), generating a ∼ 4.6% larger black-hole shadow. The identity is in
the lapse-squared scalar, which controls clock rates, redshift, the Newtonian limit, β, and horizon
structure; the spatial metric, ray-optics, and the PPN parameter γ are not its consequences and
are established separately for DFD via the physical metric in [8]. Several prior constructions also
produce exponential lapses (Papapetrou 1954, Yilmaz 1958, Dicke 1957, Puthoff polarizable vacuum
1999/2002, Broekaert 2008), so the Padé identity itself holds for any of them; what makes the present
statement an inter-theory reduction rather than a tautology is that DFD is not embedded inside
GR. The Yilmaz exponential, for example, is itself a GR solution interpretable as a wormhole with
exotic matter, whereas DFD’s flat-R3 elliptic field equation admits no throat and requires no exotic
matter. Current Event Horizon Telescope data on M87⋆ and Sgr A⋆ are consistent with both GR
and DFD at the present precision; the predicted ∼ 4.6% shadow excess is the proximal observational
discriminator.
I.

INTRODUCTION

The observational equivalence of general relativity
(GR) and competing metric theories at post-Newtonian
order is well-established [1, 2]. Within the refractive
tradition of gravity, a variety of constructions — from
Eddington’s 1920 optical-medium analogy [3] to Dicke’s
1957 variable-speed-of-light formulation [4] to Puthoff’s
polarizable vacuum [5, 6] and Broekaert’s scalar analog formulation [7] — produce weak-field refractive indices that match GR through at least linear order in
the gravitational potential. The exponential form n =
exp(2GM/rc2 ) has appeared multiple times in this literature. The purpose of this paper is to observe a specific
mathematical identity between GR’s isotropic-coordinate
Schwarzschild lapse-squared and the exponential lapsesquared of Density Field Dynamics (DFD), and to analyze its structural content.

∗ gary@gtacompanies.com

A.

Density Field Dynamics

DFD [8] is formulated on flat three-dimensional Euclidean space R3 with time as an external parameter.
The fundamental object is a dimensionless scalar field
ψ(x, t) called the loading. The optical refractive index is
nDFD (ψ) = eψ ,

(1)

and matter acceleration is
a = 21 c2 ∇ψ.

(2)

The static field equation is a nonlinear elliptic PDE on
R3 :
∇ · [µ(|∇ψ|/a⋆ ) ∇ψ] = −

8πG
ρm ,
c2

(3)

with µ an interpolation function, a⋆ an acceleration scale,
and ρm ordinary matter density [8]. Equation (3) is
structurally the AQUAL field equation of Bekenstein–
Milgrom modified-Newtonian-dynamics [11–13], with a⋆
identified with Milgrom’s a0 . It is not Einstein’s equation: the geometry of R3 is flat and fixed, there is no Einstein tensor, no Hilbert action, no dynamical 4-metric.

2
B.

The exponential form

The exponential form (1) is postulated on the basis of
a multiplicative composition axiom for refractive loading: when two loading fields ψ1 , ψ2 are superposed, their
refractive effects multiply, n(ψ1 + ψ2 ) = n(ψ1 ) n(ψ2 ).
Under continuity and measurability, Cauchy’s functional
equation implies n(ψ) = ekψ for some constant k [9].
The factor of 2 in nDFD (u) = exp(2u) below is fixed separately by normalization against observed gravitational
light bending.
Multiplicative composition is a DFD-specific constitutive postulate, not a universal feature of optical media. Series media compose additively via optical path
length, and effective-medium theories (Maxwell–Garnett,
Bruggeman) compose permittivity ϵ by volume averaging
rather than multiplying n [10]. The DFD postulate is
well-defined and testable but not inherited from classical
optics; the Padé identity below does not depend on its
derivation.

C.

Relation to prior refractive-gravity work

The exponential refractive form has a substantial prior
history. We distinguish DFD from each principal precedent before stating our result.
Yilmaz exponential metric [23, 24] and later work [25–
29]. This is a four-dimensional Lorentzian metric ds2 =
−e−2m/r c2 dt2 + e+2m/r (dr2 + r2 dΩ2 ), interpreted as a
solution of Einstein–Klein–Gordon equations with an antiscalar source. It is a solution within GR, not outside it. At the optical level its radial refractive index
is nYilmaz = e2m/r , matching DFD’s functional form; the
distinction is entirely ontological (see Sec. VI).
Dicke variable-speed-of-light [4]. Proposes a positiondependent index of refraction in otherwise flat spacetime,
reproducing weak-field GR predictions through PPN order. Differs from DFD in having no field equation analogous to (3) and in taking the speed-of-light variation as
primitive rather than as a derived consequence of a scalar
loading.
Puthoff polarizable vacuum [5, 6]. Introduces a vacuum dielectric function K = exp(2GM/rc2 ) that modifies speed, frequency, and ruler scales simultaneously,
on a flat background. Closest prior art to DFD in that
both are flat-background exponential refractive formulations. Distinguished from DFD by (a) derivation route:
PV from a scaled-ruler/scaled-clock heuristic, DFD from
Cauchy composition on ψ; (b) field equation: PV postulates the exponential directly, DFD has the nonlinear
elliptic (3) with MOND-type interpolation µ; (c) cosmological structure: DFD is embedded in a specific topological framework on CP 2 × S 3 yielding Standard-Model
parameters and α−1 from Chern–Simons level quantization [8].
Broekaert scalar analog [7]. Derives refractive formulations of gravity from variational principles on flat

backgrounds; specifically addresses PPN equivalence.
Broekaert’s construction is Lagrangian-first, DFD’s is
postulate-first via the composition axiom.
Optical-metric tradition. Gordon [14] introduced the
optical metric g̃µν = gµν + (1 − n−2 )uµ uν for light
propagation in moving or refractive media within GR.
Plebanski [15] developed the analogy between curved
spacetime and optical media. De Felice [16] and Perlick [17] consolidated these ideas; Ye and Lin [18] derived
the specific exponential weak-field form from GR in the
optical-medium analogy. DFD’s derived optical metric
g̃µν = diag(−c2 /n2 , 1, 1, 1) is conformally related to Gordon’s form with a flat reference metric, and serves the
same bookkeeping purpose. The distinction is that in
the Gordon–Plebanski tradition the optical metric is derived from a curved GR spacetime, whereas in DFD the
optical metric is a derived object on a fundamentally flat
R3 , with ψ as primitive.
Analog gravity [20–22]. A related but distinct program
in which emergent causal structure (horizons, trapped
surfaces) arises on a fundamentally flat substrate from
matter flow or refractive-index variation. The analoggravity precedent is important to DFD’s claim (Sec. V)
that a flat substrate admits no wormhole throat: such a
claim must be made explicitly about the spatial 3-metric,
not merely about the existence of a flat substrate, because analog constructions demonstrate that emergent
causal structure can exist on flat backgrounds.

D.

What this paper does

We observe a specific Padé-approximation identity between GR’s squared inverse-lapse and DFD’s exponential lapse-squared (Sec. II), analyze the order-by-order series agreement (Sec. III) and the strong-field divergence
(Sec. IV), distinguish the DFD ontology from Yilmaztype GR solutions (Secs. V–VI), and identify observational discriminants (Sec. VII). The Padé identity as a
named relation is, to our knowledge, novel; the exponential form itself is not.

II.
A.

THE PADÉ IDENTITY

DFD’s lapse-squared and refractive index

Around a spherically symmetric mass M , DFD’s exterior solution in the µ → 1 regime gives ψ(r) =
2GM/(c2 r). With u ≡ GM/(ρc2 ), where ρ denotes the
isotropic radial coordinate in GR and the flat-space radial coordinate in DFD, we have ψ = 2u on the exterior.
DFD’s matter-coupling (physical) metric has gtt =
−c2 e−ψ [8], so the lapse-squared scalar is
LDFD (u) ≡

c2
= eψ = exp(2u).
|gtt |

(4)

3
This is the redshift / clock-rate scalar of DFD’s matter sector and the natural counterpart, in DFD, of GR’s
lapse-squared. Independently, by Postulate P1 the optical refractive index is nDFD (u) = eψ = exp(2u), governing light propagation through the optical metric ds̃2 =
−c2 dt2 /n2 + dx2 . The lapse-squared LDFD and the refractive index nDFD are distinct physical quantities arising from different metrics in DFD’s two-metric structure,
but they coincide as functions of u on the exterior solution: LDFD (u) = nDFD (u) = exp(2u). The Padé identity below operates on LDFD (the lapse-squared); where
Sec. IV C uses n(r) = exp(2GM/(c2 r)), that refers to the
refractive index by P1, which on the exterior takes the
same numerical value.
B.

Padé approximant of exp

The [1, 1] Padé approximant of exp(x) about x = 0
is the unique rational function whose Taylor expansion
matches that of exp through order x2 :
P1,1 (exp(x)) =

C.

1 + x/2
.
1 − x/2

(5)

Isotropic Schwarzschild: scalar conventions

The Schwarzschild exterior in isotropic radial coordinate ϱ reads
ds2 = −A2 (ϱ) c2 dt2 + B 2 (ϱ) [dϱ2 + ϱ2 dΩ2 ],

(6)

with
A(ϱ) =

1 − u/2
,
1 + u/2


u 2
B(ϱ) = 1 +
.
2

(7)

which governs the gravitational redshift (clock frequency
ratios) and fixes the PPN parameter β through the O(u2 )
coefficient of gtt . By contrast, the PPN parameter γ lives
in the spatial metric gij and is not determined by the
lapse alone. Under this lapse-sector convention, DFD’s
LDFD (u) = exp(2u) and GR’s LGR (u) = [(1 + u/2)/(1 −
u/2)]2 are directly comparable as clock-rate ratios.
a. Note on DFD notation. A reader may worry
about an apparent collision between “n = eψ ” as DFD’s
optical refractive index (Postulate P1) and the lapsesquared scalar L = 1/A2 used in this paper. In DFD
these are distinct physical quantities arising from the
theory’s two-metric structure: the optical metric ds̃2 =
−c2 dt2 /n2 + dx2 governs light (Postulate P1, refractive
index n = eψ ), while the matter-coupling physical metric has gtt = −c2 e−ψ , giving lapse-squared L = c2 /|gtt | =
eψ . On the spherically symmetric exterior ψ = 2u, both
quantities take the same numerical form exp(2u), but
they are not the same physical object: n controls light
propagation, L controls clock rates. The Padé identity in
this paper is a statement about L, the clock-rate scalar;
where Section IV C uses n(r) = exp(2GM/(c2 r)) in describing the DFD exterior, that is the optical refractive
index by P1, which on the exterior coincides numerically
with L.
Under the Gordon ray-optics convention the GR refractive index for radial null geodesics is B/A = (1 +
u/2)3 /(1−u/2), whose Taylor series is 1+2u+ 47 u2 +· · · ;
this disagrees with DFD’s exp(2u) at O(u2 ) rather than
O(u3 ). The Padé identity we establish is specifically
a lapse-sector (clock-rate/redshift) identity; it is not a
ray-optics identity, and it does not by itself establish
agreement of light-bending or Shapiro-delay observables,
which involve the spatial metric. Full PPN agreement
between DFD and GR, including γ = 1, is established
separately using DFD’s physical metric in [8] § PPN and
is not a consequence of the present identity.

Several distinct refractive-index conventions are in use in
the literature; each corresponds to a different observable.
• Gordon ray-optics convention: nray = B/A, governing spatial ray-bending and the direction of photon propagation in a 3+1 split. This is the natural
convention in the Gordon–Plebanski optical-metric
tradition [14, 15, 17].
p
• Inverse-lapse convention: n = 1/ |gtt |/(−c2 ) =
1/A, governing clock rates and gravitational redshift. Used in phase-based PPN analyses [16, 19].
• Squared inverse-lapse:
n2 = 1/A2 , which
appears in phase-speed-squared expressions for
gravitational-redshift tests and in the PPN expansion of the tt metric component.
The Padé identity below uses the squared inverse-lapse
scalar,

2
c2
1 + u/2
2
1/A (u) ≡
=
,
(8)
|gtt |
1 − u/2

D.

The identity

2

LGR (u) = [P1,1 (exp(u))] .

(9)

The lapse-squared scalar of isotropic-coordinate
Schwarzschild is exactly the square of the [1, 1] Padé
approximant of DFD’s exponential. Figure 1 shows the
two functions and their relative difference.

III.

ORDER-BY-ORDER COMPARISON

Taylor expanding both forms about u = 0:
LDFD (u) = 1 + 2u + 2u2 + 43 u3 + 23 u4 + · · · ,
LGR (u) = 1 + 2u + 2u

2

+ 32 u3 + u4 + · · · .

(10)
(11)

4

GR = [P1, 1(exp(u))]2

100
Padé pole
(GR horizon)

30

10 2
10 4

Cassini precision

10 6

20
10
0
0.00

(b) Relative difference

102

| GR

lapse-squared (u)

40

(a) Functional forms
DFD = exp(2u)

DFD|/ DFD

50

10 8
10 10

0.25

0.50

0.75

1.00

1.25

u = GM/( c2)

1.50

1.75

2.00

10 12
0.00

0.25

0.50

0.75

1.00

1.25

u = GM/( c2)

1.50

1.75

2.00

FIG. 1. (a) DFD’s LDFD (u) = exp(2u) (blue) and GR’s LGR (u) = [P1,1 (exp(u))]2 (red dashed). The GR form has a pole at
u = 2 corresponding to the Schwarzschild horizon coordinate; DFD has no pole. (b) Relative difference |LGR − LDFD |/LDFD on
a logarithmic scale. Solar-system tests probe u ∼ 10−6 , where the difference is ∼ 10−19 ; neutron-star envelopes probe u ∼ 0.1;
EHT shadows u ∼ 0.3.

TABLE I. Taylor coefficients of LDFD and LGR through
O(u5 ).
order n
0
1
2
3
4
5

[un ]LDFD
1
2
2
4/3
2/3
4/15

[un ]LGR
1
2
2
3/2
1
5/8

difference
0
0
0
−1/6
−1/3
−43/120

TABLE II. Relative difference between GR and DFD lapsesquared scalars L(u).
u
10−6
10−2
10−1
0.30
0.50
1.00
→2

relative difference
∼ 10−19
∼ 10−7
∼ 10−4
4.6 × 10−3
2.2 × 10−2
2.2 × 10−1
→∞

IV.

The series agree through O(u2 ) and first diverge at O(u3 )
with coefficient difference 1/6. The O(u) and O(u2 ) coefficients of L = 1/A2 are set by the PPN expansion
of gtt , from which we read β = 1 for both theories. The
PPN parameter γ is determined by the spatial metric and
is not accessible from the lapse sector alone; for DFD,
γ = 1 follows from the physical metric gij = e+ψ δij and
is established in [8] § PPN, independently of the present
identity. Experimentally, γ − 1 = (2.1 ± 2.3) × 10−5
from Cassini [33] and β − 1 = (−4.5 ± 5.6) × 10−5 from
Hofmann–Müller [34] lunar laser ranging are both consistent with γ = β = 1.
As a Lorentz-invariant conservative scalar theory on
flat R3 , DFD also predicts the preferred-frame and
preferred-location parameters α1 = α2 = α3 = ξ = 0
and conservation parameters ζ1,2,3,4 = 0, matching all
ten-parameter PPN constraints [2] identically with GR
at post-Newtonian order. The detailed full-PPN derivation is given in [8].

system scale
solar surface
compact-star exterior
neutron-star envelope
photon-sphere region
Schwarzschild radius scale
inside Schwarzschild radius
Padé pole / GR horizon

STRONG-FIELD BEHAVIOR
A.

Numerical divergence

Table II lists representative relative discrepancies
|LGR − LDFD |/LDFD .

B.

The horizon as Padé pole

The Padé approximant has a simple pole at u = 2. In
isotropic coordinates this is ϱ = GM/(2c2 ); the isotropicto-Schwarzschild transformation r = ϱ(1 + u/2)2 maps
to r = 2GM/c2 , the Schwarzschild event horizon radius.
The function exp(2u) is entire; at u = 2 it takes the finite
value e4 ≈ 54.6.
a. Coordinate hygiene. The Padé comparison above
uses GR’s isotropic radial coordinate ϱ. The explicit
DFD exterior solution below is written in the flat-space
radial coordinate r of Euclidean R3 . The GR horizon at r = 2GM/c2 (Schwarzschild), the Padé pole at

5
ϱ = GM/(2c2 ) (isotropic GR), and the DFD photon
sphere at r = 2GM/c2 (flat R3 ) all sit at the same physical mass scale GM/c2 but in three distinct coordinate
charts.
C.

This is a clean strong-field discriminator: DFD predicts
a finite upper bound on gravitational-redshift signatures
from the innermost accretion regions of black holes, while
GR predicts none. AGN iron Kα lines and quasar line
profiles, which sample the innermost stable circular orbit
region, could in principle constrain this bound.

DFD’s exterior solution has no finite-radius
horizon
V.

In the strong-field µ → 1 regime, the vacuum field
equation (3) around a spherically symmetric mass M integrates to [8]
ψ(r) =

2GM
,
c2 r

2

n(r) = e2GM/(c r) ,

(12)

finite for every r > 0 and divergent only at r = 0. The
local phase speed c/n(r) is positive for all finite r > 0;
no finite-radius surface traps light. Applicability of the
µ → 1 approximation at the photon-sphere scale is controlled by a⋆ /aph ∼ 10−13 for M87⋆ -class supermassive
black holes (and smaller yet for stellar-mass); sub-µ → 1
corrections are negligible at astrophysical precision.
The radius r = 2GM/c2 appears in the DFD exterior
as the photon sphere, determined by the orbital condition
d[n(r)r]/dr = 0:
d h 2GM/(c2 r) i
2GM
DFD
.
e
r = 0 =⇒ rph
=
dr
c2

(13)

This is a surface of unstable circular photon orbits,
not a causal boundary. The critical impact parameDFD
2
2
GR
ter
√ is bcrit 2 = 2e GM/c 2 ≈ 5.44 GM/c , vs. bcrit =
3 3 GM/c ≈ 5.20 GM/c , yielding a 4.6% larger predicted shadow radius under the minimal exponential
completion [8]. At the photon sphere, ψ(rph ) = 1 exactly; extrapolation of the exterior solution to this point
strictly exits the formal ψ ≪ 1 domain, and a fully nonlinear solution may modify the numerical coefficient while
preserving the sign of the deviation.
D.

Gravitational redshift bounded at photon
sphere

A direct consequence of the finite lapse at the photon sphere: the maximum gravitational redshift for light
emitted by static observers near the DFD photon sphere
and received at infinity is set by the physical-metric lapsesquared LDFD = eψ , since matter clocks couple to the
physical metric. Thus
q
DFD
1 + zmax
= LDFD (rph ) = eψ(rph )/2 = e1/2 ,
(14)
giving
DFD
zmax
=

√

e − 1 ≈ 0.649,

(15)

whereas in GR the redshift diverges (z → ∞) for photons
climbing out of a potential well approaching the horizon.

NO WORMHOLE AND NO EXOTIC
MATTER

The principal prior alternative to GR that produces
the exponential refractive form is the Yilmaz metric [24],
interpreted by Boonserm, Ngampitipan, Simpson, and
Visser [30] as a traversable wormhole with exotic matter.
This section establishes that DFD’s fundamental flat-R3
formulation does not carry the wormhole or exotic-matter
interpretation.

A.

Yilmaz: wormhole throat at r = m

The Yilmaz exterior
ds2Yilmaz = −e−2m/r c2 dt2 + e+2m/r [dr2 + r2 dΩ2 ] (16)
has a curved 3-geometry on a constant-t slice: the spatial
2
metric is dlYilmaz
= e2m/r [dr2 + r2 dΩ2 ], giving the areal
radius RYilmaz (r) = r em/r . Differentiating, dR/dr =
em/r (1 − m/r) vanishes at r = m; the second derivative
there is positive (e/m), so r = m is a minimum with
Rmin = em ≈ 2.718 m. Both r → 0 and r → ∞ give
R → ∞, so r = m is a wormhole throat connecting two
asymptotic regions. Boonserm et al. [30] show that the
Einstein tensor of (16) requires a stress-energy tensor
violating the null energy condition at the throat. See
also Hochberg and Visser [31] and Visser’s systematic
treatment [32] of wormhole geometries and their energycondition violations.

B.

DFD: no throat in flat R3

DFD postulates flat Euclidean 3-space. The spatial
2
metric is dlDFD
= dr2 + r2 dΩ2 , giving areal radius
RDFD (r) = r and dR/dr = 1 for all r > 0. No critical point exists, so no throat exists on the fundamental
spatial slice.
a. Why analog gravity does not immediately refute
this. Analog-gravity constructions [20–22] demonstrate
that emergent causal structure can exist on fundamentally flat substrates: acoustic horizons trap phonons in
flowing fluids even though the laboratory spatial geometry is trivially flat. The claim above is therefore specifically about the spatial 3-metric of the DFD substrate, not
a universal flat-background claim. What does DFD’s derived optical metric g̃µν = diag(−c2 /n2 , 1, 1, 1) say? Its
spatial part is the same flat R3 , so the derived optical

6
areal-radius function is unchanged from RDFD (r) = r.
No throat arises in either the substrate or the optical
metric.
A stronger question — whether DFD could be reformulated in a conformally rescaled frame whose spatial
part resembles Yilmaz’s — is a matter of frame choice
and does not alter the physical dynamics on the flat substrate. We follow the analog-gravity convention of referring topological claims to the physical substrate metric.

C.

No exotic matter in the field equation

DFD’s field equation (3) is an elliptic PDE sourced by
ordinary matter density ρm ≥ 0. The energy density of
the ψ field is uψ = (c4 /8πG) W (|∇ψ|2 /a2⋆ ) with W (s) =
s − ln(1 + s), which reduces to uψ = (c4 /8πG)|∇ψ|2 in
the µ → 1 regime. Both W and its µ → 1 limit are
nonnegative, so uψ ≥ 0 for all configurations. There
is no Einstein tensor to balance against a stress-energy
tensor, no Hilbert action, and no requirement for energycondition-violating matter. Internal consistency of (3)
is a standard question for monotone elliptic operators,
resolved by standard PDE theory [8].

VI.

WHY GR IS A PADÉ APPROXIMANT OF
DFD SPECIFICALLY

The Padé identity, combined with the ontological
asymmetry, establishes DFD as a non-trivial candidate
for “the fundamental theory of which GR is an approximation.” The identity does not prove this selection —
only experiment can. Among the candidate exponential
theories surveyed, DFD is the one whose status as a Padé
parent of GR is not tautological.
Asymmetry statement. If reality follows DFD’s exponential, GR’s post-Newtonian success is mathematically inevitable at measured precision: the [1, 1] Padé
agrees with the exponential through O(u2 ), which covers all current clock-rate-based solar-system tests. Conversely, if reality follows GR strictly, DFD’s predictions disagree only at the strong-field scales probed by
Event Horizon Telescope observations and future precision gravitational-wave measurements. The distinction is
experimentally accessible; Sec. VII surveys the program.

A.

The Padé hierarchy: GR as m = 1, DFD as
m→∞

The [1, 1] identity (9) is the first nontrivial member
of an infinite hierarchy of rational approximants. For
each m ≥ 1, the diagonal [m, m] Padé of exp(u) is the
unique rational function of numerator and denominator
degrees both equal to m whose Taylor series matches
exp(u) through O(u2m ). Its square therefore satisfies


The Padé identity (9) relates GR’s squared inverselapse to exp(2u). Any theory whose lapse-squared (or
equivalent clock-rate scalar) takes the form exp(2u) will
satisfy the same Padé identity with GR. This includes
Yilmaz [24], Puthoff’s polarizable vacuum [5, 6], and
Broekaert’s scalar construction [7]. The Padé identity
is therefore not mathematically specific to DFD.
The statement “GR is the [1, 1] Padé approximant of
theory X” becomes physically meaningful, however, only
when theory X is outside GR — that is, when the statement expresses a genuine inter-theory reduction rather
than a tautology.
Yilmaz: the metric (16) is a solution of Einstein–
Klein–Gordon equations, embedded within GR. The
statement “GR is a Padé approximant of Yilmaz” is
therefore self-referential: it says GR approximates a particular GR solution, which is trivially true for any limit
procedure.
Puthoff polarizable vacuum: formulated outside standard GR, with a scaled-ruler/scaled-clock heuristic. The
Padé identity applies and expresses a genuine reduction,
but PV lacks a nonlinear field equation and a topological foundation; it is closer to an effective phenomenology
than a complete theory.
DFD: formulated on flat Euclidean R3 with a scalar
loading field, a nonlinear elliptic field equation (3) of
AQUAL type, and a topological foundation on CP 2 ×
S 3 [8]. Not a GR solution.

2
Pm,m (exp(u)) = exp(2u) + O(u2m+1 ).

(17)

Each successive m matches the exponential one Padé order further out in the lapse-sector scalar. This defines
a hierarchy of rational functions in u whose weak-field
expansions agree with exp(2u) to increasing order, not a
hierarchy of full metric theories: the lapse-squared scalar
does not determine the spatial metric, so the hierarchy
does not per se imply matching of ray-optics or spatialcurvature PPN content at higher orders.
a. The hierarchy explicitly. Table III lists the
matching order and first real pole location for m = 1
through 5. The [m, m] Padé of exp(u) has the closed
form
m  
X
m (2m − k)! k
Nm (u) =
u ,
(18)
k
(2m)!
k=0

Dm (u) = Nm (−u),

(19)

with Pm,m (exp(u)) = Nm (u)/Dm (u).
b. Interpretation: GR is the m = 1 case. The
identity (9) establishes that the squared inverselapse of isotropic-coordinate Schwarzschild equals
[P1,1 (exp(u))]2 . This positions Schwarzschild’s lapse
sector as the m = 1 element of the hierarchy (17). Every
finite-m truncation has its own lapse pole at finite u;
only the entire function — the m → ∞ limit — has no
pole at any finite u.

7
TABLE III. The Padé hierarchy of squared diagonal Padé
approximants of exp(u) in the lapse-squared scalar u =
GM/(ρc2 ). Each finite-m member is a rational function of
u whose Taylor expansion agrees with the target exp(2u)
through O(u2m ), with a Padé pole on or near the positive
real axis at the indicated location.
m Matches exp(2u) through

First real pole

O(u2 ) u = 2 (GR Schwarzschild)
O(u4 ) none (complex pair only)
O(u6 )
u ≈ 4.64
O(u8 ) none (complex pair only)
O(u10 )
u ≈ 7.29
..
..
.
.
exact (entire)
none (DFD)

1
2
3
4
5
..
.
∞

c. The m → ∞ limit recovers DFD. The sequence
of squared diagonal Padé approximants converges to the
entire function exp(2u) pointwise for all finite u and uniformly on any compact subset of the complex plane avoiding the poles of Pm,m [49]. In the limit:
lim

m→∞



lever separating the full exponential from all its rational
approximants.

2
Pm,m (exp(u)) = exp(2u) = LDFD (u).

(20)

Equation (20) is the precise sense in which GR is a special case of DFD: GR’s lapse-squared is the simplest
rational truncation of DFD’s exponential, and DFD is
the unique entire-function completion of that truncation.
The Schwarzschild horizon at u = 2 is the Padé pole of
the m = 1 truncation; higher-m truncations push their
poles outward; only the entire function exp(2u) has no
finite pole at all. GR occupies the m = 1 slot of a hierarchy whose m → ∞ limit is DFD.
d. Scope of the reduction. This identity operates on
a single scalar function of u, the lapse-squared (which,
on DFD’s exterior solution, coincides numerically with
the optical refractive index nDFD ). The hierarchy is not
a parameter limit of field equations: DFD’s elliptic PDE
on flat R3 and GR’s Gµν = 8πGTµν /c4 on a curved
Lorentzian 4-manifold are not connected by any singleparameter limit on either side. Full PPN agreement between DFD and GR — including the spatial-curvature
parameter γ = 1 and the ray-optics sector — is established separately via DFD’s physical metric gij = e+ψ δij
in [8], and is not a consequence of the present hierarchy.
e. Experimental implication. All gravitationalredshift and clock-rate observations to date are
consistent with the lapse-sector identity and with both
GR and DFD. The structural distinction is the absence
of a finite-radius horizon: the entire function exp(2u)
has no finite pole; every rational truncation does. The
black-hole shadow (Sec. VII) and the bounded gravitational redshift at the photon sphere (Sec. IV D) probe
this structural feature directly. The Padé hierarchy
recasts horizons as artifacts of rational truncation in the
lapse function; their absence in DFD is the empirical

VII.

OBSERVATIONAL CONSEQUENCES

A.

Black hole shadow: M87⋆ and Sgr A⋆

Using the explicit DFD exterior solution, the√critiGR
cal impact parameter ratio is bDFD
crit /bcrit = 2e/(3 3) ≈
1.046, giving a 4.6% larger geometric shadow than
Schwarzschild. For M87⋆ [35] with observed ring diameter 42 ± 3 µas, DFD predicts ∼ 43.9 µas (0.6σ consistency). For Sgr A⋆ [36, 37] with observed shadow diameter 51.8 ± 2.3 µas, DFD predicts ∼ 54.2 µas (∼ 1.1σ
tension). The shadow-deviation parameter δ defined by
Kocherlakota and Rezzolla [39] gives δDFD ≈ +0.046,
compatible with VLTI’s constraint (δ ∈ [−0.17, 0.01]) at
∼ 1.4σ and with the Keck constraint at ∼ 0.5σ. Under current data, M87⋆ mildly favors DFD while Sgr A⋆
mildly favors GR; the combined tension is at most ∼ 1σ
and does not statistically discriminate. Next-generation
facilities [38, 40, 41] are expected to reach the required
precision.

B.

Gravitational-wave ringdown and echoes

DFD’s horizonless exponential profile admits a modified near-photon-sphere potential that in principle supports reflected modes, distinct from exotic compact objects with sharp reflecting walls (gravastars, boson stars,
fuzzballs) [42]. A DFD-specific prediction would be
an effective reflectivity |R|2 determined by the gradient
of ψ near the photon sphere rather than by a postulated surface reflector. Because the exponential profile
is smooth, the expected reflectivity is substantially lower
than the ECO-class signatures already constrained by
LVK searches [43–46]. A quantitative DFD echo spectrum requires the full nonlinear ψ profile around a compact source and is deferred to numerical studies. No echo
signals have been observed to date.

C.

Gravitational-wave memory and distinguishing
tests

Both DFD and GR reduce to linearized gravity in the
far-field. The Christodoulou memory effect in DFD, computed from time-dependent sources of ψ on flat R3 , agrees
with the GR result to the precision probed by LIGOband stellar-mass binary black-hole sources [8, 47]. Measurements sensitive to wormhole topology [48] or exoticmatter throat structure would distinguish Yilmaz-type
scenarios from both DFD and GR; DFD predicts no such
signatures.

8

General relativity is the simplest rational truncation of
Density Field Dynamics in the gravitational clock-rate
sector. The isotropic-coordinate Schwarzschild squared
inverse-lapse equals the squared [1, 1] Padé approximant
of DFD’s exponential exactly; the Schwarzschild horizon at r = 2GM/c2 is the Padé pole of that m = 1
truncation. DFD is the entire-function completion of
the same hierarchy, free of any finite-radius pole, with
r = 2GM/c2 appearing as a photon sphere rather than a
horizon. The two theories agree through O(u2 ) — reproducing the post-Newtonian coefficient β = 1 and consistent with all current gravitational-redshift observations
— and first differ at O(u3 ). The PPN parameter γ and
ray-optics observables, which depend on the spatial metric, are established separately for DFD via its physical
metric [8].
The exponential refractive form is not novel in isolation: constructions due to Papapetrou, Yilmaz, Dicke,

Puthoff, and Broekaert all reach exponential forms. The
Padé identity relating GR’s squared inverse-lapse to any
such exponential is, to our knowledge, novel as a named
relation. Its structural content is that an entire function
(the exponential) is being approximated by a rational
function (the Padé) of order [1, 1], with the approximation’s pole appearing as the approximated form’s horizon
coordinate.
Among the candidate exponential theories, DFD is the
one outside GR whose Padé relation to GR expresses
a non-tautological inter-theory reduction: Yilmaz is a
GR solution, DFD is not. This ontological asymmetry is
what makes the statement “GR is a Padé approximant
of DFD” physically meaningful.
Strong-field observations — black-hole shadow sizes,
gravitational-wave ringdown spectra, near-horizon spectroscopic signatures of bounded gravitational redshift
(zmax ≈ 0.65 in DFD vs. z → ∞ in GR) — offer the
empirical program to distinguish DFD from GR. Current
data is consistent with both at the ∼ 1σ level.

[1] C. M. Will, The Confrontation between General Relativity and Experiment, Living Rev. Relativ. 17, 4 (2014).
[2] C. M. Will, Theory and Experiment in Gravitational
Physics, 2nd ed. (Cambridge University Press, 2018).
[3] A. S. Eddington, Space, Time and Gravitation (Cambridge University Press, 1920).
[4] R. H. Dicke, Gravitation without a Principle of Equivalence, Rev. Mod. Phys. 29, 363 (1957).
[5] H. E. Puthoff, Polarizable-Vacuum (PV) representation
of general relativity, arXiv:gr-qc/9909037 (1999).
[6] H. E. Puthoff, Polarizable-vacuum approach to general
relativity, Found. Phys. 32, 927 (2002).
[7] J. Broekaert, A Spatially-VSL Gravity Model with 1-PN
Limit of GRT, Found. Phys. 38, 409 (2008).
[8] G. Alcock, Density Field Dynamics:
A Complete Unified Theory, v3.3, Zenodo (April 2026),
doi:10.5281/zenodo.19391659; concept DOI (alwayslatest): doi:10.5281/zenodo.18066593.
[9] J. Aczél, Lectures on Functional Equations and Their Applications (Academic Press, 1966).
[10] M. Born and E. Wolf, Principles of Optics, 7th ed. (Cambridge University Press, 1999).
[11] M. Milgrom, A modification of the Newtonian dynamics
as a possible alternative to the hidden mass hypothesis,
Astrophys. J. 270, 365 (1983).
[12] J. Bekenstein and M. Milgrom, Does the missing mass
problem signal the breakdown of Newtonian gravity?, Astrophys. J. 286, 7 (1984).
[13] B. Famaey and S. S. McGaugh, Modified Newtonian
Dynamics (MOND): Observational Phenomenology and
Relativistic Extensions, Living Rev. Relativ. 15, 10
(2012).
[14] W. Gordon, Zur Lichtfortpflanzung nach der Relativitätstheorie, Ann. Phys. 377, 421 (1923).
[15] J. Plebański, Electromagnetic Waves in Gravitational
Fields, Phys. Rev. 118, 1396 (1960).
[16] F. de Felice, On the gravitational field acting as an optical

medium, Gen. Relativ. Gravit. 2, 347 (1971).
[17] V. Perlick, Gravitational Lensing from a Spacetime Perspective, Living Rev. Relativ. 7, 9 (2004).
[18] X.-H. Ye and Q. Lin, A simple optical analysis of
gravitational lensing, J. Opt. A 10, 075001 (2008),
arXiv:0711.0633.
[19] J. Evans, K. K. Nandi, and A. Islam, The OpticalMechanical Analogy in General Relativity: New Methods
for the Paths of Light and of the Planets, Am. J. Phys.
64, 1404 (1996).
[20] W. G. Unruh, Experimental black-hole evaporation?,
Phys. Rev. Lett. 46, 1351 (1981).
[21] M. Visser, Acoustic black holes: Horizons, ergospheres,
and Hawking radiation, Class. Quantum Grav. 15, 1767
(1998).
[22] C. Barceló, S. Liberati, and M. Visser, Analogue Gravity,
Living Rev. Relativ. 14, 3 (2011).
[23] A. Papapetrou, Eine Theorie des Gravitationsfeldes mit
einer Feldfunktion, Z. Phys. 139, 518 (1954).
[24] H. Yilmaz, New Approach to General Relativity, Phys.
Rev. 111, 1417 (1958).
[25] C. W. Misner, Yilmaz Cancels Newton, Nuovo Cim. B
114, 1079 (1999).
[26] C. O. Alley, P. K. Aschan, and H. Yilmaz, Refutation
of C. W. Misner’s claims in his article “Yilmaz Cancels
Newton”, arXiv:gr-qc/9506082 (1995).
[27] S. L. Robertson, MOND-Like Phenomenology from
Exponential-Metric Gravity Applied to Galactic Dynamics, Astrophys. J. 515, 365 (1999).
[28] M. Ibison, The steady-state cosmology and the cosmic
microwave background, Class. Quantum Grav. 23, 577
(2006).
[29] M. A. Makukov and E. G. Mychelkin, Triple Path to
the Exponential Metric, Found. Phys. 50, 1346 (2020),
arXiv:2009.08655.
[30] P. Boonserm, T. Ngampitipan, A. Simpson, and
M. Visser, Exponential metric represents a traversable

VIII.

CONCLUSION

9
wormhole, Phys. Rev. D 98, 084048 (2018).
[31] D. Hochberg and M. Visser, Geometric structure of the
generic static traversable wormhole throat, Phys. Rev. D
56, 4745 (1997), arXiv:gr-qc/9710001.
[32] M. Visser, Lorentzian Wormholes: From Einstein to
Hawking (AIP Press, 1996).
[33] B. Bertotti, L. Iess, and P. Tortora, A test of general
relativity using radio links with the Cassini spacecraft,
Nature 425, 374 (2003).
[34] F. Hofmann and J. Müller, Relativistic tests with lunar
laser ranging, Class. Quantum Grav. 35, 035015 (2018).
[35] Event Horizon Telescope Collaboration, First M87 Event
Horizon Telescope Results I, Astrophys. J. Lett. 875, L1
(2019).
[36] Event Horizon Telescope Collaboration, First Sagittarius
A* Event Horizon Telescope Results I, Astrophys. J. Lett.
930, L12 (2022).
[37] Event Horizon Telescope Collaboration, First Sagittarius
A* Event Horizon Telescope Results VI, Astrophys. J.
Lett. 930, L17 (2022).
[38] D. Psaltis et al., Gravitational Test beyond the First PostNewtonian Order with the Shadow of the M87 Black Hole,
Phys. Rev. Lett. 125, 141104 (2020).
[39] P. Kocherlakota and L. Rezzolla, Accurate mapping
of spherically symmetric black holes in a parametrised
framework, Phys. Rev. D 105, 064064 (2022).
[40] M. D. Johnson et al., Universal interferometric signatures of a black hole’s photon ring, Sci. Adv. 6, eaaz1310

(2020).
[41] D. Ayzenberg et al., Fundamental physics opportunities
with the next-generation Event Horizon Telescope, Living
Rev. Relativ. 28, 4 (2025).
[42] V. Cardoso and P. Pani, Testing the nature of dark compact objects: a status report, Living Rev. Relativ. 22, 4
(2019), arXiv:1904.05363.
[43] J. Abedi, H. Dykaar, and N. Afshordi, Echoes from the
abyss: Tentative evidence for Planck-scale structure at
black hole horizons, Phys. Rev. D 96, 082004 (2017),
arXiv:1608.08637.
[44] J. Westerweck et al., Low significance of evidence for
black hole echoes in gravitational wave data, Phys. Rev.
D 97, 124037 (2018).
[45] LIGO-Virgo-KAGRA
Collaboration,
Search
for
gravitational-wave echoes from black hole merger
remnants in O3, Phys. Rev. D 108, 104040 (2023).
[46] LIGO-Virgo-KAGRA Collaboration, Tests of general relativity with GWTC-3, Phys. Rev. D 112, 084080 (2025).
[47] M. Isi et al., Testing the no-hair theorem with GW150914,
Phys. Rev. Lett. 123, 111102 (2019).
[48] F. Abe, Gravitational Microlensing by the Ellis Wormhole, Astrophys. J. 725, 787 (2010).
[49] G. A. Baker, Jr. and P. Graves-Morris, Padé Approximants, 2nd ed., Encyclopedia of Mathematics and its
Applications, Vol. 59 (Cambridge University Press, Cambridge, 1996).

