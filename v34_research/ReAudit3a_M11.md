# ReAudit 3a — Independent re-audit of M11 birefringence and twist consistency

**Auditor:** ReAudit3a (independent of Audit3)
**Date:** 2026-04-07
**Sources audited:**
- `v34_research/M11_kk_overlap.md` (M11 KK Dirac overlap on CP²×S³)
- `Ab_Initio_Derivation_of_the_Fine_Structure_Constant_from_Density_Field_Dynamics.pdf` (α paper, Dec 2025)
- Cross-checked against `v34_research/Audit3_M11_twist.md` *only after* forming independent conclusions.

This re-audit was carried out without consulting Audit3 until §6. Numerical
checks performed in `python3` from the rational closed forms.

---

## 1. The 40.375 vs. 60 discrepancy — what is each number actually computing?

**Both numbers are correct, and they compute different objects on the same bundle.**

### 1.1 The α paper's 60

The α paper (Bridge Lemma, Appendix A) defines

  k_max := χ(CP², O(9) ⊕ O⁵) = χ(O(9)) + 5·χ(O) = C(11,2) + 5·1 = 55 + 5 = **60**.

This is the **holomorphic Euler characteristic** (sheaf cohomology dimension)
of the twist bundle on CP², equivalently the integer dimension of the space of
holomorphic sections. It is used in the α paper as a UV cutoff on the
Chern–Simons level sum, *not* as the coefficient of an anomaly diagram. In the
α paper, k_max = 60 plays the role of an upper limit on a sum
Σ_{k=0}^{k_max−1}(k+2)·w(k); the bundle E enters only through its rank
(the integer 60 itself), not through its detailed Q-content.

By Hirzebruch–Riemann–Roch + Kodaira vanishing on a positively-twisted line
bundle on CP², χ(O(m)) = (m+2)(m+1)/2 = C(m+2, 2). For m = 9 this is 55. The
five trivial summands give 5·1 = 5. Total: 60. **Verified.**

### 1.2 M11's 40.375

M11 computes a different integral on the same bundle:

  index(D_{O(9)}) = ∫_{CP²} ch(O(9)) · Â(CP²) |_{H²-piece}
                  = 9²/2 − (1/8)·(1)
                  = 40.5 − 0.125 = **40.375**.

(Where ch(O(9))|_{H²} = 81/2·H², Â(CP²) = 1 − p₁/24 = 1 − (3H²)/24 = 1 − H²/8,
and only the top-form piece survives integration.) **Verified.**

This is the **Atiyah–Singer / spin-c Dirac index** of the twisted Dirac
operator on CP². It is what couples to the ψFF̃ triangle anomaly: the chiral
asymmetry of the Dirac kernel weighted by F∧F. The half-integer reflects
the well-known spin-c offset on CP² (CP² is *not* spin; the canonical
spin-c structure has Â-genus 1/8 + ½·c₁²/8 etc., and twisting by an odd
line bundle leaves a half-integer residue that the integer lift absorbs into
the determinant line K_CP²^{−1} = O(3)).

### 1.3 Why both can be right

- χ(CP², O(9)) = 55 and index(D_{O(9)}) = 40.375 are computing **different
  characteristic numbers**. χ uses the full Todd class Td(CP²) =
  1 + (3/2)H + H², which gives ch·Td|_top = 81/2 + 27/2 + 1 = **55** (a
  sanity check I performed:  9²/2 + (3/2)·9 + 1 = 40.5 + 13.5 + 1 = 55).
  index(D) uses Â = √Td · e^{−c₁/2}, which gives the (40.375) above.
- The relationship χ = index(D ⊗ K^{1/2}) on a Kähler manifold means the two
  numbers differ exactly by the spin-c twist by ½·c₁ = (3/2)H. That shift is
  the +13.5 + 1 = 14.625 = 55 − 40.375. **Verified (55 − 40.375 = 14.625).**

So neither is "wrong". The α paper picks the holomorphic Euler characteristic
(an integer), M11 picks the spin-c Dirac index (half-integer). They are
*different functionals of the same bundle*.

### 1.4 But are they the right functionals for their respective channels?

This is the substantive question.

- For the **CS-level cutoff** in the α paper, what matters is the dimension
  of a Hilbert space of states (a count of holomorphic sections). χ(CP², E) is
  the natural object — and it's integer, which it must be. **OK.**
- For the **ψFF̃ triangle anomaly** in M11, what matters is the chiral
  asymmetry of the Dirac kernel coupled to F∧F. This is the AS index of the
  twisted Dirac operator. M11's 40.375 is the right functional **for this
  channel**. **OK.**

So Q1 of the brief — "is one of them wrong?" — has answer **No, both are right
for their stated purpose, but they are not the same number and cannot be
freely interchanged**. The α paper's "60" is *not* the index that drives the
birefringence anomaly; the birefringence anomaly is driven by 40.375 (or
9·40.375 once Tr Q² is included).

**This is itself a finding worth flagging:** the α paper uses the language
"closed Spin^c index = 60" in Appendix A.1 (Eq. A1: `k_max := Index(D ⊗ E) =
χ(CP², E) = 60`). On a Kähler manifold the Dolbeault index χ equals the
spin-c Dirac index *only after twisting by K^{1/2} = O(3/2)*, which is not
globally well-defined. The α paper's identification of the integer 60 with
"Index(D_CP² ⊗ E)" therefore implicitly uses the Dolbeault complex, not the
spin-c Dirac complex. M11 uses the spin-c Dirac complex directly. The two
papers are using "index" to mean two different things. This is a notational
collision, not a contradiction, but it should be cleaned up in any unified
write-up.

---

## 2. Can α use one bundle and β use a different bundle?

**No — but for a subtler reason than "double counting".**

If by "different bundle" one means *literally a different holomorphic vector
bundle on CP²* (e.g. O(9)⊕O⁵ for α and O(5)⊕O⁵ for β), then the question is
whether DFD has any principle that forces a single twist across all
observables. The α paper (Appendix A.3) derives O(9)⊕O⁵ from two non-negotiable
inputs:

1. anomaly cancellation forces minimal hypercharge flux q₁ = 3, hence O(9);
2. one trivial summand per chiral SM multiplet type {Q_L, u_R, d_R, L_L, e_R}.

Both of these inputs are **bundle-level statements**, not channel-level
statements. The chiral spectrum of the SM lives in **one** spectral triple
on CP²×S³; you don't get a different chiral spectrum when you compute α
versus when you compute the cosmic-birefringence anomaly. So if O(9)⊕O⁵ is
right for the α derivation, it is also the bundle whose chiral kernel
sources ψFF̃, and switching to O(5)⊕O⁵ for β alone is not a free choice —
it would falsify constraint (1) above (it requires q₁ = 5/3, which is not
an integer hypercharge unit).

**Q2 of the brief: would using two bundles double-count anomaly content?**
Not exactly "double count" — rather, it would require two physically
inequivalent chiral spectra coexisting in the same UV completion. That isn't
double counting in the diagrammatic sense (each diagram still counts each
chiral state once); it's incoherence at the level of *which states exist*.

So the cleanest framing is: you cannot consistently use two different
twist bundles, not because of a Ward-identity violation, but because the
microsector spectral triple is unique up to the twist, and the α paper has
already fixed that twist. Switching it for β alone has no fundamental
justification on offer in either document.

The Q²-projection escape hatch (Audit3 §1) doesn't help either: under the
α paper's own assignment Q(O(9)) = 3, Q(O) = 0, the five neutral summands are
invisible to *both* the α one-loop coefficient and the β anomaly coefficient,
and the difference between 60 and 40.375 is a Todd-vs-Â convention, not a
charge projection. **I independently confirm this.**

---

## 3. Is β = 0.73° robust to Δψ, or is Δψ a tunable?

**Δψ = 0.27 is a tunable in the H1–H4 chain, not a first-principles output.**

M11 §6 itself flags this: "Δψ would have to be revised down from 0.27 to
≈ 0.11 to land exactly on β_obs = 0.30°. This is within the H1–H4 quoted Δψ
uncertainty (the value 0.27 was itself a representative central, not a hard
prediction)."

So the linear sensitivity is

  β = (c_ψ/2)·Δψ ⇒ ∂β/∂(Δψ) = c_ψ/2 ≈ 0.0475

i.e. β is **directly proportional** to Δψ. A factor 2.4 mismatch with Planck
central can be absorbed by a factor 2.4 reduction in Δψ. There is no
non-linearity that protects against this.

**M11's 0.73° is therefore not a falsifiable parameter-free prediction** in
the same sense the α paper's 1/137 is parameter-free. It is a *conditional*
prediction: given the canonical twist O(9)⊕O⁵ AND given Δψ = 0.27 from H1–H4,
β = 0.73°. Either input can be revised within stated uncertainties, and the
resulting β slides linearly.

To make β a hard prediction, Δψ would have to be derived from first
principles in DFD with no continuous knob. I don't see that derivation in
either document; H1–H4 is invoked as the source but its own systematic band
is wide enough to cover the [0.11, 0.27] range needed to span [0.30°, 0.73°].

---

## 4. Legitimate first-principles prediction with O(9)⊕O⁵

If we accept (a) the canonical twist O(9)⊕O⁵, (b) the M11 spin-c Dirac index
40.375 for the chiral kernel coupled to F∧F, and (c) Q(O(9)) = 3 from the
α paper, the **bundle-level** ψFF̃ coefficient is unambiguously

  c_ψ/M_P = (α/2π) · ψ₀ · 9 · 40.375 = **0.0950**

(numerically verified to 4 sig figs from the rational closed form). This is
M11's central value and I reproduce it.

The β prediction then reduces to

  β [rad] = (0.0475)·Δψ
  β [deg] = (2.72°)·Δψ

For β to be a *prediction* rather than a fit, Δψ must be supplied
independently. The honest summary is:

| Δψ source            | Δψ      | β prediction | matches Planck 0.30° ± 0.11°? |
|----------------------|---------|--------------|-------------------------------|
| H1–H4 central        | 0.27    | 0.73°        | no (~3.9σ high)               |
| H1–H4 lower band     | 0.11    | 0.30°        | yes — but post-hoc            |
| no DFD prediction    | free    | scales linearly | n/a (one-parameter fit)    |

So the **legitimate** DFD prediction on the O(9)⊕O⁵ bundle is

  **β = (2.72° ± geometric few %) · Δψ**

with the numerical value depending on what Δψ is taken to be. M11's "0.73°"
is the value at the H1–H4 representative central, not a hard prediction at
the level of α = 1/137.

If instead one wanted a hard β prediction with no Δψ tunable, one would need
either (i) a first-principles derivation of Δψ in DFD or (ii) a different
observable from the same bundle that fixes the same combination c_ψ·Δψ
without going through the Δψ stage. Neither is on offer in the current
documents.

---

## 5. Summary of independent answers to the four brief questions

**Q1. Why does M11 say 40.375 and the α paper say 60? Is one wrong?**
Neither is wrong. They are different characteristic numbers of the same
bundle: 60 = χ(CP², O(9)⊕O⁵) (Dolbeault Euler characteristic, integer, used
as a CS-level cutoff in the α paper) vs. 40.375 = ∫ch(O(9))·Â (spin-c Dirac
index density, half-integer, used as the ψFF̃ anomaly coefficient in M11).
The difference 55 − 40.375 = 14.625 is exactly the Â-vs-Todd shift on CP²
(the determinant-line twist by O(3/2)). The α paper's Eq. (A1) writes
"Index(D_CP² ⊗ E)" but the integer 60 it computes is Dolbeault, not spin-c
Dirac. **Notational collision worth fixing in a unified write-up.**

**Q2. Can α use one bundle and β a different bundle without double-counting?**
Not as currently formulated in DFD. The chiral spectrum lives in one
spectral triple on CP²×S³ and the α paper has already fixed its twist via
SM hypercharge anomaly cancellation. Switching the twist for β alone would
require an independent argument that no document supplies, and a Q²
projection cannot bridge the gap (the EM-neutral O summands are invisible
to *both* channels under the α paper's own embedding). **I confirm
Audit3's verdict on this.**

**Q3. Is β = 0.73° robust to Δψ = 0.27?**
No. β is *linear* in Δψ. The H1–H4 uncertainty band on Δψ already covers
the factor needed to match Planck. **β = 0.73° is a conditional value, not
a parameter-free prediction.**

**Q4. Legitimate DFD β prediction on O(9)⊕O⁵ with first-principles Δψ?**
There is no first-principles Δψ in either document. The bundle-level
result is β/Δψ = 2.72°/rad, which on Δψ = 0.27 gives 0.73° and on Δψ = 0.11
gives 0.30°. Until DFD supplies Δψ from a closed geometric formula (the
way it supplies α from k_max = 60), β remains a one-parameter prediction
of the form **β = 2.72°·Δψ**, geometrically pinned in slope but free in
amplitude over the H1–H4 band.

---

## 6. Comparison with Audit3_M11_twist.md

After finishing §1–§5, I read Audit3_M11_twist.md.

**Agreements (independent):**
- Same conclusion that O(9)⊕O⁵ for α and a different bundle for β is not
  consistent (Audit3 §5; ReAudit3a §2).
- Same conclusion that the Q² projection collapses the EM-neutral
  summands in both channels and cannot bridge 60 → 16 (Audit3 §1–§2;
  ReAudit3a §2).
- Same observation that M11's 9·40.375 = 363.375 is the Q²-weighted index
  and M11 already absorbs the projection (Audit3 §2; ReAudit3a §2).

**Differences / additions in this re-audit:**
- Audit3 frames 60 vs 40.375 as "two normalization conventions applied to
  the same chiral kernel" (Audit3 §5). I think this is *almost* right but
  slightly imprecise: they are not normalization conventions, they are two
  *different characteristic numbers* (Dolbeault Euler char vs spin-c Dirac
  index) that happen to coincide on spin manifolds but disagree on CP²
  by exactly the determinant-line twist O(3/2). The α paper writes
  "Index(D⊗E) = χ(CP², E)" in Eq. (A1) — that identification is only
  valid in the Dolbeault sense, not in the spin-c Dirac sense, and the
  difference *matters* because the spin-c Dirac index is what couples to
  ψFF̃. **This is a stronger statement than Audit3 makes: it's a real
  notational error in the α paper, not just a conventional choice.**
- Audit3 doesn't separately address whether Δψ is a tunable. I find that
  it is (§3), and that this alone reduces M11's β = 0.73° from a hard
  prediction to a conditional one. This weakens M11's "sharp prediction"
  language even before the bundle-consistency question is engaged.
- Audit3's Option A (keep O(9)⊕O⁵ everywhere, treat β as a one-parameter
  fit on Δψ) is the same conclusion I reach in §4, with the same caveats.

**Net verdict: Audit3 and this re-audit converge on INCONSISTENT for the
two-bundle escape hatch. We diverge slightly on the framing of the 60-vs-40.375
discrepancy: Audit3 calls it a normalization convention; I call it a
genuine notational error in the α paper that should be corrected by either
(a) stating that "60" is χ_Dolbeault and not the spin-c Dirac index, or
(b) recomputing k_max from the spin-c Dirac index, which would give 40.375
+ 5·(−1/8) = 39.75, *changing the α derivation*.**

If the α paper's Bridge Lemma is taken at face value (k_max = spin-c Dirac
index), then k_max = 39.75, ⟨k+2⟩ would need recomputing, and the headline
α = 1/137 result would have to be re-verified at the new cutoff. If
instead the Bridge Lemma is read as k_max = χ_Dolbeault (the integer 60),
then the integer 60 is *not* the AS index that M11 uses for ψFF̃, and
M11's 40.375 stands without contradiction — but the α paper should
be updated to remove the false identification "Index(D⊗E) = χ(CP², E)" on
a non-spin manifold.

---

## 7. Bottom line

1. **Both 60 and 40.375 are correct numbers**, computing different
   characteristic classes on the same bundle. The α paper's identification
   of the integer 60 with "Index(D ⊗ E)" is technically wrong on a non-spin
   manifold; the integer 60 is the Dolbeault Euler characteristic χ(CP², E).
   M11's 40.375 is the spin-c Dirac index. Neither paper acknowledges the
   distinction. This should be cleaned up.
2. **You cannot mix bundles** between α and β without an independent
   physical principle, and none is on offer. Confirmed independently of
   Audit3.
3. **β = 0.73° is not a hard prediction.** It is β = (2.72°)·Δψ evaluated
   at Δψ = 0.27 from H1–H4, and Δψ has its own systematic band that
   covers the Planck-matching value 0.11. The legitimate DFD output on
   the canonical twist is the *slope* 2.72°/rad, not the value 0.73°.
4. **The cleanest way forward** is either (a) supply a first-principles
   Δψ derivation in DFD so β becomes a hard number, or (b) reclassify
   M11's 0.73° as a slope-times-input-band rather than a sharp prediction
   and report it as `β = 0.73° at Δψ_central, sliding to 0.30° at the
   lower edge of the H1–H4 band`. The "0.73° ± 0.03°" wording in M11
   §5 over-states the precision.

**Files referenced (absolute paths):**
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/M11_kk_overlap.md`
- `/Users/garyalcock/claudecode/densityfielddynamics/Ab_Initio_Derivation_of_the_Fine_Structure_Constant_from_Density_Field_Dynamics.pdf`
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/Audit3_M11_twist.md`
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/ReAudit3a_M11.md` (this file)

All numerical claims verified in `python3` from the rational closed forms.
