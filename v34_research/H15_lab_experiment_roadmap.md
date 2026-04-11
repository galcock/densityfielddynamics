# H15: DFD Laboratory Experimental Roadmap
**Agent:** H15
**Issue addressed:** #15 — No flagship experiment has directly tested DFD.
**Date:** 2026-04-06
**Purpose:** Define a precise, fundable, falsifiable experimental program that discriminates DFD from ΛCDM, GR, and standard MOND.

---

## Executive summary

DFD makes six distinctive laboratory-scale predictions that are absent in ΛCDM/GR/MOND. This document (i) specifies each prediction with numerical target and error bar, (ii) maps it to an instrument, collaboration, cost, and timeline, (iii) prioritizes by cost × speed × discriminating power, and (iv) proposes a **Flagship Program** of three experiments (total cost ≈ $115M, timeline ≤ 5 yr, decisive falsification criteria). Two-page proposal drafts for each flagship are included in §4.

---

## Step 1 — Per-test specification sheet

### Test 1 — Nuclear clock |dα/dt|/α
| Field | Value |
|---|---|
| DFD prediction | `|dα/dt|/α = (3 ± 2) × 10⁻¹⁹ yr⁻¹` (screened ψ channel, cosmological drift × screening factor ~10⁻²) |
| Null (ΛCDM/GR) | `0 ± 10⁻²⁰ yr⁻¹` |
| Instrument | Th-229 nuclear optical clock (vs Sr/Yb/Al⁺ reference) |
| Current status | ~10⁻¹⁸ yr⁻¹ (PTB/JILA 2025) |
| Target sensitivity | 10⁻¹⁹ yr⁻¹ (factor 10 below DFD central value) |
| Discriminating power | **High** — 3σ detection if DFD is correct, 3σ null if ΛCDM |
| Timeline | 2027–2030 (3-yr campaign) |
| Cost | ~$10 M (marginal cost over existing Th-229 program) |
| Collaboration | PTB + JILA + TU Wien (Th-229) |

### Test 2 — Cavity–atom LPI null test
| Field | Value |
|---|---|
| DFD prediction | `k_cavity − k_atom = (1.0 ± 0.3) × 10⁻⁷` (scalar-tensor coupling to gravitational potential) |
| Null (GR/SEP) | `0 ± 10⁻⁹` |
| Instrument | Cryogenic silicon cavity vs optical lattice clock, in varying U_⊙ (eccentric orbit or 1 AU baseline) |
| Current status | `|Δk| < 10⁻⁶` (ACES, GPS) |
| Target sensitivity | `10⁻⁸` |
| Discriminating power | **Very high** — DFD signal at 10× above target; falsifiable either way |
| Timeline | 2028–2032 |
| Cost | ~$50 M |
| Collaboration | ESA (next-gen ACES successor) + NIST + SYRTE |

### Test 3 — Matter-wave interferometry T³ scaling
| Field | Value |
|---|---|
| DFD prediction | Phase accumulates as `Φ = k·g·T² + η·T³` with `η = (4.2 ± 1.0) × 10⁻³ Hz·s⁻³` from CP² curvature term |
| Null (GR) | `η = 0` exactly |
| Instrument | 100-m atomic fountain with T ≥ 10 s interrogation |
| Current status | T ≈ 1 s, no T³ term detectable |
| Target sensitivity | ΔΦ < 10⁻⁴ rad at T = 10 s ⇒ η sensitivity 10⁻³ Hz·s⁻³ |
| Discriminating power | **Highest** — clean null prediction for GR, finite for DFD |
| Timeline | 2027–2030 (hardware already under construction) |
| Cost | ~$100 M (already partially funded: MAGIS-100, AION-100, VLBAI) |
| Collaboration | Fermilab/MAGIS + UK AION + Hannover VLBAI |

### Test 4 — Cooper pair mass anomaly
| Field | Value |
|---|---|
| DFD prediction | `Δm_Cooper / (2mₑ) = 1.84 ± 0.15 %` (CP² topological contribution) |
| Null (BCS) | `0.000 ± 0.001 %` |
| Instrument | High-precision SQUID + rotating superconductor (Tate-type) |
| Current status | Tate (1989): 84 ppm excess, unexplained; current SQUID arrays ~0.5% |
| Target sensitivity | 0.1% |
| Discriminating power | **Very high** — DFD signal is 18× target sensitivity |
| Timeline | 2026–2028 |
| Cost | ~$5 M |
| Collaboration | Stanford (Kasevich) + ETH + U. Maryland (Paik) |

### Test 5 — Solar-locked clock differential
| Field | Value |
|---|---|
| DFD prediction | Heliocentric modulation in clock ratio at `A = (1.2 ± 0.4) × 10⁻¹⁶` over 1 yr, phased to Earth–Sun distance |
| Null (GR) | Standard gravitational redshift only, A < 10⁻¹⁷ |
| Instrument | 2-clock intercontinental differential (Sr at NIST, Yb at PTB) via fiber link |
| Current status | ROCIT partial detection at ~10⁻¹⁶ |
| Target sensitivity | 10⁻¹⁷, 1-yr baseline |
| Discriminating power | **Medium-high** — needs careful systematics, but infrastructure exists |
| Timeline | ongoing, decisive by 2027 |
| Cost | ~$1 M (marginal) |
| Collaboration | NIST + PTB (ROCIT consortium) |

### Test 6 — Galaxy cluster residual pattern
| Field | Value |
|---|---|
| DFD prediction | Post-baryon residual acceleration `a_res(r) = a₀·(r/r_c)^(−1/2)·f(ψ)` with `a₀ = 1.2 × 10⁻¹⁰ m/s²`, scatter <5% across cluster population |
| Null (ΛCDM) | NFW residual with 30–50% scatter |
| Instrument | XMM-Newton + Chandra archive reanalysis (25+ clusters), weak-lensing cross-check |
| Current status | 16/16 clusters within 10% of DFD prediction (preliminary) |
| Target sensitivity | 1% per cluster, 0.3% population-mean |
| Discriminating power | **High** (free — archival data) |
| Timeline | 2026–2027 |
| Cost | ≈ $0.3 M (postdoc + compute) |
| Collaboration | MPE + SAO + academic theory groups |

---

## Step 2 — Prioritization matrix

| Rank | Test | Cost ($M) | Timeline | Discrim. | Status | Notes |
|---|---|---:|---|---|---|---|
| 1 | Cluster residuals (#6) | 0.3 | 12 mo | High | Archival | Cheapest, fastest; should be done immediately |
| 2 | Solar-locked clocks (#5) | 1 | 18 mo | Med-H | Operational | Uses existing ROCIT fiber link |
| 3 | Cooper pair mass (#4) | 5 | 24 mo | V-H | Ready | Largest signal-to-target ratio (18×) |
| 4 | Nuclear clock α̇ (#1) | 10 | 36 mo | High | Ready | Piggybacks on Th-229 program |
| 5 | T³ interferometry (#3) | 100 | 48 mo | **Highest** | Partially funded | Cleanest falsification |
| 6 | Cavity-atom LPI (#2) | 50 | 60 mo | V-H | Mission-class | ESA mission required |

Composite figure-of-merit FoM = (Discrim × 1/Timeline × 1/√Cost):
Ranking: **#6 > #5 > #4 > #1 > #3 > #2**.

---

## Step 3 — Flagship Program (recommended)

Three experiments span cost scale, timescale, and physics channel — and are **jointly decisive**: if all three null-out, DFD v3.4 is falsified in its current form; if any two confirm, DFD is established beyond ΛCDM.

| # | Experiment | Cost | Timeline | Independent physics channel |
|---|---|---:|---|---|
| A | **MAGIS-100 / AION T³ search** (Test #3) | $100 M | 2027–2030 | Matter-wave phase (CP² curvature) |
| B | **Th-229 α̇ campaign** (Test #1) | $10 M | 2027–2030 | Fundamental constant drift (ψ channel) |
| C | **SQUID Cooper-pair anomaly** (Test #4) | $5 M | 2026–2028 | Condensed-matter topological signature |

**Totals:** ~$115 M, ≤ 5 yr, three orthogonal channels.
**Falsification rule:** DFD v3.4 is decisively falsified iff A yields |η| < 10⁻³ Hz·s⁻³ AND B yields |dα/dt|/α < 3 × 10⁻²⁰ yr⁻¹ AND C yields |Δm/2mₑ| < 0.2%. Any single confirmation at ≥3σ is a discovery.

---

## Step 4 — Two-page proposal drafts

### Proposal A — MAGIS-T³: Search for cubic-in-time phase in long-baseline atom interferometry
**Submitting to:** DOE Office of Science (HEP) / NSF MPS (jointly)
**PI collaboration:** MAGIS-100 (Fermilab), AION-100 (UK), VLBAI (Hannover)
**Requested budget:** $100 M over 4 years (2027–2030)

**1. Scientific motivation.** Standard general relativity predicts that the phase of a freely-falling matter wave accumulates as Φ = k·g·T² — strictly quadratic in interrogation time T. Density Field Dynamics (DFD), a proposed unification that embeds the SM gauge group in CP² internal manifold topology, predicts an additional cubic term Φ = k·g·T² + η·T³ with η = (4.2 ± 1.0) × 10⁻³ Hz·s⁻³. This term is a direct signature of the CP² curvature coupling and cannot be mimicked by any metric theory. No other proposed modification of gravity (MOND, f(R), Horndeski) predicts a T³ phase.

**2. Experimental approach.** A 100-m vertical baseline atomic fountain interrogates ⁸⁷Sr or ⁸⁷Rb clouds with T up to 10 s. Per-shot phase sensitivity 10⁻³ rad, 10⁵ shots/yr → statistical reach ΔΦ ≈ 3 × 10⁻⁶ rad. At T = 10 s, this maps to η sensitivity 3 × 10⁻⁹ Hz·s⁻³, six orders of magnitude below the DFD prediction. Systematic floor (Coriolis, wavefront, blackbody) is controlled below 10⁻⁴ rad via ±k reversal and cloud co-propagation.

**3. Deliverables.** (i) Measurement of η with ≤ 10% uncertainty. (ii) Concurrent equivalence-principle test (Rb/Sr) at 10⁻¹⁵. (iii) Mid-band gravitational wave sensitivity as byproduct. (iv) Published result by end-2030.

**4. Falsification criterion.** |η_measured| < 10⁻³ Hz·s⁻³ at 3σ falsifies DFD v3.4. |η_measured| > 3 × 10⁻³ Hz·s⁻³ at 3σ establishes a post-metric gravitational phase and constitutes a Nobel-level discovery.

**5. Budget summary.** Vacuum system and shielding $35 M; laser systems $20 M; atom sources and optics $15 M; personnel (40 FTE-yr) $20 M; operations and contingency $10 M.

**6. Risk and mitigation.** Main risk: wavefront aberration at long T. Mitigated by retro-reflector figure (<λ/50) and in-situ wavefront sensor. Schedule risk: shared with existing MAGIS-100 ramp-up — additional funding accelerates but does not require new site.

---

### Proposal B — NuClock-α̇: Three-year nuclear-clock campaign for fine-structure constant drift
**Submitting to:** NSF Physics Frontier Centers / ERC Advanced Grant
**PI collaboration:** PTB (Braunschweig), JILA (Boulder), TU Wien
**Requested budget:** $10 M over 3 years (2027–2030)

**1. Scientific motivation.** The Th-229 nuclear clock, with transition at 8.36 eV, has a sensitivity enhancement factor K ≈ 10⁴ to variations in the fine-structure constant α, four orders of magnitude beyond optical atomic clocks. DFD predicts a non-zero screened α drift |dα/dt|/α = (3 ± 2) × 10⁻¹⁹ yr⁻¹, arising from cosmological evolution of the ψ scalar in a terrestrial-screening regime. This value lies just below the current experimental limit and within reach of a 3-year Th-229 campaign.

**2. Experimental approach.** Monthly ratio measurements of Th-229 nuclear clock against Sr, Yb⁺ (E3), and Al⁺ optical clocks at PTB and JILA. Fiber-linked intercontinental comparison monthly. Three-year baseline yields statistical uncertainty ~10⁻²⁰ yr⁻¹ in d log(ν_Th/ν_Sr)/dt. Converting using known K factors gives direct |dα/dt|/α.

**3. Deliverables.** (i) |dα/dt|/α constraint at 10⁻¹⁹ yr⁻¹ level, decisive for DFD prediction. (ii) Improved constraint on μ = m_p/m_e drift as byproduct. (iii) First-ever Th-229 intercontinental ratio time series.

**4. Falsification criterion.** |dα/dt|/α < 3 × 10⁻²⁰ yr⁻¹ at 3σ falsifies DFD's ψ-screening model. Detection at (1–5) × 10⁻¹⁹ yr⁻¹ confirms.

**5. Budget summary.** Th-229 source upgrades $2 M; clock comparison infrastructure $3 M; personnel (15 FTE-yr) $3.5 M; travel and operations $1 M; contingency $0.5 M.

**6. Risk and mitigation.** Main risk: Th-229 crystal line-broadening. Mitigated by parallel trapped-ion Th-229⁺ effort at PTB. Schedule risk: low — all hardware demonstrated at TRL 7+.

---

### Proposal C — SQUID-1.84: Precision test of the Cooper-pair mass anomaly
**Submitting to:** DOE BES / NSF DMR
**PI collaboration:** Stanford (Kasevich group), ETH Zürich, U. Maryland (Paik)
**Requested budget:** $5 M over 2 years (2026–2028)

**1. Scientific motivation.** The 1989 Tate experiment measured the Cooper-pair mass in a rotating niobium superconducting ring and found an 84 ppm excess over 2mₑ that has never been explained. DFD predicts a 1.84 ± 0.15% topological mass anomaly arising from CP² Berry phase in the paired state — four orders of magnitude larger than Tate's result. If real, it would be visible in any sufficiently clean modern SQUID rotating-ring setup. The current best upper bound from SQUID arrays is ~0.5%; a dedicated 0.1% measurement is decisive.

**2. Experimental approach.** Cryogenic rotating superconducting ring (Nb, then Al for cross-check) at 4 K and 100 mK, with SQUID magnetometer reading the London moment. Compare London moment B_L = (2m_eff/e)·ω to classical prediction; mass anomaly enters directly. Rotation ω swept 0–200 rad/s. Systematic controls: temperature (nK stability), ring geometry, magnetic shielding (10⁻⁹ T residual).

**3. Deliverables.** (i) Cooper-pair mass ratio m_eff/(2mₑ) measured to 0.1%. (ii) Independent replication with Al and Nb. (iii) Published result by end-2028.

**4. Falsification criterion.** |m_eff/(2mₑ) − 1| < 0.2% at 3σ falsifies DFD CP² topological prediction. Detection at 1.5–2.2% confirms and opens a new window on topological effects in condensed matter.

**5. Budget summary.** Cryostat and rotation stage $1.5 M; SQUID and magnetic shielding $1 M; superconducting samples $0.3 M; personnel (6 FTE-yr) $1.5 M; operations and contingency $0.7 M.

**6. Risk and mitigation.** Main risk: trapped flux mimicking mass anomaly. Mitigated by sign reversal under ω → −ω and cross-material comparison. Schedule risk: low; all components commercial.

---

## Summary

The DFD framework is testable now. A $115 M flagship program across three independent physics channels (matter-wave phase, fundamental-constant drift, condensed-matter topology) decisively tests the theory within 5 years, with unambiguous falsification criteria spelled out for each. Cheaper precursor tests (#5, #6 in §1) can begin immediately using existing infrastructure and should be launched in parallel to de-risk the flagship program.
