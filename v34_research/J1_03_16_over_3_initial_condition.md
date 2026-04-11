# J1-3: Reframing 16/3 as a Constraint on Initial Conditions

**Agent:** J1-3
**Target:** Ω_χ/Ω_b = 16/3
**Strategy:** Abandon the "derivation" framing. Treat 16/3 as an initial-condition / consistency constraint rather than a dynamical output, and determine honestly what survives.

---

## 1. Framing

J1-1 and J1-2 attacked 16/3 as a claim to be *derived* from spectral traces on CP²×S³. Both exposed a gap: the topological counts Tr_χ(1) = 16 and Tr_b(1) = 3 are zero-mode multiplicities, not energy densities, and no dynamical argument converts a trace ratio into Ω_χ/Ω_b at z = 0.

This agent takes a different route. In GR, FLRW initial data (ρ_tot, H, k) are not *derived*; they are *chosen* consistently with the constraint equations. The analogous question for DFD is:

> What initial conditions at the spectral cutoff Λ_UV are consistent with the CP²×S³ structure, and what does this imply — if anything — for Ω_χ/Ω_b today?

## 2. DFD initial data at Λ_UV

At the spectral cutoff, a DFD cosmological background requires:

1. Background metric (flat Minkowski by DFD's construction).
2. Background ψ field: ψ̄(t_UV).
3. Background χ field: χ̄(t_UV).
4. Fermion/boson occupation densities at Λ_UV.

The only constraint from the spectral action principle δS_DFD/δg = 0 at Λ_UV is that the total stress-energy source the (flat) background self-consistently. This constrains the *total* ρ, not the *split* between χ and baryonic sectors.

## 3. The trace identities are counting statements

Tr_χ(1) = 16 per generation (SO(10) spinor multiplicity) and Tr_b(1) = 3 per generation (CP² color cohomology) are exact topological facts. But they count *zero modes of the Dirac operator*, not energy densities:

- Energy density = (number density) × (mean energy per mode) × (occupation).
- Only the first factor is set by the trace.
- Occupation and mean energy per mode are set by thermal history and by whatever produced each sector.

So the trace identity constrains the *number ratio* at the level of available modes, not the *energy ratio*.

## 4. The "constraint" version of the claim

The strongest form of the claim that survives is:

**Claim (weak form).** *If the χ and baryon sectors are populated with equal per-mode occupation at some reference scale T_ref where both are non-relativistic with the same characteristic energy per mode, then ρ_χ/ρ_b = 16/3 at T_ref.*

This is a constraint on initial conditions, not a derivation. It says: *if* populations are equalised at T_ref in this specific sense, *then* the topological counts fix the ratio.

## 5. Can relaxation establish this constraint dynamically?

For the weak claim to become a prediction, some mechanism must drive the occupation toward "equal per-mode" at T_ref. Candidate mechanisms:

- **Gravitational scattering between sectors.** Rate ~ G² n T⁵. At T ~ 1 GeV this gives τ ~ (M_P² / T³) ~ 10³⁸ GeV⁻¹ ~ 10¹⁴ s, vastly longer than H⁻¹(1 GeV) ~ 10⁻⁴ s. Ruled out.
- **Quantum tunneling between sectors.** Requires a common operator coupling χ and baryons; DFD does not furnish one above the χ mass threshold in any published form.
- **Non-perturbative effects at Λ_UV.** Would be instanton-suppressed, no reason to land on equal occupation.

No known DFD mechanism relaxes the χ/baryon occupation to equality on sub-Hubble timescales at any relevant epoch. **The constraint cannot be dynamically established; it must be imposed.**

## 6. What preservation requires

Suppose the weak claim is imposed at some T_ref and asks for ρ_χ/ρ_b = 16/3 *today*. Work backwards:

- For T < m_χ ≈ 96 keV: χ is non-relativistic, dilutes as a⁻³.
- For T < Λ_QCD ≈ 1 GeV: baryons (protons, neutrons) are non-relativistic, dilute as a⁻³.
- So between T ≈ 1 GeV and T = T_now, both sectors scale identically and any ratio imposed at T ≈ 1 GeV survives to today.

Between T = m_χ and T = 1 GeV, χ is non-relativistic but the "baryon" degrees of freedom are still the quark-gluon plasma, relativistic, with ρ ∝ a⁻⁴. The quark-gluon energy density is not the baryon energy density; baryon *number* is conserved but baryon *energy* does not exist as a separate fluid until confinement.

So the natural reference point is T_ref = Λ_QCD. The claim becomes:

**Claim (reference form).** *ρ_χ / ρ_b = 16/3 at T = Λ_QCD, and the ratio is preserved to today because both components are cold dust below confinement.*

## 7. What sets the ratio at Λ_QCD?

At T = Λ_QCD:

- ρ_b is set by the baryogenesis asymmetry η_B ≈ 6 × 10⁻¹⁰ (independently measured from BBN and CMB) times m_N times the photon number density.
- ρ_χ is set by the χ relic abundance, which depends on the production mechanism (thermal freeze-out, misalignment, freeze-in, ...). DFD has not uniquely fixed this.

For the ratio to equal 16/3 at Λ_QCD, baryogenesis and χ production — two logically independent processes — must conspire to land on exactly this number. Nothing in the published DFD framework forces this conspiracy. The 16/3 is not a prediction; it is a tuning requirement on the joint (η_B, χ-production) history.

## 8. Going back to T_UV

Between T = 1 GeV and T = Λ_UV (≈ M_Pl), the χ sector is non-relativistic for T < m_χ and relativistic for T > m_χ, while "baryons" do not exist as a separate fluid — there is only the hot quark-gluon-electroweak plasma carrying baryon number.

Tracking ρ_χ/ρ_b(T_UV) is not actually a well-defined question: the denominator has no definition above confinement. What one *can* track is the χ-to-entropy ratio Y_χ = n_χ/s and the baryon-to-entropy ratio Y_B = n_B/s. These are both asymptotic invariants once χ and baryon number are frozen.

The honest statement is:

Y_χ / Y_B = (Ω_χ / Ω_b) × (m_N / m_χ) = 5.36 × (938 MeV / 96 keV) ≈ 5.24 × 10⁴.

This number, 5 × 10⁴, has no connection to 16/3. It is the number DFD would actually need to explain from first principles if it wanted to predict the dark-matter–baryon ratio. The topological 16/3 does not help with it.

## 9. The relaxation timescale check (Step 3 of the task)

For completeness, evaluate τ_relax vs. 1/H at T_UV = M_Pl. The fastest plausible cross-sector process is gravitational scattering:

σ_grav ~ G² s ~ s / M_Pl⁴, n ~ T³, v ~ 1
⇒ Γ ~ n σ v ~ T⁵ / M_Pl⁴
H(T_UV) ~ T² / M_Pl

Γ / H ~ T³ / M_Pl³. At T = M_Pl this is O(1); below M_Pl it is < 1 immediately. Gravitational relaxation is marginal exactly at the cutoff and ineffective everywhere below. **τ_relax >> H⁻¹ throughout the post-Planckian history.** The 16/3 ratio cannot be dynamically relaxed into; it must be chosen.

## 10. The honest reframe

Given all of the above, the defensible statement for the paper is:

> "DFD identifies 16/3 as the ratio of zero-mode counts between the χ sector (16 fermion species per generation from the SO(10) spinor structure) and the baryon sector (3 colors per generation from CP² cohomology). The observed value Ω_c / Ω_b = 5.36 ± 0.07 agrees with this topological invariant at the 0.25σ level. Converting this mode-count ratio into an energy-density ratio requires assumptions about sector occupation and cosmic thermal history that DFD does not currently fix. Whether the agreement reflects a deep dynamical mechanism linking baryogenesis and χ production to the topological mode counts, or is a numerical coincidence, is an open question."

This:

- Preserves the striking numerical match (0.25σ is striking and should be reported).
- Does not claim a derivation that does not exist.
- States explicitly what would need to be shown (a link from mode counts to Y_χ/Y_B).
- Lets the reader judge "coincidence vs. clue" without being oversold.

## 11. Findings summary

1. **16/3 cannot be derived dynamically.** No DFD mechanism relaxes the χ/baryon energy ratio to the trace-count ratio on sub-Hubble timescales at any epoch. Gravitational scattering fails by 40+ orders of magnitude at T ~ 1 GeV and is only marginal even at the Planck scale.
2. **16/3 cannot be cleanly imposed as a T_UV initial condition either**, because "ρ_b" is not defined above confinement. The only well-defined invariants are Y_χ and Y_B, and their ratio is ~5 × 10⁴, not 16/3.
3. **The weak form that survives** is a reference-epoch statement at T = Λ_QCD: if ρ_χ/ρ_b = 16/3 at confinement, it survives to today. But this requires baryogenesis (η_B) and χ production to conspire; DFD does not force the conspiracy.
4. **The honest reframe** replaces "derivation" with "observed coincidence with a topological invariant, mechanism open." This is intellectually defensible and removes the overclaim without discarding the numerical match.

## 12. Recommendation

Replace all language in the DFD v3.4 draft that says "16/3 is derived from spectral-trace factorization" with the Section 10 reframe. Add an explicit open-problem box: *"Derive Y_χ/Y_B ≈ 5 × 10⁴ from a DFD joint model of baryogenesis and χ production such that ρ_χ/ρ_b = 16/3 at Λ_QCD."* That is the real target, and it is an honest open problem rather than a solved one.
