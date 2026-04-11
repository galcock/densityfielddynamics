# ReAudit 2b: Independent Re-Audit of M9 (16/3 via 't Hooft anomaly matching)

**Auditor:** ReAudit2b (independent; M9 read first, prior Audit2_M9_chs.md and arXiv:2410.22412 consulted only after independent computation)
**Date:** 2026-04-07
**Target:** `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/M9_thooft_ratio.md`
**Question:** Is there a legitimate way to obtain Ω_χ/Ω_b = 16/3 as a *single* ratio of 4D 't Hooft anomaly coefficients on a *common* gauge probe, with the DFD field content (SO(10) spinor 16 for χ + 3-gen SM for baryons)?

---

## 0. One-line verdict

**No.** There is no gauge probe under which the 4D 't Hooft anomaly ratio Tr[Q_χ T_a T_b] / Tr[Q_B T_a T_b] equals 16/3 on the stated DFD field content. Direct enumeration over all SM gauge factors plus gravity yields the ratios {4, 8, 0/0, 0/0} (SU(2)_L², gravity², SU(3)_c², U(1)_Y² respectively, with the last two being 0/0 because Q_B is gauge-anomaly-free against them). The value 16/3 appears in M9 only after dividing by an ad-hoc factor of N_gen² = 9, which is *not* a standard descent normalization in any 4D anomaly-matching framework. Moreover M9's anchor citation (arXiv:2410.22412) is misattributed and uses a completely different mechanism (relaxation via β-function shifts, not 't Hooft matching).

---

## 1. Independent 4D anomaly enumeration

I take the DFD UV field content exactly as M9 specifies it: per generation, the standard 15 SM Weyl fermions plus ν_R^c, with Q_χ = +1 democratically on every Weyl mode (the "16 of SO(10)" assignment) and Q_B = +1/3 on every quark Weyl, 0 on leptons. N_gen = 3.

The 4D 't Hooft anomaly coefficient of a global U(1) current J_a against a non-Abelian gauge factor G is

  c_{a, GG} = Σ_{Weyl f} Q_a(f) · T(R_f),     (G non-Abelian)

with T(fund SU(N)) = 1/2, T(adj) = N. Against U(1)_Y² it is Σ Q_a Y_f², and against gravity² it is Σ Q_a (no rep weight). I compute all four standard probes per generation, then multiply by N_gen, then form the ratio.

### 1a. SU(2)_L²

Doublets per generation: Q_L (3 colors → 3 Weyl doublets) and L_L (1 doublet). T(2) = 1/2 per Weyl doublet.

- c_{χ, SU(2)²}^{(gen)} = (3 + 1) · (+1) · (1/2) = 2
- c_{B, SU(2)²}^{(gen)} = 3 · (+1/3) · (1/2) + 1 · 0 · (1/2) = 1/2

Times N_gen = 3:

- c_{χ, SU(2)²} = 6
- c_{B, SU(2)²} = 3/2
- **Ratio = 6 / (3/2) = 4.**

### 1b. SU(3)_c²

Color triplets per generation: Q_L (2 SU(2) members → 2 Weyl triplets), u_R^c (1), d_R^c (1). T(3) = 1/2.

- c_{χ, SU(3)²}^{(gen)} = (2 + 1 + 1) · (+1) · (1/2) = 2
- c_{B, SU(3)²}^{(gen)} = 2 · (+1/3) · (1/2) + 1 · (−1/3) · (1/2) + 1 · (−1/3) · (1/2) = 1/3 − 1/6 − 1/6 = 0

Times N_gen = 3:

- c_{χ, SU(3)²} = 6
- c_{B, SU(3)²} = 0
- **Ratio = 6 / 0 — ill-defined; U(1)_B is not anomalous against SU(3)_c² (vector-like).**

### 1c. U(1)_Y²

Standard SM hypercharges (Y normalized so Q_em = T_3 + Y): Q_L: +1/6 (×3 colors ×2 SU(2)), u_R^c: −2/3 (×3), d_R^c: +1/3 (×3), L_L: −1/2 (×2), e_R^c: +1, ν_R^c: 0.

Σ Y² per generation = 6·(1/36) + 3·(4/9) + 3·(1/9) + 2·(1/4) + 1 + 0 = 1/6 + 4/3 + 1/3 + 1/2 + 1 = 10/3.

- c_{χ, YY}^{(gen)} = (+1) · 10/3 = 10/3
- c_{B, YY}^{(gen)}: Σ Q_B Y² over quark Weyls = 6·(1/3)·(1/36) + 3·(−1/3)·(4/9) + 3·(−1/3)·(1/9) = 1/18 − 4/9 − 1/9 = 1/18 − 5/9 = 1/18 − 10/18 = −9/18 = −1/2

Times N_gen = 3:

- c_{χ, YY} = 10
- c_{B, YY} = −3/2
- **Ratio = 10 / (−3/2) = −20/3.** Sign aside, magnitude is 20/3, not 16/3.

(Note: U(1)_B − Y² is in fact non-zero per generation; it is the YY combination that vanishes only when paired against U(1)_(B−L). For the bare Q_B current the YY anomaly is non-zero and gives −20/3.)

### 1d. Gravitational (RR) probe

c_{a, RR} ∝ Σ_{Weyl} Q_a (no rep weight; the 1/24 Â-genus factor cancels in any ratio).

- c_{χ, RR}^{(gen)} = 16 · (+1) = 16
- c_{B, RR}^{(gen)}: quark Weyls only: 6·(+1/3) + 3·(−1/3) + 3·(−1/3) = 2 − 1 − 1 = 0

Times N_gen = 3:

- c_{χ, RR} = 48
- c_{B, RR} = 0
- **Ratio = 48 / 0 — ill-defined; U(1)_B has no perturbative gravitational anomaly.**

(M9 in §5b correctly notes this and pivots to a "left-handed projected" Q_{B_L} that retains only Q_L. That projection is not the operator U(1)_B; it is a different current. With that ad-hoc replacement the gravitational ratio becomes 48/6 = 8, also not 16/3.)

### 1e. Summary table of 4D anomaly ratios

| Probe | c_χ | c_B | Ratio c_χ/c_B |
|---|---|---|---|
| SU(2)_L² | 6 | 3/2 | **4** |
| SU(3)_c² | 6 | 0 | undefined (B vectorlike) |
| U(1)_Y² | 10 | −3/2 | **−20/3** |
| grav² (RR) | 48 | 0 | undefined (B grav-anomaly-free) |
| grav² with B → B_L (M9's projection) | 48 | 6 | **8** |

**16/3 does not appear among any of these.** The closest numerically is the U(1)_Y² ratio of magnitude 20/3, which is wrong by 4/3. There is no 4D probe — Abelian, non-Abelian, or gravitational — on which a single ratio of 't Hooft coefficients gives 16/3.

## 2. Is the descent normalisation 1/N_gen² standard?

**No. It is ad-hoc.** Standard descent (Stora–Zumino, anomaly inflow from a (d+2)-form characteristic class) does not introduce factors of (visible-sector generation count)² in the 4D coefficient. Generation count enters anomaly coefficients additively (Σ over generations), not as an inverse-square denominator. The factor 1/N_gen² in M9 §6 is constructed expressly to convert the bare ratio 48 into the target 16/3:

  48 / 9 = 16/3.

This is arithmetic, not physics. Once you allow free re-normalisation of the χ kinetic term by an arbitrary integer, you can land on any rational target. Specifically, M9's factor "1/(N_gen²)" has no derivation in the memo; it is asserted to come from "CHS eqs. 2.10–2.12" — equations which (see §3) do not exist.

The standard CS-descent normalisation for a topological U(1) shift symmetry on a b₃ = 1 cycle is by the volume of the cycle in α′-units, which is dimensionful and drops out of dimensionless anomaly ratios. There is no place in the descent for a discrete factor of 1/N_gen².

## 3. The CHS / arXiv:2410.22412 citation is wrong

M9 attributes the 16/3 framework to "Cabrera, Harigaya, Sundrum, *Dark Matter from Anomaly Matching of a Confining Sector*, arXiv:2410.22412 (2024)." Direct fetch (and the prior audit's PDF parse) shows arXiv:2410.22412 is:

> Banerjee, Brzeminski, Hook, "Predicting the Dark Matter — Baryon Abundance Ratio" (LCTP-24-20, October 2024).

The actual paper is a *relaxation* model with a composite QCD axion. Its 16/3 is the value of an integer combination Q_N = 2N (with N = 8 the size of a confining gauge group SU(N), times 1/3 from a β-function ratio) such that the relation ρ_DM/ρ_B = 2N/(27 − 3N) reproduces 5.36. The mechanism is *β-function shifts under confinement*, not 't Hooft anomaly matching. The probe is SU(3)_c (the colour β-function), not SU(2)_L. The paper contains no factor of 1/N_gen², no SU(2)_L² descent, no SO(10) 16-spinor identification, and no anomaly-polynomial argument at all. The numerical coincidence "16/3 in their paper, 16/3 in DFD" is structural noise — the two 16/3's are computed from completely unrelated quantities. M9's "field-content identification table" in §7 maps DFD objects onto a paper that does not contain those objects.

## 4. Comparison with prior Audit2_M9_chs.md

After completing the independent computation above, I read Audit2_M9_chs.md. It reaches the same conclusions on every load-bearing point:

1. The misattribution of arXiv:2410.22412 (Audit2 §1; this report §3) — confirmed.
2. The bare SU(2)_L² ratio is 4, not 16/3 (Audit2 §3c; this report §1a) — confirmed, and M9's own §4 admits this.
3. The 1/N_gen² factor is invented (Audit2 §3b; this report §2) — confirmed; no standard descent produces it.
4. The 16 in Banerjee–Brzeminski–Hook is 2N with N = 8, not a Weyl-fermion count, so the SO(10) 16-spinor mapping is fictitious (Audit2 §3d; this report §3) — confirmed.
5. Rubric (d): numerology, not derivation — confirmed.

The two audits are independent (this one constructed the four-probe table from scratch before reading Audit2) and converge. There is no disagreement on any technical point.

This re-audit *adds* one item Audit2 did not present: the explicit U(1)_Y² ratio of magnitude 20/3 (§1c), which is the *closest* of the standard four probes to 16/3 yet still wrong. This rules out a more sophisticated attempt where one might pair Q_χ against U(1)_Y² and hope for cancellations — the answer is 20/3, not 16/3, and there is no further rescaling that lands on 16/3 without re-introducing an ad-hoc factor.

## 5. Bottom line for the v3.4 program

- The DFD ratio Ω_χ/Ω_b = 16/3 is **not** derivable as a 4D 't Hooft anomaly ratio on the field content M9 specifies, on any standard probe (SU(2)_L², SU(3)_c², U(1)_Y², gravity², or any linear combination via 't Hooft matching).
- M9's "descent-normalised polynomial ratio" is M9-internal; it relies on (i) a fabricated factor of 1/N_gen² and (ii) a misattributed citation. Both must be withdrawn.
- The honest status remains the K1-04 conclusion: the "16" and the "3" are independent integers with no single 4D anomaly equation linking them. If DFD wants 16/3 from anomaly considerations it must either (a) find a genuine common probe with a ratio of exactly 16/3 (none of the four standard probes works), or (b) find a *real* CHS-style 5d/6d descent argument in a correctly-cited paper.
- Recommendation: **retract M9 from the v3.4 derivation chain**, do not cite arXiv:2410.22412 as anomaly-matching support, and do not present 16/3 as a 't Hooft-matched quantity in the v3.4 paper.

---

**Files referenced (absolute paths):**
- /Users/garyalcock/claudecode/densityfielddynamics/v34_research/M9_thooft_ratio.md
- /Users/garyalcock/claudecode/densityfielddynamics/v34_research/Audit2_M9_chs.md
- arXiv:2410.22412 (Banerjee, Brzeminski, Hook, "Predicting the Dark Matter — Baryon Abundance Ratio")
