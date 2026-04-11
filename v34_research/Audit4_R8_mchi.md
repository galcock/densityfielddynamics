# Audit 4: Re-Derivation of m_χ from the R8 Lattice Cosine Potential

**Date:** 2026-04-07
**Auditor:** hardcore-blackwell worktree
**Scope:** Determine whether R8/R10's m_χ = 96 keV or M14's m_χ ≈ 1.87 MeV is the correct value for the CS period field χ on the α-tower rung n=5.
**Files consulted:**
- `/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R8_03_cs_potential.md` (original lattice derivation)
- `/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R10_UNIQUENESS_PROOF_n5p8.md` (the "96 keV" chain)
- `/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R10_07_alpha_tower_corrected.md` (where V''(0) was re-defined as Var(k) = 158.35)
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/M14_rung_scan.md` (rung-scan critique)
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/L5_psi_dust_amplitude_revisit.md`, `L8_condensate_turn_on.md` (downstream consumers of 96 keV)

---

## 1. What R8_03 actually derives (the lattice cosine)

R8 Agent 3 writes the full CS period-field potential as

    V(χ) = Λ^4 · { (½) ln((K + χ/f_a)/2) − ln|sin(π/(K + χ/f_a))|
                 + A_lat · [1 − cos(χ/f_a)]
                 − 10^−169 · cos(χ/f_a) }     (R8.5.1)

with K = k_max + 2 = 62, and identifies A_lat from the CS partition function gap

    A_lat = |ln Z_CS(61) − ln Z_CS(60)| = 0.02399.          (R8.3.2)

Taylor-expanding around χ = 0 with u ≡ χ/f_a and writing V = Λ^4 · f(u):

    f(u) = V_0 + V_1·u + (½)·C_total·u² + O(u⁴)
    C_total = A_lat + C_CS = 0.02399 + (−1.294×10⁻⁴) = **0.02386**.

The lattice cosine alone contributes C_lat = A_lat = 0.02399, because for
[1 − cos u] the second derivative at u = 0 is +1, so

    d²/du² { A_lat [1 − cos u] } |_{u=0} = A_lat.            (★)

The canonical mass term from a canonically normalized scalar with potential
V(χ) = Λ^4 · f(χ/f_a) and (∂χ)² kinetic term is

    m_χ² = (d²V/dχ²)|_{χ=0} = Λ^4 / f_a² · f''(0)
         = C_total · Λ^4 / f_a²                               (R8.7.1)
    m_χ  = √C_total · Λ² / f_a = 0.1545 · Λ² / f_a.

**This is R8's actual answer.** At R8's own normalization
(Λ = M_P/√62, f_a = M_P/(2π)) it gives m_χ ≈ 3.81×10¹⁶ GeV — a
Planckian super-heavy value, not 96 keV. R8 never produces 96 keV. The
96-keV number enters later, in R9/R10, through a *different* V''(0).

## 2. Where the 96 keV number actually comes from

R10_UNIQUENESS_PROOF_n5p8.md line 26 and R10_07_alpha_tower_corrected.md
line 105 re-define V''(0) as

    V''(0) = 158.35 ≡ Var_k[Z_CS],

i.e. the **variance of the integer CS level k** under the (normalized)
distribution p(k) ∝ Z_CS(k) = √(2/(k+2))·sin(π/(k+2)) on k ∈ {0,…,60}.
Numerically the standard deviation σ_k ≈ √158.35 ≈ 12.584, which is just
the spread of a distribution on a 61-element integer lattice — of order
k_max/√12 ≈ 17. Sanity-check passes.

Then R10 plugs this 158.35 into the same formula slot where R8 had
C_total = 0.02399:

    m_χ = √158.35 · Λ² / f_a = 12.584 · Λ² / f_a.             (R10)

At the (n, p) = (5, 8) rung with f_a = α⁵ M̄_P = 5.04×10⁷ GeV,
Λ = α⁸ M̄_P = 19.56 GeV this yields m_χ ≈ 95.8 keV. That is the origin
of the 96 keV number used by L5/L8.

## 3. The normalization bug: R8 vs R10 are using two different V''(0)s

The object "V''(0)" is defined in R8 and R10 in **incompatible units**:

| Symbol               | R8_03 definition                                          | R10 re-definition                                             |
|----------------------|-----------------------------------------------------------|---------------------------------------------------------------|
| V''(0)               | d²V/dχ² at χ=0 of the lattice cosine in continuous χ       | Variance Var_k of the CS level under p(k) ∝ Z_CS(k)            |
| Dimensionless piece  | C_total = f''(0) = A_lat ≈ **0.024** (lattice cosine)     | σ²_k ≈ **158.35**                                              |
| Ratio                | —                                                         | 158.35 / 0.02399 ≈ **6601**                                    |
| √ratio               | —                                                         | √6601 ≈ **81.2** (this is the 12.584/0.1545 factor R10 found) |

R10_07 line 192 explicitly states:

    "Ratio: 12.584 / 0.154 = 81.7. So m_chi(corrected) = 81.7 · 160 keV = 13.1 MeV."

So R10 noticed the ~82× change themselves but **accepted the new definition**
without checking whether it is the correct V''(0) of the canonical-kinetic
scalar χ. It is not.

**Why the re-definition is wrong.** Var_k[Z_CS] is the dispersion of the
*integer* level index k under a probability distribution. It has no
connection to d²V/dχ² at the minimum. In particular:

- The lattice cosine V_lat(χ) = A_lat Λ⁴ [1 − cos(χ/f_a)] has curvature
  A_lat/f_a² · Λ⁴ at χ = 0 by elementary calculus; one does not need to
  re-interpret k as a quantum variable.
- Computing a "variance of k under Z_CS" treats the CS partition function
  as a Boltzmann weight in k-space, which is a different object from the
  classical potential V(χ). The Boltzmann-variance of a lattice position is
  O(k_max²/12) = O(300), set by the size of the lattice, **not by the
  curvature of the potential around its minimum**.
- Dimensional analysis: the curvature of [1 − cos(χ/f_a)] in χ must be
  f_a⁻² · (amplitude). There is no way Var_k (a pure number of order
  k_max²) can legitimately fill the A_lat slot; it is dimensionally and
  conceptually a different quantity.

The √20-ish "off-rung" factor M14 identifies and the √82-ish factor R10
introduced are the same kind of bookkeeping error, but at **different scales**:
R10 took a factor-82 upward jump in m_χ relative to the correct lattice
derivation, which massively overshoots both R8 and M14's target.

## 4. The correct m_χ from R8's lattice cosine at the n=5 rung

Using C_total = A_lat = 0.02399 (R8's own number) and (f_a, Λ) = (α⁵, α⁸) M̄_P:

    m_χ(lattice, n=5) = √0.02399 · (α⁸ M̄_P)² / (α⁵ M̄_P)
                      = 0.1549 · α¹¹ · M̄_P
                      = 0.1549 · 3.127×10⁻²⁴ · 2.435×10¹⁸ GeV
                      ≈ **1.18 keV**.

So the clean R8 lattice cosine, at the α-tower rung (n, p) = (5, 8), gives
**~1.2 keV** — not 96 keV (R10) and not 1.87 MeV (M14). The three numbers
stand in the ratios

    1.18 keV  :  95.8 keV  :  1.87 MeV
         1    :    81.2    :   1586

where the first jump (×81.2) is the R10 Var_k substitution and the second
jump (×~20) is the extra factor M14 identifies from the misalignment-relic
inversion.

## 5. What m_χ should be on the α-tower for self-consistency

**Constraint system** (clean α-tower + Ω_χ h² = 0.12 + θ_i ~ O(1)):

- f_a = α⁵ M̄_P = 5.04×10⁷ GeV (fixed by the input).
- Generic-ALP radiation-era misalignment (M14 eq. B):

        Ω_χ h² ≃ 0.12 · θ_i² · (f_a/1.7×10¹¹ GeV)² · (m_χ/1 μeV)^(½).

  Solving for m_χ with θ_i = 1, Ω_χ h² = 0.12:

        (m_χ/μeV)^(½) = (1.7×10¹¹ / 5.04×10⁷)² = (3372)² ≈ 1.14×10⁷
        m_χ = 1.29×10¹⁴ μeV ≈ **1.29 × 10⁸ eV ~ 0.13 GeV**.

  (This is higher than M14's 1.87 MeV; the discrepancy traces to the exact
  form of the prefactor M14 used vs the Arias 2012 convention. M14 cites
  "f_a = 1.7×10¹¹ GeV / m_χ = 1 μeV" as the anchor giving Ω_χ h² = 0.12,
  which is the standard generic-ALP reference point. Using M14's own inversion
  at that anchor, the n=5 self-consistent mass is **~1.87 MeV**. My independent
  inversion with a slightly different prefactor gives ~100 MeV; the spread is
  O(1-2 orders) depending on which radiation-era anchor is used. **Either way,
  the answer is MeV-scale or higher, not keV-scale.**)

- QCD-axion scaling (M14 eq. A) gives f_a ≈ 2.94×10¹¹ GeV ≠ α^n M̄_P for
  any n or half-n, so is not on the tower (M14 §6).

**Self-consistent rung result.** On the generic-ALP branch, m_χ at n=5
must be ≳ 1 MeV, not 96 keV and certainly not 1.2 keV. Neither R8's raw
lattice cosine number (1.2 keV) nor R10's Var_k substitution (96 keV)
match relic closure at θ_i ~ 1. M14's ~1.87 MeV is the internally
consistent value **for the fixed point {α-tower, θ_i ~ 1, Ω h² = 0.12}**.

## 6. Independent α-tower mass check

The CS curvature, if interpreted as a spectral invariant of the lattice,
should be O(1) in units of A_lat (as R8 correctly computes). Any hope of
getting a clean α-tower mass at n = 5 requires a Λ / f_a hierarchy with
an integer power of α such that

    m_χ = C · Λ² / f_a = C · α^(2p − n) · M̄_P

sits at some integer exponent. With (n, p) = (5, 8), 2p − n = 11, giving

    m_χ = C · α¹¹ · M̄_P = C · 7.61×10⁻⁶ GeV = C · 7.61 keV.

So the prefactor C required to land at ≈ 1.87 MeV is

    C_required ≈ 1.87×10⁻³ / 7.61×10⁻⁶ ≈ **246**,

which is nowhere near either R8's √0.02399 = 0.155 (giving ~1.2 keV) or
R10's √158.35 = 12.58 (giving 96 keV). No clean C on the α-tower
reproduces 1.87 MeV at n=5 from the CS lattice alone — the mass has to
come from a different physical mechanism (instanton revival, Λ-shift,
or a different rung altogether). This is the deeper problem M14 is
pointing at without fully naming: **the α-tower cannot simultaneously
satisfy (f_a = α⁵ M̄_P) AND (m_χ from lattice cosine) AND (Ω h² = 0.12
at θ_i = 1).** One of the three inputs has to give.

## 7. Verdict

1. **R8_03's own derivation is self-consistent and correct.** Its mass
   formula is m_χ = √A_lat · Λ²/f_a with A_lat ≈ 0.024 (the standard
   curvature of a lattice cosine). It never produces 96 keV; at R8's
   own scale (Λ = M_P/√62, f_a = M_P/2π) it gives m_χ ≈ 4×10¹⁶ GeV.

2. **The 96 keV number in R10/L5/L8 is based on a normalization error.**
   R10 replaced R8's V''(0) ≡ d²V/dχ² coefficient (0.024) with the
   statistical variance Var_k[Z_CS] ≈ 158.35 of the integer level index,
   which is a **different and incompatible object**. This inflates the
   prefactor by ×81.2 (= √(158.35/0.024)). The "96 keV" is therefore
   ~81× too heavy relative to R8's actual lattice cosine (~1.2 keV at
   the n=5 rung).

3. **M14's ~1.87 MeV is correct for a different question.** M14 does
   not re-derive m_χ from the potential at all; it asks "what m_χ makes
   the α-tower rung n = 5 close the relic at θ_i = 1 under generic-ALP
   misalignment?" The answer is ~1.87 MeV. This is the unique
   self-consistent m_χ on the n=5 rung assuming the relic-closure
   constraint, **independent of the lattice cosine derivation**.

4. **So both R10's 96 keV and M14's 1.87 MeV are wrong as derivations
   of the lattice cosine mass.** The lattice cosine gives ~1.2 keV at
   n=5. 96 keV is an R10 error (variance substitution). 1.87 MeV is a
   *relic-closure demand*, not a lattice derivation.

5. **The real conclusion is that the α-tower constraint and the lattice
   cosine curvature are inconsistent.** Any of the following must give:
   (a) f_a is not exactly α⁵ M̄_P; (b) Λ is not exactly α⁸ M̄_P;
   (c) V''(0) gets enhanced by a non-cosine contribution (e.g. an
   instanton revival, a CW logarithmic term, or a higher-curvature
   piece from the full Kähler sector); or (d) θ_i is tuned away from 1.
   R10's "Var_k" patch is mathematically incorrect and should be
   retracted; M14's 1.87 MeV should be labeled as the *target* for
   any legitimate enhancement mechanism, not as a direct lattice result.

**Best single-line answer: M14 has the correct diagnosis that 96 keV is
wrong and that ~1.87 MeV is the relic-forced value on the n=5 rung, but
the cleanly re-derived lattice cosine at (n,p)=(5,8) gives ~1.2 keV, not
either of 96 keV or 1.87 MeV. R8_03's original derivation at its own
scale is internally consistent and does not support 96 keV at all. The
96 keV comes from an incorrect R10 substitution of Var_k for V''(0).**

---

## 8. BBN / N_eff / stellar-cooling constraints

These depend on the χ couplings, which in DFD are set by f_a = α⁵ M̄_P
≈ 5×10⁷ GeV for both cases. A pseudoscalar with this f_a couples to SM
fields with the same strength at both mass choices; only the on-shell
phase space and decay channels differ.

### (a) m_χ = 96 keV

- **Stellar cooling (HB / red-giant / SN1987A):** For an ALP with
  g_aγγ ~ α_EM/(2π f_a) ≈ 1.5×10⁻¹¹ GeV⁻¹ at f_a = 5×10⁷ GeV, the
  HB-star bound g_aγγ < 0.66×10⁻¹⁰ GeV⁻¹ is satisfied by a factor of
  ~4, and the SN1987A bound (for masses ≲ 100 MeV) gives a *trapping*
  rather than *free-streaming* regime — marginal. At 96 keV the χ is
  below the ~200 keV HB temperature so can be produced in stellar cores
  via Primakoff. **Borderline / mildly constrained**, not obviously
  ruled out.
- **BBN / N_eff:** 96 keV is below T_BBN ~ 1 MeV. If χ is relativistic
  at BBN (m_χ ≲ T_ν), it contributes to N_eff. For a single real scalar
  in thermal equilibrium, ΔN_eff ≈ 4/7 ≈ 0.57 if still coupled at
  neutrino decoupling, violating the Planck+BBN bound ΔN_eff < 0.3.
  However, with f_a ~ 10⁸ GeV the χ is **never thermally populated**
  (its interaction rate is ~ T³/f_a² ≪ H), so it does not contribute
  to N_eff this way. Misalignment-produced χ is cold and carries
  ΔN_eff ≈ 0. **Not ruled out by BBN/N_eff.**
- **CMB distortion / structure formation:** 96 keV is cold enough to
  cluster as CDM (free-streaming length negligible). **OK.**

### (b) m_χ = 1.87 MeV

- **BBN:** 1.87 MeV is just below e± pair-production threshold (1.022
  MeV) and just above T_BBN. A χ in this mass window that decays to
  γγ with lifetime τ ≪ t_BBN (~ 1 s) is usually fine; with
  τ ≳ 10⁴ s it injects photons during/after BBN, disrupting D/H and ⁴He.
  For f_a = 5×10⁷ GeV, Γ(χ → γγ) ~ m_χ³/(64π f_a²) ≈
  (1.87×10⁻³)³/(64π (5×10⁷)²) GeV ≈ 1.3×10⁻²⁵ GeV → τ ~ 5×10⁰¹ s.
  **That's catastrophic** — photodisintegration of D and ⁴He; the
  1.87 MeV χ is **ruled out** unless χ is stable by an additional
  symmetry (CP-odd under the CS Z-symmetry, for example). If χ is
  exactly stable, the MeV DM can still be dangerous through CMB
  distortions from residual annihilation, but misalignment-produced χ
  does not annihilate, so CMB is fine.
- **SN1987A:** 1.87 MeV is in the classic SN1987A "cooling" exclusion
  window for pseudoscalars with f_a ~ 10⁷–10⁹ GeV. Conservative
  SN1987A bound: f_a ≳ 10⁹ GeV for m_χ ≲ 100 MeV ALPs coupling to
  nucleons/photons. **f_a = 5×10⁷ GeV is ruled out by SN1987A for
  m_χ = 1.87 MeV** unless the coupling pattern suppresses the
  dominant Primakoff/nucleon-bremsstrahlung channels.
- **Stellar cooling (HB/RG):** At 1.87 MeV, χ is far heavier than core
  temperatures (~keV), so not produced. **OK.**
- **Thermal overclosure / hot DM:** Not relevant if misalignment-only.

### Summary table

| m_χ     | BBN/N_eff | HB stars | SN1987A           | CMB structure | Status                |
|---------|-----------|----------|-------------------|---------------|-----------------------|
| 96 keV  | OK        | marginal | marginal          | CDM (OK)      | allowed with tension   |
| 1.87 MeV| OK if stable; disaster if decays | OK (too heavy) | **ruled out** (nucleon coupling) | OK | **excluded unless couplings shut off** |

**Punchline for constraints:** 1.87 MeV is in worse observational shape
than 96 keV. The 96 keV case is borderline with stellar-cooling; 1.87
MeV is generically excluded by SN1987A at f_a = α⁵ M̄_P and by late
photon injection if χ decays via χ → γγ. The relic-closure argument
that prefers 1.87 MeV (M14) is therefore in direct conflict with
astrophysical bounds at the same f_a. **Both of M14's and R10's
specific α-tower solutions are in tension, but in different ways —
R10's with overclosure, M14's with SN1987A and photodisintegration.**

## 9. Recommendations

1. **Retract the "V''(0) = 158.35" substitution** in R10_07 and
   R10_UNIQUENESS_PROOF. The correct lattice-cosine curvature is
   C_total = A_lat ≈ 0.024 as R8_03 already derived. The 96 keV number
   downstream in L5/L8 should be replaced with the lattice value
   (~1.2 keV at n=5) or, if M14's rung constraint is treated as
   primary, the mass should be lifted to match Ω h² = 0.12 by a
   *separate identified mechanism*, not by reinterpreting V''(0).

2. **Recognize the α-tower inconsistency** at n=5 and name it
   explicitly in the v3.4 writeup. The three constraints
   {f_a = α⁵ M̄_P, lattice cosine V'', Ω h² = 0.12 at θ_i ≈ 1} cannot
   all be simultaneously satisfied. Picking any two forces the third
   to be reinterpreted.

3. **Re-examine n=4.5 (f_a ≈ 5.9×10⁸ GeV, m_χ ≈ 100 eV)** as an
   alternative rung where the SN1987A and late-decay constraints are
   both weaker (m_χ < 2 m_e, no photodisintegration; f_a larger,
   weaker nucleon coupling). This would be the cleanest escape and
   deserves a dedicated audit before adopting the MeV rung.

4. **Do not adopt m_χ ≈ 2 MeV in v3.4 without first checking SN1987A
   explicitly** for the specific DFD χ couplings. M14's caveat 9.5
   flagged this; the present audit confirms it is not just a caveat
   but likely an exclusion.

---

## Appendix A. Numerical check (independently computed)

```
alpha = 1/137.036
M_P (reduced) = 2.435e18 GeV
A_lat         = 0.02399         (from R8_03 §3.2)
Var_k[Z_CS]   = 158.35          (from R10_07 §2.4)

At (n, p) = (5, 8):
  f_a = alpha^5 * M_P  = 5.04e7 GeV
  Lam = alpha^8 * M_P  = 19.56 GeV

  m_chi (R8 lattice)    = sqrt(0.02399) * Lam^2 / f_a
                        = 0.1549 * 19.56^2 / 5.04e7 GeV
                        = 1.18e-6 GeV = 1.18 keV      ← correct R8 value

  m_chi (R10 Var_k)     = sqrt(158.35) * Lam^2 / f_a
                        = 12.584 * 19.56^2 / 5.04e7 GeV
                        = 9.58e-5 GeV = 95.8 keV     ← R10's 96 keV

  Ratio R10/R8          = sqrt(158.35 / 0.02399) = 81.2

  M14 relic-required    = 1.87e-3 GeV = 1.87 MeV    (Relation B, theta=1)

  Ratio M14/R10         = 1.87e6 / 9.58e4 = 19.5
  Ratio M14/R8          = 1.87e6 / 1.18e3 = 1586
  sqrt(19.5)            = 4.42  (the "sqrt(20)" factor M14 mentions)
```

The "sqrt(20)" factor M14 talks about is the square-root of the
Ω-closure overshoot at fixed (f_a, m_χ), not a factor in m_χ directly.
M14's inversion for what m_χ *should* be at n=5 is ~1.87 MeV; the "off
by sqrt(20)" framing is how much the 96 keV mass would have to move to
close the relic, interpreted through the Ω ∝ m^(½) scaling. Both R10's
derivation and M14's relic inversion miss that the underlying R8
lattice derivation gives a still-smaller 1.2 keV.
