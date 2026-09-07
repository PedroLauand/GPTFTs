---
type: paper
date: 2006-09-05
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:hep-th/0609042v1)
reviewed: false
---

# D-branes and K-theory in 2D topological field theory

Machine-generated and unreviewed text extraction of arXiv:hep-th/0609042v1
(89 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/hep-th/0609042v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
RUNHETC-06-12

arXiv:hep-th/0609042v1 5 Sep 2006

hep-th/0609042

D-branes and K-theory
in 2D topological field theory

Gregory W. Moore
Department of Physics, Rutgers University
Piscataway, New Jersey, 08855-0849
Graeme Segal
All Souls College
Oxford University, Oxford, OX1 4AL, England
This expository paper describes sewing conditions in two-dimensional open/closed topological field theory. We include a description of the G-equivariant case, where G is a finite
group. We determine the category of boundary conditions in the case that the closed string
algebra is semisimple. In this case we find that sewing constraints – the most primitive
form of worldsheet locality – already imply that D-branes are (G-twisted) vector bundles on
spacetime. We comment on extensions to cochain-valued theories and various applications.
Finally, we give uniform proofs of all relevant sewing theorems using Morse theory.

August 31, 2006

<!-- page 2 -->
1. Introduction and Summary
The theory of D-branes has proven to be of great importance in the development of
string theory. In this paper we will focus on certain mathematical structures central to the
idea of D-branes. One of the questions which motivated our work was: “Given a closed
string background, what is the set of possible D-branes?” This is a rather complicated
question. One might at first be tempted to declare that D-branes simply correspond to
conformally invariant boundary conditions for the open string. This viewpoint is not
very useful because there are too many such boundary conditions, and in general they
have no geometrical description. It also neglects important restrictions imposed by sewing
consistency conditions.
In this paper we address the above problem in the drastically simpler case of twodimensional topological field theory (TFT), where the whole content of the theory is encoded in a finite-dimensional commutative Frobenius algebra. We shall find that describing
the sewing conditions, and their solutions for 2d topological open and closed TFT, is a
tractable but not entirely trivial problem. We also extend our results to the equivariant
case, where we are given a finite group G, and the worldsheets are surfaces equipped with
G-bundles. This is relevant to the classification of D-branes in orbifolds.
Another one of our primary motivations has been the desire to understand the relation
between D-branes and K-theory in the simplest possible terms. This relation is often
justified by considerations of anomaly cancellation or of brane-antibrane annihilation. Our
analysis shows that the relation is, in some sense, more primitive, and follows simply from
sewing constraints.
We hope the present work will be of some pedagogical interest in explaining the
structure of boundary conformal field theory and its connections to K-theory in the simplest
context. There are also, however, some potential applications of our results. One ambitious
goal is to classify the boundary conditions in topologically twisted nonlinear sigma models
and their allied topological string theories. Here we have some suggestive results, but they
are far from a complete theory.
Our main concrete results are the following two theorems. To state the first we must
point out that a semisimple Frobenius algebra1 C is automatically the algebra of complexvalued functions on a finite set X = Spec(C) — the “space-time” — which is equipped

with a “volume-form” or “dilaton field” θ which assigns a measure θx to each point x ∈ X.
1

For basic material on Frobenius algebras see, for example, [1], ch. 9 or [2].

1

<!-- page 3 -->
Theorem A For a semisimple 2-dimensional TFT corresponding to a finite space-time
(X, θ) the choice of a maximal category of D-branes fixes a choice of a square-root of
θx for each point x of X. The category of boundary conditions is equivalent to the
category Vect(X) of finite-dimensional complex vector bundles on X. The correspondence is, however, not canonical, but is arbitrary up to composition with an equivalence
Vect(X) → Vect(X) given by tensoring each vector bundle with a fixed line bundle (i.e.
one which does not depend on the particular D-brane).

Conversely, if we are given a semisimple Frobenius category B, then it is the category of

boundary conditions for a canonical 2-dimensional TFT corresponding to the commutative
Frobenius algebra which is the ring of endomorphisms of the identity functor of B.
We shall explain in the next section the sense in which the boundary conditions form
a category. The theorem will be proved in section 3. In §3.4 we shall describe an analogue
of the theorem for spin theories.

The second theorem relates to “G-equivariant” or “G-gauged” TFTs, where G is a
finite group. Turaev has shown that in dimension 2 a semisimple G-equivariant TFT
corresponds to a finite space-time X on which the group G acts in a given way, and which
is equipped with a G-invariant dilaton field θ and as well as a “B-field” B representing an
3
(X; ZZ).
element of the equivariant cohomology group HG

Theorem B For a semisimple G-equivariant TFT corresponding to a finite space time
(X, θ, B) the choice of a maximal category of D-branes fixes a G-invariant choice of
√
square roots θ x as before, and then the category is equivalent to the category of finitedimensional B-twisted G-vector-bundles on X, up to an overall tensoring with a G-linebundle.
In this case the category of D-branes is equivalent to that of the “orbifold” theory
obtained from the gauged theory by integrating over the gauge fields, and it does not
remember the equivariant theory from which the orbifold theory arose. There is, however,
a natural enrichment which does remember the equivariant theory.
This will be explained and proved in section 7.
The restriction to the semisimple case in our results seems at first a damaging weakness. We believe, however, that it is this case that reveals the essential structure of the
2

<!-- page 4 -->
theory. To go beyond it, the appropriate objects of study, in our view, are cochain-complexvalued TFTs rather than non-semisimple TFTs in the usual sense. (This is analogous to
the fact that in ordinary algebra the duality theory of non-projective modules is best studied in the derived category.) We have said something about this line of development in
sections 2 and 6, explaining how the category of boundary conditions is naturally an A∞
category in the sense of Fukaya, Kontsevich, and others.
Let us comment on one important conceptual aspect of the results of this paper.
In the Matrix theory approach to nonperturbative string theory [3][4] open string field
theory, or rather its low-energy Yang-Mills theory, is taken to be the fundamental starting
point for the formulation of the entire string theory. In particular, spacetime, and the
closed strings, are regarded as derived concepts. A similar philosophy lies at the root of
the AdS/CFT correspondence. In this paper we begin our discussion with the viewpoint
that the spacetime and closed strings are fundamental and then ask what category of
boundary conditions is compatible with that background. However, in the semisimple
case, we find that one could equally well start with the Frobenius category of boundary
conditions and derive the closed strings and the spacetime. Thus, our treatment is in
harmony with the philosophy of Matrix theory. Indeed, it is possible to obtain the closed
string algebra from the open string algebra by taking the center of the open string algebra
Z(O) ∼
= C. (In general the Cardy condition only shows that ι∗ (C) maps into the center.)

A more sophisticated version of this idea is that the closed string algebra is obtained from
the category of boundary conditions by considering the endomorphisms of the identity
functor. All this is discussed in §3.3, and justifies the important point that there is a
converse statement to Theorem A.

A closely related point is that in open string field theory there are different open
string algebras Oaa for the different boundary conditions a. For boundary conditions with

maximal support, however, they are Morita equivalent via the bimodules Oab . For some

purposes it might seem more elegant to start with a single algebra. (Indeed, Witten has
suggested in [5] that one should use something analogous to stabilization of C ∗ algebras,
namely one should replace the string field algebra by Oaa ⊗ K where K is the algebra

of compact operators.) In our framework, the single algebra is replaced by the category
of boundary conditions. If one believes that a stringy spacetime is a non-commutative
space, our framework is in good agreement with Kontsevich’s approach to non-commutative
geometry, according to which a non-commutative space is a linear category — essentially
the category of modules for the ring, if the space is defined by a ring. For commutative
3

<!-- page 5 -->
rings the category of modules determines the ring, but in the non-commutative case the
ring is determined only up to Morita equivalence. We discuss this further in section §3.

Finally, we comment briefly on some related literature. There is a rather large litera-

ture on 2d TFT and it is impossible to give comprehensive references. Here we just indicate
some closely related works. The 2d closed sewing theorem is a very old result implicit in
the earliest papers in string theory. The algebraic formulation was perhaps first formulated by Friedan. Accounts have been given in [6][7][8] and in the Stanford lectures by
Segal [9]. Sewing constraints in 2D open and closed string theory were first investigated in
[10]. Extensions to unorientable worldsheets were described in [11][12][13][14]. Our work–
which is primarily intended as a pedagogical exposition – was first described at Strings
2000 [15] and summarized briefly in [16]. It was described more completely in lectures at
the KITP in 2001 and at the 2002 Clay School [17]. In [18] one can find alternative (more
computational) proofs and examples to those we give below, together with better quality
pictures. 2 Some of our work was independently obtained in the papers of C. Lazaroiu [19]
although the emphasis in these papers is on applications to disk instanton corrections in
low energy supergravity. Regarding G-equivariant theories, there is a very large literature
on D-branes and orbifolds not reflected in the above references. In the context of 2D TFT
two relevant references are [20][21]. Alternative discussions on the meaning of B-fields in
orbifolds (in TFT) can be found in [22][23][24]. Our treatment of cochain-level theories
and A∞ algebras has been developed considerably further by Costello [25].
Acknowledgments
We would like to thank Ilka Brunner, Robbert Dijkgraaf, Dan Freed, Kentaro Hori
and Anton Kapustin for some useful and clarifying discussions. GM would like to thank
Phil Candelas and Xenia de la Ossa for hospitality at Oxford during the course of this
work. We thank K. Rabe for assistance with the figures. GM and GS thank the ITP for
hospitality during the initiation of this work (August 1998) and during the writing of the
manuscript (March 2001). We also thank the Aspen Center for Physics where some of this
work was done. GM would like to thank the IAS and the Monell foundation for hospitality
during the completion of this work. The work of GM is also supported by DOE grant
DE-FG02-96ER40949.
2

Please note that the arrows on some morphisms in figures 4, 35-38, 47-48 have the wrong

orientation.

4

<!-- page 6 -->
2. The sewing theorem
2.1. Definition of open and closed 2D TFT
Roughly speaking, a quantum field theory is a functor from a geometric category to
a linear category. The simplest example is a topological field theory, where we choose the
geometric category to be the category whose objects are closed, oriented (d − 1)-manifolds,
and whose morphisms are oriented cobordisms (two such cobordisms being identified if
they are diffeomorphic by a diffeomorphism which is the identity on the incoming and
outgoing boundaries). The linear category in this case is simply the category of complex
vector spaces and linear maps, and the only property we require of the functor is that (on
objects and morphisms) it takes disjoint unions to tensor products. The case d = 2 is of
course especially well known and understood.
There are several natural ways to generalize the geometric category. One may, for
example, consider manifolds equipped with some structure such as a Riemannian metric.
(We shall discuss some examples in the following.) The focus of this paper is on a different
kind of generalization where the objects of the geometric category are oriented (d − 1)manifolds with boundary, and each boundary component is labelled with an element of
a fixed set B0 called the set of boundary conditions. In this case a cobordism from Y0 to
Y1 means a d-manifold X whose boundary consists of three parts ∂X = Y0 ∪ Y1 ∪ ∂cstr X,
where the “constrained boundary” ∂cstr X is a cobordism from ∂Y0 to ∂Y1 . Furthermore,
we require the connected components of ∂cstr X to be labelled with elements of B0 in
agreement with the labelling of ∂Y0 and ∂Y1 .
Thus when d = 2 the objects of the geometric category are disjoint unions of circles
and oriented intervals with labelled ends. A functor from this category to complex vector
spaces which takes disjoint unions to tensor products will be called an open and closed
topological field theory: such theories will give us a “baby” model of the theory of Dbranes. We shall always write C for the vector space associated to the standard circle S 1 ,
and Oab for the vector space associated to the interval [0, 1] with ends labelled by a, b ∈ B0 .
5

<!-- page 7 -->
Fig. 1: Basic cobordism on open strings.

map

The cobordism fig. 1 gives us a linear map Oab ⊗ Obc → Oac , or equivalently a bilinear
Oab × Obc → Oac ,

(2.1)

which we think of as a composition law. In fact we have a C-linear category B whose

objects are the elements of B0 , and whose set of morphisms from b to a is the vector space

Oab , with composition of morphisms given by (2.1) . (To say that B is a category means

no more than that the composition (2.1) is associative in the obvious sense, and that there
is an identity element 1a ∈ Oaa for each a ∈ B0 ; we shall explain presently why these

properties hold.)

For any open and closed TFT we have a map e : C → C defined by the cylindrical

cobordism S 1 × [0, 1], and a map eab : Oab → Oab defined by the square [0, 1] × [0, 1].
Clearly e2 = e and e2ab = eab . If all these maps are identity maps we say the theory is
reduced. There is no loss in restricting ourselves to reduced theories, and we shall do so
from now on.
2.2. Algebraic characterization
The most general 2D open and closed TFT, formulated as in the previous section, is
given by the following algebraic data:
1. (C, θC , 1C ) is a commutative Frobenius algebra.
2a. Oab is a collection of vector spaces for a, b ∈ B0 with an associative bilinear

product

Oab ⊗ Obc → Oac
6

(2.2)

<!-- page 8 -->
2b. The Oaa have nondegenerate traces
θa : Oaa → C

(2.3)

In particular, each Oaa is a not-necessarily commutative Frobenius algebra.
2c. Moreover,
θ

a
Oab ⊗ Oba → Oaa →
C

θ

(2.4)

Oba ⊗ Oab → Obb →b C
are perfect pairings with
θa (ψ1 ψ2 ) = θb (ψ2 ψ1 )

(2.5)

ιa : C → Oaa

(2.6)

for ψ1 ∈ Oab , ψ2 ∈ Oba .
3. There are linear maps:
ιa : Oaa → C
such that
3a. ιa is an algebra homomorphism
ιa (φ1 φ2 ) = ιa (φ1 )ιa (φ2 )

(2.7)

3b. The identity is preserved

ιa (1C ) = 1a

(2.8)

3c. Moreover, ιa is central in the sense that
ιa (φ)ψ = ψιb (φ)

(2.9)

θC (ιa (ψ)φ) = θa (ψιa (φ))

(2.10)

for all φ ∈ C and ψ ∈ Oab

3d. ιa and ιa are adjoints:

for all ψ ∈ Oaa .
7

<!-- page 9 -->
3e. The “Cardy conditions.”3 Define πb a : Oaa → Obb as follows. Since Oab and Oba

are in duality (using θa or θb ), if we let ψµ be a basis for Oba then there is a dual basis ψ µ

for Oab . Then we define

πb a (ψ) =

X

ψµ ψψ µ ,

(2.11)

µ

and we have the “Cardy condition”:
πb a = ιb ◦ ιa .

(2.12)

Fig. 2: Four diagrams defining the Frobenius structure in a closed 2d TFT. It is
often more convenient to represent the morphisms by the planar diagrams. In this
case our convention is that a circle oriented so that the right hand points into the
surface is an ingoing circle.

Fig. 3: Associativity, commutativity, and unit constraints in the closed case. The
unit constraint requires the natural assumption that the cylinder correspond to the
identity map C → C.
3

These are actually generalization of the conditions stated by Cardy. One recovers his condi-

tions by taking the trace. Of course, the factorization of the double twist diagram in the closed
string channel is an observation going back to the earliest days of string theory.

8

<!-- page 10 -->
2.3. Pictorial representation
Let us explain the pictorial basis for these algebraic conditions. The case of a closed 2d
TFT is very well-known. The data of the Frobenius structure is provided by the diagrams
in fig. 2. The consistency conditions follow from fig. 3.

Fig. 4: Basic data for the open theory. Constrained boundaries are denoted with
wiggly lines, and carry a boundary condition a, b, c, . . . ∈ B0 ..

Fig. 5: Assuming that the strip corresponds to the identity morphism we must
have perfect pairings in (2.4).

Fig. 6: Two ways of representing open to closed and closed to open transitions.

9

<!-- page 11 -->
Fig. 7: ιa is a homomorphism.

Fig. 8: ιa preserves the identity.

Fig. 9: ιa maps into the center of Oaa .

Fig. 10: ιa is the adjoint of ιa .

In the open case, entirely analogous considerations lead to the construction of a nonnecessarily commutative Frobenius algebra in the open sector. The basic data are summa10

<!-- page 12 -->
Fig. 11: The double-twist diagram defines the map πba : Oaa → Obb .

Fig. 12: The (generalized) Cardy-condition expressing factorization of the doubletwist diagram in the closed string channel.

rized in fig. 4. The fact that (2.4) are dual pairings follows from fig. 5. The essential new
ingredient in the open/closed theory are the open to closed and closed to open transitions.
In 2d TFT these are the maps ιa , ιa . They are represented by fig. 6. There are five new
consistency conditions associated with the open/closed transitions. These are illustrated
in fig. 7 to fig. 12.
2.4. Sewing theorem
Geometrically, any oriented surface can be decomposed into a composition of morphisms corresponding to the basic data defining the Frobenius structure. However, a given
surface can be decomposed in many different ways. The above sewing axioms follow from
consistency of these decompositions. The sewing theorem guarantees that there are no
further relations on the algebraic data imposed by consistency of sewing.
Theorem 1 Conditions 1,2,3 above are the only conditions on the algebraic data coming
from cutting the morphisms in all possible ways.
The proof is in appendix A.
11

<!-- page 13 -->
2.5. The category of boundary conditions
The category B of boundary conditions of an open and closed TFT is an additive

category. We can always adjoin new objects to it in various ways. For example, we may

as well assume that it possesses direct sums, as we can define for any two objects a and b
a new object a ⊕ b by

Oa⊕b,c := Oac ⊕ Obc

(2.13)

Oc,a⊕b := Oca ⊕ Ocb ,

(2.14)

and hence
Oa⊕b,a⊕b :=
with the obvious composition laws, and



Oaa
Oba

Oab
Obb



,

θa⊕b : Oa⊕b,a⊕b → C

(2.15)

(2.16)

given by
θa⊕b



ψaa
ψba

ψab
ψbb



= θa (ψaa ) + θb (ψbb ).

(2.17)

The new object is the direct sum of a and b in the enlarged category of boundary conditions.
If there was already a direct sum of a and b in the category B then the new object

will be canonically isomorphic to it. In the opposite direction, if we have a boundary
condition a and a projection p ∈ Oaa (i.e. an element such that p2 = p) then we may

as well assume there is a boundary condition b = image(p) such that for any c we have

Ocb = {f ∈ Oab : pf = f } and Obc = {f ∈ Oba : f p = f }. Then we shall have
a∼
= image(p) ⊕ image(1 − p).4
One very special property that the category B possesses is that for any two objects a

and b the space Oab of morphisms is canonically dual to Oba , by a pairing which factorizes

through the composition in either order. It is natural to call a category with this property
a Frobenius category, or perhaps a Calabi-Yau category.5 It is a strong restriction on the
4

A linear category in which idempotents split in this way is often called Karoubian.

5

The latter terminology comes from the case of coherent sheaves on a compact Kähler man-

ifold, where for two sheaves E and F the dual of the morphism space Ext(E; F ) is in general
Ext(F ; E ⊗ ω), where ω is the canonical bundle. This coincides with Ext(F ; E) only when ω is
trivial, i.e. in the Calabi-Yau case. We shall discuss this example further in §6.

12

<!-- page 14 -->
category: for example the category of finitely generated modules over a finite dimensional
algebra does not have the property unless the algebra is semisimple.
Example Probably the simplest example of an open and closed theory of the type we are
studying is one associated to a finite group G. The category B is the category of finite
dimensional complex representations M of G, and the trace θM : OM M = End(M ) → C
takes ψ : M → M to 1/|G| trace(ψ). The closed algebra C is the center of the group-

algebra C[G], which maps to each End(M ) in the obvious way. The trace θC : C → C takes
P
a central element
λg g of the group-algebra to λ1 /|G|.
In this example the partition function of the theory on a surface Σ with constrained

boundary circles C1 , . . . , Ck labelled M1 , . . . , Mk is the weighted sum over the isomorphism
classes of principal G-bundles P on Σ of
χM1 (hP (C1 )) . . . χMk (hP (Ck )),
where χM : G → C is the character of a representation M , and hP (C) denotes the holonomy
of P around a boundary circle C. Each bundle P is weighted by the reciprocal of the order
of its group of automorphisms.
Returning to the general theory, we can now ask three basic questions.
(i) If we are given a “closed” TFT, can we enlarge it to an open and closed theory,
and, if so, is the enlargement unique?
(ii) If we are given the category B of boundary conditions of an open and closed theory,

together with the linear maps θa : Oaa → C which define the Frobenius structure, can we
reconstruct the whole theory, i.e. can we find the closed Frobenius algebra C?
(iii) Is an arbitrary Frobenius category the category of boundary conditions for some
closed theory?
For the first question to be well-posed, we should assume that the category of boundary

conditions is maximal, in the sense that if B′ is an enlargement of it then any object of
B′ is isomorphic to an object of B. Even so, we shall see that there are subtleties which
prevent any of these question from having a simple affirmative answer.
13

<!-- page 15 -->
2.6. Generalizations
We can obtain many interesting generalizations of the above structure by modifying
either the geometrical or the linear category.
The most general target category we can consider is a symmetric tensor category:
clearly we need a tensor product, and the axiom HY ⊔Y ∼
= HY ⊗ HY only makes sense if
1

2

1

2

there is an involutory canonical isomorphism HY1 ⊗ HY2 ∼
= HY2 ⊗ HY1

A very common choice in physics is the category of super vector spaces, i.e. vector
spaces V with a mod 2 grading V = V 0 ⊕ V 1 , where the canonical isomorphism V ⊗ W ∼
=
W ⊗ V is v ⊗ w 7→ (−1)deg v deg w w ⊗ v. One can also consider the category of ZZ-graded
vector spaces, with the same sign convention for the tensor product.

In either case the closed string algebra is a graded-commutative algebra C with a

trace θ : C → C. In principle the trace should have degree zero, but in fact the commonly

encountered theories have a grading anomaly which makes the trace have degree −n for
some integer n.6 The formulae (2.5), (2.9), and (2.11) must be replaced by their gradedcommutative analogues. In particular if we choose a basis ψµ and its dual ψ µ so that
θC (ψ µ ψ ν ) = δ µν

(2.18)

X

(2.19)

then
πb a (ψ) =

(−1)deg ψµ deg ψ ψµ ψψ µ

µ

We can also obtain interesting structures by changing the geometrical category of
manifolds and cobordisms by equipping them with extra stucture.
Example 1

We define topological-spin theories by replacing “manifolds” with “manifolds

with spin-structure.”
A spin structure on a surface means a double covering of its space of non-zero tangent
vectors which is non-trivial on each individual tangent space. On an oriented 1-dimensional
manifold S it means a double covering of the space of positively-oriented tangent vectors.
For purposes of gluing it is useful to note that this is the same thing as a spin structure
on a ribbon neighbourhood of S in an orientable surface. Each spin structure has an
6

It is easy to see that, up to an overall translation of the grading, the most general anomaly

assigns an operator of degree 21 n(i − o − χ) to a cobordism with Euler number χ and i incoming
and o outgoing boundary circles.

14

<!-- page 16 -->
automorphism which interchanges its sheets, and this will induce an involution T on any
vector space which is naturally associated to a 1-manifold with spin structure, giving the
vector space a mod 2 grading by its ±1-eigenspaces. We define a topological-spin theory

as a functor from the cobordism category of manifolds with spin structures to the category
of super vector spaces with its graded tensor structure. The functor is required to take
disjoint unions to super tensor products, and we also require the automorphism of the spin
structure of a 1-manifold to induce the grading automorphism T = (−1)degree of the super
vector space. We shall see presently that this choice of the supersymmetry of the tensor
product rather than the naive symmetry which ignores the grading is forced on us by the
geometry of spin structures if we want to allow the possibility of a semisimple category of
1
boundary conditions. There are two non-isomorphic circles with spin structure: Sns
, with

the Möbius or “Neveu-Schwarz” structure, and Sr1 , with the trivial or “Ramond” structure. A topological-spin theory gives us state-spaces Cns , respectively Cr corresponding to
1
Sns
, Sr1 .

1
There are four annuli with spin structures, for, alongside the cylinders A+
ns,r = Sns,r ×

[0, 1] which induce the identity maps of Cns,r there are also cylinders A−
ns,r which connect

1
Sns,r
to itself while interchanging the sheets. These cylinders A−
ns,r induce the grading
− ∼
+
automorphism on the state spaces. But because A = A by an isomorphism which
ns

ns

is the identity on the boundary circles — the Dehn twist which “rotates one end of the
cylinder by 2π” — the grading on Cns must be purely even. The space Cr can have both
even and odd components. The situation is a little more complicated for “U-shaped”

cobordisms, i.e. cylinders with two incoming or two outgoing boundary circles. If the
1
boundaries are Sns
there is only one possibility, but if the boundaries are Sr1 there are

two, corresponding to Ans,r
− . The complication is that there seems no special reason to
prefer either of the spin structures as “positive”. We shall simply choose one — let us

call it P — with incoming boundary Sr1 ⊔ Sr1 , and use P to define a pairing Cr ⊗ Cr → C.

We then choose a preferred cobordism Q in the other direction so that when we sew its
right-hand outgoing Sr1 to the left-hand incoming one of P the resulting S-bend is the
“trivial” cylinder A+
r . We shall need to know, however, that the closed torus formed by
the composition P ◦ Q has an even spin structure. Note that Frobenius structure θ on C

restricts to 0 on Cr .

There is a unique spin structure on the pair-of-pants cobordism of fig.2 which restricts

1
to Sns
on each boundary circle, and it makes Cns into a commutative Frobenius algebra

1
in the usual way. If one incoming circle is Sns
and the other is Sr1 then the outgoing

15

<!-- page 17 -->
circle is Sr1 , and there are two possible spin structures, but the one obtained by removing
a disc from the cylinder A+
r is preferred: it makes Cr into a graded module over Cns . The

chosen U-shaped cobordism P , with two incoming circles Sr1 , can be punctured to give us
1
a pair of pants with an outgoing Sns
, and it induces a graded bilinear map Cr × Cr → Cns

which, composing with the trace on Cns , gives a non-degenerate inner product on Cr . At

this point the choice of symmetry of the tensor product becomes important. For the
diffeomorphism of the pair of pants which shows us in the usual case that the Frobenius
algebra is commutative, when we lift it to the spin structure, induces the identity on one
incoming circle but reverses the sheets over the other incoming circle, and this proves that
the cobordsism must have the same output when we change the input from S(φ1 ⊗ φ2 ) to

T (φ1 ) ⊗ φ2 , where T is the grading involution and S : Cr ⊗ Cr → Cr ⊗ Cr is the symmetry

of the tensor category. If we take S to be the identity, this shows that the product on
the graded vector space Cr is graded-symmetric with the usual sign; but if S is the graded

symmetry then we see that the product on Cr is symmetric in the naive sense. (We must

bear in mind here that if ψ1 and ψ2 do not have the same parity then their product is in

any case zero, as we have seen that C+ is purely even.)
There is an analogue for spin theories of the theorem which tells us that a twodimensional topological field theory “is” a commutative Frobenius algebra. It asserts that
a spin-topological theory “is” a Frobenius algebra C = (Cns ⊕ Cr , θC ) with the properties

just mentioned, and with the following additional property. Let {φk } be a basis for Cns ,

with dual basis {φk } such that θC (φk φm ) = δkm , and let βk and β k be similar dual bases
P
P
for Cr . Then the Euler elements χns :=
φk φk and χr =
βk β k are independent of the

choices of bases, and the condition we need on the algebra C is that χns = χr . In particular,

this condition implies that the vector spaces Cns and Cr have the same dimension. 7 In

fact, the Euler elements can be obtained from cutting a hole out of the torus. There are
actually four spin structures on the torus. The output state is necessarily in Cns . The

Euler elements for the three even spin structures are equal to χe = χns = χr . There is

in addition an Euler element χo corresponding to the odd spin structure, it is given by
P
χo = (−1)deg βk βk β k .
We shall omit the proof that the general spin theory is what we have just described,

but it is almost identical with the proof we shall give in the appendix of the theorem of
7

Thus, in a sense, the theory has “spacetime supersymmetry.”

16

<!-- page 18 -->
Turaev about G-equivariant theories in the simple case when the group G is ZZ/2. Indeed
a spin theory is very similar to — but not the same as — a ZZ/2-equivariant theory, which
is the structure obtained when the surfaces are equipped with principal ZZ/2-bundles (i.e.
double coverings) rather than spin structures. We shall discuss equivariant theories in §7.
(One difference is that in the equivariant case the ZZ/2 action is nontrivial in the sector C1

and trivial in Cg , precisely the opposite of what we have found in the spin case.) Comparing

with the equivariant theory, the surprising result that the product on Cr is naive-symmetric
can be understood as twisted-anticommutativity.

It seems reasonable to call a spin theory semisimple if the algebra Cns is semisimple,

i.e. is the algebra of functions on a finite set X. Then Cr is the space of sections of a
vector bundle E on X, and it follows from the condition χns = χr that the fibre at each

point must have dimension 1. Thus the whole structure is determined by the Frobenius
algebra Cns together with the binary choice of the grading of the fibre of the line bundle
E at each point.

We can now see that if we had used the graded symmetry in defining the tensor
category we should have forced the grading of Cr to be purely even. For on the odd part

the inner product would have had to be skew, and that is impossible on a 1-dimensional

space. And if both Cns and Cr are purely even then the theory is in fact completely
independent of the spin structures on the surfaces.

A concrete example of a two-dimensional topological-spin theory is given by C = C⊕Cη

where η 2 = 1 and η is odd. The Euler elements are χe = 1 and χo = −1. It follows that

the partition function of a closed surface with spin structure is ±1 according as the spin

structure is even or odd. (To prove this it is useful to compute the Arf invariant of the
quadratic refinement of the intersection product associated to the spin structure and to
note that it is multiplicative for adding handles.)
The most common theories defined on surfaces with spin structure are not topological:
they are 2-dimensional conformal field theories with N = 1 supersymmetry. The general

features of the structure are still as we have described, but it should be noticed that if
the theory is not topological one does not expect the grading on Cns to be purely even:

states can change sign on rotation by 2π. If a surface Σ has a conformal structure then a

double covering of the non-zero tangent vectors is the complement of the zero-section in a
two-dimensional real vector bundle L on Σ which is called the spin bundle. The covering
17

<!-- page 19 -->
map then extends to a symmetric pairing of vector bundles L ⊗ L → T Σ, which if we

regard L and T Σ as complex line bundles in the natural way, induces an isomorphism
L ⊗C L ∼
= T Σ. An N = 1 superconformal field theory is a conformal-spin theory with an
additional map
Γ(S; L) ⊗ HS,L → HS,L

(2.20)

(σ, ψ) 7→ Gσ ψ

(2.21)

such that Gσ is real-linear in the section σ of L and satisfies G2σ = Dσ2 , where Dσ2 is
the Virasoro action of the vector field σ 2 . Furthermore, when we have a cobordism (Σ, L)
from (S0 , L0 ) to (S1 , L1 ) and a holomorphic section σ of L which restricts to σi on Si we
have the intertwining property
Gσ1 ◦ UΣ,L = UΣ,L ◦ Gσ0 .
Example 2

(2.22)

We define topological-spinc theories, which model 2d theories with N = 2

supersymmetry, by replacing “manifolds” with “manifolds with spinc -structure”.

A spinc -structure on a surface with a conformal structure is a pair of holomorphic line
bundles L1 , L2 with an isomorphism L1 ⊗ L2 ∼
= T Σ of holomorphic line bundles. A spin
structure is the particular case when L1 = L2 . An N = 2 superconformal theory assigns
a vector space HS;L1 ,L2 to each 1-manifold S with spinc -structure, and an operator
US0 ;L1 ,L2 : HS0 ;L1 ,L2 → HS1 ;L1 ,L2

(2.23)

to each spinc -cobordism from S0 to S1 . To explain the rest of the structure we need to define
the N = 2 Lie superalgebra associated to a spinc 1-manifold (S; L1 , L2 ). Let G = Aut(L1 )
denote the group of bundle isomorphisms L1 → L1 which cover diffeomorphisms of S.

(We can identify this group with Aut(L2 ).) Its Lie algebra Lie(G) is an extension of
Vect(S) by Ω0 (S). Let Λ0S;L1 ,L2 denote the complex Lie algebra obtained from Lie(G)
by complexifying Vect(S). This is the even part of a Lie superalgebra whose odd part is
Λ1S;L1 ,L2 = Γ(L1 ) ⊕ Γ(L2 ). The bracket Λ1 ⊗ Λ1 → Λ0 is completely determined by the
property that elements of Γ(L1 ) and of Γ(L2 ) anticommute among themselves, while the
composite
Γ(L1 ) ⊗ Γ(L2 ) → Λ1 → VectC (S)
takes (λ1 , λ2 ) to λ1 λ2 ∈ Γ(T S).
18

(2.24)

<!-- page 20 -->
In an N = 2 theory we require the superalgebra Λ(S; L1 , L2 ) to act on the vector

space HS;L1 ,L2 , compatibly with the action of the group G, and with a similar intertwining

property with the cobordism operators to that of the N = 1 case. For an N = 2 theory
the state space always has an action of the circle group coming from its embedding in G

as the group of fibrewise multiplications on L1 and L2 . Equivalently, the state space is
always ZZ-graded.
An N = 2 theory always gives rise to two ordinary conformal field theories by equip-

ping a surface Σ with the spinc structures (C, T Σ) and (T Σ,C). These are called the

“A-model” and the “B-model” associated to the N = 2 theory. In each case the state

spaces are cochain complexes in which the differential is the action of the constant section
1 of the trivial component of the spinc -structure.

Cochain level theories
The most important “generalization,” however, of the open and closed topological
field theory we have described is the one of which it is intended to be a toy model. In
closed string theory the central object is the vector space C = CS 1 of states of a single

parametrized string. This has an integer grading by the “ghost number”, and an operator
Q : C → C called the “BRST operator” which raises the ghost number by 1 and satisfies

Q2 = 0. In other words, C is a cochain complex. If we think of the string as moving

in a space-time M then C is roughly the space of differential forms defined along the

orbits of the action of the reparametrization group Diff+ (S 1 ) on the free loop space LM .
(More precisely, square-integrable forms of semi-infinite degree.) Similarly, the space C

of a topologically-twisted N = 2 supersymmetric theory, as just described, is a cochain

complex which models the space of semi-infinite differential forms on the loop space of
a Kähler manifold — in this case, all square-integrable differential forms, not just those
along the orbits of Diff+ (S 1 ). In both kinds of example, a cobordism Σ from p circles to q
circles gives an operator UΣ,µ : C ⊗p → C ⊗q which depends on a conformal structure µ on

Σ. This operator is a cochain map, but its crucial feature is that changing the conformal

structure µ on Σ changes the operator UΣ,µ only by a cochain-homotopy. The cohomology
H(C) = ker(Q)/im(Q) — the “space of physical states” in conventional string theory — is
therefore the state space of a topological field theory. (In the usual string theory situation
the topological field theory we obtain is not very interesting, for the BRST cohomology is
concentrated in one or two degrees, and there is a “grading anomaly” which means that
19

<!-- page 21 -->
the operator associated to a cobordism Σ changes the degree by a multiple of the Euler
number χ(Σ). In the case of the N = 2 supersymmetric models, however, there is no
grading anomaly, and the full structure is visible.)
A good way to describe how the operator UΣ,µ varies with µ is as follows.
If MΣ is the moduli space of conformal structures on the cobordism Σ, modulo dif-

feomorphisms of Σ which are the identity on the boundary circles, then we have a cochain
map
UΣ : C ⊗p → Ω(MΣ ; C ⊗q )

(2.25)

where the right-hand side is the de Rham complex of forms on MΣ with values in C ⊗q .

The operator UΣ,µ is obtained from UΣ by restricting from MΣ to {µ}. The composition

property when two cobordisms Σ1 and Σ2 are concatenated is that the diagram
C ⊗p
↓

Ω(MΣ2 ◦Σ1 ; C

Ω(MΣ1 ; C ⊗q )
↓
⊗r
−→ Ω(MΣ1 × MΣ2 ; C ) = Ω(MΣ1 ; Ω(MΣ2 ; C ⊗r ))

−→
⊗r

)

(2.26)

commutes, where the lower horizontal arrow in induced by the map MΣ1 ×MΣ2 → MΣ2 ◦Σ1
which expresses concatenation of the conformal structures.

Many variants of this formulation are possible. For example, we might prefer to give
a cochain map
UΣ : C.(MΣ ) → (C ⊗p )∗ ⊗ C ⊗q ,

(2.27)

where C.(MΣ ) is, say, the complex of smooth singular chains of MΣ . We may also prefer

to use the moduli spaces of Riemannian structures instead of conformal structures.

There is no difficulty in passing from the closed-string picture just presented to an
open and closed theory. We shall not discuss these cochain-level theories in any depth in
this work, but it is important to realize that they are the real objective. We shall now
point out a few basic things about them. A much fuller discussion can be found in Costello
[25].
For each pair a, b of boundary conditions we shall still have a vector space — indeed
a cochain complex — Oab , but it is no longer the space of morphisms from b to a in a

category. Rather, what we have is, in the terminology of Fukaya, Kontsevich, and others,

an A∞ -category. This means that instead of a composition law Oab × Obc → Oac we
20

<!-- page 22 -->
have a family of ways of composing, parametrized by the contractible space of conformal
structures on the surface of fig. 1. In particular, any two choices of a composition law from
the family are cochain-homotopic. Composition is associative in the sense that we have a
contractible family of triple compositions Oab × Obc × Ocd → Oad , which contains all the
maps obtained by choosing a binary composition law from the given family and bracketing
the triple in either of the two possible ways.
Note This is not the usual way of defining an A∞ -structure. According to Stasheff’s
original definition, an A∞ -structure on a space X consists of a sequence of choices: first,
a composition law m2 : X × X → X; then, a choice of a map
m3 : [0, 1] × X × X × X → X
which is a homotopy between (x, y, z) 7→ m2 (m2 (x, y), z) and (x, y, z) 7→ m2 (x, m2 (y, z));
then, a choice of a map

m4 : C2 × X 4 → X,
where C2 is a convex plane polygon whose vertices are indexed by the five ways of bracketing
a 4-fold product, and m4 |((∂C2 ) × X 4 ) is determined by m3 ; and so on.

There is an analogous definition — in fact slightly simpler — applying to cochain

complexes rather than spaces. These definitions, however, are essentially equivalent to the
one above coming from 2-dimensional field theory: the only important point is to have a
contractible family of k-fold compositions for each k. (A discussion of the relation between
the definitions can be found in [26].)
Apart from the composition law, the essential algebraic properties we have found in
our theories are the non-degenerate inner product, and the commutativity of the closed
algebra C. Concerning the latter, when we pass to cochain theories the multiplication in

C will of course be commutative up to cochain homotopy, but, unlike what happened with

the open-string composition, the moduli space MΣ of closed-string multiplications, i.e.
the moduli space of conformal structures on a pair of pants Σ, modulo diffeomorphisms

of Σ which are the identity on the boundary circles, is not contractible: it contains a
natural circle of multiplications, and there are two different natural homotopies between
the multiplication and the reversed multiplication. This might be a clue to an important
difference between stringy and classical space-times. The closed string cochain complex C

is the string-theory substitute for the de Rham complex of space-time, an algebra whose
21

<!-- page 23 -->
multiplication is associative and (graded-)commutative on the nose. Over the rationals or
the real or complex numbers, such cochain algebras are known by the work of Sullivan [27]
and Quillen [28] to model8 the category of topological spaces up to homotopy, in the sense
that to each such algebra C we can associate a space XC and a homomorphism of cochain
algebras from C to the de Rham complex of XC which is a cochain homotopy equivalence.
If we do not want to ignore torsion in the homology of spaces we can no longer encode
the homotopy type in a strictly commutative cochain algebra. Instead, we must replace
commutative algebras with so-called E∞ -algebras, i.e., roughly, cochain complexes C over
the integers equipped with a multiplication which is associative and commutative up to
given arbitrarily high-order homotopies. An arbitrary space X has an E∞ -algebra CX of
cochains, and conversely one can associate a space XC to each E∞ -algebra C. Thus we have
a pair of adjoint functors, just as in rational homotopy theory. A long evolution in algebraic
topology has culminated in recent theorems of Mandell [29] which show that the actual
homotopy category of topological spaces is more or less equivalent to the category of E∞ algebras. The cochain algebras of closed string theory have less higher commutativity than
do E∞ -algebras, and this may be an indication that we are dealing with non-commutative
spaces in Connes’s sense: that fits in well with the interpretation of the B-field of a string
background as corresponding to a bundle of matrix algebras on space-time. At the same
time, the nondegenerate inner product on C — corresponding to Poincaré duality — seems
to show we are concerned with manifolds, rather than more singular spaces.
For readers not accustomed to working with cochain complexes it may be worth saying
a few words about what one gains by doing so. To take the simplest example, let us consider
the category K of cochain complexes of finitely generated free abelian groups and cochainhomotopy classes of cochain maps. This is called the derived category of the category of
finitely generated abelian groups. Passing to cohomology gives us a functor from K to the
category of ZZ-graded finitely generated abelian groups. In fact the subcategory K0 of K
consisting of complexes whose cohomology vanishes except in degree 0 is actually equivalent
8

In this and the following sentence we are overlooking subtleties related to the fundamental

group.

22

<!-- page 24 -->
to the category of finitely generated abelian groups.9 But the category K inherits from the
category of finitely generated free abelian groups a duality functor with properties as ideal
as one could wish: each object is isomorphic to its double dual, and dualizing preserves
exact sequences. (The dual C ∗ of a complex C is defined by (C ∗ )i = Hom(C −i ; ZZ).) There
is no such nice duality in the category of finitely generated abelian groups. Indeed, the
subcategory K0 is not closed under duality, for the dual of the complex CA corresponding

to a group A has in general two non-vanishing cohomology groups: Hom(A; ZZ) in degree
0, and in degree +1 the finite group Ext(A; ZZ) Pontrjagin-dual to the torsion subgroup of
A. This follows from the exact sequence (not to be confused with the cochain complex):
0 → Hom(A, ZZ) → Hom(FA , ZZ) → Hom(RA , ZZ) → Ext(A, ZZ) → 0

(2.28)

The category K also has a tensor product with better properties than the tensor

product of abelian groups (which does not preserve exact sequences), and, better still,
there is a canonical cochain functor from (locally well-behaved) compact spaces to K which

takes Cartesian products to tensor products. (The simplicial, Čech, and other candidates

for the cochain complex of a space are canonically isomorphic in K.)
We shall return to this discussion in §6.

3. Solutions of the algebraic conditions: the semisimple case
3.1. Classification theorem
We now turn to the question : given a closed string theory C, what is the corresponding

category of boundary conditions? In our formulation this becomes the question: given a
commutative Frobenius algebra C, what are the possible Oab ’s?
9

To an abelian group A one can associate the cochain complex
CA = ( · · · → 0 → RA → FA → 0 → · · · ),

where FA is a free abelian group (in degree 0) with a surjective map FA → A, and RA is the
kernel of FA → A. The choice of FA is far from unique, but nevertheless the different choices of
CA are canonically isomorphic objects of K.

23

<!-- page 25 -->
We can answer this question in the case when C is semisimple. We will take C to be

an algebra over the complex numbers, and in this case the most useful characterization of
semisimplicity is that the “fusion rules”
φµ φν = Nµνλ φλ

(3.1)

are diagonalizable.10 That is, the matrices L(φµ ) of the left-regular representation, with
matrix elements Nµνλ , are simultaneously diagonalizable.
Equivalently, there is a set of basic idempotents εx such that
C = ⊕xCεx
εx εy = δxy εy

(3.2)

Equivalently, yet again, C is the algebra of complex-valued functions on the finite set

X = Spec(C) of characters of C.

The trace θC : C → C, which should be thought of as a “dilaton field” on the finite

space-time Spec(C), is completely described by the unordered set of non-zero complex
numbers
θx := θC (εx )

(3.3)

which is the only invariant of a finite dimensional commutative semisimple Frobenius
algebra.
It should be mentioned that the most general finite dimensional commutative algebra
over the complex numbers is of the form C = ⊕Cx , where x runs through the set Spec(C),

and Cx is a local ring, i.e. Cx = Cεx ⊕ mx , with εx as in (3.2) , and mx a nilpotent ideal. If

C is a Frobenius algebra, then so is each Cx , and there is some νx for which θC : mνxx → C
is an isomorphism, while mνxx +1 = 0. Let us write ωx ∈ mνxx for the element such that

θC (ωx ) = 1. The element ω of C with components ωx can be regarded as a “volume form”

on space-time. (A typical example of such a local Frobenius algebra Cx is the cohomology

ring — with complex coefficients — of complex projective space IPn of dimension n. The

cohomology ring is generated by a single 2-dimensional class t which satisfies tn+1 = 0.
The trace is given by integration over IPn , and takes tk to 1 if k = n, and to 0 otherwise.
Thus ωx = tn here.)
10

The structure constants Nµνλ need not be integral, though in many interesting examples there

is a basis for the algebra in which they are integral.

24

<!-- page 26 -->
A useful technical fact about Frobenius algebras — not necessarily commutative —
P
is that, in the notation of (2.11) , the “Euler” element χ =
ψµ ψ µ is invertible if and

only if the algebra is semisimple 11 , which in the general case means that the algebra is
isomorphic to a sum of full matrix algebras. The element χ always belongs to the centre
of the algebra; in the commutative case it has components dim(Cx )ωx .
In the semisimple case we have the following complete characterization of the possible
open algebras Oaa compatible with a fixed closed algebra C. Unfortunately, though, the
arguments we use do not work for graded Frobenius algebras.

Theorem 2: If C is semisimple then O = Oaa is semisimple for each a and necessarily of

the form O = EndC (W ) for some finite dimensional representation W of C.

Proof: The images ιa (εx ) = Px are central simple idempotents. Therefore Ox =
Px O = Px OPx is an algebra over the Frobenius algebra Cx = εx C ∼
= C, and so it suffices

to work over a single space-time point. Then ιa (1Ox ) = α1Cx for some element α ∈ C. By
the Cardy condition

α1Ox = χOx =

X

ψµ ψ µ

(3.4)

Applying θ we find α = dim Ox , and hence χOx is invertible if Ox 6= 0. It follows that

Ox is semisimple at each point x, i.e. a sum of matrix algebras ⊕i End(Wi ). In fact, the

Cardy condition shows that there can be at most one summand Wi at each point, i.e. the
algebra is simple. For the map π : Ox → Ox must take each summand End(Wi ) into itself,
and cannot factor through the 1-dimensional Cx if more than one Wi is non-zero. ♠

According to Theorem 2 the most general Oaa is obtained by choosing a vector space

Wx,a for each basic idempotent εx , i.e. a vector bundle on the finite space-time X =
Spec(C), and forming:
Oaa = ⊕x End(Wx,a ).
11

(3.5)

To see this, one observes that for any element ψ of the algebra we have θ(ψχ) = tr(ψ), where

tr(ψ) denotes the trace of ψ in the regular representation. As the pairing (ψ1 , ψ2 ) 7→ θ(ψ1 ψ2 ) is
nondegenerate, it follows that the trace-form (ψ1 , ψ2 ) 7→ tr(ψ1 ψ2 ) is nondegenerate if and only if
χ is invertible, and non-degeneracy of the trace-form is well-known to be a criterion for a finite
dimensional algebra to be semisimple. There are several definitions of semisimplicity, and their
equivalence amounts to the classical theorem of Wedderburn. For our purposes, a semisimple
algebra is just a sum of full matrix algebras.

25

<!-- page 27 -->
But let us notice that when we have an algebra of the form End(W ) the vector space W
is determined by the algebra only up to tensoring with an arbitrary complex line: any
irreducible representation of the algebra will do for W .
Elements ψ ∈ Oaa will be denoted ψ = ⊕ψx . Let Px be the projection operator onto

the xth summand. From the equation

ιa (εx ) = Px

(3.6)

the adjoint relation and the Cardy condition determine the relations:
θa (ψ) =

Xp
θx Tr(ψx )
x

εx
ι (ψ) = ⊕x Tr(ψx ) √
θx
1
πb a (ψaa ) = ⊕x √ TrWx,a (ψx,aa )Px,b
θx
a

(3.7)

ε

(one must use the same square-root in the formula for θO and ιa .) Note that θC ( √εθx √y ) =
x

θy

δx,y , i.e. the elements √εθx form a natural orthonormal basis for C. Thus, a boundary
x

condition a gives us a tuple of positive integers wx = dim Wx , one for each basic idempotent,
√
as well as a choice of the square-root θx . The relation (2.5), however, shows that these

square-roots are an intrinsic property of the Frobenius category B, and do not depend on

which particular object in it we are considering.

Let us now determine the Oaa × Obb bimodules Oab associated to a pair of boundary

conditions a, b. These are again fixed by the Cardy condition.
Lemma: When C is semisimple we have
Oab ∼
= ⊕x Hom(Wx,a ; Wx,b )

(3.8)

Proof: Restricting to each Oaa we can invoke Theorem 2. Then the ιa (εx )Oab = Oab ιb (εx )

are bimodules for the simple algebras Ox,aa and Ox,bb . We restrict to a single idempotent

and drop the x, that is, we take C = C. The only irreducible representation of Oaa =
End(Wa ) is Wa itself, and the only Oaa × Obb -bimodule is W ∗ ⊗ Wb . Therefore, Oab ∼
=
a
∗
nab Wa ⊗ Wb , where nab is a nonnegative integer. Let us work out the Cardy condition. If
∗
vm is a basis for Wa and wn is a basis for Wb then a basis for Oab is vm,α
⊗ wn,α where
α = 1, . . . , nab . Then π(ψ) = nab trWa (ψ)Pb . Comparing to ιb ιa (ψ) we get nab = 1. ♠

26

<!-- page 28 -->
We can now describe the maximal category B of boundary conditions. We first observe

that if p ∈ Oaa is a projection —i.e. p2 = p —we can assume that a = b ⊕ c in B, where

b is the image of p. For we can adjoin images of projections to any additive category in
much the same way as we adjoined direct sums. If the closed algebra C is semisimple we

can therefore choose an object ax of B for each space-time point x so that ax is supported
at x — i.e. ιax (εx )Oax ax = Oax ax — and is simple, i.e. Oax ax = C. For any object b of B
we then have a canonical morphism

⊕x Obax ⊗ ax → b,

(3.9)

where on the left we have used the possibility of tensoring any object of a linear category
by a finite dimensional vector space. Furthermore, it follows from the lemma that the
morphism (3.9) is an isomorphism, for both sides have the same space of morphisms into
any other object c. Finally, notice that ax is unique up to tensoring with a line Lx , for if
a′ is another choice then a′ ∼
= ax ⊗ Lx , where Lx = Oa a′ .
x

x

x x

Theorem 3
(i) If C is semisimple, corresponding to a space-time X, then the category B of boundary
conditions is equivalent to the category Vect(X) of vector bundles on X, by the inverse

functors
{Wx } 7→ ⊕Wx ⊗ ax ,

(3.10)

a 7→ {Oax a }.

(3.11)

(ii) The equivalence of B with Vect(X) is unique up to transformations Vect(X) →
Vect(X) given by tensoring with a line bundle L = {Lx } on X.

√
(iii) The Frobenius structure on B is determined by choosing a square-root { θ x } of the
dilaton field. It is therefore unique up to multiplication by an element σ ∈ C such
that σ 2 = 1.

Remarks
1. A boundary condition a has a support
supp(a) = {x ∈ X : Wx 6= 0}
27

(3.12)

<!-- page 29 -->
contained in X = spec(C). If two boundary conditions a and b have the same support
then Oab is a Morita equivalence bimodule between Oaa and Obb . The reader might

wish to compare this discussion to section 6.4 of [30]. Note that it is necessary to
invoke the Cardy condition to draw this conclusion.
2. Examples of semisimple Frobenius algebras in physics include:
a) The fusion rule algebra (Verlinde algebra) of a RCFT.
b) The chiral ring of an N = 2 Landau-Ginzburg theory for generic superpotential W

(that is, as long as all the critical points of W are Morse critical points). This is the case
when the IR theory is massive.
c) Generic quantum cohomology of manifolds.
3.2. Comment on B-fields
We can see from this discussion just where the idea of a B-field would appear, though
in fact on a 0-dimensional space-time any B-field must be trivial. We showed that there
is a category of boundary conditions associated to each point of space time, and that it
is isomorphic to the category of finite dimensional vector spaces, though not canonically.
More precisely, it contains minimal — i.e. irreducible — objects from which any other
object can be obtained by tensoring with a finite dimensional vector space.
Now a B-field is in essence a bundle of categories on space-time in which the fibrecategories are all isomorphic but not canonically. We can suppose that each fibre is isomorphic to the category of finite dimensional vector spaces. The crucial feature is that
the ambiguity in identifying each fibre with the standard fibre is a “group” — in this case
actually a category — of equivalences whose elements are complex lines and in which composition is given by the tensor product. Our category of boundary conditions is precisely
the category of “sections” of a bundle of categories with this structural group.
It may be helpful to think of this in the following way. An electromagnetic field is a
line bundle with connection on space-time. It is something we can think of as part of the
structure of space-time, and makes sense in the absence of fermions. But in a theory with
fermions there is a spinor-space at each point of space-time, and the electromagnetic field
is “really” the information about how the spinor spaces are connected together from point
to point of space-time. In this sense the electromagmetic field “is” the spinor-bundle with
its connection. A B-field similarly “is” the bundle of boundary conditions.
On a general topological space X the classes of B-fields are classified by the elements
of the cohomology group H 3 (X; ZZ), which can be understood as H 1 (X; G), where G is the
28

<!-- page 30 -->
“group” of line bundles under tensor product, which in algebraic topology is an EilenbergMaclane object of type K(ZZ, 2). We shall return to this topic in §7.
3.3. Reconstructing the closed algebra
When we have an open and closed TFT each element ξ of the closed algebra C defines

an endomorphism ξa = ia (ξ) ∈ Oaa of each object a of B, and η ◦ ξa = ξb ◦ η for each

morphism η ∈ Oba from a to b. The family {ξa } thus constitutes a natural transformation
from the identity functor 1B : B → B to itself.

For any C-linear category B we can consider the ring E of natural transformations of

1B . It is automatically commutative, for if {ξa }, {ηa } ∈ E then ξa ◦ ηa = ηa ◦ ξa by the
definition of naturality. If B is a Frobenius category then there is a map πa b : Obb → Oaa

for each pair of objects a, b, and we can define j b : Obb → E by j b (η)a = πa b (η) for η ∈ Obb .

In other words, j b is defined so that the Cardy condition ιa ◦ j b = πa b holds. But the

question arises whether we can define a trace θ : E → C to make E into a Frobenius algebra,
and with the property that

θa (ιa (ξ).η) = θ(ξ.j a(η))

(3.13)

for all ξ ∈ E and η ∈ Oaa . This is certainly true if B is a semisimple Frobenius category

with finitely many simple objects, for then E is just the ring of complex-valued functions

on the set of classes of these simple elements, and we can readily define θ : E → C

by θ(εa ) = θa (1a )2 , where a is an irreducible object, and εa ∈ E is the characteristic

function of the point a in the spectrum of E. Nevertheless, a Frobenius category need not

be semisimple, and we cannot, unfortunately, take E as the closed string algebra in the
general case. If, for example, B has just one object a, and Oaa is a commutative local
ring of dimension greater than 1, then E = Oaa , and so ιa : E → Oaa is an isomorphism,

and its adjoint map j a ought to be an isomorphism too. But that contradicts the Cardy
P
condition, as πa a is multiplication by ψi ψ i , which must be nilpotent. In §6 we shall give

an example of two distinct closed string Frobenius algebras which admit the same open
string algebra Oaa .

The commutative algebra E of natural endomorphisms of the identity functor of a

linear category B is called the Hochschild cohomology HH 0 (B) of B in degree 0. The

groups HH p (B) for p > 0, whose definition will be given in a moment, vanish if B is

semisimple, but in the general case they appear to be relevant to the construction of a
closed string algebra from B. Let us notice meanwhile that for any Frobenius category B

there is a natural homomorphism K(B) → HH 0 (B) from the Grothendieck group12 of B,
12

I.e. the group formed from the semigroup of isomorphism classes of objects of B under ⊕.

29

<!-- page 31 -->
which assigns to an object a the transformation whose value on b is πb a (1a ) ∈ Obb . In the
semisimple case this homomorphism induces an isomorphism K(B) ⊗ C → HH 0 (B).

For any additive category B the Hochschild cohomology is defined as the cohomology
of the cochain complex in which a k-cochain F is a rule that to each composable k-tuple
of morphisms
φ1

φ2

φk

Y0 → Y1 → · · · → Yk

(3.14)

assigns F (φ1 , . . . , φk ) ∈ Hom(Y0 ; Yk ). The differential in the complex is defined by
(dF )(φ1 , . . . , φk+1 ) =F (φ2 , . . . , φk+1 ) ◦ φ1 +
+

k
X
i=1

(−1)i F (φ1 , . . . , φi+1 ◦ φi , . . . , φk+1 )

(3.15)

+ (−1)k+1 φk+1 ◦ F (φ1 , . . . , φk ).
(Notice, in particular, that a 0-cochain assigns an endomorphism FY to each object Y , and
is a cocycle if the endomorphisms form a natural transformation. Similarly, a 2-cochain
F gives a possible infinitesimal deformation F (φ1 , φ2 ) of the composition-law (φ1 , φ2 ) 7→
φ2 ◦ φ1 of the category, and the deformation preserves the associativity of composition if
and only if F is a cocycle.)
In the case of a category B with a single object whose algebra of endomorphisms is O
the cohomology just described is usually called the Hochschild cohomology of the algebra
O with coefficients in O regarded as a O-bimodule. This must be carefully distinguished

from the Hochschild cohomology with coefficients in the dual O-bimodule O∗ . But if O is a
Frobenius algebra it is isomorphic as a bimodule to O∗ , and the two notions of Hochschild

cohomology need not be distinguished. The same applies to a Frobenius category B:
because Hom(Yk ; Y0 ) is the dual space of Hom(Y0 ; Yk ) we can think of a k-cochain as a
rule which associates to each composable k-tuple (3.14) of morphisms a linear function of
an element φ0 ∈ Hom(Yk ; Y0 ). In other words, a k-cochain is a rule which to each “circle”
of k + 1 morphisms
φ0

φ1

φ2

φk

φ0

· · · → Y0 → Y1 → · · · → Yk → · · ·
assigns a complex number F (φ0 , φ1 , . . . , φk ).
30

(3.16)

<!-- page 32 -->
Fig. 13: A cyclic pairing of a closed string state φ with k + 1 open string states.

If in this description we restrict ourselves to cochains which are cyclically invariant under rotating the circle of morphisms (φ0 , φ1 , . . . , φk ) then we obtain a sub-cochain-complex
of the Hochschild complex whose cohomology is called the cyclic cohomology HC ∗ (B) of
the category B. The cyclic cohomology — which evidently maps to the Hochschild coho-

mology — is a more natural candidate for the closed string algebra associated to B than

is the Hochschild cohomology (for a state represented by the vector (3.16) pairs in a cycli-

cally invariant way with a closed string state to give a number, in virtue of fig. 13). In our
baby examples the cyclic and Hochschild cohomology are indistinguishable, but it is worth
pointing out13 that while HH 2 (B) is, as indicated above, the space of infinitesimal deformations of B as a category, the group HC 2 (B) is its space of infinitesimal deformations as
a Frobenius category.

A very natural Frobenius category on which to test these ideas is the category of
holomorphic vector bundles on a compact Calabi-Yau manifold: that example will be
discussed in §6.
3.4. Spin theories and mod 2 graded categories
Let us give a brief outline, without proofs, of the modifications of the preceding discussion which are needed to describe the category of boundary conditions for a topological-spin
theory as defined in §2.6.

There is just one spin structure on an interval, and its automorphism group is (±1),

so for each pair of boundary conditions a, b the vector space Oab will have an involution,
i.e. a mod 2 grading. The bilinear composition Oab ⊗ Obc → Oac will preserve the grading.

There is a non-degenerate trace θa : Oaa → C which satisfies the commutativity condition

(2.5) (without signs).
13

As we learnt from Kontsevich

31

<!-- page 33 -->
If the closed theory is described by a Frobenius algebra C = Cns ⊕ Cr , as in §2.6, there

will be adjoint maps

ιns
a : Cns → Oaa
ιans : Oaa → Cns
ιra : Cr → Oaa

(3.17)

ιar : Caa → Cr
r
which preserve the grading. Moreover and ιns
a and ιa fit together to define a homomorphism

of algebras C → Oaa . The centrality condition becomes
ns
ιns
a (φ)ψ = ψιa (φ)

ιra (φ)ψ = (−1)deg φ deg ψ+deg ψ ψιra (φ)

(3.18)

Thus, ιns maps into the naive center of the algebra Oaa . The reason we get the naive

centre here, rather than the graded-algebra centre, and also the reason that the trace is
naively commutative, is the same as that given in §2.6 for the naive commutativity of the
algebra C. The sign for ιr is obtained by carefully following the choices of sections of the

spin bundle one chooses under the diffeomorphism in figure 8.
There are two Cardy conditions
b
a
ιns
a ιns (ψ) = πb (ψ) :=

ιra ιbr (ψ) = π̃ba (ψ) :=

X

X

(−1)deg ψµ deg ψ ψµ ψψ µ
(−1)deg ψµ (deg ψ+1) ψµ ψψ µ .

(3.19)

If we assume the closed algebra is semisimple then, just as before, we can assume that
Cns is the algebra of functions on a finite set X, and we can determine the category of
boundary conditions point-by-point. In other words, we can assume that C = C[η], where

the generator η of Cr satisfies η 2 = 1, but may have either even or odd degree. In either

case, the argument we have already used shows (by means of the first Cardy formula) that
the algebra Oaa is the full matrix algebra of a vector space W . If the degree of η is even

then ιr (η) = P with P even, P 2 = 1, and P ψP = (−1)deg ψ ψ. In this case the category

of boundary conditions at the point is equivalent to the category of mod 2 graded vector
spaces. If, on the other hand, the degree of η is odd, then P is odd, P 2 = 1 and P is (naive)
central. The involution of the algebra Oaa corresponds to an involution of the module W ,
and the action of P is an isomorphism between the two halves of the grading. The even

subalgebra of Oaa is a full matrix algebra. Thus the category of boundary conditions is
32

<!-- page 34 -->
the equivalent to the category of graded representations of the superalgebra C[η], which
in turn is equivalent simply to the category of ungraded vector spaces. The Frobenius
structure of the open algebra determines that of the closed algebra by taking the square,
as in the ungraded case. The two cases deg η = 0 and deg η = 1 are roughly analogous
to the distinction between the even and odd degree Clifford algebras over the complex
numbers.

Suppose, conversely, that we have an arbitrary semisimple mod 2 graded category
B, i.e. a linear category equipped with an involutory functor S which one thinks of as
the flip of the grading. Such a category has two kinds of simple object P : those such
that S(P ) ∼
= P , and those for which this is not true. The first kind of object generates a
subcategory of B isomorphic to the category of vector spaces, and the second kind generates
a subcategory isomorphic to the category of graded vector spaces. Thus any semisimple
graded category B is the category of boundary conditions for a unique topological-spin
theory.

4. Vector bundles, K-theory, and “boundary states”
In the semisimple case there is a nice geometrical interpretation of the category B
of boundary conditions: the possible objects correspond to the vector bundles over the
“space-time” X = Spec(C) associated to C, which is just a finite set of points. The fiber
above a point x is just the vector space Wx .

Fig. 14: Correlations on the upper half plane with boundary condition a are the
same as the closed string amplitude for an insertion of a boundary state Ba .

33

<!-- page 35 -->
Let us now make some comments on “boundary states”. In the conformal field theory
literature one associates to a boundary condition a a corresponding “state” Ba in the
closed string state space. (Strictly, Ba is an element of the algebraic dual.) Translated
to the present context Ba ∈ C. The defining property of the boundary state is that the
correlation functions of operators on a disk with the boundary condition a are equal to the
correlation functions of the closed theory on the sphere obtained by capping off the disk
with another disk and inserting the state Ba at the centre of the cap. This is illustrated
in fig. 14.
In equations,


θa (ιa φ1 ) · · · ιa (φn ) = θC Ba φ1 · · · φn

(4.1)

for all φ1 , . . . , φn . Using the adjoint relation and nondegeneracy of the trace we find that
Ba = ιa (1Oaa )

(4.2)

The map a 7→ Ba is a natural homomorphism
K(B) → C.

(4.3)

P
The operator which adds g handles and h =
ha holes, where ha of the holes have
Q
g
ha
the boundary condition a, is just χ
(Ba ) , where χ is the Euler element of C.
Let us record one simple property of these boundary states. First, using the Cardy

condition we have
θC (Ba Bb ) = θa (ιa (Bb ))
= θa (ιa ιb (1b ))
= θa (πa b (1b ))

(4.4)

= dim Oab
In the semisimple case we can give an explicit formula for the the “boundary state”
in terms of the basic idempotents:
BO = ι∗ (1O ) =

εx
(dim Wx ) √
θx
x

X

(4.5)

The formula shows that the boundary states form a positive cone in the unimodular
lattice LB spanned by the orthonormal basis √εθx in the closed algebra C. In particular it
x

follows from (4.5) that boundary states can only be added with positive integral coefficients.
34

<!-- page 36 -->
They are therefore not like quantum mechanical states of branes. The fundamental integral
structure is a result of the Cardy condition.
It is natural to speculate whether there should be an operation of “multiplication” of
boundary conditions. There are arguments both for and against. The original perspective
on D-branes, according to which they are viewed as “cycles” in space-time on which open
strings can begin and end, suggests that there should be a multiplication, corresponding to
the intersection of cycles. As no multiplication seems to emerge from the toy structure we
have developed in this paper one may wonder whether an important ingredient has been
omitted. Against this there are the following considerations. Our boundary conditions
seem to correspond more closely to vector bundles — i.e. to K-theory classes — on
space-time than to homology cycles: that will be plainer when we consider the equivariant
situation in §7. Now the K-theory classes of a ring have a product, coming from the tensor

product of modules, only when the ring is commutative; and we have already remarked
that the B-fields which are part of the closed string model of space-time seem to encode a
degree of noncommutativity. More precisely, D-branes seem to define classes in the twisted
K-theory of space-time, twisted by the B-field, and the twisted K-theory of a space does
not form a ring: the product of two twisted classes is a twisted class corresponding to the
sum of the twistings of the factors. But in string theory there is no concept of “turning off”
the B-field to find an underlying untwisted space-time. For example, the conformal field
theory corresponding to a torus with a non-zero B-field can be isomorphic by “T-duality”
to a theory coming from another torus with no B-field.
Another reason for not expecting a multiplication operation on D-branes also comes
from T-duality in conformal field theory. There the closed string theories defined by a
Riemannian torus T and its dual T ∗ are isomorphic, and we do indeed have a K-theory
isomorphism K(T ) ∼
= K(T ∗ ), but it is not compatible with the multiplication in K-theory.
Furthermore, in some examples of TFTs coming from N = 2 supersymmetric sigma models
the category of boundary conditions does seem to be a tensor category.
The formula (4.5) for the boundary state shows that the lattice LB , which is picked

out inside C by the dilaton field θ, is not closed under multiplication in C unless θx = 1
for all points x; but the lattices corresponding to different dilaton fields multiply into each

other just as happens with twisted K-classes. Nevertheless, in the semisimple case, if we
P √
define an element S := x θx εx , then the operation
(B1 , B2 ) 7→ SB1 B2

does define a multiplication on boundary states, though its significance is unclear.
35

(4.6)

<!-- page 37 -->
4.1. “Cardy states” vs. “Ishibashi states”
The formula (4.5) for the boundary state is reminiscent of what is what is known as a
“Cardy state” in the construction of conformal field theories with boundary. That leaves
the question: what are the “Ishibashi” or “character states”? This question can be nicely
addressed in the topological framework of this exposition. In the basis of primary fields in
closed (or chiral) conformal field theory the fusion rules are in general not diagonal. Thus
the usual basis φµ , µ = 1, . . . , N for C is different from the basis εi , i = 1, . . . , N used
above. The fusion rules are diagonal in the basis εi .
The analogy with CFT is the following. In boundary conformal field theory one
associates an “Ishibashi” or character state to every primary field of the chiral algebra.
Formally these states are solutions to (T − T̄ )|Bi = 0, or the generalization of this to
the case of other chiral algebras. They are best thought of as intertwiners between left
and right chiral representations. In the present context there is no chiral algebra, and we
should think of every element of C as a solution to (T − T̄ ) = 0, and its generalizations.
The basis of “Ishibashi states” associated to definite representations of the chiral
algebra is naturally associated to the basis φµ analogous to primary fields. In this basis
the algebra is given by
φµ φν = Nµνλ φλ

(4.7)

with positive integral Nµνλ . Using these formulae we recover, essentially, Cardy’s formula
for Cardy boundary states in terms of character boundary states. Note that there is no
need to use any relation to the modular group.
We close with one further brief remark. It is nice to see the standard relation that
the closed string coupling is the square of the open string coupling in the present context.
P
If we scale θC → λ−2 θC then χC = µ φµ φµ → λ+2 χC . We may therefore interpret λ2

as the closed string couplling. On the other hand, the squareroot of θi in BO shows that

BO → λBO , and therefore λ is the open string coupling. Indeed, the partition function
for a surface with g handles and h holes is Z(Σ) = θC ((χC )g (BO )h ), and therefore scales
as Z(Σ) → λ−χ(Σ) Z(Σ), as expected, where χ(Σ) = 2 − 2g − h is the Euler number of Σ..
36

<!-- page 38 -->
5. Landau-Ginzburg theories
D-branes can be defined in general two-dimensional N=2 Landau-Ginzburg theories
[31]. Such theories can be topologically twisted, producing topological Landau-Ginzburg
theories. It is interesting to compare with the D-branes obtained from our results applied
to the resulting closed topological theory. Here we confine ourselves to a few very elementary remarks. In the past few years, following an initial suggestion by Kontsevich, an
elaborate theory of categories of topological Landau-Ginzburg branes has been developed.
We refer to [32,33,34,35,36,37,38] for details. These categories are thought to capture more
physical information about the D-branes. In the case when all the critical points of the
superpotential are Morse there is a functor to the category of branes we construct.
Let us recall the definition of a topological LG theory. One begins with a superpotential W (Xi ) which is a holomorphic function of chiral superfields Xi . When W is a
polynomial the Frobenius algebra is simply the Jacobian ideal
C = C[Xi ]/(∂i W )

(5.1)

The Frobenius structure is defined by a residue formula. For example, in the one-variable
case we define
θ(φ) := ResX=∞

φ(X)
W ′ (X)

(5.2)

If the critical points of W are all Morse critical points then the algebra (5.1) is semisimple. Physically Morse critical points correspond to massive theories, while non-Morse
critical points renormalize to nontrivial 2d CFT’s in the infrared.
If all the critical points are Morse then the trace is easily written in terms of the
critical points pa as
θ(φ) = +

X

dW (pa )=0

φ(pa )
det(∂i ∂j W |pa )

(5.3)

In the semisimple one-variable case we can construct the basic idempotents as follows.
Let
dW =

n
Y

α=1

(X − rα )

(5.4)

where we assume all the roots are distinct. Then it is easy to check that
εβ :=

Y (X − rα )
(rβ − rα )

α:α6=β

37

(5.5)

<!-- page 39 -->
are basic idempotents. (To prove this, write (X − rα ) = (X − rβ ) + (rβ − rα )).
Example: W = 13 t3 − qt. For n = 2 we can explicitly write
√

q+t
√
2 q
√
q−t
ε2 = √
2 q

ε1 =

(5.6)

√
√
Note that θ1 = 1/(2 q) and θ2 = −1/(2 q).

Then from the general result above one finds O = End(W1 ) ⊕ End(W2 ) and
1
1
θO (Ψ) = √ Tr(Ψ1 ) + √ Tr(Ψ2 )
θ1
θ2
p
p
ι∗ (Ψ) = θ1 Tr(Ψ1 )ε1 + θ2 Tr(Ψ2 )ε2

(5.7)

Thus, the general boundary state is
ε2
ε1
B = w1 √ + w2 √
θ1
θ2

(5.8)

where w1 , w2 are integers. Note the interesting monodromy as q → e2πi q. Branes of type
(w1 , w2 ) map to branes of type (w2 , −w1 ).

Clearly, there will be similar phenomena for general Landau-Ginzburg theories. The

space of superpotentials W has a codimension one “discriminant locus” where it has nonMorse critical points. Analytic continuation around this locus will permute the εi , but will
√
only permute the θi up to sign. One may understand in this elementary way some of the
brane permutation/creation phenomena discussed in numerous places in the literature.
The “vector bundles on spacetime” that we have found can be taken quite literally in
the context of the theory of strings moving in less than one dimension which was worked
out in 1988-1991. (For a reviews [39][40][41]. ) Strings moving in a spacetime of n disjoint
points can be modelled by matrix chains or by topological field theory. The latter point
of view is described in, for example, [40][41]. In the latter point of view, one considers
topological gravity coupled to topological matter. For n spacetime points the topological
matter can be taken to be the N = 2 Landau-Ginzburg theories associated to W given by
the unfolding of An singularities:
xn+1
W =
+ a n xn + · · · + a 0
n+1
38

(5.9)

<!-- page 40 -->
For generic W we find vector bundles on n spacetime points. This is of course what we
expect for the branes in such spacetimes!
It is worth mentioning that in these simplest of string theories (the “minimal string
theories”) considerable progress has been made in recent years in understanding the full
spectrum of D-branes, going beyond the topological field theory truncation. See [42] for a
review.

6. Going beyond semisimple Frobenius algebras
The examples of topological field theories coming from N = 2 conformal field theories
— Landau-Ginzburg models and the quantum cohomology rings of Calabi-Yau manifolds
— suggest that it is of interest to understand the possible solutions of the algebraic conditions in the case when C is not semisimple. In this section we shall make some partial

progress with this problem, and shall also explain how it should perhaps be viewed in a
wider context.
6.1. Examples related to the cohomology of manifolds

A natural example of a graded commutative Frobenius algebra is the cohomology with
complex coefficients of a compact oriented manifold X. Thus, for C we can take the algebra
R
C = H ∗ (X;C) with trace θ(φ) = X φ. What are the corresponding O’s?

A natural guess, which turns out to be wrong, but for interesting reasons, is that we

should take O = C ⊗ MatN (C) = MatN (C) for some N > 0, together with
θO (ψ) =

Z

Tr(ψ)

(6.1)

X

While O is indeed a Frobenius algebra, the only natural candidate for the map ι∗ is ι∗ (φ) =

φ ⊗ 1N . However, this fails to satisfy the Cardy condition: one computes ι∗ (ψ) = Tr(ψ)
from the adjoint relation, and hence ι∗ ι∗ (ψ) = Trψ ⊗ 1N . On the other hand, one also
finds

π(ψ) =

X

i

(−1)deg ωi (deg ψ+deg ω ) ωi ⊗ elm ∧ ψ ∧ ω i ⊗ eml

= χ(T X) ∧ Tr ψ

(6.2)

Here ωi is a basis for H ∗ (X;C), eml are matrix units, and χ(T X) ∈ H top (X;C) is the

Euler class of T X. The map π annihilates forms of positive degree, and cannot agree with
ι∗ ι∗ .
39

<!-- page 41 -->
This example can be modified to give an open and closed theory by taking O to be

associated with a submanifold of X. This is, after all, the standard picture of D-branes!

Let us work in the algebraic category of ZZ-graded vector spaces, and continue to take
C = H ∗ (X;C), with X a compact connected oriented n-dimensional manifold, and the
R
trace θC (φ) = X φ of degree −n as above. Let us look for an open algebra of the form

O = MatN (O0 ), with O0 commutative. Then O0 is a Frobenius algebra, and we may as
well assume that it is H ∗ (Y ;C) for some compact oriented manifold14 Y of dimension m,

and that ι : C → O0 is f ∗ for some map f : Y → X.

Thus O = H ∗ (Y ;C) ⊗ M atN (C) with open string trace
θO (Ψ) = θo

Z

Tr(Ψ)

(6.3)

Y

of degree −m, where θo is a constant. This is a non-commutative Frobenius algebra.
By the adjoint relation ι∗ is then determined to be
ι∗ (Ψ) = θo f∗ (Tr(Ψ))

(6.4)

where f∗ is the adjoint of the ring homomorphism f ∗ : H ∗ (X) → H ∗ (Y ) with respect to

Poincaré duality. Thus ι∗ has degree n − m. On the other hand , one sees at once that

π : O → O has degree m, so if the Cardy condition is to hold we must have n = 2m. If

that is true, then we can assume, by making a small generic perturbation of f , that f is
an immersion of Y in X. We can now make the the adjoint map f∗ more explicit:
f∗ (ψ) = π ∗ (ψ) ∧ ΦN ,

(6.5)

where π : N → Y is the projection of the normal bundle (identified with a tubular

neighborhood of Y in X) and ΦN is the Thom class of the bundle, compactly supported

in the tubular neighborhood, which represents the cohomology class of Y in X. One easily
finds that
ι∗ ι∗ (Ψ) = θo χ(N Y ) ∧ Tr(Ψ) ⊗ 1.

(6.6)

where χ(N Y ) is the Euler class of the normal bundle of Y ֒→ X, i.e. the homological
self-intersection of Y in X.
14

In fact we need to allow Y to have orbifold singularities to ensure this.

40

<!-- page 42 -->
On the other hand,
π(Ψ) =

1
Tr(Ψ)χ(T Y )
θo

(6.7)

where χ(T Y ) ∈ H top (Y ;C) is the Euler class of the tangent bundle T Y , whose integral is

the Euler number of Y .

Evidently the Cardy conditions are satisfied if we choose θo so that χ(T Y ) = θo2 χ(N Y ).
This is always possible if χ(N Y ), which is the self-intersection number of Y in X, is nonzero, and also possible if Y is a Lagrangian submanifold of a symplectic manifold X, for
then N ∼
= T Y . The boundary state is B = θo N ΦN .

One immediate consequence of this discussion is that if we start, say, with O =

H ∗ (CP 2 ) as our open algebra we can easily find two different closed algebras compatible
with it, by regarding Y as a submanifold either of X = CP 4 or of X ′ = IHP 2 .

Unfortunately we do not know how to describe the category of boundary conditions
for C = H ∗ (X). But it seems likely, in any case, that to get a significant result one would

have to consider the theory on the cochain level. We next turn our attention to that case.
6.2. The Chas-Sullivan theory
There is an interesting example — due to Chas and Sullivan [43]— on the cochain
level of a structure a little weaker than that of our open and closed theories which may

illuminate the use of cochain theories. Let us start with a compact oriented manifold X,
which we shall take to be connected and simply connected. We can define a category B

whose objects are the oriented submanifolds of X, and whose vector space of morphisms
from Y to Z is OY Z = Ext∗H ∗ (X) (H ∗ (Y ); H ∗ (Z)) — the cohomology, as usual, has complex

coefficients, and H ∗ (Y ) and H ∗ (Z) are regarded as H ∗ (X)-modules by restriction. The

composition of morphisms is given by the Yoneda composition of Ext groups. With this
definition, however, it will not be true that OY Z is dual to OZY . (To see this it is enough

to consider Ext0 = Hom, when, say, Y = X and Z is a point.)

We can do better by defining a cochain complex ÔY Z of “morphisms” by
ÔY Z = BΩ(X) (Ω(Y ); Ω(Z)),

(6.8)

where Ω(X) denotes the usual de Rham complex of a manifold X, and BA (B; C), for a

differential graded algebra A and differential graded modules B and C, is the usual cobar

resolution
Hom(B; C) → Hom(A ⊗ B; C) → Hom(A ⊗ A ⊗ B; C) → . . . ,
41

(6.9)

<!-- page 43 -->
(in which the differential is given by
df (a1 ⊗ . . . ⊗ ak ⊗ b) = a1 f (a2 ⊗ . . . ⊗ ak ⊗ b)+
X
+
(−1)i f (a1 ⊗ . . . ⊗ ai ai+1 ⊗ . . . ⊗ ak ⊗ b)+

(6.10)

+(−1)k f (a1 ⊗ . . . ⊗ ak−1 ⊗ ak b) )

whose cohomology is ExtA (B; C). This is different from OY Z = Ext∗H ∗ (X) (H ∗ (Y ); H ∗ (Z)),

but related to it by a spectral sequence whose E2 -term is OY Z and which converges to

H ∗ (ÔY Z ) = ExtΩ(X) (Ω(Y ); Ω(Z)). But more important is that H ∗ (ÔY Z ) is the homology
of the space PY Z of paths in X which begin in Y and end in Z. To be precise, H p (ÔY Z ) ∼
=
Hp+dZ (PY Z ), where dZ is the dimension of Z. On the cochain complexes the Yoneda

composition is associative up to cochain homotopy, and defines a structure of an A∞ -

category B̂. The corresponding composition of homology groups

Hi (PY Z ) × Hj (PZW ) → Hi+j−dZ (PY W )

(6.11)

is the composition of the Gysin map associated to the inclusion of the codimension dZ
submanifold M of pairs of composable paths in the product PY Z × PZW with the con-

catenation map M → PY W .

Let us try to fit a “closed string” cochain algebra C to this A∞ category. The algebra

of endomorphisms of the identity functor of B, denoted E in §3, is easily seen to be just the

cohomology algebra H ∗ (X). We have mentioned in Section 2 that this is the Hochschild
cohomology HH 0 (B).
The definition of Hochschild cohomology for a linear category B was given at the end

of §3. In fact the definition of the Hochschild complex makes sense for an A∞ category

such as B̂, and it is one candidate for the closed algebra C.

In the present situation C is equivalent to the usual Hochschild complex of the dif-

ferential graded algebra Ω(X), whose cohomology is the homology of the free loop space

LX with its degrees shifted downwards15 by the dimension dX of X, so that the coho-

mology H i (C) is potentially non-zero for −dX ≤ i < ∞. This algebra was introduced by

Chas and Sullivan in precisely the present context — they were trying to reproduce the
structures of string theory in the setting of classical algebraic topology. There is a map
H i (X) → H −i (C) which embeds the ordinary cohomology ring of X in the Chas-Sullivan
15

Thus the identity element of the algebra, in H 0 (C), is the fundamental class of X, regarded

as an element of Hn (LX) by thinking of the points of X as point loops in LX.

42

<!-- page 44 -->
ring, and there is also a ring homorphism H i (C) → Hi (L0 X) to the Pontrjagin ring of the

based loop space L0 X, based at any chosen point in X.

The other candidate for C mentioned in Section 2 was the cyclic cohomology of the

algebra Ω(X), which is well-known [44] to be the equivariant homology of the free loop
space LX with respect to its natural circle-action. This may be an improvement on the
non-equivariant homology.

The structure we have arrived at is, however, not a cochain-level open and closed
theory, as we have no trace maps inducing inner products on H ∗ (ÔY Z ). When one tries to
define operators corresponding to cobordisms it turns out to be possible only when each

connected component of the cobordism has non-empty outgoing boundary. (A theory defined on this smaller category is often called a non-compact theory.) The nearest theory in
our sense to the Chas-Sullivan one is the so-called “A-model” defined for a symplectic manifold X. There the A∞ category is the Fukaya category, whose objects are the Lagrangian

submanifolds of X equipped with bundles with connection, and the cochain complex of
morphisms from Y to Z is the Floer complex which calculates the “semi-infinite” cohomology of the path space PY Z . In good cases the cohomology of this Floer complex has
a vector space basis indexed by the points of intersection of Y and Z, and the cohomol-

ogy of the corresponding closed complex is just the ordinary cohomology of X. From our
perspective the essential feature of the Floer theory is that it satisfies Poincaré duality for
the infinite dimensional manifold LX.
6.3. Remarks on the B-model
Let X be a complex variety of complex dimension d with a trivialization of its canonical
bundle. That is, we assume there is a nowhere-vanishing holomorphic d-form Ω. The Bmodel [45] is a ZZ-graded topological field theory arising from the N=2 supersymmetric σmodel of X. The natural boundary conditions for the theory are provided by holomorphic
vector bundles on X.
The category of holomorphic vector bundles is not a Frobenius category. There is,
however, a very natural ZZ-graded Frobenius category associated to X: the category VX

whose objects are the vector bundles on X, but whose space of morphisms from E to F is
OEF = Ext∗X (E; F ) = H 0,∗ (X; E ∗ ⊗ F ).
The trace θE : OEE → C, of degree −d, is defined by
Z
θE (Ψ) =
Tr(Ψ) ∧ Ω.
X

43

(6.12)

(6.13)

<!-- page 45 -->
This is nondegenerate by Serre duality, but the category is still not semisimple — in fact
the non-vanishing of groups Exti for i > 0 precisely expresses the non-semisimplicity of
the category. (For a non-zero element of Ext1X (E; F ) corresponds to an exact sequence
0 → F → G → E → 0 which does not split, i.e. to a vector bundle G with a subbundle F
with no complementary bundle.)

What are the endomorphisms of the identity functor of VX ? Multiplication by any

element of H 0,∗ (X) clearly defines such an endomorphism. A holomorphic vector field

ξ on X also defines an endomorphism of degree 1, for any bundle E has an “Atiyah
∗
class”16 aE ∈ Ext1 (E; E ⊗ TX
) — its curvature — which we can contract with ξ to give

eξ = ιξ aE ∈ Ext1 (E; E). More generally, a class
η∈H

0,q

(X;

p
^

q

TX ) = Ext (

p
^

∗
TX
;C)

∗ ⊗p
can be contracted with (aE )p ∈ Extp (E; E ⊗ (TX
) ) to give

eη = ιη (aE )p ∈ Extp+q (E; E).
V∗
Now Witten has shown in [45] that H 0,∗ (X;
TX ) is indeed the closed string algebra of the

B-model. To understand this in our context we must once again pass to the cochain-level
theory of which the Ext groups are the cohomology. A good way to do this is to replace

a holomorphic vector bundle E by its ∂-complex Ê = Ω0,∗ (X; E), which is a differential
graded module for the differential graded algebra A = Ω0,∗ (X). Then we define ÔEF

as the cochain complex HomA (Ê; F̂ ), whose cohomology groups are Ext∗X (E; F ). If we
are going to do this, it is natural to allow a larger class of objects, namely all finitely
generated projective differential graded A-modules. Any coherent sheaf E on X defines
such a module: one first resolves E by a complex E ∗ of vector bundles, and then takes the
total complex of the double complex Ê ∗ . The resulting enlarged category is essentially the
bounded derived category of the category of coherent sheaves on X. In this setting, we find
without difficulty that the endomorphisms of the identity morphism are given, just as in
the topological example above, by the Hochschild complex
Cˆ = {A → A ⊗ A → A ⊗ A ⊗ A → . . . },
V∗
whose cohomology is H ∗ (X;
TX ). There is still, however, work to do to understand
ˆ and the adjoint maps ιE and ιE . We feel that this has not yet been
the trace maps on C,
properly elucidated in the literature. For some progress on this question see [46][47].
16

∗
→ J 1 E → E, where J 1 E is the bundle of
Corresponding to the extension of bundles E ⊗ TX
1-jets of holomorphic sections of E.

44

<!-- page 46 -->
7. Equivariant 2-dimensional topological open and closed theory
An important construction in string theory is the “orbifold” construction. Abstractly,
this can be carried out whenever the closed string background has a group G of automorphisms. There are two steps in defining an orbifold theory. First, one must extend the
theory by introducing “external” gauge fields, which are G-bundles (with connection) on
the world-sheets. Next, one must construct a new theory by summing over all possible
G-bundles (and connections).
We begin by describing carefully the first step in forming the orbifold theory. The
second step — summing over the G-bundles — is then very easy in the case of a finite
group G.
7.1. Equivariant closed theories
Let us begin with some general remarks. In d-dimensional topological field theory
one begins with a category S whose objects are oriented (d − 1)-manifolds and whose

morphisms are oriented cobordisms. Physicists say that a theory admits a group G as a
global symmetry group if G acts on the vector space associated to each (d−1)-manifold, and
the linear operator associated to each cobordism is a G-equivariant map. When we have
such a “global” symmetry group G we can ask whether the symmetry can be “gauged”, i.e.
whether elements of G can be applied “independently” — in some sense — at each point
of space-time. Mathematically the process of “gauging” has a very elegant description:
it amounts to extending the field theory functor from the category S to the category

SG whose objects are (d − 1)-manifolds equipped with a principal G bundle, and whose

morphisms are cobordisms with a G-bundle.17 We regard S as a subcategory of SG by

equipping each (d − 1)-manifold S with the trivial G-bundle S × G. In SG the group of

automorphisms of the trivial bundle S × G contains G, and so in a gauged theory G acts

on the state space H(S): this should be the original “global” action of G. But the gauged

theory has a state space H(S, P ) for each G-bundle P on S: if P is non-trivial one calls
H(S, P ) a “twisted sector” of the theory. In the case d = 2, when S = S 1 we have the

bundle Pg → S 1 obtained by attaching the ends of [0, 2π] × G via multiplication by g.

Any bundle is isomorphic to one of these, and Pg is isomorphic to Pg ′ if and only if g ′

is conjugate to g. But note that the state space depends on the bundle and not just its
17

We are assuming here that the group G is discrete: if G is a Lie group we should define SG

as the category of manifolds equipped with a principal G-bundle with a connection.

45

<!-- page 47 -->
isomorphism class, so we have a twisted sector state space Cg = H(S, Pg ) labelled by a
group element g rather than by a conjugacy class.

We shall call a theory defined on the category SG a G-equivariant TFT. It is important

to distinguish the equivariant theory from the corresponding “gauged theory,” described

below. In physics, the equivariant theory is obtained by coupling to nondynamical background gauge fields, while the gauged theory is obtained by “summing” over those gauge
fields in the path integral.
An alternative and equivalent viewpoint which is especially useful in the twodimensional case is that SG is the category whose objects are oriented (d − 1)-manifolds

S equipped with a map p : S → BG, where BG is the classifying space of G. In this view-

point we have a bundle over the space Map(S, BG) whose fiber at p is Hp . To say that Hp

depends only on the G-bundle p∗ BG on S pulled back from the universal G-bundle EG
on BG by p is the same as to say that the bundle on Map(S, BG) is equipped with a flat
connection allowing us to identify the fibres at points in the same connected component by
parallel transport; for the set of bundle isomorphisms p∗0 EG → p∗1 EG is the same as the
set of homotopy classes of paths from p0 to p1 . When S = S 1 the connected components
of the space of maps correspond to the conjugacy classes in G: each bundle Pg corresponds
to a specific point pg in the mapping space, and a group-element h defines a specific path
from pg to phgh−1 .
The second viewpoint makes clear that G-equivariant topological field theories are
examples of “homotopy topological field theories” in the sense of Turaev [48]. We shall
use his two main results: first, an attractive generalization of the theorem that a twodimensional TFT “is” a commutative Frobenius algebra, and, secondly, a classification of
the ways of gauging a given global G-symmetry of a semisimple TFT. We shall now briefly
review his work .
A G-equivariant TFT gives us for each element g ∈ G a vector space Cg , associated

to the circle equipped with the bundle Pg whose holonomy is g. The usual pair-of-pants

cobordism, equipped with the evident G-bundle which restricts to Pg1 and Pg2 on the two
incoming circles, and to Pg1 g2 on the outgoing circle, induces a product
Cg1 ⊗ Cg2 → Cg1 g2
making C := ⊕g∈G Cg into a G-graded algebra.
46

(7.1)

<!-- page 48 -->
Fig. 15: Definition of the product in the G-equivariant closed theory. The heavy
dot is the basepoint on S 1 . To specify the morphism unambiguously we must
indicate consistent holonomies along a set of curves whose complement consists of
simply connected pieces. This means that the product is not commutative. We
need to fix a convention for holonomies of a composition of curves, i.e. whether we
are using left or right path-ordering. We will take h(γ1 ◦ γ2 ) = h(γ1 ) · h(γ2 ).

Fig. 16: (a) The action of αh on a state φ ∈ Cg . This can also be represented by
the cylinder as in (b).

As in the usual case there is a trace θ : C1 → C defined by the disk diagram with

one ingoing circle. Note that the holonomy around the boundary of the disk must be 1.
Making the standard assumption that the cylinder corresponds to the unit operator we
obtain a nondegenerate pairing Cg ⊗ Cg −1 → C.
A new element in the equivariant theory is that G acts as an automorphism group on
C. That is, there is a a homomorphism α : G → Aut(C) such that
αh : Cg → Chgh−1 .

(7.2)

Diagramatically, αh is defined by the surface in fig. 16.
Now let us note some properties of α. First, if φ ∈ Ch then αh (φ) = φ. The reason

for this is explained in fig. 17.

47

<!-- page 49 -->
Fig. 17: If the holonomy along path P2 is h then the holonomy along path P1
is 1. However, a Dehn twist around the inner circle maps P1 into P2 . Therefore,
αh (φ) = α1 (φ) = φ, if φ ∈ Ch .

Fig. 18: Demonstrating twisted centrality.

Fig. 19: Deforming the LHS of (a) into a spacetime evolution diagram yields (b),
whose value is TrCh (Lψ αg ). Similarly deforming the RHS of (a) gives a diagram
whose value is TrCg−1 (Rψ αh ).

Next, while C is not commutative, it is “twisted-commutative” in the following sense.
If φ1 ∈ Cg1 and φ2 ∈ Cg2 then
αg2 (φ1 )φ2 = φ2 φ1 .
48

(7.3)

<!-- page 50 -->
The necessity of this condition is illustrated in fig. 18.
The last property we need is a little more complicated. The trace of the identity map
of Cg is the partition function of the theory on a torus with the bundle with holonomy

(g, 1). Cutting the torus the other way, we see that this is the trace of αg on C1 . Similarly,

by considering the torus with a bundle with holonomy (g, h), where g and h are two
commuting elements of G, we see that the trace of αg on Ch is the trace of αh on Cg −1 .

But we need a strengthening of this property. Even when g and h do not commute we can
form a bundle with holonomy (g, h) on a torus with one hole, around which the holonomy
will be c = hgh−1 g −1 . We can cut this torus along either of its generating circles to get
a cobordism operator from Cc ⊗ Ch to Ch or from Cg −1 ⊗ Cc to Cg −1 . If ψ ∈ Chgh−1 g −1 let

us introduce two linear transformations Lψ , Rψ associated to left- and right-multiplication

by ψ. On the one hand, Lψ αg : φ 7→ ψαg (φ) is a map Ch → Ch . On the other hand

Rψ αh : φ 7→ αh (φ)ψ is a map Cg −1 → Cg −1 . The last sewing condition states that these

two endomorphisms must have equal traces:




TrCh Lψ αg = TrCg−1 Rψ αh .

(7.4)

The reason for this can be deduced by pondering the diagram in fig. 19.

Fig. 20: A simpler axiom than Turaev’s torus axiom.

The equation ((7.4)) was taken by Turaev as one of his axioms. It can, however,
be reexpressed in a way that we shall find more convenient. Let ∆g ∈ Cg ⊗ Cg −1 be

the “duality” element corresponding to the identity cobordism of (S 1 , Pg ) with both ends
P
regarded as outgoing. We have ∆g =
ξi ⊗ ξ i , where ξi and ξ i run through dual bases of
Cg and Cg −1 . Let us also write

∆h =

X

ηi ⊗ η i ∈ Ch ⊗ Ch−1 .
49

<!-- page 51 -->
Then ((7.4)) is easily seen to be equivalent to
X

X

αh (ξi )ξ i =

ηi αg (η i ),

(7.5)

in which both sides are elements of Chgh−1 g −1 . This equation is illustrated by the isomorphic

cobordisms of fig. 20.

In summary, the sewing theorem for G-equivariant 2d topological field theories is given
by the following theorem:
Theorem 4 ([48]) To give a 2d G-equivariant topological field theory is to give a G-graded
algebra C = ⊕g Cg together with a group homomorphism α : G → Aut(C) such that

1. There is a G-invariant trace θ : C1 → C which induces a nondegenerate pairing Cg ⊗
Cg −1 → C.

2. The restriction of αh to Ch is the identity.
3. For all φ ∈ Cg , φ′ ∈ Ch , αh (φ)φ′ = φ′ φ.
4. For all g, h ∈ G we have
X
where ∆g =

P

αh (ξi )ξ i =

X

ηi αg (η i ) ∈ Chgh−1 g −1 ,

ξi ⊗ ξ i ∈ Cg ⊗ Cg −1 and ∆h =

P

(7.6)

ηi ⊗ η i ∈ Ch ⊗ Ch−1 as above.

Remarks:
1. We will give a proof of the sewing theorem in the appendix.
2. Warning: Turaev calls the above a crossed G Frobenius algebra, but it is not a crossedproduct algebra in the sense of C ∗ algebras (see below). We will refer to an algebra
satisfying the conditions of the theorem as a Turaev algebra.
3. Axioms 1 and 3 have counterparts in the non-equivariant theory, but axioms 2 and 4
are new elements.
7.2. The orbifold theory
Before going any further, let us describe how we obtain the orbifold theory from the
Turaev algebra.
Let us return to the general discussion at the beginning of §7.1, where we outlined the

definition of an equivariant theory. Roughly speaking, the gauged theory is obtained from
the equivariant theory by summing over the gauge fields. More precisely, the state-space
which a gauged theory associates to a (d − 1)-manifold S consists of “wave-functions” ψ
50

<!-- page 52 -->
which associate to each G-bundle P on S an element ψP of the state-space HS,P of the
equivariant theory. The map ψ must be “natural” in the sense that when θ : P → P ′ is

a bundle isomorphism the induced isomorphism HS,P → HS,P ′ takes ψP to ψP ′ . This is
often referred to as the “Gauss law.” In the two-dimensional case, the Gauss law amounts

to saying that the state-space Corb for the circle is the G-invariant part of the Turaev
algebra C = ⊕Cg . In other words,

Corb = ⊕{Cg }Zg ,

(7.7)

where now g runs through a set of representatives for the conjugacy classes in G, and we
take the invariant part of Cg under the centralizer Zg of g in G. The algebra Corb is not a

graded algebra if G is non-abelian. One must check that the product in Corb is simply the
restriction of the product in C. The trace Corb → C is the restriction of the trace C → C

which is the given trace on C1 and is zero on Cg when g 6= 1. Then Corb is a commutative

Frobenius algebra which encodes the orbifold theory.

7.3. Solutions of the closed string G-equivariant sewing conditions
Having found the sewing conditions in the G-equivariant case we can ask what examples there are of the structure. The Frobenius algebra C1 with its G-action corresponds

to a topological field theory with a global G-symmetry. In the case when C1 is a semisim-

ple Frobenius algebra — and therefore the algebra of functions on a finite G-set X —

Turaev finds a nice answer: ways of gauging the symmetry, i.e. of extending C1 to a Tu-

raev algebra, correspond to equivariant B-fields on X, i.e. to equivariant 2-cocycles of X

with values in C× , and two such B-fields define isomorphic Turaev algebras if and only if
they represent the same class in H 2 (X;C× ) ∼
= H 3 (X; ZZ). We now review this result and
G

G

take the opportunity to introduce a more geometric picture of Turaev’s algebra C (in the
semisimple case). We shall first recall some very general constructions.
7.3.1.General constructions
Whenever a group G acts on a set X we can form a category X//G, whose objects
are the points x of X, and whose morphisms x0 → x1 are
Hom(x0 , x1 ) := {g ∈ G : gx0 = x1 }.
51

(7.8)

<!-- page 53 -->
Fig. 21: An oriented two-simplex ∆x,g1 ,g2 in the space |X//G|.

Fig. 22: An oriented 3-simplex in |X//G|.

Next, for any category C, one can form the space of the category, denoted |C|. This

is an oriented simplicial complex whose p-simplexes are in 1-1 correspondence with the
composable p-tuples of morphisms in the category. To be specific, the vertices are the
objects of the category. The edges are the morphisms. Triples of morphisms (f1 , f2 , f3 )

with f3 = f2 ◦ f1 correspond to 2-simplices, and so forth. In the present case, when we

form the simplicial complex |X//G| the 2-simplices are the triples (g1 , g2 , x) illustrated in
fig. 21. Three-simplices are shown in fig. 22, etc.

The space |X//G| is a model for (X × EG)/G. Hence the (cellular) cohomology of

∗
(X;C× ).
this space H ∗ (|X//G|;C× ) is the equivariant cohomology HG

Another object which we can associate to any category C is its algebra A(C) over the
52

<!-- page 54 -->
field C. This has a vector space basis {εf } indexed by the morphisms of C, and the product

is given by εf1 εf2 = εf1 ◦f2 when f1 and f2 are composable, and εf1 εf2 = 0 otherwise. For

the category X//G the algebra A(X//G) is the usual crossed-product algebra A(X) × G in
the sense of operator algebra theory, where A(X) is the algebra of complex-valued functions

on the set X. 18
The construction of the category-algebra A(C) can be generalized. A B-field on a
category C is a rule which associates a complex line Lf to each morphism f of C, and
associative isomorphisms
Lf1 ⊗ Lf2 → Lf1 ◦f2
to each pair (f1 , f2 ) of composable morphisms . In concrete terms, to give such a product
is to give a 2-cocycle on the space |C|. Indeed, choosing basis elements ℓf ∈ Lf , we must
have

ℓf1 · ℓf2 = b(f1 , f2 , f3 )ℓf3

(7.10)

where b(f1 , f2 , f3 ) ∈ C× defines a 2-cochain on |C|. (We choose values in C× rather than

C so the product is not degenerate.) Associativity of (7.10) holds iff b is a 2-cocycle. A

change of basis of the Lf modifies b by a coboundary. Hence the isomorphism classes of
B-fields on C are in 1-1 correspondence with cohomology classes [b] ∈ H 2 (|C|;C× ). When

we have a B-field b on C we can form a twisted category-algebra Ab (C), which as a vector
space is ⊕Lf , and where the multiplication is defined by means of the associative maps

Lf1 ⊗ Lf2 → Lf1 ◦f2 .

Applying the above construction to the category X//G, an associative product on the

2
lines Lg,x is the same thing as a 2-cocycle in HG
(X;C× ). In terms of the basis elements

ℓg,x for the lines Lg,x we shall write the multiplication
ℓg2 ,x2 ℓg1 ,x1 = bx1 (g2 , g1 )ℓg2 g1 ,x1
=0
18

if

x2 = g 1 x1
otherwise

(7.11)

For any commutative algebra A with G-action, A × G is spanned by elements a ⊗ g with

a ∈ A and g ∈ G, and the product is given by
(a1 ⊗ g1 )(a2 ⊗ g2 ) = a1 g1 (a2 ) ⊗ g1 g2 .

(7.9)

The isomorphism A(X//G) → A(X) × G takes εg,x to χgx ⊗ g, where χx is the characteristic
function supported at x.

53

<!-- page 55 -->
Here bx1 (g2 , g1 ) = b(∆x,g1 ,g2 ) is the value of the cocycle on the oriented 2-simplex of fig. 21.
Notice that if Gx is the isotropy group of some point x ∈ X then restricting (7.11) to

the elements ℓg,x with g ∈ Gx shows that bx defines an element of the group cohomology

H 2 (Gx ;C× ), corresponding to the central extension of Gx by C× whose elements are pairs
(g, λ) with g ∈ Gx and λ ∈ Lx − {0}. This central extension of the isotropy group Gx

does not in general extend to any central extension of the whole group G. It does so,
however, in the particular case when the B-field b is pulled back from a 2-cocycle of G
by the map X → (point), i.e. when bx (g2 , g1 ) is independent of x. In general the cocycle

b : G × G × X → C× can be regarded as a cocycle of the group G with values in the abelian

group A(X)× = Map(X;C× ) with its natural G-action. Thus it defines a (non-central)
extension
1 → A(X)× → G̃ → G → 1.

One technical point to notice is that for any B-field we have Lf = C canonically when
f is an identity morphism. Thus Lg,x = C when g = 1. We shall always choose ℓg,x = 1
when g = 1, thereby normalizing the cocycle so that bx (g1 , g2 ) = 1 if either g1 or g2 is 1.
The algebra Ab (X//G) = ⊕g∈G,x∈X Lg,x with the multiplication rule defined by (7.11)

can be identified with the twisted crossed-product algebra A(X) ×b G via
ℓg,x 7→ χgx ⊗ g,

where χx is the characteristic function supported at x. The twisted cross-product is defined
by
(f1 ⊗ g1 )(f2 ⊗ g2 ) = αg1 g2 (b(g1 , g2 ))f1 αg1 (f2 ) ⊗ g1 g2 ,

(7.12)

where b(g1 , g2 ) denotes the function x 7→ bx (g1 , g2 ) in A(X)× , and the group G acts on

A(X) in the natural way

αg (f )(x) = f (g −1 x),
so that g · χx = χgx .

If we wish to apply these considerations to the spin case described in sections 2.6 and

3.4 then we must consider the lines Lf to be ZZ/2 graded. In this case the theory will
admit a further twisting by H 1 (|C|; ZZ/2). However, we will not discuss this generalization
further.
54

<!-- page 56 -->
Fig. 23: The algebra of little loops for X = S3 /S2 , where Sn is the permutation
group on n letters.

7.3.2.The Turaev algebra associated to a G-space
The algebra Ab (X//G) does not satisfy the sewing conditions and is not a Turaev
algebra. In particular (7.3) is usually not satisfied for a crossed-product algebra. However,
the subcategory defined by the morphisms with the same initial and terminal object does
lead to a Turaev algebra for any B-field b on X//G. We call this the “algebra of little
loops”. Thus we define C = ⊕g Cg ⊂ Ab (X//G) by
Cg := ⊕x:gx=x Lg,x

(7.13)

θ(ℓg,x) = δg,1 θ(εx )

(7.14)

and define the trace by

where on the right θ is the given G-invariant trace on C1 , and the εx are the usual idempo-

tents in the semisimple Frobenius algebra C1 = A(X), i.e. εx = 1 ∈ L1,x = C. The algebra

of little loops can be visualized as in fig. 23.

An equivalent way to describe C is as the commutant of C1 = A(X) in Ab (X//G) =

A(X) ×b G. As A(X) is in the centre of C, it is natural to think of C as the sections of a

bundle of algebras on X; the fibre of this bundle at x ∈ X is the twisted group algebra

Cbx [Gx ], where Gx is the isotropy group of x. Furthermore, the bundle of algebras has
a natural G-action, covering the G-action on X. To see this, notice that the extension
G̃ = {f, g) : f ∈ A(X)× , g ∈ G} of the group G by the multiplicative group A(X)× defined

by the B-field sits inside the multiplicative group of A(X)×b G, normalizing the subalgebra
A(X). As A(X) is in the centre of C, this means that G acts by conjugation on the algebra

C. Notice, however, that only G̃ and not G acts on the larger algebra Ab (X//G).
55

<!-- page 57 -->
In terms of explicit formulae, the action of G on the algebra C is given by
αg1 (ℓg2 ,x ) = ℓg1 ,x ℓg2 ,x ℓ−1
g1 ,x = zx (g2 , g1 )ℓg1 g2 g −1 ,g1 x ,
1

(7.15)

where
zx (g2 , g1 ) =

bx (g1 , g2 )bx (g1 g2 , g1−1 )
.
bx (g1 , g1−1 )

(7.16)

In this way we obtain a Turaev algebra, which we shall denote by C = T (X, b, θ). The

only non-trivial point is to verify the “torus” axiom (7.4) . But in fact it is easy to see
that both sides of the equation are equal to
X

−1
ℓh,x ℓg,xℓ−1
h,x ℓg,x ,

x

where x runs through the set {x ∈ X : hx = gx = x}.
Turaev has shown that the above construction is the most general one possible in the
semisimple case.
Theorem 5 ([48], Theorem 3.6)

Let C be a Turaev algebra. If C1 is semisimple then

C is the twisted algebra T (X, b, θ) of little loops on X = Spec(C1 ) for some cocycle b ∈
2
ZG
(X;C× ).

Proof: If C1 is semisimple we may decompose it in terms of the basic idempotents εx . Then

Cg is a module over C1 , and hence it should be identified with the cross sections of the

vector bundle over the finite set X whose fibre at x is Cg,x = εx Cg . (This is a trivial case

of what is called the Serre-Swan theorem.) Now we consider the torus axiom (7.4) in the
P
case h = 1. We have ∆1 = θ(εx )−1 εx ⊗ εx , and hence
X

θ(εx )−1 αg (εx )εx =

X

θ(εx )−1 εx ,

where the second sum is over x such that gx = x. On the other hand we readily calculate
that if {ax,i } is a basis of Cg,x and {a∗x,i } is the dual basis of Cg −1 ,x then ag,ia∗g,i = θ(εx )−1 εx ,

so that the other side of the torus axiom is
X

dim(Cg,x )εx .
56

<!-- page 58 -->
Thus the axiom tells us that Cg,x is a one-dimensional space Lg,x when gx = x, and is

zero otherwise. The multiplication in C makes these lines into a G-equivariant B-field on

the category of small loops in X//G. Finally, it is not hard to show that the category of
B-fields on X//G is equivalent to the category of G-equivariant B-fields on the category
of small loops; but we shall omit the details. ♠.
Let us now consider the orbifold theory coming from the gauged theory defined by the
Turaev algebra C = T (X, b, θ). We saw in Section 7.2 that it is defined by the commutative
Frobenius algebra Corb which is the G-invariant subalgebra of C. In the case of the Turaev
algebra of a G-space X we have

Theorem 6 The orbifold algebra Corb is the centre of the crossed-product algebra A(X)×b

G. It is the algebra of functions on a finite set (X/G)string which is a “thickening” of the

orbit space X/G with one point for each pair ξ, ρ consisting of an orbit ξ and an irreducible
projective representation ρ of the isotropy group Gx of a point x ∈ ξ, with the projective
cocycle bx defined by the B-field.

Proof The Turaev algebra C consists of the elements of A(X) ×b G which commute with

A(X). But an element of A(X) ×b G belongs to its centre if an only if it commutes with

A(X) and also commutes with the elements of G, i.e. is G-invariant.

Now we saw that C is the product over the points x ∈ X of the twisted group-algebras

Cbx [Gx ]. The invariant part is therefore the product over the orbits ξ of the Gx -invariant
part of Cbx [Gx ], i.e. of the centre of Cbx [Gx ], which consists of one copy of C for each
irreducible representation ρ with the cocycle bx . ♠
The Turaev algebra C = T (X, b, θ) sits between Corb and A(X) ×b G. We shall see in

Section 7.6 that A(X) ×b G is semisimple, and hence Morita equivalent19 to its centre Corb .

But the Turaev algebra retains more information than the orbifold theory: it encodes X

and its G-action. The difference is plainest when G — of order n — acts freely on X; then
A(X) × G is the product of a copy of the algebra of n × n matrices for each G-orbit in X,

and provides us with no way of distinguishing the individual points of X. We shall see in
19

This means that the category of representations of A(X) ×b G is equivalent to the category

of representations of Corb , uniquely up to tensoring with a “line bundle” — a representation L of
Corb such that L ⊗C L′ ∼
= Corb for some L′ .
orb

57

<!-- page 59 -->
section 7.5 that the category of boundary conditions for the gauged theory C is a natural
enrichment of the category for the orbifold theory, at least in the semisimple case.

It might come as a surprise that the cross-product algebra of spacetime A(X) × G is

not the appropriate Frobenius algebra for G-equivariant topological field theory, in view of
the occurrence of the crossed-product algebra as a central concept in the theory of D-branes
on orbifolds developed in [49][50][51]. In fact, this fits in very nicely with the philosophy of
this paper. The Turaev algebra remembers the points of X, and so allows only the “little
loops” above. In this way the sewing conditions - which are meant to formalize worldsheet
locality - also encode a crude form of spacetime locality.
We shall conclude this section by making contact with the usual path integral expression for the orbifold partition function on a torus. To do this we compute dim Corb

by computing the projection onto G-invariant states in C. Note that αg (ℓh,x ) is only

proportional to ℓh,x when [g, h] = 1 and gx = x, and then
αg (ℓh,x ) =

bx (g, h)
ℓh,x
bx (h, g)

where we have combined (7.16) with the cocycle identity. Thus we find
X bx (g, h)
1 X
dim Corb =
|G|
bx (h, g)
gh=hg x=gx=hx

Fig. 24: The wavy line is a constrained boundary. If there is holonomy g along
the dotted path P then this morphism gives the G-action on O.

Fig. 26: Showing that G acts on O as a group of automorphisms.

58

(7.17)

(7.18)

<!-- page 60 -->
Fig. 25: The definition of the multiplication in O. The holonomy on all dotted
paths is 1. Note the order of multiplication.

Fig. 27: The open/closed transitions ιg and ιg .

Fig. 28: The G-twisted centrality axiom.

7.4. Sewing conditions for equivariant open and closed theory
Let us now pass on to consider G-equivariant open and closed theories. We enlarge
59

<!-- page 61 -->
Fig. 29: The G-twisted adjoint relation.

Fig. 30: The G-twisted Cardy condition. In the double-twist diagram the holonomy around P1 is 1 and the holonomy around P2 is g.

the category SG so that the objects are oriented 1-manifolds w ith boundary, with labelled

ends, equipped with principal G-bundles. The morphisms are the same cobordisms as in

the non-equivariant case, but equipped with G-bundles. Up to isomorphism there is only
one G-bundle on the interval: it is trivial, and admits G as an automorphism group. So an
equivariant theory gives us for each pair a, b of labels a vector space Oab with a G-action.

The action of g ∈ G on Oab can be regarded as coming from the “square” cobordism with

the bundle whose holonomy is g along each of its “constrained” edges. There is also a

composition law Oab × Obc → Oac , which is G-equivariant. These are illustrated in fig. 24

and fig. 25.

In the open/closed case the conditions analogous to equations (2.2) to (2.12) are the
following.
Focussing first on a single label a, we have a not necessarily commutative Frobenius
60

<!-- page 62 -->
algebra (Oaa = O, θO ) together with a G-action ρ : G → Aut(O):


ρg (ψ1 ψ2 ) = ρg ψ1 ρg ψ2

(7.19)

which preserves the trace θO (ρg ψ) = θO (ψ). See fig. 26.
There are also G-twisted open/closed transition maps
ιg,a = ιg : Cg → Oaa = O
ιg,a = ιg : Oaa = O → Cg
which are equivariant:
Cg1
↓ ιg1
O

α g2

→

Cg2 g1 g2 −1
↓ ιg2 g1 g2 −1

ρg2

→

−1

g1 g2

O

(7.21)

O

α g2

Cg2 −1 g1 g2
ιg2

(7.20)

↑

→

Cg1

ρg2

↑ ιg1
O

→

(7.22)

These maps are illustrated in fig. 27. The open/closed maps must satisfy the G-twisted
versions of conditions 3a-3e of section 2.2. In particular, the map ι : C → O obtained by

putting the ιg together is a ring homomorphism, i.e.
ιg1 (φ1 )ιg2 (φ2 ) = ιg2 g1 (φ2 φ1 )

∀φ1 ∈ Cg1 , φ2 ∈ Cg2 .

(7.23)

Since the identity is in C1 the condition (2.8) is unchanged. The G-twisted centrality
condition is

ιg (φ)(ρg ψ)) = ψιg (φ)

∀φ ∈ Cg , ψ ∈ O.

(7.24)

∀φ ∈ Cg −1 .

(7.25)

and is illustrated in fig. 28.
The G-twisted adjoint condition is


θO ψιg −1 (φ) = θC ιg (ψ)φ)
and is shown in fig. 29.
Finally, the G-twisted Cardy conditions restrict not only each algebra Oaa , but also

the spaces of morphisms Oab between labels b and a. For each g ∈ G we must have
πg,ba = ιg,b ιg,a
61

(7.26)

<!-- page 63 -->
Here πg,ba is defined by
πg,ba (ψ) =

X
µ


ψ µ ψ ρ g ψµ ,

(7.27)

where we sum over a basis ψµ for Oab , and take ψ µ to be the dual basis of Oba . See fig. 30.
We may now formulate

Theorem 7

The above conditions form a complete set of sewing conditions for G-

equivariant open/closed 2d TFT.
This will be proved in the appendix. Note that the above axioms are slightly redundant
since (7.21) and (7.25) together imply (7.22).
7.5. Solution of the sewing conditions for semisimple C
We now show that, when C is semisimple, the solutions of the above sewing conditions

are provided by G-equivariant bundles on X = Spec(C1 ) twisted by the B-field defined by
C.

Let us first say a word about these bundles. To give a finite dimensional representation

of the cross-product algebra A(X) × G is to give a representation of A(X) — i.e. a vector

bundle E on X — together with an intertwining action of G. Thus representations of

A(X) × G are precisely G-vector-bundles on X. For a finite group G there are many

equivalent ways of defining the notion of a twisted G-vector-bundle on X, twisted by a B-

2
field b representing an element of HG
(X;C× ): the simplest for our purposes is to say that

a twisted bundle is just a representation of A(X) ×b G. (Unfortunately this description

does not work when G is not finite, and so it is not the one used in [52] . We shall explain
the relationship with the description of [52] at the end of this subsection.)
The problem is easily reduced to consideration of a single G-orbit, so we may assume
X = G/H for some subgroup H of G. Accordingly, the closed string Frobenius data is
specified by a 2-cocycle b and a single constant θc ∈ C× defining the trace: θ(ℓg,x) = δg,1 θc .

As usual, the isomorphism class only depends on [b] ∈ H 2 (H;C× ).
Theorem 8

Let C = T (X, b, θc) be a Turaev algebra with C1 semisimple and X =

G/H. For a single label a the most general solution O = Oaa of the sewing constraints is
√
determined by a choice of square-root θo = θc and a projective representation V of H
with the cocycle bo which is the restriction of b.
62

<!-- page 64 -->
X:

The algebra O is the algebra of sections of the G-equivariant bundle of algebras over


O := Γ G ×H (End(V )) = IndG
H End(V ) ,

(7.28)

X

(7.29)

and the trace is determined by θo :

θO (Ψ) = θo

TrV (Ψ(x)).

x∈G/H

Proof
Let us suppose that we have a Turaev algebra C with C1 semisimple, together with

O, θO , ιg , ιg satisfying the sewing conditions. Let X be the G-space Spec(C1 ). Then, from

our results in the non-equivariant case, we know that O = EndC1 (Γ(End(E))) for some

vector bundle E → X, unique up to tensoring wtih a line bundle L → X. Thus O = ⊕Ox ,

where Ox = End(Ex ). We also know that the trace on O must be given by (3.7) . The

same square-root θo of θx must be taken for each x ∈ X to make θ : O → C invariant under

G. Now G acts compatibly on C1 and O by algebra isomorphisms, so g ∈ G maps Ox0 to

Ox by an algebra isomorphism. This proves (7.28) , where V = Ex0 . Finally, the Turaev

algebra C is the product ⊕Cx , where Cx is the twisted group-ring of Gx with the twisting

bx . The algebra homomorphism C → O makes Cx act on Ex , and so V is a projective
representation of H = Gx0 with the cocycle bx0 .

This proves that O is of the form stated. One must still check that the definition

(7.28) does provide a solution of the sewing conditions, but that presents no problems.

Remark Although in the hypothesis of the theorem we were given a cocycle b representing
2
an element of HG
(X;C× ), the conclusion uses only its restriction bx0 . This should not
2
surprise us, as cohomologous cocycles b define isomorphic Turaev algebras, and HG
(X;C× )
2
is canonically isomorphic to the group cohomology HH
(point;C× ) when X = G/H.

We can now deduce a complete description of the category of boundary conditions,
using exactly the same arguments by which we obtained Theorem 3 from Theorem 2.
Theorem 9

If C is a Turaev algebra with C1 semisimple, corresponding to a space-time

X with a B-field b, then the category of boundary conditions for C is equivalent to the
category of b-twisted G-vector-bundles on X, uniquely up to tensoring with a G-line-bundle

on X. Its Frobenius structure is determined by a choice of the dilaton field θ.
63

<!-- page 65 -->
The meaning of this theorem needs to be explained. The linear category of equivariant boundary conditions for a given Turaev algebra is an example of what is called an
“enriched” category: for each pair of objects a, b the vector space Oab has an action of
the group G. Now the category VectG of finite dmensional vector spaces with G-action is

a symmetric tensor category, with the neutral object C. To say that we have a category
enriched in a tensor category such as VectG means that we have
(i) a set of objects,
(ii) for each pair a, b of objects an object Oab of VectG , and

(iii) for each triple a, b, c of objects an associative “composition” morphism
Oab ⊗ Obc → Oac

of G-vector spaces.
The axioms are almost identical to the axioms for a category, but the space of morphisms has extra structure. In such a situation the category is said to be an enrichment
of the ordinary linear category in which the morphisms from b to a are F (Oab ), where
F : VectG → Vect is the functor defined by F (V ) = HomG (C; V ) = V G . There is, how-

ever, another ordinary category associated to the enriched category by simply forgetting
the G-action, so that the morphisms from b to a are simply Oab as a vector space.

An example of a category enriched in VectG is the category of finite dimensional rep-

resentations of G̃, where G̃ is a central extension (with a fixed cocycle) of G by the circle,
where the central circle acts by scalar multiplication. Indeed, given two such representations V1∗ ⊗ V2 is a representation of G.

Theorem 9 should really be expanded as follows. The category of b-twisted G-vector-

bundles on X has a natural enrichment in VectG , in which the G-vector space of morphisms
consists of the homomorphisms of b-twisted vector bundles which are not necessarily equivariant with respect to the G-action. This enrichment is equivalent to the category of equivariant boundary conditions. The underlying ordinary category is the category of boundary
conditions for the orbifold theory.
Theorem 9 has a converse, which is the G-equivariant extension of the discussion of
§3.3
Theorem 10

If B is a linear category enriched in VectG , with G-equivariant traces

making it a Frobenius category, and the linear category obtained from B by forgetting the
64

<!-- page 66 -->
G-action is semisimple with finitely many irreducible objects, then B is equivalent to the

category of equivariant boundary conditions for a canonical equivariant topological field
theory. The Turaev algebra defining the theory is ⊕g Cg , where an element of Cg is a family

φa ∈ Oaa , indexed by the objects a of B, satisfying

φa ◦ f = (g.f ) ◦ φb

(7.30)

for each f ∈ Oab .

To prove this, one must show that (7.30) really does define a Turaev algebra. The

details are straightforward and we will omit them.
7.6. Equivariant boundary states
To conclude our discussion, let us consider the equivariant analogues of the “boundary
states” discussed in §4. Our notion of the category of boundary conditions for a G-gauged

theory is intrinsically G-invariant, and we have already pointed out that it gives us exactly
the same category as we would obtain from the orbifold theory in which we have summed
over the gauge fields. To reformulate this in terms of boundary states we begin with the
definition.
In the gauged theory associated to a Turaev algebra C = T (X, b, θ) the observables at

any point of the world-sheet are precisely the elements of C. The boundary state Ba ∈ C

associated to a boundary condition a is characterized by the property that the correlation
function of observables φ1 , . . . , φk evaluated at points of a surface Σ with boundary S 1
with the boundary condition a (and arbitrary holonomy around the boundary) is equal to
that of the same observables on the closed surface obtained by capping-off the boundary,
with the additional insertion of Ba at the centre of the cap. It suffices (because of the
factorization properties of a field theory) to check the case when Σ is a disc. The correlation
function on the disc is obtained by propagating φ1 . . . φk ∈ Cg to H(∅) = C by the annulus

whose non-incoming boundary circle is constrained by the condition a, along which the
holonomy is necessarily g. Our rules tell us that the result is
θOaa (ιg,a (φ1 . . . φk )).
Equating this to θC1 (φ1 . . . φk Ba ), we see that
Ba =

X
g

65

ιg,a (1).

<!-- page 67 -->
The map a 7→ Ba evidently has its image in the G-invariant part — i.e. the centre —

of the Turaev algebra. It extends to a homomorphism

KG,h (X) → T (X, b, θ)G ,
and we have
Theorem 11 The G-invariant boundary states generate a lattice in T (X, b, θ)G related
to the twisted equivariant K-theory via:
KG,h (X) ⊗ C = T (X, b, θ)G.

(7.31)

Remark
1. Equation (7.31) is related to an old observation of [53]. If X = G with G acting on
itself by conjugation then T (X, 0)G is the Verlinde algebra occuring in the conformal
field theory of orbifolds for chiral algebras with one representation [53]. The different
orbits are the conjugacy classes of G. Focusing on one conjugacy class [g] we can
compare with the above results. One basis of states is provided by a choice of a
character of the centralizer of g. These are just the G-invariant boundary states
found above.
2. The translation of the above results to the language of branes at orbifolds is the
following. The boundary states corresponding to the different b-irreps Vi are the
“fractional branes” of [49]. The use of projective representations was proposed in [49],
and further explored in [54]. A different proof of the fact that the cocycle for the open
sector and that of the closed sector b are cohomologous can be found in [55].
To conclude this section, let us return to explain the relation between the definition
of twisted equivariant K-theory by A(X) ×b G-modules and the definition given in [52] .

In [52] the elements of the twisted equivariant theory are described as follows. First,

3
the twisting class b ∈ HG
(X; ZZ) is represented by a bundle P of projective Hilbert spaces

on X equipped with a G-action covering the G-action on X. Then elements of KG,P (X)
are represented by families {Tx }x∈X of fibrewise Fredholm operators in the bundle P .
Let us show how to associate such a pair (P, {Tx }) to a finitely generated A(X) ×b G-

module. Such a module is the same thing as a finitely generated A(X)-module equipped

with a compatible action of the extended group G̃ associated to b which we have already
66

<!-- page 68 -->
described. Equivalently, it is a finite dimensional vector bundle E on X with an action
of G̃ on the total space which covers the action of G on X. Let us choose a fixed infinite
dimensional Hilbert space H. Then Ê = E ⊗H is a Hilbert bundle on X, and the associated

bundle P = IP(Ê) of projective spaces has a natural action of G, and it represents the
3
class of b in HG
(X; ZZ). (Cf. the proof of Proposition 6.3 in [52] .) If T : H → H is a fixed

surjective Fredholm operator with a one-dimensional kernel, then (identity)E ⊗ T : P → P

represents an element of KG,P (X) according to the definition of [52] .

If the cocycle b is a coboundary — or even if bx (g1 , g2 ) is independent of x ∈ X — it is

plain that the two rival definitions of equivariant K coincide. A Mayer-Vietoris argument
can then be used to show that they coincide for all b.

The essential point here is that when X and G are finite the twisting class b is of
finite order, and that makes it possible to represent the K-classes by families of Fredholm
operators of constant rank, and hence by finite dimensional vector bundles.

Appendix A. Morse theory proof of the sewing theorems
In this appendix we shall use Morse theory to give uniform proofs of four theorems.
The first is the very well-known result that a two-dimensional topological field theory is
precisely encoded in a commutative Frobenius algebra. The second is the corresponding
statement for open and closed theories: this is Theorem 1 of Section 2 above. The third
and fourth are the equivariant analogues of the first two, i.e. Theorems 4 and 7 of Section
7.
A.1. The classical theorem
We wish to prove that when we have a commutative Frobenius algebra C we can assign

to an oriented cobordism Σ from S0 to S1 a linear map
UΣ : C ⊗p → C ⊗q ,

where the oriented 1-manifolds S0 and S1 have p and q connected components respectively.
We can always choose a smooth function f : Σ → [0, 1] ⊂ IR such that f −1 (0) = S0

and f −1 (1) = S1 , and which has only “Morse” singularities, i.e. the gradient df vanishes
at only finitely many points x1 , . . . , xn ∈ Σ, and

(i) the Hessian d2 f (xi ) is a non-degenerate quadratic form for each i, and
67

<!-- page 69 -->
(ii) the critical values c1 = f (x1 ), . . . , cn = f (xn ) are distinct, and not equal to 0 or
1.
Each critical point has an index, equal to 0, 1, or 2, which is the number of negative
eigenvalues of the Hessian d2 f (xi ).
The choice of the function f gives us a decomposition of the cobordism into “elementary” cobordisms. If
0 = t0 < c1 < t1 < c2 < t2 < . . . < cn < tn = 1,
and St = f −1 (t), then each Sti is a collection of, say, mi disjoint circles, with mi = mi−1 ±1,

and Σi = f −1 ([ti−1 , ti ]) is a cobordism from Sti−1 to Sti which is trivial (i.e. a union of
cylinders) except for one connected component of one of the four forms of fig. 2.
For a given Frobenius algebra C we know how to define an operator
UΣi : C ⊗mi−1 → C ⊗mi
in each case. (In the third case the map we assign is

φ 7→

X

φφi ⊗ φi ,

where {φi } and {φi } are dual bases of C such that θC (φi φj ) = δij .) We should notice two

points. First, we need C to be commutative, for otherwise we would need to have an order

on the two incoming circles of a pair of pants, and no such order is given. Secondly, the
assignments we make have the property that reversing the direction of time in a cobordism
replaces the operator by its adjoint with respect to the Frobenius inner product on the
state-spaces. This property will be a firm principle in all our constructions, and it reduces
the number of cases we have to check in the tedious arguments below.

Fig. 31:

68

<!-- page 70 -->
The important task now is to show that the composite operator UΣn ◦ · · · ◦ UΣ1 is

independent of the chosen Morse function f .

Two Morse functions f0 and f1 can always be connected by a smooth path {fs }0≤s≤1

in which fs is a Morse function except for a finite set of parameter values s at which one
of the following two things happens:
(i)

fs has one degenerate critical point where in local coordinates (u, v) it has the

form fs (u, v) = ±u2 + v 3 , or
(ii)

two distinct critical points xi , xj of fs have the same critical value fs (xi ) =

fs (xj ) = c.
In the first case, two critical points of adjacent indices are created or annihilated as the
parameter passes through the non-Morse value s, and the cobordism changes by fig. 31.
or vice-versa, or by the time-reversal of these pictures. The well-definedness of UΣ under
this kind of change is ensured by the identity 1.a = a in the algebra C.

Case (ii) is more problematical. Because operators of the form U ⊗ 1 and 1 ⊗ U ′

commute, we easily see that there is nothing to prove unless the two critical points xi and
xj are connected in the “bad” critical contour Sc , in which case they must both have index
1.
Let us consider the resulting two-step cobordism which is factorized in different ways
before and after the critical parameter value s. It will have just one non-trivial connected
component, which, because an elementary cobordism changes the number of circles by 1,
must be a cobordism from p circles to q circles, where (p, q) = (1, 1), (2, 2), (1, 3) or (3, 1).
We need to check only one of (1,3) and (3,1), as they differ only by time-reversal. Because
the Euler number of a cobordism is the number of critical points of its Morse function
(counted with the sign (−1)index ), the non-trivial component has Euler number −2, so is

a 2-holed torus when (p, q) = (1, 1) and a 4-holed sphere in the other cases.

Fig. 33:

69

<!-- page 71 -->
Fig. 32:

Fig. 34:

Fig. 35:

In the case (1,1), depicted in fig. 32, a circle splits into two which then recombine.
There is nothing to check, because, though a torus with two holes can be cut into two pairs
of pants by many different isotopy classes of cuts, there is only one possible composite
cobordism, and we have only one possible composite map C → C ⊗ C → C.

In the case (3,1), two circles of the three combine, then the resulting circle combines

with the third. The picture is fig. 33. Clearly this case is covered by the associative law
in C.

In the case (2,2) we are again factorizing a 4-holed sphere into two elementary cobor-

disms. This can be done in many ways, as we see from the pictures fig. 34. The best way
of making sure we are not overlooking any possibility is to think of the contour just below
70

<!-- page 72 -->
the doubly-critical level, which, if it consists of two circles, must have one of the two forms
(i) or (ii) in fig. 35. (Consider the possible ways of connecting the “terminals” inside the
dotted circles.) But, whatever happens, the only algebraic maps the cobordism can lead
to are
C⊗C →C →C ⊗C
and
C ⊗ C → C ⊗ C ⊗ C → C ⊗ C,
given by
φ ⊗ φ′ 7→ φφ′ 7→

X

φφ′ φi ⊗ φi

and
φ ⊗ φ′ 7→

X

φφi ⊗ φi ⊗ φ′ 7→

X

φφi ⊗ φi φ′

respectively, where {φi } and {φi } are dual bases of C such that θC (φi φj ) = δij . These two

maps are equal because of the identity
X

φ′ φi ⊗ φi =

X

φi ⊗ φi φ′ ,

(A.1)

which holds in any Frobenius algebra because the inner product of each side with φj ⊗ φk
is θC (φj φ′ φk ).

That completes the proof of the theorem: notice that we have used all the axioms of
a commutative Frobenius algebra.
A.2. Open and closed theories
As in the preceding argument we consider a cobordism Σ from S0 to S1 , but now S0
and S1 are collections of circles and intervals, and the boundary ∂Σ has a constrained part
∂constr Σ, which we shall abbreviate to ∂ ′ Σ, which is a cobordism from ∂S0 to ∂S1 . We
choose f : Σ → [0, 1] as before, but now there are two kinds of critical points of f : interior

points of Σ at which the gradient df vanishes, and points of ∂ ′ Σ at which the gradient of the
restriction of f to the boundary vanishes. For an internal critical point, “nondegenerate”
has its usual meaning. A critical point x on the boundary is called nondegenerate if it is
a nondegenerate critical point of the restriction of f to ∂ ′ Σ, and in addition the derivative
of f normal to the boundary does not vanish at x.
71

<!-- page 73 -->
As before, f is a Morse function if all its critical points are non-degenerate, and all
the critical values are distinct and 6= 0, 1. We can always choose such a function.

There are now four kind of boundary critical points, which we can denote 0±, 1±,

recording the index and the sign of the normal derivative. Six things can happen as
we pass through one of them. At those of type 0+ or 1−, an open string is created or
annihilated. At type 0− either two open strings join end-to-end, or else an open string
becomes a closed string. Type 1+ is the time-reverse of 0−. If we have a Frobenius
catgegory B, we know what to do in each of the six cases.

Fig. 36:

An internal critical point has index 0,1, or 2, as before. Only if the index is 1 can
the corresponding cobordism involve an open string. Up to time reversal, there are three
index 1 processes: two closed strings can become one, an open string can “absorb” a closed
string, and two open strings can “reorganize themselves” to form two new open strings as
in fig. 36.
For a given Frobenius category B, we assign to (open)+(closed)→(open) the map
Oab ⊗ C → Oab
given by φ ⊗ ψ 7→ φψ. (Here, as we usually do, we are regarding Oab as a C-module,

writing

φψ = ιa (φ)ψ = ιb (φ)ψ.)
To (open)+(open)→(open)+(open) we assign the map
Oab ⊗ Ocd → Oad ⊗ Ocb
given by
ψ ⊗ ψ ′ 7→

X

ψψi ⊗ ψ ′ ψ i ,

where ψi and ψ i are dual bases of Obd and Odb .
72

<!-- page 74 -->
We must now consider what happens when we change the Morse function. As before,
two Morse functions can be connected by a path {fs } in which each fs is a Morse function

except for finitely many values of s at which either one critical point is degenerate or else

two critical values coincide. We begin with the degenerate case. There are now three kinds
of degeneracy which we must allow, for besides internal degeneracies which are just as in
the closed string case we can have two kinds of degeneracy on the boundary: either f |∂ ′ Σ

has a cubic inflexion, or else the normal derivative vanishes at a boundary critical point.

Fig. 37:

When s passes through a boundary inflexion, two nondegenerate boundary critical
points of opposite index but with normal derivatives of the same sign are created or annihilated. This means that the cobordism changes between figures (i) and (ii) of fig. 37
(or the time-reversal). These changes are covered by the axiom that the category B has

identity morphisms.

When the normal derivative vanishes at a boundary critical point what happens is
that an internal critical point has moved “across the boundary of Σ, i.e. it moves into
coincidence with a boundary critical point and changes the sign of the normal derivative
there. There are four cases:
(0−) + (index 0) → (0+),
(0+) + (index 1) → (0−),
and the time-reversals of these. In the first case, the composite cobordism in which a small
closed string is created and then breaks open is replaced by the elementary cobordism in
which an open string is created. This corresponds to the axiom that C → Oaa takes 1C to

1a . In the second case, in the composite cobordism, an open string is created, and then it
either “absorbs” an existing closed string or else “rearranges” itself with an existing open
string; these composites are to be equivalent, respectively, to the elementary breaking of
73

<!-- page 75 -->
a closed or open string. Putting ψ = 1a in the formulae above we see that this is allowed
by the Frobenius category axioms.
When we have an internal degenerate critical point, what happens, up to time-reversal,
is that a closed string is created and then joins an existing open or closed string; this should
be the same as the trivial cobordism. Again, the unit axioms cover this.

Fig. 38:

Fig. 39:

Finally, we have to consider what happens when two critical values cross. They can
be two boundary critical points, two internal ones, or one of each.
If two boundary critical points are linked by a critical contour, it has the form fig. 38.
These give us four cases to check, where the contour below the critical level is fig. 39.
Case (i)a is accounted for by the associativity of composition in the category B; case (i)b

by the open-string analogue of the identity (A.1); case (ii)a by the trace axiom ιa (ψ1 ψ2 ) =
ιb (ψ2 ψ1 ), which follows by combining (cyclic),(center),and (adjoint); and case (ii)b by the
Cardy identity.
74

<!-- page 76 -->
Fig. 40:

When we have one boundary and one internal critical point at the same level we may
as well assume the boundary point is of type 0− and the internal critical point is of index
1, and that they are joined in the critical contour,which must have one of the four forms
fig. 40.
At the boundary point either an open string becomes closed, or else two open strings
join. We shall consider each possibility in turn. In the first case, if the boundary point is
encountered first, then at the interior point three things can happen: the closed string can
split into two closed strings, or it can combine with another closed or open string. Thus
the possibilities are
o → c → c + c
o + c → c + c → c
o + o → c + o → o.
When the internal point is encountered first there is only one possibility in each case, and
the three sequences are replaced respectively by
o → o + c → c + c
o + c → o → c
o + o → o + o → o.
We have to check three identities. The first two reduce to the fact that ιa : Oaa → C is a

map of modules over C. The third is the Cardy condition.

Now let us consider the case where two open strings join at the boundary critical

point. If we meet the boundary point first, there are again three things that can happen at
the internal critical point: the open string can emit a closed string, or else it can interact
with another closed or open string. The possibilities are
75

<!-- page 77 -->
o + o → o → o + c
o + o + c → o + c → o
o + o + o → o + o → o + o.
In the second and third of these cases there is only one thing that can happen when the
order of the critical points is reversed: they become

o + o + c → o + o → o
o + o + o → o + o + o → o + o.
The identities relating the corresponding algebraic maps Oab ⊗ Obc ⊗ C → Oac and Oab ⊗

Obc ⊗ Ode → Oae ⊗ Odc are immediate.

The first sequence, however, can become either
o + o → o + o + c → o + c
or
o + o → o + o → o + c.
The first of these presents nothing of interest algebraically, but to deal with the second we
need to check that
X

ψψ ′ φi ⊗ φi =

X

ψψ k ⊗ ιb (ψ ′ ψk )

for ψ ∈ Oab , ψ ′ ∈ Obc , and dual bases φi , φi of C and ψ k , ψk of Obc , Ocb . This relation
holds because the inner product of the left-hand side with ψm ⊗ φj is θb (ψψ ′ φj ψm ), while

the inner product of the right-hand side with ψm ⊗ φj is
X
k

θb (ψψ k ψm )θ(ιb (ψ ′ ψk )φj ) =

X

θb (ψm ψψ k )θb (ψk φj ψ ′ )
(A.2)

k

′

′

= θb (ψm ψφj ψ ) = θb (ψψ φj ψm ).

76

<!-- page 78 -->
Fig. 41:

Fig. 42:

Fig. 43:

77

<!-- page 79 -->
Finally, we must consider what happens when there are two internal critical points
on the same level. Here we have the possibilities which we have already discussed in the
closed case, but must also allow any or all of the strings involved to be open. We can
analyse the situation according to the number of connected components of the part of
the contour immediately below the doubly critical level which pass close to the critical
points. There must be one, two, or three such components. If there are three they can
form five configurations (apart from the case when all three are closed), as depicted in
fig. 41. The well-definedness of the composite map in all these cases follows immediately
from the associative law of composition in the Frobenius category.
If there are two components below the critical level then they can again form five
configurations (for either the two components meet twice, or else they meet once, and one
of them has a self-interaction), depicted in fig. 42. But we have only three cases to check,
as the second is the time-reversal of one from fig. 41, and the last two are time-reversals
of each other. Case 15(i) corresponds to the fact that the composition
Oab ⊗ C → Oab → Oab ⊗ C
can be effected by cutting the composite cobordism in different ways, but there is nothing
to check, as there is only one possible algebraic map.
In fig. 42 case(iii), one order of the critical points gives us the same composition
Oab ⊗ C → Oab → Oab ⊗ C
as before, while the other order gives
Oab ⊗ C → Oab ⊗ C ⊗ C → Oab ⊗ C;
but it is very easy to check that both maps take ψ ⊗ φ to

have already used.

P

ψφφi ⊗ φi in the notaion we

In fig. 42 case(iii) we must again compare compositions
Oab ⊗ C → Oab ⊗ C ⊗ C → Oab ⊗ C
and
Oab ⊗ C → Oab → Oab ⊗ C.
78

<!-- page 80 -->
This time we must check that
X

ψφi ⊗ φi φ =

X

ψφφi ⊗ φi .

This is the same formula which we met at the end of our discussion of closed string theories.
Finally, suppose that the contour below the critical level has only one connected
component. There are three possible configurations, corresponding to the three ways of
pairing four points on an interval. They are fig. 43. The first two of these are time-reversals
of cases we have already treated. The last one leads — in either order — to a factorization
Oab → Oab ⊗ C → Oab .
There is only one possibility for this, so there is nothing to check.
That completes the proof of the theorem about open and closed theories.

Fig. 44:

Fig. 45:

79

<!-- page 81 -->
Fig. 46:

Fig. 47:

A.3. Equivariant closed theories
We must now redo the discussion in the first part of this appendix, but for surfaces
and circles equipped with a principal G-bundle, where G is a given finite group.
The first observation is that any circle with a bundle is isomorphic to a standard bundle
Sg with holonomy g ∈ G on the standard circle S 1 . Furthermore the set of morphisms

from Sg to Sg ′ is {h ∈ G : hgh−1 = g ′ }. In other words, the category of bundles on S 1 is
equivalent to the category G//G formed by the group G acting on itself by conjugation.
An equivariant theory therefore gives us a vector space Cg for each g, and together the Cg

form a G-vector-bundle on G. Conversely, given the G-vector-bundle {Cg } and a circle S

with a bundle P on it, the theory gives us the vector space H(S, P ) whose elements are

rules which associate ψx,t ∈ Cgx,t to each x ∈ S and trivialization t : Px → G, where gx,t
is the holonomy of P with base-point (x, t), and we require that
ψx′ ,t′ = gψx,t
80

<!-- page 82 -->
if g is the holonomy of P along the positive path from (x, t) to (x′ , t′ ). For this to be
well-defined we need the condition that gx,t acts trivially on Cgx,t , whose necessity we have

already explained in Section 7.

Next we consider the trivial cobordism from Sg to Sg ′ . The possible extensions of
the bundles on the ends over the cylinder correspond to the possible holonomies from the
incoming base-point to the outgoing base-point, i.e. to the set of morphisms {h ∈ G :

hgh−1 = g ′ } in G//G. Clearly these cylinders induce the isomorphisms Cg → Cg ′ which

we already know. But two such cobordisms are to regarded as equivalent if there is a
diffeomorphism from the cylinder (with its bundle) to itself which is the identity on the
ends. The mapping-class group of the cylinder is generated by the Dehn twist around it,
so the morphism corresponding to h is equivalent to that for hg = g ′ h. This means that g
must act trivially on Cg , as we already know.

Now we come to the possible bundles on the four elementary cobordisms of diagram

1. The bundle on a cap must of course be trivial. The pair-of-pants cobordisms that are
relevant to us arise as the regions between nearby level curves separated by a critical level.
We can draw them as in fig. 44, where the solid contour is below the critical level, and the
dashed one is above it. We can trivialize the G-bundle in the neighbourhood of the critical
point (i.e. within the dotted circles), and then the bundle on the cobordism is determined
by giving the holonomies g1 , g2 along the ribbons, as indicated. The operator we associate
to case (i) is the multiplication map
mg1 ,g2 : Cg1 ⊗ Cg2 → Cg1 g2
of ((7.1)). In writing it this way we are choosing an ordering of the ribbons, i.e. a base-point
on the outgoing loop. The two orderings are related by the conjugation
αg2 : Cg1 g2 → Cg2 g1 ,
so the consistency condition for us to have a well-defined assignment is that
mg2 ,g1 (ψ2 ⊗ ψ1 ) = αg2 (mg1 ,g2 (ψ1 ⊗ ψ2 )).
We see that this holds in any Turaev algebra by combining ((7.3)) with the facts that G
acts on the algebra by algebra-automorphisms, and that αg2 acts trivially on Cg2 . As the
mapping-class group of the pair of pants is generated by the three Dehn twists parallel to
81

<!-- page 83 -->
its boundary circles, there are no new conditions needed to make the assignment of the
operator to the pair of pants well-defined.
The homomorphism
cg1 ,g2 : Cg1 g2 → Cg1 ⊗ Cg2
corresponding to the coordism 17(ii) is fixed by the requirement of adjunction, bearing in
mind that the dual space to Cg is Cg −1 . It is given by
cg1 ,g2 (φ) =

X

φφi ⊗ φi ,

where {φi } is a basis for Cg2 , and {φi } is the dual basis of Cg −1 .
2

Any cobordism with a bundle can be factorized by Morse theory just as before; bundles are inherited by the elementary cobordisms. The difficult part of the discussion is
considering what happens when we change the Morse function. But in fact the only step
which presents anything significant is the consideration of the interchange of two critical
points of index 1 on the same level, i.e. the cobordisms of fig. 32, fig. 33, fig. 34.
Let us consider the case fig. 32, where a string divides and then rejoins — i.e. a
torus with two holes, one incoming and one outgoing. We draw the picture in the form
fig. 45. (We do not draw it in the apparently more perspicuous form fig. 46, as then the
neighbourhoods of the two critical points would have opposite orientation in the plane.)
The cobordism corresponds to a map C4321 → C2341 , where, as in the following, we

have abbreviated Cg4 g3 g2 g1 to C4321 . If the left-hand critical point is encountered first, the
map we obtain is

C4321 → C43 ⊗ C21 ∼
= C34 ⊗ C12 → C3412 ∼
= C2341 ,
φ 7→

X

φφi ⊗ φi 7→

X

α3 (φφi ) ⊗ α1 (φi ) 7→

X

α3 (φφi )α1 (φi ) 7→

X

α2 (α3 (φφi )α1 (φi )),

where φi runs through a basis for C21 , and we write α3 for αg3 , and so on. (The maps
indicated by ∼
= in the previous line correspond to moving the choice of base-point on the
various strings.)
With the other order, we get
C4321 ∼
= C23 ⊗ C41 → C2341
= C3214 → C32 ⊗ C14 ∼
φ 7→ α−1
4 (φ) 7→

X

i
α−1
4 (φ)ψ ⊗ψi 7→

X

i
α2 (α−1
4 (φ)ψ ))⊗α4 (ψi ) 7→

82

X

i
α2 (α−1
4 (φ)ψ )α4 (ψi ),

<!-- page 84 -->
where ψi runs through a basis of C14 .

Thus we must prove that
X
X
α23 (φφi )φi =
α24−1 (φ)α2 (ψ i )α4 (ψi ).

We can deduce this from the axiom (newax) of §7, with h = g2 g4−1 g1−1 g2−1 and g = g1−1 g2−1 ,
as follows. We rewrite the right-hand side of the equation as
X
α24−1 (φ)ξ i αg (ξi ),

where ξ i is the basis α2 (ψ i ) of Ch , so that ξi = α2 (ψi ) and αg (ξi ) = α−1
1 (ψi ) = α4 (ψi ). By

the axiom this equals

X

Finally,

α24−1 (φ)αh (η i )ηi =

X

α24−1 αh (φi )φi .

α24−1 (φ)αh (φi ) = α24−1 (φφi ) = α23 (φφi ),
because φφi ∈ C43 , and so α24−1 (φφi ) = α24−1 α43 (φφi ) = α23 (φφi ). Thus we have dealt

with the case of fig. 32.

If fact this case is decidedly the most complicated of the set. We shall do one more,
namely case (i) of fig. 35, in which two strings join and then split. We draw the diagram
as in fig. 47, corresponding to the two compositions
C43 ⊗ C21 → C4321 ∼
= C41 ⊗ C23
= C1432 → C14 ⊗ C32 ∼
C43 ⊗ C21 ∼
= C4123 → C41 ⊗ C23 .
= C34 ⊗ C12 → C3412 ∼
The first sequence gives us
ψ ⊗ ψ ′ 7→ ψψ ′ 7→ α1 (ψψ ′ ) 7→

X

α1 (ψψ ′ )φi ⊗ φi 7→

where φi is a basis for C32 . The second sequence gives

X

α4 (α1 (ψψ ′ )φi ) ⊗ α2 (φi ),

ψ ⊗ ψ ′ 7→ α3 (ψ) ⊗ α1 (ψ ′ ) 7→ α3 (ψ)α1 (ψ ′ ) 7→ ψα3−1 1 (ψ ′ ) 7→

X

ψα3−1 1 (ψ ′ )ψ i ⊗ ψi ,

where ψi is a basis for C23 . But we can assume that ψi = α2 (φi ), and hence that ψ i =

α2 (φi ). So, noticing that α1 (ψψ ′ )φi ∈ C14 , and hence that

α4 (α1 (ψψ ′ )φi ) = α−1 (α1 (ψψ ′ )φi ),
what we need to prove is just that
ψ ′ α−1 (φi ) = α3−1 (α1 (ψ ′ )φi ).
This is true because α1 (ψ ′ )φi ∈ C13−1 , and so is fixed by α13−1 .
We shall leave the remaining verifications to the reader.
83

<!-- page 85 -->
Fig. 48:

Fig. 49:

A.4. Equivariant open and closed theories
We now have to redo the open and closed case taking account of G-bundles on the
cobordisms.
We assign the vector space Oab to an open string from b to a equipped with a trivial-

ization of the bundle on it. Changing the trivialization by an element g ∈ G corresponds

to the action ρg of g on Oab , which also corresponds to the map induced by a rectangular

cobordism with holonomy g along its constrained edges.

We must consider the maps to be associated to the elementary cobordisms corresponding to the critical points of a Morse function. Up to time-reversal, two interesting
things can happen at a boundary critical point: either two open strings join end-to-end
or an open string becomes closed. We have the pictures of fig. 48. As before, the solid
line is the contour below the critical point, and the dashed line that above it. In 20(i),
ga , gb , gc are the holonomies between nearby points on the respective D-branes, expressed
in terms of the chosen trivializations on the strings. (They satisfy gc gb = ga .) The map
Oab ⊗ Obc → Oac that we associate to this situation is
ψ ⊗ ψ ′ 7→ ρga (ψ)ρgb (ψ ′ ).
84

<!-- page 86 -->
The dual operation Oac → Oab ⊗ Obc is
ψ 7→

X

ρg1 (ψξ i ) ⊗ ρg2 (ξi ),

where ξi and ξ i are dual bases of Obc and Ocb .

In case (ii) of fig. 48, the open string becomes a closed string whose holonomy is g

with respect to the indicated base-point and the trivialization coming from the beginning
of the open string. The corresponding map is ιg , with adjoint ιg .
There are also the two kinds of operation coming from internal critical points which
involve open strings. They are illustrated in fig. 49.
The map Cg ⊗ Oab → Oab corresponding to 21(i) is φ ⊗ ψ 7→ ρga (ιg (φ)ψ)), while the map
Oab ⊗ Ocd → Oad ⊗ Ocb corresponding to 21(ii) is
ψ ⊗ ψ ′ 7→

X

ρga (ψ)ψi ⊗ ρgc (ψ ′ )ρgb ga−1 (ψ i ),

where {ψi } is a basis of Obd .
We now have all the same verifications to make as in the non-equivariant case. They
are very tedious, but are in 1-1 correspondence with what we have already done, and
present nothing new. As an example of the modifications needed, let us point out that the
very frequently used formula A.1 which holds in any Frobenius category when φ′ ∈ Oab

and φi and φi are dual bases for Oab and Oba , generalizes — with the same proof — when

there is a G-action on the category to
X

φ′ φi ⊗ αg (φi ) =

for any g ∈ G.
We shall say no more about the proof.

85

X

φi ⊗ αg (φi φ′ )

<!-- page 87 -->
References
[1] C. Curtis and I. Reiner, Representation theory of finite groups and associative algebras,
AMS Chelsea, 2006
[2] Yu. A. Drozd and V.V. Kirichenko, Finite Dimensional Algebras Springer-Verlag 1994
[3] T. Banks, “TASI lectures on matrix theory,” arXiv:hep-th/9911068.
[4] W. Taylor, “M(atrix) theory: Matrix quantum mechanics as a fundamental theory,”
Rev. Mod. Phys. 73, 419 (2001) [arXiv:hep-th/0101126].
[5] E. Witten, “Overview of K-theory applied to strings,” hep-th/0007175.
[6] R. Dijkgraaf, A Geometrical Approach to Two-Dimensional Conformal Field Theory,
PhD Thesis, 1989
[7] S. Sawin, “Direct sum decompositions and indecomposable TQFTs,” J. Math. Phys.
36, 6673 (1995) [arXiv:q-alg/9505026].
[8] F. Quinn, “Lectures on axiomatic topological quantum field theory,” Given at Graduate Summer School on the Geometry and Topology of Manifolds and Quantum Field
Theory, Park City, Utah, 22 Jun - 20 Jul 1991
[9] G. Segal, Lectures at Stanford University and at ITP Santa Barbara, August 1999.
Available at http://doug-pc.itp.ucsb.edu/online/geom99/
[10] D. Lewellen, “Sewing constraints for conformal field theories on surfaces with boundaries,” Nucl.Phys. B372 (1992) 654; J.L. Cardy and D.C. Lewellen, “Bulk and boundary operators in conformal field theory,” Phys.Lett. B259 (1991) 274.
[11] I. Brunner and G. Moore, unpublished.
[12] A. Alexeevski and S. Natanzon, “Non-commutative extensions of two-dimensional
topological field theories and Hurwitz numbers for real algebraic curves,” arXiv:math.gt/0202164.
[13] I. Brunner and K. Hori, “Notes on orientifolds of rational conformal field theories,”
JHEP 0407, 023 (2004) [arXiv:hep-th/0208141].
[14] K. Hori and J. Walcher, “D-brane categories for orientifolds: The Landau-Ginzburg
case,” arXiv:hep-th/0606179.
[15] http://feynman.physics.lsa.umich.edu/cgi-bin/s2ktalk.cgi?moore
[16] G. W. Moore, “Some comments on branes, G-flux, and K-theory,” Int. J. Mod. Phys.
A 16, 936 (2001) [arXiv:hep-th/0012007].
[17] See http://online.itp.ucsb.edu/online/mp01
[18] Go to http://www.physics.rutgers.edu/∼gmoore/clay.html.
[19] C.I. Lazaroiu, “ Unitarity, D-brane dynamics and D-brane categories,” hep-th/0102183;
“Generalized complexes and string field theory,” hep-th/0102122; “Instanton amplitudes in open-closed topological string theory,” hep-th/0011257; “On the structure of
open-closed topological field theory in two dimensions,” hep-th/0010269.
[20] R.M. Kaufmann, “Orbifolding Frobenius algebras,” math.AG/0107163
86

<!-- page 88 -->
[21] E. Lupercio and B. Uribe, “Topological quantum field theories, strings, and orbifolds,”
arXiv:hep-th/0605255.
[22] D. Freed, “Higher algebraic structures and quantization”, Commun. Math. Phys., 159
(1994), 343–398; hep-th/9212115.
[23] D. Freed, “ K-theory in quantum field theory,” in Current Developments in Mathematics 2001, International Press, Somerville, MA, pp. 41-87; math-ph/0206031.
[24] E. Sharpe, “Quotient Stacks and String Orbifolds,” hep-th/0103008;“String Orbifolds and Quotient Stacks,” hep-th/010221;“ Stacks and D-Brane Bundles,”hepth/0102197; “Recent Developments in Discrete Torsion,” hep-th/0008191,“Discrete
Torsion,”hep-th/0008154
[25] K. Costello, “Topological conformal field theories and Calabi-Yau categories,” arXiv:math.qa/041214
[26] G. Segal, “Categories and cohomology theories,” Topology 13 (1974), 293
[27] D. Sullivan, “Infinitesimal computations in topology,” Inst. Hautes Études Sci. Publ.
Math. No. 47, 269–331 (1978).
[28] D. G. Quillen, “Rational homotopy theory”, Annals of Mathematics 90 (1969), 205295.
[29] M. A. Mandell, “Cochains and homotopy type”, math.AT/0311016.
[30] N. Seiberg and E. Witten, “String Theory and Noncommutative Geometry,” hepth/9908142,JHEP 9909 (1999) 032
[31] K. Hori, A. Iqbal, and C. Vafa, “D-Branes and Mirror Symmetry,” hep-th/0005247
[32] A. Kapustin and Y. Li, “D-branes in Landau-Ginzburg models and algebraic geometry,” JHEP 0312, 005 (2003) [arXiv:hep-th/0210296].
[33] D. Orlov, “Triangulated categories of singularities and D-branes in Landau-Ginzburg
models,” math.AG/0302304
[34] I. Brunner, M. Herbst, W. Lerche and B. Scheuner, “Landau-Ginzburg realization of
open string TFT,” arXiv:hep-th/0305133.
[35] A. Kapustin and Y. Li, “Topological correlators in Landau-Ginzburg models with
boundaries,” Adv. Theor. Math. Phys. 7, 727 (2004) [arXiv:hep-th/0305136].
[36] C. I. Lazaroiu, “On the boundary coupling of topological Landau-Ginzburg models,”
JHEP 0505, 037 (2005) [arXiv:hep-th/0312286].
[37] M. Herbst and C. I. Lazaroiu, “Localization and traces in open-closed topological
Landau-Ginzburg models,” JHEP 0505, 044 (2005) [arXiv:hep-th/0404184].
[38] A. Kapustin and L. Rozansky, “On the relation between open and closed topological
strings,” Commun. Math. Phys. 252, 393 (2004) [arXiv:hep-th/0405232].
[39] P. Ginsparg and G. Moore, Lectures on 2D Gravity and 2D String Theory, hepth/9304011;
in Recent Directions in Particle Theory, J. Harvey and J. Polchinski, eds., World Scientific, 1993.
[40] R. Dijkgraaf, H. Verlinde, and E. Verlinde, “Notes on topological string theory and 2D
quantum gravity,” Lectures given at Spring School on Strings and Quantum Gravity,
87

<!-- page 89 -->
[41]
[42]
[43]

[44]
[45]
[46]
[47]
[48]
[49]
[50]
[51]
[52]
[53]
[54]
[55]

Trieste, Italy, Apr 24 - May 2, 1990 and at Cargese Workshop on Random Surfaces,
Quantum Gravity and Strings, Cargese, France, May 28 - Jun 1, 1990.
R. Dijkgraaf, “Intersection theory, integrable hierarchies and topological field theory,”
arXiv:hep-th/9201003.
N. Seiberg and D. Shih, “Minimal string theory,” Comptes Rendus Physique 6, 165
(2005) [arXiv:hep-th/0409306].
M. Chas, and D. Sullivan, “ Closed string operators in topology leading to Lie bialgebras and higher string algebra,” The legacy of Niels Henrik Abel, 771–784, Springer,
Berlin, 2004.
E. Getzler, J. D. S. Jones, and S. Petrack, “Differential forms on loop space and the
cyclic bar complex,” Topology 30 (1991), 339-371.
E. Witten, “Mirror manifolds and topological field theory,” hep-th/9112056; in Essays
on Mirror Manifolds, S.-T. Yau ed. International Press, 1992
N. Markarian, “Poincaré-Birkhoff-Witt Isomorphism and Riemann Roch Theorem,”
unpublished.
A. Caldararu, “The Mukai pairing, I: the Hochschild structure,”math.AG/0308079;
“The Mukai pairing, II: the Hochschild-Kostant-Rosenberg isomorphism,” math.AG/0308080
V. Turaev, “Homotopy field theory in dimension 2 and group-algebras,” math.QA/9910010
M. R. Douglas and G. Moore, “D-branes, Quivers, and ALE Instantons,” hepth/9603167.
A. Konechny and A. Schwarz, “Introduction to M(atrix) theory and noncommutative
geometry,” hep-th/0012145.
E. Martinec and G. Moore, “ Noncommutative Solitons on Orbifolds,”hep-th/0101199
M. Atiyah and G. Segal, “Twisted K-theory and cohomology,” arXiv:math.kt/0510674.
R. Dijkgraaf, C. Vafa, E. P. Verlinde and H. L. Verlinde, “The Operator Algebra Of
Orbifold Models,” Commun. Math. Phys. 123, 485 (1989).
M. Douglas, “D-branes, Categories and N=1 Supersymmetry,” hep-th/0011017
P. Aspinwall, “A Note on the Equivalence of Vafa’s and Douglas’s Picture of Discrete
Torsion,” hep-th/0009045

88
