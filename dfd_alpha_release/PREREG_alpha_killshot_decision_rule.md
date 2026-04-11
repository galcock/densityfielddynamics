# DFD κᵣ → α Killshot: Preregistered Pass/Fail

## Objective
Measure renormalized gauge stiffnesses κᵣ for U(1) and SU(2) in the true DFD micro-action,
compute α, and declare PASS/FAIL with no post-hoc tuning.

## Measured outputs (artifacts)
- `artifacts/kappa_u1_<tag>.json`
- `artifacts/kappa_su2_<tag>.json`
- `artifacts/alpha_from_kappa_<tag>.json`

## Definitions
- g₁² = 1/κᵣ(U1)
- g₂² = 1/κᵣ(SU2)
- e²  = g₁² g₂² / (g₁² + g₂²)
- α   = e² / (4π)

## Required production conditions (minimum)
1. Lattice sizes: L ∈ {10, 12} (both), with a scaling check between them.
2. Seeds: ≥ 8 independent chains per (L, group).
3. Statistics per chain: sweeps ≥ 2e6; therm ≥ 2e5; measure_every tuned so ≥ 1e4 effectively independent samples.
4. Autocorrelation: report integrated τ_int for the f₂ estimator (S'' - (S')²); require ESS ≥ 2000 per chain.
5. Blocking/jackknife: report α_mean and α_se across chains; confirm stability under block size ×2 and ×4.

## PASS / FAIL threshold
Let α̂ be the combined estimator and σ_α its standard error across independent chains.

- PASS if |α̂ - α_PDGlike| ≤ 5σ_α
- FAIL if |α̂ - α_PDGlike| > 5σ_α

Where α_PDGlike is the reference fine-structure constant value used by the comparison table in the paper
(entered as a fixed constant in the analysis script, not tuned).

## No-tuning rule
No parameter changes after viewing α̂ except:
- increasing statistics / adding seeds,
- fixing *bug-level* failures indicated by unit tests.

All changes must be recorded as new `<tag>` runs.
