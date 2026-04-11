# H13: External Verification Plan for DFD Core Derivations

**Issue:** No independent reproduction of DFD's central derivations exists. This plan defines a concrete, time-bounded workflow for getting qualified third parties to verify the key results.

**Owner:** H13 (verification campaign lead)
**Date:** 2026-04-06
**Target completion:** 6 months (pre-print by month 2, first review cycle by month 4, JCAP submission by month 6)

---

## Step 1 — Core Derivations Requiring Verification

Priority-ordered list of results that, if wrong, collapse significant portions of DFD v3.3:

| # | Result | v3.3 Reference | Why critical |
|---|--------|---------------|--------------|
| 1 | α^57 = H₀²/M_P² | Theorem O.7 | Sets cosmological constant hierarchy; single exponent determines vacuum energy |
| 2 | 16/3 = Ω_χ/Ω_b | Spectral-trace factorization | Dark-to-baryon ratio; directly testable against Planck |
| 3 | m_χ = √158 · M̄_P · α^11 | Compound α-tower | Fixes χ-field mass; drives detection prospects |
| 4 | V''(0) = 158 | Sph³ spectral computation | Integer that feeds into (3); pure spectral-geometry claim |
| 5 | μ(x) = x/(1+x) | Composition-law derivation | MOND interpolation function; the single empirical MOND prediction |
| 6 | N_gen = 3 = χ(CP²) | Euler characteristic | Explains generation count from topology |
| 7 | a₀ = 2√α · cH₀ | MOND-scale derivation | Predicts MOND acceleration from first principles |

---

## Step 2 — Verification Requirements per Result

### (1) α^57 = H₀²/M_P²
- **Expertise:** Spectral action / noncommutative geometry, dimensional analysis of the DFD heat-kernel expansion.
- **Calculation to reproduce:** The Seeley–DeWitt a₀...a₄ coefficients on the DFD internal manifold, tracking α-power counting from the volume factor and Dirac-operator eigenvalues through to the cosmological-constant line in the action.
- **Effort:** 2–4 weeks (one reviewer with a symbolic-algebra assistant).
- **Targets:** Connes, Chamseddine, Iochum, Suijlekom.

### (2) 16/3 = Ω_χ/Ω_b
- **Expertise:** Spectral triples, representation theory of the DFD gauge bundle, thermal history of χ freeze-in.
- **Calculation:** Trace factorization over the finite part of the spectral triple, yielding the 16 (χ multiplicity) / 3 (generation / color) ratio. Cross-check with the Boltzmann solver already in `v34_research/H3_01_boltzmann_solver.py`.
- **Effort:** 1–2 weeks.
- **Targets:** Chamseddine, Marcolli, Zwicky (for the cosmology side).

### (3) m_χ = √158 · M̄_P · α^11
- **Expertise:** QFT + spectral geometry. Must track (4) through to the mass formula.
- **Calculation:** Second derivative of the DFD potential at the origin, times the α^22 suppression from two insertions of the tower, square-rooted.
- **Effort:** 1 week, conditional on (4).
- **Targets:** Moroianu, Bär (Dirac/Laplace spectra on symmetric spaces).

### (4) V''(0) = 158 (Sph³ spectral computation)
- **Expertise:** Spectrum of the Laplacian / Dirac operator on S³ and its DFD deformation; lattice Chern–Simons if the discrete regularization is used.
- **Calculation:** Sum of squared eigenvalues up to the DFD cutoff on S³ with the twisted spin structure; reproduce the integer 158.
- **Effort:** 2 weeks (symbolic + numerical).
- **Targets:** Moroianu, Bär, Ammann; Yang (if lattice CS cross-check is desired).

### (5) μ(x) = x/(1+x)
- **Expertise:** Nonlinear field theory, RG-style composition laws.
- **Calculation:** Derivation of the interpolating function from the composition rule on DFD-density flows; show uniqueness under the stated symmetry constraints.
- **Effort:** 1 week.
- **Targets:** Mistele, Milgrom, Famaey.

### (6) N_gen = 3 = χ(CP²)
- **Expertise:** Algebraic topology, index theory.
- **Calculation:** Euler characteristic of CP² via Poincaré polynomial and cross-check with Atiyah–Singer applied to the DFD Dirac operator; confirm the generation count is the topological invariant and not a tunable parameter.
- **Effort:** 2–3 days.
- **Targets:** Moroianu, Atiyah-school geometers.

### (7) a₀ = 2√α · cH₀
- **Expertise:** Cosmological perturbation theory and MOND phenomenology.
- **Calculation:** Derive a₀ from the DFD low-acceleration limit; compare the numerical value with the McGaugh/SPARC determination.
- **Effort:** 1 week.
- **Targets:** Mistele, Famaey, McGaugh.

---

## Step 3 — Verification Package (per result)

Each of the seven results gets its own package in `v34_research/verification/result_{n}/` containing:

1. **`claim.md`** (1 page) — statement, symbol glossary, numerical value, connection to observation.
2. **`derivation.pdf`** (≤5 pages) — self-contained derivation with every non-obvious step justified; no forward references into the main v3.3 manuscript.
3. **`notebook.ipynb`** (Python + SymPy; Mathematica `.nb` parallel where symbolic algebra dominates) — executable, reproducible, pinned dependencies, seed fixed.
4. **`assumptions.md`** — every assumption made, flagged STRONG / MILD / CONVENTIONAL.
5. **`failure_modes.md`** — the specific steps most likely to break under scrutiny (sign conventions, regularization choice, operator ordering, finite-vs-infinite trace, choice of spin structure, etc.).
6. **`data/`** — any numerical inputs; for (1) and (7) this includes the Planck 2018 H₀ and M_P constants used.

Build order: (4) → (3) → (1) → (2) → (7) → (5) → (6). Rationale: (4) is the atomic integer; everything downstream inherits its correctness.

---

## Step 4 — Target Reviewers

Primary targets (ranked by fit and likelihood of engaging):

| Reviewer | Affiliation | Fit | Preferred results |
|----------|-------------|-----|-------------------|
| Ali Chamseddine | AUB / IHES | Spectral action co-inventor | (1), (2), (4) |
| Alain Connes | IHES / Collège de France | Noncommutative geometry | (1), (2) |
| Andrei Moroianu | CNRS / Paris-Saclay | Dirac operators, CP² | (3), (4), (6) |
| Christian Bär | Potsdam | Laplace/Dirac spectra | (4) |
| Tobias Mistele | Case Western | MOND / modified gravity | (5), (7) |
| Benoit Famaey | Strasbourg | MOND phenomenology | (5), (7) |
| Stacy McGaugh | Case Western | MOND observations | (7) |
| Roman Zwicky | Edinburgh | Cosmological perturbation theory | (2) |
| Matilde Marcolli | Caltech | NCG + cosmology | (2) |
| (Chern–Simons contact) | — | Lattice CS cross-check | (4) |

Back-channel first via conference contacts or a short introductory email (see Step 7); do not cold-send 5-page derivations.

---

## Step 5 — Journal Submission Strategy

Ranked by likelihood of fair review given the unconventional framing:

1. **JCAP** — cosmology-facing, open to foundational work that makes CMB/LSS predictions. Primary target for results (1), (2), (7).
2. **Classical and Quantum Gravity** — strict but fair on gravitational-sector derivations; good fit for (1) and the spectral action content.
3. **Foundations of Physics** — willing to consider foundational/geometric proposals with less rigid formatting requirements; fallback for the synthesis paper combining (4)–(6).
4. **Physical Review D** — highest standard; reserve for after at least two reviewers have independently verified at least (1) and (4). Do not lead with PRD.
5. **Communications in Mathematical Physics** — for the pure-math spectral computation (4) on its own.

Strategy: split into three papers — (A) spectral derivation of (1)+(4)+(3), (B) cosmological consequences (2)+(7), (C) topology and generations (6) + MOND interpolation (5).

---

## Step 6 — arXiv Pre-print Strategy

Post each paper with:
- **Primary:** `gr-qc`
- **Cross-list:** `hep-ph`, `astro-ph.CO`
- Add `math-ph` for paper (A).

Include in every preprint:
- A "Reproducibility" section pointing at the Zenodo archive.
- An explicit "Request for comments" paragraph naming the verification email and a 30-day comment window.
- A clear "Status" line: "Under external verification; comments welcome before journal submission."

---

## Step 7 — Verification Workflow (concrete timeline)

**Month 1**
- Day 1–3: Fix placeholder DOIs in existing manuscripts and in the Zenodo archive metadata. (Blocker: the v3.3 LaTeX sources currently reference placeholder DOIs; these must be resolved before any external distribution.)
- Day 4–10: Assemble verification package for result (4) — the atomic integer 158.
- Day 11–20: Assemble packages for (3) and (1).
- Day 21–28: Packages for (2), (5), (6), (7).
- Day 29–30: Internal red-team pass on all seven packages; populate `failure_modes.md`.

**Month 2**
- Deposit complete Zenodo archive with real DOIs. Freeze the computational record.
- Post paper (A) to arXiv.
- Send first wave of contact emails to Chamseddine, Moroianu, Bär, Mistele (short, one-paragraph, link to arXiv + Zenodo, no attachment).

**Month 3**
- Post papers (B) and (C).
- Send second wave (Connes, Marcolli, McGaugh, Famaey, Zwicky) — only after paper (A) has had 2+ weeks of arXiv exposure.
- Track all responses in `v34_research/verification/responses.md`.

**Month 4**
- Respond to feedback with specific, dated revisions. Every revision gets a changelog entry in the corresponding package directory.
- If any reviewer identifies a concrete error, STOP downstream submissions and triage before continuing.

**Month 5**
- Prepare JCAP submission for paper (B), bundling the referee responses already collected as supplementary material. Same for CQG on paper (A).

**Month 6**
- Submit. Track editor decisions. If desk-rejected, rotate to the next journal in the Step 5 ranking without re-litigating the preprint.

---

## Immediate Blockers to Clear Before Step 7 Starts

1. **Placeholder DOIs** in Zenodo metadata and in the v3.3 LaTeX sources — must be replaced with real DOIs before any external email goes out.
2. **Notation harmonization** — α, M_P, M̄_P, and H₀ conventions differ between `DFD_Planck_Mass_Convention_Audit.tex` and the main manuscript; fix before writing `claim.md` files.
3. **Sph³ spectral code** — there is no standalone script reproducing V''(0) = 158 today. Writing that script is prerequisite to the result (4) package and thus to the entire chain.
4. **Boltzmann solver sanity check** — `H3_01_boltzmann_solver.py` must reproduce the 16/3 ratio numerically before (2) goes out; otherwise reviewers will immediately ask for it.

Clearing items 1–4 is the first concrete task; without them, no external verification attempt is credible.

---

## Success Criteria

H13 is closed when **at least two independent reviewers**, each qualified for the relevant result, have reproduced:
- result (4) — the integer 158 — in a computational environment other than the original DFD repository, AND
- result (1) — the α^57 relation — from the spectral-action coefficients.

Those two are load-bearing for everything else. If they survive external reproduction, the remaining results become incremental. If either fails, the campaign's finding is itself the deliverable: DFD v3.3 has a concrete error to fix.
