---
source_pdf: Density_Field_Dynamics__Scalar_Refractive_Gravity__Quantum_Resolution__and_Dual_Sector_Electrodynamics.pdf
title: "Density Field Dynamics: Scalar Refractive Gravity, Quantum Resolution, and"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Density Field Dynamics: Scalar Refractive Gravity, Quantum Resolution, and
Dual-Sector Electrodynamics
Gary Alcock
Los Angeles, CA, USA
(Dated: October 1, 2025)
We develop Density Field Dynamics (DFD), a scalar-field framework in which a single refractive
index field ψ(x, t) replaces curved spacetime. Light propagates with optical index n = eψ , matter
accelerates as a = (c2 /2)∇ψ, and ψ obeys a nonlinear Poisson equation. This reproduces all
classical weak-field tests of General Relativity (deflection, redshift, Shapiro, perihelion), matches
PPN at O(1/c2 ), and explains galactic dynamics without dark matter via the crossover function
µ(|∇ψ|/a⋆ ).
DFD offers a clean resolution of the Penrose measurement paradox: superpositions always source a
single ψ field, eliminating the “two geometries” problem, while quantum evolution in this background
remains strictly unitary. We contrast DFD with Diósi–Penrose (DP) objective reduction, and state
a quantitative prediction: null deviations from unitary quantum mechanics in regimes targeted at
DP collapse times.
Finally, we show that in the dual-sector extension, Maxwell electrodynamics is consistently embedded in a ψ-dependent vacuum. A controlled ϵ/µ split preserves the optical metric speed vph = c/n,
while ψ-gradients and time-variation yield small, falsifiable corrections. Faraday induction remains
∇ × E = −∂t B (a Bianchi identity); the dual sector explains the sectoral response (electric vs.
magnetic) through the split, not by altering the identity. The same bracket [B 2 /µ − ϵE 2 ] governs
ψ sourcing, energy exchange, and body force, with concrete predictions in cavity and clock experiments. We parameterize the split as g(ψ) = κψ and show how κ is constrained and measured by
sector-resolved LPI slopes.

I.

CORE POSTULATES OF DFD

1. Light propagation:
n(x) = eψ(x) ,

c1 (x) =

c
= c e−ψ .
n

(1)

2. Matter dynamics:
a=

c2
∇ψ ≡ −∇Φ,
2

2

Φ ≡ − c2 ψ.

(2)

3. Field equation (nonlinear Poisson form):


8πG
∇· µ(|∇ψ|/a⋆ )∇ψ = − 2 (ρ − ρ̄).
c

(3)

Normalization by −8πG/c2 fixes GR’s optical tests (deflection, redshift, Shapiro).

II.

CLASSICAL TESTS AND PPN
A.

Newtonian limit

For point mass M with µ → 1:
ψ(r) =

2GM
,
c2 r

a=−

GM
r̂.
r2

(4)

2
B.

Light deflection, redshift, delay

With n ≃ 1 + ψ:
4GM
,
c2 b
∆ν
∆Φ
=− 2 ,
ν
c
4GM
∆t =
(two-way).
c3

(5)

α=

C.

(6)
(7)

PPN check

Expanding DFD to O(1/c2 ) reproduces γ = β = 1, all others 0 [6].
III.

PENROSE PARADOX, SCHRÖDINGER DYNAMICS, AND DP COMPARISON
A.

One ψ for superpositions: existence and uniqueness

Penrose argued that a mass superposition implies a superposition of geometries, in conflict with the single Hilbert
space of quantum
mechanics [9–11]. In DFD, mass density enters the sourcing equation linearly, so for a superposition
P
state |Ψ⟩ = i ci |Mi ⟩ the effective density is
X
ρeff (x) = ⟨Ψ|ρ̂(x)|Ψ⟩ =
|ci |2 ρi (x).
(8)
i

The field equation is elliptic with monotone µ, so standard theorems guarantee existence and uniqueness of a single
ψ solution for given ρeff (no branch geometries).
B.

Justifying the Schrödinger operator

We now justify the modified kinetic operator
iℏ ∂t Ψ = −
by three mutually consistent routes:
(i) Hamiltonian and classical limit.



ℏ2
∇· e−ψ ∇Ψ + mΦ Ψ,
2m

2

Φ = − c2 ψ,

(9)

Take the single-particle Hamiltonian
H(x, p) =

e−ψ(x) 2
p + mΦ(x).
2m

(10)

Hamilton’s equations give ẋ = e−ψ p/m and
p2
p2 −ψ
∇(e−ψ ) − m∇Φ = +
e ∇ψ − m∇Φ.
(11)
2m
2m
In the non-relativistic regime p2 /2m ≪ mc2 , the force is dominated by −m∇Φ = (mc2 /2)∇ψ, yielding a = (c2 /2)∇ψ
as required by DFD. Quantizing H with a symmetric-ordering prescription p2 7→ −ℏ2 ∇ · (·)∇ yields Eq. (9).
(ii) WKB/Hamilton–Jacobi. Insert Ψ = A eiS/ℏ into Eq. (9); to leading order in ℏ one obtains the Hamilton–Jacobi
equation
ṗ = −∇H = −

e−ψ
|∇S|2 + mΦ = 0,
(12)
2m
with p = ∇S; this is exactly the classical Hamiltonian (10). The next order gives the continuity equation with
probability current

ℏ  ∗ −ψ
j=
Ψ e ∇Ψ − Ψ e−ψ ∇Ψ∗ ,
(13)
2mi
which is conserved, confirming self-adjointness.
∂t S +

3
(iii) Covariant wave in optical metric. The optical metric viewpoint sets ds2 = −c2 e−2ψ dt2 + dx2 for phase
propagation (eikonal). The minimally coupled scalar wave operator □opt Ψ = 0 reduces in the nonrelativistic limit to
Eq. (9) with vph = c/n (details omitted for brevity; see also matter-wave derivations in [7, 8]).

C.

DP collapse vs. DFD prediction (quantitative)

DP proposes gravity-induced objective reduction with collapse time τDP ∼ ℏ/∆EG where ∆EG is the gravitational
self-energy of the difference density between branches [11–13]. For a simple toy estimate of two identical lumps of
mass m separated by d,
∆EG ∼

Gm2
,
d

τDP ∼

ℏd
.
Gm2

(14)

Examples:
• Large molecules (tested): m ∼ 104 amu ≃ 1.7 × 10−23 kg, d ∼ 100 nm ⇒ τDP ∼ 5 × 1015 s ≫ experimental
timescales; both DP and DFD predict unitary evolution. (See [14–16].)
• Mesoscopic spheres (future): m ∼ 10−14 kg, d ∼ 1 µm ⇒ ∆EG ∼ 6.7 × 10−33 J, τDP ∼ 0.016 s. Here DP
predicts visible collapse; DFD predicts null (no intrinsic collapse). Cantilever and opto-mechanical bounds are
approaching this region [17].
DFD prediction: For any platform claiming sensitivity to τDP ≲ 1 s, expect no gravity-induced deviations from
unitary QM (within stated uncertainties). The decisive DFD test remains the sector-resolved LPI slope (Sec. VIII),
where GR predicts a strict null.

IV.

SECTOR-RESOLVED LPI TEST

Compare cavity frequency (f ∼ c/n) with atomic frequency across two altitudes ∆h. Observable slope:
∆R
∆Φ
= ξ (M,S) 2 ,
R
c
(M )

(15)

(S)

with ξ (M,S) = αw − αL − αat .
GR: ξ = 0. Base DFD: ξ ≃ 1 ⇒ slope ∼ g∆h/c2 ≈ 1.1 × 10−14 per 100 m.

V.

MAXWELL ELECTRODYNAMICS IN A ψ-DEPENDENT VACUUM

We build on the classical foundations of Faraday’s induction and field concept, Maxwell’s field equations, Heaviside’s
vector reformulation, and standard modern expositions [1–5] by embedding Maxwell’s equations in a ψ-dependent
vacuum.

A.

Constitutive split preserving vph = c/n

ϵ(ψ) = ϵ0 n(ψ) e+κψ ,

µ(ψ) = µ0 n(ψ) e−κψ ,

n = eψ .

(16)

Here ϵ(ψ) and µ(ψ) vary oppositely such that their product tracks n2 /c2 , thereby preserving the optical-metric phase
speed vph = c/n.
ϵ(ψ)µ(ψ) = ϵ0 µ0 n2

⇒

1
c
vph = p
= .
n
ϵ(ψ)µ(ψ)

(17)

4
B.

Variational equations

Action
1
L = Lψ − 21 ϵ(ψ)E2 + 2µ(ψ)
B2 + J · A − ρϕ.

(18)

Varying ϕ and A yields Maxwell in a ψ-dependent medium:
∇ · (ϵE) = ρ,
∇ × H = J + ∂t D,
∇ × E = −∂t B,

∇ · B = 0,

(19)
(20)
(21)

with D = ϵE, H = B/µ.
C.

Corrections from ∇ψ and ψ̇

Ampère’s law acquires
∇ × B = µJ +

κ
1
∂t E + 2 ψ̇ E − κ(∇ψ × B).
c2
c

(22)

Corrections vanish for uniform ψ; appear in gradients/time variation. Faraday and ∇ · B = 0 remain identities.
D.

Energy, momentum, and sourcing

EM energy density and flux:
u = 21 (ϵE2 + B2 /µ),

S = E × H.

(23)

Poynting theorem:

B2 
∂t u + ∇ · S = −J · E − κ2 ψ̇ ϵE2 −
.
µ

(24)

Body force:
fψ = − κ2

 B2
µ


− ϵE2 ∇ψ.

(25)

ψ sourcing:
 B2

δLψ
= Smass + κ2
− ϵE2 .
δψ
µ

(26)

Thus the unified bracket governs energy exchange, momentum transfer, and scalar sourcing.
VI.

STANDING-WAVE ENERGY EQUALITY (AND WHERE IMBALANCE ENTERS)

For a lossless, steady-state standing wave in a linear medium, the cycle-averaged integrated electric and magnetic
energies are equal:
Z
Z
2
ϵE dV =
B 2 /µ dV,
(27)
V

V

so V (B 2 /µ − ϵE 2 ) dV = 0. This follows from multiplying the wave equation by E, integrating by parts, and using
the steady-state condition; no appeal to the mechanical virial theorem is needed.
Nonzero local bracket arises at O(θ2 ) due to longitudinal fields in paraxial Gaussian modes (Sec. VII); it matters
(i) when weighted by ∇ψ in the body-force channel, and (ii) for polarization/mode mixing tests (TE vs. TM). It does
not dominate the LPI slope, which is set by sector coefficients.
R

5
VII.

CAVITY MODE EXAMPLE

For a Fabry–Pérot resonator in TEM00 :
Ex = E0 cos(kz) e−(x +y )/w0 ,

2

2

2

(28)

2
2
2
By = Ec0 sin(kz) e−(x +y )/w0 .

(29)

R
By Eq. (27), (B 2 /µ − ϵE 2 )dV = 0 (time-averaged, integrated).
Paraxial longitudinal components generate a local imbalance at O(θ2 ):
ϵE 2 − B 2 /µ ∼ θ2 ϵ|E0 |2 ,

θ=

λ
.
πw0

(30)

For λ = 1064 nm, w0 = 300 µm, θ2 ≃ 1.3 × 10−6 . Implications: (i) the global LPI slope is dominated by sector
coefficients (next section), (ii) TE/TM swaps and orientation provide clean internal nulls/cross-checks. These parameter choices and cavity/clock operating regimes are representative of state-of-the-art platforms used in ultra-stable
resonators and optical clocks [27–29].
VIII.

LPI PREDICTION WITH κ (QUANTITATIVE)

The slope is
(M )

ξ (M,S) (κ) = 1 − αL

(S)

− αat (κ),

(S)

αat (κ) = Kϵ(S) κ + O(κ2 ),

(31)

(S)

where Kϵ is the (dimensionless) atomic EM-energy sensitivity.
(S)
Order-of-magnitude for Kϵ . Atomic optical transition energies scale with the effective Rydberg R∞ ∝ 1/ϵ2 (in
SI), modulo relativistic and many-body corrections; thus a crude estimate gives
δE
δϵ
≃ −2
E gross
ϵ

⇒

Kϵ(S) ∼ O(1–3),

(32)

with species/line dependence (fine/hyperfine and configuration mixing modify the coefficient). For Sr and Yb clock
(S)
(S)
transitions, Kϵ is plausibly order unity; the sector-resolved 4→3 GLS disentangles δat ∝ Kϵ κ from material (δL )
and total (δtot ) combinations.
Numbers. Keep the base prediction |∆R/R| ≈ g∆h/c2 ≃ 1.1 × 10−14 per 100 m. The dual-sector introduces
(S)
an order-unity modulation of ξ if Kϵ κ ∼ 1. Polarization (TE/TM) and dual-λ checks separate this from dispersion/thermals.
IX.

EXISTING BOUNDS ON κ AND RELATED SEARCHES

PPN and optical tests. DFD matches GR at 1PN [6]; choosing the nondispersive band with vph = c/n preserved
ensures solar-system optics are unaltered.
Why metrology has not already seen it. Most precision tests are two-way or single-sector: they cancel the sectoral
response. The LPI ratio is a sector comparison under ∆Φ/c2 change with internal nulls (swap/flip/dual-λ).
Cavity stability (accidental bound). Absence of 2ω parametric instabilities in extreme-Q resonators constrains
unintended EM↔ ψ pumping. This provides headroom consistent with |κ| below order unity; a dedicated LPI
measurement is still required to bound/measure κ.
Altitude/diurnal constraints. A pure cavity-to-cavity comparison at different altitudes largely tracks n (commonmode) and does not isolate κ; the dual-sector signature appears most cleanly in cavity vs. atom ratios with identical
geopotential steps. Diurnal solar tides (∆Φ/c2 ∼ 10−10 ) imply fractional modulations ∼ ξ 10−10 ; current clock
comparisons place strong LPI bounds on generic α(Φ)-type couplings [18–20], but those do not directly exclude
a sectoral κ that cancels in single-sector measurements. The proposed sector-resolved LPI explicitly avoids such
cancellations.
LLI / Michelson–Morley modern tests. Modern rotating-cavity experiments bound anisotropies in the speed of
light at ∼ 10−17 –10−18 [23, 24]. Our construction preserves two-way c and embeds Maxwell consistently, so these
tests are satisfied by design.

6
Equivalence principle & varying α. MICROSCOPE bounds differential acceleration at η ≲ 10−15 (final analysis)
[25, 26]; DFD’s matter acceleration is universal at given ψ so EP is respected. Constraints on α̇/α and α(Φ) from
clock comparisons exist at ≲ 10−16 –10−17 /year and ≲ 10−6 with solar potential modulation [18, 21, 22]; mapping
(S)
these onto κ depends on how ϵ variations propagate to atomic lines (captured here by Kϵ ). The clean way to
(S)
constrain κ is therefore the sector-resolved LPI slope itself, which directly measures Kϵ κ.
X.

TIKZ CONCEPT SKETCHES

ϵ
ψ enforces vph = c/n

µ
FIG. 1. Dual-sector ψ fabric: ϵ and µ shift oppositely while preserving vph = c/n, consistent with the optical metric.

mirror

mirror
FIG. 2. Fabry–Pérot cavity with TEM00 Gaussian profile. Time-averaged integrated electric and magnetic energies cancel;
paraxial longitudinal fields produce a local bracket at O(θ2 ).

XI.

CONCLUSIONS

DFD replaces curved spacetime with a scalar ψ refractive field. It recovers GR’s classical tests, resolves Penrose’s
“two geometries” problem by ensuring a unique ψ with unitary quantum evolution, and predicts a nonzero LPI slope.
In the dual-sector extension, Maxwell electrodynamics is consistently embedded in a ψ-dependent vacuum with an
ϵ/µ split that preserves vph = c/n. The unified bracket [B 2 /µ − ϵE 2 ] controls energy, momentum, and sourcing, with
concrete predictions. Falsifiers: ξ = 0 across all cavity–atom pairs (contrary to DFD), no ψ-pumping under designed
drive, no sectoral asymmetries under TE/TM swaps, and any verified DP-like intrinsic collapse at predicted τDP
scales.

[1] M. Faraday, “Experimental Researches in Electricity,” Philos. Trans. R. Soc. Lond. 122, 125–162 (1831).
[2] J. C. Maxwell, “A Dynamical Theory of the Electromagnetic Field,” Philos. Trans. R. Soc. Lond. 155, 459–512 (1865).
[3] O. Heaviside, Electromagnetic Theory, articles in The Electrician (1888–1891).
[4] J. D. Jackson, Classical Electrodynamics, 3rd ed. (Wiley, 1999).
[5] D. J. Griffiths, Introduction to Electrodynamics, 5th ed. (Cambridge, 2017).
[6] C. M. Will, Theory and Experiment in Gravitational Physics, updated ed. (Cambridge, 2018).
[7] C. J. Bordé, “Theoretical tools for atom optics and interferometry,” C. R. Acad. Sci. Paris 2, 509–530 (2001).

7
[8] P. Storey and C. Cohen-Tannoudji, “The Feynman path integral approach to atomic interferometry. A tutorial,” J. Phys.
II France 4, 1999–2027 (1994).
[9] R. Penrose, The Emperor’s New Mind (Oxford Univ. Press, 1989).
[10] R. Penrose, Shadows of the Mind (Oxford Univ. Press, 1994).
[11] R. Penrose, “On gravity’s role in quantum state reduction,” Gen. Relativ. Gravit. 28, 581–600 (1996).
[12] L. Diósi, “Models for universal reduction of macroscopic quantum fluctuations,” Phys. Rev. A 40, 1165 (1989).
[13] S. Adler and A. Bassi, “Collapse models: Analysis of the free particle dynamics,” J. Phys. A 40, 15083 (2007); A. Bassi et
al., Rev. Mod. Phys. 85, 471 (2013).
[14] M. Arndt et al., “Wave–particle duality of C60 molecules,” Nature 401, 680–682 (1999).
[15] S. Gerlich et al., “Quantum interference of large organic molecules,” Nat. Commun. 2, 263 (2011).
[16] Y. Y. Fein et al., “Quantum superposition of molecules beyond 25 kDa,” Nat. Phys. 15, 1242–1245 (2019).
[17] A. Vinante et al., “Improved noninterferometric test of collapse models using ultracold cantilevers,” Phys. Rev. Lett. 119,
110401 (2017).
[18] T. Rosenband et al., “Frequency ratio of Al+ and Hg+ single-ion optical clocks; stability and systematic uncertainty,”
Science 319, 1808–1812 (2008).
[19] P. Delva et al., “Test of special relativity using a fiber network of optical clocks,” Phys. Rev. Lett. 121, 231301 (2018).
[20] N. Ashby et al., “Testing local position invariance with four Cesium-fountain primary frequency standards and four NIST
hydrogen masers,” Phys. Rev. A 98, 052507 (2018).
[21] R. M. Godun et al., “Frequency ratio of two optical clock transitions in Yb+ and constraints on the time variation of
fundamental constants,” Phys. Rev. Lett. 113, 210801 (2014).
[22] N. Huntemann et al., “Improved limit on a temporal variation of mp /me from comparisons of Yb+ and Cs atomic clocks,”
Phys. Rev. Lett. 113, 210802 (2014).
[23] C. Eisele, A. Yu. Nevsky, S. Schiller, “Laboratory test of the isotropy of light propagation at the 10−17 level,” Phys. Rev.
Lett. 103, 090401 (2009).
[24] M. Nagel et al., “Direct terrestrial test of Lorentz symmetry in electrodynamics to 10−18 ,” Nat. Commun. 6, 8174 (2015).
[25] P. Touboul et al., “MICROSCOPE Mission: First Results,” Phys. Rev. Lett. 119, 231101 (2017).
[26] P. Touboul et al., “MICROSCOPE Mission: Final Results,” Phys. Rev. Lett. 129, 121102 (2022).
[27] T. Kessler et al., “A sub-40-mHz-linewidth laser based on a silicon single-crystal optical cavity,” Nat. Photonics 6, 687–692
(2012).
[28] T. Nicholson et al., “Systematic evaluation of an atomic clock at 2 × 10−18 total uncertainty,” Nat. Commun. 6, 6896
(2015).
[29] W. McGrew et al., “Atomic clock performance enabling geodesy below the centimetre level,” Nature 564, 87–90 (2018).

