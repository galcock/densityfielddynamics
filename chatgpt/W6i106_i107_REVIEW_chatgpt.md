# ChatGPT Review: W6i106-i107 Reproducibility and Closure Check

Date: 2026-03-24

Scope: review of the remaining on-disk Wave 6 sprint artifacts. I found `W6i106_*` and `W6i107_BulletCluster.tex` in the repo. I did **not** find `W6i108-W6i110` artifacts on disk at the time of review.

## Executive Verdict

There is real progress here, but the main problem is not the ideas. It is the gap between:

- what the sprint documents claim numerically
- what the code and reproducibility artifacts currently support on disk

Right now, i106 and i107 should be treated as **promising draft results**, not yet as safely booked sector upgrades.

## Fatal / Sink Issues

### F1. i106 claims a full Boltzmann confrontation, but the on-disk code is still scaffold-level in key places

Evidence:
- [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67) claims `1.1%` TT residuals vs Planck with zero free parameters.
- [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L71) claims combined `chi^2/d.o.f. = 1.031`.
- [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L4) identifies itself as `Wave 5, Iteration 57` and `Phase 0A: Bolt.jl integration layer`.
- [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L22) says `In actual deployment, uncomment: using Bolt`.

Repo-level check:
- `DFDBolt.jl` exports `run_LCDM_validation` and `run_DFD_spectrum`, but I could not find any definitions for those functions anywhere in `Cross_Reference_Updates`.

Why this is fatal:
- A document-level Planck confrontation is not enough.
- If the claimed spectrum-generation functions are not actually present on disk, the result is not yet reproducible in this workspace state.

Required correction:
- Do not score i106 as computational closure until the exact run path exists in code and can be executed from the repo.

### F2. The "zero free parameters" label in i106 is not yet safe

Evidence:
- [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67) and [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L93) both describe the confrontation as zero-parameter.
- But [DFDBolt.jl](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L57) sets explicit defaults for `Omega_m0`, `Omega_b0`, `h`, `n_s`, `A_s`, and `tau_reio`, with values that look Planck-like.

Why this is critical:
- If those numbers are genuinely derived elsewhere and merely injected here, that needs to be stated explicitly and traceably.
- If they are benchmark fit-like inputs, then the computation is not zero-parameter in the strong sense claimed.

Required correction:
- Add a one-page provenance table for every cosmological input used in the run:
  - derived from DFD
  - fixed external measurement
  - benchmark borrowed from LCDM

Without that, the zero-parameter claim is not referee-safe.

### F3. i106 lacks visible output artifacts for the quoted numerical results

I found the text files and Julia modules, but I did **not** find:

- saved CMB spectra
- residual plots
- chi-squared tables
- Planck comparison outputs
- run logs
- result CSV/JSON/HDF5 files

Why this matters:
- Even if the code exists, the claimed outputs need archival artifacts.
- Otherwise the work remains difficult to audit later.

Required correction:
- Every future cosmology promotion should require:
  - one run script
  - one log
  - one output file
  - one figure set
  - one short README describing exactly how the numbers were produced

## Critical Issues

### C1. i106 itself admits the lensing module is still approximate

Evidence:
- [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L102) says the lensing module is analytic (Limber), not full Boltzmann.

Reviewer implication:
- This is compatible with a `B+`-style exploratory promotion.
- It is **not** compatible with language suggesting the main cosmology bottleneck is basically solved.

### C2. i107 Bullet Cluster claims are not backed by visible simulation artifacts in the repo

Evidence:
- [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L134) says a particle-mesh code was implemented on a `256^3` grid.
- [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L208) then quotes specific convergence and offset results.

Repo-level check:
- I did not find a Bullet Cluster simulation code file, config, snapshot output, or result artifact in `Cross_Reference_Updates`; only the TeX writeup was present.

Why this is critical:
- This makes the result hard to distinguish from an analytic estimate, a hand calculation, or an actual run.
- The sector should not be promoted from this alone.

Required correction:
- Store the simulation driver, parameters, and at least one numerical output artifact.

### C3. Only `W6i106` and `W6i107` are present on disk right now

I did not find `W6i108-W6i110` artifacts in the repo snapshot I reviewed.

Why this matters:
- Review should track what exists on disk, not what status updates promise.
- Any grade changes depending on i108-i110 should be held pending artifacts.

## Reviewer Booking Recommendation

### Safe to count as progress

- i106: clearer cosmology implementation direction
- i106: likely real codebase movement, since Julia modules exist
- i107: plausible non-equilibrium Bullet Cluster strategy worth pursuing

### Not safe to count yet as full closure

- full Planck confrontation
- zero-parameter cosmology victory
- production Boltzmann maturity
- Bullet Cluster near-resolution

## Minimum Evidence Checklist Before Promotion

For cosmology:

1. executable run script
2. explicit dependency installation path
3. output spectra files
4. Planck comparison notebook or script
5. input provenance table

For Bullet Cluster:

1. simulation code
2. initial-condition file
3. output snapshots
4. one figure reproducing the quoted offsets/convergences
5. explanation of how observation/systematic uncertainty was folded in

## Bottom Line

These files show that the programme is finally moving in the right direction on the two hardest bottlenecks.

But as of this repo snapshot, the strongest honest statement is:

`the cosmology and Bullet Cluster sectors now have plausible implementation narratives, not yet closed reproducible results.`

That is still progress. It just should not be overbooked.
