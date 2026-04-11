# R9 Agent 12: What Expansion History H(z) Does v3.3 Actually Use?

## Status: CRITICAL FINDING -- The expansion history is NEVER independently derived

---

## Executive Summary

The v3.3 paper **never writes down a Friedmann equation**. It never derives H(z) from DFD principles. Instead, it **explicitly takes H(a) from the LCDM observer dictionary** and treats it as a reporting-layer input. The paper's strategy is to reinterpret what observers see through the psi-screen, not to provide an alternative expansion history. This creates a fundamental circularity for P(k): the LCDM dictionary includes Omega_CDM = 0.266 in H(z), but the paper never explains where that component comes from in DFD ontology.

---

## Question 1: What Friedmann equation does the paper use?

### Answer: NONE is written down. H(a) is imported from the dictionary.

The paper contains **zero Friedmann equations**. There is no expression of the form H^2 = (8piG/3)(rho_b + rho_rad + ...) anywhere in the cosmology section, formalism section, or P(k) confrontation section.

The closest statement is at **section_cosmology.tex line 731-732**:

> "Equations (perturb-fourier)--(G-eff) describe the linear response of perturbations once a background history H(a) is supplied. In the present monograph, H(a) is taken from the DFD observer dictionary / reconstructed screen background already used throughout Sec. [cosmology]."

This is the **only statement in the entire paper** about what H(a) is used. It explicitly says H(a) comes from the "DFD observer dictionary."

### What is the "observer dictionary"?

Defined at **section_cosmology.tex line 9**:

> "DFD cosmology is treated as an inverse optical problem: infer the line-of-sight optical bias field directly from data, and only then interpret what standard cosmology would call 'expansion history,' 'dark energy,' and 'dark matter.' In this framing, GR/LCDM enters only as an observer dictionary (how distances/angles are commonly reported), not as ontology."

And at **section_cosmology.tex line 23**:

> "All GR/LCDM quantities used in this section (e.g. D_L^dict, D_A^obs) are reporting-layer variables that serve as a convenient dictionary for published datasets."

**Conclusion: H(z) = H_LCDM(z) with Omega_m ~ 0.3, imported wholesale as a dictionary.**

---

## Question 2: Does the paper distinguish TRUE vs OBSERVED expansion history?

### Answer: Yes, but only conceptually -- never quantitatively.

The paper frames LCDM quantities as "dictionary" or "reporting-layer" variables:

- **Line 9**: expansion history is what standard cosmology "would call" it
- **Line 23**: D_L^dict, D_A^obs are "reporting-layer variables"
- **Line 539**: "No GR ontology: GR/LCDM only appear as dictionary layers for reported distances/parameters"
- **Line 343**: "H_0 is the observer-dictionary Hubble parameter (reporting layer)"

However, the paper **never provides an alternative "true" expansion history**. It only says the dictionary is not ontology. The actual numerical H(z) used in all calculations is the LCDM one.

---

## Question 3: Omega_m = 0.3 and Omega_CDM

### What values appear in the paper:

**section_cosmology.tex line 585**:
> "Computing Eq. (psi-reconstruction) with Omega_m = 0.3 (matter-only baseline: Omega_m = 1)"

This uses Omega_m = 0.3 for the LCDM luminosity distance, and Omega_m = 1 (matter-only, no Lambda) as the baseline.

**section_cosmology.tex line 691**:
> "A particle-mesh simulation (64^3 grid, 200 Mpc/h box) comparing LCDM (Omega_m = 0.30), Newtonian-baryons (Omega_b = 0.049), and DFD-baryons (Omega_b = 0.049, mu(x) = x/(1+x)) on identical initial conditions"

**pk_analysis_pipeline.py line 33-34**:
```
# Fiducial cosmology (Planck 2018 + DFD dictionary)
OMEGA_M_0 = 0.31
```

**pk_analysis_pipeline.py line 47-49**:
```python
def omega_m_z(z, Om0=OMEGA_M_0):
    """Matter density parameter at redshift z (flat LCDM dictionary)."""
    return Om0 * (1+z)**3 / (Om0*(1+z)**3 + (1-Om0))
```

### Where does Omega_CDM = 0.266 come from in DFD?

**It is never stated.** The paper uses Omega_m = 0.30-0.31 (which in LCDM = Omega_b + Omega_CDM = 0.049 + 0.266) but **never explains what provides the 0.266 component** in DFD ontology.

The paper's answer to "what is dark matter?" is given at **line 404**:

> "DFD's cosmological stance is that what standard cosmology calls 'dark sector' is largely a consequence of interpreting a psi-warped optical universe through a GR forward model."

And at **line 407**:

> "Apparent 'missing mass' in kinematics corresponds to the nonlinear response packaged by mu(x), which is fixed by the DFD stack and constrained empirically in the galactic sector."

But mu(x) modifies the FORCE LAW for given density -- it does not add density to the Friedmann equation. The paper never connects mu(x) to the cosmological energy budget.

The dust-branch theorem (**lines 676-680**) claims to address this:

> "The unique local temporal scalar is Delta = (c/a_0)|dot-psi - dot-psi_0| (the linear deviation from the psi-screen). With K'(Delta) = mu(Delta), the dust branch emerges: w -> 0, c_s^2 -> 0. The psi-sector behaves as pressureless dust, clustering under gravity without pressure support."

But this describes the PERTURBATION equation of state, not the background energy density. The paper never says "the psi-dust contributes Omega_psi-dust = 0.266 to the Friedmann equation."

---

## Question 4: BAO scale and CMB peak positions without CDM

### The paper does NOT derive the BAO scale from first principles.

The psi-reconstruction (Eq. at line 577) computes Delta-psi as:

> Delta-psi(z) = ln(D_L^LCDM(z) / D_L^matter(z))

where D_L^LCDM uses Omega_m = 0.3 (including CDM!) and D_L^matter uses Omega_m = 1 (Einstein-de Sitter). This is a ratio of two GR models -- neither is a DFD-derived quantity.

For CMB: The paper derives R = 2.34 (peak ratio) and ell_1 = 220 semi-analytically (**line 537-538**):

> "Key observables derived: Peak ratio R = 2.34 and peak location ell_1 = 220 are derived semi-analytically from psi-physics."

The peak ratio derivation uses only baryon loading (**line 477**):

> "The key point is that f_baryon depends only on R_b (fixed by BBN), and the mu-dependent gravity enhancement cancels completely in the ratio. No dark matter is required."

But the peak LOCATION ell_1 = 220 depends on the sound horizon r_s, which depends on the matter-radiation equality redshift z_eq, which depends on Omega_m h^2. The paper acknowledges this is unfinished (**line 648**):

> "The CMB requires additional physics beyond Delta-psi_screen ~ 0.3 alone -- specifically, the 'evolving constants' mechanism of Sec. (psitomo-evolution). The sound horizon r_s or effective G at z ~ 1100 may differ from late-universe values."

---

## Question 5: Does Delta-psi REPLACE or SUPPLEMENT dark matter?

### Answer: It replaces DARK ENERGY, not dark matter.

The psi-screen at z=1 is Delta-psi = 0.274 (**line 606-607**):

> "Delta-psi(z=1.0) = 0.274 +/- 0.02"

And the paper says (**line 651**):

> "Delta-psi_screen ~ 0.28 at z ~ 1 is consistent with what LCDM attributes to dark energy."

The psi-screen reinterprets the ACCELERATION (dark energy), not the matter content (dark matter). The paper's treatment of dark matter is via mu(x) for kinematics and the dust-branch theorem for cosmology, but neither provides a quantitative Omega_CDM replacement.

---

## Question 6: "Standard background" statement

### The key quote (line 731-732):

> "In the present monograph, H(a) is taken from the DFD observer dictionary / reconstructed screen background already used throughout Sec. [cosmology]."

There is no statement like "the DFD Friedmann equation takes the dictionary LCDM form." Instead, the paper sidesteps the issue by treating H(a) as an imported dictionary quantity that is not DFD's job to derive.

Additional framing at **line 687**:

> "Numerical status: PROGRAM. A full transfer-function / survey-pipeline confrontation remains a program item. Published P(k) data are processed through GR-based fiducial cosmologies (the 'GR sandbox'), so direct confrontation requires dictionary translation plus a forward DFD perturbation solver."

---

## Question 7: Transfer function in P(k) confrontation

### Answer: NO transfer function is used.

The P(k) confrontation section (section_Pk_confrontation.tex) does NOT compute P(k). It only measures the RSD parameter beta = f/b from the RATIO P_2/P_0 of power spectrum multipoles. No transfer function (EH, BBKS, or otherwise) is ever mentioned.

The growth rate used is (**section_Pk_confrontation.tex line 57**):

> "f_DFD(z) = Omega_m(z)^gamma [1 + O(k_alpha)]"

with gamma ~ 0.55, which is the LCDM growth rate. The paper states (**line 60-61**):

> "DFD and LCDM predict indistinguishable linear growth at current multipole precision"

The script pk_analysis_pipeline.py confirms this uses a flat LCDM dictionary with Omega_m = 0.31 (**line 33-34, 47-49**).

---

## Question 8: N-body simulation background

### Answer: Three comparison runs, all using different assumptions.

**section_cosmology.tex line 690-692**:

> "A particle-mesh simulation (64^3 grid, 200 Mpc/h box) comparing LCDM (Omega_m = 0.30), Newtonian-baryons (Omega_b = 0.049), and DFD-baryons (Omega_b = 0.049, mu(x) = x/(1+x)) on identical initial conditions"

The DFD-baryons run uses Omega_b = 0.049 only (no CDM component) but with the mu(x) = x/(1+x) force law enhancement. The paper does NOT state what background expansion H(a) was used for the DFD run. Given "identical initial conditions," it was likely the same LCDM H(a) for all three runs, but this is not stated.

The result (**lines 696-704**):

> "DFD produces 43.8x more structure (delta_rms = 6.4e-3), establishing that nonlinear gravity overcomes the baryonic deficit. The 5.4x overshoot relative to LCDM is physically expected: cosmological perturbation accelerations (x ~ 4e-4) lie deep in the MOND regime where the raw mu-function enhances gravity by ~400x without the cosmological External Field Effect (EFE) from the Hubble flow (a_ext ~ cH_0 ~ 6 a_0). With the EFE, the effective enhancement drops from ~400 to ~1.2, which should bring DFD into quantitative agreement."

---

## THE CRITICAL QUESTION: Answer

### DFD v3.3 does NOT claim to explain the expansion history without dark matter.

The paper's strategy is:

1. **Import H(z) from LCDM as a "dictionary"** -- this includes Omega_CDM = 0.266 implicitly
2. **Reinterpret what observers see** through the psi-screen (replaces dark ENERGY)
3. **Replace dark matter KINEMATICS** with mu(x) nonlinear gravity (galaxy rotation curves, etc.)
4. **Claim the dust-branch theorem** shows psi can cluster like CDM (replaces dark matter for P(k) growth)
5. **Never close the loop** on what fills the H(z) energy budget

The paper explicitly acknowledges this is unfinished (**line 687**):

> "A full transfer-function / survey-pipeline confrontation remains a program item."

And (**line 685**):

> "The existence of the dust branch is derived; whether it reproduces the full observed P(k) spectrum is part of the numerical program below."

### The gap:

The dust-branch theorem says psi-perturbations have w=0, c_s^2=0 (like CDM). But for this to replace CDM in the expansion history, you need:

1. **The background psi-dust energy density** to equal Omega_CDM ~ 0.266 -- never derived
2. **The perturbation transfer function** with the correct shape (BAO wiggles, turnover at k_eq) -- never computed
3. **The BAO scale** to be correct (depends on z_eq which depends on Omega_m h^2) -- never addressed

The paper uses Omega_m = 0.3 in all numerical work but never explains where the CDM-like component of that 0.3 comes from within DFD.

---

## Summary of Key Quotes with Line Numbers

| Line | File | Quote (abbreviated) |
|------|------|---------------------|
| 9 | section_cosmology.tex | "GR/LCDM enters only as an observer dictionary...not as ontology" |
| 23 | section_cosmology.tex | "All GR/LCDM quantities...are reporting-layer variables" |
| 407 | section_cosmology.tex | "Apparent 'missing mass'...corresponds to the nonlinear response packaged by mu(x)" |
| 477 | section_cosmology.tex | "f_baryon depends only on R_b (fixed by BBN)...No dark matter is required" |
| 539 | section_cosmology.tex | "GR/LCDM only appear as dictionary layers" |
| 571 | section_cosmology.tex | "D_L(Omega_m, Omega_Lambda) / D_L(Omega_m=1, Omega_Lambda=0)" |
| 585 | section_cosmology.tex | "Computing...with Omega_m = 0.3 (matter-only baseline: Omega_m = 1)" |
| 651 | section_cosmology.tex | "Delta-psi_screen ~ 0.28 at z~1 is consistent with what LCDM attributes to dark energy" |
| 676-680 | section_cosmology.tex | "dust branch emerges: w -> 0, c_s^2 -> 0" |
| 685 | section_cosmology.tex | "existence of the dust branch is derived; whether it reproduces full P(k) is part of the numerical program" |
| 687 | section_cosmology.tex | "full transfer-function / survey-pipeline confrontation remains a program item" |
| 691-692 | section_cosmology.tex | "LCDM (Omega_m = 0.30), Newtonian-baryons (Omega_b = 0.049), DFD-baryons (Omega_b = 0.049)" |
| 731-732 | section_cosmology.tex | "H(a) is taken from the DFD observer dictionary" |
| 57 | section_Pk_confrontation.tex | "f_DFD(z) = Omega_m(z)^gamma" |
| 60-61 | section_Pk_confrontation.tex | "DFD and LCDM predict indistinguishable linear growth" |
| 33-34 | pk_analysis_pipeline.py | "OMEGA_M_0 = 0.31" with comment "Planck 2018 + DFD dictionary" |
| 48 | pk_analysis_pipeline.py | "Matter density parameter at redshift z (flat LCDM dictionary)" |

---

## Implications for P(k) Research

The P(k) problem in DFD has TWO distinct sub-problems:

### Sub-problem A: Background expansion
- The paper uses LCDM H(z) with Omega_m = 0.3 as a dictionary
- This implicitly includes CDM in the energy budget
- DFD has NOT derived what replaces CDM in the Friedmann equation
- The dust-branch theorem provides the equation of state (w=0, c_s=0) but NOT the energy density

### Sub-problem B: Perturbation growth
- G_eff = G / mu_0[1 + L_0 (k-hat . g-hat)^2] enhances growth on large scales
- The EFE from the Hubble flow (a_ext ~ cH_0 ~ 6 a_0) regulates the enhancement
- No transfer function has been computed
- The N-body proof-of-concept overshoots by 5.4x without EFE

### What any P(k) solver must decide:
1. **Use LCDM H(z) as dictionary** (as the paper does) -- but then the "dark matter" question is deferred, and you are really testing whether DFD perturbation growth on a LCDM background matches LCDM P(k)
2. **Use baryon-only H(z)** (Omega_b = 0.049 only) -- but then z_eq is wrong, the BAO scale is wrong, and the transfer function turnover is at the wrong k
3. **Use baryon + psi-dust H(z)** (Omega_b + Omega_psi-dust) -- but the paper never tells you what Omega_psi-dust is

This is the most important open question in DFD cosmology.
