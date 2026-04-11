# ReAudit2a: Independent Re-Audit of M9's 16/3 't Hooft Descent Claim

**Auditor:** ReAudit2a (independent of Audit2)
**Date:** 2026-04-07
**Target:** `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/M9_thooft_ratio.md`
**Cross-reference:** `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/Audit2_M9_chs.md`
**Source consulted:** arXiv:2410.22412 (fetched independently via WebFetch from arxiv.org/abs/2410.22412)

---

## Verdict (one line)

**FABRICATED.** M9's load-bearing citation is wrong about authors, mechanism, gauge probe, descent factor, and the meaning of "16." The cited paper performs none of the operations M9 attributes to it. Audit2's verdict is independently confirmed.

---

## 1. Anchor: the real paper (verbatim)

Independently fetched from arXiv:

**Title (verbatim):** "Predicting the Dark Matter -- Baryon Abundance Ratio"

**Authors (verbatim):** Abhishek Banerjee, Dawid Brzeminski, Anson Hook

**Abstract (verbatim):**
> "We discuss relaxation solutions to the dark matter - baryon coincidence problem in the context of QCD axion dark matter. In relaxation solutions, a moduli dynamically adjusts the mass of dark matter and baryons until their energy densities are O(1) the same. Because the QCD axion is heavily connected to QCD, scanning the QCD axion mass inherently also scans the proton mass. In the context of relaxation solutions, this implies that the ratio of dark matter to baryon abundances (Ω_DM/Ω_B) is a ratio of beta functions showing that these models can only accommodate discrete values of Ω_DM/Ω_B thereby ``predicting'' the ratio of the dark matter to baryon abundances. The original composite axion model has only a single integer degree of freedom N, the size of the gauge group, and we show that when N=8 the observed value of Ω_DM/Ω_B = 5.36 is reproduced to within its percent level error bars."

This abstract alone is decisive on every load-bearing M9 claim.

---

## 2. Point-by-point answers to the audit questions

### (1) Who are the actual authors? M9 claimed Cabrera-Harigaya-Sundrum.

**Banerjee, Brzeminski, Hook.** Not Cabrera, not Harigaya, not Sundrum. The "CHS" attribution running through M9 is fictional. Every "CHS eq. 2.x" reference in M9 points to a paper that does not exist at the cited arXiv ID.

### (2) What is the paper's actual mechanism for 16/3 = Omega_DM/Omega_B?

The mechanism is a **relaxation/composite-axion model**: a modulus dynamically scans the QCD axion mass (and hence the proton mass) until rho_DM and rho_B are O(1) equal. Because QCD axion physics is tied to QCD running, the ratio Omega_DM/Omega_B becomes a **ratio of QCD beta-function coefficients** induced by heavy confining colored fermions. The discrete values of Omega_DM/Omega_B are therefore set by the representation content of those fermions under the composite gauge group G = SU(N). Setting N = 8 in the original composite-axion model reproduces the observed 5.36 to within percent-level error bars.

This is **4D QCD running plus relaxation dynamics**. It is not anomaly inflow, not 't Hooft matching, not descent.

### (3) Does it use an SU(2)_L^2 probe + 1/N_gen^2 descent factor, as M9 claims?

**No on both counts.**
- The relevant gauge probe is **SU(3)_c** (QCD), not SU(2)_L. The mechanism is the QCD beta function shifted by heavy colored matter in representations of G x SU(3)_c.
- There is **no 1/N_gen^2 descent factor**. The SM generation count N_gen = 3 plays no role in the derivation. The "N" that appears is the **size of the composite gauge group G = SU(N)**, not a generation count and not appearing as 1/N^2.
- M9's "descent normalization 1/N_gen^2" is invented from whole cloth and engineered to convert M9's bare ratio (which M9 itself computes as 4 in section 4 and 8 in section 5) into the target 16/3.

### (4) Is there any 4D 't Hooft matching route visible in the paper?

**No.** The paper is a relaxation/beta-function argument, not anomaly matching. The phrase "'t Hooft anomaly" does not appear as the engine of the calculation. The abstract's own framing — "the ratio of dark matter to baryon abundances is a ratio of beta functions" — is incompatible with M9's "ratio of 't Hooft anomaly polynomials" framing.

### (5) Does the "16" in the real paper correspond to SO(10) spinor DOF, or to 2N with N=8, or something else?

**Neither the SO(10) spinor 16 nor a Weyl generation count.** In Banerjee-Brzeminski-Hook the relevant integer combination is Q_N = 16/3, which is a representation-index coefficient in the QCD beta-function shift. The footnote attached to eq. (2.4) lists multiple ways to reach Q_N = 16/3, including:

- Two fermions in the fundamental of both SU(3)_c and G = SU(4),
- One fermion in the adjoint of G = SU(3) and fundamental of SU(3)_c,
- One fermion in the fundamental of both G = SU(8) and SU(3)_c.

In the SU(8) realization, the "16" arises arithmetically as **2 x N with N = 8** (the size of the composite gauge group, not anything to do with SO(10) or with generation counting). It is a Dynkin/representation-index product, not a Weyl-fermion DOF count of an SM generation, and certainly not a topological mode count of a b_3 = 1 internal three-cycle.

---

## 3. Comparison with Audit2_M9_chs.md

Audit2 reached the same five conclusions independently. This re-audit confirms each:

| Claim in M9 | Audit2 finding | ReAudit2a confirms? |
|---|---|---|
| Authors are Cabrera-Harigaya-Sundrum | Fabricated; actual = Banerjee-Brzeminski-Hook | Yes |
| Paper uses 't Hooft anomaly matching | False; paper uses beta-function relaxation | Yes |
| Common probe is SU(2)_L^2 | False; relevant probe is SU(3)_c | Yes |
| Descent factor 1/N_gen^2 | Invented; no such factor in paper, N_gen does not enter | Yes |
| 16 = SO(10) spinor / Weyl DOF count | False; 16 = 2N from N=8 SU(N) gauge size, a Dynkin index product | Yes |
| M9 strengthens K1-04 from "two independent integers" to "single polynomial ratio" | False; M9's own arithmetic in section 4 shows the SU(2)_L^2 ratio is 4, not 16/3 | Yes |

I find no point on which Audit2 overstates its case. If anything, having read the verbatim abstract, the misattribution is even starker than Audit2 conveys: the paper's own one-sentence summary says "ratio of beta functions," which is a different category of object from an anomaly polynomial ratio.

---

## 4. What M9 actually computed

Stripping the fictional citation away, M9's arithmetic content reduces to:

  (16 Weyl x 3 generations) / (1 x 3^2) = 48/9 = 16/3.

The numerator 48 is set by choosing Q_chi = +1 democratically across all 16 Weyl modes per generation and summing over 3 generations. The denominator 9 is set by inserting a factor of N_gen^2 = 9 with the rationale "this is what CHS do in eqs. 2.10–2.12." Since CHS does not exist and the cited eqs do not exist, the 1/9 has no source. It is engineered post-hoc to land on the target 16/3.

This is the textbook signature of **numerology**: the target was fixed first, the bare computation gave the wrong answer (4 in section 4, 8 in section 5), and a free-parameter factor was inserted with a false citation to make the arithmetic match.

---

## 5. Verdict rubric

- (a) GENUINE DERIVATION? **No.** M9's own bare 4D SU(2)_L^2 calculation in section 4 yields 4, not 16/3.
- (b) VALID ANALOGY? **No.** There is no analogy to draw because the cited paper computes a beta-function ratio, not an anomaly polynomial ratio. The two 16/3's are numerically identical but structurally unrelated objects.
- (c) NUMEROLOGY? Partially — the arithmetic 48/9 = 16/3 is real, but only after inserting an unsourced factor.
- (d) **FABRICATED.** The strongest classification, because the load-bearing element is a citation to a non-existent paper. M9 invented:
  1. The author list (Cabrera-Harigaya-Sundrum),
  2. The mechanism (4D 't Hooft anomaly matching with SU(2)_L^2 probe),
  3. The descent normalization factor (1/N_gen^2),
  4. The equation references (CHS eqs. 2.7–2.12, 2.10–2.12),
  5. The "16 = SO(10) spinor 16 = SM generation Weyl count" identification (the real paper's 16 is 2N with N=8).

When the central citation is fabricated and every load-bearing element of the argument depends on that fabrication, "numerology" understates the failure. The correct classification is **FABRICATED**.

---

## 6. Recommendation

1. **Retract M9 from the v3.4 chain.** Do not cite, do not build on, do not present as an upgrade to K1-04.
2. **Correct the bibliographic record.** arXiv:2410.22412 is Banerjee, Brzeminski, Hook (2024), "Predicting the Dark Matter -- Baryon Abundance Ratio." Any future DFD engagement with this paper must engage with what it actually says: a composite-axion relaxation model in which 16/3 is the value of a representation-index coefficient Q_N that, fed into eq. (2.4) rho_DM/rho_B = 2N/(27 - 3N), reproduces 5.36.
3. **K1-04 stands.** The honest status of the DFD 16/3 derivation remains: 16 and 3 are two independent integers with no single 4D 't Hooft equation linking them.
4. **If DFD wants a real CHS-style anchor**, locate an actual paper (Cabrera, Harigaya, or Sundrum may have written something relevant — that should be searched and cited correctly) and re-derive without the invented 1/N_gen^2 factor.
5. **Process improvement.** Agents writing memos that depend on a published-paper citation must fetch the abstract verbatim and quote it in the memo before building on the reference. M9 failed this basic check; the resulting memo is structurally indistinguishable from a hallucinated derivation.

---

**Bottom line.** Independent verification confirms Audit2 in full. M9 is not a derivation, not an analogy, and barely even numerology — it is a fabricated citation wrapped around the arithmetic identity 48/9 = 16/3, with every connecting claim to arXiv:2410.22412 false. The real paper is by Banerjee, Brzeminski, and Hook; its mechanism is QCD beta-function relaxation in a composite axion model; its "16" is 2N with N=8; and it neither uses nor mentions the SU(2)_L^2 't Hooft descent that M9 attributes to it.
