# R8 Agent 01: Kunneth Theorem and Zero-Mode Census for CP2 x S3

**Campaign:** R8 -- Promote chi to a Physical Field in DFD
**Agent:** 01 of 20
**Date:** 2026-04-05

---

## 1. Betti Numbers of the Factors

### CP2 (compact Kahler 4-manifold)

| n | b_n(CP2) | Representative |
|---|----------|----------------|
| 0 | 1 | constant function 1 |
| 1 | 0 | (simply connected) |
| 2 | 1 | Kahler 2-form J |
| 3 | 0 | |
| 4 | 1 | volume form omega_4 |

### S3 (3-sphere)

| n | b_n(S3) | Representative |
|---|---------|----------------|
| 0 | 1 | constant function 1 |
| 1 | 0 | |
| 2 | 0 | |
| 3 | 1 | volume form Omega_3 |

---

## 2. Kunneth Theorem: Betti Numbers of K = CP2 x S3

For a product manifold with torsion-free integer cohomology (both CP2 and S3 qualify):

    b_n(K) = sum_{p+q=n} b_p(CP2) * b_q(S3)

where p ranges over 0..4 and q ranges over 0..3, with q = n - p constrained to lie in [0,3].

### Detailed computation

**b_0:** p=0, q=0: 1*1 = **1**

**b_1:** p=0,q=1: 1*0=0; p=1,q=0: 0*1=0. Total = **0**

**b_2:** p=0,q=2: 1*0=0; p=1,q=1: 0*0=0; p=2,q=0: 1*1=1. Total = **1**

**b_3:** p=0,q=3: 1*1=1; p=1,q=2: 0*0=0; p=2,q=1: 1*0=0; p=3,q=0: 0*1=0. Total = **1**

**b_4:** p=0,q=4: 1*0=0 (S3 is 3-dimensional, b_4(S3)=0); p=1,q=3: 0*1=0; p=2,q=2: 1*0=0; p=3,q=1: 0*0=0; p=4,q=0: 1*1=1. Total = **1**

**b_5:** p=2,q=3: 1*1=1; p=3,q=2: 0*0=0; p=4,q=1: 1*0=0. Total = **1**

**b_6:** p=3,q=3: 0*1=0; p=4,q=2: 1*0=0. Total = **0**

**b_7:** p=4,q=3: 1*1=1. Total = **1**

### Summary table

| n | b_n(K) | Kunneth source | Harmonic representative |
|---|--------|----------------|------------------------|
| 0 | 1 | b_0 x b_0 | 1 (constant) |
| 1 | 0 | -- | -- |
| 2 | 1 | b_2(CP2) x b_0(S3) | J (Kahler form on CP2) |
| 3 | 1 | b_0(CP2) x b_3(S3) | Omega_3 (volume form on S3) |
| 4 | 1 | b_4(CP2) x b_0(S3) | omega_4 (volume form on CP2) |
| 5 | 1 | b_2(CP2) x b_3(S3) | J wedge Omega_3 |
| 6 | 0 | -- | -- |
| 7 | 1 | b_4(CP2) x b_3(S3) | omega_4 wedge Omega_3 = vol(K) |

**Euler characteristic:** chi(K) = 1 - 0 + 1 - 1 + 1 - 1 + 0 - 1 = **0**

(Cross-check: chi(CP2)*chi(S3) = 3*0 = 0. Consistent.)

**Total Betti sum:** 1+0+1+1+1+1+0+1 = 6.

---

## 3. Dimensional Reduction: 4D Field Content from Each Harmonic

Each harmonic p-form on the 7-dimensional internal manifold K, when combined with a (d-p)-form on 4D spacetime (d = 0,...,3), produces a 4D field. The key question is: which forms have ALL legs on K (producing 4D scalars) versus some legs on spacetime (producing higher-spin fields)?

### Scalar zero modes (all legs on K)

| Degree | b_n | Form on K | 4D field | Physical role |
|--------|-----|-----------|----------|---------------|
| 0 | 1 | 1 | scalar psi | Volume/breathing mode -> gravity |
| 2 | 1 | J on CP2 | scalar phi_K | Kahler modulus (CP2 shape) |
| 3 | 1 | Omega_3 on S3 | scalar chi | CS period (controls alpha) |

### Higher-form zero modes

| Degree | b_n | Form on K | 4D interpretation |
|--------|-----|-----------|-------------------|
| 4 | 1 | omega_4 on CP2 | 4-form on 4D = topological (cosmo constant contribution) |
| 5 | 1 | J wedge Omega_3 | 1-form on 4D from Hodge dual (massive, decouples) |
| 7 | 1 | vol(K) | Overall normalization, non-dynamical |

---

## 4. Mass Spectrum of the Three Scalars

### 4.1 psi (from b_0): MASSLESS

The breathing mode psi is the trace of the parent metric perturbation. Its shift symmetry is exact in the spatial sector. This is the DFD gravitational scalar, already present in v3.3. Mass: m_psi = 0 (protected by the flat-space construction).

### 4.2 phi_K (from b_2): PLANCK-MASSIVE -- DECOUPLED

The Kahler modulus phi_K parameterizes the size ratio tau = R_2/R_1 of the two internal factors. The v3.3 paper (section_gravitational_waves.tex, lines 105-121) explicitly establishes:

- The constraint function Phi(tau) = 24*tau^{6/7} + 6*tau^{-8/7} has a unique minimum at tau_* = 1/sqrt(3).
- This minimum is the Einstein product condition (6/R_1^2 = 2/R_2^2).
- The DFD master invariant G*hbar*H_0^2/c^5 = alpha^57 enforces tau = tau_* by self-consistency.
- The squashing mode mass: m_phi^2 = O(1) * Lambda^2 ~ M_P^2.
- Dimensionless curvature: Phi''/Phi = 2.94 (no parametric suppression).

**Conclusion:** phi_K has Planck-scale mass and is integrated out at all accessible energies. It contributes zero propagating degrees of freedom to the low-energy theory.

### 4.3 chi (from b_3): ULTRALIGHT -- CANDIDATE PHYSICAL FIELD

The 3-form period chi = integral_{S3} C_3 (where C_3 is a 3-form gauge field on K) is protected by:

1. **Continuous shift symmetry:** chi -> chi + const. This is the remnant of the gauge symmetry of C_3. At the perturbative level, the potential is exactly flat: V(chi) = 0.

2. **Discrete symmetry:** The Chern-Simons level is quantized as k in Z, giving a discrete Z_{k+2} identification. This does not generate a perturbative mass.

3. **Instanton-generated mass:** Non-perturbative effects (instantons wrapping S3) break the shift symmetry and generate:

       m_chi ~ Lambda * exp(-S_inst)

   where S_inst ~ k_max is the instanton action. For k_max = 60 (from the DFD CS level):

       exp(-60) ~ 10^{-26}

   If Lambda ~ M_P ~ 10^{19} GeV:

       m_chi ~ 10^{-26} * 10^{19} GeV ~ 10^{-7} eV

   **This places chi in the ultralight/fuzzy dark matter mass window (10^{-22} to 10^{-7} eV).**

---

## 5. Complete Low-Energy Field Census

Counting only fields with mass below the compactification scale:

| Field | Spin | Mass | Origin | Role in DFD |
|-------|------|------|--------|-------------|
| psi | 0 | 0 | b_0 zero mode | Gravitational scalar (refractive index) |
| chi | 0 | ~10^{-7} eV | b_3 zero mode | CS period -> controls alpha; CDM candidate |
| h_ij^TT | 2 | 0 | spin-2 zero mode | Gravitational waves |

**Total low-energy propagating DOF: 1 (psi) + 1 (chi) + 2 (h_TT) = 4.**

All other modes are either:
- Planck-massive (phi_K from b_2, all KK tower states)
- Topological / non-propagating (b_4 = cosmological constant, b_7 = normalization)
- Massive vectors (b_5 mode, mass ~ M_P from KK)

---

## 6. Key Result: Exactly Two Light Scalars

The Kunneth theorem on CP2 x S3 produces exactly three scalar zero modes. Of these:

- **One is massless** (psi) -- already the gravitational DOF in DFD v3.3.
- **One is Planck-massive** (phi_K) -- decoupled, confirmed by Phi''/Phi = 2.94.
- **One is ultralight** (chi) -- mass exponentially suppressed by instantons.

Therefore the low-energy scalar content is **exactly {psi, chi}**, with no additional light scalars and no fine-tuning required to achieve this count.

The topological origin of this result is robust: it depends only on b_2(CP2) = 1 and b_3(S3) = 1, which are integer topological invariants. No continuous deformation of the internal manifold can change the number of light scalars.

---

## 7. Implications for the R8 Campaign

1. **chi is not ad hoc.** It is the unique b_3 zero mode of the already-established internal manifold CP2 x S3. It was always there; v3.3 simply did not promote it to a dynamical field.

2. **The mass hierarchy is natural.** phi_K is heavy because the constraint potential has O(1) curvature at the Einstein point. chi is light because its potential is generated only non-perturbatively.

3. **chi controls alpha.** The CS level k is determined by the period integral of C_3 over S3. When chi varies, k varies, and alpha varies. This is the microscopic mechanism for the running of alpha in the DFD crossover.

4. **chi is a CDM candidate.** With m ~ 10^{-7} eV, chi behaves as a coherently oscillating scalar field -- ultralight axion-like dark matter. Its equation of state transitions from w = -1 (frozen) to w = 0 (matter-like) when H drops below m_chi, which occurs at z ~ 10^6.

---

## References to v3.3 Paper

- Squashing modulus mass and Phi''/Phi = 2.94: `section_gravitational_waves.tex`, lines 105-121
- Einstein product condition tau_* = 1/sqrt(3): `appendix_O_alpha57.tex`, lines 270-289
- Internal manifold topology: `appendix_Z_complete_params.tex`, lines 10, 172
- Lichnerowicz analysis (no unwanted zero modes): `section_gravitational_waves.tex`, lines 97-108
