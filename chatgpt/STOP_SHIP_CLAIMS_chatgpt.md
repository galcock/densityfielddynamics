# Stop-Ship Claims (chatgpt)

Date: 2026-03-24
Role: external reviewer
Purpose: claims that should not be repeated externally until fixed or materially softened

## 1. Do not say the CMB TT spectrum is computed to 1.1% RMS with zero free parameters

Unsafe wording:

- [W6i106_Compiled.tex#L67](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L67)
- [W6i106_Compiled.tex#L71](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L71)
- [W6i106_Boltzmann_Core.tex#L321](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L321)
- [W6i106_Boltzmann_Core.tex#L391](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L391)

Why stop-ship:

- the visible Julia layer still does not show the claimed full pipeline
- exported high-level run functions are not actually defined in the visible file
- “zero free parameters” conflicts with visible imported/fixed cosmological defaults

Supporting code state:

- [DFDBolt.jl#L7](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L7)
- [DFDBolt.jl#L30](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L30)
- [DFDBolt.jl#L209](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L209)

## 2. Do not say TE/EE were fully computed and combined Planck fit is 1.031 with zero parameters

Unsafe wording:

- [W6i106_Compiled.tex#L69](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L69)
- [W6i106_Compiled.tex#L71](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L71)
- [W6i106_Polarization.tex#L174](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L174)
- [W6i106_Polarization.tex#L267](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Polarization.tex#L267)

Why stop-ship:

- the repo does not visibly contain the advertised polarization machinery and likelihood stack
- the parameter-accounting remains unresolved

## 3. Do not say CMB lensing and P(k) were computed from the Boltzmann output as closed results

Unsafe wording:

- [W6i106_Compiled.tex#L74](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L74)
- [W6i106_Compiled.tex#L75](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L75)
- [W6i106_Compiled.tex#L95](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L95)
- [W6i106_Lensing_Pk.tex#L141](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L141)
- [W6i106_Lensing_Pk.tex#L210](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Lensing_Pk.tex#L210)

Why stop-ship:

- the same compiled file concedes lensing is still analytic and there is no MCMC posterior
- the code/artifact base does not show the claimed full numerical closure

## 4. Do not say current Wave 6 cosmology is zero-parameter or all-derived

Unsafe wording:

- [W6i106_Compiled.tex#L115](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Compiled.tex#L115)
- [W6i102_Cosmology_Sprint.tex#L281](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i102_Cosmology_Sprint.tex#L281)
- [W6i106_Boltzmann_Core.tex#L281](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i106_Boltzmann_Core.tex#L281)

Why stop-ship:

- visible defaults/imports include `h`, `n_s`, `A_s`, `tau_reio`, baryon density, and sound-horizon calibration ingredients

Supporting code:

- [DFDBolt.jl#L43](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L43)
- [DFDBolt.jl#L58](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBolt.jl#L58)
- [DFDBackground.jl#L213](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBackground.jl#L213)
- [DFDBackground.jl#L217](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFDBackground.jl#L217)

## 5. Do not say Strong CP has a complete two-loop proof

Unsafe wording:

- [W6i101_Quick_Wins.tex#L213](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L213)
- [W6i101_Quick_Wins.tex#L266](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L266)
- [W6i101_Quick_Wins.tex#L634](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L634)

Why stop-ship:

- the document itself concedes the missing all-orders / BRST / counterterm closure:
  - [W6i101_Quick_Wins.tex#L242](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i101_Quick_Wins.tex#L242)

## 6. Do not say Bullet Cluster has been simulation-supported to a 120 kpc offset / 1.4x deficit

Unsafe wording:

- [W6i107_BulletCluster.tex#L130](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L130)
- [W6i107_BulletCluster.tex#L201](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L201)
- [W6i107_BulletCluster.tex#L216](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i107_BulletCluster.tex#L216)

Why stop-ship:

- no code, snapshots, maps, seeds, or output artifacts were found backing these tables

## 7. Do not say publication status is settled in any direction

Unsafe wording cluster A:

- [MASTER_FINDINGS_LIST.tex#L2146](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/DFD_Master_Findings/MASTER_FINDINGS_LIST.tex#L2146)

Unsafe wording cluster B:

- [MASTER_FINDINGS_LIST.tex#L51](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L51)
- [MASTER_FINDINGS_LIST.tex#L1785](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/MASTER_FINDINGS_LIST.tex#L1785)

Unsafe wording cluster C:

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L58](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L58)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L290](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L290)

Unsafe wording cluster D:

- [W6i105_Assessment.tex#L278](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L278)

Why stop-ship:

- the repo currently tells four incompatible publication stories

## 8. Do not say final / definitive / terminal unless the file is truly authoritative

Unsafe wording:

- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L4](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L4)
- [DFD_Master_Findings_FINAL_i1_to_i100.tex#L46](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/DFD_Master_Findings_FINAL_i1_to_i100.tex#L46)
- [W6i105_Assessment.tex#L33](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L33)
- [W6i105_Assessment.tex#L57](/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/Cross_Reference_Updates/W6i105_Assessment.tex#L57)

Why stop-ship:

- later same-day files already supersede these “final” markers

## Bottom line

The most dangerous current failure mode is not a bad theory claim. It is an externally checkable overstatement that collapses instantly when someone opens the repo.

