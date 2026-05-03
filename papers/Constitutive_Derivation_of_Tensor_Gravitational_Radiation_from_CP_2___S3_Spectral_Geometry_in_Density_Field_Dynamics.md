---
source_pdf: Constitutive_Derivation_of_Tensor_Gravitational_Radiation_from_CP_2___S3_Spectral_Geometry_in_Density_Field_Dynamics.pdf
title: "Constitutive Derivation of Tensor Gravitational Radiation"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Constitutive Derivation of Tensor Gravitational Radiation
from CP 2 × S 3 Spectral Geometry in Density Field Dynamics
Gary Alcock
Independent Researcher, Los Angeles, CA

April 1, 2026

Abstract
We derive the transverse-traceless (TT) gravitational wave sector of Density Field Dynamics (DFD) from the same CP 2 × S 3 internal manifold that produces the fine-structure
constant, fermion mass hierarchy, and MOND interpolation function. The scalar field ψ
(governing quasi-static gravity) and the tensor hTT
ij (governing gravitational radiation) are
shown to be the trace and TT components of a single parent strain tensor, which is itself
the zero mode of the metric perturbation on the internal manifold. A Lichnerowicz analysis
on CP 2 × S 3 proves that no unwanted massless tensor or vector modes arise from internal
deformations. One scalar modulus (the squashing mode controlling the ratio R1 /R2 ) survives as a Lichnerowicz zero mode; we prove it is determined by the joint constraints from
α and G, acquiring a Planck-scale mass from the curvature of the constraint surface. The
gravitational sector contains exactly 1 scalar + 2 tensor degrees of freedom, with no additional propagating modes. The generalized Tamm–Plebanski construction gives anisotropic
constitutive relations whose TT perturbation is the gravitational wave. Source coupling reproduces the quadrupole formula identically to GR. Sector decoupling is proven from O(3)
irreducibility. The two-sector structure of the Unified Review is thereby promoted from
introduced to derived from the same topology that produces α−1 = 137.

Contents
1 Introduction

3

2 Geometry of CP 2 × S 3
2.1 Component Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Volumes and Curvature Invariants . . . . . . . . . . . . . . . . . . . . . . . . . .

3
3
3

3 Zero-Mode Derivation of ψ and hTT
ij
3.1 Metric Perturbation and Harmonic Expansion . . . . . . . . . . . . . . . . . . . .
3.2 3 + 1 Irreducible Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4
4
4

4 Lichnerowicz Rigidity: Explicit Proofs
4.1 The Lichnerowicz Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Rigidity of S 3 : Explicit Eigenvalue Computation . . . . . . . . . . . . . . . . . .
4.3 Rigidity of CP 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4 Absence of Harmonic 1-Forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5 Classification of Internal TT 2-Tensors . . . . . . . . . . . . . . . . . . . . . . . .
4.6 The Squashing Mode: Explicit Computation . . . . . . . . . . . . . . . . . . . . .
4.7 Squashing Mode Stabilization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4
4
4
5
6
6
6
7

5 Complete Low-Energy Gravitational Spectrum

8

1

6 Effective Action

9

7 Constitutive Interpretation

9

8 Source Coupling and Quadrupole Formula

10

9 Sector Decoupling: Proof
9.1 Linear Order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2 Nonlinear Order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3 Consistency with v3.3 Section 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . .

10
10
10
10

10 Summary

10

2

1

Introduction

The gravitational wave sector has been an acknowledged architectural seam in DFD. The
Unified Review (v3.3, Section 5) states plainly: “the TT sector is not independently derived
from the scalar ψ-field dynamics alone.” Within the full CP 2 × S 3 spectral completion of DFD,
the TT sector is derived as the spin-2 irreducible component of the same zero-mode parent
tensor whose trace yields ψ.
Logical status of the spectral action. DFD is not a higher-dimensional gravity theory with
10D Einstein equations. The internal manifold K = CP 2 ×S 3 enters through the Chamseddine–
Connes spectral action [6]:
SB = Tr f (D2 /Λ2 ),
(1)
where D is the Dirac operator on the total spectral geometry M = R3,1 × K, Λ is a UV cutoff,
and f is a positive test function. The spectral action is not the Einstein–Hilbert action in 10D;
it is a functional of the Dirac spectrum. Its Seeley–DeWitt expansion produces the 4D Einstein–
Hilbert term, gauge kinetic terms, the Higgs potential, and the cosmological constant as the
a0 , a2 , a4 heat-kernel coefficients. The DFD postulates P1 (n = eψ ) and P2 (a = (c2 /2)∇ψ) are
the weak-field limit of the gravitational sector produced by a4 .
This framing resolves the apparent tension between “DFD is not 10D gravity” and “we
use the spectral action on M”: the spectral action is a trace over the Dirac spectrum, not a
variational principle for a 10D metric. The internal geometry is part of the spectral data, not a
dynamical spacetime.

2

Geometry of CP 2 × S 3

2.1

Component Manifolds

The internal manifold K = CP 2 × S 3 has metric
K
gAB
dY A dY B = R12 ĝab dy a dy b + R22 ǧαβ dz α dz β ,

(2)

where ĝ is the unit Fubini–Study metric on CP 2 and ǧ is the unit round metric on S 3 .
CP 2 data. dim = 4, isometry group SU(3). Ricci tensor R̂ab = 6ĝab , scalar curvature R̂ = 24.
Einstein manifold with Λ̂ = 6. Betti numbers: (b0 , b1 , b2 , b3 , b4 ) = (1, 0, 1, 0, 1).
S 3 data. dim = 3, isometry group SO(4) ∼
= SU(2)L ×SU(2)R . Ricci tensor Řαβ = 2ǧαβ , scalar
curvature Ř = 6. Einstein manifold with Λ̌ = 2. Betti numbers: (b0 , b1 , b2 , b3 ) = (1, 0, 0, 1).

2.2

Volumes and Curvature Invariants

At radii R1 , R2 :
2

Vol(CP 2 ) = π2 R14 , Vol(S 3 ) = 2π 2 R23 , Vol(K) = π 4 R14 R23 .
24
6
144
12
RK = 2 + 2 , |RicK |2 = 4 + 4 .
R1 R2
R1
R2

3

(3)
(4)

3

Zero-Mode Derivation of ψ and hTT
ij

3.1

Metric Perturbation and Harmonic Expansion

A perturbation Hµν (x, Y ) of the external metric on M is expanded in scalar harmonics YI (Y )
on K:
X
Hµν (x, Y ) =
h(I)
∆K YI = −m2I YI .
(5)
µν (x) YI (Y ),
I

The zero mode (I = 0, Y0 = const, m20 = 0) gives a massless symmetric 2-tensor hµν (x) on
R3,1 . Higher KK modes (I ≥ 1) have masses mI ≥ 1/RK ∼ MP and decouple from low-energy
physics. Tensor and vector harmonics of K contribute to the massive KK tower through the
mixed components HµA , not through Hµν .

3.2

3 + 1 Irreducible Decomposition

Under the R3 × Rt split, hµν decomposes into O(3) irreducible representations:
hij =

1
h δij
|3 {z }

spin-0: 1 DOF

+

hTT
ij
|{z}

spin-2: 2 DOF

+ ∂(i Vj) + (∂i ∂j − 13 δij ∇2 )σ .
|
{z
}

(6)

gauge/constrained

Core Result: Parent Tensor Decomposition
The scalar ψ (trace of hµν |I=0 ) and the tensor hTT
ij (TT part of hµν |I=0 ) are the two
propagating irreducible components of the same zero-mode tensor on K = CP 2 × S 3 .
Both are massless because they share the eigenvalue m20 = 0. The two-sector structure
is the O(3) irreducible decomposition of a single parent object.

4

Lichnerowicz Rigidity: Explicit Proofs

We must verify that K produces no additional unwanted massless fields. The dangerous modes
are zero modes of the Lichnerowicz Laplacian ∆L on symmetric TT 2-tensors on K.

4.1

The Lichnerowicz Operator

Definition 4.1. For a Riemannian manifold (M, g), the Lichnerowicz Laplacian acting on
symmetric 2-tensors is:
(∆L h)ab ≡ −∇c ∇c hab − 2Racbd hcd + Rac hc b + Rbc hc a .

(7)

On an Einstein manifold (Rab = Λgab ), for TT tensors (∇a hab = 0, g ab hab = 0):
∆L hab = (−∇2 + 2Λ)hab − 2Racbd hcd .

4.2

(8)

Rigidity of S 3 : Explicit Eigenvalue Computation

Theorem 4.2. On S n with unit round metric (Rαβ = (n − 1)gαβ , constant sectional curvature
K = 1), the Lichnerowicz Laplacian (Def. 4.1) on symmetric TT 2-tensors has eigenvalues
λℓ = ℓ(ℓ + n − 1) + 2(n − 1),

ℓ ≥ 2.

In particular, λmin = λ2 = 4n > 0 for all n ≥ 2. For S 3 : λmin = 12.

4

(9)

Proof. We verify each term in ∆L explicitly on S n with unit radius and Rαβ = (n − 1)gαβ ,
sectional curvature K = 1.
Step 1: Curvature of S n . The Riemann tensor of a space of constant curvature K = 1:
Rαγβδ = gαβ gγδ − gαδ gγβ .

(10)

Step 2: Curvature contractions with a TT tensor. For hαβ with hγ γ = 0 and ∇α hαβ = 0:
−2Rαγβδ hγδ = −2(gαβ hγ γ −hαβ ) = 2hαβ ,
|{z}

(11)

=0

γ

γ

Rαγ h β + Rβγ h α = 2(n − 1)hαβ .

(12)

Step 3: Full Lichnerowicz operator. Substituting into (7):

∆L hαβ = −∇2 + 2n hαβ ,

(13)

where −∇2 ≡ −g γδ ∇γ ∇δ is the rough Laplacian (positive-definite convention).
Step 4: Rough Laplacian spectrum on TT tensors. By Higuchi [4] (Eq. (3.15)) and Rubin–
Ordóñez [5], the eigenvalues of −∇2 acting on symmetric TT 2-tensor harmonics on S n at
angular momentum level ℓ ≥ 2 are:
(TT)

µℓ

= ℓ(ℓ + n − 1) − 2.

(14)

Step 5: Combine. The Lichnerowicz eigenvalues are:
(TT)

λℓ = µℓ

+ 2n = ℓ(ℓ + n − 1) − 2 + 2n,

ℓ ≥ 2.

(15)

For S 3 (n = 3), the minimum is at ℓ = 2:
λ2 = 2 · 4 − 2 + 6 = 12 > 0.

□

(16)

Remark 4.3. Convention cross-check. The result λ2 = 12 can be verified independently.
On the unit 3-sphere, the Weitzenböck identity for symmetric 2-tensors reads ∆L = −∇2 +
(curvature endomorphism). The curvature endomorphism on a constant-curvature space contributes +2n = +6 for TT tensors (from Steps 2–3 above). The rough Laplacian eigenvalue at
ℓ = 2 is µ2 = 2 · 4 − 2 = 6 (Higuchi [4]). Total: λ2 = 6 + 6 = 12 > 0. The strict positivity (not
the specific value) is what matters for the rigidity conclusion.

4.3

Rigidity of CP 2

Theorem 4.4 (Koiso [1], Besse [2] Thm. 12.84). CP 2 with the Fubini–Study metric is infinitesimally rigid: ∆L has no zero modes on symmetric TT 2-tensors.
Proof. CP 2 = SU(3)/U(2) is a compact irreducible symmetric space of rank 1. By Koiso’s
theorem [1]:
A compact irreducible Riemannian symmetric space G/H admits no infinitesimal Einstein
deformations (i.e., ∆L has no TT zero modes) if and only if G/H is not isometric to a round
sphere S n with n ≥ 5.
CP 2 is not a sphere, so it is rigid.
The explicit spectral gap can be computed via representation theory of SU(3). TT symmetric
2-tensors on CP n = SU(n + 1)/U(n) decompose into Hermitian (type (1, 1)) and non-Hermitian
(type (2, 0) + (0, 2)) components under the complex structure. By the Weitzenböck formula on
the Kähler manifold CP n with Ric = 2(n + 1)g (Berger–Ebin [3], Besse [2] §12.J):
5

(1,1)

• Primitive (1, 1) TT tensors: λmin = 4n.
(2,0)
• (2, 0) + (0, 2) TT tensors: λmin = 8(n + 1).
For CP 2 (n = 2, Ric = 6g): λmin = min(8, 24) = 8 > 0.
Remark 4.5. The value λmin = 8 is for unit CP 2 with Ric = 6g. At radius R1 : λmin = 8/R12 .
The specific numerical value of the gap is not needed for the derivation; only its strict positivity
matters.

4.4

Absence of Harmonic 1-Forms

Lemma 4.6. b1 (CP 2 ) = b1 (S 3 ) = 0, hence b1 (K) = 0.
Proof. By the Künneth formula: b1 (K) = b1 (CP 2 )b0 (S 3 ) + b0 (CP 2 )b1 (S 3 ) = 0 · 1 + 1 · 0 = 0.
This eliminates all mixed zero modes of type ξa (y) ⊗ ζα (z) ∈ Ω1 (CP 2 ) ⊗ Ω1 (S 3 ): there are
no harmonic 1-forms on either factor to tensor together.

4.5

Classification of Internal TT 2-Tensors

Theorem 4.7 (Mode Classification). Symmetric TT 2-tensors on K = CP 2 × S 3 decompose
into four classes. The Lichnerowicz zero-mode content of each class is:
Class
(a)
(b)
(c)
(d)

4.6

Structure
TT(CP 2 ) ⊗ scalar(S 3 )
scalar(CP 2 ) ⊗ TT(S 3 )
Ω1 (CP 2 ) ⊗ Ω1 (S 3 )
ϕ1 ĝ ⊕ ϕ2 ǧ, traceless

∆L zero modes?
None
None
None
One

Reason
CP 2 rigid (Thm. 4.4)
S 3 rigid (Thm. 4.2)
b1 = 0 (Lem. 4.6)
Squashing mode

The Squashing Mode: Explicit Computation

Consider the constant TT deformation:
a b
α β
hAB = c1 R12 ĝab δA
δB + c2 R22 ǧαβ δA
δB ,

(17)

with 4c1 + 3c2 = 0 (tracelessness on 7D K).
Proposition 4.8. The mode (17) satisfies ∆L h = 0.
Proof. Since h is covariantly constant (∇C hAB = 0 because c1 , c2 are constants and ĝ, ǧ are
parallel): −∇C ∇C hAB = 0.
For the CP 2 block (A = a, B = b):
−2Racbd hcd = −2Racbd c1 ĝ cd = −2c1 R̂ab = −2c1 Λ̂ĝab ,
Rac hc b + Rbc hc a = 2Λ̂ c1 ĝab .

(18)
(19)

Total for CP 2 block: 0 − 2c1 Λ̂ĝab + 2c1 Λ̂ĝab = 0.
Identically for the S 3 block.
Physical interpretation. The squashing mode ϕ(x) is a scalar field on R3 that controls the
ratio R1 /R2 of the internal radii. It is not a tensor or vector; it does not affect the graviton
mode count (1 + 2 DOF). It is an internal geometry modulus.

6

4.7

Squashing Mode Stabilization

We now prove that the squashing modulus is determined (not free) within the DFD framework,
with its value uniquely fixed at the Einstein product condition and its mass rigorously Planckscale.
Theorem 4.9 (Squashing Modulus Determination). Define τ ≡ R2 /R1 . Then:
(i) The joint α–G constraints from the spectral action reduce to a single equation Φ(τ ) = Φ0
for a known constant Φ0 .
√
(ii) The function Φ(τ ) has a unique minimum at τ∗ = 1/ 3.
(iii) This minimum corresponds to the Einstein product condition [9]: 6/R12 = 2/R22 (equal
Einstein constants on both factors).
(iv) The DFD master invariant GℏH02 /c5 = α57 is derived under this Einstein condition
(Ap√
pendix O of the Unified Review), enforcing Φ0 = Φmin and selecting τ∗ = 1/ 3 as the
unique solution.
(v) The mass of the squashing mode is m2ϕ = O(1)·Λ2 ∼ MP2 , with the dimensionless constraint
curvature Φ′′ /Φ = 2.94 confirming no parametric suppression.
Proof. Step 1: The two constraints. The spectral action’s a4 coefficient gives the gauge kinetic
term [6]:
α−1 = A Vol(K) = A π 4 R14 R23 ,
(20)
where A = (16π/(4π)7/2 ) · (Tr(Y 2 )/12) · Λ3 /π 4 absorbs all radii-independent factors. The
topological quantities (kmax = 60, Tr(Y 2 ) = 10, Toeplitz truncation 63/64) enter through A
and Λ3 and do not depend on (R1 , R2 ).
The Einstein–Hilbert term gives:
Z
G−1 = B RK dvolK = B π 4 (24 R12 R23 + 6 R14 R2 ),
(21)
K

where B = 16πf4 cEH /(12π 4 ) collects the remaining spectral action constants.
Step 2: Reduction to one equation in τ . With τ = R2 /R1 : α−1 = Aπ 4 R17 τ 3 and G−1 =
4
Bπ R15 (24τ 3 + 6τ ). Eliminating R1 via the first equation (R1 = [α−1 /(Aπ 4 τ 3 )]1/7 ):
G−1 = C Φ(τ ),

C ≡ Bπ 4 α−1 /(Aπ 4 )

5/7

,

(22)

where
Φ(τ ) ≡ 24 τ 6/7 + 6 τ −8/7 .

(23)

Step 3: Φ(τ ) has a unique minimum.
Φ′ (τ ) =

144 −1/7 48 −15/7 48 −15/7 2
τ
−
τ
=
τ
(3τ − 1).
7
7
7

(24)

Setting Φ′ (τ ) = 0: 3τ 2 = 1, hence
1
τ∗ = √ ≈ 0.5774.
3

(25)

Since Φ(τ ) → +∞ as τ → 0+ (from the τ −8/7 term) and as τ → +∞ (from the τ 6/7 term), and
Φ′ changes sign only at τ∗ , this is the unique global minimum.
√
Step 4: τ∗ is the Einstein product condition. At τ∗ = 1/ 3:
Λ̂
6/R12
1
=
= 3τ 2 = 3 × = 1.
2
3
2/R2
Λ̌
7

(26)

So τ∗ is exactly the condition for K to be an Einstein product manifold.
Step 5: The master invariant enforces τ = τ∗ . The DFD master invariant GℏH02 /c5 = α57
is derived (Appendix O) under the Einstein product condition Λ̂ = Λ̌, which requires τ = τ∗ .
Self-consistency demands Φ0 = Φmin , giving exactly one positive solution τ = τ∗ .
Step 6: Explicit mass computation.
i
48 h 15 −22/7 2
Φ′′ (τ ) =
− τ
(3τ − 1) + 6 τ −8/7 .
(27)
7
7
At τ∗ (where 3τ∗2 − 1 = 0):
Φ′′ (τ∗ ) =

288 −8/7 288 4/7
τ∗
=
3 ≈ 77.1.
7
7

(28)

The minimum value: Φmin = 24 · 3−3/7 + 6 · 34/7 ≈ 26.2. The dimensionless curvature:
77.1
Φ′′ (τ∗ )
≈
= 2.94.
Φ(τ∗ )
26.2

(29)

The squashing mode mass:
m2ϕ =

Φ′′ (τ∗ ) 1 2
·
Λ = O(1) · Λ2 ∼ MP2 ,
Φ(τ∗ ) Kτ

(30)

where Kτ is the kinetic-term normalization for the squashing mode, arising from the spectral
action evaluated on the τ -dependent metric. Since the squashing mode is a constant deformation
on K, Kτ is an O(1) geometric factor (the norm of the mode profile integrated over K). The
dimensionless constraint curvature Φ′′ /Φ ≈ 2.94 confirms no parametric suppression: the mass
is set by the spectral cutoff Λ ∼ MP with an O(1) coefficient that is not accidentally small.
Step 7: Decoupling. At E ≪ mϕ ∼ MP , the squashing mode is frozen, contributing no
propagating degree of freedom.
Squashing Modulus: Rigorous Treatment
1. The squashing mode IS a Lichnerowicz zero mode (Prop. 4.8). Acknowledged, not
hidden.
2. It is a scalar, not a tensor (ψ + hTT mode count unaffected).
√
3. The constraint function Φ(τ ) = 24τ 6/7 +6τ −8/7 has a unique minimum at τ∗ = 1/ 3
(Eqs. 24–25).
√
4. τ∗ = 1/ 3 is the Einstein product condition (Λ̂ = Λ̌), enforced by selfconsistency with the master invariant.
5. m2ϕ = O(1) · Λ2 ∼ MP2 ; the dimensionless curvature Φ′′ /Φ = 2.94 confirms no
parametric suppression (Eq. 30).
The squashing modulus is a genuine Lichnerowicz zero mode, honestly acknowledged, uniquely determined, and rigorously Planck-massive with no
parametric suppression.

5

Complete Low-Energy Gravitational Spectrum
Field
ψ (scalar)
hTT
ij (tensor)
(r)
Aµ (gauge)
ϕ (squashing)

Origin
Trace of hµν |I=0
TT of hµν |I=0
HµA via Killing vectors
Class (d) Lich. zero mode
8

DOF
1
2
8+3+1
1

Status
Massless
Massless
Massless
m ∼ MP

The gravitational sector at E ≪ MP contains exactly 1 scalar + 2 tensor = 3 DOF. The
squashing modulus is present but Planck-massive and non-propagating at accessible energies.
No additional scalar breathing mode, vector mode, or tensor polarization contaminates the
low-energy spectrum.

6

Effective Action

The a4 Seeley–DeWitt coefficient of the spectral action (1), integrated over K, produces the 4D
Einstein–Hilbert action [6]:
Z
√
c4
S4 =
d4 x −g4 R4 .
(31)
16πG
Linearizing g4,µν = ηµν + hµν and decomposing via (6):


Z
2
c4
3 1 (∂t ψ)
2
dt d x
Sscalar [ψ] =
− (∇ψ) ,
8πG
2
c2
"
#
TT )2
4 Z
(∂
h
c
t
ij
2
Stensor [hTT ] =
dt d3 x
− (∇hTT
.
ij )
32πG
c2

(32)
(33)

The relative coefficient 1/4 between scalar and tensor prefactors is fixed by the Einstein–
Hilbert structure, not chosen. The connection to the vacuum loading paper: K0 = c4 /(8πG)
is the vacuum stiffness for the compression (scalar) channel, while K0 /4 = c4 /(32πG) governs
the shear (tensor) channel.

7

Constitutive Interpretation

With the TT sector included, the optical metric generalizes to:
ds̃2 = −

c2 2
i
j
dt + (δij + hTT
ij ) dx dx ,
n2

n = eψ .

(34)

The Tamm–Plebanski construction gives tensor constitutive relations:
+κψ
(δ ij − hij,TT ),
εij
eff = ε0 n e

(35)

−κψ
(δ ij − hij,TT ),
µij
eff = µ0 n e

(36)

with κ = α/4 ≈ 1.82 × 10−3 , the constitutive E/B split parameter. At tree level (Gordon
optical metric [7]), κ = 0; the gauge-emergence auxiliary metric introduces a correction κ =
αeff = α/n22 = α/4, where n2 = 2 is the SU(2) frame stiffness from the (3, 2, 1) partition [10].
(Not to be confused with the self-coupling coefficient ka = 3/(8α) ≈ 51.4 of Appendix G, which
governs EM–ψ backreaction strength.) Three independent constitutive channels:
1. Isotropic compression (ψ): quasi-static gravity, MOND. Governed by nonlinear µ(x)
function.
2. E/B split (κψ): EM–ψ coupling.
3. Anisotropic shear (hTT
ij ): gravitational radiation. Linear response at all observed amplitudes.
Physical picture. The vacuum medium has compression stiffness K0 = c4 /(8πG) and shear
stiffness K0 /4. The compression response is nonlinear (governed by µ(x) = x/(1+x), producing
flat rotation curves). The shear response is linear (gravitational wave amplitudes h ∼ 10−21 are
deep in the linear regime). This is physically natural: most materials have different nonlinear
thresholds for compression and shear.
9

8

Source Coupling and Quadrupole Formula

R
Matter couples to the full metric: Smatter ⊃ −(1/2) hµν T µν . The TT projection gives:
16πG TT
Πij .
c4

(37)

2G ¨TT
I (tret ).
c4 r ij

(38)

□hTT
ij = −
Far-zone solution:
hTT
ij (t, x) =
Luminosity:

dE
G ... ...ij
= − 5 ⟨ I ij I ⟩.
dt
5c
Identical to GR. Hulse–Taylor binary: 0.2% agreement.

9

Sector Decoupling: Proof

9.1

Linear Order

(39)

For any isotropic quadratic action on R3 :
δij hTT
ij = 0 (tracelessness),

(40)

∂i hTT
ij = 0 (transversality).

(41)

All possible ψ-hTT cross-terms vanish identically.

9.2

Nonlinear Order

The µ(x) function is a scalar functional of |∇ψ| (spin-0). It cannot mix with spin-2 modes by
O(3) selection rules. In the block-diagonal completion: cT = c exactly, consistent with the
GW170817 multimessenger constraint [8].

9.3

Consistency with v3.3 Section 5

The O(3) irreducibility argument in Section 5 of the Unified Review is confirmed and strengthened: what was previously a structural observation (“the principal symbol is automatically
block-diagonal”) is now derived as a consequence of the zero-mode tensor decomposition on K.

10

Summary

2
3
1. ψ and hTT
ij are trace and TT parts of the same zero-mode tensor on K = CP × S (§3).
2
2. No unwanted tensor or vector zero modes from K: CP rigid (Thm. 4.4, gap = 8/R12 ),
S 3 rigid (Thm. 4.2, gap = 12/R22 ), b1 (K) = 0 (Lem. 4.6).
3. One scalar squashing modulus exists but is determined by α–G constraints and Planckmassive (Thm. 4.9).
4. Effective action gives both Sψ and ShTT with correct relative normalization (§6).
5. Tamm–Plebanski gives anisotropic constitutive relations; GWs are shear perturbations of
the vacuum medium (§7).
6. Quadrupole formula is identical to GR (§8).
7. Sector decoupling derived from O(3) irreducibility (§9).

10

Replacement for Unified Review Section 5 Opening
Old: “The TT sector is not independently derived from the scalar ψ-field dynamics
alone.”
New: “The TT sector is derived from the same CP 2 ×S 3 spectral geometry that produces
α−1 = 137.036. Both ψ and hTT
ij are irreducible components of the zero-mode parent
tensor on the internal manifold. The Lichnerowicz analysis proves no unwanted tensor
or vector modes arise; the single scalar modulus (squashing mode) is determined by the
α–G constraints and decouples at Planck mass.”

References
[1] N. Koiso, “Rigidity and stability of Einstein metrics—the case of compact symmetric
spaces,” Osaka J. Math. 17, 51–73 (1980).
[2] A. L. Besse, Einstein Manifolds (Springer, Berlin, 1987), Chap. 12, esp. Thm. 12.84.
[3] M. Berger and D. Ebin, “Some decompositions of the space of symmetric tensors on a
Riemannian manifold,” J. Diff. Geom. 3, 379–392 (1969).
[4] A. Higuchi, “Symmetric tensor spherical harmonics on the N -sphere and their application
to the de Sitter group SO(N, 1),” J. Math. Phys. 28, 1553 (1987).
[5] M. A. Rubin and C. R. Ordóñez, “Eigenvalues and degeneracies for n-dimensional tensor
spherical harmonics,” J. Math. Phys. 25, 2888 (1984).
[6] A. H. Chamseddine and A. Connes, “The Spectral Action Principle,” Commun. Math.
Phys. 186, 731 (1997).
[7] W. Gordon, “Zur Lichtfortpflanzung nach der Relativitätstheorie,” Ann. Phys. 72, 421
(1923).
[8] B. P. Abbott et al. (LIGO/Virgo), Phys. Rev. Lett. 119, 161101 (2017).
[9] G. W. Gibbons, S. A. Hartnoll, and C. N. Pope, “Bohm and Einstein–Sasaki metrics, black
holes, and cosmological event horizons,” Phys. Rev. D 67, 084024 (2003).
[10] G. Alcock, “The Physical Origin of the Refractive Field in Density Field Dynamics: Gravity as Electromagnetic Vacuum Loading,” Zenodo (2026), https://doi.org/10.5281/
zenodo.19200031.

11

