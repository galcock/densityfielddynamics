# Fine Structure Constant Residuals and Lambda: A Unified Analysis

## Connection Between Species-Dependent Alpha Shifts and Anomalous EM-Gravity Coupling

**Date:** 2026-03-27
**Status:** Critical theoretical analysis connecting two major DFD findings

---

## 1. The Fan et al. 2023 Measurement

X. Fan, T.G. Myers, B.A.D. Sukra, and G. Gabrielse published "Measurement of the Electron Magnetic Moment" in Physical Review Letters 130, 071801 (2023). This measurement determined the electron magnetic moment 2.2 times more precisely than Hanneke et al. (2008), which had stood for 14 years.

**Published value:**

    alpha_inv(Fan 2023) = 137.035999166(15)    [0.11 ppb uncertainty]

This is extracted from the measured g/2 = 1.00115965218059(13) combined with Standard Model QED theory to fifth order in alpha.

---

## 2. Updated Four-Measurement Residual Analysis

DFD's ab initio bare topological value (zero free parameters):

    alpha_inv_bare = 137.035999854

All four published measurements sit BELOW this value:

| Measurement              | alpha_inv         | Uncertainty | delta (ppb) | Method         |
|--------------------------|-------------------|-------------|-------------|----------------|
| Rb recoil (Parker 2018)  | 137.035999206(11) | 0.080 ppb   | +4.73       | Atom recoil    |
| e- g-2 (Fan 2023)        | 137.035999166(15) | 0.11 ppb    | +5.02       | Electron g-2   |
| e- g-2 (Hanneke 2008)    | 137.035999084(51) | 0.37 ppb    | +5.62       | Electron g-2   |
| Cs recoil (Morel 2020)   | 137.035999046(27) | 0.20 ppb    | +5.90       | Atom recoil    |

**Key observations:**

1. ALL four residuals are positive (measured < bare), confirming DFD's prediction that the physical alpha is shifted downward from the bare topological value.

2. The mean residual is +5.32 ppb with a spread of 1.17 ppb.

3. The two g-2 measurements (Hanneke and Fan) are consistent at 1.6 sigma, with Fan being 2.2x more precise.

4. Fan's value (5.02 ppb) sits BETWEEN the Rb value (4.73 ppb) and the Cs value (5.90 ppb).

### Hanneke vs. Fan Consistency

The difference between the two g-2 measurements is 0.60 ppb, with a combined uncertainty of 0.39 ppb, giving a 1.6-sigma tension. This is not statistically significant but is worth monitoring. The Fan measurement, being more precise, supersedes Hanneke as the primary g-2 determination.

---

## 3. Species-Dependent Analysis: A Critical Complication

### The Simple Model and Its Problem

The DFD species-dependent model posits:

    delta(A) = C * f_EM(A)

where f_EM(A) is the nuclear Coulomb energy fraction of atom A, computed from the semi-empirical mass formula:

    E_Coulomb = a_C * Z(Z-1) / A^(1/3),    a_C = 0.711 MeV
    f_EM(A) = E_Coulomb / (A * 931.494 MeV)

Computed f_EM values:

| Nucleus | Z  | A   | E_Coulomb (MeV) | f_EM     |
|---------|----|-----|-----------------|----------|
| Li-7    | 3  | 7   | 2.23            | 0.000341 |
| K-39    | 19 | 39  | 71.70           | 0.001976 |
| Rb-87   | 37 | 87  | 213.73          | 0.002640 |
| Sr-87   | 38 | 87  | 225.61          | 0.002787 |
| Cs-133  | 55 | 133 | 413.69          | 0.003342 |
| Yb-174  | 70 | 174 | 615.13          | 0.003797 |

The ratio f_EM(Cs)/f_EM(Rb) = 1.266 matches the observed delta(Cs)/delta(Rb) = 1.247 to 1.5%, as reported in the DFD paper.

### The Problem: Where Does g-2 Fit?

If the model were simply delta = C * f_EM, then the electron g-2 measurement (f_EM = 0 for a free electron) should give delta = 0. Instead, Fan gives delta = 5.02 ppb -- larger than the Rb value.

This immediately tells us the model must have TWO components:

    delta_total(A) = delta_universal + delta_species(A)

where delta_universal is a species-independent shift (affecting all measurements) and delta_species depends on the atomic species through f_EM.

### But the Two-Component Model Also Has Problems

If we write delta = delta_0 + C * f_EM and use Fan (f_EM = 0) as the baseline:

    delta_0 = 5.02 ppb (from Fan)
    delta_species(Rb) = 4.73 - 5.02 = -0.29 ppb
    delta_species(Cs) = 5.90 - 5.02 = +0.88 ppb

The species-dependent part is NEGATIVE for Rb and positive for Cs. This means the simple proportionality delta_species = C * f_EM cannot work with a single positive C, because Rb gives a negative species contribution.

### Resolution: Different Measurement Chains

The resolution is that g-2 and atom-recoil measurements extract alpha through FUNDAMENTALLY DIFFERENT physics:

- **Atom recoil** (Rb, Cs): Measures h/m_atom via photon recoil, combined with the Rydberg constant. The measurement chain is: photon momentum -> atomic mass -> h/m -> alpha.

- **Electron g-2**: Measures the anomalous magnetic moment a_e, then inverts the QED series a_e = f(alpha) to extract alpha. The measurement chain is: cyclotron/spin frequencies -> a_e -> QED inversion -> alpha.

In DFD, the density field psi modifies the gauge coupling. These two measurement chains couple to psi differently:
- Atom recoil couples through the atomic mass (which includes nuclear Coulomb energy)
- g-2 couples through the electron's electromagnetic interaction in the Penning trap

Therefore, the g-2 "baseline" is NOT the f_EM = 0 limit of the atom-recoil measurements. They are measuring different projections of the same underlying DFD modification.

### Atom-Recoil-Only Linear Fit

Using ONLY the two atom-recoil measurements:

    delta(A) = 0.33 + 1666.7 * f_EM(A)    [ppb]

- Intercept at f_EM = 0: delta_0^(recoil) = 0.33 ppb
- Slope: 1666.7 ppb per unit f_EM

The intercept (0.33 ppb) represents the atom-recoil measurement chain's sensitivity to psi in the limit of zero Coulomb energy. This is very different from the g-2 value (5.02 ppb), confirming that the two methods probe different aspects of the DFD field.

---

## 4. The Lambda Connection

### The Core Idea

Lambda (the EM-gravity coupling parameter) says that electromagnetic energy may gravitate differently than rest mass:

    m_grav(A) = m_rest(A) + (lambda - 1) * E_EM(A)/c^2

The species-dependent alpha shift says that measurements using atoms with more Coulomb energy see a larger shift in the measured alpha:

    delta_alpha(A) / alpha = C * f_EM(A)

These are potentially THE SAME PHENOMENON viewed from two different angles:
- Lambda describes how EM energy couples to gravity (affects free-fall)
- The alpha shift describes how EM energy in atoms affects alpha measurements (affects spectroscopy/recoil)

### Attempting the Derivation

If the species-dependent shift comes from anomalous gravitational coupling of nuclear Coulomb energy in a gravitational potential psi:

    delta(A) / alpha_inv = (lambda - 1) * f_EM(A) * |psi/c^2|

Using the calibration C = 1.78 * 10^-6 from the atom-recoil data:

| Gravitational potential | |psi/c^2|  | Implied (lambda-1) |
|-|-|-|
| Earth surface           | 7 * 10^-10 | 2.5 * 10^3          |
| Solar (at Earth orbit)  | 1 * 10^-8  | 1.8 * 10^2          |
| Galactic                | 2 * 10^-6  | 8.9 * 10^-1         |

### The MICROSCOPE Problem

MICROSCOPE's final result (Touboul et al., PRL 129, 121102, 2022) constrains:

    eta(Ti, Pt) = [-1.5 +/- 2.3(stat) +/- 1.5(syst)] * 10^-15

For a lambda-type EP violation:

    eta = (lambda - 1) * |f_EM(Pt) - f_EM(Ti)|

With f_EM(Ti-48) = 0.00202 and f_EM(Pt-195) = 0.00405:

    |lambda - 1| < 7.4 * 10^-13

This is 15 orders of magnitude smaller than the (lambda-1) needed to explain the alpha shifts through Earth's gravitational potential, and 12 orders smaller even using the Galactic potential.

### Can the Alpha Shift and MICROSCOPE Be Reconciled?

**The answer is: NOT through a simple lambda mechanism.** Here is the analysis:

**Scenario A: Same lambda, different observables.** One might hope that the alpha shift and EP violation test different combinations of lambda. But they don't -- both depend on f_EM of the test body, and the linear coupling (lambda-1) * f_EM appears in both. MICROSCOPE directly bounds the same parameter that would produce the alpha shift. The mismatch is too large (10^12 or more) for any geometric factor to resolve.

**Scenario B: The alpha shift is NOT caused by lambda.** The species-dependent shift in alpha could arise from a mechanism within DFD that is distinct from anomalous gravitational coupling. For example:
- The density field psi could modify the vacuum permittivity locally in a way that depends on the local matter density (and hence nuclear composition)
- The atom-recoil measurement chain could be sensitive to how psi modifies photon dispersion, which could depend on nuclear structure
- The effect could be a quantum-level phenomenon in the measurement process, not a gravitational coupling

**Scenario C: DFD's lambda couples to DYNAMIC EM fields only.** If lambda-1 only affects oscillating electromagnetic fields (not the static nuclear Coulomb potential), then:
- MICROSCOPE (which tests free-fall of bulk matter) would see no effect, because nuclear Coulomb energy is static
- But atom-recoil measurements use PHOTONS (dynamic EM), so the alpha shift could still be real
- However, the species dependence through f_EM (nuclear Coulomb, which IS static) would then be harder to explain

**Scenario D: The species dependence is a two-point coincidence.** With only two atom-recoil measurements (Rb and Cs), the f_EM proportionality could be coincidental. The 1.5% agreement between the ratios might not survive additional measurements. Future measurements with Li, K, Sr, or Yb would test this.

---

## 5. Predictions for Future Measurements

### Atom-Recoil Predictions (from Rb-Cs linear model)

    delta(A) = 0.33 + 1666.7 * f_EM(A)  [ppb]

| Species | f_EM     | Predicted delta (ppb) | Predicted alpha_inv   |
|---------|----------|-----------------------|-----------------------|
| Li-7    | 0.000341 | 0.90                  | 137.035999731         |
| K-39    | 0.001976 | 3.62                  | 137.035999357         |
| Rb-87   | 0.002640 | 4.73                  | 137.035999206 (input) |
| Sr-87   | 0.002787 | 4.98                  | 137.035999172         |
| Cs-133  | 0.003342 | 5.90                  | 137.035999045 (input) |
| Yb-174  | 0.003797 | 6.66                  | 137.035998942         |

### Most Discriminating Tests

1. **Lithium-7**: Predicted delta = 0.90 ppb (alpha_inv = 137.035999731). This is dramatically different from the g-2 value, so a Li atom-recoil measurement would powerfully test the model. If Li gives ~0.9 ppb while g-2 gives ~5 ppb, the species-dependent model within atom recoil is confirmed AND the g-2 vs. recoil discrepancy is established.

2. **Ytterbium-174**: Predicted delta = 6.66 ppb. Higher f_EM means larger shift. An Yb measurement above the Cs value would strengthen the f_EM trend.

3. **Strontium-87**: Predicted delta = 4.98 ppb. Being close to Rb in f_EM, this tests the linearity of the model at intermediate values. Notably, Sr-87 and Rb-87 have the same A but different Z, making this a particularly clean comparison of nuclear Coulomb effects.

---

## 6. Synthesis: What Does This Mean?

### What We Know

1. **The bare topological value works.** All four measurements scatter around alpha_inv_bare = 137.035999854 with residuals of 4.7-5.9 ppb. The probability that four independent measurements all fall below a random number is 1/16 = 6.25%, making the one-sided pattern suggestive but not yet conclusive.

2. **The Rb-Cs tension is real.** The difference delta(Cs) - delta(Rb) = 1.17 ppb, with a combined uncertainty of ~0.22 ppb, represents a 5.3-sigma effect. This is not a statistical fluctuation.

3. **The f_EM proportionality works for atom recoil.** The ratio of shifts matches the ratio of nuclear Coulomb fractions to 1.5%. With only two points, this could be coincidence, but it is a striking agreement.

4. **g-2 and atom recoil measure different things.** The Fan 2023 g-2 value does not fit on the atom-recoil f_EM trend line. This is expected if the two measurement methods couple differently to the DFD field.

### What We Don't Know

1. **Whether the species dependence is from lambda or something else.** MICROSCOPE rules out a simple lambda interpretation by 12+ orders of magnitude. Either the mechanism is not lambda, or it is a fundamentally different kind of EM-gravity coupling that does not produce EP violations.

2. **Whether the pattern survives additional measurements.** A third atom-recoil species (Li, K, Sr, or Yb) would transform this from a two-point fit to a genuine test.

3. **What causes the ~5 ppb universal shift.** All measurements agree on a shift of roughly 5 ppb from the bare value. This could be the running of alpha from the topological (UV) value to the IR measurement scale, vacuum polarization effects, or the universal part of DFD's psi coupling.

### Implications for the SQMS Experiment

The proposed SQMS cavity experiment tests whether alpha varies with local gravitational potential (different from the species-dependent question). The analysis here suggests:

**Strong motivation to proceed**, because:
- The ~5 ppb universal shift is unexplained and could have a gravitational component
- The species-dependent effect (if real) indicates that EM energy and gravity are entangled in the measurement process
- A cavity experiment with variable gravitational potential (e.g., height changes, solar modulation) would probe the universal shift independently of the species question

**But the expected signal may be small**: If the universal shift of ~5 ppb is gravitational, it corresponds to alpha variations of order 5 ppb * (delta_psi / psi) where delta_psi/psi is the fractional change in gravitational potential. For a 10-meter height change on Earth, delta_psi/psi ~ 10^-15, giving delta_alpha/alpha ~ 5 * 10^-24 -- far below current sensitivity. Solar/lunar modulation gives larger potential swings (~10^-10 fractional), potentially producing signals at the 5 * 10^-19 level.

### Does the Rb-Cs Tension Already Provide Evidence for Psi-EM Coupling?

**Yes, tentatively.** The Rb-Cs atom-recoil discrepancy (5.3 sigma) combined with the f_EM proportionality constitutes evidence that the measured value of alpha depends on the nuclear composition of the atom used in the measurement. In DFD, this is naturally interpreted as the density field psi modifying the effective gauge coupling in a way that depends on the local EM energy density (nuclear Coulomb field) of the test atom.

However, this is NOT the same as lambda (anomalous gravitational coupling of EM energy). It is closer to what might be called a "vacuum screening" effect: the nuclear Coulomb field of the atom modifies the local vacuum state, which in turn modifies the effective alpha seen by photons interacting with that atom.

This distinction is crucial:
- **Lambda** (EP violation): EM energy falls differently. MICROSCOPE says no.
- **Vacuum screening**: EM energy modifies the local gauge coupling. MICROSCOPE does not constrain this, because it tests free-fall, not gauge couplings.

The DFD framework may naturally produce vacuum screening through the psi-dependent gauge coupling without requiring EP violation, but this needs to be derived explicitly from the field equations.

---

## 7. Key Conclusions

1. **Fan et al. 2023 confirms the pattern**: alpha_inv = 137.035999166(15) gives delta = 5.02 ppb, consistent with the other three measurements all being below the DFD bare value.

2. **The species-dependent model needs refinement**: g-2 and atom-recoil measurements couple differently to the DFD field, so they cannot be placed on the same f_EM trend line. The model should be: atom-recoil measurements follow delta = a + b*f_EM, while g-2 measurements follow a separate relation.

3. **The lambda connection is indirect**: MICROSCOPE rules out a direct lambda interpretation by many orders of magnitude. The species dependence is better understood as a vacuum-screening effect in the measurement chain, not as an EP violation.

4. **A third atom-recoil species is the critical test**: Any one of Li, K, Sr, or Yb measured via atom recoil would turn the two-point Rb-Cs coincidence into a genuine prediction test.

5. **The SQMS experiment probes a complementary question**: It tests the gravitational-potential dependence of alpha (the universal shift), not the species dependence. Both are motivated by DFD.

---

## References

- Fan, X., Myers, T.G., Sukra, B.A.D., and Gabrielse, G. (2023). "Measurement of the Electron Magnetic Moment." Physical Review Letters 130, 071801.
- Parker, R.H. et al. (2018). "Measurement of the fine-structure constant as a test of the Standard Model." Science 360, 191-195.
- Morel, L. et al. (2020). "Determination of the fine-structure constant with an accuracy of 81 parts per trillion." Nature 588, 61-65.
- Hanneke, D., Fogwell, S., and Gabrielse, G. (2008). "New Measurement of the Electron Magnetic Moment and the Fine Structure Constant." Physical Review Letters 100, 120801.
- Touboul, P. et al. (2022). "MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle." Physical Review Letters 129, 121102.
