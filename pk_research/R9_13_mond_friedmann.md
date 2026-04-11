# R9 Agent 13: Does MOND-Enhanced Gravity Modify the Friedmann Equation?

## Executive Summary

**Question:** Can the MOND enhancement of gravity on cosmological scales enter the Friedmann equation, making H(z) look like it has Omega_m = 0.315 even with only baryons (Omega_b = 0.049)?

**Answer: NO, not through a simple G_eff replacement. But the question reveals a deeper structural insight about DFD cosmology.**

The Friedmann equation H^2 = (8piG/3)rho is a *geometric identity* (the 00-component of Einstein's equations, or equivalently the first integral of energy conservation in Newtonian cosmology). MOND/DFD modifications to inter-particle forces do not alter this kinematic relation. However, DFD has a completely different route to explaining the apparent Omega_m = 0.315: the psi-screen optical effect replaces dark energy, while the 3-Laplacian nonlinearity provides enhanced structure growth.

---

## 1. The Naive Proposal and Why It Fails

### 1.1 The Idea

Replace G with G_eff = G/mu in the Friedmann equation:

    H^2 = (8pi G_eff / 3) rho_b = (8piG / 3)(rho_b / mu)

If mu ~ 0.156 (i.e., G_eff/G ~ 6.4), then:

    rho_b,eff = rho_b / mu = 6.4 * 0.049 * rho_crit = 0.314 rho_crit

which would mimic Omega_m = 0.315.

### 1.2 Why This Fails: The Friedmann Equation is Kinematic

The Friedmann equation is derived from **energy conservation** (Newtonian) or the **00-component of Einstein's equations** (GR). It relates the expansion rate to the *total energy content* of the universe:

    H^2 = (8piG/3) rho_total - k/a^2

This is a **constraint equation**, not a dynamical equation of motion. It expresses the fact that the expansion kinetic energy equals the gravitational potential energy (plus curvature).

MOND modifies the *force law* between particles (the dynamical equations), but it does NOT modify the energy content of the universe. The total mass-energy is still rho_b (plus radiation, plus any cosmological constant). Making gravity stronger between particles does not create more energy.

**Analogy:** Making springs stiffer does not change the total mass of the spring system.

### 1.3 Specific Analysis for Different MOND Parameter Values

**Case 1: x_bar = cH/a_0 ~ 6 (transition regime)**

    mu_0 = 6/7 = 0.857
    G_eff/G = 1/mu_0 = 1.167
    Omega_m,eff = 1.167 * 0.049 = 0.057

Far too small. Even if the replacement were valid, the cosmological MOND parameter is too large (too close to Newtonian regime) to give the needed factor of 6.4.

**Case 2: x_bar = 0 (pure FRW, no background gradient)**

This is the correct DFD value for the FRW background (grad psi_bar = 0, as established by the R2 x-bar agent and confirmed by multiple agents in the synthesis). But mu(0) = 0 for mu(x) = x/(1+x), giving G_eff = G/0 -> infinity.

This is the linearization catastrophe identified by agents 7, 8, 11, 13: the DFD perturbation operator is degenerate at the FRW background. The resolution is that the perturbation equation is the 3-Laplacian, not a linearized equation.

**Neither case gives Omega_m = 0.315 via a simple G_eff replacement in Friedmann.**

---

## 2. What the v3.3 Paper Actually Does

### 2.1 The Paper's Approach: No Modified Friedmann Equation

The v3.3 cosmology section (Section 12) is carefully constructed to AVOID modifying the Friedmann equation. Instead:

1. **The psi-screen framework** treats GR/LCDM as a "reporting dictionary." H(z) is taken as an *input* from observations, not derived from a modified Friedmann equation.

2. **The background-history input** (Section 12, paragraph after Eq. 12.28) explicitly states: "H(a) is taken from the DFD observer dictionary / reconstructed screen background." The paper does NOT derive H(a) from first principles.

3. **The G_eff enters only the perturbation growth equation** (Eq. 12.27):

       delta'' + 2H delta' = 4pi G_eff rho_bar delta

   Here G_eff = G/[mu_0(1 + L_0(k.g)^2)] modifies the *growth of perturbations*, NOT the background expansion.

### 2.2 The Paper's Resolution: Three-Pronged Strategy

The v3.3 paper achieves apparent Omega_m = 0.315 through three distinct mechanisms:

| Mechanism | Replaces | How |
|-----------|----------|-----|
| Psi-screen | Dark energy | Optical distance bias: D_L^DFD = D_L^dict * exp(Delta_psi) |
| MOND/mu(x) | Dark matter (kinematics) | Enhanced gravity on galactic scales |
| Temporal dust branch | Dark matter (clustering) | Pressureless dust from S^3 composition law |

**None of these modify the Friedmann equation.** The expansion history matches LCDM by construction (the psi-screen is defined as the ratio D_L^LCDM/D_L^EdS).

---

## 3. Could a Modified Friedmann Equation Work in Principle?

### 3.1 Relativistic MOND Theories (Background)

Some relativistic extensions of MOND (TeVeS, BIMOND, Skordis-Zlosnik AeST) DO modify the Friedmann equation via additional fields. In AeST:

    H^2 = (8piG/3)(rho_matter + rho_vector)

where the vector field's energy density rho_vector acts as effective dark matter. However:

- This requires a vector field with specific dynamics
- DFD does NOT have a vector field -- it has a scalar psi
- The R2 Skordis agent showed that DFD's temporal sector CANNOT mimic Skordis-Zlosnik's vector field

### 3.2 The Temporal Conservation Law Kills Background Modification

The temporal conservation law (Appendix Q, Theorem: Dust branch):

    a^3 mu(Delta_bar) = const

where Delta_bar is the background temporal deviation. For the homogeneous background, Delta_bar = 0 by definition (psi_dot_0 IS the background rate). Therefore:

    a^3 mu(0) = a^3 * 0 = 0 = const

The temporal sector contributes ZERO energy density to the background. This was proven rigorously by Agent 12 and confirmed in the Final Synthesis: "This caps the background temporal psi-dust density at Omega < 10^{-11}."

**The temporal sector cannot modify the Friedmann equation at the background level.**

### 3.3 Could the Spatial mu(x) Modify Friedmann?

In DFD, the gravitational field equation is:

    div[mu(|grad psi|/a*) grad psi] = -(4piG/c^2) rho

On the FRW background, grad psi_bar = 0 (spatial homogeneity). The field equation becomes:

    mu(0) * Laplacian(psi_bar) = 0

which is trivially satisfied. There is NO background spatial psi-field to source a modified Friedmann equation.

**The spatial sector is trivial on the FRW background.**

---

## 4. The Correct Way to Think About This

### 4.1 DFD's Cosmological Architecture

DFD cosmology works through a fundamentally different architecture than LCDM:

**LCDM:**
- Friedmann equation: H^2 = (8piG/3)(rho_b + rho_CDM + rho_rad + rho_Lambda)
- Background expansion determined by total energy budget
- Perturbation growth follows from the same equation

**DFD:**
- Background expansion: OBSERVED H(z), interpreted through the psi-screen
- The apparent Omega_Lambda = 0.685 is an optical artifact (distance bias)
- The apparent Omega_CDM = 0.266 is a combination of MOND enhancement and possibly temporal dust branch effects
- Perturbation growth: driven by G_eff = G/mu, which is enormously enhanced (3-Laplacian nonlinearity)

### 4.2 What Is the ACTUAL DFD Background?

If DFD does not modify the Friedmann equation, what IS the actual background? There are two logically consistent possibilities:

**Possibility A: Einstein-de Sitter with psi-screen**

The actual universe has Omega_b = 0.049 and is geometrically open (Omega_total = 0.049 + Omega_rad). But ALL distance measurements are biased by the psi-screen, so the observed expansion history LOOKS like LCDM with Omega_m = 0.315 and Omega_Lambda = 0.685.

Problem: An open universe with Omega = 0.05 has very different dynamics from flat LCDM. The Friedmann equation gives:

    H^2 = H_0^2 [Omega_b/a^3 + Omega_rad/a^4 + (1 - Omega_b - Omega_rad)/a^2]

The curvature term (1 - 0.049)/a^2 dominates at z < 20. This universe would look NOTHING like LCDM.

The psi-screen can bias DISTANCES but it cannot change the actual expansion dynamics. So if H(z) follows LCDM, there must be additional energy content.

**Possibility B: Flat universe with Lambda + baryons**

The actual universe has Omega_b = 0.049 and Omega_Lambda = 0.685, giving:

    H^2 = H_0^2 [0.049/a^3 + Omega_rad/a^4 + 0.685]

This matches LCDM DISTANCE measurements, but gives Omega_m = 0.049 (not 0.315). The psi-screen doesn't help here because it only biases distances, and this universe already has the right distances.

But then Omega_m = 0.049, and ALL probes sensitive to matter clustering would see only baryons. This contradicts CMB, BAO, and P(k).

**Possibility C (the actual DFD stance): Dictionary agnosticism**

The v3.3 paper deliberately avoids committing to a specific background cosmology. It uses GR/LCDM as a "reporting dictionary" and focuses on the psi-screen as the reconstructed observable. The Friedmann equation is not derived or modified; it is treated as part of the dictionary.

This is operationally consistent but conceptually incomplete. A full DFD cosmology would need to specify what determines H(z).

---

## 5. Answering the Five Questions

### Q1: Does DFD modify the Friedmann equation?

**No.** The v3.3 paper does not derive or modify the Friedmann equation. H(a) is taken as an observational input. The theoretical reasons are:
- The Friedmann equation is a geometric/kinematic constraint, not a force law
- The spatial psi-field is trivial (grad psi_bar = 0) on the FRW background
- The temporal conservation law forces zero background psi-dust density
- MOND modifies forces, not energy content

### Q2: If yes, what is H^2(a) in DFD?

**Not applicable.** DFD does not have its own Friedmann equation. The closest analog is the temporal conservation law a^3 mu(Delta) = const, but this governs the temporal psi-sector, not the metric expansion.

### Q3: Does the MOND enhancement effectively increase Omega_m?

**For perturbation growth: YES. For background expansion: NO.**

The MOND enhancement enters through G_eff in the growth equation:

    delta'' + 2H delta' = 4pi G_eff rho_bar delta

This makes perturbations grow faster, as if there were more matter. But this does NOT change H(z).

Quantitatively, the EFE-limited enhancement gives G_eff/G = 1.17, yielding Omega_m,eff = 0.058 for growth. This is far short of 0.315.

Without EFE (x_bar = 0, 3-Laplacian regime), the enhancement is much larger: delta ~ a^3 instead of delta ~ a, yielding sigma_8 = 17.4 (21x overshoot). With parametric EFE regulation, the best fit gives sigma_8 = 0.53 (factor 1.5 short).

### Q4: Could H^2_DFD = (8piG/3)(nu_cosmo * rho_b + rho_rad + rho_Lambda)?

**No, for the reasons in Q1.** The MOND enhancement factor nu = 1/mu cannot be inserted into the Friedmann equation because:
1. The Friedmann equation constrains energy, not force
2. mu(x) = 0 at the FRW background (x_bar = 0), giving nu -> infinity
3. The temporal conservation law prevents background psi-dust

However, this form IS effectively what happens in the PERTURBATION growth equation (where nu enters through G_eff), just not in the background expansion.

### Q5: Could this explain both expansion history AND P(k) without the dust branch (chi)?

**No.** The expansion history and P(k) require different mechanisms in DFD:

- **Expansion history:** Explained by the psi-screen (optical distance bias). This is well-established in v3.3 and numerically consistent with data (Delta_psi(z=1) = 0.27).

- **P(k):** Requires enhanced structure growth. The 3-Laplacian nonlinearity provides this, but with the EFE giving sigma_8 = 0.53 (factor 1.5 short of LCDM). The gap could be closed by: psi-screen k-remapping (~x1.3), psi-field self-sourcing (~x1.2-1.5), or galaxy bias corrections (~x1.2).

The dust branch (temporal sector) was proposed as an additional source of clustering density, but the conservation law a^3 mu(Delta) = const kills it at the background level (Omega_psi-dust < 10^{-11}). The dust branch may still contribute to perturbative structure growth (perturbations of Delta could cluster), but this has not been computed.

---

## 6. A New Insight: The "Effective Omega_m" is Probe-Dependent

This analysis reveals that in DFD, what an observer infers as "Omega_m" depends on which probe is used:

| Probe | What it measures | DFD mechanism | Inferred Omega_m |
|-------|------------------|---------------|-----------------|
| SNe Ia (H(z)) | Distances | Psi-screen | 0.315 (by design) |
| CMB peak positions | theta_s = r_s/D_A | Psi-screen | 0.315 (by design) |
| CMB peak ratios | Baryon loading | BBN only | Omega_b = 0.049 |
| CMB damping tail | Omega_m h^2 | ??? | Open question |
| BAO D_V/r_s | Distances | Psi-screen | 0.315 (by design) |
| P(k) shape | Growth + transfer | 3-Laplacian + EFE | ~0.2 (gap remains) |
| f*sigma_8 | Growth rate | G_eff | 0.058 (large deficit) |
| Cluster masses | Virial theorem | mu(x) | ~0.98 (corrected) |
| Galaxy rotation | Force law | mu(x) | N/A (no DM needed) |

**The distance-based probes ALL give Omega_m = 0.315 by construction** (the psi-screen is defined to reproduce LCDM distances). The growth-based probes give different values depending on the effective MOND enhancement.

This probe-dependence is actually a PREDICTION of DFD: future precision measurements of growth-vs-geometry should show a systematic discrepancy. This is related to the well-known S_8 tension.

---

## 7. Connection to the P(k) Campaign

This analysis reinforces the Final Synthesis conclusion:

1. **The Friedmann equation is NOT the right place to look for DFD's cosmological effect.** The psi-screen handles distances; the 3-Laplacian handles growth.

2. **The sigma_8 gap (factor 1.5) is the real open problem.** Neither a modified Friedmann equation nor the temporal dust branch can close it at the background level.

3. **The most promising closure mechanisms remain:**
   - Psi-screen k-remapping of observed P(k) (~x1.3 boost)
   - Psi-field energy self-sourcing (~x1.2-1.5 boost)
   - Galaxy bias corrections in MOND (~x1.2 boost)
   - Combined: 1.3 * 1.3 * 1.2 ~ 2.0, sufficient to close the gap

4. **The "nu ~ 6.4" number is a red herring for the background** but meaningful for perturbations. The factor Omega_m/Omega_b = 6.4 is what the 3-Laplacian enhancement needs to effectively produce in the growth equation. With parametric EFE (f_EFE = 0), the current best sigma_8 = 0.53, needing a factor of 1.5 more -- which the psi-screen and self-sourcing corrections could plausibly provide.

---

## 8. Verdict

**The MOND enhancement does NOT enter the Friedmann equation.** The idea of replacing G -> G_eff in H^2 = (8piG/3)rho is physically wrong because the Friedmann equation constrains energy content, not gravitational force strength.

However, the underlying intuition is partially correct: the MOND enhancement DOES effectively increase the apparent matter content when observed through growth-sensitive probes. This happens through G_eff in the perturbation equation, not through a modified background expansion.

DFD cosmology works through a two-pronged strategy: psi-screen for distances (replacing dark energy), and 3-Laplacian growth enhancement for structure (replacing dark matter's clustering role). Neither requires modifying the Friedmann equation.

---

*R9 Agent 13 -- Analysis complete*
*Date: 2026-04-05*
