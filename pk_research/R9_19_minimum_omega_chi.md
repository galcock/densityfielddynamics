# R9 Agent 19: Minimum Omega_chi for P(k) Shape Compatibility

## Executive Summary

**MINIMUM Omega_chi = 0.260** (97.7% of LCDM CDM density), meaning chi must provide nearly all of the CDM-like matter. MOND alone cannot fix the power spectrum shape.

The **binding constraint is the transfer function**, not growth. MOND can enhance post-recombination growth to any desired level (sigma_8 is freely adjustable), but MOND has zero effect on the pre-recombination transfer function that determines the P(k) shape. The shape requires pressureless matter at recombination, which only chi provides.

## Method

### Scan Parameters
- Omega_chi scanned from 0.00 to 0.30 in steps of 0.01
- Transfer function: Eisenstein-Hu (1998) no-wiggle approximation
- Growth: linear ODE with Omega_eff = Omega_chi + Omega_b * nu_MOND
- MOND calibrated so nu_MOND = (Omega_m_LCDM - Omega_chi) / Omega_b

### Observational Criteria
1. **sigma_8**: within 0.811 +/- 0.08
2. **P(k) shape**: max deviation < 30% from LCDM at k = 0.01-0.15 h/Mpc
3. **BAO position**: sound horizon within 1% of LCDM

## Key Results

### Transfer Function is the Binding Constraint

| Omega_chi | % of CDM | sigma_8 | P/P_LCDM(0.05) | P/P_LCDM(0.10) | max dev | BAO shift | Pass all? |
|-----------|----------|---------|-----------------|-----------------|---------|-----------|-----------|
| 0.000     | 0.0%     | 0.007   | 0.000           | 0.000           | 100.0%  | 37.8%     | No        |
| 0.050     | 18.8%    | 0.086   | 0.023           | 0.012           | 99.1%   | 27.3%     | No        |
| 0.100     | 37.6%    | 0.219   | 0.126           | 0.082           | 93.3%   | 18.7%     | No        |
| 0.150     | 56.4%    | 0.380   | 0.317           | 0.241           | 78.8%   | 11.7%     | No        |
| 0.200     | 75.2%    | 0.558   | 0.579           | 0.502           | 53.2%   | 6.1%      | No        |
| 0.240     | 90.2%    | 0.710   | 0.826           | 0.784           | 23.6%   | 2.2%      | No (BAO)  |
| 0.250     | 94.0%    | 0.748   | 0.892           | 0.864           | 15.0%   | 1.4%      | No (BAO)  |
| **0.260** | **97.7%**| **0.787**| **0.959**       | **0.948**       | **5.8%**| **0.5%**  | **YES**   |
| 0.270     | 101.5%   | 0.827   | 1.027           | 1.036           | 4.0%    | 0.3%      | YES       |

### Why the Shape Fails at Low Omega_chi

The EH shape parameter Gamma = Omega_m * h controls the P(k) turnover:

| Omega_chi | Gamma  | % of LCDM |
|-----------|--------|-----------|
| 0.000     | 0.033  | 15.6%     |
| 0.100     | 0.101  | 47.4%     |
| 0.200     | 0.168  | 79.1%     |
| 0.250     | 0.202  | 95.0%     |
| 0.266     | 0.213  | 100.1%    |

With insufficient chi, the matter-radiation equality epoch shifts to much later, placing the turnover at smaller k. This catastrophically suppresses power at k > 0.01 h/Mpc relative to LCDM.

### Relaxed Shape Criteria

| Tolerance | Min Omega_chi | % of CDM | Interpretation |
|-----------|---------------|----------|----------------|
| 10%       | 0.260         | 97.7%    | Standard BOSS  |
| 20%       | 0.250         | 94.0%    | Generous       |
| 30%       | 0.240         | 90.2%    | Very generous  |
| 50%       | 0.210         | 78.9%    | Barely constrained |
| 100%      | 0.000         | 0.0%     | No constraint  |

Even with 50% tolerance, chi must be at least 79% of CDM.

## Physical Interpretation

### MOND Cannot Replace the Transfer Function

MOND modifies gravity post-recombination. It can enhance structure growth to give the correct sigma_8. However:

1. **Pre-recombination**: The power spectrum shape is set by matter-radiation equality. Only pressureless matter (chi or CDM) can shift this epoch.

2. **Silk damping**: Without sufficient pressureless matter, baryonic perturbations are Silk-damped at k > 0.1 h/Mpc, creating a "wall" in the transfer function that no amount of post-recombination growth can fix.

3. **BAO position**: The sound horizon depends on Omega_m h^2. With only baryons, the sound horizon is 38% too large.

### The MOND Enhancement is Minimal

At Omega_chi = 0.260, the required MOND enhancement is only nu = 1.12 -- a mere 12% boost to baryon gravity. This is far from the deep-MOND regime and barely distinguishable from Newtonian gravity.

## Production Implications

**The transfer function constraint forces chi to provide essentially all of the CDM density.**

- Minimum Omega_chi ~ 0.260
- Required rho_chi ~ 2.2 x 10^-27 kg/m^3
- Chi/baryon ratio ~ 5.3 (same as CDM/baryon in LCDM)
- MOND contribution: negligible (nu ~ 1.12)

This means the chi production mechanism in DFD must be extremely efficient -- it must produce matter at the same abundance as standard CDM. The hope that MOND could reduce the chi requirement is not borne out by the P(k) shape constraint.

## Caveats

1. **EH approximation**: The Eisenstein-Hu fitting formula may not capture all physics of the baryon-chi coupled system. Full Boltzmann code (CLASS/CAMB) results could differ at the 5-10% level.

2. **No-wiggle only**: We use the smooth (no-wiggle) EH transfer function. BAO wiggles would provide additional constraining power.

3. **Scale-dependent MOND**: If MOND has scale-dependent effects pre-recombination (e.g., through density field coupling), it could modify the transfer function shape. This is not captured here.

4. **Non-standard expansion**: If Omega_m for expansion differs from the standard value, constraints would shift.

## Conclusion

**The minimum Omega_chi is 0.260 (97.7% of CDM), making MOND's contribution to the P(k) budget negligible.** The power spectrum shape is set at recombination by the amount of pressureless matter, and MOND -- which operates post-recombination -- cannot substitute for this. DFD's chi field must be produced at essentially the same abundance as standard CDM.
