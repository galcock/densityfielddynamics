# R4 Agent: Verbatim Quote Log -- v3.3 Paper EFE/Cosmological Statements

## Purpose

Systematically catalog every statement in the v3.3 paper about the cosmological External Field Effect, the background gradient, and the perturbation skeleton, classifying each as THEOREM, CLAIM, ANALOGY, or PROGRAM ITEM.

---

## 1. COSMOLOGICAL EFE: THE N-BODY PARAGRAPH (section_cosmology.tex, lines 689--706)

### Quote 1a: The N-body result and its deficit

> "A particle-mesh simulation (64^3 grid, 200 Mpc/h box) comparing Lambda-CDM (Omega_m = 0.30), Newtonian-baryons (Omega_b = 0.049), and DFD-baryons (Omega_b = 0.049, mu(x) = x/(1+x)) on identical initial conditions demonstrates the key point: Newtonian-baryons produces negligible structure (delta_rms = 1.5 x 10^{-4}), confirming the standard objection; DFD produces 43.8x more structure (delta_rms = 6.4 x 10^{-3}), establishing that nonlinear gravity overcomes the baryonic deficit."

**Classification:** CLAIM (numerical result stated, but the simulation is described as "proof-of-concept" not a theorem)

**Assumptions:** Particle-mesh at 64^3; no temporal sector; pure spatial AQUAL operator; no EFE included.

**EFE entry point:** NONE -- the N-body simulation does NOT include the EFE. This is explicitly stated next.

### Quote 1b: The overshoot and the cosmological EFE claim

> "The 5.4x overshoot relative to Lambda-CDM is physically expected: cosmological perturbation accelerations (x approx 4 x 10^{-4}) lie deep in the MOND regime where the raw mu-function enhances gravity by ~400x without the cosmological External Field Effect (EFE) from the Hubble flow (a_ext ~ cH_0 approx 6 a_0). With the EFE, the effective enhancement drops from ~400 to ~1.2, which should bring DFD into quantitative agreement."

**Classification:** CLAIM (stated without derivation; "should bring" is aspirational language)

**Key content:** This is the ONLY place in the paper where the cosmological EFE magnitude is stated numerically. The claim is:
- a_ext ~ cH_0 (the Hubble flow acceleration)
- cH_0 approx 6 a_0
- With EFE, enhancement drops from ~400x to ~1.2x

**Assumptions:**
1. The Hubble flow provides a SPATIAL gradient nabla psi_bar that acts as an external field
2. The value a_ext ~ cH_0 is stated BY ANALOGY with the galactic EFE (Appendix V), not derived from the action
3. The factor "6 a_0" uses a_0 = 2 sqrt(alpha) cH_0, giving cH_0/a_0 = 1/(2 sqrt(alpha)) approx 6

**EFE entry point:** SPATIAL gradient -- the claim is that the Hubble flow produces a background nabla psi_bar.

**CRITICAL NOTE:** The paper does NOT derive x_bar = cH_0/a_0 from the cosmological action or from the temporal sector. It is stated by dimensional analysis / analogy.

### Quote 1c: Program status

> "This is a proof-of-concept at 64^3 resolution; production-quality results require >= 256^3 with the EFE implemented."

**Classification:** PROGRAM ITEM (explicitly acknowledged as incomplete)

---

## 2. THE PERTURBATION SKELETON (section_cosmology.tex, lines 708--729)

### Quote 2a: The linearization

> "The dust-branch theorem provides the equation of state; what remains is the growth operator. Linearizing the DFD field equation around a background psi_bar in Fourier space gives
> k_i M_{ij} k_j delta_psi_k = -(8 pi G / c^2) rho_bar delta_k,  [Eq. 12.25]
> with the response tensor
> M_{ij} = mu_0 delta_{ij} + L_0 g_hat_i g_hat_j,  [Eq. 12.26]
> where mu_0 := mu(x_bar), L_0 := d mu / d ln x |_{x_bar}, g_hat := nabla psi_bar / |nabla psi_bar|."

**Classification:** THEOREM (this is a standard linearization of the AQUAL operator; mathematically correct given a nonzero nabla psi_bar)

**CRITICAL ASSUMPTION:** The entire perturbation skeleton ASSUMES nabla psi_bar != 0. The direction g_hat = nabla psi_bar / |nabla psi_bar| is UNDEFINED when nabla psi_bar = 0.

**EFE entry point:** SPATIAL gradient. The background gradient nabla psi_bar enters as the direction g_hat in the anisotropic response tensor M_{ij}.

### Quote 2b: The growth equation and G_eff

> "The linear growth equation is then
> delta_k_ddot + 2H delta_k_dot = 4 pi G_eff(a, k_hat) rho_bar delta_k,  [Eq. 12.27]
> with direction-dependent effective gravitational coupling
> G_eff(a, k_hat) = G / [mu_0 (1 + L_0 (k_hat . g_hat)^2)].  [Eq. 12.28, boxed]"

**Classification:** THEOREM (follows from Eq. 12.25-12.26 by standard manipulations)

**Key property:** G_eff is ANISOTROPIC -- it depends on k_hat . g_hat, the angle between the wavevector and the background gradient direction.

### Quote 2c: Asymptotic limits

> "For mu(x) = x/(1+x): mu_0 = x_bar/(1+x_bar) and L_0 = 1/(1+x_bar)^2. On cosmological scales (x_bar << 1), G_eff -> G/x_bar, enhancing growth; on small scales (x_bar >> 1), G_eff -> G, recovering standard gravity."

**Classification:** THEOREM (algebraic consequence of the mu function)

**CRITICAL NOTE:** When x_bar << 1 (deep MOND regime with no EFE), G_eff -> G/x_bar ~ 400G. When x_bar ~ cH_0/a_0 ~ 6, G_eff -> G/[6/(1+6) * (1 + ...)] ~ 1.2G. But x_bar ~ 6 is CLAIMED, not derived.

---

## 3. WHAT HAPPENS AT nabla psi_bar = 0?

### The paper's silence

The paper NEVER explicitly addresses the case nabla psi_bar = 0 in the perturbation skeleton. When nabla psi_bar = 0:
- g_hat is undefined
- M_{ij} = mu(0) delta_{ij} + L_0 * (undefined)
- mu(0) = 0 for mu(x) = x/(1+x)
- The perturbation equation becomes SINGULAR: k^2 * 0 * delta_psi = source

This is the self-consistent perturbation problem: in a perfectly homogeneous cosmology with no background gradient, the AQUAL operator degenerates and provides NO gravitational response at linear order.

**Classification of the silence:** This is an IMPLICIT ASSUMPTION -- the paper assumes nabla psi_bar != 0 without discussing the alternative.

---

## 4. THE TEMPORAL EFE (appendix_Q_temporal_completion.tex and section_cosmology.tex)

### Quote 4a: Temporal deviation invariance theorem

> "Assume the saturation-union composition law... Then for any background psi_0 and deviation Delta psi,
> mu(psi_0 + Delta psi) - mu(psi_0) = (1 - mu(psi_0)) mu(Delta psi)  [Eq. Q.4, boxed]"
> (Label: eq:temporal-EFE-Q)

**Classification:** THEOREM (proved from the saturation-union law; Theorem Q.1)

**Note:** The label "temporal-EFE" is used, indicating the authors view this as the temporal analog of the spatial EFE.

**EFE entry point:** TEMPORAL sector. This is about psi_0 (background temporal value), not nabla psi_bar (spatial gradient).

### Quote 4b: The temporal deviation invariant

> "Delta := (c/a_0) |psi_dot - psi_dot_0|  [Eq. Q.6]
> Here a_0 = 2 sqrt(alpha) cH_0 is the MOND acceleration scale; the combination c/a_0 has units of time, so Delta is dimensionless."

**Classification:** THEOREM (Definition + uniqueness theorem Q.2, proved from segment additivity + reference invariance)

**EFE entry point:** TEMPORAL sector. Delta measures deviation of the time derivative from the background.

### Quote 4c: Dust branch theorem

> "In a homogeneous FRW dictionary with u^mu = (1,0,0,0), solutions near the screen background satisfy:
> a^3 mu(Delta) = const, Delta propto a^{-3} (Delta << 1),  [Eq. Q.11]
> and their effective equation of state and sound speed obey
> w := p/rho -> 0, c_s^2 -> 0 as Delta -> 0.  [Eq. Q.12, boxed]"

**Classification:** THEOREM (Theorem Q.4, fully proved from the deviation-invariant closure)

**Key assumption:** Homogeneous FRW background. This is the TEMPORAL sector only -- no spatial perturbations.

### Quote 4d: Temporal-EFE in the main cosmology section

> "mu(psi_0 + Delta psi) - mu(psi_0) = (1 - mu(psi_0)) mu(Delta psi)  [Eq. 12.22]
> This is the temporal External Field Effect---a direct consequence of the saturation-union composition law"

**Classification:** THEOREM (restated from Appendix Q)

---

## 5. THE "PROGRAM" BOX IN APPENDIX Q (lines 196--204)

### Quote 5a: Theorem-grade results box

> "Proved from S^3 composition law + deviation invariance:
> 1. Temporal deviation invariance (Theorem Q.1)
> 2. Unique temporal segment scalar Delta = (c/a_0)|psi_dot - psi_dot_0| (Theorem Q.2)
> 3. K'(Delta) = mu(Delta) closure (same mu as spatial sector)
> 4. Dust branch: w -> 0, c_s^2 -> 0 as Delta -> 0 (Theorem Q.4)
> 5. No-go: Quadratic K'(Q_t) = mu(sqrt(Q_t)) gives w -> 1/2 (Lemma Q.3)"

**Classification:** THEOREM (self-classification by paper; verified by reading proofs)

### Quote 5b: Program-level items box

> "Requires further work:
> - Full P(k) shape matching Lambda-CDM (linear perturbation analysis)
> - Transfer function derivation in DFD dictionary
> - Quantitative confrontation with survey data (noting GR-sandbox / fiducial-processing issues)
> The dust branch (w -> 0, c_s^2 -> 0) is the necessary condition for CDM-like linear growth; proving the full P(k) match is a program item."

**Classification:** PROGRAM ITEM (self-classification by paper)

---

## 6. OPEN PROBLEMS TABLE (section_openproblems.tex)

### Quote 6a: P(k) entry in summary table

> "P(k) full match | Program | Dust branch proved (Thm. dust-branch); numerical pipeline in development | Mechanism"

**Classification:** PROGRAM ITEM (explicitly listed as "Program" status, resolution is "Mechanism" only)

### Quote 6b: Claim-status level F

> "[F] Open program item: first-principles derivation of the species-class map from CP^2 x S^3, full production P(k)/Boltzmann-level cosmology pipeline, narrowing of the nuclear-clock prediction band beyond the stated benchmark."

**Classification:** PROGRAM ITEM (P(k)/Boltzmann pipeline is listed as one of the open F-level items)

### Quote 6c: Dust branch in summary table

> "Dust branch (w -> 0) | Technical | K'(Delta) = mu(Delta) (Appendix temporal-completion) | Thm."

**Classification:** THEOREM (self-classification)

---

## 7. P(k) CONFRONTATION SECTION (section_Pk_confrontation.tex)

### Quote 7a: Growth rate claim

> "In DFD, the growth rate is:
> f_DFD(z) = Omega_m(z)^gamma [1 + O(k_alpha)]  [Eq. in Sec. 12]
> where gamma approx 0.55 and the psi-field correction is O(k_alpha) approx 10^{-5}, far below current measurement precision. Consequently, DFD and Lambda-CDM predict indistinguishable linear growth at current multipole precision at the scales probed by P(k) multipoles."

**Classification:** CLAIM (the formula f_DFD = Omega_m^gamma is stated without derivation; the growth index gamma = 0.55 is the standard GR value and no DFD-specific derivation is given)

**CRITICAL NOTE:** This claim ASSUMES the EFE has already been applied to set x_bar ~ 6, so that G_eff ~ 1.2G. Without the EFE (x_bar ~ 10^{-4}), the growth rate would be enormously enhanced and completely inconsistent with data.

### Quote 7b: Status statement

> "Status: consistency check completed at the level of linear multipole data products. DFD is consistent with the quoted BOSS DR12 and eBOSS DR16 multipole measurements within the stated systematic uncertainties. This should be read as an initial data-level consistency check, not as a claim that the full production-level P(k)/Boltzmann pipeline is already closed."

**Classification:** Honest self-assessment. The paper explicitly does NOT claim the P(k) problem is solved.

---

## 8. N-BODY SIMULATION: DOES IT INCLUDE THE TEMPORAL SECTOR?

### Answer: NO.

The N-body simulation (section_cosmology.tex, lines 689--706) is described as:
- "particle-mesh simulation (64^3 grid, 200 Mpc/h box)"
- Uses "mu(x) = x/(1+x)" -- this is the SPATIAL AQUAL operator
- No mention of the temporal deviation invariant Delta
- No mention of K(Delta) or the dust branch Lagrangian
- The overshoot is attributed to the ABSENCE of the cosmological EFE

The temporal sector (Appendix Q) provides the dust branch equation of state (w -> 0, c_s^2 -> 0), but this is a SEPARATE result about homogeneous background evolution, not about the N-body perturbation dynamics.

**Classification:** The N-body simulation is a SPATIAL-ONLY proof-of-concept that does not include either the temporal sector or the cosmological EFE.

---

## 9. KEY QUESTIONS ANSWERED

### Q1: Does the paper derive x_bar = cH_0/a_0 from the action? Or state it by analogy?

**ANSWER: BY ANALOGY / DIMENSIONAL ANALYSIS.** The paper states "a_ext ~ cH_0 approx 6 a_0" in the N-body discussion (line 702) without derivation. The value comes from identifying the Hubble flow acceleration cH_0 as the "external field" by analogy with the galactic EFE. No variational or action-based derivation connects the cosmological expansion to a spatial gradient nabla psi_bar.

### Q2: Does the perturbation skeleton (Eqs. 12.25-12.28) assume a nonzero nabla psi_bar?

**ANSWER: YES, NECESSARILY.** The response tensor M_{ij} = mu_0 delta_{ij} + L_0 g_hat_i g_hat_j requires g_hat = nabla psi_bar / |nabla psi_bar|, which is undefined at nabla psi_bar = 0. Furthermore, mu_0 = mu(x_bar) = 0 when x_bar = 0, making the entire operator degenerate. The skeleton is structurally dependent on a nonzero background gradient.

### Q3: Does the N-body simulation include the temporal sector?

**ANSWER: NO.** The simulation uses only the spatial AQUAL operator mu(|nabla psi|/a_star). The temporal deviation invariant Delta, the dust branch Lagrangian L_temp, and the K(Delta) closure are not implemented.

### Q4: What does the paper say about the self-consistent perturbation equation at nabla psi_bar = 0?

**ANSWER: NOTHING.** The paper does not discuss this case. It implicitly assumes nabla psi_bar != 0 throughout the perturbation skeleton. The singularity of the linearized operator at nabla psi_bar = 0 is not addressed.

---

## 10. SUMMARY TABLE

| Item | Classification | Sector | Derived from action? | Status |
|------|---------------|--------|---------------------|--------|
| Dust branch w -> 0, c_s^2 -> 0 | THEOREM | Temporal | Yes (Appendix Q) | Proved |
| Temporal deviation invariance | THEOREM | Temporal | Yes (composition law) | Proved |
| No-go: quadratic gives w = 1/2 | THEOREM | Temporal | Yes | Proved |
| Perturbation skeleton Eqs. 12.25-12.28 | THEOREM | Spatial | Yes (given nabla psi_bar != 0) | Proved conditionally |
| G_eff = G/[mu_0(1+L_0 cos^2 theta)] | THEOREM | Spatial | Yes (given nabla psi_bar != 0) | Proved conditionally |
| a_ext ~ cH_0 approx 6 a_0 | CLAIM | Spatial | NO -- by analogy | Not derived |
| Enhancement drops from ~400x to ~1.2x | CLAIM | Spatial | NO -- requires a_ext claim | Not derived |
| f_DFD = Omega_m^gamma with gamma = 0.55 | CLAIM | Mixed | NO -- assumes EFE value | Not derived |
| Full P(k) match | PROGRAM ITEM | Both | Not attempted | Open |
| Transfer function | PROGRAM ITEM | Both | Not attempted | Open |
| Survey-pipeline confrontation | PROGRAM ITEM | Both | Not attempted | Open |
| N-body with EFE | PROGRAM ITEM | Spatial | Not implemented | Open |

---

## 11. THE CRITICAL GAP

The paper has a theorem-grade temporal sector (dust branch) and a conditional spatial perturbation skeleton, but these are joined by a CLAIM (not a derivation) that the Hubble flow provides a_ext ~ cH_0. This claim is the load-bearing bridge between the temporal dust result and the spatial perturbation result. Without it:
- The temporal sector gives w -> 0, c_s^2 -> 0 (good for CDM-like behavior)
- The spatial sector at nabla psi_bar = 0 gives a DEGENERATE operator (no gravitational response)
- The spatial sector at nabla psi_bar != 0 gives anisotropic G_eff (good, but needs the value of x_bar)

The paper is honest about this: P(k) is listed as a "Program" item, not a theorem. The dust branch is the "necessary condition" for CDM-like growth; the sufficient condition requires closing the x_bar gap.

---

*Generated by R4 agent, 2026-04-05*
