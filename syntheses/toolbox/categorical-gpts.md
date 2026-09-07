---
status: draft
last-reviewed: 2026-09-07
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
machine-written: true
---

# Toolbox: categorical GPTs

The category of GPTs in house notation, with the categorical definitions the
literature adds on top of it, each illustrated on Cl_n, Q_N and Box. Sources
by statement number: Selby–Scandolo–Coecke (SSC), Gogioso–Scandolo (GS),
Barnum–Graydon–Wilce (BGW; NQ for "Some nearly quantum theories"),
Barnum–Barrett–Leifer–Wilce (BBLW), Coecke, Dmello–Ligthart–Gross (DLG),
Dmello–Gross (DG), Carqueville–Runkel (CR). Project results from the retired
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
