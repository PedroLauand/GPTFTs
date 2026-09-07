# Notation

Provisional house notation, adopted 2026-09-07 for the toolbox and for
discussions (decision log). It re-enters the notation of the retired notes,
which is also that of Barnum–Hilgert (Def 2.1) and Aubrun–Lami–Palazuelos–
Plávala (Def S8). Pedro: "we will have our own convention"; until then this is
it. Changing it is a convention change: log it, then rename everywhere.

## Systems

| symbol | meaning |
|---|---|
| A = (V_A, V_A^+, u_A) | a system: a finite-dimensional real vector space, a proper cone of unnormalised states (closed, convex, pointed, generating), and a unit u_A ∈ V_A^* with u_A(v) > 0 for v ∈ V_A^+ \ {0} |
| Ω_A = {ω ∈ V_A^+ : u_A(ω) = 1} | normalised states, a compact convex base of the cone; its extreme points are the pure states |
| (V_A^+)^* | the dual cone in V_A^*: functionals nonnegative on V_A^+ |
| E_A = [0, u_A] | effects; a measurement is a finite family (e_i) ⊂ E_A with Σ e_i = u_A |
| f : A → B | a morphism: a linear map V_A → V_B with f(V_A^+) ⊆ V_B^+. *Allowed* if u_B ∘ f ≤ u_A on V_A^+; a *channel* if u_B ∘ f = u_A |
| f^* | the transpose, f^*(e) = e ∘ f; positive for the dual cones |
| 1 = (R, R_{≥0}, id) | the trivial system. States are arrows 1 → A, effects arrows A → 1, probabilities e(ω) their composites |
| AB = (V_A ⊗ V_B, V_{AB}^+, u_A ⊗ u_B) | a composite under tomographic locality, with ⊗_min ⊆ V_{AB}^+ ⊆ ⊗_max |
| V_A^+ ⊗_min V_B^+, V_A^+ ⊗_max V_B^+ | the minimal (separable) and maximal tensor cones; Plávala writes ⊗̇ and ⊗̂, ALPP ⊙̲ and ⊙̄, BBLW ⊗_min and ⊗_max |
| ω_A = (id ⊗ u_B)(ω_AB) | the reduced state |
| A^∨ = (V_A^*, (V_A^+)^*, u^∨) | the dual system, u^∨ any interior point of V_A^+ (project result R1, unverified) |
| GPT, (GPT, ⊗) | the category of systems and morphisms; with a coherent choice of composites |
| Cl_n, Q_N, Box, Poly_n, J(A) | the standard examples: the simplex (R^n, R^n_{≥0}, Σ); quantum (Herm_N(C), PSD, tr); the square cone in R³; the regular n-gon cones; the cone of squares of a Euclidean Jordan algebra A. See `syntheses/toolbox/gpt-examples.md` |

Reading other sources into house notation: Plávala's K is Ω_A, his A(K) is V_A^*
and A(K)*₊ is V_A^+, his E(K) is E_A; Müller's (A, Ω_A, u_A) with A₊ is
(V_A, Ω_A, u_A) with V_A^+; Barrett's fiducial probability vector is an element
of V_A. Full table in `syntheses/toolbox/gpt-framework.md`.

## Field theory

| symbol | meaning |
|---|---|
| Bord_n | the oriented bordism category: objects closed oriented (n−1)-manifolds, morphisms diffeomorphism classes of bordisms; ⊔, ∅, σ for disjoint union, unit, symmetry |
| Z : Bord_n → C | a TFT valued in C, a symmetric monoidal functor |
| •₊, •₋, ∪, ∩ | the two oriented points and the cup ∅ → •₊ ⊔ •₋ and cap •₋ ⊔ •₊ → ∅ of Bord_1 |
| X^∨, ev, coev | duality data of a dualisable object; the snake (zigzag, Zorro) identities |
| η, μ, Δ, ε | disk, pants, copants, reversed disk of Bord_2; the Frobenius algebra data on Z(S¹) |
| β = ε ∘ μ, γ = Δ ∘ η | the Frobenius pairing and copairing |
| h = μ ∘ Δ | the handle operator; Z(Σ_g) = ε(h^g(1)) |
| φ, θ | involution and crosscap element of an extended (unoriented) Frobenius algebra |
| unitary TFT | target Hilb with Z(M^*) = Z(M)^*; in 2d, Z(S¹) a commutative C*-Frobenius algebra |

## Manuscript markup (`paper/draft.tex`)

| markup | meaning |
|---|---|
| `\textcolor{blue}{...}` | drafted or approved prose; the `%` comment above the block says which, and the approval date |
| `\tmp{[...]}` (red) | placeholder or open item: a missing citation, a beat not yet written, the title, the abstract |
| `\pedro{...}`, `\bereket{...}`, `\elie{...}` | coloured comments by author (purple, blue, raw sienna) |
| `% B<n> ...` | beat label. The introduction is written beat by beat, B1 to B9; there is no B5 |
| `% RETIRED (kept for salvage)` | a paragraph taken out of the text but kept commented for reuse |

## Abbreviations

| abbreviation | expansion | where |
|---|---|---|
| QT | quantum theory | B1+B2 |
| GPT | generalized probabilistic theory | B1+B2 |
| OPT | operational probabilistic theory | glossary only; the draft cites CDP2011 without naming the framework |
| NS | no-signalling | not abbreviated in the draft; used in this repository |
| TFT | topological field theory | title |
| RG | renormalisation group | retired B4 |
| AQFT | algebraic quantum field theory | retired B4 |
| SR | special relativity | this repository |
| EJA | Euclidean Jordan algebra | toolbox |
| SSC, BH, BMU, BGW, BBLW, ALPP, CR, DJ | Selby–Scandolo–Coecke; Barnum–Hilgert; Barnum–Müller–Ududec; Barnum–Graydon–Wilce; Barnum–Barrett–Leifer–Wilce; Aubrun–Lami–Palazuelos–Plávala; Carqueville–Runkel; Durhuus–Jonsson | toolbox source tags |

## Spelling in force

The draft writes "Generalized Probabilistic Theories", "no-signalling",
"axiomatizations", "spacelike" and "spacetime" as single words. Source titles
keep their own spelling (Gisin2020 has "no-signaling"). TODO Pedro: choose
American or British spelling for the manuscript; RevTeX/APS expects American,
and the current text mixes them.
