# M12: Running of α and Cosmic Birefringence in DFD

**Date:** 2026-04-07
**Status:** Numerical analysis — addresses L13 flag on β = c_ψ·Δψ/(2 M_P)
**Question:** Does RG running of α from M_P (or M_c) down to CMB photon energies (~10⁻⁴ eV) shift the predicted birefringence angle β by an O(1) factor capable of rescuing β ≈ α/2 ≈ 0.21°?

---

## 1. Setup

The DFD prediction for cosmic birefringence (axion–photon Chern–Simons coupling) is

  β = (c_ψ / 2) · (Δψ / M_P),

with the coupling identified as c_ψ = α(μ)/π in the dimensionally reduced effective action. The scale μ at which α should be evaluated is the central question: the coupling c_ψ is *generated* at compactification scale M_c ~ M_P (topological winding k_max=60 across the internal manifold), but the physical observable — the rotation of the linear polarization of CMB photons — happens at photon energy μ_γ ~ 2.7 K ~ 2.3 × 10⁻⁴ eV.

If c_ψ were a *Wilson coefficient* of a higher-dimensional operator (1/M_P) F F̃ ψ, it would not run between M_P and μ_γ at one loop in QED (the operator is dimension-5 and not renormalized by QED in the standard sense — its only running is the multiplicative anomalous dimension of ψ, plus the implicit running of α inside c_ψ if we *define* c_ψ via α at some matching scale). The relevant question is therefore: at what scale do we evaluate α?

---

## 2. Standard SM running

QED running of α (one-loop, charged-fermion thresholds, then the full SM above M_Z):

| Scale μ | α(μ)⁻¹ | α(μ) | α(μ)/π |
|---|---|---|---|
| 0 (Thomson) | 137.036 | 7.297 × 10⁻³ | 2.323 × 10⁻³ |
| m_e | ≈ 137.036 | 7.297 × 10⁻³ | 2.323 × 10⁻³ |
| m_τ | ≈ 133.5 | 7.491 × 10⁻³ | 2.385 × 10⁻³ |
| M_Z | 127.952 | 7.816 × 10⁻³ | 2.488 × 10⁻³ |
| 1 TeV | ≈ 126.9 | 7.880 × 10⁻³ | 2.508 × 10⁻³ |
| M_GUT ~ 2 × 10¹⁶ GeV | ≈ 98–100 (SM, no SUSY) | 1.013 × 10⁻² | 3.224 × 10⁻³ |
| M_P ~ 1.22 × 10¹⁹ GeV | ≈ 96 (SM extrapolation) | 1.042 × 10⁻² | 3.317 × 10⁻³ |

(SM extrapolation to M_P uses the U(1)_Y coupling in GUT-normalised form g₁² = (5/3) g'², converted back to α_em via α⁻¹ = (5/3)/α₁ + 1/α₂. The number ~96 is standard; e.g. Buttazzo et al. 2013, Fig. 2.)

**Ratios relative to α(0) = 1/137.036:**

- α(M_Z)/α(0) = 137.036/127.952 = **1.0710**
- α(M_P)/α(0) = 137.036/96 = **1.428**
- (α/π) shift from CMB to M_P: factor **1.428** (≈ +43%)

---

## 3. Numerical impact on β

The DFD prediction with α evaluated at the *generation* scale and Δψ ≈ M_P (natural displacement of the axion across one e-fold of inflation, or one winding cycle):

  β = (1/2π) · α(μ) · (Δψ/M_P).

For Δψ/M_P = 1 (the maximal natural value):

| μ | α(μ)/π | β [rad] | β [deg] |
|---|---|---|---|
| CMB (Thomson) | 2.323 × 10⁻³ | 1.16 × 10⁻³ | 0.0666° |
| M_Z | 2.488 × 10⁻³ | 1.24 × 10⁻³ | 0.0712° |
| M_P (SM extrap.) | 3.317 × 10⁻³ | 1.66 × 10⁻³ | 0.0950° |

**The observed value (Minami & Komatsu 2020; Eskilt et al. 2023):** β_obs = 0.342° ± 0.094° (≈ 0.30–0.44°).

The "naive" target β ≈ α/2 ≈ 0.21° (which is what the user's L13 note refers to) requires *not* α/π but α/2 — already a factor 2π/2 = π ≈ 3.14 larger than what the Chern–Simons coupling c_ψ = α/π actually delivers at Δψ = M_P.

---

## 4. Does RG running rescue the prediction?

**No.** The arithmetic is unambiguous:

1. **CMB → M_Z running** gives factor 1.071. Negligible (~7%).
2. **CMB → M_P running** gives factor 1.428. Still only ~43%, far short of the factor π ≈ 3.14 needed to lift α/π up to α/2.
3. The observed β/predicted β at M_P with Δψ = M_P is 0.342°/0.095° ≈ **3.6×** too small even with maximal running and maximal axion displacement.

To match β_obs the model needs *either*:
   - c_ψ ≈ 3.6 × α/π ≈ α · 1.14 (an O(1) coefficient ~1, not α/π), or
   - Δψ/M_P ≈ 3.6 (super-Planckian, generically problematic for axion EFTs), or
   - Both an enhanced coupling and a moderately super-Planckian field range.

Running of α alone — even taken to M_P — supplies at most a factor 1.43, leaving a residual deficit of 3.6/1.43 ≈ **2.5**.

---

## 5. DFD-specific subtlety: topological freezing at k_max

DFD's tower theorem fixes α through the topological winding number k_max = 60 of the internal U(1) bundle, via 1/α = (2/π)·k_max·(something) ≈ 137.036 at the matching scale. The question is whether this *fixes* α at its low-energy value (in which case there is no running and α(M_P) = α(0)) or whether the topological structure only sets the boundary condition at the high scale and the SM RG runs it down.

Two interpretations:

**(A) Topological lock — no running.**
If k_max=60 fixes α at *all* scales (because the integer winding cannot change continuously), then α(M_P) = α(M_Z) = α(0) = 1/137.036. The factor 1.43 enhancement *vanishes*, and β at the generation scale equals β at the CMB. The prediction is unchanged: β ≈ α/(2π) · (Δψ/M_P) ≈ 0.067° for Δψ = M_P, far below the observed 0.342°.

**(B) Topological boundary condition at M_c, SM running below.**
If k_max=60 fixes α(M_c) and SM loops carry it down to α(0) = 1/137.036, then matching M_c ~ M_P and inverting gives α(M_c)⁻¹ ≈ 96, matching the standard SM extrapolation. Used in c_ψ = α(M_c)/π, this enhances β by 1.43 → 0.095°. Still a factor 3.6 short.

**Either way, RG running does not rescue β ≈ α/2.**

---

## 6. What would rescue it

The factor of π discrepancy between c_ψ = α/π (what the dimensional reduction of F∧F gives) and c_ψ = α (what β ≈ α/2 demands at Δψ = M_P) cannot come from running. It must come from:

- a **multiplicity factor** in the dimensional reduction (e.g. summing over k_max=60 winding modes, which gives a factor 60/(2π) ≈ 9.5 — *too much*, would overshoot β by ×9.5/3.6 ≈ 2.6),
- an **anomaly coefficient** N_c·Q² summed over SM fermions in the loop generating ψFF̃ (the QED chiral anomaly contributes ∑ Q² ≈ 8/3 from one quark generation, ~20/3 from three; this gives the right ballpark but is *not* the same as α running),
- a **non-trivial trace** over internal-manifold zero modes (DFD-specific; the F∧F kernel may pick up a sum over k_max=60 harmonic forms).

The cleanest rescue is the third: if c_ψ = (k_max / 2π) · (α/π), then with k_max = 60 we get c_ψ = (60/2π) · (α/π) ≈ 9.55 · α/π ≈ 0.022, and β = (c_ψ/2)·(Δψ/M_P) ≈ 0.011 · (Δψ/M_P) rad ≈ 0.64° · (Δψ/M_P). For Δψ/M_P ≈ 0.53 this hits 0.342°. That is *plausible* but requires deriving the multiplicity from the topology, not from QED running.

---

## 7. Conclusion (answers to L13)

1. **Standard SM running M_Z → CMB:** factor 1.071 — negligible.
2. **SM running M_P → CMB:** factor 1.428 — still O(1) but much smaller than π ≈ 3.14.
3. **Topological freezing at k_max=60:** if true, *removes* even the 1.43 factor; the running does nothing because α is locked.
4. **Rescue of β ≈ α/2 ≈ 0.21° via running:** **fails by a factor of ≈ 2.5–3** under any interpretation.
5. **Real rescue path:** the missing factor must come from a *multiplicity / anomaly coefficient* in the F∧F dimensional reduction, specifically a sum over the k_max=60 internal-manifold harmonic 2-forms (or equivalently the SM anomaly trace ∑ N_c Q²). This is a topological prediction, not an RG one, and L13 should be re-flagged accordingly: the physics fix is in the matching coefficient, not in the running.

**Recommendation:** treat the c_ψ = α/π identification as a *placeholder* and recompute c_ψ from the explicit reduction of the 11D Chern–Simons term ∫ C ∧ G ∧ G over the k_max=60 internal cycles. The expected enhancement is O(k_max/2π) ~ 10, which (combined with sub-Planckian Δψ ~ 0.5 M_P) lands naturally on β_obs ~ 0.3°.
