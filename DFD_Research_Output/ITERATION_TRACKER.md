# DFD RESEARCH PROGRAMME — ITERATION TRACKER

**Programme**: Wave 3 (20-iteration deep cross-reference cycle)
**Patent corpus**: 15 patents + Cosmology module + Materials Science module = 17 research streams
**Compiler**: Automated agent compiler
**Last updated**: 19 March 2026

---

## ITERATION STATUS SUMMARY

| Iteration | Status | Date | Key Output |
|-----------|--------|------|-----------|
| W3i1 | COMPLETE | 2026-03-19 | Baseline cross-references; 15×15 patent interaction table; μ_0 correction |
| W3i2 | COMPLETE | 2026-03-19 | μ_0=0.652 corrected; ESS Lund bound; psi-QEC threshold; mode-mass flagged |
| W3i3 | COMPLETE | 2026-03-19 | Part XII appended; 4.0 ns bubble signal; S8/Cold Spot tensions identified; n_ψ→√2 |
| **W3i4** | **COMPLETE** | **2026-03-19** | **Part XIII appended; 347× LLR; S8 resolved; 3 new tensions; 10 top findings** |
| W3i5 | PENDING | — | 11 priority questions defined (see Part XIII §XIII.20) |
| W3i6–W3i20 | PENDING | — | |

---

## ITERATION 4 (W3i4) — COMPLETE

**Date completed**: 19 March 2026
**Corpus appended**: PART XIII (lines 2163–2797 of MASTER_FINDINGS_CORPUS.md)
**Source files**: 17 × W3i4_P*.tex + W3i4_Cosmo_update.tex + W3i4_MatSci_update.tex

### Summary of W3i4 Findings

**Critical corrections (change prior conclusions):**
1. NS timing anomaly: 48 ps → **6.0 ps** (factor-8 metric error corrected)
2. P2 SQUID-active sensitivity 6×10^{-13}: **INVALIDATED** (corrects to ~10^{-6})
3. P2+P11 hybrid sensitivity 9.6×10^{-16}: **UNREACHABLE** with bulk SRF (corrects to ~2.7×10^{-15})
4. 6D MIMO channel: **INCORRECT** — channel is SIMO (rank-1 Fisher matrix)
5. P2 coupling efficiency: 0.9 → **0.036** at 5mm (factor-25 error corrected)
6. P4 normal-incidence relay: 100% → **0.087%** (n_ψ→√2 propagated)
7. P8 Earth-Mars average: 9.7 → **9.1 kbits/s** (n_ψ→√2 propagated)
8. ESS Lund projection: 1.14×10^{-14} → **10^{-12}–10^{-13}** (realistic commissioning timeline)
9. Cosmo f_{d,0}: 0.35–0.40 → **0.18–0.25**; S8: 0.889 → **0.81–0.82**
10. P10 sub-Landauer power: corrected to **7.8×10^{-18} W** (W3i2 was 10^8 wrong)

**Resolutions:**
- T3 (S8 tension): **RESOLVED** — dust-branch f_{d,0}=0.18–0.25 gives S8=0.81–0.82
- Mode mass 28-order discrepancy: **RESOLVED** — two distinct physical quantities (gravitational vs effective coupling mass); all sensitivity bounds preserved

**Falsification upgrades:**
- T1 (Ġ/G): upgraded from 16× helioseismology to **347× LLR violation**; all resolution mechanisms fail; genuine partial falsification of DFD cosmological sector; field-theoretic core unaffected

**New tensions identified:**
- T6: DFD field equation sources ψ from T_EM only, but Mach integral uses all matter — **fundamental source inconsistency**
- T7: P2+P11 hybrid cannot reach claimed sensitivity — **sensitivity claim invalidated**
- T8: 6D channel is SIMO not MIMO — **MIMO multiplexing claim incorrect**

**New positive findings:**
- Config Beta (P1+P2+P5+P9+P15): validated at SNR=1.06×10^5 as definitive Phase-1 experiment
- P13 TAI/CLONETS-DS: 5σ detection in **3.1 days** from 2028 — most temporally accessible test
- P14 shadow: +4.6% at **0.30σ** for Sgr A* — best immediately testable prediction
- P9+P6 joint: min detectable mass **1.5×10^7 kg** at 23 km depth
- P6 decihertz: new terrestrial record h_min(0.1 Hz)~10^{-20} Hz^{-1/2} at N=10^5
- P4 underground wins at every distance (D_cross = 0 km)
- FOM_DFD = κ×T_c^{1/2} derived; MgB₂+YBCO identified for cryo-free variant
- T4 (Cold Spot): NOT YET falsification — M1 mechanism conditionally viable

### W3i4 Tensions Status

| Tension | Status | Key Figure |
|---------|--------|-----------|
| T1: Ġ/G | Genuine partial falsification (cosmological sector only) | 347× LLR violation |
| T2: P14+P5 incompatibility | Traced to T1 cascade (4×16=64×) | Resolves with T1 |
| T3: S8 | **RESOLVED** | S8=0.81–0.82 with f_{d,0}=0.18–0.25 |
| T4: Cold Spot | Not yet falsification | μ_min≈5×10^{-5} conditionally viable |
| T5: ESS Lund | Timeline revised | Q2 2027 at 10^{-12}–10^{-13} |
| T6: Source inconsistency | NEW — unresolved | EM-only vs Mach integral |
| T7: P2+P11 sensitivity | NEW — claim invalidated | Corrects to ~2.7×10^{-15} |
| T8: 6D channel SIMO | NEW — claim corrected | Capacity gain at SNR<11.8 dB only |

---

## ITERATION 5 (W3i5) — PENDING

**Status**: All 11 priority questions defined in Part XIII §XIII.20
**Estimated start**: Upon compiler invocation

### W3i5 Priority Research Questions

**Priority 1 — Theory (must resolve before publication):**
- W3i5-Q1: Source term in DFD field equation — EM-only vs all matter (resolves T1, T6)
- W3i5-Q2: Vacuum floor μ_min from DFD action (resolves T4 or confirms falsification)
- W3i5-Q3: Convention B first-principles derivation from DFD field equations

**Priority 2 — Experiment (most actionable):**
- W3i5-Q4: Config Beta full experimental protocol (P1+P2+P5+P9+P15, Phase-1)
- W3i5-Q5: P14 Sgr A* shadow precise prediction with ngEHT specification
- W3i5-Q6: CLONETS-DS sidereal discriminant complete measurement protocol

**Priority 3 — Cross-patent coherence:**
- W3i5-Q7: Minimal modification of DFD cosmological sector to satisfy LLR bound
- W3i5-Q8: P8 patent claim revision (SIMO reframing)
- W3i5-Q9: 256-cavity optical comb timing architecture specification

**Priority 4 — New physics:**
- W3i5-Q10: Coupling constant running law and cosmological implications
- W3i5-Q11: MATBG and La₃Ni₂O₇ experiment specification at improved coupling bounds

### W3i5 Agent Assignments (suggested)

| Agent | Patent/Module | W3i5 Priority Questions |
|-------|--------------|------------------------|
| Agent 1 (P1) | P1 Field Drag | Q4 (Config Beta protocol) |
| Agent 2 (P2) | P2 Resonators | Q3 (Convention B), Q9 (256-cavity timing) |
| Agent 3 (P3) | P3 Quantum | Q6 partial |
| Agent 4 (P4) | P4 WPT | Relay network maturation |
| Agent 5 (P5) | P5 Timing | Q1 (source term — P5 perspective), Q6 |
| Agent 6 (P6) | P6 Sensors | Q4 partial, Q11 partial |
| Agent 7 (P7) | P7 Storage | Grid-scale thermal architecture |
| Agent 8 (P8) | P8 Comms | Q8 (SIMO patent revision) |
| Agent 9 (P9) | P9 Navigation | Q4 partial |
| Agent 10 (P10) | P10 Computing | Q3 partial |
| Agent 11 (P11) | P11 SRF | Q3 (Convention B — P11), Q9 |
| Agent 12 (P12) | P12 Propagation | n_ψ√2 corpus finalisation |
| Agent 13 (P13) | P13 GPS | Q6 (CLONETS-DS protocol) |
| Agent 14 (P14) | P14 Cosmo | Q5 (Sgr A* prediction), Q7 (T1 modification) |
| Agent 15 (P15) | P15 Materials | Q11 (La₃Ni₂O₇/MATBG) |
| Agent 16 (Cosmo) | Cosmology | Q1 (source term — cosmo), Q2 (μ_min), Q7, Q10 |
| Agent 17 (MatSci) | Materials | Q11 |

---

## AUTHORITATIVE BOUNDS REGISTRY

*Updated after each iteration. W3i4 values supersede all prior.*

| Quantity | Value | Source | Iteration |
|---------|-------|--------|-----------|
| |λ-1| upper bound | < 1.56×10^{-9} | SQMS consolidated | W3i3 |
| μ_0 (galactic) | 0.657 ± 0.006 | Gaia DR3 | W3i3 |
| a_0 (MOND) | 1.20×10^{-10} m/s² | Milgrom | — |
| Q_EM (SQMS Nb₃Sn, 20mK) | 4×10^{10} | SQMS | W3i2 |
| Q_ψ^corr (Earth cavity) | 3.37×10^9 | P12 | **W3i4** |
| n_ψ (deep MOND limit) | √2 = 1.414 | P12 | W3i3 |
| ESS Lund realistic | 10^{-12}–10^{-13} | P11 | **W3i4** |
| LIGO 6th channel | ~6×10^{-19} | P11 | W3i3 |
| P1+P5 signal | 4.0 ns (SNR=4000) | P1 | W3i3 |
| Ġ/G (DFD prediction) | +2.6×10^{-11} yr^{-1} | P5/P14 | W3i3 |
| Ġ/G (LLR bound) | < 7.5×10^{-14} yr^{-1} | LLR | **W3i4** |
| S8 (dust-branch) | 0.81–0.82 | Cosmo | **W3i4** |
| f_{d,0} (dust fraction) | 0.18–0.25 | Cosmo | **W3i4** |
| Shadow enhancement | +4.6% (M87*: 0.77σ, Sgr A*: 0.30σ) | P14 | **W3i4** |
| P13 CLONETS-DS 5σ | 3.1 days (2028) | P13 | **W3i4** |
| P9+P6 min mass | 1.5×10^7 kg at 23km | P9+P6 | **W3i4** |

---

*Tracker created by W3i4 Compiler Agent. 19 March 2026.*
