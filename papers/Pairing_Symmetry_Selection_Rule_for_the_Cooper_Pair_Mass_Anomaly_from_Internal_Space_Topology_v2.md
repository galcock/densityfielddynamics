---
source_pdf: Pairing_Symmetry_Selection_Rule_for_the_Cooper_Pair_Mass_Anomaly_from_Internal_Space_Topology_v2.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Pairing-Symmetry Selection Rules for the Cooper-Pair Mass Anomaly
from A5 Microsector Representation Theory
Gary Alcock1
1

Independent researcher, Los Angeles, California, USA
(Dated: March 19, 2026)

The Cooper-pair mass in niobium, measured by Tate et al. (1989) via the London moment, exceeds
twice the free-electron mass by δ = 92 ± 21 ppm—an anomaly unexplained for 36 years. Working
within the A5 microsector of Density Field Dynamics (DFD), we establish three results at decreasing
levels of rigor. First (exact within the pair-space construction): two pairing-symmetry selection
rules. (a) An angular-cancellation rule: the quintet exchange channel in S 2 (V ∗ ) = 1 ⊕ 5 couples
maximally to s-wave condensates but vanishes for d-wave condensates, whose sign-changing gap
produces destructive interference. (b) An orthogonality rule: spin-triplet pairs live in Λ2 (V ∗ ) = 3,
which is orthogonal to the quintet by representation theory alone, independent of gap structure.
Second (mechanism conjecture): the physical Cooper pair |00⟩ carries quintet weight 2/3, accessing
an exchange channel unavailable to uncorrelated single
scale O(α2 ). Third
√ electrons, at the natural√
(numerical conjecture): a motivated coefficient δ = 3 α2 = 92.23 ppm, with 3 from the threegeneration structure of CP 2 × S 3 . Unlike the BCS-exchange correction of Lipavský (2016), which is
material-dependent, the framework predicts universality for conventional s-wave superconductors—a
distinction testable with existing technology.

INTRODUCTION

A rotating superconductor generates a magnetic field
B = −(2m∗ /e∗ ) ω (the London moment), where m∗ is
the effective Cooper-pair mass and e∗ = 2e [1, 2]. Tate
et al. at Stanford, using a rotating niobium ring with
SQUID flux detection, measured [3, 4]
 ∗ 
m
= 1.000 084 (21) .
(1)
2me Nb
Standard relativistic and lattice-potential corrections
predict m∗ /2me = 0.999 992 [5, 6], giving a residual
anomaly
δTate = 92 ± 21 ppm ,

(2)

a 4.4σ discrepancy in the wrong direction (mass increase
rather than decrease).
Three theoretical responses exist.
Tajmar and
de Matos [7] attributed the anomaly to an enhanced gravitomagnetic London moment, but used δTate as input;
precision tests subsequently ruled out gravitomagnetic
coupling at the required magnitude [8, 9]. De Matos [10]
invoked a graviton mass inside the condensate, also using δ as input. Most substantively, Lipavský [11] showed
that Pauli exchange processes—partner-swapping within
the BCS condensate—produce a positive relativistic mass
correction, reversing the sign predicted by earlier BECtype calculations. His result matches Tate’s magnitude
for niobium, but the correction enters through the crystal work function (W ≈ 4 eV for Nb) and the pairing
strength ∆/EF , making it material-dependent.
No existing theory provides all three of: (a) pairingsymmetry selection rules with distinct predictions for swave, d-wave, and p-wave materials, (b) material inde-

pendence for a defined class of superconductors, and (c) a
numerical prediction for the anomaly magnitude.
In this Letter we present three results, with their epistemic status explicitly labeled following the claim taxonomy of Ref. [12]: selection rules exact within the A5
pair-space construction, a mechanism conjecture identifying the exchange channel, and a numerical conjecture
for the coefficient.

FRAMEWORK

Density Field Dynamics (DFD) [12] replaces spacetime
curvature with a scalar refractive field ψ on flat R3,1 , with
optical metric ds̃2 = −c2 e−2ψ dt2 + dx2 and refractive index n = eψ . The internal manifold X = CP 2 × S 3 yields
the Standard Model gauge group, three fermion generations from c2 (CP 2 ) = 3, and the fine-structure constant
α−1 = 137.036 from Chern–Simons quantization on S 3
with kmax = |A5 | = 60 [12].
The A5 microsector assigns each fermion generation to
the fundamental three-dimensional representation V ∗ of
A5 (the icosahedral rotation group). The finite Yukawa
operator [12] acts on the group algebra C[A5 ] via Cayleygraph matrix elements and conjugacy-class projectors,
producing the fermion mass hierarchy with 1.9% mean
accuracy across nine charged fermions [12].
The gravitational clock coupling for a single electron
arises at one loop [12]:
kα =

α2
≈ 8.48 × 10−6 ,
2π

(3)

where one factor of α is the ψ–EM vacuum vertex
strength and α/(2π) is the Schwinger anomalous magnetic moment [13].

2
RESULT I: PAIRING-SYMMETRY SELECTION
RULES

(Exact within the A5 pair-space construction)
A Cooper pair is a two-electron bound state. In the A5
microsector, each electron’s generation quantum number
lives in V ∗ (dim V ∗ = 3). The pair’s internal microsector
state lives in the tensor product V ∗ ⊗ V ∗ , which decomposes as
V ∗ ⊗ V ∗ = S 2 (V ∗ ) ⊕ Λ2 (V ∗ ) ,

(4)

S 2 (V ∗ ) = 1 ⊕ 5 ,

(5)

with

2

∗

Λ (V ) = 3 .
2

(6)

the condensed-matter input of the gap symmetry; it requires both ingredients.

Spin-triplet pairs (p-wave)

For spin-triplet pairing (p-wave, ℓ = 1), the situation is
fundamentally different. The orbital wavefunction is antisymmetric, the spin part is symmetric (triplet), so overall antisymmetry requires the internal microsector part
to be antisymmetric: the pair lives in Λ2 (V ∗ ) = 3.
Since Λ2 (V ∗ ) and S 2 (V ∗ ) are orthogonal subspaces of
∗
V ⊗ V ∗ , the triplet pair has exactly zero projection onto
the quintet 5:
⟨5 | ΠΛ2 | 5⟩ = 0 .

(8)

∗

The quintet 5 in S (V ) is the exchange channel relevant
to the mass anomaly. Which component of V ∗ ⊗ V ∗ is
physically realized depends on the overall exchange symmetry of the full pair wavefunction Ψpair = ψorb ⊗ χspin ⊗
ϕinternal , which must be antisymmetric under particle exchange.
Spin-singlet pairs (s-wave and d-wave)

In conventional BCS superconductors and in cuprate
d-wave superconductors, pairing is spin-singlet [14]: the
spin part χspin is antisymmetric. Both s-wave (ℓ = 0)
and d-wave (ℓ = 2) orbital wavefunctions are symmetric under exchange. Overall antisymmetry then requires
the internal microsector part ϕinternal to be symmetric,
placing both cases in S 2 (V ∗ ).
The distinction between s-wave and d-wave therefore
arises not from the A5 decomposition, but from how the
gap symmetry enters the coupling to the exchange channel.
For an s-wave condensate, the gap ∆k = ∆ eiθ is
isotropic. The anomalous propagator F (k) = ⟨ck↑ c−k↓ ⟩
locks all angular channels to the same macroscopic phase
θ. When the exchange operator acts on the pair, every angular direction contributes coherently, and the coupling to the quintet is maximal.
For a d-wave condensate, ∆k = ∆0 cos 2ϕk , which
changes sign at four nodal directions. The angular integral governing the coherent coupling becomes
Z 2π
dϕ
cos 2ϕ = 0 .
(7)
2π
0
The sign-changing gap produces destructive interference
that cancels the exchange coupling.
Selection Rule 1 (angular cancellation).—Within the A5
pair-space construction, the quintet exchange channel of
S 2 (V ∗ ) produces a nonzero ψ-coupling for s-wave condensates and a vanishing coupling for d-wave condensates. This rule is exact given the A5 decomposition and

Selection Rule 2 (representation orthogonality).—Spintriplet pairs live in Λ2 (V ∗ ), which is orthogonal to the
quintet exchange channel by A5 representation theory
alone. The anomalous mass correction vanishes identically for spin-triplet superconductors, independent of gap
symmetry, angular structure, or any condensed-matter
input beyond the spin state.
This is a purely representation-theoretic result, requiring no condensed-matter input beyond the identification
of the spin state.

Experimental status

Selection Rule 1 is consistent with prior null reports
from Tajmar [15] for YBCO and BSCCO at 77 K, and
from Chiao [16] for YBCO—both d-wave, spin-singlet
materials. These experiments differ in method and precision from Tate’s London-moment measurement, so the
comparison is qualitative rather than a direct replication
of the Tate observable. Selection Rule 2 predicts a null for
any candidate spin-triplet superconductor; this has not
yet been tested. Neither selection rule is predicted by
Lipavský [11], whose mechanism has no representationtheoretic content and does not address pairing symmetry.

RESULT II: PAIR-ONLY EXCHANGE CHANNEL

(Mechanism conjecture)
In a conventional BCS superconductor, both electrons
in a Cooper pair occupy generation 1. The pair’s microsector state is |00⟩ ∈ S 2 (V ∗ ), which decomposes as
q
|00⟩ = √13 |1⟩ + 23 |5⟩ .
(9)
The democratic singlet |1⟩ = √13 (|00⟩ + |11⟩ + |22⟩) is
generation-blind and carries no exchange residual beyond
tree level. A single uncorrelated electron occupies only

3
one generation direction and has zero projection onto the
quintet (which requires a two-particle state to exist).
The quintet component, with weight 2/3, is the paironly exchange channel: it is accessible to Cooper pairs
but not to single electrons. Any operator coupling
through the 5 of S 2 (V ∗ ) produces a signal for s-wave
pairs that is absent for isolated electrons.
The natural scale of this coupling is set by the ψ–EM
vertex structure: one factor of α from the vertex, one
from the loop, giving O(α2 ) ∼ 5.3 × 10−5 , i.e., of order
50–100 ppm. Tate’s anomaly at 92±21 ppm falls squarely
in this range.
We note what this does not establish. The map from
the finite Yukawa operator (acting on C[A5 ]) to the
London-moment observable (measured by a SQUID on
a rotating ring) requires an auxiliary bridge connecting
the microsector pair state to the constitutive mass m∗ in
B = −(2m∗ /e∗ )ω. This bridge is physically motivated
but not yet theorem-grade.

RESULT III: COEFFICIENT

(Numerical conjecture)
We conjecture that the anomalous mass correction for
s-wave Cooper pairs is
δ=

√

3 α2 = 92.23 ppm

(10)

√
p
with 3 = Ngen and α−1 = 137.035 999 084.
The coefficient arises from three factors:
(i) ψ–EM vertex : α.
(ii) Coherence-enhanced loop: α (with the 1/(2π)
angular-averaging suppression of the free-electron
Schwinger diagram lifted by the macroscopic phase
coherence of the s-wave condensate, which locks all
angular channels to the same macroscopic phase via the
anomalous propagator). p
√
(iii) Generation factor : Ngen = 3 (all three generation channels contribute, with topologically fixed phases
adding incoherently in amplitude).
The match to Eq. (2) is 0.01σ.
We assign this result the status of numerical conjecture for three reasons. First, the coherence-lifting argument (replacing 1/(2π) with 1) is physically motivated
by the off-diagonal long-range order of the BCS ground
state but has not been derived from a controlled diagrammatic
pcalculation within the DFD framework. Second,
the Ngen factor assumes incoherent amplitude addition of generation channels, which is plausible but unproven. Third, exploratory numerical scans of the full
60-dimensional C[A5 ] group algebra
yield coefficients in
√
the range 1.75–1.78 (close to 3 ≈ 1.732) for specific
operator assignments, but these depend on the choice of
eigenbasis within the quintet subspace and are not yet
basis-independent.

The coefficient involves no continuous free parameters
once the A5 auxiliary closure is adopted. The discrete
structural choices (generation assignment, operator path
on the Cayley graph) are constrained by the microsector
framework but not uniquely fixed by the core DFD field
equations alone.

EXPERIMENTAL DISCRIMINATION

The sharpest test distinguishing this framework from
Lipavský [11] is universality.
Lipavský’s BCS-exchange correction enters through
the work function and pairing strength, both of which
vary across materials (Table I). The gap ratio ∆/EF
spans nearly a factor of 20 from Al to Nb. If the anomaly
tracks ∆/EF , Lipavský is confirmed and DFD is falsified.
If the anomaly is the same (≈ 92 ppm) for all six materials, DFD survives.
The decisive experiment is a multi-material Londonmoment measurement at ≲ 20 ppm precision. Tate’s
1989 measurement of niobium [3, 4] remains the only precision determination; it has never been replicated or extended to other materials. Modern SQUID magnetometry should permit sub-ppm accuracy [17], though no such
measurement has yet been realized.
Additional predictions (Table II):
(i) d-wave null : δ = 0 for all d-wave spin-singlet superconductors, consistent with prior null reports [15, 16].
(ii) p-wave null : δ = 0 for spin-triplet superconductors
by representation orthogonality. Untested.
(iii) Clock test: An optical lattice clock at radius r
inside a rotating Nb ring sees δf /f ∼ 2δ ω r α/(2c) ∼
8 × 10−15 at ω = 100 rad/s, r = 3.6 cm—above current
Sr clock sensitivity [19].
(iv) Equivalence principle: Ross et al. [20] bound the
Cooper-pair Eötvös parameter to ηCP ≤ 9.2 × 10−4 . The
DFD prediction δ ≈ 9.2 × 10−5 is within reach of a oneorder-of-magnitude improvement.

TABLE I. Superconducting gap ∆ and Fermi energy EF for
six type-I superconductors. The framework predicts the same
δ for all; Lipavský’s mechanism predicts δ varying with ∆/EF .
Material
Nb
Pb
Sn
In
Al
Hg

∆ (meV)
1.55
1.35
0.59
0.54
0.17
0.82

EF (eV)
5.32
9.47
10.2
8.63
11.7
7.13

∆/EF
2.9 × 10−4
1.4 × 10−4
0.6 × 10−4
0.6 × 10−4
0.15 × 10−4
1.2 × 10−4

4
TABLE II. Selection rule predictions by pairing symmetry.
Pairing
s-wave singlet
d-wave singlet
p-wave triplet

Example
Nb, Pb, Al
YBCO, BSCCO
(candidates)

Mechanism
Quintet channel
Angular cancel.
Λ2 orthog.

δ
O(α2 )
0
0

DISCUSSION

Table III summarizes the comparison. The unique
contribution of this work is the pair of selection rules:
a sharp, parameter-free distinction between s-wave, dwave, and p-wave materials. These results survive independently of the numerical coefficient.
An open question is the relationship between Lipavský’s “Pauli exchange” and our “quintet exchange
channel.” Both identify exchange processes within the
condensate as the physical origin. They may describe the
same physics in different formalisms. If so, the DFD contribution is to explain why the exchange correction takes
its magnitude (group theory) and why certain pairing
symmetries give zero (angular cancellation and representation orthogonality). Computing Lipavský’s correction
explicitly for multiple materials would resolve this.
We stress that Eq. (1) is a single measurement from
1989, at 21 ppm accuracy, that
√ has never been replicated.
The 0.01σ agreement with 3 α2 is striking but constitutes motivation for replication, not confirmation.
The principal theoretical gap is the auxiliary bridge
connecting the A5 pair-space operator to the Londonmoment observable: the map from the finite Yukawa matrix element ⟨χR |Yfinite |χL ⟩ acting on C[A5 ] to the constitutive mass m∗ in the London equation. Closing this
bridge would elevate the mechanism conjecture to a theorem.
The author thanks J. Tate and B. Cabrera for
the foundational measurement, M. Tajmar for systematic experimental follow-ups that clarified the pairingsymmetry phenomenology, P. Lipavský for the BCS-

TABLE III. Comparison of theoretical approaches. “Input”
means δTate was used to fix a parameter.
Theory
Tajmar [7]
Lipavský [11]
de Matos [10]
This work
Sel. rules
Coefficient

Prediction
(ppm)
92 (input)
∼92
92 (input)

Material
indep.?
No
No
No

Free
params
1
≥1
1

Selection
rules?
No
No
No

0 (d/p)
92.23∗

Yes
Yes

0
0†

Yes
—

∗ Numerical conjecture. † No continuous free parameters once

auxiliary closure is adopted; see text.

exchange analysis that sharpened the universality question, and colleagues whose critical feedback improved this
manuscript.

[1] F. London, Superfluids (Wiley, New York, 1950), Vol. 1.
[2] A. F. Hildebrandt, Phys. Rev. Lett. 12, 190 (1964).
[3] J. Tate, B. Cabrera, S. B. Felch, and J. T. Anderson,
Phys. Rev. Lett. 62, 845 (1989).
[4] J. Tate, S. B. Felch, and B. Cabrera, Phys. Rev. B 42,
7885 (1990).
[5] R. M. Brady, J. Low Temp. Phys. 49, 1 (1982).
[6] J. Anandan, Phys. Lett. A 105, 280 (1984).
[7] M. Tajmar and C. J. de Matos, Physica C 385, 551
(2003); AIP Conf. Proc. 813, 1415 (2006).
[8] M. Tajmar, Supercond. Sci. Technol. 24, 125011 (2011).
[9] R. D. Graham, R. B. Hurst, R. J. Thirkettle, C. H. Rowe,
and P. H. Butler, Physica C 468, 383 (2008).
[10] C. J. de Matos, Adv. Astron. 2009, 931920 (2009).
[11] P. Lipavský, Physica C 528, 108 (2016).
[12] G. Alcock, “Density Field Dynamics: A Unified Theory,”
v3.2, Zenodo (2026); DOI:10.5281/zenodo.19029160.
[13] J. Schwinger, Phys. Rev. 73, 416 (1948).
[14] C. C. Tsuei and J. R. Kirtley, Rev. Mod. Phys. 72, 969
(2000).
[15] M. Tajmar, F. Plesescu, B. Seifert, R. Schnitzer, and
I. Vasiljevich, J. Phys. Conf. Ser. 150, 032101 (2009).
[16] R. Y. Chiao, W. J. Fitelson, and A. D. Speliotopoulos,
arXiv:gr-qc/0304026 (2003).
[17] L. P. Hoang et al., Mater. Lett. 262, 127176 (2020).
[18] M. Tajmar, O. Neunzig, and M. Kößling, Front. Phys.
10, 892215 (2022).
[19] T. Bothwell et al., Nature 602, 420 (2022).
[20] M. P. Ross et al., arXiv:2407.21232 (2024).
[21] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys.
Rev. 108, 1175 (1957).
[22] B. S. DeWitt, Phys. Rev. Lett. 16, 1092 (1966).

