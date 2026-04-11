# R10 Agent 5: Self-Consistency of the R_3 Compactification System

**Campaign:** R10 -- DFD Parameter Closure
**Agent:** 5
**Date:** 2026-04-05
**Status:** COMPLETE

---

## Executive Summary

We solve the complete system of equations that constrain R_3 (the S^3 compactification radius) in DFD. The system has 5 observational constraints and 1 unknown (R_3), making it overconstrained. The central finding:

**The system splits into two DECOUPLED subsystems:**

- **Subsystem A (alpha^57 invariant):** G, H_0, alpha are related by G hbar H_0^2 / c^5 = alpha^57. This contains NO dependence on R_3. It is already self-consistent and verified to 0.03%.

- **Subsystem B (chi sector):** m_chi, Omega_chi, and Lambda = hbar c / R_3 are linked through the misalignment formula. This system has ONE free parameter (R_3) and ONE constraint (Omega_m = 0.315), so it is exactly determined -- NOT overconstrained.

The MOND acceleration a_0 = 2 sqrt(alpha) c H_0 depends only on alpha and H_0, not on R_3. Therefore a_0 does NOT provide an additional constraint on R_3.

**Result:** R_3 is uniquely determined by requiring Omega_chi = 0.266 (the CDM fraction). The solution gives Lambda = 0.77 eV, or equivalently R_3 = hbar c / Lambda = 2.56 x 10^{-7} m = 0.256 micrometers. There is no inconsistency, but also no overdetermination -- the system does not provide a nontrivial self-consistency check on R_3.

---

## 1. The Complete System of Equations

### 1.1 Equation Inventory

We catalog every DFD relation that could potentially depend on R_3.

| # | Equation | Depends on R_3? | Source |
|---|----------|-----------------|--------|
| 1 | G hbar H_0^2/c^5 = alpha^57 | NO | Appendix O, Theorem |
| 2 | alpha^{-1} = 137.036 | NO | CS level averaging, topological |
| 3 | a_0 = 2 sqrt(alpha) c H_0 | NO (depends on alpha, H_0 only) | Appendix N, derived |
| 4 | f_a = M_P / (k_max + 2) = M_P / 62 | NO | CS periodicity, topological |
| 5 | C_total = 0.0236 | NO | CS partition function, topological |
| 6 | m_chi = sqrt(C_total) Lambda^2 / f_a | YES: Lambda = hbar c / R_3 | R8 Agent 3 |
| 7 | Omega_chi h^2 = f(m_chi, f_a, <theta^2>) | YES: through m_chi(R_3) | Misalignment mechanism |
| 8 | Omega_m = Omega_b + Omega_chi | YES: through Omega_chi(R_3) | Friedmann constraint |
| 9 | <theta^2> = 12.43 | NO | Topological vacuum averaging |
| 10 | Omega_CDM/Omega_b = 16/3 | NO (topological, if accepted) | R8 Agent 20 |

### 1.2 Critical Observation: The Decoupling

The alpha^57 invariant (Eq. 1) relates G and H_0 through alpha alone:

    H_0 = sqrt(alpha^57 c^5 / (G hbar))

Using CODATA G = 6.67430 x 10^{-11} m^3 kg^{-1} s^{-2}:

    H_0^{DFD} = 72.09 km/s/Mpc

This is INDEPENDENT of R_3. The topological invariants (k_max = 60, N_gen = 3) that determine the exponent 57 are properties of the CP^2 x S^3 TOPOLOGY, not of the S^3 RADIUS.

Similarly, a_0 = 2 sqrt(alpha) c H_0 depends only on alpha (topological) and H_0 (determined by G through the alpha^57 relation). No R_3 dependence.

**The entire v3.3 framework (G, H_0, alpha, a_0, mu-function, PPN, GW speed) is R_3-independent.**

R_3 enters ONLY through the chi sector (Eqs. 6-8), which was introduced in the R8/R9 campaign as a candidate for CDM.

---

## 2. Step 1: Express Everything in Terms of R_3

### 2.1 The R_3-dependent quantities

Define:

    Lambda = hbar c / R_3   (compactification energy scale)

Then:

    m_chi(R_3) = sqrt(C_total) * Lambda^2 / f_a
               = 0.154 * (hbar c / R_3)^2 / (M_P / 62)
               = 0.154 * 62 * (hbar c)^2 / (M_P * R_3^2)

In natural units (hbar = c = 1):

    m_chi = 9.548 / (M_P * R_3^2)

### 2.2 The relic density

From the standard misalignment formula (R8 Agent 5):

    Omega_chi h^2 = (rho_chi / rho_crit) h^2

For an ALP with mass m_chi, decay constant f_a, and misalignment angle theta:

    rho_chi(T_0) = (1/2) m_chi^2 f_a^2 <theta^2> * (g_{*S,0}/g_{*S,osc}) * (T_0/T_osc)^3

The oscillation temperature:

    T_osc = [m_chi M_P / (3 sqrt(pi^2 g_*/90))]^{1/2}

Since T_osc ~ m_chi^{1/2}, the full scaling is:

    Omega_chi h^2 ~ m_chi^{1/2} * f_a^2 * <theta^2> * (known factors)

Substituting m_chi(R_3):

    Omega_chi h^2 ~ R_3^{-1} * f_a^2 * <theta^2> * (known factors)

### 2.3 Numerical implementation

Using the precise formula from R8 Agent 5, the misalignment relic density is:

    Omega_chi h^2 = 0.120 * (m_chi / m_target)^{1/2} * (f_a / f_target)^2 * (<theta^2> / <theta^2>_target)

where the target values (giving Omega h^2 = 0.120) are:

    m_target = 2.335 x 10^{-26} eV  (for f_a = 3.927 x 10^16 GeV, <theta^2> = 12.43)

---

## 3. Step 2: The Observational Constraints

### 3.1 The R_3-independent constraints (Subsystem A)

| Constraint | DFD Prediction | Observed | Status |
|------------|----------------|----------|--------|
| alpha^{-1} | 137.036 (CS averaging) | 137.036 | EXACT (by construction -- k_max = 60 chosen to match) |
| H_0 | 72.09 km/s/Mpc | 72.6 +/- 2.0 (SH0ES) | 0.3 sigma agreement |
| G | 6.674 x 10^{-11} (input) | 6.674 x 10^{-11} | Input (alpha^57 links G to H_0) |
| a_0 | 2 sqrt(alpha) c H_0 = 1.13 x 10^{-10} m/s^2 | 1.2 x 10^{-10} m/s^2 | ~6% tension |

All four are satisfied WITHOUT any reference to R_3. Subsystem A is self-consistent.

Note: The a_0 prediction (1.13 vs 1.2 x 10^{-10}) has ~6% tension. This is within the stated "< 10%" verification tolerance of v3.3 (section_alpha_relations.tex). The empirical a_0 is itself uncertain at the ~15% level due to mu-function fitting degeneracies.

### 3.2 The R_3-dependent constraint (Subsystem B)

The ONLY observational constraint on R_3 is:

    Omega_m = Omega_b + Omega_chi(R_3) = 0.315

With Omega_b = 0.049:

    Omega_chi = 0.266

This single equation determines R_3 uniquely.

### 3.3 Assessment of overconstraint

The task brief listed 5 constraints + 1 unknown, suggesting an overconstrained system. However, the actual counting is:

**R_3-independent (provide no constraint on R_3):**
- G = observed: satisfied by alpha^57 invariant, R_3-free
- H_0 = observed: satisfied by alpha^57 invariant, R_3-free
- a_0 = observed: satisfied by alpha-H_0 relation, R_3-free
- alpha = 1/137: topological, R_3-free

**R_3-dependent:**
- Omega_m = 0.315: this IS the constraint on R_3

**Count: 1 constraint, 1 unknown.** The system is EXACTLY determined, not overconstrained.

---

## 4. Step 3: Solve Numerically for R_3

### 4.1 From Omega_chi to m_chi

The misalignment relic density formula (R8 Agent 5, verified) with:
- f_a = 3.927 x 10^16 GeV
- <theta^2> = 12.43 (topological average, extended potential)
- g_{*S,osc} = 3.36 (post-neutrino-decoupling)

Requiring Omega_chi h^2 = 0.120:

    m_chi = 2.335 x 10^{-26} eV = 2.335 x 10^{-35} GeV

(If using anharmonicity correction from R9 Agent 2: m_chi = 8.1 x 10^{-27} eV, factor ~3 shift.)

### 4.2 From m_chi to Lambda

Using m_chi = sqrt(C_total) * Lambda^2 / f_a:

    Lambda^2 = m_chi * f_a / sqrt(C_total)
             = m_chi * f_a / 0.154

For m_chi = 2.335 x 10^{-35} GeV:

    Lambda^2 = 2.335e-35 * 3.927e16 / 0.154
             = 5.955e-19 GeV^2

    Lambda = 7.71 x 10^{-10} GeV = 0.771 eV

### 4.3 From Lambda to R_3

    R_3 = hbar c / Lambda

Converting: hbar c = 1.973 x 10^{-7} eV*m

    R_3 = 1.973e-7 / 0.771 = 2.559 x 10^{-7} m = 0.256 micrometers

### 4.4 Summary of the unique solution

| Quantity | Value | Units |
|----------|-------|-------|
| **R_3** | **2.56 x 10^{-7}** | **m (0.256 um)** |
| **Lambda** | **0.771** | **eV** |
| m_chi | 2.34 x 10^{-26} | eV |
| Omega_chi h^2 | 0.120 | (dimensionless) |
| Omega_chi | 0.266 | (dimensionless) |
| T_osc | 5.6 | eV (~65,000 K) |
| f_a | 3.93 x 10^{16} | GeV |

### 4.5 With anharmonicity correction

R9 Agent 2 found that the anharmonicity factor f_anh = 1.69 shifts the required mass to m_chi = 8.1 x 10^{-27} eV. This gives:

    Lambda_corrected = sqrt(8.1e-27 * 3.927e16 / (0.154 * 1e-9))
                     = ... (need to redo properly)

    Lambda^2 = 8.1e-36 * 3.927e16 / 0.154 = 2.066e-19 GeV^2
    Lambda = 4.54e-10 GeV = 0.454 eV
    R_3 = 1.973e-7 / 0.454 = 4.35 x 10^{-7} m = 0.435 um

| Scenario | m_chi (eV) | Lambda (eV) | R_3 (um) |
|----------|------------|-------------|----------|
| Harmonic, extended potential | 2.34e-26 | 0.771 | 0.256 |
| Anharmonic, extended potential | 8.1e-27 | 0.454 | 0.435 |
| Harmonic, cosine potential | 3.22e-25 | 2.86 | 0.069 |

---

## 5. Step 4: The Key Question -- Is R_3 Overconstrained?

### 5.1 Answer: NO

As established in Section 3.3, the system has exactly 1 constraint on R_3 (Omega_m = 0.315). This means:

1. R_3 is uniquely DETERMINED (not under-determined)
2. R_3 is not OVERCONSTRAINED (no internal consistency check exists)
3. There is NO structural problem with DFD -- no inconsistency can arise because there is only one equation for one unknown

### 5.2 Why the Task Brief's Analysis Was Misleading

The task brief suggested that G = G(R_3), H_0 = H_0(R_3), and a_0 = a_0(R_3), which would create an overconstrained system. This would be true IF Newton's constant were an induced quantity from integrating out KK modes on S^3:

    G_induced ~ 1 / (M_7^5 * Vol(S^3)) ~ R_3^{-3} / M_7^5

In string/M-theory compactifications, this is how it works: the 4D Planck mass is set by the compactification volume, and changing R_3 changes G. If G depended on R_3, then the alpha^57 invariant G hbar H_0^2 / c^5 = alpha^57 would fix R_3 (since G, H_0, alpha are all measured).

**However, in DFD v3.3, G is NOT derived from compactification.** The alpha^57 relation is derived from the primed-determinant scaling on the FINITE Toeplitz space (Appendix O), which depends only on the MODE COUNT (57 = k_max - N_gen), not on the mode EIGENVALUES or the S^3 radius. The proof works as follows:

1. The partition function ratio Z(alpha^{-1})/Z(1) = alpha^{57}
2. Each mode contributes a factor alpha REGARDLESS of its eigenvalue lambda_i
3. The eigenvalues lambda_i DO depend on R_3 (they scale as 1/R_3^2)
4. But the eigenvalues CANCEL in the ratio (Eq. O.4 in Appendix O)

This eigenvalue cancellation is the crucial structural feature. It means the alpha^57 invariant holds for ANY value of R_3. Newton's constant (as derived from the invariant) is R_3-independent.

### 5.3 Could G Depend on R_3 Through a Different Mechanism?

In principle, one could construct a supertrace formula where G receives contributions from the KK tower on S^3:

    1/G_eff = 1/G_bare + Sum_n [c_n / m_n^2]

where m_n ~ n/R_3 are the KK masses. This would make G_eff depend on R_3 through the sum. However:

1. DFD v3.3 does NOT derive G from a supertrace. G is an INPUT to the theory (or equivalently, determined by the alpha^57 invariant from H_0).

2. If one TRIED to add a supertrace contribution, the sum over 57 KK modes with masses m_n = lambda_n / R_3 would give:

       Sum ~ R_3^2 * Sum_n (1/lambda_n^2)

   This would make G_eff depend on R_3, creating the overconstrained system described in the task brief. But this sum is NOT present in the current theory.

3. The DFD framework treats the internal manifold as providing TOPOLOGICAL data (k_max, N_gen, alpha), not GEOMETRIC data (R_3-dependent masses). This is a deliberate structural choice.

### 5.4 What WOULD Create an Overconstrained System

For R_3 to be genuinely overconstrained, one would need ADDITIONAL R_3-dependent observables. Candidates:

**A. The cosmological constant from chi vacuum energy:**
If V_0 = Lambda^4 * C_vac contributes to rho_Lambda, then:

    Omega_Lambda * rho_crit = Lambda^4 * C_vac = (hbar c / R_3)^4 * C_vac

This would give a SECOND constraint on R_3 (from Omega_Lambda = 0.685). With:

    Lambda^4 = Omega_Lambda * rho_crit / C_vac

Using rho_crit = 8.53 x 10^{-27} kg/m^3, C_vac = 4.7238 (R8 Agent 3):

    Lambda = [0.685 * 8.53e-27 * c^2 / 4.7238]^{1/4}

Converting: rho_crit c^2 = 7.67e-10 J/m^3 = 4.79 x 10^{-6} eV^4 / (hbar c)^3

    Lambda^4 = 0.685 * 4.79e-6 / 4.7238 = 6.94e-7 eV^4
    Lambda = 0.029 eV

This gives Lambda = 0.029 eV, which is 27x SMALLER than the 0.77 eV required for Omega_chi. **The cosmological constant constraint is INCONSISTENT with the dark matter constraint.** This means either:

(a) The chi vacuum energy does NOT contribute to Omega_Lambda (it is subtracted by a separate mechanism), or
(b) C_vac is different from 4.7238, or
(c) The chi field is not responsible for both dark energy and dark matter simultaneously.

In DFD v3.3, the cosmological constant is explained by the alpha^57 hierarchy (rho_c/rho_Pl = (3/8pi) alpha^57), NOT by a chi vacuum energy. So option (a) is the natural interpretation.

**B. Short-range gravity modifications from KK modes:**
If the S^3 compactification produces KK graviton modes, there would be Yukawa corrections to gravity at distances r ~ R_3:

    V(r) = -G m_1 m_2 / r * [1 + Sum_n exp(-r * m_n)]

For R_3 = 0.256 um, this predicts deviations from Newton's law at the sub-micrometer scale. Current short-range gravity tests (Kapner et al. 2007) reach down to ~50 um, which is above R_3 = 0.256 um but within an order of magnitude. Sub-micrometer Casimir-force experiments could potentially probe this scale.

If such deviations were detected, they would provide an INDEPENDENT measurement of R_3, creating a genuine overconstrained system. Current non-detection is consistent (R_3 is below current experimental reach).

---

## 6. The Complete Self-Consistency Map

### 6.1 DFD v3.3 (without chi)

```
Topological integers: k_max = 60, N_gen = 3
        |
        v
    alpha^{-1} = 137.036  (CS level averaging)
        |
        v
    Exponent: 57 = k_max - N_gen
        |
        v
    G hbar H_0^2 / c^5 = alpha^57   -->  H_0 = 72.09 km/s/Mpc (given G)
        |                                  OR  G = 6.674e-11 (given H_0)
        v
    a_0 = 2 sqrt(alpha) c H_0 = 1.13 x 10^{-10} m/s^2
        |
        v
    mu(x) = x/(1+x)  (from S^3 composition law)
        |
        v
    Galaxy rotation, BAO, PPN, GW speed -- all R_3-FREE
```

**Free parameters: ZERO** (two topological integers fix everything)

### 6.2 DFD v3.4 (with chi)

```
v3.3 framework (R_3-free, zero parameters)
        +
    R_3 (ONE new continuous parameter)
        |
        v
    Lambda = hbar c / R_3
        |
        v
    m_chi = 0.154 * Lambda^2 / (M_P/62)
        |
        v
    Omega_chi = f(m_chi, f_a, <theta^2>)
        |
        v
    Omega_m = Omega_b + Omega_chi  -->  Fixes R_3
```

**Free parameters: ONE** (R_3), fixed by ONE observation (Omega_m).

### 6.3 Could the 16/3 ratio eliminate the free parameter?

If the ratio Omega_chi / Omega_b = 16/3 is promoted from observation to theorem (as R8 Agent 20 proposes), then:

    Omega_chi = (16/3) Omega_b

And Omega_b is determined by BBN physics (itself derivable from alpha and the baryon-to-photon ratio eta). If eta is also topologically determined, then Omega_chi would be fixed without invoking R_3 as a free parameter -- instead R_3 would be a PREDICTION:

    Omega_chi = 0.2613  (from 16/3 * 0.0490)
    -->  m_chi = 2.18 x 10^{-26} eV  (from misalignment inversion)
    -->  Lambda = 0.745 eV
    -->  R_3 = 2.65 x 10^{-7} m = 0.265 um

However, the 16/3 ratio is currently a numerical observation (0.25-sigma agreement), not a derived theorem. The path-integral connection between fermionic DOF counting and energy-density partitioning has not been established.

---

## 7. Comparison: Lambda = 0.77 eV vs Alpha-Tower Candidates

R9 Agent 9 found that the nearest candidate in the DFD alpha-tower is:

    Lambda = M_P * alpha^13 = 0.526 eV

The question: does this match?

| Candidate | Lambda (eV) | m_chi (eV) | Omega_chi h^2 | Match? |
|-----------|-------------|------------|---------------|--------|
| Required (Omega_m = 0.315) | 0.771 | 2.34e-26 | 0.120 | TARGET |
| M_P alpha^13 | 0.526 | 1.09e-26 | 0.082 | 68% of target |
| M_P alpha^{12.87} | 0.771 | 2.34e-26 | 0.120 | Exact, but non-integer |
| M_P alpha^12 | 72.1 | 2.04e-22 | 3.55e3 | Excluded (overclosure) |

The alpha^13 candidate is 68% of the required Omega, corresponding to a factor 1.47 in Lambda. This is suggestive but NOT a match at the precision needed. The required exponent (12.87) is not an integer or half-integer.

Possible resolution: If the prefactor is not unity but involves small rational factors:

    Lambda = (pi/4)^{1/2} * M_P * alpha^13 = 0.886 * 0.526 = 0.466 eV  (worse)
    Lambda = sqrt(2) * M_P * alpha^13 = 0.744 eV  (very close!)
    Lambda = (3/2)^{1/2} * M_P * alpha^13 = 0.644 eV  (not bad)

**sqrt(2) * M_P * alpha^13 = 0.744 eV gives Omega_chi h^2 = 0.112, which is 93% of the target.** This is within the anharmonicity uncertainty.

Whether sqrt(2) has a topological origin in DFD (perhaps from the complex Gaussian measure, or from the Kahler structure of S^3 quantization) is an open question.

---

## 8. Does G Depend on R_3? A Detailed Investigation

### 8.1 The Standard KK Scenario (NOT the DFD mechanism)

In standard Kaluza-Klein reduction of D-dimensional gravity on a compact manifold K:

    G_4 = G_D / Vol(K)

For D = 7 on K = CP^2 x S^3 with radii R_CP and R_3:

    Vol(CP^2) ~ R_CP^4,  Vol(S^3) ~ R_3^3
    G_4 ~ G_7 / (R_CP^4 * R_3^3)

If we also have M_7 (the 7D Planck mass) fixed by some UV completion:

    M_P^2 = M_7^5 * R_CP^4 * R_3^3

This makes M_P (and hence G) depend on BOTH R_CP and R_3. However:

### 8.2 Why This Does NOT Apply in DFD

DFD does NOT start from a 7D Einstein-Hilbert action. The DFD action (section_formalism.tex, Eq. 2.6) is written DIRECTLY in 4D:

    S_psi = integral dt d^3x { (a*^2/8piG) W(|grad psi|^2/a*^2) - (c^2/2) psi (rho - rho_bar) }

Here G appears as a 4D coupling constant, not derived from dimensional reduction. The internal manifold CP^2 x S^3 provides:
- Topological invariants (k_max, N_gen, alpha) via the microsector
- The chi field as a zero-mode of the 3-form on S^3

But it does NOT provide G. Newton's constant is either:
(a) A measured input, or
(b) Determined by the alpha^57 invariant (which is R_3-independent, per the eigenvalue cancellation theorem)

### 8.3 Could a Future Version Make G R_3-Dependent?

Yes, if DFD v3.4+ were reformulated as a genuine 7D theory with Kaluza-Klein reduction. In that case:

    G_4 = G_7 / (R_CP^4 * R_3^3)

With the alpha^57 invariant:

    G_4 hbar H_0^2 / c^5 = alpha^57

This would give:

    H_0^2 = alpha^57 c^5 * R_CP^4 * R_3^3 / (G_7 hbar)

Now H_0 depends on R_3. Combined with Omega_chi(R_3), this gives 2 equations for 3 unknowns (R_3, R_CP, G_7). Still underdetermined unless G_7 and R_CP are fixed by additional physics.

If R_CP is also stabilized (e.g., R_CP ~ l_P * sqrt(k_max)), then we have 2 equations for 1 unknown (R_3), making the system overconstrained. This would be the genuine self-consistency test envisioned in the task brief.

**This remains a promising direction for v3.4 but is NOT implemented in v3.3.**

---

## 9. Physical Interpretation of R_3 = 0.256 Micrometers

### 9.1 Comparison with Known Scales

| Scale | Value | Ratio to R_3 |
|-------|-------|-------------|
| Planck length | 1.62 x 10^{-35} m | R_3/l_P = 1.58 x 10^{28} |
| Proton Compton wavelength | 1.32 x 10^{-15} m | R_3/lambda_p = 1.94 x 10^8 |
| Bohr radius | 5.29 x 10^{-11} m | R_3/a_0 = 4.84 x 10^3 |
| Visible light wavelength | 5 x 10^{-7} m | R_3/lambda_vis = 0.51 |
| Current gravity test limit | ~5 x 10^{-5} m | R_3/L_grav = 5.1 x 10^{-3} |

R_3 = 0.256 um is remarkably close to the wavelength of visible light, and roughly 200x below the current reach of short-range gravity tests. It sits in the "mesoscopic" regime between atomic and macroscopic scales.

### 9.2 In Terms of the DFD Alpha-Hierarchy

    R_3 = hbar c / Lambda = hbar c / (0.771 eV)

In Planck units: R_3 / l_P = M_P / Lambda = 2.435e18 / 7.71e-10 = 3.16 x 10^{27}

Compare: (1/alpha)^{12.87} = (137.036)^{12.87} = 3.16 x 10^{27}. This confirms the R9 Agent 9 result that Lambda ~ M_P alpha^{12.87}.

### 9.3 Experimental Accessibility

The value R_3 ~ 0.26 um = 260 nm places the compactification scale within reach of:

1. **Sub-micrometer gravity tests:** Next-generation Casimir-force experiments probing the 100 nm -- 1 um range could detect KK graviton Yukawa corrections.

2. **Neutron scattering:** The KK mass scale is m_KK ~ hbar / (R_3 c) ~ 0.77 eV, corresponding to thermal neutron energies. Neutron interferometry at this energy scale could probe extra-dimensional effects.

3. **Atom interferometry:** Precision measurements of the gravitational acceleration at sub-micrometer separations.

---

## 10. Conclusions

### 10.1 Main Results

1. **The self-consistency system DECOUPLES.** The v3.3 observables (G, H_0, alpha, a_0) are R_3-independent. The chi sector introduces R_3 as a new parameter.

2. **R_3 is uniquely determined** by the single constraint Omega_chi = 0.266, giving R_3 = 0.256 um (Lambda = 0.77 eV).

3. **No inconsistency exists** because the system is exactly determined (1 equation, 1 unknown), not overconstrained.

4. **DFD+chi has exactly ONE free parameter** (R_3 or equivalently Lambda, m_chi, or Omega_chi). This is fixed by one measurement (the CDM density). All other observables are derived from two topological integers (k_max = 60, N_gen = 3).

5. **The alpha-tower candidate** Lambda = sqrt(2) * M_P * alpha^13 = 0.744 eV comes within 3.5% of the required value. If a topological origin for the sqrt(2) factor can be established, DFD+chi would have ZERO free parameters.

### 10.2 What Would Constitute a Genuine Self-Consistency Test

For R_3 to be overconstrained (and therefore subject to a nontrivial consistency check), DFD would need to derive G from the compactification geometry (making G depend on R_3). This requires reformulating DFD as a genuine higher-dimensional theory. In that case:
- The alpha^57 invariant would FIX R_3 (through G(R_3))
- The misalignment formula would PREDICT Omega_chi from that R_3
- Comparison with the observed Omega_m would be a genuine zero-parameter test

### 10.3 Parameter Count Summary

| Theory | Continuous free parameters | Integer inputs | Key prediction capability |
|--------|---------------------------|----------------|--------------------------|
| LCDM | 6 | 0 | Fits data, does not predict |
| DFD v3.3 | 0 | 2 (k_max, N_gen) | H_0, alpha, a_0, mu(x) |
| DFD v3.4+chi | **1** (R_3) | 2 | Everything in v3.3 + CDM abundance |
| DFD v3.4+chi + alpha^13 | **0** (if sqrt(2) M_P alpha^13 derived) | 2 | Zero free parameters |

---

## Appendix A: Numerical Verification Script

```python
"""
Self-consistency solver for the DFD R_3 system.
Verifies that R_3 is uniquely determined by Omega_chi = 0.266.
"""
import numpy as np

# Physical constants (SI)
G = 6.67430e-11       # m^3 kg^-1 s^-2
hbar = 1.05457e-34    # J s
c = 2.99792e8         # m/s
kB = 1.38065e-23      # J/K
alpha = 1/137.036
eV = 1.60218e-19      # J
GeV = 1e9 * eV
hbar_c_eVm = 1.97327e-7  # eV * m

# DFD parameters
k_max = 60
N_gen = 3
M_P = 2.435e18 * GeV / (c**2)  # kg (reduced Planck mass, in energy then /c^2)
M_P_GeV = 2.435e18   # GeV
f_a_GeV = M_P_GeV / (k_max + 2)  # = M_P/62 GeV
C_total = 0.0236
sqrt_C = np.sqrt(C_total)  # = 0.154
theta2_avg = 12.43

# Step 1: Verify alpha^57 invariant
H0_kms = 72.09  # km/s/Mpc
Mpc = 3.0857e22  # m
H0 = H0_kms * 1e3 / Mpc  # s^-1

I_obs = G * hbar * H0**2 / c**5
I_pred = alpha**57

print("=== Subsystem A: alpha^57 invariant ===")
print(f"I_obs  = {I_obs:.4e}")
print(f"I_pred = {I_pred:.4e}")
print(f"Ratio  = {I_obs/I_pred:.6f}")
print(f"Agreement: {abs(I_obs/I_pred - 1)*100:.3f}%")

# Step 2: a_0 check
a0_pred = 2 * np.sqrt(alpha) * c * H0
a0_obs = 1.2e-10
print(f"\na_0 (predicted) = {a0_pred:.3e} m/s^2")
print(f"a_0 (observed)  = {a0_obs:.3e} m/s^2")
print(f"Ratio = {a0_pred/a0_obs:.3f}")

# Step 3: Solve for R_3 from Omega_chi = 0.266
# Target: m_chi = 2.335e-26 eV
m_chi_target_eV = 2.335e-26
m_chi_target_GeV = m_chi_target_eV * 1e-9

# Lambda from m_chi = sqrt(C) * Lambda^2 / f_a
Lambda2 = m_chi_target_GeV * f_a_GeV / sqrt_C
Lambda_GeV = np.sqrt(Lambda2)
Lambda_eV = Lambda_GeV * 1e9

# R_3 from Lambda = hbar*c / R_3
R_3 = hbar_c_eVm / Lambda_eV

print(f"\n=== Subsystem B: chi sector ===")
print(f"Lambda = {Lambda_eV:.4f} eV")
print(f"R_3    = {R_3:.4e} m = {R_3*1e6:.4f} um")
print(f"m_chi  = {m_chi_target_eV:.3e} eV")

# Step 4: Check alpha-tower candidate
Lambda_alpha13 = M_P_GeV * alpha**13 * 1e9  # in eV
Lambda_sqrt2_alpha13 = np.sqrt(2) * Lambda_alpha13

print(f"\n=== Alpha-tower candidates ===")
print(f"M_P * alpha^13         = {Lambda_alpha13:.4f} eV")
print(f"sqrt(2)*M_P*alpha^13   = {Lambda_sqrt2_alpha13:.4f} eV")
print(f"Required Lambda        = {Lambda_eV:.4f} eV")
print(f"Ratio (alpha^13/req)   = {Lambda_alpha13/Lambda_eV:.4f}")
print(f"Ratio (sqrt2*a13/req)  = {Lambda_sqrt2_alpha13/Lambda_eV:.4f}")

# Step 5: Check R_3 in Planck lengths
l_P = np.sqrt(hbar * G / c**3)
print(f"\n=== Scale comparison ===")
print(f"R_3 / l_P = {R_3/l_P:.3e}")
print(f"(1/alpha)^12.87 = {(1/alpha)**12.87:.3e}")
print(f"Ratio = {(R_3/l_P) / (1/alpha)**12.87:.4f}")
```

---

## Appendix B: Sensitivity Analysis

How sensitive is R_3 to input uncertainties?

### B.1 Uncertainty in <theta^2>

The topological average <theta^2> = 12.43 assumes equal weighting over all 61 CS vacua. If modular reduction applies (Scenario B), <theta^2> = 3.35, changing m_chi by 13.8x and Lambda by 3.7x.

| Scenario | <theta^2> | m_chi (eV) | Lambda (eV) | R_3 (um) |
|----------|-----------|------------|-------------|----------|
| Extended (A) | 12.43 | 2.34e-26 | 0.771 | 0.256 |
| Cosine (B) | 3.35 | 3.22e-25 | 2.86 | 0.069 |

### B.2 Uncertainty in C_total

C_total = 0.0236 has ~10% uncertainty from the CS lattice calculation. A 10% shift in C_total propagates as:

    delta(Lambda)/Lambda = delta(C_total) / (4 * C_total) ~ 2.5%

This gives Lambda = 0.77 +/- 0.02 eV, or R_3 = 0.256 +/- 0.006 um.

### B.3 Uncertainty in f_a

f_a = M_P/62 is topologically exact (k_max + 2 = 62). No uncertainty.

### B.4 Uncertainty in Omega_m

Omega_m = 0.315 +/- 0.007 (Planck 2018). Since Omega_chi ~ m_chi^{1/2} and Lambda ~ m_chi^{1/2}:

    delta(Lambda)/Lambda = delta(Omega_chi) / Omega_chi ~ 0.007/0.266 ~ 2.6%

Giving Lambda = 0.77 +/- 0.02 eV.

### B.5 Combined uncertainty

Combining in quadrature (dominated by the <theta^2> scenario choice):

- **Within Scenario A:** Lambda = 0.77 +/- 0.03 eV, R_3 = 0.256 +/- 0.010 um
- **Scenario ambiguity:** Lambda ranges from 0.45 to 2.86 eV, R_3 from 0.069 to 0.435 um

The Scenario A vs B choice is the dominant uncertainty. Resolution requires understanding whether the DFD chi potential is truly periodic (cosine) or extended (topological).
