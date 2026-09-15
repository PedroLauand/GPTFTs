---
type: paper
date: 1993-08-09
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:hep-th/9308043v1)
reviewed: false
---

# Classification and construction of unitary topological field theories in two dimensions

Machine-generated and unreviewed text extraction of arXiv:hep-th/9308043v1
(12 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/hep-th/9308043v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
August 1993

arXiv:hep-th/9308043v1 9 Aug 1993

Classification and construction of unitary
topological field theories in two dimensions1

Bergfinnur Durhuus2
Matematisk Institut, University of Copenhagen
Universitetsparken 5, 2100 Copenhagen Ø
Denmark

Thordur Jonsson3
Raunvisindastofnun Haskolans, University of Iceland
Dunhaga 3, 107 Reykjavik
Iceland

Abstract. We prove that unitary two-dimensional topological field theories are
uniquely characterized by n positive real numbers λ1 , . . . λn which can be regarded
as the eigenvalues of a hermitean handle creation operator. The number n is the
dimension of the Hilbert space associated with the circle and the partition functions
for closed surfaces have the form
Zg =

n
X

λg−1
i

i=1

where g is the genus. The eigenvalues can be arbitary positive numbers. We show
how such a theory can be constructed on triangulated surfaces.

1

Supported in part by a NATO Science collaboration grant.
e-mail: durhuus@math.ku.dk
3
e-mail: thjons@raunvis.hi.is
2

<!-- page 2 -->
1

Introduction

Topological quantum field theory (TQFT) [1, 4] has given considerable insight into
a number of unsolved problems in theoretical physics [3, 5] and also provided an
important research tool in pure mathematics [2, 6, 7]. Most work in this field has
been devoted to studying particular examples of such theories and uncovering their
physical content as well as their relation to low-dimensional topology.
The problem of classifying topological quantum field theories is a hard one in
more than two dimensions since it is intimately tied up with the classification of
topological manifolds in these dimensions. In two dimensions the situation is radically different since a compact orientable two-dimensional manifold is characterized
topologically by its genus and the number of boundary components. In [5] it was
shown that the two-dimensional theories have indeed a very simple structure.
The classification problem for TQFT in two dimensions was addressed in [8],
see also [9], using triangulated surfaces and fields associated with vertices. In these
papers topological theories were constructed with the partition function for a closed
surface of genus g given by
Zg = λg−1
(1)
where λ is an arbitrary positive number.
In the present paper we prove that the most general unitary TQFT in two
dimensions is in fact a direct sum of theories of this type. The proof is very simple. It
uses the fact that any two-dimensional surface can be constructed by gluing together
spheres with three or fewer boundary components and therefore any unitary TQFT
in two dimensions is determined by the partition functions for a sphere with three
or fewer holes. Unitarity implies that an associated handle creation operator is
hermitean and it follows that the theory is characterized up to equivalence by the
values of partition functions for closed surfaces.
The classification of unitary TQFT on triangulated surfaces with the fields defined on links and taking values in a finite set has been discussed in a number of
recent papers [10, 11, 12]. It was first shown in [10] that the weight factors for
triangles can in this case be regarded as structure constants of a semisimple associative algebra and the physical Hilbert space can be identified with the center
of the algebra. It follows that in these theories the number λ in (1) is always the
inverse square of an integer. This is also the case in two-dimensional topological
gauge theories [13, 14]. Theories with fields defined on links can easily be realized
as vertex theories.
In the next section we describe the Atiyah axioms for unitary TQFT and point
out simplifications that occur in two dimensions. We then proceed to show that the
2

<!-- page 3 -->
theory is determined by the three loop function on the sphere and use the gluing
axiom to show that the partition function for a closed surface is necessarily a sum
of exponentials as in (1). In section 4 we construct a lattice TQFT of the most
general form. In the final section we comment on the classification problem in
higher dimensions.

2

The Atiyah axioms

In this section we recall the axioms for a unitary TQFT [4] as they apply in two
dimensions. We assume that all manifolds are smooth, oriented and compact unless
otherwise is stated. If M is an oriented manifold, we denote by M ∗ the same
manifold with the orientation reversed.
A unitary TQFT in two dimensions comprises the following assignments: To
each closed 1-dimensional manifold Σ there is assigned a finite dimensional Hilbert
space HΣ with inner product <, >Σ . To each surface S (not necessarily closed) there
is assigned an element Z(S) ∈ HΣ , called the partition function for S, where Σ = ∂S
is the boundary of S. The Hilbert space associated with the empty 1-dimensional
manifold ∅ is H∅ = C so Z(S) ∈ C if S is closed. These objects satisfy the following
conditions:
1. If f : Σ1 7→ Σ2 is an orientation preserving diffeomorphism between 1-manifolds
then there is an associated unitary mapping
Uf : HΣ1 7→ HΣ2

(2)

such that Ug◦f = Ug Uf if g is an orientation preserving diffeomorphism from
Σ2 to another 1-manifold Σ3 .
If f extends to an orientation preserving diffeomorphism between surfaces,
S1 7→ S2 , where ∂Si = Σi , i = 1, 2, then Uf (Z(S1 )) = Z(S2 ).
2. For any 1-manifold Σ,
∗
HΣ∗ = HΣ

(3)

i.e. we have an identification between these spaces, which is equivalent to
giving a non-degenerate bilinear form
(, )Σ : HΣ × HΣ∗ 7→ C

(4)

(x, y)Σ = (y, x)Σ∗ .

(5)

such that

3

<!-- page 4 -->
This form is preserved by diffeomorphisms, i.e. for f : Σ1 7→ Σ2 as in axiom 1,
(x, y)Σ1 = (Uf x, Uf ∗ y)Σ2

(6)

for all x ∈ HΣ1 , y ∈ HΣ∗1 , where f ∗ :7→ Σ∗1 7→ Σ∗2 denotes f regarded as an
orientation preserving map between Σ∗1 and Σ∗2 .
Defining the conjugate linear isomorphism y 7→ y ∗ from HΣ to HΣ∗ by
(x, y ∗ )Σ =< x, y >Σ

(7)

for x, y ∈ HΣ , we furthermore assume that x∗∗ = x for all x ∈ HΣ and
Z(S ∗ ) = Z(S)∗

(8)

for any surface S with boundary Σ.
3. If Σ = Σ1 ∪ Σ2 is a disjoint union of 1-manifolds then HΣ = HΣ1 ⊗ HΣ2 and
we have a corresponding factorization of the bilinear forms and unitary maps,
i.e. (, )Σ = (, )Σ1 ⊗ (, )Σ2 , and if f1 : Σ1 7→ Σ′1 and f2 : Σ2 7→ Σ′2 are orientation
preserving diffeomorphisms, then Uf = Uf1 ⊗ Uf2 where f : Σ 7→ Σ′1 ∪ Σ′2
denotes the diffeomorphism that equals f1 on Σ1 and f2 on Σ2 .
Let S1 and S2 be two surfaces such that ∂S1 = Σ1 ∪ Σ3 and ∂S2 = Σ2 ∪ Σ∗3 .
Let S be the surface obtained by gluing S1 and S2 together along their Σ3
boundary component,
S = S1 ∪Σ3 S2 .
(9)
Then Z(S) = (Z(S1 ), Z(S2 ))Σ3 where, by abuse of notation, (·, ·)Σ3 denotes
the pairing
∗
HΣ1 ⊗ HΣ3 ⊗ HΣ2 ⊗ HΣ
7→ HΣ1 ⊗ HΣ2
(10)
3
induced by (4).
Concretely, if {xi }, {yj }, {zk } are bases for HΣ1 , HΣ2 , HΣ3 , respectively, and
∗
{zk∗ } is the dual basis for HΣ
, then we can write
3
Z(S1 ) =

X

cik xi ⊗ zk

(11)

Z(S2 ) =

X

djl yj ⊗ zl∗

(12)

cik djk xi ⊗ yj .

(13)

i,k

j,l

for suitable constants cik , djl , and
Z(S) =

X

i,j,k

4

<!-- page 5 -->
4. Let Σ be an oriented 1-manifold and orient the cylinder Σ × [0, 1] such that
x 7→ (x, 0) is an orientation reversing map from Σ onto Σ × {0} whereas
x 7→ (x, 1) is an orientation preserving mapping from Σ onto Σ × {1}. Using
the canonical identification H1∗ ⊗ H2 ≈ Hom(H1 , H2 ), we may according to
axioms 2 and 3 regard Z(Σ × [0, 1]) as a linear map from HΣ×{0} to HΣ×{1}
and we assume that Z(Σ × [0, 1]) = Uf where f : Σ × {0} 7→ Σ × {1} is defined
by f ((x, 0)) = (x, 1). Using the mapping Uf to identify the spaces HΣ×{0} and
HΣ×{1} we can write
Z(Σ × [0, 1]) = I
(14)
where I is the identity mappping.
We refer to [4] for a detailed discussion of the axioms. Here we make a few
comments that apply especially in the two-dimensional case.
It is a standard consequence of the axioms that the unitary mapping Uf with f
as in axiom 1 only depends on the homotopy class of the diffeomorphism f . If Σ1
and Σ2 are connected, i.e. circles, there is only one homotopy class of orientation
preserving diffeomorphisms and we can write Uf = U(Σ1 , Σ2 ). By axiom 1 it follows
that the mappings U(Σ1 , Σ2 ) yield a canonical identification of all the Hilbert spaces
HΣ (where Σ is connected) with a single Hilbert space which we denote by H with
inner product <, >. With these identifications all the mappings U(Σ1 , Σ2 ) are of
course the identity and by (5) and (6) a unique symmetric bilinear form (, ) is
defined on H. Similarly, by (6) and (7) the ∗-maps define a unique conjugate linear
involution x 7→ x∗ on H given by
(x, y ∗ ) =< x, y > .

(15)

It follows from the assumed factorization properties of the inner products, bilinear forms and unitary mappings that the vectorspace associated to a 1-manifold
with n boundary components Σ1 , . . . , Σn can be identified with H⊗n . If f is a diffeomorphism of Σ1 ∪ . . . ∪ Σn onto itself which permutes the boundary components,
then the mapping induced by Uf acts on H⊗n by the corresponding permutation
of factors in the tensor product. This implies that if S is a connected surface with
∂S = Σ1 ∪ . . . ∪ Σn then Z(S) ∈ H⊗n is a symmetric tensor since there exist orientation preserving diffeomorphisms that permute the boundary components of S in any
prescribed way. Moreover, since any surface S possesses an orientation resversing
diffeomorphism, we conclude that Z(S ∗ ) = Z(S) and hence, by (8), that
Z(S) = Z(S)∗
for any surface S.
5

(16)

<!-- page 6 -->
Letting HR denote the real subspace of H defined by
HR = {x ∈ H : x = x∗ }

(17)

we have a direct sum decomposition over R,
H = HR ⊕ iHR .

(18)

According to (15) and the symmetry of (, ) it follows that the restriction of the
inner product to HR is a real inner product on HR which equals the restriction of
the bilinear form to HR . We thus conclude from (16) that any two-dimensional
unitary TQFT is effectively real, i.e. we might have started from the outset with
real Hilbert spaces and partition functions satisfying the analogues of axioms 1-4
without (7) and (8).

3

Classification

Let us assume that we are given a unitary TQFT satisfying the axioms of the
previous section. Let us denote the partition function for a connected surface of
genus g with n boundary components by Zg,n and write Zg,0 = Zg . We choose
an orthonormal basis {xi } for HR which, according to (18), also constitutes an
orthonormal basis for H with x∗i = xi . The one loop function on the sphere can
then be expressed as
X
di xi .
(19)
Z0,1 =
i

The two and three loop functions on the sphere can similarly be written as
Z0,2 =

X

qij xi ⊗ xj

(20)

Cijk xi ⊗ xj ⊗ xk ,

(21)

ij

and
Z0,3 =

X
ijk

where qij and Cijk are real and symmetric under interchange of the indices. By
axioms 3 and 4 we have
X
qij xi = x∗j
(22)
i

so qij = δij with respect to the chosen basis.
We define a handle operator H ∈ End(H) by gluing together two three loop
functions:
X
H=
Hil xi ⊗ x∗l
(23)
il

6

<!-- page 7 -->
where
X

Hil =

Cijk Cljk .

(24)

jk

This is the same as regarding Z1,2 as an operator on H. Applying H to the vector
Zg,1 clearly gives Zg+1,1 . The operator H is hermitean by (8) i.e. symmetric on HR .
We now choose the basis {xi } to consist of the eigenvectors of H and let λ1 , . . . λn
denote the eigenvalues of H (not necessarily distinct), n = dim H. Then by axiom
3
Zg = < Z0,1 , H g Z0,1 >
X

=

λgi |di |2

(25)
(26)

i

for any g ≥ 0. Furthermore,
Zg+1 = TrH g =

λgi

(27)

λg−1
i

(28)

X
i

for all g ≥ 0. It follows that
X

λgi |di |2 =

X
i

i

for all g ≥ 1.
Eq. (28) implies that all the eigenvalues are nonegative. In order to prove this
we order the eigenvalues according to their absolute value so that |λi | ≥ |λj | if i ≤ j
and assume λ1 6= 0. Clearly (28) cannot hold for all g unless λ1 is positive and we
conclude also that
k
X

λgi |di |2 = kλg−1
1

(29)

i=1

where k is the multiplicity of λ1 . Subtracting (29) from (28) and repeating the above
argument we conclude that all the eigenvalues are nonegative. Below we show that
−1
a zero eigenvalue cannot occur and we can choose a basis such that di = λi 2 .
Consider the operators Ci on HR defined by
Ci =

X

Cijk xj ⊗ x∗k .

(30)

jk

By the symmetry of Cijk and the four loop function these operators are mutually
commuting and symmetric so they can be simultaneously diagonalized and we can
choose a new self-dual basis such that Cijk = δij δik Ciii . Using the definition of the
2
handle operator we now find that Ciii
= λi and H is diagonal in this basis. If λi = 0,
then Ciii = 0. This contradicts axiom 4 which states that
X

Cijk dk xi ⊗ x∗j = I

ijk

7

(31)

<!-- page 8 -->
and implies that all Ciii 6= 0 and Ciii di = 1.
It is not hard to convince oneself that any positive operator can arise as a handle
operator. In fact we give an explicit construction in the next section.
We conclude this section by showing that all the information in a two-dimensional
unitary TQFT is contained in the spectrum of H. We begin by making precise what
we mean by the equivalence of two unitary TQFT in two dimensions. Let T be a
theory satisfying the axioms of section 2 and let T ′ be another one whose objects
are distinguished from those of T by a prime. We say that T and T ′ are equivalent
if for any 1-manifold Σ there exists a unitary mapping
′
VΣ : HΣ 7→ HΣ

(32)

such that the following conditions hold:
1. For any orientation preserving diffeomorphism f : Σ1 7→ Σ2 between 1manifolds
Uf′ = VΣ2 Uf VΣ∗1 .
(33)
2. For any oriented surface S
Z ′ (S) = V∂S (Z(S))

(34)

with the understanding that Z ′ (S) = Z(S) if S is closed.
3. For any 1-manifold Σ we have
(VΣ x, VΣ∗ y)′Σ = (x, y)Σ .

(35)

Let T, T ′ be a pair of unitary TQFT’s whose handle operators have the spectrum
λ1 , . . . , λn . Then, by previous arguments, they are both equivalent to theories where
all Hilbert spaces for connected boundary components coincide and equal H and H′ ,
respectively. We have seen that by a suitable choice of bases the three loop functions
then take the form
Xq
λi xi ⊗ xi ⊗ xi .
(36)
Z3,0 =
i

−1

Let us call such a basis a canonical basis. Furthermore, qij = δij , di = λi 2 with
respect to a canonical basis. An equivalence between T and T ′ is now obtained by
mapping a canonical basis for H to a canonical basis for H′ .
We finally remark that two unitary TQFT’s whose partition functions take the
same value for all closed surfaces have handle operators with identical spectra, in
view of (27), and are therefore equivalent.
8

<!-- page 9 -->
4

Construction

In [8] a field theoretical construction was given of a TQFT on triangulated surfaces,
using fields defined on vertices, such that Zg = N χ , where N could take any positive
value and χ is the Euler characteristic. In order to obtain a theory whose partition
functions for closed surfaces are sums of exponentials we can take a direct sum of
theories of this type.
Let us explain what we mean by the direct sum of two TQFT’s. Suppose we have
′
two theories with loop functions Zg,n and Zg,n
and Hilbert spaces H and H′ for each
connected boundary component. The direct sum is a TQFT with the Hilbert space
′
H̃ = H ⊕ H′ for each boundary component and loop functions Z̃g,n = Zg,n + Zg,n
′
where we regard Zg,n + Zg,n
in a natural way as an element of H̃⊗n , n 6= 0. Unitary
maps and bilinear forms are defined in the obvious way. One can then check that
the direct sum satisfies the axioms if the original theories do so.
Here we give an alternative and more direct construction of a TQFT with an
arbitrary handle operator using triangulations and local weights. Let S be a triangulated surface of genus g and N1 , . . . , Nn a sequence of n not necessarily distinct
positive numbers. Let J = {1, . . . , n}. A colouring of S is a mapping from the
vertices of S, V(S), into J. The image of a vertex under a colouring is called its
colour. Given a colouring φ of S we define the weight of the vertex v to be Ni where
i = φ(v). The weight w∆ of a triangle ∆ in S with corners whose colours are i, j, k
−1

is defined to be Ni 2 if i = j = k but zero otherwise. The partition function for a
closed surface S is now defined to be
Z(S) =

X Y

Nφ(v)

φ v∈V(S)

Y

(37)

w∆ ,

∆∈T (S)

where the sum is over all colourings of S and T (S) denotes the set of all triangles
in S. It is easy to see that if S is connected the only colourings which contribute
are those that assign the same colour to all vertices and
Z(S) =

n
X

Niχ .

(38)

i=1

Now let S be a connected triangulated surface with b boundary components. Let
|∂S| be the number of verticies in ∂S and define
− 1 |∂S| X

ζi (S) = Ni 2

Y

φ v∈V(S)

Nφ(v)

Y

w∆ ,

(39)

∆∈T (S)

where φ now runs over all colourings which are i on the boundary. Clearly ζi (S) =
χ(S)
Ni . We define an n-dimensional Hilbert space H by assigning a vector xi to each
9

<!-- page 10 -->
colour and let {xi } be an orthonormal basis for H and we set x∗i = xi . The partition
function for S is now defined by regarding ζi (S) as a coordinate of Z(S) with respect
to the chosen basis, i.e.
X
ζi (S)x⊗b
(40)
Z(S) =
i .
i

−1

It is not hard to check that the theory so defined satisfies all the axioms and Ni 2
are the eigenvalues of the handle operator.

5

Discussion

In this paper we have classified all two-dimensional unitary TQFT’s and shown
how they can be obtained using locally defined weights on triangulated surfaces.
Obviously one would like to generalize some of these results to higher dimensions.
The notions of equivalence and direct sums extend in a straightforward fashion
to dimensions higher than 2. As we have seen any two-dimensional unitary TQFT
can be written as a direct sum of theories for which the space associated with the
circle is 1-dimensional. It is appropriate to call such theories irreducible. It seems to
be of importance to introduce a notion of irreducibility and to establish associated
decomposition properties for TQFT’s in general. A large class of 3-dimensional
TQFT’s has been constructed [15, 16, 17, 18] generalizing the theory of Turaev
and Viro [7] and these theories serve as candidates for irreducible theories since the
dimension of the Hilbert space of the sphere is always 1 and thus they cannot be
decomposed.
A natural question to ask is whether it is true in higher dimensions that the
partition functions for closed manifolds determine a theory up to equivalence as is
the case in two dimensions. If the partition functions for manifolds M with ∂M = Σ
span the Hilbert space associated to Σ for all boundaries Σ, then it is not hard to
show that this is the case. However, this condition is in general not fulfilled. In
the two-dimensional case it holds only if the spectrum of the handle operator is
non-degenerate.

References
[1] E. Witten, Topological quantum field theory, Commun. Math. Phys. 117 (1988)
353.
[2] E. Witten, Quantum field theory and the Jones polynomial, Commun. Math.
Phys. 121 (1989) 351.
10

<!-- page 11 -->
[3] E. Witten, Topological sigma models, Commun. Math. Phys. 118 (1988) 411.
[4] M. Atiyah, Topological quantum field theories, Publ. Math. IHES 68 (1989)
175.
[5] E. Witten, On the structure of the topological phase of two-dimensional gravity,
Nucl. Phys. B 340 (1990) 281.
[6] N. Yu. Reshetikhin and V. G. Turaev, Ribbon graphs and their invariants
derived from quantum groups, Commun. Math. Phys. 127 (1990) 1.
[7] V. G. Turaev and O. Y. Viro, State sum invariants of 3-manifolds and quantum
6j-symbols, Topology 31 (1992) 865.
[8] T. Jonsson, Topological lattice theories in two dimensions, Phys. Lett. B 265
(1991) 141.
[9] T. Jonsson, Topological field theories on simplicial surfaces, Nucl. Phys. B
(Proc. Suppl.) 25 A (1992) 176.
[10] C. Bachas and P. M. S. Petropoulos, Topological models on the lattice and a
remark on string theory cloning, Commun. Math. Phys. 152 (1993) 191.
[11] M. Bordemann, T. Filk and C. Nowak, Topological actions on 2-dimensional
graphs and (graded) metrised algebras, University of Freiburg preprint, THEP
92/18.
[12] M. Fukuma, S. Hosono and H. Kawai, Lattice topological field theory in two
dimensions, Cornell University preprint, CLNS 92/1173.
[13] J. Wheater, Topology and two-dimensional lattice gauge theories, Phys. Lett.
B 264 (1991) 161.
[14] E. Witten, On quantum gauge theories in two dimensions, Commun. Math.
Phys. 141 (1991) 153.
[15] B. Durhuus, H. P. Jakobsen and R. Nest, Topological quantum field theories
from generalized 6j-symbols, Rev. Math. Phys. 5 (1993) 1.
[16] B. Durhuus, A discrete approach to topological quantum field theories, J. of
Geometry and Physics 11 (1993) 155.
[17] G. Felder and O. Grandjean, On combinatorial three-manifold invariants, ETH
preprint (1992).
11

<!-- page 12 -->
[18] S. Chung, M. Fukuma and A. Shapere, Structure of topological lattice field
theories in three dimensions, Cornell University preprint, CLNS 93/1200.

12
