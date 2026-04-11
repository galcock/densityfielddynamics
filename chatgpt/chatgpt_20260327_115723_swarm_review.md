# External Swarm Review: W6i101-W6i107 and tracker/master context

Reviewed scope:
- `W6i101_Quick_Wins.tex`
- `W6i102_Cosmology_Sprint.tex`
- `W6i103_Hard_Math.tex`
- `W6i104_Unification_Push.tex`
- `W6i105_Assessment.tex`
- `W6i106_Boltzmann_Core.tex`
- `W6i106_Polarization.tex`
- `W6i106_Lensing_Pk.tex`
- `W6i106_Compiled.tex`
- `W6i107_BulletCluster.tex`
- `ITERATION_TRACKER.md`
- master findings files for consistency checks

Priority convention:
- Fatal: core closure claim fails or corpus reverses a previously-settled framework assumption.
- Critical: major theorem/computation/pipeline claim is unsupported, internally contradictory, or materially unreproducible.

## Findings

### 1. Fatal: `W6i102_Cosmology_Sprint.tex` reintroduces the modified-Friedmann scalar-dark-energy framework that the tracker says was retracted on March 20, 2026

`W6i102` explicitly states that DFD background cosmology is governed by Friedmann equations with a dynamical `rho_psi, p_psi` sector and a sourced background scalar equation, then builds the perturbation and Boltzmann specification on top of that model. But the tracker says the Wave 4 paradigm correction established that DFD is a distance-bias theory, does **not** modify the Friedmann equation, and that the `D_H/r_d` sign-change framework was retracted as an artifact of the wrong background model. This is not a minor modeling alternative; it is a direct reversal of a documented corpus-level correction without any supersession note.

Refs:
- [`W6i102_Cosmology_Sprint.tex#L54`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L54)
- [`W6i102_Cosmology_Sprint.tex#L58`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L58)
- [`W6i102_Cosmology_Sprint.tex#L74`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L74)
- [`W6i102_Cosmology_Sprint.tex#L186`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L186)
- [`ITERATION_TRACKER.md#L399`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L399)
- [`ITERATION_TRACKER.md#L401`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L401)

### 2. Fatal: `W6i101_Quick_Wins.tex` presents a surrogate proof of two-loop strong-CP closure

The “two-loop proof” argues only that schematic Euclidean loop objects are real and then upgrades that to `delta bar-theta^(2)=0`. It does not isolate the `F \tilde F` coefficient, does not analyze phase renormalization or operator mixing, and does not show that the claimed fermion-loop cancellation actually eliminates the CP-odd structure. The file then escalates a stated conjecture about all-orders closure into a neutron-EDM prediction and says “the physics gap is now closed.” That is closure inflation, not closure.

Refs:
- [`W6i101_Quick_Wins.tex#L113`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L113)
- [`W6i101_Quick_Wins.tex#L186`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L186)
- [`W6i101_Quick_Wins.tex#L213`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L213)
- [`W6i101_Quick_Wins.tex#L234`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L234)
- [`W6i101_Quick_Wins.tex#L251`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L251)
- [`W6i101_Quick_Wins.tex#L268`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L268)

### 3. Critical: `W6i103_Hard_Math.tex` upgrades local control to global existence without closing the continuation criterion

The global-existence proof controls only the basic energy, then asserts an `H^2` estimate in Step 3 without the stronger source regularity needed to justify differentiating the equation and closing that bound. Step 4 then simply declares global continuation from the unproved `H^2` control. This is a classic local-to-global sink loop: the statement being proved is used as if already available.

Refs:
- [`W6i103_Hard_Math.tex#L121`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L121)
- [`W6i103_Hard_Math.tex#L146`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L146)
- [`W6i103_Hard_Math.tex#L167`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L167)
- [`W6i103_Hard_Math.tex#L180`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L180)

### 4. Critical: `W6i103_Hard_Math.tex` contains an internally broken `n_f` theorem

The file claims the fermion-exponent theorem follows from Spin^c data, but the derivation jumps from bundle degrees to `alpha^((k_f+k_H)/2)` scaling via an undefined “localization principle.” The generation proposition is also internally inconsistent on the page: it requires positive `k_f` and then uses `k_1=-1`, and its displayed arithmetic is wrong for the claimed exponents. This is not a rigorous theorem and is not even arithmetically self-consistent.

Refs:
- [`W6i103_Hard_Math.tex#L263`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L263)
- [`W6i103_Hard_Math.tex#L284`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L284)
- [`W6i103_Hard_Math.tex#L289`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L289)
- [`W6i103_Hard_Math.tex#L305`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L305)
- [`W6i103_Hard_Math.tex#L323`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L323)
- [`W6i103_Hard_Math.tex#L333`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L333)

### 5. Critical: `W6i105_Assessment.tex` and `W6i106_Compiled.tex` disagree on whether the cosmology bottleneck is still an unbuilt engineering project or already solved

`W6i105` says cosmology remains at grade `B`, the pipeline is still only at Phase 0B, and a substantial build remains ahead. On the same date, `W6i106_Compiled` markets a “full Boltzmann pipeline” and completed Planck confrontation, upgrades cosmology to `B+`, and summarizes TT/TE/EE/lensing/`P(k)` outputs as completed. The compiled file itself partially walks that back by admitting the lensing module is still analytic and there is still no MCMC posterior. That same-day state mismatch makes the sprint-level synthesis unreliable.

Refs:
- [`W6i105_Assessment.tex#L38`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L38)
- [`W6i105_Assessment.tex#L121`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L121)
- [`W6i105_Assessment.tex#L219`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L219)
- [`W6i106_Compiled.tex#L26`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L26)
- [`W6i106_Compiled.tex#L98`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L98)
- [`W6i106_Compiled.tex#L102`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L102)

### 6. Critical: `W6i106_Boltzmann_Core.tex`, `W6i106_Polarization.tex`, and `W6i106_Lensing_Pk.tex` present exact numerical fits as if computed, but the surrounding corpus still describes the pipeline as partial and analytic

These files give precise `HyRec` agreement, exact TT spot-checks against CLASS, exact TE/EE RMS residuals, exact `chi^2` values, exact `A_lens = 1.004`, and exact `P(k)` ratios. But no executable output, likelihood artifact, run log, or data product is included, and the same-day compiled assessment admits the lensing piece is still analytic rather than full-Boltzmann. This makes the “computed” cosmology outputs unreproducible from the materials provided. It is especially concerning that the `A_lens = 1.004` claim conflicts with the tracker’s earlier statement that `A_L^DFD ~ 1.10-1.20` became natural after the Wave 4 paradigm correction.

Refs:
- [`W6i106_Boltzmann_Core.tex#L146`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L146)
- [`W6i106_Boltzmann_Core.tex#L221`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L221)
- [`W6i106_Polarization.tex#L163`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L163)
- [`W6i106_Polarization.tex#L174`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L174)
- [`W6i106_Lensing_Pk.tex#L93`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L93)
- [`W6i106_Lensing_Pk.tex#L141`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L141)
- [`ITERATION_TRACKER.md#L418`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L418)

### 7. Critical: `W6i107_BulletCluster.tex` builds its claimed non-equilibrium improvement on an invalid scale-separation assumption

The file says the field response time is `~ 1/H_0 ~ 14 Gyr`, then uses a Yukawa initial condition and claims superposition is valid because the inter-cluster distance is “much larger than `m_psi^{-1}`.” That direction is backwards: if `m_psi ~ H_0`, then `m_psi^{-1}` is Hubble-scale, vastly larger than cluster separations. So the manuscript’s own scale estimate undercuts the initial-condition argument used for the simulation. That makes the quoted “deficit reduced from 3x to 1.4x” result non-reproducible on its stated assumptions.

Refs:
- [`W6i107_BulletCluster.tex#L96`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L96)
- [`W6i107_BulletCluster.tex#L99`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L99)
- [`W6i107_BulletCluster.tex#L154`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L154)
- [`W6i107_BulletCluster.tex#L160`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L160)
- [`W6i107_BulletCluster.tex#L216`](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L216)

## Bottom line

The highest-risk pattern in this wave is not a single arithmetic slip; it is repeated promotion of speculative or partially-implemented work into “closed,” “computed,” or “full-pipeline” language. The most serious corpus-level failure is the reappearance of the pre-i14 modified-Friedmann cosmology in `W6i102`, because that reopens a framework the tracker says was already corrected and retracted.
