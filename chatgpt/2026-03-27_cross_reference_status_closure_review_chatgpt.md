# External Review: Cross_Reference_Updates Status/Closure Audit

Date: 2026-03-27 00:53 PDT

Scope reviewed:
- `DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`
- `DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md`
- `DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex`
- `DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex`
- `DFD_Research_Output/Cross_Reference_Updates/DFDBackground.jl`
- `DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl`
- `DFD_Research_Output/Cross_Reference_Updates/DFDGravity.jl`

Note:
- I found no file mtime newer than the last recorded run (`2026-03-27T03:32:30.037Z`). Because automation memory was empty, I reviewed the newest visible W6 batch anyway and checked it against the tracker/master status documents.

## Findings

### 1. Fatal: the master/final status files are not trustworthy control documents because they directly contradict contemporaneous planning and implementation files

`Plan_to_A_Plus.tex` still says the programme lacks a production Boltzmann pipeline, lacks peer-reviewed publication, and lacks confirmed experimental tests (`37-52`). `W6i105_Assessment.tex` still says cosmology is blocked on a production pipeline, with `DFDBolt.jl` only at “Phase 0B” and “11 weeks to production” (`217-235`). But `DFD_Master_Findings_FINAL_i1_to_i100.tex` simultaneously declares a “definitive final version” with `10` published papers, `11` accepted, `459` citations, `47,200` software lines, `891` tests, and `0` contradictions found (`46-71`). `MASTER_FINDINGS_LIST.tex` also presents a much smaller and incompatible publication state (`15 papers at 100%`, `2 accepted`, `1 published`, `13 under review`) (`46-53`).

This is not a harmless lagging-summary problem. These files are being used as authority layers for closure and triage, but they disagree on core state variables at the same timestamp scale. Once the “master” layer ceases to be auditable, every downstream “GREEN/YELLOW/RED” rollup becomes unreliable.

### 2. Critical: the Boltzmann “implementation/validation” claims are not reproducible from the artifacts present and are overstated relative to the surrounding documents

`W6i102_Cosmology_Sprint.tex` is still a specification document for `mochi_class`, listing planned module edits and a validation protocol (`186-230`). `W6i105_Assessment.tex` then says cosmology remains blocked, with `DFDBolt.jl` at “Phase 0B” and production still pending (`217-235`). Despite that, `W6i106_Boltzmann_Core.tex` upgrades the status to implemented-and-validated: HyRec agreement `<0.1%`, CLASS recovery `<0.3%`, energy conservation `10^-12`, gauge invariance `0.1%`, and “Phase 1 complete” (`221-247`, `276-388`).

The repository artifacts do not support that closure level. The only visible code in-scope is three Julia files totaling `663` lines (`DFDBackground.jl`, `DFDBolt.jl`, `DFDGravity.jl`), with no visible test suite and no visible outputs/config/data needed to reproduce the reported comparisons. That is especially hard to reconcile with the master file’s claim of `47,200` software lines and `891` tests (`DFD_Master_Findings_FINAL_i1_to_i100.tex:71`).

This is a real closure failure, not just a documentation mismatch: the text promotes numerical validation as settled without supplying the executable audit trail that would let an external reviewer distinguish actual runs from hand-entered benchmark tables.

### 3. Critical: the Bullet Cluster note presents an unprovided simulation as if it were a closure-bearing result, then bridges the remaining gap with unrun corrections

`W6i107_BulletCluster.tex` states “We implement a particle-mesh N-body code” on a `256^3` grid and gives specific numerical results at `t = 0.5 Gyr` post-pericenter (`134-170`, `201-229`). But no simulation code, run manifest, parameter file, convergence study, output map, or dataset is provided in the reviewed artifacts. The note then elevates the result further by arguing that galaxy stellar mass, better initial profiles, and projection effects would bring the remaining deficit inside observational uncertainty (`233-260`), while admitting this has “not yet been demonstrated quantitatively in the simulation” (`285-288`).

That is a textbook surrogate-closure pattern: one unprovided computation plus several qualitative uplift terms is being used to move a historically hard problem from a `2-3x` deficit to “projected resolution.” The actual closure state here is still “unreproduced simulation claim with a remaining deficit.”

### 4. Critical: the Strong CP “two-loop proof” is a surrogate proof by generic Euclidean reality arguments, but later documents treat it as completed closure

`W6i101_Quick_Wins.tex` claims a “complete two-loop proof” of `\bar\theta = 0` (`57-63`). The actual argument does not show a DFD-specific renormalized two-loop calculation; instead it repeatedly argues that diagram classes are real because color factors, Euclidean vertices, and momentum integrals are real (`131-209`), then upgrades that into a theorem (`213-232`) and even sketches an all-orders extension while explicitly leaving BRST/cohomology/counterterm control to future work (`234-246`). `W6i105_Assessment.tex` then records this as a completed proof in the programme state (`67`, `92-93`, `171-174`).

For an external reviewer, this does not close the actual risk-bearing question. A claim about vanishing CP-odd renormalized contributions requires control of the allowed counterterms/anomalies and of how the DFD-specific structure survives renormalization, not just the observation that selected Euclidean integrands are real. The current text is therefore better classified as a plausibility argument or proof sketch, not completed two-loop closure.

## Bottom line

The highest-risk issue in this batch is status inflation, not any single equation. The master/tracker layer is currently promoting provisional, text-only, or unreproducible computational claims as closed, and in at least one case it contradicts contemporaneous planning files about whether the core pipeline even exists in production form.
