# R9 Agent 16: Exact Chern-Simons Potential V(theta) and Definitive m_chi

## Summary

Computed the exact potential V(theta) = -ln|F(theta)| from the finite Fourier sum of SU(2) Chern-Simons partition functions on S^3, with Z_CS(k) = sqrt(2/(k+2)) sin(pi/(k+2)) summed from k = 0 to 60. The results are definitive and surprising.

---

## 1. The Partition Functions Z_CS(k)

The SU(2) Chern-Simons partition function at level k on S^3:

    Z_CS(k) = sqrt(2/(k+2)) * sin(pi/(k+2))

Key values:
- Z_CS(0) = 1.000 (maximum, at k=0)
- Z_CS(1) = 0.707
- Z_CS(10) = 0.106
- Z_CS(60) = 0.0091
- Sum = 5.200 (the generating function value F(0))

The distribution Z_CS(k) is **monotonically decreasing** in k, heavily weighted toward low CS levels. This is crucial for the physics.

---

## 2. The Potential V(theta)

### Global Structure

V(theta) = -ln|sum_{k=0}^{60} Z_CS(k) exp(ik theta)|

The potential has a striking **asymmetric structure**:

1. **Deep central well at theta = 0** (CP-conserving vacuum)
   - V(0) = -1.6486 (the global minimum)
   - V''(0) = 158.35 (extremely sharp curvature)
   - Well width: approximately 1.24 pi radians

2. **29 shallow oscillating minima** clustered around theta ~ pi
   - Located symmetrically at theta = +/- 0.534 pi, +/- 0.568 pi, ... +/- 0.967 pi
   - V values range from 0.237 to 0.532 (all much higher than V(0))
   - Spacing between adjacent oscillating minima ~ 0.069 pi (roughly 2pi/29)
   - Curvatures V'' range from 10.3 to 27.9

3. **Total barrier height** from theta=0 to maximum: 2.197

### The Potential is NOT Cosine-Like

A standard axion cosine potential V = A(1 - cos theta) would have:
- Max/V'' ratio = 2 (i.e., max height = 2A)
- Our ratio: max height / V''(0) = 2.197 / 158.35 = 0.0139

The potential is **144 times sharper** at theta=0 than a cosine with the same barrier height. This is because V = -ln|F| creates a logarithmic singularity-like shape near the maximum of |F|, while being relatively flat where |F| is small.

---

## 3. The Key Result: V''(0) = Var(k)

### Analytic derivation (exact, no numerics needed)

Since F(theta) = sum Z(k) exp(ik theta), we have:
- F(0) = S = sum Z(k) = 5.200
- F'(0) = i * sum k Z(k) = i * 46.62
- F''(0) = -sum k^2 Z(k) = -1241.3

For V = -ln|F|, the second derivative at theta = 0 is:

    V''(0) = S2/S - (S1/S)^2

where S = sum Z(k), S1 = sum k Z(k), S2 = sum k^2 Z(k).

**This is exactly the VARIANCE of k under the probability distribution p(k) proportional to Z_CS(k).**

Numerically:
- Mean k = S1/S = 8.966
- <k^2> = S2/S = 238.74
- **V''(0) = Var(k) = 158.35**

---

## 4. Comparison with Other Estimates

| Quantity | Value | Source |
|----------|-------|--------|
| V''(0) = Var(k) | **158.35** | This calculation (exact) |
| A_lattice | 0.024 | Agent 3 lattice estimate |
| A_instanton | 10^{-169} | Agent 1 dilute instanton gas |

- V''(0) / A_lattice = 6,598 (V''(0) is 6,600 times larger)
- V''(0) / A_instanton = 1.58 x 10^{171}

### Critical interpretation

**V''(0) = 158.35 is a DIMENSIONLESS geometric quantity.** It is the variance of the CS level number under the Z_CS distribution. It does not directly give the physical mass without an energy scale.

The physical topological susceptibility is:

    chi_t = V''(0) * Lambda^4

where Lambda is the UV energy scale of the Chern-Simons theory.

If we match to the lattice QCD result chi_t^{1/4} = 75.5 MeV, then:

    Lambda_eff = (chi_t / V''(0))^{1/4} = (75.5 MeV)^4 / 158.35)^{1/4} = 21.3 MeV

This Lambda_eff ~ 21 MeV is **much lower** than Lambda_QCD ~ 200 MeV, reflecting the fact that the CS sum overestimates the curvature by the ratio V''(0)/1 ~ 158 compared to a single-instanton contribution.

---

## 5. Physical Mass m_chi

Using the standard axion mass formula m_a = sqrt(chi_t) / f_a:

| f_a (GeV) | m_chi (eV) | Category |
|------------|------------|----------|
| 10^9 | 5.70 x 10^{-3} | Standard QCD axion window |
| 10^12 | 5.70 x 10^{-6} | Ultralight axion |
| 10^16 | 5.70 x 10^{-10} | GUT-scale, ultralight |

These are the **standard QCD axion masses**, because once we fix chi_t = (75.5 MeV)^4 from lattice, the V''(0) factor is absorbed into the definition of Lambda.

**The CS sum does not change the physical mass; it changes the relationship between the curvature and the energy scale.**

---

## 6. Fourier Structure

The Fourier decomposition of V(theta) shows a slowly decaying power-law spectrum:

    |c_n| ~ 1/(2n) for n = 1, 2, 3, ...

Dominant modes:
- n=1: amplitude 0.3536 (= 1/sqrt(8), exactly Z_CS(1)/2)
- n=2: amplitude 0.1250
- n=3: amplitude 0.0680
- n=61: amplitude 0.00370 (enhanced, marks the CS truncation)
- Beyond n=61: rapid decay

The spectrum is characteristic of -ln of a trigonometric polynomial: the logarithm generates ALL harmonics from a finite sum, with amplitudes decaying as ~1/n.

---

## 7. The 29 Metastable Vacua

The oscillating minima near theta ~ pi represent **metastable CS vacua**. Their properties:

- All 29 are significantly above the global minimum (by 1.88 to 2.18 units)
- Inter-minimum barriers are tiny: mean 0.006, max 0.014
- These would be unstable to quantum tunneling to theta = 0
- The curvatures V'' at these minima range from 10 to 28

The number 29 (not 61) arises because the oscillations only appear in the range |theta| > 0.53 pi, and the spacing is roughly 2 pi / 29 in that region. The central well at theta = 0 absorbs what would otherwise be ~32 oscillations.

---

## 8. Key Physics Conclusions

### A. Where is theta_min?
**theta_min = 0** (CP-conserving vacuum). This is the deepest minimum by a factor ~exp(2) below the oscillating region.

### B. How many minima?
**30 total**: 1 deep global minimum at theta = 0, plus 29 shallow metastable minima near theta = pi (14 on each side, plus one at pi itself which is a local maximum).

### C. What is V''(theta_min)?
**V''(0) = 158.35 (exact analytic result)**, equal to the variance of k under the CS partition function distribution.

### D. Which estimate does it match?
**None of the three.** V''(0) = 158 is:
- 6,600x larger than the lattice estimate A_lat = 0.024
- 10^{171}x larger than the instanton estimate
- A new, purely geometric quantity: the variance of the CS level

However, the **physical mass** is independent of V''(0) once you fix chi_t from lattice QCD. The large V''(0) simply means the effective energy scale Lambda is suppressed: Lambda_eff = 21 MeV instead of Lambda_QCD = 200 MeV.

### E. Potential shape
The potential is **emphatically not cosine-like**. It has:
- A sharp deep well at theta = 0 (width ~ 0.11 rad for harmonic approximation)
- A broad, shallow oscillating plateau near theta = pi
- Barrier height ~ 2.2 in natural units

This non-cosine shape means:
1. Anharmonic corrections are enormous
2. The oscillation spectrum of chi around theta = 0 is NOT purely harmonic
3. Self-interactions of chi are strong
4. The standard misalignment abundance calculation (which assumes cosine) needs significant correction for large initial misalignment angles

---

## 9. Files

- Script: `pk_research/R9_16_exact_potential.py`
- Plot: `pk_research/R9_16_exact_potential.png`
- Data: `pk_research/R9_16_summary.json`
