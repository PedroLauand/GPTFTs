---
type: paper
date: 2005-06-13
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:math/0506229v3)
reviewed: false
---

# Unoriented topological quantum field theory and link homology

Machine-generated and unreviewed text extraction of arXiv:math/0506229v3
(25 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/math/0506229v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Algebraic & Geometric Topology 6 (2006) 1069–1093
arXiv version: fonts, pagination and layout may vary from AGT published version

1069

Unoriented topological quantum field theory and link
homology
VLADIMIR TURAEV
PAUL TURNER
We investigate link homology theories for stable equivalence classes of link diagrams
on orientable surfaces. We apply (1+)1–dimensional unoriented topological
quantum field theories to Bar-Natan’s geometric formalism to define new theories
for stable equivalence classes.
57M25, 57R56; 81T40

1

Introduction

In this paper we consider link diagrams on orientable surfaces up to the relation of
stable equivalence, that is up to homeomorphisms of surfaces, Reidemeister moves and
the addition or subtraction of handles disjoint from the diagram. Stable equivalence
classes of link diagrams have an equivalent formulation in terms of so called “virtual”
link diagrams pioneered by Kauffman (see for example the review articles Kauffman
and Manturov [8] and Fenn, Kauffman and Manturov [6] and references therein). Many
constructions for link diagrams on R2 can be reproduced for stable equivalence classes
of link diagrams on surfaces, for example, one can define the Jones polynomial.
In his seminal work [9] Khovanov provided a new way to look at the Jones polynomial
of links in R3 interpreting it as the Euler characteristic of a homology theory. This
approach provides an invariant that is not only stronger than the Jones polynomial
but also has nice functorial properties with respect to link cobordisms. The Jones
polynomial may be viewed as a state sum over the 2n “smoothings” of an n–crossing
link diagram on R2 , with each state making a contribution to the polynomial. Each
smoothing is a collection of circles being the result of resolving each crossing in one of
two possible ways (indicated in Figure 3). Khovanov’s insight was to associate a graded
vector space to each smoothing and arrange these so that a certain topological quantum
field theory can be used to define a differential leading to a chain complex associated to
the link diagram. Remarkably the homotopy type of this complex is independent of the
chosen diagram so its homology is an invariant. Bar-Natan has written a wonderful
Published: 24 August 2006

DOI: 10.2140/agt.2006.6.1069

<!-- page 2 -->
1070

Vladimir Turaev and Paul Turner

exposition of all in [4]. The functorial properties of this construction were conjectured
by Khovanov [9], proven by Jacobsson [7] and later reproved in more generality by
Bar-Natan [5].
Khovanov’s work does not immediately extend to link diagrams on arbitrary orientable
surfaces. One difficulty arising is the following. For classical links Khovanov’s complex
is constructed by organising the 2n smoothings into a “cube” with each edge making a
contribution to the differential. These edges join smoothings with different numbers
of circles and the corresponding term of the differential may be seen as fusing two
circles into one circle or splitting one circle into two. For links on surfaces this is no
longer the case, and there may be edges joining smoothings with the same number
of circles. This arises when the surface is part of the structure (as in the work of by
Asaeda, Przytycki and Sikora [2]) and also for stable equivalence classes. In the latter
case Manturov [12] solves this problem over the two element field F2 by setting the
differential corresponding to such cube edges to be zero. The motivation for the current
work was to find other possibilities for stable equivalence classes.
Bar-Natan’s geometric complex [5] which is locally defined can be extended to diagrams
on surfaces, but at the price of admitting nonorientable cobordisms. In this paper the
key new idea is to define the notion of unoriented topological quantum field theory,
which can then be applied to the geometric picture to obtain a link homology theory for
stable equivalence classes of diagrams on surfaces.
Here is an outline of the paper. In Section 2 we define the notion of unoriented
topological quantum field theory and study the underlying algebraic structure which
includes a Frobenius algebra with additional structure. In dimension 1+1 we classify
isomorphism classes of unoriented TQFTs in terms of these Frobenius algebras. We
include analysis of the particular case of rank-two theories, which will be used later
to give link homologies. In Section 3 we follow Bar-Natan in defining a complex of
cobordisms [[D]] associated to a link diagram D on a closed orientable surface. By
introducing Bar-Natan’s sphere, torus and 4–Tu relations we obtain an invariant of the
link diagram on the surface. In Section 4 we apply an unoriented topological quantum
field theory to the complex of cobordisms defined in Section 3 to obtain a complex of
modules. Taking homology yields a link homology. Our main theorem is the following.
Theorem 4.4 Let R be a commutative ring with unit. Let λ, µ, β, a, t ∈ R such that a
is invertible and the following relations are satisfied:
µβ = λβ = 0,
2aλµ − a2 µ2 λ2 − a2 µ4 t = 2.
Algebraic & Geometric Topology 6 (2006)

<!-- page 3 -->
Unoriented topological quantum field theory and link homology

1071

Then the 5–tuple (λ, µ, β, a, t) defines (the isomorphism class of) a link homology
theory for stable equivalence classes of diagrams on orientable surfaces.
We end the paper by discussing a few examples.

2

Unoriented topological quantum field theories

In this section we define the notion of unoriented topological quantum field theory
(briefly, TQFT). In the 1+1–dimensional case there is a classification in terms of
Frobenius algebras with additional structure.
All the constructions can be formulated in the smooth and PL categories but we prefer
to use the language of topological manifolds. Thus, by a manifold we shall mean a topological manifold. By a cobordism, we mean a triple (W, M0 , M1 ) where W is a compact
manifold whose boundary is a disjoint union of two closed manifolds M0 , M1 (possibly
void). A homeomorphism of cobordisms (W, M0 , M1 ) → (W 0 , M00 , M10 ) is a homeomorphism W → W 0 sending M0 homeomorphically to M00 and M1 homeomorphically to
M10 .

2.1

The definition

Fix an integer d ≥ 0 and a commutative ring with unity R. We define in this subsection
the notion of (d+1)–dimensional unoriented topological quantum field theory. Such
a TQFT takes values in the category of projective R–modules of finite type (direct
summands of Rn with n = 0, 1, ...) and R–linear homomorphisms. In the case where R
is a field, projective R–modules of finite type are just finite-dimensional vector spaces
over R.
Definition 2.1 A (d+1)–dimensional unoriented TQFT (A, τ ) assigns a projective R–
module of finite type AM to any closed d –dimensional manifold M , an R–isomorphism
f# : AM → AM0 to any homeomorphism of d –dimensional manifolds f : M → M 0 ,
and an R–homomorphism τ (W) : AM0 → AM1 to any (d+1)–dimensional cobordism
(W, M0 , M1 ). These modules and homomorphisms should satisfy the following seven
axioms.
(1) For any homeomorphisms of closed d –dimensional manifolds f : M → M 0 and
f 0 : M 0 → M 00 , we have (f 0 f )# = f#0 f# . The isomorphism f# : AM → AM0 is invariant
under isotopies of f .
Algebraic & Geometric Topology 6 (2006)

<!-- page 4 -->
1072

Vladimir Turaev and Paul Turner

(2) For any disjoint closed d –dimensional manifolds M, N , there is an isomorphism
AMqN = AM ⊗ AN , natural with respect to homeomorphisms, where ⊗ = ⊗R is the
tensor product over R.
(3) A∅ = R where the empty set is considered as a d –dimensional manifold (for any
d ).
(4) The homomorphism τ associated with cobordisms is natural with respect to
homeomorphisms of cobordisms.
(5) If a (d+1)–dimensional cobordism W is a disjoint union of cobordisms W1 , W2 ,
then under the identifications in axiom (2), τ (W) = τ (W1 ) ⊗ τ (W2 ).
(6) For a cobordism (W, M0 , M1 ) obtained from (d+1)–dimensional cobordisms
(W0 , M0 , N) and (W1 , N 0 , M1 ) by gluing along a homeomorphism f : N → N 0 ,
τ (W) = τ (W1 ) ◦ f# ◦ τ (W0 ) : AM0 → AM1 .
(7) For any closed d –dimensional manifold M , we have
τ (M × [0, 1], M × 0, M × 1) = Id : AM → AM
where we identify M × 0 and M × 1 with M in the obvious way.
The pair (A, τ ) is isomorphic to another (A0 , τ 0 ) if for each closed d –manifold M
there is an isomorphism ηM : AM → A0M , natural with respect to homeomorphisms and
cobordisms, multiplicative with respect to disjoint union and such that η∅ = IdR .
This definition is essentially the one of Atiyah [3] but all references to orientations of
manifolds are suppressed. The axioms (1)–(7) constitute a special case of a detailed
axiomatic definition of TQFT’s given in Turaev [13], Chapter III in a framework of
so-called space-structures. For more on the naturality in axioms 2 and 4, the reader
is referred to [13, p. 121]; otherwise a knowledge of [13] will not be required and the
language of space-structures will not be used.
In dimension 1+1 a related idea has already appeared in Alexeevski and Natanzon
[1] in the context of open–closed field theory. The definition presented there of a
Klein topological field theory is, however, rather different from that above, justifying a
separate treatment here.
Note that the tensor product in axiom (2) is unordered so that the modules AM ⊗ AN and
AN ⊗ AM are the same and not merely isomorphic. The unordered tensor product of a
finite family of modules is obtained by considering all possible orderings of this family,
Algebraic & Geometric Topology 6 (2006)

<!-- page 5 -->
Unoriented topological quantum field theory and link homology

1073

forming the corresponding ordered tensor products and then identifying the resulting
modules along the obvious isomorphisms induced by permutations. We have to use
here the unordered tensor product since we want to apply axiom (2) to nonconnected
d –manifolds without fixing any order in the set of connected components.

2.2

Extended Frobenius algebras

We recall that a commutative Frobenius algebra over R is a unital, commutative
R–algebra V which as an R–module is projective of finite type, together with a module
homomorphism  : V → R such that the bilinear form h−, −i : V ⊗ V → R defined
by hv, wi = (vw) is nondegenerate, ie, the adjoint homomorphism V → V ∗ is an
isomorphism. The homomorphism  is called the co-unit and it is useful to define a
P
coproduct ∆ : V → V ⊗ V by ∆(v) = i v0i ⊗ v00i being the unique element such that
P 0 00
for all w ∈ V , vw = i vi hvi , wi.
The map ∆ : V → V ⊗ V satisfies
(Id ⊗m) ◦ (∆ ⊗ Id) = ∆ ◦ m = (m ⊗ Id) ◦ (Id ⊗∆)
and

(Id ⊗) ◦ ∆ = Id = ( ⊗ Id) ◦ ∆

where m : V ⊗ V → V is the multiplication in V and i : R → V is the unit map.
An unoriented (d+1)–dimensional TQFT (A, τ ) has an underlying Frobenius algebra
equipped with an involution of Frobenius algebras as we now discuss.
For the underlying R–module we take V = ASd , where Sd is the standard unit sphere
in Euclidean space Rd+1 . Note that any other sphere S in Rd+1 can be related
to the standard sphere Sd by parallel translations and homotheties which allows us
to canonically identify the corresponding vector spaces (courtesy of axiom (1) in
Definition 2.1).
The unit i and the co-unit  come from the (d+1)–dimensional unit ball B in Rd+1
viewed as a cobordism from the empty set to Sd and as a cobordism from Sd to the
empty set respectively.
The product is obtained by considering a ball W00 of radius three in Rd+1 with two
interior balls of radius 1 removed. This can be viewed as a cobordism from the two
internal spheres to the external sphere which, using the canonical identifications above,
gives a map m : V ⊗ V → V . Although not necessary as part of the definition we note
that the coproduct has geometric interpretation by viewing W00 as a cobordism from
the sphere of radius three to the two internal spheres.
Algebraic & Geometric Topology 6 (2006)

<!-- page 6 -->
1074

Vladimir Turaev and Paul Turner

The involution φ : V → V is induced by an orientation-reversing homeomorphism
χ : Sd → Sd . They are all isotopic so φ is well defined.
Proposition 2.2 The R–module V equipped with structure maps m, i,  defined above
is a Frobenius algebra and φ is an involution of Frobenius algebras.
Proof It follows from the familiar oriented case that (V, m, i, ) is a Frobenius algebra.
We observe that φ2 = Id since χ ◦ χ is isotopic to the identity on Sd .
Next we claim that φ is a homomorphism of Frobenius algebras. Note that an
orientation-reversing homeomorphism Sd → Sd extends to B, hence by axiom (4) in
Definition 2.1, φ preserves the unit and counit. There is also an orientation-reversing
homeomorphism W00 → W00 mapping each boundary component to itself showing
that φ ◦ m ◦ (φ ⊗ φ) = m, and hence since φ2 = Id, we see m ◦ (φ ⊗ φ) = φ ◦ m.
One further piece of structure can be identified in the form of an element θ ∈ V .
Consider the punctured projective space P of dimension d + 1 viewed as a cobordism
between the empty set and ∂P. Now we identify ∂P with Sd via a map f : ∂P → Sd
and set θ = f# ◦ τ (P)(1). There is an involution T on P given by the negation of one
coordinate which by axiom (4) in Definition 2.1 gives T# (τ (P)(1)) = τ (P)(1). Now
T reverses the orientation of the boundary and thus if f 0 is another homeomorphism
∂P → Sd nonisotopic to f then f 0 ◦ T is isotopic to f and we have
f#0 (τ (P)(1)) = f#0 (T# (τ (P)(1))) = f# (τ (P)(1)).
This shows that θ is well defined.
Lemma 2.3 φ(θ) = θ .
Proof The map T : P → P defined above reverses the orientation on ∂P so by axiom
(4) in Definition 2.1 we have φ(θ) = θ .
When d is odd there is a stronger relation between φ and θ .
Proposition 2.4 If d is odd then φ(θv) = θv for all v ∈ V .
Proof Consider two disjoint balls B1 and B2 in Pd+1 in the complement of Pd
in Pd+1 . Let Si = ∂Bi , i = 1, 2 and consider the cobordism (W, S1 , S2 ) where
W = Pd+1 − Int(B1 t B2 ). It is clear that W is a connected sum C # Pd+1 where
Algebraic & Geometric Topology 6 (2006)

<!-- page 7 -->
Unoriented topological quantum field theory and link homology

1075

C is homeomorphic to Sd × I . As the d –sphere separating W into two connected
summands we take the boundary of a regular neighbourhood of Pd in Pd+1 . Now
choose an arbitrary orientation of S1 and endow S2 with the orientation such that
τ (C) : V ∼
= V is the identity homomorphism. We can then use the
= AS1 → AS2 ∼
decomposition of W to compute τ (W)(v) = θv.
Since d is odd, and hence Pd+1 unorientable, there is a homeomorphism T : W → W
which reverses the orientation of S2 while leaving the orientation of S1 unchanged.
This is obtained by moving B2 by an isotopy in Pd+1 back to itself passing through Pd
exactly once. Since T reverses the orientation of S2 , using the identifications above
we have T|S2 = φ : V → V . On S1 we have T|S1 = Id : V → V . By axiom (4) in
Definition 2.1 the following diagram commutes.
V∼
= AS1
Id



V∼
= AS1

τ (W)

τ (W)

/ AS2 ∼
=V


φ

/ AS2 ∼
=V

Chasing around this diagram gives φ(θv) = θv as required.
In fact in dimension 1+1 the assignment of the structure above induces a bijection from
isomorphism classes of TQFTs to a special class of Frobenius algebras.
Definition 2.5 An extended Frobenius algebra is a Frobenius algebra (V, m, i, )
together with an involution of Frobenius algebras φ : V → V and an element θ ∈ V
satisfying the following two axioms.
(1) φ(θv) = θv, for all v ∈ V .
(2) m(φ ⊗ Id)(∆(1)) = θ2 .
Two extended Frobenius algebras (V, θ, φ) and (V 0 , θ0 , φ0 ) are isomorphic if there
exists an isomorphism of Frobenius algebras g : V → V 0 such that g(θ) = θ0 and
g ◦ φ = φ0 ◦ g.
We note that in [1] such algebras appear as “structure algebras” in which the part coming
from open boundaries is trivial.
√ N−1
Example 2.6 Let N be odd and let V = R[x]/xN . Taking φ = Id and θ = Nx 2
we see that (V, φ, θ) is an extended Frobenius algebra. In this case φ is obviously
an involution of Frobenius algebras satisfying axiom (1). Axiom (2) is reduced to
m(∆(1)) = θ2 which holds for our choice of θ since m(∆(1)) = NxN−1 .
Algebraic & Geometric Topology 6 (2006)

<!-- page 8 -->
1076

Vladimir Turaev and Paul Turner

Example 2.7 Let V be the two dimensional vector space over F2 on generators 1 and
x. This may be given the structure of Frobenius algebra by defining i(1) = 1, x2 = x,
(1) = 0, (x) = 1. Taking θ = 0 and φ(1) = 1, then φ(x) = 1 + x turns this into an
extended Frobenius algebra.
There are some useful elementary consequences of the definition.
Lemma 2.8 (i) m(φ ⊗ Id)(∆(v)) = m(φ ⊗ Id)(∆(1))v for all v ∈ V .
(ii) m(φ ⊗ Id)(∆(v)) = θ2 v for all v ∈ V .
(iii) m(∆(θ)) = θ3 .
Proof To prove (i) it suffices to notice that ∆(v) = (v ⊗ 1)∆(1). Part (ii) follows
immediately from (i). For (iii) we have
m(∆(θ)) = m((θ ⊗ 1)∆(1)) = m(φ ⊗ 1)((θ ⊗ 1)∆(1)) = m(φ ⊗ 1)(∆(θ)) = θ3 .
Proposition 2.9 Isomorphism classes of unoriented 1+1–dimensional TQFTs over
R are in bijective correspondence with isomorphism classes of extended Frobenius
algebras over R.
Proof We have already shown that an unoriented 1+1–dimensional TQFT has an
underlying Frobenius algebra over R and comes equipped with an involution of
Frobenius algebras φ. Furthermore we have defined the element θ and shown in
Proposition 2.4 that φ(θv) = θv for all v ∈ V . It remains to show axiom (2) in the
definition of extended Frobenius algebra. To see this we glue the ends of an oriented
punctured cylinder together in a nonorientation-preserving way, regarding the result W
as a cobordism (W, ∅, ∂W). We can use the original orientation of the cylinder to orient
∂W and hence identify A∂W with V . One can easily compute τ (W) : R → V to be the
map taking 1 to m(φ ⊗ Id)(∆(1)). On the other hand W is a punctured Klein bottle and
hence homeomorphic to the punctured connected sum of two projective planes. Thus
τ (W)(1) = θ2 . It is clear that the isomorphism class of this algebra depends only on the
isomorphism class of the TQFT.
We now show that every extended Frobenius algebra (V, θ, φ) gives rise to an unoriented
TQFT. Given a connected closed 1–manifold M we define the set AM by
AM = {(γ, v) | γ : S1 → M a homeomorphism, v ∈ V}/ ∼
Algebraic & Geometric Topology 6 (2006)

<!-- page 9 -->
Unoriented topological quantum field theory and link homology

where

1077

(γ, v) ∼ (γ 0 , v0 ) iff either γ is isotopic to γ 0 and v = v0
or γ is not isotopic to γ 0 and v = φ(v0 ).

Note that there are two isotopy classes of homeomorphisms S1 → M . Now pick any
homeomorphism h : S1 → M and define a map (of sets) h̃ : AM → V by
(
v
if γ is isotopic to h
h̃(γ, v) =
φ(v) else.
This map is a bijection and moreover, since V is an R–module, we can use it to turn AM
into an R–module. It is easy to check that the R–module structure is independent of the
isotopy class of h. Thus to a closed 1–manifold M we have assigned an R–module
N
AM . If M is not connected we simply write M = M1 t · · · t Mk and let AM =
AMi .
We define A∅ = R.
Now let f : M → M 0 be a homeomorphism of connected 1–manifolds (up to isotopy
there are two choices). Define f# : AM → AM0 by f# (γ, v) = (f ◦ γ, v). One can check
this is a well defined isomorphism of R–modules. This extends to homeomorphisms of
nonconnected manifolds by multiplicativity.
We now wish to define τ (W) : AM0 → AM1 for a cobordism (W, M0 , M1 ). We separate
the cases of orientable and nonorientable surfaces.
Suppose first that W is orientable and connected. Choose an orientation for W and
decompose it into basic pieces (caps, cups and pairs of pants). We can appeal to the usual
case of oriented TQFT to define τ (W) which is independent of the decomposition. We
claim that τ (W) is independent of the orientation chosen for W . Indeed by choosing the
opposite orientation, each piece in the decomposition also has the opposite orientation.
Consider, for example a pair of pants (P, M, N) occurring in the decomposition and
consider the following diagram where the top route corresponds to one orientation and
the bottom route to the other.
V
z=
∼
= zzz
zz
zz

AM D

⊗2

m

/V

m

/V

φ⊗2

DD
DD
D
∼
= DD" 

V ⊗2

@@
@@ ∼
@@=
@@

φ
? AN
~~
~
~
~~ ∼
 ~~ =

Note that if a connected 1–manifold M is oriented then there is a canonical identification
of AM with V , using the map h̃ : AM → V defined by an orientation-preserving
Algebraic & Geometric Topology 6 (2006)

<!-- page 10 -->
1078

Vladimir Turaev and Paul Turner

homeomorphism h : S1 → M (here S1 is given the anticlockwise orientation). By
reversing the orientation of M the identification is given by φ ◦ h̃. Thus the left and
right triangles in the diagram above commute. Since φ is a map of Frobenius algebras
the middle square also commutes, hence the two routes give the same map. Similar
arguments hold for the other basic surfaces, showing that τ (W) is independent of the
orientation. Furthermore, the properties of oriented TQFTs guarantee that τ (W) is
natural with respect to homeomorphisms. For nonconnected W we extend the above
multiplicatively.
Suppose now that W is nonorientable and connected. We may present W as a connected
sum of an orientable surface W or and n projective planes, W = W or # nRP2 . Note
that ∂W or = ∂W and that the homomorphism τ (W or ) : AM0 → AM1 is defined by
the orientable case above. Now choose an identification AM1 ∼
= V ⊗k and define
ψn : AM1 ∼
= V ⊗k → V ⊗k ∼
= AM1 to be the identity on all factors except one where it is
multiplication by θn . We define τ (W) = ψn ◦ τ (W or ).
A priori this depends on the identification AM1 ∼
= V ⊗k , the choice of factor in ψn and
or
2
the decomposition W = W # nRP . It follows from the properties of V that the
factor in ψn does not matter. Moreover, since φ(θ) = θ the definition is independent
of the identification AM1 ∼
= V ⊗k . Now suppose that we decompose W differently as
or
or
W = W # nRP2 then there is a homeomorphism g : W → W or taking each boundary
component to itself. On each such boundary component g is either isotopic to the
identity or is an orientation-reversing homeomorphism. By the naturality of τ for
orientable surfaces we have the following commutative diagram.
AM0
(g|M0 )#



τ (W or )

or

AM0

τ (W )

/ AM1
(g|M1 )#



/ AM1

We also have the following commutative diagram.
AM1
(g|M1 )#



AM1

ψn

ψn

/ AM1


(g|M1 )#

/ AM1

Commutativity is immediate for a component of M1 on which g|M1 is isotopic to the
identity and follows from the relation φ(θv) = θv on a component where g|M1 is an
orientation-reversing homeomorphism. Combining these two diagrams shows that
τ (W) is independent of the decomposition above. We may also choose a different
Algebraic & Geometric Topology 6 (2006)

<!-- page 11 -->
Unoriented topological quantum field theory and link homology

1079

number of projective planes in the decomposition, replacing any three by a torus and a
projective plane. However, in this case we may write W = W or # T 2 # (n − 2)RP2 and
τ (W) can be computed as τ (W or ) multiplied on one factor by m(∆(1))θn−2 . However,
by Lemma 2.8 we have m(∆(1))θn−2 = m(∆(θ))θn−3 = θn showing that τ (W) is
again independent of the decomposition. For a nonconnected cobordism we extend
multiplicatively.
What remains is to show that the structure defined above verifies axioms (1)–(7) in
Definition 2.1. These are all easy to show with the exception of the gluing axiom (6).
We leave the others as an exercise and focus on proving this axiom, for which the
following definition is useful.
Definition 2.10 A cobordism (W0 , M0 , N) is nice if for all (W1 , N 0 , M1 ) and homeomorphisms f : N → N 0 we have
τ (W) = τ (W1 ) ◦ f# ◦ τ (W0 )
where (W, M0 , M1 ) is the result of gluing W0 to W1 along f .
It is easy to check the following lemma.
Lemma 2.11 (i) If the cobordism (W0 , M0 , N0 ) is obtained from (W00 , M00 , N00 ) and
(W000 , M000 , N000 ) by gluing along a homeomorphism g : N00 → M000 , and W00 and W000 are
nice, then W0 is also nice.
(ii) If (W0 , M0 , N0 ) and (W1 , M1 , N1 ) are oriented and f : N0 → M1 is orientation
preserving then τ (W) = τ (W1 ) ◦ f# ◦ τ (W0 ).
Any surface may be decomposed into a composition of cobordisms of the six basic
types (up to ordering) indicated in Figure 1 where the input boundary is always at the
top (the picture on the right at the bottom represents a twice punctured projective plane).
In order to prove that the gluing axiom holds we will show that any cobordism of the
six types in Figure 1 is nice. Thus by Lemma 2.11 (i) we will have the desired result.
First we claim that any cobordism W0 of type (2) is nice. To see this let (W1 , N 0 , M1 ) be
a cobordism which we glue to W0 along a homeomorphism f : N → N 0 . We can present
W1 as W1 = W1or # nRP2 (n ≥ 0). We now orient W1or and choose orientations for each
of the cylinders and the pair of pants in W0 such that f is orientation preserving. Let
W2 be the result of gluing W1or to W0 along f so that W = W2 # nRP2 . By Lemma 2.11
(ii) we have τ (W2 ) = τ (W1or ) ◦ f# ◦ τ (W0 ). Thus
τ (W) = ψn ◦ τ (W2 ) = ψn ◦ (τ (W1or ) ◦ f# ◦ τ (W0 ))
= (ψn ◦ τ (W1or )) ◦ f# ◦ τ (W0 ) = τ (W1 ) ◦ f# ◦ τ (W0 ).

Algebraic & Geometric Topology 6 (2006)

<!-- page 12 -->
1080

Vladimir Turaev and Paul Turner

(1)

(4)

(2)

(5)

(3)

(6)

Figure 1: Basic cobordism types

Similar arguments show that cobordisms of type (1), (4) and (5) are nice.
For a cobordism of type (6) we decompose W0 and W1 as W0 = W0or # RP2 and
W1 = W1or # nRP2 . Now let W2 be the result of gluing W1or to W0or along f . We can
write W = W2 # (n + 1)RP2 . Thus
τ (W) = ψn+1 ◦ τ (W2 ) = ψn+1 ◦ (τ (W1or ) ◦ f# ◦ τ (W0or ))
= (ψ1 ◦ τ (W1or )) ◦ f# ◦ (ψn ◦ τ (W0or )) = τ (W1 ) ◦ f# ◦ τ (W0 ).
The most difficult case is for cobordisms of type (3). We decompose W1 into the connect
sum W1or # nRP2 and we orient W1or in an arbitrary way. If there is an orientation of
W0 such that f is an orientation-preserving homeomorphism then we are done by the
same arguments as above. If there is no such orientation we decompose W1 into the
composition of W2 and W3 glued along a (canonical) map g where W2 is of type (2).
Since by the above W2 is nice we have τ (W1 ) = τ (W3 ) ◦ g# ◦ τ (W2 ). Now let W4 be
the result of gluing W2 to W0 along f , which results in a number of cylinders and a
twice punctured Klein bottle. We can compute τ (W4 ) = ψ2 ◦ τ (W4or ). On the other
hand by using Lemma 2.8 (ii) we have τ (W4 ) = τ (W2 ) ◦ f# ◦ τ (W0 ). Finally we note
that W is the result of gluing W3 to W4 along g and so
τ (W) = ψn+2 ◦ τ (W or ) = ψn+2 ◦ (τ (W3or ) ◦ g# ◦ τ (W4or ))
= (ψn ◦ τ (W3or )) ◦ g# ◦ (ψ2 ◦ τ (W4or )) = τ (W3 ) ◦ g# ◦ τ (W4 )
= τ (W3 ) ◦ g# ◦ τ (W2 ) ◦ f# ◦ τ (W0 ) = τ (W1 ) ◦ f# ◦ τ (W0 ).
The gluing axiom now follows since all the pieces in the decomposition are nice.
Algebraic & Geometric Topology 6 (2006)

<!-- page 13 -->
Unoriented topological quantum field theory and link homology

1081

Thus we have defined an unoriented TQFT. Standard arguments now show that the
isomorphism class of this TQFT depends only on the isomorphism class of the extended
Frobenius algebra. Moreover, the underlying extended Frobenius algebra is clearly
(V, θ, φ) so the construction provides the required inverse.
We remark that in order to use the underlying Frobenius algebra to make computations
we must choose for each closed 1–manifold Γ an identification γ : S1 t · · · t S1 → Γ
which gives an isomorphism τ (γ) : V ⊗r → AΓ where r is the number of components
of Γ.

2.3

Rank-two aspherical theories

In this subsection we wish to study rank-two unoriented TQFTs satisfying the condition
τ (S2 ) = 0. For convenience we refer to these as rank-two aspherical unoriented TQFTs.
Lemma 2.12 Let (A, τ ) be a rank-two aspherical unoriented TQFT and let S be any
sphere and T any torus. Then τ (S) = 0 and τ (T) = 2.
Proof We have a standard torus constructed from discs and the surface W00 (a pair
of pants surface) which evaluates to 2 because the theory is rank-two. It follows from
this, the fact that the TQFT is aspherical and axiom (4) in Definition 2.1 that any sphere
evaluates to 0 and any torus evaluates to 2.
The following is an immediate corollary to Proposition 2.9.
Proposition 2.13 The isomorphism classes of rank-two aspherical unoriented 1+1–
dimensional TQFTs over R are in bijective correspondence with the isomorphism
classes of rank-two extended Frobenius algebras over R satisfying (i(1)) = 0, where 
and i are the counit and unit of the Frobenius algebra.
We now wish to classify the Frobenius algebras appearing in the previous proposition.
Let K = Z[a, f , t, λ, µ, β]/I where I is the ideal generated by
af = 1,

µβ = λβ = 0

and

2aλµ − a2 µ2 λ2 − a2 µ4 t = 2.

Now set U = K{1, x} and define multiplication by
11 = 1,

1x = x1 = x

and

Algebraic & Geometric Topology 6 (2006)

xx = (β − aλ2 − aµ2 t)x + t1

<!-- page 14 -->
1082

Vladimir Turaev and Paul Turner

and comultiplication by
∆(1) = f (1 ⊗ x + x ⊗ 1) − (β − aλ2 − aµ2 t)f 1 ⊗ 1,
∆(x) = fx ⊗ x + ft1 ⊗ 1.
Define a unit and counit by
(1) = 0,

(x) = a and

i(1) = 1.

θ = λ1 + µx

Let
and define φ : U → U by
φ(1) = 1

and φ(x) = β1 + x.

Proposition 2.14 The triple (U, θ, φ) defined above is an extended Frobenius algebra
over K satisfying (i(1)) = 0.
Proof The proof is purely computational and hence omitted. The one thing worth
pointing out is that the relations in K imply 2β = 0.
Given another ring with unity R and a ring homomorphism ψ : K → R we can use ψ
to view R as an K –module. We set Uψ = U ⊗K R and define a comultiplication and
counit by ∆ ⊗ 1 and  ⊗ 1. Since U is a Frobenius algebra over K , it follows that Uψ
is a Frobenius algebra over R. The resulting triple (Uψ , θ ⊗ 1, φ ⊗ Id) is an extended
Frobenius algebra over R and it too satisfies (i(1)) = 0.
The example in Proposition 2.14 is universal for rank-two theories in the sense of the
following proposition.
Proposition 2.15 Let R be a commutative ring with unit and let (V, θ0 , φ0 ) be a
rank-two extended Frobenius algebra over R satisfying (i(1)) = 0. Then there exists a
ring homomorphism K → R such that (Uψ , θ ⊗ 1, φ ⊗ Id) is isomorphic to (V, θ0 , φ0 ).
Proof Any rank-two Frobenius algebra V over R satisfying (i(1)) = 0 is of the
following form (see Khovanov [10]). As an R–module we can write V = R{1, x}
and there are elements a, f , h, t ∈ R such that af = 1. In terms of these elements
multiplication is defined by
11 = 1,

1x = x1 = x

Algebraic & Geometric Topology 6 (2006)

and

xx = hx + t1

<!-- page 15 -->
Unoriented topological quantum field theory and link homology

1083

and comultiplication is defined by
∆(1) = f (1 ⊗ x + x ⊗ 1) − hf 1 ⊗ 1

and ∆(x) = fx ⊗ x + ft1 ⊗ 1.

The unit and counit are given by
(1) = 0,

(x) = a and

i(1) = 1.

Suppose now θ ∈ V and φ : V → V such that (V, θ, φ) is an extended Frobenius
algebra. Since φ is a map of Frobenius algebras we must have φ(1) = 1. Now write
θ = λ1 + µx

and φ(x) = β1 + γx.

We have (x) = (φ(x)) from which we have
a = (x) = (β1 + γx) = β(1) + γ(x) = γa.
Multiplying by f and recalling that af = 1 we see γ = 1.
By axiom (1) of Definition 2.5 we have θ = φ(θ) and θx = φ(θx). These two relations
imply that µβ = 0 and λβ = 0.
By axiom (2) we have m(φ ⊗ Id)((∆(1)) = θ2 . Now the left-hand side is equal to
(f β − hf )1 + 2fx and the right-hand side is equal to (λ2 + µ2 t)1 + (2λµ + µ2 h)x. Thus
we have
λ2 + µ2 t = f β − hf

and

2λµ + µ2 h = 2f .

Recalling that af = 1 the first equation gives h = β − aλ2 − aµ2 t and the second
2aλµ + aµ2 h = 2. Substituting for h in the latter gives
2aλµ − a2 µ2 λ2 − a2 µ4 t = 2.
The additional demand that φ is an involution and respects multiplication and comultiplication does not introduce any further relations.
Thus θ must be of the form θ = λ1 + µx and φ must be of the form φ(1) = 1 and
φ(x) = β1 + x where λ, µ, β ∈ U satisfy
µβ = λβ = 0

and

2aλµ − a2 µ2 λ2 − a2 µ4 t = 2,

and there are no further relations necessary. Along with the relation af = 1 these
are the relations defining K so there is a map ψ : K → R as required. Noting that
h = β − aλ2 − aµ2 t one easily sees that Uψ ∼
= V.

Algebraic & Geometric Topology 6 (2006)

<!-- page 16 -->
1084

3

Vladimir Turaev and Paul Turner

The complex of cobordisms for a link diagram on a surface

We consider oriented link diagrams on closed orientable surfaces (as depicted for
example in Figure 2) and define an equivalence relation on such diagrams as follows.
Two diagrams are said to be stably equivalent if they are related by
(1) surface homeomorphisms
(2) Reidemeister moves
(3) addition or subtraction of handles to the surface (when no part of the diagram is
on the handle).

1
2

3

Figure 2: An oriented knot diagram on a torus

Given a link diagram on a closed orientable surface Σ we wish to define a complex of
cobordisms along the lines of Bar-Natan’s complex for link diagrams given in [5].
Recall that for an additive category C the additive category Mat(C) is defined as
follows. Its objects are finite families {Ci }i of objects Ci ∈ C which for convenience
will be denoted ⊕Ci . A morphism F : ⊕ Ci → ⊕Cj0 is a matrix F = [Fij ] of morphisms
Fij : Ci → Cj0 in C . We will refer to the Fij as the matrix elements of the morphism F .
P
Composition is defined in terms of matrix elements by the rule [F ◦ G]ki = j Fjk ◦ Gji
and addition of morphisms given by matrix addition. If C is not additive then it is made
so by allowing formal Z–linear combinations of morphisms.
Define UCob(Σ) to be the following category. The objects are collections of disjoint
closed curves Γ in Σ. A morphism Γ → Γ0 is a surface embedded in Σ × I whose
boundary lies entirely in Σ × {0, 1} and which agrees with Γ on Σ × {0} and with
Γ0 on Σ × {1}. Two such morphisms are identified if they are related by a boundary
preserving isotopy. Since cobordisms are embedded one can clearly compose them
(rescaling the result).
Algebraic & Geometric Topology 6 (2006)

<!-- page 17 -->
Unoriented topological quantum field theory and link homology

1085

Given an oriented link diagram D on an orientable surface Σ we first number the
crossings 1, . . . , n. We can resolve each crossing in one of two ways as depicted in
Figure 3.
0{smoothing

1{smoothing

Figure 3

A resolution of each of the n crossings of D will be called a smoothing. There are 2n
such smoothings and each is indexed by a sequence s of n 0’s and 1’s, the i–th entry
informing us whether the i–th crossing is a 0– or 1–smoothing. The smoothing itself
consists of a closed 1–manifold Γs being a collection of nonintersecting closed curves
in Σ. Note that Γs is an object in the category UCob(Σ). Smoothings form a poset via
s < t iff all 1–smoothings in s are 1–smoothings in t.
Let

r(s) = number of 1–smoothings in s

and

k(s) = number of components in Γs .

As is familiar the smoothings are arranged on the vertices of a cube with an arrow from
s to t if s < t and r(t) = r(s) + 1. The cube for the knot given in Figure 2 is presented
in Figure 4 where the underlying torus has been omitted.
If s and t are smoothings such that r(t) = r(s) + 1 and s < t then Γt must be identical
to Γs outside a small disc in Σ around a 1–smoothing in Γt . We refer to this disc as
the changing disc. In this situation we define hs, ti to be the number of 1–smoothings
among the first j − 1 crossings of t where the j–th crossing is the one in the changing
disc.
For such s and t define Wst ⊂ Σ × I to be the surface which is Γs on Σ × {0}, Γ1 on
Σ × {1}, a product outside (changing disc) × I and a saddle in place of the missing
(changing disc) × I . We regard Wst as a morphism Γs → Γt in the category UCob(Σ).
M
Set
[[D]]i =
Γs ∈ Ob(Mat(UCob(Σ)))
s

where the sum is over all smoothings s with r(s) = i + n− . Here n− is the number of
negative crossings in D.
Algebraic & Geometric Topology 6 (2006)

<!-- page 18 -->
1086

Vladimir Turaev and Paul Turner

000

100

101

010

101

001

011

111

Figure 4: The cube of the diagram in Figure 2

We now want to define a morphism di : [[D]]i → [[D]]i+1 . In order to define di it is
enough to define its matrix elements (di )ts : Γs → Γt where s and t are smoothings such
that r(s) = i + n− and r(t) = i + 1 + n− . Define these matrix elements by
(
(−1)hs,ti Wst if s < t
i t
(d )s =
0
else.
Proposition 3.1 Given a diagram D, the morphism d defined above satisfies d2 = 0.
Thus ([[D]]∗ , d) is a complex in Mat(UCob(Σ)).
Proof Given a square face of the cube
t
? ???
??


??

?


s>
?u
>>
>>
>>
>
t0

0
we note that Wtu ◦ Wst ∼
= Wtu0 ◦ Wst since saddles can be reordered. The signs chosen in
the definition of the matrix elements ensure that each square anticommutes.

We continue following [5] by quotienting the category UCob(Σ) by certain relations.
These relations, the S,T, 4–Tu (Sphere, Torus and 4–Tube) relations are illustrated below
in Figure 5.
Algebraic & Geometric Topology 6 (2006)

<!-- page 19 -->
1087

Unoriented topological quantum field theory and link homology

=0
S

=2
T

+

=

+

4–Tu

Figure 5: Bar-Natan’s relations

Definition 3.2 Let UCob(Σ)/r be the category obtained from UCob(Σ) by quotienting
by the equivalence relation generated by relations S,T,4-Tu.
Proposition 3.3 Let D be a link diagram on a closed orientable surface Σ. The
homotopy type of the complex ([[D]], d) in Mat(UCob(Σ)/r ) is invariant under
Reidemeister moves.
Proof In [5] Bar-Natan has proved the analogous statement for planar link diagrams.
His proofs remain valid in our setting too.

4

Link homology

4.1

Applying an unoriented TQFT to get link homology

In this section we will apply a rank-two aspherical unoriented TQFT to the formal
complex of cobordisms of the previous section to obtain a complex of R–modules.
We can then take homology of this complex to obtain a calculable invariant of stable
equivalence classes of link diagrams on surfaces.
While geometrically the 4-Tu relation is a genuine relation on cobordisms, algebraically
it comes for free for aspherical theories.
Proposition 4.1 Let (A, τ ) be a rank-two aspherical unoriented TQFT. Suppose
cobordisms W1 , W2 , W3 , W4 are related locally as in the 4-Tu relation above then
τ (W1 ) + τ (W2 ) = τ (W3 ) + τ (W4 ).
Proof In order to do computations we need to work with the underlying Frobenius
algebra and in order to do that we need to pick identifications γi : V → Γi , i = 1, 2, 3, 4,
where the Γi are the four circles appearing W1 (and W2 , W3 , W4 ) where the local surgery
takes place. (Note that we are assuming that W1 , W2 , W3 , W4 are actually the same
manifold outside the ball in which the local change takes place.) We need to show:
Algebraic & Geometric Topology 6 (2006)

<!-- page 20 -->
1088

Vladimir Turaev and Paul Turner

which by using the identifications γi can be converted into the condition on the
underlying Frobenius algebra:
Σa0 ⊗ a00 ⊗ 1 ⊗ 1 + Σ1 ⊗ 1 ⊗ a0 ⊗ a00 = Σa0 ⊗ 1 ⊗ a00 ⊗ 1 + Σ1 ⊗ a0 ⊗ 1 ⊗ a00
where we write ∆(1) = Σa0 ⊗ a00 . By Proposition 2.15 it suffices to consider the
universal extended Frobenius algebra. Since here ∆(1) = f (1 ⊗ x + x ⊗ 1) − hf 1 ⊗ 1 it
is easy to verify that the above equation holds.
Let (A, τ ) be a rank-two aspherical unoriented TQFT. We can now define a functor
UCob(Σ) → ModR by
Γ 7→ AΓ ,
W 7→ τ (W).
This does indeed give a functor since by axiom (4) in Definition 2.1 homeomorphisms
preserving the boundary point-wise induce the same map τ and composition in UCob(Σ)
glues along the identity map and so τ (W 0 ◦ W) = τ (W 0 ) ◦ Id ◦τ (W). Note also that by
axiom (7) cylinders give the identity homomorphism.
By taking formal direct sums to genuine direct sums this extends to a functor
Mat(UCob(Σ)) → ModR .
Since (A, τ ) is rank-two and aspherical, Proposition 4.1 shows that this functor factors
through Mat(UCob(Σ)/r ) and hence there is a functor F(A,τ ) on the associated categories
of complexes
F(A,τ ) : Kom(Mat(UCob(Σ)/r )) → Kom(ModR ).
Given a link diagram D on a surface set
∗
∗
C(A,τ
) (D) = F(A,τ ) ([[D]] ).
∗
Proposition 4.2 The homotopy type of the complex C(A,τ
) (D) is an invariant of stable
equivalence classes.

Proof Let Σ → Σ0 be a homeomorphism of surfaces. This induces homeomorphisms
Γs → Γ0s on smoothings and homeomorphisms Wst → (W 0 )ts on the cobordisms defining
the complexes. Applying the TQFT gives isomorphisms AΓs → AΓ0s which in turn
Algebraic & Geometric Topology 6 (2006)

<!-- page 21 -->
Unoriented topological quantum field theory and link homology

1089

∗
∗
0
induce an isomorphism (of graded vector spaces) C(A,τ
) (D) → C(A,τ ) (D) . By axiom
(4) in the definition of TQFT we see that this is an isomorphism of complexes.

Showing invariance under Reidemeister moves is the content of Proposition 3.3.
If Σ0 is obtained from Σ by the addition or subtraction of handles disjoint from the
diagram then clearly there is a canonical identification of smoothings and cobordisms in
the complexes [[D]]0 and [[D]] (defined above using Σ0 and Σ). These identifications
∗
∗
0
lead to an isomorphism of complexes C(A,τ
) (D) → C(A,τ ) (D) .
Thus if L is a stable equivalence class of diagrams we can now define what we mean by
link homology.
Definition 4.3 The link homology for stable equivalence classes based on the TQFT
(A, τ ) is defined by
∗
∗
H(A,τ
) (L) = H(C(A,τ ) (D))
where D is any representative diagram of the class L.
Note that if we replace the unoriented TQFT (A, τ ) with an isomorphic one (A0 , τ 0 ) then
there are isomorphisms η : AΓs → A0Γs . As these are natural with respect to cobordisms
∗
∗
they induce an isomorphism of complexes C(A,τ
) (D) → C(A0 ,τ 0 ) (D). Thus isomorphic
TQFTs result in isomorphic link homology groups.
We now present our main result.
Theorem 4.4 Let R be a commutative ring with unit. Let λ, µ, β, a, t ∈ R such that a
is invertible and the following relations are satisfied:
(1)

µβ = λβ = 0,

(2)

2aλµ − a2 µ2 λ2 − a2 µ4 t = 2.

Then the 5–tuple (λ, µ, β, a, t) defines (the isomorphism class of) a link homology
theory for stable equivalence classes of diagrams on oriented surfaces.
Proof The obvious map ψ : K → R defines a rank-two extended Frobenius algebra
(V, θ, φ) satisfying (i(1)) = 0. This in turn defines a rank-two aspherical 1+1–
dimensional unoriented TQFT. Such a theory defines a link homology for stable
equivalence classes as described above.
Corollary 4.5 If R is an integral domain then each triple (a, λ, µ) with a and µ
invertible defines a link homology.

Algebraic & Geometric Topology 6 (2006)

<!-- page 22 -->
1090

4.2

Vladimir Turaev and Paul Turner

Link homologies over Q

Clearly there are solutions to equations (1) and (2) over Q. The question we now
address is whether or not any of these extend a theory isomorphic to Khovanov’s original
link homology. Given h, t ∈ Q then there is a link homology defined by the Frobenius
algebra Q{1, x} with i(1) = 1, (1) = 0, (x) = 1 and x2 = hx + t1. Recall from [11]
that such a theory is isomorphic to Khovanov’s original theory if and only if h2 + 4t = 0.
Noting that over Q we must have β = 0 and µ 6= 0 we can express h and t in terms of
λ and µ as
h = 2µ−2 − 2λµ−1

and

t = −µ−2 λ2 − 2µ−4 + 2λµ−3 .

A computation now shows
h2 + 4t = −4µ−4 .
Thus we have h2 + 4t 6= 0 resulting in the disappointing conclusion that Khovanov’s
original theory does not extend (at least using the methods of this paper) to stable
equivalence classes. This conclusion remains valid over fields of characteristic not
equal to two.
Over Q the resulting theories are all singly graded. For each of these the Euler
characteristic, χ, is the unnormalised Jones polynomial evaluated at q = 1. To see this
recall that the Euler characteristic of the homology of a complex is the same as the
Euler characteristic of the complex itself and so
X
X
χ=
(−1)i dim(H i (D)) =
(−1)i dim(F(A,τ ) ([[D]]i ))
i

i

X
=
(−1)i
i

X

dim(AΓs ) =

X
(−1)i

s∈smoothings
r(s)=i+n−

X

2k(s)

s∈smoothings
r(s)=i+n−

where k(s) is the number of components in Γs . Comparing with the definition of the
Jones polynomial we see that the right-hand side is the unnormalised Jones polynomial
evaluated at 1.

4.3

Link homologies over F2

Working over F2 one has more success than over the rationals. One has a = 1 and the
remaining equations of the main theorem become
µβ = λβ = 0

and µ2 λ2 + µ4 t = 0.

There are eight possibilities as tabulated below.
Algebraic & Geometric Topology 6 (2006)

<!-- page 23 -->
Unoriented topological quantum field theory and link homology
λ
0
0
1
0
0
1
0
1

µ
0
0
0
0
0
0
1
1

t
0
0
0
1
1
1
0
1

β
0
1
0
0
1
0
0
0

h
0
1
1
0
1
1
0
0

θ
0
0
1
0
0
1
x
1+x

1091

φ(x)
x
1+x
x
x
1+x
x
x
x

Rows 1, 4, 7 and 8 have isomorphic underlying Frobenius algebras and on classical
links give theories that are isomorphic to Khovanov’s original theory over F2 . As
extended Frobenius algebras there are two isomorphism classes among these with row 1
isomorphic to row 4 and row 7 isomorphic to row 8. The theory in the first row gives a
bigraded theory and was investigated by Manturov [12]. He observes that the graded
Euler characteristic (which can be computed from the graded Euler characteristic of the
chain complex) is the unnormalised Jones polynomial of the link.
The theory in row 3 can be made into a bigraded theory by taking R = F2 [λ] with λ in
degree −1. The Frobenius algebra has multiplication
11 = 1,

1x = x1 = x

and xx = λ2 x

and comultiplication
∆(1) = 1 ⊗ x + x ⊗ 1 + λ2 1 ⊗ 1,
∆(x) = x ⊗ x.
The counit is (1) = 0, (x) = 1. This is isomorphic to Bar-Natan’s graded characteristic
two theory. For the extended structure we have θ = λ1and φ = Id. This theory
is related to Manturov’s theory: one can filter the chain complex by powers of λ to
produce a spectral sequence (similar to that in [14]) whose E2 –page is Manturov’s
theory and which converges to the bigraded theory.
It is interesting to note that this extended Frobenius algebra has an interpretation in
terms of the equivariant cohomology of S2 along the lines of [10]. Let G = Z/2 act on
S2 by a rotation through π about a fixed axis. In this case we have
HG∗ (pt; F2 ) = H ∗ (RP∞ ; F2 ) = F2 [λ]
and

HG∗ (S2 ; F2 ) = F2 [λ, x]/hx2 = λ2 xi = F2 [λ][x]/hx2 = λ2 xi.

We see that this is the algebra of the bigraded link homology above and the element
θ is the image of the generator of HG∗ (pt; F2 ) under the homomorphism induced from
S2 → pt.
Algebraic & Geometric Topology 6 (2006)

<!-- page 24 -->
1092

Vladimir Turaev and Paul Turner

Bigraded Bar-Natan theory is also extended by the theory in row 2. Here we work over
R = F2 [β] with β in degree −2. In this case θ = 0 and φ(x) = β1 + x. Note that in
this case we have a nontrivial involution φ.

4.4

Acknowledgments

We thank D Bar-Natan and G Naot for many helpful comments. The second author was
supported by the European Commission through a Marie Curie fellowship and thanks
the Institut de Recherche Mathématique Avancée in Strasbourg for their hospitality.

References
[1] A Alexeevski, S Natanzon, Noncommutative two-dimensional field theories and
Hurwitz numbers for real algebraic curves arXiv:math.GT/0202164
[2] M M Asaeda, J H Przytycki, A S Sikora, Categorification of the Kauffman bracket
skein module of I -bundles over surfaces, Algebr. Geom. Topol. 4 (2004) 1177–1210
MR2113902
[3] M Atiyah, Topological quantum field theories, Inst. Hautes Études Sci. Publ. Math.
(1988) 175–186 (1989) MR1001453
[4] D Bar-Natan, On Khovanov’s categorification of the Jones polynomial, Algebr. Geom.
Topol. 2 (2002) 337–370 MR1917056
[5] D Bar-Natan, Khovanov’s homology for tangles and cobordisms, Geom. Topol. 9
(2005) 1443–1499 MR2174270
[6] R Fenn, L Kauffman, V Manturov, Virtual Knot Theory - Unsolved Problems arXiv:
math.GT/0405428
[7] M Jacobsson, An invariant of link cobordisms from Khovanov homology, Algebr. Geom.
Topol. 4 (2004) 1211–1251 MR2113903
[8] L Kauffman, V Manturov, Virtual Knots and Links arXiv:math.GT/0502014
[9] M Khovanov, A categorification of the Jones polynomial, Duke Math. J. 101 (2000)
359–426 MR1740682
[10] M Khovanov, Link homology and Frobenius extensions, Fund. Math. 190 (2006)
179–190
[11] M Mackaay, P Turner, P Vaz, A remark on Rasmussen’s invariant of knots arXiv:
math.GT/0509692
[12] V Manturov, The Khovanov complex for virtual links arXiv:math.GT/0501317

Algebraic & Geometric Topology 6 (2006)

<!-- page 25 -->
Unoriented topological quantum field theory and link homology

1093

[13] V G Turaev, Quantum invariants of knots and 3-manifolds, de Gruyter Studies in
Mathematics 18, Walter de Gruyter & Co., Berlin (1994) MR1292673
[14] P Turner, Calculating Bar-Natan’s characteristic two Khovanov homology arXiv:
math.GT/0411225
Institut de Recherche Mathematique Avancee
7 rue Rene Descartes, 67000 Strasbourg, France
School of Mathematical and Computer Sciences, Heriot-Watt University
Edinburgh EH14 4AS, Scotland
turaev@math.u-strasbg.fr, paul@ma.hw.ac.uk
Received: 1 September 2005

Revised: 16 January 2006

Algebraic & Geometric Topology 6 (2006)
