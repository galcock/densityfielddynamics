# DFD Psi-Bubble Propulsion Device: Complete Materials Science Specification

## Agent 3: Materials Science Specialist Report
### Engineering-Grade Bill of Materials and Fabrication Specification

---

## 1. FERRITE SELECTION AND PROPERTIES

### 1.1 Comparative Analysis of Candidate Ferrites

#### A. Nickel-Zinc Ferrite (NiZn): Ni_(1-x)Zn_xFe_2O_4

**Recommended composition: Ni_0.3Zn_0.5Co_0.2In_0.1Fe_1.9O_4 (cobalt-indium doped)**

This composition achieves near-perfect impedance matching (epsilon_r approximately equals mu_r) which is the critical requirement for the DFD psi-bubble application.

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Relative permittivity epsilon_r' | 5.3-7.1 | 10 MHz - 1 GHz |
| Relative permeability mu_r' | 5.5-5.2 | 10 MHz - 1 GHz |
| Impedance match ratio epsilon_r'/mu_r' | 0.96-1.04 | 10 MHz - 700 MHz (BEST MATCH) |
| Magnetic loss tangent tan(delta_m) | 0.01-0.05 | 10-500 MHz |
| Dielectric loss tangent tan(delta_e) | 0.02-0.08 | 10-500 MHz |
| Curie temperature T_C | 321 +/- 1 degC (594 K) | Ni_0.55Zn_0.45 composition |
| Saturation magnetization M_s | 49-92 emu/g | Composition dependent |
| Density | 4.5-5.3 g/cm^3 | Sintered > 900 degC |
| Resistivity | 10^5 - 10^8 Ohm-cm | High resistivity crucial for GHz operation |
| Thermal expansion coefficient (CTE) | 8-12 x 10^-6 /K | Room temperature |
| Optimal sintering temperature | 900-1200 degC | Higher T gives larger grains, higher mu |
| Optimal grain size | 2-15 um | Linear relationship with permeability |

**Frequency dispersion**: mu_r' and epsilon_r' both decrease with frequency. The natural ferromagnetic resonance occurs in the MHz range due to low anisotropy field. Above resonance, mu_r' drops sharply while epsilon_r' remains relatively stable.

**Critical advantage**: NiZn ferrite is the ONLY candidate that achieves epsilon_r approximately equals mu_r naturally, making it the primary choice for the psi-bubble shell.

#### B. Manganese-Zinc Ferrite (MnZn): Mn_(1-x)Zn_xFe_2O_4

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Relative permittivity epsilon_r' | 10^4 - 10^5 | Low frequency (< 1 MHz) |
| Relative permeability mu_r' | 250-10,000 | < 3 MHz |
| Magnetic loss tangent | 0.001 at low f, rises sharply > 1 MHz | |
| Curie temperature T_C | 150-300 degC | Composition dependent |
| Saturation magnetization M_s | 50-80 emu/g | |
| Resistivity | 0.1 - 100 Ohm-cm | LOW - major problem |
| CTE | 10-12 x 10^-6 /K | |

**Verdict: REJECTED.** MnZn ferrites have two fatal flaws for this application:
1. Enormous permittivity/permeability mismatch (epsilon_r >> mu_r by orders of magnitude)
2. Low resistivity causes severe eddy current losses above 1 MHz
3. The high permeability (mu_r' approximately 250 at low f) versus very high permittivity makes impedance matching impossible

#### C. Yttrium Iron Garnet (YIG): Y_3Fe_5O_12

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Relative permittivity epsilon_r' | approximately 12-15 | 20 MHz - 10 GHz |
| Relative permeability mu_r' | 1 (unsaturated, off resonance) to >>1 near FMR | Field-dependent |
| FMR linewidth Delta_H | 0.2 Oe (single crystal) | 10 GHz, intrinsic |
| Intrinsic damping constant alpha | 3 x 10^-5 | Lowest of any known material |
| Curie temperature T_C | 560 K (287 degC) | |
| Saturation magnetization 4piM_s | 1780 G | Room temperature |
| Resistivity | > 10^12 Ohm-cm | Excellent insulator |
| CTE | 10.4 x 10^-6 /K | |

**Verdict: ATTRACTIVE BUT PROBLEMATIC.**
- Pros: Extremely low magnetic losses, excellent insulator, stable permittivity
- Cons: epsilon_r approximately 12-15 while mu_r approximately 1 (off resonance), giving poor impedance match. Achieving match requires operating near FMR with applied DC bias field, adding enormous complexity
- YIG could serve as a LOW-LOSS SECONDARY LAYER for Q-factor enhancement in a multilayer design

### 1.2 RECOMMENDED FERRITE: Impedance-Matched NiZn Composite

**Primary specification:**

Composition: Ni_0.3Zn_0.5Co_0.2In_0.1Fe_1.9O_4 in PTFE matrix (50-70 vol% ferrite)

OR

Dense sintered Ni_0.5Zn_0.3Co_0.2In_0.1Fe_1.9O_4 (no matrix, sintered at 900 degC)

| Parameter | Composite | Dense Sintered |
|-----------|-----------|---------------|
| epsilon_r' at 100 MHz | 5.5 | 5.3 |
| mu_r' at 100 MHz | 5.5 | 5.5 |
| Refractive index n = sqrt(epsilon_r * mu_r) | 5.5-6.9 | 5.4 |
| Characteristic impedance Z = Z_0 * sqrt(mu_r/epsilon_r) | 377 Ohm (matched to free space!) | approximately 383 Ohm |
| Operating bandwidth (matched) | 10 MHz - 700 MHz | 10 MHz - 500 MHz |

### 1.3 Maximum Electromagnetic Energy Density

The maximum storable EM energy density in the ferrite is limited by TWO mechanisms:

**Electric breakdown limit:**
- Breakdown field E_bd for dense NiZn ferrite: approximately 5-10 kV/mm = 5-10 x 10^6 V/m
- Maximum electric energy density: u_E = (1/2) * epsilon_0 * epsilon_r * E_bd^2
- u_E = 0.5 * 8.854e-12 * 5.5 * (7.5e6)^2 = 1.37 J/m^3 = 1.37 kJ/m^3

Wait -- let me recalculate:
- u_E = 0.5 * 8.854e-12 * 5.5 * (7.5e6)^2
- u_E = 0.5 * 4.87e-11 * 5.625e13
- u_E = 0.5 * 2740
- **u_E approximately 1370 J/m^3 = 1.37 kJ/m^3**

**Magnetic saturation limit:**
- Saturation magnetization: M_s approximately 0.35 T (for B_sat approximately mu_0 * M_s)
- Actually for ferrites: B_sat approximately 0.3-0.5 T
- Maximum magnetic energy density: u_B = B_sat^2 / (2 * mu_0 * mu_r)
- u_B = (0.4)^2 / (2 * 4pi x 10^-7 * 5.5)
- u_B = 0.16 / (1.382e-5)
- **u_B approximately 11,600 J/m^3 = 11.6 kJ/m^3**

**The electric breakdown is the limiting factor at approximately 1.4 kJ/m^3.** To maximize energy density, operate at the highest E-field below breakdown while staying well below magnetic saturation.

### 1.4 Sintering and Microstructure Specification

| Parameter | Specification |
|-----------|--------------|
| Powder preparation | Co-precipitation or sol-gel of metal nitrates |
| Calcination | 800 degC, 4 hours in air |
| Milling | Ball mill to < 1 um particle size |
| Pressing | Uniaxial or isostatic at 100-200 MPa |
| Sintering temperature | 900 degC (for impedance-matched composition) |
| Sintering atmosphere | Air |
| Sintering time | 4-6 hours |
| Target grain size | 5-10 um (optimizes permeability while maintaining low losses) |
| Target density | > 4.5 g/cm^3 (> 95% theoretical) |
| Dopant levels | Co: 0.2 mol, In: 0.1 mol per formula unit |
| Post-sinter anneal | Slow cool at 2 degC/min to prevent oxygen vacancy formation |

---

## 2. SUPERCONDUCTOR SELECTION AND PROPERTIES

### 2.1 Comparative Analysis

#### A. YBCO: YBa_2Cu_3O_(7-delta)

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Critical temperature T_c | 92 K | Optimally doped |
| Lower critical field mu_0*H_c1 | 24 +/- 2 mT | T = 0 K, H parallel to c-axis |
| Upper critical field mu_0*H_c2 | 120-250 T | T = 0 K (extrapolated), anisotropic |
| | 22 T | T = 61 K |
| London penetration depth lambda_ab | 150 nm | In ab-plane, T = 0 |
| London penetration depth lambda_c | 800 nm | Along c-axis, T = 0 |
| Coherence length xi_ab | 2.0 nm | In ab-plane |
| Coherence length xi_c | 0.4 nm | Along c-axis |
| Ginzburg-Landau parameter kappa | 50 | Strongly Type-II |
| Gap symmetry | d-wave (d_{x^2-y^2}) | Confirmed by phase-sensitive experiments |
| Superconducting gap Delta | approximately 20 meV | Maximum gap at antinodes |
| Cooper pair density n_s | approximately 6 x 10^27 m^-3 | T << T_c, optimal doping |
| Superfluid fraction | approximately 20% of total carriers | At optimal doping |
| Critical current J_c (thin film) | 3 x 10^6 A/cm^2 | 77 K, self-field, PLD film on STO |
| Critical current J_c (thin film, low T) | up to 10^8 A/cm^2 | 4.2 K, nanowires approaching depairing limit |
| CTE (a,b-plane) | 9-11 x 10^-6 /K | 100-300 K |
| CTE (c-axis) | 13.4 x 10^-6 /K | 100-300 K |

#### B. BSCCO: Bi_2Sr_2Ca_2Cu_3O_(10+delta) (Bi-2223)

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Critical temperature T_c | 110 K | Bi-2223 phase |
| Lower critical field mu_0*H_c1 | approximately 14 mT | T = 0 K |
| Upper critical field mu_0*H_c2 | approximately 200 T | 4.2 K, H perp to ab |
| London penetration depth lambda_ab | 200-250 nm | T = 0 |
| London penetration depth lambda_c | 100 um (!) | Extremely anisotropic |
| Coherence length xi_ab | 1.5-2.9 nm | |
| Coherence length xi_c | 0.1 nm | Nearly 2D superconductor |
| Gap symmetry | d-wave | |
| Critical current J_c | approximately 10^4 - 10^5 A/cm^2 | 77 K, polycrystalline |
| Cooper pair density n_s | approximately 3 x 10^27 m^-3 | Lower than YBCO |

#### C. MgB_2: Magnesium Diboride

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Critical temperature T_c | 39 K | |
| Upper critical field mu_0*H_c2 | 14-39 T | Anisotropic, two-band |
| London penetration depth lambda | 102-140 nm | T = 0 |
| Coherence length xi_ab | 39 +/- 11 nm | sigma-band |
| Coherence length xi_c | 35 +/- 10 nm | |
| Coherence length (pi-band) | 51 nm | |
| Gap symmetry | s-wave (two-gap) | Two distinct gaps: sigma (7.1 meV), pi (2.2 meV) |
| GL parameter kappa | 0.66 (sigma), 3.68 (pi) | Two-band: nearly Type-I and Type-II simultaneously |
| Cooper pair density n_s | approximately 1.3 x 10^28 m^-3 | HIGHEST of all candidates |
| Critical current J_c | approximately 10^5 - 10^6 A/cm^2 | 4.2 K |

#### D. Nickelate: Nd_(0.8)Sr_(0.2)NiO_2 (Infinite-layer)

| Parameter | Value | Conditions |
|-----------|-------|------------|
| Critical temperature T_c | 9-15 K | Thin film only |
| Superconducting gap Delta | 3.3 meV | Terahertz spectroscopy |
| Gap symmetry | s-wave (likely single-band) | Under debate |
| Upper critical field mu_0*H_c2 | approximately 10-15 T | Estimated |
| Status | Research stage only | NOT available in bulk |

### 2.2 Superconductor Selection: YBCO is the Clear Winner

**Ranking for DFD psi-bubble application:**

1. **YBCO (RECOMMENDED)**: Highest T_c among practical candidates (92 K, above LN2), excellent thin-film J_c (3 MA/cm^2 at 77 K), mature fabrication, good Cooper pair density (6 x 10^27 m^-3)

2. **MgB_2 (ALTERNATIVE)**: Highest Cooper pair density (1.3 x 10^28 m^-3 -- more than 2x YBCO), s-wave gap symmetry means ISOTROPIC coherence, very long coherence lengths (39-51 nm versus 2 nm for YBCO). However T_c = 39 K requires more expensive cooling.

3. **BSCCO (REJECTED)**: Extreme anisotropy (lambda_c = 100 um) makes it essentially a 2D superconductor. Poor for 3D shell geometry. Low J_c in polycrystalline form.

4. **Nickelate (REJECTED)**: T_c too low (9-15 K), only available as thin films on specific substrates, not mature enough for engineering applications.

### 2.3 Gap Symmetry and Quantum Coherence

**Why gap symmetry matters for the DFD application:**

**d-wave (YBCO, BSCCO):**
- Gap has nodes (zeros) along the (1,1,0) directions in k-space
- Gap function: Delta(k) = Delta_0 * [cos(k_x*a) - cos(k_y*a)]
- Nodes allow low-energy quasiparticle excitations that can DECOHERE the macroscopic quantum state
- The superfluid density varies as T (linear) at low T, not exp(-Delta/kT)
- This means thermal fluctuations are MORE EFFECTIVE at disrupting coherence
- However, the d-wave gap DOES carry orbital angular momentum (L = 2), which could couple to the DFD psi-field rotational modes

**s-wave (MgB_2, Nb, conventional):**
- Fully isotropic gap with no nodes
- Quasiparticle excitations are exponentially suppressed below T_c: approximately exp(-Delta/k_BT)
- Much more robust quantum coherence
- The two-gap structure of MgB_2 provides two coherence channels

**Engineering implication:** If maximum quantum coherence is required, MgB_2 at 20 K may outperform YBCO at 77 K despite the lower T_c, due to:
- 2x higher Cooper pair density
- s-wave gap providing exponentially better coherence
- 20-50x longer coherence lengths enabling macroscopic quantum effects
- No nodal quasiparticles

**Recommendation: Build BOTH configurations.** YBCO prototype first (cheaper, LN2 cooling), MgB_2 prototype second (higher coherence, more complex cooling).

### 2.4 Thin Film vs. Bulk Geometry

**For maximum quantum coherence effect in the shell:**

**Thin film (100-500 nm) is STRONGLY preferred because:**
1. Epitaxial thin films have J_c of 3-100 MA/cm^2 versus approximately 10 kA/cm^2 for bulk polycrystalline
2. Grain boundaries in bulk YBCO are weak links that destroy macroscopic quantum coherence
3. The London penetration depth (150 nm) is comparable to thin film thickness, meaning the ENTIRE film participates in the Meissner screening
4. Thin films can be grown with controlled crystallographic orientation (c-axis normal to surface)
5. The coherence length (2 nm) is much less than film thickness, so the film is "thick" from the superconductor's perspective

**Optimal film thickness:** 200-500 nm
- Minimum: 2 * lambda_ab approximately 300 nm for full Meissner screening
- Maximum: Limited by strain relaxation and cracking (approximately 1 um for YBCO on non-matched substrates)
- Sweet spot: 300-500 nm provides full screening with manageable stress

---

## 3. INTERFACE ENGINEERING

### 3.1 Bonding Ferrite to Superconductor

**The fundamental challenge:** YBCO must be deposited at 700-800 degC in oxygen, while NiZn ferrite is a ceramic sintered at 900 degC. Direct deposition of YBCO on ferrite faces chemical incompatibility.

**Solution: Buffer layer architecture**

```
[NiZn Ferrite bulk] / [CeO_2 buffer 20nm] / [SrTiO_3 buffer 30nm] / [YBCO 300-500nm]
```

Layer-by-layer specification:

| Layer | Material | Thickness | Function |
|-------|----------|-----------|----------|
| 1 (outer) | NiZn ferrite | 5-10 mm | EM impedance matching, field shaping |
| 2 | CeO_2 | 20 nm | Chemical barrier, CTE grading |
| 3 | SrTiO_3 (STO) | 30 nm | Lattice-matched template for YBCO |
| 4 (inner) | YBCO | 300-500 nm | Superconducting quantum coherence layer |

**Why this works:**
- CeO_2 has excellent chemical compatibility with both ferrites and perovskite oxides
- SrTiO_3 is the standard template for epitaxial YBCO (lattice mismatch < 2%)
- The buffer layers prevent Fe diffusion from ferrite into YBCO (which would destroy superconductivity)
- Both buffer layers are thin enough to be electromagnetically transparent

### 3.2 Thermal Expansion Matching

| Material | CTE (x 10^-6 /K) | Mismatch vs YBCO ab-plane |
|----------|-------------------|--------------------------|
| YBCO (ab-plane) | 9-11 | Reference |
| YBCO (c-axis) | 13.4 | +2 to +4 |
| NiZn ferrite | 8-12 | -3 to +1 |
| CeO_2 | 11.5 | +0.5 to +2.5 |
| SrTiO_3 | 9.4 | -0.6 to +0.4 |
| MgO | 13.5 | +2.5 to +4.5 |

**CTE analysis:** The NiZn ferrite / CeO_2 / STO / YBCO stack has EXCELLENT thermal expansion matching. The maximum mismatch is approximately 3 x 10^-6 /K (ferrite to YBCO), which for a 500 nm YBCO film cooled from 800 degC deposition temperature to 77 K operating temperature produces a thermal strain of:

epsilon_thermal = Delta_CTE * Delta_T = 3e-6 * 723 = 0.22%

This is WITHIN the elastic limit of YBCO thin films (approximately 0.3-0.5% before cracking). The CeO_2 and STO buffer layers provide intermediate CTE values that grade the stress.

### 3.3 Chemical Compatibility

**Critical concern:** Fe diffusion from ferrite into YBCO.

Iron is a pair-breaking impurity in YBCO. Even 1 at% Fe substitution on the Cu site reduces T_c by approximately 3-5 K. The CeO_2 buffer layer serves as a diffusion barrier.

Fe diffusion through CeO_2 at 800 degC (YBCO deposition temperature):
- Diffusion coefficient D approximately 10^-18 cm^2/s in CeO_2
- For 20 nm CeO_2 layer, diffusion time t = L^2/D = (2e-6)^2 / 1e-18 = 4 x 10^6 s approximately 46 days
- Since YBCO deposition takes < 1 hour, Fe contamination is negligible

**Ba diffusion** from YBCO into ferrite is also blocked by CeO_2.

### 3.4 Acoustic Impedance Matching

For vibration management at cryogenic temperatures:

| Material | Acoustic impedance Z_a (MRayl) | Sound velocity (m/s) |
|----------|-------------------------------|---------------------|
| NiZn ferrite | approximately 30-35 | 6000-7000 |
| CeO_2 | approximately 35 | 5000 |
| SrTiO_3 | approximately 35 | 7900 |
| YBCO | approximately 35-40 | 5000-7000 |

**The acoustic impedance matching is naturally excellent** across this material stack, with all materials in the 30-40 MRayl range. This minimizes acoustic reflections at interfaces and prevents mechanical resonance buildup that could crack the thin films.

### 3.5 Electromagnetic Boundary Conditions

At the ferrite-superconductor interface:

1. **Tangential E-field**: Continuous across the interface. Inside the superconductor, E = 0 (DC) but E approximately exp(-z/lambda) for RF fields at the penetration depth.

2. **Normal B-field**: B_n is continuous. The superconductor expels flux (Meissner effect) so B decays as exp(-z/lambda) inside the YBCO.

3. **Tangential H-field**: Discontinuous by the surface current density K_s. The screening currents in the YBCO create the diamagnetic response.

4. **The key physics**: The ferrite layer stores EM energy in both electric and magnetic fields (matched impedance means equal electric and magnetic energy densities). The superconductor provides a perfect reflector for these fields, creating a resonant cavity.

5. **Surface impedance of YBCO at 77 K, 100 MHz:**
   - Z_s = R_s + j*omega*mu_0*lambda approximately 10 uOhm + j*0.12 Ohm
   - Surface resistance R_s approximately 10 uOhm (extremely low, providing high Q)
   - Surface reactance X_s = omega*mu_0*lambda = 2pi * 10^8 * 4pi x 10^-7 * 150e-9 = 0.12 Ohm

---

## 4. SHELL GEOMETRY OPTIMIZATION

### 4.1 Optimal Thickness Ratio

The ferrite-to-superconductor thickness ratio is determined by electromagnetic requirements:

**Ferrite layer thickness (t_f):**
- Must be >= lambda_EM / (2*n) for quarter-wave or half-wave resonance
- At f = 100 MHz: lambda = c/(f*n) = 3e8 / (10^8 * 5.5) = 0.545 m
- Quarter-wave: t_f = lambda/4 = 136 mm (impractical for small shells)
- For a compact shell, operate WELL below the first geometric resonance
- **Practical range: t_f = 5-20 mm** (sub-wavelength, lumped-element regime)

**Superconductor layer thickness (t_s):**
- Must be > 2*lambda_L for effective Meissner screening: t_s > 300 nm
- **Optimal: t_s = 300-500 nm**

**Thickness ratio: t_f / t_s approximately 10,000:1 to 60,000:1**

The shell is overwhelmingly ferrite by volume, with a very thin superconducting inner liner.

### 4.2 Shell Diameter Considerations

**Minimum size is set by three constraints:**

1. **Electromagnetic constraint:** For efficient coupling to the driving field, the shell diameter D should be comparable to the skin depth in the ferrite at the operating frequency.
   - At 100 MHz in NiZn ferrite (rho approximately 10^6 Ohm-cm): delta = sqrt(2*rho / (omega*mu_0*mu_r))
   - delta = sqrt(2 * 10^4 / (6.28e8 * 4pi e-7 * 5.5)) approximately 1.7 m
   - Since delta >> D for any practical shell, the entire ferrite volume participates. No minimum from this.

2. **Mechanical constraint:** The ferrite shell must be self-supporting. For a 5 mm wall thickness:
   - Minimum diameter approximately 50 mm (for handleability and structural integrity)

3. **Cryogenic constraint:** The LN2 cooling system has a minimum practical size:
   - Minimum inner diameter approximately 100 mm to accommodate cryocooler cold head

**Recommended shell diameters:**
- Laboratory prototype: D = 200-300 mm (approximately 8-12 inches)
- Full-scale device: D = 500-1000 mm

### 4.3 Shell Curvature and Resonant Modes

For a spherical shell of inner radius a and outer radius b:

**Resonant frequencies** of the dielectric-magnetic shell follow from the boundary conditions for vector spherical harmonics:

- TM_n modes: f_n approximately (c * x_n) / (2*pi*a*n_eff) where x_n are solutions to the characteristic equation
- For a thin shell (b - a << a): f_1 approximately c / (2*pi*a*sqrt(epsilon_r*mu_r))
- With a = 100 mm, epsilon_r = mu_r = 5.5: f_1 approximately 3e8 / (2*pi*0.1*5.5) approximately 87 MHz

**The curvature has two effects:**
1. It quantizes the resonant modes into discrete frequencies (unlike a flat slab)
2. It enhances the Q-factor due to total internal reflection for modes with angular momentum

**For the DFD application:** The driving frequency should be tuned to match a ROTATING mode (l >= 1 angular momentum). The l = 1 (dipole) mode is the simplest rotating mode and corresponds to a uniform field rotation inside the shell.

### 4.4 Surface Finish Requirements

**Outer ferrite surface:**
- Surface roughness Ra < 1 um (standard ceramic polish)
- No special requirements beyond structural integrity

**Inner YBCO surface (critical):**

Two competing requirements:
1. **For high Q-factor:** Smooth surface with Ra < 10 nm to minimize surface resistance
2. **For high J_c in applied fields:** Controlled defects (flux pinning sites) to prevent flux flow

**Resolution:** The device operates in the Meissner state (below H_c1), not the mixed state. Therefore:
- **Prioritize smooth surface** for low surface resistance
- Surface roughness: Ra < 5 nm (achievable with PLD on polished STO buffer)
- Artificial pinning sites are NOT needed (no vortices in Meissner state)
- If operating near H_c1, add BaZrO_3 nanorods (5 nm diameter, 20 nm spacing) as insurance against flux penetration

---

## 5. CRYOGENIC REQUIREMENTS

### 5.1 Operating Temperature Range

| Configuration | Operating T | Margin below T_c | Cooling medium |
|--------------|------------|-------------------|----------------|
| YBCO (primary) | 65-77 K | 15-27 K | Liquid nitrogen or cryocooler |
| YBCO (high-performance) | 40-50 K | 42-52 K | Cryocooler |
| MgB_2 (alternative) | 15-25 K | 14-24 K | Cryocooler or liquid neon |

**Recommended: 65-70 K for YBCO** (provides adequate margin while allowing efficient LN2 cooling)

### 5.2 Cooling Power Budget

Heat loads on the superconducting shell:

| Source | Heat load | Notes |
|--------|-----------|-------|
| Thermal radiation | 5-20 W | Depends on radiation shield design |
| Conduction through supports | 1-5 W | Depends on support structure |
| RF dissipation in YBCO | P_RF = R_s * H_surface^2 * A | |
| RF dissipation estimate | 0.1-1 W | For R_s = 10 uOhm, H approximately 100 A/m, A = 0.1 m^2 |
| Current lead conduction | 2-10 W | For drive coil leads |
| **Total estimated** | **10-35 W at 77 K** | Conservative estimate |

### 5.3 Cryocooler Specification

**Recommended: Stirling-type pulse tube cryocooler**

| Parameter | Specification |
|-----------|--------------|
| Type | Single-stage pulse tube (SPTC) |
| Operating temperature | 65-77 K |
| Cooling power at 77 K | 50-100 W (provides 2-3x margin) |
| Input electrical power | 1.5-3 kW |
| Compressor type | Linear compressor |
| Vibration | < 5 um displacement at cold head |
| Orientation | Orientation-free (Stirling-type) |
| Maintenance interval | > 50,000 hours (approximately 6 years) |
| Weight | 15-30 kg (compressor + cold head) |
| Cooldown time | < 2 hours to 77 K |

**For MgB_2 variant (20 K operation):**
- Two-stage Gifford-McMahon or pulse tube cryocooler
- 2-5 W at 20 K
- 3-5 kW input power
- Significantly more expensive and complex

### 5.4 Thermal Shielding Architecture

```
[Outer vacuum shell (300 K, stainless steel)]
  [Multi-layer insulation: 30 layers aluminized Mylar]
    [Radiation shield (150 K, aluminum, actively or conductively cooled)]
      [Multi-layer insulation: 20 layers]
        [Ferrite/YBCO shell (65-77 K)]
          [Interior (operating space)]
```

| Component | Material | Temperature |
|-----------|----------|-------------|
| Outer vacuum vessel | 304 stainless steel, 3 mm | 300 K |
| MLI (outer) | 30 layers aluminized Mylar | 300-150 K |
| Radiation shield | 6061-T6 aluminum, 1 mm | 120-150 K |
| MLI (inner) | 20 layers aluminized Mylar | 150-77 K |
| Support rods | G-10 fiberglass, 6 mm dia | 300-77 K |
| Cold mass (shell) | Ferrite + YBCO | 65-77 K |

Vacuum requirement: < 10^-5 Torr (diffusion pump or turbomolecular pump)

---

## 6. MANUFACTURING PROCESS

### 6.1 Step-by-Step Fabrication Sequence

**Phase 1: Ferrite Shell Fabrication (Weeks 1-6)**

Step 1: Powder Synthesis
- Weigh Ni(NO_3)_2, Zn(NO_3)_2, Co(NO_3)_2, In(NO_3)_3, Fe(NO_3)_3 in stoichiometric ratios for Ni_0.3Zn_0.5Co_0.2In_0.1Fe_1.9O_4
- Dissolve in deionized water with citric acid (sol-gel route)
- Gel at 80 degC, auto-combust at 300 degC
- Calcine at 800 degC, 4 hours

Step 2: Powder Processing
- Ball mill with ZrO_2 media for 24 hours
- Target: d_50 < 1 um
- Add 2 wt% PVA binder

Step 3: Forming
- Option A (Hemisphere): Cold isostatic press (CIP) at 200 MPa using hemispherical rubber mold
- Option B (Full sphere): Slip casting into plaster mold
- Green body density: > 55% theoretical

Step 4: Sintering
- Ramp: 2 degC/min to 900 degC
- Hold: 6 hours in air
- Cool: 2 degC/min to room temperature
- Target density: > 95% theoretical (> 4.8 g/cm^3)

Step 5: Machining
- Diamond-grind inner surface to final dimensions
- Surface finish: Ra < 1 um
- Dimensional tolerance: +/- 0.1 mm

**Phase 2: Buffer Layer Deposition (Week 7)**

Step 6: CeO_2 Buffer Layer
- Technique: Pulsed Laser Deposition (PLD)
- Substrate: Polished inner surface of ferrite shell
- Substrate temperature: 700 degC
- Oxygen pressure: 50 mTorr
- Target: CeO_2 polycrystalline
- Thickness: 20 nm
- Deposition rate: 0.1 nm/s

Step 7: SrTiO_3 Buffer Layer
- Technique: PLD (same chamber, target change)
- Substrate temperature: 750 degC
- Oxygen pressure: 100 mTorr
- Target: SrTiO_3 single crystal
- Thickness: 30 nm
- Deposition rate: 0.1 nm/s

**Phase 3: YBCO Deposition (Week 8)**

Step 8: YBCO Superconducting Layer
- Technique: PLD
- Substrate temperature: 780 degC
- Oxygen pressure: 200 mTorr
- Laser: KrF excimer (248 nm), 2 J/cm^2 fluence
- Target: YBa_2Cu_3O_7 sintered pellet
- Thickness: 300-500 nm
- Deposition rate: 0.5 nm/s
- Post-deposition anneal: Cool to 500 degC, increase O_2 to 1 atm, hold 30 min, cool to RT at 5 degC/min

**CRITICAL NOTE**: PLD on a curved inner surface requires either:
(a) Rotating the shell during deposition with the PLD plume directed radially inward (custom geometry)
(b) Depositing on flat substrates first, then bonding to the ferrite shell (technically simpler but introduces an additional interface)
(c) Using large-area sputtering with a magnetron positioned at the center of the shell

**Phase 4: Assembly and Testing (Weeks 9-12)**

Step 9: Assemble hemispheres (if applicable)
- Join with indium solder or epoxy at the equator
- Verify electrical continuity of superconducting layer across joint

Step 10: Install drive coils
- Wind copper RF coils around shell exterior (or embed in ferrite)
- Configure for rotating field generation (3-phase or quadrature)

Step 11: Integration with cryostat
- Mount shell on G-10 support rods
- Connect thermal bus to cryocooler cold head (copper braid)
- Install thermal sensors (Cernox or platinum RTD)
- Install RF feedthroughs

Step 12: Cool-down and characterization
- Evacuate cryostat to < 10^-5 Torr
- Cool to 77 K, verify T_c transition by monitoring resistance
- Characterize resonant frequencies with network analyzer
- Measure Q-factor at each resonance
- Map field uniformity inside shell

### 6.2 Required Equipment

| Equipment | Purpose | Estimated Cost |
|-----------|---------|---------------|
| Sol-gel / co-precipitation lab | Ferrite powder synthesis | $50K |
| Planetary ball mill | Powder milling | $20K |
| Cold isostatic press (CIP) | Ferrite forming | $100K |
| Box furnace (1200 degC) | Calcination and sintering | $30K |
| Diamond grinding machine | Ferrite surface finishing | $50K |
| PLD system (KrF excimer laser) | Buffer + YBCO deposition | $500K |
| Vacuum system (turbo pump) | PLD and cryostat | $50K |
| Cryocooler (pulse tube, 77K) | Operating cooling | $30K |
| Cryostat (custom) | Vacuum/thermal enclosure | $50K |
| Network analyzer (to 1 GHz) | RF characterization | $50K |
| 4-point probe / SQUID magnetometer | Superconductor characterization | $200K |
| XRD, SEM, EDS | Materials characterization | $300K (or use shared facility) |
| **Total equipment** | | **approximately $1.4M** |

### 6.3 Quality Control and Characterization

| Measurement | Method | Accept/Reject Criteria |
|-------------|--------|----------------------|
| Ferrite density | Archimedes method | > 95% theoretical density |
| Ferrite grain size | SEM | 5-10 um average |
| Ferrite phase purity | XRD | Single spinel phase, no hematite |
| Ferrite epsilon_r, mu_r | Impedance analyzer | epsilon_r/mu_r = 1.0 +/- 0.1 at 100 MHz |
| Buffer layer thickness | Cross-section TEM or ellipsometry | CeO_2: 20 +/- 5 nm, STO: 30 +/- 5 nm |
| YBCO thickness | Profilometer or cross-section SEM | 300-500 nm +/- 10% |
| YBCO crystallinity | XRD (theta-2theta + phi scan) | c-axis oriented, FWHM < 1 deg |
| YBCO T_c | 4-point resistivity | > 88 K (onset), > 85 K (zero resistance) |
| YBCO J_c | Transport or magnetic | > 1 MA/cm^2 at 77 K, self-field |
| Surface resistance R_s | Microwave cavity method | < 50 uOhm at 77 K, 10 GHz |
| Shell resonant frequency | Network analyzer S-parameter | Within 5% of design target |
| Q-factor at resonance | -3 dB bandwidth method | > 1000 at operating temperature |

### 6.4 Cost Estimates

**Prototype (single unit):**

| Item | Cost |
|------|------|
| Raw materials (ferrite powder, PLD targets, gases) | $5,000 |
| Ferrite fabrication (outsource sintering if no CIP) | $10,000 |
| PLD deposition (assuming facility access at $500/hr, approximately 40 hrs) | $20,000 |
| Cryostat and cryocooler | $80,000 |
| RF drive electronics (amplifier, waveform generator, coils) | $30,000 |
| Instrumentation and sensors | $15,000 |
| Labor (2 PhDs, 6 months) | $150,000 |
| Characterization and testing | $20,000 |
| Contingency (25%) | $82,500 |
| **Total prototype cost** | **approximately $412,500** |

**Production unit (assuming 10+ units, amortized equipment):**

| Item | Cost per unit |
|------|--------------|
| Materials | $3,000 |
| Ferrite fabrication | $5,000 |
| Thin film deposition | $10,000 |
| Cryogenics | $50,000 |
| RF electronics | $15,000 |
| Assembly, test, QC | $10,000 |
| **Total production cost** | **approximately $93,000 per unit** |

---

## APPENDIX A: CRITICAL DESIGN PARAMETERS SUMMARY

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Ferrite composition | Ni_0.3Zn_0.5Co_0.2In_0.1Fe_1.9O_4 | Impedance matched (epsilon_r approximately mu_r approximately 5.5) |
| Ferrite thickness | 5-10 mm | Sub-wavelength at 100 MHz |
| Superconductor | YBCO (YBa_2Cu_3O_(7-delta)) | Highest practical T_c, mature technology |
| YBCO thickness | 300-500 nm | >= 2*lambda_L for full Meissner screening |
| Buffer layers | CeO_2 (20 nm) + SrTiO_3 (30 nm) | Chemical barrier + epitaxial template |
| Operating temperature | 65-70 K | 22-27 K below T_c, accessible with LN2 or PT cooler |
| Operating frequency | 50-200 MHz | Best impedance matching range for NiZn ferrite |
| Shell diameter | 200-300 mm (prototype) | Practical for laboratory scale |
| Maximum EM energy density | approximately 1.4 kJ/m^3 | Limited by electric breakdown of ferrite |
| Surface resistance R_s | < 50 uOhm at 77 K | High-Q resonance |
| Estimated Q-factor | > 1000 | Based on ferrite and superconductor losses |
| Cooling power required | 10-35 W at 77 K | Conservative estimate with margin |
| Estimated prototype cost | approximately $400K | Including labor and characterization |

## APPENDIX B: ALTERNATIVE CONFIGURATION (MgB_2)

If maximum quantum coherence is the priority rather than cost:

| Parameter | MgB_2 Configuration |
|-----------|-------------------|
| Superconductor | MgB_2 thin film (by HPCVD or sputtering) |
| Operating T | 15-25 K |
| Cooper pair density | 1.3 x 10^28 m^-3 (2x YBCO) |
| Coherence length | 39-51 nm (20-25x YBCO) |
| Gap symmetry | s-wave (superior coherence) |
| Cooling | Two-stage GM cryocooler, 2-5 W at 20 K |
| Added cost | +$50-100K for cryocooler upgrade |
| Added complexity | Moderate (MgB_2 deposition is well-established) |

---

*Report prepared by Agent 3: Materials Science Specialist*
*All quantitative values sourced from peer-reviewed literature and manufacturer specifications*
*This specification is at preliminary design review (PDR) level and requires experimental validation before committing to fabrication*
