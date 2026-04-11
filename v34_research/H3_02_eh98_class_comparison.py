"""
H3-02: Run CLASS with DFD parameters vs Planck 2018 LCDM.

DFD + chi predictions (linear regime, identical to LCDM except fixed ratios):
  H0          = 72.09 km/s/Mpc   (from DFD boundary condition)
  Omega_b h^2 = 0.02237           (BBN-fixed)
  Omega_c h^2 = (16/3) * 0.02237  (DFD: Omega_c/Omega_b = 16/3 exactly)

Planck 2018 LCDM (TT,TE,EE+lowE+lensing):
  H0          = 67.36
  Omega_b h^2 = 0.02237
  Omega_c h^2 = 0.1200
"""
import numpy as np
from classy import Class

A_s  = 2.100e-9
n_s  = 0.9649
k_piv = 0.05  # 1/Mpc

def run_class(H0, omega_b, omega_c, tau=0.0544):
    cosmo = Class()
    cosmo.set({
        'output':'mPk',
        'P_k_max_1/Mpc':5.0,
        'z_pk':0.0,
        'H0':H0,
        'omega_b':omega_b,
        'omega_cdm':omega_c,
        'A_s':A_s,
        'n_s':n_s,
        'tau_reio':tau,
    })
    cosmo.compute()
    h = H0/100.0
    ks = np.array([0.01,0.05,0.1,0.2])  # h/Mpc
    Pk = np.array([cosmo.pk(k*h, 0.0)*h**3 for k in ks])  # (Mpc/h)^3
    sigma8 = cosmo.sigma8()
    rs_d   = cosmo.rs_drag()
    cosmo.struct_cleanup(); cosmo.empty()
    return ks, Pk, sigma8, rs_d

# DFD + chi
omega_b = 0.02237
omega_c_dfd  = (16.0/3.0)*omega_b
ks, Pk_dfd,  s8_dfd,  rs_dfd  = run_class(72.09, omega_b, omega_c_dfd)

# Planck 2018 LCDM
ks2, Pk_lcdm, s8_lcdm, rs_lcdm = run_class(67.36, 0.02237, 0.1200)

print("k [h/Mpc] | P_DFD [(Mpc/h)^3] | P_LCDM [(Mpc/h)^3] | ratio-1 [%]")
for k, pd, pl in zip(ks, Pk_dfd, Pk_lcdm):
    print(f"{k:8.3f} | {pd:18.4e} | {pl:18.4e} | {100*(pd/pl-1):+7.2f}")

print(f"\nsigma8  DFD  = {s8_dfd:.5f}")
print(f"sigma8  LCDM = {s8_lcdm:.5f}")
print(f"delta sigma8 = {100*(s8_dfd/s8_lcdm-1):+.3f} %")
print(f"\nr_s(drag) DFD  = {rs_dfd:.3f} Mpc")
print(f"r_s(drag) LCDM = {rs_lcdm:.3f} Mpc")
print(f"delta r_s      = {100*(rs_dfd/rs_lcdm-1):+.3f} %")

# Derived
h_dfd  = 72.09/100
h_lcdm = 67.36/100
print(f"\nOmega_m (DFD)  = {(omega_b+omega_c_dfd)/h_dfd**2:.4f}")
print(f"Omega_m (LCDM) = {(0.02237+0.1200)/h_lcdm**2:.4f}")
print(f"omega_m (DFD)  = {omega_b+omega_c_dfd:.5f}")
print(f"omega_m (LCDM) = {0.02237+0.1200:.5f}")
