"""
constants.py -- Physical constants and default parameters for DFD psi-bubble simulations.

All quantities in SI units unless otherwise noted.
"""

import numpy as np

# ============================================================
# Fundamental constants
# ============================================================
c       = 2.998e8          # speed of light [m/s]
G       = 6.674e-11        # gravitational constant [m^3 kg^-1 s^-2]
hbar    = 1.055e-34        # reduced Planck constant [J s]
eps0    = 8.854e-12        # vacuum permittivity [F/m]
mu0     = 4.0 * np.pi * 1e-7   # vacuum permeability [H/m]
k_B     = 1.381e-23        # Boltzmann constant [J/K]
alpha_FS = 1.0 / 137.036   # fine-structure constant (DFD-derived)
M_earth = 5.972e24         # Earth mass [kg]
R_earth = 6.371e6          # Earth radius [m]

# ============================================================
# MOND acceleration scale (Milgrom)
# ============================================================
a0_MOND = 1.2e-10          # MOND acceleration scale [m/s^2]

# ============================================================
# Reference vehicle parameters
# ============================================================
R_outer       = 5.0         # outer shell radius [m]
R_inner       = 4.5         # inner shell radius [m]  (shell thickness 0.5 m)
R_sc_inner    = 4.4         # inner superconductor layer radius [m]
R_sc_outer    = 4.5         # outer superconductor layer radius (= R_inner of ferrite) [m]

# Ferrite: NiZn  (representative values)
eps_r_ferrite = 12.0        # relative permittivity of ferrite shell
mu_r_ferrite  = 800.0       # relative permeability of ferrite shell
sigma_ferrite = 1e-2        # conductivity [S/m] (low-loss ferrite)

# YBCO Superconductor
T_c_YBCO      = 93.0        # critical temperature [K]
lambda_L_YBCO = 150e-9      # London penetration depth [m]

# ============================================================
# DFD coupling constant
# ============================================================
# The DFD field equation couples the metric potential psi to the
# electromagnetic energy density through  (4 pi G / c^4).
# This is the fundamental coupling in Einstein's equations rewritten
# in DFD form.
kappa_DFD = 4.0 * np.pi * G / c**4   # ~ 9.3e-44  [m/J]

# ============================================================
# Quantum coherence enhancement
# ============================================================
# In DFD, a macroscopically quantum-coherent EM field (e.g. inside a
# superconducting cavity) can enhance the gravitational coupling by
# a factor N_coherent ~ number of coherent Cooper pairs or photons.
# This is analogous to the Dicke superradiance factor.
# Conservative estimate: N_coh ~ 1 (no enhancement)
# Optimistic superconductor estimate: N_coh ~ 10^12 - 10^20
N_coh_default = 1.0         # default: no enhancement

# ============================================================
# Energy scales for parameter sweeps
# ============================================================
E_stored_ref = {
    '1 MJ': 1e6,
    '1 GJ': 1e9,
    '1 TJ': 1e12,
}

# ============================================================
# Helper: background gravitational potential gradient
# ============================================================
def psi_background_earth(r_orbit):
    """
    Background Newtonian potential psi = -GM/(r c^2) at orbital radius r.
    Returns dimensionless psi and its gradient dpsi/dr.
    """
    psi = -G * M_earth / (r_orbit * c**2)
    dpsi_dr = G * M_earth / (r_orbit**2 * c**2)
    return psi, dpsi_dr

def psi_background_deep_space():
    """
    In deep space far from massive bodies, the background gradient is
    dominated by the galactic field.  We approximate |dpsi/dr| ~ a0/c^2
    (the MOND scale), which is the regime where MOND nonlinearity matters.
    """
    dpsi_dr = a0_MOND / c**2   # ~ 1.3e-27 m^-1
    return 0.0, dpsi_dr
