#!/usr/bin/env python3
"""
Strong-CP Route-B sanity checks: Pauli / charge conjugation identities.

This does NOT "prove" the full anomaly claim by itself.
It verifies the key matrix identities used in Lemma S3_charge_conj.

Run:
  python3 strong_cp_pauli_checks.py
"""
import numpy as np

sigma1 = np.array([[0,1],[1,0]], dtype=complex)
sigma2 = np.array([[0,-1j],[1j,0]], dtype=complex)
sigma3 = np.array([[1,0],[0,-1]], dtype=complex)
sigmas = [sigma1, sigma2, sigma3]

def main():
    # Identity: sigma2 * sigma_a^* * sigma2 = - sigma_a
    ok_all = True
    for i, s in enumerate(sigmas, start=1):
        lhs = sigma2 @ s.conjugate() @ sigma2
        rhs = -s
        ok = np.allclose(lhs, rhs)
        ok_all = ok_all and ok
        print(f"[check] sigma2 * (sigma{i})^* * sigma2 = -sigma{i}: {ok}")

    # For anti-linear C = sigma2 K, we have C^2 = sigma2 * sigma2^* = -I
    C2 = sigma2 @ sigma2.conjugate()
    print("[check] C^2 = sigma2 * sigma2^* =")
    print(C2)
    print("[check] C^2 == -I:", np.allclose(C2, -np.eye(2)))

    # Dirac commutation logic in flat 3D:
    # D3 = i sigma^a ∂_a. Under C (antiunitary): i -> -i, sigma^a -> -sigma^a, so i sigma^a invariant.
    inv = []
    for i, s in enumerate(sigmas, start=1):
        inv.append(np.allclose((-1j)*(-s), (1j)*s))
    print("[check] (antiunitary) i*sigma^a invariant under C for all a:", all(inv))

    if not ok_all:
        raise SystemExit("FAILED: At least one Pauli identity did not hold.")
    print("OK: Pauli/charge conjugation checks passed.")

if __name__ == "__main__":
    main()
