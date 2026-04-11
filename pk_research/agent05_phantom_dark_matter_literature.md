# Agent 05: Phantom Dark Matter in MOND -- Literature Research

## Executive Summary

Phantom dark matter (PDM) is the fictitious dark matter density that emerges when interpreting MOND gravitational dynamics through a Newtonian lens. It is not an independent field -- it is the baryon distribution processed through the nonlinear MOND interpolation function. This document surveys all key papers on PDM, its formulas, spatial distribution, cosmological implications, and the critical open question of what happens at nodes of baryon acoustic oscillations.

---

## 1. Milgrom's Phantom Dark Matter: Formulas and Derivations

### 1.1 Origin: Milgrom (1986)

Milgrom (1986b) first introduced the concept of "phantom mass density." The idea: in MOND, the modified Poisson equation produces gravitational fields stronger than Newtonian for a given baryon distribution. If one interprets the resulting gravitational field through standard Newtonian gravity, one infers the existence of additional "dark" mass -- the phantom dark matter.

### 1.2 AQUAL Formulation (Bekenstein & Milgrom 1984)

In AQUAL (A QUAdratic Lagrangian), the MOND field equation is:

```
nabla . [mu(|nabla Phi|/a_0) nabla Phi] = 4 pi G rho_b
```

where mu(x) is the interpolation function with mu(x) -> 1 for x >> 1 (Newtonian) and mu(x) -> x for x << 1 (deep MOND).

The phantom density in AQUAL is derived by computing the Laplacian of the full MOND potential and subtracting the baryonic source:

```
rho_ph^AQUAL = (1/4piG) nabla^2 Phi - rho_b
            = -(1/4piG) nabla . [chi(|nabla Phi|/a_0) nabla Phi]
```

where chi = mu - 1 (so chi -> 0 in Newtonian limit, chi -> -1 + |nabla Phi|/a_0 in deep MOND).

**Key difficulty**: In AQUAL, you must first solve the full nonlinear MOND equation to find Phi before computing rho_ph.

### 1.3 QUMOND Formulation (Milgrom 2010)

Milgrom (2010) constructed QUMOND (quasi-linear MOND), which is far more tractable. The procedure:

1. Solve the standard Poisson equation for the Newtonian potential: nabla^2 Phi_N = 4 pi G rho_b
2. Compute the MOND potential algebraically: g = nu(|g_N|/a_0) g_N, where g_N = -nabla Phi_N
3. The phantom dark matter density is:

```
rho_ph^QUMOND = (1/4piG) nabla . [nu_bar(|nabla Phi_N|/a_0) nabla Phi_N]
```

where nu_bar = nu - 1 and nu(y) is the QUMOND interpolation function.

**Critical advantage**: In QUMOND, the phantom density is determined entirely by the Newtonian potential of the baryons. No nonlinear PDE needs to be solved -- only linear Poisson equations with nonlinear algebraic steps between them.

### 1.4 The nu Interpolation Function

The function nu relates the actual MOND acceleration to the Newtonian acceleration:

```
a = nu(a_N/a_0) * a_N
```

Limiting behavior:
- **Newtonian limit** (a_N >> a_0): nu(y) -> 1, so nu_bar -> 0, no phantom dark matter
- **Deep-MOND limit** (a_N << a_0): nu(y) -> 1/sqrt(y), so nu_bar -> 1/sqrt(y) - 1 ~ 1/sqrt(y) >> 1

Common "simple" interpolation function: nu(y) = [1 + sqrt(1 + 4/y)] / 2

### 1.5 Deep-MOND Limit: Point Source

For a spherically symmetric point mass M in the deep-MOND limit:

```
rho_ph = M / (4 pi r^2 r_M)
```

where r_M = sqrt(GM/a_0) is the MOND characteristic radius. This gives an isothermal-like r^{-2} profile -- "centred on the mass, but diffuse" -- which naturally explains the pseudo-isothermal dark matter halos inferred around galaxies.

---

## 2. Spatial Distribution of Phantom Dark Matter

### 2.1 In Galaxies

**Llinares et al. / Structure of ENS (Equivalent Newtonian Systems)**:
- Phantom dark matter follows a generalized profile: rho(r) = rho_alpha * r_alpha^2 / [r^alpha (r^2 + r_alpha^2)^{(2-alpha)/2}]
- Cored stellar distributions produce weak cusps in PDM (alpha <= 1)
- Cuspy stellar distributions produce cored or depleted PDM halos
- Diffuse systems in the deep-MOND regime show weak cusps with slopes around alpha ~ -1/2
- This offers a natural resolution to the core-cusp problem: "the core-cusp problem could be a MOND artefact"

**Key result**: PDM is always MORE EXTENDED than the baryon distribution. In the deep-MOND limit, rho_ph ~ r^{-2} extends well beyond the baryonic scale radius, mimicking dark matter halos.

### 2.2 In Dwarf Spheroidals (Bilek et al. 2020)

Bilek et al. (2020) computed the PDM distribution in eight classical dwarf spheroidal satellites of the Milky Way:
- The external field effect (EFE) of the Milky Way heavily shapes the PDM distribution
- For EFE-dominated dwarfs: PDM peak is offset 0.1-0.2 kpc from the stellar center
- PDM can be NEGATIVE in certain directions (cones perpendicular to external field)
- Negative PDM density is a unique MOND signature with no CDM analogue

### 2.3 In Galaxy Clusters

**Pointecouteau & Silk (2005)**: Using XMM X-ray data for 8 clusters:
- MOND reduces the mass discrepancy by factor ~1.6 at half the virial radius
- But MOND dynamical mass / baryonic mass = 4.94 +/- 0.50 in outer parts
- Galaxy clusters STILL need additional mass in MOND -- the "residual missing mass problem"
- The PDM profile in clusters shows an inner core and outer r^{-4} decline

**Milgrom & Sanders (2008)** -- "Rings and Shells of Dark Matter as MOND Artifacts":
- A mass within its MOND transition radius exhibits phantom shells/rings in the PDM distribution
- NO corresponding feature exists in the true baryon distribution
- They proposed this explains the "dark matter ring" observed in galaxy cluster Cl 0024+17

### 2.4 Knebe, Llinares, Wu & Zhao (2009) -- PDM Offsets

In "On the Separation Between Baryonic and Dark Matter: Evidence for Phantom Dark Matter?":
- Examined whether PDM can produce the ~100-200 kpc offsets seen between X-ray and lensing peaks in colliding clusters (like the Bullet Cluster)
- With a uniform external field, PDM CAN produce substantial offsets
- But in realistic cosmological MONDian simulations, offsets are too small and too rare to explain observations
- **Important negative result**: PDM alone cannot reproduce Bullet Cluster-type observations

---

## 3. Cosmological Structure Formation in MOND

### 3.1 Sanders (2001) -- The Formation of Cosmic Structure with MOND

Sanders developed a nonrelativistic Lagrangian-based MOND theory and studied structure growth:
- Perturbations suppressed until matter domination (z ~ 200) because radiation dominance persists longer in a low-density baryonic universe
- Once matter dominates, growth is MUCH faster than Newtonian: delta ~ a^2 in MOND vs delta ~ a in Newton
- Small comoving scales enter the MOND regime EARLIER than larger scales
- Using COBE-normalized initial power spectrum from CMBFAST, the FINAL power spectrum resembles LCDM
- **Key result**: A baryon-only MOND cosmology can reproduce the observed P(k) shape

### 3.2 Nusser (2002) -- Modified Newtonian Dynamics of Large-Scale Structure

- Found structure forms in MOND, possibly too fast -- overshooting sigma_8 by factor ~2
- Growth in deep-MOND regime is faster because gravity is stronger
- Predicted consequences: early reionization, first L* galaxies at z~10, cosmic web by z~4-5, clusters by z~2

### 3.3 Llinares, Knebe & Zhao (2008) -- MOND Cosmological N-body Simulations

Built a novel numerical solver for the MOND Poisson equation using multi-grid relaxation:
- Modified the cosmological N-body code AMIGA (formerly MLAPM) for MOND
- Revisited cosmic structure formation under MOND
- Found structure does form, confirming earlier analytic work
- The nonlinear nature of the MOND Poisson equation requires specialized numerical techniques

### 3.4 Angus (2009) -- MOND + Neutrinos

Proposed coupling MOND with 11 eV sterile neutrinos (fully thermalized):
- The 11 eV sterile neutrino density is nearly identical to CDM density at recombination
- Gives excellent fit to CMB angular power spectrum
- But subsequent simulations revealed problems:
  - Sterile neutrino mass must be >30 eV for low-mass clusters
  - Cannot form correct number of high-mass clusters regardless of neutrino mass
  - The nuHDM (neutrino hot dark matter) model has serious difficulties

### 3.5 Angus et al. (2011, 2013) -- Cosmological Simulations with Massive Neutrinos

Extended the Angus 2009 framework:
- "The abundance of galaxy clusters in modified Newtonian dynamics: cosmological simulations with massive neutrinos" (2011)
- "Cosmological simulations in MOND: the cluster scale halo mass function with light sterile neutrinos" (2013)
- Found the weak-field MOND + sterile neutrino combination FAILS for structure formation from z~200
- MOND is necessary for developing large-scale structure in a hot dark matter cosmology
- But cannot simultaneously match low-mass and high-mass cluster abundances

### 3.6 Skordis & Zlosnik (2021) -- AeST: Relativistic MOND with Correct CMB

The breakthrough paper: "A new relativistic theory for Modified Newtonian Dynamics" (Phys. Rev. Lett. 127, 161302):
- Proposed Aether Scalar Tensor (AeST) theory using two extra fields: a scalar field and a vector field
- In the early Universe, the gravity-modifying fields MIMIC dark matter gravitationally
- This mimicry ensures the observed CMB patterns are reproduced
- Also demonstrates agreement with the observed matter power spectrum on linear cosmological scales
- The theory's action expanded to second order is ghost-free
- **This is the first MOND theory to match CMB and P(k)**

**Critical caveat from recent work (2025)**: A study of baryon density perturbation evolution in a relativistic MOND model based on a Lorentz-violating vector field found that "the faster growth of structures expected in the low-acceleration MOND regime is not recovered in the relativistic MOND." The dynamic nature of the vector field makes it challenging to realize MOND in cosmological contexts. The MOND limit is only achieved in stationary (non-dynamic) states.

---

## 4. The Key Question: delta_phantom at Nodes of Baryon Acoustic Oscillations

### 4.1 Linear Perturbation Theory in MOND

In QUMOND linear perturbation theory, the phantom dark matter perturbation is related to the baryon perturbation through:

```
delta_phantom = (nu - 1) * delta_b = nu_bar * delta_b
```

where nu = nu(|g_N|/a_0) is the MOND interpolation function evaluated at the Newtonian acceleration of the background plus perturbation.

### 4.2 The Divergence at Acoustic Nodes

At the nodes of baryon acoustic oscillations, delta_b passes through zero. The Newtonian gravitational acceleration g_N -> 0 at these nodes. In the deep-MOND limit:

```
nu(y) -> 1/sqrt(y) as y -> 0
```

Therefore nu_bar = nu - 1 -> 1/sqrt(y) - 1 ~ 1/sqrt(y) DIVERGES as y -> 0.

**The product delta_phantom = nu_bar * delta_b is an indeterminate form (infinity * 0) at the nodes.**

This is the CRITICAL question: what happens to this product?

### 4.3 Resolution of the Indeterminacy

Near a node of the acoustic oscillation at position x_0, we can expand:
- delta_b ~ (x - x_0) * delta_b' (linear in displacement from node)
- g_N ~ (x - x_0) * g_N' (also linear, since g_N is proportional to nabla Phi_N which comes from delta_b)

So |g_N|/a_0 ~ |x - x_0| * |g_N'|/a_0, and:

```
nu_bar ~ 1/sqrt(|x - x_0| * |g_N'|/a_0)
```

while delta_b ~ (x - x_0) * delta_b'

Therefore:

```
delta_phantom ~ (x - x_0) * delta_b' / sqrt(|x - x_0| * |g_N'|/a_0)
             ~ sqrt(|x - x_0|) * delta_b' / sqrt(|g_N'|/a_0)
```

**Result**: delta_phantom -> 0 at the nodes, but MUCH MORE SLOWLY than delta_b. The phantom perturbation goes as sqrt(|x - x_0|) while baryons go as |x - x_0|. This means:

- delta_phantom / delta_b -> infinity at nodes (the ratio diverges)
- But the absolute delta_phantom remains finite and goes to zero
- The GRADIENT of delta_phantom diverges at nodes (d/dx of sqrt(|x|) diverges at x=0)

### 4.4 Implications for P(k)

This has profound implications for the phantom dark matter power spectrum:
- The phantom field is a NONLINEAR FUNCTIONAL of the baryon field
- Even if baryons oscillate sinusoidally, the phantom field does NOT
- The sqrt behavior at nodes introduces cusps in the spatial PDM distribution
- These cusps generate HIGHER HARMONICS in Fourier space
- The phantom P(k) will have power at k-values that are NOT simply related to the baryon acoustic scale

**NO PAPER IN THE LITERATURE HAS COMPUTED THIS EFFECT EXPLICITLY.**

---

## 5. Time-Averaging of Phantom Dark Matter

### 5.1 The Question

Over one acoustic oscillation cycle, baryons oscillate as delta_b ~ A * sin(k*x) * cos(omega*t). What is the time-averaged phantom dark matter density?

### 5.2 Analysis

At any instant, delta_phantom = nu_bar(|g_N|/a_0) * delta_b. In the deep-MOND limit:

```
delta_phantom ~ |delta_b|^{1/2} * sign(delta_b) * (a_0 / k^2 G rho_bar)^{1/4}
```

(This follows from g_N ~ G rho_bar delta_b / k, so |g_N|/a_0 ~ G rho_bar |delta_b| / (k a_0), and nu ~ sqrt(k a_0 / G rho_bar |delta_b|))

Time-averaging over a full oscillation cycle:

```
<delta_phantom> ~ <|cos(omega*t)|^{1/2} * sign(cos(omega*t))> * F(x)
```

The time average of |cos(t)|^{1/2} * sign(cos(t)) over a full period is:

```
(1/2pi) integral_0^{2pi} |cos(t)|^{1/2} * sign(cos(t)) dt = 0
```

by symmetry (the function is odd under t -> t + pi).

**Result: The time-averaged phantom dark matter density perturbation is ZERO to first order.**

### 5.3 Second-Order Effects

However, the time-average of |delta_phantom| (the absolute value) is NOT zero. And crucially, the MOND force is nonlinear, so there are rectification effects:

```
<|delta_phantom|> ~ <|cos(omega*t)|^{1/2}> * |F(x)| != 0
```

The time-average of |cos(t)|^{1/2} = (2/pi) * Gamma(3/4) * Gamma(1/2) / Gamma(5/4) ~ 0.847

This means there is a RESIDUAL phantom dark matter density even after time-averaging, but it comes from the nonlinear response, not the linear oscillation. This is analogous to rectification in nonlinear circuits.

### 5.4 The Divergence at Nodes: Does It Survive Averaging?

The spatial cusps at nodes (Section 4.3) appear at every instant where delta_b has nodes. Since the baryon acoustic pattern is a standing wave, the nodes are at FIXED spatial positions. Therefore:

**The cusps at nodes are PRESERVED by time-averaging.**

The time-averaged |delta_phantom| has cusps at every node of the baryon acoustic pattern, with |delta_phantom| ~ sqrt(|x - x_node|) behavior near each node.

---

## 6. Summary of Literature Gaps and Implications for DFD

### 6.1 What Has Been Done
- PDM formula derived in AQUAL and QUMOND (Milgrom 1986, 2010)
- PDM profiles computed for galaxies, dwarfs, clusters (multiple authors)
- Cosmological N-body simulations with MOND (Llinares et al. 2008; Angus et al. 2011, 2013)
- Relativistic MOND matching CMB and P(k) (Skordis & Zlosnik 2021)
- PDM offsets from baryons studied (Knebe et al. 2009)

### 6.2 What Has NOT Been Done
1. **Nobody has computed the phantom dark matter power spectrum P_phantom(k) from baryon acoustic oscillations** -- this is a completely open problem
2. **Nobody has analyzed the nonlinear rectification effect** of MOND on oscillating baryons -- the time-averaged residual PDM from acoustic oscillations
3. **Nobody has computed the cusp structure at BAO nodes** in the PDM distribution
4. **Nobody has asked whether the nonlinear MOND processing of baryons can generate an effective CDM-like P(k)** through harmonic generation and rectification

### 6.3 Relevance to DFD

The phantom dark matter mechanism in MOND is conceptually similar to what DFD achieves: a baryon distribution is processed through a nonlinear operator to produce an effective dark matter distribution. The key differences are:

1. In MOND, the nonlinearity is in the gravitational force law (mu or nu function)
2. In DFD, the nonlinearity arises from the density field dynamics themselves
3. MOND's phantom dark matter is instantaneously determined by the baryon field
4. DFD may have dynamical degrees of freedom that evolve independently

The analysis of Sections 4 and 5 suggests that MOND's nonlinear processing of baryon oscillations can in principle generate:
- Higher harmonics (power at multiples of the BAO k-scale)
- Rectified (DC) components (non-zero time-average from oscillating input)
- Cusp features at BAO nodes
- A phantom P(k) that differs qualitatively from the baryon P(k)

This provides a concrete mathematical precedent for DFD's mechanism of generating CDM-like power spectra from baryon-only physics.

---

## Key References

1. Bekenstein & Milgrom (1984) -- AQUAL formulation
2. Milgrom (1986b) -- Introduction of phantom mass concept
3. Sanders (2001) -- Cosmic structure formation with MOND, ApJ 560, 1
4. Nusser (2002) -- Modified Newtonian dynamics of large-scale structure, MNRAS 331, 909
5. Pointecouteau & Silk (2005) -- New constraints on MOND from galaxy clusters, astro-ph/0505017
6. Milgrom & Sanders (2008) -- Rings and shells of dark matter as MOND artifacts, ApJ 678, 131
7. Llinares, Knebe & Zhao (2008) -- Cosmological structure formation under MOND, MNRAS 391, 1778
8. Knebe, Llinares, Wu & Zhao (2009) -- On the separation between baryonic and dark matter, ApJ 703, 2285
9. Angus (2009) -- MOND + 11 eV sterile neutrinos for cosmology
10. Milgrom (2010) -- Quasi-linear formulation of MOND, MNRAS 403, 886
11. Angus et al. (2011) -- Abundance of galaxy clusters in MOND, MNRAS 417, 941
12. Famaey & McGaugh (2012) -- MOND review, Living Reviews in Relativity 15, 10
13. Angus et al. (2013) -- Cluster scale halo mass function with light sterile neutrinos, MNRAS 436, 202
14. Bilek et al. (2020) -- Distribution of phantom dark matter in dwarf spheroidals, A&A 640, A154
15. Skordis & Zlosnik (2021) -- New relativistic theory for MOND, Phys. Rev. Lett. 127, 161302
16. Llinares et al. (2023) -- Structure of equivalent Newtonian systems: density profiles and core-cusp, A&A
17. Recent (2025) -- Evolution of baryon density perturbation in relativistic MOND, arXiv:2503.20151

---

*Agent 05 of 20 -- Literature research on phantom dark matter in MOND*
*Completed 2026-04-04*
