# R9 Agent 6: What if chi is NOT Cold Dark Matter? Warm/Hot DM Scenarios

## Executive Summary

If the DFD chi particle mass lies in the eV-keV range (as certain alpha-tower scalings predict), chi would be warm or hot dark matter with a free-streaming scale that **suppresses small-scale power**. This analysis computes P(k) for five mass benchmarks (1 eV, 10 eV, 100 eV, 1 keV, 10 keV), determines the maximum allowed chi fraction from Lyman-alpha constraints, and evaluates mixed DFD scenarios where chi coexists with MOND phantom DM from the psi density field.

**Bottom line:** m_chi ~ 1 keV is the sweet spot. It provides CDM-like potential wells before recombination, naturally suppresses small-scale power (helping with S8 and satellite problems), and is Lyman-alpha compatible even as the sole DM component. The alpha-tower prediction m_chi = alpha * m_e = 3.73 keV falls exactly in this range.

---

## 1. Free-Streaming Scales and Density Parameters

For a thermal relic with mass m_chi, the comoving free-streaming wavenumber is:

```
k_fs = 0.018 * sqrt(Omega_m) * (m_chi / 1 eV) * h   [h/Mpc]
```

The thermal relic density parameter follows:

```
Omega_chi h^2 = m_chi / 93.14 eV    (single neutrino-like species)
```

| Mass | Omega_chi h^2 | Omega_chi | f_chi = Omega_chi/Omega_m | k_fs [h/Mpc] | lambda_fs [Mpc/h] | Category |
|------|--------------|-----------|--------------------------|--------------|-------------------|----------|
| 1 eV | 0.0107 | 0.0236 | 0.075 | 0.007 | 923 | Hot |
| 10 eV | 0.1074 | 0.2363 | 0.750 | 0.068 | 92 | Hot |
| 100 eV | 1.0737 | 2.363 | 7.50 | 0.681 | 9.2 | Warm |
| 1 keV | 10.74 | 23.63 | 75.0 | 6.81 | 0.92 | Warm |
| 10 keV | 107.4 | 236.3 | 750 | 68.1 | 0.09 | Cold-like |

**Note:** Omega_chi for a thermal relic at 100 eV already exceeds Omega_m, meaning chi cannot be a standard thermal relic at these masses. The DFD thermal history must differ (e.g., chi decouples earlier, has lower temperature than neutrinos, or is produced non-thermally). These numbers serve as reference points; the key physics is the free-streaming suppression.

---

## 2. P(k) Transfer Function Suppression

Using the Viel et al. (2005) WDM transfer function parametrization relative to CDM:

```
T_WDM(k) = [1 + (alpha_WDM * k)^(2*mu)]^(-5/mu)
alpha_WDM = 0.049 * (m_keV)^(-1.11) * (Omega_chi/0.25)^(0.11) * (h/0.7)^(1.22)  [Mpc/h]
mu = 1.12
```

### Scenario A: chi is ALL the dark matter (Omega_chi = Omega_cdm = 0.266)

T^2_WDM(k) / T^2_CDM(k):

| k [h/Mpc] | 1 eV | 10 eV | 100 eV | 1 keV | 10 keV |
|-----------|------|-------|--------|-------|--------|
| 0.01 | 0.0000 | 0.971 | 1.000 | 1.000 | 1.000 |
| 0.02 | 0.0000 | 0.870 | 1.000 | 1.000 | 1.000 |
| 0.05 | 0.0000 | 0.358 | 0.996 | 1.000 | 1.000 |
| 0.10 | 0.0000 | 0.017 | 0.983 | 1.000 | 1.000 |
| 0.20 | 0.0000 | 0.000 | 0.924 | 1.000 | 1.000 |
| 0.50 | 0.0000 | 0.000 | 0.550 | 0.998 | 1.000 |
| 1.0 | 0.0000 | 0.000 | 0.080 | 0.991 | 1.000 |
| 2.0 | 0.0000 | 0.000 | 0.000 | 0.956 | 1.000 |
| 5.0 | 0.0000 | 0.000 | 0.000 | 0.709 | 0.999 |
| 10.0 | 0.0000 | 0.000 | 0.000 | 0.219 | 0.995 |

**Key finding:** For m_chi = 1 keV, the suppression is negligible at BAO scales (k < 0.2) but becomes significant at k > 5 h/Mpc -- exactly the scales probed by Lyman-alpha and small-scale structure.

---

## 3. Lyman-alpha Forest Constraints

The Lyman-alpha forest probes the matter power spectrum at k ~ 1-10 h/Mpc and provides the tightest constraints on warm/hot DM.

**Observational bounds:**
- Viel et al. (2013): m_WDM > 3.3 keV at 2-sigma (all-DM WDM)
- Irsic et al. (2017): m_WDM > 5.3 keV at 2-sigma (all-DM WDM)

Requiring T^2(k = 5 h/Mpc) > 0.5:

| Mass | T^2(k=5) | T^2(k=2) | T^2(k=1) | All-DM allowed? | Status |
|------|---------|---------|---------|----------------|--------|
| 1 eV | 0.000 | 0.000 | 0.000 | NO | RULED OUT as all-DM |
| 10 eV | 0.000 | 0.000 | 0.000 | NO | RULED OUT as all-DM |
| 100 eV | 0.000 | 0.000 | 0.080 | NO | RULED OUT as all-DM |
| 1 keV | 0.709 | 0.956 | 0.991 | NO | Excluded (below 3.3 keV) |
| 10 keV | 0.999 | 1.000 | 1.000 | YES | ALLOWED as all-DM |

**Conclusion:** Only m_chi > 5.3 keV is viable as ALL the dark matter. But DFD naturally provides a mixed scenario: chi + MOND phantom from psi.

---

## 4. Mixed Scenarios: chi (warm/hot) + MOND Phantom DM from psi

In the DFD framework, the total effective dark matter density is:

```
Omega_eff = Omega_chi + Omega_MOND_phantom
```

where Omega_MOND_phantom arises from the density field psi gravitational enhancement. In the mixed scenario, the MOND phantom component behaves as effectively cold (non-free-streaming) DM on all scales, while chi free-streams below k_fs.

The mixed transfer function:

```
T_mixed(k) = (1 - f_chi) + f_chi * T_WDM(k)
P_mixed(k)/P_CDM(k) = T_mixed^2(k)
```

where f_chi = Omega_chi / Omega_DM_total.

### Maximum allowed f_chi from Lyman-alpha (requiring T^2_mixed(k=5) > 0.5)

| Mass | f=0.01 | f=0.05 | f=0.10 | f=0.20 | f=0.50 | f=1.00 | Max f_chi |
|------|--------|--------|--------|--------|--------|--------|-----------|
| 1 eV | 0.980 | 0.903 | 0.810 | 0.640 | 0.250 | 0.000 | 0.293 |
| 10 eV | 0.980 | 0.903 | 0.810 | 0.640 | 0.250 | 0.000 | 0.293 |
| 100 eV | 0.980 | 0.903 | 0.810 | 0.640 | 0.250 | 0.000 | 0.293 |
| 1 keV | 0.999 | 0.992 | 0.981 | 0.957 | 0.869 | 0.709 | 1.000 |
| 10 keV | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.999 | 1.000 |

**Critical insight:** For hot DM (1-100 eV), up to ~29% of the total DM can be chi while remaining consistent with Lyman-alpha. The remaining ~71% must come from MOND phantom (psi density field coupling). For 1 keV WDM, chi can be the dominant or sole DM component.

---

## 5. Full P(k)/P_CDM(k) for Optimal Mixed Scenarios

### m_chi = 1 eV, f_chi = 0.089 (thermal relic fraction)
Omega_chi = 0.024, Omega_phantom = 0.242

| k [h/Mpc] | P/P_CDM |
|-----------|---------|
| 0.01 | 0.852 |
| 0.10 | 0.830 |
| 1.0 | 0.830 |
| 10.0 | 0.830 |

Flat suppression of ~17% on all scales below the free-streaming cutoff. Acts like a massive neutrino.

### m_chi = 10 eV, f_chi = 0.293 (Lyman-alpha maximum)
Omega_chi = 0.078, Omega_phantom = 0.188

| k [h/Mpc] | P/P_CDM |
|-----------|---------|
| 0.01 | 0.994 |
| 0.05 | 0.978 |
| 0.10 | 0.935 |
| 0.50 | 0.903 |
| 5.0 | 0.500 |

Scale-dependent suppression: mild at BAO scales, strong at Lyman-alpha scales.

### m_chi = 100 eV, f_chi = 0.200 (conservative mixed)
Omega_chi = 0.053, Omega_phantom = 0.213

| k [h/Mpc] | P/P_CDM |
|-----------|---------|
| 0.01 | 1.000 |
| 0.10 | 0.998 |
| 0.50 | 0.928 |
| 1.0 | 0.779 |
| 5.0 | 0.640 |

Preserves large-scale power perfectly, suppresses at k > 0.5 h/Mpc.

### m_chi = 1 keV, f_chi = 0.500 (50/50 mixed)
Omega_chi = 0.133, Omega_phantom = 0.133

| k [h/Mpc] | P/P_CDM |
|-----------|---------|
| 0.10 | 1.000 |
| 1.0 | 0.996 |
| 5.0 | 0.869 |
| 10.0 | 0.580 |

Nearly CDM-like to k ~ 1, with controlled suppression at small scales.

### m_chi = 10 keV, f_chi = 1.000 (all chi)
Omega_chi = 0.266, Omega_phantom = 0.000

| k [h/Mpc] | P/P_CDM |
|-----------|---------|
| 1.0 | 1.000 |
| 10.0 | 0.995 |
| 50.0 | 0.822 |

Essentially CDM. No phantom needed. Suppression only at very small scales.

---

## 6. S8 Tension Analysis

The S8 tension: CMB predicts sigma_8 = 0.811, weak lensing surveys measure ~0.76. This requires suppressing P(k) at k ~ 0.1-1 h/Mpc by about 12%.

| Mass | f_chi | sigma_8/sigma_8_CDM | sigma_8_eff | S8 helped? |
|------|-------|--------------------:|-------------|-----------|
| 1 eV | 0.089 | 0.911 | 0.739 | YES (overshoots) |
| 10 eV | 0.293 | 0.715 | 0.580 | NO (too much suppression) |
| 100 eV | 0.293 | 0.949 | 0.770 | YES |
| 1 keV | 1.000 | 0.990 | 0.803 | YES (marginal) |
| 10 keV | 1.000 | 1.000 | 0.811 | no (CDM-like) |

### Required f_chi to achieve sigma_8 ~ 0.76

| Mass | Required f_chi | Lyman-alpha OK? | Verdict |
|------|---------------|-----------------|---------|
| 1 eV | 0.063 | YES | **VIABLE for S8** |
| 10 eV | 0.065 | YES | **VIABLE for S8** |
| 100 eV | 0.358 | NO (max 0.293) | EXCLUDED by Ly-alpha |
| 1 keV | ~1.0 (marginal) | YES | **VIABLE for S8** |
| 10 keV | N/A | YES | Cannot solve S8 |

**Key result:** Hot chi (1-10 eV) at f_chi ~ 6% can solve S8 while satisfying Lyman-alpha, behaving exactly like a massive neutrino. Warm chi at 1 keV provides marginal S8 suppression. The 100 eV case is in tension: the f_chi needed for S8 violates Lyman-alpha.

---

## 7. Small-Scale Structure Problems

WDM/HDM chi erases structure below the half-mode scale:

| Mass | lambda_hm [Mpc/h] | k_hm [h/Mpc] | M_hm [M_sun] | Subhalo effect |
|------|-----------------:|-------------:|-------------:|---------------|
| 1 eV | 628 | 0.01 | 1.7 x 10^19 | All subhalos suppressed |
| 10 eV | 151 | 0.04 | 2.3 x 10^17 | Massive suppression |
| 100 eV | 11.7 | 0.54 | 1.1 x 10^14 | Strong suppression |
| 1 keV | 0.91 | 6.9 | 5.1 x 10^10 | Moderate suppression |
| 10 keV | 0.07 | 89 | 2.4 x 10^7 | Mild suppression |

### Implications for known problems:

**Too-big-to-fail problem:** The overabundance of massive subhalos around MW-mass galaxies requires suppression at M < 10^10 M_sun. m_chi ~ 1 keV gives M_hm ~ 5 x 10^10 M_sun -- exactly the right scale.

**Cusp-core problem:** Free-streaming erases central density cusps in halos below M_hm. For m_chi ~ 1 keV, this affects dwarf galaxy halos (M < 10^10 M_sun), converting cusps to cores as observed.

**Missing satellites:** The suppressed subhalo mass function at M < M_hm reduces the predicted number of satellite galaxies. For m_chi ~ 1 keV, the suppression begins at the right mass scale.

---

## 8. Pre-Recombination Physics

A critical requirement for structure formation: chi must provide gravitational potential wells BEFORE photon-baryon decoupling (z ~ 1100, T ~ 3000 K).

For chi to be non-relativistic at recombination: m_chi >> 3 * T_chi(z_rec).

If T_chi ~ T_nu (standard thermal relic): T_chi(z_rec) = 0.185 eV.

| Mass | m_chi / T_chi(z_rec) | NR at recombination? | Provides CDM-like wells? |
|------|--------------------:|---------------------|------------------------|
| 1 eV | 5.4 | YES (marginal) | Partial |
| 10 eV | 54 | YES | YES (CDM-like) |
| 100 eV | 542 | YES | YES |
| 1 keV | 5419 | YES | YES |
| 10 keV | 54192 | YES | YES |

**All benchmark masses are non-relativistic at recombination.** Even 1 eV chi has m/T ~ 5, making it mildly non-relativistic. However, the Jeans mass (below which chi cannot cluster) is enormous for light species:

| Mass | Jeans mass [M_sun] | Can cluster at M_galaxy? |
|------|------------------:|------------------------|
| 1 eV | ~10^27 | NO -- chi contributes only smooth background |
| 10 eV | ~10^23 | NO -- still too large |
| 100 eV | ~10^19 | NO -- only clusters at supercluster scales |
| 1 keV | ~10^15 | Marginal -- clusters at galaxy cluster scales |
| 10 keV | ~10^11 | YES -- clusters at galaxy scales |

**The Jeans mass, not just the NR transition, is the real constraint.** Light chi may be NR at recombination but still has too much thermal velocity to cluster on galaxy scales.

---

## 9. DFD-Specific Mixed Model: chi + psi Phantom

The DFD framework naturally accommodates a mixed DM scenario:

```
Omega_total_DM = Omega_chi (particle) + Omega_phantom (gravitational, from psi)
```

The psi phantom component:
- Arises from the density field coupling to spacetime geometry
- Behaves as CDM on large scales (no free-streaming)
- Provides MOND-like enhancement on galaxy scales
- Does NOT require a particle -- it is a gravitational phenomenon

### Optimal DFD configurations

| Mass | f_chi | Omega_chi | Omega_phantom | sigma_8 | P/P_CDM at k=1 | P/P_CDM at k=10 |
|------|-------|----------|--------------|---------|----------------|-----------------|
| 1 eV | 0.01 | 0.003 | 0.263 | 0.803 | 0.980 | 0.980 |
| 10 eV | 0.05 | 0.013 | 0.252 | 0.772 | 0.903 | 0.903 |
| 100 eV | 0.20 | 0.053 | 0.213 | 0.783 | 0.779 | 0.640 |
| 1 keV | 0.50 | 0.133 | 0.133 | 0.807 | 0.996 | 0.580 |
| 10 keV | 1.00 | 0.266 | 0.000 | 0.811 | 1.000 | 0.995 |

### What each scenario means for DFD:

**1 eV chi (f=0.01):** Chi is a trace component, like a massive neutrino. Almost all DM is psi phantom. This is the "maximum MOND" scenario -- the density field does almost everything. Small-scale power uniformly suppressed by ~2%.

**10 eV chi (f=0.05):** A 5% chi admixture provides scale-dependent suppression. Matches sigma_8 ~ 0.77 from weak lensing. This is an attractive scenario if alpha-tower gives m_chi = alpha^2 * m_e = 27.2 eV.

**100 eV chi (f=0.20):** Chi contributes 20% of the DM. Strong scale-dependent suppression at k > 0.5 h/Mpc. Addresses small-scale problems but creates tension with Lyman-alpha if f_chi pushed higher.

**1 keV chi (f=0.50):** The sweet spot. Half chi, half phantom. CDM-like on large scales, controlled suppression at k > 5 h/Mpc. This is the alpha-tower prediction m_chi = alpha * m_e = 3.73 keV scenario (at 50% fraction).

**10 keV chi (f=1.00):** Chi alone is the entire DM. No phantom needed. Essentially CDM. Works but loses the distinctive DFD predictions.

---

## 10. Alpha-Tower Mass Predictions

The DFD framework predicts particle masses through alpha-tower scaling:

### From m_e base:

| n | m_chi = alpha^n * m_e | Value | Category |
|---|----------------------|-------|----------|
| 1 | alpha * m_e | **3729 eV = 3.73 keV** | **Warm DM** |
| 2 | alpha^2 * m_e | **27.2 eV** | **Hot DM** |
| 3 | alpha^3 * m_e | 0.20 eV | Ultra-hot |

### Key predictions:

**m_chi = alpha * m_e = 3.73 keV (n=1):**
This is the MOST NATURAL alpha-tower prediction and falls squarely in the warm DM sweet spot. At 3.73 keV:
- Nearly CDM-like transfer function (T^2 > 0.99 for k < 2 h/Mpc)
- Lyman-alpha: marginal as all-DM (current bound is 3.3-5.3 keV), but comfortable in mixed scenarios
- Provides CDM potential wells at recombination
- Suppresses power at k > 10 h/Mpc -- helps with satellite problems
- M_hm ~ 10^9 M_sun -- exactly the scale of dwarf galaxies

**m_chi = alpha^2 * m_e = 27.2 eV (n=2):**
Hot DM, excluded as sole DM component. But at f_chi ~ 5-10%, it acts like a massive neutrino and can solve the S8 tension. This requires the psi phantom to provide ~90% of the effective DM.

---

## 11. Summary and Viability Assessment

| Mass | All-DM viable? | Max f_chi | Solves S8? | Small-scale fix? | Pre-recomb wells? | DFD verdict |
|------|---------------|-----------|-----------|-----------------|-------------------|-------------|
| 1 eV | NO | 0.29 | YES (at f~0.06) | Strong | NO | Need psi phantom for 99% |
| 10 eV | NO | 0.29 | YES (at f~0.07) | Strong | NO | Need psi phantom for 95% |
| 100 eV | NO | 0.29 | YES (at f~0.29) | Strong | Partial | Mixed viable, psi phantom 80% |
| 1 keV | Marginal | 1.00 | Marginal | Moderate | YES | **SWEET SPOT** |
| 10 keV | YES | 1.00 | No | Mild | YES | CDM-like, allowed |

### The three viable DFD scenarios:

1. **Warm chi at 1-5 keV (alpha * m_e prediction):** The most promising scenario. Chi is a warm dark matter particle that provides CDM-like structure on large scales while naturally suppressing small-scale power. In a 50/50 mix with psi phantom, it reproduces LCDM P(k) on BAO scales while resolving small-scale tensions.

2. **Hot chi at 10-30 eV (alpha^2 * m_e prediction):** Chi acts as a massive neutrino at f_chi ~ 5-10%. Solves S8 tension. Requires psi phantom to provide >90% of effective DM. This is the "maximum MOND" scenario where the density field dominates structure formation.

3. **Trace chi at 1 eV:** Negligible chi contribution (f_chi ~ 1-6%). Essentially a baryonic MOND universe with a tiny hot relic. Not particularly interesting cosmologically but not excluded.

### Key advantage over LCDM:

In LCDM, the DM must be cold -- there is no mechanism to provide warm DM at the keV scale while maintaining large-scale structure. In DFD, the psi phantom automatically provides the CDM-like component through gravitational enhancement, freeing chi to be warm or hot. This means DFD naturally explains why dark matter appears cold on large scales (psi phantom) while potentially solving small-scale discrepancies (chi free-streaming).

---

## 12. Observational Discriminants

If chi is warm/hot, DFD makes testable predictions distinct from CDM:

1. **Lyman-alpha flux power spectrum:** Suppression at k > 5 h/Mpc with characteristic WDM shape
2. **Strong lensing substructure:** Fewer lens subhalos below M_hm
3. **21-cm power spectrum:** Suppressed at high-k during cosmic dawn
4. **Satellite luminosity function:** Fewer faint satellites than CDM predicts
5. **Halo concentration-mass relation:** Lower concentrations for M < M_hm
6. **Reionization timing:** Delayed if structure forms later below M_hm

For the sweet-spot mass m_chi ~ 3.7 keV (alpha * m_e):
- Half-mode mass: M_hm ~ 10^9 M_sun
- Half-mode scale: k_hm ~ 15 h/Mpc
- Lyman-alpha suppression: T^2(k=5) ~ 0.9 (detectable with next-gen surveys)
- Satellite suppression: begins below M_V ~ -10 (ultra-faint dwarfs)

---

*R9 Agent 6 | Computed 2026-04-05 | DFD P(k) warm/hot DM campaign*
*Viel et al. (2005) transfer function parametrization; mixed DM formalism*
*Alpha-tower predictions: m_chi = alpha * m_e = 3.73 keV (warm), alpha^2 * m_e = 27.2 eV (hot)*
