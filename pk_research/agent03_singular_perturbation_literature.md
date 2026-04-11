# Agent 03: Singular Perturbation Theory Literature Review

## The Problem Statement

In DFD, the cosmological background is homogeneous FRW with nabla-psi-bar = 0. The mu function is mu(x) = x/(1+x), so mu(0) = 0 and mu'(0) = 1. The MOND-like field equation:

    div[mu(|grad psi|) grad psi] = S

becomes **degenerate** at the background because mu(0) = 0. Standard linearization produces a 1/mu_0 divergence, breaking cosmological perturbation theory. This document surveys the mathematical and physical literature for techniques to handle this singularity.

---

## 1. Singular Perturbation Theory and Matched Asymptotics

### 1.1 Classical Framework (Bender-Orszag, Hinch, Van Dyke)

The canonical references for singular perturbation theory are:

- **Bender & Orszag** (1978), *Advanced Mathematical Methods for Scientists and Engineers*, Springer. Covers asymptotic expansions, boundary layer theory, WKB methods, and matched asymptotic expansions. The key insight: when a small parameter epsilon multiplies the highest derivative, the "outer" solution (setting epsilon = 0) fails to satisfy all boundary conditions, requiring an "inner" solution in a rescaled boundary layer.

- **Hinch** (1991), *Perturbation Methods*, Cambridge University Press. Emphasizes that there is no single best method -- one must exploit the small parameter given experience. Covers iterations, expansions, singular problems, rescaling, non-integral powers, and logarithmic corrections. The philosophy is physical understanding of subtle balances rather than purely formal mathematics.

- **Van Dyke** (1975), *Perturbation Methods in Fluid Mechanics*, Parabolic Press. The classic on matched asymptotic expansions in fluid dynamics.

### 1.2 Direct Relevance to DFD

The DFD perturbation problem has the structure of a **turning point problem**. In the standard singular perturbation framework:

- A **turning point** is defined as a point where the coefficient of the highest derivative vanishes (Wasow, 1965; Olver, 1974).
- At a turning point, the "outer" (regular perturbation) expansion breaks down.
- The solution requires an **inner expansion** near the turning point using rescaled variables.

For the DFD equation div[mu(|grad psi|) grad psi] = S, the background has |grad psi| = 0, which is precisely a turning point because mu(0) = 0 makes the coefficient of the Laplacian-like term vanish.

**Key technique**: Matched asymptotic expansions divide the domain (or parameter space) into:
- **Outer region**: where |grad psi| is large enough that mu is non-degenerate (e.g., inside galaxies).
- **Inner region**: near the background where |grad psi| ~ 0 and mu(x) ~ x (the deep-MOND regime).
- **Matching condition**: the inner and outer solutions must agree in an overlap region.

### 1.3 The Langer Transformation

For WKB-type problems with turning points, Langer (1937) showed that the WKB approximation breaks down at classical turning points where E = V(x), producing divergent solutions. He introduced a variable transformation that maps the turning point to a regular problem solvable in terms of Airy functions. This is directly relevant to cosmological perturbation theory: Martin (2004, Phys. Rev. D 67, 083512) applied modified WKB methods with Langer-type corrections to inflationary perturbation spectra. The same approach may be needed for DFD perturbations near the mu = 0 background.

### 1.4 Multiple Turning Points

Recent work by Cheng et al. (2024, Boundary Value Problems, Springer) analyzes singular perturbation problems with multiple turning points, using matched asymptotic expansions to construct composite expansions. If the DFD perturbation problem exhibits turning points at multiple scales (e.g., at the background AND at the MOND-Newtonian transition), this formalism would be needed.

---

## 2. Degenerate Elliptic PDEs

### 2.1 The p-Laplacian and Its Generalizations

The DFD field equation is closely related to the **p-Laplacian** and its generalizations. The p-Laplace operator:

    div(|grad u|^{p-2} grad u) = f

is degenerate elliptic when p > 2 (the coefficient |grad u|^{p-2} vanishes at grad u = 0). The DFD equation with mu(x) = x/(1+x) has similar structure -- the effective "diffusion coefficient" mu(|grad psi|) vanishes when the gradient vanishes.

**Critical regularity results**:

- **Araujo, Ricarte, Teixeira** (2022, Archive for Rational Mechanics and Analysis): "On the Critical Point Regularity for Degenerate Diffusive Equations." Key finding: if the source term is away from zero, solutions can never be smoother than C^{p'} at critical points (where the gradient vanishes). At zero-source critical points, higher regularity holds, sharp with respect to source vanishing rate. **This directly constrains the regularity of DFD perturbations near the homogeneous background.**

- **Pimentel & Teixeira** (2022, Advances in Mathematics): C1-regularity for degenerate diffusion equations. Established optimal regularity for equations with gradient-dependent degeneracy using a new "shoring-up" technique that prevents degeneracy laws from collapsing.

- **De Filippis et al.** (2025, J. Geometric Analysis): Gradient regularity for p-Laplacian equations with logarithmic perturbation, extending regularity theory under weak assumptions on domain boundary and variable exponent.

### 2.2 Widely Degenerate Elliptic Equations

A particularly relevant class is **widely degenerate** elliptic equations (Santambrogio & Scheven, 2025, Partial Differential Equations and Applications), where the diffusion coefficient vanishes on an entire set rather than at isolated points. The DFD cosmological background has grad psi = 0 everywhere (homogeneous), making this a case of **maximal degeneracy** -- the equation degenerates on the entire spatial domain.

### 2.3 Free Boundary Problems with Gradient Thresholds

Recent work on **free boundary problems** with gradient activation (2025, Journal of Functional Analysis) studies fully nonlinear elliptic equations where the diffusion process is driven only in the region where the gradient surpasses a given threshold. This is mathematically analogous to the DFD problem: in a homogeneous background, the "diffusion" (gravitational response) is turned off, and perturbations must exceed a threshold to activate the nonlinear gravitational dynamics.

### 2.4 Viscosity Solutions

The theory of **viscosity solutions** (Crandall & Lions, 1980s) provides the correct framework for well-posedness of degenerate elliptic PDEs:

- **Crandall, Ishii, Lions** (1992), "User's Guide to Viscosity Solutions," Bull. AMS. The foundational reference.
- Existence is typically obtained through the **Perron method**.
- Uniqueness requires careful analysis; Jensen's result was the first for second-order equations.
- The concept of **kappa-grad viscosity solutions** weakens the solution concept by disregarding test functions whose slope at touching points is below a threshold kappa -- directly relevant when mu vanishes at zero gradient.

---

## 3. Epsilon-Regularization Approaches

### 3.1 Vanishing Viscosity Method

A standard technique for degenerate elliptic PDEs is **epsilon-regularization**: replace mu(x) with mu_epsilon(x) = mu(x) + epsilon, solve the non-degenerate problem, then take epsilon -> 0.

For the DFD equation, this means:

    div[(mu(|grad psi|) + epsilon) grad psi] = S

The regularized equation is uniformly elliptic for any epsilon > 0, admits standard perturbation theory, and one studies convergence as epsilon -> 0.

**Key references**:
- Jakobsen & Karlsen (2005): Established convergence rates for the vanishing viscosity method for fully nonlinear degenerate elliptic equations.
- de Arcangelis & Lopes-Brandao (2025): Recent numerical methods for degenerate diffusions where the degeneracy is governed by gradient vanishing, using decoupling strategies to unlock monotonicity.

### 3.2 Application to DFD P(k)

**This is likely the most promising immediate approach for DFD**: compute P(k) using the epsilon-regularized equation, obtain a power spectrum P_epsilon(k), then study the limit epsilon -> 0. The physical interpretation of epsilon would be a small "vacuum conductivity" or minimum gravitational response.

If P_epsilon(k) has a well-defined limit as epsilon -> 0, the singularity is removable and standard perturbation theory gives the correct answer despite the formal divergence. If the limit is singular, the problem requires genuine nonlinear analysis.

---

## 4. MOND / AQUAL Cosmological Perturbation Theory

### 4.1 The AQUAL Problem

The Bekenstein-Milgrom (1984) AQUAL theory replaces the Poisson equation with:

    div[mu(|grad Phi|/a_0) grad Phi] = 4 pi G rho

This has **exactly the same degeneracy problem** as DFD in cosmology. Key findings from the MOND literature:

- **Felten (1984)** and subsequent authors noted that AQUAL, which changes the Poisson equation, must be amended to preserve the cosmological principle. When the Poisson equation is modified with a nonlinear function of the gradient, the symmetries ensuring homogeneity of the universe are lost.

- **Milgrom (2010)** introduced **QUMOND** (Quasi-linear MOND) partly to avoid this problem. In QUMOND, the field equation is a standard Poisson equation with a modified right-hand side that depends only on the Newtonian potential (not on the MOND potential's own gradient). This absorbs the nonlinearity onto the source side, where it does not cause the same degeneracy at zero gradient.

**Lesson for DFD**: The MOND community recognized that the AQUAL-type nonlinear Poisson equation is pathological in cosmology precisely because of the gradient degeneracy. QUMOND-type reformulations avoid this by moving the nonlinearity to the source term. **Does DFD admit an analogous reformulation?**

### 4.2 Famaey & McGaugh (2012) Review

The comprehensive Living Reviews article (Living Rev. Relativity 15, 10) summarizes the state of MOND/AQUAL cosmological perturbation theory:
- Density perturbations in MOND may grow so rapidly that too much structure is formed by the present epoch.
- Weak gravitational fields with very small gradients lead to numerical difficulties in the nonlinear AQUAL formulation.
- This is specifically identified as a fundamental challenge for structure formation calculations.

### 4.3 Skordis & Zlosnik: AeST Theory (2020-2024)

The Aether Scalar Tensor (AeST) theory represents the most successful modern attempt to embed MOND in a relativistic framework that works cosmologically:

- **Skordis & Zlosnik** (2021, Phys. Rev. Lett. 127, 161302): "A new relativistic theory for Modified Newtonian Dynamics." Demonstrated agreement with CMB and matter power spectra on linear cosmological scales. The key achievement: the action expanded to second order is free of ghost instabilities.

- **Crucial technique**: In the early Universe, the gravity-modifying fields generate a gravitational effect that **mimics dark matter** -- the scalar and vector fields conspire to produce an effective dark-matter-like perturbation even though mu ~ 0 at the background level. This is accomplished by the extra degrees of freedom (vector field, scalar field) providing the perturbation dynamics that the degenerate mu function cannot.

- **Skordis & Zlosnik** (2023, arXiv:2307.15126): Hamiltonian formalism for AeST. Establishes well-posedness through careful constraint analysis.

- **Thomas, Mozaffari, Zlosnik** (2023, arXiv:2303.00038): "Consistent cosmological structure formation on all scales in relativistic extensions of MOND." Studies how to coherently connect large-scale linear perturbation theory, nonlinear structure formation, and galactic dynamics.

- **Durakovic & Zlosnik** (2024, arXiv:2402.04091): Sudden cosmological singularities in AeST. Shows that certain parameter choices lead to singularities in the second time derivative of the scale factor, induced by the scalar field at the level of the homogeneous background.

**Key lesson for DFD**: AeST handles the mu = 0 degeneracy by having additional dynamical fields (vector, scalar) whose perturbations remain well-defined even when mu degenerates. The perturbation dynamics is carried by these extra fields, not by the mu function alone. **DFD may need an analogous mechanism -- identifying which degrees of freedom carry the perturbation dynamics when mu(0) = 0.**

### 4.4 Cosmological Perturbations in Relativistic MOND (2024)

Durakovic et al. (2024, arXiv:2410.10205): "Cosmological perturbations of a relativistic MOND theory." Shows that to 0PN order, baryon perturbation grows faster in the MOND regime, and the MOND field can be interpreted as a fluid with a specific equation of state without anisotropic stress. This suggests a path for DFD: interpret the psi field perturbation as an effective fluid and derive its equation of state near the degenerate background.

---

## 5. Modified Gravity Perturbation Theory: Lessons from Other Theories

### 5.1 f(R) Gravity

Hwang & Noh (2013, arXiv:1303.6828): "Cosmological perturbations in F(R) gravity." f(R) theories modify the Einstein-Hilbert action by replacing R with a general function f(R). The perturbation theory:
- Involves a **scalaron** (extra scalar degree of freedom from the f(R) modification).
- Can encounter singular behavior when f''(R) = 0 (analogous to the mu = 0 degeneracy in DFD).
- Physical viability requires f''(R) > 0 and f'(R) > 0 to avoid ghost and tachyonic instabilities.

**Stability analysis around critical points** uses eigenvalues of the Jacobian matrix of the perturbation equations. Points where eigenvalues change sign correspond to instabilities or singularities in the perturbation expansion.

### 5.2 Brans-Dicke Theory

The Brans-Dicke theory parameter omega controls coupling between the scalar field and geometry:
- GR is recovered in the limit omega -> infinity.
- The perturbation equations depend on omega, and the limit omega -> infinity is **singular** (the scalar field equation changes character).
- At omega = -3/2, the theory becomes conformally invariant -- another singular point.

**Direct analogy to DFD**: The omega -> infinity limit of Brans-Dicke is like the |grad psi| -> 0 limit of DFD. In both cases, the perturbation theory of the "reduced" theory (GR / homogeneous DFD) does not capture the physics of the full theory near the singular limit. One must keep the full theory and take the limit carefully.

Recent work: Akarsu et al. (2025, arXiv:2601.22937): "Linear perturbation theory and structure formation in a Brans-Dicke theory of gravity without dark matter" -- demonstrates that careful treatment of the omega-dependent terms is essential for correct structure formation predictions.

### 5.3 TeVeS (Tensor-Vector-Scalar)

Bekenstein's (2004) TeVeS employs a unit vector field, dynamical and non-dynamical scalar fields, a free function, and a non-Einsteinian metric. The perturbation theory:
- Must handle the nonlinear free function (analogous to mu).
- The vector field's unit-norm constraint introduces constraints at the perturbation level.
- Sanders (2006) and Dodelson & Liguori (2006) showed that TeVeS perturbations alone could not reproduce the CMB power spectrum, motivating AeST.

---

## 6. Critical Phenomena and Renormalization Group

### 6.1 Analogy with Phase Transitions

The point mu(0) = 0 in DFD can be viewed as analogous to a **critical point** in statistical mechanics:
- At a critical point, the "susceptibility" diverges (like 1/mu_0 diverging in DFD).
- Mean-field theory breaks down near the critical point (like linearized perturbation theory breaking down in DFD).
- The renormalization group provides systematic corrections beyond mean field.

**Wilson's epsilon expansion** (Nobel lecture, 1982): The epsilon expansion about four dimensions gave reasonable qualitative results for three-dimensional systems and enabled much greater variety of details of critical behavior to be studied. The key insight is that critical exponents are **universal** -- they depend only on symmetry and dimensionality, not on microscopic details.

### 6.2 Potential RG Approach to DFD

A possible RG-inspired approach to the DFD P(k) problem:
1. Identify the "fixed point" corresponding to mu(0) = 0.
2. Classify perturbations as **relevant** (growing away from the fixed point) or **irrelevant** (decaying toward it).
3. Compute **anomalous dimensions** that modify the naive scaling of P(k).
4. The "critical exponent" would determine how P(k) behaves at large scales (low k) where perturbations are weakest and the mu = 0 degeneracy is most severe.

This is speculative but the mathematical structure is suggestive. The mu function's behavior mu(x) ~ x for small x defines a **critical exponent** of 1 (linear vanishing), which would place the DFD theory in a specific universality class for the perturbation expansion.

---

## 7. The Porous Medium Equation Analogy

### 7.1 Mathematical Structure

The **porous medium equation** (PME):

    du/dt = div(u^m grad u),  m > 0

is the prototypical degenerate parabolic equation. When u = 0 somewhere, the equation degenerates. Key properties:
- **Finite speed of propagation** (unlike the heat equation).
- **Free boundary** separating u > 0 from u = 0.
- Solutions are only Holder continuous, not smooth, at the free boundary.

The comprehensive reference is Vazquez (2007), *The Porous Medium Equation: Mathematical Theory*, Oxford University Press.

### 7.2 Relevance to DFD

The DFD equation div[mu(|grad psi|) grad psi] = S, with mu(0) = 0, shares the PME's degenerate character. Key implications:
- Perturbations of the homogeneous background may propagate at **finite speed**, not instantaneously.
- The perturbation solution may only be Holder continuous, not smooth.
- A **free boundary** may separate the "activated" region (where |grad psi| > 0, gravity is operational) from the degenerate region.
- Standard Fourier-space perturbation theory (which assumes smoothness and infinite propagation) may be fundamentally inadequate.

---

## 8. Synthesis: Recommended Approaches for DFD P(k)

Based on this literature review, the following approaches are recommended for resolving the DFD P(k) singularity, in order of increasing mathematical sophistication:

### Approach A: Epsilon-Regularization (Most Accessible)
Replace mu(x) with mu(x) + epsilon, compute P_epsilon(k) using standard linear perturbation theory, then study epsilon -> 0. The regularized problem is uniformly elliptic and admits standard Fourier analysis. If the limit exists, the singularity is benign.

### Approach B: QUMOND-Type Reformulation
Following Milgrom's QUMOND strategy, reformulate the DFD field equation so the nonlinearity appears on the source side rather than the coefficient side. This may remove the degeneracy entirely from the perturbation equation. Check whether the DFD Lagrangian admits such a reformulation.

### Approach C: Matched Asymptotic Expansions
Divide the perturbation solution into:
- **Inner solution**: near |grad psi| = 0, where mu(x) ~ x and the equation is div[|grad psi| grad psi] = S (a p-Laplacian-like equation with p = 3).
- **Outer solution**: where |grad psi| >> 1 and mu ~ 1, recovering standard Newtonian gravity.
- **Matching**: in an intermediate zone where both expansions overlap.
This would give P(k) as a composite of different regimes.

### Approach D: Extra Degree of Freedom (AeST-Inspired)
Following the Skordis-Zlosnik strategy, identify whether DFD's full relativistic formulation contains additional dynamical fields whose perturbations remain well-defined at the mu = 0 background. These fields would carry the perturbation dynamics and produce an effective matter-like power spectrum even when mu degenerates.

### Approach E: Viscosity Solution / Free Boundary Approach
Treat the DFD perturbation equation in the viscosity solution framework, acknowledging that:
- Solutions may only be Holder continuous, not smooth.
- A free boundary may separate activated from degenerate regions.
- Fourier analysis must be replaced by real-space methods (e.g., De Giorgi-Nash-Moser theory).

### Approach F: Renormalization Group (Most Speculative)
Treat the mu = 0 point as a critical point and compute anomalous scaling corrections to P(k) using RG methods. The critical exponent of mu (linear vanishing) would determine the universality class and the modified large-scale behavior of P(k).

---

## 9. Key References (Consolidated)

### Singular Perturbation Theory
1. Bender, C.M. & Orszag, S.A. (1978). *Advanced Mathematical Methods for Scientists and Engineers*. Springer.
2. Hinch, E.J. (1991). *Perturbation Methods*. Cambridge University Press.
3. Van Dyke, M. (1975). *Perturbation Methods in Fluid Mechanics*. Parabolic Press.
4. Wasow, W. (1965). *Asymptotic Expansions for Ordinary Differential Equations*. Wiley.
5. Langer, R.E. (1937). "On the connection formulas and the solutions of the wave equation." Phys. Rev. 51, 669.
6. Hunter, J.K. *Asymptotic Analysis and Singular Perturbation Theory*. UC Davis lecture notes. https://www.math.ucdavis.edu/~hunter/notes/asy.pdf

### Degenerate Elliptic PDEs
7. Araujo, Ricarte, Teixeira (2022). "On the Critical Point Regularity for Degenerate Diffusive Equations." Arch. Rational Mech. Anal.
8. Pimentel & Teixeira (2022). "C1-regularity for degenerate diffusion equations." Advances in Mathematics.
9. Crandall, M.G., Ishii, H., Lions, P.-L. (1992). "User's Guide to Viscosity Solutions." Bull. AMS.
10. Vazquez, J.L. (2007). *The Porous Medium Equation: Mathematical Theory*. Oxford University Press.
11. Santambrogio & Scheven (2025). "Gradient regularity for widely degenerate elliptic PDEs." Partial Differential Equations and Applications.

### MOND / AQUAL / AeST
12. Bekenstein, J. & Milgrom, M. (1984). "Does the missing mass problem signal the breakdown of Newtonian gravity?" ApJ 286, 7.
13. Milgrom, M. (2010). "Quasi-linear formulation of MOND." MNRAS 403, 886.
14. Famaey, B. & McGaugh, S.S. (2012). "Modified Newtonian Dynamics (MOND): Observational Phenomenology and Relativistic Extensions." Living Rev. Relativity 15, 10.
15. Skordis, C. & Zlosnik, T. (2021). "New Relativistic Theory for Modified Newtonian Dynamics." Phys. Rev. Lett. 127, 161302.
16. Skordis, C. & Zlosnik, T. (2023). "Aether Scalar Tensor theory: Hamiltonian Formalism." arXiv:2307.15126.
17. Thomas, Mozaffari, Zlosnik (2023). "Consistent cosmological structure formation on all scales in relativistic extensions of MOND." arXiv:2303.00038.
18. Durakovic et al. (2024). "Cosmological perturbations of a relativistic MOND theory." arXiv:2410.10205.
19. Durakovic & Zlosnik (2024). "Sudden cosmological singularities in AeST." arXiv:2402.04091.
20. Famaey & Durakovica (2025). "Modified Newtonian Dynamics (MOND)." arXiv:2501.17006.

### Modified Gravity
21. Hwang & Noh (2013). "Cosmological perturbations in F(R) gravity." arXiv:1303.6828.
22. Akarsu et al. (2025). "Linear perturbation theory and structure formation in Brans-Dicke theory." arXiv:2601.22937.
23. Bekenstein, J. (2004). "Relativistic gravitation theory for the MOND paradigm." Phys. Rev. D 70, 083509.

### Critical Phenomena / RG
24. Wilson, K.G. (1983). "The Renormalization Group and Critical Phenomena." Nobel Lecture, Rev. Mod. Phys. 55, 583.
25. Goldenfeld, N. (1992). *Lectures on Phase Transitions and the Renormalization Group*. Addison-Wesley.

### WKB / Cosmological Perturbations
26. Martin, J. (2004). "WKB approximation for inflationary cosmological perturbations." Phys. Rev. D 67, 083512.
27. Ambroso, Mehats, Raviart (2001). "On singular perturbation problems for the nonlinear Poisson equation." Asymptotic Analysis.

---

## 10. Summary of Key Insights for DFD

1. **The problem is well-known in MOND theory**: The mu(0) = 0 degeneracy is a recognized obstacle. The MOND community has developed workarounds (QUMOND, AeST) rather than solving it head-on.

2. **Standard perturbation theory genuinely fails**: This is not a removable singularity -- the p-Laplacian regularity theory shows that solutions at critical points (where gradient vanishes) have fundamentally limited smoothness.

3. **The most promising path is epsilon-regularization or QUMOND-type reformulation**: These are the techniques that have actually worked in practice for similar equations.

4. **AeST provides a template**: Skordis-Zlosnik showed that the way to get a working P(k) from a MOND-type theory is to have extra degrees of freedom that carry the perturbation dynamics when mu degenerates. DFD should identify its analogous extra fields.

5. **The inner-outer matching approach could yield analytical P(k)**: By treating the large-scale (small gradient) and small-scale (large gradient) regimes separately and matching, one could obtain a composite P(k) that captures both the degenerate and non-degenerate physics.

6. **Finite propagation speed is expected**: The porous medium equation analogy suggests that DFD perturbations propagate at finite speed, unlike standard gravitational perturbations. This would modify P(k) at large scales.

---

*Agent 03 of 20 -- Literature Research on Singular Perturbation Theory*
*Generated: 2026-04-04*
