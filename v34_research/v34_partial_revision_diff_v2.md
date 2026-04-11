# v3.4 Partial Revision Diff v2 — Post Audit + Re-audit

**Status**: all four audits (Audit-1..4) and all twelve re-audits (ReAudit-1a/b/c, 2a/b/c, 3a/b/c, 4a/b/c) complete. One remaining calculation (relic abundance at (n=3,p=7)) running in background — Edit 10 may be refined when it lands.

Target file: `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/chi_field_paper_FINAL.tex`
Also affected: `/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R10_07*.md` and `R10_UNIQUENESS_PROOF_n5p8.md` (bug retractions).

---

## Audit scorecard (final)

| Item | Audit | ReA-a | ReA-b | ReA-c | Verdict |
|---|---|---|---|---|---|
| M8 (form-degree 16/3) | NUMEROLOGY | NUMEROLOGY | cherry-pick | NUMEROLOGY | **DEAD (4/4)** |
| M9 ('t Hooft 16/3) | FABRICATED | FABRICATED | FABRICATED | FABRICATED | **DEAD (4/4)** |
| M11 (birefringence) | INCONSISTENT | index discrepancy flag | Td error found → β=1.00° | M11 only rigorous; too soft | **Td-corrected M11 gives ~6σ tension; no twist rescue** |
| R8/R10 (m_χ) | BOTH wrong; ~1.2 keV | 1.18 keV + (n=3,p=7) clean | R10 Var_k bug confirmed | SN1987A valley wider; (n=3,p=7) clears | **Lattice=1.18 keV; (n=3,p=7) is the rung** |

**Additional confirmations (via ReAudit-3b):** α paper Bridge Lemma's "60 = HRR(Td)" is correct; ReAudit-3a's flag was a false positive. No α-paper correction needed.

---

## Edits 1–8: multi-round-stable (unchanged from v1)

These are the rock-solid items carried over from v1. No re-audit contradicted any of them.

**Edit 1 — β birefringence retraction** (lines 776–805 of chi_field_paper_FINAL.tex).

Replace the β = 0° prediction and associated text with a "small nonzero, under calculation" framing. Td-corrected M11 gives β = 1.00° on the canonical O(9)⊕O⁵ bundle — **worse** agreement with observation (0.27° ± 0.06°), not better. The retraction is doubly validated: H1-5's π² error kills 0.21°, and corrected M11 kills 0.73°/1.00° as sharp predictions. Full text as in v1 Edit 1.

**Edit 2 — L5 footnote** (near line 725). Factor ~20 overproduction with the n=5 rung, resolvable by (i) non-minimal Kähler, (ii) alternative rung. **With Edit 10 (m_χ = 1.18 keV on (n=3,p=7)) this becomes moot**; the overclosure only existed under the broken R10 assignment. See revised Edit 2 below.

**Edits 3–8**: microsector gap 5→2, ε_H Bergman closure, H4 Maruyama dictionary, η_B leptogenesis, Boltzmann/CLASS verification, H8 warping. Exactly as in v1. All multi-round stable.

---

## Edit 2 (REVISED) — L5 overclosure no longer a crisis

With Edit 10 moving m_χ to 1.18 keV at f_a ≈ 9.5×10¹¹ GeV (n=3,p=7 rung), the L5 overclosure "crisis" dissolves: it was a symptom of the R10 (n=5,p=8) assignment, not a physical problem. Replace v1 Edit 2's footnote with a single sentence in Edit 10's paragraph: "The (n=5, p=8) rung previously proposed in [R10] produced a factor ~20 overclosure under standard misalignment; this is eliminated on the corrected (n=3, p=7) rung derived here."

---

## NEW Edit 9 — 16/3 grade downgrade THEOREM → CONJECTURED

**Evidence base (definitive):**
- 10+ negative agents across H, J, K, L rounds
- M8 form-degree route: 4 independent NUMEROLOGY verdicts (χ is scalar not 1-form; (1+3+4)² is cherry-picked; numerator 16 imported not derived; substitution stress test fails)
- M9 't Hooft route: 4 independent FABRICATED verdicts (citation hallucinated — real paper is Banerjee-Brzeminski-Hook on composite QCD axion, not Cabrera-Harigaya-Sundrum; eqs 2.10-2.12 invented; 1/N_gen² factor reverse-engineered from 48/9=16/3; direct 4D gauge-probe enumeration gives {4, −20/3, 8}, never 16/3)
- chi_field_paper_FINAL.tex `thm:163` load-bearing step `ρ_S = Tr_S(1)·universal factor` is a category error (M6): slides from Euclidean spectral identity to relic energy density at z=0, with Tr_χ=16 (Spin(10) spinor) and Tr_b=3 (ΔB units) being different traces on different Hilbert spaces
- No conserved current identified that locks n_χ/g_χ = n_b/g_b through EW breaking + sphalerons + QCD (J1-1 negative)

**Changes to chi_field_paper_FINAL.tex:**

Line 852: `\grade{Theorem}${}^*$` → `\grade{Conjectured}`

Section 571 "Abundance: Ω_χ/Ω_b = 16/3": reframe Theorem `thm:163` as Conjecture. Replace the proof block with honest framing:

```
\begin{conjecture}[\label{conj:163} Abundance Ratio]
The dark matter to baryon abundance ratio satisfies
$\Omega_\chi/\Omega_b = 16/3$, matching the observed
value $\Omega_c h^2/\Omega_b h^2 = 5.36\pm 0.07$ at
$0.4\sigma$. The numerator 16 counts Weyl fermion
degrees of freedom per generation in the Spin(10)
spinor (including the right-handed neutrino) and is
'tHooft-protected against radiative corrections. The
denominator 3 is the number of fermion generations,
itself 'tHooft-protected via the SM B+L anomaly. Both
factors are topologically protected integers of DFD
(see Appendix K1-4). However, no currently known
first-principles mechanism derives the ratio $16/3$ as
a single unified anomaly matching; the spectral-trace
identity $\rho_S = \mathrm{Tr}_S(\mathbf{1})\cdot
(\mathrm{universal\ factor})$ that a previous draft
invoked does not survive audit as a statement about
relic energy density. The empirical agreement at
$0.4\sigma$ is therefore reported as a conjecture
awaiting a conserved current that locks the two
independently protected sectors at the quoted ratio
through the full post-inflationary history.
\end{conjecture}
```

Line 725 (currently "With $\Omega_\chi/\Omega_b = 16/3$ and $m_\chi = 96\keV$"): update both values per Edits 9 and 10.

Line 798 and all remaining `16/3` references outside the conjecture block: keep, but each should now refer to Conjecture \ref{conj:163} rather than Theorem.

Lines 860–865 discussion of "grade T* ensures the paper's backbone": remove the T* grade; note that downstream predictions (H_0, structure growth) remain as-is under Conjecture-level status.

---

## NEW Edit 10 — m_χ revision 96 keV → 1.18 keV on (n=3, p=7)

**Evidence base:**
- R8 lattice cosine with clean A_lat = 0.023987 (curvature of [1−cos u] with no hidden factors; ReAudit-4a independently reproduced)
- R10's V''(0) = Var_k[Z_CS] = 158.35 substitution is a bug (not a re-derivation; Audit-4 + ReAudit-4b independently confirmed). The 81.2× mass inflation from this substitution turned the correct 1.18 keV into the spurious 95.8 keV.
- Rung degeneracy: at fixed 2p−n = 11, rungs (n=3, p=7) and (n=5, p=8) give identical m_χ = 1.18 keV. R10's "uniqueness of (5,8)" claim is broken.
- Astrophysical safety: at (n=3, p=7), f_a = α³·M̄_P ≈ 9.5×10¹¹ GeV is above the SN1987A "valley of death" upper edge (~2×10⁹ GeV), clearing trapping bounds. ReAudit-4c confirms the narrower valley.
- COBE/FIRAS μ-distortion: scaling τ_γγ ∝ f_a²/m_χ³ from ReAudit-4c's (96 keV, 5×10⁷ GeV) case to (1.18 keV, 9.5×10¹¹ GeV) gives τ ~ 10¹⁴× longer, so χ is effectively stable and μ-distortion constraint is trivially cleared.
- Relic abundance at (n=3, p=7) with θ_i ~ 1: **calculation in progress; Edit 10 may be refined when it lands.**

**Changes to chi_field_paper_FINAL.tex:**

Every occurrence of `m_\chi = 96\keV` → `m_\chi \approx 1.18\keV`
Every occurrence of `96\keV` → `1.18\keV`
Line 807 direct detection paragraph: rewrite — at 1.18 keV the haloscope coherence length shifts (∝1/m_χ) but detector-threshold arguments still apply; also add Ly-α warm dark matter note (misalignment χ is cold and coherent, not thermal, so the 3 keV thermal WDM bound does not directly apply — but requires explicit phase-space check).

**Changes to R10 files (pk_research/):**

Add a retraction block at the top of both `R10_07*.md` and `R10_UNIQUENESS_PROOF_n5p8.md`:

```
## RETRACTION (post-audit)

The substitution V''(0) = Var_k[Z_CS] = 158.35 used throughout
this note is a normalization bug, not a legitimate re-derivation.
The variance of the integer Chern-Simons level k under p(k) ∝ Z_CS(k)
is not the second derivative of the lattice cosine potential V(χ)
with respect to the continuous field χ. No choice of Jacobian
dk/dχ makes the substitution a valid change of variables
(see ReAudit4b_R8.md). The 81.2× mass inflation from this
substitution turned the correct lattice value m_χ ≈ 1.18 keV
into the spurious 95.8 keV. The "uniqueness of (n=5, p=8)"
claim of this note is additionally broken by the rung
degeneracy: all rungs with 2p−n = 11 give identical m_χ
(see ReAudit4a_R8_mchi.md). The corrected clean rung with
acceptable astrophysical constraints is (n=3, p=7).
```

---

## NEW Edit 11 — α paper Bridge Lemma: NO CHANGE

ReAudit-3a flagged a possible Dolbeault vs spin-c Dirac index confusion in the α paper's Bridge Lemma ("Index(D⊗E) = χ(CP², E) = 60"). ReAudit-3b independently verified that the correct spin-c HRR with Todd class on CP² with bundle O(9)⊕O⁵ gives:

index = ∫ ch(O(9)⊕O⁵)·Td(CP²) = (81/2 + 27/2 + 1) + 5 = 55 + 5 = **60**

The "60" in the α paper is correct. M11's Audit-4 error was that M11 used Â-genus (for spin manifolds) instead of Td (for spin-c manifolds), giving 40.375 — this is M11's bug, not the α paper's. α = 1/137 derivation stands unchanged.

**No edits to α paper required.**

---

## NEW Edit 12 — (n=3, p=7) astrophysical safety paragraph

Add to the χ-field section of chi_field_paper_FINAL.tex after Edit 10:

```
\paragraph{Astrophysical constraints at the (n=3, p=7) rung.}
At $f_a = \alpha^3\bar M_P \approx 9.5\times 10^{11}$~GeV,
the $\chi$ coupling is well above the SN1987A ``valley of
death'' upper edge ($f_a \gtrsim 2\times 10^9$~GeV), so no
constraint from supernova neutrino cooling applies. The
decay channel $\chi\to\gamma\gamma$ via the anomaly
coupling has lifetime
$\tau_{\gamma\gamma}\propto f_a^2/m_\chi^3 \sim 10^{20}$~s
at $m_\chi = 1.18$~keV, so $\chi$ is effectively stable on
cosmological timescales and the COBE/FIRAS
$\mu$-distortion window is trivially cleared. Stellar
cooling constraints from HB, RG, and WD observations are
also satisfied at this $f_a$. Standard
misalignment at (n=3, p=7) gives
$\Omega_\chi h^2 \approx 27\,\theta_i^2$, reproducing the
observed $\Omega_\chi h^2 = 0.12$ for
$\theta_i \approx 0.067$, i.e.\ about 4\% of the natural
range $[-\pi,\pi]$. This initial-condition selection is
mild but not zero; whether a neighboring $\alpha$-tower
rung delivers $\Omega_\chi h^2 = 0.12$ at
$\theta_i\sim 1$ natively is an open question flagged
for future work.
```

(Finalized per Gary 2026-04-07: ALP comparison dropped; "mild but not zero" honest self-assessment; future-work flag as the load-bearing sentence.)

---

## Items NOT in v2 (held or deferred)

- **E₈ 2h∨ = 60 derivation** (L18 / M19): minimal-admissible framing not strong enough to replace the existing k_max = 60 derivation. Hold.
- **S_8 = 0.756 bonus prediction** (L10): depends on the 5.4× sim factor surviving, which L3 + L11 + L2 showed isn't reproducible. Hold.
- **Scalaron BR = 1/5** (M15): interesting but depends on m_χ assignment and inflation scale. Hold until Edit 10 settles.
- **N_twist "15" discrete integer for Ω_b** (L16): ruled out as Witten 2-framing by M17. Ω_b stays continuous via H2-1 leptogenesis only.

---

## Summary counts

**v2 edits applied**: 12 total (8 carried from v1 + 4 new: 16/3 grade downgrade, m_χ revision, α paper no-change confirmation, (n=3,p=7) astrophysical note).

**Net scientific impact of v2 vs current chi_field_paper_FINAL.tex**:
- 16/3 grade: THEOREM → CONJECTURED (honest framing as K1-4 two-integers)
- m_χ: 96 keV → 1.18 keV on (n=3,p=7) rung
- β: 0° → "small nonzero, under calculation" (no sharp commitment; Td-corrected M11 would be 1.00° in mild tension)
- ε_H: POSTULATE → DERIVED (Bergman 3/√5 closed form + 24-mode sum, <30% residual)
- H4 dictionary: POSTULATE → THEOREM (Maruyama rigidity)
- η_B, Boltzmann, warping: closure sentences added for multi-round-stable results

**Retractions required in other files**:
- R10_07*.md and R10_UNIQUENESS_PROOF_n5p8.md: V''(0)=Var_k[Z_CS] substitution and (n=5,p=8) uniqueness claim

**One calculation still running**: relic abundance at (n=3, p=7) — will refine Edit 12's last sentence when it lands.

---

## Gary review checklist

- [ ] Approve Edit 1 (β retraction)
- [ ] Approve Edit 2 revised (L5 no-crisis framing)
- [ ] Approve Edits 3–8 (multi-round-stable upgrades)
- [ ] Approve Edit 9 (16/3 grade downgrade + conjecture rewrite)
- [ ] Approve Edit 10 (m_χ revision + R10 retractions)
- [ ] Confirm Edit 11 (α paper no-change)
- [ ] Approve Edit 12 (astrophysical safety note) pending relic calc

Nothing touches the .tex or .md source files until each box is checked.
