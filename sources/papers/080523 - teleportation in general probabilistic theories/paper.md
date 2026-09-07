---
type: paper
date: 2008-05-23
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:0805.3553v1)
reviewed: false
---

# Teleportation in General Probabilistic Theories

Machine-generated and unreviewed text extraction of arXiv:0805.3553v1
(13 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/0805.3553v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Teleportation in General Probabilistic Theories
Howard Barnum,1, ∗ Jonathan Barrett,2, † Matthew Leifer,3, ‡ and Alex Wilce4, §
1

CCS-3: Information Sciences, MS B256, Los Alamos National Laboratory, Los Alamos, NM 87545 USA
Perimeter Institute for Theoretical Physics, 31 Caroline Street N, Waterloo, Ontario N2L 2Y5, Canada
3
Institute for Quantum Computing, University of Waterloo, Waterloo, Ontario, Canada
4
Department of Mathematical Sciences, Susquehanna University, Selinsgrove, PA 17870 USA

arXiv:0805.3553v1 [quant-ph] 23 May 2008

2

In a previous paper, we showed that many important quantum information-theoretic phenomena,
including the no-cloning and no-broadcasting theorems, are in fact generic in all non-classical probabilistic theories. An exception is teleportation, which most such theories do not support. In this
paper, we investigate which probabilistic theories, and more particularly, which composite systems,
do support a teleportation protocol. We isolate a natural class of composite systems that we term
regular, and establish necessary and sufficient conditions for a regular tripartite system to support
a conclusive, or post-selected, teleportation protocol. We also establish a sufficient condition for
deterministic teleportation that yields a large supply of theories, neither classical nor quantum, that
support such a protocol.

The standard quantum teleportation protocol [7] allows two parties, Alice and Bob, to transmit an unknown
quantum state from Alice’s site to Bob’s; in compliance
with the no-cloning theorem, Alice’s copy is destroyed in
the process. The protocol assumes that Alice and Bob
have access to the two wings, A and B, of a bipartite system A ⊗ B in a maximally entangled state, which serves
as a kind of quantum channel. The state to be teleported
belongs to an auxiliary system A′ at Alice’s site, which
is coupled to her half of the shared system. Alice measures an observable corresponding to the Bell basis on
the combined system A′ ⊗ A. Depending upon the result, she instructs Bob (via purely classical signaling) to
perform a particular unitary correction on his wing, B,
of the shared A ⊗ B system. With certainty, Alice now
knows that the state of Bob’s system is identical to the
state (whatever it was) of her ancillary system A′ .
The possibility of teleportation is surprising, in view of
the no-cloning and no-broadcasting theorems, which prohibit the copying of quantum information. In a previous
paper [3], we have shown that both no-cloning and nobroadcasting theorems are in fact quite generic features
of essentially any non-classical probabilistic theory, and
not specifically quantum at all. However, as pointed out
in [3, 4], most such theories do not allow for teleportation. Classical theories, however, do. The possibility of
teleportation can thus be regarded, in some very rough
qualitative sense, as a measure of the relative classicality
(or at any rate, tameness) of quantum theory.
In this note, we make some precise statements about
which probabilistic theories—and more particularly,
which tripartite systems—admit teleportation. For simplicity, consider the case in which the three component
systems, A′ , A and B, in the protocol described above
are identical. Then an obvious necessary condition for
the protocol to succeed is that the cone of unnormalized
states in A be isomorphic to the dual cone of unnormalized effects in A∗ —a strong condition that is nevertheless
satisfied by both quantum and classical systems. As

we shall see, this is sufficient to ground conclusive (or
one-outcome post-selected) teleportation. To obtain
deterministic teleportation appears to be more difficult;
however, where the state space has sufficient symmetry,
a sort of deterministic teleportation can always be
achieved with respect to a possibly continuously-indexed
observable. Specializing to the case in which the state
space is symmetric under the action of a finite group, we
obtain a wealth of examples of state spaces that are neither classical nor quantum-mechanical, but nevertheless
support a genuine deterministic teleportation protocol.
1. Probabilistic Models This section assembles the
necessary machinery of generalized probability theory—
essentially, the convex sets framework deriving from the
work of Mackey [17] and subsequently refined by many
authors, notably Davies and Lewis [8], C. M. Edwards [9]
and Ludwig [16]. We use more or less the same notation
as in [4, 5]; as in the latter, in this paper we consider
only probabilistic models having finite-dimensional state
spaces.
Abstract State Spaces We model a physical system by an
ordered vector space A with a (closed, pointed, generating) positive cone A+ , which we regard as consisting
of un-normalized “states”. We also posit a distinguished
order unit, that is, a linear functional uA that is strictly
positive on non-zero positive elements of A; this defines
a compact convex set ΩA = u−1
A (1) of normalized states.
We shall call an ordered linear space, equipped with such
a functional—more formally: a pair (A, uA )—an abstract
state space. If (A, uA ) and (B, uB ) are abstract state
spaces, we write A ≤ B to indicate that (i) A is a subspace of B; (ii) A+ ⊆ B+ ; and (iii) uA is the restriction
of uB to A+ . Similarly, A ≃ B, read “A is isomorphic
to B”, means that there exists an invertible, positive linear mapping A → B, with a positive inverse, and taking
the order unit of A to that of B. Equivalently, such a
mapping takes A’s normalized state space ΩA bijectively

<!-- page 2 -->
2
(and affinely) onto B’s normalized state space ΩB . We
refer to an isomorphism A → A as a symmetry of A. A
positive linear mapping with positive inverse, but that
does not necessarily preserve the order unit, we refer to
as an order isomorphism between A and B, and we say
they are order-isomorphic if such a map exists.
By way of illustration, discrete classical probability
theory concerns the case in which A is the space RE of
all real-valued functions α on a finite set E of measurement outcomes, in the natural point-wise
P ordering. The
order unit is the functional uA (α) := x∈E α(x), hence
the normalized state space ΩA consists of all probability
weights on E. In elementary quantum probability theory, A is the space of Hermitian operators on a complex
Hilbert space H, ordered in the usual way; the order unit
is the trace, so that ΩA is the set of density operators.
Physical events (e.g., measurement outcomes) associated with an abstract state space A are represented by
effects, that is, positive linear functionals f ∈ A∗ with
f (α) ≤ 1 for all α ∈ ΩA , or, equivalently, f ≤ uA . The
understanding is that f (α) represents the probability that
the event in question will occur when the system’s state is
α. As indicated above, we wish to restrict our attention
here to cases in which the space A is finite-dimensional.
Thus we may identify A with A∗∗ , so that, for α ∈ A and
f ∈ A∗ , we may write f (α) as α(f ) whenever it suits us.
In the sequel, we shall continue always to denote states
by lower case Greek letters, and effects, by lower case
Roman letters.
It is helpful to note that the set ΩA of normalized states
actually determines both the ordered space A and the
order-unit uA : one can take A to be the dual of the
space of affine real-valued functionals on ΩA , ordered by
the cone of non-negative affine functionals; uA is simply
the constant affine functional on ΩA with value 1. When
describing a particular abstract state space, it is often
easiest simply to specify the convex set ΩA . When we
wish to begin with a convex set Ω and reconstruct A in
this way, we write A = A(Ω).
Note that the point-wise ordering of functionals in A∗
on ΩA is exactly the usual dual ordering. There is a
natural norm on A∗ , namely the supremum norm kf k =
supα∈ΩA |f (α)|; this gives rise in turn to a norm on A,
called the base norm, with respect to which kαk = uA (α)
for α ∈ A+ . In particular, every normalized state has
norm 1, and conversely, a positive element of A having
norm 1 is a normalized state (so that the two meanings
of “normalized” coincide). In the sequel, we shall write
α
e for the normalized version of a positive weight α ∈ A+ ,
i.e.,
α
e :=

α
α
=
kαk
uA (α)

It will be convenient to stipulate that e
0 = 0.

Observables Let (X, B) be a measurable space: an Xvalued observable on a state space A is a weakly countably additive vector measure F : B → A∗ with F (X) = u.
This guarantees that if α ∈ Ω, B 7→ F (B)(α) is a (finitely
additive) probability measure on B. If µ is a given measure on (X, B), we shall call f : X → A∗ a density for
F with respect to µ iff, for every α ∈ Ω and every set
B ∈ B,
Z
f (x)(α)dµ(x) = F (B)(α).
B

In the simplest case, where X is a finite set and
µ is the counting measure, an X-valued P
observable
amounts to a list (f1 , ..., fn ) of effects with i fi = u.
In the sequel, when we speak of an observable, without
specifying the value space, this is what we have in mind.
Processes and Dynamics We represent physical processes
involving an initial system with state space A and a final
system with state space B by positive linear mappings
φ : A → B having the property that kφ(α)k ≤ 1 for all
α ∈ ΩA , which is just to say that φ is norm contractive,
or, equivalently, that kφk ≤ 1. In this case, we understand that kφ(α)k = u(φ(α)) represents the probability
that the process occurs when the input is α; indeed, we
can regard the effect u ◦ φ ∈ A∗ as recording precisely
this occurrence. Thus, a family {φi |i ∈ I}
Pof positive
linear mappings with kφi k ≤ 1 for all i and i kφi k = 1,
represents a family of physical processes one of which is
bound to occur. (Such a family is a (discrete) instrument
in the sense of [8, 11].)
In many cases, one wants to impose some further
constraint on the possible dynamics of a system represented by an abstract state space A. By a dynamical
semigroup for A, we mean a closed, convex set DA of
norm-contractive positive linear mappings τ : A → A,
closed under composition and containing the identity
mapping IdA . We understand DA as representing the set
of all physically possible processes on A. (Here, “physically” refers to the use of this framework for abstractly
formulating possible physical theories; the framework
could also have other applications, so the terminology
“operationally possible” might be more accurate. With
this caveat, however, we will stick with “physically.”)
A state space equipped with a distinguished dynamical
semigroup, we call a dynamical model. Note that any
abstract state space can be regarded as a dynamical
model if we take DA to be (by default) the set of all
norm-contractive positive linear mappings A → A.
In the balance of this paper, we take it as a standing
assumption, relaxed only where explicitly noted, that this
is the case.
Self-Duality and Weak Self-Duality In both classical and
quantum settings, A carries a natural inner product with
respect to which there is a canonical order-isomorphism

<!-- page 3 -->
3
A ≃ A∗ . Indeed, in both classical and quantum cases,
the positive cone is self dual, in that
A+ = A+ := {α ∈ V |∀β ∈ V+ hα, βi ≥ 0}.
This property is a very special one, not shared by most
abstract state spaces. For an example, let A be threedimensional, with ΩA a square. For each side of the
square, there is an effect taking the value 1 along that
side, with the effects corresponding to opposite sides summing to 1. The dual cone thus also has a square crosssection, so that the cones A+ and A∗+ are isomorphic.
Nevertheless, A+ is not self-dual, as A+ is the image of
A+ under a rotation by π/4.
In this paper, we shall call a finite-dimensional ordered
space weakly self-dual iff, as in the example above, there
exists an order isomorphism (that is, a bijective, positive
linear mapping with positive inverse) φ : V ≃ V ∗ . This is
a far less stringent condition than self-duality. A classical
result of Vinberg [23] and Koecher [15] shows that any
finite-dimensional self-dual cone that is homogeneous, in
the sense that any interior point can be mapped to any
other by an affine symmetry (automorphism) of the cone,
and irreducible in the sense that the cone is not a direct
sum of simpler cones, is either the cone of positive selfadjoint elements of some full matrix ∗-algebra over the
reals, complexes or quaternions, or is the cone generated
by a ball-shaped base, or is the set of positive self-adjoint
3 × 3 matrices over the octonions.
Thus, self-duality, plus irreducibility and homogeneity, brings us within hailing distance of Hilbert space
quantum mechanics. One might hope to motivate these
conditions in operational terms. In this paper, we make
some progress in this direction by identifying weak
self-duality of a system as a necessary condition for
a composite of three copies of the system to support
conclusive (probabilistic) teleportation, and a condition
not much stronger than homogeneity on the space
of normalized states of the system to be teleported,
as sufficient for the existence of a tripartite model
permitting deterministic teleportation.
2. Composite Systems In order to discuss teleportation protocols, it is important to consider composite
systems having, at a minimum, three components: one
corresponding to the sender (“Alice”), another to the receiver (“Bob”), and a third, accessible to the sender but
entangled with the receiver, to serve as a channel across
which the sender’s state can be teleported. In this section, we review the account of bipartite state spaces given
in [4], and extend it to cover systems having three or more
components. In doing so, we identify a non-trivial condition on such composites, which we term regularity, that
will play an important role in our discussion of teleportation protocols in the sequel.
In order to maintain the flow of discussion, the proofs
of several results from this section have been placed in a

brief appendix.
Bipartite Systems It will be convenient, in what follows,
to identify the algebraic tensor product, A ⊗ B, of two
vector spaces A and B with the space of all bilinear forms
on A∗ ×B ∗ . In particular, if α ∈ A and β ∈ B, we identify
the pure tensor α ⊗ β with the bilinear form defined by
(α ⊗ β)(a, b) = a(α)b(β)
for all a ∈ A∗ and b ∈ B ∗ . If A and B are ordered vector
spaces, we call a form ω ∈ A ⊗ B positive iff ω(a, b) ≥ 0
for all positive functionals a ∈ A∗ and b ∈ B ∗ . Note that
if α ∈ A and β ∈ B are positive, then α ⊗ β is a positive
form. Note, too, that the set of positive forms is a cone
in A ⊗ B.
Definition 1 The maximal tensor product of ordered
vector spaces A and B, denoted A ⊗max B, is A ⊗ B,
equipped with the cone of all positive forms. Their minimal tensor product, denoted A⊗min B, is A⊗ B equipped
with the cone of all positive linear combinations of pure
tensors.
The maximal and minimal tensor products are exactly
the injective and projective tensor products discussed by
Wittstock in [22]; see also [10, 18]. It is not difficult
to show that, in our present finite-dimensional setting,
(A ⊗max B)∗ = A∗ ⊗min B ∗ and (A ⊗min B)∗ = A∗ ⊗max
B∗.
If (A, uA ) and (B, uB ) are abstract state spaces representing two physical systems, then subject to a plausible no-signaling condition and a “local observability”
assumption guaranteeing that the correlations between
local observables determine the gloabl state (see [4]),
the largest sensible model for a bipartite system having
physically separated components modeled by A and B
is A ⊗max B, with order unit given by uAB = uA ⊗ uB .
Accordingly, we model a composite system with components (A, uA ) and (B, uB ) by the algebraic tensor product of A and B, ordered by any cone lying between the
maximal and minimal tensor cones, and with order unit
uAB = uA ⊗ uB . We shall write AB, generically, for
such a state space, denoting the convex set u−1
AB (1) of
normalized states by ΩAB .
It will be important, below, to remember that all
states, in whatever cone we use, can be represented as
linear combinations of pure product states, as these span
A ⊗ B. Unless the sets of normalized states for A or
B are simplices—that is, unless one system at least is
classical—the minimal and maximal tensor products are
quite different, with the latter containing many more normalized states than the former. These additional states
we term entangled; states in A⊗min B, we term separable.
Marginal and Conditional States Every state ω in a bipartite system AB has natural marginal states ω A ∈ A

<!-- page 4 -->
4
and ω B ∈ B, given respectively by
ω A (a) = ω(a ⊗ uB ) and ω B (b) = ω(uA ⊗ b)
for all a ∈ A∗ and b ∈ B ∗ . We also have un-normalized
conditional states, given by
ωaB (b) = ω(a, b) = ωbA (a)
and their normalized versions,
ω
eaB (b) =

ω(a, b)
ω(a, b)
and ωbA (a) = B
A
ω (a)
ω (b)

if the marginal states are non-zero, and set equal
to 0 otherwise, so that the expected identities
ω(a, b) = ωbA (a)ω B (b) = ω A (a)ωaB (b) hold. Using
these, it is not difficult to show that, just as in quantum
theory, the marginals of an entangled state are necessarily mixed, while those of an unentangled pure state are
necessarily pure.
Dynamically Admissible Composites It is reasonable to
suppose that, if τA ∈ DA and τB ∈ DB are physically
admissible processes on A and B, respectively, then, for
any state ω on a composite system AB,
(τA ⊗ τB )(ω) : a, b 7→ ω(τA∗ a, τB∗ b)
is a state of AB. When this is the case, let us say
that the composite system AB is dynamically admissible. Equivalently, AB is dynamically admissible iff for
all τA ∈ DA , τB ∈ DB , AB+ is stable under τA ⊗ τB
acting on A ⊗ B. Note that both minimal and maximal tensor products are stable under any pure tensor of
positive operators, so these are dynamically admissible
regardless of the dynamics.
Where DA and DB – as per our standing assumption –
comprise all norm-contractive positive mappings A → A
and B → B, respectively, AB is dynamically admissible
iff its positive cone AB+ is stable under τ1 ⊗ τ2 for
all positive mappings τ1 : A → A and τ2 : B → B.
Although the minimal and maximal tensor products
A ⊗min B and A ⊗max B both enjoy this property,
it is highly non-trivial. Indeed, if A = Bh (H) and
B = Bh (K), the spaces of self-adjoint operators on
Hilbert spaces H and K, and AB = Bh (H ⊗ K), the
usual quantum-mechanical composite state space, then
the cone AB+ is stable only under products of completely
positive mappings. However, this difficulty is easily
met: one need only define a composite of two dynamical
models (A, DA ) and (B, DB ) to be a model (AB, DAB )
where AB is a dynamically admissible composite of A
and B, and DAB is a semigroup of norm-contractive
positive mappings AB → AB containing all products
τA ⊗ τB where τA ∈ DB and τB ∈ DB . In the balance of
this paper, results will be formulated for composites of
state spaces, rather than of dynamical models; however,

these can easily be modified to accommodate the latter.
Bipartite states and effects as operators Elements of the
tensor product A ⊗ B and of its dual (A ⊗ B)∗ can be
regarded as operators A∗ → B and A → B ∗ , respectively.
Indeed, every f ∈ (A ⊗ B)∗ induces a linear mapping
fb : A → B ∗ , uniquely defined by the condition that
fb(α)(β) = f (α ⊗ β).

The mapping f 7→ fb is a linear isomorphism. Note also
that, if f is positive, then so is fb (though not conversely,
unless we use the maximal tensor product). Similarly,
any ω ∈ A ⊗ B induces a linear mapping ω
b : A∗ → B,
uniquely defined by the condition that
ω
b (f )(g) = (f ⊗ g)(ω)

for all f, g ∈ V ∗ . Again, the mapping ω 7→ ω
b is a linear
isomorphism. Also, since elements of the maximal tensor product A ⊗max B are precisely those corresponding
to positive bilinear forms, ω
b will be a positive operator,
regardless of which tensor product we use. In the special
case in which ω is a pure tensor, say ω = β ⊗ γ, we have
\
(β
⊗ γ)(f ) = f (β)γ.
d for the set of operaIn the sequel, we shall write AB
tors ω
b corresponding to ω ∈ AB, ordered by the cone of
\
operators ω
b with ω ∈ AB+ . For example, A ⊗
max B is
simply the space L(A, B), ordered by the cone of positive
operators.
Note that the operator ω
b corresponding to a normalized state in AB has the property that ω
b (u)(u) = 1, i.e.,
ω
b (u) is a state. Conversely, given a positive linear mapping φ : A∗ → B with the property that φ(uA ) is a state,
the bilinear form ω(a, b) := φ(a)(b) defines an element
of the maximal tensor product, with φ = ω
b . It is useful to note ([10], Equation 16) that any positive operator
φ : A∗ → B has operator norm (induced by the abovedefined order-unit and base norms on A∗ and B) given
by
kφk = kφ(u)kB
where k · kB denotes the base-norm on B; hence, bipartite states correspond exactly to positive operators of
norm 1.
Similarly, if f is a bipartite effect in A∗ ⊗max A∗ ,
then the mapping fb : A → A∗ takes any state α to the
effect fb(α)(β) = f (α ⊗ β). Evidently, this is no greater
than unity on Ω, so we have fb(α) ≤ u for all α ∈ Ω;
conversely, any such positive mapping defines a bipartite
effect.
Multi-partite Systems Up to a point, the foregoing considerations readily extend to composite systems involving more than two components. Suppose

<!-- page 5 -->
5
(A1 , u1 ), ..., (An , un ) are abstract state spaces. As above,
call an n-linear form on A∗1 × · · · × A∗n positive iff it takes
non-negative values on all n-tuples f = (f1 , ..., fn ) of
positive functionals fi ∈ A∗i . Given states αi ∈ Ai+ for
i = 1, ..., n, the product state α1 ⊗ · · · ⊗ αn , defined by
(⊗i αi )(f ) = Πi αi (fi ), is obviously positive in this sense.
Definition 2 A composite of state spaces (Ai , ui ), i =
1, ..., n, is any space A of n-linear forms on A∗1 · · · A∗n , ordered by any cone of positive forms containing all product
states, and with with order-unit given by u = u1 ⊗· · ·⊗un .
This is equivalent to saying that A contains all product
states, and A∗ contains all product effects. Examples
of composites of, say, three spaces A, B and C would
include A ⊗max B ⊗max C, A ⊗min B ⊗min C, and mixed
composites such as A ⊗min (B ⊗max C). Extending the
terminology of the previous section, we shall call a composite A of state spaces (Ai , ui ) dynamicallyNadmissible
iff A+ is stable under mappings of the form i τi where
τi : Ai → Ai are arbitrary positive mappings. A product
of dynamical models (Ai , Di ) is a dynamical model
(A, D) where A is a dynamically admissible model of
A1 , ..., An and D is a dynamical semigroup that includes
all products of mappings τi ∈ Di .
Regular composites Suppose now that A is a composite
of A1 , ..., An , and that J ⊆ {1, ...., n}. Given a list of
positive linear functionals f = (fi ) ∈ Πi∈I\J A∗i and a
state ω ∈ A+ , we may define a |J|-linear form ωfJ on
Πj∈J A∗j by setting
ωfJ (g) = ω(f ⊗ g),

We regard regularity as an eminently reasonable restriction on a model of a composite physical system, at
least in cases in which the components retain their separate identities (so that the systems are “separated”). As
we shall see in the sequel, regularity is sufficient to ground
a weak analogue of a teleportation protocol, which we
call remote evaluation. In the balance of this section, we
collect some examples of regular composites, and adduce
some technical results concerning the notion of regularity.
As a matter of notational convenience, we’ll write
ABC for a composite of three systems A, B and C, denoting by AB, BC, and AC the three bipartite subsystems.
In this case, the condition that ABC be regular amounts
to requiring that
AB ⊗min C ≤ ABC ≤ AB ⊗max C
and similarly A and BC and for AC and B. Equivalently,
we require that
AB ⊗min C ≤ ABC and (AB)∗ ⊗min C ∗ ≤ (ABC)∗ .
As an example, let us show that the mixed tensor product
A ⊗min (B ⊗max C)
is a regular composite of A, B and C. The only interesting coarse-grainings here are {{A, B}, {C}} and
{{A,P
C}, {B}}. To analyze the first of these, suppose that
ω = i ti αi ⊗ µi where αi ∈ A+ and µi ∈ (B ⊗max C)+ .
Then for all c ∈ C ∗ ,
X
ti αi ⊗ µ
bi (c),
ωcAB =
i

where (f ⊗ g)i is gi if i ∈ J and fi otherwise. We
refer to ωfJ as a partially evaluated state. The set of
J
such
N partially-evaluated states ωf generates a cone in
j∈J Aj ; together with the order unit ⊗j∈J uj , this defines an abstract state space AJ , which we call the Jpartial sub-system, and which we take to represent the
subsystem corresponding to the set of elementary systems Aj with j ∈ J.
In the simplest cases, we should expect that that a
composite of “elementary” systems A1 , ..., An can equally
be regarded as a composite of complex sub-systems AJ
obtained through an arbitrary coarse-graining of the index set I = {1, ..., n}. This suggests the following
Definition 3 A composite A of state spaces A1 , ..., An is
regular iff, for all partitions {J1 , ..., Jk } of {1, ..., n}, A
is a composite, in the sense of Definition 1, of the partial
systems AJ1 , ..., AJk .
Equivalently, A is a regular composite of A1 , ..., An
iff for all partitions J1 , .., Jk of {1, .., n}, and N
for all sequences of states µk ∈ AJk , the product state k µk belongs to A, and forNall sequences of effects fk ∈ (AJk )∗ ,
the product effect k fk belongs to A∗ .

a positive linear combination of positive elements of A
and B; hence, ωcAB ∈ (A ⊗min B)+ , so AB = A ⊗min B.
It follows that, if γ ∈ C+ , we have
ωcAB ⊗ γ ∈ (A ⊗min B ⊗min C)+
≤ ((A ⊗min B) ⊗max C)+ = (AB ⊗max C)+ .
A similar argument applies to the bipartition
{{A, C}, B}.
In the next section (see Corollary 1), we’ll show that
A ⊗max (B ⊗min C) is also regular. An example of a
non-regular composite is
(A ⊗min A) ⊗max (A ⊗min A)
where A is weakly self-dual. This follows from considerations involving entanglement swapping, as discussed in
section 6; we postpone further discussion of this example
until then.
The following lemma collects a number of facts about
composites and regular composites that will be used
freely—and often tacitly— in the sequel. (For a proof,
see the appendix.)

<!-- page 6 -->
6
Lemma 1 Let A be a composite of systems A1 , ..., An .
Then
(a) If K ⊆ J ⊆ {1, ..., n}, then (AJ )K = AK .
(b) If A is regular, then (AJ )+ = {ωuJ |ω ∈ A+ }.
(c) If A is regular, so is AJ for every J ⊆ {1, ..., n}.
Probabilistic Theories Roughly, by a probabilistic theory,
we mean a class C of probabilistic models—that is, abstract state-spaces—closed under some construction or
constructions whereby systems can be composed. Examples would include the class of all classical systems
(i.e., systems with simplicial state spaces), the class of
all quantum systems with the usual quantum-mechanical
state space, the class obtained by forming the maximal
tensor products of quantum systems, the convexified version of Spekkens’ “toy theory” [21], etc. In principle, this
idea might be given a precise category-theoretic formulation (something we expect to pursue in a subsequent
paper); here, we content ourselves with a more informal
treatment.
Consider a class C of state spaces equipped with a specific coupling A, B 7→ A ⊛ B, where A ⊛ B is a composite of A and B. We shall call ⊛ associative if for all
A, B, C ∈ C, A ⊛ (B ⊛ C) ≃ (A ⊛ B) ⊛ C) under the obvious association mapping (defined on product states by
α⊗(β⊗γ) 7→ (α⊗β)⊗γ. The straightforward but tedious
proof of the following can be found in the appendix:
Proposition 1 If ⊛ is associative, then for all
A1 , ..., An ∈ C, A1 ⊛ · · · ⊛ An is a regular composite of
A1 , ..., An .
It follows that composites constructed using only
the maximal, or only the minimal, tensor product are
regular, as are composite quantum systems. For later
purposes, if C is a class of abstract state spaces closed
under an associative coupling ⊛ preserving isomorphism,
we shall call the pair (C, ⊛) a monoidal theory. (By
preserving isomorphism, we mean that if A ≃ B and
C ≃ D, then (A ⊛ C) ≃ (B ⊛ D).) It is by no means
obvious that every sensible theory must be monoidal,
however – for instance, we may wish to consider theories in which one can form tripartite systems of the
form A ⊗min (B ⊗max C), in which there is maximal
entanglement between B and C, but no entanglement
at all between A and either B or C. There is certainly
precedent for such mixed tensorial constructions, e.g.,
in Hardy’s causaloid framework for quantum gravity
[12].
On the other hand, considerations involving
entanglement swapping, as spelled out in section 5, place
some nontrivial restrictions on non-monoidal theories.
Remark: In the interest of clarity, it will sometimes
be helpful in the sequel to adorn an element of a factor
in a tensor product with a superscript indicating to

which factor it belongs, writing, for instance, α ⊗ β or
αA ⊗ β B for product states in A ⊗ B, or f AB for an
arbitrary bipartite effect in (A ⊗ B)∗ . On occasion,
both ornamented and unornamented forms—e.g., ω and
ω AB —may occur in the same calculation; when they do,
they refer to the same object.
3. Conclusive Teleportation Suppose ABC is a composite of state spaces A, B and C. If f is an effect on
AB and ω is a state in BC, then we have positive linear
mappings fb : A → B ∗ and ω
b : B ∗ → C. Their comb
posite, ω
b ◦ f , is a positive operator A → C. If ABC is
a regular composite, we also have, for any state α ∈ A
and any effect c ∈ C ∗ , that α ⊗ ω is a state in ABC and
f ⊗ c is an effect in (ABC)∗ . We now make a technically
trivial but crucial observation:
Lemma 2 With notation as above, the un-normalized
conditional state of α ⊗ ω given an effect f ∈ AB is
(αA ⊗ ω BC )C
b (fb(α)).
f = ω

Proof: As pure tensors generate BC, it is sufficient to
check this in the case that ω = β ⊗ γ. Then, for any
b ∈ B∗, ω
b (b) = β(b)γ (using, here, our convention of
identifying a state space with its double dual). Note
also that f (α ⊗ β) = β(fb(α)). Hence, for any c ∈ C ∗ ,
(f ⊗ c)(α ⊗ ω) = f (α ⊗ β)γ(c) = β(fb(α))γ(c) =
ω
b (fb(α))(c). 
Corollary 1 For any state spaces A, B and C,
(i) There is a canonical embedding
A ⊗min (B ⊗max C) ≤ (A ⊗min B) ⊗max C.
(ii) The composite (A ⊗min B) ⊗max C is regular.
Proof: By Lemma 2, any product state α ⊗ ω with
α ∈ A+ and ω ∈ (B ⊗max C)+ yields a positive bilinear form on (A ⊗min B)∗ × C ∗ , namely, (α ⊗ β)(f, c) =
c(b
ω (fb(α))). Hence, we have a natural positive linear
mapping A ⊗min (B ⊗max C) → ((A ⊗min B)∗ ⊗min C ∗ )∗ ;
the last is isomorphic to (A ⊗min B) ⊗max C. This establishes (i).
To show that (A ⊗min B) ⊗max C is regular, we first
observe that BC = B ⊗max C. Indeed, let µ ∈ B ⊗max C,
and let µ
b be the associated positive operator B ∗ → C.
Let α be some fixed state in A. Given f ∈ (A⊗min B)∗ ≃
L+ (A, B ∗ ) and c ∈ C ∗ , set
ω(f, c) = µ
b(fb(α))(c) :

this is bilinear in f and in c, and positive where both
f and c are positive, and so, defines an element ω ∈
(A ⊗min B) ⊗max C. We now observe that the reduced

<!-- page 7 -->
7
, evaluated on a pair of effects (b, c) ∈ B ∗ × C ∗ ,
state ωuBC
A
yields
(b, c) = ω(uA , b, c)
ωuBC
A
= µ
b((u\
A ⊗ b)(α))(c)
= µ
b(b)(c) = µ(b, c).

= µ. This shows that B ⊗max C ≤ BC;
Thus, ωuBC
A
the reverse inclusion is trivial, so BC ≃ B ⊗max C, as
claimed. We now have, by part (i), that
A ⊗min (BC) = A ⊗min (B ⊗max C)
≤ (A ⊗min B) ⊗max C = ABC.
Obviously, we have ABC ≤ A ⊗max (B ⊗max C) =
A ⊗max BC. The corresponding result for the coarsegraining {{AC}, {B}} follows similarly (or by symmetry), and that for {{A}, {B, C}} is trivial, so so ABC is
regular. 
We can interpret Lemma 2 in information-processing
terms as follows. Suppose two parties, Alice and Bob,
have access to systems A and B, respectively. Suppose,
moreover, that Alice’s system consists of two subsystems,
A1 and A2 , with A1 in an unknown state α. If the total
Alice-Bob system is represented by a regular composite
AB = A1 A2 B, then if f is an effect on A and ω is a known
state on A2 B, we may prepare A1 A2 B in the joint state
α ⊗ ω: if Alice performs a measurement on A = A1 A2
having f as a possible outcome, then, conditional upon
securing this outcome, the conditional state of B is, up
to normalization, ω
b (fb(α)). Thus, we may say that Alice
has evaluated a known mapping, namely ω
b ◦ fb, on an
unknown input α, simply by securing f as a measurement outcome. In the sequel, we refer to this protocol as
remote evaluation.
This is obviously reminiscent of a teleportation protocol. Indeed, conclusive teleportation can be regarded as
the special case of remote evaluation in which the mapping ω
b ◦ fb is invertible. Suppose that η : A1 ≃ B is a
fixed isomorphism between Alice’s system A1 and Bob’s
system B (allowing us to say what we mean by saying a
state of B is the same as a state of A1 ). Suppose, further,
that the unknown state α is recoverable from the normalB
^
ized conditional state (α
⊗ ω)f by means of a physically
admissible process τ , depending on f but not on α: upon
securing a measurement outcome corresponding to f , Alice can then instruct Bob to make the correction τ ; once
this is done, she is certain that the conditional state of
Bob’s system B — whatever it is — is identical (up to
η) to the original, but unknown, state α.
In fact, we can distinguish two situations: one in which
the correction operation τ is certain to succeed, and another in which it may fail, but in which this failure will
be apparent to Bob. In the latter case, the teleportation
protocol has an additional step: Alice must wait for Bob

to report the success of the correction. We shall refer
to these as strong and weak conclusive teleportation, respectively. Notice that the standard (one-outcome postselected) quantum teleportation protocol is an instance
of a strong teleportation protocol.
We make this language precise as follows. To avoid
needess repetition, here and in the balance of this paper A1 A2 B denotes a regular composite of state spaces
A1 , A2 and B with A1 isomorphic to B by a fixed isomorphism η : A1 ≃ B; and f is an effect on A1 A2 and ω
is a state in A2 B.
Definition 4 We say that the pair (f, ω) is a conclusive
teleportation protocol on A1 A2 B iff there exists a normcontractive linear mapping τ : B → B, called a correction, such that, for every normalized state α ∈ ΩA1 ,
B

^
τ ((α
⊗ ω)f ) = tα η(α)
for some constant tα > 0. If τ can be so chosen that
tα = 1 for all α, we say that the protocol (f, ω) is strong.
B

^
By Lemma 2, the conditional state (α ⊗
ω)f can be
b
b
expressed as ω
b (f (α))/u(b
ω (f (α))). Let
µ := ω
b ◦ fb : A1 → B,

noting that this is a norm-contractive positive mapping.
Then (f, ω) is a teleportation protocol iff there exists a
norm-contractive positive mapping τ : B → B with
τ (µ(α)) = tα kµ(α)kη(α)
]
for all α ∈ ΩA . Notice that tα = u(τ (µ(α))),
i.e., tα
is the probability that the correction τ succeeds in the
conditional state ]
µ(α)). Accordingly, a strong protocol
is one for which there exists a correction that is certain
to succeed.
Theorem 1, below, gives a complete characterization of
conclusive teleportation protocols, strong or otherwise,
in terms of the mapping µ = ω
b ◦ fb. We require an easy
preliminary
Lemma 3 Let A and B be any abstract state spaces. Let
φ, ψ : A → B be any two linear mappings with ψ injective. If, for every α ∈ ΩA , there is a constant k(α) such
that φ(α) = k(α)ψ(α), then in fact k(α) ≡ k, a constant
not depending on α.
Proof: Let α and β be distinct, and hence, linearly independent, elements of ΩA , and consider γ = (α + β)/2.
Then we have
φ(γ) = k(γ)ψ(γ) = (k(γ)/2)(φ(α) + φ(β))
and also
φ(γ) = (φ(α) + φ(β))/2 = (k(α)ψ(α) + k(β)ψ(β))/2.

<!-- page 8 -->
8
Thus,
(k(α) − k(γ))ψ(α) + (k(β) − k(γ))ψ(β) = 0.
Since ψ is injective, ψ(α) and ψ(β) are linearly independent in B; hence, k(α) − k(γ) = k(β) − k(γ) = 0, whence
k(α) = k(β). 
Recall that an order-isomorphism between abstract
state spaces is a positive linear bijection with a positive
inverse, while an isomorphism also preserves normalization.
Theorem 1 Let µ := ω
b ◦ fb : A1 → B. Then

(a) (f, ω) is a conclusive teleportation protocol iff µ is
an order isomorphism; in this case τ = s(η ◦ µ−1 )
where s ≤ 1/kµ−1k ≤ 1.
(b) (f, ω) is a strong teleportation protocol iff µ is proportional to an isomorphism; in this case, the correction τ is a symmetry of B.

Proof:
(a) Suppose first that (f, ω) is a teleportation protocol.
Then there exists a positive, norm-contractive mapping
τ : B → B such that, for all α ∈ ΩA1 , there
τ (µ(α)) = tα kµ(α)kη(α)
for some constant tα > 0. As η is injective, Lemma 4
implies that
tα kµ(α)k ≡ s,
a constant independent of α. Note that, as τ is normcontractive, s < 1. Since ΩA1 spans A1 , we have τ ◦ µ =
sη. It follows that τ : B → B is a surjective linear
mapping. As we are working in finite dimensions, this
implies that τ is invertible; we have
1
τ −1 = µ ◦ η −1 ,
s
which is positive. Thus, τ is an order-isomorphism. It
follows µ = τ −1 ◦ sη is also an order-isomorphism.
For the converse, suppose that µ is an orderisomorphism. Then η ◦ µ−1 is also an order-isomorphism.
Let
τ := s(η ◦ µ−1 )
where s < 1/kµ−1 k. As kηk = 1, we have kτ k ≤
skηkkµ−1 k < 1, so τ is norm-contractive. Now τ ◦µ = sη.
For all α, let tα = s/kµ(α)k (noting that kµ(α)k > 0,
since µ is injective), so that
τ (µ(α)) = sη(α) = tα kµ(α)kη(α).
(b) Suppose first that µ = kφ for some isomorphism
φ : A1 → B. Then φ : A1 → B and some positive

constant k. Let τ = η ◦ φ−1 : then τ (µ(α)) = kη(α)
for all α. Since k = kµ(α)k for all α, we have a strong
teleportation protocol.
For the converse, suppose (f, ω) is a strong teleportation protocol. Thus, there exists a norm-contractive
positive mapping τ : B → B such that, for all α ∈ ΩA1 ,
τ (µ(α)) = kµ(α)kη(α).
We claim that τ is a symmetry. To see this, let Γ =
e = {e
γ |γ ∈ Γ};
µ(ΩA ) := {µ(α)|α ∈ ΩA1 }, and set Γ
note that this set is a convex subset of ΩB .[24] Now,
τ (µ̃(α)) = η(α) ∈ ΩB , so τ effects an affine bijection of
Γ onto ΩB . It follows that the affine span of Γ equals
that of Ω, whence, that τ preserves the affine span of the
latter – which is exactly the hyperplane u−1
B (1). As τ is
positive, it also preserves the positive cone B+ , whence,
τ preserves B+ ∩ u−1 (1) = ΩB . Thus, τ is a symmetry,
as claimed. It remains to show that µ is proportional to
an isomorphism. But as we have
τ (µ(α)) = kµ(α)kη(α),
we also have
µ(α) = kµ(α)kτ −1 (η(α))
for all α ∈ ΩA1 . Invoking Lemma 4, we see that
kµ(α)k ≡ k, a constant independent of α – whence,
µ = kτ −1 ◦ η. 
Remarks: (1) For Bob to be able to apply the correction mapping τ , the latter must belong to the dynamical
semigroup DB . Given our simplifying assumption is that
DB comprises all norm-contractive positive mappings on
B, this is automatic, but in a treatment using more general dynamical models, it would need to be assumed as
part of the definition of a teleportation protocol.
(2) If (f, ω) is a teleportation protocol on A1 A2 B,
then we can regard it also as a teleportation protocol on
A1 ⊗min (A2 ⊗max B), as the latter is regular, f is an effect on A1 ⊗min A2 , and ω is a state in A2 ⊗max B. Thus,
all teleportation protocols involving regular composites
of A1 , A2 and B live, so to speak, in A2 ⊗min (A2 ⊗max B).
One can regard non-strong conclusive teleportation
protocols as inherently inefficient. The question arises,
whether an inefficient protocol can always be replaced
with one that is perfectly efficient. We show that this is
always possible when the composite is dynamically admissible. (Recall under our standing assumption, a composite is dynamically admissible iff its positive cone is
closed under products of positive mappings on the factors.)
Corollary 2 Suppose A1 A2 B is dynamically admissible.
If (f, ω) is a conclusive teleportation protocol with correction τ , then let ω ′ ∈ A2 B be the state defined, for all

<!-- page 9 -->
9
a ∈ A∗2 and b ∈ B ∗ , by
^
ω ′ (a, b) = ω(a,
τ (b)).
Then (f, ω ′ ) is a strong conclusive teleportation protocol,
requiring no correction.
Proof: Since (f, ω) is a conclusive teleportation protocol,
there exists a positive mapping τ : B → B such that
τ ◦ω
b ◦ fb = sη

for some constant s. Since A1 A2 B is dynamically admissible, ω ′ ∈ A2 B. It is easily verified that ω
b′ =
(τ ◦ ω)/kτ ◦ ωk; hence,
ω
b ′ ◦ fb =

s
η.
kτ ◦ ωk

Thus, µ
b′ := ω
b ′ ◦ fb is proportional to a symmetry, so
(f, ω
b ) is a strong conclusive teleportation protocol, by
Theorem 1. Moreover, as the symmetry in question is η
itself, no correction is required. 
It follows from Theorem 1 that if a bipartite state ω on
A2 B and a bipartite state f on A1 A2 supply a conclusive
teleportation protocol, then the positive linear mappings
fb and ω
b are respectively injective and surjective. We can
be somewhat more precise about the geometry of the situation. Let us say that a compression on an ordered space
V is a positive mapping P : V → V such that P 2 = P .
Equivalently, P ’s range, P (V ), is an ordered subspace of
V , and P (α) = α for all α ∈ P (V ). As an example,
let K be a cube, and let F be a face thereof; the obvious affine surjection K → F extends to a compression
V (K) → V (F ).
Suppose now that (f, ω) is a conclusive teleportation
protocol on A1 A2 B with an order-isomorphic correction
τ : B → B, so that
τ ◦ω
b ◦ fb = sη

for some constant s > 0. Then fb : A1 → A∗2 is an orderembedding, and and ω
b : A∗2 → B is a positive surjection.
Let
P := fb ◦ η −1 ◦ τ ◦ ω
b : A∗2 → A∗2 :

an easy computation shows that P is a compression in
the above-defined sense, with range equal to the image
of fb.
Conversely, suppose we are given an effect f such that
fb : A1 → A∗2 taking A1 order-isomorphically onto the
range of a compression P : A∗2 → A∗2 . Let fb+ : Ran(P ) →
A1 be the inverse of fb’s co-restriction to Ran(P ), and let
αo = fb+ (uA2 ), i.e, the unique element of A1+ such that
fb(αo ) = P (uA2 ). Define
ωb′ :=

1
η ◦ fb+ ◦ P.
kαo k

Then ωb′ (uA2 ) = η(α)/kαo k ∈ ΩB (since η is an isomorphism, hence norm-preserving), whence, ωb′ corresponds to a normalized state ω ′ in A2 ⊗max B. The
pair (f, ω ′ ) gives us a strong—and correction-free—
teleportation protocol on A1 ⊗min (A2 ⊗max B). If A1 A2 B
is dynamically admissible, then ω ′ ∈ A2 B, and indeed, is
precisely the state ω ′ defined in Corollary 2.
Summarizing:
Theorem 2 Let A1 , A2 and B ≃ A1 be abstract state
spaces with B ≃ A1 . A regular composite A1 A2 B supports a conclusive teleportation protocol iff there exists an
effect f on A1 A2 , a state ω in A2 B, and a compression
P : A∗2 → A∗2 such that fb, co-restricted to Ran(P ), is
an order-isomorphism A1 ≃ Ran(P ) and ω
b , restricted to
Ran(P ), is an order-isomorphism Ran(P ) ≃ B.
Corollary 3 A1 ⊗min (A2 ⊗max A1 ) supports conclusive
teleportation with η(α) = α for all α iff A1 ≤ A∗2 is the
range of a compression P : A∗2 → A∗2 .
Proof: Suppose first that we have a compression P :
A∗2 → A∗1 : regarding P as a positive surjection π :
A∗2 → A1 , and letting ι : A1 → A∗2 be the posi\
tive inclusion mapping, we have π ∈ (A2 ⊗
max A1 ) and
\
∗ . As (π ◦ι)(α) = α for all α ∈ A , Theι ∈ (A1 ⊗
A
)
min 2
1
orem 1 tells us that A1 A2 A1 = A1 ⊗min (A2 ⊗max A1 )
supports conclusive teleportation.
Conversely, if A1 ⊗min (A2 ⊗max A1 ) supports conclusive teleportation, then by Corollary 2, there exist
positive operators ω
b : A∗2 → A1 and fb : A1 → A∗2
b
with ω
b ◦ f : A1 → A1 an isomorphism, in which case
P := fb ◦ ω
b is a compression. 
We also have

Corollary 4 Let A1 A2 B be a regular composite of three
pairwise isomorphic, weakly self-dual state spaces. If
A2 B contains a state ω with ω
b : A∗2 ≃ B, then A1 A2 B
supports conclusive teleportation. In particular, A1 ⊗min
(A2 ⊗max B) supports conclusive teleportation.
Remark: As observed above, the standing assumption
that for a system A, its dynamical semigroup DA is
the set of all positive maps on A, strongly restricts the
nature of dynamically admissible tensor products, and
is, for example, incompatible with the usual quantum
tensor product. However, our definitions and results
concerning teleportation are easily adapted to the setting
of regular composites of arbitrary dynamical models: as
noted above, the definition of a teleportation protocol
in that setting requires that the correction mapping
τ B on B belong to the dynamical semigroup DB ; with
this modification, one has one has obvious analogues of
Theorems 1 and 2, and of Corollary 2.

<!-- page 10 -->
10
4. Deterministic Teleportation As in the previous
section, A1 A2 B is a regular composite of three state
spaces A1 , A2 and B, with B isomorphic to A1 . In order for A1 A2 B to support a deterministic teleportation
protocol, we require a bipartite state ω ∈ A2 B and an
observable {f1 , ..., fn } on A1 A2 such that for every state
α in A1 and for each i, the state α is recoverable from
the conditional state of α ⊗ ω given outcome (effect) fi .

cone obtained by rotating A+ by π/4. This gives us
an order-isomorphism A∗ → A that is equivariant with
respect to the the natural action of Z4 on Ω; as this last
is transitive on the vertices of the latter, Theorem 2 tells
us that A ⊗min (A ⊗max A) will support a deterministic
teleportation protocol. Similar considerations show that
the same conclusion holds whenever ΩA is any regular
polygon.

Definition 5 Let A1 A2 B be a regular composite of A1 ,
A2 and B with B ≃ A1 via a fixed isomorphism η :
A1 → B. If ω is a state in A2 B and E = (f1 , ..., fn )
is an observable on A = A1 A2 , we shall say that the pair
(E, ω) realizes a deterministic teleportation protocol iff,
for each effect fi ∈ E, the pair (fi , ω) realizes a strong
conclusive teleportation protocol.

For the proof of Theorem 3, we need an easy lemma.

The idea is that, upon measuring E and obtaining outcome fi , Alice instructs Bob to apply a suitable correction τi ; the conditional state of B is then η(α). Note that,
by Theorem 1, the correction τi must be a symmetry of
B.
At present, it is not clear to us exactly what conditions on the pair A1 , A2 will be necessary in order to
secure a deterministic teleportation protocol. However,
Theorem 2 below provides a wealth of examples of systems which, while weakly self-dual, are neither classical
nor quantum, but can nevertheless by combined so as to
support a deterministic teleportation protocol. In particular, self-duality is not necessary for deterministic teleportation.
In what follows, let A be an abstract state space carrying an action of a finite group G that preserves the state
space Ω. Note that there is a canonical dual action of G
on A∗ given by
(ga)(α) = a(g −1 α)
∗

for all g ∈ G, a ∈ A , and α ∈ A. Note, too, that
the order-unit u = uA is invariant under this action, i.e,.
gu = u for all g ∈ G. A state ω is called G-equivariant if
for all g ∈ G and all effects a ∈ A∗ we have
gb
ω(a) = ω
b (ga) .

Lemma 4 Let A and G be as in Theorem 3. Then there
exists a unique invariant normalized state ωo ∈ ΩA .
Proof: Notice, first, that there is certainly
at least one
P
gα
fixed state, namely (1/|G|)ωo =
o , where αo
g∈G
is any one extreme state. To see that there can be no
more than one such state, let Γ denote the set of G-fixed
points of Ω. Observe that Γ is an affine section of Ω;
hence, if Γ contains more than a single point, it contains
an affine line, which must intersect the topological
boundary of Ω. Let α be a fixed state belonging to this
boundary: equivalently, α is fixed, and belongs to a
proper face of Ω. Let F be the smallest face containing
α: for each g ∈ G, gF is again a face containing α, so
F ⊆ gF . In other words, F is invariant. But since F
is a proper face and G acts transitively on Ω’s extreme
points, this is impossible. 
Proof of Theorem 3: Let A, G and ωo be as above. By
assumption, there is an equivariant order-isomorphism
φ : A∗ → A; normalizing if necessary, we can assume
that φ = ω
b for some bipartite state on AB. We claim
that ω
b (u) = ωo . Indeed, for all g ∈ G, we have
gb
ω(u) = ω
b (gu) = ω
b (u).

Thus, ω
b (u) is G-invariant; but there is only one invariant
state, namely ωo .
Now, for all g ∈ G, let fg ∈ (A ⊗max A)∗ correspond
to the operator
1 −1
fbg =
ω
b ◦ g.
|G|

(1)

Theorem 3 Let A be weakly self-dual, and suppose G
is a finite group acting on A, in such a way that (i)
G acts transitively on the extreme points of Ω, and (ii)
there exists a G-equivariant isomorphism A∗ ≃ A. Then
A⊗min (A⊗max A) supports a deterministic teleportation
protocol.
For an example, consider the state space obtained
by taking Ω to be a unit square in R3 , displaced one
unit from the origin; A+ is the cone generated by this
square base. As observed earlier, with respect to the
usual inner product, A∗ can be represented as R3 with

We claim that E = {fg } is an observable, and (E, ωo )
realizes a strong deterministic teleportationPprotocol. To
1
see this, note that for every α ∈ A, |G|
g∈G gα is a
G-invariant state, and hence, by Lemma 3, equals ωo .
Thus,
X

g∈G

X 1
ω
b −1 (gα)
|G|
g∈G


X
1
= ω
b −1 
gα
|G|

fg (α) =

g∈G

= ω
b

−1

(ωo ) = u

<!-- page 11 -->
11
(appealing,
in the last step, to the fact that ω
b (u) = ωo ).
P
So g∈G fg = u, i.e., g 7→ fg is an observable. Moreover,
ω
b (fbg (α)) = ω
b (b
ω −1 (gα)) = gα.

Thus, ω
b ◦ fbg acts as the group element g ∈ G – and
hence, in particular, has a norm-preserving inverse. 
Remarks: If the group G is compact, we can replace the
discrete observable {fg |g ∈ G} in Theorem
2 by the conR
tinuous G-valued density g 7→ fg := G ω −1 ◦ g dµ(g),
where µ is the normalized Haar measure on G. While it
is far from clear that we should want to regard this as
a “continuously indexed observable” in any literal sense,
it may be that discrete, coarse-grained
versions of the
R
effect-valued measure B 7→ g∈B fg dµ(g) (B ranging over
Borel subsets of G) can each underwrite some form of approximate teleportation protocol, of which a deterministic protocol is in some sense the limiting case. We defer
exploration of this possibility to a future paper.
Also note that homogeneity of A implies that the
group of base-preserving automorphisms of A, which is
finite or compact, acts transitively on the extreme points
of ΩA , so homogeneous weakly self-dual state spaces
are good candidates for supporting the deterministic
teleportation protocol described in Theorem 2, or its
continuous analogue.
5. Entanglement Swapping Consider a scenario in
which Alice and Bob each possess one wing of two nonlocal, bipartite systems, say S1 = A1 B1 and S2 = A2 B2 .
We may model this situation by supposing that the total system, S, is a composite of the four components
A1 , A2 , B1 and B2 . We then have, in addition to the
two non-local marginal systems S1 and S2 , two local systems, A = A1 A2 and B = B1 B2 corresponding to Alice
and Bob, respectively.
Suppose now that f is an effect on A = A1 A2 and
µ and ω are states in S1 = A1 B1 and S2 = A2 B2 ,
respectively. We have corresponding positive operators
fb : A1 → A∗2 , ω
b : A∗2 → B2 , and µ
b∗ : B1∗ → A1 (the
∗
dual of µ
b : A1 → B1 ). Composing, we obtain a positive
operator ω
b ◦ fb ◦ µ
b∗ : B1∗ → B2 , corresponding to a subnormalized state in B1 ⊗max B2 . The question arises,
does this belong to the marginal state space B = B1 B2 ?
Equivalently, can we implement the mapping in question
by (un-normalized) conditionalization on the outcome of
a measurement on A?
If S is a regular composite of A1 , A2 , B1 and B2 , the
answer is yes: µ ⊗ ω is then a legitimate state on S =
AB, whence, for all f ∈ A∗ , the partially evaluated state
(µ ⊗ ω)B (f ) = (µ ⊗ ω)(f ⊗ − ) lies in B. Now notice
the following analogue of Lemma 1 (proved in the same
way, i.e,. by checking it on pure tensors):

Lemma 5 With notation as above,
ω ◦ fb ◦ µ
b∗ ).
(f A ⊗ g B )(µS1 ⊗ ω S2 ) = g B (b

It follows that

ω
b ◦ fb ◦ µ
b∗ = (µ ⊗ ω)B (f ) ∈ B,

as claimed. This is analogous to the remote evaluation
protocol of Section 3: conditional upon Alice securing a
measurement outcome corresponding to f A , the conditional state of Bob’s system B = B1 ⊗ B2 corresponds to
A ◦µ
the operator ω
b ◦ fc
b∗ . We might call this state-pivoting,
as one can easily verify that the marginal state of B1 is
undisturbed.
Where the operation ω
b ◦fb can be reversed, this protocol
can be used to transfer the state µ from subsystem S1 to
subsystem B, as in conventional entanglement-swapping
Indeed, suppose that (i) A1 = B2 , (ii) there exists a
conclusive teleportation protocol for the tripartite system
A1 A2 B2 — i.e., that we can find a state ω
b in S2 and
an effect f in A∗ such that ω
b ◦ fb is proportional to the
identity operator on A1 . Then, for any µ ∈ S2 , Lemma
4 tells us that
(µ ⊗ ω)f = µ :
That is, conditional on the occurrence of f in some measurement by Alice on system A, the state of Bob’s system
B is µ. In this situation, we may say that µ has been teleported from S1 through ω to B.
The same considerations also allow us to convert an
effect f on A into a sub-normalized state on B. Indeed,
if S1 and S2 contain states η1 and η2 , respectively,
corresponding to order-isomorphisms ηbi : Bi∗ ≃ Ai for
i = 1, 2, then the mapping fb 7→ ηb1 ◦ fb ◦ ηb2∗ gives us an
order-preserving linear injection from A∗ to B. Pursuing
this a bit further, let (C, ⊛) be a monoidal theory, as
defined in Section 2. Let us say that a state-space
A ∈ C is C-self dual iff there exists a state η ∈ A ⊛ A
with ηb : A∗ → A an isomorphism, and ηb−1 : A → A∗
corresponding to an effect in (A ⊛ A)∗ . It follows from
the above, with A1 = A2 and B1 = B2 , that if A and B
are C-self dual, then so is A ⊛ B.
Four-part disharmonies The entanglement-swapping
protocol described above can be applied negatively, to
show that certain four-part composites aren’t regular.
Example: Consider any four non-classical state spaces
A1 , A2 , B1 and B2 with B2 ≃ A1 . If A1 , A2 and B2 support a conclusive teleportation protocol (in particular, if
all three are isomorphic and weakly self-dual) then the
composite
S := (A1 ⊗min A2 ) ⊗max (B1 ⊗min B2 )
cannot be regular. Indeed, arguing as in the proof of
Corollary 1, we see that the reduced system B := B1 B2

<!-- page 12 -->
12
is precisely B1 ⊗min B2 ≃ B1 ≃ A1 ⊗min B1 , while
S1 := A1 B1 is A1 ⊗max B1 . Since A1 and B1 are nonclassical, we can find an entangled state ω ∈ A1 ⊗max B1 .
If the composite were regular, we could apply the
entanglement-swapping protocol of Lemma 5 to pivot
ω to an entangled state on B = B1 ⊗min B2 —which is
absurd, as the latter contains no entangled states.
A similar disharmony obtains between the maximal
and the usual tensor products of quantum systems [6].
Consider a situation in which two quantum-mechanical
systems, represented by state spaces A and B, are
coupled by means of the maximal tensor product to
form A ⊗max B. Suppose also that A and B are
themselves composite systems, say A = A1 ⊗ A2 and
B = B1 ⊗ B2 , where ⊗ is the usual quantum-mechanical
tensor product. Then an application of Lemma 5
shows that if ω is a maximally entangled state on
A2 ⊗ B2 and ρ ∈ A1 ⊗max B1 is what we might call an
ultra-entangled state of A1 ⊗ B1 —that is, a state of the
maximal tensor product not belonging to A1 B1 —then
conditional on a suitable maximally entangled outcome
for a measurement on A, one finds that ρ has apparently been teleported through ω, and now resides in
B1 ⊗ B2 —which is absurd, as the latter is an ordinary
composite quantum system hosting no ultra-entangled
states.
6. Conclusions and Prospectus We have established necessary and sufficient conditions for a composite of three probabilistic models to admit a conclusive
teleportation protocol. We have also provided a class
of examples illustrating that deterministic teleportation
can be supported by weakly self-dual probabilistic models that are far from being either classical or quantummechanical. Along the way, we have developed tools for
manipulating regular composites that are likely to be useful in any systematic study of categories of probabilistic
models, and particularly categories equipped with more
than a single tensor product.
It remains an open problem to find non-trivial necessary and sufficient conditions for a deterministic teleportation protocol to exist. Theorem 3 is a step in this
direction; however, one would like a sharp criterion for
the existence of a G-equivariant isomorphism A∗ ≃ A,
where G is a finite or, more generally, compact group
acting transitively on the extreme points of ΩA .
Looking further ahead, one would like to consider in
detail the categorical structure of probabilistic theories
subject to precise axioms governing remote evaluation,
teleportation, etc., making contact with the rapidly
developing theory of information processing in compactclosed categories [1, 2, 19, 20].
Acknowledgements Significant parts of this work were
done at the following conferences, retreats and workshops

during 2007: (i) New Directions in the Foundations of
Physics, College Park, MD (HB, JB, ML, AW); (ii) Philosophical and Formal Foundations of Modern Physics,
Les Treilles, (HB); (iii) Operational Theories as Foils to
Quantum Theory, Cambridge, supported by the Foundational Questions Institute (FQXi) and SECOQC (HB,
JB, ML, AW); (iv) Operational Approaches to Quantum
Theory, Paris (HB, AW). We wish to thank the organizers of these events, Jeffrey Bub and Rob Rynasiewicz,
Tony Short and Rob Spekkens, and Alexei Grinbaum,
for the invaluable opportunities they provided for us to
work on this project.
At IQC, ML was supported in part by MITACS and
ORDCF. ML was supported in part by grant RFP1-06006 from FQXi. Research at Perimeter Institute for Theoretical Physics is supported in part by the Government
of Canada through NSERC and by the Province of Ontario through MRI. This work was also carried out partially under the auspices of the US Department of Energy
through the LDRD program at LANL under Contract
No. DE-AC52-06NA25396.

∗

Electronic address: barnum@lanl.gov
Electronic address: jbarrett@perimeterinstitute.ca
‡
Electronic address: matt@mattleifer.info
§
Electronic address: wilce@susqu.edu
[1] S. Abramsky and B. Coecke, A categorical semantics of
quantum protocols, quant-ph/0402130v5 (2004, revised
2007)
[2] J. Baez. Quantum quandaries: a category-theoretic perspective. quant-ph/0404040, 2004.
[3] 2 J. Barrett, Information processing in general probabilistic theories, Phys. Rev. A. 75 (2007) 032304[4] H. Barnum, J. Barrett, M. Leifer and A. Wilce,
Cloning and Broadcasting in Generic Probabilistic Models, quant-ph/061129 (2006)
[5] H. Barnum, J. Barrett, M. Leifer and A. Wilce, A general
no-cloning theorem, Phys. Rev. Lett. 99 240501 (2007).
[6] H. Barnum, C. Fuchs, J. Renes and A. Wilce, Influencefree states on coupled quantum-mechanical systems,
quant-ph/0507108 (2005)
[7] C.H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A.
Peres and W.K. Wootters, Teleporting an unknown
quantum state via dual classical and Einstein-PodolskyRosen channels, Physical Review Letters, Vol. 70 (1993),
1895 1899.
[8] E. B. Davies and J. T. Lewis, An operational approach
to quantum probability, Comm. Math. Phys. 17 (1970)
239-260
[9] C. M. Edwards, The operational approach to quantum
probability I, Comm. Math. Phys. 17 (1971), 207-230.
[10] A. J. Ellis, Linear operators in partially ordered normed
vector spaces, J. London Math. Soc. 41 (1966) 323-332.
[11] A. Holevo, Radon-Nikodym derivatives of quantum instruments J. Math. Phys. 39 (1998) 1373[12] L. Hardy, A framework for probabilistic theories with
non-fixed causal structure, J. Phys. A. 40 (2007) 3081
†

<!-- page 13 -->
13
[13] L. Hardy, Disentangling nonlocality and teleportation
quant-ph/9906123 (1999)
[14] M. Kläy, D. J. Foulis, and C. H. Randall, Tensor products
and probability weights, Int. J. Theor. Phys. 26 (1987),
199-219.
[15] Koecher, Die geoodätischen von Positivitaätsbereichen,
Math. Annalen 135 (1958) 192-202.
[16] G. Ludwig, An Axiomatic Basis of Quantum Mechanics
1, 2, Springer-Verlag, 1985, 1987.
[17] G. Mackey, Mathematical Foundations of Quantum Mechanics, Benjamin, 1963.
[18] I. Namioka and R. Phelps, Tensor products of compact
convex sets, Pacific J. Math. 9 (1969), 469-480.
[19] P. Selinger. Towards a semantics for higher-order quantum computation. In Proceedings of the 2nd International Workshop on Quantum Programming Languages,
Turku Finland, pages 127–143. Turku Center for Computer Science, 2004. Publication No. 33.
[20] P. Selinger. Dagger compact closed categories. Electronic Notes in Theoretical Computer Science, 170:139–
163, 2007. Proceedings of the 3rd International Workshop on Quantum Programming Languages (QPL 2005),
Chicago.
[21] R. Spekkens, Evidence for the epistemic view of quantum
states: a toy theory, Phys. Rev. A. 75 (2007) 032110
[22] G. Wittstock, Ordered normed tensor products, in H.
Neumann and H. Hartkamper (eds.), Foundations of
quantum mechanics and ordered linear spaces, Springer
Lecture Notes in Physics, 1974.
[23] E. B. Vinberg, Homogeneous cones, Dokl. Acad. Nauk.
SSSR 141 (1960) 270-273; English trans. Soviet Math.
Dokl. 2 (1961) 1416-1619.
[24] To spell this out, suppose γ1 , γ2 ∈ Γ with normalized
versions γ̃1 = t1 γ1 , γ̃2 = t2 γ2 ∈ Γ̃. Now consider a convex
combination
α = pe
γ1 + qe
γ2
where p, q ≥ 0 with p + q = 1. Then
α = pt1 γ1 + qt2 γ2 .
Let

pt1
pt2
γ1 +
γ2 ∈ Γ
pt1 + qt2
pt1 + qt2
and note that
γ=

α = (pt1 + qt2 )γ = γ
e∈e
Γ.

Appendix: proofs from section 3

Proof of Lemma 1 P
(a) Let µ ∈ (AJ )+ be a positive linear
combination µ = p tp (ωp )Jap of reduced states, where
∗
for all p, ωp ∈ A and ap = (api ) ∈ Πi∈I\J
for
P Ai . Then
K
any b = (bj ) ∈ Πj∈J\K , we have µb = p tp (ωp )Jap (b) =
P
K
J K
K
K
p (ωp )ap ⊗b ∈ A . It follows that ((A ) )+ ⊆ (A )+ .
For the converse, let ω ∈ A+ : for any a = (ai ) ∈ Πi∈I Ai ,
we have a = b ⊗ c where b = (bj ) ∈ Πj∈J\K Aj and
J K
c = (ck ) ∈ Πk∈K Ak . Thus, ωaK = (ωbJ )K
c ∈ ((A ) )+ .
For (b), suppose ω ∈ A and a = (ai ) in Πi6∈I A∗i . Pick
any c = (bj ) ∈ Πj∈J A∗j : we can set
α = ωaJ ∈ AJ and β = ωbI−J ∈ AI−J .
If A is regular, we then have α ⊗ β ∈ A, whence,
α = (α ⊗ γ)JuI−J .
Part (c) follows from (a) and (b). 
J
Proof of Proposition 1 Let A J
= i∈I Ai . We first show
that, for any set J ⊆ I, AJ = j∈J Aj ). By assumption,
we have
K
K
K
K
Ak ).
Ak ) ≥ (
Aj ) ⊗min (
A≃(
Aj ) ⊙ (
j∈J

j∈J

k∈I\J

k∈I\J

J

It follows that, for every µ ∈
J
k∈I\J Ak , µ ⊗ ν ∈ A; hence,

j∈J Aj , and for any ν ∈

µ = (µ ⊗ ν)J⊗k∈I\J uk ∈ AJ .
J
Thus, j∈J Aj ≤ AJ .
For the reverse inclusion, note that we also have
K
K
K
K
Ak );
Ak ) ≤ (
Aj ) ⊗max (
(
Aj ) ⊙ (
j∈J

k∈I\J

j∈J

k∈I\J

J
hence, for any ω ∈ A and any f ∈ ( k∈K Ak )∗ —
in particular,
for any f = (fk )k∈I\J —we have
J
ωfJ ∈
A
The rest of the proof now proj∈J j .
ceeds easily.J If J1J
, ..., Jm is a partition
of I, then we
Jm
m
Jp
. Since ⊙ is
A
)
=
A
have A =
(
p=1
j∈Jp p
p=1
Jp
a coupling, this last is a composite of A , p = 1, ..., m. 
