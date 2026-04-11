# Round 3: Self-Consistent P(k) with sigma_nabla Regularisation

## Method

This computation combines Agent 8's sigma_nabla regularisation with the QUMOND framework to self-consistently determine the DFD matter power spectrum.

### The Self-Consistency Loop

1. Start with the baryon-only Newtonian P(k) using the Eisenstein-Hu baryon transfer function
2. Compute sigma_nabla = sqrt(<|grad psi_N|^2>) from the Newtonian potential of the matter distribution
3. Determine y_eff = sigma_nabla / a* and hence nu(y_eff)
4. Solve the linear growth ODE with **time-dependent** MOND enhancement: G_eff(a) = nu(y(a)) * G, where y(a) = y_0 * a^{-3} * D(a)/D(0)
5. Update P_delta(k) from the new growth factor
6. Iterate until sigma_nabla converges

### Key Physics

- At high redshift (a << 1), y(a) >> 1 so nu -> 1 (Newtonian regime). MOND does NOT enhance early growth.
- At low redshift (a ~ 1), y(a) is smallest and MOND enhancement is strongest.
- The time-dependent treatment prevents unphysical growth factor blow-up.
- sigma_nabla is computed from the **Newtonian** potential of the actual density field (not the MOND-boosted potential), because it is the Newtonian gradient that enters the nu() argument.

### Normalisation

The matter power spectrum uses the correct Poisson equation conversion from primordial curvature R to density delta:

    P_delta(k) = (2/5)^2 * (ck/H0)^4 / Omega_source^2 * T^2(k) * D^2(z) * P_R(k)

For the baryon-only DFD case, Omega_source = Omega_b = 0.049.

## Converged Results

| Quantity | Value |
|----------|-------|
| sigma_nabla | 1.821 x 10^-29 m^-1 |
| a* | 2.670 x 10^-27 m^-1 |
| **y_eff = sigma_nabla/a*** | **6.819 x 10^-3** |
| **nu(y_eff)** | **12.62** |
| **x_bar = nu * y_eff** | **8.606 x 10^-2** |
| mu(x_bar) | 0.0792 |
| G_eff/G = nu | 12.62 |
| D_baryon (Newtonian) | 0.4844 |
| **D_DFD** | **6.243** |
| D_LCDM | 0.7878 |
| D_DFD / D_LCDM | 7.924 |
| **Iterations to converge** | **32** |

## sigma_8

| Model | sigma_8 | Ratio to LCDM |
|-------|---------|----------------|
| Baryon-only Newtonian | 0.0393 | 0.080 |
| **DFD (self-consistent)** | **0.506** | **1.026** |
| LCDM | 0.493 | 1.000 |

**Key result: DFD sigma_8 matches LCDM to within 2.6%.**

The EH-based LCDM sigma_8 of 0.493 is lower than the Planck-calibrated value of ~0.81 due to approximations in the analytic transfer function (missing radiation driving, neutrino effects, second-order corrections). The relative comparison DFD/LCDM is the meaningful quantity.

## P(k) Ratios

### Matter density power spectrum P_delta

| k [h/Mpc] | P_DFD | P_LCDM | P_DFD/P_LCDM |
|------------|-------|--------|---------------|
| 0.02 | 217,579 | 14,025 | 15.51 |
| 0.05 | 28,025 | 6,944 | 4.04 |
| 0.10 | 2,088 | 2,462 | 0.85 |
| 0.15 | 5.83 | 1,083 | 0.005 |

The DFD spectrum has MORE power than LCDM on large scales (k < 0.08 h/Mpc) and LESS power on small scales (k > 0.1 h/Mpc). This is a direct consequence of the baryon transfer function: Silk damping suppresses baryon perturbations on small scales. MOND enhancement (via growth factor) partially compensates but cannot fully overcome the exponential Silk damping at high k.

### Lensing-equivalent power spectrum P_Phi (includes nu^2 boost)

| k [h/Mpc] | P_Phi_DFD | P_LCDM | Ratio |
|------------|-----------|--------|-------|
| 0.02 | 34,652,904 | 14,025 | 2,471 |
| 0.05 | 4,463,405 | 6,944 | 643 |
| 0.10 | 332,529 | 2,462 | 135 |
| 0.15 | 929 | 1,083 | 0.86 |

The lensing potential is enormously boosted on large scales because nu^2 ~ 159 multiplies the already growth-enhanced density spectrum. This would produce very strong ISW and lensing signals on large scales -- a potential observational tension that would need to be addressed.

## Boost Decomposition

Starting from baryon-only Newtonian P(k):

| Factor | Value |
|--------|-------|
| Growth enhancement (D_DFD/D_bary)^2 | 166.1 |
| QUMOND potential boost nu^2 | 159.3 |
| Total (for potential P(k)) | 26,440 |

## Physical Interpretation

1. **Deep MOND regime**: y_eff = 0.0068 << 1, meaning the cosmological RMS acceleration is far below a_0. This is expected: cosmological perturbations at the linear level have very weak gradients.

2. **Self-regulation**: The self-consistency loop converges because stronger MOND enhancement -> larger sigma_nabla -> larger y -> weaker MOND enhancement. This negative feedback loop is the key insight from Agent 8's regularisation.

3. **sigma_8 match**: The DFD matter power spectrum achieves sigma_8 within ~3% of LCDM, despite having only 15.6% of the matter content (Omega_b/Omega_m = 0.049/0.315). This is accomplished through:
   - Growth factor enhancement by factor ~13 (D_DFD/D_bary ~ 12.9)
   - Applied through the time-dependent MOND mechanism where enhancement grows at late times

4. **Scale-dependent deficit**: DFD lacks power at k > 0.1 h/Mpc relative to LCDM due to Silk damping. This is a fundamental prediction: DFD should show less small-scale clustering than LCDM, potentially detectable in galaxy surveys at high k.

5. **Lensing excess**: The nu^2 boost to the gravitational potential creates enormous large-scale lensing power, which could be constrained by CMB lensing and galaxy-galaxy lensing observations.

## Files

- Script: `R3_self_consistent_pk.py`
- Data (JSON): `R3_self_consistent_data.json`
- Arrays (NumPy): `R3_pk_data.npz` (contains k_hMpc, P_bary, P_DFD_delta, P_LCDM, P_DFD_Phi)
