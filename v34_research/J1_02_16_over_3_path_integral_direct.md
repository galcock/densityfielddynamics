# J1-02: Direct Path Integral Attempt at Ω_χ/Ω_b = 16/3

**Agent:** J1-2
**Date:** 2026-04-06
**Angle:** Saddle-point evaluation of Z_DFD on FRW × CP² × S³
**Related:** H6, H9 (DOF counting critique), J1-1 (complementary angle)

---

## 1. Setup: DFD partition function on FRW × M_int

On the product background FRW_4 × CP²(R_c) × S³(R_s), the DFD path integral is

    Z_DFD = ∫ D[g] D[ψ] D[χ] D[Φ_SM] exp(−S_DFD[g, ψ, χ, Φ_SM])

with

    S_DFD = S_EH[g] + S_spec[D] + S_ψ[ψ, g] + S_χ[χ, g] + S_matter[Φ_SM, g]

where S_spec = Tr f(D²/Λ²) is the Chamseddine–Connes spectral action on the
7-manifold M_7 = CP² × S³ and D is the Dirac operator built from g and the
internal metric.

Split fields into homogeneous background + perturbations:

    g_μν(x, t) = ḡ_μν(t) + h_μν,   a(t) the FRW scale factor
    ψ(x, t)    = ψ̄(t) + δψ
    χ(x, t)    = χ̄(t) + δχ
    Φ_SM(x, t) = Φ̄(t) + δΦ

Integrating the Gaussian perturbations yields an effective action for the
background only:

    Z_DFD ≈ ∫ D[ā, ψ̄, χ̄, ρ̄] exp(−S_eff[ā, ψ̄, χ̄, ρ̄])

with

    S_eff = ∫ dt a³ [ −3 M_P² (ȧ/a)² + V_eff(ā, ψ̄, χ̄, ρ̄) ]

and

    V_eff = V_spec + V_ψ + V_χ + V_matter + V_int.

---

## 2. The individual pieces

### 2.1 Spectral-action contribution

From the heat-kernel expansion on CP² × S³ (dimension 7 → 4+7),

    V_spec = (f₀ Λ⁴ / 4π²) Vol(M_7)
             + (f₂ Λ² / 4π²) ∫_{M_7} R_int √g_int
             + (f₄ / 4π²) [ a₄ coefficients involving R² ]
             + O(Λ⁻²).

None of these pieces depend on ψ̄, χ̄, or ρ̄_matter; they are a cosmological
constant + curvature correction. They set the vacuum energy but do **not**
couple ψ and matter at leading order.

### 2.2 ψ sector (phase)

    V_ψ = (c²/2) (∂_t ψ̄)² × (gauge-fixed to zero on background)
          + κ ψ̄ (ρ̄_matter − ρ̄_0),

with κ ≈ (4π G/c²) being the ψ↔matter coupling fixed by the ψ EOM c²□ψ = 4πGρ.
Saddle in ψ̄ gives the usual DFD constraint ρ̄_matter = ρ̄_0 on FRW, i.e. ψ̄ tracks
the mean density. This determines ψ̄ given ρ̄_matter; it does **not**
independently fix ρ̄_χ or ρ̄_b.

### 2.3 χ sector

    V_χ = (1/2) m_χ² χ̄² + (λ_χ/4) χ̄⁴ + ...

with dχ̄/dt oscillating once m_χ > H. The saddle equation ∂V_χ/∂χ̄ = 0 has the
trivial solution χ̄ = 0. A nontrivial χ̄ exists only as a *misalignment*
initial condition, not a true minimum of V_eff.

### 2.4 Matter sector

ρ̄_matter is not a field; it is a tracked energy density set by thermal history
plus baryon number conservation. It is **externally fixed by BBN** (η_B ≈
6×10⁻¹⁰) — *no* saddle equation in the path integral determines it from
V_eff alone. You can treat ρ̄_b as a Lagrange multiplier on baryon number, but
then its value is an input, not an output.

---

## 3. The saddle-point calculation that *would* give 16/3

For 16/3 to drop out of ∂V_eff/∂χ̄ = 0, we would need a cross-term linking χ̄
and ρ̄_matter of the form

    V_int = β χ̄² ρ̄_matter + γ ρ̄_matter²/χ̄² + ...

with β, γ set by the spectral decomposition on CP² × S³ such that the
minimizer satisfies

    (χ̄²)_min / ρ̄_matter = 16/3  (in natural units of the relevant scales).

No such cross-term exists in the DFD action as written in v3.3/v3.4. The
spectral action only couples the internal geometry to curvature and to the
ψ/χ kinetic terms, not to ρ_matter directly. V_int ≡ 0 at the level of the
saddle.

**Without a V_int term, the saddle condition in χ̄ is ∂V_χ/∂χ̄ = 0, whose
solution is χ̄ = 0 (ρ_χ = 0). The saddle gives zero dark matter.**

Any nonzero ρ_χ comes from (a) misalignment initial conditions or (b)
gravitational production during inflation — neither of which is a saddle
point of V_eff.

---

## 4. Forcing the issue via initial conditions

Suppose we accept that χ̄ is set by a misalignment at the spectral cutoff Λ
and ask: *can the initial condition be chosen so that the 16/3 ratio holds
today*?

### Initial energy densities

At T = Λ_cut (take Λ_cut ≈ 10¹⁶ GeV, the DFD spectral cutoff),

    ρ_χ,i = (1/2) m_χ² f_a² θ_i²
    ρ_b,i = g_eff T_i⁴ π²/30    (baryons are a relativistic component of a
                                 thermal soup of effective dof g_eff ≈ 100)

Imposing ρ_χ,i / ρ_b,i = 16/3 at T = Λ_cut:

    T_i⁴ = (3/16) × (30/π²) × m_χ² f_a² θ_i² / g_eff
    T_i  ≈ (m_χ f_a θ_i)^(1/2) × [(3·30)/(16·π²·100)]^(1/4)
         ≈ 0.13 × √(m_χ f_a θ_i)

With DFD's natural keV-scale m_χ and f_a ≈ M_P (the spectral-geometry
decay constant is tied to the internal volume):

    √(m_χ f_a) ≈ √(10⁻⁶ GeV × 10¹⁸ GeV) = √(10¹² GeV²) ≈ 10⁶ GeV

so T_i ≈ 10⁵ GeV. But the DFD spectral cutoff is Λ_cut ≈ 10¹⁶ GeV >> 10⁵ GeV.
**The required initial temperature is off by ~11 orders of magnitude from the
natural DFD cutoff.** Tuning f_a or θ_i to close this gap requires θ_i ≈
10⁻¹¹ or f_a ≈ 10⁻⁴ M_P — neither of which is motivated by the spectral
factorization.

### Dilution chain

Even granting the tuned initial condition, the two components scale
differently with expansion:

    Relativistic era (T > m_b ≈ 1 GeV): ρ_b ∝ a⁻⁴
    χ matter era (T < m_χ ≈ keV):       ρ_χ ∝ a⁻³
    χ relativistic era (T > m_χ):       ρ_χ oscillation has not started; ρ_χ
                                        ≈ (1/2) m_χ² f_a² θ_i² = const (frozen)

From T_i = 10⁵ GeV down to T ≈ m_χ ≈ 1 keV (=10⁻⁶ GeV), a_now/a_i ≈ 10¹¹.
In that interval:

    ρ_χ: frozen → then ~ a⁻³ once H < m_χ, i.e. from T ≈ keV onward
    ρ_b: relativistic (a⁻⁴) from T=10⁵ GeV down to T ≈ 1 GeV, then a⁻³

Relative dilution: ρ_χ/ρ_b picks up a factor (T_b_NR / T_χ_osc)¹ × ... ≈
10⁹ at least. An initial ratio tuned to 16/3 is amplified by ~10⁹ by today,
producing Ω_χ/Ω_b ≈ 5×10⁹, not 16/3. The tuning is unstable to the thermal
history.

The only way to hit 16/3 today is to choose T_i precisely such that the full
dilution chain lands on 16/3 — i.e. T_i is a 1-parameter tuning with no
geometric origin. There is no way to read this number off the spectral
decomposition of CP² × S³.

---

## 5. Where the "16/3" number genuinely lives

H6 and H9 already established that 16/3 = dim(Hilbert_χ)/dim(Hilbert_b) is a
**DOF counting identity** on the internal manifold. The path-integral
derivation I attempted here confirms their conclusion from a different angle:

1. The spectral action produces a V_eff with no χ–matter cross term, so the
   saddle in χ̄ does not know about ρ_b.
2. The saddle in χ̄ is χ̄ = 0 (trivial), so the 16/3 cannot emerge from the
   minimum of V_eff.
3. Any nonzero ρ_χ comes from initial conditions (misalignment), not from
   the path integral saddle, and the initial ratio cannot be predicted
   because it depends on θ_i and T_i, which are UV inputs.
4. Even granting tuned initial conditions, the distinct dilution histories
   of χ and b break any initial ratio by factors of 10⁹⁻¹¹ by today.

**Conclusion: no direct path-integral derivation of Ω_χ/Ω_b = 16/3 exists in
DFD v3.3/v3.4 as formulated.** The ratio 16/3 is a *kinematic* ratio of
internal-manifold DOF counts, which does not map to an *energy-density*
ratio without additional assumptions about initial conditions and thermal
history. Those additional assumptions are not supplied by the spectral
factorization — they are independent tunings.

---

## 6. What would be required to rescue the claim

To promote 16/3 from DOF count to energy-density ratio, DFD would need
(at least) one of:

(a) A genuine V_int(χ̄, ρ̄_matter) cross-term from a sector of S_DFD not yet
    written down, whose minimizer gives χ̄²_min/ρ̄_matter ∝ 16/3 with a
    dimensional factor fixed by M_P, Λ_cut, and nothing else.

(b) A thermal equilibration mechanism that locks ρ_χ/ρ_b to the DOF ratio
    at some epoch T_*, *after* which both scale as a⁻³ (so the ratio is
    preserved). This needs a χ↔b scattering channel active at T_* with rate
    > H(T_*), which is not present in the current DFD Lagrangian.

(c) A late-time attractor in V_eff that drives ρ_χ/ρ_b toward 16/3
    regardless of initial conditions. Again, not present.

Without one of (a)–(c), the claim Ω_χ/Ω_b = 16/3 remains a numerology from
DOF counting, not a derivation from the path integral.

---

## 7. Verdict

**The direct path-integral derivation fails.** The saddle-point calculation
yields ρ_χ = 0 (trivial χ̄) and provides no mechanism to lock ρ_χ/ρ_b to 16/3.
Initial-condition tuning can hit 16/3 *today* only by fine-tuning T_i against
the full dilution chain — a 1-parameter tuning with no geometric origin. The
same obstruction H6 and H9 flagged (DOF ratio ≠ energy-density ratio)
reappears here from the saddle-point angle.

The "16/3" prediction of DFD is, on present evidence, a kinematic coincidence
of internal-manifold dimensions, not a dynamical output of the action.
Status: **not derived**; must be either (i) re-grounded via mechanism
(a), (b), or (c) above, or (ii) downgraded from "prediction" to
"consistency check on DOF assignments."
