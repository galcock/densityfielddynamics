# R6 Agent: Can Initial Conditions Provide Omega_psi-dust ~ 0.25?

## Date: 2026-04-05
## Status: DEFINITIVE NEGATIVE RESULT

---

## EXECUTIVE SUMMARY

The temporal sector of DFD **cannot** provide Omega_psi-dust ~ 0.25 at late times, regardless of initial conditions set during inflation or reheating. The fundamental obstacle is the energy scale prefactor a\*^2/(8piG) = 4.24 x 10^-45 kg/m^3, which is **10^18 times below** rho_crit = 8.50 x 10^-27 kg/m^3. No choice of conserved charge C_0 can compensate this deficit because the conservation law a^3 mu(Delta) = C_0 constrains C_0 < 1 (since mu < 1 always). Three independent approaches all confirm this conclusion:

1. **Direct field energy**: Even maximally excited (C_0 ~ 1), gives Omega_t ~ 10^-18
2. **Linear cross-term** (background psi_dot_0 coupling): Still short by 10^17
3. **Phantom dark matter** from QUMOND: Gives Omega_phantom ~ 0.009, short by factor 30

The dust branch (w -> 0, c_s -> 0) is a **qualitative** result about the equation of state, not a quantitative statement about energy density. DFD's temporal sector behaves like CDM, but at an amplitude suppressed by 10^18.

---

## 1. THE CONSERVATION LAW AND ITS CONSTRAINTS

### 1.1 Setup

The temporal sector Lagrangian is:

    L_temp = (a*^2 / 8piG) K(Delta)

where Delta = (c/a_0)|psi_dot - psi_dot_0| and K'(Delta) = mu(Delta) = Delta/(1+Delta).

The conserved current gives:

    a^3 mu(Delta) = C_0 = constant

Since mu(Delta) = Delta/(1+Delta) < 1 for all finite Delta, we have **C_0 < a_initial^3**.

### 1.2 Solving for Delta(a)

    Delta(a) = C_0 / (a^3 - C_0)    for a^3 > C_0

This has a singularity at a_sing = C_0^(1/3). The temporal sector only exists for a > a_sing.

### 1.3 The Omega constraint

For C_0 set at matter-radiation equality (a_eq ~ 1/3400):

    C_0,max = a_eq^3 = 2.54 x 10^-11
    Delta(a=1) = 2.54 x 10^-11
    Omega_t(today) ~ 2.8 x 10^-35

For C_0 set at inflation (a ~ 10^-26):

    C_0 ~ 10^-78
    Delta(today) ~ 10^-78
    Omega_t ~ effectively zero

For C_0 ~ 0.5 (needed for Delta(today) ~ 1):

    Singularity at a_sing = 0.794
    Temporal sector doesn't exist before a = 0.794
    MISSES all of radiation domination, CMB, BBN
    PHYSICALLY UNACCEPTABLE

---

## 2. APPROACH 1: Direct Field Energy

### 2.1 The energy density functions

Integrating K'(Delta) = Delta/(1+Delta):

    K(Delta) = Delta - ln(1+Delta)

The stress-energy tensor gives:

    p = (a*^2/8piG) K(Delta)                          [pressure]
    rho = (a*^2/8piG) [Delta mu(Delta) - K(Delta)]    [density, intrinsic part]

### 2.2 Equation of state w(Delta)

| Delta | K(Delta) | rho/prefactor | p/prefactor | w = p/rho |
|-------|----------|---------------|-------------|-----------|
| 0.001 | 5.0e-7 | 5.0e-7 | 5.0e-7 | 1.001 |
| 0.01 | 5.0e-5 | 4.9e-5 | 5.0e-5 | 1.007 |
| 0.1 | 4.7e-3 | 4.4e-3 | 4.7e-3 | 1.066 |
| 0.5 | 9.5e-2 | 7.2e-2 | 9.5e-2 | 1.311 |
| 1.0 | 3.1e-1 | 1.9e-1 | 3.1e-1 | 1.589 |
| 10 | 7.6 | 1.5 | 7.6 | 5.11 |
| 100 | 95.4 | 3.6 | 95.4 | 26.3 |

**Critical finding**: For the INTRINSIC field energy (without the psi_dot_0 cross-term), w > 1 always. This is **NOT dust**. The w -> 0 behavior only emerges when including the background coupling term.

### 2.3 The prefactor problem

    a*^2/(8piG) = (2a_0/c^2)^2 / (8piG) = a_0^2 / (2piGc^4) = 4.24 x 10^-45 kg/m^3

This is the MOND energy density scale. It encodes the ratio:

    a_0^2/(Gc^4) ~ (10^-10)^2 / (10^-10 * 10^34) ~ 10^-44

Compared to rho_crit ~ 3H_0^2/(8piG) ~ 10^-26, the ratio is:

    (a_0/cH_0)^2 * (H_0^2/c^2) / (H_0^2/c^2) ~ (a_0/cH_0)^2 ~ (a_0/a_0 * some factor)

The MOND coincidence a_0 ~ cH_0 does NOT help because the energy scale involves a_0^2/(Gc^4), not a_0^2/(GH_0^2).

### 2.4 Maximum possible field energy

With C_0 = 1 (absolute theoretical maximum), at a = 2:

    Delta(2) = 1/7 = 0.143
    K(1/7) = 1/7 - ln(8/7) = 0.009
    rho_t = 4.24e-45 * 0.009 = 3.8e-47 kg/m^3
    Omega_t = 4.5e-21

Even at the singularity (Delta -> infinity, a -> 1+):

    rho_t -> (a*^2/8piG) * Delta -> infinity

But this requires a -> C_0^(1/3), which is only reached if C_0 ~ 1 (meaning the singularity is at a ~ 1, missing all earlier cosmology).

---

## 3. APPROACH 2: Phantom Dark Matter from Modified Poisson

### 3.1 The QUMOND enhancement

The DFD/MOND modification of gravity enhances the effective gravitational constant:

    G_eff = nu(y) * G    where nu = 1/mu(sqrt(y))

At the cosmological background:

    x_bar = cH_0/a_0 = 5.45
    mu(x_bar) = 0.845
    nu(x_bar) = 1.184
    (nu - 1) = 0.184

### 3.2 Effective phantom density

The "phantom dark matter" from enhanced gravity:

    rho_phantom = (nu - 1) * rho_baryon = 0.184 * 4.17e-28 = 7.64e-29 kg/m^3
    Omega_phantom = 0.009

This falls short of the needed Omega_CDM = 0.265 by a factor of ~30.

### 3.3 What nu would be required?

For DFD to replace CDM entirely through gravitational enhancement:

    nu_required = rho_crit / rho_baryon = 1/Omega_b = 20.4

But nu(x_bar = 5.45) = 1.18. The theory would need to be in the **deep-MOND regime** (x_bar << 1) to get large nu, but the cosmological EFE always gives x_bar >> 1.

### 3.4 Friedmann equation consistency

If DFD modifies the Friedmann equation as H^2 = (8piG/3) * nu * rho_b, then to match the observed H_0:

    nu * Omega_b = 1
    nu = 20.4

This is **inconsistent** with nu(x_bar) = 1.18. DFD cannot replace all dark matter through gravitational enhancement of baryons alone.

---

## 4. APPROACH 3: Evolution Tracking from Early Times

### 4.1 Late-time scaling

For small Delta (late times), the intrinsic energy scales as:

    rho_t ~ (a*^2/16piG) * Delta^2 ~ (a*^2/16piG) * C_0^2/a^6

This decays as **a^-6** (stiff matter/kination), FASTER than radiation (a^-4), let alone matter (a^-3).

### 4.2 The linear cross-term

The full energy density includes a cross-term from the background psi_dot_0:

    rho_t = (a*^2/8piG) * [Delta mu(Delta) + (c psi_dot_0/a_0) mu(Delta) - K(Delta)]

The term (c psi_dot_0/a_0) mu(Delta) is LINEAR in Delta (for small Delta, mu ~ Delta):

    rho_linear ~ (a*^2/8piG) * (c psi_dot_0/a_0) * Delta ~ (a*^2/8piG) * x_bar * C_0/a^3

This scales as **a^-3** (matter-like!) -- THIS is the dust branch.

But the coefficient is:

    (a*^2/8piG) * x_bar = 4.24e-45 * 5.45 = 2.31e-44 kg/m^3

For Omega_t = 0.25:

    Need C_0 = 0.25 * rho_crit / (2.31e-44) = 9.2 x 10^16

This is IMPOSSIBLE since C_0 < 1.

### 4.3 The homogeneous mode paradox

For the homogeneous FRW background, psi_dot = psi_dot_0 by definition, so:

    Delta_background = 0

The temporal sector carries **ZERO** background energy density. It exists only in perturbations. This makes it fundamentally different from CDM, which has a homogeneous background Omega_CDM ~ 0.265.

### 4.4 Full numerical evolution (C_0 = 10^-6)

| a | Delta | rho_t/prefactor | rho_t * a^3 | rho_t * a^6 | n_eff |
|---|-------|-----------------|-------------|-------------|-------|
| 0.01 | 4.7e15 | 35 | 3.5e-5 | 3.5e-11 | -- |
| 0.1 | 1.0e-3 | 5.0e-7 | 5.0e-10 | 5.0e-13 | 6.0 |
| 0.3 | 3.7e-5 | 6.9e-10 | 1.9e-11 | 5.0e-13 | 6.0 |
| 1.0 | 1.0e-6 | 5.0e-13 | 5.0e-13 | 5.0e-13 | 6.0 |
| 10 | 1.0e-9 | -- | -- | -- | 6.0 |

**Confirmed**: The intrinsic field energy scales as a^-6 at late times (n_eff = 6). The dust-like (a^-3) behavior requires the cross-term with psi_dot_0, which still cannot overcome the 10^18 prefactor deficit.

---

## 5. CAN THE TEMPORAL PREFACTOR DIFFER FROM a*?

### 5.1 The action structure

The full DFD action (Eq. 2.6 in the paper) is:

    S = integral dt d^3x { (a*^2/8piG) [W(spatial) + K(temporal)] - (c^2/2) psi(rho - rho_bar) }

Both W and K share the **same** prefactor a*^2/(8piG). This is NOT a choice but a consequence of the action being a single scalar sector with one coupling constant.

### 5.2 What a different prefactor would require

For Omega ~ 0.25 with K ~ O(1):

    A^2/(8piG) ~ 0.25 * rho_crit
    A ~ 1.9 x 10^-18 m^-1
    A/a* ~ 7 x 10^8

There is no known physical reason for the temporal sector to have a prefactor 10^9 times larger than a*. In particular:

- The MOND acceleration scale a_0 is fixed by galaxy rotation curves
- a* = 2a_0/c^2 is uniquely determined
- The same mu function operates in both spatial and temporal sectors (from the S^3 composition law)
- Changing the temporal prefactor would break the composition law universality

### 5.3 Could higher-derivative terms contribute?

If the temporal sector included terms beyond K(Delta), such as K_2(Delta^2) with a different prefactor, these would generically violate the dust branch (w -> 0). The no-go lemma (Appendix Q) proves that the quadratic invariant gives w -> 1/2, not w -> 0.

---

## 6. THE FUNDAMENTAL ENERGY HIERARCHY

### 6.1 Three energy scales in DFD

| Scale | Expression | Value (kg/m^3) | Ratio to rho_crit |
|-------|-----------|----------------|-------------------|
| MOND field energy | a*^2/(8piG) | 4.24 x 10^-45 | 5.0 x 10^-19 |
| Critical density | 3H_0^2/(8piG) | 8.50 x 10^-27 | 1.0 |
| Gravitational energy (c^4/G) | c^4/(8piG^2) | -- | -- |

The MOND energy scale is tiny because:

    a*^2/(8piG) = a_0^2/(2piGc^4)

This involves a_0^2/c^4, which is the square of the dimensionless ratio a_0/c^2 ~ 10^-27 m^-1, divided by G. The critical density involves H_0^2/G, and:

    (a*^2/8piG) / rho_crit = (a_0/cH_0)^2 * (H_0^2/c^2) * (c^2/H_0^2) * ... ~ (a_0/c^2)^2 * c^2/H_0^2

Due to the MOND coincidence a_0 ~ cH_0 (within a factor):

    a_0^2/(Gc^4) / (H_0^2/G) = a_0^2/(c^4 H_0^2) ~ (a_0/(c^2 H_0))^2/c^0 ...

The 10^18 gap arises fundamentally because the Lagrangian energy scale involves (a_0/c^2)^2, not (H_0/c)^2. Despite the MOND coincidence a_0 ~ cH_0, the factor of c^2 in the denominator creates an enormous suppression.

### 6.2 Physical interpretation

The temporal sector's energy density is suppressed by the same factor that makes MOND effects tiny in natural (Planck) units. MOND is a phenomenon at acceleration scale a_0 ~ 10^-10 m/s^2, which corresponds to an energy density scale:

    rho_MOND ~ a_0^2/(Gc^4) ~ 10^-45 kg/m^3

This is the energy stored in the MOND-regime gravitational field per unit volume. It is 10^18 below the cosmological critical density because gravity is an extremely weak force in absolute terms, and MOND is a gravitational phenomenon at an already tiny acceleration scale.

---

## 7. WHAT THE DFD PAPER ACTUALLY CLAIMS

### 7.1 The dust branch theorem

Theorem 3 in Appendix Q proves:

    w -> 0 and c_s^2 -> 0 as Delta -> 0

This is a statement about the **equation of state**, not the energy density. It says:
- Perturbations in the temporal sector **behave** like CDM (pressureless, no sound speed)
- They grow gravitationally just like CDM perturbations would
- They provide the correct qualitative ingredient for structure formation

### 7.2 What the paper does NOT claim

The paper does not claim that the temporal sector provides Omega ~ 0.25. The "Open Problems" section (Section 13) explicitly lists:
- Full P(k) shape matching as a "program item"
- The amplitude of perturbations as requiring further work
- The quantitative confrontation with survey data as incomplete

### 7.3 The correct interpretation

DFD's temporal dust branch provides the **mechanism** (correct equation of state, correct growth behavior) but NOT the **amplitude** (Omega ~ 0.25). The amplitude must come from either:
- The phantom dark matter of the modified Poisson equation (but this gives only Omega ~ 0.009)
- Additional matter content (sterile neutrinos, etc.)
- A modification of the Friedmann equation itself (beyond the scalar sector energy)
- A mechanism not yet identified within DFD

---

## 8. SPECULATIVE ESCAPE ROUTES

### 8.1 Modified Friedmann equation (not from field energy)

In f(R) gravity, the modification to Einstein's equations creates an effective dark energy that does NOT come from a scalar field's kinetic energy. The effective stress-energy arises from the curvature terms themselves.

Could DFD similarly modify the Friedmann equation through the modified Poisson equation's backreaction? If the spatial sector's nonlinear mu function creates a non-zero effective stress-energy when integrated over the cosmic web, this would operate at the scale c^4/(G), not a*^2/(G), and could potentially reach Omega ~ 0.1-1.

Status: Uncomputed. Would require solving the full nonlinear DFD field equations on a cosmological domain and computing the backreaction.

### 8.2 Scale-dependent phantom DM from the cosmic web

The phantom DM density rho_phantom = (1/4piG) div[(nu-1) grad Phi_N] depends on the **gradient** of the potential, not its mean value. In a clumpy universe with cosmic web structure, the volume-averaged phantom DM could exceed the naive estimate (nu-1)*rho_b = 0.009 * rho_crit.

For filaments and voids in the deep-MOND regime (low acceleration), nu could be much larger than 1.18. If the universe's volume is dominated by voids (where nu >> 1), the effective average nu could be significantly enhanced.

Status: Requires N-body simulation with DFD/MOND gravity to quantify.

### 8.3 Reheating-era resonance

If during reheating, the inflaton's oscillations couple resonantly to the psi field (through the matter coupling c^2/2 psi rho), the temporal sector could be parametrically excited. The question is whether this can produce C_0 >> 1 -- but the conservation law constrains C_0 < a_reheat^3, and a_reheat ~ 10^-26, so C_0 < 10^-78.

Status: Does not work. The conservation law is absolute.

### 8.4 Accepting additional matter

The most conservative interpretation: DFD provides the MOND phenomenology (galaxy rotation curves, Tully-Fisher, RAR) through the spatial sector, and the dust branch provides the correct EOS for cosmological perturbations. The actual dark matter density Omega ~ 0.25 comes from a conventional dark matter candidate (sterile neutrinos at ~2 eV, for example) that interacts gravitationally.

In this picture, DFD is not a "no dark matter" theory but a "modified gravity + reduced dark matter" theory.

---

## 9. DEFINITIVE CONCLUSIONS

### 9.1 The answer to the R6 question

**NO.** The initial conditions of the DFD temporal sector, whether set during inflation or reheating, CANNOT provide Omega_psi-dust ~ 0.25 at late times. The energy scale prefactor a\*^2/(8piG) ~ 10^-45 kg/m^3 is 10^18 below rho_crit, and no initial condition can compensate this deficit because the conservation law constrains the conserved charge C_0 < 1.

### 9.2 Summary of all approaches

| Approach | Result | Can provide Omega ~ 0.25? |
|----------|--------|--------------------------|
| Direct field energy (maximized C_0) | Omega ~ 10^-18 | NO (factor 10^18 short) |
| Different temporal prefactor A != a* | Need A/a* ~ 10^9 | NO (no physical basis) |
| Linear cross-term with psi_dot_0 | Omega ~ 10^-17 | NO (factor 10^17 short) |
| C_0 ~ 1 (late singularity) | Singularity at a ~ 0.8 | NO (misses all early cosmology) |
| Phantom DM from QUMOND | Omega ~ 0.009 | NO (factor 30 short) |
| Friedmann eq. modification | nu_needed = 20 vs nu = 1.18 | NO (factor 17 short) |
| Reheating resonance | C_0 < a_reheat^3 ~ 10^-78 | NO (conservation law forbids) |

### 9.3 The root cause

The 10^18 deficit traces to a single dimensionless ratio:

    a*^2/(8piG) / rho_crit = (a_0/c^2)^2 / (H_0/c)^2 = (a_0/(cH_0))^2 * (H_0/c)^2 / ...

More simply: the Lagrangian energy scale involves a_0^2/(Gc^4), while the critical density involves H_0^2/G. Their ratio is (a_0/(c^2 H_0))^2, and despite the MOND coincidence a_0 ~ cH_0:

    (a_0/c^2)^2 * (1/H_0^2) = (2.67e-27)^2 / (2.18e-18)^2 = 7.11e-54 / 4.75e-36 = 1.5e-18

This is the irreducible 10^-18 factor. It arises because a* = 2a_0/c^2 involves dividing by c^2, which converts the MOND acceleration (~ cH_0) into a length scale (~ H_0/c). The square of this is ~ (H_0/c)^2, while rho_crit/G ~ H_0^2. The ratio (H_0/c)^2 / H_0^2 = 1/c^2, and the extra factor of 1/(8pi) gives ~ 10^-18.

### 9.4 Implications for DFD cosmology

The temporal dust branch is a genuine theoretical achievement -- proving w -> 0 and c_s -> 0 from the composition law is non-trivial. But it addresses the QUALITATIVE question (correct equation of state) while leaving the QUANTITATIVE question (correct amplitude) open. Resolving the amplitude question is listed as an open problem in the paper itself and likely requires one of:

1. A backreaction mechanism from the nonlinear spatial sector (cosmic web phantom DM)
2. Additional dark matter content (reduced CDM, sterile neutrinos)
3. A novel coupling between the modified Friedmann equation and the temporal sector not yet identified

This is the central open challenge for DFD cosmology.
