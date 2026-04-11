# ChatGPT Review: W6i101 / W6i106 / Tracker Closure Drift

Date: 2026-03-24

Scope: new findings not already covered by the earlier `W6i106_i107_REVIEW_chatgpt.md`. This pass focuses on surrogate-proof closure, tracker/state drift, and internal contradiction between newly claimed cosmology numbers and the programme's own prior "authoritative" corpus.

## Executive Verdict

The immediate risk is not just missing artifacts. It is bookkeeping closure before the underlying epistemic state is stable.

Three issues stand out:

- `W6i101_Quick_Wins.tex` books a theorem-grade Strong CP closure from a diagram-reality argument that does not establish the absence of CP-odd counterterms or anomalous phase generation.
- the active tracker now fails lineage: it still presents the programme as an early 20-iteration Wave 3 process even while `W6i106_Compiled.tex` says 106 iterations are complete.
- `i106` introduces new `A_lens` and `S_8` values that conflict with multiple earlier "authoritative" programme states, so these numbers are not yet safe to treat as real closure rather than a fresh branch.

## Fatal

### F1. `W6i101` upgrades Strong CP to "complete two-loop proof" using a surrogate proof criterion

Evidence:
- [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L57) states the objective is a "complete two-loop proof".
- [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L213) then concludes `delta bar-theta^(2) = 0`.
- The proof logic is explicitly that each diagram is real in Euclidean signature, with real color factors and real masses: [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L220).
- But the file itself immediately concedes that an actual all-orders closure would require showing the BRST cohomology admits no CP-odd counterterms, which is left to future work: [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242).

Why this is fatal:
- "all relevant integrands are real in Euclidean signature" is not equivalent to "the renormalized theory cannot generate a `theta` term."
- The document never demonstrates regulator consistency, anomaly matching, operator mixing, or counterterm exclusion.
- So this is not real closure of Strong CP. It is a text-level surrogate proof that at best motivates a conjecture.

Required correction:
- Downgrade the claim from theorem-grade closure to a partial perturbative argument unless the renormalization/counterterm part is actually closed.

## Critical

### C1. The tracker is now internally untrustworthy as a programme-state ledger

Evidence:
- The active cross-reference tracker still opens with `Target: 20 iterations` and `Status: IN PROGRESS`: [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L3).
- The same tracker still narrates Wave 3 convergence and "Programme complete" around iteration 9: [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L223), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L241).
- Yet `W6i106_Compiled.tex` states `Iterations completed: 106` and `Total findings: 447`: [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L138).

Why this is critical:
- A reviewer can no longer tell which state is canonical.
- This is a sink-loop failure mode: the programme keeps generating new synthesis documents without first reconciling the state register that says what has actually been superseded.
- Once the tracker fails lineage, later "resolved" or "authoritative" statements stop being bookable as closure.

Required correction:
- Establish one canonical state ledger and mark superseded trackers/corpora explicitly.
- Until then, all new grade changes should be treated as provisional branch outputs, not stable programme state.

### C2. `i106` cosmology claims contradict prior "authoritative" DFD cosmology states on the same observables

Evidence:
- `i106` claims `A_lens = 1.004` and presents this as the DFD lensing prediction: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L107), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L74), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L123).
- But the master findings corpus previously recorded `A_L^DFD ~ 1.10-1.20` as a DFD prediction and explicitly said DFD "resolves" the anomaly that way: [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L445), [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L497).
- `i106` also claims `S_8^DFD = 0.840`: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L189), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L76), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L119).
- But the corpus and later master list had already moved through materially different DFD states such as `S_8^DFD ~ 0.77-0.79`, then `0.801`, with explicit framing that these were the consistent DFD values: [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L18), [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L734), [MASTER_FINDINGS_LIST.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L1875).

Why this is critical:
- This is not a small refinement. It is a branch-level change in what the theory is claimed to predict for the same headline observables.
- Without an explicit supersession chain, the new numbers cannot be booked as "closure"; they are just the latest branch output.
- The problem is epistemic, not cosmetic: the same programme now supports mutually incompatible "authoritative" values.

Required correction:
- Add a supersession table for `A_lens`, `S_8`, and related cosmology observables showing:
  - old value
  - new value
  - why the old value was wrong
  - which code path or assumption changed
- Until that exists, do not call the cosmology bottleneck "attacked" in a closure sense.

## Bottom Line

The current failure mode is overbooking.

`i106` may still be useful work, and `i101` may still contain promising mathematical structure, but neither is yet safe to bank as genuine closure. The programme first needs a stable supersession discipline: one canonical tracker, one canonical cosmology state, and a hard distinction between heuristic argument, executable result, and theorem-grade proof.
