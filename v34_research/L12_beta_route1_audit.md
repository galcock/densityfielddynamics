# L12: Route 1 β Prefactor Audit — Independent Derivation

**Agent:** L12
**Date:** 2026-04-06
**Task:** Derive β = f · Δψ · α from DFD Lagrangian, pin down the geometric coefficient f, and check whether H1-5's quoted value 0.197° is self-consistent.

---

## 1. Starting Lagrangian

DFD couples a pseudoscalar ψ to photons through the standard Chern-Simons term:

    ΔL = (c_ψ / 4 M_P) ψ F_μν F̃^μν

where F̃^μν = (1/2) ε^μναβ F_αβ is the dual field strength and c_ψ is the dimensionless coupling. In DFD's normalization, c_ψ is expected to be O(1) and is identified with α/(2π) once the ψ-screen loop is integrated out, i.e.

    c_ψ / M_P  ≡  α / (2π f_ψ)            with  f_ψ = M_P

so the effective coupling is g_ψγγ = α / (2π M_P).

---

## 2. Modified Photon EoM

The term ψ F F̃ can be rewritten (up to a boundary) as

    (c_ψ / M_P) ∂_μ ψ · A_ν ∂_α A_β ε^μναβ

Varying with respect to A_ν gives the modified Maxwell equation:

    ∂_μ F^μν + (c_ψ / M_P) ∂_μ ψ · F̃^μν  =  0

For a plane wave k^μ = (ω, k) propagating in the +z direction through a slowly varying background ψ(t, z), circularly polarized modes A_± pick up a dispersion relation

    ω_±² = k² ± (c_ψ / M_P) · k · ψ̇   (for ∂_z ψ ≪ ψ̇ or covariant combination along k^μ)

The WKB phase difference between A_+ and A_− accumulated along the photon worldline is

    Δφ = ∫ dt (ω_+ − ω_−)  ≈  (c_ψ / M_P) ∫ ψ̇ dt  =  (c_ψ / M_P) · Δψ

The **polarization rotation** is half the phase splitting (E = (A_+ + A_−)/√2, rotation angle = Δφ/2):

    β  =  Δφ / 2  =  (c_ψ / 2 M_P) · Δψ

This is the **textbook Carroll-Field-Jackiw / Harari-Sikivie result** and is independent of frequency, path length, and cosmological background (as long as ψ evolves quasi-statically along the light cone).

---

## 3. Inserting the DFD value of c_ψ

DFD identifies the ψ-screen-induced coupling with the QED anomaly coefficient:

    c_ψ / M_P  =  α / (π f_ψ)           (anomaly with N_f = 1, Q = 1)

Two conventions appear in the literature; they differ by a factor of 2:

| Convention | c_ψ/M_P | β |
|---|---|---|
| A. Anomaly, f_ψ = M_P, no 2π | α/(π M_P) | β = α/(2π) · Δψ |
| B. Anomaly, f_ψ = M_P, with 2π | α/(2π M_P) | β = α/(4π) · Δψ |
| C. "Natural" f = 1, Peccei-Quinn | 1/M_P | β = (1/2) · Δψ (absurdly large) |

H1-5 used a **fourth** convention:

    β  =  (π/2) · Δψ · α

Let's see where (π/2) could come from.

---

## 4. Where Does π/2 Come From?

Starting from the clean Harari-Sikivie relation β = (1/2) (c_ψ/M_P) Δψ, to reproduce β = (π/2) α Δψ one needs

    c_ψ / M_P  =  π · α / (1)   ⇒   c_ψ = π α M_P  ≈  0.023 M_P

That is **not** the DFD anomaly value. The anomaly gives c_ψ/M_P = α/(π M_P) (convention A), which leads to

    β_A  =  (1/2) · (α/π) · Δψ  =  (α / 2π) · Δψ

For Δψ = 0.27, α = 1/137:

    β_A  =  (1/(2π · 137)) · 0.27  =  3.14 × 10^(−4) rad  =  **0.0180°**

This is **an order of magnitude smaller** than H1-5's 0.197°.

Convention B gives β_B = 0.0090° — even smaller.

To hit 0.197° one needs a coefficient of ≈ π/2 ≈ 1.57, which is a factor of ≈ 10 larger than the anomaly value α/(2π) ≈ 0.00116. The ratio is exactly (π/2)/(α/2π) = π²/α ≈ 1352. No — let me redo: (π/2)/(1/(2π)) = π². So H1-5's coefficient is π² ≈ 9.87 times larger than convention A once α is factored out.

**Put differently:** H1-5 wrote β = (π/2) Δψ α instead of β = (1/(2π)) Δψ α. These differ by a factor of π² ≈ 9.87.

---

## 5. Numerical Comparison

Compute each candidate for Δψ(z_rec) = 0.27, α = 1/137.036:

| Formula | Value (rad) | Value (deg) |
|---|---|---|
| β = (π/2) · Δψ · α   [H1-5] | 3.094 × 10⁻³ | **0.1773°** |
| β = (1/2) · Δψ · α    (no π) | 9.85 × 10⁻⁴ | 0.0564° |
| β = (1/(2π)) · Δψ · α  (anomaly, conv. A) | 3.14 × 10⁻⁴ | **0.01796°** |
| β = (1/(4π)) · Δψ · α  (anomaly, conv. B) | 1.57 × 10⁻⁴ | 0.00898° |
| β = Δψ · α           (no geometric factor) | 1.97 × 10⁻³ | 0.1129° |

Observations:

1. H1-5's stated formula (π/2)·Δψ·α gives **0.177°**, not 0.197°. The quoted 0.197° is already internally inconsistent with the formula by ~11%. Most likely H1-5 used α = 1/128 (running α at electroweak scale) or Δψ = 0.30, or dropped a factor somewhere.
2. Check: (π/2) · 0.30 · (1/137) = 0.00344 rad = 0.197°. **Yes — H1-5 implicitly used Δψ = 0.30, not 0.27.** So the arithmetic is self-consistent for a slightly different Δψ.
3. The **DFD-correct anomaly prefactor** (convention A) gives β = 0.018°, which is **an order of magnitude below** the observed Planck+ACT birefringence signal (β_obs ≈ 0.35° ± 0.14°, Minami-Komatsu 2020; more recent ≈ 0.30°).
4. H1-5's (π/2) coefficient is **not derivable from the standard Chern-Simons term** with canonical anomaly normalization. It requires either (a) a non-standard ψ-screen loop giving an enhanced prefactor ~π², or (b) a redefinition of Δψ that absorbs the 1/(2π)² (e.g., Δψ here means Δψ in units of f_ψ/π² rather than f_ψ).

---

## 6. Dimensional Analysis Check

[β] = radians = dimensionless. [Δψ] = dimensionless (ψ in Planck units). [α] = dimensionless. So any pure number f works dimensionally — dimensional analysis alone cannot fix f. The factor must come from the explicit WKB integration in Section 2, which gives **f = 1/2** (bare Harari-Sikivie) × the coupling c_ψ/M_P.

The only way f = π/2 arises is if c_ψ/M_P = π (setting α to the side), which would mean the ψ-photon coupling is O(1) in Planck units — i.e. ψ is **not** anomaly-suppressed. That contradicts the DFD derivation where ψ-screen gives the coupling through an EM loop (which unavoidably brings α/(2π)).

---

## 7. Does It Fit the Observed Signal?

Observed β_CMB ≈ 0.30° ± 0.11° (Eskilt+Komatsu 2022, combined Planck + WMAP).

- **H1-5's formula** (β = (π/2) Δψ α): 0.18°–0.20° depending on Δψ. Within 1σ of observation. ✓
- **Correct anomaly prefactor** (β = Δψ α/(2π)): 0.018°. **16σ below observation.** ✗
- **To reach 0.30° with the correct anomaly**, need Δψ ≈ 4.5 — i.e. ψ must move by several Planck units between recombination and today, which is in tension with DFD's "slow-roll-like" ψ evolution.

---

## 8. Conclusion

1. **H1-5's arithmetic is self-consistent** if Δψ(z_rec) = 0.30, not 0.27. With Δψ = 0.27 the same formula gives 0.177°, so 0.197° is a typo or uses a slightly larger Δψ.
2. **H1-5's prefactor (π/2) is NOT derivable from the standard Chern-Simons coupling.** The correct Harari-Sikivie / Carroll-Field-Jackiw result is

        β  =  (c_ψ / 2 M_P) · Δψ

   and with the DFD anomaly identification c_ψ/M_P = α/(π M_P) this gives

        **β = (α / 2π) · Δψ  ≈  0.018°  for Δψ = 0.27**

   which is a factor ~π² ≈ 10 smaller than H1-5 claims.
3. **Route 1 as written does NOT reproduce the observed ~0.3° birefringence** unless either (a) DFD's ψ-photon coupling is enhanced by ~π² over the naive anomaly value, or (b) Δψ is much larger than 0.27, or (c) the (π/2) prefactor is justified by a ψ-screen enhancement not yet shown.
4. **Route 1 requires a derivation of the enhanced prefactor** before it can be claimed as a DFD prediction. Without that, the natural DFD prediction is β ≈ 0.02°, which is inconsistent with current CMB birefringence measurements at >2σ.

**Recommendation:** Reclassify Route 1 from "prediction matching observation" to "conditional prediction pending derivation of O(π²) enhancement." The π/2 prefactor needs a first-principles ψ-screen loop calculation, not just dimensional substitution.

---

## 9. Parametric Summary Table

| Quantity | Symbol | Value |
|---|---|---|
| Fine structure | α | 1/137.036 |
| ψ excursion | Δψ(z_rec) | 0.27 (DFD input) |
| CFJ coefficient | f_CFJ | 1/2 |
| DFD anomaly coupling | c_ψ/M_P | α / π (conv. A) |
| Correct β | (α/2π) Δψ | 3.14×10⁻⁴ rad = 0.0180° |
| H1-5 claimed β | (π/2) α Δψ | 3.09×10⁻³ rad = 0.177° |
| Ratio (H1-5 / correct) | — | π² ≈ 9.87 |
| Observed β_CMB | — | ~0.30° ± 0.11° |

**The π² discrepancy is the central issue that Route 1 must resolve.**
