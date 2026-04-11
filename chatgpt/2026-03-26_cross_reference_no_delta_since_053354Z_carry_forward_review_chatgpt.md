# External Review: no new delta since 2026-03-27T05:33:54.497Z

Reviewed surfaces:

- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex`

Result: no files under the stated review surface have filesystem mtimes later than the last-run cutoff. This is therefore a carry-forward audit of unresolved fatal/critical closure problems still represented in the current tracker/master surfaces.

## Fatal / critical findings

### 1. W6i106 is still being scorecarded as effectively closed even though the file itself admits the core cosmology confrontation is incomplete

Severity: Fatal closure inflation

Evidence:

- `W6i106_Compiled.tex` closes TE/EE/lensing/P(k) outputs and upgrades cosmology to `B -> B+`, including `F439` (`C_l^{TE} computed: 0.9% RMS vs. Planck`), `F440` (`C_l^{EE} computed: 0.7% RMS vs. Planck`), `F441` (`Combined TT+TE+EE: chi^2/d.o.f. = 1.031, zero free parameters`), and `CMB lensing and matter power spectrum computed` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:69-71`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:90-95`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:148`).
- But `W6i106_Boltzmann_Core.tex` still says `The polarization spectrum (C_l^{EE}, not yet computed)`, lists `Polarization (E-mode) Pending`, `CMB lensing Pending`, `$P(k)$ output Pending`, and keeps the statement that cosmology remains grade `B` until those pieces exist (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex:361`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex:413-424`).
- `W6i106_Compiled.tex` marks the central results GREEN, including `F437` (`DFD C_l^{TT}: 1.1% RMS residual vs. Planck, zero free parameters`), `F441` (`Combined TT+TE+EE: chi^2/d.o.f. = 1.031, zero free parameters`), `F444` (`CMB lensing: A_lens^{DFD} = 1.004`), and `F445` (`P(k) ... within 1.5% of LCDM`) while giving the iteration a `12 GREEN + 3 YELLOW + 0 RED` scorecard (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:63-81`).
- The same file immediately concedes that what blocks a higher grade is not a minor polish issue but missing closure primitives: `Lensing module is analytic (Limber), not from full Boltzmann` and `No MCMC posterior -- only point prediction` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:98-104`).
- `MASTER_FINDINGS_CORPUS.md` independently says the neutrino/cosmology confrontation remains `AT RISK pending DFD Boltzmann code` and that a self-consistent bound `requires the DFD Boltzmann code` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:264-268`).
- The same wave also overstates `zero free parameters`: `W6i106_Boltzmann_Core.tex` claims the result is computed with `zero free parameters`, but its own parameter table sources key inputs from upstream model choices such as `From alpha + BBN`, `From psi-field reionization model`, `From psi-field slow-roll at inflation`, and `From psi-field amplitude at horizon exit` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex:278`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex:289-293`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex:325`), then `W6i106_Compiled.tex` amplifies that into `DFD (0 params)` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:71`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex:115`).

Why this is not real closure:

The ledger is treating a point-prediction comparison as a validated cosmology closure while the same evidence base admits there is still no full Boltzmann closure and no posterior-level confrontation. Here the contradiction is even stronger: the compiled file is closing outputs that the core file still marks as pending. That is not merely optimistic framing; it is direct internal closure contradiction plus surrogate-proof promotion.

### 2. The W6i106 lensing/P(k) package still uses unresolved analytic substitutions but is reported upward as if the lensing and growth bottleneck were solved

Severity: Critical sink-loop risk

Evidence:

- `W6i106_Lensing_Pk.tex` derives `A_lens^{DFD} = 1.0036` from an analytic slip ansatz and Limber treatment (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex:93-113`).
- The same file then states the observed Planck anomaly is simply probably a fluctuation and frames future confirmation of `A_lens ~ 1` as `vindication of DFD` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex:117-131`). That is a text-only escape hatch, not closure.
- The matter-power section reports `P(k)` as `within 1-1.5% of LCDM` and `S_8 = 0.840`, while simultaneously admitting `>3 sigma` tension with DES/KiDS and deferring the needed scale-by-scale comparison to future work (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex:168-220`).

Why this is not real closure:

The unresolved issue is not whether one can write down an analytic approximation; it is whether the sign, amplitude, and survey-level confrontation survive a full reproducible pipeline. The current package still substitutes narrative plausibility for a reproduced end-to-end confrontation, so scoring these outputs as GREEN sustains the same cosmology sink-loop.

### 3. W6i107 still converts an admitted Bullet Cluster deficit into a near-resolution claim via stacked hypothetical uplifts

Severity: Critical

Evidence:

- `W6i107_BulletCluster.tex` reports the non-equilibrium run still misses the main convergence peak (`0.22` vs observed `0.30`) and the sub-cluster peak (`0.11` vs `0.15`) (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex:201-229`).
- The rescue step is not simulated closure; it is a hypothetical bundle of future adjustments: galaxy contribution `(30-40%)`, profile choice `(20-30%)`, and projection effects `(10-20%)` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex:233-250`).
- Those speculative uplifts are then promoted to a proposition that DFD `can account for ~80-90%` of the observed lensing and that the remainder is within systematics (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex:253-260`), while findings `F448-F450` are still marked GREEN (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex:271-289`).

Why this is not real closure:

This is a classic surrogate-proof move: an underfitting simulation is being upgraded by non-simulated correction budgets until it nearly closes on paper. Until those corrections are actually implemented and reproduced in the stated pipeline, the Bullet Cluster item remains unresolved, and green-scoring its intermediate claims is misleading.

### 4. The master ledgers remain non-authoritative because they mix open blockers with blanket GREEN/passed language

Severity: Critical ledger integrity issue

Evidence:

- `MASTER_FINDINGS_CORPUS.md` says the Cold Spot tension is `RESOLVED` and that `All five tensions (T1-T5) now fully resolved`, but in the same paragraph says `Definitive resolution requires numerical DFD field equation on cosmological void` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:159-163`).
- The same corpus still states `Bullet Cluster: Under-derived; 72% match is poor and needs rigorous treatment` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:184-191`) and that the neutrino mass result is `AT RISK pending DFD Boltzmann code` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:264-268`).
- Despite that, `DFD_Master_Findings_FINAL_i1_to_i100.tex` continues to present wave-level milestones as GREEN and passed, including `2nd adversarial audit PASSED`, `3rd adversarial audit PASSED`, and broad status buckets that compress unresolved cosmology/N-body work into success states (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex:181-199`).

Why this is not real closure:

Once the master ledger simultaneously says “resolved/passed/GREEN” and “definitive resolution still requires missing computation,” it stops being an authoritative closure surface. That directly undermines downstream tracker, scorecard, and publication-status claims.

### 5. The final i1-i100 master file has internal terminal-state contradictions and unsupported external-verification claims

Severity: Critical ledger integrity issue

Evidence:

- `DFD_Master_Findings_FINAL_i1_to_i100.tex` calls itself the `definitive final version` and says it gives `the terminal state of every programme metric`, including `Papers at 100%: 18` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex:46-58`).
- The same file's publication table still lists item 18, `DFD-CLASS`, at only `85%` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex:338-346`).
- The scorecard block declares `97 GREEN / 3 YELLOW / 0 RED` as a terminal summary (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex:77-100`), but the file later compresses major status claims into broad green buckets and non-reproducible audit summaries rather than a stable finding-by-finding closure chain.
- The same master file also asserts named external validations and audit closure such as `ETH Zurich alpha verification consistent`, `Kyoto c_T = 1 confirmed`, `Princeton verifies 8/12 fermion masses`, `Perimeter N-body consistent`, `5th adversarial audit PASSED`, and `All 101 corrections confirmed minor` without providing an auditable chain to those artifacts inside the file (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex:231-241`).

Why this is not real closure:

This is not just optimistic phrasing. It is an internal contradiction in a file that claims terminal authority, combined with unsupported external-authority language. That makes the master file itself non-authoritative as a closure ledger.

### 6. The iteration tracker still records stale convergence and validation claims that its own later entries reopen

Severity: Critical sink-loop / stale-closure issue

Evidence:

- The closing section claims `Convergence: CONVERGED. Five consecutive iterations (i46-i50) with zero corrections. Scorecard frozen 8 iterations.` while also admitting `Phase 0A: 9th iteration without execution, 0 lines of code` and `R_31 unresolved ... without numerical CMB validation` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:1177-1189`).
- The tracker marks `T4 Cold Spot RESOLVED ... All five tensions (T1-T5) now fully resolved`, but the same tracker first mutates the governing prescription and later reopens the issue as a `3-9x overprediction` honest negative (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:302`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:322`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:343`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:934`).
- The tracker presents `sigma_8 = 0.83 ... remarkably close to observed`, then later says `Perturbation theory fails. mochi_class ONLY path forward` and still ends without numerical CMB validation (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:765`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:846`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:852`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:1182`).
- It also labels `Nuclear clock v3 paper VALIDATED` and `67^K blocker RESOLVED`, but adjacent later entries reopen the amplitude law via a `SCREENING FUNCTION GAP (CRITICAL)` and replace the missing Monte Carlo with an analytic lower-bound argument rather than the demanded computation (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:461`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:471`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:828`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:844`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md:862`).

Why this is not real closure:

The tracker is not just optimistic; it is recording “resolved/validated/converged” states that its own later entries revoke or narrow. That is the definition of a sink-looping status surface and should not be used as authoritative closure.

### 7. `MASTER_FINDINGS_CORPUS.md` still over-closes items outside its own stated evidence window

Severity: Critical corpus-integrity issue

Evidence:

- The corpus header/body uses later-iteration language such as `W'(0) = 0 CONFIRMED (i20, author-verified)` and `G_eff RESOLVED (i20)`, but the footer still describes the document as an i16 corpus incorporating material only through i15 plus a narrow i16 update (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:9-18`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:906`).
- The corpus has a Tier 3 section labeled `Require Full Boltzmann Code` while simultaneously marking `Alpha^57 Step 9 CLOSED`; later it still lists the Boltzmann code and the `Alpha^57 B/A ratio` as open urgent items (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:491-497`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:734`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:738`).
- The corpus says `T4 Cold Spot -- RESOLVED at 0.3 sigma`, yet the same item says `Definitive resolution requires numerical DFD field equation on cosmological void`, is later assigned `Severity: None`, and is counted among `12 questions declared CLOSED` (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:159-163`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:770`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:808`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:891`).
- The same pattern holds for lensing and omega-squared loss: the corpus still says Bullet Cluster is under-derived and the lensing programme is open, while elsewhere promoting lensing resolution claims; it also counts the `omega^2 loss rate` among closed questions while the local-vs-global `Q_psi` issue remains an urgent open uncertainty (`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:184-191`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:445`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:497`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:487-489`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:735`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:739`, `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md:891`).

Why this is not real closure:

The corpus is asserting closed status for items that are either outside its stated source window or explicitly still pending missing computation. That makes it unsuitable as a closure authority without a source-window and evidence-chain cleanup.

## Carry-forward conclusion

No new review delta was found after the last-run cutoff. The highest-priority unresolved carry-forward issues remain:

1. W6i106 cosmology closure is still overstated relative to its own admitted missing full-Boltzmann and posterior machinery.
2. W6i106 lensing/P(k) outputs still rely on analytic and text-level surrogates where a reproducible end-to-end confrontation is still missing.
3. W6i107 Bullet Cluster uplift is still hypothetical rather than reproduced, so the problem is not closed.
4. Master/tracker ledgers still overstate closure by mixing unresolved blockers with GREEN/passed status language.
5. The final i1-i100 master file still contains internal terminal-state contradictions and unsupported named-verifier claims.
6. The iteration tracker still records stale resolved/validated/converged states that later entries reopen.
7. `MASTER_FINDINGS_CORPUS.md` still over-closes items outside its own stated evidence window.
