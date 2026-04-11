# R8 Agent 5: Misalignment Relic Density with Topological Initial Conditions

**Campaign:** R8 (DFD Cosmological Observables)
**Agent:** 5 of 20
**Date:** 2026-04-05
**Status:** COMPLETE

---

## 1. Executive Summary

We compute the relic density of the DFD axion-like field chi from the vacuum misalignment mechanism, using topological initial conditions set by the Chern-Simons vacuum structure. The key results:

1. **Topological average misalignment:** `<theta^2> = 12.43` (correcting the task brief's arithmetic error of 20.6). This is 3.78x larger than the QCD axion value pi^2/3 = 3.29.

2. **Required mass for CDM:** For f_a = 3.93 x 10^16 GeV and <theta^2> = 12.43, the mass giving Omega_chi h^2 = 0.120 is:

   **m_chi = 2.33 x 10^{-26} eV**

   This places chi firmly in the **ultra-ultralight regime**, 10,000 times lighter than fuzzy dark matter (m ~ 10^{-22} eV).

3. **Higgs mechanism mass fails catastrophically:** The mass m_chi ~ 7 x 10^{-10} eV from the alpha-chi coupling to the Higgs overproduces dark matter by a factor of ~10^7. This mechanism is excluded.

4. **The theory needs a mass generation mechanism** that produces m_chi ~ 10^{-26} eV from topological data. If such a mechanism exists, the relic density is a zero-free-parameter prediction.

---

## 2. The Misalignment Mechanism for a General ALP

### 2.1 Setup

The field chi oscillates in a potential V(chi) with:
- Decay constant f_a = M_P / (k+2) = 2.435 x 10^18 / 62 = **3.927 x 10^16 GeV**
- Mass m_chi (to be determined)
- Initial misalignment angle theta_i = chi_i / f_a

### 2.2 Oscillation Temperature

Oscillations begin when m_chi = 3H(T_osc). In the radiation era:

```
H(T) = sqrt(pi^2 g_* / 90) * T^2 / M_P
```

Solving:
```
T_osc = sqrt[ m_chi * M_P / (3 * sqrt(pi^2 g_* / 90)) ]
```

### 2.3 Relic Density Formula

After oscillations begin, chi dilutes as matter:

```
rho_chi(T_0) = (1/2) m_chi^2 f_a^2 theta_i^2 * (g_{*S,0}/g_{*S,osc}) * (T_0/T_osc)^3
```

The relic density parameter:

```
Omega_chi h^2 = rho_chi(T_0) / (rho_crit / h^2)
```

Since T_osc ~ m_chi^{1/2}, the full scaling is:

```
Omega_chi h^2 propto m_chi^{1/2} * f_a^2 * <theta^2>
```

---

## 3. Topological Initial Conditions

### 3.1 CS Vacuum Structure

The Chern-Simons vacua are labeled by n = 0, 1, ..., k_max with k_max = 60. The true minimum is at n = k_max = 60. The misalignment angle for initial vacuum n:

```
theta_n = 2*pi*(k_max - n) / (k_max + 2) = 2*pi*(60 - n) / 62
```

### 3.2 Individual Vacuum Angles

| n | theta_n (rad) | theta_n^2 | Physical interpretation |
|---|---------------|-----------|------------------------|
| 0 | 6.081 | 36.97 | Maximally misaligned |
| 1 | 5.979 | 35.75 | Near-maximal |
| 10 | 5.067 | 25.68 | Large misalignment |
| 20 | 4.054 | 16.43 | Moderate-large |
| 30 | 3.040 | 9.24 | Moderate (~pi) |
| 40 | 2.027 | 4.11 | Moderate-small |
| 50 | 1.013 | 1.03 | Small |
| 55 | 0.507 | 0.26 | Very small |
| 59 | 0.101 | 0.010 | Near minimum |
| 60 | 0.000 | 0.000 | At minimum |

### 3.3 Average Over Vacua

If inflation does not select a specific vacuum, we average over all 61 vacua:

```
<theta^2> = (1/61) * sum_{n=0}^{60} [2*pi*(60-n)/62]^2
          = (2*pi/62)^2 * (1/61) * sum_{m=0}^{60} m^2
          = (2*pi/62)^2 * (1/61) * 60*61*121/6
          = 0.010270 * 73810/61
          = 0.010270 * 1210.0
          = 12.427
```

**Correction to task brief:** The brief stated <theta^2> = 20.6, which contained an arithmetic error (733940 instead of 73810 in the sum of squares). The correct value is **<theta^2> = 12.43**.

**Enhancement over QCD axion:** 12.43 / (pi^2/3) = 12.43 / 3.29 = **3.78x**

### 3.4 On Modular Reduction

A subtle issue: for a standard cosine potential V = Lambda^4[1 - cos(theta)] with period 2*pi, angles should be reduced modulo 2*pi to [-pi, pi]. Under modular reduction:

```
<theta^2>_mod = 3.35
```

This is close to the QCD value, because many high-n vacua map to small physical angles. Whether modular reduction applies depends on the shape of the DFD potential:

- **Scenario A (extended potential):** The CS topological potential is not simply periodic. The 61 vacua represent distinct topological sectors with energy V(n) that increases monotonically away from n = k_max. No modular reduction: **<theta^2> = 12.43**.

- **Scenario B (cosine potential):** If the effective potential has the standard axion form V ~ [1 - cos(theta)], modular reduction applies: **<theta^2> = 3.35**.

We present results for both scenarios.

---

## 4. Results: Required Mass for Omega_CDM

### 4.1 Mass Scan

Using f_a = 3.927 x 10^16 GeV and <theta^2> = 12.43 (Scenario A):

| m_chi (eV) | Omega_chi h^2 | Status |
|------------|---------------|--------|
| 10^{-28} | 7.85 x 10^{-3} | Under |
| 10^{-26} | 7.85 x 10^{-2} | Under |
| 10^{-24} | 7.85 x 10^{-1} | Over |
| 10^{-22} | 7.85 | Over (>>1) |
| 10^{-20} | 78.5 | Over (>>>1) |

### 4.2 Target Mass (Binary Search)

**Scenario A** (<theta^2> = 12.43, extended potential):

```
m_chi = 2.335 x 10^{-26} eV
T_osc = 5.59 eV (below neutrino decoupling, g_* = 3.36)
Omega_chi h^2 = 0.120
```

**Scenario B** (<theta^2> = 3.35, cosine potential):

```
m_chi = 3.221 x 10^{-25} eV
T_osc = 20.8 eV (below neutrino decoupling, g_* = 3.36)
Omega_chi h^2 = 0.120
```

### 4.3 Properties of the Target Mass

| Property | Scenario A | Scenario B |
|----------|-----------|-----------|
| m_chi (eV) | 2.33 x 10^{-26} | 3.22 x 10^{-25} |
| T_osc (eV) | 5.6 | 20.8 |
| T_osc / T_eq | 7.4 | 27.7 |
| Compton lambda | 274 pc | 20 pc |
| de Broglie lambda (v=10^{-3}c) | 274 kpc | 20 kpc |

Both scenarios give oscillation onset in the radiation era (T_osc > T_eq ~ 0.75 eV), validating the calculation.

### 4.4 Consistency Check

For T_osc ~ 5.6 eV (Scenario A), this is in the post-BBN, post-neutrino-decoupling epoch. The assumption of radiation domination is valid. The g_* = 3.36 (photons + 3 neutrino species at low T) is appropriate.

---

## 5. Comparison with Known Mass Mechanisms

### 5.1 Higgs Mechanism Mass

From the alpha-chi coupling:
```
d(alpha)/d(chi) = alpha / (f_a * (k+2)) = (1/137) / (3.93e16 * 62) = 3.0 x 10^{-21} GeV^{-1}
```

Induced mass:
```
m_chi(Higgs) ~ d(alpha)/d(chi) * v_H = 3.0e-21 * 246 = 7.4 x 10^{-19} GeV = 7.4 x 10^{-10} eV
```

Relic density:
```
Omega_chi h^2 = 1.05 x 10^7  (Scenario A)
              = 2.81 x 10^6  (Scenario B)
```

**VERDICT: Excluded.** Overproduces dark matter by 7-8 orders of magnitude. The Higgs mechanism mass is far too large (by a factor ~10^{16} above the target).

### 5.2 What Mass Scale is Needed?

For Scenario A, m_chi = 2.33 x 10^{-26} eV = 2.33 x 10^{-35} GeV. If this comes from an instanton-like mechanism m = Lambda^2/f_a:

```
Lambda_CS = sqrt(m * f_a) = sqrt(2.33e-35 * 3.93e16) = 9.6 x 10^{-10} GeV ~ 1 neV energy scale
```

This is an extraordinarily low scale, far below any known particle physics scale.

### 5.3 Parametric Dependence: m_chi(target) vs f_a

| f_a (GeV) | m_chi for Omega_CDM (eV) | T_osc (GeV) |
|------------|--------------------------|-------------|
| 10^{10} | 23.1 | 7.4 x 10^4 |
| 10^{12} | 2.3 x 10^{-7} | 7.4 |
| 10^{14} | 7.3 x 10^{-16} | 4.2 x 10^{-4} |
| 10^{16} | 5.6 x 10^{-24} | 3.6 x 10^{-8} |
| **3.93 x 10^{16}** | **2.3 x 10^{-26}** | **5.6 x 10^{-9}** |
| 10^{17} | 5.6 x 10^{-28} | 3.6 x 10^{-10} |
| 10^{18} | 1.0 x 10^{-30} | 1.5 x 10^{-11} |

The extreme GUT-scale f_a = 3.93 x 10^{16} GeV demands an extremely low mass, scaling as m ~ f_a^{-4} (since Omega ~ m^{1/2} f_a^2).

---

## 6. Omega_chi for Specific Initial Vacua

If the universe starts in a specific CS vacuum n (e.g., selected by inflation), the relic density varies dramatically. Using m_chi = 2.335 x 10^{-26} eV (the vacuum-averaged target):

| n | theta_n | Omega_chi h^2 | Omega/Omega_CDM |
|---|---------|---------------|-----------------|
| 0 | 6.08 | 0.357 | 2.98 |
| 1 | 5.98 | 0.345 | 2.88 |
| 5 | 5.57 | 0.300 | 2.50 |
| 10 | 5.07 | 0.248 | 2.07 |
| 20 | 4.05 | 0.159 | 1.32 |
| **30** | **3.04** | **0.0893** | **0.74** |
| 40 | 2.03 | 0.0397 | 0.33 |
| 50 | 1.01 | 0.00992 | 0.083 |
| 59 | 0.10 | 9.9 x 10^{-5} | 8.3 x 10^{-4} |
| 60 | 0.00 | 0 | 0 |

**Notable:** No single vacuum gives exactly Omega_CDM with this mass. The n ~ 20 vacuum gives Omega h^2 = 0.159, closest to 0.120 for individual vacua.

---

## 7. Anharmonic Corrections

For large theta_i (near pi), the harmonic approximation (V ~ m^2 theta^2 / 2) breaks down. The anharmonic correction factor for a cosine potential:

```
f(theta) = [ln(1/(1 - (theta_eff/pi)^2))]^{7/6}
```

where theta_eff is the angle reduced to [0, pi].

| n | theta_raw | theta_eff | f_anharmonic |
|---|-----------|-----------|-------------|
| 30 | 3.040 | 3.040 (near pi) | 3.26 |
| 20 | 4.054 | 2.230 | 0.66 |
| 10 | 5.067 | 1.216 | 0.12 |
| 5 | 5.574 | 0.709 | 0.032 |
| 0 | 6.081 | 0.203 | 0.0017 |

For the vacuum-averaged case, anharmonic corrections are important for the n ~ 30 vacua (where theta ~ pi) and tend to increase the relic density by factors of 2-3 for those vacua. A full treatment would require solving the equation of motion numerically in the anharmonic potential.

---

## 8. Physical Interpretation

### 8.1 Ultra-Ultralight Dark Matter

The required mass m_chi ~ 2.3 x 10^{-26} eV places this field ~10^4 below the fuzzy DM scale:

| | DFD chi | QCD axion | Fuzzy DM |
|--|---------|-----------|----------|
| f_a (GeV) | 3.93 x 10^{16} | ~10^{12} | ~10^{17} |
| <theta^2> | 12.4 | 3.3 | ~1 |
| m for Omega_CDM (eV) | 2.3 x 10^{-26} | ~6 x 10^{-6} | ~10^{-22} |
| de Broglie lambda | ~270 kpc | ~0.1 pc | ~1 kpc |
| Compton lambda | ~270 pc | ~0.1 mpc | ~1 pc |

### 8.2 Observational Constraints

At m ~ 10^{-26} eV with de Broglie wavelength ~270 kpc:
- **Structure formation:** The Jeans scale is ~Mpc, suppressing structure on galactic scales. This is in severe tension with observed small-scale structure (dwarf galaxies, Lyman-alpha forest).
- **CMB constraints:** Ultra-ultralight fields with m < 10^{-24} eV are strongly constrained by CMB observations (Planck + ACT), which require m > 10^{-24} eV at 95% CL for fields constituting all of CDM.
- **Galaxy formation:** The soliton core radius scales as r_c ~ 1/(m * v), giving ~Mpc cores, incompatible with observed galaxy rotation curves.

**This mass is observationally excluded as the sole dark matter component.**

### 8.3 Possible Resolutions

1. **Chi is a subdominant component:** If chi contributes only a fraction f_chi of the dark matter, the constraint relaxes to m > 10^{-24} * f_chi^{some power} eV, still problematic.

2. **The mass is not 10^{-26} eV:** If topology determines a larger mass (from Agent 3's CS partition function calculation), the relic density could still match observations.

3. **f_a is smaller:** If f_a ~ 10^{12} GeV (QCD axion scale) rather than M_P/62, then m ~ 10^{-7} eV would give Omega_CDM, well within allowed parameter space.

4. **Post-inflationary scenario:** If PQ symmetry breaks after inflation, the average <theta^2> is replaced by domain-wall contributions, potentially changing the result.

5. **Non-standard cosmological history:** Late entropy injection between T_osc and today would dilute the relic density, allowing a heavier (more viable) mass.

---

## 9. Key Question: Is Omega_chi a Zero-Parameter Prediction?

The answer depends entirely on whether Agent 3 can derive m_chi from the CS partition function.

### If m_chi is topologically determined:

- f_a = M_P/(k+2) = 3.93 x 10^16 GeV (from topology: k_max = 60)
- <theta^2> = 12.43 (from topology: 61 CS vacua)
- m_chi = ??? (from CS partition function)
- Then Omega_chi h^2 is a **zero-free-parameter prediction**

### The required m_chi for Omega_CDM:
```
m_chi = 2.335 x 10^{-26} eV  (Scenario A)
m_chi = 3.221 x 10^{-25} eV  (Scenario B)
```

### Verdict on the Higgs mechanism mass:
```
m_chi(Higgs) = 7.4 x 10^{-10} eV  -->  Omega h^2 ~ 10^7  EXCLUDED
```

The Higgs mechanism mass overshoots by ~10^7. If this is the only mass generation mechanism, chi CANNOT be cold dark matter -- it would dominate the universe's energy density by many orders of magnitude.

---

## 10. Summary Table

| Quantity | Value | Source |
|----------|-------|--------|
| k_max | 60 | DFD topology |
| f_a | 3.927 x 10^16 GeV | M_P/(k+2), Agent 2 |
| Number of CS vacua | 61 | k_max + 1 |
| <theta^2> (extended) | 12.43 | Vacuum average (Scenario A) |
| <theta^2> (cosine) | 3.35 | Vacuum average (Scenario B) |
| Enhancement over QCD | 3.78x (A), 1.02x (B) | |
| m_chi for Omega_CDM | 2.3 x 10^{-26} eV (A) | This calculation |
| m_chi for Omega_CDM | 3.2 x 10^{-25} eV (B) | This calculation |
| m_chi (Higgs mech.) | 7.4 x 10^{-10} eV | alpha-chi coupling |
| Omega(Higgs mass) | ~10^7 | **EXCLUDED** |
| T_osc (target mass) | 5.6 eV (A), 20.8 eV (B) | Radiation era |
| de Broglie lambda | 270 kpc (A), 20 kpc (B) | v = 10^{-3} c |

---

## 11. Conclusions and Implications for Other Agents

1. **For Agent 3 (mass calculation):** The required mass m_chi ~ 10^{-26} to 10^{-25} eV is extraordinarily small. If the CS partition function gives a significantly different mass, chi either over- or under-produces dark matter.

2. **For Agent 2 (decay constant):** The f_a = 3.93 x 10^16 GeV baseline gives viable cosmology ONLY if m_chi ~ 10^{-26} eV. Lower f_a dramatically relaxes the mass requirement (m ~ f_a^{-4}).

3. **For Agents working on observational signatures:** The ultra-ultralight mass regime (m < 10^{-24} eV) is in tension with structure formation constraints. This is a critical test of the theory.

4. **For the overall campaign:** The misalignment mechanism with DFD parameters generically overproduces dark matter unless the mass is tuned to an extremely small value. The Higgs mechanism mass is excluded by 7 orders of magnitude. This suggests either (a) a different mass mechanism is needed, (b) f_a is not M_P/62, or (c) chi is not the dark matter.

---

*Agent 5 computation complete. All numerical results verified by independent binary search and cross-checked against analytic scaling relations.*
