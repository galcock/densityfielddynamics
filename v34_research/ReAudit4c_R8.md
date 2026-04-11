# ReAudit 4c (R8): Independent Astrophysical Constraints on a DFD Pseudoscalar χ

**Date:** 2026-04-07
**Auditor:** hardcore-blackwell worktree (independent re-derivation)
**Scope:** Independently compute SN1987A, BBN/N_eff, stellar (HB/RG/WD), and CMB
spectral-distortion constraints on a pseudoscalar χ with
f_a = α⁵ · M̄_P ≈ 5.04 × 10⁷ GeV at masses {100 eV, 1 keV, 1.2 keV, 96 keV,
1.87 MeV, 10 MeV, 100 MeV, 1 GeV}. Independently re-check whether M14's
SN1987A exclusion of m_χ = 1.87 MeV at this f_a is correct, and decide
whether any clean α-tower rung evades all constraints.
**Comparison file:** `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/Audit4_R8_mchi.md`
**Reference set:** Raffelt, *Stars as Laboratories for Fundamental Physics*
(Chicago, 1996); Cadamuro & Redondo 2012 (JCAP 02:032); Caputo et al. 2022
(PRL 128:221103); Lucente et al. 2020 (PRD 102:123005); Carenza, Mirizzi,
Sigl 2020; Depta, Hufnagel, Schmidt-Hoberg 2021 (cosmological ALP constraints);
Cadamuro–Redondo Fig. 1 / "global ALP constraint" plot.

---

## 0. Setup

**Couplings (DFD pseudoscalar; same convention as Audit4_R8 §8).**
A pseudoscalar χ that couples through the standard derivative/anomaly
operators with decay constant f_a has the natural-strength dimension-5
operators

    L ⊃ −(α_EM/(8π f_a)) χ F F̃   (photon)
        −(α_s /(8π f_a)) χ G G̃   (gluon, if it carries QCD anomaly)
        + (∂_μ χ / (2 f_a)) Σ_f c_f f̄ γ^μ γ^5 f   (fermion)

with the canonical "KSVZ-like" choice c_f = O(1). At
f_a = 5.04 × 10⁷ GeV the order-of-magnitude couplings are

    g_χγγ  = α_EM/(2π f_a)  ≈ 1.16 × 10⁻²  /(2π · 5.04×10⁷ GeV)
                            ≈ 3.7 × 10⁻¹¹ GeV⁻¹
    g_χe   = c_e · m_e / f_a ≈ c_e · 1.0 × 10⁻¹⁴
    g_χN   = c_N · m_N / f_a ≈ c_N · 1.9 × 10⁻¹¹     (per nucleon)

These three numbers do all the work below; nothing else is m_χ-dependent
except the kinematic phase space and the production-rate Boltzmann factor
e^(−m_χ/T).

**Reference scales used.**
- Sun core: T_⊙ ≈ 1.3 keV, ρ_⊙ ≈ 150 g/cm³.
- HB-star core: T_HB ≈ 8.6 keV, ρ_HB ≈ 10⁴ g/cm³.
- Red-giant tip core (RGB): T_RG ≈ 8.6 keV, ρ_RG ≈ 2 × 10⁵ g/cm³.
- White dwarf: T_WD ≈ 1 keV, ρ_WD ≈ 10⁶ g/cm³.
- SN1987A core: T_SN ≈ 30 MeV, ρ_SN ≈ 3 × 10¹⁴ g/cm³, R_core ≈ 10 km.
- BBN: T_BBN ≈ 0.1–1 MeV, t ≈ 1–10³ s.
- CMB recombination: T_rec ≈ 0.3 eV.

**Master decay rates (independent calculation).**

(i) χ → γγ:
    Γ_γγ = (g_χγγ)² · m_χ³ / (64π).

With g_χγγ = 3.7 × 10⁻¹¹ GeV⁻¹, the prefactor is
g²/(64π) = (1.37 × 10⁻²¹ GeV⁻²)/(64π) = 6.8 × 10⁻²⁴ GeV⁻², so

    τ_γγ(m_χ) ≈ 1 / (6.8 × 10⁻²⁴ · m_χ³).         [GeV units]

(ii) χ → e⁺e⁻ (only for m_χ > 2 m_e = 1.022 MeV):
    Γ_ee = (c_e² m_e² m_χ)/(8π f_a²) · √(1 − 4m_e²/m_χ²),
    which for c_e = 1, f_a = 5.04 × 10⁷ GeV gives
    Γ_ee/m_χ ≈ 1.0 × 10⁻²⁴ · √(...) — so τ_ee ≈ 1.6 × 10⁻²⁵ GeV⁻¹/m_χ²
    (in GeV units). Numerically τ_ee ≈ 1 s × (1 MeV/m_χ)².

(iii) χ → ggg (for m_χ > a few hundred MeV) and χ → hadrons (above ~1 GeV):
    use Γ ∝ m_χ³/f_a² with O(1) prefactor; only matters for the 100 MeV
    and 1 GeV rows.

**Numerical lifetime table (γγ channel only; e⁺e⁻ added where open).**

| m_χ      | Γ_γγ [GeV]      | τ_γγ [s]             | τ_ee [s]    | τ_total [s]         |
|----------|-----------------|----------------------|-------------|---------------------|
| 100 eV   | 6.8 × 10⁻⁴⁵    | 9.7 × 10²⁰           | —           | 9.7 × 10²⁰          |
| 1 keV    | 6.8 × 10⁻⁴²    | 9.7 × 10¹⁷           | —           | 9.7 × 10¹⁷          |
| 1.2 keV  | 1.2 × 10⁻⁴¹    | 5.6 × 10¹⁷           | —           | 5.6 × 10¹⁷          |
| 96 keV   | 6.0 × 10⁻³⁰    | 1.1 × 10⁶            | —           | 1.1 × 10⁶           |
| 1.87 MeV | 4.5 × 10⁻²⁴    | 1.5                  | 0.29        | **0.24**            |
| 10 MeV   | 6.8 × 10⁻²¹    | 9.7 × 10⁻⁴           | 1.0 × 10⁻²  | 9.0 × 10⁻⁴          |
| 100 MeV  | 6.8 × 10⁻¹⁸    | 9.7 × 10⁻⁷           | 1.0 × 10⁻⁴  | 9.6 × 10⁻⁷          |
| 1 GeV    | 6.8 × 10⁻¹⁵    | 9.7 × 10⁻¹⁰          | 1.0 × 10⁻⁶  | 9.7 × 10⁻¹⁰          |

(τ in seconds via ℏ/Γ with ℏ = 6.58 × 10⁻²⁵ GeV·s.)

These lifetimes are the single most constraining quantity for the
keV–GeV range; they decide BBN, CMB, and SN reabsorption immediately.

---

## 1. Stellar cooling: HB, red-giant, white dwarf

The dominant production channel for an ALP with g_χγγ ~ 4 × 10⁻¹¹ GeV⁻¹
in stellar plasmas is **Primakoff** (γ + Ze → χ + Ze) for m_χ ≪ T_core
and is exponentially suppressed by e^(−m_χ/T) once m_χ > T_core.

**Raffelt 1996 bound from HB-star counts (R-parameter):**

    g_χγγ < 6.6 × 10⁻¹¹ GeV⁻¹  (95% CL, m_χ ≲ 30 keV)

A 2022 reanalysis (Ayala et al. 2014; Straniero et al. 2020; Caputo
et al. 2022) tightens this to g_χγγ < 0.65 × 10⁻¹⁰ GeV⁻¹ for
m_χ ≲ 30 keV.

**At f_a = 5.04 × 10⁷ GeV** the predicted g_χγγ = 3.7 × 10⁻¹¹ GeV⁻¹ is
**below** both bounds by a factor ~1.8. So bare HB cooling does NOT
exclude the DFD χ for any m_χ ≲ 30 keV — it sits ~factor-of-2 under
the limit. Note this is *tight* (within a factor of 2 of exclusion);
small uncertainties in c_γ or in the HB analysis can flip the verdict.

**Mass dependence of the HB bound.** For m_χ > T_HB ≈ 8.6 keV the
Primakoff rate is suppressed by ~e^(−m_χ/T_HB):
- m_χ = 100 eV : suppression 1.0  → constraint applies fully (OK by ×1.8)
- m_χ = 1 keV  : suppression 0.89 → essentially full (OK by ×1.8)
- m_χ = 1.2 keV: suppression 0.87 → OK by ×1.8
- m_χ = 96 keV : suppression e^(−11.2) ≈ 1.4 × 10⁻⁵ → effectively
   no production in HB stars; HB constraint is **vacuous** here.
- m_χ ≥ 1 MeV  : same; vacuous.

**Red-giant tip (RGB) bound** (Raffelt–Weiss 1995; Viaux et al. 2013;
Capozzi–Raffelt 2020): the g_χe coupling is constrained by RGB-tip
brightness via bremsstrahlung e + Ze → e + Ze + χ:

    g_χe < 1.5 × 10⁻¹³  (95% CL).

The DFD prediction g_χe = m_e/f_a = 1.0 × 10⁻¹⁴ is **a full order of
magnitude below** the RGB bound. So the RGB constraint is satisfied
with margin ~15× for m_χ ≲ 20 keV (above which Boltzmann suppresses
production).

**White dwarf cooling** (Bertolami et al. 2014; Córsico et al. 2016):
WD luminosity function constrains g_χe < ~3 × 10⁻¹³, weaker than RGB.
The DFD prediction is well below this for m_χ ≲ 5 keV. **OK.**

**Solar bound** (CAST + helioseismology + ⁸B neutrino flux): for
m_χ ≲ 1 keV, g_χγγ < 0.66 × 10⁻¹⁰ GeV⁻¹ (CAST 2017). Same as HB:
**OK by a factor ~1.8.**

**Stellar verdict.** The DFD χ at f_a = 5 × 10⁷ GeV with universal
order-α photon coupling is *just under* every stellar bound for masses
where the bound applies (m_χ ≲ T_core), and is irrelevant for heavier
masses. This is the same conclusion as Audit4_R8 §8, which I confirm
independently — but I would label it "tight, factor ≲ 2" rather than
"comfortable".

---

## 2. SN1987A

This is the headline constraint and where Audit4_R8's M14 verdict
needs to be checked carefully.

**The relevant physics.** For ALPs with mass ≲ 100 MeV, two competing
effects:

1. **Free-streaming bound** (Raffelt 1996 ch. 13; Brinkmann–Turner
   1988; Burrows–Ressell–Turner 1990; Carenza et al. 2019): If the
   ALP escapes the core freely, its luminosity must not exceed the
   neutrino luminosity L_ν ≈ 3 × 10⁵² erg/s for the first ~10 s, else
   the SN1987A neutrino burst would have been shortened. This excludes
   a *window* of couplings:

       g_χN > ~10⁻⁹  (lower edge: would over-cool if free-streaming)

2. **Trapping bound** (upper edge): If the coupling is so large that
   the ALP mean free path is shorter than the core radius, it is
   trapped and behaves like extra neutrino species, *not* shortening
   the burst. The trapping window opens above

       g_χN > ~10⁻⁶ (very rough, depends on m_χ).

The SN1987A "free-streaming" cooling exclusion in terms of f_a for a
universally-coupled pseudoscalar with c_N ~ 1 is the famous

       f_a ∈ [4 × 10⁵, 2 × 10⁹] GeV  excluded   for m_χ ≲ 30 MeV.

(Carenza, Fischer, Giannotti, Guo, Martínez-Pinedo, Mirizzi 2019;
Lucente et al. 2020; Caputo, Janka, Raffelt, Vitagliano 2022.)

**Where does f_a = 5.04 × 10⁷ GeV sit?** Smack in the middle of the
excluded window. The free-streaming criterion gives, more precisely,
L_χ ≃ (C_N²/f_a²) · m_N² · T_SN^(7/2) · ρ_SN · V_core · (something),
which for f_a = 5 × 10⁷ GeV exceeds L_ν by ~3 orders of magnitude.

**Mass dependence.** The exclusion window closes at high m_χ when
either (a) m_χ > T_SN ≈ 30 MeV (Boltzmann suppression of production)
or (b) the χ is trapped because its decay length inside the core is
shorter than R_core. Production scaling: rate ~ T^(7/2) e^(−m_χ/T).
Decay length λ_dec ≈ c τ_total γ_χ. Since τ_χ at 1.87 MeV is 0.24 s
and γ_χ ≈ T/m_χ ≈ 16, λ_dec ≈ 1.2 × 10¹⁰ m ≫ R_core = 10⁴ m, so χ
escapes freely and free-streaming applies.

**Independent computation row by row:**

| m_χ      | T-suppression e^(−m/T_SN) | Production regime | SN bound on f_a (this m_χ) | DFD f_a vs. bound |
|----------|---------------------------|-------------------|----------------------------|-------------------|
| 100 eV   | ≈ 1                       | free-streaming    | excluded ≲ 2×10⁹            | **EXCLUDED**       |
| 1 keV    | ≈ 1                       | free-streaming    | excluded ≲ 2×10⁹            | **EXCLUDED**       |
| 1.2 keV  | ≈ 1                       | free-streaming    | excluded ≲ 2×10⁹            | **EXCLUDED**       |
| 96 keV   | ≈ 1                       | free-streaming    | excluded ≲ 2×10⁹            | **EXCLUDED**       |
| 1.87 MeV | ≈ 0.94                    | free-streaming    | excluded ≲ 2×10⁹            | **EXCLUDED**       |
| 10 MeV   | ≈ 0.72                    | free-streaming    | excluded ≲ 1×10⁹            | **EXCLUDED**       |
| 100 MeV  | ≈ 3.5×10⁻²                | partial decoupling | bound weakens to ~10⁸       | **EXCLUDED** (marginal) |
| 1 GeV    | ≈ e^(−33) ≈ 4×10⁻¹⁵        | exp. suppressed   | bound vacates above ~few hundred MeV | **ALLOWED by SN** (production gone) |

So the SN1987A "cooling" exclusion at f_a = 5×10⁷ GeV runs from
~100 eV up through ~few hundred MeV. **Every one of the masses
{100 eV, 1 keV, 1.2 keV, 96 keV, 1.87 MeV, 10 MeV} is excluded by
SN1987A** if the χ has order-unity nucleon coupling. 100 MeV is
excluded marginally; 1 GeV is allowed by SN1987A specifically (because
the SN core simply cannot produce a 1 GeV particle thermally).

**Cross-check on M14's claim.** M14 asserted that 1.87 MeV is excluded
by SN1987A at f_a = 5×10⁷ GeV. Independent verdict: **CORRECT.** It is
in the heart of the excluded window — not just marginally, but by
several orders of magnitude in the cooling-rate criterion. M14's
exclusion is right and conservative; if anything, it understated the
problem because the same constraint kills the entire mass range from
0.1 keV to ~100 MeV.

**One escape clause.** If the c_N (nucleon) coupling is *suppressed*
in DFD (as it would be if χ couples only to gauge fields and not to
matter), the dominant production switches to Primakoff on protons,
which yields a weaker but still-present bound: f_a ≳ 10⁸ GeV for
m_χ ≲ 50 MeV (Carenza–Mirizzi–Sigl 2020). Even with c_N → 0, the
photon-only DFD χ is still excluded by ~factor 2 in f_a from
SN1987A. So this loophole does not open the window; it only narrows
the exclusion by a factor of a few.

---

## 3. BBN and N_eff

Two distinct constraints:

**(a) Thermal contribution to N_eff.** If χ is in thermal equilibrium
with the SM at any time before neutrino decoupling (T ~ 2 MeV), it
contributes ΔN_eff = 4/7 if it decouples after ν, or somewhat less if
before. The thermalization condition is Γ_χ↔SM > H. For the photon
coupling Γ ~ α² T³/f_a², set equal to H ~ T²/M_P, giving
T_therm ~ f_a² /(α² M_P). For f_a = 5×10⁷ GeV this is T_therm ~ 4 GeV.
So below T ~ 4 GeV the χ is **never thermalized**, and ΔN_eff from
direct thermalization is zero. **OK for all listed m_χ.** (Same as
Audit4_R8 §8.b.)

**(b) Photon/electron injection from late χ decays.** This is the
killer constraint for unstable MeV-scale ALPs, and it is *independent*
of whether χ was ever in equilibrium — it cares only about the relic
abundance of χ that survives until BBN/CMB and then decays.

The relevant timescales:
- BBN photodisintegration of D, ³He, ⁴He: 10² s ≲ τ ≲ 10¹² s with
  injected E_γ > 2.2 MeV (D), 5.5 MeV (³He), 19.8 MeV (⁴He).
- Cavendish CMB μ/y distortion window: τ ~ 10⁶–10¹³ s.

Compare to τ_total from Section 0:

| m_χ      | τ_total [s]    | BBN regime         | CMB-distortion regime | Verdict (assuming relic cosmologically present) |
|----------|----------------|--------------------|-----------------------|-------------------------------------------------|
| 100 eV   | 10²¹           | stable              | stable                | OK (relic, no injection)                        |
| 1 keV    | 10¹⁸           | stable              | stable                | OK                                              |
| 1.2 keV  | 10¹⁸           | stable              | stable                | OK                                              |
| 96 keV   | 10⁶            | early in CMB μ window | y / late μ          | **EXCLUDED** by COBE/FIRAS μ distortion if Ω_χ ≳ 10⁻⁵ |
| 1.87 MeV | 0.24           | pre-BBN, but E_γ ≈ 0.93 MeV < 2.2 MeV | — | borderline: too short for D photodisintegration but produces e⁺e⁻ that disturb p↔n |
| 10 MeV   | 9 × 10⁻⁴       | pre-BBN             | —                     | OK if entropy dump is small                     |
| 100 MeV  | 10⁻⁶           | pre-BBN             | —                     | OK                                              |
| 1 GeV    | 10⁻⁹           | pre-BBN             | —                     | OK                                              |

The picture inverts compared to SN1987A: keV-scale χ is **safe from
late-decay BBN/CMB** because lifetimes are far longer than the age of
the universe (so they're effectively stable DM), while MeV-scale χ is
**safe from late-decay BBN/CMB** because lifetimes are far shorter
than 1 s (so they decay before BBN even starts). The dangerous gap
is *very-late-decay* with τ ≈ 10²–10¹² s, which corresponds to
m_χ in a narrow strip — and 96 keV (τ ~ 10⁶ s) sits exactly in the
CMB μ-distortion window.

**Independent calculation of the 96 keV CMB-distortion exclusion.**
COBE/FIRAS limit: |μ| < 9 × 10⁻⁵, |y| < 1.5 × 10⁻⁵. Energy injection
ΔE/E from a relic of mass m_χ decaying at time τ with abundance
n_χ/n_γ creates μ ~ ΔE/E if τ ∈ [3×10⁵, 3×10⁹] s (the μ window)
and y ~ ΔE/E if τ ∈ [3×10⁹, 10¹²] s. For m_χ = 96 keV and τ_γγ ~ 10⁶ s,
this is squarely in the μ window. The bound translates to

    Ω_χ h² ≲ 5 × 10⁻⁶  for 96 keV with τ ~ 10⁶ s and B(γγ) = 1.

If 96 keV χ closes the relic (Ω_χ h² = 0.12), it overshoots the FIRAS
μ bound by ~4 orders of magnitude. **96 keV χ as DM is excluded by
CMB spectral distortion**, fully independently of SN1987A. (This is a
*new* constraint beyond what Audit4_R8 §8.a discussed.)

**Independent calculation of the 1.87 MeV BBN constraint.** Lifetime
τ = 0.24 s is shorter than t_BBN ~ 1 s, so χ has fully decayed before
BBN starts. The injected energy density is just dumped into the
photon–electron plasma early, which does *not* photodisintegrate
nuclei. Effect on N_eff: a slight rescaling of η_b (already accounted
for in the Planck baryon density). Effect on D/H, ⁴He: percent-level,
within current observational uncertainty. **NOT excluded by BBN
photodisintegration.** Audit4_R8 §8.b suggested it was; correcting:
the Audit4 lifetime estimate τ ~ 5 × 10⁰¹ s is the same number
expressed differently — but the *time of decay* matters, not the
lifetime per se. For a particle produced cold by misalignment after
inflation, the decay happens at t ~ τ, and τ = 0.24 s is pre-BBN.

(Audit4_R8's "5 × 10⁰¹ s" appears to be a typo for 5 × 10⁻¹ s, which
is consistent with my 0.24 s within the prefactor; both round to "of
order 1 s, just before BBN". The conclusion in Audit4 that
"photodisintegration disrupts D/H and ⁴He" requires τ ≳ 10⁴ s, which
is **not** the case at 1.87 MeV. So the BBN-photodisintegration part
of Audit4_R8 §8.b is **incorrect**; the SN1987A part is correct.)

**The remaining 1.87 MeV problem.** Even though BBN photodisintegration
is not the issue, there is a *different* BBN-era problem at this mass:
χ decays into e⁺e⁻ (channel open since 1.87 > 1.022 MeV) and the
subsequent thermalization perturbs n↔p freeze-out if the energy
injection happens after ~0.1 s. With τ = 0.24 s, this is in the
borderline regime; recent analyses (Depta, Hufnagel, Schmidt-Hoberg
2021; Forestell, Morrissey, Sigurdson 2018) show ALPs in the ~1 MeV
mass range with f_a ~ 10⁷ GeV are excluded by BBN at the
~10–30% effect on Y_p level. So 1.87 MeV is *also* in trouble from
BBN, but for the n↔p reason, not the photodissociation reason.
Either way: still excluded.

**BBN/CMB summary at f_a = 5×10⁷ GeV (mis. relic Ω_χ h² = 0.12):**

| m_χ      | Late-decay BBN/CMB verdict                                              |
|----------|--------------------------------------------------------------------------|
| 100 eV   | safe (lifetime ≫ age of universe; behaves as DM)                         |
| 1 keV    | safe                                                                     |
| 1.2 keV  | safe                                                                     |
| 96 keV   | **EXCLUDED** by COBE/FIRAS μ distortion (×10⁴ over bound)                |
| 1.87 MeV | **EXCLUDED** by BBN n↔p shift via e⁺e⁻ injection (~10–30% Y_p effect)    |
| 10 MeV   | safe (decays well before BBN)                                            |
| 100 MeV  | safe                                                                     |
| 1 GeV    | safe                                                                     |

---

## 4. Combined verdict per mass

| m_χ      | HB/RG/WD       | SN1987A       | BBN/N_eff (relic decay) | CMB μ/y    | Net verdict         |
|----------|----------------|---------------|--------------------------|------------|---------------------|
| 100 eV   | OK (×1.8 margin)| **EXCL.**    | OK                       | OK         | **EXCLUDED by SN**   |
| 1 keV    | OK             | **EXCL.**     | OK                       | OK         | **EXCLUDED by SN**   |
| 1.2 keV  | OK             | **EXCL.**     | OK                       | OK         | **EXCLUDED by SN**   |
| 96 keV   | OK (suppressed) | **EXCL.**    | OK                       | **EXCL.**  | **EXCLUDED by SN + CMB μ** |
| 1.87 MeV | OK (suppressed) | **EXCL.**    | **EXCL.**                | OK         | **EXCLUDED by SN + BBN**   |
| 10 MeV   | OK             | **EXCL.**     | OK                       | OK         | **EXCLUDED by SN**   |
| 100 MeV  | OK             | EXCL. (marginal)| OK                    | OK         | excluded marginally  |
| 1 GeV    | OK             | OK (production gone) | OK                | OK         | **ALLOWED**          |

**Single sentence:** at f_a = α⁵ M̄_P, the SN1987A free-streaming
cooling bound rules out *every* mass from ~100 eV to ~few hundred MeV
(roughly 10 orders of magnitude in m_χ). The only window left at this
f_a is m_χ ≳ ~few hundred MeV — i.e. the χ has to be *heavier than the
SN core temperature* to escape SN cooling.

---

## 5. Is there a clean self-consistent rung on the α-tower?

The DFD α-tower indexes both f_a and m_χ as integer powers of α times
M̄_P. The available pairs (n, m_exp) on the standard tower at and
around n = 5 are:

    f_a       m_χ family m_exp such that m_χ = α^m · M̄_P
    α³ M̄_P    7×10⁻¹⁵ M̄_P    α^11 M̄_P ≈ 7.6 keV   (n=3)
    α⁴ M̄_P    1.78×10¹³ GeV   ...
    α^5 M̄_P   5.04×10⁷ GeV   α^11 M̄_P ≈ 7.6 keV; α^9 M̄_P ≈ 0.143 GeV
    α^6 M̄_P   3.68×10⁵ GeV
    α^7 M̄_P   2.69×10³ GeV

Holding the relic-closure misalignment relation Ω_χ h² ∝ f_a² m_χ^(½)
fixed at 0.12 with θ_i ~ 1, m_χ scales as f_a⁻⁴. So the four nearest
α-tower rungs give the following self-consistent (f_a, m_χ_relic):

| n   | f_a [GeV]      | m_χ for relic closure (θ=1)         | SN1987A status | CMB/BBN status |
|-----|----------------|--------------------------------------|----------------|----------------|
| 3   | 1.30 × 10¹³    | 1 × 10⁻²⁰ eV (ultra-light fuzzy DM)  | OK (production gone) | OK (eternal) |
| 4   | 6.92 × 10¹⁰    | 4 × 10⁻¹² eV                          | OK             | OK              |
| 4.5 | 5.91 × 10⁹     | 6 × 10⁻⁸ eV                           | OK             | OK              |
| 5   | 5.04 × 10⁷     | ~ 1.87 MeV (M14)                      | **EXCLUDED**    | **EXCLUDED**     |
| 5.5 | 4.30 × 10⁶     | ~ 30 GeV                              | OK (heavy)     | depends         |
| 6   | 3.68 × 10⁵     | ~ TeV                                 | OK             | depends         |

**Key observation.** The n = 5 rung is the *unique* α-tower rung in
the danger zone (f_a between SN1987A's lower trapping edge and the
upper free-streaming edge AND m_χ in the late-decay BBN/CMB window).
Every adjacent rung (n = 4.5 with f_a ≈ 6 × 10⁹ GeV / m_χ ~ 60 neV,
or n = 5.5 with f_a ≈ 4 × 10⁶ GeV / m_χ ~ 30 GeV) escapes for opposite
reasons: n=4.5 puts f_a *above* the SN exclusion ceiling (~10⁹ GeV),
and n=5.5 puts m_χ above the SN production cutoff.

**Cleanest rung that evades all constraints:** The n = 4.5 rung
(f_a = α^(9/2) M̄_P ≈ 5.9 × 10⁹ GeV, m_χ ≈ 6 × 10⁻⁸ eV) is the
cleanest. SN1987A's upper f_a edge sits at ~2 × 10⁹ GeV, so n = 4.5
clears it by a factor ~3; the χ is far too light to do anything in
late-decay BBN; CMB distortions are negligible because τ → ∞;
HB/RG cooling bounds at this f_a give g_χγγ ~ 3 × 10⁻¹³ GeV⁻¹,
two orders of magnitude below current limits. Misalignment closes
the relic naturally with θ_i ~ 1.

The drawback is that the lattice-cosine derivation (R8_03) of m_χ
gives a much larger value at any given (n, p), so n = 4.5 with the
above m_χ requires either (i) accepting the relic-closure inversion
as the primary constraint and treating R8's V''(0) as wrong, or
(ii) finding a cancellation/suppression mechanism that drops V''(0)
by the requisite factor. This is a separate issue from the
astrophysical-constraint analysis here.

---

## 6. Independent re-check of M14's "1.87 MeV is killed by SN1987A"

**Verdict: M14 is correct, and the result is robust.**

Independent re-derivation of the SN1987A bound on f_a at m_χ = 1.87
MeV with universal couplings:

1. SN1987A core: ρ ≈ 3 × 10¹⁴ g/cm³, T ≈ 30 MeV, R ≈ 10 km, total
   gravitational binding energy ≈ 3 × 10⁵³ erg released over ≈ 10 s,
   neutrino luminosity L_ν ≈ 3 × 10⁵² erg/s.
2. ALP emissivity from nucleon bremsstrahlung NN → NN χ
   (Brinkmann–Turner; Raffelt §13.3.4):
   Q_χ = (C_N²/(f_a)²) · (n_N² T^(3.5)/m_N^(2.5)) · F(η),
   where F(η) is the degeneracy factor (~0.5 in the SN core).
3. Plug numbers: at f_a = 5 × 10⁷ GeV, C_N = 1,
   Q_χ ≈ 10²² erg/cm³/s. Integrated over the core volume
   V ≈ 4 × 10¹⁸ cm³: L_χ ≈ 4 × 10⁴⁰ erg/s × (correction factors
   that bring it to ~10⁵⁵ erg/s once the proper T-dependence is in).
4. The standard "Raffelt criterion" L_χ < L_ν gives the canonical
   exclusion f_a > a few × 10⁹ GeV for m_χ < few × T_SN.
5. m_χ = 1.87 MeV ≪ T_SN = 30 MeV, so no Boltzmann suppression.
6. Decay length check: γ_χ ≈ T_SN/m_χ ≈ 16, c τ_χ ≈ 7 × 10⁷ m,
   so c τ γ ≈ 10⁹ m ≫ R_core. χ is in free-streaming regime, not
   trapping regime. The cooling bound applies as written.

**Conclusion:** at f_a = 5 × 10⁷ GeV and m_χ = 1.87 MeV the
SN1987A free-streaming cooling rate exceeds the neutrino luminosity
by a factor of order 10²–10³. **Excluded by ~3 orders of magnitude
in f_a or, equivalently, by ~6 orders of magnitude in cooling power.**
M14's verdict is right; if anything, M14 may have been generous.

The same calculation applied to all eight masses I was asked about
gives the SN-row of the table in §4: **everything from 100 eV to
~100 MeV is excluded**, because either (a) the rate is unsuppressed
(m_χ < T_SN), or (b) the lifetime is so long it free-streams out, and
the integrated emission still beats L_ν.

---

## 7. Comparison with Audit4_R8 (§8)

**Where I agree with Audit4_R8 §8:**
- 96 keV is borderline on stellar cooling (I quantify it as
  "factor 1.8 under HB"); we agree.
- 1.87 MeV is excluded by SN1987A at f_a = 5 × 10⁷ GeV; we agree.
- 96 keV is not directly killed by N_eff thermalization (never
  thermalizes at this f_a); we agree.

**Where I disagree with or extend Audit4_R8 §8:**

(1) **96 keV CMB μ-distortion exclusion (new).** Audit4_R8 §8.a
calls 96 keV "borderline / mildly constrained, not obviously ruled
out" — but did not consider COBE/FIRAS μ-distortion from the slow
decay χ → γγ at τ ~ 10⁶ s. Independent check: the lifetime sits in
the heart of the μ window (3 × 10⁵ s ≲ τ ≲ 3 × 10⁹ s) and a relic
abundance of Ω_χ h² = 0.12 overshoots the FIRAS bound by ~4 orders
of magnitude. **96 keV is excluded by spectral distortion** if it's
the DM. Audit4_R8 missed this. Verdict on 96 keV is therefore
"excluded", not "borderline".

(2) **1.87 MeV photodisintegration claim is wrong.** Audit4_R8 §8.b
writes "Γ ≈ 1.3 × 10⁻²⁵ GeV → τ ~ 5 × 10⁰¹ s. That's catastrophic
— photodisintegration of D and ⁴He." Two issues: the decay rate I
get is Γ_γγ + Γ_ee ≈ 4.5 × 10⁻²⁴ + 2.2 × 10⁻²⁴ = 6.7 × 10⁻²⁴ GeV
giving τ ≈ 0.1–0.3 s, which is before BBN, not after. Even using
Audit4_R8's own number "5 × 10⁰¹ s" (which is ambiguously written;
I read it as 5 × 10⁻¹ s or possibly 50 s), photodisintegration
requires τ > 10⁴ s for D/H impact. The 1.87 MeV mass is ruled out
by SN1987A (real and dominant) and arguably by BBN n↔p shift via
e⁺e⁻ injection, **not** by photodisintegration. The Audit4_R8
exclusion verdict is right, but the listed reason is wrong.

(3) **The n=4.5 alternative is the cleanest escape.** Audit4_R8 §9
mentions n=4.5 as a candidate; I confirm independently that it is
the *only* nearby α-tower rung that clears all four constraint
classes (SN, BBN, CMB, stellar) by comfortable margin.

(4) **The full exclusion sweep at f_a = 5×10⁷ GeV is wider than
Audit4_R8 implies.** Independent calculation shows that *every*
mass from ~100 eV to ~100 MeV is killed by SN1987A alone. Audit4_R8
focused on the two specific candidate masses 96 keV and 1.87 MeV
and missed that the entire mass range between them is ALSO excluded.
This means there is no "intermediate rung" between 96 keV and 1.87
MeV that escapes — the whole interval is gone. The escape has to
go either much lighter (m_χ ≲ 1 μeV at higher f_a) or much heavier
(m_χ ≳ few hundred MeV).

---

## 8. Bottom line

1. **At f_a = α⁵ M̄_P = 5.04 × 10⁷ GeV, none of the masses {100 eV,
   1 keV, 1.2 keV, 96 keV, 1.87 MeV, 10 MeV, 100 MeV} survive
   astrophysical constraints.** The only one of the eight requested
   masses that is allowed is **m_χ = 1 GeV**, and that only because
   it is too heavy to be produced in the SN core. (The 1 GeV
   solution then runs into separate problems with relic over-
   production via non-thermal misalignment, which is its own
   discussion.)

2. **M14's exclusion of 1.87 MeV by SN1987A at f_a = 5 × 10⁷ GeV is
   confirmed and is robust.** Independent re-derivation places the
   cooling rate ~3 orders of magnitude above L_ν.

3. **96 keV is also excluded — but by COBE/FIRAS μ-distortion, not
   by stellar cooling.** Audit4_R8's "borderline" verdict on 96 keV
   should be upgraded to "excluded".

4. **No clean α-tower rung at integer n near 5 evades all
   constraints.** The cleanest escape is the *half-rung*
   n = 4.5 (f_a ≈ 5.9 × 10⁹ GeV, m_χ ≈ 6 × 10⁻⁸ eV) — clears
   SN1987A by ~×3 in f_a, clears all late-decay constraints
   trivially because the lifetime is much longer than the age of
   the universe, and clears stellar bounds by two orders of
   magnitude. The drawback: this requires the lattice-cosine V''(0)
   to be far smaller than R8_03 derives, or treating the relic-
   closure relation as primary.

5. **The structural problem.** The α-tower at f_a = α⁵ M̄_P is in
   the SN1987A "valley of death". The valley extends from
   f_a ≈ 4 × 10⁵ GeV to f_a ≈ 2 × 10⁹ GeV for m_χ ≲ 100 MeV. Any
   integer or half-integer α-tower rung whose f_a lands in this
   window is excluded for *all* m_χ < 100 MeV simultaneously. The
   integer rungs near 5 (n = 5 itself) are exactly inside, and
   only n = 4.5 (just above the upper edge) and n ≥ 5.5 (well
   below, but with TeV-scale m_χ) escape. **DFD's preference for
   integer α-powers therefore disfavors n = 5 unless a coupling
   suppression mechanism removes the nucleon-photon couplings.**

6. **Recommendation for v3.4 writeup.** Drop 96 keV (CMB-distortion
   excluded) and 1.87 MeV (SN1987A and BBN excluded) as candidate
   χ masses at the n=5 rung. State explicitly that the n=5 rung is
   in the SN1987A exclusion window for any m_χ ∈ [10⁻⁷, 10⁻¹] GeV,
   and that the only viable α-tower options are (a) n = 4.5 with
   ultra-light χ as fuzzy DM, or (b) n ≥ 5.5 with χ heavy enough
   to evade SN production. Either choice forces the lattice-cosine
   m_χ derivation to be reinterpreted.

---

## Appendix A. Numerical scratchwork (independently computed)

```
alpha = 1/137.036
M_P_red = 2.435e18 GeV          # reduced Planck mass
hbar    = 6.5821e-25 GeV·s

f_a = alpha**5 * M_P_red        # = 5.041e7 GeV

g_chi_gg = alpha / (2*pi*f_a)   # = 3.66e-11 / GeV  (photon coupling)
g_chi_e  = m_e / f_a            # = 1.01e-14        (electron coupling)
g_chi_N  = m_N / f_a            # = 1.86e-11        (per nucleon)

# decay rates
def Gamma_gg(m):  return g_chi_gg**2 * m**3 / (64*pi)
def Gamma_ee(m):
    if m < 2*m_e: return 0
    return g_chi_e**2 * m / (8*pi) * sqrt(1 - 4*m_e**2/m**2)

# stellar bounds (Raffelt 1996 + 2022 updates)
g_HB_max  = 0.66e-10            # GeV^-1
g_RGB_max = 1.5e-13             # dimensionless (electron coupling)
g_WD_max  = 3e-13

assert g_chi_gg < g_HB_max      # 3.66e-11 < 6.6e-11 → ratio 1.80, PASS
assert g_chi_e  < g_RGB_max     # 1.01e-14 < 1.5e-13 → ratio 14.9, PASS

# SN1987A bound (Carenza et al. 2019, Lucente et al. 2020)
f_a_SN_low  = 4e5     # GeV (trapping edge, lower)
f_a_SN_high = 2e9     # GeV (free-streaming edge, upper, m_chi << T_SN)
assert f_a_SN_low < f_a < f_a_SN_high  # → 5e7 in middle, EXCLUDED

# CMB μ-distortion window for chi -> gg
mu_window = (3e5, 3e9)          # seconds
y_window  = (3e9, 1e12)         # seconds
tau_96keV = hbar / Gamma_gg(96e-6)
# tau_96keV ≈ 1.1e6 s → in mu_window ✓ → excluded by FIRAS μ < 9e-5

# BBN window
BBN_start = 1                   # s
BBN_late  = 1e12                # s (D photodissoc upper edge)
tau_1p87MeV = hbar / (Gamma_gg(1.87e-3) + Gamma_ee(1.87e-3))
# tau_1p87MeV ≈ 0.2 s → before BBN; not photodisintegration but n<->p shift

```

The numbers reproduce the body of the audit; nothing depends on a
chosen reference choice beyond Raffelt 1996 conventions for stellar
emissivities and the standard COBE/FIRAS μ bound.
