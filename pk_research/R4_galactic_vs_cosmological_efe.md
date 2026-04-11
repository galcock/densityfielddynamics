# R4 Agent: Galactic vs Cosmological EFE -- Are They the Same Mechanism?

## Date: 2026-04-05
## Status: Complete analysis with definitive answer

---

## EXECUTIVE SUMMARY

**The cosmological EFE in v3.3 does NOT work the same way as the galactic EFE.** The galactic mechanism enters through a spatial gradient; the cosmological claim invokes a temporal evolution rate. These are fundamentally different physics. The v3.3 claim that "a_ext ~ cH_0 ~ 6a_0" provides a cosmological EFE is an **unproven assertion by analogy**, not a derived result from the DFD action.

The detailed analysis reveals:
1. The spatial gradient mechanism (galactic EFE) is rigorous and well-understood
2. The cosmological analogue requires a DIFFERENT mechanism -- the temporal K-sector
3. The temporal sector CAN provide a cosmological EFE-like effect, but NOT through the same composition law as the galactic case
4. The R2 and R3 agent analyses already established that Delta_bar = 0 by construction
5. The effective "EFE" must arise from the perturbation's own dynamics, not from a pre-existing background

---

## 1. THE GALACTIC EFE: HOW IT ACTUALLY WORKS

### 1.1 The mechanism

In AQUAL/QUMOND, a self-gravitating subsystem (galaxy) embedded in a larger system (cluster) satisfies:

    nabla . [mu(|nabla psi_total|/a_0) nabla psi_total] = 4 pi G rho

where psi_total = psi_internal + psi_external. The external field psi_ext has a nonzero spatial gradient:

    nabla psi_ext = g_ext (a constant vector)

The key: |nabla psi_total| = |nabla psi_int + g_ext|.

When |g_ext| >> |nabla psi_int|:
- mu is evaluated at |g_ext|/a_0 >> 1
- mu ~ 1 (Newtonian regime)
- The internal dynamics become effectively Newtonian

When |g_ext| << |nabla psi_int|:
- mu is determined by the internal gradient
- Standard MOND phenomenology applies

### 1.2 What makes it work

Three essential ingredients:
1. **A nonzero spatial gradient** nabla psi_ext != 0
2. **A preferred spatial direction** (the direction of g_ext)
3. **Superposition of gradients** in the nonlinear mu function

The EFE breaks the strong equivalence principle precisely because the nonlinear mu-function does not respect superposition: mu(|A + B|) != mu(|A|) + mu(|B|).

### 1.3 The composition law version

DFD's saturation-union composition law (Appendix Q of v3.3):

    mu(psi_1 + psi_2) = 1 - (1 - mu(psi_1))(1 - mu(psi_2))

gives the EFE theorem:

    mu(psi_0 + Delta_psi) - mu(psi_0) = (1 - mu(psi_0)) mu(Delta_psi)

When psi_0 corresponds to a large external field (mu(psi_0) ~ 1), perturbations see mu_eff ~ 1 regardless of their own amplitude.

---

## 2. QUESTION 1: THE SPATIAL GRADIENT ARGUMENT

### 2.1 Statement

In a homogeneous FRW universe, there is NO preferred spatial direction. The Hubble flow is isotropic -- every point sees the same expansion in every direction.

Therefore: **nabla psi_bar = 0** (no spatial gradient from the Hubble flow).

The Hubble flow contributes to psi_dot (temporal evolution), not to nabla psi (spatial gradient).

### 2.2 Verification: CORRECT

This argument is **rigorously correct**. In detail:

**The FRW background field:** psi_bar = psi_bar(t) only (no spatial dependence by homogeneity and isotropy). Therefore:

    nabla psi_bar = 0 identically

    x_s = |nabla psi_bar| / a_* = 0

    mu_spatial(x_s) = mu(0) = 0

This is confirmed by the R2 xbar derivation agent (Task 1, section (a)):
"In the homogeneous FRW background, by symmetry, grad psi_bar = 0. Therefore x_s = |grad psi_bar| / a* = 0. This is EXACT."

**Consequence:** If only the spatial sector mattered, the cosmological background would be in the deep-MOND regime with mu_0 = 0 and G_eff = G/0 (divergent). This is the "deep-MOND catastrophe" that the cosmological EFE is invoked to solve.

**The galactic EFE mechanism DOES NOT APPLY to the homogeneous cosmological background.** There is no spatial gradient to regularize the equation.

### 2.3 Literature support

This is well-understood in the MOND literature. Nusser (2002, MNRAS 331:909) used the "Jeans swindle" to write a MOND-type relationship between density fluctuations and gravitational force, precisely because the homogeneous background provides no spatial gradient. The problem is inherently nonlinear from the onset in MOND cosmology.

Milgrom himself (2014, CJP 93:107) acknowledged that MOND structure formation remains an open challenge, and no theory has been shown to fully address the mass discrepancies in cosmology that are otherwise explained by dark matter.

---

## 3. QUESTION 2: THE TEMPORAL psi_dot CONTRIBUTION

### 3.1 The temporal sector

In DFD, the full action has two kinetic sectors:

    S = integral dt d^3x { (a_*^2 / 8piG) [W(|nabla psi|^2/a_*^2) + K((c/a_0)|psi_dot - psi_dot_0|)] - coupling }

- W depends on |nabla psi|^2 (spatial gradients)
- K depends on (c/a_0)|psi_dot - psi_dot_0| (temporal deviation from screen background)

### 3.2 The background temporal deviation: Delta_bar = 0

The temporal invariant is Delta = (c/a_0)|psi_dot - psi_dot_0|.

psi_dot_0 is DEFINED as the screen-background field rate (Definition 3, Appendix Q). For the FRW background:

    psi_dot_0 = psi_bar_dot (by definition of the screen background)

Therefore:

    Delta_bar = (c/a_0)|psi_bar_dot - psi_dot_0| = 0

**The temporal sector's BACKGROUND deviation vanishes by construction.** It is a deviation-invariant quantity.

### 3.3 Cross-sector composition

Applying the composition law across sectors:

    mu_total = 1 - (1 - mu_spatial(0))(1 - mu_temporal(0)) = 1 - (1)(1) = 0

**The composition law gives mu_total = 0 for the FRW background.** Neither sector provides a nonzero background mu. The composition law does NOT rescue the deep-MOND catastrophe.

### 3.4 Verdict on Question 2

The temporal psi_dot does NOT provide an EFE-like effect through the same mechanism as the galactic EFE. The background is exactly zero in both sectors. The v3.3 claim is **not derivable** from the action as stated.

---

## 4. QUESTION 3: PERTURBATION CONTRIBUTIONS

### 4.1 Setup

For a perturbation delta_psi(x,t) on the FRW background:

**Spatial argument:** x_s = |nabla delta_psi| / a_* = k |delta_psi_k| / a_*
**Temporal argument:** Delta_pert = (c/a_0)|delta_psi_dot|

Both are determined by the perturbation itself, not by a pre-existing background.

### 4.2 Spatial sector mu

    x_s = k |delta_psi_k| / a_*

For typical values at z = 0, k = 0.1 h/Mpc:

    x_s ~ 1.3 x 10^{-4}
    mu_s ~ x_s ~ 1.3 x 10^{-4}

This gives G_eff ~ G / mu_s ~ 7700 G -- deep MOND, massive enhancement.

### 4.3 Temporal sector mu

    Delta_pert = (c/a_0)|delta_psi_dot|

For a growing perturbation delta_psi ~ D(a) f(x):

    delta_psi_dot = H f_growth D f(x)

where f_growth = d ln D / d ln a is the growth rate.

    Delta_pert = (c H f_growth / a_0) |delta_psi|

At z = 0: c H_0 / a_0 ~ 5.8, and for MOND growth f_growth ~ 2:

    Delta_pert = 11.6 |delta_psi| / c^2

But delta_psi / c^2 ~ 10^{-5} (for linear perturbations), so:

    Delta_pert ~ 10^{-4}
    mu_t ~ 10^{-4}

### 4.4 Composition of perturbation-level mu values

    mu_total = mu_s + mu_t - mu_s mu_t
             ~ 1.3e-4 + 1.0e-4 - (negligible)
             ~ 2.3e-4

The temporal sector adds ~ 77% to the perturbation's own mu. This is significant but does NOT change the qualitative picture: the system remains deep in MOND.

### 4.5 The critical point

**There is no large background mu to regularize against.** Both sectors contribute small, perturbation-level mu values. The "EFE" from the Hubble flow (mu ~ 0.85 from x_bar ~ 5.85) does NOT emerge from this calculation.

---

## 5. QUESTION 4: THE RATIO mu_t / mu_s

### 5.1 Scale dependence

For a Fourier mode with wavenumber k:

**Spatial:**
    x_s = k |delta_psi_k| / a_*

**Temporal:**
    Delta_pert = (c/a_0) H f_growth |delta_psi_k|

In deep MOND (both arguments << 1):

    mu_s ~ x_s = k |delta_psi_k| / a_*
    mu_t ~ Delta_pert = (c H f_growth / a_0) |delta_psi_k|

The ratio:

    mu_t / mu_s = (c H f_growth / a_0) / (k / a_*)
                = (c H f_growth / a_0) * (a_* / k)
                = (c H f_growth / a_0) * (2 a_0 / (c^2 k))
                = 2 H f_growth / (c k)

### 5.2 Numerical evaluation

Using H_0 = 2.18e-18 /s, f_growth = 2, c = 3e8 m/s:

    mu_t / mu_s = 2 * 2.18e-18 * 2 / (3e8 * k_phys)

Converting k: for k = 0.1 h/Mpc, k_phys ~ 2.2e-24 /m (comoving/h conversion):

    mu_t / mu_s = 8.72e-18 / (3e8 * 2.2e-24) = 8.72e-18 / 6.6e-16 ~ 0.013

| k (h/Mpc) | mu_t / mu_s | Which dominates? |
|-----------|-------------|-----------------|
| 0.001     | 1.3         | Temporal         |
| 0.005     | 0.26        | Comparable       |
| 0.01      | 0.13        | Spatial dominates |
| 0.05      | 0.026       | Spatial dominates |
| 0.10      | 0.013       | Spatial dominates |
| 0.30      | 0.0044      | Spatial dominates |

### 5.3 The crossover scale

mu_t / mu_s = 1 when:

    k_cross = 2 H f_growth / c ~ 2 * 2.18e-18 * 2 / 3e8 ~ 2.9e-26 /m
    ~ 0.0009 h/Mpc

This is the Hubble scale. For all sub-Hubble modes (k >> 0.001 h/Mpc), the spatial sector dominates perturbation dynamics. The temporal sector is a sub-leading correction.

### 5.4 Dependence on delta

The ratio mu_t/mu_s is INDEPENDENT of the perturbation amplitude delta (both scale linearly with |delta_psi_k| in the deep-MOND regime). The ratio depends only on k and cosmological parameters.

In the Newtonian regime (both arguments >> 1), both mu -> 1, so mu_t/mu_s -> 1 trivially.

---

## 6. QUESTION 5: DOES THE TEMPORAL SECTOR CHANGE THE PICTURE?

### 6.1 Linear regime

Both mu_s and mu_t are small (~10^{-4}). The total mu ~ 2e-4. The system is deep in MOND. Growth is rapid (D ~ a^2 or faster). This matches Nusser (2002) who found MOND overshoots sigma_8 by a factor of ~2.

### 6.2 Which sector controls the transition?

The transition from deep-MOND to Newtonian occurs when the relevant argument reaches ~1.

**Spatial transition:** x_s ~ 1 when k |delta_psi_k| ~ a_*
**Temporal transition:** Delta ~ 1 when (cH f/a_0)|delta_psi_k| ~ 1

From x_s ~ 1: |delta_psi_k| ~ a_*/k = 2a_0/(c^2 k)
From Delta ~ 1: |delta_psi_k| ~ a_0/(cH f)

The ratio of critical amplitudes:

    delta_psi(temporal) / delta_psi(spatial) = k a_0 / (c H f * c^2 k / (2a_0))
    ...simplifying: = 2 a_0^2 / (c^3 H f k / k) -- this gets complicated.

More directly: since mu_t/mu_s ~ 0.013 at k = 0.1 h/Mpc, the SPATIAL sector always reaches mu ~ 1 first (at a smaller perturbation amplitude) for all sigma_8-relevant scales.

**The spatial sector controls the MOND-to-Newtonian transition for all sub-Hubble modes.**

### 6.3 Impact on sigma_8

The R3 temporal contribution agent computed this precisely:
- With EFE: epsilon_t' ~ 0.002 at k = 0.1 h/Mpc
- Delta(sigma_8)/sigma_8 ~ 0.4%
- This is a sub-percent correction, below observational uncertainty

Without the assumed EFE, the temporal term would dominate at k ~ H/c (Hubble-scale modes) but remains sub-dominant at sigma_8 scales (k ~ 0.1 h/Mpc).

### 6.4 Bottom line

The temporal sector:
- Adds a ~50-77% correction to the perturbation-level mu (from ~1.3e-4 to ~2.3e-4)
- Does NOT change the deep-MOND character of linear perturbations
- Does NOT provide the large background mu ~ 0.85 that the v3.3 paper claims
- Is sub-dominant to the spatial sector for all k > 0.001 h/Mpc

---

## 7. THE FUNDAMENTAL PROBLEM: WHERE DOES x_bar ~ 5.85 COME FROM?

### 7.1 The v3.3 claim

The paper claims "cosmological External Field Effect from the Hubble flow (a_ext ~ cH_0 ~ 6a_0)" and uses x_bar = cH_0/a_0 ~ 5.85 in the linearized perturbation equation.

### 7.2 What the R2 xbar agent found

The R2 xbar derivation agent's key finding (Task 3):

"The paper's statement is actually a PROMISSORY NOTE, not a derived result. The N-body simulation (64^3) was run WITHOUT the EFE. The paper says the 5.4x overshoot is 'physically expected' because the EFE was not included, and 'with the EFE, the effective enhancement drops from ~400 to ~1.2.' But this claim is not derived from the action. It is an ASSERTION based on analogy with the galactic EFE."

### 7.3 The three possible sources of x_bar

| Source | nabla psi_bar | Delta_bar | x_bar |
|--------|--------------|-----------|-------|
| Spatial FRW background | = 0 | n/a | 0 |
| Temporal FRW background | n/a | = 0 | 0 |
| Cross-composition | 0 + 0 | 0 + 0 | 0 |

**All three give x_bar = 0. There is no mechanism in the stated action to produce x_bar ~ 5.85.**

### 7.4 What the paper actually needs

The paper needs one of the following to be true:

**(a) Redefine psi_dot_0 differently:** If psi_dot_0 is NOT set equal to psi_bar_dot but instead to some other reference (e.g., a Minkowski-space value), then Delta_bar != 0 and the temporal sector could provide a nonzero background mu. This would require modifying Definition 3 in Appendix Q.

**(b) Invoke a mode-coupling/mean-field argument:** In the nonlinear MOND equation, the coexistence of many perturbation modes creates an effective background field (the "cosmic web") that lifts any given mode out of deep MOND. This is plausible but NOT the galactic EFE mechanism.

**(c) Use a different definition of the composition law:** Apply the composition to the RATE of psi (the Hubble flow rate itself, not its deviation from the screen background) rather than to the deviation invariant.

**(d) Modify the action:** Add a term that explicitly couples the cosmological expansion rate to the spatial mu-function.

---

## 8. LITERATURE COMPARISON

### 8.1 Nusser (2002)

Nusser (MNRAS 331:909) performed the first numerical study of MOND structure formation. Key findings:
- Used the "Jeans swindle" to handle the homogeneous background
- Growth in MOND goes as delta ~ a^2 (vs delta ~ a for Newtonian/CDM)
- MOND overshoots sigma_8 by a factor of ~2
- The problem is inherently nonlinear from the onset
- Did NOT include any cosmological EFE
- Reference: https://arxiv.org/abs/astro-ph/0109016

### 8.2 Sanders (1998, 2001, 2008)

Sanders studied MOND structure formation predictions:
- Structure forms faster in MOND (bottom-up, hierarchical)
- The enhanced growth (delta ~ a^2) produces too much clustering
- Can be made consistent only with "strong anti-bias" or reduced a_0
- Did NOT invoke a cosmological EFE from the Hubble flow

### 8.3 Famaey & McGaugh (2012)

The comprehensive MOND review (Living Reviews in Relativity 15:10):
- Discusses the galactic EFE thoroughly (via AQUAL nonlinearity)
- Notes the coincidence a_0 ~ cH_0 as possibly pointing to deep cosmological origins
- Does NOT derive a cosmological EFE from the Hubble expansion
- Acknowledges MOND cosmology remains an open problem
- Reference: https://link.springer.com/article/10.12942/lrr-2012-10

### 8.4 Milgrom (2010, 2014)

Milgrom's own statements:
- The QUMOND formulation (MNRAS 403:886) provides the quasi-linear framework
- The 2014 review (CJP 93:107, arXiv:1404.7661) stresses that a_0 ~ cH_0 may point to MOND having deep interplay with cosmology
- Milgrom does NOT claim that the Hubble expansion provides a spatial EFE
- He does suggest the cosmological constant connection may be fundamental
- None of his papers derive x_bar ~ cH_0/a_0 from a field-theoretic action
- References: https://arxiv.org/abs/1404.7661, https://academic.oup.com/mnras/article/403/2/886/1184577

### 8.5 Halle & Zhao (2008)

"Around MOND: Lagrangians, Hubble Equations, Perturbations and External Field Effect" (arXiv:0710.3898):
- Explored MOND-type Lagrangians in cosmological context
- Discussed perturbation equations in modified gravity
- Highlighted the tension between MOND's nonlinearity and standard cosmological perturbation theory
- Reference: https://arxiv.org/abs/0710.3898

### 8.6 Skordis & Zlosnik (2021)

The relativistic MOND theory that reproduces the CMB and LSS:
- Uses a vector field (not just scalar modifications) to achieve correct cosmological behavior
- The mechanism for obtaining correct structure formation is fundamentally different from a simple EFE
- Demonstrates that reproducing LCDM-like cosmology requires additional dynamical fields
- This is the closest successful example to what DFD needs

### 8.7 Summary of literature

**No paper in the MOND literature derives a cosmological EFE from the isotropic Hubble flow acting through the standard AQUAL spatial gradient mechanism.** The idea that cH_0 provides an external field for cosmological perturbations is a DFD-specific claim that has no precedent in the standard MOND literature.

---

## 9. DEFINITIVE ANSWER: GALACTIC vs COSMOLOGICAL EFE

### 9.1 The galactic EFE

| Property | Galactic EFE |
|----------|-------------|
| Mechanism | Spatial gradient of external potential |
| Source | Nearby massive structures (cluster, neighbor galaxy) |
| Direction | Breaks isotropy (preferred direction of g_ext) |
| How mu is set | mu(|nabla psi_int + g_ext| / a_0) |
| Background | nabla psi_ext != 0 |
| Composition | mu(psi_total) = 1 - (1-mu(psi_ext))(1-mu(psi_int)) |
| Status | Well-derived from AQUAL action |

### 9.2 The claimed cosmological EFE

| Property | Cosmological "EFE" (v3.3 claim) |
|----------|-------------------------------|
| Mechanism | Temporal evolution rate of Hubble flow |
| Source | Cosmic expansion |
| Direction | Isotropic (no preferred direction) |
| How mu is set | mu(cH_0/a_0) (??) |
| Background | nabla psi_bar = 0 exactly |
| Composition | Cannot derive mu_0 ~ 0.85 from the action |
| Status | **Unproven assertion by analogy** |

### 9.3 The fundamental differences

1. **Gradient vs rate:** The galactic EFE uses nabla psi (spatial); the cosmological claim uses psi_dot (temporal). These are different sectors of the DFD action.

2. **Anisotropy vs isotropy:** The galactic EFE breaks spatial isotropy (g_ext picks a direction). The Hubble flow preserves isotropy (no preferred direction).

3. **Background vs deviation:** The galactic EFE provides a nonzero BACKGROUND field. The temporal sector's deviation invariant is zero for the background by construction.

4. **Derived vs asserted:** The galactic EFE follows rigorously from the AQUAL action. The cosmological "EFE" is claimed but not derived from the DFD action.

5. **Composition law applicability:** The galactic EFE uses mu composition for the same sector (spatial-spatial). The cosmological claim requires cross-sector composition (temporal providing effective spatial mu), which is not straightforwardly the same.

---

## 10. IMPLICATIONS FOR DFD

### 10.1 The gap

The v3.3 paper has a logical gap between:
- The DFD action (which gives Delta_bar = 0)
- The claimed result (x_bar ~ 5.85 providing mu_0 ~ 0.854)

This gap must be filled by either:
1. A new derivation showing how the temporal sector effectively provides a spatial-like EFE
2. A modification of the screen-background definition
3. A mode-coupling argument for effective x_bar in the nonlinear regime
4. An entirely new mechanism

### 10.2 What would work

The most promising approach is **(a) from Section 7.4**: redefine psi_dot_0 so that Delta_bar != 0. If psi_dot_0 is defined as the rate in the "screen Minkowski vacuum" rather than in the FRW background, then:

    Delta_bar = (c/a_0)|psi_bar_dot - psi_dot_0^{Mink}| != 0

The Hubble flow's characteristic rate would give Delta_bar ~ cH_0/a_0 ~ 5.85, which is exactly what the paper claims. But this requires an explicit derivation showing:
1. Why psi_dot_0 should be the Minkowski value, not the FRW value
2. How this choice is consistent with the screen-background formalism
3. What the physical interpretation of this "vacuum reference" is

### 10.3 The deeper question

Even if the cosmological EFE can be derived, it operates through a DIFFERENT mechanism than the galactic EFE. The paper's language (calling both "EFE") is misleading. What DFD actually has is:

- **Galactic EFE:** Standard AQUAL mechanism via spatial gradients (well-defined)
- **Cosmological regularization:** Temporal sector providing a floor on mu through the Hubble rate (needs derivation)

These should be presented as distinct phenomena with distinct mechanisms, not as the same "External Field Effect" operating at different scales.

---

## 11. CONCLUSIONS

1. **Question 1 (spatial gradient argument):** CORRECT. nabla psi_bar = 0 in FRW. The galactic EFE mechanism does not apply.

2. **Question 2 (temporal psi_dot as EFE):** Delta_bar = 0 by construction. The temporal sector does NOT provide a nonzero background mu through the stated formalism.

3. **Question 3 (perturbation contributions):** Both mu_s and mu_t are ~10^{-4} for linear perturbations. The temporal sector adds ~50-77% to the perturbation-level mu but does not change the deep-MOND character.

4. **Question 4 (mu_t/mu_s ratio):** The ratio is 2Hf/(ck), independent of delta. The spatial sector dominates for all k > 0.001 h/Mpc. The crossover is at the Hubble scale.

5. **Question 5 (does this change the picture?):** No. The temporal sector is a sub-leading correction at all sigma_8-relevant scales. It does NOT provide the large mu_0 ~ 0.85 that the paper claims.

6. **Literature:** No MOND paper derives a cosmological EFE from the isotropic Hubble flow through the spatial gradient mechanism. The v3.3 claim is unprecedented and unproven.

**The cosmological "EFE" in v3.3 is a promissory note, not a derived result. It operates through a fundamentally different mechanism than the galactic EFE, and the derivation showing how it arises from the DFD action has not been provided.**
