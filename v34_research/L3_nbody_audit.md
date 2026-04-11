# L3: Audit of the v3.3 N-body "5.4× Overshoot" Claim

**Agent:** L3
**Date:** 2026-04-06
**Task:** Verify the exact simulation parameters behind the v3.3 PM-sim 5.4× overshoot claim and determine whether the 5.4 ≈ Ω_c/Ω_b ≈ 5.43 coincidence is at 0.5% precision or a much looser estimate.

---

## 1. Source in the Manuscript

File: `/Users/garyalcock/claudecode/densityfielddynamics/Density_Field_Dynamics__A_Complete_Unified_Theory__v3_3/section_cosmology.tex`
Lines 689–706 (paragraph "Proof-of-concept: N-body structure formation").

Literal paper claim:

- Particle-mesh sim, 64³ grid, 200 Mpc/h box
- Three runs on identical ICs:
  1. ΛCDM with Ω_m = 0.30
  2. Newtonian baryons, Ω_b = 0.049
  3. DFD baryons, Ω_b = 0.049, μ(x) = x/(1+x)
- Newtonian: δ_rms = 1.5 × 10⁻⁴
- DFD: δ_rms = 6.4 × 10⁻³ (43.8× more than Newton)
- "5.4× overshoot relative to ΛCDM"
- Paper attributes the overshoot to the absence of an imposed cosmological EFE (a_ext ∼ cH₀ ≈ 6 a₀), claiming ~400× raw enhancement drops to ~1.2× with EFE.
- Explicitly flagged as "proof-of-concept at 64³ resolution; production-quality results require ≥256³ with the EFE implemented."

No appendix is referenced for the simulation itself; the paragraph cites only `Appendix~\ref{app:temporal-completion}` for the dust branch derivation, not for the sim. The sim has no companion paper, no Zenodo archive, and no code listing in the repo for the 200 Mpc/h run.

---

## 2. Requested Parameter Extraction

| Item | Value in v3.3 text | Reproducible? |
|------|-------------------|---------------|
| Box size | 200 Mpc/h comoving | Only in prose |
| Grid | 64³ = 262,144 cells | Only in prose |
| Particle count | not stated (presumed 64³) | — |
| μ function | x/(1+x) ("simple") | Stated |
| EFE imposed | **No** (explicitly) | Stated |
| a_ext value | Not applied; cH₀ ∼ 6 a₀ cited as what *should* be used | — |
| Initial power spectrum | **Not stated** — neither Eisenstein-Hu, CAMB, BBKS, nor power-law; no σ₈_lin, no tilt, no seed | Not reproducible |
| z range | Not stated in the paper paragraph | — |
| Solver | Particle-mesh (undocumented which μ-Poisson scheme) | — |
| What "overshoot" ratios | δ_rms(DFD) / δ_rms(ΛCDM) | — |

**δ_rms is the volume-RMS of the density contrast field** on the grid at z = 0. Not σ₈, not P(k) amplitude, not growth factor D₊. It's the cell-wise RMS of δ = (ρ − ρ̄)/ρ̄ at the final snapshot.

### Implied ΛCDM number

The paper gives 5.4× explicitly, so:

    δ_rms(ΛCDM) = 6.4e-3 / 5.4 ≈ 1.185e-3 ≈ 1.2 × 10⁻³.

This number appears nowhere in the paper — it is **back-computed** from the stated ratio. Correspondingly the ΛCDM 1.2 × 10⁻³ is an **implied, not reported, simulation observable**.

---

## 3. Reproducibility Status (a/b/c question)

Searched the repo for code, logs, or data files matching "200 Mpc/h, 64³, Ω_m=0.30, Ω_b=0.049, identical ICs" N-body runs. Found:

- `pk_research/R5_nbody_dfd.py` + `R5_nbody_results.md` — 500 Mpc/h, 64³, EFE **imposed** via |∇Φ_eff|² = |∇Φ_pert|² + (cH)². DFD/Newton σ₈ ratio = **1.12**, DFD/ΛCDM σ₈ ratio = **0.10**. Does **not** reproduce 43.8× or 5.4×.
- `pk_research/R7_nbody_no_efe.py` + `R7_nbody_no_efe_results.md` — 500 Mpc/h, 64³, no EFE. σ₈(MOND)/σ₈(Newton) = **15.35**, not 43.8. σ₈(MOND)=0.773, which compared to an LCDM σ₈ ≈ 0.81 is ≈ 0.95 (not a 5.4× overshoot).
- No 200 Mpc/h PM code anywhere in the repo.
- `pk_research/R2_agent_xbar_derivation.md` (prior agent) confirms: "The Lambda-CDM implied: δ_rms ~ 1.2e-3 — (DFD overshoots by 5.4x)". The word **"implied"** is the prior agent's reading, i.e. there is no stored ΛCDM run in this resolution/box.

### Verdict on reproducibility

- **(a) Reproducible from a published simulation:** **No.** The 200 Mpc/h run referenced in v3.3 §12 has no code, no snapshot, no data file, and no parameter deck in the repository. Two near-cousins exist at 500 Mpc/h but neither reproduces 43.8× or 5.4×.
- **(b) Estimate with 10–20% error bars:** **Yes, and at the larger end.** A 64³ grid with 200 Mpc/h cells (cell size 3.1 Mpc/h) is extremely coarse; δ_rms on this grid is dominated by the ~15 largest-wavelength modes with severe cosmic variance. At N_modes ≈ 64³/2 resolving scales k > 1 h/Mpc, but the σ₈ sphere (8 Mpc/h radius) contains only ~260 cells, a single-realisation RMS uncertainty on δ_rms of **~15–25%** is expected from cosmic variance alone; the DFD μ-feedback compounds this. Additionally the ΛCDM "1.2e-3" number is a paper-asserted back-computation, not a measurement. Overall the 5.4 figure should be read as ~5.4 ± 1.0 (≳ 18% fractional uncertainty).
- **(c) Analytic formula that happens to equal 5.4:** **No.** No analytic expression in v3.3 evaluates to 5.4 at this point. The paper frames the 5.4× as an *empirical numerical overshoot* to be *cured* by a currently-unimplemented EFE, and projects the corrected enhancement to "∼1.2", not "∼5.4/1.2 = 4.5" or anything similar. The "~400" enhancement and "~1.2" post-EFE are both scale estimates, not equations.

---

## 4. Comparison to the Corrected K1-1 Claim (5.4 ≈ Ω_c/Ω_b)

The K1-1 re-read (`v34_research/K1_01_v33_re_read.md`, §3) is the first place in the v34 campaign to notice:

    Ω_c/Ω_b ≈ 0.266 / 0.049 ≈ 5.43

numerically matches the N-body "5.4×". Is the match at 0.5%?

### Numerical check

- Planck 2018 Ω_b h² = 0.02237, Ω_c h² = 0.1200, h = 0.6736 → Ω_b = 0.0493, Ω_c = 0.2646. Ratio = **5.367**.
- Paper-used Ω_b = 0.049 and (presumed) Ω_m = 0.30 → Ω_c = 0.30 − 0.049 = 0.251 → Ratio = **5.122**.
- N-body overshoot stated as "5.4×" (one significant figure plus a decimal; no uncertainty quoted).

So depending on which value of Ω_c is chosen, Ω_c/Ω_b ∈ [5.12, 5.43]. The N-body overshoot is "5.4" to one decimal place, no error bar.

### Is the match at 0.5%?

**No — the agreement is at best at the ~1% level in the narrowest reading and at worst ~6% if one uses the paper's own Ω_m = 0.30.** Much more importantly, the N-body number carries an irreducible **~20% single-realisation cosmic-variance uncertainty** and the ΛCDM denominator in the ratio is a *back-computed* number the paper never actually reports. The coincidence is at the level of "two single-decimal-place numbers agree"; it is **not** at the level a high-precision prediction would require.

The precise statement is:

    5.4 (N-body, no error bar, irreproducible) ≈ 5.43 (Planck) ≈ 16/3 = 5.333
    |5.4 − 5.43|/5.43 ≈ 0.55%   (if Planck Ω_c used)
    |5.4 − 5.12|/5.12 ≈ 5.5%    (if paper's own Ω_c = 0.251 used)
    |5.4 − 5.333|/5.333 ≈ 1.3%  (vs 16/3)

The *central-value* numerical coincidence with Planck's Ω_c/Ω_b is at ~0.5% if and only if one ignores (i) the ~20% sim uncertainty, (ii) the irreproducibility of the ΛCDM baseline, and (iii) the fact that the paper uses Ω_m = 0.30, not the Planck value. With the paper's own cosmology, the match drifts to ~5%.

---

## 5. Bottom-Line Finding

1. The "5.4× overshoot" in v3.3 §12 has **no reproducible code, no initial power spectrum specified, no redshift range specified, and no error bar**. It is a single-realisation 64³/200-Mpc/h PM number whose ΛCDM comparator is **inferred, not simulated**.
2. The number is reproducibility-category **(b)** — an estimate that intrinsically carries ≳15–20% uncertainty from cosmic variance and grid resolution. 5.4 ≈ 16/3 = 5.333 is consistent within that uncertainty (0.06/5.333 ≈ 1.3%), but this is not a stringent test.
3. The coincidence with Ω_c/Ω_b is at ~0.5% only when pitted against the Planck value, not the paper's own Ω_m = 0.30 (which gives 5.12, a 5% miss). Combined with the ≥20% simulation error bar, **the 0.5% agreement is an artefact of (i) rounding "5.4" to one decimal place, (ii) choosing the most favourable Ω_c value, and (iii) not carrying simulation error bars**.
4. Existing higher-quality runs in the repo (R5 at 500 Mpc/h with EFE, R7 at 500 Mpc/h without EFE) give enhancement ratios of 1.12× and 15.35× respectively — **neither reproduces the 5.4×** claimed in the manuscript. The 5.4× number is effectively stranded: it belongs to a lost simulation.
5. **Recommendation for v34:** Either (a) rerun the 200 Mpc/h PM proof-of-concept, archive the code + seeds + ICs, and quote δ_rms(DFD)/δ_rms(ΛCDM) with a proper Monte-Carlo error bar across ≥10 seeds; or (b) drop the 5.4× number from the manuscript and replace it with the R5/R7 results which *are* reproducible. Under no circumstance should "5.4 ≈ Ω_c/Ω_b ≈ 5.43 at 0.5%" be presented as a structural prediction — the numerical and methodological precision does not support that claim.

### One-line summary
The v3.3 "5.4× overshoot" is (b) — an estimate with ≳20% de-facto error bars from a single-seed, unreproducible 64³ PM run whose ΛCDM denominator was never actually simulated — so its numerical agreement with Ω_c/Ω_b ≈ 5.43 (and 16/3 ≈ 5.33) is compatible but not diagnostic, and the apparent 0.5% precision is an artefact of one-decimal rounding plus cherry-picking the Planck Ω_c rather than the paper's own Ω_m = 0.30.
