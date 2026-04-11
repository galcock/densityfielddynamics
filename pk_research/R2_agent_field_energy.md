# Round 2 Agent: Field Energy in psi Gradients as Effective Dark Matter

## Executive Summary

This analysis computes the energy stored in the DFD psi field's spatial gradients and determines whether it can act as effective dark matter. The answer is a definitive **no** -- the direct field energy is suppressed by approximately 18 orders of magnitude relative to the CDM density. The fundamental reason is that the field energy prefactor a\*^2/(8piG) is of order 10^{-45} kg/m^3, compared to rho\_crit ~ 10^{-27} kg/m^3. This suppression arises from the relativistic factor (a\_0/c^2)^2, which encodes the weakness of gravity in natural units.

However, the analysis clarifies that the mechanism by which DFD might replace CDM is NOT through field energy but through the **phantom dark matter effect** from the nonlinear mu function, and potentially the **temporal dust branch** (c\_s = 0). These operate at completely different scales.

---

## 1. The Kinetic Function W(y) for mu(x) = x/(1+x)

### 1.1 Derivation

From the DFD action (section\_formalism.tex, Eq. 2):

```
S_psi = integral dt d^3x { (a*^2/8piG) W(|grad psi|^2/a*^2) - (c^2/2) psi (rho - rho_bar) }
```

The field equation is obtained by variation, giving:

```
div[mu(|grad psi|/a*) grad psi] = -(8piG/c^2)(rho - rho_bar)
```

where mu(x) = W'(x^2) in the simple (spherically symmetric) case.

For mu(x) = x/(1+x), with y = x^2:

```
W'(y) = sqrt(y)/(1 + sqrt(y))
```

Integrating from 0 to y with substitution u = sqrt(s):

```
W(y) = integral_0^y sqrt(s)/(1+sqrt(s)) ds = 2 integral_0^{sqrt(y)} u^2/(1+u) du
```

Using u^2/(1+u) = u - 1 + 1/(1+u):

### 1.2 Result

```
W(y) = y - 2*sqrt(y) + 2*ln(1 + sqrt(y))
```

**Verification**: W(0) = 0, W'(0) = 0 (since mu(0)=0), and:

```
dW/dy = 1 - 1/sqrt(y) + 1/(sqrt(y)(1+sqrt(y))) = sqrt(y)/(1+sqrt(y)) = mu(sqrt(y))
```

confirming consistency with mu(x) = x/(1+x).

### 1.3 Asymptotic Limits

| Regime | Condition | W(y) |
|--------|-----------|------|
| Deep MOND | y << 1 | (2/3) y^{3/2} + O(y^2) |
| Crossover | y ~ 1 | W(1) = 0.386 |
| Newtonian | y >> 1 | y - 2*sqrt(y) + 2*ln(sqrt(y)) ~ y |

Numerical verification:

| y | W(y) exact | W deep MOND | W Newtonian |
|---|-----------|-------------|-------------|
| 0.01 | 6.2e-4 | 6.7e-4 | 0.01 |
| 0.10 | 0.0171 | 0.0211 | 0.10 |
| 1.00 | 0.386 | 0.667 | 1.00 |
| 10.0 | 6.53 | 21.1 | 10.0 |
| 100 | 84.8 | 667 | 100 |

The deep MOND approximation is excellent for y < 0.01 and the Newtonian limit dominates for y > 100.

---

## 2. Field Energy Density

### 2.1 The Energy Functional

From conservation analysis (section\_formalism.tex, Eq. static energy):

```
E[psi] = integral d^3x [ (a*^2/8piG) W(|grad psi|^2/a*^2) + (c^2/2) rho psi ]
```

The field energy density from the kinetic term alone is:

```
rho_W(x) = (a*^2/8piG) W(|grad psi(x)|^2/a*^2)
```

### 2.2 The Fundamental Scale

The prefactor sets the energy scale:

```
a*^2/(8piG) = (2a_0/c^2)^2 / (8piG) = 4.25 x 10^{-45} kg/m^3
```

Compare to:
- rho\_crit = 8.53 x 10^{-27} kg/m^3
- rho\_b = 4.21 x 10^{-28} kg/m^3
- rho\_CDM = 2.23 x 10^{-27} kg/m^3

**The field energy scale is 4.98 x 10^{-19} times rho\_crit.** This 18-order-of-magnitude suppression is the central result.

### 2.3 Physical Origin of Suppression

The ratio can be expressed analytically:

```
[a*^2/(8piG)] / rho_crit = (4/3) * (a_0/(cH_0))^2 / c^2
```

With a\_0/(cH\_0) ~ 0.183, this gives:

```
= (4/3) * 0.0336 / c^2 ~ 5 x 10^{-19}
```

The suppression has two factors:
1. **(a\_0/(cH\_0))^2 ~ 0.034**: The MOND scale is about 1/5 of the Hubble acceleration, giving a factor ~30 suppression.
2. **1/c^2**: The relativistic suppression. Field energy density scales as (gradient)^2 / G, but the gradient is a\_0/c^2 (in 1/m units), so the energy goes as a\_0^2/(Gc^4). This is the gravitational binding energy divided by c^2 -- the standard post-Newtonian suppression.

---

## 3. Cosmic Average Field Energy

### 3.1 Setup

For a Gaussian psi perturbation field with power spectrum P\_psi(k):

```
<|grad psi|^2> = sigma_grad^2 = integral k^2 P_psi(k) * k^2 dk / (2pi^2)
```

The psi field is sourced by baryonic density perturbations:

```
psi_k = [8piG rho_b / (c^2 mu_eff k^2)] * delta_k
```

with mu\_eff = mu\_0 + L\_0/3 = 0.898 (from the background cosmological EFE with x\_bg ~ 5.5).

### 3.2 Numerical Results

Using the Eisenstein-Hu baryon-only transfer function:

| Quantity | Value |
|----------|-------|
| Coupling C = 8piG rho\_b/(c^2 mu\_eff) | 8.74 x 10^{-54} m^{-2} |
| sigma\_delta (baryon, linear, z=0) | 8.4 x 10^{-5} |
| sigma\_grad = sqrt(<\|grad psi\|^2>) | 1.41 x 10^{-31} m^{-1} |
| x\_rms = sigma\_grad / a\* | 5.29 x 10^{-5} |

The RMS dimensionless gradient from perturbations is x\_rms ~ 5 x 10^{-5}, deep in the MOND regime. This means we should use W ~ (2/3) y^{3/2}.

### 3.3 Average Energy Density

For a chi-squared-distributed y (3 DOF, as |grad psi|^2 sums 3 Gaussian components):

```
<W(y)> = 1.21 x 10^{-13}

<rho_W> = (a*^2/8piG) * <W> = 5.15 x 10^{-58} kg/m^3
```

### 3.4 Comparison to CDM

| Ratio | Value |
|-------|-------|
| <rho\_W> / rho\_crit | 6.0 x 10^{-32} |
| <rho\_W> / rho\_b | 1.2 x 10^{-30} |
| <rho\_W> / rho\_CDM | 2.3 x 10^{-31} |

**The cosmic average field energy from perturbation gradients is 31 orders of magnitude below the CDM density.**

Even using the background Hubble-flow gradient (x\_Hubble ~ 5.5, in the Newtonian regime):

```
rho_W(Hubble) = 9.6 x 10^{-44} kg/m^3 = 1.1 x 10^{-17} * rho_crit
```

This is 17 orders of magnitude below critical density.

---

## 4. Power Spectrum of rho\_W

### 4.1 Mode Coupling Structure

The energy density rho\_W(x) is a nonlinear functional of grad psi. In the deep MOND regime:

```
rho_W ~ (2/3) * |grad psi|^3 / (8piG a*)
```

This cubic dependence means the power spectrum of rho\_W involves the 6-point function of grad psi (for Gaussian fields). Schematically:

```
P_{rho_W}(k) ~ integral d^3q1 d^3q2 K(q1, q2, k-q1-q2) * P_grad(q1) P_grad(q2) P_grad(|k-q1-q2|)
```

### 4.2 Amplitude Argument

Regardless of the shape of P\_{rho\_W}(k), its amplitude is set by:

```
Omega_W = <rho_W>/rho_crit ~ 6 x 10^{-32}
```

The contribution to the matter power spectrum from rho\_W would be suppressed by:

```
(Omega_W / Omega_CDM)^2 ~ (6e-32 / 0.261)^2 ~ 5 x 10^{-62}
```

**Even if P\_{rho\_W}(k) had exactly the CDM shape, it would be 62 orders of magnitude too small to matter.**

### 4.3 Shape Analysis (Academic)

In the Newtonian limit (W ~ y), rho\_W ~ |grad psi|^2/(8piG). The power spectrum is then the standard one-loop convolution:

```
P_{|grad psi|^2}(k) = 2 * integral d^3q/(2pi)^3 * [q.(k-q)]^2 P_psi(q) P_psi(|k-q|) / (q^2 |k-q|^2)
```

This produces a spectrum that peaks at scales where P\_psi itself peaks, and falls off at both large and small k. It does NOT naturally produce a CDM-like transfer function.

---

## 5. Self-Sourcing Bootstrap

### 5.1 Modified Field Equation

If field energy gravitates (as consistency demands), the field equation becomes:

```
div[mu(x) grad psi] = -(8piG/c^2)(rho_m + rho_psi)
```

where rho\_psi = (a\*^2/8piG) W(|grad psi|^2/a\*^2).

### 5.2 Bootstrap Ratio

The key parameter is epsilon = rho\_psi / rho\_matter:

| k (h/Mpc) | delta | x | epsilon |
|-----------|-------|---|---------|
| 0.001 | 0.01 | 1.5e-3 | 2.3e-24 |
| 0.001 | 1.00 | 1.5e-1 | 2.0e-20 |
| 0.010 | 1.00 | 1.5e-2 | 2.2e-23 |
| 0.100 | 1.00 | 1.5e-3 | 2.3e-26 |

Even in the most favorable case (k = 0.001 h/Mpc, delta = 1.0), the bootstrap ratio is epsilon ~ 2 x 10^{-20}.

### 5.3 Geometric Amplification

The iterative bootstrap sums as a geometric series:

```
Total amplification = 1 / (1 - epsilon) = 1 + epsilon + epsilon^2 + ...
                    = 1 + 2 x 10^{-20} + ...
                    ~ 1.0000000000000000000 (to 19 significant figures)
```

**Self-sourcing is completely negligible at all scales and all perturbation amplitudes.**

### 5.4 Physical Understanding

The bootstrap fails because it operates on the ENERGY of the field, which is set by the prefactor a\*^2/(8piG). The field equation's LHS (the mu-modified divergence) operates on the FIELD ITSELF, not its energy. The ratio of field energy to matter energy is:

```
rho_psi / rho_m ~ (a*^2 / 8piG) * W(x^2) / rho_m
                ~ (a_0/c^2)^2 / (G rho_m) * (dimensionless factor)
                ~ (a_0^2) / (c^4 G rho_m)
                ~ (v_MOND/c)^4 << 1
```

where v\_MOND ~ sqrt(a\_0 r) is a characteristic velocity in the MOND regime. This is a fourth-power relativistic suppression.

---

## 6. What DOES Act as Effective Dark Matter in DFD

### 6.1 Phantom Dark Matter (Already Present)

The standard mechanism is the phantom dark matter density:

```
rho_phantom = (c^2/8piG) div[(mu(x)-1) grad psi]
```

Note the prefactor: **c^2/(8piG)**, NOT a\*^2/(8piG). This is a factor of:

```
c^2 / a*^2 = c^2 / (2a_0/c^2)^2 = c^6 / (4a_0^2) ~ 10^{68}
```

larger than the field energy! The phantom DM density operates at the correct energy scale for cosmological dynamics.

However, phantom DM is NOT a separate component -- it is the restatement of the MOND enhancement in Newtonian language. It is already encoded in the mu function and field equation.

### 6.2 The Temporal Dust Branch

The DFD v3.3 paper identifies a "dust branch" in the temporal sector where the psi perturbations behave as pressureless matter (w = 0, c\_s = 0). This removes the Jeans scale cutoff that kills baryon-only structure formation below ~100 Mpc. However, the dust branch contributes through its DYNAMICAL COUPLING to baryons, not through its energy density.

### 6.3 The Real Question

The correct framing is not "does field energy act as dark matter?" (answer: no, by 18+ orders of magnitude) but rather:

**Does the nonlinear, anisotropic response of the psi field to baryonic perturbations -- characterized by the tensor M\_ij = mu\_0 delta\_ij + L\_0 g\_hat\_i g\_hat\_j -- produce growth factors and a transfer function that replicate CDM phenomenology?**

This is the question addressed by the forward perturbation solver, not by field energy considerations.

---

## 7. Summary Table

| Quantity | Value | Fraction of rho\_CDM |
|----------|-------|---------------------|
| rho\_crit | 8.53 x 10^{-27} kg/m^3 | -- |
| rho\_CDM | 2.23 x 10^{-27} kg/m^3 | 1 |
| rho\_b | 4.21 x 10^{-28} kg/m^3 | 0.189 |
| a\*^2/(8piG) | 4.25 x 10^{-45} kg/m^3 | 1.9 x 10^{-18} |
| <rho\_W> (perturbation gradients) | 5.15 x 10^{-58} kg/m^3 | 2.3 x 10^{-31} |
| rho\_W(Hubble flow) | 9.60 x 10^{-44} kg/m^3 | 4.3 x 10^{-17} |
| Bootstrap epsilon (best case) | -- | 2.0 x 10^{-20} |

## 8. Conclusions

1. **W(y) = y - 2*sqrt(y) + 2*ln(1+sqrt(y))** is the exact kinetic function for the simple mu. It interpolates from (2/3)y^{3/2} in deep MOND to ~y in the Newtonian regime.

2. **The field energy is 18-31 orders of magnitude too small** to act as dark matter. The suppression is fundamental: it arises from the relativistic factor (a\_0/c^2)^2.

3. **The power spectrum of rho\_W** has the wrong shape (set by mode-coupling of grad psi) AND the wrong amplitude (suppressed by ~10^{-62} relative to CDM).

4. **Self-sourcing bootstrap** contributes a correction of order 10^{-20} -- completely negligible.

5. **The phantom dark matter mechanism** (operating through the nonlinear mu function at the c^2/(8piG) scale, not the field energy at the a\*^2/(8piG) scale) is the correct path for DFD to replicate CDM phenomenology.

---

*Computation script*: `R2_field_energy_compute.py` (in this directory)
*Prior analysis*: `agent24_gradient_energy_creative.md` (confirmed and quantified)
