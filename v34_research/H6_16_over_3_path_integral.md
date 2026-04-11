# H6: Path Integral Analysis of Ω_χ/Ω_b = 16/3

**Agent:** H6
**Issue:** DFD #6 — Is 16/3 a path integral result or just DOF counting?
**Date:** 2026-04-06
**Verdict:** **The 16/3 claim is DOF counting, not a path integral result. The gap between counting and the required energy density ratio is not closed by any rigorous derivation.**

---

## 1. The DFD Path Integral

Formally, on M_11 = M_4 × CP² × Sph³ with strict product geometry,

    Z_DFD = ∫ D[g] D[ψ_SM] D[χ] D[Φ_int] exp(i S_DFD[g, ψ, χ, Φ])

with

    S_DFD = S_spectral + S_matter + S_DFD-mod
          = (1/g²) Tr f(D/Λ) + ∫ ψ̄ D ψ + ...

where D is the Dirac operator on the product, and f is a cutoff function (Connes spectral action).

On a strict product geometry the Dirac operator decomposes:

    D = D_4 ⊗ 1 + γ_5 ⊗ D_int

with D_int acting on sections of the spinor bundle over CP² × Sph³. The heat kernel factorizes:

    Tr exp(-t D²) = Tr_4 exp(-t D_4²) · Tr_int exp(-t D_int²)

This factorization is the mathematical content behind the claim that the partition function splits as

    Z_int = Z_CP² · Z_Sph³

and that species counting becomes a multiplicative factor in front of the 4D effective action.

## 2. What Species Counting Actually Gives

The internal zero-mode space of D_int on CP² × Sph³ (with the appropriate twisting consistent with SO(10) embedding) has dimension equal to the complex spinor of Spin(10):

    dim(16_C) = 16  (one SM generation + ν_R per 16)

Multiplicity from three generations gives a total fermionic zero-mode space of dimension 48. The "16 vs 3" partition in the DFD claim is:

- **16**: Weyl species per generation that carry χ charge (all SM fermions plus ν_R)
- **3**: generations of SM baryons counted as distinct contributions to the sphaleron-processed baryon sector

The spectral trace gives:

    Tr_χ(1) / Tr_b(1) = 16/3

as a pure **dimension counting** of orthogonal subspaces of the zero-mode eigenspace. This is an identity about the *kernel of D_int*, not about energy densities.

## 3. Where the Path Integral Does and Does Not Constrain Ω_χ/Ω_b

### What the path integral does give

After integrating out nonzero internal modes (the α^57 Appendix-O structure), the 4D effective action contains a kinetic term for each zero-mode species with a **common normalization** fixed by the internal volume:

    S_eff ⊃ Σ_I (Z_I / 2) ∫ d⁴x (∂ φ_I)² + ...

with Z_I = Vol(CP² × Sph³) × (internal wavefunction norm)_I. For species in the same SO(10) rep, Z_I is **universal**: this is what "geometric factor is the same for both sectors" means in Step 3 of the task prompt. This much is a genuine path integral output.

### What the path integral does not give

The ratio Ω_χ/Ω_b is a ratio of **energy densities today**:

    Ω_χ/Ω_b = (m_χ n_χ) / (m_b n_b)

Neither m_χ, n_χ, m_b, nor n_b is determined by Tr_int(1). The path integral on a strict product geometry is **time-translation invariant and Lorentz invariant**; it does not know about reheating, cosmological evolution, or non-equilibrium number densities. Species counting controls degeneracy factors inside equilibrium distributions, but the mapping

    degeneracy counting ⟼ relic energy density

requires a dynamical production history that the spectral action does not supply.

Formally, the identity

    ∫ D[χ] χ² exp(-S) / ∫ D[b] b² exp(-S) = 16/3

holds *only* for Gaussian two-point functions in the symmetric vacuum with universal propagator normalization. At finite temperature in a cosmological background this ratio is modified by (i) distinct chemical potentials, (ii) distinct decoupling times, (iii) distinct masses in the Boltzmann suppression factors, and (iv) any non-thermal production channel.

**Conclusion of Section 3:** 16/3 is the ratio of *degeneracies*, not the ratio of *relic energy densities*. The path integral does not bridge these without extra dynamical input.

## 4. Checking the Two Candidate Dynamical Mechanisms

### 4a. Gravitational freeze-in at T_RH ~ 10^12 GeV

Thermal scattering SM+SM → χχ through graviton exchange gives a rate per particle

    Γ ~ T⁵ / M_P⁴

The yield accumulated over a Hubble time at T = T_RH is

    Y_χ ≡ n_χ/s ~ (Γ / H) |_{T_RH} ~ (T_RH / M_P)³ × (species factor)

With T_RH = 10^12 GeV and M_P = 2.4 × 10^18 GeV,

    (T_RH / M_P)³ ≈ (4.2 × 10⁻⁷)³ ≈ 7.3 × 10⁻²⁰

Even multiplying by g_* ~ 100 and an O(1) SO(10) species factor, the resulting Ω_χ h² is ~10^(-18) to 10^(-20) of the required abundance. **Gravitational freeze-in underproduces χ by roughly 20 orders of magnitude.** This mechanism cannot deliver Ω_χ/Ω_b = 16/3.

### 4b. Thermal equilibrium abundance at T_RH

If χ is in full thermal equilibrium at T_RH with g_χ relativistic degrees of freedom, then

    n_χ(T_RH) / n_b(T_RH) = g_χ / g_b

Using the claimed g_χ = 16, g_b = 3:

    Ω_χ / Ω_b = (m_χ g_χ) / (m_b g_b) = (96 keV × 16) / (≈ 938 MeV × 3)
              ≈ (1.54 × 10⁻³ MeV) / (2.81 × 10³ MeV)
              ≈ 5.5 × 10⁻⁴

This is **roughly 10⁴ times too small** (target: 5.33), not a factor of 10. The thermal equilibrium calculation is off by orders of magnitude in the wrong direction.

Moreover the "m_b ≈ 1 GeV" bookkeeping is itself incorrect for energy density: the baryon energy density today is m_N × n_b ≈ 938 MeV × n_b, while baryon number is conserved from a tiny asymmetry η_B ≈ 6 × 10⁻¹⁰. So the correct comparison at T_RH is not n_χ/n_b = 16/3 but rather n_χ/(η_B n_γ) = 16/(3 η_B) ~ 10^10, and the χ sector would dominate catastrophically unless m_χ is extraordinarily small — contradicting the 96 keV value.

## 5. Resolving the Tension

The task prompt's Step 6 offers three options. The correct answer is **(b) combined with (c)**:

**(b) The 16/3 DOF counting is not the correct mapping to Ω_χ/Ω_b.** Degeneracy counting controls multiplicities in equilibrium distributions but not relic energy densities after decoupling, symmetry breaking, and (for baryons) sphaleron reprocessing into a tiny asymmetry η_B.

**(c) The production mechanism cannot be thermal equilibrium.** Thermal equilibrium gives n_χ ~ T³ at decoupling, not n_b,asymmetry ~ η_B T³. The two sectors populate via fundamentally different physics:

- Baryons: leptogenesis → sphaleron → η_B ~ 10⁻¹⁰ asymmetry → m_N n_b today
- χ: an unspecified production mechanism that must give the observed Ω_χ h² ≈ 0.12

There is no known mechanism that links these two numbers by a factor of 16/3. Any model that derives Ω_χ/Ω_b = 16/3 must include:

1. a dynamical calculation of the baryon asymmetry η_B (not just a species count of 3),
2. a dynamical calculation of the χ abundance (freeze-in, freeze-out, misalignment, gravitational, condensate, ...),
3. a symmetry or conservation law linking (1) and (2) quantitatively, not just by degeneracy counting.

The current DFD manuscript supplies none of (1)–(3) with the rigor a path integral derivation requires. The Appendix-O α^57 factorization constrains the common 4D normalization but is silent on the cosmological history that actually sets the ratio.

## 6. What a Rigorous Derivation Would Look Like

A genuine path integral derivation of Ω_χ/Ω_b = 16/3 would need:

1. **Master spectral action** on the product geometry producing a unique 4D effective action with explicit χ and baryon sectors.
2. **Finite-temperature extension**: the Euclidean path integral on S¹_β × M_3 × CP² × Sph³, computing Z(β) and deriving equilibrium distributions for both sectors.
3. **Out-of-equilibrium extension**: a Schwinger-Keldysh or Boltzmann hierarchy that tracks both sectors through reheating, EW symmetry breaking, and QCD confinement.
4. **A conserved current** (e.g. a discrete Z_16/Z_3 or a U(1)_int) that equates (n_χ/g_χ) to (n_b/g_b) throughout cosmological evolution, making degeneracy counting survive as an energy-density ratio.
5. **Mass relation** m_χ × g_χ / (m_b × g_b) = 16/3 as a derived consequence, not an input tuned to match 96 keV.

None of these ingredients is present in the current manuscript.

## 7. Verdict

- **Is 16/3 a path integral result?** No. It is the dimension of a fermionic zero-mode space on the internal manifold, partitioned into χ and baryon subspaces by species assignment.
- **Does the spectral-trace factorization on M_11 force Ω_χ/Ω_b = 16/3?** No. It forces the common 4D kinetic normalization, not the relic energy density ratio.
- **Does any of the proposed cosmological mechanisms (gravitational freeze-in, thermal equilibrium, misalignment) reproduce 16/3?** No. Gravitational freeze-in underproduces by ~20 orders of magnitude; thermal equilibrium at T_RH gives ~5 × 10⁻⁴, not 5.33; no misalignment derivation is provided.
- **Where is the gap?** Between Step 3 (DOF counting) and Step 5 (cosmological production). The manuscript treats degeneracy counting as if it were an energy density prediction, which is a category error unless a protected conservation law is supplied.

**Bottom line for the #6 issue:** the claim Ω_χ/Ω_b = 16/3 is, as stated in the issue title, DOF counting dressed in path integral language. The factorization of Z on the product geometry is a real and correct statement about internal-sector traces; it is not a statement about relic abundances. Closing the gap requires a conservation law linking χ number density to baryon number density across the full cosmological history, and that law is currently missing.

---

*Filed by H6 as part of the v3.4 numerical-results triage campaign.*
