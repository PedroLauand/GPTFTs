---
type: paper
date: 2016-06-30
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1606.09331v3)
reviewed: false
---

# Composites and Categories of Euclidean Jordan Algebras

Machine-generated and unreviewed text extraction of arXiv:1606.09331v3
(62 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1606.09331v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Composites and Categories of Euclidean
Jordan Algebras
arXiv:1606.09331v3 [quant-ph] 5 Nov 2020

Howard Barnum1,2,3 , Matthew A. Graydon4,5 , and Alexander Wilce6
1

Riemann Center for Geometry and Physics, Institute for Theoretical Physics, Leibniz Universität Hannover

2

University of New Mexico

3

Currently unaffiliated hnbarnum@aol.com

4

Department of Applied Mathematics, University of Waterloo

5

Institute for Quantum Computing, University of Waterloo m3graydo@uwaterloo.ca

6

Department of Mathematical Sciences, Susquehanna University wilce@susqu.edu

We consider possible non-signaling composites of probabilistic models based on euclidean Jordan algebras (EJAs), satisfying some reasonable
additional constraints motivated by the desire to construct dagger-compact
categories of such models. We show that no such composite has the exceptional Jordan algebra as a direct summand, nor does any such composite
exist if one factor has an exceptional summand, unless the other factor is
a direct sum of one-dimensional Jordan algebras (representing essentially a
classical system). Moreover, we show that any composite of simple, nonexceptional EJAs is a direct summand of their universal tensor product,
sharply limiting the possibilities.
These results warrant our focussing on concrete Jordan algebras of hermitian matrices, i.e., euclidean Jordan algebras with a preferred embedding
in a complex matrix algebra. We show that these can be organized in
a natural way as a symmetric monoidal category, albeit one that is not
compact closed. We then construct a related category InvQM of embedded euclidean Jordan algebras, having fewer objects but more morphisms,
that is not only compact closed but dagger-compact. This category unifies
finite-dimensional real, complex and quaternionic mixed-state quantum mechanics, except that the composite of two complex quantum systems comes
with an extra classical bit.
Our notion of composite requires neither tomographic locality, nor preservation of purity under tensor product. The categories we construct include
examples in which both of these conditions fail. In such cases, the information capacity (the maximum number of mutually distinguishable states) of
a composite is greater than the product of the capacities of its constituents.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

1

<!-- page 2 -->
1 Introduction
Formally real Jordan algebras were first proposed as models of quantum systems by P.
Jordan in 1933 [40]. Abstractly, a Jordan algebra is a real vector space A equipped with
a commutative bilinear product satisfying the Jordan identity a2 (a b) = a (a2 b)
for all a, b ∈ A (where a2 = a a). We also assume that A has a unit element, which
P
we denote by uA . A is formally real if, for a1 , ..., an ∈ A, ni=1 a2i = 0 only when ai = 0
for all i. If A is finite-dimensional, this is equivalent to A’s being euclidean, meaning
that it carries an inner product such that ha b, ci = ha, b ci for all a, b, c ∈ A. It will
be convenient in what follows to compress the phrase euclidean Jordan algebra, which
will occur very frequently, to the acronym EJA.
The standard example is the space L(H) of self-adjoint operators on a finitedimensional Hilbert space H, with a b = (ab + ba)/2, and with ha, bi = Tr(ab). In
1934, Jordan, von Neumann and Wigner [43] showed that all finite-dimensional formally real — equivalently, euclidean — Jordan algebras are direct sums of irreducible,
or simple, such algebras, and that the latter are of just five kinds: self-adjoint parts of
real, complex or quaternionic matrix algebras (which we can regard as real, complex
or quaternionic quantum systems) spin factors (which are analogues of qubits in which
the “Bloch sphere” can have arbitrary finite dimension), and the exceptional Jordan
algebra of 3 × 3 self-adjoint octonionic matrices.
A reasonable objection is that the physical meaning of the Jordan product is obscure. (Indeed, it is not obvious why the observables of a physical system should
carry any physically meaningful bilinear product at all.) Happily, there are alternative
characterizations of euclidean Jordan algebras in terms of ordered vector spaces and
related concepts having readier physical, probabilistic, or operational interpretations.
The Koecher-Vinberg Theorem ([45, 62]; see also [44], [26], Chapter III or [56], Chapter
I, §8) identifies euclidean Jordan algebras with finite-dimensional ordered vector spaces
having homogeneous, self-dual cones; work of Alfsen and Shultz [2, 4] characterizes
EJAs in terms of certain projections associated with closed faces of the positive cone.1
Exploiting these results, several recent papers [15, 14, 53, 63, 64, 66, 65] have shown
that physically reasonable postulates force a finite-dimensional physical system to have
the structure of a euclidean Jordan algebra. To this extent, euclidean Jordan algebras
are a natural class of models for physical systems.
A physical theory, however, is more than a collection of models of physical systems.
It must also describe how systems change and how they interact. It is natural, therefore,
to represent a physical theory as a category, in which objects represent physical systems
and morphisms represent physical processes. To accommodate composite systems, one
wants the category to be monoidal, i.e., to be equipped with an associative “tensor
product”. This point of view has been developed very fruitfully in [1, 8] and elsewhere,
where it is shown that many features of finite-dimensional quantum mechanics can be

··

··

·

· ·

·

·

1

Alfsen and Shultz’ results apply, more generally, to JB-algebras, which in the context of finite
dimension are the formally real Jordan algebras.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

2

<!-- page 3 -->
recovered if the category in question is compact closed, or, better still, dagger-compact
(terms we explain in Section 5).
In this paper, building on work of Hanche-Olsen [30] and Jamjoom [38] on tensor products of JC-algebras, we classify the possible composites of euclidean Jordanalgebraic systems, subject to a standard “no-signaling” condition and a few reasonable
additional constraints. In particular, we show that no such composite exists if either
factor is exceptional, unless the other factor is a direct sum of trivial (i.e. 1-dimensional)
Jordan algebras. Furthermore, we show that a composite of simple, nontrivial Jordan
algebras is always a special Jordan algebra, and, indeed, a direct summand of the
universal tensor product defined by Hanche-Olsen
Restricting attention further to Jordan algebras corresponding to real, complex and
quaternionic quantum systems — equivalently, self-adjoint parts of real, complex and
quaternionic matrix algebras — we then identify two different monoidal sub-categories
extending the category of finite-dimensional complex matrix algebras and CP maps.
One of these, which we call RSE, unifies real, complex and quaternionic quantum
mechanics, but lacks certain desirable features. In particular, in this category, states
are not represented by morphisms; hence, the category is far from being compact closed.
The other category, which we call InvQM, and which is compact closed, also embraces
real, complex and quaternionic quantum systems and processes (CP maps), except that
its rule for composing standard complex quantum systems yields an extra classical bit.
These results, combined with the those of (any of) the papers cited above, in which
a euclidean Jordan structure emerges from information-theoretically, physically or operationally natural assumptions, lend support to the idea of unified quantum theory
that embraces real, complex and quaternionic quantum systems, and permits the formation of composites of these. Consistent with the results of [17], the composites that
arise in these constructions do not in general have the property of “tomographic locality”: states on the composite of two Jordan-algebraic systems are not, in general,
determined by the joint probabilities they assign to measurement outcomes associated
with the two component systems. Equivalently, the Jordan algebra AB corresponding
to a composite of two formally real Jordan-algebraic systems A and B, will generally
be larger than the algebraic (i.e., vector-space) tensor product A ⊗ B.
Remark: A related proposal is advanced by Baez [7], who points out that one can
regard real and quaternionic quantum systems as pairs (H, J), where H is a complex
Hilbert space and J is an anti-unitary satisfying J 2 = 1 (the real case) or J 2 = −1
(the quaternionic case). Such pairs can be organized into a dagger-compact symmetric monoidal category, taking morphisms (H1 , J1 ) → (H2 , J2 ) to be linear mappings
intertwining J1 and J2 , and (H1 , J1 ) ⊗ (H2 , J2 ) = (H1 ⊗ H2 , J1 ⊗ J2 ). This provides
a unification of real and quaternionic quantum mechanics at the level of pure states
and linear mappings between the relevant Hilbert spaces, whereas our approach takes
in quantum systems over all three of the associative division algebras R, C and H, at
the level of mixed states, observables and completely positive maps. While the precise
connection between Baez’ approach and ours is not yet entirely clear, it seems to us
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

3

<!-- page 4 -->
likely that an application of Selinger’s CPM construction [57] to Baez’ category will
yield a category of the type we consider here.
Our results rest on a mixture of standard facts about ordered vector spaces, the
order structure and the representation theory of euclidean Jordan algebras, and the
pioneering work of Hanche-Olsen [30] on universal representations and tensor products
of JC-algebras. Since much of this will be unfamiliar to many readers, we have included
a good amount of purely expository material. Section 2 provides background on order
unit spaces and their interpretation as general probabilistic models, including a fairly
general notion of composite for such model. This material will be more familiar to
many readers, but some of our notation and terminology, and some notions specific to
our present purposes, may not be. Section 3 collects background material on euclidean
Jordan algebras, their universal representations, and Hanche-Olsen’s universal tensor
product.
The balance of the paper is organized as follows. In Section 4, we introduce a general
definition for the composite of two euclidean Jordan-algebraic probabilistic models, and
establish some basic properties of any such composite. Along the way, we see that the
composite of two simple, nontrivial EJAs must be embeddable in a complex matrix
algebra, i.e. it must be special (Theorem 4.12). From this it follows that no simple,
nontrivial EJA has any composite with an exceptional EJA (Corollary 4.14), and that
if A and B are simple, special EJAs, then any composite of A and B must be an ideal
— that is, a direct summand — in their universal tensor product (Theorem 4.15).
These results warrant our focusing on special EJAs. Section 5 develops a canonical,
and naturally associative, tensor product of embedded EJAs, that is, pairs (A, MA )
where MA is a finite-dimensional complex ∗-algebra and A is a Jordan subalgebra of
the self-adjoint part of MA . (The universal tensor product is the special case in which
MA and MB are the universal complex enveloping algebras of A and B.) In Section
6 we introduce a class of mappings we call completely Jordan-preserving and use these
to construct symmetric monoidal categories of embedded EJAs, some of which we then
show are compact closed or, indeed, dagger-compact. Section 7 concludes with further
discussion of these categories and their physical and information-processing significance.
To avoid obstructing the flow of the main arguments, we have removed some technical
details to a series of appendices.
Acknowledgments Some of our results have previously been announced, without
proof, in [13].2
HB and AW wish to thank C. M. Edwards for introducing them
to the paper [30] of Hanche-Olsen. HB and MG thank Cozmin Ududec for valuable discussions. AW was supported by a grant from the FQXi foundation (FQXi-RFP3-1348).
This research was supported in part by Perimeter Institute for Theoretical Physics.
Research at Perimeter Institute is supported by the Government of Canada through
the Department of Innovation, Science and Economic Development Canada and by the
Province of Ontario through the Ministry of Research, Innovation and Science.
2

There, it is erroneously claimed that RSE is compact closed. This error is corrected in Section 6
of the present paper; see especially Examples 6.3 and 6.11
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

4

<!-- page 5 -->
2 Ordered vector spaces and probabilistic models
In this section and the next, we present enough background material to make this paper
reasonably self-contained. This section summarizes basic information about ordered
vector spaces and the “convex operational” (or “generalized probabilistic theories”)
framework for discussing probabilistic physical theories.
A good general reference for ordered vector spaces is Chapter 1 of [3] (or the summary in Appendix A of [4]). The use of ordered vector spaces with an order unit
as probabilistic models goes back at least to the work of Ludwig [46, 47]; see also
[24, 25, 35]. The more recent literature in this tradition (for a survey of which, see
[18]) has focussed on finite-dimensional quantum theory, and accordingly makes use
only of finite-dimensional ordered spaces. This will also be the case in this paper.
Hence, in order to avoid constant repetition of the qualifier, we adopt the convention
that all vector spaces are finite dimensional unless otherwise indicated. All topological
statements concerning such a space, for example references to the interior of a subset,
should be understood as referring to its unique linear topology.

2.1 Ordered vector spaces
Let A be a real vector space. A (convex, pointed) cone in A is a convex set K ⊆ A such
that a ∈ K implies ta ∈ K for all t ∈ R+ , and K ∩ −K = {0}. A cone K is generating
iff it spans A, i.e., if every a ∈ A can be expressed as a difference of elements of K. Any
cone (generating or not) induces a partial ordering of A, given by a ≤ b iff b − a ∈ K;
this is translation-invariant, i.e, a ≤ b implies a + c ≤ b + c for all a, b, c ∈ A, and
homogeneous, i.e., a ≤ b implies ta ≤ tb for all t ∈ R+ . Conversely, such an ordering
determines a cone, namely K = {a|a ≥ 0}. Accordingly, an ordered vector space is a
real vector space A equipped with a designated positive cone cone A+ . It is common
to assume, and we shall assume here, that A+ is closed and generating.
If A and B are ordered vector spaces, a linear mapping f : A → B is positive iff
f (A+ ) ⊆ B+ . If f is bijective and f (A+ ) = B+ , then f −1 (B+ ) = A+ , so that f −1 is also
positive. In this case, we say that f is an order isomorphism. An order automorphism
of A is an order isomorphism from A to itself.
Denoting the dual space of A by A∗ , the dual cone, A∗+ , is the set of positive linear
functionals on A. Since we are assuming that A+ is generating, it is easy to see that
A∗+ ∩ −A∗+ = {0}. In our finite-dimensional setting, A∗+ is also generating. Note that
if B is another ordered vector space and φ : A → B is a positive linear mapping, then
the dual mapping φ∗ : B ∗ → A∗ is also positive.

2.2 Order units and probabilistic models
An order unit in an ordered vector space A is an element u ∈ A+ such that, for all
a ∈ A, a ≤ tu for some t ∈ R+ . In finite dimensions, this is equivalent to u belonging

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

5

<!-- page 6 -->
to the interior of A+ (cf. [6], Theorem 2.8). An order unit space is a pair (A, u) where
A is an ordered vector space and u is a designated order unit.
An order unit space provides the machinery to discuss probabilistic concepts. A
state on (A, u) is a positive linear functional α ∈ A∗ with α(u) = 1. An effect is an
element a ∈ A+ with a ≤ u. If α is a state and a is an effect, we have 0 ≤ α(a) ≤ 1:
we interpret this as the probability of the given effect on the given state.
A discrete observable on A with values λ ∈ Λ is represented by an indexed family
{aλ |λ ∈ Λ} of effects summing to u, the effect aλ representing the event of obtaining
value λ in a measurement of the observable. Thus, if α is a state, λ 7→ α(aλ ) gives
a probability weight on Λ. (One can extend this discussion to include more general
observables by considering effect-valued measures (cf. [25]), but we will not need this
extra generality here.)
We denote the set of all states of A by Ω; the set of all effects — the interval between
0 and u — is denoted [0, u]. In our present finite-dimensional setting, both are compact
convex sets. Extreme points of Ω are called pure states.
Examples
(1) Discrete Classical Probability Theory: If S is a finite set, regarded as the outcome
space of some classical experiment, let A(S) = RS , ordered pointwise. Elements of
A(S)+ are then non-negative random variables, and effects are random variables with
values between 0 and 1. We turn this into an order unit space by taking u ∈ A(S)+ to
be the constant function with value 1. It is then easy to show that normalized states on
A(S) correspond exactly to probability weights on S; discrete observables correspond
in a natural way to discrete “fuzzy” random variables. Extreme effects, i.e, extreme
points of [0, u], are easily seen to be characteristic functions of subsets of S; hence,
an observable {aλ } with aλ extreme for each λ, corresponds to an ordinary “sharp”
random variable.
(2) Discrete Quantum Probability Theory: If H is a finite-dimensional Hilbert space,
let A(H) = L(H), the space of self-adjoint operators on H, ordered by the cone of positive semidefinite operators; let u = 1, the identity operator on H. Then each normalized
state α has the form α(a) = Tr(ρa) where ρ is a density operator, and, conversely, every
density operator determines in this way a normalized state,. Observables correspond
to discrete POVMs; thus, we recover orthodox finite-dimensional quantum probability
theory.
(3) A class of examples that embraces both (1) and (2) is the following. Let M be
a unital complex ∗-algebra; define M+ to consist of all a ∈ M with a = b∗ b for some
b ∈ M: then (Msa , M+ ) is an ordered vector space, in which the unit element of M
serves as an order unit. If M is finite-dimensional and commutative, one essentially recovers example (1); if M is the algebra Mn (C) of n×n complex matrices, one essentially
recovers example (2). More generally, if M is finite-dimensional, Wedderburn’s theorem tells us that M is a direct sum of matrix algebras, so one has finite-dimensional
quantum theory with superselection rules (classical discrete probability theory being
the special case in which all superselection sectors — that is, direct summands — are
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

6

<!-- page 7 -->
one-dimensional).
One might wish to privilege certain states and/or certain effects of a probabilistic model
as being “physically possible”. One way of doing so is to consider ordered subspaces
V ≤ A∗ and E ≤ A, with u ∈ E: this picks out the set of states α ∈ V ∩ A∗+ and the set
of effects a ∈ E ∩ A+ , a ≤ u. The pair (E, V ) then serves as a probabilistic model for a
system having these allowed states and effects. However, in the three examples above,
and in those that concern us in the rest of this paper, it is always possible to regard
all states in A∗ , and all effects in A, as allowed. Henceforth, then, when we speak of a
probabilistic model — or, more briefly, a model — we simply mean an order unit space
(A, u). It will be convenient to adopt the shorthand A for such a pair, writing uA for
the order unit where necessary.
Processes, Symmetries and Dynamics By a process affecting a system represented by
a probabilistic model A, we mean a positive linear mapping φ : A → A, subject to the
condition that φ(uA ) ≤ uA . The probability of observing an effect a after the system
has been prepared in a state α and then subjected to a process φ is α(φ(a)). One
can regard α(φ(u)) as the probability that the system is not destroyed by the process.
We can, of course, replace φ : A → A with the adjoint mapping φ∗ : A∗ → A∗ given
by φ∗ (α) = α ◦ φ, so as to think of a process as a mapping from states to possibly
sub-normalized states. Thus, we can view processes either as acting on effects (the
“Heisenberg picture”), or on states (the “Schrödinger picture”).
Any non-zero positive linear mapping φ : A → A is a non-negative scalar multiple of
a process in the above sense: since Ω(A) is compact, the function α 7→ α(φ(uA )) attains
a maximum value m > 0 on Ω(A); m−1 φ is then a process. For this reason, we make
little further distinction here between processes and positive mappings. In particular, if
φ is an order automorphism of A, then both φ and φ−1 are scalar multiples of processes
in the above sense: each of these processes “undoes” the other, up to normalization,
i.e., with nonzero probability. A process that can be reversed with probability one
is represented by an order-automorphism φ such that φ(uA ) = uA , in which case φ∗
takes normalized states to normalized states. Such an order-automorphism is called a
symmetry of A.
We denote the group of all order-automorphisms of A by Aut(A).3 This is a Lie
group (see e.g. [34], pp. 182-183); its connected identity component (consisting of those
processes that can be obtained by continuously deforming the identity map) is denoted
Aut0 (A). A possible (probabilistically) reversible dynamics for a system modelled by
A is a homomorphism t 7→ φt from (R, +) to Aut(A), i.e., a one-parameter subgroup of
Aut(A).
One might wish to privilege certain processes as reflecting physically possible motions or evolutions of the system. In that case, one might add to the basic data (A, u) a
preferred group G(A) ≤ Aut(A) of order automorphisms. We refer to such a structure
3

Here our usage diverges from that of [4] and [26], who use Aut(A) to denote the group of Jordan
automorphisms of a Jordan algebra A.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

7

<!-- page 8 -->
as a dynamical probabilistic model, since the choice of G(A) constrains the permitted
probabilistically reversible dynamics of the model.4
When Aut(A) acts transitively on the interior of A+ , the cone A+ (or the ordered
space A) is said to be homogeneous. The positive cone of a euclidean Jordan algebra is
always homogeneous, as we will see below. 5
Self-Duality An inner product h | i on an ordered vector space A is positive iff the
associated mapping A → A∗ , a 7→ ha|, is positive, i.e,. if ha, bi ≥ 0 for all a, b ∈ A+ . We
say that h | i is self-dualizing if a 7→ ha| maps A+ onto A∗+ , so that a ∈ A+ if and only
if ha, bi ≥ 0 for all b ∈ B. We say that A (or its positive cone) is self-dual if A admits
a self-dualizing inner product. In this case, we can represent states of A internally: if
α ∈ A∗+ with α(u) = 1, there is a unique a ∈ A+ with ha|bi = α(b) for all b ∈ A+ .
Conversely, if a ∈ A+ with ha, ui = 1, then ha| is a state. We will also use the notation
h , i for an inner product.
The probabilistic models associated with classical and quantum systems, as discussed above, are self-dual. Indeed, in non-relativistic quantum theory, where A =
L(H), the standard trace inner product ha, bi = Tr(ab) is self-dualizing. Here it is usual
to identify states internally, i.e., as density operators.
If A and B are both self-dual and φ : A → B is a positive linear mapping, we can
use self-dualizing inner products on A and B to represent the mapping φ∗ : B ∗ → A∗
as a positive linear mapping φ† : B → A, setting ha, φ† (b)i = hφ(a), bi for all a ∈ A and
b ∈ B. If φ : A → A is an order-automorphism, then so is φ† .

2.3 Composites of probabilistic models
If A and B are probabilistic models of two physical systems, one may want to construct
a model of the pair of systems considered together. In quantum mechanics, where A =
L(H1 ) and B = L(H2 ), one would form the model AB = L(H1 ⊗ H2 ) associated with
the tensor product of the two Hilbert spaces. In the framework of general probabilistic
models, there is no such canonical choice for a model of a composite system. However,
one can at least say what one means by a composite of two probabilistic models: at a
minimum, one should be able to perform measurements on the two systems separately,
and compare the results. More formally, there should be a mapping π : A × B → AB
taking each pair of effects (a, b) ∈ A × B to an effect π(a, b) ∈ AB. One would like
4

A more general definition of a dynamical model would require only that the set of possible evolutions form a semigroup of positive maps. This level of generality will emerge naturally later in this
paper, when we consider categories of systems. The definition above is sufficient for our immediate
purposes.
5
Although we do not need this fact, we note that for a homogeneous cone in an ordered vector space
A, the connected identity component Auto (A) of the Aut(A) also acts transitively on the interior of
A+ ; see e.g. [26], pp. 5-6.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

8

<!-- page 9 -->
this to be non-signaling, meaning that the probability of obtaining a particular effect
on one of the component systems in a state ω ∈ Ω(AB) should be independent of what
observable is measured on the other system. One can show that this is equivalent to π’s
being bilinear, with π(uA , uB ) = uAB [18]. Finally, one would like to be able to prepare
A and B separately in arbitrary states. Summarizing:
Definition 2.1. A (non-signaling) composite of probabilistic models A and B, is a pair
(AB, π) where AB is a probabilistic model, and π : A × B → AB is a bilinear mapping
such that
(a) π(a, b) ∈ (AB)+ for all a ∈ A+ and b ∈ B+ ;
(b) π(uA , uB ) = uAB ;
(c) For every pair of states α ∈ Ω(A) and β ∈ Ω(B), there exists a state γ ∈ Ω(AB)
such that for every pair of effects a ∈ A and b ∈ B, γ(π(a, b)) = α(a)β(b).6
Since π is bilinear, it extends uniquely to a linear mapping A ⊗ B → AB. In what
follows, we abuse notation slightly to denote this unique extension also by π, so that,
for instance, π(a ⊗ b) = π(a, b) for a ∈ A, b ∈ B.
Lemma 2.2. π is injective.
Proof: If π(T ) = 0 for some T ∈ A⊗B, then for each pair of states α ∈ Ω(A), β ∈ Ω(B),
we have by (c) of Definition 2.1 a state γ ∈ Ω(AB) with (α ⊗ β)(T ) = γ(π(T )) = 0.
But then T = 0 since product states span (A ⊗ B)∗ . 
This warrants our treating A⊗B as a subspace of AB and writing a⊗b for π(a, b). Note
that if ω is a state on AB, then π ∗ (ω) := ω ◦ π defines a joint probability assignment
on effects of A and B:
π ∗ (ω)(a, b) = ω(a ⊗ b).
This gives us marginal states ωA = ω(uA ⊗ −) and ωB = ω(− ⊗ uB ). Where these are
non-zero, we can also define conditional states ω1|b (a) := ω(a ⊗ b)/ωB (b) and ω2|a (b) =
ω(a ⊗ b)/ωA (a).7
When the mapping π : A⊗B → AB is also surjective, we can identify AB with A⊗B.
The joint probability assigment π ∗ (ω) then completely determines ω, so that states on
AB are such joint probability assignments. In this case, we say that AB is locally
tomographic, since states of AB can be determined by comparing the results of “local”
measurements, i.e., measurements carried out on A and B alone. In finite dimensions,
both classical and complex quantum-mechanical composites have this feature, while
composites of real quantum systems are not locally tomographic [5, 33].
6

γ is unique if AB is locally tomographic.

7

In the context of a more general definition of probabilistic models, in which the cone generated by
allowed states might not be the full dual cone A∗+ , we would need to modify this definition to enforce
that these conditional states belong to the allowed state-space. See [18] for details.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

9

<!-- page 10 -->
When dealing with dynamical probabilistic models, one needs to supplement conditions (a), (b) and (c) with the further condition that it should be possible for A and
B to evolve independently within the composite AB. That is:
Definition 2.3. A dynamical composite of dynamical probabilistic models A and B is
a composite AB, in the sense of Definition 2.1, plus a homomorphism
⊗ : G(A) × G(B) → G(AB)
such that (g ⊗ h)(a ⊗ b) = ga ⊗ hb for all g ∈ G(A), h ∈ G(B), a ∈ A and b ∈ B.
(Note that since AB may be larger than the algebraic tensor product A ⊗ B, the
order automorphism (g ⊗ h) need not be uniquely determined by the aforementioned
condition.)

2.4 Probabilistic theories as categories
A physical theory is more than a collection of models. At a minimum, one also needs
the means to describe interactions between physical systems. A natural way of accomplishing this is to treat physical theories as categories, in which objects represent
physical systems, and morphisms represent processes. In the setting of this paper, then,
it’s natural to regard a probabilistic theory as a category C in which objects are probabilistic models, i.e., order unit spaces, and in which morphisms give rise to positive
linear mappings between these.
The reason for this phrasing — morphisms giving rise to, as opposed to simply being,
positive linear mappings — is to allow for the possibility that two abstract processes that
behave the same way on effects of their source system, may differ in other ways—even
in detectable ways, such as their effect on composite systems of which the source and
target systems are components. If distinct morphisms between the same two objects
always induce distinct positive maps, we say the category, and the set of morphisms, has
local process tomography 8 . Notice that invertible morphisms A → A that preserve the
order unit then induce processes in the sense given above, so that every model A ∈ C
carries a distinguished group of reversible processes: models in C, in other words, are
automatically dynamical models.
In order to allow for the formation of composite systems, it is natural to ask that
C be a symmetric monoidal category. That is, we wish to equip C with a bifunctorial
product ⊗ : C × C → C that is naturally associative and commutative, and for which
there is a unit object I with I ⊗ A ≃ A ≃ A ⊗ I for objects A ∈ C. Of course, we want
to take I = R. Moreover, for objects A, B ∈ C, we want A ⊗ B to be a composite in the
8

One way to make this more precise is to require that C contain R, ordered as usual and with
order unit 1, and that C(I, A) be the cone of positive linear maps R → A, so that C(I, A) ≃ A+ . Any
morphism φ ∈ C(A, B) then gives rise to a mapping φb : C(I, A) → C(I, B) by b
φ(a) = φ ◦ a for every
a ∈ C(I, A); this extends to a positive linear mapping A → B. We shall not pursue this further here;
see [16] for more on these lines.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

10

<!-- page 11 -->
sense of Definitions 2.1 and 2.3 above. In fact, though, every part of those definitions
simply follows from the monoidality of C, except for part (b) of 2.1; we must add “by
hand” the requirement that uA ⊗ uB = uA⊗B . The category will also pick out, for
each object A, a preferred group G(A), namely, the group of invertible morphisms in
C(A, A). The monoidal structure then picks out, for g ∈ g(A) and h ∈ G(B), a preferred
g ⊗ h ∈ G(AB). The bifunctoriality of ⊗ guarantees that this will satisfy condition (b)
of Definition 2.3; it will also satisfy condition (a) as long as C(I, A) = L+ (R, A) ≃ A+ .

3 Background on Euclidean Jordan algebras
In this section, we summarize the essential background information on euclidean Jordan
algebras and their universal tensor products that will be used in the sequel. General
references for this material are the monographs [4] of Alfsen and Shultz and [26] of
Faraut and Koranyi and [31] of Hanche-Olsen and Størmer, plus the paper [30] of
Hanche-Olsen.

3.1 Euclidean Jordan algebras
As we have already mentioned, a euclidean Jordan algebra (hereafter: EJA) is a finitedimensional commutative (but not necessarily associative) real algebra (A, ) with a
multiplicative unit element u, satisfying the Jordan identity a2 (a b) = a (a2 b)
for all a, b ∈ A, and equipped with an inner product satisfying ha b, ci = hb, a ci
for all a, b, c ∈ A. Obviously, any commutative, associative real algebra provides an
example, but not a very interesting one from the algebraic point of view. The basic
nonassociative example is the self-adjoint part Msa of a complex matrix algebra M , with
a b = (ab + ba)/2 and with ha, bi = Tr(ab). A Jordan subalgebra of a Jordan algebra
A is a subspace B of A that is closed under inclusion of Jordan products, and hence
is a Jordan algebra with Jordan product given by the restriction of A’s. Any Jordan
subalgebra of an EJA is also an EJA. Since real and quaternionic matrix algebras have
representations as subalgebras of complex matrix algebras, their self-adjoint parts are
EJAs. So, too, is the spin factor Vn = R × Rn , with an inner product given by the
usual vector dot product, and with a Jordan product given by

·
· ·· · ··

·

·

(t, x) (s, y) = (ts + hx, yi, ty + sx);
this can be embedded in M2k (C) if n = 2k or 2k + 1, as discussed in more detail in
Appendix C.
As we shall see in the next section, each EJA has an associated probabilistic model.
In the case of the EJAs Mn (C)sa , Mn (R)sa , and Mn (H)sa , the associated state spaces Ω
are the positive semidefinite trace-1 self-adjoint matrices, which can be viewed as the
density matrices associated with n-dimensional complex, real, or quaternionic Hilbert
spaces respectively. In each case, the maximal number of mutually perfectly distinguishable states (a quantity we call the information capacity of a state space) is n. The
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

11

<!-- page 12 -->
state space of Vn is an n-dimensional Euclidean ball, which has information capacity
2, and so constitutes a “generalized bit”. The associative EJA of dimension n has a
simplex with n vertices as its state space, so it can be viewed as a classical system of
information capacity n.
Classification If A and B are EJAs, their vector-space direct sum A⊕B is also an EJA
under the obvious inner product and slot-wise Jordan product. In this case, A and B
can be regarded as subalgebras of A ⊕ B. More than that, they are Jordan ideals, that
is, if a ∈ A and x ∈ A⊕B, then a x ∈ A as well, and similarly for B. Conversely, if A is
any EJA and A0 ≤ A is a Jordan ideal, then so is A1 :=A⊥
0 :={b ∈ A|∀a ∈ A0 a b = 0},
and A ≃ A0 ⊕ A1 . Since A is finite-dimensional, one can repeat this process so as to
L
decompose A into a direct sum A = i Ai of finitely many irreducible or simple EJAs
Ai . (See Appendix A for further details.)
The EJAs Mn (D)sa for D = R, C, H, and the spin factors Vn , discussed above, are
all simple.9 The Jordan-von Neuman-Wigner Classification Theorem [43] provides a
near converse: every simple EJA is isomorphic to one of these types, i.e. isomorphic
to a spin factor Vn , or to the self-adjoint part of a matrix algebra Mn (D) where D is
one of the classical division algebras R, C or H, or, if n = 3, the octonions, O. This
last example, which is not embeddable into a complex matrix algebra, is called the
exceptional Jordan algebra, or the Albert algebra.
A Jordan algebra that is embeddable in the self-adjoint part of a complex matrix algebra is said to be special. In addition to Mn (C)sa , the simple EJAs Mn (R)sa , Mn (H)sa
and Vn are all special. It follows from the classification theorem that any EJA decomposes as a direct sum Asp ⊕ Aex where Asp is special and Aex is a direct sum of copies
of the exceptional Jordan algebra.

·

·

Operator commutation For each a ∈ A, define La : A → A to be the operation of
Jordan multiplication by a: La (x) = a x for all x ∈ A. Elements a, b ∈ A are said to
operator commute iff La ◦ Lb = Lb ◦ La . If A is a Jordan subalgebra of Msa , where M
is a complex ∗-algebra, then for all x ∈ A,

·

4La (Lb x) = a(bx + xb) + (bx + xb)a = abx + axb + bxa + xba
and similarly
4Lb (La x) = bax + bxa + axb + xab.
If a and b operator commute, the left-hand sides are equal. Subtracting, we have
abx + xba − bax − xab = 0
or
[a, b]x + x[b, a] = 0
9
The n-dimensional associative EJA is not simple, rather it is a direct sum of n copies of the
one-dimensional EJA.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

12

<!-- page 13 -->
which is to say, [a, b]x − x[a, b] = 0. If M is unital and A is a unital subalgebra, so that
uA = 1M , then setting x = 1M ∈ A gives us [a, b] = −[a, b], i.e., a and b commute in M .
Projections and the Spectral Theorem A projection in an EJA A is an element
a ∈ A with a2 = a. If p, q are projections with p q = 0, we say that p and q are
orthogonal. This implies that hp, qi = hp, p qi = 0.10 In this case, p + q is another
projection. A projection not representable as a sum of other projections is said to be
minimal or primitive. A Jordan frame is a set E ⊆ A of pairwise orthogonal minimal
projections that sum to the Jordan unit. The Spectral Theorem for EJAs (see e.g. [26],
Theorem III.1.1, or [4], Theorem 2.20 for an infinite-dimensional version) asserts that
P
every element a ∈ A can be expanded as a linear combination a = x∈E tx x where E
is some Jordan frame and tx is a coefficient in R for each x ∈ E. If a has spectral
P
decomposition a = x∈E tx x, where E is a Jordan frame, then a ≥ 0 iff tx ≥ 0 for
all x ∈ E. (The “if” direction is trivial; for the converse, notice that since x, a ∈ A+ ,
hx, ai = tx kxk2 ≥ 0, whence, tx ≥ 0.
By summing over those x ∈ E for which tx has a given value, we obtain a decompoP
sition i ti pi where pi are pairwise Jordan-orthogonal projections and the coefficients
ti are distinct. In this form, the spectral decomposition is unique [26]. This gives us a
P
functional calculus, as we can now define f (a) = i f (ti )pi for any real-valued function
f defined on the set of coefficients ti . In particular, every a ∈ A+ has a square root
√
P 1/2
a = i λi pi also in A+ .
L
Decomposing A as an orthogonal direct sum A = i Ai of simple Jordan ideals Ai ,
the Jordan unit uA is the sum of the Jordan units uAi of these ideals. It follows that each
Jordan frame E of A is the disjoint union of Jordan frames Ei belonging to the various
simple ideals Ai . If A is simple, the group of Jordan automorphisms acts transitively
on the set of Jordan frames ([26], Theorem IV.2.5). It follows that all Jordan frames for
a given euclidean Jordan algebra A have the same number of elements. This number is
called the rank of A. By the Classification Theorem, all simple Jordan algebras having
rank 4 or higher are special.

· ·

3.2 Euclidean Jordan algebras as probabilistic models
As remarked earlier, any euclidean Jordan algebra A can be regarded as an ordered real
vector space, with positive cone A+ = {a2 |a ∈ A}. (That this is a cone is a non-trivial
fact (see [26], Theorem III.2.1, or [3], pp. 36-28).) By the spectral theorem, a = b2 for
P
some b ∈ A iff a has a spectral decomposition a = i λi xi in which all the coefficients
λi are non-negative. It can also be shown (see [26], Proposition I.1.4) that a belongs
to the interior of A+ iff ha, bi > 0 for all nonzero b ∈ A+ . Using this, it follows that a
P
belongs to the interior of A+ iff it has a spectral decomposition a = x∈E tx x with
√ all
coefficients tx strictly positive. Hence, if a belongs to the interior of A+ , so does a.
The Jordan unit u is also an order unit. Thus, any EJA can serve as a probabilistic
10

In fact the converse is also true, cf. Ch. II Exercise 3 or Ch. III Exercise 7 in [26].

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

13

<!-- page 14 -->
model, as defined in Section 2: physical states correspond to states qua normalized
positive linear functionals on A, while measurement outcomes are represented by effects,
i.e, elements a ∈ A+ with 0 ≤ a ≤ u, and (discrete) observables, by sets {ei } of events
P
L
with i ei = u. Note that if A = ni=1 Ai where each Ai is a copy of the one-dimensional
Jordan algebra R, then A ≃ Rn , regarded as a commutative algebra (in particular,
a b = ab). As a probabilistic system, this is classical, in the sense that it is simply the
space of random variables on a finite sample space. From now on, when we speak of a
classical system, this is what we have in mind.
As discussed earlier, the inner product on A allows us to represent states internally,
i.e., for every state α there exists a unique a ∈ A+ with α(x) = ha|xi for all x ∈ A;
conversely, every vector a ∈ A+ with ha|ui = 1 defines a state in this way. Now, if a is
a projection, i.e., a2 = a, let ab = kak−2 a: then

·

hab|uA i =

1
1
1
ha|uA i =
ha2 |uA i =
ha|ai = 1.
2
2
kak
kak
kak2

Thus, ab represents a state. A similar computation shows that hab|ai = 1. Thus, every
projection, regarded as an effect, has probability 1 in some state.
Lemma 3.1. Let A be an EJA, and let a be an effect, i.e. a ∈ [0, uA ] ⊆ A+ . Then a
is a projection iff huA , ai = ha, ai.

·

·

Proof: If a is a projection, then ha, ai = huA a, ai = huA , a ai = huA , ai. Conversely,
P
suppose huA , ai = ha, ai. Let a have spectral decomposition a = x∈E tx x where E is a
P
P
Jordan frame. We then have huA , ai = x∈E tx kxk2 , while ha, ai = x∈E t2x kxk2 . Since
a is an effect, 0 ≤ tx ≤ 1 for every x ∈ E, so that t2x kxk2 < tx kxk2 unless tx = 0 or
tx = 1. In order for the two sums above to be equal, therefore, we must have that tx = 0
P
or tx = 1 for every x. Setting B = {x ∈ E|tx > 0}, we have a = x∈B x, a projection. 
When A is special, i.e., a Jordan subalgebra of a matrix algebra, its order structure
is inherited from that of the latter.
Proposition 3.2. Let A ≤ Msa , i.e., A is a Jordan subalgebra of a finite-dimensional
complex matrix algebra M. Then A+ = A ∩ M+ .
Proof: A+ ⊆ M+ because squares in A are squares in M+ . For the converse, let
P
a ∈ A ∩ M+ . By the spectral theorem for EJAs, we can express a as a sum a = i λi ei
where the ei are pairwise Jordan-orthogonal idempotents, i.e, ei ej = 0 for i 6= j.
Jordan-orthogonal idempotents in A are again Jordan-orthogonal idempotents in Msa .
Since Jordan-orthogonal idempotents in Msa are orthogonal in the usual sense and
a ∈ M+ , it follows that the coefficients λi are all non-negative, whence, a ∈ A+ . 

·

Order-automorphisms The order structure of an EJA A, together with its inner
product and order unit, entirely determines its Jordan structure, as a consequence of the
Koecher-Vinberg theorem [45, 62] (discussed in more detail below). One manifestation
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

14

<!-- page 15 -->
of this is that a symmetry of A — that is, an order-automorphism preserving the unit
uA — is the same thing as a Jordan automorphism ([4], Theorem 2.80).
Another class of order automorphisms is given by the quadratic representations of
certain elements of A. The quadratic representation of a ∈ A is the mapping Ua : A → A
given by
Ua = 2L2a − La2

··

··

i.e., Ua (x) = 2a (a x)−(a a) x. These mappings have direct physical interpretations
as filters in the sense of [66]. The following non-trivial facts will be used repeatedly in
what follows:
Proposition 3.3. Let a ∈ A. Then
(a) Ua is a positive mapping;
(b) If a lies in the interior of A+ , Ua is invertible, with inverse given by Ua−1 ;
(c) eLa = Uea/2
Proof: For (a), see Theorem 1.25 of [4]; for (b), [4] Lemma 1.23 or [26], Proposition
II.3.1. Part (c) is Proposition II.3.4 in [26]. 
Combining (a) and (b), Ua is an order automorphism for every a in the interior of A+ .
Regarding (c), note that eLa is the ordinary operator exponential. Therefore if a is in the
interior of A+ , then φt := etLa = U 2t a is a one-parameter group of order-automorphisms
with φ0 (0) = La . Therefore, for all a in the interior of A+ , Ua is in the connected
component Aut0 (A) of the identity in the group Aut(A) of order-automorphisms of A.
Notice
that Ua (uA ) = 2a2 − a2 = a2 If a belongs to the interior of A+ , then so
√
does a; thus, by the remarks above, U√a ∈ Aut0 (A) and U√a (uA ) = a. It follows
that Aut0 (A), and hence also the full group Aut(A) of order-automorphisms of A, act
transitively on the interior of A+ : if a, b belong to the interior of A+ , then U√b ◦ U√−1a
maps a to b. In other words, A+ is homogeneous.
EJAs as dynamical models Henceforth, we will write G(A) for the identity component Aut0 (A) of an EJA A. As this notation suggests, we henceforth regard an
EJA A as a dynamical probabilistic model with G(A) as its dynamical group. This
is a reasonable choice. First, elements of G(A) are exactly those automorphisms of
A+ that figure in the system’s possible dynamics, as elements of one-parameter groups
of automorphisms. This suggests that the “physical” dynamical group of a dynamical
model based on A should at least be a subgroup of G(A), so that the latter is the least
constrained choice. Moreover, G(A), like the full group of order-automorphisms, acts
transitively on the interior of the cone A+ , and its unit-preserving subgroup acts transitively on the set of Jordan frames, i.e., maximally informative sharp observables —
or, equivalently, on maximal lists (α1 , ..., αn ) of sharply-distinguishable states. These
transitivity properties, abstracted from the Jordan-algebraic setting, were among the
postulates used (in somewhat different ways) in [63, 64] and [15] to derive the Jordan
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

15

<!-- page 16 -->
structure of probabilistic models, so it is not unreasonable to require that the dynamical
group enjoy them.
If φ is any order-automorphism with φ(uA ) = a2 ∈ A+ , then Ua−1 ◦ φ is a symmetry
of A. Hence, every order-automorphism of A decomposes as φ = Ua ◦ g where g is a
symmetry. As we observed earlier, a can be chosen to belong to the interior of A+ ; it
can be shown that with this choice, the decomposition is unique ([26], III.5.1)
The Koecher-Vinberg Theorem As we have seen, the positive cone A+ of an EJA
is homogeneous, and also self-dual with respect to A’s inner product.
Conversely,
let A be an homogenous finite-dimensional ordered vector space with a self-dualizing
inner product. Choosing any order-unit u invariant under positive orthogonal transformations, there exists a unique bilinear product on A making A, with the given inner
product, a euclidean Jordan algebra, and the chosen element u, the Jordan unit. This
is the content of the Koecher-Vinberg Theorem ([45, 62]; see also [26, 56]). While we
make no use of this result here, it is at the center of efforts to provide an operational
motivation for euclidean Jordan algebras as models of physical systems, e.g., in [66, 15].

3.3 Representations of EJAs
A representation of a Jordan algebra A is a Jordan homomorphism π : A → Mn (C)sa
for some n.11 So a Jordan algebra is special iff it has an injective, or faithful, representation. Recall that every EJA decomposes as a direct sum A = Asp ⊕ Aex , where
Asp is special and Aex has no nontrivial representations. The latter, in turn, is a direct
sum of copies of the exceptional EJA M3 (O)sa . See [4], Theorem 4.3 for details.
Standard Representations For the non-exceptional simple EJAs, it will be useful
to record what we will call their standard representations. It will also prove helpful to
adopt the following abbreviations:
Rn = Mn (R)sa ; Cn = Mn (C)sa , Qn = Mn (H)sa .
As above, we write Vn for the spin factor R × Rn . With this notation we have obvious
embeddings Rn ≤ Cn = Mn (C)sa . For Qn , note that a quaternion a + bi + cj + dk can
be written as (a + bi) + (c + di)j, and so, can be represented by the pair of complex
numbers (a + bi, c + di). Thus, any n × n matrix of quaternions can be represented as
a 2n × 2n complex matrix having the form
!

Γ1 Γ2
,
−Γ2 Γ1

(1)

where the blocks Γ1 and Γ2 are n × n complex matrices. This gives us a faithful
representation of Qn in M2n (C), known as the symplectic representation [28]. There
11

This is a finite dimensional, concrete representation. For the finite-dimensional algebras we are
concerned with, this definition suffices.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

16

<!-- page 17 -->
is also what we will call a standard representation of Vn in M2k (C), where n = 2k or
2k + 1. This is less obvious; the details are given in Appendix C.
Involutions and Reversibility By an involution on a complex ∗-algebra M , we mean
a ∗-anti-automorphism of M of period 2 — in more detail, a linear mapping Φ : M → M
such that Φ(a∗ ) = Φ(a)∗ , Φ(ab) = Φ(b)Φ(a), and Φ(Φ(a)) = a for all a ∈ M . A real
involution is defined similarly, except that the mapping is only required to be realΦ
= {a ∈ M |a = a∗ = Φ(a)} of all selflinear.12 It is straightforward that the set Msa
φ
adjoint fixed-points of M under Φ is a Jordan subalgebra of Msa . Indeed, if a, b ∈ Msa
,
1
then a b = 2 (ab + ba) ∈ Msa , and

·

Φ(ab + ba) = Φ(b)Φ(a) + Φ(a)Φ(b) = ba + ab = ab + ba

·

Φ
Φ
so that a b ∈ Msa
as well. In fact, more is true: if a1 , ..., an ∈ Msa
, then

Φ(a1 · · · an + an · · · a1 ) = an · · · a1 + a1 · · · an
Φ
so that a1 · · · an + an · · · a1 ∈ Msa
.

Definition 3.4. A Jordan subalgebra A of Msa is said to be reversible if a1 , ..., an ∈
A =⇒ a1 · · · an + an · · · a1 ∈ A. An abstract EJA A is reversible iff it has a faithful
(that is, injective) representation as a reversible Jordan subalgebra of some ∗-algebra
M . If all of A’s faithful representations are reversible, then A is said to be universally
reversible (hereafter: UR). 13
Φ
In this language, then, all Jordan algebras of the form Msa
are reversible. All selfadjoint parts of real and complex matrix algebras are universally reversible, as are the
quaternionic ones of rank 3 and higher (whence, all EJAs of rank ≥ 4 are UR). The
quaternionic bit M2 (H)sa , which is isomorphic to V5 , is not universally reversible, but
it is reversible, since its standard embedding into M4 (C) is reversible: indeed, it’s the
set fixed points of the involution Φ(x) = (σy ⊗ 12 )xT (σy ⊗ 12 ) where σy = −σy is the
usual Pauli y-matrix. Spin factors Vn with n = 4 or n ≥ 6 are not reversible at all. For
details, see [30]. Thus, the reversible simple EJAs are just those of the forms Mn (R)sa ,
Mn (C)sa and Mn (H)sa .

The universal representation In addition to the standard representations discussed
above, every special EJA has a universal representation.
Definition 3.5. A universal C ∗ algebra for a euclidean Jordan algebra A is a complex
∗-algebra C ∗ (A), plus a Jordan homomorphism ψA : A → C ∗ (A)sa , such that for any
C ∗ -algebra M and any Jordan homomorphism φ : A → Msa , there exists a unique
∗-homomorphism φb : C ∗ (A) → M with φ = φb ◦ ψA .
12

Our usage is slightly nonstandard here: an involution on a complex ∗-algebra is more frequently
defined to be a conjugate-linear. The only involution in this sense that will concern us is a 7→ a∗ .
13

Some authors, for example Hanche-Olsen in [30], define universal reversibility as reversibility in all
representations, not just all faithful representations. The two definitions are equivalent, as will become
apparent below.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

17

<!-- page 18 -->
Note that the uniqueneness of the ∗-homomorphism φb : C ∗ (A) → M is equivalent
to C ∗ (A) being generated by ψA (A) as a C ∗ algebra, which is how the definition is more
usually presented. For the existence of C ∗ (A), see [4] or [31]. Universal C ∗ -algebras
for a given EJA A are unique up to canonical ∗-isomorphism, warranting our speaking
of “the” universal C ∗ -algebra of A.14 It is easy to see that any Jordan homorphism
A → B lifts, via ψA and ψB , to a C ∗ -homomorphism C ∗ (A) → C ∗ (B), and that this
lifting respects composition of Jordan homomorphisms, so that C ∗ ( · ) defines a functor
from the category of EJAs to the category of complex ∗-algebras. It can be shown that
this functor is exact ([30], Theorem 4.1). It is an important fact that A is exceptional
iff C ∗ (A) = {0}. Otherwise, the representation ψA of A in C ∗ (A) is faithful, and takes
the unit of A to the unit of C ∗ (A). In this case, we will often identify A with its image
ψA (A) in C ∗ (A), referring to this (and to the homomorphism ψA ) as the universal
embedding of A.
We can now see that reversibility in all faithful representations implies reversibility
in all representations. It is straightforward that any representation factoring through
a reversible representation is also reversible. If A is universally reversible in the sense
of Definition 3.4, then the universal representation, which is faithful, is also reversible.
Since every representation factors through this one, every representation of A is reversible.
The canonical involution If A is special, C ∗ (A) comes equipped with a unique involution that fixes every point of A. To see this, note that that the opposite algebra
C ∗ (A)op (the same vector space, equipped with reversed multiplication) is equally a universal C ∗ -algebra for A. Hence, there is a unique ∗-isomorphism ΦA : C ∗ (A)op → C ∗ (A)
fixing all points of A. We can equally well regard Φ as a ∗-antiautomorphism of C ∗ (A);
so regarded, Φ is self-inverse, hence an involution.
Definition 3.6. We call the involution Φ : C ∗ (A) → C ∗ (A) just described, the canonical
involution, ΦA , on C ∗ (A).
As discussed above, the self-adjoint fixed-points of an involution Φ on a complex
Φ
∗-algebra M constitute a Jordan subalgebra, Msa
, of Msa . With ΦA the canonical
involution on C ∗ (A)sa , we have a Jordan embedding A ≤ C ∗ (A)Φ
sa .
Proposition 3.7 ([30], Lemma 4.2 and Theorem 4.4). With notation as above, A is
UR iff A = C ∗ (A)Φ
sa . More generally, if A is UR and there exist an embedding A ≤ Msa
for a complex ∗-algebra M , and an involution Φ on M fixing points of A, then the
∗-subalgebra of M generated by A is isomorphic to C ∗ (A) and Φ, restricted to this
subalgebra, is the canonical involution.
This characterization allows the explicit computation of universal C ∗ -algebras of UR
EJAs [30]. For instance, Rn = Mn (R)sa generates Mn (C)sa as a (complex) ∗-algebra,
14

In fact, by privileging any particular construction of C ∗ (A), we can take this literally.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

18

<!-- page 19 -->
in which it sits as the set of symmetric self-adjoint matrices: in other words, the set of
fixed points of the involution Φ(a) = aT . Thus, C ∗ (Rn ) = Mn (C). Similarly, the image
of Mn (H)sa under the standard (symplectic) embedding into M2n (C) = M2 (Mn (C)) is
fixed by the involution Φ(a) = −JaT J where J is the block matrix
!

0 1
J=
−1 0

(2)

with 1 the n × n identity matrix. For a third example, consider the embedding
Mn (C)sa → (Mn (C) ⊕ Mn (C))sa given by ψ(a) = (a, aT ): the image of this embedding generates Mn (C) ⊕ Mn (C) as a ∗-algebra, and is exactly the set of fixed-points of
the involution Φ(a, b) = (bT , aT ). Thus, C ∗ (Cn ) = Mn (C) ⊕ Mn (C). Note, in passing,
that this also shows that there is no involution on Mn (C) fixing points of Cn = Mn (C)sa .
(Otherwise, Mn (C) would be the universal ∗-algebra for Cn .)
The universal C ∗ -algebras for all simple, non-exceptional EJAs are are summarized
in Table 1 below, along with the canonical involutions in the UR cases. For a spin factor
Vn , the universal C ∗ -algebra is the complex Clifford algebra CliffC (n) on n generators
[30]; these are tabulated separately in Table 1(b).
For contrast, Table 1(c) lists the complex matrix algebras into which Rn , Cn and Qn
are standardly embedded. We also list in Fig. 1 (c) algebras supporting what we are
calling standard embeddings of the spin factors Vn ; these agree with the universal ones
for n = 2k, but for n = 2k + 1, embed Vn in M2k (C) rather than the M2k (C) ⊕ M2k (C)
of the universal embedding. Thus, all the targets of embeddings in Fig. 1(c) are simple
complex matrix algebras.
A
Rn
Cn
Qn
Vn

C ∗ (A)
Mn (C)
Mn (C) ⊕ Mn (C)
M2n (C) if n > 2
CliffC (n)

Φ
a 7→ aT
(a, b) 7→ (bT , aT )
a 7→ −JaT J

n (k ∈ N+ ) CliffC (n)
2k
M2k (C)
2k + 1
M2k (C) ⊕ M2k (C)

(a)
Universal embeddings

(b)
Clifford algebras

M
Mn (C)
Mn (C)
M2n (C)
M2k (C)
M2k (C)
(c)
Standard embeddings
A
Rn
Cn
Qn
V2k
V2k+1

Table 1: Universal and standard embeddings
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

19

<!-- page 20 -->
Note that the spin factors V2 , V3 , V5 correspond to the three types of quantum bits:
V2 ≃ R2 ; V2 ≃ C2 and V5 ≃ Q2 . This last, together with line 2 of Fig. 1 table (b), gives
us the missing item in table (a):
C ∗ (Q2 ) ≃ M4 (C) ⊕ M4 (C).
It will be helpful to record here two further facts about universal C ∗ algebras. First,
C ∗ (A ⊕ B) = C ∗ (A) ⊕ C ∗ (B). This follows from the exactness of the C ∗ ( )-functor.
Combining this with Proposition 3.7, it follows that if A and B are both UR, so is
A ⊕ B. Details can be found in Appendix A.

3.4 The universal tensor product
The universal representation allows one to define a natural tensor product of EJAs,
first studied by H. Hanche-Olsen [30]:
e
Definition 3.8. The universal tensor product of two EJAs A and B, denoted A⊗B,
is
∗
∗
∗
∗
the Jordan subalgebra of C (A) ⊗ C (B) (the tensor product of C (A) and C (B) as
finite-dimensional ∗-algebras) generated by ψA (A) ⊗ ψB (B).
e ≃ A. Other examples are discussed below.
Since C ∗ (R) = C, trivially we have R⊗A
Some important general facts about the universal tensor product are collected in the
following:

Proposition 3.9. Let A, B and C denote EJAs.
(a) If φ : A → C, ψ : B → C are unital Jordan homomorphisms with operatorcommuting ranges, then there exists a unique Jordan homomorphism A e
⊗B → C
taking a ⊗ b to φ(a) ψ(b) for all a ∈ A, b ∈ B.

·

e
(b) C ∗ (A⊗B)
= C ∗ (A) ⊗ C ∗ (B) and ΦA e
⊗B = ΦA ⊗ ΦB .
e
(c) A⊗B
is universally reversible unless one of the factors has a one-dimensional
summand and the other has a representation onto a spin factor Vn with n = 4 or
n ≥ 6.

(d) If A is universally reversible, then A e
⊗Mn (C)sa = (C ∗ (A) ⊗ Mn (C))sa .
(e) uA⊗
e B = uA ⊗ uB = uC ∗ (A⊗
e B) .
Proof: (a), (c), and (d) are Propositions 5.2, 5.3 and 5.4, respectively, in [30]; (b) is
observed in the vicinity of these propositions in [30], while (e) follows easily from the
fact that ψ A (uA ) = uC ∗ (A) . 
Table 1 (c) shows that if A and B are simple and nontrivial, A e
⊗B will always be UR,
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

20

<!-- page 21 -->
and hence, by Proposition 3.7 and Proposition 3.9 (b), the fixed-point set of ΦA ⊗ ΦB .
Using this, one can compute A e
⊗B for simple A and B (with n, k > 2 in the case of Qn
and Qk ) [30]:
e
Rk
Ck
Qk
⊗
Rn Rnk
Cnk
Qnk
Cn Cnk Cnk ⊕ Cnk C2nk
C2nk
R4nk
Qn Qnk

Table 2: Universal tensor products of simple UR EJAs
For Q2 e
⊗Q2 , we obtain the direct sum of four copies of R16 = M16 (R)sa . The details
can be found in [27].
In the next two sections, we are going to explore in some detail the possibilities for
forming dynamical composites, in the sense of our Definition 2.1, of Jordan-algebraic
e
systems. As will emerge, the universal tensor product A⊗B
is such a composite of A
and B, though not the only one. In this connection, notice that A e
⊗B is in general a
e is not
larger vector space than A ⊗ B. In other words, as a composite of A and B, A⊗B
necessarily locally tomographic. Indeed, this will typically be the case for composites
of EJAs, as underlined by the following finite-dimensional case of a result of HancheOlsen (valid more generally for JC algebras), which was used in [17] to show that
the only EJAs having locally tomographic composites with a qubit are the complex
quantum systems (those whose Jordan algebras are the self-adjoint parts of complex
matrix algebras):
Proposition 3.10 ([30], Theorem 5.5). Let A be an EJA, and suppose that the vectorspace tensor product A ⊗ M2 (C) is a Jordan algebra with respect to a bilinear product
such that

·

(i) (uA ⊗ b)2 = uA ⊗ b2 and (a ⊗ 1)2 = a2 ⊗ 1,

·

(ii) (a ⊗ 1) (uA ⊗ b) = a ⊗ b,
(iii) a ⊗ 1 and uA ⊗ b operator commute for all a ∈ A and b ∈ M2 (C),
where 1 is the identity in M2 (C). Then A is the self-adjoint part of a complex matrix
algebra.

4 Composites of Jordan-Algebraic Systems
As discussed in section 3.2, we can regard an EJA A as a dynamical probabilistic
model with dynamical group G(A). If A and B are EJAs, thus regarded as models of
probabilistic physical systems, we would like to know what possibilities exist for forming
a Jordan-algebraic dynamical composite AB. We shall actually impose a further, but
we think natural, condition on such composites, namely condition (b) in the definition
below:
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

21

<!-- page 22 -->
Definition 4.1. A composite of EJAs A and B is an EJA AB, plus a bilinear mapping
π : A ⊗ B → AB, such that
(a) π makes (AB, G(AB)) a dynamical composite of (A, G(A)) and (B, G(B)), in the
sense of Definition 2.3,
(b) (φ ⊗ ψ)† = φ† ⊗ ψ † for all φ, ψ ∈ G(A), and
(c) AB is generated, as a Jordan algebra, by (images of) pure tensors.
By Lemma 2.2, the mapping π : A ⊗ B → AB is injective; hence, we can, and shall,
identify A ⊗ B with its image in AB, writing π(a, b) as a ⊗ b.
Condition (b) is rather strong, but natural if we keep in mind that our ultimate aim
is to construct dagger-compact categories of EJAs. Regarding condition (c), suppose
π : A × B → AB satisfied only (a) and (b): letting A B denote the Jordan subalgebra
of AB generated by π(A ⊗ B), one can show (Appendix D) that the co-restriction of π
to A B also satisfies (a) and (b); thus, any composite in the weaker sense defined by
(a) and (b) contains a composite satisfying all three conditions.
e
In Section 5, Proposition 5.4, we will show that A⊗B
is a composite in the sense
of Definition 4.1. The main result of the present section is to show that any such
e
composite AB is a direct summand of A⊗B.
In view of Table 2, this severely limits
the possibilities for AB.

4.1 The identity (a ⊗ u) • (x ⊗ y) = (a • x) ⊗ y.
At this point, we have limited information about how the Jordan structure of a composite AB interacts with the Jordan structures of A and B. However, we shall now
establish, for any a ∈ A and any x, y ∈ B, the identity (a ⊗ u) (x ⊗ y) = (a x) ⊗ y —
in other words, that La⊗uB acts on A ⊗ B ≤ AB as La ⊗ 1B , where 1B is the identity
operator on B.

·

·

One-parameter groups and exponentials It will be helpful first to recall some basic facts about operator exponentials, or, equivalently, one-parameter groups of linear
operators on finite-dimensional spaces (see, e.g., [22]). Let V be a finite-dimensional
real vector space, and X, a linear operator on V . Recall that φ(t) := etX is the unique
function R → L(V ) satisfying the initial-value problem
φ0 (t) = Xφ(t); φ(0) = 1
(where 1 is the identity operator on V ). In particular, φ0 (0) = X. The function φ
satisfies φ(t + s) = φ(t)φ(s) and hence, φ(t)φ(−t) = φ(0) = 1, hence, as φ(0) = 1, φ(t)
is invertible, with φ(t)−1 = φ(−t). In other words, φ is a one-parameter group of linear
operators on V . Conversely, if φ : R → L(V ) is any continuous one-parameter group of

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

22

<!-- page 23 -->
linear operators on V , then φ is differentiable, and φ(t) = etX where X = φ0 (0). Notice,
also, that in such a case we have
Xa =

d
φ(t)a|t=0
dt

for any vector a ∈ V .
For later reference, the following lemma collects some standard facts:
Lemma 4.2. Let X, Y be linear operators on a finite-dimensional inner product space
V . Then
(a) X commutes with etX for all t;
(b) If etX commutes with esY for all t, s, then X commutes with Y ;
†

(c) (etX )† = etX .
Note that, by (c), if φ(t) is a one-parameter group with φ0 (0) = X hermitian, then
φ(t) is hermitian for all t, and conversely.
Now let A be an EJA. For a ∈ A, define
φa (t) := etLa = eLta ,
i.e., φa is the solution to the initial-value problem dtd φa = La φa , φa (0) = 1. By part
(c) of Proposition 3.3, φa (t) = Ueta/2 ; by part (b) of the same Proposition, this last
is a positive mapping. Since etLa is invertible with inverse e−tLa = eL−ta , φa (t) is an
order-automorphism belonging to G(A). It follows that La belongs to gA , the Lie group
of the identity component G(A) of A. Note that hLa x, yi = hax, yi = hx, ayi = hx, La yi
for all x, y ∈ A; that is, La is self-adjoint. One can show that, conversely, a self-adjoint
element of gA has the form La for a unique a ∈ A. (See [26], pp. 6 and 49, for the
details.)
We are now ready for the main result of this sub-section.
Proposition 4.3. Let AB be a composite (in the sense of Definition 4.1) of Jordan
algebras A and B. Then the mapping a 7→ a ⊗ uB is a Jordan homomorphism from A
into AB. That is, for all a, x ∈ A and b, y ∈ B,

·

·

·

·

(a ⊗ uB ) (x ⊗ y) = (a x) ⊗ y and (uA ⊗ b) (x ⊗ y) = x ⊗ (b y)

(3)

We shall refer to (1) as the fundamental identity.
Proof: We prove the first identity; the second is handled similarly. Let φ(t) be a oneparameter group of order automorphisms of A with φ0 (0) = La , that is, φ(t) = etLa .

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

23

<!-- page 24 -->
Then ψ(t) := φ(t) ⊗ 1 is a one-parameter group of automorphisms on AB, by condition
(b) of Definition 2.3. Let Y = ψ 0 (0)∈ gAB ; then, for all x ∈ A and y ∈ B,
d
ψ(t)
(x ⊗ y)
dt
t=0

"

d
(ψ(t)(x ⊗ y))
dt
t=0

"

d
(φ(t)x ⊗ y)
dt
t=0

Y (x ⊗ y) =
=
=

#

"

#

#

"

=

#

!

d
φ(t)
x ⊗ y = La x ⊗ y = ax ⊗ y.
dt
t=0

Using condition (b) of Definition 4.1, the hermiticity of φ0 (0) = La , and the consequent
hermiticity of φ(t) (see the discussion following Lemma 4.2), we have
(φa (t) ⊗ 1)† = φa (t)† ⊗ 1 = φa (t) ⊗ 1.
Hence, Y is self-adjoint. As discussed above, it follows that there exists some v ∈ AB
with Y = Lv on A ⊗ B. Thus,

·

·

v (x ⊗ y) = Lv (x ⊗ y) = Y (x ⊗ y) = (a x) ⊗ y.

·

·

·

Setting x = uA and y = uB , we have v = v uAB = v (uA ⊗uB ) = (a uA )⊗uB = a⊗uB ,
which gives the advertised result. 
One immediate consequence of the fundamental identity (1) is that, for any composite
AB of EJAs, A ⊗ uB = {a ⊗ uB |a ∈ A} is a Jordan subalgebra of AB isomorphic to A.
In particular, since A⊗R = A⊗1, any composite of an EJA A with the one-dimensional
Jordan algebra R is canonically isomorphic to A.
The fundamental identity can be read as asserting that La ⊗ idB and idA ⊗ Lb act
on A ⊗ B ≤ AB in the expected way for all a ∈ A, b ∈ B. Recalling that, for a ∈ A,
the mapping Ua : A → A is defined by Ua = 2L2a − La2 , we have the
Corollary 4.4. In any composite AB of EJAs A and B, and for any a ∈ A, b ∈ B,
Ua⊗uB and UuA ⊗b act on A ⊗ B as Ua ⊗ idB and idA ⊗ Ub , respectively.
Another, very important, consequence of Proposition 4.3 is the following:
Proposition 4.5. Let p ∈ A and q ∈ B be projections. Then p ⊗ q is a projection in
AB, for any composite AB of A and B.
Proof: By Lemma 3.1, if A is an EJA, an effect a ∈ A+ is a projection iff huA |ai =
ha|ai. Certainly, p ⊗ q is an effect in AB+ . Now note that, by repeated application of

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

24

<!-- page 25 -->
Proposition 4.3, plus the fact that uA ⊗ uB = uAB and the associativity of the inner
product, we have
huA ⊗ uB , p ⊗ qi =
=
=
=
=
=
=
=

·
·
·
·
·
·

huA ⊗ uB , p p ⊗ qi
huA ⊗ uB , (p ⊗ uB ) (p ⊗ q)i
h(uA ⊗ uB ) (p ⊗ uB ), p ⊗ qi
hp ⊗ uB , p ⊗ qi
hp ⊗ uB , p ⊗ q qi
hp ⊗ uB , (uA ⊗ q) (p ⊗ q)i
h(p ⊗ uB ) (uA ⊗ q), p ⊗ qi
hp ⊗ q, p ⊗ qi.

It follows that p ⊗ q is a projection. 
Corollary 4.6. Let p, q be Jordan-orthogonal projections in A. In any composite AB,
and for any b ∈ B+ , p ⊗ b and q ⊗ b are Jordan-orthogonal.
Proof: Since ⊗ : A × B → AB is a positive bilinear map, we have for all a1 , a2 ∈ A
and all b ∈ B that a1 ≤ a2 ⇒ a1 ⊗ b ≤ a2 ⊗ b (since a2 ⊗ b − a1 ⊗ b = (a2 − a1 ) ⊗ b
is positive). Now suppose b is an effect in B and that p and q are Jordan orthogonal
projections in A, so that p + q ≤ uA . It’s enough to show that p ⊗ b + q ⊗ b ≤ uAB . But
p⊗b+q⊗b = (p+q)⊗b, and p+q ≤ uB , so we have (p+q)⊗b ≤ uA ⊗b ≤ uA ⊗uB = uAB .
Since the result holds for arbitrary effects b, it holds for arbitrary elements b ∈ B. 
Proposition 4.7. For all a ∈ A, b ∈ B, a ⊗ uB and uA ⊗ b operator commute in AB.
Note that this would follow trivially from Proposition 4.3 if AB were spanned by
pure tensors, that is, if AB is locally tomographic.
Proof: Suppose p ∈ A and q ∈ B are projections, and let p0 = uA − p and q 0 = uB − q.
Then we have
uAB = uA ⊗ uB = (p + p0 ) ⊗ (q + q 0 ) = p ⊗ q + p0 ⊗ q + p ⊗ q 0 + p0 ⊗ q 0 .
By Proposition 4.5, the four terms on the right are projections. They are mutually
orthogonal by Corollary 4.6, and sum to the unit in AB. Hence, p⊗uB = p⊗q+p⊗q 0 and
uA ⊗ q = p ⊗ q + p0 ⊗ q operator commute by [4], Lemma 1.48. Now let a ∈ A and b ∈ B
P
P
be arbitrary: by the spectral theorem for EJAs, we have a = i ti pi and b = j sj qj
for pairwise orthogonal families of projections pi and qj and scalars ti and sj . Since
P
pi ⊗ uB and uA ⊗ qj operator commute for all i, j, it follows that a ⊗ uB = i ti pi ⊗ uB
P
and uA ⊗ b = j sj uA ⊗ qj also operator commute. 

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

25

<!-- page 26 -->
4.2 Composites of Direct Sums
Let A ≃ A0 ⊕ A1 . Then there is a natural homomorphism G(A0 ) → G(A) given by
φ 7→ φ ⊕ idA1 (where (φ ⊕ idA1 )(A0 , a1 ) = (φ(A0 ), a1 )). If AB is a dynamical composite
of A and B, then let A0 B = J(π(A0 × B)), the Jordan subalgebra of AB generated
by pure tensors A0 ⊗ b with A0 ∈ A0 (equipped with the inner product inherited from
AB). Note that we have a natural positive bilinear map π0 : A0 × B → A0 B, obtained
by restricting and co-restricting π : A × B → AB to A0 × B and A0 B.
The following two results, taken together, will be very helpful below
Proposition 4.8. A0 B is a composite of A0 and B.
Proof: We check the requirements of Definition 4.1. First, note that u0 ⊗uB is effective as
the unit in A0 B. For all a ∈ A0 and b ∈ B, we have (u0 ⊗uB ) (a⊗b) = (u0 a)⊗b = a⊗b
by the fundamental identity and the fact that u0 is the unit in A0 . Since this holds on
all pure tensors in π(A0 × B), it holds throughout A0 B.
A normalized state α on A0 extends in a canonical way to a normalized state α
on A = A0 ⊕ A1 , given by α(A0 , a1 ) = α(A0 ). Thus, if β is a normalized state on B,
condition (c) in Definition 2.1 tells us that there is a normalized state γ on AB with
γ(a, b) = α(a)β(b) for all a ∈ A and b ∈ B. Restricting γ to A0 B gives us a positive
functional γ0 with γ0 (A0 ⊗ b) = α(A0 )β(b) for all A0 ∈ A0 and b ∈ B. In particular,
γ0 (u0 ⊗ uB ) = α(u0 )β(uB ) = 1, so γ0 is a normalized state on A0 B.
Embedding G(A0 ) in G(A) in the obvious way (that is, g ∈ G(A0 ) acts on (A0 , a1 )
as (gA0 , a1 )), we have a homomorphism ⊗0 : G(A0 ) × G(B) → G(A0 B) obtained by
restricting the domain of the given homomorphism ⊗ : G(A)×G(B) → G(AB). For any
h ∈ G(B) and any A0 ∈ A, b ∈ B we have (g ⊗h)(A0 ⊗b) = gA0 ⊗hb. Since this last lies
in π(A0 ×B), g⊗h fixes A0 B. Thus, we have a natural homomorphism G(A0 )×G(B) →
G(A0 B) satisfying the requirements for a dynamical composite. Finally, note that
(g ⊗ h)† = g † ⊗ h† since this holds at the level of AB. 

·

·

Recall that the center of an EJA A is the set of all elements in A that operator
commute with each element of A. Such elements are called central. A central projection
is thus a projection p ∈ A such that Lp ◦ La = La ◦ Lp for all a ∈ A.
Proposition 4.9. Let AB be any composite of EJAs A and B. If A = i Ai and
L
B = j Bj where Ai = ci A and Bj = dj B for mutually Jordan orthogonal families
L
of central projections ci in A and dj in B, then AB = i,j Ai Bj .

·

L

·

·

·

Proof: It is enough to prove this for the case in which A = c A ⊕ c0 A for a central
idempotent c, where c0 = uA −c. By ([4], Lemma 1.43), if p is any idempotent in an EJA
A, then Up (A) is a Jordan subalgebra of A. Moreover, if p and q are Jordan-orthogonal
idempotents, then Up (A) is Jordan-orthogonal to Up (B), by ([4], Lemma 1.45). Now
let c be a central projection in A, and write Ac for c A. Then c ⊗ uB is an idempotent
in AB, and Corollary 4.4 gives us

·

·

x ⊗ y = (c x) ⊗ y = Uc (x) ⊗ y = Uc⊗y (x ⊗ y) ∈ Uc⊗y (AB).
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

26

<!-- page 27 -->
for all x ∈ Ac and y ∈ B. As pure tensors x ⊗ y with x ∈ Ac and y ∈ B generate Ac B,
we now have Ac B ≤ Uc⊗idB (AB). By the same token Ac0 B ≤ Uc0 ⊗idB (AB). As noted
above, the two larger subalgebras are pairwise Jordan-orthogonal; hence, so are the two
smaller ones. In particular, the (internal) direct sum Ac B ⊕Ac0 B exists, and is a Jordan
subalgebra, of AB. Every pure tensor in A⊗B has the form (x1 +x2 )⊗y = x1 ⊗y+x2 ⊗y,
where x1 ∈ Ac and x2 ∈ Ac0 , and hence, belongs to Ac B ⊗Ac0 B. Since such pure tensors
generate AB as a Jordan algebra, we have AB = Ac B ⊕ Ac0 B. The general case now
follows by an easy induction. 
Corollary 4.10. Let c be a projection in an EJA A, and let AB be a composite of A
with an EJA B. Then c ⊗ uB is central in AB if c is central in A.

4.3 Composites of simple EJAs
We now show that if A and B are nontrivial simple EJAs, then any composite AB
must be special, universally reversible, and an ideal (a direct summand) of the universal
e
tensor product A⊗B.
It follows that A and B must be special; that is, no nontrivial
composite exists if either factor is M3 (O). The rough idea is that, since A and B have
rank at least two, the fact that products of distinguishable effects are distinguishable
will yield at least four distinguishable effects in AB. If the latter were simple, this
would be the end of the story; but we know from the case of universal tensor products
(which we will ultimately show are dynamical composites in our sense) that composites
can have nontrivial direct summands. Therefore, we need to work a bit harder, and
show that every irreducible direct summand of AB has rank at least 4.
We will need some preliminaries. An element s ∈ A is called a symmetry iff s2 = u.15
In this case Us is a Jordan automorphism of A, with Us2 = id ([4], Prop. 2.34). Also note
that p := 12 (s+u) is a projection, and, conversely, if p is a projection, then s := 2p−u is
a symmetry. Two projections p, q ∈ A are exchanged by a symmetry s ∈ A iff Us (p) = q
(in which case, p = Us (q)). More generally, p and q are equivalent iff there exists a
finite sequence of symmetries s1 , ...s` with q = (Us` ◦ · · · ◦ Us1 )(p). It will be important
below that if A and B are simple, then any two atomic projections are exchanged by a
symmetry ([31], Lemma 5.3.2).
Lemma 4.11. Let s ∈ A be a symmetry exchanging projections p1 , p2 ∈ A, and let
t ∈ B be a symmetry exchanging projections q1 , q2 ∈ B. Then s ⊗ uB and uA ⊗ t are
symmetries in AB, and UuA ⊗t Us⊗uB (p1 ⊗ q1 ) = p2 ⊗ q2 . In particular, the projections
p1 ⊗ q1 and p2 ⊗ q2 are equivalent.
Proof: (s ⊗ uB )2 = s2 ⊗ uB = uA ⊗ uB = uAB by Proposition 4.3. Similarly for uA ⊗ t.
Now by Corollary 4.4, we have
UuA ⊗t Us⊗uB (p1 ⊗ q1 ) = UuA ⊗t (Us (p1 ) ⊗ q1 ) = Us (p1 ) ⊗ Ut (q1 ) = p2 ⊗ q2 . 

15

Not to be confused with a symmetry qua order-automorphism.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

27

<!-- page 28 -->
Theorem 4.12. Let AB be a composite of simple, nontrivial Jordan algebras A and
B. Then AB is a special, universally reversible EJA.
Proof: We shall show that every irreducible direct summand of AB has rank ≥ 4, from
which the result follows. Decompose AB as a direct sum of simple ideals, say AB =
L
α Mα . Let πα : AB → Mα be the corresponding projections, and let uα := πα (uAB ) be
the unit in Mα . Suppose now that {p1 , ..., pn } is a Jordan frame in A and {q1 , ..., qm } is a
Jordan frame in B. By Proposition 4.5 and Corollary 4.6, pi ⊗pj are pairwise orthogonal
projections in AB. Since A and B are simple, there are symmetries in AB exchanging
the pi , and there are symmetries in B exchanging the qj . By Lemma 4.11, therefore,
the projections pi ⊗ qj are pairwise equivalent. By [4] Lemma 3.9, therefore, these
projections have the same central cover c. This means that for each α, the projection
πα : AB → Mα takes none of the projections pi ⊗ qj to the zero projection in Mα , or it
takes all of them to zero — the former case arising exactly when uα ≤ c, and the latter,
when uα c = cuα = 0. If Mα is of the first type, {πα (pi ⊗ qj )|i = 1, ..., n, j = 1, ..., m}
consists of nm distinct orthogonal projections in Mα , summing to the unit πα (u) =: uα .
Hence, the rank of Mα is at least nm. In particular, since A and B are nontrivial,
n, m ≥ 2, whence, Mα has rank at least 4, and hence, is special.
Now let p, q be arbitrary projections in A and B, respectively: extending each to
a Jordan frame, as above, we see that for all α, if πα (p ⊗ q) 6= 0, then Mα is special.
Hence, p ⊗ q belongs to the direct sum of the special summands of AB, i.e., to Msp .
Since projections p ⊗ q generate AB, the latter is special.
The argument also shows that each simple direct summand Mα , in addition to being
special, is not a spin factor, and hence, is UR. Since direct sums of universally reversible
EJAs are again UR (Appendix A, Proposition A.7), it follows that AB must be UR.

Proposition 4.13. Let A and B be EJAs having no 1-dimensional summands. If AB
is a composite of A and B, then AB is UR.
L

L

Proof: Decompose A and B into simple direct summands, say A = i Ai and B = Bj .
L
By Proposition 4.9, AB =
Ai Bj . By Proposition 4.8, each summand Ai Bj is a
composite, and hence, by the preceding result, UR. But direct sums of universally
reversible EJAs are again UR. 
We call an ideal trivial if it is isomorphic to a direct sum of rank-one EJAs.
Proposition 4.14. If A contains an exceptional ideal and B contains a nontrivial ideal,
there exists no composite AB satisfying the conditions of Definition 1.
Proof: Suppose B has a nontrivial ideal B1 , and that a composite AB exists. Let A0
be any simple ideal in A. By Proposition 4.8, A0 B is a composite of A0 and B. Let
B = B0 ⊕ B1 where B1 is a nontrivial simple ideal of B. Then, applying Proposition
4.8 again, A0 B1 = J(A0 ⊗ B1 ) ≤ A0 B, is a composite. Since A0 and B1 are simple,
Theorem 4.12 implies that A0 B1 is special. The fundamental identity (1) implies that
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

28

<!-- page 29 -->
the mapping A0 → A0 B1 , given by a 7→ a ⊗ u1 , where u1 is the unit of B1 , is a faithful
Jordan homomorphism. Therefore, A0 is special. 
Another way to express Proposition 4.14 is that if A is exceptional and AB exists,
then B must be a direct sum of 1-dimensional EJAs — in other words, a classical
system.
e
Theorem 4.15. Let A and B be simple, special EJAs. Then AB is an ideal in A⊗B.

Proof: By Propositions 4.3 and 4.7, we have Jordan homomorphisms A, B → AB with
operator-commuting ranges. Since AB is special, i.e., a JC-algebra, elements of AB
operator commute iff their images in C ∗ (AB) operator commute ([30], Lemma 5.1).
Thus, we have Jordan homomorphisms A, B → C ∗ (AB) with operator-commuting
ranges. The universal property given by Proposition 3.9 (a) of A e
⊗B yields a Jordan
∗
e
e
homomorphism φ : A⊗B → C (AB) taking (the image of) a ⊗ b in A⊗B
to (the
∗
e
image of) a ⊗ b in C (AB). Since both A⊗B and AB are generated by pure tensors,
φ takes A e
⊗B onto AB. Letting K denote the kernel of φ, an ideal of A e
⊗B, we have
⊥
⊥
e
A⊗B = K ⊕ K, where K is the complementary ideal; the mapping φ factors through
e → K ⊥ to give an isomorphism φ0 : K ⊥ ≃ AB, since the restriction
the projection A⊗B
φ0 of the surjection φ to K ⊥ is injective. 
In appendix A, we show that C ∗ (A⊕B) = C ∗ (A)⊕C ∗ (B) (Proposition A.6). Combining
this fact with Proposition 4.9, we can extend the preceding result as follows.
Corollary 4.16. Let AB be a composite of special EJAs A and B. Then AB is a direct
summand of A e
⊗B.
Combined with Table 2, Theorem 4.15 sharply restricts the possibilities for come
posites of simple EJAS. In particular, it follows that if A⊗B
is itself simple, then
e
AB ≃ A⊗B. In other words, in this case the universal tensor product is the only
“reasonable” tensor product (to the extent that we think the conditions of Definition
e
4.1 constitute reasonableness, in this context). If A = B = Cn , so that A⊗B
=
Mn2 (C)sa ⊕ Mn2 (C)sa , we have another candidate, i.e., the usual quantum-mechanical
composite Mn2 (C)sa . If A = B = M2 (H) (that is, if A and B are two quaternionic
e = M16 (R)sa ⊕ M16 (R)sa ⊕ M16 (R)sa ⊕ M16 (R)sa , giving us four posbits), we have A⊗B
sibilities for AB. These exhaust the possibilities for composites of simple real, complex
and quaternionic quantum systems!

5 EJC-algebras
In view of Theorem 4.12 and Corollary 4.14, we now restrict our attention to special
EJAs. A JC-algebra is variously defined as a norm-closed Jordan subalgebra of L(H)
for a real or complex Hilbert space H, or as a Jordan algebra that is Jordan-isomorphic
to such an algebra. In finite dimensions, any JC algebra is euclidean, and any special
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

29

<!-- page 30 -->
euclidean Jordan algebra is JC (on the second definition). Here, we consider EJAs that
are embedded, not necessarily in L(H) for a specific Hilbert space, but in some definite
complex ∗-algebra.
Definition 5.1. An embedded JC algebra (EJC) is a triple (A, πA , MA ) where A is an
EJA, MA is a finite-dimensional complex ∗-algebra, and πA is a unital, injective Jordan
homomorphism A → MAsa .
As the notation suggests, we often simply write A for (A, πA , MA ). Where no
confusion is likely to arise, we shall usually identify A with the Jordan subalgebra
πA (A) of MAsa , denoting (A, π, MA ) by the pair (A, MA ). For aesthetic reasons, we
abbreviate the phrase “embedded euclidean JC” by EJC (rather than EEJC), letting
the initial E stand simultaneously for embedded and euclidean.
Notice that Definition 5.1 does not require that A generate MA as a complex ∗algebra. While most of our examples satisfy this condition, few of our general results
depend on it.
In this section, we develop a canonical tensor product for EJC algebras, and use
this to construct several symmetric monoidal categories of EJC-algebras. In one case,
we obtain a category of reversible EJAs, with a monoidal product extending that of
ordinary complex matrix algebras; in another, which we call InvQM, we restrict attention to EJAs that arise as fixed-point algebras of involutions on complex ∗-algebras
(a class that includes all universally reversible EJCs, but also includes the quaternionic
bit, M2 (H)sa , as symplectically embedded in M4 (C)). Here, the monoidal structure
agrees with the Hanche-Olsen tensor product in the cases in which the factors are UR.
For any ∗-algebra M and any set S ⊆ Msa , let J(S) denote the Jordan subalgebra
of Msa generated by S. (We should probably write this as JM (S), but context will
generally make the usage unambiguous. See below for an example!)
Definition 5.2. The canonical tensor product of (A, MA ) and (B, MB ) is (A B, MA ⊗
MB ), where A B := J(A ⊗ B) ⊆ MA ⊗ MB , the Jordan subalgebra of (MA ⊗ MB )sa
generated by A ⊗ B. 16
Note that this makes it a matter of definition that MA B = MA ⊗MB . In particular,
if A and B are universally embedded, so that MA = C ∗ (A) and MB = C ∗ (B), then
∗
∗
e
A B = A⊗B,
so that MA⊗
e B = C (A) ⊗ C (B) by definition; but the fact that this
e
last is C ∗ (A⊗B)
(whence, A B is UR) is a theorem. It will also be the case that
∗
preserves C -generation: if A and B, as embedded, generate the C ∗ -algebras MA and
MB , then A B obviously generates MA B .
Let us call an EJC (A, MA ) reversible iff A is reversible in MA . Note that if A is a
simple EJC standardly embedded in MA , then A is reversible iff A = Rn , Cn or Qn for
some n.
16

When MA = Mn (C) for some n and similarly for B, this agrees with a construction by Jamjoom,
Def. 2.1 in [38].

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

30

<!-- page 31 -->
We are going to show that the canonical composite of EJCs is a composite in the
sense of Definition 4.1. In order to do so, we will need the following Lemma on extensions
of derivations.
Lemma 5.3. Let D be a derivation of an EJA A, and (A, MA ) a faithful representation
of A. Then D extends to a ∗-derivation of MA .
The proof can be found in Appendix E.17
Proposition 5.4. If (A, MA ) and (B, MB ) are EJC-algebras, then their canonical
tensor product A B is a composite in the sense of Definition 4.1.
Proof: First we must show that A B is a dynamical composite, in the sense of
Definition 2.3. In particular, it must be a composite of probabilistic models in the
sense of Definition 2.1. Conditions (a)-(c) of that definition are easily verified: That
uAB = uA ⊗ uB follows from the unitality of the embeddings A 7→ MA , B 7→ MB and
AB 7→ MAB . For all a, x ∈ (MA )sa and b, y ∈ (MB )sa , we have
ha ⊗ b|x ⊗ yi = Tr(ax ⊗ by) = Tr(ax)Tr(by) = ha|xihb|yi
Thus, for any states α = ha| and β = hb|, where a ∈ A+ and b ∈ B+ , we have a state
γ = ha ⊗ b| on AB with γ(x ⊗ y) = α(x)β(y) for all x ∈ A+ , y ∈ B+ .
That A B satisfies the additional conditions required to be a dynamical composite
in the sense of Definition 2.3 is not trivial. Using Lemma 5.3 one can show that
any φ ∈ G(A) extends to an element φb ∈ G((MA )sa ) that preserves A, and that
φb ⊗ 1MB is an order-automorphism of (MA ⊗ MB )sa preserving A B. It follows that
b preserves A B as well. The details are presented in
φb ⊗ ψb = (φb ⊗ 1MB ) ◦ (1MA ⊗ ψ)
b †=φ
b† ⊗ ψ
b† . Thus A B satisfies
Appendix E. It is not difficult to verify that (φb ⊗ ψ)
conditions (a) and (b) of Definition 4.1. Condition (c) is immediate from the definition
of A B. 
Combining this with Theorem 4.12, we see that if A and B are simple reversible EJCs
e
for which A⊗B
is also simple, then the canonical and universal tensor products of A
and B coincide. This covers all cases except those involving two factors of the form Cn
and Ck , and those involving Q2 as a factor. In fact, many of the latter are covered by
the following.
Corollary 5.5. Let (A, MA ) and (B, MB ) be simple reversible EJCs with A generating
MA and B generating MB as ∗-algebras. Suppose MA and MB carry involutions Φ and
Ψ, respectively, with Φ fixing points of A and Ψ fixing points of B (i.e. A ⊆ MΦ
A and
Φ
Φ⊗Ψ
B ⊆ MB ). Then A B = (MA ⊗ MB )sa , the set of self-adjoint fixed points of Φ ⊗ Ψ.
17

In [61], Upmeier shows that every derivation of a reversible JC algebra A acting on a complex
Hilbert space H extends to a ∗-derivation of the C ∗ algebra of operators on H generated by A. In
finite dimensions, the hypothesis of reversibility is not needed. This is doubtless well known, but as
we could find no reference to it, we have included a proof.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

31

<!-- page 32 -->
Proof: By the preceding proposition, A B is a dynamical composite of A and B;
hence, by Theorem 4.12 and the simplicity of A and B, A B is universally reversible.
Since Φ⊗Ψ fixes points of A⊗B, it also fixes points of the Jordan algebra this generates
in MA ⊗ MB , i.e., of A B. But then, by Proposition 3.7, A B is exactly the set of
fixed points of Φ ⊗ Ψ. 
For example, the quaternionic bit Q2 standardly embedded in M4 (C) = M2 (M2 (C)) as
the set of block matrices of the form
a b
−b a

!

(4)

with a self-adjoint and b antisymmetric is exactly the fixed-point set of the involution
Φ(x) = −J2 xTJ2 , where with 12 the 2 × 2 identity matrix
!

0 12
J2 =
.
−12 0

(5)

Thus, Q2 Q2 is the set of self-adjoint fixed points of Φ⊗Φ acting on M4 (C)⊗M4 (C) =
M16 (C). From this, it follows that Q2 Q2 ≃ R16 = M16 (R)sa . For details, see Appendix
B. Notice that Corollary 5.5 applies equally to all simple, universally embedded EJCs,
and to all standardly embedded EJCs except for Cn (recalling here that no (complexlinear) involution on Mn (C) fixes all points of Mn (C)sa ).
Canonical composites of standardly embedded, reversible EJAs It follows
from Proposition 5.4, together with Theorem 4.15 that the canonical and universal
tensor products coincide for simple, reversible EJCs whose universal tensor products
are simple. This covers all cases except for those in which one factor is M2 (H)sa (the
quaternionic bit), and those in which both factors have the form Mn (C)sa for some
n. Restricting attention to standardly embedded EJCs, these missing cases can be
computed directly: see appendix B and [27]. The results are summarized, up to isomorphism, in the following table. (Only those products with a factor of Q involve a
nontrivial isomorphism; details of these will appear elsewhere.) Recall here the abbreviations Rn = Mn (R)sa , Cn = Mn (C)sa and Qn = Mn (H)sa .
Rm
Cm
Qm
Table 3:

Rn
Cn
Qn
Rmn Cmn Qmn
Cmn Cmn C2mn
Qmn C2mn R4mn

, up to isomorphism, for standardly embedded, reversible EJCs

Associativity We now establish that the canonical tensor product is associative, setting the stage for the construction of symmetric monoidal categories of EJCs in Section
6.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

32

<!-- page 33 -->
Proposition 5.6.
is associative. More precisely, the associator mapping α : MA ⊗
(MB ⊗MC ) → (MA ⊗MB )⊗MC carries A (B C) isomorphically onto (A B) C.
The essence of the proof is the following Lemma.
Lemma 5.7. Let M and N be ∗-algebras, and let A and B be subspaces of Msa and Nsa ,
respectively, with 1 = 1M ∈ A and similarly for B. Then J(A ⊗ J(B)) = J(A ⊗ B)18 .
Proof of Lemma 5.7: We make use of the following notation. If X and Y are subsets
(note: not necessarily subspaces) of M and N, respectively, let

·

·

X Y := { a b | a ∈ X, b ∈ Y };
similarly, X +Y is the set of sums a+b with a ∈ X, b ∈ Y , and, for t ∈ R, tX consists of
multiples ta of elements a ∈ X. Finally, we write X }Y for the set {a⊗b|a ∈ X, b ∈ Y }
of pure tensors of elements in X and Y . Note that if X and Y happen to be subspaces
of M and N, respectively, then J(X } Y ) = J(X ⊗ Y ).
Now let N denote the set of all subsets Y of N such that
(i) B ⊆ Y ⊆ J(B), and
(ii) A } Y ⊆ J(A } B).
Note that B ∈ N ; hence, N is non-empty. We are going to show first that J(B) = N .
Claim 1: If Y1 , Y2 ∈ N , then the sets Y1 Y2 , Y1 + Y2 and tY1 (t any real scalar)
belong to N .
To see this, suppose that y1 ∈ Y1 ∈ N and y2 ∈ Y2 ∈ N . Then for any a ∈ A, we
have
S

·

·

1
a ⊗ (y1 y2 ) = a ⊗ (y1 y2 + y2 y1 )
2
1
=
[(a ⊗ y1 y2 ) + (a ⊗ y2 y1 )]
2
1
=
[(a ⊗ y1 )(1 ⊗ y2 ) + (1 ⊗ y2 )(a ⊗ y1 )]
2
= (a ⊗ y1 ) (1 ⊗ y2 ).

·

Since A } Y1 and A } Y2 are both, by assumption, contained in J(A } B), the last
expression defines an element of J(A ⊗ B). Since a is arbitrary here, all pure tensors
from A } (Y1 Y2 ) belong to J(A } B). Since the latter is a subspace of (M ⊗ N)sa ,
it follows that linear combinations of pure tensors from A } (N1 N2 ) are contained in
J(A } B) as well. Finally, notice that B ⊆ Y1 and B ⊆ Y2 implies that B ⊆ Y1 Y2
(for instance, express b ∈ B as b 1). The corresponding claims for Y1 + Y2 and tY1 are
straightforward, since a ⊗ (y1 + y2 ) = (a ⊗ y1 ) + (a ⊗ y2 ) and a ⊗ ty1 = t(a ⊗ y1 ).

·

·

·

·

18

Note that on the left, J(A ⊗ J(B)) refers to the Jordan subalgebra of (A ⊗ B)sa generated by
A ⊗ J(B), where J(B) refers to the Jordan subalgebra of Nsa generated by B.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

33

<!-- page 34 -->
Now let J = N . Claim 2: J = J(B). Since B ⊆ J ⊆ J(B), it’s enough to show
that J is a Jordan subalgebra of Nsa . Let y1 , y2 ∈ J: then for some Y1 , Y2 ∈ M, we
have y1 ∈ Y1 and y2 ∈ Y2 . By Claim 1, y1 y2 ∈ Y1 Y2 ∈ N , y1 + y2 ∈ Y 1 + Y2 ∈ N , and
ty1 ∈ tY1 ∈ N ; hence, y1 y2 , y1 + y2 and ty1 belong to J. In other words, J is closed
under scalar multiplication, addition and the Jordan product. This proves Claim 2.
S
We now use the fact that J(B) = N to show that J(A ⊗ J(B)) = J(A ⊗ B). Let
P
S
τ = i ai ⊗ yi be an arbitrary element of A ⊗ J(B). Since J(B) = N , for each i,
yi ∈ Yi for some Yi ∈ N . But then, by definition of N , for every i ai ⊗ yi ∈ A}Yi ⊆
J(A ⊗ B); since the latter is a subspace of M ⊗ N, τ ∈ J(A ⊗ B) as well. Thus,
A ⊗ J(B) ⊆ J(A ⊗ B).
It now follows that A ⊗ B ⊆ A ⊗ J(B) ⊆ J(A ⊗ B), hence, that J(A ⊗ B) ⊆
J(A ⊗ J(B)) ⊆ J(A ⊗ B). 
S

·

·

·

Proof of Proposition 5.6: Let (A, MA ), (B, MB ) and (C, MC ) be EJC-algebras. We
need to show that the associator mapping α : MA ⊗ (MB ⊗ MC ) → (MA ⊗ MB ) ⊗ MC
carries A (B C) onto (A B) C. Applying Lemma 5.6, (and noting that A, B C,
A B and C all contain the relevant units), we have
A

(B

C) = J(A ⊗ J(B ⊗ C)) = J(A ⊗ (B ⊗ C))

(A

B)

C = J(J(A ⊗ B) ⊗ C) = J((A ⊗ B) ⊗ C).

and
The associator mapping is a ∗-isomorphism, and carries A ⊗ (B ⊗ C) to (A ⊗ B) ⊗ C.
Hence, it also carries J(A ⊗ (B ⊗ C)) onto J((A ⊗ B) ⊗ C). 
Direct sum of EJCs If (A, MA ) and (B, MB ) are two embedded EJAs, define (A, MA )⊕
(B, MB ) = (A ⊕ B, MA ⊕ MB ), where the embedding of A ⊕ B in MA ⊕ MB is the
obvious one. Notice that by Proposition A.6, for universally embedded EJCs we have
(A, C ∗ (A)) ⊕ (B, C ∗ (B)) ≃ (A ⊕ B, C ∗ (A ⊕ B)).
Lemma 5.8. For all EJCs A, B and C, we have
A

(B ⊕ C) = (A

B) ⊕ (A

C).

Proof: One can easily check that for sets X ⊆ MA and Y ⊆ MB , J(X ⊕ Y ) =
J(X) ⊕ J(Y ). Using this, and the distributivity of tensor products over direct sums in
the contexts of vector spaces and ∗-algebras, we have
A

(B ⊕ C) = J(A ⊗ (B ⊕ C)) = J((A ⊗ B) ⊕ (A ⊗ C))
= J(A ⊗ B) ⊕ J(A ⊗ C)
= (A B) ⊕ (A C)

(where J refers variously to generated Jordan subalgebras of MA ⊗ (MB ⊕ MC ), (MA ⊗
MB ) ⊕ (MA ⊗ MC ), MA ⊗ MB , and MA ⊗ MC ). 
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

34

<!-- page 35 -->
6 Monoidal Categories of EJC-algebras
As discussed in Section 2, a physical theory ought to be represented by a category, in
which objects correspond to systems and morphisms to physical processes. An obvious
candidate for a category in which objects are embedded JC-algebras is the following.
Recall here that a linear map φ : MA → MB is completely positive if the map φ :
MA ⊗ Cn → MB ⊗ Cn is positive for each positive integer n.
Definition 6.1. Let (A, MA ) and (B, MB ) be EJC-algebras. A linear mapping φ :
MA → MB is Jordan preserving iff φ(A) ⊆ B. The category EJC has, as objects,
EJC-algebras, and, as morphisms, completely positive Jordan-preserving mappings.
In view of Proposition 5.6, one might guess that EJC is symmetric-monoidal under
. There is certainly a natural choice for the monoidal unit, namely I = (R, C).
However, the following examples show that tensor products of EJC morphisms are
generally not morphisms.
Example 6.2. Let (A, C ∗ (A)) and (B, C ∗ (B)) be simple, nontrivial, universally embedded EJCs, and suppose that B is not UR (e.g., the spin factor V4 ). Suppose, further,
e
that A⊗B
is irreducible — for instance, let A = Rn for any n. Let Bb be the set of
fixed points of the canonical involution ΦB (cf. Definition 3.6). Then by Theorem 4.15,
e
A B = A⊗B,
the set of fixed points of ΦA ⊗ ΦB . In particular, uA ⊗ Bb is contained in
A B. Now let α be a state on C ∗ (A). It is easily verified that every state is completely
positive,19 and it is trivial that it is Jordan-preserving, and so, a morphism in EJC.
But
b = α(u )B
b = B,
b
(α ⊗ idB )(uA ⊗ B)
A
which by Proposition 3.7 is larger than B because B is not UR. So α ⊗ idB isn’t
Jordan-preserving.
The next example is similar:
Example 6.3. Let Cn = Mn (C)sa and Rk = Mk (R)sa , as usual. Consider these as
standardly embedded, i.e., consider the EJCs (Cn , Mn (C)) and (Rk , Mk (C)), where in
the latter, Rk is embedded as the set k × k complex matrices with real entries, i.e., the
set of self-adjoint symmetric k × k complex matrices. Then we have
(Cn , Mn (C))

(Rk , Mk (C)) = (Cnk , Mnk (C))

where the embedding of Cnk in Mnk (C) is the standard one. Now let α be a state on
Mn (C), and let b be any self-adjoint matrix in Mk (C). Then 1n ⊗ b is self-adjoint in
Mn (C) ⊗ Mk (C) = Mnk (C), and (α ⊗ idMk (C))(1n ⊗ b) = b. Since b needn’t belong to
Rk , the mapping α ⊗ idMk (C) isn’t Jordan-preserving.
19

Letting α be a state on A and therefore on the complex matrix algebra MA , β a positive functional
on any complex matrix algebra MB , and f ∈ (MA ⊗ MB )+ , we have β((α ⊗ idB )(f )) = (α ⊗ β)(f ).
This is nonnegative since α ⊗ β is a positive functional. Since this holds for all positive β, (α ⊗ idB )(f )
is positive, i.e. (since MB was arbitrary) α is completely positive.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

35

<!-- page 36 -->
6.1 Completely Jordan Preserving Maps
Examples 6.2 and 6.3 suggest the following adaptation of the notion of complete positivity to our setting.
Definition 6.4. A linear mapping φ : (A, MA ) → (B, MB ) is completely Jordan preserving (CJP) iff, for any embedded JC-algebra (C, MC ), the mapping φ ⊗ idMC is
positive, and takes A C into B C.
Note that this implies that φ is both Jordan-preserving (take C = R) and completely
positive (take C = Cn for any n).
Lemma 6.5. If φ : MA → MB is CJP, then for any (C, MC ), φ ⊗ idMC is again CJP.
Proof: If (D, MD ) is another embedded JC-algebra, consider (C
associativity of gives us

D, MC ⊗ MD ). The

(φ ⊗ idMC ) ⊗ idMD = φ ⊗ (idMC ⊗MD ).
Since φ is CJP, the latter carries A (C D) into B (C D). Since is associative,
this tells us that (φ ⊗ idC ) ⊗ idD carries (A C) D into (B C) D. 
While all CJP morphisms are CP, Example 6.2 shows that the converse is false. On
the other hand, the class of CJP morphisms is still quite large.
Example 6.6. Let φ : MA → MB be a ∗-homomorphism taking A to B. It is easily
verified that φ ⊗ idMC is again a ∗-homomorphism. Since ∗-homomorphisms preserve
the concrete Jordan product,20 φ ⊗ idMC takes the Jordan subalgebra generated by
A ⊗ C to that generated by B ⊗ C, i.e., sends A C into B C. So φ is CJP.
Example 6.7. Let (A, MA ) be an embedded JC-algebra, and let a ∈ A. The mapping
Ua : MA → MA given by Ua (b) = aba is completely positive; recall that its restriction
to (MA )sa can be expressed in terms of the Jordan product on (MA )sa by

··

·

Ua (b) = 2a (a b) − (a2 ) b
Since A is a Jordan subalgebra of (MA )sa , this makes it clear that Ua (b) ∈ A for all
a, b ∈ A. Thus, Ua is a morphism. Now if (C, MC ) is another embedded JC-algebra,
one easily sees21 that
Ua ⊗ Uc = Ua⊗c
for all c ∈ MC ; in particular,
Ua ⊗ idMC = Ua ⊗ U1 = Ua⊗1 .
Since a ⊗ 1 ∈ A
20

C, it follows that Ua is CJP.

That is, a ∗-homomorphism ϕ satisfies ϕ((xy + yx)/2) = (ϕ(x)ϕ(y) + ϕ(y)ϕ(x))/2.

21

Observe that that (Ua ⊗ Uc )(x ⊗ y) = axa ⊗ cyc = (a ⊗ c)(x ⊗ y)(a ⊗ c) = Ua⊗c (x ⊗ y) and that
the “pure tensors” x ⊗ y span MA ⊗ MC .
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

36

<!-- page 37 -->
Proposition 6.8. Let (A, MA ), (A0 , MA0 ), (B, MB ), (B 0 , MB 0 ) and and (C, MC ) be
EJC-algebras.
(i) If φ : MA → MB and ψ : MB → MC are CJP, then so is ψ ◦ φ, and
(ii) if φ : MA → MB and ψ : MA0 → MB 0 are CJP, then so is φ ⊗ ψ : MA A0 =
MA ⊗ MA0 → MB ⊗ MB 0 = MB B 0 .
φ ⊗ ψ = (φ ⊗ idMB0 ) ◦ (idMA ⊗ ψ)
is again CJP.
Proof: (i) is straightforward, and (ii) follows from (i) and Lemma 6.5. 
As Example 6.2 illustrates, for certain non-UR EJCs A, there are no non-zero CJP
maps from A to I. In particular, normalized states on such an A will not count as
morphisms in the category CJP. Operationally, this means that the preparation of
states and registration of effects need not correspond to any physical process in CJP.
We now show that this defect can sometimes be remedied by relativizing the definition
of CJP mappings to certain sub-categories of CJP.

6.2 Relatively CJP Mappings
Definition 6.9. Let (A, MA ) and (B, MB ) belong to C. A positive linear mapping
φ : MA → MB is relatively CJP with respect to C if, for all (C, MC ) ∈ C, the mapping
φ ⊗ idMC is positive and maps A C into B C. We denote the set of all such maps
by CJPC (A, B).
Proposition 6.10. Let C be any class of EJCs closed under the formation of the canonical tensor product and containing the trivial EJC I. Then C is a symmetric monoidal
category with completely positive relatively CJP mappings as morphisms and the canonical tensor product as the monoidal product.
Proof: Exactly as in the proof of Proposition 6.8, we see that if A, B, C ∈ C and
φ ∈ CJPC (A, B) and ψ ∈ CJPC (B, C), then ψ ◦ φ ∈ CJPC (A, C), and also that if
A, B, C, D ∈ C and φ ∈ CJPC (A, B) and ψ ∈ CJPC (C, D), then φ ⊗ ψ ∈ CJPC (A ⊗
C, B ⊗ D). In other words, C becomes a symmetric monoidal category with relatively
CJP mappings as morphisms. We denote this category by CJPC . Note that φ’s being
relatively CJP with respect to C implies that φ is CP. For, either C contains an A
such that MA is noncommutative, or it does not. If all MA are commutative, then all
positive maps between them are CP. On the other hand, if some MA is noncommutative,
it contains a summand isomorphic to Mn (C) for some n ≥ 2. By closure under , it
contains C with a summand equal to Mm (C) for arbitrarily large m (just take C =
A A · · · A with sufficiently many factors of A). Since the definition of “completely
Jordan preserving relative to C” requires φ ⊗ idC be positive for all C, and positivity on
a matrix algebra requires positivity on all summands, we have that for every positive
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

37

<!-- page 38 -->
integer n, there exists m ≥ n such that φ ⊗ Mm (C) is positive. That is sufficient for φ
to be completely positive.
Example 6.11 (The category CQM). Let C be the class of hermitian parts of complex
∗-algebras with standard embeddings. Then φ belongs to CJPC iff φ is CP. Evidently,
this category is essentially orthodox, mixed-state QM with superselection rules. From
now on, we shall call this category CQM.
Example 6.12 (The category RSE). Recall that the standard embeddings for simple,
reversible Jordan algebras represent
(a) Rn as the set of self-adjoint elements of Mn (C) having real entries;
(b) Cn as itself, that is, the set of all self-adjoint elements of Mn (C);
(c) Qn as the set of 2n×2n complex matrices having symplectic 2×2 block structure.
For A = Rn , Cn or Qn , let St(A) denote the matrix algebra, and σA : A → St(A)
the embedding, given above. Now let Co denote the class of reversible, simple EJCs
(A, MA ) that are standardly embedded up to isomorphism, in the sense that there exists
a ∗-isomorphism φ : MA ≃ St(A) acting on the identity on A (or, more exactly, such
that φ ◦ πA = σA . ) It is straightforward to check that Co is closed under the canonical
tensor product [27]. Now let C consist of direct sums of EJCs belonging to Co . Since
the canonical tensor product distributes over direct sums, by Lemma 5.8, C is also
closed under . By the remarks above, then, CJPC is a symmetric monoidal category,
which we call RSE. This represents a kind of unification of finite-dimensional real,
complex and quaternionic quantum mechanics, in so far as its objects are the Jordan
algebras associated with real, complex and quaternionic quantum systems, and direct
sums of these. Moreover, as restricted to complex (or real) systems, its compositional
structure is the standard one. However, Example 6.3 shows that not every quantummechanical process — in particular, not even processes that prepare states — will count
as a morphism in RSE, so this unification comes at a high cost.
Example 6.13 (The category URUE). Let C be the class of universally reversible
EJCs with universal embeddings. By Proposition 5.4 and Theorem 4.12, if A and B
are simple, then A B is UR. It is straightforward that C ∗ (A ⊕ B) = C ∗ (A) ⊕ C ∗ (B)
(Appendix A, Proposition A.6) and that A ⊕ B is UR iff A and B are UR (Corollary
A.7). Finally, we know that the canonical tensor product distributes over direct sums
(Lemma 5.8). Putting these observations together, we see that C is closed under . We
denote the category CJPC by URUE.
Morphisms in URUE can be characterized more concretely: they are precisely those
CP maps that intertwine the canonical involutions on universal C ∗ algebras.
Proposition 6.14. Let A and B be UR, universally embedded EJCs. Then a mapping
φ : C ∗ (A) → C ∗ (B) belongs to URUE iff it is CP, and satisfies φ ◦ ΦA = ΦB ◦ φ.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

38

<!-- page 39 -->
Proof: First, we show that CP intertwiners are relatively CJP. Let φ : A → B be a
CP intertwiner. We are to show that for every C ∈ C, φ ⊗ idC : A C → B C
is positive and Jordan-preserving. It is positive because φ is CP. By Corollary 5.5,
we have A C = (MA ⊗ MC )ΦA ⊗ΦC and B C = (MB ⊗ MC )ΦB ⊗ΦC . Intertwining
then immediately gives that φ ⊗ idC is Jordan-preserving: suppose x ∈ A C, i.e.
(ΦA ⊗ ΦC )(x) = x. Then (ΦB ⊗ ΦC ) ◦ (φ ⊗ idC (x)) = ((ΦB ◦ φ) ⊗ ΦC )(x) = (φ ◦ ΦA ) ⊗
ΦC )(x) = ((φ ⊗ id) ◦ (ΦA ⊗ ΦC ))(x) = (φ ⊗ idC )(x), i.e. (φ ⊗ idC )(x) is fixed by ΦB ⊗ ΦC ,
i.e. it is in B C.
For the converse, suppose φ is relatively CJP for the class of UR, universally embedded EJCs. Note that C ∗ (A)sa decomposes as the direct sum of ΦA ’s +1 and
−1 eigenspaces. Moreover, as A is UR, the +1 eigenspace is precisely A. Now,
φ ◦ ΦA = ΦB ◦ φ trivially on A. We now claim that φ also intertwines ΦA and ΦB
on the −1-eigenspace. To see this, note that φA ⊗ idC is also relatively CJP for any
object C in URUE. If a and c belong to the −1-eigenspaces of ΦA and ΦC , respectively,
then a ⊗ c belongs to the +1 eigenspace of ΦA ⊗ ΦC , whence,
(ΦB ⊗ ΦC )(φ ⊗ id)(a ⊗ c) = (φ ⊗ id)(ΦA ⊗ ΦC )(a ⊗ c).
Since ΦC (c) = −c, this reduces to
−(ΦB (φ(a)) ⊗ c) = −(φ(ΦA (a)) ⊗ c).
With c non-zero, this implies that ΦB (φ(a)) = φ(ΦA (a)) for all a in the −1 eigenspace
of ΦA , as required. Thus, φ intertwines ΦA and ΦB on all of C ∗ (A)sa , and hence, by
the Cartesian decomposition, on all of C ∗ (A). 
As we will see below ( Corollary 6.17), maps in URUE(A, I) and URUE(I, A) correspond exactly to states and effects, respectively, on A. In this respect, the category
URUE is closer than RSE to being a legitimate “unified” quantum theory, although
it omits the quaternionic bit (which is reversible, but not universally so). Even as
restricted to complex quantum systems, however, it differs from orthodox QM in two
interesting ways. First, and most conspicuously, the tensor product is not the usual
one: Cn e
⊗Ck = Cnk ⊕ Cnk , rather than Cnk . Secondly, it allows some processes that
orthodox QM does not. In particular, the mapping on C ∗ (Cn ) = Mn (C) ⊕ Mn (C) that
swaps the two summands is a morphism in URUE. Since the image of Cn in C ∗ (Cn )
consists of pairs (a, aT ), this mapping effects the transpose automorphism on Cn . This
is not permitted in orthodox QM, as the transpose is not a CP mapping on Mn (C).
(This causes no difficulty with positivity in the context of URUE, where the tensor
product is different.)
In spite of its divergences from orthodoxy, URUE is in many respects a well-behaved
probabilistic theory. Proposition 6.14 suggests a way in which it can be improved, which
we explore in the next section.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

39

<!-- page 40 -->
6.3 The Category InvQM
Recall that we write MΦ for the set of fixed-points of an involution Φ on a complex ∗algebra M. Notice that the involution Φ on Mn (C) with Rn = Mn (C)Φ
sa (the transpose)
Φ
T
and on M2n (C) with Qn = M2n (C)sa , namely Φ(a) = −Ja J where J is the unitary in
Eq. (2), are both unitary with respect to the trace inner product ha, bi := Tr(ab∗ )22 .
The canonical involution on C ∗ (Cn ) = Mn (C) ⊕ Mn (C), namely, the mapping (a, b) 7→
(bT , aT ), is likewise unitary.
Definition 6.15. Call an EJC (A, MA ) involutive iff there exists an involution Φ on
MA , unitary with respect to the trace inner product on MA , with A = (MA )Φ
sa . Let
InvQM denote the category in which objects are involutive EJC-algebras, and in which
a morphism φ : A → B is a CP mapping φ : MA → MB intertwining ΦA and ΦB , i.e,
ΦB ◦ φ = φ ◦ ΦA .
As pointed out earlier, the condition that A be the set of self-adjoint fixed points
of an involution makes A reversible in MA . Thus, the class of involutive EJC-algebras
contains no “higher” (n = 4 or n > 5) spin factors. In fact, up to isomorphism it
contains exactly direct sums of the universally embedded UR EJCs (A, C ∗ (A)) where
A = Rn , Cn , with n arbitrary, or Qn with n > 2, together with the standardly embedded quabit, i.e., (Q2 , M4 (C)), with Q2 the self-adjoint fixed points of the involution
Φ(a) = −JaT J discussed in Section 3.3. In other words, InvQM includes exclusively
quantum systems over the three division algebras R, C and H, albeit with the complex
systems represented in their universal embeddings. Note that (R, M1 (R)) counts as
an involutive EJC: since M1 (R) = R is commutative, the identity map provides the
necessary involution.
Proposition 6.14 tells us that URUE is a full subcategory of InvQM, obtained
by omitting the quabit.
On the other hand, it is easy to see that CP mappings
MA → MB intertwining ΦA and ΦB are automatically relatively CJP for the class of
involutive EJCs. By Corollary 5.5 the canonical tensor product of involutive EJCs is
again involutive, as
ΦA ⊗ΦB
A B = (MA ⊗ MB )sa
for all A, B ∈ InvQM. Proposition 5.3 implies that A B is a composite of A and
B in the sense of Definition 4.1. Composites and tensor products of intertwining CP
maps are also intertwining CP-maps (as are associators, unit-introductions and the
swap mapping), so InvQM is a symmetric monoidal category — indeed, a monoidal
subcategory of the category of involutive EJC-algebras and relatively CJP maps. In
fact, these two categories are equal, because every step of the proof of Proposition 6.14
is valid for InvQM, indeed, for any category of the form CJPC , where C is an -closed
subset of (the set of objects of) InvQM. So we have:
22

We follow the convention that inner products are linear in the first argument.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

40

<!-- page 41 -->
Proposition 6.16. Let C be any set of involutive EJCs closed under . Then CJPC
is a symmetric monoidal category, with hom-sets CJPC (A, B) = {φ : MA → MB :
φ is completely positive and φ ◦ ΦA = ΦB ◦ φ}.
In other words, CJPC for such a C is a full monoidal subcategory of InvQM. In
particular, InvQM = CJPobInvQM .
In the special case in which A and B are universally embedded complex quantum
systems, say A = Cn and B = Ck , we have MA = C ∗ (Cn ) = Mn (C) ⊕ Mn (C) and
similarly MB = Mk (C) ⊕ Mk (C). The involutions ΦA are given by ΦA (a, b) = (bT , aT ),
and similarly for ΦB . In this case, the interwining CP-maps are sums of mappings
of the two forms: (a, b) 7→ (φ(a), φT (b)) and (a, b) 7→ (φT (b), φ(a)), where φ is a CP
mapping Mn (C) → Mk (C) and φT is determined by the condition φT (xT ) = (φ(x))T ,
i.e. φT := T ◦ φ ◦ T .
Two special cases of InvQM-morphisms are worth emphasising:
Corollary 6.17. Let (A, MA ) belong to InvQM. Then
(a) InvQM(I, A) is the set of linear mappings φa : R → MA , for each a ∈ A+ , where
φa is the map determined by φa (1) = a;
(b) InvQM(A, I) is the set of positive linear functionals (including, in particular,
every state) on MA of the form |ai, a ∈ A+ .
(c) Each of InvQM(I, A) and InvQM(A, I) is a cone affinely isomorphic to A+ .
Proof: A linear map φ : I → MA is determined by φ(1). Let φa ∈ InvQM(I, A) be
the map with φ(1) = a. Complete positivity of φa is equivalent to a ∈ (MA )+ ,23 and
intertwining, to the condition that a ∈ A.24 So a ∈ (MA )+ ∩ A, which by Proposition
3.2 is equal to A+ .
The completely positive maps MA → MI are the maps |ai, a ∈ (MA )+ , i.e.
x 7→ hx|ai, where the inner product is the canonical one on MA . (In particular, a
is Hermitian.) Recall that ΦI = idC so intertwining, for such a map, means that
hΦA (x)|ai = hx|ai. Unitarity of ΦA implies hΦA (x), ai = hx, ΦA (a)i, so intertwining,
for Hermitian x, becomes hx, ΦA (a)i = hx, ai, i.e. ΦA (a) = a, i.e. a ∈ A. So we have
established that a ∈ (MA )+ ∩ A = A+ .
Considered as maps A → L(R, (MA )sa ) and L((MA )sa , R), the maps γ : a 7→ φa
and µ : a 7→ |ai induce isomorphisms of linear spaces between A and their ranges,
taking A+ onto InvQM(I, A) and InvQM(A, I) respectively, which establishes the
23

Complete positivity certainly implies a ∈ (MA )+ , since positivity is equivalent to a ∈ (MA )+ . On
the other hand, for any C, φa ⊗ idC : MI ⊗ MC → MA ⊗ MC acting on x ∈ (MI ⊗ MC )+ ≃ (MC )+
just gives a ⊗ x, which is positive iff a ∈ (MA )+ .
24

Noting that ΦI = id : MI → MI , we see that φa ◦ ΦI = φa , so intertwining says that ΦA ◦ φa = φa .
Since a CP map intertwines iff it does so on the Hermitian part of its domain, intertwining is equivalent
to ΦA ◦ φa (λ) = φa (λ) holding for all λ ∈ R, i.e. λΦA (a) = λa, which by involutiveness is equivalent
to a ∈ A.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

41

<!-- page 42 -->
affine isomorphisms claimed in (c). 
The category InvQM provides a unification of finite-dimensional real, complex and
quaternionic quantum mechanics, but with the same important caveats that apply to
URUE: the representation of orthodox, complex quantum systems Cn in InvQM is
through the universal embedding ψ : Cn 7→ C ∗ (Cn ) = Mn (C) ⊕ Mn (C), a 7→ (a, aT ). As
a consequence, the composite of two complex quantum systems in InvQM is a direct
sum of two copies of the their standard composite — equivalently, is the standard
composite, combined with a classical bit. Moreover, the mapping that swaps the direct
summands of C ∗ (Cn ), a perfectly good morphism in InvQM, acts as the transpose on
ψ(a) = (a, aT ).

6.4 Compact Closure
A compact structure on a symmetric monoidal category C is a choice, for every object
A ∈ C, of a dual object: A triple (A0 , ηA , fA ) consisting of an object A0 ∈ C, a co-unit
ηA : A ⊗ A0 → I and a unit fA : I → A0 ⊗ A such that
idA ⊗fA
η ⊗id
A → A ⊗ I −→
A ⊗ (A0 ⊗ A) −→ (A ⊗ A0 ) ⊗ A A−→ A I ⊗ A → A
and
idA0 ⊗ηA 0
fA ⊗id 0
A ⊗ I → A0
A0 → I ⊗ A0 −→A (A0 ⊗ A) ⊗ A0 −→ A0 ⊗ (A ⊗ A0 ) −→
give the identity morphisms on A and A0 , respectively (and where the unlabeled arrows
are the obvious unit introductions and associators).25 The standard example is the
category FinVec of finite-dimensional vector spaces (say, over C) and linear mappings.
Here there is a canonical linear functional ηA : A ⊗ A∗ → C, namely, the trace. A
P
canonical unit is supplied by picking a basis E for A, and setting fA = x∈E fx ⊗ fx ,
where {fx } is the dual basis for A∗ ; one then shows that this is independent of E, and
that the identities above hold.
We say a symmetric monoidal category is compact closed if it admits a compact
structure. 26 In [1], it is shown that a large number of information-processing protocols,
including in particular conclusive teleportation and entanglement-swapping, hold in
any compact closed symmetric monoidal category, if we interpret objects as systems
and morphisms as physically allowed processes. In this section, we shall see that our
25

Our usage is slightly perverse. The usual convention is to denote the unit by ηA and the co-unit
by A . Our choice is motivated in part by the desire to represent states as morphisms A → I and
effects as morphisms I → A, rather than the reverse, together with the convention that takes the unit
to correspond to the maximally entangled state.
26
This makes compact closure a property of some symmetric monoidal categories (SMCs). Some
authors instead define a compact closed category as a distinct mathematical structure, namely an
SMC equipped with a distinguished compact structure.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

42

<!-- page 43 -->
category InvQM is compact closed. More exactly, we shall show that it inherits a
compact structure from the natural compact structure on the category ∗-Alg of finitedimensional complex ∗-algebras, which we now review.
If M is a finite-dimensional complex ∗-algebra, let Tr denote the canonical trace
on M, regarded as acting on itself by left multiplication (so that Tr(a) = tr(La ),
La : M → M being La (b) = ab for all b ∈ M). This induces an inner product on
M, given by ha, biM = Tr(ab∗ )27 . Note that this inner product is self-dualizing, i.e,.
a ∈ M+ iff ha, bi ≥ 0 for all b ∈ M+ .
Now let M be the conjugate algebra, writing a for a ∈ M when regarded as belonging
to M (so that ca = c a for scalars c ∈ C and ab = ab for a, b ∈ M). Note that
ha, bi = hb, ai. Now define
X
fM =
e⊗e∈M⊗M
e∈E

where E is any orthonormal basis for M with respect to h | iM . Then straightforward
computations show that fM ∈ (M ⊗ M)+ , and that, for all a, b ∈ M,
ha ⊗ b, fM i = ha, bi = Tr(ab∗ ),
where the inner product on the left is the trace inner product on M ⊗ M∗ . Now define
ηM : M ⊗ M → C by ηM = |fM i, noting that this functional is positive (so, up to
normalization, a state) since fM is positive in M ⊗ M.
A final computation shows that, for any states α and α on M and M, respectively,
and any a ∈ M, a ∈ M, we have
(ηM ⊗ α)(a ⊗ fM ) = α(a) and (α ⊗ ηM )(fM ⊗ a) = α(a).
Thus, ηM and fM define a compact structure on ∗-Alg, for which the dual object of M
is given by M.
Definition 6.18. The conjugate of a EJC-algebra (A, MA ) is (A, MA ), where A =
{a|a ∈ A}. We write ηA for ηMA and fA for fMA .
Any linear mapping φ : M → N between ∗-algebras M and N gives rise to a linear
mapping φ : M → N, given by φ(a) = φ(a) for a ∈ M. It is straightforward to show
that if Φ is a unitary involution on MA with A = MA Φ
sa , then Φ : M → M is also a
Φ

unitary involution with MA sa = A. Thus, the class of involutive EJCs is closed under
the formation of conjugates.
Lemma 6.19. Let (A, MA ) belong to InvQM. Then fA ∈ A

A.

Proof: By assumption, there is a unitary involution Φ on MA such that A = (MA )Φ
sa ;
by Corollary 5.5, A A is then the set of self-adjoint fixed points of Φ ⊗ Φ. Since Φ is
unitary, if E is an orthonormal basis for MA , then so is {Φ(e)|e ∈ E}; hence, as fA is
27

Again, we are following the convention that complex inner products are linear in the first argument.

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

43

<!-- page 44 -->
independent of the choice of orthonormal basis, fA is invariant under Φ ⊗ Φ. Since fA
is also self-adjoint, it belongs to (MA ⊗ MA )Φ⊗Φ
A. 
sa , i.e., to A
It follows now from part (b) of Corollary 6.17 that the functional
ηA = |fA i : MA ⊗ MA → R
is an InvQM morphism. Hence, InvQM inherits the compact structure from ∗-Alg,
as promised. We have arrived at the following.
Theorem 6.20. InvQM is compact closed.
Dagger compactness In fact, we can do a bit better. A dagger on a category C is
an involutive contravariant functor † : C → C that fixes objects; that is, A† = A for all
A ∈ C, and f † ∈ C(B, A) for all f ∈ C(A, B) with f †† = f . If C is a symmetric monoidal
category equipped with a dagger satisfying (f ⊗ g)† = f † ⊗ g † for all morphisms f and
†
g, and also σA,B
= σB,A , where σA,B : A ⊗ B → B ⊗ A is the “swap” morphism, then
C is said to be dagger-monoidal. Finally, if C admits a compact structure such that
ηA† = fA , then C is said to be dagger-compact.
It is not difficult to show that ∗-Alg is dagger-compact, where, if M and N are
finite-dimensional ∗-algebras and φ : M → N is a linear mapping, φ† is the hermitian
adjoint of φ with respect to the natural trace inner products on M and N. If (A, MA )
and (B, MB ) are involutive EJC-algebras with given unitary involutions ΦA and ΦB ,
then for any intertwiner φ : MA → MB , φ† also intertwines ΦA and ΦB . Hence, we
have
Corollary 6.21. InvQM is dagger-compact.

7 Conclusion
We have constructed two categories of probabilistic models — the categories RSE
and InvQM — that, in different ways, unify finite-dimensional real, complex and
quaternionic quantum mechanics. In each case, there is a price to be paid for this
unification. For RSE, this price is steep: RSE is a monoidal category, but one in
which states (for instance) on complex systems don’t count as physical processes. In
particular, RSE is very far from being compact closed.28
In contrast, InvQM is clearly a well-behaved — indeed, dagger-compact — probabilistic theory, in which the states, as well as the effects, of real, complex, and quaternionic Euclidean Jordan algebras appear as morphisms. On the other hand, InvQM
admits the transpose automorphism on the complex Hermitian Jordan algebra, and requires complex quantum systems to compose in a non-standard way. Nevertheless, by
28

In [13], we erroneously claimed that the category URSE of universally reversible, but standardly
embedded, EJC algebras, with relatively CJP mappings, is compact closed. That this is not the case
is clear from Example 6.3.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

44

<!-- page 45 -->
virtue of being dagger compact, InvQM continues to enjoy many of the informationprocessing properties of standard complex QM, e.g., the existence of conclusive teleportation and entanglement-swapping protocols [1]. Also, composites in InvQM satisfy
the Cirel’son bound on correlations owing to the way that, by construction, these composites are embedded within a tensor product of complex matrix algebras.
All of this is in spite of the fact that composites in InvQM are not locally tomographic: the canonical composite A B is larger than the vector space tensor product
A ⊗ B. Local tomography is well known to separate complex QM from its real and
quaternionic variants, so its failure in URUE and RSE is hardly surprising, but it
is noteworthy that we are able to construct (non-locally tomographic) composites in
URUE in all of the non-real cases, and certain composites involving quaternions even
in RSE. Even more interesting is the fact that, for quaternionic systems A and B,
the information capacity — the number of sharply distinguishable states — of A B
is larger than the product of the capacities of A and B. A related point is that, for
quaternionic quantum systems A and B, the product of a pure state of A and a pure
state of B will generally be a mixed state in A B.
The category InvQM contains interesting compact closed subcategories. In particular, real and quaternionic quantum systems, taken together, form a (full) monoidal
sub-category of InvQM closed under composition. We conjecture that this is exactly
what one gets by applying Selinger’s CPM construction [57] to Baez’ (implicit) category of pairs (H, J), H a finite-dimensional Hilbert space and J an anti-unitary with
J 2 = ±1 [7].
Another compact-closed subcateory of InvQM, which we might call InvCQM,
consists of universally embedded complex quantum systems Cn . It is interesting to note
that, in an hypothetical universe described by InvQM, the subcategory InvCQM acts
as a kind of “ideal”, in that if A ∈ InvQM and B ∈ InvCQM, then A B ∈ InvCQM
as well. This is provocative, as it suggests that such a universe, initially consisting of
many systems of all three types, might eventually evolve into one in which complex
systems greatly predominate.
Although it is not compact closed, the category RSE of reversible, standardly embedded EJCs remains of interest. This is still a monoidal category, and contains, in
addition to real and quaternionic quantum systems, orthodox complex quantum systems in their standard embedding (and composing in the normal way). Indeed, these
form a monoidal subcategory, CQM, which, again, functions as an “ideal”.
It is worth noting that the set of quaternionic quantum systems does not form a
monoidal subcategory of either RSE or InvQM, as the composite of two quaternionic
systems is real. Efforts to construct a free-standing quaternionic quantum theory have
had to contend with the absence of a suitable quaternionic composite of quaternionic
systems. For instance, as pointed out by Araki [5], the obvious candidate for the
composite of A = Mm (H)sa and B = Mn (H)sa , Mmn (H)sa , does not have a large
enough dimension to accommodate the real tensor product A ⊗ B, causing difficulty

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

45

<!-- page 46 -->
for the representation of product effects.29 In our approach, the issue simply doesn’t
arise. It seems that “quaternionic quantum mechanics” is best seen as an inextricable
part of a larger theory. Essentially the same point has also been made by Baez [7].
The category InvQM is somewhat mysterious. It encompasses real and quaternionic
QM in a completely natural way; however, while it also contains complex quantum
systems, these compose in an exotic manner: as pointed out above, the composite of two
complex quantum systems in InvQM comes with an extra classical bit — equivalently,
{0, 1}-valued superselection rule. This functions to make the transpose automorphism
of Mn (C)sa count as a morphism. The extra classical bit is flipped by the Jordan
transpose (swap of C ∗ summands) on either factor of such a composite, but unaffected
if both parties implement the Jordan transpose (which does, of course, effect a Jordan
transpose on the composite). The precise physical significance of this is a subject for
further study.
As Example 6.2 shows, there is no way to enlarge InvQM so as to include higher spin
factors, without either sacrificing compact closure (and even rendering the set C(A, I),
which might naturally be thought to represent states, trivial) or venturing outside the
ambient category of EJC-algebras, to make use of morphisms that are not (relatively)
completely Jordan-preserving maps. Example 6.3 shows, more strikingly, that there is
no way to construct a category of the form CJPC that contains standardly embedded
complex quantum systems and real systems, without, again, sacrificing compact closure
(indeed, the representation of states by morphisms).

References
[1] S. Abramsky and B. Coecke, Categorical quantum mechanics, in D. Gabbay, K.
Engesser and D. Lehman, Handbook of Quantum Logic and Quantum Structures vol
II, Elsevier, 2008; doi:10.1016/B978-0-444-52869.5001-4 arXiv:quant-ph/0402130)
[2] E. M. Alfsen and F. W. Shultz, State spaces of Jordan algebras, Acta Mathematica
140 (1978) 155-190 doi:10.1007/BF02392307
[3] E. M. Alfsen and F. W. Shultz, State Spaces of Operator Algebras: Basic Theory,
Orientations and C ∗ -Products, Birkhauser, 2001 doi:10.1007/978-1-4612-1047-2
[4] E. Alfsen and F. Shultz, Geometry of state spaces of operator algebras, Birkhäuser,
2003 doi:10.1007/978-1-4612-0019-2
[5] H. Araki, On a characterization of the state space of quantum mechanics, Comm.
Math. Phys. 75, 1980, 1-24 doi:10.1007/BF01962588
Attempts to interpret the quaternionic “Hilbert space” Hmn as a tensor product of Hm and Hn
raise at least the possibility of signaling via the noncommutativity of scalar multiplication. This
noncommutativity underlies the the argument in [50] that stronger-than-quantum correlations are
achievable in such a model.
29

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

46

<!-- page 47 -->
[6] C. Aliprantis and
doi:10.1090/gsm/084

D.

Toukey,

Cones

and

Duality,

Springer,

2007

[7] J. Baez, Division algebras and quantum theory, Foundations of Physics 42 819-855
(2012) doi:10.1007/s10701-011-9566-z arXiv:1101.5690
[8] J. Baez, Quantum quandaries: a category-theoretic perspective in D. Rickles, S.
French and J. Saatsi, Eds., The Structural Foundations of Quantum Gravity, Oxford,
2006, 240-265 (quant-ph/0404040
[9] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Cloning and broadcasting in generic
probabilistic theories, preprint, 2006 arxiv:quant-ph/0611295
[10] H. Barnum, J. Barrett, M. Leifer and A. Wilce, Teleportation in general probabilistic theories, in S. Abramsky and M. Mislove, Eds., Mathematical Foundations of
Information Flow (Proceedings of the Clifford Lectures 2008), Proceeding of Symposia in Applied Mathematics 71, American Mathematical Society, Providence,
2012, 25-48 doi:http://dx.doi.org/10.1090/psapm/071/600 arXiv:0805.3553
[11] H. Barnum, R. Duncan and A. Wilce, Symmetry, compact closure and dagger
compactness for categories of convex operational models, Journal of Philosophical
Logic 42 (2013) 501-523 doi:http://dx.doi.org/10.1007/s10992-013-9280-8 arXiv:
1004.2920
[12] H. Barnum, C. Gaebler and A. Wilce, Ensemble steering, weak self-duality and
the structure of probabilistic theories, Foundations of Physics 43 1411-1437 (2013)
doi:10.1007/s10701-013-9752-2; arxiv:0912.5532
[13] H. Barnum, M. Graydon and A. Wilce, Some Nearly Quantum Theories, EPTCS
195 (2015), 59-70 doi:10.4204/EPTCS.195.5 arXiv:1507.06278
[14] H. Barnum and J. Hilgert, Spectral properties of convex bodies, J. Lie Theory
30, 315-344 (2020). (ArXiv version: Strongly symmetric spectral convex bodies are
Jordan algebra state spaces arxiv:1904.03753 (2019))
[15] H. Barnum, M. Mueller and C. Ududec, Higher-order interference and singlesystem postulates characterizing quantum theory, New J. Physics 16 (2014)
doi:10.1088/1367-2630/16/12/123029 arXiv:1403.4147
[16] H. Barnum and A. Wilce, Information processing in convex operational theories, Electronic Notes in Theoretical Computer Science 270 (2011) 3-15
doi:10.1016/j.entcs.2011.01.002 arXiv:0908.2352
[17] H. Barnum and A. Wilce, Local tomography and the Jordan structure of
quantum theory, Found. Phys. 44 (2014), 192-212 doi:10.1007/s10701-014-9777-1
arXiv:1202.4513
[18] H. Barnum and A. Wilce, Post-classical probability theory, in G. Chiribella and R.
Spekkens, eds., Quantum Theory: Informational Foundations and Foils, Springer,
2017 doi:10.1007/978-94-017-7303-4 11; arXiv:1205.3833

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

47

<!-- page 48 -->
[19] J. Barrett, Information processing in generalized probabilistic theories, Physical
Review A 75 (2005) doi:10.1103/PhysRevA.75.032304 arXiv:quant-ph/0508211
[20] L. J. Bunce and J. D. Maitland-Wright, Introduction to the Ktheory of Jordan C ∗ algebras, Quart. J. Math. 40 (1989) 377-398
doi:http://dx.doi.org/10.1093/qmath/40.4.377
[21] G. Chiribella, M. D’Ariano and P. Perinotti, Informational derivation of quantum theory, Physical Review A 84 (2011), 012311 doi:10.1103/PhysRevA.84.012311
arXiv:1011.6451
[22] M. L. Curtis, Matrix Groups, Springer, 1984 doi:http://dx.doi.org/10.1007/978-14612-5286-3
[23] B. Dakic and C. Brukner, Quantum theory and beyond: is entanglement special?
in H. Halvorson, ed., Deep Beauty, Princeton, 2011 doi:10.1017/CBO9780511976971
arXiv:0911.0695
[24] E. B. Davies and J. Lewis, An operational approach to quantum probability,
Comm. Math. Phys. 17 (1970) 239-260 doi:10.1007/BF01647093
[25] C. M. Edwards, The operational approach to algebraic quantum theory I, Comm.
Math. Phys. 16 (1970), 207-230 doi:10.1007/bf01646788
[26] J. Faraut and A. Korányi, Analysis on Symmetric Cones, Oxford, 1994
[27] M. A. Graydon, Conical Designs and Categorical Jordan Algebraic Post-Quantum
Theories, Ph. D. Dissertation, University of Waterloo, 2017 arXiv:1703.06800
[quant-ph]
[28] M. A. Graydon, Quaternions and Quantum Theory, Master’s Thesis, University of
Waterloo, 2011
[29] H. Hanche-Olsen, JB algebras with tensor products are C ∗ algebras, in H. Araki et
al. (eds.), Operator Algebras and their Connections with Topology and Ergodic Theory, Lecture Notes in Mathematics 1132 (1985), 223-229 doi:10.1007/BFb0074886
[30] H. Hanche-Olsen, On the structure and tensor products of JC-algebras, Can. J.
Math. 35 (1983), 1059-1074 doi:http://dx.doi.org/10.4153/CJM-1983-059-8
[31] H. Hanche-Olsen and E. Størmer, Jordan Operator Algebras, Pitman, 1984 (Out
of print; available at https://folk.ntnu.no/hanche/joa/)
[32] L.
Hardy,
Quantum
theory
arXiv:quant-ph/0101012, 2001

from

five

reasonable

axioms,

[33] L. Hardy and W. Wootters”,”Limited holism and real-vector-space quantum theory, Found. Phys. 42 (2012) 454-473 doi:10.1007/s10701-011-9616-6
arXiv:1005.4870
[34] J. Hilgert, K. H. Hoffman and J. D. Lawson, Lie Groups, Convex Cones, and
Semigroups, Oxford, 1989

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

48

<!-- page 49 -->
[35] A. Holevo, Probabilistic and Statistical Aspects of Quantum Mechanics, Springer
Basel, 2011 doi:10.1007/978-88-7642-378-9
[36] F. B. Jamjoom, On the tensor products of JC-algebras, Quart. J. Math. Oxford
45 (1994) 77-90 doi:http://dx.doi.org/10.1093/qmath/45.1.77
[37] F. B. Jamjoom, On the tensor products of Simple JC algebras, Mich. Math. J. 41
(1994), 289-295 doi:http://dx.doi.org/10.1307/mmj/1029004996
[38] F. B. Jamjoom, On the tensor products of JW-algebras, Can. J. Math. 47 (1995)
786-8000 doi:http://dx.doi.org/10.4153/CJM-1995-040-1
[39] P. Janotta and R. Lal, Generalized probabilistic theories without the norestriction hypothesis, Phys. Rev. A. 87 (2013) doi:10.1103/PhysRevA.87.052131
arXiv:1302.2632
[40] Über die Multiplikation quantenmechanischer Größen, Zeit. Phys. 80 (1933), 285291. (Also see [41, 42].)
[41] P. Jordan, Über eine Klasse nichtassociativer hyperkomplexer Algebren,
Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, MathematischPhysikalische Klasse 33 (1932) 569-575,
[42] P. Jordan, Über Verallgemeinerungsmöglichkeiten des Formalismus Quantenmechanik, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen,
Mathematisch-Physikalische Klasse 39 (1933), 209-217
[43] P. Jordan, J. von Neumann and E. Wigner, On an algebraic generalization of the quantum mechanical formalism, Annals of Math. 35 (1934), 29-64
doi:10.2307/1968117
[44] M. Koecher, The Minnesota Notes on Jordan Algebras and their Applications, Ed.
A. Krieg and S. Walcher, Springer Lecture Notes in Mathematics 1710, Springer,
1999 doi:10.1007/BFb0096285
[45] Die Geodätischen von Positivitätsbereichen, Math. Ann. 135 (1958) 192-202.
doi:http://dx.doi.org/10.1007/BF01351796
[46] G. Ludwig, Deutung des Begriffs, “physikalische Theorie” und axiomatische
Grundlegung der Hilbertsraumstruktur der Quantenmechanik durch Hauptsätze des
Messens Springer Lecture Notes in Physics 4 1970
[47] G. Ludwig, An axiomatic basis for quantum mechanics. Volume 1: Derivation of
Hilbert Space Structure, Springer, 1985
[48] H. Neumann and A. Hartkämper, Eds., Foundations of Quantum Mechanics and
Ordered Linear Spaces, Springer, Lecture Notes in Physics 29, 1974 doi:10.1007/3540-06725-6
[49] H. Neumann, The structure of ordered Banach spaces in axiomatic quantum mechanics, in H. Neumann and A. Hartkämper, Eds., Foundations of Quantum Mechanics and Ordered Linear Spaces, Springer, Lecture Notes in Physics 29 (1974)
116-121 doi:http://dx.doi.org/10.1007/3-540-06725-6 13
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

49

<!-- page 50 -->
[50] M. McKague, Quaternionic quantum mechanics allows non-local boxes, Preprint,
arXiv:0911.1761, 2009
[51] Ll. Masanes and M. Müller, A derivation of quantum theory from physical requirements, New J. Phys. 13 (2011) doi:10.1088/1367-2630/13/6/063001
arXiv:1004.1483
[52] M. Mueller and Ll. Masanes, Information-theoretic postulates for quantum mechanics, in G. Chiribella and R. Spekkens, eds. Quantum Theory: Informational Foundations and Foils, Springer, 2016 doi:10.1007/978-94-017-7303-4 5;
arXiv:1203.451
[53] M. Müller and C. Ududec, The structure of reversible computation determines the self-duality of quantum theory, Phys. Rev. Lett. 108 (2012), 130401
doi:10.1103/PhysRevLett.108.130401 arXiv:1110.3516
[54] A. G. Robertson, Automorphisms of spin factors and the decomposition of positive maps, Quart. J. Math. Oxford Ser.
34 (1983) 87-96
doi:http://dx.doi.org/10.1093/qmath/34.1.87
[55] I. Satake, Linear embeddings of self-dual homogeneous cones, Nagoya Math. J. 46
(1972) 121-145 doi:10.1017/S0027763000014811
[56] I. Satake, Algebraic structures of symmetric domains, Publications of the Mathematical Society of Japan 14, Iwanami Shoten and Princeton University Press, 1980
[57] P. Selinger, Dagger compact categories and completely positive maps (extended
abstract), in Proceedings of the 3d International Workshop on Quantum Programming Languages (QPL 2005), Electronic Notes in Theoretical Computer Science
170 (2007) 139-163 doi:10.1016/j.entcs.2006.12.018
[58] A. M. Sinclair, Jordan homomorphisms and derivations of semi-simple Banach
algebras, Proc. Amer. Math. Soc. 24 (1970) 209-214 doi:10.2307/2036730
[59] E. Størmer, Jordan algebras of type I, Acta Math. 115 (1966), 165-184
doi:10.1007/BF02392206
[60] D. Topping, Jordan Algebras of Self-Adjoint Operators, Am. Math. Soc. Memoirs
53, Providence, 1965 doi:10.1090/memo/0053
[61] H. Upmeier, Derivations ofJordan C ∗ -algebras, Math. Scand. 46 (1980) 251-264
doi:10.7146/math.scand.a-11867
[62] E. Vinberg, Homogeneous cones, Dokl. Acad. Nauk. SSSR 141 (1960) 270-3. English translation: E. Vinberg (1961): Soviet Math. Dokl. 2, pp. 1416-1619.
[63] A. Wilce, Four and a half axioms for finite-dimensional quantum theory in
Y. Ben-Menahem and M. Hemmo (eds.), Probability in Physics, Springer, 2012
doi:10.1007/978-3-642-21329-8 17; arXiv:0912.5530

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

50

<!-- page 51 -->
[64] A. Wilce, Symmetry and self-duality in categories of probabilistic models, in B. Jacobs and P. Selinger, Eds., Proceedings of QPL 2011, Electronic Proceedings in Theoretical Computer Science 95 (2012) 289-293
doi:http://dx.doi.org/10.4204/EPTCS.95.19 arXiv:1210.0622
[65] A. Wilce, A royal road to quantum theory (or thereabouts), Entropy 20 (2018),
227-253 doi:10.3390/e20040227 arXiv:1606.09306
[66] A. Wilce, Conjugates, filters and quantum mechanics, Quantum 3 (2019) 158-191
doi:http://dx.doi.org/10.22331/q-2019-07-08-158 arXiv:1206.2897

A Direct Sums of EJAs
The first part of this Appendix collects some basic facts about direct sums of EJAs that
are used in the body of the paper. The second part contains a proof that C ∗ (A ⊕ B) =
C ∗ (A) ⊕ C ∗ (B), and that the direct sum of universally reversible EJAs is again UR.
Direct Summands and Central Projections The direct sum of EJAs A and B is
A⊕B := A×B, equipped with the slotwise operations, so that the canonical projections
π1 : A × B → A and π2 : A × B → B are unital Jordan homomorphisms. Identifying A
and B with A×{0} and {0}×B, respectively, we write a+b for (a, 0)+(0, b). Note that
A and B are then ideals in A ⊕ B, and that B = A⊥ := {z ∈ A ⊕ B|ha, zi = 0 ∀a ∈ A}.
Conversely, we will show that if E is an EJA and A is an ideal in A, then A⊥ is also
an ideal, and a b = 0 for all a ∈ A, b ∈ A⊥ ; hence, E ≃ A ⊕ A⊥ .
Suppose E is an EJA and A ≤ E is an ideal: let B = A⊥ . Then for all z ∈ E, a ∈ A
and b ∈ B,
ha, z bi = ha z, bi = 0

·

·

·
·
·

·

since a z ∈ A. Thus, B is also an ideal, and E = A ⊕ B as a vector space. Finally,
if a ∈ A and b ∈ B, then a b ∈ A ∩ B = {0}. Hence, if a, x ∈ A and b, y ∈ B then
(a + b) (x + y) = a x + b y, i.e., in the representation of A ⊕ B as A × B, operations
are slotwise. Note that u = pA + pB for a unique pA ∈ A and pB ∈ B. For a ∈ A we
have a pB = 0, so a = a u = a pA , whence pA = p2A and A = A pA . In other words,
we have

· ··
· ·

·

Lemma A.1. Let A be an ideal in an EJA E. Then there exists a projection p ∈ E
such that p a = a for every a ∈ A. Thus, A = p A, and E = p A ⊕ p0 A, where
p0 = 1 − p.

·

·

·

·

The center of an EJA E is the set of elements operator-commuting with all other
elements. Denote this by C(E). If E = A ⊕ B, and p is the unit of A, so that A = p A,
then it’s easy to check that p ∈ C(E). Conversely, if p is a central projection, then
p A is an ideal, with unit element p. If p is a minimal central projection, then p A is
a minimal direct summand of E. If E is simple, then its only central projections are 0
and 1, and conversely.

·

·

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

·

51

<!-- page 52 -->
One can show that for every projection p in an EJA E, there exists a unique minimal
projection c(p) ∈ C(E), the central cover of p, such that p ≤ c(p). Then A := c(p)E
is an ideal of E, in which c(p) is the unit. If A is a minimal ideal, then elements of A
are exactly those with central cover c(p) (see 2.37 and 2.39 in [4].) More generally, two
elements of E having the same central cover have nonzero components in exactly the
same ideals of E.
Recall that a symmetry of A is an element s ∈ A with s2 = u. Projections e, f in A
are exchanged by a symmetry s iff Us (e) = f . If there exists a sequence of symmetries
s1 , ..., sn with Usn ◦ · · · ◦ Us1 (e) = f , then e and f are equivalent.
Lemma A.2 ([4], Lemma 3.9). Equivalent projections have the same central cover.
The universal C ∗ -algebra of a direct sum Recall that a sequence of vector spaces
and linear maps, or of Jordan algebras and Jordan homomorphisms, or of C ∗ algebras
and ∗-homomorphisms
β
α
A −→ B −→ C
is said to be exact at B iff the image of α is the kernel of β. A short exact sequence is
one of the form
β
α
0 −→ A −→ B −→ C −→ 0
that is exact at A, B and C (with the maps on the ends being the only possible ones).
This means that α is injective (its kernel is 0), while β is surjective (its image is the
kernel of the zero map, i.e., all of C).
Let EJA and C ∗ be the categories of EJAs and Jordan homomorphisms, and of
∗
C -algebras and ∗-homomorphisms, respectively.
Theorem A.3 ([30]). A 7→ C ∗ (A) is an exact functor from EJA to C ∗ . In other
α

C ∗ (α)

β

C ∗ (β)

words, if A −→ B −→ C is an exact sequence in EJA, then C ∗ (A) −→ B −→ C ∗ (C)
is an exact sequence in C ∗ .
We are going to use this to show that C ∗ (A ⊕ B) = C ∗ (A) ⊕ C ∗ (B). We need some
preliminaries. The following is standard:
Lemma A.4. Let
α

β

0 −→ A −→ C −→ B −→ 0
be a short exact sequence of vector spaces. Then the following are equivalent:
(a) There is an isomorphism φ : A ⊕ B ≃ C such that α and β are respectively the
canonical injection and surjection given by
α(a) = φ(a, 0) and β(φ(a, b)) = b
(b) The sequence is split at B: there exists a linear mapping γ : B → C such that
β ◦ γ = idB .
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

52

<!-- page 53 -->
The idea is that, given φ, we can define γ by γ(b) = φ(0, b) and, given γ, we can
define φ by φ(a, b) = α(a) + γ(b).
If A, B and C are Jordan algebras or C ∗ algebras, the implication from (a) to (b)
is obviously valid, but the converse requires additional assumptions.
Lemma A.5. Let

β

α

0 −→ A −→ C −→ B −→ 0.
be a short exact sequence of ∗-algebras and ∗-homomorphisms, which is split by a ∗homomorphism γ : B → C with β ◦ γ = idB . Let φ : A ⊕ B → C be as defined above,
i.e, φ(a, b) = α(a) + γ(b) for a ∈ A, b ∈ B. Then the following are equivalent:
(a) γ(B) is a (2-sided) ∗-ideal in C;
(b) φ is multiplicative, and thus a ∗-isomorphism;
(c) There exists a ∗-homomorphism δ : C → A with
δ

γ

0 ←− A ←− C ←− B ←− 0
exact.
Proof: (a) ⇒ (b). It is easy to see that a C ∗ -algebra C is the direct sum of two ∗-ideals
A, B ≤ C iff A ⊕ B = C and A ∩ C = {0}, i.e., iff C is the vector-space direct sum of A
and B. We already know that α(A) + β(B) = C (since φ is a linear isomorphism). It
therefore suffices to show that α(A) and γ(B) are ∗-ideals with zero intersection. We
are assuming that γ(B) is a ∗-ideal. As it’s the kernel of a ∗-homomorphism, α(A) is
automatically a ∗-ideal. To see that α(A) ∩ γ(C) = {0}, let c ∈ C with c = α(a) = γ(b)
for some a ∈ A and b ∈ B. Then we have
b = β(γ(b)) = β(α(a)) = 0
whence, c = γ(0) = 0.
(b) ⇒ (c). If φ is a ∗-isomorphism, then let δ = πA ◦ φ−1 where πA : A ⊕ B → A is
the projection πA (a, b) = a. Note that δ is the composition of two ∗-homomorphisms,
and thus, a ∗-homomorphism. To verify exactness, note that as φ(a, b) = α(a) + γ(b),
we have φ(0, b) = γ(b), whence, φ−1 (γ(b)) = (0, b). Thus, δ(γ(b))= πA (0, b) = 0.
(c) ⇒ (a). By exactness, γ(C) is the kernel of the ∗-homomorphism δ, and hence,
a ∗-ideal. 
Now let E = A ⊕ B. Then we have a short exact sequence
j

p

0 −→ A −→ A ⊕ B −→ B −→ 0.
where j(a) = (a, 0) and p(a, b) = b. This is split by the homomorphism k : A → A ⊕ B
given by k(b) = (0, b). Hanche-Olsen’s exactness theorem, that is Theorem A.3, gives
us a short exact sequence
C ∗ (j)

C ∗ (p)

0 −→ C ∗ (A) −→ C ∗ (A ⊕ B) −→ C ∗ (B) −→ 0.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

53

<!-- page 54 -->
By functoriality, C ∗ (p) ◦ C ∗ (j) = idC ∗ (B) , so this is again split. Thus, regarded as a
vector space, C ∗ (A ⊕ B) is canonically isomorphic to C ∗ (A) ⊕ C ∗ (B). On the other
hand, we also have an exact sequence
q

k

0 ←− A ←− A ⊕ B ←− B ←− 0
where q(a, b) = a. By the same argument, then, we have a short exact sequence
C ∗ (q)

C ∗ (k)

0 ←− C ∗ (A) ←− C ∗ (A ⊕ B) ←− C ∗ (B) ←− 0.
Applying the preceding Lemma, we have
Proposition A.6. If A and B are EJAs, then
C ∗ (A ⊕ B) ≃ C ∗ (A) ⊕ C ∗ (B).
Notice that if ΦA and ΦB are, respectively, the canonical involutions on C ∗ (A) and
C ∗ (B) fixing points of A and B, then ΦA ⊕ΦB is a ∗-involution on C ∗ (A)⊕C ∗ (B) fixing
points of A ⊕ B. But there is only one such ∗-involution on C ∗ (A ⊕ B), the canonical
one. In other words, in identifying C ∗ (A ⊕ B) with C ∗ (A) ⊕ C ∗ (B), we also identify
ΦA⊕B with ΦA ⊕ ΦB .
Recalling now the fact ([30], Lemma 4.2) that an EJA A is universally reversible
(UR) iff A coincides with the set of self-adjoint fixed points in C ∗ (A) of the canonical
∗-involution ΦA , we have the following.
Corollary A.7. A ⊕ B is UR iff A and B are UR.
Proof: Let Φ = ΦA ⊕ ΦB be the canonical involution on C ∗ (A ⊕ B) = C ∗ (A) ⊕ C ∗ (B).
For (a, b) ∈ C ∗ (A)⊕C ∗ (B), we have Φ(a, b) = (ΦA (a), ΦB (b)) = (a, b) iff ΦA (a) = a and
ΦB (b) = b. Since A and B are UR, this holds iff a ∈ A and b ∈ B, i.e., iff (a, b) ∈ A ⊕ B.
Thus, A ⊕ B is exactly the set of fixed-points of Φ, and so, is UR.
Conversely, let A ⊕ B be UR. Suppose for a contradiction that one of A or B, say
B, is not UR: then there exists b ∈ C ∗ (B) such that ΦB (b) = b but b ∈
/ B. Let a be in
A. Then ΦA⊕B ((a, b)) ≡ (ΦA (a), ΦB (b)) = (a, b), whence by the fact that A ⊕ B is UR,
(a, b) ∈ A ⊕ B, but since b ∈
/ B this is in contradiction with the definition of A ⊕ B as
A × B equipped with a product. 
(One can also easily prove the above Corollary directly from the definition of universal reversibility, without using the canonical involutions.)

B The Quabit
In this appendix, we show that the canonical tensor product Q2 Q2 of two quabits
in their standard representation is R16 , the self-adjoint part of the real matrix algebra
M16 (R).
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

54

<!-- page 55 -->
The symplectic representation A quaternion q = a + bi + cj + dk can alternatively
be expressed in the form (a + bi) + (c + di)j, i.e., z + wj where z, w ∈ C, and also has
a standard representation as a 2 × 2 complex matrix, namely
"

[q] :=

z w
−w z

#

.

Treating H as a ∗-algebra over C, the mapping q 7→ [q] is a ∗-homomorphism from
H into M2 (C). This yields a natural representation — that is, ∗-homomorphism —
πo : Mn (H) → Mn (M2 (C)) ≃ M2n (C), given by
πo (a)p,q = [ap,q ]
for a ∈ Mn (H) and p, q = 1, ..., n. An equivalent, but for our purposes, more useful,
representation is given by
π(a)p,q = F πo (a)p,q F
where
1
 0

F =
 0
0


0
0
1
0

0
1
0
0

0
0 

.
0 
1


This is called the symplectic representation of Mn (H).
If we express each entry of a in the form ap,q = zp,q + wp,q j, then a = Γ1 + Γ2 j where
(Γ1 )p,q = zp,q and (Γ2 )p,q = wp,q . Computing, one finds that
"

π(a) =

Γ1 Γ2
−Γ2 Γ1

#

.

Notice that π(a) is self-adjoint iff Γ1 is self-adjoint and Γ2 is anti-symmetric, and that
this is the case iff a is self-adjoint in M2 (H).
From now on, we identify Q2 with π(M2 (H)sa ) ≤ M4 (C)sa . Regarded as an embedded EJA in this way, the canonical tensor product Q2 Q2 is defined to be the Jordan
subalgebra of the self-adjoint part of M4 (C) ⊗ M4 (C) = M16 (C) generated by Q2 ⊗ Q2 .
Our main goal in this Appendix is to prove
Proposition B.1. C ∗ (Q2

Q2 ) ≃ M16 (C).

Since Q2 Q2 is UR, this will follow from ([30], Theorem 4.4) if we can show that
(i) Q2 Q2 generates M16 (C) as a ∗-algebra, and (ii) there is a ∗-involution on M16 (C)
fixing elements of Q2 Q2 pointwise.
Quaternionic Pauli Matrices In order to show that Q2 Q2 generates M16 (C), we
begin by writing down some useful elements of Q2 . The analogues of the Pauli matrices

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

55

<!-- page 56 -->
σx , σy , σz ∈ M2 (C) are the following quaternionic Pauli matrices:
"

σ0 =
"

σ3 =

1 0
0 1

#

0 −i
i
0

#

"

σ1 =
"

σ4 =

1
0
0 −1

#

0 −j
j
0

#

"

σ2 =
"

σ5 =

0 1
1 0

#

0 −k
k
0

#

Evidently, σ1 , σ2 and σ3 are the standard Pauli matrices σz , σx and σy , respectively.
Note that these are all traceless and self-adjoint, and satisfy σa σb = δa,b σ0 where
a, b ∈ {1, ..., 5} — that is, σa and σb anti-commute if a 6= b, and σa squares to the
identity.
Applying the representation π gives us six elements of Q2 , s0 = π(σ0 ),
s1 = π(σ1 ), ..., s5 = π(σ5 ). Direct computation reveals that

·

"

s0 =
"

s3 =

1 0
0 1

#

"

= σ0 ⊗ σ0

σy
0
0 −σy

s1 =

#

"

= σz ⊗ σy

s4 =

σz 0
0 σz

#

0 −iσy
iσy
0

"

= σ0 ⊗ σz

s2 =

#

"

= σy ⊗ σy

s5 =

σx 0
0 σx

#

0 σy
σy 0

#

= σ0 ⊗ σx

= σx ⊗ σx

These again obey the Pauli-like identities mentioned above. Using these, we can compute (associative) products of these matrices, e.g.,
s3 s4 = (σz ⊗ σy )(σy ⊗ σy ) = σz σy ⊗ σy σy = −iσx ⊗ σ0 .
Lemma B.2. Q2 ⊗ Q2 generates M16 (C) as a ∗-algebra.
Proof: Begin by noting that the elements
σa ⊗ σb ⊗ σc ⊗ σc ,
where a, b, c, d ∈ {0, x, y, z}, are a basis for M16 (C). For each a ∈ {0, x, y, z}, let
x1 (a) = σa ⊗ σ0 ⊗ σ0 ⊗ σ0
x2 (a) = σ0 ⊗ σa ⊗ σ0 ⊗ σ0
x3 (a) = σ0 ⊗ σ0 ⊗ σa ⊗ σ0
x4 (a) = σ0 ⊗ σ0 ⊗ σ0 ⊗ σa
Then x1 (a)x2 (b)x3 (c)x4 (d) = σa ⊗ σb ⊗ σc ⊗ σd . These last form a basis for M16 (C), so
it will suffice to show that, for a ∈ {x, y, z}, the elements xp (a) can be manufactured
from elements of Q2 ⊗ Q2 by forming (associative) products.
For a start, notice that
s1 ⊗ s0 = σ0 ⊗ σz ⊗ σ0 ⊗ σ0 = x2 (z) and s0 ⊗ s1 = σ0 ⊗ σ0 ⊗ σ0 ⊗ σz = x4 (z).
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

56

<!-- page 57 -->
Similarly, with s2 in place of s1 , we have x2 (x) and x4 (x) in Q2
As noted above, s3 s4 = −iσx ⊗ σ0 . Similarly,

Q2 .

s3 s5 = iσy ⊗ σo and s4 s5 = −iσz ⊗ σo .
Hence,
(s3 ⊗ s4 )(s4 ⊗ s4 ) = s3 s4 ⊗ s4 s4 = −iσy ⊗ σ0 ⊗ σ0 ⊗ σ0 = −ix1 (y)
and similarly
((s3 ⊗ s5 )(s5 ⊗ s5 ) = ix1 (y) and (s4 ⊗ s5 )(s5 ⊗ s5 ) = −ix1 (z).
Thus, we have x1 (a) for all a. In an entirely similar way, we find that considering
(s3 ⊗ s3 )(s3 ⊗ s4 ) = −ix3 (y), (s3 ⊗ s3 )(s3 ⊗ s5 ) = ix3 (x), (s4 ⊗ s4 )(s4 ⊗ s5 ) = −ix3 (z).
So we have x3 (a) ∈ (Q2 Q2 )2 for all a.
It remains to obtain x2 (y) and x4 (y). But now we have
(s3 ⊗ s0 )x1 (z) = (σz ⊗ σy σ0 ⊗ σ0 )(σz ⊗ σ0 ⊗ σ0 ⊗ σ0 ) = x2 (y)
and similarly
x3 (z)(s0 ⊗ s3 ) = x3 (y).
Hence, x2 (y) and x4 (y) also belong to (Q2

Q2 )2 , completing the proof. 

An Involution We now wish to find an involution on M16 (C) fixing Q2 Q2 pointwise.
If φ : M → M is a ∗-involution on a complex ∗-algebra M, recall that we write Mφsa
for the set of self-adjoint fixed-points of φ. In finite dimensions, this is always an EJA.
Suppose φ and ψ are ∗-involutions on complex ∗-algebras M and N, respectively: if A
is a Jordan subalgebra of Mφsa and B is a Jordan subalgebra of Nψsa , then it’s easy to
see that A "B is a Jordan
subalgebra of (M ⊗ N)φ⊗ψ
sa .
#
0 −1
Let J =
. Then
1 0
φ(a) := −JaT J = −(JaJ)T
is a ∗-involution (a ∗-antiautomorphism of period two) on Mn (C). This fixes Q2
pointwise, i.e., φ(π(a)) = π(a) for every a ∈ M2 (H)sa . Identifying M16 (C) with
M4 (M4 (C)) = M4 (C) ⊗ M4 (C), we then have an involution
Φ = φ ⊗ φ : M16 (C) → M16 (C).
By the comments above, we have
Lemma B.3. Φ = φ ⊗ φ fixes every element of Q2

Q2 .

This completes the proof of Proposition B.1. Moreover, as a consequence of ([30],
Theorem 4.4), we have
Corollary B.4. Q2

Q2 = M16 (C)Φ .

Since C ∗ (A) ≃ M ≃ C ∗ (B) (as ∗-algebras with involution) implies A ≃ Mφsa ≃ B,
and since M16 (C) ≃ C ∗ (M16 (R)sa ), we have
Corollary B.5. Q2

Q2 ≃M16 (R)sa =: R16 .

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

57

<!-- page 58 -->
C Spin factors
The Jordan-von Neumann-Wigner Classification Theorem [43] singles out exactly three
classes of finite dimensional simple euclidean Jordan algebras: the matrix algebras
Rn , Cn , Qn , the exceptional Jordan algebra M3 (O)sa , and one further type. The remaining type were dubbed Spin Factors by Topping in [60]. For each finite N 3 n > 1,
there exists a unique spin factor of dimension 1 + n (up to Jordan isomorphism [31])
denoted by Vn . Abstractly, Vn is generated as a Jordan algebra by a spin system of
cardinality n: a collection of 2 ≤ n ∈ N symmetries (i.e. self-adjoint unitaries) sp
in a unital JB algebra A, with sp 6= ±uA such that sp sq = uA δp,q . It follows that
Vn ∼
= R ⊕ Rn as a real inner product space, and also as a euclidean Jordan algebra with

·



λ0 ⊕ ~λ

·

 



µ0 ⊕ ~µ = λ0 µ0 + h~λ, ~µi ⊕ λ0 ~µ + µ0~λ.

(6)

Concretely, the usual complex Pauli matrices can be used to define the spin factors.
We recall the usual complex Pauli matrices as follows
1
uC2 = σ0 =
0

!

!

0
1

1 0
σ1 =
0 −1

0
σ2 =
1

!

!

0 −i
σ3 =
.
i 0

1
0

(7)

Following [31], we define for each finite N 3 n > 1 and ∀1 ≤ p ≤ n, with b·c and d·e
the usual floor and ceiling functions

tp =


n − p
d p e−1


⊗b 2 c d 2 e

σ ⊗ 2

⊗ σ1 ⊗ σ0

3


p
n − p

−1


d
e

 ⊗ 2
⊗b 2 c d 2 e

σ
⊗
σ
⊗
σ

2
3
0



n − p


d p e−1


⊗d 2 e d 2 e
σ ⊗ 2


⊗ σ1 ⊗ σ0

3


p
n − p

−1

d
e

2
 ⊗
⊗d 2 e d 2 e

σ3

⊗ σ2 ⊗ σ0
0

p odd

n even

p even
(8)
p odd

n odd

p even
1

2

where our notation is such that x⊗ = 1 ∈ R, x ⊗ 1 = x = x⊗ , x⊗ = x ⊗ x, and so
on. One can easily check that for each n > 1, {t1 , . . . , tn } generates a spin factor of
dimension 1 + n with tp tq = (tp tq + tq tp )/2. It turns out [30], with finite k ∈ N, that
the maps

·

ψ2k : V2k −→ M2k (C)sa :: sp 7−→ tp
ψ2k+1 : V2k+1 −→ M2k (C)sa ⊕ M2k (C)sa :: sp 7−→ tp

(9)
(10)

are precisely the canonical injections of Vn into their universal C∗-algebras (i.e. their
universal representations). Our standard representation πn of Vn differs from the universal representation when n is odd. Specifically, when n is even we define vp = tp , and

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

58

<!-- page 59 -->
when n is odd we define ∀1 ≤ p < n
vp =


d p e−1

σ ⊗ 2
⊗σ
3

⊗b 2 c
1 ⊗ σ0
n

p

 ⊗d 2 e−1
σ
⊗σ

3

vn = σ3⊗

d p2 e

−

n − p
⊗b 2 c d 2 e

2 ⊗ σ0

p odd

(11)

p even

b n2 c

(12)

and we embed Vn into its standard C∗-algebra via the following Jordan monomorphism
with vp vq = (vp vq + vq vp )/2

·

⊗b 2 c
πn : Vn −→ M2 (C)sa
:: sp 7−→ vp .
n

(13)

For example, the universal and standard representations for the qubit — i.e. V3 — differ
as follows
t1 = σ1 ⊗ σ0
t2 = σ2 ⊗ σ0
t3 = σ3 ⊗ σ1

v1 = σ1
v2 = σ2
v3 = σ3

(14)
(15)
(16)

hence the name standard representation. Incidentally, note that V3 ∼
= C2 as a euclidean
∼
∼
Jordan algebra. Furthermore, V2 ∼
R
,
V
Q
,
and
V
M
= 2 5 = 2
9 =
2 (O)sa ; the ambient
spaces for the real, quaternionic, and octonionic quantum bits.

D Weak Composites
By a weak composite of EJAs A and B, we mean an EJA AB and a bilinear mapping
π : A ⊗ B → AB satisfying parts (a) and (b), but not necessarily part (c), of Definition
4.1. That is, we suspend the requirement that AB be generated, as a Jordan algebra,
by π(A ⊗ B). We are going to show that the Jordan subalgebra of AB generated by
the image of A ⊗ B in AB also satisfies these conditions, and hence, is a composite in
the strict sense.
Observe, first, that we made no use of Condition (c) in proving any of the results
leading up to, and including, Corollary 4.4. So all of these are also satisfied by weak
composites.
Proposition D.1. Let AB be a weak composite of EJAs A and B. Then the Jordan
subalgebra of AB generated by A ⊗ B is also a composite.
Proof: Identifying A ⊗ B with its image, π(A ⊗ B), in AB, let A B = J(A ⊗ B)
denote the Jordan subalgebra of AB generated by A⊗B. That the co-restriction π : A⊗
B → A B satisfies the conditions for a composite (Definition 2.1) is straightforward.
It is also straightforward that A B will satisfy the conditions for a composite of
Jordan models (Definition 4.1), provided that it satisfies the conditions for a dynamical
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

59

<!-- page 60 -->
composite (Definition 2.3). To see that it does, let φ ∈ G(A) and ψ ∈ G(B). We need
to show that φ ⊗ ψ preserves A B. We can expand φ as Ua ◦ g and ψ as Ub ◦ h for
some interior elements a ∈ A+ , b ∈ B+ , and Jordan homomorphisms g ∈ G(A) and
h ∈ G(B) ([26], III.5.1). Now
φ ⊗ ψ = (Ua ◦ g) ⊗ (Ub ◦ h) = (Ua ⊗ Ub ) ◦ (g ⊗ h).
Since (g ⊗ h)(uAB ) = g(uA ) ⊗ h(uB ) = uA ⊗ uB = uAB , g ⊗ h is a symmetry, hence,
a Jordan automorphism of AB ([4], Theorem 2.8). As it maps A ⊗ B to itself, it also
preserves J(A ⊗ B), i.e., A B.
It remains to show that Ua ⊗ Ub also preserves A B. Begin with the observation
that if A is an EJA and X ⊆ A, then for all x ∈ X, Ux (J(X)) ⊆ J(X). This is
evident from the fact that, as x ∈ J(X) and the latter is a Jordan subalgebra of A,
Ux (y) = 2x (x y) − (x2 ) y for all y ∈ J(X).
Now consider that the proof of the identities (a ⊗ u) (x ⊗ y) = (a x) ⊗ y and
(u ⊗ b) (x ⊗ y) = x ⊗ (b y) relies only on (a) and (b), and so, holds in our context. By
Corollary 4.4, Ua⊗u = Ua ⊗ id and Uu⊗b = idA ⊗ Ub . If a, b are interior elements, then
Ua ∈ G(A) and Ub ∈ G(B), so by (b), we have

··

·

·

·

·

·

Ua ⊗ Ub = (Ua ⊗ idB ) ◦ (idA ⊗ Ub ) = Ua⊗uB ◦ UuA ⊗b .
Since Ua⊗uB and UuA ⊗b preserve J(A ⊗ B) = A
Ua ⊗ Ub , and the proof is finished. 

B, by the remark above, so does

E Extending order automorphisms
In this appendix, for the reader’s convenience, we collect facts concerning extensions of
derivations used in the body of this paper. Throughout, A is an EJC algebra, that is,
a Jordan subalgebra of Msa , where M is a finite-dimensional complex matrix algebra.
We begin by recalling some facts about order-automorphisms and Jordan derivations
([4], Chapter 6).
If {φ(t)}t∈R is a one-parameter group of order-automorphisms of A, then for every
a ∈ A, φ(t)(a) = etδ a where δ = φ0 (0) is a linear operator on A. The linear operators
δ arising in this way are called order derivations of A. Order-derivations come in two
basic types: those having the form δ = La for some a ∈ A and those having the property
δ(u) = 0. The latter are exactly the Jordan derivations of A, that is, the linear maps
A → A satisfying the Leibniz law δ(a b) = δ(a) b + aδ(b) for all a, b ∈ A. Order
derivations of the form La are said to be self-adjoint; those that are Jordan derivations
are said to be skew. The former are self-adjoint with respect to the canonical inner
product on A, by the definition of a euclidean Jordan algebra, while the latter are
skew-adjoint. Every order-derivation has the form δ = La + δ 0 where δ 0 is skew ([4],
Proposition 1.60). It follows that φ := etδ fixes the Jordan unit uA iff δ is skew.
A mapping δ : M → M is said to be an order-derivation of M iff it preserves Msa
and its restriction to Msa is an order derivation in the sense discussed above. If a ∈ M,

·

·

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

60

<!-- page 61 -->
define δa : M → M by

1
δa (x) = (ax + xa∗ ).
2
Then δa is an order derivation in this broader sense. Moreover, every order-derivation
of M has this form for some a ∈ M ([4], Appendix 183.) Note that δa is self-adjoint
precisely when a is self-adjoint and skew precisely when a is skew-adjoint. In the
latter case, a direct computation shows that δa is actually a ∗-derivation of M, that is,
δa (xy) = δa (x)y + xδa (y) and δa (x∗ ) = δa (x)∗ .
The following essentially restates Lemma 5.3:
Lemma E.1. Any Jordan derivation of A extends to a ∗-derivation of M. Hence, any
order-derivation of A extends to an order-derivation of M.
Proof. The set of derivations of a finite-dimensional real or complex algebra is a Lie
algebra, and in the case of a Jordan algebra A, it is the linear span of the elements
[La , Lb ], for a, b ∈ A, in fact every derivation is a sum of such elements.30 Since La and
Lb are linear operators A → A, [La , Lb ] belongs to the real associative algebra of such
operators. Since A is a subalgebra of (MA )sa , La and Lb extend to linear operators
(MA )sa → (MA )sa , namely the Jordan multiplication operators corresponding to a
and b viewed as elements of (MA )sa . But as noted above, every Jordan derivation of
MA is also a ∗-derivation for the associative product, establishing the first claim. A
∗-derivation on M preserves Msa , and is also a Jordanderivation on the latter, so this
also establishes that all skew order derivations on A extend to order-derivations of M.
A self-adjoint order derivation of A is simply a map La : A → A with a ∈ A, which
extends to δa : M → M since a is self-adjoint in M. Thus, all order-derivations on A
extend to order-derivations on M. 

Lemma E.2. Any one-parameter group of order automorphisms of A extends to a
one-parameter group of order-automorphisms of M.
Proof: If {φ(t)}t∈R is a one-parameter group of order-automorphisms of A, then φ(t)(a) =
etδ a where δ = φ0 (0) is an order-derivation of A. Thus, we have δ = La + δ 0 where a ∈ A
and δ 0 is skew ([4], Proposition 1.60). La obviously extends from A to M, simply because a ∈ M and the Jordan product on A is the restriction of that on M. By Lemma
5.3, δ 0 also extends to a Jordan derivation δ 00 on M. Thus, we have an extension
δb = La + δ 00 on M. In particular, δ 00 (A) ⊆ A. We now have an order-automorphism
b
φ(t)
= etδb of M+ . Note that this preserves A, since
b
φ(t)x
=

∞
X

tk bk
δ x
k=1 k!

·

b = (L + δ 00 )x = a x + δ 00 (x), which belongs to A if x does. 
and δx
a
30

See e.g. [26], Proposition II.4.1 for the fact that these are derivations, called inner derivations. In
[61], for example, it is said to be well-known that all derivations of a finite-dimensional JB algebra (i.e.
an EJA) are inner.
Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

61

<!-- page 62 -->
Corollary E.3. Every element of G(A) extends to an element of G((MA )sa ).
Lemma E.4. Let A and B be EJC-algebras. If δ is any ∗-derivation of MA fixing A,
then δ ⊗ 1 is a ∗-derivation of MA ⊗ MB fixing A B.
Proof: Let M and N be ∗-algebras, and let a, b ∈ M and x, y ∈ N. Then

·

1
(a ⊗ x) (b ⊗ y) = (ab ⊗ xy + ba ⊗ yx).
2
If δ is a ∗-derivation of M, then it is straighforward to check that δ ⊗ 1 is a ∗-derivation
of M ⊗ N, and that for all a, b ∈ M and x, y ∈ N,

·

·

·

(δ ⊗ 1)((a ⊗ x) (b ⊗ y)) = (a ⊗ x) (δ(b) ⊗ y) + (δ(a) ⊗ x) (b ⊗ y).

·

In particular, if A ⊆ M and δ(A) ⊆ A, it follows that (δ ⊗1)(A⊗B) ⊆ (A⊗B) (A⊗B)
for any B ⊆ N. It follows easily that, where A and B are EJCs and M = MA and
N = MB , δ ⊗ 1 preserves A B. 31
Proposition E.5. If φ and ψ are order-automorphisms in G(A) and G(B), respectively,
then φ ⊗ ψ: A ⊗ B → A ⊗ B extends to an order-automorphism in G(A B).
Proof: By Corollary E.3, we can assume that φ is an order-automorphism of Msa fixing
A. Since φ ∈ G(A), it occurs as part of a one-parameter group φ(t) = etδ of orderautomorphisms, say as φ = φ(1) = eδ , where δ is an order-derivation of A. By Lemma
E.1, δ extends to an order derivation of M fixing A. It follows that
φ ⊗ 1 = etδ ⊗ 1 =

∞ n
X
t
n=0 n!

δn ⊗ 1 =

∞ n
X
t
n=0 n!

(δ ⊗ 1)n = et(δ⊗1) .

By Lemma E.4, δ ⊗ 1 fixes A B; thus, so does the series at right, whence, so does
φ ⊗ 1. It follows that if φ is an order-automorphism of (MA )sa fixing A, so φ ⊗ 1 is an
order-automorphism of A ⊗ B fixing J(A ⊗ B) = A B. Hence, if φ and ψ are orderautomorphisms of MA and MB , respectively fixing A and B, then φ⊗ψ = (φ⊗1)◦(1⊗ψ)
fixes A B. 

31

The details: let δ be a ∗-derivation on a ∗-algebra M, and let X ⊆ Msa with δ(X) ⊆ X. Let
Y = {a ∈ J(X)|δ(a) ∈ J(X)}. Evidently X ⊆ Y . Now if a, b ∈ Y and t ∈ R, then δ(ta + b) =
tδ(a) + δ(b) ∈ J(X), so J(X) is a subspace of M . If a, b ∈ Y then δ(a b) = a δ(b) + δ(a) b ∈ J(X).
Thus, Y is a Jordan subalgebra of Msa , containing X, and contained in J(X). Ergo, Y = J(X), and
δ(J(X)) ⊆ J(X).

·

·

Accepted in Quantum 2020-10-07, click title to verify. Published under CC-BY 4.0.

·

62
