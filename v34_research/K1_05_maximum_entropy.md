# K1-5: Maximum Entropy Derivation of Ω_χ/Ω_b = 16/3

**Agent:** K1-5
**Date:** 2026-04-06
**Task:** Derive Ω_χ/Ω_b = 16/3 from a Jaynesian maximum-entropy / equipartition argument.
**Verdict:** **FAILS.** Maximum entropy gives 16/3 only at the instant of high-T equipartition. The subsequent non-relativistic transitions of the baryons (at T ~ 1 GeV) and of χ (at T ~ 96 keV) shift the energy-density ratio by a factor of ~10^4, destroying the prediction.

---

## Step 1 — Setup: the constrained optimization

Sectors: baryons (g_b = 3, counting the three colors of a single Dirac quark flavor used as the baryonic DOF placeholder) and χ (g_χ = 16, from Tr_χ(1) on CP²×S³).

Constraint: Σ ρ_i = ρ_total (fixed by Friedmann).
Secondary constraints: conserved charges (B−L, χ-number) — these show up as Lagrange multipliers but drop out when the chemical potentials are small compared to T, which is the case at T ≫ m.

Entropy functional (Jaynes, over coarse-grained phase-space measure):
    S[{ρ_i}] = − Σ_i ρ_i log(ρ_i / g_i)

Lagrangian:
    L = − Σ_i ρ_i log(ρ_i/g_i) − λ(Σ_i ρ_i − ρ_total)

∂L/∂ρ_i = − log(ρ_i/g_i) − 1 − λ = 0
    ⇒ ρ_i / g_i = exp(−1−λ) = const
    ⇒ **ρ_χ / ρ_b = g_χ / g_b = 16/3.** ✓

So far so good: Jaynes delivers 16/3 as the prior.

## Step 2 — When is this physically realized?

The Jaynes result coincides with the true ensemble value only in the **high-T, relativistic, chemical-equilibrium limit**, where Boltzmann factors collapse to unity and ρ_i is determined purely by the DOF count:

    ρ_i^{rel} = (π²/30) g_i T^4   (bosons; ×7/8 for fermions).

In this regime the ratio ρ_χ/ρ_b is literally g_χ/g_b up to the fermion/boson (7/8) factors. If both sectors are fermionic the factors cancel: **ρ_χ/ρ_b = 16/3 exactly**, at any temperature T ≫ max(m_χ, m_b).

## Step 3 — Gravitational decoupling temperature

Cross section (gravitational 2→2, dimensional):
    σ_grav ~ G_N² s ~ s / M_P^4 ~ T² / M_P^4.

Number density (relativistic): n ~ T^3. Rate:
    Γ = n σ v ~ T^3 · T²/M_P^4 = T^5 / M_P^4.

Hubble (radiation era):
    H ~ T² / M_P.

Ratio:
    Γ/H ~ T^3 / M_P^3.

Decoupling (Γ = H) at **T_dec ~ M_P ~ 10^19 GeV**.

Interpretation: gravitational scattering is *never* in equilibrium below the Planck scale. The only way to have a 16/3 initial condition is to **postulate** it at T ~ M_P (e.g., as a post-reheating boundary condition, or from trans-Planckian equipartition), not to derive it from sub-Planckian gravitational kinetics.

This is a serious blow: we cannot *dynamically* enforce the 16/3 ratio at any accessible epoch. We have to assume it.

## Step 4 — Suppose we grant the 16/3 initial condition at T ≫ m_b, m_χ. Does it survive?

Assume ρ_χ/ρ_b = 16/3 is imposed at some T_0 with T_0 ≫ 1 GeV. Both sectors are relativistic, so:
    ρ_b = (7/8)(π²/30) g_b T^4,     ρ_χ = (7/8)(π²/30) g_χ T^4.

Each sector scales as T^4 ∝ a^{-4} while relativistic, so the ratio is preserved:
    ρ_χ/ρ_b = 16/3    for T_0 > T > ~1 GeV. ✓

Now the baryons go non-relativistic at T ~ m_b ~ 1 GeV. After that point:
    ρ_b = m_b n_b,     with n_b ∝ a^{−3}    ⇒    ρ_b ∝ a^{−3}.

Meanwhile χ is still relativistic (m_χ ≈ 96 keV ≪ 1 GeV), so:
    ρ_χ ∝ a^{−4}.

Between a(T=1 GeV) and a(T=96 keV), the scale factor grows by
    a_χ/a_b = T_b/T_χ = 10^9 eV / 10^{4.98} eV ≈ 10^{4.02} ≈ 1.05 × 10^4.

During this interval:
    ρ_b ∝ a^{−3},    ρ_χ ∝ a^{−4}
    ⇒ (ρ_χ/ρ_b) picks up a factor (a_χ/a_b)^{−1} ≈ 10^{−4}.

So at T = m_χ ≈ 96 keV:
    ρ_χ/ρ_b ≈ (16/3) × 10^{−4} ≈ 5 × 10^{−4}.

After that χ also goes non-relativistic and both scale as a^{−3}, so the ratio is *frozen* at ~5 × 10^{−4} all the way to today.

**Predicted Ω_χ/Ω_b ≈ 5 × 10^{−4}**, vs. target 16/3 ≈ 5.33.

**Discrepancy: a factor of ~10^4 in the wrong direction.** The maximum-entropy prediction is off by four orders of magnitude.

## Step 5 — Why the argument fails

The Jaynesian equipartition argument is blind to the *kinematic history* after equipartition is set. The 16/3 DOF ratio is a statement about relativistic phase space, not about mass. Once either sector's temperature falls below its mass, that sector's energy density stops scaling as T^4 and instead tracks mn ∝ T^3. The sector that becomes non-relativistic *later* (χ, because m_χ ≪ m_b) loses energy density faster relative to the sector that became non-relativistic first (baryons, which got frozen earlier in comoving terms).

The net effect is a large mass-hierarchy suppression of ρ_χ/ρ_b. Specifically, if both sectors are thermal with a common temperature:

    ρ_χ(today) / ρ_b(today) = (g_χ m_χ / g_b m_b) × (T_χ/T_b)^3_{at equipartition}

With T_χ = T_b at equipartition and plugging numbers:
    = (16/3) × (m_χ/m_b) = (16/3) × (9.6×10^{−5} / 1) ≈ 5 × 10^{−4}.

This is the same 5 × 10^{−4}. The mass ratio m_χ/m_b ≈ 10^{−4} is what wrecks the prediction.

## Step 6 — Can anything rescue it?

To get Ω_χ/Ω_b = 16/3 with the correct phenomenology (Ω_χ/Ω_b ≈ 5.33 from Planck), one needs either:

(a) **Different temperatures:** T_χ ≠ T_b at equipartition, with (T_χ/T_b)^3 ≈ 10^4, i.e. T_χ ≈ 21 T_b at the moment ρ_χ and ρ_b decouple. No symmetry in CP²×S³ motivates this; it would be an *ad hoc* tuning.

(b) **Non-thermal χ:** χ produced by a mechanism that is not a thermal relic at all — e.g. misalignment, inflaton decay branching, or a gravitational Bogoliubov calculation (H9/H1-series). In that case the 16/3 is not a max-entropy result.

(c) **χ is not matter-like today:** if χ is ultralight and behaves as dark radiation or dark energy, it bypasses the m_χ n_χ scaling. But then it is not Ω_χ and doesn't match the CDM budget.

None of these are consequences of maximum entropy. They are additional assumptions grafted onto it.

## Step 7 — Honest conclusion

**Maximum entropy does NOT give Ω_χ/Ω_b = 16/3.**

- The Jaynes calculation reproduces 16/3 as the high-T equipartition ratio, matching the DOF count g_χ/g_b = 16/3. This is correct but trivial.
- Gravitational scattering never equilibrates the sectors below the Planck scale, so the 16/3 initial condition must be *postulated*, not derived.
- Even if postulated, the ratio is destroyed by the mass-dependent non-relativistic transitions. The final present-day ratio is suppressed by m_χ/m_b ≈ 10^{−4}, giving Ω_χ/Ω_b ≈ 5 × 10^{−4}, which is **four orders of magnitude too small**.
- The numerical coincidence Ω_χ/Ω_b^{obs} ≈ 5.33 and g_χ/g_b = 16/3 ≈ 5.33 cannot be explained by maximum entropy applied to a thermal relic.

**This approach joins H9, J1-2, J1-3 in the list of failed derivations.** The fact that *all* equilibrium/max-entropy/equipartition arguments fail in the same way — they set the right ratio at high T but cannot preserve it across the mass thresholds — is informative: it suggests the 16/3 match, if not a coincidence, must come from a **non-thermal** mechanism in which χ's abundance is set by a process that already knows about its mass (misalignment with m_χ-dependent initial field displacement, inflationary Bogoliubov with a specific k/m_χ structure, or direct topological fixing of the comoving number density at a single epoch with no subsequent thermalization).

**Recommendation:** abandon maximum-entropy / equilibrium derivations and focus on topological / non-thermal production channels for the next round.

---
*End K1-5*
