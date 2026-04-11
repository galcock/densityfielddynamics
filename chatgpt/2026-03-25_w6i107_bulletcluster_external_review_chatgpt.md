# External Review: W6i107 Bullet Cluster

Date: 2026-03-25
Reviewer stance: external, read-only, closure-focused
Scope: newest material under `DFD_Research_Output/Cross_Reference_Updates`, centered on `W6i107_BulletCluster.tex` and tracker/roadmap consistency.

## Executive verdict

This run does not find a credible new closure. The newest file, [`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex), introduces a stronger Bullet Cluster claim, but that uplift is not bankable:

- the file appears internally inconsistent about the relevant `m_psi` scale;
- the quoted simulation outputs are still unreproducible from the local artifact base;
- the tracker and roadmap still treat Bullet Cluster as an open deficit, not a closed result.

## Fatal

### F1. `W6i107` uses mutually inconsistent `m_psi` scales inside the same Bullet Cluster argument

Evidence:

- The file sets the response time by `t_psi ~ 1/m_psi ~ 1/H_0 ~ 14 Gyr`: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L96).
- It then treats that slow timescale as the basis for merger-scale field freezing and for the `~200` lag ratio: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L103), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L122).
- But the initial-condition section says cluster superposition is valid because the inter-cluster distance is much larger than `m_psi^{-1}`: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L154), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L160).

Why this is fatal:

- If `t_psi ~ 1/H_0`, then the associated field scale is horizon-sized, not much smaller than a cluster separation.
- So the file cannot simultaneously use `m_psi^{-1}` as a cosmological response scale and also cite `d_intercluster >> m_psi^{-1}` as the reason the two-cluster Yukawa superposition is valid.
- That means the lag argument and the initial-condition argument are not working from one coherent physical scale. The claimed Bullet Cluster uplift is therefore unstable before reproducibility is even considered.

Required correction:

- Fix the unit/scale convention for `m_psi` and state one consistent relation between response time, Compton length, and cluster separation.
- Until that is repaired, the `1.4x` deficit result should not be treated as physical closure.

## Critical

### C1. The `256^3` Bullet Cluster result is still a text-only simulation claim

Evidence:

- The file says a particle-mesh N-body code was implemented and the `psi` field was evolved spectrally on a `256^3` grid: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L134), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L164).
- It reports concrete outputs: `kappa_peak`, `120 kpc` offset, and deficit reduction from `3x` to `1.4x`: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L216), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L277).
- In the reviewed tree I do not see a Bullet Cluster solver, parameter file, output dataset, run log, seed record, or convergence study accompanying that claim.

Why this is critical:

- The numerical result is still not locally reproducible.
- That makes the quoted simulation a surrogate for computation, not a validated computational artifact.

### C2. The new Bullet Cluster uplift is not reconciled with the project’s own tracker and roadmap

Evidence:

- The roadmap still frames Bullet Cluster as a genuine unresolved gap and treats non-equilibrium dynamics as work to be done, not as completed closure: [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L198), [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L206), [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L221).
- The tracker still records Bullet Cluster as downgraded but open, at `1.5-2.5x` deficit and only "within systematics with neutrinos": [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L845), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L866).
- `W6i107` instead presents `80-90%` explanatory power and a `1.4x` deficit as if the non-equilibrium route has now materially lifted the status: [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L253), [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L277).

Why this is critical:

- This is a source-of-truth problem, not just a messaging problem.
- A new branch-level uplift is being stated without an explicit supersession path from the existing honest-negative/open-deficit record.

## Bottom line

The newest Bullet Cluster file should be treated as exploratory, not as closure.

The gating problem is now twofold:

- the local artifact base still does not reproduce the claimed simulation;
- the paper’s own field-scale logic appears inconsistent inside `W6i107`.

Until both are fixed, Bullet Cluster remains an unresolved programme liability rather than a closed or nearly closed result.
