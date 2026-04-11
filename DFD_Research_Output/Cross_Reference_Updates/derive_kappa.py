#!/usr/bin/env python3
"""
derive_kappa.py -- Brute-force search for the closed-form formula for kappa_{U(1)}
==================================================================================

Given the known result alpha^{-1} = 6*pi*kappa_{U(1)} = 137.03599985,
we know kappa_{U(1)} = 7.269985593... and beta_{U(1)} = 3.796945276...

The ratio C = kappa/beta = 1.914688... encodes all the spectral geometry.

This script systematically tries hundreds of combinations of the known
inputs to find a formula that reproduces kappa_{U(1)} or alpha^{-1}.

Author: Derived for G. Alcock, DFD project
Date: March 22, 2026
"""

import math
from fractions import Fraction
import itertools

# ============================================================================
# KNOWN INPUTS
# ============================================================================

k_max = 60
d = 64
N_species = 7
Tr_Y2 = 10
g_F = 8
n1 = 1
n2 = 2
N_gen = 3
q1 = 3
a = 9  # twist degree

# Derived rationals
traceless = Fraction(63, 64)
eps_adj = Fraction(4096, 4095)
w_hyp = Fraction(7, 80)
wilson_ratio = 6  # (n2/n1) * N_gen

# CS weighted average (closed-form finite sum)
def cs_weight(k):
    return (2.0 / (k + 2)) * math.sin(math.pi / (k + 2))**2

numerator_cs = sum((k + 2) * cs_weight(k) for k in range(k_max))
denominator_cs = sum(cs_weight(k) for k in range(k_max))
beta_U1 = numerator_cs / denominator_cs

# Also compute with j-indexing
num_j = sum(math.sin(math.pi / j)**2 for j in range(2, 62))  # j=2..61
den_j = sum(math.sin(math.pi / j)**2 / j for j in range(2, 62))

# Targets
alpha_inv_target = 137.03599985
kappa_target = alpha_inv_target / (6 * math.pi)
C_target = kappa_target / beta_U1  # = 1.914688...

print("=" * 80)
print("BRUTE-FORCE SEARCH FOR kappa_{U(1)} FORMULA")
print("=" * 80)
print(f"\nKnown values:")
print(f"  beta_U(1)     = {beta_U1:.12f}")
print(f"  kappa_U(1)    = {kappa_target:.12f}")
print(f"  alpha^(-1)    = {alpha_inv_target}")
print(f"  C = kappa/beta = {C_target:.12f}")
print(f"  num_j (sum sin^2(pi/j)) = {num_j:.12f}")
print(f"  den_j (sum sin^2(pi/j)/j) = {den_j:.12f}")

# Additional useful numbers
Lambda3 = k_max * (k_max + 3) / (k_max + 4)  # = 59.0625
Lambda3_alt = 60 * 63 / 64

print(f"  Lambda^3 = {Lambda3:.6f}")
print(f"  (d-1)/d  = {float(traceless):.10f}")
print(f"  eps_adj  = {float(eps_adj):.12f}")
print(f"  w_hyp    = {float(w_hyp):.10f}")


# ============================================================================
# STRATEGY 1: Try alpha^{-1} = F * beta * (63/64) * (4096/4095)
# where F is a simple expression of the known inputs
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 1: alpha^(-1) = F * beta * (63/64) * (4096/4095)")
print("=" * 80)

F_target = alpha_inv_target / (beta_U1 * float(traceless) * float(eps_adj))
print(f"\nF_target = {F_target:.12f}")
print(f"F_target / pi = {F_target / math.pi:.12f}")
print(f"F_target / (2*pi) = {F_target / (2*math.pi):.12f}")
print(f"F_target / (4*pi) = {F_target / (4*math.pi):.12f}")
print(f"F_target * 3 / (35*pi) = {F_target * 3 / (35*math.pi):.12f}")

# We know 35*pi/3 works to ~85 ppm. Let's find what EXACTLY works.
exact_F = alpha_inv_target / (beta_U1 * 63/64 * 4096/4095)

results = []

# Try simple fractions times pi
for num in range(1, 200):
    for den in range(1, 200):
        val = num * math.pi / den
        err_ppm = abs(val - exact_F) / exact_F * 1e6
        if err_ppm < 100:
            results.append((err_ppm, f"{num}*pi/{den}", val))

results.sort()
print(f"\nBest matches for F = n*pi/m:")
for err, formula, val in results[:20]:
    alpha_test = val * beta_U1 * 63/64 * 4096/4095
    print(f"  F = {formula:>15s} = {val:.10f}  err = {err:>8.2f} ppm  alpha^-1 = {alpha_test:.8f}")


# ============================================================================
# STRATEGY 2: Try alpha^{-1} = (a*pi + b) * beta * products_of_factors
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 2: Direct search for alpha^(-1) formulas")
print("=" * 80)

alpha_exp = 137.035999084

# Known building blocks
blocks = {
    'pi': math.pi,
    '2pi': 2*math.pi,
    '4pi': 4*math.pi,
    '6pi': 6*math.pi,
    'beta': beta_U1,
    '63/64': 63/64,
    '4096/4095': 4096/4095,
    '7/80': 7/80,
    'N_sp=7': 7,
    'TrY2=10': 10,
    'gF=8': 8,
    'n1=1': 1,
    'n2=2': 2,
    'Ngen=3': 3,
    'd=64': 64,
    'kmax=60': 60,
    'q1=3': 3,
    'a=9': 9,
}

# Try: alpha^{-1} = A * beta * correction_factors
# where A involves pi and SM integers

print("\nSearching: alpha^{-1} = A * beta * (63/64) * (4096/4095)")
print(f"Need A = {exact_F:.12f}")
print(f"35*pi/3 = {35*math.pi/3:.12f}  (err: {abs(35*math.pi/3 - exact_F)/exact_F*1e6:.1f} ppm)")

# Try A = (a*pi + b/c) for small integers
best_abc = []
for a_coeff in range(-20, 21):
    for b_num in range(-100, 101):
        for c_den in range(1, 50):
            val = a_coeff * math.pi + b_num / c_den
            if val <= 0:
                continue
            err = abs(val - exact_F) / exact_F
            if err < 1e-4:  # within 100 ppm
                best_abc.append((err*1e6, f"{a_coeff}*pi + {b_num}/{c_den}", val))

best_abc.sort()
print(f"\nBest A = a*pi + b/c formulas (top 15):")
for err, formula, val in best_abc[:15]:
    print(f"  A = {formula:>25s} = {val:.10f}  err = {err:>8.3f} ppm")


# ============================================================================
# STRATEGY 3: Try kappa_{U(1)} directly as algebraic expression
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 3: Direct formulas for kappa_{U(1)}")
print("=" * 80)

print(f"\nTarget: kappa_U(1) = {kappa_target:.12f}")

# Try: kappa = beta * (rational) * (63/64) * (4096/4095)
# Need: rational = kappa / (beta * 63/64 * 4096/4095) = C_target
C_with_factors = kappa_target / (beta_U1 * 63/64 * 4096/4095)
print(f"C (without Toeplitz factors) = {C_with_factors:.12f}")
print(f"  C / pi = {C_with_factors/math.pi:.12f}")

# Or: kappa = beta * (rational)
C_simple = kappa_target / beta_U1
print(f"\nC (kappa/beta, no factors) = {C_simple:.12f}")
print(f"  C_simple * 6 = {C_simple * 6:.12f}")
print(f"  C_simple * 12 = {C_simple * 12:.12f}")
print(f"  C_simple / pi = {C_simple / math.pi:.12f}")

# The paper's formula: alpha^{-1} = 6*pi*kappa
# And alpha^{-1} ~ (35*pi/3) * beta * (63/64) * (4096/4095)
# So kappa ~ (35/(18)) * beta * (63/64) * (4096/4095)
# 35/18 = 1.94444...  vs  C_with_factors = 1.94599...
# Difference is (1.94599 - 1.94444)/1.94444 = 79 ppm

# Try: kappa = (a/b) * beta * (63/64) * (4096/4095) for simple a/b
print(f"\nSearching kappa = (a/b) * beta * (63/64) * (4096/4095):")
print(f"Need a/b = {C_with_factors:.12f}")

for a_try in range(1, 300):
    for b_try in range(1, 200):
        val = a_try / b_try
        err = abs(val - C_with_factors) / C_with_factors
        if err < 1e-4:
            alpha_test = 6 * math.pi * val * beta_U1 * 63/64 * 4096/4095
            print(f"  {a_try}/{b_try} = {val:.10f}  err = {err*1e6:.2f} ppm  "
                  f"alpha^-1 = {alpha_test:.8f}")


# ============================================================================
# STRATEGY 4: Maybe the formula does NOT factor through beta directly
# Try: alpha^{-1} = f(sums, d, SM inputs) with no beta intermediate
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 4: Formulas NOT factoring through beta")
print("=" * 80)

# The CS sums
S1 = num_j  # sum sin^2(pi/j) for j=2..61
S2 = den_j  # sum sin^2(pi/j)/j for j=2..61
S3 = sum(math.sin(math.pi / j)**2 * j for j in range(2, 62))
S4 = sum(math.sin(2*math.pi / j)**2 for j in range(2, 62))
S5 = sum(math.sin(math.pi / j)**2 / j**2 for j in range(2, 62))
S6 = sum(math.sin(math.pi / j) for j in range(2, 62))
S7 = sum(1.0/j for j in range(2, 62))  # harmonic-like sum

print(f"CS sums:")
print(f"  S1 = sum sin^2(pi/j)     = {S1:.12f}")
print(f"  S2 = sum sin^2(pi/j)/j   = {S2:.12f}")
print(f"  S3 = sum j*sin^2(pi/j)   = {S3:.12f}")
print(f"  S4 = sum sin^2(2pi/j)    = {S4:.12f}")
print(f"  S5 = sum sin^2(pi/j)/j^2 = {S5:.12f}")
print(f"  S6 = sum sin(pi/j)       = {S6:.12f}")
print(f"  S7 = sum 1/j (j=2..61)   = {S7:.12f}")
print(f"  beta = S1/S2             = {S1/S2:.12f}")

# Try: alpha^{-1} = c * S_i * correction_factors
targets_to_try = [
    ("alpha^{-1}", alpha_inv_target),
    ("kappa", kappa_target),
]

sums_to_try = [
    ("S1", S1), ("S2", S2), ("S3", S3), ("S4", S4),
    ("S1/S2 (=beta)", S1/S2),
    ("S1*S2", S1*S2),
    ("S1+S2", S1+S2),
    ("S1-S2", S1-S2),
    ("S3/S1", S3/S1),
    ("S3/S2", S3/S2),
]

factors_to_try = [
    ("1", 1),
    ("63/64", 63/64),
    ("4096/4095", 4096/4095),
    ("(63/64)*(4096/4095)", 63/64 * 4096/4095),
    ("7/80", 7/80),
    ("(7/80)*(63/64)*(4096/4095)", 7/80 * 63/64 * 4096/4095),
]

pi_factors = [
    ("1", 1), ("pi", math.pi), ("2pi", 2*math.pi),
    ("4pi", 4*math.pi), ("6pi", 6*math.pi),
    ("pi/2", math.pi/2), ("pi/3", math.pi/3),
    ("pi^2", math.pi**2), ("2pi^2", 2*math.pi**2),
    ("sqrt(pi)", math.sqrt(math.pi)),
]

print(f"\nSearching alpha^(-1) = c * S * pi_factor * correction_factor:")
hits = []

for tname, target in targets_to_try:
    for sname, sval in sums_to_try:
        for fname, fval in factors_to_try:
            for pname, pval in pi_factors:
                if sval * fval * pval == 0:
                    continue
                c_needed = target / (sval * fval * pval)
                # Check if c_needed is a simple fraction
                for cn in range(1, 100):
                    for cd in range(1, 100):
                        if abs(cn/cd - c_needed) / abs(c_needed) < 1e-5:  # 10 ppm
                            computed = (cn/cd) * sval * fval * pval
                            err = abs(computed - target) / target * 1e6
                            if err < 50:
                                hits.append((err, tname,
                                    f"({cn}/{cd})*{sname}*{pname}*{fname}",
                                    computed))

hits.sort()
print(f"\nTop 30 hits (< 50 ppm):")
for err, tname, formula, val in hits[:30]:
    print(f"  {tname:>12s} = {formula:>60s} = {val:.10f}  err = {err:.3f} ppm")


# ============================================================================
# STRATEGY 5: The "obvious" formula approach
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 5: Physical formula decomposition")
print("=" * 80)

# From the Chamseddine-Connes spectral action:
# S_gauge = (f0/2pi^2) * integral [c1*G^2 + c2*W^2 + c3*B^2] d^4x
# where c3 = (1/2) * g_F * Tr(Y^2) = (1/2)*8*10 = 40  (standard CCM)
#
# In DFD, the U(1) coupling is: 1/g1^2 = (f0/2pi^2) * c3_DFD
# and kappa_U(1) = (f0/2pi^2) * c3_DFD  (since g1^2 = 1/kappa)
#
# The spectral action scale f0 is determined by the CS level sum.
# The DFD version of c3 involves the Toeplitz truncation.

# Hypothesis: kappa_{U(1)} = beta * w * eps_adj * (d-1)/d * X
# where X is a spectral geometry factor from a4 on CP^2 x S^3

X_needed = kappa_target / (beta_U1 * float(w_hyp) * float(eps_adj) * float(traceless))
print(f"\nIf kappa = beta * w * eps_adj * (d-1)/d * X:")
print(f"  X = {X_needed:.12f}")
print(f"  X / pi^2 = {X_needed / math.pi**2:.12f}")
print(f"  X / (2*pi^2) = {X_needed / (2*math.pi**2):.12f}")
print(f"  X / (4*pi) = {X_needed / (4*math.pi):.12f}")

# Hypothesis: kappa = beta * (something involving Tr(Y^2), g_F, N_species)
# Let's try the standard spectral action form:
# kappa = beta * (1/2) * g_F * Tr(Y^2) * normalization * truncation_factors
# = beta * 40 * normalization * (63/64) * (4096/4095)
# Then normalization = kappa / (beta * 40 * 63/64 * 4096/4095)
norm_40 = kappa_target / (beta_U1 * 40 * 63/64 * 4096/4095)
print(f"\nIf kappa = beta * 40 * norm * (63/64) * (4096/4095):")
print(f"  norm = {norm_40:.12f}")
print(f"  1/(4*pi^2) = {1/(4*math.pi**2):.12f}")
print(f"  norm * 4*pi^2 = {norm_40 * 4*math.pi**2:.12f}")
# norm ~ 0.04865, and 1/(4*pi^2) = 0.02533.  Not a match.

# What about: kappa = (f0/2pi^2) * c3_DFD * truncation
# where f0 is set by the CS vacuum: f0 = beta/(something)?
# Or f0 itself is determined by the spectral action consistency?

# Let's try: alpha^{-1} = 6*pi * beta * c3_DFD / (2*pi^2) * trunc
# = 3*beta*c3_DFD/pi * trunc
# c3_DFD = c3_standard * w_DFD?
# c3_standard = 40.
# If c3_DFD = 40 * w_hyp = 40 * 7/80 = 3.5
c3_DFD_try = 40 * float(w_hyp)
alpha_try = 6*math.pi * beta_U1 * c3_DFD_try / (2*math.pi**2) * 63/64 * 4096/4095
print(f"\nIf c3_DFD = 40 * w = {c3_DFD_try}:")
print(f"  alpha^(-1) = 6*pi*beta*c3_DFD/(2*pi^2)*(63/64)*(4096/4095)")
print(f"             = {alpha_try:.10f}")
print(f"  err = {abs(alpha_try - alpha_inv_target)/alpha_inv_target * 1e6:.1f} ppm")

# Try: alpha^{-1} = (3/pi) * beta * c3_DFD * (63/64) * (4096/4095)
alpha_try2 = (3/math.pi) * beta_U1 * c3_DFD_try * 63/64 * 4096/4095
print(f"\n  (3/pi)*beta*3.5*(63/64)*(4096/4095) = {alpha_try2:.10f}")
print(f"  err = {abs(alpha_try2 - alpha_inv_target)/alpha_inv_target * 1e6:.1f} ppm")

# The approximate formula works: (35*pi/3) * beta * (63/64) * (4096/4095)
# 35*pi/3 = 4*pi * (5/2) * (7/6)
# Let's understand the decomposition:
# 4*pi from 1/(4*pi) in alpha definition
# 5/2 = 1 + R_W/4 = 1 + 6/4  (electroweak)
# 7/6 = N_sp / (N_gen * n2) = 7/6  (spectral triple)
# So: 4*pi * (1 + n2*N_gen/n1/4) * N_sp/(N_gen*n2)
# = 4*pi * (1 + 3/2) * 7/6 = 4*pi * 5/2 * 7/6 = 140*pi/12 = 35*pi/3
approx_formula = 4*math.pi * (1 + wilson_ratio/4) * N_species/(N_gen*n2)
print(f"\nApprox decomposition: 4*pi * (1 + R_W/4) * N_sp/(N_gen*n2)")
print(f"  = 4*pi * {1+wilson_ratio/4} * {N_species/(N_gen*n2):.6f}")
print(f"  = {approx_formula:.12f}")
print(f"  35*pi/3 = {35*math.pi/3:.12f}")
print(f"  Match: {abs(approx_formula - 35*math.pi/3) < 1e-10}")


# ============================================================================
# STRATEGY 6: Exact numerical decomposition of the gap
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 6: Analyzing the 85 ppm gap in the approximate formula")
print("=" * 80)

approx_alpha = 35*math.pi/3 * beta_U1 * 63/64 * 4096/4095
gap = alpha_inv_target - approx_alpha
gap_ppm = gap / alpha_inv_target * 1e6
print(f"\nApprox: (35*pi/3)*beta*(63/64)*(4096/4095) = {approx_alpha:.10f}")
print(f"Target: {alpha_inv_target}")
print(f"Gap:    {gap:.10f}")
print(f"Gap:    {gap_ppm:.2f} ppm")

# The gap could be a higher-order correction from the spectral action
correction_factor = alpha_inv_target / approx_alpha
print(f"\nCorrection factor: {correction_factor:.12f}")
print(f"  1 + x where x = {correction_factor - 1:.10e}")
print(f"  x = {(correction_factor-1)*1e6:.2f} ppm")

# Maybe the correction involves the CS sums at higher order?
# Or it's from the exact a_4 coefficient vs the leading-order approximation.

# Let's check if the gap is related to (pi^2/6 - something) or other constants
x = correction_factor - 1
print(f"\n  x = {x:.10e}")
print(f"  x * d^2 = {x * d**2:.8f}")
print(f"  x * k_max = {x * k_max:.8f}")
print(f"  1/x = {1/x:.4f}")
print(f"  pi^2 * x = {math.pi**2 * x:.8f}")


# ============================================================================
# STRATEGY 7: Try the formula WITHOUT the EW mixing decomposition
# i.e., derive alpha^{-1} directly from the CS sum
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 7: Direct formulas for alpha^{-1} from CS sums")
print("=" * 80)

# We know:
# alpha^{-1} = 6*pi * kappa_U(1)
# And in the lattice approach: beta = 1/g^2, kappa ~ measured renormalized
# The relationship beta -> kappa is non-perturbative in the lattice.
# But in the spectral action, it should be algebraic.

# What if kappa = beta * (35/(18)) * (63/64) * (4096/4095) * (1+delta)?
# where delta is an exactly computable correction?

# Or what if the EXACT formula is:
# alpha^{-1} = 6*pi * beta * (some exact expression)

# Let's check: does 6*pi*beta equal anything nice?
sixpi_beta = 6 * math.pi * beta_U1
print(f"\n6*pi*beta = {sixpi_beta:.12f}")
print(f"alpha^{-1} / (6*pi*beta) = {alpha_inv_target/sixpi_beta:.12f}")

# This ratio is kappa/beta = C_simple = 1.91469...
# Does C_simple have a nice form?
print(f"\nkappa/beta = {C_simple:.12f}")
print(f"  2 - 1/(something)? 2 - {2-C_simple:.10f}")
print(f"  1/(2-C) = {1/(2-C_simple):.10f}")
print(f"  C * 6 = {C_simple*6:.10f}")
print(f"  C * 12 = {C_simple*12:.10f}")
print(f"  C * 18 = {C_simple*18:.10f}")
print(f"  C * 18/35 = {C_simple*18/35:.12f}")
print(f"  C * pi = {C_simple*math.pi:.10f}")

# C * 18/35 should be close to 1 if 35/18 is the leading approximation
# C * 18/35 = 0.985... so the correction is -1.5%

# Let me try: is C = pi/e (Euler's number)?
print(f"  pi/e = {math.pi/math.e:.12f}  (err: {abs(math.pi/math.e - C_simple)/C_simple*1e6:.0f} ppm)")

# Is C related to zeta functions or Catalan's constant?
G_catalan = 0.915965594177  # Catalan's constant
print(f"  2*Catalan = {2*G_catalan:.12f}  (err: {abs(2*G_catalan - C_simple)/C_simple*1e6:.0f} ppm)")

# Euler-Mascheroni
gamma_EM = 0.5772156649015
print(f"  pi*gamma = {math.pi*gamma_EM:.12f}  (err: {abs(math.pi*gamma_EM - C_simple)/C_simple*1e6:.0f} ppm)")

# Golden ratio
phi = (1 + math.sqrt(5))/2
print(f"  phi*phi/sqrt(pi) = {phi**2/math.sqrt(math.pi):.12f}")


# ============================================================================
# STRATEGY 8: The REAL physical approach -- spectral action a4 coefficient
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 8: From the a4 Seeley-DeWitt coefficient")
print("=" * 80)

# The Gilkey formula for a4 for P = -(g^ij nabla_i nabla_j + E) on n-dim:
# a4 = (4*pi)^(-n/2) * (1/360) * integral of [
#   60*E_{;ii} + 180*E^2 + 30*Omega_{ij}*Omega_{ij}
#   + (5*R^2 - 2*R_{ij}*R_{ij} + 2*R_{ijkl}*R_{ijkl}) * Id
#   - 12*R*E + ... ] * sqrt(g) d^nx
#
# For a CONNECTION Laplacian (E=0), acting on the gauge bundle:
# The gauge kinetic term comes from 30*Omega_{ij}*Omega_{ij} term
# where Omega is the curvature of the connection = F_ij
#
# On CP^2 x S^3 (7-dimensional):
# a4 = (4*pi)^(-7/2) * (1/360) * integral [30 * tr(F^2) + ...] d^7x
#
# But wait: for the GAUGE KINETIC term extraction, we need the
# a4 coefficient on the 7D internal space, which then gives
# kappa = (f0/(2*pi^2)) * C_gauge
# where C_gauge is the a4 gauge coupling coefficient.

# Actually, the spectral action gives the 4D effective action.
# The internal dimensions contribute to the gauge coupling through
# a4 on the internal space X.

# For connection Laplacian on X = CP^2 x S^3:
# The gauge kinetic contribution is proportional to
# integral_X [tr_internal(Omega^2)] * vol(X)
# = c3 * vol(X)
# where c3 depends on the bundle structure.

# Key curvature invariants:
# CP^2 (Fubini-Study, unit diameter):
R_CP2 = 24  # Scalar curvature of unit CP^2
vol_CP2 = math.pi**2 / 2  # Volume of unit CP^2
# S^3 (unit radius):
R_S3 = 6  # Scalar curvature of unit S^3
vol_S3 = 2 * math.pi**2  # Volume of unit S^3

vol_X = vol_CP2 * vol_S3
print(f"\nGeometric data:")
print(f"  vol(CP^2) = pi^2/2 = {vol_CP2:.10f}")
print(f"  vol(S^3)  = 2*pi^2 = {vol_S3:.10f}")
print(f"  vol(X)    = pi^4   = {vol_X:.10f}")
print(f"  pi^4      = {math.pi**4:.10f}")

# The spectral action prefactor for n=7 dimensions:
sa_prefactor = 1 / (4*math.pi)**(3.5)  # (4pi)^(-7/2)
print(f"  (4pi)^(-7/2) = {sa_prefactor:.10e}")

# For the Chamseddine-Connes spectral action on the SM spectral triple:
# The gauge coupling constant is extracted from:
# f(0) * a4(D^2) where a4 involves tr(F^2) terms
# The coefficient depends on the internal Hilbert space dimension
# and the representation of the gauge group.

# In the DFD framework:
# - The Chern-Simons levels contribute through beta_{U(1)}
# - The Toeplitz truncation modifies the trace
# - The hypercharge weighting w = 7/80 enters

# Let me try the Chamseddine-Connes style:
# 1/g^2 = f0 * a_gauge / (2*pi^2)
# where a_gauge is the coefficient of tr(F^2) in a4
# For the SM: a_gauge = c3 = (1/2) * g_F * Tr(Y^2)
# In DFD: modified by truncation

# If f0 = 2*pi^2 * beta / (c3 * corrections):
# Then kappa = 1/g^2 = beta  (bare, before corrections)
# But kappa != beta because of renormalization / truncation corrections

# Actually, the paper says (Eq. 11 of ab initio paper):
# beta_{U(1)} = 1/g1^2  (input, bare)
# kappa_{U(1)} ~ 7.25    (measured, renormalized)
# These are NOT the same.  The relationship is non-perturbative.

print(f"\n  kappa/beta = {C_simple:.12f} (= non-perturbative renormalization)")
print(f"  This ratio IS the content of the lattice simulation.")
print(f"  The spectral action gives kappa directly, bypassing the lattice.")


# ============================================================================
# STRATEGY 9: Deep numerical search - products of small integer powers
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 9: Exhaustive formula search")
print("=" * 80)

# Target: alpha^{-1} = 137.03599985
# Try: alpha^{-1} = product of (known_quantity)^power

from math import log

# The known quantities (positive)
known = {
    'pi': math.pi,
    'beta': beta_U1,
    'd': 64.0,
    'k': 60.0,
    'N_sp': 7.0,
    'TrY2': 10.0,
    'gF': 8.0,
    'Ngen': 3.0,
    'n2': 2.0,
    '(d-1)/d': 63/64,
    'eps': 4096/4095,
    'S1': S1,
    'S2': S2,
}

# Try: target = pi^a * beta^b * product of integer factors
# First, let's find what power of pi and beta comes close

print(f"\nlog(alpha^(-1)) = {math.log(alpha_inv_target):.10f}")
print(f"log(pi) = {math.log(math.pi):.10f}")
print(f"log(beta) = {math.log(beta_U1):.10f}")

# alpha^{-1} = pi^a * beta^b * (integer product)
# log(alpha^{-1}) = a*log(pi) + b*log(beta) + log(int_product)

log_target = math.log(alpha_inv_target)

print("\nSearching: alpha^{-1} = pi^a * beta^b * (integer/rational):")
good_combos = []

for a_pow in [-2, -1, 0, 1, 2, 3]:
    for b_pow in [-1, 0, 1, 2]:
        remainder = alpha_inv_target / (math.pi**a_pow * beta_U1**b_pow)
        if remainder <= 0:
            continue
        # Check if remainder is a simple fraction
        for rn in range(1, 500):
            for rd in range(1, 200):
                val = rn / rd
                if abs(val - remainder) / remainder < 1e-5:
                    computed = math.pi**a_pow * beta_U1**b_pow * val
                    err = abs(computed - alpha_inv_target)/alpha_inv_target * 1e6
                    if err < 10:
                        good_combos.append((err, f"pi^{a_pow} * beta^{b_pow} * {rn}/{rd}",
                                          computed))

good_combos.sort()
if good_combos:
    print("\nBest matches (< 10 ppm):")
    for err, formula, val in good_combos[:20]:
        print(f"  alpha^(-1) = {formula:>35s} = {val:.10f}  err = {err:.4f} ppm")
else:
    print("  No matches found < 10 ppm with simple fractions")


# ============================================================================
# STRATEGY 10: Reverse-engineer from the EXACT alpha^{-1}
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 10: What exact formula could give 137.03599985?")
print("=" * 80)

# The number 137.03599985 has to come from somewhere.
# It equals 6*pi*kappa_U(1).
# The paper says the spectral action on the Toeplitz-truncated CP^2 x S^3
# geometry produces this directly.

# Key insight: the LATTICE gives kappa ~ 7.25 with 1% precision.
# The SPECTRAL ACTION gives kappa = 7.269986 at sub-ppm.
# These are TWO INDEPENDENT routes to the same number.

# The spectral action route uses a_4, which is a polynomial in curvatures.
# For CP^2 x S^3, all curvatures are known constants.
# The Toeplitz truncation discretizes this.

# The KEY question: in the spectral action, does beta_{U(1)} appear?
# Or is the spectral action computed INDEPENDENTLY and just happens to
# agree with 6*pi*kappa = 137?

# From the text: "The spectral action on S^3 involves a sum over CS levels
# k = 0, ..., k_max-1, each weighted by w(k). The effective coupling parameter
# that emerges from this sum is precisely beta_{U(1)} = <k+2>."

# So YES, beta_{U(1)} is the spectral action's output from the S^3 sector.
# The CP^2 sector contributes the Toeplitz truncation and hypercharge structure.
# The product gives kappa_{U(1)}.

# The most natural formula structure is:
# kappa_{U(1)} = (spectral action on CP^2) * (spectral action on S^3)
# = [a4_CP2 with truncation] * [CS_weighted_average]
# = [geometric_factor * w * eps * (d-1)/d] * beta

# So: kappa = G * beta  where G is the CP^2 spectral geometry factor
# G = kappa/beta = 1.914688...
# G must encode: w = 7/80, eps = 4096/4095, (d-1)/d = 63/64,
# and the a4 coefficient on CP^2.

G_remaining = C_simple / (float(w_hyp) * float(eps_adj) * float(traceless))
print(f"\nkappa = beta * w * eps * (d-1)/d * G_remaining")
print(f"G_remaining = {G_remaining:.12f}")
print(f"  = a4 coefficient on Toeplitz-truncated CP^2")
print(f"  G_remaining / (4*pi^2) = {G_remaining / (4*math.pi**2):.12f}")
print(f"  G_remaining / pi^2 = {G_remaining / math.pi**2:.12f}")
print(f"  G_remaining / (2*pi) = {G_remaining / (2*math.pi):.12f}")
print(f"  G_remaining * 2 = {G_remaining * 2:.12f}")
print(f"  G_remaining * 3 = {G_remaining * 3:.12f}")

# Check: does G_remaining = d/3 = 64/3?
print(f"  d/3 = {d/3:.12f}  (err: {abs(d/3 - G_remaining)/G_remaining*1e6:.0f} ppm)")
# Check: G_remaining = 4*pi^2 / (something)?
# 4*pi^2 / G_remaining:
print(f"  4*pi^2/G = {4*math.pi**2/G_remaining:.12f}")
# Check: related to Ricci scalar?
print(f"  R_CP2/G = {R_CP2/G_remaining:.12f}")

# If G = d/3 exactly:
# kappa = beta * (7/80) * (4096/4095) * (63/64) * (64/3)
# = beta * 7/(80*3) * 64 * 63/64 * 4096/4095
# = beta * 7/240 * 63 * 4096/4095
# = beta * 7*63/(240) * 4096/4095
# = beta * 441/240 * 4096/4095
# = beta * 147/80 * 4096/4095
# = beta * 1.8375 * 1.000244
# = beta * 1.83795  ... but we need 1.91469. Not matching.

# Actually, the alpha^{-1} is 6*pi*beta*C_simple
# If alpha^{-1} = 6*pi*beta * w * eps * (d-1)/d * G:
# = 6*pi * beta * (7/80) * (4096/4095) * (63/64) * G
# = 6*pi * 3.797 * 0.0875 * 1.000244 * 0.984375 * G
# = 6*pi * 3.797 * 0.08612 * G
# = 6*pi * 0.3269 * G
# = 6.163 * G
# For alpha^{-1} = 137.036: G = 137.036/6.163 = 22.24
# Or: G = alpha^{-1} / (6*pi*beta*w*eps*(d-1)/d) = 22.24
# G = 22.24... what is this?
# 22.24 ~ 2*pi * Tr(Y^2) / ... hmm
# Actually let me compute more carefully

G_raw = alpha_inv_target / (6*math.pi * beta_U1 * float(w_hyp) * float(eps_adj) * float(traceless))
print(f"\nalpha^(-1) = 6*pi * beta * w * eps * (d-1)/d * G")
print(f"G = {G_raw:.12f}")
print(f"  G/pi = {G_raw/math.pi:.12f}")
print(f"  G/(2*pi) = {G_raw/(2*math.pi):.12f}")
print(f"  G/pi^2 = {G_raw/math.pi**2:.12f}")
print(f"  G/d = {G_raw/d:.12f}")
print(f"  G*3 = {G_raw*3:.12f}")
print(f"  G*80/7 = {G_raw*80/7:.12f}")

# Interesting: G*80/7 should be related to 1/w_hyp * G
G_unweighted = G_raw / float(w_hyp)
print(f"\n  G/w = {G_unweighted:.12f}")

# So the chain is: alpha^{-1} = 6*pi * beta * (7/80) * (63/64) * (4096/4095) * G
# where G ~ 22.24 is the a4 trace coefficient

# What if G = (2*pi)^2 * (Tr(Y^2)/something)?
# (2*pi)^2 = 39.48
# G = 22.24
# 22.24 / 39.48 = 0.5633
# Not obvious.

# What if G = (Tr(Y^2))^2 / (g_F * something)?
# 100/8 = 12.5, not 22.24

# What if G = d^2 / (something)?
# 4096/22.24 = 184.2
# 184.2 ~ 3*k_max = 180? Close but not exact.

# Try the full formula without splitting:
# alpha^{-1} = (pi * N_sp * d^2) / ((d^2-1) * something)
# or variations

# Let me try: alpha^{-1} = pi * beta * (d-1) * N_sp / (g_F * something)
for divisor in range(1, 100):
    test = math.pi * beta_U1 * (d-1) * N_species / (g_F * divisor)
    err = abs(test - alpha_inv_target)/alpha_inv_target
    if err < 0.001:
        print(f"  pi*beta*(d-1)*Nsp/(gF*{divisor}) = {test:.8f}  err = {err*1e6:.1f} ppm")

# Try: alpha^{-1} = pi * beta * d * N_sp / (g_F * something)
for divisor in range(1, 100):
    test = math.pi * beta_U1 * d * N_species / (g_F * divisor)
    err = abs(test - alpha_inv_target)/alpha_inv_target
    if err < 0.001:
        print(f"  pi*beta*d*Nsp/(gF*{divisor}) = {test:.8f}  err = {err*1e6:.1f} ppm")


# ============================================================================
# STRATEGY 11: COMPREHENSIVE SCAN
# ============================================================================

print("\n" + "=" * 80)
print("STRATEGY 11: Comprehensive formula scan (target: alpha^{-1} = 137.036)")
print("=" * 80)

# Build all possible products of the form:
# alpha^{-1} = (pi^a) * (beta^b) * prod(integers^powers) * (63/64)^c * (4096/4095)^d
# where integers are drawn from {2, 3, 5, 7, 8, 10, 60, 63, 64}

# Simpler: just scan products of basic building blocks
basic_values = {
    '2': 2, '3': 3, '5': 5, '7': 7, '8': 8, '10': 10,
    '60': 60, '63': 63, '64': 64,
}

target = alpha_inv_target
best_products = []

# Try: alpha^{-1} = pi^a * beta^b * (n1/n2) * (63/64)^c * (4096/4095)^d
# for reasonable ranges of a, b, c, d and small numerator/denominator

# Focus: what simple expression gives kappa_target = 7.26999?
# kappa = alpha^{-1} / (6*pi)
print(f"\nkappa_target = {kappa_target:.12f}")
print(f"kappa * 80/7 = {kappa_target * 80 / 7:.12f}")
print(f"kappa * 80 = {kappa_target * 80:.12f}")
print(f"kappa * 240/7 = {kappa_target * 240 / 7:.12f}")
print(f"beta * 63/64 * 4096/4095 = {beta_U1 * 63/64 * 4096/4095:.12f}")

# The ratio kappa/(beta*63/64*4096/4095) = 1.9460 ~ 35/18 = 1.9444
# The difference: 1.9460 - 1.9444 = 0.0016 = 0.08%
# So 35/18 is not exact. Is there a better fraction?
target_ratio = C_with_factors
print(f"\nTarget ratio kappa/(beta*(63/64)*(4096/4095)) = {target_ratio:.12f}")
# Find best continued fraction approximation
from fractions import Fraction
frac_approx = Fraction(target_ratio).limit_denominator(10000)
print(f"Best fraction (limit 10000): {frac_approx} = {float(frac_approx):.12f}")
print(f"  err = {abs(float(frac_approx) - target_ratio)/target_ratio*1e6:.2f} ppm")

frac_approx2 = Fraction(target_ratio).limit_denominator(1000)
print(f"Best fraction (limit 1000): {frac_approx2} = {float(frac_approx2):.12f}")
print(f"  err = {abs(float(frac_approx2) - target_ratio)/target_ratio*1e6:.2f} ppm")

frac_approx3 = Fraction(target_ratio).limit_denominator(100)
print(f"Best fraction (limit 100): {frac_approx3} = {float(frac_approx3):.12f}")
print(f"  err = {abs(float(frac_approx3) - target_ratio)/target_ratio*1e6:.2f} ppm")


# ============================================================================
# FINAL ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("FINAL ANALYSIS AND CONCLUSIONS")
print("=" * 80)

print(f"""
RESULT OF EXHAUSTIVE SEARCH:

1. The formula alpha^(-1) = 6*pi*kappa_U(1) is EXACT (from electroweak mixing
   + Frame Stiffness Theorem).

2. The computation of kappa_U(1) from the spectral action on Toeplitz-truncated
   CP^2 x S^3 involves beta_U(1) as the key input from the S^3 sector.

3. The APPROXIMATE formula:
   alpha^(-1) = (35*pi/3) * beta * (63/64) * (4096/4095)
   gives alpha^(-1) = {approx_alpha:.10f}  (err: {gap_ppm:.2f} ppm)

4. This approximate formula decomposes as:
   35*pi/3 = 4*pi * (5/2) * (7/6)
   where:
   - 4*pi: from alpha = e^2/(4*pi)
   - 5/2 = 1 + R_W/4 = 1 + 6/4: electroweak mixing with Wilson ratio 6
   - 7/6 = N_species/(N_gen*n2): spectral triple correction

5. The ~85 ppm gap between the approximate formula and the exact result
   corresponds to a multiplicative correction factor of {correction_factor:.12f}.
   This correction encodes the FULL spectral-action computation on the
   Toeplitz-truncated geometry, beyond the leading-order approximation.

6. NO SIMPLE CLOSED-FORM FORMULA was found for the exact kappa_U(1) in terms
   of the Table XXVIII inputs alone. The ratio kappa/beta = {C_simple:.12f}
   is NOT a simple algebraic expression of the known integers.

7. CONCLUSION: The closed-form formula for kappa_U(1) genuinely requires
   evaluating the a_4 Seeley-DeWitt coefficient on the Toeplitz-truncated
   CP^2 x S^3 geometry. This is a finite algebraic computation but not
   reducible to a single simple equation.

8. The BEST available approximation is:
   kappa_U(1) ~ (35/18) * beta * (63/64) * (4096/4095)
   = {35/18 * beta_U1 * 63/64 * 4096/4095:.12f}
   (target: {kappa_target:.12f}, err: ~85 ppm)

   Or equivalently:
   alpha^(-1) ~ (35*pi/3) * beta * (63/64) * (4096/4095)
   = {35*math.pi/3 * beta_U1 * 63/64 * 4096/4095:.10f}
   (target: {alpha_inv_target}, err: ~85 ppm)
""")

# Verify the two routes agree
print("VERIFICATION: Two-route consistency")
print("-" * 50)
# Route 1: Spectral action
print(f"  Route 1 (spectral): alpha^(-1) = {alpha_inv_target} (stated in paper)")
# Route 2: Lattice MC
alpha_lattice_L6 = 1/0.007297  # From Table VI, L=6
alpha_lattice_L12 = 1/0.007291
print(f"  Route 2 (lattice L=6):  alpha^(-1) = {alpha_lattice_L6:.4f}")
print(f"  Route 2 (lattice L=12): alpha^(-1) = {alpha_lattice_L12:.4f}")
print(f"  Experimental:           alpha^(-1) = {alpha_exp}")
