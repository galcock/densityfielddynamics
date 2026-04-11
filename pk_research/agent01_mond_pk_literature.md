# Agent 01: Literature Review — Matter Power Spectrum P(k) in MOND-Type Theories

## Executive Summary

This report surveys ALL known mechanisms for deriving the matter power spectrum P(k) in MOND-type theories without cold dark matter. The central challenge is that standard MOND modifies gravity at galactic scales but provides no mechanism for the enhanced structure growth observed in the CMB and large-scale structure — growth that in LCDM is driven by pressureless CDM forming potential wells before recombination.

**Key finding for DFD**: The literature identifies exactly ONE mechanism that consistently works for P(k) in MOND-type relativistic theories: a **vector field** (or equivalent extra degree of freedom) that develops a growing mode during matter domination, forming potential wells into which baryons fall. The 2024 Khronon theory shows a single scalar field with k-essence kinetics CAN mimic this, which is directly relevant to DFD's single-scalar approach.

---

## 1. Skordis-Zlosnik AeST / RMOND (2020-2021)

### Reference
- Skordis & Zlosnik, PRL 127, 161302 (2021); arXiv:2007.00082

### Field Content
- Metric g_mu_nu (standard)
- Unit timelike vector field A_mu (the "aether"), constrained by A_mu A^mu = -1
- Scalar field phi
- Auxiliary scalars (mu, nu, Y, Q) that are non-dynamical and can be algebraically eliminated

The theory has **6 physical degrees of freedom** at the fully nonlinear level.

### How It Achieves P(k)

The mechanism operates through a specific sequence:

1. **Early universe**: The vector and scalar fields collectively contribute an effective dust-like component to the cosmological stress-energy tensor. This dust-like degree of freedom **mimics CDM** at the background level and in perturbations.

2. **Vector field growing mode**: The vector field perturbation develops a growing mode during matter domination. This growing mode sources a difference between the two gravitational potentials (Phi and Psi), creating effective potential wells.

3. **Baryon capture**: Baryons fall into these potential wells after recombination, exactly as they fall into CDM potential wells in LCDM. The acoustic oscillation pattern in the CMB is preserved because the vector field maintains the correct peak ratios (crucially, the third peak).

4. **Late-time MOND transition**: The fields evolve so that at late times and on galactic scales, the theory reduces to MOND dynamics with the correct acceleration scale a0.

### Key Mathematical Insight
The coupling constant K_B (dimensionless) replaces the dimensionful MOND acceleration a0. The acceleration scale emerges dynamically from the cosmological background (FLRW solution), linking a0 to the Hubble expansion — addressing the "cosmological coincidence" that a0 ~ cH0.

### Numerical Results
- Excellent fit to Planck CMB TT power spectrum
- Excellent fit to SDSS DR7 LRG matter power spectrum
- Ghost-free at second order in perturbations
- Gravitational wave speed c_GW = c (passes GW170817 constraint)
- Specific sigma8 values not publicly reported in available summaries, but the fits are described as matching LCDM quality

### Critical Assessment for DFD
AeST requires THREE fields (metric + vector + scalar). The vector field is **essential** — Dodelson & Liguori showed analytically (in the predecessor TeVeS) that the scalar field perturbations decay as oscillatory Bessel functions and CANNOT drive structure growth. It is the vector field growing mode that does the work.

---

## 2. Bekenstein TeVeS (2004-2009)

### Reference
- Bekenstein, PRD 70, 083509 (2004)
- Skordis, Mota, Ferreira & Boehm, PRL 96, 011301 (2006)
- Skordis, CQG 26, 143001 (2009)

### Field Content
- Metric g_mu_nu
- Timelike vector field U_mu
- Scalar field phi
- Additional non-dynamical scalar field sigma

### How It Achieves P(k)

TeVeS was the first relativistic MOND theory to be tested against P(k):

1. **Skordis et al. (2006)** linearized the TeVeS equations and incorporated them into CMBFAST. They found that TeVeS CAN produce a matter power spectrum resembling LCDM.

2. **Dodelson & Liguori (2006)** provided the analytical explanation: the vector field perturbation alpha has a growing mode. The scalar field perturbations are decaying Bessel functions. Therefore structure growth is driven entirely by the vector field.

3. **Vector field mechanism**: The vector field sources the difference between the two metric potentials. As the vector perturbation grows, overdense regions accrete more matter than in standard GR.

### Why TeVeS Ultimately Failed
- Could not simultaneously fit CMB peaks AND matter power spectrum with the same parameters
- Ruled out by GW170817 (gravitational wave speed != light speed)
- Stability problems in stellar configurations
- The free function required fine-tuning

### Key Mathematical Insight
The growth of structure in TeVeS is proportional to the growing mode of the vector field perturbation. The scalar field oscillates and decays — it cannot drive growth. This is a fundamental result that constrains any MOND relativistic theory.

---

## 3. Sanders' MOND Cosmology (1998-2001)

### Reference
- Sanders, ApJ 480, 492 (1998)
- Sanders, ApJ 560, 1 (2001)

### Approach
Sanders worked within a non-relativistic MOND framework, modifying the CMBFAST code for a two-field MOND-like Lagrangian-based theory.

### Key Results

1. **Enhanced growth rate**: In the MOND regime, density perturbations grow as delta ~ a^2 (where a is the scale factor), compared to delta ~ a in Newtonian gravity. This is because MOND's nonlinear gravity amplifies the gravitational pull on overdense regions.

2. **P(k) shape**: The resulting large-scale structure is "largely compatible with observations" — the SHAPE of P(k) can be reproduced.

3. **Sigma8 problem**: Nusser (2002) implemented Sanders' growth relation in N-body simulations and found structure forms TOO FAST — sigma8 is overshot by roughly a factor of 2. The enhanced growth rate that helps on large scales overshoots on 8 Mpc/h scales.

4. **Neutrino supplement**: Sanders (2003) proposed that 2 eV neutrinos could provide the missing mass in galaxy clusters, supplementing MOND at cluster scales. However, this does not solve the P(k) normalization problem.

### Key Mathematical Insight
The MOND nonlinear Poisson equation:
  div[mu(|grad Phi|/a0) grad Phi] = 4 pi G rho

In the deep-MOND regime (|grad Phi| << a0), this becomes effectively:
  |grad Phi|^2 / a0 ~ G M / r^2

The nonlinearity means that gravity is enhanced by a factor sqrt(a0 r / GM) compared to Newton, leading to the a^2 growth instead of a growth.

### Critical Assessment for DFD
This is the most directly relevant result: a SINGLE nonlinear field equation produces enhanced growth. The problem is normalization (sigma8 too high). DFD's challenge is achieving the RIGHT amount of enhancement.

---

## 4. Milgrom's Phantom Dark Matter (1986-2010)

### Reference
- Milgrom, ApJ 306, 9 (1986)
- Milgrom, MNRAS 399, 474 (2009) — QUMOND
- Milgrom, PRD 80, 123536 (2009)

### Concept

The "phantom dark matter" (PDM) is the apparent dark matter density that a Newtonian observer would infer when analyzing a MOND system:

  rho_phantom = (1/4piG) div(g_MOND - g_Newton)

where g_MOND is the true MOND gravitational field and g_Newton is what Newtonian gravity predicts from baryons alone.

### Key Properties of Phantom Dark Matter

1. **Can be negative locally**: Unlike real CDM, the phantom density can become negative in certain configurations. This is a distinctive observational signature.

2. **Traces baryonic distribution symmetries**: The phantom DM respects the symmetries of the baryonic mass distribution but can have offset concentration peaks.

3. **Arises from nonlinearity**: The phantom DM is entirely a consequence of the nonlinear Poisson equation — it is the "extra" gravitational effect beyond Newton.

### QUMOND Formulation
Milgrom (2010) introduced QUMOND (Quasi-Linear MOND), where:
- The Newtonian potential is computed first (linear Poisson equation)
- The MOND potential is obtained by a nonlinear algebraic transformation
- Only linear PDEs need to be solved, with nonlinear algebraic steps

This is computationally much more tractable and gives the phantom DM distribution directly.

### Relevance to P(k)
The phantom dark matter concept shows that MOND's nonlinear gravity creates an EFFECTIVE dark matter component. However, this is only defined for static/quasistatic systems. Extending it to cosmological perturbations requires a relativistic theory — which is where TeVeS and AeST come in.

### Critical Assessment for DFD
The phantom DM concept is the mathematical bridge between MOND and CDM-like behavior. If DFD's nonlinear scalar field equation can generate a phantom DM component with the right cosmological properties, it could achieve P(k). The key question is whether a single scalar field's nonlinearity can produce enough effective DM at the right scales.

---

## 5. Angus Sterile Neutrino + MOND (2009)

### Reference
- Angus, MNRAS 394, 527 (2009); arXiv:0805.4014

### Approach
Rather than modifying the gravitational theory to produce P(k), Angus proposed supplementing MOND with a single species of massive sterile neutrino (~11 eV).

### Key Results

1. **CMB fit**: With Omega_nu_s ~ 0.23 and standard baryonic + dark energy components, the model achieves the same expansion history as LCDM.

2. **Uniqueness constraint**: Only ONE massive sterile neutrino species works. Three active neutrinos at 2 eV fail. Multiple sterile species fail.

3. **Galaxy-cluster bridge**: The 11 eV neutrino provides cluster-scale dark matter while being too hot to influence individual galaxy dynamics (where MOND dominates).

### Critical Assessment for DFD
This approach is philosophically opposite to DFD — it adds real particles rather than modifying the field equation. However, it demonstrates that MOND + a single additional component CAN match P(k), and it quantifies what properties that component needs (mass ~11 eV, Omega ~ 0.23).

---

## 6. Milgrom's BIMOND (Bimetric MOND) (2009-2010)

### Reference
- Milgrom, PRD 80, 123536 (2009)
- Milgrom, MNRAS 405, 1129 (2010); arXiv:1001.4444
- Milgrom, arXiv:1006.3809 (2010)

### Field Content
Two metric tensors (g_mu_nu and g-hat_mu_nu), with the two sectors coupled through MOND-like functions.

### How It Achieves P(k)

1. **Twin matter**: The second metric couples to "twin matter" (TM), a hypothetical matter sector.

2. **Repulsive interaction**: In the deep-MOND regime, matter and twin matter REPEL each other gravitationally.

3. **Shepherding mechanism**: Matter inhomogeneities grow not only by self-gravity but also through "shepherding" by flanking TM overdensities that push matter into denser concentrations.

4. **Mode decomposition**: Perturbations decompose into two uncoupled systems — one for the sum of fluctuations (follows Newtonian dynamics) and one for the difference (follows MOND dynamics with enhanced, nonlinear gravity).

### Critical Assessment for DFD
BIMOND requires two metrics and twin matter — far more complex than DFD's single scalar field. However, the shepherding/repulsion mechanism is conceptually interesting: structure can be enhanced by repulsive interactions between sectors, not just attractive self-gravity.

---

## 7. Blanchet Dipolar Dark Matter (2006-2013)

### Reference
- Blanchet, CQG 24, 3529 (2007); arXiv:astro-ph/0605637
- Blanchet & Le Tiec, PRD 80, 023524 (2009); arXiv:0901.3114
- Blanchet & Marsat, arXiv:1312.6991 (2013)

### Concept
MOND phenomenology arises from the "gravitational polarization" of a cosmic fluid made of dipole moments (particles carrying both positive and negative gravitational mass), aligned in the gravitational field.

### How It Achieves P(k)

1. **At first order** in cosmological perturbation theory, the model is EQUIVALENT to LCDM. The dipolar dark matter behaves exactly like CDM for linear perturbations.

2. **At second order**, the internal energy of dipolar DM modifies the curvature perturbation, producing a new type of non-Gaussianity in the bispectrum.

3. **Galactic scales**: The polarization effect produces MOND-like dynamics.

### Critical Assessment for DFD
This is elegant because P(k) comes "for free" at linear order — the model IS LCDM cosmologically. The MOND behavior emerges only in the nonlinear, quasistatic regime. This suggests a design principle: make the cosmological sector look like LCDM, with MOND emerging only in specific limits.

---

## 8. Berezhiani-Khoury Superfluid Dark Matter (2015-2022)

### Reference
- Berezhiani & Khoury, PRD 92, 103510 (2015); arXiv:1507.01019
- Khoury, SciPost Phys. Lect. Notes 42 (2022)

### Field Content
Axion-like particles with:
- Mass ~ eV
- Strong self-interactions
- Polytropic equation of state P ~ rho^3 in the superfluid phase

### How It Achieves P(k)

1. **Cosmological scales**: The DM particles behave as standard CDM — they cluster gravitationally and produce the standard P(k).

2. **Galaxy scales**: In galaxies, the DM forms a superfluid with phonon excitations governed by a MOND-like effective action. The phonons mediate a MONDian force between baryonic particles.

3. **Cluster scales**: Due to higher velocity dispersion, the DM is in a mixed or normal (non-superfluid) phase, explaining why MOND fails at cluster scales.

### Key Mathematical Insight
The MOND behavior emerges from the phonon Lagrangian of the superfluid, which has a kinetic term proportional to X^(3/2) where X = (d_mu theta)^2 / 2m. This fractional power produces the MOND interpolation function.

### Critical Assessment for DFD
Superfluid DM achieves P(k) trivially because it IS dark matter cosmologically. The interesting insight for DFD is the mathematical mechanism: a fractional power in the kinetic term of a scalar field produces MOND-like behavior. If DFD's scalar field has a similar nonlinear kinetic structure, the same mathematics may apply.

---

## 9. Deffayet-Esposito-Farese-Woodard Nonlocal MOND (2014-2025)

### Reference
- Deffayet, Esposito-Farese & Woodard, PRD 90, 064038 (2014); arXiv:1405.0393
- Deffayet, Esposito-Farese & Woodard, arXiv:2512.10513 (2025)

### Field Content
Pure metric theory — NO additional fields. Uses nonlocal operators (inverse d'Alembertians) acting on curvature scalars.

### How It Achieves P(k)

1. **Nonlocal scalar**: A nonlocal scalar X = inverse_box[R] (where R is the Ricci scalar) is typically positive in gravitationally bound systems and negative in cosmological settings.

2. **Two-branch solution**: The algebraic function f(X) has a positive branch (galactic MOND) and a negative branch (cosmological LCDM-like behavior).

3. **Recent advance (2025)**: A single model now interpolates between MOND in gravitationally bound systems and LCDM-like cosmology, reproducing CMB, BAO, and linearized structure formation.

### Critical Assessment for DFD
This is the ONLY approach that achieves MOND + P(k) with NO extra fields beyond the metric. The price is nonlocality. For DFD, this suggests that a purely local single-scalar approach may require something equivalent to nonlocality — perhaps through the field's self-interaction potential or through time-derivative terms that effectively introduce memory.

---

## 10. Relativistic Khronon Theory (2024)

### Reference
- Verwayen, Milgrom & Zlosnik, JCAP 11, 040 (2024); arXiv:2404.06584

### Field Content
- Metric g_mu_nu
- **Single scalar field tau** (the "Khronon"), with time dimensions

This is the ONLY theory with a single scalar field that claims CMB + P(k) compatibility.

### How It Achieves P(k)

1. **K-essence kinetics**: The Khronon scalar field has a kinetic term of the Dirac-Born-Infeld (DBI) form. This k-essence term allows the scalar to behave as an effective dark matter fluid.

2. **Generalized Dark Matter (GDM) equivalence**: The Khronon equations can be recast as a GDM fluid with:
   - Time-dependent equation of state w(t) in the background
   - Zero viscosity
   - Non-zero, k-dependent sound speed c_s(k) in linear perturbations

3. **Background cosmology**: The scalar field's energy density scales like dust (w = 0) at late times, mimicking CDM. At earlier times, it can scale differently (e.g., as radiation).

4. **Perturbation growth**: The k-dependent sound speed allows the scalar perturbations to grow on large scales (where c_s is small) while remaining stable on small scales.

### Key Mathematical Insight
The action is:
  S = (c^3/16piG) integral d^4x sqrt(-g) [R - 2 J(Y) + 2 K(Q)] + S_matter

where Y involves the acceleration of the Khronon flow and K(Q) is the k-essence kinetic term. The J(Y) term gives MOND at galactic scales; the K(Q) term gives dark-matter-like cosmological behavior.

The DBI form K(Q) = M^4 [sqrt(1 + 2Q/M^4) - 1] naturally produces dust-like behavior (w -> 0) at late times.

### Critical Assessment for DFD — THIS IS THE KEY RESULT

The Khronon theory demonstrates that a **single scalar field** CAN achieve both MOND and P(k) if:
1. It has k-essence (nonlinear kinetic) dynamics
2. The kinetic term has the right functional form (DBI-like)
3. The background solution naturally evolves to w = 0 (dust-like)
4. Perturbations have a k-dependent sound speed

**This is the existence proof that DFD needs.** If DFD's density scalar field can be given k-essence-like kinetic properties, or if its existing nonlinear dynamics already produce these features, then P(k) may be achievable.

---

## Summary Table: Mechanisms for MOND-Compatible P(k)

| Theory | Fields | Mechanism | P(k) Quality | sigma8 | Single Field? |
|--------|--------|-----------|---------------|--------|---------------|
| AeST/RMOND | metric + vector + scalar | Vector growing mode forms potential wells | Excellent (Planck-quality CMB + SDSS P(k)) | Not public | No (3 fields) |
| TeVeS | metric + vector + scalar | Vector growing mode (same as AeST) | Partial (could not fit all simultaneously) | N/A | No (3 fields) |
| Sanders MOND | Nonlinear Poisson | Enhanced growth delta ~ a^2 | Shape OK, normalization fails | ~2x too high | Yes (1 field) |
| Phantom DM | Nonlinear Poisson | Effective DM from nonlinearity | Conceptual only | N/A | Yes (1 field) |
| Angus nu_s + MOND | MOND + 11 eV neutrino | Real particles for clustering | Good (CMB match) | Plausible | No (extra particles) |
| BIMOND | 2 metrics | Twin matter shepherding | Qualitative only | N/A | No (2 metrics) |
| Dipolar DM | metric + dipolar fluid | Equals LCDM at linear order | Excellent (= LCDM) | Same as LCDM | No (extra matter) |
| Superfluid DM | metric + axion-like DM | IS CDM cosmologically | Excellent (= CDM) | Same as CDM | No (extra particles) |
| Nonlocal MOND | metric only (nonlocal) | Nonlocal operators mimic CDM | Claimed good (2025) | Not reported | Yes (pure metric) |
| **Khronon (2024)** | **metric + scalar** | **K-essence kinetics -> GDM fluid** | **Claimed good** | **Not reported** | **YES** |

---

## Key Insights for DFD

### What Works for P(k)

1. **Vector field growing modes** (TeVeS, AeST): The most proven mechanism. The vector perturbation grows and creates potential wells. Scalar perturbations alone decay as Bessel functions.

2. **K-essence scalar dynamics** (Khronon 2024): A single scalar with DBI-type kinetic term CAN mimic dark matter. The key is the k-dependent sound speed and dust-like equation of state.

3. **Being CDM at linear order** (Dipolar DM, Superfluid DM): If the theory IS LCDM at the perturbative level, P(k) comes automatically. MOND emerges only in the nonlinear/quasistatic regime.

4. **Nonlinear growth enhancement** (Sanders, phantom DM): The MOND nonlinear Poisson equation enhances growth from delta ~ a to delta ~ a^2. This gives the right SHAPE but wrong AMPLITUDE (factor ~2 overshoot in sigma8).

### What DFD Needs

For DFD's single scalar field to achieve P(k), the most promising path based on this literature is:

**Path A: K-essence route (following Khronon)**
- If DFD's scalar field equation has nonlinear kinetic terms, it may naturally behave as a GDM fluid cosmologically
- Requires: DBI-like or similar kinetic structure, w -> 0 at late times, k-dependent sound speed
- Advantage: Proven to work with a single scalar

**Path B: Nonlinear growth with normalization fix**
- The MOND-like nonlinear equation already gives delta ~ a^2 growth
- Problem: sigma8 overshoot by factor ~2
- Possible fix: DFD's specific nonlinearity may have a different growth exponent, or scale-dependent modifications that suppress power on 8 Mpc/h scales

**Path C: Effective vector-like behavior from scalar**
- If DFD's scalar field in a cosmological background develops perturbations that mimic the growing mode of a vector field
- This would require the scalar perturbation to NOT decay as Bessel functions — needing a qualitatively different dispersion relation from standard scalar fields

### The Fundamental Obstruction

Dodelson & Liguori's result is the key theoretical obstacle: **standard scalar field perturbations in a MOND-type theory decay as oscillatory Bessel functions**. They cannot drive structure growth. Only the vector field growing mode works.

The Khronon theory circumvents this by using k-essence dynamics that change the scalar field's dispersion relation. The DBI kinetic term gives the scalar a k-dependent effective mass and sound speed, preventing the Bessel-function decay.

**For DFD**: The question is whether DFD's nonlinear field equation already provides this kind of modified dispersion relation, or whether the kinetic structure needs to be explicitly designed.

### The Nonlinear Rectification Question

No papers were found specifically on "nonlinear rectification generating DC components from oscillating MOND sources." However, the underlying physics is present in several works:

1. **Sanders' enhanced growth**: The nonlinear Poisson equation effectively rectifies — small perturbations in the deep-MOND regime get amplified nonlinearly, producing more structure than the linear theory predicts.

2. **QUMOND phantom DM**: The divergence operation on the MOND-modified gravitational field produces an effective DC (zero-frequency) density component from the oscillating baryon-photon fluid. This is mathematically equivalent to rectification.

3. **BIMOND mode coupling**: The nonlinear MOND coupling between matter and twin matter creates growing differences from oscillating inputs.

This rectification concept — that MOND's nonlinearity can convert oscillating (AC) baryon-photon perturbations into a growing (DC) effective dark matter component — may be the key physical insight for DFD. It is implicit in the literature but has never been explicitly formulated as a rectification mechanism.

---

## References (Chronological)

1. Bekenstein & Milgrom, ApJ 286, 7 (1984) — AQUAL nonlinear Poisson
2. Milgrom, ApJ 306, 9 (1986) — Phantom dark matter concept
3. Sanders, ApJ 480, 492 (1998) — MOND cosmology basics
4. Sanders, ApJ 560, 1 (2001) — Modified CMBFAST for MOND
5. Nusser, MNRAS 331, 909 (2002) — N-body MOND, sigma8 overshoot
6. Sanders, MNRAS 342, 901 (2003) — 2 eV neutrinos for clusters
7. Bekenstein, PRD 70, 083509 (2004) — TeVeS
8. Skordis, Mota, Ferreira & Boehm, PRL 96, 011301 (2006) — TeVeS P(k)
9. Dodelson & Liguori, PRL 97, 231301 (2006) — Vector field growing mode
10. Blanchet, CQG 24, 3529 (2007) — Gravitational polarization
11. Skordis, CQG 26, 143001 (2009) — TeVeS review
12. Angus, MNRAS 394, 527 (2009) — 11 eV sterile neutrino + MOND
13. Milgrom, PRD 80, 123536 (2009) — BIMOND
14. Blanchet & Le Tiec, PRD 80, 023524 (2009) — Dipolar dark matter
15. Milgrom, MNRAS 399, 474 (2009) — QUMOND
16. Milgrom, MNRAS 405, 1129 (2010) — BIMOND twin matter
17. Milgrom, arXiv:1006.3809 (2010) — BIMOND fluctuation growth
18. Famaey & McGaugh, Living Rev. Rel. 15, 10 (2012) — Comprehensive review
19. Blanchet & Marsat, arXiv:1312.6991 (2013) — Dipolar DM cosmology
20. Deffayet, Esposito-Farese & Woodard, PRD 90, 064038 (2014) — Nonlocal MOND
21. Berezhiani & Khoury, PRD 92, 103510 (2015) — Superfluid dark matter
22. Skordis & Zlosnik, PRL 127, 161302 (2021) — AeST/RMOND
23. Skordis & Zlosnik, PRD (2021) — AeST linear stability (arXiv:2109.13287)
24. Khoury, SciPost Phys. Lect. Notes 42 (2022) — Superfluid DM lectures
25. Verwayen, Milgrom & Zlosnik, JCAP 11, 040 (2024) — Khronon theory
26. Deffayet, Esposito-Farese & Woodard, arXiv:2512.10513 (2025) — Nonlocal MOND interpolation
