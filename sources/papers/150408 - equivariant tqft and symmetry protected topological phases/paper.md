---
type: paper
date: 2015-04-08
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1504.01830v1)
reviewed: false
---

# Equivariant Topological Quantum Field Theory and Symmetry Protected Topological Phases

Machine-generated and unreviewed text extraction of arXiv:1504.01830v1
(26 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1504.01830v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:1504.01830v1 [cond-mat.str-el] 8 Apr 2015

Equivariant Topological Quantum Field
Theory and Symmetry Protected Topological
Phases
Anton Kapustin∗
Simons Center for Geometry and Physics, Stony Brook, NY
Alex Turzillo
California Institute of Technology, Pasadena, CA
April 9, 2015

Abstract
Short-range entangled topological phases of matter are closely connected to Topological Quantum Field Theory. We use this connection
to classify Symmetry Protected Topological Phases in low dimensions,
including the case when the symmetry involves time-reversal. To accomplish this, we generalize Turaev’s description of equivariant TQFT
to the unoriented case. We show that invertible unoriented equivariant TQFTs in one or less spatial dimensions are classified by twisted
group cohomology, in agreement with the group cohomology proposal
of Chen, Gu, Liu and Wen. We also show that invertible oriented
equivariant TQFTs in spatial dimension two or less are classified by
ordinary group cohomology.

∗

On leave of absence from California Institute of Technology

1

<!-- page 2 -->
1

Introduction and overview

Recently the problem of classifying gapped phases of matter whose
ground state is short-range entangled (SRE phases) received a lot of
attention.1 SRE phases can be divided into two broad classes, bosonic
and fermionic, depending on whether the fundamental degrees of freedom are bosons or fermions. The bosonic SRE phases are in many
ways simpler, and there has been a substantial progress in their classification. In particular, it has been proposed in [3] that D-dimensional
bosonic SRE phases with a finite internal symmetry G are classified
by the abelian group H D+1 (BG, U (1)). Here BG is the classifying
space of G, and D is the dimension of space (thus the dimension of
space-time is D + 1). Later it was noticed that some SRE phases in
spatial dimension 3 are not captured by the group cohomology classification [4], and it was proposed by one of the authors that the group
cohomology classification can be improved by replacing ordinary cohomology of BG with a particular generalized cohomology theory (the
stable cobordism) [5]. Other generalized cohomology theories have
also been proposed as candidates for the classification scheme [6, 2],
and it appears that the answer might depend on the detailed assumptions about the properties of SRE phases . But for D ≤ 2 all classification schemes agree, and in fact in the Hamiltonian approach one
can use the matrix product representation of SRE states to prove that
D = 1 bosonic SRE phases are classified by H 2 (BG, U (1)) [7]. The
D = 1 fermionic SRE phases have also been classified [8]. The D = 0
case is even simpler.
One promising avenue for extending these results to higher dimensions is via equivariant Topological Quantum Field Theory. It is a very
attractive conjecture that a large class of gapped phases is described
at large scales by a TQFT.2 Both gapped phases and TQFTs can be
tensored, and this operation makes both sets into commutative semigroups (sets with an associative and commutative binary operation).
Both semigroups have a neutral element 1 corresponding to the trivial
gapped phase or a TQFT. An element Φ of a semigroup is said to be
invertible if there exists an element Φ̄ such that Φ ◦ Φ̄ = Φ̄ ◦ Φ = 1.
1

There are at least two slightly different definitions of short-range entanglement, see
[1] and [2]. The difference between them is discussed in section 2.4.
2
There are some exceptions to this rule, due to the existence of phases with a nonvanishing thermal Hall conductivity. These exceptions only occur when D = 2 mod 4,
because only in these dimensions there exist gravitational Chern-Simons terms.

2

<!-- page 3 -->
Thus it makes sense to talk about invertible gapped phases and invertible TQFTs. According to one of the definitions of SRE phases [2],
an invertible gapped phase is the same as an SRE phase. Thus, if one
believes into the correspondence between gapped phases and TQFTs,
the classification of SRE phases is reduced to the classification of invertible TQFTs. More generally, SRE phases with a symmetry G
correspond to invertible G-equivariant TQFTs.
While classifying TQFTs in D > 1 is unrealistic, classifying invertible ones is much simpler. In fact, using the known algebraic
description of equivariant TQFTs in D = 0, 1 and 2, it is easy to
check that in these dimensions invertible G-equivariant TQFTs are
classified by H D+1 (BG, U (1)), provided the group G does not act on
space-time (see Section 2). But if some elements of G involve timereversal, the problem is more complicated. From the TQFT viewpoint,
time-reversal symmetry means that the theory can be defined on unorientable space-times. The difficulty is that an algebraic description
of unoriented equivariant TQFTs is not known even in low dimensions.
The main goal of this paper is to provide such an algebraic description
in D = 0 and D = 1 and to show that invertible equivariant TQFTs
are classified by twisted group cohomology H D+1 (BG, U (1)ρ ), where
ρ : G→Z2 is a homomorphism which tells us which elements of G are
time-reversing and which are not. This agrees with the proposal of
[3]. It is likely that this method can be extended to D = 2. In higher
dimensions an algebraic description of general TQFTs is prohibitively
complicated, and this approach to classifying SRE phases becomes
impractical. Note that equivariant TQFTs which are not necessarily
invertible are interesting in their own right, as they describe Symmetry
Enhanced Topological (SET) phases.
In Section 2 we deal with the case of a finite symmetry G which acts
trivially on space-time. We recall algebraic descriptions of oriented
equivariant TQFTs in D ≤ 2 and show that invertible equivariant
TQFTs are classified by elements of H D+1 (BG, U (1)). All of this is
either trivial (D = 0) or well-known to experts (D = 1 and D = 2).
In Section 3 we consider unoriented equivariant TQFT in D = 0
and the corresponding SRE phases with time-reversing symmetries.
In Section 4 we formulate axioms of unoriented equivariant TQFT
in D = 1 by extending Turaev’s axioms in the oriented case [11].
We show how these axioms lead to a generalization of Turaev’s Gcrossed algebra, which we call ρ-twisted G-crossed algebra. We prove
that every ρ-twisted G-crossed algebra gives rise to an unoriented

3

<!-- page 4 -->
equivariant TQFT. Finally we show that invertible TQFTs in D = 1
give rise to ρ-twisted 2-cocycles on BG, and that conversely to every
element of H 2 (BG, U (1)ρ ) one can associate a ρ-twisted G-crossed
algebra which is unique up to isotopy.
It would be interesting to give an algebraic description of D = 2
unoriented equivariant TQFTs and show that in the invertible case
they are classified by H 3 (BG, U (1)ρ ). The first step is to categorify
our algebraic description of D = 1 unoriented equivariant TQFT by
replacing vector spaces with categories, linear maps with functors, and
equalities with isomorphisms. The nontrivial part is to find a complete
set of coherence conditions between isomorphisms analogous to the
pentagon and hexagon conditions in the oriented case which ensure
consistency under gluing.
A.K. would like to thank V. Ostrik for helpful discussions. The
work of A.K. was supported by the Simons Foundation. The work of
A. T. was supported in part by the DOE grant DE-FG02-92ER40701.

2 Oriented equivariant TQFT and SRE
phases with an internal symmetry
2.1

D=0

A D = 0 TQFT is ordinary quantum mechanics with zero Hamiltonian and is completely determined by its space of states (a finitedimensional complex vector space V ). Equivariant TQFT is merely a
vector space V with an action of G. Since G is finite, this representation is unitarizable (unitary for a suitable choice of inner product
on V ). The trivial equivariant TQFT corresponds to V = C with
a trivial action of G. Equivariant TQFTs which are invertible with
respect to the tensor product are one-dimensional representations of
G, i.e., elements of H 1 (BG, C∗ ) ≃ H 1 (BG, U (1)).

2.2

D=1

D = 1 TQFTs are in one-one correspondence with commutative Frobenius algebras [9] (see [10] for a nice exposition, including various generalizations). The vector space A underlying the algebra is the space
of states of the TQFT on a circle. The state-operator correspondence identifies A with the space of local operators, which is clearly

4

<!-- page 5 -->
a commutative algebra. The Frobenius structure is a non-degenerate
bilinear inner product
η(a, b) ∈ C,

a, b ∈ A,

satisfying η(ab, c) = η(a, bc). It is a combination of the usual sesquilinear Hilbert space inner product and the anti-linear CPT transformation:
η(a, b) = (CPTa, b).
A trivial D = 1 TQFT has A ≃ C and η(1, 1) = 1. An invertible
TQFT has A ≃ C, and thus is completely determined by η(1, 1) ∈
C∗ = C\{0}. But if we are interested only in classifying TQFTs up
to isotopy (i.e. up to continuous deformations), then all these TQFTs
can be identified (since π0 (C∗ ) is trivial). If we identify invertible
TQFTs and SRE phases, this means that in the absence of symmetry
there are no nontrivial D = 1 SRE phases.
To incorporate a symmetry G, we need to consider G-equivariant
D = 1 TQFTs. G-equivariance means that we can couple the theory
to an arbitrary G-bundle. The precise definition of equivariant TQFT
will be recalled in section 3. For now, we only need the algebraic
description of such TQFTs due to Turaev [11]. He defines a G-crossed
algebra as a finite-dimensional Frobenius algebra (A = ⊕g∈G Ag , η)
together with a homomorphism α : G→Aut A such that
Ag · Ah ⊂ Agh and 1 ∈ A1 .

(1)

η(Ag , Ah ) = 0 if gh 6= 1.

(2)

αh (Ag ) ⊂ Ahgh−1 .

(3)

α preserves η and αh |Ah = id.

(4)

∀ψg ∈ Ag , ψh ∈ Ah we have ψg · ψh = αg (ψh ) · ψg .

(5)

∀g ∈ G let ξig and ξgi be dual bases in Ag and Ag−1 . Then
X
X
αh (ξig )ξgi =
ξjh αg (ξhj ), ∀g, h ∈ G.

(6)

i

j

Let us make a few remarks about this definition. Ag is the gtwisted sector of the space of states on a circle. αh describes the
action of G on the space of states. If G is abelian, it acts on each
twisted sector separately, but in general it mixes different twisted sectors. The penultimate axiom shows that A is not commutative, but
is twisted-commutative. The last axiom arises from considering a

5

<!-- page 6 -->
punctured torus with twists by g and h along the two generators of
its fundamental group and computing the corresponding state in two
different ways. This axiom, together with the Frobenius condition
η(a, bc) = η(ab, c), implies
dim Ag = Tr αg |A1 .
Both sides of this equality compute the partition function of a torus
twisted by g along one direction and by 1 along the other direction. On
the left-hand side, the direction twisted by g is regarded as space and
the direction twisted by 1 is regarded as time. On the right-hand side,
it is the other way around. Since the right-hand side is a character of
a finite group G, we get an inequality 0 < dim Ag ≤ dim A1 . That is,
twisting by g cannot increase the number of states.
In particular, let us consider an invertible G-equivariant TQFT.
Then A1 ≃ C, and therefore Ag ≃ C for all g ∈ G. If we choose a
basis vector ℓh in each Ah , we see that the algebra structure is given
by a collection of complex numbers θ(g, h) such that
ℓg · ℓh = b(g, h) · ℓgh .
Twisted commutativity of A implies that b(g, h) is nonzero for all g, h
and fixes αh in terms of b. Associativity of multiplication implies
that b is a 2-cocycle, and changing a basis in Ag changes it by a
coboundary. The rest of the axioms are easily checked. With b fixed,
the only freedom left is the choice of the inner product η; all such
choices lead to isotopic TQFTs, which means that isotopy classes of
invertible oriented equivariant D = 1 TQFTs are classified by [b] ∈
H 2 (BG, C∗ ) ≃ H 2 (BG, U (1)). This result has been proved in [11].

2.3

D=2

When studying oriented D = 2 TQFTs one usually assumes that the
space of local operators (i.e. the vector space attached to S 2 ) is onedimensional, and thus the algebra of local operators is isomorphic to
C. If one is interested only in unitarizable TQFTs, one does not loose
much by focusing on this special case. Indeed, it is easy to show that
if the TQFT is unitarizable (i.e. the bilinear inner product arises from
a Hermitian inner product and an ant-linear CPT symmetry), then
the algebra of local operators is semi-simple. It is also commutative,
and therefore isomorphic to a sum of several copies of C. The generators of this algebra label different superselection sectors, and one

6

<!-- page 7 -->
might as well focus on a single sector where all but one generator act
trivially. The argument applies equally well for all D > 0, but in
D = 1 it is traditional to allow the algebra of local operators to be
non-semi-simple, in view of string theory applications which require
one to consider non-unitary TQFTs.
We are mostly interested in unitarizable TQFTs, and therefore in
this section we assume that the space of local operators is C. Such
oriented D = 2 TQFTs are described by modular tensor categories
with vanishing central charge c ∈ Z/8 [12, 13]. (If the central charge
is nonzero, one gets a framed D = 2 TQFT). The data of a modular tensor category attach a vector space to every closed oriented
2-manifold, and a map of vector spaces to every oriented bordism between such 2-manifolds. Similarly, oriented equivariant D = 2 TQFT
is described by a G-modular category [14, 15]. Its definition is a categorification of the notion of G-crossed algebra. In particular, for every
g ∈ G one has a category Cg , and a bi-functor Cg × Ch →Cgh satisfying the associativity constraint. The data of a G-modular category
attach a vector space to every closed oriented 2-manifold with a Gbundle and a trivialization at a base point, and a map of vector spaces
for every oriented G-bordism between such 2-manifolds (i.e. to every
oriented 3-manifold with a G-bundle which “interpolates” between the
two oriented 2-manifolds with G-bundles). Objects of the category Cg
represent quasi-particles in the g-twisted sector.
An invertible oriented equivariant D = 2 TQFT is described by
a G-modular category with C1 ≃ Vect, where Vect is the category of
finite-dimensional vector spaces. This condition ensures that for the
trivial G-bundle the vector space attached to any oriented 2-manifold
is one-dimensional. If the TQFT describes a gapped phase, this means
that the space of ground states is non-degenerate for any topology.
This is a hallmark of an SRE phase.
From C1 ≃ Vect one can deduce that Cg ≃ Vect for all g ∈ G.
Indeed, by the definition of a G-modular category [15], Cg is nonempty
for all g ∈ G. Then Prop. 4.58 in [16] implies that Cg ≃ Vect.
As a consequence, the vector space attached to any 2-manifold with
any G-bundle is one-dimensional. That is, there is no ground-state
degeneracy even after twisting by an arbitrary G-bundle.
Finally, Prop. 4.61 in [16] tells us that in the invertible case C is
entirely determined by an element of H 3 (BG, C∗ ) ≃ H 3 (BG, U (1)).
This agrees with the group cohomology proposal which says that D =
2 bosonic SRE phases with symmetry G are classified by elements of

7

<!-- page 8 -->
H 3 (BG, U (1)).

2.4 On the definition of SRE phases with symmetry G
Kitaev [2] proposed to define SRE phases as invertible gapped phases.
That is, a gapped phase Φ is an SRE phase if there exists another
gapped phase Φ̄ such that Φ ⊗ Φ̄ can be deformed to the trivial
gapped phase without closing the gap. This definition ensures that
SRE phases form an abelian group. But if an SRE phase Φ has a
symmetry G, a problem arises: it is not clear from this definition
whether Φ̄ can be chosen symmetric, and whether the deformation of
Φ ⊗ Φ̄ to the trivial phase can be chosen so that it does not break the
symmetry. In particular, suppose we define a Symmetry Protected
Topological (SPT) phase as an SRE phase with symmetry G which
is trivial if we ignore symmetry, but cannot be deformed to the trivial gapped phase if G is required to be preserved [1]. Then it is not
clear whether SPT phases with a fixed symmetry G form an abelian
group. In the TQFT world, an analogous question can be formulated
as follows. Consider a forgetful map Ψ from the set of G-equivariant
TQFTs to the set of arbitrary TQFTs. Let T be a G-equivariant
TQFT such that Ψ(T ) is invertible. Is it true that T is invertible?
The discussion in this section implies that this is true for D ≤ 2 and
if G does not involve time-reversal.

3

Unoriented equivariant D = 0 TQFT

In the D = 0 case, the homomorphism ρ : G→Z2 tells us whether a
particular element g reverses the direction of time. Our goal is to show
that invertible unoriented equivariant TQFTs in D = 0 spatial dimensions are classified by the twisted cohomology group H 1 (BG, U (1)ρ ).
Recall that a ρ-twisted 1-cochain on BG is the same as a function
φ : G→U (1) satisfying
φ(gh) = φ(g)φ(h)ρ(g) .
Here and below we identify Z2 with {1, −1}, and thus ρ(g) = −1 if g
is time-reversing and ρ(g) = 1 otherwise. Two twisted cochains φ(g)
and ψ(g) are regarded as equivalent (i.e. cohomologous) if there exists

8

<!-- page 9 -->
µ ∈ U (1) such that for all g ∈ G we have

φ(g),
ρ(g) = 1,
ψ(g) = µρ(g)−1 φ(g) =
µ−2 φ(g), ρ(g) = −1.
A D = 0 TQFT associates a complex vector space V to a point.
To each g ∈ G it associates an operator
Λ(g) : V →V.
where Λ(g) is linear if ρ(g) = 1 and anti-linear if ρ(g) = −1. After
choosing a basis in V , we can attach to every Λ(g) a complex nondegenerate matrix M (g), by letting

M (g),
ρ(g) = 1,
Λ(g) =
M (g)K, ρ(g) = −1.
Here K : V →V is an operator which complex-conjugates the coordinates of a vector in the chosen basis. The matrices M (g) do not form
a complex representations of G, rather [17]:

M (g1 )M (g2 ),
ρ(g1 ) = 1,
M (g1 g2 ) =
M (g1 )M (g2 )∗ , ρ(g1 ) = −1.
In the invertible case V ≃ C the matrices M (g) become elements
of C∗ , and the above equation becomes precisely the twisted cocycle
condition for the C∗ -valued 1-cochain M (g), where Z2 acts on C∗ by
complex conjugation.
We should also investigate the effect of a change of basis in V . In
the invertible case, if we replace the basis element ℓ ∈ V by λ−1 ℓ,
λ ∈ C∗ , the function M (g) transforms as follows:

M (g),
ρ(g) = 0,
M (g) 7→
−1
∗
λ λ M (g), ρ(g) = 1.
This is precisely the shift of the twisted 1-cocycle M (g) by a twisted
coboundary. Thus equivalence classes of invertible unoriented equivariant D = 0 TQFTs are classified by elements of H 1 (BG, C∗ρ ) ≃
H 1 (BG, U (1)ρ ).

4

Unoriented equivariant D = 1 TQFT

4.1

Definition of unoriented equivariant TQFT

For D > 0 we can avoid anti-linear operators by interpreting the
orientation-reversing symmetry as a parity symmetry (P or CP ).

9

<!-- page 10 -->
Since CP T is a symmetry of any local unitary QFT, we do not loose
generality by doing this. Thus ρ(g) = −1 if g reverses spatial orientation, ρ(g) = 1 otherwise.
At first we will try to be as general as possible and do not fix the
spatial dimension D. We consider a finite group G together with a homomorphism ρ : G→Z2 . The kernel of ρ will be denoted G0 . For any
manifold X we will denote by o(X) its orientation bundle. Any TQFT
is defined as a functor from a geometric source category with a symmetric monoidal structure to the category of finite-dimensional vector
spaces Vect (or more generally, to a symmetric monoidal category).
In the case of equivariant TQFT based on the pair (G, ρ) he source
category C is defined as follows. An object of C is a closed D-manifold
M , a base point for every connected component of M , a G-bundle E
over M , a trivialization of G at every base point, and a trivialization of
o(M )⊗ρ(E) everywhere on M . The last datum expresses the fact that
ρ(E) is isomorphic to the orientation bundle of X. A morphism of C is
an isomorphism class of a D+1-dimensional bordism N equipped with
a G-bundle E and a trivialization of o(N )⊗ρ(E), with every connected
component of the boundary given a base point and a trivialization of E
there. Two such bundles are said to be isomorphic if they are related
by a bundle map that is an homeomorphism of the total space, covers
a homeomorphism of the base space, and preserves the trivialization
and boundary data. There is also a decomposition of the boundary
into two disjoint parts, corresponding to the source and target of the
morphism. Composition of morphisms is obvious. The symmetric
monoidal structure arises from the operation of disjoint union.
Let us now specialize to the case D = 1. In this case the definition
can be simplified, because all 1d manifolds are orientable. Since we
are given trivializations of E at all base points, as well a trivialization
of o(M )⊗ρ(E), we also have a trivialization of o(M ) at all base points.
But since M is orientable, this means that we are given a trivialization
of o(M ) everywhere, i.e. an orientation. Then ρ(E) is also trivialized
everywhere, and the G-bundle reduces to a G0 -bundle. Thus the objects for C are exactly the same as in the oriented equivariant TQFT
with symmetry group G0 . Morphisms are different however, for example because unorientable bordisms are now allowed. Moreover, even
when bordisms are orientable, they are not given an orientation. More
precisely, if the boundary of a bordism is connected, there is a base
point with an orientation on it, and one can use this to extend orientation to the whole N . But if more than one base point is present,

10

<!-- page 11 -->
there is no guarantee that orientations so obtained agree between each
other. This will be discussed in more detail below.

4.2

Algebraic description for D = 1

From the above definition we extract the following algebraic data.
First of all, let M = S 1 . As remarked above, S 1 is actually oriented,
and the structure group G is reduced to G0 . Thus unoriented equivariant TQFT assigns a vector space Ag to every g ∈ G0 .
Now consider a cylinder regarded as a bordism from S 1 to S 1 .
It has two marked points on the boundaries which we call p− and
p+ (source and target). A G-bundle over a cylinder trivialized over
p− is determined by the holonomy around the source S 1 and thus
is labeled by an element g ∈ G. We are also given a trivialization
at p+ , and the holonomy along a path from p− to p+ gives a welldefined element h ∈ G. We know that g ∈ G0 , but h can be an
arbitrary element of G. If ρ(h) = 1, the two trivializations of ρ(E)
obtained from the trivializations of E at p− and p+ agree. Then,
since o(N ) ⊗ ρ(E) is trivialized everywhere, the orientations at p−
and p+ also agree, and the source and target circles have the same
orientation. Thus the source is labeled by g, and the target by hgh−1 ,
and the cylinder is assigned a map αh : Ag →Ahgh−1 . Similarly, if
ρ(h) = −1, the two orientations disagree, and the target is labeled
by hg−1 h−1 , while the source is still labeled by g. Such a cylinder is
assigned a map αh : Ag →Ahg−1 h−1 . We can summarize both cases
by saying that αh maps Ag to Ahgρ(g) h−1 . Since gluing two cylinders
labeled by (g, h) and (hgρ(g) h−1 , h′ ) using the trivial identification of
target and source circles gives a cylinder labeled by (g, h′ h), we must
have αh′ ◦ αh = αh′ h . In particular, each αh is invertible.
In general, we note that if N is an orientable bordism, and the
paths between base points on different boundary components all lie
in G0 , the morphism becomes a morphism in the oriented equivariant
theory with symmetry group G0 . Thus we get all the same algebraic
data as in the oriented G0 -equivariant theory. That is, a G0 -crossed
algebra
A = ⊕g∈G0 Ag ,

η : A ⊗ A→C,

α : G0 →Aut A,

satisfying (1)-(6). In particular, for h ∈ G0 the map αh is an automorphism of A. On the other hand, for h ∈
/ G0 the map αh is an

11

<!-- page 12 -->
∼
=

g

hgh−1
h
(a) Axiom (8) for h ∈ G0 .

∼
=

g

hg −1h−1
h
(b) Axiom (8) for h ∈
/ G0 .
anti-automorphism:
αh (ab) = αh (b)αh (a),

∀h ∈
/ G0 , ∀a, b ∈ A.

(7)

To see this, we compare the two pants diagram with cylinders attached
either to the torso or to the pant legs and note that for h ∈
/ G0 they
are related by a reflection rather than the identity homeomorphism.
Finally, in the unoriented case we have cross-cap states θg ∈ Ag2 ,
g∈
/ G0 . The state θg , g ∈
/ G0 , arises from a Möbius strip with an oriented boundary and a base point on the boundary. The fundamental
group of the Möbius strip is isomorphic to Z, where an orientationreversing generator is fixed once the orientation of the boundary has
been fixed. θg corresponds to a G-bundle whose holonomy along this
generator is g.
The cross-cap states have the following properties:
αh∈G0 (θg ) = θhgh−1 and αh /∈G0 (θg ) = θhg−1 h−1

(8)

θg · ψk = αg (ψk ) · θgk for all ψk ∈ Ak .

(9)

12

<!-- page 13 -->
g

k
g

∼
=

gk
k
1

1

1

Figure 1: Axiom (9). To obtain the right figure from the left, the puncture with
holonomy k is pulled through the crosscap along the path with holonomy g.
X

i
αg (ξgh
)ξigh = θg · θh .

(10)

i

The first of these properties is illustrated in Figures 1a and 1b.
The vectors θhg(−1) h−1 and αh (θg ) are defined by the two pictures
which happen to be related by an isotopy. The second property arises
from an isotopy of the punctured Möbius strip shown in Figure 1. The
third property arises from the fact that a Klein bottle with two holes
can be represented in two apparently different ways: as a cylinder
with an orientation-reversing twist, or as a cylinder with an insertion
of two cross-caps, see Figure 2.

g
#

h

∼
=

g

gh

Figure 2: Axiom (10). Two projective planes are punctured and sewed along their
boundaries, the diagonal lines, to obtain their connected sum, the Klein bottle.
We will call the data (A, η, α, θg , g ∈
/ G0 ) algebraic TQFT data. In
Appendix A we sketch a proof of
Proposition 1. Unoriented equivariant D = 1 TQFTs with symmetry (G, ρ : G → Z2 ) are in bijective correspondence with algebraic
TQFT data (A, η, α, θg , g ∈
/ G0 ).
We have already explained how to assign algebraic TQFT data to
any unoriented equivariant D = 1 TQFT. The converse procedure is
described in Appendix A.

13

<!-- page 14 -->
4.3 Invertible unoriented equivariant D = 1
TQFT
Let us now specialize to the invertible case. For an invertible unoriented equivariant D = 1 TQFT, the vector spaces Ag∈G0 are onedimensional. After fixing a basis {ℓg }g∈G0 of A so that η(ℓg , ℓg−1 ) = 1,
the algebraic TQFT data are determined by nonzero complex numbers θ(g), g ∈
/ G0 , z(h, k), h, k ∈ G0 , and w(h, k), h ∈
/ G0 , k ∈ G0
defined as follows:
θg = θ(g)ℓg2 ,

mk,l (ℓk , ℓl ) = b(k, l)ℓkl ,

αh /∈G0 (ℓk ) = w(h, k)ℓhk−1 h−1 .

αh∈G0 (ℓk ) = z(h, k)ℓhkh−1 ,

These numbers satisfy a number of identities following from the properties of algebraic TQFT data.
Proposition 2. Invertible unoriented equivariant D = 1 TQFTs with
symmetry (G, ρ) are in bijective correspondence with elements of the
ρ-twisted group cohomology H 2 (BG, C∗ρ ) ≃ H 2 (BG, U (1)ρ ).
Twisted cohomology is the cohomology of the usual group cochain
complex with respect to the ρ-twisted coboundary maps
δρn : C n (G, U (1)) → C n+1 (G, U (1)).
In degree 2, the ρ-twisted cocycle condition reads
a(g, h)a(gh, k) = a(h, k)ρ(g) a(g, hk)

(11)

A proof of Proposition 2 is rather lengthy, see Appendix B. But
the map in one direction, from twisted group cohomology to the set
of algebraic TQFT data, is easy to describe:
b(k, l) = a(k, l)

(12)

θ(g) = a(g, g)
a(h, k)a(hk, h−1 )
z(h, k) =
a(h, h−1 )
a(h, k−1 )a(hk−1 , h−1 )a(k, k−1 )
w(h, k) =
a(h, h−1 )

(13)
(14)
(15)

To prove Proposition 2, we must show that these numbers satisfy the
TQFT axioms (7)-(10) and that the map is injective and surjective.
This is done in Appendix B.

14

<!-- page 15 -->
Appendix A: Proof of Proposition 1
We have already shown that an unoriented equivariant D = 1 TQFT
has an underlying extended Turaev algebra (A, θg , αh ). Oriented cobordisms and bundle isomorphisms constitute a G0 -crossed algebra A =
⊕g∈G0 Ag , while crosscaps correspond to states θg ∈ Ag2 and orientationreversing homeomorphisms to algebra anti-automorphisms αh : Ag →
Ahg−1h−1 . It remains to show the converse: that from each extended
Turaev algebra we can construct an unoriented equivariant TQFT
with this underlying algebra. We generalize the approaches of [10]
and [18] to unoriented equivariant theories.
We begin by defining the vector spaces assigned to simple objects
P[g],x,t of the source category C. To each circle S equipped with principal G-bundle P[g] , basepoint x, local trivialization t : P[g] |x → G,
and global trivialization of o(S) ⊗ ρ(P[g] ), assign the vector space
H(P[g],x,t) ∼
= Ag where g is the holonomy of P[g] around S with respect to x and t. Any object E can be factored into simple objects
⊔i P[gi ],xi ,ti and assigned a vector space H(E) ∼
= ⊗i H(P[gi ],xi ,ti ). It is
clear that H(E) does not depend on the factorization of E.
Next we consider the linear maps assigned to morphisms of simple
objects. One type of morphism α̃k : P[g],x,t → P[g],y,s arises from
an isomorphism f of the bundle P[g] where (y, s) = (f (x), (f −1 )∗ t).
Realized as its mapping cylinder, f must have a global trivialization
of o(S × I) ⊗ ρ(f ). Since o(S × I) is trivial, so must be ρ(f ), and
so the holonomy of P[g] along a positive path from (x, t) to (y, s) is
an element k ∈ G0 . We assign the linear map αk : Ag → Akgk−1 to
this morphism. The other type of morphism α̃h : P[g],x,t → P[g−1 ],y,s
arises from a bundle anti-isomorphism P[g] → P[g−1 ] whose restriction
to the base circle is not isotopic to the trivial homeomorphism. Since
a bundle map of this type exchanges the sheets of o(S), the holonomy
of P[g−1 ] from (x, t) to (y, s) is an element h ∈
/ G0 . We assign the
linear map αh : Ag → Ahg−1 h−1 to α̃h . This assignment is well defined
for isomorphism classes of bundles, as the cylinder α̃k α̃g , related to
α̃k by a Dehn twist, is assigned the linear map αk αg , which equals αk
when restricted to Ag by (4).
Now we wish to define linear maps for cobordisms (W, E0 , E1 ).
The strategy will be to decompose W as a sequence of n elementary
cobordisms (W i , E0i , E1i ), sewn along bundle (anti-)isomorphisms si :
E1i → E0i+1 with E00 = E0 and E1n = E1 . After assigning a linear
map to each W i , we assign their composition τ (W ) to W . We must

15

<!-- page 16 -->
then verify that τ (W ) does not depend on the decomposition. Begin
by considering the cobordism of base spaces (N, M0 , M1 ). By Sard’s
lemma, there exists a smooth function f : N → I such that f −1 (0) =
M0 , f −1 (1) = M1 , and f is Morse; that is, the gradient df vanishes at
finitely many critical points xi , the Hessian d2 f is a non-degenerate
quadratic form at all xi , and the critical values ci = f (xi ) are distinct
and not equal to 0 or 1. The index ind(xi ) is the number of negative
eigenvalues of d2 f at xi . Choose ti ∈ I such that 0 = t0 < c1 <
t1 < · · · < cn < tn = 1. By the implicit function theorem, each
Mti = f −1 (ti ) is a disjoint union of mi circles, and Σi = f −1 ([ti−1 , ti ])
is a cobordism from Mti−1 to Mti with a single critical point. The
classification of surfaces tells us that Σi is homeomorphic to a disjoint
union of cylinders and one of five possibilities: a cap, a pair-of-pants,
their adjoints, and a twice-punctured real projective plane.
These spaces are base spaces for five classes of cobordisms W .
Since any G-bundle over the disk is trivial, there is a unique cobordism
over the cap, to which we assign the linear map η : A1 → C. A
G-bundle over the pair-of-pants, based and trivialized at the critical
point, is almost determined by the holonomies k and l around the legs
of the pants. We assign to it the linear map mk,l : Ak ⊗Al → Akl . The
orderings are related by conjugation αl : Akl → Alk , and consistency
requires that mk,l (ψk ⊗ ψl ) = αk ml,k (ψl ⊗ ψk ), which is enforced by
the axioms (4) and (5) of the G0 -crossed algebra A. The holonomies
determine the bundle up to cylinders α̃k sewn to the boundary circles,
which were assigned maps αk above. The next two maps are fixed
by adjunction. The adjoint of η distinguishes a state ψη ∈ A1 with
the property thatP
η(ψη ) = 1. The adjoint pair-of-pants is assigned a
map ∆k,l (ψkl ) = i ψkl φi ⊗ φi where {φi } is a basis for Al and {φi }
is a dual basis for Al−1 . A G-bundle over the crosscap is specified (up
to cylinders) by a holonomy g ∈
/ G0 around the orientation-reversing
loop. We assign to it the linear map ψk 7→ mg2 ,k (θg ⊗ ψk ), determined
by the distinguished state θg ∈ Ag2 .
One may worry about a redundancy in the assignment of linear
maps to composite cobordisms. Whenever an elementary cobordism
W i and its sewing maps si−1 and si can be modified in a way that preserves the composite cobordism W , consistency requires that τ (W ) is
also preserved. The map si used to sew a cap or its adjoint into
another cobordism does not affect the composite cobordism. The
consistency of the algebraic description follows from the fact that
αk and αh preserve η. Let W i be a pair-of-pants sewn along si−1

16

<!-- page 17 -->
and si . Sewing instead along (α̃k ⊗ α̃k ) ◦ si−1 and si ◦ α̃−1
k does not
change W . Since αk is an automorphism of A, τ (W ) is also preserved. Let R be the bundle isomorphism that exchanges two circles. Then (α̃h ⊗ α̃h ) ◦ R ◦ si−1 and si ◦ α̃−1
h yield the same W . We
require α−1
m(α
(ψ
)
⊗
α
(ψ
))
=
m
(ψ
h l
h k
k,l k ⊗ ψl ), which is enforced
h
i
i
i
by axiom (7). Let (W , E0 , E1 ) be a twice-punctured real projective
plane with holonomy g realized as a cobordism from si−1 : P[k] → E0i
to si : E1i → P[g2 k] . There is a bundle isomorphism, covering a
Dehn twist of the base space, between this cobordism and a twicepunctured real projective plane with holonomy g−1 k−1 with sewing
maps si−1 and si ◦ α̃g . By axioms (7) and (9), the consistency condition αg m(θg−1 k−1 ⊗ ψk ) = mg2 ,k (θg ⊗ ψk ) is fulfilled. Now consider the
Möbius strip with holonomy g ∈
/ G0 constructed by sewing a cap into
the twice-punctured real projective plane with holonomy g. Sewing
this cobordism into another along si yields the same composite cobordism related to the Möbius strip with holonomy hg−1 h−1 sewn along
α̃h−1 ◦ si by a bundle isomorphism that covers a Y-homeomorphism of
the base space. Axiom (8) encodes this relation in the algebraic data.
The linear map τ (W ) assigned to an arbitrary cobordism W is
given by the composition of maps assigned to its factors under Morse
decomposition. It remains to show that τ (W ) does not depend on
the choice of Morse function. Any two Morse functions f0 and f1
are related by a smooth family of functions fs that are Morse at all
but finitely many values of s. One possibility is that two critical
points merge and annihilate for some s. Then fs has a degenerate
critical point. This situation only occurs when deforming a pair-ofpants and an adjoint cap into a cylinder. For τ (W ) to be consistent
over the deformation, we require mk,1 (ψk ⊗ ψη ) = ψk . This condition
is enforced by the axioms of A. The remaining possibility is that
two critical values coincide for some non-Morse value of s. We must
check, for each composition W of two elementary cobordisms, that
all factorizations give the same linear map. This situation occurs
when both critical points
index 1, in which case W has Euler
P haveind(x
i ) = −2. Hence W is one of seven
characteristic χ(W ) = i (−1)
cobordisms: a genus zero oriented cobordism from three circles to
one, its adjoint, a genus zero oriented cobordism from two circles to
two, a twice-punctured torus from one circle to one, a crosscap-pants
cobordism from two circles to one, its adjoint, and a twice-punctured
Klein bottle from one circle to one.
The consistency of the first two cobordisms follows immediately

17

<!-- page 18 -->
from associativity of multiplication. The remaining two oriented conditions have been proven in Appendix A.3 of [10] and follow from the
oriented axioms, notably (6). The next condition says that moving a
crosscap from the “torso” to a leg of the pair-of-pants is a consistent
deformation and also follows from associativity of multiplication. The
Klein bottle has a decomposition as a pair-of-pants glued along its two
legs to an adjoint pair-of-pants as well as a decomposition as a sphere
with two crosscaps. The composite linear maps assigned to these realizations are equal to the others by axiom (10). We have assigned a
linear map to each cobordism in terms of a Morse function f and have
seen that this map is independent of the choice of f . This completes
the proof of Proposition 1.

Appendix B: Proof of Proposition 2
Consider the map from 2-cochains a ∈ C n (G, U (1)) to TQFT data
defined in (12)-(15). If we restrict to the set Z 2 (G, U (1)ρ ) of 2-cochains
satisfying the ρ-twisted 2-cocycle condition (11), we obtain a map f
from twisted cocycles to TQFT data. We will show that numbers in
the image of f satisfy the axioms (7)-(10), and hence give rise to a
consistent invertible UETQFT.
For an invertible theory, these axioms can be written as
w(h, kl)b(k, l) = w(h, k)w(h, l)b(hl−1 h−1 , hk −1 h−1 )
w(h, g 2 )θ(g) = θ(hg−1 h−1 )
b(g2 , k)θ(g) = b(gk−1 g−1 , gkgk)w(g, k)θ(gk)
b(g2 hg −1 , gh)w(g, h−1 g−1 ) = θ(g)θ(h)b(g 2 , h2 )b(h−1 g−1 , gh)
It will be useful to impose a “cyclic-symmetric gauge” on the restriction of the cocycle a to G0 :
a(k, k−1 ) = 1,

a(k, l) = a(l−1 , k−1 )−1 ,

∀k, l ∈ G0 .

We also fix some T ∈ G and impose the condition a(k, T ) = 1, k ∈ G0 .

18

<!-- page 19 -->
Axiom (7):
w(h, kl)b(k, l) =
=
=
=
=
=
=

a(h, l−1 k−1 )a(hl−1 k−1 , h−1 )a(kl, l−1 k−1 )
a(k, l)
a(h, h−1 )
a(h, l−1 k−1 )
a(hl−1 , k−1 h−1 )
−1
−1
−1
a(h, h ) a(l , k )a(hl−1 , k−1 )a(k−1 , h−1 )
a(hl−1 , k−1 h−1 )
a(h, l−1 )
a(h, h−1 )a(k−1 , h−1 )
a(h, l−1 )
a(hl−1 h−1 , hk−1 h−1 )a(h, k−1 h−1 )
a(h, h−1 )a(k−1 , h−1 )
a(hl−1 h−1 , h)
a(h, l−1 )a(hl−1 h−1 , hk−1 h−1 )a(h, k−1 h−1 )
a(h−1 , h)a(hl−1 , h−1 )
a(h, h−1 )a(k−1 , h−1 )
a(h, l−1 )a(hl−1 , h−1 )a(hl−1 h−1 , hk −1 h−1 )
a(h, k−1 )a(hk−1 , h−1 )
a(h, h−1 )a(h, h−1 )
w(h, k)w(h, l)b(hl−1 h−1 , hk −1 h−1 )

Axiom (8):
w(h, g 2 )θ(g) =
=
=
=
=
=

a(h, g−2 )a(hg−2 , h−1 )a(g2 , g−2 )
a(g, g)
a(h, h−1 )
a(hg−2 , h−1 )
a(hg−1 , g−1 )a(h, g−1 )a(g, g)a(g−1 , g−1 )
a(h, h−1 )
a(h, g−1 )a(g, g)a(g−1 , g−1 )
a(g−1 , h−1 )a(hg−1 , g−1 h−1 )
a(h, h−1 )
a(hg−1 h−1 , hg −1 h−1 )a(h, g−1 )a(g, g)a(g−1 , g −1 )
a(g−1 , h−1 )
a(h, h−1 )a(hgh−1 , h)a(h, g −1 h−1 )
a(hg−1 h−1 , hg −1 h−1 )a(g, g)a(g−1 , g−1 ) a(h, g −1 )a(g−1 , h−1 )
a(h, h−1 )a(hgh−1 , h)a(hg −1 , h−1 ) a(h, g −1 )a(g−1 , h−1 )
a(hg−1 h−1 , hg −1 h−1 )

= θ(hg −1 h−1 )

19

<!-- page 20 -->
Axiom (9):
a(g, k)a(g, k−1 )a(k, k−1 ) a(gk−1 , k)
a(g, g−1 )
a(g−1 , gk)
a(g, k−1 )a(gk−1 , g−1 )
a(gk−1 g −1 , gk)
= θ(g)a(g2 , k)a(g, k)
a(g, g−1 )
a(g, k−1 )a(gk−1 , g −1 )
=
a(g, gk)a(gk−1 g−1 , gk)
a(g, g−1 )
a(g, k−1 )a(gk−1 , g −1 )
= a(gk−1 g −1 , gkgk)
a(gk, gk)
a(g, g−1 )

θ(g)a(g2 , k) = θ(g)a(g2 , k)

= b(gk−1 g−1 , gkgk)w(g, k)θ(gk)
Axiom (10):
a(g, gh)a(g 2 h, g−1 )a(h−1 g −1 , gh)
a(g, g−1 )
2
a(g, gh) a(g h, h)
a(h−1 g −1 , gh)
a(g, g−1 ) a(g−1 , gh)
a(g2 , h)a(g, g)a(g, h)
a(g2 h, h)a(h−1 g−1 , gh)
a(g, g−1 )a(g−1 , gh)
a(g, g)a(g, h)
a(g2 , h2 )a(h, h)a(h−1 g−1 , gh)
a(g, g−1 )a(g−1 , gh)

b(g2 hg−1 , gh)w(g, h−1 g−1 ) = a(g2 hg −1 , gh)
=
=
=

= a(g, g)a(h, h)a(g2 , h2 )a(h−1 g−1 , gh)
= θ(g)θ(h)b(g 2 , h2 )b(h−1 g−1 , gh)
We have shown that data in the image of f define consistent invertible unoriented equivariant TQFTs. Both Z 2 (G, U (1)ρ ) and the
set of invertible UETQFTs are groups, and it is easy to see that f is
a group homomorphism.
It remains to show that f is injective and surjective. Let (g, h, k)
denote the twisted cocycle condition (11). We will construct a cocycle
that solves (12)-(15), an inverse to f .
Consider the twisted cocycle condition for (k, T, T −1 ):
a(k, T )a(kT, T −1 ) = a(T, T −1 ).
Taking into account a(k, T ) = 1, we get a(kT, T −1 ) = a(T, T −1 ) This
also implies a(T k, T −1 ) = a(T, T −1 ). So in this gauge we get w(T, k) =
a(T, k−1 ). Next consider the twisted cocycle condition for (l, k, T ):
a(l, k)a(lk, T ) = a(l, kT )a(k, T ).

20

<!-- page 21 -->
Taking into account a(k, T ) = 1, we get a(l, kT ) = a(l, k). Since
T −2 ∈ G0 , this implies a(k, T −1 ) = a(k, T −2 ). Next consider the
twisted cocycle condition for (T, k, T −1 ):
a(T, k)a(T k, T −1 )a(k, T −1 ) = a(T, kT −1 ).
Using previous results, this is equivalent to
a(T, kT −1 ) = a(k, T −2 )a(T, T −1 )a(T, k)
Next consider the twisted cocycle condition for (T, l, k):
a(T l, k)a(T, l)a(l, k) = a(T, lk)
Recall also that in our gauge a(T, l) = w(T, l−1 ). Then
a(T l, k)a(l, k)w(T, l−1 ) = w(T, k −1 l−1 )
Since αg αh = αgh and by axiom (7), we see
a(T l, k) = w(T, k −1 )a(T lT −1 , T kT −1 ).
We have determined the components of the twisted cocycle where
one argument is in G0 and the other is not. We have also determined
a(T k, T −1 ) and a(T, kT −1 ) up to a single term a(T, T −1 ). We can
determine a(T l, kT −1 ) by requiring that a satisfies the twisted cocycle
condition (T, l, kT −1 ):
a(T l, kT −1 )a(T, l)a(l, kT −1 ) = a(T, lkT −1 )
By construction, a is a 2-cochain that satisfies (12)-(15) as well as the
(k, T, T −1 ), (l, k, T −1 ), (T, k, T −1 ), (T, l, k), (l, k, m), and (T, l, kT −1 )
cocycle conditions. The component a(T l, mT −1 ) is also determined
by (T l, k, T −1 ), and equality of the two expressions must hold if a is
a cocycle:
a(T l, kT −1 ) = a(T lk, T −1 )a(T l, k)a(k, T −1 )
In the above expression, apply the (T, lk, T −1 ) condition to the first
a(T,lkT −1 )
term to obtain a(T,lk)a(lk,T
−1 ) . Hit the second term with (T, l, k) to ob−1

−1

)a(k,T )
a(T,lk)
. Hit a(lk, T −1 ) with (l, k, T −1 ) to get a(l,kT a(l,k)
.
tain a(l,k)a(T,l)
−1
After cancellation, we are left with the first expression for a(T l, kT ).

21

<!-- page 22 -->
To see injectivity of f , consider the trivial TQFT with b, w, θ
trivial. The cocycle solution has a(k, l) = 1 and a(k, lT ) = 1. We
w(T,k −1 l−1 )
have a(T l, k) = a(l,k)w(T,l
−1 ) = 1 as well as
a(T l, kT −1 ) = a(T lk, T −1 )a(T l, k)a(k, T −1 ) = θ(T −1 ) = 1
so the only the trivial cocycle corresponds to the trivial theory.
It remains to show that a satisfies the cocycle condition for all
possible combinations of arguments; in particular, we must show the
(k, l, mT ), (kT, l, m), (k, lT, m), (k, lT, mT ), (kT, l, mT ), (kT, lT, m),
and (kT, lT, mT ) conditions. Consider the first condition:
a(k, l)a(kl, mT ) = a(l, mT )a(l, kmT )
Since a(k, lT ) = a(k, l) for all k, l ∈ G0 in our gauge, this follows from
the G0 cocycle condition. Now consider the third:
a(kT, l)a(kT l, m)a(l, m) = a(lT, km)
a(T,kl)
, the
Apply the (T, k, l) condition to the first term to get a(k,l)a(T,k)
a(T,klm)
(T, kl, m) condition to the second term to get a(kl,m)a(T,kl)
, and the

. The desired
(T, k, lm) condition to the third term to get a(T,lkm)a(T,m)
a(k,lm)
condition is reduced to a known condition.
Now consider (T k, l, mT −1 ):
a(T k, l)a(T kl, mT −1 )a(l, mT −1 ) = a(T k, lmT −1 )
−1

a(T,kl)
a(T,klmT )
The first term becomes a(T,k)a(k,l)
after (T, k, l), the second a(T,kl)a(kl,mT
−1 )
−1
−1
−1
−1
after (T, kl, mT ), the third (a(k, l)a(kl, mT )) after (l, m, T ),
a(T,klmT −1
−1 ). Everything cancels.
and the fourth a(T,k)a(k,lmT
−1 ) after (T, k, lmT
Since a(kT, T −1 ) = a(T, T −1 ), we get the (l, lT, T −1 ) condition by
applying (kl, T, T −1 ) to a(klT, T −1 ). Then (k, lT, mT −1 ) reads

a(k, lT )a(klt, mT −1 ) = a(lT, mT −1 )a(k, lT mT −1 )
)a(klT,m)
The last term is just a(k, lT m) in our gauge and becomes a(k,lT
a(lT,m)
−1

)a(klT,m)
after (klT, m, T −1 ),
after (k, lT, m). a(klT, mT −1 ) becomes a(klT m,T
a(m,T −1 )
−1

)a(lT,m)
and a(lT, mT −1 ) becomes a(lT m,T
after (lT, m, T −1 ). We
a(m,T −1 )
have seen that a(klT m, T −1 ) = a(T, T −1 ) = a(lT m, T −1 ) so we are
done.

22

<!-- page 23 -->
The condition (k, lT, T −1 ) is shown by noting that a(k, lT ) =
a(k, l) and a(klT, T −1 ) = a(T, T −1 ) = a(lT, T −1 ). Consider the (k, T l, mT −1 )
condition:
a(k, T l)a(kT l, mT −1 ) = a(T l, mT −1 )a(k, T lmT −1 )
Hit the second term with (kT l, m, T −1 ) to get a(kT lm, T −1 )a(m, T −1 )a(kT l, m)
−1 )a(k,T lm)
and the fourth term with (k, T lm, T −1 ) to get a(kT lm,T
.
a(T lm,T −1 )
lm)a(T l,m)
by (k, T l, m) and a(T lm, T −1 )
Then a(kT l, m) becomes a(k,Ta(k,T
L)
−1

l,m)a(m,T )
becomes a(Ta(T
by (T, lm, T −1 ).
l,mT −1 )
Consider (T, T, T ):

a(T 2 , T )a(T, T )a(T, T ) = a(T, T 2 )
The first term vanishes, and we are left with θ(T )2 = w(T, T −2 ), which
is true by axiom (10) with g = h = T .
Consider (lT −1 , T, T ):
a(lT −1 , T )a(T, T ) = a(lT −1 , T 2 )
−1

−1

2

,T )
−1 , T ). The third is a(T ,T ) .
The first term is just a(T
a(l,T −1 ) by (l, T
a(l,T −1 )
−1
The condition then follows from (T, T, T ). Consider (T, mT , T ):

a(T, mT −1 ) = a(T, m)a(mT −1 , T )
The first term becomes a(T m, T −1 )a(T, m)a(m, T −1 ) by (T, m, T −1 )
a(T −1 ,T )
−1 )a(T −1 , T ) =
and the second becomes a(m,T
−1 ) . We are left with a(T m, T
1. This is θ(T −1 )θ(T ), which vanishes by axiom (10). Now consider
(kT, lT −1 , T ):
a(kT, lT −1 )a(lT −1 ) = a(kT, l)
The first term is a(kT l, T −1 )a(kT, l)a(l, T −1 ) by (kT, l, T −1 ) and the
−1 ,T )
by (l, T −1 , T ). We are left with a(kT l, T −1 )a(T −1 , T ) =
second is a(T
a(l,T −1 )
1 which holds as before.
Start with the (T −1 , T, mT −1 ) cocycle condition:
a(T −1 , T )a(T, mT −1 ) = a(T −1 , T mT −1 )
Apply (T, m, T −1 ) to the third term. It becomes a(T m, T −1 )a(T, m)a(m, T −1 ).
−1 )a(T,T −1 )
Note that a(T, m) = w(T,m
and that a(T −1 , T mT −1 ) =
a(T m,T −1 )

23

<!-- page 24 -->
w(T −1 ,T m−1 T −1 )a(T −1 ,T )
a(T −1 ,T )
. By (m, T, T −1 ), we have a(mT −1 , T ) = a(m,T
−1 )
a(mT −1 ,T )

The first equation becomes
w(T, m−1 ) = w(T −1 , T m−1 T −1 )
Since αT αT −1 = 1, this becomes w(T, m−1 )w(T, m) = 1 which is true
by axiom (7). This proves the (T −1 , T, mT −1 ) cocycle condition.
Now consider the (lT −1 , T, m) condition:
a(lT −1 , T )a(l, m)a(T, m) = a(lT −1 , T m)
−1

,T )
and the fourth
Hit the first term with (l, T −1 , T ) to get a(T
a(l,T −1 )
−1

,T m)
. Apply the new result
term with (l, T −1 , T m) to get a(l,m)a(T
a(l,T −1 )
−1
−1
−1
(T , T, m) to a(T , T m) to get a(T, m)a(T , T ). Everything cancels. This proves (lT −1 , T, m).
Now consider the (lT, kT, m) condition:

a(lT, kT )a(lT kT, m)a(kT, m) = a(lT, kT m)
Hit the first term with (lT, k, T ), the second term with the new result
(lT k, T, m), the third term with (k, T, m), and the fourth term with
(lT, k, T m). Everything cancels.
Finally, check (kT, T −1 l, mT ):
a(kT, T −1 l)a(kl, m)a(T −1 l, mT ) = a(kT, T −1 lmT )
The last term becomes a(kT, T −1 lm)a(T −1 lm, T ) by (kT, T −1 lm, T ).
a(kT, T −1 lm) becomes a(kl, m)a(kT, T −1 l)a(T −1 l, m) by (kT, T −1 l, m)
−1 l,mT )
by (T −1 l, m, T ). Everything canand a(T −1 lm, T ) becomes a(T
a(T −1 l,m)
cels, proving the last cocycle condition (kT, lT, mT ).
This proves that each invertible unoriented equivariant TQFT arises
from a twisted 2-cocycle. Since this twisted 2-cocycle gives an inverse
to f , we have shown that f is surjective. This completes the proof of
Proposition 2.

References
[1] X. Chen, Z. -C. Gu, and X. -G. Wen, “Local unitary transformations, long-range quantum entanglement, wave function renormalization, and topological order,” Phys. Rev. B 82, 155138
(2010).

24

<!-- page 25 -->
[2] A. Kitaev, talk at the IPAM workshop “Symmetry and Topology
in Quantum Matter,” Jan 26-30, 2015.
[3] X. Chen, Z. -C. Gu, Z. -X. Liu and X. -G. Wen, “Symmetry
protected topological orders and the group cohomology of their
symmetry group,” Phys. Rev. B 87, 155114 (2013).
[4] A. Vishwanath, T. Senthil, “Physics of three dimensional bosonic
topological insulators: Surface Deconfined Criticality and Quantized Magnetoelectric Effect,” Phys. Rev. X 3, 011016 (2013)
[5] A. Kapustin, “Symmetry Protected Topological Phases,
Anomalies, and Cobordisms: Beyond Group Cohomology,”
arXiv:1403.1467 [cond-mat.str-el].
[6] D. S. Freed, “Short-range entanglement and invertible field theories,” arXiv:1406.7278 [cond-mat.str-el].
[7] X. Chen, Z. -C. Gu, and X. -G. Wen, “Classification of gapped
symmetric phases in 1D spin systems,” Phys. Rev. 83, 035107
(2011).
[8] L. Fidkowski, A. Kitaev,‘ ‘Topological phases of fermions in one
dimension,” Phys. Rev. B 83, 075103 (2011).
[9] M. Atiyah, “Topological quantum field theories,” Inst. Hautes
Etudes Sci. Publ. Math. 68, 175 (1989).
[10] G. Moore, G. Segal, “D-branes and K-theory in 2D topological
field theory,” arXiv: hep-th/0609042.
[11] V. Turaev, “Homotopy field theory in dimension 2 and groupalgebras,” arXiv: math/9910010 [math.QA].
[12] G. W. Moore and N. Seiberg, “Taming the Conformal Zoo,” Phys.
Lett. B 220, 422 (1989).
[13] B. Bakalov and A. Kirillov (Jr)., “Lectures on Tensor Categories
and Modular Functors,” American Mathematical Society, 2000.
[14] V. Turaev, “Homotopy quantum field theory,” EMS Tracts in
Mathematics, EMS, Zr̈ich, 2010.
[15] V. Turaev, A. Virelizier, “On 3-dimensional homotopy quantum
field theory II: the surgery approach,” Internat. J. Math. 25,
1450027 (2014).
[16] V. Drinfeld, S. Gelaki, D. Nikshych, V. Ostrik, “On braided fusion categories. I.,” Selecta Math. 16, 1 (2010).

25

<!-- page 26 -->
[17] H. Weyl, “Commutator algebra of a finite group of collineations,”
Duke Math. J. 3, 200 (1937).
[18] V. Turaev, P. Turner, “Unoriented topological quantum field theory and link homology,” Alg. & Geom. Top. 6, 1069-1093 (2006).

26
