#!/usr/bin/env python3
"""
Compute a_4(CP^2 x S^3) via the Seeley-DeWitt convolution formula.

For a product manifold X = M_1 x M_2:
    a_n(X) = sum_{p+q=n} a_p(M_1) * a_q(M_2)

where a_p are the INTEGRATED heat kernel coefficients for the scalar
Laplacian (no endomorphism, E=0).

Standard heat kernel expansion (Vassilevich, Phys. Rep. 388, 279 (2003)):
    Tr exp(-t D) ~ sum_k t^{(2k-d)/2} a_{2k}

Integrated coefficients for the scalar Laplacian on a closed manifold
without boundary (Gilkey; Vassilevich eq. 4.1-4.3):

    a_0 = (4 pi)^{-d/2} * int_M dV

    a_2 = (4 pi)^{-d/2} * (1/6) * int_M R dV

    a_4 = (4 pi)^{-d/2} * (1/360) * int_M (5 R^2 - 2 R_{ab} R^{ab}
           + 2 R_{abcd} R^{abcd}) dV

(For scalar Laplacian with E=0 and Omega=0.)

References:
    [1] D.V. Vassilevich, "Heat kernel expansion: user's manual",
        Phys. Rep. 388, 279 (2003), hep-th/0306138
    [2] P.B. Gilkey, "Invariance Theory, the Heat Equation, and the
        Atiyah-Singer Index Theorem" (1984, 1995)
    [3] A.H. Chamseddine, A. Connes, "The Spectral Action Principle",
        Commun. Math. Phys. 186, 731 (1997), hep-th/9606001
"""

import numpy as np
from fractions import Fraction

# =============================================================================
# SECTION 1: GEOMETRIC DATA FOR CP^2 (Fubini-Study metric)
# =============================================================================
# CP^2 is a Kahler-Einstein manifold of real dimension d = 4.
#
# Fubini-Study metric normalization (standard Riemannian geometry convention):
#   Holomorphic sectional curvature H = 4 (sectional curvatures in [1,4]).
#
# Riemann tensor for a complex space form with hol. sect. curv. H:
#   R_{abcd} = (H/4)(g_{ac}g_{bd} - g_{ad}g_{bc}
#              + J_{ac}J_{bd} - J_{ad}J_{bc} + 2J_{ab}J_{cd})
#
# For H = 4:
#   Ric_{ab} = 2(n+1) g_{ab} = 6 g_{ab}     (n = complex dim = 2)
#   R = 4n(n+1) = 24
#   R_{ab}R^{ab} = 6^2 * 4 = 144
#   R_{abcd}R^{abcd} = 192                    (verified numerically)
#
# Volume:  Vol(CP^2) = pi^2/2
# Topology: chi = 3, sigma = 1
#
# Gauss-Bonnet verification (d=4, Einstein with E_ab = 0):
#   chi = (R_{abcd}R^{abcd}) * Vol / (32 pi^2)
#       = 192 * (pi^2/2) / (32 pi^2) = 192/64 = 3  [CHECK]

d_CP2 = 4
R_CP2 = 24
RicSq_CP2 = 144
RiemSq_CP2 = 192
Vol_CP2 = np.pi**2 / 2

print("=" * 70)
print("GEOMETRIC DATA")
print("=" * 70)

print(f"\nCP^2 (Fubini-Study, H=4, real dim {d_CP2}):")
print(f"  R             = {R_CP2}")
print(f"  R_ab R^ab     = {RicSq_CP2}")
print(f"  R_abcd R^abcd = {RiemSq_CP2}")
print(f"  Vol           = pi^2/2 = {Vol_CP2:.10f}")

# Gauss-Bonnet check
chi_CP2 = RiemSq_CP2 * Vol_CP2 / (32 * np.pi**2)
print(f"  chi (GB)      = {chi_CP2:.1f} (topological value = 3)")

# =============================================================================
# SECTION 2: GEOMETRIC DATA FOR S^3 (round metric, radius r)
# =============================================================================
# For S^d of radius r (constant sectional curvature K = 1/r^2):
#   R_{abcd} = K (g_{ac}g_{bd} - g_{ad}g_{bc})
#   Ric_{ab} = (d-1)K g_{ab}
#   R = d(d-1)K = d(d-1)/r^2
#   R_{ab}R^{ab} = d(d-1)^2 K^2 = d(d-1)^2/r^4
#   R_{abcd}R^{abcd} = 2d(d-1)K^2 = 2d(d-1)/r^4
#   Vol(S^d) = 2 pi^{(d+1)/2} r^d / Gamma((d+1)/2)
#
# For S^3, d=3, r=1:
#   R = 6,  Ric^2 = 12,  Riem^2 = 12,  Vol = 2 pi^2

d_S3 = 3

def S3_invariants(r):
    """Compute geometric invariants for S^3 of radius r."""
    R = 6.0 / r**2
    RicSq = 12.0 / r**4
    RiemSq = 12.0 / r**4
    Vol = 2 * np.pi**2 * r**3
    return R, RicSq, RiemSq, Vol

r_S3 = 1.0
R_S3, RicSq_S3, RiemSq_S3, Vol_S3 = S3_invariants(r_S3)

print(f"\nS^3 (round, radius r = {r_S3}, dim {d_S3}):")
print(f"  R             = {R_S3}")
print(f"  R_ab R^ab     = {RicSq_S3}")
print(f"  R_abcd R^abcd = {RiemSq_S3}")
print(f"  Vol           = 2 pi^2 = {Vol_S3:.10f}")


# =============================================================================
# SECTION 3: HEAT KERNEL COEFFICIENTS
# =============================================================================

def heat_kernel_coefficients(d, R, RicSq, RiemSq, Vol):
    """
    Compute integrated Seeley-DeWitt coefficients a_0, a_2, a_4
    for the scalar Laplacian on a d-dimensional closed manifold
    with constant curvature invariants.

    Returns both 'tilde' coefficients (without (4pi)^{-d/2} prefactor)
    and full coefficients. The tilde coefficients are the ones that
    convolve multiplicatively for product manifolds.
    """
    prefactor = (4 * np.pi) ** (-d / 2.0)

    # Tilde (geometric) coefficients
    tA0 = Vol
    tA2 = (1.0/6.0) * R * Vol
    Q4 = 5 * R**2 - 2 * RicSq + 2 * RiemSq
    tA4 = (1.0/360.0) * Q4 * Vol

    # Full coefficients
    a0 = prefactor * tA0
    a2 = prefactor * tA2
    a4 = prefactor * tA4

    return (tA0, tA2, tA4), (a0, a2, a4), Q4


# CP^2
(tA0_CP2, tA2_CP2, tA4_CP2), (a0_CP2, a2_CP2, a4_CP2), Q4_CP2 = \
    heat_kernel_coefficients(d_CP2, R_CP2, RicSq_CP2, RiemSq_CP2, Vol_CP2)

# S^3
(tA0_S3, tA2_S3, tA4_S3), (a0_S3, a2_S3, a4_S3), Q4_S3 = \
    heat_kernel_coefficients(d_S3, R_S3, RicSq_S3, RiemSq_S3, Vol_S3)

print("\n" + "=" * 70)
print("HEAT KERNEL COEFFICIENTS (scalar Laplacian)")
print("=" * 70)

print(f"\nCP^2:")
print(f"  Q_4 = 5({R_CP2})^2 - 2({RicSq_CP2}) + 2({RiemSq_CP2})")
print(f"      = {5*R_CP2**2} - {2*RicSq_CP2} + {2*RiemSq_CP2} = {Q4_CP2}")
print(f"  tA_0 = Vol = {tA0_CP2:.10f}")
print(f"  tA_2 = R*Vol/6 = {tA2_CP2:.10f}")
print(f"  tA_4 = Q_4*Vol/360 = {tA4_CP2:.10f}")
print(f"  a_0  = (4pi)^{{-2}} * tA_0 = {a0_CP2:.10e}")
print(f"  a_2  = (4pi)^{{-2}} * tA_2 = {a2_CP2:.10e}")
print(f"  a_4  = (4pi)^{{-2}} * tA_4 = {a4_CP2:.10e}")

print(f"\nS^3:")
print(f"  Q_4 = 5({R_S3})^2 - 2({RicSq_S3}) + 2({RiemSq_S3})")
print(f"      = {5*R_S3**2} - {2*RicSq_S3} + {2*RiemSq_S3} = {Q4_S3}")
print(f"  tA_0 = Vol = {tA0_S3:.10f}")
print(f"  tA_2 = R*Vol/6 = {tA2_S3:.10f}")
print(f"  tA_4 = Q_4*Vol/360 = {tA4_S3:.10f}")
print(f"  a_0  = (4pi)^{{-3/2}} * tA_0 = {a0_S3:.10e}")
print(f"  a_2  = (4pi)^{{-3/2}} * tA_2 = {a2_S3:.10e}")
print(f"  a_4  = (4pi)^{{-3/2}} * tA_4 = {a4_S3:.10e}")


# =============================================================================
# SECTION 4: EXACT SYMBOLIC COMPUTATION
# =============================================================================
print("\n" + "=" * 70)
print("EXACT SYMBOLIC EXPRESSIONS")
print("=" * 70)

# CP^2 (R=24, Ric^2=144, Riem^2=192, Vol=pi^2/2):
#   Q_4 = 5(576) - 2(144) + 2(192) = 2880 - 288 + 384 = 2976
#   tA_0 = pi^2/2
#   tA_2 = (24/6)(pi^2/2) = 2 pi^2
#   tA_4 = (2976/360)(pi^2/2) = 2976/720 * pi^2 = 62/15 * pi^2

Q4_CP2_int = 5 * 24**2 - 2 * 144 + 2 * 192
frac_Q4_CP2 = Fraction(Q4_CP2_int, 360)
frac_tA4_CP2 = Fraction(Q4_CP2_int, 720)  # Q4/360 * Vol = Q4/360 * pi^2/2

print(f"\nCP^2:")
print(f"  Q_4 = 5(576) - 2(144) + 2(192) = {Q4_CP2_int}")
print(f"  tA_0 = pi^2/2")
print(f"  tA_2 = 2 pi^2")
print(f"  tA_4 = ({Q4_CP2_int}/720) pi^2 = {frac_tA4_CP2} pi^2")
print(f"       = {float(frac_tA4_CP2):.10f} pi^2")

# S^3 (R=6, Ric^2=12, Riem^2=12, Vol=2pi^2):
#   Q_4 = 5(36) - 2(12) + 2(12) = 180
#   tA_0 = 2 pi^2
#   tA_2 = (6/6)(2 pi^2) = 2 pi^2
#   tA_4 = (180/360)(2 pi^2) = pi^2

Q4_S3_int = 5 * 36 - 2 * 12 + 2 * 12
frac_tA4_S3 = Fraction(Q4_S3_int * 2, 360)  # Q4/360 * 2 pi^2

print(f"\nS^3:")
print(f"  Q_4 = 5(36) - 2(12) + 2(12) = {Q4_S3_int}")
print(f"  tA_0 = 2 pi^2")
print(f"  tA_2 = 2 pi^2")
print(f"  tA_4 = ({Q4_S3_int}/180) pi^2 = {frac_tA4_S3} pi^2")


# =============================================================================
# SECTION 5: CONVOLUTION FOR THE PRODUCT MANIFOLD CP^2 x S^3
# =============================================================================
# tA_4(X) = tA_4(CP2)*tA_0(S3) + tA_2(CP2)*tA_2(S3) + tA_0(CP2)*tA_4(S3)
# All in units of pi^{2+2} = pi^4:

# Term 1: (62/15 pi^2) * (2 pi^2) = 124/15 pi^4
frac_term1 = frac_tA4_CP2 * 2
# Term 2: (2 pi^2) * (2 pi^2) = 4 pi^4
frac_term2 = Fraction(4)
# Term 3: (pi^2/2) * (1 pi^2) = pi^4/2
frac_term3 = Fraction(1, 2) * frac_tA4_S3

frac_total = frac_term1 + frac_term2 + frac_term3

d_product = d_CP2 + d_S3  # = 7
prefactor_product = (4 * np.pi) ** (-d_product / 2.0)

print("\n" + "=" * 70)
print("CONVOLUTION: a_4(CP^2 x S^3)")
print("=" * 70)
print(f"\nProduct dimension: d = {d_CP2} + {d_S3} = {d_product}")
print(f"\nConvolution (coefficients of pi^4):")
print(f"  tA_4(CP^2) * tA_0(S^3) = {frac_tA4_CP2} * 2 = {frac_term1} pi^4")
print(f"  tA_2(CP^2) * tA_2(S^3) = 2 * 2 = {frac_term2} pi^4")
print(f"  tA_0(CP^2) * tA_4(S^3) = (1/2) * {frac_tA4_S3} = {frac_term3} pi^4")
print(f"\n  tA_4(CP^2 x S^3) = {frac_term1} + {frac_term2} + {frac_term3}")
print(f"                    = {frac_total} pi^4")
print(f"                    = {float(frac_total):.10f} pi^4")

# Numerical verification
tA4_product_num = tA4_CP2 * tA0_S3 + tA2_CP2 * tA2_S3 + tA0_CP2 * tA4_S3
print(f"  Numerical check:  {tA4_product_num / np.pi**4:.10f} pi^4")

# Full a_4 with prefactor:
# a_4(X) = (4pi)^{-7/2} * tA_4
# = (4pi)^{-7/2} * (frac_total) * pi^4
# = frac_total * pi^4 / (4^{7/2} * pi^{7/2})
# = frac_total * pi^{1/2} / 4^{7/2}
# = frac_total * sqrt(pi) / 128

frac_a4_coeff = frac_total / 128   # coefficient of sqrt(pi)
a4_product = float(frac_total) * np.pi**4 * prefactor_product

print(f"\n  a_4(CP^2 x S^3) = (4pi)^{{-7/2}} * {frac_total} * pi^4")
print(f"                   = ({frac_total}/128) * sqrt(pi)")
print(f"                   = {frac_a4_coeff} * sqrt(pi)")
print(f"                   = {float(frac_a4_coeff) * np.sqrt(np.pi):.10e}")
print(f"  Numerical check: {a4_product:.10e}")
print(f"  Match: {np.isclose(float(frac_a4_coeff)*np.sqrt(np.pi), a4_product)}")


# =============================================================================
# SECTION 6: GAUGE COUPLING EXTRACTION
# =============================================================================
# In the Chamseddine-Connes spectral action framework:
#   S_B = Tr f(D^2/Lambda^2) ~ f_4 Lambda^d a_0 + f_2 Lambda^{d-2} a_2
#         + f_0 a_4 + ...
#
# For a Dirac operator coupled to a U(1) gauge field A, the a_4 coefficient
# contains a term proportional to tr(F^2):
#   a_4^{gauge} = -(4pi)^{-d/2} * (1/12) * int tr(F_{mu nu} F^{mu nu}) dV
#
# The gauge kinetic term in the action is:
#   S_gauge = -f_0 * (4pi)^{-d/2} * (Vol / 12) * tr(F^2)
#
# This gives the identification:
#   1/g^2 = f_0 * (4pi)^{-d/2} * Vol / (12)
# where Vol = Vol(CP^2 x S^3) = Vol(CP^2) * Vol(S^3)

Vol_product = Vol_CP2 * Vol_S3
# = (pi^2/2)(2pi^2) = pi^4

kappa_U1 = prefactor_product * Vol_product / 12.0

# Exact: kappa = (4pi)^{-7/2} * pi^4 / 12
#       = pi^4 / (12 * 4^{7/2} * pi^{7/2})
#       = pi^{1/2} / (12 * 128)
#       = sqrt(pi) / 1536

print("\n" + "=" * 70)
print("GAUGE COUPLING EXTRACTION (Spectral Action)")
print("=" * 70)
print(f"\nVol(CP^2 x S^3) = (pi^2/2)(2 pi^2) = pi^4 = {Vol_product:.10f}")
print(f"\nGauge coefficient (coefficient of -tr(F^2) in a_4):")
print(f"  kappa_{{U(1)}} = (4pi)^{{-7/2}} * pi^4 / 12")
print(f"               = sqrt(pi) / 1536")
print(f"               = {kappa_U1:.10e}")
print(f"  Exact check:   {np.sqrt(np.pi)/1536:.10e}")

print(f"\nFor f_0 = 1:")
print(f"  1/g^2_{{U(1)}} = {kappa_U1:.10e}")
print(f"  g^2_{{U(1)}}   = {1.0/kappa_U1:.6f}")
print(f"  g_{{U(1)}}     = {np.sqrt(1.0/kappa_U1):.6f}")
print(f"  alpha_{{U(1)}} = g^2/(4pi) = {1.0/(kappa_U1 * 4 * np.pi):.6f}")

# Relation to alpha = 1/137.036:
alpha_em = 1.0 / 137.036
# At GUT scale, alpha_1(GUT) ~ 1/60 (with SM hypercharge normalization)
alpha_gut = 1.0 / 60.0
print(f"\n  For comparison:")
print(f"    alpha_em = 1/137.036 = {alpha_em:.6e}")
print(f"    alpha_1(GUT) ~ 1/60 = {alpha_gut:.6e}")
print(f"    To match alpha_1(GUT), need f_0 = {alpha_gut * 4 * np.pi / (1.0/kappa_U1):.6e}")
f0_needed = 1.0 / (kappa_U1 * 4 * np.pi * 60)
print(f"    i.e., f_0 = {f0_needed:.6f}")


# =============================================================================
# SECTION 7: PARAMETRIC DEPENDENCE ON S^3 RADIUS
# =============================================================================
print("\n" + "=" * 70)
print("PARAMETRIC DEPENDENCE ON S^3 RADIUS r")
print("=" * 70)

print(f"\n{'r':>8s} {'tA4(X)/pi^4':>14s} {'a4(X)':>14s} {'kappa':>14s} {'1/alpha':>10s}")
print("-" * 66)

for r in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    R_s, RicSq_s, RiemSq_s, Vol_s = S3_invariants(r)
    (tA0_s, tA2_s, tA4_s), _, _ = heat_kernel_coefficients(
        d_S3, R_s, RicSq_s, RiemSq_s, Vol_s)

    tA4_prod = tA4_CP2 * tA0_s + tA2_CP2 * tA2_s + tA0_CP2 * tA4_s
    a4_prod = prefactor_product * tA4_prod

    Vol_prod = Vol_CP2 * Vol_s
    kappa = prefactor_product * Vol_prod / 12.0
    inv_alpha = kappa * 4 * np.pi

    print(f"{r:8.2f} {tA4_prod/np.pi**4:14.6f} {a4_prod:14.6e} {kappa:14.6e} {1.0/inv_alpha:10.4f}")

# Find r that gives alpha^{-1} = 137.036
from scipy.optimize import brentq

def alpha_inv_minus_target(r, target):
    _, _, _, Vol_s = S3_invariants(r)
    Vol_prod = Vol_CP2 * Vol_s
    kappa = prefactor_product * Vol_prod / 12.0
    return kappa * 4 * np.pi - 1.0/target

try:
    r_alpha_em = brentq(alpha_inv_minus_target, 0.01, 100, args=(137.036,))
    print(f"\n  r(S^3) for alpha^{{-1}} = 137.036:  r = {r_alpha_em:.6f}")
except:
    # If scipy not available, compute analytically
    # kappa * 4pi = 1/137.036
    # (4pi)^{-7/2} * pi^2/2 * 2pi^2 r^3 / 12 * 4pi = 1/137.036
    # (4pi)^{-5/2} * pi^4 r^3 / 12 = 1/137.036  ... nope, just skip
    pass

# Analytical: kappa(r) = (4pi)^{-7/2} * (pi^2/2)(2pi^2 r^3) / 12
#            = (4pi)^{-7/2} * pi^4 r^3 / 12
# kappa(1) * r^3 = kappa(r)
# alpha^{-1} = kappa(r) * 4pi = kappa(1) * r^3 * 4pi
# For alpha^{-1} = 137.036:
# r^3 = 137.036 / (kappa_U1 * 4 * np.pi)
# r^3 = 137.036 / (sqrt(pi)/1536 * 4pi)
r_cubed_target = 137.036 / (kappa_U1 * 4 * np.pi)
r_target = r_cubed_target**(1.0/3.0)
print(f"\n  Analytical: r^3 = {r_cubed_target:.6f}")
print(f"              r   = {r_target:.6f}")
print(f"  Verification: alpha^{{-1}} = {kappa_U1 * r_target**3 * 4 * np.pi:.6f}")


# =============================================================================
# SECTION 8: DIRECT INTEGRATION VERIFICATION
# =============================================================================
# For product manifolds, the curvature of X = M_1 x M_2 satisfies:
#   R_X = R_1 + R_2     (scalar curvature is additive)
#   |Ric_X|^2 = |Ric_1|^2 + |Ric_2|^2   (Ricci is block-diagonal)
#   |Riem_X|^2 = |Riem_1|^2 + |Riem_2|^2  (Riemann has no cross terms)
#
# Therefore Q_4(X) = 5(R_1+R_2)^2 - 2(|Ric_1|^2+|Ric_2|^2) + 2(|Riem_1|^2+|Riem_2|^2)
#                  = Q_4(M_1) + Q_4(M_2) + 10 R_1 R_2
#
# Integrating over X:
#   int_X Q_4(X) dV_X = Q_4(X) * Vol_X  (since X is homogeneous)
#                      = (Q_4(M_1) + Q_4(M_2) + 10 R_1 R_2) * Vol_1 * Vol_2
#
# Then: a_4(X) = (4pi)^{-(d1+d2)/2} * (1/360) * int_X Q_4 dV
#
# NOTE: This direct integration method must agree with the convolution formula.
# The convolution formula reads (with tilde coefficients):
#   tA_4(X) = tA_4(M_1)*tA_0(M_2) + tA_2(M_1)*tA_2(M_2) + tA_0(M_1)*tA_4(M_2)
# which equals:
#   = (Q4_1/360)*V1 * V2 + (R1/6)*V1 * (R2/6)*V2 + V1 * (Q4_2/360)*V2
#   = V1*V2 * [Q4_1/360 + Q4_2/360 + R1*R2/36]
#   = V1*V2/360 * [Q4_1 + Q4_2 + 10 R1 R2]  (since 360/36 = 10)
# This confirms the identity.

print("\n" + "=" * 70)
print("DIRECT INTEGRATION VERIFICATION")
print("=" * 70)

R_X = R_CP2 + R_S3
RicSq_X = RicSq_CP2 + RicSq_S3
RiemSq_X = RiemSq_CP2 + RiemSq_S3
Vol_X = Vol_CP2 * Vol_S3

Q4_X = 5 * R_X**2 - 2 * RicSq_X + 2 * RiemSq_X
a4_direct = prefactor_product * (1.0/360.0) * Q4_X * Vol_X

print(f"\n  Product curvature invariants (pointwise):")
print(f"    R_X = {R_CP2} + {R_S3} = {R_X}")
print(f"    |Ric_X|^2 = {RicSq_CP2} + {RicSq_S3} = {RicSq_X}")
print(f"    |Riem_X|^2 = {RiemSq_CP2} + {RiemSq_S3} = {RiemSq_X}")
print(f"    Vol_X = {Vol_X / np.pi**4:.6f} pi^4")
print(f"\n  Q_4(X) = 5({R_X})^2 - 2({RicSq_X}) + 2({RiemSq_X})")
print(f"         = {5*R_X**2} - {2*RicSq_X} + {2*RiemSq_X} = {Q4_X}")
print(f"\n  a_4(direct) = (4pi)^{{-7/2}} * {Q4_X}/360 * pi^4")
print(f"              = {a4_direct:.10e}")
print(f"  a_4(convolution) = {a4_product:.10e}")
print(f"  Match: {np.isclose(a4_direct, a4_product)}")


# =============================================================================
# SECTION 9: SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print(f"""
Product manifold:  X = CP^2 x S^3     (dim = 7)
Metrics:           Fubini-Study (H=4) x Round (r=1)

Individual Seeley-DeWitt coefficients (scalar Laplacian, tilde form):
  CP^2:  tA_0 = pi^2/2,    tA_2 = 2 pi^2,     tA_4 = {frac_tA4_CP2} pi^2
  S^3:   tA_0 = 2 pi^2,    tA_2 = 2 pi^2,     tA_4 = {frac_tA4_S3} pi^2

Convolution:
  tA_4(X) = {frac_term1} + {frac_term2} + {frac_term3}
          = {frac_total}  pi^4
          = {float(frac_total):.10f}  pi^4

Full coefficient:
  a_4(CP^2 x S^3) = {frac_a4_coeff} sqrt(pi)
                   = {float(frac_a4_coeff)*np.sqrt(np.pi):.10e}

Gauge coupling (spectral action, f_0 = 1):
  kappa_{{U(1)}} = sqrt(pi) / 1536
               = {np.sqrt(np.pi)/1536:.10e}

  alpha_{{U(1)}}^{{-1}} = 4 pi * kappa = 4 pi^{{3/2}} / 1536
                      = pi^{{3/2}} / 384
                      = {np.pi**1.5 / 384:.10e}

  => alpha_{{U(1)}} = 384 / pi^{{3/2}} = {384 / np.pi**1.5:.6f}
""")
