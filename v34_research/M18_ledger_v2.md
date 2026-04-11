# DFD v3.4 + chi-field: Updated Unified Claim-Status Ledger (M18 v2)

**Supersedes:** L20 (which predated rounds L12-L19)
**Date:** 2026-04-07
**Incorporates:** L12, L13, L14, L15, L16, L17, L18, L19 + L1-L11 negative-result campaign

## Status Legend

- **THEOREM** — Rigorous proof, no free parameters, no loopholes
- **DERIVED** — Follows from stated axioms by uncontested calculation
- **CONDITIONAL** — Follows conditionally on an explicit assumption
- **CONJECTURED** — Supported by evidence / structural argument, no derivation
- **OPEN** — Gap identified, no resolution yet

## Master Ledger

| Claim | L20 status | M18 v2 status | Evidence / round |
|---|---|---|---|
| **Foundations** | | | |
| psi-field existence & positivity | THEOREM | THEOREM | Unchanged |
| Modular / covariance axioms | THEOREM | THEOREM | Unchanged |
| Dictionary mapping DFD <-> GR/QFT | THEOREM | THEOREM | Maruyama rigidity (H4) |
| chi stability via strict-product | CONDITIONAL | CONDITIONAL | Strict-product axiom (H8) |
| **Gravitational sector (psi-field)** | | | |
| Equivalence principle recovery | THEOREM | THEOREM | Unchanged |
| Schwarzschild / FRW limits | DERIVED | DERIVED | Unchanged |
| GW constitutive derivation | DERIVED | DERIVED | v3.3 paper archived |
| **Galactic / cluster sector** | | | |
| SPARC rotation-curve fits | DERIVED | DERIVED | Unchanged |
| Cluster scaling relations | DERIVED | DERIVED | Unchanged |
| **Particle physics (k_max=60 tower)** | | | |
| Alpha tower theorem | THEOREM | THEOREM | ALPHA_TOWER_FINAL |
| Toeplitz operator construction | THEOREM | THEOREM | Archived |
| Dictionary/Maruyama rigidity | THEOREM | THEOREM | H4 |
| Yukawa hierarchy | DERIVED | DERIVED | Unchanged |
| CKM structure | DERIVED | DERIVED | Unchanged |
| PMNS structure | DERIVED | DERIVED | Unchanged |
| alpha variation bound | DERIVED | DERIVED | H10 |
| m_chi two-scale derivation | DERIVED | DERIVED | H5 |
| Planck-mass convention | DERIVED | DERIVED | H11 |
| beta = 0 birefringence | CONJECTURED | CONJECTURED | Z_2 loopholes (H1-2, H1-4) |
| **beta = alpha/2 numerical value** | (predicts 0.21°) | **CONJECTURED, range [0.03°, 1.6°]** | **Downgraded.** Route 1 (direct): pi^2 normalization error (L12). Route 2 (parity-mixing): pure numerology, no derivation (L13). Route 3 (KK / E8 holonomy): yields a wide allowed range [0.03°, 1.6°], not a sharp prediction (L14). All three independent derivation routes fail to fix the value at 0.21°. |
| **k_max = 60 closure** | OPEN | **CONJECTURED** | **Upgraded from OPEN.** Derived via E_8 dual Coxeter number 2 h^v structure (L18). Pending APS index-theorem proof; promote to DERIVED upon completion. |
| **epsilon_H prefactor** | POSTULATE | **DERIVED** | **Upgraded.** Bergman-kernel argument fixes prefactor to 3/sqrt(5) (L19). |
| **Dark matter (chi-field) sector** | | | |
| chi-field existence | THEOREM | THEOREM | Unchanged |
| T_chi = T_CDM | DERIVED | DERIVED | Unchanged |
| **Omega_chi / Omega_b = 16/3 amplitude** | CONJECTURED | **CONJECTURED (hardened negative)** | **Hardened downgrade.** Eight independent negative-result agents (L1-L9, L11) all fail to derive 16/3; L10 produces it only conditionally on additional assumptions. The L20 downgrade is now backed by a 9-agent negative campaign. Treated as numerical coincidence. |
| 16 and 3 't Hooft protection | THEOREM | THEOREM | K1-4 |
| Cross-framework 16/3 appearance | CONJECTURED | CONJECTURED | K1-2, K1-3 |
| chi warping tolerance | DERIVED | DERIVED | H8 |
| Counting vs. production consistency | DERIVED | DERIVED | H9 |
| Microsector gaps | 3 open | 3 open | H7 |
| **NEW: 10^18 chi overclosure crisis** | --- | **OPEN** | **New crisis row.** L5 / L8 identify a ~10^18 overclosure of Omega_chi under naive thermal-relic counting. No resolution; flagged as the dominant open theoretical problem in the chi sector. |
| **Cosmology** | | | |
| H_0 from DFD constants | DERIVED | DERIVED | Unchanged |
| sigma_8 match | DERIVED | DERIVED | Unchanged |
| P(k) match (linear) | DERIVED | DERIVED | R2 campaign |
| **A_s amplitude** | Free | **DERIVED (within factor 4)** | **Upgraded.** L15 derives A_s from Toeplitz f_2/f_0 = 5.4547 to within a factor of 4 of Planck-measured value. No longer free; not yet exact. |
| **Omega_b from leptogenesis** | CONDITIONAL | **CONDITIONAL (refined)** | L16 reduces residual freedom from one continuous parameter to one discrete integer (Chern-Simons level), pending integer-fixing argument. |
| **n_s = 0.964 +/- 0.001** | DERIVED | **DERIVED (with 3 caveats)** | L17 confirms Starobinsky-uniqueness derivation but flags 3 caveats: (i) e-fold matching window, (ii) reheating-temperature dependence, (iii) higher-order slow-roll corrections. Central value 0.964 +/- 0.001. |
| Boltzmann / transfer-function consistency | DERIVED | DERIVED | H3-1, H3-2 |
| LEAD A: 5.4x N-body overshoot | CONJECTURED | CONJECTURED | K1-1 |

## Aggregate Counts

| Status | L20 count | M18 v2 count | Delta |
|---|---|---|---|
| THEOREM | 11 | 11 | 0 |
| DERIVED | 15 | 17 | +2 |
| CONDITIONAL | 3 | 3 | 0 |
| CONJECTURED | 4 | 5 | +1 |
| OPEN | 1 | 2 | +1 |
| **Total tracked claims** | 34 | 38 | +4 |

## Net Changes vs. L20

**Upgrades (3):**
1. k_max = 60: OPEN -> CONJECTURED (E_8 2h^v structure, L18)
2. epsilon_H prefactor: POSTULATE -> DERIVED (Bergman 3/sqrt(5), L19)
3. A_s amplitude: Free -> DERIVED within factor 4 (L15)

**Downgrades / hardenings (2):**
1. beta = alpha/2: sharp 0.21° prediction -> CONJECTURED range [0.03°, 1.6°]; all three derivation routes (L12 pi^2 error, L13 numerology, L14 KK range) fail
2. 16/3 amplitude: CONJECTURED -> CONJECTURED (hardened) — 8 negative agents (L1-L9, L11), L10 conditional only

**Refinements (2):**
1. Omega_b: one continuous parameter -> one discrete integer pending (L16)
2. n_s: 0.9641 -> 0.964 +/- 0.001 with 3 caveats (L17)

**New rows (1):**
1. 10^18 chi overclosure crisis (L5 / L8): OPEN — dominant open chi-sector problem

## Summary

- 11 THEOREMs (unchanged from L20)
- 17 DERIVED (+2: epsilon_H, A_s; k_max stays CONJECTURED pending APS proof)
- 3 CONDITIONAL (unchanged)
- 5 CONJECTURED (+1: k_max joins; beta and 16/3 hardened in place)
- 2 OPEN (+1: 10^18 overclosure crisis added; k_max moved out of OPEN)

**Net: +2 derived, +1 conjectured, +1 open, no theorems lost or gained.** The k_max upgrade and the new 10^18 overclosure crisis are the headline movements; the beta = alpha/2 sharp prediction is now formally a range, and the 16/3 negative-result base is broadened from 7 to 9 independent failed derivations.
