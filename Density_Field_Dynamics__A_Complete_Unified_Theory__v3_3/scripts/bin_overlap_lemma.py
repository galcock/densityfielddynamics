#!/usr/bin/env python3
"""
Computes the Z3×Z3 bin-overlap weights for the order-3 class in A5.
Verifies Lemma Y.X: r(C3; r,s) = 8/3 (diagonal), 2 (off-diagonal).
"""
import numpy as np
from fractions import Fraction

def build_A5():
    """Build A5 and return (G, mult_table, idx, a_idx, e_idx, C3)"""
    def mult_perm(p1, p2):
        return tuple(p1[p2[i]] for i in range(5))
    
    def inv_perm(p):
        inv = [0]*5
        for i in range(5):
            inv[p[i]] = i
        return tuple(inv)
    
    e = (0, 1, 2, 3, 4)
    a = (1, 2, 0, 3, 4)  # (0 1 2) order-3
    b = (1, 2, 3, 4, 0)  # (0 1 2 3 4) order-5
    
    G = set([e])
    frontier = [e]
    gens = [a, inv_perm(a), b, inv_perm(b)]
    while frontier:
        g = frontier.pop()
        for gen in gens:
            h = mult_perm(gen, g)
            if h not in G:
                G.add(h)
                frontier.append(h)
    
    G = list(G)
    n = len(G)
    idx = {g: i for i, g in enumerate(G)}
    
    mult_table = np.zeros((n, n), dtype=int)
    for i, g in enumerate(G):
        for j, h in enumerate(G):
            mult_table[i, j] = idx[mult_perm(g, h)]
    
    e_idx = idx[e]
    a_idx = idx[a]
    
    def order(g_idx):
        x = e_idx
        for k in range(1, 100):
            x = mult_table[x, g_idx]
            if x == e_idx:
                return k
        return -1
    
    C3 = [i for i in range(n) if order(i) == 3]
    
    return G, mult_table, idx, a_idx, e_idx, C3

def compute_bin_overlaps():
    """Compute the Z3×Z3 bin-overlap matrix."""
    G, mult_table, idx, a_idx, e_idx, C3 = build_A5()
    n = len(G)
    omega = np.exp(2j * np.pi / 3)
    
    # Left action L(a): L(a)|g⟩ = |ag⟩
    L_a = np.zeros((n, n), dtype=complex)
    for i in range(n):
        L_a[mult_table[a_idx, i], i] = 1
    
    # Right action R(a): R(a)|g⟩ = |ga⟩
    R_a = np.zeros((n, n), dtype=complex)
    for i in range(n):
        R_a[mult_table[i, a_idx], i] = 1
    
    # Z3 projectors
    P_L = {}
    P_R = {}
    for r in range(3):
        P_L[r] = (np.eye(n) + omega**(-r) * L_a + omega**(-2*r) * (L_a @ L_a)) / 3
        P_R[r] = (np.eye(n) + omega**(-r) * R_a + omega**(-2*r) * (R_a @ R_a)) / 3
    
    # Class projector
    P_C3 = np.zeros((n, n))
    for g in C3:
        P_C3[g, g] = 1
    
    # Compute bin overlaps
    W = np.zeros((3, 3))
    for r in range(3):
        for s in range(3):
            tr = np.real(np.trace(P_C3 @ P_L[r] @ P_R[s]))
            W[r, s] = tr
    
    return W

if __name__ == "__main__":
    print("="*60)
    print("Z3×Z3 Bin-Overlap Lemma Verification")
    print("="*60)
    print()
    
    W = compute_bin_overlaps()
    
    print("r(C3; r, s) = Tr(P_C3 P_r^L P_s^R):")
    print()
    print("       s=0      s=1      s=2")
    for r in range(3):
        print(f"r={r}  ", end="")
        for s in range(3):
            frac = Fraction(W[r, s]).limit_denominator(10)
            print(f"{str(frac):8s} ", end="")
        print()
    
    print()
    print("Expected: diagonal = 8/3, off-diagonal = 2")
    print(f"Diagonal values: {[Fraction(W[i,i]).limit_denominator(10) for i in range(3)]}")
    print(f"Off-diagonal values: {[Fraction(W[i,j]).limit_denominator(10) for i in range(3) for j in range(3) if i != j]}")
    
    diag_ok = all(abs(W[i,i] - 8/3) < 0.01 for i in range(3))
    offdiag_ok = all(abs(W[i,j] - 2) < 0.01 for i in range(3) for j in range(3) if i != j)
    
    print()
    print(f"Verification: diagonal = 8/3? {diag_ok}")
    print(f"Verification: off-diagonal = 2? {offdiag_ok}")
    print(f"LEMMA VERIFIED: {diag_ok and offdiag_ok}")
