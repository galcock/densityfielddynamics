# M17 — The "15" Framing Subtraction: Rigorous Audit

**Question.** L16 reduces Ω_b ↦ N_twist = 55 − 15 = 40, asserting that "15" is the
Witten 2-framing / S³ framing-anomaly subtraction for an O(9) rank-1 Wilson line in
SU(2) Chern–Simons at level k = 60. Is "15" derivable from Witten (1989,
*Comm. Math. Phys.* 121, 351)?

## 1. What Witten actually computes

For CS theory with gauge group G at level k on a 3-manifold M, the partition function
Z(M) depends on a choice of **2-framing** of M (Atiyah 1990). Under a shift of the
2-framing by s ∈ ℤ, Witten (1989, eq. 2.23) showed

    Z(M, framing + s) = Z(M, canonical) · exp(2πi · s · c/24),

where the central charge of the boundary WZW model is

    c = k · dim G / (k + h∨).

For SU(2), dim G = 3, h∨ = 2, so at k = 60:

    c = 60 · 3 / 62 = 180/62 = 90/31 ≈ 2.9032.

This is the **only** universal framing-dependent factor in Witten's setup. There is
no place in the formula where the integer 15 arises from k = 60.

## 2. Wilson-line ribbon framing (the other "framing")

A Wilson line in representation R carries an independent **ribbon framing**. Under a
twist of the ribbon by one unit, the line picks up a phase

    θ_R = exp(2πi · h_R),    h_R = C₂(R) / (2(k + h∨)),

with C₂(R) the quadratic Casimir of R. For SU(2) spin-j:

    C₂(j) = j(j+1),    h_j = j(j+1) / (2·62) = j(j+1)/124.

For j = 9 ("O(9)" read as the spin-9, dim-19 irrep — the only natural reading inside
SU(2)):

    h_9 = 9·10/124 = 90/124 = 45/62 ≈ 0.7258.

A ribbon-framing shift by N units gives phase exp(2πi · N · 45/62). Setting this
phase trivial requires N ≡ 0 (mod 62), again giving no "15".

## 3. Searching exhaustively for 15 in the SU(2)_{60} data

Candidate combinations actually available from (k, h∨, dim G, j, C₂):

| Expression | Value |
|---|---|
| c = k·dimG/(k+h∨) | 90/31 ≈ 2.903 |
| c·24 | 2160/31 ≈ 69.68 |
| (k − h∨)/4 | 58/4 = 14.5 |
| (k + h∨)/4 | 62/4 = 15.5 |
| k/4 | 15.0 ✓ |
| h_9 · (k+h∨) | 45 |
| 2j+1 (dim of j=9) | 19 |
| j(j+1)/6 | 15.0 ✓ |
| C₂(SU(2))·dim(j=9)/(2(k+h∨)+…) | not 15 |

Two exact hits on 15:

* **k/4 = 60/4 = 15**, but this has *no* derivation from Witten's formula —
  c/24 ≠ k/4 except by accident, and dividing the bare level by 4 is not a
  framing-anomaly quantity.
* **j(j+1)/6 = 90/6 = 15** for j = 9. This is just the Casimir divided by 6, which
  is *not* a framing correction either: framing involves C₂/(2(k+h∨)) = 45/62, not
  C₂/6.

Both "derivations" of 15 are numerological coincidences with no anchor in the
Witten/Atiyah framing-anomaly formalism.

## 4. What the framing anomaly *actually* contributes at k = 60, j = 9

Total framing phase under (s, N) shifts:

    arg Z = 2π · [ s · (90/31)/24 + N · 45/62 ] = 2π · [ s · 15/124 + N · 45/62 ].

Note 15 *does* appear here as the numerator of c/24 = 15/124 — but this is a
**rational-number numerator inside an irrational phase**, not an integer
"subtraction." It contributes 15/124 ≈ 0.121 per unit framing shift, which has
nothing to do with subtracting 15 from 55 to get 40.

The closest thing to "15" in the legitimate framing data is therefore the appearance
of 15 = (k·dim G)/(24 · gcd) numerator after reducing 90/(31·24) → 15/124. This is a
*coefficient inside a continuous U(1) phase*, not a counted integer of twists.

## 5. Verdict on L16

The claim "N_twist = 55 − 15 = 40, with 15 the Witten framing subtraction" is
**not derivable** from Witten 1989 / Atiyah 1990 in any rigorous sense:

1. The framing anomaly is a continuous U(1) phase exp(2πi · s · c/24), not an
   integer subtraction from a count.
2. c/24 = 15/124 at SU(2)_{60}; the "15" here is a numerator of a rational phase,
   not a discrete twist count.
3. The Wilson-line ribbon framing for j = 9 contributes h_9 = 45/62, again a phase,
   not 15.
4. No combination of (k = 60, h∨ = 2, dim G = 3, C₂(9) = 90) yields the integer 15
   via any formula appearing in Witten's CS partition function or Reshetikhin–Turaev
   surgery formula. The two numerical coincidences (k/4 = 15 and j(j+1)/6 = 15) have
   no provenance in the framing formalism.

**Recommendation: downgrade L16.** The reduction 55 → 40 cannot currently be
justified as a Witten 2-framing subtraction. Either:

* (a) re-derive the "15" from a *different* mechanism (e.g., a counting of zero
  modes, a Hirzebruch defect, an η-invariant, or an index-theoretic subtraction —
  none of which is the Witten framing anomaly), and rewrite L16 to cite that
  mechanism honestly; or
* (b) treat 40 as an empirical input and remove the claim that it follows from CS
  framing; or
* (c) abandon the 55 → 40 reduction and let Ω_b stand on its prior derivation.

Until one of (a)–(c) is executed, L16 should be marked **NOT DERIVED — relies on a
numerical coincidence misattributed to Witten 1989**.

## 6. Pointers for a possible rescue (option a)

If a rigorous "15" exists, the most plausible non-Witten sources are:

* **Casson invariant of S³-related surgeries**: λ(S³) = 0, but Dehn surgery
  contributions on torus knots can yield small integers; none obviously give 15 at
  these parameters.
* **η-invariant of the signature operator on a lens space L(p, q)**: η = (something
  involving p, q); for L(4, 1) the value is ±1/4, not 15.
* **Hirzebruch defect / signature defect** for a plumbed 3-manifold: integer-valued,
  but requires specifying the plumbing graph — not provided in L16.
* **Index of a Dirac operator on a U(1)-bundle of degree n over S²**: equals n; one
  would need to identify n = 15 from independent geometry.

None of these are "the Witten framing anomaly," so option (a) requires renaming the
mechanism, not just citing Witten 1989 differently.

---

**Bottom line.** "15" is **not** derivable from Witten 1989 for SU(2)_{60} with a
spin-9 Wilson line. L16's framing-anomaly justification is incorrect and the claim
should be downgraded or rewritten.
