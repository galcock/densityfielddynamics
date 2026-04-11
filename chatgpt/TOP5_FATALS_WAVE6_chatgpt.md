# Top 5 Fatals for Wave 6 (chatgpt)

Date: 2026-03-24

1. **Cosmology closure is overclaimed relative to the visible code.**
   - Claimed in:
     - [W6i106_Boltzmann_Core.tex#L146](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L146)
     - [W6i106_Polarization.tex#L174](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L174)
     - [W6i106_Lensing_Pk.tex#L141](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L141)
   - Not backed by visible implementation state:
     - [DFDBolt.jl#L11](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L11)
     - [DFDBolt.jl#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L30)
     - [DFDBolt.jl#L209](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209)

2. **“Zero free parameters” is being used where imported defaults are still visible.**
   - Problem lines:
     - [W6i106_Compiled.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67)
     - [W6i106_Compiled.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L115)
     - [DFDBolt.jl#L57](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L57)
     - [DFDBolt.jl#L61](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L61)

3. **Strong CP “proof complete” is still not a full renormalized closure.**
   - Problem lines:
     - [W6i101_Quick_Wins.tex#L113](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L113)
     - [W6i101_Quick_Wins.tex#L242](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242)

4. **Bullet Cluster is still text-only, not simulation-backed in the repo snapshot.**
   - Problem lines:
     - [W6i107_BulletCluster.tex#L130](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L130)
     - [W6i107_BulletCluster.tex#L201](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201)

5. **Programme bookkeeping is diverging enough to undermine trust in the current state.**
   - Problem lines:
     - [ITERATION_TRACKER.md#L3](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L3)
     - [ITERATION_TRACKER.md#L1170](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/ITERATION_TRACKER.md#L1170)
     - [MASTER_FINDINGS_LIST.tex#L1785](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L1785)
     - [W6i105_Assessment.tex#L302](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L302)
     - [W6i106_Compiled.tex#L140](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L140)

## Reviewer judgment

If these five are not fixed, later Wave 6 “A+” promotions will continue to look less like hard closure and more like drift between aspirational summaries and the underlying artifacts.

