# ChatGPT Nonstop Review: W6i105 / W6i107 / Tracker Context

Date: 2026-03-27

Scope: external, read-only review of the latest unreconciled `Cross_Reference_Updates` frontier and related state files. I did not find files under `DFD_Research_Output/Cross_Reference_Updates` newer than the last-run timestamp (`2026-03-27T20:51:15Z`), so this pass targets the newest available branch artifacts that still drive closure language: [`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex), [`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex), plus tracker/roadmap context.

## Executive Verdict

This pass still does not surface a bankable closure. The main problem is not just missing code. The newer Bullet Cluster writeup now relies on surrogate inference and hand-added uplift percentages, while the assessment ledger continues to book Strong CP as internally complete even though the underlying proof file still leaves the renormalization/counterterm gate open.

## Fatal

### F1. `W6i107` does not prove the claimed Bullet Cluster memory mechanism; it proves non-adiabaticity, then upgrades that to pre-merger profile retention

Evidence:

- The core proposition says that because `t_psi >> t_cross`, the field is "effectively frozen" and therefore approximately tracks the pre-merger mass distribution: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L103).
- But the proof only derives `|delta psi| / |psi_eq| ~ 200`: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L120).
- The conclusion then jumps from "`|delta psi|` is much larger than post-merger equilibrium" to "the field remains close to its pre-merger configuration": [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L125).

Why this is fatal:

- `|delta psi| >> |psi_eq,post|` only shows the adiabatic approximation fails. It does not establish that the solution stays near the pre-merger profile rather than oscillating, dispersing, or developing a different non-equilibrium configuration.
- So the central physical mechanism for the claimed offset is not actually derived. This is surrogate proof by narrative interpretation of one scaling ratio.
- Until the memory effect itself is demonstrated from the evolution, the later numerical uplift cannot be booked as real closure.

Required correction:

- Separate "non-adiabatic response" from "pre-merger profile retention" as distinct claims.
- Only claim merger-memory closure if the time evolution or explicit outputs actually show retention of the required offset pattern.

## Critical

### C1. `W6i107` closes its remaining Bullet Cluster gap with uncomputed percentage patches, not reproduced calculations

Evidence:

- The file reports concrete simulation-style outputs at `t = 0.5 Gyr`: `kappa_peak`, `120 kpc` offset, and `8:1` mass ratio: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201).
- It then attributes the remaining deficit to three additive effects: galaxy contribution `30--40%`, profile improvement `20--30%`, and projection effects `10--20%`: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L233).
- On that basis it promotes a proposition that DFD can explain `80--90%` of the observed convergence and that the rest is within systematics: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L253).

Why this is critical:

- Those gap-closing percentages are not shown as outputs of the stated simulation.
- The document is therefore moving from one unreproduced computational claim to a stronger closure claim by adding scenario-level corrections that are themselves not computed here.
- That is exactly the kind of sink-loop behaviour that makes a hard problem look nearly closed without actually closing it.

Required correction:

- Distinguish simulated outputs from speculative uplift terms.
- Do not aggregate unrun corrections into an "80--90%" closure statement unless those corrections are separately computed and archived.

### C2. `W6i105` books Strong CP as internally complete even though the source proof file explicitly leaves the counterterm/cohomology gate open

Evidence:

- The assessment marks the Strong CP sector as having "2-loop proof done" and says the only blocker is peer-reviewed publication: [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L91), [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L170).
- It also says "Internal work needed: None. The 2-loop proof is complete": [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L172).
- But the underlying source file still states that a rigorous all-orders result would require showing BRST cohomology admits no CP-odd counterterms, and explicitly leaves that to future work: [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L234).

Why this is critical:

- The assessment layer is hardening a provisional proof into programme-state bookkeeping.
- That contaminates downstream grade changes, priorities, and "only submission remains" language.
- This is a state-ledger sink loop: unresolved internal work disappears at the assessment layer even though the source derivation still flags the missing closure condition.

Required correction:

- The assessment should preserve the distinction between "two-loop perturbative argument" and "internally closed theorem-grade result."
- Until the counterterm/cohomology issue is actually closed, Strong CP should remain marked as technically incomplete rather than publication-ready by bookkeeping alone.

## Bottom Line

The highest-risk pattern remains overbooking:

- `W6i107` upgrades a hard astrophysical tension using a non-adiabaticity argument that does not prove the claimed memory effect, then narrows the remaining deficit with uncomputed correction percentages.
- `W6i105` propagates a still-incomplete Strong CP result into the programme ledger as if nothing internal remained.

These are not cosmetic issues. They are closure-discipline failures. Real closure still needs executable lineage for computational claims and a stricter separation between partial arguments, speculative uplift, and bankable result states.
