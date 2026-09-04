---
status: draft
last-reviewed: 2026-09-04
sources:
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/101130 - informational derivation of quantum theory/paper.md
machine-written: true
---

# Toolbox: the GPT framework

Definitions and results as stated in the filed framework references, cited by
statement number: Plávala (P), Müller (M), Barrett (B), and Chiribella–D'Ariano–
Perinotti (CDP) where they add a definition. Three presentations of the same
objects; the translation table at the end says how they correspond. Nothing
here fixes a project convention; `conventions/domain/standing-assumptions.md`
says what is not assumed. Where the extraction lost a formula the statement is
paraphrased in words; check the PDF before quoting.

## Single systems

**G1. State space** [P Def 2.1, Prop 2.2; M Def 5; B Assumptions 1, 2].
P: a state space K is a set of points that is convex, closed, bounded and a
subset of a real finite-dimensional vector space; hence a compact convex subset.
M: a pair (A, Ω_A), A a real finite-dimensional vector space, Ω_A ⊂ A compact
convex of dimension dim A − 1, with a linear normalisation functional u_A equal
to 1 on Ω_A; the state cone A₊ = {λω : λ ≥ 0, ω ∈ Ω_A} is pointed and
Ω_A = {ω ∈ A₊ : u_A(ω) = 1}. B: a state is the vector of outcome probabilities
for a set of fiducial measurements; the allowed normalised states form a closed
convex set, and unnormalised states are its convex hull with the zero vector.

**G2. Pure and mixed states, faces** [P Def 3.1–3.3, 3.6, 3.7, Thm 3.5; M Def
6]. Pure = extreme point; mixed otherwise; a face is a convex subset containing
every decomposition of its points. K = conv(ext K). Polytope: finitely many pure
states. Strictly convex: every proper face is a point.

**G3. Effects** [P Def 3.8, Prop 3.10, 3.13, Lemma 3.11, 3.15, Def 3.16,
Lemma 3.17; M Def 9]. E(K) is the set of affine functions K → [0, 1]. A(K) is
the space of affine functions K → R and A(K)₊ its positive cone, which is
convex, closed, pointed and generating. E(K) = {f ∈ A(K) : 0 ≤ f ≤ 1_K}, where
the unit effect 1_K is the order unit of A(K)₊. Every effect has a complement
1_K − f. M: an effect is e ∈ A* with 0 ≤ e(ω) ≤ 1 for all normalised ω.

**G4. Measurements** [P Def 6.11, Prop 6.13, Cor 6.14; M Def 9]. An n-outcome
measurement is a channel K → S_n into the n-outcome simplex, equivalently a
family of effects f₁, …, f_n with Σ f_i = 1_K. Two-outcome measurements are in
bijection with E(K).

**G5. Duality and the cone-first presentation** [P Thm 3.19, Prop 3.20, Def
3.21–3.29, Thm 3.26, Prop 3.28, Lemma 3.34]. K = {φ ∈ A(K)*₊ : ⟨φ, 1_K⟩ = 1}:
the state space is a base of the dual cone. Conversely start from (V, C, u) with
V real finite-dimensional, C ⊂ V a convex closed pointed generating cone and
u ∈ C an order unit; then E = [0, u] is a linear effect algebra and
S(E) = {ψ ∈ C* : ⟨ψ, u⟩ = 1} is its state space. Convex effect algebras, linear
effect algebras and order unit spaces are equivalent presentations. This is the
presentation in which cone and order unit are primitive; the retired notes used
a version of it, and which presentation the paper adopts is open.

**G6. Norms and discrimination** [P Prop 3.37, 3.38, 3.42, Thm 3.43]. The order
unit norm on A(K), ‖f‖ = inf{λ : −λ1_K ≤ f ≤ λ1_K}; the base norm on A(K)*,
‖ψ‖ = inf{λ + μ : ψ = λx − μy, x, y ∈ K}. The optimal probability of
discriminating x₀ from x₁ with priors λ, 1 − λ is given by the base norm of
λx₀ − (1 − λ)x₁ [P Thm 3.43; formula lost in extraction].

**G7. No-restriction hypothesis** [P §3.7; MM Requirement 5]. The assumption
that every f ∈ E(K) corresponds to a yes–no question that can, at least in
principle, be performed. A restricted theory keeps a convex E ⊂ E(K) with
0, 1_K ∈ E separating the states; its state space
S(E) = {ψ ∈ cone(E)* : ⟨ψ, 1_K⟩ = 1} contains K, so restricting the effects is
equivalently enlarging the state space [P (3.44), (3.45)]. P: "it is not trivial
to consistently define a theory with restrictions" (citing Janotta–Lal).
Masanes–Müller's Requirement 5, "all measurements allowed", is no-restriction
for the generalised bit. Standing assumptions: not assumed; TODO Pedro.

**G8. Transformations and channels** [P Def 6.1, 6.7, Prop 6.8; M Def 12; B
Assumptions 3, 7, §VIII]. P: a channel K_A → K_B is an affine map; its adjoint
Φ* : E(K_B) → E(K_A) is linear and unital, Φ*(1_{K_B}) = 1_{K_A}. M: a
transformation is a linear T : A → A with T(Ω_A) ⊆ Ω_A, reversible if T⁻¹ is
also one; every reversible transformation is a linear symmetry of Ω_A; a
dynamical state space (A, Ω_A, T_A) may allow only a subgroup. B: linearity of
transformations is derived, not assumed, from the fiducial vector being a
complete description; normalisation-decreasing transformations are included;
Assumption 7 (all well-defined transformations are allowed) makes a theory a
function of its state spaces alone.

**G9. Instruments and measure-and-prepare channels** [P Def 6.15, 6.17, Prop
6.18, Cor 6.19, 6.20]. An instrument is a channel K → S_n ⊗ K_B recording the
outcome and the post-measurement state. A measure-and-prepare channel is P ∘ m,
Φ(y) = Σ_i ⟨y, f_i⟩ x_i. Every measurement, and every constant channel, is
measure-and-prepare; not every channel is (G18).

**G10. Perfect distinguishability and capacity** [M Def 10; CDP Def 5, 6].
States ω₁, …, ω_n are jointly perfectly distinguishable if some measurement has
e^(i)(ω_j) = δ_ij. The capacity N_A is the largest such n. CDP: a set is maximal
if no further state can be added.

## Composite systems

**G11. Bipartite axioms** [P Def 5.1 (BP1)–(BP5), Lemma 5.2; B Assumptions 4,
5, 6; M after Def 14]. P: (BP1) K_AB is a state space; (BP2) product
preparations exist and depend affinely on each factor; (BP3) product effects
exist and depend linearly; (BP4) the unit effect is 1_A ⊗ 1_B; (BP5) local
effects separate bipartite states. Consequence: K_AB ⊂ A(K_A)* ⊗ A(K_B)*. B:
Assumption 4, local operations commute, and Assumption 5, the global state
assumption (joint states are fixed by joint probabilities of local fiducial
measurements), with product states allowed (Assumption 6). M: Tomographic
Locality, "all states ω_AB are uniquely determined by the joint statistics of
all local measurements", attributed to Hardy 2001; equivalently AB = A ⊗ B and
K_AB = K_A K_B for the dimensions.

**G12. Minimal and maximal tensor products** [P Def 5.3, 5.4, 5.8, Prop 5.6,
Cor 5.7, Prop 5.11, 5.13; M Def 16]. K_A ⊗̇ K_B = conv{x_A ⊗ x_B}.
K_A ⊗̂ K_B = {φ ∈ A(K_A)* ⊗ A(K_B)* : ⟨φ, f_A ⊗ f_B⟩ ≥ 0 for all effects,
⟨φ, 1_A ⊗ 1_B⟩ = 1} = S(E(K_A) ⊗̇ E(K_B)). Any valid composite ⊗̃ satisfies
⊗̇ ⊆ ⊗̃ ⊆ ⊗̂, and dually E(K_A) ⊗̇ E(K_B) ⊆ E(K_AB) ⊆ E(K_A) ⊗̂ E(K_B). Both
extremes are associative. States outside ⊗̇ are entangled. M: "given two state
spaces, there are in general infinitely many inequivalent possible composites".

**G13. Reduced states and no-signalling** [M Lemma 18; P §5.4; B Corollary 1].
With P(a, b|x, y) = e_x^(a) ⊗ e_y^(b)(ω_AB) the marginals are independent of
the other party's input because the effects of a measurement sum to the unit:
"composite state spaces automatically satisfy the no-signalling principle" [M].
Reduced states ω_A = (1_A ⊗ u_B)(ω_AB) generalise the partial trace. B derives
the same from commuting local operations.

**G14. Capacity is supermultiplicative** [M Lemma 19]. N_AB ≥ N_A N_B.

**G15. Entanglement exists unless a factor is classical** [P Prop 5.20, Thm
5.21; M after Ex 17]. K_A ⊗̇ K_B = K_A ⊗̂ K_B if and only if at least one factor
is a simplex. Quantum composites sit strictly between: ⊗̇ is the separable
states, ⊗̂ the operators positive on all product tests, including non-density
"witness" operators [M Ex 17].

**G16. Complete positivity** [P Def 6.21, Prop 6.22, 6.23, 6.27, 6.28]. A
channel Φ : K_B → K_C is completely positive with respect to a composition rule
if id_A ⊗ Φ maps K_A ⊗̃ K_B into K_A ⊗̃ K_C for every K_A. The identity and every
measurement are CP for any rule; every channel is CP with respect to ⊗̇ and
with respect to ⊗̂. For intermediate rules CP is a genuine constraint: this is
where a composition rule constrains the dynamics.

## Compatibility and broadcasting

**G17. Compatibility** [P Def 7.1, 7.3, Prop 7.4]. Channels Φ₁ : K_A → K_B and
Φ₂ : K_A → K_C are compatible if a channel K_A → K_B ⊗̃ K_C has both as
marginals; self-compatible if compatible with itself. Every measure-and-prepare
channel is self-compatible.

**G18. No-broadcasting** [P Thm 7.7, Cor 7.8, 7.9, Thm 7.10, 7.11, Prop 7.16].
Equivalent: id_K is measure-and-prepare; id_K is self-compatible; a universal
broadcasting channel K → K ⊗̃ K exists; K is a simplex. Hence every
non-classical K has a pair of incompatible channels, a channel that is not
measure-and-prepare, a pair of incompatible two-outcome measurements, and no
post-processing-greatest measurement. A subset B ⊂ K can be broadcast if and
only if some measure-and-prepare channel fixes every point of B [P Thm 7.10].

## Examples

**G19. Classical theory** [P Def 4.1; M after Ex 17]. K = S_n, a simplex;
everything else is called non-classical. The composite of two classical systems
is unique, ⊗̇ = ⊗̂.

**G20. Quantum theory** [P §8.1, 8.2; M Ex 7, 17]. K = D(H), the density
operators; A(D(H)) ≅ B_H(H) via X ↦ Tr(ρX); A₊ ≅ positive operators;
E = {X : 0 ≤ X ≤ 1}. The composite is D(H_A ⊗ H_B), strictly between ⊗̇ and ⊗̂;
it satisfies tomographic locality, K_AB = (MN)² = M²N², and no-restriction.

**G21. Boxworld** [P §9; B §IV.C "Generalized Non-Signalling Theory"]. Single
system: the square S = conv{s₀₀, s₁₀, s₀₁, s₁₁} ⊂ R³ with s₁₁ = s₁₀ + s₀₁ − s₀₀,
dim A(S) = 3 [P (9.2), (9.3)]; B's (2, 2) system, two binary fiducial
measurements. Composites in B's GNST: any non-signalling probability table is a
state, PR boxes included; the dynamics of single systems is "essentially
classical, corresponding to no more than relabellings of measurements and
outcomes" [B §I, §VI].

## Translation table

| object | Plávala | Müller | Barrett |
|---|---|---|---|
| system | K ⊂ V compact convex | (A, Ω_A, u_A) | fiducial vector P; allowed set S |
| unnormalised states | A(K)*₊ | A₊ | conv(S ∪ {0}) |
| effects | E(K) = [0, 1_K] ⊂ A(K) | e ∈ A*, 0 ≤ e ≤ u_A | vectors R with R·P the outcome probability |
| unit | 1_K | u_A | normalisation |
| channel | affine K_A → K_B | linear T with T(Ω) ⊆ Ω | M ∈ T, normalisation non-increasing |
| composite | ⊗̇ ⊆ ⊗̃ ⊆ ⊗̂ under (BP1)–(BP5) | Ω_min ⊆ Ω_AB ⊆ Ω_max under tomographic locality | tensor product from Assumptions 4 and 5 |

## What a TFT target needs from this

T7 in `tft-framework.md` asks for a symmetric monoidal category of GPT systems.
The ingredients above: objects (G1 or G5); morphisms (G8: all channels, or the
channels completely positive with respect to a chosen rule, G16); a tensor
product (a choice of ⊗̃ for every pair, associative, G12); and duals for T3,
which none of P, M or B discusses. Every one of these is open and belongs in
`standing-assumptions.md` once chosen. Machine-written; UNVERIFIED as the
paper's route.
