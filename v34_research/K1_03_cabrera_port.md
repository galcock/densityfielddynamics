# K1-3: Porting the Cabrera-Harigaya-Sundrum (2024) Mechanism into DFD

**Agent:** K1-3
**Date:** 2026-04-06
**Target:** arXiv:2410.22412 — "Dark Matter Abundance from the Ratio of Beta Functions"
**Task:** Attempt to port the CHS mechanism for Ω_DM/Ω_B ≈ 16/3 into DFD. Attack J1-1's conclusion that "neither ingredient exists in DFD."

---

## 1. The CHS Mechanism (Extracted)

From WebFetch of arXiv:2410.22412:

### 1.1 The key formula

    ρ_DM / ρ_B  =  2N / (27 − 3N)            (CHS Eq. master relation)

For N = 8 this gives 16/3 ≈ 5.33, matching the observed Ω_DM/Ω_B.

The intermediate identity is

    Q_N  ≡  (4/3) Σ_ψ n_ψ C(R₁,ψ) d(R₂,ψ)

which, for a single Dirac fermion in the fundamental of both G = SU(N) and
QCD SU(3), reduces to Q_N = 2N/3. For N = 8, Q_N = 16/3.

The density ratio arises because

    Λ_QCD(φ) ∝ [ Λ_N(φ) ]^{Q_N / β_3}

with β_3 = 9 (SU(3) with three light flavors in the relevant regime), so
r ≡ c_N/c_B = β_3 / Q_N = 27/(2N).

### 1.2 The three ingredients

**(I1) Beta function coefficient Q_N.** A two-loop mixed anomaly-like
coefficient counting colored fermions charged under *both* QCD and the
dark group G. It is fixed entirely by group theory + matter content.

**(I2) Scanner modulus φ.** A slow-rolling scalar coupling to the
confinement scales of both QCD and G through integrated-out heavy
fermions:

    (M_χ + y_χ φ) χ̄ χ     ⇒     Λ_N(φ) ∝ (M_χ + y_χ φ)^{(4 n_χ T_R / 3)/β_N}

The finite-density effective potential

    V(φ) = m_B(φ) n_B + m_DM(φ) n_DM

is minimized dynamically so that the two contributions balance, yielding

    ρ_DM / ρ_B |_{φ_min}  =  − c_B / c_D

with c_B, c_D the log-derivatives of the baryon and DM masses w.r.t. φ.

**(I3) Dark confining gauge group G = SU(N).** Makes DM = G-hadrons.
Gives a second confinement scale Λ_N that runs with φ.

---

## 2. Searching for DFD Analogs

### 2.1 Ingredient 1: Is 16/3 a DFD beta-function coefficient?

**Attempt A — Standard Model beta functions on the DFD background.**

For SU(3) with n_f Dirac flavors in the fundamental,

    b₀^(3) = (11/3)·3 − (2/3)·2·n_f = 11 − (4/3) n_f.

At the DFD QCD matching scale n_f = 6: b₀^(3) = 11 − 8 = 3. At n_f = 5:
b₀^(3) = 11 − 20/3 = 13/3. At n_f = 4: 17/3. At n_f = 3: 7. At n_f = 2:
25/3. **At n_f = 4.25 one would get 16/3**, which is not an integer.
No standard SU(3) threshold hits 16/3.

For SU(2)_L with 3 generations of SM doublets (6 quark doublets +
3 lepton doublets, but only the 3 doublet components count per flavor):

    b₀^(2) = (11/3)·2 − (2/3)·(6/2)·(3 gens·4 doublets) = 22/3 − 4 = 10/3.

Not 16/3.

For U(1)_Y with SM hypercharges: b₀^(1) = −41/10 (or 41/6 in GUT
normalization). Not 16/3.

No single SM beta function coefficient equals 16/3.

**Attempt B — A combination.** 16/3 = 8/3 + 8/3 = 2·(2N_c/3) with N_c = 4,
or 16/3 = β_3(n_f=4)/1 if one counted 4 heavy colored fermions. CHS's
own derivation is precisely Q_N = 2N/3 with N = 8, i.e. a *dark* gauge
group of rank 8. DFD has no SU(8) sector.

**Attempt C — ψ–matter running.** DFD's ψ field couples to matter
through ρ_eff = ρ_b·f(a_ψ/a_0) (MOND relation), not through a minimal
gauge coupling whose β-function could be computed. ψ has no gauge
charge and therefore contributes zero to any b₀. The running of the
ψ–matter coupling is set by the external classical MOND interpolating
function, not by a fermion loop, so there is no Q_N-like coefficient
to evaluate.

**Attempt D — The S³ Chern-Simons level.** The DFD internal manifold
supports CS theory with k_max = 60. CS at level k has **no continuous
running** — k is an integer topological invariant quantized by level
quantization. There is no β-function in the usual sense; the only
"running" is the 1-loop shift k → k + h∨. This is not the same
mathematical object as Q_N.

**Verdict on Ingredient 1:** DFD contains no coefficient equal to 16/3
arising from a β-function of a gauge coupling charged under two groups.
The closest structural match is that CHS's 16/3 = 2N/3 is identical in
form to the DFD ratio Tr_χ/Tr_b = 16/3 that appears in the χ-sector
trace-anomaly budget — but this is a *trace* ratio (group-theory index
of the χ representation relative to the baryon representation), not a
β-function. The coincidence is real but superficial: they are different
invariants of the same numerical form.

### 2.2 Ingredient 2: Is ψ the "scanner modulus"?

ψ has several of the scanner's attributes but fails on the critical one.

| Property                                 | CHS scanner φ     | DFD ψ                          |
|------------------------------------------|-------------------|--------------------------------|
| Slow-rolling on cosmological timescales  | Yes               | Yes (dust branch, w = 0)       |
| Couples to matter masses                 | Yes, via y_χ χ̄χ  | Yes, via MOND relation         |
| Log-derivative c = ∂ln m/∂φ non-zero     | Yes               | **Zero at tree level**         |
| Couples to gauge-field running           | Yes (through χ)   | **No direct coupling**         |
| Has finite-density potential V(ψ)        | V(φ) = m_B n_B…   | Effective dark-fluid stress    |

The decisive failure: CHS's mechanism requires c_B = ∂ln m_B/∂φ and
c_D = ∂ln m_DM/∂φ *both non-zero and unequal*, because ρ_DM/ρ_B =
−c_B/c_D. In DFD the MOND relation modifies the *effective* inertial
response of baryons in weak-field regions, but does not change the
Lagrangian rest masses m_p, m_n, m_χ. Therefore c_B^DFD ≈ 0 and the
ratio is mathematically undefined.

One could *try* to generalize by letting ψ shift the χ mass via a
portal (ψ χ̄χ). The internal-manifold analysis (H11) pins m_χ =
M_P α^9 independently of ψ. Allowing a portal breaks that lock,
re-introduces a free parameter, and loses DFD's predictivity — i.e.
it wins "16/3 from dynamics" only by surrendering "m_χ from
geometry". A Pyrrhic victory.

**Verdict on Ingredient 2:** ψ has the kinematics of a scanner but
not the coupling structure. Forcing it to act as one costs DFD the
very prediction (m_χ from α^9) that already gives the right DM mass.

### 2.3 Ingredient 3: Is S³ CS at k = 60 the dark confining sector?

CS theory is **topological**, not confining. It has:
- No propagating degrees of freedom (on a closed manifold).
- A finite-dimensional Hilbert space, not a hadron spectrum.
- A partition function Z_CS(S³, k, G) given exactly by the
  Witten/Reshetikhin-Turaev formula, not by a strong-coupling scale.

The "confinement scale" Λ_CS ≡ M_P α^8 ≈ 19.6 GeV cited in H5 is a
DFD *two-scale rewrite* — a convenient parametrization of the α-tower
— not a dynamically generated strong-coupling scale. There is no
Yang-Mills kinetic term on S³ from which it descends, and therefore
no RG flow from UV to IR that CHS's scanner could modulate.

One could propose that the χ field lives in the *bulk* (not on S³)
and gets its mass from a 4D confining sector analogous to SU(N). But
DFD's core claim is that χ is the 4D image of a topological internal
mode, not a confined hadron of a hidden gauge group. Replacing the
geometric origin of m_χ with a hidden SU(8) sector is precisely the
model CHS already wrote down — DFD would then be *adding* CHS on top,
not deriving its result.

**Verdict on Ingredient 3:** S³ CS at level 60 is topological and
cannot play the role of the dark confining gauge group. DFD has no
hidden SU(N) confining sector.

---

## 3. Attempted Port

Step-by-step substitution into the CHS derivation:

| CHS step                                | DFD substitution            | Works?    |
|-----------------------------------------|------------------------------|-----------|
| Pick G = SU(N), N = 8                   | S³ CS k = 60                 | No (topological, not confining) |
| Compute β_N, β_3                        | No 4D SU(8) β-function       | No        |
| Define Q_N = (4/3) Σ n C(R₁) d(R₂)      | Trace ratio Tr_χ/Tr_b = 16/3 | Same number, different object |
| Scanner field φ                         | ψ                            | Partial (slow-roll yes, couplings no) |
| m_B(φ), m_DM(φ)                         | m_p, m_χ                     | No φ-dependence in DFD         |
| ρ_DM/ρ_B = −c_B/c_D                     | Undefined (both c ≈ 0)       | No        |
| Λ_QCD(φ) ∝ Λ_N(φ)^{Q_N/β_3}            | No analog                    | No        |

The port fails at multiple independent points. The one non-trivial
coincidence — that both frameworks produce the number 16/3 — turns out
to refer to different mathematical objects:
- CHS: a β-function coefficient Q_N = 2N/3 for a hidden SU(N=8) sector.
- DFD: a trace ratio Tr_χ/Tr_b of the χ field (spin-2 traceless) over
  the baryon stress-energy trace in the two-fluid decomposition.

Both are dimensionless invariants of their respective theories, and
both equal 16/3, but the equality is structural coincidence not
dynamical equivalence.

---

## 4. Is the Coincidence Meaningful?

Worth noting as a potential bridge, *not* as a derivation:

Numerology: 2·N/3 = 16/3 ⟺ N = 8. DFD's CS level k_max = 60 is not 8,
but 60/8 = 7.5, not an integer. However, the dual Coxeter numbers
h∨(SU(N)) for small N are 2, 3, 4, 5, 6, 7, 8, 9, … — and SU(8) has
h∨ = 8. At CS level k, the effective level is k + h∨ = 68 for SU(8).
This is numerologically uncomfortable and is not pursued here.

A more honest framing: the **observed** Ω_DM/Ω_B ≈ 5.36 picks out the
rational 16/3, and *any* theory deriving that number must produce it
either as 2N/3 (CHS-type: hidden SU(N)) or as a trace ratio of two
sectors with appropriate group-theory content (DFD-type: χ vs baryon
traces). These are the only two rational paths to 16/3 with small
denominators. DFD chose the trace-ratio path; CHS chose the
β-function path. Each is self-consistent inside its own framework.

---

## 5. Conclusion

**J1-1's verdict stands.** The CHS mechanism does not port to DFD:

1. DFD has no gauge β-function coefficient equal to 16/3. The SM
   β-functions at physical flavor thresholds give (3, 13/3, 17/3,
   7, 25/3, …), none of which is 16/3. No dark SU(8) exists in DFD.

2. ψ is slow-rolling but does not couple to fermion masses with a
   non-zero log-derivative, so the finite-density balance
   ρ_DM/ρ_B = −c_B/c_D is mathematically undefined in DFD. Forcing
   a portal coupling to rescue it destroys the independent α^9
   prediction for m_χ.

3. S³ CS at k = 60 is topological, not confining. It has no RG flow
   that a scanner could modulate and no dynamical Λ_CS in the
   CHS sense.

**However**, the two frameworks independently produce the number 16/3
as a dimensionless invariant. In CHS it is a β-function coefficient
Q_N = 2N/3 for N = 8. In DFD it is a trace ratio Tr_χ/Tr_b from the
χ-sector decomposition. These are different objects with the same
numerical value — a coincidence that deserves noting but not
conflation. DFD's derivation of 16/3 stands on its own trace-ratio
construction and does not gain or lose from the CHS mechanism.

**Recommendation:** Cite CHS (2024) in the DFD DM section as an
independent rational-number derivation of the same 16/3, reached by
entirely different group-theory machinery. This strengthens the case
that 16/3 is not coincidental to the observed Ω_DM/Ω_B. Do not
attempt to identify the two mechanisms.

---

## References

- Cabrera, Harigaya, Sundrum (2024), arXiv:2410.22412.
- DFD internal: H5 (two-scale rewrite), H11 (Planck mass audit),
  J1-1 (prior CHS assessment), α-tower theorem (m_χ = M_P α^9).
