# Wave 6 Meta-Drift Review (chatgpt)

Date: 2026-03-24
Role: external reviewer
Focus: publication status, counts, trackers, summary-vs-technical drift

## Executive Judgment

The biggest immediate credibility risk is no longer a single equation or simulation claim. It is **status drift across the corpus**:

- publication status contradicts itself
- iteration counts contradict themselves
- findings totals and scorecards contradict themselves
- summary files promote sectors faster than the technical files support

This is fixable, but it needs to be treated as a first-order problem.

## 1. Publication Status Is Contradictory

### Story A: no papers submitted or accepted

- [MASTER_FINDINGS_LIST.tex#L2145](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L2145)
- [MASTER_FINDINGS_LIST.tex#L2146](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L2146)

This root master ledger says:

- no papers submitted
- no papers accepted
- no citations exist

### Story B: active and successful publication pipeline

- [MASTER_FINDINGS_LIST.tex#L1785](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1785)
- [MASTER_FINDINGS_LIST.tex#L1786](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1786)
- [MASTER_FINDINGS_LIST.tex#L1787](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1787)
- [MASTER_FINDINGS_LIST.tex#L1788](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1788)
- [MASTER_FINDINGS_LIST.tex#L1798](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1798)

This parallel ledger says:

- `$c_T$` paper published
- BD letter accepted
- several papers under review
- arXiv/Zenodo/public-facing milestones already active

### Story C: mature external record with citations

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L58](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L58)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L62](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L62)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L244](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L244)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L281](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L281)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L330](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L330)

This file says:

- multiple papers published
- multiple papers accepted
- citations exist at nontrivial scale

### Why this matters

Any outside reader who notices these three incompatible stories will stop trusting the rest of the bookkeeping, even where the technical work is solid.

## 2. Scoreboard / Counts Drift Is Severe

### Iteration counts

- [ITERATION_TRACKER.md#L3](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L3)
- [ITERATION_TRACKER.md#L241](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L241)
- [ITERATION_TRACKER.md#L256](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L256)
- [W6i105_Assessment.tex#L60](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L60)
- [W6i106_Compiled.tex#L138](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L138)

The tracker starts as if the target is still 20 iterations, then records far deeper waves, while Wave 6 documents assume 105/106 completed iterations.

### Findings totals

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L46](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L46)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L56](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L56)
- [W6i105_Assessment.tex#L62](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L62)
- [W6i106_Compiled.tex#L140](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L140)

Competing totals:

- 410 findings final at i1-i100
- 432 by i105
- 447 by i106

That can be valid if carefully rolled forward, but the files are not currently stitched together in a way that makes that chain safe.

### Scorecards

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L53](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L53)
- [W6i105_Assessment.tex#L63](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L63)
- [W6i106_Compiled.tex#L141](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L141)

Competing scorecards:

- `97/3/0`
- `18 GREEN / 4 YELLOW / 0 RED` for the sprint-local layer
- `127/10/0`

These are not clearly separated as local-vs-global scoreboards, so they read as contradictions.

### Honest negatives

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L67)
- [W6i105_Assessment.tex#L283](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L283)
- [W6i106_Compiled.tex#L143](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L143)

Competing totals:

- 14
- 7
- 8

Again: maybe explainable, but not currently explained.

## 3. Wave 6 Summary Files Are Outrunning Technical Files

### Cosmology

- Summary upgrade:
  - [W6i106_Compiled.tex#L26](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L26)
  - [W6i106_Compiled.tex#L89](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L89)
- Technical caution:
  - [W6i106_Boltzmann_Core.tex#L402](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L402)
  - [W6i106_Boltzmann_Core.tex#L422](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L422)
  - [DFDBolt.jl#L4](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L4)
  - [DFDBolt.jl#L11](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L11)
  - [DFDBolt.jl#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L30)
  - [DFDBolt.jl#L209](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209)

The technical core still says important phases are pending and even says cosmology remains grade B, while the compiled summary promotes B+.

### Masses / unification

- Summary promotion:
  - [W6i105_Assessment.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L115)
  - [W6i105_Assessment.tex#L131](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L131)
- Canonical artifacts still behind:
  - [mass_canonical.py#L6](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py#L6)
  - [mass_canonical.py#L17](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/mass_canonical.py#L17)
  - [Mass_Model_Reconciliation.tex#L198](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Mass_Model_Reconciliation.tex#L198)
  - [Full_QCD_Running.tex#L26](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Full_QCD_Running.tex#L26)

The summary says fermion masses are now A and unification A-, but canonical scripts still encode the older mass dictionary and a PDG-fed `Λ_QCD` path.

## 4. “Final” and “Definitive” Markers Are Unreliable

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L2](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L2)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L29](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L29)
- [W6i105_Assessment.tex#L33](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L33)
- [W6i106_Compiled.tex#L26](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L26)

Examples:

- `FINAL VERSION`
- `definitive state`
- `Wave 6 Final`

These are being used on documents that are then superseded by later same-day or same-wave files. So these markers are not trustworthy as corpus-level status labels.

## 5. Fix Order

1. **Choose one canonical truth source for programme status**
   - counts
   - scorecard
   - honest negatives
   - external/publication status

2. **Make summary files explicitly subordinate to technical files**
   - no sector promotion unless the technical file and code/artifact base both support it

3. **Stop using “published/accepted/under review/no papers” inconsistently**
   - this is a pure trust issue and should be easy to fix compared to theory work

4. **Stop using “final/definitive” on files that are known to be superseded**

5. **Separate local sprint metrics from global programme metrics**
   - e.g. make it impossible to confuse `18/4/0 this sprint` with `127/10/0 total`

## Reviewer Bottom Line

This is now a documentation-governance issue as much as a physics issue.

If the programme wants outside readers to trust the strongest Wave 6 claims, it needs:

- one authoritative status ledger
- one authoritative external-status ledger
- one authoritative scoreboard ledger
- and summary documents that no longer outrun the technical substrate

