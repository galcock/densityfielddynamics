# R5 Full Nonlinear DFD Perturbation PDE Solver Results

## Equation Solved

Full two-sector DFD perturbation equation:
```
Delta_3(delta_psi) + (4 a_0 / c^4) d^2(delta_psi)/dt^2
    = -(8 pi G / c^2) a_0 rho_bar delta
```

Using QUMOND formulation with self-consistent sigma_nabla regulation.

## Physical Parameters

| Parameter | Value |
|---|---|
| H_0 | 67.4 km/s/Mpc (h = 0.674) |
| Omega_b | 0.049243 |
| Omega_m (LCDM) | 0.315 |
| a_0 | 1.2e-10 m/s^2 |
| a* = 2a_0/c^2 | 2.670e-27 m^{-1} |
| rho_crit | 8.533e-27 kg/m^3 |
| rho_b_0 | 4.202e-28 kg/m^3 |
| 4a_0/c^4 | 5.942e-44 s^2 m^{-3} |
| n_s | 0.965 |
| A_s | 2.1e-09 |

## Three Scenarios

### Scenario A: QUMOND only
- Growth ODE with self-consistent nu(y_k) where y_k depends on delta
- No sigma_nabla regulation (single-mode y only)
- No temporal wave term

### Scenario B: QUMOND + sigma_nabla
- Same as A but y_eff = sqrt(y_k^2 + y_sigma^2)
- sigma_nabla computed self-consistently from all modes
- Iterated to convergence

### Scenario C: Full equation (QUMOND + sigma_nabla + temporal)
- Same as B plus temporal wave term from K''(0) = 1
- nu_effective = nu(y_eff) / (1 + R_t) where R_t = (4a_0/c^4)(aH)^2/k_com^2

## Results: sigma_8

| Scenario | sigma_8 | sigma_8 / sigma_8_LCDM |
|---|---|---|
| LCDM reference | 0.8100 | 1.0000 |
| A: QUMOND only | 0.041320 | 0.051013 |
| B: QUMOND + sigma_nabla | 0.041320 | 0.051013 |
| C: Full equation | 0.041320 | 0.051013 |

## Results: P_DFD / P_LCDM

| Scenario | k=0.02 | k=0.05 | k=0.10 | k=0.15 |
|---|---|---|---|---|
| A: QUMOND only | 0.003143 | 0.000047 | 0.001013 | 0.001509 |
| B: + sigma_nabla | 0.003143 | 0.000047 | 0.001013 | 0.001509 |
| C: Full equation | 0.003143 | 0.000047 | 0.001013 | 0.001509 |

## sigma_nabla Analysis

| Quantity | Scenario B | Scenario C |
|---|---|---|
| sigma_g(a=1) | 6.2713e-37 m/s^2 | 6.2713e-37 m/s^2 |
| y_sigma = sigma_g/a_0 | 5.2261e-27 | 5.2261e-27 |
| nu(y_sigma) | 13832813397196.0234 | 13832813397196.0234 |

## Temporal Wave Term Analysis

The temporal ratio R_t = (4a_0/c^4)(aH)^2 / k_com^2 at a=1:

| k (h/Mpc) | R_t |
|---|---|
| 0.001 | 5.9418e-28 |
| 0.010 | 5.9418e-30 |
| 0.100 | 5.9418e-32 |
| 1.000 | 5.9418e-34 |

## Growth Factor D(a=1) and D_ratio = D_DFD/D_LCDM

| k (h/Mpc) | D_LCDM | D_A | D_ratio_A | D_ratio_B | D_ratio_C |
|---|---|---|---|---|---|
| 0.0203 | 0.0512 | 7.4410e-02 | 1.454238 | 1.454238 | 1.454238 |
| 0.0492 | 0.0512 | 1.6615e-01 | 3.247145 | 3.247145 | 3.247145 |
| 0.0985 | 0.0512 | 3.1662e-01 | 6.187964 | 6.187964 | 6.187964 |
| 0.1504 | 0.0512 | 4.7215e-01 | 9.227550 | 9.227550 | 9.227550 |

## Key Physical Findings

### 1. Nonlinear MOND suppression (Scenario A)

The self-consistent QUMOND growth with y-dependent nu(y) gives much weaker
growth than LCDM. This is because for small perturbations delta << 1,
the MOND parameter y_k << 1 puts the system deep in the MOND regime where
nu ~ 1/sqrt(y). The growth source becomes ~ sqrt(delta) rather than ~ delta,
giving a fundamentally different (slower) growth law.

### 2. sigma_nabla regulation (Scenario B)

The collective gradient from all modes (sigma_nabla) provides a background
y_sigma that regularizes the single-mode y_k. If y_sigma >> y_k, then
nu(y_eff) is approximately nu(y_sigma) = constant, linearizing the equation.
However, with baryon-only perturbations, sigma_nabla is small and does not
push the system toward LCDM-like growth.

### 3. Temporal wave term (Scenario C)

The temporal term from K''(0) = 1 is negligible at cosmological scales.
The ratio R_t = (4a_0/c^4)(aH)^2/k_com^2 ranges from ~6e-28 at k=0.001 h/Mpc
to ~6e-34 at k=1 h/Mpc. This is far too small to affect growth.
The term becomes relevant only at scales vastly exceeding the Hubble horizon,
where it provides wave-like propagation of the density field perturbation.

### 4. Implications for DFD

The pure QUMOND perturbation approach with baryon-only transfer function
cannot reproduce LCDM-like structure formation. The DFD framework requires
additional physics beyond simple QUMOND to match observations:

- **Pre-recombination MOND**: Enhancement of baryon perturbations before
  decoupling, modifying the effective transfer function
- **Non-perturbative DFD effects**: The density field psi may provide
  backreaction or effective dark matter at the background level
- **Modified initial conditions**: The DFD action may predict different
  primordial spectra or additional degrees of freedom
- **External field effect (EFE)**: Scale-dependent EFE from the cosmic
  density field may regulate the MOND enhancement differently
