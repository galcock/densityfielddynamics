# R9 Agent 14: The DFD Friedmann Equation -- Derivation from the Action Principle

## Executive Summary

**DFD does NOT have its own Friedmann equation. The background expansion history H(z) is imported from GR/LCDM as a "dictionary" input, not derived from the DFD action.**

This is the single most important structural finding of this analysis. The v3.3 paper explicitly states that GR/LCDM enters "only as an observer dictionary" and that H(a) is "supplied" externally. The DFD action on flat Minkowski spacetime has no metric degree of freedom to vary, so there is no variational derivation of a Friedmann-type equation from S_DFD.

---

## Task 1: Equations of Motion from the DFD Action

### The complete DFD action (from section_formalism.tex)

```
S_DFD = S_psi + S_h + S_int + S_matter
```

where the scalar sector is:

```
S_psi = integral dt d^3x { (a*^2 / 8piG) [W(|grad psi|^2 / a*^2) + K(Delta)] - (c^2/2) psi (rho - rho_bar) }
```

### (a) Variation with respect to psi: Field equation

Varying S_psi with respect to psi yields the spatial field equation:

```
div[ mu(|grad psi| / a*) grad psi ] = -(8piG / c^2)(rho - rho_bar)
```

where mu(x) = W'(x^2) is the response function. This is the AQUAL-type equation governing gravitational dynamics. The temporal part, from the K(Delta) term, gives:

```
d/dt[ a^3 mu(Delta) ] = 0    (conservation law from shift symmetry)
```

with Delta = (c/a_0)|dot_psi - dot_psi_0| the temporal deviation invariant. This yields the "dust branch": w -> 0, c_s^2 -> 0.

### (b) Variation with respect to a(t): NO SUCH VARIATION EXISTS

**This is the critical point.** In GR, the Friedmann equation arises from varying the Einstein-Hilbert action with respect to the metric component g_00 (or equivalently the scale factor a(t) in the FRW ansatz). In DFD:

- The theory is formulated on **flat Minkowski spacetime** (R^3 with refractive index n = e^psi)
- The scale factor a(t) is **not a dynamical variable** in the DFD action
- There is no metric degree of freedom to vary
- The action S_DFD contains exactly 1 scalar DOF (psi) and 2 tensor DOFs (h_ij^TT)

**Therefore, there is no DFD Friedmann equation derivable from the action principle.**

### (c) Variation with respect to matter fields: Standard EOM

Matter couples to the physical metric:

```
g_tilde_munu = diag(-c^2 e^{-psi}, e^{+psi}, e^{+psi}, e^{+psi})
```

In the non-relativistic limit, test particles obey:

```
d^2 x / dt^2 = (c^2/2) grad psi
```

This is the standard geodesic equation in the optical metric.

---

## Task 2: How Does a(t) Enter the DFD Action?

### Where a(t) appears

The scale factor a(t) enters the DFD action in **two places**, both as external inputs:

1. **The volume element**: d^3x = a^3(t) d^3x_comoving in FRW coordinates. This is a coordinate choice, not a dynamical variable.

2. **The background density**: rho_bar(t) = rho_bar_0 / a^3(t), which dilutes with expansion.

3. **The temporal deviation invariant**: Delta = (c/a_0)|dot_psi - dot_psi_0|, where psi_0 is the background screen field -- itself determined by the background expansion.

### What determines a(t)?

In v3.3, a(t) is **NOT** determined by psi. The relationship is inverted:

- The "observer dictionary" provides H(a) from LCDM
- The psi-screen provides optical corrections to distances measured by observers
- The background psi_bar(t) is related to the screen: Delta_psi = psi_em - psi_obs

The paper does NOT establish the relation a(t) proportional to exp(psi_bar(t)/2) or any other dynamical link. Instead, a(t) is imported from external cosmology.

### Could a(t) be derived from psi?

In principle, if DFD on flat spacetime encodes "expansion" entirely through psi, one would need:

```
H_eff = (c/2) d(psi_bar)/dt    [NOT stated in v3.3]
```

But this equation does not appear in the paper. The temporal conservation law d/dt[a^3 mu(Delta)] = 0 uses a(t) as an input, not an output.

---

## Task 3: What Does v3.3 Actually Do?

### Answer: Option (c) -- H(z) from the psi-screen reinterpretation, with LCDM as "dictionary"

The key passages from section_cosmology.tex:

**Line 9** (opening statement): "DFD cosmology is treated as an inverse optical problem: infer the line-of-sight optical bias field directly from data, and only then interpret what standard cosmology would call 'expansion history,' 'dark energy,' and 'dark matter.' In this framing, GR/LCDM enters only as an observer dictionary (how distances/angles are commonly reported), not as ontology."

**Line 23**: "All GR/LCDM quantities used in this section (e.g. D_L^dict, D_A^obs) are reporting-layer variables that serve as a convenient dictionary for published datasets."

**Lines 569-581** (the psi-screen reconstruction):
```
D_L(Omega_m, Omega_Lambda) / D_L(Omega_m=1, Omega_Lambda=0) = function of z only

Delta_psi(z) = ln(D_L^obs(z) / D_L^matter(z)) = ln(D_L^LCDM(z) / D_L^matter(z))
```
"since observations are well-fit by LCDM. This is an H_0-independent reconstruction."

**Line 585**: "Computing Eq.(psi-reconstruction) with Omega_m = 0.3 (matter-only baseline: Omega_m = 1)"

**Lines 731-732** (the smoking gun): "Equations (perturb-fourier)--(G-eff) describe the linear response of perturbations once a background history H(a) is supplied. In the present monograph, H(a) is taken from the DFD observer dictionary / reconstructed screen background already used throughout Sec.(cosmology)."

### The logical structure is:

1. **Start with LCDM as "dictionary"**: Use LCDM distances D_L^LCDM(z) as the reporting framework
2. **Define a matter-only baseline**: D_L^matter(z) with Omega_m = 1 (Einstein-de Sitter)
3. **The psi-screen IS the difference**: Delta_psi(z) = ln(D_L^LCDM / D_L^matter)
4. **Supply H(a) from the dictionary** for the perturbation equations
5. **Claim**: What LCDM attributes to dark energy is "really" the psi-screen optical bias

### What v3.3 does NOT do:

- Does NOT derive H(z) from the DFD action
- Does NOT derive the Friedmann equation from psi dynamics
- Does NOT specify what Omega_m value enters the background H(a) -- it says "Omega_m = 0.3" in one place (the LCDM dictionary) and "Omega_m = 1" as the matter-only baseline
- Does NOT explain what matter content (baryons only? baryons + CDM?) drives the actual background expansion

---

## Task 4: Critical Implications for P(k)

### The Omega_m ambiguity

This is the most consequential issue. The paper uses two different matter contents:

| Context | Matter content | Source |
|---------|---------------|--------|
| psi-screen reconstruction | Omega_m = 0.3 (LCDM) vs Omega_m = 1 (matter-only) | Eq. (psi-reconstruction) |
| N-body proof-of-concept | Omega_b = 0.049 (baryons only) | Line 691-692 |
| Growth equation | "H(a) is supplied" from dictionary | Line 732 |
| CMB peak ratio | Baryon loading R_b from BBN only | Line 477 |

**There is no consistent answer to the question: "What is the matter content of the DFD universe?"**

### If the true DFD universe has only baryons (Omega_b = 0.049):

- The background expansion is Einstein-de Sitter with Omega_b = 0.049 << 1
- This is an **open universe** with curvature Omega_k = 0.951
- H(z) is dramatically different from LCDM
- The psi-screen would need to correct not just distances but the ENTIRE expansion history
- The growth equation with only baryonic matter and mu-enhanced gravity must reproduce P(k)
- This is the scenario the N-body simulation tests -- and it overshoots by 5.4x (before EFE)

### If the DFD universe has Omega_m = 0.3 (including some CDM-like component):

- The chi field from the b_3 parameter could provide the CDM component
- The temporal dust branch (w -> 0, c_s^2 -> 0) provides exactly this
- H(z) would be close to LCDM automatically
- P(k) matching becomes much easier

### The paper's implicit position:

The paper tries to have it both ways:
1. Claims "no dark matter required" for galactic dynamics (mu function handles rotation curves)
2. Claims the dust branch from temporal completion provides CDM-like clustering
3. Uses LCDM H(a) as "dictionary" without specifying whether CDM is ontologically real

The cleanest reading is: **DFD replaces CDM particles with the psi temporal dust branch**, which has the same equation of state (w=0, c_s^2=0) and therefore produces the same background expansion and linear growth. If so, then:

- The "Friedmann equation" is just the standard one with Omega_m = 0.3, where 0.25 of that comes from the psi dust branch
- H(z) is standard LCDM
- P(k) matching reduces to showing the psi dust branch clusters identically to CDM

### But this creates a tension:

If the psi dust branch IS the dark matter, then:
- It should appear in the stress-energy tensor on the RHS of the Friedmann equation
- rho_psi ~ (a*^2 / 8piG) K(Delta) must equal 0.25 rho_crit
- This requires Delta ~ O(1) cosmologically, meaning |dot_psi - dot_psi_0| ~ a_0/c

Is this consistent? Let's check:
- a_0/c ~ 4 x 10^{-19} s^{-1}
- H_0 ~ 2.3 x 10^{-18} s^{-1}
- So Delta ~ O(0.2) -- marginal, in the transition regime

The paper does NOT perform this self-consistency check.

---

## Conclusions

### Finding 1: No DFD Friedmann equation exists
DFD on flat spacetime has no metric DOF. The Friedmann equation cannot be derived from the DFD action. H(z) is imported from LCDM as a "dictionary."

### Finding 2: The background is underdetermined
The paper does not specify what matter content drives the actual background expansion. It uses Omega_m = 0.3 from LCDM in some places and Omega_b = 0.049 (baryons only) in others.

### Finding 3: The dust branch may resolve this -- but it's not demonstrated
The temporal completion theorem proves w -> 0, c_s^2 -> 0, which is the necessary condition for the psi field to act as CDM. But the paper does not compute rho_psi to verify it matches the required Omega_CDM = 0.25.

### Finding 4: For P(k), this matters enormously
If H(z) comes from LCDM with Omega_m = 0.3 (including psi dust as CDM-equivalent), then the P(k) shape depends primarily on whether the psi dust branch clusters with the same transfer function as CDM. This is stated as a "program item."

If H(z) comes from baryons only (Omega_b = 0.049), the expansion history is completely wrong and P(k) cannot possibly match observations, regardless of mu-enhanced growth.

### Recommendation for the P(k) program:
The first priority must be establishing what H(z) DFD actually predicts. The three options are:

1. **Import LCDM H(z) as dictionary** (current approach): Then P(k) work reduces to showing the psi perturbation transfer function matches CDM. Achievable but not a prediction.

2. **Derive H(z) from psi dust branch + baryons**: Requires computing rho_psi(a) self-consistently and showing Omega_psi ~ 0.25. This would be a genuine prediction. The conservation law a^3 mu(Delta) = const provides the scaling; the question is the normalization.

3. **Baryon-only expansion + psi-screen optical corrections**: The most radical option. Would require the psi-screen to correct not just distances but the entire expansion phenomenology. Almost certainly fails for P(k).

Option 2 is the scientifically correct path and should be pursued.

---

## Key Equations Summary

| Equation | Source | Role |
|----------|--------|------|
| div[mu grad psi] = -(8piG/c^2)(rho - rho_bar) | Vary S_psi w.r.t. psi | Spatial field equation |
| d/dt[a^3 mu(Delta)] = 0 | Shift symmetry of K(Delta) | Temporal conservation |
| w -> 0, c_s^2 -> 0 | Dust branch theorem | psi behaves as CDM |
| Delta_psi(z) = ln(D_L^LCDM / D_L^matter) | psi-screen reconstruction | Optical bias = "dark energy" |
| G_eff = G / [mu_0(1 + L_0 (k_hat . g_hat)^2)] | Linear perturbation | Growth enhancement |
| H(a) = "supplied from dictionary" | Line 732 | Background is external input |

---

*R9 Agent 14, 2026-04-05*
*Analysis of DFD v3.3 (section_formalism.tex, section_cosmology.tex, appendix_Q_temporal_completion.tex)*
