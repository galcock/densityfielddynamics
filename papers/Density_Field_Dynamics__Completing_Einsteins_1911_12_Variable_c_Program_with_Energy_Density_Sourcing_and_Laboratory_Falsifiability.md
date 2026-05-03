---
source_pdf: Density_Field_Dynamics__Completing_Einsteins_1911_12_Variable_c_Program_with_Energy_Density_Sourcing_and_Laboratory_Falsifiability.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Density Field Dynamics: Completing Einstein’s 1911–12 Variable-c Program with
Energy-Density Sourcing and Laboratory Falsifiability
Gary Alcock
Independent Researcher, Los Angeles, CA, USA
(Dated: September 19, 2025)
Einstein’s 1911–12 variable light-speed proposal tied c(x) to Newtonian potential but was abandoned in 1915 with the adoption of curved spacetime. The missing pieces were a sourcing principle
beyond Newton’s potential and a consistent conservation law. We show that a single scalar field
ψ(x), derived from a variational action and coupled universally to density, closes that gap: photons propagate with n = eψ (so the one-way phase speed is c1 = ce−ψ ), while matter accelerates
2
as a = c2 ∇ψ. A constrained, monotone family µ(|∇ψ|/a⋆ ) follows from first principles: GR normalization in the solar regime, Noether scale symmetry in the deep-field regime, and convexity for
stability. In the high-gradient limit the nonlinear field equation reduces asymptotically to Poisson’s
equation, fixing the 1/r potential and yielding the exact GR coefficients for deflection, redshift,
Shapiro delay, and perihelion (shown explicitly at 1PN). Crucially, a sector-resolved cavity–atom
comparison predicts a non-null, geometry-locked slope ∆R/R = ξ ∆Φ/c2 ; in a nondispersive optical band the expectation is ξ ≃ 2, giving ∼ 2.2 × 10−14 per 100 m—well within current 10−16
precision [4, 5]. We state explicit falsification criteria. Thus Density Field Dynamics (DFD) is a
minimal, action-consistent completion of Einstein’s abandoned program, experimentally decidable
with present technology.

I.

MOTIVATION

In 1911–12 Einstein wrote that “the velocity of light in the gravitational field is a function of the place” and
tied constancy to regions of constant potential [1, 2]. Lacking a dynamical law and a conservation framework, he
abandoned this approach in 1915 in favor of curved spacetime. Here we present a minimal scalar completion that (i)
is derived from a variational action with universal coupling to density (closing the conservation gap), (ii) reproduces
GR’s classic weak-field coefficients, and (iii) makes one clean laboratory prediction that GR forbids. For a modern
overview of experimental confrontations with GR see [3]; for VSL overviews distinct from our local, action-based
approach see [7].
II.

CONVENTIONS AND NOTATION

We work in Euclidean R3 for quasi-static fields with time t, write gradients as ∇, and use dℓ for spatial line elements
2
2
and ds for spacetime intervals. The effective potential is Φ ≡ − c2 ψ, so that matter acceleration is a = −∇Φ = c2 ∇ψ.
The optical index is n = eψ ; in a verified nondispersive band, geometric optics gives phase velocity vph = c/n = c1
(one-way). Round-trip measurements along a fixed path remain invariant at c (consistent with precision Lorentz tests
in electrodynamics [6]).
III.

ACTION, FIELD EQUATION, AND CONSERVATION

We focus on the weak-field, quasi-static regime relevant to solar-system and laboratory tests, while exhibiting the
1PN scaffold.
a. Field sector.
 2



Z
|∇ψ|2
c2
a⋆
Sψ = d3 x dt
W
−
ψ(ρ
−
ρ̄)
,
(1)
8πG
a2⋆
2
√
with W ′ (y) = µ( y). Variation yields the quasilinear elliptic equation
 


|∇ψ|
8πG
∇· µ
∇ψ = − 2 (ρ − ρ̄).
(2)
a⋆
c
Universal coupling and spatial translation invariance imply Noether conservation of the total (field+matter) momentum; the constant background ρ̄ does not spoil this invariance. With y ≡ |∇ψ|2 /a2⋆ , a positive energy density follows

2
from convexity:
Eψ =

a2⋆
[2y W ′ (y) − W (y)] ≥ 0,
8πG

(3)

and the associated stress is uniformly elliptic for µ′ (x) > 0, ensuring well-posedness (Lax–Milgram/monotone operators).
b. Relativistic 1PN structure. The scalar induces the isotropic 1PN line element
ds2 = −(1 + 2Φ/c2 )c2 dt2 + (1 − 2γ Φ/c2 ) dx2 ,

2

Φ = − c2 ψ.

(4)

Because photons see the Gordon optical metric with n = eψ , Fermat’s principle reproduces
R Einstein deflection,
P the full
locking γ = 1 (see Supplemental Material and [3]). The worldline action Sm = − i mi c ds in (4) reduces to
R 3
2
d x dt ρ (v 2 /2 − Φ), giving a = −∇Φ = c2 ∇ψ.

IV.

THE SCALE a⋆ AND FIRST-PRINCIPLES CONSTRAINTS ON µ(x)

Dimensional consistency clarifies the argument of µ. In potential variables,
X≡

|∇Φ|
a0

(dimensionless),

|∇ψ|
2 |∇Φ|
= 2
≡ X,
a⋆
c a⋆

(5)

so the two forms are equivalent if we identify
a⋆ ≡

2a0
.
c2

(6)

Here a0 is a universal acceleration scale (empirically near galactic scales), while a⋆ is the corresponding ψ-sector scale.
The function µ is not ad hoc; it is fixed up to a narrow family by:
1. GR normalization (solar regime). For X ≫ 1, µ → 1 to recover Newtonian/GR behavior and the 1/r
potential [3].
2. Scale symmetry (deep field). In the low-acceleration regime, Noether scale invariance of Sψ under (x, ψ) →
(λx, ψ) fixes the dimensional dependence µ(X) ∝ X, yielding asymptotically flat rotation curves and Tully–
Fisher/RAR scaling without inserting them by hand.
3. Ellipticity and stability. Monotonicity µ′ (X) > 0 ensures uniform ellipticity; convex W guarantees Eψ ≥ 0
and coercivity. Standard monotone-operator methods then give existence/uniqueness for appropriate data.
A convenient two-parameter family obeying all constraints is
µα,λ (X) =

X
1 + λX α

1/α ,

α ≥ 1, λ > 0,

(7)

interpolating smoothly between µ ∼ X (deep field) and µ → 1 (solar). Within the stated constraints, (7) is essentially
unique up to reparameterizations (rescalings of X).
a. High-gradient (Poisson) limit. Let µ(X) = 1 + ε(X) with ε → 0 and Xε′ (X) → 0 as X → ∞. Then
∇2 ψ = −

8πG
(ρ − ρ̄) − ∇ε·∇ψ,
c2

(8)

so corrections are suppressed by 1/X ∼ a0 /|∇Φ|. For a point mass M ,
ψ(r) =

i
2GM h
1 + O a0 r/GM ,
2
c r

Φ(r) = −


GM
+ O a0 r ,
r

(9)

and subleading terms do not renormalize the classic-test coefficients (explicitly verified in the Supplemental Material).

3
V.

RECOVERY OF CLASSICAL TESTS

With ψ ≃ 2GM/(c2 r) and n ≃ 1 + ψ, we obtain:
• Gravitational redshift: ∆ν/ν = −∆Φ/c2 .
R
• Light deflection: α = ∂b n dz = 4GM/(c2 b) (Fermat integral).
R
R
• Shapiro delay: T = (1/c) n dℓ ⇒ one-way 2GM/c3 dℓ/r, two-way coefficient 4GM/c3 .
• Perihelion: PPN with β = γ = 1 gives ∆ϖ = 6πGM/[c2 a(1 − e2 )].
Each matches GR’s numerical coefficient (explicit steps are provided in the Supplemental Material, including the
historical factor-of-two in deflection; see also [3]).
VI.

RELATION TO SCALAR–TENSOR THEORIES

DFD differs from Brans–Dicke/scalar–tensor frameworks in three key ways: (i) no varying G (GR normalization is
recovered in high-gradient limit), (ii) photons propagate in the Gordon optical metric with n = eψ (one-way) while
preserving two-way invariance along a fixed path, and (iii) the deep-field µ ∼ X behavior follows from Noether scale
symmetry rather than phenomenological fitting. For broader VSL perspectives distinct from our local completion,
see [7].
VII.

STRONG FIELDS AND RADIATIVE SECTOR

A companion analysis [8] treats compact profiles, optical horizons, shadow radii, and binary inspiral waveforms.
The radiative sector is minimal: no extra propagating modes beyond GR, so cGW = c (consistent with multimessenger
bounds). Strong-field departures map to parameterized post-Einsteinian (ppE) phase coefficients, giving falsifiable
GW signatures.
VIII.

COSMOLOGY: LINE-OF-SIGHT OPTICAL BIAS

DFD predicts a line-of-sight (LOS) optical bias: accumulated refractive gradients shift inferred distances, mimicking
dark energy in some analyses. A concrete test is directional H0 variation:
Z
Z χ
2
1 χ
(−Φ) dℓ,
(10)
ψ dℓ ≃ 2
δH0 (n̂) ∝
χ 0
c χ 0
predicting correlations between δH0 (n̂) and LOS density gradients. Detection (or absence) of these correlations
provides a cosmological discriminator.
IX.

SECTOR-RESOLVED LABORATORY DISCRIMINATOR

Lock a laser to a cavity (fcav ∝ c1 /L) and compare to an atomic transition (fat ). Define measurable sector
coefficients
αw =

∂ ln fcav
,
∂(Φ/c2 )

(M )

(M )

αL

=

∂ ln L(M )
,
∂(Φ/c2 )

(S)

αat =

∂ ln fat
.
∂(Φ/c2 )

(11)

(S)

Form four ratios per site R(M,S) = fcav /fat , then across two altitudes:

∆R 
∆Φ
(M )
(S) ∆Φ
= αw − αL − αat
≡ξ 2 .
2
R
c
c

(12)

Deriving αw = 2. In a nondispersive band, fcav ∝ c1 /L with c1 = ce−ψ and ψ = −2Φ/c2 , so
∂ ln fcav
∂(−ψ)
∂ ln L
(M )
=
−
= 2 − αL ,
∂(Φ/c2 )
∂(Φ/c2 ) ∂(Φ/c2 )

(13)

4
hence the wave-sector response is αw = 2. In GR, local position invariance (LPI) enforces α’s = 0 and ξ = 0 [3]. In
DFD, ξ ≃ 2 is the geometry-locked expectation in a nondispersive band, subject to direct sector-resolved measurement
via over-determined multi-material/multi-species fits to Eq. (12). Numerically,
∆R
≃ 2.18 × 10−14 per 100 m (Earth)
R
(ξ ≃ 2), with optical-clock precision ∼ 10−16 [4, 5].

A.

(14)

Matter-wave interferometry discriminator

DFD modifies the kinetic term for massive de Broglie waves via the e−ψ dressing of gradients, which introduces a
small, geometry-locked cubic-in-time phase for light-pulse atom interferometers operating in a vertical gradient. For
a Mach–Zehnder sequence with effective wavevector keff and pulse separation T , one finds
∆ϕDFD = ∆ϕGR + δϕT 3 ,

∆ϕGR = keff g T 2 ,

(15)

with the additional contribution
δϕT 3 ≃

2
ℏ keff
g 3
T ,
m c2

(16)

where m is the atomic mass and g the local gravitational acceleration. Equation (16) is independent of laser phase noise
and is reversal-odd under keff → −keff , allowing isolation by k-reversal and rotation. For representative parameters
(keff ∼ 107 m−1 , T = 1 s, Sr/Yb mass), δϕT 3 ∼ 2 × 10−11 rad, within reach of long-baseline facilities using vibration
isolation and common-mode rejection. A practical strategy is:
• Alternate (+keff , −keff ) shots to cancel even-in-k terms (∝ T 2 ) and retain the T 3 odd component.
• Modulate the source height or insert short ∆h steps to convert g → g + δg and verify the linear dependence of
δϕT 3 on g.
• Employ species or isotope pairs (m → m′ ) to check the 1/m scaling in Eq. (16).
2
In GR the odd-in-k cubic term is absent; detecting a clean T 3 contribution that follows the (keff
/m) g scaling constitutes an orthogonal falsification/confirmation channel complementary to the cavity–atom slope test [9].
a. Systematics discrimination and experimental specifics. A geometric potential change ∆Φ is universal; local
systematics are not. The design employs:

• Sector resolution: Two cavity materials (ULE, Si) and two atomic species (Sr, Yb) yielding four R(M,S) per
(M )
(S)
altitude and an over-determined fit for (αw , αL , αat ).
• Dispersion bound: Dual-wavelength probing of each cavity; ξ is taken from the dispersion-free band and bounded
against ∂n/∂ω.
• Orientation/elastic controls: 180◦ flips of cavities to model and subtract elastic sag; polarization/birefringence
checks.
• Hardware/electronics swaps: Interchange optics, PDs, servos, and RF references to expose electronics-induced
slopes.
• Environment and geodesy: Temperature/pressure/humidity thresholds, vibration isolation, and geodesy beyond
g∆h to fix ∆Φ.
• Allan budget: Full noise model (laser, cavity, clocks, comb) with stationarity checks; no data in motion; stationary windows only.
Any local systematic produces non-universal α’s and is rejected in the joint GLS fit; only a geometry-locked ∝ ∆Φ/c2
slope across sectors survives (cf. precision tests of Lorentz symmetry in electrodynamics [6] for methodology parallels).

5
X.

FALSIFICATION CRITERIA

DFD is falsified if any of the following hold (after controls):
1. Sector-resolved LPI: ξ = 0 within uncertainties across altitude, with dual-wavelength dispersion bounds and
elastic/orientation controls applied.
2. Geometry-locked loops: Crossed-cavity or reciprocity-broken fiber-loop tests with vertical separation yield
strict nulls when dispersion is bounded.
3. Dispersion explanation: Verified ∂n/∂ω fully accounts for residuals in-band.
4. Cosmology: No correlation between δH0 (n̂) and LOS density gradients when observational systematics are
controlled.

XI.

CONCLUSION

A century after 1912, Einstein’s variable-c intuition can be made consistent by sourcing a scalar refractive field from
density via an action principle. The framework recovers GR where tested and makes a clean, laboratory prediction that
GR forbids. Either a nonzero, sector-resolved, geometry-locked slope appears, or DFD is falsified. Complementary
tests extend to strong fields, gravitational waves, and cosmology [3, 8].

6
Site A (higher altitude)

ULE cavity

Sr clock
Self-referenced comb

Si cavity

(M )

(M,S)

RA

=

Yb clock

fcav

(S)

∆Φ
∆R
=ξ 2
R
c
Geometry-locked slope (universal across M, S)

fat

∆Φ ≈ g ∆h

Site B (lower altitude)

ULE cavity

Sr clock
Self-referenced comb

Si cavity

Yb clock
(M )
fcav
(M,S)
RB
= (S)
fat

FIG. 1. Sector-resolved cavity–atom test across a gravitational potential difference (schematic). Two fixed
altitudes. Each site: ULE/Si ultra-stable cavities, Sr/Yb optical clocks, and a self-referenced comb. Four ratios per site
(M )
(S)
R(M,S) = fcav /fat are formed. The geometry-locked observable is the slope of ln R vs. Φ/c2 : ∆R/R = ξ ∆Φ/c2 with
(M )
(S)
ξ = αw − αL − αat . GR predicts ξ = 0; in a verified nondispersive optical band DFD expects ξ ≃ 2. Multi-material/multispecies fits extract sector coefficients and reject non-universal systematics.

7

[1] A. Einstein, “On the Influence of Gravitation on the Propagation of Light,” Annalen der Physik 35, 898–908 (1911).
[2] A. Einstein, “Lichtgeschwindigkeit und Statik des Gravitationsfeldes,” Annalen der Physik 38, 355–369 (1912).
[3] C. M. Will, “The Confrontation between General Relativity and Experiment,” Living Rev. Relativity 17, 4 (2014).
[4] A. D. Ludlow, M. M. Boyd, J. Ye, E. Peik, and P. O. Schmidt, “Optical atomic clocks,” Rev. Mod. Phys. 87, 637–701
(2015).
[5] N. Huntemann et al., “Single-Ion Atomic Clock with 3 × 10−18 Systematic Uncertainty,” Phys. Rev. Lett. 116, 063001
(2016).
[6] M. Nagel et al., “Direct terrestrial test of Lorentz symmetry in electrodynamics to 10−18 ,” Nature Communications 6, 8174
(2015).
[7] J. Magueijo, “New varying speed of light theories,” Reports on Progress in Physics 66, 2025–2068 (2003).
[8] G. Alcock, “Strong Fields and Gravitational Waves in Density Field Dynamics: From Optical First Principles to Quantitative
Tests,” Zenodo (2025). doi:10.5281/zenodo.17115941.
[9] G. Alcock, “Matter-Wave Interferometry Tests of Density Field Dynamics,” Zenodo (2025). doi:10.5281/zenodo.17150358.

