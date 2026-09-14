---
status: draft
last-reviewed: 2026-09-14
sources:
  - sources/papers/180201 - reconstructing quantum theory from diagrammatic postulates/paper.md
  - sources/papers/170125 - categorical probabilistic theories/paper.md
  - sources/papers/160630 - composites and categories of euclidean jordan algebras/paper.md
  - sources/papers/150722 - some nearly quantum theories/paper.md
  - sources/papers/080523 - teleportation in general probabilistic theories/paper.md
  - sources/papers/140514 - terminality implies non-signalling/paper.md
  - sources/papers/240522 - entanglement swapping in gpts and iterated chsh games/paper.md
  - sources/papers/260322 - probabilistic theories stable under teleportation/paper.md
  - sources/papers/170516 - introductory lectures on topological quantum field theory/paper.md
  - sources/papers/100416 - symmetry compact closure and dagger compactness for categories of convex operational models/paper.md
  - sources/papers/091230 - ensemble steering weak self-duality and the structure of probabilistic theories/paper.md
  - sources/papers/120613 - conjugates filters and quantum mechanics/paper.md
  - sources/papers/190711 - deriving dagger compactness/paper.md
machine-written: true
---

# Toolbox: categorical GPTs

The category of GPTs in house notation, with the categorical definitions the
literature adds on top of it, each illustrated on Cl_n, Q_N and Box. Sources
by statement number: Selby–Scandolo–Coecke (SSC), Gogioso–Scandolo (GS),
Barnum–Graydon–Wilce (BGW; NQ for "Some nearly quantum theories"),
Barnum–Barrett–Leifer–Wilce (BBLW), Coecke, Dmello–Ligthart–Gross (DLG),
Dmello–Gross (DG), Carqueville–Runkel (CR); added 2026-09-14: Barnum–Duncan–
Wilce (BDW), Barnum–Gaebler–Wilce (BGW-G), Wilce, Tull. Project results from the retired
notes are labelled R and live in `project-results-archive.md`; they are not
assumed. Provisional conventions P1, P2 in `standing-assumptions.md`.

**C1. Process theory.** Systems as wires, processes as boxes with input and
output wires, wired together into diagrams without causal loops; equivalently a
symmetric monoidal category. Sequential composition is "after", parallel
composition "while". [SSC Def 2.1; Coecke §2, Rem 2.1, 4.1] House: (GPT, ⊗).

**C2. The category GPT.** Objects A = (V_A, V_A^+, u_A); morphisms positive
linear maps; Hom(A, B) is a cone, not a vector space, so GPT is a wide, non-full
subcategory of Vec under the forgetful functor. Channels u_B ∘ f = u_A are the
causal subcategory. [retired notes, R12; SSC Prop 2.25: with a classical
interface the states form a finite-dimensional pointed convex cone and processes
induce completely positive maps between cones] Cl_n: stochastic-type positive
maps, channels the stochastic ones; Q_N: positive maps on Hermitian matrices,
channels trace-preserving; Box: positive maps of the square cone.

**C3. Trivial system, states, effects.** 1 = (R, R_{≥0}, id); ω : 1 → A is a
state, e : A → 1 an effect, e ∘ ω = e(ω) the probability. u_A : A → 1 is the
discarding effect. [retired notes; GS Def 1 environment structure; SSC Prop
2.24 discarding maps]

**C4. Composites and the monoidal structure.** A composite is a bilinear
positive π : V_A × V_B → V_AB with π(u_A, u_B) the unit and all product states
present; π is injective; under tomographic locality V_AB = V_A ⊗ V_B and the
cone lies in [⊗_min, ⊗_max]. Any coherent (associative, symmetric) choice makes
(GPT, ⊗) symmetric monoidal. A composite of several systems is regular if it is
a composite for every partition; associative rules give regular composites;
A ⊗_min (B ⊗_max C) embeds in (A ⊗_min B) ⊗_max C. [BGW Def 2.1, Lemma 2.2,
Def 2.3 dynamical composite; BBLW Def 2, 3, Prop 1, Cor 1; G12] Cl_n: one
composite; Q_N: the density-operator composite, strictly between; Box: Barrett's
GNST uses ⊗_max.

**C5. Discarding, causality, terminality.** Terminality: every process followed
by discarding equals discarding; equivalently one deterministic effect per
system. It is CDP's Axiom 1 (no signalling from the future) and implies
two-party non-signalling once causal structure is explicit; the converse needs a
unique closed diagram. In house notation the deterministic effect is u_A and
terminal processes are the channels. [Coecke Def 3.1, Prop 3.2, Thm 5.1, 5.4;
CDP Axiom 1; GS Def 1(3)] Holds in Cl_n, Q_N, Box alike.

**C6. Cups and caps.** A theory has cups and caps if for each system there are
processes ∪_A : 1 → A ⊗ A^∨ and ∩_A : A^∨ ⊗ A → 1 satisfying the snake
equations; equivalently inputs may be connected to inputs and loops are allowed
("compact structure"). SSC: they "assert that the theory has 'maximal'
correlations", and "non-trivial causal subtheories will not have cups and
caps": the cap cannot be a channel. Quantum: Choi–Jamiołkowski, the cup a
supernormalised maximally entangled state; classical: the copy–delete pair.
[SSC Def 2.36, Ex 2.37, 2.38, §2.5] Consequence for house GPT: cups and caps
live among allowed or cone-linear morphisms, not channels; the causal
subcategory is never compact closed.

**C7. Dualisable objects and the forced dual.** In any symmetric monoidal C, X
is dualisable if there are X^∨, ev : X^∨ ⊗ X → 1, coev : 1 → X ⊗ X^∨ with the
snake identities; duality data are unique up to unique isomorphism; 1d TFTs
valued in C are exactly the dualisable objects (T5). In Vec every object is
dualisable. In GPT the underlying linear data are forced by Vec: X^∨ =
(V^*, (V^+)^*, u^∨), ev the pairing, coev the identity element Σ f_a ⊗ f^a; what
is contingent is positivity of coev as a state of X ⊗ X^∨ and of ev as an
effect on X^∨ ⊗ X, one element tested from inside and from outside one composite
cone. [CR Thm 3.2; R1, R2 unverified] Cl_n: coev is separable, lies in ⊗_min;
Q_N: coev is the unnormalised maximally entangled operator, in the density-
operator cone after a transpose twist of the dual leg; Box: expected to fail
(R8, unverified).

**C8. Teleportation as the snake.** A pair (f, ω) of a bipartite effect and a
bipartite state is a conclusive teleportation protocol iff the induced map
μ = ω̂ ∘ f̂ is an order isomorphism, up to a correction; a regular composite of
three pairwise isomorphic weakly self-dual systems with a suitable ω supports
conclusive teleportation; deterministic teleportation is a measurement each of
whose outcomes teleports up to a correction; a weakly self-dual system with a
finite group acting transitively on pure states and an equivariant isomorphism
V ≅ V^* supports it, so "self-duality is not necessary for deterministic
teleportation". The snake identity is the exact protocol with resource and
measurement both equal to coev (R3). [BBLW Def 4, Thm 1, Cor 4, Def 5, Thm 3]

**C9. Dagger.** A dagger sends a process A → B to a process B → A,
compositionally; "time reversal". Sharp: the dagger of a testable causal state
tests it. With a classical interface the dagger is linear. Quantum: the
Hermitian adjoint. [SSC Def 2.40, Post 4, Lemma 4.1] House GPT has no dagger by
default; a self-dual system supplies one via the inner product.

**C10. Purification.** Every state has a purification, unique up to a
reversible transformation on the purifying system (CDP); SSC use the symmetric
version, every process has an essentially unique symmetric purification, and
show it implies the standard one given pure cups. [CDP Postulate 1; SSC Post 5,
Def 3.1, Prop 6.1, 6.2] Q_N yes; Cl_n no.

**C11. Classical interface.** A full classical subtheory (all classical systems
n ∈ N), all classically controlled processes, and enough causal-compatible local
tomographic tests. GS's version: a full sub-SMC equivalent to R₊-Mat, enrichment
in commutative monoids, and an environment (discarding) structure. Consequence:
the convex-cone structure of C2. [SSC Post 2, Def 2.14–2.16, 2.19, Prop 2.25;
GS Def 1]

**C12. Categories of Jordan-algebraic systems.** Embedded JC-algebras (A, M_A)
with completely Jordan-preserving CP maps form symmetric monoidal categories
under the canonical tensor product; the universally reversible ones with dagger-
CJP maps are dagger-compact. No composite of EJAs has an exceptional summand
unless the other factor is classical; a composite of simple special EJAs is an
ideal in their universal tensor product. Phenomena: failure of local tomography,
supermultiplicative capacity, mixed states with pure marginals. The closest
published analogue of "a category of GPTs with duals". [BGW Def 5.1, 5.2, 6.1,
6.4, Prop 6.10, Prop 4.14, Thm 4.15; NQ Thm 2, abstract]

**C13. Entanglement-swapping and teleportation-stable theories.** A theory with
well-defined entanglement swapping is (V, 1, {P^(n)}, {D^(n)}) with effect and
state cones at every n, closed under tensoring, positive pairing, partial
contractions and permutations; Algorithm 1 decides consistency of bipartite
input data and Algorithm 2 induces all higher cones by minimal tensor products.
Dualisability in this setting: η ∈ D^(2), ε ∈ P^(2) with η̂ ε̂ = c·id;
teleportation up to a correction group H when a measurement {ε_h} has
η̂ ε̂_h = c·h. Theories stable under iterated swapping fall into exactly seven
representation-theoretic families; a locally tomographic one needs local
dimension at least three ("no-pancake"); boxworld composites lose their CHSH
value under iteration. [DLG Def 1, Alg 1–2, Lemma 2, 3; DG Eq. 2, Condition 1,
Thm 9, 11, Result 13, Lemma 15]

**C14. GPT versus Vec.** Vec: one monoidal product, compact closed,
dualisability automatic. GPT: a family of products (a cone per pair, plus a
global sector without tomographic locality), duals exist as objects but ev and
coev are morphisms only if positive; "generically not compact closed". [R12,
R13, unverified] This is the crux the retired notes built on and the reason T3
(finite-dimensionality and duality of TFT values) is a constraint on cones.

## Added 2026-09-14 (distillation of BDW, BGW-G, Wilce, Tull)

**C15. Convex operational model; category of COMs.** A COM is (A, A^#, u_A):
a base-normed space with unit functional, and an effect space A^# with a
chosen regular cone A^#_+ ⊆ A^*_+ containing u_A; *saturated* if A^#_+ = A^*_+
(quantum systems are). Morphism: a positive map whose transpose is positive
for the chosen effect cones; process: u_B ∘ φ ≤ u_A; every morphism is a
positive multiple of a process. A category of COMs has hom-cones that are
regular sub-cones of the positive maps, contains I = (R, R, 1), and has
C(I, A) ≅ A, C(A, I) ≅ A^#; a monoidal category of COMs has I as unit and
A ⊗ B a locally tomographic non-signalling composite. [BDW Def 4, 8, 9, 13,
14, Def 10, 11] House: A^# = V_A^* with A^#_+ the effect cone, cone(E_A) if
restricted, (V_A^+)^* if not; C13 (iii)–(iv) is C3.

**C16. Remote evaluation; compact closure = teleportation.** For ω ∈ B ⊗ C
and f ∈ (A ⊗ B)^#, (f ⊗ 1_C)(α ⊗ ω) = ω̂(f̂(α)): the process ω̂ ∘ f̂ is
implemented by preparing α ⊗ ω and conditioning on the outcome f; conclusive
teleportation is the case C ≃ A, ω̂ ∘ f̂ ≃ 1_A. Prop 17: for a monoidal
category of COMs, (a) compact closed ⇔ (b) every A can be teleported through
some B and B through A ⇔ (c) every morphism is ω̂ ∘ f̂ for some bipartite
state and effect. Reading: "all dynamics can be induced by the kind of
conditioning that occurs in a teleportation-like protocol". [BDW Lemma 12, 15,
Rem 16, Prop 17, §6] Cl_n and Q_N yes; Box no (Result 0, project).

**C17. Weakly and symmetrically self-dual categories.** A COM is weakly
self-dual if there is an order isomorphism φ : A ≅ A^# (effect space, not
dual cone: see X6 and the narrative `qf-view-of-dualizability-and-dagger.md`
§5), symmetrically self-dual if φ(α)(β) = φ(β)(α); strongly self-dual if
the form is positive definite and A is saturated. φ^{-1} is an unnormalised
state γ ∈ A ⊗_max A, an *isomorphism state*, pure. A monoidal category of COMs
is WSD if every A has γ_A ∈ A ⊗ A and f_A ∈ (A ⊗ A)^# with f̂_A = γ̂_A^{-1},
both morphisms ("stronger than merely requiring every COM A ∈ C to be weakly
self-dual"); SSD if γ_A can be chosen symmetric. Thm 21: WSD ⇔ compact closed
with a compact structure A' = A for all A. Open (their §6): when WSD of the
objects alone gives this. [BDW §5.1, Def 18, 20, Ex 19, Thm 21] Q_N: γ is the
Choi state of the maximally entangled vector [Ex 19]. The project's condition
(b) is BDW's SSD (decision 2026-09-11; `tsirelson-...` §1).

**C18. Canonical adjoint and dagger compactness.** In a WSD category the
categorical adjoint of φ : A → B is φ' = γ̂_A^* ∘ φ^* ∘ f̂_B^*, the transpose
conjugated by the isomorphism states. Thm 27: for A in a WSD category,
φ'' = φ for all φ ∈ C(A, A) ⇔ τ_A := γ̂_A ∘ f̂_A^* = 1_A ⇔ f_A and γ_A are
symmetric bilinear forms. Thm 24 / Cor 28: a WSD category is dagger compact
for the canonical adjoint iff it is SSD. Remark after Cor 28: saturated WSD
with involutive adjoint makes int A_+ a Koecher domain of positivity; with
homogeneity, "close" to Jordan. "A dagger amounts to reversing the order of
conditioning." Open: conditions equivalent to strong self-duality. [BDW Lemma
22, 25, Cor 23, 26, Thm 24, 27, Cor 28, §6]

**C19. Isomorphism states, purity, homogeneity, steering.** ω ∈ A ⊗_max B is
an isomorphism state if ω̂ : A^* → B is an order isomorphism; on an
irreducible A, order automorphisms lie on extremal rays of the positive maps,
so isomorphism states are pure. Thm 4.1: A homogeneous ⇔ every normalised
interior state is the A-marginal of an isomorphism state in B ⊗_max A, B any
system order-isomorphic to A^*; Cor 4.2: for irreducible A, weakly self-dual
and homogeneous ⇔ every interior state is the marginal of an isomorphism state
in A ⊗_max A. Steering: ω steers its marginal if every decomposition of the
marginal is realised by conditioning on an observable on the other side;
universal uniform steering ⇒ homogeneous (Prop 5.7); universal self-steering
(from A ⊗ A) ⇒ homogeneous and weakly self-dual (Prop 5.8). "Reduces the gap
... largely to that between weak and strong self-duality." Note: the arXiv
text carries an author's bracketed note after Def 3.1 that the step from a
scaled isomorphism state to a bipartite effect "needs more argument". [BGW-G
Def 3.1, 3.2, Thm 3.3, Cor 3.5, Thm 4.1, Cor 4.2, Def 5.1, Prop 5.7, 5.8, §1]

**C20. Conjugate systems.** For a uniform model A (all basic measurements of
rank n, maximally mixed state ρ available), a conjugate is an isomorphic
model Ā with a non-signalling state η_A with η_A(x, x̄) = 1/n for every basic
outcome x, and every state the marginal of some correlating state; a *weak*
conjugate drops the second clause. η_A is an isomorphism state. Thm 1: A
sharp (each basic outcome certified by a unique state) with a conjugate ⇒
⟨a, b⟩ := η_A(a, γ_A(b)) is a self-dualising inner product on the effect
space E(A), so E(A) ≅ V(A) as ordered spaces. Cor 1: + arbitrary reversible
filters ⇒ homogeneous and self-dual, hence EJA. Cor 2: weak conjugate + all
non-singular states preparable by reversible symmetric filters ⇒ same. Thm 2:
these two packages and "A is a Jordan model" are equivalent. No no-restriction
hypothesis. Gloss: a conjugate "allows for the formation of records of the
outcomes of measurements on A in causally separated systems". [Wilce Def 1,
Lemma 2, 4, Thm 1, Cor 1, 2, Thm 2, §1] Q_N: Ā is the conjugate Hilbert
space, η_A the EPR state.

**C21. State dagger; dagger compactness from purification.** A state dagger
sends states to effects, ψ ↦ ψ̄, with id_I ↦ id_I, (ψ ⊗ φ)‾ = ψ̄ ⊗ φ̄,
(φ̄ ∘ (ψ ⊗ 1))‾ = ψ̄-of-the-other-leg, and compatibility with coherence
isomorphisms; a state dagger dual is a dual whose cap is the state dagger of
its cup. Prop 5: a dagger compact structure on a symmetric monoidal category
is the same as a state dagger with a state dagger dual for every object
(Prop 6: with discarding and completely mixed states, compatible). Thm 7:
extension from a dilating subcategory. Thm 8: CPM categories are dilation
structures with a state dagger satisfying a CP condition. Def 11 axioms:
essentially unique purification; sharpness (each causal pure state has a
unique pure co-causal certifying effect, and conversely); pure composition;
pre-duals (the completely mixed state has a purification that is a cup);
identity tomography (weaker than local tomography; holds in real QT).
Thm 13: these ⇒ dagger compact with discarding, pure morphisms a dagger
compact subcategory. Rem 14: FCStar and Rel lack purification; open. "Dagger
compact structure ... lacks a clear interpretation." [Tull Def 1, 4, 9, 11,
Prop 5, 6, Thm 7, 8, 13, Rem 14, abstract] Q_N and Q_N over R satisfy the
axioms [Ex 12].
