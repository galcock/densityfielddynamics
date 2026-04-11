# L4: Scan of ⟨G_eff/G⟩ for 16/3

## Setup
v3.3 formula: `G_eff/G = 1/μ(x(1 + L(k̂·ĝ)²))`. With μ(y)=y/(1+y) this gives
`1/μ = 1 + 1/y`, so the direction average over cos θ ∈ [0,1] is
`⟨G_eff/G⟩ = 1 + (1/x)·⟨1/(1+L cos²θ)⟩`.

Target: 16/3 ≈ 5.33333.

## Scan
Ran `L4_g_eff_scan.py` over {μ_simple, μ_n (n=2,3), μ_{α,λ} family}, L ∈ {0, 0.1, 0.5, 1, 2, 5, 10},
and weights {isotropic, k², transverse, Gaussian baryon-localized}.

**Every combination yields a finite x_crit** solving ⟨G_eff/G⟩=16/3; i.e. 16/3 is not a
privileged value — every smooth μ passes through it somewhere.

## Key analytic result
For μ_simple, L=0, isotropic:
  ⟨G_eff/G⟩ = 1 + 1/x  =  16/3  ⇒  **x = 3/13** (exactly).

Numerical verification: 5.333333333333 vs target 5.333333333333 ✓.

## Does 3/13 match any natural DFD scale?
Checked against: α, √α, α², 1/(4π), 1/√(k+2) for k=0..11, 1/137, ln2, π/6, etc.

- 3/13 = 0.230769... — **no match** to any natural scale in the list.
- α⁻¹·(3/13) ≈ 31.62 — not meaningful.
- 3/13 is not of the form 1/(k+2), 1/√N, α^n.
- Closest "structural" coincidence: 3/13 = 3/(16-3) = 3/(TARGET·3 - 3) — circular.

## Other μ families
| μ | L | weight | x_crit |
|---|---|--------|--------|
| simple | 0 | iso | 0.2308 (=3/13) |
| μ_2 | 0 | iso | 0.2000 (=1/5) |
| μ_3 | 0 | iso | 0.1878 |
| μ_{1,2} | 0 | iso | 0.1909 |
| μ_{2,1} | 0 | iso | 0.4804 |

μ_2 at L=0 gives **x = 1/5**, which is clean but not a known DFD scale
(closest: 1/√(k+2) for k=23? No. 1/(k+2)? → k=3 sector but k+2=5 means k=3, which *is*
the "χ sector 3 pairs" index, but this is circumstantial).

With non-zero L or non-isotropic weights, x_crit shifts continuously; no L picks out a privileged
value α, √α, etc. to 3-digit tolerance.

## Conclusion
**No natural DFD configuration gives ⟨G_eff/G⟩ = 16/3 exactly.** The cleanest solution is
μ_simple with L=0 → x = 3/13, but 3/13 does not match any predicted DFD scale. μ_2 → x=1/5
is suggestive (k=3 sector label "k+2=5") but circumstantial, not a derivation.

The 16/3 factor therefore **cannot be recovered as a direction-averaged G_eff/G** from the
v3.3 interpolation function family without tuning x to a non-natural value. If 16/3 is to be
derived, it must come from a different route (path-integral / conserved-current / χ-mode counting),
not from μ-interpolation averaging.

## Files
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/L4_g_eff_scan.py`
- `/Users/garyalcock/claudecode/densityfielddynamics/v34_research/L4_g_eff_scan.md`
