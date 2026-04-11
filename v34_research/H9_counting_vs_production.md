# H9: Spectral-Trace Counting vs. Production Mechanism

**Issue #9:** DFD's 16/3 ratio (Ω_χ/Ω_b) is derived from counting degrees of freedom in the spectral trace factorization. Counting is not a production mechanism. This note asks whether any physical process — inflation, reheating, phase transitions — actually delivers 16/3 as a dynamical outcome.

**Bottom line:** The standard reheating calculation does NOT produce 16/3. The ratio is a counting argument in search of a mechanism.

---

## Step 1 — Initial condition at the spectral cutoff

At T ~ M_P, the spectral trace factorizes the total action into a χ sector (16 DOF) and a baryon sector (3 DOF). The claim is:

    ρ_χ / ρ_b |_{T = M_P}  =  16 / 3

with absolute normalization set by the Friedmann constraint

    ρ_total  =  (3 / 8πG) · H²    at    T ~ M_P.

This is an *initial condition*, not a production mechanism. It asserts a partition of the cutoff-scale energy density without specifying how that partition survives the cosmological evolution that follows.

---

## Step 2 — Inflation erases the initial condition

DFD uses Starobinsky (R²) inflation with N ≈ 60 e-folds. Any pre-existing energy density at T ~ M_P is diluted by

    a_end / a_start  =  e^{60}    ⇒    ρ_pre / ρ_infl  ~  e^{-3·60}  ≈  10^{-78}.

Whatever 16:3 partition existed at the cutoff is diluted to cosmological irrelevance by the end of inflation. The post-inflationary universe is populated entirely by inflaton decay products. The real question is therefore:

> **Does reheating produce Ω_χ / Ω_b = 16/3?**

Not "is the initial condition preserved." The initial condition is gone.

---

## Step 3 — Scalaron reheating in DFD

The Starobinsky scalaron has mass m_s ≈ 3 × 10^{13} GeV (taking the canonical value; the argument is insensitive to this). It couples to all matter species gravitationally through the trace of the stress-energy tensor, with characteristic decay width

    Γ(scalaron → X X̄)  ~  m_s³ / M_P².

Key features of gravitational scalaron decay:

1. **Democratic at the gravitational scale.** The coupling is universal; each species gets a rate that differs only by mass-threshold factors and a small DOF prefactor.
2. **Kinematically open to χ.** m_s ≈ 10^{13} GeV ≫ 2 m_χ ≈ 2 × 96 keV, so χ pair production is allowed.
3. **Branching ratio per channel.**

       Γ(scalaron → χχ) / Γ_total  ≈  g_χ / g_*(T_RH)

   where g_*(T_RH) ≈ 106.75 is the SM relativistic count. With g_χ = 1 (complex scalar) or 2, χ receives at most ~1–2% of the inflaton energy.

So reheating gives

    (ρ_χ / ρ_b)_{RH}  ~  O(10^{-2}),   not   16/3 ≈ 5.33.

The discrepancy is three orders of magnitude in the wrong direction.

---

## Step 4 — What thermal equilibrium would require

Suppose (counterfactually) that χ and baryons thermalized at T_RH. Number densities of relativistic species are

    n_i  =  (ζ(3)/π²) · g_i · T_RH³,

so the mass-weighted ratio is

    (n_χ m_χ) / (n_b m_b)  =  (g_χ / g_b) · (m_χ / m_b).

Setting this to 16/3 and using m_χ = 96 keV, m_b = m_p = 938 MeV:

    g_χ / g_b  =  (16/3) · (m_b / m_χ)
               =  (16/3) · (9.38 × 10^8 eV) / (9.6 × 10^4 eV)
               =  (16/3) · 9771
               ≈  5.21 × 10^4.

A DOF ratio of ~5 × 10^4 is unphysical. **DFD's 16/3 cannot be a thermal-equilibrium ratio** — neither at reheating, nor at any later epoch where both sectors would be relativistic.

---

## Step 5 — Non-thermal rescue attempts

The counting argument can only survive if the χ abundance is set non-thermally. Candidate mechanisms:

### (a) Branching-ratio fine-tuning

For scalaron decay to deliver 16/3 directly, we would need

    BR(scalaron → χχ)  =  16/19 ≈ 0.842,
    BR(scalaron → SM)   =   3/19 ≈ 0.158.

Gravitational decay of the Starobinsky scalaron is democratic in g_* and does not produce an 84%/16% split. There is no identified coupling that would give χ an ~85% branching fraction against the entire Standard Model.

### (b) Spectral-trace-weighted decay

One could *postulate* that the scalaron decay rate is weighted by the spectral trace, i.e. by the DFD action rather than by SM gauge couplings. This is the mechanism implicit in the DFD literature. But the Starobinsky scalaron is the R² mode — its coupling to matter is the gravitational trace coupling, which is blind to the DFD spectral weighting. There is no derivation connecting the spectral trace to the scalaron's decay amplitude.

### (c) Democratic gravitational decay, counted honestly

If we count decay channels by spin and multiplicity under a universal gravitational coupling:

    Fermion channels  : 3 generations × 16 Weyl DOF ≈ 48
    Scalar χ          : 1 (or 2 for complex)

This gives

    BR(χ)  ≈  1 / 49    and    n_χ / n_b  ≈  1/(49 · 3)  ≈  1/147,

which is the *opposite* of 16/3. Democratic gravitational reheating suppresses χ relative to baryons.

### (d) Freeze-in at sub-reheating scales

A Planck-suppressed operator (1/M_P² × χ² × SM) gives a freeze-in yield

    Y_χ  ~  T_RH³ / M_P² · t_H  ~  (T_RH / M_P),

which depends linearly on T_RH and has no reason to land on 16/3.

### (e) Production at the spectral scale, protected from dilution

This is the only logically consistent rescue: χ is produced at T ~ M_P (above the inflationary scale) and its energy density is *not* diluted by inflation because it is somehow locked into the spectral structure of spacetime itself. But this requires abandoning the standard cosmological timeline — χ becomes a geometric background mode, not a particle species, and one must then re-derive that this background reproduces cold dark matter phenomenology (P(k), halo formation, free streaming). This is precisely the program that the separate P(k) closure work is grappling with.

---

## Step 6 — Honest conclusion

The 16/3 ratio is a **counting argument without a production mechanism**. Specifically:

1. The spectral-trace factorization fixes an *initial condition* at T ~ M_P.
2. Inflation dilutes that initial condition to zero.
3. Starobinsky reheating repopulates the universe democratically across SM species, giving χ at most ~1–2% of ρ, not 84%.
4. Thermal equilibrium cannot deliver 16/3 either; the required DOF ratio is ~5 × 10^4.
5. No known branching mechanism assigns χ an ~85% branching fraction of scalaron decay.
6. Democratic gravitational decay pushes the ratio in the wrong direction (χ suppressed, not enhanced).

The claim "gravitational freeze-in preserves 16/3" is not supported by the calculation. DFD currently has three live options:

- **(a) Find the subtle mechanism.** A concrete derivation showing that some physical process (scalaron decay, phase-transition preheating, gravitational particle production, etc.) delivers Ω_χ / Ω_b = 16/3 at percent-level accuracy. No such derivation exists in the current DFD literature.

- **(b) Concede numerological coincidence.** Accept that 16/3 matches the observed Ω_dm / Ω_b ≈ 5.36 to ~1%, but is a post-hoc DOF count without dynamical backing. This weakens the claim from "prediction" to "consistency check."

- **(c) Commit to geometric, non-particle χ.** Treat χ not as a reheated species but as a spectral/geometric mode whose energy density is defined at the cutoff and survives by being part of the background geometry itself. This is philosophically clean but requires a full re-derivation of structure formation observables (P(k), N_eff, BAO, CMB damping) from the geometric framework — it does NOT automatically reproduce CDM phenomenology.

**Recommendation.** The DFD manuscript should stop claiming 16/3 as a derived dark matter abundance until one of (a), (b), or (c) is worked out explicitly. Option (c) is the most consistent with DFD's broader "geometry is primary" stance, but it promotes Ω_dm / Ω_b = 16/3 from "particle-physics prediction" to "geometric postulate" — and the honest write-up should say so.

---

## Numerical appendix

- Observed ratio (Planck 2018):  Ω_dm / Ω_b  =  0.265 / 0.0493  ≈  5.375
- DFD counting:                   16 / 3      ≈  5.333
- Agreement:                      ≈  0.8%

- Scalaron mass:                  m_s  ≈  3 × 10^{13} GeV
- χ mass (DFD):                   m_χ  ≈  96 keV
- Reheating temperature:          T_RH ≈  10^9 – 10^{12} GeV  (model-dependent)
- g_*(T_RH):                      ≈  106.75  (SM only)

- Required thermal DOF ratio:     g_χ / g_b  ≈  5.2 × 10^4   (unphysical)
- Gravitational democratic BR:    BR(χ)      ≈  1 / g_*      (~1%, not 84%)
- Required scalaron BR:           BR(χ)      =  16/19 ≈ 84%   (no mechanism)

The gap between "counting gives 16/3" and "reheating gives 16/3" is three orders of magnitude. It must be closed or conceded.
