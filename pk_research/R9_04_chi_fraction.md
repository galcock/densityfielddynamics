# R9 Agent 4: What if Chi is Only a Fraction of Dark Matter?

## Research Question

The 89-agent campaign assumed chi must provide ALL of Omega_CDM = 0.266. But what if chi provides only a fraction, with MOND nonlinearity (phantom dark matter) providing the rest? From R7, the self-consistent N-body WITHOUT external field effect gives sigma_8 = 0.773 (95% of target). The P(k) shape is wrong (Silk damping), but sigma_8 is close.

**Hypothesis**: Omega_chi ~ 0.05 (providing pre-recombination potential wells to fix transfer function shape) + MOND phantom DM (providing post-recombination growth enhancement).

## Method

### Two-component approach:
1. **Transfer function T(k)**: Eisenstein-Hu (1998) with mixed matter content Omega_m = Omega_b + Omega_chi. Chi acts as pressureless, gravitationally-coupled matter pre-recombination -- identical to CDM for transfer function purposes.
2. **Growth factor D(a)**: Post-recombination growth driven by Omega_chi (normal gravity) + Omega_b * nu_MOND (MOND-enhanced baryon contribution).

### Three scenario sets:
- **S1**: Constant MOND enhancement -- nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b so that total Omega_eff = 0.315
- **S2**: Scale-dependent MOND -- nu(k) = 1 + (nu_max - 1)/(1 + (k/k_MOND)^1.5) with k_MOND = 0.05 h/Mpc
- **S3**: Minimum chi search -- fine grid over Omega_chi to find thresholds

### Reference values (Planck 2018):
- sigma_8 = 0.811
- s_BAO = 150.87 Mpc/h
- Omega_b = 0.0493, Omega_CDM = 0.266, Omega_m = 0.315

## Results

### Scenario 1: Chi Transfer Function + Constant MOND Growth

The growth factor D is forced to match LCDM by construction (Omega_eff = 0.315). The ONLY difference is the transfer function shape.

| Omega_chi | f_chi | sigma_8 | sig8/target | shape_dev (dex) | P/P_LCDM(k=0.1) | s_BAO (Mpc/h) |
|-----------|-------|---------|-------------|-----------------|------------------|---------------|
| 0.050     | 0.19  | 0.086   | 0.105       | 1.578           | 0.012            | 192.0         |
| 0.100     | 0.38  | 0.219   | 0.270       | 0.877           | 0.082            | 179.0         |
| 0.150     | 0.56  | 0.380   | 0.468       | 0.492           | 0.241            | 168.6         |
| 0.200     | 0.75  | 0.558   | 0.688       | 0.236           | 0.502            | 160.1         |
| 0.266     | 1.00  | 0.811   | 1.000       | 0.000           | 1.000            | 150.9         |

### Scenario 2: Chi Transfer + Scale-Dependent MOND Growth

MOND enhancement strong at large scales (k << 0.05), weak at small scales. This makes things WORSE because small-scale growth is further suppressed.

| Omega_chi | f_chi | sigma_8 | sig8/target | shape_dev (dex) | P/P_LCDM(k=0.1) |
|-----------|-------|---------|-------------|-----------------|------------------|
| 0.050     | 0.19  | 0.020   | 0.025       | 3.047           | 0.0001           |
| 0.100     | 0.38  | 0.049   | 0.061       | 1.978           | 0.002            |
| 0.150     | 0.56  | 0.116   | 0.143       | 1.245           | 0.021            |
| 0.200     | 0.75  | 0.273   | 0.337       | 0.655           | 0.128            |
| 0.266     | 1.00  | 0.813   | 1.003       | 0.002           | 1.005            |

### Scenario 3: Minimum Chi Search

For sigma_8 within 5% of target AND shape deviation < 0.1 dex:

| Criterion | Scenario 1 (constant MOND) | Scenario 2 (scale-dep MOND) |
|-----------|---------------------------|----------------------------|
| Min Omega_chi for sigma_8 OK | 0.261 | 0.266 |
| Min Omega_chi for shape OK | 0.240 | 0.256 |
| Min Omega_chi for BOTH | **0.261 (f = 0.98)** | **0.266 (f = 1.00)** |

### Transfer Function Shape at k = 0.1 h/Mpc

The fundamental constraint is T^2(k), set at recombination:

| Omega_chi | T^2 / T^2_LCDM at k=0.1 |
|-----------|--------------------------|
| 0.050     | 0.012                    |
| 0.100     | 0.082                    |
| 0.150     | 0.241                    |
| 0.200     | 0.502                    |
| 0.266     | 1.000                    |
| Baryon only | ~0.000                 |

### P/P_LCDM Across Scales (transfer function only, growth matched)

| Omega_chi | k=0.005 | k=0.01 | k=0.02 | k=0.05 | k=0.1 | k=0.2 | k=0.5 |
|-----------|---------|--------|--------|--------|-------|-------|-------|
| 0.050     | 0.55    | 0.29   | 0.08   | 0.02   | 0.01  | 0.008 | 0.005 |
| 0.100     | 0.74    | 0.53   | 0.26   | 0.13   | 0.08  | 0.06  | 0.05  |
| 0.150     | 0.85    | 0.71   | 0.49   | 0.32   | 0.24  | 0.20  | 0.17  |
| 0.200     | 0.93    | 0.86   | 0.72   | 0.58   | 0.50  | 0.45  | 0.41  |
| 0.266     | 1.00    | 1.00   | 1.00   | 1.00   | 1.00  | 1.00  | 1.00  |

## Key Finding: The Transfer Function is the Bottleneck

**The hypothesis that a small Omega_chi ~ 0.05 can fix the transfer function while MOND handles growth is FALSE.**

The reason is fundamental: the power spectrum P(k) factorizes into two pieces:

    P(k) = T^2(k) * D^2(a) * k^n_s * (normalization)

- **D^2(a)** is the growth factor -- a single number (scale-independent). MOND with constant nu ~ 6.4 can match D_LCDM exactly. This is confirmed: with Omega_eff = 0.315, D/D_LCDM = 1.000.

- **T^2(k)** is the transfer function -- encodes HOW MUCH power there is at each scale relative to the primordial spectrum. This is set ENTIRELY at recombination (z ~ 1100) by the matter content.

The problem: with Omega_chi = 0.05, the transfer function at k = 0.1 h/Mpc has only 1.2% of the LCDM power. Even with perfect growth (D matched exactly), sigma_8 reaches only 0.086 -- a factor of 9.4 below the target. No amount of post-recombination MOND growth can compensate.

**Why the transfer function depends so strongly on Omega_chi:**

At recombination, perturbations in baryons are suppressed by:
1. **Silk damping**: photon diffusion erases baryon perturbations at k > k_silk ~ 0.1 h/Mpc
2. **Radiation driving**: baryon perturbations oscillate rather than grow during radiation domination
3. **Missing potential wells**: without chi, there are no cold, pressureless perturbations to hold the gravitational potential steady through the radiation-matter transition

CDM (or chi) provides a "scaffolding" of potential wells that baryons fall into after recombination. With only 19% of the needed scaffolding (Omega_chi = 0.05), the scaffolding is too shallow by ~90%.

## The Minimum Chi Fraction

The minimum Omega_chi to match LCDM P(k) within observational tolerances:

- **sigma_8 within 5%**: Omega_chi > 0.261 (98% of Omega_CDM)
- **Shape within 0.1 dex**: Omega_chi > 0.240 (90% of Omega_CDM)
- **Both simultaneously**: Omega_chi > 0.261

**There is essentially no room for fractional chi.** The DFD chi field must provide very nearly the full Omega_CDM to reproduce the observed power spectrum shape.

## Why MOND Cannot Help With the Shape

MOND enters AFTER recombination as a modification to gravity in the post-recombination growth equation. By that time, the transfer function shape is already set. MOND can only provide a scale-independent (or nearly scale-independent) boost to the growth factor.

Even with scale-dependent MOND (Scenario 2), where nu(k) varies from ~5 at k=0.01 to ~2 at k=0.1, this makes the problem WORSE: it further suppresses small-scale power relative to large scales, amplifying the shape mismatch.

The only way MOND could fix the shape would be if it operated PRE-recombination to create potential wells. But standard MOND modifies the Poisson equation -- it cannot create pressureless perturbations in the radiation era because there is no pressureless component to enhance.

## Implications for DFD

1. **Chi must be a full CDM replacement**: Omega_chi must be approximately 0.266 (at least 0.24 for shape, 0.26 for sigma_8). There is no viable "chi-lite" scenario.

2. **The "phantom DM from MOND" idea works for DYNAMICS (rotation curves, cluster masses) but NOT for the transfer function**. Galaxy-scale MOND effects are a post-recombination, late-universe phenomenon. They cannot create the ~150 Mpc BAO feature at the right amplitude or prevent Silk damping of baryon perturbations.

3. **The BAO scale is also affected**: with Omega_chi = 0.05, s_BAO = 192 Mpc/h vs the target 151 Mpc/h. The sound horizon depends on the baryon-to-total-matter ratio. Less chi means a higher baryon fraction, which means more radiation pressure, larger sound horizon, and wrong BAO peak positions.

4. **This result strengthens the case for chi as a genuine pre-recombination species**: chi must exist before recombination, couple gravitationally, and have Omega_chi ~ 0.266 to create the observed transfer function. It cannot be a post-recombination emergent phenomenon.

## Connection to R7 Result

R7 found sigma_8 = 0.773 without EFE in self-consistent N-body. That result used the BARYON transfer function but boosted growth with MOND. Our analysis shows:

- Pure baryon transfer with perfect growth gives sigma_8 ~ 0.086 (from our calculation)
- R7 getting sigma_8 = 0.773 implies their effective T^2 ratio at sigma_8 scales is ~0.91
- This means R7 must have been using something closer to the LCDM transfer function as input (possibly mixed chi+baryon), or there is a nonlinear mode-coupling effect in the N-body that redistributes power

The R7 result needs reconciliation with the linear theory presented here.

## Technical Notes

- Solver: `R9_04_chi_fraction_solver.py`
- Transfer functions: Eisenstein-Hu 1998 no-wiggle approximation
- Growth: Linear ODE with constant effective Omega
- Scale-dependent MOND: nu(k) = 1 + (nu_max - 1)/(1 + (k/0.05)^1.5)
- k range: 0.001 to 3.16 h/Mpc, 2000 log-spaced points
- Growth interpolation: pre-computed on 80-point Omega_eff grid for efficiency

## Bottom Line

**The minimum Omega_chi to reproduce the LCDM power spectrum is ~0.26, which is 98% of Omega_CDM.** The transfer function shape, set at recombination, cannot be fixed by post-recombination MOND effects. Chi must be a genuine pre-recombination pressureless species at nearly the full CDM density. The "chi-lite + MOND phantom DM" scenario is ruled out by the transfer function constraint.
