---
source_pdf: Composition_Dependent_Bounds_on_Scalar_Field_Couplingto_Nuclear_Decay_Rates__4_.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Composition-Dependent Bounds on Scalar-Field Coupling
to Nuclear Decay Rates
Gary Alcock1, ∗
1

Independent Researcher, Los Angeles, California, USA
(Dated: March 19, 2026)

Scalar-tensor theories of gravity generically predict composition-dependent coupling of a gravitational scalar field to nuclear transition rates. We apply the Flambaum nuclear sensitivity formalism
(I)
to compute isotope-specific sensitivity coefficients κq for eight nuclides central to the decade-long
debate over reported annual modulations in decay rates. The sensitivity is driven by Q-value through
κq ∝ n/Q, placing 32 Si (Q = 0.227 MeV) at the top of the hierarchy. We show that existing null
results constrain different regions of the (kqeff , κq ) parameter space and do not exclude compositiondependent signals in untested low-Q isotopes. The classic positive datasets (32 Si at BNL, 226 Ra
at PTB) are now understood to be dominated by environmental systematics—particularly humidity and temperature—and cannot be treated as detections. We identify 187 Re (Q = 2.63 keV,
κq ≈ 19,000) and the 229 Th nuclear clock isomer (K ∼ 104 ) as the most sensitive future targets, and
propose a multi-isotope ratio test that eliminates environmental systematics while directly probing
composition dependence. For the highest-sensitivity low-Q isotopes, the question of whether nuclear decay rates couple to gravitational environment at the 10−6 –10−7 level remains experimentally
open.

I.

INTRODUCTION

Between 2008 and 2012, Jenkins, Fischbach, and collaborators reported annual modulations in nuclear decay rates correlated with the Earth–Sun distance [1, 2,
4, 5]. The primary datasets—the 32 Si/36 Cl ratio at
Brookhaven National Laboratory (BNL) [12] and the
226
Ra/152 Eu ratio at the Physikalisch-Technische Bundesanstalt (PTB) [13]—showed ∼ 0.1% annual modulations.
These claims have been extensively challenged.
Pommé et al. [8] compiled data from 14 laboratories,
finding no solar-phase oscillations at 10−6 –10−5 precision across multiple isotopes. Bellotti et al. [9] constrained 137 Cs modulations below 5×10−5 at Gran Sasso.
Cooper [6] found no anomaly in 238 Pu aboard Cassini.
Hardy et al. [7] set a ±0.02% limit on 198 Au. Most damagingly, Pommé et al. [10] showed that the original BNL
32
Si and Ohio State 36 Cl datasets correlate better with local dew point and temperature than with the Earth–Sun
distance, identifying humidity-driven instrumental instability as the likely cause of the reported modulations.
The standard conclusion is that the Jenkins–Fischbach
effect is an experimental artifact [8, 10]. We do not dispute this for the claimed ∼ 10−3 amplitudes. However,
we note that the experimental program that “disproved”
the effect tested different isotopes from those originally
claimed, and the null bounds span a wide range (10−6 to
10−4 ) depending on isotope and technique. Scalar-tensor
theories generically predict composition-dependent coupling [17, 18], in which different isotopes have different
sensitivity to a gravitational scalar field. In such a framework, a null for isotope A does not constrain isotope B.

∗ gary@gtacompanies.com

The purpose of this paper is not to resurrect the
Jenkins–Fischbach claims. It is to develop a quantitative framework for computing isotope-specific nuclear
sensitivity coefficients, to map existing null results onto
the resulting parameter space, and to identify the most
sensitive targets for future measurements that could
detect—or definitively exclude—composition-dependent
scalar coupling to nuclear decay rates at the 10−6 –10−7
level.

II.
A.

THEORETICAL FRAMEWORK

Scalar-field coupling to fundamental constants

We work within a scalar-field framework in which a
gravitational potential ψ couples to fundamental constants through distinct Standard Model channels [15, 17,
18]:
δα
= kα δψ,
α

δXq
= kq δψ,
Xq

(1)

where α is the fine-structure constant, Xq ≡ mq /ΛQCD ,
and kα , kq are channel coupling constants. Compositiondependent coupling is a generic feature of scalar-tensor
theories [17, 18], but the numerical values of kα and
kq are model-dependent. As a concrete benchmark we
adopt DFD values [15]: kα = α2 /(2π) ≈ 8.5 × 10−6 and
kq = αs2 /(2π) ≈ 0.035 (with αs = 0.47). In the bounds
analysis below, kq is treated as a free parameter; the
benchmark serves only to define a target sensitivity for
future experiments. For Earth’s annual orbit, the solar
potential variation is


1
GM⊙
1
|∆ψ⊙ | =
−
= 3.30 × 10−10 , (2)
c2
rperi
raph

2

Nuclear Sensitivity Ranking

numerically identical to |∆Φ⊙ /c2 | used in LPI tests [16].

32Si

Nuclear sensitivity coefficients

(I)

(3)

(I)

where κα and κq encode the nuclear-physics sensitivity. Following Flambaum and collaborators [19–21]:
a. Beta decay. For a transition with Q-value Q and
phase-space power n (n = 5 allowed, n = 7 firstforbidden, n = 9 second-forbidden),
κ(β)
=n
q

δEr
,
Q

SENSITIVITY RANKING AND EXISTING
BOUNDS

Table I presents computed sensitivity coefficients for
all eight isotopes in the experimental record. Figure 1
shows the ranking graphically. Figure 2 displays the Qvalue correlation.

A.

77

238Pu

51
51
36
28
15

226Ra
198Au
36Cl
54Mn

0

What the bounds constrain

The critical observation is that existing null results
constrain different regions of the sensitivity parameter
space. We define an effective coupling kqeff ≡ kq × fenh ,
where fenh ≥ 1 absorbs any nuclear resonance enhancement beyond the generic Flambaum estimate δEr ≈
10 MeV. An experimental upper limit (δλ/λ)max on iso(I)
tope I constrains kqeff < (δλ/λ)max /(κq |∆ψ⊙ |). The
existing bounds give:

Signal reported
Null result
100

200

300

q (strong-channel sensitivity)

(4)

where δEr ≈ 10 MeV is Flambaum’s estimate for a
generic nuclear level shift per unit δXq /Xq [19]. The
(β)
electromagnetic sensitivity is κα = n |∆EC |/Q, where
∆EC is the parent–daughter Coulomb energy difference.
The 1/Q dependence is the key structural prediction:
low-Q transitions are dramatically more sensitive. This
is the same near-degeneracy mechanism that makes the
229
Th isomer (8.4 eV) sensitive at the 104 level [22]
and the 150 Sm compound resonance (0.1 eV) sensitive
at 108 [19].
b. Alpha decay. The Gamow penetration factor
(α)
(α)
gives κα = 2πη and κq = 2πη δEr /VB , where η is
the Sommerfeld parameter and VB ≈ 30 MeV the barrier
height.
These estimates carry systematic uncertainties of a factor ∼ 2–3 from nuclear matrix elements not captured by
the simple Q-value scaling.

III.

128

137Cs

The fractional change in decay rate λI is

δλI
(I)
= KI δψ = kα κ(I)
δψ,
α + kq κq
λI

308

90Sr

FIG. 1. Strong-channel sensitivity κq for all eight isotopes.
The ranking is driven by Q-value. Note that no isotope
with κq > 100 has been measured with environmentallycontrolled modern apparatus at < 10−5 sensitivity. The
highest-sensitivity isotope in the experimental record (32 Si)
was measured with 1980s gas-counting technology in an uncontrolled environment [10, 12].

q (strong-channel sensitivity)

B.

Q-value Drives Sensitivity
32Si

300
Signal ( /EC)
Signal ( )
Null ( /EC)
Null ( )
238
226Ra Pu

200
137Cs
90Sr
36Cl
54Mn

100
0

0

198Au

2

4

Q-value (MeV)

6

FIG. 2. Strong-channel sensitivity κq versus Q-value. Circles: β − /EC; squares: α. The dashed curve shows κq = 7 ×
10 MeV/Q. The tightest null bounds (Gran Sasso 137 Cs, PTB
90
Sr) probe intermediate-sensitivity isotopes; the highestsensitivity region (Q < 0.3 MeV) remains unexplored with
modern techniques.

• The Gran Sasso 137 Cs bound (< 5 × 10−5 at κq =
77) constrains kqeff < 2 × 103 .
• The PTB 90 Sr bound (< 8 × 10−5 at κq = 128)
constrains kqeff < 2 × 103 .

3
TABLE I. Nuclear sensitivity coefficients and existing experimental bounds. The predicted modulation δλ/λ = KI |∆ψ⊙ |
uses kα = 8.5 × 10−6 and kq = 0.035 as a DFD-motivated benchmark (not a generic scalar-tensor prediction; see text).
Experimental bounds are upper limits from the references cited; the 32 Si and 226 Ra entries list the claimed amplitudes, which
are now attributed to environmental systematics [10, 11].
Isotope
32
Si
90
Sr
137
Cs
226
Ra
238
Pu
198
Au
36
Cl
54
Mn

Decay type
β − , 1st forb. uniq.
β − , 1st forb. uniq.
β − , 2nd forbidden
α
α
β − , allowed
β − , 2nd forbidden
EC, allowed

Q (MeV)
0.227
0.546
1.176
4.871
5.593
1.372
0.709
1.377

κq
308
128
77
51
51
36
28
15

Baseline δλ/λ
3.6 × 10−9
1.5 × 10−9
8.9 × 10−10
5.9 × 10−10
5.9 × 10−10
4.2 × 10−10
3.3 × 10−10
1.7 × 10−10

Expt. bound
∼ 10−3 (syst.)†
< 8 × 10−5
< 5 × 10−5
∼ 10−3 (syst.)†
< 3 × 10−4
< 2 × 10−4
∼ 5 × 10−4 (syst.)†
Not bounded‡

Status
Artifact
Null
Null
Artifact
Null
Null
Artifact
Open

Source
[10]
[8]
[9]
[10]
[6]
[7]
[10]
[2]

† Claimed detection, now attributed to humidity/temperature systematics by Pommé et al. [10, 11].
‡ The 54 Mn flare-precursor claim [2] is a single event; later searches found no flare–decay correlation for other isotopes [3]. Not a robust

bound.

• The Cassini 238 Pu bound (< 3 × 10−4 at κq = 51)
constrains kqeff < 2 × 104 .
None of these constrain kqeff below ∼ 103 . A measurement
of 32 Si (κq = 308) at 10−6 would constrain kqeff < 10,
pushing into the theoretically interesting regime for the
first time. A measurement of 187 Re (κq ≈ 19,000) at
10−6 would constrain kqeff < 0.2—directly probing the
benchmark coupling scale adopted in this framework.

B.

The status of the original positive claims

The original BNL 32 Si and Ohio State 36 Cl datasets,
which launched the entire debate, are now understood to
be contaminated by environmental systematics. Pommé
et al. [10] showed that the 32 Si decay rate variations inversely correlate with dew point at a nearby weather
station, and that similar humidity-driven effects explain
the 36 Cl data. Pommé and Pelczar [11] extended this
analysis to 90 Sr/90 Y and 60 Co, finding humidity correlations in those datasets as well. The PTB 226 Ra
data were originally ratioed against 152 Eu, a technique
that Schrader [14] showed is sensitive to measurementtechnique choices.
We therefore treat the original ∼ 10−3 claims as artifacts. The question we address is not whether those
specific signals were real, but whether compositiondependent scalar coupling at the 10−6 –10−7 level—below
all existing bounds—could exist and how it would be detected.

IV.

QUALITATIVE FEATURES OF SCALAR
COUPLING

If a scalar-field coupling to nuclear decay rates exists
at any level, several qualitative features follow from the

framework:
1. Phase: Maximum rate at perihelion (deepest ψ).
This is a generic prediction of any solar-potential
coupling.
2. Periodicity: Annual from 1/r⊕-⊙ . Sub-annual periodicities (e.g., 33-day) would require asphericity
in the solar mass distribution, which is speculative.
3. Composition dependence: Different isotopes
(I)
(I)
couple differently through KI = kα κα + kq κq .
This is the central testable prediction and has not
been directly probed.
4. Scalar mechanism: The coupling proceeds
through ψ, not through neutrinos. This resolves
the mechanistic difficulties of the original neutrino
hypothesis [1].
We note that the 33-day periodicity claimed by Sturrock et al. [5] and the 54 Mn flare-precursor event [2] are
suggestive but not established. Later searches found no
correlation between major solar flares and decay rates
in monitored isotopes [3], and the 33-day signal in the
BNL data may be an artifact of the same environmental
contamination that produces the annual modulation [10].
We do not treat these as confirmed features.
V.

THE AMPLITUDE LANDSCAPE

Figure 3 shows the amplitude landscape. Three
regimes are relevant:
Above 10−4 : Excluded for all tested isotopes. The
original ∼ 10−3 claims are environmental artifacts [10].
10−5 –10−4 : Excluded for 137 Cs, 90 Sr, and 198 Au. Not
excluded for 32 Si, 36 Cl, or any isotope with κq > 200,
because these have never been measured with adequate
environmental control at this sensitivity.

4

Amplitude Gap: Three Scenarios
Jenkins claimed
(32Si, 226Ra)
Pommé upper limits
(14 labs)
DFD + enhancement
(resonance × 100)
DFD baseline
(kq = s2/2 )

10

8

6

4

log10 [ / ]

2

0

FIG. 3. Amplitude landscape for annual decay-rate modulation. Red: original Jenkins claims (now attributed to systematics). Orange: tightest existing null bounds (Pommé,
Gran Sasso). Blue: baseline scalar-coupling prediction with
kq = αs2 /(2π). Green: prediction with nuclear resonance enhancement (×100). The experimentally unexplored window
between 10−7 and 10−5 is where a composition-dependent signal could reside.

Below 10−5 : Unexplored for all isotopes in the
dataset. This is the regime where baseline scalarcoupling predictions (10−9 –10−7 ) and modestly enhanced predictions (10−7 –10−5 ) reside.
The key point is that the highest-sensitivity isotopes
(32 Si, 90 Sr) have never been measured at the 10−6
level with modern environmentally-controlled apparatus. The tightest bounds come from intermediatesensitivity isotopes (137 Cs, 198 Au). The parameter space
for composition-dependent coupling in low-Q transitions
at amplitudes below current isotope-specific bounds remains open.

VI.

CONNECTION TO ATOMIC CLOCK TESTS

The same multi-channel coupling structure applies at
the atomic scale. Atomic clock comparisons searching
for annual modulation of frequency ratios in the solar
gravitational potential constrain the coupling constants
kα and kc (composition-dependent) [16].
The most stringent constraint on α-coupling to gravity comes from the PTB Yb+ E3/E2 measurement by
Filzinger et al. [27], who searched for oscillations in the
E3/E2 frequency ratio at periods set by ultralight dark
matter candidates and also improved limits on coupling
of α to gravitational potential. From their long-term

E3/E2 dataset they report c2 α−1 dα/dΦ = (−2.4±3.0)×
10−9 , corresponding to |kα | ≲ 5 × 10−9 at 2σ. Because
both transitions occur in the same ion, compositiondependent effects cancel, making this a clean probe of
the α-channel alone.
Cross-species comparisons (e.g., Cs/Sr, H/Cs) probe
a different combination of couplings: kα ∆κα + kc ∆C.
If composition-dependent coupling exists, it would appear in cross-species ratios but vanish in same-ion
comparisons—a distinctive pattern. The Cs/Sr channel,
with ∆κα = 2.77 [25, 26], offers the largest α-lever arm
among operational clock pairs and has not been searched
for annual solar-potential modulation at the required sensitivity.
This establishes a structural parallel: the nuclear sen(I)
sitivity hierarchy (κq varying by isotope) mirrors the
(i)
atomic sensitivity hierarchy (κα varying by species).
Both predict composition dependence as the distinguishing signature. We include this discussion not because
the atomic-clock bounds enter the nuclear-sector derivation, but because the same coupling structure and the
same annual ∆ψ⊙ connect the two sectors, and progress
in either informs the other.
VII.

DECISIVE FUTURE TESTS

We identify five measurements that would either detect
or definitively constrain composition-dependent scalar
coupling at the benchmark scale:
1. 187 Re (Q = 2.64 keV [24], β − , t1/2 = 4.12 ×
1010 yr [24]): The lowest Q-value of any known
β emitter gives κq ≈ 19,000. A half-life measurement at fractional precision 10−6 , repeated at
different orbital phases, would constrain kqeff <
0.2—directly probing the theoretically interesting
regime. The long half-life makes direct counting impractical, but calorimetric techniques (as developed for KATRIN-type experiments) or massspectrometric approaches may be feasible.
2. 229 Th nuclear clock: The 8.4 eV isomeric transition achieves Flambaum’s enhancement K ∼
104 [22]. Recent observation of the radiative decay [23] and ongoing efforts toward direct laser excitation make this platform increasingly realistic.
Once operational at 10−18 fractional precision, it
constrains kq to ∼ 10−4 , four orders of magnitude
beyond any existing nuclear-sector bound.
3. 32 Si remeasurement: Repeating the BNL measurement with modern pulse-counting apparatus in
a temperature- and humidity-controlled environment at 10−6 sensitivity. This directly addresses
the Pommé critique [10]: if the modulation persists
when environmental systematics are eliminated, it
is physical; if it vanishes, the debate is closed for
this isotope.

5
4. Multi-isotope ratio test: Simultaneously monitoring two isotopes with different κq in the same
detector or facility. The ratio of any annual modulations should equal KA /KB if the coupling is real,
and zero if both signals are environmental artifacts
(which affect both equally). This eliminates systematics by design and directly probes composition
dependence.

229

5. Cross-species atomic clock campaign: A dedicated search for annual modulation of the Cs/Sr
or Rb/Sr frequency ratio over a full orbital cycle, analyzed specifically for solar-potential correlation. A detection would establish the compositiondependent coupling at the atomic scale; a null
at the 10−6 level constrains kc ∆C below existing
bounds.

The decade-long debate over solar-modulated nuclear
decay rates has been largely settled at the phenomenological level: the original ∼ 10−3 signals are almost certainly
environmental artifacts. But the theoretical question—
whether nuclear decay rates couple to gravitational environment through composition-dependent scalar fields—
remains open for the highest-sensitivity low-Q isotopes
at amplitudes below current isotope-specific bounds, because the experimental program that closed the debate
tested different isotopes at sensitivities (10−5 –10−4 ) that
do not probe the benchmark coupling scale (10−7 –10−6 )
in the most sensitive transitions.
The Flambaum nuclear sensitivity formalism provides
a rigorous hierarchy: κq ∝ n/Q, with 32 Si, 187 Re, and
229
Th at the top. The decisive next step is not to
reanalyze old data, but to perform new measurements
of the highest-sensitivity isotopes with environmentallycontrolled modern apparatus. The multi-isotope ratio
test we propose eliminates systematics by design and directly probes the composition-dependent signature that
distinguishes scalar coupling from environmental contamination.
If the coupling exists at the benchmark scale, the 229 Th
nuclear clock will find it. If it does not, the same measurements will set the most stringent bounds on scalarfield coupling to nuclear structure ever achieved. Either
outcome advances fundamental physics.

VIII.
A.

DISCUSSION

What is and is not claimed

We do not claim that the original Jenkins–Fischbach
signals are real. The Pommé dew-point analysis [10, 11]
provides a compelling environmental explanation for the
BNL and Ohio State datasets, and the PTB data are
similarly suspect [14].
What we do claim is: (i) Scalar-tensor theories predict composition-dependent coupling as a generic feature, not a special case. (ii) The Flambaum formalism
provides a quantitative hierarchy of nuclear sensitivities
driven by Q-value. (iii) Existing null results constrain
intermediate-sensitivity isotopes but leave the highestsensitivity region (κq > 200) unexplored at better than
10−4 . (iv) Specific future measurements (187 Re, 229 Th,
32
Si remeasurement, multi-isotope ratio) can probe the
benchmark coupling scale for the first time.

Th nuclear clock shows no anomalous annual shift at
10−18 precision. Individually, each null constrains kqeff ;
collectively, they would exclude composition-dependent
coupling at the benchmark scale and below.

IX.

CONCLUSION

ACKNOWLEDGMENTS
B.

Falsification criteria

The framework of composition-dependent scalar coupling to nuclear decay rates is falsified if: (a) 32 Si shows
no modulation at 10−6 sensitivity with modern apparatus, and (b) 187 Re shows no effect at 10−6 , and (c) the

We acknowledge V. V. Flambaum for the nuclear sensitivity framework upon which the isotope-specific calculations rely, J. H. Jenkins and E. Fischbach for identifying
the anomaly that motivated this analysis, and S. Pommé
and collaborators for the rigorous environmental reanalyses that clarified the status of the original datasets.

[1] J. H. Jenkins et al., Astropart. Phys. 32, 42 (2009).
[2] J. H. Jenkins et al., Astropart. Phys. 37, 81 (2012).
[3] J. H. Jenkins et al., Astropart. Phys. 31, 407 (2009).
[4] E. Fischbach et al., Space Sci. Rev. 145, 285 (2009).
[5] P. A. Sturrock et al., Astropart. Phys. 34, 121 (2010).
[6] P. S. Cooper, Astropart. Phys. 31, 267 (2009).
[7] J. C. Hardy et al., Appl. Radiat. Isot. 70, 1975 (2012).
[8] S. Pommé et al., Phys. Lett. B 761, 281 (2016).
[9] E. Bellotti et al., Phys. Lett. B 720, 116 (2013).

[10] S. Pommé, K. Pelczar, K. Kossert, and I. Kajan, Sci.
Rep. 11, 16002 (2021).
[11] S. Pommé and K. Pelczar, Sci. Rep. 12, 9535 (2022).
[12] D. E. Alburger, G. Harbottle, and E. F. Norton, Earth
Planet. Sci. Lett. 78, 168 (1986).
[13] H. Siegert, H. Schrader, and U. Schötzig, Appl. Radiat.
Isot. 49, 1397 (1998).
[14] H. Schrader, Appl. Radiat. Isot. 68, 1583 (2010).
[15] G. Alcock, Zenodo (2025), doi:10.5281/zenodo.19029160.

6
[16] C. M. Will, Living Rev. Relativ. 17, 4 (2014).
[17] T. Damour and J. F. Donoghue, Phys. Rev. D 82, 084033
(2010).
[18] T. Damour, Class. Quantum Grav. 29, 184001 (2012).
[19] V. V. Flambaum and E. V. Shuryak, Phys. Rev. D 65,
103503 (2002).
[20] V. V. Flambaum and A. F. Tedesco, Phys. Rev. C 73,
055501 (2006).
[21] V. V. Flambaum and R. B. Wiringa, Phys. Rev. C 76,
054002 (2007).

[22] V. V. Flambaum, Phys. Rev. Lett. 97, 092502 (2006).
[23] S. Kraemer et al., Nature 617, 706 (2023).
[24] M. Galeazzi et al., “The electron end-point energy of
187
Re,” Phys. Rev. C 63, 014302 (2001); see also KAERI
Nuclear Data, https://atom.kaeri.re.kr.
[25] V. A. Dzuba, V. V. Flambaum, and J. K. Webb, Phys.
Rev. A 59, 230 (1999).
[26] E. J. Angstmann, V. A. Dzuba, and V. V. Flambaum,
Phys. Rev. A 70, 014102 (2004).
[27] M. Filzinger et al., Phys. Rev. Lett. 130, 253001 (2023).

