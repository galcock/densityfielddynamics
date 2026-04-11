# R4 Agent: N-body Simulation Analysis and EFE Implications

## What the v3.3 N-body Simulation Actually Did

### Source
Section 12 (Cosmological Implications) of v3.3, paragraph "Proof-of-concept: N-body structure formation" (lines 689-706 of section_cosmology.tex).

---

## Q1: What equation was solved?

The text says: "particle-mesh simulation" with "mu(x) = x/(1+x)".

This is the **spatial-only AQUAL-type (3-Laplacian) Poisson equation**:

    div[ mu(|grad psi|/a*) grad psi ] = -4 pi G rho / c^2

solved on the particle-mesh grid. There is **no mention** of the temporal sector (W-functional or K-sector) being included in the N-body solver. The simulation solves the modified Poisson equation at each timestep to get the gravitational acceleration, then advances particles.

**Verdict: Spatial AQUAL only. No temporal (W+K) sector.**

---

## Q2: Boundary conditions

Not stated. Standard particle-mesh codes use **periodic boundary conditions** on the computational box. This is the default for cosmological PM codes and nothing in the text indicates otherwise.

**Verdict: Periodic (implicit/standard).**

---

## Q3: Was grad(psi) computed self-consistently at each timestep?

Yes, necessarily. A particle-mesh simulation works by:
1. Assigning particle masses to a grid (CIC or similar)
2. Solving the field equation on the grid to get psi
3. Computing grad(psi) from the grid solution
4. Interpolating forces back to particles
5. Advancing positions/velocities

The field equation with mu(x) = x/(1+x) is nonlinear, so the solver must iterate at each timestep. The resulting grad(psi) is the **total self-consistent field** from ALL particles in the box.

**Verdict: Yes, self-consistent at each timestep. grad(psi) includes contributions from all particles.**

---

## Q4: Was the temporal sector included?

**No.** The text explicitly separates the N-body result from the "Forward perturbation skeleton" (which introduces the linearized growth equation with G_eff). The N-body paragraph describes only the modified Poisson equation with mu(x). The temporal EFE equation (mu(psi_0 + Delta_psi) - mu(psi_0) = (1-mu(psi_0)) mu(Delta_psi)) is discussed as a separate theoretical result, not as something implemented in the simulation.

**Verdict: No temporal sector in the simulation.**

---

## Q5: Box size and particle count

- **Grid**: 64^3 = 262,144 cells
- **Box**: 200 Mpc/h
- **Particles**: Not explicitly stated, but PM codes typically use N_particles = N_grid, so likely 64^3 = 262,144 particles

Cell size: 200/64 = 3.125 Mpc/h. This is very coarse -- only resolves scales above ~6 Mpc/h. No small-scale nonlinear structure is captured.

**Verdict: 64^3 grid, 200 Mpc/h box. Proof-of-concept resolution only.**

---

## Q6: Initial conditions

"Identical initial conditions" for all three runs (LCDM, Newtonian-baryons, DFD-baryons). The text does not specify the IC generator, but standard practice is:
- Zel'dovich approximation or 2LPT displacement field
- Applied at some high-z starting redshift
- Same random seed for all three runs

The parameters are: Omega_m = 0.30 (for LCDM), Omega_b = 0.049 (for baryon-only runs).

**Verdict: Standard cosmological ICs, same seed for all three models. Specifics not given.**

---

## Q7: Expansion history assumed

Not explicitly stated. The simulation likely uses the **LCDM expansion history** H(a) as the background (the "observer dictionary" approach described throughout the cosmology section). The DFD modification enters only through the force law (mu-enhanced Poisson equation), not through a modified Friedmann equation.

This is consistent with the paper's philosophy: H(a) is a reporting-layer variable, and DFD modifies the growth of perturbations within that background.

**Verdict: LCDM expansion history H(a) as background (implicit).**

---

## Q8: The Results

| Model | delta_rms | Ratio to Newton | Ratio to LCDM |
|---|---|---|---|
| LCDM (Omega_m = 0.30) | ~1.2e-3 (implied) | ~8x | 1.0x |
| Newtonian baryons (Omega_b = 0.049) | 1.5e-4 | 1.0x | 0.125x |
| DFD baryons (mu = x/(1+x)) | 6.4e-3 | 42.7x | **5.4x** |

Key numbers:
- DFD/Newton = 6.4e-3 / 1.5e-4 = **42.7x** (the paper says 43.8x -- small rounding difference)
- DFD/LCDM = **5.4x** overshoot
- Implied LCDM delta_rms = 6.4e-3 / 5.4 = 1.185e-3

---

## Q9: CRITICAL -- What was the effective x-bar at each particle?

This is the key diagnostic question.

In the particle-mesh simulation, the solver computes the **total** grad(psi) on the grid, which is the collective field from ALL particles. At each grid point, the argument to mu is:

    x = |grad(psi)_total| / a*

where grad(psi)_total is the self-consistent solution including contributions from every particle in the box.

**There was NO imposed external field.** The text explicitly states that the simulation was run "without the cosmological External Field Effect (EFE) from the Hubble flow." The 5.4x overshoot is presented as the expected consequence of omitting the EFE.

However, the collective grad(psi)_total IS a form of self-regularization:
- Each particle sees not just its own field but the fields of all other particles
- The collective |grad(psi)| at any point is larger than any single particle's contribution
- This collective field acts as a kind of "internal EFE" -- the bulk flow of matter in the simulation box raises x-bar above the naive single-particle estimate

**Verdict: x-bar was the self-consistent total |grad(psi)|/a* from all particles. No imposed EFE. The collective field provides partial self-regularization.**

---

## Q10: Interpretation of the 5.4x Overshoot WITHOUT EFE

The paper claims:
- Raw mu-enhancement in the deep-MOND regime: ~400x (at x ~ 4e-4, mu(x) ~ x, so G_eff ~ G/x ~ G/4e-4 = 2500G... but this is the field equation enhancement, not the growth factor enhancement)
- Expected overshoot without EFE: ~400x over LCDM
- Observed overshoot: only 5.4x

**This is a MASSIVE discrepancy with the paper's own claim.** If the raw mu-enhancement should give ~400x overshoot, but the simulation gives only 5.4x, then the self-consistent collective field is already providing enormous self-regulation:

    Suppression factor from self-consistency alone = 400 / 5.4 = 74x

This means the self-consistent nonlinear Poisson solver, even without an imposed EFE, suppresses the naive linear estimate by a factor of ~74. The collective sigma_nabla (the rms of |grad(psi)| from all particles) raises the effective x-bar far above the naive perturbation estimate of x ~ 4e-4.

### Estimating the effective x-bar from the simulation result

If LCDM gives delta_rms ~ 1.2e-3 and DFD gives 5.4x more, the effective enhancement factor is:
- G_eff/G ~ 5.4 (as a growth-rate-squared-like ratio, roughly)
- For mu(x) = x/(1+x): G_eff/G = 1/mu(x) ~ 1/x for small x
- So effective x ~ 1/5.4 ~ 0.19

Compare with the paper's claim of x ~ 4e-4 for perturbation accelerations. The self-consistent solver has raised the effective x from ~4e-4 to ~0.19 -- a factor of ~475 increase. This is the collective sigma_nabla effect.

**Key insight: The self-consistent 3-Laplacian already "knows about" the collective field. The 64^3 PM solver naturally includes the mean-field regularization through the nonlinear Poisson equation.**

---

## Q11: Value of Imposed EFE

**No EFE was imposed.** The text is explicit: the 5.4x overshoot exists precisely because the cosmological EFE was NOT included. The paper states that including the EFE (a_ext ~ cH_0 ~ 6 a_0, giving x_ext ~ 6) would drop the enhancement from ~400x to ~1.2x.

---

## Q12: What the 42.7x (not 400x) Tells Us About Self-Regulation

The paper claims naive mu-enhancement should be ~400x, but the simulation gives 42.7x over Newton (= 5.4x over LCDM).

There are two ways to read this discrepancy:

### Reading A: The "400x" is a LINEAR estimate, not applicable to nonlinear PM

The 400x claim comes from: at x ~ 4e-4, mu(x) ~ 4e-4, so G_eff ~ G/mu ~ 2500G. But this is the pointwise field-equation enhancement, not the growth-factor enhancement. The growth factor integrates over the expansion history, and the relationship between G_eff and delta_rms is not simply linear:
- delta grows as D(a), where D depends on the integral of G_eff(a) * Omega(a)
- The 42.7x in delta_rms corresponds to the integrated nonlinear enhancement over the simulation time

### Reading B: The self-consistent solver provides massive self-regulation

Even without the EFE, the nonlinear Poisson equation self-regulates because:
1. As perturbations grow, |grad(psi)| increases
2. Larger |grad(psi)| means larger x
3. Larger x means mu(x) closer to 1
4. mu closer to 1 means LESS enhancement
5. This is a negative feedback loop built into the 3-Laplacian

The self-consistent PM solver captures this feedback automatically. The naive "400x" estimate ignores it entirely.

### Reading C (most likely): Both effects combine

The 400x is the wrong baseline. The correct comparison is:
- **Without** self-consistency AND without EFE: ~400x overshoot (linear perturbation theory)
- **With** self-consistency but without EFE: 5.4x overshoot (the actual simulation)
- **With** self-consistency AND with EFE: ~1.2x overshoot (the paper's prediction, not yet simulated)

The self-consistent nonlinear solver already provides a ~74x suppression. The EFE needs to provide only an additional ~4.5x suppression to reach the target of ~1.2x.

---

## P(k) Confrontation Section Analysis

The P(k) confrontation (section_Pk_confrontation.tex) is entirely separate from the N-body simulation. It:

1. Uses **linear Kaiser formula** for RSD multipoles P_0, P_2, P_4
2. Extracts beta = f/b from BOSS DR12 and eBOSS DR16
3. Compares with DFD prediction: f_DFD(z) = Omega_m(z)^gamma [1 + O(k_alpha)]
4. The psi-field correction is O(k_alpha) ~ 10^-5, negligible at current precision
5. **Conclusion: DFD and LCDM predict indistinguishable linear growth** at current multipole precision

The confrontation explicitly states: "DFD's distinctive signatures appear in strong-field regimes (galaxy rotation curves, atomic clock comparisons) rather than linear-regime RSD."

This section uses NO nonlinear simulation results. It is purely a linear-theory consistency check.

---

## Summary of Key Findings

1. **The N-body simulation solved spatial-only AQUAL** (modified Poisson with mu(x) = x/(1+x)). No temporal sector, no imposed EFE.

2. **The 5.4x overshoot is the result of the self-consistent 3-Laplacian** operating on 64^3 particles in a 200 Mpc/h box with LCDM expansion history.

3. **The self-consistent solver already provides ~74x suppression** relative to the naive linear estimate of ~400x. This is the nonlinear self-regulation of the 3-Laplacian: as structure grows, grad(psi) increases, x increases, mu approaches 1, and the enhancement weakens.

4. **The paper claims an additional EFE suppression of ~4.5x** (from 5.4x to 1.2x) is needed, coming from the cosmological background field a_ext ~ cH_0 ~ 6 a_0.

5. **The P(k) confrontation is entirely linear-theory** and separate from the N-body result. It shows DFD = LCDM at current precision in the linear RSD regime.

6. **Critical gap**: The N-body simulation has NOT been run with the EFE included. The paper acknowledges this: "production-quality results require >= 256^3 with the EFE implemented."

7. **The effective x-bar in the simulation** was the self-consistent total |grad(psi)|/a* from all particles -- roughly x_eff ~ 0.19, far above the naive perturbation estimate of x ~ 4e-4. This demonstrates that the collective field (sigma_nabla regularization) is already doing most of the heavy lifting.

---

## Implications for the P(k) Closure Program

The N-body result is actually **encouraging** for DFD:
- The self-consistent 3-Laplacian gets within a factor of 5.4 of the LCDM target WITHOUT any EFE
- The remaining factor is small enough that the cosmological EFE (a well-motivated physical mechanism) could plausibly close the gap
- The key unknown is whether the EFE, when properly implemented, gives exactly the right suppression at each scale k to reproduce the observed P(k) shape

The danger is:
- The EFE is a single number (x_ext ~ 6), not a function of k
- P(k) matching requires the RIGHT suppression at EVERY scale
- If the EFE oversuppresses large scales or undersuppresses small scales, the shape will be wrong
- The baryon-only transfer function T_b(k) has a very different shape from T_LCDM(k), and the mu-enhancement must compensate for this shape difference scale-by-scale

**Bottom line**: The 5.4x overshoot without EFE is a proof-of-concept success, not a failure. It shows the nonlinear self-regulation is powerful. The open question is whether the EFE + self-regulation together produce the right P(k) SHAPE, not just the right amplitude.
