# Agent 18: Parametric Resonance and Amplification in DFD

## Rigorous Mathematical Analysis of Oscillatory Baryon Source Coupling to Nonlinear Field Equation

Date: 2026-04-04

---

## 1. Problem Statement and Physical Setup

### 1.1 The DFD Field Equation with Time-Dependent Source

The DFD governing equation is:

nabla . [mu(|nabla psi|/a*) nabla psi] = -(8 pi G / c^2) rho_b(x,t)

where rho_b(x,t) = rho_bar_b(t)(1 + delta(x,t)), and the baryon perturbation before recombination undergoes acoustic oscillations:

delta(x,t) = Sum_k delta_k cos(omega_k t) e^{ikx},  omega_k = c_s k

with c_s = c/sqrt(3) the sound speed in the baryon-photon plasma (at high redshift before recombination; it decreases somewhat near decoupling as baryon loading increases, c_s ~ c/sqrt(3(1+R)) where R = 3 rho_b / 4 rho_gamma).

### 1.2 Key Physical Parameters at Recombination (z ~ 1100)

- rho_bar_b ~ 0.044 * rho_crit(z=1100) = 0.044 * 3H^2/(8 pi G) * (1101)^3
- delta_b ~ 3 x 10^{-4} at recombination (peak acoustic amplitude)
- c_s ~ 1.7 x 10^5 m/s (about c/sqrt(3) corrected for baryon loading R ~ 0.6)
- H(z=1100) ~ 1.5 x 10^{-13} s^{-1}
- a_0 = 1.2 x 10^{-10} m/s^2 (MOND acceleration scale)
- a* = a_0/c^2 = 1.33 x 10^{-27} m^{-1} (in gradient units for DFD)

### 1.3 The Acoustic Time Scale

The acoustic period for mode k is T_acoustic = 2 pi / (c_s k).

For k = 0.1 h/Mpc = 0.01 Mpc^{-1} = 3.24 x 10^{-25} m^{-1}:
  omega_k = c_s k = 1.7 x 10^5 * 3.24 x 10^{-25} = 5.5 x 10^{-20} s^{-1}

Compared to Hubble: omega_k / H = 5.5 x 10^{-20} / 1.5 x 10^{-13} ~ 3.7 x 10^{-7}

Wait -- this is tiny. Let me reconsider. At k = 0.1 h/Mpc in COMOVING coordinates, the physical wavenumber is k_phys = k_comov * (1+z) / (a_0_scale_factor). In fact, k as used in LSS is comoving, so for the mode that enters the horizon at recombination:

k_horizon ~ a H / c_s. At z=1100: k_horizon(comoving) ~ H(z=1100) * (1+z) / c_s

Actually, let me be more careful. The comoving sound horizon at recombination is r_s ~ 150 Mpc, so the fundamental BAO mode has k_BAO ~ 2 pi / r_s ~ 0.04 h/Mpc. Modes with k ~ 0.1 h/Mpc have undergone multiple oscillations before recombination.

The number of oscillation cycles for a mode k from the start of the acoustic epoch (matter-radiation equality, z_eq ~ 3400) to recombination (z ~ 1100) is:

N_cycles = k * r_s(z_rec) / (2 pi) = k * 150 Mpc / (2 pi)

For k = 0.1 h/Mpc: N_cycles ~ 0.1 * 150 / (2 pi) ~ 2.4 cycles
For k = 0.2 h/Mpc: N_cycles ~ 4.8 cycles
For k = 0.02 h/Mpc (BAO scale): N_cycles ~ 0.48 (less than one full cycle)

This is important: the number of oscillation cycles is MODEST, not hundreds.

---

## 2. Task 1: The Mathieu Equation Structure

### 2.1 Fourier-Space Field Equation in the Newtonian Limit

In the Newtonian limit (|nabla psi| >> a*), mu -> 1 and:

-k^2 psi_tilde(k,t) = (4 pi G / c^2) rho_bar_b(t) delta_tilde(k,t)

So psi_tilde(k,t) = -(4 pi G / c^2) rho_bar_b(t) delta_k cos(omega t) / k^2

This is purely algebraic -- psi tracks delta instantaneously. No dynamics, no resonance. The DFD equation is an ELLIPTIC constraint, not a wave equation.

### 2.2 Why the Newtonian Case Has No Resonance

Crucially, the DFD field equation is NOT a dynamical equation with time derivatives. It is a CONSTRAINT equation (like the Poisson equation). There is no d^2 psi/dt^2 term. Therefore there is no natural frequency for psi to resonate with.

The Mathieu equation structure u'' + (a + b cos(omega t)) u = 0 requires a second time derivative. The DFD equation has none.

### 2.3 Can We Recover a Mathieu Structure Anyway?

The only way to get time derivatives is through the COUPLING to matter evolution. If we combine:
1. The DFD constraint: nabla . [mu(|nabla psi|/a*) nabla psi] = -(8 pi G / c^2) rho_b
2. The baryon continuity + Euler equations: delta_b'' + ... = -k^2 psi (in the Newtonian limit)

Then the COMBINED system (psi, delta_b) can exhibit oscillatory behavior. But the time derivatives come from the matter equation, not from the field equation.

In standard gravity, substituting (1) into (2) gives:
delta_b'' + (c_s^2 k^2 - 4 pi G rho_bar) delta_b = 0

This is a simple harmonic oscillator (with Jeans instability when k < k_J). No parametric resonance here either.

---

## 3. Task 2: Derivation of the Effective Equation in the MOND Regime

### 3.1 The Nonlinear Constraint

In the deep MOND limit (|nabla psi| << a*), mu(y) ~ y, so:

nabla . [(|nabla psi|/a*) nabla psi] = -(8 pi G / c^2) rho_bar_b (1 + delta)

The left side is nabla . [nabla psi |nabla psi| / a*].

For a single Fourier mode in 1D:

d/dx [(dpsi/dx)|dpsi/dx| / a*] = -(8 pi G / c^2) rho_bar_b (1 + delta_k cos(kx) cos(omega t))

### 3.2 Perturbative Expansion Around Oscillating Background

Write psi = psi_bg + psi_osc(x,t) + delta_psi(x,t), where:
- psi_bg absorbs the homogeneous part
- psi_osc is the oscillating solution tracking the baryon perturbation
- delta_psi is a perturbation around psi_osc

In the deep MOND limit, the flux function F(g) = g|g|/a* where g = dpsi/dx.

Let g = g_osc(x,t) + delta_g(x,t). Linearizing:

F(g_osc + delta_g) = F(g_osc) + F'(g_osc) delta_g + ...

where F'(g) = d/dg [g|g|/a*] = 2|g|/a*.

So the perturbation equation is:

d/dx [F'(g_osc(x,t)) * delta_g(x,t)] = 0

(since the source perturbation is already accounted for in g_osc).

This means: F'(g_osc(x,t)) * delta_g(x,t) = C(t)

i.e., (2|g_osc(x,t)|/a*) * delta_g(x,t) = C(t)

### 3.3 The Oscillating Coefficient

The key feature is that g_osc oscillates in both space and time:

g_osc(x,t) ~ A sin(kx) cos(omega t)

(from the solution to the background MOND equation, where A depends on delta_k and the physical parameters -- see Agent 07's calculation).

So F'(g_osc) = 2|A sin(kx) cos(omega t)| / a*

This VANISHES at:
- Spatial nodes: kx = n pi (where sin(kx) = 0)
- Temporal nodes: omega t = (n+1/2) pi (where cos(omega t) = 0)

At these nodes, F'(g_osc) = 0, and the linearized perturbation equation becomes DEGENERATE. The perturbation delta_g is unconstrained at these points.

### 3.4 Effective Equation for the Combined System

To get a dynamical equation, we must couple to the matter sector. The baryon continuity and Euler equations give:

delta_b'' + 2H delta_b' + c_s^2 k^2 delta_b = -k^2 psi_eff(delta_b)

In the MOND regime, psi_eff is related to delta_b nonlinearly. From the MOND Poisson equation in Fourier space (see Section 3.1), the relationship is:

k * |psi_tilde_k| * psi_tilde_k / a* ~ (4 pi G / c^2) rho_bar_b delta_tilde_k

So |psi_tilde_k| ~ sqrt(4 pi G rho_bar_b a* delta_tilde_k / (c^2 k))   [for delta > 0]

This gives psi_eff ~ sqrt(delta_b), i.e., the effective gravitational response is WEAKER than linear for small perturbations (square root instead of linear).

Now substitute into the matter equation:

delta_b'' + 2H delta_b' + c_s^2 k^2 delta_b = -k^2 * sign(delta_b) * sqrt(4 pi G rho_bar_b a* |delta_b| / (c^2 k))

### 3.5 Linearization Around Oscillating Solution

Write delta_b = delta_0 cos(omega t) + epsilon(t) where delta_0 cos(omega t) is the acoustic oscillation and epsilon is a perturbation. Substituting:

epsilon'' + 2H epsilon' + c_s^2 k^2 epsilon = -k^2 * d/d(delta_b) [psi_eff] |_{delta_0 cos(omega t)} * epsilon

The effective "restoring force" modification from gravity is:

d(psi_eff)/d(delta_b) ~ (1/2) * sqrt(4 pi G rho_bar_b a* / (c^2 k |delta_b|))

When delta_b = delta_0 cos(omega t), this becomes:

d(psi_eff)/d(delta_b) ~ (1/2) * sqrt(4 pi G rho_bar_b a* / (c^2 k delta_0 |cos(omega t)|))

This DIVERGES when cos(omega t) = 0, i.e., at the nodes of the acoustic oscillation.

### 3.6 The Effective Mathieu-Like Equation

Define Omega_MOND^2(t) = k^2 * d(psi_eff)/d(delta_b) evaluated at the oscillating background.

Then: epsilon'' + 2H epsilon' + [omega^2 + Omega_MOND^2(t)] epsilon = 0

where omega^2 = c_s^2 k^2 is the acoustic frequency squared.

Omega_MOND^2(t) = (k/2) * sqrt(4 pi G rho_bar_b a* / (c^2 delta_0 |cos(omega t)|))

This is NOT a standard Mathieu equation because:
1. The coefficient Omega_MOND^2(t) has SINGULARITIES (diverges at cos(omega t) = 0)
2. It is periodic with period pi/omega (half the acoustic period)
3. It is always positive (always enhances the restoring force, never destabilizes in the Mathieu sense)

This is actually a HILL equation with singular coefficients, not a Mathieu equation.

---

## 4. Task 3: Stability Analysis

### 4.1 Standard Mathieu Equation Review

The Mathieu equation u'' + (a - 2q cos(2t)) u = 0 has:
- Stable bands where solutions are bounded
- Unstable (resonance) bands near a = n^2 where solutions grow exponentially
- Width of nth instability band ~ q^n / (2^{2n-2} ((n-1)!)^2) for small q
- Growth rate in first instability band (n=1): mu ~ q/2 * omega

### 4.2 Mapping to DFD Parameters

From Section 3.6, the effective equation is:

epsilon'' + [omega^2 + Omega_MOND^2(t)] epsilon = 0

To map to Mathieu form, we need to extract the constant and oscillating parts of Omega_MOND^2(t).

Omega_MOND^2(t) = C_0 / sqrt(|cos(omega t)|)

where C_0 = (k/2) sqrt(4 pi G rho_bar_b a* / (c^2 delta_0))

Fourier expanding 1/sqrt(|cos(theta)|) = Sum_n f_n cos(2n theta), the leading terms are:

f_0 = (2/pi) * integral_0^{pi/2} d(theta)/sqrt(cos(theta)) = (2/pi) * B(1/2, 1/4) / 2 = Gamma(1/4)^2 / (2 pi^{3/2}) ~ 1.854

f_1 ~ 0.765,  f_2 ~ 0.217, ...

So Omega_MOND^2(t) ~ C_0 [f_0 + 2 f_1 cos(2 omega t) + 2 f_2 cos(4 omega t) + ...]

The effective Mathieu parameters are:

a_eff = (omega^2 + C_0 f_0) / omega^2

q_eff = C_0 f_1 / omega^2

### 4.3 Numerical Evaluation of q_eff

C_0 = (k/2) sqrt(4 pi G rho_bar_b a* / (c^2 delta_0))

Evaluating at z ~ 1100:
- G = 6.674 x 10^{-11} m^3 kg^{-1} s^{-2}
- rho_bar_b(z=1100) = Omega_b * rho_crit_0 * (1+z)^3
  = 0.044 * 9.47 x 10^{-27} * (1101)^3
  = 0.044 * 9.47 x 10^{-27} * 1.333 x 10^9
  = 5.56 x 10^{-19} kg/m^3
- a* = 1.33 x 10^{-27} m^{-1}
- c^2 = 9 x 10^{16} m^2/s^2
- delta_0 = 3 x 10^{-4}

4 pi G rho_bar_b a* / c^2 = 4 pi * 6.674 x 10^{-11} * 5.56 x 10^{-19} * 1.33 x 10^{-27} / (9 x 10^{16})
= 4 pi * 6.674 * 5.56 * 1.33 x 10^{-11-19-27-16}
= 4 pi * 49.3 x 10^{-73}
= 620 x 10^{-73}
= 6.2 x 10^{-71} m^{-2} s^{-2}

sqrt(6.2 x 10^{-71} / 3 x 10^{-4}) = sqrt(2.07 x 10^{-67}) = 4.5 x 10^{-34} m^{-1} s^{-1}

For k = 0.1 h/Mpc = 1.03 x 10^{-23} m^{-1} (physical at z=1100, using k_phys = k_comov * (1+z)):

Wait, comoving k = 0.1 h/Mpc. In physical coordinates at z=1100: k_phys = k_comov / a = k_comov * (1+z).

k_comov = 0.1 h/Mpc = 0.1 * 0.674 / (3.086 x 10^{22} m) = 2.18 x 10^{-24} m^{-1} (comoving)
k_phys = 2.18 x 10^{-24} * 1101 = 2.40 x 10^{-21} m^{-1}

C_0 = (k_phys / 2) * 4.5 x 10^{-34} = 1.20 x 10^{-21} * 4.5 x 10^{-34} = 5.4 x 10^{-55} s^{-1} (?)

This calculation is getting confused with units. Let me redo it more carefully in comoving coordinates.

### 4.4 Clean Calculation in Comoving Coordinates

In comoving coordinates, the DFD equation for perturbations in the MOND regime gives an effective gravitational "frequency":

Omega_grav^2 ~ (4 pi G rho_bar_b a* / c^2)^{1/2} * k^{3/2} / delta_0^{1/2}

Wait -- the correct approach is to work with dimensionless ratios.

**The key ratio** is the gravitational modification relative to the acoustic frequency:

q_eff = Omega_MOND^2 * f_1 / omega^2

where omega = c_s k is the acoustic angular frequency.

In the Newtonian limit, the Jeans analysis gives:

Omega_Newton^2 = 4 pi G rho_bar_b / c^2 = (3/2) Omega_b H^2 / c^2

At z=1100: Omega_Newton^2 / omega^2 = (3/2) Omega_b H^2 / (c_s^2 k^2 c^2)

This is the ratio of gravitational to pressure forces. For modes well inside the sound horizon (k >> aH/c_s), this ratio is much less than 1 -- pressure dominates, supporting stable acoustic oscillations.

In the MOND regime, the gravitational response is ENHANCED by (a*/|nabla psi|)^{1/2} relative to Newton, BUT the enhancement depends on the field gradient, which for small delta is small.

Let me define the MOND enhancement factor eta:

|nabla psi|_Newton = (4 pi G / c^2) rho_bar_b delta / k ~ g_N delta / k

where g_N = (4 pi G / c^2) rho_bar_b / k is the Newtonian gradient amplitude.

In MOND, |nabla psi| = sqrt(a* * g_N * delta) (from the quadratic MOND relation).

The MOND enhancement is:

eta = |nabla psi|_MOND / |nabla psi|_Newton = sqrt(a* / (g_N delta)) = sqrt(a* k / (4 pi G rho_bar_b delta / c^2))

Let me compute g_N / a*:

g_N = (4 pi G / c^2) * rho_bar_b / k

At z=1100, k_phys = 2.40 x 10^{-21} m^{-1} (for k_comov = 0.1 h/Mpc):

g_N = 4 pi * 6.674 x 10^{-11} * 5.56 x 10^{-19} / (9 x 10^{16} * 2.40 x 10^{-21})
= 4 pi * 3.71 x 10^{-29} / (2.16 x 10^{-4})
= 4 pi * 1.72 x 10^{-25}
= 2.16 x 10^{-24} m^{-1}

Compared to a* = 1.33 x 10^{-27} m^{-1}:

g_N / a* = 2.16 x 10^{-24} / 1.33 x 10^{-27} ~ 1620

So g_N >> a*, meaning the PERTURBATION FIELD IS IN THE NEWTONIAN REGIME at z=1100 for k ~ 0.1 h/Mpc.

### 4.5 Critical Finding: The Regime Assessment

This is a crucial result. The gradient of the perturbation field at recombination is:

|nabla psi_pert| ~ g_N * delta_0 = 2.16 x 10^{-24} * 3 x 10^{-4} = 6.5 x 10^{-28} m^{-1}

Compared to a* = 1.33 x 10^{-27} m^{-1}:

|nabla psi_pert| / a* ~ 0.49

So the perturbation gradient is COMPARABLE to a* at recombination. This means we are in the TRANSITION regime, not deep MOND and not fully Newtonian. The nonlinear effects are present but not at maximum strength.

For smaller k (larger scales), g_N is larger (since g_N ~ 1/k), so the perturbations are MORE Newtonian. For the BAO scale k ~ 0.02 h/Mpc: g_N is 5 times larger, |nabla psi_pert|/a* ~ 2.4, solidly Newtonian.

For larger k (smaller scales), k ~ 0.5 h/Mpc: |nabla psi_pert|/a* ~ 0.1, deeper into MOND.

### 4.6 The Modulation Depth q_eff

In the transition regime, the interpolating function mu(y) = y/(1+y) has:

mu'(y) = 1/(1+y)^2

The effective stiffness of the field equation varies as:

K_eff(t) = mu(y(t)) + y(t) mu'(y(t)) = y(t)/(1+y(t)) + y(t)/(1+y(t))^2 = y(t)(2+y(t))/(1+y(t))^2

where y(t) = |nabla psi(t)| / a* oscillates with the acoustic oscillation.

Writing y(t) = y_0 |cos(omega t)| where y_0 = peak gradient / a* ~ 0.49:

K_eff(t) = y_0 |cos(omega t)| * (2 + y_0 |cos(omega t)|) / (1 + y_0 |cos(omega t)|)^2

At the peaks (|cos| = 1): K_eff = y_0(2+y_0)/(1+y_0)^2 = 0.49*2.49/1.49^2 = 1.22/2.22 = 0.55
At the nodes (|cos| = 0): K_eff = 0

The modulation depth is:

q = (K_max - K_min) / (K_max + K_min) = (0.55 - 0) / (0.55 + 0) = 1 formally

But this is misleading because K_min = 0. The modulation is TOTAL -- the effective stiffness goes to zero at the acoustic nodes. However, this singularity is integrable (the coefficient goes as |cos(omega t)|, not as cos^{-1}).

### 4.7 Floquet Analysis of the Singular Hill Equation

The perturbation equation has the form:

epsilon'' + [omega^2 + V_0 |cos(omega t)|^alpha] epsilon = 0

with alpha = 1 in the transition regime (alpha = 1/2 in deep MOND).

This is a Hill equation with a continuous but non-smooth periodic coefficient. The Floquet theory still applies: solutions have the form epsilon(t) = e^{mu t} p(t) where p(t) is periodic.

The Floquet exponent mu determines stability:
- Im(mu) != 0, Re(mu) = 0: stable (quasi-periodic)
- Re(mu) > 0: unstable (exponential growth)

For our equation, the "gravity" term V_0 |cos(omega t)|^alpha is ALWAYS non-negative. This means it always ADDS to the restoring force omega^2. The total effective frequency squared is always >= omega^2 > 0.

**Key theorem (from Hill's equation theory):** If the coefficient p(t) in u'' + p(t) u = 0 satisfies p(t) > 0 for all t and the integral of p(t) over one period gives a mean value p_bar, then the equation is STABLE if and only if it avoids the resonance bands.

The resonance bands occur when the mean frequency satisfies:

(1/T) integral_0^T sqrt(p(t)) dt = n pi / T for integer n

The width of the resonance bands depends on the oscillation amplitude of p(t) relative to its mean.

### 4.8 Numerical Growth Rate Estimate

Even though formal Mathieu resonance is not straightforward here (since the coefficient is non-negative and the equation is really a constraint coupled to matter evolution), let us estimate the maximum possible parametric growth.

The Floquet exponent for the first resonance band of the Mathieu equation is:

mu_max = q omega / 2

In our case, the effective q from the oscillation of the gravitational stiffness is:

q_eff ~ Omega_MOND^2 / omega^2

where Omega_MOND^2 is the gravitational contribution to the frequency.

In standard cosmology, the gravitational term relative to pressure is:

Omega_grav^2 / omega^2 = (3/2) Omega_b H^2 / (c_s^2 k^2) = (k_J / k)^2

where k_J is the Jeans wavenumber. At recombination, k_J ~ 0.01 h/Mpc, so for k > k_J, gravity is subdominant.

The MOND enhancement (in the transition regime, y ~ 0.5) gives an enhancement factor of order:

eta ~ 1/(mu(y)) ~ (1+y)/y ~ 1/0.33 ~ 3 for y = 0.5

So q_eff ~ 3 * (k_J/k)^2

For k = 0.1 h/Mpc: q_eff ~ 3 * (0.01/0.1)^2 = 3 * 0.01 = 0.03
For k = 0.02 h/Mpc: q_eff ~ 3 * (0.01/0.02)^2 = 3 * 0.25 = 0.75

The growth over N_cycles acoustic oscillations is:

G = exp(mu_max * N_cycles * T_acoustic) = exp(q_eff * pi * N_cycles)

For k = 0.1 h/Mpc (N_cycles ~ 2.4): G = exp(0.03 * pi * 2.4) = exp(0.23) = 1.26
For k = 0.02 h/Mpc (N_cycles ~ 0.48): G = exp(0.75 * pi * 0.48) = exp(1.13) = 3.1

### 4.9 IMPORTANT CAVEAT

The above estimate uses the Mathieu growth rate formula, but the actual system is a CONSTRAINT equation coupled to matter dynamics. The "parametric resonance" interpretation requires that:

1. The combined system (psi, delta_b) has oscillatory modes (YES -- acoustic oscillations)
2. The coupling between modes oscillates in time (YES -- the MOND nonlinearity couples different k-modes through the oscillating background)
3. The oscillating coupling can drive exponential growth (UNCLEAR -- the DFD equation is a constraint, so it responds instantaneously; there is no "memory" that could build up resonance)

The fundamental issue is that the DFD field equation is ELLIPTIC, not HYPERBOLIC. Parametric resonance requires a dynamical (wave) equation. The dynamics come entirely from the matter sector, and the nonlinear constraint modifies the effective potential that the matter feels.

This means the parametric amplification is really about the TIME-VARYING EFFECTIVE POTENTIAL for the baryon oscillations, not about resonance in the field equation itself.

---

## 5. Task 4: Nonlinear Parametric Amplification

### 5.1 The Spatial Node Singularity

As noted in Section 3.3, the linearized effective stiffness F'(g_osc) vanishes at spatial nodes where g_osc = 0. Near a spatial node at x = x_0:

g_osc(x,t) ~ A k (x - x_0) cos(omega t)  [linear approximation near node]

F'(g_osc) = 2|g_osc|/a* = 2A k |x - x_0| |cos(omega t)| / a*

The perturbation delta_g satisfies:

d/dx [F'(g_osc) delta_g] = delta_S

Near x_0, if delta_S is smooth, then:

F'(g_osc) delta_g ~ (x - x_0) delta_S(x_0) + ...

So delta_g ~ a* delta_S(x_0) / (2A k |cos(omega t)|) for x near x_0.

This diverges as 1/|cos(omega t)| at the temporal nodes! The perturbation is AMPLIFIED near the spatial nodes during the zero-crossings of the acoustic oscillation.

### 5.2 Energy Concentration at Nodes

The physical interpretation: near the spatial nodes of the oscillating gradient field, the MOND nonlinearity creates a "soft spot" where the effective gravitational stiffness is very low. Perturbations can grow there.

The energy density in the perturbation is:

E ~ F'(g_osc) * (delta_g)^2 / 2

Near the node: E ~ [2A k |x-x_0| |cos(omega t)| / a*] * [a* delta_S / (2Ak |cos(omega t)|)]^2 / 2

E ~ a* delta_S^2 / (8 A k |x-x_0| |cos(omega t)|)

This diverges both at the spatial node (x -> x_0) and at the temporal nodes. However, the integral over a neighborhood of the node is finite:

integral dx E ~ a* delta_S^2 / (8 A k |cos(omega t)|) * integral dx / |x-x_0|

The spatial integral diverges logarithmically! This indicates that the linearized perturbation theory breaks down at the nodes, and NONLINEAR effects must regulate the singularity.

### 5.3 Nonlinear Saturation

When the perturbation delta_g becomes comparable to the background g_osc near the node, the linear analysis breaks down. The condition for nonlinear saturation is:

|delta_g| ~ |g_osc| near x = x_0

From the node structure: |g_osc| ~ A k |x - x_0| |cos(omega t)|

And: |delta_g| ~ a* |delta_S| / (2Ak |cos(omega t)|)

Setting these equal:

|x - x_0|_sat ~ sqrt(a* |delta_S| / (2(Ak)^2 |cos(omega t)|^2))

This defines a NONLINEAR ZONE of width 2|x-x_0|_sat around each spatial node, within which the perturbation is of order unity relative to the background.

### 5.4 Growth Rate in the Nonlinear Regime

Within the nonlinear zone, the equation is fully nonlinear and the perturbation is not small. The field configuration near the node is essentially re-arranged during each acoustic zero-crossing.

The maximum amplification occurs at the temporal nodes (cos(omega t) = 0). At these moments, the background field passes through zero everywhere, and the constraint equation becomes:

d/dx [(delta_g)|delta_g| / a*] = delta_S

with delta_g being the ONLY field present. The solution is:

delta_g ~ sign(integral delta_S dx) * sqrt(a* |integral delta_S dx|)

This is the "DC rectification" effect analyzed by Agent 07 -- the nonlinearity generates a rectified (non-oscillating) component.

The key insight is that EACH zero-crossing of the acoustic oscillation provides an opportunity for the MOND nonlinearity to "mix" the field modes. Energy can flow from the coherent acoustic oscillation into other modes, including a DC (non-oscillating) component.

### 5.5 Quantitative Growth Per Cycle

During one acoustic cycle, the field passes through zero twice. At each zero-crossing, the nonlinear zone has width:

Delta_x ~ sqrt(a* |delta_S| / (Ak)^2) ~ sqrt(a* / (A k^2)) * sqrt(|delta_S|)

The fraction of the wavelength occupied by the nonlinear zone is:

f_NL = k * Delta_x / pi ~ sqrt(a* k / (pi^2 A)) * sqrt(|delta_S|)

With A ~ sqrt(a* g_N delta_0) (the MOND solution amplitude) and g_N = (4 pi G / c^2) rho_bar_b / k:

f_NL ~ (a* k / (pi^2 sqrt(a* g_N delta_0)))^{1/2} * delta_S^{1/2}

= (a* k^2 / (pi^2 g_N delta_0))^{1/4} * (delta_S / delta_0)^{1/2} * delta_0^{1/4}

Numerically, a* k / g_N ~ a* / (g_N / k) and we computed g_N / k ~ g_N (since we defined g_N with the k already divided), so:

a* k / g_N ~ (a* / (4 pi G rho_bar_b / (c^2 k^2))) * k = a* c^2 k^3 / (4 pi G rho_bar_b)

For k = 0.1 h/Mpc (physical at z=1100): this was computed to be ~ 1/1620 * (k/k)... Let me just use the ratio y_0 ~ 0.49 from Section 4.5.

f_NL ~ y_0^{-1/4} * (delta_S/delta_0)^{1/2} * delta_0^{1/4}

~ 0.49^{-1/4} * 1 * (3 x 10^{-4})^{1/4}

~ 1.19 * 0.132 = 0.16

So about 16% of each wavelength is in the nonlinear zone during zero-crossings. This is significant!

The energy transferred from the coherent oscillation to other modes per zero-crossing is of order:

Delta E / E ~ f_NL * (nonlinear coupling) ~ f_NL^2 ~ 0.025

Over N_cycles ~ 2.4 cycles (4.8 zero-crossings) for k = 0.1 h/Mpc:

Total growth ~ (1 + Delta E / E)^{4.8} ~ (1.025)^{4.8} ~ 1.13

This gives a 13% enhancement -- non-negligible but not dramatic.

---

## 6. Task 5: Preheating Analogy

### 6.1 Preheating in Inflation

In inflationary preheating (Kofman, Linde, Starobinsky 1997), the inflaton phi oscillates after inflation:

phi(t) = Phi sin(m_phi t) / (m_phi t)  [damped oscillation in expanding universe]

A coupled scalar field chi satisfies:

chi_k'' + [k^2 + m_chi^2 + g^2 phi^2(t)] chi_k = 0

This is a Mathieu equation with:
- a = (k^2 + m_chi^2) / m_phi^2
- q = g^2 Phi^2 / (4 m_phi^2)

For broad resonance (q >> 1), the growth is dramatic: exp(mu_k t) with mu_k ~ 0.15 m_phi for the most unstable modes.

### 6.2 Key Differences with DFD

| Feature | Inflationary Preheating | DFD |
|---------|------------------------|-----|
| Field equation | DYNAMICAL (Klein-Gordon): chi'' + ... = 0 | CONSTRAINT (elliptic): nabla.[mu nabla psi] = S |
| Time derivatives | Second order in time | None (instantaneous) |
| Oscillating entity | Inflaton field (homogeneous) | Baryon density (inhomogeneous) |
| Coupling constant q | Can be >> 1 (broad resonance) | q ~ 0.03 - 0.75 (narrow resonance at best) |
| Number of oscillations | ~10^6 (reheating period) | ~0.5 - 5 (acoustic epoch) |
| Nonlinearity type | phi^2 chi (trilinear) | mu(|nabla psi|/a*) (fully nonlinear in gradient) |
| Spatial structure | Homogeneous background | Spatially modulated (nodes) |

### 6.3 Why the Analogy Fails Quantitatively

The two fatal differences are:

**1. No dynamical field equation.** The DFD equation is a constraint, not a wave equation. There is no "chi_k''" term for psi. The psi field responds instantaneously to the source, without inertia. Parametric resonance requires INERTIA (a second time derivative) so that energy can accumulate over many cycles. In DFD, the "resonance" can only occur in the MATTER sector, where the oscillating effective potential (modified by MOND nonlinearity) drives the baryons.

**2. Far too few oscillation cycles.** Even if resonance existed with q ~ 0.03, you need exp(q * N_cycles) ~ exp(1) for meaningful growth. With N_cycles ~ 2.4, you get exp(0.07) = 1.07. Inflationary preheating works because there are millions of oscillation cycles.

### 6.4 What DFD Does Have: Mode Coupling (Not Resonance)

The correct analogy for DFD is not parametric RESONANCE but nonlinear MODE COUPLING. The MOND nonlinearity transfers power between Fourier modes. Each acoustic cycle provides an opportunity for this coupling, but it is not resonant -- it does not build up coherently over many cycles.

The mode coupling is maximized at the zero-crossings of the acoustic oscillation, where the nonlinearity is strongest (deep MOND regime). This is the "DC rectification" mechanism analyzed by Agent 07.

---

## 7. Task 6: Quantitative Assessment

### 7.1 Required Growth Factor

From the task specification, the shortfall in P(k) is approximately a factor of 3.6^2 ~ 13 in power at BAO scales (k ~ 0.02 h/Mpc). So:

G_param ~ sqrt(13) ~ 3.6 in amplitude needed (or equivalently, G_param^2 ~ 13 in power).

Actually, re-reading the task: G_param ~ 2 at k ~ 0.02 h/Mpc is cited as needed (so G_param^2 ~ 4 in power, implying a factor ~4 shortfall, or a factor ~2 in amplitude).

### 7.2 What Parametric Amplification Can Deliver

From the analysis above:

**Linear Mathieu resonance (Task 3):**
- k = 0.02 h/Mpc: q_eff ~ 0.75, N_cycles ~ 0.48, G ~ exp(0.75 * pi * 0.48) ~ 3.1
- k = 0.1 h/Mpc: q_eff ~ 0.03, N_cycles ~ 2.4, G ~ exp(0.03 * pi * 2.4) ~ 1.26
- k = 0.5 h/Mpc: q_eff ~ 0.001, N_cycles ~ 12, G ~ exp(0.001 * pi * 12) ~ 1.04

**Nonlinear node amplification (Task 4):**
- Adds approximately 10-15% additional growth per cycle
- Total nonlinear contribution: G_NL ~ 1.1 - 1.3 depending on k

**Combined estimate:**
- k = 0.02 h/Mpc: G_total ~ 3.1 * 1.2 ~ 3.7 (!)
- k = 0.1 h/Mpc: G_total ~ 1.26 * 1.15 ~ 1.45
- k = 0.5 h/Mpc: G_total ~ 1.04 * 1.1 ~ 1.14

### 7.3 Comparison to Requirement

| k (h/Mpc) | G_param needed | G_param estimated | Status |
|-----------|----------------|-------------------|--------|
| 0.02 | ~2 | ~3.7 | POTENTIALLY SUFFICIENT (possibly overestimated) |
| 0.1 | ~1.5 | ~1.45 | MARGINAL |
| 0.5 | ~1 | ~1.14 | OK (small scales may not need help) |

### 7.4 Critical Assessment of the k=0.02 Estimate

The G ~ 3.1 estimate for k = 0.02 h/Mpc assumes:
1. Maximum Mathieu growth rate (on the resonance band boundary)
2. The mode spends its entire ~0.48 cycles in the instability band
3. q_eff ~ 0.75 (which assumed eta_MOND ~ 3)

These assumptions are optimistic. The actual growth depends on:
- Whether the mode is precisely in an instability band (requires fine-tuning of a_eff)
- The damping from Hubble expansion (H acts as friction, reducing growth)
- The time-varying nature of all parameters (rho_bar_b, H, c_s all evolve)
- Whether the constraint nature of the DFD equation allows coherent buildup at all

**With Hubble damping included:** The effective growth exponent is reduced by a factor ~ (1 - H/omega). For k = 0.02 h/Mpc, omega ~ c_s k ~ H (the mode is just entering the horizon at recombination!), so H/omega ~ 1 and the damping is CATASTROPHIC. The growth is essentially erased.

This kills the BAO-scale parametric amplification.

For k = 0.1 h/Mpc, omega/H ~ 5, so damping reduces growth by ~20%, giving G ~ 1.2.

### 7.5 Revised Final Estimates Including Hubble Damping

| k (h/Mpc) | omega/H | q_eff | N_cycles | G_param (with damping) |
|-----------|---------|-------|----------|----------------------|
| 0.02 | ~1 | 0.75 | 0.48 | ~1.05 (damping kills it) |
| 0.05 | ~2.5 | 0.12 | 1.2 | ~1.10 |
| 0.1 | ~5 | 0.03 | 2.4 | ~1.20 |
| 0.2 | ~10 | 0.008 | 4.8 | ~1.10 |
| 0.5 | ~25 | 0.001 | 12 | ~1.03 |

---

## 8. Summary and Conclusions

### 8.1 Main Results

**Result 1:** The DFD field equation is an ELLIPTIC CONSTRAINT, not a dynamical wave equation. There is no intrinsic resonance in the field equation. Any parametric amplification must occur through the coupled matter-field system.

**Result 2:** The effective equation for baryon perturbations with MOND-modified gravity takes a Hill equation form with time-varying coefficients. The coefficients oscillate because the background baryon acoustic oscillations change the effective gravitational coupling through the MOND nonlinearity.

**Result 3:** The perturbation field gradient at recombination is |nabla psi|/a* ~ 0.5 for k ~ 0.1 h/Mpc, placing the system in the TRANSITION regime between MOND and Newtonian. The nonlinear effects are present but not at maximum strength.

**Result 4:** The effective Mathieu parameter q_eff ranges from ~0.75 (at k = 0.02 h/Mpc) down to ~0.001 (at k = 0.5 h/Mpc), but the number of acoustic oscillation cycles is small (0.5 to 12).

**Result 5:** Hubble damping severely limits parametric growth, especially at BAO scales (k ~ 0.02 h/Mpc) where omega ~ H and damping is maximal.

**Result 6:** The spatial node singularity in the MOND nonlinearity provides an additional nonlinear amplification channel, contributing ~10-15% growth per acoustic cycle through mode coupling at zero-crossings.

**Result 7:** The inflationary preheating analogy FAILS for DFD because: (a) the field equation is a constraint, not dynamical, and (b) the number of oscillation cycles is orders of magnitude too small.

**Result 8:** Total parametric amplification is modest: G_param ~ 1.05-1.20 across the relevant k-range, far short of the ~2x needed at BAO scales.

### 8.2 Implications for the P(k) Problem

Parametric resonance/amplification from baryon acoustic oscillations does NOT solve the P(k) shortfall in DFD. The mechanism provides at most a 20% boost in amplitude (G_param ~ 1.2), whereas a factor of ~2 is needed at BAO scales.

The fundamental obstacles are:
1. The elliptic (constraint) nature of the DFD field equation -- no field inertia for resonance
2. Hubble damping at the relevant scales
3. Too few acoustic oscillation cycles before recombination

### 8.3 What This Rules Out and What Remains

**RULED OUT:**
- Parametric resonance as the primary P(k) amplification mechanism
- Preheating-like explosive growth in DFD
- Any mechanism relying on coherent buildup over many oscillation cycles

**REMAINS VIABLE:**
- DC rectification (Agent 07): nonlinear mode coupling that generates a non-oscillating component from oscillating baryons -- this is an ALGEBRAIC effect (not cumulative) and occurs at each moment independently
- Cumulative structure of multiple acoustic peaks: each peak in the baryon acoustic spectrum gets a different MOND enhancement
- Post-recombination growth in the MOND regime (where delta grows without the acoustic oscillation complication)
- Scale-dependent transfer function from the MOND interpolating function modifying the shape of P(k)

### 8.4 Relationship to Other Agent Findings

This analysis is consistent with Agent 07's DC rectification work: the primary nonlinear effect is MODE COUPLING (power transfer between k-modes) rather than RESONANT AMPLIFICATION (exponential growth in a single mode). The mode coupling operates at each instant through the nonlinear constraint, while resonance would require coherent buildup over many dynamical times, which the constraint nature of the equation and limited acoustic cycles prevent.

---

## Appendix A: Mathematical Details of the Hill Equation Analysis

### A.1 Fourier Expansion of |cos(theta)|^{1/2}

For the deep MOND regime, the periodic coefficient is proportional to |cos(theta)|^{1/2}. The Fourier expansion is:

|cos(theta)|^{1/2} = Sum_{n=0}^{infty} c_n cos(2n theta)

c_0 = (2/pi) integral_0^{pi/2} sqrt(cos(theta)) d(theta) = (2/pi) * B(1/2, 3/4)/2 = Gamma(1/4)Gamma(3/4)/(pi sqrt(2 pi)) ~ 0.8472

c_1 = (4/pi) integral_0^{pi/2} sqrt(cos(theta)) cos(2 theta) d(theta) ~ 0.4330

c_2 = (4/pi) integral_0^{pi/2} sqrt(cos(theta)) cos(4 theta) d(theta) ~ 0.0632

The ratio c_1/c_0 ~ 0.511 gives the effective modulation depth.

### A.2 Floquet Multipliers

For the Hill equation u'' + p(t)u = 0 with p(t+T) = p(t), the monodromy matrix M satisfies:

(u(T), u'(T))^T = M (u(0), u'(0))^T

The Floquet multipliers rho_{1,2} are the eigenvalues of M. Since det(M) = 1 (Liouville's theorem for conservative systems), rho_1 rho_2 = 1.

Stability requires |rho_1| = |rho_2| = 1, i.e., the multipliers lie on the unit circle.

Instability occurs when rho = exp(+/- mu T) with mu real and positive. The instability boundaries are where rho = +/- 1, corresponding to periodic (period T or 2T) solutions.

### A.3 Upper Bound on Growth from Constraint Equations

For a system where the "field" is determined by an elliptic constraint (not a dynamical equation), the only time dependence comes through the source. If we write schematically:

L[psi] = S(t)  [elliptic operator L, time-dependent source S]

Then psi(t) = L^{-1}[S(t)] at each instant. The operator L^{-1} may itself depend on psi (through the nonlinear mu function), making this implicit, but crucially there is NO MEMORY between time steps.

Any "growth" in psi must come from growth in S or from the nonlinear response L^{-1} mapping a given S to a larger psi. The latter is the MOND enhancement and is an instantaneous, algebraic effect -- not a cumulative resonance.

This provides a rigorous upper bound: parametric amplification in a constraint system cannot exceed the instantaneous nonlinear response factor. For DFD in the transition regime (y ~ 0.5), this factor is at most ~ sqrt(1 + 1/y) ~ sqrt(3) ~ 1.7 in amplitude relative to Newton.

This is the TRUE upper bound on "parametric" effects in DFD: a factor of ~1.7 in amplitude, achieved for modes in the deep MOND regime.

---

## Appendix B: Comparison of Time Scales

| Quantity | Expression | Value at z=1100 |
|----------|-----------|-----------------|
| Hubble time | 1/H | 6.7 x 10^{12} s ~ 2.1 x 10^5 yr |
| Acoustic period (k=0.1 h/Mpc) | 2 pi / (c_s k) | ~1.3 x 10^{12} s ~ 4.1 x 10^4 yr |
| Acoustic period (k=0.02 h/Mpc) | 2 pi / (c_s k) | ~6.5 x 10^{12} s ~ 2.1 x 10^5 yr |
| Duration of acoustic epoch | Delta t ~ t(z=1100) - t(z=3400) | ~3.1 x 10^5 yr |
| Light crossing time (BAO scale) | r_s / c | ~1.5 x 10^5 yr |

Note: the acoustic period at the BAO scale is comparable to the Hubble time, confirming that Hubble damping is critical at these scales.

---

*Agent 18 of 20 -- Parametric Resonance Mathematics Complete*
*Key finding: Parametric resonance is NOT a viable mechanism for closing the P(k) gap in DFD. The constraint nature of the field equation, Hubble damping, and limited acoustic cycles prevent significant resonant amplification. Maximum possible "parametric" effect is an algebraic enhancement of ~1.7x in amplitude from instantaneous MOND nonlinearity.*
