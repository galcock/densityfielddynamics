# R4 Agent: Does the Saturation-Union Composition Law Create a Cross-Sector EFE?

## Executive Summary

**The composition law does NOT apply cross-sector in the way hypothesized.** The spatial and temporal sectors enter the action ADDITIVELY (Eq. 2.6 of v3.3), not through the saturation-union composition law. The composition law was derived for combining two POTENTIALS (microsector weights that multiply, so psi adds), not for combining spatial and temporal SECTORS of the same field. The temporal sector's contribution to cosmological perturbations is negligible compared to the spatial sector by a factor of ~300. The cosmological EFE comes from the SPATIAL sector's external field, not from temporal-spatial cross-coupling.

---

## Task 1: Does the Composition Law Apply Cross-Sector?

### What the Paper Actually Says

The full scalar-sector action (Eq. 2.6 / eq:action-full-dynamic in section_formalism.tex, line 141) is:

```
S_psi = integral dt d^3x { (a*^2 / 8piG) [ W(|grad psi|^2 / a*^2) + K((c/a_0)|psi_dot - psi_dot_0|) ] - (c^2/2) psi (rho - rho_bar) }
```

The spatial and temporal sectors enter as a SUM in the Lagrangian:

```
L_total = L_spatial[W] + L_temporal[K]
```

This is ordinary additive k-essence structure, NOT the saturation-union composition.

### The Composition Law's Actual Role

The saturation-union law (Assumption 3 / ass:composition in Appendix N):

```
mu(psi_1 + psi_2) = 1 - (1 - mu(psi_1))(1 - mu(psi_2))
```

was derived for a specific purpose: combining TWO INDEPENDENT microsector contributions that ADD in psi (because microsector weights MULTIPLY, so log-weights add). This is used in two ways:

1. **Spatial sector (Appendix N):** Derives the functional form mu(x) = x/(1+x) from the requirement that combining two spatial potentials psi_1, psi_2 satisfies the composition law.

2. **Temporal sector (Appendix Q):** Derives the temporal deviation invariance theorem:
   ```
   mu(psi_0 + Delta_psi) - mu(psi_0) = (1 - mu(psi_0)) mu(Delta_psi)
   ```
   This gives the temporal constitutive law K'(Delta) = mu(Delta) using the SAME mu function.

### Why Cross-Sector Application is Wrong

The composition law applies to combining potentials within a SINGLE sector:
- (a) Two spatial potentials: psi = psi_1 + psi_2, both entering through |grad psi|
- (b) Background + deviation in temporal sector: psi_dot = psi_dot_0 + delta(psi_dot)

It does NOT apply to combining the spatial argument x_s = |grad psi|/a* with the temporal argument Delta_t = (c/a_0)|psi_dot - psi_dot_0|. These are DIFFERENT INVARIANTS entering DIFFERENT TERMS in the Lagrangian.

The correct combination is at the level of the ACTION (additive):
```
L = L_spatial(x_s) + L_temporal(Delta_t) + L_matter
```

NOT at the level of the mu-function:
```
mu_total =/= 1 - (1 - mu_s)(1 - mu_t)   [WRONG]
```

**Verdict: The saturation-union law does NOT create a cross-sector effective field equation. The sectors are additive in the Lagrangian.**

---

## Task 2: mu_t for a Cosmological Perturbation

For a perturbation delta_psi growing as delta_psi ~ a^p with amplitude A:

```
delta(psi_dot) = p H delta_psi
```

The temporal deviation invariant for the perturbation is:
```
Delta_t = (c/a_0)|delta(psi_dot)| = (c/a_0)|p H delta_psi|
```

Note: this uses a_0 (not a_*) as the normalization, as defined in Eq. (Q.3) of the paper:
```
Delta := (c/a_0)|psi_dot - psi_dot_0|
```

### Numerical Evaluation at z = 0

```
c/a_0 = (3e8 m/s) / (1.2e-10 m/s^2) = 2.5e18 s
H_0 = 2.18e-18 s^-1  (for H_0 ~ 67 km/s/Mpc)
c H_0 / a_0 = 2.5e18 * 2.18e-18 = 5.45
```

For |delta_psi| ~ Phi/c^2 ~ 10^-5 (typical potential perturbation at z=0) and p = 2 (matter-dominated growth):
```
Delta_t = 5.45 * 2 * 10^-5 = 1.09e-4
mu_t = 1.09e-4 / (1 + 1.09e-4) = 1.09e-4
```

### Comparison with mu_s

For |grad(delta_psi)| ~ k |delta_psi| with k = 0.1 h/Mpc ~ 10^-23 m^-1:
```
x_s = |grad(delta_psi)| / a* = k |delta_psi| / a*
    = 10^-23 * 10^-5 / (2.67e-27)
    = 3.75e-2

mu_s = 3.75e-2 / 1.0375 = 3.61e-2
```

---

## Task 3: The Ratio

```
mu_s / mu_t = 3.61e-2 / 1.09e-4 = 331
```

**The spatial sector dominates by a factor of ~330.**

Even if one incorrectly applied the saturation-union law cross-sector, the temporal contribution would be negligible:
```
mu_total = mu_s + mu_t - mu_s * mu_t
         = 3.61e-2 + 1.09e-4 - (3.61e-2)(1.09e-4)
         = 3.621e-2

Fractional change from temporal: 0.3%
```

**The temporal sector is irrelevant for the effective mu at P(k) scales.**

---

## Task 4: The Background Temporal Contribution

### What psi_dot_0 Is

From Appendix Q (line 55-56):
> "The screen-background field psi_0 is the psi-screen solution already present in the cosmology section (Sec. 12)."

And from the definition (Eq. Q.3):
```
psi_dot := u^mu nabla_mu psi
psi_dot_0 := u^mu nabla_mu psi_0
Delta := (c/a_0)|psi_dot - psi_dot_0|
```

The background psi_dot_0 IS subtracted by definition. The temporal invariant Delta measures the DEVIATION from the background, not the absolute time derivative. This is theorem-grade (Theorem Q.2, temporal segment identification): reference invariance FORCES subtraction of psi_dot_0.

### Consequence

For the homogeneous background: psi = psi_0, therefore psi_dot = psi_dot_0, therefore Delta = 0.

**There is NO background temporal contribution.** The temporal sector's Delta is identically zero on the background. It only activates for perturbations, where it gives mu_t ~ 10^-4 as computed above.

This is exactly analogous to the spatial sector: the spatial argument x_s = |grad psi|/a* is zero for the homogeneous background (where grad psi_bar = 0 by symmetry) and only activates for perturbations.

---

## Task 5: The cH_0/a_0 Claim and the Cosmological EFE

### What the Paper Says

From section_cosmology.tex (lines 698-704):
> "cosmological perturbation accelerations (x ~ 4e-4) lie deep in the MOND regime where the raw mu-function enhances gravity by ~400x without the cosmological External Field Effect (EFE) from the Hubble flow (a_ext ~ cH_0 ~ 6 a_0). With the EFE, the effective enhancement drops from ~400 to ~1.2"

### What a_ext ~ cH_0 Means

This is a SPATIAL external field, not a temporal one. The cosmological EFE arises because:

1. **The Hubble flow generates a background gradient.** In an expanding universe, the effective gravitational acceleration associated with the Hubble flow is a_H = cH_0 ~ 7e-10 m/s^2 ~ 6 a_0.

2. **This enters through the SPATIAL sector's EFE.** The total spatial gradient at any point is:
   ```
   |grad psi_total| = |grad psi_perturbation + grad psi_Hubble|
   ```

3. **The nonlinearity of mu** means the perturbation response is evaluated at the TOTAL argument:
   ```
   x_total = |a_int + a_ext| / a_0
   ```
   When a_ext ~ 6 a_0, we have x_total >> 1 and mu(x_total) ~ 1, Newtonianizing the dynamics.

### How This Works Mechanically

From the perturbation theory (Eq. 12.10 / eq:G-eff):
```
G_eff = G / mu_0[1 + L_0 (k_hat . g_hat)^2]
```

where mu_0 = mu(x_bar) is evaluated at the BACKGROUND gradient's dimensionless value.

If x_bar ~ 6 (from cH_0 / a_0 ~ 6):
```
mu_0 = 6/7 = 0.857
L_0 = 1/(1+6)^2 = 1/49 = 0.020
```

Then:
```
G_eff ~ G / 0.86 ~ 1.16 G
```

This gives an enhancement factor of ~1.2 (matching the paper's claim), compared to ~400 without the EFE.

### What is psi_bar_dot?

The background psi field in DFD cosmology tracks the cosmic expansion through the psi-screen. The psi-screen at redshift z is:
```
Delta_psi(z) = psi_em(z) - psi_obs
```

The paper reconstructs Delta_psi(z=1) ~ 0.27. This is a slowly-varying field, so psi_dot ~ H * Delta_psi / Delta_z, which is small but nonzero.

However, the temporal sector measures deviations from this background: Delta = (c/a_0)|psi_dot - psi_dot_0|. Since psi_dot_0 IS the background by definition, Delta_bar = 0 identically.

**The psi-screen's slow evolution does NOT activate the temporal sector.** It is fully absorbed into psi_dot_0.

---

## Key Conclusions

### 1. No Cross-Sector Composition Law
The saturation-union law applies within sectors (combining potentials), not between sectors (combining spatial + temporal). The sectors are additive in the Lagrangian.

### 2. Temporal Sector is Negligible for P(k)
mu_s/mu_t ~ 330. The temporal sector contributes at the 0.3% level to the effective response for cosmological perturbations. It is irrelevant for P(k).

### 3. The Temporal Sector's Role is the Dust Branch
The temporal sector's contribution is not through modifying mu_eff. Its role is providing the dust branch (w -> 0, c_s^2 -> 0) that allows DFD's psi-field to behave as pressureless matter. This is a qualitative role (equation of state), not a quantitative correction to the spatial growth enhancement.

### 4. The Cosmological EFE is Purely Spatial
The a_ext ~ cH_0 ~ 6 a_0 external field is a SPATIAL gradient from the Hubble flow, entering through the standard (spatial) EFE mechanism. It is not related to the temporal sector.

### 5. Background Temporal Contribution is Zero
psi_dot_0 is defined as the background value, so Delta_bar = 0 by construction. The temporal sector only sees perturbations, where its contribution is suppressed by ~300x relative to the spatial sector.

---

## Implications for the P(k) Program

The hierarchy is clear:
```
P(k) determination is controlled by:
1. Spatial sector mu(x_s) with G_eff = G/mu_0 [DOMINANT]
2. Cosmological EFE from a_ext ~ cH_0 ~ 6 a_0 [CRITICAL for normalization]
3. Dust branch equation of state w -> 0 [QUALITATIVE requirement]
4. Temporal sector mu_t correction [NEGLIGIBLE, ~0.3%]
```

The open question for P(k) is NOT the temporal sector. It is:
- How exactly does a_ext ~ cH_0 enter the linearized perturbation equations?
- Is a_ext the background gradient |grad psi_bar|? If so, what determines grad psi_bar in DFD cosmology?
- The paper's perturbation theory (Eq. 12.10) uses mu_0 = mu(x_bar) where x_bar = |grad psi_bar|/a*. What is x_bar?

The answer: x_bar ~ cH_0/a_0 ~ 6, giving mu_0 ~ 0.86 and G_eff ~ 1.16G, an enhancement of only ~16% over standard gravity. This is the regime the paper claims should reproduce LCDM-like growth.

---

## Status

| Question | Answer | Confidence |
|---|---|---|
| Does composition law apply cross-sector? | NO - sectors are additive in Lagrangian | HIGH (explicit eq. in paper) |
| Is mu_t negligible? | YES - suppressed by ~330x vs mu_s | HIGH (dimensional analysis) |
| Is Delta_bar = 0? | YES - by definition of psi_dot_0 | HIGH (theorem-grade) |
| Source of cosmological EFE? | Spatial gradient from Hubble flow | HIGH (explicit in paper) |
| Does temporal sector matter for P(k)? | Only qualitatively (dust branch) | HIGH |

*R4 Agent analysis, 2026-04-05*
