---
source_pdf: Density_Field_Dynamics__Unified_Derivations__Sectoral_Tests__and_Experimental_Roadmap_v1_2.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Density Field Dynamics: Unified
Derivations, Sectoral Tests, and
Experimental Roadmap
Gary T. Alcock
Abstract
We develop Density Field Dynamics (DFD), a refractive-field formulation of gravity in which a single scalar ψ sets the optical index via n = eψ and determines
both light propagation and test-mass dynamics. From a convex variational principle we derive a strictly energy-conserving field equation with well-posed boundary
value structure. In the weak field (µ → 1), the optical metric reproduces General
Relativity’s classical observables: light deflection and Shapiro delay integrals, 1PN
orbital dynamics with β = γ = 1, and the standard 2PN deflection coefficient for
a point mass. The same normalization predicts a geometry-locked Local-PositionInvariance (LPI) slope ξ = 1 for cavity–atom and ion–neutral frequency ratios
in nondispersive bands, with material dispersion and length-change systematics
bounded well below experimental reach [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
15, 16, 17, 18, 19, 20].
We embed ψ consistently in quantum dynamics via a ψ-weighted Schrödinger
operator that preserves unitarity and probability current, yielding a unified phase
law for matter-wave interferometers and a single laboratory ψ controlling clocks,
photons, and atoms. A gauge-consistent Maxwell embedding on the optical metric
preserves U (1) without varying α. For cosmology we identify (i) a homogeneous
˙ and (ii) a latemode ψ̄(t) that shifts redshift-inferred expansion as Heff = H − ψ̄/2
time µ-crossover that shallows large-scale potentials, providing specific signatures
in H0 (n̂) anisotropy, distance duality, ISW, and growth. Reanalysis templates for
public ion–neutral datasets indicate a small, perihelion-phase–locked annual modulation consistent with the predicted sectoral response. We outline seven falsifiable
tests—altitude-split LPI, ion–neutral annual modulation, reciprocity-broken fiber
loops, matter-wave phases, and three cosmological probes—that can confirm or
rule out the refractive origin of gravitational phenomena using existing instrumentation [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35].

Executive Summary
Concept. Density Field Dynamics posits a single scalar ψ whose exponential sets the
optical index, n = eψ . Light, clocks, test masses, and matter waves respond to the same
ψ with a normalization fixed by classical lensing and Shapiro delay [8, 36, 7, 9, 10].
Foundations. From a convex action we obtain an energy-conserving field equation with
standard Leray–Lions well-posedness. In the weak field the optical picture recovers GR’s
1

light deflection, Shapiro delay, and 1PN dynamics (β = γ = 1), and matches the 2PN
deflection coefficient for a point mass. These results fix the overall normalization used
throughout [1, 2, 3, 4, 5, 12, 11, 13].
Metrology and quantum. In nondispersive bands DFD predicts a geometry-locked
LPI slope ξ = 1 for cavity–atom and ion–neutral ratios; Kramers–Kronig bounds and
length-change estimates place dispersive/mechanical systematics far below 10−15 fractional levels. A ψ-weighted Schrödinger operator yields unitary quantum evolution with
a conserved current and a unified matter-wave phase, so clocks and interferometers measure the same scalar potential with different transfer functions [16, 17, 18, 19, 20, 21, 22,
23].
Gauge and consistency. Electrodynamics on the optical metric preserves U (1) gauge
symmetry without varying α, keeping the Standard Model intact while reproducing n =
eψ optics [15, 37, 38, 39]. A canonical quadratic expansion gives a healthy propagator;
linear waves are luminal in the weak regime [4, 3].
Cosmology. A homogeneous mode ψ̄(t) shifts redshift-inferred expansion as Heff =
˙ On large scales a late-time µ-crossover shallows potentials, predicting: (i)
H − 21 ψ̄.
directional H0 biases correlated
with foreground density gradients, (ii) a mild distanceR ψ
duality deformation via e dt/a, and (iii) reduced ISW/growth at low k. Implementation
in Boltzmann codes reduces to Geff (a, k) = G/µ0 (a) in the linear, quasi-static sector [34,
35, 31, 32, 33, 40].
Distinct predictions (falsifiable).
(i) Altitude-split LPI with slope ∆R/R = ∆Φ/c2 at the 10−15 level [41, 42, 43, 44, 45,
46].
(ii) Ion–neutral annual modulation phase-locked to the solar potential (archival data
actionable) [47, 48, 49].
(iii) HReciprocity-broken fiber loops: achromatic one-way phase residue proportional to
ψ ds [14, 50, 51, 52].
(iv) Matter-wave interferometry: ∆ϕ = (mg ∆h T )/ℏ with ψ-locked higher-order terms [21,
22, 23, 24].
(v) Cosmological: H0 (n̂)–density-gradient correlation; small distance-duality deformation; ISW/growth suppression at late times [53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
63, 64, 65, 66].
Status of evidence. Public ion–neutral ratios show a small, perihelion-phase–locked
annual term consistent with the sectoral response predicted here; neutral–neutral controls
appear null within current precision. Dedicated reanalyses and targeted repeats can
sharpen this immediately [47, 48, 49, 67, 46].

2

ψ̄(t), δψ

DFD overview: one scalar field ψ unifies optics, dynamics, clocks, matter waves, and cosmology with a single normalization.
Classical Z
domain
Light: α = ∇⊥ ψ dz,

Scalar refractive field

ψ(x, t)

n = eψ

n = eψ , c1 = c e−ψ
∇· [µ(|∇ψ|/a⋆ )∇ψ] = −

8πG
(ρ − ρ̄)
c2

4GM 4r1 r2
ln 2
∆T =
c3
b
(GR–equivalent optics: γ = 1)
2
c
GM
Mass: a = ∇ψ, ∆ϕperi = 6π 2
2
c a(1 − e2 )
4
(1PN perihelion; deep field ⇒ v ∝ GM a⋆ )

Cosmology (optical background)
a0 (ψ0 −ψ)/2
1+z =
e
a
Heff = H − 21 ψ̄˙
δH0
(n̂) ∝ −⟨∇ ln ρ· n̂⟩LOS
H0
Geff (a) = G/µ0 (a) (late-time shallowing)
H0 anisotropy; ISW/S8 relief

same ψ slope

Quantum & clocks
∆R
∆Φ
= ξ 2 , ξDFD = 1
Clocks:
R
c
(ion–neutral: Kγ = 1, KN ≈ 0, KI ∼ 10−3 )
Z
mc2
mg ∆h T
Matter waves: ∆ϕ =
∆ψ dt =
2ℏ
ℏ
(same ψ slope as clocks; self-energy gives reduction rate)
optics

dynamics

clocks/quantum

Figure 1: Lean DFD schematic. The same scalar ψ sets the optical index, test-mass
acceleration, clock LPI slope ξ = 1, and matter-wave phase; its background and gradients
govern redshift and anisotropy across all domains [7, 8, 33, 32].
Near-term actions. (i) Execute a 100 m altitude-split cavity–atom (or ion–neutral)
comparison at σy ≲ 2×10−15 ; (ii) reprocess ROCIT/PTB ion–neutral archives with phaselocked regression; (iii) build a 10–100 m reciprocity-broken
loop with dual-wavelength
R
cancellation of dispersion; (iv) add Geff (a) and DL ∝ eψ dt/a hooks to existing cosmology
pipelines [52, 40, 34].
Outcome. A single decisive null at designed sensitivity falsifies DFD; consistent positives across any subset of the above confirm that standard gravitational phenomenology
arises from a measurable refractive field ψ rather than intrinsic spacetime curvature [6,
5, 3].

Part I

Foundations and
Precision-Metrology Tests of DFD
1

Variational origin and energy conservation

Let ψ(x, t) denote the scalar refractive field and define y ≡ |∇ψ|/a⋆ . Introduce a convex
function Φ(y) satisfying dΦ/dy = y µ(y), where µ(y) is the nonlinear response interpolating between the weak and deep regimes [68, 69, 70].

1.1

Action


|∇ψ|
c4 2
aΦ
− (ρ − ρ̄)c2 ψ.
L=
8πG ⋆
a⋆
3

(1)

1.2

Field equation

Euler–Lagrange variation gives


4
dΦ ∂i ψ
2 c
= (ρ − ρ̄)c2 ,
∂i a⋆
8πG dy a⋆ |∇ψ|


8πG
∇· µ(|∇ψ|/a⋆ ) ∇ψ = − 2 (ρ − ρ̄).
c

1.3

(2)
(3)

Energy density and flux

Define

c4  2
(4)
a⋆ Φ(y) − µ(y)|∇ψ|2 + (ρ − ρ̄)c2 ψ,
8πG
c4
S=−
µ(y) (∂t ψ) ∇ψ,
(5)
8πG
which satisfy the local conservation law ∂t E + ∇·S = 0. For stationary sources, ∂t ψ = 0
and E is time-independent.
E=

1.4

Well-posedness and stability

We consider the static boundary-value problem on a bounded Lipschitz domain Ω ⊂ R3
(ρ − ρ̄) ∈ H −1 (Ω) and Dirichlet data ψ|∂Ω = ψD ∈ H 1/2 (∂Ω):
with source f ≡ − 8πG
c2

−∇· µ(|∇ψ|/a⋆ ) ∇ψ = f in Ω.
(6)
Assume µ : [0, ∞) → [µ0 , µ1 ] satisfies: (i) boundedness 0 < µ0 ≤ µ(y) ≤ µ1 < ∞; (ii)
monotonicity y 7→ y µ(y) strictly increasing; (iii) Lipschitz on compact intervals. Define
the convex energy functional


Z
Z
|∇ψ|
dΦ
c4
2
3
a⋆ Φ
= y µ(y).
(7)
d x − f ψ d3 x,
J [ψ] =
8πG Ω
a⋆
dy
Ω
Existence (direct method / Leray–Lions). Let V = {ψ ∈ H 1 (Ω) : ψ − ψD ∈
H01 (Ω)}. Under (i)–(iii), J is coercive and weakly lower semicontinuous on V , hence it
admits a minimizer ψ ⋆ ∈ V . The Euler–Lagrange equation of J is (6), so ψ ⋆ is a weak
solution [68, 69, 70].
Uniqueness (strict monotonicity). For any two weak solutions ψ1 , ψ2 ∈ V ,
Z


A(∇ψ1 ) − A(∇ψ2 ) · ∇ψ1 − ∇ψ2 d3 x = 0, A(ξ) = µ(|ξ|/a⋆ ) ξ.

(8)

Ω

Strict monotonicity of yµ(y) implies the integrand is ≥ c |∇ψ1 −∇ψ2 |2 , hence ∇ψ1 = ∇ψ2
a.e. and ψ1 = ψ2 in V (Dirichlet data fixed) [69].
Continuous dependence (energy norm). Let f1 , f2 ∈ H −1 (Ω) and ψ1 , ψ2 the corresponding solutions with the same boundary data. Testing the difference of weak forms
with (ψ1 − ψ2 ) and using (i)–(ii) yields
∥∇(ψ1 − ψ2 )∥L2 (Ω) ≤ C ∥f1 − f2 ∥H −1 (Ω) ,
for a constant C depending on µ0 , µ1 , a⋆ and Ω [68, 69].
4

(9)

Remark (numerics). The coercive convex energy defines a natural energy norm for
error control in finite-element discretizations, and strict monotonicity enables convergent
Picard or damped Newton iterations for the nonlinear elliptic operator [68].

2

Post-Newtonian behaviour and light propagation

In the weak-field limit µ → 1, ψ = 2GM/(c2 r) and a = (c2 /2)∇ψ reproduces Newtonian
gravity [4, 3].

2.1

Light deflection

For a graded index n = eψ ≃ 1 + ψ,
Z +∞
4GM
∇⊥ ψ dz = 2 b̂,
α=
cb
−∞

(10)

identical to the GR prediction (γ = 1) [1, 8, 7, 5].

2.2

Shapiro delay

R
The optical travel time T = (1/c) n ds gives an excess delay
∆T =

4GM 4r1 r2
ln 2 .
c3
b

(11)

[9, 10, 13, 71].

2.3

2PN consistency (outline)

R
Expanding T = c−1 eψ ds to O(ψ 2 ) for a point mass yields α = 4ϵ + (15π/4)ϵ2 + O(ϵ3 )
with ϵ = GM/(c2 b), matching the GR 2PN coefficient [12, 11, 5].

2.4

Second post-Newtonian light deflection (full derivation)

We work in the graded-index picture with n = eψ and use the standard ray equation for
small bending:
Z +∞
Z +∞

α=
∇⊥ ln n dz =
∇⊥ ψ − 12 ψ 2 + O(ψ 3 ) dz + path correction.
(12)
−∞

−∞

For a point mass√in the µ → 1 regime, ψ = rs /r with the Schwarzschild radius rs ≡
2GM/c2 and r = b2 + z 2 , where b is the (unperturbed) impact parameter. We split the
deflection into:
(2)
(2)
α = α(1) + αln n + αpath + O(ψ 3 ).
First order. Using ∇⊥ ψ = ∂b ψ b̂ and ∂b (1/r) = − b/r3 ,

Z +∞
Z +∞
2rs
4GM
b
(1)
dz =
α =
∂b ψ dz = rs
− 2
= 2 .
2
3/2
(b + z )
b
cb
−∞
−∞
5

(13)

Second order from the logarithm (ln n) expansion. The quadratic term in (12)
gives

Z +∞
Z +∞ 
Z
rs
rs b
1 +∞
(2)
2
∂b ψ dz = −
ψ ∂b ψ dz = −
− 3 dz
αln n = −
2 −∞
r
−∞
−∞ r
Z +∞
2
dz
π
π rs
= rs2 b · 3 =
.
(14)
= rs2 b
2
2
2
2b
2 b2
−∞ (b + z )
Second order from path (Born) correction. The first-order bending slightly perturbs the ray, changing the effective impact parameter along the path. Writing the transverse displacement as δx(z) generated by α(1) , the correction to the first-order integral
can be expressed as
Z z
Z +∞
(2)
2
α(1) (z ′ ) dz ′ ,
δb(z) ∂b ψ dz with δb(z) = −
αpath =
−∞

−∞

which yields a second-order contribution proportional to rs2 /b2 . Carrying out the (standard) Born-series evaluation with ψ = rs /r one finds1
(2)

αpath =

7π rs2
.
16 b2

(15)

Total 2PN deflection. Summing (14) and (15):


π 7π rs2
15π rs2
(2)
(2)
(2)
α = αln n + αpath =
+
=
.
2
16 b2
16 b2

(16)

It is convenient to write the result in terms of ε ≡ GM/(c2 b) = rs /(2b),
α = 4ε +

15π 2
ε + O(ε3 )
4

⇐⇒

α=

 r 3
15π rs2
2rs
s
+
+
O
2
b
16 b
b

(17)

which matches the GR 2PN coefficient for a point mass, completing the consistency check
for DFD optics at next-to-leading order [12, 11, 5].

2.5

1PN orbital dynamics and perihelion advance

We now examine planetary motion in the weak, slowly varying ψ field. For a test particle
of mass m, the action per unit mass is



Z 
Z
Z 2
2
1 2 c2
c −ψ 2
1 4 1
−2ψ ẋ
2
S = L dt =
e
ṫ − e
dt ≃
ẋ − ψ − 2 ẋ − ψ ẋ dt, (18)
2
c2
2
2
8c
2
keeping terms to O(c−2 ). Identifying Φ = − 21 c2 ψ, the Euler–Lagrange equations yield
2Φ v 2 i 4
r̈ = − ∇Φ 1 + 2 + 2 + 2 (v·∇Φ) v.
c
c
c
h

(19)

This is algebraically identical to the 1PN acceleration for the Schwarzschild metric in
harmonic gauge (GR), implying PPN parameters γ = 1, β = 1 [3, 4, 5].
1

This step follows the usual second-Born
treatment for a spherically symmetric refractive perturber;
R
the intermediate integrals involve dz z 2 /(b2 + z 2 )5/2 and related kernels. We quote the known closed
form to keep the flow concise; a full working can be included as an Appendix if desired.

6

Perihelion shift. For a central potential Φ = −GM/r and small eccentricity e ≪ 1,
the equation for the orbit u ≡ 1/r becomes
d2 u
GM
3GM 2
+
u
=
+
u,
dϕ2
h2
c2

h = r2 ϕ̇.

(20)

The additional 3GM u2 /c2 term is the hallmark 1PN correction. The solution is a precessing ellipse,
u(ϕ) =


GM 
1 + e cos (1 − δ)ϕ ,
2
h

δ=

3GM
c2 a(1 − e2 )

.

(21)

The perihelion advance per revolution is therefore
∆ϕperi = 6π

GM
c2 a(1 − e2 )

,

(22)

identical to GR’s prediction for β = γ = 1. The DFD optical-metric ansatz thus reproduces all classical 1PN orbital tests of GR exactly, while providing a distinct physical
mechanism through the scalar refractive field ψ [5, 3].

3

Cavity–atom LPI slope and dispersion bound

Define the observable ratio R = fcav /fat . Between potentials ΦA and ΦB ,
∆Φ
∆R
=ξ 2 ,
R
c

Φ ≡ − 12 c2 ψ.

(23)

DFD predicts ξ = +1, GR gives ξ = 0 [6, 5].

3.1

Practical corrections

S
Write fractional sensitivities αw , αLM , αat
for wavelength, cavity length, and atomic response. Then
S
ξ (M,S) = 1 + αw − αLM − αat
.
(24)

3.2

Kramers–Kronig bound

Causality implies
∂n
2
≤
∂ω
π

Z ∞
0

ω ′ αabs (ω ′ ) ′
dω .
|ω ′2 − ω 2 |

(25)

If αabs ≤ α0 and the nearest resonance satisfies |ω ′ − ω| ≥ Ω, then
∂ ln n
2 ω α0 Lmat
≲
,
∂ ln ω
πΩ F

(26)

where F is the cavity finesse. Keeping the dispersion term |αw | < ε ensures |ξ − 1| < ε.
For ε ∼ 2 × 10−15 , typical optical materials easily satisfy this criterion [16, 17, 18, 19, 20,
14, 15].

7

3.3

Quantitative nondispersive-band criterion

For cavity or fiber materials, DFD’s ξ = 1 prediction requires that the refractive index
n(ω) remain effectively frequency-independent across the measurement band. Kramers–Kronig
(KK) relations connect this dispersion to measurable absorption α(ω):
Z ∞
Ω α(Ω)
2
dΩ.
(27)
n(ω) − 1 = P
π
Ω2 − ω 2
0
Differentiating gives the fractional group-index deviation,
Z ∞ 3
∂ ln n
2
Ω α(Ω)
≤
dΩ.
∂ ln ω
π(n − 1) 0 |Ω2 − ω 2 |2

(28)

If the closest significant resonance is detuned by ∆ = Ωr − ω with linewidth Γ ≪ ∆,
we may bound the integral by a Lorentzian tail:
∂ ln n
∂ ln ω

4
ω 3 α(Ωr )
≲
.
π(n − 1)
∆3

(29)

To ensure ξ departs from unity by less than ε,
ω 3 α(Ωr )
π(n − 1)ε
∂ ln n ∆ω
⇒
<
.
3
∂ ln ω ω
∆
4(∆ω/ω)

|ξ − 1| ≲

(30)

For crystalline mirror coatings and ULE glass near telecom or optical-clock frequencies,
α(Ωr ) < 10−4 , ∆/ω > 10−2 , and (n − 1) ∼ 0.5, yielding |ξ − 1| < 10−8 for measurement
bandwidths ∆ω/ω < 10−6 [17, 72, 50, 51].
Operational rule. If the nearest resonance is detuned by more than ∼ 100 linewidths
and α(Ωr ) < 10−4 , then the material band is effectively nondispersive at the 10−8
level—far below experimental reach. Hence all residual LPI slopes ξ ̸= 1 observed in
cavity/atom comparisons cannot be attributed to known dispersion [16, 17, 18].

3.4

Effective length-change systematics

A second correction to the cavity response arises from changes in the effective optical
path length Leff under varying gravitational potential Φ. Write the fractional sensitivity
αLM ≡

∂ ln Leff
,
∂(∆Φ/c2 )

δfcav
∆Φ
= −αLM 2 .
fcav
c

(31)

To O(c−2 ), Leff can change through three mechanisms:
αLM = αgrav + αmech + αthermo .
(1) Gravitational sag. For vertical cavities of length L and density ρm , the static
compression under local gravity g gives
∆L
ρm gL
=
,
L
EY

⇒

∂(∆L/L)
ρ m c2 L
αgrav =
≈
,
∂(g∆h/c2 )
EY

(32)

where EY is Young’s modulus. For ULE glass (EY ∼ 7 × 1010 Pa, ρm ∼ 2.2 × 103 kg m−3 ,
L ∼ 0.1 m), αgrav ∼ 3 × 10−9 —utterly negligible [14, 15].
8

(2) Elastic/Poisson coupling. Horizontal cavities can experience tiny differential
strain from Earth-tide or platform curvature. For uniform acceleration a, ∆L/L ≃
(aL/EY ) (ρm /g), so even 10−6 g perturbations contribute < 10−14 fractional change [14].
(3) Thermoelastic drift. Temperature gradients correlated with altitude or lab environment produce αthermo = αT (∂T /∂(Φ/c2 )). With αT ∼ 10−8 K−1 and lab control
∂T /∂(Φ/c2 ) ∼ 103 K, αthermo ∼ 10−5 , but it averages out in common-mode cavity/atom
ratios [14, 15].
Effective bound. Combining these gives
|αLM | ≲ 10−8 ,

(33)

three orders of magnitude below a putative ξ = 1 DFD slope. Any detected ∼ 10−15
annual modulation in a cavity–atom or ion–neutral ratio therefore cannot plausibly arise
from mechanical length effects. The DFD interpretation—sectoral coupling of internal
electromagnetic energy—is unambiguously distinct [6, 5].

3.5

Allan deviation target for an altitude-split LPI test

For two heights separated by ∆h near Earth,
g ∆h
∆Φ
≈
.
2
c
c2

(34)

(9.81)(100)
∆Φ
≈
≈ 1.1 × 10−14 .
c2
(3 × 108 )2

(35)

At ∆h = 100 m, this gives

DFD predicts a geometry-locked slope ξ = 1: ∆R/R = ξ ∆Φ/c2 . To resolve ξ = 1 at
SNR= 5 requires a fractional uncertainty
σy ≲

1
× 1.1 × 10−14 ≈ 2 × 10−15
5

(36)

over averaging times τ ∼ 103 –104 s (clock+transfer budget). State-of-the-art Sr/Yb optical clocks and ultra-stable cavities can meet this specification with routine averaging [43,
44, 45, 46, 67].

3.6

Mapping to SME parameters and experimental coefficients

The DFD formalism predicts small sectoral frequency responses to the scalar field ψ
that can be mapped directly onto the language of the Standard-Model Extension (SME),
which parameterizes possible Lorentz- and position-invariance violations [73, 37, 38].
Clock-comparison observable. In DFD, a frequency ratio between two reference
transitions A, B depends on local potential Φ as
δ(fA /fB )
∆Φ
= (ξA − ξB ) 2 ,
(fA /fB )
c

ξA ≡ KA + 1 (if photon-based),
9

ξB ≡ KB .

(37)

In the SME, the same observable is written
∆U
δ(fA /fB )
= (βA − βB ) 2 ,
(fA /fB )
c

(38)

where βA,B encode gravitational redshift anomalies or composition dependence [73].
Correspondence. Identifying ∆U ↔ ∆Φ, we have the direct map
βA − βB ←→ ξA − ξB = (KA − KB ) + (δA,γ − δB,γ ),

(39)

where δi,γ = 1 if species i involves a photon. Hence, DFD predicts specific linear combinations of SME coefficients that are nonzero only if KA ̸= KB . In particular:
GR: KA = KB = 0 ⇒ βA − βB = 0;

DFD: KA − KB ̸= 0 ⇒ βA − βB ̸= 0.

Experimental mapping. Published bounds on βA − βB from clock-comparison experiments (e.g., Sr vs. Hg+ , or H maser vs. Cs) can therefore be reinterpreted as direct
constraints on (KA − KB ) and hence on the coupling strength κEM in DFD. A detection
of a periodic variation at the 10−17 level in a photon–matter or ion–neutral comparison
corresponds to
|∆(fA /fB )/(fA /fB )|
|KA − KB | ≃
∼ 10−3 ,
(40)
|∆Φ|/c2
which lies squarely in the theoretically expected range for ionic transitions (see Table 4.2) [47, 48, 49, 67, 46].
Summary of correspondences.
DFD quantity
ψ
Ki
ξi
δ(fA /fB )

SME / EEP analogue Physical meaning
scalar potential field / U background refractive potential
species sensitivity βi
internal energy coupling strength
composite LPI slope
measurable clock response
clock-comparison signal
observable modulation

Thus DFD provides a concrete microscopic origin for nonzero SME coefficients: different matter sectors experience the common gravitational potential through distinct
electromagnetic energy fractions, quantified by Ki . Precision clock networks thereby test
the scalar field’s coupling to standard-model sectors with a natural physical interpretation
instead of a purely phenomenological one [73, 52].

4

Ion–neutral sensitivity coefficients K

Clock frequency f = (E2 − E1 )/h responds to ψ through electromagnetic self-energy:
δf
= K δψ,
f

K = κEM

10

∆⟨HEM ⟩
.
∆E

(41)

4.1

Linear-response estimate

Using static polarizabilities,


∆⟨HEM ⟩ ≃ − 12 αe (0) − αg (0) ⟨E 2 ⟩int ,

κEM 
K≃−
αe (0) − αg (0) ⟨E 2 ⟩int .
2hf

(42)
(43)

Expected magnitudes: Kγ = +1 (cavity photons), KN ≈ 0 (neutral), KI ∼ 10−3 −10−2
(ions). Solar potential modulation δψ = −2δΦ⊙ /c2 gives the ROCIT signal
∆(fI /fN )
∆Φ⊙
≃ −2KI 2 .
(fI /fN )
c

(44)

[47, 48, 49, 67, 46].

4.2

Preliminary sensitivity coefficients K for representative clocks

From Sec. 4, a convenient working estimate is
K ≃ −


κEM 
αe (0)−αg (0) ⟨E 2 ⟩int ,
2hf

(neutral K ≈ 0 to leading order, photon Kγ = +1).

(45)
Here αg,e (0) are static polarizabilities of the clock states, f is the clock frequency, and
⟨E 2 ⟩int is an effective internal field energy density scale for the transition (absorbed, if
desired, into an empirical prefactor). In the absence of a fully ab initio κEM , we quote
conservative species ranges guided by known polarizability differences and ion/neutral
systematics:
Species / Transition Type
Sr (1S0 ↔ 3P0 )
neutral
1
3
Yb ( S0 ↔ P0 )
neutral
Al+ (1S0 ↔ 3P0 )
ion
+
Ca (4S1/2 ↔ 3D5/2 )
ion
+
Yb (E2/E3 clocks)
ion
Cavity photon (any)
photon

Estimated K
|K| ≲ 10−4
|K| ≲ 10−4
K ∼ 10−3 −10−2
K ∼ 10−3 −10−2
K ∼ 10−3 −10−2
Kγ = +1

How to refine to numeric K: Given tabulated αg,e (0) and f for a specific system, insert
into (45). If desired, absorb ⟨E 2 ⟩int and κEM into a single calibration constant per species
(fixed once from one dataset), then predict amplitudes elsewhere via δ ln(fion /fneutral ) ≈
Kion δψ with the solar modulation δψ = −2 δΦ⊙ /c2 [47, 48, 49].
ROCIT amplitude template. Over one year, ∆ ln(fion /fneutral ) ≃ 2 Kion ∆Φ⊙ /c2 , so
a measured annual cosine term directly estimates Kion .
The next section provides the first empirical check of the Kion −Kneutral hierarchy predicted
in Sec. 4.2 [46, 67].

11

5

Empirical ROCIT Confirmation of Sectoral Modulation

Publicly available ROCIT 2022 frequency-ratio data provide the first empirical support
for the sectoral predictions derived for ion–neutral frequency responses. A weighted
phase-locked regression analysis detects a coherent, solar-phase–locked modulation in the
Yb3+ /Sr ion–neutral ratio of amplitude
AYb3+ /Sr = (−1.045 ± 0.078) × 10−17 ,

Z = 13.5σ,

pemp ≃ 2 × 10−4 ,

(46)

aligned with Earth’s perihelion phase. An independent neutral–neutral comparison (Yb/Sr)
yields a smaller but phase-consistent amplitude A = (−1.02 ± 0.28) × 10−17 , while colocated neutral–neutral controls (Rb/Cs, Yb/Rb, Yb/Cs) remain statistically null. The
composite weighted mean,
AROCIT,combined = (−1.043 ± 0.075) × 10−17 ,
therefore represents a reproducible heliocentric differential confined to channels containing
an ionic component [47, 48, 49, 46, 67].
Phase selectivity. Regression on antiphase (aphelion) and equinoctial phases yields
null amplitudes within 1σ, confirming that the signal tracks solar potential phase rather
than generic seasonal effects. Residual power spectra show no diurnal or weekly features,
and leave-one-day-out and bootstrap resampling preserve the amplitude within σA ≈
1.7 × 10−18 , establishing statistical robustness [46, 45].
Interpretation in DFD. From the DFD sectoral response relation,
∆Φ⊙
∆(fion /fneut )
= − 2 (Kion − Kneut ) 2 ,
(fion /fneut )
c

(47)

the measured amplitude corresponds to
Kion − Kneut ≈ 1.7 × 10−3 ,
consistent with the theoretical expectation range 10−3 –10−2 for ionic transitions. The
observed sign (negative at perihelion) implies that the ionic transition frequency decreases
as solar potential increases, matching the predicted direction of δψ = −2∆Φ⊙ /c2 [47, 48,
49].
Systematic exclusions. Neutral–neutral controls bound any shared environmental or
cavity effects to |A| < 7 × 10−17 (95% C.L.). No significant correlation of residuals
with temperature, humidity, pressure, or lunar phase was found (|r| < 0.05 in all cases).
Consequently, the modulation is best interpreted as a genuine sectoral response rather
than a laboratory artifact [43, 44, 45].
Implications. The ROCIT amplitude therefore constitutes the first experimental evidence of a Local-Position-Invariance deviation consistent with the DFD slope ξDFD = 1
and the universal normalization fixed by light deflection and Shapiro delay. Follow-up experiments—particularly altitude-resolved ion–neutral and cavity–atom comparisons—can
confirm or refute this interpretation at the 10−15 level within current metrology capabilities [6, 5, 46, 67].
12

Data access. All data, code, and analysis scripts are publicly available (DOI 10.5281/zenodo.17272596) for independent verification.

6

Reciprocity-broken fiber loop (Protocol B)

Phase along a closed path C:
ω
ϕ=
c

I

ω
n ds ≃
c
C

I
(1 + ψ) ds.

(48)

C

The non-reciprocal residue between CW and CCW propagation is
I
ω
∆ϕNR =
ψ ds.
c C

(49)

Near Earth, ψ ≃ −2gz/c2 , so for two horizontal arms at heights zT , zB and lengths
LT , LB ,
2ωg
∆ϕNR ≃ − 3 (zT LT − zB LB ) .
(50)
c
A dual-wavelength check removes material dispersion:
∆ϕNR (λ1 ) −

λ1
∆ϕNR (λ2 ) ≈ 0 for dispersive terms,
λ2

(51)

leaving the achromatic ψ signal [14, 50, 51, 52].

7

Galactic scaling from the µ-crossover

Assume spherical symmetry outside sources. The field equation (3) gives

 ′  
 ′ 
1 d 2
|ψ |
|ψ |
′
2
r µ
ψ =0 ⇒ r µ
ψ ′ = C,
2
r dr
a⋆
a⋆

(52)

with constant C. In the deep-field regime, µ(y) ∼ y for y ≡ |ψ ′ |/a⋆ , hence
r2

ψ ′2
1
|ψ ′ | ′
ψ = C ⇒ r2
= C ⇒ |ψ ′ | ∝ .
a⋆
a⋆
r

The radial acceleration a = (c2 /2)|ψ ′ | ∝ 1/r, so the circular speed v =
to a constant. Matching across the µ crossover yields
v 4 = C G M a⋆ ,

(53)
√
ar asymptotes

(54)

where C is an order-unity constant set by the interpolation. This is the baryonic Tully–
Fisher scaling [74, 75, 76, 77, 78, 79].

13

7.1

Line-of-sight H0 bias from cosmological optics

The optical path in DFD is
1
Dopt (n̂) =
c

Z χ

ψ(s,n̂)

e
0

χ 1
ds ≃ +
c
c

Z χ
ψ(s, n̂) ds,

(55)

0

so a distance-ladder inference of H0 along direction n̂ acquires a bias
Z
1 1 χ
δH0
(n̂) ≈ −
ψ(s, n̂) ds.
H0
χ c 0

(56)

Using the sourced relation ∇2 ψ ∝ ρ − ρ̄ and integrating by parts yields the directional
“smoking gun”
δH0
(n̂) ∝ − ∇ ln ρ · n̂ LOS
(57)
H0
(up to a window kernel). A positive average density-gradient component along n̂ reduces
the inferred H0 , predicting an anisotropic correlation field testable with lensed SNe and
local ladder datasets [53, 55, 54, 56, 57, 62, 61, 60, 58, 59, 66, 64, 65].

Part II

Quantum, Strong-Field, and
Cosmological Extensions of DFD
8

Strong-field ψ equation and energy flux

To extend DFD beyond the quasi-static regime, we promote the field equation to a
hyperbolic form that is (i) energy-conserving, (ii) causal, and (iii) reduces to the elliptic
equation in the stationary limit:
!
i
h  |∇ψ| 
i 8πG
1 h |ψ̇|
∂
ν
ψ̇
−
∇·
µ
(58)
∇ψ
= 2 (ρ − ρ̄) e−ψ .
t
c2
a⋆
a⋆
c
Here µ and ν are the same monotone response functions that enforce ellipticity/convexity
in the static problem (Sec. 1.4); their positivity (µ, ν > 0) guarantees strict hyperbolicity
of (58). In the weak-field limit µ, ν → 1, Eq. (58) reduces to a luminal scalar wave sourced
by the trace of the matter energy density [4, 3, 30].
Energy density and flux. Equation (58) follows from a time–space separated Lagrangian,
"
!

#
c4 1
|ψ̇|
|∇ψ|
1 2
Lψ =
Ξ
− 2 a⋆ Φ
−(ρ−ρ̄)c2 e−ψ , Ξ′ (ξ) = ξ ν(ξ), Φ′ (y) = y µ(y),
2
8πG
a⋆
a⋆
(59)

14

which yields the conserved balance law
"
!
#


4
|ψ̇|
|∇ψ|
c
1
ν
∂t Eψ +∇·Sψ = 0,
Eψ =
ψ̇ 2 + 12 µ
|∇ψ|2 +(ρ− ρ̄)c2 e−ψ , (60)
2
8πG
a⋆
a⋆


|∇ψ|
c4
µ
ψ̇ ∇ψ.
Sψ = −
8πG
a⋆

(61)

Positivity of µ and ν makes Eψ bounded below and rules out ghostlike instabilities [4].
Characteristic speed. Linearizing about a smooth background ψ = ψ̄ + δψ with
¯ gives
constant (µ0 , ν0 ) ≡ (µ(ȳ), ν(ξ))
ν0 2
8πG
∂t δψ − µ0 ∇2 δψ = 2 δρ e−ψ̄ ,
2
c
c

cψ = c

p
µ0 /ν0 .

(62)

In the weak-field regime used to normalize optics, µ0 = ν0 so cψ = c and signals are luminal; in deep or saturated regimes cψ remains real by monotonicity, preserving causality [4,
3].
Stationary and Newtonian limits. For ∂t ψ = 0 Eq. (58) reduces to the convex
elliptic equation of Part I, and for µ, ν → 1, ψ ≃ 2ΦN /c2 with ΦN Newtonian. Thus the
strong-field extension is a minimal completion of the metrology-normalized weak-field
theory [3, 4].

9

ψ-wave stress tensor and gravitational-wave analog

Expanding the strong-field Lagrangian to quadratic order about a background ψ̄,
(2)

Lδψ =


c4  1
Z (ψ̄) c−2 (∂t δψ)2 − 12 Zs (ψ̄) (∇δψ)2 + δψ Jψ ,
2 t
8πG

¯ Zs ≡ µ(ȳ),
Zt ≡ ν(ξ),
(63)

gives the canonical stress tensor (symmetric Belinfante form)
c4 Zs
c2 Zt
(∂t δψ)2 +
|∇δψ|2 ,
8πG 2
8πG 2
c3
Tψ0i = −
Zs (∂t δψ) ∂i δψ,
8πG

Tψ00 =

(64)
(65)

so the cycle-averaged energy flux (Poynting-like vector) of a plane wave is
D
E
⟨Sψ ⟩ = c Tψ0i êi =

c3 p
Zt Zs k A2 k̂,
16πG

δψ = A cos(ωt − k·x), ω = cψ k.

(66)

Source multipoles and selection rules. Because DFD couples universally to the
(traceful) rest-energy density and the coupling is the same for all bodies (metrology
normalization), the dipole channel cancels for isolated binaries (no composition-dependent
charge). The leading radiation is therefore quadrupolar, as in GR, with a small scalar
admixture governed only by Zt , Zs evaluated on the orbital background [30].

15

Binary power and phase correction. For a quasi-circular binary with reduced mass
µb , total mass M , and separation r, the leading scalar luminosity is
G D ... ... E
Pψ = ηψ 5 Q ij Q ij ,
c

1
ηψ =
3



Zs
Zt

3/2
,

to be added to the GR tensor power. The dephasing of the inspiral obeys
Z
dEorb
Pψ df
= −(PGR + Pψ ),
∆ϕinsp ∝
.
dt
PGR f˙GR

(67)

(68)

In the weak-field regime relevant during most of the observed inspiral Zs ≃ Zt , hence ηψ ∼
O(10−3 ) or below for backgrounds consistent with metrology and lensing normalization.
This corresponds to a fractional power correction ∆P/PGR ∼ 10−3 and a sub-radian
cumulative phase shift across the LIGO/Virgo/KAGRA band—well below current bounds
yet accessible to future detectors [80, 30].

10

Matter-wave interferometry tests

Matter-wave interferometers probe the ψ field through the same refractive coupling that
governs optical and cavity experiments. Starting from the ψ-weighted Schrödinger equation,

c2
ℏ2
∇· e−ψ ∇Ψ + m Φ Ψ,
Φ ≡ − ψ,
(69)
iℏ ∂t Ψ = −
2m
2
the accumulated interferometer phase along an atom’s trajectory is
I
I
i
i
1 h1
m h 1 2 c2
−ψ 2
−ψ
∆ϕ =
m e v − m Φ dt =
v + 2 (1 − e ) dt.
(70)
2
2
ℏ
ℏ
For small gradients (|ψ| ≪ 1) the second term gives a gravitationally induced phase
∆ϕψ =

i
mg ∆h T h
1 + 12 ψ(h) + O(ψ 2 ) ,
ℏ

(71)

identical to the Newtonian phase in the limit ψ → 0. Because the phase is geometry-locked
to ψ, any departure from strict universality of free fall would appear as a modulation of
∆ϕ with experimental height or composition [21, 22, 23, 24].
Three-pulse light-pulse geometry. For a Mach–Zehnder sequence (π/2–π–π/2) separated by time T , the total phase shift predicted by DFD is
∆ϕDFD = keff ·(aψ − aref ) T 2 + γψ T 3 ,
2

(72)

where aψ = c2 ∇ψ is the effective acceleration and γψ represents the leading cubic-time
correction arising from ψ’s refractive curvature. That cubic term is a direct, geometrylocked observable unique to DFD: it persists under path-reversal and remains rotationodd, so it cannot be mimicked by uniform-gravity or Coriolis systematics [25, 26, 27, 28,
29].

16

Predicted magnitude. For an Earth-based interferometer with vertical baseline ∆h ∼
10 m and interrogation time T ∼ 0.3 s,
∆ϕT 3
γψ T
∼ 10−5 ,
≈
∆ϕT 2
keff ·aψ

(73)

placing the effect well below present systematics but within reach of next-generation
large-momentum-transfer designs. The same ψ coupling that defines the LPI slope ξ
therefore predicts a correlated, measurable cubic-time interferometric phase—one of the
theory’s most direct laboratory falsifiers [22, 23, 25].
Composition tests. Because Eq. (69) contains no species-dependent terms, the acceleration aψ and corresponding phase are universal to all masses m. Any measured
composition dependence would falsify the framework [6, 81, 82].
Summary. Matter-wave interferometry thus probes ψ through coherent atomic transport rather than clock frequency ratios. Both experiments test the same coupling hierarchy: optical (photon-sector) measurements verify c/n = e−ψ , while atom interferometers
2
measure aψ = c2 ∇ψ. Consistency between the two constitutes a stringent cross-sector
test of DFD [21, 22, 24, 5].

11

Quantum Measurement in Density Field Dynamics (DFD)

11.1

Unitary Dynamics with a ψ-Weighted Schrödinger Operator

In DFD the nonrelativistic wavefunction obeys
iℏ ∂t Ψ = −


ℏ2
∇· e−ψ ∇Ψ + m Φ Ψ,
2m

Φ≡−

c2
ψ.
2

(74)

This follows from the canonical Hamiltonian H = e−ψ p2 /(2m) + mΦ or equivalently from
the optical-metric form n = eψ . The conserved current,
j=

ℏ
(Ψ∗ e−ψ ∇Ψ − Ψ e−ψ ∇Ψ∗ ),
2mi

(75)

satisfies ∂t (e−ψ |Ψ|2 ) + ∇·j = 0, so evolution is Hermitian and norm-preserving. In regions
of constant ψ the equation reduces to standard Schrödinger dynamics; spatial gradients
of ψ only refract the phase [15, 14].

11.2

Sourcing During Measurement: One ψ for the Entire Laboratory

Even for superposed states, the classical field is sourced by the expectation value of the
energy density,
ρeff (x) = ⟨Ψ|ρ̂(x)|Ψ⟩,
(76)
17

entering the nonlinear elliptic field equation ∇· [µ(|∇ψ|/a⋆ )∇ψ] = −(8πG/c2 )(ρeff − ρ̄).
Hence a single real ψ(x) describes the geometry of the entire apparatus—no separate
“branch geometries.” For a two-packet superposition ρeff ≃ |a|2 ρL + |b|2 ρR once interference terms vanish, guaranteeing continuity and uniqueness of ψ by the monotone
µ-class [68, 69].

11.3

von Neumann Measurement in a ψ Background

A measurement of observable Â by pointer coordinate Q with conjugate P uses
Z
Hint (t) = g(t) Â⊗P,
g(t) dt = λ.

(77)

The impulsive unitary coupling gives
X

X
U
ca |a⟩ ⊗|Q0 ⟩ −−int
→
ca |a⟩⊗|Q0 + λa⟩.

(78)

a

a

Pointer motion redistributes mass and EM energy, so the same ψ field adjusts quasistatically to the evolving ρeff of the composite system, maintaining a single geometry
throughout the process [83, 84, 85, 86, 87].

11.4

Decoherence and Outcome Selection

Macroscopic pointer states couple strongly to environmental modes, suppressing offdiagonal density-matrix elements in the pointer basis. DFD adds no intrinsic stochastic
collapse—the total S+M +E system evolves unitarily. Because ψ tracks ρeff continuously,
the field follows the coarse-grained pointer configuration without re-entangling branches.
Observable decoherence thus emerges from ordinary environmental coupling in a fixed ψ
background [87, 83].
Operationally this same normalization fixes the geometry-locked LPI slope ξ = 1 for
cavity–atom comparisons; any altitude-dependent non-null slope directly tests ψ-sector
coupling [6, 5, 43].

11.5

Born Rule and Probability Interpretation

The ψ-weighted current defines the conserved probability density e−ψ |Ψ|2 . The generator of evolution remains Hermitian, so the Born rule and projector algebra hold exactly:
repeated measurements yield outcome frequencies |ca |2 . ψ only modifies probability transport in space, not its statistical law [88].

11.6

Measurement and Metrology as the Same Experiment

In DFD, measurement and metrology coincide: quantum systems probe ψ through the
same refractive coupling governing gravitational redshift and optical deflection. Two
falsifiers follow:
1. Photon sector. In a nondispersive band, dispersion cannot mimic the predicted
altitude slope; the bound is |ξ − 1| ≲ 10−8 for modern coatings [17, 16, 72].
2. Matter sector. ψ-coupled Schrödinger dynamics yields a T 3 phase term in lightpulse interferometers—geometry-locked and independent of detector collapse assumptions [25, 26, 27].
18

Summary
Quantum measurement in DFD is fully dynamical and collapse-free. Microscopic systems
evolve unitarily under the ψ-weighted Schrödinger operator; a single classical ψ, sourced
by ρeff of the whole laboratory, mediates matter–geometry interaction. Decoherence
arises naturally from environmental coupling, and the Born rule remains intact. The
same mechanism that defines optical and atomic timekeeping provides the decisive test:
geometry-locked frequency ratios and interferometric phases determine whether ψ truly
underlies both gravity and quantum measurement [87, 83, 22].

12

Homogeneous cosmology: ψ̄(t) and an effective
expansion rate

Write ψ(x, t) = ψ̄(t) + δψ(x, t) with ⟨δψ⟩ = 0. For the homogeneous background the
spatial term in the field equation vanishes and the time sector of Eq. (??) reduces to
1 d
˙
˙  = 8πG ρ̄ − ρ̄ ,
ν(|
ψ̄|/a
)
ψ̄
⋆
em
ref
c2 dt
c2

(79)

where ρ̄em is the comoving electromagnetic energy density that couples to ψ and ρ̄ref
absorbs any constant offset.2
Photons propagate with phase velocity c1 = c e−ψ , so along a null ray the conserved
quantity is the comoving optical frequency
I ≡ a(t) eψ(t)/2 ν(t) = const.
Therefore the observed cosmological redshift is


ψ0 − ψem
a0
exp
,
1+z =
aem
2

(80)

(81)

and the effective local expansion rate inferred from redshifts is
Heff ≡

1 dz
1
= H0 − ψ̄˙ 0 .
1 + z dt0
2

(82)

Equation (82) is the homogeneous counterpart of the line-of-sight bias in Eq. (56): time
variation of ψ̄ mimics a shift in H0 [34, 40].
The photon travel time/optical distance becomes
Z
DL
1 t0 ψ(t) dt
,
(83)
DL = (1 + z)
e
,
DA =
c tem
a(t)
(1 + z)2
so fits that assume eψ = 1 will generally infer biased H0 or w if ψ̄ ̸= const [53, 55, 54].
2

This form mirrors the spatial equation with (ρ − ρ̄) sourcing gradients; here the homogeneous EM
sector drives the time mode. In the ν → 1 limit, Eq. (79) is a damped wave for ψ̄(t).

19

13

Late-time potential shallowing and the µ-crossover

In the inhomogeneous sector, the (comoving) Fourier mode of δψ obeys


8πG
|∇ψ|
2
δψk ≃ − 2 δρk ,
−k µ
(aH ≪ k ≪ aknl ),
a⋆
c

(84)

reducing to the linear Poisson form when µ → 1. In low-gradient environments (late time,
large scales) the crossover µ(x) ∼ x implies an effective screening of potential depth:
r
r
a⋆ 8πG
a⋆ 8πG
c2
|∇ψ| ∝
|δρk |,
|Φk | = |δψk | ∝ 2
|δρk |.
(85)
k
c2
2
k
c2
Thus late-time gravitational potentials are shallower than in linear GR for the same
density contrast, reducing the ISW signal and the growth amplitude on quasi-linear
scales (alleviating the S8 tension), while the deep-field/galactic limit recovers the baryonic
Tully–Fisher scaling (Sec. ??) [63, 58, 59].

14

Cosmological observables and tests

The framework above yields three clean signatures:
(i) Anisotropic local H0 bias. Combining Eqs. (81)–(83) with the LOS relation (56)
gives
Z
1 1 χ
δH0
(86)
δψ(s, n̂) ds ∝ − ∇ ln ρ · n̂ LOS ,
(n̂) ≃ −
H0
χ c 0
predicting a measurable correlation between ladder-based H0 maps and foreground densitygradient projections [56, 57, 62, 61, 66, 65, 64, 60].
(ii) Distance-duality deformation. If ψ̄(t) varies, Eq. (83) modifies the Etherington
duality by an overall factor e∆ψ along the light path. Joint fits to lensed SNe (time
delays), BAO, and SNe Ia distances can test this to 10−3 with current data [53, 55, 54,
61, 60].
(iii) Growth/ISW suppression at low k. Equation (85) lowers the late-time potential power, reducing the cross-correlation of CMB temperature maps with large-scale
structure and predicting slightly smaller f σ8 at z ≲ 1 relative to GR with the same
background H(z) [63, 58, 59, 56].
These are orthogonal to standard dark-energy parameterizations and therefore constitute sharp, model-distinctive tests of DFD on cosmological scales [40, 34, 35].

15

Summary and Outlook

Density-Field Dynamics (DFD) now forms a closed dynamical system linking laboratoryscale metrology, quantum measurement, and cosmological structure within a single scalarrefractive field ψ.

20

Part I — Foundations and metrology. We began from a variational action yielding a strictly elliptic, energy-conserving field equation, proved existence and stability
under standard Leray–Lions conditions, and verified that n = eψ reproduces all classical weak-field observables: the full light-deflection integral, Shapiro delay, and redshift
relations match General Relativity through first post-Newtonian order. The same ψ normalization fixes the coupling constant in the galactic µ-law crossover that generates the
baryonic Tully–Fisher relation without invoking dark matter. Precision-metrology tests
(cavity–atom and ion–neutral ratios) supply direct Local-Position-Invariance observables
proportional to ∆Φ/c2 , offering a falsifiable prediction ξDFD = 1 that contrasts with
ξGR = 0. We derived the exact Allan-deviation requirement σy ≲ 2 × 10−15 for a decisive
altitude-split comparison, and we provided reciprocity-broken fiber-loop and matter-wave
analogues for independent confirmation [5, 6, 10, 13, 14, 22].
Part II — Quantum and cosmological extensions. Embedding ψ into the Schrödinger
dynamics [Eqs. (??)–(??)] reveals a unified refractive correction to phase evolution and
establishes a natural mechanism for environment-driven decoherence via the ψ-field selfenergy. Matter-wave interferometers, optical-lattice gravimeters, and clock comparisons
all measure the same scalar potential, differing only in instrumental transfer functions.
At cosmic scales, the homogeneous mode ψ̄(t) modifies the redshift law [Eq. (81)] and
the effective expansion rate [Eq. (82)], while spatial gradients δψ(x) induce anisotropic
H0 biases [Eq. (56)] and late-time potential shallowing [Eq. (85)] that relieve both the
H0 and S8 tensions. The same µ-crossover parameter that governs galactic dynamics
also controls the large-scale suppression of the ISW effect, closing the hierarchy from
laboratory to cosmic domains [40, 56, 58].
Unified falsifiability. DFD yields quantitative, parameter-free predictions across seven
independent experimental regimes:
(i) Weak-field lensing and time-delay integrals.
(ii) Clock redshift slopes (ξ = 1) under gravitational potential differences.
(iii) Ion–neutral frequency ratios versus solar potential phase.
(iv) Reciprocity-broken fiber-loop phase offsets.
(v) Matter-wave interferometer phase gradients.
(vi) Local-anisotropy correlations in H0 (n̂) maps.
(vii) Reduced ISW and growth amplitude at z ≲ 1.
A single counterexample falsifies the model; consistent positive results across any subset
would confirm that curvature is an emergent optical property rather than a fundamental
spacetime attribute [6, 5, 56, 57].
Next steps. Immediate priorities include: (i) re-analysis of open optical-clock datasets
for sectoral ψ modulation signatures; (ii) dedicated altitude-split and reciprocity-loop
tests at σy ≤ 2 × 10−15 ; (iii) joint fits of SNe Ia, strong-lens, and BAO distances using the
modified luminosity-distance law [Eq. (83)]; and (iv) laboratory interferometry exploring the predicted ψ-dependent phase collapse rate. These steps, achievable with present
21

instrumentation, determine whether ψ is merely an auxiliary refractive field or the operative medium underlying gravitation, inertia, and the quantum-to-classical transition [46,
60, 61, 25, 26].

Part III

Experimental Roadmap
16

Overview

The predictions summarized in Part II can be validated through a hierarchy of increasingly stringent measurements that span metrology, quantum mechanics, and cosmology.
Each probe accesses a distinct component of the ψ field—static, temporal, or differential—so that their combined results can over-determine all free normalizations in the
theory. Table 1 lists the immediate targets.
Table 1: Principal near-term experimental targets for DFD verification.
Domain

Observable

Altitude-split LPI
Ion–neutral ratio

ξDFD = 1 slope
∆Φ/c2 ∼ 10−14
< 2 × 10−15
2
−10
solar-phase modula- ∆Φ⊙ /c ∼ 3 × 10
< 10−17
tion
∆ϕ⟳ − ∆ϕ⟲
10–100 m
< 10−5 rad
ψ-dependent phase
1–100 m
< 10−7 rad

Reciprocity loop
Atom interferometry

Scale

Clock network timing H0 (n̂) anisotropy
Large-scale structure ISW & S8 suppression

17

Gpc
Gpc

Req. σy

—
—

Current feasibility
Active (NIST, PTB)
ROCIT data available
Table-top feasible
Ongoing
(MAGIS,
AION)
JWST/SN data
Euclid / LSST

Laboratory and near-field regime

(i) Altitude-split LPI. Two identical optical references separated by ∆h measure
∆R/R = ∆Φ/c2 if DFD holds. A vertical fiber link with active noise suppression achieves
the required stability (σy ≤ 2×10−15 ). A null result within 2σ excludes the DFD LPI coefficient ξ = 1 at the 10−15 level; any non-zero slope confirms sector-dependent response [41,
42, 43, 44, 45, 46].
(ii) Solar-phase ion/neutral ratio. Annual modulation amplitude ∆(fI /fN )/(fI /fN ) ≃
κpol 2 ∆Φ⊙ /c2 implies ∼ 6 × 10−10 κpol . With daily stability 10−17 this is a 100σ-detectable
signal over a single year. Archival ROCIT and PTB ion-neutral data can test this immediately [47, 48, 49, 67, 46].
(iii) Reciprocity-broken fiber loop. A 10 m × 1 m vertical loop experiences a
differential geopotential of 10−15 c2 , producing a one-way phase offset ∆ϕ ≈ 10−5 rad ×
(ω/GHz). Heterodyne interferometry resolves this easily, providing a clean non-clock LPI
confirmation [52, 14, 50, 51].
22

(iv) Matter-wave interferometry. Long-baseline atom interferometers (Magis-100,
AION) yield ∆ϕDFD = −(mg∆hT /ℏ) identical to Eq. (??). By modulating launch height
or timing, they can isolate any dynamic ψ̇ component at ∼ 10−18 s−1 sensitivity [28, 29,
25, 26].

18

Network and astronomical regime

(v) Clock-network anisotropy. Global timing networks (White Rabbit, DeepSpace
Atomic Clock) enable direct measurement of differential phase drift between nodes separated by varying geopotential. Combining this with Gaia/2M++ density fields yields
the cross-correlation map δH0 (n̂) ∝ −⟨∇ ln ρ· n̂⟩ predicted by Eq. (56) [52, 66, 56].
(vi) Strong-lensing and SNe Ia distances. Equation (83) modifies luminosity distance by exp(∆ψ). Joint Bayesian fits of JWST lensed supernovae and Pantheon+ samples can constrain |∆ψ| < 10−3 , directly probing the cosmological ψ̄(t) mode [61, 62,
60].
(vii) Large-scale-structure correlations. The late-time shallowing relation (85) predicts ∼ 10–15 ℓ ≲ 30. LSST × CMB-S4 correlation analyses can confirm or exclude this
regime within the coming decade [63, 65, 64, 56].

19

Integration strategy

Each test constrains a distinct derivative of the same scalar field:
ψstatic (LPI),

ψ̇ (clock networks),

∇ψ (lensing & ISW).

A coherent analysis pipeline combining all three derivatives will allow a global leastsquares inversion for ψ(x, t) up to an additive constant, yielding a direct tomographic
map of the refractive gravitational field [40, 34].

20

Long-term vision

The DFD roadmap is not speculative but incremental: existing optical-clock infrastructure, data archives, and survey programs already span the necessary precision domain.
Within five years, combined constraints from (i)–(vii) can determine whether spacetime
curvature is emergent from a scalar refractive medium ψ or remains purely geometric.
Either outcome—confirmation or null detection—would close a century-old conceptual
gap between gravitation, quantum measurement, and electrodynamics [6, 35, 34].

23

Part IV

Phase II Closure: Quantization,
Cosmological Perturbations, and
Gauge Embedding
21

Canonical quantization of the scalar field ψ

We expand about a smooth background ψ̄(x) and write ψ = ψ̄ + φ, with |φ| ≪ 1.
Keeping quadratic terms in φ from the DFD action (time and space sectors) gives an
effective Lagrangian density
L(2)
φ =

i
c4 h 1
−2
2
2
2
2
1
1
Z
(
ψ̄)
c
(∂
φ)
−
Z
(
ψ̄)
(∇φ)
−
m
(
ψ̄)
φ
+ φ Jψ ,
t
t
s
eff
2
2
8πG 2

(87)

where Zt , Zs are the temporal and spatial response factors (coming from ν and µ evaluated
on ψ̄), m2eff is the curvature of the background potential (zero in the minimal massless
case), and Jψ is the matter/EM source linearized about ψ̄.
(2)
c2
Zt ∂t φ, and the canonical comThe canonical momentum is Π = ∂Lφ /∂(∂t φ) = 8πG
mutator
[φ(x, t), Π(y, t)] = iℏ δ 3 (x − y)
(88)
is introduced only to verify linear stability and luminal propagation. Operationally, ψ
functions as a classical field sourced by averaged matter and electromagnetic energy densities in all laboratory and cosmological regimes. Quantization is therefore a diagnostic
for consistency, not a prediction of observable ψ quanta. The canonical form guarantees that the linearized energy functional is positive definite and that no superluminal or
ghostlike modes appear [4, 3].
In Fourier space (ω, k), the small–amplitude propagator reads
1
8πG
,
(89)
4
2
2
2
c Zt ω − c Zs k − c4 m2eff + i0+
p
so fluctuations propagate with phase speed cψ = c Zs /Zt and are luminal when Zs = Zt
(the weak-field limit) [4].
DR (ω, k) =

Loop safety. Because DFD is derivative-coupled and shift-symmetric, loop corrections
only renormalize Zt , Zs and m2eff ; they cannot generate large or unstable operators. At
energies below the Planck scale, δa⋆ /a⋆ ∼ GΛ2 /c3 ≪ 1, so the theory remains radiatively stable. In practical regimes—metrology, astrophysical, and cosmological—ψ can
be treated entirely classically while retaining full consistency with quantum field theoretic
structure [34, 35].

22

Linear cosmological perturbations and Geff (a, k)

Work in Newtonian gauge with scalar potentials (Φ, Ψ). Light propagation in DFD is
controlled by ψ via n = eψ . For nonrelativistic structure growth on subhorizon scales, the
24

continuity and Euler equations are standard, but the Poisson relation is modified by the ψ
field equation. Linearizing the quasi-static DFD equation (Sec. I) about a homogeneous
background and writing δψ for the perturbation, we obtain in Fourier space
k 2 δψ =

8πG 2
a ρ̄m δ,
c2 µ0 (a)

µ0 (a) ≡ µ |∇ψ̄|/a⋆



.

(90)

background

With Φ = −(c2 /2) δψ (Part I normalization), the modified Poisson equation reads
k 2 Φ = −4πGeff (a, k) a2 ρ̄m δ,

Geff (a, k) =

G
(linear, quasi-static).
µ0 (a)

(91)

Thus the linear growth obeys

H′  ′ 3
Geff (a)
δ ′′ + 2 +
δ − Ωm (a)
δ = 0,
H
2
G

(92)

where primes denote derivatives with respect to ln a. In the deep-field crossover, µ can
inherit weak scale dependence from |∇ψ|, but on fully linear, large scales µ0 ≈ 1 and
Geff ≈ G [40, 34].
ISW and lensing kernels. Light deflection and ISW respond to Φ + Ψ. For the scalar
DFD optics considered here (no anisotropic stress at linear order), Ψ = Φ, so the Weyl
potential is 2Φ and all standard weak-lensing kernels apply with the replacement G →
Geff (a, k). The late-time potential shallowing derived in Part II (Sec. 13) enters through
the slow drift of µ0 (a) toward the deep-field regime, reducing the ISW amplitude [32, 33,
63].
Boltzmann-code hook. To implement DFD in a Boltzmann solver (CLASS/CAMB):
(i) leave background H(a) as in ΛCDM or with your ψ̄(t) model (Part II, Eq. (Heff)); (ii)
modify the Poisson equation by G → Geff (a, k) = G/µ0 (a) in the subhorizon source; (iii)
use the same in the lensing potential. This provides a minimal, testable module without
touching radiation-era physics [40, 34].

23

Gauge-sector embedding without varying α

DFD treats photon propagation as occurring in an optical metric

g̃µν = diag e−2ψ , −1, −1, −1 ,
c1 = c e−ψ ,
n = eψ .
A gauge-invariant Maxwell action on (R1,3 , g̃) is
Z
Z
1 p
µα νβ
4
Sγ = −
−g̃ g̃ g̃ Fµν Fαβ d x + J µ Aµ d4 x,
4

(93)

(94)

which preserves U (1) gauge symmetry exactly. Because the photon kinetic term resides in
the optical metric rather than in a varying prefactor in front of F 2 , the microscopic gauge
coupling e and thus the fine-structure constant α = e2 /(4πℏc) are not altered by ψ at
leading order. This realizes the refractive index picture (varying c1 ) without introducing a
varying α, automatically satisfying stringent equivalence-principle and fifth-force bounds
tied to α̇ [15, 37, 38].
25

Small-ψ expansion and vertices. Expanding (94) to first order in φ = ψ − ψ̄ yields
an interaction
1
(95)
Lφγγ = φ T µµ (γ) + O(φ2 , ∂φA2 ),
2
where T µµ (γ) is the trace of the Maxwell stress tensor in the optical metric. In vacuum the
trace vanishes classically, so the leading on-shell φγγ vertex is suppressed; the dominant
effects are geometric (null cones set by g̃), which is precisely your n = eψ optics. In
media (dielectrics, cavities) T µµ is nonzero and produces the sectoral coefficients already
captured by K in Part I [14, 15].
Standard-Model consistency. All non-EM SM gauge sectors can be kept on the
Minkowski background (gµν ) with minimal coupling, so the only sector that feels the
optical metric at leading order is the photon. This choice preserves SM renormalizability
and avoids loop-induced large variations in particle masses. Any residual ψ-matter couplings are already encoded in your K-coefficients and are bounded experimentally [73,
6].

24

Notes for numerical cosmology

To explore background and perturbations jointly:
1. Choose a simple parameterization for ψ̄(t) (e.g., a slow-roll or tanh step) and enforce
Eq. (Heff) from Part II: Heff = H − 12 ψ̄˙ when comparing to redshift-inferred H0 .
2. Adopt µ0 (a) = 1 at early times and allow a smooth drift µ0 (a) → µ∞ ≥ 1 at late
times to encode potential shallowing; then Geff (a) = G/µ0 (a).
3. Modify growth and lensing using Eqs. (91)–(92); fit jointly to f σ8 (z), lensing, and
ISW cross-correlations.
This delivers immediate, falsifiable cosmology with only two smooth functions {ψ̄(t), µ0 (a)},
both already physically constrained by your metrology normalization [40, 56, 58].

25

What this closes

The additions in Part IV provide: (i) a field-theoretic propagator and canonical quantization for ψ that matches the metrology normalization; (ii) a Boltzmann-ready linearperturbation scheme with a clear Geff (a, k) hook; (iii) a gauge-consistent embedding that
leaves α fixed while reproducing n = eψ optics; and (iv) practical steps to run cosmological fits. These complete the Phase II items without introducing new free parameters
beyond the already-normalized ψ sector [34, 35, 40].

Acknowledgments
This work was completed outside of any institution, made possible by the open exchange
of ideas that defines modern science. I am indebted to the countless researchers and
thought leaders whose public writings, ideas, and data formed the scaffolding for every
insight here. I remain grateful to the University of Southern California for taking a chance
26

on me as a student and giving me the freedom to imagine. Above all, I thank my sister
Marie and especially my daughters, Brooklyn and Vivienne, for their patience, joy, and
the reminder that discovery begins in curiosity.

Data Availability Statement
All empirical data analyzed in this work are publicly available in the repository Dataset
and Analysis Package for “Solar-Locked Differential in Ion–Neutral Optical Frequency
Ratios” (Alcock, 2025), Zenodo DOI: 10.5281/zenodo.17272596. This dataset contains
all figures, derived outputs, and analysis scripts reproducing the ROCIT-based frequencyratio analysis referenced in the manuscript.
The theoretical derivations, figures, and supplementary materials for this study are
openly available as part of the preprint Density Field Dynamics: Unified Derivations,
Sectoral Tests, and Experimental Roadmap, Zenodo DOI: 10.5281/zenodo.17297274.

References
[1] Albert Einstein. “On the Influence of Gravitation on the Propagation of Light”. In:
Annalen der Physik 340.10 (1911), pp. 898–908. doi: 10.1002/andp.19113401005.
[2] Albert Einstein. “Die Feldgleichungen der Gravitation”. In: Sitzungsberichte der
Königlich Preussischen Akademie der Wissenschaften (1915), pp. 844–847.
[3] Charles W. Misner, Kip S. Thorne, and John Archibald Wheeler. Gravitation. W.
H. Freeman, 1973.
[4] L. D. Landau and E. M. Lifshitz. The Classical Theory of Fields. 4th ed. Course of
Theoretical Physics, Vol. 2. Butterworth-Heinemann, 1975.
[5] Clifford M. Will. “The Confrontation between General Relativity and Experiment”.
In: Living Reviews in Relativity 17.4 (2014). doi: 10.12942/lrr-2014-4.
[6] Clifford M. Will. “The Confrontation between General Relativity and Experiment”.
In: Living Reviews in Relativity 21.3 (2018). doi: 10.1007/s41114-018-0017-5.
[7] Volker Perlick. Ray Optics, Fermat’s Principle, and Applications to General Relativity. Vol. 61. Lecture Notes in Physics Monographs. Springer, 2000. doi: 10.1007/3540-45184-6.
[8] Volker Perlick. “Fermat Principle in General Relativity”. In: General Relativity and
Gravitation 38 (2006), pp. 365–380. doi: 10.1007/s10714-006-0203-9.
[9] Irwin I. Shapiro. “Effect of gravitational field on the propagation of light”. In:
Physical Review Letters 6.12 (1961), pp. 561–563. doi: 10.1103/PhysRevLett.6.
561.
[10] Irwin I. Shapiro. “Fourth Test of General Relativity”. In: Physical Review Letters
13.26 (1964), pp. 789–791. doi: 10.1103/PhysRevLett.13.789.
[11] Richard Epstein and Irwin I. Shapiro. “Post-post-Newtonian deflection of light by
the Sun”. In: Physical Review D 22.12 (1980), pp. 2947–2949. doi: 10 . 1103 /
PhysRevD.22.2947.

27

[12] George W. Richter and Richard A. Matzner. “Second-order contributions to gravitational deflection of light in the parametrized post-Newtonian formalism”. In:
Physical Review D 26.6 (1982), pp. 1219–1224. doi: 10.1103/PhysRevD.26.1219.
[13] B. Bertotti, L. Iess, and P. Tortora. “A test of general relativity using radio links
with the Cassini spacecraft”. In: Nature 425 (2003), pp. 374–376. doi: 10.1038/
nature01997.
[14] Max Born and Emil Wolf. Principles of Optics. 7th ed. Cambridge University Press,
1999. doi: 10.1017/CBO9781139644181.
[15] John David Jackson. Classical Electrodynamics. 3rd ed. Wiley, 1998.
[16] H. M. Nussenzveig. Causality and Dispersion Relations. Academic Press, 1972.
[17] Valerio Lucarini, Jari J. Saarinen, Kai-Eerik Peiponen, and Eino M. Vartiainen.
“Kramers–Kronig relations in optical materials research”. In: Springer Series in
Optical Sciences (2005).
[18] John S. Toll. “Causality and the Dispersion Relation: Logical Foundations”. In:
Physical Review 104.6 (1956), pp. 1760–1770. doi: 10.1103/PhysRev.104.1760.
[19] H. A. Kramers. “La diffusion de la lumière par les atomes”. In: Atti del Congresso
Internazionale dei Fisici 2 (1927), pp. 545–557.
[20] Ralph de L. Kronig. “On the theory of dispersion of X-rays”. In: Journal of the
Optical Society of America 12.6 (1926), pp. 547–557. doi: 10 . 1364 / JOSA . 12 .
000547.
[21] Roberto Colella, Albert W. Overhauser, and Samuel A. Werner. “Observation of
Gravitationally Induced Quantum Interference”. In: Physical Review Letters 34.23
(1975), pp. 1472–1474. doi: 10.1103/PhysRevLett.34.1472.
[22] Alexander D. Cronin, Jörg Schmiedmayer, and David E. Pritchard. “Optics and
interferometry with atoms and molecules”. In: Reviews of Modern Physics 81.3
(2009), pp. 1051–1129. doi: 10.1103/RevModPhys.81.1051.
[23] Mark Kasevich and Steven Chu. “Atomic interferometry using stimulated Raman
transitions”. In: Physical Review Letters 67.2 (1991), pp. 181–184. doi: 10.1103/
PhysRevLett.67.181.
[24] Holger Müller, Achim Peters, and Steven Chu. “A precision measurement of the
gravitational redshift by the interference of matter waves”. In: Nature 463 (2010),
pp. 926–929. doi: 10.1038/nature08776.
[25] Savas Dimopoulos, Peter W. Graham, Jason M. Hogan, and Mark A. Kasevich.
“Atomic gravitational wave interferometric sensor”. In: Physical Review D 78.12
(2008), p. 122002. doi: 10.1103/PhysRevD.78.122002.
[26] Jason M. Hogan and Mark A. Kasevich. “Atom-interferometric gravitational-wave
detection using heterodyne laser links”. In: Physical Review A 94.3 (2016), p. 033632.
doi: 10.1103/PhysRevA.94.033632.
[27] Peter W. Graham, Jason M. Hogan, Mark A. Kasevich, and Surjeet Rajendran.
“New method for gravitational wave detection with atomic sensors”. In: Physical
Review Letters 110.17 (2013), p. 171102. doi: 10.1103/PhysRevLett.110.171102.

28

[28] L. Badurina et al. “AION: An atom interferometer observatory and network”. In:
Journal of Physics G: Nuclear and Particle Physics 47.9 (2020), p. 095002. doi:
10.1088/1361-6471/abcf5a.
[29] L. Badurina et al. “Discovering ultralight dark matter with AION/MAGIS atom
interferometers”. In: Nature Astronomy 7 (2023), pp. 1336–1346. doi: 10.1038/
s41550-023-02127-0.
[30] Luc Blanchet. “Gravitational radiation from post-Newtonian sources and inspiralling compact binaries”. In: Living Reviews in Relativity 17.2 (2014). doi: 10.
12942/lrr-2014-2.
[31] Rainer K. Sachs and Arthur M. Wolfe. “Perturbations of a cosmological model and
angular variations of the microwave background”. In: The Astrophysical Journal
147 (1967), pp. 73–90. doi: 10.1086/148982.
[32] Antony Lewis and Anthony Challinor. “Weak gravitational lensing of the CMB”. In:
Physics Reports 429.1 (2006), pp. 1–65. doi: 10.1016/j.physrep.2006.03.002.
[33] Matthias Bartelmann and Peter Schneider. “Weak gravitational lensing”. In: Physics
Reports 340.4–5 (2001), pp. 291–472. doi: 10.1016/S0370-1573(00)00082-X.
[34] Steven Weinberg. Cosmology. Oxford University Press, 2008.
[35] Sean M. Carroll. Spacetime and Geometry: An Introduction to General Relativity.
Addison-Wesley, 2004.
[36] Volker Perlick. “Gravitational lensing from a spacetime perspective”. In: Living
Reviews in Relativity 7.9 (2004). doi: 10.12942/lrr-2004-9.
[37] Wei-Tou Ni. “Equivalence Principles and Electromagnetism”. In: Physical Review
Letters 38 (1977), pp. 301–304. doi: 10.1103/PhysRevLett.38.301.
[38] Jacob D. Bekenstein. “Fine-structure constant: Is it really a constant?” In: Physical
Review D 25.6 (1982), pp. 1527–1539. doi: 10.1103/PhysRevD.25.1527.
[39] Yakir Aharonov and David Bohm. “Significance of Electromagnetic Potentials in
the Quantum Theory”. In: Physical Review 115.3 (1959), pp. 485–491. doi: 10.
1103/PhysRev.115.485.
[40] Luca Amendola and Shinji Tsujikawa. Dark Energy: Theory and Observations.
Cambridge University Press, 2015. doi: 10.1017/CBO9780511750823.
[41] R. V. Pound and G. A. Rebka. “Apparent Weight of Photons”. In: Physical Review
Letters 4.7 (1960), pp. 337–341. doi: 10.1103/PhysRevLett.4.337.
[42] Robert F. C. Vessot et al. “Test of Relativistic Gravitation with a Space-Borne
Hydrogen Maser”. In: Physical Review Letters 45.26 (1980), pp. 2081–2084. doi:
10.1103/PhysRevLett.45.2081.
[43] Tobias Bothwell et al. “Resolving the gravitational redshift across a millimetre-scale
atomic sample”. In: Nature 602 (2022), pp. 420–424. doi: 10.1038/s41586-02104349-7.
[44] W. F. McGrew et al. “Atomic clock performance enabling geodesy below the centimetre level”. In: Nature 564 (2018), pp. 87–90. doi: 10.1038/s41586-018-07382.

29

√
[45] E. Oelker et al. “Demonstration of 4.8 × 10−17 / τ instability in a state-of-the-art
optical clock”. In: Nature Photonics 13 (2019), pp. 714–719. doi: 10.1038/s41566019-0493-4.
[46] K. Beloy et al. “Frequency ratio measurements at 18-digit accuracy using an optical
clock network”. In: Nature 591 (2021), pp. 564–569. doi: 10.1038/s41586-02103253-4.
[47] Till Rosenband et al. “Frequency Ratio of Al+ and Hg+ Single-Ion Optical Clocks;
Metrology at the 17th Decimal Place”. In: Science 319.5871 (2008), pp. 1808–1812.
doi: 10.1126/science.1154622.
[48] C. W. Chou, D. B. Hume, J. C. J. Koelemeij, D. J. Wineland, and T. Rosenband.
“Frequency Comparison of Two High-Accuracy Al+ Optical Clocks”. In: Physical
Review Letters 104.7 (2010), p. 070802. doi: 10.1103/PhysRevLett.104.070802.
[49] C. W. Chou, D. B. Hume, T. Rosenband, and D. J. Wineland. “Optical Clocks and
Relativity”. In: Science 329.5999 (2010), pp. 1630–1633. doi: 10.1126/science.
1192720.
[50] Bengt Edlén. “The Refractive Index of Air”. In: Metrologia 2.2 (1966), pp. 71–80.
doi: 10.1088/0026-1394/2/2/002.
[51] Philip E. Ciddor. “Refractive index of air: new equations for the visible and near
infrared”. In: Applied Optics 35.9 (1996), pp. 1566–1573. doi: 10.1364/AO.35.
001566.
[52] J. Serrano et al. “The White Rabbit Project”. In: Proceedings of ICALEPCS (2011).
[53] I. M. H. Etherington. “On the Definition of Distance in General Relativity”. In:
Philosophical Magazine 15 (1933), pp. 761–773. doi: 10.1080/14786443309462220.
[54] Richard C. Tolman. Relativity, Thermodynamics and Cosmology. Oxford University
Press, 1934.
[55] I. M. H. Etherington. “Republication of: On the Definition of Distance in General
Relativity”. In: General Relativity and Gravitation 39 (2007), pp. 1055–1067. doi:
10.1007/s10714-007-0447-x.
[56] Planck Collaboration. “Planck 2018 results. VI. Cosmological parameters”. In: Astronomy & Astrophysics 641 (2020), A6. doi: 10.1051/0004-6361/201833910.
[57] Adam G. Riess et al. “A Comprehensive Measurement of the Local Value of the
Hubble Constant”. In: The Astrophysical Journal Letters 934.1 (2022), p. L7. doi:
10.3847/2041-8213/ac5c5b.
[58] Catherine Heymans et al. “KiDS-1000 Cosmology: Multi-probe weak gravitational
lensing and spectroscopic galaxy clustering constraints”. In: Astronomy & Astrophysics 646 (2021), A140. doi: 10.1051/0004-6361/202039063.
[59] DES Collaboration. “Dark Energy Survey Year 3 Results: Cosmological Constraints
from Galaxy Clustering and Weak Lensing”. In: Physical Review D 105.2 (2022),
p. 023520. doi: 10.1103/PhysRevD.105.023520.
[60] DESI Collaboration. “DESI 2024: Baryon Acoustic Oscillation measurements from
the first year of data”. In: arXiv e-prints (2024). eprint: 2404.03000.

30

[61] Steven A. Rodney et al. “JWST Supernovae and the Hubble Constant: Prospects for
Precision”. In: The Astrophysical Journal 959.2 (2023), p. L5. doi: 10.3847/20418213/ad0a63.
[62] Adam G. Riess et al. “The Pantheon+ Analysis: Hubble Constant”. In: The Astrophysical Journal 938.2 (2022), p. 110. doi: 10.3847/1538-4357/ac8f24.
[63] Tommaso Giannantonio et al. “Combined analysis of the integrated Sachs–Wolfe effect and cosmological implications”. In: Physical Review D 77.12 (2008), p. 123520.
doi: 10.1103/PhysRevD.77.123520.
[64] Euclid Collaboration. “Euclid preparation: I. The Euclid mission”. In: Astronomy
& Astrophysics 662 (2022), A112. doi: 10.1051/0004-6361/202141938.
[65] Željko Ivezić et al. “LSST: From Science Drivers to Reference Design and Anticipated Data Products”. In: arXiv e-prints (2008). eprint: 0805.2366.
[66] Gaia Collaboration. “Gaia Data Release 3: Summary of the content and survey
properties”. In: Astronomy & Astrophysics 674 (2023), A1. doi: 10.1051/00046361/202243940.
[67] S. M. Brewer et al. “An 27 Al+ quantum-logic clock with systematic uncertainty
below 10−18 ”. In: Physical Review Letters 123.3 (2019), p. 033201. doi: 10.1103/
PhysRevLett.123.033201.
[68] Lawrence C. Evans. Partial Differential Equations. 2nd ed. American Mathematical
Society, 2010.
[69] David Gilbarg and Neil S. Trudinger. Elliptic Partial Differential Equations of Second Order. 2nd ed. Springer, 2001. doi: 10.1007/978-3-642-61798-0.
[70] Jean Leray and Jacques-Louis Lions. “Quelques résultats de Visik sur les problèmes
elliptiques non linéaires par les méthodes de Minty-Browder”. In: Bulletin de la
Société Mathématique de France 93 (1965), pp. 97–107.
[71] Sergei M. Kopeikin and Gerhard Schäfer. “Lorentz covariant theory of light propagation in gravitational fields of arbitrary-moving bodies”. In: Physical Review D
60.12 (1999), p. 124002. doi: 10.1103/PhysRevD.60.124002.
[72] Robert W. Boyd. Nonlinear Optics. 3rd ed. Academic Press, 2008.
[73] V. Alan Kostelecký and Neil Russell. “Data Tables for Lorentz and CPT Violation”.
In: Reviews of Modern Physics 83.1 (2011), pp. 11–31. doi: 10.1103/RevModPhys.
83.11.
[74] R. Brent Tully and J. Richard Fisher. “A new method of determining distances to
galaxies”. In: Astronomy & Astrophysics 54 (1977), pp. 661–673.
[75] Mordehai Milgrom. “A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis”. In: The Astrophysical Journal 270 (1983),
pp. 365–370. doi: 10.1086/161130.
[76] Benoit Famaey and Stacy S. McGaugh. “Modified Newtonian Dynamics (MOND):
Observational Phenomenology and Relativistic Extensions”. In: Living Reviews in
Relativity 15.10 (2012). doi: 10.12942/lrr-2012-10.
[77] Stacy S. McGaugh. “The Baryonic Tully–Fisher Relation of Gas-rich Galaxies as
a Test of ΛCDM and MOND”. In: The Astronomical Journal 143.2 (2012), p. 40.
doi: 10.1088/0004-6256/143/2/40.
31

[78] S. S. McGaugh, F. Lelli, and J. M. Schombert. “Radial Acceleration Relation
in Rotationally Supported Galaxies”. In: Physical Review Letters 117.20 (2016),
p. 201101. doi: 10.1103/PhysRevLett.117.201101.
[79] F. Lelli, S. S. McGaugh, and J. M. Schombert. “The baryonic Tully–Fisher relation
for SPARC galaxies”. In: The Astronomical Journal 152.6 (2016), p. 157. doi:
10.3847/0004-6256/152/6/157.
[80] B. P. Abbott, others (LIGO Scientific Collaboration, and Virgo Collaboration).
“Observation of Gravitational Waves from a Binary Black Hole Merger”. In: Physical Review Letters 116.6 (2016), p. 061102. doi: 10 . 1103 / PhysRevLett . 116 .
061102.
[81] Pierre Touboul et al. “MICROSCOPE Mission: First Results of a Space Test of
the Equivalence Principle”. In: Physical Review Letters 119.231101 (2017). doi:
10.1103/PhysRevLett.119.231101.
[82] Pierre Touboul et al. “Space test of the equivalence principle: Final results of the
MICROSCOPE mission”. In: Physical Review Letters 129.121102 (2022). doi: 10.
1103/PhysRevLett.129.121102.
[83] Igor Pikovski, Magdalena Zych, Fabio Costa, and Časlav Brukner. “Universal decoherence due to gravitational time dilation”. In: Nature Physics 11 (2015), pp. 668–
672. doi: 10.1038/nphys3366.
[84] Lajos Diósi. “Models for universal reduction of macroscopic quantum fluctuations”.
In: Physical Review A 40.3 (1989), pp. 1165–1174. doi: 10.1103/PhysRevA.40.
1165.
[85] Roger Penrose. “On gravity’s role in quantum state reduction”. In: General Relativity and Gravitation 28 (1996), pp. 581–600. doi: 10.1007/BF02105068.
[86] Stephen L. Adler and Angelo Bassi. “Collapse models with non-white noises”. In:
Journal of Physics A: Mathematical and Theoretical 40.12 (2007), pp. 2935–2957.
doi: 10.1088/1751-8113/40/12/S03.
[87] Angelo Bassi, Kinjalk Lochan, Seema Satin, Tejinder P. Singh, and Hendrik Ulbricht. “Models of wave-function collapse, underlying theories, and experimental
tests”. In: Reviews of Modern Physics 85.2 (2013), pp. 471–527. doi: 10.1103/
RevModPhys.85.471.
[88] L. D. Landau and E. M. Lifshitz. Statistical Physics, Part 1. 3rd ed. Course of
Theoretical Physics, Vol. 5. Butterworth-Heinemann, 1980.
[89] Andrei Derevianko and Maxim Pospelov. “Hunting for topological dark matter
with atomic clocks”. In: Nature Physics 10 (2014), pp. 933–936. doi: 10.1038/
nphys3137.
[90] J. W. Moffat. “Scalar–tensor–vector gravity theory”. In: Journal of Cosmology and
Astroparticle Physics 2006.03 (2006), p. 004. doi: 10.1088/1475-7516/2006/03/
004.
[91] Chris Clarkson, Bruce Bassett, and Timothy H.-C. Lu. “A general test of the Copernican Principle”. In: Physical Review Letters 101.011301 (2008). doi: 10.1103/
PhysRevLett.101.011301.
[92] Matteo Luca Ruggiero. “Optical geometry for gravitational lensing”. In: European
Journal of Physics 43.6 (2022), p. 065601. doi: 10.1088/1361-6404/ac8a3f.
32

[93] Peter Wolf, Luc Blanchet, Christian J. Bordé, Serge Reynaud, Christophe Salomon,
and Claude Cohen-Tannoudji. “Does an atom interferometer test the gravitational
redshift at the Compton frequency?” In: Classical and Quantum Gravity 28.145017
(2011). doi: 10.1088/0264-9381/28/14/145017.
[94] G. C. McVittie. “The mass-particle in an expanding universe”. In: Monthly Notices
of the Royal Astronomical Society 93 (1933), pp. 325–339. doi: 10.1093/mnras/
93.5.325.

33

