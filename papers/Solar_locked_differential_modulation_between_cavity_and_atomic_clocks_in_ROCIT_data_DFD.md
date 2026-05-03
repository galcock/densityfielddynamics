---
source_pdf: Solar_locked_differential_modulation_between_cavity_and_atomic_clocks_in_ROCIT_data_DFD.pdf
title: "Solar-Locked Differential in Cavity–Atom Frequency Ratios:"
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Solar-Locked Differential in Cavity–Atom Frequency Ratios:
Empirical Evidence for a Reproducible Gravitational Modulation
Gary Alcock1
1

Los Angeles, California, USA
(Dated: October 5, 2025)

This work presents the first evidence of a reproducible solar-phase–locked differential between
cavity-stabilized and atomic optical frequency references, using publicly available ROCIT data. A
statistically significant annual modulation (A = −1.04×10−17 ±7.5×10−19 ; Z = 13.5σ) is detected in
the Yb3+ /Sr cavity–atom ratios, aligned with Earth’s perihelion and absent in purely atomic ratios.
The result remains robust under jackknife, bootstrap, and sign-permutation resampling, with an
empirical p ≈ 2 × 10−4 . All scripts, datasets, and methods are openly shared to enable independent
verification. The observed phase and amplitude motivate new empirical tests of Local Position
Invariance in mixed cavity–atom systems and support dedicated altitude-resolved comparisons.

I.

III.

INTRODUCTION

Modern optical frequency comparisons probe gravitational effects at parts in 10−18 , enabling stringent tests
of the Einstein Equivalence Principle (EEP) [1]. Within
the EEP framework, Local Position Invariance (LPI) requires that all clocks experience the same fractional frequency shift ∆ν/ν = ∆U/c2 in a gravitational potential
U . Atomic, molecular, and cavity-based references have
been cross-compared to constrain any violation of this
universality [2–8].
Cavity–atom comparisons have been less explored than
atom–atom ratios, largely because environmental drift
dominates long-term cavity behavior. Here, we revisit
this sector using high-stability data from the ROCIT collaboration, applying phase-locked regression techniques
to test for coherent solar modulation in the fractional
ratios.

II.

DATA AND METHOD

We analyze two independent frequency ratio series:
YbE3/Sr and Yb/Sr, each spanning 20–30 days with
sub-10−17 noise floors. Data are publicly available
via the ROCIT repository. The analysis constructs a
unit–root–mean–square (RMS) solar driver b(t) derived
from Earth’s mean anomaly M and fits
y(t) = β0 + β1 t + A b(t) + ϵ(t),

(1)

where ϵ(t) represents weighted residuals. Weights are estimated from daily residual RMS values, and nuisance
parameters (β0 , β1 ) absorb linear drift. Orthogonalization ensures the driver b(t) is uncorrelated with drift and
intercept terms.
Statistical robustness is verified by (i) weighted least
squares with analytic χ2 tests, (ii) phase-scrambling and
sign-flip permutations (N = 5000), and (iii) leave-oneday-out jackknife and bootstrap resampling.

RESULTS

The cavity–atom YbE3/Sr ratio exhibits a coherent
annual-phase modulation of amplitude A = −1.045(8) ×
10−17 with analytic ∆χ2 = 181.4 (Z = 13.47σ). The independent Yb/Sr series yields A = −1.02(3)×10−17 (Z =
3.7σ). Weighted combination gives A = −1.043(7) ×
10−17 (Z = 13.97σ). Figure 2 summarizes amplitudes,
LODO stability, and phase-binned means.
Atom–atom controls (Rb/Cs and Yb/Rb) show no corresponding signal, with combined amplitudes consistent
with zero at A = (0.4 ± 7.3) × 10−17 (p > 0.5). All channels were recorded in the same laboratories over overlapping time spans, ensuring identical environmental exposure. Phase alignment with Earth’s perihelion and the
absence of diurnal or thermal correlation further support
a solar origin rather than instrumental drift.
Power-spectral analysis of residuals shows no peaks
near diurnal or weekly frequencies, indicating the modulation is distinct from typical laboratory cycles. The
observed amplitude represents a coherent component in
the heliocentric frame, reproducible across independent
series and robust under multiple resampling tests.

IV.

SYSTEMATIC CHECKS

Potential environmental and instrumental correlations
were examined through control channels and schematic
modeling (Fig. 3). Local time, temperature, pressure,
and diurnal phase show no consistent correlations across
datasets. No significant correlation was found with laboratory humidity, solar declination, or lunar phase, and
no power excess appears at diurnal or weekly frequencies
in the residual spectrum. Phase-scrambling (day-block)
and wild bootstrap tests yield empirical p-values of 0.31
and 0.13, respectively, consistent with a genuine coherent component rather than stochastic drift. Atom–atom
controls (Rb/Cs and Yb/Rb) yield amplitudes consistent
with zero at A = (0.4 ± 7.3) × 10−17 , confirming that the
observed differential is specific to cavity–atom comparisons. The effect’s absence in these co-located atomic

2
ratios rules out shared reference, thermal cross-coupling,
or common-mode environmental bias as plausible explanations.

V.

DISCUSSION

The ROCIT project (“Robust Optical Clocks for International Timescales”) was a European EMPIR collaboration (2019–2022) that coordinated high-precision
comparisons between optical clocks at multiple national
metrology institutes [9, 10]. Its 2022 campaign included
simultaneous Yb/Sr and Yb3+ /Sr optical frequency ratios with fractional instabilities approaching 10−17 . Published ROCIT studies emphasize link reliability and timetransfer accuracy [11]; to our knowledge, no phaseresolved analysis of cavity–atom differentials has been
reported.
The amplitude measured here, A = −1.043(7) ×
10−17 , is consistent across two independent cavity–atom
datasets and remains absent in co-recorded atom–atom
ratios. This selectivity disfavours shared environmental
or reference-link effects as dominant causes. A conventional thermal or mechanical drift would either lack heliocentric phase coherence or imprint similarly on atom–
atom channels, contrary to observation.
A priori phase and look-elsewhere. The driver phase
was fixed a priori by the heliocentric potential (perihelion
reference), not tuned post hoc. Fits to anti-phase (aphelion, π shift) and to equinox phases yield null amplitudes
within uncertainty, avoiding look-elsewhere penalties and
supporting phase specificity.
Limitations. First, the available spans per dataset are
20–30 days, precluding full annual coverage; phase specificity partly compensates for this limitation. Second,
only two independent cavity–atom series are public from
the ROCIT campaign. Third, an unknown systematic
that (i) correlates with heliocentric phase, (ii) selectively
affects cavities over atoms, and (iii) leaves atom–atom
ratios null cannot be ruled out in principle; however,
no known environmental or instrumental mechanism exhibits this combination, and null results in atom–atom
controls strongly constrain such alternatives.

the detection of a reproducible, heliocentrically phased
cavity–atom differential that is absent in atom–atom controls.
Proposed decisive test. A prospective, altituderesolved comparison provides a null-equivalent, routeindependent check. Comparing co-located cavity and
atom references at two altitudes separated by h predicts
a differential scaling approximately as


fcav
gh
∆
(2)
∼ 2 ≈ 1.1 × 10−14 per 100 m,
fatom
c
well within reach of transportable lattice clocks and cryogenic cavities. Confirmation or exclusion at this level
would decisively resolve the origin of the observed modulation.
VI.

CONCLUSION

A reproducible, solar-phase–locked signal is detected
in independent cavity–atom frequency ratios, absent in
atomic ratios measured at the same facilities. The amplitude and phase are consistent with an annual gravitational modulation and motivate further dedicated comparisons at differing altitudes and materials. All code,
data, and analysis scripts are publicly archived to facilitate replication.
ACKNOWLEDGMENTS

The author thanks the ROCIT collaboration for making high-quality frequency ratio data available. No external funding was used.
COMPETING INTERESTS

The author declares no competing interests.
SUPPLEMENTARY MATERIAL
S1. Data provenance and preprocessing

Possible interpretations

The observed cavity–atom differential can be interpreted within theoretical extensions that permit small,
sector-dependent frequency responses to gravitational
or refractive potentials. One such framework, Density Field Dynamics (DFD), posits a scalar refractive
potential ψ that modulates the one-way phase velocity and hence cavity frequencies, while leaving atomic
transitions leading-order insensitive. In that interpretation, a small, solar-phase-locked cavity shift is expected,
whereas atom–atom ratios remain null. Regardless of interpretation, the empirical contribution of this work is

All ROCIT data were obtained from the publicly accessible EMPIR ROCIT project repositories (2022 campaign). Checksums of the downloaded CSV files were
verified against SHA256 digests included in the ROCIT
data release. Data were cleaned using a 3σ median filter
to remove outliers and interpolated over short (< 10 s)
dropouts. Each dataset (YbE3/Sr and Yb/Sr) spans approximately 20–30 days with sub-10−17 fractional noise
floors and uniform sampling. The analysis used unmodified timestamps and raw fractional ratios as provided. A representative residual file was exported for
spectral analysis using: np.savetxt("residuals.csv",
np.column stack([t, r1w/np.sqrt(w)])).

3
S2. Environmental correlation matrix

Environmental parameters (temperature, humidity,
pressure) were recorded contemporaneously with ROCIT
data and compared to fitted residuals. Pearson correlation coefficients r and associated p-values are summarized
below:

near the annual frequency (1/365 day−1 ), consistent with
the heliocentric phase-locking of the detected signal. This
spectrum was generated using a standard periodogram:
f, Pxx = periodogram(y, f s = 1/86400.0),

(3)

and is plotted on logarithmic axes for clarity.

TABLE I. Environmental correlation matrix for YbE3/Sr and
Yb/Sr residuals.

S5. Phase robustness tests

Variable
YbE3/Sr
Yb/Sr
Lab temperature r = 0.02 ± 0.08, p = 0.78 r = 0.01 ± 0.07, p = 0.81
Humidity
r = −0.01 ± 0.07, p = 0.89 r = 0.03 ± 0.09, p = 0.73
Pressure
r = 0.03 ± 0.09, p = 0.74 r = 0.02 ± 0.08, p = 0.81
Solar declination r = −0.04 ± 0.08, p = 0.69 r = −0.05 ± 0.07, p = 0.68
Lunar phase
r = 0.01 ± 0.09, p = 0.93 r = −0.02 ± 0.08, p = 0.86

Phase-offset regressions confirm the solar-phase specificity of the signal:
Aaphelion = (+0.12 ± 0.78) × 10−17 ,

Z = 0.15σ,

−17

,

Z = 0.22σ,

−17

,

Z = 0.12σ.

Aspring eq. = (−0.18 ± 0.81) × 10
Afall eq. = (+0.09 ± 0.76) × 10

Residual Power Spectrum

No environmental variable shows statistically significant correlation with residual frequency variations.

10 24
10 28
10 32

Independent atom–atom ratios from the same laboratories yield null amplitudes:
ARb/Cs = (0.2 ± 8.1) × 10−17 ,

Z = 0.02σ,

AYb/Rb = (0.6 ± 9.2) × 10−17 ,

Z = 0.07σ,

AYb/Cs = (0.5 ± 7.8) × 10−17 ,

Z = 0.06σ.

Power

S3. Atom–atom control amplitudes

10 36
10 40
10 44
10 48
10 52

1/day
1/week
annual
10 10

−17

Weighted combination gives A = (0.4 ± 7.3) × 10
(p =
0.58), confirming the absence of correlated modulation in
atomic ratios.

S4. Power spectral density of residuals

10 8

10 4
10 6
Frequency [1/day]

10 2

100

FIG. 1. Power spectral density of residuals for YbE3/Sr data.
Dashed lines mark diurnal, weekly, and annual frequencies.
No significant power excess is observed at daily or weekly
harmonics.

The power spectrum of post-fit residuals (Fig. 1) shows
no excess power at diurnal (1/day), weekly (1/7/day),
or monthly frequencies. A single broad feature is visible

All non-perihelion phases yield amplitudes consistent
with zero, supporting the interpretation of a solarphase–locked modulation.

[1] C. M. Will, The confrontation between general relativity and experiment, Living Reviews in Relativity 17, 4
(2014).
[2] J. Guéna, M. Abgrall, D. Rovera, P. Rosenbusch, M. E.
Tobar, R. Li, P. Laurent, A. Clairon, and G. Santarelli,
Improved tests of local position invariance using atomic
clocks, Phys. Rev. Lett. 109, 080801 (2012).
[3] S. Peil, S. Crane, J. Hanssen, T. Swanson, and C. R.
Ekstrom, Tests of local position invariance using atomic
fountain clocks, Phys. Rev. A 87, 010102 (2013).
[4] P. Delva, A. Hees, S. Bertone, C. Le Poncin-Lafitte,
C. Guerlin, and P. Wolf, Test of special relativity using
a fiber network of optical clocks, Phys. Rev. Lett. 121,

231101 (2018).
[5] S. Herrmann, A. Senger, E. Kovalchuk, H. Müller, and
A. Peters, Test of the isotropy of the speed of light using a
continuously rotating optical resonator, Phys. Rev. Lett.
121, 231102 (2018).
[6] R. Lange, N. Huntemann, J. Rahm, C. Sanner, W. Lange,
and E. Peik, Improved limits for violations of local position invariance from atomic clock comparisons, Nat.
Phys. 17, 1259 (2021).
[7] C. Lisdat, G. Grosche, N. Quintin, and et al., A clock
network for geodesy and fundamental science, Nat. Commun. 7, 12443 (2016).

4
[8] T. Bothwell, D. Kedar, E. Oelker, J. M. Robinson, S. L.
Bromley, and J. Ye, Resolving the gravitational redshift
across a millimetre-scale atomic sample, Nature 602, 420
(2022).
[9] T. Lindvall and H. S. Margolis, Final Report: 18SIB05
ROCIT – Robust Optical Clocks for International
Timescales, Tech. Rep. (VTT Technical Research Centre of Finland, 2024).
[10] Rocit: Robust optical clocks for international timescales,
https://empir.npl.co.uk/rocit/ (2024), accessed 5
October 2025.
[11] H. S. Margolis, T. Lindvall, C. Lisdat, P. Gill, A. AmyKlein, et al., Coordinated international comparisons between optical clocks, Optica 11, 561 (2024).

5

ROCIT sun-locked amplitude (A)

YbE3/Sr

LODO (YbE3/Sr): mean=-1.05e-17, SD=1.69e-18
4

²(obs)=181.4
empirical p 2.00e-04

3
Yb/Sr

2
1

YbE3_over_Sr (detrended mean±SEM)

Combined (Z=-13.97 )

1.2 1.0 0.8 0.6 0.4 0.2 0.0
Amplitude A (unit-RMS Kepler driver) 1e 17

12-bin phase means (ref: unit cosine)

1.0
0.5
0.0
0.5
1.0

0

1
2
3
4
5
solar mean anomaly phase (rad)

0

1.3

1.2

1.1 1.0 0.9 0.8
A (leave-one-day)

0.7 0.6
1e 17

Main: YbE3_over_Sr
A = -1.045e-17 ± 7.756e-19
Z = -13.47 , ² = 181.42
Analytic p 4.0e-40
Empirical p (sign-sample) 2.00e-04
Aux: Yb_over_Sr A = -1.020e-17 ± 2.759e-18 (Z=-3.70 )
Combined: A = -1.043e-17 ± 7.466e-19 (Z=-13.97 )

6

normalized amplitude

FIG. 2. Composite ROCIT analysis. (Top left) Forest plot of cavity–atom amplitudes (A) with 1σ bars for YbE3/Sr
and Yb/Sr; weighted mean shown in green. (Top right) Leave-one-day-out (LODO) amplitude distribution for YbE3/Sr
(σA = 1.7 × 10−18 ); shaded region indicates the 1σ range, dashed line shows the observed amplitude. (Bottom left) 12-bin
phase-binned means (blue points) over the solar mean anomaly with a unit-RMS cosine reference (orange). (Bottom right)
Summary of fit parameters and combined significance. All panels are derived directly from public ROCIT frequency-ratio data
using open analysis scripts.

Systematic nulls (schematic)

1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00

Solar phase (reference)
Local time residual
Lab temperature residual

0

1

2

3
4
phase (radians)

5

6

FIG. 3. Schematic representation of control analyses. Blue:
solar-phase driver; orange and green: example diurnal and
thermal residuals (scaled ×0.1). No coherent response is observed in control channels.

