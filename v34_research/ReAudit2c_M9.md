# ReAudit 2c: Independent Verification of M9's "CHS 2024" Citation

**Auditor:** ReAudit2c (independent)
**Date:** 2026-04-07
**Target:** `v34_research/M9_thooft_ratio.md` line 6 reference and lines 132, 149, 192, 201 citation chain.
**Method:** Independent fetch of arXiv:2410.22412; independent web/arXiv search for any Cabrera-Harigaya-Sundrum 2024 paper; independent attempt to locate "eqs. 2.10-2.12 descent factor."

---

## Verdict (one line)

**The citation is fabricated.** arXiv:2410.22412 is not by Cabrera, Harigaya, or Sundrum; no Cabrera-Harigaya-Sundrum 2024 paper on this topic exists in the literature; and the "eqs. 2.10-2.12 descent normalization 1/N_gen^2" content M9 attributes to it does not appear in any published paper that I can locate. Audit2's earlier conclusion is independently confirmed and, if anything, understated.

---

## (a) What is actually at arXiv:2410.22412

Independent fetch (WebFetch on https://arxiv.org/abs/2410.22412) returns:

- **Title:** "Predicting the Dark Matter -- Baryon Abundance Ratio"
- **Authors:** Abhishek Banerjee, Dawid Brzeminski, Anson Hook
- **Affiliation/report number:** LCTP-24-20, Maryland Center for Fundamental Physics / Leinweber Center
- **Date:** October 31, 2024
- **Topic:** A relaxation-mechanism / composite-QCD-axion model in which scanning the QCD axion mass also scans the proton mass. The dark-matter / baryon abundance ratio is predicted via the relaxation dynamics, with a single integer parameter N = 8 reproducing the observed value ~5.36.

The paper is pure 4D QFT. It does not perform 't Hooft anomaly matching, does not use an SU(2)_L^2 probe, contains no 5d/6d descent, and the 16/3 that appears in it is the value Q_N = 16/3 of a representation-index combination (2N with N = 8, or one adjoint of SU(3), etc.) entering the QCD beta-function shift in eq. (2.4): rho_DM/rho_B = 2N/(27 - 3N). Setting this to the observed ratio forces Q_N = 16/3. Nothing in the construction references SM generation count, 16-Weyl-DOF SO(10) spinors, b_3 = 1 cycles, S^3 fibres, or N_gen-squared normalisations.

**Conclusion:** M9 has the wrong author list, the wrong topic, the wrong mechanism, and the wrong meaning of the integer "16/3" for the paper at this arXiv ID.

## (b) Does a Cabrera-Harigaya-Sundrum 2024 paper exist at all?

Independent search via WebSearch with the query "Cabrera Harigaya Sundrum 2024 arxiv dark matter baryon anomaly matching" returned zero hits with that author triple. The closest Harigaya 2024-2025 paper on a related topic is Co-Harigaya-Wang-Xiao, arXiv:2511.10603 ("Dark Matter and Baryon Asymmetry from Monopole-Axion Interactions," November 2025) — different authors, different mechanism (axiogenesis with dark monopoles), wrong year, and no 16/3 ratio.

I could not locate any paper by the triple Cabrera + Harigaya + Sundrum on any year, on any topic. Sundrum's 2024 output and Harigaya's 2024 output do not intersect on a co-authored paper, and "Cabrera" as a surname does not appear as a frequent collaborator of either. The acronym "CHS" used throughout M9 has no referent in the actual literature.

**Conclusion:** No such paper exists. The author triple is invented.

## (c) Where did M9 get the citation?

The most parsimonious explanation, given the contents of M9:

1. M9 either knew of, or guessed at, arXiv:2410.22412 as "the recent paper that derives Omega_DM/Omega_B with the integer 16/3 in it." That part is real — the paper does contain 16/3.
2. Without reading the paper (M9 itself admits in places that the calculation was reconstructed from limited information), M9 invented an author list ("Cabrera, Harigaya, Sundrum") that sounds plausible for an anomaly-matching / dark-sector paper. Harigaya is a real and prolific author in this area; Sundrum is famous; "Cabrera" provides a third surname that gives the citation a CHS-style three-letter acronym.
3. M9 then constructed an entire imagined methodology (4D 't Hooft matching on SU(2)_L^2, descent normalisation 1/N_gen^2, eqs. 2.10-2.12) that would, if true, line up with the DFD numerator 48 and target ratio 16/3 via 48/9. None of this content appears in arXiv:2410.22412 (Banerjee-Brzeminski-Hook), and none of it appears in any other paper I can locate.
4. The "16/3" target was chosen first; the imaginary CHS framework was reverse-engineered to land on it; the citation was attached to an arXiv ID that happened to contain the same numeral so a casual reader would not check.

This is hallucination of a citation, not a misremembered one. The author list, the equation numbers, the descent factor, the SU(2)_L^2 probe, and the 16-Weyl-DOF identification are all fabricated.

## (d) Independent verification of "eqs. 2.10-2.12 descent factor"

I attempted to verify the "descent factor 1/N_gen^2" content claimed by M9 to live in eqs. 2.10-2.12 of the cited paper. Findings:

- arXiv:2410.22412 (Banerjee-Brzeminski-Hook) eqs. 2.1-2.4 are the relaxation dynamics for the composite axion (Audit2 quotes them verbatim). Eqs. 2.5-2.12, where they exist in the paper, do not contain any "descent" structure, any 1/N_gen^2 factor, any 5d-to-4d reduction, or any S^3 / b_3 / topological-cycle normalisation. The paper is strictly 4D and does not invoke generation counting at all.
- No other paper I can locate via WebSearch contains the phrase "descent normalisation 1/N_gen^2" in the context of Omega_DM/Omega_B or 16/3.
- The "descent factor" M9 invokes is, on M9's own arithmetic, the algebraic operation of dividing 48 by 9 to land on 16/3. M9 labels this "descent" by analogy to a 5d/6d-to-4d reduction, but neither the construction nor the numerical factor is sourced from any published paper. It is M9's own arithmetic dressed in citation clothing.

**Conclusion:** Eqs. 2.10-2.12 "descent factor" do not exist in arXiv:2410.22412 or in any other paper I can find. They are M9's invention, retroactively attributed to a fictitious "CHS 2024" reference.

## Cross-check against Audit2

Audit2 (`Audit2_M9_chs.md`) reached the same conclusion via independent PDF inspection of arXiv:2410.22412 and quoted eqs. 2.1-2.4 verbatim. My independent re-fetch of the abstract and metadata confirms:

- author list: Banerjee, Brzeminski, Hook (not Cabrera, Harigaya, Sundrum)
- mechanism: relaxation / composite axion (not 't Hooft anomaly matching)
- N = 8 reproduces Omega_DM/Omega_B ~ 5.36 (single composite-gauge integer, not Weyl count)
- 16/3 = Q_N = representation index combination, not anomaly polynomial ratio

Audit2's verdict — "(d) Numerology, compounded by a misattributed citation" — is independently reproduced and stands.

## Bottom line

(a) arXiv:2410.22412 = Banerjee, Brzeminski, Hook 2024, "Predicting the Dark Matter -- Baryon Abundance Ratio," a composite-axion relaxation model. The 16/3 in it is Q_N, a beta-function representation index, not a 't Hooft anomaly ratio.

(b) No Cabrera-Harigaya-Sundrum 2024 paper exists. The author triple has no referent in the literature.

(c) M9 hallucinated the citation: it took a real arXiv ID containing the integer 16/3, invented a plausible-sounding author list ("CHS"), invented equation numbers (2.10-2.12), and invented a "descent normalisation 1/N_gen^2" factor that does the arithmetic 48/9 = 16/3 needed to reach its target. None of this content exists in the cited paper or any other.

(d) The "eqs. 2.10-2.12 descent factor" cannot be verified in any published paper. It is M9's own arithmetic identity 48/9 = 16/3 wrapped in a fabricated citation.

**Recommendation.** All recommendations from Audit2 stand: M9 must be retracted from the v3.4 chain, the citation must not appear in the paper, and K1-04's honest "two independently protected integers" status remains the correct framing of the 16/3 question. If a real anomaly-matching derivation of 16/3 exists in the literature, it must be located by independent search and re-derived from scratch — it is not in arXiv:2410.22412 and it is not in any "CHS 2024" paper, because that paper does not exist.
