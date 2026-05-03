---
source_pdf: dfd_neutrino_paper_v7_s2_seesaw_closure.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

A Closed-Form Neutrino Sector from DFD v3.5: TBM Geometry, a
Discrete S2 Lock, and a Seesaw Scale Closure
Gary Alcock
January 1, 2026
Abstract
DFD v3.5 provides three ingredients that, when combined with a strict no-hidden-knobs
rule, appear to close the neutrino sector to a surprising extent: (i) a tribimaximal (TBM)
neutrino mixing base from the neutrinos-at-center overlap rule (Appendix K), (ii) a derived
heavy √
Majorana scale MR = MP α3 (Appendix P), and (iii) a derived electroweak scale v =
8
MP α 2π (Section 13 / Appendix K).
This note pushes a fourth ingredient as hard as possible. TBM singles out a canonical
residual transposition S2 (the µ ↔ τ swap), and the unique smallest positive S2 -equivariant
deformation of the identity is I + P− , where P− projects onto the odd-parity axis. On the
doublet this produces eigenvalues (2, 1) exactly, hence a discrete lock m2 /m1 = 2.
√The closure step is that the same S2 doublet structure also forces a normalization
√ factor
1/ 2 in the center-coupling
Dirac
overlap,
turning
the
Appendix-P
ansatz
y
∼
α into a
D
p
no-knobs value yD = α/2. With the seesaw, this removes the remaining continuous scale
and yields explicit absolute masses, mass-squared splittings, and 0νββ and beta-decay effective
masses in terms of α and MP only.

1

What TBM gives you for free in DFD (and what it does not)

Appendix K of the unified manuscript states the TBM base (when neutrinos are “at center”):
p
p

p1/3 p0
p2/3

UTBM = −p 1/6
(1)
p1/3 p1/2 .
1/6 − 1/3
1/2
TBM fixes the eigenvectors (columns) and therefore fixes a discrete set of residual permutation
symmetries of the neutrino mass matrix. However, TBM by itself does not fix the eigenvalues
(m1 , m2 , m3 ).
The push here is: can TBM’s residual symmetry content, plus a strict no-hidden-knobs principle,
force a specific doublet split such as m2 /m1 = 2?

2

Why full S3 invariance cannot split a doublet

Let generation space carry the permutation representation of S3 . The S3 -invariant endomorphisms
are the centralizer, spanned by I3 and J = 11T . On the standard doublet subspace {x1 +x2 +x3 = 0}
one has J = 0, hence every S3 -equivariant operator is proportional to the identity on the doublet.
Therefore:
Any non-degenerate doublet spectrum requires breaking S3 to a proper subgroup.
1

3

TBM naturally singles out a transposition S2 (the µ ↔ τ swap)

Consider the transposition that swaps the µ and τ components:


1 0 0
Sµτ = 0 0 1 .
0 1 0
Its eigenvectors in the µ–τ plane are the even and odd parity axes
1
v− = √ (0, 1, −1),
2

1
v+ = √ (0, 1, 1),
2

with Sµτ v± = ±v± . Up to an unphysical rephasing of the τ row, the TBM basis contains exactly
this even/odd structure: the third TBM column is v+ as written above, and a row sign flip converts
it to v− without changing physical mixing probabilities. Thus TBM motivates a canonical residual
transposition subgroup S2 = ⟨Sµτ ⟩.

4

The no-hidden-knobs split: the minimal positive S2 -equivariant
deformation is I + P−

Let P− be the rank-1 projector onto the odd axis v− :


0 0
0
1
T
P− := v− v−
= 0 1 −1 .
2
0 −1 1
Impose three no-knobs constraints:
1. Residual symmetry: the splitting operator must commute with Sµτ .
2. Positivity: it must be positive (mass-like, not tachyonic).
3. Minimality: among nontrivial choices, pick the smallest deformation of I with no continuous
coefficient.
The unique candidate satisfying these is
O := I3 + P− .

(2)

On v− one has Ov− = 2v− , while on the orthogonal complement of v− one has eigenvalue 1 (because
P− annihilates that subspace). In particular,
λ− : λ+ = 2 : 1
on the two parity axes.
If the light-neutrino doublet (m1 , m2 ) corresponds to the (v+ , v− ) parity sectors under the
TBM-motivated S2 , then the minimal no-hidden-knobs split is
m2
= 2.
m1
2

5

A fully explicit neutrino mass matrix (TBM + m2 /m1 = 2 +
m3 /m2 = α−1/3 )

Assume the DFD hierarchy

m3
= r := α−1/3 ,
m2

and the discrete lock above m2 /m1 = 2. Then, up to the overall scale m1 , the spectrum is fixed:
m1 : m2 : m3 = 1 : 2 : 2r.
Using TBM eigenvectors, the mass matrix is
Mν = m1 P1 + (2m1 ) P2 + (2rm1 ) P3 ,
where the TBM projectors Pi = ci cTi are rational matrices. Writing them explicitly:




4 −2 2
1
1 −1
1
1
1 −1 ,
P1 = −2 1 −1 ,
P2 =  1
6
3
2 −1 1
−1 −1 1


0 0 0
1
P3 = 0 1 1 .
2
0 1 1

(3)

(4)

Therefore, the neutrino mass matrix is fixed in closed form:





 
4 −2 2
1
1 −1
0 0 0
2
1
1 −1 + r 0 1 1 .
Mν = m1  −2 1 −1 +  1
6
3
2 −1 1
−1 −1 1
0 1 1

(5)

All entries are rational linear combinations of (1, r), with r = α−1/3 fixed by the single topological
constant α.

6

Parameter-free oscillation invariant (the compression)

From m1 : m2 : m3 = 1 : 2 : 2r one gets
∆m221 = 3m21 ,

∆m232 = 4(r2 − 1)m21 ,

hence

∆m232
4 2
4  −2/3
=
(r
−
1)
=
α
−
1
≈ 34.106787 .
3
3
∆m221

7

Seesaw closure from S2 normalization

√
Appendix P motivates a center-overlap Dirac Yukawa scale yD ∼ α. In the presence of the TBMselected S2 doublet, there is a canonical no-hidden-knobs refinement: if the relevant center-coupled

3

right-handed state is the normalized √
symmetric combination of a two-state subspace, then any
overlap amplitude acquires a factor 1/ 2. Thus one is led to
r
√
α
α
yD = √ =
.
2
2

(6)

With the DFD theorem MR = MP α3 and the seesaw estimate mν ∼ (yD v)2 /MR , the heaviest
light-neutrino mass closes as
m3 =

(α/2) v 2
v2
=
.
MP α 3
2MP α2

(7)

√
Using v = MP α8 2π, this becomes a pure α-power:
m3 = π MP α14 .

(8)

Given the fixed ratios m2 /m1 = 2 and m3 /m2 = α−1/3 , all three light masses follow:
m1 =

8

m3
,
2α−1/3

m2 =

m3
,
α−1/3

m3 = πMP α14 .

(9)

Numerical predictions (manuscript conventions)

Using the manuscript values α−1 = 137.036, MP = 1.22 × 1019 GeV, and v = 246.09 GeV, Eq. (7)
gives:
Quantity

Prediction

Notes

m1
m2
m3
Σmν

4.52 meV
9.04 meV
46.61 meV
60.17 meV

from m2 /m1 = 2 and m3 /m2 = α−1/3
same
from the S2 -normalized seesaw closure
fully determined

6.13 × 10−5 eV2
2.09 × 10−3 eV2
34.1068

equals 3m21
equals 4(r2 − 1)m21
equals (4/3)(α−2/3 − 1)

∆m221
∆m232
∆m232 /∆m221

Beta decay and neutrinoless double beta decay (TBM limit)
In the TBM limit Ue3 = 0,
r

4
2
1
mββ = m1 + m2 = m1 ,
3
3
3

mβ =

2 2 1 2 √
m + m = 2 m1 .
3 1 3 2

(10)

Thus
mββ = 6.03 meV,

mβ = 6.39 meV.

4

(11)

9

Falsifiers specific to this closure

This closure is deliberately sharp, so it can fail sharply:
• If the measured ratio ∆m232 /∆m221 is incompatible with (4/3)(α−2/3 − 1) at high precision,
the S2 lock m2 /m1 = 2 is wrong.
• If future cosmology strongly prefers Σmν far from ∼ 60 meV while α remains fixed, then the
S2 -normalized seesaw closure (or the identification of MR ) fails.
• If 0νββ bounds push below ∼ 6 meV (in the same TBM-limit mapping), the TBM+S2 closure
for the (m1 , m2 ) subspace fails.

Pointer
Unified DFD manuscript (Zenodo DOI): https://doi.org/10.5281/zenodo.18066593

5

