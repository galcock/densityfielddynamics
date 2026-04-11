# Agent 17: DFD v3.3 Paper -- Complete Mathematical Extraction for P(k) Closure

**Source:** Density Field Dynamics: A Complete Unified Theory v3.3
**Date:** 2026-04-04
**Scope:** All equations, theorems, assumptions, notation, and open problems relevant to P(k), growth, G_eff, perturbation theory, and the dust branch.

---

## TABLE OF CONTENTS

1. [Core DFD Formalism (Section 2)](#1-core-dfd-formalism)
2. [Galactic Dynamics and mu-Function (Section 7)](#2-galactic-dynamics-and-mu-function)
3. [Cosmology Section (Section 12)](#3-cosmology-section)
4. [P(k) Confrontation (Section 12 subsection)](#4-pk-confrontation)
5. [Appendix N: mu Derivation](#5-appendix-n-mu-derivation)
6. [Appendix Q: Temporal Completion / Dust Branch](#6-appendix-q-temporal-completion)
7. [Open Problems (Section 14)](#7-open-problems)
8. [Notation Dictionary](#8-notation-dictionary)
9. [Theorem/Assumption Dependency Map](#9-theorem-assumption-dependency-map)
10. [Identified Gaps for P(k) Closure](#10-identified-gaps-for-pk-closure)

---

## 1. Core DFD Formalism

### 1.1 Fundamental Fields and Metric

The DFD scalar field psi defines the optical metric on flat Minkowski spacetime:

```
d~s^2 = -c^2 dt^2 / n^2(x,t) + dx^2,    n(x,t) = e^{psi(x,t)}
```

**Acceleration of matter** (non-relativistic):
```
a = (c^2 / 2) nabla(psi)
```

**One-way phase velocity:**
```
c_phase = c / n = c e^{-psi}
```

### 1.2 Action Principle

**Quasi-static spatial sector:**
```
S_psi = int dt d^3x { (a_*^2 / 8pi G) W(|nabla psi|^2 / a_*^2) - (c^2/2) psi (rho - rho_bar) }
```

Where:
- W(y) is a dimensionless convex kinetic potential with W(0)=0, W'(0)=1
- a_* is the characteristic gradient scale, [a_*] = 1/m
- Relation to MOND scale: a_* = 2 a_0 / c^2
- a_0 = 2 sqrt(alpha) c H_0 ~ 1.2 x 10^{-10} m/s^2
- y = |nabla psi|^2 / a_*^2 is dimensionless

**Full dynamic action (spatial + temporal):**
```
S_psi = int dt d^3x { (a_*^2 / 8pi G) [ W(|nabla psi|^2 / a_*^2) + K( (c/a_0)|dot{psi} - dot{psi}_0| ) ] - (c^2/2) psi (rho - rho_bar) }
```

Where K is the temporal kinetic function with K'(Delta) = mu(Delta).

**Complete DFD action:**
```
S_DFD = S_psi + S_h + S_int + S_matter
```

- S_h = (c^4 / 32pi G) int dt d^3x [ (1/c^2)(d_t h_ij^TT)^2 - (nabla h_ij^TT)^2 ]
- GW propagation speed c_T = c (consistent with GW170817)

### 1.3 Field Equation

**General nonlinear form (Eq. 2.16 equivalent):**
```
nabla . [ mu(|nabla psi| / a_*) nabla psi ] = -(8 pi G / c^2)(rho - rho_bar)
```

Where the response function:
```
mu(x) = W'(x^2) + 2 x^2 W''(x^2),    x = |nabla psi| / a_*
```

**Acceleration form (master equation):**
```
nabla . a + (k_a / c^2) a^2 = -4 pi G rho
```

Where k_a = 3 / (8 alpha) ~ 51.4

### 1.4 The mu-Function

**Canonical (derived) form:**
```
mu(x) = x / (1 + x)
```

This is the "Simple" form, uniquely derived from S^3 microsector (Theorem ref:thm:mu-theorem).

**Physical constraints on any admissible mu:**
1. Solar limit: mu(x) -> 1 as x -> infinity
2. Deep-field limit: mu(x) ~ x as x -> 0
3. Monotonicity: mu'(x) > 0 for x > 0
4. Convexity: associated W must be convex

**Key property for clusters:** Psi(x) = 1/mu(x) = (1+x)/x is convex for x > 0 (used in Jensen-type arguments).

### 1.5 Conserved Quantities

Stress-energy conservation: tilde{nabla}_mu tilde{T}^{mu nu} = 0

Static energy functional:
```
E[psi] = int d^3x [ (a_*^2 / 8pi G) W(|nabla psi|^2 / a_*^2) + (c^2/2) rho psi ]
```

Minimized by field equation solutions (convexity of W guarantees unique minimizer).

---

## 2. Galactic Dynamics and mu-Function

### 2.1 Deep-Field Limit

When x = |nabla psi| / a_* << 1, mu(x) -> x. The field equation becomes:
```
nabla . [ (|nabla psi| / a_*) nabla psi ] = -(8pi G / c^2) rho
```

For spherical symmetry with enclosed mass M:
```
|psi'| = sqrt(2 G M a_* / (c^2 r^2))
```

This gives a logarithmic potential and flat rotation curves:
```
v_c = (G M a_* c^2 / 2)^{1/4} = const    (flat rotation curve)
```

### 2.2 Baryonic Tully-Fisher Relation

```
M_bar = v_f^4 / (G a_0)
```

Where a_0 = a_* c^2 / 2. This is a parameter-free prediction with slope exactly 4.

### 2.3 Radial Acceleration Relation

The exact DFD RAR with mu(x) = x/(1+x):
```
g_obs = [ g_bar + sqrt(g_bar^2 + 4 g_bar a_0) ] / 2
```

**KEY NOTATION:**
- g_obs = v_c^2 / r  (observed centripetal acceleration)
- g_bar = G M_bar(<r) / r^2  (Newtonian baryonic acceleration)
- a_0 = 1.2 x 10^{-10} m/s^2  (calibrated from SPARC RAR, then frozen)

### 2.4 Calibration

Single theory calibration: a_0 = (1.20 +/- 0.02_stat +/- 0.24_sys) x 10^{-10} m/s^2 from SPARC RAR fit. Frozen for all subsequent predictions.

---

## 3. Cosmology Section

### 3.1 psi-Screen Framework

**Core definition:**
```
Delta psi(z, n_hat) = psi_em(z, n_hat) - psi_obs
```

Gauge choice: psi_obs = 0, so Delta psi = psi_em.

### 3.2 Three Primary Optical Relations

**(1) Luminosity-distance bias (SNe Ia):**
```
D_L^DFD(z, n_hat) = D_L^dict(z, n_hat) exp(Delta psi(z, n_hat))
```

**(1b) Angular-diameter-distance bias:**
```
D_A^DFD(z, n_hat) = D_A^dict(z, n_hat) exp(Delta psi(z, n_hat))
```

**(2) Distance duality (Etherington reciprocity):**
```
D_L(z, n_hat) = (1+z)^2 D_A(z, n_hat)
```

Holds exactly. No e^{Delta psi} factor appears (common screening cancels).

**(3) CMB acoustic-scale screen:**
```
ell_1(n_hat) = ell_true exp(-Delta psi(n_hat))
```

### 3.3 Screen Estimators

**Estimator A (SNe alone):**
```
hat{Delta psi}_SN(z_i, n_hat_i) = ln D_L^obs(z_i, n_hat_i) - ln D_L^dict(z_i) - M
```

**Estimator B (duality consistency check):**
```
hat{Delta psi}_dual(z, n_hat) = ln[ D_L^obs / ((1+z)^2 D_A^obs) ] = 0
```

**Estimator C (CMB peak anisotropy):**
```
hat{Delta psi}_CMB(n_hat) = -ln( ell_1(n_hat) / <ell_1> )
```

### 3.4 Closure Theorems

**Theorem (Duality consistency):** Under (H1)-(H2), hat{Delta psi}_dual = 0.

**Theorem (SN inversion):** Under (H1)-(H3), hat{Delta psi}_SN = Delta psi - M, and the centered field equals true screen anisotropy.

**Corollary (Harmonic closure):** a_{lm}^SN(z_*) = a_{lm}^CMB for all l >= 1.

### 3.5 Effective Gravity (G_eff) -- CRITICAL FOR P(k)

**Linear growth equation:**
```
ddot{delta} + 2H dot{delta} = 4 pi G_eff(a_sc, k) rho_bar delta
```

**G_eff in quasi-static limit:**
```
G_eff(a_sc, k) = G / mu(x)
```

**IMPORTANT clarification:** G_eff is an effective response factor (rescaling by 1/mu), not a claim that fundamental G varies.

### 3.6 Acceleration Scales

```
a_* = c H_0                           (cosmological scale)
a_0 = 2 sqrt(alpha) a_*               (galactic crossover scale)
```

### 3.7 Background mu Parameterization

```
mu_bg(a_sc) = 1 + eta_1 (1 - a_sc) + eta_2 (1 - a_sc)^2
```

With prior: mu_bg -> 1 for a_sc <= 0.5 (z >= 1).

### 3.8 Controlled psi-Regime Test Knobs

```
delta ln c_1     = gamma_c   Delta psi
delta ln G_eff   = gamma_G   Delta psi
delta ln a_*     = gamma_*   Delta psi
delta ln alpha   = gamma_alpha Delta psi
```

In strict DFD: gamma_c = -1. Other gammas are controlled falsification tests.

### 3.9 Growth Rate

**DFD growth rate:**
```
f_DFD(z) = Omega_m(z)^gamma [ 1 + O(k_alpha) ]
```

Where gamma ~ 0.55 and the psi-field correction O(k_alpha) ~ 10^{-5}, far below current measurement precision.

**KEY RESULT:** DFD and LCDM predict indistinguishable linear growth at current multipole precision.

### 3.10 psi-Screen Reconstruction

**H_0-independent reconstruction:**
```
Delta psi(z) = ln( D_L^obs(z) / D_L^matter(z) ) = ln( D_L^LCDM(z) / D_L^matter(z) )
```

**Key result:** Delta psi(z=1.0) = 0.274 +/- 0.02

### 3.11 CMB Peak Ratio

**Asymmetry factor decomposition:**
```
A = f_baryon x f_ISW x f_vis x f_Dop = 0.474 x 0.50 x 0.98 x 0.90 = 0.209
```

**Peak ratio:**
```
R = ((1+A)/(1-A))^2 = (1.209/0.791)^2 = 2.34
```

Observed (Planck): R ~ 2.4. Agreement: 2.5%.

### 3.12 Forward Perturbation Skeleton -- CRITICAL FOR P(k)

**Linearized DFD field equation in Fourier space:**
```
k_i M_ij k_j delta psi_k = -(8 pi G / c^2) rho_bar delta_k
```

**Response tensor:**
```
M_ij = mu_0 delta_ij + L_0 hat{g}_i hat{g}_j
```

Where:
- mu_0 = mu(x_bar)
- L_0 = (d mu / d ln x)|_{x_bar}
- hat{g} = nabla psi_bar / |nabla psi_bar|

**Linear growth equation:**
```
ddot{delta}_k + 2H dot{delta}_k = 4 pi G_eff(a, hat{k}) rho_bar delta_k
```

**Direction-dependent effective gravitational coupling (BOXED in paper):**
```
G_eff(a, hat{k}) = G / { mu_0 [ 1 + L_0 (hat{k} . hat{g})^2 ] }
```

**For mu(x) = x/(1+x):**
- mu_0 = x_bar / (1 + x_bar)
- L_0 = 1 / (1 + x_bar)^2

**Regime behavior:**
- Cosmological scales (x_bar << 1): G_eff -> G / x_bar  (enhanced growth)
- Small scales (x_bar >> 1): G_eff -> G  (standard gravity recovered)

### 3.13 Connection to Reconstructed Screen

```
Delta psi_screen(z, n_hat) = int_0^{chi(z)} W(chi') delta psi(chi' n_hat) d chi'
```

Where W(chi) is the lensing kernel. The SAME delta psi field drives both forward growth and inverse screen reconstruction.

### 3.14 N-body Proof-of-Concept

64^3 grid, 200 Mpc/h box:
- LCDM (Omega_m = 0.30): baseline
- Newtonian-baryons (Omega_b = 0.049): delta_rms = 1.5 x 10^{-4} (negligible structure)
- DFD-baryons (Omega_b = 0.049, mu = x/(1+x)): delta_rms = 6.4 x 10^{-3} (43.8x more than Newtonian)

The 5.4x overshoot relative to LCDM is expected: cosmological perturbation accelerations (x ~ 4 x 10^{-4}) lie deep in MOND regime where raw mu-function enhances gravity by ~400x without cosmological EFE. With EFE from Hubble flow (a_ext ~ c H_0 ~ 6 a_0), effective enhancement drops from ~400 to ~1.2.

### 3.15 ISW Prediction

DFD predicts ISW amplitude suppressed to ~30% of LCDM:
- LCDM: ISW from Lambda-induced potential decay at z < 2
- DFD: ISW from mu-evolution (much slower)

Falsification: If CMB x galaxy cross-correlation yields > 4 sigma ISW detection, DFD is falsified.

### 3.16 Effective Equation of State (Dictionary Translation)

```
w_eff(z) ~ -1 - (1/3) d(Delta psi) / d ln(1+z)
```

Not fundamental in DFD; merely a reporting-layer translation.

---

## 4. P(k) Confrontation

### 4.1 Method

Anisotropic galaxy power spectrum P(k, mu_angle) encodes RSD through Kaiser formula. Legendre multipoles:
```
P_l(k) = (2l+1)/2 int_{-1}^{1} P(k, mu_angle) L_l(mu_angle) d mu_angle
```

Quadrupole-to-monopole ratio in linear theory:
```
P_2/P_0 = [ (4/3) beta + (4/7) beta^2 ] / [ 1 + (2/3) beta + (1/5) beta^2 ]
```

Where beta = f/b (growth rate / galaxy bias).

### 4.2 Results

| Sample | z_eff | beta_meas | beta_theory |
|--------|-------|-----------|-------------|
| BOSS DR12 z_1 | 0.38 | 0.270 +/- 0.009 | 0.357 |
| BOSS DR12 z_3 | 0.61 | 0.281 +/- 0.007 | 0.395 |
| eBOSS DR16 QSO | 1.50 | 0.366 +/- 0.013 | 0.404 |

Measured beta values lie 10-25% below theory prediction. Deficit largest at lower redshift, smallest at higher redshift.

### 4.3 Key Conclusions

1. DFD growth rate: f_DFD(z) = Omega_m(z)^gamma [1 + O(k_alpha)] where gamma ~ 0.55 and O(k_alpha) ~ 10^{-5}
2. **DFD and LCDM predict indistinguishable linear growth** at current multipole precision
3. The 10-25% deficit arises from: FoG damping, galaxy bias uncertainty (~10%), mock calibration systematics
4. DFD distinctive signatures appear in strong-field regimes, not linear-regime RSD

**STATUS (verbatim from paper):** "Consistency check completed at the level of linear multipole data products. DFD is consistent with the quoted BOSS DR12 and eBOSS DR16 multipole measurements within the stated systematic uncertainties. This should be read as an initial data-level consistency check, not as a claim that the full production-level P(k)/Boltzmann pipeline is already closed."

---

## 5. Appendix N: mu Derivation

### 5.1 Assumptions (Complete List)

**Assumption N.1 (Microsector multiplicative weight defines e^psi):**
```
e^{psi(s)} := Z_{S^3}(k_0) / Z_{S^3}(k_eff(s))
```

**Assumption N.2 (Minimal weak-field level response):**
```
k_eff(s) = k_0 (1 + s),    k_0 >> 1
```

**Assumption N.3 (Saturation-union composition law):**
```
mu(psi_1 + psi_2) = 1 - (1 - mu(psi_1))(1 - mu(psi_2))
mu(0) = 0,    0 <= mu < 1
```

**Assumption N.4 (Newtonian limit fixes slope):**
```
mu(s) = s + O(s^2) as s -> 0
```

### 5.2 Derived Results

**Lemma (S^3 partition function):**
```
Z_{S^3}(k) = sqrt(2/(k+2)) sin(pi/(k+2))
log Z_{S^3}(k) = const - (3/2) log(k+2) + O(k^{-2})
```

The exponent 3/2 = dim(S^3)/2 is topologically fixed.

**Proposition (psi scaling):**
```
psi(s) = (3/2) log(1+s) + O(k_0^{-1})
```

**Lemma (Composition implies exponential):**
Under saturation-union + continuity: mu(psi) = 1 - e^{-c psi} for some c > 0.

**Theorem (mu-theorem, the KEY result):**
Under Assumptions N.1-N.4:
```
mu(s) = s / (1 + s) + O(k_0^{-1})
```

**Proof chain:** c = 2/3 is forced by requiring mu(s) = s + O(s^2) combined with psi = (3/2) log(1+s).

### 5.3 Acceleration Scale Derivation

**Scaling charge:** q_{S^3} = 3/2

**Spacetime functional:**
```
S[psi] = int d^3x [ Xi(x) - q_{S^3} log Xi(x) ],    q_{S^3} = 3/2
```

Where Xi(x) = k_a (|a|/(cH_0))^2 = beta |nabla psi|^2, beta = k_a c^2 / (4 H_0^2).

**Theorem (Scaling stationarity):**
```
Xi_* = q_{S^3} = 3/2
```

**Theorem (MOND scale):**
```
a_* = 2 sqrt(alpha) c H_0 ~ 1.20 x 10^{-10} m/s^2
```

Numerical: a_* = 1.197 x 10^{-10} vs observed a_0 = (1.20 +/- 0.26) x 10^{-10}. Agreement: 0.3%.

### 5.4 Alternative Variational mu

A variational approach gives a different but functionally equivalent mu:
```
mu(u) = [1 + 2u - sqrt(1 + 4u)] / (2u)
```

Same asymptotics as x/(1+x): mu ~ u for u << 1, mu -> 1 for u >> 1. Observationally indistinguishable at current precision.

---

## 6. Appendix Q: Temporal Completion / Dust Branch

### 6.1 Temporal Deviation Invariance

**Theorem (Temporal deviation invariance):**
From saturation-union composition:
```
mu(psi_0 + Delta psi) - mu(psi_0) = (1 - mu(psi_0)) mu(Delta psi)
```

Equivalently: the normalized incremental response depends only on the deviation:
```
[mu(psi_0 + Delta psi) - mu(psi_0)] / [1 - mu(psi_0)] = mu(Delta psi)
```

### 6.2 Unique Temporal Invariant

**Definition (Local temporal increment density):**
```
dot{psi} := u^mu nabla_mu psi
dot{psi}_0 := u^mu nabla_mu psi_0
Delta := (c / a_0) |dot{psi} - dot{psi}_0|
```

Where a_0 = 2 sqrt(alpha) c H_0. The combination c/a_0 has units of time, so Delta is dimensionless.

**Theorem (Temporal segment identification):**
Delta is the UNIQUE choice (up to constant factor) satisfying:
1. Reparameterization covariance
2. Segment additivity
3. Reference invariance (vanishes when psi = psi_0)

### 6.3 No-Go Lemma -- CRITICAL

**Lemma (No-go: quadratic invariant):**
Define Q_t := (u^mu nabla_mu psi)^2 and suppose K'(Q_t) = mu(sqrt(Q_t)) = sqrt(Q_t)/(1 + sqrt(Q_t)).

Then:
```
K(Q_t) = (2/3) Q_t^{3/2} + O(Q_t^2)
w := p/rho -> 1/2    (Q_t -> 0)
```

This is NOT dust. The quadratic identification gives radiation-like equation of state.

### 6.4 Dust Branch Theorem -- THE KEY COSMOLOGICAL RESULT

**Temporal Lagrangian (deviation-invariant closure):**
```
L_temp = (a_*^2 / 8pi G) K(Delta),    K'(Delta) = mu(Delta) = Delta / (1 + Delta)
```

**Lemma (Shift symmetry current):**
```
nabla_mu J^mu = 0,    J^mu = (a_*^2 / 8pi G) K'(Delta) (c/a_*) sgn(dot{psi} - dot{psi}_0) u^mu
```

**Theorem (Dust branch):**
In homogeneous FRW:
```
a^3 mu(Delta) = const
Delta ~ a^{-3}    (for Delta << 1)
```

And:
```
w := p/rho -> 0        as Delta -> 0
c_s^2 -> 0             as Delta -> 0
```

**Proof sketch:**
- From shift current conservation: a^3 K'(Delta) = const
- K'(Delta) = mu(Delta), so a^3 mu(Delta) = const
- For Delta << 1: mu(Delta) ~ Delta, so Delta ~ a^{-3}
- Near Delta = 0: K(Delta) ~ (1/2) Delta^2, so p ~ (1/2) Delta^2
- rho ~ (c/a_*) dot{psi}_0 Delta (linear in Delta)
- Therefore w = p/rho = O(Delta) -> 0
- c_s^2 = dp/d rho -> 0

### 6.5 Summary of Theorem-Grade vs Program

**THEOREM-GRADE (proved from S^3 composition + deviation invariance):**
1. Temporal deviation invariance
2. Unique temporal segment scalar Delta = (c/a_0)|dot{psi} - dot{psi}_0|
3. K'(Delta) = mu(Delta) closure (same mu as spatial sector)
4. Dust branch: w -> 0, c_s^2 -> 0 as Delta -> 0
5. No-go: Quadratic K'(Q_t) = mu(sqrt(Q_t)) gives w -> 1/2

**PROGRAM-LEVEL (not claimed as theorem):**
- Full P(k) shape matching LCDM (linear perturbation analysis)
- Transfer function derivation in DFD dictionary
- Quantitative confrontation with survey data (GR-sandbox / fiducial-processing issues)

**The dust branch (w -> 0, c_s^2 -> 0) is the NECESSARY CONDITION for CDM-like linear growth; proving the full P(k) match is a program item.**

---

## 7. Open Problems

### 7.1 Claim Status Levels

- **T0:** Theorem from core DFD postulates (exact RAR inversion for mu(x)=x/(1+x))
- **T1:** Theorem from enlarged frontier-axiom system (G_eff growth law, perturbation operator, etc.)
- **E:** Empirical benchmark
- **F:** Open program item

### 7.2 P(k)-Relevant Open Problems

From the summary table (Table 14.1):

| Problem | Status | Resolution |
|---------|--------|------------|
| P(k) full match | **Program** | Dust branch proved (Thm dust-branch); numerical pipeline in development |
| Boltzmann code | Addressed | Not needed (GR tool) |
| Dust branch (w->0) | **Theorem** | K'(Delta) = mu(Delta) |

### 7.3 Hyperbolicity Status

- **Elliptic** in static limit (well-posed BVP)
- **Hyperbolic** for small perturbations about smooth backgrounds
- **Uncertain** for fully nonlinear dynamical evolution

Perturbation metric satisfies hyperbolicity conditions for constrained mu-family.

### 7.4 Paper's Explicit Framing of What Remains

(Verbatim from Appendix Q tcolorbox "Program-Level"):
- Full P(k) shape matching LCDM (linear perturbation analysis)
- Transfer function derivation in DFD dictionary
- Quantitative confrontation with survey data (noting GR-sandbox / fiducial-processing issues)

(Verbatim from Section 12):
"A full transfer-function / survey-pipeline confrontation remains a program item. Published P(k) data are processed through GR-based fiducial cosmologies (the 'GR sandbox'), so direct confrontation requires dictionary translation plus a forward DFD perturbation solver."

---

## 8. Notation Dictionary

| Symbol | Definition | Units/Type |
|--------|-----------|------------|
| psi | DFD scalar field | dimensionless |
| n = e^psi | refractive index | dimensionless |
| a = (c^2/2) nabla psi | acceleration field | m/s^2 |
| a_* | characteristic gradient scale = 2 a_0 / c^2 | 1/m |
| a_0 | MOND acceleration = 2 sqrt(alpha) c H_0 | m/s^2 |
| a_star (cosmological) | c H_0 | m/s^2 |
| alpha | fine-structure constant = 1/137.036 | dimensionless |
| mu(x) | response/crossover function | dimensionless |
| x | = \|nabla psi\| / a_* | dimensionless |
| W(y) | kinetic potential, y = x^2 | dimensionless |
| K(Delta) | temporal kinetic function | dimensionless |
| Delta | = (c/a_0)\|dot{psi} - dot{psi}_0\| | dimensionless |
| Delta psi | psi-screen: psi_em - psi_obs | dimensionless |
| k_a | = 3/(8 alpha) ~ 51.4 | dimensionless |
| Xi | = k_a (\|a\|/(cH_0))^2 | dimensionless |
| Xi_* | = 3/2 (crossover invariant) | dimensionless |
| q_{S^3} | = 3/2 (scaling charge from S^3) | dimensionless |
| G_eff | = G / mu(x) in quasi-static limit | m^3/(kg s^2) |
| mu_0 | = mu(x_bar) at background | dimensionless |
| L_0 | = (d mu / d ln x)\|_{x_bar} | dimensionless |
| hat{g} | = nabla psi_bar / \|nabla psi_bar\| | unit vector |
| M_ij | = mu_0 delta_ij + L_0 hat{g}_i hat{g}_j | response tensor |
| beta | = f/b (growth rate / galaxy bias) | dimensionless |
| f | = d ln delta / d ln a | dimensionless |
| gamma | growth index ~ 0.55 | dimensionless |
| k_alpha | = alpha^2 / (2 pi) | dimensionless |
| rho_bar | mean cosmic density | kg/m^3 |

---

## 9. Theorem/Assumption Dependency Map

```
Assumption N.1 (psi from Z)
Assumption N.2 (level response)     --> Proposition (psi = 3/2 log(1+s))
Assumption N.3 (saturation-union)   --> Lemma (composition => exponential)
Assumption N.4 (Newtonian slope)    --> THEOREM: mu(s) = s/(1+s)  [Thm mu-theorem]

Lemma (S^3 partition function)
  + k_a = 3/(8 alpha)               --> Xi_* = 3/2  [Thm Xi-mean]
                                     --> a_* = 2 sqrt(alpha) c H_0  [Thm a-star-final]

Assumption N.3 (saturation-union)    --> Temporal deviation invariance  [Thm temporal-deviation-Q]
  + Segment additivity               --> Unique Delta = (c/a_0)|dot{psi} - dot{psi}_0|  [Thm segment-id]
  + K'(Delta) = mu(Delta)            --> DUST BRANCH: w -> 0, c_s^2 -> 0  [Thm dust-branch]
                                     --> NO-GO: quadratic gives w -> 1/2  [Lemma no-go-quadratic]

Dust branch  [Thm dust-branch]
  + Linearized field equation        --> Response tensor M_ij
  + Background history H(a)          --> G_eff(a, hat{k}) = G / {mu_0 [1 + L_0 (hat{k}.hat{g})^2]}
                                     --> Linear growth equation

Forward growth law
  + Screen reconstruction            --> Forward-inverse closure (falsifiable)
```

---

## 10. Identified Gaps for P(k) Closure

### 10.1 What IS Proved (Theorem-Grade)

1. mu(x) = x/(1+x) is uniquely determined
2. a_0 = 2 sqrt(alpha) c H_0 is derived
3. Dust branch: w -> 0, c_s^2 -> 0 (necessary condition for CDM-like growth)
4. No-go for quadratic temporal invariant (w -> 1/2)
5. Linear growth equation with direction-dependent G_eff
6. G_eff = G / {mu_0 [1 + L_0 (hat{k}.hat{g})^2]}
7. DFD and LCDM predict indistinguishable linear growth rate f(z) at current precision

### 10.2 What is NOT Proved (Program Items)

1. **Full P(k) shape:** The dust branch gives the right equation of state but the actual P(k) shape has not been computed end-to-end
2. **Transfer function:** No DFD-native transfer function exists yet
3. **Initial conditions / primordial spectrum:** Paper does not derive the primordial power spectrum within DFD
4. **Baryon acoustic oscillations:** BAO feature in P(k) not derived in DFD framework
5. **Survey pipeline confrontation:** Published P(k) data processed through GR-based fiducial cosmologies; need dictionary translation
6. **Cosmological EFE implementation:** The N-body proof-of-concept shows 5.4x overshoot without EFE; with EFE (a_ext ~ 6 a_0), enhancement drops to ~1.2 -- but this is not implemented in a production solver
7. **Nonlinear P(k):** Only linear perturbation theory is developed
8. **Anisotropy of G_eff:** The direction-dependent G_eff from hat{k}.hat{g} coupling is a distinctive DFD prediction but its observational consequences for P(k) multipoles have not been fully worked out

### 10.3 Critical Path for P(k) Closure

Based on the paper's own identification, the following chain must be completed:

1. **Background:** Supply H(a) from DFD observer dictionary (already done implicitly)
2. **Linear perturbations:** Solve the growth equation with G_eff(a, hat{k}) -- the mathematical framework exists in Eqs. (perturb-fourier)-(G-eff)
3. **Evaluate x_bar(a):** Determine the background field gradient as a function of scale factor -- this requires knowing what sets x_bar on cosmological scales
4. **Transfer function:** Compute T(k) accounting for radiation-matter transition, baryon loading, and Silk damping -- all within DFD dictionary
5. **EFE on cosmological scales:** Implement External Field Effect from Hubble flow (a_ext ~ c H_0 ~ 6 a_0) to regulate the otherwise excessive mu-enhancement
6. **P(k) shape comparison:** Compare DFD P(k) against observed power spectrum shape (BOSS/eBOSS/DESI)

### 10.4 Key Physical Questions

1. **What sets x_bar on cosmological scales?** The perturbation accelerations give x ~ 4 x 10^{-4}, deep in MOND regime. The cosmological EFE from Hubble flow (a_ext ~ c H_0 ~ 6 a_0) is crucial -- how exactly does this enter the perturbation equations?

2. **Is G_eff isotropic on average?** The direction-dependent G_eff involves hat{k}.hat{g}. If the background gradient hat{g} has no preferred direction on cosmological scales (homogeneity), the angular average of G_eff might reduce to an isotropic expression. This needs to be worked out.

3. **What replaces CDM in the Boltzmann hierarchy?** Standard Boltzmann codes have CDM as a separate species. In DFD, the dust branch of the psi-field plays this role, but the coupling to baryons and radiation through the psi-field (rather than through metric perturbations) needs to be spelled out.

4. **Acoustic oscillations without CDM:** In LCDM, CDM provides the gravitational wells for baryon infall. In DFD, the psi-field's dust branch should provide equivalent wells. But does the coupling structure allow the same BAO physics?

5. **Silk damping and diffusion:** These depend on the photon-baryon coupling, which should be unchanged. But the gravitational driving term changes from Phi (metric) to psi (scalar), which may modify the effective Jeans scale.

---

## APPENDIX: Key Equations Quick Reference for Other Agents

### The Essential Five Equations for P(k)

**(E1) Field equation:**
nabla . [mu(|nabla psi|/a_*) nabla psi] = -(8pi G/c^2)(rho - rho_bar)

**(E2) mu-function:**
mu(x) = x/(1+x)

**(E3) Growth equation:**
ddot{delta}_k + 2H dot{delta}_k = 4pi G_eff(a, hat{k}) rho_bar delta_k

**(E4) G_eff:**
G_eff(a, hat{k}) = G / { mu_0 [1 + L_0 (hat{k}.hat{g})^2] }

**(E5) Dust branch:**
w -> 0, c_s^2 -> 0 (from K'(Delta) = mu(Delta) with Delta = (c/a_0)|dot{psi} - dot{psi}_0|)

### Numerical Constants

- alpha = 1/137.036
- a_0 = 1.20 x 10^{-10} m/s^2
- a_* (cosmological) = c H_0 ~ 7 x 10^{-10} m/s^2
- k_a = 3/(8 alpha) ~ 51.4
- Xi_* = 3/2
- gamma (growth index) ~ 0.55
- k_alpha = alpha^2/(2pi) ~ 8.5 x 10^{-6}

---

*End of Agent 17 extraction. This document is the foundational reference for all P(k) closure work.*
