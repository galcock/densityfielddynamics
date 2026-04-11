"""
L4: Scan ⟨G_eff/G⟩ for configurations giving exactly 16/3.

v3.3 formula:  G_eff/G = 1 / [ μ(x · (1 + L·(k̂·ĝ)²)) ]
with μ(y) = y/(1+y)  ⇒  1/μ(y) = 1 + 1/y

Direction averaging over k̂·ĝ = cos θ ∈ [-1,1]:
    ⟨G_eff/G⟩(x,L) = 1 + (1/2)∫_{-1}^{1} dμ /(x(1+Lμ²))
                    = 1 + (1/x) · (1/√L) · arctan(√L)/...
We evaluate numerically and search for 16/3.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

TARGET = 16.0 / 3.0          # 5.333333...
ALPHA  = 1.0 / 137.035999084

# ---------- μ families ----------
def mu_simple(y):                     # standard MOND-like
    return y / (1.0 + y)

def mu_alpha_lambda(y, a=1.0, lam=1.0):
    # v3.3 family: μ_{α,λ}(y) = y^α / (1 + y^(α·λ))^(1/λ)
    return y**a / (1.0 + y**(a*lam))**(1.0/lam)

def mu_n(y, n=2):                     # μ_n(y) = y / (1+y^n)^(1/n)
    return y / (1.0 + y**n)**(1.0/n)

# ---------- directional average ----------
def avg_Geff_over_G(x, L, mu=mu_simple, weight=None):
    """Average 1/μ(x(1+L cos²θ)) over isotropic directions (sin θ dθ)."""
    def integrand(c):                 # c = cos θ ∈ [0,1], symmetric
        y = x * (1.0 + L*c*c)
        w = 1.0 if weight is None else weight(c)
        return w / mu(y)
    num, _ = quad(integrand, 0.0, 1.0, limit=200)
    if weight is None:
        return num                    # ∫_0^1 dc = 1 already normalized
    den, _ = quad(weight, 0.0, 1.0, limit=200)
    return num/den

# ---------- scan over x for several L, μ ----------
def find_x_crit(L, mu=mu_simple, weight=None, xlo=1e-6, xhi=1e3):
    f = lambda x: avg_Geff_over_G(x, L, mu, weight) - TARGET
    try:
        flo, fhi = f(xlo), f(xhi)
        if flo*fhi > 0:
            return None
        return brentq(f, xlo, xhi, xtol=1e-14)
    except Exception:
        return None

# weights to try
w_k2   = lambda c: c*c           # growth mode weight
w_perp = lambda c: 1 - c*c       # transverse
w_ob   = lambda c: np.exp(-c*c)  # baryon-density-like localization

natural_scales = {
    "alpha":          ALPHA,
    "sqrt(alpha)":    np.sqrt(ALPHA),
    "alpha^2":        ALPHA**2,
    "1/137":          1/137.0,
    "1/(4pi)":        1/(4*np.pi),
    "1/sqrt(3)":      1/np.sqrt(3),
    "1/sqrt(4)":      0.5,
    "1/sqrt(5)":      1/np.sqrt(5),   # k=3 sector
    "1/sqrt(6)":      1/np.sqrt(6),
    "3/16":           3/16,
    "16/3-1":         TARGET-1,
    "1/(TARGET-1)":   1/(TARGET-1),   # = 3/13
    "3/13":           3/13,
    "ln2":            np.log(2),
    "pi/6":           np.pi/6,
}

print(f"TARGET ⟨G_eff/G⟩ = 16/3 = {TARGET:.10f}\n")

rows = []
for muname, muf in [("simple x/(1+x)", mu_simple),
                    ("mu_2 (n=2)",     lambda y: mu_n(y,2)),
                    ("mu_3 (n=3)",     lambda y: mu_n(y,3)),
                    ("mu_{1,2}",       lambda y: mu_alpha_lambda(y,1,2)),
                    ("mu_{2,1}",       lambda y: mu_alpha_lambda(y,2,1))]:
    for L in [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        for wname, w in [("iso",None),("k2",w_k2),("perp",w_perp),("gauss",w_ob)]:
            xc = find_x_crit(L, muf, w)
            if xc is not None:
                rows.append((muname, L, wname, xc))

print(f"{'mu':<18}{'L':>6}{'weight':>8}{'x_crit':>20}   match?")
print("-"*70)
for muname,L,w,xc in rows:
    match = ""
    for nm,val in natural_scales.items():
        if abs(xc-val)/max(val,1e-30) < 1e-3:
            match = f"  <-- {nm}={val:.6g}"
            break
    print(f"{muname:<18}{L:>6.2f}{w:>8}{xc:>20.10g}{match}")

# analytic check for simple μ, isotropic, L=0: ⟨G_eff/G⟩=1+1/x → 16/3 ⇒ x=3/13
x0 = 3.0/13.0
val = avg_Geff_over_G(x0, 0.0, mu_simple)
print(f"\nAnalytic check: μ_simple, L=0, x=3/13 → ⟨G_eff/G⟩ = {val:.12f}  (target {TARGET:.12f})")

# Is 3/13 a "natural" DFD scale? Check against 1/(k+2) family
for k in range(0,12):
    if abs(x0 - 1.0/(k+2)) < 1e-6:
        print(f"  3/13 matches 1/(k+2) with k={k}?  no.  1/(k+2)={1/(k+2):.6g}")
print(f"  3/13 = {3/13:.10f};  closest simple rationals: 3/13 exactly.")
print(f"  α⁻¹·3/13 = {3/13/ALPHA:.4f} (not obviously meaningful)")
print(f"  3/13 vs 1/√17 = {1/np.sqrt(17):.6f} — not a match")
