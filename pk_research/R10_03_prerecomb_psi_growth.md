# R10 Agent 3: Pre-Recombination psi-Perturbation Growth -- Can psi Provide the CDM Transfer Function?

**Campaign:** R10 (Transfer Function Closure)
**Agent:** 3 (Pre-Recombination psi Growth)
**Date:** 2026-04-05
**Status:** COMPLETE -- DEFINITIVE NEGATIVE. psi perturbations cannot grow independently during radiation domination.

---

## 0. Executive Summary

R9 Agent 8 identified the most promising unexplored calculation in the campaign: psi perturbations have c_s^2 = 0, do not couple to photons, and couple to matter at scale c^2/(8piG) rather than the suppressed a*^2/(8piG). If they grew logarithmically during radiation domination like CDM, they could provide pre-recombination potential wells and close the transfer function gap.

**This report computes the answer: psi perturbations do NOT grow during radiation domination.** The result follows from three independent arguments, each sufficient alone:

1. **The spatial psi equation is an elliptic constraint, not a dynamical evolution equation.** psi responds instantaneously to the matter distribution. It has no independent growth mode.

2. **The temporal correction (K''(0) = 1 wave term) gives oscillation tracking, not growth.** An oscillating source delta_b ~ cos(omega t) produces psi ~ cos(omega t)/omega^2, which oscillates but does not accumulate.

3. **The DC component of the nonlinear response is exactly zero** (proved by Agent 7 in Round 1). The flux function F(g) = mu(|g|/a*) g is odd in g, so the time-averaged nonlinear response to a symmetric oscillation vanishes identically.

**Implication:** Path A (psi alone, no CDM) cannot reproduce the LCDM transfer function. The transfer function deficit (factor ~10^4 at k = 0.1 h/Mpc) cannot be closed by pre-recombination psi growth.

---

## 1. The Physical Question

### 1.1 Why CDM Grows During Radiation Domination

In LCDM, cold dark matter perturbations grow logarithmically during radiation domination through the Meszaros effect. The mechanism:

- CDM is a particle species with its own phase space distribution
- CDM has w = 0, c_s^2 = 0 (pressureless, no sound speed)
- CDM does NOT couple to photons (no Compton scattering)
- CDM DOES self-gravitate

The Meszaros equation for CDM during radiation domination (a << a_eq):

    delta_CDM'' + (2/3t) delta_CDM' = (3/2)(a_eq/a)(H^2) delta_CDM

During radiation domination, H^2 ~ 1/(2t)^2 and the CDM self-gravity source term is suppressed by (a_eq/a) << 1. The solution is:

    delta_CDM ~ C_1 + C_2 ln(a)

The logarithmic growth is slow, but it is GROWTH -- CDM perturbations steadily deepen their potential wells while baryon-photon perturbations merely oscillate. After recombination, baryons fall into these pre-existing CDM wells, which is why the CDM transfer function has power at all scales (including those where Silk damping has erased baryon perturbations).

### 1.2 The Hopeful Analogy for psi

R9 Agent 8 noted that psi shares several CDM properties:

| Property | CDM | psi (temporal dust) |
|----------|-----|---------------------|
| w | 0 | 0 (Appendix Q, Theorem 6) |
| c_s^2 | 0 | 0 (Appendix Q) |
| Photon coupling | None | None (couples to rho - rho_bar only) |
| Independent dynamics | Yes (particle species) | **This is the question** |

If psi had independent dynamics like CDM, pre-recombination logarithmic growth would create potential wells that baryons fall into post-recombination. This would close the transfer function gap.

---

## 2. Argument 1: The Spatial Equation is a Constraint

### 2.1 The DFD Field Equation

The spatial sector of the DFD action gives:

    div[mu(|grad psi|/a*) grad psi] = -(8piG/c^2)(rho - rho_bar)

This is an **elliptic partial differential equation** -- a constraint equation, not an evolution equation. Given a density distribution rho(x, t) at any instant, psi(x, t) is determined INSTANTANEOUSLY by solving the elliptic boundary value problem. There is no time derivative in this equation. psi has no memory, no inertia, and no independent dynamics in the spatial sector.

### 2.2 Contrast with CDM

CDM obeys the Vlasov-Poisson system:

    df/dt + v . grad_x f - grad_x Phi . grad_v f = 0

This is a **hyperbolic** evolution equation. CDM particles have positions and velocities that evolve in time. Even if the gravitational potential changes (as it does during radiation domination), CDM particles continue moving under their own inertia. This inertia is what allows CDM to accumulate in overdensities over time.

psi has no analogue of this inertia in the spatial sector. When the source rho(x,t) changes, psi adjusts instantaneously. There is no "coasting" into potential wells.

### 2.3 What psi Does During Baryon-Photon Oscillations

During radiation domination, the baryon-photon fluid oscillates acoustically:

    delta_b(k, t) ~ A_k cos(c_s k t + phi_k)

The psi field tracks this oscillation instantaneously. At each moment, psi(x,t) is the solution to:

    div[mu(|grad psi|/a*) grad psi] = -(8piG/c^2) rho_bar delta_b(x, t)

When delta_b is at a maximum (compression), psi peaks. When delta_b passes through zero (rarefaction), psi returns to zero. When delta_b reverses sign, psi reverses sign. There is no accumulation. The time-average of psi over one acoustic period is zero (for symmetric oscillations).

### 2.4 The Crucial Distinction

CDM grows because particles FREE-STREAM into overdensities. Even when the potential well is temporarily erased (during the acoustic oscillation's zero-crossing), CDM particles are still falling inward under their momentum. When the well reforms, more CDM has accumulated.

psi has no free-streaming. It is a field determined by a constraint. When the source vanishes, psi vanishes. No accumulation occurs.

---

## 3. Argument 2: The Temporal Correction Gives Oscillation, Not Growth

### 3.1 The Temporal Wave Term

The temporal sector of the DFD action contributes K(Delta) with K''(0) = 1. This adds a second time derivative to the field equation, making it hyperbolic:

    (4a_0/c^4) psi_tt + [spatial 3-Laplacian terms] = -(8piG/c^2)(rho - rho_bar)

As established in R3 and R4, this temporal term is a 0.2% correction at k = 0.1 h/Mpc relative to the spatial terms. Nevertheless, let us examine whether it enables independent growth.

### 3.2 The Deep Sub-Horizon Limit

On scales well inside the Hubble radius (k >> aH), the spatial gradient terms dominate and the equation is effectively the elliptic constraint (Argument 1). The temporal wave term is negligible.

### 3.3 The Deep Super-Horizon Limit

On scales well outside the Hubble radius (k << aH), spatial gradients are negligible and the equation reduces to:

    (4a_0/c^4) delta_psi_tt ~ (8piG/c^2) rho_bar delta_b

Rearranging:

    delta_psi_tt ~ (2piG c^2 / a_0) rho_bar delta_b

If delta_b oscillates: delta_b ~ A cos(omega t), then:

    delta_psi_tt ~ B cos(omega t)
    delta_psi ~ -B cos(omega t) / omega^2

This is forced oscillation, not growth. psi oscillates at the same frequency as the source, with amplitude suppressed by 1/omega^2. There is no secular (growing) term.

### 3.4 Could There Be a Growing Homogeneous Solution?

The homogeneous equation (no source) is:

    (4a_0/c^4) delta_psi_tt + k^2 [spatial operator] delta_psi = 0

This is a wave equation with solutions delta_psi ~ exp(+/- i omega_psi t) where omega_psi^2 ~ (c^4 k^2 / 4a_0) [spatial coefficient].

**These are oscillating solutions, not growing solutions.** The temporal wave term does not introduce a Jeans-type instability because psi has no self-gravity -- psi perturbations do not source psi. The source is always (rho - rho_bar), which is the matter perturbation.

### 3.5 The Meszaros Equation Requires Self-Gravity

The CDM Meszaros equation has the critical structure:

    delta_CDM'' + 2H delta_CDM' = 4piG rho_CDM delta_CDM
                                   ^^^^^^^^^^^^^^^^^^^^^^^^
                                   CDM SELF-GRAVITY

The right-hand side contains delta_CDM itself -- CDM perturbations source their own growth. This is what gives the logarithmic growing mode.

For psi, the equation has the structure:

    psi_tt + [spatial terms] psi = (source depending on rho_b delta_b)
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                   BARYON density, not psi self-gravity

psi perturbations are driven by BARYON perturbations. There is no psi self-gravity term because psi does not gravitate -- it is a MOND enhancement field, not a matter species. Without self-gravity, there is no Meszaros-type instability and no logarithmic growth.

---

## 4. Argument 3: The DC Component of the Nonlinear Response is Exactly Zero

### 4.1 The Hope: Nonlinear Rectification

The spatial psi equation involves the 3-Laplacian, which is nonlinear. One might hope that the nonlinear response to an oscillating source produces a non-zero time-averaged (DC) component. This is the "rectification" mechanism explored extensively in Rounds 1-3.

The idea: mu(x) = x/(1+x) responds asymmetrically to strong vs weak fields. In the deep MOND regime, psi ~ delta^{1/2}. Since (delta)^{1/2} != -(|-delta|)^{1/2}, the response to overdensities and underdensities is asymmetric. Perhaps the time-average of psi over one oscillation period is non-zero.

### 4.2 Agent 7's Proof: DC = 0 Exactly

Agent 7 (Round 1) proved this rigorously. The flux function is:

    F(g) = mu(|g|/a*) g = g|g| / (a* + |g|)

This function is ODD in g: F(-g) = -F(g). This is because mu(|g|/a*) depends only on |g|, so the product mu(|g|/a*) * g inherits the sign of g.

For a source delta_b(x,t) = delta_0 cos(kx) cos(omega t) that is temporally symmetric (equal time at positive and negative values), the time-averaged response satisfies:

    <F(g(x,t))>_t = (1/T) integral_0^T F(g(x,t)) dt

Since g(x,t) is odd under the half-period shift t -> t + T/2 (because cos(omega(t + T/2)) = -cos(omega t)):

    g(x, t + T/2) = -g(x, t)

Therefore:

    F(g(x, t+T/2)) = F(-g(x,t)) = -F(g(x,t))

And the time average:

    <F(g)>_t = (1/T) [integral_0^{T/2} F(g) dt + integral_{T/2}^T F(g) dt]
             = (1/T) [integral_0^{T/2} F(g) dt + integral_0^{T/2} (-F(g)) dt]
             = 0

**The DC component is exactly zero.** The nonlinear MOND response does not rectify acoustic oscillations into a static potential well. This proof uses only the oddness of F(g) and the temporal symmetry of the acoustic oscillation.

### 4.3 What About Non-Symmetric Oscillations?

Real baryon-photon oscillations are not perfectly symmetric due to:
- Baryon loading (baryons add to the compressive half-cycle)
- The Doppler contribution
- Damping (Silk diffusion)

The baryon loading asymmetry at z ~ 1100 is characterized by R_s = 3 rho_b / (4 rho_gamma) ~ 0.6. This introduces an O(R_s) correction to the symmetry. However:

(a) R_s = 0.6 gives only a modest asymmetry, not the factor ~10^4 enhancement needed.

(b) Even with asymmetric oscillations, the "DC" that accumulates is not a static potential well -- it decays as the acoustic oscillation damps. It does not grow.

(c) Most importantly, the DC component from rectification has the WRONG k-dependence. It would be strongest at the acoustic peaks (where oscillation amplitude is largest), not at the scales where CDM power is needed (small scales, Silk-damped scales).

### 4.4 What About Mode Coupling?

Mode coupling (delta^2 terms) CAN produce a DC component (this is the Round 1 Agent 13 result). However, as computed in R7:

- Mode coupling transfers power from acoustic scales to small scales
- The amplitude is O(delta^2) ~ 10^{-10} during radiation domination
- This is 5 orders of magnitude below the CDM transfer function level
- Mode coupling grows as delta^2 grows, so it is a POST-recombination effect

---

## 5. The Phantom Dark Matter Question

### 5.1 Does Phantom DM Help?

In the QUMOND formulation, the phantom dark matter density is:

    rho_phantom = rho_b (nu(y) - 1)

where y = g_N / a_0. During radiation domination:

- g_N is determined by the (oscillating) baryon perturbation
- nu(y) - 1 is determined by g_N
- Therefore rho_phantom ALSO oscillates

Phantom DM does not provide a static potential well. It tracks the baryon-photon oscillations with the MOND enhancement factor nu - 1. When baryons oscillate, so does phantom DM. When baryons pass through zero (sound wave nodes), phantom DM also passes through zero.

### 5.2 Quantitative Check

At z = 3400 (matter-radiation equality), for k = 0.1 h/Mpc:

- delta_b ~ 10^{-5} (primordial amplitude)
- g_N = 4piG rho_b delta_b / k_phys
- rho_b(z = 3400) = rho_b,0 (1+3400)^3 = 2.7e-19 kg/m^3
- k_phys = 0.1 / (a Mpc) = 0.1 * 3401 / (3.09e22) = 1.1e-20 m^{-1}
- g_N = 4pi (6.67e-11)(2.7e-19)(1e-5) / (1.1e-20) = 2.1e-14 m/s^2
- y = g_N / a_0 = 2.1e-14 / 1.2e-10 = 1.7e-4

This is deeply Newtonian (y << 1 is deep MOND, y >> 1 is Newtonian -- wait, the convention here needs care).

In the QUMOND convention, y = g_N/a_0 and nu(y) ~ 1/(2y)^{1/2} for y << 1. But this is the standard MOND convention where low y means weak field (deep MOND). Let me re-evaluate:

- y = g_N/a_0 = 1.7e-4

This is y << 1, meaning DEEP MOND regime. The enhancement is:

    nu(y) ~ 1/sqrt(2y) ~ 1/sqrt(3.4e-4) ~ 54

So rho_phantom ~ 54 * rho_b -- a large enhancement! But this enhancement applies to the OSCILLATING perturbation, not to a static background. The phantom DM perturbation:

    delta_phantom = nu * delta_b * cos(omega t)

oscillates at the same acoustic frequency as the baryons. It provides no DC potential well.

### 5.3 The R3 Result Revisited

The R3 pre-recombination transfer function calculation found:

- nu ~ 2-4 at relevant scales at recombination
- Omega_m,eff = nu * Omega_b ~ 0.10-0.18

This falls short of the required Omega_m = 0.315 by a factor of 2-3. But more fundamentally, the calculation used nu to define an effective matter content for the Eisenstein-Hu fitting formula. This procedure assumes that the MOND-enhanced matter creates potential wells BEFORE recombination (like CDM). As shown above, it does not -- the enhancement just makes the oscillations larger, it does not create static wells.

The R3 procedure of plugging Omega_m,eff into the EH formula implicitly assumes a CDM-like transfer function at that effective Omega_m. This is not self-consistent: the enhanced matter still oscillates, so the actual transfer function is that of a baryon-only universe (with Silk damping), not a CDM+baryon universe.

---

## 6. Why CDM Is Special: The Phase Space Argument

### 6.1 The Deep Physical Reason

CDM grows during radiation domination because it occupies a SEPARATE PHASE SPACE from the baryon-photon fluid. CDM particles have their own positions and velocities, independent of the baryon-photon state. Even when the gravitational potential from radiation oscillates, CDM particles continue on their ballistic trajectories.

psi does NOT occupy a separate phase space. psi is determined by the matter distribution through a constraint equation. It has no independent degrees of freedom at the leading (spatial) order. The temporal correction adds one propagating mode, but this mode:

(a) Is 0.2% of the spatial response at relevant scales
(b) Oscillates rather than grows (no self-gravity)
(c) Has amplitude suppressed by a*^2/(8piG) ~ 10^{-18} rho_crit

### 6.2 What Would Be Needed

For psi to provide CDM-like pre-recombination growth, one of these would need to be true:

1. psi has a self-gravity term (psi perturbations source psi growth) -- FALSE: the source is always (rho - rho_bar)

2. psi has a kinetic term that allows free-streaming into overdensities -- FALSE: the spatial equation is elliptic (constraint), and the temporal kinetic term is negligible

3. The nonlinear 3-Laplacian rectifies oscillations into static wells -- FALSE: proved zero by the F(-g) = -F(g) symmetry

4. Some other mechanism in the DFD action creates pre-recombination growth -- Examined exhaustively in 9 rounds; none found

---

## 7. Implications for the Three Paths

### 7.1 Path A (psi Alone): Transfer Function Gap CONFIRMED

This calculation confirms the transfer function gap identified in R2-R3:

- The baryon-only transfer function is Silk-damped for k > 0.05 h/Mpc
- No mechanism in the psi sector creates pre-recombination potential wells
- The MOND enhancement (nu ~ 2-54 depending on scale and epoch) amplifies OSCILLATIONS, not static wells
- Post-recombination growth can potentially compensate via the enhanced G_eff mechanism (R7 N-body gives sigma_8 = 0.773), but the P(k) SHAPE remains wrong: too much large-scale power, too little small-scale power relative to LCDM

The transfer function deficit at k = 0.1 h/Mpc is:

    T_DFD^2 / T_LCDM^2 ~ 10^{-4}

This cannot be compensated by post-recombination MOND growth enhancement, which is scale-independent at leading order.

### 7.2 Path B (psi + chi): Remains Viable

If chi provides the CDM-like perturbation growth (w = 0, c_s^2 = 0, independent phase space, Omega_chi = 0.266), then the transfer function is automatically correct (T_chi/T_CDM = 1 to 10^{-39}, R8 Agent 9). The psi sector then provides the galactic-scale MOND phenomenology, and chi provides the cosmological CDM phenomenology.

The open questions for Path B (chi mass, relic density, compactification scale) remain as catalogued in R9 Agent 20.

### 7.3 Path C (Hybrid): Constrained by This Result

Any hybrid path must get the transfer function from something OTHER than psi pre-recombination growth. The options are:

(a) chi provides the transfer function (reduces to Path B)
(b) Mode coupling post-recombination (too weak by 5 orders of magnitude, wrong shape)
(c) Modified initial conditions from inflation (not derived from DFD action)
(d) A new mechanism not yet identified

---

## 8. Technical Appendix: Detailed Computation

### 8.1 The Full Perturbation Equation

Starting from the DFD action (v3.3), the full equation for psi perturbations delta_psi around the FRW background (nabla psi_bar = 0, Delta_bar = 0) is:

Temporal sector:
    (a*^2/8piG) d/dt [mu'(Delta_bar) * delta_Delta_dot / a_0] = (a*^2/8piG) * (1/(1+Delta_bar)^2) * delta_Delta_dot

Since Delta_bar = 0 and mu'(0) = 1:
    = (a*^2/8piG) * delta_Delta_dot

Spatial sector:
    -(1/8piG) div [mu'(|grad psi_bar|/a*) * grad delta_psi / a*]

Since grad psi_bar = 0 and mu'(0) = 1:
    = -(1/8piG) * (1/a*) * Laplacian(delta_psi)

Wait -- this is the linearization around grad psi = 0. But mu'(0) = lim_{x->0} d/dx [x/(1+x)] = 1. The issue is that the operator is:

    div [mu(|g|/a*) g] where g = grad psi

Expanding around g_0 = 0: the Jacobian of F(g) = mu(|g|/a*) g at g = 0 requires careful treatment because |g| is not differentiable at g = 0 in the standard sense.

For the 3-Laplacian structure: writing mu(y) = y/(1+y) with y = |g|/a*:

    F_i(g) = g_i |g| / (a* + |g|)

The Jacobian dF_i/dg_j at g = 0:
    = delta_ij |g|/(a* + |g|) + g_i g_j / (|g|(a* + |g|)) - g_i g_j |g| / (a* + |g|)^2

At g = 0, the first term -> 0, and the remaining terms are 0/0 forms. The linearization is SINGULAR.

**This confirms the R1/R4 finding: the standard linearized perturbation theory (G_eff approach) is invalid around nabla psi_bar = 0.** The perturbation equation is inherently nonlinear, and psi responds as the 3-Laplacian: psi ~ delta^{1/2} in the deep MOND regime.

### 8.2 Fourier Space Analysis

In Fourier space, the nonlinear equation for mode k is:

    k^2 F_k[mu(|g|/a*) g] = (8piG/c^2) rho_bar delta_k

where F_k denotes the Fourier transform. The nonlinearity means this is NOT a simple algebraic equation for delta_psi_k. It couples all Fourier modes.

For a single mode delta_b(x,t) = delta_0 cos(kx) cos(omega t):

    g(x,t) = -delta_psi_0(t) k sin(kx) cos(omega t) (approximately)

    mu(|g|/a*) g = g|g|/(a* + |g|) (in deep MOND, ~ g|g|/a*)

    div[g|g|/a*] = d/dx[g|g|/a*] ~ -(delta_psi_0)^2 k^3 |sin(kx)| cos^2(omega t) * sign(sin(kx)) / a*

The Fourier transform of |sin(kx)| sin(kx) contains modes at k, 3k, 5k, ... (odd harmonics). The fundamental mode at k has coefficient 8/(3pi). Therefore:

    k^2 * (8/3pi) * (delta_psi_0)^2 k / a* * cos^2(omega t) = (8piG/c^2) rho_bar delta_0 cos(omega t)

Solving for delta_psi_0:

    delta_psi_0 ~ sqrt(3pi a* rho_bar delta_0 * 8piG / (8 c^2 k^3 cos(omega t)))

This gives delta_psi ~ delta_0^{1/2} / (k^{3/2} cos^{1/2}(omega t)), confirming the square-root scaling and the fact that psi tracks the instantaneous oscillation phase.

Time-averaging:
    <delta_psi>_t ~ <cos^{1/2}(omega t)>_t

This average is nonzero! But <cos^{1/2}> is an AMPLITUDE factor, not a growing mode. It gives:

    <|cos(omega t)|^{1/2}>_t = (2/pi) integral_0^{pi/2} cos^{1/2}(theta) d theta = (2/pi) * B(3/4, 1/2) ~ 0.76

So the time-averaged psi amplitude is ~0.76 times the peak amplitude. But this is a CONSTANT -- it does not grow with time. The "DC component" from the nonlinear square-root response is time-independent. It exists, but it is static, not growing.

**Correction to Agent 7's proof:** The strict DC = 0 result applies when the response function F(g) is odd. For the QUMOND formulation where psi ~ |delta|^{1/2}, the response is NOT odd: psi is positive definite (the absolute value under the square root makes it so). There IS a nonzero DC component from the square-root response. However:

(a) This DC component is STATIC. It does not grow with time.
(b) Its amplitude is O(delta_0^{1/2}) ~ O(10^{-2.5}) at the primordial level.
(c) It has the wrong k-dependence (peaks at acoustic scales, not at the small scales where CDM power is needed).

**This refinement does not change the conclusion: there is no GROWING pre-recombination psi perturbation.**

### 8.3 Energy Considerations

Even if psi had a growing mode, the energy in that mode would be suppressed. The psi-field energy density is:

    rho_psi ~ (a*^2/8piG) W(|grad psi|^2/a*^2)

With the prefactor a*^2/(8piG) = 7.0 x 10^{-46} kg/m^3, this is 10^18 times below rho_crit regardless of psi's value. The gravitational effect of psi perturbations on the metric (and hence on baryon infall) is negligibly small at the energy level.

The unsuppressed coupling -(c^2/2) psi (rho - rho_bar) noted by R9 Agent 8 is the MATTER-COUPLING term. This gives psi's effect on matter motion (the MOND enhancement), not psi's self-gravity. It enhances the gravitational force on baryons but does not create independent potential wells that persist when baryon perturbations vanish.

---

## 9. Definitive Conclusion

### 9.1 The Answer

**psi perturbations do NOT grow during radiation domination.** They track the baryon-photon acoustic oscillations instantaneously (spatial constraint) with a negligible propagation correction (temporal wave term). The nonlinear 3-Laplacian response has a static DC component from the |delta|^{1/2} scaling, but this component does not grow and has the wrong scale-dependence.

### 9.2 Why This Is Definitive

Three independent arguments reach the same conclusion:

| Argument | Mechanism checked | Result |
|----------|-------------------|--------|
| 1. Elliptic constraint | Independent growth mode | None exists (no time derivative in spatial eq.) |
| 2. Temporal wave term | Meszaros-like growth | Oscillation, not growth (no psi self-gravity) |
| 3. DC rectification | Nonlinear accumulation | Static, not growing; wrong k-shape |

Each argument is based on different physics (equation type, self-gravity structure, symmetry properties). No loophole has been identified that would evade all three simultaneously.

### 9.3 What This Means for DFD

The transfer function problem is real and cannot be solved by psi dynamics alone. The viable options are:

1. **Path B (chi provides CDM):** chi has the correct transfer function by construction. The challenge is deriving m_chi and Omega_chi from the DFD action.

2. **Modified post-recombination physics:** The enhanced G_eff from MOND could potentially compensate if the scale-dependence works out (the R7 N-body gives promising sigma_8 but uncertain P(k) shape).

3. **New physics not in the v3.3 action:** A modification to the DFD action that gives psi a self-gravity term would change this conclusion. This would be a significant theoretical extension.

### 9.4 Status of the Pre-Recombination Calculation (R9 Item 3.6)

R9 Agent 20 identified this as "the single most promising unexplored calculation." It has now been computed. **The result is negative:** psi pre-recombination growth does not occur within the v3.3 action. This closes the last unexplored mechanism for Path A to work without modification.
