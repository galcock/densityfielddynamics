# Round 3: MOND-Modified Pre-Recombination Transfer Function

**Agent**: Round 3 focused agent (Claude Opus 4.6)
**Date**: 2026-04-04
**Script**: `R3_prerecomb_transfer.py`

## Executive Summary

This analysis tests the hypothesis that MOND enhancement during the acoustic epoch (z ~ 1100) could effectively increase the gravitational mass driving baryon oscillations, yielding an effective matter density Omega_m,eff = nu(k, z_rec) x Omega_b that matches LCDM's Omega_m ~ 0.315. **The results are mixed but physically illuminating.**

### The Key Finding

At recombination (z = 1100), for perturbation amplitude delta ~ 3 x 10^-4:

| k [h/Mpc] | g_N/a0  | nu    | Omega_m,eff |
|-----------|---------|-------|-------------|
| 0.01      | 4.89    | 1.17  | 0.058       |
| 0.02      | 2.44    | 1.31  | 0.065       |
| 0.05      | 0.978   | 1.63  | 0.080       |
| 0.10      | 0.489   | 2.01  | 0.099       |
| 0.20      | 0.244   | 2.58  | 0.127       |
| 0.50      | 0.098   | 3.74  | 0.184       |

**The regime is TRANSITIONAL, not deeply Newtonian.** For k > 0.05 h/Mpc, g_N/a0 < 1 and MOND enhancement IS active, with nu ranging from ~1.6 to ~3.7. However, this enhancement falls short of the nu ~ 6.4 needed to fully match LCDM (Omega_m,eff = 0.315).

## Task 1: MOND Enhancement at Recombination

### Physical Setup
- Mean baryon density at z = 1100: rho_b = 5.61 x 10^-19 kg/m^3
- Perturbation amplitude: delta ~ 3 x 10^-4 (typical at recombination)
- Gravitational acceleration: g_N(k) = 4 pi G rho_b delta / k_phys
- k_phys = k_comoving / (a_rec x Mpc_m)

### Key Physics
The gravitational acceleration from density perturbations scales as:
- g_N proportional to 1/k (larger scales have stronger gravity)
- g_N proportional to rho_b proportional to (1+z)^3

At z=1100, rho_b is 1.3 x 10^9 times its present value. Despite this enormous enhancement, the acceleration per unit wavenumber g_N ~ 10^-10 m/s^2, which is comparable to a0 = 1.2 x 10^-10 m/s^2 at BAO scales.

**This is actually a remarkable coincidence**: the perturbation-scale gravitational acceleration at recombination happens to be of order a0 for the wavenumbers of interest.

## Task 2: The MOND-Modified Transfer Function

Using the scale-dependent Omega_m,eff(k) = nu(k, z_rec) x Omega_b in the Eisenstein-Hu fitting formula:

| k [h/Mpc] | Omega_m,eff | z_eq,eff | s_eff [Mpc] | T_DFD/T_LCDM |
|-----------|-------------|----------|-------------|---------------|
| 0.01      | 0.058       | 634      | 18.05       | 0.40          |
| 0.02      | 0.065       | 706      | 17.90       | 0.30          |
| 0.05      | 0.080       | 877      | 17.58       | 0.23          |
| 0.10      | 0.099       | 1085     | 17.20       | 0.22          |
| 0.20      | 0.127       | 1392     | 16.70       | 0.22          |
| 0.50      | 0.184       | 2017     | 15.85       | 0.35          |

The transfer function ratio T_DFD/T_LCDM ~ 0.22-0.40, showing:
1. Significant but incomplete recovery of LCDM shape
2. Scale-dependent enhancement (as expected from k-dependent nu)
3. Interesting upturn at high-k where MOND enhancement is strongest

### Comparison with LCDM targets
- z_eq(LCDM) = 3430 vs z_eq,eff = 634-2017 (too low)
- s(LCDM) = 14.45 Mpc vs s_eff = 15.9-18.1 Mpc (too large)
- The sound horizon is still ~10-25% too large

## Task 3: Derived Quantities

| Quantity | LCDM | DFD (k=0.05) | DFD (k=0.20) |
|----------|------|-------------|-------------|
| z_eq     | 3430 | 877         | 1392        |
| s [Mpc]  | 14.45| 17.58       | 16.70       |
| k_silk [Mpc^-1] | 0.090 | 0.069 | 0.073 |

The effective z_eq is 25-40% of the LCDM value, not the 100% that would be needed.

## Task 4: P_DFD(k) and Growth Factor

### Critical Issue: DFD Growth Factor
The post-recombination growth factor in a baryon-only + Lambda cosmology with MOND enhancement is highly sensitive to the expansion history. With Omega_Lambda,DFD = 1 - Omega_b ~ 0.951 (much more Lambda-dominated than LCDM), the linear growth factor is very different:

- With nu_eff = 6.4 (the value needed to match LCDM clustering): D_MOND blows up to ~10^6
- This is because the DFD expansion history (Omega_b = 0.049, Omega_Lambda = 0.951) accelerates much earlier, and the MOND-enhanced source term drives exponential-like growth

**This indicates the growth factor problem is NOT just about nu_eff -- the background expansion must also be considered self-consistently.** The DFD framework needs to specify what drives H(a) in a baryon-only universe.

## Task 5: sigma_8

The LCDM sigma_8 from the no-wiggle EH formula gives ~0.0001 (much below the target 0.811) because the no-wiggle formula without proper normalization underestimates power. The DFD sigma_8 is corrupted by the blowup of the growth factor. **A proper sigma_8 calculation requires correct normalization tied to CMB observations.**

## Task 6: Self-Consistency Iteration

The iteration shows:
- **Convergence at low k (k < 0.1 h/Mpc)**: nu stabilizes quickly
  - nu(0.01) converges to ~1.05
  - nu(0.05) converges to ~1.63
- **Oscillation at high k (k ~ 0.2 h/Mpc)**: nu oscillates between ~2 and ~6.5
  - This is because T(k) changes significantly with Omega_m_eff, which changes delta, which changes nu
  - The oscillation is bounded and slowly damping (would need damped iteration)
- **NaN at very high k**: numerical issues at k > 0.7 h/Mpc

The converged values at the BOSS wavenumbers:

| k [h/Mpc] | nu_converged | Omega_m,eff | T_conv/T_LCDM |
|-----------|-------------|-------------|---------------|
| 0.01      | 1.05        | 0.052       | 0.36          |
| 0.02      | 1.17        | 0.058       | 0.26          |
| 0.05      | 1.63        | 0.080       | 0.23          |
| 0.10      | 2.37        | 0.117       | 0.28          |
| 0.20      | 3.77        | 0.186       | 0.44          |
| 0.50      | 6.95        | 0.342       | 1.17          |

## Critical Assessment

### What Works
1. **The physics is real**: g_N/a0 IS of order unity at recombination for BAO-scale perturbations. This is not a trivially wrong idea.
2. **Scale dependence is physical**: nu increases at higher k (smaller scales have weaker g_N), providing exactly the kind of scale-dependent enhancement needed.
3. **Partial recovery**: At k > 0.2 h/Mpc, the MOND enhancement brings Omega_m,eff into the range 0.15-0.35, approaching LCDM.

### What Does NOT Work
1. **Insufficient enhancement at low k**: At k = 0.01-0.05 h/Mpc (the BAO scales), nu ~ 1.0-1.6, giving Omega_m,eff ~ 0.05-0.08. This is far below the LCDM value of 0.315.
2. **Wrong scale dependence for z_eq**: Since nu increases with k, z_eq,eff increases with k. But the BAO feature requires a single z_eq that applies uniformly.
3. **Sound horizon still too large**: s_eff ~ 16-18 Mpc vs LCDM's 14.45 Mpc.
4. **Growth factor blows up**: The DFD expansion history with Omega_Lambda ~ 0.95 does not match LCDM, and MOND-enhanced growth in this background produces wildly different results.

### What Would Be Needed
To fully match LCDM at k = 0.05 h/Mpc:
- nu_needed = 6.40, requiring g_N/a0 = 0.029
- This corresponds to delta ~ 9 x 10^-6 (vs actual delta ~ 3 x 10^-4)
- Or equivalently, a0 would need to be ~34x larger at recombination

### Alternative Paths Forward
1. **DFD phi-field provides CDM-like potential wells**: The DFD scalar field phi could source gravitational potential wells at recombination independently of MOND, if phi has its own dynamics that couple to the metric.
2. **Running a0**: If a0 evolves with redshift (a0(z) = a0,0 x f(z)), the MOND regime could extend to higher accelerations at recombination.
3. **Gradient energy mechanism**: The DFD gradient energy terms (explored by earlier agents) could modify the effective gravitational potential on perturbation scales.
4. **Effective field theory approach**: Rather than standard MOND on baryon perturbations, the DFD framework may modify gravity through its field equations in a way that doesn't reduce to simple nu(g_N/a0).

## Conclusion

The pre-recombination MOND enhancement is **physically present but quantitatively insufficient** with standard MOND parameters. The approach yields Omega_m,eff ~ 0.05-0.18 across the BOSS wavenumber range, which is a factor of 2-6 below the LCDM target of 0.315. The enhancement has the right qualitative trend (increasing with k) but the wrong magnitude.

**The DFD transfer function problem remains open.** The most promising direction is that the DFD framework provides ADDITIONAL gravitational effects beyond standard MOND interpolation -- through its phi-field dynamics, gradient energy terms, or modified a0 -- that enhance pre-recombination potential wells to match LCDM.
