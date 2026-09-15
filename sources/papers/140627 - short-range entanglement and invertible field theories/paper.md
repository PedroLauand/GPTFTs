---
type: paper
date: 2014-06-27
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1406.7278v2)
reviewed: false
---

# Short-range entanglement and invertible field theories

Machine-generated and unreviewed text extraction of arXiv:1406.7278v2
(59 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1406.7278v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
SHORT-RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

arXiv:1406.7278v2 [cond-mat.str-el] 10 Aug 2014

DANIEL S. FREED
Abstract. Quantum field theories with an energy gap can be approximated at long-range by
topological quantum field theories. The same should be true for suitable condensed matter systems.
For those with short range entanglement (SRE) the effective topological theory is invertible, and
so amenable to study via stable homotopy theory. This leads to concrete topological invariants of
gapped SRE phases which are finer than existing invariants. Computations in examples demonstrate
their effectiveness.

Contents
1. Introduction
2. Field theories from a bordism point of view
2.1. Field theories
2.2. Invertible field theories
2.3. Relative field theories and anomalies
2.4. Global symmetries and equivariant extensions
2.4.1. General discussion
2.4.2. Anomalies
2.4.3. Gauging antilinear symmetries
2.5. Unitarity
2.6. Topological field theories and the cobordism hypothesis
2.7. Invertible topological theories and maps of spectra
2.8. An illuminating example
3. The long-range effective topological field theory
3.1. Low energy, long time
3.2. Short-range entanglement hypothesis and its consequences
3.3. Symmetries and SPT phases
4. Bordism and homotopy theory
4.1. Madsen-Tillmann spectra
4.2. Variations
4.2.1. Global symmetry groups
4.2.2. Theories of H-type
4.2.3. Time-reversal symmetries
4.2.4. Orientation-reversal and unitarity
4.2.5. Interlude on unitarity
5. SRE phases
5.1. Target spectra
5.1.1. Preliminary: duals to the sphere spectrum
5.1.2. Bosonic theories
5.1.3. Fermionic theories
5.1.4. Antilinear symmetries
5.2. Topological invariants of short-range entangled phases

2
5
5
9
10
11
11
12
13
14
14
15
17
21
21
24
25
26
26
29
29
30
30
30
31
32
33
33
34
36
36
37

Date: August 10, 2014.
The work of D.S.F. is supported by the National Science Foundation under grant DMS-1207817. Some of this
work was undertaken at the Mathematical Sciences Research Institute as part of the program on Algebraic Topology.
1

<!-- page 2 -->
2

D. S. FREED

5.2.1. Bosonic theories
5.2.2. Fermionic theories
5.2.3. Symmetry protected topological phases
5.3. Relation to group (super) cohomology
6. Computations and special cases
6.1. d “ 1 bosonic theories: group cohomology
6.2. d “ 1 fermionic theories
6.3. d “ 2 bosonic theories: Kitaev E8 phase and chiral central charge
6.4. d “ 2 bosonic theories: mixed gravitational/gauge phases
6.5. d “ 3 bosonic theories: time-reversal symmetry
7. Boundary conditions and long-range topological field theories
7.1. Boundary terminations
7.2. The invertible field theory of an exotic d “ 3 bosonic phase
Appendix A. Some homotopy groups of Madsen-Tillmann spectra
References

37
38
39
39
40
41
41
43
47
48
49
49
51
52
57

1. Introduction
The long-range behavior of gapped systems in condensed matter physics is accessible via topology.
For noninteracting fermionic systems there is a classification of topological phases using ideas related
to K-theory [K1]. Over the past few years the interacting case has been vigorously studied, for both
fermionic systems and bosonic systems, with an emphasis on short-range entanglement (SRE); a
small sampling of papers is [CGW1, CGW2, CGLW, GW, LV, VS, We, PMN, CFV, WPS, HW, WS,
Ka1, Ka2, WGW, KTTW]. Particular symmetry protected topological (SPT) phases are captured
by group cohomology [CGLW, GW], but other investigations (e.g. [VS]) reveal the existence of
additional SRE phases and raise the question of a complete classification. In this paper we propose
an invariant of bosonic and fermionic SRE topological phases constructed from effective field theory.
Computations and examples demonstrate that it effectively detects known SRE phases.
Our proposal applies to gapped systems which at low energy (long time) can be approximated
by topological field theories. Such a system must be sufficiently local that it can be formulated
on arbitrary manifolds, and it must have a continuum limit which is a field theory, at least at low
energy. We do not investigate microscopic behavior at all in this paper, but rather simply assume
the existence of a long-range topological theory.1 Short range entanglement, or the absence of
topological order, is a microscopic assumption. Kitaev [K2, K3, K4] has been studying SRE phases
from first principles microscopically,2 and has suggested the macroscopic consequence that the longrange topological theory has a unique vacuum on any background manifold. We go further and
assume that the long-range topological field theory describing an SRE phase is fully extended and
invertible, concepts that we explain below. From mathematical investigations it has been known for
a long time that fully extended, invertible, topological field theories are equivalent to maps between
spectra in the sense of algebraic topology. This link with stable homotopy theory is the basis of
our proposal.
1Rather than a single long-range approximation, we envision a connected space of long-range theories.
2We remark that there is an alternative microscopic definition of SRE proposed by Chen-Gu-Wen [CGW1].

<!-- page 3 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

3

While our proposal in §5.2 is specific and precise, we neither formulate nor prove a mathematical
theorem which justifies it. Also, while we enumerate groups which should house invariants of SRE
phases, we do not argue either that the effective field theory is a complete invariant or that every
possible effective field theory is realized by a microscopic system. In place of proof the paper
marshals evidence in two stages. Pre-§5.2 is a long conceptual march leading to the proposal. Post§5.2 is a series of experimental checks, including the relationship to group cohomology, boundary
terminations, and specific computations. We include a long discussion in §6.3 about detecting
Kitaev’s E8 phase using invertible topological field theories. There are additional possible effective
field theories which are “4th roots”, perhaps an indication that not all possible effective theories are
realized by microscopic systems. Another example, the “3d bosonic E8 phase with half-quantized
surface thermal Hall effect” [VS], [BCFV], is also treated in detail.
It may be useful to broadly characterize our proposal in field-theoretic language: whereas the
group cohomology captures pure gauge theories, the additional SRE phases contain couplings to
gravity or are purely gravitational. The SPT phases have no purely gravitational component. More
fundamentally, the long-range field theory is envisioned as the low-energy behavior of the coupling
to gravity of the original system. (And, if there are global symmetries, we gauge them and so
couple to gauge theory too.)
Bordism as a tool to classify SPT phases appears differently in the recent papers of Kapustin [Ka1],
[Ka2], [KTTW]. In unpublished work Kitaev [K2, K3, K4] develops a classification of SRE phases
based on microscopic considerations. Their results and approach differ from ours, and it will be very
interesting to reconcile them. It may be that there is more microscopic information in the physics
which leads to different or additional input into the effective field theories. In particular, there are
a few ingredients in our proposal (choice of tangential structure, choice of target spectrum) which
involve leaps of faith and can easily be adjusted if further microscopic implications are discovered.
We begin in §2 with an exposition of several formal points in field theory: extended field theory,
invertible field theory, relative field theory, anomalies, global symmetries and gauging, topological
field theory, unitarity. While many of these concepts are familiar to physicists, the mathematical
language may be unfamiliar and we hope to provide some bridge here. We touch on the cobordism
hypothesis, which classifies fully extended topological theories, in §2.6; the precise nature of this
classification is illuminated in §2.8 with a toy example in preparation for a later discussion of
the “Kitaev E8 phase” in §6.3. But the cobordism hypothesis is overkill for invertible theories.
In §2.7 we describe the link between fully extended, invertible, topological field theories and stable
homotopy theory in general terms. That involves particular Madsen-Tillmann spectra, which are
unstable analogs of Thom’s bordism spectra; we describe them in §4. There we also discuss the
crucial theorem of Galatius-Madsen-Tillmann-Weiss [GMTW] which identifies these spectra as
geometric realizations of bordism categories. That these unstable bordism spectra are appropriate
to field theories is natural since field theories are dimension-specific. The material in §2 and §4 is
general background not particular to condensed matter systems.
In §3 we give much of the general argument about effective field theories for SRE topological
phases. We begin in §3.1 with elementary thoughts indicating why topology may sufficiently describe the low energy behavior of gapped systems. Most of our assumptions are stated explicitly
in §3.2. There is still conceptual work to translate those assumptions into concrete mathematical
statements. Specifically, once we know that SRE gapped phases give rise to invertible topological

<!-- page 4 -->
4

D. S. FREED

theories, there are still parameters to choose: the tangential structure on manifolds representing
space and the target category for the field theory. The latter is discussed in §5.1 separately for
bosonic and fermionic theories; the bosonic case is a bit surprising and we settle on a kludge for
the target spectrum. For the tangential structures we assume without much justification that in
bosonic theories the space manifolds are oriented and in fermionic theories they are spin. Along the
way we encounter a few tricky issues, for example the gauging of antilinear symmetries (§§2.4.3,
5.1.4) and implementation of unitarity (§4.2.5).
We state our proposal in §5.2. We divide theories into bosonic and fermionic. Also, symmetries
may be anomalous and we propose a classification of anomaly theories and anomalous gauged theories as well. Possible effective invertible topological theories for SRE phases with fixed symmetry
form an abelian group; for SPT phases they form a subgroup which we also delineate.
Our first deduction in §5.3 from the proposal is that the phases previously identified using group
cohomology are included. In §6.1 we show that for bosonic theories in d “ 1 space dimensions group
cohomology provides a complete classification, which agrees with known results [CLW]. Already
for fermionic theories in d “ 1 the situation is more interesting, as described in §6.2: we detect the
Majorana chain [K6] in our classification. In §6.3 we identify bosonic d “ 2 SRE phases. These
were introduced by Kitaev [K5], [K2] and are related to 2-spacetime3 dimensional chiral conformal
field theories whose chiral central charge is an integer divisible by 8. These central charges do not
show up in the usual account of the associated 3-spacetime dimensional topological field theory;
there only the reduction mod 8 is used. Our explanation of how they fit in here, and so the role
of the chiral central charge as a real number not taken mod 8, is based on the easier examples
discussed in §2.8. In §6.4 we illustrate a constraint imposed by unitarizability. In §6.5 we compute
that the abelian group of d “ 3 bosonic time-reversal symmetric effective SRE field theories is
isomorphic to pZ{2Zqˆ2 . One generator is accounted for by group cohomology, and we claim the
other is the 3d bosonic E8 phase with half-quantized surface thermal Hall effect mentioned earlier.
Finally, in §7 we give a general discussion of boundary conditions/terminations/excitations and use
it to justify the aforementioned claim. An appendix includes topological computations which are
needed in the text.
The notion of a non-extended invertible field theory arose in joint work with Greg Moore [FM1,
§5.5]. Fully extended invertible topological theories, and the relation to stable homotopy theory,
has been a longstanding discussion topic with Mike Hopkins and Constantin Teleman, as have
many other general ideas described in §2. In particular, we used these ideas in [FHT] to construct
a topological field theory based on the Verlinde ring. The specific application to SRE phases
described here crystallized during the Symmetry in Topological Phases workshop in Princeton, and
I thank the organizers for inviting me. I had long conversations with Alexei Kitaev after a first
draft of this paper was complete, and those inspired a significant modification of §5.1.2 and §6.3.
I thank him for sharing his perspectives. I also thank Zheng-Cheng Gu, Mike Hopkins, Anton
Kapustin, Constantin Teleman, Ashvin Vishwanath, Kevin Walker, Oscal Randal-Williams, and
Xiao-Gang Wen for very helpful conversations and correspondence.

3The number d above is the dimension of space; spacetime has dimension d ` 1.

<!-- page 5 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

5

2. Field theories from a bordism point of view
We begin with a formal viewpoint on the structure of a field theory, which is the lens through
which we analyze the long-range effective topological theory in §3. In the mathematics literature
this approach was abstracted in Segal’s axioms for two-dimensional conformal field theory [S1] and
in Atiyah’s axioms for topological field theories [A1]. The lectures [S2] treat general quantum field
theories from this perspective. Our focus in this paper is on invertible field theories, which we
define in §2.2. Other general topics we quickly review include extended field theories, relative field
theories, anomalies, gauging symmetries, and unitarity. We then focus on fully extended topological
theories, for which the powerful cobordism hypothesis [BD, L, F1] provides a classification result.
Invertible topological theories can be analyzed using homotopy theory, and in this section we explain
why that is true but defer a more precise description to §4. We conclude with a few toy examples
which illuminate subtleties we will encounter in the condensed matter systems of §6. The subtleties
discussed there may have broader interest. There are many expositions of this material, in addition
to the ones referenced earlier in this paragraph, and here we offer another. A somewhat different
point of view on topological field theories may be found in [MW]. The reader may wish to use this
section for reference and skip on first reading to later parts of the paper.
We remark that this formal viewpoint does not distinguish “classical” from “quantum”, and
indeed we will give examples of both types. Another remark is that the field theories which arise
in condensed matter physics are usually defined on spacetimes which are products of space and
time, whereas the discussion in this section models theories defined on more general spacetimes.
We discuss the necessary modification in §4.2 and account for it in the proposals of §5.2.
2.1. Field theories

Figure 1. Quantum mechanical evolution
Let n be the spacetime dimension of a field theory F , which we simply call the dimension of F .
We write n “ d ` 1 where d is the space dimension.4 The case n “ 1 (d “ 0) is mechanics; there is
only time. A quantum mechanical system assigns a complex vector space H (the ‘quantum Hilbert
space’) to a point and the time evolution Ut : H Ñ H to a closed interval of length t. The group
law Ut1 `t2 “ Ut1 ˝ Ut2 is encoded by gluing intervals, as illustrated in Figure 1. An n-dimensional
4In the condensed matter literature d is often called the dimension of the theory, whereas in quantum field theory

and string theory literature it is n which is the dimension. We use the terms ‘spacetime dimension’ and ‘space
dimension’ to avoid confusion.

<!-- page 6 -->
6

D. S. FREED

Euclidean field theory assigns a partition function F pXq P C to a compact n-dimensional manifold X with no boundary. There is a complex vector space F pY q for each compact pn ´ 1q-manifold,
thought of as a spatial slice, and now this ‘quantum Hilbert space’ may depend on Y . Roughly
speaking, the vector space F pS n´1 q attached to a small sphere S n´1 is the space of local operators,
and to a closed manifold X with k small open balls removed we attach the correlation functions

(2.1)

F pXz

k
ď

B n q : F pS n´1 q b ¨ ¨ ¨ b F pS n´1 q ÝÑ C,

i“1

as illustrated in Figure 2. Here all boundary components are “incoming”, whereas each interval in
Figure 1 has an incoming boundary component and an outgoing boundary component, each a single
point. There are analogous quantum evolution operators in any dimension for manifolds with both
incoming and outgoing components, and the group law of quantum mechanics has a generalization.

Figure 2. Correlation functions
The mathematical expression of this formal structure is the assertion that
(2.2)

F : Bordxn´1,ny ÝÑ Vect

is a homomorphism, or functor, between symmetric monoidal categories. The bordism category
Bordxn´1,ny consists of closed5 pn ´ 1q-manifolds and bordisms between them. A bordism X : Y0 Ñ
Y1 is a compact n-manifold with boundary, the boundary has a continuous partition p : BX Ñ t0, 1u
–
which divides it into incoming and outgoing components, and there are diffeomorphisms Y0 ÝÝÑ
–
pBXq0 and Y1 ÝÝÑ pBXq1 ; see Figure 3 in which one should view time as flowing from left to right.6
The target category has complex vector spaces as objects and linear maps as morphisms.7
There are two kinds of composition. The internal composition glues morphisms (Figure 4) and
the external composition is disjoint union. Similarly Vect has two composition laws: the internal
composition is the usual composition of linear maps and the external composition is tensor product.
The homomorphism (2.2) is required to preserve both composition laws. This formulation is rather
compact and one must unpack it to see the usual structures in field theory.
5A manifold is closed if it is compact without boundary.
6In that figure the diffeomorphisms map open collar neighborhoods. This guarantees that the composition, or

gluing, operation on bordisms yields smooth manifolds.
7One should use topological vector spaces and continuous linear maps. The topology on the vector spaces is not
relevant for topological field theories since the vector spaces are finite dimensional so have a unique linear topology.

<!-- page 7 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

7

Figure 3. A bordism X : Y0 Ñ Y1

Figure 4. Composition X 1 ˝ X of morphisms X : Y0 Ñ Y1 and X 1 : Y1 Ñ Y2
Typically one does not have bare n-manifolds, but rather each n-manifold X is endowed with
a space8 FpXq of fields. For example, in quantum mechanics (Figure 1) the 1-manifolds have a
Riemannian metric: the total length represents time. Higher dimensional field theories are often
formulated on Riemannian manifolds, though conformal field theories only require a conformal
structure. Other possible fields include orientations, spin structures, scalar fields, spinor fields, etc.
There is a bordism category Bordxn´1,ny pFq of manifolds equipped with a specified collection of
fields, and a functor
(2.3)

F : Bordxn´1,ny pFq ÝÑ Vect

represents a field theory with F as the set of (background) fields.
Example 2.4. To illustrate the notation, consider n “ 3 spacetime dimensional Chern-Simons
theory with gauge group T “ U p1q. There is a classical and a quantum theory. The fields FpXq
in the classical theory on a 3-manifold X consist of an orientation o and a principal T-bundle with
connection A. A closed 3-manifold X appears in the bordism category Bordx2,3y as a morphism
X : H2 Ñ H2 from the empty 2-manifold to itself. We have F pH2 q “ C and so F pXq : C Ñ C is
8Some fields, such as gauge fields, have internal symmetries, and they form a stack rather than a space.

<!-- page 8 -->
8

D. S. FREED

multiplication by a complex number, and if we make the fields explicit we denote it as F pX; o, Aq.
It is given by the formula
˙
ˆ
ż
i
A ^ dA
(2.5)
F pX; o, Aq “ exp ´
2π X,o
where implicitly, since A is a 1-form on the total space of a T-bundle, we have used a global section
to pull it down to the base X.9 The orientation is used to define integration of differential forms.
An oriented 2-manifold Y with T-connection has an attached Chern-Simons line F pY ; o, Aq, and
a bordism with fields has a relative Chern-Simons invariant mapping between the Chern-Simons
lines of the boundaries. This theory is invertible in the sense described in §2.2.
In the quantum theory [W1] one integrates over the gauge field A, and to get a well-defined
3-dimensional theory one needs in addition to the orientation o a field f which is a certain sort of
“framing” called a p1 -structure. The quantum invariant F pX; o, f q P C of a closed 3-manifold is an
arbitrary complex number—for example, it vanishes for some manifolds—and the quantum vector
spaces F pY ; o, f q do not necessarily have dimension one. So the quantum theory is not generally
invertible.
Remark 2.6. This description of a field theory has an important deficiency: it does not encode
smooth dependence on parameters. For example, the partition function on a closed n-manifold X
must depend smoothly on the background fields in FpXq. (Example: the smooth dependence of
the partition function of 2-dimensional Yang-Mills theory on the area of a surface.) Formally, the
definitions are enlarged to include fiber bundles X Ñ S of n-manifolds with fields, and these must
map to smoothly varying linear maps of smooth vector bundles over S. For topological theories,
which are our main concern, instead of families one usually postulates instead that the morphism
sets in the categories Bordxn´1,ny pFq and Vect have a topology and all maps are continuous. There
are two obvious topologies on the set of linear maps HompV0 , V1 q between two finite dimensional
vector spaces, equivalently on the set of n ˆ m matrices. We can use the usual topology induced
from the usual topology on the real numbers, or we can use the discrete topology. Both are used
in the classification scheme of §5.2.
Remark 2.7. One should also allow smooth families of field theories F . For topological field theories
it is more natural to study continuous families, i.e., to form a topological space of topological field
theories. This is crucial for the classification of gapped topological phases: if two gapped systems
are connected by a continuous path, we expect their effective topological field theories can also be
joined by a continuous path.
Finally, in this paper we will always consider fully extended field theories, usually topological. An
n-dimensional fully extended theory assigns invariants to manifolds of all dimensions ď n. These
compact manifolds with fields, which are now allowed corners, are organized into an algebraic
structure called a symmetric monoidal p8, nq-category, denoted Bordn pFq. The target for an
extended field theory is a symmetric monoidal p8, nq-category C, which typically has its “pn ´ 1qst
loop space” isomorphic to Vect. If so, then an extended field theory
(2.8)

F : Bordn pFq ÝÑ C

9If a section does not exist, there is a more complicated definition.

<!-- page 9 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

9

restricts on pn ´ 1q- and n-manifolds to a usual field theory (2.3). As already indicated, the
invariants attached to manifolds of dimension ď n ´ 2 tend to be categorical in nature. A theory
which extends in this way is fully local, and it is natural to make this strong locality hypothesis for
the effective topological theory which comes from a gapped physical theory. See [L] for a modern
description of fully extended topological field theories.

2.2. Invertible field theories
‘Invertibility’ refers to the tensor product operation on vector spaces and linear maps. First,
C is a “unit element” for tensor product in the sense that for any vector space V we have an
–
isomorphism C b V ÝÝÑ V which is naturally defined. Thus we call C a tensor unit. A complex
–
vector space V is invertible if there exists a vector space V 1 and an isomorphism V b V 1 ÝÝÑ C.
Since dimpV bV 1 q “ pdim V qpdim V 1 q, it follows immediately that if V is invertible, then dim V “ 1.
Conversely, if V is 1-dimensional then V b V ˚ is isomorphic to C. Thus the invertible vector spaces
are precisely the lines.
Invertibility of a linear map T : V0 Ñ V1 under tensor product is equivalent to the usual definition
of invertibility, namely that there exist S : V1 Ñ V0 such that the compositions S ˝ T and T ˝ S
are identity maps. If L is a line, then a linear map λ : L Ñ L is multiplication by a complex
number λ P C and it is invertible if and only if λ ­“ 0. We denote the nonzero complex numbers
as Cˆ .
Invertible complex vector spaces and invertible linear maps between them form a subcategory
Line Ă Vect which by definition has the property that all morphisms are invertible. Such a category
is called a groupoid.
An invertible field theory F : Bordn pFq Ñ Vect is one for which all vector spaces F pY q and
linear maps F pXq are invertible.10 We can express that by saying that F factors through a functor
Bordn pFq ÝÑ Line. Thus all quantum Hilbert spaces are one-dimensional and all propagations
are invertible. The tensor product of invertible theories is invertible, so (isomorphism classes of or
deformation classes of) invertible theories form an abelian group.
Example 2.9. Here is a simple example with n “ 1. Fix a smooth manifold M of any dimension
and a smooth complex line bundle L Ñ M with connection. We define a 1-dimensional field theory
whose set of fields FpXq on a 1-manifold X consists of a pair po, φq of an orientation o and a smooth
map φ : X Ñ M . Then to Y “ pt` a point with the positive orientation and φpptq “ m P M we
set F pY q “ Lm to be the fiber of the line bundle L Ñ M at m. To X “ r0, 1s with the usual
orientation and a map φ : r0, 1s Ñ M we assign the parallel transport F pXq : Lφp0q Ñ Lφp1q along
the path φ. The reader can easily work out the values of F on other manifolds. We can make
a family of such field theories by varying the line bundle L Ñ M and its connection. The path
components of this family of field theories are parametrized by the topological equivalence classes

10For a fully extended invertible field theory the value of F on any manifold of dimension ď n is invertible under

the symmetric monoidal product of the target. A theorem of the author and Constantin Teleman asserts that for
oriented theories if the number F pS n q is nonzero and the vector spaces F pS p ˆ S n´1´p q are one-dimensional, then
F is invertible.

<!-- page 10 -->
10

D. S. FREED

of line bundles L Ñ M (without connection.) In §4 and §5 we will learn that the set of path
components can be computed by stable homotopy theory.11
Example 2.10. Continuing with n “ 1 we now take the line bundle to be one of the fields, rather
than being pulled back from an external manifold. Thus let FpXq consist of an orientation o and
a complex line bundle L Ñ X with connection. The definition of the theory is similar to that
in Example 2.9. (The two theories are related: choose the universal line bundle L Ñ CP8 in
Example 2.9.) We continue this example in §2.8.
Example 2.11. Let n “ 2 and suppose F includes just an orientation. The line F pY q attached to
any closed 1-manifold Y is the trivial line C and the number attached to any closed 2-manifold X
is
(2.12)

λEulerpXq ,

the exponential of the Euler number with base some λ P Cˆ . This is a connected12 family of theories
with parameter space13 Cˆ . If we drop the orientation, then there is another theory not connected
2
to this family:14 the invariant of a closed surface X is p´1qw1 pXq , where w12 pXq is the characteristic
number associated to the square of the first Stiefel-Whitney class of the tangent bundle. (It is
nontrivial for the real projective plane, for example.)
Classical lagrangian field theories are invertible field theories: the invariant of a closed n-manifold
is the exponentiated action eiSpXq . Here ‘X’ includes a choice of background fields.
Example 2.13. Finite gauge theories provide a typical example of a classical topological theory in
any dimension n [DW, FQ]. Let G be a finite group and fix a cocycle which represents a cohomology
class λ P H n pBG; R{Zq. The fields FpXq are an orientation and a principal G-bundle P Ñ X.
(As principal G-bundles have automorphisms—deck transformations—the fields in this case form a
groupoid, or stack, rather than a space; see [FH] for one mathematical treatment.) Let λpP q P R{Z
be the pairing of the characteristic class λ of P in H n pX; R{Zq with the fundamental class of the
orientation. The invariant of the invertible field theory is e2πiλpP q . Note that no orientation is
required if the cocycle vanishes. This classical Dijkgraaf-Witten theory is invertible; the quantum
theory, obtained by a finite sum over bundles P , is typically not invertible. The case n “ 3 is a
special case of Chern-Simons theory (briefly described in Example 2.4 with gauge group T).
2.3. Relative field theories and anomalies
A field theory F as described in 2.1 might be termed absolute. Suppose α is an (absolute) pn`1qdimensional field theory. Then we can have an n-dimensional theory F which is defined relative
11The computation: rΣ1 M T SO ^M , Σ2 HZs – H 2 pM ; Zq. In all computations rX, Y s denotes pointed homotopy
1
`

classes of maps between the pointed spaces X, Y .
12As agrees with the computation rΣ2 M T SO , Σ3 HZs – H 3 pBSO ; Zq “ 0.
2
2
13
The computation of the parameter space: rΣ2 M T SO2 , Σ2 HC{Zs – H 2 pBSO2 ; C{Zq – C{Z. Aficionados may
relish the following. If we compose with Σ2 HC{Z Ñ Σ2 IC{Z, then the theories with parameter λ P Cˆ and ´λ P Cˆ
become isomorphic. Here IC{Z is the Brown-Comenetz dual of the sphere spectrum (§5.1.2). Note the numerical
invariants of 2-manifolds only depend on λ2 .
14We compute: rΣ2 M T O , Σ3 HZs – H 3 pBO ; Zq
r – Z{2Z. Here Z
r is the nontrivial local system on BO2 .
2
2

<!-- page 11 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

11

to α. In fact, it is more precise and important to realize that we need only the truncation τďn α
of α which remembers the values on manifolds of dimension ď n. Thus α need only be defined on
such manifolds in the first place. To a closed n-manifold X (with fields) the theory α assigns a
vector space αpXq. A relative theory F then assigns either a linear map
(2.14)

F pXq : C ÝÑ αpXq

or a linear map
(2.15)

F pXq : αpXq ÝÑ C.

In the first case we evaluate the map on 1 P C to obtain a vector in αpXq; in the second case
F pXq is a covector, an element of the dual vector space. There are similar statements for lower
dimensional manifolds. In the first case we write
(2.16)

F : 1 ÝÑ τďn α

and in the second
(2.17)

F : τďn α ÝÑ 1,

where 1 is the trivial theory.
If α is invertible, then F is termed an anomalous field theory with anomaly theory α.
We refer to [FT] for more explanations and for nontrivial examples. Here is an easy one, which
illustrates the relationship with boundary conditions15. Relative theories can be viewed as boundary
conditions in any dimension, an idea we take up in §7.
Example 2.18. Let n “ 0 and suppose α is a quantum mechanics theory (Figure 1) with Hilbert
space H attached to a point. Then a relative theory F : 1 Ñ τď0 α is determined by evaluating
on 0-manifolds, and it is enough to evaluate on a point with each orientation. Since αppt` q “ H
and αppt´ q “ H˚ we obtain a vector ΩF P H and a dual vector θF P H˚ . We can use the relative
theory F as a boundary condition for α, as illustrated in Figure 5.
2.4. Global symmetries and equivariant extensions
2.4.1. General discussion. Let G be a Lie group. For simplicity we discuss a non-extended field
theory (2.3). A global symmetry group may have an action on fields, and it also may have an
action on the category Vect. In the simplest cases those actions are trivial, and then G is a global
symmetry if the functor (2.3) lifts to a functor
(2.19)

F : Bordxn´1,ny pFq ÝÑ RepG

15Rather than a boundary ‘condition’, a relative theory can be viewed as a boundary ‘theory’.

<!-- page 12 -->
12

D. S. FREED

Figure 5. Quantum mechanics with boundary
into the category of representations of G. More plainly, the group G acts on the vector space F pY q
attached to each pn ´ 1q-manifold and the linear maps assigned to bordisms are G-invariant.
In this situation we might “gauge the symmetry” or, in less ambiguous terms, construct a Gequivariant extension of the theory. This means that there is a new field which is a G-connection;
if G is finite, then a G-connection is simply the underlying principal G-bundle. Whence the terminology: this is the gauge field. There is a new set of fields Fr which maps to the single field16 B∇ G
of a G-connection, and the fiber over the trivial G-connection is the old set F of fields. The
G-equivariant extension is a functor
(2.20)

Fr : Bordxn´1,ny pFrq ÝÑ Vect

whose restriction to the trivial G-connection is the original theory (2.19). This makes sense since
the trivial G-connection has the group G as its automorphism group.
Example 2.21. A typical example in field theory is a σ-model into a Riemannian manifold M
with a group G of isometries. The classical model makes sense in any spacetime dimension n. The
fields FpXq on an n-manifold consist of a metric g and a map φ : X Ñ M . In the G-equivariant
extension an element of FrpXq is a triple pg, Θ, φq where Θ is a connection on a principal G-bundle
P Ñ X and now φ is a G-equivariant map P Ñ M . The map to B∇ G sends pg, Θ, φq to Θ. If Θ is
the trivial G-connection then φ is equivalent to a map X Ñ M , and the deck transformations of
the trivial bundle X ˆ G Ñ X become the original G-action on the fields.
This example does not fit our simplified description, since the global symmetry group G does act
on the fields F, but there is a modification which covers this situation. In the quantum σ-model
we integrate over the field φ, and as there is no G-action on the remaining fields our description
applies as is.
2.4.2. Anomalies. There may be obstructions to constructing this G-equivariant extension: see [KT]
for a recent discussion and examples. One well-known example is the gauged WZW model [W5]. In
good cases there is only a single obstruction which can be interpreted as an anomaly. In these cases
the extension (2.20) does not exist but rather there is an invertible pn ` 1q-spacetime dimensional
theory α and an extension Fr which is a theory relative to α in the sense of §2.3.
Example 2.22. A standard example in n “ 4 is quantum chromodynamics. This theory has a
global SUN ˆ SUN symmetry (for N the number of flavors) which is anomalous.
We account for such anomalies in our proposals (§5.2).
16B G is most naturally a simplicial sheaf on the category of smooth manifolds [FH].
∇

<!-- page 13 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

13

2.4.3. Gauging antilinear symmetries. In quantum mechanics, due to Wigner’s theorem, the global
symmetry group G is equipped with a homomorphism17
(2.23)

φ : G Ñ µ2 “ t˘1u

which tracks whether a given symmetry acts linearly or antilinearly. Because states are lines in a
Hilbert space, rather than vectors, the group G acts projectively and there is an extension by the
group T of unit norm scalars. For theories tied to spacetime, as opposed to abstract theories, one
can also track whether or not symmetries reverse the orientation of time by another homomorphism
(2.24)

t : G Ñ µ2 .

In many situations t “ φ, but that needn’t be so in general. See [FM2, §§1,3] for a general
discussion.
We handle the extension by simply replacing G with the extended symmetry group. In doing so
we must take care that the group of scalars acts by scalar multiplication on all vector spaces in the
theory. We discuss time-reversal in §4.2.3. Here we explain how to gauge antilinear symmetries.
Consider a 1-spacetime dimensional theory F , so a quantum mechanical model as in Figure 1.
Let F ppt` q “ H and suppose G is a group of global symmetries as above. For simplicity, assume
G is a discrete group. As explained in §2.4.1 a G-equivariant extension Fr is a theory on manifolds
equipped with a principal G-bundle. Now H is the value of Fr on pt` equipped with the trivial
(which means trivialized) G-bundle. Consider the 1-manifold X “ r0, 1s with a (necessarily trivial,
but not trivialized) G-bundle, and suppose there are trivializations over the endpoints t0, 1u. Let
g P G be the parallel transport. Then Fr pX, gq : H Ñ H is the action of the global symmetry g.
However, if φpgq “ ´1—i.e., if g acts antilinearly—then this does not fit into (2.20) since the
category Vect has only linear maps. The way out is that φ defines a 2-dimensional invertible
anomaly theory α, and Fr is an anomalous theory with anomaly α, as in (2.17). The anomaly
theory assigns αpX, gq “ C, the complex conjugate to the trivial line of complex numbers, and then
the relative theory gives a linear map
(2.25)

Fr pX, gq : C b H ÝÑ H.

(A linear map C b V Ñ W is equivalent to an antilinear map V Ñ W . See [FT, (2.7)] for the
analog of (2.25) in an arbitrary relative theory.)
This discussion extends to higher dimensions. For extended field theories with values in a higher
category C we would need to explain how complex conjugation acts on C. In this paper we focus on invertible field theories, and we will implement this “antilinearity anomaly” using twisted
cohomology; see §5.1.4.
17Notation: µ “ tλ P C : λk “ 1u is the group of k th roots of unity.
k

<!-- page 14 -->
14

D. S. FREED

2.5. Unitarity
The formal setup of topological field theory described here is based on the Euclidean version of
quantum field theory. For Euclidean QFTs unitarity is expressed by both a reality condition and
a reflection-positivity condition. (A standard reference is [GJ]; see [Detal, p. 690] for a heuristic
explanation.) The unitarity condition for a fully extended topological theory (2.8) implements only
the reality condition. Namely, assuming the fields F include an orientation there is an involution
of Bordn pFq which reverses the orientation. Also, assuming that the target C is based on complex numbers, then it has an involution of complex conjugation. Unitarity is the statement that
F : Bordn pFq Ñ C is equivariant for these involutions. A formal justification from the path integral
stems from a basic fact: orientation reversal conjugates the Euclidean action.
In this paper we indicate how to implement unitarity for invertible topological field theories,
which are maps of spectra. The involutions are quite explicit, and unitarity amounts to a twisted
extension of the field theory to unoriented manifolds. One subtlety, which also occurs in noninvertible theories, is that for spin theories there are two notions of unitarity—the two different
Euclidean pin groups lead to two orientation-reversing involutions on spin manifolds.18
Because of the gaps in our understanding of unitarity, related to positivity and the choice of pin
group, we do not implement unitarity fully in our proposal in §5.2. We discuss unitarity further
in §§4.2.4, 4.2.5.

2.6. Topological field theories and the cobordism hypothesis
One can debate which theories deserve the moniker ‘topological’.19 We will say that a fully
extended theory (2.8) is topological if the fields F are topological, and the fields are topological
if they satisfy homotopy invariance: if ft : X 1 Ñ X is a homotopy of local diffeomorphisms of nmanifolds, then the pullbacks by f0 and f1 on fields are equal.20 Thus orientations, spin structures,
and G-bundles for discrete groups G are all examples of topological fields. Metrics, conformal
structures, and connections for positive dimensional Lie groups are all examples of non-topological
fields. On the other hand, flat G-connections are topological fields for any Lie group G.
Fully extended topological field theories are a topic of current interest in topology and other
parts of mathematics. The cobordism hypothesis, conjectured by Baez-Dolan [BD] and proved by
Hopkins-Lurie in dimensions ď 2 and in general by Lurie [L], is a powerful result which determines
the space of fully extended topological theories of a fixed type. The ‘type’ refers to both the fields F
and the target C. Thus one speaks of “oriented” theories or “framed” theories, which tells about
the topological fields in the theory. The theorem very roughly states that a theory F is determined
by its value F pptq on the 0-manifold consisting of a single point. One can intuitively think of this
as the value on an n-dimensional ball, and the idea is that any n-manifold is glued together from
balls, so that if the theory is fully local then its values can be reconstructed from those on a point.
18I thank Kevin Walker for emphasizing this point. I do not know a physical argument which distinguishes one of

them as the preferred choice, though in specific examples often one is preferred over the other.
19For example, with our definition classical Chern-Simons theory (Example 2.4) is not topological if the gauge
group is not discrete.
20Some fields, such as gauge fields, have internal symmetries and then the pullbacks are not strictly ‘equal’ but
rather are ‘equivalent’ or ‘homotopic’.

<!-- page 15 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

15

Furthermore, the value on a point is constrained to satisfy strong finiteness conditions. We refer
the reader to [L] and the expository account [F1].
Remark 2.26. If n “ 1 and we let the field F be an orientation, then a theory
(2.27)

F : Bordx0,1y pFq ÝÑ Vect

is determined by the vector space F ppt` q. The finiteness condition is that F ppt` q is finite dimensional. Of course, in usual quantum mechanics the quantum Hilbert space is typically infinite
dimensional; not so in this topological version.
The cobordism hypothesis tells not just about individual theories, but rather about the collection
of theories with fixed F and C. The first (easy) theorem is that this collection is an ordinary space
rather than a more abstract category. One should think of this space as parametrizing families of
theories, as in Example 2.9 and Example 2.11. Yet in the homotopical setting for field theories, it is
only the homotopy type of the space of theories which is well-defined; see §2.8 for more discussion.
The theorem in particular computes the set of path components of this space. Two theories lie
in the same path component if and only if they can be continuously connected. This matches
well the notion of a topological phase, and indeed the cobordism hypothesis is a powerful tool for
distinguishing topological phases of gapped theories. In this paper we focus on invertible theories,
which describe SRE phases, and the cobordism hypothesis reduces to a much easier statement, as
we explain in §2.7. We emphasize that the cobordism hypothesis—for invertible and non-invertible
theories—determines the complete homotopy type of the space of theories, not just the set of path
components.
2.7. Invertible topological theories and maps of spectra
We begin with an analogy. Let Crxs be the ring of polynomials in a variable x with complex
coefficients and let C be the ring of complex numbers. Define the ring homomorphism F : Crxs Ñ C
which sends a polynomial f pxq to its value f p0q at x “ 0. Let S Ă Crxs denote the subset of
polynomials with nonzero constant term. Note that S is closed under multiplication: if f1 , f2 P S,
then f1 f2 P S. Extend the homomorphism F to ratios of polynomials f {g where g P S. This is
for the simple reason that gp0q ­“ 0 if g P S, so f p0q{gp0q makes sense. We write S ´1 Crxs for the
ring of such ratios: we have inverted elements in S. This inversion construction is easy in this case
since Crxs is a commutative ring; it is trickier in the noncommutative case and in the categorical
context to which we now turn.
Suppose
(2.28)

F : Bordn pFq ÝÑ C

is an invertible topological field theory. By definition F takes values in the subset C ˆ Ă C consisting
of invertibles: invertible objects, invertible 1-morphisms, and invertible morphisms at all levels.
Now, as in the analogy, the fact that all values are invertible21 means that the theory factors
21In our analogy, only some values are invertible; here all are.

<!-- page 16 -->
16

D. S. FREED

through the symmetric monoidal p8, nq-category | Bordn pFq| obtained by adjoining inverses of all
morphisms:
(2.29)

Bordn pFq

F



Fr

| Bordn pFq|

/C
O
/ Cˆ

The map Fr encodes all information about the theory F .
The domain and codomain of Fr are each a higher category, in fact an 8-category, in which all
arrows are invertible. Such categories are called 8-groupoids. The basic idea is that an 8-groupoid
is equivalent to a space. This is easiest to see in the opposite direction: from a space S we can
extract an 8-groupoid πď8 S. Putting aside the ‘8’ for a moment, we extract an ordinary groupoid
called the fundamental groupoid πď1 S. Its objects are the points of S and a morphism x0 Ñ x1
between points x0 , x1 P S is a continuous path x : r0, 1s Ñ S from x0 to x1 up to homotopy. This
is a groupoid because paths are invertible: reverse time. The higher groupoids track homotopies of
paths, homotopies of homotopies, etc. The conclusion is that Fr may be considered as a continuous
map of spaces. This already brings us into the realm of topology. But more is true. The domain
and codomain of Fr are symmetric monoidal 8-groupoids, which induces more structure on the
corresponding spaces. (Recall that the monoidal product on the bordism category is disjoint union
and on the category C it is some sort of tensor product.) Namely, those spaces are infinite loop
spaces. So for each of the spaces S there exist a sequence of pointed spaces S0 “ S, S1 , S2 , . . .
such that the loop space of Sn is22 Sn´1 . Furthermore, the fact that F preserves the symmetric
monoidal structure—a field theory takes compositions to compositions and disjoint unions to tensor
products—implies that Fr is an infinite loop map. Such sequences of spaces are called spectra and
an infinite loop map gives rise to a map of spectra.
The bottom line is that the space of invertible field theories (with specified F, C) is23 a space
of maps in homotopy theory. We are interested in the abelian group of path components, which
houses an invariant of gapped topological phases, and that is the group of homotopy classes of maps
between spectra. Therefore, the computation of invertible field theories starts by recognizing the
spectra in the domain and codomain, which in turn depend on the choice of F and C. The domain
spectra, obtained from bordism multicategories, will be discussed in §4. We remark that to study
invertible field theories one does not need the cobordism hypothesis; the power of the latter is for
more general non-invertible topological field theories.
Remark 2.30. The set of path components here has a natural abelian group structure. In fact, a
spectrum X determines a collection tπn XunPZ of abelian groups, its homotopy groups. There is
additional information in the spectrum which binds these groups together, but a first heuristic is
that a spectrum is some topological version of a Z-graded abelian group.
Example 2.31. We continue with Example 2.11. In this case n “ 2 and the field F is an orientation. Now the target C is a 2-category, and we need to determine the spectrum corresponding to
22The Clinton question: here best to take ‘is’=‘is homeomorphic to’. See §4.1 for further discussion.
23The space is only determined up to homotopy equivalence, i.e., there is only a well-defined homotopy type.

<!-- page 17 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

17

the invertibles C ˆ . A typical choice is to take C to be the 2-category of complex linear categories.
This conforms to the usual picture that a 2-dimensional field theory assigns a complex number
to a closed 2-manifold, a complex vector space to a closed 1-manifold, and a complex linear category to a 0-manifold. In the invertible sub 2-groupoid C ˆ all of these are “1-dimensional”. This
means that the category is equivalent to Vect, the category of vector spaces; the vector spaces
are isomorphic to C; and the numbers we encounter are nonzero, so elements of Cˆ . When we
make the corresponding spectrum X, the fact that invertible categories are all equivalent implies24
π0 X “ 0. The fact that all invertible 1-morphisms are equivalent implies π1 X “ 0. Finally we
come to π2 X, which captures the 2-morphisms Cˆ . Here we get two different answers, depending
on whether we consider Cˆ to have the discrete topology or the continuous topology. In the discrete case we have π2 Xdiscrete – Cˆ . For the ordinary topology we use π0 Cˆ “ 0, π1 Cˆ – Z to
deduce π2 Xcontinuous “ 0, π3 Xcontinuous – Z. Higher homotopy groups of X vanish. Hence each
of Xdiscrete and Xcontinuous has only a single nonzero homotopy group. Such spectra are called
Eilenberg-MacLane spectra and are basic building blocks. The notation is
(2.32)

Xdiscrete » Σ2 HCˆ ,
Xcontinuous » Σ3 HZ.

The domain spectrum, to be explained in §4, is denoted Σ2 M T SO2 . Thus the two sets of path
components are:
(2.33)

rΣ2 M T SO2 , Σ2 HCˆ s – Cˆ ,
rΣ2 M T SO2 , Σ3 HZs “ 0.

Resuming Example 2.11 we see that the first of the computations in (2.33) distinguishes the Euler
theories, parametrized by the base λ P Cˆ of the exponential in (2.12). The discreteness in Xdiscrete
means that theories for distinct λ cannot be connected by a smooth path. In the usual topology
they can, and this explains the second computation in (2.33): the space of theories is connected.
Remark 2.34. For a general invertible bosonic theory in higher than 2-spacetime dimensions we
need more nonzero homotopy groups in the target spectrum. This surprise is discussed in §5.1.
Remark 2.35. The distinction between Xdiscrete and Xcontinuous is important and carries through
to more elaborate target spectra. The discrete target, based on Cˆ with the discrete topology, is
where we detect individual theories. The other target, based on Cˆ with its usual topology and
manifested as Z shifted up one degree, is where we detect deformation classes of theories. In the
next section we elaborate on the meaning of spaces of maps into targets such as Xcontinuous .
2.8. An illuminating example
We have alluded several times to the homotopical setting of the cobordism hypothesis and so
too the computations of deformation classes of invertible field theories. It often happens that the
geometric interpretation of a homotopical computation is subtle. There are many examples in
24We reprise the following argument in §5.1.2.

<!-- page 18 -->
18

D. S. FREED

topology, enumerative geometry, etc. We illustrate in our present context with a simple example.
In §6 we encounter a more sophisticated example of the same type in the classification of gapped
topological phases.
In Example 2.10 we discussed an invertible field theory in n “ 1 spacetime dimensions with fields
(2.36)

Fgeometric “ tpo, L, ∇qu

a triple consisting of an orientation, complex line bundle, and connection. Then there is an obvious
theory
(2.37)

Fgeometric : Bord1 pFgeometric q ÝÑ Line

with values in the category of complex lines. Namely, to a point pt` with positive orientation and a
line bundle L Ñ pt` we attach the line L. (A line bundle over a point is a single line.) If we reverse
the orientation of pt` , so consider pt´ , we take the dual line; if there are several points we form
the tensor product. If pL, ∇q Ñ r0, 1s is a line bundle with covariant derivative over the interval
with its usual orientation, the field theory assigns to it the parallel transport Fgeometric : L0 Ñ L1
from the fiber over the initial endpoint to the fiber at the terminal endpoint. If pL, ∇q Ñ S 1 is
a line bundle with connection over an oriented circle, then Fgeometric assigns to it the holonomy,
which is a number in Cˆ . This is a well-defined theory, and it is not “topological” according to our
definition, since the connection ∇ is not a homotopy-invariant field.
We can instead take the set of topological fields
(2.38)

Ftopological “ tpo, Lqu

consisting of an orientation and a complex line bundle but no connection. Now we ask to classify
topological field theories
(2.39)

Ftopological : Bord1 pFtopological q ÝÑ Line

As emphasized in Example 2.31 it is important to specify which topology we use on linear isomorphisms in the category Line: the discrete or continuous topology. Here we use the continuous
topology. The computation of equivalence classes of theories is
(2.40)

ˆ
2
2
ˆ
2
0
rΣ1 M T SO1 ^ BCˆ
` , Σ Zs “ rS ^ BC` , Σ Zs “ H pBC ; Zq – Z.

According to the discussions in §2.6 we conclude that the space of theories (2.39) is not connected,
but rather there is an integer invariant which distinguishes deformation classes of theories. There is
always a trivial theory—it sends every 0-manifold with fields to the trivial line C and every closed
1-manifold with fields to the number 1 P Cˆ —and it is in the deformation class of theories labeled
by the integer 0 in (2.40). So we are led to ask:

<!-- page 19 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

19

Question 2.41. What theory (2.39) is labeled by the integer k in (2.40)? Can we construct a
single example of such a theory?
It is clear what to do on 0-manifolds. For example,
(2.42)

Ftopological pL Ñ pt` q “ Lbk ,

the kth tensor power of the line L. In other words, we observe that the truncation τď0 Fgeometric
of the geometric theory above does not use the covariant derivative, and so we take Ftopological on
0-manifolds to be that theory to the k th power.
What do we do on 1-manifolds? The theory Fgeometric uses the connection on L Ñ r0, 1s to
define a definite linear map—parallel transport—and the connection on L Ñ S 1 to define a definite
number—the holonomy. But the now the fields (2.38) do not include a connection and we have no
apparent way to determine these linear maps and numbers.
There are several ways out, and they illuminate what is is being computed in (2.40) and in later
computations. Similar remarks apply to all topological theories and to the cobordism hypothesis.
The first comment, already made in Remark 2.6, is that a field theory gives invariants for
families of manifolds with fields parametrized by a smooth manifold S, not just for single manifolds.
So, for example, we can consider a family of points pt` parametrized by the 2-sphere S “ S 2
endowed with a complex line bundle L Ñ S 2 on the total space. Let d be the degree of this
line bundle. A field theory Ftopological returns another line bundle over S, and according to (2.42)
Ftopological of this family is the kth tensor power Lbk Ñ S, which has degree kd. The ratio kd{d “ k
of the degrees is the integer in (2.40), and it is detected by this 2-parameter family of points.
Similarly, we can consider a 1-parameter family of circles S ˆ S 1 Ñ S parametrized by S “ S 1 .
The fields are an orientation along the fibers of this map and a line bundle L Ñ S ˆ S 1 on the
total space, say of degree d. A field theory Ftopological returns a map S Ñ Cˆ and what the
computation (2.40) tells is that the winding number of this map around the origin in C is kd. In
other words, the computation (2.40) determines homotopical information in any particular field
theory in the deformation class, and that information may need to be measured in families.
This still does not construct a particular theory (2.39); it only constrains any such. To construct a
theory we need to make some choices—which in itself is not surprising—but what may be surprising
is that we can choose to change the domain Bord1 pFtopological q or the codomain Line in order to
construct a particular theory. What’s more, we may go outside the realm of topological field theories
and use more general field theories.
For instance we can replace Ftopological with Fgeometric . There is an obvious map Fgeometric Ñ
Ftopological which forgets the connection ∇, and the important point is that the fibers of this map
are contractible. That is, the space of covariant derivatives ∇ on a fixed line bundle L Ñ X is a
contractible space. (In fact, it is an infinite dimensional affine space.) If we make this substitution,
bk
where Fgeometric is defined
then we know how to construct a theory. Namely, we take Fgeometric
after (2.37). Another choice would be to fix a smooth model of the classifying space for line
bundles, say by fixing a complex Hilbert space H and taking the classifying space to be the infinite
dimensional projective space PpHq. Furthermore, we fix a smooth line bundle H Ñ PpHq with
covariant derivative. Augment the topological fields (2.38) by a contractible choice: a classifying

<!-- page 20 -->
20

D. S. FREED

map γ : X Ñ PpHq for each line bundle L Ñ X. Again there is a map from triples po, L, γq to po, Lq
and the fibers are contractible. With these choices and replacements it is easy to construct a
particular theory using parallel transport in the bundle H bk Ñ PpHq, pulled back via the classifying
map γ.
Remark 2.43. A different possibility is to keep the domain fields as is (2.38) but change the target
category Line. We can replace it by the 2-category of Z-gerbes; the automorphisms of any object
comprise the category of Z-torsors, and the automorphism group of any automorphism is Z. This
is the target of a 2-dimensional field theory with fields (2.38). This theory assigns to a line bundle
L Ñ X over a closed oriented surface its degree, which is an integer. The information on lower
dimensional manifolds can be used to compute this degree locally; see [F2].
Another insight can be gleaned from (2.29), which we unwrap:
(2.44)

Fr

Bordn pFq ÝÑ | Bordn pFq| ÝÝÑ C ˆ

Let double vertical bars around a higher category denote its geometric realization, which is a
topological space. The process of geometric realization inverts all arrows in the category, so factors
through the single bar construction. In these terms what we calculate in (2.40) is the group of
homotopy classes of maps of spaces
(2.45)

} Bordn pFq} ÝÑ }C ˆ }

whereas a particular field theory Ftopological is a map of categories
(2.46)

Bordn pFq ÝÑ C ˆ

The functor ‘geometric realization’ takes a map of categories (2.46) to a map of spaces (2.45).
Furthermore, Grothendieck’s homotopy hypothesis asserts that the functor of geometric realization
is an equivalence between higher groupoids and spaces, so we expect to be able to invert
(2.47)

C ˆ ÞÝÑ }C ˆ }

since C ˆ is a higher groupoid. Such an inversion would let us pass from a map of spaces (2.45)
to a field theory (2.46), but in practice we cannot explicitly construct an inverse without making
choices. In our example, C ˆ “ Line is the groupoid of complex lines and its geometric realization
as a space is |C ˆ | » CP8 . We need to identify that geometric realization with an explicit model
of CP8 to get back to one-dimensional vector spaces.
In summary, the most relevant interpretation we can offer of the computation (2.40) for this
paper is our first: it computes homotopy classes of a class of theories obtained by augmenting
the topological fields with geometric fields which constitute a contractible choice. This resonates
with the construction of quantum Chern-Simons theory [W1], for example, in which a Riemannian
metric is introduced to evaluate the path integral.
Remark 2.48. The complication here arises since we seek to interpret nontorsion elements of the
group of deformation classes, computed in (2.40). Torsion elements, such as in footnote 14, lift to
maps into Cˆ
discrete shifted down a degree, and so are realized by definite topological theories.

<!-- page 21 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

21

3. The long-range effective topological field theory
In this section we begin to apply the generalities about invertible topological field theories to
short-range entangled phases. We start in §3.1 with some general remarks about scaling, energy
gaps, and effective theories. In §3.2 we give general arguments about short-range entangled (SRE)
phases in gapped condensed matter systems. In the last subsection §3.3 we bring in local symmetries, including time-reversal, and in particular define symmetry protected topological (SPT)
phases in terms of invertible topological field theories.
3.1. Low energy, long time
In classical nonrelativistic physics there are three basic dimensions:25 length (L), time (T ), and
mass (M ). (For mathematical discussions of dimensions and units, see [Ta, §2.1], [DF, §2.1].) The
dimensions of other physical quantities can be expressed in terms of these. For example, energy
has dimension
rEs “

(3.1)

M L2
.
T2

Universal physical constants also have dimensions, for example Planck’s constant ~ and the speed
of light c:
(3.2)

r~s “

M L2
,
T

rcs “

L
.
T

The constant ~ is present in any quantum system, the constant c in any relativistic system, and
both in a relativistic quantum system. These constants allow us to convert between dimensions,
often silently by assuming units in which ~ “ 1 and c “ 1. Thus in a quantum system we have
(3.3)

rEs “

1
T

(assuming ~).

This dimensional analysis suggests that the low energy behavior of a quantum system is reflected
in its long time behavior. In a relativistic quantum system we have L “ T using c, and so
(3.4)

rEs “ M “

1
1
“
T
L

(assuming ~, c),

thereby relating low energy to low mass and long time to large distance.
Consider, then, a Riemannian manifold M with Riemannian metric g. Let ∆ be the Laplace
operator on differential forms, which we take as the Hamiltonian of a nonrelativistic quantum
system.26 The eigenvalues of ∆ are energies, so the low energy behavior involves the low lying
eigenvalues. Equivalently, we can consider the long time evolution, which is eit∆ for t large. Nonzero
25There are others, such as temperature and electric current, but they do not play a role in this discussion.
26The dimensionally correct expression is H “ p~2 {mq∆, where m “ mass; instead, we set ~ “ 1 and m “ 1.

<!-- page 22 -->
22

D. S. FREED

eigenvalues lead to oscillations, which tend to cancel out if t is large, and once more we are led
to the low lying spectrum.27 Now we encounter a fundamental dichotomy. If 0 is an isolated
point of the spectrum, then for t large the kernel of ∆ dominates. However, if 0 is not an isolated
point of the spectrum, then the low lying continuous spectrum mixes inextricably with the kernel.
Therefore, we isolate the kernel at long time only if there is a gap in the spectrum above 0. This
always happens if M is compact. In that case the Hodge and de Rham theorems combine to prove
that the kernel of the Laplace operator ∆ on differential forms has topological significance: the
dimension of the kernel of ∆ on Ωq pM q is the q th Betti number of M .
A gapped quantum system is one in which 0 is an isolated point of the spectrum of the Hamiltonian H. By the dimensional analysis above, this energy gap is equivalent to a mass gap in a
relativistic quantum system. One is interested in the long time (and large distance) behavior of
a system since that is what we can observe, and often that behavior is described by an effective
system. We use the general term ‘long-range’ for either ‘long time’ or ‘large distance’. For example, quantum field theories at large distance are often well-approximated by another quantum field
theory, and the approximating theory contains more than the vacuum state if there is no mass gap;
see [W2, §2.5] for a discussion. It is sometimes said that if there is a mass gap then the low energy
theory is trivial, but there is a more nuanced truism:28
(3.5) The low energy behavior of a gapped system is approximated by a topological field theory.
For this to make sense, we need to study the theory on arbitrary spacetimes, so couple to background
gravity. That can be done for many field theories. For example, 4-dimensional Yang-Mills theory
makes sense on arbitrary Riemannian manifolds, and conjecturally there is a mass gap, so one
should obtain a 4-dimensional topological field in the low energy limit. (Here n “ 4 is the spacetime
dimension.)
Remark 3.6. The N “ 1 supersymmetric Yang-Mills theory also has a conjectural mass gap, and
presumably the low energy effective topological theory is more interesting in that case.
We turn to condensed matter systems, which we treat very heuristically. We assume the quantum
Hilbert space H is the tensor product over a set S of sites of finite dimensional Hilbert spaces
(3.7)

H“

â

Hs

sPS

and we may assume Hs “ V is a fixed Hilbert space independent of the site s; the sites are initially
arranged in a regular pattern, such as a lattice; and the Hamiltonian H is local in that it is a sum
(3.8)

H“

ÿ

Hs ,

sPS

˘
˘
`Â
`Â
1
where Hs “ T b id relative to a decomposition H “
s2 Hs2 in which s runs over
s1 Hs1 b
sites in a small vicinity of s and the operator T is independent of s. The sites S are located in a
27In Riemannian geometry the heat operator e´t∆ is more familiar and leads to the same conclusion.
28I do not know where this idea originated; one older reference is [W3, p. 405].

<!-- page 23 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

23

background space Y of dimension d. (We emphasize that d is the dimension of space and d ` 1 the
dimension of spacetime.) This is a nonrelativistic system, and Galilean boosts have been broken by
the sites, which don’t move in time. Thus time is completely separate from the geometry of space.
Initially Y typically lies in flat Euclidean space, and coupling to gravity in this context means
that the system can be studied on any curved d-dimensional manifold Y . Fix a compact Y and
imagine that the finite set of sites S becomes more and more dense. With no pretense of precision
we assume that the system is gapped in that 0 is the lowest eigenvalue of H and the spectrum
of H has a fixed size gap above 0 which persists in the limit that S becomes dense. Furthermore,
we assume the kernel of H stabilizes to a finite dimensional vector space F pY q. In this situation
we would like to assert (3.5): there is an effective d-space dimensional topological field theory F
which approximates the low energy/long time behavior of the system. The vector spaces F pY q
are part of that theory. The deformation class of the theory F is then a topological invariant of
the original system, much the same way that the Betti numbers are topological invariants of the
Laplace operator on a compact Riemannian manifold.
Remark 3.9. Some parts of the gluing laws of a topological field theory are clearly going to hold. For
example, if Y “ Y 1 >Y 2 is a disjoint union, and we envision a system as described after Remark 3.6,
then the quantum Hilbert space (3.7) of Y is the tensor product of those on Y 1 and Y 2 and the
Hamiltonian (3.8) decomposes accordingly. Therefore, so too does the kernel F pY q. One expects a
more subtle decomposition emerges from a continuum limit process.
Remark 3.10. This procedure does not obviously give numerical invariants on all compact pd ` 1qdimensional manifolds. We expect invariants corresponding to time evolution, and since the field
theory is defined for compact manifolds we must take circular time S 1 . When we return to the
initial time the manifold and its fields can undergo a symmetry, so the manifold we obtain is a
fiber bundle X d`1 Ñ S 1 . We do expect invariants for these mapping cylinders. This kind of
impoverished pd ` 1q-dimensional field theory, perhaps with variations, goes under many names: a
pd ` ǫq-dimensional theory, a theory of H-type, . . . . Many, in fact most, of the effective theories
of H-type that we encounter do extend to full pd ` 1q-dimensional theories, and it may be that
additional considerations in the microscopic theory can imply that property of the long-range
topological theory. Even more is possible. A 1-parameter family of pd ` 1q-manifolds parametrized
by S is the total space of a fiber bundle M d`2 Ñ S 1 , and the theory gives a map S 1 Ñ Cˆ . Its
winding number is an integer invariant associated to M . It may happen that these integer invariants
are defined for arbitrary closed pd ` 2q-manifolds, not just mapping cylinders. This would impose
a more severe constraint on the low energy effective theory, as we illustrate in §6.3. Geometrically,
an H-type theory gives invariants for manifolds equipped with a rank d bundle stably equivalent
to the tangent bundle.
Remark 3.11. If one starts with a gapped quantum field theory, at first glance one can imagine its
low energy behavior giving rise to a specific topological field theory, or at least a contractible space of
theories depending on some mild choices in the approximation. For a condensed matter system there
seem to be more choices as one must, in addition to any cutoffs, take a continuum limit. This leads to
the expectation that we obtain a space of theories—again presumably contractible, but hopefully at
least connected—and makes it more plausible that one could encounter the phenomenon highlighted
in §2.8. Indeed, we will in §6.3.

<!-- page 24 -->
24

D. S. FREED

3.2. Short-range entanglement hypothesis and its consequences
We make explicit the assumptions beyond (3.5) which underlie our proposal in §5.2. The most
drastic of these is invertibility, which is an expression of short-range entanglement; see (6) below.
(1) We assume that the low energy effective topological theory F is fully extended, in the sense
discussed after Remark 2.7. This is a strong form of locality, and it seems reasonable since
the continuum limit theory is obtained from local discrete systems, as in (3.7) and (3.8).
To define the extended theory we must specify what sorts of (higher categorical) invariants
F computes on low dimensional manifolds. In other words, we must specify the target C
for the field theory; see (2.8). Since we restrict to invertible theories, we need only specify
a spectrum. That is one of the key choices to be made; see §5.1 for a full discussion.
(2) We assume that F is unitary, since microscopic condensed matter systems are typically
unitary.
(3) One important consideration which affects the choice of C is the topology on the space
of theories, as already mentioned and illustrated in Remark 2.7, Example 2.11, and Example 2.31. To the extent that the theory F has numerical invariants of closed pd ` 1qmanifolds, they lie in C; the invariants of closed d-manifolds are C-vector spaces. In both
cases we use the usual topology on C to allow the theory F to deform by continuously
varying the numerical invariants, the linear maps between vector spaces, etc. Two microscopic gapped systems related by a continuous deformation are considered to define
the same topological phase, and they should give rise to effective topological field theories
which are deformation equivalent. On the other hand, we also consider anomaly theories α, which can arise when gauging an anomalous global symmetry. (See §2.3 and the
text before Example 2.22.) In that case we do not allow continuous deformations of the
anomaly theory: anomalous theories relative to distinct anomaly theories should not be
viewed as the same topological phase. Thus, for the classification of anomalies we take
the discrete topology on C.29
(4) Another important choice is of the background fields F in the low energy effective topological theory (2.8). We expect only topological fields. Our choice here is based on limited
experience, and is more or less a guess. Naively one may think a lattice system on a
manifold induces a framing, but we hope there is rotational invariance which allows us
to formulate the theory on more general manifolds. As orientations are typically used to
define local Hamiltonians (3.8), we require invariance only under rotations connected to
the identity. Therefore, for purely bosonic systems we choose F to include an orientation,
and if the theory includes fermions then we augment this to a spin structure. In the
fermionic case one can think that the coupling of such a system to background gravity
involves spacetime spinor fields, whence the necessity of a spin structure. There is an
additional field—a background principal bundle—if we gauge a global symmetry, as we
elaborate below in §3.3.
29I thank Xiao-Gang Wen for explaining this point to me.

<!-- page 25 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

25

(5) As already discussed in Remark 3.10 we take F to be a theory defined in d space dimensions
which defines complex numbers only on special closed pd ` 1q-manifolds. In Remark 3.10
we explain then that integers are obtained for special closed pd ` 2q-manifolds. ‘Special’
in both cases means the manifold is equipped with a rank d vector bundle and a stable
isomorphism with the tangent bundle.
(6) Finally, we assume F is invertible, which is the hypothesis of no long-range entanglement,
referred to as short-range entanglement. The macroscopic definition given in some literature (for example [VS]) is that dim F pY q “ 1 for all closed d-manifolds. This is precisely
invertibility at this level—dimension d—of the field theory. It is not too much of a stretch
to extrapolate that to invertibility at all levels. The theorem mentioned in footnote 10
supports this extrapolation.
3.3. Symmetries and SPT phases
Suppose that a Lie group G acts as global symmetries of a condensed matter system. This can
include internal symmetries which act on the local Hilbert space Hs “ V in (3.7). It can also
include time-reversal symmetry, since we consider time as external to space and so time-reversal
symmetries fix the points of space. We do not, however, consider symmetries which move points of
space since we want to consider the theory on an arbitrary d-manifold Y . For example, this rules
out rotation and reflection symmetries of theories on Euclidean space.
Just as we study the condensed matter system on arbitrary space manifolds Y to explore its low
energy behavior (coupling to gravity), to explore the effect of the global symmetry we attempt to
construct an equivariant extension, as in §2.4. Recall that this means that we augment the set of
fields to include a G-connection on a principal G-bundle. As mentioned after Example 2.21 there
may be obstructions to constructing a G-invariant extension. We assume that any obstruction,
if it exists, can be expressed as an anomaly theory in one higher dimension. Passing to the low
energy approximation, we stipulate that there is a topological anomaly theory α and the original
long-range effective theory F is extended to be an anomalous theory Fr with anomaly α. The
topological theories α and Fr have a principal G-bundle as an additional background field—the
choice of connection does not appear in the classification of effective topological theories. (See the
discussion in §2.8.) Also, both theories are truncated only on manifolds of dimension ď d, as in
§3.2(4). As for any anomaly theory, α is invertible. We make the hypothesis that for short-range
entanglement the G-equivariant long-range topological theory Fr is also invertible. When we come
to classify anomalies in §5.2 we use the considerations of §3.2(2) to guide the choice of topology on
the space of anomaly theories.
In summary, then, we will assume one of two cases. Either the original long-range effective
theory F extends to a G-equivariant theory Fr, or there is an anomaly α and there is an anomalous
G-equivariant extension Fr. In both cases the original set of fields F in F is augmented to
(3.12)

Fr “ F Y tG-bundleu.

There is an embedding F Ñ Fr which chooses the trivial G-bundle. Restriction along this map
allows us to study the effective theory Fr ignoring the symmetry G. This restriction is simply the

<!-- page 26 -->
26

D. S. FREED

theory F . A topological phase is said to be symmetry protected if this restriction F is the trivial
theory. (Notice that the anomaly theory α is trivialized under this restriction since the original
long-range effective theory F is an absolute theory—it has no anomaly.)

4. Bordism and homotopy theory
In this section we recall the Madsen-Tillmann spectra which appear in the study of invertible
topological field theories. In the notation of §2.7 the simplest of these is the spectrum30
Σn M T On » | Bordn |

(4.1)

which is the geometric realization of the bordism category, obtained by inverting all morphisms.
The Madsen-Tillmann spectra were introduced in [MT] and versions of (4.1)—including nontrivial
fields F—are proved in [MaWe], [GMTW], [Ay]. Those theorems treat the geometric realization
of a topological 1-category, whereas the right hand side of (4.1) is the geometric realization of an
p8, nq-category. The p8, nq version is stated in [L, §2.5] and the techniques to prove it are most
likely contained in the cited references. We proceed to use the p8, nq statement as the basis for our
proposal in §5.2. We give a brief introduction in §4.1; the class notes [F3] contain much more detail.
In §4.2 we note the modifications to include symmetry and the modifications for theories of H-type
discussed in Remark 3.10. We also explain orientation-reversal and unitarity in this context.
4.1. Madsen-Tillmann spectra
Pontrjagin studied smooth maps
(4.2)

f : S n`q Ñ S q

by choosing a regular value p P S q and focusing on the inverse image M “ f ´1 ppq Ă S n`q ,
an n-dimensional closed submanifold. It carries an additional topological structure. Namely, for
all m P M the differential
(4.3)

dfm : Tm S n`q {Tm M Ñ Tp S q

is an isomorphism from the normal space to M at m to a fixed vector space, the tangent space
of S q at p. This is a framing of the normal bundle. We emphasize that it is a normal, rather
than tangential, framing. The submanifolds for different regular values and homotopic maps are
all framed bordant in the sense that for any two M0 , M1 there exists a compact pn ` 1q-dimensional
manifold N Ă r0, 1s ˆ S n`q with boundary t0u ˆ M0 > t1u ˆ M1 ; the manifold N carries a normal
30The ‘Σn ’ denotes a shift, or suspension, and is present because of an unfortunate indexing convention. What

should appear on the left hand side of (4.1) is the 0-space of the Madsen-Tillmann spectrum, which is standardly
denoted ‘Ω8 Σn M T On ’, but we blur the notation.

<!-- page 27 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

27

framing which agrees with that of M0 and M1 on the boundary. This is the fundamental connection
between bordism and homotopy theory [Mi, §7], which was elaborated and given computational
punch by Thom in his PhD thesis [Th]. If we seek to understand not n-dimensional closed submanifolds of a fixed sphere S n`q but rather n-dimensional abstract closed framed manifolds, then
a basic theorem of Whitney tells that every abstract manifold embeds in some sphere, so it suffices
to take q large. We increase q by suspending (4.2); large q is realized by iterated suspension. The
suspension of (4.2) is a map between the suspension of the domain and codomain spheres, and
the suspension of a sphere is a sphere of dimension one greater. A sequence of spaces related by
suspension is a spectrum, and Thom introduced special spectra to compute bordism groups. The
manifolds classified by these bordism groups may carry geometric structures (framings, orientations,
spin structures, . . . ) on their stable normal bundle.
The bordism question for invertible topological field theory differs in a fundamental way. A field
theory has a definite spacetime dimension n, and the geometric structures live on the n-dimensional
tangent bundle. So whereas Thom’s theory is stable normal, the Madsen-Tillmann spectra which
arise encode unstable31 tangential bordism. We sketch the basic example M T On and indicate the
modifications M T SOn for oriented n-manifolds and M T Spinn for spin n-manifolds.
Formally, a prespectrum T‚ is a sequence tTq uqPZ of pointed spaces and pointed maps sq : ΣTq Ñ
Tq`1 , where ‘Σ’ denotes suspension. It is a spectrum if the induced maps tq : Tq Ñ ΩTq`1 are
homeomorphisms, where ‘Ω’ denotes based loops. Any prespectrum has an associated spectrum,
and furthermore it suffices to define Tq for q ě q0 for some q0 P Z. The simplest example, indicated
above, is the sphere prespectrum with Tq “ S q . We now construct a prespectrum whose associated
spectrum is M T On for a fixed n P Zą0 .
Let Grn pW q be the Grassmannian of n-dimensional subspaces of the real vector space W . A
point of rV s P Grn pW q is an n-dimensional subspace V Ă W . The Grassmannian is a smooth
manifold, and there is a tautological rank n universal subbundle
(4.4)

S ÝÑ Grn pW q

whose fiber at rV s is V . Even better, there is a tautological exact sequence
(4.5)

0 ÝÑ S ÝÑ W ÝÑ Q ÝÑ 0

of vector bundles; the fiber of the universal quotient bundle Q Ñ Grn pW q at V P Grn pW q is the
quotient vector space W {V , and the vector bundle W Ñ Grn pW q has constant fiber W . For any
integer q ą 0 we define the space Tn`q to be the Thom space of the universal quotient bundle
(4.6)

Qpqq ÝÑ Grn pRn`q q.

The Thom space is obtained from the manifold Qpqq by introducing an inner product on the vector
bundle (4.6) and collapsing the subspace of all vectors of norm ě R to a point, where R ą 0 is any
31M T spectra are still part of stable homotopy theory—they are spectra—but the dimension is fixed, not stabilized.

<!-- page 28 -->
28

D. S. FREED

real number, as indicated in Figure 6. The structure map sn`q is obtained by applying the Thom
space construction to the map
R ‘ Qpqq

/ Qpq ` 1q




/ Grn pRn`q`1 q

(4.7)
Grn pRn`q q

The bottom arrow takes a subspace V Ă Rn`q and regards it as a subspace of Rn`q`1 all of whose
vectors have first coordinate zero.

Figure 6. The Thom space of a vector bundle V Ñ M
More useful to us is the nth suspension Σn M T On , which is represented by the shift of this
prespectrum with pΣn T qq “ Tn`q . A map S m Ñ Σn M T On is represented by a pointed map
S m`q Ñ Tn`q for some q large, so a map f : S m`q Ñ Qpqq which sends the basepoint of S m`q to
a vector of norm ě R. Suppose the map is transverse to the zero section Z Ă Qpqq. Then the
pullback M :“ f ´1 pZq Ă S m`q is a submanifold of dimension m. Its normal bundle is identified
via df with the normal bundle to Z in Qpqq, which in turn is identified with the vector bundle (4.6).
But because of the degrees it is more natural to consider the virtual bundle Qpqq ´ Rn`q « ´Spnq
whose pullback is then identified with the negative of the tangent bundle to M , stabilized to have
rank n. (Recall that Spnq Ñ Grn pRn`q q is the universal subbundle (4.4).) The choice of embedding
into a sphere S m`q disappears in the limit q Ñ 8 and, as in Thom’s bordism theory, we obtain
abstract manifolds rather than embedded ones.
Remark 4.8. The pullback of Spnq Ñ Grn pRn`q q to M is a rank n bundle which is equipped with
a stable isomorphism to the tangent bundle T M .
More generally, for any smooth manifold S, a map S ˆ S m Ñ Σn M T On leads to a smooth proper
map π : N Ñ S with dim N ´ dim S “ m and with a rank n vector bundle V Ñ N equipped with
a stable isomorphism with T N ´ π ˚ T S. The Galatius-Madsen-Tillmann-Weiss theorem [GMTW]
asserts that the spectrum Σn M T On classifies a bordism theory of proper fiber bundles, rather than
arbitrary proper maps π.
Remark 4.9. There is a sequence of maps
(4.10)

Σ1 M T O1 ÝÑ Σ2 M T O2 ÝÑ Σ3 M T O3 ÝÑ ¨ ¨ ¨

<!-- page 29 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

29

whose “limit” is the Thom spectrum M O which classifies unoriented manifolds. In this precise
sense the Madsen-Tillmann spectra approximate Thom spectra.
To construct the Madsen-Tillmann spectra M T SOn (M T Spinn ) use the Grassmannian of oriented (spin) subspaces.
Quite generally, a map S Ñ T of spectra represents a T -cohomology class on S. The T cohomology of a Madsen-Tillmann spectrum S “ Σn M T SOn is isomorphic to the T -cohomology
of the space BSOn by the Thom isomorphism. For example, if T “ Σq HZ then there is a Thom
isomorphism
(4.11)

rΣn M T SOn , Σq HZs – H q pBSOn ; Zq.

There is an orientation condition which is satisfied here because we consider the Madsen-Tillmann
spectrum with group SOn . If instead we use On , then we obtain cohomology with twisted coefficients:
(4.12)

rΣn M T On , Σq HZs – H q pBOn ; Zw q,

where Zw Ñ BOn is the nontrivial local system with holonomy ´1 around the nontrivial loop
in BOn . The general form of the twisted Thom isomorphism is
(4.13)

rΣn M T On , Σq T s – T τ `q pBOn q,

where τ is the twisting of T -cohomology defined by the virtual vector bundle Rn ´ Spnq Ñ BOn .
There are similar statements for the groups SOn and Spinn . We refer to [ABGHR] and references
therein for a modern treatment of twisted cohomology, orientations, and the Thom isomorphism.
4.2. Variations
4.2.1. Global symmetry groups. Let G be a Lie group. As explained in §3.3 the long-range effective topological theory approximating a condensed matter system with global symmetry group G
includes a G-bundle among its background fields; see (3.12). Such a bundle can be obtained from a
universal G-bundle EG Ñ BG by pullback. To incorporate the bundle into the Madsen-Tillmann
spectrum M T On replace (4.6) with the pullback bundle
(4.14)

Qpqq ÝÑ Grn pRn`q q ˆ BG

over the Cartesian product. A map f : S m`q Ñ Qpqq which is transverse to the zero section of (4.14)
gives a manifold M Ă S m`q and a G-bundle P Ñ S m`q . The structure maps defined from (4.7)
extend to incorporate the BG factor. The spectrum so obtained is denoted
(4.15)

M T On ^ BG`

The wedge, pronounced “smash”, is the appropriate product for pointed spaces; the ‘`’ denotes a
disjoint basepoint.32 Of course, there are similar spectra to (4.15) for oriented and spin manifolds.
32The classifying space BG does have a basepoint which represents the trivial G-bundle, and we use it at the end

of §5.2 to implement the embedding described after (3.12) in the discussion of SPT phases. The basepoint of BG is
ignored in the construction of BG` “ BG > pt, the disjoint union of BG and a point.

<!-- page 30 -->
30

D. S. FREED

4.2.2. Theories of H-type. In a d-space dimensional theory we obtain numerical invariants only for
pd ` 1q-manifolds which are essentially products: time is not mixed with space; see Remark 3.10. In
terms of (2.8) an “H-type” theory is defined on the subcategory of Bordd`1 pFq which only contains
top dimensional bordisms which are fibered over 1-manifolds:
(4.16)

F : Bordd pFq ÝÑ C

An invertible theory of that form, if F is empty, is a map out of the spectrum Σd M T Od . In terms
of the explicit prespectrum described in §4.1, the q th -space of Σd M T Od is the Thom space of
(4.17)

Qpqq ÝÑ Grd pRd`q q.

We explained in the paragraph after (4.7) that manifolds in the usual pd` 1q-spacetime dimensional
theory have tangent bundles stabilized to rank d ` 1. Here in the space theory they are stabilized
to rank d. So to get a bundle of rank d ` 1 we simply add an extra rank one trivial bundle R; the
fiber represent time, which is visibly a product and does not mix with space.
4.2.3. Time-reversal symmetries. The general picture of symmetries in quantum mechanics (§2.4.3)
distinguishes time-preserving vs. time-reversing (2.24) from linear vs. antilinear (2.23). Often, of
course, they are equal dichotomies. In that sense an accounting of antilinearity suffices to account
for time-reversal. But more to the point, as we consider theories of H-type (§4.2.2) in which there
is no explicit time, there is no need to track (2.24) other than through antilinearity.
4.2.4. Orientation-reversal and unitarity. This is to implement the unitarity (§2.5). The geometric
realization of the oriented bordism category Bordn pFq is Σn M T SOn , if F consists of an orientation.
Thus orientation-reversal induces an involution on Σn M T SOn . Introducing the notation M V for
the Thom spectrum of the virtual vector bundle V Ñ M , we can summarize (4.7) as
(4.18)

Σn M T SOn “ BSOn

Rn ´Spnq

,

where Spnq Ñ BSOn is the universal rank n bundle. Orientation-reversal on rank n bundles is
represented as the deck transformation of the double cover
(4.19)

BSOn ÝÑ BOn .

There is an induced involution on the Thom spectrum (4.18).
In a unitary theory orientation-reversal maps to complex conjugation. Complex conjugation
on Cˆ corresponds to the involution
(4.20)

z ÞÝÑ ´z̄

on C{Z via exponentiation. Let HCˆ be the target of an invertible unitary theory Σn M T SOn Ñ
Σn HCˆ . This represents a twisted cohomology class of Σn M T On . The twisted Thom isomorphism
theorem (4.12) identifies this twisted cohomology group with
(4.21)

Ą
H n pBOn ; C{Zq,

<!-- page 31 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

31

where the coefficients are twisted by the complex conjugation action (no sign). Note the short
exact sequence
(4.22)

0 ÝÑ Z ÝÑ C ÝÑ C{Z ÝÑ 0,

which is equivariant for the p´1q-action on Z and the action (4.20) on the other two groups. So
when we map to HZ or IZ we use the p´1q-action in place of the action (4.20) on HC{Z and IC{Z.
We remark that the twisted Thom isomorphism involves more complicated twistings for IC{Z.
An analogous construction works if we replace SOn with Spinn and On with Pinn . However,
there are two choices for Pinn . If we view Pinn as embedded in the real Clifford algebra Cliff n ,
then the choices depend on the sign in the relation γi2 “ ˘1 which defines Cliff n ; see [ABS]. So it
seems there are two distinct notions of unitarity for spin theories. We will simply write ‘Pin’ and
not investigate the distinction further in this paper.
We now sketch precisely how we implement the p´1q-involution on spectra.
Construction 4.23 (p´1q-action on spectra). Let H Ñ RP8 denote the real Hopf line bundle.
The Thom spectrum pRP8 qH´R of the reduced Hopf bundle is a bundle, or sheaf, of spectra
over RP8 whose typical fiber is the sphere spectrum. The holonomy around the nontrivial loop
acts on the homotopy groups π‚ S 0 of the sphere as multiplication by ´1. In other words, for each q
the homotopy groups make a local system over RP8 with fiber πq S 0 and holonomy ´1. Any other
spectrum T is a module over S 0 and there is an induced bundle of spectra over RP8 with fiber T ;
the holonomy acts on π‚ T as multiplication by ´1.
See [ABGHR] for a precise definitions, statements, and proofs of these assertions about bundles
of spectra and the twisted Thom isomorphism.
4.2.5. Interlude on unitarity. See §2.5 for a general discussion of unitarity, and §4.2.4 for its
implementation in invertible theories. Here we compute and interpret groups of low-dimensional
oriented unitary theories, using (4.21).
The group of n “ 1 spacetime dimensional oriented theories with Eilenberg-MacLane target is
(4.24)

rΣ1 M T SO1 , Σ1 HC{Zs – H 1 pBSO1 ; C{Zq “ 0;

there is only the trivial theory F which assigns the trivial line L “ C to the oriented point pt`
and the number 1 to the oriented circle. This theory is clearly unitarizable. A unitary structure is
data, and according to (4.21) the group of isomorphism classes of unitarity data is
(4.25)

Ą – H 1 pRP8 ; C{Zq
Ą – Z{2Z,
H 1 pBO1 ; C{Zq

Ą Ñ BO1 has holonomy ´1 around the nontrivial loop.33 The two equivwhere the local system C{Z
alence classes of unitarity data on F are easily explained. Writing F ppt` q “ L the unitarity data
33Here are two methods to compute (4.25): (1) use a cell structure on RP8 with a single cell in each dimension,

trivialize the local system over each cell, and derive the cochain complex
(4.26)

1´c

1`c

1´c

C{Z ÝÝÝÑ C{Z ÝÝÝÑ C{Z ÝÝÝÑ ¨ ¨ ¨

in which c is complex conjugation; (2) use the short exact coefficient sequence (4.22) where C, C{Z are local systems
with holonomy ´1 and Z is untwisted.

<!-- page 32 -->
32

D. S. FREED
–

provides an isomorphism F ppt´ q ÝÝÑ L. The oriented interval with both endpoints incoming is a
bordism pt´ > pt` Ñ H0 and applying F and the unitarity isomorphism we obtain a nondegenerate
hermitian form h : L b L Ñ C. Such a form is either positive or negative, which accounts for (4.25).
Remark 4.27. The positivity condition in a unitary theory means we should exclude the negative
form, so only allow a unique isomorphism class of unitarity data. The group (4.21) only implements
the correct action of orientation-reversal, not the positivity, but I do not know how to pick out the
subgroup corresponding to positive unitarity data in higher dimensions.
As a further illustration we consider n “ 2 spacetime dimensional oriented theories with EilenbergMacLane target. These theories are discussed in Example 2.11 and Example 2.31. The group of
oriented theories is
(4.28)

rΣ2 M T SO2 , Σ2 HC{Zs – H 2 pBSO2 ; C{Zq – C{Z,

and the theory Fz corresponding to z P C{Z has
(4.29)

Fz pXq “ λEulerpXq

for a closed oriented 2-manifold X, where λ “ e2πiz P Cˆ . Since X has an orientation-reversing
involution, only those theories with Fz pXq real can possibly be unitarizable, which forces z P iR.
That is consistent with the computation of (4.21) for n “ 2:
(4.30)

Ą – Z{2Z ‘ iR,
H 2 pBO2 ; C{Zq

together with the computation of the map
(4.31)

Ą ÝÑ H 2 pBSO2 ; C{Zq,
H 2 pBO2 ; C{Zq

which includes 12 Z{Z ‘ iR ãÑ C{Z. For z “ 1{2 ´ ix we have (4.29) with λ “ ´e2πx , but since the
Euler number is even the numerical invariants are positive. The line Fz pS 1 q “ L attached to the
oriented circle has a real structure, since S 1 has an orientation-reversing involution (reflection), and
the cylinder with both boundaries incoming gives a nondegenerate real symmetric bilinear form
h : L b L Ñ C. Glue 2-disks to each incoming boundary component to deduce that hpℓ, ℓq “ λ2 is
positive. The conclusion is that all theories with parameter λ P Rˆ Ă Cˆ are uniquely unitarizable.

5. SRE phases
There is one more preliminary before we can state our proposed topological invariant of shortrange entangled (SRE) phases: we must specify our choice of target spectrum for classifying longrange effective topological theories. Recall that in general to define a topological field theory (2.8)

<!-- page 33 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

33

we need to specify a target higher category C, but for an invertible theory we need the much
weaker information of the sub-groupoid C ˆ of invertibles; see (2.29). While concrete arguments
give information about the highest few homotopy groups of C ˆ , we can only guess at the structure
lower down, which is increasingly relevant as the dimension of the theory increases. In the general
fermionic case we take a universal choice, the Brown-Comenetz dual to the sphere spectrum. In
the bosonic case we have solid arguments to determine the “top part” of the spectrum, but after
that only sparse data points. For that reason we take the same target spectrum as in the fermionic
case—after all, theories with only bosons are special cases of general theories—though in space
dimension d “ 1 the “top part”, an Eilenberg-MacLane spectrum, is all that is relevant and so we use
it instead. We explain these choices in §5.1. Our main proposal is stated precisely in §5.2. In §5.3
we work out the relationship to the group cohomology classifications in the literature [CGLW],
[GW].
5.1. Target spectra
The discussions in Example 2.31 and especially §3.2(2) are relevant here.
5.1.1. Preliminary: duals to the sphere spectrum. Let A be an abelian group, which might be
discrete or have a topology. (In the latter case there is an additional hypothesis: A is locally
compact.) Examples: Z{nZ, Z, R{Z. There are two notions of dual group we might consider.
The first is the Pontrjagin dual, which is the group of continuous homomorphisms A Ñ R{Z. The
Pontrjagin dual of Z{nZ is isomorphic to Z{nZ, the Pontrjagin dual of Z is isomorphic to R{Z, and
the Pontrjagin dual of R{Z is isomorphic to Z. On the other hand, we can consider an integral dual
HompA, Zq. However, the naive interpretation is not so well behaved. For example, if A “ Z{nZ
there are no nonzero homomorphisms A Ñ Z. The resolution is to consider Homp´, Zq in the
derived sense, which means that we replace A by a free chain complex whose homology in degree 0
is A and then compute Hom. The result is called Ext‚ pA, Zq and is the “correct” integral dual. For
A “ Z{nZ the only nonzero group is in degree ´1, whereas for A “ Z the only nonzero group is in
degree 0.
Both notions of duality exist in the world of spectra; see [An], [HS, Appendix B], [FMS, Appendix B], [HeSt] for precise definitions and discussion.. Recall that a spectrum T‚ has an associated
Z-graded abelian group π‚ T . For the sphere spectrum S 0 the first several homotopy groups are
(5.1)

πt0,1,2,... u S 0 – tZ , Z{2Z , Z{2Z , Z{24Z , 0 , 0 , . . . u

The analog of the Pontrjagin dual is the Brown-Comenetz dual. For the sphere we denote it
as IC{Z. (We replace R{Z with C{Z; in topology it is often Q{Z instead.) Its homotopy groups
are the Pontrjagin dual groups to (5.1):
(5.2)

πt0,´1,´2,... u IC{Z – tC{Z , Z{2Z , Z{2Z , Z{24Z , 0 , 0 , . . . u

Note carefully the indexing difference on the left hand side between (5.2) and (5.1). The analog of
the integral dual is the Anderson dual. For the sphere we denote it as IZ. Its homotopy groups

<!-- page 34 -->
34

D. S. FREED

are the integral dual to (5.1); the torsion groups are degree shifted:
(5.3)

πt0,´1,´2,... u IZ – tZ , 0 , Z{2Z , Z{2Z , Z{24Z , 0 , 0 , . . . u

There is a fiber sequence IZ Ñ IC Ñ IC{Z and a corresponding long exact sequence of homotopy
groups. Note IC » HC is an Eilenberg-MacLane spectrum with a single nonzero homotopy group.
These spectra enjoy universal properties which make them universal targets for invertible field
theories. Recall that the notation ‘rX, X 1 s’ is used for the abelian group of homotopy classes of
maps X Ñ X 1 between spectra. If X is any spectrum, then
(5.4)

rX, Σn IC{Zs “ IC{Zn pXq – Hompπn X, C{Zq.

(To compute the IC{Z cohomology of a space Y , set X “ Σ8 Y the suspension spectrum, so πn X is
the nth stable homotopy group of Y .) Thus an invertible n-spacetime dimensional theory whose
values on closed n-manifolds are numbers in C{Z pushes uniquely to a field theory with values
in IC{Z, and any theory with target IC{Z is determined by its numerical values on n-manifolds.
For maps from any spectrum X into IZ there is a short exact sequence
(5.5)

0 ÝÑ Ext1 pπn´1 X, Zq ÝÑ IZn pXq ÝÑ Hompπn X, Zq ÝÑ 0

which is split, but not canonically.
5.1.2. Bosonic theories. We continue with theories F defined in d-space dimensions and assume
first that F is a bosonic theory. The target is a pd ` 1q-category Cbose , but since F is invertible
ˆ
we need only the groupoid Cbose
. Standard quantum mechanics dictates that F pY q is a complex
vector space for any closed d-manifold Y , and since F is invertible it must be 1-dimensional. Furthermore, a diffeomorphism of Y acts as an invertible map F pY q Ñ F pY q, which is multiplication
ˆ
of the target groupoid to the top two levels
by a scalar in34 Cˆ . Thus the truncation Ωd Cbose
is the groupoid Line of complex lines. A crucial point, discussed in §3.2(2), is that we use the
continuous topology on the morphism spaces, in particular on Cˆ . This gives information about
ˆ
:
some homotopy groups of Cbose
(5.6)

ˆ
πd Cbose
“ 0,

ˆ
πd`1 Cbose
“ 0,

ˆ
πd`2 Cbose
– Z.

The first equality expresses the fact that any two lines are isomorphic; the latter two that Cˆ is
ˆ
connected with infinite cyclic fundamental group. Furthermore, πk Cbose
“ 0 for k ą d ` 2 since
there are no non-identity k-morphisms for k ą d ` 1.
It remains to determine the lower homotopy groups. We have quite solid information about
the next homotopy group down, as we know the nature of the higher categorical invariant usually
attached to manifolds of dimension d ´ 1 by the theory F . For example, a standard choice is to
34In a unitary theory this scalar has unit norm, but the partition function of a general pd ` 1q-manifold need not.

<!-- page 35 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

35

assign a linear category to a closed pd ´ 1q-manifold, and since all invertible linear categories are
isomorphic deduce
(5.7)

ˆ
“ 0.
πd´1 Cbose

An alternative choice is to assign an invertible complex algebra to a closed pd ´ 1q-manifold, and
the triviality of the Brauer group of C leads to the same conclusion (5.7). At this stage we have
reproduced the first part of Example 2.31, in which the target is a 2-category and there are no further
homotopy groups. Note that (5.6) and (5.7) amount to an Eilenberg MacLane spectrum Σd`2 HZ:
a single nonzero homotopy group. This is the full story for d ď 1.
What is perhaps surprising is that we postulate a nonzero homotopy group at the next level
down:
(5.8)

ˆ
­“ 0.
πd´2 Cbose

One rationale for (5.8) is the 4-dimensional integral invertible oriented extended topological field
theory
(5.9)

ˆ
pd “ 2q
σ : Bord4 porientationq ÝÑ Cbose

for which the integer invariant σpW q of a closed oriented 4-manifold W is its signature SignpW q.
In its analytic incarnation this invariant involves only differential forms on W , not spinor fields, so
in that sense is bosonic. The theory factors through a map
(5.10)

Σ4 M T SO4 ÝÑ Σ4 KO

which can be viewed as the universal symbol [FHT, §3] of the signature operator in dimension 4.
The relevant stretch of homotopy groups of the target spectrum in (5.10) is
(5.11)

πt0,1,2,3,4u – tZ , 0 , 0 , 0 , Z u.

This theory does not factor through Σ4 HZ, so the bottom Z in (5.11) cannot be replaced by 0.
ˆ
) comes from
Another piece of evidence for at least a nonzero homotopy group in this spot (πd´2 Cbose
conformal nets. These are a possible target for 3-dimensional theories with numerical invariants
in C{Z, and conjecturally not all invertible conformal nets are isomorphic. (See [DH] for a discussion
of conformal nets in this context.)
We do not have any information about lower homotopy groups. So we could take the shifted
ˆ
Postnikov truncation Σd´6 KOx4, ..., 8y as a reasonable choice of target spectrum Cbose
. But the
Z at the bottom of the spectrum is overkill—a smaller torsion group will do—and so instead for
theories in dimension d ě 2 we use the universal choice, the Anderson dual of the sphere.
Hypothesis 5.12. The target spectrum for classifying long-range effective theories of a d-space
dimensional bosonic system is Σ3 HZ for d “ 1 and Σd`2 IZ for d ě 2.
Remark 5.13. The classification of anomalies has similar target spectra, but as indicated in §3.2(2)
we use instead the discrete topology on Cˆ . Thus for d ě 2 the target which classifies anomaly
theories is Σd`2 IC{Z; for d “ 1 it is Σ3 HC{Z.

<!-- page 36 -->
36

D. S. FREED

5.1.3. Fermionic theories. The hypothesis for theories with fermions is different. Namely, the
dichotomy between bosonic and fermionic states in quantum mechanical systems is encoded by
stipulating that the quantum Hilbert space be Z{2Z-graded: states with even grading are bosonic
and states with odd grading are fermionic. That persists in the long-range effective theory: vacua
are either bosonic or fermionic. So the complex lines F pY q in an invertible long-rang theory are
either even or odd. The existence of distinct isomorphism classes of Z{2Z-graded lines modifies (5.6):
(5.14)

ˆ
– Z{2Z,
πd Cfermi

ˆ
“ 0,
πd`1 Cfermi

ˆ
– Z.
πd`2 Cfermi

The k-invariant is nonzero; it is the composition βZ ˝ Sq 2 of the integer Bockstein and the Steenrod
square.
As in the bosonic case higher homotopy groups vanish. But now we expect many nontrivial lower
homotopy groups. For example, we expect (5.7) to be replaced by
(5.15)

ˆ
πd´1 Cfermi
– Z{2Z

since the super Brauer group of invertible Z{2Z-graded complex algebras has two elements (represented by even and odd complex Clifford algebras). The idea that modules over Clifford algebras
may be used as the state space of a quantum system is familiar in condensed matter theory; see
also [F5]. From the super Brauer category we compute how the three Eilenberg-MacLane spectra fit
ˆ
by arguments
together, though we do not do so here. We can gather information about πd´2 Cfermi
analogous to those in §5.1.2. For example, there is an invertible theory
(5.16)

Σ4 M T Spin4 ÝÑ KO

which assigns the Â-genus to a closed spin 4-manifold. (The universal symbol is quaternionic,
ˆ
which explains the absence of shift in KO.) This suggests that πd´2 Cfermi
­“ 0. Invertible fermionic
conformal nets are another clue, but the only knowledge is conjectural.
Therefore, by fiat really, we make a universal choice for the target spectrum, namely the Anderson
spectrum IZ. Notice that its first four homotopy groups (5.3) agree with (5.14) and (5.15) and
more precisely the Postnikov truncations are equivalent.
Hypothesis 5.17. The target spectrum for classifying long-range effective theories of a d-space
dimensional fermionic system is Σd`2 IZ.
Remark 5.18. We use the shift Σd`2 IC{Z as a target to classify anomaly theories.
5.1.4. Antilinear symmetries. As explained in §2.4.3 antilinear symmetries lead to anomalous field
theories after gauging. For invertible theories we account for the anomaly using twisted cohomology.
We implement complex conjugation on the target spectra by the universal p´1q-action defined
in Construction 4.23. Consider, for example, the Eilenberg-MacLane spectrum HZ. In degree 1
a cohomology class is represented by a map to Cˆ , and the p´1q-action is complex conjugation
on Cˆ . The classifying space for a degree 1 class is Cˆ , and Construction 4.23 gives a fiber bundle
(not principal!) with fiber Cˆ over RP8 whose holonomy acts as complex conjugation on Cˆ . In

<!-- page 37 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

37

degree 2, as just explained, a cohomology class is represented by a complex line bundle and this
action is complex conjugation on complex line bundles. In degree 3 there is a similar story with
bundles of complex algebras, and it is reasonable to extend this picture to all degrees. The same
story applies to HC{Z, which one can view as flat elements in HZ (with a degree shift). For
example, an element in degree 0 in HC{Z is a locally constant map to Cˆ . Similar considerations
apply to other target spectra. The top nonzero homotopy group of IZ (respectively IC{Z) is the
same as that of HZ (respectively HC{Z), and the p´1q-action is trivial on the Z{2Z homotopy
groups in (5.14) and (5.15) is trivial. Our tentative grasp on lower homotopy groups puts further
justification beyond reach.
5.2. Topological invariants of short-range entangled phases
We propose a home for long-range effective topological field theories of gapped systems with shortrange entanglement. We do not know if the map from the microscopic phases to the deformation
classes of field theories is either injective or surjective. Regardless, the evidence presented in the
remainder of the paper suggests that it is a very effective invariant.
Assume the theory is d-space dimensional and has a global symmetry group G, which is a Lie
group equipped with a smooth homomorphism
(5.19)

φ : G ÝÑ µ2 “ t˘1u

which encodes linearity vs. antilinearity: an element g P G with φpgq “ 1 acts linearly and an
element g P G with φpgq “ ´1 acts antilinearly. Recall our assumption, stated before (3.12), that
there is a G-equivariant extension of the long-range effective theory (non-anomalous case) or that
there is an anomaly and an anomalous extension (anomalous case).
The hypotheses underlying the proposal are stated in §3.2 and §5.1. We use the twisted Thom
isomorphism (4.13) (and its variations for SO and Spin replacing O).
5.2.1. Bosonic theories. According to Hypothesis 5.12 the target spectrum is Σd`2 HZ for d “ 1
and Σd`2 IZ for d ě 2. We use the notation ‘Σd`2 T Z’ for this target spectrum. Note that T Z is
a ring spectrum. Let τT Z denote the Thom twisting of the ring spectrum T Z associated to the
virtual bundle (see (4.18))
(5.20)

Rd ´ Spdq ÝÑ BSOd ,

and τ̄T Z the analogous Thom twisting for Od in place of SOd . Let wT Z denote the p´1q-twist of T Z
(Construction 4.23) associated to the double cover BSOd Ñ BOd . The homomorphism (5.19)
determines a p´1q-twist of T Z associated to the double cover35 BG0 Ñ BG, where G0 “ ker φ; we
denote it φT Z . Degree shifts are Thom twistings of trivial bundles, whence sums of twistings and
degrees are defined.
35If φ is identically `1, then G “ G and φ
0
T Z “ 0 is trivial.

<!-- page 38 -->
38

D. S. FREED

Proposal 5.21 (bosonic theories). Short-range entangled phases of a d-space dimensional bosonic
theory with global symmetry group G map to the abelian group
τ

SREbose pd, G, φq “ T Z T Z

(5.22)

`φT Z `d`2

pBSOd ˆ BGq

in the non-anomalous case. The unitarizable theories lie in the image of the map36
(5.23)

τ̄

T Z TZ

`wT Z `φT Z `d`2

τ

pBOd ˆ BGq ÝÑ T Z T Z

`φT Z `d`2

pBSOd ˆ BGq.

Anomalies are classified by the abelian group
τ

Anombose pd, G, φq “ T C{Z T Z

(5.24)

`φT Z `d`2

pBSOd ˆ BGq

and the anomalous theories with fixed anomaly map to a torsor for the abelian group (5.22).
An anomaly theory has spacetime dimension d ` 2, but here is only defined on manifolds of dimension ď d; this explains the degrees in (5.24). The last assertion is that any two choices of anomalous
theories with the same anomaly are related by tensoring with a non-anomalous theory.
5.2.2. Fermionic theories. The proposal for fermionic theories is similar: we simply swap out
the Eilenberg-MacLane spectra we used in the d “ 1 bosonic case for the Anderson and BrownComenetz spectra (§5.1.3) and assume all manifolds are spin in addition to being oriented. The
corresponding Thom twistings of (5.20) are denoted τIZ and τ̄IZ ; the p´1q-twisting of IZ associated
to the double cover BSOd Ñ BOd is wIZ ; and the p´1q-twisting of IZ associated to the double
cover BG0 Ñ BG is φIZ .
Proposal 5.25 (fermionic theories). Short-range entangled phases of a d-space dimensional fermionic
theory with global symmetry group G map to the abelian group
τ

SREfermi pd, G, φq “ IZ IZ

(5.26)

`φIZ `d`2

pB Spind ˆBGq

in the non-anomalous case. The unitarizable theories lie in the image of the map
(5.27)

τ̄

IZ IZ

`wIZ `φIZ `d`2

τ

pB Pind ˆBGq ÝÑ IZ IZ

`φIZ `d`2

pB Spind ˆBGq.

Anomalies are classified by the abelian group
(5.28)

τ

Anomfermipd, G, φq “ IC{Z IZ

`φIZ `d`2

pB Spind ˆBGq

and the anomalous theories with fixed anomaly map to a torsor for the abelian group (5.26).
36A more precise proposal would identify the subgroup of the domain of (5.23) representing unitary theories which

satisfy positivity. As I do not know how to do this—see §4.2.5—we settle for a weaker formulation.

<!-- page 39 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

39

5.2.3. Symmetry protected topological phases. Now we address the question of symmetry protected
topological (SPT) phases. The “symmetry protection” means that the effective topological field
theory F is trivial when the symmetry is ignored. As explained at the end of §3.3 this means
that the G-extension Fr is trivial when restricted to the trivial G-bundle. The basepoint of BG
determines an embedding X ãÑ X ^ BG` for any spectrum X, and so a restriction map
rX ^ BG` , X 1 s ÝÑ rX, X 1 s

(5.29)

for any spectrum X 1 . When X is a Madsen-Tillmann spectrum we can rewrite (5.29) using the
twisted Thom isomorphism; then the map is pullback along the inclusion
BOd ãÑ BOd ˆ BG

(5.30)
defined by the basepoint of BG.
Proposal 5.31.

(i) Symmetry protected topological phases of a d-space dimensional bosonic theory with global
symmetry group G map to the kernel
(5.32)

´
¯
τ `φ `d`2
τ `d`2
SP Tbose pd, G, φq “ ker T Z T Z T Z
pBSOd ˆ BGq ÝÑ T Z T Z
pBSOd q

of the indicated restriction map constructed from (5.30).
(ii) Symmetry protected topological phases of a d-space dimensional fermionic theory with global
symmetry group G map to the kernel
(5.33)

´
¯
τ `φ `d`2
τ `d`2
SP Tfermi pd, G, φq “ ker IZ IZ IZ
pB Spind ˆBGq ÝÑ IZ IZ
pB Spind q

of the indicated restriction map.
5.3. Relation to group (super) cohomology
From the definition of T Z at the beginning of §5.2.1 we construct a map of spectra
(5.34)

Σd`2 HZ ÝÑ Σd`2 T Z.

It induces the second map in the composition
(5.35)

τ

H d`2 pBG; Zφ q ÝÑ H d`2 pBSOd ˆ BG; Zφ q ÝÑ T Z T Z

`φT Z `d`2

pBSOd ˆ BGq;

the first is induced from the projection BSOd ˆ BG Ñ BG. Here Zφ Ñ BG is the local system
defined by (5.19). Note that ordinary cohomology is oriented for oriented vector bundles, which
explains why the twisting τT Z is trivialized when restricted under (5.34). The homomorphism (5.35)
maps the group cohomology phases discussed37 in [CGLW] to SREbose pd, G, φq. Furthermore, the
image of (5.35) lies in the subgroup SP Tbose pd, G, φq of symmetry protected phases; see (5.32).
37To compare it helps to observe that H d`2 pBG; Z q – H d`1 pBG; U p1q q, where U p1q has its continuous topology.
φ

φ

<!-- page 40 -->
40

D. S. FREED

Remark 5.36. If G is discrete, then the topological cohomology of BG is isomorphic to the group
cohomology of the group G. More generally, if G is a (finite dimensional) Lie group, then a theorem
of D. Wigner [Wi] states that the topological cohomology of BG with coefficients in a discrete Gmodule is isomorphic to the Borel cohomology of G; see [St] for more on group cohomology.
For theories with fermions Gu and Wen [GW] introduced a group “super” cohomology theory. In
fact, it can be identified with a certain generalized cohomology theory of the classifying space BG.
This generalized cohomology theory, which we simply call E, had already appeared in at least
a few contexts in theoretical physics: (1) in spin Chern-Simons theories [J] and (2) in QCD, in
the Wess-Zumino term of the long-range effective theory of pions [F4]. The spectrum E has two
nonzero homotopy groups:
π0 E – Z,

(5.37)

π´2 E – Z{2Z.

The k-invariant which relates them is nonzero. We defer to [F4, §1] for generalities on this cohomology theory.
The two nontrivial homotopy groups in E occur in (5.14), shifted up by degree d ` 2, and as the
k-invariant match there is a map E Ñ IZ of spectra. The theory E is oriented for spin bundles, as
proved in [F4, Proposition 4.4]. Therefore, there is a homomorphism38
(5.38)

φ `d`2

E E

τ

pB Spind ˆBGq ÝÑ SREfermi pd, G, φq “ IZ IZ

`φIZ `d`2

pB Spind ˆBGq.

The projection B Spind ˆBG Ñ BG induces an inclusion
(5.39)

E φE `d`2 pBGq ÝÑ E φE `d`2 pB Spind ˆBGq

which, after composition with (5.38), induces a homomorphism of the group “super” cohomology
into SREfermi pd, G, φq, as expected. Note that the image of E φE `d`2 pBGq in SREfermipd, G, φq lies
in the subgroup SP Tfermi pd, G, φq of symmetry protected phases; see (5.33).

6. Computations and special cases
We illustrate how the proposed invariants of gapped short-range entangled (SRE) phases in §5.2
detect phases not covered by the group cohomology classification discussed in §5.3. We organize the
discussion by space dimension d and by whether or not the theory includes fermions. The examples
treated here are non-anomalous. Clearly there are many more computations and analyses which
can be carried out.
38The map (5.38) is part of a long exact sequence; the terms which come before and after are maps into the

spectrum which is the cofiber of E Ñ IZ so has vanishing homotopy group in degrees ě ´2. The spin orientation
of E explains why τIZ does not appear in the domain of (5.38).

<!-- page 41 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

41

6.1. d “ 1 bosonic theories: group cohomology
This is the one case in which there is nothing beyond the group cohomology classification. There
are two reasons for this: (1) the group SO1 which governs the spatial tangential structure is trivial,
and (2) for d “ 1 we have T Z “ HZ. More formally, from (5.22) and (5.32) we deduce
SREbose p1, G, φq “ SP Tbose p1, G, φq
φ

(6.1)

“ HZ HZ

`3

pBSO1 ˆ BGq

3

– H pBG; Zφ q.
6.2. d “ 1 fermionic theories
Since the shifted Madsen-Tillmann spectra are connective (in this case the relevant spectrum is
Σ1 M T Spin1 ^BG` ), we can replace the codomain Σ3 IZ of an invertible topological field theory
by its connective cover. That connective cover is a module for ko-theory, which is connective real
K-theory. (See [F5, §4], for example, where that connective cover is the theory called ‘R´1 ’.) In
particular, the connective cover is Spin-oriented so the Thom twisting is trivial. Hence
(6.2)

φ

SREfermi p1, G, φq – IZ IZ

`3

pB Spin1 ˆBGq.

The subgroup coming from the BG factor is
φ

(6.3)

IZ IZ

`3

pBGq.

Remark 6.4. This already goes beyond the group “super” cohomology theory E, since E has two
nonzero cohomology groups (5.37), whereas the truncation of IZ we are using here has a third
nonzero homotopy group π´3 – Z{2Z.
Consider the special case G “ µ2 with φ nontrivial; this is the case of a time-reversal symmetry
which squares to the identity. Then (6.3) is cyclic of order 8:
(6.5)

φ

IZ IZ

`3

pBµ2 q – Z{8Z.

One proof of (6.5) is [DFM, Theorem 3.13].
Remark 6.6. One interpretation of the left hand side of (6.5) is the group of degree shifts of KOtheory, which is the Brauer group of real Z{2Z-graded central simple algebras. This is surely very
closely related to the classification in [FK, §V].
Because the group Spin1 – Z{2Z is nontrivial, there are additional SRE phases (6.2) not captured
by (6.3). One example is the truncation to 1-space dimension of the 2-spacetime dimensional “Arf
theory”. The invariant of a 2-dimensional closed spin manifold is ˘1 according to the Arf invariant
of the quadratic form defining the spin structure: even spin structures have invariant `1 and
odd spin structures have invariant ´1. The invariants on 1- and 0-dimensional manifolds are also

<!-- page 42 -->
42

D. S. FREED

explicit. The invariant of S 1 is the trivial even line for the bounding spin structure and the odd line
for the nonbounding spin structure. The invariant of pt` with the standard spin structure is the
complex Clifford algebra Cliff C
1 . (For simplicity we take the target 2-category C of the theory to be
algebras-bimodules-intertwiners. Equivalently, we can assign to pt` the category of Z{2Z-graded
Cliff C
1 -modules.) For more on the Arf theory, and a beautiful geometric application, see [G].
It appears that the Arf theory is realized as the long-range effective topological theory of the
Majorana chain [K6] in its nontrivial phase. For example, the description of the effective theory [K6,
(15)] does assign the Clifford algebra Cliff C
1 to a point.
In the remainder of this section we illustrate some relevant computational techniques. More
elaborate techniques are needed in higher dimensions, as we illustrate in the appendix. The Arf
theory is predicted by
(6.7)

IZ3 pΣ1 M T Spin1 q – IZ3 pB Spin1 q – Z{2Z.

In fact, since the Arf theory extends to a 2-spacetime dimensional theory, we can detect it in the
group IZ3 pΣ2 M T Spin2 q. It is illuminating to first compute
IC{Z2 pΣ2 M T Spin2 q – IC{Z2 pB Spin2 q
– IC{Z2 pCP8 q
(6.8)

– Hompπ2s CP8
` , C{Zq
– Hompπ2s CP8 ˆ π2s S 0 , C{Zq
– C{Z ˆ Z{2Z.

The first line is the Thom isomorphism; the third the defining property of IC{Z; the fourth the
general fact Σ8 pX` q » Σ8 X _ S 0 ; and the last line the results π2s pCP8 q – Z (computed in [Li],
for example) and π2s S 0 – Z{2Z. This is the set of 2-dimensional invertible spin theories with
target IC{Z. It includes the family of Euler theories (Example 2.11) parametrized by C{Z and the
Arf theory. The group of path components of (6.8) is
(6.9)

IZ3 pΣ2 M T Spin2 q – IZ3 pCP8 q – Z{2Z.

One computation of this group uses the split short exact sequence (5.5)
(6.10)

0 ÝÑ Extpπ2 Σ2 M T Spin2 q ÝÑ IZ3 pΣ2 M T Spin2 q ÝÑ Hompπ3 Σ2 M T Spin2 , Zq ÝÑ 0

and the computations π3s pCP8 q “ 0 and π3s pS 0 q – Z{24Z.
The Atiyah-Hirzebruch spectral sequence provides another means to compute the generalized
cohomology groups (6.8) and (6.9). The relevant portion of the E2 page of the spectral sequence
(6.11)

`
˘
E2pq “ H p CP8 ; IZq pptq ùñ IZp`q pCP8 q

<!-- page 43 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

43

Figure 7. Computation of IZ3 pCP8 q
for computing (6.9) is shown in Figure 7. The differentials emanating from the initial column
vanish, as can be seen from the splitting pt Ñ CP8 Ñ pt of the projection to a point. That
reasoning also applies to the spectral sequence
(6.12)

`
˘
E2pq “ H p CP8 ; IC{Zq pptq ùñ IC{Zp`q pCP8 q,

a portion of which is shown in Figure 8, and it also applies to prove that the short exact sequence
(6.13)

0 ÝÑ C{Z ÝÑ IC{Z2 pCP8 q ÝÑ Z{2Z ÝÑ 0

splits. (One reads off (6.13) from the E8 page.)

Figure 8. Computation of IC{Z2 pCP8 q – C{Z ˆ Z{2Z

6.3. d “ 2 bosonic theories: Kitaev E8 phase and chiral central charge
To investigate SRE phases at the other extreme from those detected by group cohomology, we
set G “ t1u to be the trivial group. Then necessarily φ : G Ñ µ2 is the trivial homomorphism.
Unwinding Proposal 5.21 we have
(6.14)

SREbose p2, t1u, 1q “ rΣ2 M T SO2 , Σ4 IZs,

<!-- page 44 -->
44

D. S. FREED

the group of H-type oriented theories with target the Anderson dual of the sphere. The following
computations are carried out in Appendix A. Recall that the group π4 M SO is Thom’s oriented
bordism group of 4-manifolds, which is isomorphic to Z via homomorphism which attaches to each
closed oriented 4-manifold M its signature SignpM q.
Proposition 6.15.
(i ) π3 Σ2 M T SO2 “ 0.
(ii ) π4 Σ2 M T SO2 – Z and the composition
(6.16)

Sign

π4 Σ3 M T SO2 ÝÑ π4 M SO ÝÝÝÝÑ Z

maps the generators to ˘4.
(iii ) π3 Σ3 M T SO3 “ 0.
(iv ) π4 Σ3 M T SO3 – Z and the composition
(6.17)

Sign

π4 Σ3 M T SO3 ÝÑ π4 M SO ÝÝÝÝÑ Z

maps the generators to ˘2.
We interpret these computations using (5.5). First, (i) and (ii) imply
(6.18)

rΣ2 M T SO2 , Σ4 IZs – Z.

Furthermore, the generating field theory extends to a Z-valued invertible 4-dimensional oriented
theory whose numerical invariant is 4 times the signature. Assertions (iii) and (iv) together imply
(6.19)

rΣ3 M T SO3 , Σ4 IZs – Z

and the generating field theory extends to a Z-valued invertible 4-dimensional theory whose numerical invariant is 2 times the signature. A 2-dimensional theory which generates the group (6.18)
does not extend to 3 dimensions, and a 3-dimensional theory which generates the group (6.19) does
not extend to 4 dimensions. We relate these factors to known geometric facts about η-invariants
and determinant lines.
The interpretation of the homotopical computations (6.14), (6.19) is not obvious at first glance;
indeed that mystery was the motivation for §2.8. Furthermore, the example discussed there—in
particular, the contractible choice replacing Ftopological with Fgeometric —has a clear analog in our
current situation. If we include a Riemannian metric as a field, then there is a 3-spacetime dimensional theory whose invariant of a closed oriented Riemannian 3-manifold is the exponentiated
Atiyah-Patodi-Singer η-invariant [APS].39 As in Remark 2.43 there is a related 4-dimensional
theory (called α̃8 below) whose value on a closed oriented 4-manifold M is a multiple of the signature SignpM q. If we use the η-invariant associated to the signature operator, then the multiple is 1.
39More precisely, for a self-adjoint operator B the invariant is exp`πipη

˘

B ` hB q , where hB “ dim ker B.

<!-- page 45 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

45

But we can use instead the η-invariant associated to the self-duality operator; the corresponding
boundary operator B is 1{2 that of the signature operator. (This η-invariant appears in quantum
Chern-Simons theory [FG, (1.27)].) This theory represents a generator of (6.19); the multiple of
the signature is 1/2. The invariants of 2-manifolds are determinant lines, and the determinant
line of the 2-dimensional signature operator on a closed oriented Riemannian manifold has a natural 4th root: the determinant line of the B̄-operator. Determinant lines of B̄ provide a generator
of (6.18); the multiple of the signature is 1/4.
Remark 6.20. The discussion in §4.1, especially Remark 4.8, and also Remark 3.10 are relevant here.
A theory classified by (6.19) gives integer invariants of 4-manifolds whose stable tangent bundle
can be represented by a rank 3 vector bundle. Such manifolds have even signature. (For example,
the 4th Stiefel-Whitney number vanishes. It is the reduction modulo 2 of the Euler number which
is equal to the signature modulo 2.) An example of such a 4-manifold is the mapping cylinder of
a 3-manifold, which fibers over the circle, but then the signature vanishes. A nontrivial example
is the connected sum M “ pCP2 q#2 # pS 1 ˆ S 3 q#3 , which has signature 2 and Euler number 0.
The vanishing Euler number implies that M admits a nonzero vector field, which splits an oriented
line bundle off of T M . Similarly, 4 divides the signature of a compact oriented 4-manifold whose
stable tangent bundle is 2-dimensional. In this case there are nontrivial examples which are fiber
bundles; the base and fiber are both compact oriented 2-manifolds. The first examples are due to
Atiyah [A3]; an example with signature exactly 4 is constructed in [EKKOS, Theorem 1].
We now argue that the SRE phase referred to in the literature as “Kitaev’s E8 phase” or “Kitaev’s
E8 state” (see [K5], [K2], [LV]) has the field theory whose invariant is exactly the signature as its
low energy approximation.
To make a first connection to E8 Chern-Simons, we recall that the gravitational Chern-Simons
invariant enters into the quantization of classical Chern-Simons theory as a counterterm [W1,
(2.20)]. Its appearance means that in general quantum Chern-Simons theory is anomalous as an
oriented theory. The anomaly is an invertible 4-dimensional theory
(6.21)

αc̄ : Σ4 M T SO4 ÝÑ Σ4 ICˆ

whose invariant on a closed oriented 4-manifold M is
(6.22)

e2πi c SignpM q{8 “ e2πi c p1 pM q{24 .

The anomaly depends only on the mod 8 reduction c̄ of the chiral central charge c P R of the
corresponding 2-dimensional chiral Wess-Zumino-Witten model.
Remark 6.23. Walker’s approach [Wa] to quantum Chern-Simons theory uses bounding 4-manifolds
to control the framing dependence. In joint work with Constantin Teleman (so far unpublished) we
prove that a modular tensor category is invertible as an object in the 4-category of braided tensor
categories, and we use it to define an invertible oriented 4-dimensional topological field theory which
is precisely αc̄ . Note that the modular tensor category determines c̄ “ c pmod 8q—see [K5, (172)],
for example—but it does not determine c P R. The usual approach to quantum Chern-Simons

<!-- page 46 -->
46

D. S. FREED

theory in the mathematics literature is to lift to a theory of manifolds with a pw1 , p1 q-structure.
A w1 -structure is a trivialization of w1 : an orientation. A p1 -structure is similar [BHMV], but its
geometric avatars are not as simple as an orientation. For example, a p1 -structure on a 3-manifold
can be given by a “2-framing” [A2]. In this way one obtains Chern-Simons as an extended theory
of 1-, 2-, and 3-dimensional manifolds, but to do so one needs to lift c pmod 8q to c pmod 24q. Of
course, given c P R there is a preferred choice, but starting from a modular tensor category there
are 3 choices.
We observe that given a chiral central charge c P R there is a 4-dimensional invertible theory

(6.24)

α̃c : Σ4 M T SO4 ÝÑ Σ4 HR

whose invariant on a closed oriented 4-manifold M is the real number

(6.25)

c SignpM q{8.

The anomaly theory αc̄ in (6.21) is obtained by composing (6.24) with the map Σ4 HR Ñ Σ4 ICˆ
induced by the exponential map e2πip´q : R Ñ Cˆ ; see (5.4). If c “ 8n for some n P Z, then
(6.24) factors through an integral theory

(6.26)

α̃8n : Σ4 M T SO4 ÝÑ Σ4 IZ

These integral topological theories are not part of the usual quantum Chern-Simons theory: only
the exponential (6.21) of (6.24) occurs (as the “framing anomaly” theory). For the theories
in (6.26) the framing anomaly is trivial. What does occur in Chern-Simons is the invertible metric 3-dimensional theory whose partition function is the exponentiated η-invariant to a suitable
power [W1]. E8 Chern-Simons at level 1, or Chern-Simons theory for the maximal torus of E8
(with its Cartan matrix specifying the level, or “K-matrix”), has chiral central charge c “ 8. The
η-invariant which occurs is associated to the signature operator, and this is the class of theories we
associate to Kitaev’s E8 phase.
Remark 6.27. Proposition 6.15 implies that there are additional possibilities for an H-type 2dimensional theory: a “4th root” of the effective theory of Kitaev’s E8 phase. Such theories are
associated with chiral central charge c “ 2, and in general the 2-dimensional H-type theories are
associated with chiral central charge divisible by 2. This matches the conformal anomaly in 2dimensional conformal field theory—see [S1, (5.9)], for example: if the chiral central charge is not
divisible by 2, then a p1 -structure is needed to define the theory. Even if we require the theory to
extend to 3-manifolds, there is still the possibility of dividing by 2, so having chiral central charge
divisible by 4. So it appears that our proposal allows for more effective topological theories than
have been seen so far by SRE phases.

<!-- page 47 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

47

6.4. d “ 2 bosonic theories: mixed gravitational/gauge phases
Continuing with d “ 2 space dimensional theories, we give an example to illustrate the unitarizability restriction in (5.23). Now we allow a global symmetry group G.
We focus on the Kunneth component
(6.28) H 2 pBSO2 ; Zq b H 2 pBG; Zφ q Ă H 4 pBSO2 ˆ BG; Zφ q
ÝÑ IZτIZ `φIZ `4 pBSO2 ˆ BGq “ SP Tbose p2, G, φq.
The group H 2 pBSO2 ; Zq is infinite cyclic with generator the Euler class e. For simplicity let G be
finite and φ the trivial homomorphism. Then H 2 pBG; Zq – H 1 pBG; Cˆ q is isomorphic to the
group of abelian characters χ : G Ñ Cˆ . Fix one and let λχ P H 2 pBG; Zq be the corresponding
class. Let F be the theory which corresponds to e b λχ in (6.28). We remark in passing that
F does not extend to a 3-spacetime dimensional theory: the Euler class e is not the restriction
of a class in H 2 pBSO3 ; Zq “ 0. The main point: this theory is not unitarizable. To see this
it suffices to restrict along HZ ÝÑ IZ in (5.23), since we are trying to hit e b λχ which lies in
ordinary cohomology. There is an isomorphism τ̄HZ – wHZ of twistings in the domain of (5.23),
so the relevant group is H 4 pBO2 ˆ BG; Zφ q and the relevant Kunneth component is H 2 pBO2 ; Zq b
H 2 pBG; Zφ q. The Euler class e does not 40 drop to a class in H 2 pBO2 ; Zq.
Remark 6.29. It is instructive to compute something nontrivial in the theory F . Let Y be a closed
oriented 2-manifold and P Ñ Y a principal G-bundle. Then F pP Ñ Y q is a complex line. Suppose
ϕ is an automorphism of P Ñ Y , so a map
P

ϕ

/P

(6.30)


Y

ϕ̄


/Y

of principal G-bundles covering an orientation-preserving diffeomorphism of Y . Gluing the ends
of r0, 1s ˆ P Ñ r0, 1s ˆ Y using ϕ we obtain a principal G-bundle Qϕ Ñ Xϕ over the mapping
cylinder Xϕ . Note that the mapping cylinder is a 3-manifold which is the total space of a fiber
bundle Xϕ Ñ S 1 with typical fiber Y . The rank 2 relative tangent bundle T pXϕ {S 1 q Ñ Xϕ is
oriented so has an Euler class epXϕ {S 1 q P H 2 pXϕ ; Zq. The G-bundle Qϕ Ñ Xϕ has a characteristic
class λχ pQϕ q P H 1 pXϕ ; Cˆ q. Then the action of ϕ on the line F pP Ñ Y q is multiplication by
(6.31)

xepXϕ {S 1 q ! λχ pQϕ q, rXϕ sy P Cˆ .

In (6.31) we pair the cup product of the characteristic classes with the fundamental class of the
oriented 3-manifold Xϕ . A special case of note: ϕ̄ is the identity diffeomorphism, P Ñ Y is
the trivial bundle, and the gauge transformation ϕ is given by an element g P G (assuming Y is
connected). Then (6.31) reduces to χpgqEulerpY q , where EulerpY q P Z is the Euler number.
40It does drop to a class on BO with twisted coefficients, but that is not relevant here.
2

<!-- page 48 -->
48

D. S. FREED

6.5. d “ 3 bosonic theories: time-reversal symmetry
Set G “ µ2 and φ : µ2 Ñ µ2 the identity map. The group cohomology captures a subgroup of
the group of SRE phases:
H 5 pBµ2 ; Zφ q “ H 5 pRP8 ; Zφ q – Z{2Z,

(6.32)

as appears in [CGLW]. Another nontrivial SRE phase of order 2 was introduced in [VS] where it
was emphasized that this goes beyond the group theory computation. This SRE phase is predicted
by Proposal 5.21.
Proposition 6.33. We have
(6.34)

SREbose p3, µ2 , idq “ IZτIZ `φIZ `5 pBSO3 ˆ RP8 q – Z{2Z ˆ Z{2Z.

Furthermore, the map
(6.35)

i : H 5 pBSO3 ˆ RP8 ; Zφ q ÝÑ IZτIZ `φIZ `5 pBSO3 ˆ RP8 q

is surjective and
(6.36)

H 5 pBSO3 ˆ RP8 ; Zφ q – Z{2Z ˆ Z{2Z ˆ Z{2Z.

We defer most of the proof to the appendix; here we briefly sketch two ways to compute (6.36).
The first is a direct approach. Use the chain complex41
(6.37)

0

0

2

0

0

2

0

2

0

2

0

Z ÐÝÝ 0 ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ¨ ¨ ¨

for BSO3 and the chain complex
(6.38)

2

Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ÐÝÝ Z ¨ ¨ ¨

for RP8 with the nontrivial local system Zφ Ñ RP8 . Compute the cohomology of the cochain
complex obtained by applying Homp´, Zq to the tensor product of (6.37) and (6.38). An alternative
approach is to apply the Kunneth formula for cohomology [Sp, §5.5], which in this case gives a split
short exact sequence
“
‰5
(6.39) 0 ÝÑ H ‚ pBSO3 ; Zq b H ‚ pRP8 ; Zφ q ÝÑ H 5 pBSO3 ˆ RP8 ; Zφ q
“
‰6
ÝÑ H ‚ pBSO3 ; Zq ˚ H ‚ pRP8 ; Zφ q ÝÑ 0
Here ‘˚’ denotes the torsion product of abelian groups. The tensor product in the kernel of (6.39)
is isomorphic to Z{2Z ˆ Z{2Z generated by the nonzero class in H 5 pRP8 ; Zφ q – Z{2Z and the
tensor product of p1 P H 4 pBSO3 ; Zq and the nonzero class a P H 1 pRP8 ; Zφ q. The quotient group
in (6.39) is isomorphic to Z{2Z, which is the torsion product H 3 pBSO3 ; Zq ˚ H 3 pRP8 ; Zφ q.
41This is the minimal chain complex [Ha, Proposition 3E.3] derived from the homology of BSO .
3

<!-- page 49 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

49

Claim 6.40. The image ipp1 baq of p1 ba under (6.35) is the long-range effective topological theory
of the SRE phase identified in [VS].
We argue for this claim in §7.
Remark 6.41. Since ipp1 b aq is torsion we can lift it to the group IC{ZτIZ `φIZ `4 pBSO3 ˆ RP8 q
where it is easier to identify a particular theory in this class; see Remark 2.48.

7. Boundary conditions and long-range topological field theories
We begin in §7.1 with a general discussion of spatial boundary conditions for field theories and
condensed matter systems. We specialize to the case at hand: the bulk theory is gapped and
the long-range topological theory is invertible. We apply these general ideas in §7.2 to argue for
Claim 6.40, which locates the 3d E8 phase with half-quantized surface thermal Hall effect introduced
in [VS] and further investigated in [BCFV]. We recover some key aspects of that theory from our
topological viewpoint.
7.1. Boundary terminations
Suppose we are given a theory F in n spacetime dimensions. It may be a quantum field theory or
a condensed matter theory. Then to a compact pn ´ 1q-manifold Y with empty boundary we obtain
a complex vector space of states. We would like to extend to allow compact pn ´ 1q-dimensional
manifolds Y which have nonempty boundary. These boundaries are spatial, not temporal. In
this case we expect to impose boundary conditions β which essentially close off the boundary. In
other words, the pair pY, βq behaves as a closed pn ´ 1q-manifold for the pair of theories pF, βq,
and the pF, βq theory attaches to it a vector space of states. (Without the boundary condition β
we expect instead a module for an algebra more complicated than C, or an object in a category
more complicated than Vect.) Furthermore, we expect β to be local. In classical physics a spatial
boundary condition is typically a local constraint on fields: a boundary condition for a system of
classical partial differential equations. In quantum physics a spatial boundary condition is a relative
field theory (§2.3)
(7.1)

β : τď n´1 F ÝÑ 1.

The theory F evaluates on Y to a map F pY q : Vect Ñ F pBY q and the boundary condition β
evaluates on BY to a map βpBY q : F pBY q Ñ Vect. The composition βpBY q ˝ F pY q : Vect Ñ Vect
is tensor product with the vector space associated to Y in the theory pF, βq. If F is an invertible
field theory, then β is an anomalous theory with anomaly F . We call pF, βq a bulk-boundary pair.
Remark 7.2 (Vocabulary). A quantum boundary condition β in quantum field theory is sometimes
called a D-brane, a term most appropriate in the context of 2-spacetime dimensional conformal
field theories. In condensed matter physics β goes by a name like edge termination or surface

<!-- page 50 -->
50

D. S. FREED

termination, depending on the dimension of the theory. Sometimes the word ‘excitation’ is used in
place of ‘termination’.
Remark 7.3. If F is a topological field theory with values in an p8, nq-category C, then a boundary
condition is a 1-morphism F pptq Ñ 1 in C. The dual42 map 1 Ñ F pptq may be considered as an
“object in F pptq”. For example, if n “ 2 and C is a 2-category of categories, then β is literally an
object in the 1-category F pptq. Boundary conditions in topological theories are a special case of a
much more general construction [L, Example 4.3.22].
Remark 7.4. If F is a d-space dimensional theory of H-type, then (7.1) is replaced by
(7.5)

β : τď d´1 F ÝÑ 1.

There is not a unique boundary condition for a given F , but rather F determines a collection
of boundary conditions. These formal considerations can lead to physical consequences. One
important example in condensed matter physics is the integer quantum Hall effect; see [W4] for an
account aimed at mathematicians.
Suppose the theory F is the long-range topological approximation to a gapped d-space dimensional system of H-type. Then if a boundary condition produces a combined bulk-boundary pair
which is still gapped, we expect that the long-range topological approximation is a bulk-boundary
pair pF, βq of topological theories. If F describes a short-range entangled phase—that is, F is
invertible—then β is a pd ´ 1q-space dimensional anomalous theory with anomaly F . We implicitly
assume that the truncation τď d´1 F of F is nontrivial. If, furthermore, F describes an SPT phase,
then we arrive at the following trichotomy.
A long-range effective boundary condition:
(7.6)

(i) produces a gapless bulk-boundary pair which preserves the symmetry,
(ii) is non-anomalous and breaks the symmetry, or
(iii) is anomalous, symmetric, and exhibits long-range entanglement.

Possibility (ii) arises since by the definition of an SPT phase F restricts to a trivial theory when the
symmetry is broken, and a theory relative to the trivial theory is non-anomalous. For (iii) we observe
that an invertible theory relative to an invertible theory τď d´1 F is a trivialization of τď d´1 F , so
if τď d´1 F is not trivial then any relative theory must not be invertible. In the physics lingo it is
not short-range entangled but rather is long-range entangled—it “exhibits topological order”. The
trichotomy (7.6) is a restatement of an assertion in the introduction to [VS].

42The choice of direction of the arrow in (7.1) reflects our choice that BY is outgoing rather than incoming. There

is an equivalent exposition with the other choice, and we would not need the dual here.

<!-- page 51 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

51

7.2. The invertible field theory of an exotic d “ 3 bosonic phase
We turn now to the SPT phase identified as ipp1 b aq at the end of §6.5.
The argument that ipp1 b aq corresponds to the 3d E8 phase with half-quantized surface thermal Hall effect is based on (iii) in the trichotomy (7.6). Consider a long-range effective boundary condition—surface termination—which is time-reversal symmetric and anomalous with anomaly ipp1 b aq. This boundary condition is a relative 3-spacetime dimensional topological theory. We
claim that any Chern-Simons theory with chiral central charge

c”4

(7.7)

pmod 8q

is such an effective boundary condition: it satisfies (iii) in the trichotomy. (See §6.3 for a topological
discussion of chiral central charge.) One of the simplest examples is Chern-Simons theory for the
maximal torus of SO8 , which was proposed for this role in [VS, §VII] and was realized as a boundary
condition in the exactly soluble Hamiltonian constructed in [BCFV].
To justify the claim begin with the short exact coefficient sequence
1r r
r ÝÑ 1 Z
r
0 ÝÑ Z
2 ÝÑ 2 Z{Z ÝÑ 0

(7.8)

r Z
r – 1 Z{Z – Z{2Z, which in particular is
in which the first map is the inclusion. Identify 12 Z{
2
untwisted, and so write43 p1 b a as the image of
(7.9)

1
2 p1

pmod Zq P H 4 pBSO3 ; 12 Z{Zq Ă H 4 pBSO3 ˆ RP8 ; 12 Z{Zq

under the connecting homomorphism in the long exact sequence deduced from (7.8). The image i
in the Brown-Comenetz dual of the sphere is computed via the sequence of maps

(7.10) H 4 pBSO3 ; 21 Z{Zq – H 4 pΣ4 M T SO3 ; 21 Z{Zq
ÝÑ H 4 pΣ4 M T SO3 ; C{Zq – rΣ4 M T SO3 , Σ4 HC{Zs
ÝÑ rΣ4 M T SO3 , Σ4 IC{Zs – C{Z.

The last isomorphism follows from Proposition 6.15(iv). Since (7.9) has order 2, so does its image,
and checking against (6.22) we identify it with the anomaly theory αc̄ with c̄ ” 4 pmod 8q. As
explained in §6.3, αc̄“4 is the (framing) anomaly of any quantum Chern-Simons theory whose chiral
central charge satisfies (7.7).
43This maneuver allows us to write the torsion class p b a as a class in one lower degree, and so identify it with
1

particular field theories. This circumvents the issues raised in §2.8 about nontorsion classes; see Remark 2.48.

<!-- page 52 -->
52

D. S. FREED

Appendix A. Some homotopy groups of Madsen-Tillmann spectra
We prove Proposition 6.15 and Proposition 6.33. I thank Oscar Randal-Williams for sharing his
expertise, for correcting a mistake in a previous version of Proposition 6.15, and for providing a
few arguments in the proof.
First recall some facts about Madsen-Tillmann spectra. Set Xn “ Σn M T SOn . Then X1 » S 0 .
Let Σ8 Y denote the suspension spectrum of a pointed space Y . The fibration
Xn´1 ÝÑ Xn ÝÑ Σn Σ8 pBSOn q`

(A.1)

is proved in [GMTW, Proposition 3.1] and [FHT, Lemma 3.8]. For any space Y we have
Σ8 pY` q » S 0 _ Σ8 Y.

(A.2)

The stable homotopy groups of a pointed space Z are πjs Z “ πj Σ8 Z. The oriented version of (4.10)
expresses the Thom spectrum M SO as the colimit of a sequence of maps X1 Ñ X2 Ñ X3 Ñ ¨ ¨ ¨ .
The homotopy groups of M SO are Thom’s oriented bordism groups. The long exact sequence of
homotopy groups deduced from (A.1) implies that
–

πj Xn ÝÝÑ πj M SO,

(A.3)

j ă n,

is an isomorphism and that there is an exact sequence
χ

πn`1 Xn`1 ÝÝÑ Z ÝÑ πn Xn ÝÑ πn M SO ÝÑ 0.

(A.4)

An element of πn`1 Xn`1 is represented by a closed oriented pn ` 1q-manifold W , and its image
under χ is the Euler number of W . For n even the map χ is zero. For n “ 3 the map χ is surjective,
since χpCP2 # S 1 ˆ S 3 q “ 1.
Proof of Proposition 6.15. First apply (A.4) with n “ 3 to derive the exact sequence
χ

π4 X3 ÝÑ π4 X4 ÝÝÑ Z ÝÑ π3 X3 ÝÑ π3 M SO

(A.5)

As remarked above the Euler characteristic map χ is onto, and since π3 M SO “ 0 we deduce
π3 X3 “ 0, which is (iii) in the proposition. Next, apply (A.4) with n “ 4 to deduce π4 X4 – Z ˆ Z
Sign

and the composition π4 X4 Ñ π4 M SO ÝÝÝÑ Z is surjective. Then a stretch of the long exact
sequence of homotopy groups deduced from (A.1) with n “ 4 is

(A.6)

π1s pBSO4 q`
Z{2Z

/ π4 X3

/ π4 X4

ZˆZ

χ

/ π s pBSO4 q`

/π X

Z

0

0

3

3

<!-- page 53 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

53

from which π4 X3 – Z or Z ˆ Z{2Z. To see that it is the former, let F be the fiber of the spectrum
map X3 Ñ HZ which represents the generator of H 0 pX3 ; Zq – Z. So there is a cofiber sequence
F ÝÑ X3 ÝÑ HZ.

(A.7)

Then (A.3) and the vanishing of π3 X3 imply that πj F “ 0, j ď 3, whence the Hurewicz map
π4 F Ñ H4 F is an isomorphism. In addition, the map π4 F Ñ π4 X3 is an isomorphism. Figure 9
is a schematic depiction of the long exact sequence of F2 -cohomology groups induced by the cofi-

Figure 9. Long exact sequence in F2 -cohomology induced by F Ñ X3 Ñ HZ
bration (A.7), where F2 “ Z{2Z is the field of 2 elements. The F2 -cohomology of a spectrum is
a Z-graded F2 -vector space which is a module for the Steenrod algebra. The dots indicate basis
elements and the vertical arrows the action of the Steenrod operations Sq 1 , Sq 2 . The degrees in
the figure ascend from 0 to 5. The F2 -cohomology of HZ is isomorphic to the group of cohomology operations HZ Ñ HZ{2Z and is computed by a theorem of Serre. The generators are the
operations Sq 2 , Sq 3 , Sq 4 , Sq 5 (preceded by reduction modulo 2), and the action of the Steenrod
operations is given by the Adem relations. For X3 the generators are w2 u, w3 u, w22 u, w2 w3 u where
u P H 0 pX3 ; F2 q is the mod 2 Thom class of the virtual bundle (5.20), which stably is minus the
canonical rank 3 bundle Sp3q Ñ BSO3 . Its total Stiefel-Whitney class is
(A.8)

w̃ “

1
“ 1 ` w2 ` w3 ` w22 ` ¨ ¨ ¨ ,
1 ` w2 ` w3

the inverse of the Stiefel-Whitney class of Sp3q Ñ BSO3 . The action of the total Steenrod operation Sq “ 1 ` Sq 1 ` Sq 2 ` ¨ ¨ ¨ is Sqpuq “ w̃u. The horizontal arrow in degree 0 follows from the
definition of X3 Ñ HZ, and the arrows in degrees 2,3,4 from the module structure, as does the
lack of a horizontal arrow in degree 5. Exactness then implies the existence of a class in H 4 pF ; F2 q
which maps to Sq 5 P H 5 pHZ; F2 q. Thus
(A.9)

F2 – H 4 pF ; F2 q – HompH4 F, F2 q – Hompπ4 F, F2 q – Hompπ4 X3 , F2 q

and we conclude π4 X3 ﬂ Z ˆ Z{2Z, whence π4 X3 – Z. For the last claim in (iv) we revisit (A.5).
A 4-manifold which represents a class in π4 X3 has vanishing w4 , since w4 is a stable characteristic

<!-- page 54 -->
54

D. S. FREED

class and vanishes for rank 3 bundles. Thus its Euler number is even, and since the Euler number
and signature are congruent modulo 2 its signature is also even. Then observe that the 4-manifold
pCP2 q#2 # pS 1 ˆ S 3 q#3 represents an element of π4 X3 (since it has vanishing Euler characteristic,
so a nonvanishing vector field which splits a line bundle off its tangent bundle) and has signature 2.
Similar techniques prove (i) and (ii). (An alternative is to use the Madsen-Weiss theorem [MaWe]
and known facts about the stable homology of mapping class groups of surfaces.) First
(A.10)

πt0,1,2u X2 – tZ , 0 , Zu

from (A.3) and (A.4) with n “ 2. There is a nontrivial k-invariant connecting these homotopy
groups; if not, then H 2 pX2 ; F2 q – H 2 pBSO2 ; F2 q would be 2-dimensional. Let C denote the
spectrum with these two nonzero homotopy groups and nontrivial k-invariant. Its F2 -cohomology
is worked out in Figure 10 using the cofiber sequence Σ2 HZ Ñ C Ñ HZ. All cohomology in

Figure 10. Long exact sequence in F2 -cohomology induced by Σ2 HZ Ñ C Ñ HZ
degree 1 vanishes. Also, the nontrivial connecting map H 2 pΣ2 HZ; F2 q Ñ H 3 pHZ; F2 q is the kinvariant. Let F 1 be the fiber of the Postnikov map X2 Ñ C, and consider the cofiber sequence
F 1 Ñ X2 Ñ C. The induced maps on F2 -cohomology are worked out in Figure 11; the nonzero

Figure 11. Long exact sequence in F2 -cohomology induced by F 1 Ñ X2 Ñ C
cohomology is in degrees 0,2,4,5. We deduce
(A.11)

H 4 pF 1 ; F2 q – F2 ,

<!-- page 55 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

55

and from Hurewicz πď3 F 1 “ 0 and π4 F 1 Ñ H4 F 1 is an isomorphism. Now the long exact sequence
of homotopy groups induced from (A.1) with n “ 2 includes the stretch
π4 S 0

/ π4 X2

(A.12)
0

/ π s pBSO2 q`
2

/ π3 S 0

Z ˆ Z{2Z

Z{24Z

This implies π4 X2 – Z or ZˆZ{2Z; (A.11) rules out the latter since π4 F 1 – π4 X2 and H 4 pF 1 ; F2 q –
HompH4 F 1 , F2 q – Hompπ4 F 1 , F2 q. For the last statement in (ii) consider the long exact sequence
of homotopy groups induced from (A.1) with n “ 3:
π4 X2

/ π4 X3

/ π s pBSO3 q`

/ π3 X2

Z

Z

Z{2Z

0

(A.13)

1

and so the first homomorphism is multiplication by ˘2 on generators.

Proof of Proposition 6.33. As a preliminary we prove that π5 X3 is finite. Since this group is finitely
generated, an equivalent assertion is π5 X3 b Q “ 0. To prove this observe that X3 Ñ M SO induces
an isomorphism on rational homology in degrees ď 7, whence also on rational homotopy groups in
that range. Collating with (A.3) and facts in the previous proof we have
(A.14)

πt0,1,2,3,4,5u X3 – tZ, 0, 0, 0, Z, finiteu.

Introduce the mapping spectrum
A “ MappX3 , Σ5 IZq.

(A.15)
From44 (5.5) and (A.14) we deduce
(A.16)

πt0,1,2,3,4,5u A – t0, Z, 0, 0, 0, Zu,

and πě6 A “ 0. The cohomology group in (6.34) is AφA pRP8 q, which we compute using the AtiyahHirzebruch spectral sequence. The rows in the E2 page, shown in Figure 12, are twisted cohomology
groups of RP8 . All differentials vanish in this range, for degree reasons, whence AφA pRP8 q is
isomorphic to Z{2Z ˆ Z{2Z or Z{4Z, depending on whether there is a group extension.
Define
(A.17)

B “ MappX3 , Σ5 HZq.

44More simply, the Z-graded homotopy group of the Anderson dual to X is the derived R Hompπ X , Zq; there
3
‚ 3

is a shift of 5 in (A.16)

<!-- page 56 -->
56

D. S. FREED

Figure 12. Computation of AφA pRP8 q
Then
(A.18)

πj B “ rΣj X3 , Σ5 HZs – H 5´j pX3 ; Zq – H 5´j pBSO3 ; Zq,

where the last step is the Thom isomorphism. Hence
(A.19)

πt0,1,2,3,4,5u B – t0, Z, Z{2Z, 0, 0, Zu.

The map HZ Ñ IZ induces a map B Ñ A and so a map of Atiyah-Hirzebruch spectral sequences.
The E2 page of the spectral sequence for B φB pRP8 q is shown in Figure 13. The group B φB pRP8 q –

Figure 13. Computation of B φB pRP8 q
pZ{2Zqˆ3 was computed after (6.36), and it follows that d2 : E21,´1 Ñ E23,´2 vanishes and there is
no group extension passing from the degree 0 part of the E8 page to B φB pRP8 q. The map of
spectral sequences now implies that there is no group extension in the A-spectral sequence either,
that AφA pRP8 q – pZ{2Zqˆ2 , and that i : B φB pRP8 q Ñ AφA pRP8 q is surjective.


<!-- page 57 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

57

References
[A1]
[A2]
[A3]
[ABGHR]

[ABS]
[An]
[APS]
[Ay]
[BCFV]
[BD]
[BHMV]
[CFV]
[CGLW]

[CGW1]

[CGW2]

[CLW]

[Detal]

[DF]

[DFM]

[DH]

[DW]
[EKKOS]
[F1]

M. F. Atiyah, Topological quantum field theories, Inst. Hautes Études Sci. Publ. Math. (1988), no. 68,
175–186 (1989).
, On framings of 3-manifolds, Topology 29 (1990), no. 1, 1–7.
, The signature of fibre-bundles, Global Analysis (Papers in Honor of K. Kodaira), Univ. Tokyo
Press, Tokyo, 1969, pp. 73–84.
Matthew Ando, Andrew J. Blumberg, David Gepner, Michael J. Hopkins, and Charles Rezk,
An 8-categorical approach to R-line bundles, R-module Thom spectra, and twisted R-homology,
arXiv:1403.4325.
M. F. Atiyah, R. Bott, and A. Shapiro, Clifford modules, Topology 3 (1964), no. suppl. 1, 3–38.
D. W. Anderson, Universal coefficient theorems for K-theory. mimeographed notes, University of California at Berkeley, 1969.
M. F. Atiyah, V. K. Patodi, and I. M. Singer, Spectral asymmetry and Riemannian geometry. I, Math.
Proc. Cambridge Philos. Soc. 77 (1975), 43–69.
David Ayala, Geometric cobordism categories, ProQuest LLC, Ann Arbor, MI, 2009. Thesis (Ph.D.)–
Stanford University.
FJ Burnell, Xie Chen, Lukasz Fidkowski, and Ashvin Vishwanath, Exactly Soluble Model of a 3D Symmetry Protected Topological Phase of Bosons with Surface Topological Order, arXiv:1302.7072.
John C. Baez and James Dolan, Higher-dimensional algebra and topological quantum field theory,
J. Math. Phys. 36 (1995), no. 11, 6073–6105, arXiv:q-alg/9503002.
C. Blanchet, N. Habegger, G. Masbaum, and P. Vogel, Topological quantum field theories derived from
the Kauffman bracket, Topology 34 (1995), no. 4, 883–927.
Xie Chen, Lukasz Fidkowski, and Ashvin Vishwanath, Symmetry Enforced Non-Abelian Topological Order
at the Surface of a Topological Insulator, Phys. Rev. B 89 (2014), 165132, 1306.3250.
Xie Chen, Zheng-Cheng Gu, Zheng-Xin Liu, and Xiao-Gang Wen, Symmetry protected topological orders and the cohomology class of their symmetry group, Phys.Rev. B87 (2013), 155114,
arXiv:1106.4772 [cond-mat.str-el].
Xie Chen, Zheng-Cheng Gu, and Xiao-Gang Wen, Local unitary transformation, long-range quantum
entanglement, wave function renormalization, and topological order, Phys. Rev. B 82 (2010), 155138,
arXiv:1004.3835.
Xie Chen, Zheng-Cheng Gu, and Xiao-Gang Wen, Complete classification of one-dimensional
gapped quantum phases in interacting spin systems, Physical Review B 84 (2011), no. 23, 235128,
arXiv:1103.3323.
Xie Chen, Zheng-Xin Liu, and Xiao-Gang Wen, Two-dimensional symmetry-protected topological orders and their protected gapless edge excitations, Physical Review B 84 (2011), no. 23, 235141,
arXiv:1106.4752.
Pierre Deligne, Pavel Etingof, Daniel S. Freed, Lisa C. Jeffrey, David Kazhdan, John W. Morgan,
David R. Morrison, and Edward Witten (eds.), Quantum fields and strings: a course for mathematicians.
Vol. 1, 2, American Mathematical Society, Providence, RI, 1999. Material from the Special Year on
Quantum Field Theory held at the Institute for Advanced Study, Princeton, NJ, 1996–1997.
Pierre Deligne and Daniel S. Freed, Classical field theory, Quantum Fields and Strings: a course for
mathematicians, Vol. 1, 2 (Princeton, NJ, 1996/1997), Amer. Math. Soc., Providence, RI, 1999, pp. 137–
225.
Jacques Distler, Daniel S. Freed, and Gregory W. Moore, Spin structures and superstrings, Surveys in
differential geometry. Volume XV. Perspectives in mathematics and physics, Surv. Differ. Geom., vol. 15,
Int. Press, Somerville, MA, 2011, pp. 99–130. arXiv:0906.0795.
Christopher L. Douglas and André G. Henriques, Topological modular forms and conformal nets, Mathematical foundations of quantum field theory and perturbative string theory, Proc. Sympos. Pure Math.,
vol. 83, Amer. Math. Soc., Providence, RI, 2011, pp. 341–354. arXiv:1103.4187.
Robbert Dijkgraaf and Edward Witten, Topological gauge theories and group cohomology, Comm. Math.
Phys. 129 (1990), no. 2, 393–429.
H. Endo, M. Korkmaz, D. Kotschick, B. Ozbagci, and A. Stipsicz, Commutators, Lefschetz fibrations
and the signatures of surface bundles, Topology 41 (2002), no. 5, 961–977, arXiv:math/0103176.
Daniel S. Freed, The cobordism hypothesis, Bull. Amer. Math. Soc. (N.S.) 50 (2013), no. 1, 57–92,
arXiv:1210.5100.

<!-- page 58 -->
58

[F2]

[F3]
[F4]
[F5]
[FG]
[FH]
[FHT]
[FK]
[FM1]
[FM2]
[FMS]
[FQ]
[FT]
[G]
[GJ]
[GMTW]
[GW]
[Ha]
[HeSt]
[HS]
[HW]
[J]
[K1]
[K2]
[K3]
[K4]
[K5]
[K6]
[Ka1]
[Ka2]
[KT]
[KTTW]

D. S. FREED

, Characteristic numbers and generalized path integrals, Geometry, topology, & physics,
Conf. Proc. Lecture Notes Geom. Topology, IV, Int. Press, Cambridge, MA, 1995, pp. 126–138.
arXiv:dg-ga/9406002.
, Bordism: Old and New. http://www.ma.utexas.edu/users/dafr/M392C/index.html.
, Pions and generalized cohomology, J. Differential Geom. 80 (2008), no. 1, 45–77,
arXiv:hep-th/0607134.
, Anomalies and invertible field theories, arXiv:1404.7224.
Daniel S. Freed and Robert E. Gompf, Computer calculation of Witten’s 3-manifold invariant, Comm.
Math. Phys. 141 (1991), no. 1, 79–117.
Daniel S. Freed and Michael J. Hopkins, Chern-Weil forms and abstract homotopy theory,
Bull. Amer. Math. Soc. (N.S.) 50 (2013), no. 3, 431–468, arXiv:1301.5959.
Daniel S. Freed, Michael J. Hopkins, and Constantin Teleman, Consistent orientation of moduli spaces ,
The many facets of geometry, Oxford Univ. Press, Oxford, 2010, pp. 395–419. arXiv:0711.1909.
Lukasz Fidkowski and Alexei Kitaev, Topological phases of fermions in one dimension,
Phys. Rev. B 83 (2011), 075103, arXiv:1008.4138.
Daniel S. Freed and Gregory W. Moore, Setting the quantum integrand of M-theory,
Commun. Math. Phys. 263 (2006), 89–132, arXiv:hep-th/0409135.
,
Twisted equivariant matter,
Ann. Henri Poincaré 14 (2013),
no. 8,
1927–2023,
arXiv:1208.5055.
Daniel S. Freed, Gregory W. Moore, and Graeme Segal, The uncertainty of fluxes,
Commun. Math. Phys. 271 (2007), 247–274, arXiv:hep-th/0605198.
Daniel S. Freed and Frank Quinn, Chern-Simons theory with finite gauge group, Comm. Math. Phys.
156 (1993), no. 3, 435–472, arXiv:hep-th/911100.
Daniel S. Freed and Constantin Teleman, Relative quantum field theory, Comm. Math. Phys. 326 (2014),
no. 2, 459–476, arXiv:1212.1692.
Sam Gunningham, Spin Hurwitz numbers and topological quantum field theory, arXiv:1201.1273.
James Glimm and Arthur Jaffe, Quantum physics, second ed., Springer-Verlag, New York, 1987. A
functional integral point of view.
Søren Galatius, Ulrike Tillmann, Ib Madsen, and Michael Weiss, The homotopy type of the cobordism
category, Acta Math. 202 (2009), no. 2, 195–239, arXiv:math/0605249.
Zheng-Cheng Gu and Xiao-Gang Wen, Symmetry-protected topological orders for interacting fermions—
fermionic topological non-linear σ-models and a group super-cohomology theory, 1201.2648.
Allen Hatcher, Algebraic topology, Cambridge University Press, Cambridge, 2002.
Drew Heard and Vesna Stojanoska, K-theory, reality, and duality, 1401.2581.
M. J. Hopkins and I. M. Singer, Quadratic functions in geometry, topology, and M-theory, J. Diff. Geom.
70 (2005), 329–452, arXiv:math/0211216.
Ling-Yan Hung and Xiao-Gang Wen, Universal symmetry-protected topological invariants for symmetryprotected topological states, Phys. Rev. B 89 (2014), arXiv:1311.5539.
J. A. Jenquin, Spin Chern-Simons and spin TQFTs, arXiv:math/0605239.
Alexei
Kitaev,
Periodic
table
for
topological
insulators
and
superconductors,
AIP Conf.Proc. 1134 (2009), 22–30, arXiv:0901.2686 [cond-mat.mes-hall].
, Toward Topological Classification of Phases with Short-range Entanglement, 2011.
http://online.kitp.ucsb.edu/online/topomat11/kitaev/. Lecture at KITP.
,
On
the
Classification
of
Short-Range
Entangled
States,
June,
2013.
http://scgp.stonybrook.edu/archives/7874. Lecture at SCGP.
, Short range entangled quantum states, May, 2014. lecture at MSRI.
, Anyons in an exactly solved model and beyond, Annals of Physics 321 (2006), no. 1, 2–111,
arXiv:cond-mat/0506438.
, Unpaired Majorana fermions in quantum wires, Physics-Uspekhi 44 (2001), no. 10S, 131,
arXiv:cond-mat/0010440.
Anton Kapustin, Symmetry Protected Topological Phases, Anomalies, and Cobordisms: Beyond Group
Cohomology, 1403.1467.
, Bosonic Topological Insulators and Paramagnets: a view from cobordisms, 1404.6659.
Anton Kapustin and Ryan Thorngren, Anomalies of discrete symmetries in various dimensions and
group cohomology, 1404.3230.
Anton Kapustin, Ryan Thorngren, Alex Turzillo, and Zitao Wang, Fermionic symmetry protected topological phases and cobordisms, arXiv:1406.7329.

<!-- page 59 -->
SHORT RANGE ENTANGLEMENT AND INVERTIBLE FIELD THEORIES

[L]
[Li]
[LV]
[MaWe]
[Mi]
[MT]
[MW]
[PMN]
[S1]
[S2]
[Sp]
[St]
[Ta]
[Th]
[VS]

[W1]
[W2]
[W3]

[W4]

[W5]
[Wa]
[We]
[WGW]

[Wi]
[WPS]
[WS]

59

Jacob Lurie, On the classification of topological field theories, Current developments in mathematics,
2008, Int. Press, Somerville, MA, 2009, pp. 129–280. arXiv:0905.0465.
Arunas Liulevicius, A theorem in homological algebra and stable homotopy of projective spaces, Trans.
Amer. Math. Soc. 109 (1963), 540–552.
Yuan-Ming Lu and Ashvin Vishwanath, Theory and classification of interacting integer topological phases
in two dimensions: A Chern-Simons approach, Phys. Rev. B 86 (2012), 125119, arXiv:1203.3156.
Ib Madsen and Michael Weiss, The stable moduli space of Riemann surfaces: Mumford’s conjecture,
Ann. of Math. (2) 165 (2007), no. 3, 843–941, arXiv:math/0212321.
John W. Milnor, Topology from the differentiable viewpoint, Based on notes by David W. Weaver, The
University Press of Virginia, Charlottesville, Va., 1965.
Ib Madsen and Ulrike Tillmann, The stable mapping class group and QpCP8
` q, Invent. Math. 145 (2001),
no. 3, 509–544.
Scott Morrison and Kevin Walker, Higher categories, colimits, and the blob complex,
Proc. Natl. Acad. Sci. USA 108 (2011), no. 20, 8139–8145, arXiv:1108.5386.
Eugeniu Plamadeala, Michael Mulligan, and Chetan Nayak, Short-Range Entangled Bosonic States with
Chiral Edge Modes and T -duality of Heterotic Strings, Phys. Rev. B 88 (2013), 045131, 1304.0772.
Graeme Segal, The definition of conformal field theory, Topology, geometry and quantum field theory,
London Math. Soc. Lecture Note Ser., vol. 308, Cambridge Univ. Press, Cambridge, 2004, pp. 421–577.
, Felix Klein Lectures 2011. http://www.mpim-bonn.mpg.de/node/3372/abstracts.
Edwin H. Spanier, Algebraic topology, Springer-Verlag, New York, 1981. Corrected reprint.
James D. Stasheff, Continuous cohomology of groups and classifying spaces, Bull. Amer. Math. Soc. 84
(1978), no. 4, 513–530.
Terence Tao, Compactness and contradiction, American Mathematical Society, Providence, RI, 2013.
René Thom, Quelques propriétés globales des variétés différentiables, Comment. Math. Helv. 28 (1954),
17–86.
Ashvin Vishwanath and T Senthil, Physics of three-dimensional bosonic topological insulators: surfacedeconfined criticality and quantized magnetoelectric effect, Physical Review X 3 (2013), no. 1, 011016,
arXiv:1209.3058.
Edward Witten, Quantum field theory and the Jones polynomial, Comm. Math. Phys. 121 (1989), no. 3,
351–399.
, Dynamics of quantum field theory, Quantum fields and strings: a course for mathematicians,
Vol. 1, 2 (Princeton, NJ, 1996/1997), Amer. Math. Soc., Providence, RI, 1999, pp. 1119–1424.
, The Verlinde algebra and the cohomology of the Grassmannian, Geometry, topology, & physics,
Conf. Proc. Lecture Notes Geom. Topology, IV, Int. Press, Cambridge, MA, 1995, pp. 357–422.
arXiv:hep-th/9312104.
,
The
Chern-Simons
functional
in
condensed
matter
physics.
http://videostreaming.gc.cuny.edu/videos/video/792/in/channel/55/. Lecture at CUNY graduate center, May, 2013.
, On holomorphic factorization of WZW and coset models, Comm. Math. Phys. 144 (1992), no. 1,
189–212.
K. Walker, TQFTs. http://canyon23.net/math/tc.pdf.
Xiao-Gang Wen, Symmetry-protected topological invariants of symmetry-protected topological phases of
interacting bosons and fermions, Phys. Rev. B 89 (2014), arXiv:1301.7675.
Juven Wang, Zheng-Cheng Gu, and Xiao-Gang Wen, A field theory representation of pure gauge
and mixed gauge-gravity symmetry-protected topological invariants, group cohomology and beyond,
arXiv:1405.7689.
David Wigner, Algebraic cohomology of topological groups, Trans. Amer. Math. Soc. 178 (1973), 83–93.
Chong Wang, Andrew C Potter, and T Senthil, Classification of interacting electronic topological insulators in three dimensions, Science 343 (2014), no. 6171, 629–631, arXiv:1306.3238.
Chong Wang and T Senthil, Interacting fermionic topological insulators/superconductors in 3D,
arXiv:1401.1142.

Department of Mathematics, University of Texas, Austin, TX 78712
E-mail address: dafr@math.utexas.edu
