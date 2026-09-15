---
type: paper
date: 1995-05-23
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:q-alg/9505026v1)
reviewed: false
---

# Direct Sum Decompositions and Indecomposable TQFT's

Machine-generated and unreviewed text extraction of arXiv:q-alg/9505026v1
(10 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/q-alg/9505026v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:q-alg/9505026v1 23 May 1995

DIRECT SUM DECOMPOSITIONS AND
INDECOMPOSABLE TQFT’S
STEPHEN SAWIN

Abstract. The decomposition of an arbitrary axiomatic topological quantum field
theory or TQFT into indecomposable theories is given. In particular, unitary
TQFT’s in arbitrary dimensions are shown to decompose into a sum of theories
in which the Hilbert space of the sphere is one-dimensional, and indecomposable
two-dimensional theories are classified.

1. Introduction
In [DJ94], Durhuus and Jonsson define a notion of direct sum of axiomatic topological quantum field theories, or TQFT’s. They show that every unitary TQFT in
two dimensions can be written as a direct sum of theories in which the Hilbert space
associated to the circle is one-dimensional. Such theories are easily classified and are
described in terms of Euler number.
Durhuus and Jonsson leave open two questions: Higher dimensional theories and
nonunitary theories. The first they explicitly address, suggesting every unitary theory
in d dimensions can be decomposed into a direct sum of theories in which the Hilbert
space associated to the sphere S d−1 is one-dimensional. In this paper we give a
complete decomposition theory for TQFT’s over an algebraically closed field, and
describe the indecomposable theories explicitly in two dimensions. In particular we
prove the conjecture suggested by Durhuus and Jonsson.
The nonunitary, indecomposable TQFT’s in two dimensions which we construct are
remarkably degenerate: Any cobordism of genus two or higher gets sent to the zero
operator on the appropriate space. In particular, we construct many counterexamples
to the conjecture that a TQFT is determined by its values on closed manifolds. The
same conjecture for unitary TQFT’s is still open.
This paper is divided into four sections after this introduction. Section 2 defines
TQFT’s and the direct sum operation of Durhuus and Jonsson. Our definition of
TQFT is category theoretic, as this seems to be the most natural setting. Section 3
shows that the vector space associated with the (d−1)-sphere inherits the structure of
a commutative Frobenius algebra from the TQFT, and most importantly that the decomposition of the TQFT into indecomposable theories is exactly the decomposition
1

<!-- page 2 -->
2

STEPHEN SAWIN

of this Frobenius algebra into indecomposable subalgebras. It also classifies indecomposable Frobenius algebras in terms of ordinary indecomposable algebras. This,
together with the parallel theory for unitary TQFT’s and C ∗ -Frobenius algebras,
which is developed along the way, gives a decomposition theory for TQFT’s. Section
4 shows that two-dimensional TQFT’s are determined by their Frobenius algebras,
and gives a partial description of the two-dimensional indecomposable TQFT’s. Section 5 ends with some remarks.
I would like to thank Michael Artin, Scott Axelrod, John Baez, Lisa Sawin, Is
Singer and Washington Taylor for help and conversations. I would also like to thank
John Barrett for pointing out to me the existence of non-semisimple abelian Frobenius
algebras.
2. Axiomatic TQFT’s and Direct Sums
The cobordism category Cob(d) in dimension d has as objects closed, oriented, (d−
1)-dimensional smooth manifolds. A morphism with domain Σ1 and codomain Σ2 ,
called a cobordism from Σ1 to Σ2 , is up to diffeomorphism an oriented d-dimensional
manifold with boundary Σ∗1 ∪ Σ2 , where Σ∗ is the manifold Σ with the opposite
orientation. By ‘up to diffeomorphism’ we mean two morphisms M and M ′ are
considered the same if there is a boundary- and orientation-preserving diffeomorphism
between them. More precisely, a morphism should be a d-manifold M together with
a choice of some subset of the boundary components to be the domain, and a choice
of ordering of the components of the domain and codomain. We will avoid this red
tape and always make the domain, codomain and order clear from context.
Composition is by gluing: If M1 : Σ1 → Σ2 and M2 : Σ2 → Σ3 , then M2 M1 :
Σ1 → Σ3 is the manifold formed by identifying points in M1 and M2 on the shared
boundary Σ2 . The identity 1Σ for each object Σ is the cobordism Σ × I.
Disjoint union gives a tensor product structure on Cob(d). That is, we have a
covariant functor from Cob(d)×Cob(d) to Cob(d) which sends Σ1 ×Σ2 to Σ1 ∪Σ2 , and
if M : Σ1 → Σ2 and M ′ : Σ′1 → Σ′2 then M × M ′ goes to M ∪ M ′ : Σ1 ∪ Σ′1 → Σ2 ∪ Σ′2 .
The empty (d − 1)-manifold ∅ is the trivial object, and the empty d-manifold 1∅ is
the trivial morphism. That is, they are the units for ∪ on objects and morphisms.
Furthermore the cobordism cΣ1 ,Σ2 : Σ1 ∪ Σ2 → Σ2 ∪ Σ1 given by the union of Σ1 × I
with Σ2 × I with the boundary components ordered appropriately, satisfies
cΣ1 ,Σ2 cΣ2 ,Σ1 = 1Σ1 ∪Σ2 ,
cΣ1 ∪Σ2 ,Γ = (cΣ1 ,Γ ⊗ 1Σ2 )(1Σ1 ⊗ cΣ2 ,Γ )
and thus makes the cobordism category a symmetric monoidal or tensor category
[Lan71].
Vect(F) is also a tensor category. The objects are finite-dimensional vector spaces
over a field F, and morphisms with domain V and codomain W are linear maps
from V to W . Composition of morphisms is composition of linear maps, and tensor

<!-- page 3 -->
DIRECT SUM DECOMPOSITIONS AND INDECOMPOSABLE TQFT’S

3

product of objects and morphisms is tensor product of vector spaces and linear maps.
Also 1V is the identity map on V , the trivial object is F, and the trivial morphism is
multiplication by 1 on F.
Definition 1. [Ati89, Ati90] A TQFT is a functor Z of tensor categories from Cob(d)
to Vect(F). Two TQFT’s are considered equivalent if there is a natural isomorphism
between them.
Of course, there is also a duality structure on cobordisms. If M : Σ1 → Σ2 , then
we can consider M ∗ as a cobordism from Σ2 to Σ1 . This kind of duality is analogous
to that in the category Hil of Hilbert spaces and bounded linear functionals, where
each f : H1 → H2 has an adjoint f ∗ : H2 → H1 . This motivates the following
strengthening:
Definition 2. A unitary TQFT is a tensor functor from Cob(d) to Hil such that
Z(M ∗ ) = Z(M)∗ .
Durhuus and Jonsson [DJ94] define the notion of the direct sum of two TQFT’s.
The direct sum of Z1 and Z2 is the theory Z which associates to each connected Σ
the vector space Z1 (Σ) ⊕Z2 (Σ), associates to each disconnected Σ the tensor product
of the vector spaces associated to its components, associates to each connected M
the linear map Z1 (M) ⊕ Z2 (M), interpreted in the obvious way as an operator on the
appropriate vector spaces, and associates to each disconnected M the tensor product
of the values of the components. The reader may check that this is again a TQFT,
and that if Z1 and Z2 are unitary, so is the direct sum.
3. Frobenius Algebras and Decomposition of TQFT’s
Recall that a Frobenius algebra is a finite-dimensional algebra A over a field F,
together with a linear functional µ : A → F such that the bilinear pairing (a, b) =
µ(ab) is nondegenerate. If the pairing is symmetric, for example if the algebra is
commutative, we get what Quinn [Qui95] calls an ambialgebra. If A is a C ∗ -algebra
and µ is a positive functional (i.e., µ(a∗ a) > 0 for all nonzero a ∈ A) then we call A a
C ∗ -Frobenius algebra. The following theorem is essentially due to Dijkgraaf [Dij89].
Let S be the (d − 1)-sphere S d−1 .
Proposition 1. If Z is a d-dimensional TQFT, then Z gives Z(S) the structure
of a commutative Frobenius algebra, and an action of this algebra on Z(Σ) for each
connected (d − 1)-manifold Σ. If Z is unitary, Z(S) is a C ∗ -Frobenius algebra and
the action on Z(Σ) is a C ∗ -representation.
Proof. Let A be Z(S). Multiplication is given by the map Z(M21 ) : A ⊗ A → A,
where M21 is the d-ball with two d-balls removed. The unit is the image of 1 under
the map Z(M01 ) : F → A, where M01 is the d-ball. That it is a unit is immediate,
associativity follows from the fact that both sides of the associativity equation are Z

<!-- page 4 -->
4

STEPHEN SAWIN

of the d-ball with three d-balls removed. Commutativity follows from the fact that
M21 = M21 cS,S .
The map µ is Z(M10 ) : A → F, where M10 is S d with one d-ball removed. The
pairing is then Z(M20 ), where M20 is the d-sphere with two balls removed. To see
that it is nondegenerate, let M02 be the connect sum of two d-balls, and notice (1S ∪
P
M20 )(M02 ∪ 1S ) = 1S , so that if Z(M02 )(1) = i ai ⊗ bi ∈ A ⊗ A, then we have
P
i (x, ai )bi = x, and thus the pairing is nondegenerate. See Figures 1 and 2 for a
pictorial presentation of the Frobenius algebra structure and axioms.

Unit

Mu

Product

Pairing

Figure 1. The structure of a Frobenius algebra

=

=

Associativity

=

=

Unit Axiom

Nondegeneracy

Figure 2. The axioms of a Frobenius algebra
Σ
For the action of A on Z(Σ), let Σ be connected and let M1,Σ
: S ∪ Σ → Σ be
Σ × I with a d-ball removed. It is easy to check that this is an algebra action.
Now suppose that Z is unitary. The fact that the pairing is nondegenerate means
there is a conjugate-linear isomorphism ∗ from A to itself such that (a∗ , b) = ha, bi,
Σ ∗
Σ
where h·, ·i is the inner product on A. Notice that (M1,Σ
) = (1 ∪ M1,Σ
)(M02 ∪ 1), so
P
P
P
that hax, yi = i ha ⊗ x, ai ⊗ bi yi = i hx, ha, ai ibi yi = i hx, (a∗ , ai )bi yi = hx, a∗ yi.
Thus A is a ∗-algebra, and the representation onto each Z(Σ) is a ∗-representation.
Since this representation on Z(S) is faithful, A is a C ∗ -algebra with the operator
norm in this representation, and the representations on Z(Σ) will be C ∗ -algebra
representations. Finally µ(a∗ a) = ha, ai > 0, so µ is positive.

We say that Z is based on the commutative Frobenius algebra A if Z(S) is isomorphic
to A as a Frobenius algebra.
Theorem 1. Suppose Z is based on a direct sum A = A1 ⊕ A2 of Frobenius algebras.
Then there exist TQFT’s Z1 and Z2 , based on A1 and A2 respectively, such that
Z = Z1 ⊕ Z2 . Conversely, If Z decomposes as a direct sum of theories, than the associated Frobenius algebra decomposes as a corresponding direct sum of Frobenius algebras. Further, the same is true for unitary TQFT’s and direct sum of C ∗ -Frobenius
algebras.

<!-- page 5 -->
DIRECT SUM DECOMPOSITIONS AND INDECOMPOSABLE TQFT’S

5

Proof. Let p1 and p2 be the elements of A which correspond to the identities of A1
and A2 respectively, so that pi pj = δi,j pi and p1 + p2 = 1. Thus if we define Zi (Σ) for
Σ connected to be the range of the action of pi , we have that Z(Σ) = Z1 (Σ) ⊕ Z2 (Σ).
Likewise define the action of pi on Z(Σ) for disconnected Σ to be the tensor product
of its action on each connected component, and define Zi (Σ) to be its range. Let pi
act on Z(∅) = F as 1. This defines Z on (d − 1)-manifolds in a manner satisfying the
assumptions of a TQFT.
Now let M : Σ → Γ be a d-cobordism. Define M ′ : S ∪k ∪ Σ → Γ to be M with a dball removed from each of its k components, and define Zi (M)(x) = Z(M ′ )(p⊗k
i ⊗ x)
for x ∈ Z(Σ). Notice if we had removed more than one ball from some components
and put pi ’s in the appropriate tensor factors, we would have gotten the same operator: Removing two d-balls from the same component can be regarded as removing
one d-ball and gluing M21 in, so that we get the same operator as removing one ball
and applying the result to pi · pi = pi . See Figure 3 for a pictorial version of this
argument.
pi

pi

=

pi

pi

=

pi

Figure 3. Removing two balls is the same as removing one
Σ
We claim that Zi (M)Zi (N) = Zi (MN). Since this implies that Zi (M)Z(M1,Σ
)=
Γ
Zi (M)Zi (1Σ ) = Zi (M) = Z(M1,Γ )Zi (M), we have Zi (M) : Zi (Σ) → Zi (Γ) and Zi
is a functor. Since Zi (M ∪ N) = Zi (M) ⊗ Zi (N), it is a tensor functor and hence a
TQFT.
To see this claim, notice that Zi (M)Zi (N)(x) is Z(K)(p⊗n
i ⊗ x), where K is MN
with some positive number of d-balls removed from each component. We have already
seen this is the same as Zi (MN) (see Figure 4).

pi

pi

pi

=

pi

pi

=

Figure 4. The action of pi intertwines composition
Thus Zi is a TQFT.
Is Z = Z1 ⊕ Z2 ? For Σ connected we have Z(Σ) = Z1 (Σ) ⊕ Z2 (Σ), and clearly if Σ
is not connected, then Z(Σ) is the tensor product of Z of the connected components.
If M is connected, then Zi (M)(x) = Z(M ′ )(pi ⊗ x), so Z1 (M)(x) + Z2 (M)(x) =

<!-- page 6 -->
6

STEPHEN SAWIN

Z(M ′ )((p1 + p2 ) ⊗ x) = Z(M)(x). Likewise, if M is disconnected then Z(M) is the
tensor product of the values of Z on the connected components. Thus Z = Z1 ⊕ Z2 .
The converse is easy. If Z = Z1 ⊕ Z2 , then µ = Z(M10 ) = Z1 (M10 ) ⊕ Z2 (M10 ) =
µ1 ⊕ µ2 . Also m = Z(M21 ) = Z1 (M21 ) ⊕ Z2 (M21 ) = m1 ⊕ m2 , where m, m1 , and m2
represent the products in A, A1 and A2 respectively. Thus A = A1 ⊕ A2 .
If Z is unitary and its C ∗ -Frobenius algebra A decomposes as C ∗ -Frobenius algebra
into a direct sum A1 ⊕ A2 , then the above argument shows that Z = Z1 ⊕ Z2 as
TQFT’s: We just need to show that Zi is unitary. But pi is a self-adjoint projection,
since the direct sum was as a C ∗ -algebra direct sum, so
hy, Zi(M)xi = hy, Z(M)(pi x)i
= hZ(M)∗ y, pi xi
= hpi Z(M ∗ )y, xi
= hZ(M ∗ )(pi y), xi
= hZi (M ∗ )y, xi.
Thus Zi is unitary. Conversely, if Z = Z1 ⊕ Z2 is a direct sum of unitary theories,
then the subspaces A1 and A2 of A are orthogonal, so the C ∗ -norm is the direct sum
norm and the involution is the direct sum involution.
Thus the direct sum decomposition of a TQFT corresponds exactly to the direct
sum decomposition of its associated commutative Frobenius algebra. Indecomposable commutative C ∗ -Frobenius algebras are easy to classify: For λ ∈ R+ , define the
commutative C ∗ -Frobenius algebra Cλ to be the C ∗ -algebra C, with µ(x) = λ−1 x. It
is clearly a simple C ∗ -algebra, and µ is positive. Since the only indecomposable commutative C ∗ -algebra is one-dimensional, it is clear this exhausts all the possibilities.
Corollary 1. Every unitary TQFT is a direct sum of unitary TQFT’s, each based
on the Frobenius algebra Cλ for some λ. In particular, every unitary TQFT is the
direct sum of theories with one-dimensional Z(S d−1 ).
The story is a bit more complicated for arbitrary Frobenius algebras, because
there are so many commutative algebras. Nevertheless, we can get a fairly complete
description modulo this issue. Assume F is algebraically closed. For each λ ∈ F
nonzero, let Sλ be the algebra F with µ(x) = λ−1 x. Also, let A be a commutative
algebra spanned by the identity and at least one nilpotent, and suppose the socle,
the space of all x ∈ A such that ax = 0 for all nilpotent a ∈ A, is one-dimensional.
Let µ be any linear functional on A which is nonzero on the socle. Let NA,µ be this
algebra together with this functional.
Proposition 2. Sλ and NA,µ are indecomposable Frobenius algebras. Further, every
commutative indecomposable Frobenius algebra is isomorphic to one of these, and
these are nonisomorphic up to algebra isomorphism.

<!-- page 7 -->
DIRECT SUM DECOMPOSITIONS AND INDECOMPOSABLE TQFT’S

7

Proof. Obviously Sλ is an indecomposable Frobenius algebra. Now consider NA,µ .
Notice for any finite-dimensional algebra there is a bound on the number of nilpotent
elements which can be multiplied to get a nonzero product. Thus for any x ∈ A, there
must be a y ∈ A such that xy is a nonzero element of the socle, for otherwise we would
be able to write an arbitrarily long product of nilpotents times x which is nonzero. For
this y we have µ(xy) is nonzero, and thus the bilinear form is nodegenerate. So NA,µ
is a Frobenius algebra. It is clearly indecomposable, because A is indecomposable.
To see that every indecomposable Frobenius algebra is one of the above, first note
that if a Frobenius algebra decomposes into a direct sum as an algebra, it decomposes in the same way as a Frobenius algebra, because the summands are orthogonal
subspaces with respect to the bilinear pairing, and thus the bilinear pairing is nondegenerate when restricted to each. So every indecomposable Frobenius algebra is also
indecomposable as an algebra. Thus it is spanned by the identity and nilpotents. If
it has no nilpotents, then it is one-dimensional, and it is clearly isomorphic to exactly
one Sλ . If it has nilpotents, then arguing as above it has a nonempty socle. Every
element of the socle is orthogonal to all nilpotent elements, so the socle is dual to
the space spanned by the identity, and thus is one-dimensional. So the algebra is
isomorphic to exactly one of the algebras used to construct the N’s. Clearly µ must
be nonzero on the socle, or otherwise the socle would be orthogonal to all of A. Thus
the algebra isomorphism extends to a Frobenius algebra isomorphism to exactly one
NA,µ.
We call a TQFT simple if it is based on Sλ , i.e., if Z(S) is one-dimensional. We
call a TQFT based on NA,µ nilpotent.
Corollary 2. Every TQFT is a direct sum of simple and nilpotent theories.
4. TQFT’s in Two Dimensions
In two dimensions, the Frobenius algebra completely determines the TQFT. The
following theorem is due to Dijkgraaf [Dij89].
Theorem 2. There is exactly one two-dimensional TQFT based on a given commutative Frobenius algebra. There is exactly one two-dimensional unitary TQFT based
on a given commutative C ∗ -Frobenius algebra.
Proof. First let us construct the TQFT from a given commutative Frobenius algebra
A. Certainly the vector space associated to n copies of S 1 is A⊗n and to the empty
one-manifold is F. We must associate operators to two-manifolds. Clearly Z(M21 )
is the product, Z(M10 ) is µ, Z(M01 ) is the identity, and Z(M12 ) is the dual map to
the product under the pairing. If M is any two-dimensional cobordism, use a Morse
function to write it as a product of cobordisms, each of which is a union of some
number of copies of 1S with one of M10 , M01 , M12 , M21 . The value of Z on such a
cobordism is determined by the requirement of tensor functoriality and the values of

<!-- page 8 -->
8

STEPHEN SAWIN

these four cobordisms. To check it does not depend on the Morse function, recall by
Cerf theory [Cer70] that any change of Morse function has the effect of a sequence of
the following moves, illustrated in Figure 5:
(i) Mnm 1S ∪n = Mnm = 1S ∪m Mnm
(ii) (M10 ∪ 1S )(M12 ) = (1S ∪ M10 )(M12 ) = 1S = M21 (M01 ∪ 1S ) = M21 (1S ∪ M01 )
(iii) (M21 ∪ 1S )(1S ∪ M12 ) = M12 M21 = (1S ∪ M21 )(M12 ∪ 1S ).
=
(i)

=

=
(ii)

=
(iii)

Figure 5. Moves of Cerf theory
Our construction of Z(M) is clearly invariant under (i). Move (ii) is just the
statement that 1 ∈ A is the identity, and that µ is dual to the identity. For (iii)
P
notice Z(M12 )(x) = i xai ⊗ bi , where ai is a basis of A and bi is its dual basis.
P
Then the left-hand side of (iii) on x ⊗ y is xyai ⊗ bi = Z(M12 )Z(M12 )(x ⊗ y), the
P
right-hand side. Likewise Z(M12 )(x) = ai ⊗ xbi , showing the other equality. Thus
Z(M) is well-defined.
A Morse function on M1 and M2 gives a Morse function on M1 M2 , so Z(M1 M2 ) =
Z(M1 )Z(M2 ). Clearly Z(1S ∪n ) = 1A⊗n , so Z is a functor. It is easy to check that
it takes union of one-manifolds and cobordisms to tensor product of vector-spaces
and operators respectively, the empty one- and two-manifold get sent to F and 1
respectively, and that permutation of components corresponds to permutation of
tensor factors. Thus Z is a TQFT.
If Z ′ is another TQFT based on the same Frobenius algebra A, the identification
of the Frobenius algebras gives a linear isomorphism between the vector spaces of Z
and Z ′ . What’s more, this map intertwines Z(Mnm ) with Z ′ (Mnm ) with m, n = 0, 1, 2
as above, since their value is determined by the Frobenius algebra. The fact that Z
and Z ′ are tensor functors then ensures that the isomorphism intertwines Z(M) with
Z ′ (M). Since it obviously intertwines the tensor product structure, this is a natural
isomorphism.
If A is a C ∗ -Frobenius algebra, then ha, bi = µ(a∗ b) defines a positive-definite inner
product on A, and hence on every vector space associated with the theory. One need
only check that Z(M10 ) = Z(M01 )∗ and Z(M12 ) = Z(M21 )∗ .
Thus there is a two-dimensional indecomposable TQFT associated to each Sλ
and each NA,µ, and an indecomposable unitary TQFT to each Cλ , and every twodimensional TQFT is a direct sum of these.
It is worth noting what these theories look like. Following Durhuus and Jonsson
[DJ94], we check that in the theory Zλ associated to Sλ , every vector space can be

<!-- page 9 -->
DIRECT SUM DECOMPOSITIONS AND INDECOMPOSABLE TQFT’S

9

associated to F in such a way that Zλ (M) = λ−χ(M )/2 , where χ(M) is the Euler
number.
For the nilpotent case, we will of course not be able to give a simple description of
the whole TQFT ZA,µ , but we can describe a surprisingly large amount.
We can write a chain of ideals A = Nn ⊃ Nn−1 ⊃ · · · ⊃ N1 , where N1 is the socle,
and each Nk is the preimage in A of the socle of A/Nk−1 . Choose a basis for ai of A
which restricts to a basis of each Nk , and let bi be its dual basis. We claim ai bi = s,
where s is the element of the socle with µ(s) = 1. To see this, notice if ai ∈ Nk and y
is nilpotent, then yai ∈ Nk−1 , and hence can be written as a linear combination of aj
for j 6= i. Thus yai bi = 0, and ai bi is in the socle. Since µ(ai bi ) = 1, we have ai bi = s.
Now let M = M21 M12 , a twice-punctured torus. Then
Z(M)(x) =

X

xai bi = dim(A)xs = dim(A)f (x)s

i

where f (x) is the functional on A which is 1 on the identity and zero on the nilpotents
(the unique homomorphism to F). From this one easily concludes that the torus with
n incoming punctures and m outgoing punctures is sent to the operator
xi ⊗ · · · ⊗ xn 7→ f (x1 ) · · · f (xn ) dim(A)s⊗m
and any manifold of genus more than one gets sent to the operator 0 on the appropriate space.
5. Remarks
• It would be nice to find an action or state sum definition of the two-dimensional
nilpotent TQFT’s ZA,µ . There is no obvious impediment to this, but the surprising behavior of this TQFT would appear to make it difficult.
• It has been asked (e.g. by [DJ94]) whether two TQFT’s which agree on all
closed d-manifolds are naturally isomorphic. The answer is no, even in two
dimensions, if we do not restrict to unitary theories. For any ZA,µ the sphere
gets sent to µ(1), the torus gets sent to dim(A), and all others get sent to
zero. Clearly many different A and µ give the same values for these, and
since they correspond to nonisomorphic Frobenius algebras, they correspond
to inequivalent TQFT’s. The values on closed d-manifolds does determine the
TQFT for 2-dimensional unitary and semisimple theories.
• It is clear that the proofs of Proposition 1 and Theorem 2 really only involve
the category of cobordisms. Thus it would be natural to express them as
corollaries to purely topological theorems about this category. Specifically,
we could define the notion of a Frobenius object in a tensor category, and a
Frobenius action of one object on another. Then Proposition 1 follows from
the statement that S is a Frobenius object in Cob(d) with a Frobenius action

<!-- page 10 -->
10

STEPHEN SAWIN
P

on each connected , and Theorem 2 from the statement that Cob(2) is the
free tensor category generated by one Frobenius object.
• If Z is a d dimensional TQFT, and X is an r-manifold for r < d, then Z and
X together naturally give a (d − r)-dimensional TQFT, which assigns to each
(d−r−1)-manifold Σ the vector space Z(Σ×X), and to each (d−r)-cobordism
M the operator Z(M × X). In particular for each (d − 2)-manifold we get a
two-dimensional TQFT, which we can classify as in the previous section. This
classification should give important information about the TQFT in a simple
format. For example, if we take the Chern-Simons TQFT and X = S 1 , we
−1
get a sum of simple TQFT’s with λi = S0,i
.
References
[Ati89] M. F. Atiyah. Topological quantum field theories. Publ. Math. IHES, 68:175–186, 1989.
[Ati90] M. F. Atiyah. The Geometry and Physics of Knots. Lezioni Lincee. Cambridge University
Press, 1990.
[Cer70] J. Cerf. La stratification naturelle des espaces de fonctions différentiables réeles et la théorèm
de la pseudoisotopie. Publ. Math. I.H.E.S., 39, 1970.
[Dij89] R. H. Dijkgraaf. A Geometric Approach To Two-Dimensional Conformal Field Theory. PhD
thesis, University of Utrecht, 1989.
[DJ94] B. Durhuus and T. Jonsson. Classification and construction of unitary topological quantum
field theories in two dimensions. J. Math. Phys., 35(10):5306–5313, October 1994.
[Lan71] S. Mac Lane. Categories For the Working Mathematician. Graduate Texts in Mathematics.
Springer-Verlag, New York-Heidelberg-Berlin, 1971.
[Qui95] F. Quinn. Lectures on axiomatic topological quantum field theory. In D. Freed and K. Uhlenbeck, editors, Geometry and Quantum Field Theory, volume 1 of IAS/Park City Mathematics Series. AMS/IAS, 1995.
Math Dept. 2-265, MIT, Cambridge, MA 02139-4307, (617) 253-4995
E-mail address: sawin@math.mit.edu
