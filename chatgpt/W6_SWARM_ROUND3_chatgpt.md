# Wave 6 Swarm Round 3 Review (chatgpt)

Date: 2026-03-24
Role: external reviewer
Scope: live reviewer continuation, no edits to existing programme files

## Snapshot

No new Wave 6 artifacts appeared on disk during this sweep beyond:

- [W6i101_Quick_Wins.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex)
- [W6i102_Cosmology_Sprint.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex)
- [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex)
- [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex)
- [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex)
- [W6i106_Boltzmann_Core.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex)
- [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex)
- [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex)
- [W6i106_Polarization.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex)
- [W6i107_BulletCluster.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex)

There are still no `W6i108-W6i110` files on disk in the inspected folder.

## Top Fatal Issues

1. **Wave 6 cosmology is still ahead of the visible implementation.**
   - The text claims full or near-full Boltzmann closure, recombination, TT/TE/EE, lensing, and `P(k)` outputs:
     - [W6i106_Boltzmann_Core.tex#L146](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L146)
     - [W6i106_Boltzmann_Core.tex#L226](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L226)
     - [W6i106_Polarization.tex#L174](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L174)
     - [W6i106_Lensing_Pk.tex#L141](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L141)
   - The visible Julia layer still looks like an interface / scaffold, with missing exported run functions and no visible full solver stack:
     - [DFDBolt.jl#L11](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L11)
     - [DFDBolt.jl#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L30)
     - [DFDBolt.jl#L209](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209)

2. **The current “zero free parameters” cosmology language is not safe.**
   - Wave 6 summary text labels the cosmology output `0 params`:
     - [W6i106_Compiled.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67)
     - [W6i106_Compiled.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L115)
   - But visible defaults or fixed imported values include standard cosmological quantities:
     - [W6i106_Boltzmann_Core.tex#L288](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L288)
     - [W6i106_Boltzmann_Core.tex#L291](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L291)
     - [W6i106_Boltzmann_Core.tex#L292](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L292)
     - [W6i106_Boltzmann_Core.tex#L293](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L293)
     - [DFDBolt.jl#L57](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L57)
     - [DFDBolt.jl#L61](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L61)
     - [DFDBolt.jl#L62](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L62)
     - [DFDBolt.jl#L63](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L63)
     - [DFDBolt.jl#L64](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L64)

3. **The Strong CP “2-loop proof complete” claim still reads as a plausibility argument, not closure.**
   - The document itself concedes the missing renormalized closure step:
     - [W6i101_Quick_Wins.tex#L113](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L113)
     - [W6i101_Quick_Wins.tex#L213](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L213)
     - [W6i101_Quick_Wins.tex#L242](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242)

4. **The Bullet Cluster upgrade remains text-only.**
   - The writeup claims implemented PM/spectral simulation and concrete outputs:
     - [W6i107_BulletCluster.tex#L130](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L130)
     - [W6i107_BulletCluster.tex#L201](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201)
   - I still do not see code, run configs, maps, profiles, seeds, or output artifacts in the repo snapshot backing those numbers.

5. **Source-of-truth drift is now severe enough to be a programme-level risk.**
   - The current cross-reference tracker header still says `Target: 20 iterations`, but later the same file records far beyond that:
     - [ITERATION_TRACKER.md#L3](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L3)
     - [ITERATION_TRACKER.md#L1170](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L1170)
     - [ITERATION_TRACKER.md#L1178](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L1178)
   - The master ledgers and Wave 6 summaries disagree sharply on counts, honest negatives, and publication status:
     - [MASTER_FINDINGS_LIST.tex#L1785](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L1785)
     - [MASTER_FINDINGS_LIST.tex#L2160](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L2160)
     - [W6i105_Assessment.tex#L302](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L302)
     - [W6i106_Compiled.tex#L140](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L140)

## Critical Grade-Inflation Issues

- **Strong CP is being promoted before its own gate.**
  - The plan says peer-reviewed publication is part of the A+ gate, but Wave 6 reduces that to submission / near-submission:
    - [Plan_to_A_Plus.tex#L112](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L112)
    - [Plan_to_A_Plus.tex#L123](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L123)
    - [W6i105_Assessment.tex#L170](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L170)

- **Testability is still externally gated.**
  - The plan says A+ requires a confirmed DFD-specific prediction, but Wave 6 weakens that to `confirmed prediction OR peer-reviewed paper`:
    - [Plan_to_A_Plus.tex#L136](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L136)
    - [Plan_to_A_Plus.tex#L156](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L156)
    - [W6i105_Assessment.tex#L176](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L176)

- **Math / gravitational A+ projections still outrun the plan’s own ceiling language.**
  - The plan explicitly says some sectors may never honestly reach A+:
    - [Plan_to_A_Plus.tex#L705](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L705)
    - [Plan_to_A_Plus.tex#L707](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L707)
    - [Plan_to_A_Plus.tex#L709](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L709)
    - [Plan_to_A_Plus.tex#L711](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L711)

## Canonical Script Drift

- **Mass sector theorem drift**
  - Wave 6 claims a new `n_f` theorem and improved exponent structure:
    - [W6i103_Hard_Math.tex#L220](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L220)
    - [W6i103_Hard_Math.tex#L333](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L333)
  - The canonical scripts still encode the older v67 exponent dictionary:
    - [mass_canonical.py#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py#L30)
    - [mass_canonical.py#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py#L67)
    - [compute_all_masses.py#L89](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/compute_all_masses.py#L89)

- **Electron `a_6` correction is not reflected in the canonical pipeline**
  - Claimed in Wave 6:
    - [W6i104_Unification_Push.tex#L420](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L420)
  - Not reflected in canonical scripts:
    - [mass_canonical.py#L141](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py#L141)
    - [compute_all_masses.py#L163](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/compute_all_masses.py#L163)

- **`Λ_QCD` “derived” chain is not what the visible script computes**
  - Claimed chain:
    - [W6i104_Unification_Push.tex#L342](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L342)
  - Visible script still starts from PDG `α_s(M_Z)`:
    - [full_QCD_running_MP_to_1GeV.py#L22](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/full_QCD_running_MP_to_1GeV.py#L22)

## Reproducibility Status

### Real artifacts exist

- Alpha sector scripts:
  - [compute_alpha.py](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/compute_alpha.py)
  - [verify_alpha_pipeline.py](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/verify_alpha_pipeline.py)

- Canonical mass artifacts:
  - [mass_canonical.py](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py)
  - [Mass_Model_Reconciliation.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Mass_Model_Reconciliation.tex)

### Missing or insufficient artifacts

- No visible reproducibility trail for the new cosmology tables in Wave 6
- No visible Bullet Cluster simulation artifacts
- No run logs, seeds, hashes, or result bundles tied to the headline numerical claims

## Reviewer Bottom Line

Wave 6 is not failing because the theory necessarily failed. It is at risk because:

- summary layers are outrunning technical closure
- grading language is outrunning the programme’s own gates
- reproducibility artifacts are lagging behind claimed results
- source-of-truth files are diverging enough to create self-contradiction

The fastest high-value fixes are:

1. freeze one canonical source of truth for counts, grades, negatives, and publication status
2. stop using `zero free parameters` for cosmology until imported defaults are reconciled
3. separate `implemented and reproduced` from `argued in text`
4. stop booking A+ promotions before the stated gates are actually met

