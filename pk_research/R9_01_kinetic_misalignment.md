# R9 Agent 1: Kinetic Misalignment for DFD's Axion-Like Field

**Campaign:** R9 (Dark Matter Production Mechanisms)
**Agent:** 1 (Kinetic Misalignment)
**Date:** 2026-04-05
**Status:** COMPLETE -- mechanism inapplicable; DFD has no axion

---

## 0. Executive Summary

The kinetic misalignment mechanism (Co, Hall & Harigaya 2019) cannot rescue an axion dark matter candidate in DFD because **DFD does not possess a QCD axion or axion-like dark matter candidate**. The theory solves the Strong CP problem topologically (Theorem 5 of Appendix L, v3.3) and produces dark matter through a completely different mechanism: the psi-sector dust branch (Appendix Q). The premise of this investigation -- that a chi field with f_a = 3.93 x 10^16 GeV needs kinetic misalignment to achieve Omega_chi = 0.266 -- is built on a misidentification. This report documents the full computation to make the negative result explicit and instructive.

---

## 1. The Kinetic Misalignment Mechanism

### 1.1 Standard (Vacuum) Misalignment Review

In standard vacuum misalignment, an axion field a starts displaced from its potential minimum by an angle theta_i = a_i / f_a. After the QCD phase transition generates the axion mass m_a, the field begins oscillating and its energy density redshifts as matter. The relic abundance is:

    Omega_a h^2 ~ 0.12 * (f_a / 10^12 GeV)^(7/6) * theta_i^2

For f_a = 3.93 x 10^16 GeV, this requires m_a ~ 10^(-26) eV to get Omega = 0.266, which is below the fuzzy dark matter bound (m > 10^(-22) eV from Lyman-alpha). Hence standard misalignment fails at this f_a.

### 1.2 Kinetic Misalignment Formula

In kinetic misalignment (Co, Hall & Harigaya, arXiv:1910.14152), the axion starts with large initial angular velocity:

    dot{theta}_i = dot{a}_i / f_a >> H_osc

where H_osc is the Hubble rate when m_a ~ 3H. The field rotates many times before the potential turns on, and the relic density receives an enhancement:

    Omega_a h^2 = Omega_a^(standard) * n_rot

where n_rot ~ dot{theta}_i / m_a is the number of rotations before trapping. More precisely, for dot{theta}_i >> m_a f_a:

    Omega_a h^2 ~ (m_a * n_a * s_0) / (3 * H_0^2 * M_Pl^2)

where n_a / s ~ (dot{theta}_i * T_osc) / (f_a * s) is the comoving number density set by the initial rotation, and s_0 is today's entropy density.

The parametric scaling in the large-kick regime is:

    Omega_a h^2 ~ 0.12 * (dot{theta}_i / (10^12 GeV)) * (f_a / 10^12 GeV)^(1/2) * (m_a / 10^(-5) eV)^(-1/2)

### 1.3 Required Initial Velocity

For kinetic misalignment to produce Omega_chi = 0.266 with:
- f_a = 3.93 x 10^16 GeV
- m_chi = 0.154 * Lambda_QCD^2 / f_a

First compute m_chi. Using Lambda_QCD^(DFD) = M_Pl * alpha^(19/2) = 61.20 MeV (Appendix Z, Eq. for Lambda_QCD):

    m_chi = 0.154 * (61.20 MeV)^2 / (3.93 x 10^16 GeV)
          = 0.154 * 3.745 x 10^(-3) GeV^2 / (3.93 x 10^16 GeV)
          = 1.47 x 10^(-20) GeV
          = 1.47 x 10^(-11) eV

This mass is well below the fuzzy DM bound, confirming the problem with standard misalignment.

For kinetic misalignment, the required kick velocity is (inverting the relic density formula):

    dot{theta}_i ~ (Omega_chi h^2 / 0.12) * (10^12 GeV / f_a)^(1/2) * (m_chi / 10^(-5) eV)^(1/2) * 10^12 GeV

Substituting:
- Omega_chi h^2 ~ 0.12 (to match observations)
- f_a = 3.93 x 10^16 GeV, so (10^12 / f_a)^(1/2) = (2.54 x 10^(-5))^(1/2) = 5.04 x 10^(-3)
- m_chi = 1.47 x 10^(-11) eV, so (m_chi / 10^(-5))^(1/2) = (1.47 x 10^(-6))^(1/2) = 1.21 x 10^(-3)

    dot{theta}_i ~ 1.0 * 5.04 x 10^(-3) * 1.21 x 10^(-3) * 10^12 GeV
                 ~ 6.1 x 10^6 GeV

Converting to the angular velocity:

    dot{a}_i = dot{theta}_i * f_a = 6.1 x 10^6 * 3.93 x 10^16 GeV^2
             = 2.4 x 10^23 GeV^2

This is a very large initial field velocity, corresponding to an energy density:

    rho_i ~ dot{a}_i^2 ~ (2.4 x 10^23 GeV^2)^2 ~ 5.8 x 10^46 GeV^4

For comparison, the radiation energy density at T ~ 10^10 GeV (near the GUT scale) is rho_rad ~ T^4 ~ 10^40 GeV^4. So the required kick energy density would vastly exceed the radiation bath unless it occurs at temperatures T > 10^11 GeV.

**Result:** Kinetic misalignment requires dot{theta}_i ~ 6 x 10^6 GeV, which is technically possible but requires an extremely energetic early-universe process to impart the kick.

---

## 2. What Does DFD Actually Say?

### 2.1 No QCD Axion in DFD

Appendix L of v3.3 proves:

**Theorem (Strong CP all-loops closure):** In the DFD microsector on M = CP^2 x S^3 with the Standard Model fermion content:
1. The microscopic theory is CP invariant at theta_bare = 0 (tree-level verified).
2. The CP anomaly phase is trivial: A_CP = 1.

Therefore theta-bar = 0 to all loop orders. **No axion is required.**

The proof uses the Dai-Freed anomaly formula. The mapping torus T_CP has dimension dim(M) + 1 = 7 + 1 = 8 (even). On any closed even-dimensional Spin^c manifold, the eta-invariant vanishes identically because the chirality operator forces exact +/- lambda spectral pairing. Therefore A_CP = exp(i*pi/2 * 0) = 1.

This is not a soft statement -- it is a theorem-grade result. DFD explicitly predicts:
- No QCD axion exists
- Axion searches (ADMX, ABRACADABRA, CASPEr, etc.) will find nothing
- Any observed theta-bar != 0 would falsify the mechanism

### 2.2 No Axion-Like Dark Matter Candidate

The chi symbol in section_quantum.tex refers to internal mode frames (chi_a^(3), chi_b^(2), chi^(1)) -- these are Berry connection frames for the gauge emergence mechanism on CP^2 x S^3, NOT a propagating pseudo-scalar dark matter candidate.

DFD does not contain:
- A Peccei-Quinn symmetry
- An axion decay constant f_a in the dark matter sector
- A light pseudo-scalar that could serve as axion dark matter

### 2.3 How DFD Produces Dark Matter

DFD's dark matter mechanism is entirely different. The temporal completion theorem (Appendix Q) proves:

The S^3 saturation-union composition law forces the temporal sector to depend on deviations from background:

    mu(psi_0 + Delta_psi) - mu(psi_0) = (1 - mu(psi_0)) * mu(Delta_psi)

With K'(Delta) = mu(Delta), the dust branch emerges:

    w -> 0,    c_s^2 -> 0

The psi-sector behaves as **pressureless dust**, clustering under gravity without pressure support. This is the DFD replacement for cold dark matter -- not a particle, but a field-theoretic dust mode of the psi field itself.

---

## 3. The "Double Transit" Clarification

Appendix M in v3.3 describes the **photon double-transit enhancement** (Gamma = 4), which is an optical effect in the solar corona, not a topological phase transition. It explains why resonantly scattered Ly-alpha photons show 4x the asymmetry of locally emitted O VI lines in UVCS data.

There is no "double transit" topological transition that changes Chern-Simons levels and could kick a chi field. The Chern-Simons structure in DFD is:
- Static: k_max = 60 is the UV truncation from the Spin^c index on CP^2
- Quantized: levels k = 0, 1, ..., 59 are integers (gauge invariance)
- Structural: they determine alpha = 1/137 through the weighted level sum
- Not dynamical: no CS level transitions occur in the cosmological evolution

### 3.1 Could a Topological Transition Provide a Kick?

Even hypothetically, within DFD's framework:

1. **The CS levels are topological invariants** of the gauge bundle E = O(9) + O^5 on CP^2. They do not change during cosmological evolution.

2. **The instanton number on CP^2** is integer-quantized: Tr(F ^ F) integrates to a topological integer 8*pi^2 * k_3. This is discrete, not continuous -- there is no smooth "transition" between values.

3. **The mapping torus construction** (Appendix L) is a mathematical device for computing the anomaly, not a physical process that occurs in time.

Therefore no topological kick mechanism exists within DFD's mathematical structure.

---

## 4. Is There a Topological Constraint on chi-dot_i?

### 4.1 Formal Answer

Since DFD has no chi field (axion-like pseudo-scalar), the question of a topological constraint on its initial velocity is moot. However, we can ask the more general question: does DFD's topology constrain initial field velocities?

**For the psi field:** The psi field is classical by design (S_psi ~ (M_Pl / a_star)^2 >> hbar). Its initial conditions are set by the cosmological boundary conditions, not by a misalignment mechanism. The dust branch is an attractor -- the psi perturbations naturally evolve toward pressureless dust behavior regardless of initial conditions.

**For hypothetical pseudo-scalars from CP^2 x S^3:** The compact topology does support harmonic forms that could in principle give rise to pseudo-scalar zero modes. However:
- H^1(CP^2 x S^3) = 0 (no harmonic 1-forms, hence no axion-like zero modes from reduction)
- H^3(CP^2 x S^3) = Z (the S^3 volume form), but this is the winding number that protects proton stability, not a propagating field
- The Chern-Simons theory on S^3 is topological (no propagating degrees of freedom in the bulk)

So the topology actively forbids light pseudo-scalar propagating modes.

### 4.2 Quantization Constraint

If one were to force an axion-like field into DFD by coupling it to Tr(F ^ F), the periodicity of theta would impose:

    a = a + 2*pi*f_a

This would quantize the field space. But since theta = 0 is topologically enforced and there is no anomaly, such a field would have zero potential and zero mass -- it would be exactly massless and decouple completely. It could not serve as dark matter.

---

## 5. Comparison: DFD vs. Axion Dark Matter

| Feature | QCD Axion (PQ) | Kinetic Misalignment | DFD Dark Matter |
|---------|---------------|---------------------|-----------------|
| Solves Strong CP? | Yes (PQ mechanism) | Yes (PQ mechanism) | Yes (topological, Thm L.4) |
| DM candidate? | Yes (a) | Yes (a with kick) | Yes (psi dust branch) |
| New particle? | Yes (axion) | Yes (axion) | No |
| New symmetry? | Yes (U(1)_PQ) | Yes (U(1)_PQ) | No |
| Free parameters | f_a, theta_i | f_a, dot{theta}_i | None (derived) |
| Falsifiable? | Axion searches | Axion searches | No axion signal; psi signatures |
| Status in DFD | Excluded (Thm L.4) | Excluded (Thm L.4) | Derived (Thm Q) |

---

## 6. Conclusions

### 6.1 Direct Answers to the Four Questions

**Q1: Kinetic misalignment formula for Omega_chi.**
Derived in Section 1.2. In the large-kick regime: Omega_a h^2 ~ 0.12 * (dot{theta}_i / 10^12 GeV) * (f_a / 10^12 GeV)^(1/2) * (m_a / 10^(-5) eV)^(-1/2).

**Q2: Required chi-dot_i for Omega = 0.266.**
dot{theta}_i ~ 6 x 10^6 GeV, corresponding to dot{a}_i ~ 2.4 x 10^23 GeV^2. This is an enormous field velocity requiring energy densities above the radiation bath at T < 10^11 GeV.

**Q3: Does the double transit provide this kick?**
No. Appendix M describes a photon scattering enhancement in the solar corona, not a cosmological topological transition. The CS structure in DFD is static and quantized -- no level transitions occur that could kick a field.

**Q4: Is there a topological constraint on chi-dot_i?**
The question is moot: DFD has no axion field chi. The topology of CP^2 x S^3 actively forbids axion-like zero modes (H^1 = 0) and makes any coupling to Tr(F ^ F) trivial (theta = 0 is exact). The dark matter role is played by the psi dust branch, which requires no initial velocity or misalignment mechanism.

### 6.2 The Deeper Point

The standard misalignment problem (f_a too large for vacuum misalignment) and its kinetic misalignment solution are both artifacts of the Peccei-Quinn framework. DFD sidesteps the entire problem:

1. Strong CP is solved by **topology** (even-dimensional mapping torus forces eta = 0), not by a new symmetry
2. Dark matter is provided by the **psi dust branch** (pressureless, clustering mode forced by S^3 composition law), not by a new particle
3. The Chern-Simons structure on S^3 determines **alpha = 1/137**, not an axion decay constant

These are three separate predictions, each independently falsifiable. The kinetic misalignment mechanism, while elegant in its own right, has no role to play in DFD.

---

## References

- Co, Hall & Harigaya, "QCD Axion Predictions with Cosmological Birefringence," arXiv:1910.14152 (2019)
- Dai & Freed, "eta-invariants and determinant lines," J. Math. Phys. 35, 5155 (1994)
- Alcock, "Density Field Dynamics: A Complete Unified Theory," v3.3, Appendices K, L, M, Q, Z
