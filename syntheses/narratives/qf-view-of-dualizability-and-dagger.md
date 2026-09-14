---
status: draft
last-reviewed: 2026-09-14
sources:
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
  - sources/papers/080523 - teleportation in general probabilistic theories/paper.md
  - sources/papers/091230 - ensemble steering weak self-duality and the structure of probabilistic theories/paper.md
  - sources/papers/100416 - symmetry compact closure and dagger compactness for categories of convex operational models/paper.md
  - sources/papers/111016 - reversible computation determines the self-duality of quantum theory/paper.md
  - sources/papers/120613 - conjugates filters and quantum mechanics/paper.md
  - sources/papers/150722 - some nearly quantum theories/paper.md
  - sources/papers/160630 - composites and categories of euclidean jordan algebras/paper.md
  - sources/papers/170125 - categorical probabilistic theories/paper.md
  - sources/papers/180201 - reconstructing quantum theory from diagrammatic postulates/paper.md
  - sources/papers/190711 - deriving dagger compactness/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/260322 - probabilistic theories stable under teleportation/paper.md
machine-written: true
---

# The QF side: cone, unit, self-duality, compact closure, dagger

A map of what the quantum-foundations (QF) literature already knows about the
two structures the project imports from field theory, written so that a
discussion can start from familiar ground. The order is Pedro's (session of
2026-09-14): first the minimal description of a GPT, a cone of unnormalised
states completed by one unit effect; then the standard QF conditions that can
be stated at that level, weak and strong self-duality above all; then what QF
found when it added **dualizability**, i.e. compact closure of the category;
then what it found when it added a **dagger**. Statements are cited into the
filed sources by statement number; toolbox labels (G, C, X) point to
`syntheses/toolbox/`. Project results (R) are never assumed. Where two sources
use one word for two things, §5 says so.

The one-paragraph version. QF has names for both of our axioms already. For a
symmetric monoidal category of GPTs, *compact closure is equivalent to every
system being teleportable through its dual, and to every process being a
remote-evaluation protocol* [BDW Prop 17]; a category in which every system is
its own dual by an isomorphism state is compact closed, and it is *dagger
compact with respect to the canonical adjoint exactly when that isomorphism
state is a symmetric bilinear form* [BDW Thm 21, 27, Cor 28]. That symmetric
form is not an inner product; QF calls the inner-product case *strong*
self-duality and has three derivations of it (bit symmetry, a sharp dagger, a
conjugate system with sharpness) and one open problem: "to identify
operational and category-theoretic conditions equivalent to the strong
self-duality of a probabilistic theory" [BDW §6].

---

## 1. The minimal description and the conditions it supports

### 1.1 A cone and one unit effect

A system is A = (V_A, V_A^+, u_A): a finite-dimensional real vector space, a
proper cone of unnormalised states, and one strictly positive functional
[G1; P1]. Everything in the standard formalism is read off from this:
normalised states Ω_A = u_A^{-1}(1) ∩ V_A^+ [G1]; effects E_A = [0, u_A] in
the dual cone, with u_A the order unit of that cone [G3]; measurements as
finite families summing to u_A [G4]; the bipolar theorem recovering the cone
from the effects [G5]. Barnum–Duncan–Wilce say the same and add the option
the project has kept open: their *convex operational model* is a triple
(A, A^#, u_A) in which A^# carries a chosen cone A^#_+ ⊆ A^*_+ of physically
accessible effects, "generally smaller than the dual cone"; the model is
*saturated* when A^#_+ = A^*_+, "as, e.g., in the case of quantum systems"
[BDW Def 4]. Saturated is the no-restriction hypothesis [G7, X4], which the
standing assumptions leave undecided.

The unit effect is unique by construction, and this is the operational
content of *terminality*: one deterministic effect per system, every process
followed by discarding equals discarding [C5; Coecke Def 3.1; CDP Axiom 1].
A morphism is a positive map; a *process* is one with u_B ∘ φ ≤ u_A, the
probability that it occurs [BDW Def 8, 9; G8]. States are processes 1 → A,
effects processes A → 1 [C3; BDW Def 13 (iii), (iv)].

One remark of BDW is worth carrying, because the project met the same point
as result R1. The dual of a system is not automatically a system: "there is a
type issue: A has, by definition, a distinguished unit functional u_A ∈ A^#;
in order for A^# to be treated as a COM, one would need to privilege a state
α_o ∈ A to serve as an order unit on A^#. Only in special cases is there a
natural way of doing so" [BDW §5, before 5.1]. Their footnote 11 names the
special case: a symmetric state space with a group-invariant state. Our
A^∨ = (V_A^*, (V_A^+)^*, u^∨) with u^∨ "any interior point" [notation table;
R1, unverified] is this choice made arbitrarily.

### 1.2 The conditions QF states at this level

All of the following are conditions on a single cone (or a cone and its
composites), needing nothing categorical.

**Weak self-duality** [X6]. There is an order isomorphism V_A ≅ V_A^*
carrying V_A^+ onto (V_A^+)^* [BBLW §2; BGW-G Def 3.1]. BBLW's example is the
square: the dual cone "also has a square cross-section, so that the cones A_+
and A^*_+ are isomorphic. Nevertheless, A_+ is not self-dual, as A^*_+ is the
image of A_+ under a rotation by π/4" [BBLW §2]. "A far less stringent
condition than self-duality" [same]. Weak self-duality is what teleportation
needs [§2.2 below].

**Isomorphism state** [BGW-G Def 3.2]. A bipartite state ω ∈ A ⊗_max B whose
conditioning map ω̂ : A^* → B is an order isomorphism. A is weakly self-dual
iff A ⊗_max A contains one [BDW after Def 18; BGW-G §3]. On an irreducible
cone, order automorphisms are extremal among positive maps, so isomorphism
states are *pure* [BGW-G Thm 3.3, Cor 3.5]. This is the object that will
become the cup.

**Symmetric self-duality** [BDW Def 18]. The isomorphism φ : A ≅ A^# can be
chosen with φ(α)(β) = φ(β)(α), i.e. the bilinear form ⟨α, β⟩ := φ(α)(β) is
symmetric as well as non-degenerate. BDW: "for a given linear map
φ : A → A^#, the bilinear form ⟨α, β⟩ := φ(α)(β) is non-degenerate iff φ is a
linear isomorphism, and symmetric iff φ = φ^*" [BDW §5.1]. Nothing is said
about the sign of the form. This is the project's condition (b) of
`pipeline/tsirelson-from-self-duality-and-swapping.md` §1 under a published
name; see §5.

**Strong self-duality** [X7]. An inner product, positive definite, with
V_A^+ = (V_A^+)^* under it [MU "Self-duality"; BGW §2.2 "self-dualizing
inner product"; SSC Def 4.6]. BDW's own phrasing of the difference: "A will
be self-dual, in the classical sense described above, iff ⟨ , ⟩ is
positive-definite, and A^# = A^*, i.e., A is saturated. To emphasize the
distinction, we shall henceforth refer to this situation as strong
self-duality" [BDW §5.1]. Müller–Ududec, footnote 16: "In the relevant
literature, this is usually called strong self-duality, as opposed to a
certain weaker form of self-duality. However, since we do not study this
weaker notion of self-duality in this paper, we drop the prefix 'strong'"
[MU fn 16]. Consequence noted by BGW: with a self-dualising inner product,
states are represented internally as elements of the cone, and every positive
φ : A → B between self-dual systems has a positive adjoint φ^† with
⟨a, φ^†(b)⟩ = ⟨φ(a), b⟩ [BGW §2.2]. Examples: classical and quantum yes; the
square no; regular polygons iff n is odd [MU; BBLW §2; JL].

**Homogeneity** [X8] and **Koecher–Vinberg** [X9]. Aut(V_A^+) transitive on
the interior; homogeneous plus strongly self-dual is exactly a Euclidean
Jordan algebra cone [SSC Thm 4.8; BBLW §2; BGW-G §1]. BGW-G give homogeneity
an operational reading that already uses bipartite states: A is homogeneous
iff every normalised interior state is the marginal of an isomorphism state
on B ⊗_max A, B any system order-isomorphic to A^* [BGW-G Thm 4.1]; for an
irreducible A, weakly self-dual and homogeneous iff every interior state is
the marginal of an isomorphism state in A ⊗_max A [Cor 4.2]. They read this
as purification "using a fixed ancilla".

The ladder, as QF states it: weakly self-dual ⊂ symmetrically self-dual ⊂
strongly self-dual ⊂ (with homogeneity) Jordan. Bit symmetry lands on the
third rung directly [MU Thm 1; X10].

---

## 2. Dualizability, i.e. compact closure: what QF found

### 2.1 The definition, and why it is a property of the composition rule

A dual for A in a symmetric monoidal category is (A', η, ε) with the snake
identities; duals are unique up to canonical isomorphism; compact closure is
the *property* that every object has one, not the extra structure of a chosen
one, and a compact structure is *degenerate* when A' = A [BDW §2.1; C6, C7].
In Vec every object is dualisable [C7, C14]. In a category of GPTs the linear
data of the dual are forced by Vec and the whole question is positivity: is
coev a state of the chosen composite, and ev an effect on it [C7; R1, R2
unverified]. Two filed QF results make the same point from the examples:

- For Euclidean Jordan algebras with their *standard* embedding in complex
  matrix algebras (the category RSE), states of complex systems are not
  morphisms, so RSE "is very far from being compact closed" [BGW §7, Example
  6.3]; with the *universal* embedding (InvQM) the same objects form a
  compact closed, indeed dagger compact, category [BGW Thm 6.20, Cor 6.21], at
  the price that "the composite of two complex quantum systems comes with an
  extra classical bit" and local tomography fails [BGW abstract, §7]. Same
  cones, different composition rule, opposite answer.
- The quaternionic bit "cannot be added to URUE without destroying compact
  closure and the representation of states as morphisms", and non-quantum
  spin factors "are ruled out if we want to regard states as morphisms — in
  particular, if we demand compact closure" [NQ §1, Example 1]. Müller's
  lecture notes cite exactly this as the way "the old problem of how to deal
  with the tensor product of quaternionic quantum systems" is resolved,
  "by constructing dagger-compact categories of such systems" [M §3, after
  Def 16].

So QF already treats compact closure as a constraint on how systems compose,
not only on which cones there are. That is the project's Result 0 stated
from the other side: the cones of boxworld admit duals in Vec, and no
composition rule in [⊗_min, ⊗_max] makes both cup and cap positive.

### 2.2 Compact closure is teleportation is remote evaluation

The central QF theorem for the project, in BDW's words. A bipartite state ω
on B ⊗ C and a bipartite effect f on A ⊗ B compose to a process
ω̂ ∘ f̂ : A → C, and "one can implement the transformation ω̂ ∘ f̂ by
preparing the tripartite system ABC in state α ⊗ ω ... and then making a
measurement on AB, of which f is a possible outcome: the un-normalized
conditional state of C, given the effect f on AB, is exactly ω̂(f̂(α))"
[BDW Lemma 12, 15]. This is *remote evaluation*, and conclusive teleportation
is the special case C ≃ A, ω̂ ∘ f̂ ≃ 1_A [BDW §3.3]. Then:

> **Proposition 17.** Let C be a monoidal category of COMs. The following are
> equivalent. (a) C is compact closed. (b) Every A ∈ C can be teleported
> through some B ∈ C, which in turn can be teleported through A. (c) Every
> morphism in C has the form ω̂ ∘ f̂ for some bipartite state ω and bipartite
> effect f. [BDW Prop 17]

And the reading they give it: "compact closure amounts to the condition that
all processes – that is, all dynamics – can be induced by the kind of
conditioning that occurs in a teleportation-like protocol. Indeed, in such a
theory, a process between systems A and B amounts to a choice of bipartite
state on A ⊗ B" [BDW §6]; "in particular, without need to invoke any
mysterious 'collapse' of the state, nor for that matter, any other physical
dynamics at all" [BDW Rem 16].

The teleportation side has its own literature. BBLW characterise conclusive
teleportation in a regular tripartite composite: a pair (f, ω) teleports iff
the induced map is an order isomorphism up to a correction [BBLW Def 4,
Thm 1; C8]; weak self-duality is *necessary* for a composite of three copies
of a system to support it [BBLW §1, §5]; deterministic teleportation exists
in a large class of weakly self-dual, neither classical nor quantum systems
with a transitive finite group and an equivariant isomorphism [BBLW Thm 3],
so "self-duality is not necessary for deterministic teleportation" [BBLW
§5]. Their "C-self dual" system, a state η ∈ A ⊛ A with η̂ an isomorphism
and η̂^{-1} an effect, closed under ⊛ [BBLW §5], is the object BDW then make
the definition of a weakly self-dual *category*.

### 2.3 When every system is its own dual

BDW separate two things the project has also had to separate: that each cone
is weakly self-dual (an isomorphism exists in Ordlin), and that the
isomorphism and its inverse are *in the category*, as a state γ_A ∈ A ⊗ A and
a multiple of an effect f_A ∈ (A ⊗ A)^# with f̂_A = γ̂_A^{-1} [BDW Def 20].
"Note that this is stronger than merely requiring every COM A ∈ C to be
weakly self-dual" [same]. With that:

> **Theorem 21.** A monoidal category C of convex operational models is weakly
> self-dual iff it is compact closed, and can be equipped with a compact
> structure such that A' = A for all objects A ∈ C. [BDW Thm 21]

The gap between the two notions is left open by them: "it would be
interesting to investigate conditions under which this follows just from weak
self-duality of the objects" [BDW §6]. That gap is exactly the project's
C7/R2 question, positivity of coev inside one chosen composite cone, and it
is where Result 0 lives.

Two further QF statements about cups and caps, from the process-theoretic
side. Selby–Scandolo–Coecke: cups and caps "assert that the theory has
'maximal' correlations"; a non-trivial theory with cups has entangled states;
"the cap cannot be causal", so "non-trivial causal subtheories will not have
cups and caps" [SSC §2.5, Def 2.36; C6]. In house terms the cap is an allowed
morphism, never a channel. And in their framework cups and caps imply a
generalised no-restriction hypothesis [SSC Lemma 4.10; X4]. See §5 for how
this sits with BDW's restricted effect cones.

Finally, the entanglement-swapping literature builds dualisability in as
its Eq. (2): a state η ∈ D^(2) and effect ε ∈ P^(2) with η̂ ε̂ = c · id
[DG Condition 1; C13], and every one of the seven swapping-stable families
has it [DG Result 13]. Classical systems always do: R_+-Mat "always comes
with compact closed structure" [GS §"Inner product structure"; C7].

### 2.4 What QF concluded about dualizability, in one list

- It is a property of the composition rule as much as of the cones [BGW, NQ].
- It is equivalent to teleportation of every system through its dual, and to
  every process being classical conditioning on a bipartite state [BDW Prop
  17].
- Weak self-duality of each system is necessary [BBLW §5] and, once the
  isomorphism state and its inverse are morphisms, sufficient, with every
  system its own dual [BDW Thm 21].
- The causal subtheory never has it: the cap is not a channel [SSC §2.5].
- Isomorphism states are pure on irreducible cones [BGW-G Thm 3.3], and
  their availability for every interior state is homogeneity [BGW-G Thm 4.1].

---

## 3. The dagger: what QF found

### 3.1 The definition and the problem of meaning

A dagger is an identity-on-objects involutive contravariant functor; dagger
monoidal if it respects ⊗ and the symmetry; dagger compact if there is a
compact structure with η_A^† = ε_A up to the swap [BGW §6.4 "Dagger
compactness"; CHK Def 1.4, 1.5; Tull §1]. Diagrammatically it reflects a
diagram top to bottom [SSC Def 2.39; Tull (1)]. Quantum: the Hermitian
adjoint; the CPM construction transports it to mixed states and completely
positive maps [Selinger Thm 4.20; C9].

QF is candid that the dagger is the structure without an accepted reading.
Tull: "Dagger compact structure is a common assumption in the study of
physical process theories, but lacks a clear interpretation"; "the dagger
lacks a clear meaning in terms of processes" [Tull abstract, §Intro]. BDW:
dagger compactness enforces "a certain self-duality, in that there is a
bijection between the states of a system A ∈ C, represented by elements of
C(I, A), and the measurement-outcomes associated with that system,
represented by elements of C(A, I)", and in the foundational rather than
systematising mode "these strong structural assumptions need further
justification, or at any rate, further motivation" [BDW §1]. SSC call it
"time reversal" and observe that it is independent of cups and caps: cups and
caps give the transpose, the dagger gives the adjoint, and "the difference
between the transpose and the dagger is the conjugate ... Hence having a
dagger besides cups & caps is a truly fundamental structure within quantum
theory" [SSC §2.5, before Def 2.39]. Four answers have been given.

### 3.2 BDW: the dagger is the canonical adjoint, and it exists iff the isomorphism state is symmetric

In a weakly self-dual category (§2.3) every morphism has a *canonical
adjoint* φ' : B → A, and in GPT terms it is the linear transpose conjugated
by the isomorphism states, φ' = γ̂_A^* ∘ φ^* ∘ f̂_B^* [BDW Lemma 22]. It is
a dagger only if it is an involution, and:

> **Theorem 27.** For any object A in a weakly self-dual category C of convex
> operational models, the following are equivalent: (i) φ'' = φ for all
> φ ∈ C(A, A), (ii) τ_A = 1_A, (iii) f_A and γ_A are symmetric as bilinear
> forms. [BDW Thm 27; τ_A := γ̂_A ∘ f̂_A^*, Lemma 25]

> **Corollary 28.** A WSD monoidal category of COMs is dagger compact with
> respect to the canonical adjoint, if and only if it is symmetrically
> self-dual. [BDW Cor 28; Thm 24 for the forward direction]

Their reading: "As in the special case of quantum mechanics, a dagger amounts
to reversing the order of conditioning" [BDW §6]. And their next step, left
as a remark: in a *saturated* weakly self-dual theory with an involutive
adjoint, "the interior of A_+ is a domain of positivity in the sense of
Koecher", and with homogeneity "we are close" to Jordan [BDW after Cor 28].
Their closing open problem is the one the project has too: "Perhaps the most
urgent task, though, is to identify operational and category-theoretic
conditions equivalent to the strong self-duality of a probabilistic theory"
[BDW §6].

For the project this is the decisive confirmation of the 2026-09-11 decision
that unitarity gives a symmetric cone isomorphism and not an inner product
(decision log, 2026-09-11; `tsirelson-from-self-duality-and-swapping.md` §1).
The 2d Frobenius form β_Q(X, Y) = tr(XYᵀ), symmetric and indefinite, is a
symmetric self-duality in BDW's sense and is not a strong one; Cor 28 says
that this is precisely the condition for the dagger, no more.

### 3.3 BGW and SSC: the dagger from strong self-duality, and strong self-duality from a sharp dagger

The two directions of the same link.

*From an inner product to a dagger.* If A and B carry self-dualising inner
products, the transpose of a positive map is represented as a positive map
φ^† : B → A, and order automorphisms go to order automorphisms [BGW §2.2].
This is how InvQM is dagger compact: the trace inner product on each
∗-algebra is self-dualising, the dagger is the Hermitian adjoint with respect
to it, and intertwiners of the involutions stay intertwiners [BGW §6.4, Cor
6.21]. C9's remark that "a self-dual system supplies one via the inner
product" is this.

*From a dagger to an inner product.* SSC take the dagger as a postulate but
sharpen it: the dagger of a testable causal state preparation *tests* it,
and of a maximal one is causal [SSC Def 2.40, Postulate 4]; "cups & caps
being about correlations whilst the sharp dagger is about tests and
measurements" [SSC fn 4]. With a classical interface and symmetric
purification the dagger is linear [Lemma 4.1], the cone is homogeneous
[Lemma 4.3] and spectral [Lemma 4.5], and the sharp dagger *provides an inner
product* with respect to which the state cone is strongly self-dual
[SSC Lemma 4.7, Def 4.6]; Koecher–Vinberg then gives a Euclidean Jordan
algebra [Lemma 4.9] and purity of cups selects quantum theory [Prop 5.1;
X17]. In classical theory the sharp dagger is the transpose and is
constructed from the cups and caps [SSC Ex 2.42]; in quantum theory it is
the Hermitian adjoint [Ex 2.41].

### 3.4 Tull: the dagger is a state dagger, and it follows from purification

Tull reduces dagger compactness to a mapping of states to effects, ψ ↦ ψ̄,
compatible with ⊗, with the scalar identity, and with the coherence
isomorphisms; every object has a *state dagger dual*, a dual whose cap is
the state dagger of its cup:

> **Proposition 5.** Specifying a dagger compact structure on a symmetric
> monoidal category C is equivalent to specifying a state dagger for which
> every object has a state dagger dual. [Tull Def 4, Prop 5; Prop 6 with
> discarding and completely mixed states]

"In a compact category the dagger is determined by its mapping from states
(processes with no input) to effects (with no output)" [Tull §Intro]. The
dagger of a general process is then defined by bending wires through a cup
[Tull (7)]. He then derives the state dagger from operational axioms on a
category with discarding, completely mixed states and normalisation:
essentially unique *purification*, *sharpness* (for every causal pure state
a unique pure co-causal effect certifying it, and conversely), *pure
composition*, *pre-duals* (the completely mixed state has a purification
that is a cup for its dual), and *identity tomography* [Tull Def 11]:

> **Theorem 13.** Let C be a symmetric monoidal category with discarding and
> completely mixed states, satisfying normalisation and the above axioms.
> Then C forms a dagger compact category with discarding, with the pure
> morphisms C_pure as a dagger compact subcategory. [Tull Thm 13]

Sharpness "is crucial in allowing us to define a (state) dagger as a property
rather than extra structure" [Tull §5]; identity tomography "is weaker than
local tomography, since this fails in Quant_R" [same]. Along the way, CPM
categories are characterised as dilation structures with a state dagger
satisfying a CP condition [Tull Thm 8]. What is *not* covered: categories
without purification, FCStar (all finite-dimensional C*-algebras, i.e.
quantum with classical systems) and Rel, "in future it would be desirable to
derive dagger compactness in categories without such purification" [Tull
Rem 14]. So on the QF side the dagger has an operational derivation only for
theories with purification.

### 3.5 Müller–Ududec and Wilce: two more routes to the inner product

Both land on strong self-duality without naming a dagger.

*Bit symmetry* [X10]. If every pair of perfectly distinguishable pure states
can be mapped to any other by a reversible transformation, the system is
(strongly) self-dual, with an inner product invariant under the reversible
group, ⟨ω, ω⟩ = 1 on pure states and 0 between perfectly distinguishable
ones [MU Thm 1]. Their gloss: "self-duality ... can be understood from a
dynamical point of view", and bit symmetry "yields stronger restrictions on
the set of allowed bipartite states than the no-signalling principle alone,
suggesting reversible time evolution as a possible reason for limitations of
non-locality" [MU abstract]. That last sentence is the QF antecedent of the
Tsirelson question in `tsirelson-from-self-duality-and-swapping.md`.

*Conjugate systems* [Wilce]. A *conjugate* of a uniform model A is an
isomorphic model Ā with a non-signalling state η_A perfectly and uniformly
correlating every basic measurement on A with its counterpart on Ā, and with
every state the marginal of some correlating state [Wilce Def 1]. Physically,
"a conjugate system Ā allows for the formation of records of the outcomes of
measurements on A in causally separated systems, exactly as in the quantum
case" [Wilce §1]. η_A is an isomorphism state [Wilce Lemma 2], and:

> **Theorem 1.** Suppose A is sharp and has a conjugate. Then the state η_A
> gives rise to a self-dualizing inner product on E(A), with respect to which
> E(A) and V(A) are isomorphic as ordered vector spaces. [Wilce Thm 1;
> ⟨a, b⟩ := η_A(a, γ_A(b)), Lemma 4]

With arbitrary reversible filters the cone is also homogeneous, hence a
Euclidean Jordan algebra [Wilce Cor 1, 2, Thm 2], and none of this assumes the
no-restriction hypothesis [Wilce abstract]. In quantum theory "the state Ψ in
some sense explains the normalized trace inner product" [Wilce §1]. For the
project this is the one filed result in which a *cup-like state plus
sharpness* yields the *inner product*, i.e. dualizability data plus a
single-system condition forces strong self-duality. UNVERIFIED as a route
for the 2d gap; Wilce's η_A is uniformly correlating, which is more than a
cup.

### 3.6 Steering: the same objects from a third direction

Barnum–Gaebler–Wilce connect isomorphism states to Schrödinger steering. A
theory supports *universal self-steering* if every state of every A is the
marginal of a state on A ⊗ A steering for it [BGW-G §5]; then every
irreducible system is homogeneous and weakly self-dual [Prop 5.8; Prop 5.7
for uniform steering ⇒ homogeneity]. "This reduces the gap between the
generic 'self-steering' theory and quantum mechanics, largely to that between
weak and strong self-duality" [BGW-G §1]. Same gap as BDW's, same gap as
ours.

---

## 4. Summary table

| condition | what it says (house notation) | QF source | toolbox |
|---|---|---|---|
| cone + unit | A = (V_A, V_A^+, u_A); E_A = [0, u_A]; one deterministic effect | P Def 2.1, Prop 3.10; BDW Def 4; Coecke Def 3.1 | G1, G3, C5 |
| restricted effects | A^#_+ ⊆ (V_A^+)^*; saturated = no-restriction | BDW Def 4; P §3.7 | G7, X4 |
| weakly self-dual | order iso V_A ≅ V_A^*, V_A^+ ↦ (V_A^+)^* | BBLW §2; BGW-G Def 3.1 | X6 |
| isomorphism state | ω ∈ A ⊗_max B with ω̂ : V_A^* → V_B an order iso; pure if irreducible | BGW-G Def 3.2, Thm 3.3 | C19 |
| symmetrically self-dual | the iso V_A → effect space is a symmetric bilinear form | BDW Def 18, 20 | C17 |
| strongly self-dual | positive definite, and saturated | MU; BGW §2.2; BDW §5.1; SSC Def 4.6 | X7 |
| homogeneous | Aut(V_A^+) transitive on interior ⇔ interior states are marginals of isomorphism states | SSC Def 4.2; BGW-G Thm 4.1 | X8, C19 |
| compact closed | every A has a dual with snake identities ⇔ teleportation ⇔ remote evaluation | BDW §2.1, Prop 17; SSC Def 2.36 | C6, C7, C16 |
| WSD category | γ_A ∈ A ⊗ A isomorphism state, f_A its inverse, both morphisms ⇔ degenerate compact closed | BDW Def 20, Thm 21 | C17 |
| dagger compact (canonical adjoint) | ⇔ γ_A symmetric | BDW Thm 24, 27, Cor 28 | C18 |
| dagger from inner product | φ^† via self-dualising inner products | BGW §2.2, Cor 6.21 | C9 |
| sharp dagger ⇒ strong SD | dagger tests states ⇒ inner product ⇒ EJA | SSC Def 2.40, Lemma 4.7 | X17 |
| state dagger | dagger compactness ⇔ states ↦ effects with state dagger duals; from purification + sharpness | Tull Prop 5, Thm 13 | C21 |
| bit symmetry ⇒ strong SD | reversible maps transitive on bits | MU Thm 1 | X10 |
| conjugate + sharp ⇒ strong SD | uniformly correlating η_A gives the inner product | Wilce Thm 1 | C20 |
| self-steering ⇒ homogeneous WSD | every state steered from A ⊗ A | BGW-G Prop 5.8 | C19 |

---

## 5. Where the sources diverge, and one proposal

**"Weakly self-dual" means two things.** BBLW and BGW-G compare the state
cone with the *dual* cone, V_A^+ ≅ (V_A^+)^* [BBLW §2; BGW-G Def 3.1]; the
glossary follows them [X6]. BDW compare the state space with the *effect
space* A^#, which may be a proper sub-cone of the dual cone [BDW Def 4,
Def 18]. The two coincide under no-restriction and differ otherwise, and the
difference is live in the project: Dmello–Gross's families and OST have
restricted effect cones, and the 2d Frobenius form lands on the effect cone
(`tsirelson-from-self-duality-and-swapping.md` §1). When reading a source,
check which.

**Proposal (for Pedro; conventions are his).** Adopt BDW's term
*symmetrically self-dual* for the project's condition (b), "a symmetric order
isomorphism of the state cone onto the effect cone", and record in the
glossary that it sits strictly between weak and strong self-duality. It is a
published name for exactly the condition unitarity gives [BDW Def 18, Cor 28;
decision of 2026-09-11].

**Cups and caps versus restricted effects.** SSC derive a generalised
no-restriction hypothesis from cups and caps [SSC Lemma 4.10]; BDW build
compact closed categories of models with restricted effect cones A^#_+ [BDW
Def 4, 13, Thm 21]. UNVERIFIED whether the two are in tension: SSC's lemma
uses their classical interface and their notion of "physically possible",
and BDW's Def 13 (i) lets the hom-cones be any regular sub-cones, so the
frameworks may simply differ on what "all effects" ranges over. Nobody has
checked. Relevant because the standing assumptions leave no-restriction open.

**Three readings of the dagger, none agreed.** BDW: "reversing the order of
conditioning" [§6]. SSC: "time reversal", made operational as testing [Def
2.39, 2.40]. Tull: no clear meaning, hence derive it [abstract]. The
project's reading, a region read from either end
(`spacetime-reading-of-the-axioms.md` Part 2), is a fourth, and it is
closest to SSC's. None of the three QF readings mentions spacetime.

**One editorial note in a source.** BGW-G's arXiv text carries, after Def
3.1, an author's bracketed note that a step "needs more argument" (whether
η^{-1} is a bipartite effect once η is scaled to a state). Read Def 3.1 and
the sentence after it with that in mind; BDW Def 20 sidesteps it by
*requiring* f_A to be a morphism.

---

## 6. What this gives the project

- Both axioms have QF statements. Dualizability = compact closure =
  teleportation through the dual = every process is remote evaluation [BDW
  Prop 17]. Unitarity with a GPT target = dagger compactness for the canonical
  adjoint = symmetric self-duality of every system [BDW Cor 28]. Neither is an
  inner product.
- The gap the project has, from symmetric to strong self-duality
  (`tsirelson-from-self-duality-and-swapping.md` §4), is the gap QF names as
  open [BDW §6; BGW-G §1]. QF's routes across it are bit symmetry [MU Thm 1],
  a sharp dagger [SSC Lemma 4.7], a conjugate with sharpness [Wilce Thm 1],
  purification with sharpness [Tull Thm 13]. The project's route is different
  in kind: positivity of the 2d algebra [OST Lemma 4.1, in one family]. Whether
  any QF route can be read off the bordism category is open.
- The QF side has no spacetime reading of either structure. Its readings are
  informational (teleportation, conditioning, records, tests, purification).
  That is the space the paper's B8 is meant to fill, and this file is the
  record of what it must not claim as new.

## Sources

Filed, cited by statement number: `100416` Barnum–Duncan–Wilce (BDW);
`080523` Barnum–Barrett–Leifer–Wilce (BBLW); `091230` Barnum–Gaebler–Wilce
(BGW-G); `160630` and `150722` Barnum–Graydon–Wilce (BGW, NQ); `180201`
Selby–Scandolo–Coecke (SSC); `190711` Tull; `111016` Müller–Ududec (MU);
`120613` Wilce; `170125` Gogioso–Scandolo (GS); `210312` Plávala (P);
`201102` Müller (M); `260322` Dmello–Gross (DG); `130516`
Coecke–Heunen–Kissinger (CHK); `050000` Selinger. Project: decision log
2026-09-11; `pipeline/tsirelson-from-self-duality-and-swapping.md` §1, §4;
`pipeline/spacetime-reading-of-the-axioms.md`; `paper/results-structure.md`
Result 0.
