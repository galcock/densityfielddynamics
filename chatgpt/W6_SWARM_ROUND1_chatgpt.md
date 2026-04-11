# ChatGPT Swarm Review: Wave 6 Round 1

Date: 2026-03-24

Scope: first checkpoint from the multi-agent reviewer swarm. This note only records findings already surfaced from the first active wave plus direct repo checks.

## Highest-Risk Findings So Far

### 1. Strong CP "2-loop proof" is not yet a real renormalized closure

The current `W6i101` note still looks like a plausibility sketch, not a full EFT-level proof that the renormalized `F\tilde F` coefficient and renormalized `arg det(M_u M_d)` both vanish.

Key refs:
- [W6i101_Quick_Wins.tex#L113](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L113)
- [W6i101_Quick_Wins.tex#L182](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L182)
- [W6i101_Quick_Wins.tex#L242](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242)
- [W6i101_Quick_Wins.tex#L266](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L266)
- [W6i101_Quick_Wins.tex#L634](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L634)

Reviewer bottom line:
- do not book Strong CP to A+ on this note alone
- label it as a `2-loop closure sketch` until the renormalized operator-level proof exists

### 2. The "global existence" upgrade is still on a surrogate PDE, not the full DFD system

`W6i103` proves something interesting, but what it proves is a semilinear wave equation with an externally prescribed source under spherical symmetry. That is not yet the full DFD coupled dynamics.

Key refs:
- [W6i103_Hard_Math.tex#L59](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L59)
- [W6i103_Hard_Math.tex#L109](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L109)
- [W6i103_Hard_Math.tex#L121](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L121)
- [W6i103_Hard_Math.tex#L167](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L167)

Reviewer bottom line:
- this is partial progress, not yet a sector-closing theorem
- Math Foundations and Gravitational should not be promoted on this result without an explicit bridge to the real DFD equations

### 3. The Born-rule gap is still genuinely open

The same `W6i103` file still contains an explicit circularity/open-gap problem in the Born-rule section. That means the quantum sector cannot honestly be represented as nearly closed.

Key refs:
- [W6i103_Hard_Math.tex#L477](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L477)
- [W6i103_Hard_Math.tex#L485](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L485)
- [W6i103_Hard_Math.tex#L509](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i103_Hard_Math.tex#L509)

Reviewer bottom line:
- keep treating Born rule as a hard foundational blocker
- do not let newer sprint prose quietly harden it into a solved sector

### 4. `W6i105` has grading arithmetic drift and milestone inflation

The Wave 6 assessment file appears to overstate its own promotions.

Key refs:
- [W6i105_Assessment.tex#L52](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L52)
- [W6i105_Assessment.tex#L62](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L62)
- [W6i105_Assessment.tex#L99](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L99)
- [W6i105_Assessment.tex#L138](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L138)
- [W6i105_Assessment.tex#L170](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L170)
- [W6i105_Assessment.tex#L374](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L374)

Reviewer bottom line:
- promotion counts need recomputing
- `submission` cannot stand in for `peer-reviewed publication`
- unification should not be hardened to `A-` while `\bar\rho` remains a 3x miss

### 5. i106 cosmology still looks ahead of the on-disk implementation

`W6i106_Compiled.tex` reports full Planck-confrontation style numbers, but the on-disk Julia wrapper still looks like an integration layer and does not visibly define the exported spectrum-running functions.

Key refs:
- [W6i106_Compiled.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67)
- [W6i106_Compiled.tex#L71](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L71)
- [W6i106_Compiled.tex#L93](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L93)
- [DFDBolt.jl#L4](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L4)
- [DFDBolt.jl#L22](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L22)
- [DFDBolt.jl#L31](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L31)

Reviewer bottom line:
- do not book i106 as true computational closure
- require executable run scripts, outputs, and provenance for every quoted cosmology number

### 6. The "zero free parameters" cosmology language is not yet safe

The current Julia wrapper uses explicit Planck-like defaults for `Omega_m0`, `Omega_b0`, `h`, `n_s`, `A_s`, and `tau_reio`. Unless each one is traced back to a DFD derivation or a fixed external measurement policy, the strong `0 params` wording is too aggressive.

Key refs:
- [DFDBolt.jl#L57](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L57)
- [W6i106_Compiled.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L115)

Reviewer bottom line:
- add a cosmological input provenance table before using `zero free parameters` in this sector

## Immediate Reviewer Recommendation

Freeze sector promotions at the following conservative levels until the next closure artifacts exist:

- Strong CP: keep at `A`
- Gravitational / Math Foundations: keep at pre-upgrade levels unless the surrogate-to-DFD bridge is made explicit
- Quantum Sector: keep the Born-rule gap front and center
- Cosmology / Computational Maturity: do not promote on prose alone; require executable artifacts

## Status

This is a live checkpoint only. More swarm results are still incoming.
