# AGENT 8: POWER SYSTEMS AND ENERGY SOURCE SPECIALIST
## Complete Power Architecture for the DFD Psi-Bubble Propulsion Device
### 5-Metre Radius Vehicle — Full Specification

**Document Status:** Engineering Analysis — DFD Research Programme
**Date:** March 2026
**Classification:** UNCLASSIFIED

---

## PREAMBLE: SCOPE AND ASSUMPTIONS

The psi-bubble propulsion device stores a large quantity of electromagnetic energy in a resonant ferrite-superconductor shell. The shell's high-Q factor (Q ~ 10^9 for superconducting walls) means that once charged, steady-state maintenance power is low. The dominant power challenge is therefore two-fold:

1. **Initial charge-up**: pumping energy into the cavity against zero initial field
2. **Maintenance against residual losses**: P_maintain = ωU/Q

For a 5m radius vehicle, the shell is a roughly spherical or toroidal cavity of characteristic dimension R = 5 m. The resonant frequency is set by the shell geometry and ferrite properties. The key operating frequency range is estimated as:

```
f_res = c / (2π R √(ε_r μ_r)) × mode_number
```

For ferrite with μ_r ~ 100–1000 and ε_r ~ 10–20 at operating point:
- Effective wavelength: λ_eff = λ_free / √(ε_r μ_r) ≈ λ_free / √(1000) ≈ λ_free / 31
- At R = 5 m, fundamental mode: f ≈ c/(2R × √(μ_r ε_r)) ≈ (3×10^8)/(10 × 31) ≈ **1 MHz**
- With higher mode numbers or lower permeability operating points: 1–30 MHz range

**Operating frequency band: 1–30 MHz (HF band)**

This has important implications for RF power amplifier technology selection.

---

## PART 1: ENERGY STORAGE REQUIREMENTS

### 1.1 Stored EM Energy Formula

For a resonant cavity of volume V = (4/3)πR³ ≈ 523 m³ (R=5m sphere), the stored EM energy is:

```
U = (1/2) ε₀ ε_r E² V = (1/2μ₀μ_r) B² V
```

In ferrite material with μ_r ~ 100:
- Magnetic energy density: u_B = B²/(2μ₀μ_r) = B²/(2 × 4π×10⁻⁷ × 100) = B²/(2.51×10⁻⁴) J/m³
- Electric energy density: u_E = ε₀ε_r E²/2

For U = total stored energy, E_field, B_field related by cavity Q and mode geometry.

**Practical limit — magnetic saturation of ferrite:**
- NiZn ferrite saturates at B_sat ~ 0.3–0.5 T
- MnZn ferrite: B_sat ~ 0.3–0.4 T
- Hexagonal ferrite (for higher frequencies): B_sat up to 0.5 T
- **Hard upper bound on stored energy from saturation:**

```
U_max_ferrite = B_sat² × V / (2μ₀μ_r) = (0.4)² × 523 / (2 × 4π×10⁻⁷ × 100)
             = 0.16 × 523 / (2.51×10⁻⁴)
             = 83.68 / (2.51×10⁻⁴)
             ≈ 3.33 × 10⁸ J ≈ 333 MJ
```

This is a hard physical ceiling regardless of scenario. Higher Q does not help here — Q affects loss rate, not storage capacity. The saturation field of the ferrite absolutely limits stored magnetic energy.

### 1.2 Scenario A — Classical Coupling (κ = 2G/c⁴)

**Coupling constant:** κ_class = 2G/c⁴ = 2 × 6.674×10⁻¹¹ / (3×10⁸)⁴ = 1.65×10⁻²⁷ m/J

**Gravitomagnetic force on vehicle of mass M moving through field:**
The stress-energy of the EM field sources spacetime curvature. For propulsive force F:
```
F ≈ κ_class × U × (characteristic gradient scale)⁻¹ × c²
```

A rough order-of-magnitude estimate for meaningful propulsion (F ~ 10⁵ N, vehicle mass M ~ 10⁴ kg, acceleration ~ 10 m/s²):

```
U_required_A ≈ F × R / κ_class ≈ 10⁵ × 5 / (1.65×10⁻²⁷) ≈ 3×10³² J
```

Even the crude estimate gives ~10^32 J. The briefing scenario of 10^15 J is actually optimistic by many orders. The sun's total radiated energy over its ~10 billion year lifetime is ~10^44 J. At 10^15 J we are asking for the energy equivalent of the Hiroshima bomb × 2×10^7.

**Scenario A Verdict: COMPLETELY INFEASIBLE.** Classical GR coupling requires stored energy orders of magnitude beyond any conceivable power source and vastly exceeds the ferrite saturation limit (333 MJ). This scenario is retained only as a theoretical baseline.

**Field strengths at U = 10^15 J:**
```
B = √(2μ₀μ_r × U/V) = √(2 × 4π×10⁻⁷ × 100 × 10¹⁵/523)
  = √(2 × 1.26×10⁻⁴ × 1.91×10¹²)
  = √(4.8×10⁸) ≈ 2.2×10⁴ T
```
This is 22,000 Tesla — roughly 10,000× the saturation field of any known material. **Physically impossible.**

### 1.3 Scenario B — Chiao Enhancement (κ_eff ~ 10⁻²⁴)

**Enhancement factor over classical:** ~10³

**Required stored energy: ~10^9 J = 1 GJ**

Check against ferrite saturation limit (333 MJ):
```
U_B = 10⁹ J >> U_max_ferrite = 3.3×10⁸ J
```

Still exceeds the ferrite saturation limit by a factor of ~3. However, this could be addressed by:
1. Using higher-volume shell geometry (larger vehicle, or distributed shell segments)
2. Operating in multiple coupled cavity segments each at sub-saturation
3. A distributed multi-module architecture with ~3× more ferrite volume

**Field strengths at U = 10^9 J (in 523 m³, μ_r = 100):**
```
B = √(2μ₀μ_r × U/V) = √(2 × 1.26×10⁻⁴ × 1.91×10⁶)
  = √(4.8×10²) ≈ 22 T
```
This is just above the saturation field of soft ferrite (0.4 T) by a factor of 55. However, in the superconducting structural walls, the superconductor windings could themselves carry the 22 T field — ITER-class high-temperature superconductor (REBCO) achieves 45+ T in laboratory settings. The ferrite is in the field-guiding role; the actual field energy can be distributed such that ferrite operates at sub-saturation in specific zones while the superconductor carries the high-field regions.

**Scenario B Assessment: Marginal. Achievable with engineered architecture, but requires state-of-the-art REBCO superconductors and careful field distribution. Energy source challenge is the dominant problem.**

**Power source needed:** 1 GJ in reasonable charge-up time.
- At 1 hour charge-up: P_chargeup = 10^9 / 3600 ≈ **278 MW electrical**
- At 1 day charge-up: P_chargeup ≈ **11.6 MW electrical**
- At 1 week charge-up: P_chargeup ≈ **1.65 MW electrical**

### 1.4 Scenario C — Full Enhancement Stack (κ_eff maximized)

**Required stored energy: ~10^6 J = 1 MJ**

Check against ferrite saturation:
```
1 MJ << 333 MJ ✓
```
Comfortably within ferrite saturation limits.

**Field strengths at U = 10^6 J:**
```
B = √(2μ₀μ_r × U/V) = √(2 × 1.26×10⁻⁴ × 1.91×10³)
  = √(0.481) ≈ 0.69 T
```
This is somewhat above soft ferrite saturation (0.4 T) but within reach of:
- Hard ferrites: B_sat up to 0.5 T (close, may require μ_r adjustment)
- Garnet ferrites at reduced operating point
- Or simply accepting μ_r ~ 50 operating point: B = √(2 × 6.3×10⁻⁵ × 1.91×10³) = √(0.241) ≈ 0.49 T — acceptable

Alternatively, operating at 1 MJ in a slightly larger volume (distribute to μ_r regions that remain unsaturated).

**Scenario C Assessment: ACHIEVABLE with current technology. The ferrite operates near but within saturation. This is the design-point scenario.**

**Current density in superconducting walls at B = 0.69 T:**
REBCO tape at 77K carries J_c ~ 10^10 A/m² at self-field. At 0.69 T external field, J_c reduces to ~3×10^9 A/m². For a wall thickness of 5 mm:
- Linear current density: K = J_c × t = 3×10^9 × 0.005 = **1.5×10^7 A/m**
- This is demanding but within demonstrated REBCO performance.

**Power source needed:** 1 MJ in reasonable charge-up time.
- At 10 minutes: P_chargeup = 10^6 / 600 ≈ **1.67 kW** — trivially achievable
- At 1 minute: P_chargeup ≈ **16.7 kW**
- At 1 second (pulse): P_chargeup ≈ **1 MW** (requires energy storage buffer)

**Summary Table: Energy Requirements**

| Scenario | U (J) | B_field (T) | Charge-up (MW @ 1hr) | Feasibility |
|---|---|---|---|---|
| A: Classical | 10^15 | 2.2×10^4 | 2.8×10^8 | Impossible |
| B: Chiao | 10^9 | ~22 | 0.28 | Very Challenging |
| C: Full Stack | 10^6 | ~0.69 | 2.8×10^-4 | Achievable |

---

## PART 2: RF POWER GENERATION

### 2.1 Operating Frequency Analysis

The ferrite-superconductor resonant shell for a 5m radius vehicle operates in the HF band. Detailed analysis:

**Mode TM010 analog for spherical cavity in ferrite medium:**
```
f_010 = 2.405 × c / (2π R √(ε_r μ_r))
```

For ferrite properties near operating point:
- NiZn ferrite at 1 MHz: ε_r ≈ 12, μ_r ≈ 200 → √(ε_r μ_r) = √2400 ≈ 49
- f = 2.405 × 3×10^8 / (2π × 5 × 49) = 7.22×10^8 / 1539 ≈ **469 kHz**

- MnZn ferrite at lower frequency: μ_r ≈ 1000, ε_r ≈ 15 → √(ε_r μ_r) = 122
- f = 2.405 × 3×10^8 / (2π × 5 × 122) = 7.22×10^8 / 3833 ≈ **188 kHz**

- Higher modes or partial-fill geometry: multiply by mode number n
- For n = 5 with the NiZn case: f ≈ **2.3 MHz**

**Selected operating frequency for design: f_op = 1–3 MHz (Medium Wave / lower HF band)**

This choice is deliberate: it maximizes ferrite permeability (most ferrites peak μ_r at 100 kHz – 3 MHz), keeps RF components large and manageable, and uses well-understood amplifier technology.

### 2.2 RF Power Required

**Maintenance power (Scenario C):**
```
P_maintain = ω U / Q = 2π × 2×10⁶ × 10⁶ / 10⁹
           = 1.257×10⁷ × 10⁶ / 10⁹
           = 1.257×10⁷ / 10³
           = 12.57 kW ≈ 13 kW
```

With Q = 10^9 (superconducting walls), maintenance power at 1 MJ stored, 2 MHz operating frequency = **~13 kW**. This is the continuous steady-state RF power injection requirement.

**If Q_ferrite dominates (Q ~ 10^4 for ferrite loss):**
```
P_maintain(ferrite-limited) = ω U / Q_ferrite = 1.257×10⁷ × 10⁶ / 10⁴ = 1.257 GW
```
This is catastrophic — the ferrite loss would be the dominant loss mechanism. This drives the requirement for the superconducting walls to dominate the Q: the ferrite must be positioned in low-field regions (field nodes) of the resonant mode, while the superconductor carries the high-field regions. This is the key design insight: the ferrite provides permeability (modifying the dispersion relation and enabling mode propagation at low frequencies in a physically compact cavity), while the superconductor provides the high-Q walls.

**Effective combined Q:**
```
1/Q_total = 1/Q_SC + 1/Q_ferrite + 1/Q_radiation
```
If ferrite is in low-field zone: Q_ferrite_effective >> 10^8, Q_SC ~ 10^10 (Nb SRF at 4K)
Then: Q_total ≈ min(Q_SC, Q_ferrite_effective) ~ 10^9 — achievable

**Charge-up power at 10-minute charge-up for 1 MJ:**
```
P_chargeup = U/t = 10^6 / 600 = 1.67 kW
```

**Total RF power budget:**
```
P_total_RF = P_maintain + P_chargeup = 13 kW + 1.67 kW ≈ 15 kW continuous
```

After full charge-up (10 minutes), steady state:
```
P_RF_steady = 13 kW
```

**For Scenario B (Q = 10^9, U = 10^9 J):**
```
P_maintain_B = ω U / Q = 1.257×10⁷ × 10⁹ / 10⁹ = 12.57 MW ≈ 13 MW
P_chargeup_B (1 hour) = 10^9/3600 = 278 kW
P_RF_total_B ≈ 13 MW steady-state
```

### 2.3 RF Amplifier Technology Selection

**Frequency: 1–3 MHz; Power: 15–100 kW (Scenario C range)**

**Options compared:**

| Technology | Power range | Efficiency | Pros | Cons |
|---|---|---|---|---|
| GaN HEMT solid state | 1–50 kW per module | 65–80% | Compact, reliable, no HV supply | Multiple modules needed at >10 kW |
| SiC MOSFET | 1–30 kW per module | 70–85% | Very high efficiency, rugged | Lower power density than GaN |
| LDMOS | 1–10 kW per module | 60–75% | Mature, cheap | Lower efficiency |
| Vacuum tube — EL519 triode | 10–100 kW single tube | 70–85% | Very high single-unit power | Requires 4–10 kV HV supply, fragile |
| Tetrode (4CX35,000A) | 35–100 kW single tube | 75–85% | Very high power, proven in AM broadcast | Very large, requires HV |
| Induction heating inverter | 1–500 kW | 90–95% | Extremely high efficiency | Narrow-band, custom |
| Push-pull RF amplifier array | Scalable | 75–90% | Modular redundancy | Complexity |

**Selected architecture for Scenario C (15 kW total RF):**
- 3 × GaN solid-state amplifier modules, each 7 kW output at 1–3 MHz
- Each module: single GaN die (GS66516T or equivalent), push-pull configuration
- Total installed RF power: 21 kW (50% redundancy)
- Efficiency: 75% (DC-to-RF conversion)
- DC input power: 21 / 0.75 = **28 kW electrical DC input**
- Mass per module: ~8 kg (including heatsink and housing)
- Total RF amplifier mass: **~30 kg**

**For Scenario B (13 MW total RF):**
This exceeds solid-state and requires industrial RF power:
- 26 × 500 kW klystron amplifiers (at 1–3 MHz, modified from medium-wave broadcast)
- Or equivalent: 130 × 100 kW GaN modules in power-combined arrays
- Klystron efficiency: 80%
- Total DC input: 13 MW / 0.80 = **16.25 MW electrical**
- Mass: 26 klystrons × 500 kg each = **13,000 kg** — not aerospace-viable

### 2.4 Rotating Mode Excitation

The psi-bubble propulsion concept requires a rotating EM mode to generate the frame-dragging analog. This requires:

- **Minimum phase channels:** 3 channels at 120° phase spacing (3-phase analogy)
- **Optimal:** 4 channels at 90° (quadrature), easier to implement with I/Q architecture
- **Recommended: 4 independent RF channels per axis of rotation = 12 total channels** (for 3D mode rotation capability)

Each channel:
- Power: 15 kW / 4 = 3.75 kW per channel (Scenario C)
- Phase control: ±1° resolution, <1 μs switching time
- Frequency: locked to cavity resonance via phase-locked loop (PLL)

**Phase-Locked Loop Architecture:**
- Cavity pickup: directional coupler samples reflected power
- Frequency discriminator: IQ demodulator on cavity transmission signal
- Loop bandwidth: 1–10 kHz (fast enough to track thermal drift of resonance)
- Reference oscillator: OCXO (oven-controlled crystal oscillator), frequency stability 1×10⁻¹⁰
- Phase noise: <-120 dBc/Hz at 1 kHz offset
- Automatic frequency control: tracks cavity resonance as ferrite operating point shifts

---

## PART 3: POWER SOURCE OPTIONS

### 3.1 Scenario C Primary Design Point (15–30 kW electrical)

**This is well within reach of multiple technologies:**

#### Option 3.1.1 — Naval-derivative Compact Gas Turbine
- Honeywell T55 class: 25 kW shaft output in ~30 kg package
- Rolls-Royce Allison 250: 15–25 kW, well-proven
- Generator efficiency: 94% (permanent magnet generator)
- Total electrical output: ~23 kW from 30 kg engine + ~10 kg generator = **40 kg total**
- Fuel: JP-8, AVTUR, or hydrogen
- Run time: limited by fuel tankage
- **Assessment: Excellent choice for Scenario C. Standard aerospace power system.**

#### Option 3.1.2 — Lithium-Ion Battery Bank
- Energy requirement for 1-hour operation: 30 kW × 3600 s = 108 MJ = 30 kWh
- Li-ion energy density: 250 Wh/kg = 0.9 MJ/kg
- Battery mass for 1 hour: 30,000 Wh / 250 Wh/kg = **120 kg**
- For 8-hour endurance: **960 kg** — feasible but heavy
- Peak power density: modern LFP cells deliver >1 kW/kg continuous
- **Assessment: Viable for short-duration operation. Mass-efficient for up to 2-3 hours.**

#### Option 3.1.3 — Fuel Cell (PEM Hydrogen)
- Power density: 1–3 kW/kg (stack only), 0.3–0.8 kW/kg (system with tanks)
- For 30 kW continuous: stack mass ~15 kg, system ~60 kg
- Hydrogen storage: 30 kW × 3600 s / (33,000 Wh/kg LHV × η_FC) = 30,000/19,800 = 1.5 kg H₂/hour
- At 700 bar compressed H₂: gravimetric density ~5.7%wt → tank + H₂ mass ~26 kg/hour
- **Assessment: Good specific power, but H₂ logistics complex. Viable for space applications.**

#### Option 3.1.4 — KRUSTY/Kilopower Fission Reactor (NASA design)
- Power output: 1–10 kW electrical (as tested)
- Extended designs (Kilopower KRUSTY-scale): 10–43 kW electrical
- Mass: ~400 kg for 10 kW system (including shielding)
- Specific power: **25 W/kg** — poor compared to chemical options
- Advantage: indefinite run time (years), no fuel logistics
- Shielding: shadow shield approach, ~100 kg for human-crewed application
- **Assessment: Overengineered for Scenario C. Appropriate for deep-space missions where refueling is impossible. Mass penalty too high for atmospheric or near-Earth operations.**

### 3.2 Scenario B Primary Design Point (13 MW electrical)

At 13 MW, options narrow considerably:

#### Option 3.2.1 — Compact Naval Fission Reactor
- S9G reactor (Virginia-class submarine): ~165 MWth, ~50 MWe — overkill
- KLT-40S (floating power): 35 MWe — appropriate scale but 144 tonnes with shielding
- RITM-200 type scaled down: 10–20 MWe possible at ~50 tonnes
- **Key problem:** Minimum practical naval reactor with shielding masses ~50,000–150,000 kg
- For aerospace: A 5m radius vehicle has a useful mass budget of perhaps 10,000–50,000 kg
- **Assessment: Barely feasible for large vehicle (>50m). Not viable for 5m radius without breakthrough in compact reactor design.**

#### Option 3.2.2 — SPARC/Commonwealth Fusion Systems Approach
- SPARC tokamak (projected): 140 MWe net from 185 MWth, total mass ~thousands of tonnes
- Not compact. **Not applicable at this scale.**

#### Option 3.2.3 — Superconducting Magnetic Energy Storage (SMES)
SMES stores energy in a superconducting coil magnetic field:
- Energy density of SMES: W = LI²/2
- For REBCO coil at 20 T field: energy density ~160 MJ/m³ = 160 kJ/L
- For U = 10^9 J storage: volume = 10^9 / 1.6×10^8 = **6.25 m³** of superconducting coil
- Mass: ~40 kg/L for REBCO coil systems → **250,000 kg** — prohibitive
- Advanced SMES at 45 T: energy density ~640 MJ/m³
- For 10^9 J at 45 T: volume = 1.56 m³, mass ~62,000 kg
- **Assessment: Even at the limits of superconductor technology, SMES for 1 GJ masses tens of thousands of kg. Marginal for large vehicle.**

#### Option 3.2.4 — SMES for Scenario C (1 MJ)
- At 20 T REBCO: volume = 10^6/1.6×10^8 = **0.00625 m³ = 6.25 litres**
- Mass: ~40 kg/L × 6.25 L = **250 kg** plus cryostat ~100 kg = **350 kg total SMES**
- This is a viable buffer/backup energy storage for Scenario C
- **Assessment: SMES as primary or backup store for Scenario C is very attractive.**

### 3.3 Beamed Power Option

For ground-to-vehicle or orbital power delivery:

**Microwave beaming (2.45 GHz ISM):**
- Scenario C: 30 kW received power
- Rectenna efficiency: 85% at 2.45 GHz
- Required beam power: 35 kW
- Rectenna aperture at 1 km range: A = 4πR²P_rx/(P_tx × G_tx) → ~1 m² at 35 kW
- **Feasible for tethered demonstration. Not practical for long-range or space operation.**

**Laser beaming (1 μm wavelength):**
- Scenario C: 30 kW received
- Photovoltaic receiver efficiency: 50% (monochromatic)
- Required laser power: 60 kW
- Beam divergence at 100 km: diffraction-limited spot ~10 m diameter from 1 m aperture
- **Feasible for space operations (satellite-to-vehicle). Requires high-power fiber laser array.**

---

## PART 4: POWER CONDITIONING ARCHITECTURE

### 4.1 Complete Power Flow — Scenario C Design

```
PRIMARY SOURCE (Gas Turbine or Battery)
         |
    [Permanent Magnet Generator]
    Output: 3-phase AC, 400V, 50/60 Hz
         |
    [Active Rectifier / PFC Stage]
    Output: 800V DC bus
    Efficiency: 98%
         |
    [High-Voltage DC Bus — 800V]
    Distributed to:
    ├── [RF Amplifier Array] (3 × GaN modules)
    │   Input: 800V DC
    │   Output: 3.75 kW RF per channel × 4 channels = 15 kW RF
    │   Efficiency: 75%
    │
    ├── [SMES Buffer Coil] (optional)
    │   250 kg REBCO coil, 1 MJ capacity
    │   Bidirectional converter: 98% round-trip efficiency
    │
    ├── [Cryogenic System Controller]
    │   Powers LN2/LHe systems for superconducting walls
    │   ~5 kW cryocooler power
    │
    └── [Avionics / Control Systems]
        ~2 kW
```

**Total electrical budget (Scenario C):**
```
RF power (net to cavity):  15 kW
RF amplifier losses:        5 kW (at 75% efficiency)
Cryogenic system:           5 kW
Control and avionics:       2 kW
Power conditioning losses:  1 kW (bus, cabling)
TOTAL:                     28 kW continuous
```

### 4.2 DC Bus Design

- **Voltage: 800V DC** (standard high-performance aerospace bus, used in more-electric aircraft)
- **Current at 28 kW:** 35 A (manageable, thin cables)
- **Bus architecture:** Ring bus with fault isolation switches at each load
- **Fault tolerance:** Any single point failure isolated within 2 ms by solid-state circuit breakers
- **Cabling:** SiC insulated, 6 AWG for main trunk, 10 AWG for branch circuits
- **Bus capacitance:** 10 mF electrolytic + 1 mF film for transient suppression

### 4.3 Waste Heat Management

**Total heat to dissipate:**
```
Gas turbine waste heat:    6 kW (from engine, exhausted)
RF amplifier waste heat:   5 kW
Cryocooler rejection:      15 kW (at COP of 0.33 for 5 kW cooling at 77K)
Power conditioning:         1 kW
Total (excluding exhaust): 21 kW thermal
```

**Heat rejection options:**

1. **Liquid cooling loop (primary):** 50/50 water-glycol, 60°C maximum operating temperature
   - Pump power: 200 W
   - Radiator: 0.5 m² finned aluminum at 40°C ambient → 20 kW rejection
   - Mass: ~20 kg (radiator + pump + plumbing)

2. **Thermoelectric recovery (supplemental):** TEG modules on RF amplifier heatsinks
   - ΔT ~ 40°C, TEG efficiency ~ 5%: recovery = 5 kW × 0.05 = **250 W** recovered
   - Negligible but worth implementing (zero moving parts)

3. **Brayton cycle (for Scenario B only):**
   - At 13 MW total heat rejection (Scenario B), a closed-cycle Brayton plant is essential
   - Space Brayton: 1 m² radiator per 10 kW at 400 K → 1,300 m² for 13 MW
   - This is a major driver for Scenario B unfeasibility on a compact vehicle

**For space operation (no convective cooling):**
- Radiator specific power (current state of art): ~200 W/kg at 350 K
- For 21 kW (Scenario C): radiator mass = 21,000/200 = **105 kg**
- For 13 MW (Scenario B): radiator mass = 13×10^6/200 = **65,000 kg** — catastrophic

### 4.4 DC-to-RF Conversion Efficiency Summary

```
Gas turbine shaft → Generator AC:    94%
AC → 800V DC bus:                    98%
800V DC → RF at 1-3 MHz (GaN):      75%
RF → cavity stored energy:           99.9% (high Q coupling, critically coupled)
─────────────────────────────────────────
Total DC-to-stored-energy:           0.94 × 0.98 × 0.75 × 0.999 ≈ 69%
Fuel-to-stored-energy efficiency:    ~24% (turbine thermal efficiency ~35%)
```

---

## PART 5: CHARGE-UP SEQUENCE AND ENERGY MANAGEMENT

### 5.1 Cold Start Charge-Up Sequence

**Phase 0 (t = 0 to 30 min): System initialization**
- Power primary source (turbine start or battery activation)
- Initialize cryogenic system (cool superconducting walls to 77K or 4K)
  - 77K (REBCO, LN2): ~20 minutes to cool 5m shell from ambient (assumes pre-chilled LN2 supply)
  - 4K (Nb SRF): ~2 hours using Gifford-McMahon cryocooler
  - **Recommended: REBCO at 77K for rapid startup capability**
- Verify superconducting wall transition: monitor resistance → zero
- Establish PLL lock on cavity resonance

**Phase 1 (t = 30 min to 40 min): Cavity charge-up (Scenario C)**
- Apply RF at resonance frequency with critical coupling
- Increase RF power gradually to avoid thermal shock to ferrite
- Charge rate: 15 kW into cavity, 1 MJ in ~67 seconds at full power
- **Scenario C charge-up: <2 minutes at full RF power**
- Monitor: cavity Q (from input reflection), stored energy (from field pickup amplitude)
- Safety interlock: if Q drops (indicating superconductor quench), instantly dump RF power

**Phase 2 (t > 40 min): Steady-state operation**
- RF power reduced to maintenance level: ~13 kW
- PLL continuously tracks resonance (ferrite operating point shifts with temperature and field)
- Power source throttles to match 28 kW total demand
- Rotating mode control: phase of 4 RF channels adjusted for desired propulsion vector

### 5.2 Emergency Discharge Protocol

If the cavity must be rapidly de-energized (superconductor quench, emergency landing, fault):

**Quench-triggered discharge:**
- Detection: cavity Q drops by >10% in <100 ms (anomalous loss increase)
- Response time: <10 ms (hardware interlock, no software latency)
- Action: dump resistor switched across RF feed port
- Energy absorption: 1 MJ into 10 Ω dump resistor → peak power 100 MW for ~10 μs
  - Requires high-energy dump resistor bank: ceramic wirewound, pulse-rated
  - Actual energy dissipation: 1 MJ over ~1 second (controlled ramp)
- **Mass of dump resistor bank:** ~50 kg (ceramic pulse resistors, mounted on heatsink)
- Parallel option: reverse-couple RF out of cavity (regenerative braking) back to bus
  - If cavity Q is still high during controlled dump: extracted energy charges SMES buffer
  - Recovery efficiency: up to 90% of stored energy recovered into SMES

**Controlled discharge (normal shutdown):**
- Reduce RF drive: energy rings down with time constant τ = Q/ω = 10^9/(2π×2×10^6) = **79.6 seconds**
- Cavity self-discharges in ~8τ = **~636 seconds = ~11 minutes** to 1/e^8 = 0.034% of initial energy
- Alternatively, open a controlled coupling port: extract to SMES in <1 second

### 5.3 Load Following (Propulsion Direction Changes)

As thrust vector is rotated, the rotating mode pattern changes:
- Phase of each RF channel adjusted: software-defined by propulsion controller
- No change in total stored energy or maintenance power
- Phase change speed: limited by PLL settling time ~1 ms
- **Thrust vectoring response time: ~1 ms** — effectively instantaneous

For thrust magnitude changes (scale U up or down):
- Increase/decrease RF input power proportionally
- Time constant for 10× increase in stored energy: τ_charge = ΔU/P_RF = 9×10^5/15×10^3 = **60 seconds**
- Time constant for 10× decrease (controlled dump to SMES): **~1 second**

### 5.4 Energy Recovery on Deceleration

If the vehicle decelerates and the propulsion field decreases:
- Stored EM energy can be recovered by overcoupling the RF feed (reverse power flow)
- Recovery into SMES: efficiency ~85%
- Recovery into battery: efficiency ~90% (via bidirectional DC-DC converter)
- Net round-trip (charge → propulsion → recover → recharge): ~65% if fully regenerative
- **Practical implementation:** Bidirectional GaN RF amplifier modules (using synchronous rectification)

---

## PART 6: MASS AND VOLUME BUDGET — 5m RADIUS VEHICLE

### 6.1 Detailed Component Mass Table (Scenario C)

| Component | Mass (kg) | Volume (m³) | Power (kW) | Notes |
|---|---|---|---|---|
| **Primary Power Source** | | | | |
| Gas turbine (30 kW shaft) | 15 | 0.03 | 30 output | Honeywell AGT1500 scaled, or Capstone C30 |
| Permanent magnet generator | 8 | 0.01 | — | 94% efficiency |
| Fuel tank (JP-8, 4hr endurance) | 15 + 28 fuel | 0.04 | — | 7 L/hr at 30 kW output |
| **Sub-total: Primary Source** | **66** | **0.08** | | |
| **SMES Buffer (optional but recommended)** | | | | |
| REBCO coil wound on former | 200 | 0.008 | — | 1 MJ storage |
| Cryostat (LN2, vacuum jacket) | 80 | 0.05 | — | |
| Bidirectional DC converter | 15 | 0.005 | — | |
| **Sub-total: SMES** | **295** | **0.063** | | |
| **RF Power Electronics** | | | | |
| GaN RF amplifiers (3 × 7 kW) | 30 | 0.015 | 28 input | |
| PLL and phase control system | 5 | 0.005 | 0.1 | OCXO reference |
| RF feed cables and directional couplers | 10 | 0.01 | — | Low-loss coaxial |
| Impedance matching networks | 8 | 0.008 | — | Q-matched coupling loops |
| **Sub-total: RF Power** | **53** | **0.038** | | |
| **Power Conditioning** | | | | |
| Active rectifier / PFC | 5 | 0.004 | — | 98% efficiency |
| 800V DC bus equipment | 8 | 0.008 | — | Contactors, fuses, cable |
| Solid-state circuit breakers | 3 | 0.002 | — | Per IEEE 946 |
| Emergency dump resistor bank | 50 | 0.02 | — | 1 MJ pulse rating |
| **Sub-total: Conditioning** | **66** | **0.034** | | |
| **Thermal Management** | | | | |
| Liquid cooling pump and loop | 8 | 0.015 | 0.2 | 50/50 glycol |
| Radiator (atmospheric ops) | 12 | 0.3 | — | 21 kW rejection |
| Space radiator (space ops) | 105 | 0.5 | — | Replace atmospheric |
| Cryocooler (LN2 at 77K) | 20 | 0.02 | 5.0 | 5 kW cooling power |
| **Sub-total: Thermal** | **40 (atm) / 133 (space)** | | | |
| **Cryogenic Shell Systems** | | | | |
| REBCO superconducting tape (shell walls) | 300 | — | — | 5m radius shell, 2mm wall |
| Ferrite core segments (low-field zones) | 500 | — | — | NiZn ferrite |
| Cryogenic vessel structure | 200 | — | — | |
| LN2 inventory (77K ops, 4hr) | 50 | 0.063 | — | Boil-off replaced by cryocooler |
| **Sub-total: Shell** | **1,050** | | | |
| **Control and Avionics** | | | | |
| Propulsion controller (DSP/FPGA) | 5 | 0.005 | 1.0 | |
| Navigation sensors | 10 | 0.01 | 0.5 | |
| Communications | 5 | 0.005 | 0.5 | |
| **Sub-total: Control** | **20** | **0.02** | | |

### 6.2 Summary Mass Budget

| Subsystem | Mass (kg) — Atmospheric | Mass (kg) — Space |
|---|---|---|
| Primary Power Source (turbine + fuel, 4hr) | 66 | 200 (fission or SMES) |
| SMES Buffer | 295 | 295 |
| RF Power Electronics | 53 | 53 |
| Power Conditioning | 66 | 66 |
| Thermal Management | 40 | 133 |
| Cryogenic Shell | 1,050 | 1,050 |
| Control and Avionics | 20 | 20 |
| **TOTAL POWER SYSTEM** | **1,590** | **1,817** |
| Vehicle structure, payload (est.) | 5,000 | 5,000 |
| **TOTAL VEHICLE (est.)** | **~6,600** | **~6,800** |

### 6.3 Specific Power Comparison

| System | Specific Power (kW/kg) |
|---|---|
| DFD psi-bubble power system (Scenario C, turbine) | 28 kW / 371 kg = **0.075 kW/kg** |
| DFD psi-bubble power system (excl. shell, Scenario C) | 28 kW / 225 kg = **0.124 kW/kg** |
| Ion engine power system (NASA Dawn, solar) | ~0.024 kW/kg |
| Nuclear fission (KRUSTY/Kilopower) | ~0.025 kW/kg |
| Gas turbine + generator (aerospace) | ~0.75 kW/kg (engine alone) |
| Lithium-ion battery (discharge phase) | ~1 kW/kg |
| GaN RF amplifier (module only) | ~0.23 kW/kg |

The overall power system specific power of 0.075–0.124 kW/kg is dominated by the SMES buffer mass. Without the SMES (operating directly from turbine):
- Power system mass (no SMES): 66 + 53 + 66 + 40 + 20 = **245 kg**
- Specific power: 28 kW / 245 kg = **0.114 kW/kg** — comparable to spacecraft power systems

---

## PART 7: COMPLETE SPECIFICATIONS FOR 5m RADIUS SCENARIO C VEHICLE

### 7.1 Power Source Module
- **Type:** Honeywell Auxiliary Power Unit derivative, or Capstone C65 microturbine
- **Shaft power output:** 30 kW continuous, 45 kW peak (5 min)
- **Generator:** Permanent magnet, 400V 3-phase 60 Hz output
- **Mass:** 15 kg (engine) + 8 kg (generator) = 23 kg
- **Fuel:** JP-8 / Jet-A / AVTUR
- **Fuel consumption:** ~7 kg/hr at 30 kW output
- **Endurance at 100 kg fuel:** ~14 hours
- **Noise:** ~70 dB(A) at 1m (enclosure required for crewed vehicle)
- **Dimensions:** 0.4m × 0.3m × 0.3m

### 7.2 RF Generation Module
- **Operating frequency:** 2.0 MHz (centre), tunable ±200 kHz via PLL
- **Number of channels:** 4 (quadrature phased for rotating mode)
- **Power per channel:** 3.75 kW CW into load
- **Amplifier topology:** GaN HEMT push-pull, class E/F hybrid (>80% drain efficiency)
- **Amplifier chip:** GS66516T (650V, 60A, 16 mΩ) or equivalent
- **DC supply voltage:** 400V per amplifier (stepped down from 800V bus)
- **Phase control resolution:** 0.1° (13-bit DAC driving phase shifter)
- **Frequency control:** 32-bit DDS (direct digital synthesiser), 1 μHz resolution
- **PLL reference:** OCXO, ±0.01 ppm stability
- **Modulation:** CW with adjustable amplitude (for charge-up ramp)
- **Output impedance:** 50 Ω coaxial
- **Coupling to cavity:** Inductive loop, critically coupled (β = 1 at operating power)
- **Total RF output:** 15 kW (4 × 3.75 kW)
- **Total DC input:** 21 kW (at 75% efficiency, including driver stages)
- **Module dimensions:** 4 × (0.3m × 0.2m × 0.1m)
- **Total RF module mass:** 30 kg (amplifiers) + 5 kg (PLL/control) + 10 kg (cables) = 45 kg

### 7.3 Energy Storage Module (SMES Buffer)
- **Coil material:** REBCO 2G HTS tape (SuperPower or AMSC), 12mm wide, 0.1mm thick
- **Coil configuration:** Solenoid, 0.3m diameter, 0.5m length
- **Operating field:** 10 T
- **Inductance:** 200 H
- **Operating current:** 100 A
- **Stored energy:** LI²/2 = 200 × 100²/2 = **1 MJ ✓**
- **Operating temperature:** 77K (liquid nitrogen cooled)
- **Cryostat design:** Vacuum-jacketed Dewar, MLI insulation
- **Cryostat dimensions:** 0.5m diameter, 0.7m length
- **Charge/discharge rate:** 1 MJ in/out in 60 seconds (P = 16.7 kW peak)
- **Round-trip efficiency:** 96% (converter losses only, coil = lossless)
- **Total SMES system mass:** 295 kg

### 7.4 Power Conditioning Module
- **Input:** 400V AC 3-phase from generator
- **Active rectifier:** IGBT-based, unity power factor, 98% efficiency
- **DC bus voltage:** 800V ± 5%
- **Bus capacitance:** 10 mF (transient energy buffer)
- **Distribution:** Radial to 5 load zones with solid-state circuit breakers
- **Emergency dump:** 50 kg ceramic dump resistor bank, rated 1 MJ pulse
- **Monitoring:** 100 Hz telemetry of all voltages, currents, temperatures to propulsion controller
- **Total conditioning mass:** 66 kg

### 7.5 Cooling System
- **Primary coolant:** 50% propylene glycol / 50% water
- **Pump:** Centrifugal, 8 L/min, 30 W
- **Heat exchangers:** Copper-aluminium brazed plate, one per RF amplifier
- **Radiator (atmospheric):** Aluminium fin-tube, 0.5m × 0.8m × 0.05m, fan-cooled
- **Capacity:** 21 kW at 40°C ambient, 60°C maximum coolant temperature
- **Cryocooler (for SMES):** Sumitomo RDE-418D Gifford-McMahon, 6 kW input → 1 kW cooling at 77K
  (Note: 5 kW reject heat is included in the 21 kW total above)
- **Total cooling system mass:** 40 kg

### 7.6 Operational Power Modes

| Mode | RF Power (kW) | Total Electrical (kW) | Duration Capability |
|---|---|---|---|
| Standby (cavity cold, no RF) | 0 | 5 (cryo only) | Indefinite (turbine idle) |
| Charge-up | 15 | 28 | ~2 minutes to full energy |
| Full propulsion (Scenario C) | 13 (maintenance) | 25 | Fuel-limited (~14 hr) |
| Emergency dump | 0 (RF off) | 5 | <1 second cavity dump |
| SMES-only (turbine shutdown) | 13 | From SMES | ~80 minutes (1 MJ reserve) |

---

## PART 8: SCALING TO SCENARIO B (FOR COMPLETENESS)

For Scenario B (1 GJ stored, 13 MW RF), a 5m radius vehicle is not viable. The implied vehicle scale is much larger.

**Minimum viable platform for Scenario B:**
- Vehicle radius: ~50m (to have mass budget for power systems)
- Total vehicle mass: ~5×10^6 kg (equivalent to a small destroyer)
- Power source: S5W-class naval fission reactor, 20 MWe, ~200 tonnes
- RF amplifiers: 26 × 500 kW klystrons, ~13,000 kg
- Cooling: Brayton cycle with 1,300 m² radiator area
- SMES buffer: 10 GJ, REBCO at 45T: ~600,000 kg of coil
- **Total power system mass: ~800,000 kg**
- **Assessment: Scenario B at this scale corresponds to a ship- or station-class platform, not an aerospace vehicle.**

---

## PART 9: KEY FINDINGS AND DESIGN RECOMMENDATIONS

### 9.1 Critical Findings

1. **Scenario C is the only viable design point for an aerospace vehicle.** At 1 MJ stored energy (full enhancement stack), all components are at or below the state of the art. At 1 GJ (Scenario B), the power system masses dominate and exceed any plausible aerospace mass budget.

2. **Ferrite saturation is the hard physical ceiling.** For a 5m radius ferrite cavity, the maximum stored magnetic energy is ~333 MJ (at B_sat = 0.4 T). Both Scenario A and B exceed this. Scenario C is comfortably below it.

3. **RF maintenance power of 13 kW (Scenario C) is trivially achievable.** Any standard aerospace gas turbine, fuel cell, or battery bank can provide this. The propulsion concept becomes credible from an energy standpoint at this enhancement level.

4. **REBCO superconducting walls at 77K (liquid nitrogen) are strongly preferred** over Nb SRF at 4K (liquid helium) for aerospace applications. The startup time is 20 minutes vs. 2 hours, the cryogenic infrastructure is far simpler, and 77K systems are far more robust.

5. **The Q factor determines operating cost, not feasibility.** At Q = 10^9, 1 MJ costs only 13 kW to maintain. At Q = 10^4 (ferrite-only), the same energy would cost 13 GW — impossible. The superconducting walls are non-negotiable.

6. **SMES buffer adds 295 kg but provides critical resilience:** immediate energy for propulsion maneuvers independent of turbine response time, regenerative energy capture on deceleration, and a safety buffer against turbine failure.

7. **The 2 MHz operating frequency is well-served by GaN solid-state amplifiers.** No klystrons or exotic vacuum tubes required for Scenario C. The entire RF system fits in 45 kg.

### 9.2 Development Priorities

1. **Confirm EM→ψ coupling parameter λ** (Patent 11 / SRF lab work): This sets whether Scenario C enhancement factors are achievable. All other engineering is secondary to this question.

2. **Ferrite-superconductor interface design:** How to position ferrite in field nodes while maintaining operating permeability. High-field simulation required.

3. **77K REBCO shell fabrication:** Coating or tape-winding a 5m radius shell in REBCO is a significant manufacturing challenge. Partner with AMSC, SuperPower, or Bruker.

4. **PLL design for rotating mode:** 4-channel phase-locked system with sub-millisecond response. Prototype with smaller cavity first.

5. **SMES coil design:** 200H, 10T, 77K — within demonstrated technology but requires custom winding.

### 9.3 Technology Readiness Levels

| Component | TRL | Limiting Factor |
|---|---|---|
| Gas turbine power source | 9 | None — fully mature |
| GaN RF amplifiers at 2 MHz | 8 | Minor adaptation needed |
| REBCO superconducting walls | 5 | Need 5m-scale fabrication |
| SMES buffer (1 MJ, 77K) | 5 | Need custom coil design |
| PLL for rotating mode | 7 | Need multi-channel adaptation |
| Ferrite-SC interface design | 3 | Fundamental design work needed |
| Full integrated power system | 3 | Awaits ferrite-SC demonstration |

---

## APPENDIX A: KEY EQUATIONS SUMMARY

```
Stored energy:           U = B²V/(2μ₀μ_r)
Maintenance power:       P_m = ωU/Q = 2πfU/Q
Charge-up time:          t_c = U/P_RF (at critical coupling)
Cavity decay constant:   τ = Q/ω = Q/(2πf)
SMES energy:             U_SMES = LI²/2
SMES energy density:     u = B²/(2μ₀) (for air-core, no μ_r gain)
Ferrite saturation cap:  U_max = B_sat²V/(2μ₀μ_r)
RF channel count:        N_ch ≥ 3 (3 for min. rotation), 4 recommended (quadrature)
```

## APPENDIX B: VENDOR LIST

| Item | Vendor options |
|---|---|
| GaN RF amplifiers | Wolfspeed (GaN Systems), Microsemi, Qorvo |
| Gas turbine (15–30 kW) | Capstone Turbine, PBS Aerospace, Honeywell |
| REBCO tape | SuperPower (Furukawa), AMSC, Bruker |
| SMES coil design | ASG Superconductors, Babcock & Wilcox (historical) |
| Cryocoolers (77K) | Sumitomo, Cryomech, CSIC |
| Ferrite materials | TDK, Fair-Rite, Ferroxcube |
| High-energy dump resistors | Arcol, Riedon, Vishay |
| PLL / DDS modules | Analog Devices (AD9910), Texas Instruments |
| Power conditioning | Vicor, SL Power, custom |

---

*End of Agent 8 Power Architecture Analysis*
*DFD Research Programme — March 2026*
