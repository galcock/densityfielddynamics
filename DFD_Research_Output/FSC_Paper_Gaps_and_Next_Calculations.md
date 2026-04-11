# DFD Fine Structure Constant Paper: Gaps, Errors, and Next Calculations

**Date:** 2026-03-27
**Subject:** Critical review of "Ab Initio Derivation of the Fine Structure Constant from Density Field Dynamics"
**Purpose:** Identify factual errors, analytical gaps, and prioritized next calculations

---

## 1. CRITICAL ERROR: Morel/Parker Citation Swap

### The Problem

The paper attributes the Rb measurement to Parker (2018, Berkeley) and the Cs measurement to Morel (2020, LKB Paris). This is **backwards**.

**Verified experimental facts:**
- **Parker et al. 2018 (Berkeley):** Measured alpha using **cesium-133** atom recoil. Result: alpha^{-1} = 137.035999046(27). Published in Science, April 2018.
- **Morel et al. 2020 (LKB Paris):** Measured alpha using **rubidium-87** atom recoil. Result: alpha^{-1} = 137.035999206(11). Published in Nature, December 2020.

### Why This Matters

This is not a minor typo. It would be the first thing any experimentalist checks, and getting it wrong instantly destroys credibility. Reviewers at PRL or Nature Physics will reject on this alone. The Morel and Parker groups are the two most prominent atom-recoil teams in the world; confusing which atom they used signals unfamiliarity with the experimental literature.

### Impact on the Analysis

The **numerical values** in the paper are likely correct (the alpha^{-1} numbers are right, just attributed to the wrong groups). This means the species-dependent analysis may survive the correction, but the text, citations, and any discussion referencing "the Rb experiment by Parker" or "the Cs experiment by Morel" must be inverted throughout.

**Specifically:** If the paper argues that heavier nuclei (Cs, Z=55) produce larger shifts than lighter nuclei (Rb, Z=37), then the correct assignment is:
- Cs (Z=55, A=133): alpha^{-1} = 137.035999046 (Parker 2018, Berkeley)
- Rb (Z=37, A=87): alpha^{-1} = 137.035999206 (Morel 2020, LKB Paris)

This means **Cs gives the LOWER alpha^{-1}** and **Rb gives the HIGHER alpha^{-1}**. Whether this is consistent with delta proportional to f_EM (where f_EM scales with nuclear coupling) depends on the sign convention for the species-dependent shift.

### How to Fix

1. Swap all Rb/Cs attributions throughout the paper
2. Verify that Table 5 predictions assign the correct alpha^{-1} value to the correct atom
3. Re-examine the ratio test delta(Cs)/delta(Rb) with correct assignments
4. Update all citation references

---

## 2. Two-Component Model: Predictions Must Reference the Corrected Value

### The Problem

The paper's Table 5 predictions use the species-dependent coupling constant C = delta/f_EM measured from the **bare DFD value** alpha^{-1}_bare = 137.035999854. But if the Toeplitz correction is physical, then the universal (species-independent) part has already been subtracted, and species-dependent shifts should be measured from the **corrected value** (Fan 2023).

### Recomputation Referenced to Fan 2023

Fan et al. 2023 (electron g-2): alpha^{-1} = 137.035999166(15)

Species-dependent residuals referenced to Fan:
- delta_species(Rb) = 137.035999166 - 137.035999206 = **-0.040** (i.e., Rb is 0.040 ABOVE Fan)
- delta_species(Cs) = 137.035999166 - 137.035999046 = **+0.120** (i.e., Cs is 0.120 BELOW Fan)

Compare to residuals referenced to bare DFD value (137.035999854):
- delta(Rb) from bare = 137.035999854 - 137.035999206 = +0.648
- delta(Cs) from bare = 137.035999854 - 137.035999046 = +0.808

### Critical Differences

1. **Sign flip for Rb:** Referenced to Fan, the Rb residual is NEGATIVE (Rb measures alpha^{-1} higher than Fan). Referenced to bare, both residuals are positive.

2. **Ratio test changes:**
   - From bare: delta(Cs)/delta(Rb) = 0.808/0.648 = 1.247
   - From Fan: delta(Cs)/delta(Rb) = 0.120/(-0.040) = -3.0

   The ratio **changes sign** when referenced to Fan. This means the linear fit delta = C * f_EM cannot work in the same way. Either:
   - (a) The two-component decomposition is wrong
   - (b) The species-dependent shifts should NOT be referenced to Fan but to some intermediate value
   - (c) The Fan value itself contains species-dependent contamination (it comes from electron g-2, which involves virtual hadronic contributions that are nuclear-species-independent, so this escape route is unlikely)

3. **The f_EM proportionality test breaks down.** If Rb and Cs residuals have opposite signs relative to Fan, then no monotonic function of nuclear properties (Z, A, f_EM) can fit both.

### Why This Matters

This is the most important consistency check in the paper. The three-layer structure (bare -> Toeplitz corrected -> species-dependent) requires that the species-dependent shifts be small perturbations around the corrected value. If the corrected value (Fan) falls BETWEEN the Rb and Cs measurements, the species-dependent model must explain why one atom shifts up and one shifts down. This is still physically possible (the nuclear coupling could have either sign depending on nuclear structure) but it requires a more sophisticated model than simple proportionality to f_EM.

### How to Compute

1. Define delta_i = alpha^{-1}(Fan) - alpha^{-1}(atom i) for each atom
2. Plot delta_i vs f_EM(atom i) for Rb and Cs
3. Test whether a linear fit through the origin works
4. If not, test whether a linear fit with nonzero intercept works (this would indicate the Fan value has a systematic offset)
5. Re-derive predictions for Sr, Yb using whatever fit works

---

## 3. Hoang et al. 2019/2020: The Cooper Pair Mass Anomaly Has Changed

### The Problem

The DFD prediction for the Cooper pair mass anomaly is delta = sqrt(3) * alpha^2 = 92.23 ppm. This was consistent with the original Tate et al. (1989/1990) measurement of 84 +/- 21 ppm (the DFD prediction falls within the 1-sigma error bar).

However, Hoang, Abe, Takahashi et al. (Materials Letters, 2020) repeated the measurement using rotating spherical-shell superconductors at ultra-low temperature (10^{-4} K) with 6 different type-I superconductors. For niobium, their result is:

**Hoang Nb result: 18 +/- 2.1 ppm**

This is a dramatic reduction from Tate's 84 ppm and is now in severe tension with the DFD prediction of 92.23 ppm:

**Tension: (92.23 - 18) / 2.1 = 35 sigma**

### Why This Matters

A 35-sigma discrepancy is fatal if taken at face value. The paper currently presents the Tate result as supporting evidence for DFD. Including Hoang would transform this from a success into a crisis.

### Possible Resolutions

1. **Systematic differences between experiments:** Tate used a cylindrical geometry; Hoang used spherical shells. If the anomaly depends on geometry (e.g., through boundary conditions for the London moment), the DFD prediction may apply only to specific configurations.

2. **Temperature dependence:** Tate measured at ~2K (well below Nb T_c = 9.25K but not ultra-low). Hoang measured at 10^{-4} K. If the anomaly has temperature dependence (e.g., through thermal population of the quintet channel), the two measurements probe different regimes.

3. **The DFD prediction is wrong:** The sqrt(3) * alpha^2 derivation from the quintet exchange channel may have an error, or the A5 microsector mechanism may not be the correct explanation.

4. **Material purity / vortex effects:** Different superconductor samples can have different defect densities, which affect vortex pinning and can produce systematic shifts in London moment measurements.

### How to Address

1. Cite Hoang et al. explicitly and state the tension
2. Analyze whether geometry or temperature effects could explain the 74 ppm difference
3. If DFD predicts a specific temperature dependence for the quintet channel occupation, calculate it and compare
4. Consider whether the prediction should be delta = sqrt(3) * alpha^2 * T_dependence(T/T_c)

### Reference

Hoang, C.M., Abe, M., Takahashi, Y., et al. "High-precision measurement of Cooper-pair mass using rotating spherical-shell superconductor." Materials Letters 261 (2020): 127073.

---

## 4. Lattice Monte Carlo: L=16 Anomaly

### The Problem

The paper reports that 9/10 lattice MC runs at L=16 converge, but the mean is +1.13% from the physical alpha^{-1} value. This is WORSE than L=12, which gives -0.08%. In standard finite-size scaling, larger lattices should give results closer to the continuum limit, not farther.

### Why This Matters

This anti-scaling behavior suggests one of:

1. **Underthermalisation:** 40k thermalisation sweeps may be insufficient at L=16. The autocorrelation time typically scales as tau ~ L^z with z >= 2 for local algorithms. Going from L=12 to L=16 increases the required thermalisation by a factor of (16/12)^z >= 1.78 for z=2, or >= 3.16 for z=3 (critical slowing down). If L=12 needed ~20k sweeps, L=16 might need 35k-63k. The paper reports 40k, which is marginal.

2. **Phase transition or crossover:** There may be a bulk phase transition near L=16 in this lattice action. SU(2) lattice gauge theory has a well-known bulk transition at certain bare coupling values. If the simulation parameters place L=16 near this transition, the results would show anomalous fluctuations and poor convergence.

3. **Finite-size effects that are non-monotonic:** If the lattice action has competing terms with different finite-size scaling exponents, the total error could be non-monotonic in L. This is unusual but not impossible.

### How to Diagnose

1. **Autocorrelation analysis:** Measure the integrated autocorrelation time tau_int for the observable at L=12 and L=16. If tau_int(L=16) >> tau_int(L=12) * (16/12)^2, there is a sign of critical slowing down or proximity to a phase transition.

2. **Thermalisation study:** Run L=16 with 80k, 120k, and 160k thermalisation sweeps. If the +1.13% offset decreases, the problem is underthermalisation.

3. **Plaquette distribution:** Plot the plaquette expectation value distribution at L=16. A bimodal distribution indicates a first-order phase transition.

4. **Monotonicity test at L=14:** Run at L=14 to see if the error is monotonically increasing from L=12 or if L=16 is a specific anomaly.

5. **Run L=24 and L=32:** The paper needs to demonstrate that the finite-size scaling behavior is under control. Without this, the lattice evidence is inconclusive.

---

## 5. The b_0 Value: Section 6.6 vs. Unified Theory

### The Problem

The fine structure constant paper uses b_0 = 9 in Section 6.6 (for the magnitude gap analysis). The unified theory's section_gauge_coupling.tex uses b_3 = -7.

### Resolution: Both Can Be Correct (Different N_f)

The standard one-loop beta function coefficient for SU(3) is:

b_3 = -(11 - 2N_f/3)

where N_f is the number of active quark flavors.

| N_f | b_3 | |b_3| |
|-----|-----|-------|
| 0   | -11 | 11    |
| 2   | -11 + 4/3 = -29/3 | 9.67 |
| 3   | -11 + 2 = -9 | 9 |
| 4   | -11 + 8/3 = -25/3 | 8.33 |
| 5   | -11 + 10/3 = -23/3 | 7.67 |
| 6   | -11 + 4 = -7 | 7 |

So:
- **b_0 = 9 (FSC paper, Section 6.6):** Corresponds to N_f = 3 (u, d, s quarks active). This is appropriate at the nuclear energy scale (~1 GeV) relevant for the species-dependent coupling.
- **b_3 = -7 (unified theory):** Corresponds to N_f = 6 (all quarks active). This is appropriate at high energies where all quarks contribute to the running, which is the context of gauge unification.

### The Real Issue: Sign and Enhancement Factor

The 4400x enhancement factor comes from the chain:

delta(alpha_EM) -> delta(alpha_s) via RG -> delta(Lambda_QCD) via dimensional transmutation -> delta(nuclear binding)

Each step has a specific coefficient:
1. alpha_s/alpha_EM ~ 16 (coupling ratio)
2. 2*pi/(|b_3| * alpha_s) ~ 7.6 (dimensional transmutation amplification, using |b_3|=7)
3. Nuclear structure enhancement K ~ 30-40 (model-dependent)

Product: 16 * 7.6 * 36 ~ 4400

But with |b_3| = 9 (N_f = 3), step 2 becomes 2*pi/(9 * 0.118) ~ 5.9, and the product becomes:

16 * 5.9 * 36 ~ 3400

**The choice of N_f matters at the ~30% level for the enhancement factor.** The paper must be explicit about which N_f is used and why.

### How to Fix

1. State explicitly that b_0 = 9 corresponds to N_f = 3 at the nuclear scale
2. Note that the unified theory uses b_3 = 7 for N_f = 6 at high energies
3. Clarify that the enhancement factor in Section 6.6 should use the nuclear-scale value
4. Recompute the enhancement with both values and report the range

---

## 6. Prioritized Next Calculations

### Priority A: Compute c_1 (Toeplitz Two-Loop Coefficient) from CP^2 Geometry

**Why it matters:** The entire three-layer structure stands or falls on whether the Toeplitz correction is calculable. If c_1 can be derived from the Bergman kernel on CP^2, it transforms the theory from a one-parameter fit to a zero-parameter prediction.

**How to compute:**
- CP^2 is a homogeneous Kahler manifold with Fubini-Study metric
- The Bergman kernel B_k on CP^2 has an EXACT expansion (not asymptotic) because CP^2 = SU(3)/U(2) is a symmetric space
- The Tian-Yau-Zelditch expansion gives B_k = (k+1)(k+2)/2 * (1/Vol) * [1 + b_1/k + b_2/k^2 + ...]
- For CP^2 with Fubini-Study metric: b_1 = scalar_curvature/(4*pi*n) where n=2 (complex dimension)
- The scalar curvature of CP^2 with Fubini-Study metric is R = 12 (in standard normalization where R_ij = 6*g_ij)
- This gives b_1 = 12/(4*pi*2) = 3/(2*pi) or b_1 = 3 depending on normalization
- The question is how b_1, b_2 enter the spectral action trace that gives the coupling constant

**Key computation:** Evaluate Tr[f(D^2/Lambda^2)] on the Dirac operator D on the spectral triple built from CP^2, carrying the TYZ coefficients through the heat kernel expansion. The c_1 coefficient in the alpha prediction is a specific combination of b_1 and b_2.

**Expected timeline:** This is a well-defined mathematical calculation that could be completed in days if the spectral triple is correctly specified.

### Priority B: Derive kappa_s = alpha_s/4 from Non-Abelian Gauge Emergence

**Why it matters:** The EM result kappa = alpha/4 (verified in the vacuum loading paper) needs to extend to SU(3) to close the remaining x4000 gap between DFD prediction and nuclear clock observations.

**How to compute:**
- Start from the gauge emergence framework in Appendix of the unified theory
- The EM coupling kappa = alpha^2/(2*pi) comes from one-loop corrections to the optical metric
- For SU(3), the same mechanism gives kappa_s = alpha_s^2/(2*pi)
- But the vacuum loading paper derives kappa = alpha/4 (not alpha^2/(2*pi))
- If the non-perturbative mechanism that gives alpha/4 extends to SU(3), it should give kappa_s = alpha_s/4
- With alpha_s ~ 0.118: kappa_s = 0.0295
- The ratio kappa_s/kappa = alpha_s/alpha = 16.2
- Combined with dimensional transmutation (x7.6) and nuclear structure (x30-40): total enhancement ~ 16.2 * 7.6 * 35 ~ 4300

This is tantalisingly close to the required x4000 factor.

### Priority C: Nuclear Structure Enhancement K(A,Z) for Rb-87 and Cs-133

**Why it matters:** The species-dependent shifts (gap 2) cannot be predicted without knowing how sensitive each nucleus is to changes in alpha_s and Lambda_QCD.

**How to compute:**
- K(A,Z) parametrises how nuclear binding energies respond to changes in fundamental constants
- For the semi-empirical mass formula: E_binding = a_V*A - a_S*A^{2/3} - a_C*Z(Z-1)/A^{1/3} - a_A*(A-2Z)^2/A + delta_pairing
- Each coefficient depends differently on alpha_s and Lambda_QCD
- The Coulomb term a_C depends directly on alpha_EM
- The volume and surface terms depend on Lambda_QCD through the nuclear force range
- For Rb-87 (Z=37, A=87): compute dE/d(alpha_s) and dE/d(alpha_EM)
- For Cs-133 (Z=55, A=133): same computation
- The RATIO K(Cs)/K(Rb) determines whether the species-dependent model's predictions for delta(Cs)/delta(Rb) are correct
- More sophisticated: use nuclear shell model to check for near-degeneracies that could amplify the response

### Priority D: Run L=24 and L=32 Lattice Simulations

**Why it matters:** The L=16 anomaly (gap 4) must be resolved before the lattice evidence can be cited as support.

**How to compute:**
- Use the same lattice action as the existing code (available in dfd_alpha_release/)
- For L=24: estimate thermalisation requirement as 40k * (24/16)^3 ~ 135k sweeps (assuming z=3 for critical slowing)
- For L=32: ~320k sweeps
- Run 10 independent streams at each L for statistical control
- Compute the integrated autocorrelation time at each L
- Plot alpha^{-1}(L) vs 1/L^2 (or 1/L) and fit the continuum extrapolation
- If L=16 is an outlier, determine whether it sits near a bulk phase transition

### Priority E: Test Atom-Recoil Linear Fit Referenced to Fan 2023

**Why it matters:** This is the consistency check described in gap 2. If the linear fit fails when referenced to Fan, the three-layer model needs revision.

**How to compute:**
1. Tabulate: {atom, Z, A, alpha^{-1}_measured, f_EM(Z,A)}
   - Rb-87: alpha^{-1} = 137.035999206, Z=37, A=87
   - Cs-133: alpha^{-1} = 137.035999046, Z=55, A=133
2. Compute delta_i = alpha^{-1}(Fan) - alpha^{-1}(atom_i)
   - delta(Rb) = 137.035999166 - 137.035999206 = -0.040
   - delta(Cs) = 137.035999166 - 137.035999046 = +0.120
3. Plot delta vs f_EM and test for linearity
4. With only two points, the "fit" is trivially determined, but the sign flip for Rb is the critical issue
5. If both had the same sign, extrapolation to Sr and Yb would be straightforward
6. With opposite signs, the model must accommodate sign changes, which means f_EM is not the right variable (or it needs a constant offset)

---

## 7. Summary: Urgency Ranking

| # | Gap | Severity | Effort | Impact |
|---|-----|----------|--------|--------|
| 1 | Morel/Parker swap | CRITICAL (paper-killing) | 1 hour | Must fix before any submission |
| 2 | Predictions referenced to Fan | HIGH | 1 day | Changes all four atom-recoil predictions |
| 3 | Hoang et al. 35-sigma tension | HIGH | 1 week | Must address or remove Cooper pair claim |
| 4 | L=16 lattice anomaly | MEDIUM | 2-4 weeks (compute time) | Weakens lattice support until resolved |
| 5 | b_0 convention | LOW | 2 hours | Affects enhancement factor by ~30% |
| 6a | c_1 from CP^2 | HIGH (next paper) | 1-2 weeks | Upgrades from fit to prediction |
| 6b | kappa_s = alpha_s/4 | HIGH (next paper) | 1-2 weeks | Closes the x4000 gap |
| 6c | Nuclear K(A,Z) | MEDIUM | 2-4 weeks | Enables quantitative species predictions |
| 6d | L=24,32 lattice runs | MEDIUM | 2-4 weeks | Resolves finite-size scaling |
| 6e | Fan-referenced linear fit | HIGH | 1 day | Critical consistency check |

**Bottom line:** Items 1 and 2 must be fixed before the paper is submitted anywhere. Item 3 (Hoang) must at least be acknowledged and discussed. Items 4 and 5 are important but not paper-killing. The Priority A-E calculations in section 6 represent the natural next phase of the research programme.

---

## Sources

- [Parker et al. 2018 - Science](https://www.science.org/doi/10.1126/science.aap7706) - Cesium atom recoil measurement
- [Morel et al. 2020 - Nature](https://www.nature.com/articles/s41586-020-2964-7) - Rubidium atom recoil measurement
- [Fan et al. 2023 - PRL](https://link.aps.org/doi/10.1103/PhysRevLett.130.071801) - Electron magnetic moment / alpha determination
- [Hoang et al. 2020 - Materials Letters](https://www.sciencedirect.com/science/article/abs/pii/S0167577X19318087) - Cooper pair mass, spherical shell superconductors
- [Tate et al. 1990 - Phys. Rev. B](https://link.aps.org/doi/10.1103/PhysRevB.42.7885) - Original Cooper pair mass measurement
- [Tajmar & Matos 2006](https://arxiv.org/abs/gr-qc/0607086) - Gravitomagnetic interpretation of Tate anomaly
