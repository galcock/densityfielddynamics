---
source_pdf: Density_Field_Dynamics_and_the_c_Field__A_Three_Dimensional__Time_Emergent_Dynamics_for_Gravity_and_Cosmology.pdf
title: "Density Field Dynamics and the c-Field:"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Density Field Dynamics and the c-Field:
A Three-Dimensional, Time-Emergent Dynamics for
Gravity and Cosmology
Gary Alcock
August 18, 2025
Abstract
We formulate a dynamical alternative to curved spacetime in which the universe
is fundamentally Euclidean R3 and time is emergent. A single scalar “c-field” ψ(x)
controls the one-way speed of light via c1 (x) = c e−ψ(x) , preserving the measured twoway light speed c. Matter and photons couple to the same ψ: massive test bodies
accelerate according to
a =

c2
∇ψ ≡ −∇Φ,
2

Φ≡−

c2
ψ,
2

while photons follow Fermat paths in the refractive index n(x) = eψ(x) . From a local,
isotropic action we derive a nonlinear Poisson equation for ψ,
i
h  |∇ψ| 

8πG
∇· µ
∇ψ = − 2 ρm − ρ̄m ,
a⋆
c
which fixes the weak-field normalization needed to reproduce exactly Einstein’s classical
tests (light deflection α = 4GM/(c2 b), gravitational redshift, Shapiro delay, and the
Mercury perihelion advance) [1, 2, 3]. In the low-gradient (galactic/void) regime, the
same equation yields |∇ψ| ∝ 1/r, implying v(r) → const (flat rotation curves) without
dark matter and a Tully–Fisher/RAR
scaling [4, 5, 6, 7]. On cosmic scales, line-of-sight
R
optical length Dopt = 1c eψ ds produces a foreground-dependent bias that explains
the Hubble tension and mimics cosmic acceleration without a cosmological constant
[8, 9, 10]. We present explicit derivations and conservation laws from the action, and
give falsifiable laboratory protocols (one-way-c metrology and atom interferometry) at
the 10−10 m s−2 scale [11, 12].

1

Principles and Definitions

(P1) Three-dimensional ontology. Physical space is Euclidean R3 . Time is not fundamental; durations are operationally defined via round-trip light and physical clocks.
(P2) One-way light as a field. The one-way light speed is dynamical:
c
c1 (x) = c e−ψ(x) ,
n(x) ≡
= eψ(x) .
(1)
c1
1

Two-way c is invariant by reciprocity along any fixed path (Sec. 10).
(P3) Unified coupling of matter and light. Matter accelerations and photon paths are
governed by the same ψ:
c2
c2
∇ψ ≡ −∇Φ,
Φ ≡ − ψ.
a =
2
2
R
R ψ
Photons extremize optical length n ds = e ds (Fermat) [2, 13].

2

(2)

Action and Field Equation (Dynamics and Conservation)

Locality and isotropy in R3 with a single universal matter coupling select the functional
"
#


Z
a2⋆
|∇ψ|2
c2
3
dx
F[ψ] =
(3)
W
+
ψ (ρm − ρ̄m ) ,
8πG
a2⋆
2
where ρm is the rest-mass density, ρ̄m its coarse-grained mean (to enforce large-scale homogeneity), a⋆ is a universal acceleration scale, and µ(·) ≡ W ′ (·) is a single crossover function.
Variation gives the nonlinear Poisson equation
 


|∇ψ|
8πG
∇· µ
(4)
∇ψ = − 2 (ρm − ρ̄m ).
a⋆
c
The weak-field normalization−8πG/c2 is fixed by the requirement that light bending match
Einstein (Appendix A). The field stress tensor
i
a2⋆ h
(ψ)
µ ∂i ψ ∂j ψ − 12 δij W
(5)
Tij =
4πG
(ψ)

(m)

ensures momentum conservation: ∂j (Tij + Tij ) = 0.
Regimes. Choose µ once with
µ(x) → 1 (x ≫ 1)

and

µ(x) ∼ x (x ≪ 1).

Then:
• High-gradient (solar/strong): µ → 1 ⇒ ∇2 ψ = −(8πG/c2 )(ρm − ρ̄m ).
• Low-gradient (galaxies/voids): µ(x) ∼ x ⇒ |∇ψ| ∝ 1/r (spherical), yielding v(r) →
const.

3

Weak-Field Limit and Newtonian Gravity

For a point mass M and µ → 1, solving (4) gives
2GM
c2
GM
,
⇒
a
=
∇ψ = − 2 r̂.
2
cr
2
r
Thus Newton’s inverse-square law is recovered exactly from (2)–(4), not assumed.
ψ(r) =

2

(6)

4

Light Propagation: Bending, Redshift, and Shapiro
Delay

With n = eψ ≃ 1 + ψ and ψ = 2GM/(c2 r):
Deflection. The small-angle eikonal integral (Appendix B):
Z ∞
Z ∞
4GM
α =
∇⊥ ln n dz =
∇⊥ ψ dz =
.
c2 b
−∞
−∞

(7)

Gravitational redshift. A frequency transfer between rA and rB gives
∆Φ
∆ν
= ψ(rA ) − ψ(rB ) = − 2 .
ν
c

(8)

the standard GR result [1].
Shapiro delay. The excess one-way time is
Z
Z
1
1
2GM 4rS rR
∆t1w =
(n − 1) ds ≃
ψ ds =
ln 2 ,
c
c
c3
b

(9)

giving the textbook two-way coefficient 4GM/c3 [3] (Appendix C).

5

Relativistic Orbits: Perihelion Advance

Test-particle dynamics follow the Lagrangian
L = 12 m eψ(r) (ṙ2 + r2 θ̇2 ) − m Φ(r),

ψ=−

2Φ
.
c2

(10)

Expanding to O(Φ/c2 ) and using Binet’s equation for u = 1/r yields
d2 u
GM
3GM 2
+u = 2
+
u + ··· ,
2
dθ
ℓ /m
c2
hence the anomalous advance
∆ϖ =

6πGM
,
a(1 − e2 )c2

identical to GR (Appendix D; see also [1]).

3

(11)

(12)

6

Galactic Dynamics: Flat Rotation Curves and Tully–
Fisher

In the deep-field regime (|∇ψ| ≪ a⋆ with µ(x) ∼ x), spherical symmetry gives a Gauss law
from (4):
4πG
r2 µ(|ψ ′ |/a⋆ ) ψ ′ = − 2 M (r).
(13)
c
⋆
M (r) and hence |ψ ′ | ∝ 1/r outside the mass.
With µ(x) = x one finds r2 |ψ ′ | ψ ′ = − 4πGa
c2
The circular speed
c2
2
2
r |ψ ′ | → vflat
,
(14)
v (r) = r |a| =
2
is constant. Eliminating ψ ′ gives an asymptotic scaling
4
vflat
≃ C GM a⋆ c2 ,

(15)

with C a number of order unity fixed by the chosen µ. This reproduces the observed Tully–
Fisher scaling and the tight radial-acceleration relation without dark halos [6, 4, 5, 7].

7

Cosmological Field Equation and Optical Cosmography

Equation (4) with the subtraction (ρm − ρ̄m ) supplies the cosmological closure. Homogeneity
demands ⟨∇ψ⟩ = 0 in the ensemble, but real sightlines traverse inhomogeneities:
1
Dopt (z, n̂) =
c

Z χ(z)
e
0

ψ(r)

χ(z)
1
ds ≃
+
c
c

Z χ(z)
ψ(r) ds.

(16)

0

Thus the observed Hubble law inherits a directional bias
Z
δH0 (n̂)
1 1 χ
≈ −
ψ(r) ds,
H0
χ c 0

(17)

predicting a correlation of local-ladder H0 with foreground large-scale structure [8]. These
biases have the right sign and coherence to account for the late/early-time H0 discrepancy
[9, 10].

8

Emergent Time and Quantum Coupling

Operational time is defined by round-trip procedures. Quantum phases couple directly to
optical length. The minimal nonrelativistic coupling consistent with (10) is
iℏ ∂t Ψ(r, t) = −


ℏ2
∇· e−ψ(r) ∇Ψ + m Φ(r) Ψ,
2m

4

(18)

so an interferometer with arms sampling different ψ acquires
Z

Z
Z
ω0
ω0
ψ
ψ
e ds −
e ds ≃
∆ϕ =
(ψ1 − ψ2 ) ds.
c
c
γ1
γ2

(19)

State-of-the-art atom interferometers and optical clocks can probe the predicted 10−10 m s−2 scale effects [11, 12].

9

One-Way-c Observables (Metrology Protocols)

Two-way c is invariant along a fixed path, but differences between distinct routes expose ψ:
Z
Z


Z
Z
1
1
ψ
ψ
∆T1w ≡
e ds −
ψ ds −
e ds ≃
ψ ds .
(20)
c γAB
c γAB
γBA
γBA
Asymmetric fiber links (two heights), Mach–Zehnder with vertical separation, and
triangular time transfer among three stations isolate the effect while path swapping
removes instrument bias.

10

Lorentz invariance, simultaneity, and experimental
constraints

Conventionality of one-way c. As emphasized by Reichenbach, Edwards, and others,
the one-way speed of light is not directly measurable without a simultaneity convention;
only two-way c is empirically fixed [14, 15, 16, 17]. DFD promotes the convention parameter
to a field ψ but constrains it dynamically via (4).
Two-way invariance and Michelson–Morley/Kennedy–Thorndike. For a fixed arm
γ used in both directions, the round-trip time is
Z
Z
Z
1
2
1
ψ
ψ
e ds +
e ds =
eψ ds,
(21)
T2w =
c γ
c γ rev
c γ
which is independent of the arm orientation under a rigid rotation of the apparatus if ψ is a
scalar function of the ambient mass distribution on the arm scale. Thus modern Michelson–
Morley tests (optical cavities/whispering galleries) remain null to current sensitivity [18, 19,
20]. Kennedy–Thorndike experiments (boost dependence) are likewise preserved because the
round-trip speed along a fixed arm is path-symmetric [21, 1].
Local Lorentz symmetry. Locally, light rays in the optical medium n = eψ follow null
geodesics of Gordon’s “optical metric” [13, 2]. Hence matter and light exhibit local Lorentz
symmetry with respect to that effective metric, explaining the excellent agreement of specialrelativistic kinematics and clock comparisons (Ives–Stilwell, time dilation, etc.) while allowing global one-way anisotropy tied to ψ.
5

GPS and time transfer. Global navigation timing enforces a synchronization convention equivalent to isotropic two-way c in the chosen Earth-centered inertial frame [22]. DFD
reproduces all round-trip observables by design; one-way anisotropy shows up only in routedependent comparisons (Sec. 7), which are not tested by standard GPS common-view protocols.
Summary. DFD is consistent with the tightest existing tests of Lorentz invariance and
light-speed isotropy because those tests are fundamentally two-way [1, 18, 19, 20]. What
is new (and falsifiable) is the prediction of nonreciprocal one-way delays between distinct
routes in the presence of ambient ∇ψ.

11

Discussion and Conclusion

A single scalar ψ controlling the one-way light speed unifies gravity and optics in R3 with
emergent time. From the action (3) we obtain a nonlinear Poisson law (4) whose weak-field
normalization reproduces all Einstein classic tests exactly, and whose deep-field limit yields
flat rotation curves and a Tully–Fisher/RAR scaling without dark matter. Cosmologically,
line-of-sight optical length produces a foreground-dependent H0 bias (resolving the Hubble
tension) and an acceleration scale ∼ 10−10 m s−2 without a cosmological constant. The
framework is falsifiable now via precision metrology and atom interferometry. It replaces
four-dimensional curvature with a dynamical one-way c, closes conservation by construction,
and removes the GR–QM clash by eliminating fundamental time.

A

Weak-Field Normalization and the Factor of Two

In the weak-field regime take µ → 1, so ∇2 ψ = −(8πG/c2 )ρm . For a point mass, ψ =
2GM/(c2 r) (up to a constant). Photons see n = eψ ≃ 1 + ψ = 1 + 2GM/(c2 r). The eikonal
bending formula requires ψ = −2Φ/c2 with ∇2 Φ = 4πGρm to obtain α = 4GM/(c2 b). This
fixes the unique −8πG/c2 normalization in (4); any other choice fails the Einstein factor.

B

Light Deflection (Full Integral)

With ψ = 2GM/(c2 r) and r =

√

b2 + z 2 ,

∂ψ
2GM
b
= − 2
.
∂b
c
(b2 + z 2 )3/2
Thus

Z ∞
α =

∂ψ
2GM b
dz =
c2
−∞ ∂b

Z ∞

dz

−∞

(b2 + z 2 )3/2

6

=

2GM b 2
4GM
.
· 2 =
2
c
b
c2 b

C

Shapiro Delay (One-Way and Two-Way)
1
∆t1w =
c

Z

1
(n − 1) ds ≃
c

Z

2GM
ψ ds =
c3

Z

dz
2GM z +
√
=
ln
2
2
c3
b +z

√

b2 + z 2
b

+L

.
−L

2
ln 4L
; the round-trip doubles the coefficient to 4GM/c3 as in GR.
For L ≫ b, ∆t1w ≃ 2GM
c3
b2

D

Perihelion Advance (Derivation)

With L = 21 meψ (ṙ2 + r2 θ̇2 ) − mΦ and ψ = −2Φ/c2 , the conserved angular momentum is
ℓ = meψ r2 θ̇. Eliminating θ̇ and expanding eψ = 1 − 2Φ/c2 + · · · , the radial Euler–Lagrange
equation yields to first post-Newtonian order
ℓ2
2Φ ℓ2
′
r̈ − 2 3 = −Φ + 2 2 3 .
mr
c mr
Writing u = 1/r and using (d/dt) = θ̇(d/dθ) = (ℓ/mr2 )(d/dθ) gives
d2 u
GM
3GM 2
+u= 2
+
u,
2
dθ
ℓ /m
c2
hence ∆ϖ = 6πGM/[a(1 − e2 )c2 ].

E

Optical Cosmography and H0 Bias

Let χ be the comoving
R Euclidean distance inferred in absence of ψ. The actual optical
1 χ ψ
distance is Dopt = c 0 e ds. For statistically homogeneous ψ, ⟨ψ⟩ = 0, so ⟨Dopt ⟩ = χ/c.
Fluctuations along a given line yield
Z
Z
1 χ
δH0
11 χ
δDopt
δDopt ≃
ψ ds,
=−
ψ ds,
≃−
c 0
H0
χ/c
χc 0
predicting directional anisotropy correlated with foreground large-scale structure.

F

One-Way-c Metrology (Protocols)

Asymmetric fiber: deploy two parallel fibers at heights h1 ̸= h2 between stations A
and B. Measure
TAB and
R
R TBA with active path swapping; the nonreciprocal difference is
−1
∆T1w = c ( γAB ψ ds − γBA ψ ds).
R
Mach–Zehnder: vertical arm separation ∆h imprints ∆ϕ = (ω0 /c) ∆(eψ ) ds.
Triangular time transfer:H stations A,B,C; two loops (A→B→C→A and A→C→B→A).
The loop difference isolates ψ ds geometry while each edge preserves two-way c.

7

References
[1] Clifford M. Will. The confrontation between general relativity and experiment. Living
Reviews in Relativity, 17(4), 2014.
[2] Volker Perlick. Ray Optics, Fermat’s Principle, and Applications to General Relativity.
Springer, 2000.
[3] Irwin I. Shapiro. Fourth test of general relativity. Physical Review Letters, 13:789–791,
1964.
[4] Mordehai Milgrom. A modification of the newtonian dynamics as a possible alternative
to the hidden mass hypothesis. Astrophysical Journal, 270:365–370, 1983.
[5] Jacob Bekenstein and Mordehai Milgrom. Does the missing mass problem signal the
breakdown of newtonian gravity? Astrophysical Journal, 286:7–14, 1984.
[6] R. Brent Tully and J. Richard Fisher. A new method of determining distances to
galaxies. Astronomy and Astrophysics, 54:661–673, 1977.
[7] Stacy S. McGaugh, Federico Lelli, and James M. Schombert. The radial acceleration
relation in rotationally supported galaxies. Physical Review Letters, 117:201101, 2016.
[8] Licia Verde, Tommaso Treu, and Adam G. Riess. Tensions between the early and the
late universe. Nature Astronomy, 3:891–895, 2019.
[9] Planck Collaboration. Planck 2018 results. vi. cosmological parameters. Astronomy &
Astrophysics, 641:A6, 2020.
[10] Adam G. Riess, Wenlong Yuan, Lucas M. Macri, and et al. A comprehensive measurement of the local value of the hubble constant with 1 km s−1 mpc−1 uncertainty from
the hubble space telescope and the sh0es team. Astrophysical Journal Letters, 934:L7,
2022.
[11] Achim Peters, Keng-Yeow Chung, and Steven Chu. Measurement of gravitational acceleration by dropping atoms. Nature, 400:849–852, 1999.
[12] C. W. Chou, D. B. Hume, T. Rosenband, and D. J. Wineland. Optical clocks and
relativity. Science, 329:1630–1633, 2010.
[13] Walter Gordon. Zur lichtfortpflanzung nach der relativitätstheorie. Annalen der Physik,
377(22):421–456, 1923.
[14] Hans Reichenbach. Philosophy of Space and Time. Dover (English translation), 1958.
Originally 1928.
[15] William F. Edwards. Special relativity in anisotropic space. American Journal of
Physics, 31:482–489, 1963.

8

[16] R. Anderson, I. Vetharaniam, and G. E. Stedman. Conventionality of simultaneity,
gauge dependence and test theories of relativity. Physics Reports, 295(3–4):93–180,
1998.
[17] David Malament. Causal theories of time and the conventionality of simultaneity. Noûs,
11(3):293–300, 1977.
[18] Holger Müller, Sven Herrmann, Christian Braxmaier, Stephan Schiller, and Achim Peters. Modern michelson–morley experiment using cryogenic optical resonators. Physical
Review Letters, 91:020401, 2003.
[19] Ch. Eisele, A. Yu. Nevsky, and S. Schiller. Laboratory test of the isotropy of light
propagation at the 10−17 level. Physical Review Letters, 103:090401, 2009.
[20] Sven Herrmann, Alexander Senger, Holger Müller, and et al. Rotating optical cavity
experiment testing lorentz invariance at the 10−17 level. Physical Review D, 80:105011,
2009.
[21] Roy J. Kennedy and Edward M. Thorndike. Experimental establishment of the relativity
of time. Physical Review, 42:400–418, 1932.
[22] Neil Ashby. Relativity in the global positioning system. Living Reviews in Relativity,
6(1), 2003.

9

