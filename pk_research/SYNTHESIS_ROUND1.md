# P(k) Closure Synthesis — Round 1

## Date: 2026-04-04
## Status: 21/28 agents completed, synthesis in progress

---

## THE CONVERGENT MECHANISM

Five independent agent calculations converge on the same picture:

### 1. The Spatial Sector IS the 3-Laplacian (Agents 7, 8, 11, 13)

The linearization around ∇ψ̄ = 0 is DEGENERATE (μ(0) = 0). The leading-order perturbation equation is NOT a standard Poisson equation but the **p-Laplacian with p = 3**:

    Δ₃(ψ) ≡ ∇·(|∇ψ|∇ψ) = a* S

Key consequences:
- **Green's function**: G₃(r) = C ln(r), NOT 1/r
- **Scaling**: ψ scales as S^{1/2}, NOT S (square-root response)
- **Fourier response**: ψ̂(k) ~ (S δ)^{1/2} k^{-3/2}, NOT Sδ/k²
- **Growth equation**: δ̈ + 2Hδ̇ = A(k) δ^{1/2} (NONLINEAR)
- **Unregulated growth**: δ ~ a³ in EdS (vs a¹ for Newtonian)

This gives ENORMOUSLY enhanced growth: starting from δ ~ 10⁻⁵ at z = 1100, deep MOND gives δ ~ 10⁻⁵ × (1100)³ ≈ 10⁴ by z = 0. Way more than enough — in fact TOO much.

### 2. The Temporal EFE Regulates Growth (Agents 12, 17, 21)

Agent 21 (deep v3.3 reader) found the KEY MECHANISM in the paper itself:

- The v3.3 N-body simulation shows: WITHOUT temporal EFE, δ_rms overshoots ΛCDM by 5.4×
- The paper identifies the temporal EFE from the Hubble flow as the regulator
- Composition law: μ(ψ₀ + Δψ) = 1 - (1-μ(ψ₀))(1-μ(Δψ))
- Background temporal μ₀ ~ 0.854 (from x̄ ~ 5.85 set by Hubble flow ∝ cH₀)
- Perturbation feels: μ_total ~ μ₀ + (1-μ₀)μ(Δψ) ~ 0.854

This means G_eff ~ G/0.854 ~ 1.17G — near-Newtonian for the overall coupling.

### 3. The Two-Regime Growth Picture (Agents 8, 11, 15, 21)

The growth has TWO regimes:

**Spatial-only (p-Laplacian)**: δ ~ a³, overshoots by ~5×
**Temporal-regulated**: G_eff ~ 1.17G, undershoots

The CORRECT growth is the INTERPLAY between these. The spatial nonlinearity provides enhanced growth; the temporal EFE caps it. The effective growth exponent is scale-dependent:

- Large scales (low k): deeper in MOND, more enhancement → growth index p > 1
- Small scales (high k): closer to Newtonian → growth index p ~ 1

This scale-dependence IS the effective transfer function.

### 4. Agent 15 Quantified the Scale-Dependent Growth

From Agent 15's calculation:
- D_MOND/D_LCDM ranges from 0.10 (k=0.005) to 1.70 (k=0.20 h/Mpc)
- MOND growth enhancement: 18.5× at k=0.02 h/Mpc over baryon-only Newtonian
- The P(k) shape TILTS correctly: more power at smaller scales, mimicking CDM

### 5. The Observational Target is Softer Than Assumed (Agents 4, 22, 23)

- S₈ tension: DFD predicting σ₈ ~ 0.79 would be PREFERRED by DES weak lensing
- BAO peak position must match to ~1% (non-negotiable)
- P(k) shape: must match to ~5% for k = 0.05-0.15 h/Mpc
- Agent 22 found: the ψ-screen remaps k-space (k_obs = k_true × e^{Δψ(z)}), which can partially reconcile shape differences

---

## THE GAP: What's Missing

The regulated growth gives σ₈ within a factor of ~2-5 of the target. The remaining shortfall comes from:

1. **The temporal EFE is too strong if μ₀ ~ 0.854**: This nearly kills the MOND enhancement. The growth becomes nearly Newtonian, and baryons-only Newtonian gives σ₈ ~ 0.05.

2. **But if x̄ is set by the PERTURBATION gradient** (not Hubble flow): Then the p-Laplacian nonlinear growth applies, and we get σ₈ overshoot.

3. **The critical question**: What EXACTLY sets x̄ in the DFD perturbation equation? Is it:
   (a) The temporal ψ̇ background (Hubble flow) → x̄ ~ 5.85 → near-Newtonian
   (b) The spatial ∇δψ of the perturbation itself → x̄ ~ δ^{1/2} → deep MOND
   (c) Some combination → intermediate growth

**HYPOTHESIS**: The answer is (c). The full equation of motion includes BOTH the spatial W and temporal K terms. The temporal K term provides a mass-like regulator, but the spatial W term provides the nonlinear enhancement. The competition between them determines the effective growth rate.

---

## THE PATH FORWARD — Round 2 Agent Tasks

1. **Full EOM with both sectors**: Derive the complete perturbation equation from the full action with W + K, including both spatial and temporal contributions.

2. **Numerical ODE solver**: Solve the self-consistent growth equation δ̈ + 2Hδ̇ = 4πG_eff(k, δ, a)ρ̄δ with the correct G_eff from the full two-sector theory.

3. **The composition law applied to perturbations**: Does the saturation-union composition law apply mode-by-mode or collectively? This determines whether the temporal EFE is mode-independent (x̄ same for all k) or mode-dependent.

4. **The ψ-screen effect on observed P(k)**: Quantify the k-space remapping from Agent 22.

5. **Galaxy bias in MOND**: Does the MOND-enhanced clustering change the observed galaxy-matter bias?

---

## KEY NUMBERS FROM AGENTS

| Quantity | Value | Source |
|----------|-------|--------|
| p-Laplacian growth exponent (unregulated) | δ ~ a³ | Agent 11 |
| Temporal EFE μ₀ from Hubble flow | 0.854 | Agent 21 |
| G_eff with full temporal EFE | 1.17G | Agent 21 |
| N-body overshoot without EFE | 5.4× | Agent 21 (from v3.3) |
| Time-averaged ⟨ν⟩ at BAO scale | 1.929 | Agent 15 |
| MOND growth enhancement at k=0.02 | 18.5× | Agent 15 |
| D_MOND/D_LCDM at k=0.20 | 1.70 | Agent 15 |
| Required σ₈ target | 0.77-0.85 | Agent 4 |
| P(k) shape tolerance (k=0.05-0.15) | < 5% | Agent 4 |
| BAO position tolerance | < 1% | Agent 4 |
| Parametric resonance growth | ~3% (negligible) | Agent 18 |
| DC rectification at O(δ²) | ~10⁻⁷ (negligible) | Agent 7 |
| Temporal conservation cap | Ω_ψ < 10⁻¹¹ | Agent 12 |
