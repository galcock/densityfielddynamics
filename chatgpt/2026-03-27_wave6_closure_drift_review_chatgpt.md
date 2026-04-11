# ChatGPT Review: Wave 6 Closure Drift and Source-of-Truth Failures

Date: 2026-03-27

Scope: no files under [`/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates) were newer than the last run timestamp (`2026-03-27T16:50:45.232Z`), so this pass reviewed the latest uncovered Wave 6 closure/state files instead of a fresh delta. This note focuses only on net-new fatal and critical issues not already covered in the existing `chatgpt` reviews.

## Executive Verdict

The strongest new problem in this batch is not one isolated derivation failure. It is closure inflation riding on an unstable state ledger.

Three patterns recur:

- arithmetic or derivational gaps are still being booked as theorem-grade closure;
- text-only computational claims are being promoted as if they came from executable survey-grade pipelines;
- roadmap and assessment files are not aligned with the programme's own later tracker/master state, so they cannot function as reliable source-of-truth documents.

## Fatal

### F1. `W6i103_Hard_Math.tex` claims an `n_f` theorem that does not reproduce its own advertised exponents

Evidence:

- The theorem states `n_f = (k_f + k_H)/2`: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L263).
- The worked assignments then do not follow that formula. For example, the file writes `n_mu = (5 + 4)/2 = 7/2 - 1 = 7/2` and `n_t = (-1 + 4)/2 + (1 - 1) = 1/2 + 0 = 1/2`: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L333), [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L336).
- The same proof then says these values “match the empirical values exactly” and the summary box says all 9 exponents are derived with zero free parameters: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L346), [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L359).

Why this is fatal:

- This is not a small typo. The theorem-grade closure claim fails on the file's own arithmetic.
- Once ad hoc offsets are inserted inside the worked examples, the result is no longer an ab initio derivation.
- That breaks the claimed upgrade of the fermion-mass sector at the exact point where the programme is trying to book “all 9 exponents derived.”

Required correction:

- Withdraw theorem-grade language for the `n_f` result until the closed-form rule actually reproduces the listed exponents without inserted corrections.

### F2. `W6i104_Unification_Push.tex` replaces its failed CKM derivation mid-file with an unrelated alpha ansatz and still books near-exact closure

Evidence:

- The file first derives `sin(theta_C) = 0.1573` from the overlap-integral route and explicitly notes a `~30%` discrepancy: [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L123).
- It then pivots to a theorem using `lambda = 31 alpha = 0.2262` and uses that replacement track to claim strong CKM/Jarlskog agreement: [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L140), [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L168).
- The file never shows how the failed geometric overlap result is transformed into `31 alpha`, but still rolls the result into its unification scorecard: [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L452), [W6i104_Unification_Push.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i104_Unification_Push.tex#L551).

Why this is fatal:

- A derivation that misses by 30% cannot be silently replaced by a numerology-like ansatz and still count as the same closed result.
- This is not real closure; it is a mid-file branch swap presented as one derivation.
- That contaminates the broader “all 19 parameters / zero free parameters” unification framing built on top of it.

## Critical

### C1. `W6i103_Hard_Math.tex` violates its own “not fit to data” standard, so the fermion closure is surrogate proof rather than derivation

Evidence:

- The file says the exponents “must be derived ... not fit to data”: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L216).
- But the bundle assignment is introduced as the “unique solution consistent with all constraints and the observed mass hierarchy”: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L330).
- The same section then markets the result as “Zero free parameters”: [W6i103_Hard_Math.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L359).

Why this is critical:

- Selecting the assignment by consistency with the observed hierarchy is a calibration move, not a first-principles closure.
- That means the file is using text-level uniqueness rhetoric as a surrogate for an actual derivation from the action.

### C2. `W6i106_Lensing_Pk.tex` books survey-facing cosmology results as if they came from a full pipeline, but the evidence presented is still analytic/text-only

Evidence:

- `W6i106_Compiled.tex` books `F444` to `F447` as completed findings and presents the iteration as if the Boltzmann sector has delivered survey-facing outputs: [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L74), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L75), [W6i106_Compiled.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L95).
- The `P(k)` table contains no actual survey values, covariance, window-function treatment, likelihood, or residuals. “BOSS DR12” appears only as qualitative status text such as “Within 2%” and “Consistent”: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L168).
- The same file then upgrades the neutrino cancellation story with a plain stated overlap factor rather than a shown reproducible computation: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L241).

Why this is critical:

- This is not yet a reproducible confrontation with survey data.
- The programme is booking executable-looking closure from qualitative comparison language and hand-inserted factors.
- That is exactly the “text-only claim presented as computational result” failure mode this review was asked to prioritize.

### C3. The only stated `S_8` escape hatch in `W6i106_Lensing_Pk.tex` is internally mis-signed

Evidence:

- The file defines `S_8(R) = 0.840[1 - 0.015 ln(R/8 h^{-1} Mpc)]`: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L216).
- It then says smaller-scale lensing should see lower `S_8` and quotes an effective range `0.820--0.840`: [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L220), [W6i106_Lensing_Pk.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L224).

Why this is critical:

- For `R < 8`, the displayed formula makes the bracket larger than 1, so it raises `S_8` at smaller scales rather than lowering it.
- That means the file's own algebra does not support its claimed direction of relief.
- The proposed resolution path for the `S_8` tension is therefore not just incomplete; it is internally inconsistent as written.

### C4. `W6i106_Polarization.tex` silently re-promotes `beta = 0` to GREEN closure after the master corpus had already downgraded it

Evidence:

- `W6i106_Polarization.tex` says the Chern-Simons coupling “vanishes identically” and books `F442` as GREEN: [W6i106_Polarization.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L220), [W6i106_Polarization.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L278).
- But the master corpus had already downgraded `P24 cosmic birefringence beta=0` from “structural” to “promising but not theorem-grade,” explicitly noting that no independent derivation was in hand: [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L14), [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L19).

Why this is critical:

- A previously downgraded watch item is being re-promoted to near-theorem status without an explicit supersession chain or visible new closure artifact.
- That is a sink-loop pattern: branch rhetoric is outrunning canonical state control.

### C5. `Plan_to_A_Plus.tex` is not source-of-truth aligned with the programme's own later tracker/master state

Evidence:

- The roadmap says DFD has “no free parameters” and treats Parameter Economy as already-satisfied A+ status: [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L37), [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L89).
- It also says the main cosmology blocker is that there is still no production-grade Boltzmann pipeline: [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L39), [Plan_to_A_Plus.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/Plan_to_A_Plus.tex#L50).
- But nearby programme state elsewhere had already moved through materially different canonical claims about free-parameter count and Boltzmann/pipeline status, including tracker/master material that no longer matches this roadmap framing: [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L160), [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L335), [MASTER_FINDINGS_CORPUS.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/MASTER_FINDINGS_CORPUS.md#L838).

Why this is critical:

- The roadmap cannot guide closure if it cannot say which programme state is canonical.
- This breaks planning lineage in the same way the tracker previously broke closure lineage: the next step could be “build the pipeline,” “reconcile the already-claimed pipeline,” or “downgrade prior claims,” and the document does not distinguish those states.

### C6. `W6i105_Assessment.tex` leaves a misleading “no contradictions / no regressions” state in circulation after later tracker updates reversed one of its flagship cosmology claims

Evidence:

- The assessment says no sector regressed, gives a bounded honest-negative count, and states `Total contradictions: 0`: [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L138), [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L283), [W6i105_Assessment.tex](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L285).
- Later tracker state then demotes the same lensing result from GREEN to YELLOW and rewrites the `A_L` range into an honest negative: [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L977), [ITERATION_TRACKER.md](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L982).

Why this is critical:

- Without an explicit supersession note, `W6i105` reads like a canonical closure ledger even after one of its headline claims has been materially reversed.
- That is a sink-loop problem: interim branch assessments continue to look bankable after the underlying state has changed.

## Bottom Line

This Wave 6 slice should not be read as stable progress toward closure.

The key net-new failure mode is state-control collapse:

- a fermion “theorem” that fails its own formula,
- a CKM “derivation” that swaps in a different ansatz after the geometric route fails,
- survey-facing cosmology results that are still text-only,
- a downgraded birefringence claim being re-promoted without a visible closure artifact,
- an assessment file that still reads contradiction-free after later reversals,
- and a roadmap that no longer matches the programme's own state ledger.

Until the programme restores a single canonical source of truth and separates executable results from narrative placeholders, these documents should be treated as provisional branch outputs rather than bankable closure.
