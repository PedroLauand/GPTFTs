---
type: paper
date: 2015-07-22
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1507.06278v3)
reviewed: false
---

# Some Nearly Quantum Theories

Machine-generated and unreviewed text extraction of arXiv:1507.06278v3
(12 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1507.06278v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Some Nearly Quantum Theories
Howard Barnum

Matthew A. Graydon

Alexander Wilce

University of New Mexico
Albuquerque, USA
hnbarnum@aol.com

Perimeter Institute for Theoretical Physics
Waterloo, Canada
Institute for Quantum Computing, University of Waterloo
Waterloo, Canada
mgraydon@perimeterinstitute.ca

Susquehanna University
Selinsgrove, USA
wilce@susqu.edu

We consider possible non-signaling composites of probabilistic models based on euclidean Jordan
algebras. Subject to some reasonable constraints, we show that no such composite exists having the
exceptional Jordan algebra as a direct summand. We then construct several dagger compact categories of such Jordan-algebraic models. One of these neatly unifies real, complex and quaternionic
mixed-state quantum mechanics, with the exception of the quaternionic “bit”. Another is similar,
except in that (i) it excludes the quaternionic bit, and (ii) the composite of two complex quantum
systems comes with an extra classical bit. In both of these categories, states are morphisms from
systems to the tensor unit, which helps give the categorical structure a clear operational interpretation. A no-go result shows that the first of these categories, at least, cannot be extended to include
spin factors other than the (real, complex, and quaternionic) quantum bits, while preserving the representation of states as morphisms. The same is true for attempts to extend the second category to
even-dimensional spin-factors. Interesting phenomena exhibited by some composites in these categories include failure of local tomography, supermultiplicativity of the maximal number of mutually
distinguishable states, and mixed states whose marginals are pure.

1

Introduction

A series of recent papers [17, 12, 18, 16, 5] have shown that any of various packages of probabilistic
or information-theoretic axioms force the state spaces of a finite-dimensional probabilistic theory to be
those of formally real, or euclidean, Jordan algebras. Thus, euclidean Jordan algebras (hereafter, EJAs)
form a natural class of probabilistic models. Moreover, it is one that keeps us in the general neighborhood of standard quantum mechanics, owing to the classification of simple EJAs as self-adjoint parts of
real, complex and quaternionic matrix algebras (corresponding to real, complex and quaternionic quantum systems), the exceptional Jordan algebra of self-adjoint 3 × 3 matrices over the octonions, and one
further class, the so-called spin factors. The latter are essentially “bits”: their state-spaces are balls of
arbitrary dimension, with pairs of antipodal points representing maximal sets of sharply distinguishable
states.1
This raises the question of whether one can construct probabilistic theories (as opposed to a collection
of models of individual systems) in which finite-dimensional complex quantum systems can be accommodated together with several — perhaps all — of the other basic types of EJAs listed above. Ideally,
these would be symmetric monoidal categories; even better, we might hope to obtain compact closed, or
still better, dagger-compact, categories of EJAs [1]. Also, one would like the resulting theory to embrace
mixed states and CP mappings.
In this paper, we exhibit two dagger-compact categories of EJAs — called URUE and URSE, acronyms
1 Where this ball has dimension 2, 3 or 5, these are just the state spaces of real, complex and quaternionic quantum bits.

Chris Heunen, Peter Selinger, and Jamie Vicary (Eds.):
12th International Workshop on Quantum Physics and Logic (QPL 2015).
EPTCS 195, 2015, pp. 59–70, doi:10.4204/EPTCS.195.5

c H. Barnum, M. A. Graydon & A. Wilce

<!-- page 2 -->
Some Nearly Quantum Theories

60

that will be explained below — that include all real, complex and quaternionic matrix algebras, with one
exception: the quaternionic bit, or “quabit”, represented by M2 (H)sa , cannot be added to URUE without
destroying compact closure and the representation of states as morphisms. URSE includes a faithful
copy of finite-dimensional complex quantum mechanics, while in URUE, composites of complex quantum systems come with an extra classical bit — that is, a {0, 1} valued superselection rule.
There is scant hope of including more exotic Jordan algebras in a satisfactory categorical scheme. Even
allowing for a very liberal definition of composite (our Definition 1 below), the exceptional Jordan algebra is ruled out altogether (Corollary 1), while non-quantum spin factors are ruled out if we want to
regard states as morphisms — in particular, if we demand compact closure (see Example 1). Combined
with the results of (any of) the papers cited above that derive a euclidean Jordan-algebraic structure from
information-theoretic assumptions, these results provide a compelling motivation for a kind of unified
quantum theory that accommodates real, complex and quaternionic quantum systems (possibly modulo
the quabit) and permits the formation of composites of these.
A condition frequently invoked to rule out real and quaternionic QM is local tomography: the doctrine
that the state of a composite of two systems should depend only on the joint probabilities it assigns to
measurement outcomes on the component systems. Indeed, it can be shown [7] that standard complex
QM with superselection rules is the only dagger-compact category of EJAs that includes the qubit. Accordingly, URUE and URSE are not locally tomographic. In our view, the very existence of these quite
reasonable, well-behaved categories suggests that local tomography is not as well-motivated as is sometimes supposed.
A broadly similar proposal is advanced by Baez [3], who points out that one can view real and quaternionic quantum systems as pairs (H, J), where H is a complex Hilbert space and J is an anti-unitary
satisfying J 2 = 1 (the real case) or J 2 = −1 (the quaternionic case). This yields a symmetric monoidal
category in which objects are such pairs, morphisms (H1 , J1 ) → (H2 , J2 ) are linear mappings intertwining J1 and J2 , and (H1 , J1 )⊗ (H2 , J2 ) = (H1 ⊗ H2 , J1 ⊗ J2 ). The precise connection between this approach
and ours is still under study.
A forthcoming paper [4] will provide more details, including full proofs of the results presented here, as
well as additional results obtained since our presentation of this paper at QPL XII.

2

Euclidean Jordan algebras

We begin with a concise review of some basic Jordan-algebraic background. References for this section
are [2] and [8]. A euclidean Jordan algebra (hereafter: EJA) is a finite-dimensional commutative real
algebra (A, ) with a multiplicative unit element u, satisfying the Jordan identity

·

··

· ·

a2 (a b) = a (a2 b)
for all a, b ∈ A, and equipped with an inner product satisfying

·

·

ha b|ci = hb|a ci
for all a, b, c ∈ A. The basic example is the self-adjoint part Msa of a real, complex or quaternionic matrix
algebra M, with a b = (ab + ba)/2 and with ha|bi = tr(ab). Any Jordan subalgebra of an EJA is also an
EJA. So, too, is the spin factor Vn = R × Rn , with the obvious inner product and with

·

·

(t, x) (s, y) = (ts + hx|yi,ty + sx) :

<!-- page 3 -->
H. Barnum, M. A. Graydon & A. Wilce

61

this can be embedded (universally) in M2k (C)sa for n = 2k and M2k (C)sa ⊕ M2k (C)sa for n = 2k + 1.
Moreover, one can show that
V2 ≃ M2 (R)sa , V3 ∼
= M2 (C)sa , and V5 ≃ M2 (H)sa .

Classification Direct sums of EJAs are also EJAs, so we can obtain more examples by forming direct
sums of the EJAs of the types mentioned above. The Jordan-von Neumann-Wigner Classification Theorem (see [8] Chapter IV) provides a converse: every euclidean Jordan algebra is a direct sum of simple
EJAs, each of which is isomorphic to a spin factor Vn , or to the self-adjoint part of a matrix algebra
Mn (K) where K is one of the classical division rings R, C or H, or, if n = 3, to the Octonions, O. This
last example, which is not embeddable into the self-adjoint part of a complex matrix algebra, is called
the exceptional Jordan algebra, or the Albert algebra. A Jordan algebra that is embeddable in Mn (C)sa
for some n, is said to be special. It follows from the classification theorem that any EJA decomposes as
a direct sum Asp ⊕ Aex where Asp is special and Aex is a direct sum of copies of the exceptional Jordan
algebra.
Projections and the Spectral Theorem A projection in an EJA A is an element p ∈ A with p2 = p. If
p, q are projections with p q = 0, we say that p and q are orthogonal. In this case, p + q is another projection. A projection not representable as a sum of other projections is said to be minimal or primitive.
A Jordan frame is a set E ⊆ A of pairwise orthogonal minimal projections that sum to the Jordan unit.
The Spectral Theorem (cf. e.g. [8], Theorem III.1.1) for EJAs asserts that every element a ∈ A can be
expanded as a linear combination a = ∑x∈E tx x where E is some Jordan frame.

·

One can show that all Jordan frames for a given Euclidean Jordan algebra A have the same number of
elements. This number is called the rank of A. By the Classification Theorem, all simple Jordan algebras
having rank 4 or higher are special.
Order Structure Any EJA A is at the same time an ordered real vector space, with positive cone
A+ = {a2 |a ∈ A}; for a, b ∈ A, a ≤ b iff b − a ∈ A+ . This allows us to interpret A as a probabilistic
model: an effect (measurement-outcome) in A is an element a ∈ A+ with a ≤ u. A state on A is a positive
linear mapping α : A → R with α (u) = 1. If a is an effect, we interpret α (a) as the probability that a
will be observed (if tested) in the state α .
The cone A+ is self-dual with respect to the given inner product on A: an element a ∈ A belongs to A+
iff ha|bi ≥ 0 for all b ∈ A+ . Every state α then corresponds to a unique b ∈ A+ with α (a) = ha|bi.
Remark: Besides being self-dual, the cone A+ is homogeneous: any element of the interior of A+ can be
obtained from any other by an order-automorphism of A, that is, a linear automorphism φ : A → A with
φ (A+ ) = A+ . The Koecher-Vinberg Theorem ([11, 15]; see [8] for a relatively accessible proof based on
the one in [13]) identifies EJAs as precisely the finite-dimensional ordered linear spaces having homogeneous, self-dual positive cones. This fact underwrites the derivations in several of the papers cited above
[17, 18, 16].2
Reversible and universally reversible EJAs A Jordan subalgebra of Msa , where M is a complex ∗algebra, is reversible iff
a1 , ..., ak ∈ A ⇒ a1 a2 · · · ak + ak · · · a2 a1 ∈ A,
2 A different characterization of EJAs, in terms of projections associated with faces of the state space, is invoked in [5].

<!-- page 4 -->
Some Nearly Quantum Theories

62

where juxtaposition indicates multiplication in M. Note that with k = 2, this is just closure under the
Jordan product on Msa . An abstract EJA A is reversible iff it has a representation as a reversible Jordan
subalgebra of some complex ∗-algebra. A reversible EJA is universally reversible (UR) iff it has only
reversible representations.
Universal reversibility will play a large role in what follows. Of the four basic types of special Euclidean
Jordan algebra considered above, the only ones that are not UR are the spin factors Vk with k ≥ 4. For
k = 4 and k > 5, Vk is not even reversible; V5 — equivalently, M2 (H)sa — has a reversible representation,
but also non-reversible ones. Thus, if we adopt the shorthand
Rn = Mn (R)sa , Cn = Mn (C)sa , and Qn = Mn (H)sa ,
we have Rn ,Cn UR for all n, and Qn UR for n > 2.

3

Composites of EJAs

A probabilistic theory must allow for some device for describing composite systems. Given EJAs A and
B, understood as models for two physical systems, we’d like to construct an EJA AB that models the two
systems considered together as a single entity. Is there any satisfactory way to do this? If so, how much
latitude does one have?
A good candidate for such an EJA is provided by a construction due to Hanche-Olsen [9], which we now
review. In the sequel, we show that, at least if no non-UR spin factors are involved, it does provide such
a model.
The universal tensor product A representation of a Jordan algebra A is a Jordan homomorphism π :
A → Msa , where M is a complex ∗-algebra. For any EJA A, there exists a (possibly trivial) ∗-algebra
C∗ (A) and a representation ψA : A → C∗ (A)sa with the universal property that any representation π : A →
Msa , where M is a C∗ -algebra, decomposes uniquely as π = π̃ ◦ ψA , π̃ : C∗ (A) → M a ∗-homomorphism.
Evidently, (C∗ (A), ψA ) is unique up to a canonical ∗-isomorphism. Since ψ op : A → C∗ (A)op provides
another solution to the same universal problem, there exists a canonical anti-automorphism ΦA on C∗ (A),
fixing every point of ψA (A).
We refer to (C∗ (A), ψA ) as the universal representation of A. A is exceptional iff C∗ (A) = {0}. If A
has no exceptional factors, then ψA is injective. In this case, we will routinely identify A with its image
ψA (A) ≤ C∗ (A).
In [9], Hanche-Olsen defines the universal tensor product of two special EJAs A and B to be the Jordan
subalgebra of C∗ (A) ⊗C∗ (B) generated by A ⊗ B. This is denoted A e
⊗B. It can be shown that
C∗ (A e
⊗B) = C∗ (A) e
⊗C∗ (B) and ΦA e⊗B = ΦA ⊗ ΦB .
Some further important facts about the universal tensor product are the following:
Proposition 1 Let A, B and C denote EJAs.
(a) If φ : A → C, ψ : B → C are unital Jordan homomorphisms with operator-commuting ranges3 , then
there exists a unique Jordan homomorphism A e
⊗B → C taking a ⊗ b to φ (a) ψ (b) for all a ∈ A,
b ∈ B.

·

·(y·z) = y·(x·z) for all z ∈ C.

3 Elements x, y ∈ C operator commute iff x

<!-- page 5 -->
H. Barnum, M. A. Graydon & A. Wilce

63

(b) A e
⊗B is UR unless one of the factors has a one-dimensional summand and the other has a representation onto a spin factor Vn with n ≥ 4.
(c) If A is UR, then A e
⊗Mn (C)sa = (C∗ (A) ⊗ Mn(C))sa .
These are Propositions 5.2, 5.3 and 5.4, respectively, in [9].
e will always be UR, hence,
Note that part (b) implies that if A and B are irreducible and non-trivial, A⊗B
the fixed-point set of ΦA ⊗ ΦB . Using this one can compute A e
⊗B for irreducible, universally reversible A
and B [9]. Below, and for the balance of this paper, we use the shorthand Rn := Mn (R)sa , Cn = Mn (C)sa
and Qn = Mn (H)sa (noting that Qn is UR only for n > 2):
e
⊗
Rm
Cm
Qm
Rn Rnm
Cnm
Qnm
Cn Cnm Cnm ⊕Cnm C2nm
C2nm
R4nm
Qn Qnm
Figure 2
For Q2 e
⊗Q2 , a bit more work is required, but one can show that Q2 e
⊗Q2 is the direct sum of four copies
of R16 = M16 (R)sa (stated in [9]; details will be provided in [4]).
General composites of EJAs The universal tensor product is an instance of the following (as it proves,
only slightly) more general scheme. Recall that an order-automorphism of an EJA A is a linear bijection
φ : A → A taking A+ onto itself. These form a Lie group, whose identity component we denote by G(A).
Definition 1: A composite of EJAs A and B is a pair (AB, π ) where AB is an EJA and π : A ⊗ B → AB is
a linear mapping such that
(a) If a ∈ A+ and b ∈ B+ , then π (a ⊗ b) ∈ (AB)+ , with π (u ⊗ u) the Jordan unit of AB;
(b) for all states α on A, β on B, there exists a state γ on AB such that γ (π (a ⊗ b)) = α (a)β (b);
(c) for all automorphisms φ ∈ G(A) and ψ ∈ G(B), there exists a preferred automorphism φ ⊗ ψ ∈
G(AB) with (φ ⊗ ψ )(π (a ⊗ b)) = π (φ (a) ⊗ ψ (b)). Moreover, we require that
(φ1 ⊗ ψ1 ) ◦ (φ2 ⊗ ψ2 ) = (φ1 ◦ φ2 ) ⊗ (ψ1 ◦ ψ2 )
and
(φ ⊗ ψ )† = φ † ⊗ ψ †
for all φ , φi ∈ G(A) and ψ , ψi ∈ G(B).
It follows from (b) that π is injective (if π (T ) = 0, then for any states α , β , there’s a state γ of AB with
(α ⊗ β )(T ) = γ (π (T )) = 0; it follows that T = 0). Henceforth, we’ll simply regard A ⊗ B as a subspace
of AB.
Condition (c) calls for further comment. The dynamics of a physical system modeled by a Euclidean Jordan algebra A will naturally be represented by a one-parameter group t 7→ φt of order automorphisms of
A. As order-automorphisms in G(A) are precisely the elements of such one-parameter groups, condition
(c) is equivalent to the condition that, given dynamics t 7→ φt and t 7→ ψt on A and B, respectively, there
is a preferred dynamics on AB under which pure tensors a ⊗ b evolve according to a ⊗ b 7→ φt (a) ⊗ ψt (b).
In other words, there is a dynamics on AB under which A and B evolve independently.

<!-- page 6 -->
Some Nearly Quantum Theories

64

Theorem 1: If A and B are simple EJAs, then any composite AB is special, and an ideal in A e
⊗B.
The basic idea of the proof is to show that if p1 , ..., pn is a Jordan frame in an irreducible summand of A,
and q1 , ..., qm is a Jordan frame in an irreducible summand of B, then {pi ⊗ q j |i = 1, ..., n, j = 1, ..., m} is a
pairwise orthogonal set of projections in AB, whence, the latter has rank at least four, and must therefore
be special. For the details, we refer to [4].
Corollary 1: If A is simple and B is exceptional, then no composite AB exists.
In particular, if B is the exceptional factor, there exists no composite of B with itself.
Corollary 2: If A e
⊗B is simple, then AB = A e
⊗B is the only possible composite of A and B.
There are cases in which A e
⊗B isn’t simple, even where A and B are: namely, the cases in which A and B
are both hermitian parts of complex matrix algebras. From table (2), we see that if A = Cn and B = Cm ,
e = Cnm ⊕ Cnm . In this case, Proposition 1 gives us two choices for AB: either the entire direct
then A⊗B
sum above, or one of its isomorphic summands, i.e., the “obvious” composite AB = Cnm .

4

Embedded EJAs

Corollary 1 above justifies restricting our attention to special EJAs. These are precisely the finite dimensional JC-algebras, i.e. the ones isometrically isomorphic to norm closed Jordan subalgebras of
self-adjoint linear operators on complex Hilbert spaces [9][10]. In fact, it will be helpful to consider
embedded JC-algebras, that is, Jordan subalgebras of specified finite-dimensional C∗ algebras.
Definition 2: An embedded JC algebra, or EJC, is a pair (A, MA ) where A is a unital Jordan subalgebra
of a unital finite-dimensional complex ∗-algebra MA (that is, a Jordan subalgebra such that the Jordan
unit uA coincides with the unit of MA ).
The notation MA is intended to emphasise that the embedding A 7→ MA is part of the structure of interest.
Given A, there is always a canonical choice for MA , namely the universal enveloping ∗-algebra C∗ (A) of
A [9].
Definition 3: The canonical product of EJCs (A, MA ) and (B, MB ) is the pair (A ⊙ B, MA ⊗ MB ) where
A ⊙ B is the Jordan subalgebra of (MA ⊗ MB)sa generated by the subspace A ⊗ B.
Note that, as a matter of definition, MA⊙B = MA ⊗ MB . If MA = C∗ (A) and MB = C∗ (B), then A ⊙ B is
the Hanche-Olsen tensor product.
One would like to know that A ⊙ B is in fact a composite of A and B in the sense of Definition 1. Using
a result of Upmeier [14], we can show that this is the case for reversible EJAs A and B. (that is, real,
complex and quaternionic systems, and direct sums of these). Whether A ⊙ B is a composite in the sense
of Definition 1 when A or B is non-reversible spin factor remains an open question.
We can now form a category:
Definition 4: EJC is the category consisting of EJCs (A, MA ) and completely positive (CP) maps
φ : MA → MB with φ (A) ⊆ B. We refer to such maps as Jordan preserving.
Proposition 2: The canonical product ⊙ is associative on EJC. More precisely, the associator mapping

α : MA ⊗ (MB ⊗ MC ) → (MA ⊗ MB ) ⊗ MC
takes A ⊙ (B ⊙C) to (A ⊙ B) ⊙C.

<!-- page 7 -->
H. Barnum, M. A. Graydon & A. Wilce

65

(Note that since the associator mapping is CP, this means that α is a morphism in EJC.) The proof is
somewhat lengthy, so we refer the reader to the forthcoming paper [4].
Proposition 2 suggests that EJC might be symmetric monoidal under ⊙. There is certainly a natural
choice for the monoidal unit, namely I = (R, C). But the following example shows that tensor products
of EJC morphisms are generally not morphisms:
Example 1: Let (A,C∗ (A)) and (B,C∗ (B)) be simple, universally embedded EJCs, and suppose that B is
not UR (e.g., a spin factor Vn with n > 3). Let Bb be the set of fixed points of the canonical involution ΦB .
e the set of fixed points of ΦA ⊗ ΦB . In particular, uA ⊗ Bb is contained
Then by Corollary 2, A ⊙ B = A⊗B,
in A ⊙ B. Now let f be a state on C∗ (A): this is CP, and trivially Jordan-preserving, and so, a morphism
in EJC. But
b = f (uA )Bb = B,
b
( f ⊗ idB )(uA ⊗ B)
which isn’t contained in B. So f ⊗ idB isn’t Jordan-preserving.

5

Reversible and universally reversible EJCs

It seems that the category EJC is simply too large. We can try to obtain a better-behaved category by
restricting the set of morphisms, or by restricting the set of objects, or both.
As a first pass, we might try this:
Definition 5: Let (A, MA ) and (B, MB ) be EJCs. A CP map φ : MA → MB is completely Jordan preserving (CJP) iff φ ⊗ 1C takes A ⊙C to B ⊙C for all (C, MC ).
It is not hard to verify the following
Proposition 3: If φ : MA → MB and ψ : MC → MD are CJP, then so is

φ ⊗ ψ : MA⊙C = MA ⊗ MB → MB ⊗ MC = MB⊙D .

Thus, the category of EJC algebras and CJP mappings is symmetric monoidal.4
There are many examples of CJP mappings: Jordan homomorphisms are CJP maps. If a ∈ A, the mapping
Ua : A → A
given by Ua = 2La2 − L2a , where La (b) = ab, is also CJP. On the other hand, by Example 1 above,
CJP(A, I) is empty for universally embedded simple A!
So not all CP maps are CJP; for instance, states are never CJP. More seriously, we can’t interpret states as
morphisms in this category. The problem is the non-UR spin factors in CJP. If we remove these, things
are much better.
Definition 6: Let C be a subclass of embedded EJC algebras, closed under ⊙ and containing I. A linear
mapping φ : MA → MB is CJP relative to C iff φA ⊗ idC is Jordan preserving for all C in C . CJPC is the
4 Notice that scalars of this category are real numbers. It is sometimes suggested that quaternionic Hilbert spaces can’t be

accommodated in a symmetric monoidal category owing to the noncommutativity of H, as the scalars in a symmetric monoidal
category must always be commutative. As we are representing quaternionic quantum systems in terms of the associated real
vector spaces of hermitian operators, this issue doesn’t arise here.

<!-- page 8 -->
Some Nearly Quantum Theories

66

category having objects elements of C , mappings relatively CJP mappings.
Example 2: URUE is the class of universally reversible, universally embedded EJC algebras. URSE
is the category of universally reversible, standardly embedded EJC algebras, and RSE is the category
of reversible, standardly embedded EJC algebras. Equipped with relatively CJP mappings, both are
symmetric monoidal categories.
Note that RSE consists of direct sums of real, complex and quaternionic quantum systems. URSE and
URUE contain all real and complex quantum systems, and all quaternionic quantum systems except the
“quabit”, i.e., the quaternionic bit Q2 := M2 (H)sa .
In both of the categories URUE and URSE, states are morphisms. However, Example 1 provides us with
a no-go result for extensions of these categories that preserve the property that states are morphisms. For
URUE, we cannot maintain this property while enlarging the class C to include a spin factor other
than the real, complex, and quaternionic bits, while for URSE, we cannot enlarge it to contain an evendimensional one (it remains open whether we can include the additional odd-dimensional ones).
Not only do URUE and URSE include all states as morphisms, but we are going to see that they inherit
compact closure from the category ∗-ALG of finite-dimensional, complex ∗-algebras and CP maps, in
which they are embedded. It’s worth taking a moment to review this compact structure. If M is a finitedimensional complex ∗-algebra, let Tr denote the canonical trace on M, regarded as acting on itself by
left multiplication (so that Tr(a) = tr(La ), La : M → M being La (b) = ab for all b ∈ M). This induces
an inner product on M, given by ha|biM = Tr(ab∗ )5 . Note that this inner product is self-dualizing, i.e,.
a ∈ M+ iff ha|bi ≥ 0 for all b ∈ M+ . Now let M be the conjugate algebra, writing a for a ∈ M when
regarded as belonging to M (so that ca = c a for scalars c ∈ C and ab = ab for a, b ∈ M). Note that
ha|bi = hb|ai. Now define
fM = ∑ e ⊗ e ∈ M ⊗ M
e∈E

where E is any orthonormal basis for M with respect to h | iM . Then a computation shows that
h(a ⊗ b) fM | fM iM⊗M = ha|biM .
Since the left-hand side defines a positive linear functional on M ⊗ M, so does the right (remembering
here that pure tensors generate M ⊗ M, as we’re working in finite dimensions). Call this functional ηM .
That is,
ηM : M ⊗ M → C is given by ηM (a ⊗ b) = ha|bi = Tr(ab∗ )
and is, up to normalization, a state on M ⊗ M. A further computation now shows that
ha ⊗ b| fM iM⊗M = η (a ⊗ b).
It follows that fM belongs to the positive cone of M ⊗ M, by self-duality of the latter. A final computation
shows that, for any states α and α on M and M, respectively, and any a ∈ M, a ∈ M, we have
(ηM ⊗ α )(a ⊗ fM ) = α (a) and (α ⊗ ηM )( fM ⊗ a) = α (a).
Thus, ηM and fM define a compact structure on ∗-ALG, for which the dual object of M is given by M.
Definition 7: The conjugate of a EJC algebra (A, MA ) is (A, MA ), where A = {a|a ∈ A}. We write ηA
for ηMA and fA for fMA .
5 We are following the convention that complex inner products are conjugate linear in the second argument.

<!-- page 9 -->
H. Barnum, M. A. Graydon & A. Wilce

67

5.1 Universally-embedded, universally reversible EJAs
Now consider the category URUE of universally reversible, universally embedded EJAs A, i.e., pairs
(A, MA ) with A UR and MA = C∗ (A). Let ΦA be the canonical involution on C∗ (A).
Lemma 1: Let (A, MA ) belong to URUE. Then
(a) fA ∈ A ⊙ A;
(b) ηA ◦ (ΦA ⊗ ΦA ) = ηA .
Proof: (a) follows from the fact that ΦA is unitary, so that if E is an orthonormal basis, then so is
{ΦA (e)|e ∈ E}. Since fA is independent of the choice of orthonormal basis, it follows that f is invariant
e Now (b) follows from part (a) of the previous lemma. 
under ΦA ⊗ ΦA , hence, an element of A⊗A.
Define γA : C∗ (A) → C∗ (A) by γ (a) = ΦA (a∗ ). This is a ∗-isomorphism, and intertwines ΦA and ΦA ;
⊗B) → C∗ (A ⊗ B) intertwines ΦA ⊗ ΦB = ΦA e⊗B and ΦA ⊗ ΦB = ΦA e⊗B — whence,
hence, γA ⊗ idB : C∗ (A e
takes A e
⊗B to A e
⊗B. In particular, γA is CJP relative to the class of UR, universally embedded EJCs.
Lemma 2: Let A be a universally embedded UR EJC. Then for all α ∈ CJP(A, I), there exists a ∈ A with
α (b) = hb|ai for all b ∈ A.
Proof: Since α ∈ C∗ (A)∗ , there is certainly some a ∈ C∗ (A) with α = |ai. We need to show that a ∈ A.
Since α is CJP,
γA ⊗ α : C∗ (A) ⊗C∗ (A) = C∗ (A ⊗ A) → C∗ (A)
is Jordan-preserving. In particular, (α ⊗ γA )( fA ) ∈ A. But
(α ⊗ γA )( fA ) =

∑ (α ⊗ γA)(e ⊗ e)

e∈E

=

∑ he|aiΦ(e∗ )

e∈E

= Φ( ∑ he|aie∗ )
e∈E

= Φ(( ∑ ha|eie)∗ ) = Φ(a∗ ) = γA (a).
e∈E

Hence, γA (a) ∈ A, whence, a ∈ A, whence, a ∈ A. (Alternatively: ΦA (a∗ ) ∈ A implies a∗ ∈ A, whence, a
is self-adjoint, whence, a ∈ A.) 
It follows that ηA and fA belong, as morphisms, to URUE. Hence, URUE inherits the compact structure
from ∗-ALG, as promised.
The same holds for URSE. Specifically, we want to show that fA belongs to A ⊙ A whenever A is a
standardly embedded UR EJC.
Suppose that E is an orthonormal basis for MA : then so is {e∗ |e ∈ E}; thus, since fA is independent of
the choice of basis, we have
fA∗ = ∑ e∗ ⊗ e∗ = ∑ e∗ ⊗ e∗ = fA .
e∈E

e∗ ∈E ∗

b is the self-adjoint part of MA ⊗ MA , then fA ∈ A ⊗ A. This covers the case where A = Cn .
Thus, if A ⊙ A
⊗A. This covers A = Rn
We also have, by the results above, that fA ∈ A ⊙ A whenever the latter equals A e
and A = Qn for n > 2.

<!-- page 10 -->
Some Nearly Quantum Theories

68

In fact, we can do a bit better. If M and N are finite-dimensional ∗-algebras and φ : M → N is a linear
mapping, let φ † denote the adjoint of φ with respect to the natural trace inner products on M and N. It
†
is not difficult to show that, for any M in ∗-ALG, fM
= ηM and vice versa; indeed, ∗-ALG is daggercompact.
Definition 8: Let (A, MA ) and (B, MB ) be EJCs. A linear mapping φ : MA → MB is †-CJP iff both φ and
φ † are CJP. If C is a category of EJCs and CJP mappings, we write C † for the category having the same
objects, but with morphisms restricted to †-CJP mappings in C .
If A belongs to URUE or URSE, then fA and ηA are both CJP and, hence, are both †-CJP with respect
to the indicated category. Hence,
Theorem 2: The categories URUE† and URSE† are dagger-compact.

6

Conclusion

We have found two theories — the categories URSE and URUE of universally reversible euclidean
Jordan algebras, standardly and universally embedded — that, in slightly different ways, unify finitedimensional real, complex and (almost all of) quaternionic quantum mechanics. By virtue of being
compact closed, both theories continue to enjoy many of the information-processing properties of standard complex QM, e.g., the existence of conclusive teleportation and entanglement-swapping protocols
[1].
One property of standard QM that some of our composites do not share is the possibility of local tomography: a state ω on A ⊙ B is not generally determined by the joint probability assignment a, b 7→ ω (a⊗ b),
where a and b are effects of A and B, respectively. Another way to put it is that A ⊙ B is generally much
larger than the vector-space tensor product A ⊗ B. As local tomography is well known to separate complex QM from its real and quaternionic variants, this is hardly surprising. Perhaps more surprising is that
some of our composites—those involving quaternionic factors—also exhibit supermultiplicativity of the
maximal number of distinguishable states, and, relatedly, violate another property sometimes assumed
as a basic desideratum for composites: that products of pure states are pure.
Neither theory includes the quabit, Q2 . Example 1 shows that the quabit can’t be added to URUE without
a violation of compact closure. On the other hand, if fQ2 belongs to the canonical composite Q2 ⊙ Q2 ,
then the slightly larger category RSE, which consists of all finite-dimensional real, complex and quaternionic quantum systems, will be compact closed (indeed, dagger compact).6
The categories URSE and URUE contain interesting compact closed subcategories. In particular, real
and quaternionic quantum systems (less the quabit), taken together, form a sub-theory, closed under
composites. We conjecture that this is exactly what one gets by applying the CPM construction to
Baez’s (implicit) category of pairs (H, J), H a finite-dimensional Hilbert space and J an anti-unitary with
J 2 = ±1 — and, again, excluding the quabit. Should RSE prove to be compact closed, we could entertain
the stronger conjecture that this is exactly what one obtains by applying CPM to Baez’s category.
Complex quantum systems also form a monoidal subcategory of URSE, which we might call CQM:
indeed, one that functions as an “ideal”, in that if A ∈ URSE and B ∈ CQM, then A ⊙ B ∈ CQM as well.
This is provocative, as it suggests that a universe initially consisting of many systems of all three types,
6 Since this note was accepted for presentation at QPL XII we have settled this question in the affirmative. The details will
be given in [4].

<!-- page 11 -->
H. Barnum, M. A. Graydon & A. Wilce

69

would eventually evolve into one in which complex systems greatly predominate.
The category URUE is somewhat mysterious. Like URSE, this encompasses real, complex and quaternionic quantum systems, excepting the quabit. In this theory, the composite of complex quantum systems
comes with an extra classical bit — equivalently, a {0, 1}-valued superselection rule. This functions to
make the transpose operation — which is a Jordan automorphism of Mn (C)sa , but an antiautomorphism
of Mn (C) — count as a morphism. The precise physical significance of this is a subject for further study.

Acknowledgements
We thank Cozmin Ududec for valuable discussions. Research at Perimeter Institute is supported by the
Government of Canada through Industry Canada and by the Province of Ontario through the Ministry of
Research & Innovation. MAG was supported by an NSERC Alexander Graham Bell Canada Graduate
Scholarship. AW was supported by a grant from the FQXi foundation.

References
[1] S. Abramsky & B. Coecke (2005): Abstract Physical Traces. Theory and Applications of Categories 14, pp.
111–124. Available at http://arxiv.org/abs/0910.3144.
[2] E. M. Alfsen & F. W. Shultz (2003): Geometry of state spaces of operator algebras.
doi:10.1007/978-1-4612-0019-2.

Birkhäuser,

[3] J. Baez (2012): Division algebras and quantum theory. Foundations of Physics 42, pp. 819–855,
doi:10.1007/s10701-011-9566-z. Available at http://arxiv.org/abs/1101.5690.
[4] H. Barnum, M. A. Graydon & A. Wilce (in preparation): Composites and categories of Euclidean Jordan
algebras.
[5] H. Barnum, M. Müller & C. Ududec (2014): Higher-order interference and single-system postulates characterizing quantum theory. New Journal of Physics 16, p. 123029, doi:10.1088/1367-2630/16/12/123029.
Available at http://arxiv.org/abs/1403.4147.
[6] H. Barnum & A. Wilce (2011): Information processing in convex operational theories. Electronic
Notes in Theoretical Computer Science 270, pp. 3–15, doi:10.1016/j.entcs.2011.01.002. Available at
http://arxiv.org/abs/0908.2352.
[7] H. Barnum & A. Wilce (2014): Local tomography and the Jordan structure of quantum theFoundations of Physics 44, pp. 192–212, doi:10.1007/s10701-014-9777-1.
Available at
ory.
http://arxiv.org/abs/1202.4513v2.
[8] J. Faraut & A. Koranyi (1994): Analysis on Symmetric Cones. Oxford.
[9] H. Hanche-Olsen (1983): On the structure and tensor products of JC-algebras. Can. J. Math. 35, pp. 1059–
1074, doi:10.4153/CJM-1983-059-8.
[10] H. Hanche-Olsen & E. Størmer (1984): Jordan Operator Algebras. Pitman, Boston-London-Melbourne.
Available at http://www.math.ntnu.no/~hanche/joa/.
[11] M. Koecher (1958): Die geodätischen von positivitätsbereichen. Math. Annalen 135, pp. 192–202,
doi:10.1007/BF01351796. See also: M. Koecher (1999): The Minnesota Notes on Jordan Algebras and
Their Applications. Springer.
[12] M. Müller & C. Ududec (2012): The structure of reversible computation determines the self-duality of
quantum theory. Phys. Rev. Lett. 108, p. 130401, doi:10.1103/PhysRevLett.108.130401. Available at
http://arxiv.org/abs/1110.3516.

<!-- page 12 -->
Some Nearly Quantum Theories

70

[13] I. Satake (1980): Algebraic Structures of Symmetric Domains. Publications of the Mathematical Society of
Japan, No. 14, Iwanami Shoten and Princeton University Press.
[14] H. Upmeier (1980): Derivations of Jordan C∗ -algebras. Math. Scand. 46, pp. 251–264.
[15] E. Vinberg (1960): Homogeneous cones. Dokl. Acad. Nauk. SSSR 133, pp. 9–12. English translation:
E. Vinberg (1961): Soviet Math. Dokl. 1, pp. 787-790.
[16] A. Wilce (2012):
Conjugates,
http://arxiv.org/abs/1206.2897.

Filters

and

Quantum

Mechanics.

Available

at

[17] A. Wilce (2012): Four and a half axioms for quantum mechanics.
In Y. Ben-Menahem &
M. Hemmo, editors: Probability in Physics, Springer, doi:10.1007/978-3-642-21329-8 17. Available at
http://arxiv.org/abs/0912.5530.
[18] A. Wilce (2012): Symmetry and self-duality in categories of probabilistic models. In B. Jacobs, P. Selinger
& B. Spitters, editors: Proceedings of QPL 2011, Series 95, pp. 275–279, doi:10.4204/EPTCS.95. Available
at http://arxiv.org/abs/1210.0622.
