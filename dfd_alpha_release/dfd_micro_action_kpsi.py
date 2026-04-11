#!/usr/bin/env python3
"""DFD (k,psi) microsector utilities for lattice simulations.

Implements:
  - SU(2)_k Chern–Simons partition function on S^3 (Witten): Z = S_00
  - Reflection-positive weight w(k) = |Z|^2
  - Coarse-graining map psi(k) = -(1/zeta) log( w(k) / w(k_ref) )
  - Lattice action terms used for the kappa_r background-field extraction.

Designed to be imported by:
  dfd_kappa_backgroundfield_mc.py

Reference:
  - E. Witten, 'Quantum Field Theory and the Jones Polynomial',
    Commun. Math. Phys. 121 (1989) 351.
"""
from __future__ import annotations
import numpy as np

def su2_cs_Z_S3(k: int | np.ndarray) -> np.ndarray:
    """Z(S^3; SU(2)_k) = sqrt(2/(k+2)) * sin(pi/(k+2))."""
    k = np.asarray(k, dtype=float)
    if np.any(k < 0):
        raise ValueError("k must be >= 0 for SU(2)_k CS.")
    return np.sqrt(2.0/(k+2.0)) * np.sin(np.pi/(k+2.0))

def w_of_k(k: int | np.ndarray) -> np.ndarray:
    """Reflection-positive Euclidean weight w(k)=|Z|^2."""
    Z = su2_cs_Z_S3(k)
    return (Z * Z).astype(float)

def psi_of_k(k: int | np.ndarray, *, zeta: float = 1.0, k_ref: int = 1) -> np.ndarray:
    """psi(k) = -(1/zeta) log( w(k)/w(k_ref) )."""
    if k_ref < 0:
        raise ValueError("k_ref must be >=0")
    wk = w_of_k(k)
    wref = float(w_of_k(np.asarray([k_ref]))[0])
    return -(1.0/float(zeta)) * np.log(wk / wref)

def action_kpsi(k_field: np.ndarray, neighbors: np.ndarray, *, Kpsi: float, zeta: float = 1.0, k_ref: int = 1) -> float:
    """S_k + S_grad = sum_x[-log w(k_x)] + (Kpsi/2) sum_<xy> (psi_x-psi_y)^2."""
    kf = np.asarray(k_field)
    if not np.issubdtype(kf.dtype, np.integer):
        raise TypeError("k_field must be integer dtype")
    if np.any(kf < 0):
        raise ValueError("k_field must be >=0")
    psi = psi_of_k(kf, zeta=zeta, k_ref=k_ref)
    Sk = float(np.sum(-np.log(w_of_k(kf))))
    dpsi = psi[neighbors[:,0]] - psi[neighbors[:,1]]
    Sg = 0.5 * float(Kpsi) * float(np.sum(dpsi*dpsi))
    return Sk + Sg

def plaquette_psi(psi_site: np.ndarray, plaq_corners: np.ndarray) -> np.ndarray:
    """Average psi over 4 corners for each plaquette (P,4)->(P,)."""
    return psi_site[plaq_corners].mean(axis=1)
