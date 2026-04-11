# SYSTEM DESIGN: psi-SECURE COMMUNICATION NETWORK

## Program Designation: LOCKED GEOMETRY

**Classification:** UNCLASSIFIED -- FOR OFFICIAL USE ONLY
**Date:** March 2026
**Revision:** 1.0

---

## 1. MISSION NEED STATEMENT

U.S. military communications face escalating threats from adversary jamming, spoofing, and signals intelligence (SIGINT) collection. Current anti-jam waveforms (frequency hopping, spread spectrum, directional antennas) operate within the electromagnetic spectrum and are therefore fundamentally vulnerable to EM-based countermeasures. Quantum computing threatens the cryptographic foundations of all current secure communication systems. The DoD requires a communication modality that is physically immune to EM jamming, inherently resistant to spoofing through geometric authentication rather than cryptographic keys, and invisible to conventional SIGINT collection.

---

## 2. SYSTEM OVERVIEW

LOCKED GEOMETRY is a tactical and strategic communication network that encodes and transmits information through controlled variations in a scalar refractive field (psi). Information propagates through "psi-corridors" -- shaped refractive paths between transmitter and receiver where the field geometry itself provides deterministic timing, native authentication, and immunity to electromagnetic interference.

### 2.1 Fundamental Security Properties

**Anti-Jam (Physical Layer):**
psi-field signals do not occupy any band in the electromagnetic spectrum. An EM jammer, regardless of power or bandwidth, has no effect on psi-channel signals. This is not a matter of signal processing gain or spread-spectrum advantage -- it is a categorical immunity based on operating in a different physical modality entirely.

**Anti-Spoof (Geometry-Locked Authentication):**
Each psi-corridor has a unique geometric fingerprint defined by the spatial distribution of the refractive index along the path. The receiver measures the local psi, grad(psi), and the curvature tensor K_ij = d_i d_j psi of the received corridor and compares it to a stored template using a Generalized Likelihood Ratio Test (GLRT). A spoofed signal, even if it carries the correct symbol sequence, will arrive with the wrong geometric fingerprint because the spoofer cannot replicate the physical psi-field geometry between the legitimate transmitter and receiver. This authentication is based on physics, not on computational assumptions that quantum computers can break.

**LPI/LPD (Low Probability of Intercept/Detection):**
psi-field signals are not detectable by any known electromagnetic sensor (antenna, receiver, spectrum analyzer, SIGINT platform). An adversary would need psi-field detection hardware (which does not currently exist outside the DFD patent portfolio) to even know that a communication is occurring.

**Quantum-Safe:**
Security does not rely on computational complexity (RSA, ECC, AES). Geometry-locked authentication is based on the physical impossibility of replicating a scalar field geometry, not on the difficulty of factoring large numbers. Post-quantum cryptographic algorithms are not needed for the psi-layer (though they can be layered on top for defense-in-depth).

---

## 3. NETWORK ARCHITECTURE

### 3.1 Network Topology

LOCKED GEOMETRY operates as a mesh network with the following node types:

**Type A -- Fixed Infrastructure Node:**
- Ground-based psi-transmitter/receiver with metamaterial beamformer array
- High-power parametric resonator bank (Patent 2)
- Capable of forming multiple simultaneous corridors to different receivers
- Installed at military bases, embassies, command centers, and communication relay sites

**Type B -- Mobile Platform Node:**
- Vehicle-mounted (ship, aircraft, ground vehicle) psi-transceiver
- Medium-power resonator with conformal metamaterial panels
- 1-4 simultaneous corridor capacity
- Provides operational-level communications

**Type C -- Tactical Node:**
- Man-portable or small UAS-mounted psi-transceiver
- Single-corridor capacity
- Optimized for low power and weight
- SOF and forward-deployed unit communications

**Type D -- Submarine/Underwater Node:**
- Submarine or seafloor-mounted psi-transceiver
- Corridors propagate through water (psi-field is not EM)
- Provides broadband submarine communications without surfacing

**Type E -- Space Node:**
- Satellite-mounted psi-transceiver
- Orbital corridor mesh providing global backbone
- Space-to-ground corridors for strategic communications

### 3.2 Corridor Management

**Corridor Synthesis:**
A psi-transmitter sculpts a corridor to a receiver by programming the phase pattern {phi_k} across its metamaterial beamformer array (Patent 8). The corridor is a spatially confined region of modified refractive index extending from transmitter to receiver.

**Multiplexing:**
Multiple independent corridors can operate simultaneously using:
- **Spatial multiplexing:** Distinct gradient maps grad-psi_k(r) for each corridor
- **Temporal multiplexing:** Orthogonal temporal codes in delta-psi_k(t)
- **Corridor code division:** Corridors distinguished by their unique geometric signatures

**Routing:**
The Network Controller stitches corridor segments end-to-end to form multi-hop routes. Each segment terminates at an intermediate node that receives, processes, and retransmits on a new corridor segment. Corridor segments can be dynamically rerouted around damaged or compromised nodes.

### 3.3 Modulation and Coding

Symbols are encoded in three dimensions of the psi-field (Patent 8):

1. **Envelope amplitude:** delta-psi(t) -- analogous to amplitude modulation
2. **Phase chirps:** d/dt(psi) -- analogous to frequency modulation
3. **Spatial gradient keys:** grad(psi)(r) -- unique to psi-communications, encodes addressing and authentication information in the spatial structure of the corridor

A composite constellation maps bits to the tuple (delta-psi, psi-dot, grad-psi), providing high spectral efficiency within the psi-channel.

### 3.4 Geometry-Locked Authentication

The authentication process (Patent 8):

1. Receiver measures incoming psi(r,t) and grad(psi)(r,t) continuously
2. Extracts the corridor fingerprint: spatial gradient profile + curvature tensor K_ij
3. Compares fingerprint to stored template for the claimed transmitter using GLRT
4. **Match:** Accept message; transmitter identity and route confirmed
5. **Mismatch:** Reject message; flag as potential spoof; alert network

The geometric fingerprint cannot be forged because it depends on the physical psi-field distribution along the entire corridor path between the specific transmitter and receiver locations. An attacker at a different location, even with identical hardware, would produce a different geometric fingerprint.

---

## 4. LINK SPECIFICATIONS

### 4.1 Fixed Infrastructure Links (Type A to Type A)

| Parameter | Specification |
|---|---|
| Range | 100-1000 km (ground) / global (via space relay) |
| Data rate | 1-100 Mbps |
| Latency | <10 ms (ground) / <300 ms (via GEO relay) |
| Simultaneous corridors | 8-16 |
| Power | 10-50 kW per node |
| Availability | >99.99% |

### 4.2 Mobile Platform Links (Type B)

| Parameter | Specification |
|---|---|
| Range | 50-500 km |
| Data rate | 100 kbps - 10 Mbps |
| Latency | <50 ms |
| Simultaneous corridors | 1-4 |
| Power | 2-10 kW |
| Weight | 100-300 kg (vehicle-mounted) |

### 4.3 Tactical Links (Type C)

| Parameter | Specification |
|---|---|
| Range | 5-50 km |
| Data rate | 10 kbps - 1 Mbps |
| Latency | <100 ms |
| Simultaneous corridors | 1 |
| Power | 100-500 W |
| Weight | 5-15 kg (man-portable) |

### 4.4 Underwater Links (Type D)

| Parameter | Specification |
|---|---|
| Range | 10-100 km |
| Data rate | 100 kbps - 10 Mbps |
| Latency | <100 ms |
| Corridors | 1-2 |
| Power | 1-5 kW |

This represents a revolutionary improvement over current underwater communications (acoustic modems at 10 kbps, VLF at ~50 bps).

---

## 5. COMPARISON TO EXISTING SYSTEMS

| Feature | SINCGARS FH | HAVE QUICK | Link-16 | MUOS | psi-Comms |
|---|---|---|---|---|---|
| Anti-jam method | Frequency hop | Frequency hop | TDMA/crypto | Spread spectrum | Non-EM channel |
| Jam immunity | Moderate | Moderate | Moderate | Good | Absolute |
| Anti-spoof | Crypto | Crypto | Crypto | Crypto | Geometry-locked |
| Quantum-safe | No | No | No | No | Yes |
| SIGINT visible | Yes | Yes | Yes | Yes | No |
| Underwater | No | No | No | No | Yes |
| Through plasma | No | No | No | No | Yes |
| Bandwidth | 16 kbps | 16 kbps | 238 kbps | 384 kbps | 10+ Mbps |

---

## 6. OPERATIONAL SCENARIOS

### 6.1 Scenario: GNSS-Denied, Jammed Environment

Setting: Near-peer conflict. Adversary deploys widespread GPS jamming and broadband communications jamming across theater of operations.

**Current capability:** Units fall back to degraded HF radio with reduced data rates. Tactical data links unreliable. Coordination degrades significantly.

**With LOCKED GEOMETRY:** All units with psi-nodes maintain full-rate, secure, unjammable communications. Jamming has zero effect on psi-channel. Force coordination and C2 are unimpaired.

### 6.2 Scenario: SOF Deep Behind Enemy Lines

Setting: Special operations team in denied territory. Must communicate with command without revealing position.

**Current capability:** Satellite burst transmissions (detectable by adversary SIGINT). HF sky-wave (detectable). All options create EM emissions that can be geolocated.

**With LOCKED GEOMETRY (Type C node):** Team establishes psi-corridor to relay node. Zero EM emissions. Adversary SIGINT detects nothing. Broadband data (including video) transmitted securely.

### 6.3 Scenario: Submarine Communication at Depth

Setting: Submarine at operating depth must receive updated targeting data and transmit status report.

**Current capability:** Trail VLF antenna (slow, depth limited). Surface to periscope depth for SATCOM (compromises stealth). ELF decommissioned.

**With LOCKED GEOMETRY (Type D node):** Submarine establishes psi-corridor to seafloor relay node or friendly submarine. Broadband exchange at operating depth. No depth change, no antenna deployment, no stealth compromise.

---

## 7. DEVELOPMENT ROADMAP

| Phase | Duration | Objective | Cost Est. |
|---|---|---|---|
| 1: Lab Link | 18 months | First psi-communication link; demonstrate modulation and demodulation | $8M |
| 2: Authentication | 12 months | Demonstrate geometry-locked authentication; spoof rejection testing | $5M |
| 3: Multi-node | 18 months | 3-node network with routing and multiplexing | $15M |
| 4: Field Demo | 24 months | Type B/C nodes; operational-distance links; underwater link | $40M |
| 5: Network Integration | 24 months | Integration with existing C4I; interoperability testing | $60M |
| 6: IOT&E | 18 months | Operational test with Fleet/SOF units | $30M |

**Total to IOC:** ~9.5 years, ~$158M

---

## 8. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| psi-corridor range less than projected | Medium | High | Relay node architecture; corridor amplification |
| Data rate limited by psi-channel bandwidth | Medium | Medium | Multi-corridor bonding; advanced modulation |
| Adversary develops psi-detection capability | Low | High | Stealth corridor hops; rapid rekeying of gradient maps |
| Underwater corridor attenuation higher than expected | Medium | Medium | Shorter corridor segments; seafloor relay infrastructure |
| Type C node too heavy/power-hungry for SOF | Low-Medium | Medium | Aggressive miniaturization; energy harvesting |

---

## 9. TRANSITION STRATEGY

### 9.1 Phase 1: Overlay Network

Deploy LOCKED GEOMETRY as a supplementary network alongside existing communications. Critical messages sent on both psi-channel and conventional channel. Validates reliability while building operator confidence.

### 9.2 Phase 2: Primary for Critical Functions

psi-channel becomes primary for nuclear C2 (replacing EHF AEHF), submarine communications, SOF communications, and strategic command links. Conventional systems retained as backup.

### 9.3 Phase 3: Full Integration

psi-channel integrated as primary transport layer for all military communications. Conventional EM links retained for backward compatibility, deception operations, and commercial interoperability.

---

**END OF SYSTEM DESIGN 3**
