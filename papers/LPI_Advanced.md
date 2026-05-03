---
source_pdf: LPI_Advanced.pdf
title: "Completing the Local Position Invariance Test Suite:"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Completing the Local Position Invariance Test Suite:
A Sector-Resolved Cavity–Atom Frequency Ratio
Experiment
Gary Alcock
Los Angeles, CA, USA
October 2025
Abstract
Local Position Invariance (LPI) — the universality of gravitational redshift
across all physical systems — has been tested for decades using atom–atom, matter–
matter, and resonator–resonator comparisons. Yet one critical cross-sector test
remains absent: cavity-stabilized optical frequencies (photon sector) compared directly to atomic transitions (matter sector) across a gravitational potential. Here
we present the formalism, explicit predictions, and control strategies for this missing experiment, which would complete the LPI test suite. In General Relativity
(GR), cavity–atom ratios must remain strictly constant, yielding slope coefficients
ξ (M,S) = 0. In Density Field Dynamics (DFD), a scalar refractive framework consistent with GR’s classic tests but predicting deviations in low-acceleration regimes,
evacuated cavities track the refractive index n = eψ while atomic transitions remain leading-order ψ-insensitive, giving ξ (M,S) ≃ 1. This implies a geometry-locked
slope of order ∆R/R ∼ ∆Φ/c2 ≈ 1.1 × 10−14 per 100 m on Earth. We provide
(i) a historical review of LPI tests, (ii) full derivations of the cavity–atom slope
observable and its parametrized post-Newtonian (PPN) consistency, (iii) a sectoral
decomposition across materials and species, and (iv) an error budget demonstrating feasibility with existing 10−16 cavities and 10−18 optical clocks. We argue that
this cross-sector test provides the final closure of LPI, yielding a binary and decisive discriminator: a null confirms GR and rules out DFD, while a non-null slope
falsifies GR’s universality.

1

Introduction

The Einstein equivalence principle (EEP) underpins all metric theories of gravity. Its
LPI component requires that all systems undergo identical gravitational redshifts, independent of composition or mechanism. The gravitational redshift has been tested in
progressively more precise experiments: Pound–Rebka (1960), the 1976 GP-A rocket [1],
and modern optical clock comparisons [2, 3]. Each confirmed GR to better than 10−6 .
Yet all these comparisons are sector-homogeneous. No experiment has compared
cavity-stabilized optical frequencies (tracking photon propagation) against atomic transitions (quantum energy levels) across altitude. This work proposes the missing cross-sector
test, completing the LPI suite.

1

2

Background and Literature Review

2.1

Historical redshift tests

• Pound–Rebka (1960): Mössbauer γ-ray redshift in a tower.
• GP-A (1976): H maser on a suborbital rocket, 7 × 10−5 confirmation.
• Modern optical clocks: Yb+ , Sr lattice clocks achieving 10−18 stability.

2.2

Sectoral coverage

1. Atom–atom: microwave or optical transition comparisons.
2. Resonator–resonator: cavity or oscillator stability tests.
3. Matter–matter: Mössbauer and nuclear transitions.
4. Cavity–atom: missing.

3

Formalism of the Cavity–Atom Test

Define the ratio:

∆Φ
∆R(M,S)
= ξ (M,S) 2 ,
(M,S)
R
c

(1)

where
(M )

ξ (M,S) = αw − αL

(S)

− αat .

In GR, ξ (M,S) = 0. In DFD, ξ (M,S) = 1.
For ∆h = 100 m on Earth:
∆R
≈ 1.1 × 10−14 .
R

4

PPN Consistency

DFD recovers GR’s solar-system predictions by construction. Its effective potential Φ =
−c2 ψ/2 yields γ = β = 1, all other PPN parameters vanishing. Thus light deflection,
Shapiro delay, and perihelion precession are preserved. Deviations appear only in crosssector LPI tests, where GR requires null slopes.

5

Sector Decomposition

With two cavity materials and two atomic species:
Sr
δtot = αw − αLULE − αat
,

(2)

δL = αLSi − αLULE ,
Yb
Sr
δat = αat
− αat
.

(3)

2

(4)

Table 1: Mapping of measured slopes to sector parameters.
Measured ratio Combination Parameter
ULE/Sr
Si/Sr
ULE/Yb
Si/Yb

δtot
δtot + δL
δtot + δat
δtot + δL + δat

total offset
cavity diff.
atom diff.
over-determined

Table 2: Illustrative systematic error budget for cavity–atom slopes.
Systematic
Target (frac.) Control method
Dispersion (dual-λ)
Elastic sag
Thermal drift
Polarization/birefringence
Comb transfer noise

< 3 × 10−15
< 3 × 10−15
< 3 × 10−15
< 3 × 10−15
< 1 × 10−16

dual-wavelength probing
180◦ orientation flips
environmental stabilization
swaps + polarization control
stabilized links

6

Error Budget and Systematic Controls

7

Feasibility
• Cavities: 10−16 fractional stability [4, 5].
• Optical clocks: 10−18 stability [6, 2].
• Baseline: 30–100 m suffices for 5σ discrimination.

8

Discussion: Completing the LPI Suite

This test completes the quadrilateral: atom–atom, resonator–resonator, matter–matter,
and cavity–atom. Its binary outcome:
• ∆R/R = 0: GR confirmed, DFD falsified.
• ∆R/R ∼ 10−14 : GR falsified, DFD supported.
Either result is decisive.

9

Conclusion

We have presented the formalism, PPN consistency, predictions, and systematic controls
for the final untested LPI sector. This cavity–atom comparison is feasible today, requires no new technology, and provides a definitive discriminator between GR and DFD.
Completing the LPI test suite is both achievable and foundational.

3

References
[1] R F C Vessot et al., Phys. Rev. Lett. 45, 2081 (1980).
[2] W F McGrew et al., Nature 564, 87 (2018).
[3] R Lange et al., Phys. Rev. Lett. 126, 011102 (2021).
[4] T Kessler et al., Nat. Photonics 6, 687 (2012).
[5] S Häfner et al., Opt. Lett. 40, 2112 (2015).
[6] T L Nicholson et al., Nat. Commun. 6, 6896 (2015).

4

