---
source_pdf: Geometric_Cancellation_of_Cavity__Atom_LPI_Signalsin_Density_Field_Dynamics__A_Formal_Proof.pdf
title: "Geometric Cancellation of Cavity–Atom LPI Signals"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Geometric Cancellation of Cavity–Atom LPI Signals
in Density Field Dynamics: A Formal Proof
Gary Alcock
Independent Researcher

February 25, 2026

Abstract

construction, the vacuum constitutive relations:
εeff = ε0 e+ψ ,

We prove that in Density Field Dynamics (DFD),
the tree-level response of electromagnetic cavity resonances and atomic transition frequencies to the scalar
field ψ cancel in their ratio, reducing the measurable
Local Position Invariance (LPI) violation parameter
from ξLPI ∼ 1 to ξLPI = kαeff · ∆S α ∼ 10−5 . Three independent empirical checks confirm this cancellation.
The BACON optical clock network (Nature 591, 564,
2021) further constrains the screening regime, requiring that kαeff be evaluated at the local gravitational
environment rather than the source field. This erratum strengthens the theory’s consistency with all
existing clock data while preserving the ROCIT 13.5σ
detection as the primary experimental signature.

(2)

This
is an impedance-matched medium: Z =
p
µeff /εeff = Z0 . The phase velocity is vph =
√
1/ εeff µeff = c e−ψ , consistent with n = eψ .
Step 2: Coulomb potential. Virtual photons
propagate on the same optical metric. The static
Coulomb potential between charges is:
V (r) =

e2
e2
=
e−ψ .
4πεeff r
4πε0 r

(3)

The fine-structure constant, measured in coordinate
frame units, becomes:
α(ψ) =

1

µeff = µ0 e+ψ .

Statement of the Problem

e2
e−ψ
= α0 −ψ = α0 .
4πεeff ℏclocal
e

(4)

The e−ψ from εeff and the e−ψ from clocal cancel, so
DFD replaces curved spacetime with a scalar refracα is ψ-independent at tree level.
tive field ψ on flat R3 , with optical metric
Step 3: Atomic structure. With α constant,
the Bohr radius scales as:
c2
ds̃2 = − 2 dt2 + dx2 ,
n = eψ .
(1)
ℏ
n
(0)
a0 (ψ) =
= a0 e+ψ .
(5)
me clocal α
An earlier version of the theory (Sec. 10, DFD v3.1)
claimed that the cavity–atom frequency ratio R = Atoms expand in stronger fields. The Rydberg enfcav /fatom responds to ψ with ξLPI ≈ 1–2, by assign- ergy:
ing Kγ = 1 (photon sector) and Katom ≈ 0 (atomic
ER = 12 α2 me c2local ∝ e−2ψ .
(6)
sector).
This note proves that the optical metric’s consti- For a general transition with relativistic correction
tutive relations require both sectors to respond iden- ϵA :
fatom ∝ e−(2+ϵA )ψ ,
(7)
tically at tree level, reducing ξLPI by a factor ∼ 105 .

2

where ϵA depends on the transition (e.g., ϵSr = 0.06).
Step 4: Cavity frequency. A Fabry–Pérot cavity of material spacer length L, mode number m:

The Constitutive Chain

Step 1: Tamm–Plebanski formalism. The optical metric (1) determines, via the Tamm–Plebanski

fcav =
1

m clocal
.
2L(ψ)

(8)

5

The spacer is an electromagnetic solid: its lattice constant is set by the Bohr radius, so L ∝ a0 (ψ) ∝ e+ψ .
The local light speed is clocal = c e−ψ . Therefore:

Three Independent Confirmations

Check 1: Fine-structure splitting. If α var(9) ied as α0 e−ψ (geometric, unscreened), the ratio of
two transitions in the same atom with different αBoth effects—slower light and longer spacer— sensitivities would show annual modulation at amplicontribute e−ψ each, compounding to e−2ψ .
tude ∆S α ×δψannual ∼ 10−10 . Precision spectroscopy
constrains such variation to < 10−17 . The geometric
scenario is ruled out by > 107 .
3 The Cancellation
Check 2: PTB Yb+ E3/E2. The same-ion comparison |KE3 − KE2 | < 10−8 (Lange et al. 2021). GeFrom Eqs. (7) and (9):
ometric prediction: |∆S α | × δψannual ≈ 5.14 × 1.65 ×
−2ψ
−10 ≈ 8.5 × 10−10 . Ruled out by ∼ 100×.
fcav
e
R=
∝ −(2+ϵ )ψ = e+ϵA ψ .
(10) 10
A
fatom
e
Check 3:
BACON network (Beloy et
al.
2021).
Three
species (Al+ , Sr, Yb) compared at
The leading e−2ψ factor—universal gravitational
6–8 × 10−18 over 8 months spanning perihelion. Geredshift—cancels exactly. The residual geometric
ometric prediction for Yb/Sr: 0.25 × 1.65 × 10−10 =
variation is:
4.1 × 10−11 . Observed stability: ∼ 10−17 . Ruled out
ξgeom = ϵA ≈ 0.06 (for Sr/Si cavity).
(11) by ∼ 106 .
All three checks independently confirm the geometWhy even ξgeom is unphysical. The residual ϵA ric cancellation.
arises from relativistic corrections to atomic structure
that depend on α. But we proved in Eq. (4) that α
is ψ-independent at tree level. The e−(2+ϵA )ψ scal- 6 Screening Regime Constraint
ing of atomic frequencies is an artifact of expressing
The BACON data provide a further constraint. With
frequencies in coordinate time; in proper time (what
solar-orbit screening (a = 5.93 × 10−3 m/s2 , kαeff =
a local observer measures), α = α0 exactly, and the
2.4 × 10−5 ), the predicted Yb/Sr annual signal is:
ratio R is constant.
This is the Weak Equivalence Principle (WEP): δR/R = 0.25×2.4×10−5 ×1.65×10−10 = 1.0×10−15 .
in a local freely-falling frame, non-gravitational
(14)
physics—including α—is position-independent. DFD The BACON Yb/Sr weighted standard deviation is
satisfies WEP at tree level by construction (PPN: 1.1 × 10−17 , ruling out this scenario by ∼ 100×.
γ = β = 1).
With Earth-surface screening (a = 9.8 m/s2 , k eff =
fcav ∝

e−ψ
= e−2ψ .
e+ψ

6.0 × 10−7 ):

4

The Physical Residual

δR/R = 0.25×6.0×10−7 ×1.65×10−10 = 2.5×10−17 .
(15)
This is comparable to the BACON between-day variability (ξYb/Sr = 10.8 × 10−18 , χ2red = 6.0) and therefore consistent with the data.
Conclusion: Screening must be evaluated at the
local gravitational environment, not at the source of
the perturbation. Physically, the Unruh–de Sitter
mechanism depends on the total local |∇ψ|, which at
Earth’s surface is dominated by Earth’s own field.

WEP is broken at one loop by Unruh–de Sitter
screening of quantum fluctuations. The screened effective coupling is:
√
kαeff (a) = 2 α µLPI (a/a0 ),
(12)
where µLPI (y) = (1 + y)−1/2 and a is the local gravitational acceleration.
The measurable LPI violation in a cavity–atom
comparison is:
α
α
ξLPI = kαeff · (SA
− Scav
),

α

7

(13)

α ≡ d ln ν /d ln α is the transition’s αwhere SA
A
α ≈ 1 for an EM-bonded spacer.
sensitivity and Scav

Implications

1. Section 10 erratum: ξLPI ≈ 1–2 is replaced
by ξLPI = kαeff (alocal ) · ∆S α ∼ 10−7 at Earth’s
2

surface.
2. ROCIT detection preserved: The 13.5σ
ion–neutral modulation uses a different channel (cavity–atom with ionic transition) where
∆S α ∼ 6, giving signals at ∼ 10−5 —unaffected
by this revision.
3. Nuclear clocks become paramount: With
α ≈ 5900 (Beeks et al. 2025), the Th-229/Sr
STh
annual signal from α-coupling alone is:
δR/R ≈ 6×10−7 ×5900×1.65×10−10 ≈ 5.8×10−13 ,
(16)
detectable at current nuclear clock precision (∼
10−12 ).
4. Height tests require space: The heightseparated test needs ∼ 10−20 precision for ∆h =
100 m, pushing it to future space missions.
5. Theory becomes cleaner: The “why hasn’t
anyone noticed 10−10 drift?” problem disappears. All existing null results are naturally explained.

8

Summary

The optical metric ds̃2 = −c2 e−2ψ dt2 + dx2 uniquely
determines constitutive relations ε = ε0 eψ , µ = µ0 eψ .
These modify the Coulomb potential, causing cavity
spacers to expand by e+ψ while light slows by e−ψ .
The compound effect gives fcav ∝ e−2ψ , identical to
the atomic scaling, so the ratio is constant at tree
level.
The physical LPI violation is a one-loop quantum
correction, screened by the local gravitational environment to kαeff ∼ 10−7 at Earth’s surface. Three independent empirical checks confirm this picture. The
nuclear clock transition in 229 Th, with S α ≈ 5900,
amplifies this residual to ∼ 10−13 —within reach of
current experimental programs.
Acknowledgments. The author thanks the BACON collaboration, Jun Ye, and Nils Huntemann for
the precision data that constrain these predictions.

3

