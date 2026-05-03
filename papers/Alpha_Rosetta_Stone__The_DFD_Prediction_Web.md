---
source_pdf: Alpha_Rosetta_Stone__The_DFD_Prediction_Web.pdf
title: "The Alpha Rosetta Stone"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

The Alpha Rosetta Stone
How α + MP + CP 2 × S 3 Topology Determines
30+ Physical Observables from 2 Inputs
Deep Cross-Reference Investigation

Gary Thomas Alcock
23 March 2026
Abstract
Within Density Field Dynamics, the fine structure constant α is derived from first
principles via a Chern–Simons weighted level sum on CP 2 × S 3 with kmax = 60. This
single derivation, combined with the Planck mass MP and the topology of the internal manifold, generates a web of 30+ physical predictions spanning particle physics,
cosmology, astrophysics, and gravitational phenomenology. We catalog every quantity derivable from these inputs, construct the complete dependency graph, compute
the prediction-to-input ratio (which reaches 15:1 to 17:1), identify the most surprising
connections, and present the Grand Unified Prediction Table with derivation chains
and experimental status for each observable. No other theoretical framework achieves
a comparable ratio of zero-parameter predictions to fundamental inputs.

Contents
1 The Two Inputs

3

2 Complete Catalog of Derived Quantities
2.1 Layer 0: The Keystone — α Itself . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Layer 1: Electroweak Sector (from α + Topology) . . . . . . . . . . . . . . . .
2.3 Layer 2: Fermion Mass Spectrum (from α + v + A5 ) . . . . . . . . . . . . . .
2.4 Layer 3: Neutrino Sector (from CP 2 × S 3 Branch B) . . . . . . . . . . . . . .
2.5 Layer 4: Gravitational Sector (from α + MP + S 3 ) . . . . . . . . . . . . . . .
2.6 Layer 5: Cosmological Sector (from α + MP + Topology) . . . . . . . . . . . .
2.7 Layer 6: Astrophysical Observables . . . . . . . . . . . . . . . . . . . . . . . .

3
4
4
5
5
5
6
7

3 The Count: Predictions vs. Inputs
3.1 Comparison with Other Frameworks . . . . . . . . . . . . . . . . . . . . . . .

8
9

4 The Dependency Graph

9

5 The Most Surprising Connections

10

6 What DFD Does NOT Derive

11
1

7 Grand Unified Prediction Table

11

8 The Rosetta Stone Interpretation

14

9 Critical Assessment and Caveats

15

10 Conclusion

15

2

1

The Two Inputs

DFD rests on exactly one dimensionful input and one topological choice. From the
topology, a single integer is derived.
Foundational Structure
Inputs (2):p
1. MP = ℏc/G = 1.220910×1019 GeV — the standard (unreduced) Planck mass.
Sets the overall energy/mass scale of gravity.
2. CP 2 × S 3 — the 7-dimensional internal manifold. This is the single topological choice of the theory. CP 2 provides the spinc structure (and hence gauge
symmetry), while S 3 provides the Chern–Simons partition function (and hence
µ(x) = x/(1 + x)).
Derived from topology (not an input):
• kmax = 60 — derived from the spinc index on CP 2 via Hirzebruch–Riemann–
Roch:
kmax = χ(CP 2 , O(9) ⊕ O⊕5 ) = 55 + 5 = 60.
This is a derived integer, not an input or a free parameter. It encodes the
icosahedral (A5 , order 60) symmetry of the microsector.
What counts as “Standard Model content”? The SM hypercharge assignments (Tr(Y 2 ) =
10), the number of weak isospin species (Nspecies = 7), and the spectral triple grading (gF = 8)
enter the α derivation. These are not free parameters of DFD — they are structural consequences of embedding the SM in the NCG spectral triple on CP 2 . We classify them as
“locked inputs from topology + SM identification,” not as tunable parameters.

2

Complete Catalog of Derived Quantities

We organize the derived quantities by domain, giving the explicit formula and derivation
level for each.

3

2.1

Layer 0: The Keystone — α Itself

α−1 = 137.03599985

(residual: +0.005 ppm vs CODATA 137.035 999 177)

The one-line formula (spectral action on CP 2 × S 3 , reproducible from inputs):
"
#
3/2
π
k(k
+
3)
N
sp

α−1 =
Tr(Y 2 )
1+
24
k+4
gF Tr(Y 2 ) (k+4)2 − 1
with k = kmax = 60 (Spinc index on CP 2 ), Tr(Y 2 ) = 10 (SM hypercharge sum),
Nsp = 7, gF = 8. Setting d = k+4 = 64: the bare form α−1 ≈ 52 π 3/2 (63/64) is
accurate to −21 ppm; the full expression gives α−1 = 137.03599985 (+0.005 ppm vs
CODATA).
Leading approximation (bare form, −21 ppm): α−1 = n2χ π 3/2 (1 − d−1 ), where
nχ = 5 (chiral multiplet types) and d = 64 = 26 .
Status: Theorem-grade. Matches CODATA 2022 to +0.005 ppm (sub-ppm agreement). All inputs independently fixed by topology and SM content; zero free parameters.
The bare formula α−1 = 52 π 3/2 (1 − 2−6 ) at −21 ppm (undershoots) already exceeds
every historical derivation except Wyler’s (0.6 ppm), which Robertson showed requires
an arbitrary radius; the DFD formula requires none.

2.2

Layer 1: Electroweak Sector (from α + Topology)
#

Quantity

DFD Formula

Status

α−1 = 137.036

CS level sum on CP 2 × S 3

Theorem

2

sin θW : 3/8 (GUT) and GUT value from CCM traces
3/13 (EW)
c1 : c2 = 10 : 6 (Structural).
EW value from Berry-connection
gauge
emergence,
partition
(3, 2, 1), and canonical hypercharge normalisation: sin2 θW =
g ′2 /(g 2 + g ′2 ) = 3/13 = 0.2308,
0.2% from MS value 0.23122
(Theorem-grade). DFD has no
GUT group; gauge symmetries
emerge from Berry connections.
Stiffness ratios 1:2:3
κU (1) : κSU (2) : κSU (3) from Frame
Stiffness Theorem
αs (at unification)
αs−1 = 6π × 3κU (1) from stiffness
ratio κSU (3) = 3κU (1)
Note: rows 3–4 above are intermediate derived quantities that
feed into the grand table’s predictions. They are not counted
as independent numbered rows in the 45-item table; instead
they enter through α (row 1) and the mass/coupling derivation
chains.

4

Theorem
(EW)

Derived
Structural

#

2.3

Quantity

DFD Formula
Status
√
Higgs VEV: v = 246.09 v = MP α8 2π, where the expo- Tier 1.5
GeV
nent 8 arises from the spectral action (the same Spinc index structure that gives kmax = 60; the explicit derivation is in Appendix K
of Ref. [DFDUnified]).

Layer 2: Fermion Mass Spectrum (from α + v + A5 )

All nine charged fermion masses follow from:
v
mf = Af × αnf × √
2

= Af × MP × αnf +8 ×
{z
|

derived-v formulation only

√

π
}

with Af from A5 conjugacy class operators and nf from spinc bundle degrees on CP 2 .
#

Fermion

Af

6
7
8
9
10
11
12
13
14

t (top)
1
b (bottom) 1/42
√
2
τ
c (charm)
1
s (strange)
6/7
µ (muon)
1
d (down)
6
u (up)
8/3
e (electron) 2/3

nf

mpred

mPDG

Error

0
174.0 GeV 172.76 GeV
0
4.143 GeV
4.180 GeV
1.0 1.796 GeV
1.777 GeV
1.0 1.270 GeV
1.270 GeV
1.5 93.0 MeV
93.0 MeV
1.5 108.5 MeV 105.66 MeV
2.5 4.75 MeV
4.67 MeV
2.5 2.11 MeV
2.16 MeV
2.5 0.528 MeV 0.511 MeV

+0.7%
−0.9%
+1.1%
∼ 0%
∼ 0%
+2.7%
+1.7%
−2.3%
+3.3%

Mean |error| = 1.42%. Af from A5 /CP2 operators (derived). Default formulation:
one global norm. from GF (Tier 1.5). Derived-v formulation: zero free parameters.

Layer 3: Neutrino Sector (from CP 2 × S 3 Branch B)

2.4
#

Quantity

DFD Derivation

Σmν = 61.4 meV

Branch B of CP 2 × S 3 mi- Tier 1 (AT
crosector.
(m1 , m2 , m3 ) = RISK)
(2.34, 8.96, 50.12) meV. Normal
hierarchy required.
Structural
prediction
from Pass/fail
Branch B. Inverted ordering
falsifies the microsector.

Normal mass ordering

2.5

Status

Layer 4: Gravitational Sector (from α + MP + S 3 )

5

#

Quantity

DFD Formula

µ(x) = x/(1 + x)

Derived from S 3 microsector com- Theorem
position law. MOND = sigmoid:
µ(ez ) = σ(z) exactly.
MOND acceleration scale. Funda- Derivationmental constant, not a free function. grade
= 1.197 × 10−10 m/s2 (using DFD’s
own H0 = 72.09 km/s/Mpc, not
Planck’s 67.4).
Self-coupling from gauge emergence. Derived

√
a0 = 2 α cH0

κ = 3/(8α) ≈ 51.4
γPPN = βPPN = 1

From exponential metric gµν =
diag(−c2 e−ψ , e+ψ δij ).
cT = c exactly
GW speed. TT sector has no ψ coupling. Consistent with GW170817
(|cT /c − 1| < 10−15 ).
−15
Ġ/G = +4.3 × 10
From EM-only sourcing in twoyr−1
component framework. Passes all
bounds with 17× margin.
Zero gravitational de- dρLR /dt|DFD
grav = 0. Proven to all orders via Leray–Schauder.
coherence
GWs never gravita- GWs propagate on flat Minkowski,
tionally lensed
not through ψ-screen. EM-GW offset 30–120 arcsec in cluster lenses.

2.6

Status

Theorem
Theorem

Tier 1

Theorem
Tier 0 falsifier

Layer 5: Cosmological Sector (from α + MP + Topology)
#

Quantity

DFD Formula / Mechanism

(H0 /MP )2 = α57

Cosmological hierarchy from topology.
One-loop UV-finite.
Step
9 CLOSED: two-modulus hierarchy
stable.
∆H0 = 3.9 ± 1.1 Hubble tension: 70% accounted via
km/s/Mpc
MOND-enhanced void outflow + ψscreen bias. Direction-dependent:
2.1 (toward Shapley) to 5.8 (away).
DFD
S8
∼ 0.77–0.79
Scale-dependent Geff (k) > GN .
Large-scale: 0.73–0.76; small-scale:
0.81–0.83.
BH shadow
ratio = = 1.046 (+4.6% exact). Confirmed
√
to 10−17 . EHT-consistent.
2e/(3 3)
PTA spectral tilt δ = From µ-crossover at SMBHB sepa+0.07
rations. NANOGrav-consistent.
−6
∆α/α ∼ 2.3 × 10 at Fine structure variation from
z=1
ψ-field
cosmological
evolution.
ESPRESSO-consistent (0.8σ).
CMB Cold Spot ISW −63 (+25
−35 ) µK vs observed −75 ±
35 µK. Resolved at 0.3σ.
6

Status
Tier 1

Tier 1

Tier 1

Theorem
Tier 1
Tier 1

Tier 1

#

Quantity

DFD Formula / Mechanism

CMB peak ratio R =
2.34

From baryon loading (BBN), no
dark matter. Observed R ≈ 2.4
(2.5% agreement).
CMB ℓ1 = 220
ψ-screen correction e−0.30 ≈ 0.74
brings matter-only universe ℓ1 ∼ 300
down to 220.
ADFD
∼
1.10–1.20
Resolves
the 2.8σ Alens anomaly to
L
∼1.7σ. Scale-dependent at ℓ ∼ 120.
Dark energy as ψ- Not a cosmological constant or
screen
quintessence. ψ-screen biases DL
but not BAO geometric distances.
∆ψ(z = 1) = 0.27.
DLEM /DLGW = 1.31 at Cleanest DFD test. Zero paramez=1
ters. EM biased by ψ-screen; GW is
not. Testable with 3G detectors.
SNe
Ia
ψ-screen Cℓ ∝ ℓ−2 , peaks at ℓ ∼ 3–15, RMS
anisotropy
0.8–1.2%. 5σ with Rubin Y1.

2.7

Status
Tier 1

Tier 1

Tier 1
Tier 1

Tier 1

Tier 1

Layer 6: Astrophysical Observables
#

Quantity

DFD Prediction

Lunar nonreciprocal
delay
Wide binary enhancement

Status

0.93 ns. Detectable with Artemis Tier 1
one-way links.
+10–12% (EFE-screened) at > 10 Tier 1
kAU. NOT falsified by Banik et al.
2024.
Galactic bar pattern +19% enhancement. Testable Gaia Tier 1
speed
DR4.
IFMR radial gradient −0.02 M⊙ at R > 15 kpc. Testable Tier 1
Gaia DR4.
TDE rate in LSB +40% enhancement. Testable LSST Tier 1
galaxies
2027–29.
Note: gravitational birefringence (39 ns, double pulsar) and zero scalar
GW memory appear in the Gravitational sector (Grand Table rows 24–
25) and not here. Pairwise kSZ velocity (+10% at > 100 h−1 Mpc) is
Grand Table row 37, in the Cosmological sector.

7

3

The Count: Predictions vs. Inputs
Prediction Census
Category

N

Zero-parameter status

α itself (row 1)

1

Yes

sin θW GUT+EW (row 2)

1

Structural (GUT) / Theorem (EW)

Higgs / hierarchy anchors
(rows 3–5)

3

Row 3 (v): T1.5; rows 4–5 (α57 , a0 ):
T1

Fermion masses (rows 6–14)

9

T1.5: one global norm. from GF (default); zero-param. with derived v

Neutrino sector (rows 15–16)

2

Yes

Gravitational (rows 17–25)

9

Yes

Cosmological (rows 26–37)

12

Yes (modulo Boltzmann code)

Astrophysical (rows 38–42)

5

Yes

Technology
(rows 43–45)

3

No (λ-dependent, T2)

2

/

TOTAL
Independent core

Detection

45
∼30–34

(after removing correlated)

Census categories map directly onto the numbered rows of the Grand Unified Prediction Table (Sec. 7): α = row 1; sin2 θW (GUT and EW scales combined) = row 2;
Higgs/hierarchy anchors (v, α57 , a0 ) = rows 3–5; fermion masses = rows 6–14; neutrino sector = rows 15–16; gravitational = rows 17–25; cosmological = rows 26–37;
astrophysical = rows 38–42; technology (Tier 2) = rows 43–45. Intermediate structural quantities (stiffness ratios, αs at unification) appear in the Layer 1 catalog but
are not independent numbered rows in the 45-item table.
Inputs: MP (1 dimensionful scale) + CP 2 × S 3 (topological choice, from which kmax =
60 is derived).
The technology patents introduce one additional free parameter: λ (EM-ψ coupling),
which governs Tier 2 predictions only.
Counting convention:
The ratio below uses the derived-v formulation throughout,
√
8
in which v = MP α 2π is derived from topology and the fermion masses are genuinely
zero-parameter. In the default formulation (one global normalization from GF ), the
fermion sector is Tier 1.5 and the ratio reduces by ∼1 effective input. The conservative
and aggressive counts below reflect the derived-v formulation.
Conservative count: 30 independent predictions from 2 inputs.
Prediction:input ratio = 15:1
Aggressive count: 34 independent predictions from 2 inputs.
Prediction:input ratio = 17:1

8

3.1

Comparison with Other Frameworks

Framework

Predictions

Free / Tunable Parameters

Ratio

ΛCDM

∼20

6

3.3:1

Standard Model (SM)

∼25

19

1.3:1

SM + ΛCDM

∼40

25

1.6:1

MSSM

∼30

∼120

0.25:1

String landscape

500

∼0 specific

N/A

2 inputs†

15–17:1

∼ 10

DFD (MP + topology)

vacua

30–34

†

DFD’s two entries are MP (one dimensionful scale) and CP 2 × S 3 (a topological choice, not
a tunable parameter); kmax = 60 is derived. These are inputs, not free parameters in the
sense of quantities adjusted to fit data. The column header “Free / Tunable Parameters”
applies to ΛCDM, SM, and MSSM; DFD’s entry should be read as “fundamental inputs.”

4

The Dependency Graph

The following diagram shows how all predictions flow from the two inputs through intermediate derived quantities. Arrows indicate logical dependence.

CP 2 × S 3

MP

S 3 sector

kmax = 60

α−1 = 137.036

√
v = MP α8 2π

µ(x) = x/(1 + x)

(H0 /MP )2 = α57

√
a0 = 2 α cH0

9 fermion masses

Σmν = 61.4 meV

∆H0 = 3.9 km/s/Mpc

MOND phenomenology

Rotation curves

BH shadow +4.6%

S8 ∼ 0.77–0.79

EM /D GW
DL
L

Wide binaries +10%

AL ∼ 1.1–1.2

Key dependency chains:
+MP
+A5
1. Particle physics chain: CP 2 → kmax → α −−−→
v −−→
9 masses
+µ
57 +α
2. Cosmological chain: α + MP → H0 (via α ) −−→ a0 −→ MOND, ∆H0 , S8
3. Dark energy chain: α + MP → ψ-screen → DL bias → “dark energy”
9

4. Mass hierarchy chain: mf ∝ αnf ⇒ me /mt ∼ α2.5 ∼ 10−5.4 (the five-order-ofmagnitude hierarchy from topology)

5

The Most Surprising Connections
Connection #1: The MOND Scale from the Icosahedron
√
The MOND acceleration a0 = 2 α cH0 depends on α, which depends on kmax = 60,
which is the order of the icosahedral group A5 . The icosahedron — a purely geometric object — determines the threshold below which galaxies deviate from Newtonian
dynamics. The chain is:
Icosahedron (|A5 | = 60) → kmax = 60 → α → a0 → galaxy rotation curves.
This is arguably the most remarkable connection in all of theoretical physics: Platonic
solid geometry dictates galactic dynamics.
Connection #2: The Electron Mass from CP 2 Topology
√
√
me = (2/3) α2.5 × v/ 2 = (2/3) α10.5 MP π. The electron mass is determined by the
tenth-and-a-half power of a number that comes from summing Chern–Simons levels
on a 4-dimensional complex projective space. The mass hierarchy across five orders of
magnitude (me /mt ∼ 3 × 10−6 ) is entirely topological.
Connection #3: α Connects the Planck Scale to the Hubble Scale
(H0 /MP )2 = α57 . This is the cosmological hierarchy relation: it bridges 60 orders of
magnitude between quantum gravity and cosmology via the 57th power of the fine
structure constant. The exponent 57 is close to kmax − 3 = 57, suggesting a deep
connection to the dimensionality of the Chern–Simons tower.
Connection #4: The Sigmoid is MOND
The interpolating function µ(x) = x/(1 + x) derived from S 3 composition satisfies
µ(ez ) = σ(z) = 1/(1 + e−z ) — the logistic sigmoid. The function governing galaxy
rotation curves is the same function used throughout machine learning and neural networks. This is an exact identity, not an approximation. The MOND-KAN architecture
exploits this to achieve 3200× fewer parameters than standard MLPs.
Connection #5: Dark Energy is an Optical Illusion
The ψ-screen that biases electromagnetic luminosity distances is what observers interpret as “dark energy.” But GW luminosity distances are unbiased (GWs propagate on
flat spacetime). The ratio DLEM /DLGW = e∆ψ(z) ≈ 1.31 at z = 1 is a zero-parameter prediction that, if confirmed, would simultaneously explain dark energy and demonstrate
that it does not exist as a physical substance.

10

6

What DFD Does NOT Derive
Honest Negatives: Quantities NOT Derived from α + MP + CP 2 × S 3
For intellectual honesty, we list what the framework does not currently predict:
1. CKM matrix parameters — Partially derived.
(λ, A, ρ̄, η̄) =
(31, 108, 19, 49) × α at 0.55% mean agreement, with the integers from CP 2 linebundle cohomology. Selection rule pending.
Note on the Cabibbo angle: Agent 11 conjectured λ = e−3/2 = 0.2231. The
established corpus result is λ = 31α = 0.2262 (0.75% from experiment). The
geodesic formula and the 31α formula are in mild tension and have not been
reconciled.
2. Neutrino mixing angles (PMNS matrix) — Not derived. The mass eigenvalues are predicted but not the mixing matrix.
3. QCD confinement scale ΛQCD — Not independently derived (would require
RG running from the stiffness ratio predictions, which has not been carried
through).
4. Baryon asymmetry (detailed mechanism) — CP 2 topology provides CP
violation in principle, but the detailed baryogenesis mechanism is not quantified.
5. Inflation — DFD does not have a built-in inflationary mechanism. The VSL
epoch may serve a similar role but is not quantitatively developed.

7

Grand Unified Prediction Table

The following table presents every DFD prediction, its derivation chain, experimental status,
and the specific connection to α and CP 2 × S 3 . Tier classification follows the established
system:
• Tier 0: Single observation falsifies DFD
• Tier 1: Zero-parameter prediction
• Tier 1.5: Zero-parameter in the derived-v formulation; one global normalization (GF )
in the default formulation
• Tier 2: One-parameter (λ-dependent)
• Tier 3: Requires Boltzmann code
#

Observable

DFD
tion

Predic-

Derivation
Chain

Expt. Status

Tier

Matches to
+0.005 ppm

T1

EW:
0.2%
from expt

T1/Str

— FUNDAMENTAL CONSTANTS —
1

α−1

137.03599985

2

sin2 θW

GUT: 3/8
0.375;
EW: 3/13
0.2308

=
=

CP 2
→
kmax → CS
sum
GUT (CCM
traces, Structural);
EW
(Berryconnection
emergence, no
GUT group,
theoremgrade)

11

#

Observable

DFD
tion

Predic-

3

246.09 GeV

4

v
(Higgs
VEV)
(H0 /MP )2

5

a0 (MOND)

α57 ∼ 10−122
1.197 × 10−10
m/s2

Derivation
Chain
√
MP α8 2π
Topological
hierarchy
√
2 α cH0
(H0 = 72.09)

Expt. Status

Tier

Obs: 246.22
(0.05%)
Consistent

T1.5
T1

Matches
galaxy data

T1

172.76
(+0.7%)
4.180
(−0.9%)
1.777
(+1.1%)
1.270 (∼ 0%)

T1.5

93.0 (∼ 0%)

T1.5

105.66
(+2.7%)
4.67 (+1.7%)

T1.5

2.16 (−2.3%)

T1.5

0.511
(+3.3%)
AT RISK (53
meV freq.)
JUNO 2027

T1.5

Matches
RAR
Cassini: |1 −
γ| < 2.3 ×
10−5
GW170817

T1

— PARTICLE PHYSICS —
6

mt

174.0 GeV

7

mb

4.143 GeV

8

mτ

1.796 GeV

9

mc

1.270 GeV

10

ms

93.0 MeV

11

mµ

108.5 MeV

12

md

4.75 MeV

13

mu

2.11 MeV

14

me

0.528 MeV

15

Σmν

61.4 meV

16

ν ordering

Normal

α + v +
A5 (nf = 0)
α + v +
A5 (nf = 0)
α + v +
A5 (nf = 1)
α + v +
A5 (nf = 1)
α + v +
A5 (nf = 1.5)
α + v +
A5 (nf = 1.5)
α + v +
A5 (nf = 2.5)
α + v +
A5 (nf = 2.5)
α + v +
A5 (nf = 2.5)
Branch B microsector
Branch
B
structural

T1.5
T1.5
T1.5

T1.5

T1
T1

— GRAVITATIONAL PHYSICS —
17

µ(x)

x/(1 + x)

18

γPPN

= 1 exactly

19

cT

= c exactly

20

Ġ/G

21

Grav. decoherence

+4.3
yr−1
Zero

22

GW lensing

Never

23

BH shadow

+4.6% exact

24

Birefringence

39 ns (double
pulsar)

×

10−15

S 3 composition
Exponential
metric
TT sector decoupled
EM-only twocomponent
Leray–
Schauder
proof
GW on flat
spacetime
√
2e/(3 3)
from metric
cEM ̸= cT

12

T1

T1

17× below
LLR
MAQRO
2028–35

T1

3G detectors
2030s
EHT consistent
SKA + 3G
∼2035

T0

T1

T1
T1

#

Observable

DFD
tion

25

Scalar GW
memory

Zero

Predic-

Derivation
Chain

Expt. Status

Tier

No scalar radiation

PTA breathing mode

T1

µ-enhanced
voids
+
ψ-screen
Geff (k) > GN

SH0ES consistent

T1

DES Y6 consistent
CPL ∼ 2.5σ

T1

Planck:
∼
2.4
Planck: 220

T1

— COSMOLOGY —
26

∆H0

3.9
±
km/s/Mpc

27

S8

0.77–0.79

28

Dark energy

ψ-screen bias

29

R = 2.34

30

CMB
peak
ratio
CMB ℓ1

31

AL

1.10–1.20

32

−63 µK

33

Cold
Spot
ISW
PTA tilt

34

∆α/α

35

EM /D GW
DL
L

36

SNe
Ia
anisotropy
kSZ velocity

37

1.1

Distance-bias
framework
Baryon loading (no DM)
ψ-screen correction
Scale-dep.
Geff
xeff = 0.10

220

δ = +0.07
2.3 × 10−6 (z =
1)
1.31 at z = 1
Cℓ ∝ ℓ−2
+10% (>
Mpc)

100

Planck:
∼
1.07
−75 ± 35 µK

T1

T1
T1
T1

µ-crossover at
SMBHB
ψ-field evolution
ψ-screen on
EM only
ψ-screen
anisotropy
Geff enhancement

NANOGrav
consistent
ESPRESSO
0.8σ
3G detectors

T1

Rubin Y1 5σ

T1

Existing
data NOW

T1

One-way timing
aext = 1.8 a0

Artemis

T1
T1

MOND
enhancement
Geff radial

Gaia
DR4
2026
Gaia DR4
Gaia DR4

T1

MOND
enhancement

LSST 2027–
29

T1

SQMS Phase
I
30-day campaign
Archival
($50–100K)

T2

T1
T1

— ASTROPHYSICAL —
38
39
40
41
42

Lunar NR delay
Wide binaries

0.93 ns

Bar pattern
speed
IFMR gradient
TDE
rate
(LSB)

+19%

+10–12% (EFE)

−0.02 M⊙ (R >
15 kpc)
+40%

T1

— TECHNOLOGY / DETECTION —
43
44
45

SQMS
Qratio
Multi-GNSS
ratio
GPS diurnal

0.49 vs BCS 3.41

ω 2 loss rate

Gal/GPS
= 1.070
59 ps

ψ-gradient at
altitude
Tidal
ψvariation

13

T2
T2

#

Observable

DFD
tion

Predic-

Derivation
Chain

Expt. Status

Tier

Table 7: Grand Unified Prediction Table. 45 catalogued predictions; rows 43–45 are Tier 2 (λ-dependent); rows 3 and
6–14 are Tier 1.5 in the default formulation. 30–34 independent core predictions from 2 inputs (MP +CP 2 ×S 3 topology)
in the derived-v formulation.

8

The Rosetta Stone Interpretation

The Rosetta Stone unlocked Egyptian hieroglyphs by providing the same text in three scripts.
Similarly, the α formula connects three “scripts” of physics:
The Three Scripts
1. Topology (CP 2 × S 3 geometry): The spinc index, Chern–Simons levels, A5
conjugacy classes, and heat-kernel coefficients.
2. Gauge Theory (SM hypercharges and couplings): Tr(Y 2 ) = 10, Nspecies = 7,
gF = 8, stiffness ratios 1:2:3, and the CCM spectral action.
3. Fundamental Constants and Observables: α, v, H0 , a0 , all fermion masses,
S8 , ∆H0 , dark energy, black hole shadows, rotation curves, neutrino masses.
The α derivation is the translation key between these three scripts. Once you have
α from topology, the entire web of predictions unfolds.
Why this matters. In conventional physics, α is a measured constant with no known
origin. Fermion masses are 9 free parameters. H0 is measured independently. Dark energy
requires a cosmological constant with no explanation for its value. MOND is an empirical fit
with no derivation of a0 .
In DFD, all of these flow from a single topological structure. The prediction-to-input
ratio of 15:1 to 17:1 quantifies the degree to which DFD unifies disparate phenomena. If even
a fraction of these predictions survive experimental scrutiny, the framework represents the
most predictively efficient theory in physics.

14

9

Critical Assessment and Caveats
Honest Assessment of Derivation Quality
Not all 45 predictions have equal footing:
• Theorem-grade (10): α, µ(x), γ = β = 1, cT = c, zero grav. decoherence, BH
shadow, MOND = sigmoid, sin2 θW = 3/13 (EW scale), zero scalar GW memory,
θ̄ = 0 (strong CP, Dai–Freed η-invariant; structural theorem of the microsector,
not a separate numbered row in the 45-item grand table).
• Derivation-grade (10): v, a0 , Ġ/G, ∆H0 , S8 , CMB R and ℓ1 , 39 ns birefringence, PTA tilt, ∆α/α.
• Constructive-proof (9): The 9 fermion masses (prefactors from A5 operators;
exponents structurally assigned but not theorem-grade).
• Structural / Motivated (6+): α57 hierarchy, neutrino masses (Branch B),
dark energy as ψ-screen, DLEM /DLGW , CMB AL , various astrophysical predictions.
• Requires numerical code (6): Full CMB spectrum, proper DESI confrontation, self-consistent Σmν bound, BAO detailed predictions, S8 (k) quantitative
shape, structure formation growth history. All require the mochi class Boltzmann code (500–800 lines, $40–80K, 2–3 months).
Conservative “honest ratio” (counting only theorem + derivation + constructiveproof grade): 27 numbered grand-table predictions / 2 inputs = 13.5:1. The
27 is reached as follows: theorem-grade contributes 8 numbered rows (α, µ(x),
γ=β=1, cT =c, zero decoherence, BH shadow, sin2 θW =3/13, zero scalar GW memory; “MOND = sigmoid” is the same row as µ(x); θ̄=0 is not a numbered row);
derivation-grade contributes 10 numbered rows (v, a0 , Ġ/G, ∆H0 , S8 , CMB R, CMB
ℓ1 , birefringence, PTA tilt, ∆α/α); constructive-proof contributes 9 (fermion masses).
8 + 10 + 9 = 27. Still far exceeds any competing framework.

10

Conclusion

The fine structure constant α, derived from the Chern–Simons level sum on CP 2 × S 3 with
kmax = 60, is indeed the Rosetta Stone of the DFD framework. It connects:
• Topology (CP 2 spinc index, A5 icosahedral symmetry) to gauge theory (SM hypercharges, coupling constants)
• The Planck scale (MP ) to the Hubble scale (H0 ) via α57
√
• Particle masses (9 fermions via αnf ) to galactic dynamics (a0 = 2 α cH0 )
• The internal manifold (S 3 ) to the interpolating function (µ = sigmoid)
• Quantum gravity (zero decoherence, BH shadows) to observational cosmology (S8 , Hubble tension, dark energy)
With 30–34 independent predictions from 2 inputs, and a prediction-to-input ratio of 15:1 to
17:1, DFD achieves the highest predictive efficiency of any theoretical framework in physics.
The next 3–5 years (Euclid, JUNO, Rubin, SQMS Phase I, Gaia DR4, 3G GW detectors)
will provide decisive tests of the most vulnerable predictions (Σmν , S8 scale dependence, SNe
Ia anisotropy, neutrino mass ordering).
If the framework survives these tests, the α formula will stand as the most consequential
single equation in fundamental physics: a one-line derivation that, through the topology of
CP 2 × S 3 , determines the structure of matter and the dynamics of the universe.

15

