---
status: draft
last-reviewed: 2026-09-07
sources:
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/101130 - informational derivation of quantum theory/paper.md
  - sources/papers/191121 - entangleability of cones/paper.md
machine-written: true
---

# Toolbox: the GPT framework

Definitions and results in house notation (`conventions/domain/notation.md`,
P1), each read from a filed source and cited by statement number: Plávala (P),
Müller (M), Barrett (B), Chiribella–D'Ariano–Perinotti (CDP), Aubrun–Lami–
Palazuelos–Plávala (ALPP). Statements only; check the PDF before quoting.
Rewritten into house notation on 2026-09-07 (first version used each source's
own notation).

## Single systems

**G1. System.** A = (V_A, V_A^+, u_A): V_A a finite-dimensional real vector
space, V_A^+ ⊂ V_A a proper cone (closed, convex, pointed, generating), u_A a
strictly positive functional. Normalised states Ω_A = {ω ∈ V_A^+ : u_A(ω) = 1}
form a compact convex base. [ALPP Def S8; M Def 5 with A₊ = V_A^+; P Def 2.1,
Prop 2.2 for Ω_A; B Assumptions 1, 2 for the fiducial-vector version]

**G2. Pure and mixed states, faces.** Pure = extreme point of Ω_A; mixed
otherwise; a face is a convex subset containing every decomposition of its
points. Ω_A = conv(ext Ω_A). Polytope: finitely many pure states; strictly
convex: every proper face is a point. [P Def 3.1–3.3, 3.6, 3.7, Thm 3.5]

**G3. Effects.** E_A = [0, u_A] ⊂ (V_A^+)^*: functionals with 0 ≤ e ≤ u_A in
the dual order. The dual cone (V_A^+)^* is proper; u_A is its order unit; every
effect has a complement u_A − e. [P Prop 3.10, 3.13, Lemma 3.11, 3.15, 3.17;
M Def 9]

**G4. Measurements.** A finite family (e_i) ⊂ E_A with Σ e_i = u_A;
equivalently a channel A → Cl_n. Two-outcome measurements ↔ E_A. [P Def 6.11,
Prop 6.13, Cor 6.14]

**G5. Duality.** Ω_A = {ω ∈ ((V_A^+)^*)^* : u_A(ω) = 1}, the bipolar theorem
recovering V_A^+ from the effect cone. Conversely a proper cone C with an order
unit u gives the effect algebra [0, u] and the state space
{ψ ∈ C^* : ψ(u) = 1}; convex effect algebras, linear effect algebras and order
unit spaces are equivalent presentations. In house notation the cone is
primitive and this is the passage V_A^+ ↔ (V_A^+)^*. [P Thm 3.19, Def 3.29,
Thm 3.26, Prop 3.28]

**G6. Norms and discrimination.** Order unit norm on V_A^* and base norm on
V_A; the optimal probability of discriminating ω₀ from ω₁ with priors λ, 1−λ
is given by the base norm of λω₀ − (1−λ)ω₁. [P Prop 3.37, 3.38, 3.42, Thm 3.43;
formula lost in extraction]

**G7. No-restriction hypothesis.** E_A = [0, u_A]: every mathematically
admissible effect is performable. A restricted theory keeps a convex
E ⊂ [0, u_A] containing 0 and u_A and separating Ω_A; equivalently it enlarges
the state space to {ψ ∈ cone(E)^* : ψ(u_A) = 1} ⊇ Ω_A. [P §3.7 (3.44)–(3.45);
JL Thm 1 for the unrestricted effect set; MM Requirement 5 for the gbit]
Standing assumptions: not assumed.

**G8. Transformations.** A morphism f : A → B is a positive linear map; allowed
if u_B ∘ f ≤ u_A, a channel if u_B ∘ f = u_A. The transpose f^* is positive for
the dual cones and unital for channels. Reversible transformations are linear
automorphisms of Ω_A; a dynamical system may allow only a subgroup. Linearity
is derived from mixing, not assumed. [P Def 6.1, 6.7, Prop 6.8; M Def 12; B
Assumptions 3, 7, §VIII]

**G9. Instruments and measure-and-prepare channels.** Instrument: a channel
A → Cl_n ⊗ B recording outcome and post-measurement state. Measure-and-prepare:
f(ω) = Σ_i e_i(ω) x_i for effects e_i and states x_i. Every measurement and
every constant channel is measure-and-prepare. [P Def 6.15, 6.17, Prop 6.18,
Cor 6.19, 6.20]

**G10. Perfect distinguishability, capacity.** ω₁, …, ω_n are jointly
perfectly distinguishable if a measurement has e_i(ω_j) = δ_ij; the capacity
N_A is the largest such n. A sequence of perfectly distinguishable *pure*
states is a frame (X9 in `gpt-axioms.md`). [M Def 10; CDP Def 5, 6; BH Def
3.1, 3.2]

## Composite systems

**G11. Bipartite axioms and tomographic locality.** A composite of A and B is a
system on some V_AB with bilinear product maps on states and effects, product
probabilities factorising, and the unit u_A ⊗ u_B. If local effects separate
joint states then V_AB = V_A ⊗ V_B: tomographic locality (B Assumption 5, the
global state assumption; M after Def 14; MM Requirement 2; CDP Axiom 4;
P (BP5)). Without it V_AB ⊇ V_A ⊗ V_B with a global sector (R12). [P Def 5.1
(BP1)–(BP5), Lemma 5.2; B Assumptions 4–6; BGW Def 2.1 for the cone version]

**G12. Minimal and maximal tensor cones.**
V_A^+ ⊗_min V_B^+ = cone{v ⊗ v' : v ∈ V_A^+, v' ∈ V_B^+} and
V_A^+ ⊗_max V_B^+ = {g : (e ⊗ e')(g) ≥ 0 for all e ∈ (V_A^+)^*, e' ∈ (V_B^+)^*}.
Any composite cone satisfies ⊗_min ⊆ V_AB^+ ⊆ ⊗_max; dually the effect cone lies
between (V_A^+)^* ⊗_min (V_B^+)^* and (V_A^+)^* ⊗_max (V_B^+)^*. Both extremes
are associative. Min–max duality: (C₁ ⊗_min C₂)^* = C₁^* ⊗_max C₂^*. States
outside ⊗_min are entangled. M: "given two state spaces, there are in general
infinitely many inequivalent possible composites". [P Def 5.3, 5.4, 5.8, Prop
5.6, Cor 5.7, Prop 5.11, 5.13; M Def 16; BBLW Def 1; ALPP §1]

**G13. Reduced states and no-signalling.** With P(a, b|x, y) =
(e_x^a ⊗ e_y^b)(ω_AB), marginals are independent of the other party's setting
because Σ_b e_y^b = u_B; ω_A = (id ⊗ u_B)(ω_AB). "Composite state spaces
automatically satisfy the no-signalling principle." B derives the same from
commuting local operations. [M Lemma 18; B Assumption 4, Cor 1]

**G14. Capacity is supermultiplicative.** N_AB ≥ N_A N_B. [M Lemma 19]

**G15. Entangleability.** V_A^+ ⊗_min V_B^+ = V_A^+ ⊗_max V_B^+ if and only if
one of the cones is classical (simplicial); for k cones, all but at most one
classical. Special case (C, C^*): nuclear iff C classical, equivalent to
no-broadcasting. Quantum composites sit strictly between the two extremes. [ALPP
Thm A, Cor 4, §2.3; P Prop 5.20, Thm 5.21; M Ex 17]

**G16. Complete positivity relative to a composite.** f : B → C is completely
positive for a composition rule if id_A ⊗ f maps V_AB^+ into V_AC^+ for every
A. Identities and measurements are CP for any rule; every positive map is CP
for ⊗_min and for ⊗_max; for intermediate rules CP is a genuine constraint, the
place where the composition rule constrains dynamics. [P Def 6.21, Prop 6.22,
6.23, 6.27, 6.28; BGW Def 6.4 for the Jordan case]

## Compatibility and broadcasting

**G17. Compatibility.** f₁ : A → B and f₂ : A → C are compatible if a channel
A → B ⊗ C has them as marginals; self-compatible if compatible with itself.
Every measure-and-prepare channel is self-compatible. [P Def 7.1, 7.3, Prop
7.4]

**G18. No-broadcasting.** Equivalent: id_A is measure-and-prepare; id_A is
self-compatible; a universal broadcasting channel A → A ⊗ A exists; A is
classical. Hence every non-classical system has incompatible channels, channels
that are not measure-and-prepare, incompatible two-outcome measurements, and no
post-processing-greatest measurement. A subset S ⊂ Ω_A can be broadcast iff
some measure-and-prepare channel fixes every point of S. [P Thm 7.7, Cor 7.8,
7.9, Thm 7.10, 7.11, Prop 7.16]

## Examples (details in `gpt-examples.md`)

**G19. Classical Cl_n.** (R^n, R^n_{≥0}, Σ_i): Ω a simplex; unique composite,
⊗_min = ⊗_max. [P Def 4.1; ALPP Def S16, S18]

**G20. Quantum Q_N.** (Herm_N(C), PSD, tr): Ω the density operators, effects
0 ≤ X ≤ 1 under Hilbert–Schmidt pairing; composite Q_{MN}, strictly between
⊗_min and ⊗_max; tomographically local, dim M²N² = (MN)²; no-restriction holds.
[P §8.1, 8.2; M Ex 7, 17]

**G21. Boxworld Box.** The square cone: V = R³, V^+ = cone over the square
with vertices s₀₀, s₁₀, s₀₁, s₁₁ = s₁₀ + s₀₁ − s₀₀; Barrett's (2,2) system.
Composites in Barrett's GNST admit every non-signalling table, PR boxes
included; single-system dynamics is "essentially classical, corresponding to no
more than relabellings of measurements and outcomes". [P §9 (9.2), (9.3); B
§IV.C, §I, §VI]

## Translation table

| house | Plávala | Müller | Barrett | ALPP |
|---|---|---|---|---|
| V_A^+ | A(K)*₊ | A₊ | conv(S ∪ {0}) | C |
| Ω_A | K | Ω_A | allowed normalised P | Ω |
| V_A^* ⊇ (V_A^+)^* | A(K) ⊇ A(K)₊ | A^* | vectors R | V^* ⊇ C^* |
| u_A | 1_K | u_A | normalisation | u |
| E_A | E(K) = [0, 1_K] | 0 ≤ e ≤ u_A | R with R·P a probability | [0, u] |
| morphism | affine K_A → K_B (channel) | linear T, T(Ω) ⊆ Ω | M ∈ T | positive map |
| ⊗_min, ⊗_max | ⊗̇, ⊗̂ | Ω_min, Ω_max | — | ⊙̲, ⊙̄ |

## What a TFT target needs from this

T7 in `tft-framework.md` needs a symmetric monoidal category of systems.
Ingredients above: objects (G1), morphisms (G8, or the CP ones for a chosen
rule, G16), a tensor product (a choice of V_AB^+ for every pair, associative,
G12), and duals for T3, which the framework does not supply (see
`categorical-gpts.md` C6–C7 and the project results R1–R2). Every choice is open
and belongs in `standing-assumptions.md` once made.
