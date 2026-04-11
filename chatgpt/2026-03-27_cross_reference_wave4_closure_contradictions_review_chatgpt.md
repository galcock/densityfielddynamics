# External Review: Wave 4 Closure Contradictions

Date: 2026-03-27
Scope reviewed:
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i12_DarkSRF_Dictionary.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i15_P11_update.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i15_Experimental_update.tex`
- `/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W4i15_P3_update.tex`

## Finding 1: Fatal
The W4i12 Dark SRF update contains a top-level executive summary that asserts a stronger-than-SQMS Dark SRF bound, while the same file later concludes that the Dark SRF reinterpretation is unverified and that SQMS remains authoritative. This is not a minor wording issue: any tracker/corpus synthesis that reads the executive summary first can import the opposite conclusion from the body.

Evidence:
- `W4i12_DarkSRF_Dictionary.tex` lines 104-121 claim a corrected Dark SRF bound of `5.4e-10` and explicitly call it `2.9x tighter` than SQMS.
- The same file at lines 880-909 recomputes the W4i10 formula to `0.047`, identifies a significant arithmetic/interpretation failure, and states the `4.2e-10` and `7.1e-10` bounds should be treated as `UNVERIFIED`.
- The same file at lines 1229-1243 concludes that the Dark SRF reinterpretation is unverified, SQMS `1.56e-9` remains authoritative, and no haloscope experiment can be usefully reinterpreted for DFD.
- The tracker adopts the invalidation path at lines 320-333, so the source file now contains mutually incompatible closure states.

Why this matters:
- This is a closure-corrupting contradiction at the source-file level.
- It blurs the distinction between a real derivation and a superseded surrogate estimate.
- It creates a high probability of future sink-looping, because later agents can truthfully cite opposite outcomes from the same document.

## Finding 2: Critical
The Wave 4 tracker closes the SQMS `omega^2` vulnerability as resolved, but the same iteration's experimental roadmap still treats that derivation as unverified and uses it as a gate for Phase I. That means the programme has not actually achieved the closure state claimed in the tracker.

Evidence:
- `W4i15_P11_update.tex` lines 104-159 say the `omega^2` flag is resolved, the mechanism is derived end-to-end from the action principle, and the programme-level vulnerability is `CLOSED`.
- `W4i15_Experimental_update.tex` lines 585-586 still lists `SQMS Phase I` as `UNCHANGED` with `omega^2 loss rate still unverified`.
- `W4i15_Experimental_update.tex` lines 637-640 explicitly say to proceed with SQMS Phase I only `if omega^2 loss rate derivation is verified`.

Why this matters:
- The tracker cannot honestly claim resolved closure if execution gating inside the same iteration still depends on later verification.
- This is a classic surrogate-proof pattern: one document treats an internal derivation as sufficient closure while another still treats it as pending validation.
- It undermines the claimed readiness of SQMS Phase I.

## Finding 3: Critical
The 67^K blocker is reported as resolved, but the underlying P3 document still leaves the key mechanism-placement question open in the context that actually matters for the claimed architecture. The result may be a lower-bound argument, but it is not full closure of the architecture-level concern.

Evidence:
- `W4i15_P3_update.tex` lines 275-296 and 814-824 downgrade the 67^K issue from blocker to recommended and call it analytically resolved as a lower bound.
- However, lines 832-845 state that the SPT use-case remains open because it depends on whether the relevant coupling operates through `psi_grav` or negligible `delta psi_EM`, and explicitly says the two-component decomposition must be rigorously verified in the SPT context.

Why this matters:
- This is not yet a reproducible end-to-end closure for the advertised architecture.
- The current result closes only a narrower mathematical lower-bound statement, not the broader implementation claim the tracker language suggests.
- Without separating those two claims, the corpus risks treating a partial analytical bound as closure of the actual device-level mechanism.

## Bottom Line
The dominant issue in the new Wave 4 material is premature closure language. The biggest risk is not missing arithmetic; it is allowing tracker-level “resolved/closed/authoritative” labels to outrun what the underlying files actually support.
