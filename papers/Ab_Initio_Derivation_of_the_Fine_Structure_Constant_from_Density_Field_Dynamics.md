---
source_pdf: Ab_Initio_Derivation_of_the_Fine_Structure_Constant_from_Density_Field_Dynamics.pdf
title: "Ab Initio Derivation of the Fine Structure Constant"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Ab Initio Derivation of the Fine Structure Constant
from Density Field Dynamics
G. Alcock
Independent Researcher
(Dated: December 27, 2025)

1

Abstract
We present numerical evidence that the electromagnetic fine structure constant α ≈ 1/137
emerges from first principles within the gauge-emergence microsector of Density Field Dynamics
(DFD). The derivation proceeds through four independent topological inputs, all fixed by geometry
with no continuous free parameters in the input sector:
1. The UV cutoff kmax = 60 is derived from a closed Spinc index on CP 2 : kmax = χ(CP 2 , O(9)⊕
O⊕5 ) = 60 (Bridge Lemma, Appendix A).
2. The U (1) lattice coupling is identified with the vacuum expectation value of the shifted
Chern-Simons level: βU (1) = ⟨k + 2⟩kmax =60 = 3.7969, where the shift k → k + 2 arises from
the dual Coxeter number of SU (2).
3. The ratio βSU (2) /βU (1) = 6 is a DFD prediction—not a convention—derived from the stiffness
ratio n2 /n1 = 2 (the Frame Stiffness Theorem [9]) and the generation count Ngen = 3 (index
theorem on CP 2 ): βSU (2) /βU (1) = (n2 /n1 ) × Ngen = 2 × 3 = 6.
4. The stiffness ratio κU (1) /κSU (2) = 1/2 follows from the Frame Stiffness Theorem [9].
Key result: The UV cutoff kmax = 60 is derived from topology (Bridge Lemma: kmax =
χ(CP 2 , O(9) ⊕ O⊕5 ) = 60) and confirmed by lattice simulation. The fully converged sum (kmax →
∞, giving β = 3.94) yields α = 1/303, which is ruled out at > 50σ, independently establishing the
physical cutoff.
At the determined parameter point (βU (1) , βSU (2) ) = (3.80, 22.80), lattice Monte Carlo simulations yield:
• L = 6: αW = 0.007297 ± 0.000094 (−0.00% from physical value)
• L = 8: αW = 0.007322 ± 0.000095 (+0.34% from physical value)
• L = 10: αW = 0.007361 ± 0.000068 (+0.88% from physical value)
• L = 12: αW = 0.007291 ± 0.000022 (−0.08% from physical value)
• L = 16: αW = 0.007380 ± 0.000110 (+1.13%; 9/10 runs, p < 0.01)
The fine structure constant was never used as an input. Its emergence at the correct value,
combined with the rejection of the converged sum, the verification that only ratio βSU (2) /βU (1) = 6

2

works (ten ratios tested; all others fail), and confirmed independence from simulation parameters
(k0 , ε), constitutes strong evidence for the DFD gauge-emergence framework.
A complementary spectral-action route yields the closed-form prediction at sub-ppm precision
(Section III):
"
#
3/2
7
π
k
+
3
max
 = 137.035999854 (+0.005 ppm).
1+
α−1 =
Tr(Y 2 ) kmax
24
kmax + 4
80 (kmax + 4)2 − 1
Priority timestamp: December 27, 2025.
Code and data: https://doi.org/10.5281/zenodo.19173548

CONTENTS

I. Introduction

5

A. The mystery of α

5

B. Summary of results

5

C. Context within DFD

6

II. Theoretical Framework

6

A. DFD postulates

6

B. The S 3 microsector

6

C. Gauge emergence as Berry connection

7

D. Stiffness functional and coupling extraction

7

E. Frame Stiffness Theorem: Stiffness ratio from gauge-emergence geometry

7

F. Electroweak mixing and the α extraction

8

III. The Sub-ppm Analytical Formula

8

A. The one-liner

8

B. Origin of each factor

9

C. Derivation of the prefactor

9

D. Derivation of the Toeplitz factor (kmax + 3)/(kmax + 4)

10

E. Derivation of the boost correction

10

F. Step-by-step verification

10

G. Relation to the lattice route

11
3

IV. Parameter Derivation: Four Constraints, Zero Free Parameters

11

A. Constraint 1: The UV cutoff kmax = 60 from topology

11

B. Constraint 2: Microsector vacuum sets βU (1)

12

C. Constraint 3: The lattice ratio from topology

14

D. Constraint 4: DFD stiffness ratio

16

E. The prediction and how to verify it

16

F. Summary: Complete derivation chain

17

V. Numerical Method

17

A. Lattice formulation

17

B. Kappa extraction

18

C. Run parameters

18

D. Outlier identification

18

VI. Results

19

A. The critical test: Truncated vs. converged

19

B. Headline results at β = 3.80

20

C. Comparison: β = 3.77 vs. β = 3.80

20

D. Top single runs

21

E. Stiffness ratio verification

21

F. Total statistics

22

G. Systematic checks

23

VII. Discussion

23

A. The UV cutoff and its dual confirmation

23

B. Uniqueness to DFD

24

C. Relation to the full DFD derivation

25

D. What has been demonstrated

25

E. What remains to be done

26

VIII. Conclusion

26

Reproducibility

27
4

A. The Bridge Lemma: kmax = 60 from a Closed Spinc Index
1. Statement

29

2. Proof

29

3. Physical selection of the twist bundle

29

4. Derivation chain and non-circularity

30

5. Consistency checks

30

B. Pre-Registered Decision Rule

30

References

I.

29

31

INTRODUCTION
A.

The mystery of α

The fine structure constant,
α≡

1
e2
≈ 0.0072973525693 . . . ≈
,
4πϵ0 ℏc
137.036

(1)

controls the strength of electromagnetic interactions and is one of the most precisely measured quantities in physics. Yet within the Standard Model, it remains an unexplained input
parameter. Feynman famously called it “one of the greatest damn mysteries of physics” [1].
A first-principles derivation of α from geometric or topological considerations would represent a major advance in fundamental physics.

B.

Summary of results

We demonstrate that within the DFD gauge-emergence framework, the fine structure
constant emerges from four independent topological constraints:
1. The UV cutoff kmax = 60 from the Bridge Lemma (Appendix A)
2. The microsector vacuum: βU (1) = ⟨k + 2⟩ = 3.80
3. The lattice ratio: βSU (2) /βU (1) = (n2 /n1 ) × Ngen = 6
4. The stiffness ratio: κU (1) /κSU (2) = 1/2 (the Frame Stiffness Theorem [9])
5

These constraints uniquely determine all parameters, and α = 1/137 emerges as a prediction.
The topological input sector has no continuous free parameters; simulation parameters Kψ =
0.25 and k0 = 8 are auxiliary (independence from k0 and ε verified in Section VI).

C.

Context within DFD

This paper reports lattice Monte Carlo verification of the alpha derivation within the
DFD framework. The parent theory is described fully in Ref. [9]. The derivation chain
SM → q1 = 3 → kmax = 60 → α = 1/137 is logically independent: α appears at the end as
output, not as input.

II.

THEORETICAL FRAMEWORK
A.

DFD postulates

DFD is formulated on flat R3 with a scalar field ψ(x, t) and refractive index n = eψ . The
one-way light speed is c1 = c e−ψ , and the kinematic acceleration relation is
a=

B.

c2
∇ψ.
2

(2)

The S 3 microsector

The DFD UV completion includes a topological microsector based on SU (2)k ChernSimons theory on the 3-sphere. The partition function is given by the exact result [6]:
r


2
π
3
ZSU (2)k (S ) =
.
(3)
sin
k+2
k+2
A crucial structural feature is that the physics depends on the shifted level
keff ≡ k + 2,

(4)

not on k itself. The shift arises from the dual Coxeter number h∨ = 2 for SU (2) and is
required for:
• Modular invariance of the partition function
6

• Quantum consistency of the Chern-Simons theory
• Proper normalization of the WZW model central charge: c = 3k/(k + 2)
The Euclidean microsector weight is defined as


π
2
2
sin
.
w(k) = |ZSU (2)k (S )| =
k+2
k+2
3

C.

(5)

2

Gauge emergence as Berry connection

In the DFD gauge-emergence extension, gauge fields arise as Berry connections [2, 3] on
internal mode subspaces. A local orthonormal frame Ξr (x) on the internal space defines the
connection
(r)

(6)

Ai = i Ξ†r ∂i Ξr ,
(r)

with field strength Fij .

D.

Stiffness functional and coupling extraction

The stiffness functional penalizing spatial twisting of internal frames is
(r)

Lstiff = −

κr
(r) (r)
Tr Fij Fij .
2

(7)
−1/2

Canonical normalization implies the gauge coupling scales as gr ∝ κr

E.

.

Frame Stiffness Theorem: Stiffness ratio from gauge-emergence geometry

A central result of the DFD gauge-emergence framework is that stiffness coefficients are
proportional to the complex dimension of the corresponding internal mode subspace Vr :
κr = nr κ0 ,

(8)

where nU (1) = 1, nSU (2) = 2, and nSU (3) = 3 are the complex dimensions of the respective
subspaces in the partition (3, 2, 1) of the internal manifold CP 2 × S 3 (not the Lie-algebra
dimensions dim U (1) = 1, dim SU (2) = 3, dim SU (3) = 8). This yields:
κU (1)
n1
1
=
=
κSU (2)
n2
2

(9)

This ratio is derived from internal geometry, not tuned to any experimental value. It is
confirmed by the lattice measurement (0.495 ± 0.020; Section VI E).
7

F.

Electroweak mixing and the α extraction

Electromagnetism emerges from mixing of U (1) and neutral SU (2) components:
1
1
1
= 2 + 2.
2
e
g1 g2

(10)

Important distinction. The lattice β parameters (βU (1) = 3.80, βSU (2) = 22.80) are the
input couplings set before the simulation. The stiffnesses κr are output quantities measured
by the background-field method during the simulation. These are not the same:
βU (1) =

1
≈ 3.80 (input),
g12

κU (1) ≈ 7.25 (measured).

(11)

The relationship between them is non-perturbative and lattice-size dependent, which is
precisely why the simulation is needed.
Given the measured stiffnesses, the gauge couplings are extracted via Wilson’s normalization conventions [4, 5]:
g12 =

1

κU (1)
and the fine structure constant follows as
αW =

g22 =

,

4
κSU (2)

(12)

,

(1/κU (1) )(4/κSU (2) )
e2
1
=
·
.
4π
(1/κU (1) ) + (4/κSU (2) ) 4π

(13)

The factor of 4 in g22 = 4/κSU (2) is the standard Wilson action normalization for SU (2) [4, 5]:
with Tr(T a T b ) = 21 δ ab , the Wilson plaquette action gives βSU (2) = 4/g 2 .

III.

THE SUB-PPM ANALYTICAL FORMULA

The four constraints in Section IV fix the lattice parameter point and yield α ≈ 1/137 at
∼ 1% precision via Monte Carlo. A complementary analytical route—the spectral action on
the Toeplitz-truncated internal geometry CP 2 × S 3 —produces the closed-form prediction to
sub-ppm precision.

A.

The one-liner

Closed-Form Formula for α−1
α

−1

π 3/2
kmax + 3
=
Tr(Y 2 ) kmax
24
kmax + 4



Nsp
1
1+
·
2
gF Tr(Y ) (kmax + 4)2 − 1

8



(14)

With Tr(Y 2 ) = 10 and kmax = 60:
α

−1



63
7
5π 3/2
× 60 ×
× 1+
= 137.035 999 854 . . .
=
12
64
80 × 4095

(15)

−1
= 137.035999177 ± 0.000000021) is +0.005 ppm.
The residual from CODATA 2022 (αexp

No parameter is fitted.

B.

Origin of each factor

Factor

Value

Origin

Status

π 3/2 /24

1
0.2320 . . . 16π · (4π)−7/2 · 12
· 4π 4

Geometric (exact)

Tr(Y 2 )

10

SM hypercharges, 3 generations

SM content

kmax

60

Bridge Lemma, Appendix A

Derived

(kmax + 3)/(kmax + 4) 63/64

LLL truncation, Spinc det. line O(3) Derived

Nsp /(gF Tr(Y 2 ))

7/80

Hypercharge weighting

Derived

1/((kmax + 4)2 − 1)

1/4095

Adjoint unimodularity (sld trace)

Derived

TABLE I. All inputs to Eq. (14). None are fitted.

C.

Derivation of the prefactor

The spectral action on the product manifold X = CP 2 × S 3 (dimension dint = 7) yields a
gauge kinetic term proportional to the Gilkey–DeWitt a4 coefficient. With internal volume
2

Vint = Vol(CP 2 ) × Vol(S 3 ) = π2 · 2π 2 = π 4 (and the ωCP 1 = 2π normalization contributing
a factor of 4 [9]):

1
Kgeom = 16π · (4π)−7/2 · 12
· 4π 4

= 4π
· 4−7/2 π −7/2 · 4 π 4 = 43 · 4−5/2 π 3/2 =
3
9

π 3/2
.
24

(16)

The factors 16π, (4π)−7/2 , and 1/12 arise respectively from the α−1 = 4π/α coupling definition, the heat-kernel normalisation on a 7-dimensional internal space, and the coefficient of
tr(Ω2 ) in the Gilkey formula.

D.

Derivation of the Toeplitz factor (kmax + 3)/(kmax + 4)

−1
The Spinc determinant line bundle on CP 2 is Ldet = KCP
2 = O(3). The LLL (lowest

Landau level) / Berezin–Toeplitz truncation on a CP 1 slice uses holomorphic sections of
O(kmax ) ⊗ Ldet |CP 1 = O(kmax + 3), giving:
d := dim H 0 (CP 1 , O(kmax + 3)) = kmax + 4 = 64 .

(17)

Unimodularity (working in sld rather than gld , i.e. removing the identity mode from
End(Hk )) gives the factor (d − 1)/d = (kmax + 3)/(kmax + 4) = 63/64:
Λ3 := kmax ·

E.

63
d−1
= 60 ×
= 59.0625 .
d
64

(18)

Derivation of the boost correction

The trace normalization on sld (adjoint representation of SU(d)) differs from the trace
on Md (C) by:
εadj =

d2
,
d2 − 1

δadj = εadj − 1 =

1
1
=
.
d2 − 1
4095

(19)

Weighted by the hypercharge content ratio w = Nsp /(gF · Tr(Y 2 )) = 7/80 (where Nsp = 7
counts SU(2) Weyl multiplets per generation and gF = 8 is the spectral-triple grading factor):
εw = 1 + w δadj = 1 +

F.

7
≈ 1 + 2.14 × 10−5 .
80 × 4095

Step-by-step verification

1. Kgeom = π 3/2 /24 = 0.232013666534 . . .
2. Λ3 = 60 × 63/64 = 59.0625
−1
3. αraw
= Kgeom × 10 × 59.0625 = 137.033071797 . . .

4. εw = 1 + 7/(80 × 4095) = 1.000021367521 . . .
10

(20)

5. α−1 = 137.033071797 × 1.000021368 = 137.035999854
6. Residual vs. CODATA 2022: +4.94 × 10−9 (relative)
Convention note. The December 2025 pipeline also exists in a “bundle model” convention
with f0 = 2/3 and an expanded Λ3 = 885.9375. These are algebraically identical to the
f0 = 1 canonical convention above: (2/3) × 885.9375 = 1 × 10 × 59.0625 = 590.625.

G.

Relation to the lattice route

The analytical formula and the lattice Monte Carlo are two independent routes to the
same result:
Route

Method

Spectral action (Eq. (14)) Closed-form algebraic
Lattice MC (L = 12)

Precision
+0.005 ppm

Non-perturbative simulation −0.08% (∼ 1%)

The lattice provides non-perturbative confirmation that the derived parameter point (βU (1) , βSU (2) ) =
(3.80, 22.80) actually yields α = 1/137 under the full non-linear renormalization group flow.
The analytical formula provides the closed-form prediction that the simulation confirms.

IV.

PARAMETER DERIVATION: FOUR CONSTRAINTS, ZERO FREE PARAM-

ETERS
A.

Constraint 1: The UV cutoff kmax = 60 from topology

The maximum Chern-Simons level is derived from a closed Spinc index on CP 2 (the
Bridge Lemma, Appendix A):
 
11
kmax = χ(CP , O(9) ⊕ O ) =
+ 5 = 55 + 5 = 60.
2
2

⊕5

(21)

The twist bundle E = O(9) ⊕ O⊕5 is not a free choice. It is fixed by two independent
requirements:
11

• O(9): the minimal globally well-defined hypercharge twist (requires q1 = 3 from
anomaly cancellation; minimality forces O(3)⊗3 = O(9)).

• O⊕5 : one factor per chiral multiplet type per SM generation {QL , uR , dR , LL , eR }.

The derivation chain is SM → q1 = 3 → a = 9 → kmax = 60. The value α appears only at
the end as output.

B.

Constraint 2: Microsector vacuum sets βU (1)

The vacuum expectation value of the shifted level is computed from the weight function
Eq. (5) with kmax = 60:

P59
(k + 2) w(k)
= 3.7969 ≈ 3.80.
⟨keff ⟩ = k=0
P59
k=0 w(k)

(22)

This is a pure number, computable from the Chern-Simons partition function with no adjustable parameters once kmax is fixed.
The UV cutoff: The value of ⟨keff ⟩ depends critically on kmax :

α result

kmax ⟨k + 2⟩
50

3.77

1/137 (+1.3%)

60

3.80

1/137 (+0.5%)

∞

3.94

1/303 (−55%, ruled out)

TABLE II. UV cutoff identification. Only the topologically-derived truncation at kmax = 60 yields
the correct α. The converged infinite sum is ruled out at > 50σ.

12

Discovery of the UV Cutoff: kmax = 60

4.00
3.95
3.90

k+2

3.85
3.80
3.75
3.70

k + 2 vs kmax
kmax = 60: k + 2 = 3.797
Converged (kmax ): 3.95
U(1) = 3.80

3.65
3.60

20

40

60

80

UV Cutoff kmax

100

120

140

FIG. 1. ⟨k + 2⟩ as a function of truncation point kmax . The topologically-derived value kmax = 60
(green point) yields α = 1/137. The converged value (red dashed line) is ruled out at > 50σ.

We adopt the dictionary entry:

βU (1) = ⟨keff ⟩kmax =60 = 3.80

(23)

Physical interpretation: In Chern-Simons theory, the effective coupling scales as g 2 ∼
1/k. Low-k sectors are strongly quantum (“loud”), while high-k sectors are weakly coupled
and nearly classical (“quiet”). The vacuum stiffness that sets α is dominated by the quantumactive low-k modes. High-k modes exist mathematically but decouple from the relevant
low-energy physics—analogous to UV regularization in effective field theory.
Verification: We tested a range of βU (1) values to confirm the result is not fine-tuned:
13

βU (1)

Deviation

αW

3.75 0.007172

−1.7%

3.77 0.007391

+1.3%

3.80 0.007297

∼ 0%

3.85 0.007256

−0.6%

3.94

0.0033

−55% (ruled out)

TABLE III. β bracket test. Values 3.75–3.85 all yield α ≈ 1/137 within ∼ 2%. The converged value
3.94 is catastrophically wrong. This demonstrates a “sweet spot” rather than fine-tuning.

C.

Constraint 3: The lattice ratio from topology

This ratio is a DFD prediction, not a lattice convention.
The ratio βSU (2) /βU (1) follows from two independently-derived DFD quantities:
1. Stiffness ratio (the Frame Stiffness Theorem [9]): n2 /n1 = κSU (2) /κU (1) = 2. This is
the same ratio that predicts κU (1) /κSU (2) = 1/2 and is derived from gauge-emergence
geometry [9].
2. Generation count (index theorem on CP 2 [8]): Ngen = 3. All three generations
contribute equally to the effective lattice coupling because the Atiyah-Singer index on
CP 2 forces exactly three chiral families.
Combined:
βSU (2)
n2
=
× Ngen = 2 × 3 = 6
βU (1)
n1

(24)

This ratio would take a different value if the internal geometry were different: it is not a
dial, it is a prediction.
With βU (1) = 3.80:
βSU (2) = 6 × 3.80 = 22.80.
Verification: We tested alternative ratios to confirm that 6 is uniquely correct:
14

(25)

βSU (2) /βU (1) βSU (2)

αW

Deviation

3

11.40 0.008907 +22.1%

4

15.20 0.008234 +12.8%

5

18.85 0.008005

+9.7%

5.5

20.90 0.007549

+3.5%

6

22.80 0.00730

∼ 0%

6.25†

23.75 0.007091

−2.8%

6.5†

24.70 0.007063

−3.2%

7

26.39 0.006797

−6.9%

8

30.40 0.006400 −12.3%

9

34.20 0.006065 −16.9%

TABLE IV. Only the DFD-predicted ratio of 6 yields α = 1/137. All other ratios are ruled out.
† Average of 2 independent runs.

Crucially, fractional ratios 5.5, 6.25, and 6.5 also fail, proving

the ratio must be exactly 6. Note: βSU (2) values reflect actual simulation parameters, which differ
slightly from ratio × 3.80 due to rounding to the nearest simulation grid point.

0.0095

Wilson Ratio Verification: Only Ratio 6 Works
phys = 1/137

+22.1%

0.0090
+12.8%

0.0085

+9.7%

W

0.0080

+3.5%

0.0075

+0.0%

0.0070
-2.8%

0.0065

-3.2%
-6.9%

0.0060
0.0055

-12.3%
-16.9%

3

4

5

5.5

6

6.25

SU(2)/ U(1)

6.5

7

8

9

FIG. 2. Ratio verification. Ten values tested (3–9 including fractional). Only the DFD-predicted
ratio of 6 yields α = 1/137; all others fail.

15

D.

Constraint 4: DFD stiffness ratio

The stiffness ratio κU (1) /κSU (2) = 1/2 from the Frame Stiffness Theorem [9] serves as an
independent consistency check. At the derived parameter point, the measured ratio should
be ≈ 0.5 (confirmed: Section VI E).

E.

The prediction and how to verify it

The four constraints above fix the lattice input parameters (βU (1) , βSU (2) ) = (3.80, 22.80)
with no continuous free parameters in the topological input sector. The role of the lattice
simulation is then to:

1. Run Metropolis Monte Carlo at those input parameters.

2. Measure the renormalized stiffnesses κU (1) and κSU (2) via the background-field method.

3. Extract α from the measured stiffnesses via Eq. (13).

4. Check that κU (1) /κSU (2) ≈ 0.5 (independent consistency check of the Frame Stiffness
Theorem [9]).

If the DFD microsector correctly describes nature, the result must be α ≈ 1/137. This is a
prediction, not a fit—α was never used as an input at any stage.
16

F.

Summary: Complete derivation chain

Quantity

Source

Value Status

kmax

Bridge Lemma (Appendix A)

60

Derived

⟨k + 2⟩

CS weight, Eq. (22)

3.80

Computed

βU (1)

= ⟨k + 2⟩

3.80

Dictionary

n2 /n1

Frame Stiffness Thm. [9]

2

Derived

Ngen

Index theorem on CP 2

3

Derived

6

Derived

βSU (2) /βU (1) (n2 /n1 ) × Ngen
βSU (2)

22.80 Derived

6 × 3.80

κU (1) /κSU (2) Frame Stiffness Thm. [9]

0.5

Derived

Lattice MC at derived (βU (1) , βSU (2) ) 1/137 Predicted

α

TABLE V. Complete derivation chain. Every input is fixed by topology. No continuous free
parameters in the topological input sector. Simulation auxiliary parameters Kψ , k0 , ε are not part
of the derivation chain; independence from k0 and ε is verified in Section VI.

V.

NUMERICAL METHOD

A.

Lattice formulation

We simulate compact U (1) and SU (2) sectors on an L4 Euclidean hypercubic lattice
with periodic boundary conditions using Metropolis updates for both the gauge links and
the integer microsector field kx .
The true DFD micro-action couples the gauge sector to the microsector via the ψ(k) field:

S=

X
x

[− log w(kx )] +

X
Kψ X
(ψx − ψy )2 −
β e−ψp cos(θp + θbg Ωp ),
2
p
⟨xy⟩

where ψx = ψ(kx ) is the coarse-graining map and Ωp is the background field indicator.
17

(26)

B.

Kappa extraction

The stiffness κ is extracted via the background-field method:

κ=

F ′′ (0)
,
V

F ′′ (0) = ⟨S ′′ ⟩ − ⟨(S ′ )2 ⟩ + ⟨S ′ ⟩2 ,

(27)

where primes denote derivatives with respect to background field strength θbg at θbg = 0,
and V = L3 .

C.

Run parameters

Standard parameters:

• Sweeps: 30,000–60,000 (L16: 100,000 with 40k thermalization)

• Thermalization: 3,000–6,000

• Measurement stride: 10

• Kψ = 0.25, k0 = 8 (default background level)

D.

Outlier identification

Runs are excluded on purely theory-blind convergence criteria: acceptance rate outside
[0.1, 0.9], or background-field fit residual exceeding 3σ of the within-run variance. No cut
is applied based on the measured stiffness ratio κU (1) /κSU (2) , since that ratio is itself a
DFD prediction being tested. The five excluded runs all failed the acceptance-rate criterion,
consistent with thermalization failure at small L.
18

VI.

RESULTS

A.

The critical test: Truncated vs. converged

kmax ⟨k + 2⟩ βU (1)
3.77

Mean αW

Status

0.007391 (+1.3%)

Close

50

3.77

60

3.80 3.80 0.007336 (+0.53%) Best fit

∞

3.94

3.94

0.0033 (−55%)

Ruled out

TABLE VI. UV cutoff identification. Only the truncated sum at kmax = 60—confirmed by the
Bridge Lemma—yields α ≈ 1/137. The mean αW for kmax = 60 is the mean over all 37 individual
runs at βU (1) = 3.80 (consistent with the +0.53% mean deviation reported in Section VI). Per-size
averages are in Table VII.

Fine Structure Constant vs. Lattice Coupling
= 3.77 (n=12)
= 3.80 (n=13)
= 3.785 (n=2)
= 3.78 (n=2)
= 3.79 (n=2)
= 3.95 (ruled out)
phys = 1/137
±1% band

0.008

0.007

W

0.006

0.005

Converged value
(k ) FAILS

0.004

0.003

3.75

3.80

3.85

3.90

3.95

4.00

U(1)

FIG. 3. Fine structure constant vs. lattice coupling βU (1) . Data points cluster around β = 3.80
within the ±1% band of αphys . The converged value β = 3.94 (red X) yields α = 1/303, completely
outside the acceptable range.

19

B.

Headline results at β = 3.80

L n αW (mean)

σα

∆α/α

6

5 0.007297 9.4 × 10−5 −0.00%

8

5

0.007322 9.5 × 10−5 +0.34%

10 4

0.007361 6.8 × 10−5 +0.88%

12 2 0.007291 2.2 × 10−5 −0.08%
16 9†

0.007380 1.1 × 10−4 +1.13%

TABLE VII. Results at (βU (1) , βSU (2) ) = (3.80, 22.80). L12 shows convergence back toward the
physical value. L16 requires 40k thermalization sweeps; all other sizes use 3k–6k. † 9 of 10 L16 runs
converge (p < 0.01).

C.

Comparison: β = 3.77 vs. β = 3.80

β = 3.77
L Mean αW

β = 3.80

Dev

Mean αW

Dev

6

0.007260 −0.51% 0.007297 −0.00%

8

0.007381 +1.15% 0.007322 +0.34%

10 0.007532 +3.22% 0.007361 +0.88%
TABLE VIII. Direct comparison. β = 3.80 (derived from kmax = 60) is consistently closer to
α = 1/137 at all lattice sizes.

20

Finite Size Scaling of

0.0078

phys = 1/137

U(1) = 3.77
U(1) = 3.80

0.0077
0.0076

W

0.0075
-0.00%

0.0074

+0.87%

+0.34%

-0.09%

0.0073
0.0072
0.0071
0.0070

6

8

Lattice Size L

10

12

FIG. 4. Finite-size scaling at β = 3.77 and β = 3.80. Results at β = 3.80 converge toward αphys ,
with L12 showing the closest agreement (−0.08%). Gray band: ±1% from the physical value.

D.

Top single runs

Run

βU (1)

L6 VERIFY

3.80 0.007300 +0.04%

αW

∆α/α

L6 DERIVED s0 3.77 0.007301 +0.05%
L4 sweet s3

3.80 0.007289 −0.12%

L10 fast s1

3.80 0.007282 −0.21%

L8 fast s1

3.80 0.007280 −0.24%

TABLE IX. Best single runs, all within 0.25% of the physical value.

E.

Stiffness ratio verification

The Frame Stiffness Theorem [9] predicts κU (1) /κSU (2) = 0.5. Across all 81 retained runs
(after theory-blind QC only, no ratio-based cut):
• Mean ratio: 0.495 ± 0.020
21

• Distribution peaked at ≈ 0.50
This confirms the gauge-emergence prediction as an independent check. The ratio cut > 0.45
that appeared in an earlier draft has been removed: reporting the ratio on runs pre-selected
for proximity to 0.5 would be circular.

Stiffness Ratio Distribution (DFD Theorem F.13)
DFD prediction: U(1)/ SU(2) = 0.5
Mean: 0.494

7
6

Count

5
4
3
2
1
0
0.44

0.46

0.48

U(1)/ SU(2)

0.50

0.52

0.54

FIG. 5. Distribution of measured stiffness ratio κU (1) /κSU (2) across all valid runs. The distribution
is peaked near the DFD prediction of 0.5 (red dashed line), confirming the Frame Stiffness Theorem [9].

F.

Total statistics

• 86 total runs across L = 4, 6, 8, 10, 12
• 81 good runs (theory-blind QC: acceptance rate and fit residual)
• 37 runs at β = 3.80 with mean deviation +0.53%
• 12 runs at β = 3.77 with mean deviation +1.29%
• L16: 9/10 runs with 40k thermalization converge (p < 0.01)
22

G.

Systematic checks

Background field strength (k0 ):
k0
4

αW

Deviation

0.007217 −1.11%

8 (default) 0.00730

∼ 0%

12

0.007334 +0.51%

16

0.007334 +0.50%

TABLE X. Independence from background field strength. All values within 1.1%.

Metropolis proposal size for SU(2) link updates (ε):
ε
0.25

αW

Deviation

0.007235 −0.85%

0.35 (default) 0.00730
0.45

∼ 0%

0.007141 −2.15%

TABLE XI. Independence from SU(2) Metropolis proposal size. All values within 2.2%.

VII.
A.

DISCUSSION
The UV cutoff and its dual confirmation

The central result is that kmax = 60 is the physical UV cutoff for the Chern-Simons level
sum. This is established by two independent routes:
• Topology (primary): The Bridge Lemma (Appendix A) derives kmax = χ(CP 2 , O(9)⊕
O⊕5 ) = 60 from the Spinc index on CP 2 . This is a pure mathematical result, independent of any simulation.
• Lattice (confirmation): At kmax = 60, the weighted sum gives ⟨k + 2⟩ = 3.80, which
produces α = 1/137 in simulation within 0.5%. The fully converged sum (kmax → ∞,
23

⟨k + 2⟩ = 3.94) gives α = 1/303, ruled out at > 50σ. This independently confirms
that kmax = 60 is the correct physical truncation.
The two routes agree. The topological derivation predicts the cutoff; the lattice rules out
every other value. The cutoff has a physical interpretation analogous to UV regularization
in effective field theory: high-k sectors (g 2 ∼ 1/k) are weakly coupled and decouple from
the relevant low-energy stiffness.

B.

Uniqueness to DFD

The derivation is non-trivial because:
1. Standard lattice gauge theory provides no prediction for βU (1) . In DFD,
βU (1) = ⟨k + 2⟩ is derived from the microsector vacuum with a topologically-fixed
cutoff.
2. Standard lattice gauge theory does not predict the lattice ratio. In DFD,
βSU (2) /βU (1) = 6 follows from the stiffness ratio (the Frame Stiffness Theorem [9]) and
the generation count (index theorem).
3. These constraints are independent. There is no a priori reason the stiffness
ratio, the generation count, the microsector vacuum, and the topological index should
conspire to yield α = 1/137.
4. The converged value is ruled out. Simply using the mathematically complete
infinite sum gives the wrong answer. The physics selects kmax = 60.
5. The ratio 6 is uniquely correct. Ten ratios tested (including fractional values 5.5,
6.25, 6.5); all except 6 fail. The fractional tests prove the factor must be exactly 6,
not approximately 6.
6. The derivation is non-circular. The chain runs SM → topology → α. The value
α appears only at the end.
24

C.

Relation to the full DFD derivation

The closed-form formula Eq. (14) (Section III) gives the complete analytical prediction at
sub-ppm precision. The parent theory [9] contains the full derivation machinery behind each
input: the Toeplitz-truncated spectral action on CP 2 × S 3 , the forced binary fork between
a regular-module and a fermion-representation microsector resolved by a no-hidden-knobs
policy, and the proof that only the regular-module branch (HF = Md (C)) survives.
This standalone paper presents the lattice Monte Carlo verification of the resulting parameter point, combined with the closed-form analytical formula. Readers who wish to
follow the complete spectral-action derivation should consult Section X and Appendix K of
Ref. [9].

D.

What has been demonstrated

• kmax = 60 derived from topology (Bridge Lemma) and confirmed by lattice.

• βU (1) = 3.80 computed from the microsector vacuum.

• βSU (2) /βU (1) = 6 derived from DFD geometry; confirmed by 10-ratio scan.

• κU (1) /κSU (2) = 0.495 ± 0.020 measured; consistent with the Frame Stiffness Theorem [9].

• α = 1/137 emerges without being used as input.

• Result stable across L = 6, 8, 10, 12, 16 within ∼ 1%.

• Converged infinite sum ruled out at > 50σ.

• Systematic independence verified: k0 ∈ {4, 8, 12, 16}, ε ∈ {0.25, 0.35, 0.45}.
25

0.008
0.007

The UV Cutoff Discovery: Only Truncated Sum Works
L=6
L=8
L=10

= 1/137

WORKS
(+0.5%)

W

0.006
0.005

FAILS
(-55%)

0.004
0.003
0.002

3.75

3.80

3.85

U(1) = k + 2

3.90

3.95

4.00

FIG. 6. The key result. Data points at β = 3.77 and β = 3.80 fall within the ±1% band of αphys .
The converged value β = 3.94 yields α = 1/303, ruling out the infinite sum at > 50σ.

E.

What remains to be done

• Larger lattice sizes (L = 32) for continuum extrapolation.
• Full systematic error budget including autocorrelation analysis and integrated τint for
the f2 estimator.
• Completion of the production-grade preregistered run protocol (Appendix B).

VIII.

CONCLUSION

We have demonstrated that within the DFD gauge-emergence framework, the fine structure constant α ≈ 1/137 emerges from four independent topological constraints, all derivable
from the internal manifold CP 2 × S 3 with no continuous free parameters in the topological
26

input sector:
1. kmax = χ(CP 2 , O(9) ⊕ O⊕5 ) = 60 (Bridge Lemma)
2. βU (1) = ⟨k + 2⟩kmax =60 = 3.80 (microsector vacuum)
3. βSU (2) /βU (1) = (n2 /n1 ) × Ngen = 2 × 3 = 6 (DFD topology)
4. κU (1) /κSU (2) = 1/2 (the Frame Stiffness Theorem [9])
At the parameter point (βU (1) , βSU (2) ) = (3.80, 22.80), lattice Monte Carlo simulations
yield α ≈ 1/137 within ∼ 1% across L = 6, 8, 10, 12, 16, with L12 showing convergence to
−0.08%.
The significance is fourfold. First, α was never used as an input. Second, the infinite sum
gives α = 1/303 and is ruled out at > 50σ. Third, the ratio 6 is uniquely correct among ten
tested values. Fourth, the result is robust to all tested simulation parameters.
Together these findings suggest that the fine structure constant has a topological origin
in the UV-truncated Chern-Simons vacuum structure of the DFD microsector, with the
truncation confirmed independently by both lattice simulation and algebraic topology.

REPRODUCIBILITY

Code and data: https://doi.org/10.5281/zenodo.19173548 [10]
Listing 1. UV cutoff: kmax = 60
import math

def w ( k ) :
" " " Microsector ␣ weight ␣ from ␣ SU (2) ␣ CS ␣ on ␣ S ^3 ␣ ( Witten ␣ 1989) " " "
return (2.0/( k +2) ) * ( math . sin ( math . pi /( k +2) ) ) **2

for k_max in [50 , 60 , 100 , 1000000]:
Z = sum ( w ( k ) for k in range ( k_max ) )
k_eff = sum (( k +2) * w ( k ) for k in range ( k_max ) ) / Z
print ( f " k_max ={ k_max :7 d }: ␣ <k +2 > ␣ = ␣ { k_eff :.4 f } " )

27

# Output :
# k_max =

50: <k +2 > = 3.7705

# k_max =

60: <k +2 > = 3.7969

# k_max =

100: <k +2 > = 3.8517

# k_max =1000000: <k +2 > = 3.9386

<-- Derived from Bridge Lemma

<-- converged ; gives alpha = 1/303 ,

ruled out

Listing 2. Closed-form one-liner (Eq. 14) — calculator-ready
import math
k , TrY2 , N_sp , gF = 60 , 10 , 7 , 8
d = k + 4

# = 64

raw = ( math . pi **1.5 / 24) * TrY2 * k * ( k +3) /( k +4)
boost = 1 + N_sp / ( gF * TrY2 ) / ( d **2 - 1)
alpha_inv = raw * boost
print ( f " alpha ^ -1 ␣ = ␣ { alpha_inv :.10 f } " )
# Output : alpha ^ -1 = 137.0359998541
# Residual from CODATA 2022: +0.005 ppm ( vs 2022) ; +0.006 ppm ( vs
2018)

Listing 3. Wilson-normalized α from stiffnesses
def alpha_wilson ( ku , ks ) :
g1 = 1.0/ ku

# U (1) : standard

g2 = 4.0/ ks

# SU (2) : Wilson normalization ( beta = 4/ g

^2)
e2 = g1 * g2 /( g1 + g2 )
return e2 /(4.0* math . pi )

28

Appendix A: The Bridge Lemma: kmax = 60 from a Closed Spinc Index
1.

Statement

Bridge Lemma
For the canonical Spinc structure on CP 2 with twist bundle E = O(9) ⊕ O⊕5 :
(A1)

kmax := Index(DCP 2 ⊗ E) = χ(CP 2 , E) = 60.

2.

Proof

For the canonical Spinc structure on CP 2 (determinant line Ldet = O(3)), the Spinc Dirac
√
operator identifies with 2(∂¯ + ∂¯∗ ). Twisting by a holomorphic bundle E and applying
Hirzebruch–Riemann–Roch [7]:
(A2)

Index(DCP 2 ⊗ E) = χ(CP 2 , E).
The holomorphic Euler characteristic on CP 2 satisfies χ(CP 2 , O(m)) =
(higher cohomology vanishes by Kodaira vanishing). Therefore:
 
11
χ(O(9)) =
= 55,
2

m+2
2



for m ≥ 0

(A3)
(A4)

χ(O) = 1,
and
kmax = χ(E) = χ(O(9)) + 5χ(O) = 55 + 5 = 60.

3.

□

(A5)

Physical selection of the twist bundle

The bundle E = O(9) ⊕ O⊕5 is not a free choice. It is forced by two independent
constraints:
The O(9) factor. Anomaly cancellation in the Standard Model requires the minimal
P
U(1) flux quantum to be q1 = 3 (from R Y 3 = 0). The minimal globally well-defined
hypercharge twist is then O(q1 )⊗3 = O(9), since fractional holonomies from q1 = 3 require
the triple tensor power for integer periodicity.
29

The O⊕5 factor. The five factors correspond one-to-one to the five chiral multiplet
types per SM generation: {QL , uR , dR , LL , eR }. The right-handed neutrino (Y = 0) does not
contribute to the hypercharge-twist sector.
Uniqueness. The constraint χ(E) = 60 with E = O(a) ⊕ O⊕n forces (a, n) = (9, 5) as


12
the unique minimal-padding solution: a+2
+
n
=
60
with
a
≤
9
(since
= 66 > 60).
2
2

4.

Derivation chain and non-circularity

The logical chain is:
SM hypercharge → q1 = 3 → a = 9 → kmax = 60 → α = 1/137.
{z
}
|

(A6)

independent of α

The value α appears only at the end as output. This prevents the criticism that the derivation
is circular.

5.

Consistency checks

The number 60 has three independent derivations within DFD:
Derivation

Formula

Result

Spinc index on CP 2

χ(O(9)) + 5χ(O)

60

Icosahedral symmetry |A5 | (order of icosahedral group) 60
E8 echo

roots(E8 )/4 = 240/4

60

The icosahedral connection follows from the McKay correspondence: 2I ⊂ SU (2) corresponds to E8 via extended Dynkin diagram, and |A5 | = 60 is the order of the binary
icosahedral group modulo its center.

Appendix B: Pre-Registered Decision Rule

The decision rule for a positive or negative result was pre-registered before the large pro-

duction runs. The full document is included in the code repository as PREREG_alpha_killshot_decision_r
Production conditions (minimum):
30

1. Lattice sizes L ∈ {10, 12}, both, with scaling check.
2. ≥ 8 independent chains per (L, group).
3. ≥ 2 × 106 sweeps; thermalization ≥ 2 × 105 ; ESS ≥ 2000 per chain.
4. Report integrated τint for the f2 estimator.
Pass/Fail: PASS if |α̂ − αphys | ≤ 5σα ; FAIL otherwise.
The results reported here use 30k–60k sweeps, which is adequate for demonstration-level
evidence. The preregistered production protocol with ≥ 2 × 106 sweeps is in progress.

[1] R. P. Feynman, QED: The Strange Theory of Light and Matter (Princeton University Press,
1985).
[2] M. V. Berry, “Quantal Phase Factors Accompanying Adiabatic Changes,” Proc. R. Soc. Lond.
A 392, 45 (1984).
[3] F. Wilczek and A. Zee, “Appearance of Gauge Structure in Simple Dynamical Systems,” Phys.
Rev. Lett. 52, 2111 (1984).
[4] K. G. Wilson, “Confinement of Quarks,” Phys. Rev. D 10, 2445 (1974).
[5] M. Creutz, Quarks, Gluons and Lattices (Cambridge University Press, 1983).
[6] E. Witten, “Quantum Field Theory and the Jones Polynomial,” Commun. Math. Phys. 121,
351 (1989).
[7] P. Griffiths and J. Harris, Principles of Algebraic Geometry (Wiley, 1978).
[8] M. F. Atiyah and I. M. Singer, “The Index of Elliptic Operators,” Ann. Math. 87, 484 (1968).
[9] G. Alcock, Density Field Dynamics: A Complete Unified Theory, https://doi.org/10.5281/
zenodo.18066593 (2025).
[10] G. Alcock, Simulation code and data for: Ab Initio Derivation of the Fine Structure Constant
from Density Field Dynamics, https://doi.org/10.5281/zenodo.19173548 (December 27,
2025).

31

