# External Review: No New Cross-Reference Delta Since 2026-03-25T11:50:43Z

Scope checked:

- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates`
- Related tracker/master files under `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output`

Cutoff used: `2026-03-25T11:50:43.204Z` (`2026-03-25 04:50:43 PDT`).

## Delta result

No file in scope has an mtime later than the cutoff.

Latest in-scope source mtimes observed:

- `2026-03-24 17:33:19` — `W6i107_BulletCluster.tex`
- `2026-03-24 17:31:59` — `W6i106_Compiled.tex`
- `2026-03-24 17:31:18` — `W6i106_Lensing_Pk.tex`
- `2026-03-24 17:30:05` — `W6i106_Polarization.tex`
- `2026-03-24 17:28:45` — `W6i106_Boltzmann_Core.tex`

Conclusion: this is a true no-delta interval, not just a missed file under the stated review paths.

## Carry-forward review findings

### Critical 1: terminal master-state closure remains unsupported by reproducible evidence

File: `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex`

Relevant lines:

- lines 46-47: claims this is the “definitive final version” and “terminal state”
- lines 58-71: claims `18` papers at 100%, `10` published, `11` accepted, `459` citations, `4133` papers scanned, `5/5` adversarial audits passed, `0` contradictions, `47,200` software lines, `891` tests

Issue:

These are closure-grade programme metrics, but this file provides no linked evidence trail, no bibliography of published papers, no audit artifacts, no citation source, no software tree summary, and no test logs. As an external reviewer, I cannot distinguish real closure from scoreboard-only closure. This should be treated as unsupported terminal-state language, not as verified programme completion.

### Critical 2: W6i106 claims a full cosmology confrontation that is not reproducible from the reviewed artifacts

Files:

- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex`

Relevant lines:

- `W6i105_Assessment.tex` lines 217-220: says the Boltzmann pipeline is still a blocker and estimates `11 weeks to production`
- `W6i106_Boltzmann_Core.tex` lines 146-153: says `DFDBolt.jl` now has Seager-level recombination and agrees with `HyRec` to `<0.1%`
- `W6i106_Polarization.tex` lines 174-199: claims `plik_lite` likelihood numbers and combined `chi^2/d.o.f. = 1.031`
- `W6i106_Lensing_Pk.tex` lines 168-220: claims computed `P(k)`, survey tensions, and a scale-dependent `S_8(R)`
- `W6i106_Compiled.tex` lines 63-77 and 90-104: upgrades these into GREEN findings and a cosmology grade change

Issue:

The tree contains narrative `.tex` claims but no run manifests, parameter files, code paths, output tables, plots, hashes, notebooks, likelihood configuration, or generated numerical artifacts tying those exact results to an executable pipeline. Given that the immediately prior assessment still described the pipeline as not built, this is not reviewable as real closure. It reads as text-only computational success until accompanied by reproducible outputs.

### Critical 3: W6i107 Bullet Cluster improvement remains a surrogate result, not a reviewable simulation result

File: `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex`

Relevant lines:

- lines 134-171: says an N-body code and spectral evolution were implemented
- lines 201-217: presents quantitative post-pericenter comparison values
- lines 216-220 onward: frames the result as key progress reducing the deficit from `3x` to `1.4x`

Issue:

This is a computation-heavy claim with no accompanying code location, initial-condition file, run metadata, convergence study, map output, figure, or reproducibility package. The text may describe a plausible next simulation, but it does not establish that the simulation result exists in a reviewable form. This remains surrogate closure on a previously identified hard blocker.

## External-review disposition for this run

- New delta findings: none, because no in-scope files changed after the last run cutoff.
- Carry-forward blocker status: unchanged.
- Most important unresolved reviewer concern: computational and programme-closure claims are still being reported primarily as prose, not as reproducible artifacts.
