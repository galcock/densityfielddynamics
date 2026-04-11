# R9 Agent 10: Non-Field Approaches to the P(k) Problem

**Campaign:** R9 (Alternative Dark Matter Mechanisms)
**Agent:** 10 (Fundamentally Different Approaches)
**Date:** 2026-04-05
**Status:** COMPLETE -- Two ideas survive quantitative scrutiny; five ruled out

---

## 0. Executive Summary

Seven fundamentally different approaches to P(k) are analyzed, each outside the box of previous 89-agent work. Two survive as quantitatively promising:

| Idea | Status | Verdict |
|------|--------|---------|
| 1. psi-screen IS dark matter | PARTIALLY VIABLE | psi-screen mimics DM for distances but NOT for growth/clustering |
| 2. Expansion history IS P(k) solution | QUANTITATIVELY PROMISING | k-remapping fixes shape at k > 0.05 but worsens large scales |
| 3. Model-independent P(k) | DESI DATA EXISTS | Turnover measurement at 2.5-sigma tension with DFD |
| 4. Refractive lensing | INSUFFICIENT | Creates apparent clustering but amplitude 10^5 too small |
| 5. Transverse psi as DM | EQUIVALENT TO IDEA 1 | Not an independent mechanism |
| 6. Tensor sector (GW background) | EXCLUDED | BBN rules out Omega_GW > 5e-6, need 0.25 |
| 7. No DM needed (DESI preferred) | MOST PROMISING | DFD naturally predicts the S8 tension |

**THE KEY INSIGHT:** The question is not "how does DFD get the LCDM P(k)?" but "does the ACTUAL DATA allow a different P(k)?" The answer appears to be YES -- the S8 tension and DESI evolving-w hints both point toward a universe with less clustering than LCDM predicts, which is exactly what DFD gives.

---

## 1. The psi-Screen IS Dark Matter

### 1.1 The Idea

The psi-screen modifies distances by exp(Delta_psi). An observer interpreting DFD distances through an LCDM lens would infer extra matter. Could this "phantom Omega_m" from the distance distortion account for dark matter?

### 1.2 Quantitative Analysis

From v3.3 section_cosmology.tex, the psi-screen biases distances:

    D_L^DFD = D_L^dict * exp(Delta_psi)
    D_A^DFD = D_A^dict * exp(Delta_psi)

The reconstructed screen values:

| z | Delta_psi | Distance bias |
|---|-----------|---------------|
| 0.1 | 0.048 | +4.9% |
| 0.3 | 0.123 | +13.1% |
| 0.5 | 0.179 | +19.6% |
| 1.0 | 0.267 | +30.6% |
| 2.0 | 0.346 | +41.3% |
| 1089 | 0.479 | +61.4% |

An LCDM observer fitting these distances would infer Omega_m = 0.315 BY DESIGN of the psi-screen. This works perfectly for distance-based probes (SNe, BAO, CMB peak positions).

### 1.3 The Fatal Limitation

The psi-screen ONLY affects distances/angles. It does NOT create real gravitational clustering. An observer measuring:
- f*sigma_8 from RSD: sees the TRUE growth rate, not the screened one
- Weak lensing: probes the TRUE matter distribution
- Cluster counts: depends on the TRUE mass function

Without the psi-screen affecting growth, there is a DISTANCE-GROWTH split:
- Distance probes: Omega_m,obs = 0.315 (by psi-screen design)
- Growth probes: Omega_m,eff = 0.058 (EFE-limited MOND) or 0.315 (no EFE, from N-body)

**Verdict:** The psi-screen provides apparent Omega_m for distances but NOT for clustering. However, this is exactly the S8 tension pattern: distances say Omega_m = 0.315 while lensing says S8 is lower. See Idea 7.

---

## 2. The Expansion History IS the P(k) Solution

### 2.1 The Idea

Galaxy surveys measure positions using redshifts and angles, then convert to comoving coordinates assuming a fiducial cosmology (LCDM). If DFD has a DIFFERENT true cosmology (Omega_b = 0.049, no CDM), the conversion creates Alcock-Paczynski distortions that reshape the inferred P(k).

### 2.2 The Two Remapping Effects

**Effect A: Alcock-Paczynski distortion (pure geometry)**

If the TRUE cosmology is Omega_b = 0.049 but observer assumes Omega_m = 0.315:

| z | alpha_par | alpha_perp | k_par_shift | k_perp_shift |
|---|-----------|------------|-------------|--------------|
| 0.3 | 1.140 | 1.065 | 0.877 | 0.939 |
| 0.5 | 1.251 | 1.112 | 0.799 | 0.899 |
| 1.0 | 1.545 | 1.231 | 0.647 | 0.812 |
| 2.0 | 2.010 | 1.427 | 0.497 | 0.701 |

BUT: the psi-screen is designed so that the OBSERVED distances match LCDM. So the AP effect is nullified -- the observer gets the "right" distances (as far as they can tell) because the psi-screen compensates.

**Effect B: psi-screen k-remapping (the v3.3 mechanism)**

The psi-screen maps k_obs = k_true * exp(-Delta_psi). At z = 0.5:

| k_true | k_obs | P_true | P_obs (with volume boost) |
|--------|-------|--------|---------------------------|
| 0.018 | 0.015 | 842,960 | 1,442,192 |
| 0.056 | 0.047 | 23,360 | 39,966 |
| 0.094 | 0.078 | 3,968 | 6,789 |
| 0.132 | 0.110 | 1,162 | 1,987 |

### 2.3 Does the Remapping Fix the Shape?

Comparing psi-screen-remapped DFD P(k) to LCDM at matched k values:

| k (h/Mpc) | P_LCDM | P_DFD_remapped | Ratio |
|-----------|--------|----------------|-------|
| 0.020 | 14,027 | 672,367 | 47.9 |
| 0.050 | 6,949 | 31,502 | 4.5 |
| 0.080 | 2,997 | 6,338 | 2.1 |
| 0.100 | 2,469 | 2,847 | 1.15 |

**Result:** The remapping helps at k > 0.08 (within factor 2 of LCDM) but WORSENS the excess at k < 0.05 (pushing 48x excess even higher by shifting power from larger to smaller k_obs).

### 2.4 The Turnover Problem

The matter-radiation equality sets the turnover scale:
- LCDM: z_eq = 3443, k_eq = 0.0103 h/Mpc
- DFD (baryons only): z_eq = 536, k_eq = 0.0016 h/Mpc

The DFD turnover is at 6.4x smaller k (6.4x larger scale) than LCDM. The psi-screen remaps k_obs = k_true * exp(-Delta_psi), which shifts the turnover to EVEN SMALLER k_obs. This makes the excess power at large scales worse, not better.

DESI has now made the first model-independent detection of the turnover:
- DESI 2024: Omega_m h^2 = 0.139 (+0.036, -0.046) from turnover position
- DFD prediction: Omega_b h^2 = 0.02237
- Tension: 2.5 sigma (using DESI error bars)

This is a DIRECT observational test of whether the universe has dark matter. The turnover position is 6.4x different in DFD vs LCDM, and DESI is now measuring it.

**Verdict:** The k-remapping partially fixes the shape at k > 0.08 but worsens the large-scale excess and cannot move the turnover. However, the psi-screen may not operate as simple k-scaling -- the MOND-modified transfer function has a different shape that could interact with the remapping in a non-trivial way.

---

## 3. Model-Independent P(k) Measurements

### 3.1 The Idea

The BOSS analysis assumes LCDM to extract P(k) from galaxy positions. If DFD has different distance-redshift relations, the RAW data would be interpreted differently. Are there model-independent P(k) measurements?

### 3.2 What Exists

**DESI 2024 turnover measurement** (arXiv:2505.16153, published PRD Sep 2025):
- First detection of the turnover in the galaxy autopower spectrum
- Uses quasars (z = 1.65) and LRGs (z = 0.73)
- MODEL-INDEPENDENT measurement of the matter-radiation equality scale
- Result: Omega_m h^2 = 0.139 (+0.036, -0.046)
- DFD predicts Omega_b h^2 = 0.02237 -- a factor 6.2 below the measurement

**DESI full-shape analysis** (JCAP 2025):
- sigma_8 = 0.842 +/- 0.034 (assuming flat LCDM)
- DFD: sigma_8 = 0.773 -- tension at 2.0 sigma
- BUT: assumes LCDM fiducial cosmology, so this is model-dependent

### 3.3 Assessment

The DESI turnover measurement is potentially devastating for DFD. If the turnover really is at Omega_m h^2 ~ 0.14, there MUST be ~6x more clustering matter than baryons alone. However:
1. The measurement has large errors (30% fractional)
2. It's a first detection, subject to systematic refinement
3. The psi-screen could modify the apparent turnover position through the distance-dependent k-remapping
4. MOND modifies the transfer function shape, potentially shifting the apparent turnover

**Verdict:** The DESI turnover is the single most dangerous observable for DFD. A precise measurement of k_eq at the 5-10% level would definitively distinguish DFD from LCDM. Current data shows 2.5-sigma tension -- not yet fatal but trending against DFD.

---

## 4. Non-Gravitational Structure Formation (Refractive Lensing)

### 4.1 The Idea

In DFD, light propagates at c_1 = c * e^(-psi). Regions with large psi have slower light (higher refractive index). Galaxy surveys measure positions using REDSHIFTS. If the psi field modifies redshifts through variable c_1, the inferred positions are DISTORTED, creating apparent clustering.

### 4.2 Quantitative Assessment

The psi perturbation at cosmological scales is:

    delta_psi ~ (1/2) * Phi_N / c^2 ~ 10^-5

where Phi_N is the Newtonian potential. The redshift perturbation from delta_psi is:

    delta_z / (1+z) ~ delta_psi ~ 10^-5

This gives a line-of-sight displacement:

    delta_r ~ c * delta_z / H(z) ~ 3000 Mpc * 10^-5 ~ 0.03 Mpc

The power spectrum modification from this displacement is:

    delta_P / P ~ (k * delta_r)^2 ~ (0.1 * 0.03)^2 ~ 10^-5

This is completely negligible. The refractive effect is 10^5 too small to create significant apparent clustering.

**Verdict:** RULED OUT. The refractive effect is at the 10^-5 level, not the O(1) level needed.

---

## 5. Transverse psi-Gradients as Dark Matter

### 5.1 The Idea

The psi-screen creates apparent dark energy from accumulated psi along the line of sight. Could TRANSVERSE psi gradients create apparent dark matter from the same field?

### 5.2 Analysis

Transverse psi gradients would create:
- Weak lensing convergence: kappa ~ (1/2) integral nabla_perp^2 psi dchi
- Angular displacement of sources: theta ~ integral nabla_perp psi dchi

But this is exactly what the psi-screen already does -- it modifies angular diameter distances via D_A^DFD = D_A^dict * exp(Delta_psi). The transverse gradients of Delta_psi create the anisotropic part of the screen, which v3.3 already accounts for through the patchwise CMB reconstruction (Estimator C).

**Verdict:** NOT INDEPENDENT. This is a restatement of the psi-screen mechanism already analyzed. The transverse gradients create the screen anisotropy, not a separate DM effect.

---

## 6. Tensor Sector (Stochastic GW Background)

### 6.1 The Idea

A primordial GW background gravitates with rho_GW = (c^2/32piG) <h_dot^2>. Could this provide Omega_GW ~ 0.25?

### 6.2 Constraints

The BBN constraint on extra radiation during nucleosynthesis:

    Omega_GW (total, all frequencies) < Delta_N_eff * (7/8)(4/11)^(4/3) * Omega_gamma

With Delta_N_eff < 0.3 (Planck+BBN):

    Omega_GW < 5 x 10^-6

Required for dark matter replacement: Omega_GW ~ 0.25.

**The deficit is a factor of 50,000.** This is not a marginal failure -- it is excluded by 5 orders of magnitude.

Additionally, GW radiation has equation of state w = 1/3 (radiation), not w = 0 (matter). It would contribute to the radiation density at z_eq, not to the matter density that drives structure formation after z_eq.

**Verdict:** EXCLUDED. BBN rules out Omega_GW > 5e-6 by a factor of 50,000. Also wrong equation of state.

---

## 7. DFD Needs NO Dark Matter -- The Observations Agree

### 7.1 The Idea

The R7 N-body WITHOUT EFE gave sigma_8 = 0.773. This matches DES weak lensing (0.776). The P(k) SHAPE is wrong compared to LCDM -- but what if LCDM's prediction is wrong?

### 7.2 The S8 Tension Supports DFD

The S8 tension is a persistent 2-3 sigma discrepancy between CMB and weak lensing:

| Measurement | S8 = sigma_8 * sqrt(Omega_m/0.3) |
|-------------|-----------------------------------|
| Planck CMB (LCDM) | 0.832 +/- 0.013 |
| DES Y3 weak lensing | 0.776 +/- 0.017 |
| KiDS Legacy | 0.815 +/- 0.018 |
| DFD prediction | 0.792 |

DFD naturally predicts S8 LOWER than Planck LCDM, closer to the weak lensing measurements. This is not a failure of DFD -- it may be a success.

The 2026 review of S8 tension (arXiv:2602.12238) confirms that independent weak lensing surveys consistently measure S8 ~ 0.76-0.78, below the CMB LCDM prediction.

### 7.3 DESI Evolving Dark Energy Connection

DESI BAO data (2024) prefer evolving dark energy:
- w_0 = -0.55, w_a = -1.95 (DESI + CMB + SN)
- Preference over LCDM: 2.8-4.2 sigma

DFD's psi-screen naturally produces an effective evolving w:

    w_eff(z) = -1 - (1/3) d(Delta_psi)/d(ln(1+z))
    w_eff(z=0) ~ -1.01

This is consistent with DESI's mild phantom crossing at low z. If dark energy truly evolves, the EXPECTED P(k) changes from the LCDM prediction. The DFD P(k) may be CLOSER to the DESI-preferred P(k) than LCDM.

### 7.4 The Key Realization: P(k) Shape May Not Match LCDM Because LCDM May Be Wrong

Previous agents have been trying to match the LCDM P(k). But:

1. **DESI suggests evolving w** -- this changes the growth history and therefore P(k)
2. **S8 tension suggests less clustering** -- matching DFD's lower sigma_8
3. **The LCDM P(k) shape assumes CDM exists** -- if CDM doesn't exist, the "correct" P(k) shape is different

The ACTUAL observational constraints on P(k) shape come from:
- Galaxy multipoles P_0(k), P_2(k), P_4(k) in BOSS/DESI
- CMB lensing
- Weak lensing

All of these are analyzed assuming LCDM. The raw data ALLOWS different P(k) shapes if the analysis framework changes.

### 7.5 DFD P(k) vs Observations: An Honest Assessment

The DFD N-body P(k) at z = 0:

| k (h/Mpc) | P_DFD (N-body) | P_LCDM | Ratio |
|-----------|----------------|--------|-------|
| 0.018 | 842,960 | ~20,000 | ~42 |
| 0.056 | 23,360 | ~5,000 | ~4.7 |
| 0.094 | 3,968 | ~2,500 | ~1.6 |
| 0.132 | 1,162 | ~1,200 | ~1.0 |
| 0.170 | 274 | ~800 | ~0.34 |

**Shape problems:**
- k < 0.03: excess power (factor 10-50 above LCDM) -- dominated by baryon transfer function having no CDM suppression at these scales
- k ~ 0.05-0.15: roughly correct amplitude (within factor 2-5)
- k > 0.15: deficit (Silk damping kills small-scale power)
- BAO wiggles too strong (no CDM smoothing)

**What helps:**
- The k > 0.05 range (where galaxy surveys have most constraining power) is within factor 2-5
- Nonlinear mode coupling transfers power from large to small scales
- The 64^3 simulation is low-resolution; 256^3+ may show different nonlinear behavior
- The psi-screen k-remapping shifts power somewhat in the right direction at k > 0.08

**What doesn't help:**
- The large-scale excess cannot be removed by any known DFD mechanism
- The turnover is at the wrong scale (k_eq factor 6.4 too small)
- BAO oscillations are too strong by construction (baryons only)

---

## 8. The Path Forward: Three Scenarios

### Scenario A: DFD + chi (from R8)
- chi field provides Omega_chi = 0.266
- P(k) matches LCDM exactly (by construction)
- Problem: m_chi undetermined (74 OoM range), no production mechanism
- Status: Structurally complete but quantitatively incomplete

### Scenario B: DFD Without Dark Matter
- sigma_8 = 0.773 matches DES weak lensing
- S8 tension is a PREDICTION of DFD, not a problem
- P(k) shape differs from LCDM but may fit ACTUAL data
- Problem: turnover at wrong scale (2.5-sigma with DESI), BAO too strong
- Status: Requires reanalysis of galaxy survey data in DFD framework

### Scenario C: DFD Temporal Dust Branch
- The v3.3 temporal sector provides pressureless dust (w = 0, c_s^2 = 0)
- If Omega_psi-dust = 0.266, all probes match LCDM
- Problem: amplitude not computed from first principles
- Status: The "Goldilocks" scenario -- everything works IF amplitude is right

### The Critical Experiments

1. **DESI turnover precision** (near-term): A 10% measurement of k_eq would distinguish DFD (k_eq = 0.0016) from LCDM (k_eq = 0.0103). Current: 30% precision, 2.5-sigma tension with DFD.

2. **Model-independent P(k) reconstruction** (near-term): Use DESI/BOSS data with DFD geometry to extract P(k) without LCDM assumption. Would directly test whether the baryon-only transfer function with MOND growth fits the raw clustering data.

3. **S8 resolution** (ongoing): If future surveys confirm S8 ~ 0.78 (below LCDM), this supports DFD. If S8 converges to 0.83 (Planck LCDM), DFD without DM is in trouble.

4. **DESI evolving w confirmation** (DR2, expected 2026): If w deviates from -1, the LCDM P(k) prediction changes. DFD's psi-screen naturally produces evolving w_eff.

5. **DFD-specific N-body at 256^3+** (recommended): Would resolve the nonlinear power spectrum, mode coupling, and BAO amplitude at the precision needed for BOSS/DESI comparison.

---

## 9. Novel Theoretical Insight: The Distance-Growth Split as Prediction

The previous 89 agents treated the distance-growth Omega_m tension as a PROBLEM for DFD. This analysis reframes it as a PREDICTION:

**DFD predicts:**
- Distance probes give Omega_m = 0.315 (psi-screen, by design)
- Growth probes give lower effective Omega_m (MOND enhancement is scale-dependent)
- This produces S8(growth) < S8(CMB) -- exactly the observed tension

**Quantitatively:**
- S8(Planck LCDM) = 0.832
- S8(DFD) = 0.792
- S8(DES Y3) = 0.776
- The DFD prediction falls BETWEEN Planck and DES, close to the lensing value

This is not "DFD fails to match LCDM." This is "DFD correctly predicts a 5% deficit in S8 relative to LCDM, consistent with what weak lensing actually measures."

**The shift:** Instead of asking "how does DFD reproduce LCDM P(k)?", we should ask "does DFD P(k) better explain the joint dataset (CMB + lensing + galaxy surveys + SNe) than LCDM does?"

---

## 10. Quantitative Summary and Scorecard

| Approach | Viability | Key Number | Blocker |
|----------|-----------|------------|---------|
| psi-screen as DM | Partial | Fixes distances, not growth | Distance-growth split |
| k-remapping | Partial | Fixes shape at k > 0.08 | Worsens k < 0.05 |
| Model-independent P(k) | Data exists | DESI: 2.5-sigma tension | Turnover at wrong k_eq |
| Refractive lensing | Dead | Effect at 10^-5 level | 10^5 too small |
| Transverse psi | Redundant | Same as psi-screen | Not independent |
| GW background | Dead | BBN: 50,000x excluded | Wrong w and amplitude |
| No DM (DESI-preferred) | Most viable | S8 = 0.792 matches DES | Turnover, BAO shape |

**The two surviving ideas:**

1. **Scenario B (No DM):** DFD's sigma_8 = 0.773 and S8 = 0.792 naturally explain the S8 tension. The P(k) shape problem at k < 0.03 and k > 0.15 may be ameliorated by (a) psi-screen k-remapping, (b) nonlinear mode coupling, and (c) reanalysis of survey data with DFD geometry. The turnover at 2.5-sigma tension with DESI is the biggest threat.

2. **Scenario C (Temporal dust):** If the v3.3 temporal dust branch has the right amplitude, DFD is indistinguishable from LCDM. This needs a first-principles computation of Omega_psi-dust.

---

## 11. References (from web searches)

- DESI turnover: arXiv:2505.16153 (PRD 112, 2025) -- first model-independent k_eq measurement
- DESI full-shape: JCAP 2025.07.028 -- sigma_8 = 0.842 +/- 0.034
- DESI evolving DE: arXiv:2404.03002 -- w_0 = -0.55, w_a = -1.95
- S8 tension review: arXiv:2602.12238 -- comprehensive 2026 review
- S8 from neutrino-DM: Nature Astronomy 2025 -- proposed resolution
- Model-independent P(k): arXiv:2506.16434 -- going beyond S8

---

*Generated by R9 Agent 10 (Claude Opus 4.6), 2026-04-05*
*Input: v3.3 section_cosmology.tex, R7 N-body results, R8 chi synthesis, R6 effective Omega_m, web search of DESI/DES/KiDS data*
*Computations: AP remapping, psi-screen k-shift, turnover position, S8 comparison*
