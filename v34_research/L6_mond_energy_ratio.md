# L6: MOND Gravitational Enhancement Energy vs Baryon Rest Mass

**Agent:** L6
**Date:** 2026-04-06
**Question:** Is the ratio of total MOND gravitational enhancement energy to total baryon rest-mass energy equal to 16/3?

## TL;DR

**NO.** The ratio is ~10⁻¹⁰, not 16/3 ≈ 5.333. The hypothesis fails by
roughly ten orders of magnitude, and fails *on dimensional grounds* before
any numerics: gravitational binding energies in virialized systems scale
as v²/c² ~ 10⁻⁶ relative to rest mass, so no binding-energy-to-rest-mass
ratio can be O(1), let alone 5.33.

## Method

Computed numerically (script: `/tmp/L6_mond.py`).

1. **MOND extra energy per galaxy.** Deep-MOND virial scaling gives
   E_MOND ~ M (G M a₀)^{1/2}, vs Newtonian E_N ~ G M² / R. Using baryon
   size R_b(M) = 3 kpc × (M/10¹⁰ M☉)^{0.3}, the extra is
   ΔE(M) = max(E_MOND − E_N, 0) for M below the MOND transition mass.

2. **Galaxy population.** Schechter mass function with
   M★ = 10^{10.66} M☉, φ★ = 3.96×10⁻³ Mpc⁻³, α = −1.35 (Baldry+2012-ish).
   Integrated 10⁷–10¹³ M☉.

3. **Denominator.** Baryon rest-mass energy density, both (a) restricted
   to the galaxy population produced by the Schechter integral, and
   (b) the full cosmic baryon density ρ_b = Ω_b ρ_crit with Ω_b = 0.0493.

## Numerical Result

| Quantity | Value |
|---|---|
| Schechter baryon density | 1.69 × 10⁻²⁹ kg/m³ |
| Cosmic baryon density | 4.21 × 10⁻²⁸ kg/m³ |
| Galaxy fraction of cosmic baryons | 4.0% |
| MOND extra energy density | 3.43 × 10⁻²¹ J/m³ |
| Baryon rest-mass energy (galactic) | 1.52 × 10⁻¹² J/m³ |
| Baryon rest-mass energy (cosmic) | 3.78 × 10⁻¹¹ J/m³ |
| **Ratio (galaxy denominator)** | **2.26 × 10⁻⁹** |
| **Ratio (cosmic denominator)** | **9.06 × 10⁻¹¹** |
| Target 16/3 | 5.333 |
| Result / target | ~4 × 10⁻¹⁰ |

## Why 16/3 Cannot Be This Ratio

Any gravitational binding or kinetic-energy correction to rest mass is
bounded by the virial ratio v²/c². For galaxies v ~ 200 km/s so
v²/c² ~ 4×10⁻⁷. Summing over cosmic structure cannot push that above
~10⁻⁶ of ρ_b c². A ratio of 5.33 would require the MOND correction to
carry 533% of the baryon rest-mass energy, which is physically impossible
for a non-relativistic virial-scale correction.

The 16/3 factor in DFD (α-tower / path integral / conserved current in
H6, J1_01–03, K1_04) is a **counting / operator coefficient**, not a
ratio of energy densities. Coercing it into a cosmological energy budget
conflates a dimensionless group-theoretic factor with a virial ratio.

## Conclusion

- The MOND extra-energy to baryon-rest-mass ratio is **~10⁻¹⁰**, not 16/3.
- The 16/3 identity does **not** live in this ratio.
- Any DFD claim linking 16/3 to a cosmic energy budget should be redirected
  to the operator-counting / path-integral derivations where 16/3 is
  dimensionless by construction.

**Status:** Hypothesis falsified. 16/3 is not the MOND-to-baryon energy ratio.
