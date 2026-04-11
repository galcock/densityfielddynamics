#!/usr/bin/env python3
"""
Round 3: Self-consistent P(k) with sigma_nabla regularisation + QUMOND.

Key correction: proper normalisation of P(k) using the Poisson equation
to convert from primordial curvature R to matter density delta:
  Delta^2_delta(k) = (4/25) * (ck/(aH))^4 / Omega_m^2 * T^2 * D^2 * Delta^2_R(k)

For the baryon-only case, Omega_m -> Omega_b in the Poisson source.
"""

import numpy as np
from scipy.integrate import solve_ivp
import json

# ============================================================
# Constants
# ============================================================
c = 2.998e8; G = 6.674e-11; H0 = 2.184e-18; Mpc = 3.0857e22; hh = 0.674
rho_crit = 3*H0**2/(8*np.pi*G)
Ob = 0.049; Om = 0.315
rho_b0 = Ob*rho_crit
Ob_h2 = Ob*hh**2; Om_h2 = Om*hh**2
ns = 0.9649; As = 2.1e-9; kpiv = 0.05  # 1/Mpc
a0_mond = 1.2e-10; astar = 2*a0_mond/c**2
prefac0 = 8*np.pi*G*rho_b0/c**2

Nk = 4000
k_h = np.logspace(-4, 1.5, Nk)  # h/Mpc

print("="*70)
print("R3: Self-consistent P(k) with sigma_nabla regularisation")
print("="*70)

# ============================================================
# Transfer functions (EH98)
# ============================================================
def eh_baryon(k_arr, ob_h2):
    om = ob_h2; th = 2.7255/2.7
    keq = 7.46e-2*om*th**(-2)
    b1d = 0.313*om**(-0.419)*(1+0.607*om**0.674)
    b2d = 0.238*om**0.223
    zd = 1291*om**0.251/(1+0.659*om**0.828)*(1+b1d*ob_h2**b2d)
    Rd = 31.5e3*ob_h2*th**(-4)/zd
    Req = 31.5e3*ob_h2*th**(-4)/(2.5e4*om*th**(-4))
    s = (2/(3*keq))*np.sqrt(6/Req)*np.log(
        (np.sqrt(1+Rd)+np.sqrt(Rd+Req))/(1+np.sqrt(Req)))
    ksilk = 1.6*ob_h2**0.52*om**0.73*(1+(10.4*om)**(-0.95))
    a1 = (46.9*om)**0.670*(1+(32.1*om)**(-0.532))
    a2 = (12.0*om)**0.424*(1+(45.0*om)**(-0.582))
    ab = 2.07*keq*s*(1+Rd)**(-0.75)*a1**(-1)*a2**(-1)
    bb = 1.5+np.sqrt((17.2*om)**2+1)
    bn = 8.41*om**0.435
    T = np.empty_like(k_arr)
    for i,k in enumerate(k_arr):
        q = k/(13.41*keq); x = k*s
        xe = x*(1+(bn/x)**3)**(-1./3) if abs(x)>1e-10 else 0.0
        j0 = np.sin(xe)/xe if abs(xe)>1e-8 else 1.0
        Cnw = 14.2+386/(1+69.9*q**1.08)
        T0 = np.log(np.e+1.8*q)/(np.log(np.e+1.8*q)+Cnw*q**2)
        T[i] = (T0/(1+(x/5.2)**2)+ab/(1+(bb/x)**3)*np.exp(-(k/ksilk)**1.4))*j0 if abs(x)>1e-10 else T0
    return T

def eh_full(k_arr, ob_h2, om_h2):
    fb = ob_h2/om_h2; fc = 1-fb
    th = 2.7255/2.7
    keq = 7.46e-2*om_h2*th**(-2)
    b1d = 0.313*om_h2**(-0.419)*(1+0.607*om_h2**0.674)
    b2d = 0.238*om_h2**0.223
    zd = 1291*om_h2**0.251/(1+0.659*om_h2**0.828)*(1+b1d*ob_h2**b2d)
    Rd = 31.5e3*ob_h2*th**(-4)/zd
    Req = 31.5e3*ob_h2*th**(-4)/(2.5e4*om_h2*th**(-4))
    s = (2/(3*keq))*np.sqrt(6/Req)*np.log(
        (np.sqrt(1+Rd)+np.sqrt(Rd+Req))/(1+np.sqrt(Req)))
    ksilk = 1.6*ob_h2**0.52*om_h2**0.73*(1+(10.4*om_h2)**(-0.95))
    a1 = (46.9*om_h2)**0.670*(1+(32.1*om_h2)**(-0.532))
    a2 = (12.0*om_h2)**0.424*(1+(45.0*om_h2)**(-0.582))
    ac = a1**(-fb)*a2**(-fb**3)
    b1c = 0.944/(1+(458*om_h2)**(-0.708))
    b2c = (0.395*om_h2)**(-0.0266)
    bc = 1/(1+b1c*(max(fc,1e-10)**b2c-1))
    ab = 2.07*keq*s*(1+Rd)**(-0.75)*a1**(-fb)*a2**(-fb**3)
    bb = 0.5+fb+(3-2*fb)*np.sqrt((17.2*om_h2)**2+1)
    bn = 8.41*om_h2**0.435
    T = np.empty_like(k_arr)
    for i,k in enumerate(k_arr):
        q = k/(13.41*keq); x = k*s
        def T0f(a_,b_):
            C_ = 14.2/a_+386/(1+69.9*q**1.08)
            return np.log(np.e+1.8*b_*q)/(np.log(np.e+1.8*b_*q)+C_*q**2)
        f_ = 1/(1+(x/5.4)**4)
        Tc = f_*T0f(1,bc)+(1-f_)*T0f(ac,bc)
        xe = x*(1+(bn/x)**3)**(-1./3) if abs(x)>1e-10 else 0.0
        j0 = np.sin(xe)/xe if abs(xe)>1e-8 else 1.0
        Cnw = 14.2+386/(1+69.9*q**1.08)
        T0 = np.log(np.e+1.8*q)/(np.log(np.e+1.8*q)+Cnw*q**2)
        Tb = (T0/(1+(x/5.2)**2)+ab/(1+(bb/x)**3)*np.exp(-(k/ksilk)**1.4))*j0 if abs(x)>1e-10 else T0
        T[i] = fb*Tb+fc*Tc
    return T


# ============================================================
# Power spectrum with correct normalisation
# ============================================================
def make_Pk(k_hMpc, Tk, Dgrowth, Omega_source):
    """
    P_delta(k) in (Mpc/h)^3.

    The relation from primordial curvature R to matter overdensity delta:
      delta(k,z) = (2/3) * (ck/(aH))^2 / Omega_m * T(k) * D(z) * (3/5) * R(k)

    Wait, more carefully at z=0:
      delta_k = (2/5) * (ck/H0)^2 / Omega_m * T(k) * D(z=0) * R_k

    Hmm, the standard relation uses the Poisson equation during matter domination:
      Phi_k = -(3/2)(H0/k)^2 * Omega_m / a * delta_k  ->  at a=1:
      delta_k = -(2/3)(k/H0)^2 * Phi_k / Omega_m

    And Phi_k(z) = (9/10) * R_k * T(k) * (D(z)/a)  (with Phi constant during MD)
    Actually, the exact relation involves the transfer function normalised so T(0)=1.
    In the matter era: Phi = (3/5) R for adiabatic ICs (radiation era -> matter era transfer).
    Then Phi(k,z) = (3/5) R_k T(k) D(z)/a  (with D normalised to a in MD era).
    And D(z=0) from the growth solver already accounts for the late-time decay.

    So: delta_k = (2/3)(ck/H0)^2 * (3/5) * R_k * T(k) * D(0) / Omega_m
                = (2/5)(ck/H0)^2 * T(k) * D(0) / Omega_m * R_k

    P_delta(k) = (2/5)^2 * (ck/H0)^4 * T^2(k) * D^2(0) / Omega_m^2 * P_R(k)
    where P_R(k) = (2*pi^2/k^3) * As * (k/kpiv)^{ns-1}

    In conventional units with k in 1/Mpc:
      (ck/H0) = c * k_Mpc / (H0)  [dimensionless if k is in proper 1/m]
      k_m = k_Mpc / Mpc
      (ck_m/H0) is dimensionless

    For output in (Mpc/h)^3 with k in h/Mpc:
      k_Mpc = k_hMpc * h
    """
    k_Mpc = k_hMpc * hh            # 1/Mpc
    k_m = k_Mpc / Mpc              # 1/m
    ckH0 = c * k_m / H0            # dimensionless

    # Primordial P_R(k) = (2*pi^2/k^3) * As * (k/kpiv)^{ns-1}
    # in Mpc^3 with k in 1/Mpc
    PR_Mpc3 = (2*np.pi**2 / k_Mpc**3) * As * (k_Mpc/kpiv)**(ns-1)

    # P_delta = (2/5)^2 * (ck/H0)^4 * T^2 * D^2 / Omega_source^2 * P_R
    # in Mpc^3 with k in 1/Mpc
    Pdelta = (2./5.)**2 * ckH0**4 * Tk**2 * Dgrowth**2 / Omega_source**2 * PR_Mpc3

    # Convert to (Mpc/h)^3
    return Pdelta * hh**3


def sigma_R(Pk, k_arr, R=8.0):
    """sigma_R. Pk in (Mpc/h)^3, k in h/Mpc, R in Mpc/h."""
    x = k_arr*R
    W = np.where(x<1e-3, 1-x**2/10, 3*(np.sin(x)-x*np.cos(x))/x**3)
    return np.sqrt(np.trapezoid(k_arr**3*Pk*W**2, np.log(k_arr))/(2*np.pi**2))


def sigma_nabla_integral(Pk, k_arr):
    """
    Compute integral P_delta(k) dk/(2*pi^2) in physical units (m^2).
    Then sigma_nabla = prefac0 * sqrt(integral).

    NOTE: this is the integral of the DENSITY power spectrum, not the
    potential power spectrum. sigma_nabla involves the gradient of the
    POTENTIAL, so we need:

    sigma_nabla^2 = integral k^2 P_psi(k) k^2 dk/(2*pi^2)  -- NO

    Let me redo: for the MOND argument, sigma_nabla = sqrt(<|grad psi|^2>).
    psi = Newtonian potential / c^2 (dimensionless).

    In QUMOND: we need |grad psi_N| where psi_N is the Newtonian potential.
    nabla^2 psi_N = (8*pi*G*rho_b0/(c^2*a^3)) * delta  [comoving, with a=1 at z=0]

    psi_N(k) = -(8*pi*G*rho_b0/c^2) * delta(k) / k^2  [at z=0, a=1]
    |grad psi_N|^2: integral k^2 * |psi_N(k)|^2 * 4*pi*k^2 dk/(2*pi)^3
                  = integral k^4 * P_psi(k) dk/(2*pi^2)

    P_psi(k) = (8*pi*G*rho_b0/c^2)^2 * P_delta(k) / k^4

    sigma_nabla^2 = (8*pi*G*rho_b0/c^2)^2 * integral P_delta(k) dk/(2*pi^2)

    where integral is over physical k and P in physical units.
    """
    kp = k_arr*hh/Mpc            # 1/m
    Pp = Pk/hh**3*Mpc**3          # m^3
    I = np.trapezoid(Pp*kp, np.log(kp))/(2*np.pi**2)  # m^2
    return I  # in m^2


# ============================================================
# Growth solvers
# ============================================================
def solve_growth_std(Om_p, Om_e, OL):
    def rhs(x,y):
        a=np.exp(x); H2=Om_e/a**3+OL
        f_=2+a*(-3*Om_e/a**4)/(2*H2)
        g_=1.5*Om_p/(a**3*H2)
        return [y[1], g_*y[0]-f_*y[1]]
    ai=1e-4
    sol=solve_ivp(rhs,[np.log(ai),0],[ai,ai],method='RK45',rtol=1e-10,atol=1e-13,dense_output=True)
    return sol.sol(0.0)[0]


def solve_growth_mond_sc(Ob_val, OL, sI0_m2, D_norm):
    """
    Growth with self-consistent time-dependent MOND.
    sI0_m2: integral P_delta dk/(2*pi^2) at z=0, in m^2.
    D_norm: current estimate of D(z=0) for normalising sigma_nabla(a).

    sigma_nabla(a) = prefac0 * a^{-3} * D(a)/D_norm * sqrt(sI0_m2)
    y(a) = sigma_nabla(a) / astar
    nu(a) = [1 + sqrt(1 + 4/y(a))]/2
    """
    sI_sqrt = np.sqrt(max(sI0_m2, 0))

    def rhs(x, Y):
        a = np.exp(x)
        D = Y[0]
        H2 = Ob_val/a**3 + OL
        f_ = 2 + a*(-3*Ob_val/a**4)/(2*H2)

        # sigma_nabla at this epoch
        sn = prefac0 * a**(-3) * abs(D)/D_norm * sI_sqrt
        y = sn/astar

        if y > 1e-10:
            nu = 0.5*(1+np.sqrt(1+4/y))
        else:
            nu = 1.0  # Newtonian floor
        nu = min(nu, 1e4)

        g_ = 1.5*nu*Ob_val/(a**3*H2)
        return [Y[1], g_*Y[0]-f_*Y[1]]

    ai = 1e-4
    sol = solve_ivp(rhs, [np.log(ai), 0], [ai, ai],
                    method='RK45', rtol=1e-9, atol=1e-12,
                    dense_output=True, max_step=0.02)
    return sol.sol(0.0)[0]


# ============================================================
# Step 1: Baselines
# ============================================================
print("Step 1: Baselines")
print("-"*50)
Tb = eh_baryon(k_h, Ob_h2)
Tl = eh_full(k_h, Ob_h2, Om_h2)

D_bary = solve_growth_std(Ob, Ob, 1-Ob)
D_lcdm = solve_growth_std(Om, Om, 1-Om)

# For baryon-only P(k): the Poisson source is Omega_b, so Omega_source = Omega_b
Pb = make_Pk(k_h, Tb, D_bary, Ob)
# For LCDM: Omega_source = Omega_m
Pl = make_Pk(k_h, Tl, D_lcdm, Om)

s8b = sigma_R(Pb, k_h); s8l = sigma_R(Pl, k_h)
sI_b = sigma_nabla_integral(Pb, k_h)
sn_b = prefac0*np.sqrt(sI_b)

print(f"  D_bary={D_bary:.6f}, D_LCDM={D_lcdm:.6f}")
print(f"  sig8_bary={s8b:.4f}, sig8_LCDM={s8l:.4f}")
print(f"  P_bary(0.1)={np.interp(0.1,k_h,Pb):.2f} (Mpc/h)^3")
print(f"  P_LCDM(0.1)={np.interp(0.1,k_h,Pl):.2f} (Mpc/h)^3")
print(f"  sigma_nabla_bary={sn_b:.4e} m^-1")
print(f"  y_bary={sn_b/astar:.4e}")
print()


# ============================================================
# Step 2: Self-consistent iteration
# ============================================================
print("Step 2: Self-consistent iteration")
print("-"*50)

# The DFD power spectrum:
# P_DFD(k) = nu^2(y_eff) * make_Pk(k, Tb, D_DFD, Ob)
# where D_DFD is the MOND-enhanced growth factor.
#
# The nu^2 factor boosts the z=0 potential (QUMOND).
# The enhanced D comes from solving the growth ODE with G_eff(a) = nu(y(a))*G.

# BUT: for sigma_nabla, we need the Newtonian potential gradient:
# sigma_nabla = sqrt(<|grad psi_N|^2>)
# where psi_N is what enters the MOND equation.
# The TOTAL force is nu * grad(psi_N), but the ARGUMENT of nu is
# |grad psi_N|, not |grad(nu*psi_N)|.
# So sigma_nabla should be computed from the NEWTONIAN potential,
# which uses P_delta with standard (Newtonian) gravity.
# But wait -- in the self-consistent picture, the density field
# IS already enhanced by MOND (because growth was faster).
# So the density delta itself is bigger, and hence psi_N = -4*pi*G*rho*delta/k^2
# is bigger too.
#
# In other words:
# P_delta_DFD(k) = T_b^2 * D_DFD^2 * primordial  (just growth-enhanced)
# P_psi_N(k) = (prefac0/k^2)^2 * P_delta_DFD(k)
# sigma_nabla from this P_psi_N.
# Then y_eff = sigma_nabla / a* determines nu.
# The TOTAL matter power spectrum seen by observers would be:
# P_total = nu^2 * P_delta_DFD  (because the TOTAL force = nu * F_N,
#   so effective delta_total = nu * delta_N... approximately.)
#
# Actually in QUMOND: the modified Poisson equation is
#   nabla^2 Phi = nabla . [nu(|grad psi_N|/a0) * grad psi_N]
# In the linear regime (nu ~ constant): Phi = nu * psi_N
# So the total gravitational potential is Phi = nu * psi_N.
# The lensing and dynamics see Phi, not psi_N.
# But the matter density delta is sourced by the growth of delta itself,
# not by Phi. The growth equation:
#   delta'' + 2H delta' = 4*pi*G*rho * nu * delta  (in QUMOND)
# So the density perturbation delta grows with G_eff = nu*G.
# P_delta(k,z=0) involves D_DFD which includes the nu-enhancement at each epoch.
#
# For sigma_nabla: we want |grad psi_N|, where psi_N is the NEWTONIAN potential
# of the actual matter distribution:
#   nabla^2 psi_N = (8*pi*G*rho_b/c^2) * delta
# So P_psi_N(k) = (prefac0/k^2)^2 * P_delta_DFD(k)
# And sigma_nabla is from this.
# The nu^2 boost does NOT enter sigma_nabla, only the growth enhancement does.

# For the OBSERVED P(k) that we compare to LCDM:
# The observed clustering is driven by the total force, so
# P_observed ~ P_delta_DFD in many-body simulations (it's the matter delta).
# But the lensing potential is Phi = nu * psi_N, so:
#   P_Phi = nu^2 * P_psi_N
# In LCDM comparison, we compare P_delta to P_delta_LCDM.

# So the comparison P_DFD/P_LCDM should just be:
#   (T_b/T_LCDM)^2 * (D_DFD/D_LCDM)^2 * (Om/Ob)^2
# The (Om/Ob)^2 comes from the normalisation: for baryon-only,
# delta = (2/5)(ck/H0)^2 * T * D / Omega_b * R
# For LCDM: delta = (2/5)(ck/H0)^2 * T * D / Omega_m * R
# So P_bary/P_LCDM = (T_b/T_l)^2 * (D_b/D_l)^2 * (Om/Ob)^2

# Actually, we should compare the OBSERVED power spectra.
# In DFD/MOND, what is observed as "clustering" is the density field delta,
# which is sourced by the growth equation with G_eff = nu*G.
# So P_observed_DFD = P_delta_DFD = make_Pk(k, Tb, D_DFD, Ob)
# This is the actual matter P(k).

max_iter = 150
tol = 1e-8
damp = 0.5

# Start with baryon-only values
# sigma_nabla depends on P_delta_DFD (Newtonian potential of the actual density).
# Initially: P_delta_DFD = P_bary
sI = sI_b
D_prev = D_bary

for it in range(max_iter):
    sn = prefac0*np.sqrt(sI)
    y0 = sn/astar
    if y0 > 1e-15:
        nu0 = 0.5*(1+np.sqrt(1+4/y0))
    else:
        nu0 = 1.0

    # Solve growth with MOND
    D_new = solve_growth_mond_sc(Ob, 1-Ob, sI, D_prev)

    # Build density P(k) at z=0
    P_delta = make_Pk(k_h, Tb, D_new, Ob)

    # New sigma_I from P_delta
    sI_new = sigma_nabla_integral(P_delta, k_h)

    # Damped update in log
    ln_old = np.log(max(sI, 1e-300))
    ln_new = np.log(max(sI_new, 1e-300))
    ln_upd = (1-damp)*ln_old + damp*ln_new
    rel = abs(ln_upd-ln_old)/max(abs(ln_old), 1e-300)

    if it%5==0 or rel<tol:
        sn_new = prefac0*np.sqrt(sI_new)
        y_new = sn_new/astar
        nu_new = 0.5*(1+np.sqrt(1+4/y_new)) if y_new>1e-15 else 1.0
        print(f"  It {it+1:3d}: D={D_new:.4f} nu0={nu0:.4f} y0={y0:.4e} "
              f"sn_new={sn_new:.4e} rel={rel:.2e}")

    D_prev = D_new
    sI = np.exp(ln_upd)

    if rel<tol and it>5:
        print(f"\n  *** Converged after {it+1} iterations ***")
        nconv = it+1; break
else:
    nconv = max_iter
    print(f"\n  Did not converge ({rel:.2e})")

# Final
sn_f = prefac0*np.sqrt(sI)
y_f = sn_f/astar
nu_f = 0.5*(1+np.sqrt(1+4/y_f))
x_f = nu_f*y_f
mu_f = x_f/(1+x_f)
D_f = solve_growth_mond_sc(Ob, 1-Ob, sI, D_prev)

# The observed DFD P(k) is the actual matter density P(k):
P_dfd_delta = make_Pk(k_h, Tb, D_f, Ob)
s8_dfd = sigma_R(P_dfd_delta, k_h)

print()
print("="*70)
print("CONVERGED RESULTS")
print("="*70)
print(f"  sigma_nabla    = {sn_f:.6e} m^-1")
print(f"  a*             = {astar:.6e} m^-1")
print(f"  y_eff          = {y_f:.6e}")
print(f"  nu(y_eff)      = {nu_f:.6f}")
print(f"  x_bar = nu*y   = {x_f:.6e}")
print(f"  mu(x_bar)      = {mu_f:.6f}")
print(f"  G_eff/G = nu   = {nu_f:.6f}")
print(f"  D_bary_Newt    = {D_bary:.6f}")
print(f"  D_DFD          = {D_f:.6f}")
print(f"  D_LCDM         = {D_lcdm:.6f}")
print(f"  D_DFD/D_LCDM   = {D_f/D_lcdm:.6f}")
print(f"  Iterations     = {nconv}")
print()

print("sigma_8:")
print(f"  bary Newt  = {s8b:.4f}")
print(f"  DFD        = {s8_dfd:.4f}")
print(f"  LCDM       = {s8l:.4f}")
print(f"  DFD/LCDM   = {s8_dfd/s8l:.4f}")
print()

b_D2 = (D_f/D_bary)**2
print("Boost (vs bary Newt):")
print(f"  (D_DFD/D_b)^2  = {b_D2:.4f}")
print(f"  nu^2 (pot boost)= {nu_f**2:.4f}")
print()

regime = "DEEP MOND" if y_f<0.1 else ("NEWTONIAN" if y_f>10 else "INTERMEDIATE")
print(f"  MOND regime: {regime} (y={y_f:.4e})")
print()

kt = [0.02,0.05,0.10,0.15]
print("P_DFD_delta / P_LCDM (matter density spectra):")
print(f"  {'k':>8s} {'P_DFD':>14s} {'P_LCDM':>14s} {'Ratio':>10s}")
rats = {}
for k in kt:
    pd = np.interp(k,k_h,P_dfd_delta); pl = np.interp(k,k_h,Pl)
    r = pd/pl if pl>0 else 0; rats[k] = r
    print(f"  {k:8.3f} {pd:14.2f} {pl:14.2f} {r:10.4f}")
print()

# Also show the potential power spectrum P_Phi = nu^2 * P_psi_N
# This is what lensing would see.
P_Phi = P_dfd_delta * nu_f**2  # approximately
print("P_Phi_DFD / P_LCDM (lensing-equivalent, includes nu^2):")
print(f"  {'k':>8s} {'P_Phi':>14s} {'P_LCDM':>14s} {'Ratio':>10s}")
rats_phi = {}
for k in kt:
    pphi = np.interp(k,k_h,P_Phi); pl = np.interp(k,k_h,Pl)
    r = pphi/pl if pl>0 else 0; rats_phi[k] = r
    print(f"  {k:8.3f} {pphi:14.2f} {pl:14.2f} {r:10.4f}")
print()

res = dict(sigma_nabla=float(sn_f), astar=float(astar), y_eff=float(y_f),
           nu=float(nu_f), x_bar=float(x_f), mu_bar=float(mu_f),
           Geff=float(nu_f), D_bary=float(D_bary), D_DFD=float(D_f),
           D_LCDM=float(D_lcdm), D_ratio=float(D_f/D_lcdm),
           sigma8_bary=float(s8b), sigma8_DFD=float(s8_dfd),
           sigma8_LCDM=float(s8l), sigma8_ratio=float(s8_dfd/s8l),
           iterations=nconv, boost_D2=float(b_D2), boost_nu2=float(nu_f**2),
           regime=regime,
           ratios_delta={str(k):float(v) for k,v in rats.items()},
           ratios_phi={str(k):float(v) for k,v in rats_phi.items()})
with open("/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R3_self_consistent_data.json","w") as f:
    json.dump(res,f,indent=2)
np.savez("/Users/garyalcock/claudecode/densityfielddynamics/pk_research/R3_pk_data.npz",
         k_hMpc=k_h, P_bary=Pb, P_DFD_delta=P_dfd_delta, P_LCDM=Pl, P_DFD_Phi=P_Phi)
print("Saved R3_self_consistent_data.json and R3_pk_data.npz")
