# ChatGPT Review: Wave 6 Closure Carry-Forward

Date: 2026-03-27
Reviewer stance: external, read-only, closure-focused

Scope:
- No files under `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates` were newer than the last run timestamp (`2026-03-27 00:53:21 PDT`).
- This pass therefore carries forward the highest-risk closure claims from the current Wave 6 packet and related control/master files, with added focus on Strong CP and Bullet Cluster.

## Executive verdict

There is still no audit-grade basis for treating the current Wave 6 cosmology and closure package as genuinely closed.

The dominant failure mode remains the same:
- computational and simulation results are written as completed outputs while the local artifact base still shows specification text, stubs, or no executable evidence;
- control documents disagree about what the canonical programme state even is;
- some theorem-grade closures are still surrogate proofs that explicitly leave the real renormalization/counterterm closure for future work.

## Fatal

### F1. i106 books completed cosmology outputs that the local implementation cannot reproduce

Evidence:
- [`W6i106_Compiled.tex#L63`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L63) upgrades recombination, `\Lambda`CDM recovery, TT/TE/EE residuals, `\chi^2/{\rm d.o.f.}=1.031`, `A_lens=1.004`, and `P(k)`/`S_8` into GREEN findings.
- [`W6i106_Compiled.tex#L90`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L90) then uses those numbers to justify a cosmology grade upgrade.
- [`W6i102_Cosmology_Sprint.tex#L180`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L180) still frames `mochi_class` as a specification and validation plan.
- [`DFDBolt.jl#L4`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L4) identifies the visible Julia artifact as `Wave 5, Iteration 57` and `Phase 0A: Bolt.jl integration layer`.
- [`DFDBolt.jl#L22`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L22) still has `using Bolt` commented out.
- [`DFDBolt.jl#L31`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L31) exports run functions, but the file ends at diagnostics in [`DFDBolt.jl#L209`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209) with no implementation of the claimed pipeline runners.

Why this is fatal:
- The local repo still supports, at most, an interface sketch plus analytic helper code.
- The reported fit statistics and spectra-level confrontations are therefore text-only claims, not reproducible computational results.

## Critical

### C1. The slip/lensing sign is still internally unstable across the Wave 6 cosmology packet

Evidence:
- [`W6i102_Cosmology_Sprint.tex#L128`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L128) defines `\Psi/\Phi = 1 + \eta_\psi` and frames `\eta_\psi` as a positive detectable enhancement.
- [`W6i106_Compiled.tex#L74`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L74) promotes that into `A_lens^{DFD}=1.004`.
- [`DFDBolt.jl#L104`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L104) instead states `Psi/Phi = -(1 + 2*eta_psi) where eta_psi < 0`.
- [`DFDBolt.jl#L126`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L126) also states `Sigma/mu = 1 + eta_psi < 1`.

Why this is critical:
- This is not a cosmetic convention issue. It changes the physical direction of the lensing correction.
- Until the sign and observable mapping are reconciled, the `A_lens`, `P(k)`, and weak-lensing narrative are not stable enough to book as closure.

### C2. The control docs still fail lineage, so no new “terminal” or “grade-upgraded” state is trustworthy

Evidence:
- [`ITERATION_TRACKER.md#L3`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L3) still opens with `Target: 20 iterations`.
- [`ITERATION_TRACKER.md#L223`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L223) says convergence was reached at iteration 8 and iteration 9 was final.
- [`ITERATION_TRACKER.md#L241`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L241) says `PROGRAMME COMPLETE` with total iterations `9`.
- [`ITERATION_TRACKER.md#L256`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L256) then immediately continues into `Iteration 10 (Wave 4, Iteration 1)`.
- [`DFD_Master_Findings_FINAL_i1_to_i100.tex#L46`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L46) calls itself the `definitive final version` and `terminal state`.
- [`W6i106_Compiled.tex#L138`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L138) says `Iterations completed: 106`.

Why this is critical:
- A reviewer still cannot tell which state ledger supersedes which.
- That is a sink-loop pattern: new synthesis layers continue to accumulate without a canonical state register.

### C3. The master “zero RED / zero contradictions” closure language is still not compatible with the tracker’s own recorded falsifications and dead ends

Evidence:
- [`DFD_Master_Findings_FINAL_i1_to_i100.tex#L32`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L32) advertises `97/3/0` and `Zero RED`.
- [`DFD_Master_Findings_FINAL_i1_to_i100.tex#L55`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L55) says `Total RED across programme: 0`.
- [`DFD_Master_Findings_FINAL_i1_to_i100.tex#L65`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L65) says `Contradictions found: 0`.
- [`DFD_Master_Findings_FINAL_i1_to_i100.tex#L104`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L104) says no RED finding has ever been recorded.
- But the tracker records `GENUINE FALSIFICATION` and `GENUINE TENSION` states in [`ITERATION_TRACKER.md#L123`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L123) and [`ITERATION_TRACKER.md#L126`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L126).
- It also records dead-end status such as `P8 comms EFFECTIVELY DEAD` and `P1 FINAL: zero resources recommended` in [`ITERATION_TRACKER.md#L190`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L190) and [`ITERATION_TRACKER.md#L191`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L191).

Why this is critical:
- The final master file still reads as closure narrative rather than conservative audit record.
- If falsifications, dead patents, and major reversals exist in the programme history, they must be explicitly reclassified, not erased by scoreboard compression.

### C4. The Strong CP “two-loop proof complete” remains a surrogate proof, not real closure

Evidence:
- [`W6i101_Quick_Wins.tex#L57`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L57) sets the objective as a `complete two-loop proof`.
- [`W6i101_Quick_Wins.tex#L213`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L213) states the theorem `\delta\bar\theta^{(2)} = 0`.
- The proof logic is that the relevant Euclidean integrals, color factors, and masses are real, see [`W6i101_Quick_Wins.tex#L220`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L220).
- But the same file explicitly concedes that a rigorous all-orders closure would require showing the BRST cohomology admits no CP-odd counterterms, which is left to future work in [`W6i101_Quick_Wins.tex#L242`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242).
- Despite that, [`W6i105_Assessment.tex#L172`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L172) says `The 2-loop proof is complete`.

Why this is critical:
- “diagram contributions are real in Euclidean signature” is not equivalent to “renormalized theory cannot generate a CP-odd term”.
- The missing counterterm/cohomology step is exactly the part that separates a persuasive sketch from theorem-grade closure.

### C5. Bullet Cluster is still being advanced through narrative escalation, not traceable simulation evidence

Evidence:
- [`W6i105_Assessment.tex#L190`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L190) lists Bullet Cluster resolution as a blocker and says it was not attempted in the A+ sprint at [`W6i105_Assessment.tex#L193`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L193).
- [`W6i107_BulletCluster.tex#L134`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L134) then claims a particle-mesh N-body implementation on a `256^3` grid.
- [`W6i107_BulletCluster.tex#L208`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L208) reports exact post-merger convergence values and offsets.
- [`W6i107_BulletCluster.tex#L277`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L277) upgrades the result into GREEN findings.
- A file scan of the same directory found no Bullet Cluster simulation code, parameter sets, outputs, or snapshots; only [`W6i107_BulletCluster.tex`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex) and an unrelated [`derive_kappa.py`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/derive_kappa.py).

Why this is critical:
- This is the same closure problem as i106 in a simulation context.
- A same-day jump from “not attempted” to quantified `256^3` simulation outputs is not auditable without new code and output artifacts.

## Bottom line

This packet is still best treated as an advanced internal draft branch, not a closed review corpus.

The minimum gating repairs remain:
- one canonical supersession ledger for tracker/master status;
- executable cosmology and Bullet Cluster artifacts for every quoted numerical result;
- explicit separation between heuristic argument, partial perturbative result, and theorem-grade proof.
