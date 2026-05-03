---
source_pdf: Strong_Fields_and_Gravitational_Waves_in_Density_Field_Dynamics__From_Optical_First_Principles_to_Quantitative_Tests.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Strong Fields and Gravitational Waves in Density Field Dynamics:
From Optical First Principles to Quantitative Tests
Gary Alcock1
1

Independent Researcher, Los Angeles, CA, USA
(Dated: September 8, 2025)

Density Field Dynamics (DFD) posits a single scalar field ψ(x, t) on Euclidean R3 such that
2
massive test bodies experience a = c2 ∇ψ and photons propagate with refractive index n = eψ
(one-way c1 = c/n). Weak-field optics are matched to GR’s classic tests by normalization. We
answer three outstanding critiques: principle, strong field, and radiation. (i) We formulate a
Minimal Optical Equivalence principle: light follows the eikonal of an effective optical metric
ds̃2 = −c2 dt2 /n2 (x, t) + dx2 , while matter sees the conservative potential Φ = −c2 ψ/2; this is
the precise content of “emergent time” and fixes normalization. (ii) We supply a constrained,
monotone family µα (x) with convex energy density and show existence/uniqueness (static) by direct variational methods, yielding well-posed compact profiles, photon spheres, and optical horizons
(with causal meaning via the optical metric). (iii) We add a minimal massless TT sector at speed
c and derive the quadrupole flux from an action with universal effective stress coupling; deviations
are parameterized and mapped to ppE phase coefficients with explicit formulae. Quantitatively,
we present (a) an EHT shadow pipeline based on the extremum of n(r)r and (b) a ppE dictionary {ε0 , ε2 , φ3 } → {β−5 , β−3 , β−2 } for catalog fits. The laboratory discriminator —a co-located
cavity–atom ratio across altitude—is derived in the main text (not relegated), with required dispersion/elastic controls. We discuss EFT/quantum consistency at low energies and outline cosmological
consequences to the extent they are falsifiable.
1

PRINCIPLE, KINEMATICS, AND ACTION

Minimal Optical Equivalence. Postulate P1 (Light).
In a broadband nondispersive window, electromagnetic
waves propagate according to the eikonal of an effective
optical metric
ds̃2 ≡ −

c2 dt2
+ dx2 ,
n2 (x, t)

n(x, t) = eψ(x,t) .

(1)

This is the Gordon/Perlick optical geometry statement,
grounding ray optics in wave theory (see App. B with references to standard optical metric literature). Postulate
P2 (Matter). Test bodies move under the conservative
potential
Φ≡−

c2
ψ,
2

a=

c2
∇ψ = −∇Φ,
2

α = 1, λ = 1
α = 2, λ = 0.5
α = 2, λ = 2

0.5

0

0

1

2
3
x = |∇ψ|/a⋆

4

5

FIG. 1. Constrained crossover functions µα,λ (x): linear deepfield, saturating solar limit, monotone and elliptic.

(2)

which fixes the weak-field normalization to match GR’s
classic optical tests (deflection factor of two, Shapiro coefficient, gravitational redshift).
Variational formulation and dimensions. We adopt
the action
 2

Z
 |∇ψ|2  c2
a⋆
3
Sψ = dt d x
W
− ψ(ρ − ρ̄) , (3)
8πG
a2⋆
2
√

µα,λ (x)

I.

with W ′ (y) = µ( y), a⋆ an acceleration scale. Dimensional analysis (App. A) verifies consistency; variation
yields
 

8πG
|∇ψ| 
∇· µ
∇ψ = − 2 (ρ − ρ̄).
(4)
a⋆
c

Constrained µ family (not ad hoc). We impose: (i)
solar limit µ → 1; (ii) deep-field branch µ(x) ∼ x; (iii)
monotonicity µ′ (x) > 0 for ellipticity; (iv) convex W
for energy positivity and stability. A convenient twoparameter family satisfying these is

µα,λ (x) =

x
1 + λxα

1/α ,

α ≥ 1, λ > 0.

(5)

This encodes a one-parameter departure from the minimal λ = 1 case and will be used for EHT/ppE fits.

2
1.1
α=2
α=4

θsh /θGR

1.05
optical horizon

1
0.95

photon sphere

0.9

0.5

1

FIG. 2. Optical horizon and photon sphere in the optical
metric.

II.

STATIC STRONG FIELDS: EXISTENCE,
PHOTON SPHERES, HORIZONS

Static equation and existence. Under spherical symmetry with ρ = 0 for r > R⋆ ,

1 d 2
′
′
r
µ(|ψ
|/a
)ψ
= 0.
(6)
⋆
r2 dr
With µ′ > 0 and convex W , the operator is uniformly
elliptic; existence/uniqueness (weak solution), regularity,
and a maximum principle follow by standard PDE methods (App. C).
Optical causal structure. The optical metric (1) supplies causal meaning: optical horizons are loci where
n → ∞ (c1 → 0), forbidding outward null escape. We
stress that this is an optical horizon; its global structure
need not coincide with GR event horizons, and this difference is observationally testable via photon rings.
Photon sphere and shadow (derived, not assumed).
Null geodesics of (1) or equivalently Fermat’s principle
give the conserved impact b = n(r)r sin θ. Circular photon orbits obey

d
n(r) r
=0
dr
r=rph

⇐⇒

ψ ′ (rph ) = −

1
.
rph

(7)

Thus bcrit = n(rph ) rph and θsh ≃ bcrit /Do . This eikonal
derivation is standard in optical geometry; we provide
the wave→ray limit in App. B.
EHT comparison:
quantitative pipeline. Write
n(r) = exp ψ(r) and expand near rph :


ln n(r) r = ln bcrit + 21 κ(r − rph )2 + · · · ,
(8)
with curvature κ > 0. Then
∆θsh
∆bcrit
∆rph
=
= ∆ψ(rph ) +
.
θsh
bcrit
rph

(9)

Using (6) to relate ψ ′ and µ, and (7), we obtain closed
forms
1
,
bcrit = rph eψ(rph ) ,
|ψ ′ (rph )|
∆ ln bcrit = ∆ψ(rph ) − ∆ ln |ψ ′ (rph )|.
(10)
rph =

⇒

1.5

2

λ
FIG. 3. Schematic EHT band: Eq. (10) turns (α, λ) into a
quantitative shadow prediction.

Equations (6)–(10) make {α, λ, a⋆ } quantitatively fit-able
to EHT shadow radii given (M, D), with priors from
galactic phenomenology. We include a worked example
in App. F.

III.

RADIATION: ACTION, COUPLING, FLUX

Minimal radiative sector (justified). We add a free,
massless transverse–traceless field at speed c,
Sh =

c3
64πG

Z

h
i
dt d3 x (∂t hij )2 − c2 (∇hij )2 ,

(11)

and couple it to matter via the effective spatial stress
derived from the optical metric (universal minimal coupling),
Sint =

1
2

Z

ij
dt d3 x hij Teff
[ψ; ρ, v],

(12)

yielding (TT gauge)
∂tt hij − c2 ∇2 hij =

32πG ij TT
(Teff ) .
c4

(13)

This construction (i) fixes cGW = c as observed, (ii) guarantees only +, × polarizations in the far zone, and (iii)
places all deviations into the conservative source dynamics via ψ (App. D derives the flux).
Quadrupole flux and energy balance. At leading PN
ij TT
order, (Teff
)
reduces to the standard mass quadrupole
Iij computed with the conservative potential Φ =
−c2 ψ/2. The far-zone flux is
dE
G D ... ... E
= − 5 I ij I ij [1 + δrad ],
dt
5c

(14)

where δrad packages any small radiative-sector inefficiency beyond GR. Detailed steps are in App. D with
standard references.

3
raise by ∆h

strain (arb.)

1

0
Cavity

comb

−1
0

2

4

6

8

Atom

take R at two altitudes

10

time
FIG. 4. Inspiral chirp schematic. In DFD, leading wave dynamics match the GR quadrupole law; measurable differences
enter via conservative/radiative parameters quantified below.

FIG. 6. Sector-resolved LPI test in the main text: Eq. (22) is
the DFD slope; GR predicts 0. Controls: dispersion, elastic
sag, swaps/blinds.

V.
|∆Ψ(f )| (arb.)

10−2

β−5 ̸= 0
β−2 ̸= 0

In a nondispersive window, an evacuated cavity measures fcav ∝ vphase /L = c/nL while co-located atomic
transitions fat obey the standard gravitational redshift.
Define the dimensionless ratio R ≡ fcav /fat . At a fixed
location,
 δΦ 
δR
δfcav
δfat
=
(21)
−
= −δψ − − 2 ,
R
fcav
fat
c

10−3

101

102
f (arb.)

FIG. 5. Illustrative ppE phase residuals from (17).
(18)–(20) to translate catalog bounds into (ε0 , ε2 , φ3 ).

IV.

Use

F(v) = FGR (v) [1 + φ3 v + · · · ].

(15)

Ψ(f ) = ΨGR (f )+β−5 u−5 +β−3 u−3 +β−2 u−2 +· · · , (17)
with explicit coefficients
5
ε0 ,
128 η
3
β−3 =
C1 (η) ε2 ,
128 η
3
β−2 =
D3 (η) φ3 .
128 η

1
|{z}

+

1
|{z}

≃ 2,

optical phase

(22)
in DFD, while GR demands ∆R/R = 0 because all clocks
redshift identically. The experiment is sector-resolved :
dispersion is bounded by a dual-λ check; elastic sag is
nulled by 180◦ flips; environmental thresholds and hardware swaps follow standard metrology best practice.

(16)

Stationary-phase integration gives the Fourier phase

β−5 = −

ξ≡

atomic redshift

Let u = (πM f )1/3 and η = m1 m2 /M 2 . Parametrize
conservative and dissipative departures by

3

using fcav ∝ e−ψ and δfat /fat = −δΦ/c2 . Moving the colocated system between two geopotentials (∆Φ ≃ g ∆h)
gives the observable slope
∆R
∆Φ
=ξ 2 ,
R
c

PN/PPE MAPPING: FIT-READY
FORMULAS

E(v) = EGR (v) [1 + ε0 + ε2 v 2 + · · · ],

LABORATORY DISCRIMINATOR IN THE
MAIN TEXT

(18)
(19)
(20)

Here C1 (η) and D3 (η) are the standard GR weights (tabulated in App. E). Equations (18)–(20) let one directly fit
DFD parameters to catalog ppE bounds without bespoke
waveform models.

VI.

QUANTUM/EFT AND COSMOLOGY
(SCOPE AND FALSIFIABILITY)

Low-energy
EFT
consistency. At
laboratory/astrophysical energies, DFD acts as a classical
medium theory with an optical metric for light and a
conservative potential for matter. Quantization of hij
follows the standard free massless TT field. The ψ field
need not be canonically quantized to confront current
phenomenology; loop corrections would renormalize
W (hence µ), providing a natural origin for crossover
behavior (cf. induced-gravity heuristics). Observable
constraints enter via §IV.
Cosmology (claim limited to a testable bias). Rather
than assert “no dark energy,” we make a narrower, falsifiable statement: optical path-length bias from n = eψ
induces a line-of-sight selection in local distance ladders,
shifting inferred H0 anisotropically. The smoking gun is

4
a correlation between δH0 (n̂) and LOS density-gradient
proxies. This is testable with existing ladder data without re-deriving FRW dynamics here.

VII.

DISCUSSION

Direct methods (coercivity, weak lower semicontinuity)
yield a minimizer ψ ∈ H 1 (Ω) for bounded Ω and admissible boundary data. The Euler–Lagrange equation is
(4). Maximum principles and Schauder estimates ensure
regularity; uniqueness follows from strict convexity of W .
These establish well-posedness of static compact profiles.
Appendix D: Quadrupole Flux

We addressed “why this theory” by elevating the optical postulates to a minimal equivalence principle tied
to the eikonal of the optical metric; we justified the
scalar–tensor radiation sector by an action with universal effective stress coupling; we replaced ad hoc µ with a
constrained family admitting PDE existence/uniqueness
and yielding quantitative shadow predictions; we moved
the decisive LPI derivation into the main text; and we
provided fit-ready ppE formulae. The remaining work
is empirical: (i) fit (α, λ, a⋆ ) to EHT shadow radii with
priors; (ii) translate catalog ppE bounds into (ε0 , ε2 , φ3 );
(iii) run the sector-resolved LPI test with dual-λ and elastic controls. Any of these can falsify the sector presented
here.

Compute the Noether stress tensor for (11), project
TT, and evaluate the far-zone flux, obtaining (14). The
source multipoles coincide with GR at leading PN order because the conservative dynamics are Newtonian in
Φ = −c2 ψ/2; deviations appear as (ε0 , ε2 ) in the binding
energy and φ3 in the radiative efficiency.

Appendix E: ppE Dictionary

Starting from dE/dt = −F, expand (15)–(16) to first
order and integrate in stationary phase. One recovers
(18)–(20) with

Appendix A: Dimensions and Normalizations

ψ is dimensionless; [a⋆ ] = m s−2 , [ρ] = kg m−3 . The
Lagrangian density in (3) has units J m−3 ; variation
yields (4) with 8πG/c2 ensuring the Newtonian and optical normalizations that reproduce GR’s classic tests.

C1 (η) =

743 11
+ η,
336
4

D3 (η) = −16π,

the standard GR weights for 1PN conservative and 1.5PN
dissipative terms. This enables direct translation of catalog bounds into DFD parameters.

Appendix B: Wave → Ray: Optical Metric and
Eikonal
Appendix F: Shadow Worked Example

Starting from Maxwell in a slowly varying dielectric, one obtains the Gordon optical metric; the
eikonal/Hamilton–Jacobi equations yield rays as null
geodesics of (1). This legitimizes using (7) in strong gradients (standard references in the bibliography).

For a given (α, λ, a⋆ ), integrate (6) outward from R⋆
with boundary data matching the solar normalization at
large r. Solve d[n(r)r]/dr = 0 for rph and evaluate bcrit =
n(rph )rph . Compare θsh = bcrit /Do to EHT; use (10) for
sensitivity. This provides concrete posteriors on (α, λ)
independent of galaxy data.

Appendix C: Static Existence/Uniqueness and
Stability

With µ′ (x) > 0 and convex W , the operator is uniformly elliptic for |∇ψ| < ∞. Define the functional
Z
 |∇ψ|2  c2 Z
a2
d3 x ψ(ρ − ρ̄).
E[ψ] = d3 x ⋆ W
−
8πG
a2⋆
2

[1] C. M. Will, The Confrontation between General Relativity and Experiment, Living Rev. Relativity 17, 4 (2014).
[2] V. Perlick, Ray Optics, Fermat’s Principle, and Applications to General Relativity (Springer, 2000).
[3] W. Gordon, Zur Lichtfortpflanzung nach der Relativitätstheorie, Ann. Phys. 72, 421 (1923).

ACKNOWLEDGMENTS

I thank colleagues in gravitational wave physics and
precision optical metrology for helpful discussions.

[4] M. A. Abramowicz, B. Carter, and J.-P. Lasota, Optical
reference geometry for stationary and static dynamics,
Gen. Relativ. Gravit. 20, 1173 (1988).
[5] M. Maggiore, Gravitational Waves, Vol. 1: Theory and
Experiments (Oxford Univ. Press, 2007).

5
[6] L. Blanchet, Gravitational Radiation from PostNewtonian Sources and Inspiralling Compact Binaries,
Living Rev. Relativity 17, 2 (2014).
[7] C. Cutler and É. E. Flanagan, Gravitational waves from
merging compact binaries, Phys. Rev. D 49, 2658 (1994).
[8] N. Yunes and F. Pretorius, Fundamental theoretical bias
and the parametrized post-Einsteinian framework, Phys.
Rev. D 80, 122003 (2009).
[9] B. P. Abbott et al., GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral, Phys.

Rev. Lett. 119, 161101 (2017).
[10] A. Goldstein et al., Fermi-GBM Detection of GRB
170817A, Astrophys. J. Lett. 848, L14 (2017).
[11] Event Horizon Telescope Collaboration, First M87 EHT
Results. I. The Shadow, Astrophys. J. Lett. 875, L1
(2019).

