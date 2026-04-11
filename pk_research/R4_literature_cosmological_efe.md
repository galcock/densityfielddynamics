# R4 Agent: Literature Review -- The Cosmological External Field Effect in MOND

## Date: 2026-04-05
## Status: Comprehensive literature search complete
## Agent: R4 Literature Cosmological EFE Agent

---

## EXECUTIVE SUMMARY

The literature reveals a striking gap: **no paper in the MOND/modified gravity literature has rigorously derived whether the Hubble expansion provides a cosmological External Field Effect (EFE) for perturbation theory.** Every cosmological MOND simulation and perturbation analysis has instead employed some version of the "Jeans swindle" -- assuming the MOND modification applies only to peculiar accelerations, leaving the FRW background intact. This assumption is physically motivated but never rigorously justified from an action principle. The consequences are profound:

1. **Sanders (2001)** explicitly treats the Hubble deceleration as a "background field" that influences finite regions -- this IS a form of cosmological EFE, but applied through a two-field Lagrangian construction, not derived from the standard AQUAL/QUMOND action.

2. **Nusser (2002)** uses the Jeans swindle explicitly, applying MOND only to density fluctuations, and admits "we do not see any physical justification for it."

3. **Llinares, Knebe & Zhao (2008)** avoid the Jeans swindle by deriving their equations from Zhao's 2008 covariant theory, where the interpolation function is assumed spatially constant on the grid scale, with the acceleration threshold gamma(a) = a * g_0 encoding the expansion factor.

4. **Skordis (2006, 2009)** and **Skordis & Zlosnik (2021)** provide the most rigorous treatments through relativistic theories (TeVeS and AeST), where the scalar field has a nonzero, time-dependent cosmological background that naturally regularizes the perturbation theory.

5. **Milgrom** has never published a definitive statement on whether the Hubble expansion provides a cosmological EFE. His Scholarpedia article and reviews discuss the EFE only in galactic contexts.

**The central finding: In FRW cosmology, the spatial gradient of the background potential vanishes (grad Phi_bar = 0), so the standard spatial-gradient EFE mechanism does not operate. The question is whether there exists an alternative temporal mechanism.**

---

## 1. BEKENSTEIN & MILGROM (1984) -- THE AQUAL PAPER

### Reference
Bekenstein, J. & Milgrom, M. (1984). "Does the missing mass problem signal the breakdown of Newtonian gravity?" ApJ 286, 7.

### What it establishes

The AQUAL (A-Quadratic Lagrangian) formulation provides the first action-based MOND theory. The field equation is:

    nabla . [mu(|nabla Phi|/a_0) nabla Phi] = 4 pi G rho

The EFE is derived exactly for isolated subsystems: when a system with internal potential phi_int is embedded in an external field with gradient g_ext, the total gradient |nabla Phi| = |nabla phi_int + g_ext| enters the mu function. When |g_ext| >> |nabla phi_int|, the system becomes effectively Newtonian.

### What it does NOT address

- The paper does not discuss cosmological perturbation theory
- No treatment of the FRW background
- No discussion of whether the Hubble flow provides an EFE
- The theory is purely non-relativistic, so cannot address FRW cosmology rigorously

### Key implication for cosmology

In AQUAL, the EFE requires a nonzero SPATIAL gradient of the external potential. In FRW symmetry, grad Phi_bar = 0 by homogeneity. Therefore, **the standard AQUAL EFE mechanism provides NO cosmological EFE.**

---

## 2. SANDERS (2001) -- THE PIVOTAL PAPER

### Reference
Sanders, R. H. (2001). "The Formation of Cosmic Structure with Modified Newtonian Dynamics." ApJ 560, 1. [arXiv: astro-ph/0011439]

### What Sanders does

Sanders constructs a **two-field Lagrangian-based theory of MOND** (nonrelativistic) that embodies several critical assumptions:

1. **Constancy of the MOND acceleration parameter a_0**
2. **MOND force associated with peculiar accelerations only** -- this is the key assumption
3. **The deceleration of the Hubble flow as a background field that influences the dynamics of a finite-size region**

### The critical insight

Sanders treats the Hubble deceleration explicitly as a background field -- this is conceptually a cosmological EFE, but implemented through a different mechanism than the standard spatial-gradient EFE. The MOND modification applies only to the PECULIAR acceleration (deviation from Hubble flow), not to the total acceleration.

### Growth rate results

Within this framework, the evolution equation for spherically symmetric overdensities is **nonlinear** and implies **very rapid growth** even in a low-density background, particularly at the epoch when the cosmological constant begins to dominate. Small comoving scales enter the MOND regime earlier and evolve to large overdensities sooner.

Using COBE-normalized initial conditions, Sanders finds the final power spectrum resembles the standard LCDM universe.

### What this means for DFD

Sanders' result represents a specific choice: MOND applies to peculiar accelerations, with the Hubble deceleration providing a "background field." This is neither the no-EFE case nor the standard spatial EFE case -- it is a third option where the cosmological expansion rate sets the context but does not enter through the mu function in the same way as the galactic EFE.

The growth rate delta ~ a^2 in the deep-MOND regime that Sanders finds is the result WITHOUT a standard spatial EFE (since there is none in FRW), but WITH the two-field Lagrangian construction that separates peculiar from cosmological acceleration.

---

## 3. NUSSER (2002) -- N-BODY SIMULATIONS

### Reference
Nusser, A. (2002). "Modified Newtonian dynamics of large-scale structure." MNRAS 331, 909. [arXiv: astro-ph/0109016]

### How Nusser handles the background

Nusser explicitly employs the **Jeans swindle**: he writes a MOND-type relationship between the FLUCTUATIONS in density and the gravitational force. The MOND modification applies only to density perturbations, leaving the background FRW cosmology intact.

His relation connects the peculiar force field perturbations g to the Newtonian gravitational acceleration g_N through a transition function involving the acceleration threshold g_0. This applies ONLY to fluctuations over the uniform background.

### Nusser's own assessment

Critically, Nusser states: **"Although our procedure can be derived from a Lagrangian... we do not see any physical justification for it."** This is an extraordinary admission -- the Jeans swindle works computationally but lacks rigorous physical justification in MOND.

### No effective mu parameter

Nusser does NOT employ an effective mu(x) function for the background. He simply decrees that the background is unmodified and MOND acts only on perturbations. There is no background EFE parameter.

### Numerical results

Even with this approach, Nusser finds that MOND overshoots sigma_8 by a factor of approximately 2 -- structure forms too fast. This is the no-EFE result (or rather, the Jeans-swindle result where the background provides no regulation).

---

## 4. LLINARES, KNEBE & ZHAO (2008) -- COSMOLOGICAL N-BODY CODE

### Reference
Llinares, C., Knebe, A. & Zhao, H. (2008). "Cosmological Structure Formation under MOND: a new numerical solver for Poisson's equation." MNRAS 391, 1778. [arXiv: 0809.2899]

### How they handle the background field

Rather than applying the Jeans swindle explicitly, Llinares et al. derive their equation from Zhao's (2008) covariant MOND theory. Their comoving peculiar MONDian potential equation is:

    nabla . [mu(x) nabla Phi_M] = 4 pi G a^2 rho

where rho is the density CONTRAST (perturbation), a is the scale factor, and mu(x) is the MOND interpolation function.

### Key assumption about mu

The authors assume mu(x) is **spatially constant** -- evaluated at a single value across the simulation grid, based on a non-relativistic limit of Zhao's covariant theory. The acceleration threshold is encoded as:

    gamma(a) = a * g_0

This ensures the universe is Newtonian at early times (high redshift) and progressively more MONDian as the universe expands. The MOND acceleration scale effectively increases with the scale factor.

### No explicit Jeans swindle

Their formulation avoids the explicit Jeans swindle by deriving the equations from a covariant theory. However, the assumption that "MOND does not affect fluctuations and leaves the background cosmology intact" is still present as an assumption of the underlying theory.

### Results

Proper numerical integration produces even STRONGER clustering than previous ad-hoc approaches -- the large-scale structure evolution is faster, leading to more galaxy clustering, especially compared to LCDM.

---

## 5. SKORDIS (2006, 2008, 2009) -- TeVeS PERTURBATION THEORY

### References
- Skordis, C. (2006). "Tensor-vector-scalar cosmology: Covariant formalism for the background evolution and linear perturbation theory." Phys. Rev. D74, 103513. [arXiv: astro-ph/0511591]
- Skordis, C. (2008). "Generalizing TeVeS Cosmology." Phys. Rev. D77, 123502. [arXiv: 0801.1985]
- Skordis, C. (2009). "The Tensor-Vector-Scalar theory and its cosmology." Class. Quant. Grav. 26, 143001. [arXiv: 0903.3602]

### How TeVeS handles the cosmological background

TeVeS is Bekenstein's relativistic MOND theory with a metric tensor, a vector field, and a scalar field. In cosmology:

1. **The scalar field has a nonzero, time-dependent background value** phi_bar(t) that evolves with the expansion
2. **The vector field aligns with the cosmic time direction** in FRW
3. **The free function F(mu) from the scalar field Lagrangian** determines both galactic MOND phenomenology and cosmological evolution

### The crucial point for EFE

In TeVeS, the scalar field gradient in the background is purely TEMPORAL: d(phi_bar)/dt is nonzero but nabla phi_bar = 0 (spatial gradient vanishes by FRW symmetry). This temporal evolution of the scalar field provides an analogue to a background field, but it enters the perturbation equations through the time derivative of the background, not through a spatial gradient.

### Perturbation theory structure

Skordis derives the complete linear perturbation equations for scalar, vector, and tensor modes. The background scalar field value enters the perturbation equations through:
- The background value of the free function F and its derivatives
- The time evolution equations for scalar perturbations
- The effective gravitational constant for perturbation growth

This provides a natural regularization: the perturbation equations are well-defined because the background scalar field is nonzero, even though the spatial gradient vanishes.

### Implications

TeVeS suggests that the cosmological "EFE" -- if it exists -- comes from the TEMPORAL sector (scalar field evolution in time) rather than the SPATIAL sector (gradient of potential). This is qualitatively different from the galactic EFE.

---

## 6. SKORDIS & ZLOSNIK (2021) -- AeST THEORY

### Reference
Skordis, C. & Zlosnik, T. (2021). "New Relativistic Theory for Modified Newtonian Dynamics." Phys. Rev. Lett. 127, 161302. [arXiv: 2007.00082]

### Major achievement

AeST (Aether Scalar Tensor theory) is the first relativistic MOND theory demonstrated to reproduce both:
- The observed CMB power spectrum
- The observed matter power spectrum
- MOND phenomenology in galaxies

### Cosmological scalar field

The scalar field phi in AeST evolves cosmologically as shift-symmetric k-essence, with energy density proportional to (1+z)^3 plus small decaying corrections -- behaving like dust. The scalar field has a nonzero background that provides the "dark matter mimic" on cosmological scales.

### How perturbations work

The field equations involve the metric g_{mu nu}, a unit-timelike vector A_mu (with A_mu A^mu = -1), and a scalar field phi. In the quasistatic limit for perturbations, the field dependence reduces to two potentials.

The theory achieves its cosmological success by having the scalar field's cosmological energy density mimic cold dark matter on large scales, while providing MOND-like behavior through the same field on galactic scales.

### Implications for cosmological EFE

AeST provides a natural resolution: the scalar field background evolves with cosmic time and provides the "regulation" of MOND behavior at cosmological scales. The free function that controls MOND phenomenology in galaxies also controls the cosmological background, but **MONDian behavior on galactic scales does not necessarily result in MONDian behavior on cosmological scales** -- the free function may operate in different regimes.

---

## 7. THE JEANS SWINDLE IN MOND -- LITERATURE ASSESSMENT

### The fundamental problem

In Newtonian gravity, the Jeans swindle works because the Poisson equation is linear. Setting nabla^2 Phi_bar = 4 pi G rho_bar and subtracting gives nabla^2 delta_Phi = 4 pi G rho_bar delta. The background and perturbation decouple exactly.

In MOND (AQUAL), the equation is:

    nabla . [mu(|nabla Phi|/a_0) nabla Phi] = 4 pi G rho

This is NONLINEAR. For a uniform background, nabla Phi_bar = 0, so the MOND operator evaluated at the background gives:

    nabla . [mu(0) * 0] = 0

This is trivially satisfied regardless of what mu(0) is (even though mu(0) = 0 in the standard interpolation function). The background equation is automatically satisfied.

### The mu(0) = 0 issue

When we perturb around this background, with nabla Phi = nabla delta_Phi (small), we get:

    nabla . [mu(|nabla delta_Phi|/a_0) nabla delta_Phi] = 4 pi G rho_bar delta

For small perturbations, |nabla delta_Phi|/a_0 << 1, so mu ~ |nabla delta_Phi|/a_0 (deep-MOND regime). The perturbation equation is:

    nabla . [(|nabla delta_Phi|/a_0) nabla delta_Phi] ~ 4 pi G rho_bar delta

This is in the deep-MOND limit. There is NO breakdown or singularity -- the equation is perfectly well-defined.

### Who does what

| Author(s)            | Year | Approach to background                         | EFE present? |
|----------------------|------|------------------------------------------------|--------------|
| Sanders              | 2001 | Two-field Lagrangian; Hubble deceleration as background field | Implicit (through peculiar acceleration separation) |
| Nusser               | 2002 | Explicit Jeans swindle; MOND on fluctuations only | No |
| Skordis              | 2006 | TeVeS covariant theory; scalar field background | Yes (temporal, through scalar field) |
| Llinares, Knebe, Zhao| 2008 | Covariant theory; spatially constant mu | No explicit EFE; mu evolves with scale factor |
| Milgrom              | 2010 | QUMOND; quasi-linear formulation | Not addressed explicitly |
| Milgrom              | 2010 | BIMOND; twin-matter sector | Different mechanism (twin matter repulsion) |
| Angus & Diaferio     | 2011 | QUMOND PM code; sterile neutrinos | Jeans swindle assumed |
| Katz, McGaugh et al. | 2013 | QUMOND cosmological N-body | Jeans swindle assumed |
| Skordis & Zlosnik    | 2021 | AeST; full relativistic CMB+P(k) | Yes (scalar field provides dark matter mimic) |

---

## 8. MILGROM'S OWN STATEMENTS

### What Milgrom has said

From the Scholarpedia article and various reviews:

1. The EFE is discussed ONLY in galactic contexts -- subsystems embedded in larger systems
2. The cosmological coincidence a_0 ~ cH_0 is noted as possibly deep, suggesting "the state of the universe at large strongly enters local dynamics of small systems"
3. The Jeans mass in MOND differs from Newtonian: M_J(MOND) ~ T^2/a_0 (vs. T^{3/2} rho^{-1/2} in Newton)
4. Milgrom notes that in MOND, "uniform expansion of a spherical region is not possible" and "an isotropic and homogeneous universe as described by the Robertson-Walker metric is not possible in the context of (non-relativistic) MOND"

### What Milgrom has NOT said

- No explicit statement on whether the Hubble expansion provides an EFE
- No derivation of the cosmological perturbation equation from the AQUAL or QUMOND action with EFE
- No resolution of the tension between MOND's inability to support FRW and the need for cosmological MOND perturbation theory

### The gap

Milgrom's own admission that FRW is not possible in non-relativistic MOND is profound. It means that applying the Jeans swindle (which assumes an FRW background) in MOND is inherently contradictory at the non-relativistic level. One MUST go to a relativistic theory (TeVeS, AeST, etc.) to have a consistent cosmological background.

---

## 9. FAMAEY & MCGAUGH (2012) REVIEW

### Reference
Famaey, B. & McGaugh, S. S. (2012). "Modified Newtonian Dynamics (MOND): Observational Phenomenology and Relativistic Extensions." Living Rev. Rel. 15, 10. [arXiv: 1112.3960]

### Coverage of cosmological EFE

The comprehensive review discusses:
- The EFE extensively in galactic contexts (Section 6.3)
- Structure formation challenges in MOND
- The sigma_8 overshoot problem
- Relativistic extensions (TeVeS, BIMOND, GEA)

However, the review does NOT contain an explicit discussion of whether the Hubble expansion provides a cosmological EFE. The EFE is treated as a galactic/cluster phenomenon throughout.

### Structure formation discussion

The review notes that MOND encounters difficulties with structure formation, potentially producing too much structure by z=0. This is consistent with the no-EFE (Jeans swindle) results from Nusser (2002).

---

## 10. THE QUMOND COSMOLOGICAL PERTURBATION THEORY

### Reference
Milgrom, M. (2010). "Quasi-linear formulation of MOND." MNRAS 403, 886.

### How QUMOND works

In QUMOND, one first solves the standard Newtonian Poisson equation:

    nabla^2 Phi_N = 4 pi G rho

Then constructs the MOND potential:

    nabla^2 Phi = nabla . [nu(|nabla Phi_N|/a_0) nabla Phi_N]

where nu(y) is the QUMOND interpolation function (nu(y) ~ 1 for y >> 1, nu(y) ~ y^{-1/2} for y << 1).

### Cosmological application

For cosmological perturbation theory in QUMOND:
1. First solve the Newtonian perturbation equation (standard, well-defined)
2. Then apply nu to the Newtonian peculiar acceleration
3. The EFE enters through the Newtonian acceleration: if |nabla Phi_N| is small (deep MOND), nu is large, enhancing the effective gravity

The QUMOND formulation avoids the mu(0) problem entirely because it starts from the Newtonian potential (always well-defined) and then applies the nonlinear modification.

### Cosmological simulations using QUMOND

Angus & Diaferio (2011) and Katz, McGaugh, Teuben & Angus (2013) used QUMOND-based N-body codes for cosmological simulations, augmented with sterile neutrinos to provide hot dark matter. These codes use the Jeans swindle implicitly -- MOND modifies only the peculiar acceleration field.

---

## 11. RECENT WORK: COSMOLOGICAL PERTURBATIONS IN RELATIVISTIC MOND (2024)

### Reference
arXiv: 2410.10205 (2024). "Cosmological perturbations of a relativistic MOND theory."

### Key findings

This paper presents post-Newtonian (PN) and fully nonlinear relativistic perturbation equations for a MOND-type theory in cosmological context. Key points:

1. **At 0PN order, baryon perturbation grows faster in the MOND regime** -- confirming earlier non-relativistic results
2. **The Jeans criterion is derived for the MOND field** -- establishing when gravitational instability occurs
3. **Two free functions** are used: J(A) for MOND phenomenology and K(Q) for cosmology, allowing independent tuning
4. **The background enters through the Hubble parameter H and scale factor a**
5. **The tau-field background satisfies Q=1 and A_a=0** at zeroth order, with K_Q = I_0/a^3

### Implications

The use of two separate free functions (one for MOND phenomenology, one for cosmology) suggests that the cosmological behavior can be tuned independently of the galactic MOND behavior. This is consistent with Skordis & Zlosnik's finding that "MONDian behaviour on galactic scales does not necessarily result in MONDian behaviour on cosmological scales."

---

## 12. SYNTHESIS: THE ANSWER TO THE CENTRAL QUESTION

### Does the Hubble flow provide a cosmological EFE?

**The literature consensus (insofar as one exists) is: NO, not through the standard spatial-gradient mechanism.**

The reasons:

1. **In FRW, nabla Phi_bar = 0.** The spatial gradient of the background gravitational potential vanishes by homogeneity. The standard AQUAL EFE requires a nonzero spatial gradient. Therefore, there is no spatial EFE.

2. **The Jeans swindle is valid but trivial.** When nabla Phi_bar = 0, the MOND operator applied to the background gives identically zero, and perturbations are automatically in the deep-MOND regime. No EFE is needed to make the equations well-defined.

3. **Sanders' "background field" is not the standard EFE.** Sanders' two-field Lagrangian separates peculiar from cosmological acceleration, treating the Hubble deceleration as a context that influences dynamics. But this is not the same as the galactic EFE -- it is a separate theoretical construction.

4. **Relativistic theories provide a TEMPORAL mechanism.** In TeVeS and AeST, the scalar field has a nonzero background that evolves in time. This provides regulation of the perturbation theory, but through the time derivative (cosmological evolution), not through a spatial gradient. The scalar field's cosmological energy density mimics dark matter.

### What this means for perturbation growth

Without a cosmological EFE:
- Perturbations are in the deep-MOND regime from the start
- Growth is enhanced: roughly delta ~ a^2 in Einstein-de Sitter (vs. delta ~ a in Newtonian with dark matter)
- This produces TOO MUCH structure (sigma_8 overshoot by factor of ~2, per Nusser 2002)
- Regulation must come from somewhere else: nonlinear effects, virialization, or the specific relativistic theory chosen

### The gap in the literature

**No paper has explicitly computed:**
1. The full MOND perturbation equation including both spatial and temporal background contributions
2. Whether the time-dependent scalar field in relativistic MOND provides an effective x_bar that regulates the growth rate in the same way as a galactic EFE
3. A systematic comparison between the no-EFE growth rate and the EFE-regulated growth rate in cosmological MOND

This gap is exactly what DFD may fill through the K-sector (temporal) dynamics.

---

## 13. IMPLICATIONS FOR DFD P(k) CLOSURE

### The DFD advantage

DFD has BOTH sectors:
- The Psi-sector (spatial, analogous to AQUAL/QUMOND): nabla Phi_bar = 0 in FRW, so no spatial EFE
- The K-sector (temporal): Delta(eta) evolves in time, and the temporal dynamics may provide the "missing" EFE

### What the literature tells us

1. **The Jeans swindle is valid in the Psi-sector** (confirmed by this literature and by R4_jeans_swindle_mond.md)
2. **There is no spatial cosmological EFE** (confirmed universally)
3. **A temporal EFE-analogue may exist** (suggested by TeVeS/AeST scalar field dynamics)
4. **Without regulation, structure forms too fast** (confirmed by Nusser 2002, Sanders 2001)
5. **The relativistic theory matters** -- different relativistic completions of MOND give qualitatively different cosmological predictions

### The key question for DFD

Does the K-sector temporal dynamics provide the self-consistent x_bar that the R2/R3 agents computed? The literature is consistent with this possibility but does not confirm or deny it, because no previous MOND theory has the exact DFD K-sector structure.

The fact that AeST (Skordis & Zlosnik 2021) succeeds in matching the CMB and P(k) through a scalar field that mimics dark matter cosmologically -- while providing MOND in galaxies -- suggests that the "right" answer involves a temporal field that provides effective dark-matter-like behavior on large scales. DFD's K-sector (Delta field) may accomplish exactly this.

---

## REFERENCES

1. Bekenstein, J. & Milgrom, M. (1984). ApJ 286, 7. -- Original AQUAL paper
2. Sanders, R. H. (2001). ApJ 560, 1. [astro-ph/0011439] -- MOND cosmic structure formation
3. Nusser, A. (2002). MNRAS 331, 909. [astro-ph/0109016] -- MOND N-body simulations
4. Skordis, C. (2006). Phys. Rev. D74, 103513. [astro-ph/0511591] -- TeVeS cosmology
5. Skordis, C. (2008). Phys. Rev. D77, 123502. [arXiv: 0801.1985] -- Generalized TeVeS
6. Skordis, C. (2009). Class. Quant. Grav. 26, 143001. [arXiv: 0903.3602] -- TeVeS review
7. Llinares, C., Knebe, A. & Zhao, H. (2008). MNRAS 391, 1778. [arXiv: 0809.2899] -- MOND N-body code
8. Milgrom, M. (2010). MNRAS 403, 886. -- QUMOND formulation
9. Milgrom, M. (2010). Phys. Rev. D82, 043523. [arXiv: 1006.3809] -- BIMOND cosmological fluctuations
10. Angus, G. & Diaferio, A. (2011). MNRAS 417, 941. -- QUMOND cosmological simulations
11. Famaey, B. & McGaugh, S. S. (2012). Living Rev. Rel. 15, 10. [arXiv: 1112.3960] -- MOND review
12. Katz, H., McGaugh, S., Teuben, P. & Angus, G. (2013). ApJ 772, 10. [arXiv: 1305.3651] -- QUMOND cluster simulations
13. Milgrom, M. (2014). Scholarpedia 9, 31410. -- MOND paradigm article
14. Milgrom, M. (2015). Can. J. Phys. 93, 107. [arXiv: 1404.7661] -- MOND theory review
15. Skordis, C. & Zlosnik, T. (2021). Phys. Rev. Lett. 127, 161302. [arXiv: 2007.00082] -- AeST theory
16. Hees, A. & Famaey, B. (2007). arXiv: 0710.3898 -- MOND Lagrangians, perturbations, EFE
17. (2024). arXiv: 2410.10205 -- Cosmological perturbations of relativistic MOND
18. (2023). arXiv: 2303.00038 -- Consistent structure formation in relativistic MOND extensions
