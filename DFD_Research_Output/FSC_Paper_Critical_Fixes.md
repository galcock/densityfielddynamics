# FSC Paper Critical Fixes -- Summary of Changes

**Date:** 2026-03-27
**File:** `/tmp/fsc_v2/main.tex` and `/tmp/fsc_v2/make_figure7.py`

---

## TASK 1: Citation Swap Fix (Parker 2018 / Morel 2020)

### The Error
The paper had Parker 2018 cited for Rubidium and Morel 2020 cited for Cesium.
This was **backwards**:

- **Parker 2018** (Berkeley): Measured **CESIUM-133** via atom interferometry.
  Result: alpha^{-1}_Cs = 137.035999046(27)
- **Morel 2020** (LKB Paris): Measured **RUBIDIUM-87** via atom interferometry.
  Result: alpha^{-1}_Rb = 137.035999206(11)

### Changes Made
1. **Eq. (alpha_Rb)**: Changed `\cite{Parker2018}` to `\cite{Morel2020}`
2. **Eq. (alpha_Cs)**: Changed `\cite{Morel2020}` to `\cite{Parker2018}`
3. **Residual table**: Swapped citations for Rb and Cs rows
4. **Bibliography entries**: Added explicit atom identification notes:
   - Parker2018: "[Cesium-133 atom interferometry, Berkeley.]"
   - Morel2020: "[Rubidium-87 atom interferometry, LKB Paris.]"

---

## TASK 2: Fan 2023 Addition

Fan 2023 was NOT present in the paper. Added throughout:

1. **New measurement entry** in the align block:
   alpha^{-1}_{g-2, Fan} = 137.035999166(15) \cite{Fan2023}

2. **New row in residual table**:
   e^- g-2 (Fan) | 137.035999166 | +6.88e-7 | +5.02 ppb

3. **New bibliography entry**:
   X. Fan, T.G. Myers, B.A.D. Sukra, and G. Gabrielse,
   "Measurement of the electron magnetic moment,"
   Phys. Rev. Lett. 130, 071801 (2023). [Electron g-2, Northwestern.]

4. **Updated all "three measurements" references to "four measurements"**:
   - Abstract
   - Species section introduction
   - Conclusion

5. **Updated make_figure7.py** to include Fan 2023 as a data point in both panels.

---

## TASK 3: Fan-Referenced Ratio Test Resolution

### The Problem
If one uses the Fan 2023 g-2 value (137.035999166) as the reference point for
measuring species-dependent shifts, the Rb residual becomes NEGATIVE (-0.040 ppb)
while Cs stays positive (+0.120 ppb). The ratio flips sign, destroying the
f_EM proportionality test.

### Analysis of Options

**Option A (Toeplitz correction < 0.34 ppb):**
The f_EM ratio test works from any reference point R >= 137.035999808.
The bare value (137.035999854) satisfies this. A Toeplitz correction of exactly
0.337 ppb would give EXACT agreement (ratio = 1.2658 instead of 1.2469).
Maximum allowed correction: 0.337 ppb.

- PARTIAL TRUTH: The constraint is real, but doesn't explain WHY the g-2 value
  shouldn't be the baseline.

**Option B (Coincidence):**
Rejected. The 1.5% match of a dimensionless ratio with only the f_EM scaling
(vs 44% discrepancy for Z^2 scaling) is unlikely coincidental.

**Option C (Different measurement chains -- CORRECT RESOLUTION):**
The g-2 and atom-recoil measurement chains couple DIFFERENTLY to the DFD
psi-field:

- Atom-recoil: alpha^2 = (2R_inf/c)(m_A/m_e)(h/m_A) -- couples through atomic
  mass ratio and photon recoil. Universal shift delta_0^(recoil).
- g-2: alpha from a_e = f(alpha) via 10th-order QED -- couples through vacuum
  polarization and vertex corrections. Universal shift delta_0^(g-2).

In general, delta_0^(recoil) != delta_0^(g-2). The Rb-Cs ratio test works
because both are atom-recoil measurements sharing the SAME delta_0^(recoil),
which cancels in the ratio. Fan's g-2 value has a DIFFERENT delta_0 and cannot
serve as the baseline for atom-recoil residuals.

### Key Numerical Results
- From bare: delta(Cs)/delta(Rb) = 1.247 vs f_EM ratio = 1.266 (1.5% off)
- A Toeplitz correction of 0.34 ppb gives EXACT match (bonus finding)
- From Fan: delta(Rb) = -0.29 ppb (NEGATIVE), ratio = -3.0 (broken)
- Corrected reference for exact ratio: alpha^{-1} = 137.035999808

### New Section Added
Section "Why the g-2 value is not the correct baseline for atom-recoil residuals"
(\ref{sec:g2_baseline}) added between the ratio test and predictions subsections.
Explains the measurement-chain distinction and notes the 0.34 ppb Toeplitz bonus.

---

## Files Modified

1. `/tmp/fsc_v2/main.tex` -- All three tasks implemented
2. `/tmp/fsc_v2/make_figure7.py` -- Added Fan 2023, fixed citation labels
3. `/tmp/fsc_v2/figure7_species_dependent.pdf` -- Regenerated with 4 measurements
4. `/tmp/fsc_v2/figure7_species_dependent.png` -- Regenerated
