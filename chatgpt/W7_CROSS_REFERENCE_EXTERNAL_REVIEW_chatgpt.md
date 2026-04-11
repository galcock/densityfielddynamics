# External Review: Cross Reference Updates W6 and Master Files

Date: 2026-03-24
Reviewer stance: external, read-only, closure-focused
Scope reviewed:
- `DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`
- `DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md`
- `DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex`
- `DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex`
- `DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl`
- `DFD_Research_Output/Cross_Reference_Updates/DFDGravity.jl`

## Executive result

This batch does not justify real closure. The dominant failure mode is surrogate closure: polished narrative documents present quantitative completion, fit quality, simulation output, and terminal scorecards that are not supported by the local computational artifacts, and in several places are contradicted by those artifacts.

## Fatal and critical findings

### 1. Fatal: i106 cosmology claims are presented as completed numerical results, but the local codebase only contains a Phase 0A interface stub and cannot reproduce the quoted outputs

Evidence:
- `W6i106_Boltzmann_Core.tex` claims "`DFDBolt.jl` now includes a Seager-level recombination module" and "`HyRec` shows agreement to `< 0.1%`" at [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L147), [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L150), [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L377).
- The same file quotes exact CLASS comparison numbers, gauge-invariance numbers, Planck residual structure, and `chi^2` values at [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L226), [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L252), [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L313).
- `W6i106_Compiled.tex` upgrades those same numbers into GREEN findings F433-F447, including `TT+TE+EE: chi^2/d.o.f. = 1.031` and `P(k)`/`S8` outputs at [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L63), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L71), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L74), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L75).
- But `DFDBolt.jl` explicitly identifies itself as "`Wave 5, Iteration 57`" and "`Phase 0A: Bolt.jl integration layer`" at [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L4), [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L5).
- The exported functions advertised in the header for actually running spectra and comparisons are not implemented. `rg` finds only `modified_poisson!`, `modified_slip`, `lensing_factor`, and `compare_spectra`; there is no `run_LCDM_validation`, `run_DFD_spectrum`, or `compare_to_CLASS` implementation anywhere in the file. The file ends at line 209 after diagnostics only at [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L1), [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209).

Why this is fatal:
- The i106 package is being treated as computational closure.
- The local artifact base supports at most an interface sketch plus simple background/slip utilities.
- Without the solver, recombination implementation, external likelihood inputs, and saved outputs, the quoted numerical fit metrics are text-only claims, not reproducible results.

### 2. Critical: the W6 cosmology narrative contradicts the local gravity code on the sign and interpretation of the slip/lensing correction

Evidence:
- `W6i102_Cosmology_Sprint.tex` defines `Psi/Phi = 1 + eta_psi` and says `eta_psi ~ O(alpha) ~ 10^-2`, framing it as a positive late-time detectable enhancement at [W6i102_Cosmology_Sprint.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L126).
- `W6i106_Lensing_Pk.tex` then turns that into a positive lensing enhancement and reports `A_lens^DFD = 1.004` at [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L110), [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L127).
- By contrast, `DFDBolt.jl` states "`eta_psi < 0`" and that negative `eta_psi` means "lensing mass < dynamical mass" at [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L105), [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L107).
- `DFDGravity.jl` reinforces that sign convention: "`Sigma < mu`" and "`SIGN: eta_psi < 0 always (lensing weaker than dynamics)`" at [DFDGravity.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDGravity.jl#L173), [DFDGravity.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDGravity.jl#L207).

Why this is critical:
- The sign of the slip feeds directly into `A_lens`, `P(k)`, and the claimed cosmology fit narrative.
- This is not a minor convention mismatch: the prose and the code imply opposite physical effects.
- Until the sign convention and the derived observables are reconciled, the i102/i106 cosmology closure is internally unstable.

### 3. Critical: the Bullet Cluster file reports a concrete 256^3 simulation and quantitative post-merger outputs with no local code, data products, or run records

Evidence:
- `W6i107_BulletCluster.tex` says a particle-mesh N-body code was implemented on a `256^3` grid, following Springel and Farrar, with the `psi` field evolved by a spectral method at [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L135), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L164).
- It then reports exact numerical outputs: `kappa_peak` values, `120 kpc` offset, and deficit reduction from `3x` to `1.4x` at [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L208), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L217), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L277).
- A file scan of `Cross_Reference_Updates` finds no Bullet Cluster code, no N-body implementation, no parameter files, and no output data products. The only Bullet Cluster artifact present is the `.tex` file itself.

Why this is critical:
- The document promotes a computationally expensive simulation result to quasi-closure status.
- Locally, it is unreproducible and unsupported.
- That makes the result a text-only surrogate for a simulation, not a simulation-backed finding.

### 4. Critical: the final master “zero RED / zero contradictions / terminal closure” narrative conflicts with the tracker’s own recorded falsifications, dead ends, and reversals

Evidence:
- `DFD_Master_Findings_FINAL_i1_to_i100.tex` claims `97/3/0`, `Zero RED`, `Contradictions found: 0`, and "No RED finding has ever been recorded across 100 iterations" at [DFD_Master_Findings_FINAL_i1_to_i100.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L32), [DFD_Master_Findings_FINAL_i1_to_i100.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L65), [DFD_Master_Findings_FINAL_i1_to_i100.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L104).
- But `ITERATION_TRACKER.md` explicitly records `T1` as a "GENUINE FALSIFICATION" before later re-resolution attempts at [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L117), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L123).
- The tracker also declares `P8 comms EFFECTIVELY DEAD` and `P1 FINAL: zero resources recommended` at [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L190), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L191).
- It later records a convergence/triage summary with `DEAD(2): P1,P8` at [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L210), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L211).

Why this is critical:
- A programme history containing explicit falsification declarations, dead patents, and major reversals cannot be faithfully compressed into “zero RED ever” without a rigorous reclassification audit.
- The final master file is functioning as a closure narrative, not as a conservative audit artifact.

### 5. Critical: master-status and publication scoreboards are not traceable across the project’s own summary files

Evidence:
- `MASTER_FINDINGS_LIST.tex` presents the programme as `i1--i90` with `2 accepted`, `1 published`, `13 under review` at [MASTER_FINDINGS_LIST.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L47), [MASTER_FINDINGS_LIST.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L51).
- One day later, `DFD_Master_Findings_FINAL_i1_to_i100.tex` claims `10 published`, `11 accepted`, `6 under review`, `459 citations`, `4133 papers scanned`, and `5/5 adversarial audits passed` at [DFD_Master_Findings_FINAL_i1_to_i100.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L59), [DFD_Master_Findings_FINAL_i1_to_i100.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L66).
- The local corpus reviewed here does not provide the underlying acceptance letters, publication artifacts, citation source table, or audit records needed to justify that jump.

Why this is critical:
- The scoreboards are being used as evidence of maturity and closure.
- Without supporting records, they are status assertions, not audit-grade facts.

### 6. Critical: W6 assessment says Bullet Cluster work was not attempted in the A+ sprint, but W6i107 immediately presents it as a quantified simulation result

Evidence:
- `W6i105_Assessment.tex` says the galactic blocker is "Bullet Cluster resolution + SPARC galaxy fits" and explicitly marks Bullet Cluster as "Not attempted in A+ Sprint: Deferred to i106+ due to priority" at [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L189), [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L193).
- `W6i107_BulletCluster.tex`, dated the same day, reports a completed `256^3` simulation with quantitative table outputs and GREEN findings at [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L135), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L208), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L277).

Why this is critical:
- A same-day shift from "not attempted" to detailed simulation outputs is only credible if accompanied by new code/data artifacts.
- None are present locally.
- This is a classic sink-loop pattern: unresolved blocker becomes “resolved” by narrative escalation rather than traceable work product.

## Secondary concerns

### 7. W6i102 repeatedly labels parameters and pipeline elements as “zero free parameters” while relying on derived observational inputs that are not shown as uniquely fixed locally

Examples:
- `dfd_params.ini` with "zero free parameters" at [W6i102_Cosmology_Sprint.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L206).
- i106 later uses a parameter table including `H0`, `Omega_c h^2`, `tau_reion`, `n_s`, and `A_s` as if all are fully theory-derived at [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L276).

This may be defensible in a long derivation chain, but in the local review set it is not demonstrated at audit level.

### 8. The final master file uses documentary confidence language that exceeds what the local artifact trail can carry

Examples:
- "definitive final version"
- "terminal programme state"
- "zero contradictions"
- exact citation and publication counts

Those phrases are closure-grade. The local support is not.

## Reviewer conclusion

The current W6/master package is not blocked by minor polish issues. It is blocked by closure hygiene:

1. Claimed numerical closures must be backed by executable code, inputs, and saved outputs.
2. The sign convention and physical interpretation of `eta_psi`, `Sigma`, and lensing must be made internally consistent before cosmology findings can be trusted.
3. The Bullet Cluster result must not be treated as a real simulation result until code and outputs exist locally.
4. The final master scorecard must be downgraded from terminal closure language until the tracker’s own falsifications, dead ends, and reversals are formally reconciled.

Without those repairs, the present state reads as an advanced internal draft set, not an audit-passing closure corpus.
