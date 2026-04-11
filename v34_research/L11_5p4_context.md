# L11: Verbatim context for "5.4×" in v3.3

Source: `Density_Field_Dynamics__A_Complete_Unified_Theory__v3_3/section_cosmology.tex`
Line of interest: 697 (in the paragraph `\paragraph{Proof-of-concept: $N$-body structure formation.}`)

## 1. Full paragraph containing "5.4×" (lines 689–706, VERBATIM)

```
\paragraph{Proof-of-concept: $N$-body structure formation.}
A particle-mesh simulation ($64^3$ grid, 200~Mpc/$h$ box) comparing
$\Lambda$CDM ($\Omega_m = 0.30$), Newtonian-baryons ($\Omega_b = 0.049$),
and DFD-baryons ($\Omega_b = 0.049$, $\mu(x) = x/(1+x)$) on identical
initial conditions demonstrates the key point: Newtonian-baryons produces
negligible structure ($\delta_{\rm rms} = 1.5 \times 10^{-4}$),
confirming the standard objection; DFD produces $43.8\times$ more
structure ($\delta_{\rm rms} = 6.4 \times 10^{-3}$), establishing that
nonlinear gravity overcomes the baryonic deficit.  The $5.4\times$
overshoot relative to $\Lambda$CDM is physically expected: cosmological
perturbation accelerations ($x \approx 4 \times 10^{-4}$) lie deep in
the MOND regime where the raw $\mu$-function enhances gravity by
$\sim\!400\times$ without the cosmological External Field Effect (EFE)
from the Hubble flow ($a_{\rm ext} \sim cH_0 \approx 6\,a_0$).
With the EFE, the effective enhancement drops from $\sim\!400$ to
$\sim\!1.2$, which should bring DFD into quantitative agreement.
This is a proof-of-concept at $64^3$ resolution; production-quality
results require $\geq 256^3$ with the EFE implemented.
```

## 2. N-body setup description (VERBATIM extracted)

- "particle-mesh simulation ($64^3$ grid, 200~Mpc/$h$ box)"
- Three models on **identical initial conditions**:
  - "$\Lambda$CDM ($\Omega_m = 0.30$)"
  - "Newtonian-baryons ($\Omega_b = 0.049$)"
  - "DFD-baryons ($\Omega_b = 0.049$, $\mu(x) = x/(1+x)$)"

## 3. What was compared to what

- Newtonian-baryons: $\delta_{\rm rms} = 1.5 \times 10^{-4}$
- DFD-baryons: $\delta_{\rm rms} = 6.4 \times 10^{-3}$
- DFD/Newtonian ratio: "$43.8\times$ more structure"
- DFD vs $\Lambda$CDM: "$5.4\times$ overshoot relative to $\Lambda$CDM"

So "5.4×" = (DFD $\delta_{\rm rms}$) / ($\Lambda$CDM $\delta_{\rm rms}$).
This implies $\Lambda$CDM $\delta_{\rm rms} \approx 6.4\times10^{-3} / 5.4 \approx 1.19\times10^{-3}$
(the $\Lambda$CDM number itself is not printed in the paragraph).

## 4. What the "5.4" is a ratio of (per v3.3 text)

Per v3.3: a ratio of **numerical $\delta_{\rm rms}$ amplitudes** of the
DFD particle-mesh run over the $\Lambda$CDM particle-mesh run on identical
ICs. It is NOT identified anywhere in this paragraph as $\Omega_c/\Omega_b$.

## 5. Surrounding discussion of EFE correction (VERBATIM, already in paragraph above)

Key lines:
- "cosmological perturbation accelerations ($x \approx 4 \times 10^{-4}$) lie deep in the MOND regime"
- "the raw $\mu$-function enhances gravity by $\sim\!400\times$ without the cosmological External Field Effect (EFE) from the Hubble flow ($a_{\rm ext} \sim cH_0 \approx 6\,a_0$)"
- "With the EFE, the effective enhancement drops from $\sim\!400$ to $\sim\!1.2$, which should bring DFD into quantitative agreement."
- "proof-of-concept at $64^3$ resolution; production-quality results require $\geq 256^3$ with the EFE implemented."

## 6. Any formula for why 5.4 was expected

**NONE.** v3.3 offers no closed-form formula predicting 5.4. The only
quantitative scaling given is an order-of-magnitude argument:
- raw enhancement $\sim 400\times$
- post-EFE residual $\sim 1.2\times$
- $a_{\rm ext} \sim cH_0 \approx 6\,a_0$

There is no equation deriving the 5.4 value. The text frames 5.4 as an
*overshoot* of a still-uncorrected simulation, to be eliminated once the
EFE is added — i.e., v3.3 treats 5.4 as a transient numerical artifact,
not a physical target.

## Planck 2018 cross-check

- $\Omega_c h^2 = 0.1200 \pm 0.0012$
- $\Omega_b h^2 = 0.02237 \pm 0.00015$
- $\Omega_c/\Omega_b = 0.1200/0.02237 = 5.3644\ldots \approx 5.364 \pm 0.064$

Is the v3.3 "5.4" within error bars of 5.364? **Yes, trivially** —
5.4 lies ~0.036 above the central value, well inside 1σ (~0.064)
and in fact less than 1σ away even with rounding.

## Does v3.3 EXPLICITLY note this coincidence?

**NO.** Searched the v3.3 tree for every string `5.4`:

```
section_strong_fields.tex:113  b_crit^DFD ≈ 5.44 GM/c^2   (2e factor, unrelated)
section_cosmology.tex:697      "5.4× overshoot relative to ΛCDM"
appendix_Y_finite_yukawa.tex:683  s = 5.4×10^-4  (Yukawa table entry, unrelated)
PATCH_NOTES_v3_3.txt:94        "Newton-baryons, 5.4x overshoot relative to LCDM (expected without EFE)"
```

None of these identify 5.4 with $\Omega_c/\Omega_b$. The cosmology
paragraph and the patch note both treat 5.4 purely as a simulation
artifact. Nowhere in v3.3 is the coincidence with the Planck cold-to-baryon
ratio acknowledged.

## Does v3.3 attempt any derivation of 5.4?

**NO.** The only scaling given is the raw-MOND $\sim 400\times$ vs
post-EFE $\sim 1.2\times$ narrative. There is no derivation, no formula,
and no target value — 5.4 is presented as a number to be *removed* by
adding the EFE in production runs, not as a predicted ratio.

## Dismissal text (the "smoking gun")

From section_cosmology.tex lines 697–706 (VERBATIM — already quoted above):

> "The $5.4\times$ overshoot relative to $\Lambda$CDM is physically expected:
> cosmological perturbation accelerations ($x \approx 4 \times 10^{-4}$) lie
> deep in the MOND regime where the raw $\mu$-function enhances gravity by
> $\sim\!400\times$ without the cosmological External Field Effect (EFE)
> from the Hubble flow ($a_{\rm ext} \sim cH_0 \approx 6\,a_0$). With the
> EFE, the effective enhancement drops from $\sim\!400$ to $\sim\!1.2$,
> which should bring DFD into quantitative agreement."

And from `PATCH_NOTES_v3_3.txt:94` (VERBATIM):

> "Newton-baryons, 5.4x overshoot relative to LCDM (expected without EFE),"

Both instances frame 5.4 as a **transient pre-EFE numerical overshoot**
that should disappear (drop from ~400 to ~1.2) once the EFE is implemented.
v3.3 never notices that 5.4 ≈ $\Omega_c/\Omega_b$ (Planck 2018 = 5.364±0.064),
and therefore dismisses as a bug exactly the quantity that Planck would
call the cold-dark-matter-to-baryon ratio.

## Smoking-gun summary

- v3.3 line 697 reports DFD/$\Lambda$CDM $\delta_{\rm rms}$ ratio = 5.4.
- Planck 2018 $\Omega_c/\Omega_b$ = 5.364 ± 0.064.
- 5.4 is within 1σ of the Planck cold-to-baryon ratio.
- v3.3 does NOT note this.
- v3.3 explicitly dismisses 5.4 as an EFE-less artifact to be removed.
- No derivation of 5.4 exists anywhere in v3.3.
