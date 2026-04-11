# Relic Abundance at (n=3, p=7) α-Tower Rung

**Date:** 2026-04-07
**Inputs:** m_χ = 1.18 keV (ReAudit-4a, clean R8 lattice cosine), f_a = 9.5×10¹¹ GeV (n=3 rung: α³·M̄_P = 9.46×10¹¹ GeV, consistent with f_a to 0.4%), θ_i ~ O(1), standard cosmology, generic ALP potential with T-independent mass.

---

## 1. Oscillation Temperature

With a temperature-independent mass (the DFD lattice cosine minimum is fixed by α-tower geometry, not by QCD-like instanton screening at high T), 3H(T_osc) = m_χ gives

  T_osc = [m_χ M_P / (3·√(π²g*/90))]^{1/2} ≈ 5.78×10⁵ GeV ≈ 580 TeV

using g*(T_osc) ≈ 75. This is **deep in the radiation era**, far above T_eq (~0.8 eV) and far above Λ_QCD (~0.2 GeV). The radiation-dominated, sudden-onset misalignment approximation is valid.

## 2. Misalignment Relic (First Principles)

ρ_χ(T_osc) = ½ m_χ² f_a² θ_i² = 6.28×10¹¹ GeV⁴
Y_χ = n_χ/s = (ρ_osc/m_χ) / [(2π²/45)g_{*S}(T_osc)·T_osc³] ≈ 8.4×10⁻²

Redshifting to today with entropy conservation (g_{*S,0} = 3.91, T_0 = 2.348×10⁻⁴ eV):

  **Ω_χ h² ≈ 27 · θ_i²**

## 3. Cross-Checks

| Formula | Ω_χ h² | Note |
|---|---|---|
| First principles (this work) | 27 | clean calc, g*(T_osc)=75 |
| Marsh 2016 ultralight form, 0.12·(f/10¹⁷)²·(m/10⁻²² eV)^½ | 37 | factor ~1.4 from g* convention |
| Visinelli–Gondolo 2009 QCD form, 0.236·(f/10¹²)^{7/6} | 0.22 | **inapplicable** — assumes T-dep QCD-instanton mass, not T-indep cosine |
| Arias et al. 2012 ultralight, 0.16·(m/eV)^{½}·(f/10¹⁷)² | 5×10⁻¹⁰ | **inapplicable** — Arias fit assumes late oscillation (T_osc ≲ MeV); breaks badly for T_osc ~ 500 GeV |

The first-principles calc and Marsh 2016 (the two formulas valid in this regime) agree within 40%, cross-confirming **Ω_χ h² ≈ 27 · θ_i²**.

## 4. Ratio to Observation

Observed Ω_c h² = 0.1200 ± 0.0012 (Planck 2018).

  **Ω_χ / Ω_obs ≈ 225 · θ_i²**

**The (n=3, p=7) rung OVERSHOOTS by a factor of ~225 at θ_i ~ 1.**

## 5. Tuning Required

To match observation: θ_i = √(0.12/27) ≈ **0.067** (i.e., ~2.1% of π, ~3.8% of π as a fraction of the natural range).

Tuning penalty: **θ_i² ≈ 4.4×10⁻³**, a ~225× fine-tuning relative to the natural O(1) expectation. The "axionic anthropic window" (Wilczek, Tegmark et al.) permits θ_i down to ~0.01 before the tuning cost becomes implausible — so θ_i ≈ 0.067 is near the edge of the acceptable window but NOT yet catastrophic. It is, however, unmotivated from any DFD-internal symmetry (the lattice cosine does not select small θ).

Maximum boost from anti-tuning (θ_i → π) is only π² ≈ 9.87, insufficient to rescue underproduction scenarios and irrelevant here since we overshoot.

## 6. Alternative Production Channels (not needed, but relevant if θ_i is down-tuned)

- **Gravitational production (Ford 1987, Parker–Toms):** Y_χ^grav ~ 10⁻³·(m_χ/H_inf)^{3/2} ≈ 10⁻³⁰ for H_inf ~ 10¹³ GeV. Negligible contribution.
- **Scalaron portal σ → χχ (M15, BR = 1/5):** Rough estimate with T_rh ~ 3×10⁹ GeV, m_σ ~ 3×10¹³ GeV gives Ω_χ h² ~ 10⁻² from this channel — subdominant to misalignment overshoot, but would be the **only** channel that could regenerate Ω_c h² ≈ 0.12 if θ_i were suppressed by an additional factor, e.g., by early-universe Hubble friction or topological pinning. Present overshoot makes this moot.
- **Inflaton direct coupling:** model-dependent, typically Ω h² ~ 10⁻⁴ to 10⁻² for gravitational/Planck-suppressed operators; subdominant here.

Since misalignment alone already overshoots, no additional channel is needed — in fact additional channels make the tension worse.

## 7. SN1987A Bound Check (ReAudit-4c cross-check)

Axion–photon coupling on the α-tower: g_aγγ ~ α/(2π·f_a) ≈ (1/137)/(2π·9.5×10¹¹ GeV) ≈ 1.2×10⁻¹⁵ GeV⁻¹.

SN1987A bound (Raffelt 2008, Payez et al. 2015): g_aγγ ≲ 5.3×10⁻¹² GeV⁻¹ for m_a ≲ 100 MeV.

**Margin: 4.4×10³ below bound.** Coupling is far too weak for Primakoff production/trapping in the supernova core. ReAudit-4c's claim is **confirmed**. Electron and nucleon couplings (model-dependent but typically ~m_e/f_a and m_N/f_a) are similarly ~10⁻¹⁵, well below their respective SN bounds (~10⁻⁹ for nucleons, ~10⁻¹⁰ for electrons).

## 8. Cosmological / Structure Bounds on m_χ = 1.18 keV

**Critical distinction:** Misalignment χ is produced as a **cold, coherent Bose condensate** (occupation number (f_a/m_χ)² ~ 10³⁶ per de Broglie volume at T_osc), NOT as a thermal relic. Thermal warm-DM bounds DO NOT apply.

- **Lyman-α (thermal WDM: m ≳ 3 keV, Iršič et al. 2017):** inapplicable. The Ly-α bound is on the free-streaming length ~ σ_v/H. For misalignment, σ_v ≈ 0 at production (field is coherent) and the free-streaming scale is set by v_osc ~ (T_osc/m_χ)·(a_osc/a_0) ~ 10⁻¹⁴ today — completely negligible compared to thermal WDM σ_v ~ 10⁻⁴. **Cleared by ~10 orders of magnitude.**
- **CMB free-streaming (Planck):** bound is on the thermal component; misalignment χ contributes as CDM with N_eff shift ≈ 0. Cleared.
- **Galaxy substructure / ultralight DM de Broglie:** λ_dB = 2π/(m_χ v) ≈ 2π/(1.18 keV · 10⁻³ c) ~ 10⁻⁹ pc. Negligible quantum pressure on any astrophysical scale; behaves as CDM. Cleared.
- **X-ray line / decay:** for an ALP with m = 1.18 keV and f_a = 9.5×10¹¹ GeV, τ_{χ→γγ} ~ 64π/(g_aγγ² m_χ³) ~ 10³⁴ s ≫ t_U. No decay-line constraint. Cleared.

**All standard warm/ultralight DM bounds are cleared.** m_χ = 1.18 keV is a perfectly viable cold DM mass in the coherent misalignment production channel.

## 9. Verdict

(a) **(n=3, p=7) with θ_i ~ 1 gives Ω_χ h² ≈ 27, a factor of 225× too large — a ~15σ mismatch with Planck (where σ ≈ 0.001 on Ω_c h²).**

(b) **Tuning required:** θ_i ≈ 0.067 (≈ 2% of π). This is a ~225× fine-tuning, sitting at the edge of the "natural misalignment" window but technically not anthropically forbidden. There is **no DFD-internal mechanism** identified that would dynamically select this value — the lattice cosine geometry places θ_i uniformly on (-π, π], so small θ_i carries a 4% prior cost on top of any other DFD penalties.

(c) **Overall assessment — MARGINAL, with caveats:**
 - The rung passes **all astrophysical bounds** (SN1987A, Ly-α, CMB, substructure, decay) — these are cleared by large margins.
 - The rung **fails to naturally reproduce Ω_c h²** at θ_i ~ 1; it requires a 4% tuning of the initial misalignment.
 - The QCD-axion-like VG formula **accidentally** gives Ω h² ~ 0.22 at θ_i ~ 1, but this is not applicable because DFD's potential has a T-independent cosine, not a QCD-instanton-suppressed one. **Earlier audits that quoted this number were using the wrong formula.**
 - A rung with **smaller f_a** (larger n) would reduce Ω by (f_a)², since Ω ∝ f_a² for fixed m. Specifically, f_a ≈ 6.3×10¹⁰ GeV would exactly match Ω_c h² at θ_i ~ 1 — this is roughly α¹·M̄_P scaled down by an additional factor of ~15, NOT on a clean α-tower rung.
 - Alternatively, a rung with **smaller m_χ** at the same f_a would reduce Ω. Since Ω ∝ m_χ^{1/2}·f_a² (T-indep mass regime, using Marsh), halving m_χ to ~0.5 keV reduces Ω by √2, and pushing to sub-eV ultralight regime would land near observation — but this conflicts with the R8 lattice audit that pins m_χ = 1.18 keV.

**Conclusion:** (n=3, p=7) is **not a natural self-consistent DFD χ dark matter rung**. It passes all bounds but requires a 4% tuning of θ_i to land on Ω_c h². This is **better than the other rungs checked so far** (which either failed SN1987A, Ly-α, or overshot by orders of magnitude more), so it is currently the **least-bad candidate**, but it does not close the DFD dark-matter story cleanly. A full α-tower scan (M14) should check whether any (n, p) pair gives Ω h² ≈ 0.12 at θ_i ~ 1 without invoking tuning. If none does, the DFD χ-as-DM program needs either (i) a dynamical θ_i selection mechanism, (ii) late entropy dilution (but the overshoot here is only 225×, so the dilution would have to be mild), or (iii) acceptance of a 4% anthropic tuning as the final answer.

**Recommended next step:** extend M14_rung_scan.md to sweep (n, p) in the neighborhood of (3, 7) and report the exact rung where Ω h² crosses 0.12 at θ_i = 1. If that rung exists on the α-tower grid, it supersedes (3, 7). If it doesn't, (3, 7) with θ_i ≈ 0.067 is the final DFD χ-DM rung.
