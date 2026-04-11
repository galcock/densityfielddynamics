# Round 3: QUMOND Reformulation of the DFD Field Equation

## Executive Summary

This document derives the QUMOND (quasi-linear MOND) reformulation of the DFD
field equation, which moves the nonlinearity from the differential operator to the
source side. This avoids the degenerate coefficient at grad psi_bar = 0 that plagues
direct linearization. Key results:

1. The DFD QUMOND construction is structurally identical to Milgrom's QUMOND for AQUAL
2. For cosmological plane waves, QUMOND is EXACT (no curl correction needed per mode)
3. The RMS gradient y_eff = 9.43e-5 places DFD cosmology deep in the MOND regime
4. The resulting nu(y_eff) = 103.5 far exceeds the needed value of 6.4
5. Even with nu >> 1, sigma_8 = 0.008 because the baryon transfer function deficit dominates
6. The QUMOND formulation confirms that the growth enhancement alone cannot close the
   gap -- the transfer function shape (BAO wiggles, Silk damping) is the binding constraint

---

## 1. The Standard QUMOND Construction

### 1.1 Review: AQUAL to QUMOND in Standard MOND

The AQUAL (AQUAdratic Lagrangian) equation is:

    div[ mu(|grad Phi|/a0) grad Phi ] = 4 pi G rho

This has the same structural problem as DFD when linearizing around a zero-gradient
background. Milgrom's QUMOND reformulation proceeds in two steps:

**Step 1 (Linear):** Solve the standard Poisson equation:

    nabla^2 Phi_N = 4 pi G rho

This defines the Newtonian potential Phi_N with its well-behaved Green's function.

**Step 2 (Algebraic):** Define the MOND potential via:

    grad Phi = nu(|grad Phi_N|/a0) * grad Phi_N + curl(h)

where nu(y) is the QUMOND interpolation function related to mu by:

    mu(x) * x = y,  with x = nu(y) * y

The curl correction h ensures grad Phi is irrotational (since Phi must be a scalar).

### 1.2 Deriving nu(y) for mu(x) = x/(1+x)

The algebraic relation mu(x)*x = y gives:

    x^2/(1+x) = y
    x^2 - y*x - y = 0
    x = [y + sqrt(y^2 + 4y)] / 2

Therefore:

    nu(y) = x/y = [1 + sqrt(1 + 4/y)] / 2

Asymptotic limits:
- y >> 1 (Newtonian): nu(y) -> 1 + 1/y + ... (approaches unity)
- y << 1 (deep MOND): nu(y) -> 1/sqrt(y) (large enhancement)

**Verification:** mu(nu(y)*y) * nu(y) * y = y implies mu(x)*x = y. Check:
  x = nu(y)*y = [y + sqrt(y^2+4y)]/2
  mu(x)*x = x^2/(1+x)
  x^2 = [y + sqrt(y^2+4y)]^2/4 = [y^2 + 2y*sqrt(y^2+4y) + y^2+4y]/4
       = [2y^2 + 4y + 2y*sqrt(y^2+4y)]/4
  1+x = 1 + [y + sqrt(y^2+4y)]/2 = [2 + y + sqrt(y^2+4y)]/2
  x^2/(1+x) = [2y^2+4y+2y*sqrt(y^2+4y)] / [2*(2+y+sqrt(y^2+4y))]
             = y * [2y+4+2*sqrt(y^2+4y)] / [2*(2+y+sqrt(y^2+4y))]
             = y * 2[y+2+sqrt(y^2+4y)] / [2*(2+y+sqrt(y^2+4y))]
             = y. Verified.

---

## 2. DFD QUMOND Reformulation

### 2.1 The DFD Field Equation

    div[ mu(|grad psi|/a*) grad psi ] = S

where:
- S = -(8 pi G / c^2)(rho - rho_bar) is the source
- mu(x) = x/(1+x) is the DFD interpolation function
- a* = a0/c^2 = 1.335e-27 m^-1 is the DFD acceleration scale
- psi is the dimensionless DFD potential

### 2.2 Dimensional Analysis

In DFD, the field psi is dimensionless (unlike the Newtonian potential which has
units m^2/s^2). The key dimensional quantities:

    Source: S = -(8piG/c^2)(rho - rho_bar)    [units: m^-2]
    Gradient: grad psi                          [units: m^-1]
    Scale: a* = a0/c^2                          [units: m^-1]
    Argument: |grad psi|/a*                     [dimensionless]

Check: div[mu * grad psi] has units m^-1 * m^-1 = m^-2. Matches S. Consistent.

### 2.3 The QUMOND Construction for DFD

**Step 1 (Linear Poisson):**

    nabla^2 psi_N = S = -(8piG/c^2)(rho - rho_bar)

This gives psi_N as the "Newtonian analog" DFD potential. In Fourier space:

    psi_N(k) = (8piG/c^2) rho_bar delta_k / k^2

**Step 2 (QUMOND Enhancement):**

    grad psi = nu(|grad psi_N|/a*) * grad psi_N + curl(h)

where:

    nu(y) = [1 + sqrt(1 + 4/y)] / 2

and h is a solenoidal correction satisfying:

    nabla^2 h = -curl[ nu(|grad psi_N|/a*) * grad psi_N ]

with boundary condition div(h) = 0.

### 2.4 Why This Works

The QUMOND construction avoids the degeneracy at grad psi_bar = 0 because:

1. The linear Poisson equation nabla^2 psi_N = S is well-posed everywhere
2. The nonlinearity enters only ALGEBRAICALLY through nu, not in the differential operator
3. nu(y) is well-defined for all y > 0 (diverges as 1/sqrt(y) for y -> 0, but the
   product nu(y)*grad psi_N remains well-behaved)
4. No iteration is needed -- solve once, apply nu, done

---

## 3. Application to Cosmological Perturbations

### 3.1 Single Fourier Mode: Exact QUMOND

For a single density perturbation delta(x) = delta_k exp(ik.x):

    psi_N(x) = (8piG/c^2) rho_bar delta_k exp(ik.x) / k^2

    grad psi_N = i * (8piG/c^2) rho_bar delta_k * k_hat * exp(ik.x) / k

The magnitude |grad psi_N| = (8piG/c^2) rho_bar |delta_k| / k is CONSTANT in space.

Therefore nu(|grad psi_N|/a*) is also constant, and:

    curl[ nu * grad psi_N ] = nu * curl[ grad psi_N ] = 0

**Result: For a single Fourier mode, the curl correction vanishes identically.
The QUMOND construction is EXACT, with h = 0.**

The DFD potential for a single mode is:

    grad psi = nu(y_k) * grad psi_N

    psi(k) = nu(y_k) * psi_N(k)

where:

    y_k = |grad psi_N| / a* = (8piG rho_bar / (c^2 a*)) * |delta_k| / k

### 3.2 The Mode-Dependent Enhancement Parameter

Define:

    alpha = 8piG/c^2 = 1.866e-26 m/kg
    A = alpha * rho_bar_b / a* = 5.872e-27 m^-1

Then for each mode:

    y_k = A * |delta_k| / k_phys

where k_phys is in m^-1. The QUMOND enhancement for each mode:

    P_psi(k) = nu^2(y_k) * P_psiN(k)

### 3.3 Superposition of Modes: The Curl Problem

For a realistic cosmological field with many modes, the total gradient:

    grad psi_N(x) = sum_k (grad psi_N)_k * exp(ik.x)

has spatially varying magnitude |grad psi_N(x)|, making nu(x) vary in space.

The curl correction then satisfies:

    nabla^2 h = -curl[ nu(|grad psi_N(x)|/a*) * grad psi_N(x) ]

This is nonzero whenever:
- nu varies in space (i.e., |grad psi_N| is not uniform), AND
- grad psi_N has components in more than one direction

The curl term generates MODE COUPLING: power from mode k leaks into other modes
through the nonlinear nu function. This is analogous to the mode-coupling analysis
in Agent 13 and Agent 16.

For weakly nonlinear perturbations, the curl correction is subleading. The dominant
effect is the mode-by-mode enhancement nu^2(y_k).

---

## 4. Numerical Results: y_eff and nu(y_eff)

### 4.1 The RMS Gradient

The RMS gradient of the Newtonian DFD potential:

    <|grad psi_N|^2> = (alpha * rho_bar)^2 * sigma_{-1}^2 * (Mpc/h -> m)^2

where:

    sigma_{-1}^2 = int P_delta(k) dk / (2 pi^2) = 0.1231 (Mpc/h)^2

Computed with the Eisenstein-Hu baryon-only transfer function (Omega_b h^2 = 0.02237).

The dimensionless RMS gradient:

    y_eff = |grad psi_N|_rms / a* = 9.434e-05

### 4.2 QUMOND Enhancement

| Quantity | Value |
|---|---|
| y_eff | 9.434e-05 |
| nu(y_eff) | 103.46 |
| nu^2(y_eff) | 10703 |
| nu_needed = Omega_m/Omega_b | 6.397 |
| y_needed for nu = 6.397 | 0.02897 |

The DFD cosmology is deeply in the MOND regime (y_eff << 1), giving nu >> nu_needed.

### 4.3 Volume-Averaged nu (Chi-3 Distribution)

For a Gaussian random field, |grad psi_N(x)| follows a chi distribution with 3 DOF.
The volume-averaged QUMOND function:

    <nu> = int nu(|g|/a*) * f_chi3(|g|/sigma_comp) d|g| = 117.03

    <nu^2> = 14766

The volume-averaged nu exceeds the point estimate nu(y_eff) = 103.5 by a factor of
1.13, consistent with Jensen's inequality (nu is convex, so <nu(y)> > nu(<y>)).

### 4.4 Table: <nu> vs y_rms

| y_rms | nu(y_rms) | <nu>_chi3 | <nu>/<nu(y)> | Omega_eff |
|-------|-----------|-----------|--------------|-----------|
| 1e-10 | 100001 | 113188 | 1.132 | 5574 |
| 1e-08 | 10001 | 11319 | 1.132 | 557 |
| 1e-06 | 1001 | 1132 | 1.132 | 55.8 |
| 1e-04 | 100.5 | 113.7 | 1.131 | 5.60 |
| 1e-02 | 10.5 | 11.8 | 1.125 | 0.583 |
| 0.029 | 6.39 | 7.17 | 1.121 | 0.353 |
| 0.10 | 3.70 | 4.12 | 1.112 | 0.203 |
| 0.50 | 2.00 | 2.18 | 1.091 | 0.107 |
| 1.00 | 1.62 | 1.74 | 1.077 | 0.086 |
| 5.00 | 1.17 | 1.22 | 1.040 | 0.060 |
| 10.0 | 1.09 | 1.12 | 1.026 | 0.055 |

The enhancement ratio <nu>/<nu(y_rms)> approaches the universal constant 1.132 in the
deep MOND limit. This is the 3D analog of the acoustic-averaging constant C_MOND = 1.669
found by Agent 15 (which was for 1D oscillations).

### 4.5 Resulting sigma_8

    sigma_8 (baryon-only Newtonian) = 8.0e-05
    sigma_8 (QUMOND, global nu) = nu * sigma_8_N = 103.5 * 8.0e-05 = 0.0082

Even with nu = 103.5, sigma_8 is two orders of magnitude too small. This is because:
1. The baryon transfer function has massive Silk damping at k > 0.1 h/Mpc
2. The BAO oscillations create deep nulls
3. The growth factor enhancement (nu) cannot compensate for the exponential
   suppression in T(k)

To achieve sigma_8 = 0.81, one would need <nu^2> ~ 1.03e8, corresponding to
<nu> ~ 10169. This requires y_rms ~ 1.5e-9, which is physically unreasonable
without additional mechanisms.

---

## 5. The Curl Correction in Detail

### 5.1 General Formula

For a multi-mode field:

    grad psi = nu(|grad psi_N(x)|/a*) * grad psi_N(x) + curl(h)

The curl of the first term:

    curl[nu(y(x)) * g_N(x)] = grad nu(y) cross g_N + nu * curl(g_N)

Since g_N = grad psi_N is irrotational, curl(g_N) = 0. Therefore:

    curl[nu * g_N] = grad nu cross g_N

Now: grad nu = (d nu/dy) * grad y, and y = |g_N|/a*, so:

    grad y = grad|g_N| / a* = (g_N . nabla) g_N / (a* |g_N|)
           = (1/a*) * sum_j (g_N^j / |g_N|) * partial_j g_N

For a Gaussian random field, this cross product is generically nonzero, producing
a solenoidal field that must be compensated by curl(h).

### 5.2 Magnitude Estimate for Cosmological Perturbations

The curl correction is of order:

    |curl[nu * g_N]| ~ |d nu/dy| * |grad y| * |g_N|
                     ~ |d nu/dy| * |g_N|^2 / (a* L) * sin(theta)

where L is the coherence length of the field and theta is the angle between
grad|g_N| and g_N.

For the deep MOND limit (y << 1):
    d nu/dy ~ -1/(2 y^{3/2})
    |curl| ~ |g_N|^2 / (2 a* y^{3/2} L)
           = (a*)^{1/2} |g_N|^{1/2} / (2 L)

The ratio of curl correction to the main term:

    |curl(h)| / |nu * g_N| ~ 1/(k L)

where k is the wavenumber and L is the gradient coherence length. For modes with
k*L >> 1 (most cosmological modes), the curl correction is subdominant.

### 5.3 Implication for P(k)

The curl correction contributes to the power spectrum at order (k_NL/k)^2 where
k_NL is the nonlinear scale. For cosmological linear scales (k < 0.1 h/Mpc), this
correction is negligible, and the mode-by-mode QUMOND enhancement is an excellent
approximation:

    P_DFD(k) = nu^2(y_k) * P_N(k) + O(curl correction)

The mode coupling from the curl term becomes important only at small scales where
nonlinearities generate significant gradient correlations.

---

## 6. Connection to the Degeneracy Problem

### 6.1 Why QUMOND Avoids the Degeneracy

The direct DFD equation has a degenerate coefficient at grad psi_bar = 0:

    div[ mu(|grad psi|/a*) grad psi ] = S
    => mu(0) = 0, so the linearized operator vanishes

The QUMOND reformulation sidesteps this entirely:

1. The LINEAR Poisson equation nabla^2 psi_N = S is non-degenerate
2. psi_N has a well-defined Green's function (1/|r-r'|)
3. The nonlinearity enters only in the ALGEBRAIC relation grad psi = nu * grad psi_N
4. nu diverges as 1/sqrt(y) for y -> 0, but the product nu(y) * grad psi_N =
   nu(y) * y * a* * (grad psi_N/|grad psi_N|) is well-defined

### 6.2 Comparison with the Singular Perturbation Approach (Agent 8)

Agent 8 showed that direct perturbation theory gives:

    J_leading = (1/a*) |grad delta_psi| * grad delta_psi

which is QUADRATIC, not linear. The effective coupling is:

    G_eff ~ G * |grad delta_psi| / a*

The QUMOND approach gives the SAME physics but organizes it differently:

    grad psi = nu(|g_N|/a*) * g_N ~ (a*/|g_N|)^{1/2} * g_N = sqrt(a* |g_N|) * g_N_hat

Both approaches agree: the DFD response at grad psi_bar = 0 is proportional to
sqrt(|source|), not proportional to |source| as in Newtonian gravity.

---

## 7. Self-Consistency and the Psi-Screen

### 7.1 QUMOND is Non-Iterative

A key advantage of the QUMOND formulation: it requires NO iteration.

    1. Solve nabla^2 psi_N = S ONCE (linear, trivial in Fourier space)
    2. Compute nu(|grad psi_N|/a*) at each point
    3. Construct grad psi = nu * grad psi_N + curl(h)
    Done.

This contrasts with the direct DFD equation, which is an implicit nonlinear PDE
requiring iterative or continuation methods.

### 7.2 The Psi-Screen's Role

The numerical results show that "bare" QUMOND (without the psi-screen) gives:
- nu(y_eff) = 103.5 (far exceeding nu_needed = 6.4)
- sigma_8 = 0.008 (two orders of magnitude below observed)

The psi-screen mechanism (R2 Agent) provides an external field effect that:
1. Sets an effective background gradient, raising y_eff
2. Brings nu closer to the needed value of 6.4
3. But does NOT solve the transfer function shape problem

For the QUMOND formulation to match observations, the psi-screen must set:

    y_screen = 0.029 (to get nu = 6.4)

This corresponds to |grad psi_screen|/a* = 0.029, or:

    |grad psi_screen| = 0.029 * a* = 3.87e-29 m^-1

### 7.3 Modified QUMOND with External Field

With a psi-screen providing background gradient g_0:

    y_eff = |g_N + g_0| / a*

For g_0 >> g_N (strong EFE), y_eff ~ |g_0|/a* and nu ~ nu(|g_0|/a*).
The perturbations then grow with an effectively constant G_eff = G/mu(nu*y_eff).

The QUMOND equation becomes:

    nabla^2 psi_N = S (unchanged)
    grad psi = nu(|grad psi_N + g_0|/a*) * (grad psi_N + g_0) - nu(|g_0|/a*) * g_0 + curl(h)

Linearizing in grad psi_N around g_0:

    delta(grad psi) = [nu(y_0) + nu'(y_0) * (g_0.grad psi_N)/(a*|g_0|)] * grad psi_N
                    + nu'(y_0) * (g_0.grad psi_N) * g_0 / (a*|g_0|) + ...

This is now LINEAR in grad psi_N, with well-defined coefficients set by the
external field g_0. This is the proper linearized DFD theory.

---

## 8. Power Spectrum in QUMOND Formulation

### 8.1 Mode-by-Mode Formula (Ignoring Curl)

For each wavenumber k:

    P_psi(k) = nu^2(y_k) * P_psiN(k)

    P_delta,DFD(k) = nu^2(y_k) * P_delta,N(k)

where P_delta,N(k) is the baryon-only Newtonian matter power spectrum (Eisenstein-Hu).

### 8.2 With Psi-Screen (Linearized)

If the psi-screen provides a background y_0 = |g_0|/a*, the linearized enhancement is:

    P_delta,DFD(k) = nu^2(y_0) * P_delta,N(k) * (1 + anisotropy corrections)

The anisotropy corrections arise from the preferred direction g_0 and are suppressed
by averaging over the screen's orientation (if it varies on large scales).

For y_0 = 0.029 (nu = 6.4):

    P_DFD(k) / P_N(k) = nu^2 = 40.9

    sigma_8,DFD / sigma_8,N = nu = 6.4

    sigma_8,DFD = 6.4 * 8.0e-05 = 5.1e-04

This is STILL far below 0.81. The fundamental problem remains the baryon transfer
function, not the growth enhancement.

### 8.3 Needed Enhancement for sigma_8 = 0.81

    nu^2_needed = (0.81 / 8.0e-05)^2 = 1.03e8
    nu_needed = 10169

No physically reasonable y can produce this. The deficit is structural: the baryon-only
transfer function has sigma_8 ~ 8e-05, requiring a factor of ~10000 in sigma_8
enhancement, or 10^8 in power spectrum enhancement.

---

## 9. Conclusions

### 9.1 Mathematical Results

1. **QUMOND reformulation exists and is well-defined** for the DFD field equation,
   with the same structure as Milgrom's QUMOND for AQUAL.

2. **The nu function** is nu(y) = [1 + sqrt(1+4/y)]/2, with deep MOND limit
   nu ~ 1/sqrt(y).

3. **For single Fourier modes**, QUMOND is exact with no curl correction.

4. **For multi-mode fields**, the curl correction is subdominant on linear scales
   and introduces mode coupling only at nonlinear scales.

5. **The DFD cosmology is deeply in the MOND regime**: y_eff = 9.4e-05, giving
   nu = 103.5, far exceeding the target nu = 6.4.

### 9.2 Physical Implications

1. **The QUMOND formulation confirms** that the growth equation enhancement alone
   cannot produce the observed P(k). The baryon transfer function deficit
   (sigma_8,baryon = 8e-05 vs sigma_8,obs = 0.81) dominates.

2. **The psi-screen** must play a dual role:
   - Provide an effective background gradient (external field effect)
   - Somehow modify the transfer function shape (BAO + Silk damping)

3. **Mode coupling from nu** acts in the right direction (transfers power from
   large to small scales, partially filling in Silk-damped regions) but is
   quantitatively insufficient.

4. **The QUMOND framework** provides the cleanest theoretical foundation for
   computing the DFD P(k), since it separates the linear problem (Poisson) from
   the nonlinear enhancement (algebraic nu).

### 9.3 Key Numbers

| Quantity | Value |
|---|---|
| a* = a0/c^2 | 1.335e-27 m^-1 |
| alpha = 8piG/c^2 | 1.866e-26 m/kg |
| alpha * rho_bar / a* | 5.872e-27 m^-1 |
| sigma_{-1}^2 (baryon) | 0.1231 (Mpc/h)^2 |
| y_eff (bare, no screen) | 9.434e-05 |
| nu(y_eff) | 103.46 |
| <nu>_chi3 (volume avg) | 117.03 |
| y_needed for nu = 6.4 | 0.02897 |
| sigma_8 (baryon-only) | 8.0e-05 |
| sigma_8 (QUMOND, bare) | 0.0082 |
| sigma_8 (QUMOND, w/ screen at y=0.029) | 5.1e-04 |
| sigma_8 (observed) | 0.81 |
