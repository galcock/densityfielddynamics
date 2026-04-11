# External Review: Wave 6 Cross-Reference Updates

Date: 2026-03-25
Scope reviewed:
- `DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex`
- `DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex`
- `DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex`
- `DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md`
- `DFD_Research_Output/MASTER_FINDINGS_CORPUS.md`
- `DFD_Research_Output/MASTER_VERIFICATION_REPORT.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex`
- `DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`
- supporting code files present in `Cross_Reference_Updates/`

Method:
- External consistency review only.
- No existing files edited.
- Priority on fatal, critical, and sink-loop issues.
- Distinguish real closure from text-only closure and unreproducible computation.

## Executive verdict

The main failure mode in this batch is not ordinary optimism. It is closure inflation: multiple files promote unresolved or only-specified work into "GREEN", "final", "published", "validated", or "computed" states even when the tracker/corpus still records open existential bottlenecks, unresolved tensions, dead patents, or non-executed code paths. The worst instances are the terminal master findings, the Boltzmann/cosmology claims, and the Bullet Cluster update.

## Findings

### 1. Fatal: the "definitive final" master file asserts zero contradictions / zero RED / completed publication record while the tracker and corpus still record unresolved critical tensions, dead patents, and non-executed cosmology bottlenecks

Evidence:
- `DFD_Master_Findings_FINAL_i1_to_i100.tex` declares `Total RED across programme: 0`, `Contradictions found: 0`, `97 GREEN / 3 YELLOW / 0 RED`, and `No RED finding has ever been recorded across 100 iterations` at lines 53-68 and 80-105.
- The same file escalates this into archival claims such as `10 published, 11 accepted, 0 RED` and `Programme COMPLETE` at lines 288-300.
- But `ITERATION_TRACKER.md` explicitly records unresolved existential and critical items:
  - post-i18 status still `NOT CONVERGED`; baryon growth vs `P(k)` unresolved and `Only mochi_class can answer` at lines 663-669.
  - i21 still lists `CMB third peak 30-45% deficit` as `CRITICAL` and `mochi_class nonlinear solver` as the only resolution path at lines 810-815.
  - i22 says the third-peak deficit is only partially reduced and `NO complete DFD-internal resolution` exists at lines 825-830.
  - i23 still logs a `SCREENING FUNCTION GAP (CRITICAL)` and says `mochi_class ONLY path forward` for the CMB third peak at lines 843-847.
  - the same tracker repeatedly keeps dead patents and unresolved portfolio states alive through later iterations, e.g. lines 684, 700, 710, 1157, 1186.
- `MASTER_FINDINGS_CORPUS.md` likewise states `NOT CONVERGED`, `mochi_class is existentially urgent`, and lists dead patents and critical invalidations up front at lines 7-21 and 31-133.

Why this matters:
- A terminal summary cannot simultaneously claim "zero contradictions" and "programme complete" while the authoritative tracker still says the decisive cosmology bottleneck was not executed and several sector-level claims remain disputed or dead.
- This is a trust-breaking synthesis error, not a minor wording issue.

### 2. Fatal: Wave 6 cosmology files present Planck-fit and matter-spectrum numbers as executed computations, but the workspace does not contain the implementation or data required to reproduce those claims

Evidence in prose:
- `W6i106_Boltzmann_Core.tex` claims:
  - `C_l^{TT}` residual better than `1.5%` with RMS `1.1%` and exact `chi^2` values versus Planck at lines 321-344.
  - `Recombination module implemented`, `LCDM recovery to 0.3%`, gauge invariance and energy conservation verified, and direct Planck confrontation completed at lines 375-399.
- `W6i106_Polarization.tex` claims TE/EE spectra computed, combined `chi^2/d.o.f.=1.031`, and only `Delta chi^2 approx 7` worse than six-parameter LCDM at lines 163-199 and 266-276.
- `W6i106_Lensing_Pk.tex` claims `P(k)` computed from Boltzmann output, `S_8=0.840`, lensing amplitude `A_lens^DFD=1.004`, and neutrino suppression already included in the Boltzmann computation at lines 189-246 and 270-286.
- `W6i106_Compiled.tex` then upgrades these to green findings and says the number-one bottleneck was attacked, with direct Planck confrontation completed, at lines 63-75 and 92-102.

Workspace reality:
- The only Julia cosmology files present are `DFDGravity.jl`, `DFDBackground.jl`, and `DFDBolt.jl`, each about 6-7 KB.
- `DFDBolt.jl` advertises `run_LCDM_validation`, `run_DFD_spectrum`, and `compare_to_CLASS` in comments/exports at lines 7-13 and 30-31, but those functions are not actually defined anywhere in the file.
- `DFDBolt.jl` also says `In actual deployment, uncomment: using Bolt` at lines 22-23, showing the Bolt integration is not active in this workspace.
- `DFDBackground.jl` explicitly says necessary functions are duplicated `for standalone testing` at lines 20-21, which is consistent with a toy module, not a full Planck-likelihood pipeline.
- I found no Planck likelihood assets, no `plik` data, no CLASS checkout, and no Bolt package integration files in the workspace. A targeted search for `planck`, `plik`, and `class` produced no supporting cosmology pipeline assets beyond unrelated files.
- The code files also contain no actual test suite or validation harness corresponding to the claimed 78/78 tests or to the later 891-test programme-level claims.

Why this matters:
- The reported `chi^2`, RMS residuals, and spectrum-level confrontations are not reproducible from the on-disk implementation provided.
- This is the clearest example of surrogate closure in the batch: specification-level modules are being narrated as if they were executed data products.

### 3. Critical: the Bullet Cluster update upgrades an unverified simulation narrative into near-closure without any executable simulation artifact in the workspace

Evidence:
- `W6i107_BulletCluster.tex` says `We implement a particle-mesh N-body code` on a `256^3` grid at lines 130-171.
- It then reports numerical results for convergence peaks, mass ratio, and peak offsets at lines 201-228.
- It further claims the model can account for `~80-90%` of the observed convergence and that the remaining deficit is within systematics at lines 253-259.
- Findings F448-F451 present this as a major improvement and nearly within observational uncertainties at lines 271-288.

Workspace reality:
- A file search in `Cross_Reference_Updates` returns no Bullet Cluster code, no N-body code, no simulation output, and no data products beyond `W6i107_BulletCluster.tex` itself.
- The claimed 80-90% closure depends on additional galaxy stellar mass and optimized initial profiles that `have not yet been demonstrated quantitatively in the simulation` in the file's own wording at lines 285-288.

Why this matters:
- The document presents hypothetical uplift terms as if they were part of a demonstrated resolution.
- This is a classic sink-loop pattern: "deficit reduced", then "could be within systematics", then implicitly treated as sector progress without the missing simulation ever being present.

### 4. Critical: the master findings chronology is internally inconsistent about whether cosmology was still blocked by a non-executed solver or already passed numerically

Evidence:
- `MASTER_FINDINGS_LIST.tex` says `SymBoltz.jl Published` but also says Phase 0A was `Not executed in 10 consecutive iterations` at lines 662-669.
- The same file classifies the Boltzmann architecture as grade-A specification only at lines 804-811.
- It still records the CMB third peak as a critical open tension that only `mochi_class/SymBoltz.jl` can resolve at lines 673-680.
- Yet later in the same file it claims `First DFD CMB Power Spectrum -- Planck Consistent` and grades it as a numerical data confrontation at lines 980-987.
- It also claims `First Working DFD Gravity Code` with `78/78 validation tests pass` and `Bolt.jl validated to 0.06% vs CLASS` at lines 1043-1050, and later advertises only `Code v2.0: 2847 lines, 6 tests pass` at lines 1194-1199.

Why this matters:
- The document mixes three incompatible states:
  - solver specification not executed,
  - critical CMB tension unresolved until a future solver run,
  - solver already executed and Planck-consistent.
- That breaks the audit trail for the programme's most important falsifier.

### 5. Critical sink-loop: `Plan_to_A_Plus.tex` repeatedly treats publication/peer review as the main remaining barrier in sectors where the verification report still records unresolved technical issues

Evidence:
- `Plan_to_A_Plus.tex` frames the main global blockers as Boltzmann pipeline, global existence, and peer review/experiment at lines 48-52.
- It says Strong CP's gap is effectively publication, not physics, and assigns `High` likelihood of A+ once published at lines 109-125.
- It says testability's gap is mainly lack of independent testing/publication and that `the physics is there` at lines 131-158.
- It treats the quantum sector as largely a formalization/publication problem, with Page-Geilker resolution existing and Born rule as the main remaining hard gate around lines 291-321 and 542 onward.
- Agent review independently flagged the same issue against `MASTER_VERIFICATION_REPORT.tex`.

Counter-evidence from the verification report:
- `MASTER_VERIFICATION_REPORT.tex` summary still records `3 critical errors`, `5 serious issues`, and `8 moderate concerns` at lines 42-49 and recommends prompt correction before further distribution/publication near lines 1094-1096.
- The report also states the quantum papers rely on a `psi`-modified Schrödinger equation lacking derivation from the action and that the zero-decoherence claim is not proved strongly enough, around lines 477-495 and 712-728.
- It flags anomaly/evidence and lambda-bound usage issues around lines 564-592, 699, 858, and 1010.

Why this matters:
- A planning document can say "publication is the next gate" only after the internal technical gate is actually closed.
- Here the same corpus still contains unresolved technical reasons not to publish as-is, so the plan is overstating closure.

### 6. High: the final master record's publication and software counts are not supported by the reviewed corpus and are in direct tension with earlier tracker states

Evidence:
- `DFD_Master_Findings_FINAL_i1_to_i100.tex` claims:
  - `10 published`, `11 accepted`, `459 citations`, `47,200 lines`, `891 tests` at lines 58-71 and again lines 329-345 and 459-460.
- But `MASTER_FINDINGS_LIST.tex` as of i90 still reports only `2 accepted`, `1 published` at lines 46-53, and its milestone table still shows only `1` publication and `2` acceptances by i90 at lines 1815-1819.
- The only on-disk cosmology code in the reviewed update folder is a handful of small standalone modules and scripts, not evidence for a 47k-line software stack with 891 tests.

Why this matters:
- Some growth between i90 and i100 is possible in principle, but in the reviewed workspace there is no supporting publication ledger, codebase, or test tree commensurate with the magnitude of the claimed jump.
- These should not be elevated to "final" archival facts without traceable evidence.

## Lower-confidence but important notes

- `W6i103_Hard_Math.tex` and `W6i105_Assessment.tex` upgrade spherical global existence and related math status aggressively. I did not independently check the PDE proof; the concern here is maturity signaling, not a line-by-line refutation of the proof.
- `W6i101_Quick_Wins.tex` and `W6i105_Assessment.tex` repeatedly convert "draft complete", "publication-ready", or "proof done" into sector-grade movement before external or broader internal validation is visible elsewhere in the corpus.

## Bottom line

The stop-ship issue is status inflation, not just content disagreement. The reviewed files frequently collapse these distinct states into one:

1. theorem/specification/narrative derivation
2. implemented and executed computation
3. independently verified result
4. published archival fact

For the cosmology pipeline, the Bullet Cluster resolution, and the terminal master findings, those states are being treated as interchangeable. They are not.
