---
source_pdf: Matter_Wave_Interferometry_Tests_of_Density_Field_Dynamics.pdf
title: "Matter-Wave Interferometry Tests of Density Field Dynamics"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Matter-Wave Interferometry Tests of Density Field Dynamics
Gary Alcock1
1

Independent Researcher, Los Angeles, CA, USA
(Dated: September 18, 2025)

Density Field Dynamics (DFD) posits a scalar refractive field ψ(x) such that light propagates
2
with n = eψ (one-way phase speed c1 = ce−ψ ) and matter accelerates as a = c2 ∇ψ. While our
cavity–atom redshift test probes the photon sector, matter-wave interferometers test the external
wavefunction coupling. We derive the perturbative phase from the ∇ψ ·∇ operator in the DFDmodified Schrödinger equation and obtain a clean discriminator for light-pulse interferometers:
∆ϕDFD =

2
ℏ keff
g 3
T ,
m c2

in contrast to the standard GR scaling ∆ϕGR = keff gT 2 . We provide explicit, plug-in predictions for
Kasevich–Chu, Raman, and Bragg geometries (vertical and horizontal), source-mass configurations,
and dual-species protocols (Rb/Yb), and we analyze systematics with look-alike time scalings. For
Earth g and keff ∼ 1.6 × 107 m−1 (Rb, 780 nm), the DFD residual is ∼ 2 × 10−11 rad at T = 1 s, within
the reach of current long-baseline instruments when using rotation, k-reversal, and source-mass
modulation.
I.

INTRODUCTION

Atom interferometers are leading probes of gravity, redshift, and fundamental symmetries.[1–6] In DFD, photons
follow the eikonal of an optical metric with n = eψ while
2
matter sees the conservative potential Φ = − c2 ψ.1 The
photon-sector discriminator is a co-located cavity–atom
redshift comparison across altitude; here we develop the
matter-sector analogue: light-pulse atom interferometry.
The novelty is a gradient–gradient coupling that yields a
T 3 scaling distinct from the GR T 2 law, giving a route
to sector-resolved falsification with existing facilities.
Relation to existing gravity-gradient cancellation and
why it was not seen. Long-baseline experiments actively suppress or calibrate out cubic-in-T gravitygradient contributions using frequency-shift gravitygradient (FSGG) compensation or closely related k-vector
tuning schemes,[27–30] because within GR such terms
are treated as systematics. As a result, published analyses
typically (i) operate at fixed T for the headline measurement, (ii) do not report a residual vs. T regression with
the even-in-keff , rotation-odd discriminator posed here,
and (iii) use k-reversal specifically to cancel odd-in-keff
laser/systematic terms. To our knowledge, no experiment
has isolated a coefficient beven in ϕres (T ) = aT 2 + beven T 3
that (a) is even under keff → −keff and (b) flips sign under 180◦ rotation of a horizontal baseline—the specific
signature predicted here.

1 See the Einstein 1911–12 completion and the strong-field/GW

manuscripts for the action, normalization, and recovery of GR’s
weak-field coefficients; we adopt that notation here.

II.

THEORY: ψ-COUPLING IN THE
SCHRÖDINGER DYNAMICS

To first order in weak fields (|ψ| ≪ 1), the nonrelativistic equation for mass m reads (expanding e−ψ ≈ 1 − ψ)
iℏ ∂t Ψ = −

i
ℏ2 h
ℏ2 2
∇ Ψ + mΦ Ψ +
ψ ∇2 Ψ + (∇ψ)·∇Ψ ,
2m
2m
(1)
2

2

p
with Φ ≡ − c2 ψ. Treat H = H0 +δH with H0 = 2m
+mΦ
and

δH =

i
ℏ2 h
ψ ∇2 + (∇ψ)·∇ .
2m

(2)

Evaluate the small phase along the unperturbed classical
branches A, B:
1
∆ϕDFD =
ℏ

Z 2T



dt ⟨δH⟩A − ⟨δH⟩B .

(3)

0

The operator (∇ψ)·∇ acting on a locally plane-wave factor
on each branch pulls down the instantaneous momentum,
⟨(∇ψ)·∇⟩ → i (∇ψ)·p/ℏ, so that

∆ϕ∇ψ = −

1
2m

Z 2T
dt (∇ψ)·∆p(t) .

(4)

0

In uniform Earth gravity, ∇ψ = −2g/c2 ; the constant
part cancels between arms unless one accounts for the
finite spatial separation of the arms induced by the light
pulses. Keeping the leading variation sampled at the arm
positions yields the T 3 law below.

2
III.

LIGHT-PULSE GEOMETRIES AND THE T 3
DISCRIMINATOR

Consider a vertical Kasevich–Chu sequence (π/2–π–π/2
at t = {0, T, 2T }) with effective Raman wavevector keff ẑ.
Let the recoil velocity be vr = ℏkeff /m. Between pulses,
the branch momentum difference is piecewise constant:
∆pz (t) = +ℏkeff for 0 < t < T , and −ℏkeff for T < t < 2T
(mirror swaps the arms). Using (4) with ∇ψ(rA,B , t) =
−2 g ẑ/c2 evaluated at the arm locations and expanding
to first order in the instantaneous arm separation ∆z(t)
(which is vr t on the first half and vr (2T −t) on the second),
the constant part cancels but the linear piece adds over
the two intervals, giving
∆ϕKasevich−−Chu
=
DFD

2
ℏ keff
keff vr g 3
g 3
T =
T . (5)
2
c
m c2

By contrast, the standard light-pulse phase from GR
(after the usual laser phase bookkeeping) is
∆ϕKasevich−−Chu
= keff g T 2 .
GR

C.

Dual-species protocol (Rb/Yb)

Because the DFD term scales as ∆ϕDFD =
2
(ℏkeff
/m) (g/c2 ) T 3 , the differential phase between two
species i, j operated in matched geometry is
!
2
2
keff,i
keff,j
g T3
(i−j)
.
(10)
−
∆ϕDFD = 2 ℏ
c
mi
mj
If both species share the same lattice/Bragg wavelength
(engineered co-propagating optics), keff,i = keff,j and (10)
reduces to a clean mass discriminator ∝ (1/mi − 1/mj ).
With independent Raman pairs (e.g. 87 Rb at 780 nm and
171
Yb at 556 nm), keep the explicit keff values; Eq. (10)
is then the quantity to regress against T 3 . In either case,
the GR common-mode keff gT 2 cancels under standard
k-reversal and conjugate-AI subtraction.

IV.

CONCRETE EXPERIMENTAL DESIGNS
(PLUG-AND-PLAY)

(6)

Design A (vertical Kasevich–Chu, 10 m fountain).
Species 87 Rb, λ = 780 nm, keff ≈ 1.6 × 107 m−1 , pulses
at t = {0, T, 2T } with T = 1–2 s. Arm apex separation
∆z
max ≈ vr T ∼ 1–2 cm.
(1.6 × 107 )(1.2 × 10−2 )(9.8)
Kasevich−−Chu
−11
∆ϕDFD
≈
≃ 2 × 10
rad.
∆ϕDFD ≈ 2 × 10−11 rad × (T /s)3 .
(3.0 × 108 )2
(7)
Design B (horizontal Bragg, L ∼ 1 m, rotation). Rotate the bench by 180◦ about ẑ to flip g· n̂. DFD flips
The absolute GR phase keff gT 2 ∼ 1.6×108 rad is removed
sign; many laser/system alignment systematics do not.
by chirp/common-mode subtraction; the residual DFD
Design C (tabletop source mass). Dither a 500 kg tungterm is what to search for, using scaling and sign tests
sten stack at R ∼ 0.25 m. Search at the dither frequency;
below.
scale with gs /c2 .
Numerics (Rb, 780 nm): keff ≃ 1.6 × 107 m−1 , vr =
ℏkeff /m ≈ 1.2 × 10−2 m s−1 . For T = 1 s,

A.

Horizontal baselines and rotation
V.

For a horizontal Raman/Bragg baseline with separation
direction n̂, Earth’s field projects as g· n̂:
2
ℏ keff
∆ϕhoriz
=
DFD

m

Key orthogonal signatures:
g· n̂ 3
T ,
c2

(8)

which flips sign under 180◦ rotation about the vertical.
This provides a powerful discriminator from many systematics.
B.

Source-mass configuration (tabletop)

2
gs 3
ℏ keff
T × G(geometry),
m c2

1. Time scaling: DFD ∝ T 3 vs. GR ∝ T 2 .
2. Orientation: rotation flips DFD (via g· n̂), many
systematics do not.
2
3. k-reversal: DFD ∝ keff
(even under keff → −keff );
laser-phase systematics change sign and cancel.

4. Recoil dependence: DFD ∝ vr ; separate from
gravity-gradient terms using velocity selection.

Place a dense source mass (e.g. ∼ 500 kg W) at distance
R producing gs = GM/R2 . Then
∆ϕsrc
DFD =

DISCRIMINANTS FROM GR AND
SYSTEMATICS CONTROL

(9)

where G encodes near-field placement; lock-in by modulating the mass.

5. Dual-species: residual ∝ (1/m1 −1/m2 ) or the full
2
keff
/m contrast in Eq. (10); GR null after commonmode rejection.
Systematics evidence and controls. Gravity-gradient
noise (GGN) from atmosphere and seismic fields sets
the long-baseline floor; recent characterizations provide

3
TABLE I. Systematics overview and kill-switches. The DFD signal alone shows T 3 scaling, rotation sign flip, and even parity
2
under k-reversal (∝ keff
).
Effect
DFD (target)
Gravity gradient Γ
Wavefront curvature / tilt
Vibrations (residual)
AC Stark / Zeeman
Laser phase (uncorrelated)

T -scaling
T3
T 2 /T 3 mix
T2
≈ T2
pulse-bounded
T2

high/low-noise models and motivate underground siting
or subtraction.[20, 21] Wavefront aberrations are a leading accuracy term; dedicated measurements and in-situ
phase-retrieval methods demonstrate < 3 × 10−10 g equivalent bias and routes to further reduction.[18, 19] Active isolation routinely delivers 102 –103 vertical attenuation at 30 mHz–10 Hz in fieldable systems.[14] Frequencydependent electronics/Raman-chirp phases are odd-in-keff
and cancel under k-reversal with residuals characterized
and mitigated.[17, 24] Rotation platforms and mirrortilt compensation explicitly separate Coriolis/Sagnac
terms and have been demonstrated across wide orientation/rotation ranges.[15, 23] Source-mass gravity signals in horizontal/baseline geometries establish lock-in
protocols directly applicable to our T 3 search.[22]

VI.

SENSITIVITY SNAPSHOT AND
FEASIBILITY

Long-baseline results demonstrate the needed stability and controls: the Stanford 10 m fountain achieved
long-time point-source interferometry with single-shot
acceleration sensitivity at the few×10−9 g level and
1.4 cm arm separation,[7, 8] while dual-species EP tests
reached η ∼ 10−12 with 2T = 2 s free fall.[9] VLBAI
(Hannover) reports high-flux Rb/Yb sources, 10 m magnetic shielding, and seismic attenuation tailored for long
baseline.[10, 11] SYRTE’s absolute gravimeters and mobile surveys document µGal-class stability with active vibration isolation.[12–14] These capabilities jointly bound
key systematics (vibration, wavefronts, gradients) at or
below our target |∆ϕDFD | ∼ 2 × 10−11 rad for T ∼ 1 s,
and several groups already deploy rotation control and
k-reversal protocols routinely.[15–17]

VII.

DISCUSSION AND OUTLOOK

This work closes the matter-sector gap in the DFD
experimental program. Together with the cavity–atom
redshift comparison (photon sector), matter-wave tests
over-constrain the sector coefficients. A null result at or

Rotation flip
Yes
Often No
No
No
No
No

k-reversal parity
2
Even (keff
)
Mixed
Odd (cancels)
Odd/Even mix
Design-dependent
Odd (cancels)

below the |∆Φ|/c2 lever arm (after the stated controls)
would falsify this DFD sector. Positive detection would
present a geometry-locked, scaling-locked deviation from
GR that cannot be attributed to standard systematics.
ACKNOWLEDGMENTS

I thank colleagues in precision atom interferometry
for advice on rotation tests, dual-species protocols, and
source-mass lock-in strategies.
Appendix A: Sketch of the T 3 derivation from the
gradient operator

Write the branch centers as zA,B (t) = z0 (t) ± 21 ∆z(t)
with ∆z(t) = vr t for 0 < t < T and ∆z(t) = vr (2T − t)
for T < t < 2T . Expand the field along the arms:
∇ψ(zA,B ) ≈ ∇ψ(z0 ) ± 21 ∆z ∂z (∇ψ)|z0 .

(A1)

The constant part ∇ψ(z0 ) cancels in (4) because
R 2T
∆pz dt = 0 for the piecewise ±ℏkeff profile. The
0
linear term gives (using Earth field ∂z (∇ψ) = −2Γ ẑ/c2
and the kinematic separation implicit in ∆z)
Z


1
∆ϕ∇ψ = −
dt 12 ∆z(t) ∂z (∇ψ) · ∆p(t)
2m
Z
Z
g ℏkeff T
g ℏkeff 2T
→ 2
t dt + 2
(2T − t) dt
c m 0
c m T
ℏkeff g  T 2
T2
ℏkeff g 3
=
+
T =
T ,
(A2)
m c2 2
2
m c2
and multiplying by the impulsive momentum separation
ℏkeff from the light pulses yields (5). A full WKB treatment gives the same result and shows cancellation of the
companion ψ∇2 piece for these geometries.

Appendix B: Figure templates (TikZ/PGFPlots)

4

vertical

z

0

T

2Tt

FIG. 1. Light-pulse Mach–Zehnder (Kasevich–Chu) geometry.
Solid/dashed are the two arms; pulses at 0, T, 2T .
4
T 2 (GR)
T 3 (DFD)
|∆ϕ| (arb.)

3

2

1

0

0

0.5

1
T (s)

1.5

2

FIG. 2. Scaling discriminator: DFD T 3 vs. GR T 2 .

[1] M. Kasevich and S. Chu, “Measurement of the gravitational acceleration of an atom with a light-pulse interferometer,” Appl. Phys. B 54, 321 (1992).
[2] A. Peters, K. Y. Chung, and S. Chu, “High-precision gravity measurements using atom interferometry,” Metrologia
38, 25 (2001).
[3] S. Dimopoulos, P. W. Graham, J. M. Hogan, and M. A.
Kasevich, “Atomic gravitational wave interferometric sensor,” Phys. Rev. D 78, 122002 (2008).
[4] G. M. Tino and M. A. Kasevich (eds.), Atom Interferometry (IOS Press, 2014).
[5] A. D. Cronin, J. Schmiedmayer, and D. E. Pritchard,
“Optics and interferometry with atoms and molecules,”
Rev. Mod. Phys. 81, 1051 (2009).
[6] J. M. Hogan, D. M. S. Johnson, and M. A. Kasevich,
“Atom interferometry,” Nat. Phys. 16, 913 (2020).
[7] S. M. Dickerson et al., “Multiaxis Inertial Sensing with
Long-Time Point Source Atom Interferometry,” Phys. Rev.
Lett. 111, 083001 (2013).
[8] A. Sugarbaker et al., “Enhanced Atom Interferometer
Readout through the Application of Phase Shear,” Phys.
Rev. Lett. 111, 113002 (2013).
[9] P. Asenbaum et al., “Atom-Interferometric Test of the
Equivalence Principle at the 10−12 Level,” Phys. Rev.

Lett. 125, 191101 (2020).
[10] D. Schlippert et al., “Very long baseline atom interferometry,” Proc. SPIE (2024).
[11] D. Schlippert et al., “The Hannover Very Long Baseline
Atom Interferometer,” APS DMP (2022).
[12] P. Gillot et al., “The LNE–SYRTE cold atom gravimeter,”
LNE–SYRTE report (2015).
[13] X. Wu et al., “Gravity surveys using a mobile atom interferometer,” Sci. Adv. 5, eaax0800 (2019).
[14] F. E. Oon et al., “Compact active vibration isolation and
tilt stabilization for a transportable quantum gravimeter,”
Phys. Rev. Applied 18, 044037 (2022).
[15] Q. d’Armagnac de Castanet et al., “Atom interferometry at arbitrary orientations and rotation rates,” Nat.
Commun. 15, 6080 (2024).
[16] D. Yankelev et al., “Atom interferometry with thousandfold increase in dynamic range,” PNAS 117, 23414 (2020).
[17] B. Cheng et al., “Influence of chirping the Raman lasers
in an atom gravimeter,” Phys. Rev. A 92, 063617 (2015).
[18] V. Schkolnik et al., “The effect of wavefront aberrations
in atom interferometry,” Appl. Phys. B 120, 311 (2015).
[19] W. J. Xu et al., “In situ measurement of the wavefront
phase shift in an atom interferometer,” Phys. Rev. Applied
22, 054014 (2024).

5
[20] J. Carlton et al., “Characterizing atmospheric gravity
gradient noise for vertical atom interferometers,” Phys.
Rev. D 111, 082003 (2025).
[21] J. Carlton et al., “Clear skies ahead: atmospheric gravity gradient noise for vertical atom interferometers,”
arXiv:2412.05379 (2024).
[22] G. W. Biedermann et al., “Testing gravity with a horizontal gravity-gradiometer atom interferometer,” Phys.
Rev. A 91, 033629 (2015).
[23] Q. Beaufils et al., “Rotation-related systematic effects in a
cold atom accelerometer on a satellite,” NPJ Microgravity
9, 37 (2023).
[24] Y. Xu et al., “Evaluation of a frequency-dependent phase
shift in chirped-Raman atom gravimeters,” Phys. Rev. A
110, 062816 (2024).
[25] D. Schlippert et al., “Quantum Test of the Universality
of Free Fall Using Rubidium and Potassium,” Phys. Rev.

Lett. 112, 203002 (2014).
[26] C. Overstreet et al., “Observation of effective field theory
effects in atom interferometry,” Science 375, 226 (2022).
[27] G. D’Amico, G. Rosi, S. Zhan, L. Cacciapuoti, M. Fattori, and G. M. Tino, “Canceling the Gravity Gradient
Phase Shift in Atom Interferometry,” Phys. Rev. Lett.
119, 253201 (2017).
[28] C. Overstreet, P. Asenbaum, T. Kovachy, R. Notermans,
J. M. Hogan, and M. A. Kasevich, “Effective Inertial
Frame in an Atom Interferometric Test of the Equivalence
Principle,” Phys. Rev. Lett. 120, 183604 (2018).
[29] A. Roura, “Circumventing Heisenberg’s Uncertainty Principle in Atom Interferometry Tests of the Equivalence
Principle,” Phys. Rev. Lett. 118, 160401 (2017).
[30] P. Asenbaum, C. Overstreet, T. Kovachy, D. D. Brown,
J. M. Hogan, and M. A. Kasevich, “Phase Shift in an
Atom Interferometer due to Spacetime Curvature across
its Wave Function,” Phys. Rev. Lett. 118, 183602 (2017).

