---
source_pdf: Well_posedness_of_the_Psi_Equation.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

WELL-POSEDNESS AND BOUNDARY VALUE PROBLEMS FOR A CLASS
OF QUASILINEAR DIVERGENCE-FORM EQUATIONS ARISING IN
DENSITY FIELD DYNAMICS
GARY ALCOCK

Abstract. We study the quasilinear elliptic partial differential equation

−∇ · µ(|∇ψ|)∇ψ = f in Ω ⊆ R3 ,
where µ is a nonlinear constitutive function. Motivated by density-field models of gravitational
optics, we develop a rigorous framework for existence, uniqueness, and regularity of weak solutions,
extend the analysis to exterior domains with asymptotically flat boundary conditions, and incorporate monotone nonlinear Robin–Neumann conditions modeling photon-spheres and horizons. We
further establish stability estimates, continuous dependence on data, and parabolic well-posedness
using nonlinear semigroup theory. A variational formulation, catalog of admissible µ-families, and
finite element method (FEM) implementation outline are provided. Open problems relevant to
global existence and singularity formation are discussed.

Contents
1. Introduction
Notation
1.1. Physical motivation for µ and boundary conditions
2. Assumptions on µ
3. Weak formulation and variational structure
4. Main results
5. Exterior domains and optical boundary conditions
6. Stability and continuous dependence
7. Parabolic extension and semigroup theory
8. Finite element method (FEM) implementation
9. Catalog of admissible µ-families
10. Open problems
Acknowledgements
References
Figure: Exterior Domain with Optical Boundaries

1
2
2
2
2
3
3
3
3
4
4
4
4
4
5

1. Introduction
We investigate the nonlinear elliptic equation

−∇ · µ(|∇ψ|)∇ψ = f,

(1)

posed on a domain Ω ⊆ R3 . Here ψ : Ω → R is the unknown scalar potential, µ : [0, ∞) → (0, ∞)
is a nonlinear coefficient, and f represents a source term. Such equations belong to the class of
quasilinear divergence-form PDEs with p-growth, generalizing the p-Laplacian. They arise in fluid
Date: September 24, 2025.
1

2

GARY ALCOCK

mechanics, nonlinear diffusion, and, in recent physical models, as optical potentials in effective
theories of gravitation.
Notation.
• Lp (Ω): standard Lebesgue spaces, 1 ≤ p ≤ ∞.
• W 1,p (Ω): Sobolev space of Lp functions with Lp weak derivatives.
• V := W01,p (Ω): closure of Cc∞ (Ω) in W 1,p .
• V ′ : dual of V .
• ⟨·, ·⟩: duality pairing between V ′ and V .
1.1. Physical motivation for µ and boundary conditions. In density-field models of gravitation, one introduces an “optical potential” ψ such that the refractive index is n = eψ . The
flux coefficient µ(|∇ψ|) encodes the response of the medium to spatial gradients of ψ. Its form
determines how weak-field Newtonian gravity, strong-field photon spheres, and effective horizon
behavior emerge.
Boundary conditions are motivated as follows:
• Photon sphere: defined by an extremum of the optical circumference n(r)r. This yields
a Robin-type condition with coefficient κopt (ψ) tied to the local optical speed.
• Horizon: at the surface where outgoing null characteristics stall, one enforces an “ingoing
flux only” condition. Mathematically this corresponds to a nonlinear Neumann condition
eliminating outgoing flux. We emphasize this is physically motivated but mathematically
non-standard, and justifying it within elliptic PDE theory is an open problem.
2. Assumptions on µ
We assume µ : [0, ∞) → (0, ∞) satisfies:
• (A1) Continuity: µ is continuous on [0, ∞).
• (A2) Coercivity: ∃α > 0, p ≥ 2 such that
µ(|ξ|)|ξ|2 ≥ α|ξ|p

∀ξ ∈ R3 .

• (A3) Growth: ∃β > 0 such that
|µ(|ξ|)ξ| ≤ β(1 + |ξ|)p−1 .
• (A4) Monotonicity: For all ξ, η ∈ R3 ,

µ(|ξ|)ξ − µ(|η|)η · (ξ − η) ≥ 0.
If strict, uniqueness follows.
Examples include the p-Laplacian µ(s) = p
sp−2 , saturating nonlinearities µ(s) = (1 + s2 )(p−2)/2 ,
and MOND-like regularized forms µ(s) = s/ s2 + s2a [6, 7].
3. Weak formulation and variational structure
Define the flux map a(ξ) := µ(|ξ|)ξ. For ψ ∈ W 1,p (Ω) with boundary data ψ = ψD , the weak
formulation is:
Z
Z
a(∇ψ) · ∇v dx =
f v dx, ∀v ∈ W01,p (Ω).
(2)
Ω

Ω

Define the energy density
Z 1
a(tξ) · ξ dt,

H(ξ) :=
0

so that a(ξ) = ∇ξ H(ξ). Then the functional
Z
Z
E[ψ] :=
H(∇ψ) dx −
f ψ dx
Ω

Ω

WELL-POSEDNESS OF THE ψ-EQUATION

3

is convex and coercive under (A1)–(A3).
4. Main results
Theorem 4.1 (Existence). Under (A1)–(A4), for any f ∈ V ′ , there exists a weak solution ψ ∈
W 1,p (Ω) of (1) attaining the prescribed boundary data.
Theorem 4.2 (Uniqueness). If a(ξ) = µ(|ξ|)ξ is strictly monotone, the weak solution of Theorem
4.1 is unique.
Theorem 4.3 (Regularity). If f ∈ Lq (Ω) with q > 3/p′ , then any weak solution ψ is locally Hölder
0,α
1,α
continuous: ψ ∈ Cloc
(Ω). If µ ∈ C 1 and f ∈ C 0,γ , then ψ ∈ Cloc
(Ω).
Proofs follow standard methods from monotone operator theory and quasilinear elliptic regularity
[1, 2, 3, 4].
5. Exterior domains and optical boundary conditions
Let Ω = R3 \ BR denote an exterior domain. We impose:
• Asymptotic flatness: ψ(x) → 0 as |x| → ∞.
• Photon-sphere boundary: Nonlinear Robin condition
a(∇ψ) · n + κopt (ψ) ψ = gph

on Γph ,

with κopt positive and bounded.
• Horizon boundary: Ingoing-flux Neumann condition
a(∇ψ) · n = ghor ,

with outgoing flux set to zero.

This asymmetric boundary condition is physically motivated but not standard in elliptic
PDE theory. A full mathematical justification remains open.
Theorem 5.1 (Exterior well-posedness). Under (A1)–(A4) and the above boundary conditions,
there exists a weak solution ψ ∈ W 1,p (Ω). If the boundary operators are strictly monotone, the
solution is unique.
6. Stability and continuous dependence
Theorem 6.1 (Stability). Let ψ1 , ψ2 be solutions with data (f1 , BC1 ), (f2 , BC2 ). If a is strongly
monotone and locally Lipschitz, then


′
p
∥∇(ψ1 − ψ2 )∥L (Ω) ≤ C ∥f1 − f2 ∥V + ∥BC1 − BC2 ∥ .
7. Parabolic extension and semigroup theory
Consider

∂t ψ − ∇ · µ(|∇ψ|)∇ψ = f (t, x).
Let A : V → V ′ be the monotone operator A(ψ) = −∇ · a(∇ψ). By Crandall–Liggett theory [5],
−A generates a contraction semigroup on L2 (Ω).
Theorem 7.1 (Parabolic well-posedness). Under (A1)–(A4), there exists a unique evolution ψ ∈
Lp (0, T ; W 1,p (Ω)) ∩ C([0, T ]; L2 (Ω)). If f is time-independent and boundary operators are dissipative, then solutions converge to a steady state as t → ∞.

4

GARY ALCOCK

8. Finite element method (FEM) implementation
The weak form (2) is directly implementable in finite element packages. Nonlinear terms are
treated via Newton iteration with Jacobian
Aij (∇ψ) = µ(|∇ψ|)δij + µ′ (|∇ψ|)

∂i ψ ∂j ψ
.
|∇ψ|

Remark 8.1. At
p |∇ψ| → 0, the Jacobian may become ill-conditioned. A practical remedy is to
replace |∇ψ| by |∇ψ|2 + s20 with small s0 > 0 (regularization). For background on FEM analysis
of quasilinear PDEs, see [8, 9].
Optical boundary conditions appear as Robin/Neumann integrals in the variational form.

9. Catalog of admissible µ-families
• p-Laplacian: µ(s) = sp−2 .
• Saturating: µ(s) = (1 + s2 )(p−2)/2 .
• Regularized MOND-like: µ(s) = √ 2s

s +s2a

[6, 7].

• Anisotropic: µ replaced by positive-definite tensor M (∇ψ).

10. Open problems
• Global existence with physically realistic sources f .
• Gradient blow-up and singularity formation.
• Regularity near horizons under nonlinear asymmetric BCs.
• Mathematical justification of the “ingoing flux only” horizon condition.
• Coupling of the scalar ψ-equation to tensorial sectors in relativistic completions.

Acknowledgements
The author thanks the PDE community for foundational results that make this analysis possible.

References
[1] L. C. Evans, Partial Differential Equations, 2nd ed., AMS, 2010.
[2] D. Gilbarg and N. Trudinger, Elliptic Partial Differential Equations of Second Order, Springer, 2001.
[3] O. A. Ladyzhenskaya and N. N. Uraltseva, Linear and Quasilinear Elliptic Equations, Academic Press, 1968.
[4] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Differential Equations, Springer, 2010.
[5] M. G. Crandall and T. M. Liggett, Generation of semi-groups of nonlinear transformations on general Banach
spaces, Amer. J. Math. 93 (1971), 265–298.
[6] M. Milgrom, A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis,
Astrophysical Journal 270 (1983), 365–370.
[7] J. Bekenstein and M. Milgrom, Does the missing mass problem signal the breakdown of Newtonian gravity?,
Astrophysical Journal 286 (1984), 7–14.
[8] S. Brenner and R. Scott, The Mathematical Theory of Finite Element Methods, 3rd ed., Springer, 2008.
[9] A. Ern and J.-L. Guermond, Theory and Practice of Finite Elements, Springer, 2004.

WELL-POSEDNESS OF THE ψ-EQUATION

Figure: Exterior Domain with Optical Boundaries

∇ψ

Horizon

ψ→0
Photon sphere

Asymptotic boundary

5

