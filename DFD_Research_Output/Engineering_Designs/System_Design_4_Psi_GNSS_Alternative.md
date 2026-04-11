# SYSTEM DESIGN: psi-GNSS ALTERNATIVE

## Program Designation: GEOMETRIC TRUTH

**Classification:** UNCLASSIFIED -- FOR OFFICIAL USE ONLY
**Date:** March 2026
**Revision:** 1.0

---

## 1. MISSION NEED STATEMENT

GPS and other GNSS constellations represent the single most critical vulnerability in U.S. military operations. Every precision weapon, every coordinated maneuver, every synchronized communication, and every time-stamped intelligence product depends on satellite-delivered Position, Navigation, and Timing (PNT). Adversaries have invested heavily in GPS jamming, spoofing, and anti-satellite capabilities. The DoD requires a PNT system that:

- Cannot be jammed by electromagnetic means
- Cannot be spoofed, even by a sophisticated adversary
- Works in all domains: air, land, sea, underwater, space, and indoors
- Does not depend on vulnerable satellite constellations
- Provides timing precision equal to or better than GPS
- Can operate independently or as a complement to GPS

No current alternative PNT technology satisfies all six requirements simultaneously. GEOMETRIC TRUTH does.

---

## 2. SYSTEM OVERVIEW

GEOMETRIC TRUTH is a PNT system that derives position and time from the geometric and phase structure of controlled scalar refractive fields, rather than from satellite-broadcast electromagnetic signals. A constellation of psi-field emitters generates overlapping refractive corridors with known geometric signatures. A receiver measures local psi potential and its gradient from three or more emitters and computes position from the intersection of iso-psi surfaces. Timing is extracted from the phase of psi oscillations relative to a reference manifold. Authentication is achieved by verifying the local psi curvature tensor against stored templates.

### 2.1 Operating Principle

Each GEOMETRIC TRUTH emitter generates a spatial psi distribution psi_i(r) that forms a refractive corridor (Patent 9). The corridor defines concentric iso-psi surfaces -- surfaces of constant psi value -- that propagate outward from the emitter. At any point in space, a receiver can measure:

1. **psi value** from each detectable emitter
2. **grad(psi)** -- the gradient vector pointing toward each emitter
3. **K_ij = d_i d_j psi** -- the curvature tensor encoding the emitter's unique geometric signature

Position is determined by the intersection of three or more iso-psi surfaces, analogous to GPS trilateration but using scalar field geometry instead of EM time-of-flight.

Timing is extracted from the psi oscillation phase: phi(t) = omega*t + psi(r). Because the psi-field defines a deterministic propagation delay tau = (1/c) * integral(e^psi ds) along each corridor, the receiver can derive absolute time from local phase measurement without two-way clock exchange.

### 2.2 Why It Cannot Be Spoofed

GPS spoofing works because the spoofer can generate an EM signal indistinguishable from the real satellite signal. The receiver has no way to verify that the signal traveled the claimed path through space.

psi-PNT spoofing would require the attacker to generate a psi-field with the correct curvature tensor K_ij at the receiver's location. This tensor depends on the entire spatial structure of the psi-corridor between the emitter and the receiver -- a physical field distribution that extends over kilometers or more. Generating a fake psi-field with the correct K_ij at a specific location while maintaining physical consistency (the psi equation of motion must be satisfied) is physically impossible without controlling the actual emitter.

The receiver verifies each emitter's identity by comparing measured K_ij to stored templates. A spoofed signal fails this test even if it carries the correct psi amplitude and frequency.

---

## 3. SYSTEM ARCHITECTURE

### 3.1 Emitter Constellation

GEOMETRIC TRUTH can be deployed in multiple constellation configurations:

**Configuration 1: Terrestrial Network**
- Ground-based emitter stations at military installations, communication towers, and dedicated sites
- Emitter spacing: 50-200 km (theater dependent)
- Coverage: Regional (theater of operations)
- Advantages: Hardened, high-power, no satellite vulnerability
- Deployment: Days-weeks for tactical network

**Configuration 2: Airborne Network**
- Emitters on high-altitude aircraft (E-3, E-8, Global Hawk class) or tethered aerostats
- Emitter spacing: 100-500 km
- Coverage: Theater-wide from 3-5 aircraft
- Advantages: Rapid deployment, mobile, no ground infrastructure
- Deployment: Hours

**Configuration 3: Maritime Network**
- Emitters on surface ships, submarines, and seafloor installations
- Emitter spacing: 20-100 km
- Coverage: Operational area around a carrier strike group or submarine operating area
- Advantages: Mobile with the force, works underwater

**Configuration 4: Space Network**
- Emitters on satellites in LEO, MEO, or cislunar orbits
- Global coverage (analogous to GPS constellation but using psi-field instead of EM)
- Long-term replacement for GPS
- Advantages: Global, persistent

**Configuration 5: Hybrid**
- Combination of terrestrial, airborne, maritime, and space emitters
- Provides maximum redundancy and coverage
- Gradual transition from GPS dependency

### 3.2 Emitter Station Architecture

Each emitter station comprises:

- **Parametric psi-Resonator Bank:** 4-8 resonators (Patent 2) providing high-power coherent psi-field generation
- **Metamaterial Beamformer Array:** Panel array forming steerable corridors to provide coverage over the desired area (Patent 2)
- **Timing Reference:** Cesium or rubidium atomic clock providing the master oscillation frequency for psi generation. Alternatively, the emitter network can self-synchronize using psi-corridor timing loops (Patent 5)
- **Control System:** Manages corridor synthesis, power levels, and timing synchronization with other emitters
- **Communication Link:** Conventional or psi-based link to the network management center

**Specifications per Ground Station:**
- Power: 5-20 kW
- Weight: 500-2000 kg (ground installation)
- Footprint: 3m x 3m antenna/panel area
- Establishment time: <24 hours for tactical deployment

### 3.3 Receiver Architecture

The user receiver is the critical item for widespread adoption:

**Standard Military Receiver:**
- psi-field sensor measuring psi and grad(psi) from multiple emitters
- Digital signal processor computing position, velocity, and time
- Curvature tensor calculator for spoof rejection
- Hybrid interface for GPS/INS fusion
- Form factor: GPS receiver replacement (similar size/weight/power)

**Specifications:**
- Size: 10 cm x 8 cm x 3 cm (card-level module)
- Weight: <200 g
- Power: <3 W
- Position accuracy: <1 m (3+ emitters at <200 km)
- Velocity accuracy: <0.01 m/s
- Timing accuracy: <100 ps (approaching sub-femtosecond with direct psi-phase extraction)
- Time to first fix: <10 seconds
- Update rate: 100 Hz

**Embedded Receiver (for weapons, UAS, UUV):**
- Reduced form factor: 5 cm x 4 cm x 1.5 cm
- Power: <1 W
- Weight: <50 g
- Designed for integration into guided munitions, small UAS, and autonomous vehicles

---

## 4. PERFORMANCE COMPARISON

### 4.1 Position Accuracy vs. Conditions

| Condition | GPS | eLoran | psi-PNT (Terrestrial) | psi-PNT (Space) |
|---|---|---|---|---|
| Open sky, no interference | 3-5 m | 8-20 m | <1 m | <1 m |
| Urban canyon | 10-50 m | 30-100 m | 1-3 m | 2-5 m |
| Indoor | Unavailable | Unavailable | 2-5 m | 5-10 m |
| Underwater | Unavailable | Unavailable | 1-3 m | N/A |
| Heavy jamming (100W) | Unavailable | Degraded | <1 m (unaffected) | <1 m (unaffected) |
| Sophisticated spoofing | Compromised | Compromised | <1 m (immune) | <1 m (immune) |
| After ASAT attack | Degraded/lost | Unaffected | <1 m (unaffected) | Degraded |

### 4.2 Timing Performance

| System | Timing Accuracy | Holdover (no signal) | Spoof Resistant |
|---|---|---|---|
| GPS | ~10 ns | Depends on local clock | No |
| GPS + CSAC | ~10 ns | ~1 us/hour | No |
| eLoran | ~100 ns | N/A | Partial |
| psi-PNT | ~100 ps | Infinite (geometry-locked) | Yes |
| psi-PNT + psi clock sync | <1 ps | Sub-femtosecond hold | Yes |

The sub-femtosecond timing capability (Patent 5) enables applications far beyond navigation: distributed electronic warfare synchronization, coherent sensor arrays, and time-sensitive targeting.

### 4.3 Resilience Matrix

| Threat | GPS | eLoran | Inertial | MagNav | psi-PNT |
|---|---|---|---|---|---|
| RF jamming | Vulnerable | Resistant | Immune | Immune | Immune |
| Spoofing | Vulnerable | Vulnerable | Immune | Immune | Immune |
| ASAT/space denial | Critical | N/A | N/A | N/A | Varies by config |
| Nuclear scintillation | Vulnerable | Vulnerable | Immune | Immune | Immune |
| Signal blockage | Vulnerable | Partial | Immune | N/A | Resistant |
| Drift over time | None | None | Severe | Moderate | None |

---

## 5. DEPLOYMENT SCENARIOS

### 5.1 Scenario: Theater PNT Network (Indo-Pacific)

**Requirement:** Provide resilient PNT across the Western Pacific where Chinese GPS jamming and ASAT capabilities threaten space-based PNT.

**Solution:** Deploy 8-12 GEOMETRIC TRUTH ground stations on allied territory (Japan, Guam, Philippines, Australia) plus 3-4 airborne emitters on AWACS/JSTARS-class aircraft.

**Result:** Theater-wide psi-PNT coverage from Okinawa to the Strait of Malacca. All U.S. forces maintain full PNT capability regardless of GPS status. Precision weapons retain accuracy. Sensor networks maintain synchronization.

**Deployment timeline:** 6-12 months for ground stations; 2-4 months for airborne emitters.

### 5.2 Scenario: Submarine Operating Area PNT

**Requirement:** Provide continuous, covert PNT to submarines operating under Arctic ice or in contested waters where surfacing for GPS fix is unacceptable.

**Solution:** Deploy 6-8 seafloor psi-emitter stations in the operating area, plus psi-emitters on 2-3 submarines or UUVs.

**Result:** All submarines in the operating area maintain continuous sub-meter position accuracy at operating depth, with zero need to surface. Navigation data is drift-free and spoof-immune.

### 5.3 Scenario: Urban Operations PNT

**Requirement:** SOF and infantry units require PNT inside buildings, tunnels, and urban canyons where GPS is unavailable.

**Solution:** Rapidly deploy 4-6 tactical GEOMETRIC TRUTH emitters (man-portable or vehicle-mounted) around the urban area.

**Result:** All equipped personnel and vehicles maintain meter-level PNT inside buildings, underground, and in GPS-denied urban canyons. No GPS required.

---

## 6. DEVELOPMENT ROADMAP

| Phase | Duration | Objective | Cost Est. |
|---|---|---|---|
| 1: Concept Validation | 18 months | Laboratory demonstration of psi-field generation and position determination from 3 emitters at 10m scale | $10M |
| 2: Sensor Development | 18 months | psi-PNT receiver prototype; miniaturization; spoof rejection testing | $15M |
| 3: Field Demonstration | 24 months | 3-emitter constellation at 1-10 km scale; accuracy and timing validation | $30M |
| 4: Theater Prototype | 24 months | 8-emitter regional network; integration with military GPS receivers | $60M |
| 5: Receiver Production | 18 months | Engineering development model receiver; MIL-STD qualification | $40M |
| 6: IOT&E | 18 months | Operational testing across all domains (land, sea, air, undersea) | $35M |

**Total to IOC:** ~10 years, ~$190M

---

## 7. TRANSITION STRATEGY

### Phase 1: GPS Augmentation (Years 1-5)
- psi-PNT operates alongside GPS as a cross-check and spoof-detection overlay
- Hybrid receivers output fused GPS/psi position and flag GPS spoofing
- psi curvature tensor verification protects GPS from spoofing attacks

### Phase 2: GPS Backup (Years 5-8)
- psi-PNT provides primary PNT in GPS-denied environments
- Automatic failover from GPS to psi-PNT when jamming detected
- Submarine and underground operations rely primarily on psi-PNT

### Phase 3: GPS Complement (Years 8-12)
- psi-PNT and GPS operate as co-equal PNT sources
- Military operations no longer single-point dependent on GPS
- Space-based psi-emitters begin deployment for global coverage

### Phase 4: GPS Succession (Years 12+)
- Full global psi-PNT constellation operational
- GPS maintained for civilian/commercial use and backward compatibility
- Military PNT fully resilient against all known threats

---

## 8. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| psi-field range insufficient for theater coverage | Medium | High | Denser emitter network; airborne relays |
| Receiver miniaturization challenges | Medium | Medium | Phased miniaturization; start with vehicle-mounted |
| Adversary develops psi-field jamming | Low | High | psi-field physics makes broadband jamming impractical; frequency agility |
| Timing accuracy less than predicted | Low | Medium | Hybrid with atomic clocks; psi-clock synchronization loop (Patent 5) |
| Cost of emitter infrastructure | Low | Medium | Dual-use with communications (Patent 8); share infrastructure |
| Bureaucratic resistance from GPS community | High | Medium | Position as complement/augmentation, not replacement; demonstrate value |

---

## 9. COST-BENEFIT ANALYSIS

### Cost of GPS Vulnerability (Annual)
- GPS jamming incidents affecting military operations: increasing annually
- Cost per GPS-denied weapon miss: $500K-$2M per munition
- Cost per GPS-spoofed drone loss: $5M-$150M per platform
- Cost of GPS satellite replacement: $500M per satellite
- GPS constellation reconstitution after ASAT attack: $5-10B, 5-10 years

### Cost of GEOMETRIC TRUTH
- Development to IOC: ~$190M over 10 years
- Theater network (12 emitters): ~$60M
- Global constellation: ~$5B (comparable to GPS but inherently spoof/jam immune)
- Receiver unit cost at scale: $500-$2,000 (comparable to military GPS receiver)

### Return on Investment
- Prevention of a single GPS-spoofed drone loss pays for multiple theater network deployments
- Prevention of GPS constellation degradation from ASAT attack justifies the entire program cost many times over
- The ability to operate with full PNT in a GPS-denied environment is an operational advantage that cannot be quantified in dollars alone -- it is the difference between winning and losing in a near-peer conflict

---

**END OF SYSTEM DESIGN 4**
