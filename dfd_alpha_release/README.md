# Ab Initio Evidence for the Fine Structure Constant from Density Field Dynamics

Author: G. Alcock
Priority date: December 27, 2025

## What this is

Simulation code and compiled results for the lattice Monte Carlo derivation of alpha = 1/137 from the DFD gauge-emergence microsector. Three inputs, all fixed before any simulation was run:

1. Beta_U1 = 3.80 from the truncated SU(2) Chern-Simons weighted average at k_max = 60
2. Beta_SU2 / Beta_U1 = 6 from Wilson normalization conventions
3. Kappa_U1 / Kappa_SU2 = 1/2 from DFD Theorem F.13

## How to reproduce

Requirements: Python 3.10+, numpy

python3 run_kappa_alpha.py --outdir results --tag reproduce_L6 --u1_L 6 --u1_sweeps 30000 --u1_therm 3000 --u1_meas 10 --u1_beta 3.80 --u1_seed 42 --su2_L 6 --su2_sweeps 30000 --su2_therm 3000 --su2_meas 10 --su2_beta 22.80 --su2_eps 0.35 --su2_seed 1042

Expected: alpha_W approximately 0.00730, within 0.5% of physical value 0.0072973525693.

## Key results

L=6: alpha=0.007297 (-0.00%)
L=8: alpha=0.007322 (+0.34%)
L=10: alpha=0.007361 (+0.88%)
L=12: alpha=0.007291 (-0.08%)

The converged infinite sum gives alpha=1/303, ruled out at greater than 50 sigma.

## Contact

Email listed on the paper.
