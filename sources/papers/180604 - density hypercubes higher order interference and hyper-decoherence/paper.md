---
type: paper
date: 2018-06-04
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1806.00915v1)
reviewed: false
---

# Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

Machine-generated and unreviewed text extraction of arXiv:1806.00915v1
(16 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1806.00915v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Density Hypercubes, Higher Order Interference
and Hyper-Decoherence: a Categorical Approach

arXiv:1806.00915v1 [quant-ph] 4 Jun 2018

Stefano Gogioso
University of Oxford
stefano.gogioso@cs.ox.ac.uk

Carlo Maria Scandolo
University of Oxford
carlomaria.scandolo@cs.ox.ac.uk

In this work, we use the recently introduced double-dilation construction by Zwart and Coecke to
construct a new categorical probabilistic theory of density hypercubes. By considering multi-slit
experiments, we show that the theory displays higher-order interference of order up to fourth. We also
show that the theory possesses hyperdecoherence maps, which can be used to recover quantum theory
in the Karoubi envelope.

1

Introduction

Quantum interference is often considered to be one of the fundamental features of quantum theory,
responsible for quantum advantage in a number of computational tasks. However, there is a known limit
to how much interference quantum theory can exhibit. Sorkin proposed a hierarchy of theories based on
the maximum order of interference they exhibit [25, 26], which is quantified by the maximum number of
slits on which a theory shows an irreducible interference behaviour. Interference in quantum theory is
limited to the second order: the interference pattern of two slits cannot be reduced to the pattern of single
slits, but the interference pattern of three slits can be reduced to the pattern arising from pairs of slits and
single slits. This limitation has been recently confirmed in various experiments [13, 14, 22, 23, 24].
A natural question arises: Why is interference in Nature limited to the second order? Does the presence
of higher-order interference create any paradoxical consequences in Nature that conflict with some of
the principles we believe to be fundamental? Recent work has shown that higher-order interference—
i.e. interference of order higher than the second—is forbidden [1] in physical theories which admit a
fundamental level of description where everything is pure and reversible [4, 5]. Further work has ruled out
higher-order interference based on thermodynamic considerations [4, 15].
Other literature has instead focused on the analysis of specific feature that theories with higher-order
interference would possess, e.g. whether they would provide any advantage in certain computational
tasks [16, 17, 18, 20]. It was also shown that theories having second-order interference and lacking
interference of higher orders are relatively close to quantum theory [2, 21, 27, 28].
Unfortunately, one of the major shortcomings in the study of higher-order interference is the scarcity
of concrete models displaying such post-quantum features, so that it has so far been very hard to look for
specific examples of paradoxical or counter-intuitive consequences. Two models—density cubes [10]
and quartic quantum theory [30]—have been proposed in the past, but are not fully defined operational
theories, e.g. because they do not deal with composite systems [18]. This limitation precludes them from
being used to study all possible consequences of higher order interference, including potential violation of
Tsirelson bound.
In this article, we provide the first complete construction of a full-fledged operational theory exhibiting
interference up to the fourth order. Our construction is inspired by the double-dilation construction
of [29] and it is carried out in within the framework of categorical probabilistic theories [12]. The
Submitted to:
----

c S. Gogioso & C. M. Scandolo
This work is licensed under the Creative Commons
Attribution-Noncommercial-Share Alike License.

<!-- page 2 -->
2

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

resulting theory of ‘density hypercubes’ has composite systems, exhibits higher-order interference and
possesses hyper-decoherence maps [18, 19, 30]. Quantum theory, with its second-order interference, is an
extension of classical theory: the latter can be recovered by decoherence, which eliminates the secondorder interference effects. Similarly, the theory of density hypercubes, with its third- and fourth-order
interference, is an extension of quantum theory: the latter can now be recovered by hyper-decoherence,
which eliminates third- and fourth-order interference effects.
The paper is organized as follows. In Section 2, we define the categorical probabilistic theory of
density hypercubes using the double-dilation construction. In Section 3, we define hyper-decoherence
maps, and show that quantum theory is recovered in the Karoubi envelope. In Section 4, we show that
density hypercubes display interference of third- and fourth-order, but not of fifth-order and above. In
Section 5, finally, we discuss open questions and future lines of research. Proofs of all results can be
found in the Appendix.

2

The Theory of Density Hypercubes

2.1

Construction of the theory

In this section, we define the categorical probabilistic theory of density hypercubes, using a recently
introduced construction known as double dilation [29]. The construction is done in two steps: first we
define the category DD(fHilb), containing hyper-quantum systems and processes between them, and only
in a second moment we introduce quantum and classical systems, using (hyper-)decoherence and working
in the Karoubi envelope Split(DD(fHilb)).
The double-dilation category DD(fHilb) is defined to be a symmetric monoidal subcategory of
CPM(fHilb) with objects—the density hypercubes—in the form DD(H) := H ⊗ H , where H is a finitedimensional Hilbert space and H := H ∗ ⊗ H is the corresponding doubled system in the CPM category.
Even though DD(fHilb) is symmetric monoidal and has its own graphical calculus, in this work we will
always use the graphical calculi of CPM(fHilb) and fHilb to talk about density hypercubes. When working
in CPM(fHilb), we will use solid black lines for morphisms and calligraphic letters (e.g. H ) for objects.
When working in fHilb, we will use solid grey lines for morphisms and plain letters (e.g. H) for objects.
The morphisms DD(H) → DD(K) in DD(fHilb) are the CP maps H ⊗ H → K ⊗ K taking the
following form for a doubled CP map F, some auxiliary systems E , G and some special commutative
†-Frobenius algebra (henceforth known as a classical structure) on G in fHilb:
H

E
F̄
G

K

(1)
H

G
F
E

K

In the diagram above, F is a doubled CP map H → G ⊗ K ⊗ E in CPM(fHilb)—i.e. one in the form
F = f ∗ ⊗ f for some f : H → G ⊗ K ⊗ E in fHilb—and we have used F̄ to denote the CP map obtained
by inverting the tensor product ordering of inputs and outputs of f (for purely aesthetic reasons). We will
always use upper-case letters (e.g. F) to denote doubled CP maps in CPM(fHilb), lower-case letters to
denote the corresponding linear maps in fHilb, and we will always write discarding maps explicitly.

<!-- page 3 -->
S. Gogioso & C. M. Scandolo

3

Composition in DD(fHilb) is the same as composition of CP maps, while tensor product is only
slightly adjusted to take into account the doubled format of our new morphisms:
Ḡ

F̄

F̄

Ḡ
N

(2)

=

F

F

G

G

Just as was the case for CP maps, maps of density hypercubes can all be obtained as composition of a
“doubled” map and one or two “discarding” maps:
E

H

F̄
G

E

K

G

(3)
G

H

F

|

{z

E

G

K

E

}

doubled map

|

{z

}

discarding maps

We refer to the discarding map obtained by doubling E as the “forest” and to the discarding map obtained
from the classical structure as the “bridge”. The scalars of DD(fHilb) are exactly the scalars R+ of
CPM(fHilb), and hence the theory of density hypercubes is probabilistic. It is furthermore convex, because
the following “tree-on-a-bridge” effects can be used to add-up maps of density hypercubes—analogously
to the way ordinary discarding maps H can be used to add-up CP maps in CPM(fHilb)—by expanding
them in terms of the orthonormal bases |ψx ix∈X associated [8] with the classical structures :
H

H

=
H

2.2

=

∑

x∈X

H

H

Ψ†x

H

Ψ†x

(4)

Component symmetries

States in the theory DD(fHilb) take the form of fourth order tensors, an observation which prompted the
choice of “density hypercubes” as a name for the theory. If (|ψx i)x∈X is a choice of orthonormal basis for
some finite-dimensional Hilbert space H, the states on DD(H) = H ⊗ H in DD(fHilb) can be expanded
as follows in fHilb:

Φ

ψxT01 ψx∗01

K∗

φ∗

ψxT10 ψx∗10

K∗

φ

ψx†11 ψx11

K

φ

ψx†00 ψx00

K

K

=
K

(5)

∑

x00 ,x01 ,x10 ,x11 ∈X

Φ

φ∗

<!-- page 4 -->
4

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

Recall that density matrices possess a Z2 symmetry given by self-adjointness. This symmetry can be
understood in terms of the following action τ : Z2 → Aut(C) of Z2 on the complex numbers:
τ(1) := z 7→ z∗

τ(0) := z 7→ z

(6)

The components of a density matrix ρ then satisfy the following equation, for every a ∈ Z2 (trivial for
a = 0, self-adjoint for a = 1):
τ(a)(ρ x0 x1 ) = ρx(0⊕a) x(1⊕a)
(7)
Instead of a Z2 symmetry, density hypercubes possess a Z2 × Z2 symmetry. This symmetry can be
understood in terms of the following action τ : Z2 × Z2 → Aut(C) of Z2 × Z2 on the complex numbers:
τ(0, 1) := z 7→ z∗
τ(1, 1) := z 7→ z

τ(0, 0) := z 7→ z
τ(1, 0) := z 7→ z∗

(8)

The components of a density hypercube ρ satisfy the following equation for every (a, b) ∈ Z2 × Z2 , where
by ⊕ we have denoted addition in Z2 :
τ(a, b)(ρ x(0,0) x(0,1) x(1,0) x(1,1) ) = ρ x(0⊕a,0⊕b) x(0⊕a,1⊕b) x(1⊕a,0⊕b) x(1⊕a,1⊕b)

(9)

We see that the components are related by a trivial symmetry for a = (0, 0), by a self-adjoining symmetry
for a = (1, 0) and a = (0, 1), and by a self-transposing symmetry in for a = (1, 1). An alternative way to
look at this symmetry is observe that states of density hypercubes can all be expressed as certain sums of
doubled states in the following form:
Φ

K

Φ

K

(10)

For these states, we have the usual self-conjugating Z2 symmetry of density matrices Φ ⊗ Φ 7→ Φ∗ ⊗ Φ∗
as well as an independent self-transposing Z2 symmetry Φ ⊗ Φ 7→ Φ ⊗ Φ, which taken together give the
same Z2 × Z2 symmetry described above in terms of components.
In order to visualise the Z2 × Z2 symmetry action, we divide the components ρx00 x01 x10 x11 of a ddimensional density hypercube ρ into 15 classes, depending on which indices x00 , x01 , x10 , x11 have
same/distinct values chosen from the set {1, ..., d}. We arrange the indices on a square: index 00 is on the
top left corner, 10 acts as reflection about the vertical mid-line, 01 acts as reflection about the horizontal
mid-line and 11 acts as 180o rotation about the centre. We use colours as names for index values in
{1, ..., d}, with distinct colours denoting distinct values.

| {z } |

4 distinct

{z

3 distinct

} |

{z

2 distinct

} | {z }

all equal

(11)
For example, the component ρ0321 of a 4+ -dimensional system will fall into the 1st class from the
left above, the component ρ0122 will fall into the 2nd class, the component ρ0003 into the 8th class, the
component ρ0011 into the 12th class and the component ρ0000 into the 15th class.
Then we look at the individual orbits of components in each class under the symmetry. Classes
with components having orbits of order 4 are shown below: each orbit contributes a single independent
complex value to the tensor, i.e. two independent real values, and each component class is annotated by
the total number of independent real values contributed in dimension d. Just as we did above, we are using

<!-- page 5 -->
S. Gogioso & C. M. Scandolo

5

colours to denote values in {1, ..., d}: the geometric action of Z2 × Z2 on the coloured vertices/edges of
the squares exactly mirrors the algebraic action of Z2 × Z2 on the components in the different classes.
↔

10

↔

10

↔

10

↔

10

↔

l 01 &
.
%11 l 01

l 01 &
.
%11 l 01

l 01 &
.
%11 l 01

l 01 &
.
%11 l 01

l 01 &
.
%11 l 01

10

10

10

10

↔
{z

|

↔
{z

}

2 41 d(d−1)(d−2)(d−3)

|

↔
{z

2 14 d(d−1)(d−2)

}

|

↔
{z

2 41 d(d−1)(d−2)

}

|

10

10

↔
{z

2 14 d(d−1)(d−2)

}

|

2 41 d(d−1)

}

(12)
Classes with components having orbits of order 2 and 1 are shown below, each component class annotated
by the total number of independent real values contributed in dimension d. Each orbit in the first, second
and fourth classes contributes a single independent real value, because each component is stabilised by (at
least) one self-adjoining symmetry; each orbit in the third class contributes instead two independent real
values, because the components are only stabilised by a self-transposing symmetry.
10,11

↔
{z

|

1
2 d(d−1)

01,11

}

|

↔
{z

1
2 d(d−1)

10,01

}

|

(13)

↔
{z

}

2 12 d(d−1)

|{z}
d

Adding up the contributions from all orbit classes, we see that the states of d-dimensional density
hypercubes form a convex cone of real dimension 12 (d 4 − 3d 3 + 7d 2 − 3d) within the (2d 4 )-dimensional
real vector space of complex fourth-order tensors.

2.3

Normalisation and causality

The “forest” discarding maps DD(H) := CPM( H ) in DD(fHilb) (i.e. the doubled versions of the
discarding maps of CPM(fHilb)) form an environment structure [9, 12], and we say that a map of density
hypercubes is normalised if the corresponding CP map is trace preserving (with normalised states as a
special case):
F̄

F̄

normalised
F

⇔

=

(14)

F

Normalised maps of density hypercubes form a sub-SMC of DD(fHilb), which we refer to as the
normalised sub-category. Sub-normalised maps of density hypercubes can be defined analogously by
requiring the corresponding CP map to be trace non-increasing: they also form a sub-SMC of DD(fHilb),
which we refer to as the sub-normalised sub-category.
Despite the presence of several kinds of discarding maps, the following results shows that the
sub-normalised sub-category is causal [3], or equivalently that that the normalised sub-category is
terminal [6, 7].
Proposition 1. The process theory DD(fHilb) is causal, in the following sense: for every object DD(H),
the only effect DD(H) → R+ in DD(fHilb) which yields the scalar 1 on all normalised states of DD(H) is
the “forest” discarding map of density hypercubes DD(H) .

<!-- page 6 -->
6

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

3

Decoherence and Hyper-decoherence

So far, we have constructed a symmetric monoidal category, which is enriched in convex cones and comes
equipped with an environment structure providing a notion of normalization. The final ingredients necessary for the definition of the categorical probabilistic theory of density hypercubes is the demonstration
that classical systems and quantum systems arise in the Karoubi envelope of DD(fHilb) by choosing some
suitable family of decoherence and hyper-decoherence maps.

3.1

Decoherence to classical theory

Consider a finite-dimensional Hilbert space H and a classical structure on it, associated with some
orthonormal basis (|ψx i)x∈X . We define the -decoherence map dec on the density hypercube DD(H) to
be the following morphism in DD(fHilb):
H

dec

H

=

:=
H

H

∑

x∈X

†

H

Ψx

H

Ψ†x

Ψx

H

Ψx

H

(15)

The dec map defined above is idempotent, so it can be used to define classical systems via the Karoubi
envelope construction—in the same way as ordinary decoherence maps gives rise to classical systems in
quantum theory. It should be noted that decoherence maps defined this way are sub-normalised but not
normalised, so that the hyperquantum-to-classical transition in the theory of density hypercubes is not
deterministic; we defer further discussion of this point to the next sub-section on hyper-decoherence.
Proposition 2. Let Split(DD(fHilb)) be the Karoubi envelope of DD(fHilb), and write Split(DD(fHilb))K
for the full subcategory of Split(DD(fHilb)) spanned by objects in the form (DD(H), dec ). There
is an R+ -linear monoidal equivalence of categories between Split(DD(fHilb))K and the probabilistic
theory R+ -Mat of classical systems. Furthermore, classical stochastic maps correspond to the maps
in Split(DD(fHilb))K normalised with respect to the discarding maps (DD(H),dec ) := DD(H) ◦ dec ,
which we can write explicitly as follows:
H

(DD(H),dec )

H

3.2

H

=

:=

(16)
H

Hyper-decoherence to quantum theory

We now show that the quantum systems arise in the Karoubi envelope as well, via suitable hyperdecoherence maps. Recall that the generic discarding map in the theory of density hypercubes involved
two pieces: (the doubled version of) a traditional discarding map from CPM(fHilb) and a second “tree-ona-bridge” discarding map derived from a classical structure . In the previous sub-section, we saw that the
latter is the discarding map of some classical system living in the Karoubi envelope Split(DD(fHilb)),
and that it can be used to define the “hyper-quantum–to–classical” decoherence maps. In this sub-section,
we shall see that this “hyper-quantum–to–classical” decoherence process can be understood in two
steps: a “hyper-quantum–to–quantum” hyper-decoherence, followed by the usual “quantum–to–classical”
decoherence.

<!-- page 7 -->
S. Gogioso & C. M. Scandolo

7

If is a classical structure on a density hypercube DD(H), we define the -hyper-decoherence map
hypdec to be the following map of density hypercubes:
H

H

H

H

:=

hypdec

(17)

Hyper-decoherence maps are idempotent, and hence we can consider the full subcategory C of the Karoubi
envelope Split(DD(fHilb)) spanned by objects in the form (DD(H), hypdec ): doing so allows us to prove
that the hyper-decoherence maps defined above truly provide the desired “hyper-quantum–to–quantum”
decoherence, as considered by [18, 19].
Proposition 3. Let Split(DD(fHilb)) be the Karoubi envelope of DD(fHilb), and write Split(DD(fHilb))Q
for the full subcategory of Split(DD(fHilb)) spanned by objects in the form (DD(H), hypdec ). There
is an R+ -linear monoidal equivalence of categories between Split(DD(fHilb))Q and the probabilistic
theory CPM(fHilb) of quantum systems and CP maps between them. Furthermore, trace-preserving
CP maps correspond to the maps in Split(DD(fHilb))Q normalised with respect to the discarding maps
DD(H) ◦ hypdec , which we can write explicitly as follows:
(DD(H),hypdec ) :=
H

(DD(H),hypdec )

H

=

:=
H

(18)
H

Taking the double-dilation construction together with the content of Propositions 2 and 3, we come to
the following definition of a categorical probabilistic theory [12] of density hypercubes.
Definition 4. The categorical probabilistic theory of density hypercubes DH(fHilb) is defined the be the
full sub-SMC of Split(DD(fHilb)) spanned by objects in the following form:
• the density hypercubes (DD(H), idDD(H) );
• the quantum systems (DD(H), hypdec ), for all classical structures

on H;

• the classical systems (DD(H), dec ), for all classical structures on H.
The environment structure for the categorical probabilistic theory is given by the discarding maps
DD(H) ,
(DD(H),hypdec ) and
(DD(H),dec ) respectively. The classical sub-category for the categorical
probabilistic theory is the full sub-SMC spanned by the classical systems.
The hyper-quantum–to–classical and hyper-quantum–to–quantum decoherence maps of density hypercubes play well together with the quantum–to–classical decoherence map of quantum theory: the
decoherence map dec : (DD(H), idDD(H) ) → (DD(H), dec ) of density hypercubes factors, as one would
expect, into the hyper-decoherence map hypdec : (DD(H), idDD(H) ) → (DD(H), hypdec ) followed
by the decoherence map dec : (DD(H), hypdec ) → (DD(H), dec ) of quantum systems. From this,
it is clear that the reason why hyper-quantum–to–classical transition was sub-normalised is that the
hyper-quantum–to–quantum transition itself is sub-normalised (see Appendix B).
The sub-normalisation of hyper-decoherence maps is a sign that the theory of density hypercubes
presented here is still partially incomplete, and that some suitable extension will need to be researched in
the future. What we know for sure is that the current theory does not satisfy the no-restriction condition on
effects, and that an extension in which hyper-decoherence maps are normalised is possible: the additional
effect needed by normalisation exists in CPM(fHilb) and is non-negative on all states of DD(fHilb) (see
Appendix B). In line with the recent no-go theorem of [19], preliminary considerations seem to indicated
that the addition of said effect would mean that the theory no longer satisfies purification.

<!-- page 8 -->
8

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

4

Higher Order Interference

In this section, we will show that the theory of density hypercubes displays third- and fourth-order
interference effects, broadly inspired by the framework for higher-order interference in GPTs presented
by [1, 2, 18]. Because interference has to do with decompositions of the identity map in terms of certain
projectors, we begin by introducing a handy graphical notation for keeping track of the various pieces that
the identity map is composed of.
The identity map of hyper-quantum systems idDD(H) : DD(H) → DD(H) takes the following explicit
form in fHilb, for any orthonormal basis (|ψx i)x∈X of the Hilbert space H:
H∗

H∗

H∗

H∗

=
H

H

H

H

H∗

ψxT01

ψx∗01

H∗

H∗

ψxT10

ψx∗10

H∗

H

ψx†11

ψx11

H

H

ψx†00

ψx00

H

∑

x00 ,x01 ,x10 ,x11 ∈X

(19)

In order to denote the pieces in the decomposition corresponding to specific values x00 , x01 , x10 , x11 ∈ X
of the indices, we adopt the following graphical notation, inspired by the Z2 × Z2 symmetry of the
components:
x00

x10

H∗

ψxT01

ψx∗01

H∗

H∗

ψxT10

ψx∗10

H∗

H

ψx†11

ψx11

H

H

ψx†00

ψx00

H

:=
x01

x11

(20)

In fact, we will adopt the same colour-based notation for index values which we originally introduced in
Section 2, so that the following is a decomposition piece involving two distinct index values {•, •} ⊆ X:
H∗

ψ•T

ψ•∗

H∗

H∗

ψ•T

ψ•∗

H∗

H

ψ•†

ψ•

H

H

ψ•†

ψ•

H

:=

(21)

Using the colour-based notation defined above for its pieces, the identity on a 2-dimensional hyperquantum system (with X = {•, •}) would be fully decomposed as follows:
idC2 =

+

+

+

+

+

+

+
(22)
The same notation can be used to graphically decompose projectors corresponding to various subspaces
determined by the orthonormal basis (|ψx i)x∈X . For any non-empty subset U ⊆ X, we define the following
projector on DD(H):
!
PU := DD

+

+

+

∑ |ψx ihψx |

x∈U

+

+

+

+

+

(23)

<!-- page 9 -->
S. Gogioso & C. M. Scandolo

9

In particular, the P{•} for • ∈ X are the projectors corresponding to the individual vectors |ψ• i of the
basis, while PX is the identity idDD(H) . No matter how large X is (with #X ≥ 2), the projectors P{•,•}
corresponding to 2-element subsets {•, •} ⊆ X are always decomposed as follows:
+
(24)
The presence of higher order interference in the theory of density hypercubes is really a matter of shapes:
when the dimension of H is at least 3, the identity contains pieces of shapes which do not appear in
projectors for 1-element and 2-element subsets. Because of this, in the theory of density hypercubes
the probabilities obtained from 1-slit and 2-slit interference experiments will not be enough to explain
the probabilities obtained from 3-slit and/or 4-slit experiments; however, the probabilities obtained from
1-slit, 2-slit, 3-slit and 4-slit experiments will always be enough to explain the probabilities obtained in
experiments with 5 or more slits.
Below you can see an atlas of all possible shapes that pieces of the identity can take in our graphical
notation, together with a note of the smallest dimension that a projector must have to contain pieces of
that shape:
P{•,•} =

+

+

+

+

+

+

+

+

+

+

+

+

+

+

(25)
| {z } |
1-dim

{z

} |

2-dim

{z

3-dim

} | {z }
4-dim

The shape labelled as 1-dimensional only requires a single index value, and hence pieces of that shape
appear in all projectors. The shapes labelled as 2-dimensional all require exactly two distinct index values,
and hence pieces of those shapes can only appear in projectors for subsets with at least 2 elements. The
shapes labelled as 3-dimensional all require exactly three distinct index values, and hence pieces of those
shapes can only appear in projectors for subsets with at least 3 elements. Finally, the shape labelled
as 4-dimensional requires exactly four index values, and hence pieces of that shape can only appear in
projectors for subsets with at least 4 elements.
Thanks to the graphical notation introduced above, we already have a first intuition of why density
hypercubes display higher-order interference. However, a rigorous proof requires a complete set-up with
states, projectors, measurements and probabilities for a d-slit interference experiment, so that is what we
now endeavour to provide.
1. We choose a d-dimensional space H ∼
= Cd , and we value our tensor indices in the set X = {1, ..., d}
(the same set that we use to label the d slits).
2. We fix an orthonormal basis (|xi)x∈X , and we interpret |xi to be the state in which the particle goes
through slit x with certainty.
3. The initial state for the particle is the superposition state in which the particle goes through each
slit with the same amplitude. More precisely, it is the pure normalised density hypercube state ρ+
corresponding to the vector √1d |ψ+ i := √1d (|1i + ... + |di):
ρ+ :=

1 Ψ+
d 2 Ψ+

H
H

(26)

4. The particle goes through some non-empty subset U ⊆ X of slits at random: afterwards, the
experimenter knows which subset the particle passed through, but no more information than that is
available in the universe.

<!-- page 10 -->
10

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach
5. The particle is measured at the screen, and the experimenter estimates the probability P[+|U] that
the particle is still in state ρ+ after having passed through the given subset U of the slits:
P[+|U] :=

1 Ψ+
d 2 Ψ+

PU

Ψ†+

PU

Ψ†+

1
d2

(27)

It is immediate to see that the outcome probability P[+|U] depends solely on the number of different
pieces appearing in the decomposition of the projector PU :
P[+|U] =

1
· number of pieces in PU
d4

(28)

To count the number of pieces in PU , it is convenient to group them by shapes. If U is a subset of size k,
standard combinatorial arguments can be usedto obtain the number of pieces of each shape appearing in
the decomposition (as a convention, we set kj = 0 for j > k):
(29)
| {z } |
(1k)·1!

{z

} |

7 shapes, (2k)·2! each

{z

6 shapes, (3k)·3! each

} | {z }
(4k)·4!

By adding up the contributions from pieces of each shape, we get the following closed expression for the
outcome probability P[+|U]:
1
(30)
P[+|U] = 4 (#U)4
d
For d ≥ 3 we observe third-order interference, witnessed (by definition) by the following inequality:
P[+|{1, 2, 3}] 6=

∑ P[+|V ] − ∑ P[+|V ]
V ⊂{1,2,3}

V ⊂{1,2,3}

s.t. #V =2

s.t. #V =1

(31)

Indeed, the left hand side evaluates to 81/d 4 , while the right hand side evaluates to the following expression
(again by standard combinatorial arguments):
 
  i
1
1h 3 4
3 4
1
2 −
1 = 4 45 6= 4 81
(32)
4
d
2
d
d
1

The difference between left and right hand sides is 36/d 4 , which is exactly the contribution d14 6 · 33 · 3!
of the 6 shapes requiring 3 distinct values (appearing in P{1,2,3} but not in any of the sub-projectors). For
d ≥ 4 we observe fourth-order interference, witnessed (by definition) by the following inequality:
P[+|{1, 2, 3, 4}] 6=

∑ P[+|V ] − ∑ P[+|V ] + ∑ P[+|V ]
V ⊂{1,2,3,4}

V ⊂{1,2,3,4}

V ⊂{1,2,3,4}

s.t. #V =3

s.t. #V =2

s.t. #V =1

(33)

Indeed, the left hand side evaluates to 256/d 4 , while the right hand side evaluates to the following
expression (again by standard combinatorial arguments):
 
 
  i
1h 4 4
4 4
4 4
1
1
3 −
2 +
1 = 4 232 6= 4 256
(34)
4
d
3
2
1
d
d

<!-- page 11 -->
S. Gogioso & C. M. Scandolo

11


The difference between left and right hand sides is 24/d 4 , which is exactly the contribution d14 44 · 4! of
the shape requiring 4 distinct values (appearing in P{1,2,3,4} but not in any of the sub-projectors).
For d ≥ 5, however, we observe absence of fifth-order (or higher-order) interference, witnessed (by
definition) by the following equality:
P[+|{1, 2, 3, 4, 5}] =
+

∑ P[+|V ] −

∑ P[+|V ]

V ⊂{1,2,3,4,5}

V ⊂{1,2,3,4,5}

s.t. #V =4

s.t. #V =3

∑ P[+|V ] −

∑ P[+|V ]

V ⊂{1,2,3,4,5}

V ⊂{1,2,3,4,5}

s.t. #V =2

s.t. #V =1

Indeed, the left hand side evaluates to 625/d 4 , and the right hand side yields the same:
 
 
 
  i
5 4
5 4
5 4
1
1h 5 4
4 −
3 +
2 −
1 = 4 625
4
4
3
2
1
d
d

5

(35)

(36)

Conclusions

In this work, we used an iterated CPM construction known as double-dilation to construct a full-fledged
probabilistic theory of density hypercubes, possessing hyper-decoherence maps and showing higher-order
interference effects. We have defined all the necessary categorical structures. We have gone over the
mathematical detail of the (hyper-)decoherenceinduced relationship between our new theory, quantum
theory and classical theory. We have imported diagrammatic reasoning from the familiar setting of
mixed-state quantum theory. We have developed a graphical formalism to study the internal component
symmetries of states and processes. Finally, we have shown that the theory displays interference effects of
orders up to four, but not of orders five and above.
A number of questions are left open and will be answered as part of future work. Firstly, we
endeavour to carry out a more physically-oriented analysis of the theory, including a study of the structure
of normalised states and effects and a characterisation of the normalised reversible transformations.
Secondly, we need to investigate the physical significance and implications of sub-normalisation of the
hyper-decoherence maps, and construct a suitable extension of our theory where said maps become
normalised. Finally, we intend to look at concrete implementations of certain protocols in our theory, such
as those previously studied [16, 18] in the context of higher-order interference.
From a categorical standpoint, we also wish to further understand the specific roles played by doublemixing and double-dilation in our theory. At present, we know that the former is enough for density
hypercubes to show higher-order interference and decohere to classical systems, but the latter seems to be
necessary for quantum systems to arise by hyper-decoherence. Further investigation will hopefully shed
more light on the individual contributions of the two constructions. Finally, we endeavour to investigate
the generalisation of our results to higher iterated dilation, and more generally to higher-order CPM
constructions [11] (with finite abelian symmetry groups other than the ZN2 groups arising from iterated
dilation).

<!-- page 12 -->
12

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

References
[1] H. Barnum, C. M. Lee, C. M. Scandolo & J. H. Selby (2017): Ruling out Higher-Order Interference from
Purity Principles. Entropy 19(6), p. 253, doi:10.3390/e19060253.
[2] H. Barnum, M. P. Müller & C. Ududec (2014): Higher-order interference and single-system postulates
characterizing quantum theory. New J. Phys. 16(12), p. 123029, doi:10.1088/1367-2630/16/12/123029.
[3] G. Chiribella, G. M. D’Ariano & P. Perinotti (2010): Probabilistic theories with purification. Phys. Rev. A 81,
p. 062348, doi:10.1103/PhysRevA.81.062348.
[4] G. Chiribella & C. M. Scandolo (2016): Entanglement as an axiomatic foundation for statistical mechanics.
arXiv:1608.04459 [quant-ph]. Available at http://arxiv.org/abs/1608.04459.
[5] G. Chiribella & C. M. Scandolo (2017): Microcanonical thermodynamics in general physical theories. New J.
Phys. 19(12), p. 123043. Available at 10.1088/1367-2630/aa91c7.
[6] Bob Coecke (2016): Terminality implies no-signalling... and much more than that. New Generation Computing
34(1-2), pp. 69–85, doi:10.1007/s00354-016-0201-6.
[7] Bob Coecke & Raymond Lal (2013): Causal categories: relativistically interacting processes. Foundations of
Physics 43(4), pp. 458–501, doi:10.1007/s10701-012-9646-8.
[8] Bob Coecke, Dusko Pavlovic & Jamie Vicary (2013): A new description of orthogonal bases. Mathematical
Structures in Computer Science 23(3), pp. 555–567.
[9] Bob Coecke & Simon Perdrix (2010): Environment and classical channels in categorical quantum mechanics.
In: International Workshop on Computer Science Logic, Springer, pp. 230–244.
[10] B. Dakić, T. Paterek & Č. Brukner (2014): Density cubes and higher-order interference theories. New J. Phys.
16(2), p. 023028, doi:10.1088/1367-2630/16/2/023028.
[11] S Gogioso (2018): Higher-order CPM Constructions.
[12] S. Gogioso & C. M. Scandolo (2018): Categorical Probabilistic Theories. In B. Coecke & A. Kissinger, editors:
Proceedings 14th International Conference on Quantum Physics and Logic, Nijmegen, The Netherlands, 3-7
July 2017, Electronic Proceedings in Theoretical Computer Science 266, Open Publishing Association, pp.
367–385, doi:10.4204/EPTCS.266.23.
[13] F. Jin, Y. Liu, J. Geng, P. Huang, W. Ma, M. Shi, C. Duan, F. Shi, X. Rong & J. Du (2017): Experimental test
of Born’s rule by inspecting third-order quantum interference on a single spin in solids. Phys. Rev. A 95, p.
012107, doi:10.1103/PhysRevA.95.012107.
[14] T. Kauten, R. Keil, T. Kaufmann, B. Pressl, Č. Brukner & G. Weihs (2017): Obtaining tight bounds on
higher-order interferences with a 5-path interferometer. New J. Phys. 19(3), p. 033017, doi:10.1088/13672630/aa5d98.
[15] M. Krumm, H. Barnum, J. Barrett & M. P. Müller (2017): Thermodynamics and the structure of quantum
theory. New J. Phys. 19(4), p. 043025, doi:10.1088/1367-2630/aa68ef.
[16] C. M. Lee & J. H. Selby (2016): Deriving Grover’s lower bound from simple physical principles. New J. Phys.
18(9), p. 093047, doi:10.1088/1367-2630/18/9/093047.
[17] C. M. Lee & J. H. Selby (2016): Generalised phase kick-back: the structure of computational algorithms from
physical principles. New J. Phys. 18(3), p. 033023, doi:10.1088/1367-2630/18/3/033023.
[18] C. M. Lee & J. H. Selby (2017): Higher-Order Interference in Extensions of Quantum Theory. Found. Phys.
47(1), pp. 89–112, doi:10.1007/s10701-016-0045-4.
[19] C. M. Lee & J. H. Selby (2017): A no-go theorem for theories that decohere to quantum mechanics.
arXiv:1701.07449 [quant-ph]. Available at http://arxiv.org/abs/1701.07449.
[20] C. M. Lee, J. H. Selby & H. Barnum (2017): Oracles and query lower bounds in generalised probabilistic
theories. arXiv:1704.05043 [quant-ph]. Available at https://arxiv.org/abs/1704.05043.
[21] G. Niestegge (2013): Three-Slit Experiments and Quantum Nonlocality. Found. Phys. 43(6), pp. 805–812,
doi:10.1007/s10701-013-9719-3.

<!-- page 13 -->
S. Gogioso & C. M. Scandolo

13

[22] D. K. Park, O. Moussa & R. Laflamme (2012): Three path interference using nuclear magnetic resonance: a
test of the consistency of Born’s rule. New J. Phys. 14(11), p. 113025, doi:10.1088/1367-2630/14/11/113025.
[23] A. Sinha, A. H. Vijay & U. Sinha (2015): On the superposition principle in interference experiments. Sci.
Rep. 5, p. 10304, doi:10.1038/srep10304.
[24] U. Sinha, C. Couteau, T. Jennewein, R. Laflamme & G. Weihs (2010): Ruling Out Multi-Order Interference in
Quantum Mechanics. Science 329(5990), pp. 418–421, doi:10.1126/science.1190545.
[25] R. D. Sorkin (1994): Quantum mechanics as quantum measure theory. Mod. Phys. Lett. A 9(33), pp.
3119–3127, doi:10.1142/S021773239400294X.
[26] R. D. Sorkin (1997): Quantum Classical Correspondence: The 4th Drexel Symposium on Quantum Nonintegrability, chapter Quantum Measure Theory and its Interpretation, pp. 229–251. International Press,
Boston.
[27] C. Ududec (2012): Perspectives on the formalism of quantum theory. Ph.D. thesis, University of Waterloo.
[28] C. Ududec, H. Barnum & J. Emerson (2011): Three Slit Experiments and the Structure of Quantum Theory.
Found. Phys. 41(3), pp. 396–405, doi:10.1007/s10701-010-9429-z.
[29] M. Zwart & B. Coecke (2018): Double Dilation 6= Double Mixing (extended abstract). In B. Coecke &
A. Kissinger, editors: Proceedings 14th International Conference on Quantum Physics and Logic, Nijmegen,
The Netherlands, 3-7 July 2017, Electronic Proceedings in Theoretical Computer Science 266, Open Publishing
Association, pp. 133–146, doi:10.4204/EPTCS.266.9.
[30] K. Życzkowski (2008): Quartic quantum theory: an extension of the standard quantum mechanics. J. Phys. A
41(35), p. 355302, doi:10.1088/1751-8113/41/35/355302.

A

Proofs

Proposition 1. The process theory DD(fHilb) is causal, in the following sense: for every object DD(H),
the only effect DD(H) → R+ in DD(fHilb) which yields the scalar 1 on all normalised states of DD(H) is
the “forest” discarding map of density hypercubes DD(H) .
Proof. Seen as an effect in CPM(fHilb), any such effect must take the form of a sum ∑x∈X px |ax ihax |,
where px ∈ R+ and (|ax i)x∈X is an orthonormal basis for H ⊗ H which satisfies an additional condition due
to the symmetry requirement for effects in DD(fHilb). If we write σH,H for the symmetry isomorphism
H ⊗ H → H ⊗ H which swaps two copies of H in fHilb, the additional condition on the orthonormal basis
implies that for each x ∈ X there is a unique y ∈ X such that σH,H |ax i = eiθx |ay i and px = py ; we define an
involutive bijection s : X → X by setting s(x) to be that unique y. For each x ∈ X, consider the normalised
state ρx := 21 (|ax ihax | + |as(x) ihas(x) |) in CPM(fHilb), which we can realise in the sub-category DD(fHilb)
by considering the classical structure on C2 corresponding to orthonormal basis |0i, |1i and the vector
|rx i := √41 (|ax i ⊗ |0i + |as(x) i ⊗ |1i):
2

Rx

ρx =

1
2

Ax

H

As(x)

H

+
Ax

H

As(x)

!

H

=

(37)

H
Rx

H

<!-- page 14 -->
14

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

Now observe that the requirement that our effect yield 1 on all normalised states implies, in particular,
that the following equation must hold:
H

Rx

=

1

=

A

1
(px + ps(x) )
2

=

(38)

px

H

Rx

As a consequence, our effect is written ∑x∈X |ax ihax |, which is exactly the “forest” discarding map
of density hypercubes on DD(H).

DD(H)

Proposition 2. Let Split(DD(fHilb)) be the Karoubi envelope of DD(fHilb), and write Split(DD(fHilb))K
for the full subcategory of Split(DD(fHilb)) spanned by objects in the form (DD(H), dec ). There
is an R+ -linear monoidal equivalence of categories between Split(DD(fHilb))K and the probabilistic
theory R+ -Mat of classical systems. Furthermore, classical stochastic maps correspond to the maps
in Split(DD(fHilb))K normalised with respect to the discarding maps (DD(H),dec ) := DD(H) ◦ dec ,
which we can write explicitly as follows:
H

(DD(H),dec )

H

=

:=
H

(16)
H

Proof. Consider two objects (DD(H), dec ) and (DD(K), dec ), where and are special commutative
†-Frobenius algebras associated with orthonormal bases (|ψx i)x∈X and (|φy i)y∈Y of H and K respectively.
The morphisms (DD(H), dec ) → (DD(K), dec ) in Split(DD(fHilb)) are exactly the maps of density
hypercubes DD(H) → DD(K) in the following form:
F̄

(39)
F

We can expand the definition of decoherence maps to see that these morphisms correspond to generic
matrices Mxy of non-negative real numbers, with matrix composition as sequential composition, Kronecker
product as tensor product, and the R+ -linear structure of matrix addition.
Ψ†x

F̄

=

Ψx

Φy†

F̄

Φy

(40)

∑∑

x∈X y∈Y

Ψ†x

F

Ψx

Φ†y

F

Φy

The discarding maps obtained by decoherence of the environment structure for DD(fHilb) yield the usual
environment structure for classical systems:
H

(H ,dec )

H

=

:=
H

=
H

∑

x∈X

Hence CK is equivalent to the probabilistic theory R+ -Mat of classical systems.

H

Ψ†x

H

Ψ†x

(41)

<!-- page 15 -->
S. Gogioso & C. M. Scandolo

15

Proposition 3. Let Split(DD(fHilb)) be the Karoubi envelope of DD(fHilb), and write Split(DD(fHilb))Q
for the full subcategory of Split(DD(fHilb)) spanned by objects in the form (DD(H), hypdec ). There
is an R+ -linear monoidal equivalence of categories between Split(DD(fHilb))Q and the probabilistic
theory CPM(fHilb) of quantum systems and CP maps between them. Furthermore, trace-preserving
CP maps correspond to the maps in Split(DD(fHilb))Q normalised with respect to the discarding maps
DD(H) ◦ hypdec , which we can write explicitly as follows:
(DD(H),hypdec ) :=
H

(DD(H),hypdec )

H

=

:=
H

(18)
H

Proof. We can define an essentially surjective, faithful monoidal functor from Split(DD(fHilb)) to the
category CPM(fHilb) of quantum systems and CP maps by setting (DD(H), hypdec ) 7→ H on objects
and doing the following on morphisms:
H

K

F̄

F̄

7→
H

K

F

H

K

(42)

F

In order to show monoidal equivalence we need to show that the functor is also full, i.e. that every
CP map can be obtained from a map of Split(DD(fHilb)) in this way. Because of compact closure,
it is actually enough to show that all states can be obtained this way. Consider a finite-dimensional
Hilbert space H and a classical structure on it, and write (|ψx i)x∈X for the orthonormal basis of H
associated to . The most generic mixed quantum state on H takes the form ρ = ∑y∈Y py |γy ihγy |, where
(|γy i)y∈Y is some orthonormal basis of H and py ∈ R+ . Let be the classical
structure associated
with the
p
p
√
orthonormal basis (|γy i)y∈Y , and define the states | γy i := ∑x∈X |ψx i hψx |γy i, where hψx |γy i ∈ C is
p
2
√
√
such that hψx |γy i = hψx |γy i ∈ C. If we write |φ i := ∑yY py | γy i ⊗ |γy i, then the desired state ρ can
be obtained as follows:
p
√
Γy
py
Φ̄
ρ = ∑ py Γy
= ∑ √
=
(43)
p
y∈Y
y∈Y
Γy
py
Φ
Hence the monoidal functor defined above is full, faithful and essentially surjective, i.e. an equivalence of
categories. Furthermore, it is R+ -linear and it respects discarding maps.

B

Possibility of extension for the theory of density hypercubes

The theory of density hypercubes presented in this work is fully-fledged1 but incomplete: as shown by
Equation 18, the hyper-decoherence maps are not normalised (i.e. they are not “deterministic”, in the
parlance of OPTs/GPTs)
H

(DD(H),hypdec )

H

=

:=
H

(18)
H

1 In the sense that it contains all the features necessary to consistently talk about operational scenarios, such as preparations,
measurements, controlled transformations, reversible transformation, test, non-locality scenarios, etc.

<!-- page 16 -->
16

Density Hypercubes, Higher Order Interference and Hyper-Decoherence: a Categorical Approach

When it comes to this work, however, this is not much of a problem: all we need to show is that
an extension of our theory can exists in which the “tree-on-a-bridge” effect above can be completed
to the discarding map, and our results—both hyper-decoherence to quantum theory and higher-order
interference—will automatically apply to any such extension.
Let (|ψx i)x∈X be the orthonormal basis associated with the special commutative †-Frobenius algebra
. The effect needed to complete (DD(H),hypdec ) to the discarding map DD(H) is itself an effect in
CPM(fHilb), which can be written explicitly as follows:
H

H

−
H

=
H

∑

x,y∈X
s.t. x6=y

H

Ψ†x

H

Ψ†y

(44)

Because it is an effect in CPM(fHilb), which has R+ as its semiring of scalars, it is in particular nonnegative on all states in DD(fHilb), showing that: (i) hyper-decoherence maps are sub-normalised; (ii) our
theory does not satisfy the no-restriction condition; (iii) an extension to a theory with normalised hyperdecoherence is possible. This shows that our results on hyper-decoherence have physical significance.
Furthermore, let |1i, ..., |di be an orthonormal basis of Cd , and let correspond to the Fourier basis for
the finite abelian group Zd :


1 d i 2π jk
d
√ ∑e
| ji
(45)
d j=1
k=1,...,d
Choosing k := d, in particular, shows that the orthonormal basis above contains the state √1d |ψ+ i used
in Section 4. Then the effect defined in Equation 44 also shows that the computation of P[+|U] in
Section 4 can be done as part of a bona-fide measurement in any such extended theory, and hence that our
higher-order interference result has physical significance.
