---
type: paper
date: 2009-12-30
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:0912.5532v2)
reviewed: false
---

# Ensemble Steering, Weak Self-Duality, and the Structure of Probabilistic Theories

Machine-generated and unreviewed text extraction of arXiv:0912.5532v2
(24 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/0912.5532v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:0912.5532v2 [quant-ph] 4 Mar 2010

Ensemble Steering, Weak Self-Duality, and the
Structure of Probabilistic Theories
Howard Barnum∗, Carl Philipp Gaebler†and Alexander Wilce‡
March 4, 2010

Abstract
In any probabilistic theory, we may say a bipartite state ω on a composite
system AB steers
its marginal state ω B if, for any decomposition of ω B as a
P
mixture ω B = i pi βi of states βi on B, there exists an observable {ai } on A
such that the conditional states ωB|ai are exactly the states βi . This is always
so for pure bipartite states in quantum mechanics, a fact first observed by
Schrödinger in 1935. Here, we show that, for weakly self-dual state spaces (those
isomorphic, but perhaps not canonically isomorphic, to their dual spaces), the
assumption that every state of a system is steered by some bipartite state on
two copies of that system, of a composite amounts to the homogeneity of the
cone of unnormalized states. If the state space is actually self-dual, and not
just weakly so, this implies (via the Koecher-Vinberg Theorem) that it is the
self-adjoint part of a formally real Jordan algebra, and hence, quite close to
being quantum mechanical.

1

Introduction

The founders of quantum mechanics were already well aware that some of its most
non-classical (and seemingly paradoxical) aspects are naturally understood in terms
information. The Bohrian notion of complementarity, for example, can be understood
in terms of one type of knowledge about a system precluding another. The fact
∗

Perimeter Institute for Theoretical Physics; hbarnum@perimeterinstitute.ca
Harvey Mudd College
‡
Susquehanna University; wilce@susqu.edu
†

1

<!-- page 2 -->
that measurement must disturb the state of a system, also stressed by Bohr, again
gives fundamental status to a notion closely connected to information, the notion of
measurement, whose essence is the acquisition of some sort of information about a
system. Schrödinger was particularly inclined to take this point of view, as evidenced
by his description of entanglement:
The best possible knowledge of a total system does not necessarily include
total knowledge of all its parts, not even when these are fully separated
from each other and at the moment are not influencing each other at all.
[28]
The development of quantum information theory has rekindled interest in the possibility of characterizing quantum theory in operational or information-theoretic terms.
Characteristically, this newer work has focused on finite-dimensional systems, and
has emphasized considerations involving composite systems. It has become clear
that many properties of quantum systems, e.g., the existence and basic properties
of entangled states, are much better understood as generically non-classical, rather
than specifically quantum, phenomena, in the sense that they arise in arbitrary nonclassical probabilistic theories [12, 4, 6, 18, 23, 24, 31]. There is therefore a premium
on identifying operationally meaningful properties of bipartite quantum states that
are, so to say, parochial—that is, properties that are not generic in this way. An
example is the principle of information causality, recently introduced in [27]. Ideally,
one would like to find a small set of such principles that pick out quantum mechanics
on the nose, but failing this, it is still of interest to identify principles that define a
small neighborhood of theories close to quantum mechanics.
A property of entangled quantum states that struck Schrödinger as especially odd
is the fact that an observer controlling one component of such a state can steer the
other system into any statistical ensemble for its (necessarily, mixed) marginal state,
simply by choosing to measure a suitable observable [28, 21].
It is rather discomforting that the [quantum] theory should allow a system to be steered or piloted into one or the other type of state at the
experimenter’s mercy in spite of his having no access to it. [28]
What Schrödinger found discomforting is now understood to be an important information theoretic feature of quantum mechanics. This became clear when Bennett
and Brassard [13], in the same paper that introduced quantum key distribution, considered a natural quantum scheme for another important cryptographic primitive, bit
commitment, and showed that ensemble steering can be used to break it.1
1

In the scheme, the two possible values Alice can commit to are represented by two distinct
ensembles for the same density matrix; she is to send samples from the ensemble to Bob in order

2

<!-- page 3 -->
In this paper, we connect the possibility of ensemble steering with two very special geometric properties shared by finite-dimensional classical and quantum state
spaces. First, such state spaces are self-dual: their cones of (un-normalized) effects
are canonically isomorphic to their dual cones of (un-normalized) effects, meaning
that the isomorphism defines an inner product. Secondly, they are homogeneous:
their groups of order-isomorphisms act transitively on the interiors of their positive
cones. These two properties come close to characterizing finite-dimensional quantum
and classical state spaces: according to a celebrated theorem, due to Koecher [25] and
Vinberg [30], finite-dimensional homogeneous, self-dual cones are precisely the cones
of positive elements of formally real Jordan algebras. Once one has gone this far,
two further axioms (local tomography, and the existence of qubits) suffice to recover
QM uniquely. Here, we establish that in any probabilistic theory in which universal
self-steering is possible (meaning that every state is the marginal of a bipartite state
steering for that marginal) state spaces must be homogeneous and weakly self-dual,
meaning that the cones of un-normalized states and un-normalized effects must be
isomorphic, but perhaps not not canonically so. This reduces the gap between the
generic “self-steering” theory and quantum mechanics, largely to that between weak
and strong self-duality.
A brief outline of the rest of this paper is as follows. In Section 2, we review, for the
reader’s convenience, the mathematical framework in which we work, a variant of the
generalized probability theory proposed by Mackey [26] over 50 years ago, and now
quite standard in foundational work in quantum theory. In particular, we discuss
what we mean by a composite system, and by a probabilistic “theory”. (A more
detailed treatment of some of this material, can be found, e.g., in [4].) In Section 3,
we introduce weakly self-dual state spaces, and establish some of their properties. In
particular, we show (as a case of a result that we establish for general state spaces)
that, for an irreducible state space A, any bipartite state on A ⊗ A corresponding
to an order-isomorphism between A and its dual is pure. In Section 4, we connect
this to the possibility of purifying a state, showing that weakly self-dual homogeneous
state spaces are precisely those in which every interior state (i.e., state not on the
boundary of the state space) arises as the marginal of such an isomorphism state.
Section 5 discusses steering per se, illustrating the idea with several examples, and
establishing an order-theoretic necessary and sufficient condition for the steering of
one marginal. suitable quotient of the other. Section 6 summarizes our main results
and suggests a number of questions for further work.
to commit, and later reveal which states she drew so that Bob can check that she used the claimed
ensemble. However, by sending, not a draw from the ensemble but one system of a pure bipartite
entangled state with the specified density matrix, and keeping the other system, she can realize either
ensemble after she’s already sent the systems to Bob by making measurements on her entangled
system, enabling her to perfectly mimic commitment to either bit.

3

<!-- page 4 -->
2

The ordered linear spaces formalism

This section provides a quick summary of the formalism of abstract state spaces used
in [4, 5, 6, 10, 11]. In the interest of brevity, we omit detailed motivation for the
definitions below, referring the interested reader to [4]. Suffice it to say here that any
model of a probabilistic system characterized by states and observables in the usual
way [16, 17], fits naturally into this very general framework. Although much of what
we do below can be extended to a more general context, we restrict ourselves here to
finite-dimensional systems. Thus, we assume—generally, without further comment—
that all vector spaces in what follows are finite dimensional. In particular, this allows
us to routinely identify a vector space V with its double dual V ∗∗ .
An ordered linear space (OLS) is a real vector space V equipped with a partial ordering
compatible with the linear structure in the sense that it satisfies x ≤ y ⇒ x+z ≤ y +z
and x ≤ y =⇒ tx ≤ ty for all x, y, z ∈ V and all non-negative scalars t. Any such
ordering is determined by the the pointed convex cone2 V+ , called the positive cone,
of vectors x with 0 ≤ x, since x ≤ y iff y − x ∈ V+ ; conversely, any pointed convex
cone induces an ordering on V in this way. If a and b are elements of an ordered
linear space V with a ≤ b, we write [a, b] for the set of vectors x ∈ V with a ≤ x ≤ b.
It is easy to see that this set is convex.
If a pointed convex cone is also generating (i.e., spans V , so that V = V+ − V+ ) and
closed, it is called regular. Henceforth, we mean by “ordered linear space” one whose
positive cone is regular. Examples include the space RX of real-valued functions on
a set X, ordered pointwise on X, and the space L(H) of Hermitian operators on
a (finite-dimensional) Hilbert space H, with the usual operator-theoretic order, i.e.,
a ≥ 0 iff a = b† b for some b ∈ L(H).
We say that a linear map ϕ : V → W between ordered linear spaces V and W is
positive iff it is order-preserving, or equivalently iff it takes the positive cone of V into
that of W , i.e., ϕ(x) ∈ B+ for all x ∈ V+ . In particular, a linear functional f ∈ V ∗
is positive iff f (x) ≥ 0 for all x ∈ V+ . An order isomorphism between ordered linear
spaces V and W is a positive linear isomorphism ϕ : V → W with positive inverse—
that is, ϕ is an order isomorphism iff it is bijective and satisfies ϕ(x) ≥ 0 in W iff x ≥ 0
in V . An order-isomorphism from an OLS to itself is an order-automorphism (or just
automorphism). The set L+ (V, W ) of positive linear mappings from an OLS V to an
OLS W is a pointed, closed convex cone in the space L(V, W ) of all linear maps from
V to W ; where V and W are finite-dimensional, this cone is also generating. In the
special case where W = R, we write L+ (V, R) as V+∗ , referring to this as the dual cone
to V .
2

A convex cone in a real vector space V is a convex set K ⊆ V closed under multiplication by
non-negative scalars. If K ∩ −K = {0}, the cone is said to be pointed.

4

<!-- page 5 -->
An order unit in an ordered linear space V is a vector u ∈ V+ such that, for every
x ∈ V+ , there is some positive scalar t with x ≤ tu. An order unit on V is an order
unit in V ∗ —equivalently (in finite dimensions), a strictly positive functional u ∈ A∗ ,
that is, one with u(α) > 0 for α > 0. (In other words,
u is in the interior of A∗+ .)
P
X
For example, if A = R , the functional u(f ) = x∈X f (x) is an order unit. For
A = L(H), the trace is an order unit.
A face of a cone V+ is a sub-cone F+ with the property that if x, y ∈ V+ with
x + y ∈ F+ , then x, y ∈ F+ .3 In particular, if F+ is a face and 0 ≤ x ≤ y ∈ F+ ,
then x ∈ F+ as well. The smallest face containing a given element y ∈ V+ is denoted
Face(y). When this coincides with the ray generated by y, we say that y is extremal
in V+ (note this is not the same thing as saying y is an extreme point of V+ —only 0
is that). A proper face, i.e., one not the whole cone, is contained in the topological
boundary of the cone. An easy exercise shows that y is an order-unit in the OLS
F := F+ − F+ spanned by F+ , iff F+ = Face(y). Note also that the intersection of
faces is a face, and that a face of a face of V+ is a face of V+ .
If A and B are ordered linear spaces, there is a natural ordering on their direct sum,
namely, (A ⊕ B)+ = {x + y|x ∈ A+ , y ∈ B+ }. We refer to A ⊕ B, with this ordering,
as the ordered direct sum of A and B. An ordered linear space V is irreducible iff
there exists no non-trivial decomposition V of V as an ordered direct sum. Every
OLS in finite dimension is a direct sum of irreducible ones. An OLS is simplicial iff
it can be represented as an ordered direct sum of one-dimensional subspaces.
Definition 2.1. By an abstract state space, we mean a pair (A, uA ) where A is an
ordered linear space and uA is a distinguished order-unit on A. We refer to a positive
element of A with uA (α) = 1 as a normalized state. The set of all normalized states
is a compact convex subset of A+ , which we denote by ΩA . 4
In quantum mechanics, the relevant example is A = L(H), as described above, with
uA (a) = Tr(a); thus, ΩA is the set of density matrices of H. However, any finitedimensional compact convex set can be represented, in an essentially canonical way,
as ΩA for a suitable abstract state space (A, uA ) [29], so the definition allows for
arbitrarily general models.
Of course, the picture thus far is incomplete: we also need some way to describe
the results of measurements performed on a system. To this end, note that if a is
an outcome of some measurement, then, for any state α ∈ ΩA , there should be a
3

A subcone of V+ is, of course, a subset of V+ that is itself a cone.
The set ΩA is a base for the positive cone A+ : a convex set S such that every non-zero α ∈ A+
is a positive scalar multiple of a unique vector in S. In the case S = ΩA ), the vector is α/uA (α).
Indeed, what we are calling an abstract state space is essentially the same thing as a ordered vector
space with a distinguished cone-base, i.e., what we might call a (finite-dimensional) cone-base space.
4

5

<!-- page 6 -->
well-defined probability α(a) to obtain a as the result of measuring the system when
the latter is in state α. In order to maintain consistency with our intuitive notion
that convex combinations of states reflect randomized preparations, we must require
that α 7→ α(a) be affine, i.e., that it preserve convex combinations. It can be shown
that any affine functional on ΩA extends uniquely to a positive linear functional on
A; thus, we are led to the following
Definition 2.2. An effect on an abstract state space (A, uA ) is a positive functional
a ∈ A∗ such that a ≤ uA —equivalently, a ∈ A∗ is an effect iff 0 ≤ a(α) ≤ 1 for every
normalized state α ∈ ΩA .
Note that 0 and uA are, respectively, the smallest and largest effects on A, and the
set of all effects on A is precisely the interval [0, uA ]. From the discussion above,
we see that every measurement outcome will correspond to (or define) an effect on
A. We make the further assumpition here that the converse holds, i.e, that every
effect represents a measurement outcome.
Accordingly, a discrete observable on
A
is
a
family
{a
}
of
effects,
indexed
by
a
x x∈X
P
P finite set X (a “value space”), with
x∈X ax (α) = 1 for all α ∈ Ω, i.e., with
x ax = uA . In the classical case where
S
A = R for a finite set S, an observable in this sense corresponds to a “fuzzy” random
variable, while in the quantum case, with A = L(H), an effect is a positive operator
between 0 and 1, and an observable is a discrete POVM (positive operator-valued
measure). A common type of observableP
has X = {1, 2, ..., n}; such an observable
amounts to a set a1 , ..., an of effects with i ai = uA .
The formalism sketched above accommodates composite systems. Let A and B be
abstract state spaces, with order-units uA ∈ A∗ , uB ∈ B ∗ and normalized state spaces
ΩA and ΩB . We write A ⊗max B for the space of bilinear forms on A∗ × B ∗ , ordered
by the cone of forms nonnegative on products a ⊗ b of positive elements (i.e. a ∈ A∗+ ,
∗
b ∈ B+
), with order unit uA ⊗ uB . We write A ⊗min B for the same space, ordered
by the (generally, much smaller) cone generated by the product states α ⊗ β, where
α ∈ A+ and β ∈ B+ .
States in A⊗max B satisfy a natural no-signaling condition, namely, that the marginal
states of A and B are well-defined, not depending on which observable may be measured on the other wing. Conversely, it can be shown [24, 31] that a joint probability
assignment to measurement outcomes associated with A and B that satisfies this
non-signaling requirement, necessarily extends to a positive bilinear form on A∗ × B ∗ ,
hence, to an element of A ⊗max B. Thus, the maximal tensor product captures all
non-signaling states—at least, insofar as we regard bipartite states as determined by
joint probability assignments to pairs of local measurement outcomes. This last assumption, sometimes called local tomography or local observability, is well-known to be
violated by real quantum mechanics in which the composite of two systems described
by n-dimensional real Hilbert spaces is taken to be the state space of the tensor
6

<!-- page 7 -->
product of the two Hilbert spaces. Attempts to similarly describe the composite of
two quaternionic quantum systems are even more problematic: the state space over a
tensor product of quaternionic “Hilbert spaces” is too small to accomodate even the
product states. Local tomography is therefore often suggested [3, 20, 12, 4, 15, 14] as
a possible axiom for quantum theory. We shall adopt it here as a working assumption.
More generally, we can consider the space (A∗ ⊗ B ∗ )∗ of bilinear forms on A∗ × B ∗ ,
equipped with any cone lying between the minimal and maximal ones, as “a tensor
product” of A and B. (Note that as we are in finite dimensions, (A∗ ⊗B ∗ )∗ and A⊗B
are isomorphic as vector spaces. In what follows, we shall write AB, generically, for
such a composite. 5
If F+ is a face of A+ , then any choice of composite AB induces a canonical choice for
a composite of F and B, which we denote by F B. It consists of those states whose
A-marginals lie in F , and is easily seen to be a face of AB. For G a face of B, AG is
defined similarly. We also write F G, for the face F B ∩ AG.
For the purposes of this paper, we may understand by the phrase physical theory, a
class of abstract state spaces, closed under the formation of such a product, so as to
allow the representation of composite systems. In a more complete treatment of this
idea, one may take a theory to be a category of abstract state spaces, with morphisms
corresponding to the processes allowed by the theory. For some further development
of this idea, see [10, 11]. In accordance with our standing assumption, we here
consider only finite-dimensional theories, i.e., those consisting of finite-dimensional
state spaces.

3

Weak self-duality

A bipartite state on a composite system AB, represented by a positive bilinear form
ω : A∗ × B ∗ → R, can also be represented by a positive map ω̂ : A∗ → B = B ∗∗
defined by ω̂(a)(b) = ω(a, b). Note that we then have ω̂(uA ) = ω B , the B marginal
of ω. Notice also that the adjoint map ω̂ ∗ : B ∗ → A∗∗ = A represents the same
state, evaluated in the opposite order, i.e, ω̂ ∗ (b)(a) = ω̂(a)(b) = ω(a, b). Hence,
ω̂ ∗ (uB ) = ω A . (Conversely, any positive linear map taking uA to a normalized state
of B defines a normalized bipartite state in A ⊗max B.)
Definition 3.1. An abstract state space A is weakly self-dual iff there exists an
order-isomorphism η : A∗ ≃ A.
5

We might, abandoning local tomography, also consider still larger spaces, of which A ⊗ B is only
a quotient. Indeed, this is necessary to accommodate the states on the usual tensor product of real
Hilbert spaces, as a composite state space.

7

<!-- page 8 -->
Multiplying by a sufficiently large or small positive scalar if necessary, one can assume
in the above definition that η(uA ) =: αo ∈ ΩA , i.e., η defines a bipartite state. It
follows that η −1 (αo ) = uA , so η −1 is a bipartite effect. [HB: Not clear to me this
follows. More argument needed...perhaps define isomorphism effect earlier and use
its properties?]
Definition 3.2. A bipartite state ω in A ⊗max B is an isomorphism state iff ω̂ :
A∗ → B is an order isomorphism.
The existence of a composite containing isomorphism states is far from guaranteeing
the weak self-duality of A or B; indeed, for any state space B, there is a state space
A whose positive cone is isomorphic to the dual of B’s, hence for which A ⊗max B
contains isomorphism states. But the existence of an isomorphism state in A ⊗ A
obviously does imply that A is weakly self-dual. We call such a state an automorphism
state.
If ω is a state on AB, and τ : A → A and η : B → B are automorphisms of A and
B, respectively, then η ◦ ω̂ ◦ τ ∗ defines another isomorphism state, with
(η ◦ ω̂ ◦ τ ∗ )(a)[b] = ω(τ a, η ∗ b).
Theorem 3.3. Let A be an irreducible ordered linear space. Then automorphisms of
A lie on extremal rays of the cone L+ (A, A) of positive maps from A to A.
Proof of Theorem: Let χ be an automorphism on A+ . Suppose χ = ψ + µ, where
ψ, µ : A → A are positive maps. Let x 6= 0 be extremal in A+ ; then χ(x), ψ(x), µ(x)
are also extremal, whence, as χ(x) = ψ(x) + µ(x), there are constants cx , dx ≥ 0 with
ψ(x) = cx χ(x)

(1)

µ(x) = dx χ(x)

(2)

cx + d x = 1

(3)

We will show that cx and dx are independent of x, so that ψ = cχ and µ = dχ.
It will be sufficient to prove this for x ranging over the elements of a basis E = {xi }
for A consisting of extremal elements of A+ . Let S ⊆ E be maximal with respect to
the property that
cx = c′x and dx = d′x
for all x, x′ ∈ S. We claim that S = E. To see this, suppose y is any extremal
element ofP
A+ , and let Sy be the support of y in E. Expanding y in the
P basis E, we
have y = i ti χ(xi ).PFrom (1) and (2), we have ψ(y) = cy χ(y) = cy i ti χ(xi ) and
µ(y) = dy χ(y) = dy i ti χ(xi ), with cy + dy = 1 from (3). Alternatively, expanding y
8

<!-- page 9 -->
P
P
P
before
applying ψ and µ gives ψ(y) = i ti ψ(xi ) = i ti cxi χ(xi ), µ(y) = i ti µ(xi ) =
P
basis as well.
i αi dxi χ(xi ). Since {xi } is a basis and χ an automorphism,
P{χ(xi )} is aP
But
the
expansion
of
an
element
in
a
basis
is
unique.
So
c
t
χ(x
)
=
y
i
i i
i ti cxi χ(xi ),
P
P
dy i ti χ(xi ) = i ti dxi χ(xi ), and thus for all i, either ti = 0 or cy = cxi and dy = dxi .
Thus, if Sy ∩ S 6= ∅, the set Sy ∪ S again enjoys the property that the coefficients
cxi and dxi are constant; since S is maximal with respect to this property, Sy ⊆ S.
Letting K(S) denote the cone A+ ∩ span(S), we now see that every extremal point of
A+ lies either in K(S) or in K(E \ S). That is, A+ is the direct convex sum of K(S)
and K(E \ S). As A+ is irreducible, we must have K(E \ S) = {0}, i.e., S = E. This
completes the proof

Example 3.4. Automorphisms need not be extremal in reducible cones.
Consider the cone in two dimensions with extreme rays along the positive x and y
axes. Consider the convex base with extreme points (0, 1) and (1, 0), and let χ be
the automorphism such that χ(x, y) = (2x, y). Let ϕ, µ be automorphisms such that
ϕ(x, y) = (x/2, y/2), µ(x, y) = (3x/2, y/2). Then for all (x, y), χ(x, y) = ϕ(x, y) +
µ(x, y). But ϕ and µ are not multiples of χ. Thus the automorphism χ is not
extremal.
△
Note that if A ≃ B, say by an isomorphism η : B ≃ A, then there is an orderisomorphism L(A, B) ≃ L(A, A) given by ϕ 7→ η ◦ ϕ, where ϕ : A → B. Thus,
Theorem 3.3 tells us that order-isomorphisms (if any exist) are extremal in the cone
of positive linear maps between any two finite-dimensional ordered linear spaces. In
particular, if A and B are abstract state spaces, then if we interpret positive linear
maps A∗ → B as bipartite states between A and B, we have
Corollary 3.5. If A is an irreducible abstract state space, then isomorphism states
(if any exist) are pure in A ⊗max B.
We will say a positive map ϕ : A → B between ordered linear spaces A and B factors
isomorphically through a face F+ of A+ if there exists a positive, idempotent linear
map p : A → F such that p(A+ ) = F+ , and ϕ = ϕ′ ◦ p, where ϕ′ : F+ → Y is
an order-isomorphism from F onto the span of a face of Y . We have the following
extension of Theorem 3.3:
Corollary 3.6. Let ω be a state in A ⊗max B. If ω̂ : A∗ → B factors isomorphically
through an irreducible face of A∗ then it lies on an extremal ray in the cone of positive
maps from A∗ to B.
Proof: Let A and B be finite-dimensional ordered linear spaces with regular cones
A+ and B+ . Suppose a positive surjection ϕ : A → B factors as ϕ = ϕ′ ◦ p where
p : A → F is a positive idempotent projecting A onto the span of a face F+ of A+ .
9

<!-- page 10 -->
Assume ϕ′ is an order-isomorphism, hence, extremal in L+ (F, B). We’d like to show
that ϕ is extremal in L+ (A, B).
To this end, let ϕ = α + β where α, β ∈ L+ (A, B). It will be enough to show α and
β are multiples of one another. Let x ∈ A be extremal. We can decompose x as
x = x0 + x1 where x1 ∈ im(P ) and x0 ∈ ker (P ) = ker (ϕ). Now
α(x0 ) + β(x0 ) = ϕ(x0 ) = 0.
Hence, α = −β on ker (P ). Also,
α(x1 ) + β(x1 ) = ϕ′ (x1 )
for all x1 ∈ im+ (p), so, by the extremality of ϕ′ and x1 , we have
α(x1 ) = cϕ′ (x1 ) and β(x1 ) = dϕ′ (x1 )
for all x1 ∈ im(P ), with c, d ≥ 0 and c + d = 1. We wish to show, then, that
α(x0 ) = β(x0 ) = 0 for all x ∈ A—equivalently, for all x0 ∈ ker (ϕ) = ker (p). To see
this, let y ∈ F+ be extremal. Since p takes A+ onto F+ , we can find some x1 ∈ A+
with p(x1 ) = y. Since ϕ′ : F+ ≃ B is an order-isomorphism, we have ϕ(x) = ϕ′ (p(x1 ))
extremal in B+ for any x = x1 + x0 with x0 any element of ker p. From the discussion
above, we have
α(x1 ) = ϕ(x) − α(x0 ) = ϕ(x) + β(x0 ), and also β(x1 ) = ϕ(x) − β(x0 ).
As α and β are positive maps, α(x1 ) and β(x1 ) lie in B+ . Since ϕ(x) is extremal
and ϕ(x) ± β(x0 ) ≥ 0, it must be that β(x0 ) is a non-negative multiple of ϕ(x). A
similar argument shows that α(x0 ) is a non-negative multiple of ϕ(x). But then, as
α(x0 ) = −β(x0 ), we must have α(x0 ) = β(x0 ) = 0.


4

Purification

An important fact about quantum states is that they can be purified: any state is
the marginal of a pure bipartite state. One would like to know to what extent this is
true more generally. Within the general framework developed above, we can already
obtain, fairly easily, some remarkably strong results in this direction.
Given an abstract state space (A, u), we can turn A∗ into an abstract state space by
using any interior state αo ∈ A+ as the order unit. We shall write A , generically, for
such a state space (A∗ , αo ), leaving the choice of αo tacit. Since the latter choice is,
in general, not at all canonical, there are generally many non-isomorphic state spaces
10

<!-- page 11 -->
related to A in this way, none of which has any special status as “the dual” of A.
Nevertheless, these spaces are useful. For one thing, the identity map A → A can be
interpreted as an isomorphism (hence, by Theorem 3.3, pure if A is irreducible) state
in A ⊗max A having αo as its A-marginal. In this sense, every state interior to A
has a purification. In general, however, the “ancilla” A in terms of which αo ∈ A is
purified, depends on αo .
Theorem 4.1. The following are equivalent:
(a) A is homogeneous;
(b) Every normalized state in the interior of A+ is the A-marginal of an isomorphism state in B ⊗max A, where B is any (fixed) state space order-isomorphic
to A∗ .
This gives us a physical interpretation of homogeneity: first, that the various “dual”
abstract state spaces A = (A∗ , αo ) are all isomorphic, not only as ordered linear
spaces but as abstract state spaces (although not necessarily in a canonical way), and
second, as telling us that in the irreducible case, all interior states of A can be purified
to isomorphism states using a fixed ancilla, namely, any choice of A . (Note, too,
that because the dual of a homogeneous cone is homogeneous, condition (b) is also
equivalent to the homogeneity of A∗ .)
Proof: (a) ⇒ (b) Consider an order-isomorphism η : B ∗ → A. Define η(uB ) =: αo ,
∗
then since uB is in the interior of B+
, αo belongs to the interior of A+ . Since the
latter is homogeneous, for any normalized state α we can find some order-isomorphism
τ : A ≃ A with α = τ (αo ); thus, α = (τ ◦ η)(uB ). Note that as α ∈ ΩA , it follows
that τ ◦ η defines a normalized bipartite state, with marginal α.
(b) ⇒ (a): Let α, β be any two elements of int A+ . Let tα, sβ be the normalized
versions of α and β, with t, s > 0. Let ωα , ωβ be the isomorphism states on B ⊗max A
with A-marginals tα, sβ respectively, whose existence is guaranteed by (b). That is,
ω̂α (uB ) = tα, ω̂β (uB ) = sβ. The automorphism (s/t)ω̂β ◦ ω̂α−1 takes α to β, so A is
homogeneous.

In the case that A is weakly self-dual, we can use an order-isomorphism η : A∗ ≃ A
to identify A with A , using αo = η(uA ). Applying the preceding Theorem, we have
Corollary 4.2. For any irreducible state space A, the following are equivalent:
(a) A is weakly self-dual and homogeneous;
(b) Every normalized state in the interior of A+ is the marginal of an isomorphism
state in A ⊗max A.
11

<!-- page 12 -->
Remark: Recently, Chiribella, D’Ariano and Perinotti [15] have examined the consequences of assuming, as an axiom, that all states dilate to a pure state that is unique
up to a reversible transformation on one marginal. We note that if α ∈ ΩA can be
achieved as the marginal of two isomorphism states ω and µ in the same composite
BA (so B ∗ ≃ A, say via an isomorphism σ), so that α = ω̂(uB ) = µ̂(uB ), then
τ := ω̂ ◦ µ̂−1 is a unit-preserving order-automorphism of B ∗ , and ω(a, b) = µ(τ (a), b).
We are using the convention ω̂ : B ∗ → A; τ is a reversible map acting on B ∗ (note
that unit preservation is the condition dual to base preservation). So for the set of
isomorphism states having α as A-marginal, the dilation condition is met; in constructing a composite, uniqueness can be ensured by including no other pure states
with α as marginal, in the extreme generators of the composite cone.

5

Steering

P
By an ensemble for a state β ∈ B, we mean a finite set of βi ∈ B+ such that i βi = β.
Note that we defined ensembles not as lists of probabilities and associated normalized
states, but as lists of unnormalized states; the two definitions are
as the
Pequivalent,
6
B
norms uB (βi ) of the βi encode the probabilities. Indeed, from i βi = ω and the
positivity of the βi , it follows
(βi ),
P
P that uBB (βi ) must be probability weights, 0 ≤ uB
B
i uB (βi ) = 1. If instead
i βi ≤ ω is required, we have a subensemble for ω .
As discussed in Section 1, pure quantum-mechanical states have the interesting property that any ensemble for either marginal state can be realized as the conditional
states arising from a suitable choice of observable on the other wing of the system.
Generalizing, we are led to the following
Definition 5.1. A bipartite state ω ∈ A ⊗max BPis steering for its B marginal iff,
for every ensemble (convex decomposition) ω B = i βi , where βi are un-normalized
states of B, there exists an observable E = {xi } on A with βi = ω̂(xi ). We say that
ω is bisteering iff it’s steering for both marginals.
If α is any state on A and β is a pure state on B, then ω = α ⊗ β is trivially steering
for ω B = β since the latter has no non-trivial ensembles. If α is mixed, then ω will
not be steering for ω A . On the other hand, any pure product state is steering, as
is any isomorphism state. In light of Theorem 4.2, this might suggest that steering
states are always pure. But that is not correct. Indeed, any classical bipartite state
exhibiting perfect correlation between its marginals is steering for both its marginals.
(This is closely related to Example 2.4 above.)
6

Although we will not need it, there is a unique norm, called the base norm, that agrees with the
linear functional uB on B+ , so the terminology is justified.

12

<!-- page 13 -->
It follows almost immediately from the definition, that if ω is steering for its Bmarginal, ω̂(A+ ) is a face of B+ . Indeed, we have
Lemma 5.2. If ω is steering, then ω̂(A+ ) = Face(ω B ).
Proof: Suppose that β1 , β2 ∈ B+ with β1 + β2 ∈ ω̂(A+ )—say, βi = ω̂(ai ) where
ai ∈ A∗ + . Since uA is an order unit for A∗+ , we can find a scalar t > 0 such that
t(a1 + a2 ) ≤ uA , whence,
tβ1 + tβ2 = ω̂(t(a1 + a2 )) ≤ ω̂(uA ) = ω B .
Thus, {tβ1 , tβ2 } is a sub-ensemble for ω B . Since ω steers ω B , tβ1 and tβ2 —and hence,
also β1 and β2 —lie in ω̂(A+ ). This shows that ω̂(A+ ) is a face of B+ . Notice that the
argument also shows that ω B is an order unit for ω̂(A+ ); hence, the latter is exactly
Face(ω B ).

The converse, however, is not true: a state may satisfy ω̂(A+ ) = Face(ω B ) but not
be steering, as in the following example.
Example 5.3. A+ is the simplicial cone R3+ , B+ is R2+ , with the usual order units
(1, 1, 1) and (1, 1) respectively, and ω(a, b) is determined by the following table of
probabilities:
x
y
x 1/4 0
(4)
y 0 1/4
z 1/4 1/4
The row index ranges over the values x := (1, 0), y := (0, 1) for a, the column index
b ranges over the values x := (1, 0, 0), etc..
We see that ω̂(x) = (1/4, 0), ω̂(y) = (0, 1/4), and ω̂(z) = (1/4, 1/4), while ω̂(u) =
ω̂(x + y + z) = (1/2, 1/2). The image of the order interval [(0, 0, 0), (1, 1, 1)] of R3+
under ω̂ is the hexagon with vertices (0, 0), (1/4, 0), (0, 1/4), (1/2, 1/4), (1/4, 1/2),
(1/2, 1/2). This is a proper subset of the interval [0, π((1, 1, 1))], which is the square
with vertices (0, 0), (1/2, 0), (0, 1/2), (1/2, 1/2). So as claimed, even though π(u) is
the desired order unit in R2+ , the image π([0, u]) of the unit interval in R3 , while it
generates R2+ , is not a unit interval (for any ordering of R2 ).
In particular, the ensemble (0, 1/2), (1/2, 0) for ω B = (1/2, 1/2) can not be represented as ω̂(a1 ), ω̂(a2 ) for any elements a1 , a2 ∈ [0, uA ]—much less with a1 , a2 summing
to uA . Accordingly, ω is not steering.
△
In fact, the condition that ω be steering for its B-marginal places a very strong and
subtle constraint on ω̂. If X and Y are partially ordered sets, an order-preserving
13

<!-- page 14 -->
surjection p : X → Y is a quotient map iff, for all y1 , y2 ∈ X, y1 ≤ y2 iff yi = p(xi )
for some x1 ≤ x2 in X. We shall say that p is a strong quotient map iff it has
the property that every chain y1 ≤ y2 ≤ · · · ≤ yn in Y is the image of some chain
x1 ≤ x2 ≤ · · · ≤ xn in X, i.e., y1 = p(x1 ), y2 = p(x2 ), ..., yn = p(xn ). Evidently, a
strong quotient map is a quotient map (just apply the definition to chains of length
2), but the converse is, in general, false.
Theorem 5.4. Let ω be a bipartite state in AB. Then ω is steering for its B marginal
iff ω̂ : [0, uA ] → [0, ω B ] is a strong quotient map of ordered sets.
Proof: First, suppose ω is steering, and let 0 ≤ β1 ≤ β2 ≤ · · · βk−1 ω B . Then {β1 , β2 −
β1 , . . . , βk−1 − βk−2 , ω B − βk−1 } is an ensemble for ω B ; as ω is steering, there is an
observable {a1 , a2 , a3 , ..., ak } on A with ω̂(a
P1 ) = β1 , ω̂(a2 ) = β2 − β1 , . . . , ω̂(ak ) =
B
ω − βk−1 . In particular, defining bj =
i≤j aj , we have ω̂(bj ) = βj ; since b1 ≤
b2 ≤ · · · βk , ω̂ induces a quotient map of ordered sets [0, uA ] → [0, ω B ]. For the
converse, suppose ω̂ induces such a quotientP
map. For any ensemble {η1 , ..., ηk } for
B
ω , define β1 = η1 , β2 = η2 + η1 , ..., βj = i≤j βi for j ≤ k − 1. By definition of
A
a strong quotient map, there arePthen elements b1 < b2 < ... < bk−1
Pin [0, u ] with
ω̂(bi ) = βi . Setting aj = bj − ( i<j bi ), we have ω̂(aj ) = ηj and j≤k−1 aj = bk .
Thus, {a1 , ..., ak−1, ak := uA − bk } is the desired observable steering to {ηi }.

Remarks: (i) We suspect, but so far have been unable to prove, that a quotient map
of order-intervals [0, u] → [0, v] is necessarily a strong quotient.
(ii) An obvious sufficient condition for ω̂ : [0, uA ] → [0, ω B ] to be a quotient map of
ordered sets is for there to exist an affine section σ : [0, ω B ] → [0, uA ]. However, as
Example A.3 in Appendix A shows, this is not necessary for steering.
It follows from Theorem 5.4 that the ordering of Face(ω B ) = ω̂(A+ ) is exactly the
quotient linear ordering induced by the linear surjection ω̂, i.e., β1 ≤ β2 in Face(ω B )
iff βi = ω̂(ai ) for some a1 , a2 ∈ A with a1 ≤ a2 . It also follows that if ω̂ is injective,
it is an order isomorphism. This last point is important enough to record as
Corollary 5.5. et ω be steering for ω B , where ω B is interior to B+ , so that Face(ω B ) =
B+ . If ω̂ is injective (non-singular), then ω̂ is an order isomorphism. If B+ (and
therefore A+ ) is irreducible, therefore, by Theorem 3.3, it is pure in A ⊗max B.
In other words, if A and B have the same dimension, then the states that are steering
for an interior marginal are precisely the isomorphism states (and hence steering for
both marginals).
We are now in a position to make good on the claim made in the introduction.
14

<!-- page 15 -->
Definition 5.6. A probabilistic theory supports universal steering if, for every system
B in the theory and every state β ∈ B, there exists a system Aβ and a bipartite state
ω in Aβ ⊗ B that steers its B-marginal ω B = β. A theory supports uniform universal
steering if, for every system B in the theory, there exists a system AB such that for
every state β ∈ A, there exists a state ω in AB ⊗ B that steers its B-marginal β.
A probabilistic theory supports universal self-steering if, for every system A in the
theory, every state α ∈ A can be represented as a marginal of some bipartite state on
two copies of A—that is, some state ω ∈ AA—steering for that marginal. (That is,
it supports uniform universal steering with AB ≃ A.)
Corollary 5.5, combined with Theorem 4.1, establish
Proposition 5.7. In any theory that supports universal uniform steering, every irreducible, finite-dimensional state space in the theory is homogeneous.
In light of Corollary 4.2, we also have
Proposition 5.8. In any theory that supports universal self-steering, every irreducible, finite-dimensional state space in the theory is homogeneous and weakly selfdual.
If a theory supports universal self-steering, and also has the property that every direct
summand of a state space is again a state space belonging to the theory (a reasonable
requirement, at least in finite dimensional settings), then every finite-dimensional
state space in the theory is a direct sum of homogeneous, weakly self-dual factors,
hence, homogeneous and weakly self-dual.7
An interesting question is to what extent the gap between universal steering and
uniform universal steering is a genuine one. One might investigate this question by
looking for examples of state spaces for which each state can be steered, but that are
not homogeneous.
Remark: A particularly strong “steering” axiom would require that, for every state α
of every system A in the theory, there exist a steering state ω on a composite AA of
two copies of A, having both marginals equal to α. Such a theory must be “monoentropic” in the sense that measurement and mixing entropies of states coincide, as
7

It is easily seen that direct sums of homogeneous or weakly self-dual cones are, respectively,
homogeneous or weakly self-dual. For weak self-duality, one just proves that any sum of isomorphisms
αi : Ai → Bi of direct summands, is an isomorphism of the direct sums ⊕i Ai and ⊕i Bi . For
homogeneity, one uses the fact that the interior of the positive cone of a direct sum consists precisely
of sums of P
interior points of the positive
cones of all summands. Then to get from any such interior
P
point x = i xi to any other y = i yi , one uses a sum of automorphisms αi of the summands Ai ,
chosen (as homogeneity of each Ai+ ensures is possible) such that αi (xi ) = yi .

15

<!-- page 16 -->
discussed in [7]; states in such a theory must also be spectral, in the sense of [32].
Further elaboration of these points can be found in Appendix B of [7].

6

Conclusion and discussion

We have shown that the state spaces of any probabilistic theory that allows for uniform universal ensemble steering, in the sense that for every system A in the theory,
there’s another system B such that every state on system A can be steered by some
state in the composite BA, are homogeneous. We say that system B steers system
A, in this case. If we require systems to be self -steering (i.e., that each system A
steer itself ), they must be homogeneous and weakly self-dual. If one could motivate the stronger assumption that these state spaces are strongly self-dual, then the
Koecher–Vinberg Theorem [25, 30], together with the Jordan–von Neumann–Wigner
classification theorem [22], would imply that all state spaces are those of formally real
Jordan algebras. In our finite dimensional setting, this means that their normalized
state spaces are convex direct sums of sets affinely isomorphic to the unit-trace elements in the cones of positive semidefinite matrices in a real, complex, or quaternionic
matrix algebra, or to Euclidean balls, or to the unit-trace 3 × 3 positive semidefinite
matrices over the octonions.
From here, our standing assumption of local tomography (that bipartite states are
determined by the probabilities they assign to product effects) restricts the possibilities further. A theorem of Hanche-Olsen [19] asserts that any JB-algebra A (which
includes all formally real Jordan algebras, at least in finite dimension) whose vectorspace tensor product with the self-adjoint part of M2 (C)—that is, with a qubit—can
be made into a JB tensor product, is isomorphic to the self-adjoint part of a (complex) C ∗ -algebra. In other words, it is essentially quantum-mechanical. As we will
establish elsewhere, Hanche-Olsen’s requirements for a JB tensor product impose on
the cones associated with the three JB-algebras in question, exactly the operational
requirements we’ve imposed on a composite of state spaces. Thus, Hanche-Olsen’s
result implies that if a homogeneous, self-dual state space has a locally tomographic
homogeneous, self-dual composite with a qubit, then it is the state space of a C ∗ algebra — so, a direct sum of the state spaces of standard quantum theory.
Therefore, if a self-dual physical theory makes room for qubits, and permits universal self-steering, its state spaces are essentially quantum-mechanical, in the fairly
standard sense that uses the complex field, but extended to allow for superselection
sectors (direct summands).
These considerations trace a route, within a broad landscape of locally tomographic
16

<!-- page 17 -->
non-signaling theories, from the single information-theoretic feature of quantum states
that most puzzled Schrödinger—the possibility of steering—to the full mathematical
apparatus of (finite-dimensional) C ∗ -algebraic quantum mechanics. This route is
interrupted by a gap: that between weak and strong self-duality. There may be ways
to bridge this gap. One strategy for doing so can be found in [32].
On the other hand, it would also be interesting to see whether a complete and selfconsistent theory can be constructed using only weakly self-dual state spaces, that
still allows for universal steering. An essential step towards constructing such a
theory would be to find a class of weakly, but not strongly, self-dual, homogeneous
state spaces that is closed under some reasonable non-signaling tensor product. A
plausible idea is to include all steering states, but as discussed in Appendix B, it does
not work. We are investigating other possibilities based on keeping a rich supply of
steering states. Of course, should it prove that any category of homogeneous, weaklyself-dual state spaces that admits a reasonable tensor product must be strongly selfdual then the gap mentioned above will turn out to have been only an illusion, and
quantum theory, in the C ∗ -algebraic sense, will be naturally characterized, at least
in finite dimension, in terms of steering and the existence of a locally tomographic
nonsignaling tensor product.8
Finally, we mention that additional information-processing properties provide some
motivation for weak self-duality, both via steering, and more directly. For example,
in [8] it was shown that an exponentially secure bit commitment protocol, based on
the nonuniqueness of convex decomposition in nonclassical state spaces, exists in any
theory which has at least some nonclassical state spaces, coupled only by the minimal
tensor product (so that there is no entanglement). But in a nonclassical theory in
which all states can be steered, this type of bit commitment protocol cannot exist.
This does not provide a tight connection between steering and no-bit-commitment;
other types of bit commitment protocols might be able to coexist with steering. But
it is suggestive. Another connection is between weak self-duality and teleportation: if
it is possible, to conclusively teleport a system through a copy of itself with nonzero
success probability, then it must be weakly self-dual [6].9
8

We note that our notion of tensor product is less innocuous than might be evident, as it requires
the positivity of bipartite states on all product effects, which, for example, need not be required in
a theory in which only a subcone of A∗+ is considered to represent operationally relevant effects on
which positivity is to be required.
9
This also requires that all composites AB, A′ B ′ of isomorphic systems A ≃ A′ , B ≃ B ′ ,
contained in the theory, be isomorphic.

17

<!-- page 18 -->
Acknowledgments
This research was supported by the United States Government through grant OUR0754079 from the National Science Foundation. It was also supported by Perimeter
Institute for Theoretical Physics; work at Perimeter Institute is supported in part by
the Government of Canada through Industry Canada and by the Province of Ontario
through the Ministry of Research and Innovation. HB and AW also wish to thank:
Samson Abramsky and Bob Coecke for extending them the hospitality of the Oxford
University Computing Laboratory during November of 2009, when parts of this paper
were written; C. Martin Edwards for referring us to the work of H. Hanche-Olsen;
the Foundational Questions Institute and and the University of Cambridge’s DAMTP
for sponsoring the workshop Operational Probabilistic Theories as Foils to Quantum
Theory, Cambridge (U.K.), July 2007, where some of these ideas were initially presented and their development into the present paper begun. Further work was done
at other workshops and conferences: we thank Renato Renner, Oscar Dahlsten, and
the the Pauli Center for Theoretical Studies and the initiative “Quantum Science
and Technology” at ETH Zürich, for sponsoring the workshop “Information Primitives and Laws of Physics”, March, 2008; Jeffrey Bub, Robert Rynasiewicz, and the
University of Maryland, College Park and Georgetown University for organizing and
sponsoring New Directions in the Foundations of Physics, May 2008; Hans Briegel,
Bob Coecke, and the other organizers and the European network QICS, the EPSRC,
and the IQOQI of the Austrian Academy of Sciences for the workshop “Foundational
Structures for Quantum Information and Computation”, September 2008.

References
[1] S. Abramsky and B. Coecke, A categorical semantics of quantum protocols, in
Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science:
LICS 2004, pp. 415–425, IEEE Computer Society (2004); also quant-ph/0402130v5
(2004).
[2] E. M. Alfsen, Compact Convex Sets and Boundary Integrals, Springer, 1971.
[3] H. Araki, On a characterization of the state space of quantum mechanics, Comm.
Math. Phys. 75, 1-24 (1980).
[4] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Cloning and broadcasting in
generic probabilistic theories (2006) (arXiv:quant-ph/061129).
[5] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Generalized no-broadcasting
theorem, Phys. Rev. Lett. 99 240501 (2007). Also arXiv:0707.0620.
18

<!-- page 19 -->
[6] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Teleportation in general probabilistic theories, in Proceedings of the Clifford Lectures, Tulane University, March
12-15, 2008, to appear in Proceedings of Symposia in Applied Mathematics (AMS);
also arXiv:0805.3553 (2008).
[7] H. Barnum, J. Barrett, L. Clark, M. Leifer, R. Spekkens, N. Stepanik, A. Wilce,
and R. Wilke, Entropy and Information causality in general probabilistic theories,
arXiv:0909.5075(2009).
[8] H. Barnum and O. Dahlsten and M. Leifer and B. Toner, Nonclassicality without
entanglement enables bit commitment, Proc. IEEE Information Theory Workshop,
Porto, May 2008, arXiv:0803.1264 (2008).
[9] H. Barnum, C. Fuchs, J. Renes and A. Wilce, Influence-free states on compound
quantum systems, quant-ph/0507108 (2005).
[10] H. Barnum and A. Wilce, Information processing in convex operational theories
(2009) (arXiv:0908.2352). To appear in a special issue of Electronic Notes in Theoretical Computer Science: Proceedings of QPL/DCM (Quantum Physics and Logic
/ Developments in Computational Models), Reykjavik, July 12-13, 2008.
[11] H. Barnum and A. Wilce, Ordered linear spaces and categories as frameworks for
information-processing characterizations of quantum and classical theory (2009);
also arXiv:0908.2354.
[12] J. Barrett, Information processing in general probabilistic theories, Phys. Rev.
A 75 032304 (2007); also arXiv:quant-ph/0508211.
[13] C.H. Bennett and G. Brassard, Quantum cryptography: public key distribution
and coin tossing, Proceedings of IEEE International Conference on Computers
Systems and Signal Processing, Bangalore India, December 175-179 (1984).
[14] B. Dakic and C. Brukner, Quantum theory and beyond: is entanglement special?
arXiv:0911.0695 (2009)
[15] G. Chiribella, G. M. D’Ariano and P. Perinotti, Reversible realization of physical
processes in probabilistic theories (2009) (arXiv:0908.1583).
[16] E. B. Davies and J. T. Lewis, An operational approach to quantum probability,
Comm. Math. Phys. 17 239-260 (1970).
[17] C. M. Edwards, The operational approach to algebraic quantum theory I, Comm.
Math. Phys. 16 207–230 (1970).
[18] D. J. Foulis and C. H. Randall, Empirical Logic and Tensor Products, in Interpretations and Foundations of Quantum Mechanics, H. Neumann, ed., Bibliographisches Institut, Wissenschaftsverlag, Mannheim, 1981.
19

<!-- page 20 -->
[19] H. Hanche-Olsen, JB-algebras with tensor products are C ∗ -algebras, Lecture
Notes in Mathematics (Springer) 1132 pp. 223-229 (1985).
[20] L. Hardy, Quantum theory from five reasonable axioms, quant-ph/00101012.
See also L. Hardy, A framework for probabilistic theories with non-fixed causal
structure, J. Phys. A. 40 3081 (2007).
[21] L. P. Hughston, R. Jozsa, and W. K. Wootters, A complete classification of
quantum ensembles having a given density matrix, Phys. Lett. A 183, 14-18 (1993).
[22] P. Jordan, J. von Neumann and E. P. Wigner, On an algebraic generalization of
the quantum-mechanical formalism, Annals of Mathematics 35, 29-64 (1934) .
[23] M. Kläy, Einstein-Podolsky-Rosen experiments: the structure of the sample
space, Foundations of Physics Letters 1, 205-244 (1988).
[24] M. Kläy, C. H. Randall and D. J. Foulis, Tensor products and probability weights,
Int. J. Theor. Phys. 26, 199-219 (1987).
[25] M. Koecher, Die geodätischen von positivitätsbereichen, Math. Annalen 135,
192-202 (1958).
[26] G. Mackey, Mathematical Foundations of Quantum Mechanics, Addison Wesley,
1963.
[27] M. Pawlowski, T. Paterek, D. Kazlikowski, V. Scarani, A. Winter and
M. Żukowski, et al. A new physical principle: Information causality (2009)
(arXiv:0905.2292).
[28] E. Schrödinger, Probability relations between separated systems, Proceedings of
the Cambridge Philosophical Society 32 446-452 (1936).
[29] F. W. Shultz, Journal of Combinatorial Theory A 17 317 (1974).
[30] E. B. Vinberg, Homogeneous cones, Dokl. Acad. Nauk. SSSR 141 (1960) 270273; English trans. Soviet Math. Dokl. 2, 1416-1619 (1961).
[31] A. Wilce, Tensor products in generalized measure theory, Int. J. Theor. Phys.
31, 1915 (1992) .
[32] A. Wilce, Four and a half axioms for finite dimensional quantum mechanics,
arXiv:0912.5530.

20

<!-- page 21 -->
A

Examples for Section 5

Example A.1. An example where there is a section that enables steering.
Consider the following state in the maximal tensor product of two state spaces with
square base. We’ll view this as the state space of two two-outcome tests {a, a′ } and
{b, b′ }, and also identify a, a′ , b, b′ with the atomic effects in the dual cone. We’ll label
each of the four vertices of the normalized state space by the two atomic effects it
makes certain: ab, ab′ , a′ b, a′ b′ . Writing, e.g. ab ⊗ a′ b′ for a bipartite product state,
the state:
1
(5)
ω = (ab ⊗ ab + a′ b ⊗ a′ b)
2
has
1
1
(6)
ω̂(a) = ab, ω̂(a′ ) = a′ b ,
2
2
so measuring {a, a′ } on the first system gives the ensemble { 12 ab, 12 a′ b} for the secondsystem marginal ω B = 21 (ab + a′ b). Face(ω B ) is generated as nonnegative linear
combinations of ab and a′ b, and is thus a two-dimensional ordered subspace of the
three-dimensional state space of the second system. Its unit interval is the square that
is the convex hull of (0, 0), ab/2, a′b/2, (ab + a′ b)/2. The quotient of the first system
space, A, by the kernel of the linear map ω̂, can be represented by setting up the
state space to have 90◦ opening angle between opposite extremal rays, and taking the
orthogonal (90◦ ) projection onto the plane normal to the ray b′ , i.e. the projection
along the ray generated by b′ . This indeed gives a two-dimensional classical state
space, i.e. one isomorphic to Face(ω B ). Moreover, there is an affine section σ of this
quotient map into A∗+ , given by inverting the relations (6), thus allowing us to map
the unit interval [0, ω B ] in Face(ω B ) to the diagonal cross section, in the a, a′ plane,
of the unit interval of A∗+ . σ ◦ π is indeed a positive projection on A∗+ , namely the
orthogonal projection onto this plane.
△
For the state (5), the mentioned section is the only affine section over Face(ω B ). A
slight modification, however, gives an example in which many affine sections exist.
Example A.2. An example in which there are many affine sections over
the image of the order unit. Let
1
ω̂ = (x ⊗ ab + y ⊗ a′ b)
2

(7)

with x any state in the line segment [ab, ab′ ] and y any state in the segment [a′ b, a′ b′ ]
respectively. This still gives a state steering for the same marginal ω B = 21 (ab + a′ b)
as in the preceding example. If we choose x = ab, y = a′ b′ , that is,
1
ω̂ = (ab ⊗ ab + a′ b′ ⊗ a′ b) ,
2
21

(8)

<!-- page 22 -->
we can steer the marginal using either of the two observables {a, a′ }, {b, b′ }. In this
case, there are two distinct sections over Face(ω B ) that enable steering.
△
In the example of Eq. (8), the kernel of ω̂ is generated, not by b′ as before, but by
a′ b − ab′ , and the natural way of attempting to represent the quotient map, namely
by projection onto a subspace complementary to the kernel in the original space, if
we project orthogonally in the natural geometry, projects onto the subspace spanned
by ab, a′ b′ , and the order unit, giving a slice of the order interval that includes the
diagonal of the square.
Although the kernel of this map is of course one-dimensional, its positive kernel, which
we’ve claimed must be an exposed face of the state cone, is the trivial such exposed
face: the zero subspace. This example shows that quotients whose positive kernel is
trivial are not necessarily uninteresting or ill-behaved.
Example A.3. An affine section of the order-quotient map is not necessary
for steering. Let A ≃ R4 be an abstract state space whose normalized states form
a cube; its dual cone is a regular polyhedral cone in R4 with octahedral base. The
atomic effects (largest effects on extremal rays of the effect cone) are the vertices of
such an octahedral base. The example has B ≃ R3 ordered by a cone with regular
hexagonal base; the center of the hexagon is a state having three distinct two-state
extremal ensembles, each composed of a pair of opposite vertices of the hexagon (with
weights 1/2 on each one). ω̂ AB is chosen to take the six vertices of the octahedron
of atomic effects in A∗ to the six vertices of the hexagon of states normalized to
1/2, in such a way that opposite vertex-pairs are mapped to opposite vertex-pairs.
This is clearly positive and linear, and maps the order-unit (twice the center of the
octahedron of atomic effects) to the center of the hexagon of normalized states (which
is twice the center of the hexagon of states normalized to 1/2). Face(ω̂ B ) is the entire
hexagonal cone in R3 , so ω̂ is itself (technically, is a representative of) the quotient π.
All three ensembles for ω B consist of extremal states, and because they have unique
ω̂-preimages, a section of ω̂, we know that a section of π must take these, the vertices
of a hexagon, to the vertices of the octahedron, matching opposites to opposites.
But no affine map can do this. The affine span of the hexagonal points has affine
dimension 2, while that of the octagonal ones has affine dimension 3.
△

B

The Steering Product

A physical theory, as distinct from a model of a single physical system, should allow
some device whereby several such models can be combined to yield a model of a
composite system. It is natural to suppose that such a theory constitutes a category
22

<!-- page 23 -->
equipped with a well-behaved tensor product; that is, a symmetric monoidal category
as described in e.g. [1]. This suggests the following problem: given two weakly selfdual state spaces A and B, does there exist a reasonable model for a composite state
space AB that is again weakly self-dual? In light of the connection between weak selfduality and steering, one might consider building a weakly self-dual tensor product
by including all steering states, but as we’ll see, this does not work, even where the
factors are quantum-mechanical.
Note that for non-simplicial weakly self-dual factors, neither the maximal nor minimal
tensor product will be weakly-self-dual, since (A(Ω) ⊗max A(Ω′ ))∗ ∼
= A(Ω)∗ ⊗min
A(Ω′ )∗ ∼
= A(Ω) ⊗min A(Ω′ ) ≇ A(Ω) ⊗max A(Ω′ ).
If A and A′ are order-isomorphic (alternatively, and notationally easier, A = A′ ;
hereafter this will be assumed), one candidate for the weakly self-dual tensor product, namely, the convex hull of the pure tensor states and the isomorphism states.
However, this is unsatisfactory in various ways, not least that it degenerates to the
minimal tensor product if A and B are not isomorphic; also, using this observation,
it’s easy to see that this tensor product is not associative.
A better candidate is the steering product.
Definition B.1. Let A ⊗str B, called the “steering product” of A and B, be A ⊗ B,
ordered by the cone generated by all steering states in A ⊗max B.
As remarked above, pure product states are steering; hence, this is a valid tensor
product in our sense.
Conjecture B.2. ⊗str is associative.
Suppose ηA : A∗ → A and ηB : B ∗ → B are order-isomorphisms implementing the
weak self-duality of A and B. We can use these to convert a state ω̂ : A∗ → B to an
effect
ηAB (ω) := ηB−1 ω̂ηA : A → B ∗
This gives us a linear map ηAB : A⊗max B → A∗ ⊗max B ∗ = (A⊗min B)∗ . Evidently,
this is positive. It is also easy to check that ηAB takes product states to product effects,
and isomorphism states to isomorphism effects.
Question 1. If ω̂ is steering, is ηAB (ω̂) also steering (in some suitable dual sense)?
Fact B.3. If A = B = Lh (C2 )—that is, if A and B are two qubits, then A ⊗str B =
A ⊗max B (which is not weakly self-dual).
Proof: To see this one uses the fact that states in the maximal tensor product all
correspond to positive maps that are decomposable, i.e., sums of completely positive
23

<!-- page 24 -->
and co-completely positive maps. The extremal ones are all either product states,
or isomorphism states, since the automorphism group of a qubit—indeed, of any
quantum system—is generated by the maps X 7→ AXA† for nonsingular A, and any
transpose map X 7→ X t .

One might ask whether if A and B are weakly self-dual, A ⊗str B is too. This is not
so, as the above example of two qubits, combined with observation that the maximal
tensor product of non-simplicial weakly self-dual cones is not weakly self-dual, show.
Same question if A and B are homogeneous.
Question 2. Is the steering-for-both-marginals product equal to the steering-for-onemarginal product? This would follow, for example, from the proposition that every
steering-for-one-marginal state is a convex combination of steering-for-both-marginals
states.
Question 3. Is the steering-for-both-marginals product, perhaps under conditions like
homogeneity of both state spaces, equal to the topological closure of the cone generated by automorphisms?
We don’t know the answer for sure even in the quantum case, because this raises the
question whether states corresponding to nondecomposable maps can be steering. We
conjecture that they cannot, and that therefore the answer is “yes” in the quantum
case.

24
