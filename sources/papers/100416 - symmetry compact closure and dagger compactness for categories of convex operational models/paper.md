---
type: paper
date: 2010-04-16
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1004.2920v1)
reviewed: false
---

# Symmetry, Compact Closure and Dagger Compactness for Categories of Convex Operational Models

Machine-generated and unreviewed text extraction of arXiv:1004.2920v1
(17 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1004.2920v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Symmetry, Compact Closure and Dagger Compactness for
Categories of Convex Operational Models

arXiv:1004.2920v1 [quant-ph] 16 Apr 2010

Howard Barnum∗, Ross Duncan†and Alexander Wilce‡
April 13, 2010

Abstract
In the categorical approach to the foundations of quantum theory, one begins with a symmetric
monoidal category, the objects of which represent physical systems, and the morphisms of which
represent physical processes. Usually, this category is taken to be at least compact closed, and
more often, dagger compact, enforcing a certain self-duality, whereby preparation processes (roughly,
states) are interconvertible with processes of registration (roughly, measurement outcomes). This
is in contrast to the more concrete “operational” approach, in which the states and measurement
outcomes associated with a physical system are represented in terms of what we here call a convex
operational model: a certain dual pair of ordered linear spaces – generally, not isomorphic to one
another. On the other hand, state spaces for which there is such an isomorphism, which we term
weakly self-dual, play an important role in reconstructions of various quantum-information theoretic
protocols, including teleportation and ensemble steering.
In this paper, we characterize compact closure of symmetric monoidal categories of convex operational models in two ways: as a statement about the existence of teleportation protocols, and as
the principle that every process allowed by that theory can be realized as an instance of a remote
evaluation protocol — hence, as a form of classical probabilistic conditioning. In a large class of cases,
which includes both the classical and quantum cases, the relevant compact closed categories are degenerate, in the weak sense that every object is its own dual. We characterize the dagger-compactness
of such a category (with respect to the natural adjoint) in terms of the existence, for each system, of
a symmetric bipartite state, the associated conditioning map of which is an isomorphism.

1. Categorical Semantics and Quantum Foundations
One natural way to formalize a physical theory is as some kind of category, C, the objects of which
are the systems, and the morphisms of which are the processes, contemplated by that theory. In order to
provide some apparatus for representing compound systems, it is natural to assume further that C is a
symmetric monoidal category. In the categorical semantics for quantum theory pioneered by Abramsky
and Coecke [1], Selinger [38, 37], and others (e.g., [2, 3, 7, 17]), it is further assumed that C is at least
compact closed, and more usually, dagger compact. This last condition enforces a certain self-duality,
in that there is a bijection between the states of a system A ∈ C, represented by elements of C(I, A),
and and the measurement-outcomes associated with that system, represented by elements of C(A, I).
The motivating example here is the category FDHilb of ﬁnite-dimensional complex Hilbert spaces and
unitary mappings — that is, the category of ﬁnite-dimensional “closed” quantum systems and unitary
processes. Many of the information-processing features of ﬁnite-dimensional quantum systems occur in
any dagger-compact category, notably, conclusive (that is, post-selected) teleportation and entanglementswapping protocols. On the other hand, if our interest in a categorical reformulation of quantum theory
is mainly foundational, rather than strictly one of systematization, these strong structural assumptions
need further justiﬁcation, or at any rate, further motivation.
∗ Perimeter Institute for Theoretical Physics hbarnum@perimeterinstitute.ca
† Oxford University Computing Laboratory, ross.duncan@comlab.ox.ac.uk
‡ Department of Mathematics, Susquehanna University, wilce@susqu.edu

1

<!-- page 2 -->
There is an older tradition, stemming from Mackey’s work on the foundations of quantum mechanics
[35], in which an individual physical (or, more generally, probabilistic) system is represented by a set of
states, a set of observables or measurements, and an assignment of probabilities to measurement outcomes,
conditional upon the state. From this basic idea, one is led to a representation of systems involving pairs
of ordered real vector spaces — the convex operational models of our title — and of physical processes,
by certain positive linear mappings between such spaces. The motivating example is the category of
Hermitian parts of C ∗ algebras and completely positive mappings.
This “convex operational” approach, in contrast to the categorical one, is conservative of classical
probabilistic concepts, but liberal as to how systems may be combined and transformed, so long as this
probabilistic content is respected. In particular, there is no standing assumption of monoidality; rather,
systems are combined using any of a variety of “non-signaling” products. Nor is there, in general, any hint
of the kind of self-duality mentioned above — indeed, the natural dual object for a convex operational
model is not itself an operational model. Nevertheless, here again various familiar “quantum” phenomena
– such as no-cloning and no-broadcasting theorems, information-disturbance tradeoﬀs, teleportation and
entanglement swapping protocols, and ensemble steering – emerge naturally and in some generality
[15, 8, 9, 12]. A key idea here is that of a remote evaluation protocol [9] (of which teleportation is a
special case), which reduces certain kinds of dynamical processes to purely classical conditioning.
It is obviously of interest to see how far such convex operational theories can be treated formally,
that is, as categories, and more especially, as symmetric monoidal categories; equally, one would like to
know how much of the special structure assumed in the categorical approach can be given an operational
motivation.1 Some ﬁrst steps toward addressing these issues are taken in [13, 14]. Here, we aim to make
further progress, albeit along a somewhat narrower front. We focus on symmetric monoidal categories of
convex operational models – what we propose to call probabilistic theories. We show that such a theory
admits a compact closed structure if and only if every system allowed by the theory can be teleported
(conclusively, though not necessarily with probability 1) through a copy of itself – or, equivalently, if
and only if every process contemplated by the theory can be represented as a remote evaluation protocol
involving a copy of itself. We then specialize further, to consider weakly self-dual theories, in which for
every system A there is a bipartite state γA on A ⊗ A corresponding to an isomorphism between A and
its dual, and an eﬀect corresponding to its inverse. (Such state spaces ﬁgure heavily in earlier treatments
of teleportation protocols [9] and ensemble steering [12] in general probabilistic theories.) We show that
if the state implementing weak self-duality can be chosen to be symmetric for every A, then a weakly
self-dual monoidal probabilistic theory is not merely compact closed, but dagger compact.
Organization and Notation Sections 2 and 3 provide quick reviews of the category-theoretic and the
convex frameworks, respectively, mainly following [1] for the former and [8, 9, 12, 13, 14] for the latter.
Section 4 makes precise what we mean by a monoidal probabilistic theory, as a symmetric monoidal
category of convex operational models, and establishes that all such theories have the property of allowing
remote evaluation [9]; when the state spaces involved are weakly self-dual, teleportation arises as a special
case. Section 5 contains the results on categories of weakly self-dual state spaces described above. Section
6 discusses some of the further ramiﬁcations of these results.
We assume that the reader is familiar with basic category-theoretic ideas and notation, as well as with
the probabilistic machinery of quantum theory. We write C, D etc. for categories, A ∈ C, to indicate that
A is an object of C, and C(A, B) for the set of morphisms between objects A, B ∈ C. Except as noted,
all vector spaces considered here will be ﬁnite-dimensional and real. We write VecR for the category of
ﬁnite-dimensional real vector spaces and linear maps. The dual space of a vector space A is denoted by
A∗ . An ordered vector space is a real vector space V equipped with a regular — that is, closed, convex,
pointed, generating — cone V+ , and ordered by the relation x ≤ y ⇔ y − x ∈ A+ . A linear mapping
φ : V → W between ordered linear spaces V and W is positive if φ(V+ ) ⊆ W+ . We write L+ (A, B)
for the cone of positive linear mappings from A to B. The special case in which B = R, the positive
linear functionals on A, is the dual cone of A+ , denoted A∗+ . The category of ordered linear spaces and
positive linear maps we denote by Ordlin. Finally, we make the standing assumption that, except where
otherwise indicated, all vector spaces considered here are finite dimensional.
1 That some motivation is needed is clear in view of a result, to appear elsewhere, that any of a broad class of symmetric
monoidal categories can be interpreted as categories of convex operational models.

2

<!-- page 3 -->
Acknowledgements HB and AW wish to thank Samson Abramsky and Bob Coecke for enabling them to
visit the Oxford University Computing Laboratory in November 2009, where some of this work was done,
and for helpful discussions during that time. The authors also wish to thank Peter Selinger for helpful
discussions. RD is supported by EPSRC postdoctoral research fellowship EP/E04006/1. HB’s research
was supported by Perimeter Institute for Theoretical Physics; work at Perimeter Institute is supported
in part by the Government of Canada through Industry Canada and by the Province of Ontario through
the Ministry of Research and Innovation.
2. The Category-Theoretic Perspective
A monoidal category [36] is a category C equipped with a bifunctor2 ⊗ : C × C → C, a distinguished
unit object I, and natural associativity and left and right unit deletion isomorphisms,
αA,B,C : A ⊗ (B ⊗ C) ∼
= (A ⊗ B) ⊗ C,
λA : I ⊗ A ∼
= A,

ρA : A ⊗ I ∼
= A,

subject to some coherence conditions (for which, see [36]). If these isomorphisms are identities, the
category is called strict monoidal. Every monoidal category is equivalent to a strict one, so setting
A ⊗ I = A etc, is harmless and we will do this throughout.
A symmetric monoidal category (SMC) is a monoidal category further equipped with a natural family
of symmetry isomorphisms,
σA,B : A ⊗ B ∼
= B ⊗ A,

again, subject to some coherence conditions (for which, again, see [36]). Unlike the other isomorphisms,
these symmetry isomorphisms cannot generally be made strict.
Examples of SMCs include commutative monoids (as one-object categories), the category of sets and
mappings (with A ⊗ B = A × B), and – of particular relevance for us – the category of (say, ﬁnitedimensional) vector spaces over a ﬁeld K and K-linear maps, with A ⊗ B the usual tensor product.
Another source of examples comes from logic: one can regard the set of sentences of a logical calculus
as a category, with proofs, composed by concatenation, as morphisms. In this context, one can take
conjunction, ∧, as a monoidal product.
Much more broadly, if somewhat less precisely, if one views the objects of a category C as “systems”
(of whatever sort), and morphisms as “processes” between systems, then a natural interpretation of the
product in a symmetric monoidal category is as a kind of accretive composition: A ⊗ B is the system
that consists of the two systems A and B sitting, as it were, side by side, without any special interaction;
f ⊗ g represents the processes f : A → X and g : A → Y acting in parallel. Taking this point of view, it
is helpful to regard processes of the form I → A, where I is the monoidal unit in C, as states, associated
with ways of preparing the system A. Similarly, we regard processes of the form a : A → I as “eﬀects”,
or measurement-outcomes. We shall henceforth adhere to the convention of denoting states by lower-case
Greek letters α, β, ... and eﬀects, lower-case Roman letters a, b, ....
In any monoidal category, one can regard endomorphisms s ∈ C(I, I) as “scalars” acting on elements
of C(A, B) by sx = s ⊗ x. In every monoidal category, C(I, I) is a commutative monoid, even if C is not
symmetric. When C(I, I) is isomorphic to a particular monoid S, we shall say that C is a symmetric
monoidal category over S.
2.1 Compact Closed Categories
A dual for an object A of a symmetric monoidal category C is an object B and two morphisms, the
unit, η : I → B ⊗ A (not to be confused with the tensor unit I) and the co-unit, ǫ : A ⊗ B → I, such that
A
B

1A ⊗η
η⊗1B

/ A⊗B ⊗A
/ B ⊗A⊗B

ǫ⊗1A
1B ⊗ǫ

/ A = 1A

2 Bifunctoriality means that: (i) 1
A⊗B = 1A ⊗ 1B ; and (ii) given morphisms f : A → X and g : B → Y
canonical product morphism f ⊗ g : A ⊗ B → X ⊗ Y , such that (f ⊗ g) ◦ (f ′ ⊗ g ′ ) = (f ◦ f ′ ) ⊗ (g ◦ g ′ ).

3

(1)

/ B = 1B .
in C, there is a

<!-- page 4 -->
Duals are unique up to a canonical isomorphism. Indeed, if (B1 , η1 , ǫ1 ) and (B2 , η2 , ǫ2 ) are duals for
A, then φ := (1B2 ⊗ ǫ1 ) ◦ (η2 ⊗ 1B1 ) : B1 → B2 has inverse φ−1 = (1B1 ⊗ ǫ2 ) ◦ (η1 ⊗ 1B2 ); moreover,
η2 = (φ ⊗ 1A ) ◦ η1 . Some, for example the authors of [17], use the term compact structure to refer to what
we are calling a dual, i.e., a particular choice of (A′ , ηA , ǫA ) for a given object A ∈ C or, when applied to
a category, a particular choice of dual for each object.
A symmetric monoidal category C is compact closed 3 if for every object A in the category, there is a
dual, (A′ , ηA , ǫA ), where A′ is an object of the category.4 As thus deﬁned, compact closedness is a property
of the SMC C, not an additional structure: it requires the existence of at least one dual for each object, but
not the explicit speciﬁcation of a distinguished one. The alternative deﬁnition of compact closed category,
which diﬀers only in requiring a choice of duals be speciﬁed [32], is perhaps more common. Owing to the
uniqueness up to isomorphism mentioned above, the various possible choices of duals are largely—but not
entirely—equivalent. A compact structure is said to be degenerate iﬀ A′ = A; a compact closed category
C with a distinguished compact structure is said to be degenerate if every object’s compact structure is
degenerate. This does depend on an explicit choice of duals, and thus imposes some non-trivial structure
beyond compact closure. This is the setting that will most interest us below.
Remark 1. If (A′ , ηA , ǫA ) and (B ′ , ηB , ǫB ) are duals for objects A, B ∈ C, then we can construct a
canonical dual (A′ ⊗ B ′ , ηAB , ǫAB ) for A ⊗ B by setting ηAB = τ ◦ (ηA ⊗ ηB ) and ǫAB = (ηA ⊗ ηB ) ◦ τ −1 ,
where
τ = 1A′ ⊗ σAB ′ ⊗ 1B : (A′ ⊗ A) ⊗ (B ′ ⊗ B) ≃ (A′ ⊗ B ′ ) ⊗ (A ⊗ B).

Since all duals are isomorphic we are free to assume that A ⊗ B has this particular dual. 5

In any compact closed category, an assignment A 7→ A′ extends to a contravariant functor (−)′ :
C → C, called the adjoint, taking morphisms φ : A → B to φ′ : B ′ → A′ deﬁned by:
op

B′

ηA ⊗1B ′

/ A′ ⊗ A ⊗ B ′

φ′


A′ o

′

(2)

1A′ ⊗φ⊗1B ′


A′ ⊗ B ⊗ B ′ .

1A′ ⊗ǫB

The functor ′ is nearly involutive, in that there are natural isomorphisms wA : A′′ → A. To say that
is involutive is just to say that A′′ = A and φ = φ′′ ; note that this does not imply that wA = 1A .

Remark 2. In the classic treatment of coherence for compact closed categories in [32], one has that
σ ◦ ηA = (1A ⊗ wA ) ◦ ηA′ ; a similar condition holds for ǫ ([32], eq. (6.4)ﬀ.). In the case of a degenerate
category, this implies that
σ ◦ ηA = (1A ⊗ wA ) ◦ ηA .
(3)
It is easy to show that if the units – or, equivalently, co-units – are symmetric, in the sense that, for
every object A ∈ C, ηA = σA,A ◦ ηA or, equivalently, ǫA = ǫA ◦ σA,A , then the the functor ′ is involutive.
However the converse does not necessarily hold, unless wA = 1A . In general, it is not clear what coherence
requirements are appropriate for the degenerate categories we consider, nor whether the functors involved
are always strict. Therefore, in Section 5 we will establish explicitly that the involutiveness of the adjoint is
equivalent to the symmetry of the unit and co-unit for the compact closed categories of convex operational
models considered in this paper.
Remark 3. For an arbitrary degenerate compact closed category, there is no guarantee that the unit ηA
will be symmetric. (We thank Peter Selinger [39] for supplying a nice example involving a category of
plane tangles.) Thus, it is a non-trivial constraint on such a category that the canonical adjoint be an
involution. This will be important below.
3 Sometimes just compact.
4 We use the notation A′ , rather than the more standard A∗ , for the designated dual of an object in a compact closed

category, because we wish to reserve the latter to denote, specifically, the dual space of a vector space.
5 Technically, this depends on the ability to factor objects uniquely as tensor products; however, all categories ordinarily
considered in this context have this property. The fact that the symmetry isomorphism can’t generally be made strict is
relevant here.

4

<!-- page 5 -->
2.2 Daggers
A dagger category [38, 1] is a category C together with an involutive functor (−)† : C op → C that acts
as the identity on objects. That is, A† = A for all A ∈ C, and, if f ∈ C(A, B), then f † ∈ C(B, A), with
(g ◦ f )† = f † ◦ g †

and f †† = f

for all f ∈ C(A, B) and g ∈ C(B, C).6 We say that f is unitary iﬀ f † = f −1 . A dagger-monoidal category
is a symmetric monoidal category with a dagger such that (i) all the canonical isomorphisms deﬁning the
symmetric monoidal structure are unitary, and (ii)
(f ⊗ g)† = f † ⊗ g †
for all morphisms f and g in C. Finally, a dagger-monoidal category C is dagger compact if it is compact
closed and
ηA = σA,A′ ◦ ǫ†A
for every A, i.e.:
A ⊗ A′
n7
n
n
nn
nnn
σ
I PPP η
PPPA
PP'

A′ ⊗ A
ǫ†A

commutes. In the case of a degenerate compact closed category, the canonical adjoint ′ functions as a
dagger if it is involutive. However, as remarked above, this is a nontrivial condition.
In the work of Abramsky and Coecke [1], a symmetric monoidal category is interpreted as a physical
theory, in which a morphism α : I → A is interpreted, as discussed above, as representing a state of the
system A; a morphism b = β † : A → I is understood as the registration of an eﬀect — e.g., a measurement
outcome — associated with A. The scalar β † ◦ α : I → I is understood, somewhat ﬁguratively in the
abstract setting, as the “probability” that the given eﬀect will occur when the given state obtains.7 This
raises the obvious question of how to implement the compelling idea that probabilities should be identiﬁed
with real numbers in the interval [0, 1] without passing through Hilbert space. One way to do this is
simply to posit a mapping p : C(I, I) → [0, 1], whereby the scalars of C can be interpreted probabilistically.
Another is to examine the symmetric monoidal possibilities in cases in which the category consists, ab
initio, of concretely described probabilistic models of a reasonably simple and general sort. In this paper,
we concentrate on this second strategy. As a ﬁrst step, in the next section we describe the kinds of
concrete probabilistic models we have in mind.
3. Convex Operational Models and their Duals
The more traditional approach to modeling probabilistic physical theories [35, 16] begins by associating
to each individual physical (or other probabilistic) system a triple (X, Σ, p) – sometimes called a Mackey
triple — where Σ is a set of possible states, X is a set of possible measurement-outcomes, and p : X ×Σ →
[0, 1] assigns to each pair (x, s) the probability, p(x, s), that x will occur, if measured, when the system’s
state is s.
This minimal apparatus can be “linearized” in a natural way. The probability function p gives us a
mapping Σ → [0, 1]X , namely s 7→ p(·, s). We can plausibly identify each state s ∈ Σ with its image under
this mapping (thus identifying states if they cannot be distinguished statistically by the outcomes in X).
Having done so, let Ω denote the point-wise closed, and hence compact, convex hull of Σ ⊆ [0, 1]X . This
represents the set of possible probabilistic mixtures of states in Σ, in so far as these can be distinguished
by outcomes in X. Every measurement outcome x ∈ X can now be represented by the aﬃne evaluation
6 Those new to categories should note that a functor from C op to C is sometimes called a contravariant functor from
C → C; the description we have just given (minus the involutiveness condition) defines this notion without reference to C op .
7 We can be more precise here: given a dagger-compact category of states and processes C, any dagger-monoidal functor
from C to FDHilb, the category of finite dimensional Hilbert spaces, will send the scalar β † ◦ α to the inner product hβ | αi.

5

<!-- page 6 -->
functional ax : Ω → [0, 1], given by ax (α) = α(x) for all α ∈ Ω. More broadly, we can regard any
aﬃne functional a : Ω → [0, 1] as representing a mathematically possible measurement outcome, having
probability a(α) in state α ∈ Ω. Such functionals are called effects in the literature.
In general, the (mixed) state space Ω that we have just constructed will have inﬁnite aﬃne dimension.
Accordingly, for the next few paragraphs, we suspend our standing ﬁnite-dimensionality assumption.
Now, any compact convex set Ω can be embedded, in a canonical way, as a base for the positive cone
V+ (Ω) of a regularly ordered linear V (Ω) [4]. This means that every ρ ∈ V+ (Ω) has the form ρ = tα for
a unique scalar t ≥ 0 and a unique vector α ∈ Ω (hence, Ω spans V (Ω)). This space V (Ω) is complete
in a natural norm, the base norm, the unit ball of which is given by the closed convex hull of Ω ∪ −Ω.
Moreover, V (Ω) has the following universal property: every bounded aﬃne mapping L : Ω → M, where
M is any real Banach space, extends uniquely to a bounded linear mapping L : V (Ω) → M.
In particular, every aﬃne functional on Ω – in particular, every eﬀect – extends uniquely to a linear
functional in V (Ω)∗ . In particular, there is a unique unit functional uΩ ∈ V (Ω)∗ such that uΩ (α) = 1
∗
for α ∈ Ω, and Ω = u−1
Ω (1) ∩ V+ (Ω). Thus, eﬀects correspond to positive functionals a ∈ V (Ω) with
0 ≤ a ≤ uΩ .
One often regards any eﬀect a ∈ V (Ω)∗ as a bona fide measurement outcome. This is the point of view,
e.g., of [8, 9]. However, we may sometimes wish to privilege certain eﬀects as “physically accessible”.
This suggests the following more general formulation:
Definition 4. A convex operational model (COM) is a triple (A, A# , uA ) where
(i) A is a complete base-normed space with (strictly positive) unit functional uA , and
∗
(ii) A# is a weak-∗ dense subspace of A∗ , ordered by a chosen regular cone A#
+ ⊆ A+ containing uA .

An effect on A is a functional a ∈ A#
+ with a ≤ uA .
Henceforth, where no ambiguity seems likely, we write A for the triple (A, A# , uA ). Also, we now revert,
for the balance of this paper, to our standing assumption that all COMs are finite-dimensional. In this
case, the weak-∗ density assumption above simply says that A# = A∗ , so that A# = A∗ as vector spaces.
∗
Even in this situation, however, the chosen cone A#
+ will generally be smaller than the dual cone A+ , so
# ∗
the positive cone (A )+ will in general be larger than A+ . It is useful to regard normalized elements of
the former cone as mathematically consistent probability assignments on the eﬀects in A# , from which
∗
the model singles out those in A+ as physically possible. In the special case in which A#
+ = A+ — as,
e.g., in the case of quantum systems — we shall say that the COM A is saturated.
Example 5. Let E be a ﬁnite set, thought of as the outcome set for a discrete classical
experiment.
P
Take A = RE , with A+ the cone of non-negative functions on E, and let uA (f ) = x∈E f (x). Then
Ω = u−1 (1) is simply the set of probability weights on E. Geometrically, this last is a simplex. In ﬁnite
dimensions, every simplex has this form. Accordingly, we say a COM is classical iﬀ its normalized state
space is a simplex.
Example 6. Let H be a ﬁnite-dimensional complex Hilbert space, and let A = Lh (H), the space of
Hermitian operators a : H → H, with the usual positive cone, i.e, A+ consists of all Hermitian operators
of the form a† a. Let uA (a) = Tr(a). Then ΩA is the convex set of density operators on H, i.e., the usual
space of mixed quantum states.
Example 7. Let (X, Σ, p) be any Mackey triple. Construct the state-space Ω and the associated ordered
∗
Banach space V (Ω) as described above. Letting A#
+ be the cone in V (Ω) generated by the evaluation
functionals ax , x ∈ X, we have a convex operational model. This will be ﬁnite-dimensional iﬀ the span
of (the image of) Σ in RX is ﬁnite dimensional.
3.1 Processes as Positive Mappings
Definition 8. A morphism of COMs from (A, A# , uA ) to (B, B # , uB ) is a positive linear map φ : A → B
such that the usual linear adjoint map φ∗ : B ∗ → A∗ is positive with respect to the designated cones A#
+
#
and B+
.
6

<!-- page 7 -->
The set of morphisms of COMs from A to B is clearly a sub-cone of L+ (A, B). It is clear that the
composition of two mappings of COMs is again a mapping of COMs, so that COMs form a concrete
category.
Definition 9. Let A and B be COMs. A process from A to B is a morphism φ : A → B such that, for
every state α ∈ ΩA , uB (φ(α)) ≤ 1, or, equivalently, if φ∗ (uB ) ≤ uA .
If φ : A → B is a process, we can regard uB (φ(α)) as the probability that the process represented
by φ occurs. If we regard R as an COM with uR the identity mapping on R, this is consistent with our
understanding of a(α) as the probability of the eﬀect a : A → R occurring. Notice that a positive linear
map φ : R → A is a process if and only if φ(1) is a sub-normalized state, while a positive functional
f : A → R is a process if and only if f ∈ A#
+ and f ≤ uA – in other words, if and only if f is an eﬀect.
Finally, since ΩA is compact, uA (φ(α)) attains a maximum value, say M on ΩA . M −1 φ is a process, so
every morphism of COMs is a positive multiple of a process.
3.2 Bipartite States and Composite Systems
Given two separate systems, represented by COMs A and B, we should expect that any state of the
composite system AB will induce a joint probability assignment p(a, b) on pairs of eﬀects a ∈ A# , b ∈ B # .
If the two systems can be prepared independently, we should also suppose that, for any two states α ∈ A
and β ∈ B, the product state α ⊗ β, given by (α ⊗ β)(a, b) = α(a)β(b), will be a legitimate joint state.
Finally, if the two systems do not interact, the choice of measurement made on A ought not to inﬂuence
the statistics of measurement outcomes on B, and vice versa. This latter “no-signaling” condition is
equivalent [43] to the condition that the joint probability assignment p extends to a bilinear form on
A# × B # , normalized so that p(uA , uB ) = 1. Abstractly, then, one makes the following deﬁnition.
Definition 10. A (normalized, non-signaling) bipartite state between convex operational models A and
B is a bilinear form ω : A# × B # → R that is positive, in the sense that ω(a, b) ≥ 0 for all eﬀects a ∈ A#
and b ∈ B # , and normalized (satisﬁes ω(uA , uB ) = 1).
Implicit in this deﬁnition is the assumption, lately called local tomography [18], that a joint state
is determined by the joint probabilities it assigns to measurement outcomes associated with the local
systems A and B. As has been pointed out by many authors, e.g. [6, 33, 15], this condition is violated in
both real and quaternionic quantum theory, and can therefore be made to serve as an axiom separating
standard complex QM from these. A more general notion of non-signaling bipartite state would merely
associate, rather than identify, each such state with a positive bilinear form on A# × B # . See the remarks
following Deﬁnition 11 for more on this.
It is clear that any product ω = α ⊗ β of normalized states α ∈ A and β ∈ B deﬁnes a non-signaling
state; hence, so do convex combinations of product states. Non-signaling states arising in this way, as
mixtures of product states, are said to be separable or unentangled. An entangled non-signaling state
is one that is not a convex combination of product states. Many of the basic properties of entangled
quantum states actually hold for entangled states in this much more general setting [33, 8].
The space B(A# , B # ) of all bilinear forms on A# × B # , ordered by the cone of all positive bilinear
forms, is the maximal tensor product, A ⊗max B, of A and B. This notation is reasonable, since (in ﬁnite
dimensions), B(A# , B # ) is one model of the tensor product (A# )∗ ⊗ (B # )∗ — thus, of the vector-space
tensor product A ⊗ B.8 Ordering A ⊗ B instead by the generally much smaller cone of unentangled
states, that is, the cone generated by the product states, gives the minimal tensor product, A ⊗min B.
It is important to note that these coincide only when A or B is classical [8]. If A and B are quantum
state spaces, then the cone of bipartite density matrices for the composite system lies properly between
the maximal and minimal cones. This indicates the need for something more general:
Definition 11. A (locally tomographic) composite of COMs A and B is a convex operational model
(AB, (AB)# , uAB ), such that AB ⊆ B(A# , B # ), with uAB = uA ⊗ uB , α ⊗ β ∈ (AB)+ for all α ∈ A+ ,
#
#
β ∈ B+ , and a ⊗ b ∈ (AB)#
+ for all a ∈ A+ , b ∈ B+ .
8 This is a straightforward extension of the definition in [13] to the context of possibly non-saturated models.

7

<!-- page 8 -->
It is worth stressing that there are perfectly reasonable theories that are not locally tomographic.
Indeed, one of these is quantum mechanics over the real, rather than complex, scalars. We might more
generally deﬁne a composite in the wide sense of COMs A and B to be a COM (AB, (AB)# , uAB ),
together with (i) a positive linear embedding (injection) i : A ⊗min B → AB, and (ii) a positive map
r : AB → A ⊗max B, surjective as a linear map, such that for all a ∈ A# , b ∈ B # ,
r(i(α ⊗ β))(a, b) = a(α)b(β),
i.e., r ◦ i is the canonical embedding of A ⊗min B in A ⊗max B. However, we shall make no use of this
extra generality here. Accordingly, we assume henceforth that all composites are locally tomographic, as
per Deﬁnition 11 above.
3.3 Conditioning and Remote Evaluation
A bipartite state ω on A and B gives rise to a positive linear mapping ω
b : A# → B with
b(b
ω (a)) = ω(a, b)

for all a ∈ A# and b ∈ B # ; dually, a bipartite eﬀect f ∈ (AB)# gives rise to a linear map fb : A → B # ,
given by fb(α)(β) = f (α ⊗ β), and subject to f (α) ≤ uB for all α ∈ ΩA .
The marginals of ω are given by ωB = ω
b (uA ) and ωA = ω
b ∗ (uB ). Note that ω is normalized iﬀ
uB (b
ω (uA )) = 1. We can deﬁne the conditional states of A and B given (respectively) eﬀects b ∈ [0, uB ]
and a ∈ [0, uA ] by
ω
b (a)
ω
b ∗ (b)
and ωB|a :=
ωA|b :=
ωB (b)
ωA (a)
provided the marginal probabilities ωB (b) and ωA (a) are non-zero. Accordingly, we refer to ω
b (a) as the
un-normalized conditional state. Notice that the linear adjoint, ω
b ∗ : B # → A, of ω
b represents the same
state, but evaluated in the opposite order: ω
b ∗ (b)(a) = ω
b (a)(b) = ω(a, b).

Lemma 12 (Remote Evaluation 1). Let A, B and C be convex operational models. For any bipartite
effect on f ∈ (AB)∗ and any bipartite state ω ∈ BC, and for any state α ∈ A,
(f ⊗ −)(α ⊗ ω) = ω
b (fb(α)).

Proof: It is straightforward that this holds where f and ω are a product eﬀect and a product state,
respectively. Since these generate (AB)∗ and AB, the result follows. 
Operationally, this says that one can implement the transformation ω
b ◦ fb by preparing the tripartite
system ABC in state α ⊗ ω, where α ∈ A is the “input” state to be processed, and then making a
measurement on AB, of which f is a possible outcome: the un-normalized conditional state of C, given
the eﬀect f on AB, is exactly ω
b (fb(α)). Thus, the process φ := ω
b ◦ fb : A → C becomes a special case of
conditioning. In [9], we have called this protocol remote evaluation. Note that conclusive, or post-selected,
teleportation arises as the special case of remote evaluation in which, up to some speciﬁed isomorphism,
C ≃ A and ω
b ◦ fb ≃ 1A . We shall return to this point below.
4. Categories of convex operational models
We now wish to chart some connections between the two approaches outlined above. In the ﬁrst place,
we will bring some category-theoretic order to the concepts developed in the preceding section.
Since morphisms of COMs compose, we can deﬁne a category Com of all convex operational models
and COM morphisms. As described in Section 3.1, the hom-sets Com(A, B) are themselves cones. Let
I denote the COM R with its standard cone and order unit, i.e. I = (R, R, 1).
Definition 13. A category of COMs is a subcategory C of Com such that: (i) C(A, B) is a (regular)
sub-cone of the cone Com+ (A, B); (ii) C contains the distinguished COM I; (iii) C(I, A) ≃ A; and (iv)
C(A, I) ≃ A# . We call a such a category finite-dimensional if all state spaces A ∈ C are ﬁnite dimensional.
8

<!-- page 9 -->
A more general deﬁnition would require only that C(A, B) be some set of processes, in the sense
of Deﬁnition 9, between A and B. However, we should like to be able to construct random mixtures
of processes, so C(A, B) should at least be convex. Allowing for the taking of limits as a reasonable
idealization, it is plausible to take C(A, B) also to be closed. Finally, one should require that, if φ : A → B
is a physically valid process, then so is tφ for any t ∈ [0, 1] – this reﬂecting the possibility of attenuating
a process (as, for instance, by some ﬁlter that admits only a fraction t of incident systems, but otherwise
leaves systems unchanged, or by in some other way conditioning its occurrence on an event assigned
a probability less than 1). This much given, the physically meaningful processes between two systems
should generate a closed, convex, pointed cone of positive mappings, as per Deﬁnition 13.
In [8, 9, 12], a probabilistic theory is deﬁned, rather loosely, to be any class of COMs (or “probabilistic
models”) that is equipped with some device, or devices, for forming composite systems. Tightening this
up considerably, we make the following deﬁnition.
Definition 14. A monoidal category of COMs is a category of COMs equipped with a monoidal structure,
such that (i) the monoidal unit is the COM I; (ii) for every A, B ∈ C, A ⊗ B is a non-signaling composite
in the sense of Deﬁnition 11.
While Deﬁnition 14 does not require it, in the rest of the paper we will assume that all monoidal
categories of COMs are symmetric monoidal, and (in accordance with our standing assumtion), ﬁnite
dimensional.
As an example, the category FDCom of all ﬁnite-dimensional convex operational models and positive
mappings can be made into a monoidal category in two ways, using either the maximal or the minimal
tensor product. Another example is the “box-world” considered, e.g., in [22, 40]: here, state spaces
are constructed by forming maximal tensor products of basic systems, the normalized state spaces of
which are two-dimensional squares. Another example is aﬀorded by the category of quantum-mechanical
systems, represented as the self-adjoint parts of complex matrix algebras. Here, the appropriate monoidal
product of two systems A and B is what is sometimes referred to as the “spatial” tensor product, obtained
by forming tensor products of the Hilbert spaces on which the A and B act, and taking the self-adjoint
operators on this space.
4.1 Remote Evaluation Again
We now reformulate the conditioning maps and remote evaluation protocol discussed above in purely
categorical terms. In fact, both make sense in any symmetric monoidal category C. Suppose, then, that
ω : I → B ⊗ A is a “bipartite state”, i.e, a state of the composite system B ⊗ A. Then there is a canonical
mapping ω
b : C(B, I) → C(I, A) given by
ω

/ B⊗A
I EE
EE
EE
EE
b⊗1A
ω
b (b) EE
E" 
A

(4)

Dually, if f ∈ C(A ⊗ B, I), there is a natural mapping fb : C(I, A) → C(B, I) given by
α⊗1B

/ A⊗B .
BE
EE
EE
EE
EE f
fb(α)
EE 
"
I

(5)

Note that if C is already a category of COMs, then ω
b and fb are exactly the conditioning and co-conditioning
maps discussed in the last section. This has a simple but important corollary, namely, that these maps
are indeed morphisms of COMs. Another consequence is that any monoidal category of COMs is closed
under conditioning – that is, if ω is a normalized bipartite state of such a theory, belonging, say, to a

9

<!-- page 10 -->
composite system AB, then for every eﬀect a on A and b on B, the composite states ωB|a and ωA|b are
indeed states of A and B, respectively (as opposed to merely being elements of (A# )∗ and (B # )∗ ).9
The remote evaluation protocol of Lemma 12 also has a purely category-theoretic formulation:
Lemma 15 (Remote Evaluation 2). Let ω : I → B ⊗ C and f : A ⊗ B → I in C. Then
ω
b (fb(α)) = (f ⊗ 1C ) ◦ (1A ⊗ ω) ◦ α = (f ⊗ 1C ) ◦ (α ⊗ ω)

(6)

ω
b ∗ (fb∗ (β)) = (1A ⊗ f ) ◦ (ω ⊗ β).

(7)

for all α ∈ C(I, A). Dually, for every β ∈ C(I, B), we have

Proof: We prove (6), the proof of (7) being similar. Tensoring the diagram (5) with C (on the right) gives
the right-hand triangle in the diagram below. Applying (4) to compute ω
b (fb(α)) gives the lower triangle.
The square commutes by the bifunctoriality of the tensor.
AO

α

I

1A ⊗ω

/ A⊗B⊗C
O NNN
NNNf ⊗1C
NNN
NNN
NNN
'
α⊗1B ⊗1C
37 C
p
p
b
ω
b (f (α))
pp
ppp
p
p
pppb
ppp f (α)⊗1C
ω
/ B⊗C

Chasing around the diagram gives the desired result. 
Suppose that, in the preceding lemma, ω(1) ∈ A ⊗ B is a normalized state, and f : B ⊗ C → I
is an eﬀect, i.e, 0 ≤ f ≤ uBC . Then, in operational terms, the Lemma says that the mapping ω
b ◦ fb
is represented, within the category C, by the composite morphism (f ⊗ 1C ) ◦ (1A ⊗ ω).10 In other
words: preparing BC in joint state ω, and then measuring AB and obtaining f , guarantees that the
“un-normalized conditional state” of C is ω
b (fb(α)), where α is the state of A.
Remark 16. An important point here is that any process that factors as ω
b ◦ fb can be simulated by a
remote evaluation protocol, using what amounts to classical conditioning – in particular, without need
to invoke any mysterious “collapse” of the state, nor for that matter, any other physical dynamics at all.
4.2 Teleportation, conditional dynamics and compact closure
Suppose that, in the remote evaluation protocol of Lemma 15, we have C = A. Suppose further
that the mapping ω
b : B # → A has a right inverse — that is, suppose there exists a positive linear map
#
rb : A → B such that ω
b ◦ rb = 1A . Then we can re-scale rb to obtain an eﬀect f on A ⊗ B by
f (α, β) = cb
r (α)(β),

for a small enough positive constant c. Upon obtaining the result f in a measurement on A ⊗ B when
the composite system is in state α ⊗ ω, the un-normalized conditional state of C is:
ω
b (fb(α)) = cα.

The normalized conditional state will be exactly α. This is what is meant, in quantum-information
theory, by a conclusive, correction-free teleportation protocol. Adopting this language, we will say that it
is possible to teleport system A through system B if and only if there exists such a pair ω
b , rb.
b −1 , and system B can also be teleported through
If ω
b is in fact an isomorphism A# ∼
= B, then rb = ω
system A. When this is the case, Lemma 15 tells us that ω : I → B ⊗ A and f : A ⊗ B → I with fb = ω
b −1 ,
9 This is closely related to the notion of regular composite introduced in [9].

10 Technically we are relying on the isomorphisms between A ∼ C(I, A) and A# ∼ C(A, I) to guarantee that the internal

=

representation of ω
b ◦ fb defines the right linear map.

10

=

<!-- page 11 -->
provide respectively a unit and co-unit making (B, ω, f ) a dual for A. Thus, a compact closed category
of COMs is exactly one in which every system A is paired with a second system B = A′ , in such a way
that each system can be teleported through the other.
Proposition 17. Let C be a monoidal category of COMs. The following are equivalent.
(a) C is compact closed.
(b) Every A ∈ C can be teleported through some B ∈ C, which in turn can be teleported through A.
(c) Every morphism in C has the form ω
b ◦ fb for some bipartite state ω and bipartite effect f .

Proof: The equivalence of (a) and (b) is clear from the preceding discussion. To see that these are in
turn equivalent to (c), suppose ﬁrst that (a) holds, and let (A′ , ηA , eA ) be the dual for A. Suppose that
φ : A → B is a morphism in C, and deﬁne ωφ = (1A′ ⊗ φ) ◦ ηA . By Remote Evaluation (Lemma 15), we
have
ω
cφ e
(c
A (α)) = (eA ⊗ 1B ) ◦ (1A ⊗ ωφ ) ◦ α

for every α ∈ C(I, A). Since C is compact closed, the following diagram commutes:
φ
1A
/A
/B
A II
O
O
II
II
II
eA ⊗1A
eA ⊗1B
1A ⊗ηA III
I$
1A ⊗1A′ ⊗φ
/ A ⊗ A′ ⊗ B ,
A ⊗ A′ ⊗ A

∼
and hence ω
cφ e
(c
cφ ◦ ec
A (α)) = φ(α). Since C(I, A) = A we have φ = ω
A as required. Conversely, if (c) holds,
b
then for each A, the identity mapping 1A factors as ω
bA ◦ fA for some ωA ∈ B ⊗ A and some f ∈ A ⊗ B.
It follows that ω
bA = fbA−1 , so this gives us a compact closed structure. 
5. Weakly Self-Dual Theories
In a compact closed category C, the internal adjoint ′ : C → C described in Section 2 establishes
an isomorphism C ≃ C op . In particular, for every object A in the category, understood as a “physical
system”, there is a distinguished isomorphism between the system’s state space C(I, A) and the space
C(A, I) of eﬀects.
In contrast, a convex operational model A is not generally isomorphic to its dual. Indeed, there is a
type issue: A has, by deﬁnition, a distinguished unit functional uA ∈ A# ; in order for A# to be treated
as a COM, one would need to privilege a state αo ∈ A to serve as an order unit on A# . Only in special
cases is there a natural way of doing so.11 Beyond this, there is the more fundamental problem that,
geometrically, the cones A+ and A#
+ are generally not isomorphic. This said, those convex operational
models that are order-isomorphic to their duals are of considerable interest – not only because both
classical and quantum systems exhibit this sort of self-duality, but because it appears to be a strong
constraint, in some measure characteristic of these theories.
5.1 Weak vs Strong Self-Duality
A ﬁnite-dimensional ordered vector space A (or its cone, A+ ) is said to be self-dual iﬀ there exists an
inner product – that is, a positive-deﬁnite, hence also symmetric and non-degenerate, bilinear form h , i
– on A such that
A+ = A+ := {a ∈ A|ha, xi ≥ 0 ∀x ∈ A+ }.
11 When the state space is sufficiently symmetric, there may be a natural choice of state invariant under the symmetry
group. For example, if the base-preserving automorphisms act transitively on the pure states, the state obtained by groupaveraging is the natural choice.

11

<!-- page 12 -->
In this case, we have A ≃ A∗ , as ordered spaces, via the canonical isomorphism a 7→ ha, .i. A celebrated
theorem of Koecher and Vinberg [28, 41, 21] states that if A+ is both self-dual and homogeneous, meaning
that the group of order-automorphisms of A acts transitively on the interior of A+ , then A is isomorphic,
as an ordered space, to a formally real Jordan algebra ordered by its cone of squares. The Jordan-von
Neumann-Wigner [26] classiﬁcation of such algebras then puts us within hailing distance of quantum
mechanics.
Definition 18. A COM (A, A# , uA ) is weakly self-dual (WSD) iﬀ there exists an order-isomorphism
φ : A ≃ A# . We shall say that A is symmetrically self-dual iﬀ φ can be so chosen that φ(α)(β) = φ(β)(α)
for all α, β ∈ A.
Note that, for a given linear map φ : A → A# , the bilinear form hα, βi := φ(α)(β) is non-degenerate
iﬀ φ is a linear isomorphism, and symmetric iﬀ φ = φ∗ . If we don’t require saturation, any ﬁnitedimensional ordered linear space A can serve as the state space for a weakly self-dual COM, simply by
setting (A# )+ = φ(A+ ) for some nonsingular positive linear mapping A → A∗ , and taking any point in
the interior of (A# )+ for uA . However in the saturated case, weak self-duality is a real constraint on the
geometry of the state cone, although strong self-duality is an even stronger one.
Note that, for a given linear map φ : A → A# , the bilinear form hα, βi := φ(α)(β) is non-degenerate
iﬀ φ is a linear isomorphism, and symmetric iﬀ φ = φ∗ . Thus, A will be self-dual, in the classical
sense described above, iﬀ h , i is positive-deﬁnite, and A# = A∗ , i.e, A is saturated. To emphasize the
distinction, we shall henceforth refer to this situation as strong self-duality.
If φ : A ≃ A# is an order-isomorphism implementing A’s self-duality, then φ−1 : A# ≃ A deﬁnes an
un-normalized bipartite non-signaling state γ in A ⊗max A with φ−1 = γ
b – that is, γ(a, b) = φ−1 (a)(b).
Following [12], we shall call such a state an isomorphism state. It is shown in [12] that such a state is
necessarily pure in A ⊗max B.12 In this language, A is WSD iff A ⊗max B contains an isomorphism state.
Example 19. Let A be the convex operational model of a basic quantum-mechanical system, i.e., the
space of self-adjoint operators associated with the system’s Hilbert space H. The standard maximally
entangled state on A ⊗ A is the pure state associated with the unit vector
1 X
xi ⊗ xi
Ψ= √
d i

where {x1 , ..., xn } is an orthonormal basis for H. Using this, one has a mapping
R : T 7→ RT := (T ⊗ 1)PΨ
taking operators T : H → H to operators B(H ⊗ H). It is a basic result, due to Choi and, independently,
Jamiolkowski, that this is a linear isomorphism, taking the cone of completely positive maps on B(H)
onto the cone of positive operators on H ⊗ H. Note that R−1 maps [31] ρ to Tρ where the latter is given
by
hx|Tρ (σ)yi = dTr(ρ((|yihx|) ⊗ σ T ))
where |yihx| is the operator z 7→ hz, xiy, and the transpose is deﬁned relative to the chosen orthonormal
basis. This gives us a state γ ∈ A ⊗ A with γ
b : A∗ ≃ A, namely,
γ
b(a)(b) = Tr(PΨ (a ⊗ b)) = Tr(PΨ (a ⊗ 1)(1 ⊗ b)).

5.2 Categories of self-dual COMs
Let C be a monoidal category of COMs, as described in Section 4. There is a distinction between
requiring that a state space A ∈ C be weakly self-dual, which implies only that there exist an orderisomorphism A# ≃ A – an isomorphism in Ordlin – and requiring that this correspond to an (unnormalized) state γ ∈ (AA)+ , hence, to an element of C(I, A ⊗ A). We now focus on categories in which
this latter condition holds for every system.
12 Strictly speaking, [12] deals with the case in which A and B are saturated, but the proof is easily extended to the
general case.

12

<!-- page 13 -->
Definition 20. A symmetric monoidal category C of COMs is weakly self-dual (WSD) iﬀ for every
A ∈ C, there exists a pair (γA , fA ) consisting of a bipartite state γA ∈ A ⊗ A and a positive functional
fA ∈ (A ⊗ A)# = C(A ⊗ A, I) (a multiple of an eﬀect) such that (i) γA is an isomorphism state, and (ii)
−1
fbA = γ
bA
. If γA can be chosen to be symmetric for every A ∈ C, we shall say that C is symmetrically
self-dual (SSD).
Note that this is stronger than merely requiring every COM A ∈ C to be weakly self-dual. Equivalently,
we may say that category C of COMs is WSD iﬀ every system can be equipped with a designated
conclusive, correction-free teleportation protocol γA ∈ AA, fA ∈ (AA)# , whereby A can be teleported
“through itself”. Thus, by Proposition 17, we have:
Theorem 21. A monoidal category C of convex operational models is weakly self-dual iff it is compact
closed, and can be equipped with a compact structure such that A′ = A for all objects A ∈ C.
Recall that any morphism φ in a compact closed category has a categorial adjoint, φ′ . In the context
of a WSD category of COMs, this has a useful interpretation in terms of the linear adjoint, φ∗ :
Lemma 22. Let C be any WSD category of ASPs, regarded as compact closed as above. Let φ : A → B.
Then the canonical adjoint mapping φ′ : B → A is given by
∗
φ′ = (fbB ◦ φ ◦ γ
bA )∗ = γ
bA
◦ φ∗ ◦ fbB∗

Proof. We must show that, for any β ∈ B – that is, any β ∈ C(I, B) – we have φ′ (β) := φ∗ ◦ β =
∗
γ
bA
(φ∗ (fbB∗ (β))), where φ∗ : B # → A# is the linear adjoint. Let ω := (1A ⊗ φ) ◦ γA : I → A ⊗ B. Then we
have
φ′ (β)

= φ′ ◦ β
= (1A ⊗ fB ) ◦ (1A ⊗ φ ⊗ 1B ) ◦ (γA ⊗ 1B ) ◦ β

= (1A ⊗ fB ) ◦ (1A ⊗ φ ⊗ β) ◦ γA
= (1A ⊗ (fB ◦ (1B ⊗ β))) ◦ ((1A ⊗ φ) ◦ γA )
= (1A ⊗ fb∗ (β)) ◦ ω)
= ω
b ∗ (fbB∗ (β)).

Now, for any b : B → I, we have
ω
b ∗ (b) =
=
=
=
=
=

\
(σB,B
◦ ω)(b)
(1A ⊗ b) ◦ ω

(1A ⊗ b) ◦ (1A ⊗ φ) ◦ γA
(1A ⊗ (b ◦ φ)) ◦ γA

(1A ⊗ φ∗ (b)) ◦ γA
∗
bA
γ
(φ∗ (b)).

With b = fbB∗ (β), this gives the desired result. 

Corollary 23. For all A ∈ C, fA′ = σA,A ◦ γA .

Proof. Note ﬁrst that fA∗ (1) = fA ∈ (A ⊗ A)# . Thus, the preceding Lemma gives us
∗
fA′ (1) = (b
γA⊗A
◦ fA∗ ◦ fbI∗ )(1)

Since fI = fI∗ = 1I , we have

∗
∗
fA′ (1) = (b
γA
⊗γ
bA
)(fA ).

13

<!-- page 14 -->
Thus, for every a, b ∈ A# , we have
fA′ (1)(a, b) =

∗
∗
(b
γA
⊗γ
bA
)(fA )(a, b)

fA (b
γA (a), γ
bA (b))
∗
b
f (b
γA (b))(b
γ ∗ (a))

=
=
=

A

A

∗
b(b
γA
(a))

=
=

γA (b, a)
(σ ◦ γA )(a, b).


Theorem 24. Let C be a symmetrically self-dual monoidal category of COMs. Then C is dagger compact
with † given by the canonical adjoint ′ : C op → C.
Proof. By Theorem 21, C is degenerate compact closed, with a compact structure on A ∈ C given by
(A, γA , fA ), where γA is symmetric. Deﬁne (·)† : C op → C by (·)† = (·)′ ; then (·)† is a monoidal functor
−1
′
which is the identity on objects. Since σA,B
= σA,B
in any compact closed category, C is dagger-monoidal.
†
That fA = σA,A ◦ γA is immediate from Corollary 23. 
Lemma 25. For all A, let τA : A → A be the order-isomorphism given by
τA := γ
bA ◦ fbA∗ .
Then, for all φ ∈ C(A, B), we have

φ′′ = τB−1 ◦ φ ◦ τA .

∗
γB ◦ fbB∗ )−1 = γ
bB
◦ fbB . By Lemma 22, we have
Proof: Notice ﬁrst that τB−1 = (b

φ′′ = (fbA ◦ φ′ ◦ γ
bB )∗

=
=
=
=

(fbA ◦ (fbB ◦ φ ◦ γ
bA )∗ ◦ γ
bB )∗
b∗ ◦ (fbB ◦ φ ◦ γ
γ
bA )∗∗ ◦ fb∗
B
A
∗
∗
b
b
(b
γB ◦ fB ) ◦ φ ◦ (b
γA ◦ f A )
−1
τB ◦ φ ◦ τA 

Corollary 26. Let φ : A → B with φ′′ = φ. Then φ ◦ τA = τB ◦ φ.
Theorem 27. For any object A in a weakly self-dual category C of convex operational models, the
following are equivalent: (i) φ′′ = φ for all φ ∈ C(A, A), (ii) τA = 1A , and (iii) fA and γA are symmetric
as a bilinear forms.
Proof: (i) implies (ii): From (i), and the fact that the morphisms in C(A, B) are a basis for L(A, B), (·)′′
is the identity map. Let Ei , Fj be bases of the spaces L(A, A), L(B, B) of linear maps on vector spaces
A, B respectively. Then the maps X 7→ Fj XEi , where X ∈ L(A, B), are a basis for the space of linear
maps from L(A, B) to itself. Using this fact, we can expand the map (·)′′ : φ 7→ τB−1 ◦ φ ◦ τA , which is a
map from L(A, B) to itself, in a basis Mij : φ 7→ Fj XEi where E0 = 1B , F0 = 1A . By the uniqueness of
expansions in bases and the fact that (·)′′ is the identity map, we get τA = 1A , τB = 1B .
−1
(ii) implies (iii): By (ii) we have τA := γ
bA ◦fbA∗ = 1A , so fbA∗ = γ
bA
= fbA . Since f (a, b) ≡ fb(a)(b) ≡ fb∗ (b)(a),
fbA∗ = fbA is equivalent to symmetry of fA . Symmetry of γA then follows from the fact that γA = fA−1 .
(iii) implies (i): If fA (hence, also γA ) are symmetric, then we have fA∗ = fA , whence, τA = γA ◦ fbA = 1A ;
thus, by Lemma 25, φ′′ = φ for all φ ∈ C(A, A). 
Applying Theorem 24, we now have the
Corollary 28. A WSD monoidal category of COMs is dagger compact with respect to the canonical
adjoint ′ : C op → C, if and only if it is symmetrically self-dual.
14

<!-- page 15 -->
Theorem 27 tells us that if C is a saturated weakly self-dual theory in which ′ is an involution, then
the interior of A+ is a domain of positivity in the sense of Koecher [30]. If we further suppose that every
irreducible state space in C is homogeneous, meaning that G(A+ ) acts transitively on the interior of A+
for every A ∈ C (a condition one can motivate physically in several ways, e.g., [12, 44]), then we are close
to requiring that every state space in C be a formally real (also called Euclidean) Jordan algebra [28, 41].
This line of thought will be pursued in a sequel to this paper.
6. Conclusion
We began with the observation that compact closure, and still more, dagger compactness, represent
strong constraints on a physical theory, thought of as a symmetric monoidal category of “systems” and
“processes”. Our results cast some light on the operational (or, if one prefers, the physical) content
of these assumptions in the concrete — but still very general — context of probabilistic (or convex
operational) theories. In particular, we have seen that, in probabilistic theories qua categories of COMs,
compact closure amounts to the condition that all processes – that is, all dynamics – can be induced by
the kind of conditioning that occurs in a teleportation-like protocol. Indeed, in such a theory, a process
between systems A and B amounts to a choice of bipartite state on A ⊗ B. Finally, we have established
that for weakly self-dual theories symmetric weak self-duality implies the existence of a dagger compatible
with the compact closed structure. As in the special case of quantum mechanics, a dagger amounts to
reversing the order of conditioning.
Throwing these results into sharper relief is the following result (details of which will appear elsewhere).
Let C be any symmetric monoidal category, with associated monoid of scalars S = C(I, I). Then, for any
monoid homomorphism p : S → [0, 1], there exists a functor Vp : C → Com. This can be used to transfer
the monoidal structure of C to the image category F (C), giving us a representation of C as a category
of COMs. The construction is straightforward: one deﬁnes a Mackey triple (XA , ΣA , pA ) for each object
A ∈ C, with XA = C(A, I), ΣA = C(I, A) and pA (x, α) = p(x ◦ α); linearizing this, as in Example 7, yields
a COM (V (A), V (A)# , uA ).
Several directions for further study suggest themselves. It would be interesting to identify necessary
and suﬃcient conditions for the COM representations discussed in section 4.1 to yield finite dimensional
models – and, equally, one would like to know how far the other results of Sections 4 and 5 extend to
inﬁnite-dimensional systems. Our deﬁnition of category of weakly self-dual state spaces assumes the
existence of a state that induces, by conditioning, an isomorphism from the state cone to the eﬀect cone,
and an eﬀect inducing its inverse; but as we noted, it would be interesting to investigate conditions under
which this follows just from weak self-duality of the objects. As mentioned at the end of section 5, the
consequences of homogeneity of the state-spaces should also be explored. Perhaps the most urgent task,
though, is to identify operational and category-theoretic conditions equivalent to the strong self-duality
of a probabilistic theory.
7. * References
[1] S. Abramsky and B. Coecke, A categorical semantics of quantum protocols, in Proceedings of the 19th
Annual IEEE Symposium on Logic in Computer Science: LICS 2004, pp. 415–425, IEEE Computer
Society (2004); also quant-ph/0402130v5 (2004).
[2] S. Abramsky and B. Coecke, Categorical quantum mechanics, in Handbook of Quantum Logic and
Quantum Structures II, K. Engesser, D. Gabbay, D. Lehman, eds., Elsevier (2008).
[3] S. Abramsky and R. Duncan, A categorical quantum logic, Mathematical Structures in Computer
Science 16, 486–489 (2006).
[4] E. M. Alfsen, Compact Convex Sets and Boundary Integrals, Springer, 1971.
[5] E. M. Alfsen and F. W. Shultz, State Spaces of Operator Algebras: Basic Theory, Orientations, and
C ∗ -products. Boston, Birkhauser (2002).
15

<!-- page 16 -->
[6] H. Araki, 1980, On a characterization of the state space of quantum mechanics, Comm. Math. Phys
75 (1980) 1-24.
[7] J. Baez. Quantum quandaries: a category-theoretic perspective. quant-ph/0404040, 2004.
[8] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Generalized no-broadcasting theorem, Phys. Rev.
Lett. 99 (2007) 24051
[9] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Teleportation in general probabilistic theories, in
Proceedings of the Cliﬀord Lectures, Tulane University, March 12-15, 2008, to appear in Proceedings
of Symposia in Applied Mathematics (AMS); also arXiv:0805.3553 (2008).
[10] H. Barnum and O. Dahlsten and M. Leifer and B. Toner, Nonclassicality without entanglement enables bit commitment, Proc. IEEE Information Theory Workshop, Porto, May 2008, arXiv:0803.1264
(2008).
[11] H. Barnum, C. Fuchs, J. Renes and A. Wilce, Inﬂuence-free states on compound quantum systems,
quant-ph/0507108 (2005)
[12] H. Barnum, P. Gaebler and A. Wilce, Ensemble steering, weak self-duality and the structure of
probabilistic theories, arXiv:0912.5532 (2009)
[13] H. Barnum and A. Wilce, Information processing in convex operational theories (2009)
(arXiv:0908.2352). To appear in a special issue of Electronic Notes in Theoretical Computer Science:
Proceedings of QPL/DCM (Quantum Physics and Logic / Developments in Computational Models),
Reykjavik, July 12-13, 2008.
[14] H. Barnum and A. Wilce, Ordered linear spaces and categories as frameworks for informationprocessing characterizations of quantum and classical theory (2009); also arXiv:0908.2354.
[15] J. Barrett, Information processing in general probabilistic theories, Phys. Rev. A 75 032304 (2007);
also arXiv:quant-ph/0508211.
[16] E. Beltrametti and G. Cassinelli, The logic of quantum mechanics, Academic Press 1980.
[17] B. Coecke, E. O. Paquette and D. Pavlovic, Classical and quantum structuralism, in I. Mackie and
S. Gay (eds), Semantic Techniques for Quantum Computation, pages 29–69, Cambridge University
Press, 2009.
[18] G. M. d’Ariano, How to derive the Hilbert-space formulation of quantum mechanics from purely
operational axioms, arXiv.org quant-ph/0603011 (2006).
[19] E. B. Davies and J. T. Lewis, An operational approach to quantum probability, Comm. Math. Phys.
17 239-260 (1970).
[20] C. M. Edwards, The operational approach to algebraic quantum theory I, Comm. Math. Phys. 16
(1970) 207-230.
[21] J. Faraut and A. Korányi, Analysis on Symmetric Cones, Oxford, 1994.
[22] D. Gross, M. Müller, R. Colbeck and O. C. O. Dahlsten, All reversible dynamics in maximally
nonlocal theories are trivial. Phys. Rev. Lett. 104 (2010), 080402.
[23] H. Hanche-Olsen, On the structure and tensor products of JC algebras, Can. J. Math. 35 (1983),
1059-1074.
[24] H. Hanche-Olsen, JB-algebras with tensor products are C ∗ -algebras, Lecture Notes in Mathematics
(Springer) 1132 (1985) pp. 223-229.
[25] C. Heunen, Categorical quantum models and logics, Doctoral thesis, Radboud University, Nijmegen.
Amsterdam, Pallas Publications, 2009.
16

<!-- page 17 -->
[26] P. Jordan, J. von Neumann and E. P. Wigner, On an algebraic generalization of the quantummechanical formalism, Annals of Mathematics 35 (1934), 29-64.
[27] M. Kläy, Einstein-Podolsky-Rosen experiments: the structure of the sample space, Foundations of
Physics Letters 1 (1988), 205-244.
[28] M. Koecher, Die geodätischen von positivitätsbereichen, Math. Annalen 135 (1958), 192-202.
[29] M. Koecher, On Real Jordan algebras, Bull. Amer. Math. Soc. 68 (1962), 374-377.
[30] M. Koecher, The Minnesota Notes on Jordan Algebras and their Applications edited and annotated
by A. Krieg and S. Walcher, Lecture Notes in Mathematics 1710, Springer Verlag, 1999.
[31] M. Keyl and R. Werner, Channels and Maps, in D. Bruss and G. Leuchs, Lectures on Quantum
Information, pp. 73-86, Wiley, 2007
[32] G. M. Kelly and M. L. Laplaza, Coherence for compact closed categories, J Pure Appl Algebra
(1980) 193-213.
[33] M. Klay, C. H. Randall, and D. J. Foulis, Tensor products and probability weights, Int. J. Theor.
Phys. 26 (1987) 199-219
[34] G. Ludwig, Foundations of Quantum Mechanics I, Springer, 1983.
[35] G. Mackey, Mathematical Foundations of Quantum Mechanics, Addison-Wesley, 1963
[36] S. MacLane, Categories for the Working Mathematician, Springer (1971). Second edition (1997).
[37] P. Selinger, Dagger compact closed categories and completely positive maps (extended abstract), in
Proceedings of QPL 05. Electronic Notes in Theoretical Computer Science 170, 139–163 (2007).
[38] P. Selinger, Towards a semantics for higher-order quantum computation. In Proceedings of the 2nd
International Workshop on Quantum Programming Languages, Turku, Finland. TUCS General Publication No. 33, pp. 127-143, June 2004.
[39] P. Selinger, personal communication.
[40] A. J. Short and J. Barrett, Strong non-locality: A tradeoﬀ between states and measurements.
arXiv:quant-ph/0909.2601.
[41] E. B. Vinberg, Homogeneous cones, Dokl. Acad. Nauk. SSSR 141 (1960) 270-273; English trans.
Soviet Math. Dokl. 2, 1416-1619 (1961).
[42] J. von Neumann, Mathematische Grundlagen der Quantenmechanik, Berlin, Springer 1932. English
translation: Mathematical Foundations of Quantum Mechanics, Princeton, Princeton University Press,
1955.
[43] A. Wilce, Tensor products in generalized measure theory, Int. J. Theor. Phys. 31, 1915 (1992) .
[44] A. Wilce, Four and a half axioms for ﬁnite dimensional quantum mechanics, electronic preprint
arXiv:0912.5530.

17
