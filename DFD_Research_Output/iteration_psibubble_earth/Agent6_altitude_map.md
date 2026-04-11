# DFD psi-Bubble: Minimum Operating Altitude vs Magnetic Field Strength

**Agent:** Agent 6 — Altitude Mapping
**Date:** 2026-03-28
**Framework:** Density Field Dynamics (DFD)

---

## 1. Physical Setup and Governing Equations

### Threshold Condition

The psi-bubble activates when the electromagnetic energy density exceeds a critical fraction of the local rest-mass energy density:

```
η = U_EM / (ρ c²) > η_c = α/4 ≈ 1.8243 × 10⁻³
```

where:
- `α = 1/137.036` (fine structure constant)
- `η_c = α/4 = 1.8243 × 10⁻³` (vacuum loading threshold)
- `U_EM = B²/(2μ₀)` (magnetic energy density, J/m³)
- `μ₀ = 4π × 10⁻⁷ H/m`
- `c = 3 × 10⁸ m/s`

### Atmospheric Density Profile

```
ρ(h) = ρ₀ × exp(−h/H)
```

- `ρ₀ = 1.225 kg/m³` (sea-level density)
- `H = 8500 m` (scale height)

### Critical Density and Minimum Altitude

At threshold `η = η_c`, the critical atmospheric density is:

```
ρ_c = B² / (2μ₀ η_c c²)
```

Inverting the altitude profile:

```
h_min = H × ln(ρ₀ / ρ_c)
      = H × ln( 2μ₀ η_c c² ρ₀ / B² )
```

The device **cannot** sustain the psi-bubble below `h_min` because ambient atmospheric density quenches `η` below `η_c`.

---

## 2. Device Parameters (Fixed)

| Parameter | Value |
|---|---|
| Device mass | 1,000 kg |
| Shell volume V | 10 m³ (sphere r = 1.337 m, A = 22.45 m²) |
| Q-factor | 10⁹ |
| Coupling constant k_a | 51.4 |
| Gravity g | 9.8 m/s² |
| Device weight W | 9,800 N |

---

## 3. Results Table

Columns:
- **h_min**: Minimum altitude where psi-bubble can form (km)
- **ρ at h_min**: Atmospheric density at that altitude (kg/m³)
- **U_EM**: Magnetic energy density in the shell (J/m³)
- **E_stored**: Total stored magnetic energy in 10 m³ shell (J)
- **F_cross**: Q-amplified cross-term force = Q × k_a × (U_EM/c²) × g × V (N)
- **F_mode1**: Mode I thrust at h_min = η_c × ρ × c × A (N)
- **F > W?**: Whether Q-amplified force exceeds 9,800 N device weight

| B (T) | h_min (km) | ρ at h_min (kg/m³) | U_EM (J/m³) | E_stored (J) | F_cross (N) | F_mode1 (N) | F > W? |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 170.35 | 2.42 × 10⁻⁹ | 3.98 × 10⁵ | 3.98 × 10⁶ | 22.3 | 0.030 | NO |
| 2 | 158.57 | 9.69 × 10⁻⁹ | 1.59 × 10⁶ | 1.59 × 10⁷ | 89.1 | 0.119 | NO |
| 5 | 143.0 | 6.06 × 10⁻⁸ | 9.95 × 10⁶ | 9.95 × 10⁷ | 557 | 0.744 | NO |
| 10 | 131.2 | 2.42 × 10⁻⁷ | 3.98 × 10⁷ | 3.98 × 10⁸ | 2,227 | 2.98 | NO |
| 20 | 119.4 | 9.69 × 10⁻⁷ | 1.59 × 10⁸ | 1.59 × 10⁹ | 8,908 | 11.9 | NO (91%) |
| **50** | **103.8** | **6.06 × 10⁻⁶** | **9.95 × 10⁸** | **9.95 × 10⁹** | **55,670** | **74.4** | **YES** |
| 100 | 92.1 | 2.42 × 10⁻⁵ | 3.98 × 10⁹ | 3.98 × 10¹⁰ | 222,700 | 298 | YES |
| 200 | 80.3 | 9.69 × 10⁻⁵ | 1.59 × 10¹⁰ | 1.59 × 10¹¹ | 890,800 | 1,191 | YES |
| 500 | 64.7 | 6.06 × 10⁻⁴ | 9.95 × 10¹⁰ | 9.95 × 10¹¹ | 5.57 × 10⁶ | 7,443 | YES |
| 1000 | 52.9 | 2.42 × 10⁻³ | 3.98 × 10¹¹ | 3.98 × 10¹² | 2.23 × 10⁷ | 29,770 | YES |

**Note on Mode I altitude at threshold:** At `h_min`, `η = η_c` by construction (the device is exactly at the activation threshold). The Mode I formula `F = η_c × ρ × c × A` therefore evaluates at the minimum ambient density — because `h_min` is the *lowest* altitude where `η ≥ η_c`, and higher altitudes provide lower `ρ` but maintain `η ≥ η_c`. Mode I thrust at `h_min` represents the minimum available thrust while the bubble is active.

---

## 4. Scaling Laws

All quantities scale as B²:

```
h_min  ∝  −ln(B²)  →  decreases by H×ln(4) ≈ 11.8 km per doubling of B
U_EM   ∝  B²
E      ∝  B²
F_cross ∝  B²       →  doubles every factor of √2 in B
F_mode1 ∝  B²       →  doubles every factor of √2 in B
```

Per order of magnitude in B (10× increase):

| Quantity | Change |
|---|---|
| h_min | decreases by ~19.6 km |
| U_EM, E, F_cross, F_mode1 | increases by ×100 |

---

## 5. Hover Analysis

### Q-Amplified Cross-Term Hover

The Q-amplified force equals device weight when:

```
F_cross = Q × k_a × B²/(2μ₀c²) × g × V = m × g

B_hover = √( m × 2μ₀c² / (Q × k_a × V) )
        = √( 1000 × 2 × 4π×10⁻⁷ × 9×10¹⁶ / (10⁹ × 51.4 × 10) )
        = 20.98 T
```

**B_hover ≈ 21 T**

At B = 21 T:
- `h_min = 118.6 km` (above Karman line, in thermosphere)
- `U_EM = 1.751 × 10⁸ J/m³`
- `E_stored = 1.751 × 10⁹ J`
- `F_cross = 9,800 N` (exactly equals weight by construction)
- `F_mode1 = 13.1 N` (Mode I negligible at this altitude/density)

**The Q-amplified cross-term achieves hover at B ≈ 21 T operating at ~118.6 km altitude.**

### Mode I Thrust Hover

Mode I hover requires `F_mode1 = η_c × ρ × c × A = m × g`:

```
ρ_hover = m × g / (η_c × c × A)
        = 9800 / (1.8243×10⁻³ × 3×10⁸ × 22.45)
        = 7.977 × 10⁻⁴ kg/m³

h_hover = H × ln(ρ₀/ρ_hover)
        = 8500 × ln(1.225 / 7.977×10⁻⁴)
        = 62.4 km
```

**Mode I hover altitude ≈ 62.4 km (mesosphere/lower thermosphere)**

This is independent of B (it depends only on geometry and atmospheric density). Mode I hover is achieved once the psi-bubble is active (any B sufficient to reach 62.4 km with `η ≥ η_c`).

From the table: at B = 500 T, `h_min = 64.7 km`, which is just above the Mode I hover altitude (62.4 km). At B = 1000 T, `h_min = 52.9 km`, and Mode I thrust (29,770 N) greatly exceeds weight (9,800 N). **The Mode I hover crossover occurs near B ≈ 480 T at ~62.4 km altitude.**

---

## 6. Hover Summary

| Mechanism | B Required | Altitude | Notes |
|---|---|---|---|
| Q-amplified cross-term only | ~21 T | ~118.6 km | High altitude, thermosphere; Mode I weak |
| Mode I thrust only | ~480 T | ~62.4 km | Low thermosphere/mesopause; 10 m³ sphere |
| Combined (cross-term dominant) | ≥ 21 T | 62–120 km | Cross-term dominates at all B |

**At B ≥ 50 T (operating above ~104 km), the cross-term force exceeds device weight by factors of 5.7× or more, enabling ascent rather than mere hover.**

---

## 7. Operational Regimes

| Regime | B Range | Altitude | Capability |
|---|---|---|---|
| Sub-threshold | < 21 T | > 119 km | Bubble forms but insufficient lift |
| Marginal hover | ~21 T | ~119 km | Cross-term exactly balances weight |
| Lift-capable | 21–50 T | 104–119 km | Positive net force; can ascend |
| Strong thrust | 50–200 T | 80–104 km | 6–91× over-thrust; rapid ascent |
| Extreme | 200–1000 T | 53–80 km | Thrust >> weight; 91×–2270× excess |

---

## 8. Key Findings

1. **The critical magnetic field for DFD hover via Q-amplified coupling is ~21 T** — achievable in principle with high-temperature superconducting magnets (current record: ~45 T in hybrid systems).

2. **h_min decreases by ~11.8 km per doubling of B**, meaning stronger fields allow operation at lower (denser) altitudes.

3. **At 50 T, the psi-bubble can operate above ~104 km (Karman line ~100 km)** with a cross-term force 5.7× device weight.

4. **Mode I thrust at h_min is always small** (because `ρ` at `h_min` is by definition the minimum activating density), but cross-term force compensates across the full range.

5. **The energy cost is severe**: at B = 21 T (hover threshold), stored energy = 1.75 GJ — equivalent to ~486 kWh. At B = 100 T, E = 39.8 GJ.

6. **The Mode I mechanism is more efficient per unit area at lower altitudes**: at sea level, `η_c × ρ₀ × c ≈ 6.7 × 10⁵ N/m²` — a 10 m³ sphere could theoretically provide ~15 MN of Mode I thrust at sea level if the bubble could form there.

---

## 9. Formulas Used

```
μ₀     = 4π × 10⁻⁷ H/m
c      = 3 × 10⁸ m/s
α      = 1/137.036
η_c    = α/4 = 1.8243 × 10⁻³
ρ₀     = 1.225 kg/m³
H      = 8500 m

U_EM   = B²/(2μ₀)                              [J/m³]
ρ_c    = B²/(2μ₀ η_c c²)                       [kg/m³]
h_min  = H × ln(ρ₀/ρ_c)                        [m]
E      = U_EM × V                               [J]
F_cross = Q × k_a × (U_EM/c²) × g × V         [N]
F_mode1 = η_c × ρ(h_min) × c × A              [N]
W      = m × g                                  [N]
```

Where sphere surface area: `A = 4π × (3V/4π)^(2/3)` = 22.45 m² for V = 10 m³.

---

*Generated by Agent 6 — DFD psi-Bubble Earth Iteration Campaign*
