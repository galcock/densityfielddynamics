# Audit 2: M9's "16/3 via CHS 't Hooft Anomaly Descent" Claim

**Auditor:** Audit2
**Date:** 2026-04-07
**Target:** `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/M9_thooft_ratio.md`
**Reference checked:** arXiv:2410.22412 (full PDF fetched and parsed)

---

## Verdict (one line)

**(d) Numerology, compounded by a misattributed citation.** M9's claim that 16/3 follows from a "strict 4D 't Hooft anomaly matching on a common SU(2)_L^2 probe with 1/N_gen^2 descent normalization" paralleling "Cabrera-Harigaya-Sundrum 2024 (arXiv:2410.22412)" is false on every load-bearing element. The cited paper is not by Cabrera/Harigaya/Sundrum, does not perform 't Hooft anomaly matching, does not use an SU(2)_L^2 probe, contains no 1/N_gen^2 descent factor, and its 16/3 is an entirely unrelated quantity (a ratio of QCD beta-function coefficients in a composite-axion relaxation model).

---

## 1. The cited paper is misattributed

arXiv:2410.22412 is:

> "Predicting the Dark Matter - Baryon Abundance Ratio"
> Abhishek Banerjee, Dawid Brzeminski, Anson Hook
> LCTP-24-20, Maryland Center for Fundamental Physics / Leinweber Center, dated October 31, 2024.

It is NOT by Cabrera, Harigaya, and Sundrum. M9 invented the author list. Every occurrence of "CHS" and "Cabrera–Harigaya–Sundrum" in M9_thooft_ratio.md refers to a paper that does not exist at the cited arXiv ID. This alone falsifies every statement in M9 of the form "CHS 2024 derive 16/3 as..." or "identical to CHS eq. 2.10–2.12."

## 2. What the actual paper says (verbatim quotes)

The paper is a relaxation/composite-axion model, not an anomaly-matching argument. The 16/3 appears in a footnote-level remark attached to eq. (2.4), with the following verbatim content (Banerjee-Brzeminski-Hook 2024):

> "ΛQCD(ϕ) ∝ (ΛN(ϕ))^(2N/(3β3)) ≡ ΛQCD(0) e^(cB ϕ/f), (2.2)"
>
> "r = cN/cB = 27/(2N), (2.3)"
>
> "ρDM/ρB = 2/(2r−3) = 2N/(27−3N), (2.4)"
>
> "The requirement to predict ρDM/ρB within 10% of the measured value is QN = 16/3. This can be achieved by having two fermions transforming under the fundamental representation under both SU(3) and G = SU(4) and/or one fermion which is in the adjoint representation of G = SU(3) and fundamental representation of SU(3) in addition to the discussed case of one fermion under the fundamental representation of both G = SU(8) and SU(3). Any choice with QN = 16/3 keeps the analysis unchanged."

The object Q_N = 16/3 is the representation-index coefficient appearing in the QCD beta-function shift induced by confining heavy colored fermions in a composite QCD-axion model. It is the value of Q_N that reproduces Omega_DM / Omega_B = 5.36 given the relaxation dynamics eq. (1.7) / (2.4). It has nothing to do with:

- 't Hooft anomaly matching (the words do not appear anywhere in the relevant section);
- an SU(2)_L^2 probe (the probe is SU(3)_c, and the mechanism is beta-function running, not anomaly inflow);
- descent from 5d/6d (the paper is strictly 4D QFT);
- any factor of 1/N_gen^2 (the SM generation count does not enter; N is the size of the composite gauge group G = SU(N), unrelated to N_gen = 3);
- "16 Weyl fermions per generation including nu_R" (the 16 in Q_N = 16/3 is not a Weyl count — it arises from 2 fermions times SU(4) fundamental, or 1 adjoint of SU(3), or 1 fundamental of SU(8); the "16" is literally 8 * 2 = 16 with 8 = N as the size of the gauge group).

## 3. Point-by-point audit of M9's claims

### 3a. "Strict 4D 't Hooft matching on a common SU(2)_L^2 probe"
**False.** No 't Hooft matching appears in the cited paper. The mechanism is IR-matching of gauge couplings via confinement-induced shifts in beta-function coefficients.

### 3b. "Descent normalization 1/N_gen^2"
**Invented.** No such factor appears in the cited paper. M9 explicitly admits in section 6 that the bare anomaly computation gives 8, not 16/3, and that "the factor of 9 in the denominator is not an arbitrary fudge: it is the square of N_gen." But it IS an arbitrary fudge: it is introduced by M9 to force the result, justified by reference to "CHS eqs. 2.10–2.12" which do not exist.

### 3c. "c_{chi,SU(2)^2} / c_{B,SU(2)^2} = 16/3"
**False by M9's own arithmetic.** In section 4, M9 computes c_chi / c_B against SU(2)_L^2 directly: c_B,SU(2)^2 = 3/2 and c_chi,SU(2)^2 = 6, giving ratio 4. M9 then explicitly writes: "Wait — this gives 6 / (3/2) = 4, not 16/3." The rest of the memo is a series of re-attempts with different probes (gravitational, then mixed left-handed, then "descent-normalized") none of which is a strict 4D 't Hooft matching, and the final value 16/3 is only reached after inserting the unjustified 1/9 = 1/N_gen^2 factor.

### 3d. "16 = 2 * 8 Weyl DOF of SO(10) spinor matches DFD b3=1 + Weyl partners"
**Coincidence, not derivation.** Even if SO(10) 16-spinors are a real thing in GUTs, the Banerjee-Brzeminski-Hook Q_N = 16/3 has NO connection to SO(10) 16-plets — it arises purely from the requirement that 2N/3 * ratio-of-beta-functions reproduces 5.36, which algebraically forces Q_N = 16/3. The "16" here is 2 * N with N = 8 the composite gauge group size; it is not a fermion generation count.

### 3e. "N_gen = 3 <-> visible sector" mapping to CHS
**No such mapping exists in the real paper.** The paper does not discuss 3 SM generations as a distinguished quantity; N_gen does not enter the derivation at any step.

### 3f. "CHS confining sector with 16 Weyl DOF"
**Fabricated.** The confining group in Banerjee-Brzeminski-Hook is G = SU(N) with N = 8 (or SU(4), or SU(3)-adjoint, per the footnote). There is no "16 Weyl DOF confining sector." The 16 is a product 2N, not a fermion count.

## 4. What M9's derivation actually is

Reading M9 section 6 charitably: M9 computes the naive anomaly ratio (getting 4 or 8 depending on probe), notes this does not equal 16/3, and then postulates a "descent normalization" of 1/N_gen^2 = 1/9 that converts 48/1 into 48/9 = 16/3. The postulate is attributed to "CHS eqs. 2.10–2.12," which are fictitious. Strip the fictitious citation and the remaining content is: "(16 * 3) / (1 * 9) = 16/3, where the 16 is a Weyl count, the 3 is N_gen, and the 9 is N_gen-squared." This is arithmetic, not physics — 48/9 reduces to 16/3 by construction once you choose to divide by 9.

## 5. Verdict rubric

(a) Genuine 4D 't Hooft matching derivation? **No.** M9's own section 4 shows the bare 4D SU(2)_L^2 ratio is 4, not 16/3.

(b) Valid 5d/6d descent argument? **No.** Neither M9 nor the cited paper performs a 5d/6d descent. M9 invokes "descent" as a rhetorical label for dividing by 9; the cited paper is pure 4D QFT.

(c) Suggestive analogy? **No.** There is no analogy to draw because the cited paper's 16/3 is a beta-function coefficient in a composite-axion relaxation model, not an anomaly ratio. The two 16/3's are numerically identical but structurally unrelated — and M9 admits it could not read the full PDF and reconstructed the argument from the abstract.

(d) **Numerology.** M9 took a published paper it had not read, invented author names, invented equation numbers, invented a "descent normalization" factor of 1/N_gen^2 that happens to convert its preferred numerator (48) into its target (16/3), and presented the result as parity with a 't Hooft matching argument that does not exist in the literature.

## 6. Recommendation

1. **Retract M9 from the v3.4 chain.** Do not cite it, do not build on it, do not treat it as an upgrade to K1-04.
2. **Correct the attribution.** arXiv:2410.22412 is Banerjee, Brzeminski, Hook (2024), "Predicting the Dark Matter - Baryon Abundance Ratio." If DFD wants to engage with their Q_N = 16/3, it must engage with what the paper actually says: a relaxation mechanism in a composite QCD axion model where Q_N is a representation-index combination, and 16/3 is the value reproducing Omega_DM / Omega_B = 5.36 via eq. (2.4): ρDM/ρB = 2N/(27 - 3N).
3. **K1-04 stands unchallenged.** M9 claimed to strengthen K1-04's "16 and 3 are independently protected" to "single descent-normalized polynomial ratio." That claim is withdrawn. The honest status remains what K1-04 said: 16 and 3 are two independent integers with no single 't Hooft equation linking them.
4. **If a real CHS-style argument exists for DFD's 16/3,** it must be found in a different paper (actual Cabrera-Harigaya-Sundrum work, if any exists, should be located and cited correctly), and must be re-derived from scratch without the fabricated 1/N_gen^2 factor.

---

**Bottom line.** M9 is not a derivation. It is a citation failure wrapped around an arithmetic identity (48/9 = 16/3). The target integer was chosen first and the "descent normalization" was engineered to land on it. Parity with arXiv:2410.22412 is not achieved because the paper in question performs a completely different calculation.
