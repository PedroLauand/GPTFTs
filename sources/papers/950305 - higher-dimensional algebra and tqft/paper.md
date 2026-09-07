---
type: paper
date: 1995-03-05
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:q-alg/9503002v2)
reviewed: false
---

# Higher-dimensional Algebra and Topological Quantum Field Theory

Machine-generated and unreviewed text extraction of arXiv:q-alg/9503002v2
(36 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/q-alg/9503002v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Higher-Dimensional Algebra and
Topological Quantum Field Theory
John C. Baez and James Dolan
Department of Mathematics
University of California
Riverside CA 92521

arXiv:q-alg/9503002v2 6 Mar 2004

February 5, 1995
Abstract
The study of topological quantum field theories increasingly relies upon concepts from higherdimensional algebra such as n-categories and n-vector spaces. We review progress towards a
definition of n-category suited for this purpose, and outline a program in which n-dimensional
TQFTs are to be described as n-category representations. First we describe a ‘suspension’
operation on n-categories, and hypothesize that the k-fold suspension of a weak n-category
stabilizes for k ≥ n + 2. We give evidence for this hypothesis and describe its relation to stable
homotopy theory. We then propose a description of n-dimensional unitary extended TQFTs as
weak n-functors from the ‘free stable weak n-category with duals on one object’ to the n-category
of ‘n-Hilbert spaces’. We conclude by describing n-categorical generalizations of deformation
quantization and the quantum double construction.

1

Introduction

One important lesson we have learned from topological quantum field theory is that describing
dynamics using group representations is only a special case of describing it using category representations. In fact, examining the structure of the known n-dimensional topological quantum field
theories, it appears that many are representations of some sort of n-category. While a category is a
structure with objects and morphisms between these objects, in an n-category there are also ‘morphisms between morphisms’ or 2-morphisms, ‘morphisms between 2-morphisms’ or 3-morphisms,
and so on, up to n-morphisms. In the theory of manifolds, k-morphisms correspond to manifolds
(with boundary, corners, etc.) of dimension k.
The theory of n-categories is one of several related approaches to describing topology in purely
algebraic terms. Taken together, these constitute a subject known as ‘higher-dimensional algebra’.
While the basic insights of this subject are simple and beautiful, it is far from reaching its final
form. The aim of this paper is to paint, in rather broad strokes, a picture of some patterns that are
becoming apparent. In many cases these are only well-understood in low dimensions. The topology
of higher dimensions is known to be very different, so uncautious extrapolation is risky. Nonetheless,
the patterns we see so far should serve as a useful guide to research, if only to goad us to a better
understanding — and in particular, an algebraic understanding — of the relation between topological
quantum field theory and the traditional techniques of algebraic topology, which work in arbitrarily
high dimensions.
In the rest of this section we review some of the physics issues addressed by topological quantum
field theories (TQFTs), and recall the mathematical definition of a TQFT. In Section 2, we give a
sketchy overview of why n-categories should serve as a natural framework for an algebraic approach
to TQFTs. In Section 3 we recall the definition of a ‘strict n-category’, and in Section 4 we begin
to explain why a weakening of this notion is crucial — though only well-understood for n ≤ 3.
In Section 5 we describe how to ‘suspend’ an n-category, and argue that the process of iterated
suspension of an n-category should stabilize after n + 2 times. In Section 6 we recall the roots of
higher-dimensional algebra in algebraic topology, and explain how our notion of suspension relates

1

<!-- page 2 -->
to that in homotopy theory. In Section 7 we argue that an algebraic framework for smooth manifold
theory of dimension ≤ n is given by the ‘free stable n-category with duals on one object’. In Section
8 we then argue that a unitary extended n-dimensional TQFT is a representation of this n-category
in the n-category of ‘n-Hilbert spaces’. In Section 9 we conclude with some examples illustrating
the role of ‘quantization’ in higher-dimensional algebra. Since we wish to assume a minimum of
familiarity with the subject, we take a rather expository approach, and frequently refer the reader
to review articles and books rather than original papers. For this reason, our bibliography is by no
means complete.
Why are TQFTs interesting as physics? One reason is that they possess certain features one
expects of a quantum theory of gravity. This is not to say that quantum gravity is, or will be, a
TQFT. Nonetheless, to understand the significance of TQFTs, it is useful to recall some ideas from
quantum gravity.
The ‘general covariance’ or ‘diffeomorphism-invariance’ of general relativity is often regarded as a
crucial feature to be preserved, if possible, by any quantum theory accomodating gravity. However,
it has traditionally been a bit unclear what we really are asking for when we say we want a theory
to be generally covariant. In Einstein’s original work on general relativity [30], he emphasized that
the equations should preserve their form under arbitrary coordinate transformations: “The general
laws of nature are to be expressed by equations which hold good for all systems of coordinates, that
is, are covariant with respect to any substitutions whatever (generally covariant).”
Later, it became clear that this definition of general covariance is vacuous without some restriction on how the quantities involved in the laws transform under coordinate transformations. The
importance of tensors and their transformation rules is often stressed. In fact, requiring all the
quantities in a field theory to be tensors misses the point in at least two ways. On the one hand,
modern field theories typically make use of nontensorial objects such as spinor fields, connections,
and other bundle sections. (Note that connections can be regarded as bundle sections with the
aid of jet bundles.) On the other hand, special-relativistic classical field theories on Minkowski
space, which we normally do not think of as ‘generally covariant,’ can nonetheless be reformulated
as diffeomorphism-invariant, purely tensorial equations by coupling them to Einstein gravity, setting
the gravitational constant equal to zero, and then adding an extra equation saying that the metric
is flat!
Reflection along these lines led to the recognition that the key feature distinguishing general
relativity from previous theories is actually its lack of a fixed prior geometry. In the words of Misner,
Thorne and Wheeler [63], “By ‘prior geometry’ one means any aspect of the geometry of spacetime
that is fixed immutably, i.e., that cannot be changed by changing the distribution of gravitating
sources.” The best-known example of prior geometry is the Minkowski metric in special relativity.
In special-relativistic quantum field theory, dynamics is described in terms of representations of the
symmetry group of this metric, that is, the Poincaré group. Note that even in the diffeomorphisminvariant reformulation of special-relativistic field theory described above, there is, for each solution
of the equations of motion, a canonical choice of a subgroup of the diffeomorphism group isomorphic
to the Poincaré group: the isometry group of the metric.
More generally, while sufficient conditions for a theory to lack prior geometry are difficult to
state, it certainly seems necessary that there be no canonical way to choose, for each state of the
theory, a subgroup of the spacetime diffeomorphism group isomorphic to some fixed nontrivial Lie
group. For, by the Erlangen philosophy that a geometry is known by its group of symmetries, such
a subgroup would indicate the presence of prior geometry independent of the state. This, in turn,
suggests that in theories without prior geometry, dynamics will not be described in terms of the
representations of a Lie group of spacetime symmetries.
The question is then, how is dynamics described in such theories? This is known as the ‘problem
of time’. In canonical quantum gravity on a spacetime of the form R × S, it is manifested by the

2

<!-- page 3 -->
fact that physical states should satisfy the Wheeler-DeWitt equation
Hψ = 0,
expressing their invariance under the diffeomorphism group. This gives rise to the so-called ‘inner
product problem’, namely: what is the correct inner product on the space of states? In quantum
theories with prior geometry, the inner product is chosen so that spacetime symmetry group acts
unitarily on the space of states, but in a formalism where states are diffeomorphism-invariant the
inner product must be determined in some other way.
Many different approaches have been proposed to both these problems [3, 41], but here we only
consider one, namely Atiyah’s definition of a TQFT [4]. This is in fact a very radical approach!
First, rather than attempting to describe the dynamics of fields on a single spacetime manifold, a
TQFT describes the dynamics of fields in terms of a category in which the objects are (n − 1)dimensional manifolds representing possible choices of ‘space’, and morphisms are n-dimensional
cobordisms representing choices of ‘spacetime’. In fact, a TQFT is a kind of a representation of this
category, assigning a vector space of states to each object and a linear operator to each morphism.
Second, in any unitary TQFT satisfying a certain nondegeneracy condition, the structure of this
category automatically determines the inner product in the space of states for any (n − 1)-manifold.
To fully appreciate these ideas one must recognize that a group is just a very special sort of
category. Recall that a category consists of a collection of objects, and for any objects x and y, a set
hom(x, y) of morphisms from x to y. (Technically, we are considering only locally small categories.)
If f ∈ hom(x, y), we write f : x → y. Morphisms g: x → y and f : y → z can be composed to obtain
a morphism f g: x → z, and composition is associative. Moreover, for every object x there is a
morphism 1x : x → x acting as the identity for composition. It follows that all the structure of a
category with a single object x can be summarized by saying that hom(x, x), is a monoid: a set
equipped with an associative product and identity element. Loosely, we say that a category with
only one object is a monoid. Similarly, a category with only one object and all morphisms invertible
is a group.
Recall also that given two categories C and D, a functor F : C → D maps objects of C to objects
of D and morphisms of C to morphisms of D in a structure-preseving manner. In other words,
f : x → y implies F (f ): F (x) → F (y), and also F (f g) = F (f )F (g) and F (1x ) = 1F (x) . Thinking of a
group as a one-object category G, a group representation is thus just a functor from G to Vect, the
category whose objects are (finite-dimensional) vector spaces and morphisms are linear maps. This
leads us to define a ‘representation’ of a category C to be a functor from C to Vect.
An n-dimensional TQFT is a certain sort of representation of the category nCob of n-dimensional
cobordisms. This category has compact oriented (n − 1)-manifolds as objects, and oriented cobordisms between such manifolds as morphisms. Composition of cobordisms is given by gluing as shown
in Figure 1. The identity 1M for any object M is represented by the cylinder [0, 1] × M . In what
follows we will often abuse language and identify cobordisms with the manifolds with boundary
representing them, but it is important to keep in mind the distinction: for example, composition is
not strictly associative, but only associative up to equivalence, unless we treat cobordisms carefully
[67].

f

g

fg

◦

=

1. Composition in nCob

3

<!-- page 4 -->
A representation of nCob is thus a functor Z: nCob → Vect. The fact that Z assigns to the
cylindrical spacetime [0, 1] × M the identity on Z(M ), that is, the trivial time evolution operator,
corresponds to the Wheeler-DeWitt equation. The dynamics of the theory only becomes evident
upon considering nontrivial cobordisms.
The category nCob is not merely a category; it has extra structures in common with Vect, and
the definition of a TQFT requires that the functor Z: nCob → Vect preserve these extra structures.
In fact, these extra structures are important clues about the nature of higher-dimensional algebra.
First, both nCob and Vect are ‘monoidal’ categories. For precise definitions of this and other
terms from category theory, see Mac Lane [57]; roughly speaking, a category is monoidal if it has
tensor products of objects and morphisms satisfying all the usual axioms, and an object 1 playing
the role of identity for the tensor product. In nCob, the tensor product is given by disjoint union, as
shown in Figure 2, and the identity is the empty set. In Vect, the tensor product is the usual tensor
product of vector spaces, which has C as its identity. In a TQFT, the functor Z: nCob → Vect is
required to be ‘monoidal’, that is, to preserve tensor products and to send the identity object in
nCob to the identity object in Vect.
g

f

f ⊗g

⊗

=
2. Tensor product in nCob

Second, both nCob and Vect are ‘symmetric’ monoidal categories. In a symmetric monoidal
category, there is for any pair of objects x, y a natural isomorphism, the ‘braiding’,
Bx,y : x ⊗ y → y ⊗ x,
which is required to satisfy various axioms including the symmetry equation
By,x Bx,y = 1x⊗y .
In nCob, the symmetry Bx,y is a cobordism of the sort shown in Figure 3. In Vect, the symmetry
is the usual isomorphism of vector spaces x ⊗ y and y ⊗ x.

Bx,y

y
x
@@ ???  
@@ ??  
@@  
@ ?
 ????

  ???? ???
 
y
x

=

3. Symmetry in nCob
Third, both nCob and Vect are ‘rigid’ monoidal categories. These are monoidal categories in
which every object x has a ‘dual’ x∗ , and there are ‘unit’ and ‘counit’ maps
ix : 1 → x ⊗ x∗ ,

ex : x ⊗ x∗ → 1

4

(1)

<!-- page 5 -->
satisfying various axioms including the triangle identities, which say that the following diagrams
must commute:
1x
✲ x
x
✸
◗
✑
◗
✑
◗
✑
✑ 1x ⊗ex
ix ⊗1x ◗
◗
✑
◗
✑
s
x ⊗ x∗ ⊗ x
x∗

✲ x∗
◗
✸
✑
✑
◗
✑
◗
✑
1x∗ ⊗ix ◗
✑ ex ⊗1x∗
◗
✑
◗
s
◗
✑
x∗ ⊗ x ⊗ x∗
1x

(For ease of exposition, we demand one extra axiom besides the usual ones, namely that in the
symmetric case the natural morphism from x to x∗∗ corresponding to the ‘twist’ in Figure 31 be
the identity.) In nCob, x∗ is the manifold x equipped with the opposite orientation. The unit and
counit are the cylinders shown in Figure 4, where we also depict the triangle identities.

x∗
ex

x

=

ix

=
x∗

x

x

x∗

x

x∗

=
x

=
x∗

x

x∗

4. Unit, counit, and triangle identities in nCob
In short, a TQFT is a rigid symmetric monoidal functor X: nCob → Vect, that is, one preserving the rigid symmetric monoidal structure. Now the category Hilb, whose objects are (finitedimensional) Hilbert spaces and whose morphisms are linear maps, is also rigid symmetric monoidal.
A ‘unitary’ TQFT is a rigid symmetric monoidal functor Z: nCob → Hilb which is also compatible with a second sort of duality structure. The operation †: nCob → nCob taking each object
to itself and taking each cobordism f : x → y to the orientation-reversed cobordism f † : y → x is
a contravariant functor, that is, 1†x = 1x and (f g)† = g † f † . There is also a contravariant functor
†: Hilb → Hilb taking each object to itself and taking each linear map f : x → y to the Hilbert
space adjoint f † : y → x. A unitary TQFT must satisfy Z(f † ) = Z(f )† for all morphisms f . Given
cobordisms f and g from the empty set to x, the inner product of the vectors Z(f )1 and Z(g)1 is
then given by Z(f † g)1. If Z(x) is spanned by vectors of this form, the inner product in Z(x) is thus
determined by Z.
To conclude, it is crucial to note that Atiyah never propounded the notion of a TQFT as a
panacea for the problems of quantum field theories without prior geometry. Indeed, the TQFTs
we understand so far appear to reduce in the classical limit to field theories with no local degrees
of freedom, that is, for which all solutions are locally physically equivalent. One does not expect

5

<!-- page 6 -->
a realistic theory of quantum gravity to have this property. Indeed, while there are many clues
indicating that quantum gravity is closely related to known TQFTs [6], it may be an inherently
more complex sort of theory. Ideas from higher-dimensional algebra, however, may still be very
useful [5].

2

Cobordisms

While it is customary to begin in field theory by writing down a Lagrangian, the most efficient ways
to construct TQFTs tend to be algebraic in flavor. Since a TQFT is a rigid symmetric monoidal
functor from nCob to Vect, one can begin by describing nCob as a rigid symmetric monoidal category
in terms of generators and morphisms. Here the ‘generators’ are morphisms from which one can
obtain all the morphisms by the operations present: composition, tensor product, the symmetry,
and duals. Then, to actually construct a TQFT, one merely needs to assign objects and morphisms
in Vect to all of the generators of nCob, and check that the relations hold.
How does one determine generators and relations for nCob? Assuming momentarily that we
already understand the objects in nCob and their automorphisms, we can obtain generators for the
remaining morphisms using Morse theory [62]. A cobordism from M to M ′ can be represented as
an n-manifold N having boundary identified with M ∪ M . If we put a ‘height’ function on N — a
smooth real function F with F |M = 0 and F |M ′ = 1 — generically it will be a Morse function. That
is, it will have only nondegenerate critical points pi , occuring at distinct levels F (pi ) = ti . Slicing N
along level sets of F between the critical levels ti amounts to factoring our cobordism as a product
of simple ‘generating’ cobordisms, as shown in Figure 5.
Q
mmm QQQQQ
QQQ
mmm
m
m
QQQ
m
QmQmQm
QQQ
mmm
m
QQQ
mm
QQQ mmmmm
m
QQQ
m
m
QQQ
m
m
Q
QmmQmQ
QQQ
mmm
m
m
QQQ
m
QQQ mmmmm
m RRR
l
l
RRR
lll
RR
QlQlQl
QQQ
mmm
m
m
QQQ
m
QQQ mmmmm
m




5. Describing a cobordism using Morse theory
We can visualize the result as a ‘movie’ of N in which each ‘frame’ is obtained from the previous
one by attaching a j-handle — that is, cutting out a copy of Dn−j−1 × S j−1 and gluing in a copy of
S n−j × Dj — where j is the number of negative eigenvalues of the Hessian of F at the intervening
critical point. These basic processes are shown for n = 2 in Figure 6; the cases j = 0, 1, 2 are called
the birth of a circle, the death of a circle, and the saddle point, respectively.

•

•
•
6. Handle attachments for n = 2

6

<!-- page 7 -->
Of course, the manifold N admits many different Morse functions, so the cobordism it represents
can be expressed in many different ways as the product of a series of handle attachments. However,
given two Morse functions F0 and F1 , we can interpolate between them by a smooth family of
functions Fs . Generically, the functions Fs will be Morse functions except for finitely many values si
at which the level of one critical point passes another, two critical points coalesce, or a critical point
splits in two. The study of these generic paths between Morse functions is known as Cerf theory
[19, 50]. In the same sense as which handle attachments give generators for nCob, these paths
between Morse functions give relations, known as handle slides and cancellations. We can visualize
these as ‘movie moves’ going between two different movies of the same cobordism. An example of a
handle cancellation for the n = 2 case is shown in Figure 7.

=

7. A handle cancellation for n = 2
For the case n = 1 it is easy to use these ideas to give a purely algebraic description of nCob.
It is (up to the standard notion of equivalence of categories) just the free rigid symmetric monoidal
category on one object x! The object x corresponds to the positively oriented point. As shown in
Figure 8, the unit and counit
ix : 1 → x ⊗ x∗ ,

ex : x∗ ⊗ x → 1,

correspond to the two types of handle attachments, namely the birth and the death of an S 0 (a pair
of oppositely oriented points).
x∗
•
ix

=
•
x

=

ex

•
x∗

x
•

8. Handle attachments for n = 1
Similarly, as shown in Figure 9, the triangle identities correspond to handle cancellations.
x∗
•

x∗
•

x
•
=

=
•
x∗

x
•

•
x∗

•
x

9. Handle cancellations for n = 1

7

•
x

<!-- page 8 -->
This simple result indicates that the rigid symmetric monoidal structure captures all the essential
aspects of nCob for n = 1. It is tempting to seek similar purely algebraic presentations of nCob
in higher dimensions. For n = 2 we can achieve this using the principle of ‘internalization’. In its
simplest form, this amounts to the fact that any algebraic structure definable using commutative
diagrams in the category Set can be generalized to categories sufficiently resembling Set. For example, a monoid can be defined as an object x in Set equipped with a product m: x × x → x and
unit i: 1 → x making various diagrams commute. Here 1 denotes any one-element set, and we use
the standard trick of thinking of the identity element of x as the image of a map i: 1 → x. We can
generalize the definition to any monoidal category C, replacing × with the tensor product in C and
1 with the identity object of C, thus obtaining the notion of a ‘monoid object’ in C. For example,
a monoid object in Vect is an algebra. It turns out that 2Cob is the ‘free rigid symmetric monoidal
category on one commutative monoid object with nondegenerate trace’. The object in question is
S 1 , and the product, identity, and trace tr: S 1 → 1 are shown in Figure 10, This result yields a
complete classification of 2-dimensional TQFTs [26, 68].

m

=

i

=

tr

=

10. S 1 as a commutative monoid object with nondegenerate trace
Moving to higher dimensions, the best presentations of 3Cob for the purposes of constructing
TQFTs are based on the Kirby calculus [50, 66, 67]. While very algebraic in flavor, these have not
yet been distilled to a statement comparable to those for 1Cob and 2Cob. The Kirby calculus also
gives a description of 4Cob which has yielded a few TQFTs so far [15, 52]. For n ≥ 6 the theory
of cobordisms becomes more closely tied to homotopy theory, due to the h-cobordism theorem [61].
Also, while we will not go into it here, it is important to note the existence of a theory of piecewiselinear (PL) manifolds paralleling the smooth theory [10, 21, 23, 36, 64]. The smooth and PL versions
of nCob are equivalent for n ≤ 6, but not in general for larger n.
What we seek, however, is a unified algebraic framework for this entire collection of results,
one that applies to all dimensions and explains the fascinating relationships between results in
neighboring dimensions. Such a framework should clarify the existing TQFT constructions, which
appear at first to rely on miraculous analogies between topology and algebra, and it should aim at
a classification of TQFTs. We suggest that n-category theory will provide such a framework. The
reason is quite simple. We sketched how to go about a ‘generators and relations’ description of the
morphisms for nCob assuming we already had a description of the objects and their automorphisms,
but for higher n these grow more complicated to describe as well. Note however that in describing an
n-dimensional manifold as a ‘movie’, each ‘frame’, being an (n − 1)-manifold, can itself be regarded
a ‘movie’ of one lower dimension, as shown in Figure 11. In other words, each object in nCob gives
a morphism in (n − 1)Cob. A fully algebraic description of nCob should therefore involve objects,
morphisms between objects, 2-morphisms between morphisms, and so on, up to n-morphisms. We
may loosely call any such structure an n-category.

8

<!-- page 9 -->
ooOO

PPP
PPP
nnn
QnnQnQ
mm
QQQ
m
mm
QQQ
m
m
QQQ mmmm
m RRR
ll
RRR
l
l
l
RR
QlQlQl
QQQ
mmm
m
m
QQQ
m
QQQ mmmmm
m

/•
•

/•
•
/

/




/•
•
/

11. Frames as movies of one lower dimension
If we take the objects of our n-category to be 0-manifolds, and the morphisms to be 1-manifolds
with boundary, the most general sort of 2-morphism will be some kind of 2-manifold with corners,
as shown in Figure 12.
•
• q
,
k

/

•
•

0 •
•

o

•
•

12. 2-manifold with corners as 2-morphism between 1-manifolds with boundary
This is a considerable nuisance, since as n increases it becomes more and more difficult to specify
a precise class of ‘n-manifolds with corners’ and precise recipes for composing them. However, this
added complexity is of vital importance, since it permits the definition of an ‘extended’ TQFT,
one which behaves well under the extra cutting and pasting constructions available in this context.
Heuristic reasoning involving path integrals suggests that the TQFTs described in terms of local
Lagrangians should be of this extended sort, and so far this has been borne out in rigorous work on
important examples [32, 33, 54, 65, 72]. It is, in fact, the theory of extended TQFTs that provides
the best information about the relationship between higher-dimensional algebra and TQFTs.
We could at this point attempt to define ‘manifolds with corners’ more precisely, and define
composition operations on them. Various approaches have already been successfully pursued in the
work mentioned above. However, in order to get an idea of what a convenient formalism should
eventually look like, we prefer to turn to the theory of n-categories, and see what that suggests.

3

Strict n-Categories

Often when people refer to n-categories they mean what we shall call ‘strict’ n-categories. These
appear not to be sufficiently general for TQFT applications, but unlike the more general ‘weak’ ncategories, they have already been defined for all n. In what follows we briefly sketch this definition
and some of its implications, while in the next section we indicate the importance of weakening it
in certain ways. Readers familiar with strict n-categories can skip this section. In the rest of this
section we omit the qualifier ‘strict’.
The most elegant approach involves the theory of ‘enriched’ categories [47]. This is based on
the observation that in the definition of a category C, the category Set, whose objects are sets and
whose morphisms are functions, plays a distinguished role. The reason is that:

9

<!-- page 10 -->
For every pair of objects x, y in C there is a set hom(x, y) of morphisms, and for every triple of
objects x, y, z in C composition is a function ◦: hom(x, y) × hom(y, z) → hom(x, z).
Note also that the monoidal structure of Set, the Cartesian product ×, plays a role here. All the
rest of the category axioms can be written out as commutative diagrams in the category Set, and
all of these diagrams make sense in any monoidal category. Thus one can relativize the definition of
a category by letting an arbitrary monoidal category K play the role that Set does here. In other
words, a category C ‘enriched over K’, or ‘K-category’, is a collection of objects for which:
For every pair of objects x, y in C there is a object hom(x, y) in K, and for every triple of objects
x, y, z in C there is a morphism ◦: hom(x, y) ⊗ hom(y, z) → hom(x, z) in K.
One also demands that the usual axioms of a category hold, translated into commutative diagrams
in K.
A simple example is the category Vect, which is enriched over itself, or ‘closed’ [28]. That is, given
vector spaces x and y, the set hom(x, y) is actually a vector space, and composition ◦: hom(x, y) ⊗
hom(y, z) → hom(x, z) is actually a linear map. Another example is the category of modules over a
ring, which is enriched over the category of abelian groups.
This notion of enriched category permits a wonderful recursive definition of n-categories, as
follows. We say a category is ‘small’ if the collection of objects is a set. The category of all small
categories is denoted Cat — note that the ‘smallness’ condition prevents Russell-type paradoxes.
Now Cat is actually a monoidal category, with the identity 1 taken as any category with one object x
and one morphism 1x , and with the tensor product being the usual Cartesian product × of categories.
This product is an obvious generalization of the Cartesian product of sets, as shown in Figure 13.

•

•

S
•

•

•

•

•
S×T

T
•

•

•

•

+C
•

+•

•

•

+•

+•

•

•

+•

+•

C ×D

D

•

13. The Cartesian product of sets S and T , and of categories C and D
To be precise, the objects of C × D, written as x × y, are just ordered pairs consisting of an object x
of C and an object y of D. The morphisms of C × D can be described using generators and relations.
Given a morphism f : x → x′ in C and a morphism g: y → y ′ in D, there are morphisms
x × g: x × y → x × y ′ ,

f × y: x × y → x′ × y

in C × D. These are the generators; the relations say that
(f × y)(f ′ × y) = f f ′ × y,

(x × g)(x × g ′ ) = x × gg ′ ,

and very importantly, that diagrams of the following form commute:
x×y

✲ x′ × y

f ×y

x′ ×g

x×g

❄
x × y′

❄
✲ x′ × y ′ .

f ×y ′

10

(2)

<!-- page 11 -->
This implies that all the squares in Figure 13 commute.
The definition of (strict) n-categories is then as follows. 2-categories are simply categories enriched over Cat. The category 2Cat of small 2-categories, in turn, has a Cartesian product making
it into a monoidal category. This allows us to define 3-categories as categories enriched over 2Cat.
In general, nCat is defined as the category of small categories enriched over (n − 1)Cat, which is
monoidal when equipped with its Cartesian product. The Cartesian product at each stage is defined
by a generalization of the Cartesian product of categories to the enriched context [47].
For the reader dizzied by the rapid ascent up this recursive ladder, let us briefly pause to contemplate the case of 2-categories [49]. Here for any pair of objects x and y, hom(x, y) is a category. Objects in hom(x, y) should be thought of as morphisms from x to y, while the morphisms
in hom(x, y) should be thought of as ‘morphisms between morphisms’ or 2-morphisms. The 2morphisms are sometimes drawn as 2-dimensional surfaces labelled with double arrows; in Figure
14 we show objects x, y, morphisms f : x → y and g: x → y, and a 2-morphism α: f ⇒ g.
f
>
x•

•y

α


>
g

14. Diagram of a 2-morphism α: f ⇒ g
Given objects x, y in a 2-category C and morphisms f, g, h: x → y, we can compose 2-morphisms
α: g ⇒ h and β: f ⇒ g to obtain a 2-morphism αβ: f ⇒ h. This operation, which is really just
composition of morphisms in the category hom(x, y), is often called ‘vertical’ composition, for reasons
made clear by Figure 15.
f
>
β 
g
x •_ _ _ _>_ _ _ _• y
α



>
h

15. Vertical composition of 2-morphisms
On the other hand, given objects x, y and z, the composition functor from hom(x, y) × hom(y, z) to
hom(x, z), gives various other operations. Referring back to the definition of the Cartesian product
of categories, one sees that composition takes an object in hom(x, y) and one in hom(y, z) to one in
hom(x, z): this is how one composes 1-morphisms in C. Composition also takes an object in one of
these categories and a morphism in the other to a morphism in hom(x, z). This gives two ways to
compose a 1-morphism and a 2-morphism in C to obtain a 2-morphism, as shown in Figure 16.
g
>
f
x •_ _ _ _>_ _ _ _• y β



f
>

•z

x•

α



g
y •_ _ _ _>_ _ _ _• z

>
f′

>
g′

16. Composition of a 1-morphism and a 2-morphism

11

<!-- page 12 -->
Thanks to eq. (2), we can use these basic composition operations to define an operation called
‘horizontal composition’ of 2-morphisms, as shown in Figure 17. Given f, f ′ : x → y, g, g ′ : y → z,
α: f ⇒ f ′ and β: g ⇒ g ′ , the horizontal composite of α and β is a 2-morphism α ⊗ β: gf ⇒ g ′ f ′ .
g
>

f
>
x•

α



y•

β

>
f′

•z


>
g′

17. Horizontal composition of 2-morphisms
One can show that vertical and horizontal composition satisfy an ‘exchange identity’
(αα′ ) ⊗ (ββ ′ ) = (α ⊗ β)(α′ ⊗ β ′ )

(3)

making the diagram in Figure 18 define a unique 2-morphism. This makes it quite convenient to
define 2-morphisms diagrammatically by ‘pasting’ together diagrams, in a manner nicely mimicking
how one can paste together 2-manifolds with corners. This is the basic sense in which 2-categories
encode 2-dimensional topology.

>

>

β′ 
α′ 
•__ _ _>_ _ __•_ __ _>__ _ _•
α
β 

>
>

18. Exchange identity
Just as the primordial example of a category is Set, the primordial example of a 2-category
is Cat. We have already discussed Cat as a category in which the objects are small categories
and the morphisms are functors. Actually, however, Cat is a 2-category, in which given functors
F, G: C → D, the 2-morphisms from F to G are the ‘natural transformations’ α: F ⇒ G. Recall
that such a thing assigns to each object x of C a morphism αx : F (x) → G(x), in such a way that
for any morphism f : x → y in C, the consistency condition
F (x)

✲ G(x)

αx

F (f )

❄
F (y)

G(f )

(4)

❄
✲ G(y)

αy

holds.
While this example may seem abstract, it has a certain inherently geometrical character. A
functor F : C → D can be viewed as a diagram in D shaped liked C, and a natural transformation
α: F ⇒ G should then be viewed as a prism in D going between two such diagrams, as shown in
Figure 19.

12

<!-- page 13 -->
1•
F

1•

C
•

.

•

0•
D

α



.•

0

G


•


1•

0•

19. Natural transformation α between functors F, G: C → D
The consistency condition in the definition of a natural transformation says that the rectangular
‘vertical’ faces of this prism commute.
These remarks about 2-categories generalize considerably. In an n-category one has composition
operations that allow one to paste together n-morphisms according to a wide variety of ‘pasting
schemes’, much as one can glue together n-manifolds with corners [42]. Moreover, the primordial
example of an (n + 1)-category is nCat. The reason is simply that nCat is closed, i.e., enriched
over itself. That is, in addition to ‘n-functors’ between n-categories and ‘n-natural transformations’
between these, there are higher transformations between these which can be visualized using higherdimensional analogs of Figure 19. Given two n-categories C and D, we thus obtain an n-category
hom(C, D).

4

Weakening

One profound difference between a set and a category is that elements of a set are either equal or
not, while objects in a category can also be isomorphic in different ways (or not at all). Modern
mathematics and physics takes advantage of this insight in many ways. For example, the fact
that an object can admit nontrivial automorphisms is precisely what yields the notion of symmetry
group. However, it is primarily category theorists who have followed through on this insight with
the philosophy of ‘weakening’. As clearly enunciated by Kapranov and Voevodsky [46], this is based
on the principle that “In any category it is unnatural and undesirable to speak about equality of two
objects.” Instead, it is better whenever possible to speak in terms of isomorphisms between them.
For example, in the context of set theory, algebraic structures are frequently defined using equations. These structures can often be generalized to the context of category theory, but one has the
choice of generalizing them ‘strictly’ — keeping the equations as equations — or ‘weakly’ — replacing the equations by specified isomorphisms. When one opts to ‘weaken’ a definition in this way,
one typically demands that the isomorphisms themselves satisfy new equations, called ‘coherence
laws’, in order to manipulate them with some of the same facility as the original equations. For
example, a monoid is a set with a product that is required among other things to satisfy the equation
(xy)z = x(yz). The categorical analog of a monoid is a category with tensor product, or monoidal
category. Actually, though, monoidal categories come in two versions: strict, where the associativity
of the tensor product is given by an equation:
(x ⊗ y) ⊗ z = x ⊗ (y ⊗ z),
and ‘weak’, where instead there is a natural isomorphism, the ‘associator’:
Ax,y,z : (x ⊗ y) ⊗ z → x ⊗ (y ⊗ z).

13

<!-- page 14 -->
The associator allows one to rebracket iterated tensor products, but to make sure that any two
different paths of rebracketings have the same effect one must impose the ‘pentagon identity’, that
((x ⊗ y) ⊗ z) ⊗ w

✲ (x ⊗ y) ⊗ (z ⊗ w) Ax,y,z⊗w
✲ x ⊗ (y ⊗ (z ⊗ w))

Ax⊗y,z,w

✻
1x ⊗Ay,z,w

Ax,y,z ⊗1w

❄
(x ⊗ (y ⊗ z)) ⊗ w

Ax,y⊗z,w

✲ x ⊗ ((y ⊗ z) ⊗ w)

commutes. Similarly, in a weak monoidal category the equations 1x = x1 = x holding in a monoid
are replaced by isomorphisms satisfying coherence laws.
The monoidal categories that arise in nature, such as nCob and Vect, are usually weak. People
frequently ignore this fact, however (and the reader will note we did so in Section 1). The justification
for doing so is Mac Lane’s theorem [56] that any weak monoidal category is equivalent to a strict
one. However, the sense of ‘equivalence’ here is rather subtle and itself intimately connected with
weakening. Following Kapranov and Voevodsky’s principle, in addition to weakening algebraic
structures, one should also weaken the sense in which maps between them preserve the structure.
For example, the strictest notion of a ‘monoidal functor’ between monoidal categories would require
that it preserve tensor products ‘on the nose’. A weaker and often more useful notion, however,
requires merely that it preserve tensor products up to a natural isomorphism compatible with the
associativity constraints. It is this weaker notion which plays a role in the definition of ‘equivalence’
of monoidal categories.
Mac Lane’s theorem is an example of the ‘strictification’ theorems in higherdimensional algebra. These assert that any weakened algebraic structure of a given sort is equivalent to some stricter counterpart, in an appropriately weakened sense of ‘equivalence’. They simplify
certain computations by allowing us to consider a special class of cases without essential loss of generality.
However, in many situations weak notions are more general than their strict counterparts in
interesting ways. Also, there is a certain matter of choice involved in picking coherence laws, and
this can lead to different degrees of weakening. For example, one weakened categorical analog of a
commutative monoid is a symmetric monoidal category, the equation xy = yx having been replaced
by an isomorphism Bx,y : x ⊗ y → y ⊗ x satisfying various coherence laws including By,x Bx,y = 1x⊗y .
The stricter notion where commutativity remains an equation is too narrow to be very interesting.
However, a still weaker notion is very interesting, namely a ‘braided’ monoidal category, in which
the coherence law By,x Bx,y = 1x⊗y is dropped.
As the name suggests, braided monoidal categories are important in 3-dimensional topology [20,
34, 66]. A further ‘categorification’ of the notion of commutative monoid, namely a braided monoidal
2-category, appears to play a corresponding role in 4-dimensional topology [18, 46]. One goal of the
n-categorical approach to TQFTs is to systematically understand why weakened categorical analogs
of familiar algebraic structures are important in topology.
Perhaps the most fundamental candidate for weakening is the definition of n-category itself. In
the context of n-categories, Kapranov and Voevodsky’s principle indicates that it is undesirable to
speak of equality between two k-morphisms when k < n; instead, one should speak in terms of
(k + 1)-isomorphisms between them. One can unfold the recursive definition of strict n-category and
obtain a completely ‘explicit’ definition in terms of operations on k-morphisms, which are required
to satisfy various equations. Each equation presents an opportunity for repeated weakening. For
example, we can weaken an equation between k-morphisms by replacing it with a natural (k + 1)isomorphism and demanding that this new isomorphism satisfy coherence laws. We can weaken
further by replacing these coherence laws with (k + 2)-isomorphisms, which must satisfy their own

14

<!-- page 15 -->
coherence laws, and so on. This process becomes increasingly complex with increasing n, and so far
the definition of what might be called a ‘weak n-category’ has only been worked out for n ≤ 3.
In defining n-categories with n = 0 or 1 — i.e., in defining sets or categories — there is no
opportunity for weakening. Weak 2-categories are usually known as ‘bicategories’ [12], but there is a
strictification theorem saying that all of these are equivalent (or more precisely, biequivalent) to strict
2-categories. Weak 3-categories, or ‘tricategories’, have recently been developed by Gordon, Power,
and Street [37]. These are not all triequivalent to strict 3-categories, but there is a strictification
theorem saying they are triequivalent to ‘semistrict 3-categories’. These are categories enriched over
2Cat thought of as a monoidal category not with its Cartesian product, but with a weakened product
similar to that defined by Gray [38]. In this ‘semistrict’ tensor product, eq. (2) is dropped, and
instead there is only a natural 2-isomorphism between the left- and right-hand sides. Topologically
this is very natural, since it means that the squares in Figure 20, rather than commuting, are ‘filled
in’ with 2-isomorphisms.

+C
•

•
•

•

•

•

D

vv
v~ vvvv

+•
6>

+•

+•
vv
v~ vvvv

+
6> •

C⊗D

+•

20. The semistrict tensor product of 2-categories
To advance further in n-category theory, it is urgent to define ‘weak n-categories’ for all n. It
is clear that new ideas are needed to do so without a combinatorial explosion, since already the
explicit definition of a tricategory takes 6 pages, and that of a triequivalence 13 pages! However,
the potential payoffs of a good theory of weak n-categories should encourage us to persevere.
Having completed our brief survey of n-category theory, let us return to topological quantum
field theory. In what follows, we propose answers to the basic questions: Of which n-category are
n-dimensional extended TQFTs representations? and In what sense is an n-dimensional extended
TQFT a representation of this n-category? Our answers are inevitably somewhat vague, except for
low n, since they rely on notions from the theory of weak n-categories. Nonetheless, we hope they
will serve as a guide for future research.

5

Suspension

To begin, it is useful to consider an issue that might at first seem of purely formal interest. Suppose
we have an (n + 1)-category C with only one object x. We can regard C as an n-category C̃ by
re-indexing: the objects of C̃ are the morphisms of C, the morphisms of C̃ are the 2-morphisms of C,
and so on. However, the n-categories we obtain this way will have extra structure. For example, since
the objects of C̃ were really morphisms in C from x to itself, we can multiply (i.e., compose) them.
We have already seen the simplest example of this phenomenon in Section 1: if C is a category with
a single object, C̃ is a monoid. If instead we start with a strict (resp. weak) 2-category with a single
object, we obtain a strict (resp. weak) monoidal category! Similarly, starting with strict, semistrict,
or weak 3-categories with only one object, we obtain corresponding sorts of monoidal 2-categories,
i.e., 2-categories having tensor products of objects, morphisms, and 2-morphisms [37, 46].
We can iterate this process, and construct from an (n + k)-category C with only one object,
one morphism, and so on up to one (k − 1)-morphism, an n-category C̃ whose j-morphisms are
the (j + k)-morphisms of C. In doing so we obtain a particular sort of n-category with extra
structure and properties, which we call a ‘k-tuply monoidal’ n-category. In Figure 21 we tabulate

15

<!-- page 16 -->
our best guesses concerning k-tuply monoidal n-categories. Ultimately we expect a table along these
lines for weak k-tuply monoidal n-categories. For the moment, however, we work with ‘semistrict’
ones, which have already been defined in a few cases where the weak ones have not. The idea is
that strictification theorems are either known or expected saying that all weak k-tuply monoidal
n-categories are equivalent (in a suitable sense) to these semistrict ones.
More precisely, for the n = 0 and n = 1 columns we define the semistrict notions to be the
same as the strict ones. In the n = 2 column, we define semistrict 2-categories to be strict ones,
while semistrict monoidal and braided monoidal 2-categories have been defined by Kapranov and
Voevodsky [46]. Semistrict weakly and strongly involutory monoidal 2-categories have been discussed
by Breen [14]. Semistrict 3-categories, mentioned in the previous section, have been studied by
Gordon, Power and Street [37] and Leroy [55].

k=2

commutative
monoids

k=3

‘’

k=4

‘’

n=1
categories
monoidal
categories
braided
monoidal
categories
symmetric
monoidal
categories
‘’

k=5

‘’

‘’

k=0
k=1

n=0
sets
monoids

n=2
2-categories
monoidal
2-categories
braided
monoidal
2-categories
weakly involutory
monoidal
2-categories
strongly involutory
monoidal
2-categories
‘’

21. Semistrict k-tuply monoidal n-categories
There are many interesting patterns to be seen in this table. First, it is clear that many of
the concepts already discussed appear in this table, together with some new ones. Second, as we
proceed down any column of this table, the n-categories in question first gain additional structures,
which then acquire additional properties of an ‘abelian’ nature. This process appears in its most
rudimentary form in the first column. We have already seen that a category with only one object x
is essentially the same as the monoid hom(x, x). Why does a 2-category C with only one object x
and one morphism 1x give a commutative monoid hom(1x , 1x )?
The argument goes back at least to Eckmann and Hilton [27]. The elements of hom(1x , 1x )
are the 2-morphisms of C, and as described in our brief review of 2-categories, we can compose
α, β: 1x ⇒ 1x either vertically or horizontally to obtain a new 2-morphism from 1x to 1x . We write
the vertical composite as αβ and the horizontal composite as α ⊗ β. Writing simply 1 for 11x , with
a little work one can check that 1 ⊗ α = α ⊗ 1 = α, so that 1 is the identity for both vertical and
horizontal composition. One also has the exchange identity (αα′ ) ⊗ (ββ ′ ) = (α ⊗ β)(α′ ⊗ β ′ ) from
eq. (3). These two facts let us perform the remarkable computation:
α⊗β

= (1α) ⊗ (β1)
= (1 ⊗ β)(α ⊗ 1)
= βα
= (β ⊗ 1)(1 ⊗ α)
= (β1) ⊗ (1α)
= β ⊗ α,

16

(5)

<!-- page 17 -->
so vertical and horizontal composition are equal and hom(1x , 1x ) is a commutative monoid. Conversely, one can show that any commutative monoid can be thought of as the 2-morphisms in a
2-category with one object and one morphism.
When we consider a semistrict 3-category with one object x, one morphism 1x , and one 2morphism 11x , it turns out that these are again essentially just commutative monoids. The same appears to be true for semistrict 4-categories with only one 3-morphism. While semistrict 4-categories
are not understood in general, it seems that those with only one morphism are, these being braided
monoidal 2-categories, and one can check that of these, those with only one 3-morphism are commutative monoids. Of course this argument is somewhat circular, since it assumes we understand
one column of the table in order to check another, but it serves as a interesting cross-check. In any
event, it appears that the n = 0 column stabilizes after two steps.
The same sort of process is at work in the next two columns, in increasingly sophisticated
incarnations. The basic pattern is shown in Figure 22.
k=0
k=1
k=2
k=3
k=4

n=0
sets
xy
xy = yx
‘’
‘’

n=1
categories
x⊗y
Bx,y : x ⊗ y → y ⊗ x
−1
Bx,y = By,x
‘’

n=2
2-categories
x⊗y
Bx,y : x ⊗ y → y ⊗ x
−1
Ix,y : Bx,y ⇒ By,x
−1 −1
Ix,y = (Iy,x )hor

22. Semistrict k-tuply monoidal n-categories: structure and properties
In the n = 0 column we began with sets, which then acquired a product, which then satisfied the
commutativity equation xy = yx. In the n = 1 we begin with categories, which permit a more
nuanced version of the process: first they acquire a product, then they acquire an isomorphism
Bx,y : x ⊗ y → y ⊗ x, taking the place of the commutativity equation. Finally, the braiding is
−1
required to satisfy an equation of its own, the symmetry equation Bx,y = By,x
. Note that what was
a property (commutativity) has become structure (the braiding), which then acquires an analogous
property of its own (symmetry).
In the n = 2 column a still more subtle version of the ‘abelianization’ process occurs. We
begin with 2-categories. These first acquire a product, then a braiding isomorphism, and then a
−1
2-isomorphism Ix,y : Bx,y ⇒ By,x
, the ‘involutor’, taking the place of the symmetry equation. In the
−1 −1
last step, the involutor satisfies an equation of its own, Ix,y = (Iy,x
)hor , meaning that the horizontal
−1
composite of Ix,y and Iy,x is the identity. One can also think of both sides of the equation as 2−1
isomorphisms from Bx,y to By,x
. We give a topological interpretation of this equation in Section
7.
The pattern here is evident, at least in outline, and it is tempting to predict that it continues for
higher n. In particular, we can guess that each column will take one step longer to stabilize. A bit
more precisely, let nCatk denote the category of k-tuply monoidal weak n-categories. There should
be a forgetful functor
F : nCatk → nCatk−1 ,
and a corresponding ‘reverse’ functor, technically a left adjoint
S: nCatk−1 → nCatk ,
which we shall call ‘suspension’ (for reasons to become clear shortly). For example, when we repeatedly suspend a set C, we obtain first the free monoid on C, and then the abelianization thereof.
Similarly, when we repeatedly suspend a category C, we obtain first the free monoidal category on
C, then the free braided monoidal category on C, and then the symmetrization thereof. We propose
the:

17

<!-- page 18 -->
Stabilization Hypothesis. After suspending a weak n-category n + 2 times, further suspensions
have no essential effect. More precisely, the suspension functor S: nCatk → nCatk+1 is an equivalence of categories for k ≥ n + 2.
We could also embellish this hypothesis by considering nCatk not merely as a category but as
(n + k + 1)-category, and using not equivalence but some notion of ‘(n + k + 1)-equivalence’.
One can regard the above hypothesis, and those to follow, either as a conjecture pending a general
definition of ‘weak n-category’, or as a feature one might desire of such a definition. Apart from
the already given algebraic evidence for the stabilization hypothesis, there is quite a bit of indirect
topological evidence from homotopy theory and the theory of tangles. The latter leads us back to
our goal: understanding topological quantum field theory in n-categorical terms.

6

Homotopy Theory

Modern higher-dimensional algebra has it roots in the dream of finding a natural and convenient
completely algebraic description of the homotopy type of a topological space. The prototype here
is the fundamental groupoid; given a space X, this is the category Π1 (X) whose objects are the
points of X and whose morphisms are the homotopy classes of paths (with fixed endpoints). This is
a groupoid, meaning that every morphism has an inverse, given by reversing a path from x to y to
obtain a path from y to x. In fact, Π1 gives an equivalence between the category of groupoids and
the category of ‘homotopy 1-types’, where, roughly speaking, two spaces define the same homotopy
n-type if they are equivalent as far as concerns homotopy classes of maps from n-dimensional CW
complexes into them.
The goal of generalizing the fundamental groupoid to higher dimensions has led to a variety of
schemes. One of the most popular involves Kan complexes [60], which model a space by an algebraic
analog of a simplicial complex. Alternative approaches based on cubes have been developed by
Brown, Higgins, Loday and others [16]. Indeed, it was in this context that Brown first coined the
term ‘higher-dimensional algebra’.
Here, however, we restrict our attention to n-categorical approaches. Ever since Grothendieck’s
famous 600-page letter to Quillen [39], it has been tempting to associate to a space X a ‘fundamental
n-groupoid’ Πn (X), some sort of n-category whose objects are points, whose morphisms are paths,
whose 2-morphisms are paths between paths, and so on up to the n-morphisms, which are homotopy
classes of n-fold paths. This amounts to taking the imagery of n-category theory quite literally, as
in Figure 23, where we show a typical 2-morphism.

>

•


•

>

23. A 2-morphism in the fundamental n-groupoid
Roughly speaking, an n-groupoid should be some sort of n-category in which all k-morphisms
(k ≥ 1) have inverses, at least weakly. There are good reasons to want to use weak n-categories here.
In the fundamental groupoid, composition is associative, since the morphisms are merely homotopy
classes of paths. In the fundamental 2-groupoid, however, composition of paths f : [0, 1] → X is not
strictly associative, but only up to a homotopy, the associator, which performs the reparametrization
of [0, 1] shown in Figure 24.

18

<!-- page 19 -->
(f g)
h
66
66
66
66
66
66
66
66
66
66
(gh)

f

24. The associator in homotopy theory
In the fundamental 2-groupoid, the associator satisfies the pentagon identity ‘on the nose’, but in
higher fundamental n-groupoids it does so only up to a homotopy, which in turn satisfies a coherence
condition up to homotopy, and so on. In fact, the whole tower of these ‘higher associativity laws’
was worked out by Stasheff [69] in 1963, and have an appealing geometrical description as faces of
the ‘associahedron’. For example, the pentagon, being a 2-morphism, is a 2-dimensional face. One
expects these higher associativity laws to play a crucial part in the definition of weak n-categories,
as indeed they do in the cases understood so far (n ≤ 3). Similar remarks hold for the identity law
[37] and for the inverses.
Of course, one expects strictification theorems saying that ‘weak n-groupoids’ are all ‘n-equivalent’
to some better-behaved class of n-groupoids, implying that the latter are sufficient for homotopy
theory. There are, in fact, two distinct strands of progress along these lines. First, the category
of homotopy 2-types has been shown equivalent to a category whose objects are strict 2-categories
having strict inverses for all k-morphisms [17, 58]. Moreover, the category of homotopy 3-types has
been shown equivalent to a category whose objects are semistrict 3-categories having strict inverses
[44, 55]. This naturally suggests the possibility that homotopy n-types might be equivalent to some
sort of semistrict n-categories having strict inverses. Second, for all n the category of homotopy
n-types has been shown equivalent to a category whose objects are strict n-categories having a particular sort of ‘weak inverses’ [45]. We see here a kind of tradeoff that would be nice to understand
better.
In any event, while the correspondence between homotopy n-types and ‘weak n-groupoids’ is still
incompletely understood, it is already very valuable, since it sets up an analogy between topological
spaces and n-categories that lets us import techniques and insights from topology into higherdimensional algebra. In what follows we use this analogy to shed some light on the stabilization
hypothesis of the previous section.
First, the topologically minded reader might already have noticed that the n = 0 column of
Figure 21 — sets, monoids, and commutative monoids thereafter — is familiar from homotopy
theory. Typically in homotopy theory one works with spaces with basepoint, and defines πk (X) to
be the set of homotopy classes of based maps from S n to X. For k = 0, πk (X) is indeed just a
set, while for k = 1 it is a group, and for k ≥ 2 it is an abelian group. These facts can be seen as
consequences of Figure 21 together with the correspondence between homotopy n-types and weak
n-groupoids, but historically, of course, they were discovered first.
In particular, the Eckmann-Hilton argument given in eq. (5) is just the algebraic distillation of
a very topological proof that π2 is abelian. We illustrate the key steps of eq. (5) in Figure 25. Here
each rectangle is labelled with a map from the rectangle to some space X, mapping the boundary
to the basepoint of X. Such a map can be thought of as a based map from S 2 to X, defining an
element of π2 (X). In Figure 25, α and β represent arbitrary based maps from S 2 to X, while 1
represents the trivial map sending all of S 2 to the basepoint of X. Such maps can be either vertically
or horizontally composed by juxtaposition. and the figure shows successive frames in a movie of a
homotopy from α ⊗ β to β ⊗ α, proving that π2 (X) is abelian. The same sort of argument shows
that πk (X) is abelian for all k ≥ 2.

19

<!-- page 20 -->
α

β

α⊗β

α

1

α

1

α

1

β

β

β

1

(1⊗β)(α⊗1)

(β⊗1)(1⊗α)

βα

β

α

β⊗α

25. The Eckmann-Hilton argument
Figure 25 also clarifies how, when we proceed from the n = 0 to the n = 1 column in Figure
21, the commutativity equation is weakened to a braiding isomorphism. In π2 (X), homotopic maps
from S 2 to X are decreed to be equal. In a more refined context, however, we could regard the
homotopy as an isomorphism. In Figure 26 we depict the homotopy from α ⊗ β to β ⊗ α given by
the Eckmann-Hilton argument as a map from the cube to X, whose horizontal slices give the frames
of the movie shown in Figure 25. (Here we have compressed α and β to small discs for clarity;
everything outside these discs is mapped to the basepoint of X.) One can see that this homotopy is
precisely a braiding!
 α  β 








α

β






26. Braiding Bα,β : α ⊗ β → β ⊗ α
In particular, an alternate version of the Eckmann-Hilton argument:
α⊗β

= (α1) ⊗ (1β)
= (α ⊗ 1)(1 ⊗ β)
= αβ
= (1 ⊗ α)(β ⊗ 1)
= (1β) ⊗ (α1)
= β ⊗ α,

−1
gives another homotopy from α ⊗ β to β ⊗ α, corresponding to Bβ,α
, as shown in Figure 27.

 α  β 







α

β






−1
27. Bβ,α
:α⊗ β → β ⊗ α

These two homotopies are not generally homotopic to each other, corresponding to the fact that
−1
generally Bα,β 6= Bβ,α
in a braided monoidal category. This is a good example of how different
proofs of the same equation may, upon weakening, give rise to distinct isomorphisms.
Algebraically, the point here is that the Eckmann-Hilton argument relies on the interplay between
horizontal and vertical composition of 2-morphisms in 2-categories. For the definition of horizontal

20

<!-- page 21 -->
composition given in Figure 17 to be unambiguous, we needed the commuting square condition, eq.
(2), in the definition of the Cartesian product of categories. In the context of semistrict 3-categories
this equation is weakened to an isomorphism, as shown in Figure 20, so Figure 17 gives two distinct
notions of horizontal composition of 2-morphisms, related by a 3-isomorphism. Arbitrarily picking
one of these, and recapitulating the Eckmann-Hilton argument in this context, one finds that instead
of an equation between α ⊗ β and β ⊗ α, one has a 3-isomorphism, the braiding.
Lest the reader think we have drifted hopelessly far from physics by now, we should note that
elements of π2 (X) correspond to ‘topological solitons’ in a nonlinear sigma model with target space
X, for a spacetime of dimension 3. In this context, Figures 26 and 27 show the worldlines of such
topological solitons, and the fact that the two pictures cannot be deformed into each other is why the
statistics of such solitons is described using representations of the braid group [8]. In a spacetime of
dimension 4 or more, the analogous pictures can be deformed into each other, since there is enough
room to pass the two strands across each other. Topologically, this means that the two homotopies
from α ⊗ β to β ⊗ α are themselves homotopic when α, β represent based maps from S k to X for
k ≥ 3. Algebraically, this corresponds to moving down in Figure 21 from braided monoidal categories
−1
to symmetric monoidal categories, where one has Bα,β = Bβ,α
. Physically, this is why the statistics
of topological solitons in spacetimes of dimension 4 or more is described using the symmetric group.
Having discussed the n = 0 and n = 1 columns of Figure 21 from the viewpoint of homotopy
theory, we could proceed to the n = 2 column, but instead let us explain the general pattern and
what it has to do with the stabilization hypothesis. In fact, the ‘suspension’ operation on n-categories
is closely modelled after homotopy theory. In topology, one obtains the ‘suspension’ SX of a space
X with basepoint ∗ as a quotient space of X × [0, 1] in which one collapses all the points of the form
(x, 0), (x, 1), and (∗, t) to a single point. We can draw this as in Figure 28, with the proviso that all
the points on the dotted line are identified.

X

•99
 999

99


SX 99
99 ∗

99 
9 
•

∗

28. Space X and its suspension SX
In fact, suspension is a functor, so a map f : X → Y gives rise to a map Sf : SX → SY , and one
obtains thereby a sequence
[X, Y ]

S

✲ [SX, SY ]

S ✲

[S 2 X, S 2 Y ]

S

✲ ···

where [X, Y ] denotes the set of homotopy classes of maps from X to Y . Moreover, if X is a CW
complex of dimension n, this sequence stabilizes after n + 2 steps, i.e., the map
S: [S k X, S k Y ] → [S k+1 X, S k+1 Y ]
is an isomorphism for k ≥ n + 2. This theorem is the basis of stable homotopy theory, a subject with
close ties to higher-dimensional algebra [1]. Given the conjectured relation between homotopy ntypes and weak n-groupoids, one expects this theorem to translate into a proof of our stabilization
hypothesis in the special case of weak n-groupoids. Roughly speaking, the idea is that when we
suspend X, an k-morphism in the fundamental n-groupoid of X gives a (k + 1)-morphism in the
fundamental (n + 1)-groupoid of SX in a manner analogous to the algebraic notion of suspension
described in Section 5. In Figure 29, for example, we show how a point of X gives a loop in SX,
and how a path in X gives a path between loops in SX.

21

<!-- page 22 -->
X

•

x

f

•';
 '' ;;;


Sx 'Sy ;
  '' ;;;

 '

SX ;;  Sf +3 '' 
;; -
;; -  
;;-- 
•

0•

y

29. Suspending k-morphisms in the fundamental n-groupoid of a space X
For readers comfortable with homotopy theory we can make this a bit more precise as follows.
Let nHotk denote the category of pointed (k − 1)-connected homotopy n + k-types for k ≥ 1, or just
homotopy n-types for k = 0. Then we can think of suspension as a functor S̃: nHotk → nHotk+1 ,
where we take the reduced suspension for k ≥ 1, while for k = 0 we first adjoin a basepoint and
then take the reduced suspension. Now suppose we have an equivalence Π: nHotk → nGpdk to
some category of weak n-groupoids, with adjoint given by a functor N : nGpd → nHot, where N is
obtained by composing a kind of ‘nerve’ functor with ‘geometrical realization’. One expects that
the n-categorical suspension functor of the previous section yields one for weak n-groupoids, say
S: nGpdk → nGpdk+1 , where nGpdk denotes the category of k-tuply monoidal weak n-groupoids,
and that S is equivalent to N S̃Π. If this is so, the stabilization result from homotopy theory should
imply that S is an equivalence for k ≥ n + 2. This argument also makes it clear that the forgetful
functor from nCatk to nCatk−1 is analogous to looping in homotopy theory [46].

7

Tangles

Now let us venture an answer to the question: Of which n-category are n-dimensional extended
TQFTs representations? Recall from Section 2 that we expect this to be an n-category in which
the objects are 0-manifolds, the morphisms are 1-manifolds with boundary, the 2-morphisms are 2manifolds with corners, and so on. These should all be oriented, but experience with 3-dimensional
TQFTs has shown that it may be convenient to equip them with some extra structure as well, a
kind of ‘framing’. One could attempt to make this more precise and give an explicit description of
the resulting n-category in terms of generators and relations. Instead, we try to isolate the crucial
algebraic properties of this n-category, and hypothesize that it is in fact the universal n-category
with these properties. We have already seen that a key feature of the n-categories appropriate for
homotopy theory is the presence of inverses. Here we wish to argue that the corresponding feature
of the n-category of which extended TQFTs are representations is the presence of duals. Of course,
both ‘inverses’ and ‘duals’ may need to be understood in an appropriately weakened sense.
We have already seen two levels of duality in the definition of a unitary TQFT. First, in nCob
each object x is an oriented (n−1)-manifold, and its dual x∗ is the same manifold with its orientation
reversed. Second, each morphism f : x → y is an oriented n-manifold with boundary, and its dual
f † : y → x is the same manifold with its orientation reversed. It is important to note that the dual
morphism f † : y → x is different from the ‘adjoint’ morphism f ∗ : y ∗ → x∗ given by the composite
y∗

⊗1 ∗
✲ y ∗ ⊗ x ⊗ x∗ 1⊗f✲
y ⊗ y ⊗ x∗

1⊗ix

✲ x∗ .

ey ⊗1

The notion of adjoint morphism is derived from duality on objects, but the notion of dual morphism
is conceptually independent. Presumably this is just the tip of the iceberg: in the n-categorical
formulation of the theory of cobordisms there should be n+1 distinct levels of duality, corresponding
to orientation reversal for j-manifolds with corners for all 0 ≤ j ≤ n.
Indeed, while the details have only been worked out in special cases, it seems that there should
be a general notion of a k-tuply monoidal n-category ‘with duals’. Such a structure should have

22

<!-- page 23 -->
n + 1 duality operations, allowing us to take duals of j-morphisms for all 0 ≤ j ≤ n. For the moment
let us denote all these duality operations with the symbol ⋆ . For j > 0 the dual of a j-morphism
f : x → y is a j-morphism f ⋆ : y → x, while the dual of a 0-morphism, or object, is simply another
object. For all 0 < j < n there should be an associated unit and counit
if : 1 y → f f ⋆ ,

ef : f ⋆ f → 1 x ,

satisfying the triangle identities, probably in a weakened sense. Note that for n-morphisms there
cannot be a unit and counit since there are no (n + 1)-morphisms. Also, there can only be a unit
and counit for objects in the presence of a monoidal structure, that is, if k ≥ 1. In this case, if
we write the monoidal structure as a tensor product, the unit and counit for object take the usual
forms as in eq. (1). Other properties we expect of duality are f ⋆⋆ = f, and (f g)⋆ = g ⋆ f ⋆ whenever
the j-morphisms f, g can be composed.
Since the precise axioms for a k-tuply monoidal n-category ‘with duals’ have only been formulated
in certain semistrict cases, let us go through them one by one. We shall pay special attention to the
example of the free semistrict k-tuply monoidal n-category with duals on one object. We denote this
n-category by Cn,k and the generating object by x. We hypothesize that the weak analog of this
n-category has a special significance for topological quantum field theory:
Tangle Hypothesis. The n-category of framed n-tangles in n + k dimensions is (n + k)-equivalent
to the free weak k-tuply monoidal n-category with duals on one object.
The sort of tangle studied in knot theory is what we would call a 1-tangle in 3 dimensions, shown
in the n = 1, k = 2 entry of Figure 30 below. By an n-tangle in n + k dimensions we intend a
generalization of this concept, roughly speaking an n-manifold with corners embedded in [0, 1]n+k
so that the codimension j corners of the manifold are mapped into the subset of [0, 1]n+k for which
the last j coordinates are either 0 or 1. By a ‘framing’ of an n-tangle we mean a homotopy class
of trivializations of the normal bundle. (Such a framing, together with the standard orientation on
[0, 1]n+k , determines an orientation on the submanifold.)

23

<!-- page 24 -->
n=0

n=1

n=2
x
•

•x
x∗
•

k=0



x x∗ x
• • •

k=1



•x

•
x

x x∗ x
• L• •






 • z •
x∗ x

•
x
x
•
k=2

k=3

k=4

x∗
•
x
•





x

•

• x∗

x

•






 x∗

x
 x •7[77 • 

• 7  


 


x 


•

4d


x
 x x∗


•
•
•
O







• x∗
















x

•

5d

 x ∗
x

x


 • •O
•






x

•






x

•








•
x
x∗ x
• = • 




5d


 








/

• vv•


zvvv
r
9
v

r
r v

•∗r •v
x
x
4d










x

•

4d






x
/






6d


 






















30. Examples of n-morphisms in Cn,k , drawn as n-tangles in n + k dimensions
Implicit in the tangle hypothesis is that there should be a weak n-category whose n-morphisms
are suitably defined isotopy classes of n-tangles in n + k dimensions. The precise definition of ‘ntangles’ and ‘isotopy classes’ for this purpose is only well-understood for n = 1, and only beginning
to be understood for n = 2. In what sense should isotopy classes of n-tangles in n + k dimensions be
the n-morphisms in an n-category? Roughly, a j-morphism f : x → y in this n-category should be a
certain equivalence class of j-tangles in [0, 1]j+k , going from the equivalence class x of (j − 1)-tangles
in [0, 1]j+k−1 × {0} to the equivalence class y of (j − 1)-tangles in [0, 1]j+k−1 × {1}. The duality
operation on j-tangles corresponds to reflection of [0, 1]j+k about the last coordinate axis.
Clearly much remains to be made precise here. Rather than continuing to speak in generalities,
let us describe what is known so far in various special cases. This should also be the best way of
illustrating the significance of the k-tuply monoidal structure.

24

<!-- page 25 -->
We begin with n = 0 column of Figure 30. Here there is just one level of duality to consider,
which we denote by ∗. For k = 0, a k-tuply monoidal n-category C is just a set. A set ‘with
duals’ is simply one equipped with an involution, that is, a function ∗: C → C with x∗∗ = x for all
x. Thus C0,0 is the free set with involution on one object x, namely the two-element set {x, x∗ }.
Now for k > 0, a framing of a 0-dimensional submanifold of [0, 1]k is equivalent to an orientation,
so in this degenerate case we somewhat artificially identify a framing with an orientation. The
cobordism hypothesis then states that C0,0 describes the set of isotopy classes of oriented 0-tangles
in 0 dimensions — i.e., the positively and negatively oriented point!
Proceeding down the column to k = 1, a k-tuply monoidal n-category C is just a monoid. A
monoid ‘with duals’ is one equipped with an involution, which in this context means a function
∗: C → C with x∗∗ = x and (xy)∗ = y ∗ x∗ . Thus C0,1 is the free monoid with involution on one
object x. Elements of C0,1 are thus formal (noncommuting) products of the elements x and x∗ .
These correspond to isotopy classes of oriented 0-tangles in [0, 1], or simply strings of positively and
negatively oriented points, as shown in Figure 30.
Continuing down to k = 2, a k-tuply monoidal n-category is a commutative monoid, and again
‘having duals’ simply means being equipped with an involution. Thus C0,2 is the free commutative
monoid on one object x. Any element of C0,2 is thus of the form xn (x∗ )m . Similarly, an isotopy class
of oriented 0-tangles in 2 dimensions is just a collection of n positively oriented and m negatively
oriented points. The same holds for all dimensions k ≥ 2, essentially because there are enough
dimensions to freely move the points about in a manner corresponding to the Eckmann-Hilton
argument.
In the n = 1 column we have various kinds of category with extra structure. Here there are two
levels of duality — duality for objects and duals for morphisms — so to avoid confusion we denote
the dual of an object x by x∗ , and the dual of a morphism f : x → y by f † : y → x. For k = 0 we
just have categories, and by a category ‘with duals’ we mean one equipped with operations ∗ and †
as just described, such that ∗2 = 1 on objects, †2 = 1 on morphisms, and (f g)† = g † f † . With this
definition, C1,0 , the free category with duals on one object x, is rather dull: it has objects x and x∗
and only identity morphisms. If we artificially take a framing in this degenerate case to mean an
orientation, the tangle hypothesis states that the morphisms in this category correspond to isotopy
classes of oriented 1-tangles in 1 dimension. There are indeed only two of these, one of which is
shown in Figure 30.
Moving down the n = 1 column to k = 1, we have monoidal categories. This is the first point
at which there is room for the unit and counit. By a monoidal category ‘with duals’ we thus mean
a category with duals in the above sense which is also monoidal, for which (x ⊗ y)∗ = y ∗ ⊗ x∗
and (f ⊗ g)† = f † ⊗ g † , and equipped with a unit and counit for the ∗ duality, natural morphisms
satisfying the triangle identity. We also require
e†x = ix∗ .
This expresses a relation between the two levels of duality, but we should emphasize that the relations
between different levels of n-categorical duality are very poorly understood, and our treatment here
is provisional. In any event, with this definition the morphisms in C1,1 describe isotopy classes of
framed (or equivalently, oriented) 1-tangles in 2 dimensions [34]. Composition of morphisms in this
category corresponds to vertical juxtaposition of 1-tangles, while the tensor product corresponds to
horizontal juxtaposition.
Continuing down to k = 2, we have braided monoidal categories. By a braided monoidal category
‘with duals’ we mean a monoidal category with duals which is also braided. We also require that
the braiding and the ‘balancing’ shown in Figure 31 be unitary, where a morphism f is said to be
unitary if f f † = f † f = 1.

25

<!-- page 26 -->
•

•
31. The balancing in a braided monoidal category with duals
Turaev and Yetter [71, 73] have shown that the morphisms in C1,2 correspond to isotopy classes
of framed 1-tangles in 3 dimensions. Here a couple of remarks are in order. First, in this dimension,
our sort of framing is equivalent to an orientation together with what is often called a framing in
knot theory. Second, it is common to study 1-tangles in 3 dimensions using categories in which the
existence of the balancing is a separate postulate [20]. In our approach it arises automatically. In
fact, this idea is already implicit in the work of Fröhlich and Kerler [35].
By a symmetric monoidal category ‘with duals’ we mean just a braided monoidal category with
duals which is also symmetric. The morphisms in C1,3 correspond to isotopy classes of framed 1−1
tangles in 4 dimensions, because C1,3 is obtained from C1,2 by adding the extra relations Bu,v = Bv,u
for all u, v, corresponding to the fact that in 4 dimensions there is room to unlink all links. The
same is true in all higher dimensions — as one would expect from the stabilization hypothesis. More
generally, transversality results from differential topology imply that for k ≥ n + 2, all embeddings
of compact n-manifolds in Rn+k are isotopic [40]. Given the tangle hypothesis, this is a powerful
piece of evidence for the stabilization hypothesis.
In the n = 2 column we find the situation less well understood but still very promising. The
precise definition of a k-tuply monoidal 2-category with duals has not yet been systematically worked
out. Instead, work so far has focused on the relation between braided monoidal 2-categories with
duals and 2-tangles in 4 dimensions. Carter, Saito and others have worked out a description of such
2-tangles as movies in which each frame is a 1-tangle in 3 dimensions, giving explicit ‘movie moves’
which go between any two movies representing isotopic 2-tangles [18]. Fischer [31] has used this
information to describe a 2-category of 2-tangles in 4 dimensions, and came close to proving the
tangle hypothesis in this case. There are a number of loose ends, however, and recently Kharlamov
and Turaev [51] have done some careful work on this subject, particularly concerning the equivalence
relation on 1-tangles in 3 dimensions needed to defining 1-morphisms as equivalence classes.
Rather than reviewing this work in detail, let us simply touch upon what may at first seem the
most surprising feature, namely, how the various levels of duality interact to yield the 2-morphisms
corresponding to the movies in Figure 6: the birth of a circle, death of a circle, and saddle point. This
after all, is a crucial part of the tangle conjecture: that duality in n-categories naturally yields the
correct handle attachments and handle cancellations in the Morse-theoretic description of n-tangles.
We expect the movies in Figure 6 to occur whenever k ≥ 1, so for simplicity consider the case
k = 1. In a monoidal 2-category with duals there should be 3 levels of duality: each object x should
have a dual x∗ , each morphism f : x → y should have a dual f † : y → x, and each 2-morphism α: f ⇒ g
should have a dual α̂: g ⇒ f . The dualities for objects and morphisms should have associated units
and counits, but not the duality for 2-morphisms. Thus for any object x there are morphisms
ix : 1 → x ⊗ x∗ ,

ex : x∗ ⊗ x → 1,

and for any morphism f : x → y there are 2-morphisms
ιf : 1y ⇒ f f † ,

ǫf : f † f ⇒ 1 x .

The unit and counit for morphisms should satisfy the triangle identities, while the unit and counit for
objects should probably satisfy them only weakly, i.e., up to the 2-isomorphisms shown as 2-tangles
in 3 dimensions in Figure 32.

26

<!-- page 27 -->
x∗
•
q
qq
q8qq
∗ qqq
x qq
•
2ff•
U ....... ff x∗
......
•
x∗

x
q•
q
q
x qqq
x qqqqq
•
•
.
x
.. .

•
x

32. The 2-isomorphisms 1x ⇒ (1x ⊗ ex )(ix ⊗ 1x ) and 1x∗ ⇒ (ex ⊗ 1x∗ )(1x∗ ⊗ ix )
as 2-tangles in 3 dimensions
We also expect rules such as
(x ⊗ y)∗ = y ∗ ⊗ x∗ ,
x∗∗ = x,

(f g)† = g † f † ,

(αβ)ˆ= β̂ α̂,

ˆ = α,
α̂

f †† = f,

and
e†x = ix∗ ,

ǫ̂f = ιf † .

Then, as shown in Figure 33, the birth of a clockwise oriented circle corresponds to the unit of
the counit of x, that is, ιex : 11 ⇒ ex e†x . Similarly, the death of a clockwise oriented circle corresponds
to the counit of the unit of x, ǫix : i†x ix ⇒ 11 . One sort of saddle point is given by the unit of the unit
of x, ιix : 1x⊗x∗ ⇒ ix i†x , while another is given by the counit of the counit of x, ǫex : e†x ex ⇒ 1x∗ ⊗x .
Differently oriented versions of the 1-manifolds with boundary appearing here can be obtained by
replacing x with x∗ above.

<

∗

0 x
•
k •x∗

x• ,
x• q

<

•
x

x∗
A•

• . . . . . . . . . 0. . . . .
o

x∗•

v •x

6

rr• x
rr
x •
r
rr
q8 qq rrryr
x∗•qq
r
x •rr

x∗
.. •
•x∗

33. The 2-morphisms ιex , ǫix , ιix , and ǫex as 2-tangles in 3 dimensions
The reader may enjoy studying how the triangle identities for ι and ǫ translate into handle cancellations. For example, the following triangle identity, where ⊗ denotes horizontal composition:
ix

1ix

❅
❅
ιix ⊗1ix ❅
❅
❘
❅
ix i†x ix

✲ ix
✒
1ix ⊗ǫix

gives the isotopy between 2-tangles in 3 dimensions shown in Figure 34.

27

<!-- page 28 -->
x∗•

6

x∗•

8

x •

=

x •

x∗•

6

x∗•

8

x •

x •

34. A 2-categorical triangle identity as 2-tangle isotopy
Proceeding down the n = 2 column in Figure 30, we observe the following features. Taking
k = 2, a 2-morphism α: f → g in C2,2 should correspond to a 2-tangle in 4 dimensions, going from
an equivalence class f of 1-tangles in 3 dimensions to another equivalence class g. The braiding
phenomena arise from the fact that C2,2 is a braided monoidal 2-category [18, 31]. The case k = 3
corresponds to 2-tangles in 5 dimensions. In Figure 30 we have shown such a 2-tangle going from a
seemingly linked pair of circles to an unlinked pair. The point is that, thinking of the 5th dimension
as time, any link in 4-dimensional space can be unlinked as time passes. In fact, an over-crossing
can be isotoped to an under-crossing while pushing one strand either a little bit ‘up’ into the 4th
dimension or a little bit ‘down’. Algebraically, since C2,3 is weakly involutory, we expect these two
−1
−1 −1
−1
distinct isotopies to correspond to Ix,y : Bx,y ⇒ By,x
and (Ix,y
)hor : Bx,y ⇒ By,x
. The case k = 4
corresponds to 2-tangles in 6 dimensions. In this dimension and higher dimensions, the two isotopies
from an over-crossing to an under-crossing are themselves isotopic. This should correspond to the
−1 −1
fact that in a strongly involutory monoidal 2-category, Ix,y = (Ix,y
)hor .
Now, taken together, the stabilization hypothesis and tangle hypothesis suggest a proposal for
the n-category of which n-dimensional extended TQFTs are representations:
Extended TQFT Hypothesis, Part I. The n-category of which n-dimensional extended TQFTs
are representations is the free stable weak n-category with duals on one object.
The idea here is, first, that by the stabilization hypothesis Cn,k should stabilize for k ≥ n + 2,
yielding what we call the ‘free stable weak n-category with duals on one object’, Cn,∞ . Topologically this suggests that when considering the category whose objects are framed 0-manifolds, whose
morphisms are framed 1-manifolds with boundary, whose 2-morphisms are framed 2-manifolds with
corners, and so on up to n, we are free to think of all these objects as embedded in [0, 1]n+k where
k ≥ n + 2. Thus in particular the n-morphisms can be thought of as isotopy classes of framed
n-tangles in n + k dimensions, where k ≥ n + 2.
In the next section we turn to the implications of this hypothesis for topological quantum field
theory; here we briefly summarize one more sophisticated piece of evidence for it. This comes from
the connection between framed cobordism theory and stable homotopy theory [1, 70]. By the relation
between the n-categorical and homotopy-theoretic notions of suspension, one expects the homotopy
n-type of Ωk S k to correspond to a very special weak n-groupoid, namely the free k-tuply monoidal
weak n-groupoid on one object, Gn,k . Now duals are simply a weakened form of inverses [45], so by
the universal property of Cn,k one expects there to be a weak n-functor T : Cn,k → Gn,k that turns
duals into inverses. Topologically speaking, T should be given by the Thom-Poyntragin construction.
Indeed, this construction is implicit in Figure 26, where a tangle is used to describe a homotopy.
Suppose, for example, that α = β is the generating object x of C1,2 . Then the tangle in Figure
26 is the morphism Bx,x in C1,2 . On the other hand, T x is the object in G1,2 , or point in Ω2 S 2 ,
corresponding to identity map from S 2 to itself. Thus T Bx,x is a morphism in G1,2 corresponding
to a nontrivial homotopy from T x ⊗ T x to itself.
More generally, define a ‘j-loop’ in any monoidal n-category to be an j-morphism from 1j−1
to 1j−1 , where we define the object 10 to be the unit for the monoidal structure and, recursively,

28

<!-- page 29 -->
1i+1 = 11i . Now T should map j-loops in Cn,k to j-loops in Gn,k . In particular, an n-loop in Cn,k is
just an isotopy class of compact framed j-manifolds embedded in [0, 1]n+k (or equivalently S n+k ).
On the other hand, an n-loop in Gn,k is an an element of πn+k (S k ). There is indeed a map from the
former to the latter, given by the Thom-Pontryagin construction. Now for k ≥ n + 2, Gn,k should
stabilize to a weak n-groupoid Gn,∞ representing the homotopy n-type of the infinite loop space
Ω∞ S ∞ , so we expect to obtain a weak n-functor T∞ : Cn,∞ → Gn,∞ . By the universal property of
Gn,∞ , this n-groupoid should simply be the result of adjoining formal inverses to all j-morphisms
in Cn,∞ . One expects from this that the ith framed cobordism group is isomorphic to πi (Ω∞ S ∞ ),
that is, the ith stable homotopy group of spheres. This is indeed the case!

8

Extended TQFTs

One can think of n-category theory as providing a natural hierarchy of generalizations of set theory.
The basic idea is that the mathematics of sets, regarded as the study of the category Set, leads us to
consider general categories. Regarding this as the study of the 2-category Cat we are then lead to
consider general 2-categories, and so on. In general, the category nCat of small strict n-categories
is a strict (n + 1)-category, and we expect something of a similar but more sophisticated sort to
hold for weak n-categories. At each level of this hierarchy one can do abstract algebra, which at
at the nth level is intimately tied to n-dimensional topology. To describe an extended TQFT as a
representation of an n-category, we must also develop analogs of linear algebra at each level.
In physics, linear algebra is usually done over R or C, but for higher-dimensional linear algebra it
is useful to start more generally with any commutative ‘rig’, or ‘ring without negatives’. This is a set
R equipped with two commutative monoid structures, written + and ·, satisfying the distributive
law a · (b + c) = a · b + a · c. A good example of such a thing without additive inverses is the
natural numbers (including zero), and one reason we insist on such generality is to begin grappling
with the remarkable fact that many of the important vector spaces in physics are really defined
over the natural numbers, meaning that they contain a canonical lattice with a basis of ‘positive’
elements [28]. Examples include the weight spaces of semisimple Lie algebras, fusion algebras in
conformal field theory [35], and thanks to the work of Kashiwara and Lusztig on canonical bases,
the finite-dimensional representations of quantum groups [20, 22].
Linear algebra over the commutative rig R can be thought of as the study of the category Vect of
‘vector spaces’ over R, by which we simply mean R-modules isomorphic to Rk for some k. Now Vect
itself has two symmetric monoidal structures corresponding to the direct sum ⊕ and tensor product
⊗ of vector spaces, and the tensor product distributes over direct sum up to a natural isomorphism
satisfying certain coherence laws. Thus Vect is a categorical analog of a rig, which one might call a
‘rig category’. These are often called ring categories, but there need be no additive inverses. Precise
definitions and strictification theorems for these have been given by Laplaza [53] and Kelly [48].
The analogy between the commutative rig R and the symmetric rig category Vect suggests the
existence of a recursive hierarchy of ‘n-vector spaces’. For example, the categorical analog of an Rmodule is a ‘module category’ over Vect. This is a category V equipped with a symmetric monoidal
structure ⊕ and a functor ⊗: Vect × V → V satisfying the usual conditions for a module up to
natural isomorphisms satisfying various coherence laws. The module categories of special interest,
the ‘2-vector spaces’, are those equivalent as module categories to the k-fold Cartesian product
Vectk . A careful study of these has been done by Kapranov and Voevodsky [46]. The primordial
example of a 2-vector space is Vect itself, but when R = C a more interesting example is the category
of representations of a semisimple algebra. In general one hopes to define a weak (n + 1)-category
(n+1)Vect of ‘(n+1)-vector spaces’ over R having as objects ‘module n-categories’ over nVect which
are n-equivalent, as module n-categories, to nVectk for some k. Moreover, (n + 1)Vect should be a
monoidal — in fact stable — (n + 1)-category, permitting one to define module (n + 1)-categories
over it and to continue the recursive definition. The primordial example of an (n + 1)-vector space

29

<!-- page 30 -->
should, of course, be nVect.
Much remains to be done to develop a full-fledged rigorous theory of higher-dimensional linear
algebra. Indeed, attempting to develop it without a well-established theory of weak n-categories
is rather like developing linear algebra without solid foundations in set theory (which of course is
historically what occurred). Nonetheless, it is already becoming evident from examples that the
sense in which n-dimensional extended topological quantum field theories are ‘representations’ of
some n-category is that they are weak n-functors from it to nVect.
Note that while Vect is a stable 1-category, Hilb is a stable 1-category with duals, and that the 2
levels of duality this entails are both crucial in the definition of a unitary TQFT. As Freed [32] has
pointed out, one can, at least for low n so far, develop a theory of ‘n-Hilbert spaces’. Taking our
basic rig to be C, recall that associated to any vector space V there is, in addition to the dual V ∗ ,
the vector space V having the same additive structure but on which C acts in a complex-conjugated
manner. A Hilbert space is then a vector space equipped with an inner product, a linear map
h·, ·i: V ⊗ V → C
that satisfies a nonnegativity condition and is also nondegenerate, meaning that by duality it
yields an isomorphism V ∼
= V ∗ . Similarly, associated to a 2-vector space there is the dual V ∗ =
hom(V, Vect), defined using the appropriate notion of ‘hom’ for 2-vector spaces, and also V , the
opposite category of V (i.e., having the direction of all morphisms reversed). A 2-Hilbert space V
should thus be a 2-vector space equipped with an inner product, that is, a functor
h·, ·i: V ⊗ V → Vect.
This should be linear in the appropriate sense. Nonnegativity will be automatic because the rig
category Vect has no negatives, but we should require nondegeneracy, meaning that the inner product
should define an equivalence of Vect-modules between V and V ∗ . (That these are equivalent has
already been established by Yetter [74].) With still further conditions giving V some of the properties
of Hilb, it appears that one obtains a notion of ‘2-Hilbert space’ such that 2Hilb is a stable 2-category
with duals. Examples should certainly include the category of representations of a finite-dimensional
C*-algebra, such as the group algebra of a finite group [32].
We hypothesize, therefore, that we can recursively define a stable weak n-category with duals,
‘nHilb’, such that the following holds.
Extended TQFT Hypothesis, Part II. An n-dimensional unitary extended TQFT is a weak
n-functor, preserving all levels of duality, from the free stable weak n-category with duals on one
object to nHilb.
The best evidence for this so far is the work of Freed and Quinn on the Dijkgraaf-Witten model
[32, 33], of Lawrence on extended TQFTs defined via triangulations [54], and of Walker [72] on
Chern-Simons theory. If this hypothesis is true, one should be able to specify an n-dimensional
unitary extended TQFT simply by specifying a particular n-Hilbert space, thanks to the universal
property of the stable weak n-category with duals on one object. (More precisely, this should specify
a weak n-functor up to ‘equivalence’ of these, a notion so far understood only for low n.) In future
work we intend to describe the n-Hilbert spaces giving rise to various well-known TQFTs.

9

Quantization

To paraphrase Nelson, quantization is a mystery, not a functor. And indeed, while in some technical
sense we understand how quantum groups give precisely the algebraic structures needed to construct
3-dimensional TQFTs, and how the ‘quantization’ of the group corresponds to the passage from
classical to quantum field theory, we do not yet know to what extent this miracle can be generalized

30

<!-- page 31 -->
to higher dimensions. The search for algebraic structures appropriate for 4-dimensional TQFTs is
already underway, with Donaldson theory as a powerful lure [18, 22, 23, 24, 54]. One would like
higher-dimensional algebra to offer some guidance here, and eventually one would very much like a
comprehensive picture of quantization for topological field theories in all dimensions.
In its simplest guise, quantization concerns the relation between the commutative algebras of
observables in classical mechanics and the noncommutative algebras in quantum mechanics. On
the one hand, one can start with a commutative algebra A and try to obtain a noncommutative
algebra by ‘deformation quantization’. There is in general no systematic procedure for doing this.
Nonetheless, one can study the possibilities, for example by considering algebra structures on A[[h̄]]
given by formal power series
a ⋆ b = ab + h̄m1 (a ⊗ b) + h̄2 m2 (a ⊗ b) + · · ·
The requirement that this ‘star product’ makes A[[h̄]] into an algebra imposes conditions on the mi
which can be studied using homological algebra [11]. Most simply, the quantity
{a, b} = m1 (a ⊗ b) − m1 (b ⊗ a),
which measures the first-order deviation from commutativity of the star product, must be a Poisson
bracket on A, i.e. a Lie bracket with
{a, bc} = {a, b}c + b{a, c}.
On the other hand, there is an obvious way to get a commutative algebra from a noncommutative
algebra A, namely by taking its center Z(A). Physically this corresponds to extracting the classical
part of a quantum theory, the so-called ‘superselection rules’. Note that taking the center, while a
perfectly systematic process, is not a functor, since a homomorphism f : A → B need not restrict to
a homomorphism from Z(A) to Z(B).
Figure 21 sheds some light on these ideas and their generalizations. In the n = 0 column one
has, in the k = 1 and k = 2 rows, monoids and commutative monoids respectively. A monoid object
in Vect is an algebra, while a commutative monoid object is a commutative algebra. In addition to
the forgetful functor from the category of commutative algebras to that of algebras, we have seen
there are two nonfunctorial, but still very interesting, processes relating these categories: ‘taking
the center’ and ‘deformation quantization’.
These processes have analogs in other columns of Figure 21. As one marches down any column,
one expects the last step before stabilization to consist of imposing equations on structure already
present. In this situation one can consider formal deformations of the stabilized sort of structure in
the category of not-quite-stabilized structures. For example, in the n = 1 column one can consider
deformations of a symmetric monoidal category in the category of braided monoidal categories.
This is precisely where quantum groups arise! The category of representations of a Lie group
is a symmetric monoidal category object in 2Vect, while the category of representations of the
corresponding quantum group is a braided monoidal category object in 2Vect. The latter is a kind
of deformation of the former in which, for example, the braiding is given by a formal power series
Bx,y (a ⊗ b) = b ⊗ a + h̄r1 (a ⊗ b) + r2 (a ⊗ b) + · · ·
The condition that B be a braiding imposes conditions on the ri ; for example, r1 must be a solution
of the ‘classical Yang-Baxter equations’. For a detailed treatment of the ‘deformation quantization’ of symmetric monoidal categories into balanced braided monoidal categories, see Mattes and
Reshetikhin [59]. The tangle invariants arising this way can be expanded as formal power series in h̄,
and the coefficients, known as ‘Vassiliev invariants’ or ‘invariants of finite type’, have special topological properties [9, 13]. Their relation with the deformation quantization of commutative algebras
is clarified by the manner in which they arise in Chern-Simons perturbation theory [2].

31

<!-- page 32 -->
The operation of ‘taking the center’ can also be generalized, in a subtle and striking manner. We
can think of a k-tuply monoidal n-category C — strict, semistrict, or weak — as an object in the
corresponding version of (n + k)Cat. Let Z(C) be the largest sub-(n + k + 1)-category of (n + k)Cat
having C as its only object, 1C as its only morphism, 11C as its only 2-morphism, and so on, up to
only one k-morphism. Thus Z(C) is a (k + 1)-tuply monoidal n-category.
In what sense is Z(C) the ‘generalized center’ of C? Consider first the case where C is a monoid,
thought of as a category with one object. Then Z(C) is the largest sub-2-category of Cat having C as
its only object, the identity functor 1C as its only morphism, and natural transformations α: 1C ⇒
1C as 2-morphisms. In other words, Z(C) is the commutative monoid consisting of all natural
transformations α: 1C ⇒ 1C . Since there is only one object in C, such a natural transformation is
simply a single morphism in C, and the the commutative square condition in eq. (4) implies this
morphism must commute with all the other morphisms in C. Thus Z(C) is just the center of C as
traditionally defined. This also shows that Z is not a functor.
We leave it to the reader to check that if C is a set, Z(C) is the monoid consisting of all functions
F : C → C. Similarly, if C is a category, Z(C) is the monoidal category whose objects are functors
F : C → C and whose morphisms are natural transformations between such functors. The monoidal
structure here corresponds to composition of functors. A more interesting example was worked out
by Kapranov and Voevodsky [46]. Suppose that we start with a monoidal category C and work in
the semistrict context. The 2-morphisms in 2Cat are known as ‘quasinatural transformations’, since
the square in eq. (4) is required to commute only up to a 2-isomorphism [38]. The 3-morphisms in
2Cat are known as ‘modifications’. The generalized center Z(C) thus turns out to be the braided
monoidal category whose objects are quasinatural transformations α: 1C ⇒ 1C and whose morphisms
are modifications between these.
It turns out that when C is the monoidal category of representations of a Hopf algebra H, Z(C)
is the braided monoidal category of representations of a Hopf algebra called the quantum double of
H [20]. Moreover, while not themselves quantum doubles, quantum groups are easily constructed
as quotients of quantum doubles [20]. We thus see that that in the n = 1 column of Figure
21, interesting braided monoidal categories can be obtained either by deformation quantization of
symmetric monoidal categories, or by taking the generalized center of monoidal categories. We
expect a more complex version of this story to occur in the higher-n columns. For example, in the
n = 2 column there should be a theory of deformations of a strongly symmetric monoidal 2-category
in the category of weakly symmetric ones. From Figure 30 one would expect this to be related to
a Vassiliev theory for surfaces embedded in R5 . The generalized center construction should also be
interesting. For example, one can obtain braided monoidal 2-categories as the generalized centers of
monoidal 2-categories [7].

Acknowledgements
We would like to thank Lawrence Breen, Ronald Brown, Louis Crane, André Joyal, Thomas Kerler,
Ruth Lawrence, Stephen Sawin, Bruce Smith, Ross Street, Dominic Verity, and David Yetter for
helpful discussions and correspondence. We also thank Aaron Lauda for preparing XyPic versions
of all the figures in this paper.

References
[1] J. Adams, Infinite Loop Spaces, Princeton U. Press, Princeton, 1978.
[2] J. Andersen, J. Mattes, and N. Reshetikhin, The Poisson structure on the moduli space of flat
connections and chord diagrams, preprint.
[3] A. Ashtekar, Lectures on Non-perturbative Canonical Quantum Gravity, Singapore, World
Scientific, 1991.

32

<!-- page 33 -->
[4] M. Atiyah, Topological quantum field theories Inst. Hautes Études Sci. Publ. Math. 68 (1988)
175-186.
The Geometry and Physics of Knots, Cambridge U. Press, Cambridge, 1990.
[5] Knots and Quantum Gravity, ed. J. Baez, Oxford U. Press, 1994.
[6] J. Baez, Knots and quantum gravity: progress and prospects, U. C. Riverside preprint, to
appear in Proceedings of the Seventh Marcel Grossman Meeting on General Relativity, available
as gr-qc/9410018.
[7] J. Baez, F. Halanke, and M. Neuchl, Braided monoidal 2-categories, to appear.
[8] J. Baez, M. Ody and W. Richter, Topological aspects of spin and statistics in nonlinear
sigma models, U. C. Riverside preprint, to appear in Jour. Math. Phys., available as condmat/9208005.
[9] D. Bar-Natan, On the Vassiliev knot invariants, to appear in Topology.
[10] J. Barrett and B. Westbury, Spherical categories, U. Nottingham preprint, available as hepth/9310164.
The equality of 3-manifold invariants, U. Nottingham preprint, available as hep-th/9406019.
[11] F. Bayen, M. Flato, C. Fronsdal, A. Lichnerowicz, and D. Sternheimer, Deformation theory
and quantization, I, II, Ann. Phys. 110 (1978), 61-110, 111-151.
[12] J. Bénabou, Introduction to bicategories, Springer Lecture Notes in Mathematics 47, New York,
1967, pp. 1-77.
[13] J. Birman, New points of view in knot theory, Bull. Amer. Math. Soc. 28 1993, 253-287.
[14] L. Breen, On the classification of 2-gerbes and 2-stacks, Astérisque 225 (1994), 1-160.
[15] B. Broda, A surgical invariant of 4-manifolds, in Proceedings of the Conference on Quantum
Topology, ed. D. Yetter, World Scientific, Singapore, 1994, pp. 45-50.
[16] R. Brown, Higher-dimensional group theory, in Low-Dimensional Topology, eds. R. Brown and
T. Thickstun, London Math. Soc. Lecture Notes 48, Cambridge U. Press, Cambridge, 1982,
pp. 215-238.
From groups to groupoids: a brief survey, Bull. London Math. Soc. 19 (1987) 113-134.
[17] R. Brown and C. Spencer, G-groupoids, crossed modules, and the classifying space of a topological group, Proc. Kon. Akad. v. Wet. 79 (1976), 296-302.
[18] J. Carter and M. Saito, Knotted surfaces, braid movies, and beyond, in Knots and Quantum
Gravity, ed. J. Baez, Oxford U. Press, 1994, pp. 191-229.
[19] J. Cerf, La Stratification Naturelle de Espace des Fonctions Différentiables Réeles et la
Theéoreme de la Psedoisotopie, Publ. Math. I. H. E. S. 39 (1970).
[20] V. Chari and A. Pressley, A Guide to Quantum Groups, Cambridge U. Press, 1994.
[21] S. Chung, M. Fukuma, and A. Shapere, Structure of topological lattice field-theories in three
dimensions, Int. Jour. Mod. Phys. A9 (1994), 1305-1360.
[22] L. Crane and I. Frenkel, Four dimensional topological quantum field theory, Hopf categories,
and the canonical bases, Jour. Math. Phys. 35 (1994), 5136-5154.

33

<!-- page 34 -->
[23] L. Crane, L. Kauffman and D. Yetter, State-sum invariants of manifolds, I, Kansas U. preprint,
available as hep-th/9409167.
[24] L. Crane and D. Yetter, On algebraic structures implicit in topological quantum field theories,
Kansas U. preprint available as hep-th/9412025.
[25] R. Dijkgraaf and E. Witten, Topological gauge theories and group cohomology, Commun. Math.
Phys. 129 (1990) 393-429.
[26] B. Durhuus and T. Jonsson, Classification and construction of unitary topological quantum
field theories in two dimensions, Jour. Math. Phys. 35 (1994), 5306-5313.
[27] B. Eckmann and P. Hilton, Group-like structures in categories, Math. Ann. 145 (1962), 227-255.
[28] S. Eilenberg and G. Kelly, Closed categories, in Proceedings of the Conference on Categorical
Algebra, eds. S. Eilenberg et al, Springer, Berlin, 1966, pp. 421-562.
[29] P. Etinghof and M. Khovanov, Representations of tensor categories and Dynkin diagrams,
Harvard U. preprint available as hep-th/9408078.
[30] A. Einstein, The foundation of the general theory of relativity, in The Principle of Relativity,
by H. Lorentz et al, trans. W. Perrett and G. Jeffery, Dover, New York, 1952, p. 117.
[31] J. Fischer, 2-categories and 2-knots, Duke Math. Jour. 75 (1994), 493-526.
[32] D. Freed, Higher algebraic structures and quantization, Commun. Math. Phys. 159 (1994),
343-398.
[33] D. Freed and F. Quinn, Chern-Simons theory with finite gauge group, Commun. Math. Phys.
156 (1993), 435-472.
[34] P. Freyd and D. Yetter, Braided compact monoidal categories with applications to low dimensional topology, Adv. Math. 77 (1989), 156-182.
[35] J. Fröhlich and T. Kerler, Quantum Groups, Quantum Categories and Quantum Field Theory,
Springer Lecture Notes in Mathematics 1542, Berlin, 1993.
[36] M. Fukuma, S. Hosono, and H. Kawai, Lattice topological field theory in two-dimensions,
Comm. Math. Phys. 161 (1994), 157-175.
[37] R. Gordon, A. J. Power, and R. Street, Coherence for tricategories, Memoirs Amer. Math. Soc.
117 (1995) Number 558.
[38] J. Gray, Formal Category Theory: Adjointness for 2-Categories, Springer Lecture Notes in
Mathematics 391, Berlin, 1974.
[39] A. Grothendieck, Pursuing stacks, unpublished manuscript, 1983, distributed from UCNW,
Bangor, United Kingdom.
[40] M. Hirsch, Differential Topology, Springer, Berlin, 1976.
[41] C. Isham, Canonical quantum gravity and the problem of time, in Integral Systems, Quantum
Groups, and Quantum Field Theories, eds. L. Ibort and M. Rodriguez, Kluwer, Dordrecht,
1993, pp. 157-207.
[42] M. Johnson, The combinatorics of n-categorical pasting, Jour. Pure Appl. Alg. 62 (1989),
211-225.

34

<!-- page 35 -->
[43] A. Joyal and R. Street, Braided tensor categories, Adv. Math. 102 (1993), 20-78.
[44] A. Joyal and M. Tierney, Algebraic homotopy types, unpublished.
[45] M. Kapranov and V. Voevodsky, ∞-groupoids and homotopy types, Cah. Top. Geom. Diff. 32
(1991), 29-46.
[46] M. Kapranov and V. Voevodsky, 2-Categories and Zamolodchikov tetrahedra equations, in Proc.
Symp. Pure Math. 56 Part 2 (1994), AMS, Providence, pp. 177-260.
Braided monoidal 2-categories, 2-vector-spaces, and Zamolodchikov tetrahedra equations,
Northwestern U. preprint.
[47] G. Kelly, Basic concepts of enriched category theory, London Math. Soc. Lecture Notes 64,
Cambridge U. Press, Cambridge, 1982.
[48] G. Kelly, Coherence theorems for lax algebras and distributive laws, Springer Lecture Notes in
Mathematics 420, Berlin, pp. 281-375.
[49] G. Kelly and R. Street, Review of the elements of 2-categories, Springer Lecture Notes in
Mathematics 420, Berlin, 1974, pp. 75-103.
[50] T. Kerler, Bridged links and tangle presentations of cobordism categories, Harvard U. preprint.
[51] V. Kharlamov and V. Turaev, On the definition of 2-category of 2-knots, LOMI preprint.
[52] R. Kirby, The Topology of 4-Manifolds, Springer Lecture Notes in Mathematics 1374, Berlin,
1989.
[53] M. Laplaza, Coherence for distributivity, Springer Lecture Notes in Mathematics 281, Berlin,
1972, pp. 29-72.
[54] R. Lawrence, Triangulation, categories and extended field theories, in Quantum Topology, eds.
R. Baadhio and L. Kauffman, World Scientific, Singapore, 1993, pp. 191-208.
[55] O. Leroy, Sur une notion de 3-categorie adaptee a l’homotopie, U. Montpellier II preprint.
[56] S. Mac Lane, Natural associativity and commutativity, Rice U. Studies 49 (1963), 28-46.
[57] S. Mac Lane, Categories for the Working Mathematician, Springer, Berlin, 1988.
[58] S. Mac Lane and J. Whitehead, On the 3-type of a complex, Proc. Nat. Acad. Sci. 36 (1950),
41-58.
[59] J. Mattes and N. Reshetikhin, On invariants of tangles derived from balanced categories, in
Proceedings of the Conference on Quantum Topology, ed. D. Yetter, World Scientific, Singapore,
1994, pp. 269-299.
[60] J. P. May, Simplicial Objects in Algebraic Topology, Van Nostrand, Princeton, 1968.
[61] J. Milnor, Lectures on the h-cobordism theorem, Princeton U. Press, Princeton, 1965.
[62] J. Milnor, Morse Theory, Princeton U. Press, Princeton, 1969.
[63] C. Misner, K. Thorne and J. Wheeler, Gravitation, Freeman, San Francisco, 1973.
[64] U. Pachner, P.L. homeomorphic manifolds are equivalent by elementary shelling, Europ. J.
Combinatorics 12 (1991) 129-145.

35

<!-- page 36 -->
[65] F. Quinn, Lectures on axiomatic topological quantum field theory, Virginia Polytechnic Institute
and State U. preprint, to appear in the proceedings of the Park City Geometry Institute.
[66] N. Reshetikhin and V. Turaev, Ribbon graphs and their invariants derived from quantum groups
Comm. Math. Phys. 127 (1990), 1-26.
N. Reshetikhin and V. Turaev, Invariants of 3-manifolds via link-polynomials and quantum
groups Invent. Math. 103 (1991), 547-597.
[67] S. Sawin, Links, quantum groups and TQFTs, to appear.
[68] S. Sawin, Two dimensional topological quantum field theory, to appear.
[69] J. Stasheff, H-spaces from a Homotopy Point of View, Springer Lecture Notes in Mathematics
167, Berlin, 1971.
[70] R. Stong, Notes on Cobordism Theory, Princeton U. Press, Princeton, 1968.
[71] V. Turaev, Operator invariants of tangles, and R-matrices, Math. USSR Izvestia 35 (1990),
411-444.
[72] K. Walker, On Witten’s 3-manifold invariants, preprint.
[73] D. Yetter, Markov algebras, in Braids, Contemp. Math. 78 (1988), 705-730.
[74] D. Yetter, Categorical linear algebra — a setting for questions from physics and low-dimensional
topology, Kansas U. preprint.

36
