---
type: paper
date: 2019-04-07
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1904.03753v1)
reviewed: false
---

# Strongly symmetric spectral convex bodies are Jordan algebra state spaces

Machine-generated and unreviewed text extraction of arXiv:1904.03753v1
(78 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1904.03753v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:1904.03753v1 [math-ph] 7 Apr 2019

Strongly symmetric spectral convex bodies are
Jordan algebra state spaces
Howard Barnum∗1 and Joachim Hilgert†2
1 Los Alamos, New Mexico, USA
2 Department of Mathematics, University of Paderborn, Germany

April 9, 2019

Abstract
We show that the finite-dimensional convex compact sets having the
properties of spectrality and strong symmetry are precisely the normalized
state spaces of finite-dimensional simple Euclidean Jordan algebras and the
simplices. Various assumptions are known characterizing complex quantum
state spaces among the Jordan state spaces, which combine with this theorem to give simple characterizations of finite-dimensional quantum state
space.
Spectrality and strong symmetry arose in the study of “general probabilistic theories” (GPTs), in which convex compact sets are considered as
state spaces of abstractly conceivable physical systems, though not necessarily ones corresponding to actual physics. We discuss some implications
of our result—which is purely convex geometric in nature—for such theories. A major concern in the study of such theories, and also in the theory
of operator algebras, has been the characterization of the state spaces of
finite and infinite-dimensional Jordan algebras, and the characterization of
standard quantum theory over complex Hilbert spaces, or the state spaces
of von Neumann or C∗ -algebras, within the class of Jordan-algebraic state
∗
†

hnbarnum@aol.com
hilgert@math.upb.de

<!-- page 2 -->
2
spaces. In the finite-dimensional case, our characterization of simple Jordanalgebraic state spaces and classical (i.e. simplicial) state spaces, can serve
as an alternative to existing characterizations of Jordan-algebraic systems,
for example via the properties of positive projections associated with faces
[1, 2].
While our result is purely convex-geometric in nature, it has strong implications for work relating geometric properties of the state spaces of systems to physical and information processing characteristics of GPT theories.
It shows that some generalizations of important aspects of quantum and classical thermodynamics to theories satisfying natural postulates, e.g. in [3, 4],
apply to a narrower class of theories than might have been hoped, already
relatively close to complex quantum theory since their systems are Jordan
algebraic. Sorkin’s notion of irreducibly k-th order interference, involving k
or more possibilities, generalizing the interference between two possibilities
in quantum theory, has been studied in the GPT framework and looked for in
experiments. Our result shows that the assumption of no higher-order (k ≥ 3)
interference, used along with spectrality and strong symmetry to characterize the same class of Jordan-algebraic convex sets in [5], was superfluous.
It also implies that [6]’s extension, on the assumption that interference
is no
√
greater than some fixed maximal degree k, of the important Ω( N) lower
bound on the quantum black-box query complexity of searching N possibilities for one having a desired property (which is achieved by Grover’s celebrated quantum algorithm), to a class of GPTs satisfying certain postulates
allowing the formulation of a generalized notion of query algorithm actually applies in the Jordan-algebraic setting where higher-order interference
(k ≥ 3) is not possible.
On the other hand, our work suggests that whether one is interested in
investigating the physical and information properties of possible probabilistic theories or in the geometric properties of convex compact sets, it is worth
focusing on the implications of postulates weaker than the conjunction of
strong symmetry and spectrality.

1 Introduction
In [5], the normalized state spaces of simple finite-dimensional Euclidean Jordan
algebras, and the simplices, were characterized as the unique finite-dimensional
compact convex sets satisfying three properties: spectrality, strong symmetry, and
the absence of higher-order interference. In this paper, we show that the same
class of convex compact sets is characterized by the first two of these properties:

<!-- page 3 -->
3
Theorem 1.1. A finite-dimensional convex compact set is spectral and strongly
symmetric if and only if it is a simplex or affinely isomorphic to the space of
normalized states of a simple Euclidean Jordan algebra.
Simplices are the state spaces of particular nonsimple Euclidean Jordan algebras, namely products of several copies of the trivial (one-dimensional) Euclidean
Jordan algebra, so this theorem implies the claim in our title.
Spectrality (in this convex sense) and strong symmetry are notions originating
in an area of research, now often called “general probabilistic theories” (GPTs),
that considers convex compact sets as an abstract notion of state space of a system, physical or otherwise, on which one can make measurements, attempt to
control the dynamics, etc.; a state encodes the probabilities of the results of all
measurements that it is possible to make on a system. Roughly speaking, a system specified by a convex compact state space Ω is spectral if every state is a
convex combination of pure (i.e. extremal, in the convex sense) states that are
perfectly distinguishable from each other via some measurement it is possible to
perform on the system. A system is strongly symmetric if the symmetry group of
its state space acts transitively on the set of lists (of a given length) of perfectly
distinguishable states. These two properties are convex abstractions of properties that hold for quantum systems: in the quantum case, the state space is the
set of density matrices on a Hilbert space, perfectly distinguishable sets of states
are the sets of rank-one projectors (pure density matrices) vv† corresponding to
orthonormal sets of Hilbert space vectors v (modulo phase factors), spectrality is
the spectral decomposition of density matrices, and strong symmetry reflects the
facts that any orthonormal basis can be taken to any other via a unitary operator
and that conjugations by unitaries, ρ 7→ U ρ U †, are symmetries of the set of density matrices. Although much of quantum physics is best represented in infinitedimensional Hilbert spaces, quantum information theory has focused on degrees
of freedom that can be represented in finite-dimensional Hilbert spaces, or on
controlling finite-dimensional subalgebras of observables in larger systems, corresponding to effective finite-dimensional Hilbert spaces, e.g. ones describable as
tensor products of two-dimensional complex Hilbert spaces (“qubits”). And most
of the characteristically quantum phenomena such as interference, tradeoffs between information gain and disturbance in the measurement process, the existence
of incompatible observables, and entanglement, that are associated with the cryptographic and computational advantages of quantum information processing over
classical, are already present in finite-dimensional systems. So finite-dimensional
results such as those of the present paper can help us understand the conceptual

<!-- page 4 -->
4
and physical basis of such quantum phenomena. Indeed most recent research on
general probabilistic theories has been done in finite-dimensional settings.
That simple Euclidean Jordan algebras and simplices are spectral and strongly
symmetric is known (cf. [5]), so the new result here is the converse. It is obtained
by showing that compact convex sets in finite dimension satisfying spectrality and
strong symmetry are (up to affine isomorphism) a subset of the regular convex
bodies, defined in [7] as bodies whose symmetry group acts transitively on maximal chains of faces, and using the classification of those convex bodies in [8] to
verify that this subset consists precisely of the abovementioned classes of sets.
Several recent works have explored the consequences of the conjunction of
spectrality and strong symmetry, or sets of principles that imply these, for the
state space of a system
√ in the GPT framework. In particular, in [6], the important
lower bound of Ω( N) queries (due to Bennett, Brassard, Bernstein, and Vazirani
[9]) on computing OR (that is, x1 ∨ x2 ∨ · · · ∨ xN ) via quantum queries to an N-bit√
string (x1 , x2 , · · · , xN ) ∈ {0, 1}N , which shows that one cannot improve on the N
queries used in Grover’s quantum algorithm for “searching” over N possibilities
for one having a desired property, was extended to systems satisfying a set of
five postulates. These postulates include strong symmetry, and imply (by results
in [10]) spectrality. In [3], the conjunction of strong symmetry and spectrality
was shown to imply thermodynamical results generalizing important facts about
quantum thermodynamics, and similar results were obtained in [4]. Our work
implies that these recent results, as well as additional results on query complexity
obtained in [11], apply to a much smaller set of GPT systems than might have
been hoped. We discuss this further in the concluding section of the paper.
The paper is organized as follows. After this outline of the paper’s structure,
Section 1.1 briefly describes some terminological and mathematical conventions
used in the rest of the paper. Section 2 provides the necessary background on
convex compact sets and associated structures, especially their groups of automorphisms, and defines the notion of measurement, which is used in formulating the notion of perfect distinguishability and the properties of spectrality and
strong symmetry which depend on it. It also touches on the use of this framework to represent potential physical systems abstractly, which motivates notions
like measurement, distinguishability, spectrality, and strong symmetry. Section
3 defines perfect distinguishability, spectrality and strong symmetry, and reviews
important consequences (mostly from [5]) of the latter two properties that will be
needed in proving the main theorem. Section 4 describes the main class of convex
compact sets that are the target of the characterization via spectrality and strong
symmetry in the main theorem: the normalized state spaces of simple Euclidean

<!-- page 5 -->
5
Jordan algebras. It also reviews the already-known direction of the main theorem
for these cases, explaining how known results in Jordan theory imply that these
state spaces are spectral and strongly symmetric. Finally, it reviews the structure of these Jordan algebras considered as representations of the automorphism
groups of their normalized state spaces, and of the automorphism groups of the
cones over these state spaces. This structure will be used in the proof of the main
theorem in Section 9, to compare them with the polar representations in which
Madden and Robertson [8] embed all regular convex bodies in order to classify
them. Section 5 briefly reviews the easily seen fact that simplices, the other part
of the class of bodies we characterize, are spectral and strongly symmetric, which
completes the proof of the “if” direction of the main theorem. Section 6 establishes, via a direct and simple geometric argument essentially from [12] (but also
using strong symmetry which was not explicitly assumed there), the “only if” direction for the special case of strongly symmetric spectral systems in which no
more than a pair of states can be perfectly distinguished at once: they are affinely
isomorphic to balls. This enables us to avoid some case-checking later. Section
7 introduces the main tools we will use in the new part of our characterization
theorem: the notion of regular convex body and associated theory, and Section 8
describes the classification by Madden and Robertson [8] of these bodies as convex hulls of particular orbits in polar representations of compact groups, along
with some of the theory of polar representations used in the classification. The
classification uses a one-to-one correspondence (which was described in Section
7) which associates each regular convex body Ω embedded as the convex hull of
an orbit in a polar representation with a polytope π (Ω) given as the convex hull
of a particular orbit of the “restricted Weyl group” of the representation, acting
in a subspace a, with π (Ω) = a ∩ Ω. Finally, Section 9 completes the proof of
the characterization theorem by proving the new part: that all strongly symmetric
spectral convex compact sets are normalized state spaces of simple Jordan algebras, or simplices. This is done by first proving that they are regular, and then
that the associated polytope π (Ω) is a simplex. We then go through the list of
representations in the Madden-Robertson classification of regular convex bodies,
and verify that all of those (other than the simplices themselves) whose polytope
is a simplex with three or more vertices occur in polar representations of automorphism groups of Euclidean Jordan algebras acting on those algebras. We compare
the representation-theoretic description of the orbits leading to normalized Jordan
state spaces from Section 4, to the description of the points whose orbits yield
the regular convex body in the Madden-Robertson construction, and see that, up
to an affine transformation, they are the same. Section 10 discusses the implica-

<!-- page 6 -->
6
tions of the result for GPTs, including recent work assuming strong symmetry and
spectrality; discusses several simple and physically or informationally meaningful ways of adding additional assumptions to further narrow the class of systems
to that of standard complex quantum theory, and also discusses the relation of
the present work to other characterizations of Jordan-algebraic state spaces, and
Section 11 briefly concludes.

1.1 Some mathematical terminology
A few terminological conventions and definitions are worth noting. We will sometimes abuse notation by referring to a singleton set, {x}, by the name of its element x, especially when {x} is the face of a convex set consisting of the single extremal point x. For S any subset of an inner product space V, ( · , · ) we
define S⊥ := {x ∈ V : ∀y ∈ S (x, y) = 0}. We also adopt the common practice
whereby, when we substitute a set in a place in an expression where an element
of the set is expected, the expression is taken to refer to the set of all its referents when elements of the set are substituted in that place. For example, for S
a subset of an inner product space V , {x : (x, S) = 0} has the same meaning as
{x : ∀y ∈ S (x, y) = 0}, i.e. it refers to S⊥; for G a group acting on a set S, G.x for
fixed x ∈ S is the orbit through x, and so forth.
We use the notation En to indicate n-dimensional Euclidean space, by which
we mean a finite-dimensional real vector space equipped with a distinguished positive definite inner product (a concrete example is Rn equipped with the dot product). When S is a subset of a real affine space or linear space, we use the notation
Conv S for the convex hull of S, i.e. the set of all convex combinations of elements
of S.
For any group G acting linearly on a vector space V , and any subspace L of
V , we denote the subgroup that preserves the subspace L by GL , and the subgroup
that fixes L pointwise by GL . (NG (L) and ZG (L) are also common notation for
these.) We write G0 for the connected identity component of a Lie group G, and
Gs0 for the semisimple part of G0 .
We write := or =: to indicate that the expression on the side with the colon is
defined by the expression on the side with the equals sign, both when defining an
expression for the first time and in occasional reminders. Finally, as is common
in the literature, we use “positive” to mean “nonnegative”.

<!-- page 7 -->
7

2 Background and framework
We study convex compact subsets Ω of finite-dimensional real affine spaces A.
From now on the term “convex compact set” refers to such sets. Unless otherwise
noted, it refers to full-dimensional sets, i.e. ones whose affine span, Aff Ω, is A.
We will be concerned with intrinsic properties of such a set, which are invariant
under affine transformations. In this setting, unlike the setting of compact convex subsets of Euclidean space (defined as a finite-dimensional real vector space
with positive definite inner product), there is no way of distinguishing a notion of
rectangle from that of square or parallelogram, for example; a trapezoid, however,
represents a distinct affine isomorphism class from the other three.
Some intrinsic properties of convex compact sets are best formulated by embedding Aff Ω as an affine hyperplane, not containing the origin, in a real vector space V of dimension one greater than the dimension, which we’ll call n, of
Aff Ω. The properties we study are independent of the particular embedding.
Such an embedding determines the convex, topologically closed, pointed, generating cone1 V+ := R+ Ω, its dual cone V+∗ ⊂ V ∗ , and a unique u in the interior of
V+∗ , defined by the property that u(Ω) = 1 (meaning u(ω ) = 1 for all ω ∈ Ω).
Definition 2.1. Let a compact convex set Ω of dimension n be embedded in an
affine hyperplane in V \ {0} where V is a vector space of dimension n + 1, as
above. We call V+ := R+ Ω ⊂ V the cone over Ω, the cone generated by Ω, or
Cone (Ω).2 We call the unique u ∈ int V+∗ defined by the property that u(Ω) = 1,
the order unit associated with Ω.3
We also define the cone generated by S, sometimes writing it as Cone (S),
for general subsets S of a real vector space V , as the set of nonnegative linear
combinations of elements of S; in the special case of S = Ω in the setting of
Definition 2.1 this agrees with the definition given there. For our purposes, a
cone C is defined to be a subset of a real vector space, closed under addition and
1 These concepts will be defined below.
2 Note that V by itself does not determine Ω; different choices of u ∈ int V ∗ give rise to dif+
+
ferent bases for V+ , which need not in general be affinely isomorphic. For example, a cone with
square base also has trapezoidal bases, obtained for example by swinging the hyperplane containing the square base around one edge of the square (which we can think of as a “hinge”). V+ , on
the other hand, is determined (up to affine isomorphisms) by Ω in the above construction (independently of the particular embedding of Aff Ω into V \{0}).
3 The term comes from the theory of order-unit and base-norm Banach spaces; see for example
[13, 1].

<!-- page 8 -->
8
nonnegative scalar multiplication. It is called generating if it spans the vector
space, and pointed if C ∩ −C = {0}. The cones obtained from Definition 2.1
are pointed, generating, and topologically closed. For reasons that will become
clearer later, sometimes V ∗ is referred to as the observable space.
An important interpretation of this formalism, which was the motivation and
setting of [5], views Ω as the space of normalized states of an abstract physical
system. This may or may not correspond to the state space of any system in physical theories currently in use. Because of this interpretation, we sometimes use the
terms “state” for elements of Ω, and “pure state” for extremal elements of Ω. For
instance, for finite-dimensional quantum systems corresponding to a Hilbert space
of finite dimension d, Ω, of affine dimension d 2 − 1, is the set of density matrices
(i.e. unit-trace positive semidefinite d × d complex Hermitian matrices). The pure
states are the rank-one density matrices (which are the Hermitian projectors onto
one-dimensional subspaces of the underlying Hilbert space). The cone V+ is the
positive semidefinite matrices.
An (n − 1)-simplex in an affine space is the convex hull of n affinely independent points; if x1 , ..., xn are such points, we write △(x1 , ..., xn) for this simplex.
The (n − 1) in (n − 1)-simplex refers to its dimension, equal to the dimension of
the affine space it spans. All k-simplices are affinely isomorphic; the abstract ksimplex, i.e. the affine equivalence class of such simplices, or an arbitrary such
simplex considered only up to affine equivalence, is often referred to as △k . In
the “operational” or GPT interpretation, the (n − 1)-simplex is often thought of as
a finite-dimensional classical state space. The associated vector space V of one
higher dimension is usually taken to be Rn , with the extremal points xi embedded
as the unit coordinate vectors ei = (0, 0, ..., 0, 1, 0, ...0) with 1 in the i-th place, so
that △n−1 is identified with the standard probability simplex.
The barycenter (also known as centroid) c(Ω) of a full-dimensional compact
convex set Ω ⊂ A, where dim A = dim Ω = n, is defined by introducing coordinates
so as to identify A with Rn , and letting:
c(Ω) :=

Z

Ω

d µ (x)x

(1)

where d µ is Lebesgue measure on Rn . One shows that c(Ω) is independent of the
particular coordinatization of A as Rn , and (what amounts to the same thing) that
c(Ω) is covariant under affine transformations, i.e. for any affine transformation
T , it holds that c(T (Ω)) = T (c(Ω)).
The automorphism group, Aut Ω, of Ω is the set of affine transformations of
Aff Ω that take Ω onto itself. It is a compact group. (This is often called Ω’s

<!-- page 9 -->
9
symmetry group but (mainly for consistency with [7, 8]) we’ll reserve that term
for use in a slightly different context to be introduced later.) We’ll often denote
it with the letter K. In the GPT literature, its elements are often called reversible
transformations. Any affine space can be viewed as a vector space by choosing
a point to be 0; it is natural to do this for Aff Ω by taking the barycenter of Ω as
zero. (This should not be confused with the extension of Aff Ω to the vector space
V described above, which is of one greater dimension.) The transformations in
Aut Ω, because they are affine, fix the barycenter, so with respect to this vector
space structure on Aff Ω, they are linear. They also extend (as do any affine
transformations on Aff Ω) linearly to all of V . We may also refer to the extension
as Aut Ω, or as K (K and its extension are of course isomorphic as groups). In fact
we have:
Proposition 2.2. Let Ω be a compact convex subset of A ≃ Aff Ω. A may be
equipped with the structure of a Euclidean space E in such a way that Aut Ω ⊆
O(E). In doing so, the barycenter of Ω becomes 0 ∈ E, and Aut Ω is precisely the
subgroup of O(E) that preserves Ω.
This follows from the well-known fact that if a compact group K acts linearly
on a real vector space V , there exists a K-invariant inner product on V 4 and the
fact that Aut Ω is a compact group that fixes c(Ω) (Proposition 2.4).
Definition 2.3. We call the identification of Aff Ω with a Euclidean vector space E
such that Aut Ω ⊆ O(E) ≡ O(Aff Ω) a canonical embedding of Ω into Euclidean
space.
Recalling the construction of the cone V+ ⊂ V over Ω in Definition 2.1, we
note that we can also equip V with an inner product so that K’s extension to V is
a subgroup of O(n + 1). This subgroup will fix the ray R+ c(Ω), i.e. the ray over
the image of 0 := c(Ω) under the embedding of Aff Ω into V . With this choice
of inner product, and identifying V ∗ with V via the inner product, u ∈ V is the
embedded image of 0 ∈ E ≃ Aff Ω.
The following fact is very useful:
Proposition 2.4. Let K :=RAut Ω act transitively on the extreme boundary ∂e Ω of
Ω, and let ω ∈ ∂e Ω. Then K d µ (k)k.ω = c(Ω), where d µ is Haar measure on K.
c(Ω) is the unique K-invariant point in Ω.
4 One proves this by verifying that if h., .i : V × V → R :: (x, y) 7→ hx, yi is an arbitrary inner

product on V , then (x, y) 7→
invariant inner product.

R

K dkhkx, kyi, where dk is normalized Haar measure on K, is a K-

<!-- page 10 -->
10
The property in the premise of this proposition, transitive action of Aut Ω
on ∂e Ω, is sometimes called reversible transitivity on pure states. A convex set
with the property is also sometimes called an orbitope, following [14]. When
the compact group and representation K are clear, we will sometimes refer to
Conv K.ω as the orbitope over ω or the orbitope generated by ω . If the connected
identity component of Aut Ω acts transitively on ∂e Ω, we say Ω has continuous
reversible transitivity.
The next two definitions are essential for defining the central properties we
will investigate: spectrality and strong symmetry.
Definition 2.5. An effect is an element of the interval [0, u] ⊆ V+∗ , with respect
to the (partial) ordering of V ∗ induced by V+∗ (namely, x ≥ y := x − y ∈ V+∗ ). A
measurement is a finite sequence ei , i ∈ {1, ..., m} of effects such that ∑m
i=1 ei = u.
An equivalent characterization of effects is as precisely the elements of V ∗
that satisfy, for all ω ∈ Ω, ei (ω ) ∈ [0, 1] ⊂ R. (While the first clause only requires
them to be in V ∗ , the rest of the definition implies they are positive, i.e. in V+∗ .) In
the operational interpretation effects, since they give probabilities when evaluated
on states, are used to mathematically represent the probabilities of outcomes of
measurements. The definition of measurement guarantees that for every state ω ∈
Ω, the probabilities ei (ω ) for the outcomes 1, . . ., m of a measurement e1 , ..., em
sum to 1: ∑i ei (ω ) = u(ω ) = 1.
Since we are in finite dimension, a positive definite inner product ( · , · ) : V ×
V → R induces (as does any nondegenerate bilinear form, positive definite or not)
an isomorphism between V ∗ and V . It is common to use such an inner product
to represent the dual space “internally” in the primal space; then the dual cone
becomes V+∗internal := {y ∈ V : ∀x ∈ V+ , (y, x) ≥ 0}. We say that a cone V+ is selfdual if there exists an inner product with respect to which V+∗internal = V+ .5 We
will call such an inner product self-dualizing.
When, as in much of this paper, we deal with self-dual cones, we will normally fix a self-dualizing inner product, use it to identify V with V ∗ and drop the
superscript “internal”.
A face of a convex set C is a convex subset F such that whenever x = ∑i pi xi ,
with pi > 0, is a finite convex decomposition of x ∈ F in terms of xi ∈ C, all the xi
are in F. An exposed face is the intersection of C with a supporting hyperplane;
5 This is a properly stronger property than affine isomorphism of V ∗ with V , which is some+
+

times called “weak self-duality”. The cone with square base, for example, separates the two
properties.

<!-- page 11 -->
11
it is easily shown to be a face, but the two notions are not equivalent. Where
necessary we modify these definitions so that (1) C itself is considered to be an
exposed face as well as a face, and (2) the empty set is considered to be an exposed
face, and a face, when C is compact, but not when C is a cone. This gives a
bijection ϕ between the faces of the cone V+ ≡ R+ Ω ⊂ V over Ω, and the faces of
a convex compact set Ω: for each face G of R+ Ω, ϕ (G) := G ∩ Aff Ω is a face of
Ω. ϕ ’s inverse takes each nonempty face H of Ω to the face R+ H of G, and ∅ to
{0}. There is an analogous bijection in the case of exposed faces. When ordered
by inclusion, the set of faces and the set of exposed faces are each lattices, in which
we write the least upper bound (“join”) of a pair x, y of elements as x ∨ y, and their
greatest lower bound (“meet”) as x∧y. In any lattice, meet and join are associative.
For any subset S of a convex set C, we define the face generated by S, face(S) as
the smallest face that contains S. (Of course it must be shown unique for this to
be an admissible definition; it is.) So for a pair of elements face({x, y}) = x ∨ y,
and by associativity of join, for a finite set of elements, face({x1 , ...., xk}) = x1 ∨
x2 ∨ · · · ∨ xk . A similar notion applies to the lattice of exposed faces: ExpFace(S),
the exposed face generated by S, is the smallest exposed face containing S. When
several convex sets may coexist in the same space, we may use the name of a set as
a subscript to indicate which convex set we are generating a face in, e.g. faceC (S)
is the face of C generated by S.
Both the set of faces and the set of exposed faces of a compact convex set Ω
or of a (pointed, closed, generating) cone V+ , are bounded lattices. Their upper
bounds are Ω (resp. V+ ), and lower bound ∅ (resp. {0}). 6
A cone V+ is said to be perfect if V can be equipped with an inner product
such that every face F of V+ , including V+ itself, is equal to its dual with respect
to the restriction of the inner product to lin F.7
In the literature on general probabilistic theories, systems are sometimes modeled using an explicit specification of a proper subset of the sets of effects and of
measurements, or positive maps, subject to reasonable conditions, called the “allowed” or “physical” effects, measurements, or positive maps. When the full set of
effects is allowed, the system is said to satisfy the “no-restriction hypothesis”. We
are concerned with intrinsic properties of the compact convex set Ω which cannot
depend on such a choice, so we have no need of this possibility. We mention it
6 The face lattice is an affine invariant of compact convex sets, but does not fully separate affine

equivalence classes of compact convex sets, as the fact that a cone and its base have isomorphic
face lattices, but the cone does not in general determine its base up to affine equivalence, illustrates.
7 The cone with pentagonal base (indeed, the cone over any regular n-gon with odd number of
vertices greater than 3) illustrates that this is properly stronger than self-duality.

<!-- page 12 -->
12
because the framework used in [5] does allow for the possibility of a restricted set
of allowed effects, and the notions of spectrality and strong symmetry in [5] are
defined as we define them here except that the notion of perfect distinguishability
used is with respect to the set of allowed effects. In principle this could affect
the notions of spectrality, and of strong symmetry, for a fixed state space. However, the conjunction of spectrality and strong symmetry, even with respect to a
restricted set of effects, is shown in [5] to imply no-restriction. All of the results
we use from [5] concern consequences of the conjunction of these two properties,
so they hold equally for strongly symmetric spectral sets in our more specialized
setting.

3 Distinguishability, spectrality, and strong symmetry
In this section we continue to use Ω to refer to an arbitrary finite-dimensional
compact convex set.
Definition 3.1. A set of points ωi , i ∈ {1, ..., k} in Ω is called perfectly distinguishable if there is a measurement {ei }, i ∈ {1, ..., k} such that ei (ω j ) = δi j .
In the operational interpretation, perfect distinguishability means that if we are
guaranteed that a physical system has been prepared in one of the states ω1 , .., ωk ,
but we do not know which one, we may ascertain which one was prepared with
perfect certainty by doing the measurement {ei }. If we get the result j, then
the state that was prepared must have been ω j . Perfect distinguishability, and
approximations to it, are central to considerations of the information storage and
processing properties of abstract systems in this interpretation.
An equivalent characterization of distinguishability will also be useful to us.
We call an indexed set of effects E = {ei } a submeasurement if ∑i ei ≤ u. For each
submeasurement E = {e1 , ..., er }, the indexed set E ′ := {e1 , ..., er , er+1 }, where
er+1 := u − ∑ri=1 ei , is a measurement. We could have equally well defined perfect
distinguishability of ω1 , ..., ωr as the existence of a submeasurement such that
ei (ω j ) = δi j , for it is easy to see that er+1 (ωi ) = 0 for all i ∈ {1, .., r}, whence
there are many ways of constructing an r-outcome measurement {e′1 , ..., e′r } such
that ei (ω j ) = δi j —for instance, let e′1 = e1 + er+1 , and e′i = ei for all i ∈ {2, ..., r}.
Definition 3.2. [5] A sequence ω1 , ..., ωk of perfectly distinguishable pure states
is called a frame, or a k-frame if we wish to specify its cardinality.

<!-- page 13 -->
13
In GPT models in which restricted sets of allowed effects are specified, as
done in [5], distinguishability and frames are usually defined with respect to the
allowed effects, so fewer sets of states may be distinguishable, and there may
be fewer frames, than in the no-restriction case. Although we referenced [5] for
the above definitions, we have defined distinguishability, and hence all concepts
dependent on it, with respect to the set of all effects. So for us, these notions
depend only the convex geometry of Ω.
Definition 3.3. A frame in Ω is called maximal if it is not a subsequence of any
other frame.
Although the cardinality of a frame can be no greater than n + 1 (recall that
n := dim(Aff Ω)), for a given Ω the maximal cardinality of a frame may be much
less than n.8
We are now ready to introduce the two properties of convex sets that we will
use in our characterization theorem.
Definition 3.4 ([5]). A convex compact set Ω is called spectral if, for each point
ω ∈ Ω, there is some frame whose convex hull contains ω .9
This is a very strong property of convex compact sets. Jordan algebraic state
spaces satisfy a stronger property, called unique spectrality, which requires that
for any two convex decompositions ω = ∑ki=1 pi ωi = ∑ri=1 qi τi of ω into the elements ωi , τi of two frames, k = r and there exists a permutation σ of {1, ..., k} such
that qσ (i) = pi . Unique spectrality was not assumed in [5] and will not be assumed
in our characterization theorem either, but it follows [5] from the conjunction of
spectrality and the next property, strong symmetry.
Definition 3.5. A convex compact set Ω of dimension n is called strongly symmetric if, for each k ∈ {1, ..., n + 1}, Aut Ω acts transitively on the set of k-frames.
8 An example of the latter phenomenon is the mixed-state space (the density matrices) of a d-

dimensional quantum system, where as mentioned before, dim(Aff Ω) = d 2 − 1. The frames are
just lists of mutually orthogonal rank-one projectors, and the cardinality (length) of a largest such
list is d, which is far from achieving the general upper bound of n + 1 which is here d 2 . Modulo
reorderings a simplex has a unique maximal frame, the set of vertices of the simplex; the frames
of a simplex are just the ordered subsets of the vertices, i.e. finite sequences, without repetition, of
vertices. In this case, the general upper bound is achieved.
9
There are other notions of spectrality for convex compact sets in the literature, for instance
Alfsen and Shultz’s ([1], Definition 8.74). Although related, Alfsen and Shultz’s notion should not
be confused with the one used here. However the conjunction of our weak notion of spectrality
with strong symmetry also implies [5] that Ω is spectral in Alfsen and Shultz’s sense. Riedel [15]
also introduced a notion of spectral ordered linear space, but we will not use it here.

<!-- page 14 -->
14
Note that the set of k-frames may well be empty for many values of k (in which
case, trivially, Aut Ω acts transitively on it).
“Strong symmetry” was the term introduced in [5]. “Frame-symmetric” or
“frame-transitive” might have been a better choice. The notion of frame that is
involved in the definition of strong symmetry is not itself obviously symmetryrelated. And for sets having few frames, it is actually not a very strong symmetry
requirement.
Since a k-frame is a finite sequence of perfectly distinguishable pure states,
strong symmetry implies that one can arbitrarily permute the elements of any set
of perfectly distinguishable pure states, via symmetries. It is therefore at least
prima facie a stronger property than requiring that every set of perfectly distinguishable pure states (which we might call an unordered frame) can be mapped
onto any other such set of the same size by a symmetry.10
We collect some more consequences of the conjunction of spectrality and
strong symmetry in the following proposition.
Proposition 3.6 (Mostly from [5]). For a convex compact set Ω that is spectral
and strongly symmetric, the following hold:
1. Every face of Ω is generated by a frame. Any two frames that generate the
same face F have the same cardinality, which we call the rank, |F|, of the
face. If the face G is a proper subset of F, then |G| < |F|.
2. Every face of Ω is exposed.
3. The cone V+ := R+ Ω over Ω is a perfect self-dual cone. The self-dualizing
inner product (., .) can be chosen to be Aut Ω-invariant, and such that
(ω , ω ) = 1 for all pure states (extremal points) ω of Ω.
4. With respect to the self-dualizing inner product on V , the elements of any
frame are an orthonormal set. The states of a frame, viewed as elements
of the dual space via this inner product, are effects, and are therefore a
distinguishing submeasurement for that frame. If ω1 , ..., ωn is a maximal
frame, i.e. a frame for Ω, then ∑ni=1 ωi is the order unit.
10 The pentagon (like any regular n-gon with n > 3) provides an example of a non-spectral but

strongly symmetric convex compact set. Spectral but not strongly symmetric convex compact sets
also abound: for example, any ball is easily smoothly deformed to another smooth, strictly convex
set with trivial automorphism group; all smooth, strictly convex sets are spectral.

<!-- page 15 -->
15
5. If F = ω1 ∨ · · · ∨ ωk for some frame ω1 , ..., ωk (equivalently, F is the face
generated by that frame) then the barycenter of F is ∑ki=1 ωi /k. (It follows
that ∑ki=1 ωi does not depend on which frame ω1 , ..., ωk for F is summed
over.)
6. If F is a face of V+ , (resp. Ω) then F ′ := F ⊥ ∩V+ (resp. F ⊥ ∩ Ω) is a face
of V+ (resp. Ω) such that F ∧ F ′ = {0} (resp. F ∧ F ′ = ∅) and F ∨ F ′ = V+
(resp. F ∨ F ′ = Ω). (Here all ⊥’s and linear spans are taken in V , with
respect to the self-dualizing, invariant inner product.) In a lattice, these two
conditions define what it means for an element F ′ to be a complement of F,
so we call F ′ the face complementary to F, or simply F’s complement.
7. The face generated by a maximal frame is Ω itself. Every frame A of Ω,
generating a face F, extends to a maximal frame M, by appending a frame
B for F ′ . Similarly if F < G (i.e. F ( G), every frame for F extends to a
frame for G.
8. The map F 7→ F ′ on the face lattice of V+ (equivalently of Ω) is an orthocomplementation, with respect to which the lattice is orthomodular, i.e. for
F ≤ G, G = F ∨ (F ′ ∧ G). The additional states appended to a frame on
F in order to extend it to a frame on G (cf. item 7 above), are a frame for
F ′ ∧ G.
We may think of orthomodularity as stating that F ′ ∧ G behaves as a “relative
orthocomplement” of F in G, i.e. an orthocomplement in the sublattice consisting
of elements below or equal to G.
Proof. Item 1 is Proposition 2 of [5]. Item 2 follows easily from item 1.
Item 3 is established in [5] in the course of proving Theorem 8 of that paper,
which states that for every face F, the orthogonal projection (with respect to the
self-dualizing Aut Ω-invariant inner product) PF onto the linear span of a face
F, is a positive map. Iochum [16] showed that for self-dual cones, positivity of
all such projections with respect to a self-dualizing inner product is equivalent
to perfection. The self-duality of the cones R+ Ω ⊂ V over strongly symmetric
spectral convex sets, with respect to an inner product with the stated properties,
was established as Proposition 3 of [5].11
11 In fact self-duality does not require spectrality, nor does it require the full strength of strong

symmetry: in [17] it was shown that transitivity of Aut Ω on 2-frames (ordered pairs of perfectly
distinguishable states) implies self-duality.

<!-- page 16 -->
16
Item 4 is Proposition 6 of [5].
Item 6 is partly stated in Proposition 7 of [5], and the rest can be extracted
from the proof of that Proposition.
Item 7 is part of Proposition 7 of [5].
Item 8 begins with the claim that the map ′ is an orthocomplementation. A
complementation is an involutive map of a bounded lattice such that F ∨ F ′ = 1
and F ∧ F ′ = 0. It is called an orthocomplementation if it is order-reversing:
F ≤ G ⇔ G′ ≤ F ′ . The involutiveness of ′ is also part of Proposition 7 of [5]. The
other two conditions on a complementation are part of item 6 above. The last part
of orthocomplementation, order-reversingness, is shown as part of the proof of
Theorem 9 in [5]; it follows directly from the extendibility of frames to maximal
frames.
The second part of item 8, i.e. orthomodularity, is Theorem 9 of [5]. The
crucial element in its proof (given that we have already established that ′ is an
orthocomplement) is the “relative frame extension property”, i.e. the last sentence
in item 7. The last sentence of item 8 is a step in this proof from [5].
The only item we have not covered yet is item 5. It does not appear to be explicitly stated in [5], although it is likely known. We include a proof in Appendix
B, as part of a proof that the faces of strongly symmetric spectral sets are strongly
symmetric and spectral.

4 A class of examples: strongly symmetric spectral
convex sets from simple Euclidean Jordan algebras
Finite-dimensional Euclidean Jordan algebras were introduced by Pascual Jordan
around 1932 [18], as a possible algebraic setting for the formalism of quantum
theory. The notion abstracts properties of the complex Hermitian matrices, which
are the observables12 of a finite-dimensional quantum system; in particular, properties of the symmetrized product A • B := (AB + BA)/2 which, unlike the ordinary associative matrix product, preserves Hermiticity. Our main result asserts
that we can identify, up to affine isomorphisms, the spaces of normalized states
of a certain class of these algebras with the strongly symmetric spectral convex
compact sets. So in this section, we will introduce these algebras, define their
12 As noted in Section 2, in the setting of general probabilistic theories, a reasonable generaliza-

tion of the space of observables is the vector space V ∗ .

<!-- page 17 -->
17
normalized state spaces, and give their classification so that we can identify them
when they appear in the classification of regular convex bodies (as defined in 7.6) .
We also give the proof, mainly consisting of references to known results, that they
are strongly symmetric and spectral, since this is one direction (the already-known
one) of our main theorem. Finally, we explain that the action of the automorphism
group of the normalized state space on the subspace where it acts nontrivially, is
via a polar representation, indeed a symmetric space representation, and identify
a point in the representation, the convex hull of whose orbit is the normalized
state space. This will be used in Section 9 to connect these state spaces with the
Madden-Robertson classification of regular convex bodies, since the latter proceeds by showing that their symmetry groups’ actions can be induced by polar
representations.
Our main reference for facts about Euclidean Jordan algebras and the associated cones will be Chapters I-V of the book of Faraut and Koranyi [19], which
deals with symmetric cones in finite dimension. We also refer to Chapter I of
[20].13
A Jordan algebra is a real algebra (i.e., a real vector space V equipped with a
bilinear product • : V ×V → V ) that is commutative and that, while not in general
associative, satisfies a special case of associativity, the Jordan property: a2 • (a •
b) = a • (a2 • b), where we use the notation a2 := a • a. It need not have a unit,
but one can always be adjoined if it is absent. We will consider only unital finitedimensional Jordan algebras. A Jordan algebra is called formally real if a2 + b2 =
0 implies that a = b = 0. In finite dimension, formal reality coincides with another
property, Euclideanity. A Jordan algebra (V, •) is said to be Euclidean if it is
possible to introduce an inner product ( · , · ) : V ×V → R that is “associative”, i.e.
(a • b, c) = (a, b • c).
The set of squares in a Jordan algebra is obviously closed under nonnegative
scalar multiplication. In a formally real (equivalently Euclidean), Jordan algebra,
it is also closed under addition, so it is a convex cone (cf. e.g. [19], Ch III §2),
13 [19] is the most elementary and the most focused on our concerns, but because it is very

detailed, relevant material is occasionally somewhat scattered and one sometimes needs to chase
chains of definitions and theorems. Satake’s Chapter I [20] is succinct and extremely well organized, but uses notions somewhat more general than we need (e.g. Jordan triple systems), and also
uses some machinery from algebraic geometry and algebraic groups. Another good reference,
but less focused than the other two on the concerns of this paper, and somewhat more involved
because it also covers infinite-dimensional cases, is the first part of [1]. The spectral theorem is
Theorem 2.20 on p. 46. Neither this nor Satake’s chapter is as explicit as [19] about frames and
frame-transitivity.

<!-- page 18 -->
18
which we call V+ . It is immediate from formal reality that V+ is pointed. Since
it is in addition topologically closed, it has a compact convex base, giving an
example of the formalism of compact convex sets embedded as bases of regular
cones, described in Section 2, and permitting an “operational” interpretation as
the state space of a physical system. V+ is self-dual with respect to the associative
inner product.
Soon after Jordan introduced them, Jordan, von Neumann and Wigner [21]
classified the finite-dimensional formally real Jordan algebras. They are precisely
the n × n self-adjoint matrices with entries in R, C, or H and the 3 × 3 octonionic
self-adjoint matrices, equipped in each case with symmetrized matrix multiplication x • y = (xy + yx)/2 as Jordan product, and the spin factors Rn ⊕ R for every
n ≥ 1, equipped with the product
(x, s) • (y,t) = (tx + sy, hx, yi + st).

(2)

Here x, y ∈ Rn , s,t ∈ R. Self-adjoint (“Hermitian” is also used) means M = M † ,
t
where M † := M , and M’s entries are the conjugates of M’s with respect to the
canonical conjugation on R, C, H, or O. The conjugation is the identity in the
case of R, thus the self-adjoint real matrices are just the real symmetric matrices.
Although we do not make direct use of them in obtaining our results, important
facts about the positive cones of Euclidean Jordan algebras are (1) the KoecherVinberg theorem [22, 23] 14 that the cones of squares in finite-dimensional formally real Jordan algebras are precisely the homogeneous self-dual cones (homogeneity being defined as transitive action of the automorphism group of the cone
on the interior), and (2) the result that they are precisely the symmetric cones,
i.e. the regular cones whose interiors are Riemannian symmetric spaces ([25]; see
also [23]).

4.1 Normalized Jordan algebra state spaces: spectrality and
strong symmetry
Now we define the normalized state spaces of Euclidean Jordan algebras (which
we will henceforth sometimes abbreviate as “EJAs”), and explain how to show the
known fact that they are spectral and strongly symmetric.
Recall that an idempotent in an algebra is an element c such that c2 = c, and it
is called primitive if it is not a nontrivial sum of other idempotents.
14 Proofs may also be found in [20], Ch. I Theorem 8.5, [19], Theorem III.3.1, and [24].

<!-- page 19 -->
19
Definition 4.1. A Jordan frame is defined to be a complete set of orthogonal primitive idempotents ci in a Euclidean Jordan algebra, where orthogonality means that
ci • c j = δi j ci and completeness means ∑i ci = e, the unit of the algebra.
Theorem 4.2 (Spectral theorem for finite-dimensional Euclidean Jordan algebras). Every element x of a Euclidean Jordan algebra has a decomposition
r

x = ∑ λi ci

(3)

i=1

where λi ∈ R and ci are a Jordan frame. When we rewrite this as
x = ∑ λα cα ,

(4)

α

where cα := (∑i∈α ci ) and the sets α ⊆ {1, ..., r} are a partition of the indices into
the largest subsets within which λi =: λα is constant, then the decomposition (4),
into not-necessarily-primitive idempotents, is unique.
This is a combination of Theorems III.1.1 and III.1.3 in [19].
The values λα are the spectrum of x. We can define the trace of x ∈ V as
∑i λi , and the determinant as Πi λi , where λi are the coefficients in the spectral
decomposition (3). Using the trace we define a bilinear form (x, y) := tr (x • y) on
the Jordan algebra. Proposition III.1.5 of [19] states that the positive definiteness
of this form (making it an inner product) is equivalent to Euclideanity. Indeed,
in a simple Euclidean Jordan algebra every associative inner product is a positive
scalar multiple of this one.
Definition 4.3. In a Euclidean Jordan algebra V , the squares satisfying tr x =
1 form a compact convex base Ω for the cone V+ of squares. We call this the
normalized state space of V .
Proposition 4.4 (e.g. [19], Corollary IV.3.2). The primitive idempotents are precisely the extremal points of Ω.
In a Euclidean Jordan algebra V the spectrum of a square is nonnegative. One
usually represents the dual space internally using the trace inner product. Since
tr x = tr (e • x) ≡ (e, x), we then have that e is the order unit for this choice of base.
Proposition 4.5. The normalized state spaces of finite-dimensional Euclidean
Jordan algebras are spectral.

<!-- page 20 -->
20
Proof. The primitive idempotents of an EJA V are precisely the extremal points of
its normalized state space Ω. Since the cone is self-dual, and all idempotents are
below or equal to the order unit e,15 they are also effects. Orthogonality of primitive idempotents in the sense ei • e j = 0 of Definition 4.1 implies orthogonality
with respect to the inner product, tr ei • e j = 0, so any subset of a Jordan frame,
considered as a set of effects, is a submeasurement that perfectly distinguishes the
same subset, considered as states. Consequently, an ordered subset of a Jordan
frame (and in particular, an ordered Jordan frame itself) is a frame in the sense of
Definition 3.2. So the spectral theorem implies spectrality.
In order to complete the proof of strong symmetry, we also show:
Proposition 4.6. All the frames in an EJA state space are ordered subsets of Jordan frames.
This is known, and implicitly assumed in [5], but we give a proof.
Proof. Since ∂e Ω is the set of primitive idempotents, and V+ is self-dual with respect to the inner product ha, bi = tr a • b, a frame is a sequence ci , i ∈ {1, . . ., s}
of primitive idempotents such that there exists a submeasurement ei for which
hei , c j i = δi j . In a general setting, not only in Jordan state spaces, it follows immediately from the condition hei , ω j i = δi j on a frame that if ei = ∑k pk fk is a
convex decomposition of ei into effects fk , each of the fk also has the property
fk (ω j ) = δk j . So the condition that ωi is a frame may be restated as the existence
of a submeasurement consisting of extremal (in the convex body [0, u]) effects.
Proposition 1.40 of [1] states that the extreme points of the positive part [0, u]
of the unit ball of a JB-algebra are the idempotents. The finite-dimensional JBalgebras are the EJAs. It is also known (cf. [1], Proposition 2.18) that for idempotents pi , ∑ki=1 pi ≤ u implies that pi ⊥ p j for all i, j ∈ {1, . . . , k} with i 6= j. So in
the condition for ci to be a frame, we may take the ei to be a mutually orthogonal
set of idempotents. We show that hei , ci i = 1 for an idempotent ei and a primitive
idempotent ci implies that ci ≤ ei . To do so we use the fact, from [1], that JBalgebras V are equipped with normalized self-adjoint idempotent positive linear
maps Pp : V → V called compressions, in bijection with the idempotents p, such
that p = Ppe and the exposed faces (all faces in finite dimension) are the positive
parts of the images of compressions. We have 1 = hei , ci i = hPei e, ci i = he, Pei ci i.
Since it follows from Proposition 1.41 (in finite dimensions, where the dual space
15 An easy argument from the spectral theorem gives that every primitive idempotent is part of
a Jordan frame, and it is part of the definition of Jordan frame that it sums to the order unit.

<!-- page 21 -->
21
may be identified with the primal space) of [1] that compressions on an EJA
are neutral, i.e. ||Pω || = ||ω || =⇒ Pω = ω , we have that Pei ci = ci , hence
ci ∈ im+ Pei , where the latter is defined as im Pei ∩ V+ . By Lemma 1.39 of [1],
im+ Pei ∩ [0, e] = [0, ei ], and since ci ∈ [0, e], we have ci ≤ ei .
With ci ≤ ei , and ei ⊥ e j for all i 6= j, it follows that ci ⊥ c j for all i 6= j, and
consequently that the ci are a subsequence of an ordered Jordan frame.
Proposition 4.7. The normalized state space of a Euclidean Jordan algebra is
strongly symmetric.
Proof. Corollary IV.2.7 of Theorem IV.2.5 in [19] states that the compact group K,
defined as the subgroup of Aut 0 (V+ ) that fixes the Jordan unit e, acts transitively
on the set of Jordan frames. Since we’ve adopted a canonical inner product, this is
a subgroup of Aut Ω. It is clear from the proof of Theorem IV.2.5 in [19] that this
transitive action is on ordered Jordan frames. Since we showed, in the proof of
Proposition 4.5 and in Proposition 4.6, that the frames (in the sense of Definition
3.2) are precisely the ordered subsets of Jordan frames, the group K, and hence
Aut Ω, acts transitively on the set of k-frames for each k.
In particular, we have the following:
Corollary 4.8. The normalized state space of a Euclidean Jordan algebra is an orbitope, i.e. Ω = Conv K.ω0 , for any ω0 ∈ ∂e Ω. In particular, for Herm(n, D), D ∈
{R, C, H, O}, Ω = Conv K.e11 , where e11 is the matrix unit diag(1, 0, 0, ..., 0).
This is so because extremal states are 1-frames, and the last sentence follows
from Proposition 4.4 and the fact that e11 is a primitive idempotent.
We note here that the state space of a spin factor, V = Rn ⊕ R, is the unit n-ball
{(x,t) : t = 1, |x|2 ≤ 1} in the affine subspace t = 1.

4.2 Classification of Euclidean Jordan algebras, their cones,
state spaces, and automorphism groups
In this section we give a more detailed description of the Euclidean Jordan algebras, their cones of squares, their normalized state spaces, and the automorphism
groups of these objects. We also give a representation-theoretic description of
normalized Jordan algebra state spaces that will allow us to identify them with the
convex hulls of certain orbits in polar representations.
The automorphism group of the cone of squares of a Jordan algebra V , like
the automorphism group of any self-dual cone, is reductive [26]. If the algebra

<!-- page 22 -->
22

Table 1: Euclidean Jordan algebras with associated cones and Lie algebras
V
V+
g
k
dimV
rank V
Sym(m, R)
PSD(m, R)
sl(m, R) ⊕ R
o(m)
m(m + 1)/2
m
Herm(m, C)
PSD(m, C)
sl(m, C) ⊕ R su(m)
m2
m
Herm(m, H)
PSD(m, H)
sl(m, H) ⊕ R su(m, H) m(2m − 1)
m
n−1
R⊕R
Lorentz(1, n − 1) o(1, n − 1)
o(n)
n
2
Herm(3, O)
PSD(3, O)
e6(−26)
f4
27
3

is simple, then Aut V+ = Gs × R+ , where Gs is simple. Also, Aut 0 (V+ ) = Gs0 ×
R+ .16 We will also write Aut s (V+ ) and Aut s0 (V+ ) for the groups Gs and Gs0 .
V is an irreducible representation space for Gs (cf. e.g. [20], p. 42), and for
its connected identity component Gs0 . Like any semisimple Lie group, Gs has
Cartan decompositions g = k ⊕ p of its Lie algebra and, correspondingly, Gs =
K exp p of the group. We may choose one such that K is the subgroup of Gs0
that fixes the identity e, since this is a maximal compact subgroup of the linear
group Gs . V is an irreducible spherical representation of Gs , and of its connected
identity component Gs0 , which means that Gs ’s (and also Gs0 ’s) maximal compact
subgroup, K, has a one-dimensional fixed-point space (in this case, Re).
In Table 1 (essentially from [19]) we list the finite-dimensional simple Euclidean Jordan algebras and associated data. V is the algebra, with positive cone
V+ , g is the Lie algebra of Aut V+ , and k the Lie algebra of Aut Ω (where Ω is
the normalized state space). We use the notation Herm(m, D) for the Jordan algebra of self-adjoint matrices over a classical division algebra D ∈ {R, C, H, O},
PSD(m, X ) for the positive semidefinite matrices, and Lorentz(1, n − 1) for the
Lorentz cone {(z, x) ∈ R ⊕ Rn−1 : |z|2 ≥ |x|2 , z ≥ 0}. Also we write Sym(m, D)
for the space of symmetric matrices with entries in D, and note in particular that
Herm(m, R) ≡ Sym(m, R).
In the three infinite families of matrix cases, Aut 0V+ is the group of transfor16

In the non-simple case, Aut 0V+ ≃ Gs0 × Rk+ , where k is the number of simple factors of V ,
each copy of R+ acts as dilations on simple factors, and Gs0 is a product of the groups Aut s0V+i
acting on simple factors Vi (in other words, Aut 0V+ = Πi Aut 0V+i ); the full (not necessarily connected) automorphism group allows, besides non-identity components in each factor, permutations
of isomorphic factors.

<!-- page 23 -->
23
mations X 7→ AX A†, where A is any nonsingular matrix over the relevant division
algebra D, i.e. A ∈ GL(m, D).17 The identity component, Aut 0 (Ω), of the maximal compact subgroup consists of those transformations for which A is drawn
from the subgroups SO(m), SU (m, C), SU (m, H) respectively. This preserves the
identity matrix in V ≃ Herm(m, D), which is the unit e of the Jordan algebra. The
space orthogonal to this consists of the traceless self-adjoint matrices over R, C, H
respectively, and it is an irreducible representation space for K.
The set of such transformations for which A is drawn from the subgroups
SO(m), SU (m, C), SU (m, H) respectively is the identity component of a maximal compact subgroup of Aut 0 (V+ ). It preserves the identity matrix in V ≃
Herm(m, D), which is the unit e of the Jordan algebra. The subspace of V orthogonal to the identity matrix consists of the traceless self-adjoint matrices over
R, C, H respectively, and it is an irreducible representation space for K.
A similar description is not obviously possible in the case of Herm(3, O), because O is nonassociative. However, one can deal with this by observing that
the transformations X 7→ AX A† for A ∈ SL(m, D), D ∈ {R, C, H} are determinantpreserving, and symmetric octonionic matrices have well-defined determinant (indeed, there is a Jordan-algebraic definition of determinant, cf. [19]). Then one
can show (cf. [27]) that for arbitrary m and D ∈ {R, C, H}, and for m = 3 and
D = O, the determinant-preserving linear transformations of V are Aut s0 (V+ ).18
The identity-preserving subgroup, in the cases D ∈ {R, C, H}, is as stated in the
previous paragraph. In the octonionic case it is the compact real form of F4 . (In
[27] this is dubbed SU (3, O).)
Returning to consideration of general EJAs, the Lie algebra of the subgroup
that fixes the Jordan unit e is the compact part k in a Cartan decomposition g =
k ⊕p of the reductive group Aut V+ , and V itself can be identified with p in this decomposition.19 As with any Cartan decomposition, there is a natural K-invariant
17 Aut

0V+ = Aut V+ except in the following cases where Aut 0V+ is of index two, with a
representative of the nonidentity component as stated: Herm(n, R) for n even, X 7→ MXM †
with M = diag(−1, 1, ..., 1); Herm(n, C), transpose; R ⊕ Rn−1 for n ≥ 3, x 7→ Mx with M =
diag(1, −1, 1, 1, .., 1) [20]. The groups generated by X 7→ MXM † with M ∈ SL(n, C), SL(n, H)
are not precisely SL(n, C), SL(n, H) in general, although they have the same Lie algebras as those
groups; they are homomorphic images.
18 Even though in the case of D = O we can identify a subset of 3 × 3 octonionic matrices M such
that X 7→ MXM † is determinant-preserving on octonionic-hermitian matrices X, and this generates
the group of determinant-preserving linear transformations, this group is not identical to the maps
X 7→ MXM † because of the nonassociativity of octonionic matrix multiplication (see [27], where
the group is dubbed SL(3, O)).
19
For example, this is part of Theorem 8.5 of [20], with the Cartan decomposition given in

<!-- page 24 -->
24
inner product on V , such that k is represented by real antisymmetric matrices and
p by symmetric ones. Furthermore for a simple Jordan algebra p decomposes
as R ⊕ p0 , where p0 = p ∩ gs , gs is the semisimple part of the Lie algebra of
Aut V+ = R+ × Gs (so gs = lieGs ) and R is generated by the Jordan unit e. Although the actions of Aut V+ , and of Gs , on V are not their adjoint actions (on, i.e.
corestricted to, p), the restriction of these actions to K does coincide (on p) with
the restriction of the adjoint action.20 In other words, p0 is the representation space
of a polar representation (Definition 8.5), called a symmetric space representation
(Definition 8.9), of the compact group K. The Jordan trace gives the component
in the R factor of the Jordan algebra V ≃ p = R ⊕ p0 . Recall that the normalized
state space, Ω := V+ ∩{x ∈ V : tr x = 1}, is also Conv K.ω for any extremal ω ∈ Ω
(from strong symmetry). Everything in the affine plane {x ∈ V : tr x = 1} has the
form c ⊕ ω0 , where c = e/rankV is the unit-trace element of the fixed-point space
Re, and ω0 ∈ p0 . Thus Ω is affinely isomorphic to Conv K.ω0 , an orbitope in the
polar representation of k on p0 . This is what will permit us, in Section 9, to identify these Jordan algebra state spaces with certain regular convex bodies, since
regular bodies are described in the Madden-Robertson classification [8] as convex
hulls of orbits in polar representations.

5 Simplices are strongly symmetric and spectral
In the previous section, we saw that the state spaces of simple Euclidean Jordan
algebras are strongly symmetric and spectral, part of the “if” direction of our main
theorem. In this section, we establish the other part of the “if” direction: the easy
fact that simplices are strongly symmetric and spectral.
The standard presentation of an n-simplex as embedded in a vector space V of
one higher dimension takes the n + 1 vertices of the simplex as the unit vectors
ei of V = Rn+1 considered as a Euclidean space in the usual way, i.e. with “dot
product” as inner product, and represents effects in the same space, with evaluation given by this inner product. V+ is then the nonnegative orthant, Rn+ , and it is
manifestly self-dual with respect to this inner product. So the order unit u is the
Lemma 8.6 of that book and the proof. It also follows from the conjunction of Theorem III.2.1
and Theorem III.3.1 in [19] (this conjunction is, roughly, Satake’s Theorem 8.5).
20 In the matrix cases with D ∈ {R, C, H}, this is manifested in the fact that while in general
†
A 6= A−1 , equality does hold when A is respectively orthogonal, unitary, or quaternionic-unitary;
this exemplifies the general fact that for compact groups, representations are isomorphic to their
duals, which establishes the claim for the spin-factor and octonionic cases too.

<!-- page 25 -->
25
all-ones vector (1, 1, ..., 1), the dual cone V+∗ is equal to the primal cone, and the
set of effects is the unit hypercube (the convex hull of the 2n+1 vectors of length
n + 1 with entries in {0, 1}). The unit vectors are therefore not only the pure
states, but are also effects, and they sum to u, so they constitute a measurement.
Every ordered subset of the unit vectors is a submeasurement, and perfectly distinguishes the same subset considered as states, so is a frame; since by definition
frames are ordered subsets of the pure states, and in a simplex, the pure states are
the unit vectors, these are all the frames. The full set of unit vectors is the unique
maximal frame, up to order. Since the simplex is defined as its convex hull, the
simplex is spectral. The group Aut Ω is the symmetric group Sn acting to permute
the vertices, so it is obviously transitive on k-frames for each k ∈ {1, ..., n + 1},
i.e. the simplex is strongly symmetric.
It is relatively easy to show that the simplices are the only strongly symmetric
spectral polytopes. For example, from item 3 of Proposition 3.6 we know that the
cone over a strongly symmetric spectral body must be perfect. Theorem 1 of [28]
states that the only self-dual polyhedral cones in En whose maximal faces are all
self-dual in their spans (with respect to the restriction of the inner product) are
isometric (hence also affinely isomorphic) to the simplicial cone Rn+ .

6 Strongly symmetric spectral bits are balls
In this section, we prove a special case of our main theorem, for convex sets whose
largest frame has cardinality 2. We show that they are all affinely isomorphic
to balls, which are the normalized state spaces of the Euclidean Jordan algebras
known as spin factors. This case can be handled without the Farran-MaddenRobertson theory [7, 8] of regular convex bodies, and we can use it in the proof
of our main theorem, where it allows us to avoid some tedious case-checking
involving the Madden-Robertson classification.
We call a convex body Ω a bit if the largest frame it contains has cardinality
2. We say Ω has reversible transitivity if Aut Ω acts transitively on the set ∂e Ω of
pure states of Ω. All strongly symmetric convex bodies have this property, since
extremal states are 1-frames.
In [12] (Section IV) B. Dakić and C. Brukner claimed that spectral bits that
have reversible transitivity on pure states (i.e. on 1-frames) are necessarily balls,
and give an argument for this claim. The claim may well be true, but their argument makes an implicit assumption. When this assumption is made explicit,
one immediately sees that it follows from transitivity on 2-frames, which in the

<!-- page 26 -->
26
case of bits is identical to strong symmetry. Once this is observed, one sees that
Dakic and Brukner’s argument establishes the following result, which is weaker
than Dakić and Brukner’s claim.
Theorem 6.1. Let Ω be a strongly symmetric spectral compact convex body whose
largest frame is of cardinality 2. Then Ω is affinely isomorphic to a ball.
The proof, which is essentially Dakić and Brukner’s argument done in slightly
more detail and with an explicit assumption of transitivity on 2-frames, is in Appendix A.

7 Regular convex bodies and regular convex compact sets
In this section we will use some definitions and results from [7] and [8] concerning
compact convex sets embedded in Euclidean space, which the authors of [7] and
[8] call convex solids or, when they are full-dimensional, convex bodies. Some of
the notions studied in [7] and [8] are sensitive to the particular embedding of a
compact convex set in Euclidean space, and fail to be invariant under affine transformations, whereas our concern is with affine-invariant structure. Nevertheless
their results are immediately applicable to our situation, because of the canonical
embedding (Definition 2.3 of compact convex sets of dimension n into En . In
the following, the group of rigid transformations of En is defined as the group
generated by rotations, translations, and reflections.
Definition 7.1 ([7]). A solid is a compact convex subset of Euclidean space En .
It has affine dimension m ≤ n, and if we wish to indicate its dimension, we may
call it an m-solid in En or simply m-solid. A convex body is an n-solid in En , i.e. a
full-dimensional solid; it may also be called an n-body. The symmetry group GB
(sometimes G, for short) of a convex body B is the subgroup of the group of rigid
transformations of En consisting of those transformations that take B into (so in
fact, onto) itself.
The symmetry group GB of B consists of affine automorphisms, but in general
it may be a proper subgroup of the group Aut B of affine automorphisms of B. For
example, a nonsquare rectangle has a smaller symmetry group than a square, and
a parallelogram whose sides are not all the same length has a smaller symmetry
group than a rectangle, whereas Aut Ω is the same in all three cases. Similarly, a

<!-- page 27 -->
27
general solid ellipsoid has a smaller symmetry group than a (spherical) ball, but
the two are affinely isomorphic.
The notion of symmetry group, and the associated results of [7] and [8] are
nevertheless useful to us because of the following (which is immediate from
Proposition 2.2):
Proposition 7.2. Let Ω be canonically embedded in a Euclidean space E, in the
sense of Definition 2.3. Then Aut Ω is the symmetry group GΩ.
In [7] and [8] the term “face” is used to mean “exposed face”, that is, the
intersection of the set with a supporting hyperplane. Since we will use some
definitions and results from [7] and [8], and since all faces in strongly symmetric
spectral convex bodies are exposed,21 that is how we will use the term from now
on. It is a fairly standard convention to include ∅ and Ω as faces, and even as
exposed faces, of Ω; they are called improper faces and the others are called
proper faces.
Definition 7.3. A flag of a convex compact set Ω is a sequence F1 , ..., Fr of distinct
nonempty exposed faces of Ω such that F0 ⊂ F1 ⊂ · · · Fr .

In other words it is a chain in the face lattice, not containing the empty face.22
Every convex body may be considered as a compact convex set relative to the
natural affine space structure of En (obtained by forgetting about the inner product
and 0). So the notion of flag also applies to convex bodies.
Definition 7.4. A maximal flag is a flag that is not a subsequence of any other
flag. 23
21 In fact this is true of all regular convex bodies as well, by Proposition 8.7 and the fact [29, 30]

that all faces of orbitopes in polar representations are exposed. We suspect it would remain true if
the definition of regularity were changed to refer not to exposed faces, but just to faces.
22 This is almost identical to the definition in [7], except that they also exclude the face Ω,
whereas we prefer to allow (but not require) its inclusion. When we need their notion we will use
the term “short flag”.
23 We define a maximal flag exactly as in [8], except that our flags contain the full set, whereas
theirs do not. Maximal flags of these two types are obviously in bijection with each other, by
deleting or appending Ω at the end of the sequence of faces. In [7] a slightly different definition
of maximal flag is given, but the definitions give rise to the same notion of regularity, and are
equivalent for regular convex bodies. Explicitly, σΩ ⊂ N, which we may call the “signature” of
Ω, is the ordered (by restriction from the usual ordering of N) set of integers i such that there
is a proper face of Ω of dimension i. Farran and Robertson call a flag maximal if the sequence
dim F0 , ..., dim Fr of dimensions of faces in the flag is equal to σΩ . Once regular convex bodies are
defined, it will be clear the two definitions coincide for such bodies (though not in general, cf. the
examples in Fig. 2 of [7]).

<!-- page 28 -->
28
We have the following elementary fact.
Proposition 7.5. Let g be an automorphism of Ω. If F is a face of Ω, g.F is also
a face of Ω, and g.c(F) = c(g.F). Let Φ be a flag of Ω. Then g.Φ is a flag of Ω;
it is maximal if and only if Φ is.
Definition 7.6. [7] A convex body B is called regular if its symmetry group GB
acts transitively on the set of maximal flags of B. 24
We give an analogous definition for arbitrary convex compact sets:
Definition 7.7. A convex compact set Ω is called regular if its affine automorphism group Aut Ω acts transitively on the set of maximal flags of Ω.
Unlike the notion of regular compact convex set, the notion of regular convex
body is not affine-invariant, because it is sensitive to the embedding in Euclidean
space. But we have the following elementary relation between the notions of
regular convex body (Definition 7.6) and of regular compact convex set (Definition
7.7).
Proposition 7.8. Every regular convex body B, considered as a compact convex
set, is regular. Not every convex body that is regular when considered as a compact convex set, is a regular convex body, but every canonically embedded regular
compact convex set is a regular convex body.
Proof. The first sentence holds because because the symmetry group GB is a subgroup of Aut B, and transitive action by a subgroup trivially implies transitive
action by the group. The second holds because a regular compact convex set may
be embedded in such a way that its symmetry group is too small a subgroup of
the automorphism group to act transitively on frames (consider a triangular simplex, embedded as a non-equilateral triangle), but in its canonical embedding, the
symmetry group is equal to the automorphism group (cf. Proposition 7.2).
The following is Farran and Robertson’s version (probably originating, for the
case of groups generated by a finite number of reflections, with Coxeter or earlier),
adapted to this setting, of a standard notion from the theory of group actions on
topological spaces, that of a fundamental set for an action.
24 Once again, this is essentially the definition from Farran and Robertson [7], except that their

notion of flag omits B itself. It obviously gives the same notion of regularity.

<!-- page 29 -->
29
Definition 7.9. Let B be a convex body of affine dimension n in V ≃ En , with
barycenter 0, and let G be a compact subgroup of O(En ) that preserves B. A
convex solid (not necessarily full-dimensional) D ⊂ En , is called a fundamental
region for the action of G on B if
1. B ⊆ GD, and
2. Every G-orbit in B meets the relative interior of B in at most one point.
Theorem 7.10 (Farran and Robertson (Theorem 7 of [7])). Let B be a convex body
embedded in En . Suppose in addition that B is regular. Let Φ = (F1 , ...., Fr ) be
a maximal flag of B, and let ci be the barycenter of Fi . Then the (r − 1)-simplex
△Φ := △(c1 , ..., cr−1, cr ) is a fundamental region for the action of B’s symmetry
group G on B.
When we work with a fixed flag Φ, we often write △ for △Φ , and omit the
subscripts indicating the dependence of other objects on Φ as well. The automorphism group, Aut B =: K, of any convex compact set is a compact Lie group. If
it has trivial Lie algebra (k = {0}), then it is a finite group. The same two statements hold for the symmetry group of a convex body B as defined by Farran and
Robertson (since their definition of convex body requires B to affinely span the
Euclidean space in which it is embedded). We write △ for △Φ and △′ for the
r − 2-simplex △(c1 , ..., cr−1) in Aff B ≡ Rn . This differs from the definition of △
only by omitting the barycenter cr ≡ 0 of B; its affine dimension is r − 2, whereas
△’s is r − 1.
The facial structure of the simplex △ encodes important information about
how generic the orbits are, via the following theorem.
Theorem 7.11 (Theorem 8 of [7]). Let △ be the fundamental domain for the
regular convex body B, as defined in Theorem 7.10, and let G = GB, B’s symmetry
group. Let F be a face of △ of nonzero dimension. If x is in the relative interior
of F, and y ∈ F is arbitrary, then Gx ≤ Gy . In particular, if x and y are both in the
relative interior, Gx = Gy .
We now assume without loss of generality that B is canonically embedded in
En , so in particular cr = 0. The points c1 , ...., cr−1 linearly generate—equivalently,
△′ linearly generates—an (r − 1)-dimensional vector space in Aff B ≡ Rn , which
we call L. (Of course, △ also (both linearly and affinely) generates L.)
Following [7] we define a map π : B 7→ π (B) := B ∩ L. In [7], π is called a
projection, presumably because it is idempotent: if B is a regular polytope, then
π (B) = B.

<!-- page 30 -->
30
Definition 7.12. For a regular convex body B embedded in Euclidean space En ,
we call the subspace L defined in the preceding paragraph a Farran-Robertson
section, and the polytope π (B) := L ∩ B its Farran-Robertson polytope. We define
the Farran-Robertson polytope of a regular compact convex set Ω as the FarranRobertson polytope of Ω when Ω is considered as a convex body by canonically
embedding it in Euclidean space.
As embedded in En , the convex solid π (B) depends on the choice of a maximal
flag of B, but as we shall see in Propositions 8.7 and 8.8, all π (B) are G-conjugate,
hence isometric.
Theorem 7.13 (Theorem 9 of [7]). Let B be a regular convex body with symmetry
group K. The Farran-Robertson polytope π (B) is a regular polytope, of affine
dimension k = dim L, whose symmetry group W is a finite group generated by
reflections, isomorphic to KL /K L .
As an example, consider a 3-dimensional ball Ω centered on the origin. Aut Ω ≡
GΩ is O(3). L may be taken to be any line through the origin and π (Ω) the simplex △1 consisting of the diameter L ∩ Ω. Aut π (Ω) ≃ Z2 is generated by the
reflection through the plane orthogonal to this diameter.
Examples where Ω 6= π (Ω) but with a more interesting π (Ω), for example
where π (Ω) is the three-vertex simplex △2 , are harder to visualize because the
affine span of Ω will tend to be too large. In the lowest-dimensional example
(as it will turn out) Ω is the unit-trace positive semidefinite real symmetric 3 × 3
matrices, with L the diagonal unit-trace matrices (two dimensions) and L ∩ Ω ≃
△2 . Aff Ω, the unit-trace real symmetric matrices, is 5-dimensional in that case.
Ω in this second example is affinely isomorphic to the example on pp. 378-379 of
[7], where it is presented as the convex hull of the Veronese surface, an embedding
of P2 (R) into E6 . This surface is the extreme boundary of its convex hull Ω, which
spans a 5-dimensional subspace.
The following theorem allows us to understand the facial structure of Ω by
understanding that of π (Ω). We will need it later to show that frames in π (Ω)
correspond to frames in Ω in the strongly symmetric spectral case; it is of course
also of intrinsic interest. This theorem is stated near the top of p. 369 of [8].25
25 An essentially identical (except for its more restricted premise) theorem is stated for a more

restricted setting (the subclass of polar representations occuring within adjoint representations of
real semisimple groups) in [7].

<!-- page 31 -->
31
Proposition 7.14 ([8]; see also [7], Theorem 10, and its proof). Let B be a regular
convex body with symmetry group G, and Farran-Robertson polytope π (B). Let
F be a face of π (B) with centroid c(F), and write Gc(F) for the isotropy subgroup
of G at c(F). Then the orbit Gc(F) F is a face of B, which we call HF , and each
face of B is of the form gHF for some face F of π (B) and some g ∈ G. Moreover,
if F1 , F2 , ..., Fr is a maximal flag of P, then HF1 , HF2 , ...., HFr is a maximal flag of B,
and every maximal flag of B arises from a flag of π (B) in this way.
Since the symmetry group of a convex body is its automorphism group, we
also have the analogous statement for convex compact sets and their automorphism groups.

8 Classification of regular convex bodies via polar
representations
In this section, we sketch the classification of regular convex bodies from [8], via
polar representations as defined, classified (in the irreducible case), and related
to noncompact symmetric spaces in [31]. The results of this section will be used
through the classification set out in [8], Tables 2, 3, and 4. Besides the tables
themselves we need to understand which orbit, in the polar representation listed
in the table, gives rise to the regular convex body.
Let us write ρ for the representation of the action of the symmetry group GΩ
on En . Proposition 2.1 of [8] states that for a regular convex body Ω, this representation is irreducible. 26 Proposition 2.2 of [8] states that for regular convex
bodies Ω, ρ is a polar representation, defined as one for which the subspace normal to a principal (i.e. highest-dimensional) orbit of the action meets every orbit
orthogonally.
More formally, let G be a compact Lie group with Lie algebra g and let ρ :
G → O(V ) be a representation on a real inner product space. (As usual we often
write g for ρ (g) where g ∈ G.) v ∈ V is called regular if the orbit G.v is of maximal
dimension (i.e. no orbit has higher dimension). The tangent space at v to an orbit
26 In [8] the proof is attributed to M. Pinto in a paper “to appear” which we have not been able

to find. It involves showing that regular convex bodies belong to the wider class of perfect (not
to be confused with the notion of perfection of cones) convex bodies [7], and the observation that
this implies ρ is irreducible. It is not hard to reconstruct a simple proof along these lines. We
note that Markus Müller [32] has shown more directly that the automorphism group of a strongly
symmetric spectral convex body Ω acts irreducibly on Aff Ω.

<!-- page 32 -->
32
G.v is g.v. It is a linear subspace of V . We define a linear cross-section of the set
of G-orbits in V to be a subspace of V that intersects every G-orbit. Although this
term is not explicitly defined in [31], this is the sense in which it is used there. We
will usually omit the qualifier linear, since we make no use of any other kind of
cross-section.
Definition 8.1 (following [31]). For any v ∈ V , define av to be the subspace of V
normal to the G-orbit at v, i.e. av := (g.v)⊥ .
Proposition 8.2 ([31], Lemma 1). For any v, av is a cross-section of the set of
G-orbits.
Note that by Definition 8.1, V itself is a cross-section.27 More interesting are
the minimal-dimensional cross sections.
Definition 8.3 ([31]). Cross-sections of the form av for regular v are called Cartan
subspaces.28
Such cross-sections are of minimal dimension.
Proposition 8.4 ([31]). Let v0 be regular. The following are equivalent:
1. For any regular v ∈ V , there is a k ∈ G such that g.v = k.(g.v0).
2. For any regular v ∈ V , there is a k ∈ G such that av = k.av0 .
3. For any u ∈ av0 , (g.u, av0 ) = 0.
Thus we have uniqueness (up to the action of G) of minimal cross-sections if and
only if the orbits intersect one such cross-section orthogonally.
Definition 8.5 ([31]). A representation satisfying any (and hence all) of the three
equivalent conditions in Proposition 8.4 is called polar.
Thus the polar representations are ones for which the minimal dimensional
cross-sections of the form av for regular v, i.e. normals to maximal-dimensional
orbits, are all G-conjugate (item 1 in Proposition 8.4), or equivalently ones for
which, for every maximal-dimensional orbit, the subspace normal to that orbit (at
any point) intersects every orbit orthogonally (item 3 in Proposition 8.4).
27 Sometimes a definition is used in which a cross section must intersect each orbit finitely may

times, which would rule out V except in the case of g = 0.
28 It seems likely that in [31] this definition is meant to apply only in the polar case, but in
the proof of Proposition 2.2 of [8] (Proposition 8.7 below), it is clearly meant to apply prior to
establishing the representation is polar.

<!-- page 33 -->
33
Remark 8.6. A cross-section that meets all orbits orthogonally is minimal. Hence
an equivalent definition (cf. [33, 34, 35]) of polar representation is that it is a
representation for which there exists a cross-section that meets all orbits orthogonally.
Proposition 8.7 ([8], Proposition 2.2 and its proof). Let B be a regular n-solid in
E ≃ En , with centroid 0, and let π be the inclusion of the symmetry group G of B
in O(n) ≃ O(E). Then the representation π is polar, and for any maximal flag Φ
of B, the centroids of the faces in Φ are a basis for a Cartan subspace, LΦ .
Proof (greatly expanded version of proof in [8]). Let x and v each be on principal
orbits (not assumed to be the same orbit) of this G-action, and recall that ax :=
{u ∈ En : hu, g.xi = 0} and av := {u ∈ En : hu, g.vi = 0}. We will show:
Claim 1. There is a g ∈ G such that av = g.ax.

This will prove Proposition 8.7, because transitive action of G on the set {ay :
y ∈ V } of Cartan subspaces is one of the equivalent conditions that defines (via
Proposition 8.4) Dadok’s notion of polar representation.
To do this we show that the Farran-Robertson sections LΦ are Cartan subspaces; recall that LΦ is the linear space spanned by the centroids of the faces in
the maximal flag Φ, and hence the linear span of the simplex △ whose vertices
are those centroids, and indeed of the simplex △′ whose vertices are those of △,
with the exception of 0 (the centroid of Ω). Since the topological boundary ∂ B
contains representatives of all nonzero orbits, L is a cross-section of the representation. In the proof of Theorem 9 in [7], it is established that “G.y is perpendicular
to L for all y ∈ L.” In other words, for all y ∈ L, L ⊆ ay . Since L is a cross-section
it contains representatives of principal orbits, i.e. regular elements; letting one
such be x, we have L ⊆ ax . But since x is regular ax is a minimal cross-section by
Lemma 1 of [31], so L = ax , and L is a Cartan subspace.
To show that G acts transitively on the set of Cartan subspaces, we fix one
such subspace ax = LΦ . Since △Φ is a fundamental region for the action of G on
B, every nonzero v on a principal orbit has the form v = g.x for some g ∈ G and
some x in an element of △Φ . We have x ∈ LΦ . By Proposition 7.5 g.Φ is also a
maximal flag, and (since by that Proposition g takes centroids of face to centroids
of faces) g.LΦ = Lg.Φ . Of course g.x ∈ Lg.Φ ; moreover, by the same argument used
to establish that LΦ is a Cartan subspace, Lg.Φ = ag.x , and hence Lg.Φ is a Cartan
subspace. Since Lg.Φ = g.LΦ , this shows that av = g.ax, establishing Claim 1.

<!-- page 34 -->
34
Proposition 8.8 (Corollary of Proposition 8.7). Let Ω be a regular compact convex set canonically embedded in a Euclidean space E. The representation of
Aut Ω in O(E) is polar. The centroids of a maximal flag of Ω are a basis for
a Cartan subspace.
To study regular nonpolytopal convex compact sets Ω, we may assume that
the Lie algebra g of Aut Ω is nontrivial, i.e. not equal to {0}. For compact Lie
groups, this is equivalent to assuming the group is not finite. The next definitions
and results concern situations where the Lie group is connected, and hence (except
in the degenerate case of the trivial group) has nontrivial Lie algebra. If ρ is a
representation of a Lie group G, we write d ρ for the derived representation of G’s
Lie algebra.
Definition 8.9 ([31]). 29 Let G be a compact connected Lie group, g its Lie algebra. A representation ρ : G → SO(V ) is called a symmetric space representation if
there are a real semisimple Lie algebra h with Cartan decomposition h = k ⊕ p, a
Lie algebra isomorphism A : g → k, and an isomorphism L of linear spaces V → p
such that L ◦ d ρ (X ) ◦ L−1(y) = [A(X ), y] for all X ∈ g, y ∈ p.
In other words, L ◦ d ρ (X ) ◦ L−1 = ad (A(X )).
The symmetric spaces in the proposition are H/K, for groups such that K is
compact with Lie algebra k ≃ g, and the Lie algebra h of the real semisimple group
H has Cartan decomposition h = k ⊕ p, where p, as mentioned in the definition,
can be identified with the representation space V . They are of noncompact type
since one normally takes the term “Cartan decomposition” to imply that k ⊕ p is
noncompact semisimple. However by the duality bijection between compact and
noncompact symmetric spaces, the definition also includes the isotropy representations associated with symmetric spaces of compact type, because the compact
duals (with Lie algebra decomposition k ⊕ ip) give rise to equivalent polar representations K y ip.
Symmetric space representations are polar, with a, defined as usual as a maximal abelian subspace of p, a Cartan subspace in the terminology of [31].30 The
29 The statement in [31] appears to have a couple of typographical errors which we have cor-

rected: it has a in place of g in the last line, and omits the L−1 that we’ve inserted on the left-hand
side. Other than that, we quote [31] verbatim.
30 Of course a is not a Cartan subalgebra of h, unless h is a split real form of a complex Lie
algebra. But a is the intersection of p with a particular type of Cartan subalgebra of h (one that is
“maximally noncompact”, i.e. whose intersection with p is maximal). The term “Cartan subspace”
was already standard in the symmetric space context.

<!-- page 35 -->
35
action of G on p is often called the isotropy representation of G in the context of
symmetric space theory; a symmetric space representation in the above sense is
just one that is equivalent to such an isotropy representation.
Dadok is able to use the symmetric space representations to classify the irreducible polar representations (up to orbit equivalence) by using the following
theorem:
Theorem 8.10 (Proposition 6 of [31]). Let ρ : G → SO(V ) be a polar representation of a connected compact Lie group G. There is a connected Lie group G̃
with symmetric space representation ρ̃ : G̃ → SO(V ) such that the G-orbits and
the G̃-orbits in V coincide.
The key point, from [8], is that “for a[n irreducible] noncompact symmetric
space H/K, knowledge of K and the dimension of H/K are sufficient to determine
H. But these are already given by the symmetry group G and the dimension n,
respectively. Thus we have associated to the given n-solid B a symmetric space
H/K.” (The bracketed modification is necessary for the truth of the claim.)
The following incorporates and extends Proposition 8.7, giving more detail on
the embedding of a regular convex body in polar representations of its symmetry group and some subgroups thereof, including consequences of Theorem 8.10,
mostly extracted from the discussion on pp. 366-367 of [8], and from [31] .
Proposition 8.11. Let B (of dimension n) be a regular convex body in a Euclidean
space V ≃ En , with centroid 0 and symmetry group G, and lie(G) = g. Fix a
maximal flag Φ and a corresponding fundamental region △ := △Φ (cf. Theorem
7.10). Then
1. The Farran-Robertson section LΦ ⊆ V is a linear cross-section of the form
ax for regular x.
2. For every regular x′ ∈ V , ax′ is a linear cross-section and there is a g ∈ G
such that ax′ = Lg.Φ .
3. Both the inclusions G → O(V ) and G0 → SO(V ) → O(V ) are polar.
4. By Theorem 8.10 we may make the identification V ≃ p where p is the
isotropy representation of G̃ ≤ G associated with an irreducible noncompact symmetric space H/G̃. (So, h = g ⊕ p is a Cartan decomposition of h.)
The representation G y V ≃ p is the restriction of the representation G̃ y p.
We have g̃ := lieG̃ = g := lie(G) = lie(G0 ). Every maximal abelian subspace

<!-- page 36 -->
36
a ⊆ p is a Cartan subspace of the polar representations G̃ y p, G y p, and
G0 y p, and is a Farran-Robertson section of B, so π (B) = a ∩ B.
Proof. The polarity of the inclusion G → O(V ) in item 3 is Proposition 8.7, while
items 1 and 2 are the key points in its proof. Item (iii) in Proposition 8.4 characterizes the polarity of a representation entirely in terms of the derived representation g → so(V ), whence the inclusion G0 → SO(V ) → O(V ) is also polar since
g ≡ lie(G) = lie(G0 ).
Turning to item 4, Theorem 8.10 and its proof in [31] show that because G̃ has
the same orbits as G, its Lie algebra g̃ is a quotient of g and the derived symmetric
space representation g̃ → so(V ) factorizes g → so(V ). So g = g̃ ⊕ z, where z is
central in g and does not act on V , i.e. z.V = {0}. Hence the connected subgroup Z
of G0 with lie(Z) = z acts trivially on V . Since G0 is a subgroup of SO(V ) this implies that Z is trivial, whence g = g̃. But the Riemannian symmetric space doesn’t
change if we replace the maximal compact subgroup G̃ of H with a locally isometric one, so we can assume that G0 = G̃/Z̃, where Z̃ := {g ∈ G̃ : g|V = id}. It follows that V = p, h = g ⊕ p. Since it is known from the theory of symmetric spaces
that the subspaces (g.x)⊥ for regular x, i.e. the Cartan subspaces of Definition 8.3,
of a symmetric space isotropy representation are precisely the maximal abelian
subspaces of p, we may choose any such subspace as a Cartan subspace. The Cartan subspaces of the polar representations of G, G̃, and G0 coincide because their
Lie algebras do; consequently a is a Farran-Robertson section for G → V (with
respect to some choice of maximal flag of B ⊂ V ), and π (B) = a ∩ B.
Madden and Robertson do not state the above Proposition (Proposition 8.11)
as formally as we do. But their classification applies it to all of the irreducible polar representations that are symmetric space representations in the sense of Definition 8.9, which were classified by Cartan. Combined with the regularity of
the Farran-Robertson polytope (Theorem 7.13), and Coxeter’s work [36] (building on the classification of regular polytopes by Schläfli [37] and a construction
by Wythoff) classifying the embeddings of regular polytopes as orbitopes in finite groups generated by reflections, this enables them to classify regular convex
bodies, a classification given in their Tables 2, 3, and 4. We formally summarize
their classification as Theorem 8.12 below, and reproduce their tables, with minor
changes and the addition of the rightmost column, indicating which symmetric
spaces are associated with Euclidean Jordan algebras, as Tables 2, 3 and 4 below.
We precede this with a brief sketch of their argument involving Coxeter’s work.
Groups generated by a finite set of reflections in finite-dimensional real affine
space, or isomorphic to such a concrete group, are usually called reflection groups;

<!-- page 37 -->
37
each finite (not merely finitely generated) reflection group has a canonical representation on Euclidean space En , in which it is generated by a finite number
of orthogonal reflections through linear hyperplanes and there is no subspace on
which the action is trivial. The automorphism groups of regular polytopes are finite reflection groups; when the polytope is canonically embedded in Euclidean
space, its automorphism group acts acts in this canonical representation. If W is a
finite reflection group, we use the term W -orbitope for the convex hull Conv W.v
of an orbit of W in its canonical representation, and also call Conv W.v the W orbitope of v, or simply the orbitope of v when W is clear from context. Coxeter
considered all finite reflection groups groups W , specified by what are now called
Coxeter diagrams, and showed that the only regular W -orbitopes are, up to dilation by a positive scalar, convex hulls of orbits of particular points in the canonical
representation, identified by marking a node of the Coxeter diagram.
With a finite reflection group W fixed, a unit-length normal α ∈ En to the fixed
hyperplane α ⊥ (the “mirror”) of a reflection that is an element of W is called a
root, and the associated reflection is denoted by sα . (A different normalization
constant is sometimes chosen, and in the theory of Weyl groups of Lie groups,
which are a subset of the finite reflection groups, a different normalization is often
used, in which not all roots have the same length.) Thus each reflection is associated with two roots ±α , and the set R of roots is finite. Since for any g ∈ O(n),
gsα g−1 is the reflection sgα , in particular for any two roots sα sβ sα is the reflection
with root sα β , so R is W -invariant, W R = R.
A set Φ of roots is called simple if every root β ∈ R can be written β =
∑α ∈Φ cα α , where the coefficients cα are all of the same sign (which may of course
depend on β ), or zero. Simple sets of roots exist, and are bases for the canonical
representation space En ; the associated reflections sα are a minimal set of generators for W . The complement of the union of the mirrors of the reflections in R
is a dense subset of Euclidean space, and we call its connected components open
Weyl chambers and their closures Weyl chambers.31 The Weyl chambers are regular cones with simplicial base, and are fundamental regions for the group action.
The elements of the basis dual to the simple roots (when the roots are normalized
in a particular way) are called the fundamental weights. The cone generated by
the fundamental weights is a Weyl chamber, called the positive Weyl chamber C+ :
each fundamental weight generates an extremal ray of C+ , and each extremal ray
of C+ is generated by a fundamental weight.
31 The terminology is not uniform in the literature; sometimes “Weyl chamber” is used for the

open Weyl chambers, and “closed Weyl chamber” for their closures.

<!-- page 38 -->
38
For a group generated by a finite set of linear reflections in En to be finite,
obviously the product sα sβ of each pair of reflections must have finite order nαβ .
(It is a nontrivial fact that this is sufficient.) It follows from this and the fact that the
product of two reflections is a rotation by twice the angle between them, that the
angles between α and β must be rational multiples k/n of π . For α , β in a simple
set Φ, we will have k = nαβ − 1, i.e. the angles are π − π /nαβ , although we still
say the lines generated by the roots have angle π /nαβ . The Coxeter diagram of the
group is determined by these angles for a simple set of roots: its nodes correspond
to the simple roots and edges between nodes correspond to the angles other than
π /2 between the lines generated by roots—these edges are labeled by the integer
nαβ (less commonly, nαβ lines are used to link the pair of nodes, as in a Dynkin
diagram). Usually the label nαβ = 3 is omitted, so the angle π /3 is represented
by an unlabeled edge; there is no edge between nodes corresponding to pairs of
roots at angle π /2.32 It turns out that the relations (sα sβ )nαβ = 1 between pairs
of generators encoded in such a diagram suffice to uniquely determine a finite
reflection group (this nontrivial theorem immediately implies the nontrivial fact
mentioned above).
For the Weyl groups of Lie groups, which includes the reflection groups relevant to the classification of nonpolytopal regular convex bodies, only the labels 4
and 6 appear, reflecting the fact that in this case the angles between lines through
the simple roots are limited to π /2, π /3, π /4, and π /6. In this case the Coxeter diagram, in the version with angles represented by edge multiplicities, is just
the Dynkin diagram with the information about root lengths (associated with the
different normalization usually used in this case) omitted.
Returning to the general case, the point identified by marking a node is, up to
(strictly) positive scalar multiples, the fundamental weight dual to the marked root.
As mentioned above, Coxeter showed that the regular polytopes arise as convex
hulls of orbits (i.e. the orbitopes) of particular fundamental weights; every such
polytope arises as the orbitope of the weight specified by marking an end node
(node connected to only one other node) in some Coxeter diagram, although not all
end nodes have such polytopes as orbitopes, and some non-end nodes give rise to
32 Coxeter diagrams are also used to specify not-necessarily-finite, but discrete, groups generated

by a finite number of reflections in finite-dimensional real affine space, and further groups sharing
algebraic properties with these—see e.g. [38]. In this case, the labels on edges are drawn from the
set {4, 5, 6, ...} ∪ {∞}, the label indicating the order of the product of the two reflections associated
with the linked pair of nodes, still with order 3 unlabeled and no edge for order 2. The full set
of groups thus specified by Coxeter diagrams are known as Coxeter groups. For finite reflection
groups, only the integer labels appear.

<!-- page 39 -->
39
regular polytopes. To classify non-polytopal regular convex bodies, Madden and
Robertson needed only to consider Coxeter’s classification of regular orbitopes for
the case of finite reflection groups that are Weyl groups of irreducible symmetric
spaces, cf. the last two paragraphs on p. 366 of [8].
Theorem 8.12 (Madden-Robertson classification of regular convex bodies [8]).
1. Let G/K be an irreducible noncompact symmetric space, with the compact
group K connected, and let K y p be the isotropy representation of K,
i.e. g = k + p is the Cartan decomposition of g := lie G and K y p is the
restriction to K of the corestriction to p of the adjoint action G y g. Let a be
a maximal abelian subspace (also called Cartan subspace) of p and let v ∈ a
be such that P := Conv WK .v ⊂ a is a regular polytope, where WK := Ka /K a
is the Weyl group of K. Then B := K.P = Conv K.v is a nonpolytopal regular
convex body, P is its Farran-Robertson polytope π (B), and P = a ∩ B . B is
completely determined, up to affine isomorphism, by the affine isomorphism
class of π (B) and the symmetric space.
2. Conversely, for every regular convex body B that is not a polytope, there
exists an irreducible noncompact symmetric space G/K such that B is an
orbitope Conv K.v in the isotropy representation K y p of the compact connected Lie group K. Its Farran-Robertson polytope π (B) is a ∩ B, and is a
WK -orbitope.
3. In the above items v may be taken to be any strictly positive multiple of
one of a certain set of fundamental weights in a. Any weight w for which
Conv WK .w is a regular polytope may be chosen. These weights were classified by Coxeter: fundamental weights are specified by marking a node of the
Coxeter diagram, and Coxeter indicated which marked nodes correspond to
weights giving rise to regular polytopes.
4. The list of irreducible noncompact symmetric space representations presented as G/K for connected K, together with information on their dimensions, ranks, and the regular polytopes that occur as Weyl orbitopes in Cartan subspaces, is given in Tables 2, 3 and 4, which except for their last
column are essentially Tables 2,3, and 4 of [8].
Note that the same regular convex body may appear more than once in the
tables describing the classification. These occurrences include the coincidences
between noncompact irreducible symmetric spaces already noted by Cartan (cf.

<!-- page 40 -->
40
[39], pp. 519-520), which are are finite in number, plus some cases, including
some infinite series, where the same invariant regular convex body B appears in
different symmetric spaces. For the spectral strongly symmetric bodies, the coincidences between symmetric spaces arising from EJAs are indicated in the tables
by coincidences of EJAs in the rightmost column.33 The only other coincidences
between spectral strongly symmetric convex bodies in the tables are the actions
of proper subgroups of SO(n) on balls Bn , which occur in type AIII and CII when
p = 1. Appendix C contains more detail.

9 Classification of strongly symmetric spectral convex compact sets
In this section we apply the theory of the preceding sections to prove our main
result, which is the “only if” direction of Theorem 1.1: that strongly symmetric
spectral convex sets are normalized EJA state spaces or simplices. We proceed by
way of several intermediate propositions.
Proposition 9.1. Let Ω be a strongly symmetric spectral convex compact set. Then
Ω is regular.
In order to prove this proposition we first establish:
Lemma 9.2. Let Ω be a strongly symmetric spectral convex set. Let ω1 , ..., ωr be
a maximal frame in Ω. The sequence
Fi =

_

1≤ j≤i

{ω j }, i ∈ {1, ..., r}

(5)

is a maximal flag. Conversely, let (F1 , ..., Fr ) be a maximal flag of Ω. Then there
exists a maximal frame ω1 , ω2 , ...., ωr such that (5) holds.
In other words, the formula (5) gives a bijection between maximal frames in
Ω and maximal flags of Ω.
Proof. Let X = [ω1 , ..., ωr ] be a maximal frame. It follows from item 1 of Proposition 3.6 that the initial segments of X generate a sequence of faces, the Fi of
33 For completeness we note a few coincidences between listed EJAs, which only happen for the

polytope △1 : Herm(2, R) ≃ R2 ⊕ R, Herm(2, C) ≃ R3 ⊕ R and Herm(2, H) ≃ R5 ⊕ R. (Although
it only occurs once in the table, we note that R9 ⊕ R may be interpreted as Herm(2, O).)

<!-- page 41 -->
Table 2: Classical noncompact symmetric spaces with associated isotropy representations and Farran-Robertson
polytopes (adapted from [8], Table 2)
Dimension of
Rank of
isotropy
symmetric
space
representation
n−1
(n − 1)(n + 2)/2
n−1
(n − 1)(2n + 1)

Type
AI
AII

Symmetric space G/K
SL(n, R)/SO(n)
SU ∗(2n)/Sp(n)

AIII

SU (p, q)/S(U p ×Uq )

q

2pq

BI

SO0 (p, q)/(SO(p) × SO(q))
p + q odd, q < p

q

pq

DI

SO0 (p, q)/(SO(p) × SO(q))
p + q even

q

pq

DIII

SO∗ (2n)/U (n)

⌊n/2⌋ = q

n(n − 1)

CI

Sp(n, R)/U (n)

n=q

n(n + 1)

CII

Sp(p, q)/(Sp(p) × Sp(q))

q

4pq

Root space
An−1
( An−1
Cq (q < p)
Bq (q = p)

Polytope
△n−1
△n−1

EJA
Herm(n, R)
Herm(n, H)

✷q , ✸q

R2 ⊕ R (p = q = 1)

Bq

✷q , ✸q

R p ⊕ R (q = 1)

✸q

R p ⊕ R (q = 1)

✷q , ✸q

R2 ⊕ R (q = 1)

✷q , ✸q

R2 ⊕ R (q = 1)

✷q , ✸q

R4 ⊕ R (p = q = 1)

(
Bq (q < p)
D (q = p)
( q
Cq
q odd
BCq q even
Cq
(
Cq
(q = p)
BCq (q < p)

41

<!-- page 42 -->
42

Table 3: Exceptional noncompact symmetric spaces with associated isotropy representations and Farran-Robertson polytopes (adapted from [8], Table 3)

Symmetric space G/K
presented by g, k
EIII e6(−14) so(10) ⊕ R
EIV e6(−26) f4
EVI e7(−5) so(12) ⊕ su(2)
EVII e7(−25) e6 ⊕ R
EIX e8(−24) e7 ⊕ su(2)
f4(4)
sp(3) ⊕ su(2)
FI
f4(−20) so(9)
FII
g2(2)
su(2) ⊕ su(2)
G
Type

Rank of Dimension of
isotropy
symmetric
space
representation Root space Polytope
2
2
4
3
4
4
1
2

32
26
64
54
112
28
16
8

B2
A2
F4
C3
F4
F4
A1
G2

✷2
△2
Herm(3, O)
24-cell
✷3 , ✸3
24-cell
24-cell
△1
hexagon

Table 4: Noncompact symmetric spaces arising as K C /K for simple K, with associated isotropy representations and Farran-Robertson polytopes ([8], Table 4)

Type and
root space
An (n ≥ 1)
Bn (n ≥ 2)
Cn (n ≥ 3)
Dn (n ≥ 4)
F4
G2

Dimension of
isotropy
Polytope
EJA
representation
SL(n + 1, C)/SU (n + 1)
n(n + 2)
△n
Herm(n, C)
SO(2n + 1, C)/SO(2n + 1)
n(2n + 1)
✷n , ✸n
Sp(n, C)/Sp(n)
n(2n + 1)
✷n , ✸n
SO(2n, C)/SO(2n)
n(2n − 1)
✸n
C
F4 /F4
52
24-cell
C
G2 /G2
14
hexagon
Symmetric space

EJA

<!-- page 43 -->
43
(5), each properly contained in the next. This is a flag, which we will call ΦX .
In this sequence, the rank |Fi | of Fi is i. Suppose this flag is not maximal. Then
it can be enlarged, either by extending it before F1 , or by extending it after Fr ,
or by inserting some face G with Fi ( G ( Fi+1 . It cannot be extended before
F1 = {ω1 }, because the only face below the pure state ω1 is the improper face ∅.
It must have Fr = Ω by Proposition 3.6 (7), so it cannot be extended beyond Fr .
So there must be an i ∈ {1, ..., r} and a face G such that Fi ( G ( Fi+1 . By Proposition 3.6 (1) Fi ( G ( Fi+1 implies |Fi | < |G| < |Fi+1 |, which contradicts the fact,
observed above, that |Fi | = i and |Fi+1| = i + 1 by construction. Since every way
of extending the flag ΦX is inconsistent with the maximality of the frame X , ΦX
is a maximal flag.
Conversely, suppose Φ = {F1 , ..., Fr } is a maximal flag. By Proposition 3.6 (1)
each Fi is the join of (the singletons corresponding to) a frame, whose cardinality
is |Fi |. We will show (“Claim 1”) that F1 = {ω1 } for some extremal point ω1 , and
(“Claim 2”) that for each i ∈ {2, ..., r}, there exists an extremal ωi , distinguishable
from every state in the frame Fi−1 , such that Fi = Fi−1 ∨ ωi . It follows from the
associativity of join that (5) holds for each i, and since Fr = Ω for a maximal
flag, ω1 , ..., ωr generates Ω. Since Ω is generated by a maximal frame, and by
Proposition 3.6(1) all frames generating the same face have the same cardinality,
ω1 , ..., ωr has the same cardinality as a maximal frame, whence it is a maximal
frame.
To show Claim 2 we use the fact, which is part of Prop. 3.6(7), that if F ( G,
any frame for F extends to a frame for G by adjoining a frame for F ′ ∧G. Consider
′ ∧ F , whose join
F = Fi−1 , G = Fi , for i ∈ {2, ..., r}. The frame for the face Fi−1
i
with Fi−1 is Fi , is nonempty because F’s containment in G is strict.34 . Say it is
Σ = [σ1 , ..., σm], for m ≥ 1. We show that m = 1. If m > 1, then we can extend the
flag Φ to a flag Φ̃ defined by F̃j = Fj for j ∈ {1, ..., i − 1}, F̃j := F̃j−1 ∨ σ j−i+1 for
j ∈ {i, ..., i + m − 1}, and F̃j := Fj−m+1 for j ∈ {i + m, ..., r}. For m > 1, Φ is a
proper subflag of Φ̃, contradicting Φ’s maximality. So we must have m = 1, and
Φ̃ = Φ.
To show Claim 1, that F1 = {ω1 } for some extremal ω1 , we use essentially the
same argument: there is a frame η1 , .., η|F1| for F1 , nonempty because F1 6= ∅, and
if |F1 | 6= 1, then we can extend the flag by prefixing it with the nonempty sequence
W
of subfaces [Hi := k∈1,..i {ηk }]i∈{1,...,|F1|−1} , generated by the initial segments of
that frame. Since the flag was maximal, the extension must be impossible, so
34 Were F ′ ∧ G = 0 (i.e.

(F ′ ∧ G) ∨ F = G.

∅) then we’d have (F ′ ∧ G) ∨ F = F, while orthomodularity says

<!-- page 44 -->
44
|F1 | = 1, hence F1 = {η1 }, with η1 extremal.
Proposition 9.1 follows almost immediately.
Proof of Proposition 9.1. Let Φ1 = {F1 , . . . , Fr } and Φ2 = {G1 , . . ., Gr } be two
maximal flags of Ω. Then by Lemma 9.2 the faces of Φ1 , resp. Φ2 , are the sequences of faces generated by the initial segments of the maximal frames ω1 , ..., ωr ,
η1 , ..., ηr respectively, defined by the bijection (5). By strong symmetry, there exists g ∈ Aut Ω such that for all i ∈ {1, ..., r}, gωi = ηi . It follows that gΦ1 =
Φ2 .
Next we determine the implications of the conjunction of strong symmetry
and spectrality for the polytope π (Ω) that exists because of regularity.
Proposition 9.3. Let Ω be a strongly symmetric spectral convex compact set of
rank r. The polytope π (Ω) is a simplex with r vertices, which constitute a maximal
frame.
Proof. Let the dimension of Ω be n; without loss of generality we view Ω as
canonically embedded in En , i.e. assume that the barycenter of Ω is 0 ∈ Aff Ω ≃
En , viewing Aff Ω as a vector space as described earlier, and introduce an invariant inner product. Picking a maximal flag (it does not matter which one), F1 , ..., Fr ,
and letting ω1 , ..., ωr be the maximal frame corresponding to it via the bijection
(5), we consider the simplex △′ of Farran and Robertson (defined following Theorem 7.10 above), which, using the description of the barycenters of faces from
Proposition 3.6 (5), is equal to △(ω1 , (ω1 + ω2 )/2, ..., (ω1 + · · · ωr−1 )/(r − 1)).
We next identify the linear subspace L of Aff (Ω) generated by this simplex. Since
the barycenters just listed are manifestly linearly independent in Aff (Ω) (as must
be any set of barycenters of faces of a flag), L is (r −1)-dimensional (as also noted
following Theorem 7.10). It is easy to see that ω1 , ..., ωr−1 are a (linear) basis for
the space L.
So far in this proof, we have been working in the setting where Aff Ω is viewed
as a Euclidean vector space E with c(Ω) as its zero, and inner product chosen
so that Aff Ω is a subgroup of the orthogonal group. It is now useful to go to
the setting, described in Section 2 and used extensively in Proposition 3.6, in
which this Euclidean vector space is embedded as an affine subspace in the vector
space V of dimension one greater, in such a way that the embedded version of
E ≃ Aff Ω does not contain the origin of V , and hence the cone V+ = R+ Ω ⊂ V
has affine dimension one more than Ω’s. Of course the barycenter of Ω, which
was 0 in E ≃ Aff Ω, embeds as a nonzero element c of V . As described just

<!-- page 45 -->
45
before Proposition 2.4, we extend the action of SO(E) to an action of SO(E) on
V , which must fix the ray over c (pointwise), and equip V with a corresponding
invariant inner product such that this action of SO(E) ≃ SO(n) is as a subgroup
of SO(V ) ≃ SO(n + 1). By Proposition 3.6(3) this invariant inner product can be
chosen to be self-dualizing for the cone V+ and such that all pure states have unit
Euclidean norm, and we do so.
Now L, which was a linear subspace in E ≃ Aff Ω, is embedded in V as an
affine subspace but–since it is an affine subspace of Aff Ω–not a linear subspace.35
L was the linear space spanned by c1 , ..., cr−1; as an affine space, it is generated
by c1 , ..., cr−1, cr , where cr = c(Ω).
The simplex π (Ω) = L ∩ Ω is therefore embedded as the intersection of the
affine subspace L ⊂ V with Ω. L ⊂ Aff Ω is also affinely generated by ω1 , ...., ωr ∈
Aff Ω. When viewed as vectors in V (the vector space of dimension one greater
than Aff Ω), ω1 , ..., ωr are orthonormal. Defining L̃ as the linear span of ω1 , ..., ωr
in V , we have that L = L̃ ∩ Aff Ω. From this it follows that π (Ω) := L ∩ Ω is just
the intersection of Ω with the subspace L̃ = lin {ω1 , ..., ωr } ⊆ V .
We will show that this intersection L̃ ∩ Ω is the simplex △(ω1 , ...., ωr ). Recall (Proposition 3.6, item 4) that the extremal points ω1 , ..., ωr are orthonormal
in V , and are therefore an orthonormal basis for their span L̃. By the self-duality
of V+ , ω1 , ..., ωr are also on extremal rays of the dual cone with respect to the
inner product. So everything in V+ has nonnegative inner product with each of
ω1 , ..., ωr . These constraints impose in particular that L̃∩V+ lies in the closed positive halfspaces Hi+ := {x ∈ L̃ : (ωi , x) ≥ 0}, i ∈ {1, ..., r} of each the hyperplanes
Hi = {x ∈ L̃ : (ωi , x) = 0} in L̃. These constraints define a polyhedral cone which
(using the mutual orthogonality of the ωi ) is identical to the cone over the simplex
△(ω1 , ..., ωr ). Since ω1 , ..., ωr are in V+ and in L̃, we know that L̃ ∩V+ contains
this cone, and since we have just shown that L̃ ∩V+ is contained in this cone, we
have that L̃ ∩V+ is equal to it, and hence that π (Ω) := L̃ ∩ Ω = △(ω1 , ..., ωr ).
Since the states ω1 , . . ., ωr are the vertices of the Farran-Robertson polytope
of Ω, the faces F1 , ..., Fr of the polytope defined by the formula (5) are a maximal
flag of that polytope. Then by Proposition 7.14, the faces HFi of Ω are also a
maximal flag of Ω. Since HFi is Gc(Fi) .F, c(Fi ) is the centroid of HFi . Since
35 This was equivalent to its being linearly generated by c , ..., c
1
r−1 when we had identified cr

with 0 ∈ E.

<!-- page 46 -->
46
c(Fi ) = (1/i) ∑ij=1 ωi , HFi is the face of Ω generated by ω1 , ..., ωi, i.e.
HFi =

i
_

i=1

ωi , i ∈ {1, ..., r}.

(6)

So by Lemma 9.2, ω1 , ..., ωi are a frame in Ω, not merely in π (Ω), and ω1 , ..., ωr
is a maximal frame.
We now have results sufficient to prove Theorem 1.1, which we reiterate here.
Theorem 1.1. A convex compact set is strongly symmetric and spectral if and
only if it is a simplex or affinely isomorphic to the space of normalized states of a
simple Euclidean Jordan algebra.
Proof. The “if” direction, that Euclidean Jordan algebra state spaces and simplices are strongly symmetric and spectral, was already known [5] based on known
results about Euclidean Jordan algebras); an explicit proof was reviewed in Sections 4 and 5.
By Propositions 9.1 and 9.3, the strongly symmetric spectral convex compact
sets are all to be found among the regular convex compact sets whose FarranRobertson polytope is a simplex. Since a regular polytope is its own FarranRobertson polytope, the only polytopes that are strongly symmetric and spectral
are the simplices, of every dimension. To identify the nonpolytopal strongly symmetric spectral compact convex sets we will use the Madden-Robertson classification of nonpolytopal regular convex bodies B in En , which is given in Tables 2,
3 and 4 (Tables 2, 3 and 4 of [8]). Because each regular compact convex set admits a canonical embedding as a regular convex body in En , with symmetry group
equal to its affine automorphism group (Prop. 7.2) all regular compact convex sets
appear in the table. Conversely all table entries correspond to regular convex compact sets, because all regular convex bodies, considered as convex compact sets,
i.e. forgetting about the Euclidean and vector space structure of En , are regular
(see Proposition 7.8).
All possibilities for nonpolytopal strongly symmetric spectral convex bodies
are found among the entries of Tables 2, 3 and 4: they are the cases whose FarranRobertson polytope is a simplex. For each such case, Theorem 8.12 tells us, the
given data suffices to determine, up to isomorphism, the regular convex body as
the convex hull of the orbit of a (positive scalar multiple of a) fundamental weight
in a, corresponding to one of the ends of the Coxeter diagram associated with the
Weyl group. The entries with simplicial polytope are those for which the polytope

<!-- page 47 -->
47
is explicitly indicated to be a simplex, and the cases q = 1 of families where the
polytope is ✷q or ✸q , since ✷1 = ✸1 = △1 , the closed line segment, which is the
unique 1-dimensional polytope.
Theorem 6.1, which states that strongly symmetric spectral convex bodies
whose maximal frames have size two must be balls, establishes that the ✷1 and
✸1 cases in the tables in [8] (as well as the △1 cases) all have Ω a ball of some
dimension; these are Jordan-algebraic normalized state spaces (for the spin factors).36
In each of the symmetric space representations in these tables, the regular
convex body is determined, up to isomorphism, by the regular polytope π (B)
and the symmetric space. A comparison of the cases with simplicial polytopes
△n for n ≥ 2 with our Table 1 (taken from [19]) shows that they all correspond to
polar representations K y p0 of compact groups K coming from simple Euclidean
Jordan algebras V ≃ p = p0 ⊕ Re, where e is the Jordan unit. These are indicated
in the rightmost columns of Tables 2, 3 and 4. By Proposition 9.3, in the strongly
symmetric spectral cases, π (B) is a simplex, and as embedded in V , its vertices are
a maximal frame. The maximal abelian subspaces of V ≃ p (viewed as subspaces
of g = lie(Aut V+ )) are of the form a0 ⊕ Re, where a0 are the maximal abelian
subspaces of p0 . In, for example, [19], Proposition VI.3.3, and the discussion
preceding it, the Peirce decomposition ⊕ri, j=1Vi j of a simple EJA of rank r is used,
and it is observed that a = ⊕iVii where Vii = Rci , and the ci , i ∈ {1, . . . , r} are a
Jordan frame. With Ω defined as usual as the normalized state space embedded
in V = p, with the Jordan unit e as order unit, we have that a ∩ Ω is the simplex
generated by the ci , which is affinely isomorphic to a0 ∩ Ω0 , where Ω0 := Ω −
e/tr e = Ω − e/r is the translation of the normalized Jordan state space into a0 .
This exhibits the strongly symmetric compact convex set Ω as affinely isomorphic
to the K-orbit Ω0 of a Farran-Robertson polytope Ω0 ∩ a0 , which is a simplex.
Because according to the Madden-Robertson classification the Farran-Robertson
polytope determines, up to isomorphism, the regular convex body obtained as its
G-orbit in a symmetric space representation, and all regular convex bodies (up to
isomorphism) are obtained in this way, all strongly symmetric convex bodies are
isomorphic to Jordan state spaces.
36 Appendix C includes a case-by-case examination of the ✷ and ✸ cases, but this is not
1
1

necessary for the proof. It includes the cases in which the symmetric space is that associated with
a spin factor (noted in the “EJA” column in Tables 2, 3 and 4), as well as the infinite series of
symmetric spaces of type AIII and CII which illustrate the fact that balls Bd may have actions by
affine automorphisms, transitive on the sphere ∂e Bd ≃ Sd−1 , of proper subgroups of the obvious
rotation group SO(d).

<!-- page 48 -->
48
Remark 9.4. The reader may wonder how the irreducible Riemannian symmetric
spaces H/K relate to the cones of squares in simple EJAs associated with the polar representation, since the interiors of these cones are precisely the irreducible
symmetric cones, meaning the irreducible open cones37 V+◦ that are noncompact
Riemannian symmetric spaces Aut 0 (V+◦ )/K (where K is a maximal compact connected subgroup) on which Aut (V+◦ ) acts via isometries. Writing V+ := V+◦ , note
that Aut V+◦ = Aut V+ . The answer lies in recalling that the (reductive) lie algebra
of G = Aut V+ has in general a Cartan decomposition g = k ⊕ p, with respect to
which p can be identified with the Jordan algebra V , and then V+ = exp p (cf. e.g.
[19]). However, for simple Jordan algebras also g = gss ⊕ R, where R generates
the uniform dilations and the semisimple part gss is simple, and when we further
break down gss = k ⊕ p0 , we see that p0 is the traceless38 part of p, which goes under exp to the component of the unit-determinant part of p that lies in V+ , which
is in fact a symmetric space H/K for H ≡ Gss , the semisimple part of Aut V+ .
The symmetric cone is in fact a reducible symmetric space, the product of H/K
with R.39 The R factor gives the flat direction in the tangent space of V+ , i.e.
the direction along a ray from the origin. The interior of V+ is the cone over the
irreducible symmetric space associated with the representation. A nice example
is the Lorentz cone, in which H/K is a paraboloid inside the cone, with focus
on the axis of rotational symmetry, and is in fact an orbit of the (connected, also
known as “orthochronous”) Lorentz group; the full cone is obtained by including
dilations. When V is not simple, everything still works roughly as before except
that now the symmetric space is a product ×ki=1 (Hi /Ki × R) ≃ (×ki=1 Hi /Ki ) × Rk
of irreducible symmetric spaces, with Rk reflecting the possibility of independent
dilations of the cones over the simple factors Hi /Ki .
♦

10 Discussion
We have characterized a particular subset of the finite-dimensional Jordan algebraic state spaces—those corresponding to simple Euclidean Jordan algebras, and
to finite products of the one-dimensional Euclidean Jordan algebra—as those convex sets satisfying the properties of spectrality and strong symmetry. In this sec37

with pointed closure, i.e. proper cones rather than wedges.
We remind the reader that trace and determinant are defined for EJAs in general (cf. [19]),
and coincide with the usual matrix notions in the matrix cases Herm(n, D).)
39 Concretely, the second factor is represented as R , but it is equipped with the multiplicative
+
group structure, isomorphic (via the exponential map) to the additive group structure on R.
38

<!-- page 49 -->
49
tion, we consider extensions and implications of this result. First we discuss various known ways in which the two properties can be supplemented with additional
ones to characterize precisely the state spaces of complex quantum theory. Then
we discuss some other characterizations of this class, or more general classes,
of Jordan-algebraic state spaces, and how these relate to our work. Finally we
review work in the setting of general probabilistic theories that derives strong
consequences from the conjunction of spectrality and strong symmetry, or from
sets of postulates that can be shown to imply these two properties, emphasizing
the new light our result throws on this work.

10.1 From Jordan algebra state spaces to complex quantum
theory
Characterizations of quantum state space, whether in terms of postulates whose
appeal is mathematical, physical, informational, or some combination of these,
often proceed by first characterizing Jordan-algebraic state spaces, or some subset
thereof, and then adding an additional postulate or set of postulates that narrows
things down to standard, i.e. complex, quantum theory. In the following two
subsections we describe two important classes of such postulates. These can, of
course, be used in conjunction with Theorem 1.1 to characterize the irreducible
complex quantum systems.
10.1.1 From Jordan state spaces to complex quantum theory via relations
between continuous symmetries and observables
The important characterizations by Alfsen and Shultz ([40], cf. [1]) of the state
spaces of two natural classes of Euclidean Jordan algebras, the JB-algebras and
the JBW-algebras, which are Jordan analogues of the C∗ -algebras and the von
Neumann algebras, were extended by them to characterize the state spaces of C∗ algebras and von Neumann algebras (each of which reduces to direct sums of
the state spaces of standard complex quantum theory, in the finite-dimensional
setting), in several ways. One of these, by Proposition 10.27 of [1], is to postulate
the existence of a “dynamical correspondence” ([1], Definition 6.10), on the JBalgebra A. The dynamical correspondence determines a unique C∗ product on A +
iA. In the special case in which the JB-algebra is a JBW-algebra, the dynamical
correspondences on A are in bijection with the Connes orientations (Theorem 6.18
of [1]); the existence of either of these determines a unique W ∗ product on A + iA,

<!-- page 50 -->
50
and the normal state space of A is isomorphic to the normal state space of this von
Neumann algebra.
A dynamical correspondence ψ on a JB-algebra A is a linear map, ψ : a 7→ ψa ,
of A into the set of skew order-derivations of A, satisfying certain properties. It
is called complete if it is surjective (note, also, that there is no requirement that
it be injective). The order-derivations are the elements of the Lie algebra autV+
of the group of affine automorphisms of the positive cone of a Jordan algebra.
This is the span of two complementary subspaces, the self-adjoint (also called
symmetric) and skew-adjoint (also called skew) order derivations, which in the
finite-dimensional case are the −1 and +1 eigenspaces, respectively, usually denoted p and k, of the Cartan involution on autV+ . The self-adjoint ones may be
identified with the space of Jordan multiplication operators, La : b 7→ a • b. The
skew order-derivations are precisely the generators of one-parameter groups of
automorphisms of the Jordan algebra (cf. Lemma 2.81 of [1]). The Jordan automorphisms are also precisely the Jordan unit preserving automorphisms of the
cone of unnormalized states, and hence in a manifestly self-dual representation
in our finite-dimensional setting, they are also precisely the (linearized extensions
of) affine automorphisms of A’s normalized state space (cf. [19]). The conditions
defining a dynamical correspondence are (1) that the commutator of the images
of Jordan algebra elements a and b is the negative of the commutator of the corresponding Jordan multiplication operators, that is, that [ψa , ψb ] = −[La , Lb ], and
(2) that the image of an element annihilate that element, ψa a = 0.
The first of these conditions requires Jordan structure for its formulation. As
Alfsen and Shultz note, their notion of dynamical correspondence “axiomatizes
the transition h 7→ Lih from the self-adjoint part of a C∗ -algebra to the set of
skew order-derivations on the algebra.” The appearance of the minus sign in the
commutator when one moves between commutators of Jordan algebra multiplication operators (which as noted above are the selfadjoint part of autV+ ) and the
Lie bracket of generators of reversible transformations (the skew-adjoint part of
autV+ ) reflects the close relation of this transition to the existence of a complex
structure on autV+ . Such a complex structure, compatible with Lie brackets and
the Cartan involution, is what Alfsen and Shultz ([1], Definition 6.8) call a Connes
orientation on a JB-algebra.
The second condition can be rephrased as saying that the one-parameter dynamical group generated by the image ψa of an observable a conserves that observable, so it can easily be reformulated, in our setting, in a way that refers
only to convex, and not to Jordan, structure, using the abovementioned identification of the Jordan automorphisms with the order-unit-preserving affine order-

<!-- page 51 -->
51
automorphisms of the cone over the effects.
In finite dimension, Alfsen and Shultz’ results (Theorem 6.15 or Proposition
10.27 of [1]) combined with the main result of the present paper imply that that
the conjunction of spectrality, strong symmetry, and the existence of a dynamical
correspondence, characterizes complex quantum theory and classical theory, that
is, the normalized state spaces of Jordan algebras corresponding to the Hermitian
parts of full matrix algebras over C, and simplices.
Proposition 10.1. Let Ω be a finite dimensional convex compact set satisfying (1)
spectrality, (2) strong symmetry, and (3) dynamical correspondence, or equivalently the existence of a Connes orientation. Then Ω is affinely isomorphic to the
normalized state space of the Jordan algebra Herm(n, C), i.e. the set of density
matrices of a finite-dimensional quantum system, or to a simplex, i.e. the state
space of a finite-dimensional classical system.
Another assumption is then needed to rule out classical theory (i.e., the simplices). Many natural alternatives are known, and among these we mention: existence of a tradeoff between information gained about an unknown state, and disturbance to that state (a result reported in [41]); impossibility of universal cloning,
or of universal broadcasting [42, 43], the existence of a state having two different convex decompositions into pure states (a more or less folkloric mathematical
fact that is the finite-dimensional case of Choquet’s theorem); the lack of universal compatibility of measurements [44]; nontriviality of the connected identity
component of the automorphism group of the normalized states (emphasized by
Hardy [45, 46]).
The authors of [5] narrowed down the class of Jordan algebras characterized
there to the complex quantum state spaces, using a principle they call energy observability.
Definition 10.2. A normalized state space Ω is said to have energy observability
([5], Def. 30) if the Lie algebra aut Ω of Aut Ω is nontrivial and there exists
an injective linear map ϕ from aut Ω to the observable space V ∗ of the system,
such that for each x ∈ aut Ω, ϕ (x) is conserved by the one-parameter subgroup
generated by x, and ϕ (x) = λ u (for some λ ∈ R) if and only if x = 0.
Energy observability is closely related to dynamical correspondence, but it
is formulated in the convex framework without reference to Jordan structure, incorporates nontriviality of the connected automorphism group of Ω, and differs

<!-- page 52 -->
52
from the existence of a dynamical correspondence in other ways. The terminology is motivated by the idea that a continuous one-parameter subgroup of automorphisms is a potential dynamical time-evolution, and in quantum physics the
generator of such an evolution is a Hermitian operator H (the Hamiltonian) conserved by the evolution (identified with energy). Here “generator” is meant
in
√
iHt
40
the “physicists” sense that the evolution operator is ω 7→ e (where i = −1).
The assumption that aut Ω is nontrivial is there because without it there is nothing
that fits the intuitive notion of energy that inspired the definition. (And if we were
to formally extend the above definition to that situation, energy would, logically
speaking, be observable because anything is true of the empty set.) However, it
should also be noted that this nontriviality assumption is doing the work of ruling
out classical theory.
Proposition 10.3. Let Ω be a finite dimensional convex compact set satisfying (1)
spectrality, (2) strong symmetry, and (3) energy observability. Then Ω is affinely
isomorphic to the normalized state space of the Jordan algebra Herm(n, C), i.e.
the set of density matrices of a finite-dimensional quantum system.
The relation of energy observability to dynamical correspondence is, roughly,
that a dynamical correspondence is a linear map (but not necessarily an injection41 ) of observables into the Lie algebra, i.e. in the opposite direction from the
map required by energy observability, and also that dynamical correspondence imposes some conditions of compatibility with the Jordan structure, while the notion
of energy observability uses only the convex structure of the state space and does
not need Jordan structure for its definition. The conservation conditions are essentially the same for the two notions (modulo the reversal of direction of the map).
The possibility of noninjectivity of dynamical correspondences is needed in order
to allow some non-simple Jordan algebras to have dynamical correspondences: for
example, a finite product of one-dimensional Jordan algebras—which corresponds
to a finite-dimensional classical system, has trivial (zero-dimensional) aut Ω, but
may still have a dynamical correspondence, because all observables can map to
the unique element 0 of aut Ω; more generally, for a product of nontrivial Jordan
algebras, observables that are linear combinations of the Jordan units of the simple
factors will map to zero.
40 In the usual mathematical terminology, the generator of this evolution is instead the anti-

Hermitian operator iH; then the injection from the Lie algebra of generators of one-parameter
subgroups of automorphisms (i.e. lie(Aut (Ω)) ≡ aut Ω) into the observables is just X 7→ −iX.
41 In [5] (on p. 29) dynamical correspondences are mistakenly described as injections; they are
injective in the simple case, which is the one under consideration there, but not in general.

<!-- page 53 -->
53
We have already mentioned the close relation of the existence of a dynamical
correspondence to Connes’ condition of the existence of an orientation. In [47]
Connes defined an orientation in the setting of self-dual cones V+ in (not necessarily finite-dimensional) Hilbert spaces. The Lie algebra of the automorphism
group of such a cone is involutive, and an orientation on such a cone was defined as a complex structure on the Lie algebra of aut V+ compatible with this
involution. Connes showed that the existence of an orientation characterizes the
positive cones of von Neumann algebras within the class of self-dual, facially homogeneous cones in Hilbert spaces ([47], Théorème 5.2). Since Bellissard and
Iochum [48] showed that these are precisely the positive cones of JBW algebras,
this provides a way of characterizing the von Neumann algebra state spaces within
the class of JBW algebraic ones. Alfsen and Shultz explicitly transferred the definition of Connes orientation to JBW-algebraic state spaces and established, in
Theorem 6.18 of [1], a bijection between Connes orientations in the sense of their
Definition 6.8 ([1]) and dynamical correspondences in the JBW-algebraic case.
10.1.2 From Jordan state spaces to complex quantum theory via local tomography
A different approach to ruling out the Jordan algebraic systems other than complex
quantum theory involves introducing an appropriate notion of composite system
consisting of two or more “subsystems”. The existence of “tomographically local” Jordan-algebraic composites of Jordan-algebraic systems can then be used as
a postulate to narrow things down to complex quantum systems. Tomographic
locality can be mathematically formulated as the requirement that the ambient
vector space VAB spanned by the cone of unnormalized states of a composite
of systems A, B whose ambient vector spaces are VA and VB , be the real tensor
product VA ⊗ VB .42 In [24] it was shown that the existence of a locally tomographic Jordan-algebraic composite of a Jordan-algebraic system A with a qubit
(the lowest-dimensional nontrivial complex quantum system, whose state space
is a three-dimensional ball), satisfying some other natural desiderata, implies that
A must be complex quantum. However, this does not rule out the possibility of
42 The notion of “tomography” in this context is that of determining the state of a system by

making various measurements on identically prepared copies of a system. “Local” tomography
of a composite system is possible if one can estimate the state by making measurements on its
parts, A and B, and estimating the correlations between sufficiently many measurement results. If
VAB = VA ⊗VB , then products of effects eA ⊗ fB span the dual of the state space, so determining the
probabilities of a spanning set allows one to determine the components of the state in a basis.

<!-- page 54 -->
54
theories whose systems are spectral and strongly symmetric but in which qubits
do not occur as a system type that must be composable with other systems.
In [49], Ll. Masanes and M. Müller formulated five postulates applicable to
theories whose systems are described in the GPT framework, and showed that the
only two theories satisfying them are finite-dimensional complex quantum theory
and finite-dimensional classical theory. One of these postulates is that composite
systems are locally tomographic. Their notion of theory is somewhat implicit in
their arguments, rather than fully explicit, but it appears to require that for any two
systems of the theory, there exists another system of the theory that is a locally tomographic composite of those systems. Since the four postulates not referring to
composite systems are satisfied by all systems with simple Jordan algebraic state
spaces, and by systems whose state spaces are simplices, we can combine their
result with the main result of this paper to conclude that any collection of (finitedimensional) systems satisfying strong symmetry and spectrality, and closed under the formation of composites, must consist either entirely of complex quantum
systems, or entirely of classical systems.
That the tomographic locality of the assumed composites is necessary for these
results is indicated, for example, by the constructions in [50] of theories in which
some of the Jordan algebraic systems other than complex quantum ones can be
combined to form composites that are not tomographically local; these theories
even have the additional structure of dagger compact closed categories (the terminology of [51] for a notion earlier defined in [52]). In addition to the category of irreducible complex quantum systems, there is the category of real quantum systems, and another category that includes all irreducible real and quaternionic quantum systems. A third additional category allows the inclusion of real,
quaternionic, and complex systems in a single category, at the price of a notion of
composite that does not preserve irreducibility. Not all Jordan algebraic systems
occur in these constructions, though: the spin factors whose state spaces are dballs for d ∈
/ {1, 2, 3, 5} do not occur in these categories, nor does the exceptional
Jordan-algebraic system.43 The lattter, indeed, does not have Jordan-algebraic
composites, tomographically local or not, with nonclassical Jordan-algebraic systems ([50], Corollary 4.10), and Example 6.2 in [50] suggests that there may be
obstructions to Jordan-algebraic composites involving the spin factors whose state
spaces are the d-balls for d = 4 and d ≥ 6 as well. (References to [50] are to arXiv
version v2.)
43 The d-balls with d ∈ {1, 2, 3, 5} are the classical, real quantum, complex quantum, and quater-

nionic quantum bits, respectively.

<!-- page 55 -->
55
A similar argument involving tomographic locality can be made using the result of [53], in which it is shown that only for d = 3 does there exist a composite, satisfying tomographic locality and continuous reversible transitivity on pure
states, of two systems each of which has a Euclidean d-ball as state space. Since
by Theorem 1.1 (cf. Theorem 6.1), spectrality and strong symmetry imply that
bits are balls, and also that nonclassical systems are simple Jordan-algebraic and
hence have continuous reversible transitivity on pure states, it follows from Theorem 1.1 and [53] that no tomographically local composite of a bit with itself can
preserve spectrality and strong symmetry, except in the complex quantum case
(for which bits are 3-balls) or the classical case.

10.2 Relations with other characterizations of Jordan algebraic
classes of state spaces
Jordan algebraic systems share with standard (i.e. complex) quantum theory many
geometric properties of informational and physical significance in addition to
spectrality and strong symmetry. These include the absence of higher-order interference [54, 55]; purity-preserving projectivity [56, 1, 5]; homogeneity and selfduality. Obviously, Theorem 1.1 implies that systems with spectrality and strong
symmetry have these other properties too. This raises the question of whether
the theorem could be proved differently, by establishing a direct implication from
spectrality and strong symmetry to combinations of these other properties sufficient to establish the Jordan algebraic nature of the state space. For example, as
noted in Proposition 3.6 it is known [5] that spectrality and strong symmetry imply
self-duality of the cone over the normalized state space. In light of the KoecherVinberg theorem [22, 23], which states that the homogeneous self-dual cones are
precisely the Jordan-algebraic ones, one could therefore try to show directly that
spectrality and strong symmetry imply homogeneity. Similarly, it is known [5]
that the conjunction of spectrality and strong symmetry implies projectivity of the
state space in the sense that each face is the positive part of the image of a projection that is the dual of (and hence, given self-duality of the cone, identical to)
what Alfsen and Shultz call a compression. Since self-duality near-trivially implies Alfsen and Shultz’ postulate of symmetry of transition probabilities (STP),
and the finite-dimensional case of their theorem characterizing the state spaces of
a wide class of Euclidean Jordan algebras has projectivity, symmetry of transition probabilities, and one of several other properties (equivalent in the context of
projectivity and STP) as premises, we would just need to establish a direct im-

<!-- page 56 -->
56
plication from spectrality and strong symmetry to one of these other properties
to obtain a direct proof of the Jordan structure. The most promising choice is
perhaps the preservation of purity by the duals of compressions: that the image
of a pure state under a compression is always a multiple of a pure state. In fact,
the result in [5] was obtained by showing that the duals of compressions preserve
purity—but the additional assumption of absence of higher-order interference was
used in showing this.
Alternative properties capable of characterizing the Jordan-algebraic state spaces
among those satisfying Alfsen and Shultz’s conditions of projectivity and symmetry of transition probabilities are (1) the Hilbert ball property, or (2) the satisfaction of the atomic covering law by the lattice of faces of the state space. A finitedimensional convex set has Alfsen and Shultz’ Hilbert ball property if and only if
for every pair of extreme points of Ω, the face they generate is affinely isomorphic
to a Euclidean ball. (See [1], Def. 9.9, for additional technical conditions relevant in infinite dimension.) The atomic covering law for a lower-bounded lattice
states that if a is an atom in the lattice, and b any element of the lattice, then either
a ∨ b = b, or a ∨ b covers b. Here “x covers y” means x > y and there exists no w
such that x > w > y, i.e. x is above y and there is nothing between them, and an
atom is an element that covers 0. So an alternative proof of our result could also
aim at establishing either one of these properties directly. By the main result of [5]
a direct proof of the absence of higher-order interference (see the next subsection
for a rough definition) from spectrality and strong symmetry would also do the
job.

10.3 Implications for other results on general probabilistic theories having spectrality and strong symmetry
10.3.1 Higher order interference
In [57] Rafael Sorkin introduced a notion of a hierarchy of orders or degrees of
probabilistic interference, one for each positive integer, for physical theories modeled in a “histories” framework. In [58, 55, 59] Sorkin’s notion was adapted to
the GPT framework. Roughly speaking, interference of order k represents the
idea that there are processes in which k or more mutually exclusive “paths” or
“histories” are available to the system, such that there is a measurement whose
probabilities, when measured on a system that has undergone such a process, cannot be determined from the probabilities in all situations in which k − 1 or fewer
of the paths are available. Quantum theory has interference of order at most 2 (the

<!-- page 57 -->
57
lowest order that intuitively represents interference, since theories with maximal
interference order of 1 are classical). If a theory fails to have interference of order
k, then it can have no interference of order k + 1 or higher. We call interference
of order 3 or above higher-order interference. As mentioned in the introduction,
Theorem 1.1 improves on the main result of [5], which characterized the same
class of theories, but in addition to spectrality and strong symmetry, used the additional assumption of no higher-order interference.
10.3.2 Query computation and query complexity
In query problem in the theory of computation, it is assumed that one has access to
a sequence, parametrized by “instance size” n, of “black boxes” capable of computing a function fn between finite sets (the usual case is f : {0, 1}n → {0, 1}). fn
is not known, but a finite family Fn of possible functions is specified; sometimes a
prior distribution over Fn is specified as well. One may then ask about the “query
complexity” of computing some function gn whose domain is the family of functions Fn ; roughly speaking, this is the number of times the black box appears in a
circuit capable of computing, with high probability of success (either in the worst
case or, in case a prior distribution on Fn has been specified, in expectation with
respect to that distribution), the function gn . The circuit is realized in some background circuit model of computation, such as a classical or quantum circuit model,
and the behavior of the black boxes may also be classical, quantum, or more general, giving rise to a variety of possible query models of computation. Typically
one is concerned with how the number of queries scales with the input size n. For
example, in Grover’s “search problem” of “identifying a marked state”, for which
the instance size parameter is usually written as N, FN , of cardinality N, is the
set of functions {1, ..., N} → {0, 1} that take the value 1 on exactly one element
of its domain {1, ..., N}, usually termed the “marked state”. In Grover’s problem
gN : FN → {1, ..., N} is the function that identifies which of these N possibilities
for fN is computed by the black box, i.e. which state is marked. Grover’s celebrated quantum
query algorithm [60, 61] computes gN with a number of queries
√
of order N. In the closely related query problem of computing OR, FN consists
of all N 2 functions {1, ..., N} → {0, 1} and gN is OR of the values of fN on all its
inputs, i.e. gN ( fN ) is 1 if fN is zero on all N inputs, otherwise it is 1. A variant
√ of
Grover’s algorithm computes OR, again with a number of queries of order N.
In [6] it was shown, in a reasonable query model generalizing the quantum
query model, that five principles, of which the fifth is strong symmetry, imply that to have probability 1/2 or greater of correctly identifying the marked

<!-- page 58 -->
58
state
in Grover’s search problem, the number of queries must be at least (3/2 −
√ p
2) N/h, where √
h is the maximal “order of interference” of the GPT theory. A
lower bound of Ω( N) was established in the quantum
√ case in [9]; it is achieved
by Grover’s algorithm. The bound in [6] is also Ω( N). This limits the potential
√
gain from higher-order interference of degree h to at most a constant factor, c/ h
compared to quantum. The authors of [6] argued that their result is “somewhat
surprising as one might expect more interference to imply more computational
power”.
However, it can be shown (cf. [10]) that the conjunction of the principles
used in [6] implies spectrality. Together with Theorem 1.1 this implies that the
GPT systems considered in [6] are Jordan-algebraic, and hence that the order h
of interference is at most 2 [55, 54]. The question of whether or not higher-order
interference of some fixed maximal degree can give a non-constant asymptotic
speedup (in terms of number of queries) over Grover’s quantum algorithm for the
Grover search problem in some GPT with a reasonable query model remains open,
but our results imply that if such a speedup is possible it will be in a setting not
allowed by the postulates in [6].
Besides strong symmetry, the assumptions in [6] are causality (roughly, no signaling from the future, which is implicit in the setting of this paper, and most work
on GPTs, because of the uniqueness of the order unit u), purification (every state
on a system A arises as the marginal of a pure state on a possibly larger composite
system AB, and any two such purifications are related by an automorphism of ΩB ),
purity preservation under composition, and the existence of a pure sharp effect. It
is not explicitly stated whether one must assume purity preservation under both
parallel and sequential composition, but it appears that only parallel composition
is used in the proofs. Even with strong symmetry omitted, and purity preservation
required only under parallel composition, the conjunction of these conditions is
an extremely strong assumption,44 since if they are augmented with purity preservation under pure operations,45 they would already imply the Jordan-algebraic
nature of the state space (though not the restriction to simple Jordan algebras or
simplices), as shown in [62]. However, since to the best of our knowledge purity
44 Most of the strength of this conjunction lies in purification, purity preservation under parallel

composition, and the existence of a pure sharp effect, since causality is part of essentially every
definition of composite system in the GPT framework. The existence of a pure sharp effect would
follow from the other conditions and the no-restriction hypothesis, which, although also quite
strong in its way, is a natural and oft-made assumption in the GPT framework.
45 Pure operations are linear maps that lie in extremal rays of the cone of “allowed” positive
maps on the state space.

<!-- page 59 -->
59
preservation under sequential composition of pure operations was not previously
known to follow from the other assumptions, the possibility that the assumptions
of [6] still allow for higher-order interference was open until it was excluded by
the main result of the present paper.
In [11], a definition of query computation was formulated and two results
were obtained concerning query computation in general probabilistic theories under nearly the same assumptions as [6]: the ubiquitous (and innocuous) causality,
purification, purity preservation under parallel composition, and strong symmetry,
as well as preservation of the maximally mixed state (centroid of the state space)
under parallel composition.46 Pure sharpness was not explicitly assumed, but the
results of the paper involve situations in which nontrivial sets of perfectly distinguishable states exist, which are needed for the function queries to be possible,
and the existence of such sets can be shown to imply pure sharpness; indeed, in
[11] the cone of unnormalized states is shown to be not only self-dual, but perfect.
The first main result of [11] was that if kn classical queries yield no information
concerning a function to be computed, then in a general probabilistic model with
maximal order of interference k, n queries yield no information. This allows one
to obtain, from classical zero-information lower bounds on the number of queries
needed to compute or approximate properties of a black-box function f , lower
bounds in more general models, but it neither rules out nor definitely establishes
the possibility of speedups over quantum query computation in more general GPT
models. It generalizes a result of Meyer and Pommersheim [63], who studied the
quantum case. The second main result of [11] was a confirmation that the generalization (from the classical and quantum cases) of the notion of black-box query
used there is reasonable, in the sense that if there is a polynomial-size family of
GPT circuits C f for a family of functions f , one can use them to simulate the
black-box queries to the functions f , with a polynomial family of circuits. Much
of the interest in query algorithms, both quantum and classical, implicitly relies
on this type of result, since they allow one to pass with at most polynomial cost
from query algorithms to concrete circuit algorithms in cases where circuits for
the function f exist—giving rise to efficient algorithms in cases where the amount
of resources required by the query algorithm for the computation interleaved between the queries is also polynomial.
The absence of an explicit assumption of sequential purity preservation is the
only thing distinguishing the assumptions (excluding strong symmetry but including pure sharpness) of [11] from those of sharp theories with purification (which
46

This last may well follow from the others.

<!-- page 60 -->
60
are known to have Jordan-algebraic state spaces). But without sequential purity
preservation, it was still not clear that the systems of [11] are Jordan algebraic.
However, they do have spectrality so, as in the case of [6], Theorem 1.1 implies
that these theories, too, have Jordan-algebraic state spaces, and cannot exhibit
higher-order interference. This should motivate attempts to extend these results to
more general settings.
10.3.3 Entropic and thermodynamic aspects of probabilistic theories
In [3], spectrality and strong symmetry were used to obtain important properties
of quantum entropy and entropy-like quantities in a more general context. Given
spectrality, it is natural to investigate real-valued entropy-like functions on the
space of states defined using Schur-concave functions:47 for each such function
f , one defines a corresponding generalized entropy as the value of f on the spectrum of the state.The von Neumann entropy of a quantum state, which is given by
the Shannon entropy H(p) := − ∑i pi ln pi of its spectrum p = {p1 , ..., pn}, is one
such entropy. In general theories, one can define the measurement entropy and the
preparation entropy of states. The measurement entropy of state σ is the minimum, over finegrained measurements, of the Shannon entropy of the probabilities
of the outcomes when the measurement is made on a system in state σ ; the preparation entropy is the minimum entropy of probabilities pi such that σ = ∑i pi ωi ,
for pure states ωi . Analogous definitions can also be made for the generalized
entropies determined by Schur-concave functions other than Shannon entropy. In
quantum theory, the preparation and measurement entropies corresponding to a
given f are equal to each other and to the spectral entropy corresponding to f .
In [3], it was shown, assuming spectrality and strong symmetry, that the outcome
probabilities of any fine-grained measurement on σ are majorized by those of
47 A function f : Rn → R is called Schur-concave if whenever x majorizes y, f (y) ≥ f (x). x is

↓
↓
m
↓ ↓
said to majorize y, for x, y ∈ Rn , if for all m ∈ {1, .., n}, it holds that ∑m
i=1 xm ≥ ∑i=1 ym , where x , y
are the vectors whose elements are those of x and y respectively, arranged in decreasing order.
Sometimes Schur-concave functions are considered to have as domain ∪n∈N Rn , in which case
majorization is defined by comparing two vectors with the shorter one padded out with zeros to the
length of the longer one. “x majorizes y” is generally interpreted as a formalization of the idea that
x is “more mixed” or “more random” than y, because of the Birkhoff-von Neumann theorem, which
states that x majorizing y is equivalent to y being a convex combination of vectors obtained from
x by permuting its entries. Schur-concave functions are often viewed as real-valued “measures of
randomness” since they are precisely the real-valued functions that can never decrease under such
operations. This accounts for the terminology “generalized entropies” and also for a relation of
majorization to microcanonical thermodynamics (cf. e.g. [64]).

<!-- page 61 -->
61
the spectral measurement (which are equal to σ ’s spectrum), and hence that the
measurement entropy determined by any Schur-concave function is equal to the
corresponding spectral entropy.48 In parallel work in [4] the same conclusion was
obtained using causality, purification, purity preservation under both parallel and
sequential composition of pure operations, and strong symmetry. The first four
of these assumptions together imply spectrality. So in light of the present paper,
the setting of [3, 4] is no more general than that of simple Jordan-algebraic state
spaces, and classical ones.49 However, the same conclusions can also be obtained
from different postulates, including or implying spectrality, but not strong symmetry. This was done, using different sets of assumptions, in [10], [65], and [66]. In
light of the present work, it becomes even more interesting to determine whether
the assumptions used in these works imply the Jordan algebraic structure of state
space (even if not the simple structure or classicality of the Jordan algebra, which
is enforced by strong symmetry but which does not follow from the assumptions
of [65], [10], or [66]). The results in [10, 66] concern a class of theories they
call sharp theories with purification, which satisfy the four properties of causality, purification, purity preservation (under both parallel and sequential composition), and pure sharpness. In [62] it was shown that all systems in this class
of theories are Jordan-algebraic (although this class is not precisely simple Jordan algebras and classical theory, since some nonclassical nonsimple state spaces
are definitely allowed, and to the best of our knowledge it is not known whether
all simple Jordan algebras are). However, the assumptions of [65] are just projectivity of the state space and symmetry of transition probabilities (equivalently,
projectivity and self-duality of the state cone, which are in turn equivalent ([2],
cf. also [65]) to its perfection together with the normalization of the orthogonal
projections onto the linear spans of faces). All Jordan algebraic state spaces have
these properties, but it is an open question whether they are the only ones. Essentially these assumptions (in the guise of projectivity and symmetry of transition
probabilities) appear in Alfsen and Shultz’s derivation [56, 1] of Jordan-algebraic
structure, but there a choice of one of several additional assumptions, for instance
that the “filters” that project onto faces of the state space take pure states to multiples of pure states or one of the other alternatives discussed above, is used. It is
not known whether or not this assumption can be dropped in the characterization
48 The theorem was stated for the Renyi α -entropies, but the proof uses Schur concavity and

applies to arbitrary Schur concave functions.
49 It should nevertheless be noted that to the best of our knowledge, the conclusions obtained in
[3] and [4] were not previously known for the non-quantum, non-classical simple Jordan algebras.

<!-- page 62 -->
62
of Jordan-algebraic state spaces.50 So, the results of [65] add additional interest
to the question of whether there are non-Jordan-algebraic state spaces satisfying
projectivity and self-duality, while the results of the present paper show that such
state spaces will not be found among those satisfying strong symmetry.

11 Conclusion
We have shown that the finite-dimensional compact convex sets satisfying two
properties, spectrality and strong symmetry, are up to affine isomorphism precisely the sets of normalized states of simple finite-dimensional Euclidean Jordan
algebras, and simplices, answering a question posed in [5] of whether the additional property of no higher-order interference used there in addition to spectrality
and strong symmetry, is needed to characterize this set of state spaces. While this
can be viewed purely as a result in convex geometry, it has important implications for the research program that studies general probabilistic theories, since
significant results in that program were obtained under the assumption that the
normalized state spaces of systems are spectral and strongly symmetric, or under assumptions that imply this; we described some of these implications in the
preceding section. We also discussed the relation of our result to other characterizations of Jordan algebraic state spaces.
These Jordan-algebraic compact convex sets, and the cones over them, figure
in many other areas of mathematics and applications, including complex analysis, symmetric spaces, optimization, and statistics, and the present result may
have interesting implications in some of these areas as well. From the both the
perspective of general probabilistic theories and that of the purely mathematical
theory of convex sets, our results suggest exploring the consequences of assumptions weaker than spectrality and strong symmetry.
50 In [2] H. Araki gave a derivation of Jordan-algebraic structure in finite dimension inspired

by Alfsen and Shultz’s, but using a notion of projection on the state space he calls “filter”, which
is prima facie weaker than the notion of dual of a compression; he also assumed filters preserve
purity, but conjectured the assumption could be dropped. Alfsen and Shultz [1], p. 354, state that
“in the finite-dimensional context his axioms force the filters to be compressions”, but it is not
clear whether this is meant to apply to the axioms without the purity-preservation assumption.

<!-- page 63 -->
63

Acknowledgments
HB thanks the Department of Mathematical Sciences and the QMATH group at
the University of Copenhagen for hosting him as Visiting Professor while investigations preliminary to the present work were undertaken, and the Villum Foundation for making his visit possible through its support of QMATH. Both authors
thank Henrik Schlichtkrull for putting them in contact with each other.

A Proof of Theorem 6.1
In this section we establish Theorem 6.1, following [12] but bringing in the stronger
assumption of 2-transitivity.
Theorem 6.1. Let Ω be a strongly symmetric spectral compact convex body whose
largest frame is of cardinality 2. Then Ω is affinely isomorphic to a ball.
Proof. We view Ω as canonically embedded in the affine space Aff Ω ≃ E that
it generates, of dimension n, equipped with a Euclidean inner product for which
Aut Ω is a subgroup
of O(E), and recall that because Aut Ω acts transitively on
R
∂e Ω, we have that Aut Ω d µ (k) k.ω is a fixed point of the group action, and is in
fact the barycenter, 0. Because it is an orbit of a subgroup of O(V ), the set ∂e Ω of
extremal points of Ω is contained in the sphere S := {x ∈ V : ||x|| = c} with respect
to the associated norm. We scale the inner product by a positive real number so
that c = 1.
We now prove that every pair of perfectly distinguishable points in Ω are the
endpoints of some diameter of S. We begin by showing (following Dakić and
Brukner but with a bit more detail) that for every extremal ω ∈ Ω, the point −ω
also belongs to Ω, and [ω , −ω ] is a 2-frame.
A chord of a sphere is defined to be a closed line segment whose endpoints
are two distinct points on the sphere. We will use the fact that the only chords
of a sphere that contain its center are the diameters, i.e. the chords from x to −x.
Since Ω is spectral with maximal frame size 2, every nonextremal point in Ω, in
particular its center, 0, is a convex combination of two perfectly distinguishable
extremal points of Ω. Let ω0 and ω1 be extremal points of Ω such that 0 is a
convex combination of them. Since we showed above that all extremal points of
Ω lie on the sphere S, the set of convex combinations of ω0 and ω1 is a chord of
S containing its center, 0. Therefore it is a diameter, and ω1 = −ω0 . Since Ω has
reversible transitivity on pure states (i.e. transitivity of Aut Ω on 1-frames, which

<!-- page 64 -->
64
are precisely the extremal points), every extremal point ω of Ω can be obtained
from ω0 by acting with an element of O(V ), whence by linearity of the action,
−ω is also in Ω. So we have established that Ω is symmetric under coordinate
inversion x 7→ −x, and that every pair ω , −ω is a maximal frame.
We still need to show that there are no other maximal frames in Ω, i.e. no
2-frames that are not the endpoints of a diameter.51 If we have transitivity on
2-frames, we get this immediately: every 2-frame is an automorphic image of
(ω0 , −ω0 ), and therefore of the form (ω , −ω ) for some extremal ω .
Once we have this fact, we can use it as in [12] to establish that Ω is a ball.
The centroid of a compact convex set, which is 0 in the case of Ω, is in its relative
interior. Ω is full-dimensional, so its relative interior is its interior, and there is
an open ball around 0 contained in Ω. So for any x ∈ S there is λ ∈ (0, 1] small
enough that λ x ∈ Ω. By spectrality, λ x is a convex combination of two perfectly
distinguishable extremal points of Ω. Since we showed above, using 2-transitivity,
that all such pairs are endpoints of diameters, λ x must be a convex combination
of the endpoints of a diameter. For x ∈ S the only diameter containing λ x 6= 0 is
the one between x and −x. So we have shown that x ∈ Ω; but x was an arbitrary
element of S. Since the entire sphere S belongs to the extreme boundary of the
convex set Ω, and we earlier showed that all extremal points of Ω are in S, Ω is
the convex hull of the (n − 1)-sphere Sn−1 , i.e. an n-dimensional ball.

B Faces of strongly symmetric spectral sets are strongly
symmetric and spectral
In this section we prove the following theorem, which includes item 5 of Proposition 3.6.
Theorem B.1. Let Ω be a strongly symmetric spectral compact convex set. Then
every face of Ω is a strongly symmetric spectral compact convex set; moreover if
F is a face of Ω and K = Aut Ω, then K(F) := KF /K F = Aut F. Here KF is the
subgroup that takes F to itself; K F is the subgroup that fixes F pointwise. Also,
|F|
KF := K c(F) , where c(F) = ∑i=1 ωi /|F|, for any frame ωi for F, is the centroid of
F.
51 This is the main point at which we perceive a gap in the argument in [12] which we do not see

how to easily bridge using only reversible transitivity and strong symmetry.

<!-- page 65 -->
65
Proof. By Proposition 2.4 and the fact that u = ∑ri=1 ωi in a strongly symmetric
compact convex set, where ωi are a maximal frame, and the fact that u is Aut Ωinvariant in our setup, the barycenter of Ω is easily shown to be (∑ri=1 ωi )/r, for
any maximal frame [ω1 , ..., ωr ]. It is easily shown that any face of F is spectral,
since spectrality of Ω asserts, for ω ∈ F, that ω is a convex combination of perfectly distinguishable states, but these states must be in F by the definition of
face, and by Proposition 3.6 they must be extendable to a frame for F. Then one
shows, using strong symmetry, that for each face F of Ω, there is a subgroup of
K := Aut Ω, that preserves lin F and (necessarily or else it could not consist of
automorphisms of Ω) induces automorphisms of F, and acts transitively on the
maximal frames in F. This is immediate from strong symmetry, since the maximal frames in F are |F|-frames in Ω, and strong symmetry says K can take any
|F|-frame (whether in F or not) to any other. One has to show that frames in F
are still frames for F viewed in its affine span, but that is so because the cone
is perfect, and when the dual cone is represented internally via the self-dualizing
inner product, the distinguishing effects are the states themselves (cf. item 4 of
Proposition 3.6). Perfection of the cone V+ implies that the cone over F is selfdual in its linear span according to the restriction of the inner product, so these
effects are still in the relative dual cone of F.
In fact, an element of K takes maximal frames of F to maximal frames of F
if, and only if, it belongs to the subgroup Klin F , that preserves lin F. The action
of this group on lin F gives a faithful representation of the group Klin F /K lin F
(equivalently KF /K F ). Since we have shown that F is spectral and strongly symmetric, it follows from claim in the first sentence of this proof that the barycenter
|F|
of F is ∑i=1 ωi /|F| for any maximal frame ωi for F. Any automorphism of F
preserves its barycenter, so the automorphism of F induced by any element of
KF must do so, i.e. KF ⊆ K c(F) . Furthermore, K c(F) ⊆ KF . To see this, note
that c(F) is in the relative interior of F and therefore F = face(c(F)). Hence for
ϕ ∈ K c(F) we have ϕ (F) = ϕ (face(c( f ))) = faceϕ (c(F)) = face(c(F)) = F, i.e.
ϕ ∈ KF . Here the second equality is a general fact about automorphisms ϕ (that
face(ϕ (x)) = ϕ (face(x))), and the third is from the assumption ϕ ∈ K c(F) .

<!-- page 66 -->
66

C More detail on the classification of regular polytopes via symmetric space representations
C.1 Details of the symmetric space representations containing
regular convex bodies as orbits of Farran-Robertson polytopes
In this subsection we go line by line through those entries in Tables 2, 3 and 4
that describe symmetric spaces associated with simplicial Farran-Robertson polytopes, along the way verifying that all cases where the simplex has 3 or more
vertices (△n , n ≥ 2), are ones associated with EJAs, and for the △1 cases (where
the convex body must be a ball), noting which ones are spin factor Jordan algebra automorphism representations (i.e. lie(K) = lie(Aut V ) ≡ derV ),52 and which
involve other transitive actions on balls.
The nomenclature for groups, symmetric spaces, and root systems is that used
in [8], which is very close to that used in Helgason [39], Ch. X.53 Tables 2 and
3 in [8], reproduced in the first columns of Tables 2 and 3 above, include those
symmetric spaces from Table V in Chapter X of Helgason [39], Table 2 being
the series, Table 3 the exceptional cases. These are the Type I and Type III noncompact symmetric spaces, in Cartan’s nomenclature. The list of coincidences
between different classes of symmetric spaces given in §6.4 of Ch. X of [39] (pp.
519-520) is helpful here too; we refer to these below by Helgason’s enumeration,
e.g. as “coincidence (i)”, etc.
From Table 2: classical symmetric space representations.
AI is the symmetric space SL(n, R)/SO(n) with root space An−1 , whose polytope is the n-vertex simplex, △n−1 . lie(K) = so(n), and the associated polar representation V0 = p0 , from the Cartan decomposition sl(n, R) = so(n) ⊕ p0 , is the
traceless real symmetric matrices. As discussed in Section 4, this is the polar
representation V0 associated with the Jordan algebra V consisting of the real symmetric matrices V0 ⊕ RI (where I is the identity matrix). The regular convex body
is then isomorphic to the unit-trace real symmetric positive semidefinite matrices.
AII is SU ∗(2n)/Sp(n), of rank n − 1, and dimension (n − 1)(2n + 1), with
polytope △n−1 . SU ∗(2n) is also known as SL(n, H), and Sp(n) as SU (n, H).
52 Here V is a Jordan algebra, and Aut V is the compact group of Jordan algebra automorphisms,
with Lie algebra derV .
53 Helgason combines BI and DI in the class BDI, whereas [8] keep them separate.

<!-- page 67 -->
67
The Cartan decomposition is sl(n, H) = su(n, H) ⊕ p0 where p0 is the traceless
quaternionic-Hermitian matrices, so the associated polar representation has SU (n, H) ≡
Sp(n) acting on the traceless quaternionic-Hermitian matrices. The regular convex
compact body of the Madden-Robertson construction is therefore affinely isomorphic to the unit-trace positive semidefinite quaternionic-Hermitian matrices.
Type AIII, SU (p, q)/S(U p ×Uq ), with root system Cq (for p = q) or BCq (for
p > q). Two polytopes are listed here because when q > 1 the two end nodes
of the Dynkin diagrams of Cq are nonequivalent, as are those of BCq , giving rise
to two orbit types in each case. At any rate, only in the case q = 1 are these
simplical polytopes, △1 . The symmetric spaces are then SU (p, 1)/S(U p × U1 ),
the dimension is 2p, and we know that the associated orbitopes are balls B2p by
Theorem 6.1. For p > 1, the root system is of type BC1 , while for p = 1 it is of
type C1 .
The p = 1, q = 1 case corresponds to the spin factor R2 ⊕R, with positive cone
a Lorentz cone with 2 space dimensions, whose base is the disc, by coincidence
(i) of Helgason. (Note that S(U1 ×U1 ) ≃ U (1), with Lie algebra so(2).)
In the p > 1 case, S(U p × U1 ) ≃ U (p)54 acts transitively on B2p . In, for instance, [53] the U (p) and SU (p) representations with transitive action on B2p are
described; for Q ∈ U (p) or SU (p), we have the 2p × 2p real matrix


Re Q Im Q
ρ (Q) =
.
(7)
−Im Q Re Q
For Type BI the simplicial cases are the q = 1 cases of SO(p, q)/(SO(p) ×
SO(q)) for p + q odd, q < p, of type BI, with root space Bq . So we have p > 1
even, and the symmetric space is SO(p, 1)/(SO(p) × SO(1)) ≡ SO(p, 1)/SO(p).
The Cartan decomposition is so(p, 1) = so(p) ⊕ R p , and we have so(p) acting irreducibly on R p . The action is equivalent to the Lie algebra representation derived
from the defining representation of SO(p). This is the polar representation embedded in the spin factor Jordan algebra R p ⊕ R, where the R summand is spanned by
the Jordan identity e, which is fixed by the full SO(n) representation as explained
in Section 4. Its positive cone is a Lorentz cone in one “time” dimension, and even
“space” dimension p, with normalized state space Ω a p-ball. If we write (x,t) for
54 S(U

p ×Uq ) is defined by the (complex) linear representation on C

p ⊕ Cq consisting of block-

diagonal matrices M with blocks in U(p) and U(q) with det M = 1, so S(U p ×U1 ) is isomorphic to
the matrices of the linear representation V ⊕ det∗ of U(p), where V is the defining representation
and det∗ the dual of the one-dimensional determinant representation. This is a faithful representation of U(p).

<!-- page 68 -->
68
a an element of R p ⊕ R, the convex hull of the orbit in the polar representation is
that ball, translated to the plane t = 0.
Type DI with the same group quotient, but p + q even, similarly gives the
Lorentz cones for odd “space” dimension in the q = 1 cases, again as embedded
in spin factors.
The simplicial cases △1 in these two lines (BI and DI) account for all spin
factor isotropy group representations. A few of these will reappear below, due to
coincidences noted in [39].
DIII has q = ⌊n/2⌋, which gives q = 1, and hence △1 , only for n = 2 and n = 3.
For n = 2, the dimension n(n − 1) is 2, and the symmetric space is SO∗ (4)/U (2).
Coincidence (xi) in Helgason’s list indicates that this coincides with type AI (n =
1), i.e real symmetric 2 × 2 matrices Herm(2, R) ≃ R2 ⊕ R, aka the “rebit”, also
appearing as AIII (p = q = 1), DI (p = 2, q = 1) (Helgason’s BDI(p = 2, q = 1)),
and CI (n = 1).
For n = 3, q = 1 we have d = 6. By coincidence (vii) in Helgason, this is
also AIII (p = 3, q = 1). Ω is the 6-ball. The DIII symmetric space is given by
SO∗ (6)/U (3), while p = 3, q = 1 implies the AIII symmetric space is SU (3, 1)/(S(U (3)×
U (1)). The isomorphisms cited in the Helgason coincidence (vii) are su(3, 1) ≃
so∗ (6) and su(4) ≃ so(6), corresponding to the “numerators” in the noncompact
and compact forms of the symmetric space respectively. As for the denominators,
S(U3 ×U1 ) ≃ U (3). A transitive action of U (3) on the 5-sphere (boundary of the
6-ball) is known (cf. Table I in [53]).
Type CI, for n = q = 1, gives Sp(1, R)/U (1), with dimension 2, rank 1. This is
again the 2-ball (cf. coincidence (i) in Helgason again). This is the only simplicial
case.
For type CIII, the simplicial cases have q = 1, with polytope △1 and regular
convex body a ball B4p . The symmetric space is Sp(p, 1)/(Sp(p) × Sp(1)). Since
sp(1) ≃ su(2), and Sp(p) × SU (2) acts transitively on the boundary of the 4p-ball
(cf. [53] once again) In dimension 4, i.e. p = q = 1, Helgason’s coincidence (iii)
implies that we have an EJA R4 ⊕ R: we have sp(1) × sp(1) ≃ so(4).
From Table 3: exceptional symmetric space representations.
Table 3 concerns spaces derived from exceptional Lie groups. Of these, only
two have simplicial polytopes.
EIV, with polytope △2 , has symmetric space determined by the pair of Lie
algebras (g, k) = (e6(−26) , f4 ). The dimension of the polar representation of k,
hence of Aff Ω, is 26, and the Cartan decomposition and the Lie algebra f4 is that

<!-- page 69 -->
69
of the automorphism group of the convex set of unit-trace 3 × 3 positive definite
octonionic-Hermitian matrices, which is indeed 26-dimensional, corresponding
to the 27-dimensional exceptional Jordan algebra (cf. Table 1); p0 in the Cartan
decomposition is the traceless octonionic-Hermitian matrices.
FII has polytope △1 , and symmetric space determined by g = f4(−20) , k =
so(9). Its dimension is 16, so B is a 16-ball. Spin(9), a double cover of SO(9),
is known to act transitively on the unit 15-sphere in its (16-dimensional) fundamental representation (cf. [53] or [67]). Since the other exceptional case is
Herm(3, O), one might be tempted to think this representation is the octonionic
bit, Herm(2, O). But Herm(2, O) is 10-dimensional, with 9-dimensional traceless
part, so the “octobit” is naturally identified with the spin factor R9 ⊕ R, with state
space a 9-ball.55
From Table 4: representations from simple complex groups
In Table 4, corresponding to Helgason’s Type IV symmetric spaces, which
arise from quotients of complex semisimple groups (viewed as real groups) by
their compact real forms, the only simplicial polytopes appear in the the first line,
of type and root space An , for n ≥ 1, and noncompact symmetric space given by
SL(n + 1, C)/SU (n + 1), with dimension n(n + 2). The Cartan decomposition is
sl(n + 1, C) = su(n + 1, C) ⊕ p where p is the traceless complex Hermitian matrices; the convex hull, Ω, of the orbit of the highest restricted weight state in
the traceless positive semidefinite matrices is affinely isomorphic to the unit-trace
positive semidefinite matrices, i.e. the “density matrices” of standard quantum
theory over C.
The remaining lines of Table 4 include some families with polytopes ✷n , ✸n ,
but the cases n = 1 are not included so there are no more simplicial cases.

C.2 Actions by polar representations other than symmetric space
representations
In Dadok’s classification of polar representations of compact connected groups K
by symmetric space representations, usually the polar representation is isomorphic
to a symmetric space representation, but sometimes it is necessary to pass, via
Theorem 8.10, to a symmetric space representation of a larger connected compact
group K̃, acting on the same space and having the same orbits as the original polar
55 See [27] for an interpretation of Herm(2, O) as acted on by double covers of SO(9, 1) and of

SO(9).

<!-- page 70 -->
70
representation. The original representation is the restriction of the representation
of K̃ to the subgroup K.
In the representations associated with simplicial Farran-Robertson polytopes,
this only occurs in the △1 cases, those in which the regular body B is a ball.
These must be cases in which K acts transitively (and linearly) on the sphere
∂ B ≡ ∂e B. Any representation of a compact group acting transitively on a sphere
is polar.56 So all such representations of compact connected groups must occur
either as symmetric space isotropy representations in Tables 2, 3 and 4, or as the
restrictions of such representations to subgroups via Theorem 8.10 of Dadok (for
a more compact and slightly more detailed presentation, see the main theorem of
[67] and the remarks following it).
In both cases, the subgroup necessarily acts transitively not only on the set of
extremal points (1-frames), but on the set of 2-frames as well, since the 2-frames
in a ball are just pairs [x, −x]. One motivation for interest in these possibilities
comes from general probabilistic theories: we might be interested in theories in
which the state space is strongly symmetric and spectral, but the group of allowed
reversible transformations is a proper subgroup of Aut 0 Ω, yet we still want it
to act transitively on frames. In [5], the condition of energy observability (formulated for this case to require an injection of the Lie algebra of the allowed
subgroup into the observables with the properties described in [5], Def. 30) was
shown to rule out not only all Jordan-algebraic state spaces with Aut 0 Ω as the
allowed transformations, but also the systems with Ω a ball Bd , but with only a
proper subgroup of SO(d) as the allowed reversible transformations.

C.3 More detail on the Jordan-algebraic cases
For the symmetric space isotropy representations in which the compact group
acts on the orthocomplement of the identity in a Jordan algebra, and has the Lie
algebra of the group of Jordan automorphisms (call these Jordan isotropy representations), the main text already gave a general argument why the regular convex
body is affinely isomorphic to the normalized Jordan algebra state space. In this
subsection, we see a little more concretely how this works, by looking in more
detail at those representations for which the Farran-Robertson polytopes are △n ,
n ≥ 2, which is to say the “matrix” cases Herm(m, D). We need to verify that,
56 This is implied at the end of Case I on p. 133 of [31]. It is also fairly obvious: the Cartan

subspace is 1-dimensional, generated by a diameter, and the sphere is the unique (up to dilation)
orbit.

<!-- page 71 -->
71
possibly up to an affine isomorphism, the orbit whose convex hull is the regular
convex body B in the Madden-Robertson construction is the same orbit whose
convex hull gives the normalized state space of V . For △n , n ≥ 2, if A = p ⊕ R
is an EJA then it must be of the form Herm(n, D), D ∈ {R, C, H, O}. The Coxeter/Dynkin diagram for the restricted Weyl group of Gss is that of An−1 . The
space p in the Cartan decomposition g = k ⊕ p of the Lie algebra of Aut ss
0 A+ is
the traceless symmetric matrices over D. A maximal abelian subspace a of p is
given by the traceless diagonal matrices in each case; its dimension is n − 1. Its
Weyl group Ka /K a (also written NK (a)/ZK (a)) is Sn . It is convenient to study K’s
action p by extending it to an action of p ⊕ R, where R in this case is generated by
the identity matrix, so we have an action on the space of symmetric matrices, not
just the traceless ones. K’s action fixes the identity matrix, and the traceless matrices are an invariant (in fact irreducible) subspace for the K-action. W ≃ Sn acts
as the group of all permutations of the unit diagonal matrices eii , for i ∈ {1, ..., n}
(or if we prefer to consider its action on the traceless matrices, it permutes the n
traceless matrices e11 − I/n ≡ diag((n − 1)/n, −1/n, ..., −1/n), e22 − I/n, etc..).
These matrices form the n vertices of an (n − 1)-simplex in the unit-trace (resp.
traceless) matrices. A set of generators for this group is the reflections in the hyperplanes normal to the traceless matrices eii − e j j , but these are not all necessary;
a minimal set is eii − ei+1,i+1 . Thus eii − ei+1,i+1 are a system of simple roots for
An−1 . For An−1 , the diagram is linear with n − 1 simple roots, and unmarked links
because adjacent roots are all at angle 2π /3. If we identify the unit matrices eii
with unit vectors ei in Rn (the unit-trace matrices) to make index manipulation
easier, then e11 , projected into the traceless matrices (i.e. e11 − I/n) is λ1 , the
first fundamental weight, which is the point in the Madden-Robertson construction that corresponds to the first node of the Coxeter diagram. The convex hull
of its W -orbit is a simplex, the translation to the traceless matrices of the simplex
△(e1 , ..., en) in the unit-trace matrices. This simplex in a is therefore Madden and
Robertson’s π (B) in this polar representation, for the case of the first (leftmost)
node of the Coxeter diagram. The last node gives (up to possible dilation) the polar body,57 and the polar of a simplex is again a simplex; indeed since the diagram
is symmetric the regular convex body associated with the last node will also be
57 In the particular case of A

n−1 , this is confirmed by the fact that λn−1 /(n − 1) is the barycenter
of a maximal face of the simplex π (B), which is a negative multiple of a vertex of the simplex, sox
the convex hull of its orbit gives (up to dilation) the negative of the original simplex, which is an
isomorphic simplex and (up to dilation) the polar of the original simplex.

<!-- page 72 -->
72
affinely isomorphic to the one associated with the first. 58
Since we saw that in this construction, we could identify the fundamental
weight λ1 ∈ a whose W -orbitope gives π (B) and whose K-orbitope gives B in
the Madden-Robertson embedding in a polar representation, as the traceless part
of the unit matrix e11 , when that polar representation is one corresponding to a Euclidean Jordan algebra, we see that B = Conv (K.(e11 − I/n)) ≡ Conv (K.e11 ) −
I/n is affinely isomorphic to the normalized state space Conv K.e11 of the corresponding Euclidean Jordan algebra, the isomorphism being given by mapping
the linear hyperplane of traceless symmetric matrices to the affine hyperplane of
unit-trace ones, by adding I/n.

References
[1] E. Alfsen and F. Shultz, Geometry of State Spaces of Operator Algebras.
Birkhäuser, 2003.
[2] H. Araki, “On a characterization of the state space of quantum mechanics,”
Comm. Math. Phys., vol. 75, pp. 1–24, 1980.
[3] M. Krumm, H. Barnum, J. Barrett, and M. P. Müller, “Thermodynamics and
the structure of quantum theory,” New J. Phys., vol. 19, p. 043025, 2017.
arXiv:1608.04461.
58 The other nodes in the Coxeter diagram correspond, in general in the Madden-Robertson

construction, to the barycenters of a maximal flag of faces of this convex body (the orbitope over
λ1 ), and this is confirmed in the An−1 case by the explicit formula for the fundamental weights:
the weight λk is the projection of ∑ki=1 ei into subspace ∑i xi = 0, i.e. writing ti for the projection
to the subspace ∑i xi = 0 (the traceless diagonal matrices in our particular representation),
k

λk = ∑ ti .

(8)

i

For comparison, the barycenters of the unit (n − 1)-simplex in the unit-trace matrices are bk :=
∑kj=1 ei /k, and their translations to the (n − 1)-dimensional subspace ∑ni=1 xi = 0, which are the
barycenters of a maximal flag of of (proper) faces of the simplex Conv W.t1 in that space, are just
l

ck := ∑ t j /k ≡ λk /k.
j=1

(9)

<!-- page 73 -->
73
[4] G. Chiribella and C. M. Scandolo, “Operational axioms for diagonalizing
quantum states,” 2015. arXiv:1506.00380.
[5] H. Barnum, M. Müller, and C. Ududec, “Higher-order interference and
single-system postulates characterizing quantum theory,” New J. Phys.,
vol. 16, p. 123029, 2014. Also: arXiv:1403.4147.
[6] C. M. Lee and J. H. Selby, “Deriving Grover’s lower bound from simple
physical principles,” New J. Phys,, vol. 18, p. 093047, 2016.
[7] H. R. Farran and S. Robertson, “Regular convex bodies,” J. London Math.
Soc., ser. 2, vol. 49, pp. 371–384, 1994.
[8] T. Madden and S. Robertson, “The classification of regular solids,” Bull.
London Math. Soc., vol. 27, pp. 363–370, 1995.
[9] C. H. Bennett, G. Brassard, E. Bernstein, and U. Vazirani, “Strengths and
weaknesses of quantum computing,” SIAM J. Comp., pp. 1510–1523, 1997.
[10] G. Chiribella and C. M. Scandolo, “Entanglement as an axiomatic foundation for statistical mechanics,” 2016. arXiv:1608.0449.
[11] H. Barnum, C. M. Lee, and J. H. Selby, “Oracles and query lower bounds
in generalised probabilistic theories,” Found. Phys., vol. 48, pp. 954–981,
2018. arXiv:1704.05043.
[12] B. Dakić and C. Brukner, “Quantum theory and beyond: Is entanglement
special?,” in Deep Beauty: Understanding the Quantum World Through
Mathematical Innovation (H. Halvorson, ed.), Cambridge: Cambridge University Press, 2011. Also: arXiv:0911.0695.
[13] E. Alfsen and F. Shultz, State Spaces of Operator Algebras. Birkhäuser,
2001.
[14] R. Sanyal, F. Sottile, and B. Sturmfels, “Orbitopes,” Mathematika, vol. 57,
pp. 275–314, 2011. Also http://arxiv.org/abs/0911.5436.
[15] N. Riedel, “Spektraltheorie in geordneten Vektorraumen,” Rev. Roum. Math.,
vol. 28, pp. 33–79, 1983.
[16] B. Iochum, Cônes Autopolaires et Algèbres de Jordan. Lecture Notes in
Mathematics, Vol. 1049, Springer, 1984.

<!-- page 74 -->
74
[17] M. Müller and C. Ududec, “The structure of reversible computation determines the self-duality of quantum theory,” Phys. Rev. Lett., vol. 108,
p. 130401, 2012.
[18] P. Jordan, “Über ein Klasse nichtassoziativer hypercomplexe Algebren,”
Nachr. Akad. Wiss. Göttingen Math. Phys. Kl. I., vol. 33, pp. 569–575, 1933.
[19] J. Faraut and A. Koranyi, Analysis on Symmetric Cones. Oxford University
Press, 1994.
[20] I. Satake, Algebraic Structures of Symmetric Domains, vol. 14 of Publications of the Mathematical Society of Japan. Iwanami Shoten and Princeton
University Press, 1980.
[21] P. Jordan, J. von Neumann, and E. Wigner, “On an algebraic generalization of the quantum mechanical formalism,” Ann. Math., vol. 35, pp. 29–64,
1934.
[22] M. Koecher, “Die Geodätischen von Positivitätsbereichen,” Math. Annalen,
vol. 135, pp. 192–202, 1958.
[23] E. Vinberg, “Homogeneous cones,” Dokl. Acad. Nauk. SSSR, vol. 133, pp. 9–
12, 1960. English translation: E. Vinberg (1961): Soviet Math. Dokl. 1, pp.
787-790.
[24] H. Barnum and A. Wilce, “Local tomography and the Jordan structure
of quantum theory,” Found. Phys., vol. 44, pp. 192–212, 2014. Also:
arXiv:1202.4513.
[25] M. Koecher, “Positivitätsbereiche im Rn ,” Amer. J. Math., vol. 79, pp. 575–
596, 1957.
[26] G. Mostow, “Self-adjoint groups,” Ann. Math., vol. 62, pp. 44–55, 1955.
[27] T. Dray and C. A. Manogue, “Octonionic Cayley spinors and E6 ,” Comment.
Math. Univ. Carolin., vol. 51, pp. 193–207, 2010.
[28] G. P. Barker and J. Foran, “Self-dual cones in Euclidean spaces,” Linear
Algebra and its Applications, vol. 13, no. 12, pp. 147–155, 1976.
[29] L. Biliotti, A. Ghighi, and P. Heinzner, “Polar orbitopes,” 2012.
http://arxiv.org/abs/1206.5717.

<!-- page 75 -->
75
[30] L. Biliotti, A. Ghighi, and P. Heinzner, “Invariant convex sets in polar
representations,” Israel J. Math., vol. 213, pp. 423–441, 2016. E-print
http://arxiv.org/abs/1411.6041.
[31] J. Dadok, “Polar coordinates induced by actions of compact Lie groups,”
Trans. Am. Math. Soc., vol. 288, pp. 124–137, 1985.
[32] M. P. Müller personal communication to H. Barnum, 2016.
[33] V. M. Gichev, “Polar representations of compact groups and convex hulls of
their orbits,” Differential Geometry and its Applications, vol. 28, pp. 608 –
614, 2010.
[34] F. Gozzi, “A note on polar representations.” arXiv:1704.03129, 2017.
[35] J. Eschenburg and E. Heintze, “Polar representations and symmetric spaces,”
Journal für die Reine und Angewandte Mathematik (Crelles Journal),
vol. 1999, no. 507, pp. 93–106, 1999.
[36] H. S. M. Coxeter, Regular Polytopes.
Reprinted by Dover Press, 1973.

New York: Macmillan, 1963.

[37] L. Schläfli, Theorie der Vielfachen Kontinuität. Bern: J. H. Graf, 1901.
[38] J. E. Humphreys, Reflection Groups and Coxeter Groups. No. 29 in Cambridge Studies in Advanced Mathematics, Cambridge: Cambridge University Press, 1992.
[39] S. Helgason, Differential Geometry, Lie Groups, and Symmetric Spaces,
vol. 34 of Graduate Studies in Mathematics. American Mathematical Society, 2001. Reprint of 1978 edition published by Academic Press, New
York, vol. 80 of series Pure and Applied Mathematics.
[40] E. M. Alfsen and F. W. Shultz, “State spaces of Jordan algebras,” Acta Mathematica, vol. 140, pp. 155–190, 1978.
[41] J. Barrett, “Information processing in generalized probabilistic theories,”
Phys. Rev. A, vol. 75, p. 032304, 2007. arXiv:0508211.
[42] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, “Generalized nobroadcasting theorem,” Phys. Rev. Lett., vol. 99, p. 240501, 2007.

<!-- page 76 -->
76
[43] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, “Cloning and broadcasting in
generic probabilistic theories.” arXiv.org e-print quant-ph/0611295, 2006.
[44] M. Plávala, “All measurements in a probabilistic theory are compatible if
and only if the state space is a simplex,” Phys. Rev. A, vol. 94, p. 042108,
2016. arxiv:1608.05614.
[45] L. Hardy, “Quantum theory from five reasonable axioms.” arXiv.org e-print
quant-ph/0101012, 2001.
[46] L. Hardy, “Why quantum theory?.” arXiv.org e-print quant-ph/0111068.
Contribution to NATO Advanced Research Workshop “Modality, Probability, and Bell’s Theorem”, Cracow, Poland 19–23.8.01, 2001.
[47] A. Connes, “Caractérisation des espaces vectoriels ordonneés sous-jacents
aux algèbres de von Neumann,” Annales de l’Institut Fourier (Grenoble),
vol. 24, pp. 121–155, 1978.
[48] J. Bellissard and B. Iochum, “Homogeneous self-dual cones and Jordan algebras,” in Quantum Fields—Algebras, Processes (L. Streit, ed.), (Wien, New
York), pp. 153–165, Springer, 1980.
[49] Ll. Masanes and M. P. Müller, “A derivation of quantum theory from
physical requirements,” New J. Phys., vol. 13, no. 6, p. 063001, 2011.
arXiv:1004.1483.
[50] H. Barnum, M. Graydon, and A. Wilce, “Composites and categories of Euclidean Jordan algebras.” arXiv:1606.09331, 2016.
[51] P. Selinger, “Dagger compact closed categories and completely positive
maps (extended abstract),” in Electronic Notes in Theoretical Computer Science (Proceedings of the 3rd International Workshop on Quantum Programming Languages (QPL 2005)), vol. 170, pp. 139–163, Elsevier, 2007.
[52] S. Abramsky and B. Coecke, “A categorical semantics of quantum protocols,” in Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science (LICS ’04), pp. 415–425, 2004.
[53] Ll. Masanes, M. P. Müller, R. Augusiak, and D. Pérez-Garcia, “Entanglement and the three-dimensionality of the Bloch ball,” J. Math. Phys., vol. 55,
p. 122203, 2014. Also arxiv:1111.4060v4.

<!-- page 77 -->
77
[54] G. Niestegge, “Conditional probability, three-slit experiments, and the Jordan algebra structure of quantum mechanics,” Adv. Math. Phys., vol. 2012,
p. 156573, 2012.
[55] C. Ududec, H. Barnum, and J. Emerson, “Probabilistic interference in operational models.” Unpublished, 2009.
[56] E. M. Alfsen and F. W. Shultz, “State spaces of Jordan algebras,” Acta Mathematica, vol. 140, pp. 155–190, 1978.
[57] R. Sorkin, “Quantum mechanics as quantum measure theory,”
Mod.Phys.Lett., vol. A9, pp. 3119–3128, 1994. arXiv:gr-qc/9401003.
[58] C. Ududec, H. Barnum, and J. Emerson, “Three slit experiments and the
structure of quantum theory,” Found. Phys., vol. 41, pp. 396–405, 2011.
[59] C. Ududec, Perspectives on the formalism of quantum theory. PhD thesis,
University of Waterloo, 2012.
[60] L. Grover, “A fast quantum mechanical algorithm for database search,” Proceedings of the 28th Annual ACM Symposium on the Theory of Computing
(STOC), pp. 212–219, May 1996.
[61] L. Grover, “Quantum mechanics helps in searching for a needle in a
haystack,” Phys. Rev. Lett., pp. 325–328, July 1997.
[62] H. Barnum, C. M. Lee, C. M. Scandolo, and J. H. Selby, “Ruling out higher
order interference from purity principles,” Entropy, vol. 19, p. 253, 2017.
arXiv:1704.05106.
[63] D. A. Meyer and J. Pommersheim, “On the uselesness of quantum queries,”
Theoretical Computer Science, vol. 412, no. 51, pp. 7068–7064, 2011.
[64] P. M. Alberti and A. Uhlmann, Stochasticity and partial order. Berlin: VEB
Deutscher Verlag Wiss., 1981.
[65] H. Barnum, J. Barrett, M. Krumm, and M. Müller, “Entropy, majorization
and thermodynamics in general probabilistic theories,” in Electronic Proceedings in Theoretical Computer Science (Proceedings 12th International
Workshop on Quantum Physics and Logic) (C. Heunen, P. Selinger, and
J. Vicary, eds.), vol. 195, pp. 43–58, 2015. Also: arXiv:1508.03107.

<!-- page 78 -->
78
[66] G. Chiribella and C. M. Scandolo, “Microcanonical thermodynamics in
general physical theories,” New J. Phys., vol. 19, p. 123043, 2017.
arXiv:1608.04459.
[67] J. Eschenburg and E. Heintze, “On the classification of polar representations,” Mathematische Zeitschrift, vol. 232, no. 3, pp. 391–398, 1999.
