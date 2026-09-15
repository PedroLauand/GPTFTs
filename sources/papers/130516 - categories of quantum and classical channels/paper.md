---
type: paper
date: 2013-05-16
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1305.3821v3)
reviewed: false
---

# Categories of Quantum and Classical Channels

Machine-generated and unreviewed text extraction of arXiv:1305.3821v3
(28 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1305.3821v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:1305.3821v3 [quant-ph] 16 Sep 2014

CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS
BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

Abstract. We introduce a construction that turns a category of pure state
spaces and operators into a category of observable algebras and superoperators.
For example, it turns the category of finite-dimensional Hilbert spaces into the
category of finite-dimensional C*-algebras and completely positive maps. In
particular, the new category contains both quantum and classical channels,
providing elegant abstract notions of preparation and measurement. We also
consider nonstandard models, that can be used to investigate which notions
from algebraic quantum information theory are operationally justifiable.

1. Introduction
Algebraic quantum information theory provides a very neat framework in which
to study protocols and algorithms involving both classical and quantum systems.
Instead of stacking structure on top of the base formalism of Hilbert space – to
accommodate, for example, mixed states, their measurement and evolution, and
classical outcomes – these basic notions are equal and first-class citizens in the
algebraic approach.
The basic setup is that individual systems are modeled by C*-algebras, which
can be grouped by tensor products, and can evolve along completely positive maps,
also called channels. Classical systems correspond to commutative algebras. This
uniformises many notions. For example, a density matrix corresponds simply to a
channel from the trivial classical system C to a quantum system, and a positive
operator valued measurement is just a channel from a quantum system to a classical
one. One ends up with a category of classical and quantum systems and channels
between them. Advanced protocols can then be modeled by combining channels in
sequence as well as in parallel. For more information we refer to [22, 23].
This paper abstracts that idea away from Hilbert spaces, in an attempt to obtain
a more operational formalism. The Hilbert space formalism is blessed with such
an excess of structure, that many conceptually different notions coincide in this
model [29]. Instead, we will take only the very basic notion of compositionality as
primitive.
To be precise, we will be working within the programme of categorical quantum
mechanics [1, 8]. This programme starts with so-called dagger compact categories,
that assume merely a way of grouping systems together that allows for entanglement, and a way of composing operations on those systems. A surprising amount
Date: September 17, 2014.
1991 Mathematics Subject Classification. 81P45, 16B50, 18D35, 46L89, 46N50, 81P16.
Key words and phrases. Abstract C*-algebras, categorical quantum mechanics, completely
positive maps, quantum channel.
This research was supported by the Engineering and Physical Sciences Research Council Fellowship EP/L002388/1, and the John Templeton Foundation.
1

<!-- page 2 -->
2

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

of theory already follows from these primitives, including scalars, the Born rule,
quantum teleportation, and much more.
The categories initially studied mostly accommodated pure states. However,
there is a beautiful construction that works on arbitrary dagger compact categories,
and turns the category containing pure quantum states and operations into the
category of mixed states and completely positive maps [32, 10]. The resulting
categories can even be axiomatised [7, 15, 10]. Thus mixed states, and channels
between quantum systems, can be studied without leaving the theory of dagger
compact categories.
Another line of research within categorical quantum mechanics concerns incorporating classical systems. These can be modeled in terms of the tensor structure
alone, by promoting the no-cloning theorem into an axiom: the ability to copy
and delete becomes an extra feature of classical systems over quantum ones. This
leads to so-called commutative Frobenius algebras within a category [13, 14, 12, 2].
Again, it is pleasantly surprising how much follows: for example, this formalism
encompasses complementary observables, and measurement-based quantum computing [9].
This paper combines these two developments in representing quantum channels and classical systems, respectively. We show that (possibly noncommutative) Frobenius algebras in the category of Hilbert spaces correspond to finitedimensional C*-algebras precisely when they are normalisable (see also [38]). This
justifies regarding such algebras in arbitrary categories as abstract C*-algebras 1.
Then, we present a construction that turns a category (of pure states spaces) into
one of channels, in such a way that the category of Hilbert spaces becomes the
category of finite-dimensional C*-algebras and channels. We study the cases of
“completely quantum” and “completely classical” abstract C*-algebras, showing
that this so-called CP*–construction neatly combines quantum channels and classical systems.
Finally, we exemplify our constructions in nonstandard models. This provides
counterexamples that separate conceptually different notions, even some that are
commonly held to coincide. Our results thus form the starting point for an investigation of the foundations of quantum mechanics from an operational point of view.
For example, one can show that commutativity of an algebra of observables need
not imply distributivity of its accompanying quantum logic [11]. The nonstandard
model of sets and relations is a satisfying example of our abstract theory, which
there becomes a theory about the well-studied notion of a groupoid (see also [18]).
This opens possibilities to employ “quantum reasoning” to obtain group theoretic
results, and vice versa.
Before giving a brief introduction to dagger compact categories, we end this introduction by reviewing related work. There have been earlier attempts to combine
classical systems with quantum channels [33]. One attempt introduces biproducts
to model classical information. This has the drawback that classical and quantum
1By an abstract C*-algebra we mean an object in a monoidal category satisfying certain re-

quirements. By a concrete one we mean an object satisfying those requirements in the category
of (finite-dimensional) Hilbert spaces. This is not to be confused with terminology from functional analysis. There, a concrete C*-algebra is a *-subalgebra of the algebra B(H) of bounded
operators on a Hilbert space H that is uniformly closed, whereas an abstract C*-algebra is any
Banach algebra with an involution satisfying ka∗ ak = kak2 ; these notions are equivalent by the
Gelfand-Naimark-Segal construction; see e.g. [16, Theorem I.9.12].

<!-- page 3 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

3

information no longer stand on equal footing, and that adding more primitives than
merely compositionality requires operational justification. Another attempt relies
on splitting idempotents. This is a clean categorical construction that does not need
external ingredients, but it is not so clear that this does not capture too much. Our
CP*–construction mediates between these two earlier attempts, as made precise
in [19]: it needs no external structure, and it captures the right amount of objects.
A separate development adds classical data to a quantum category via a categorical construction involving the commutative Frobenius algebras in the category [12].
The notion of “classical morphism” from that work inspired the formulation of the
CP*–construction, by generalising from commutative algebras to non-commutative.
Finally, categorical quantum mechanics links to topological quantum computing [26]. The dagger compact categories of the former form a more basic setting
than the modular tensor categories of the latter. Specifically, this article deals
with symmetric monoidal categories rather than the more general braided ones.
Nevertheless, as the diagrammatic notation of dagger compact categories exemplifies [34], even before going into topological quantum computing, there already is
topology in quantum computing. Furthermore, the CP*–construction goes through
in a braided setting, for details we refer to the forthcoming book [20]. This article
will avoid those complications and stick to the symmetric setting.
1.1. Dagger compact categories and graphical language. It is often useful
to reason in a very general sense about processes and how they compose. Category
theory provides the tool to do this. A category consists of a collection of objects
A, B, C, . . ., a collection morphisms f, g, · · · , an associative operation ◦ for (vertical)
composition, and for every object A an identity morphism 1A . Objects can be
thought of as types. They dictate which morphisms can be composed together. We
shall primarily be interested in categories that have not only a vertical composition
operation, but a horizontal composition as well.
Definition 1.1. A monoidal category consists of a category V, an object I ∈ V
called the monoidal unit, a bifunctor ⊗ : V × V → V called the monoidal product,
and natural isomorphisms αA,B,C : A ⊗ (B ⊗ C) → (A ⊗ B) ⊗ C, λA : I ⊗ A → A,
and ρA : A ⊗ I → A, such that λI = ρI and the following diagrams commute:
A ⊗ (B ⊗ (C ⊗ D))

α

(A ⊗ B) ⊗ (C ⊗ D)

α

A⊗α

((A ⊗ B) ⊗ C) ⊗ D
α⊗D

α

A ⊗ ((B ⊗ C) ⊗ D)
A ⊗ (I ⊗ B)

α

(A ⊗ (B ⊗ C)) ⊗ D
(A ⊗ I) ⊗ B
ρ⊗B

A⊗λ

A⊗B
Our main example is the category FHilb, whose objects are finite-dimensional
complex Hilbert spaces, and whose morphisms are linear functions. It becomes

<!-- page 4 -->
4

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

a monoidal category under the usual tensor product of Hilbert spaces, with unit
object C.
We often drop α, λ, and ρ when they are clear from the context. Monoidal
categories where all three of these maps are actually equalities, rather than natural
isomorphisms, are called strict. In any monoidal category, they can be used to
construct a natural isomorphism from some object to any other bracketing of that
object, with or without monoidal units. For example:
(A ⊗ I) ⊗ (B ⊗ (I ⊗ C)) ∼
= (A ⊗ (B ⊗ (C ⊗ I))).
Mac Lane’s coherence theorem proves that the equations in Definition 1.1 suffice to
show that any such natural isomorphism is equal to any other one [25]. This lets
us treat monoidal categories as if they were strict. That is, we may omit brackets,
α, λ, and ρ without ambiguity, simply assuming they are included where necessary.
Instead of the usual algebraic notation for morphisms in monoidal categories, it is
often vastly more convenient to use a graphical notation (see also [34]). Morphisms
can be thought of as processes. A morphism takes something of type A and produces
something of type B. We draw morphisms as:
B

D

f

g

,

, ...
C

A

Identity morphisms are special “do nothing” processes, which take something of
type A and return the thing itself. We represent objects, and the identity morphisms
on them, as empty wires:
A

B

,

,

C

, ...

Morphisms are composed by connecting an output wire into an input wire:
C

◦

g

g

B

C

=

f

B

B

A

f
A

This notation neatly incorporates the assumption that composition is associative,
and that composition with an identity has no effect.
The monoidal product of two morphisms is expressed as juxtaposition:
B′

B

⊗

f
A

=

g
A′

B′

B

g

f
A

A′

<!-- page 5 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

5

The monoidal product is also associative and unital, but possibly only up to isomorphism. The (identity on) the monoidal unit object I is denoted by the empty
picture.
Definition 1.2. A symmetric monoidal category is a monoidal category with an
−1
additional natural isomorphism σA,B : A ⊗ B → B ⊗ A, such that σA,B
= σB,A ,
ρA = λA ◦ σA,I , and the following “hexagon” diagram commutes:
(B ⊗ A) ⊗ C

α

B ⊗ (A ⊗ C)

σ⊗C

B⊗σ

(A ⊗ B) ⊗ C

B ⊗ (C ⊗ A)
α

α

A ⊗ (B ⊗ C)

σ

(B ⊗ C) ⊗ A

We draw symmetry maps as wire crossings:

This graphical notation unambiguously represents morphisms in symmetric monoidal
categories [21]. Moreover, this representation is sound and complete with respect to
the algebraic definition of a symmetric monoidal category. Our example monoidal
category FHilb becomes symmetric by letting σH,K (h ⊗ k) := k ⊗ h, for all H and
K.
Definition 1.3. A compact category is a symmetric monoidal category in which
every object A comes with a dual object A∗ and morphisms ηA : I → A∗ ⊗ A and
εA : A ⊗ A∗ → I satisfying:
A∗

A

ηA ⊗ A∗

A∗ ⊗ A ⊗ A∗

1A

A ⊗ ηA

A∗ ⊗ ε

1A

A ⊗ A∗ ⊗ A

εA ⊗ A

A∗

A

In the graphical notation, the object A∗ is represented as a wire labelled A, but
directed downward instead of upward:
A :=

A

A∗ :=

We represent ηA as a cup, and εA as a cap:
εA :=

ηA :=

A

<!-- page 6 -->
6

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

The diagrams from the previous definition are called the “snake equations” because
of their graphical representations:

A

=

A

A

=

A

In a compact category, any map f : A → B can also be considered as a map
f ∗ : A∗ → B ∗ by using caps and cups to “bend the wires” around:
A

f∗
B

A

:=

f
B

Our example category FHilb is compact closed. For a finite-dimensional Hilbert
space H, let H ∗ be the dual Hilbert space. Any orthonormal basis
P ei for H then
induces a basis ei for H ∗ . Define εH (ei ⊗ ej ) = δij and ηH (1) = i ei ⊗ ej . These
maps satisfy the snake equations and do not depend on the choice of basis ei .
Computing f ∗ : B ∗ → A∗ in terms of ε and η yields the (operator) transpose of f ,
i.e. f ∗ (ξ) = ξ ◦ f . This is not to be confused with the matrix transpose, which is
basis-dependent (as it depends on fixing a particular isomorphism A∗ ∼
= A).
Finally, we abstract the notion of conjugate-transpose.
Definition 1.4. A dagger on a category V is a contravariant functor † : Vop → V
satisfying A† = A for all objects A, and f †† = f for all morphisms f . A unitary in
a dagger category is a map u : A → B with u ◦ u† = 1B and u† ◦ u = 1A .
In particular, †-categories are always isomorphic with their opposite category.
As the notation suggests, the † functor is an abstract version of the conjugatetranspose of a complex linear map. Thus, for linear maps, the abstract notion of
unitary is precisely the usual one.
Definition 1.5. A dagger compact category is a compact category that comes with
a dagger such that (f ⊗ g)† = f † ⊗ g † , the structure maps αA , λA , and σA,B are all
unitary, and ε†A = ηA∗ .
The role of conjugation in a dagger compact category is played by the lower-star
operation: f∗ : A∗ → B ∗ , which is defined as:
f∗ := (f † )∗ = (f ∗ )†
Our example category FHilb is dagger compact via the formula for adjoints:
hf (h) | ki = hh | f † (k)i.
Finally, we will need the following notion of structure-preserving functor between
dagger compact categories.
Definition 1.6. A functor F : C → D between dagger symmetric monoidal categories is a dagger symmetric monoidal functor when F ◦ † = † ◦ F and it comes
with an isomorphism ψ : I → F (I) and a natural isomorphism ϕA,B : F A ⊗ F B →
F (A ⊗ B) making the following diagrams commute:

<!-- page 7 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

(F A ⊗ F B) ⊗ F C

ϕ ⊗ FC

ϕ

F (A ⊗ B) ⊗ F C

F ((A ⊗ B) ⊗ C)

α

F (α)

F A ⊗ (F B ⊗ F C)
FA ⊗ I

ρ

FA ⊗ ϕ

ϕ

ϕ

F A ⊗ F (B ⊗ C)

I ⊗ FA

FA
F (ρ−1 )

FA ⊗ ψ

FA ⊗ FI

7

λ

FI ⊗ FA
σF A,F B

ϕA,B

F (A ⊗ B)

FA
F (λ−1 )

ψ ⊗ FA

F (A ⊗ I)
FA ⊗ FB

F (A ⊗ (B ⊗ C))

ϕ

F (I ⊗ A)

FB ⊗ FA
ϕB,A

F σA,B

F (B ⊗ A)

Preserving the dagger and the monoidal structure suffices to preserve the compact structure [17].
2. Abstract C*-algebras
This section defines so-called normalisable dagger Frobenius algebras. The running example investigates these structures in the category of finite-dimensional
Hilbert spaces. As will turn out, they are precisely finite-dimensional C*-algebras.
Therefore, we will think of normalisable dagger Frobenius algebras in arbitrary
dagger compact categories as abstract C*-algebras.
Definition 2.1. A dagger Frobenius algebra is an object A in a dagger monoidal
: A ⊗ A → A and : I → A, called multicategory together with morphisms
plication and unit, satisfying the following diagrammatic equations:
=

=

=

=

=

These identities are called associativity, unitality, and the Frobenius law. The
†

†
maps
and ( ) ,
(comultiplication) and and
(counit) are defined as
respectively. They automatically satisfy coassociativity and counitality, which are
the upside-down versions of associativity and unitality.
Example 2.2. An important example is the set A = Mn of n-by-n matrices with
complex entries. This set is clearly an algebra: defining
as (a, b) 7→ ab and
: C → A by 1 7→ 1A satisfies associativity and unitality. The algebra A becomes
a Hilbert space under the Hilbert–Schmidt inner product ha | bi = Tr(a† b). It has
a canonical orthonormal basis {eij | i, j = 1, . . . , n}, where eij is the matrix all of
whose entries vanish except for a one at location (i, j). We can now compute
(eij ) = h (eij ) | 1i = heij |

(1)i = heij | 1A i = Tr(eji ) = δij ,

<!-- page 8 -->
8

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

so that
h
whence

: a 7→ Tr(a) by linearity. Similarly,
(eij ) | ekl ⊗ epq i = heij |
(ekl ⊗ epq )i = heij | δlp ekq i = δik δjq δlp ,
P
(eij ) = l eil ⊗ elj . With these explicit expressions it is easy to see
X
◦
(eij ⊗ ekl ) =
(δjk eil ) = δjk
eip ⊗ epl
p

X
=
(

⊗ )(eij ⊗ ekp ⊗ epl )

p

X
⊗ )(
eij ⊗ ekp ⊗ epl )

=(

p

⊗ )◦( ⊗

=(
Similarly,
◦

(eij ⊗ ekl ) = ( ⊗
,

Linearity now shows that (A,

)◦(

)(eij ⊗ ekl ).
⊗ )(eij ⊗ ekl ).

) is a dagger Frobenius algebra in FHilb.

Any dagger Frobenius algebra defines a cap and a cup satisfying the snake identities.
(1)

:=

=

:=

=

This cup and cap provide an alternative form of the Frobenius law that is sometimes
more convenient:
=

=

=

or, equivalently

Definition 2.3. A dagger Frobenius algebra (A,
satisfies the following equation:

,

=

) is symmetric when it

=
The dagger Frobenius algebra Mn in FHilb is symmetric by the cyclic property
of the trace: Tr(ba) = Tr(ab).
Proposition 2.4. For any symmetric Frobenius algebra:
=
Proof. Symmetry can be used to interchange traces with Frobenius caps and cups.
=

=

=

=

=


A dagger Frobenius algebra is certainly symmetric when it is commutative, i.e.
when it satisfies the following equation:
=

<!-- page 9 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

9

Being commutative is strictly stronger than being symmetric. For example, in
FHilb, the algebra Mn is commutative precisely when n = 1. Nevertheless, there
are plenty of commutative dagger Frobenius algebras in FHilb. For example, consider the subalgebra A of Mn consisting of matrices that are diagonal in some fixed
orthogonal basis. It turns out that this is the only example: commutative dagger
, ) in FHilb are in one-to-one correspondence with orFrobenius algebras (A,
thogonal bases of A; see [14]. Orthonormal bases correspond to so-called normal
algebras.2 This abstract characterisation of orthonormal bases is what first sparked
the interest in Frobenius algebras in categorical quantum mechanics [13].
We will combine symmetric and commutative algebras as follows. If A and B are
dagger Frobenius algebras in FHilb, then so is their direct sum A ⊕ B. If A and B
are symmetric or commutative, then so is A ⊕ B. However, not many interesting,
non-commutative algebras in FHilb are normal, so we need to find a condition to
take the place of normality. Investigating matrix algebras Mn , we might think it
suffices to consider algebras that are normal up to a scaling factor 1/n. However,
“scaled normality”, unlike normality, is not preserved by direct sum. For example,
if A = Mm and B = Mn the induced Frobenius algebra on of A ⊕ B is only normal
up to a scalar when n = m.
For this reason we will consider a more general condition, called normalisability.
Before defining this concept, we introduce the notion of a central map.
Definition 2.5. A map z : A → A is central for a multiplication

on A when:

z
z

=

=

z

The terminology derives from the usual notion of centre for e.g. a group, ring,
algebra, etc. Left (or right) multiplication
◦ (a ⊗ −) : A → A with an element
a : I → A is a central map precisely when a is in the centre Z(A) = {a ∈ A | ∀b ∈
A : ab = ba}. Furthermore, all central maps of a Frobenius algebra arise this way.
A map g : A → A in a dagger category is called positive when g = h† ◦ h for some
h. It is called positive definite if it is a positive isomorphism. Using these conditions,
we can define normalisability as a well-behavedness property of the “loop”.
Definition 2.6. A dagger Frobenius algebra (A,
, ) is normalisable when it
comes with a central, positive definite z : A → A such that
z

=

z

The map z is called the normaliser, and we will often depict it simply as
algebra is normal when we may take z = 1.

. The

The equation above uniquely fixes the map z 2 , so normalisers are unique in any
category where positive square roots are unique, when they exist (such as FHilb).
2There is a closely related notion called specialness. A dagger Frobenius algebra is normal
if and only if it is special and symmetric. In FHilb, normal and special coincide for dagger
Frobenius algebras.

<!-- page 10 -->
10

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

All normal Frobenius algebras are symmetric. This turns out the be the case for
dagger normalisable Frobenius algebras as well.
Proposition 2.7. Normalisable dagger Frobenius algebras are symmetric.
Proof. Expand the counit.
(∗)

=

=

=

=

=

=

=

Note that the step marked (∗) is just a diagram deformation: the two multiplication
maps have traded places. This corresponds to cyclicity of the trace.

The dagger Frobenius algebra Mn in FHilb is normalised by z(a) = n−1/2 a:

z2
eij

=

1
n

=
eij

1 P
k
n

=

eik

ekj

eij

The point of normalisability is that the algebra Mm ⊕ Mn is also normalisable (but
no longer special unless
m = n), by the central map z(a, b) = (m−1/2 a, n−1/2 b).
L
Thus direct sums
k Mnk of matrix algebras are normalisable dagger Frobenius
algebras in FHilb. But these are precisely the finite-dimensional C*-algebras! This
is a standard fact, see e.g. [16, Theorem III.1.1]. Recall that a finite-dimensional
C*-algebra is a finite-dimensional algebra A equipped with an involution satisfying
ka∗ ak = kak2 (for some norm satisfying kabk ≤ kakkbk that is then unique). The
following theorem shows that this exhausts all examples of normalisable dagger
Frobenius algebras in FHilb. Thus we may think of normalisable dagger Frobenius
algebras in arbitrary categories as abstract C*-algebras (see also [39]).
We can show this directly by defining the C*-algebra structure in terms of the
Frobenius algebra structure. First note that any Frobenius algebra fixes an isomorphism A∗ ∼
= A as follows:
:=

:=

These two maps are inverse because of snake identies from equation (1).
Theorem 2.8. If (A,
, , ) is a normalisable dagger Frobenius algebra in
FHilb, then the following involution gives it the structure of a finite-dimensional
C*-algebra:

⋆
:=
v

v∗

Conversely, up to isomorphism, all finite-dimensional C*-algebras arise in this way.
Proof. Any dagger Frobenius algebra in FHilb is a C*-algebra under the involution
above, and all finite-dimensional C*-algebras arise in this way [38], so it suffices to
, ) in FHilb is normalisable.
prove that any dagger Frobenius algebra (A,

<!-- page 11 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

11

L
Since it is unitarily isomorphic to a C*-algebra of the form
k Mnk , there is an
(k)
orthonormal basis {eij : 0 ≤ i, j < nk } for A, in terms of which
is defined as
(k)

(k′ )

(k)

) directly:
eij ⊗ ei′ j ′ 7→ δkk′ δji′ eij ′ . Use this to compute TrA (


 ′ †
X
(k′ )
(k)
(k)
(k )
TrA (
eij ⊗ ei′ j ′
)(eij ) =
ei′ j ′
i′ j ′ k′

=

X  (k′ ) †
(k)
ei′ j ′ δkk′ δji′ eij ′

i′ j ′ k′

=

X  (k) † (k)
ejj ′ eij ′

=

X

j′

δij = nk δij .

j′

Also

(k)

(k)

−1/2 (k)
eij defines a normaliser: it is positive

(eij ) = δij . Therefore eij 7→ nk

and invertible, satisfies TrA (
) ◦ ( )2 =
summand of A and so is central.

, and acts by a constant scalar on each


For future reference, we prove two lemmas about abstract C*-algebras, including
an alternative form of the normalisability condition. As a matter of convention, we
define the following shorthands:
:=

:=

We can use any such shorthand without ambiguity by stating that we always preserve the (cylic) ordering of inputs/outputs. That is, the left input of
will
will always
always be clockwise from the right input, and the right output of

∗
be clockwise from the left output. This rule also applies to depictions of
∗

and
:
:=

:=

=

Lemma 2.9. Any symmetric dagger Frobenius algebra satisfies

.

Proof. Apply the Frobenius law and associativity.
=

=

=

=

=

=

The middle equation uses symmetry.
Lemma 2.10. Any normalisable dagger Frobenius algebra satisfies


=

.

<!-- page 12 -->
12

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

Proof. Use centrality of the normaliser, associativity, and unitality.
(∗)

=

=

=

=

=

=

The marked equation follows from Proposition 2.4.

=



To end this section where it started, reconsider the algebra Mn in FHilb. It is
isomorphic to (Cn )∗ ⊗ Cn by eij 7→ hi| ⊗ |ji, where {|0i, . . . , |ni} is any orthonormal
basis of Cn . As it turns out, this way of constructing C*-algebras works in the
abstract, as long as the category is not too ill-behaved. To be precise, we call an
object X in a dagger compact category positive-dimensional if there is a positive
definite z : I → I satisfying
z

X

=

z

X

X

A dagger compact closed category is called positive-dimensional if all its objects
are. All the categories we will consider are positive-dimensional.
Proposition 2.11. In a positive-dimensional dagger compact category, every object
of the form H ∗ ⊗ H carries a canonical normalisable dagger Frobenius algebra with
the following multiplication and unit:

Proof. It follows immediately from compactness that this is a dagger Frobenius
algebra. Positive-dimensionality provides a positive definite scalar z that satisfies
(z 2 ◦ TrX (1X )) ⊗ 1X = 1X . Then:
z

=

z

=

z
z

Hence 1H ∗ ⊗H ⊗ z is a normaliser.



The abstract C*-algebra of the previous proposition is called an abstract matrix
algebra, and is also denoted by B(H).
3. Abstract completely positive maps
Having abstracted C*-algebras from FHilb to arbitrary categories, this section
does the same for completely positive maps. This will lead to a fully abstract
procedure, called the CP*–construction, that turns any dagger compact category
(like FHilb) into the category of abstract C*-algebras and abstract completely
positive maps.
First recall the definition of completely positive maps between C*-algebras. An
element a of a C*-algebra A is positive when it is of the form a = b⋆ b for some

<!-- page 13 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

13

b ∈ A. A linear function f : A → B between C*-algebras is positive when it takes
positive elements to positive elements. It is completely positive when the function
f ⊗ 1 : A ⊗ Mn → B ⊗ Mn is positive for every natural number n. Completely
positive maps form a large and well-studied class of transformations that send
(possibly unnormalised) states of open systems to (possibly unnormalised) states,
and hence account for dynamics [4, 27, 37]. There is some debate about whether
other maps are in fact unphysical [3, 28, 35, 40].
This definition translates to abstract C*-algebras as follows: an element a : I →
, ) is positive when a =
(b⋆ ⊗ b) for some
A of an abstract C*-algebra (A,
b : I → A. Expanding definitions, we see that a : I → A is positive when

b⋆

a

=

=

=

b∗

b

b

b∗

b

c∗

c

for some b : I → A. By Lemma 2.10, this implies:
=

=

=

a

b∗

b

b∗

b

for some object X and c : I → X ⊗ A; the middle equation follows from Lemma 2.9.
In fact, for Hilbert spaces, the following two characterisations of positive elements
a are equivalent:
=

∃b.
a

=

∃c.
b∗

a

b

c∗

c

However, in other categories, the implication from left to right is strict. For this
reason, we will take the weaker notion to define an abstract positive element.
This abstract description of positive elements generalises to maps f : A → B
between abstract C*-algebras (A,
, ) and (B,
, ) as follows: there are an
object X and a map g : A → X ⊗ B satisfying

(2)

f

=

g∗

g

The positive elements of A are then precisely the maps I → A satisfying this
condition. Equation (2) is called the CP*–condition. Proposition 3.4 below shows
that this is precisely the right condition to capture complete positivity abstractly.
But before that, the following lemma records that it indeed makes sense to take
tensor products of abstract C*-algebras.
Lemma 3.1. If (A,

,

,

) and (B,

,

,

) are normalisable dagger Frobe-

nius algebras in a dagger compact category, then so is (A ⊗ B,

,

,

).

<!-- page 14 -->
14

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

Proof. All the required properties – associativity, unitality, the Frobenius law, and
normalisability – follow easily from the graphical calculus for dagger compact categories.

Incidentally, Lemmas 2.9 and 2.10 provide an alternative form of the CP*–
condition that is sometimes more convenient: equation (2) holds if and only if

(3)

f

=

h∗

h

for some object X and morphism h : A → X ⊗ B.
Proposition 3.4 below shows that if a map A → B satisfies the CP*–condition (2),
then its composition with another map I → A satisfying that condition still satisfies
that condition. It is in fact easier to first prove the more general result that the CP*–
condition is closed under composition, i.e. that maps satisfying (2) form a category.
In fact, the rest of this section shows that if V is a dagger compact category, then
so is the category of abstract C*-algebras in V and maps satisfying (2), that we
now officially define.
Definition 3.2. Given a dagger compact category V, we define the data for a
new category CP∗ [V]. Objects are normalizable dagger Frobenius algebras in V.
Morphisms (A,
) → (B,
) are morphisms f : A → B in V satisfying the
CP*–condition (2).
The next theorem shows that CP∗ [V] is a well-defined category inheriting composition and identities from V. In fact, it also inherits tensor products from V by
Lemma 3.1, and then becomes a dagger compact category.
Theorem 3.3. If V is a dagger compact category, CP∗ [V] is again a well-defined
dagger compact category.
Proof. Identity maps 1A : (A,
) → (A,
) satisfy the CP∗ -condition by Lemma 2.9,
where the role of g in equation (2) is played by
.
) → (B,
) and g : (B,
) → (C,
) satisfy the
Next, suppose f : (A,
CP*–condition. It then follows from Lemma 2.10 that their composition does, too.

g

i∗

i∗

i

i

g

=

=

=

f
f

h∗

h

h∗

h

<!-- page 15 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

15

Thus CP∗ [V] is indeed a well-defined category.
Lemma 3.1 gives monoidal structure on the level of objects. Given a morphism
f : (A,
) → (C, ∗ ) with Kraus map h, and g : (B,
) → (D, ∗ ) with Kraus
) → (C ⊗ D,

map i, then f ⊗ g : (A ⊗ B,

∗

∗

∗ ∗

) satisfies the CP*–condition:

∗
∗

f

g

=

g

f

=
i∗

h∗

i

h

Note that (I, ρI ), where ρI : I ⊗ I → I is the coherence isomorphism of V, is
a normalisable dagger Frobenius algebra by the coherence theorem. Using this
definition of ⊗ and I, the coherence isomorphisms α, λ, and ρ from V trivially
satisfy the CP*–condition. Thus CP∗ [V] is a monoidal category.
To show that CP∗ [V] inherits symmetry, it suffices to show that the swap map
σA,B : A ⊗ B → B ⊗ A of V lifts to a morphism σA,B : (A ⊗ B,
) → (B ⊗

A,

) in CP∗ [V]. This can be done with two applications of Lemma 2.9.

=

=

=

h∗

h

Thus CP∗ [V] is a symmetric monoidal category.
) → (B,
The category CP∗ [V] also inherits the dagger from V. If f : (A,

†
†
†
satisfies (2), then so too does f : because
◦f ◦
=
◦f ◦
,

f†

=

g∗

g†

=

g∗

g†

h∗

)

.

h

Since the coherence isomorphisms of CP∗ [V] are those of V, they are unitary, and
thus CP∗ [V] is a dagger symmetric monoidal category.
Finally, for compactness, let (A,
) be an object in CP∗ [V]. Let A∗ be a dual
∗
of A, with cap εA∗ : A ⊗ A → I. If a Frobenius algebra is dagger normalisable,
so too are the opposite algebra and the transposed algebra (i.e. the dual). Thus

<!-- page 16 -->
16

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

) is a well-defined object of CP∗ [V]. Now, εA∗ : (A,
(A∗ ,
satisfies the CP*–condition, again by Lemma 2.9:

=

=

) ⊗ (A∗ ,

)→I

=

We have already showed that the dagger of a map satisfying the CP*–condition
also satisfies the CP*–condition, so finally let ηA = ε†A∗ . We complete the proof by
noting that σ, η, and ε are all defined with the same underlying maps as in V, so
the symmetry and snake equations are automatically satisfied.

We have constructed a category whose objects are abstract C*-algebras, and
we claim that the morphisms are abstract completely positive maps. The following
proposition justifies that claim, by showing that maps satisfying the CP*–condition
correspond exactly to maps that are completely positive in the usual sense, in that
f : A → B applied to a positive (open) state preserves positivity.
) and (B,
) be normalisable dagger Frobenius alProposition 3.4. Let (A,
gebras and f : A → B a morphism in a dagger compact category. The following are
equivalent:
(a) f satisfies the CP*–condition (2);
(b) f ⊗ 1C sends positive elements of (A,
(B,

) ⊗ (C,

) ⊗ (C,

) to positive elements of

) for all normalisable dagger Frobenius algebras (C,
) ⊗ (X ∗ ⊗ X,

(c) f ⊗ 1X ∗ ⊗X sends positive elements of (A,
) ⊗ (X ∗ ⊗ X,

elements of (B,

);

) to positive

) for all objects X.

Proof. For (a) ⇒ (b): if ρ is a positive element of (A,

)⊗ (C,

), then it can be

∗

regarded as a morphism ρ : I → (A,
)⊗(C,
) in CP [V]. It then follows from
Theorem 3.3 that (f ⊗ 1C ) ◦ ρ is also a morphism in CP∗ [V], so it must also be a
positive element. The implication (b) ⇒ (c) is trivial. Finally, for (c) ⇒ (a): setting
) := (A,
)⊗(X ∗ ⊗X,
).
X = A∗ , the following is a positive element of (B,
=
ρ

Indeed, graphical rewriting using the Frobenius law and symmetry shows:
B

B
=
ρ

=

<!-- page 17 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

17

So, by assumption, (f ⊗ 1A∗ ) ◦ ρ is also a positive element. Applying white caps to
both sides establishes that f satisfies the CP*–condition.

f

=

g∗

This finishes the proof.

g

⇒

f

=

g∗

g



The previous proposition is a fully abstract version of Stinespring’s dilation theorem [36], or rather (because our abstract C*-algebras are finite-dimensional) of
Choi’s theorem [6]. The morphism g in equation (2) therefore called a Kraus map
for f ; we emphasise that it is not unique. Traditional formulations in FHilb allow
a sum of Kraus maps; this is expressed abstractly by the indexing object X in (2).
) and (X ∗ ⊗X,
) in the previous proposition
The abstract C*-algebras (C,
are called the ancillary system, or ancilla. In these terms, the previous proposition
shows that the CP*–condition (2) characterises those maps that preserve positivity
even when their input and output systems are regarded as open subsystems of
larger systems. In fact, the previous proposition does slightly better than Choi’s
theorem, because the ancilla can be an arbitrary abstract C*-algebra instead of just
an abstract matrix algebra.
Because of the way we have modeled the definition of CP∗ [V] after the case of
FHilb, the category CP∗ [FHilb] is indeed that of (concrete) finite-dimensional
C*-algebras and completely positive maps, as the following proposition records.
Proposition 3.5. CP∗ [FHilb] is equivalent to the category of finite-dimensional
C*-algebras and completely positive maps.
Proof. Define a functor E from CP∗ [FHilb] to the category of finite-dimensional
C*-algebras and completely positive maps, acting on objects as in Theorem 2.8
and as the identity on morphisms. This functor is then essentially surjective on
objects by that theorem. Furthermore, Proposition 3.4 shows that E(f ) is a completely positive map between concrete C*-algebras if and only if f satisfies the
CP*–condition. This makes E a well-defined functor that is full. It is faithful by
construction, and hence it is an equivalence of categories.

Remark 3.6. We have employed complex Hilbert spaces. It is natural to wonder
about performing the CP*–construction on real finite-dimensional Hilbert spaces.
On the level of objects, Theorem 2.8 still goes through: abstract C*-algebras in
the category of real finite-dimensional Hilbert spaces correspond to so-called finitedimensional real C*-algebras (see [24]). However, these need not be direct sums of
complex matrix algebras; rather, they are direct sums of algebras of matrices over
the real numbers, complex numbers, or over the quaternions [24, Theorem 5.7.1].
On the level of morphisms, Proposition 3.4 still holds. However, in the real case
these morphisms do not give all completely positive maps [31, Theorem 4.3]. The
underlying issue is that there are more positive elements in real C*-algebras than
those of the form a∗ a.

<!-- page 18 -->
18

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

In the concrete case, *-homomorphisms between C*-algebras are automatically
completely positive. We conclude this section by proving this holds fully abstractly,
providing an easy way to show that some maps are morphisms in CP∗ [V].
Definition 3.7. If (A,
) and (B,
) are dagger normalisable Frobenius algebras, a morphism f : A → B is called a *-homomorphism when it satisfies the
following equations.

f

f

f

=

f

=

f∗

Lemma 3.8. Let (A,
) and (B,
) be dagger normalisable Frobenius algebras
in a dagger compact category V. If f : A → B is a *-homomorphism, then it is a
well-defined morphism in CP∗ [V].
Proof. Graphical manipulation shows the following.

f

=

f

=

=
f

=

f

f
f∗

f∗

f

◦
. Both morphisms
Hence this morphism is a composition of f ∗ ⊗ f and
are completely positive, i.e. of the form of the right-hand side of equation (2): the
former by construction, the latter by Lemma 2.9. Therefore f is also completely
positive by Theorem 3.3, and hence a morphism in CP∗ [V].

4. Completely classical systems and completely quantum systems
) in FHilb
As discussed in Section 2, commutative abstract C*-algebras (A,
correspond to orthogonal bases of A. More precisely, the basis vectors are the
copyable points, i.e. morphisms p : I → A that satisfy
◦ p = p ⊗ p. Expanding
arbitrary vectors in this basis, one can show that the normalised positive elements
of A are precisely those vectors with positive coefficients summing to 1. Thus,
normalised positive elements of a commutative abstract C*-algebra may be regarded
as probability distributions over its copyable points. That is, we may think of
commutative abstract C*-algebras as “completely classical” systems.3
On the other hand, Section 2 showed that abstract matrix algebras can be
regarded as “completely quantum” systems: their states have no probabilistical
mixing aspect at all. In general, abstract C*-algebras are combinations of “completely classical” and “completely quantum” parts. This section focuses on these
two extreme cases. It proves that the CP*–construction subsumes earlier constructions that remained separate: the Stoch–construction into its “completely classical” part [12], and the so-called CPM–construction into its “completely quantum”
3Commutativity might be too strong a notion of “completely classical” system in the abstract.
A weaker notion of broadcastability, that coincides with commutativity in FHilb, seems more
reasonable. Subsequent work will investigate such more operational notions of classicality.

<!-- page 19 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

19

part [32, 10, 5]. Thus the CP*–construction combines the two, and places classical
and quantum systems and channels on an equal footing in a single category.
4.1. Completely classical systems. First, recall the Stoch–construction [12].
Like the CP*–construction of the previous section, it turns a dagger compact category V into a new one, Stoch[V]. It will turn out that it is precisely the full
subcategory of CP∗ [V] consisting of commutative abstract C*-algebras, and that
we may regard it as the subcategory of classical channels.
Objects of Stoch[V] are commutative normalisable dagger Frobenius algebras.
Morphisms (A,
) → (B,
) in Stoch[V] are morphisms f : A → B in V with
(4)

=

f

g∗

g

for some commutative normalisable dagger Frobenius algebra (X,
) and a morphism g : A → X ⊗ B in V. Here, the conjugation g∗ is taken with respect to the
,
, and
.
caps and cups induced by
Theorem 4.1. For a dagger compact category V, the category Stoch[V] is isomorphic to the full subcategory of CP∗ [V] consisting of all commutative normalisable
dagger Frobenius algebras.
Proof. We show that (4) implies (2).

f

=

f

=

g∗

g

=

g

g

=

g∗

The converse holds since the dualisers , , and , are always invertible.

g



The following corollary justifies thinking of Stoch[V] as a category of classical
) → (B,
) in CP∗ [V] normalised if
channels. We call a morphism f : (A,
it preserves counits:
◦ f = . Recall that a stochastic map between finitedimensional Hilbert spaces is a matrix with positive real entries whose every column
sums to one.
Corollary 4.2. Normalised morphisms in Stoch[FHilb] correspond to stochastic
maps between finite-dimensional Hilbert spaces.
Proof. Combine Theorem 4.1, Proposition 3.5 and [22, 3.2.3 and 2.1.3].



4.2. Completely quantum systems. First, we recall the CPM–construction [32,
10]. Like the CP*–construction of the previous section, it turns a dagger compact
category V into a new one, CPM[V]. It will turn out that it is precisely the
full subcategory of CP∗ [V] consisting of abstract matrix algebras B(H) = (H ∗ ⊗
), that are simply identified with H, and that we may regard it as the
H,
subcategory of quantum channels.

<!-- page 20 -->
20

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

Objects of CPM[V] are the same as those of V, and morphisms f : A → B in
CPM[V] are morphisms f : A∗ ⊗ A → B ∗ ⊗ B in V for which there exist an object
X and a morphism g : A → X ⊗ B satisfying:
=

f

g∗

g

Composition, identity maps, and ⊗ on objects of CPM[V] are as in V. The tensor
product is defined on morphisms of CPM[V] as follows:
D∗

A∗

A

B∗

C∗

C

D

C

=

g

⊗

f

D∗

C∗

D

g

f

B
B∗

A∗

A

B

CPM[V] inherits symmetry and compact structure from V, only “doubled”.
A∗ B ∗

B

A
A∗

σA,B :=

A A∗

A

ηA :=

εA :=
A

B∗

A∗

A

A∗ A

A∗

B

The following theorem proves that CPM[V] embeds in CP∗ [V], preserving all
structure. To formulate that embedding, recall that a functor F is dagger symmetric
monoidal if it comes with natural unitary isomorphisms ϕA,B : F (A⊗ B) → F (A)⊗
F (B) satisfying ϕI,A = ϕA,I = 1A and
F (A ⊗ B ⊗ C)
ϕA⊗B,C

ϕA,B⊗B

F (A) ⊗ F (B ⊗ C)

F (A ⊗ B)

1F (A) ⊗ ϕB,C

F (σA,B )

F (A ⊗ B) ⊗ F (C)
F (A) ⊗ F (B) ⊗ F (C)
ϕA,B ⊗ 1F (C)

F (B ⊗ A)

ϕA,B

F (A) ⊗ F (B)

σF (A),F (B)
σB,A

F (B) ⊗ F (A)

For simplicity, we have assumed that the categories involved are strict monoidal.
Theorem 4.3. If V is a positive-dimensional dagger compact category,
B(A) = (A∗ ⊗ A,

)

B(f ) = f

defines a functor B : CPM[V] → CP∗ [V] that is full, faithful, and dagger symmetric monoidal.
Proof. First of all, B is well-defined, because a morphism f : A∗ ⊗ A → B ∗ ⊗ B in
V determines a morphism A → B in CPM[V] precisely when if it determines a
) → (B ∗ ⊗ B,
) in CP∗ [V]. Indeed, if f is a morphism
morphism (A∗ ⊗ A,
in CPM[V], it also satisfies the CP*–condition:

<!-- page 21 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

=

f

g∗

g

=

g∗

21

g

Conversely, if f is in CP∗ [V], then it is also in CPM[V]:

=

f

g∗

g

=

g∗

g

Composition is defined identically in CPM[V] and CP∗ [V], so B is functorial,
full, and faithful.
Define ϕA,B : B(A ⊗ B) → B(A) ⊗ B(B) as the following “reshuffling map”.
A∗

B∗

A

B

B∗

A∗

A

B

A∗

A

B∗

B

ϕ†A,B :=

ϕA,B :=
B∗

A∗

A

B

To verify that this defines a morphism in CP∗ [V], it suffices to show that it is a
*-homomorphism by Lemma 3.8.

ϕ

=
ϕ

ϕ

=
ϕ

ϕ†

⇔

=

⇔

=

Next, we show naturality of ϕ:

<!-- page 22 -->
22

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

ϕB,A
B(f ) ⊗ B(g)

g

f

=
g

f

B(f ⊗ g)

ϕA,B

The last thing that remains to be shown is coherence for ϕ with respect to the
symmetric monoidal structure. For associativity:
B∗ B

A∗ A

B∗ B

A∗ A

C∗ C

C∗ C

ϕA,B ⊗ 1B(C)

1B(A) ⊗ ϕB,C
B ∗ A∗

A B

=

C∗ C

A∗ A

C ∗B ∗

B C

ϕA⊗B,C

ϕA,B⊗C
C ∗ B ∗ A∗

A B

C ∗ B ∗ A∗

A

I A∗ A

A∗ A

C

B C

As for the unit equations:
A∗ A

I

I

I

=
I A∗ A

=

I

A∗ I

I

A∗

A

B∗

A∗ A

A

Finally, as for symmetry:
B∗

B

B

A∗

A

σB(A),B(B)

ϕB,A
A∗

A

B∗

B

=

A∗

B∗

B

A

ϕA,B

B(σA,B )
B∗

A∗

A

B

B∗

A∗

A

B

Thus B is a full, faithful, dagger symmetric monoidal functor.



As a consequence of the previous theorem and Proposition 3.5, the category
CPM[FHilb] is equivalent to the category of matrix algebras and completely positive maps. This justifies thinking of the “completely quantum” part of CP∗ [V] as
a category of quantum channels.
The category CPM[FHilb] is strictly smaller than the category CP∗ [FHilb] of
all finite-dimensional C*-algebras and completely positive maps. That is, the embedding B of the previous theorem does not extend to an equivalence of categories:
for example, the finite-dimensional C*-algebra A = M1 ⊕ M2 cannot be isomorphic
to a matrix algebra Mn because dim(A) = 12 + 22 = 5 6= n2 = dim(Mn ).
In analogy to the case V = FHilb, it stands to reason to regard objects H of V
as systems whose state space consists of pure states, and objects B(H) of CP∗ [V]
as systems whose state space consists of mixed states. So one might think that the
“pure” category V should embed into the “mixed” category CP∗ [V]. The following
corollary shows that this is indeed the case.

<!-- page 23 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

23

Corollary 4.4. If V is a dagger compact category,
A 7→ B(A)

f 7→ f∗ ⊗ f

defines a dagger symmetric monoidal functor V → CP∗ [V].
Proof. Combine the previous theorem with [32, Theorem 4.20].



There are no meaningful functors in the opposite directions. A construction
CP∗ [V] → V would model decoherence, which cannot be a structure preserving
functor. More precisely, the functor V → CP∗ [V] does not have any adjoints,
because it does not preserve (co)limits: B(H ⊕ K) 6∼
= B(H) ⊕ B(K) for nontrivial
Hilbert spaces H and K. Similarly, a functor CP∗ [V] → CPM[V] would need to
coherently turn an (abstract) C*-algebra into an (abstract) matrix algebra. Again,
it cannot be an adjoint because it cannot preserve (co)limits.
5. Nonstandard models
So far, we have abstracted classical and quantum systems and channels from
the category FHilb to arbitrary dagger compact categories V. Now it is high
time to see some other examples. This section considers three: the category of
sets and relations, the category of matrices with positive entries, and the category
of relations with values in a cancellative quantale. We will see that abstract C*algebras in these categories turn out to be important well-known structures, that
are nevertheless quite different from concrete C*-algebras.
5.1. Relations. First, recall the category Rel. Its objects are sets, and morphisms
A → B are relations R ⊆ A × B. The composition of R : A → B and S : B → C is
given by
S ◦ R = {(a, c) ∈ A × C | ∃b ∈ B : (a, b) ∈ R, (b, c) ∈ S},
and {(a, a) | a ∈ A} is the identity on A. Cartesian product makes Rel into a
compact category. Finally, it becomes a dagger compact category by
R† = {(b, a) | (a, b) ∈ R}.
We start by investigating the objects of CP∗ [Rel]. This immediately shows
that these nonstandard abstract C*-algebras are quite different from C*-algebras
(in FHilb): they are precisely groupoids. Recall that a groupoid is a category
whose morphisms are all invertible [25].
Proposition 5.1. Normalisable dagger Frobenius algebras in Rel are (in one-toone correspondence with) groupoids.
Proof. By [18, Theorem 7], it suffices to show that normalisability implies speciality
in Rel. Let (A,
, , ) be a normalisable dagger Frobenius algebra in Rel.
is an isomorphism. In Rel, this means
= {(a, z(a)) |
Then the normaliser
is also positive, and hence self-adjoint.
a ∈ A} for a bijection z : A → A. But
Since all isomorphisms in Rel are unitary, z equals its own inverse. Therefore
◦ = 1A , that is, (A,
) is special.


<!-- page 24 -->
24

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

Explicitly, the set A = Mor(G) of morphisms of a groupoid G becomes an
abstract C*-algebra in Rel under
= {((g, f ), g ◦ f ) | f and g are composable morphisms in G},
= {(∗, 1a) | a is an object of G}.

The proof of the previous proposition illustrates that we may take
that normalisers of dagger Frobenius algebras are not unique.
Next, we determine the morphisms of CP∗ [Rel].

= 1A , but

Definition 5.2. A relation R ⊆ Mor(G) × Mor(H) between groupoids G and H
repects inverses when (g, h) ∈ R implies (g −1 , h−1 ) ∈ R and (1dom(g) , 1dom(h) ) ∈ R.

Proposition 5.3. The category CP∗ [Rel] is isomorphic to the category of groupoids
and relations respecting inverses.
Proof. Unfolding definitions shows that a morphism R ⊆ (A × A) × (B × B) in Rel
is completely positive, i.e. is of the form of the right-hand side of equation (2),
precisely when
(∗)

((a, a′ ), (b, b′ ) ∈ R =⇒ ((a′ , a), (b′ , b) ∈ R, ((a, a), (b, b)) ∈ R.

If G and H are groupoids, corresponding to Frobenius algebras (G,
(H,

) and

), and R ⊆ G × H, then
= {((g, g ′ ), g −1 ◦ g ′ ) ∈ G3 | g −1 and g ′ are composable},
◦R◦

= {((g, g ′ ), (h, h′ )) ∈ G2 × H 2 | g −1 and g ′ are composable},

h−1 and h′ are composable},

(g −1 ◦ g ′ , h−1 ◦ h′ ) ∈ R}.

Substituting this into (∗) translates precisely into R respecting inverses.



∗

Next we investigate “completely quantum” objects in CP [Rel]. Recall that
a category is indiscrete when there is precisely one morphism between each two
objects. Indiscrete categories are automatically groupoids.
Proposition 5.4. The objects in CP∗ [Rel] that are isomorphic to B(A) for some
set A are (in one-to-one correspondence with) indiscrete groupoids.
Proof. By definition, B(A) corresponds to a groupoid whose set of morphisms is
A × A, and whose composition is given by

(b2 , a1 )
if b1 = a2 ,
(b2 , b1 ) ◦ (a2 , a1 ) =
undefined otherwise.
We deduce that the identity morphisms of B(A) are the pairs (a2 , a1 ) with a2 = a1 .
So objects of B(A) just correspond to elements of A. Similarly, we find that the
morphism (a2 , a1 ) has domain a1 and codomain a2 . Hence (a2 , a1 ) is the unique
morphism a1 → a2 in B(A).


In other words, the essential image of the embedding B : CPM[Rel] → CP∗ [Rel]
is the full subcategory of CP∗ [Rel] consisting of indiscrete groupoids.
There are many more connections between the theory of groupoids and abstract
C*-algebras. For example, projections in an abstract C*-algebra in Rel are precisely
the connected components of its corresponding groupoid [11, Lemma 22].

<!-- page 25 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

25

5.2. Positive matrices. To conclude this section, we consider categories that are
in some sense between the categories FHilb and Rel; the former can be thought of
as involving matrices over the complex numbers, whereas the latter can be thought
of as involving matrices over the two element set. We will consider matrices ranging
over other domains.
We start with the category Mat(R≥0 ). Its objects are natural numbers, and a
morphism m → n is an m-by-n matrix whose entries are nonnegative real numbers,
i.e. elements of [0, ∞). Composition is matrix multiplication, and identity matrices
give identity morphisms. Tensor product acts as multiplication on objects, and as
Kronecker product on morphisms.
We will determine the objects of CP∗ [Mat(R≥0 )] by reducing to CP∗ [FHilb].
There is an obvious dagger symmetric monoidal functor Mat(R≥0 ) → FHilb,
sending n to Cn with its canonical basis. Hence a normalisable dagger Frobenius
algebra (n,
, , ) in Mat(R≥0 ) also defines a C*-algebra structure on Cn .
Recall that
L any finite-dimensional C*-algebra A can be written in standard form
as A ∼
= k Mnk .
Definition 5.5. Write En = {eij | i, j = 1, . . . , n} for the standard basis of Mn . By
the matrix of a linear map f : Mm → Mn , we mean
the function F : Em × En → C

given by the entries F (eij , eL
kl ) = hekl | fLeij i = Tr(elk f (eij )). This definition
extends to linear maps f :
l Mnl between finite-dimensional C*k Mmk →
algebras in standard form. We say that f is really positive when its matrix F
has entries in R≥0 . If f is completely positive and really positive, we call it really
completely positive.
Proposition 5.6. The category CP∗ [Mat(R≥0 )] is isomorphic to the category
of finite-dimensional C*-algebras in standard form and really completely positive
maps.
Proof. The fact that the functor Mat(R≥0 ) → FHilb is dagger symmetric monoidal
and faithful implies that the induced functor CP∗ [Mat(R≥0 )] → CP∗ [FHilb] is
also dagger symmetric monoidal and faithful. It is full by construction, and injective on objects. Hence it suffices to show that it is surjective on objects. First,
observe that the structure maps
, , and
of the C*-algebra Mn are really
3
completely positive. The matrices M : En → R≥0 for multiplication, U : En → R≥0
for the unit, and Z : En2 → R≥0 then take the form
M (eij , ekl , epq ) = δjk δip δlq ,
U (eij ) = δii ,
√
N (eij ) = 1/ n.
Hence Mn is in the image of the functor CP∗ [Mat(R≥0 )] → CP∗ [FHilb]. Because
CP∗ [Mat(R≥0 )] has biproducts, C*-algebras in standard form are reached, too. 
Finally, let us consider matrices with entries ranging over other sets of positive
numbers, such as the unit interval [0, 1]. To be precise, we will consider the category
Mat(Q), where Q is a cancellative commutative quantale. Recall that a quantale
is a partial order (Q, ≤) that has suprema of arbitrary subsets, together with a
commutative multiplication (Q, ·, 1) satisfying
_
_
x · ( yi ) =
x · yi .
i

i

<!-- page 26 -->
26

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

W
It is cancellative when x · y = x · z implies y = z or x = 0, where 0 = ∅. For more
information we refer to [30]. The extended nonnegative real numbers [0, ∞] form
an example under the usual ordering and multiplication, as does the unit interval
[0, 1]. Another example is the Boolean algebra {0, 1} under the usual ordering and
multiplication.
The category Mat(Q) has sets as objects, morphisms A → B are Q-valued
matrices, i.e. functions A × B → Q. Composition of R : A → B and S : B → C is
_
S ◦ R(a, c) =
R(a, b) · S(b, c).
b

Cartesian product and matrix transpose makes this into a dagger compact category,
very much like Rel. In fact, notice that Mat({0, 1}) = Rel.4
Lemma 5.7. Any normalisable dagger Frobenius algebra in Mat(Q) induces a
groupoid.
Proof. Let (A,
, , ) be a normalisable dagger Frobenius algebra in Mat(Q).
Notice that there is a (unique) homomorphism f : Q → {0, 1} of quantales such
that f (x) = 0 if and only if x = 0, namely

0 if x = 0,
f (x) =
1 otherwise.
It induces a dagger symmetric monoidal functor f ∗ : Mat(Q) → Rel; see also [2,
Section 5.2]. Therefore G := A becomes a dagger Frobenius algebra in Rel with
multiplication f ∗ (

) and unit f ∗ ( ). Moreover, f ∗ ( ) = f ∗ (

) ◦ f ∗ ( )2 by

normalisability. But, as in the proof of Proposition 5.1, f ∗ ( ) is a positive isomorphism in Rel, and so f ∗ ( )2 = 1G . At this point Lemma 2.10 guarantees that
(G, f ∗ ( ), f ∗ ( ), 1G ) is a normalisable dagger Frobenius algebra in Rel, which
corresponds to a groupoid by Proposition 5.1.

The previous lemma shows that if we “collapse” the matrix M : G3 → Q of multiplication to M : G3 → {0, 1}, it becomes the multiplication table of a groupoid.
Similarly, the matrix U : G → Q becomes the set of identities of that groupoid.
The only freedom left is what nonzero elements of Q to place in the nonzero entries of these matrices. It is easy to obtain several constraints on these values [2,
Section 5.2]. However, in general, CP∗ [Mat(Q)] does not seem to correspond to
a familiar category such as CP∗ [Rel]. We refrain from explicating it further, but
note that it does provide a nonstandard model that lends itself to easy calculation,
for example to find counterexamples.
References
[1] Abramsky, S., Coecke, B.: Categorical quantum mechanics, pp. 261–324. Elsevier (2008)
[2] Abramsky, S., Heunen, C.: H*-algebras and nonunital frobenius algebras: first steps in
infinite-dimensional categorical quantum mechanics. Clifford Lectures, AMS Proceedings of
Symposia in Applied Mathematics 71, 1–24 (2012)
[3] Alicki, R.: Comment on ‘reduced dynamics need not be completely positive’. Physical Review
Letters 75, 3020 (1995)
[4] Bhatia, R.: Positive definite matrices. Princeton University Press (2007)
4Notice also that R

≥0 is not a quantale under its usual ordering.

<!-- page 27 -->
CATEGORIES OF QUANTUM AND CLASSICAL CHANNELS

27

[5] Boixo, S., Heunen, C.: Entangled and sequential quantum protocols with dephasing. Physical
Review Letters 108, 120,402 (2012)
[6] Choi, M.D.: Completely positive linear maps on complex matrices. Linear Algebra and Its
Applications 10(3), 285–290 (1975)
[7] Coecke, B.: Axiomatic description of mixed states from Selinger’s CPM–construction. Electronic Notes in Theoretical Computer Science 210, 3–13 (2008)
[8] Coecke, B. (ed.): New Structures for Physics. No. 813 in Lecture Notes in Physics. Springer
(2009)
[9] Coecke, B., Duncan, R.: Interacting quantum observables: categorical algebra and diagrammatics. New Journal of Physics 13, 043,016 (2011)
[10] Coecke, B., Heunen, C.: Pictures of complete positivity in arbitrary dimension. In: Electronic
Proceedings in Theoretical Computer Science, vol. 95, pp. 27–35 (2012)
[11] Coecke, B., Heunen, C., Kissinger, A.: Compositional quantum logic. In: B. Coecke, L. Ong,
P. Panangaden (eds.) Computation, Logic, Games, and Quantum Foundations, no. 7860 in
Lectures Notes in Computer Science, pp. 21–36. Springer (2013)
[12] Coecke, B., Paquette, É.O., Pavlović, D.: Classical and quantum structuralism. In: S. Gay,
I. Mackey (eds.) Semantic Techniques in Quantum Computation, pp. 29–69. Cambridge University Press (2010)
[13] Coecke, B., Pavlović, D.: Quantum measurements without sums. In: Mathematics of Quantum Computing and Technology. Taylor and Francis (2007)
[14] Coecke, B., Pavlović, D., Vicary, J.: A new description of orthogonal bases. Mathematical
Structures in Computer Science 23(3), 555–567 (2012)
[15] Coecke, B., Perdrix, S.: Environment and classical channels in categorical quantum mechanics. In: Computer Science Logic, pp. 230–244. Springer (2010)
[16] Davidson, K.R.: C*-algebras by example. American Mathematical Society (1991)
[17] Duncan, R.: Types for quantum computing. Ph.D. thesis, Oxford University (2006)
[18] Heunen, C., Contreras, I., Cattaneo, A.S.: Relative frobenius algebras are groupoids. Journal
of Pure and Applied Algebra 217, 114–124 (2013)
[19] Heunen, C., Kissinger, A., Selinger, P.: Completely positive projections and biproducts.
arxiv:1308.4557, to appear in the proceedings of Quantum Physics and Logic X (2013)
[20] Heunen, C., Vicary, J.: Introduction to Categorical Quantum Mechanics. Oxford University
Press (to appear)
[21] Joyal, A., Street, R.: Braided tensor categories. Advances in Mathematics 102, 20–78 (1993)
[22] Keyl, M.: Fundamentals of quantum information theory. Physical Reports 369, 431–548
(2002)
[23] Keyl, M., Werner, R.F.: Channels and maps. In: D. Bruß, G. Leuchs (eds.) Lectures on
Quantum Information, pp. 73–86. Wiley (2007)
[24] Li, B.: Real operator algebras. World Scientific (2003)
[25] Mac Lane, S.: Categories for the Working Mathematician, 2nd edn. Springer (1971)
[26] Panangaden, P., Paquette, É.O.: New structures for physics. In: Coecke [8], pp. 939–979
[27] Paulsen, V.: Completely bounded maps and operators algebras. Cambridge University Press
(2002)
[28] Pechukas, P.: Reduced dynamics need not be completely positive. Physical Review Letters
74, 1060–1062 (1994)
[29] Redei, M.: Why John von Neumann did not like the Hilbert space formalism of quantum
mechanics (and what he liked instead). Studies in the History and Philosophy of Modern
Physics 27, 493–510 (1996)
[30] Rosenthal, K.I.: Quantales and their applicatoins. Pitman Research Notes in Mathematics.
Longman Scientific & Technical (1990)
[31] Ruan, Z.J.: On real operator spaces. Acta Mathematica Sinica 19(3), 485–496 (2003)
[32] Selinger, P.: Dagger compact closed categories and completely positive maps. In: Quantum
Programming Languages, Electronic Notices in Theoretical Computer Science, vol. 170, pp.
139–163. Elsevier (2007)
[33] Selinger, P.: Idempotents in dagger categories. In: Quantum Programming Languages, Electronic Notes in Theoretical Computer Science, vol. 210, pp. 107–122. Elsevier (2008)
[34] Selinger, P.: A survey of graphical languages for monoidal categories. In: Coecke [8], pp.
289–356

<!-- page 28 -->
28

BOB COECKE, CHRIS HEUNEN, AND ALEKS KISSINGER

[35] Shaji, A., Sudarshan, E.C.G.: Who’s afraid of not completely positive maps? Physics Letter
A 341(1–4), 48–54 (2005)
[36] Stinespring, W.F.: Positive functions on C*-algebras. Proceedings of the American Mathematical Society 6(2), 211–216 (1955)
[37] Størmer, E.: Positive linear maps of operator algebras. Springer (2013)
[38] Vicary, J.: Categorical formulation of finite-dimensional quantum algebras. Communications
in Mathematical Physics 304(3), 765–796 (2011)
[39] Zakrzewski, S.: Quantum and classical pseudogroups I. Communications in Mathematical
Physics 134, 347–370 (1990)
[40] Życzkowski, K., Bengtsson, I.: On duality between quantum states and quantum maps. Open
Systems & Information Dynamics 11, 3–42 (2004)
Department of Computer Science, University of Oxford
E-mail address: {coecke,heunen,alek}@cs.ox.ac.uk
