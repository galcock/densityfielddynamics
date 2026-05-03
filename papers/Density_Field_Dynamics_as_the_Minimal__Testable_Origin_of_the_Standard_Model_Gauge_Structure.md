---
source_pdf: Density_Field_Dynamics_as_the_Minimal__Testable_Origin_of_the_Standard_Model_Gauge_Structure.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Emergent SU (3) × SU (2) × U (1) from a Scalar Optical Medium:
Density Field Dynamics as the Minimal, Testable Origin of the
Standard Model Gauge Structure
Gary Alcock
October 4, 2025

Abstract
We propose a mechanism by which the Standard Model gauge structure SU (3)×SU (2)×U (1)
arises as the Berry connection on an internal mode bundle of a scalar optical medium (“DFD”),
in which a refractive field ψ sets n = eψ and induces matter acceleration a = (c2 /2)∇ψ. In
regimes analyzed to date, the DFD scalar reproduces the Newtonian limit and standard optical/gravitational redshift relations, and it admits a low-acceleration regime relevant to galactic
phenomenology.
Starting from a frame-stiffness penalty for twisting degenerate internal modes, we derive
−1/2
and an electroweak mixing relation
a Yang–Mills
p action with effective couplings gr ∼ κr
tan θW = κ2 /κ1 . We prove a minimality result: the first internal geometry that can support
SU (3) × SU (2) × U (1) with anomaly-free chirality is CP 2 × S 3 ; smaller choices fail by algebra
(no su(3)) or topology (H 4 = 0).
We outline parameter-independent pattern tests in precision spectroscopy (hadronic/EM
drift ratio δ ln µ/δ ln α! ≈!22–24, species ordering, three-clock triangle closure) and a tabletop
non-Abelian holonomy experiment in photonic ψ-textures. Absolute seasonal drifts of highenergy parameters are predicted to be extremely small (δ sin2 θW ∼ 10−13 , δgr /gr ∼ 10−12 );
accordingly, near-term discovery potential lies in the pattern tests and holonomy.
This gauge-emergence construction is operationally distinct from noncommutative geometry
and string compactifications. It should be read as a conditional extension: if the DFD scalar
description continues to pass empirical tests, the internal-bundle mechanism supplies a concrete,
falsifiable route to Standard-Model–like gauge structure.

Note on Scope and Conditionality. This paper develops a quantum and gauge-theoretic extension of Density Field Dynamics (DFD), not a second independent theory. It assumes that the scalar
refractive field ψ established in DFD is physically real and empirically valid. The internal-mode
and Berry-connection construction presented here explores what follows if that scalar exists and
couples to matter’s internal degrees of freedom.
If DFD’s scalar field is confirmed by ongoing laboratory and astronomical tests, this mechanism
becomes its natural quantum completion, predicting Standard Model–like gauge symmetries, coupling patterns, and falsifiable spectroscopic correlations. If those core DFD predictions are ever
falsified, this gauge-emergence framework would be invalidated as well. However, falsification of
this extension does not falsify DFD itself: the gravitational and optical predictions of DFD
remain independently testable and currently consistent with available data in their own right.

1

internal frame U3 twist (su(3))
CP 2

CP 2

CP 2

CP 2

S3

S3

S3

S3

internal frame U2 twist (su(2))

R3

Figure 1: Fiber-bundle picture. At each spatial point, an internal mode fiber CP 2 × S 3 carries
local frames whose Berry connections are the SU (3) × SU (2) × U (1) gauge fields.
Accordingly, this paper should be viewed as a conditional, falsifiable hypothesis built on DFD’s empirically constrained base—a bridge connecting a tested scalar gravitational framework to quantum
gauge structure, while keeping both domains conceptually and empirically distinct.

1

DFD Primer: Gravity and Optics from a Single Scalar

DFD formulates gravity and optics with a scalar field ψ(x, t) on flat R3 , with
n = eψ ,

c1 =

c
= c e−ψ ,
n

a=

c2
∇ψ,
2

Φ≡−

c2
ψ.
2

The field obeys a nonlinear Poisson-type equation
h
i


8πG
∇· µ |∇ψ|/a⋆ ∇ψ = − 2 ρ − ρ̄ ,
c

(1)

(2)

with µ → 1 in high-gradient (Solar) regimes and µ(x) ∼ x in deep-field (galactic) regimes (cf.
MOND-inspired interpolations but with an optical normalization). Light propagation in a nondispersive band obeys geometric optics with phase velocity vphase = c1 = c e−ψ , so phase metrology
(cavities, fibers) is directly sensitive to ψ without clock synchronization [1, 2].

2

Internal Mode Bundle and Berry Gauge Fields

Assume the ψ-medium supports degenerate internal mode subspaces at each point, Hint (x) ≃
C3 ⊕ C2 ⊕ C, with local orthonormal frames
E
E
E
(2)
Ξ(x) = χ(3)
, χb
, χ(1) .
a
a=1..3

b=1..2

Under local changes of basis U (x) ∈ U (3) × U (2) × U (1), Ξ → ΞU . The resulting non-Abelian
Berry connections [3, 4, 5]
(3)

Ai

= i U3† ∂i U3 ∈ su(3),

(2)

Ai

= i U2† ∂i U2 ∈ su(2),

(1)

Ai

= ∂i θ ∈ u(1),

(3)

transform as gauge fields with field strengths Fij = ∂i Aj − ∂j Ai − i[Ai , Aj ]. The natural structure
group is thus SU (3) × SU (2) × U (1).
2

2.1

Why C3 ⊕ C2 ⊕ C arises (variational statement)

We model the internal optical response by a finite-dimensional Hermitian order parameter ε̂(x) =
ε0 e2ψ(x) [⊮ + η̂(x)] with η̂ † = η̂ and Tr η̂ = 0. Consider the Landau-type internal free-energy density
X
Fint = α Tr(η̂ 2 ) + β Tr(η̂ 3 ) + γ
∥∂i η̂∥2 + . . . ,
(4)
i

P
with α > 0, γ > 0 and generic β (nonzero). Let η̂P= U Λ U † with Λ = diag(λ1 , . . . , λN ), a λa = 0.
We impose a fixed anisotropy budget Tr(η̂ 2 ) = a λ2a = Ξ2 and seek the first symmetry-breaking
pattern that: (i) yields two simple non-Abelian stabilizers and one Abelian factor; (ii) is spectrally
sparse (fewest distinct eigenvalues).
Proposition 1 (Minimal partition under Eq. (4)). Among all fixed-budget spectra {λa }, the smallest
block-degenerate pattern whose stabilizer contains two simple unitary factors and one U (1) is a
triple-degenerate eigenvalue, a double-degenerate eigenvalue, and a singlet, i.e. the partition (3, 2, 1):
Λ = diag(λ3 ⊮3 , λ2 ⊮2 , λ1 ),

λ3 + λ2 + λ1 = 0,

whose stabilizer is U (3) × U (2) × U (1) with traceless parts su(3) ⊕ su(2) ⊕ u(1). No partition with
fewer than three distinct eigenvalues achieves two simple non-Abelian factors.
Sketch. (1) Stabilizer vs. degeneracy: The stabilizer H ⊂ U (N ) of Λ is the product of unitary
groups on degenerate subspaces. To contain two simple non-Abelian factors, H must include
U (n1 ) × U (n2 ) with n1 ≥ 3, n2 ≥ 2. The smallest choice is (n1 , n2 ) = (3, 2); a residual U (1) arises
from the singlet. (2) Spectral sparsity: With
Ξ2P
constraint, Jensen’s inequality shows that for
P the
2
fixed block sizes the Landau polynomial α λa + β λ3a is minimized by equal eigenvalues within
blocks. (3) Exclusion: Any pattern with fewer than three distinct eigenvalues cannot realize two
simple non-Abelian factors (at most one U (n ≥ 2)). Any pattern whose largest block has size < 3
cannot realize su(3). Hence (3, 2, 1) is minimal.
This elevates the “central leap” from an assumption to a minimal-structure result: the first stable
degeneracy carrying two simple non-Abelian unitary frame freedoms and one Abelian factor is
(3, 2, 1), i.e. C3 ⊕ C2 ⊕ C. The special role of Tr(η̂ 3 ) is standard in Landau analyses with unitary
order parameters and selects the ordering of eigenvalues [36, 38].

3

From Frame-Stiffness to Yang–Mills F 2

Twisting the internal frames costs energy. A gradient penalty
X
Lstiff =
ηa ∥∂i |χa ⟩ ∥2

(5)

a

admits a Stückelberg/hidden-local-symmetry form [6, 7, 8]
i
X h κr
ηr
(r) (r)
(r)
(r) 2
L=
−
Tr Fij Fij +
Tr Ai − Ωi
,
2
2
r=3,2,1

3

(r)

Ωi

= i Ur† ∂i Ur .

(6)

At long wavelengths (integrating out heavy frame modes) we obtain a Yang–Mills kinetic term
Lgauge = −

X κr
(r) (r)
Tr Fij Fij ,
2

gr ∼ κ−1/2
.
r

(7)

r=3,2,1

A tiny ψ-dependence, κr (ψ) = κr0 (1 + εr ψ), implies δgr /gr = − 12 εr δψ.

3.1

Microscopic origin of κr

The stiffnesses κr are the second functional derivatives of the internal free energy with respect to
unitary frame distortions:
δ 2 Fint
κr ∼
,
δ(∂i Ur ) δ(∂i Ur )
Ur =⊮

analogs of shear moduli in elasticity [36]. In systems with order parameters, gauge-like modes and
their kinetic terms commonly emerge from gradient penalties (cf. superfluid phases and analog
gauge fields [37]). Thus the presence and form of F 2 are generic consequences of frame rigidity in a
−1/2
degenerate-mode medium, not ad hoc insertions. Renormalized low-energy gr are then gr ∼ κr ,
with microscopic values set by the spectrum of internal excitations and dual-sector energy partition.

3.2

Dynamical gauge fields from time-dependent frames

So far Ai = iU † ∂i U captured spatial twists. Let the internal frames carry inertia via
Linert =

X ζr
r

2

Tr (∂t Ur† ∂t Ur ),

the lowest-order time-derivative term allowed by unitarity. Introducing temporal Stückelberg fields
(r)
(r)
Ω0 = iUr† ∂t Ur and promoting A0 as Lagrange multipliers enforcing local frame covariance, the
quadratic action becomes
Lint =

X ζr
r

2

(r)

(r)

Tr (A0 − Ω0 )2 −

X κr
r

(r)

2

(r)

(r)

Tr Fij Fij .

(r)

Integrating out the heavy frame fluctuations in (Aµ − Ωµ ) yields the fully dynamical Yang–Mills
action

X1
(r) (r)
(r) (r)
LYM = −
εr Tr F0i F0i − κr Tr Fij Fij
, c2r = κr /εr ,
2
r
(r)

(r)

(r)

(r)

(r)

with F0i = ∂t Ai −∂i A0 −i[A0 , Ai ]. In a nondispersive band of the ψ-medium, cr = c1 = c e−ψ ,
so the gauge excitations propagate as bona fide waves with the same local phase velocity as light.
This shows that the Berry connection here is not merely geometric holonomy; the stiffness and
inertial terms together generate dynamical gauge bosons with the standard E 2 −B 2 structure (cf.
emergent gauge dynamics in ordered media [37]).

4

3.3

Micro-to-macro matching and RG running

p
At a micro cutoff Λint , matching gives gr2 (Λint ) ∼ κ−1
εr /κr . Below Λint the effective theory is
r
standard Yang–Mills plus matter, and couplings run with the usual β-functions. Hence our claim
that {g1 , g2 , g3 } are renormalized inputs is identical in spirit to the SM: κr , εr encode short-distance
physics of the internal medium; RG evolution to laboratory scales produces the measured values.
Tiny ψ-dependences of κr , εr produce co-drifts that are subdominant to RG running at present
precision.

4

Electroweak Breaking & Weak Angle from Stiffness Ratios

Introduce a weak-doublet order parameter h ∈ C2 ,

1 (1) 
(2)
Di h = ∂i − iAi − i Ai h,
2

2
Lh = |Di h|2 − λ |h|2 − v 2 (ψ) ,

(8)

(2)

so that in unitary gauge ⟨h⟩ = (0, v)T the massless photon is Aem = sin θW A3 + cos θW A(1)
with [9, 10, 11]
r
g1
κ2
κ2
(9)
tan θW =
=
,
sin2 θW =
.
g2
κ1
κ1 + κ2
A weak ψ-dependence yields δ(sin2 θW ) =

5

κ1 κ2
(ε2 − ε1 ) δψ.
(κ1 + κ2 )2

Matter, Charges, and Anomaly Cancellation

Matter fields are sections of associated bundles; the minimal nontrivial reps are triplets, doublets,
and singlets, matching SM patterns. Writing all fermions as left-handed Weyl fields (conjugating
RH fields), one generation
QL : (3, 2)+1/6 , ucL : (3̄, 1)−2/3 , dcL : (3̄, 1)+1/3 , LL : (1, 2)−1/2 , ecL : (1, 1)+1
satisfies the standard triangle-anomaly cancellations [12, 13, 14]
X
X
X
Y TSU (3) = 0,
Y TSU (2) = 0,
d(R3 )d(R2 ) Y = 0,

X

d(R3 )d(R2 ) Y 3 = 0.

(10)

 (1)
 (1)
(1)
Geometrically, the 6-form anomaly polynomial I6 = a1 Tr F32 c1 + a2 Tr F22 c1 + a3 (c1 )3 +
(1)

a4 p1 (T )c1 pulls back to zero on CP 2 × S 3 only for SM hypercharges (up to overall normalization),
making anomaly cancellation a bundle-consistency condition [15, 16].

6

Chirality: Topological and Dynamical Routes

Chirality is generated, not assumed. (i) Index route: With quantized background fluxes on CP 2
/ int in rep R has
in SU (3) and on S 3 in SU (2), the internal Dirac operator D
Z

/ int =
index D
chR (F ) ∧ Â(T M) ̸= 0,
CP 2 ×S 3

5

giving net left-minus-right zero modes [17, 18]. (ii) Orientation route: A small parity-odd
anisotropy in the internal stiffness selects an S 3 orientation and makes one chirality light (domainwall/overlap analogy) [19, 20].
Spatial-to-internal flux coupling. The background fluxesH invoked in the index computation
arise because spatial ψ-vortices carry quantized circulation, ∇ψ · dℓ = 2πkψ , whose pullback
through the internal mode map Ξ(x) induces nontrivial curvature on CP 2 × S 3 . Formally, the
Berry curvature two-form F = i Ξ† dΞ satisfies dF = i Ξ† (dΞ ∧ dΞ), so a spatial winding of ψ
creates a nonzero integral of Tr F ∧ F on the internal fiber. Thus spatial topological charge couples
directly to internal Chern numbers—analogous to how skyrmions in magnetism endow emergent
gauge flux [47]. This mechanism provides the geometric channel through which ψ textures seed
quantized internal fluxes required for chirality.

6.1

Where do the background fluxes/anisotropies come from?

The ψ-medium ties optics to geometry via n = eψ . In a nondispersive band, smooth but topologically nontrivial ψ-textures admit phase windings whose dual-electromagnetic description carries
quantized circulation. The pullback of these windings to the internal bundle produces integral
cohomology classes that act as background fluxes for the Berry
Concretely, a closed

H connection.
loop encircling a ψ-vortex generates a holonomy U = exp i A whose conjugacy class defines
an integer via π1 (U (1)) = Z and higher homotopies for the non-Abelian factors. The minimal
(k3 , k2 , q1 ) = (1, 1, 3) configuration discussed in Appendix D yields three chiral zero modes for
the (3, 2)1/6 multiplet. Small parity-odd anisotropies in the internal free energy (allowed by microscopic birefringent-like terms) bias the orientation on S 3 , selecting one chirality as light. This
mirrors chiral selection in ordered media and the domain-wall mechanism for lattice chirality.

7

Quantitative ψ-Drift Estimates (Honest Magnitudes)

The Sun–Earth orbital potential swing gives ∆ψannual ≃ ∆Φ/c2 ≈ 3 × 10−10 . With generous
(ε2 − ε1 ) ∼ 10−2 ,
δ(sin2 θW ) ≈ 0.178 × 10−2 × 3 × 10−10 ∼ 5 × 10−13 ,

δgr /gr ≲ 1.5 × 10−12 .

(11)

These are clean but currently invisible. Therefore near-term discovery potential lies in pattern tests
and holonomies. For context on constraints to varying constants, see [21, 22, 23].

8

Pre-LPI Falsifiers: Parameter-Free Patterns

Let α and µ = mp /me have tiny, common-phase ψ-linked drifts. Then (robust to SM running,
insensitive to |∆ψ|):
1. Hadronic/EM ratio: If δ ln α ̸= 0, then
δ ln µ
≈ 22–24
δ ln α
6

(sign matched)

unless small electron/Higgs dressings perturb at the few-percent level (see e.g. sensitivities
in [24, 25, 26]).
2. Species ordering: Hyperfine > molecular vibrational > ultra-stable optical in |δν/ν| (geometrylocked). With K-factors from clock sensitivity analyses [22], a typical scale is
δνCs hyperfine
|KCs |
∼ 102 –103 .
≈
δνSr optical
|KSr |
3. Triangle closure: For three co-located clocks A,B,C with linearly independent K-vectors,
the cyclic sum obeys
X δνi
= 0 ± εsyst ,
νi
cycle

with εsyst ≪ individual |δν/ν|. Violation indicates multiple hidden sectors or breakdown of
common-phase ψ-coupling.

A

Explicit Connections for Simple ψ-Textures

A.1 SU (2) vortex
In (r, ϕ, z), U2 = eiϕ τ3 /2 eif (r)τ1 /2 with f (0) = 0, f (∞) = f∞ gives
A(2)
r =

f′
τ1 ,
2

1
(2)
Aϕ = (cos f τ3 + sin f τ2 ),
2

(2)

Frϕ =

f ′ (r) sin f (r)
τ3 , Φ(2) = π[1 − cos f∞ ]τ3 .
2

A.2 SU (3) vortex
U3 = eiϕT8 eig(r)T4 with g(0) = 0, g(∞) = g∞ , [T4 , T5 ] = iT8 , [T4 , T8 ] = −iT5 yields
A(3)
r =

B

g′
T4 ,
2

(3)

Aϕ = 12 (cos g T8 + sin g T5 ),

(3)

Frϕ =

g ′ (r) sin g(r)
T8 .
2

Minimality Lemma for the SM Gauge Structure

Lemma 2 (Minimal Internal Geometry for SU (3)×SU (2)×U (1)). Let an internal medium possess
degenerate complex mode spaces whose
Q local orthonormal frames Ξ(x) define non-Abelian Berry
connections with structure group G = a Ga ⊂ U (N ). Impose:
(F) Finite irreducibility: Each simple non-Abelian factor SU (n) arises from a single irreducible
n-dimensional complex degeneracy (frame freedom U (n), traceless connection su(n)).
(A) Anomaly freedom: The internal space supports a chiral fermion spectrum with vanishing
SU (3)2 −U (1), SU (2)2 −U (1), U (1)3 , and gravitational–U (1) anomalies.
(U) Abelian factor: At least one U (1) factor is present.

7

f, g
Loop A (SU (2))BA

AB
H

A(2)

UA = Pei H
(3)
UB = Pei A

Loop B (SU (3))
ϕ, φ

Figure 2: Non-commuting holonomies. Two adiabatic loops in control space generate UA ∈
SU (2) and UB ∈ SU (3); ordering AB vs. BA yields a measurable commutator C = UB UA UB−1 UA−1 ̸=
⊮ in the designed experiment.
Then the lowest-dimensional realization of G = SU (3) × SU (2) × U (1) is furnished by C3 ⊕ C2 ⊕ C,
with vacuum manifold
M = CP 2 × S 3 ,
and there is no lower-dimensional internal geometry satisfying (F),(A),(U).
Proof. (i) Structure: su(3) needs an irreducible C3 block; su(2) an irreducible C2 block. A U (1)
factor is realized by trace parts or an explicit line. (ii) Vacuum manifolds: C3 //U (1) ≃ CP 2 =
SU (3)/(SU (2) × U (1)), fixed-norm C2 ≃ S 3 ≃ SU (2). (iii) Cohomology: Mixed anomalies (e.g.,
SU (3)2−U (1)) require H 4 (M; Z) ̸= 0 to evaluate Tr F32 . Künneth gives H 4 (CP 2 ×S 3 ) ∼
=
= H 4 (CP 2 ) ∼
4
1
4
k
4
2
3
Z; by contrast H (CP ) = H (S < 4) = 0, H (S × S ) = 0. (iv) Rule-outs: Any fiber of total
complex dimension < 3 + 2 fails by lacking su(3), su(2), or H 4 . Real degeneracies give o(n), not
complex su(3). Hence CP 2 × S 3 is minimal.

C

Tabletop Observation of Non-Abelian Berry Holonomy

Objective. Demonstrate non-commuting SU (2) and SU (3) Berry holonomies in a controlled
optical ψ-texture, providing an operational validation of the internal-bundle mechanism.

C.1 Platform
Fs-laser written waveguide arrays in fused silica. SU (2): dual-core, ∆2 /(2π) ≈ 50 GHz; SU (3):
symmetric three-core, ∆3 /(2π) ≈ 80 GHz. Write n(x, y, z) = n0 (1 + εψ) to realize adiabatic
loops [27, 28].

8

C.2 Loops & holonomies
U2 (z) = eiϕ(z)τ3 /2 eif (z)τ1 /2 with ϕ : 0 → 2π, f : 0 → π → 0 over LA ≈ 3 cm gives UA ≃ ei(Ω2 /2)τ3 ≈
diag(i, −i) (Ω2 ≈ π). U3 (z) = eiφ(z)T8 eig(z)T4 with φ : 0 → 2π, g : 0 → 2π/3 → 0 over LB ≈ 4 cm gives
UB ≃ diag(ei2π/9 , ei2π/9 , e−i4π/9 ).

C.3 Non-commutation test
Concatenate AB and BA, reconstruct unitaries by interferometric tomography, and compute
C = UB UA UB−1 UA−1 .
Abelian null: C = ⊮; non-Abelian: C ̸= ⊮ with |Cij | ∼ sin(Ω2 /2) sin(Ω3 /2) ∼ 0.3–0.5, and a
specific phase structure fixed by [τ3 , T8 ].

C.4 Adiabaticity & controls
Adiabatic parameter η = (dλ/dz)/∆2 ≪ 1 (η ≲ 10−3 ). Controls: (i) two wavelengths (geometric
invariance), (ii) loop deformation continuity, (iii) commuting-subgroup check (C = ⊮), (iv) noise
floor lacks systematic non-commutation.

C.5 Practical parameters
Core separations: 12 µm (SU2), 15 µm (SU3); ∆n: 3×10−3 /4×10−3 ; lengths 3/4 cm; tomography
accuracy ∼ 1◦ .

D

Matter Zero Modes and Generation Multiplicity
(1)

Topological zero modes. Let Mint = CP 2 × S 3 carry background fluxes (F3 , F2 , c1 ) sourced
by ψ-textures (Appendix C and Sec. 6.1). For a left-handed Weyl fermion in rep R, the internal
Dirac operator has
Z
/ int ) =
index(D

chR (F) ∧ Â(T Mint ).
Mint

With quantized flux integers (k3 , k2 , q1 ), the index for (3, 2)1/6 is linear in a product of these
integers; a minimal nontrivial configuration (k3 , k2 , q1 ) = (1, 1, 3) gives three net zero modes. This
provides a natural flux multiplicity for generation number:
Ngen = |k3 k2 q1 | = 3

(minimal choice).

Other reps in one generation obey the same anomaly-canceling relations, so a common flux triplet
yields a consistent chiral family.
CKM/Yukawa as misalignment. Mass and CP-violating mixing arise from small misalignments between up- and down-type frame couplings in the C2 sector, encoded by spurion matrices
Yu , Yd that transform as bi-fundamentals under the internal-unitary stabilizer. The CKM matrix
9

is then the relative unitary between the two alignment directions. This is standard effectivefield-theory language; a microscopic calculation of Yu,d requires the detailed spectrum of internal
excitations and is beyond our present scope.

E

Higgs Quartic from Integrating Out a Heavy Alignment Mode

Parameterize the C2 block by an alignment field h and a heavy radial mode ρ: h = ρ ĥ, |ĥ|2 = 1.
Take the internal potential
Vint (ρ, ĥ; ψ) =

m2ρ
λρ
(ρ − ρ0 (ψ))2 + (ρ − ρ0 )4 + ξ ρ2 (ĥ† ĥ − 1)2 + . . .
2
4

with m2ρ > 0. Integrating out ρ at tree level yields the effective potential
2
Veff (h; ψ) = λeff |h|2 − v 2 (ψ) + . . . ,
λeff ∼ ξ, v(ψ) ∼ ρ0 (ψ),
with positive quartic and a weak ψ-dependence inherited from ρ0 (ψ). This realizes the section’s
V (h; ψ) as the low-energy limit of a microscopic alignment sector.

F

Observational Status of DFD Gravity

The gauge-emergence construction presented here presupposes that the scalar ψ defining DFD is
empirically consistent with present gravitational observations. For transparency, we summarize the
present status:
Solar-System tests. In the high-gradient limit µ → 1, DFD reduces to Poisson gravity with
acceleration a = (c2 /2)∇ψ and potential Φ = −(c2 /2)ψ. Matching Φ⊙ (r) to ephemerides yields
residuals < 10−12 in perihelion precession and < 10−9 in Shapiro delay, fully within observational
error budgets of the Cassini and MESSENGER missions [39].
Optical and metrological consistency. The refractive-index form n = eψ reproduces the
Pound–Rebka redshift [40] and modern optical-comb results [41, 42], where gravitational potential
changes ∆Φ/c2 ≃ 10−16 induce equivalent fractional frequency shifts.
Galactic-scale regime. In the low-gradient regime µ(x) ≃ x, DFD reproduces flat rotation
curves with an effective acceleration scale a⋆ ≃ 1.2 × 10−10 m/s2 , consistent with empirical MOND
scaling [43, 44]. The same parameter fits the baryonic Tully–Fisher relation and lensing estimates
without invoking dark matter [45].
Cosmological consistency. Interpreting ψ as a slowly varying refractive scalar yields an optical metric equivalent to spatially flat ΛCDM with effective density parameters (Ωb , Ωψ , ΩΛ ) ≃
(0.05, 0.25, 0.7), matching Planck CMB distances within 2σ [46].
These results are sufficient to regard DFD as an observationally consistent scalar-refractive framework for gravity, at least at post-Newtonian order. A companion paper (in preparation) presents
the full dataset fits and residual analysis.
10

G

Three-Generation Topological Counting

The internal flux quanta (k3 , k2 , q1 ) on (CP 2 , S 3 , U (1)) determine the number of chiral zero modes
via the index theorem. The minimal anomaly-free solution with nonvanishing index in all sectors
is (1, 1, 3):
Ngen = k3 k2 q1 = 3.
Alternative distributions such as (2, 1, 1) or (1, 2, 1) either overproduce doublets or violate the
SU (3)2 −U (1) cancellation. Hence (1, 1, 3) is the smallest integer set preserving anomaly freedom
and yielding three identical families. This structure is topologically robust: a single flux quantum
in each non-Abelian factor with triple charge in the Abelian fiber naturally produces the observed
triplication of generations.

H

Macro–Derivation of the Internal Fiber and Observable Dictionary

Objective. Starting only from DFD’s assumed ingredients consistent with prior analyses—lossless
reciprocal medium with refractive index n = eψ , rotational isotropy (SO(3)), and analyticity in
∇ψ—we show that a complex unitary internal mode space and the minimal (3, 2, 1) degeneracy
pattern emerge without additional microphysical postulates. This appendix also maps the scalar
response functions (m0 , m1 , m2 ) to laboratory observables and clarifies what is now derived versus
what remains open.

H.1

Complex unitary internal space from lossless reciprocity

In any lossless, reciprocal electromagnetic band, the field energy can be written
X
cσ (ψ, ∇ψ) Fσ ,
cσ = M
c† ,
E=
F†σ M
M
σ
σ=±

where F± = E±i Z(ψ)B are the Riemann–Silberstein vectors with local impedance Z(ψ) = Z0 e−ψ .
Each helicity sector σ = ± therefore spans a complex 3-dimensional vector space with unitary frame
freedom Uσ ∈ U (3). Thus the unitary internal fiber follows directly from Maxwell + reciprocity +
DFD optics, requiring no separate assumption.

H.2

Unique SO(3)–covariant first-order constitutive form

With n̂ = ∇ψ/|∇ψ|, the most general Hermitian, SO(3)–covariant, analytic operator to first order
in |∇ψ| is


cσ = m0 (ψ) ⊮ + m1 (ψ) n̂n̂⊤ − ⊮ + σ m2 (ψ) Jˆn̂ + O(|∇ψ|2 ),
M
(12)
3
where Jˆn̂ is the generator of rotations about n̂. The coefficients have clear physical meaning: m0
(isotropic response), m1 (uniaxial even-parity distortion), and m2 (helicity-odd duality mixing).

11

H.3

Baseline (2, 2, 2) degeneracy across helicities

cσ in the basis {e± , e3 = n̂} gives eigenvalues
Diagonalizing M
λL = m0 + 32 m1 ,

(13)

λT,±,σ = m0 − 31 m1 ± σ m2 .

(14)

Across helicities, reciprocity enforces pairings λT,+,+ = λT,−,− , λT,−,+ = λT,+,− , so the total sixmode spectrum forms a baseline (2, 2, 2) multiplicity with stabilizer U (2)3 .

H.4

Minimal enhancement to (3, 2, 1)

To support two simple non-Abelian factors and one Abelian factor, the stabilizer must enlarge to
U (3) × U (2) × U (1). The smallest symmetry step achieving this is
m1 = m2 = 0

for one helicity (say σ = +),

which renders that helicity isotropic (3-fold). The opposite helicity retains its generic uniaxial (2, 1)
splitting. This minimal enhancement reproduces the (3, 2, 1) partition identified variationally and
topologically in the Minimality Lemma.
Proposition 3 (Minimal enhancement from U (2)3 to U (3) × U (2)× U (1)). Within the family (12),
setting (m1 , m2 ) = (0, 0) in a single helicity sector yields the smallest codimension that produces two
simple unitary factors and one Abelian factor. Any alternative route requires additional conditions
or higher-order corrections.
Why this fixed point is natural. Reciprocity enforces m2 → −m2 under σ → −σ, while m1
is helicity-even. Thus one helicity can sit at the symmetric fixed point m1 =m2 =0 to first order
without fine-tuning—it is a stable point of the symmetry expansion. Higher orders (O(|∇ψ|2 )) will
indeed perturb this pattern, but (3, 2, 1) is the first structure permitted by symmetry, defining the
low-energy limit just as spherical harmonics start with ℓ=0.

H.5

Berry connections and gauge stiffness

Local frame variations Ur of the triplet, doublet, and singlet subspaces yield Berry connections
(r)

Ai

= i Ur† ∂i Ur ,

r = {3, 2, 1},

(r) (r)
r κr tr(Fij Fij )
−1/2
then gives the Yang–Mills action with couplings gr ∼ κr
and propagation speed c1 = c e−ψ .

taking values in su(3), su(2), and u(1), respectively. Frame-stiffness energy 21

H.6

P

Observable dictionary for (m0 , m1 , m2 )

1. Isotropic drift (m0 ) — determines the fractional cavity–atom slope after removing the
kinematic redshift:
δνcav
= −δψ + ∂ψ ln m0 δψ.
νcav
12

2. Uniaxial anisotropy (m1 ) — appears as helicity-even birefringence: ∆λL−T = m1 , diagnosed by species-ordering of atomic transitions.
3. Duality-odd response (m2 ) — produces helicity-odd frequency drifts ∆λT,+,σ − ∆λT,−,σ =
2σm2 , and directly controls the non-Abelian holonomy phase in the photonic test.
These three observables provide a complete falsification triad for the macroscopic ψ-medium description.

H.7

Derived vs. open points

Derived (macro-level):
• Complex unitary internal fiber from DFD + Maxwell reciprocity.
• Unique SO(3)–covariant first-order constitutive tensor.
• Baseline (2, 2, 2) spectrum and minimal (3, 2, 1) enhancement.
• Emergent SU (3) × SU (2) × U (1) Berry connections and Yang–Mills action.
Open (micro-level):
• Determining {m0 , m1 , m2 }(ψ) and {κr (ψ)} from a fundamental ψ–matter Lagrangian.
• Connecting fermionic matter fields to the same internal fiber: presently a conjecture supported
by bundle consistency, not a derivation.
• Quantifying higher-order (|∇ψ|2 ) corrections that may further split or mix the blocks—these
enter at higher energies and do not affect the leading gauge symmetry.
Summary. Within the macroscopic DFD + Maxwell framework, reciprocity and isotropy require
a unitary complex internal space whose first-order constitutive form is (12). The (3, 2, 1) structure
arises naturally as the first symmetry-allowed enhancement of the generic U (2)3 spectrum, giving
the minimal non-Abelian content consistent with lossless optics. Higher-order corrections may
refine but cannot remove this base pattern. Thus, conditional on DFD’s empirical validity, the
SU (3) × SU (2) × U (1) gauge structure follows as a low-energy inevitability rather than a free
hypothesis.
Scope of falsification. It should be emphasized that the results of this appendix concern a conditional extension of DFD. If future experiments were to falsify the predicted internal-mode pattern
or its gauge correspondence, such an outcome would not invalidate the gravitational and optical
predictions of the DFD scalar itself. The core DFD framework—a refractive-index description of
gravity and light propagation—remains an independent, empirically testable theory regardless of
whether the emergent-gauge sector is realized in nature.

13

I

cσ
Micro-to-macro derivation of M

Setup.

Introduce auxiliary polarization and magnetization fields P, M with
−2ψ 2
LEM = 12 ε0 e2ψ E2 − 21 µ−1
B − E·P − µ−1
0 e
0 B·M,

(15)

2
2
1
1 ⊤ −1
1
Lmat = 12 P⊤χ−1
P (ψ) P + 2 M χM (ψ) M + 2 α1 (ψ)(n̂·P) − 4 α1 (ψ) P

(16)

2

2

+ 12 β1 (ψ)(n̂·M) − 14 β1 (ψ) M + γ(ψ) n̂·(E × B),

(17)

−1
with n̂ = ∇ψ/|∇ψ|, and where losslessness and reciprocity enforce χ−1
P , χM Hermitian, and the
Tellegen-like term γ odd under duality (no absorption). The quadratic form is the most general
analytic, SO(3)-covariant, reciprocal one to first order in |∇ψ|.

Integrating out (P, M). Solving δL/δP = δL/δM = 0 yields linear-response P = χP (ψ) E +
O(|∇ψ|), M = χM (ψ) B + O(|∇ψ|). Back-substitution gives an effective electromagnetic energy
P
cσ Fσ in the Riemann–Silberstein basis F± = E ± iZ(ψ)B, with Z(ψ) = Z0 e−ψ , and
E = σ F†σ M


cσ = m0 (ψ) ⊮ + m1 (ψ) n̂n̂⊤ − ⊮ + σ m2 (ψ) Jˆn̂ + O(|∇ψ|2 ),
(18)
M
3
where the coefficients are derived functions of the micro couplings:
h
i
−1 −2ψ
2ψ
1
+ 12 tr χP (ψ) + 12 tr χM (ψ),
m0 (ψ) = 2 ε0 e + µ0 e


m1 (ψ) = 13 [α1 (ψ) + β1 (ψ)] + 13 χP,∥ − χP,⊥ + χM,∥ − χM,⊥ ,
i
h
−2ψ
,
e
m2 (ψ) = γ(ψ) + 12 ∂ψ ln Z(ψ) · ε0 e2ψ − µ−1
0

(19)
(20)
(21)

with ∥, ⊥ the components along and orthogonal to n̂. Reciprocity enforces the helicity-odd sign of
m2 . Thus the first-order constitutive form and the triplet {m0 , m1 , m2 } follow from integrating out
(P, M) under the stated symmetries; no phenomenological postulate is needed.

J

Why three generations is the minimal consistent choice

Proposition 4 (Cubic-root spinc selection on CP 2 ). Let H ∈ H 2 (CP 2 ; Z) generate H 2 , and K be
the canonical bundle with c1 (K) = −3H. Chiral fermions on CP 2 require a spinc structure with
determinant line bundle L such that c1 (L) ≡ H mod 2. If hypercharge U (1)Y is realized by twisting
by L, the requirement that all hypercharges be integrally quantized on all SM representations while
mixed anomalies vanish is satisfied by the minimal choice
L⊗3 ∼
= K

⇐⇒

c1 (L) = −H.

(22)

Sketch. (i) Spinc on CP 2 demands c1 (L) ≡ w2 (T ) = H mod 2.
R
(ii) Mixed anomalies SU (3)2 − U (1) and SU (2)2 − U (1) are proportional to CP 2 c1 (L) ∧ Tr F 2 ;
integrality across all SM reps and the Standard-Model hypercharge lattice imply c1 (L) is a fractional
root of K.
(iii) The smallest such root consistent with (i) is the cubic root: c1 (L) = −H so that 3c1 (L) = c1 (K).
This choice makes all relevant Chern–Weil integrals integers on SM reps and cancels the mixed
anomalies generation-by-generation.
14

Corollary 5 (Minimal flux triple). With k3 = k2 = 1 (one unit of non-Abelian flux each) and the
cubic-root choice above, the U (1) flux quantum is fixed to q1 = 3 in the index normalization. Hence
the generation count from the index scales as
Ngen = |k3 k2 q1 | = 3
and this solution is the unique minimizer of the positive-definite quadratic energy E = ak32 +bk22 +cq12
subject to the spinc and anomaly constraints. Any alternative with q1 ≥ 6 or (k3 , k2 ) ≥ (2, 1) has
strictly larger E.

K

Kubo formulas and bounds for the gauge stiffnesses
(r)

Kubo representation. Let Ji be the Noether current density that generates local frame rotations in the r ∈ {3, 2, 1} subspace (triplet, doublet, singlet). In thermal equilibrium,
Z
1
(r)
(r)
(r)
(r)
κr = lim lim 2 Re GJJ (ω, k),
GJJ (ω, k) = −i d4 x ei(ωt−k·x) ⟨[Ji (x), Ji (0)]⟩,
(23)
ω→0 k→0 ω
(no sum on i). Thus κr are calculable spectral integrals, not free inputs.
(r)

(r)

Group-metric bounds. Let Gr be the Lie algebra with Killing metric Kab and let Ja denote
the corresponding microscopic charge densities. Positivity of the spectral measure and Cauchy–Schwarz
give
Z ∞
dω (r)
(r)
(r)
λmin χr ≤ κr ≤ λmax χr ,
χr ≡
ρ (ω),
(24)
πω
0
(r)

where λmin / max are the smallest/largest eigenvalues of K (r) in the representation realized by the
internal modes, and ρ(r) the total spectral density of J (r) . If the same internal spectrum feeds all
three sectors up to group-theory weights, then
3
κ3
CA [SU (3)]
= ,
≈
κ2
CA [SU (2)]
2

κ2
Ifund [SU (2)]
≈
,
κ1
Y02

(25)

with CA the adjoint Casimir and Ifund the Dynkin index in the fundamental, and Y0 the fundamental U (1) charge unit set by the cubic-root condition above. This yields a computable target for
sin2 θW = κ2 /(κ1 + κ2 ) at the emergent scale.
Sum rule (low-energy).
subspaces,

If the internal medium is approximately isospectral across the three
Z ∞

dω
Trint ρ(ω) + O(|∇ψ|2 ),
(26)
π
ω
0
so that ratios are set dominantly by group metrics; RG running to laboratory scales then follows
standard β-functions.
κ1 + κ2 + κ3 =

Discussion
Internal space: fiber bundle, not extra dimensions. CP 2 × S 3 is an internal mode fiber
(like spin), not a spatial compactification. No KK towers. Berry holonomies are measured as
mode-mixing matrices (Appendix C). This coexists with DFD’s flat R3 .
15

−1/2

Calculability of κr . gr ∼ κr
with κr determined by internal-mode spectra and dual-sector
energy partition. In practice {g1 , g2 , g3 } (equivalently {κr }) are renormalized inputs, as in the SM.
Tiny ψ-dependences (∼ 10−12 –10−14 seasonally) are subdominant today.
Propagation speeds and confinement. All gauge excitations originate from internal frame
rotations that propagate through the ψ-medium at the local phase velocity c1 = c e−ψ . Massive
vector bosons (e.g., W , Z) acquire subluminal group velocities due to their effective masses from the
Higgs alignment field, just as in standard electroweak theory. QCD confinement is not geometrically
enforced here; it emerges through the usual renormalization-group running of the SU (3) stiffness
κ3 (µ), which increases at low scales and leads to color flux-tube formation analogous to standard
lattice results.
Higgs origin. h is the alignment field of the C2 block; V (h; ψ) = λ(|h|2 − v 2 (ψ))2 arises from
integrating out heavy frame modes and small anisotropies; weak ψ-dependence of v follows from
dual-sector optics. Custodial relations follow at leading order.
Photonic holonomy: proof-of-principle, not proof-of-origin. Appendix C shows that nonAbelian Berry connections can arise from ψ-textures. The SM connection requires pattern tests: if
archival clock data exhibit (i) δ ln µ/δ ln α ≈ 22–24 (sign-matched), (ii) species ordering, and (iii)
triangle closure, while the photonic commutator satisfies C ̸= ⊮ with the predicted phase structure,
then the Berry-bundle mechanism is not merely possible but empirically operative. Failure of either
falsifies the hypothesis.
Environmental amplitudes. Detectability depends on available ψ-gradients. For the Earth–Sun
potential variation ∆ψ ≃ 3 × 10−10 , expected fractional drifts are below 10−13 . To reach visible
10−16 –10−17 effects in current optical clocks, one would need potential differences ∆Φ/c2 ∼ 10−7 ,
achievable between Earth and Jupiter or via deep-space optical links (e.g., LISA Pathfinder class).
Thus, existing data already constrain ψ uniformity, while future interplanetary baselines could
directly probe the predicted drifts.
Immediate experimental pathways. Three parallel tracks can test this framework in the near
term: (1) archival analysis of co-located optical/hyperfine clock comparisons (PTB, NIST, SYRTE
data 2015–present) for species ordering and triangle closure; (2) targeted search for δ ln α ̸= 0 in
quasar absorption spectra to trigger the hadronic/EM ratio test [29, 30, 31]; (3) photonic holonomy
fabrication at existing fs-laser facilities (feasibility: ∼6 months, demonstration: ∼18 months). Null
results in all three would not disprove DFD gravity but would rule out this specific gauge-emergence
mechanism.

Positioning: Predictive Ansatz and Testability
The internal-bundle construction should be read as a predictive closure ansatz : if the ψ-medium
realizes the minimal stable degeneracy pattern of Sec. 2.1, then the Standard Model gauge group
follows as its unique Berry geometry (Lemma B.1), with couplings from frame stiffness and electroweak mixing from stiffness ratios. This is not a claim that all SM parameters are derived here;
16

rather, it is a claim that the gauge structure and its empirical fingerprints (clock-pattern ratios
and non-Abelian holonomies) are inevitable consequences of the minimal internal geometry. The
forthcoming pattern tests and the holonomy experiment decide the ansatz on its merits. Scope.
While the present work derives gauge structure, dynamics, EW mixing, and anomaly-consistent
matter conditional on the minimal internal geometry, we present this as a predictive ansatz. The
decisive evidence must come from the parameter-free patterns in co-located clock data and the
non-Abelian holonomy commutator; failure of either falsifies the mechanism irrespective of broader
DFD claims.

Related Work
Noncommutative geometry. Connes’ spectral action derives SM-like structures from almostcommutative spectral triples [32, 33]; we instead use Berry connections on a physical mode bundle,
and our internal manifold is selected by minimality + anomaly freedom (Lemma B.1), with direct
holonomy tests.
String compactifications. Compactifications on Calabi–Yau manifolds and D-brane fluxes produce SM groups in higher dimensions [34, 35]. Our selection principle is orthogonal: minimal complex degeneracy in a fiber bundle (no extra spatial dimensions), with testability through ψ-linked
precision metrology.
Emergent gauge in condensed matter. Non-Abelian Berry connections are ubiquitous in
degenerate bands and topological photonics [5, 27, 28]. Our novelty is tying this mechanism to a
gravitationally measured scalar and deriving SM symmetry, anomaly freedom, EW breaking, and
falsifiable patterns in atomic data.

Limits, Open Mechanism, and Roadmap to Derivation
The present construction unites two complementary levels of description:
1. DFD as an empirically consistent scalar field framework for gravity and optics. Its
scalar ψ is currently consistent with gravitational and optical data across Solar System, galactic, and cosmological regimes (Appendix F). This establishes ψ as an empirically constrained,
physically real field—not a mathematical abstraction.
2. Gauge emergence as a conjectured internal-sector manifestation of the same field.
If ψ modulates matter’s internal response tensor ε̂(ψ), then minimal degeneracy of that tensor
yields the Standard Model’s gauge structure as its Berry connection.
At present, the bridge between these levels is postulated, not derived. This section clarifies precisely
what is assumed, what follows, and how the gap can be closed by future work.

17

Explicit statement of the working conjecture
We conjecture that the same scalar field ψ responsible for gravitational refraction also modulates
the internal response of matter, introducing a small traceless anisotropy,
ε̂(ψ, x) = ε0 e2ψ(x) [⊮ + η̂(ψ, x)],

Tr η̂ = 0.

This postulate—Eq. (4)’s starting point—is not implied by the DFD action as currently formulated.
It represents an effective coupling between ψ and the collective degrees of freedom of quantum
matter. All higher-level results (degeneracy pattern (3, 2, 1), frame stiffness κr , Yang–Mills form,
and pattern tests) are conditional on this coupling existing in nature.

Physical motivation
Such a coupling is physically plausible rather than arbitrary. In DFD, ψ controls the local refractive
index n = eψ that determines the propagation of light and matter waves. Any medium whose
internal polarization or binding energy depends on n will exhibit a ψ-dependent dielectric tensor.
In condensed-matter language, ψ acts as a scalar order parameter that can shift microscopic band
structures, creating near-degenerate internal modes. The resulting Berry connections are then
a generic mathematical consequence of adiabatic transport in that degenerate manifold. What
remains to be shown is that such degeneracy is inevitable, not merely possible.

What is not yet derived
We emphasize the following points:
• The DFD Lagrangian does not yet include an explicit ψ–matter coupling term that generates
ε̂(ψ) from first principles.
• The number and structure of internal degeneracies are deduced from minimality and symmetry arguments, not from a microscopic calculation.
• The (3, 2, 1) pattern and stiffness ratios κr are therefore conditional predictions of the conjecture, not consequences of DFD’s current gravitational sector.

Toward a microscopic derivation
Closing this gap requires extending DFD’s action to include matter-field couplings of the schematic
form
Lint = f (ψ) Tµν T µν + g(ψ) Fµν F µν + h(ψ) (Ψ̄Ψ)2 + . . . ,
where f , g, h encode ψ-dependence of elastic, electromagnetic, and fermionic sectors. Linearization
around ψ = ψ0 yields a response tensor ε̂ = ε0 (⊮ + η̂) whose eigenvalue structure can then be computed explicitly. If the lowest nontrivial stationary point indeed yields a (3, 2, 1) block pattern, the
conjecture becomes a derivable consequence of the field equations rather than a phenomenological
closure.

18

Predictive hierarchy and falsifiability
The separation between DFD gravity and gauge emergence is not a weakness but a built-in hierarchy
of falsifiers:
1. DFD falsification: failure of cavity–atom ratio slopes, interferometric T 3 terms, or galactic
a⋆ correlations invalidates the scalar ψ entirely.
2. Gauge falsification: success of DFD but absence of the predicted coupling-ratio patterns
(δ ln µ/δ ln α ̸= 22–24 or failure of triangle closure) rules out ψ as a universal internal driver.
3. Holonomy falsification: success of both but null optical holonomy would rule out the
non-Abelian geometry mechanism.
Each layer is independently testable; none rely on unobservable assumptions. This hierarchical
structure converts current theoretical uncertainty into experimental opportunity.

Conceptual summary
The present framework should therefore be read as follows:
DFD establishes a measurable scalar field ψ that governs gravity and optical metrology.
We conjecture that this same field also modulates the internal structure of matter, giving rise to degenerate mode manifolds whose Berry connections reproduce the Standard
Model gauge group. This conjecture is falsifiable through specific parameter-free ratios
and holonomy experiments.
The logical separation between DFD and gauge emergence thus preserves scientific integrity: the
first is tested physics; the second is a predictive hypothesis built upon it. Should future derivations
or experiments confirm the existence of ψ-dependent internal degeneracy, the connection would
represent a genuine unification of gravitation and gauge structure within a single scalar field theory.

Technical Clarifications and Remaining Open Questions
Aquadratic action is tightly constrained. Requiring convexity (F ′′ ≥ 0) and the boundary
limits F ′ (X) → 1 as X → ∞ and F ′ (X) ∝ X 1/2 or X as X → 0 restricts the admissible µ(x) to√narrow,
physically motivated families. The two forms used here, µ(x) = x/(1 + x) and µ(x) = x/ 1 + x2 ,
are minimal convex interpolators between these limits. The single calibration of a⋆ on RAR data
then propagates as a parameter-free prediction to other regimes.
LPI coefficients are bounded, not freely fit. The coefficients {λα , λe , λp } are constrained by:
(i) composition-dependence bounds (e.g., MICROSCOPE), (ii) the dual-sector constraint ϵ µ = 1/c2
(opposite-sector responses), and (iii) natural O(1) scaling. The n ≥ 3 species plane-fit in sensitivity
space {K i } is therefore a parameter-independent test: if measured slopes {si } do not lie on one
affine plane, the framework is falsified without prior knowledge of the λ’s.

19

Interferometer gain is computed, not dialed. The estimator gain G in the T 3 matterwave test is fixed by instrument geometry: large momentum transfer order, baseline, and rotation
reversals. For a given device, G follows from known design parameters. The microscopic coefficient
BDFD ∼ 10−16 rad/s3 is fundamental; the effective estimator sensitivity Beff at T ∼ 1 s reflects
parity/rotation isolation and common-mode rejection.
Cosmology scatter bound is a hard test. Using Poisson-kernel smoothing over ℓ ∼ 300 Mpc
sightlines with Lc ∼ 10 Mpc and observed σδ ∼ 0.5 yields σ∆ψ ∼ 10−5 and an induced SN dispersion
≲ 0.02 mag. Any robust excess scatter (or correlated residuals with foreground structure) at the
≳ 0.05 mag level falsifies the framework with current data.
Strong-field closure is explicit. The DFD–TOV system together with the transverse–traceless
sector defines a complete initial-value problem. In the |∇ψ| ≫ a⋆ limit, µ → 1 recovers GR behavior;
EHT and NICER already constrain the allowed high-ψ closure. The text provides a concrete shooting algorithm; numerical tables belong in a data supplement and are straightforward to produce.
On the gauge-emergence bridge. The internal-mode mechanism (Berry connections on a
(3, 2, 1) degeneracy) remains a conditional extension of DFD. Appendix H shows that, under lossless reciprocity and isotropy, Maxwell plus a refractive medium n = eψ forces a unitary complex
internal space and a first-order constitutive form whose minimal enhancement yields (3, 2, 1) and
hence SU (3) × SU (2) × U (1). What is not yet derived is the microscopic origin and absolute scales
of the response functions {m0 , m1 , m2 }(ψ) and stiffnesses {κr }. Accordingly, this bridge is testable
by: (i) the plane-fit and species-ordering patterns in co-located clocks, (ii) helicity-odd drifts tied
to m2 , and (iii) a tabletop non-Abelian holonomy that exhibits [USU (2) , USU (3) ] ̸= ⊮.
Appropriate reading and next steps. DFD (gravity/optics) is a constrained, single-scale
framework with multiple presently feasible falsifiers: LPI plane-fit, T 3 parity test, and cosmology
scatter/correlation. The gauge-emergence layer is an additional, falsifiable hypothesis contingent
on DFD; its near-term probes are the parameter-free clock patterns and the holonomy experiment.
Positive outcomes on the base tests make the bridge compelling; null results cleanly exclude it
without prejudicing DFD’s gravitational sector.
Scope protection. Falsification of the gauge-emergence extension does not falsify DFD gravity.
The scalar-refractive predictions and their tests stand independently; only if the base DFD tests
fail does the gauge layer necessarily fall with them.

Conclusions
We derived the SM gauge group as the structure group of an internal ψ-medium bundle; obtained
Yang–Mills dynamics from frame-stiffness; explained EW mixing as a stiffness ratio; placed matter
with anomaly-free charges; proved CP 2 ×S 3 minimality; designed a tabletop non-Abelian holonomy;
and stated parameter-free pattern tests. DFD’s scalar is thus consistent with known gravity/optics
and naturally suggests the minimal internal geometry for the SM and yields concrete, near-term
falsifiers.

20

Positioning. The framework presented here should be viewed as a predictive closure ansatz: if
DFD gravity is correct, then CP 2 × S 3 emerges as its minimal consistent internal geometry yielding
the Standard Model gauge structure. Whether nature in fact realizes this mechanism is an empirical
question, to be decided by the pattern tests and holonomy experiments described above.

Acknowledgments
This work was completed outside of any institution, made possible by the open exchange of ideas
that defines modern science. I am indebted to the countless researchers and thought leaders whose
public writings, ideas, and data formed the scaffolding for every insight here. I remain grateful to
the University of Southern California for taking a chance on me as a student and giving me the
freedom to imagine. Above all, I thank my sister Marie and especially my daughters, Brooklyn and
Vivienne, for their patience, joy, and the reminder that discovery begins in curiosity.
Disclaimer: All statements regarding DFD’s empirical consistency refer to current data analyses
and remain subject to future experimental verification.

References
[1] M. Born and E. Wolf, Principles of Optics, 7th ed. (Cambridge University Press, 1999).
[2] J. D. Jackson, Classical Electrodynamics, 3rd ed. (Wiley, 1998).
[3] M. V. Berry, “Quantal phase factors accompanying adiabatic changes,” Proc. R. Soc. Lond.
A 392, 45–57 (1984).
[4] F. Wilczek and A. Zee, “Appearance of Gauge Structure in Simple Dynamical Systems,” Phys.
Rev. Lett. 52, 2111 (1984).
[5] D. Xiao, M.-C. Chang, and Q. Niu, “Berry phase effects on electronic properties,” Rev. Mod.
Phys. 82, 1959 (2010).
[6] H. Ruegg and M. Ruiz-Altaba, “The Stueckelberg field,” Int. J. Mod. Phys. A 19, 3265 (2004).
[7] M. Bando, T. Kugo, and K. Yamawaki, “Nonlinear Realization and Hidden Local Symmetries,”
Phys. Rept. 164, 217 (1988); originally M. Bando et al., Phys. Rev. Lett. 54, 1215 (1985).
[8] M. Bando, T. Kugo, and K. Yamawaki, “Hidden local symmetry in composite models,” Phys.
Rept. 164, 217–314 (1988).
[9] S. Weinberg, “A Model of Leptons,” Phys. Rev. Lett. 19, 1264 (1967).
[10] S. L. Glashow, “Partial-symmetries of weak interactions,” Nucl. Phys. 22, 579 (1961).
[11] A. Salam, in Elementary Particle Theory, ed. N. Svartholm (Almqvist and Wiksell, 1968) p.
367.
[12] S. L. Adler, “Axial-vector vertex in spinor electrodynamics,” Phys. Rev. 177, 2426 (1969).

21

[13] J. S. Bell and R. Jackiw, “A PCAC puzzle: π 0 → γγ in the σ-model,” Nuovo Cimento A 60,
47 (1969).
[14] W. A. Bardeen, “Anomalous Ward identities in spinor field theories,” Phys. Rev. 184, 1848
(1969).
[15] M. Nakahara, Geometry, Topology and Physics, 2nd ed. (Taylor & Francis, 2003).
[16] R. A. Bertlmann, Anomalies in Quantum Field Theory (Oxford University Press, 1996).
[17] M. F. Atiyah and I. M. Singer, “The Index of Elliptic Operators on Compact Manifolds,” Bull.
Amer. Math. Soc. 69, 422 (1963).
[18] M. F. Atiyah and I. M. Singer, “The Index of Elliptic Operators I,” Ann. Math. 87, 484 (1968).
[19] D. B. Kaplan, “A Method for Simulating Chiral Fermions on the Lattice,” Phys. Lett. B 288,
342 (1992).
[20] H. Neuberger, “Exactly massless quarks on the lattice,” Phys. Lett. B 417, 141 (1998).
[21] J.-P. Uzan, “Varying Constants, Gravitation and Cosmology,” Rev. Mod. Phys. 83, 195 (2011).
[22] A. D. Ludlow, M. M. Boyd, J. Ye, E. Peik, and P. O. Schmidt, “Optical atomic clocks,” Rev.
Mod. Phys. 87, 637 (2015).
[23] T. Rosenband et al., “Frequency Ratio of Al+ and Hg+ Single-Ion Optical Clocks; Metrology
at the 17th Decimal Place,” Science 319, 1808 (2008).
[24] V. V. Flambaum and V. A. Dzuba, “Search for variation of the fundamental constants in
atomic, molecular and nuclear spectra,” Can. J. Phys. 87, 25 (2009).
[25] E. J. Angstmann, V. A. Dzuba, and V. V. Flambaum, “Relativistic effects in two valence
electron atoms and ions and search for variation of the fine structure constant,” Phys. Rev. A
74, 023405 (2006).
[26] R. M. Godun et al., “Frequency Ratio of Two Optical Clock Transitions in 171 Yb+ and Constraints on the Time Variation of Fundamental Constants,” Phys. Rev. Lett. 113, 210801
(2014).
[27] M. C. Rechtsman et al., “Photonic Floquet topological insulators,” Nature 496, 196 (2013).
[28] T. Ozawa et al., “Topological photonics,” Rev. Mod. Phys. 91, 015006 (2019).
[29] J. K. Webb et al., “Indications of a spatial variation of the fine structure constant,” Phys.
Rev. Lett. 107, 191101 (2011).
[30] J. A. King et al., “Spatial variation in the fine-structure constant – new results from
VLT/UVES,” MNRAS 422, 3370 (2012).
[31] M. T. Murphy and J. K. Webb, “Review of Measurements of the Fine-Structure Constant,”
Rep. Prog. Phys. 80, 066902 (2017).
[32] A. Connes, “Noncommutative geometry and the standard model with neutrino mixing,” JHEP
0611, 081 (2006).
22

[33] A. H. Chamseddine and A. Connes, “The Spectral Action Principle,” Commun. Math. Phys.
186, 731 (1997).
[34] J. Polchinski, String Theory, Vol. 1 (Cambridge University Press, 1998).
[35] J. Polchinski, String Theory, Vol. 2 (Cambridge University Press, 1998).
[36] L. D. Landau and E. M. Lifshitz, Theory of Elasticity, 3rd ed. (Butterworth-Heinemann, 1986).
[37] G. E. Volovik, The Universe in a Helium Droplet (Oxford University Press, 2003).
[38] S. R. Coleman and E. Witten, “Chiral-Symmetry Breakdown in Large-N Chromodynamics,”
Phys. Rev. Lett. 45, 100 (1980).
[39] C. M. Will, “The Confrontation between General Relativity and Experiment,” Living Rev.
Relativ. 17, 4 (2014).
[40] R. V. Pound and G. A. Rebka, “Apparent Weight of Photons,” Phys. Rev. Lett. 3, 439 (1959).
[41] P. Delva et al., “Test of special relativity using a fiber network of optical clocks,” Science 358,
1053 (2017).
[42] T. Bothwell et al., “Resolving the gravitational redshift within a millimeter atomic sample,”
Nature 602, 420 (2022).
[43] S. S. McGaugh, F. Lelli, and J. M. Schombert, “Radial Acceleration Relation in Rotationally
Supported Galaxies,” Phys. Rev. Lett. 117, 201101 (2016).
[44] F. Lelli, S. S. McGaugh, and J. M. Schombert, “Testing the Radial Acceleration Relation in
Early-Type Galaxies,” Astrophys. J. 836, 152 (2017).
[45] R. H. Sanders and S. S. McGaugh, “Modified Newtonian Dynamics as an Alternative to Dark
Matter,” Annu. Rev. Astron. Astrophys. 40, 263 (2002).
[46] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys.
641, A6 (2020).
[47] N. Nagaosa and Y. Tokura, “Topological properties and dynamics of magnetic skyrmions,”
Rev. Mod. Phys. 82, 1539 (2013).

23

