# H11: Planck Mass Convention Audit (Issue #11)

**Date:** 2026-04-06
**Scope:** v3.3 main paper (`Density_Field_Dynamics__A_Complete_Unified_Theory__v3_3/`) vs. χ-field paper (`v34_research/chi_field_paper_FINAL.tex` and `chi_field_supplementary_FINAL.tex`).
**Question:** Do the two papers use compatible Planck-mass conventions, and does every formula give the right number?

## 0. Definitions

- `M_P  = √(ħc/G)      = 1.2209 × 10^19 GeV`  (full Planck mass; v3.3 default)
- `M̄_P = M_P/√(8π)     = 2.4353 × 10^18 GeV`  (reduced Planck mass; χ sector default)
- Ratio: `M_P / M̄_P = √(8π) ≈ 5.01325`
- `α^-1 = 137.036`, so `α^8 = 8.0412 × 10^-18`, `√(2π) = 2.5066`.

The χ paper declares the convention explicitly at lines 42–43 and 157–161 of `chi_field_paper_FINAL.tex`:

```
\newcommand{\MP}{M_{\mathrm{P}}}
\newcommand{\MPbar}{\bar{M}_{\mathrm{P}}}
...
M_P  = sqrt(hbar c/G) = 1.221e19 GeV  (full)
Mbar_P = M_P/sqrt(8pi) = 2.435e18 GeV (reduced)
"DFD v3.3 uses M_P uniformly; the chi sector naturally
 employs Mbar_P from the f_a = 1/sqrt(Vol) normalization."
```

So the two conventions are **knowingly mixed**. The audit checks whether each formula is dimensionally and numerically correct in whichever convention it is written in, and provides the equivalent form in the other.

## 1. Per-formula audit

Both observational values and the two-convention forms are listed. "Source" refers to the .tex file(s) where the formula appears.

### 1.1 Poisson / modified-Poisson equation

- Form used: `∇·[μ ∇ψ] = -(8πG/c²) ρ`
- **v3.3:** appendix_V_extended_phenom.tex:24,266,271,276; section_conclusions.tex:27; section_ppn.tex:88; section_strong_fields.tex:18; section_openproblems.tex:33; section_wellposedness.tex:77,212; section_cosmology.tex:711.
- **χ paper:** line 118 (same form).
- **Convention:** This is `8πG`, i.e. the **unreduced** form. It is equivalent to writing `(1/M̄_P²)` with `ρ/c²` on the RHS via `8πG = 1/(c² M̄_P² · ... )` in natural units. Both papers use the 8πG form — consistent.
- **Status:** ✅ Consistent. No change needed.

### 1.2 Friedmann / critical density

- `ρ_crit = 3H_0²/(8πG)` (v3.3 section_G_derivation.tex:79–81).
- Reduced form `H² = ρ/(3 M̄_P²)` is not written explicitly in either paper.
- **Status:** ✅ Consistent (only unreduced form appears).

### 1.3 (H_0/M_P)² = α^57  —  vacuum-energy / Λ relation

- **v3.3:** section_openproblems.tex:193,320; section_conclusions.tex:284; section_G_derivation.tex:47–49, 106, 222; appendix_O_alpha57.tex.
- **χ paper:** lines 394–395, 455, 552.
- Both write `(H_0/M_P)² = α^57`. Uses full `M_P`.
- In M̄_P form: `(H_0/M̄_P)² = 8π · α^57`. The papers never state it this way — not needed; using `M_P` is simpler and consistent.
- Numerical: `H_0 = M_P · α^28.5 ≈ 1.54 × 10^-42 GeV ≈ 2.33 × 10^-18 s^-1 ≈ 72 km/s/Mpc`. ✅

### 1.4 Majorana scale  M_R = M_P α^3

- **v3.3:** section_conclusions.tex:286; section_openproblems.tex:294,322; section_quantum.tex (implicitly via α-tower).
- **χ paper:** lines 395, 455, 555, 613.
- Both use full `M_P`. Numerical: `M_R = 4.74 × 10^12 GeV`.
- Equivalent in M̄_P: `M_R = √(8π) · M̄_P · α^3 = 9.46 × 10^11 × √(8π) ≈ 4.74 × 10^12 GeV`. ✅
- **Status:** ✅ Consistent, both papers use M_P form.

### 1.5 Higgs VEV  v = M_P α^8 √(2π)

- **v3.3:** section_conclusions.tex:79,258,293; section_openproblems.tex:94,292,328; section_quantum.tex:404–411,722,752,773; section_introduction.tex:274,399; section_G_derivation.tex:222; section_alpha_relations.tex:363; appendix_K.tex:879.
- **χ paper:** lines 459, 558.
- **Computation (full M_P):** `1.2209e19 × 8.0412e-18 × 2.5066 = 246.089 GeV`. ✅ matches the 246.0892 GeV value quoted in both papers.
- **Note on the task brief's arithmetic:** the task prompt computed `(1/137)^8 = 1.56 × 10^-17`, which is incorrect. The correct value is `(1/137.036)^8 = 8.04 × 10^-18`, roughly half of the prompt's number. With the correct α^8 the formula gives 246 GeV with `M_P`, and gives `49.09 GeV` with `M̄_P`. So **the M_P form is the correct one**, as both papers already write. **There is no inconsistency.**
- **Equivalent M̄_P form:** `v = √(8π) · M̄_P · α^8 · √(2π) = √(16 π²) · M̄_P · α^8 = 4π · M̄_P · α^8 = 246.09 GeV`. The reduced-Planck form of this relation is the clean `v = 4π · M̄_P · α^8` — worth noting as an equivalent-but-not-written form.
- **Status:** ✅ Numerically correct in both papers; convention uniformly M_P.

### 1.6 Axion decay constant  f_a = M̄_P α^5

- **χ paper:** lines 461, 561. `f_a/M̄_P = α^5 = 5.04 × 10^7 GeV`.
- **v3.3:** no corresponding f_a formula (this is new in the χ sector; the v3.3 paper has no axion, relying on Theorem strong_cp_all_loops).
- **Computation:** `M̄_P · α^5 = 2.435e18 × 2.011e-11 = 5.040 × 10^7 GeV`. ✅
- **Why M̄_P here, not M_P?** The χ paper derives this from `f_a² = 1/Vol(M_7)` after the volume factor strips out √(8π) (line 311–320). The natural answer is in the reduced convention.
- **Equivalent M_P form:** `f_a = M_P · α^5 / √(8π) = 2.526e8 / 5.013 = 5.04 × 10^7 GeV`. ✅
- **Status:** ✅ Numerically correct. Convention is M̄_P. No v3.3 counterpart to conflict with.

### 1.7 χ mass  m_χ = √158 · M̄_P · α^11

- **χ paper:** lines 490–522, 564.
- **Computation:** `sqrt(158) × 2.435e18 × (1/137.036)^11 = 12.570 × 2.435e18 × 3.1257e-24 = 9.565 × 10^-5 GeV ≈ 95.7 μeV`. ✅
- **Convention-equivalent relation stated in the paper (line 520–522):** `m_χ ≈ √(2π) · M_P · α^11`, because `√158 · M̄_P ≈ √(2π) · M_P`.
- **Numerical cross-check:** `√158 · M̄_P = 12.570 × 2.435e18 = 3.060e19`; `√(2π) · M_P = 2.5066 × 1.2209e19 = 3.0605e19`. Ratio = **1.000273** (agrees to 0.03%, as claimed in the paper). ✅
- **Why the agreement?** `√(2π) · √(8π) = √(16π²) = 4π ≈ 12.566 ≈ √158 = 12.570`. Check: `(4π)² = 16π² ≈ 157.914 ≈ 158`. So `√158 ≈ 4π`, and the "√158" in the paper is really `4π` dressed up from the origin of the potential; the 0.03% discrepancy is just `158/(16π²) - 1 = 5.4e-4`.
- **Status:** ✅ Numerically correct. The two forms are equivalent to 0.03%. The paper correctly flags this.

### 1.8 Λ = M̄_P α^8  (χ potential energy scale)

- **χ paper:** lines 490–492 ("Λ = M̄_P α^8, the same α^8 rung as the Higgs VEV").
- **Internal consistency check with the Higgs:** `Λ (χ-paper) = M̄_P α^8 = 2.435e18 × 8.04e-18 = 19.58 GeV`. The Higgs VEV is `246.09 GeV` which equals `4π × Λ`.
- So the χ paper places Λ ("the potential energy scale") at `v/(4π) ≈ 19.6 GeV`, not at `v = 246` GeV itself. This is a **meaningful convention choice, not an error**: the χ sector uses the reduced mass, so its natural α^8 rung is `M̄_P α^8 = Λ`, and the full Higgs VEV sits a factor of 4π above because the microsector formula is written in the unreduced convention.
- See-saw consistency: `Λ²/f_a = (M̄_P α^8)²/(M̄_P α^5) = M̄_P α^11`, as stated in line 516–518. ✅

### 1.9 ΛQCD = M_P α^(19/2)

- **v3.3:** DFD_Unified_Review.tex:168; section_conclusions.tex:77; appendix_K.tex:628.
- **χ paper:** not used.
- Full M_P form. `1.2209e19 × α^9.5 ≈ 61 MeV`. ✅ Quoted as 61.20 MeV in v3.3. (Not touched by the convention issue.)

### 1.10 ν mass term  m_3 = (14/13) π M_P α^14

- **v3.3:** DFD_Unified_Review.tex:209.
- Full M_P form, no conflict.

## 2. Master conversion table

For every α-rung formula in the two papers, the table lists the "native" convention (as written) and the equivalent expression in the other convention. All values use `M_P = 1.2209 × 10^19 GeV`, `M̄_P = 2.4353 × 10^18 GeV`, `α = 1/137.036`.

| Quantity      | Written as (paper)                       | Native conv. | Equivalent form                                   | Numerical value         | Source                                              |
|---------------|------------------------------------------|--------------|---------------------------------------------------|-------------------------|-----------------------------------------------------|
| Λ (cosmology) | `(H_0/M_P)² = α^57`                      | M_P          | `(H_0/M̄_P)² = 8π α^57`                           | H_0 ≈ 1.5e-42 GeV       | v3.3 sec_G_derivation; χ L394                       |
| M_R           | `M_R = M_P α^3`                          | M_P          | `M_R = √(8π) M̄_P α^3`                            | 4.74 × 10^12 GeV        | v3.3 sec_openproblems; χ L455,555                   |
| ΛQCD          | `Λ_QCD = M_P α^(19/2)`                   | M_P          | `Λ_QCD = √(8π) M̄_P α^(19/2)`                     | 61.2 MeV                | v3.3 appendix_K, sec_conclusions                    |
| v             | `v = M_P α^8 √(2π)`                      | M_P          | `v = 4π M̄_P α^8`  (since √(2π)·√(8π)=4π)         | **246.089 GeV**         | v3.3 sec_quantum; χ L459,558                        |
| Λ_χ           | `Λ = M̄_P α^8`                           | M̄_P         | `Λ = M_P α^8 / √(8π) = v/(4π)`                    | 19.58 GeV               | χ L491                                              |
| f_a           | `f_a = M̄_P α^5`                         | M̄_P         | `f_a = M_P α^5 / √(8π)`                           | 5.04 × 10^7 GeV         | χ L461,561                                          |
| m_χ           | `m_χ = √158 · M̄_P α^11`                 | M̄_P         | `m_χ ≈ √(2π) · M_P α^11` (0.03% higher)           | 9.57 × 10^-5 GeV ≈ 96 μeV | χ L512,564                                          |
| m_3 (ν)       | `m_3 = (14/13)π M_P α^14`                | M_P          | `(14/13)π √(8π) M̄_P α^14`                        | ~0.05 eV                | v3.3 DFD_Unified_Review L209                        |

## 3. Rules for consistency

1. **Low-α rungs (N ≤ 9.5) = M_P convention.** Every formula v3.3 writes (H_0, M_R, ΛQCD, v, m_ν) is in full `M_P`. The χ paper reproduces each of these in the same M_P form — no conflict.
2. **χ-sector rungs (N = 5, 8, 11) = M̄_P convention.** Only the χ paper introduces f_a, Λ_χ, m_χ. It uses M̄_P because the volume-of-M_7 derivation yields the reduced form natively.
3. **Bridge identity.** `√158 ≈ 4π`, so the α^11 rung can be written with `√(2π) · M_P` **or** `√158 · M̄_P`; they agree to 0.03% which is below the current observational accuracy on m_χ.
4. **Bridge identity for the α^8 rung.** `v = M_P α^8 √(2π) = 4π M̄_P α^8`, exact (no √158-type slop). The factor of `4π` between the Higgs v and the χ potential scale Λ is mechanical, not a discrepancy.

## 4. Inconsistencies found

**None that produce a wrong observational number.** Every formula reproduces the correct value in its stated convention, and the bridge identities (Section 3) make each pair exactly or ≤0.03%-equivalent to its counterpart in the other convention.

What is *stylistically* inconsistent — and worth tidying for publication — is:

1. **Mixed conventions inside one paper.** The χ paper uses M_P for the shared-with-v3.3 rungs (H_0, M_R, v) and M̄_P for the χ-native rungs (f_a, Λ_χ, m_χ). This is legitimate but the reader has to track it. **Recommendation:** add a one-line "conversion identities" box next to the master dictionary table (Table at line 552–564 of `chi_field_paper_FINAL.tex`) listing:
   - `v = M_P α^8 √(2π) = 4π M̄_P α^8`
   - `f_a = M̄_P α^5 = M_P α^5 / √(8π)`
   - `m_χ = √158 M̄_P α^11 ≈ √(2π) M_P α^11` (0.03%)
2. **The v3.3 paper never mentions M̄_P.** That's fine as long as the χ-paper supplement clearly declares the convention switch (which it does at lines 158–161). No code change to v3.3 is required — just cross-reference the χ-paper glossary.

## 5. Answer to the task prompt's arithmetic puzzle

The task prompt wrote:

> `(1/137)^8 = 1.56×10^-17`  ⇒ `M_P × (1/137)^8 = 191 GeV`  ⇒ `× √(2π) = 479 GeV`

This is a miscalculation. The correct value is `(1/137.036)^8 = 8.0412×10^-18`, exactly half of 1.56e-17. Redoing the arithmetic:

- `M_P × α^8 × √(2π) = 1.2209e19 × 8.0412e-18 × 2.5066 = 246.09 GeV` ✅

So **there is no missing factor and no "off" formulation**. The Higgs VEV formula in v3.3 and the χ paper is exactly right as written, in the M_P convention. The task prompt's worry "we get 479 GeV, that's wrong" came from `α^8` being computed as `(α^4)²` where `α^4` was off by √2.

## 6. Recommendations (for the papers, not this audit)

1. **No formula changes needed.** Every Planck-mass formula is numerically correct in the convention it is written in.
2. **Add conversion footnote** in the χ paper's master table (around line 552–564 of `chi_field_paper_FINAL.tex`) giving the three bridge identities in Section 3 above, so readers see explicitly that `v = 4π M̄_P α^8` and `m_χ ≈ √(2π) M_P α^11 ≈ √158 M̄_P α^11`.
3. **Add one line to v3.3 `section_quantum.tex`** near the `v = M_P α^8 √(2π)` box (line 404) noting that in the reduced-Planck convention this is `v = 4π M̄_P α^8`, which cross-references the χ paper.
4. **Do NOT rewrite v3.3 in M̄_P.** The full Planck mass is simpler for the v3.3 exponents (α^57, α^19, α^14, α^8, α^3) because those rungs all drop the awkward √(8π) factor. Leave v3.3 as-is.

## 7. Bottom line

Issue #11 is a **labeling/stylistic** inconsistency, not a numerical one. No formula in either paper gives the wrong observational value. The χ paper already declares the mixed convention explicitly and provides a one-line equivalence statement for m_χ. The recommended fix is purely cosmetic: a small conversion table as in Section 2 above, inserted into the χ paper's dictionary table and cross-referenced from v3.3's Higgs-VEV box.

**Verdict:** ✅ Closed-with-cosmetic-fix. No derivations to redo.
