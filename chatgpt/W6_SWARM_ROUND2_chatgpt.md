# ChatGPT Swarm Review: Wave 6 Round 2

Date: 2026-03-24

Scope: second checkpoint from the rotating 6-thread reviewer swarm. This note adds the new findings that came in after the first round, especially on cosmology, Bullet Cluster, source-of-truth drift, and external-gate inflation.

## New Highest-Risk Findings

### 1. Wave 6 cosmology is not repo-consistent with the existing DFD cosmology story

`W6i102` appears to reset the mechanism and headline numbers for cosmology in ways that conflict with the rest of the repo.

Key refs:
- [W6i102_Cosmology_Sprint.tex#L281](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L281)
- [W6i102_Cosmology_Sprint.tex#L305](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L305)
- [W6i102_Cosmology_Sprint.tex#L315](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L315)
- [MASTER_FINDINGS_LIST.tex#L1338](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L1338)

Reviewer bottom line:
- Wave 6 cannot quietly replace the distance-bias / no-modified-Friedmann framing with a new modified-expansion style story without explicit corpus-level reconciliation.

### 2. The on-disk Julia implementation still does not support the i106 computational claims

This is now independently confirmed by both local review and agent review.

Key refs:
- [DFDBolt.jl#L1](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L1)
- [DFDBolt.jl#L11](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L11)
- [DFDBolt.jl#L22](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L22)
- [DFDBolt.jl#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L30)
- [DFDBolt.jl#L209](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209)
- [W6i106_Boltzmann_Core.tex#L146](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L146)
- [W6i106_Boltzmann_Core.tex#L376](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L376)

Reviewer bottom line:
- the repo still looks like an integration scaffold, not a demonstrated full Boltzmann implementation
- the missing function definitions and commented-out Bolt integration are hard blockers against claiming computational closure

### 3. The "zero free parameters" cosmology wording is currently not defensible

The current code uses hard-coded cosmological defaults and tunable-looking inputs, while the documents describe the outputs as zero-parameter.

Key refs:
- [DFDBolt.jl#L57](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L57)
- [DFDBackground.jl#L217](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBackground.jl#L217)
- [DFDGravity.jl#L63](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDGravity.jl#L63)
- [W6i106_Compiled.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67)
- [W6i106_Compiled.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L115)

Reviewer bottom line:
- without an explicit provenance table for every cosmological input, the strong zero-parameter language is unsafe

### 4. The source of truth is now split between Wave 6 and the master archive

Wave 6 is minting new findings IDs, score totals, and sector states that are not carried into the master archive.

Key refs:
- [W6i105_Assessment.tex#L50](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L50)
- [W6i106_Compiled.tex#L55](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L55)
- [W6i106_Compiled.tex#L135](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L135)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L48](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L48)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L108](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L108)

Reviewer bottom line:
- until Wave 6 findings are carried into one canonical corpus, the new grade changes are off-ledger

### 5. Bullet Cluster is still a document-level estimate, not a backed simulation result

The `W6i107` note describes a simulation, but no code path, snapshots, maps, or outputs are present in the repo snapshot.

Key refs:
- [W6i107_BulletCluster.tex#L130](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L130)
- [W6i107_BulletCluster.tex#L164](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L164)
- [W6i107_BulletCluster.tex#L201](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201)
- [W6i107_BulletCluster.tex#L253](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L253)
- [W6i107_BulletCluster.tex#L285](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L285)

Reviewer bottom line:
- this cannot yet support a sector promotion
- it should be framed as a promising semi-analytic / numerical programme direction

### 6. Quantum/Born-rule closure drift is severe across the corpus

The Born rule has been treated in prior docs as open, then GREEN/derived, and then open again.

Key refs:
- [W4i34_QG_Compiled.tex#L271](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i34_QG_Compiled.tex#L271)
- [W4i36_QG_Experiment.tex#L375](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i36_QG_Experiment.tex#L375)
- [W4i42_Compiled.tex#L483](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i42_Compiled.tex#L483)
- [W6i103_Hard_Math.tex#L517](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L517)
- [W6i105_Assessment.tex#L254](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L254)

Reviewer bottom line:
- the quantum sector needs a corpus-wide reset to one honest statement
- Page-Geilker resolution should stay separate from Born-rule derivation

### 7. External-gate sectors are being promoted too early

The A+ plan itself says some sectors require peer review and/or independent confirmation, but Wave 6 projection language weakens those gates.

Key refs:
- [Plan_to_A_Plus.tex#L110](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L110)
- [Plan_to_A_Plus.tex#L132](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L132)
- [W6i105_Assessment.tex#L170](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L170)
- [W6i105_Assessment.tex#L176](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L176)
- [W6i105_Assessment.tex#L374](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L374)

Reviewer bottom line:
- submission is not publication
- publication is not independent confirmation
- external-gate sectors need stricter promotion rules than internal ones

## Immediate Reviewer Recommendations

1. Freeze all Wave 6 sector promotions until the master ledger is updated or explicitly superseded.
2. Treat cosmology and Bullet Cluster as implementation lanes, not scorecard lanes, until reproducible artifacts exist.
3. Remove or soften `zero free parameters` language in cosmology until input provenance is explicit.
4. Reset the quantum sector to one honest corpus-wide statement.
5. Distinguish `internal closure`, `submission-ready`, and `externally validated` as separate states.

## Status

More reviewer outputs are still incoming from the remaining meta-audit agents.
