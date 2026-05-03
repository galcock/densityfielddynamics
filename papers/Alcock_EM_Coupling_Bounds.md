---
source_pdf: Alcock_EM_Coupling_Bounds.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Accidental and Intentional Constraints on an EM→ ψ Back–Reaction
Coupling
A conservative bound from cavity stability and a practical path to 10−14
Gary Alcock
September 19, 2025
Abstract
We investigate electromagnetic back-reaction on scalar background fields in extended
gravity theories. We consider a minimal extension of Density Field Dynamics (DFD) in
which the electromagnetic (EM) stress acts back on the scalar background ψ with a single
dimensionless parameter λ. When λ = 1, EM probes the optical metric n = eψ but does not
source ψ; when |λ − 1| ̸= 0, EM can pump ψ. We show that the mere stability of existing
high–Q cavities (no observed parametric instability near twice the drive frequency) provides
an “accidental” constraint |λ − 1| ≲ 3 × 10−5 under deliberately conservative assumptions.
The same equations, used intentionally with modest modulation depth and multi–cavity
geometry, imply an immediately accessible search sensitivity approaching |λ − 1| ∼ 10−14 .
We state both a driven ( 2ω = Ωψ ) and a parametric ( 2ω ≃ 2Ωψ ) route, derive compact
design laws, and explain why such effects were not already seen in standard metrology
workflows.

1

Physical interpretation of |λ − 1| ̸= 0

Technical summary. λ toggles whether EM only rides the ψ background (λ = 1) or also
pushes it (|λ − 1| ̸= 0); the latter allows EM cavities to drive or parametrically amplify a ψ
normal mode.
Intuitive picture. Think of ψ as the water and EM as a paddle. If λ = 1, the paddle
slides across without making waves. If |λ − 1| ̸= 0, the paddle does make waves; splash with the
right rhythm and the waves grow.

2

Mode equation and two pumping channels

Reduce the ψ field to a single lab mode q(t) with natural frequency Ωψ and damping γψ :
q̈ + 2γψ q̇ + Ω2ψ q =

(λ − 1)
Mψ

Z

u(r) Ξ(r, t) d3 r + α U (t) q.

(1)

Here u(r) is the normalized spatial profile of the ψ mode, Mψ its effective mass, U (t) the stored
EM energy, and
!
1 −2ψ0
E2
2
Ξ(r, t) ≡ − e
B − 2 ,
(2)
2
c
whose time average carries a 2ω component for a drive at ω. We use U (t) = U0 [1 + m cos(2ωt)]
with modulation depth m ≪ 1.
(i) Driven channel (2ω = Ωψ ).
|q|res ≃

The resonant steady amplitude is

|λ − 1|
2Mψ Ωψ γψ

Z

b 2ω (r) d3 r ≡
u(r) Ξ

b 2ω is the 2ω component and G the geometry overlap.
where Ξ

1

| λ − 1 | |G|
,
2Mψ Ωψ γψ

(3)

(ii) Parametric channel (2ω ≃ 2Ωψ ). Writing the stiffness modulation as q–equation coefficient ∝ U (t) gives a Mathieu gain parameter [8]
h = (λ − 1)

U0
H m,
Mψ Ω2ψ

1
Γ ≃ h Ωψ − γψ .
2

(4)

The instability threshold is
|λ − 1|min =

2γψ Mψ Ω2ψ
Ωψ U0 H m

u2 (r) w(r) d3 r,

w=

(5)

with the positive overlap [6]
1
H=
U0

Z

ε0 2 µ0 2
E + H .
4
4

3

Geometry transparency and two compact laws

3.1

Driven overlap G: when it cancels and how to restore it

(6)

For a single, symmetric pillbox driven in a pure eigenmode (e.g. TM010 or TE011 ), Bessel
identities and time–averaged equipartition make the cross–section integral of B 2 \
− E 2 /c2 vanish,
so G ≈ 0. It revives with (i) a co–phased TE+TM superposition, (ii) a small iris or near–cutoff
asymmetry, or (iii) beating of two nearby modes. A convenient parametrization is
G = u(z0 ) e−2ψ0 η× U0 cos ϕ,

(7)

with η× = O(0.1–1) for well–matched TE/TM radii and ϕ their phase [7].

3.2

Parametric overlap H: robust area–ratio law

For a ψ “tube” of height L and cross–section Aψ , with N compact cavities of total aperture
Acav,tot placed at antinodes, one finds
H ≈

Acav,tot
2
κeff
,
L
Aψ

(8)

with κeff = O(1) capturing mode–shape details. Plugging this into (5) yields the design rule
|λ − 1|min =

A2ψ
π γψ
cs U0 m κeff Acav,tot

(9)

after using Mψ ≃ Aψ L/(2πcs ) for the 1D standing mode (with ψ–sound speed cs ).1

4

Accidental bound vs. intentional search

Accidental constraint (conservative)
Take a single high–Q cavity: U0 ∼ 100 kJ, m ∼ 0.01 (ambient amplitude/PLL dither), γψ /Ωψ ∼
10−3 (weak loss), Aψ ∼ 0.8 m2 , Acav,tot ∼ 3 × 10−3 m2 (one iris), κeff ∼ 1, cs ≤ c. Using (9) gives
|λ − 1| ≲ 3 × 10−5 ,
because any substantially larger coupling would have produced obvious parametric instability
near 2ω in normal operation—and it has not.
1

Any equivalent normalization gives the same scaling; the constant prefactors here are chosen so the law is
numerically tight for cylindrical tubes.

2

Intentional search (same physics, better knobs)
Keep the same setup but make it intentional: U0 → 1 MJ, m → 0.1, array Acav,tot at all
antinodes (×10), shrink Aψ by ×3, and isolate to keep γψ unchanged. Equation (9) then points
to
|λ − 1| ∼ 10−14 reach,
without changing the model or introducing new assumptions.
Table 1: Accidental vs. intentional settings and resulting reach.
Parameter
Stored energy U0 (J)
Modulation depth m
Cavity aperture Acav,tot (m2 )
Tube area Aψ (m2 )
Loss ratio γψ /Ωψ
Projected |λ − 1|min

5

Accidental

Intentional

105

106
0.10
3 × 10−2
0.27
10−3
∼ 10−14

0.01
3 × 10−3
0.8
10−3
≲ 3 × 10−5

Why this was not already seen

(i) Pure eigenmodes suppress the driven channel (G ≈ 0). (ii) Parametric pumping needs deliberate 2ω modulation of stored energy; routine metrology avoids such tones and heavily filters
them. (iii) Any residual 2ω features are treated as technical AM sidebands, not as a new degree
of freedom, and are actively suppressed.

6

Orthogonal cross–check: driven amplitude

With a TE+TM superposition (phase ϕ = 0) so that η× ̸= 0,
∆ψ ≡ u(z0 ) |q|res ≈

| λ − 1 | η× U0 cs
.
πAψ γψ

(10)

Even modest values (η× ∼ 0.3, U0 = 100 kJ, Aψ = 0.8 m2 , γψ = 0.03 s−1 ) give ∆ψ ∼ 1.2 ×
10−3 |λ − 1|, which crosses cavity–atom sensitivity [3] in the 10−12 –10−15 range for |λ − 1| in
10−9 –10−12 , consistent with the parametric thresholds.
Intentional ψ-pump detection checklist
Required capabilities:
• High-Q resonator (Q ≳ 104 ) with stored energy U0 ≳ 1 MJ (pulsed acceptable).
• Phase-stable amplitude modulation at 2ω with depth m ∼ 0.1 on stored energy.
• Placement of cavity apertures at ψ antinodes (maximize H; use multiple irises).
• Phase-sensitive readout near Ωψ ; preserve 2ω tones (do not auto-suppress).
• Null sensitivity target: ∆ψ ≲ 10−14 or equivalently |λ−1| ≲ 10−14 via Eqs. (9)–(10).

3

7

Conclusion

We are not asking anyone to believe new physics; we are asking them to notice the parametric instability that is not there. Unoptimized cavities accidentally constrain |λ − 1|, and an
intentional 2ω modulation test using the same hardware pushes ten orders tighter. A single
afternoon’s measurement could either discover λ ̸= 1 or constrain it below 10−14
using existing apparatus. We invite groups with high–Q cavities and phase–stable 2ω drive
to implement the intentional search of Eqs. (9)–(10).
The broader framework within which this coupling appears is developed in Refs. [1, 2, 5],
with complementary experimental tests in matter-wave interferometry [4].

Acknowledgments
We thank microwave and optical cavity teams for maintaining exquisitely stable resonators that
enable these constraints.

Appendix: Figures
EM paddle

λ = 1: rides only

|λ − 1| ̸= 0: makes waves

Figure 1: Paddle–on–water analogy: probe–only vs. pump.
∆ψ (schematic)

accidental bound
unstable region

stable region

|λ − 1|

Figure 2: Stability constraint: if |λ − 1| were too large, parametric instability would appear.

References
[1] G. Alcock, Density Field Dynamics: Completing Einstein’s 1911–12 Variable-c Program
with Energy-Density Sourcing and Laboratory Falsifiability, submitted to Class. Quantum
Grav. (2025).
[2] G. Alcock, Strong Fields and Gravitational Waves in Density Field Dynamics: From Optical First Principles to Quantitative Tests, Zenodo preprint (2025).
doi:10.5281/zenodo.17115941
[3] G. Alcock, Sector-Resolved Test of Local Position Invariance Using Co-Located Cavity–Atom Frequency Ratios, submitted to Metrologia (2025).
4

[4] G. Alcock, Matter–Wave Interferometry Tests of Density Field Dynamics, submitted to
Phys. Rev. Lett. (2025).
[5] G. Alcock, Density Field Dynamics Resolves the Penrose Superposition Paradox, submitted
to Class. Quantum Grav. (2025).
[6] J. D. Jackson, Classical Electrodynamics, 3rd ed., Wiley (1998).
[7] R. E. Collin, Foundations for Microwave Engineering, 2nd ed., McGraw–Hill (1992).
[8] N. W. McLachlan, Theory and Application of Mathieu Functions, Dover (1964).

5

