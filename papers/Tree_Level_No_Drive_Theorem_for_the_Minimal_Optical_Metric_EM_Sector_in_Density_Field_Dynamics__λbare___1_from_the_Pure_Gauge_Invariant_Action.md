---
source_pdf: Tree_Level_No_Drive_Theorem_for_the_Minimal_Optical_Metric_EM_Sector_in_Density_Field_Dynamics__λbare___1_from_the_Pure_Gauge_Invariant_Action.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Tree-Level No-Drive Theorem for the Minimal Optical-Metric EM Sector in Density
Field Dynamics:
λbare = 1 from the Pure Gauge-Invariant Action
Gary Alcock1
1

Independent Researcher, Los Angeles, CA, USA∗
(Dated: May 2, 2026)

In Density Field Dynamics (DFD), the parameter λ introduced in Appendix R of the unified
paper controls whether laboratory electromagnetic fields can pump the scalar field ψ at frequency
2ω beyond the optical-metric forward-propagation channel. Appendix R is broader than a single
baseline: it contains a minimal tree-level optical-metric sector, a geometry-restoration channel,
threshold-sensitive nonlinear structure, and a dual-sector κ extension. Here we address the minimal
sector only. We show that in the minimal tree-level optical-metric EM sector of DFD, the linear-in-ψ
EM source produced by the gauge-invariant action is proportional to the EM energy density (E 2 /c2 +
B 2 )/(2µ0 ) rather than the stress invariant (E 2 /c2 −B 2 )/(2µ0 ). For ideal standing-wave cavity modes
with energy equipartition, the energy-density source has no 2ω component after volume integration.
Consequently the bare-coupling value of the back-reaction parameter equals unity at tree level in the
minimal sector, which we write as λbare = 1. The effective laboratory inference λeff differs from λbare
by explicit corrections: a classical 1/Q mimicking effect from finite cavity quality factor, geometryrestoration contributions for non-symmetric or TE+TM superposition modes, threshold corrections
if the system approaches ηc = α/4, and any contributions from constitutive-sector splitting (the
κ channel) or from beyond-baseline dimension-5 operators ξ ψ Fµν F µν . We therefore reinterpret
Appendix R’s accidental bound |λ − 1| < 3 × 10−5 and the projected intentional-search reach
|λ − 1| ∼ 10−14 as constraints on these beyond-minimal-sector channels: the minimal sector’s
λbare = 1 is the null baseline, and nonzero inferred λeff diagnoses which beyond-baseline channel is
active.
I.

INTRODUCTION

Density Field Dynamics (DFD) [1] is a scalar
refractive-index theory of gravity with postulates (P1)
n = eψ for the optical refractive index and (P2) a =
(c2 /2)∇ψ for matter acceleration. These postulates specify how the scalar field ψ affects electromagnetic and material systems but leave open the inverse question: can
rapidly oscillating EM fields, in turn, actively pump ψ
modes beyond the standard contribution of their energy
density to the matter source?
Appendix R of [1] introduces a phenomenological parameter λ to quantify this back-reaction. The parameter
enters the single-mode reduction of the ψ equation of
motion as the coefficient of an EM-driven source term:
Z
(λ − 1)
u(r) Ξ(r, t) d3 r + αpar U (t)q,
q̈ + 2γψ q̇ + Ω2ψ q =
Mψ
(1)
where Ξ ≡ −(1/2)e−2ψ0 (B 2 − E 2 /c2 ) is the stress invariant (equivalently −Fµν F µν /4 up to sign), and αpar
is the parametric (stiffness-modulation) coupling of Appendix R. We use the subscript “par” to distinguish it
locally from the fine-structure constant α; Appendix R
itself writes this coefficient simply as α. The parameter
λ = 1 corresponds to no direct back-reaction drive at 2ω
through this specific channel; λ ̸= 1 signals an additional
coupling.

∗ gary@gtacompanies.com

The Appendix R text describes λ as “a distinct physical degree of freedom not constrained by the forward
propagation relations.” The accidental bound |λ − 1| <
3 × 10−5 (from the absence of parametric instability in
high-Q cavities) is presented as a phenomenological constraint. Appendix R also develops additional structure
beyond this minimal baseline: geometry-restoration arguments for asymmetric or TE+TM superposition modes
that can restore driven overlap, threshold-sensitive nonlinear coupling activated above ηc = α/4, and a dualsector κ extension with its own leading-order phenomenology.
a. Scope of this paper. We address only the minimal
tree-level optical-metric EM
gauge-invariant
R √ sector : the
action SEM = −(1/4µ0 )
−g̃ Fµν F µν d4 x in the DFD
optical metric n = eψ , with no added operators and no
constitutive-sector splitting. In that minimal baseline we
show that the bare back-reaction parameter equals unity
at tree level: λbare = 1. We distinguish this from the
effective laboratory inference
λeff = 1 + δQ + δgeom + δthr + δκ + δξ ,

(2)

where δQ ∼ 1/Q is the finite-Q equipartition-violation
mimic, δgeom captures geometry-restoration channels for
non-ideal or TE+TM modes ([1], Appendix R), δthr
captures threshold physics above ηc , δκ captures dualsector constitutive splitting, and δξ captures any beyondbaseline dimension-5 operator ξ ψ Fµν F µν . The minimalsector tree-level result λbare = 1 is the null baseline; a
nonzero inferred λeff − 1 diagnoses which combination of
these channels is active.

2
Section II establishes the optical metric and EM action.
Section III derives the ψ-expansion of the EM Lagrangian
in a single convention. Section IV computes the cavity
drive term from both (E 2 + B 2 ) and (E 2 − B 2 ) sources
for ideal equipartitioned modes. Section V states the
minimal-sector no-drive theorem. Section VI examines
each beyond-baseline channel in Eq. (2) and sharpens
the distinction from κ.
II.

SETUP: OPTICAL METRIC AND EM
ACTION

Expanded in powers of ψ:
LEM (ψ) =



1  E2
1  E2
2
2
+
ψ
2 − B
2 + B
c
c
2µ0
2µ0


1 E2
2
ψ 2 + O(ψ 3 ).
(8)
+
2 − B
4µ0 c

Proof. With the conventions above, compute
X
Fµν F µν = 2F0i F 0i + 2
Fij F ij
i<j
00 ij

= 2g̃ g̃ F0i F0j + 2

c2 2
dt + dx2 ,
n2

n = eψ .

(3)

The metric and inverse-metric components are
g̃ij = δij ,

(4)

g̃ 00 = −c−2 e2ψ ,

g̃ ij = δ ij ,

(5)

√
with −g̃ = c e−ψ .
The gauge-invariant EM action is
Z p
1
SEM = −
−g̃ g̃ µα g̃ νβ Fµν Fαβ d4 x.
4µ0

2e2ψ 2
E + 2B 2 .
c2

(10)

The four-volume density (per d(ct) d3 x, the standard relativistic measure) is
p

−g̃

=

p

−g̃/c = e−ψ .

(11)

d(ct)d3 x

(6)

The EM postulate (P1) specifies that photons propagate
along null geodesics of this metric with effective speed
c/n; the action (6) is the minimal gauge-invariant action
whose equations of motion reproduce this propagation.
The matter postulate (P2) couples matter to ψ through
its energy density ρ as the source term in the ψ field equation. EM field energy contributes to this source through
its energy-momentum content; the question is whether
additional EM–ψ couplings appear beyond this energydensity channel.
III.

(9)

Using g̃ 00 = −c−2 e2ψ and g̃ ij = δ ij , with F0i = Ei and
Fij = ϵijk B k :
Fµν F µν = −

g̃00 = −c2 e−2ψ ,

g̃ ik g̃ jl Fij Fkl .

i<j

In DFD, the optical metric in Cartesian coordinates is
ds̃2 = −

X

THE ψ-EXPANSION OF THE EM
LAGRANGIAN

We fix conventions once and for all: coordinates
(ct, x, y, z) (time coordinate is x0 = ct), metric signature (−, +, +, +), F0i = Ei , Fij = ϵijk B k (spatial components dimensionally [B]), four-volume measure
d4 x = d(ct) d3 x. Under these conventions, the flat-space
2
Maxwell Lagrangian density is Lflat
Maxwell = (ϵ0 /2)E −
2
2 2
2
(1/2µ0 )B = (1/2µ0 )(E /c − B ), which serves as our
ψ = 0 check. We use only these conventions throughout.
Lemma 1 (EM Lagrangian in optical metric). In the
DFD optical metric (3) under the conventions above, the
EM Lagrangian density LEM per unit coordinate fourvolume d4 x = d(ct) d3 x is


2
1
ψ E
−ψ
2
LEM (ψ) =
e
−e B .
(7)
2µ0
c2

(In 4D with√signature (−, +, +, +) and time coordinate
ct, the bare −g̃ is c e−ψ ; we have absorbed the factor c
into the standard relativistic measureR d(ct) = c dt. This
is equivalent
to writing the action as L d(ct) d3 x rather
R
than cL dt d3 x.) Therefore


2e2ψ E 2
e−ψ
2
LEM = −
+ 2B
−
4µ0
c2

 ψ 2
1
e E
−ψ 2
=
−e B ,
2µ0
c2

(12)

as stated. Taylor expansion of e±ψ about ψ = 0 yields
Eq. (8).
Consistency check at ψ = 0: LEM |0 = (1/2µ0 )(E 2 /c2 −
2
B ) = (ϵ0 /2)E 2 − (1/2µ0 )B 2 , matching the flat-space
Maxwell Lagrangian density under our conventions.
The key observation from Eq. (8): the term linear in
ψ has coefficient (E 2 /c2 + B 2 )/(2µ0 ) = uEM (EM energy
density), while the term quadratic in ψ has coefficient
(E 2 /c2 − B 2 )/(4µ0 ).
Corollary 2 (Source structure for ψ from the EM sector). The EM contribution to the right-hand side of the
ψ equation of motion, defined as ∂LEM /∂ψ (the EM Lagrangian density variation with respect to ψ), is

∂LEM
1  E2
2
(r, t) = uEM (r, t)+
−
B
ψ(r, t)+O(ψ 2 ),
2
∂ψ
2µ0 c
(13)
where uEM = (ϵ0 E 2 + B 2 /µ0 )/2 = (E 2 /c2 + B 2 )/(2µ0 )
is the EM energy density.

3
In contrast, the integrated (E 2 /c2 − B 2 ) source at 2ω has
its full amplitude:
Z
d3 r u0 (E 2 /c2 − B 2 )2ω = u0 UEM cos(2ωt),
(22)
∂L
EM
2
,
(gravitational-sector coefficient)· ˜
□ψ = ρmatter c ψ-coupling +
R
∂ψUEM = d3 r (ϵ0 |E0 |2 + µ−1 |B0 |2 )/2 is the total
where
0
(14)
cavity energy.
where the gravitational-sector coefficient is set by the normalization of the kinetic term in the DFD action ([1],
Corollary 4 establishes the key quantitative separation:
Appendix U; it takes the form c4 /(8πG) in Newtonianfor standing-wave cavity fields, pumping at 2ω requires a
limit conventions), and the matter coupling follows from
source term coupled to (E 2 /c2 −B 2 ), not to (E 2 /c2 +B 2 ).
(P2). The linearized-in-ψ EM source appearing on the
right-hand side is proportional to ∂LEM /∂ψ, with an
V. MAIN THEOREM
overall coefficient fixed by the gravitational-sector normalization.
The crucial structural fact for what follows is that the
Theorem 5 (Tree-level no-drive theorem for the minimal
linear-in-ψ coefficient in Eq. (13) is proportional to uEM ,
optical-metric sector). Assume:
not to the stress invariant E 2 /c2 − B 2 . This proportion(i) The DFD postulates P1 and P2 as in [1];
ality is a property of LEM itself, read off directly from the
(ii) The minimal EM action Eq. (6), with no addiexpansion (8), and is independent of any choice of overall
tional dimension-5 operator and no constitutivegravitational-sector normalization convention. The theosector splitting;
rem in Section V uses only this structural proportionality;
(iii) A laboratory system satisfying η := UEM /(ρc2 ) ≪
it does not require pinning down the overall coefficient.
ηc = α/4, where ρ is the cavity-walls matter density, so that threshold physics is inactive;
(iv) A single ideal symmetric standing-wave cavity mode
IV. STANDING-WAVE CAVITY: WHERE DOES
with exact energy equipartition (Q → ∞ limit).
2ω DRIVE COME FROM?
Then the bare-coupling value of the Appendix R backreaction parameter is unity at tree level in the minimal
Consider an ideal standing-wave cavity with field prosector:
files
λbare = 1 at tree level, minimal sector .
(23)
E(r, t) = E (r) cos(ωt), B(r, t) = B (r) sin(ωt), (15)
The full ψ equation of motion has three contributions: a gravitational-sector kinetic term, a matterdensity source, and the EM contribution from ∂LEM /∂ψ.
Schematically,

0

0

with the 90◦ temporal phase shift characteristic of standing waves. The time-averaged energy equipartition condition
Z
Z
2
d3 r ϵ0 |E0 |2 = d3 r µ−1
(16)
0 |B0 |
is satisfied for any standing-wave cavity mode.
Lemma 3 (Fourier content of EM bilinears). Under the
profile (15), the Fourier decomposition of E 2 and B 2 in
time yields
E 2 (r, t) = 12 |E0 |2 [1 + cos(2ωt)],
B

2

(r, t) = 12 |B0 |2 [1 − cos(2ωt)].

(17)
(18)

Consequently:
(E 2 /c2 + B 2 )2ω = 12 (|E0 |2 /c2 − |B0 |2 ) cos(2ωt),
2

2

2

2

2

2

(E /c − B )2ω = 12 (|E0 | /c + |B0 | ) cos(2ωt).

(19)
(20)

Proof. By Corollary 2, the EM contribution ∂LEM /∂ψ to
the ψ equation of motion contains a zeroth-order piece
uEM (EM energy density) and a linear-in-ψ piece proportional to (E 2 /c2 − B 2 )ψ. The linear-in-ψ piece acts
as a stiffness modulation (mass-like term, modifying Ω2ψ )
rather than as a direct drive.
By Corollary 4 and hypothesis (iv), for a single
ideal symmetric standing-wave cavity mode with exact
equipartition, the 2ω Fourier component
of the volumeR
integrated zeroth-order source uEM (r, t) u(r) d3 r vanishes. No direct drive at frequency 2ω is produced by the
minimal optical-metric action.
The Appendix R mode equation
(1) identifies the
R
drive term as [(λ − 1)/Mψ ] u(r)Ξ(r, t) d3 r with Ξ =
(1/2µ0 )(E 2 /c2 −B 2 ). Under hypotheses (i)-(iv), the minimal sector produces no such drive, so the bare-coupling
value of (λ − 1) is zero at tree level in the minimal sector:
λbare = 1.

Corollary 4 (Vanishing of energy-density drive at 2ω).
We emphasize what this theorem does and does not
For any standing-wave cavity mode with a uniform spatial
claim.
It establishes the minimal-sector tree-level basetest function u(r) ≡ u0 , the integrated 2ω component of
line
for
an ideal symmetric single-mode standing-wave
the energy-density source vanishes by equipartition:
cavity.
It
does not claim that the effective laboratory
Z
2

2
u
c
inference
λ
0
⟨|E
|
⟩
eff equals unity for real cavities. In particular,
2
0
d3 r u0 (E 2 /c2 +B 2 )2ω =
0.
c2 −⟨|B0 | ⟩ cos(2ωt) = TE+TM
superposition modes, asymmetric cavity geome2
(21)
tries, and mode-beating configurations (all analyzed in

4
[1], Appendix R) can restore driven overlap even within
the minimal sector; these are discussed as the δgeom channel in Section VI below. Additional corrections arise from
each of the other beyond-baseline channels listed in the
abstract.
Corollary 6 (Inferred-λ decomposition). For a laboratory experiment fitting the Appendix R mode equation (1)
to cavity observations, the inferred parameter λeff decomposes as
λeff − 1 = δQ + δgeom + δthr + δκ + δξ ,

(24)

where δQ ∼ 1/Q is the finite-Q equipartition-violation
mimic, δgeom arises from geometry-restoration channels
(non-ideal or TE+TM superposition modes, asymmetric cavity geometries), δthr arises only if η approaches
ηc , δκ arises from dual-sector constitutive splitting (the
κ channel of [1], Appendix R), and δξ arises from any
beyond-baseline dimension-5 operator ξ ψ Fµν F µν . Each
channel is separately analyzed in Section VI and, in
principle, separately constrainable by cavity-geometry, Qscaling, threshold-approach, and constitutive-splitting experiments.
Corollary 7 (Reinterpretation of existing cavity
bounds). The Appendix R accidental bound |λ − 1| <
3 × 10−5 from cavity stability is not a constraint on a
single intrinsic DFD parameter but a joint constraint on
|δQ + δgeom + δthr + δκ + δξ |. Similarly the projected
intentional-search reach ∼ 10−14 is a joint bound. Separating the channels requires the experimental protocols
described in Section VI.
VI.

DISCUSSION

The inferred-λ decomposition Eq. (24) has five distinct
channels. We analyze each in turn.
A.

δQ : Finite-Q equipartition-violation mimic

For a real cavity with quality factor Q, equipartition
of electric and magnetic energy holds only to fractional
accuracy 1/Q. The deviation produces a small residual
2ω component
in the volume-integrated energy-density
R
source u (E 2 /c2 +B 2 ) d3 r that was required to vanish in
Corollary 4. The residual mimics a back-reaction drive:
δQ ∼

1
.
Q

δQ is distinguishable from genuine beyond-baseline
channels by Q-scaling tests: a true ξψF 2 operator produces a Q-independent signal (up to overall amplitude),
while δQ scales as 1/Q.

B.

δgeom : Geometry-restoration channels

Theorem 5 covers only the ideal symmetric single-mode
standing-wave case (hypothesis (iv)). Appendix R of [1]
explicitly discusses geometry configurations outside that
idealization which restore driven overlap:
• TE+TM superposition modes. A cavity excited in a mixed TE+TM mode has different spatial profiles for |E0 |2 and |B0 |2 that do not satisfy
the pure equipartition structure of a single mode.
The integrated 2ω component of (E 2 /c2 +B 2 ) need
not vanish for such superpositions.
• Asymmetric cavity geometries. Geometries
symmetry can produce nonzero
Rwith broken2 spatial
u(r) (|E0 | /c2 − |B0 |2 )(r) d3 r for the particular
test function u(r) of the ψ mode, even when the
globally integrated equipartition holds.
• Mode beating. Two or more cavity modes
with commensurate frequencies can produce timevarying profiles that do not individually satisfy the
standing-wave assumption (ii) of Lemma 3.
Each
of these restores nonzero overlap G
≡
R
u(r) Ξ̂2ω (r) d3 r (in the notation of Appendix R
Eq. (R3)) and produces a nonzero effective drive proportional to δgeom . We stress that these restored-overlap
channels are produced by the same minimal opticalmetric action Eq. (6): the cancellation Corollary 4
that gives λbare = 1 only covered the ideal symmetric
single-mode standing-wave case of hypothesis (iv),
so leaving that idealization does not introduce any
new operators, it only drops the specific cancellation
condition. The minimal-sector action can, and in nonsymmetric geometries does, produce a 2ω drive through
the energy-density source without any beyond-baseline
coupling being present.
Experimental isolation of δgeom uses cavity-geometry
scans: the signal should vary with cavity shape and mode
content in a calculable way, while δξ (a genuine beyondbaseline operator) would not.

C.

δthr : Threshold physics

(25)

For state-of-the-art superconducting cavities with Q ∼
1010 -1011 , δQ ∼ 10−10 -10−11 . The existing accidental bound 3 × 10−5 is comfortably above this classical
background; the projected intentional-search reach 10−14
is well below it, so distinguishing δQ from the other
channels is an experimental requirement for sub-10−10
searches.

For laboratory cavities with η ∼ 10−14 ≪ ηc =
α/4 ∼ 10−3 , the nonlinear kG threshold coupling ([1],
Appendix G, Theorem G.2) is inactive and δthr ≈ 0. For
astrophysical plasmas where η approaches or exceeds ηc
(coronal mass ejections, laboratory fusion plasmas, etc.),
nonlinear activation can produce effective λ ̸= 1 through
the threshold channel. This is outside the hypotheses of
Theorem 5.

5
D.

δκ : Dual-sector constitutive splitting

This distinction is critical and deserves emphasis.
Appendix R of [1] introduces a dual-sector extension
with parameter κ governing electric-magnetic constitutive splitting: in that extension, the effective permittivity ϵ and permeability µ respond differently to ψ, rather
than both being set by the single optical refractive index n = eψ . Specifically the minimal sector uses one
global n for both polarizations of the EM field, while the
κ extension allows distinct responses for E and B.
This is structurally different from the λ channel:
• λ controls whether a direct (E 2 /c2 − B 2 )ψ source
appears in the Lagrangian, producing an inhomogeneous drive of the ψ mode.
• κ controls whether the effective optical response
splits between E-mode and B-mode, producing a
modification of the dispersion relation rather than
a drive.
Both parameters are phenomenologically present in
full Appendix R but are independent degrees of freedom. A dual-sector constitutive splitting (κ ̸= 0) in
general produces unequal E 2 and B 2 response spatial
profiles, which breaks equipartition at the sector level
and generates a nonzero effective δκ even in the nominally below-threshold regime. The minimal-sector theorem of this paper fixes λbare = 1 under the assumption κ = 0. A genuine measurement of λeff ̸= 1 therefore does not automatically indicate a ξψF 2 operator: it
could instead indicate activation of the κ channel. Distinguishing the two requires independent measurement of
κ through polarization-sensitive or E/B-asymmetric observables. This is a separate experimental program from
the direct-drive cavity test.
The present theorem therefore does not overturn Appendix R. It establishes the null baseline for one of Appendix R’s coupling channels, conditional on the others
being inactive or held fixed.

E.

δξ : Beyond-baseline dimension-5 operator

Any effective Lagrangian of the form Lξ = ξ ψ Fµν F µν
is gauge-invariant and general-covariant in the optical
metric, and is not excluded on symmetry grounds. It
is, however, not produced by the minimal optical-metric
action Eq. (6) under the conventions of Lemma 1: that
Lemma exhibits the full ψ-dependence of the minimal action, and it contains no ψ F 2 cross-term at linear order.
Any nonzero ξ is therefore a beyond-baseline operator.
δξ is the channel corresponding to dilaton-type coupling familiar from scalar-tensor gravity and stringtheoretic dilaton models. Measuring δξ separately from
δκ , δQ , and δgeom is a genuinely new experimental question: it would constrain the presence of a dimension-5

coupling not required by the DFD postulates P1 and P2
alone.
F.

Experimental isolation protocol

To separate the five channels in Eq. (24), an experimental program would include:
1. Q-scaling series to isolate δQ (scales as 1/Q, other
channels do not);
2. Geometry and mode-content variation to map
δgeom predictions;
3. η-varying series (through cavity energy or wall density control) to test threshold behavior δthr ;
4. Polarization-sensitive measurements to characterize δκ independently;
5. Universal residual after the above subtractions, if
present, constrains δξ .
The minimal-sector theorem of this paper is an input
to such a program, not a replacement for it.

VII.

SUMMARY

We have proved a tree-level no-drive theorem for the
minimal optical-metric EM sector in DFD: under DFD
postulates P1 and P2, the gauge-invariant action Eq. (6)
with no added operators, below-threshold conditions,
ideal standing-wave equipartition, and mode symmetry,
the bare-coupling value of the Appendix R back-reaction
parameter is unity at tree level, λbare = 1. The derivation uses only the ψ-expansion of the minimal action and
the Fourier content of standing-wave fields.
The effective laboratory inference λeff decomposes into
five additive channels (Corollary 6), none of which is zero
a priori in a real experiment. In particular, a nonzero
λeff − 1 does not automatically diagnose beyond-DFD
physics: it may reflect finite-Q equipartition violation
(δQ ), geometry-restoration channels via TE+TM superposition or cavity asymmetry (δgeom ), threshold physics
approaching ηc (δthr ), dual-sector constitutive splitting
(δκ ), or a genuine dimension-5 operator ξψFµν F µν (δξ ).
The Appendix R accidental bound |λ − 1| < 3 × 10−5
and the projected intentional-search reach ∼ 10−14 are
joint bounds on these channels. Separating them experimentally requires cavity-geometry variation, Q-scaling,
threshold-approach, and polarization-sensitive protocols,
outlined in Section VI.
The theorem therefore does not overturn Appendix R
or eliminate λ as a phenomenological parameter. It identifies the null baseline within one specific channel and
clarifies what a nonzero inferred λeff would and would not
imply. This is a narrower claim than “pure DFD predicts
λ = 1 exactly,” which our earlier framing sometimes suggested. The narrower claim is what the minimal-sector
action actually supports.

6

[1] G. Alcock, “Density Field Dynamics: A Complete Unified
Theory,” v3.4, Zenodo (2026).

