---
type: paper
date: 2016-04-22
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1604.06527v6)
reviewed: false
---

# Reflection positivity and invertible topological phases

Machine-generated and unreviewed text extraction of arXiv:1604.06527v6
(141 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1604.06527v6>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

arXiv:1604.06527v6 [hep-th] 18 Dec 2022

DANIEL S. FREED AND MICHAEL J. HOPKINS
Abstract. We implement an extended version of reflection positivity (Wick-rotated unitarity) for
invertible topological quantum field theories and compute the abelian group of deformation classes
using stable homotopy theory. We apply these field theory considerations to lattice systems, assuming the existence and validity of low energy effective field theory approximations, and thereby
produce a general formula for the group of Symmetry Protected Topological (SPT) phases in terms
of Thom’s bordism spectra; the only input is the dimension and symmetry type. We provide computations for fermionic systems in physically relevant dimensions. Other topics include symmetry in
quantum field theories, a relativistic 10-fold way, the homotopy theory of relativistic free fermions,
and a topological spin-statistics theorem.

Contents
1. Introduction
2. Symmetry groups in relativistic quantum field theory
2.1. Stabilization of Wick-rotated symmetry groups
2.2. Curved manifolds and bordism categories with Hn -structure
3. Unitarity and Wick rotation
3.1. Wick rotation in quantum mechanics
3.2. Reflection positivity in Euclidean quantum field theory
pn
3.3. The extended symmetry group H
4. Reflection symmetry on manifolds
4.1. An involution on Hn -manifolds
4.2. Duals and opposites
4.3. Reflection structures and positivity
4.4. Doubles
5. Invertible topological field theories and stable homotopy theory
5.1. Extended field theories
5.2. Invertible topological field theories
5.3. Universal targets
5.4. Remarks on non-topological invertible theories and low energy approximations
6. Equivariant stable homotopy theory
6.1. Spectra
6.2. Borel equivariant stable homotopy theory
6.3. Real structures
7. Reflection structures and stability
7.1. Madsen-Tillmann and Thom spectra
7.2. Naive positivity and stability
7.3. H-type theories

2
9
9
15
18
18
19
21
25
26
27
28
29
31
32
33
35
37
39
39
43
48
55
55
58
62

Date: December 18, 2022.
This material is based upon work supported by the National Science Foundation under Grant Numbers DMS1207817, DMS-1160461, DMS-1510417, and DMS-1158983. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National
Science Foundation. We thank the Aspen Center for Physics for hosting our very productive working group. The
first author also thanks the Institute for Advanced Study through the Wolfensohn Fund for providing a stimulating
environment for parts of this work.
1

<!-- page 2 -->
2

D. S. FREED AND M. J. HOPKINS

8. Positivity in extended invertible topological theories
8.1. Spaces of invertible field theories, extended positivity, and stability
8.2. Proof of Theorem 8.20
8.3. Transfers
9. Fermionic theories with scalar internal symmetry group
9.1. Symmetry groups of fermionic systems
9.2. Free fermions and twisted Dirac operators
9.3. Phases of topological insulators and topological superconductors
10. Computations
11. A topological spin-statistics theorem
Appendix A. The CRT theorem for general symmetry types
A.1. Pin groups and pin manifolds
A.2. Lorentz signature symmetry groups
A.3. Wick rotation and the CRT theorem
Appendix B. Involutions on categories and duality
Appendix C. Noncompact Wick-rotated vector symmetry groups
Appendix D. Computations with A1 -modules
D.1. Cell diagrams
D.2. The charts
D.3. The cases s “ ˘1
D.4. The case s “ 4
D.5. The case s “ ˘2
D.6. The case s “ ˘3
p n via classifying spaces
Appendix E. Construction of H
E.1. Preliminary
p npmq
E.2. A family of spaces B H
pmq
pn
E.3. The Lie groups H
References

63
63
70
72
75
76
78
90
96
105
106
107
109
112
116
119
120
120
122
123
123
127
130
133
134
134
136
137

1. Introduction
The moduli space, or stack, of a geometric object with fixed discrete invariants is a central
object of interest in geometry. A typical example is the moduli stack of Riemann surfaces of fixed
genus. Here the underlying topological space is connected, but moving up to complex dimension
two the moduli stack of complex surfaces of general type with fixed Euler number and signature
is not necessarily connected. It has finitely many components [Ca], so there are finitely many
deformation types. If singular objects are permitted, then sometimes connectivity can be restored.
For example, Reid [Re] speculates that the moduli stack of three-dimensional Calabi-Yau varieties
is connected if one allows certain singularities. To illustrate further, consider the moduli stack of
one-dimensional Riemannian manifolds. If we allow simple singularities, such as the figure eight,
then we can connect a single circle to two circles by a path (standard Morse function on a twodimensional torus). We can also connect one circle to two circles if we allow noncompact smooth
manifolds: elongate a circle to an ellipse to two lines and then each line to a circle. On the other
hand, the set of path components of the moduli stack of smooth closed Riemannian 1-manifolds is
isomorphic to Zě0 ; the isomorphism maps a 1-manifold to the cardinality of π0 .

<!-- page 3 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

3

In theoretical physics one contemplates moduli stacks of quantum systems with fixed discrete
invariants, such as dimension and symmetry type. If we remove the singular locus of phase transitions, then path components of the moduli stack are identified with phases of the quantum system.1
In condensed matter physics the quantum systems are modeled discretely, using lattices, and the
classification of phases is an active topic of current interest. As far as we know there is not a robust
mathematical theory of lattice systems and their moduli which leads to rigorous computations of
sets of phases. Quantum field theories also exhibit phases and phase transitions, and those too are
topical. Physicists often pass back and forth between lattice models and field theories using various
mechanisms. In this paper we envision passing from a lattice system to an effective low-energy field
theory using two heuristic principles to argue that the set of phases is conserved:
(i) the deformation class of a quantum system is determined by its low energy behavior;
(ii) the low energy physics of a gapped 2 system is well-approximated by a topological 3 field theory.
A stronger version of (i) asserts that the entire homotopy type of the moduli stack is determined
by the low energy behavior. These two principles are applied by physicists to quantum systems of
all kinds: condensed matter systems, quantum field theories, string theories. For discrete lattice
systems we also assume an emergent low energy relativistic symmetry. We remark that fracton
models [NH] are thought not to satisfy (ii), nor to have any sort of emergent relativistic symmetry,
but those are not relevant here. The lattice models that motivate this paper belong to a special
class, often called short-range entangled, for which the long-range effective topological field theory
is invertible. In particular, there is a unique ground state for the lattice model on any compact
manifold. Early discussions of this property may be found in [CGW, K1]. (Now ‘invertible’ is used
in place of ‘short-range entangled’ to describe the lattice model.)
One reason to pass to continuum models is that there is a mathematical Axiom System for
Wick-rotated quantum field theory; it encodes the structural properties of correlation functions
and linear spaces of quantum states. It was first introduced in the mid 1980’s for scale-independent
theories: by Segal [Se1] for 2-dimensional conformal field theories and later by Atiyah [A1] for
topological field theories. With modifications these axioms are now believed to be relevant to scaledependent theories as well. In this framework a quantum field theory is a linear representation of a
bordism category. The latter categorifies Thom’s bordism groups [T], and a field theory categorifies
integer-valued bordism invariants, such as the signature of a compact oriented manifold.
The twin pillars of quantum field theory are locality and unitarity. These fundamental properties
persist after Wick rotation: locality manifests as factorization laws for correlation functions and
unitarity manifests as reflection positivity. Locality is encoded in the Axiom System using composition of morphisms: gluing bordisms along codimension one submanifolds. In the early 1990’s,
especially motivated by 3-dimensional Chern-Simons theory, an extended notion of locality was
1There is a tight analogy with the example of Riemannian 1-manifolds above: a figure eight corresponds to a
first-order phase transition, while a noncompact manifold corresponds to a higher-order phase transition.
2A quantum mechanical system is gapped if its minimum energy is an eigenvalue of finite multiplicity of the
Hamiltonian, assumed bounded below, and is an isolated point of the spectrum. For quantum field theory ‘spectrum’
means the spectrum of representations of the translation group of Minkowski spacetime. For lattice systems the
spectral gap must be bounded below independent of the lattice size.
3We allow a topological field theory tensored with a non-topological invertible field theory; see §5.4. A field theory
is topological if it does not depend on any continuously varying (background) fields, such as a metric or conformal
structure. We give a precise definition of a topological field theory in §2.2.

<!-- page 4 -->
4

D. S. FREED AND M. J. HOPKINS

introduced by gluing bordisms with corners along higher codimension submanifolds, and this led
naturally to formulations involving higher categories; see [F1, La, BD, L], for example. Extended
locality is a characteristic feature of both physical and mathematical applications of field theory,
whereas unitarity is often not present in purely mathematical contexts. Unitarity in field theory, or
rather its Wick-rotated manifestation—reflection positivity—is the first main subject of this paper.
It is straightforward to implement reflection positivity in the non-extended Axiom System. A natural question arises: What is the extended notion of reflection positivity that goes with extended
locality? We offer a solution in a very special case: invertible topological field theories. These
theories can be studied using stable homotopy theory [FHT1], and indeed we define4 a theory of
this type as a map of spectra. Spectra are the main characters in stable homotopy theory, a mathematical field that partly grew out of Thom’s work. The domain of an invertible topological field
theory is a Madsen-Tillmann bordism spectrum, and our main result tells that extended reflection
positivity brings us full circle to the bordism spectra introduced by Thom in his thesis [T].
Theorem 1.1. There is a 1:1 correspondence

(1.2)

$
,
&deformation classes of reflection positive
.
invertible n-dimensional extended topological – rM T H, Σn`1 IZp1qstor .
%
field theories with symmetry group Hn

The right hand side is the torsion subgroup of homotopy classes of maps from a Thom spectrum to
a shift of the Anderson dual to the sphere spectrum. There are standard computational techniques
which we employ in the latter part of this paper to illustrate the efficacy of the theorem. Often
field theories are classified by enumerating lagrangians with specified background and fluctuating
fields that are consistent with a given symmetry group. By contrast, Theorem 1.1 is a direct
quantum classification of correlation functions and state spaces, as encoded by the Axiom System.
The only inputs are the discrete invariants: the spacetime dimension n and the Wick-rotated
vector symmetry group5 Hn . We prove Theorem 1.1 in §8 as a corollary of a more general result
(Theorem 8.20). There is a related assertion which remains conjectural in this paper: the abelian
group of deformation classes of all reflection positive invertible field theories, including those that
are not topological, is obtained by simply omitting ‘tor’ on the right hand side of (1.2). We make
some comments about this generalization in §5.4 and Remark 8.41; we use it in the computations
of §9. More to the point, we introduce “continuous invertible topological field theories” as a
substitute for invertible non-topological theories, and prove theorems for those.6 We remark that
for general reasons nontorsion only arises if the spacetime dimension n is odd.
We apply Theorem 1.1 to compute the abelian group of phases of invertible lattice systems with
fixed dimension and symmetry type. This implicitly assumes that every possible deformation class
of invertible topological theory can be realized by a lattice model, something not implied by the
4A better starting point is the topological version of the Axiom System, and then Theorem 5.12 brings us to

stable homotopy theory. But as the literature is still in flux we opt for Ansatz 5.14 instead; see the remarks following
Theorem 5.12.
5The basic case is H “ SO . In general there is a homomorphism ρ : H Ñ O whose image includes SO ; the
n
n
n
n
n
n
kernel consists of internal global symmetries. There is a unique associated stable symmetry group H independent of
dimension, as we prove in Theorem 2.19.
6We thank Peter Teichner for his encouragement to adopt this point of view.

<!-- page 5 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

5

heuristic principles (i) and (ii) above. We emphasize the algorithmic nature of our classification:
given a spacetime dimension n and a symmetry group Hn the right hand side of (1.2) is the group
of topological phases and is computable. We provide concrete evidence for this application of Theorem 1.1: in §9.3 we undertake detailed computations for some fermionic systems and compare to
results in the physics literature, the latter derived by means of physical arguments. Some readers
may wish to examine our tables of computations before tackling the more theoretical parts of the
paper. In unpublished work Kitaev [K1, K2, K3] develops a classification of invertible phases based
on microscopic considerations, and he too is led to stable homotopy theory and results consonant
with our effective field theory classification. Kapustin [Ka1] initiated computations of topological
phases via character groups of bordism groups, and he used them and subsequent computations,
for example [KTTW], as phenomenological evidence for a general classification along these lines.
Gaiotto-Kapustin [GK], following on Gu-Wen [GW], show that some invertible fermionic phases defined by lattice models are characterized by spin bordism groups; see also Brumfiel-Morgan [BrMo].
Campbell [C] and Guo-Putrov-Wang [GPW] carry out computations for other bosonic and fermionic
cases of interest, providing further affirmative checks against the condensed matter literature.
A second subject of this paper, after extended reflection positivity, is the study of symmetry
groups in relativistic quantum field theory, and that is where we begin in §2. Our starting point is
a theory on n-dimensional Minkowski spacetime with global symmetry group H1,n´1 , after dividing
out by translations. The analytic continuations of correlation functions, which exist as a consequence of positivity of energy, are invariant under the complex Lie group Hn pCq, and the entire
Wick-rotated theory is symmetric under the compact real form Hn Ă Hn pCq that appears on the
left hand side of (1.2). In an appendix §A.3 we discuss Wick rotation and the CRT theorem7 for
general symmetry types. We use the rigidity of compact Lie groups to constrain possible symmetry
groups (Theorem 2.7) à la Coleman-Mandula [CM]. One key result in this section (Theorem 2.19)
is the existence and uniqueness of a stabilization H, which is the group in the Thom spectrum
on the right hand side of (1.2). When we move to curved Riemannian manifolds—i.e., couple
the theory to background gravity—the symmetry becomes infinitesimal in the sense of Cartan: an
Hn -structure on the tangent bundle. In §3 we formulate reflection symmetry in terms of a group
extension
(1.3)

p n ÝÑ t˘1u ÝÑ 1;
1 ÝÑ Hn ÝÑ H

p n zHn are a Wick-rotated analog of anti-unitary symmetries in quantum mechanics.
elements in H
p n and the group extension (1.3) in Appendix E.) We use this
(We give a topological account of H
extension in §4.1 to define an involution on the bordism category of Hn -manifolds. In the basic
case Hn “ SOn the involution is orientation-reversal; our uniform treatment gives analogs for
any symmetry group. For example, fermionic theories with time-reversal symmetry (and no other
symmetry) have Hn “ Pin˘
n : the involution takes a pin structure to its “w1 -flipped” pin structure.
Topological field theories are independent of the Riemannian metric, so we can replace Hn by a
noncompact analog, which we construct in Appendix C.
7There is a subtlety concerning double covers of the Lorentz signature isometry group, uncovered in [GT], which

we explicate in the context of Wightman quantum field theory for general symmetry types; see §A.2.

<!-- page 6 -->
6

D. S. FREED AND M. J. HOPKINS

Three basic lessons we learned about reflection positivity: (i) ‘reflection’ and ‘positivity’ are
distinct; (ii) ‘reflection’ is a structure whereas ‘positivity’ is a condition; and (iii) ‘extended positivity’ is a structure, not a condition. In the Axiom System a field theory is defined to be a
homomorphism—a symmetric monoidal functor—
(1.4)

F : Bordxn´1,ny pHn q ÝÑ VectC

from the bordism category to the category of complex vector spaces and linear maps. A reflection structure (§4.3) is equivariance data for F with respect to the generalized orientation-reversal
involution on Bordxn´1,ny pHn q and the involution of complex conjugation on VectC . (We briefly
review involutions on categories and equivariant functors in Appendix B.) A reflection structure
induces a hermitian metric on the vector space of states attached to an pn ´ 1q-manifold, and positivity is the condition that these hermitian structures be positive definite. Analogous to reflection
positivity in Euclidean space (§3.2) we see that the partition function of the double of a manifold
with boundary must be positive in order that a reflection structure be positive. Our treatment of
this material using general symmetry groups means it applies to all theories, including those with
time-reversal symmetry and fermions which, after Wick rotation, involve nonorientable manifolds
with pin structure.
To proceed to extended field theories we specialize in §5 to the invertible case. (Invertible field
theories were first singled out in [FM2] in an application to string theory.) In §5.2 we review how
invertibility catalyzes a transition to stable homotopy theory: the analog of (1.4) for an invertible
topological field theory is a map of spectra
(1.5)

F : Σn M T Hn ÝÑ I.

The domain is the invertible quotient of a higher bordism category, a Madsen-Tillmann spectrum.
There is freedom to choose the codomain spectrum, and in §5.3 we introduce two universal choices.
The first is (a shift of) ICˆ , a “character dual” to the sphere spectrum, which is used to track
topological theories on the nose: theories with unequal partition functions are distinct. The second
universal target spectrum is (a shift of) the Anderson dual IZp1q to the sphere spectrum. It
tracks deformation classes of invertible theories rather than individual theories. Significantly, in
the spirit of “derived geometry”, maps into IZp1q classify deformation classes of invertible theories
that are not necessarily topological; the topological theories have finite order in the abelian group
of homotopy classes of maps. For the application to topological phases one should include the nontopological theories, as they incorporate nonzero thermal Hall response. An example is Kitaev’s
E8 phase [K5]. See §5.4 for a general discussion, including an interpretation of maps into IZp1q
as a continuous invertible topological field theory. In this paper we only use non-topological field
theories heuristically and posit that their deformation classes are encoded in continuous topological
field theories, which we treat rigorously.
The main arguments about extended positivity occur in §6–§8. Madsen-Tillmann spectra filter
Thom spectra, which leads to a notion of a stable invertible topological field theory: a map out of
a Thom spectrum. For invertible theories a reflection structure is a lift of (1.5) to an equivariant
map of Z{2-equivariant spectra. Section 6 begins with a brief exposition of spectra and Borel

<!-- page 7 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

7

equivariant stable homotopy theory, sufficient for the considerations in this paper. The involution
on the domain that models generalized orientation-reversal is straightforward to construct from
the group extension (1.5). On the other hand, it is not clear a priori how to model complex
conjugation on the codomain, so in §6.3 we give an extended discussion motivating our choice,
Definition 6.30. We conclude §6 by introducing spectra and spaces of “higher super lines”, including
Hermitian structures and a higher notion of positivity (Definition 6.41, Definition 6.45). There is a
basic link between non-extended positivity and stability, which we establish in Theorem 7.22 and
Theorem 7.30 using obstruction theory arguments. This results in an intermediate classification
(Corollary 7.33) of invertible topological theories with reflection structure satisfying non-extended
positivity. We undertake a more systematic study in §9. There we define extended positivity for
invertible field theories in terms of higher super lines and their embellishments. We give an intuitive
construction of the space of invertible reflection positive theories, and then we identify its homotopy
type in Theorem 8.20, whose proof occupies the second half of §6. Theorem 1.1 is a corollary.
The third main subject of this paper is what might be called the homotopy theory of relativistic
free fermions.8 There are two distinct scenarios in which a free fermion field theory gives rise to a
deformation class of n-dimensional reflection positive invertible theories. First scenario: an pn ´ 1qdimensional free fermion theory has an associated n-dimensional invertible anomaly theory, which
is not necessarily topological; our concern here is its deformation class.9 Second scenario: an ndimensional massive free fermion theory has a long-range effective invertible topological field theory
approximation, according to the general principle (ii) invoked above, applied to a quantum field
theory rather than a lattice system. We sketch the first scenario in some detail in §9.2, culminating
in a formula (Conjecture 9.70) for the deformation class of the anomaly theory. Since massive free
fermions have trivial anomaly, the starting point is the group of free fermionic data under direct sum
modulo massive free fermionic data. The existence of a mass term has a meaning in terms of Clifford
modules (Lemma 9.55), and this produces an identification of the quotient as a homotopy group of
the KO-theory spectrum (Theorem 9.63). The formula for the deformation class of the associated
anomaly theory is, conjecturally, a product of the Atiyah-Bott-Shapiro map [ABS] with the KOtheory class of the spinor data, followed by a Pfaffian map (Conjecture 9.70). In this paper we
provide a detailed sketch of these ideas; we hope to give a thorough mathematical treatment in the
future. There is a huge literature on relativistic free fermion field theories and associated anomalies;
the recent paper [W1], which describes several particular cases in detail, provided motivation and
guidance for the general story here. By contrast, we only comment briefly (§9.2.6) on the second
scenario, beginning from a massive n-dimensional free fermion theory, enough to show that the
starting and ending data match those in the first scenario. In fact, it is this second scenario that
is relevant to this paper, and in particular the conjecture (9.75) about its low energy effective field
theory is used in the computations which follow.
To enable detailed comparisons with the physics literature we carry out the discussion of relativistic free fermions for 10 cases simultaneously. To enumerate them we resume group theoretical
arguments in §9.1 to classify relativistic symmetry groups whose internal subgroup is the unit reals t˘1u, unit complexes T, or unit quaternions SU2 . Restricting to fermionic theories in which
p´1qF embeds in this internal subgroup—which implements the “spin/charge relation” [SeWi]—we
8A free fermion field theory is neither topological nor invertible, but it has an associated invertible field theory.
9The anomaly theory lies in differential KO-theory, whereas its deformation class lies in topological KO-theory.

<!-- page 8 -->
8

D. S. FREED AND M. J. HOPKINS

obtain the 10 groups in question. They include Spin, Pin˘ , and semidirect products with the various unit scalars. This “relativistic 10-fold way” is a variation on the nonrelativistic case, which is
described in many works: a sample includes [D, AZ, HHZ, K6, SRFL, FM1, KZ, WS]. Remark 9.32
provides a link to this condensed matter literature: we compute a group I of symmetries that preserve points of space in a nonrelativistic setting. It is this group I which acts at each lattice site in a
discrete model, and it can be used to compare to the ubiquitous symmetry tables for fermion lattice
systems. Our uniform treatment is based on Lemma 9.27, which embeds each symmetry group in a
Clifford algebra. Usual constructions with Clifford modules—the Atiyah-Bott-Shapiro-Thom class,
Dirac operators and their indices—then generalize easily. There is a purely geometric application
that we do not pursue here: index theory on pin and pinc manifolds is straightforward using this
embedding.
The results of the homotopy theory computations are reported in §9.3. We provide a table
for each of the 10 fermionic symmetry groups. In each spacetime dimension n ď 5 we compute
the group of free fermion theories (Theorem 9.63), the group of deformation classes of interacting
theories (Theorem 1.1), and the map between them (Conjecture 9.70). We make comparisons with
the condensed matter literature where available and find almost total agreement; in the few cases
with a discrepancy we motivate a reexamination of the physics assertions. In §10 we outline how
the calculations are done and supply Ext charts that encode the E2 -term of the relevant Adams
spectral sequences. The Ext charts also encode the map to KO-theory; in fact, one of the main
tasks in this section is to rewrite the “twisted” Atiyah-Bott-Shapiro maps in a more accessible form.
We provide more explanation of the charts in Appendix D. In that appendix we also illustrate the
use of Margolis homology to derive information from the Adams spectral sequence. Papers by
Campbell [C] and Beaudry-Campbell [BeC] give pedagogical introductions to the Adams spectral
sequence and flesh out the details of our computations. Notice that whereas Theorem 1.1 computes
the group of interacting phases for any symmetry type, the 10 fermionic symmetry types are special
in that there is a notion of a free fermionic phase which does not exist in general. This leads to
a richer application of homotopy theory and a more stringent test against the condensed matter
literature.
The sections of the paper not yet mentioned contain complements or background material. An
analog of the spin-statistics theorem in relativistic quantum field theory holds for reflection positive
invertible topological theories, as we explain in §11. Section A.1 contains a review of pin groups
and Clifford algebras, background for the discussion of the CRT theorem later in Appendix A and
for some of the material in §9.
Beyond the immediate relevance to the study of topological phases, the successful application of
bordism computations to quantum systems is evidence—perhaps the first substantial test against
physics—that the sparse Axiom System initiated by Segal and Atiyah captures essential features
of quantum field theory.
The lecture series [F4] provides additional background and discussion on many of the topics
treated here.
We warmly thank David Ben-Zvi, Jonathan Campbell, Jacques Distler, Mike Freedman, Davide Gaiotto, Zheng-Cheng Gu, Meng Guo, Matt Hastings, Andre Henriques, Anton Kapustin,
Alexei Kitaev, Max Metlitski, Greg Moore, Andy Neitzke, Graeme Segal, Nathan Seiberg, Peter

<!-- page 9 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

9

Teichner, Constantin Teleman, Ulrike Tillmann, Senthil Todadri, Kevin Walker, Xiao-Gang Wen,
Edward Witten, and the anonymous referees for many illuminating conversations, correspondence,
comments, and feedback on the first version of this paper.

2. Symmetry groups in relativistic quantum field theory
The analytic extension of correlation functions, a consequence of positivity of energy, provides
a powerful constraint on symmetry groups. We explore the general structure in §2.1 from the
Wick-rotated point of view. The rigidity of compact Lie groups is the key idea that underlies our
proofs of structure theorems, such as Theorem 2.7. One important result is Theorem 2.19, which
constructs a stable group H from an n-dimensional symmetry group Hn , assuming the spacetime
dimension satisfies n ě 3. In the expository §2.2 we recall the axiomatization of a field theory as
a categorified bordism invariant. We accommodate general symmetry groups on curved manifolds
using reductions of frame bundles, an analog of the passage from Klein’s Erlangen Programm [BB]
to Cartan’s H-structures [S].
2.1. Stabilization of Wick-rotated symmetry groups
The Poincaré group is the connected double cover of the identity component of the isometry
group I1,n´1 of n-dimensional Minkowski spacetime M n . Minkowski spacetime M n is assumed
equipped with a time orientation, a choice of component of timelike vectors in the inner product
Ò
Ă I1,n´1 denote the subgroup of isometries that preserve
space R1,n´1 of translations. Let I1,n´1
the time orientation. Assume n ě 2. Many treatments of quantum field theory, for example those
based on S-matrix theory, begin with the assumption that the Poincaré group is a subgroup of the
(unbroken) global symmetry group H1,n´1 of the theory. Then the Coleman-Mandula theorem [CM]
asserts that on the level of Lie algebras there is a splitting as a direct sum of the Lie algebra of
Poincaré with the Lie algebra of a compact Lie group K. We find it more natural to posit from
Ò
the beginning a homomorphism ρn : H1,n´1 Ñ I1,n´1
. After all, g P H1,n´1 acts on the operators
in the theory, and so on the supports of those operators. For a single point operator, or local
operator, that action is ρn pgq. The relativistic invariance of the theory is the hypothesis that the
Ò
image of ρn contains the identity component of I1,n´1
. Therefore, the image is either the identity
Ò
component or the entire two-component group I1,n´1
. The kernel of ρn is the group K of internal
symmetries—symmetries that fix the points of spacetime. Note that K contains the central element
of the Lorentz group Spin1,n´1 if that element acts effectively, which by the spin-statistics theorem
happens if and only if the theory contains fermionic states. (That element is often denoted ‘p´1qF ’.
Below we deduce in general a central element k0 P K with pk0 q2 “ 1, and it is identified with either
the central element of Spin or the identity element.) The internal symmetry group K is assumed
to be a compact Lie group.10
10The global symmetry group of a “noncompact field theory”, such as for a free massless R-valued scalar field

theory, may be noncompact. Our discussion does not include supersymmetries or higher symmetries.

<!-- page 10 -->
10

D. S. FREED AND M. J. HOPKINS
Ò
Assume the translation subgroup R1,n´1 Ă I1,n´1
lifts to a normal subgroup of H1,n´1 ; see [FM1,

Remark 2.13] for a justification of this hypothesis. Let H1,n´1 denote the quotient of H1,n´1 by
this normal subgroup of translations. There is a short exact sequence11
ρn

Ò
1 ÝÑ K ÝÑ H1,n´1 ÝÝÝÑ O1,n´1

(2.1)

Ò
where the image of ρn contains the identity component of O1,n´1
Ă O1,n´1 , by the relativistic
invariance of the theory. The CRT theorem, reviewed in §A.3, gives a larger symmetry group.
A fundamental consequence of the positivity of energy12 in quantum field theory, also reviewed
in §A.3, is a holomorphic extension13 of correlation functions on which the complexification Hn pCq
of H1,n´1 acts as symmetries. There is an exact sequence
ρn

(2.2)

1 ÝÑ KpCq ÝÑ Hn pCq ÝÝÝÑ On pCq

of complex Lie groups. The Wick-rotated theory has a compact real form Hn of Hn pCq as symmetry
group such that Hn fits into the exact sequence
ρn

(2.3)

1 ÝÑ K ÝÑ Hn ÝÝÝÑ On

of compact Lie groups with the same compact kernel K as in (2.1). The image of this ρn is either On
or SOn , depending on whether the relativistic theory has spatial reflections or not; equivalently, by
the CRT theorem, whether it has time-reversal symmetry or not.
Definition 2.4. The symmetry type of a quantum field theory is a pair pHn , ρn q of a compact Lie
group Hn and a homomorphism ρn : Hn Ñ On whose image contains SOn Ă On . The kernel K of ρn
is called the group of internal symmetries. We require that the anti-Wick rotation to Minkowski
spacetime has a Lorentzian real form (2.1) with compact internal symmetry group K “ ker ρn .
The caveats in footnote 10 apply. See Remark 2.13 below for an example of a pair pHn , ρn q that
does not satisfy the anti-Wick rotation condition. The symmetry type is a basic structure in a
quantum field theory, useful to articulate explicitly in any example.
Ą
Define SHn “ ρ´1
n pSOn q and let SH n be the double cover of SHn constructed from the spin
double cover of SOn . These compact Lie groups are usefully encoded in the pullback diagram
1

(2.5)

1

1
11We overload the symbol ‘ρ

/K

/K

/K

Ąn
/ SH

ρn

/ Spin

n

2:1



/ SHn
_


ρn

1:2

/ Hn

ρn



2:1

/ SOn
_


/1

/1

1:2

/ On

n ’. Here it denotes the homomorphism induced from the previous ρn after modding
out translations. Below we use it for the complexification, restriction to the Euclidean real form, and various lifts.
12The dual to the cone of forward timelike vectors determines the notion of positive energy.
13See [KS] for a geometric version on curved manifolds.

<!-- page 11 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

11

r n as the pullback14
If ρn : Hn Ñ On is surjective, define H
1

/K

rn
/H

1

/K


/ Hn

(2.6)

ρn

ρn

/ Pin`
n

/1


/ On

/1

r n over Spinn Ă Pin` is SH
Ą n . Let k, hn , on denote the Lie algebras of K, Hn , On ,
The restriction of H
n
respectively. The following theorem makes precise the sense in which the entire symmetry group
is nearly the product of (Wick-rotated) spacetime symmetries and internal symmetries. In our
approach to symmetry it plays the role of the Coleman-Mandula theorem.
Theorem 2.7.
–

(1 ) There is a splitting hn – o1n ‘ k, and ρn induces an isomorphism of Lie algebras o1n ÝÝÑ on .
Ą n – Spinn ˆK. Hence there exists a central element k0 P K
(2 ) If n ě 3 there is an isomorphism SH
with pk0 q2 “ 1 and an isomorphism
(2.8)

SHn – Spinn ˆK

L

xp´1, k0 qy,

where xp´1, k0 qy is the cyclic group generated by p´1, k0 q.
(3 ) If n ě 3 and ρn : Hn Ñ On is surjective, then there exists a group extension
(2.9)

1 ÝÑ K ÝÑ J ÝÑ t˘1u ÝÑ 1

and a pullback diagram of group extensions

n

/1


/J


/ t˘1u

/1

L

xp´1, k0 qy.

/K

rn
/H

1

/K

(2.10)

ρn

/ Pin`

1

There is an isomorphism
(2.11)

rn
Hn – H

r n to be a product is encoded in the group extenThe pullback (2.10) shows that the failure of H
sion (2.9), which is independent of n.
Corollary 2.12. There is a canonical homomorphism Spinn Ñ Hn under which the image of the
central element ´1 P Spinn is k0 P K.
14See §A.1 for a review of pin groups.

<!-- page 12 -->
12

D. S. FREED AND M. J. HOPKINS

This homomorphism anti-Wick rotates back to a homomorphism of the Poincaré group into the
total symmetry group H1,n´1 of the relativistic theory, the traditional starting point for discussions
of symmetry in quantum field theory.
Ą 2 is isomorphic to a semidirect product
Remark 2.13. For n “ 2 we can only conclude that SH
of Spin2 and K. An example is SH2 “ SO2 ˙ O2 , where a rotation R P SO2 acts on O2 by the
automorphism that is the identity on SO2 Ă O2 and composes a reflection with R. Alternatively,
´1
SH2 – Z{2Z ˙ pT ˆ Tq where the involution on T ˆ T is pλ1 , λ2 q ÞÑ pλ1 , λ´1
1 λ2 q.
Proof of Theorem 2.7. Split the Lie algebra hn “ rhn , hn s ‘ z, where z Ă hn is the center, and let o1n
be the orthogonal complement of the ideal k X rhn , hn s Ă rhn , hn s with respect to the nondegenerate
Killing form on the semisimple Lie algebra rhn , hn s. Then ρn induces an isomorphism o1n Ñ on ,
Ą n which locally projects
which proves (1). The exponential of o1n is a closed Lie subgroup S Ă SH
Ą n – S ˙ K.
diffeomorphically onto Spinn under ρn , so is isomorphic to Spinn . It follows that SH
We claim this semidirect product is a direct product if n ě 3. To see this observe that conjugation
by s P S induces an automorphism αpsq of K which is the identity on the identity component
K 0 Ă K, since the Lie algebra of S commutes with the Lie algebra of K. Since S is connected, the
induced automorphism of π0 K is also trivial. Hence on each component of K the automorphism αpsq
is left multiplication by an element zpsq P Z 0 in the center of K 0 . (Proof: Write α “ αpsq and
suppose αpkq “ zk for some k in that component and z P K 0 . Any other element of that component
has the form kk0 for k0 P K 0 , and αpkk0 q “ zpkk0 q. But we can also write any element in the
component as k01 k for some k01 P K 0 , and αpk01 kq “ k01 zk “ pk01 zk01 ´1 qpk01 kq from which k01 zk01 ´1 “ z.
This holds for every k01 P K 0 , from which we deduce z P Z 0 .) Next, Spinn acts trivially on Z 0 ;
this follows since the outer automorphism group of a compact Lie group is discrete, every inner
automorphism of the abelian group Z 0 is trivial, and Spinn is connected. Hence the map s ÞÑ zpsq is
a homomorphism S Ñ Z 0 . But if n ě 3 the Lie group S – Spinn has no nontrivial homomorphisms
to an abelian Lie group.
Ąn Ă H
r n is a normal subgroup. Fix h̃ P
Assume ρn : Hn Ñ On is surjective. We claim Spinn Ă SH
`
r
Hn such that ρn ph̃q “ e2 P Pinn . Conjugation by e2 induces an involution α : Spinn Ñ Spinn . It
Ą n – Spinn ˆK defined as conjugation by h̃, so there is an induced
lifts to an automorphism of SH
automorphism β : K Ñ K and a homomorphism γ : Spinn Ñ K.
Lemma 2.14. If n ě 3, then the homomorphism γ is trivial.
r n pCq by pulling back as in (2.6) using the complexified groups (2.2); pullback over
Proof. Define H
r 1,n´1 Ă H
r n pCq Ą H
r n . Note
the Lorentzian real forms to obtain the first of the pair of real forms H
that h̃ lies in each of these groups, and conjugation by h̃ preserves both real forms. Thus we obtain
a homomorphism Spinn pCq Ñ KpCq that restricts to γ : Spinn Ñ K and to a homomorphism
Spin1,n´1 Ñ K. Now if γ is nontrivial, then so is the induced map on Lie algebras, and since on is
simple, γ9 : on Ñ k is injective. It follows that the Lie algebra map o1,n´1 Ñ k is also injective.
Hence k contains a subalgebra isomorphic to o1,2 – sl2 R. The Killing form on k induces a nonzero
semidefinite invariant symmetric bilinear form on the simple Lie algebra sl2 R, which is impossible
since every invariant symmetric form on sl2 R is a multiple of the Killing form, which is indefinite
and nondegenerate.


<!-- page 13 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

13

r n is a normal subgroup. Set J “ H
r n { Spinn . Then (2.10) follows
It follows that Spinn Ă H
r n Ñ Hn equals the kernel of
from (2.6) and (2.11) follows from the fact that the kernel of H
Ą n Ñ SHn . This completes the proof of Theorem 2.7.
SH

Remark 2.15. Lemma 2.14 is not true without using the anti-Wick rotation back to Lorentzian
signature. Namely, let n “ 3 and H3 “ Z{2Z ˙ pSO3 ˆ SO3 q, where the nontrivial element of Z{2Z
acts by shearing pg1 , g2 q ÞÑ pg1 , g1 g2 q; the homomorphism ρ3 that kills the last factor K “ SO3
maps H3 Ñ O3 and sends the generator of Z{2Z to the central element ´1 P O3 . The reader can
check that γ : Spin3 Ñ SO3 is surjective. But H3 is not a possible symmetry group because of the
anti-Wick rotation, as in the proof of Lemma 2.14.
If we restrict the internal symmetry group to only include the image of the central element
´1 P Spinn under Spinn Ñ Hn , then there are five possibilities. In these cases K is trivial
?
or K – t˘1u. Let µ4 “ t˘1, ˘ ´1u be the multiplicative group of fourth roots of unity, and
define En Ă On ˆ µ4 as the subgroup of pA, λq such that det A “ λ2 .
Proposition 2.16. Assume n ě 3. If the internal symmetry group K is trivial, then Hn – SOn
or Hn – On . If K – t˘1u is cyclic of order two, then there are six possibilities for Hn up to
´
isomorphism: SOn ˆ t˘1u, Spinn , On ˆ t˘1u, En , Pin`
n , and Pinn .
Proof. The first statement is clear from the fact that the image of ρn in (2.3) is either SOn or On .
The group extensions by t˘1u are central and are classified up to isomorphism by the cohomology
group H 2 pBSOn ; t˘1uq – Z{2Z or H 2 pBOn ; t˘1uq – Z{2Z ˆ Z{2Z, depending on the image of ρn ,
and it is not difficult to work out what the groups Hn are.

The non-identity element of K in SOn ˆ t˘1u, On ˆ t˘1u, and En is not the image of the central
element ´1 P Spinn . This leaves the five basic symmetry types listed in the following table:

(2.17)

states/symmetry

Hn

K

k0

bosons only
fermions allowed
bosons, time-reversal (T )
fermions, T 2 “ p´1qF
fermions, T 2 “ id

SOn
Spinn
On
Pin`
n
Pin´
n

t1u
t˘1u
t1u
t˘1u
t˘1u

1
´1
1
´1
´1

Appendix A reviews the pin groups and justifies the Wick rotation of time-reversal that leads to
the last three lines in the first column of the table.
The main result in this section is a stabilization of Hn for increasing dimensions, as needed in
Theorem 1.1. Throughout this paper for k ă ` we use the embedding

(2.18)

Ok ÝÑ O`
ˆ
I
A ÞÝÑ `´k

˙
A

of orthogonal groups, where I denotes the identity matrix.

<!-- page 14 -->
14

D. S. FREED AND M. J. HOPKINS

Theorem 2.19. Assume n ě 3. There exist compact Lie groups Hm , m ą n, and homomorphisms in , ρn which fit into the commutative diagram


Hn 
(2.20)


in

ρn

On 

/ Hn`1   n`1 / Hn`2  
i





ρn`1



/ On`1  

/ ...

ρn`2

/ On`2  

/ ...

in which squares are pullbacks.
The stabilization is usually apparent, even when n “ 2 and Theorem 2.19 does not apply. For
L
example, if Hn “ Pin`
xp´1, ´1qy, where Pin`
n ˙T
n acts on T “ U1 through its components by
L
conjugation, then Hm “ Pin`
˙T
xp´1,
´1qy.
(We
encounter this and related groups in §9.)
m
Remark 2.21. For m ă n, define Hm and the homomorphism ρm : Hm Ñ Om by a pullback square:
/ Hn

Hm
(2.22)

ρm



Om





ρn

/ On

Remark 2.23. The pullback diagram (2.20) and the fact that ρm`1 pHm`1 q acts transitively on the
m-sphere imply diffeomorphisms
Hm`1 {Hm – Om`1 {Om – S m

(2.24)

L
Proof of Theorem 2.19. In view of (2.8), for m ą n define SHm :“ Spinm ˆK xp´1, k0 qy, and so
r m as
obtain a stabilization over SOm . If ρn pHn q “ SOn this completes the proof. If not, define H
the pullback
1

/K

rm
/H

/ Pin`

m

/1

1

/K


/J


/ t˘1u

/1

(2.25)

and
(2.26)

rm
Hm – H

L

xp´1, k0 qy.



Theorem 2.19 allows us to speak about symmetry types in quantum field theory independent of
dimension. Set
(2.27)

H “ colim Hn .
nÑ8

For Hn “ SOn we obtain H “ SO8 “ SO. Thus we can speak of ‘oriented theories’=‘SO theories’,
‘Spin theories’, ‘Pin` theories’, etc. The colimit of (2.20) is a homomorphism
(2.28)

ρ : H ÝÑ O.

The symmetry type of a theory (Definition 2.4) can be taken to be the pair pH, ρq in place of pHn , ρn q.

<!-- page 15 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

15

2.2. Curved manifolds and bordism categories with Hn -structure
Fix an n-dimensional relativistic quantum field theory with symmetry type pHn , ρn q. A “coupling
to background gravity” means that we define the theory on each n-dimensional smooth Riemannian
manifold X. The Hn -symmetry is no longer global; it is tangential and encoded in a reduction of
the orthonormal frame bundle to Hn . Let BO pXq Ñ X denote the principal On -bundle of frames:
a point of BO pXq is an orthonormal basis of the tangent space at a point of X. If P Ñ X
is a principal Hn -bundle, define the principal On -bundle ρn pP q “ P ˆHn On Ñ X via mixing:
rph, gs “ rp, ρn phqgs for all p P P , g P On , and h P Hn .
Definition 2.29. An Hn -structure is a pair pP, θq consisting of a principal Hn -bundle P Ñ X
θ
equipped with an isomorphism of principal On -bundles BO pXq ÝÑ ρn pP q. An Hn -manifold is a
Riemannian n-manifold endowed with an Hn -structure. A differential Hn -structure is a connection Θ on P Ñ X with the property that θ maps the Levi-Civita connection to ρn pΘq.
It also makes sense to have an Hn -structure on a Riemannian manifold of dimension ` ą n, via
ρn
the composition Hn ÝÑ On ãÑ O` , and on a manifold of dimension k ă n by stabilizing the Ok frame bundle to a principal On -bundle via the inclusion Ok ãÑ On . The Stability Theorem 2.19
implies that an Hn -manifold has an induced Hm -structure for all m ě n. The same applies to the
differential refinements.
Example 2.30. In bosonic theories of electromagnetism, K “ T is the group U1 of unit norm
complex numbers, at least in the absence of further global symmetries. If there is no time-reversal
symmetry, then Hn “ SOn ˆ T. Thus P Ñ X is the fiber product of the frame bundle with a
principal T-bundle, which is usually equipped with a connection, or gauge field. In theories of
electromagnetism with fermions we still have K “ T, but now the center ´1 P Spinn of the spin
group is identified15 with ´1 P T and so
(2.31)

Hn “ Spincn “ Spinn ˆT

L

t˘1u

is the group introduced in [ABS]. In other words, the Riemannian manifold X has a Spinc -structure.
If, in addition, there is time-reversal symmetry, then there are several different extensions, including
the Atiyah-Bott-Singer group Pincn ; see Proposition 9.4 for the complete classification.
Example 2.32. For Hn “ On ˆ K an Hn -structure on a Riemannian manifold is an auxiliary
principal K-bundle, and a differential Hn -structure is a connection on that bundle. For Hn “ Spincn
the differential structure is usually called a spinc connection.
The basic properties of Wick-rotated correlation functions on all compact manifolds simultaneously are encoded in the powerful framework of bordism categories, following the fundamental work
of Segal [Se1] and Atiyah [A1]. Topological field theories do not depend on the metric, nor do they
require differential structures, and for the most part we focus on topological theories and so on
topological bordism categories. The geometric case is used as motivation; we make some comments
in Remark 2.39.
15This assumes the spin/charge relation that particles of even electromagnetic charge are bosons while those of

odd electromagnetic charge are fermions; see [SeWi] for more discussion.

<!-- page 16 -->
16

D. S. FREED AND M. J. HOPKINS

For the topological bordism category Bordxn´1,ny pHn q defined in the next paragraph, we drop
the connection. We can also drop the Riemannian metric, as just mentioned, and to do so we would
replace the compact Lie group Hn and homomorphism ρn : Hn Ñ On with a canonically associated
noncompact real Lie group H n and homomorphism H n Ñ GLn R. We give the construction in
Appendix C. Our field theories are discrete in the sense that the partition function in C-valued and
C has the discrete topology. Hence the theories factor through the topological bordism category
built with H n -manifolds in place of Hn -manifolds. So we follow standard usage (“spin theories”,
etc.) and use the compact Lie group Hn , but no connections.
Define a topological bordism category Bordxn´1,ny pHn q as follows. An object is a compact pn ´ 1qmanifold Y without boundary, equipped with an Hn -structure Q Ñ Y and an “arrow of time”.
To make sense of an Hn -structure on an pn ´ 1q-manifold we stabilize the tangent bundle of Y
to a rank n bundle R ‘ T Y Ñ Y by summing with a trivial line bundle, thought of as a normal
direction into n dimensions. In this topological setting the Riemannian metric is not present; in the
geometric setting of Remark 2.39, an object in a geometric bordism category is an pn ´ 1q-manifold
with a germ of an embedding in an n-manifold. The arrow of time is a normal orientation. In
the topological setting only the tangential information is relevant—we can drop the germ—and the
arrow of time is an orientation of the trivial subbundle R Ñ Y of R ‘ T Y Ñ Y . Nonetheless,
even in this topological case it is illuminating to use the product germ p´, q ˆ Y for some  ą 0
and replace R ‘ T Y Ñ Y by the tangent bundle to the germ. A morphism X : Y0 Ñ Y1 is an
equivalence class of compact n-manifolds X with Hn -structure P Ñ X and an isomorphism of
–
the boundary BX Ý
Ñ Y0 > Y1 with the disjoint union of the incoming Y0 and the outgoing Y1 ; the
equivalence relation is diffeomorphism commuting with all of the data. The isomorphisms include
the Hn -structures and under those isomorphisms the orientation of the trivial bundle R Ñ Yi must
line up with the incoming normal to the boundary for i “ 0 and with the outgoing normal to the
boundary for i “ 1. In other words, the arrow of time is used to distinguish incoming and outgoing
boundary components of morphisms. Composition of morphisms is gluing of bordisms. There is a
additional commutative composition law on the category—disjoint union—and with this structure
Bordxn´1,ny pHn q is a symmetric monoidal category. See [L, CS] for detailed accounts.
A Wick-rotated field theory is a linear representation of a bordism category.
Definition 2.33. A topological field theory with Wick-rotated vector symmetry group Hn is a symmetric monoidal functor
(2.34)

F : Bordxn´1,ny pHn q ÝÑ VectC

to the symmetric monoidal category of complex vector spaces under tensor product.
Much has been written about this definition, and we defer to previous accounts—such as the
original [A1] and the recent survey [F2, §§2–4] and the references therein—for more exposition.
Here we simply make the connection to point operators16 and their correlation functions.
Remark 2.35 (Vector spaces of point operators). The sphere S n´1 is the link of a point in n dimensions, i.e., it is the boundary of a small ball about the point. Therefore, the vector space V :“
16These are usually called ‘local operators’ in the physical literature, but we use ‘point’ rather than ‘local’ to

distinguish point operators from line operators and higher dimensional analogs, since those too are local.

<!-- page 17 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

17

F pS n´1 q is the space of point operators in a topological field theory; in a geometric theory we take
a limit as the radius of the sphere shrinks to zero. If the theory has total symmetry group Hn ,
then the sphere has an Hn -structure and the vector space of point operators depends on it. If
Hn “ SOn ˆ K or Hn “ On ˆ K, the extra data is a principal K-bundle Q Ñ S n´1 (with connection). So there is a vector space VQ of point operators for each Q. The group Aut Q of global
gauge transformations acts on VQ . For the trivial K-bundle this is the familiar representation of
the global symmetry group K on local operators. If K is finite, then the “twist operators” for
Q Ñ S 1 nontrivial are familiar in n “ 2. They are also familiar when H2 “ Spin2 , in which case
the operators associated to the nonbounding spin circle create a defect at the excised point which
changes the spin structure on the punctured surface. In n “ 3 dimensions, if H3 is a Cartesian
product of SO3 and K “ T, then the twist operators in some sense create a magnetically charged
instanton for the global symmetry group K; the Z-grading from the action of K on the point
operators measures the electric charge.
Remark 2.36 (Correlation functions of point operators). Let M be a closed n-manifold. Fix points
x1 , . . . , xk of M at which we place local operators. Let X be the compact manifold with boundary
obtained from M by removing small open balls about each xi ; regard X as a bordism
(2.37)

X:

ğ

S n´1 pxi q ÝÑ Hn´1

i

from the disjoint union of the k boundary spheres to the empty manifold. Equip the manifold X with
an Hn -structure P , and let Qi denote its restriction to the ith sphere. Applying the theory (2.34)
we obtain a homomorphism
(2.38)

F pX; P q : VQ1
b ¨ ¨ ¨ b VQk ÝÑ C
looooooooomooooooooon
k times

which, evaluated on operators O1 , . . . , Ok , is usually written xO1 px1 q ¨ ¨ ¨ Ok pxk qyM .

Figure 1. Correlation functions
Remark 2.39 (Remark about non-topological theories). Wick-rotated field theories which are not
topological can also be formulated as functors on bordism categories, but now the objects and
morphisms have a geometric structure. The references [Se2, KS, ST] develop this idea in various
directions. We confine ourselves here to a few heuristic formal remarks. Analogous to the topological
bordism category Bordxn´1,ny pHn q we envision a geometric bordism category Bord∇
xn´1,ny pHn q whose

<!-- page 18 -->
18

D. S. FREED AND M. J. HOPKINS

objects and morphisms are smooth manifolds with differential Hn -structures (Definition 2.29).
An object is a closed pn ´ 1q-manifold equipped with an infinite jet of an embedding into an ndimensional manifold with differential Hn -structure and an arrow of time. A morphism is a compact
n-manifold with differential Hn -structure together with a partition of the boundary and boundary
isomorphisms as in the topological case. As in the topological case (2.34), a field theory is a functor
with domain Bord∇
xn´1,ny pHn q and codomain a suitable symmetric monoidal category of topological
vector spaces. We want the correlation functions and vector spaces to vary smoothly in smooth
families, so the whole structure must be “sheafified” over the category of smooth manifolds and
smooth maps [ST, §2].

3. Unitarity and Wick rotation
We recall in §3.1 how positivity of energy leads to Wick rotation in quantum mechanics, and
describe reflection positivity in that context. The usual quantum mechanical context for reflection
positivity is recollected in §3.2, with attention paid to nontrivial internal symmetry groups. These
preliminaries are motivation for §3.3, where we encode the reflection structure in a novel way via a
coextension of the Wick-rotated vector symmetry group to a Z{2Z-graded group, constructed from
a hyperplane reflection. (We give a topological account of the construction in Appendix E.) The
new components act antilinearly on the Hilbert space of states. It is this formulation that we use
in the rest of the paper.
3.1. Wick rotation in quantum mechanics
A quantum mechanical system, according to basic axioms, consists of a complex separable Hilbert
space H equipped with a self-adjoint operator H, the Hamiltonian. The group R of time translations
is represented unitarily on H:

(3.1)

R ÝÑ U pHq
t ÞÝÑ e´itH{~ ,

where i is a choice of complex number such that i2 “ ´1. If we assume positivity of energy—that
H is a nonnegative self-adjoint operator—then real time evolution (3.1) is the boundary value of a
?
holomorphic semigroup of bounded operators defined on the lower half plane T “ R´ ´1 Rą0 Ă C.
?
The semigroup of imaginary time evolution is the restriction to ´ ´1 Rą0 , which is the semigroup
(3.2)

τ ÞÝÑ e´τ H{~ ,

τ ą 0.

The transition from (3.1) to (3.2) is called Wick rotation.
The unitarity of time evolution manifests in the reality of the semigroup (3.2).

<!-- page 19 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

19

Example 3.3 (Particle on the circle). Let A1 denote the affine17 time line. The trajectory of a
particle on the circle is a function λpsq “ eixpsq , s P A1 ; the lagrangian density is L “ 21 x9 2 |ds|. The
ensuing quantum mechanical system has Hilbert space H “ L2 pS 1 ; Cq, Hamiltonian the Laplace
operator H “ ∆ (up to a constant), and imaginary time evolution the heat operator τ ÞÑ e´τ ∆ .
It is illuminating to add a “θ-angle” to this system; see [GKKS, Appendix D], for example.
ş
Orient S 1 and fix ω P Ω1 pS 1 q with S 1 ω “ 1. Then for a fixed constant θ P R define the lagrangian
(3.4)

1
L “ x9 2 |ds| ´ θλ˚ pωq.
2

In this classical theory we must orient time in order to integrate L; time-reversal exchanges the
theories labeled by θ and ´θ. Upon quantization we obtain the Hilbert space H “ L2 pS 1 ; Leiθ q
of sections of the complex line bundle Leiθ with holonomy eiθ . The Hamiltonian is the Laplace
operator on this space, and imaginary time evolution is by the associated heat operator. Now
time-reversal (θ ÞÑ ´θ) acts as complex conjugation:
(3.5)

H ÞÝÑ H

(3.6)

e´τ ∆ ÞÝÑ e´τ ∆

We encode the formal structure in terms of oriented compact Riemannian 1-manifolds, as
described in §2.2, though we emphasize that this is not a topological theory. The interval of
length τ ą 0 maps to the imaginary time evolution e´τ H{~ : H Ñ H. The semigroup law is manifest by gluing intervals. The circle of length τ maps to Tracepe´τ H{~ q P C. We interpret these
oriented Riemannian 1-manifolds as morphisms in a geometric bordism category whose objects are,
roughly, compact oriented 0-manifolds. More precisely, they are 0-manifolds embedded in the germ
of an oriented Riemannian 1-manifold, and there is an arrow of time, or orientation of the normal
bundle. The simplest object is a single point, which we can view as 0 P R embedded in a small
interval p´, q with its standard orientation; in the quantum mechanics it maps to the Hilbert
space H. According to (3.5) we have
(3.7)

orientation-reversal ÞÝÑ complex conjugation

More precisely, the orientation-reversal on objects in the geometric bordism category reverses the
orientation and reverses the arrow of time. This is the ‘reflection’ part of ‘reflection positivity’; the
positivity is the positive definiteness of the Hilbert space H.
3.2. Reflection positivity in Euclidean quantum field theory
Positivity of energy in a relativistic quantum field theory also results in an analytic continuation
and restriction to Euclidean space, as we review in §A.3. Here we focus on the Wick rotation
of correlation functions and the Wick rotation of unitarity as manifested in reflection positivity.
17We (pedantically) distinguish the affine time line A1 from the group R of translations of time, which appears

in (3.1): after all, a 1-hour seminar and a seminar ending at 1:00 can be quite different.

<!-- page 20 -->
20

D. S. FREED AND M. J. HOPKINS

(See [GJ, §6], [Kaz, §2.2] for an account.) Let n be the spacetime dimension and En Euclidean
n-space. In this subsection we restrict to the basic symmetry type Hn “ SOn ; we take up general
symmetry types in the next subsection (see Remark 3.28). Fix an affine hyperplane Π Ă En and
let σ denote (affine) reflection about Π. Let O denote an operator, or product of operators, in
the quantum theory which is supported in the open half-space En` on one side of Π; the reflected
operator σpOq has support in the complementary half-space En´ . Let xOyEn P H denote the half`
space correlation function, which is a vector in the Hilbert space of the theory. In a lagrangian field
theory it is the functional integral over the half-space En` . Then the reflection part of ‘reflection
positivity’ is
(3.8)

xσpOqyEn “ xOyEn
´

`

Figure 2. Reflection positivity in Euclidean space
in accordance with (3.7); see (3.6) for the analog in quantum mechanics. The Hilbert space H is
associated to pΠ, oq, where o is an orientation of the normal line to Π, the arrow of time in §2.2.
The reflection σ reverses o, and the Hilbert space associated to pΠ, ´oq is the complex conjugate
(3.9)

–

HpΠ,´oq ÝÝÑ HpΠ,oq ,

according to the dictum (3.7); cf. (3.5). Therefore, xσpOqyEn P H and (3.8) is an equation in the
´

complex conjugate Hilbert space H. The positivity part of ‘reflection positivity’ is the positive
definiteness of H, which implies that the norm square of the vector xOyEn is nonnegative:
`

(3.10)

xσpOq OyEn ě 0

A theorem of Osterwalder-Schrader [OS] reconstructs the relativistic theory in Minkowski spacetime
from the Euclidean theory; reflection positivity is an important ingredient.

<!-- page 21 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

21

Remark 3.11. In theories with fermionic states the Hilbert space H is Z{2Z-graded. The norm
square of an odd vector is then purely imaginary [DM, §4.4] and positive definiteness requires a
sign choice; see Example 6.49 for details in the invertible case.
Remark 3.12 (Internal symmetry and reflection positivity). Suppose the full Wick-rotated vector
symmetry group Hn has a nontrivial internal symmetry group K, and for simplicity take Hn “
SOn ˆ K. Let X be Euclidean space with an open neighborhood of the support of the operators O,
σpOq removed. Let Y “ BX XH` and assume σpY q “ BX XH´ . In general there are twist operators
that are defined by a principal K-bundle P Ñ X, as in Remark 2.35. The reflection σ must account
for the K-bundle, and it might seem at first that σ should “reverse” it by an involution on K. But
that does not happen; rather σ lifts to P Ñ X. We give three arguments.
(1) If O is a point operator, then Y is a sphere. Identifying σpY q with Y via a translation, σ acts
on Y as reflection in the equatorial plane parallel to Π. If we one-point compactify X to S n
minus the two balls and assume P extends over the compactification, then the restrictions of
P to Y and σpY q are isomorphic, since the compactification is diffeomorphic to r0, 1sˆS n´1 .
(2) Continuing, suppose P Ñ X is the trivial bundle and V is the vector space of local operators attached to Y . (In a geometric theory we take a limit as the radius of the removed
ball shrinks to zero.) The automorphism group K of the trivial bundle over Y acts on V ,
producing K-multiplets of point operators. The hyperplane reflection σ induces an isomorphism V Ñ V that commutes with the K-action, since geometrically the lift of reflection to
the trivial bundle commutes with the global gauge transformations. So a K-multiplet in V
is mapped to a K-multiplet in V that transforms in the complex conjugate representation.
(3) Let n “ 1 and H1 “ SO1 ˆ Z{3Z. Let α : Bordx0,1y pH1 q Ñ VectC be the invertible theory
which attaches a nontrivial character χ : Z{3Z Ñ T to the positively oriented point with its
trivial Z{3Z bundle. (That object Y of the bordism category has automorphism group Z{3Z,
which then acts on the vector space αpY q.) This theory is unitary. Now αpP Ñ S 1 q is
χ applied to the holonomy of the principal Z{3Z-bundle P Ñ S 1 . Reflection reverses the
orientation of S 1 , and if the bundle stays the same under reflection, then the holonomy
complex conjugates, which is precisely what it should do in a reflection positive theory.
pn
3.3. The extended symmetry group H
Let pHn , ρn q be a symmetry type (Definition 2.4). We use reflection symmetry (3.8) to construct
p n from Hn by adjoining an involution. In the special case Hn “ Spinn ,
a larger symmetry group H
`
p n “ Pin ; the general case is a bootstrap from this, following the proof of Theorem 2.19.
we define H
n
The arguments in Remark 3.12 motivate the triviality of the hyperplane reflection automorphism
p n as a symmetry group of the Euclidean quantum field theory;
of K in our construction. We view H
p n zHn on the Hilbert space H is by an anti-unitary transformation.
the action of an element in H
Proposition 3.13. There exists a canonical group extension
(3.14)

jn
p n ÝÑ t˘1u ÝÑ 1,
1 ÝÑ Hn ÝÝÝÑ H

split (noncanonically) by a choice of hyperplane reflection σ P On , such that the splitting induces
Ą n – Spinn ˆK that is the product of conjugation by σ on Spinn and the
the automorphism of SH

<!-- page 22 -->
22

D. S. FREED AND M. J. HOPKINS

identity automorphism of K. There is a homomorphism ρ̂n that fits into the pullback diagram
Hn
(3.15)

jn

pn
/H

ρn





ρ̂n

/ t˘1u ˆ On

On

pn Ñ H
p n`1 which, together with the inclusions in : Hn Ñ Hn`1 ,
Finally, there are inclusions ı̂n : H
induce a commutative diagram linking (3.15) for varying n.
A hyperplane reflection σ P On induces an automorphism of SOn by conjugation in On , and it lifts
uniquely to an automorphism of Spinn , which is realized as conjugation by σ̃ P Pin`
n , where σ̃ is a
lift of σ. However, it is the twisted conjugation [ABS, §3] by σ̃ in Pin`
that
lifts
conjugation
by σ
n
in On , where the twist is multiplication by the nontrivial character
(3.16)

–

`
Pin`
n ÝÑ π0 Pinn ÝÝÑ t˘1u.

Note σ̃ is only determined up to sign; the splitting of (3.14) associated to σ is determined up to
multiplication by k0 .
See Appendix E for an alternative approach to Theorem 3.13 using homotopy theory.
Proof. 18 Define
(3.17)

y n “ Pin` ˆK
SH
n

L

xp´1, k0 qy

and project onto π0 Pin`
n to define the quotient map in the extension
(3.18)

y n ÝÑ t˘1u ÝÑ 1
1 ÝÑ SHn ÝÑ SH

p n “ SH
y n . In general, define H
p n as the pullback
If ρn pHn q “ SOn , then set H
φn

pn
H
(3.19)

ρ̂n



ˆ On 
2

/µ



/ Hn`3

/ O



ρn`3

n`3

where the bottom map is
ˆ
(3.20)

p, Aq ÞÝÑ

A 0
0 I3

˙

18Our original proof had an error. We thank Peter Teichner for bringing it to our attention.

<!-- page 23 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

23

in an pn ` 3q ˆ pn ` 3q block decomposition. Here /µ` Ă T denotes the group of `th roots of unity.
`
˘
Use this embedding to define the subgroup S /µ2 ˆ On of /µ2 ˆ On as the intersection
(3.21)

`
˘
`
˘
S /µ2 ˆ On :“ /µ2 ˆ On X SOn`3 .

Then define
(3.22)

´ `
˘¯
pn.
y 1 :“ ρ̂´1 S /µ ˆ SOn
Ă H
SH
n
n
2

Construct the homomorphism jn by mapping into the pullback square (3.19):
jn

Hn
(3.23)

ρn

ρ̂n



On 



'
/ Hn`3

φn

pn
/H


/ /µ ˆ On  

/ O



ρn`3

n`3

2

The bottom left map is A ÞÑ p1, Aq, and the top curved map is the inclusion in (2.20). The group
extension (3.14) can be read off from (3.23).
y n , as defined in (3.17), is isomorphic to SH
y 1 , as defined in (3.22). To prove
We claim that SH
n
this, pull back (3.19) over the homomorphism Spinn`3 Ñ On`3 into the southeast corner to obtain
Pin`
n ˆK
(3.24)

pr1




Pin`
n

Ą n`3 “ Spin
/ SH

n`3 ˆK



pr1


/ Spin

n`3

`
`
To check that the pullback has the indicated form, embed Pin`
n Ă Cliff n and Spinn`3 Ă Cliff n`3
as usual. Then from (3.20) we find that the bottom map sends ei to ˘ei en`1 en`2 en`3 P Spinn`3 ,
and we observe that pei en`1 en`2 en`3 q2 “ `1, which explains why the southwest corner is Pin`
n
.
The
northeast
corner
is
computed
by
Theorem
2.7(2).
Finally,
(3.24)
is
a
rather than Pin´
n
pullback diagram, since (3.19) is, and this determines the northwest corner. To recover (3.17)
y 1 is the northwest corner of the pullback of (3.19) over the homomorfrom (3.22), observe that SH
n
phism SOn`3 Ñ On`3 . The isomorphism (2.8) implies that the northeast corner of this pullback
is obtain by dividing the northeast corner of (3.24) by the order 2 subgroup xp´1, k0 qy. The top
homomorphism of (3.24) is an injection, and now (3.17) follows.
If σ P On is a hyperplane reflection, and ξ P Pin`
n is a lift (which is determined up to a sign),
p n which in (3.19) satisfies
then define the splitting of (3.14) to send ´1 P t˘1u to the element ĥ P H

(3.25)

ρ̂n pĥq “ p´1, σq
L
φn pĥq “ rξen`1 en`2 en`3 , 1s P SHn`3 “ Spinn`3 ˆK xp´1, k0 qy

<!-- page 24 -->
24

D. S. FREED AND M. J. HOPKINS

Ą n induces the automorphism stated in Proposition 3.13.
Note that ĥ2 “ 1. Conjugation by ĥ on SH
p n`1 as a pullback:
Finally, define ı̂n using the definition of H
6 Hn`3

φn
ı̂n

pn
H

(3.26)

ρ̂n
/µ

2



ˆ On 

in`3
φn`1

p n`1
/H




'
/ Hn`4

ρ̂n`1


/ /µ ˆ O
n`1

/O



ρn`4

n`4

2

Recall our convention (2.18) for the embedding On ãÑ On`1 . This, together with (3.20), makes
/µ

2

(3.27)
/µ

ˆ On

/ On`3




/ On`4

ˆ On`1
2

a commutative diagram, and this is the key observation necessary to construct the commutative
diagram indicated in the final sentence of Proposition 3.13, whose proof is now complete.

Remark 3.28. Now we formulate reflection positivity on Euclidean space for a theory with symmetry
type pHn , ρn q. Adjoining translations via the pullback
1

/K

/ Hn

1

/K


/ Hn

(3.29)

ρn

/ Eucn

/1


/ On

/1

we obtain a larger group Hn and a homomorphism Hn Ñ Eucn to the Euclidean group. The
complex point observables form a vector bundle O Ñ En , and the action of Eucn on En lifts to
p n of Hn and a homomorphism
an action of Hn on O. Proposition 3.13 gives a coextension H
p n Ñ t˘1u ˆ Eucn . As before fix a hyperplane reflection σ and now fix a lift σ̂ P H
p n of p´1, σq P
H
t˘1u ˆ Eucn . Then part of the data of a reflection structure is a lift of σ̂ to an antilinear map of
the complex vector bundle O Ñ En . Therefore (3.8)–(3.10) apply, with σ̂ replacing σ.
Proposition 3.30. For each n ě 1 there is an inclusion of group extensions
1
(3.31)
1

/ Hn
_


/ t˘1u ˆ Hn
_

in

/ Hn`1

jn`1



/ t˘1u

/1

/ t˘1u

/1

sn`1 ˚jn`1 in

p n`1
/H

in which in is the inclusion in (2.20) and jn the inclusion in (3.14). Furthermore, the inclusions in
and ı̂n induce a commutative diagram linking (3.31) for varying n.

<!-- page 25 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

25

p n for σ P On reflection in the hyperplane
Proof. First, define a particular splitting sn : /µ2 Ñ H
orthogonal to e1 . Namely, as in (3.25), characterize the element ĥn “ sn p´1q by

(3.32)

ρ̂n pĥn q “ p´1, σq
L
φn pĥn q “ re1 e2 e3 e4 , 1s P SHn`3 “ Spinn`3 ˆK xp´1, k0 qy

jn`1
in
p n`1 centralizes the image of Hn ÝÝ
p n`1 . It is
Then ĥn has order 2, and ĥn`1 P H
Ñ Hn`1 ÝÝÝÑ H
easy to verify that (3.31) commutes.


For the basic symmetry groups in (2.17) the extended symmetry groups are listed here:

(3.33)

states/symmetry

Hn

pn
H

bosons only
fermions allowed
bosons, time-reversal (T )

SOn
Spinn
On

fermions, T 2 “ p´1qF

Pin`
n

On
Pin`
n
t˘1u ˆ On
`
y
Pin

fermions, T 2 “ id

Pin´
n

n

´
y
Pinn

pn is a consequence of the fact that hyperplane reflections are inner in On . As in
The splitting of O
Remark A.9, let α̂ be the automorphism of Pin˘
n that is the identity on Spinn and multiplication
by the central element ´1 on the complement; it covers the identity automorphism of On . Then a
computation of the pullback (3.19) yields isomorphisms

(3.34)

L
y ` – p /µ ˙ Pin` q xp´1, ´1qy
Pin
n
n
4
y ´ – /µ ˙ Pin´
Pin
n
n
2

where the generators of /µ4 , /µ2 act on the pin group via α̂.

4. Reflection symmetry on manifolds
p n produces an involution (§4.1) on Hn -manifolds that generalThe enhanced symmetry group H
izes orientation-reversal for H “ SO. In the field theory context it induces an involution on bordism
categories that we call ‘bar’. (See Appendix B for a general discussion of involutions on categories
and other relevant background.) In §4.2 we prove that the dual of an object in a bordism category
is isomorphic to its bar. The definitions of reflection structure and positive reflection structure for
non-extended field theories are in §4.3. In a reflection positive theory the partition function of any
double is nonnegative, as we prove in §4.4. We work as always with arbitrary symmetry groups.19
19The definition of the double of a (s)pin manifold is somewhat tricky, for example; the general setting is clarifying.

<!-- page 26 -->
26

D. S. FREED AND M. J. HOPKINS

Kevin Walker has introduced theories with more general reflection structures in which, possibly,
pn “
the group extension (3.14) that controls anti-unitarity is not split. In particular, he allows H
´
Pinn when Hn “ Spinn . This leads to exotic hermitian structures. Our more restrictive framework
is based on Wick rotation of relativistic theories.
4.1. An involution on Hn -manifolds
Recall from §2.2 that an Hn -manifold is a Riemannian n-manifold equipped with a reduction
pP, θq of its orthonormal frame bundle BO pXq Ñ X to Hn . Extend the principal Hn -bundle P Ñ X
p n -bundle jn pP q Ñ X, where jn is the inclusion of groups in (3.14). Using (3.15)
to a principal H
`
˘
extend the isomorphism θ : BO pXq Ñ ρn pP q to an isomorphism θ̂ : t˘1u ˆ BO pXq Ñ ρ̂n jn pP q .
Definition 4.1. The opposite Hn -structure pP 1 , θ1 q is the principal Hn -bundle P 1 :“ jn pP qzP Ñ X
and the restriction θ1 of θ̂ to t´1u ˆ BO pXq.
–

Taking opposites is involutive: there is a canonical isomorphism pP, θq ÝÝÑ pP 2 , θ2 q.
Remark 4.2. Let σ P On be a hyperplane reflection and φσ the automorphism of Hn resulting from
the splitting of (3.14). Then we can identify the principal Hn -bundle P 1 Ñ X as the projection
P Ñ X of manifolds with the original Hn -action on P precomposed with the automorphism φσ .
p n is the splitting element, then we map P Ñ jn pP qzP by p ÞÑ p ¨ σ̃.
For if σ̃ P H
Example 4.3. An SOn -structure is an orientation, and the opposite SOn -structure is the reverse
orientation. In this case P Ñ X is the bundle of oriented orthonormal frames, jn pP q Ñ X the
bundle BO pXq Ñ X of all orthonormal frames, and jn pP qzP Ñ X the bundle of oppositely oriented
orthonormal frames.
Example 4.4. For simplicity, we sometimes abbreviate ‘Pin˘
n -structure’ to ‘pin structure’, just as
‘Spinn -structure’ is abbreviated to ‘spin structure’. The opposite of a pin structure is obtained by
tensoring with the orientation double cover; see Definition A.8, Remark A.9, and the text following (3.33). One motivation for our general study of symmetry groups (§2.1) and involutions (§3.2)
is to explain the appearance of this opposite pin structure in the formulation of reflection positivity
for Wick-rotated quantum field theories with fermions and time-reversal symmetry.
We use the involution in Definition 4.1 to construct an involution of categories
(4.5)

βB “ β : Bordxn´1,ny pHn q Ñ Bordxn´1,ny pHn q.

In Appendix B we explain that an involution on a category B is a functor β : B Ñ B and a natural
transformation of functors η : idB Ñ β 2 . The objects and morphisms in Bordxn´1,ny pHn q are
Riemannian manifolds with Hn -structure: the functor β fixes the underlying Riemannian manifold
and flips the Hn -structure to its opposite. The equivalence η implements the canonical isomorphism
indicated after Definition 4.1. We emphasize that the “bar involution” β is covariant: a morphism
X : Y0 Ñ Y1 maps to a morphism βX : βY0 Ñ βY1 . Put differently, the arrows of time on objects
are unchanged under β.

<!-- page 27 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

27

Remark 4.6. One can envisage other involutions on the bordism category, and so other notions of
reflection structure (Definition 4.14 below), especially for mathematical applications. The heuristics
in Remark 3.12 are meant to illustrate why we feel the involution defined here correctly models
Wick-rotated unitarity in relativistic field theories.
4.2. Duals and opposites
An object Y in a symmetric monoidal category, such as Bordxn´1,ny pHn q, may have a dual Y _ ,
which is equipped with duality data; see Definition B.8 for a quick review. In a topological bordism
category every object has a dual. The underlying smooth manifold of the dual Y _ equals that
of Y , but the arrow of time is reversed. This reversal is evident in the coevaluation and evaluation
duality data. For example, evaluation is the bordism
(4.7)

eY “ r0, 1s ˆ Y : Y _ > Y ÝÑ Hn´1

with the entire boundary incoming. The Hn -structure is the same at the two ends, but the arrows
of time are opposite. If the boundary at 0 P r0, 1s is the object Y , with its arrow of time, then
the boundary at 1 P r0, 1s is the object Y _ . See Figure 3, where the coevaluation cY and the
“S-diagram” (B.9) are also depicted.

Figure 3. Evaluation, coevaluation, and the gluing to the identity
An object Y in a topological bordism category has a canonical product germ (see §2.2), namely
the germ of t0u ˆ Y in X “ p´, q ˆ Y , where we fix  ą 0. Let σ be the diffeomorphism of X that
reflects t ÞÑ ´t and fixes Y . The splitting in Proposition 3.13 leads to an alternative construction
of the opposite Hn -structure and the following important identification.
Proposition 4.8. For any object Y in Bordxn´1,ny pHn q there is an isomorphism
(4.9)

–

h : βY ÝÝÑ Y _

Also, βh_ “ h.
Reversing the Hn -structure (βY ) is equivalent to reversing the arrow of time (Y _ ). Or, in the
language of Definition B.14, every object in Bordxn´1,ny pHn q carries a hermitian structure.
Proof. Set X “ p´, q ˆ Y . The reflection

(4.10)

σ : p´, q ˆ Y ÝÑ p´, q ˆ Y
pt, yq ÞÝÑ p´t, yq

<!-- page 28 -->
28

D. S. FREED AND M. J. HOPKINS

lifts to the frame bundle BO pXq. We now construct a diagram of principal K-bundles:
Q1 
(4.11)


BY



/ P1  
π1



/ jn pP q o

? _P o
π




/ BO pXq  ´1ˆid/ t˘1u ˆ BO pXq o 1ˆid ? _ BO pXq o


? _ Q_

? _ B_
Y

Let BY Ă BO pXq be the On´1 -subbundle of frames with first vector ˘B{Bt, the sign chosen to align
with the arrow of time of the object Y . Let B_
Y be the compatible frames with the opposite arrow of
time. Then σ induces an isomorphism BY Ñ B_
Y which is realized inside BO pXq as multiplication
by the hyperplane reflection σ1 P On in the orthogonal complement to the vector e1 P Rn . (Observe
π
that σ1 centralizes On´1 Ă On .) Let P Ý
Ñ BO pXq Ñ X be the Hn -structure: the composition is a
principal Hn -bundle and the first map is a principal K-bundle over its image. Set Q_ “ π ´1 pB_
Y q;
π1

then Q_ Ñ X is a principal Hn´1 -bundle. Let jn pP q, P 1 be as in Definition 4.1, so that P 1 ÝÑ
BO pXq Ñ X is the opposite Hn -structure. Set Q1 “ π 1 ´1 pBY q, so that Q1 Ñ X is an Hn´1 -bundle
p n be the lift of σ1 P On , as defined in (3.32);
that encodes the opposite Hn -structure. Let ĥn P H
then ĥn centralizes Hn´1 and has order two. The action of multiplication by ĥn on jn pP q restricts
to an isomorphism of Hn´1 -bundles Q1 Ñ Q_ . (It covers multiplication by p´1, σ1 q P t˘1u ˆ On
on t˘1u ˆ BO pXq, which restricts to an isomorphism BY Ñ B_
Y .)
βh_ is the inverse of the involution ĥn on jn pP q, restricted to the bar dual bundles. Since ĥn is
its own inverse, we conclude βh_ “ h.

Remark 4.12. In a geometric bordism category not every germ admits a reflection which is an
isometry. It is only for germs which do admit such a reflection that we expect the associated
topological vector space of a field theory to have a Hilbert space structure; see [KS]. This is the
case for the (noncompact) affine hyperplane in Figure 2, consistent with (3.9).
4.3. Reflection structures and positivity
Let
(4.13)

βC “ β : VectC ÝÑ VectC

be the involution of complex conjugation (Example B.2). Recall (2.34) that a topological field
theory is a symmetric monoidal functor F : Bordxn´1,ny pHn q Ñ VectC .
Definition 4.14. A reflection structure on F is equivariance data for the involutions βB , βC .
Equivariance data is spelled out in Definition B.6. For every closed pn ´ 1q-manifold Y with
Hn -structure we have an isomorphism of vector spaces
(4.15)

–

F pβY q ÝÝÑ F pY q,

the curved space analog of (3.9). Combining with the isomorphism (4.9), we see that F peY q is a
hermitian form
(4.16)

hY : F pY _ q b F pY q – F pβY q b F pY q – F pY q b F pY q ÝÑ C,

<!-- page 29 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

29

which by the usual “S-diagram” argument (Figure 3) is nondegenerate. Sesquilinearity is a consequence of the isomorphism

(4.17)

eY ÝÑ βpeY q
pt, yq ÞÝÑ p1 ´ t, yq

where recall as a manifold eY “ r0, 1s ˆ Y .
Definition 4.18. A reflection structure is positive if the induced hermitian form hY is positive
definite for all Y P Bordxn´1,ny pHn q.
Remark 4.19. In a non-extended field theory reflection is data and positivity is a condition. In the
extended case considered later, both reflection and positivity are data.
Remark 4.20. There is also a notion of positivity if the domain is the category of super vector
spaces; see Example 6.49.
Example 4.21. To avoid trivialities, suppose the spacetime dimension n is even. Fix a nonzero
complex number λ P C. There is a simple invertible field theory of unoriented manifolds (Hn “ On )
whose partition function on a closed n-manifold X is λEulerpXq , where EulerpXq is the Euler number
of X. The vector space Fλ pY q attached to any closed pn ´ 1q-manifold Y is the trivial line C: the
Euler characteristic of a compact manifold with boundary is a well-defined number. In the bordism
Dn
Dn
category we can write the closed manifold S n as the composition Hn´1 ÝÝÑ S n´1 ÝÝÑ Hn´1 of two
closed balls. Denote the first arrow as X and apply the theory Fλ :
(4.22)

λ2 “ Fλ pS n q “ hS n´1 pFλ pXq, Fλ pXqq.

Therefore, a necessary condition for positivity is that λ be real.
A reflection structure imposes a curved space analog of (3.8), which for an n-dimensional Hn bordism X, asserts that
(4.23)

F pβXq “ F pXq.

For example, if H “ SOn then the partition function complex conjugates when the orientation of
spacetime is reversed. For a theory of unoriented manifolds (Hn “ On ), condition (4.23) implies
that every partition function is real. For theories of pin manifolds (Hn “ Pin˘
n ) the partition
function of the w1 -twisted pin structure (Definition A.8) is the complex conjugate of the original
partition function.
4.4. Doubles
The reflection-conjugation equation (4.23) also applies to manifolds with boundary. We use it
to derive a necessary condition for reflection positivity.

<!-- page 30 -->
30

D. S. FREED AND M. J. HOPKINS

Definition 4.24. Let X be a compact Hn -manifold with boundary, viewed as a bordism Hn´1 Ñ
BX. The double of X is the closed Hn -manifold
(4.25)

∆X “ eBX pβX, Xq.

The double is illustrated in Figure 4. In that picture Y “ BX.

Figure 4. The double of X
Proposition 4.26. If a theory F : Bordxn´1,ny pHn q Ñ VectC admits a positive reflection structure,
then F p∆Xq ě 0 for all compact Hn -manifolds X with boundary.
Note that the value of a theory on a closed n-manifold does not depend on the reflection structure.
The necessary condition for positivity in Proposition 4.26 is the compact manifold analog of the
usual reflection positivity statement (3.10) in Euclidean space.
Proof. From (4.25) and (4.23) we deduce
(4.27)

˘
`
˘
`
F p∆Xq “ F peBX q F pβXq, F pXq “ hBX F pXq, F pXq “ }F pXq}2F pBXq ě 0.



The double construction is standard for unoriented and oriented manifolds. It is a bit trickier
for spin and pin manifolds, so we give a recognition principle and illustrate with some examples.
σ
Observe that the double has an obvious (anti-)involution ∆X ÝÑ β∆X with fixed point set Y “
t1{2uˆBX, and σ induces multiplication by ´1 on the normal bundle. Set X 1 “ X YBX r0, 1{2sˆBX
and cut along Y “ BX 1 to write
(4.28)

∆X “ βX 1 YBX 1 X 1 ,

which is the typical description of a double. But we must account for the Hn -structure as well.

<!-- page 31 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

31

Proposition 4.29. Let X be a closed Hn -manifold, σ : X Ñ βX an anti-involution with fixed point
set Y such that
(i ) There exists a submanifold N Ă X with boundary Y such that X is the union of N and σN
along Y and σ induces a diffeomorphism βN – σN of Hn -manifolds; and
ˇ
(ii ) σ ˇY induces the hyperplane reflection isomorphism of the Hn -structure on Y to its opposite.
Then X – ∆N as Hn -manifolds
p n ; see (3.32).
The isomorphism in (ii) is left multiplication by ĥn P H
Proof. Use the tubular neighborhood theorem to replace Y with r0, 1s ˆ Y and so construct the
desired Hn -isomorphism.

Corollary 4.30. The sphere S n with Hn -structure Hn`1 Ñ Hn`1 {Hn is a double
We note from Remark 2.23 that the homogeneous space Hn`1 {Hn is diffeomorphic to S n .
Proof. Reflection σ in the hyperplane perpendicular to e1 is an involution of S n with fixed point
set the equatorial S n´1 perpendicular to e1 . The reflection lifts to an isomorphism of the principal
Hn -bundle Hn`1 Ñ Hn`1 {Hn with the pullback of its opposite. (The isomorphism is globally left
p n`1 .)
multiplication by re1 , 1; 1s Ă H

Example 4.31. For Hm “ Spinm the circle Spin2 { Spin1 has the bounding spin structure: the
Spin1 -bundle Spin2 Ñ Spin2 { Spin1 is the nontrivial double cover of the circle. The nonbounding
spin circle is not a double. Indeed, there is a reflection positive invertible 1-dimensional spin
topological field theory α into super vector spaces that attaches the odd line to a positively oriented
1
q “ ´1. This does not violate Proposition 4.26 since
spin point; it follows that αpSnonbounding
1
Snonbounding is not a double. Turning this argument around, since the oriented circle is a double,
the 1-dimensional oriented topological field theory into super vector spaces that attaches the odd
line to a positively oriented point does not admit a positive reflection structure.
Remark 4.32. The group Hn`1 acts as symmetries of the Hn -sphere in Corollary 4.30. Topologically,
then, there is a universal family of Hn -spheres parametrized by the classifying space BHn`1 . Field
theories may be evaluated on families of manifolds and bordisms; this family of spheres enters our
analysis in §7.2.

5. Invertible topological field theories and stable homotopy theory
We first recall that to fully implement locality in field theory we need to use a bordism multicategory that encodes gluing laws in arbitrary codimension. Next we recount how invertible topological
field theories lie in the framework of homotopy theory: invertibility moves the discussion from abstract multicategories to topological spaces. Finally, we specify the universal target that tracks
deformation classes of invertible topological theories. The main result is Theorem 5.23, which is
our point of departure for implementing reflection positivity in invertible topological theories. We

<!-- page 32 -->
32

D. S. FREED AND M. J. HOPKINS

conclude in §5.4 with a discussion of invertible non-topological theories and their role in low energy
approximations of gapped quantum systems.
The material in this section is covered in much more expository detail in many references, so we
only recount essentials.
5.1. Extended field theories
There are several physics motivations for extending an n-dimensional Wick-rotated field theory
to lower dimensional manifolds, and these are hardly restricted to the topological case of interest
here. First, the vector space of physical states attached to an pn ´ 1q-manifold Y depends locally
on Y . This is familiar in n “ 2 dimensions, where a theory not only has a vector space attached
to a circle, but also to an interval with boundary conditions; the gluing laws for intervals lie in
codimension two, since intervals are glued along 0-manifolds in this 2-dimensional theory. The
result is sometimes called an open-closed theory [MS].20 The labels on the boundary are objects
in a category, so it is natural to associate that category to the 0-manifold consisting of a single
point. As we are doing quantum mechanics, the category is linear and indeed the vector space
associated to the interval with boundary labels β0 , β1 is Hompβ0 , β1 q in the category. The objects
are boundary conditions, or D-branes. Another common example is 3-dimensional Chern-Simons
theory, in which a unitary modular tensor category is associated to the 1-manifold S 1 , which is a
manifold of codimension two in this theory.
Let X n be a Riemannian n-manifold on which a theory F is defined, and fix x P X. We explained
in Remark 2.35 that the vector space F pSxn´1 q attached to a small sphere around x, in the limit of
small radius, is the space of point operators at x. A field theory also has extended operators, whose
support may be a submanifold W Ă X of dimension k ą 0. An extended operator with k “ 1 is
called a line operator, with k “ 2 a surface operator, etc. The link of W at any x P W is a sphere
Sxn´k´1 . In an extended field theory F there is an invariant F pSxn´k´1 q which is a k-category whose
objects are the operators on W . Thus the line operators in a theory form a 1-category, the surface
operators a 2-category, etc.; see [Ka2] for a thorough account.
We believe that every field theory of physical relevance should be fully extended. The mathematical implementation is most developed in the topological case: a sampling of references
is [F1, La, BD, L, F2, AF]. Invariants of manifolds of increasing codimension are encoded in a higher
categorical structure of increasing complexity. The modern framework also includes invariants for
families of manifolds; see [ST] for a non-topological version. The domain of an n-dimensional topological field theory with symmetry group Hn is the bordism multicategory Bordn pHn q whose objects
are 0-manifolds; 1-morphisms are bordisms of 0-manifolds, which are 1-manifolds with boundary;
2-morphisms are bordisms of bordisms, which are 2-manifolds with corners; and so on until we
reach n-manifolds with arbitrary corners. At that point we continue to pn ` `q-morphisms which
are roughly `-dimensional families of n-manifolds, where ` is an arbitrary positive integer. The
entire structure is an p8, nq-category [BM, L, BS, Ng, CS, S-P].
Definition 5.1. Let C be a symmetric monoidal p8, nq-category. A fully extended n-dimensional
topological field theory with Wick-rotated vector symmetry group Hn and target C is a symmetric
20There is a difference between an open-closed theory and a fully extended 2-dimensional theory [L, §4.2].

<!-- page 33 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

33

monoidal functor
(5.2)

F : Bordn pHn q ÝÑ C.

We typically shorten this to ‘topological field theory’. In general there is no preferred choice of
target C, and it is an open issue to construct suitable general targets. In the very special invertible
case we study here there are two preferred targets; see §5.3.
5.2. Invertible topological field theories
There is a natural superposition of quantum systems which does not introduce interactions
between them. In the framework of Wick-rotated field theories on compact manifolds this is implemented by tensoring theories together, and that tensor product makes sense for fully extended
theories too. There is a unit for the tensor product: the trivial theory 1 in which the vector space
attached to any pn ´ 1q-manifold is C, all correlation functions equal 1, and a similar triviality in
higher codimension. A theory F is invertible if there exists F 1 such that F b F 1 – 1.
Example 5.3. An n “ 1 theory F with H1 “ SO1 is determined by the vector space F ppt` q
attached to a point with positive orientation; it is invertible if and only if this vector space is
one-dimensional. (A one-dimensional vector space is called a line. A vector space V is invertible
if and only if there exists V 1 such that V b V 1 – C, and this happens if and only if V is a line.)
In an n-dimensional invertible field theory, the vector space attached to any pn ´ 1q-dimensional
manifold is a line and all correlation functions between nonzero operators are nonzero.
We first explain the transition to stable homotopy theory in the non-extended case, as in Example 5.3. The codomain, or target, of a non-extended topological field theory (Definition 2.33)
is the ordinary category VectC whose objects are complex vector spaces and whose morphisms are
linear maps. To accommodate theories with fermionic states, we use instead the codomain category sVectC of super vector spaces. An invertible theory F factors through the subcategory sLineC
whose objects are complex super lines21 and whose morphisms are invertible linear maps:
/ sVectC
:

F

Bordxn´1,ny pHn q
(5.4)
'

,

sLineC

The category sLineC is a groupoid : every morphism is invertible. Even more, it is a Picard groupoid :
every object is invertible under tensor product. The main point is that groupoids and Picard
groupoids come from topology, as we quickly review.
One of the first constructions in algebraic topology goes in the opposite direction:
(5.5)

πď1

Spaces ÝÝÝÝÑ Groupoids

21A Z{2Z-graded line is either even or odd, which means the single quantum state is either bosonic or fermionic.

<!-- page 34 -->
34

D. S. FREED AND M. J. HOPKINS

To any topological space S is attached a groupoid πď1 S whose objects are the points of S; the
set pπď1 Sqps0 , s1 q of morphisms from s0 P S to s1 P S is the set of homotopy classes of paths
from s0 to s1 . If the space has no higher homotopy information—S is a homotopy 1-type—then
πď1 S captures the homotopy type of S completely. There is an inverse construction that takes a
groupoid G (or a category) and attaches a homotopy 1-type }G}, the classifying space [Se3].
Example 5.6. Let S “ }sLineC }. Then π0 S – Z{2Z, since there are two isomorphism classes
of super line; and π1 S – Cˆ , since the automorphism group of any super line is the group Cˆ of
nonzero complex numbers under multiplication.
Remark 5.7. In Example 5.6 the groupoid sLineC is discrete: there is no topology on objects or
morphisms. If we use the standard topology on the morphism spaces of linear maps, then the
geometric realization }sLineC } is a homotopy 2-type with π0 – Z{2Z, π1 “ 0, and π2 – Z. In other
words, whereas in Example 5.6 the discrete group Cˆ of morphisms gives rise to π1 – Cˆ , with
the usual topology the group Cˆ deformation retracts to the circle (π0 “ 0, π1 – Z), and so its
homotopy groups show up one degree higher in the geometric realization.
A symmetric monoidal structure on a groupoid goes over to an infinite loop structure on the
classifying space S. That is, there exists a sequence X “ tS0 , S1 , S2 , . . . u of pointed spaces equipped
with homotopy equivalences Sq » ΩSq`1 , where S0 “ S and ΩSq`1 is the based loop space. These
satisfy the condition that Sq is pq ´ 1q-connected. We call X a spectrum and we call S its 0-space.
See §6 for a review of spectra.
Example 5.8. The classifying space } LineC } has only one nontrivial homotopy group π1 – Cˆ ,
so it is an Eilenberg-MacLane space KpCˆ , 1q. The corresponding Eilenberg-MacLane spectrum is
denoted ΣHCˆ : the 0-space of the spectrum HCˆ is a KpCˆ , 0q, for which a simple model is the
discrete group Cˆ , and the ‘Σ’ indicates a shift.
The functor (5.5) is the first in a sequence of functors tπ0 , πď1 , πď2 , . . . u in which the zeroth
maps a space to its set of path components and the higher ones map to higher groupoids. The
classifying space construction also works in this context, and it produces a space with potentially
nonzero homotopy groups in any degree.
A symmetric monoidal p8, nq-category B has a higher Picard groupoid quotient B, obtained by
formally adjoining inverses for every object and morphism. Also, a symmetric monoidal p8, nqcategory C has a maximal Picard subgroupoid Cˆ ãÑ C constructed by removing the non-invertible
objects and morphisms from C.
Definition 5.9. A fully extended field theory F : Bordn pHn q Ñ C is invertible if it admits a
factorization
(5.10)

Bordn pHn q


Bordn pHn q

F

Fr

/C
O
?
/ Cˆ

Passing to classifying spaces, Fr is equivalent to an infinite loop map
(5.11)

}F } : } Bordn pHn q} ÝÑ }Cˆ },

<!-- page 35 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

35

or equivalently a map of spectra. The homotopy type of the domain is given by the following
variation of the celebrated Galatius-Madsen-Tillmann-Weiss [GMTW] Theorem.
Theorem 5.12. } Bordn pHn q} is the 0-space of the Madsen-Tillmann spectrum Σn M T Hn .
One version of this theorem is proved in [BM], though it is only for unoriented manifolds and is
carried out for “n-uple categories” rather than p8, nq-categories. Proofs of Theorem 5.12 in the
context of p8, nq-categories have appeared in preprint form. The theorem is stated in [L, §2.5] as
a corollary of the cobordism hypothesis. A preprint of Ayala-Francis [AF] proves the cobordism
hypothesis and Theorem 5.12 for framed manifolds. A preprint by Schommer-Pries [S-P] contains
a complete proof of Theorem 5.12 independent of the cobordism hypothesis. Nonetheless, because
there is currently no published proof, in this paper we only use Theorem 5.12 as motivation and
formally define an invertible field theory as a map of spectra (Ansatz 5.14 below).
See §7.1 for a review of Madsen-Tillmann spectra.
5.3. Universal targets
There are two universal targets for invertible topological field theories, corresponding to the
discrete and continuous topologies on Cˆ . These targets are spectra; there is no need to define an
p8, nq-category C with non-invertible morphisms and objects as we only consider invertible theories.
The first target is constructed so that invertible n-dimensional field theories with that target
are determined by the partition function. The spectrum ICˆ is characterized in the homotopy
category of spectra by a functorial isomorphism
(5.13)

π0 : rB, ICˆ s ÝÑ Hompπ0 B, Cˆ q

from the abelian group of homotopy classes of spectrum maps B Ñ ICˆ to the character group
of π0 B, for any spectrum B. The shift Σn ICˆ satisfies a similar universal property with π0 replaced by πn . The spectrum ICˆ is closely related to the Brown-Comenetz dual to the sphere
spectrum [BC]. Combining with the discussion in §5.2 we arrive at the following.
Ansatz 5.14. A discrete invertible n-dimensional extended topological field theory with symmetry
group Hn is a spectrum map
(5.15)

F : Σn M T Hn ÝÑ Σn ICˆ .

The space of theories of this type is MappΣn M T Hn , Σn ICˆ q.
Here ‘Map’ indicates the space of maps between the indicated spectra; see (6.8) below. The word
‘discrete’ is meant to evoke the choice Σn ICˆ for the codomain: Cˆ has the discrete topology.
Remark 5.16. The choice of codomain spectrum Σn ICˆ , which implements the dictum ‘the partition
function determines the theory’, holds magic derived from the first few stable homotopy groups
of spheres. For example, the truncation to πxn´1,ny is a non-extended theory, and it takes values
in a groupoid equivalent to the groupoid sLineC of super lines: the homotopy groups of spheres
“knows about” the bosonic/fermionic grading of quantum states. The next Z{2Z in the stable stem
also has an interpretation in terms of statistics of particles; see [GK] where objects with nontrivial
Z{2Z-grading are termed ‘Majorana’.

<!-- page 36 -->
36

D. S. FREED AND M. J. HOPKINS

The spectrum Σn ICˆ is appropriate for classifying isomorphism classes of topological theories,
but we are interested instead in deformation classes: we want to identify two theories if there is a
continuous path of theories connecting them. For example, as maps into Σn ICˆ the Euler theories Fλ0 , Fλ1 in Example 4.21 are nonisomorphic if λ0 ­“ λ1 , whereas they are always deformation
equivalent. The Anderson dual Σn`1 IZp1q is the appropriate codomain to compute deformation
classes.22 Roughly speaking, it results from Σn ICˆ by taking the continuous topology on Cˆ . Its
universal property is expressed in the short exact sequence
0 ÝÑ Ext1 pπn B, Zp1qq ÝÑ rB, Σn`1 IZp1qs ÝÑ Hompπn`1 B, Zp1qq ÝÑ 0

(5.17)

which is non-canonically split. The kernel is the torsion subgroup:
rB, Σn`1 IZp1qstor – Ext1 pπn B, Zp1qq.

(5.18)
There is a map

φ : rB, Σn ICˆ s – Hompπn B, Cˆ q ÝÑ Ext1 pπn B, Zp1qq

(5.19)

onto the kernel of (5.17). It sends a homomorphism πn B Ñ Cˆ to the pullback of the exponential
group extension
exp

1 ÝÑ Zp1q ÝÑ C ÝÝÝÑ Cˆ ÝÑ 1.

(5.20)

If we give Cˆ its usual topology, then φ may be regarded as mapping the topological space
Hompπn B, Cˆ q to its group of path components.
Intuitively, to define the notion of deformation equivalence of theories (5.15) we want to consider
a second topology on MappΣn M T Hn , Σn ICˆ q induced from the continuous topology on Cˆ , and
then compute π0 . Instead we make use of the fibration
exp

HC ÝÝÝÑ ICˆ ÝÑ ΣIZp1q

(5.21)
induced from (5.20) as follows.

Definition 5.22. Theories α0 , α1 P MappΣn M T Hn , Σn ICˆ q are deformation equivalent if there
exists ξ P H n pΣn M T Hn ; Cq whose image under exp is the difference rα1 s ´ rα0 s of the isomorphism
classes rα0 s, rα1 s P rΣn M T Hn , Σn ICˆ s.
We immediately conclude the following.
Theorem 5.23. There is a 1:1 correspondence

(5.24)

$
,
&deformation classes of discrete invertible.
n-dimensional extended topological field – rΣn M T Hn , Σn`1 IZp1qstor .
%
theories with symmetry group Hn

22Zp1q “ 2π

?

´1Z Ă C avoids the choice of a particular

?

´1 P C.

<!-- page 37 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

37

This appears, at least implicitly, in a joint paper [FHT1] of the authors and Constantin Teleman;
Theorem 5.23 has been the basis of many investigations since.
It is natural to ask for a field theoretic interpretation of a map of spectra Σn M T Hn Ñ Σn`1 IZp1q
whose homotopy class is not torsion, so does not factor through Σn ICˆ . We give one in the next
subsection (Ansatz 5.26).
5.4. Remarks on non-topological invertible theories and low energy approximations
The main immediate application of Theorem 1.1 in this paper is to low-energy approximations
of gapped unitary quantum systems in case that approximation is invertible. For the heuristic
discussion in this section we momentarily drop the invertibility hypothesis.
A typical example of the phenomenon we wish to highlight is 3-dimensional Yang-Mills theory
with a Chern-Simons term. The coupling constant of the Chern-Simons term obeys an integrality constraint. Then the low energy effective theory is quantum “topological” Chern-Simons theory [W3]. In fact, this low energy theory is not topological; there is a mild metric dependence [W2].
One precise expression of the mildness is that the energy-momentum tensor23 is a multiple of the
identity operator, which is the only point operator in the theory anyhow. (See the discussion
in [GK, §1.1].) Witten observes that if one is willing to introduce some sort of framing, then the
long distance topological Chern-Simons theory is the tensor product of a purely topological theory
and an invertible theory. The invertible theory is analogous to a gravitational Chern-Simons theory,
but more precisely its partition function is the exponential of the Atiyah-Patodi-Singer η-invariant.
The coupling constant does not obey the usual integrality constraint, which is why the framing is required for this global decomposition. The full quantum Yang-Mills theory with Chern-Simons term
is a theory of oriented Riemannian manifolds (the Wick rotated symmetry group is H3 “ SO3 ),
and so one expects the same for the low-energy approximation. That indeed holds; it is only to
make a global decomposition into topological ˆ invertible that a framing is introduced.
This example violates the physical principle (ii) stated towards the beginning of §1. A more
precise expectation is that the low energy physics of a gapped system is well-approximated by
a theory whose energy-momentum tensor may depend on the the background fields, but as an
operator it is a multiple of the identity at each point. Or, at least locally we suppose the low
energy theory is topological ˆ invertible. If the low energy theory happens to be invertible, then
we conclude that any non-topological invertible theory can occur and that there is no shift of
symmetry group, e.g., no extra tangential structure is required. We expect that choices must be
made in constructing the low energy effective theory, so a potential ‘low energy approximation’
map from gapped theories to theories that are locally topological times invertible may only be
defined up to homotopy. (See [F4, §11.4] for another perspective on the appearance of a possibly
nontopological invertible theory.)
To illustrate the nature of the low energy approximation, we contemplate the following three
geometric objects associated to a smooth manifold M : (a) a principal Cˆ -bundle P Ñ M with
connection, (b) a principal Cˆ -bundle P Ñ M with flat connection, and (c) a principal Cˆ -bundle
P Ñ M (with no connection). In particular, we track what information is induced on the free
loop space LM “ MappS 1 , M q by integrating over the loop. In (a) we obtain a smooth function
23The energy-momentum tensor is a multiple of the Cotton tensor of the Riemannian 3-manifold.

<!-- page 38 -->
38

D. S. FREED AND M. J. HOPKINS

LM Ñ Cˆ , the holonomy, and if there is nonzero curvature then it has nonzero derivative. In (b)
the holonomy is a locally constant function LM Ñ Cˆ , and therefore we can use the discrete
topology on Cˆ : the holonomy represents a class in H 0 pLM ; Cˆ q. In (c) there is no connection,
so no holonomy, but nonetheless we can extract a principal Zp1q-bundle EP Ñ LM , a fiber bundle
of Zp1q-torsors. Namely, an element λ P Cˆ determines a Zp1q-torsor Eλ Ă C of all x P C
such that exppxq “ λ, and so the holonomy function LM Ñ Cˆ of a connection Θ P AP on
P Ñ M determines EP,Θ Ñ LM , so a Zp1q-torsor over AP ˆ LM . Since the affine space AP
of connections is contractible, the principal Zp1q-bundle over AP ˆ LM descends to a principal
Zp1q-bundle EP Ñ LM . It may be regarded as the homotopical information in a connection. It
determines a class in the sheaf cohomology group H 0 pLM ; Cˆ q in which Cˆ has the continuous
topology. Since Cˆ is an Eilenberg-MacLane space with π1 – Zp1q, there is an isomorphism
(5.25)

–

H 0 pLM ; Cˆ q ÝÝÑ H 1 pLM ; Zp1qq.

Returning to invertible field theories24 we have the following situations: (a) a non-topological theory, as contemplated in Remark 2.39; (b) a discrete invertible topological theory, as in Ansatz 5.14;
and (c) a topological field theory whose partition “function” is a Zp1q-torsor rather than a complex
number. While (a) and (b) have clear analogs for non-invertible field theories, it is unclear what a
non-invertible analog of (c) would be. In the invertible case we posit the following definition of a
type (c) theory.
Ansatz 5.26. A continuous invertible n-dimensional extended topological field theory with symmetry group Hn is a spectrum map
(5.27)

ϕ : Σn M T Hn ÝÑ Σn`1 IZp1q.

The space of theories of this type is MappΣn M T Hn , Σn`1 IZp1qq.
Remark 5.28. In differential geometry a principal Cˆ -bundle P Ñ M has a primary topological
`
˘
invariant in H 2 M ; Zp1q , its Chern class. A connection gives a secondary geometric invariant, its
holonomy. If the connection is flat, the secondary invariant is also topological (discrete), and in that
`
˘
case the Chern class lies in the torsion subgroup of H 2 M ; Zp1q . The stable continuous invertible
field theories we encounter in §7.2 attach a primary Zp1q-valued invariant to closed pn`1q-manifolds.
A discrete invertible topological field theory F (Ansatz 5.14) gives rise to a continuous invertible
topological field theory ϕ, which retains the homotopical information in F , in particular its deformation class. In this paper we do not develop the theory of non-topological field theories, but in
the invertible case we use instead continuous topological theories, which represent the homotopical
information carried by a geometric theory.
Remark 5.29. In the application to low energy approximations of gapped theories, we expect that
only this homotopical shadow of a geometric theory is well-defined, due to the choices in constructing
a low energy theory.
24Note that each of (a), (b), and (c) above determines the corresponding type of invertible 1-dimensional field

theory of oriented manifolds equipped with a map to M .

<!-- page 39 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

39

6. Equivariant stable homotopy theory
Reflection symmetry in invertible topological theories is expressed by a Z{2-action on the constituent spectra. This requires working in Z{2-equivariant stable homotopy theory. What we will
use here is Borel equivariant homotopy theory. This is somewhat easier than the more general
theory, and at the moment is all that seems needed for our main results. There are many places
to read about equivariant stable homotopy theory. The reader may wish to consult [Ad], [GM],
[HHR, Chapter 2], [Sch] and [tD, Chapter 8].
6.1. Spectra
Let T be the category of pointed topological spaces, and for A, B P T write T pA, Bq for the set
of basepoint preserving continuous functions from A to B and T pA, Bq for the same set, regarded
as a topological space with the compact open topology.
A spectrum X is a sequence tX0 , X1 , . . . u of pointed spaces, equipped with structure maps
sn : S 1 ^ Xn Ñ Xn`1 . A map X Ñ Y of spectra is a sequence of maps Xn Ñ Yn making the
diagrams
S 1 ^ Xn

sX
n



S 1 ^ Yn

sY
n

/ Xn`1

/ Yn`1

commute. The set of spectrum maps from X to Y is a subset of
ź

T pXn , Yn q

n

and so may be regarded as a topological space with the subspace topology. The space of maps
between spectra X and Y will be denoted SpX, Y q.
The homotopy groups πn X of a spectrum X are defined for n P Z by
(6.1)

πn pXq “ lim
ÝÑ πn`k Xn`k
k

in which the bonding maps are given by the suspension mapping
Σ

sn`k

πn`k Xn`k Ý
Ñ πn`k`1 ΣXn`k ÝÝÝÑ πn`k`1 Xn`k`1 .
The group πn`k Xn`k is defined for any n P Z as soon as k ě ´n. A map X Ñ Y is a weak
equivalence if it induces an isomorphism of homotopy groups.
Equipped with the weak equivalences, the category S of spectra becomes a bona fide place for
doing homotopy theory. A functor S Ñ C to a category C is a homotopy functor if it takes weak
equivalences to isomorphisms. There is a universal homotopy functor S Ñ ho S characterized by
the property that the restriction mapping gives an equivalence between the category of functors

<!-- page 40 -->
40

D. S. FREED AND M. J. HOPKINS

ho S Ñ C with the category of homotopy functors S Ñ C. The category ho S is the homotopy
category of spectra, and the set (in fact abelian group) ho SpX, Y q is called the abelian group of
homotopy classes of maps from X to Y . We will use the common abbreviation
rX, Y s “ ho SpX, Y q.
Example 6.2. The suspension spectrum Σ8 Z of a space Z is the spectrum
` 8 ˘
Σ Z n “ Sn ^ Z
with the structure maps derived from the equivalence S 1 ^ S n “ S n`1 . When the context is clear
it is customary to drop the Σ8 and not distinguish in notation between a space nd its suspension
spectrum.
Example 6.3. For a non-negative integer k ě 0 let S k be the suspension spectrum of the k-sphere
and S ´k be the spectrum defined by
#
` ´k ˘
S
“
n

˚
S n´k

năk
.
něk

From the formula (6.1) one easily checks that for all k P Z one has an isomorphism
rS k , Xs « πk X
natural in X.
6.1.1. Smash product. Suppose that X “ tXn u is a spectrum and Z is a space. Define X ^ Z to
be the spectrum with
`
˘
X ^ Z n “ Xn ^ Z
and the structure maps derived from those of X. This is the smash product of the spectrum X
with the space Z.
Example 6.4. The spectrum S 0 ^ Z is the suspension spectrum of Z.
Example 6.5. The spectrum S ´k ^ S k consists of the spaces
#
` ´k
˘
S ^ Sk m “

˚
Sm

There is an inclusion
S ´k ^ S k Ñ S 0
which is easily checked to be a weak equivalence.

măk
m ě k.

<!-- page 41 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

41

For a spectrum X “ tXn u there is a functorial weak equivalence
«

´n
ho lim
Ñ X.
ÝÑ S ^ Xn Ý

(6.6)

(See, for example [HHR, §2.2.1] where it is called the canonical homotopy presentation.)
There is an enrichment ho S of ho S over the homotopy category of spaces. It is characterized by
the existence of an isomorphism
ho T pZ, ho SpX, Y qq « ho SpX ^ Z, Y q

(6.7)

functorial in CW complexes Z, and spectra X and Y . We will employ the abbreviation
MappX, Y q “ ho SpX, Y q.

(6.8)

Taking Z to be the space S 0 in (6.7) gives the isomorphism
rX, Y s “ π0 MappX, Y q.
When the spectrum X “ tXn u has the property that each Xn is a CW complex and Y has the
property that each map
Yn Ñ ΩYn`1
is a weak equivalence, the homotopy type of MappX, Y q is given by
lim
ho SpX, Y q “ ho Ð
Ý MpXn , Yn q,

(6.9)

with MpXn , Yn q is the homotopy limit of the diagram
T pXn , Yn q
!

T pXn´1 , Yn´1 q
}

„

T pXn´1 , ΩYn q

!

T pX0 , Y0 q
}

„

...

T pXn´2 , ΩYn´1 q

!

}

„

T pX0 , ΩY1 q

in which the southeast arrows are given by the compositions
T pXm , Ym q Ñ T pS 1 ^ Xm´1 , Ym q « T pXm´1 ΩYm q.
Note that the projection map MpXn , Yn q Ñ T pXn , Yn q is a weak equivalence, so that (6.9) can
heuristically be interpreted as giving a presentation of ho SpX, Y q as a homotopy inverse limit of
the spaces T pXn , Yn q.
A spectrum Y with the property that for all n the map Yn Ñ ΩYn`1 is a weak equivalence is
called an Ω-spectrum (or a loop spectrum). Every spectrum Y is naturally weakly equivalent to an
Ω-spectrum. Indeed, given Y define LY by
k
LYn “ ho Ý
lim
Ñ Ω Yn`k .

Using the homeomorphism ΩpΩk Yn`k q « Ωk ΩYn`k one sees that LY has the structure of an Ωspectrum and that the canonical map Y Ñ LY is a weak equivalence.

<!-- page 42 -->
42

D. S. FREED AND M. J. HOPKINS

6.1.2. Duality. The operation X ^ Z extends to a symmetric monoidal smash product on spectra.
In fact there is a unique extension having the property that it commutes with colimits in both
variables, and for spaces Z1 and Z2 and integers k, ` ě 0 one has
` ´k
˘ `
˘
S ^ Z1 ^ S ´` ^ Z2 » S ´pk``q ^ Z1 ^ Z2 .
The existence and uniqueness can be deduced from the canonical homotopy presentation (6.6).
Equipped with the smash product the categories ho S and ho S become symmetric monoidal
categories. By Example 6.5 the suspension spectra of spheres are dualizable (in fact invertible). It
follows that the suspension spectrum of any finite CW complex is also dualizable.
6.1.3. Stability. An easy check (or an appeal to the invertibility of spheres) shows that for all k
and all X the map
πk X Ñ πk`1 X ^ S 1
is an isomorphism. This implies a map A Ñ X gives rise to a long exact sequence
¨ ¨ ¨ Ñ πk A Ñ πk X Ñ πk X Y CA Ñ πk´1 A Ñ . . .
in which X Y CA is the spectrum
`
˘
X Y CA n “ Xn Y CAn
with CA “ A ˆ r0, 1s{A ˆ t1u Y ˚ ˆ r0, 1s. This, in turn, implies that the map from A to the
homotopy fiber of X Ñ X Y CA is a weak equivalence.
6.1.4. Thom Spectra. Let X be a space. Given a map V : X Ñ BO, define a sequence of maps
Vn : Xn Ñ BOn by the homotopy pullback squares
(6.10)

Xn
Vn



BOn

/X


V

/ BO .

The map Vn : Xn Ñ BOn classifies a vector bundle of rank n over Xn (which will also be denoted
Vn ). By construction, the pullback of Vn`1 Ñ Xn`1 to Xn comes equipped with an isomorphism
to Vn ‘ R Ñ Xn . This give a map of Thom spaces
Σ ThompXn ; Vn q “ ThompXn ; Vn ‘ 1q Ñ ThompXn`1 , Vn`1 q
making the sequence of spaces tThompXn ; Vn qu into a spectrum. This is the Thom spectrum of V ,
denoted ThompX; V q. The canonical homotopy presentation of ThompX; V q takes the form
´n
ThompX; V q “ ho Ý
lim
Ñ S ^ ThompXn ; Vn q.

<!-- page 43 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

43

We will also encounter the Thom spectrum ThompX; ´V q associated to a map V : X Ñ BO by
composing with the “additive inverse” map p´1q : BO Ñ BO (see §7.1). With Xn and Vn defined
as in (6.10), the isomorphism
Vn`1 |Xn « Vn ‘ R
becomes
´Vn`1 |Xn « ´Vn ´ R.
This leads to maps
ThompX; ´Vn q Ñ S 1 ^ ThompXn`1 ; ´Vn`1 q,
and an alternative presentation
(6.11)

n
ThompX; ´V q “ ho Ý
lim
Ñ S ^ ThompXn ; ´Vn q.

If V has virtual dimension d then V ´ Rd has virtual dimension 0 and one defines
ThompX; V q “ S d ^ ThompX; V ´ Rd q.
The Thom spectrum construction is a functor on the category of spaces over the classifying
space Z ˆ BO of KO-theory. It is symmetric monoidal in the sense that for V : X Ñ Z ˆ BO and
W : Y Ñ Z ˆ BO there is a natural weak equivalence
˚
ThompX ˆ Y ; πX
V ‘ πY˚ W q « ThompX; V q ^ ThompY ; W q,

in which πX and πY are the projections.
6.2. Borel equivariant stable homotopy theory
Now suppose that G is a compact Lie group (which in our case will be Z{2) and let ShG be the
category of spectra equipped with a G action, and equivariant maps. An object of ShG consists of
a sequence tXn , sn u of left G-spaces Xn and equivariant maps S 1 ^ Xn Ñ Xn`1 in which S 1 has
the trivial G-action. Sometimes what we are calling a G-spectrum is called a naive G-spectrum.
Definition 6.12. A map X Ñ Y in ShG is a Borel weak equivalence if it is a weak equivalence
when regarded as a map in S.
Equipped with the Borel weak equivalences, the category ShG becomes a category in which one
can do homotopy theory. The homotopy category ho ShG is defined as the target of the universal
homotopy functor out of ShG . We will use the abbreviation
rX, Y shG “ ho ShG pX, Y q.
The construction of the smash product goes through in a straightforward way for the Borel
equivariant spectra, and there is a derived equivariant mapping space between two equivariant

<!-- page 44 -->
44

D. S. FREED AND M. J. HOPKINS

spectra. In fact, it follows from the expression (6.9) that when X and Y are G-spectra, the space
ho SpX, Y q acquires the homotopy type of a G-space. The derived equivariant mapping space works
out to be homotopy fixed point space
MapG pX, Y q “ MappX, Y qhG ,
and the maps in the homotopy category of G-spectra are given by
rX, Y shG “ π0 MappX, Y qhG .
In Borel equivariant homotopy theory the suspension spectra of finite G-sets (with a disjoint base
point added) are self dual. This implies that the suspension spectra of finite G-CW-complexes are
dualizable and the suspension spectrum of the one point compactification S V of a finite dimensional
representation V of G is invertible. These facts are not quite immediate. If X is a finite G-set,
then the evaluation map
X` ^ X` Ñ S 0
is the map of suspension spectra induced by the map
X ˆ X Ñ S0
sending the diagonal to the non base point and the complement of the diagonal to the base point.
It is not so straightforward to write down the coevaluation map. Nevertheless, for G-spectra W
and Z, the composite
MappZ, W ^ X` q Ñ MappZ ^ X` , W ^ X` ^ X` q Ñ MappZ ^ X` , W q
is a G-equivariant map that is a weak equivalence of underlying spaces, and so gives an equivalence
MappZ, W ^ X` qhG « MappZ ^ X` , W qhG
and an isomorphism
rZ, W ^ X` shG « rZ ^ X` , W shG .
Once one knows that the finite G-sets are dualizable it follows that the suspension spectrum
of any finite G-CW-complex is dualizable. We denote the dual of X as DpXq. This implies the
invertibility of S V since the map
DpS V q ^ S V Ñ S 0
is a weak equivalence of underlying spectra. It is customary to use the notation
S ´V “ DS V .
For more on virtual representation spheres see Example 6.17 of §6.2.2.

<!-- page 45 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

45

6.2.1. Homotopy fixed points and homotopy orbits. Regarding a non-equivariant spectrum as a
G-spectrum with the trivial action gives a functor
S Ñ ShG .
This functor preserves weak equivalences and so induces a functor on homotopy categories. The
homotopy orbit and fixed point functors provide both a left and right adjoint to this induced
functor.
Recall that the homotopy orbit space of a pointed G-space Z is the space
ZhG “ EG` ^ Z,
G

and that the homotopy fixed point space is the space
Z hG “ T pEG` , ZqG
of equivariant basepoint preserving maps from EG` to Z. These notions extend component-wise
to equivariant spectra. The homotopy orbit spectrum of a G-spectrum X “ tXn u is the spectrum
1
XhG “ tpXn qhG u and the pre homotopy fixed point spectrum is the spectrum X h G “ tpXn qhG u.
The functor XhG preserves weak equivalences and so directly induces a functor on homotopy
1
categories. The functor X h G preserves weak equivalences between Ω-spectra and so induces a
homotopy fixed point functor
p ´ qhG : ho ShG Ñ ho S
1

sending X to pLXqh G .
These functors on the homotopy category are adjoints to the inclusion
ho S Ñ ho ShG
in the sense that there are natural isomorphisms
(6.13)

rX, AshG « rXhG , As

(6.14)

rA, Y shG « rA, Y hG s

in which X and Y are G-spectra and A is a spectrum with trivial G-action. Also, the fixed point
spectrum AhZ{2 is computed as
(6.15)

»

»

MapZ{2 pS 0 , Aq » MappBZ{2` , Aq Ð
Ý A _ MappBZ{2, Aq Ý
Ñ A ˆ MappBZ{2, Aq,

in which the left pointing map involves a choice of a basepoint x P BZ{2 and is the sum of the map
BZ{2` Ñ S 0
sending BZ{2 to the non basepoint and the map
BZ{2` Ñ BZ{2
which is the identity map on BZ{2 and sends the disjoint base point on the left to the new basepoint
on the right.

<!-- page 46 -->
46

D. S. FREED AND M. J. HOPKINS

6.2.2. Equivariant Thom spectra. Suppose that B is a space and p : X Ñ B is a principal Gbundle. A map W : B Ñ BO leads, as above, to a sequence of maps
/ Bn`1

Bn


Wn



Wn`1



/ BOn`1

BOn
and a Thom spectrum ThompB; W q “
by the pullback square

/B
W

/ BO

(
ThompBn ; Wn q . Define principal G-bundles Xn Ñ Bn
Xn
pn



Bn

/X


p

/ B.

The bundle p˚n Wn is a G-equivariant vector bundle on Xn . In fact, by descent, the data of a Gequivariant vector bundle on Xn is equivalent to the data of a vector bundle over Bn . The G-action
on pXn , p˚ Wn q induces a G-action on the Thom spectrum ThompX, p˚ W q “ tThompXn ; p˚n Wn qu
making it into an equivariant spectrum. By construction the homotopy orbit spectrum is given by
(6.16)

ThompX; p˚ W qhG “ ThompB; W q.

As in §6.1.4, equivariant Thom spectra for maps B Ñ Z ˆ BO are defined by subtracting a
suitable trivial bundle and suspending the result.
Example 6.17 (Representation spheres). An element V P KO0 pBGq is classified by a map
V : BG Ñ Z ˆ BO
and so gives rise to an equivariant Thom spectrum. When V corresponds to a representation of G
the equivariant Thom spectrum is the spectrum S V . This construction sends sums of elements of
KO0 pBGq to smash products of G-spectra. Composing with the map
ROpGq Ñ KO0 pBGq
gives a construction of a sphere S V associated to every virtual representation V of G. This gives
another approach to the construction and invertibility of representation spheres in Borel equivariant
stable homotopy theory.
6.2.3. The σ-sphere. We now specialize to the case G “ Z{2, and write σ for the real sign representation. The sphere S σ has an equivariant cell decomposition with one non-basepoint fixed 0-cell,
and one free 1-cell as shown here.

<!-- page 47 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

47

This gives a pushout square
Z{2 ˆ BD1

/ Z{2 ˆ D 1




/ Sσ

S0
leading to a cofibration sequence
(6.18)

Z{2` Ñ S 0 Ñ S σ

of equivariant spectra. Passing to duals and using the self-duality of finite G-sets gives a cofibration
sequence
(6.19)

S ´σ Ñ S 0 Ñ Z{2` .

The map S 0 Ñ Z{2` is the transfer map and, non-equivariantly, has degree 1 on each summand of
Z{2` “ S 0 _ S 0 .
Write
γ “1´σ
δ “ σ ´ 1.
For a Z{2-spectrum X we define

(6.20)

X δ “ Sδ ^ X
X γ “ S γ ^ X.

Smashing with (6.18) and (6.19) gives for any X, (co-)fibration sequences

(6.21)
(6.22)

X δ Ñ Z{2` ^ X Ñ X

and
γ

X Ñ Z{2` ^ X Ñ X .

<!-- page 48 -->
48

D. S. FREED AND M. J. HOPKINS

6.3. Real structures
Our next aim is to equip ICˆ and IZp1q with Z{2-actions corresponding to complex conjugation,
in such a way that the cofibration sequence (see (5.21))
(6.23)

exp

IZp1q Ñ HC ÝÝÑ ICˆ

is a cofibration sequence of Z{2-equivariant spectra. Though there no mystery about the action
on the abelian group-valued functor r ´ , ICˆ s, there are infinitely many refinements of this to an
action on the spectrum ICˆ . Here we will motivate a specific choice, and check it against three
situations in which there is a naturally occurring action.
6.3.1. Z{2-actions. The space of Z{2-actions on a spectrum X is the space of maps
BZ{2 Ñ B hAutpXq
from the classifying space of Z{2 to the classifying space of the monoid of self homotopy equivalences
of X. Smashing a map S 0 Ñ S 0 with the identity map of X gives a map
B hAutpS 0 q Ñ B hAutpXq.
The maps BZ{2 Ñ B hAutpS 0 q then correspond both to (i) Z{2-actions on S 0 and (ii) Z{2-actions
on all spectra which are natural in the sense that they commute with all maps and are homotopy
colimit preserving. Put more succinctly, the “natural” Z{2-actions are homotopy colimit preserving
sections of the forgetful functor
ShZ{2 Ñ S.

(6.24)

Associating to a vector space its one point compactification defines a map
BO Ñ B hAutpS 0 q,
so that a virtual representation V of Z{2, of virtual dimension 0, determines a natural Z{2-action
via the composition
V

BZ{2 Ý
Ñ BO Ñ B hAutpS 0 q.
The corresponding section of (6.24) is the one sending a spectrum X to S V ^ X.
Remark 6.25. Because S 0 is the tensor unit in S, the space B hAutpS 0 q is actually an infinite loop
space. The map BO Ñ B hAutpS 0 q also turns out to be an infinite loop map. This means that
“natural” Z{2-actions may be composed, and that the composition of actions corresponding to
virtual representations V and W is the natural action corresponding to V ‘ W .

<!-- page 49 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

49

Remark 6.26. From the defining property of IZp1q one can check that the map
MappS 0 , S 0 q Ñ MappIZp1q, IZp1qq
f ÞÑ f ^ id
is a weak equivalence. Now the loop space of any component of the space of maps BZ{2 Ñ
B hAutpS 0 q is the space of maps BZ{2 Ñ hAutpS 0 q. The homotopy type of this latter space falls
within the purview of the Segal conjecture, and consists of the path components of QBZ{2` ˆ QS 0
whose first component is a generator of
π0 QBZ{2` « Z.
For this reason, one knows a lot about the space of actions of Z{2 on IZp1q, and in particular that
there are infinitely many inequivalent actions inducing the sign representation on π0 IZp1q.
For the spectrum HC one has B hAutpHCq « KpAutpCq, 1q, in which AutpCq is the group of
abelian group automorphisms of C. In this case there is no difference between Z{2-actions on HC
and Z{2-actions on C, and complex conjugation is uniquely specified.
6.3.2. Duality. Spectra with no negative homotopy groups are modeled by (higher) Picard groupoids.
Picard groupoids come equipped with a Z{2-action sending each object to its inverse. This corresponds to a natural Z{2-action on spectra which we now determine.
Let C be a Picard category and consider the category of pairs px, yq equipped with an isomorphism
x b y Ñ 1. The functor px, yq ÞÑ x is an equivalence of categories, so the Z{2-action sending x to
its inverse corresponds to the action on the category of pairs sending
xby Ñ1
to
y b x Ñ x b y Ñ 1.
If C corresponds to a spectrum X then the category of pairs corresponds to X _ X « X ˆ X, and
the category of pairs px, yq equipped with an isomorphism x b y Ñ 1 is the homotopy fiber of the
map
X _ X Ñ X.
Writing this in terms of equivariant spectra we are looking at the homotopy fiber of
Z{2` ^ X Ñ X,
which by (6.21) is X δ .
Summarizing, we have the following.
Proposition 6.27. The natural Z{2-action corresponding to “duality” is given by the map
δ

BZ{2 Ý
Ñ BO Ñ B hAutpS 0 q
and associates to a spectrum X, the Z{2-equivariant spectrum
X δ “ S δ ^ X “ S σ´1 ^ X.

<!-- page 50 -->
50

D. S. FREED AND M. J. HOPKINS

6.3.3. Complex conjugation. A complex conjugation on IZp1q corresponds to a map
ν : BZ{2 Ñ B hAutpIZp1qq
having at least the property that its effect on π1 is the sign representation of Z{2 on Zp1q. Write
`
˘
T BZ{2, B hAutpIZp1qq c
`
˘
for the space of maps inducing this homomorphism on π1 . The space T BZ{2, B hAutpIZp1qq c is
`
˘
a union of infinitely many path components of T BZ{2, B hAutpIZp1qq (see Remark 6.26).
Similarly, complex conjugation on ICˆ corresponds to a map
ν 1 : BZ{2 Ñ B hAutpICˆ q,
whose effect on π1 corresponds to the action of Z{2 by complex conjugation on Cˆ .
`
˘
T BZ{2, B hAutpICˆ q c for this space of maps.
Since the maps

Write

MappIZp1q, HCq Ñ HompZp1q, Cq
MappHC, ICˆ q Ñ HompC, Cˆ q
are weak equivalence, so are the maps
MappIZp1q, HCqhZ{2 Ñ HompZp1q, CqZ{2
MappHC, ICˆ qhZ{2 Ñ HompC, Cˆ qZ{2
for any Z{2-actions on IZp1q and ICˆ . It follows that any action ν as above extends uniquely to
a Z{2-equivariant map
IZp1qν Ñ HC
and so induces a Z{2-action ν 1 on the cofiber ICˆ . Similarly an action ν 1 as above induces a
Z{2-action ν on IZp1q. In this way we have an equivalence
(6.28)

`
˘
`
˘
T BZ{2, B hAutpIZp1qq c « T BZ{2, B hAutpICˆ q c .

The space of real structures on IZp1q and ICˆ will be defined to be a single path component of
the above spaces. Before specifying which one, we turn to a motivating example.
Example 6.29 (Hermitian structures and positivity). Let f VectC be the topological groupoid of
finite dimensional complex vector spaces and (complex) linear isomorphisms, endowed with the

<!-- page 51 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

51

symmetric monoidal structure of b. For V P f VectC , let V ˚ be the dual vector space. We define a
covariant “duality” functor V ÞÑ V _ by
V_ “V˚
` ˘´1
f_ “ f˚
.
The canonical isomorphism V __ « V extends the functor V _ to a Z{2-action on f VectC . (See
Appendix B.) There is another Z{2-action
V ÞÑ V
gotten by redefining scalar multiplication by x P C to be scalar multiplication by x̄.
Let f Vectpos
C be the topological groupoid of finite dimensional complex vector spaces equipped
with a positive definite Hermitian inner product, and unitary transformations. Since the inclusion
U pnq Ă GLn pCq is a homotopy equivalence, the functor
f Vectpos
C Ñ f VectC
is a weak equivalence of topological categories. On f Vectpos
C the Hermitian inner product gives
˚
a natural isomorphism V « V , trivializing the composition “bar star” of the two Z{2-actions
defined above. This suggests that whatever complex conjugation is, on the categories in which C
is regarded as having a topology, the combined action (in the sense of Remark 6.25) of complex
conjugation and duality should be trivializable. The trivialization is non-canonical, however. One
might have chosen negative definite vector spaces, or, for each prime p made a choice of positive or
negative definite Hermitian inner products on vector spaces of dimension p and then extend to all
finite dimensional vector spaces by tensoring.
With Example 6.29 as motivation, and in view of Proposition 6.27, we propose the following.
Definition 6.30. The space of real structures on IZp1q is the path component of the space
(6.31)

`
˘
T BZ{2, B hAutpIZp1qq c

containing the map 1 ´ σ. The space of real structures on ICˆ is the path component of the
`
˘
space T BZ{2, B hAutpICˆ q c corresponding to the space of real structures on IZp1q under the
equivalence (6.28).
As above, we write IZp1qν for the Z{2-spectrum corresponding to a real structure ν : BZ{2 Ñ
B hAutpIZp1qq. Any real structure fits canonically into a cofibration sequence
(6.32)

1

exp

IZp1qν ÝÑ HCν ÝÝÝÑ pICˆ qν

1

in which ν and ν 1 correspond under the equivalence (6.28); the superscript on HC is the unique
complex conjugation, explained at the end of §6.3.1.

<!-- page 52 -->
52

D. S. FREED AND M. J. HOPKINS

Remark 6.33. Since the space of real structures ν on IZp1q is connected, but not contractible, any
IZp1qν is non-canonically equivariantly equivalent to IZp1qγ “ S 1´σ ^ IZp1q.
Ansatz 6.34. We use the basepoint in (6.31) to fix once and for all ν “ γ “ 1 ´ σ. Under the
equivalence (6.28) this determines a real structure ν01 on ICˆ . Our choices render the cofibration
sequence (6.32) as
1

exp

1

IZp1qγ ÝÑ HCν0 ÝÝÝÑ pICˆ qν0

(6.35)

Remark 6.36. The real structure γ on IZp1q is the restriction of a natural action of Z{2; the
corresponding real structure ν01 is not. However, in terms of the polar decomposition Cˆ “ T ˆ Rą0
we have
1

pICˆ qν0 « IT ^ S 1´σ _ HRą0 .

(6.37)

The spectrum IT is characterized in the homotopy category of spectra by a functorial isomorphism
–

rB, ITs ÝÝÑ Hompπ0 B, Tq

(6.38)

for all spectra B, analogous to (5.13). The equivariant spectrum ITγ “ IT ^ S 1´σ fits into a
cofibration sequence analogous to (6.35):
1

exp

1

IZp1qγ ÝÑ HRp1qν0 ÝÝÝÑ ITν0

(6.39)

Remark 6.40. This definition of real structure fits with the three cases in which one has an algebraic
interpretation of IZp1q (see Remark 5.16). The zeroth space of ΣIZp1q is modeled by the unit
complex numbers with the usual topology; that of Σ2 IZp1q corresponds to the symmetric monoidal
groupoid of Z{2-graded complex lines; and Σ3 IZp1q to the Brauer-Wall symmetric monoidal 2groupoid of Z{2-graded simple algebras over C, Z{2-graded bimodules and intertwiners. These
three models come equipped with natural real structures, coming from change of scalars. By
direct computation one can show that the homotopy fixed points of Σi IZp1qγ is modeled by the
corresponding real versions of the three categories described above. To check this it suffices to do
so when i “ 3 as the other cases are gotten from it by passing to loop spaces. The real Brauer-Wall
category corresponds to a spectrum B with the following homotopy groups
πi B “ 0

i R r0, 3s

π0 B “ Z{8

(the eight real Clifford algebras)

π1 B “ Z{2

(the even and odd real line)

π2 B “ t˘1u
and has the property that the multiplication by η maps
π0 B Ñ π1 B Ñ π2 B

<!-- page 53 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

53

are non-zero. A straightforward computation shows that any spectrum X with these properties is
homotopy equivalent to B. To verify the claim it therefore suffices to show that the p´1q-connected
`
˘hZ{2
cover of Σ3 IZp1qγ
has these properties. We therefore need to know the groups
`
˘hZ{2
πi Σ3 IZp1qγ

iě0

and the effect of multiplication by η. Now for the real structure γ “ 1 ´ σ one has
MappS 0 , Σ3 IZp1qγ qhZ{2 « MappS 0 , S p1´σq ^ Σ3 IZp1qqhZ{2
« MappS pσ´1q , Σ3 IZp1qqhZ{2
pσ´1q

« MappShZ{2 , Σ3 IZp1qq
« MappThompBZ{2; σ ´ 1q, S 3 ^ IZp1qq,
by (6.13) and (6.16). We therefore need information about
rThompBZ{2; σ ´ 1q, S i ^ IZp1qs

1ďiď3

or, from the defining property of IZp1q, the character groups of
πi ThompBZ{2; σ ´ 1q 0 ď i ď 2.
As described in §10, these groups coincide with the same homotopy groups of M T Pin´ and are
shown in Figure 5 (the case s “ 1) to be the groups Z{2, Z{2, and Z{8 with both η-multiplications
non-zero.
6.3.4. Terminology. It will be convenient in the sequel to have names for the objects assigned to
closed manifolds of arbitrary codimension in an invertible field theory. In codimension 0 we have
a complex number and in codimension 1 an object in the category of complex Z{2Z-graded lines
with the monoidal structure of graded tensor product and the Koszul sign in the symmetry. We
refer to such an object as a ‘complex super line’ or a ‘Z{2Z-graded line’. Hence in codimension k
we introduce the term ‘complex super k-line’.25
Definition 6.41.
(i) IZp1q is the spectrum of higher complex super lines;
`
˘hZ{2
(ii) IZp1qγ
is the spectrum of higher real super lines;
(iii) IZp1qH :“ pIZp1qγ ^ S σ´1 qhZ{2 is the spectrum of higher Hermitian super lines;
(iv) ICˆ is the spectrum of higher flat complex super lines;
(v) The k th space in the spectrum IZp1q is the space of complex super k-lines.
25Kapranov [Kap, §3.4] suggests a higher use of super based on the sphere spectrum.

<!-- page 54 -->
54

D. S. FREED AND M. J. HOPKINS

Example 6.29 is the motivation for (iii). There are analogs of (iv) and (v) for real and Hermitian
super lines. For example, the fixed point spectrum
(6.42)

1

ˆ ν0
σ´1 hZ{2
ICˆ
q
H :“ ppIC q ^ S

is the spectrum of higher flat Hermitian super lines, and the k th space of that spectrum is the space
of flat Hermitian super k-lines. As for the fixed point spectrum in (iii), since S 1´σ ^ S σ´1 is the
sphere spectrum with the trivial Z{2-action—the “bar star” involution—we deduce from (6.15) a
canonical identification
(6.43)

`
˘
IZp1qH “ Map BZ{2` , IZp1q .

Pulling back along BZ{2 Ñ pt we obtain a map
(6.44)

IZp1q ÝÑ IZp1qH ;

the image is a summand, split by a choice of point in BZ{2.
Definition 6.45. The image IZp1qpos of (6.44) is the spectrum of higher positive definite Hermitian
super lines.
The k th space in IZp1qpos is the space of positive definite Hermitian super k-lines. Define the
spectrum of higher flat positive definite Hermitian super lines as the homotopy pullback

(6.46)

ICˆ
pos

/ ΣIZp1qpos




/ ΣIZp1qH .

ICˆ
H

We examine this homotopy-theoretic definition of positivity by focusing on the top piece, first in
the ungraded case and then in the Z{2Z-graded case.
Example 6.47 (Hermitian lines). Consider the spectrum Σ2 HZ. Its zero-space represents the ordinary groupoid of complex lines; morphisms have the continuous topology. There is a contractible
space of trivializable involutions, and we imagine a point in it to represent bar star. The analog
of (6.43) implies that the set of components of the fixed point spectrum of any such involution is
(6.48)

π0 MappBZ{2` , Σ2 HZq “ π0 Σ2 HZ ‘ π0 MappBZ{2, Σ2 HZq “ t0u ‘ Z{2.

The zero space of MappBZ{2` , Σ2 HZq represents the groupoid of Hermitian lines, the Z{2Z tracks
the sign of the Hermitian form. The positive subspace, obtained by pulling back along BZ{2 Ñ pt,
picks out the positive definite forms.

<!-- page 55 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

55

Example 6.49 (super Hermitian lines). The zero-space of the spectrum Σ2 IZp1q represents the
groupoid of super lines L with continuous topology on morphisms. We compute the set of components of the fixed point spectrum of a trivializable involution:
(6.50)

π0 MappBZ{2` , Σ2 IZp1qq “ π0 Σ2 IZp1q ‘ π0 MappBZ{2, Σ2 IZp1qq “ Z{2 ‘ Z{2.

This is the group of isomorphism classes of super Hermitian lines. The first Z{2Z is the grading of
the line, the second the “sign” of the form. But the sesquilinearity condition
(6.51)

x`¯1 , `2 y “ p´1q|`1 ||`2 | x`¯2 , `1 y,

`1 , `2 P L,

?
¯ `y P ´1R for all ` P L. (The form is a bilinear map LˆL Ñ C.) The
implies that if L is odd then x`,
?
notion of positivity in this case chooses a ray in ´1R; there is no canonical choice. In the literature,
e.g. [DM, (4.4.2)], an arbitrary choice is made. In our homotopy theoretic presentation, this choice
lies in the identification of the space of super Hermitian lines with the 0-space of Σ2 IZp1q. As we
descend deeper into extended field theories, there are further choices to be made; see Remark 6.26.

7. Reflection structures and stability
We begin in §7.1 by reviewing Madsen-Tillmann spectra; see [GMTW, §3]. They give a filtration (7.6) of Thom spectra, which leads to an analysis of the obstructions to extending invertible
field theories to stable theories. In §7.2 we develop the relation between naive positivity and stability in two situations: non-equivariant discrete theories and equivariant continuous theories. In
each case the only obstruction in n spacetime dimensions arises from the partition function of the
n-sphere. But its positivity does not guarantee positive definite metrics on the state spaces attached
to arbitrary pn ´ 1q-manifolds (Proposition 7.37), consideration of which is deferred until §8. We
conclude in §7.3 by analyzing the obstruction to extending “H-type” theories to “L-type” theories.
7.1. Madsen-Tillmann and Thom spectra
The homomorphism ρn : Hn Ñ On in (2.3), which defines the symmetry type of a theory, produces
a rank n vector bundle Vn Ñ BHn over the classifying space. We refer to §6.1.4 for the general
theory of Thom spectra.
Definition 7.1. The Madsen-Tillmann spectrum M T Hn is the Thom spectrum of ´Vn Ñ BHn .
More natural for us is a suspension, the connective spectrum
(7.2)

Σn M T Hn “ ThompBHn ; Rn ´ Vn q.

<!-- page 56 -->
56

D. S. FREED AND M. J. HOPKINS

The general construction of Thom spectra is described in §6.1.4. Here is a geometric description. Let
Grn pRn`q q denote the Grassmannian of n-dimensional subspaces of Rn`q . It approximates BOn ,
and the pullback

(7.3)

Xn,n`q

/ BHn




/ BOn

Grn pRn`q q

is a finite dimensional approximation to BHn . The q th space of the spectrum (7.2) can be taken to
be the Thom space ThompXn,n`q ; Qq q of the vector bundle Qq Ñ Xn,n`q , which is the pullback of
the rank q “quotient bundle” over the Grassmannian: the fiber at a subspace W Ă Rn`q is W K .
Remark 7.4. The Pontrjagin-Thom construction provides the basic relationship to Hn -manifolds.
If a map S k`q Ñ ThompXn,n`q ; Qq q is transverse to the 0-section of Qq Ñ Xn,n`q , then the inverse
image of the 0-section is a k-manifold M Ă S k`q whose stable tangent bundle is equipped with an
isomorphism to the pullback of the “tautological bundle”26 Vn Ñ Xn,n`q , which is equipped with
an Hn -structure. Theorem 5.12 implies that the abelian group πk Σn M T Hn is generated by closed
k-dimensional Hn -manifolds under disjoint union. The class of a closed manifold M k is zero if and
only if M “ BW where W is a compact pk ` 1q-manifold whose stable tangent bundle is isomorphic
to a rank n bundle with an Hn -structure extending that of M . This bordism group was introduced
by Reinhart [R]; see also [E, Appendix].
Remark 7.5. Not every element of the homotopy group is represented by a manifold; group completion of the semigroup of manifold classes is needed to obtain the homotopy group. For example,
π0 M T O0 – Z but since a 0-dimensional manifold has a unique O0 -structure such manifolds only
realize the submonoid of nonnegative integers. We also remark that the sphere S 2m represents
a nonzero element in π2m Σ2m M T SO2m , but is zero in the next group π2m`1 Σ2m`1 M T SO2m`1 :
the closed ball D2m`1 has nonzero Euler characteristic so no SO2m -structure. As another illustration, the 2-sphere and the genus 2 surface represent opposite elements of π2 Σ2 M T SO2 : a genus 2
handlebody with a 3-ball excised admits an SO2 -structure.
The Stabilization Theorem 2.19 provides a sequence of spectra27
(7.6)

Σn M T Hn ÝÑ Σn`1 M T Hn`1 ÝÑ Σn`2 M T Hn`2 ÝÑ ¨ ¨ ¨

whose colimit, denoted M T H, is the Thom spectrum of the stable vector bundle
(7.7)

´ V ÝÑ BH

which is the negative of the classifying map of (2.28); see the construction in §6.1.4, especially the
presentation (6.11) which is equivalent to (7.6). From the geometric description in Remark 7.4
26The fiber of the tautological bundle at a point W Ă Rn`q in Gr

n pR

n`q

27That theorem supplies a stable tangential structure BH from which BH

q is W .

n is constructed by pullback; recall (2.27).

<!-- page 57 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

57

the homotopy groups πk Σn M T Hn stabilize once n ą k; then πk M T H is the bordism group of
k-dimensional manifolds with a stable tangential H-structure. We identify M T H with the Thom
spectrum M H K of the perpendicular28 stable normal structure. In many cases H K “ H; however,
for example, pPin˘ qK “ Pin¯ .
Following Ansatz 5.14 an invertible topological field theory is a map with domain Σn M T Hn . To
investigate extensions along the sequence (7.6) we will use the following in §7.2.
Proposition 7.12. The fiber of the map Σn M T Hn ÝÑ Σn`1 M T Hn`1 is Σn pBHn`1 q` . The map
Σn pBHn`1 q` Ñ Σn M T Hn is represented by the universal family BHn Ñ BHn`1 of Hn -spheres.
See [GMTW, §3.1], [FHT1, Lemma 3.1] for a proof. The universal family of spheres was mentioned
in Remark 4.32. We remind that spectra are built out of based spaces; for a based space X the
spectrum Σn X` is the one-point union of S n and the suspension spectrum Σn X, and the latter is
pn ´ 1q-connected if X is connected.
Our final task in this section is to refine Ansatz 5.14 and Ansatz 5.26, which formulate invertible
field theories as maps of spectra, to include reflection structures. Recall from §4 that the reflection
structure on the bordism category maps a manifold with Hn -structure to the same manifold with
the opposite Hn -structure, which is defined using the group extension (3.14). Turning to bordism
spectra we observe that this group extension induces a Z{2-action on BHn and makes the vector
bundle Vn Ñ BHn into an equivariant vector bundle Vnβ Ñ BHnβ . Applying the discussion in §6.2.2
we refine the Thom spectrum (7.2) to a Z{2-equivariant spectrum we denote Σn M T Hnβ . There is
an equivariant lift of (7.6). Recall the involutions on IZp1q, ICˆ chosen after Remark 6.33.
Ansatz 7.13.
28 The classifying space BH K is the pullback

BH K

/ BH




/ BO

(7.8)

BO

in which the bottom map classifies the negative of the universal bundle (of rank zero). There is a sequence of
K
K
inclusions ¨ ¨ ¨ HnK ãÑ Hn`1
ãÑ Hn`2
¨ ¨ ¨ of compact Lie groups such that BH K is the colimit of BHnK . Namely, define
K
r
Hn as the pullback (see (2.10))
1

/K

r nK
/H

/ Pin´
n

/1

1

/K


/J


/ t˘1u

/1

(7.9)

and then set
(7.10)

r nK
HnK – H

L

xp´1, k0 qy.

One checks that BHnK is the pullback

(7.11)

BHnK

/ BH




/ BO

BOn

<!-- page 58 -->
58

D. S. FREED AND M. J. HOPKINS

(i) A discrete invertible n-dimensional extended topological field theory with symmetry group Hn
and reflection structure is an equivariant map
(7.14)

1

F : Σn M T Hnβ ÝÑ Σn pICˆ qν0 ,

(ii) A continuous invertible n-dimensional extended topological field theory with symmetry group Hn
and reflection structure is an equivariant map
(7.15)

ϕ : Σn M T Hnβ ÝÑ Σn`1 IZp1qγ .

The space of theories of this type is
(7.16)

In pHn qreflection “ MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q.

7.2. Naive positivity and stability
We first prove that the double of an Hn -manifold is null bordant through an Hn`1 -manifold.
Recall the evaluation bordism (4.7), the identification of duals and bars in Proposition 4.8, and
Definition 4.24 of a double.
Proposition 7.17. Let Y0 , Y1 be closed pn ´ 1q-dimensional Hn -manifolds and X : Y0 Ñ Y1 an
Hn -bordism. Then
(7.18)

βX > eY1 > X : βY0 > Y0 ÝÑ Hn´1

is Hn`1 -bordant to eY0 .
Proof. The bordism29 is r0, 1s ˆ X.



Corollary 7.19. The double ∆X of a compact Hn -manifold with boundary is null bordant through
an Hn`1 -manifold.
By Corollary 4.30 this applies to S n with its canonical Hn -structure, and so every double is Hn`1 bordant to S n .
Proof. Apply Proposition 7.17 to X : Hn´1 Ñ BX (and smooth the corners of r0, 1s ˆ X).



Remark 7.20. If X is the 2-dimensional disk, viewed as a bordism from the empty 1-manifold to the
circle, then ∆X is the 2-dimensional sphere S 2 and the null bordism r0, 1s ˆ X is the 3-dimensional
ball D3 . The Euler characteristic obstructs the existence of an H2 -structure on D3 which restricts
to the given H2 -structure on S 2 (for any stable tangential structure H).
The sequence of bordism spectra (7.6) results in a special type of invertible field theory. The following applies to both discrete (Ansatz 5.14) and continuous (Ansatz 5.26) invertible field theories,
possibly with reflection structure (Ansatz 7.13).
29It is a bordism of manifolds with boundary, or better a higher morphism in a multi-bordism category. We only

use Y0 “ Hn´1 , as in Corollary 7.19, in which case r0, 1s ˆ X is a null bordism of a closed manifold.

<!-- page 59 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

59

Definition 7.21. An n-dimensional invertible topological field theory with domain Σn M T Hn is
stable if it is the restriction of a theory defined on M T H.
Stability can be investigated one step at a time in the sequence (7.6) using obstruction theory. We
first carry this out for discrete invertible topological field theories without reflection structure. Recall that the sphere has a canonical Hn -structure given by the principal bundle Hn`1 Ñ Hn`1 {Hn .
Theorem 7.22. A discrete invertible theory F : Σn M T Hn Ñ Σn ICˆ is stable if and only if
F pS n q “ 1. The subspace of MappΣn M T Hn , Σn ICˆ q consisting of theories F with F pS n q “ 1
is homotopy equivalent to the mapping space MappM T H, Σn ICˆ q.
By Corollary 7.19 the condition is equivalent to F p∆Xq “ 1 for all compact X n with boundary.
Proof. If F is the restriction of Fr : M T H Ñ Σn ICˆ , then F pS n q “ FrpS n q “ 1 since S n is null bordant as an Hn`1 -manifold. Conversely, by Proposition 7.12 the map F extends over Σn`1 M T Hn`1
if and only if it evaluates trivially on the universal family of Hn -spheres. But that evaluation is
the constant function BHn`1 Ñ Cˆ with value F pS n q. There is no further obstruction in the
sequence (7.6), because the subsequent fibers have vanishing homotopy groups in degrees ď n and
πq Σn ICˆ “ 0 for q ą n.
To analyze the space of discrete stable theories we note that the cofibration sequence
(7.23)

Σn M T Hn ÝÑ Σn`1 M T Hn`1 ÝÑ Σn`1 pBHn`1 q`

of spectra induces a fibration sequence
(7.24)

`
˘
Map Σn`1 pBHn`1 q` , Σn ICˆ ÝÑ MappΣn`1 M T Hn`1 , Σn ICˆ q
`
˘
ÝÑ MappΣn M T Hn , Σn ICˆ q ÝÑ Map Σn pBHn`1 q` , Σn ICˆ

of mapping spaces. The first space is contractible, since Σn`1 pBHn`1 q` is n-connected. The fiber of
the last map is the subspace indicated in the theorem, by the obstruction argument in the previous
paragraph. To pass to stable maps make a similar argument with the cofibration sequence
(7.25)

Σn`1 M T Hn`1 ÝÑ M T H ÝÑ C

and the induced fibration on mapping spaces.



Remark 7.26. If X n is a closed Hn -manifold, then r0, 1s ˆ X is a null bordism of βX > X. Thus if
F is stable and has a reflection structure, then }F pXq}2 “ 1.
Next, we turn to continuous invertible field theories with reflection structure, which according
to Ansatz 7.13(ii) are Z{2Z-equivariant maps
(7.27)

ϕ : Σn M T Hnβ ÝÑ Σn`1 IZp1qγ .

We investigate stability for these equivariant theories.

<!-- page 60 -->
60

D. S. FREED AND M. J. HOPKINS

Remark 7.28. As explained after (5.25) a continuous invertible field theory assigns a Zp1q-torsor to
a closed Hn -manifold, hence an equivariant theory (7.27) assigns to a β-equivariant family X Ñ S of
closed Hn -manifolds an equivariant Zp1q-torsor over S, where the action on Zp1q-torsors is that in
Example B.5; see also Remark 6.40. The universal model is the map exp : C Ñ Cˆ , equivariant for
complex conjugation, with fibers Zp1q-torsors. Over the fixed point set Rˆ “ Rą0 > Ră0 the fibers
are Zp1q-torsors of Type P and Type N; see Example B.5. As discussed in §5.4 a non-topological
invertible field theory (type (a) in that discussion) has a homotopy class that is a continuous theory.
If we have a reflection structure, then the partition function of a β-fixed Hn -manifold is real, and
if it is positive then the corresponding Zp1q-torsor has Type P.
Remark 7.29. A stable continuous theory ϕ̃ assigns an integer (better: element of Zp1q) to a closed
pn ` 1q-manifold. The universal property (5.17) of maps into the Anderson dual implies that the
topological field theory associated to ϕ̃ is determined by its truncation to n- and pn ` 1q-manifolds.
Theorem 7.30. An equivariant continuous invertible field theory ϕ : Σn M T Hnβ Ñ Σn`1 IZp1qγ is
stable if and only if ϕpS n q has Type P. The subspace of MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q consisting
of equivariant continuous invertible field theories with Type P partition function on S n is homotopy
equivalent to the mapping space MapZ{2 pM T H β , Σn`1 IZp1qγ q.
Proof. Since S n is diffeomorphic to βS n , the partition function ϕpS n q is a Zp1q-torsor with involution. The partition function of the universal family of n-spheres is then a Zp1q-torsor over BHn`1
with involution covering the trivial involution on the base. It is classified by a map BHn`1 Ñ Rˆ
whose homotopy class in H 0 pBHn`1 ; t˘1uq – t˘1u encodes the Type (P or N) of ϕpS n q.
Now use the stabilization sequence (7.6) as before. If ϕ is stable, then it is trivial on the
fiber Σn pBHn`1 q` of the first map, which is represented by the universal family of n-spheres.
The argument in the preceding paragraph shows that ϕpS n q has Type P. To prove the converse,
if ϕpS n q has Type P then the first obstruction vanishes, and so ϕ is the restriction of a map
β
β
q` Ñ
Ñ Σn`1 IZp1qγ . The obstruction at the next stage is a map Σn`1 pBHn`2
Σn`1 M T Hn`1
β
β
n`1
n`1
n`1
γ
n`1
_Σ
BHn`2 with Z{2 acting trivially on the suspenΣ
IZp1q . But Σ
pBHn`2 q` » S
β
n`1
n`1
sion S
of the basepoint. Since Σ
BHn`2 is pn ` 1q-connected, the obstruction lies in
rS n`1 , Σn`1 IZp1qγ sZ{2 – rS σ´1 , IZp1qsZ{2
(7.31)

– rEZ{2` ^ S σ´1 , IZp1qs
Z{2

– Hompπ0 EZ{2` ^ S σ´1 , Zp1qq “ 0,
Z{2

since
π0 EZ{2` ^ S σ´1 “ π1 RP8 “ Z{2.
Z{2

There are no further obstructions to extending to M T H, because the fibers have nonvanishing
homotopy groups only in degrees greater than n ` 1 and πq Σn`1 IZp1q “ 0 for q ą n ` 1.
The equivariant version of (7.23) with the β-involution leads to the fibration sequence
(7.32)

`
˘
β
β
MapZ{2 Σn`1 pBHn`1
q` , Σn`1 IZp1qγ ÝÑ MapZ{2 pΣn`1 M T Hn`1
, Σn`1 IZp1qγ q
`
˘
β
ÝÑ MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q ÝÑ MapZ{2 Σn pBHn`1
q` , Σn`1 IZp1qγ

<!-- page 61 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

61

As in (7.24) the first space is contractible. The obstruction argument above identifies the fiber of
the last map as equivariant continuous theories with positive sphere partition function. To pass to
stable maps use an equivariant version of (7.25).

Corollary 7.33. There is a 1:1 correspondence

(7.34)

$
,
isomorphism classes of continuous invertible/
’
’
/
’
/
’
/
&n-dimensional extended topological field
.
theories with (i) symmetry group Hn ,
– rM T H β , Σn`1 IZp1qγ sZ{2 .
’
/
’
/
’
/
’
%(ii) reflection structure, and (iii) partition /
n
function on S of Type P

Example 7.35. The restriction map30
(7.36)

rM T SOβ , Σ4 IZp1qγ sZ{2 ÝÑ rΣ3 M T SO3β , Σ4 IZp1qγ sZ{2

is an index two inclusion of infinite cyclic groups. It follows that there exist continuous invertible
3-dimensional oriented theories ϕ with reflection structure such that ϕpS 3 q has Type N. In turn,
this suggests the existence of invertible non-topological theories with reflection structure whose realvalued partition function on S 3 is negative; see 5.4. Here is an explicit example. The domain is the
geometric bordism category of oriented Riemannian manifolds. The partition function is F pX 3 q “
expp2πiξX q, where ξX is the Atiyah-Patodi-Singer invariant [APS].31 To apply the arguments
in Theorem 7.30 we need to use a Riemannian sphere that is a double—the round sphere does
nicely—in which case the spectrum of the APS operator is symmetric about zero and so the ηinvariant vanishes. The dimension of the kernel is one, ξX “ 1{2, and so F pS 3 q “ ´1. We
remark that the corresponding integer invariant of a closed oriented 4-manifold W is pSignpW q ˘
EulerpW qq{2; either sign works. Also, the square of this theory, whose deformation class generates
rM T SOβ , Σ4 IZp1qγ sZ{2 , represents “Kitaev’s E8 -phase” [K5].
Let F be a invertible topological n-dimensional theory, and suppose that F pS n q ą 0. Then the
hermitian form on F pS n´1 q is positive definite; see (4.27). The positivity holds for any null bordant
pn ´ 1q-manifold, but on other manifolds there is no guarantee of positivity (Definition 4.18), even
for stable theories.
Proposition 7.37. Let F be an invertible n-dimensional topological field theory of Hn -manifolds
with F pS n q ą 0. Suppose F has a reflection structure. Then the sign of the hermitian form (4.16)
on a closed pn ´ 1q-manifold is a bordism invariant and determines a homomorphism
πn´1 Σn´1 M T Hn´1 ÝÑ t˘1u.

(7.38)

Proof. If X : Y0 Ñ Y1 is an Hn -bordism, then by reversing the arrow of time on the incoming
boundary we obtain X 1 : Hn´1 Ñ βY0 > Y1 . Hence by Corollary 7.19 and the remark which follows,
we deduce that the hermitian line F pY0 qbF pY1 q is positive definite. Therefore, F pY0 q and F pY1 q are
simultaneously positive or simultaneously negative.

30The involution on π M T SO and π Σ3 M T SO
4

4

negates under orientation-reversal.
31of the operator called ‘B ev ’ in their paper.

3 acts as ´1:

both groups are detected by the signature, which

<!-- page 62 -->
62

D. S. FREED AND M. J. HOPKINS

We conclude this section with a lemma we will use in §8.
Lemma 7.39. The map Σn M T Hn Ñ M T H induces a surjection on Hn`1 p´; Rq.
We remark that πn`1 pBq b R Ñ Hn`1 pB; Rq is an isomorphism for any spectrum B.
Proof. Arrange the stabilization (7.6) and cofibration sequences (7.23) as follows:

(7.40)

Σn pBHn`1 q`

Σn`1 pBHn`2 q`





Σn M T Hn


Σn pBHn q`

i

s

/ Σn`1 M T Hn`1


χ

Σn`1 pBHn`1 q`

j

/ Σn`2 M T Hn`2


Σn`2 pBHn`2 q`

¨

The two compositions with shape ¨ / ¨ are cofibration sequences. The map s˚ on πn`1 sends the gen¨
erator of the infinite cyclic group πn`1 Σn`1 pBHn`2 q` to the class of S n`1 , and the map χ˚ on πn`1
sends the class of a closed pn ` 1q-manifold to its Euler number. Also, πn`1 Σn`2 pBHn`2 q` “ 0.
It follows that j˚ on πn`1 is surjective. If n is even, then χ˚ “ 0 on πn`1 and by exactness i˚ is
surjective. If n is odd, then χ˚ ˝ s˚ is multiplication by 2. Working now on πn`1 b R we can lift
any class in πn`1 Σn`2 M T Hn`2 b R through j˚ to have zero image under χ˚ , hence by exactness
to be in the image of i˚ b R. In other words, pj ˝ iq˚ b R is surjective. Finally, the stabilization
map Σn`2 M T Hn`2 Ñ M T H induces an isomorphism on πn`1 .

7.3. H-type theories
Wen [Wen] and Morrison-Walker [MW] introduced the notion of n-dimensional topological field
theories defined only on n-manifolds with an infinitesimal time direction. These are of Hamiltonian
type, or H-type, and are the minimal expectation for the low energy effective theory describing a
Hamiltonian system. In this paper we assume emergent relativistic invariance, so do not engage
with H-type theories in a serious way. Nonetheless, in this subsection we indicate briefly how to
analyze invertible theories of H-type.
The first issue is definitional: Do the n-manifolds in the bordism category have (i) an oriented
time direction or merely (ii) a time direction? In unoriented theories this means a reduction of On
to either (i) On´1 or (ii) O1 ˆ On´1 . We opt for (i). After all, a Hamiltonian system does have
a definite orientation of time, and even in relativistic quantum field theory we assume a time
orientation of Minkowski spacetime (§2.1). Then a more general symmetry group Hn is reduced
to Hn´1 , and an invertible theory of H-type is a map out of the spectrum Σn´1 M T Hn´1 .
β
Now the extension question: Does an equivariant map ϕ : Σn´1 M T Hn´1
Ñ Σn`1 IZp1qγ extend
β
to an equivariant map Σn M T Hn Ñ Σn`1 IZp1qγ ? (In Wen’s language this is an extension from
H-type to L-type.) The obstruction is the value of ϕ on the universal family of Hn´1 -spheres

<!-- page 63 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

63

S n´1 parametrized by BHn . Without the equivariance the value32 is a Z{2Z-graded complex line
bundle over BHn ; the equivariance implies the value is a Z{2Z-graded real line bundle. (See
Remark 6.40 for the connective cover of Σ2 IZp1q and its bar involution γ.) The first obstruction is
the grading: the single quantum state on S n´1 should be bosonic. If so, the remaining obstruction
is a class in H 1 pBHn ; Z{2Zq – HompHn , Z{2Zq – Hompπ0 Hn , Z{2Zq. For example, if Hn “ On or
n´1 q.
Hn “ Pin˘
n , then a hyperplane reflection should act trivially on the line ϕpS
Example 7.41. Continuing Example 7.35, the restriction map
(7.42)

rΣ3 M T SO3β , Σ4 IZp1qγ sZ{2 ÝÑ rΣ2 M T SO2β , Σ4 IZp1qγ sZ{2

is an index two inclusion of infinite cyclic groups. So there exists a continuous invertible theory ϕ of
H-type with reflection structure that does not extend to all oriented 3-manifolds. Here is an example
defined on the category of oriented Riemannian 2-manifolds: assign the Z{2Z-graded determinant
line ϕpY q of the B̄-operator to a closed 2-manifold Y . Then index B̄S 2 “ 1 implies that ϕpY q is odd.

8. Positivity in extended invertible topological theories
In this section we develop the theory of extended positivity in invertible field theories. We
already introduced a homotopy-theoretic manifestation of extended positivity for higher super lines
in Definition 6.41. Here, in §8.1, we begin by introducing spaces of invertible field theories leading
up to the space of invertible reflection positive theories. Our main result, Theorem 8.20, identifies
the homotopy type of the space of invertible continuous reflection positive theories as the 0-space
of the Anderson dual to a Thom spectrum. The homotopy type of the corresponding space in the
discrete case, worked out in Theorem 8.29, is a corollary, as is Theorem 1.1 in the introduction.
The proof of Theorem 8.20 appears in §8.2 and §8.3.
8.1. Spaces of invertible field theories, extended positivity, and stability
8.1.1. Preliminary: splitting off a reflection. Fix n ą 0. Recall that if pHn , ρn q is a symmetry
pn.
type (Definition 2.4), then we have a canonical coextension (3.14) of Hn by t˘1u to a group H
It is this extension that determines the β-involution on the Madsen-Tillmann spectrum M T Hn , as
pn.
in the discussion preceding Ansatz 7.13; the homotopy quotient of M T Hnβ is M T H
The splitting of interest is contained in (3.31) (and is also implicit in Proposition 4.8). It exists
whenever there is an “auxiliary” direction. The middle vertical homomorphism in (3.31) induces
BHn´1 ˆ BZ{2 Ñ B Ĥn ,
which factors the projection
BHn´1 ˆ BZ{2 Ñ B Ĥn Ñ BZ{2.
32Parallel to the Zp1q-torsors attached to n-manifolds are graded gerbes attached to pn ´ 1q-manifolds.

The
construction of a line may depend on a choice of metric, for example, so may be part of a non-topological theory.

<!-- page 64 -->
64

D. S. FREED AND M. J. HOPKINS

This, in turn, gives a sequence of equivariant maps
(8.1)

Σn´1 M T Hn´1 ^ S 1´σ Ñ Σn M T Hnβ Ñ M T H ^ S 1´σ

factoring the smash product of the identity map of S 1´σ with the defining inclusion of Σn´1 M T Hn´1
into M T H.
The stable form of the splitting implies the following.
Proposition 8.2. The Z{2-equivariant spectra M T H β and M T H γ are canonically equivariantly
weakly equivalent.
We remind that, despite the similarity of notation, the β-involution is defined by the group coextension whereas the γ-involution is natural, obtained by smashing with S 1´σ .
Proof. Take n Ñ 8 in (8.1). The colimit of the first term is M T H ^ S 1´σ and the composition is
homotopic to the identity map.

8.1.2. Spaces of theories. Let n ą 0 be the spacetime dimension and fix a positive integer k ď n.
Let G be a Lie group equipped with a homomorphism ρ : G Ñ Ok . The map ρ is used to form
the Thom spectrum M T G “ ThompBG; ´ρq. Define the space of continuous invertible k-truncated
n-dimensional topological field theories of symmetry type pG, ρq as33
In pGq “ In pG, ρq “ MappΣk M T G, Σn`1 IZp1qq.
Usually ρ is understood in the notation. A point of In pGq may be thought of as a k-dimensional
field theory that associates to a closed `-manifold M , ` ď k, a super pn ´ `q-line.
Different flavors of field theories are obtained by changing the target, as in Definition 6.41 and
Definition 6.45. We give the definitions for continuous invertible theories; there are analogous
definitions for discrete invertible theories.
Definition 8.3. Fix integers n ą 0 and k ď n.
(i) The space of continuous invertible k-truncated n-dimensional Hermitian extended topological
field theories with symmetry type pG, ρq is
In pG, ρqHermitian “ MappΣk M T G, Σn`1 IZp1qH q
(ii) The space of continuous invertible k-truncated n-dimensional positive definite extended topological field theories with symmetry type pG, ρq is
In pG, ρqpositive “ MappΣk M T G, Σn`1 IZp1qpos q.
33The ‘k’ usually appears in the notation for G, as in (8.9) below, so we do not adorn ‘I’ with it.

<!-- page 65 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

65

Note that composition with the map IZp1qpos Ñ IZp1qH induces a map
In pG, ρqpositive ÝÑ In pG, ρqHermitian .

(8.4)

Assume the symmetry type is a pair pHn , ρn q as in Definition 2.4. We recall the notation (7.16)
for the space of theories with reflection structure:
In pHn qreflection “ MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q.

(8.5)

Composition with the first map in (8.1) produces a map
In pHn qreflection ÝÑ In pHn´1 qHermitian .

(8.6)

Therefore, the value of a theory with reflection structure on a closed manifold of dimension ` ď n´1
is a Hermitian super pn ´ `q-line. (The Hermitian line for ` “ n ´ 1 is described in §4.3 for not
necessarily invertible theories.) Recall the stabilization ρ : H Ñ O in (2.28), and define
In pHqstable “ MappM T H, Σn`1 IZp1qq,

(8.7)

the space of stable n-dimensional invertible topological field theories of symmetry type H.
We use the notations Iδn pGqHermitian , Iδn pGqpositive , Iδn pHn qreflection for the corresponding spaces of
n
ˆ
n
ˆ ν01
discrete field theories, which are mapping spaces with codomain Σn ICˆ
H , Σ ICpos , and Σ pIC q ,
respectively. (See (6.42) and (6.46).)
The main objects of interest are invertible reflection positive theories. As stated after (8.6), an
invertible theory with reflection structure has values on closed manifolds of dimension ď pn ´ 1q
that are higher Hermitian super lines. The following definition uses (8.4) to impose positivity,
which in dimension n ´ 1 is a condition (Definition 4.18) and in dimensions ă pn ´ 1q is a structure.
Definition 8.8. Fix n ą 0 and a symmetry type pHn , ρn q in the sense of Definition 2.4. Define
the spaces In pHn qreflection and Iδn pHn qreflection of n-dimensional continuous (resp. discrete) invertible
positive

positive

reflection positive topological field theories with symmetry type pHn , ρn q and maps out of these spaces
so that each square in the diagram
Iδn pHn qreflection
positive

(8.9)


Iδn pHn qreflection

/ In pHn qreflection
positive

/ In pHn´1 qpositive



(8.6)
/ In pHn qreflection
/ In pHn´1 qHermitian

is a homotopy pullback.
For the spaces of theories in the right hand column we use Definition 8.3 with k “ n ´ 1, G “ Hn´1 ,
and ρ “ ρn´1 . Our task is to determine the homotopy types of In pHn qreflection and Iδn pHn qreflection .
positive

positive

<!-- page 66 -->
66

D. S. FREED AND M. J. HOPKINS

8.1.3. Extended positivity structure. Definition 8.8 is natural given our homotopy-theoretic implementation of higher positive definite Hermitian super lines in Definition 6.45. We now make a short
digression to identify extended positivity in an invertible n-dimensional field theory as a structure
that trivializes an associated invertible pn ´ 1q-dimensional field theory. For this we need yet an
additional space of invertible field theories, based on the target spectrum of higher real super lines
(Definition 6.41(ii)).
Definition 8.10. The space of continuous invertible pn ´ 1q-dimensional real extended topological
field theories with symmetry type pHn´1 , ρn´1 q is
(8.11)

` n´1
˘
IR
M T Hn´1 , pΣn IZp1qγ qhZ{2 .
n´1 pHn´1 q “ Map Σ

The partition function on a closed pn´1q-manifold lies in t˘1u, the value on a closed pn´2q-manifold
`
˘hZ{2
.)
is a real super line, etc. (See Remark 6.40 for the top few homotopy groups of IZp1qγ
0
To begin, for any pointed space X there is an equivalence of spectra X` « X _ S , which leads
to a cofibration sequence
X ÝÑ X` ÝÑ S 0 .

(8.12)

`
˘
Set X “ BZ{2, smash with Σn´1 M T Hn´1 , and apply Map ´, Σn`1 IZp1q to obtain the fibration
sequence
(8.13)

In pHn´1 qpositive ÝÑ In pHn´1 qHermitian ÝÑ IR
n´1 pHn´1 q.

For the middle term use (6.43) and for the last the identification
MappΣn´1 M T Hn´1 ^ BZ{2, Σn`1 IZp1qq « MapZ{2 pΣn M T Hn´1 ^ S σ´1 , Σn`1 IZp1qq
« MapZ{2 pΣn M T Hn´1 , Σn`1 IZp1qγ q
« MapZ{2 pΣn´1 M T Hn´1 , Σn IZp1qγ q
« MappΣn´1 M T Hn´1 , Σn pIZp1qγ qhZ{2 q.
Therefore, the space In pHn qreflection may also be defined as the homotopy fiber of the composition
positive

(8.14)

κ : In pHn qreflection ÝÑ In pHn´1 qHermitian ÝÑ IR
n´1 pHn´1 q.

This leads to the following definition.
Definition 8.15. An (extended ) positivity structure on a continuous n-dimensional field theory
ϕ P In pHn qreflection is a trivialization of κpϕq.
That is, a positivity structure is a path from κpϕq to the basepoint in IR
n´1 pHn´1 q. This discussion identifies the space of continuous reflection positive invertible field theories as the space of
continuous invertible field theories with both a reflection structure and a positivity structure.

<!-- page 67 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

67

Remark 8.16. The partition function of the field theory κpϕq : Σn´1 M T Hn´1 Ñ Σn pIZp1qγ qhZ{2 is
the homomorphism
πn´1 Σn´1 M T Hn´1 ÝÑ t˘1u

(8.17)

induced on πn´1 , and it agrees with the homomorphism (7.38) which tracks the sign of the hermitian
lines in the theory ϕ. The highest piece of the positivity structure is therefore the standard positivity
constraint in Definition 4.18. The theory κpϕq assigns a real super line to a closed pn ´ 2q-manifold
and more complicated objects in lower dimensions; their trivializations are data.
8.1.4. Main theorems. We apply the splitting of §8.1.1 to construct a map
In pHqstable ÝÑ In pHn qreflection

(8.18)

positive

as follows. (These spaces of invertible field theories are defined in (8.7) and (8.9).) Map
(8.19)

Σn´1 M T Hn´1 ^ BZ{2` ÝÑ Σn´1 M T Hn´1 ÝÑ M T H

into Σn`1 IZp1q to obtain a map of In pHqstable into the upper right corner of (8.9). Use equivariant
maps of the sequence (8.1) into Σn`1 IZp1qγ to map In pHqstable into the middle of the bottom row
of (8.9) . The two compositions into the lower right corner are canonically homotopic, so the fact
that the right square in (8.9) is a homotopy pullback yields (8.18).
Theorem 8.20. The map In pHqstable ÝÑ In pHn qreflection in (8.18) is a homotopy equivalence.
positive

We give the proof of Theorem 8.20 in §8.2 and §8.3.
Corollary 8.21. There is an isomorphism
(8.22)

π0 In pHn qreflection – rM T H, Σn`1 IZp1qs.
positive

Next, we turn to discrete invertible theories. First, observe that the Z{2-action on C by complex
conjugation is equivalent to the Z{2-action on MappZ{2, Rq, so for any Z{2-spectrum X one has
1

MapZ{2 pX, HCν0 q « MappX, HRq.

(8.23)

The spectrum MappX, HRq carries a residual Z{2-action, induced from the Z{2-action on X; it
splits as a wedge of the p`1q- and p´1q-eigenspaces. The exponential sequence (6.35) of Z{2equivariant spectra implies that the left map in the bottom row of (8.9) extends to a fibration
sequence
1

(8.24)

MapZ{2 pΣn M T Hnβ , Σn pICˆ qν0 q ÝÑ MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q
1

ÝÑ MapZ{2 pΣn M T Hnβ , Σn`1 HCν0 q.

Apply (8.23) to the last term and use the fact that the left hand square in (8.9) is a homotopy
pullback to obtain a fibration sequence
(8.25)

Iδn pHn qreflection ÝÑ In pHn qreflection ÝÑ MappΣn M T Hn , Σn`1 HRq.
positive

positive

<!-- page 68 -->
68

D. S. FREED AND M. J. HOPKINS

Proposition 8.26. The image of the homomorphism
(8.27)

π0 Iδn pHn qreflection ÝÑ π0 In pHn qreflection
positive

positive

is the torsion subgroup of π0 In pHn qreflection .
positive

Theorem 1.1 in the introduction follows from Proposition 8.26 and (8.22). In Theorem 8.29 below
we determine the homotopy type of the space of discrete invertible reflection positive field theories.
Proof. Since (8.25) is a fibration sequence of spectra, applying π0 we obtain an exact sequence of
abelian groups in which, after applying (8.22), the second map is34
(8.28)

rM T H, Σn`1 IZp1qs ÝÑ rΣn M T Hn , Σn`1 HRp1qs.

The construction following (8.19) implies that this map is pullback along the defining inclusion of
Σn M T Hn into M T H. The proposition follows if we prove (8.28) is injective after tensoring the
domain with R. This follows immediately from Lemma 7.39.

We parlay (8.25) into a more useful expression for the homotopy type of the space of discrete
invertible reflection positive field theories. Recall the spectrum IT introduced in Remark 6.36.
Theorem 8.29. For n odd there is a homotopy equivalence
(8.30)

«

MappM T H, Σn ITq ÝÝÑ Iδn pHn qreflection
positive

For n even there is a fibration sequence
(8.31)

s

MappM T H, Σn ITq ÝÑ Iδn pHn qreflection ÝÝÑ Rą0
positive

in which Rą0 has the discrete topology and s maps a discrete theory F to F pS n q.
Compare with the more rigid Theorem 7.22 in the absence of reflection structures. Also, note
that for any n-manifold X the disjoint union βX > X is null bordant, and so in a stable theory
the partition functions have unit norm, consistent with the appearance of IT in (8.30) and (8.31).
There is a canonical section of s given by Euler theories (Example 4.21): given x P Rą0 define the
Euler theory as the composition
(8.32)

?
x

1

Σn M T Hnβ ÝÑ Σn pBHnβ q` ÝÑ Σn S 0 ÝÝÝÑ Σn HRą0 ÝÑ Σn pICˆ qν0

β
The restriction to Σn´1 M T Hn´1
is trivialized; using (8.9) we obtain a reflection positive theory.
34 The map (8.28) is Z{2-equivariant for the β-involution on M T H and Σn M T H

n . By Proposition 8.2 the β- and
γ-involutions on M T H agree, from which Z{2-acts as ´1 on the domain. It follows that the image is contained in
the p´1q-eigenspace of the codomain, which is why we write ‘HRp1q’ in place of ‘HR’.

<!-- page 69 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

69

Proof. For any pointed space Cn use the nonequivariant version of the exponential sequence (6.39)
and the fibration sequence (8.25) to construct the diagram

(8.33)

MappM T H, Σn ITq

/ MappM T H, Σn`1 IZp1qq

/ MappM T H, Σn`1 HRp1qq




/ In pHn qreflection


/ MappΣn M T Hn , Σn`1 HRq


/˚


/ Cn

Iδn pHn qreflection
positive

positive



ΩCn

in which the rows are fibration sequences, as is the middle column, by Theorem 8.20. We claim
#
˚,
n odd,
(8.34)
Cn “
KpR, 1q, n even,
renders the last column a fibration sequence; it follows that the first column is as well. (Here
KpR, 1q is an Eilenberg-MacLane space.) There is an exponential to pass from the third column to
the first column in (8.33), and so naturally ΩCn « Rą0 with the discrete topology.
To prove the claim observe first that we can replace the upper right entry of (8.33) with the
homotopy equivalent space MappΣn`2 M T Hn`2 , Σn`1 HRp1qq, using arguments similar to those
in §7.2. To analyze the resulting right vertical map consider the composition
(8.35)

j˚

i˚

πq Σn M T Hn b R ÝÝÝÑ πq Σn`1 M T Hn`1 b R ÝÝÝÑ πq Σn`2 M T Hn`2 b R.

The composition j˚ ˝ i˚ is an isomorphism for q ă n, and since we map to Σn`1 HR only q ď n ` 1
is relevant. Use (7.40) and the exact sequence
(8.36)

Euler

rS m s

πm`1 Σm`1 M T Hm`1 ÝÝÝÝÝÑ Z ÝÝÝÝÑ πm Σm M T Hm ÝÑ πm Σm`1 M T Hm`1 ÝÑ 0

to verify the following four assertions. If n is odd, then j˚ ˝ i˚ is an isomorphism for q “ n
and q “ n ` 1. If n is even, then j˚ ˝ i˚ is an isomorphism for q “ n ` 1 and is surjective for q “ n
p n`1 {H
p n s is fixed by the β-involution. It
with kernel generated by rS n s. Observe that rS n s “ rH
follows that the upper right arrow in (8.33) is injective with image the p´1q-eigenspace of the βinvolution; the cokernel the p`1q-eigenspace generated by rS n s. (Compare with the discussion in
footnote 34 .) The claim, and so the theorem, follows.

We conclude this subsection with a comment about our application of these theorems to computations. Namely, the considerations in §5.4 lead to the following conjecture, which uses non-topological
invertible theories (for which we do not develop mathematical foundations in this paper).
Conjecture 8.37. There is a 1:1 correspondence
$
,
&deformation classes of reflection positive .
invertible n-dimensional extended field
(8.38)
– rM T H, Σn`1 IZp1qs.
%
theories with symmetry type pHn , ρn q

<!-- page 70 -->
70

D. S. FREED AND M. J. HOPKINS

We remark that since the rational cohomology of BH vanishes in odd degrees, elements of infinite
order in (8.38) occur only for n odd.
Remark 8.39. A restatement of Corollary 8.21 is the 1:1 correspondence
$
,
&isomorphism classes of reflection positive continuous.
invertible n-dimensional extended topological
(8.40)
– rM T H, Σn`1 IZp1qs.
%
field theories with symmetry type pHn , ρn q
If we accept that the effective low energy theory of an invertible gapped system is a continuous
invertible topological field theory, as in Remark 5.29, then we can apply (8.40) to the computations
in §9 rather than (8.38). This has an advantage: (8.40) is a theorem in the context of this paper.
Remark 8.41. A homotopy class of maps M T H Ñ Σn`1 IZp1q leads to a canonical isomorphism
class of invertible field theories via the following sketch; the theories are topological if and only
if the homotopy class has finite order. By the twisted Thom isomorphism the homotopy classes
are elements of IZp1qτ `n`1 pBHq, where τ is the canonical “density twisting”: the pullback to
manifolds with tangential H-structure can be integrated. According to the main theorem in [FH1]
{ τ `n`1 pB Hq. Choose a “cocycle”
there is a unique lift to the differential cohomology group IZp1q
∇

representative. Then on any manifold with a differential H-structure we can integrate to construct
an invariant, and these invariants fit to an invertible field theory on Bord∇
n pHq.
8.2. Proof of Theorem 8.20
We restate the theorem in the language of stable homotopy theory.
Proposition 8.42. The square
MappM T H, Σn`1 IZp1qq
(8.43)


MapZ{2 pΣn M T Hnβ , Σn`1 IZp1qγ q

/ MappΣn´1 M T Hn´1 , Σn`1 IZp1qq

/ MapZ{2 pΣn´1 M T H γ

n´1 , Σ

n`1 IZp1qγ q

is a homotopy pullback square of spaces.
The analysis of this square becomes cleaner if every term of the form MapZ{2 pX, Σn`1 IZp1qγ q is
replaced with MapppX ^ S σ´1 qhZ{2 , Σn`1 IZp1qq. Doing so, Proposition 8.42 becomes the assertion
that the square

(8.44)

Σn´1 M T Hn´1 ^ BZ{2`

/ Σn M T Ĥnpσ´1q




/ MTH

Σn´1 M T Hn´1

becomes a homotopy pullback square after applying Mapp ´ , Σn`1 IZp1qq. We use the notation
(8.45)

p pσ´1q “ ThompB H
p n ; ´ρ̂n ` σ ´ 1q.
MTH
n

To clarify the argument we state this as as

<!-- page 71 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

71

Proposition 8.46. For any m ě n, the square
Σm´1 M T Hm´1 ^ BZ{2`

pσ´1q
/ Σm M T Ĥm




/ MTH

(8.47)

Σm´1 M T Hm´1

becomes a homotopy pullback square after applying Mapp ´ , Σn`1 IZp1qq.
The proof of Proposition 8.46 will make repeated use of the following result, which follows from
the universal property (5.17) of IZp1q.
Lemma 8.48. Suppose A is a spectrum having the property that πi A “ 0 for i ď n and πn`1 A is
a torsion group. If A Ñ X Ñ Y is a cofibration sequence then
MappY, Σn`1 IZp1qq Ñ MappX, Σn`1 IZp1qq
is a weak equivalence of spaces.
The proof of Proposition 8.46 is by decreasing induction on m. As m Ñ 8 the square (8.47)
becomes
/ M T H ^ BZ{2`
M T H ^ BZ{2`


MTH


/ MTH

which is obviously a pushout. On the other hand for m ą pn ` 2q the maps
Σm´1 M T Hm´1 Ñ M T H
pσ´1q
Σm M T Ĥm
Ñ M T H ^ BZ{2`

become equivalences after applying Mapp ´ , Σn`1 IZp1qq, so the result is true for all m ą n ` 2.
(Compare with the proof of Theorem 7.30.)
Since the homotopy fiber of the left vertical map in (8.47) is Σm´1 M T Hm´1 ^ BZ{2, Proposition 8.46 is equivalent to the assertion that for all m ě n, the sequence
pσ´1q
Σm´1 M T Hm´1 ^ BZ{2 Ñ Σm M T Ĥm
Ñ MTH

becomes a fibration sequence after applying Mapp ´ , Σn`1 IZp1qq. The induction step therefore
follows from
Proposition 8.49. For m ě n, the square
Σm´1 M T Hm´1 ^ BZ{2

pσ´1q
/ Σm M T Ĥm




/ Σm`1 M T Ĥ pσ´1q

(8.50)
Σm M T Hm ^ BZ{2

m`1

becomes a homotopy pullback square after applying Mapp ´ , Σn`1 IZp1qq.

<!-- page 72 -->
72

D. S. FREED AND M. J. HOPKINS

What is at stake in Proposition 8.49 is to prove that the induced map
(8.51)

Σm´1 pBHm q` ^ BZ{2 Ñ Σm ThompB Ĥm`1 ; σ ´ 1q

of homotopy fibers of the vertical maps in (8.50) becomes a homotopy equivalence after applying
Mapp´, Σn`1 IZp1qq. The following result will be proved in §8.3.
Lemma 8.52. The map (8.51) is the pm ´ 1qst suspension of the map of Thom spectra (of the
bundle pσ ´ 1q) associated to the map
(8.53)

BHm ˆ BZ{2 Ñ B Ĥm`1

given by the choice of reflection in the last coordinate.
Assuming Lemma 8.52 we can prove Proposition 8.49.
Proof of Proposition 8.49. It suffices to show that the induced map (8.51) becomes a weak equivalence after applying Mapp ´ , Σn`1 IZp1qq. The map (8.53) fits into a Cartesian square
Sm

Sm




/ BHm ˆ BZ{2

/ BZ{2




/ B Ĥm`1

/ BZ{2 ,

BHm

BHm`1

so Lemma 8.52 implies that the cofiber of (8.51) is 2m-connected. Since m ě n ě 1, one has
2m ě n and so the cofiber is n-connected. Both terms in (8.51) are rationally acyclic. The result
then follows from Lemma 8.48.

8.3. Transfers
Suppose that M Ñ X is a fiber bundle with fibers closed smooth manifolds Mx of dimension n.
Let TM {X be the vector bundle over M whose fiber at a P Mx is the tangent space Ta Mx . There is
functorial stable map
Σ8 X` Ñ ThompM, ´TM {X q
called the transfer map. When there is an embedding M Ă X ˆRn for some n it can be constructed
from the Pontrjagin Thom collapse
ThompX, Rn q Ñ ThompM, Rn ´ TM {X q

<!-- page 73 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

73

by passing to suspension spectra and desuspending n times. The transfer map is constructed in
the general case by passing to the colimit over the category of pairs
Xα Ñ X
iα : Mα ãÑ Xα ˆ RNα
in which Mα Ñ Xα is the pullback of M Ñ X along the map Xα Ñ X.
When there is an embedding M Ă W over B, the Pontrjagin Thom construction leads to a
twisted transfer map
ThompB; W q Ñ ThompX; W ´ TM {X q.
The twisted transfer extends in the evident manner to the case of virtual bundles W .
Proposition 8.54. Suppose that W is a vector bundle over X, that f : M Ñ W is a map over X
transverse to the zero section and let N be the inverse image of 0. There is a commutative diagram
ThompX; 0q

/ ThompN ; ´TN {X q




/ ThompM ; W ´ TM {X q

ThompX; W q

in which the left vertical map is derived from the zero section, and the right is the natural map of
Thom complexes coming from the inclusion N Ă M and the isomorphism
TM {X « TN {X ‘ W.
Proof. It suffices to establish the case in which there is an embedding
ι : M ãÑ Rn .
Applying the Pontrjagin-Thom constructions to the rows in the transverse pullback square
N

/ X ˆ Rn




/ W ˆ Rn .

M

pf,ιq

gives a diagram
ThompX; Rn q

/ ThompN ; Rn ´ TN {X q




/ ThompM ; W ` Rn ´ TM {X q

ThompX; W ‘ Rn q

in which the left vertical map is the inclusion of the zero section. Desuspending, the claim follows
easily from this.


<!-- page 74 -->
74

D. S. FREED AND M. J. HOPKINS

Proof of Lemma 8.52. The idea is to apply Proposition 8.54 to the left triangle in the diagram
/ Spρm ‘ σq

Spρm q ˆ BZ{2
(8.55)

(



BHm ˆ BZ{2

/ Spρ̂m`1 q

/ B Ĥm`1

with
X “ BHm ˆ BZ{2
W “σ
M “ Spρm ‘ σq
N “ Spρm q ˆ BZ{2
The diagram is written in order to clarify the relationship with manifolds. Note that there are
equivalences
Spρ̂m`1 q « B Ĥm
Spρm q « BHm´1 .
Also, for a vector bundle V Ñ X the relative tangent bundle of p : SpV q Ñ X is given by
TSpV q{X ‘ R “ p˚ V . Proposition 8.54 then gives the left square in the diagram

(8.56)

Σm´1 pBHm q` ^ BZ{2`

/ Σm´1 pBHm q` ^ BZ{2





Σm´1 M T Hm´1 ^ BZ{2`

/ Σm ThompB Ĥm`1 ; σ ´ 1q

/Y



pσ´1q
/ Σm M T Ĥm

with
Y “ Σm ThompSpρm ‘ σq; 1 ´ ρm ´ σ ´ 1 ` σq;
the right square in (8.56) is the pullback of transfer maps induced from the pullback square in (8.55).
The map (8.51) is the composition of
(8.57)

Σm´1 pBHm q` ^ BZ{2 Ñ Σm´1 pBHm q` ^ BZ{2`

with the top row of (8.56). Lemma 8.52 now follows from the fact that the composition of (8.57)
with the left map in the top row of (8.56) is the identity.


<!-- page 75 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

75

9. Fermionic theories with scalar internal symmetry group
In this section we apply Theorem 1.1 to some basic symmetry groups, namely those whose
subgroup K of internal symmetries is the group O1 , U1 , Sp1 of unit norm elements in the normed
division algebras R, C, H, respectively. (We use the names t˘1u, T, SU2 for these three groups.) The
internal symmetry group K “ T is the basic charge symmetry of electromagnetism; in quantum mechanical models the presence of a so-called particle-hole symmetry “breaks”35 it to either K “ t˘1u
or K “ SU2 . In §9.1 we classify the possible symmetry groups Hn with these internal symmetries, and restricting to fermionic symmetry groups we recover the 10-fold way; see Tables (9.24)
and (9.25). (Wang-Senthil [WS] list many of these groups—in a nonrelativistic form (9.34), (9.35)—
and the corresponding “Cartan label”. Metlitski [M] introduces the group Pinc̃` , which provided
guidance for our treatment here. This twisted form of Pinc also appears implicitly in [SeWi, §A.4].)
Lemma 9.27 relates the relativistic 10-fold way to the 10 real and complex Clifford algebras, thus
providing a link to other 10-fold ways.
In §9.2 we sketch two ways in which a theory of free fermions in Minkowski spacetime gives
rise to a deformation class of reflection positive invertible field theories, or to a reflection positive
continuous invertible topological field theory. If one begins with an pn´1q-dimensional free fermion
theory, then there is an associated n-dimensional invertible anomaly theory; if the original free
fermion theory admits a mass term, then the anomaly is trivializable. In this paper we do not
attempt a complete treatment, so state the main result as a conjecture, Conjecture 9.70. It expresses
the deformation class of the anomaly theory as a composition of a twisted Atiyah-Bott-Shapiro map
and a Pfaffian map on real K-theory. This K-theory interpretation depends on Lemma 9.55, which
expresses the existence of a mass in terms of Clifford algebras.
The second scenario is to begin with a massive free fermion theory in n dimensions, as we
sketch in §9.2.6. The low energy effective field theory is invertible, and (9.71) is a formula for its
deformation class. It is this scenario about gapped theories that is relevant to this paper.
We carry out computations in low dimensions in §9.3. For each of the 10 electron symmetry
groups we list the groups of deformation classes of reflection positive invertible topological theories
and compute the map from free fermions to it. There is no further physical reasoning; we compute
directly from the results in Theorem 1.1 and (9.71). The techniques lie in stable homotopy theory,
and in the next section we give some details to illustrate how the computations are made. As
discussed in §1 these classification results apply to invertible topological phases of condensed matter
systems, often called SPT phases. The fermionic symmetry groups with K “ T pertain to topological
insulators; those with K “ t˘1u and K “ SU2 pertain to topological superconductors.
Remark 9.1. Most of the interacting groups we compute are torsion so are covered by Theorem 1.1.
In the general case we interpret the computations as theorems by using (8.40), in which the interacting group is a group of isomorphism classes of reflection positive continuous invertible topological
field theories. See §5.4 for a discussion of expectations for low energy effective field theories.
In the theoretical discussions we assume n ě 3; in the computations we apply the results to all n.
35We do not have any fundamental understanding of this mechanism, especially the appearance of SU .
2

we simply offer it as a storyline in relativistic theory that matches the condensed matter literature.

In §9.1

<!-- page 76 -->
76

D. S. FREED AND M. J. HOPKINS

9.1. Symmetry groups of fermionic systems
We already classified symmetry groups Hn with K “ t˘1u in Proposition 2.16. The fermionic
groups are the ones for which ´1 P K is the distinguished element k0 of Theorem 2.7 and Corollary 2.12.36 (The other possibility is k0 “ 1, in which case the symmetry group is bosonic.) Those
´
fermionic groups are Spinn , Pin`
n , and Pinn .
Next, we classify symmetry groups with K “ T. These are group extensions
(9.2)

1 ÝÑ T ÝÑ SHn ÝÑ SOn ÝÑ 1

if there is no time-reversal symmetry and
(9.3)

1 ÝÑ T ÝÑ Hn ÝÑ On ÝÑ 1

if there is time-reversal symmetry. Recall the group En introduced before Proposition 2.16.
Proposition 9.4 (K “ T). Up to isomorphism there are two distinct group extensions (9.2)
with n ě 3, and the groups SHn that appear are SOn ˆ T and Spincn . Up to isomorphism there
are six distinct group extensions (9.3) with n ě 3, and the groups Hn that appear are mutually
nonisomorphic. Three of the groups have identity component SOn ˆ T:
(9.5)

On ˆ T

(9.6)

On ˙ T

(9.7)

En ˙ T

L

t˘1u

The identity component of the remaining three groups is Spincn :
(9.8)

Pincn “ Pin`
n ˆT

(9.9)

`
Pinc̃`
n “ Pinn ˙T t˘1u
L
´
Pinc̃´
n “ Pinn ˙T t˘1u

(9.10)

L

t˘1u

L

L
The group Pincn is also isomorphic to Pin´
t˘1u. It sits in the complex Clifford algebra
n ˆT
˘
n
generated by R with a nondegenerate symmetric bilinear form [ABS]. In Pinc̃˘
n the action of Pinn
´1
on T factors through π0 Pin˘
n and is via inversion λ ÞÑ λ . In each case we divide out by the
diagonal subgroup t˘1u. The groups with identity component Spincn are fermionic.
Proof. The extension (9.2) is central, so up to isomorphism classified by the cohomology group
(9.11)

H 2 pBSOn ; Tq – H 3 pBSOn ; Zq – Z{2Z.

The underline indicates the sheaf cohomology of continuous functions into T with the standard
topology. It is well-known that Spincn corresponds to the nonzero element.
36This implies the “spin/charge relation” of condensed matter physics, which is emphasized in [SeWi]:

have even charge and fermions have odd charge.

bosons

<!-- page 77 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

77

The only nontrivial automorphism of T is inversion, so in the extension (9.3) either On acts
trivially or it acts through its components with elements of determinant ´1 acting by inversion. In
each case the group extensions are classified by a cohomology group of the classifying space BOn :
(9.12)

H 2 pBOn ; Tq – H 3 pBOn ; Zq – Z{2Z

(9.13)

r – H 3 pBOn ; Zq
r – Z{2Z ˆ Z{2Z
H 2 pBOn ; Tq

The tilde indicates coefficients twisted by inversion. The product (9.5) and semi-direct product (9.6)
account for (9.12) and the remaining four groups for (9.10), as can be seen from cohomological
computations we omit.

According to the arguments in Appendix A, the anti-Wick rotation of Pinc̃` contains a timereversal symmetry T with T 2 “ p´1qF and the anti-Wick rotation of Pinc̃´ contains a timereversal symmetry T with T 2 “ 1. More precisely, the groups (9.8) and (9.5) are Wick rotations of
relativistic symmetry groups that include CT symmetry; the remaining groups are Wick rotations
of relativistic symmetry groups that include T symmetry.37
Finally, we classify symmetry groups with K “ SU2 . Now we have possible extensions
(9.14)

1 ÝÑ SU2 ÝÑ SHn ÝÑ SOn ÝÑ 1

and
(9.15)

1 ÝÑ SU2 ÝÑ Hn ÝÑ On ÝÑ 1

Proposition 9.16 (K “ SU2 ). Up to isomorphism there are two distinct group extensions (9.14)
with n ě 3, and the groups SHn that appear are SOn ˆ SU2 and
(9.17)

G0 “ Spinn ˆt˘1u SU2 .

Up to isomorphism there are four distinct group extensions (9.15) with n ě 3, and the groups Hn
that appear are mutually nonisomorphic. Two of the groups have identity component SOn ˆ SU2 :
(9.18)

On ˆ SU2

(9.19)

En ˆt˘1u SU2

The identity component of the remaining two groups is G0 :
(9.20)

`
G`
n “ Pinn ˆt˘1u SU2

(9.21)

´
G´
n “ Pinn ˆt˘1u SU2

37This is our interpretation of [W1, §3.7].

There are more general possibilities with larger internal symmetry
group K. This occurs in [SeWi, §3], for example, in a theory with both T and CT symmetry.

<!-- page 78 -->
78

D. S. FREED AND M. J. HOPKINS

The symmetry groups with identity component G0 are fermionic.
Proof. The classification of the identity component SHn follows from Theorem 2.7(2): there are
two central elements k0 P SU2 with k02 “ 1. To classify the two-component group Hn we apply a
useful general result [FHT2, Corollary 7.3]. Namely, for any compact Lie group H, let H 0 denote
the component of the identity element, Z 0 Ă H 0 its center, and π “ π0 H the abelian group of
components. Then there exists a group L that fits into the diagram

1

/ Z0

/L

/π

/1

1


/ H0


/H

/π

/1

(9.22)

of group extensions. Furthermore, the group L acts on H 0 by conjugation—the action descends
to an action of π since Z 0 is central, but it depends on the choice of L—and the group H is
reconstructed from H 0 and L as a semidirect product

(9.23)

H – L ˙Z 0 H 0 “ L ˙ H 0

L

Z 0.

By the Stabilization Theorem 2.19 we may assume that n is odd, since for n even Hn is obtained
by pullback, so the center of SOn is trivial and the center of Spinn is t˘1u. First, assume H 0 “
SHn “ SOn ˆ SU2 , so that Z 0 “ t˘1u. There are two possibilities: L – t˘1uˆ2 or L – µ4 . We
can take the image of L in On to be the central subgroup t˘1u. The conjugation action on SOn is
trivial, and as all automorphisms of SU2 are inner we can take the entire action on H 0 to be trivial.
Then (9.23) (with a direct product in place of a semidirect product) yields the two groups (9.18)

and (9.19). The argument for H 0 “ Spinn ˆt˘1u SU2 is similar; again Z 0 – t˘1u.

9.2. Free fermions and twisted Dirac operators
In this section we take up the homotopy theory of relativistic free fermions. We treat the
10 fermionic symmetry groups simultaneously via embeddings into Clifford algebras (§9.2.1). For
each we define a twisted Atiyah-Bott-Shapiro map (§9.2.2) that encodes the index of twisted Dirac
operators (§9.2.3) on compact Riemannian manifolds. The relativistic story begins on Minkowski
spacetime in Lorentz signature, where a free fermion theory is specified by a real Clifford module for
a Lorentz signature Clifford algebra (§9.2.4). We develop that algebraic theory for the fermionic
symmetry groups, and in particular determine those theories that admit a nondegenerate mass
term (Lemma 9.55). A massless theory has an anomaly, which is an invertible field theory, and we
conjecture its deformation class in §9.2.5. A formally similar setup (§9.2.6) attaches an invertible
field theory to a massive free fermion theory, and we conjecture that its deformation class is given
by the same formula. It is this formula that we use in the computations in §9.3.

<!-- page 79 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

79

9.2.1. A relativistic 10-fold way. Proposition 2.16, Proposition 9.4, and Proposition 9.16 combine
to yield 3 ` 4 ` 3 “ 10 fermionic symmetry groups, which we arrange into two tables:

(9.24)

(9.25)

s

Hc

K

Cartan

D

0
1

Spinc
Pinc

T
T

A
AIII

C
Cliff C
´1

s

H

K

Cartan

D

0
´1
´2

Spin
Pin`
Pin` ˙t˘1u T

t˘1u
t˘1u
T

D
DIII
AII

R
Cliff ´1
Cliff ´2

´3

Pin´ ˆt˘1u SU2

SU2

CII

Cliff ´3

4

Spin ˆt˘1u SU2

SU2

C

H

`

3

Pin ˆt˘1u SU2

SU2

CI

Cliff `3

2
1

Pin´ ˙t˘1u T
Pin´

T
t˘1u

AI
BDI

Cliff `2
Cliff `1

In addition to the fermionic symmetry group H or H c and its internal group K, we list the
Cartan label, an integer s called the “type”, and a super division algebra D. The type is defined
mod 2 in (9.24) and mod 8 in (9.25); we choose a convenient integer representative. We use
notations Hpsq, H c psq, Kpsq, Dpsq when we make the type explicit. The Cartan label is used in
the condensed matter literature, where this 10-fold way has many incarnations: see [D, AZ, HHZ,
K6, SRFL, FM1, KZ, WS]. In those references the particle-hole symmetry determines the internal
symmetry group K: in its absence K “ T; if particle-hole symmetry is present and squares to `1,
then K “ t˘1u; and if particle-hole symmetry is present and squares to ´1, then K “ SU2 .
The existence (and square) of time-reversal symmetry in the references above matches that in our
account except for the entry AIII, which is usually listed as not having time-reversal symmetry
(but see [WS, §III]). The super division algebra D is the unique super division algebra in the
Morita class of the Clifford algebra38 Cliff s . The groups Spinc and Pinc in the first table (9.24) are
distinguished as having a central subgroup isomorphic to T, so are called complex ; the center of
the groups in (9.25) is t˘1u, and so they are called real.
Remark 9.26. We would have found it more natural from a mathematical point of view in several
places to define Hp4q “ Spin ˆt˘1u Spin4 rather than Spin ˆt˘1u Spin3 , but we lack a physics
motivation to do so.
The following embedding allows a uniform treatment of these symmetry groups, and it opens a
path to relating this relativistic 10-fold way to other 10-fold ways in the literature. Fix n ě 0.
38The Clifford algebra Cliff

˘|s| is generated by e1 , . . . , e|s| subject to ea eb ` eb ea “ ˘2δab ; see [ABS].

<!-- page 80 -->
80

D. S. FREED AND M. J. HOPKINS

Lemma 9.27. Fix a real type s as in (9.25), and let Hn psq denote the n-dimensional version of the
group Hpsq of type s in Table (9.25). Write An psq “ Cliff `n bDpsq. Then there is an embedding
(9.28)

ι : Hn psq ÝÑ An psq

such that the natural map
c : Rn ˆ An psq ÝÑ An psq

(9.29)

is Hn psq-equivariant and graded commutes with right multiplication by An psq.
Here c is the extension of scalars of Clifford multiplication Rn ˆ Cliff `n Ñ Cliff `n . (Recall that
Rn Ă Cliff `n .) Note that An psq is Morita equivalent to Cliff `pn`sq ; we specify a Morita equivalence
in §9.2.2. We regard Hn psq as an ungraded group, and in fact ιpHn psqq is contained in the even
part of the superalgebra An psq. In the complex case (9.24) there is an embedding ιC : Pincn ãÑ
C
Cliff C
n b Cliff ´1 constructed using the same formulas as the real case s “ 1. Of course, there is also
the usual embedding ιC : Spincn ãÑ Cliff C
n.
Proof. The case s “ 0 requires no comment. For s “ 4 we use the fact that SU2 – Sp1 Ă H.
The scalar ´1 passes between the factors in the real tensor product Cliff `n bH, which explains the
division by t˘1u in the group H. In the remaining six cases Dpsq is a Clifford algebra on |s| generators, and the group Spin|s| Ă Cliff s is isomorphic to t˘1u, T, SU2 for |s| “ 1, 2, 3, respectively.
For |s| “ 1, 2 fix a unit vector e P R|s| Ă Dpsq; for |s| “ 3 define the volume form ω “ e1 e2 e3 as the
ordered product of the generators of Cliff |s| . Define ι by

(9.30)

g ÞÝÑ g b 1,
#
g b e, |s| “ 1, 2,
g ÞÝÑ
g b ω, |s| “ 3,

g P Spinn ,

λ ÞÝÑ 1 b λ,

λ P T or SU2 .

g P Pin˘
n z Spinn ,

A case-by-case check completes the proof. To illustrate, we check the equivariance of c for g P
Pinn z Spinn and |s| “ 1, 2; it suffices to take g “ ei for some standard basis element ei P Rn . For
ξ P Rn Ă Cliff `n , we have ei ¨ pξ b 1q “ ´ei ξe´1
i b 1. For ψ P Cliff `n homogeneous of parity |ψ|
and x P Dpsq, we have ei ¨ pψ b xq “ p´1q|ψ| ei ψ b ex, since ei acts as left multiplication in An psq
by ιpei q and the Koszul sign rule applies in the superalgebra An psq. Their Clifford product is
(9.31)

´ p´1q|ψ| ei ξψ b ex “ ei ¨ pξψ b xq,

which proves the equivariance. We leave the other checks to the reader.



Remark 9.32. In the condensed matter literature free fermion systems are often treated nonrelativistically and so are organized by nonrelativistic symmetry groups. More specifically, they are
organized by the subgroup I of internal vector symmetries that fix the points of space. (The internal

<!-- page 81 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

81

symmetry group K in our account, which starts from a relativistic theory, is the subgroup that fixes
the points of spacetime.) We can easily compute the group In in spacetime dimension n for a general
group of symmetries, as in §1. Namely, let ρn : Hn Ñ On be a Wick-rotated symmetry group. Fix
a splitting Rn “ R ˆ Rn´1 of translations of En into Wick-rotated-time translations cross spatial
translations. The subgroup O1 ˆ On´1 Ă On preserves that splitting, and O1 ˆ tidu Ă O1 ˆ On´1
is the vector subgroup of transformations that fix space pointwise. So for the symmetry group Hn
we define the nonrelativistic internal subgroup In as the pullback
In 
(9.33)





O1 ˆ tidu 



/ Hn
/ O1 ˆ On´1  



ρn

/ On

–

The inclusion Hn ãÑ Hn`1 induces an isomorphism In ÝÝÑ In`1 ; denote the colimit of these groups
as I. We tabulate I for each of the ten fermionic symmetry groups in Tables (9.24) and (9.25):

(9.34)

(9.35)

s

Hc

0
1

Spinc
Pinc

I

Cartan

T
(Spinc1 )
Z{2Z ˆ T (Pinc1 )

A
AIII

s

H

I

0
´1
´2

Spin
Pin`
Pin` ˙t˘1u T

t˘1u
Z{2Z ˆ t˘1u
Z{2Z ˙ T

(Spin1 )
(Pin`
1)
(Pin`
2)

D
DIII
AII

´3

Pin´ ˆt˘1u SU2

Z{4Z ˆt˘1u SU2 (Pin`
3)

CII

4

Spin ˆt˘1u SU2

3
2
1

Cartan

SU2

(Spin3 )

C

`

Z{2Z ˆ SU2

CI

´

Z{4Z ˙t˘1u T

(Pin´
3)
(Pin´
2)
(Pin´
1)

Pin ˆt˘1u SU2
Pin ˙t˘1u T
´

Pin

Z{4Z

AI
BDI

In the physics literature a Z{2Z subgroup of I containing a time-reversal symmetry, if it exists,
is labeled ‘Z{2ZT ’. The t˘1u subgroup is often labeled ‘Z{2Zf ’ where ‘f ’ means ‘fermionic’ since
the nontrivial element is the center of the spin group. The groups in parentheses are abstractly
isomorphic to the group I.
Remark 9.36. In the pullback (9.33) the group In has two extra pieces of structure: the canonical
central element k0 P K Ă In of order dividing two (Theorem 2.7(2)) and a Z{2Z-grading φ : In Ñ
O1 “ t˘1u with K “ ker φ. In condensed matter models we are given pIn , k0 , φq and part of
the determination of the low energy effective field theory is the (re)construction of the symmetry

<!-- page 82 -->
82

D. S. FREED AND M. J. HOPKINS

Ą n : “ Spinn ˆIn ;
type pHn , ρn q. We achieve this as follows. If φ is trivial then In “ K, so set SH
then define Hn “ SHn by (2.8). If φ is surjective, consider the commutative diagram
/ Spin

Spin1

n

#

(9.37)

In

#

Irn

{

/ Hn

{



#

n

# 
/ t˘1u


/ On

O1

J


/ Pin`

Pin`
1
 {

rn
/H

in which every parallelogram is a pullback, the kernel of every vertical map is K, and the northeast
diagonal composition is exact. Given pIn , k0 , φq define Irn by pullback, set K “ ker φ, set J “
r n be the pullback (2.10), and define Hn using (2.11).
Irn { Spin1 , let H
9.2.2. Twisted Atiyah-Bott-Shapiro map. Atiyah-Bott-Shapiro [ABS, §11] give a canonical construction of K-theory elements on Thom complexes. The universal incarnation [H, §6.1] is a map
of spectra
(9.38)

φ : M Spin ÝÑ KO.

Following their arguments we produce similar maps for the group Hpsq of type s in Table (9.25).
Fix a dimension n P Zě0 .
As a first step we stipulate a Morita equivalence
(9.39)

An psq

« Cliff `pn`sq .

Morita

There is a sign at stake—for any Clifford algebra A the groupoid of invertible pA, Aq-bimodules
is equivalent to the groupoid of Z{2Z-graded lines: the sign is the parity of the line. Define the
isomorphism
(9.40)

–

Cliff `n b Cliff `s ÝÝÝÑ Cliff `pn`sq

as in [ABS, (1.6)], and choose [ABS, (6.9)] a Cliff ˘8 -module M “ M 0 ‘ M 1 of dimension 8|8
such that the volume form acts as `1 on M 0 . There result Morita equivalences (9.39) for all
cases except s “ 4. For that we fix a quaternionic Cliff ˘4 -module N “ N 0 ‘ N 1 of quaternionic
dimension 1|1 such that the volume form acts as `1 on N 0 .

<!-- page 83 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

83

Now to the twisted ABS construction. Let π : Vn Ñ BHn psq be the universal bundle associated
to ρn : Hn psq Ñ On . Define the spinor bundle39
(9.41)

S :“ EHn psq ˆHn psq An psqop ÝÑ BHn psq;

This is a vector bundle of right An psqop -modules, or equivalently of left An psq-modules. Left Clifford multiplication (9.29) defines a family of odd skew-adjoint endomorphisms of π ˚ S Ñ Vn . These
operators are invertible off the zero section, and they commute with the left An psq-module structure.
`
˘
Therefore, using the Morita equivalence (9.39), they define an element in KOn`s ThompBHn psq; Vn q ,
where ThompBHn psq; Vn q is the Thom space of the universal bundle π : Vn Ñ BHn psq. Take the
limit n Ñ 8 after subtracting a trivial rank n bundle from Vn to obtain
(9.42)

φ : M Hpsq ÝÑ Σs KO

out of the Thom spectrum associated to the stable normal structure H. For s “ 0 this is the AtiyahBott-Shapiro (ABS) map [H, §6.1]. We rewrite in terms of the stable tangential structure H; see the
comments following (7.6). That perp maneuver exchanges Pin` and Pin´ , which in Table (9.25)
exchanges s Ø ´s. Therefore, (9.42) is a generalized ABS map
(9.43)

φ : M T Hpsq ÝÑ Σ´s KO.

In the complex case we obtain a generalized ABS map
(9.44)

φ : M T H c psq ÝÑ Σ´s K.

9.2.3. Twisted Dirac operators. Next, following [LM, §II.7], we define twisted Dirac operators for
the structure groups in Table (9.25). Suppose X is an n-dimensional Riemannian manifold equipped
with an Hn psq-structure P Ñ X. We assume given a connection on P Ñ X compatible with the
Levi-Civita connection on the orthonormal frame bundle. Use the embedding (9.28) to form the
Z{2Z-graded spinor bundle
(9.45)

S1 :“ P ˆHn psq An psq ÝÑ X.

Clifford multiplication (9.29) defines a vector bundle map T ˚ X b S1 ÝÑ S1 , and as usual the
Dirac operator D
{X acts on smooth sections of S1 as the covariant derivative followed by Clifford
multiplication. The Dirac operator is odd and skew-adjoint. (See 39 for our conventions.) It
commutes with the right An psq-module structure on S1 , or equivalently with the left An psqop -module
structure.
39Our choice of Aop in (9.41), rather than A, is essentially a sign choice. We use a geometric model [AS] in which

a class in KOm pXq is represented by a Z{2Z-graded vector bundle over X that is a left module for Cliff m equipped
with a family of commuting odd skew -adjoint (Fredholm) operators.

<!-- page 84 -->
84

D. S. FREED AND M. J. HOPKINS

There are topological and geometric indices of Dirac operators on compact manifolds. The topological index is defined using Fredholm operators [AS]. Namely, if X is closed, then D
{X extends
to a Fredholm operator on Sobolev completions of the space of smooth sections of S1 . This construction works in families: from a fiber bundle X Ñ S of closed Riemannian n-manifolds with
Hn psq-structure we obtain a family of odd skew-adjoint Fredholm operators parametrized by S.
Recalling that An psqop is Morita equivalent to Cliff ´pn`sq , via (9.39), we deduce that this family
of operators has a topological index that lies in KO´pn`sq pSq. For s “ 0 this reduces to the usual
Clifford-linear Dirac operator definition of the topological index. The Atiyah-Singer index theorem equates this topological index with an analytic index. If S is a smooth manifold and X Ñ S
a smooth family of Riemannian manifolds with Hn psq-structure, then there is a geometric index
y ´pn`sq pSq; see [FL] for the differential complex
that lies in the differential cohomology group KO
K-theory version as well as the Atiyah-Singer theorem in this differential context.
Remark 9.46. For s “ ˘1 this discussion specializes to an effective approach to Dirac operators
and index theory on unoriented manifolds with a Pin˘ -structure.
Remark 9.47. There is an analogous discussion in the complex case: replace H Ñ H c and KO Ñ K.
9.2.4. Free fermion theories on Minkowski spacetime M n´1 . As before we only treat the eight
real fermionic symmetry groups. Fix a type s in Table (9.25). Let H1,n´2 psq be the Lorentz
signature anti-Wick rotation of Hn´1 psq, as in (2.1). If s “ 0, which is the basic case, then
H1,n´2 psq “ Spin1,n´2 is the Lorentz spin group. The analog of (9.28) is an embedding (see (A.3)
for Cliff p,q conventions).
(9.48)

ι : H1,n´2 psq ÝÑ Cliff n´2,1 b Dpsq “: Bn´1 psq,

and there is a Morita equivalence of superalgebras
(9.49)

Bn´1 psq

« Cliff `pn´3`sq .

Morita

We use the conventions following (9.39) to define the Morita equivalence. The image of ι lies
in the even subalgebra Bn´1 psq0 Ă Bn´1 psq. A free fermionic field is specified by a real spinor
representation of H1,n´2 psq, which by definition is an ungraded real module S of Bn´1 psq0 . A
spinor field is then a function ψ : M n´1 Ñ S.
Remark 9.50. The CRT theorem, which is reviewed in Appendix A, implies that the free fermion
theory has a larger Lie group H1,n´2 psqβ Ą H1,n´2 psq of symmetries; the non-identity component
acts antilinearly on the Hilbert space of states. Proposition A.15(3) implies that the embedding (9.48) extends to H1,n´2 psqβ , and so H1,n´2 psqβ acts on the real vector space S, consistent
with Proposition A.20(2).
We quickly summarize special facts about a real spinor representation S of the Lorentz spin
group Spin1,n´2 ; proofs may be found in [De, §6]. Fix a component C of timelike vectors ξ P R1,n´2
with |ξ|2 ą 0. The first special property is the existence of symmetric Spin1,n´2 -invariant maps
(9.51)

Γ : S ˆ S ÝÑ R1,n´2 .

<!-- page 85 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

85

If S is irreducible, then Γ is unique up to a real factor and nonzero Γ are definite. Choose Γ positive
definite in the sense that Γpψ, ψq P C for all ψ P S. This fixes Γ up to a positive real factor.
There are two isomorphism classes of real irreducible representations for n ´ 1 ” 2, 6 pmod 8q and
a unique irreducible in other cases. Let S1 , S2 be representative irreducibles (in dimensions with a
unique irreducible, set S2 “ 0); let Z be the commutant of the spin action, so Z “ R, C, or H; and
fix positive definite Γ for S1 , S2 . A general real spinor representation S decomposes as
(9.52)

S – W1 bZ S1 ‘ W2 bZ S2

for right Z-modules W1 , W2 . Then positive definite pairings Γ in (9.51) correspond to positive
definite hermitian forms on W1 , W2 . For each choice there is a unique compatible Z{2Z-graded
Cliff n´2,1 -module structure on S ‘ S˚ , where S is in even degree and S˚ in odd degree; in particular,
the duality pairing S˚ b S Ñ R is Spin1,n´2 -invariant. Conversely, if S0 ‘ S1 is a Cliff n´2,1 -module,
then there is a duality pairing S0 b S1 Ñ R that makes the resulting symmetric form (9.51) positive
definite. (Deligne proves this for simple modules in [De, (6.1)]; any module is a sum of simples and
the argument applies to each summand.) Observe that Γ is a contractible choice.
The group H1,n´2 psq contains the spin group Spin1,n´2 as a subgroup and the quotient Qn´1 psq is
compact and independent of n up to isomorphism. An irreducible real representation of H1,n´2 psq
decomposes under the subgroup Spin1,n´2 as (9.52), and a central extension Q{
n´1 psq of Qn´1 psq
{
acts on each Wi . A choice of Qn´1 psq-invariant positive definite hermitian form on Wi yields a
H1,n´2 psq-invariant pairing (9.51), and then a Bn´1 psq-module S ‘ S˚ . Conversely, every Bn´1 psqmodule has this form.
Definition 9.53. The module S admits a mass term if there is a nondegenerate skew-symmetric
H1,n´2 psq-invariant bilinear form
(9.54)

m : S ˆ S ÝÑ R.

We call m the mass form.
Lemma 9.55. S admits a mass term if and only if S ‘ S˚ extends to a super module of the
superalgebra Bn´1 psqres, where e is odd, e2 “ ´1, and e (graded) commutes with the Clifford
generators of Bn´1 psq.
If s “ 4 the hypothesis is that e commutes with D “ H. As always, the commutation with Clifford
generators obeys the Koszul sign rule.
Proof. Given a Bn´1 psqres-module structure on S ‘ S˚ , define m by
(9.56)

mps1 , s2 q “ xEs1 , s2 y,

s1 , s2 P S,

`
´1 ˘
where E : S Ñ S˚ is part of the action of e “ E0 ´E0
on S ‘ S˚ . Since e2 “ ´1, the form m is
nondegenerate, and since e (graded) commutes with Bn´1 psq, the form m is H1,n´2 psq-invariant.
We must prove that m is skew-symmetric. It suffices to assume that S ‘ S˚ is a simple Bn´1 psqresmodule, since any module is a direct sum of simples. Then m is either symmetric or skew-symmetric.

<!-- page 86 -->
86

D. S. FREED AND M. J. HOPKINS

Let f P R1,n´2 Ă Cliff n´2,1 Ă Bn´1 psq be the Clifford generator with f 2 “ ´1. So f is a timelike
`
´1 ˘
vector, and we choose it to lie in C. Write f “ F0 ´F0
for its action on S ‘ S˚ . The positive
definiteness of Γ implies that
(9.57)

ps1 , s2 qS :“ xF s1 , s2 y,

s1 , s2 P S,

is a positive definite inner product on S. The mass form is mps1 , s2 q “ pF ´1 Es1 , s2 qS . Set A “
F ´1 E P EndpSq. Since m is either symmetric or skew-symmetric, either A˚ “ A or A˚ “ ´A,
where ˚ is with respect to the inner product (9.57). But ef “ ´f e implies A2 “ ´ idS , which rules
out A˚ “ A since A˚ A is a nonnegative operator.
Conversely, let m be a mass form. Using the inner product (9.57) write
(9.58)

mps1 , s2 q “ pBs1 , s2 qS ,

s1 , s2 P S,

?
for an invertible skew-symmetric operator B : S Ñ S. Define P “ B ˚ B and A “ P ´1 B “ BP ´1 .
`
´1 ˘
Then set E “ F A and let e P Bn´1 psqres act on S‘S˚ via E0 ´E0 , where as above f P Bn´1 psqres
`
˘
´1
acts as F0 ´F0 . We must check that this determines a well-defined action of Bn´1 psqres. It is
easy to verify that e2 “ ´ idS‘S˚ , and ef “ ´f e follows from F ´1 E “ ´E ´1 F , which in turn
follows from A “ ´A´1 . For later use we observe the commutation relation P F ´1 E “ F ´1 EP .
Let40 c P R1,n´2 ‘ R|s| Ă Bn´1 psq be a vector perpendicular to f , and write its action on the
`
´1 ˘
module S ‘ S˚ as C0 ˘C0 , the sign determined according as c2 “ ˘1 in Bn´1 psq. It remains to
show that ec “ ´ce as operators on S ‘ S˚ , or equivalently that
pEC ´1 q2 “ ˘ idS .

(9.59)
First, we use (9.56)–(9.58) to write
(9.60)

mps1 , s2 q “ xF Bs1 , s2 y “ xEP s1 , s2 y,

s1 , s2 P S.

Since cf “ ´f c in Bn´1 psq we have C ´1 F “ ˘F ´1 C. Next, cf P H1,n´2 psq Ă Bn´1 psq preserves
the duality pairing S˚ b S Ñ R, from which
(9.61)

xCF ´1 s˚ , C ´1 F sy “ ¯xs˚ , sy,

s˚ P S˚ ,

s P S.

Now since m is H1,n´2 psq-invariant,
(9.62)

mpC ´1 F s1 , C ´1 F s2 q “ mps1 , s2 q,

s1 , s2 P S.

Use the first expression in (9.60) together with the previous identities to conclude that C ´1 F B “
´BC ´1 F . It follows that C ´1 F commutes with P . Then rewrite (9.62) using the second expression
in (9.60) to deduce F C ´1 EP C ´1 F “ ¯EP . Apply the foregoing to arrive at (9.59).

40We leave the reader to give the appropriate modification for s “ 4.

<!-- page 87 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

87

There is an abelian group law on free fermion theories: direct sum of Clifford modules S. The
relationship [ABS, (11.4)], [A2, p. 383] between Clifford modules and K-theory yields the following.
Theorem 9.63. The abelian group of relativistic free fermion field theories in dimension n ´ 1
with type s, modulo those that admit a mass term, is isomorphic to
(9.64)

KOn´3`s pptq – π3´s´n pKOq.

Massive free fermions are anomaly-free; see [W1, §1.2] for a recent exposition. So the map from a
free fermion theory to the isomorphism class of its anomaly factors through the quotient (9.64).
Remark 9.65. The nature of an irreducible real twisted spin representation S0 depends on the
value of t “ n ´ 1 ` s pmod 8q. We ask if it is self-conjugate—if S˚0 – S0 —and if so whether the
induced nondegenerate bilinear form S0 b S0 Ñ R is symmetric (S0 orthogonal) or skew-symmetric
(S0 symplectic). Also, the commutant is a real division algebra, so is isomorphic to R, C, or H. We
list the types. If t ” 3, 4, 7, then S0 is symplectic, and the commutant is R, C, H, respectively. If
t ” 0, 1, 5, then S0 is orthogonal and the commutant is C, R, H, respectively. If t ” 2, 6, then there
are two nonisomorphic irreducible spin representations that are each others dual; the commutant
is R, H, respectively. For t ” 3, 4, 7 the K-group (9.64) vanishes, as it must since there is always a
mass term. For t ” 0, 1 the K-group is isomorphic to Z{2Z—the direct sum of two copies of the
irreducible module admits a mass term—and for t ” 5 it vanishes. For t ” 2, 6 the K-group is
isomorphic to Z. These are the cases for which the anomaly theory is not topological.
9.2.5. The anomaly theory and its deformation class. Our starting point is the Bn´1 psq0 -module S
that defines a free fermion theory on Minkowski spacetime M n´1 in pn´1q dimensions, as in §9.2.4.
In this subsection we sketch the associated n-dimensional anomaly theory, an invertible field theory
in n dimensions. (See [F3], [F4, §11] for expositions of anomalies from this viewpoint.) The anomaly
theory is not necessarily topological, but it has a deformation class that is topological—or which
can be regarded as a continuous invertible topological theory—and we propose a general formula
for it. See [W1] for a discussion of many special cases from a more physical viewpoint.
First, the real representation S of H1,n´2 psq extends to a complex representation SC of the complexification H1,n´2 psqpCq, which then restricts to a complex representation of Hn´1 psq. On a
curved Riemannian manifold X n´1 with differential Hn´1 psq-structure P Ñ X there is an associated complex vector bundle P ˆHn´1 psq SC Ñ X whose sections are complex spinor fields. There is
a Wick-rotated Dirac lagrangian, possibly with mass term, which is a skew-symmetric form on the
space of spinor fields. If X is closed, then the fermionic functional integral over the space of spinor
fields is the pfaffian of the Dirac operator on X. In a smooth family X Ñ S the pfaffian is not a
function, but rather is a section of the pfaffian line bundle
(9.66)

Pfaff X{S ÝÑ S.

The bundle Pfaff X{S Ñ S carries a canonical hermitian metric and compatible covariant derivative;
it is Z{2Z-graded by the mod 2 index. It is part of the anomaly theory associated to the module S.

<!-- page 88 -->
88

D. S. FREED AND M. J. HOPKINS

We now give a conjectural description of the entire anomaly theory. Fix k P Zě0 , which is the
codimension in the n-dimensional theory. Let X n´k be a closed pn ´ kq-dimensional Riemannian
manifold with differential Hn´k psq-structure. The universal Dirac operator (§9.2.3) acts on sections
of a real vector bundle S1 Ñ X of left An´k psqop -modules, where An´k psq “ Cliff `pn´kq bDpsq is
Morita equivalent to Cliff `pn´k`sq ; see (9.39). Let S ‘ S˚ Ñ X be the constant vector bundle with
fiber S ‘ S˚ . Then S1 bR pS ‘ S˚ q Ñ X is a real vector bundle of Z{2Z-graded An´k psqop b Bn´1 psqmodules. Our conventions in §9.2.2 give a definite Morita equivalence An´k psqop b Bn´1 psq «
Morita

Cliff ´p3´kq . For a family X Ñ S the geometric index of the Dirac operator41 with coefficients in S1 bR
y ´p3´kq pSq. Notice that it is independent of n
pS ‘ S˚ q lies in the differential cohomology group KO
and s. The anomaly picks off the lowest piece of the index via the canonical Pfaffian homomorphism
(9.67)

y
Pfaff : KO

´p3´kq

1`k

{
pSq ÝÑ IZp1q

pSq.

The invariants in differential IZp1q fit together into an invertible field theory; see [HS].
{ 1 pSq –
Example 9.68. For k “ 0, so X Ñ S of relative dimension n, there is an isomorphism IZp1q
p 1 pSq – MappS, Tq. The corresponding lowest piece of the index is the partition function e2πipξ{2q
H
of the anomaly theory on an n-manifold, where ξ is the Atiyah-Patodi-Singer invariant [APS]. The
division by 2 is due to the skew-symmetry of the Dirac form, the same division by 2 that passes
from determinant to pfaffian. The equality between the exponentiated ξ-invariant and the integral
in differential K-theory has only been proved in a basic case [Klo, O, BuS, FL] as far as we know.
2

{ pSq is isomorphic
Example 9.69. For k “ 1, so X Ñ S of relative dimension n´1, the group IZp1q
to the group of isomorphism classes of Z{2Z-graded hermitian line bundles L Ñ S with compatible
covariant derivative. For the anomaly theory that element is the pfaffian line bundle Pfaff X{S Ñ
S. The main theorem in [DF] is the gluing law in the non-extended invertible field theory in
dimensions n ´ 1, n with partition function the exponentiated ξ-invariant.
The story continues to lower dimensional manifolds, on which the invariants are graded gerbes [Lo,
Bu] and higher analogs.
The deformation class of an invertible field theory gotten from integration in differential cohomology is the underlying topological cohomology theory. In the background are techniques from [HS],
which lead to the following.
Conjecture 9.70. Fix a type s in Table (9.25) and a dimension n. Fix an isomorphism class of free
fermion theories modulo those that admit a mass term, i.e., an element rSs P π3´s´n pKOq. Then
the deformation class of the n-dimensional anomaly theory is the homotopy class of the composition
(9.71)

φ^rSs

µ

Pfaff

M T Hpsq ÝÝÝÝÝÑ Σ´s KO ^ Σ´3`s`n KO ÝÝÑ Σn´3 KO ÝÝÝÝÑ Σn`1 IZp1q,

where φ is the Atiyah-Bott-Shapiro map (9.43), µ is multiplication in the ring spectrum KO, and
Pfaff is the topological version of (9.67).
41Some details of this construction appear in [FH2, Appendix]

<!-- page 89 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

89

There is a similar conjecture in the complex case (9.24) with the usual replacements H Ñ H c and
KO Ñ K. We hope to address this conjecture in the future. We use it in our computations below.
Remark 9.72. If the group π3´s´n pKOq is finite, hence is isomorphic to Z{2Z, then there is a reflection positive invertible topological field theory in the deformation class whose partition function
is the mod 2 index. If the group is free cyclic, hence isomorphic to Z, then the deformation class is
represented by a reflection positive invertible field theory whose partition function is the exponentiated ξ-invariant of Atiyah-Patodi-Singer, the secondary invariant for a Z-valued topological index
in n ` 1 dimensions. This is the case in which there are local anomalies as well as global anomalies,
and because of the shift s it happens in both even and odd dimensions.

9.2.6. Massive free fermion theories. In §9.2.5 we explained how a free fermion theory in pn ´
1q dimensions has an associated n-dimensional invertible anomaly theory, and Conjecture 9.70
states its deformation class. Here we show that a second scenario leading to invertible n-dimensional
theories has the same starting data. This is the scenario we apply in §9.3. Namely, begin with a
massive free fermion theory in n dimensions. Because the theory has a mass gap its long-range
physics is described by a field theory, which naturally is also n-dimensional. As argued in §5.4
we expect that theory to be, at least locally, the product of a topological theory and an invertible
theory. But a massive free fermion theory has a unique vacuum on each spatial manifold—the
vacuum in the fermionic Fock space—so in fact the long-range effective theory is invertible.
Remark 9.73. One must make choices to define the massive free fermion theory, and they can be
summarized as a trivialization of an anomaly; see [F4, §11] for a general discussion. There is a
canonical choice for each fixed mass, and it is implicitly used in the discussion below as well as
in §9.3. However, when the mass is a not necessarily constant function then there is an anomaly;
see [CFLS] for discussion and details.
As in previous sections fix a type s in Table (9.25) and let H1,n´1 psq be the Lorentz signature antiWick rotation of the corresponding group Hn psq. In the notation of (9.48) there is an embedding
H1,n´1 psq ãÑ Bn´1 psqre1 s, where e1 is an extra Clifford generator with pe1 q2 “ `1. By Lemma 9.55
spinor representations of H1,n´1 psq that admit a mass term are in bijection with super modules
over the superalgebra Bn´1 psqre1 , es, where e is an extra Clifford generator with e2 “ ´1. Observe
that Bn´1 psqre1 , es is Morita equivalent to Cliff `pn´3`sq . We speculate that
(9.74)

(i) the resulting low energy theory is trivial if the Bn´1 psqre1 , es-module is
extended to a module over the algebra Bn´1 psqre1 , e, f s with f 2 “ ´1.

The group of equivalence classes of Bn´1 psqre, f s-modules modulo those that extend is the Kgroup (9.64). The Morita equivalence to massless theories in dimension n ´ 1 and the vanishing of
the anomaly for theories that admit a mass term are evidence in favor of (9.74). Furthermore, we
speculate that
(9.75)

(ii) the low energy theory is invertible and its deformation class is (9.71).

<!-- page 90 -->
90

D. S. FREED AND M. J. HOPKINS

As some evidence supporting (ii) we point out that the partition function in special cases is computed in [W1, §2.1.6, §2.2.3, §3.4, §4.3, §5]. The universal part of the partition function of the low
energy theory is an exponentiated ξ-invariant, as in Example 9.68.
9.3. Phases of topological insulators and topological superconductors
We apply Conjecture 8.37 to compute possible topological phases for each of the 10 fermionic
symmetry types (9.24) and (9.25). We remind that the fermionic symmetry groups with K “ T
pertain to topological insulators; those with K “ t˘1u and K “ SU2 pertain to topological
superconductors. The abelian group of topological phases—that is, the group of deformation classes
of reflection positive invertible topological field theories with symmetry group H in n spacetime
dimensions—is
T Pn pHq :“ rM T H, Σn`1 IZp1qs.

(9.76)

It may be computed from the homotopy groups42 πq M T H; see the universal property (5.17). As we
are only interested in n ď 5, we need only compute for q ď 6, and for q “ 6 we only need to know
π6 M T H{torsion, since that determines Hompπ6 M T H, Zq. The abelian group T Pn pHq classifies
deformation classes of interacting theories. The abelian group of deformation classes of massive
(gapped) free fermion theories in n dimensions modulo those with trivial long-range effective theory
is given by Lemma 9.55 and (9.74), at least conjecturally:
#
(9.77) F Fn pHpsqq :“

π3´s´n pKq – rΣ´s K, Σn`1 IZp1qs,
H c psq a complex symmetry type;
π3´s´n pKOq – rΣ´s KO, Σn`1 IZp1qs, Hpsq a real symmetry type,

where s is the parameter in (9.24) or (9.25). (See Remark 9.65 for an enumeration of the K-theory
groups in the real case via the types of spin representation.) According to (9.75) and (9.71) the
natural homomorphism
(9.78)

Φ : F Fn pHq ÝÑ T Pn pHq

from the group of deformation classes of free fermion theories to the group of all theories is the
product with the ABS map (9.43). We compute Φ for each symmetry class.
The results are organized by internal symmetry group. Some of the bordism groups appear
in the mathematics literature, whereas for the more exotic symmetry groups the computations
are new. With the bordism groups in hand, the classification of interacting theories is an immediate consequence of Conjecture 8.37 and the universal property expressed in the short exact
sequence (5.17). The free fermion computation is (9.64). The map (9.78) from massive free fermion
phases to interacting phases does not follow from the rest—it must also be computed. We give a
uniform treatment based on Lemma 9.27 and §9.2.2. Manifold generators and formulas for partition
functions in 4 dimensions are worked out in [GPW].
42These are Thom’s bordism groups, but for the perpendicular tangential structure on the stable normal bundle

(see footnote 28 ). Note that Pin` { Pin´ and Pinc̃` { Pinc̃´ exchange when passing from tangential to normal.

<!-- page 91 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

91

We check our computations against the condensed matter literature, where groups of SPT phases
are deduced using very different arguments. There is almost total agreement, and in the few places
we differ we use the homotopy computations to predict what should happen in the physics. The
computations that we did not find in the physics literature should be considered predictions.
9.3.1. Internal symmetry group K “ t˘1u. The symmetry groups are classified in Proposition 2.16.
The low degree spin and pin bordism groups are described in a geometric way in [KT1]. The general
structure of spin bordism is elucidated in [ABP1]. The computation of pin bordism groups in all
degrees may be found in [ABP2] and [KT2].
Theorem 9.79. The low degree bordism groups for K “ t˘1u are:

(9.80)

q

πq M T Spin

πq M T Pin`

πq M T Pin´

6
5
4
3
2
1
0

0
0
Z
0
Z{2Z
Z{2Z
Z

0
0
Z{16Z
Z{2Z
Z{2Z
0
Z{2Z

Z{16Z
0
0
0
Z{8Z
Z{2Z
Z{2Z

Corollary 9.81 (Symmetry class D). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Spin are isomorphic to:

n

(9.82)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pSpinq ÝÝÑ T Pn pSpinq ÝÑ coker Φ
0
0
0
0
0
0

0
0
Z
Z{2Z
Z{2Z
0

0
0
Z
Z{2Z
Z{2Z
0

0
0
0
0
0
0

Literature Note. The groups T P1 pSpinq and T P2 pSpinq were computed by the “group super-cohomology
theory” in [GW]; see Table II. That theory is a 2-stage Postnikov truncation of IZp1q, so in general
only computes a subgroup of topological phases; it is the entire group in very low dimensions. The
interacting classification T Pn pSpinq appears in [QHZ]: see §IIA for n “ 3, §IID for n “ 2, and §IIE
for n “ 1. The group T P3 pSpinq is discussed in [LV, §V A], but their restriction to “non-chiral”
phases means that the E8 phases that generate T P3 pSpinq were not accounted for. All of the groups
in the table, but not the map from free fermions to interacting theories, appear in [KTTW]. Those
authors conjecture a cobordism classification of interacting fermionic SPT phases.

<!-- page 92 -->
92

D. S. FREED AND M. J. HOPKINS

Proof. That Φ is an isomorphism in low dimensions follows since the ABS map M Spin Ñ KO
induces an isomorphism on πď7 .

In the next example we meet a nontrivial kernel of Φ, which is to say free fermion phases that
become trivial when interactions are allowed.
Corollary 9.83 (Symmetry class DIII). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Pin` are isomorphic to:

(9.84)

Φ

n

ker Φ ÝÑ F Fn pPin` q ÝÝÑ T Pn pPin` q ÝÑ coker Φ

5
4
3
2
1
0

0
16Z
0
0
0
2Z

0
Z
Z{2Z
Z{2Z
0
Z

0
Z{16Z
Z{2Z
Z{2Z
0
Z{2Z

0
0
0
0
0
0

Literature Note. There are many arguments in the physics literature that 16 copies of the basic
free fermion theory in 4 dimensions has a trivial phase once interactions are allowed, and that this
does not occur with fewer copies. (As noted in Remark 8.41, the group T P4 pPin` q is torsion, hence
a priori some multiple of the free theory necessarily becomes trivial once interactions are allowed.)
A sample includes [K1, FCV, WS, MFCV, K4] and [W1, §4]. The interacting case in 3 dimensions
is investigated in [W1, §3], and various aspects of the invertible field theory are described explicitly.
It is also discussed in [LV, §V B], but the nonzero element is missed within the “K-formalism” as
the authors explain. The groups T Pn pPin` q as computed here also appear in [KTTW, Table 2].
Corollary 9.85 (Symmetry class BDI). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Pin´ are isomorphic to:
n

(9.86)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pPin´ q ÝÝÑ T Pn pPin´ q ÝÑ coker Φ
0
0
0
8Z
0
0

0
0
0
Z
Z{2Z
Z{2Z

0
0
0
Z{8Z
Z{2Z
Z{2Z

0
0
0
0
0
0

Literature Note. The breaking of the Z classification of free fermions in 2 spacetime dimensions to
the Z{8Z classification of interacting fermions is treated in [FK1, FK2, TPB, YWOX], and [W1, §5].
The groups T Pn pPin´ q, n “ 1, 2, are computed by the group super-cohomology in [GW, Table II].
The vanishing of T P3 pPin´ q is argued in [LV, §V B]. The groups T Pn pPin´ q as computed here also
appear in [KTTW, Table 2].

<!-- page 93 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

93

9.3.2. Internal symmetry group K “ T. The symmetry groups are classified in Proposition 9.4.
Spinc bordism groups are computed in [ABP1]; cf. [Sto, Chapter XI]. Pinc bordism groups are
computed in [BG]. The twisted Pinc bordism computations are new.
Theorem 9.87. The low degree bordism groups for K “ T are:

(9.88)

q

πq M T Spinc

πq M T Pinc

πq M T Pinc̃`

πq M T Pinc̃´

6
5
4
3
2
1
0

Z2
0
Z2
0
Z
0
Z

Z{16Z ˆ Z{4Z
0
Z{8Z ˆ Z{2Z
0
Z{4Z
0
Z{2Z

Z2 ˆ Z{2Z
0
pZ{2Zq3
Z{2Z
Z
0
Z{2Z

Z2 ˆ Z{2Z
0
Z{2Z
0
Z ˆ Z{2Z
0
Z{2Z

Corollary 9.89 (Symmetry class A). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Spinc are isomorphic to:

n

(9.90)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pSpinc q ÝÝÑ T Pn pSpinc q ÝÑ coker Φ
0
0
0
0
0
0

Z2
0
Z2
0
Z
0

Z
0
Z
0
Z
0

Z
0
Z
0
0
0

Literature Note. The vanishing of the group T P4 pSpinc q is mentioned in [WPS] at the end of
Appendix F.
Corollary 9.91 (Symmetry class AIII). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Pinc are isomorphic to:

(9.92)

Φ

n

ker Φ ÝÑ F Fn pPinc q ÝÝÑ T Pn pPinc q ÝÑ coker Φ

5
4
3
2
1
0

0
8Z
0
4Z
0
2Z

0
Z
0
Z
0
Z

0
Z{8Z ˆ Z{2Z
0
Z{4Z
0
Z{2Z

0
Z{2Z
0
0
0
0

<!-- page 94 -->
94

D. S. FREED AND M. J. HOPKINS

Literature Note. The group T P4 pPinc q and the map from free fermions is discussed in [WS, §III];
see also [SeWi, §A.4] for the map from free fermions. The vanishing of the group T P3 pPinc q is
discussed in [LV, §V D] as well as in the last paragraph of [W1, §3.7].
Corollary 9.93 (Symmetry class AII). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Pinc̃` are isomorphic to:
n

(9.94)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pPinc̃` q ÝÝÑ T Pn pPinc̃` q ÝÑ coker Φ
0
0
0
0
0
0

Z2
pZ{2Zq3
Z{2Z
0
Z
Z{2Z

Z
Z{2Z
Z{2Z
0
Z
0

Z
pZ{2Zq2
0
0
0
Z{2Z

Literature Note. The Z{2Z invariant of free fermion systems in 3 and 4 spacetime dimensions was
introduced by Kane-Mele [KM] and Fu-Kane-Mele [FKM] and has been further studied in many
papers. The interacting case in 4 dimensions is investigated in [WPS] and in 3 dimensions in [W1,
§3.7]; their results agree with ours. The initial computation in [LV, §V C 2] of T P3 pPinc̃` q –
pZ{2Zq2 was corrected in a subsequent erratum. The original argument in that paper asserts a
Z{2Z subgroup of bosonic phases, which would have symmetry group O ˙ T, as in (9.6). We
`
˘
computed that π3 M pO ˙ Tq – Z{2Z and the natural projection Pinc̃` Ñ O ˙ T induces the
zero map on π3 of the Thom spectra. This implies that the group of bosonic phases is Z{2Z, as
claimed, but that the lift of that bosonic phase to a fermionic phase is trivial. This triviality of the
pullback was not noticed initially; our homotopy theoretic methods give a systematic approach, and
we encounter this issue again in Literature Note 9.3.2. The physical results in 4 dimensions were
recounted in [M] at the end of §VI, where the question of agreement with a bordism computation
was raised. This provided strong motivation for the computations in this section. We remark that
the description of the partition function of some phases in terms of Stiefel-Whitney classes matches
our bordism computations as well. Also, §4.7 of [W1] treats the invertible topological field theory
in 4 dimensions defined by the free fermion theory, so only detects the image of Φ in T P4 pPinc̃` q.
Corollary 9.95 (Symmetry class AI). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group Pinc̃´ are isomorphic to:
n

(9.96)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pPinc̃´ q ÝÝÑ T Pn pPinc̃´ q ÝÑ coker Φ
0
0
0
0
0
0

Z
0
0
0
Z
Z{2Z

Z2
Z{2Z
0
Z{2Z
Z
Z{2Z

Z
Z{2Z
0
Z{2Z
0
0

<!-- page 95 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

95

Literature Note. The group T P4 pPinc̃´ q is discussed in detail in the erratum to [WS]. The group
T P3 pPinc̃´ q is asserted to be cyclic of order two in [LV, §V C 1] generated by a bosonic phase.
The bosonic phase is the same one identified for the symmetry class AII—see the Literature Note
following (9.94)—and again we compute that its lift to a fermionic phase with symmetry group Pinc̃´
vanishes, which explains the discrepancy.

9.3.3. Internal symmetry group K “ SU2 . The symmetry groups G0 , G` , G´ are defined and
classified in Proposition 9.16.
Theorem 9.97. The low degree bordism groups for K “ SU2 are:

(9.98)

q

πq M T G0

πq M T G`

πq M T G´

6
5
4
3
2
1
0

Z{2Z ˆ Z{2Z
Z{2Z ˆ Z{2Z
Z2
0
0
0
Z

pZ{2Zq4
Z{2Z
Z{4Z ˆ Z{2Z
0
Z{2Z
0
Z{2Z

Z{2Z ˆ Z{4Z ˆ Z{16Z
pZ{2Zq2
pZ{2Zq3
0
Z{2Z
0
Z{2Z

Corollary 9.99 (Symmetry class C). The groups of deformation classes of free fermion theories
and of reflection positive invertible theories with symmetry group G0 “ Spin ˆt˘1u SU2 are isomorphic to:

n

(9.100)

5
4
3
2
1
0

Φ

ker Φ ÝÑ F Fn pG0 q ÝÝÝÝÑ T Pn pG0 q ÝÝÝÝÑ coker Φ
0
0
0
0
0
0

Z{2Z
0
Z
0
0
0

Z{2Z ˆ Z{2Z
0
Z2
0
0
0

Z{2Z
0
Z
0
0
0

Literature Note. That T P4 pG0 q “ 0 was suggested in [WS] in the last paragraph preceding §V A.
Corollary 9.101 (Symmetry class CI). The groups of deformation classes of free fermion theories and of reflection positive invertible theories with symmetry group G` “ Pin` ˆt˘1u SU2 are

<!-- page 96 -->
96

D. S. FREED AND M. J. HOPKINS

isomorphic to:

(9.102)

Φ

n

ker Φ ÝÑ F Fn pG` q ÝÝÑ T Pn pG` q ÝÑ coker Φ

5
4
3
2
1
0

0
4Z
0
0
0
2Z

0
Z
0
0
0
Z

Z{2Z
Z{4Z ˆ Z{2Z
0
Z{2Z
0
Z{2Z

Z{2Z
Z{2Z
0
Z{2Z
0
0

Our computations prove Φ maps the generator of F F4 pG` q to an element of order 4 in T P4 pG` q.
Literature Note. Wang-Senthil [WS, §V] discusses the n “ 4 case and conjecture the same group
T P4 pG` q – Z{4Z ˆ Z{2Z that we compute; the map from free fermions also agrees.
Corollary 9.103 (Symmetry class CII). The groups of deformation classes of free fermion theories and of reflection positive invertible theories with symmetry group G´ “ Pin´ ˆt˘1u SU2 are
isomorphic to:

(9.104)

Φ

n

ker Φ ÝÑ F Fn pG´ q ÝÝÑ T Pn pG´ q ÝÑ coker Φ

5
4
3
2
1
0

0
0
0
2Z
0
0

Z{2Z
Z{2Z
0
Z
0
0

pZ{2Zq2
pZ{2Zq3
0
Z{2Z
0
Z{2Z

Z{2Z
pZ{2Zq2
0
0
0
Z{2Z

Literature Note. The 4-dimensional case is treated in [WS, §VI]; the answer they obtain for T P4 pG´ q
is pZ{2Zq5 , which disagrees with the corresponding entry in (9.104), but it may be a different
symmetry group they are considering. In any case, in the note following Corollary 9.93, we compute
the group of bosonic phases with symmetry group O ˆt˘1u SU2 and find pZ{2Zq4 , but the lift to
fermionic phases kills a pZ{2Zq2 subgroup.

10. Computations
The computations in §9.3 involve finitely generated abelian groups having no odd torsion, so
it suffices then to make them after completing at 2. This can be done using the Adams spectral
sequence
(10.1)

˚
Exts,t
A pH pM T Hq, Z{2q ñ πt´s M T H,

<!-- page 97 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

97

where A is the mod 2 Steenrod algebra, and, though not indicated in the notation, the homotopy
groups have been completed at 2.
What makes this approach tractable is an identification43 of the spectrum Σs M T Hpsq with

(10.2)

M Spin ^M T O|s|

´3 ď s ď 0

M Spin ^M O|s|

0ďsď3

ΣM Spin ^M SO3

s “ 4,

and in the complex case, of Σs M T H c psq with
M Spinc ^M Os « Σ´2 M Spin ^M U1 ^ M Os .

(10.3)

Let A1 Ă A be the sub algebra generated by Sq1 and Sq2 . Anderson, Brown, and Peterson [ABP1]
give an isomorphism
H ˚ M Spin « A b tZ{2 ‘ M u

(10.4)

A1

in which M is a graded A1 -module with Mi “ 0 for i ă 8. This means that for t ´ s ă 8 one can
identify the E2 -term of the Adams spectral sequence for44 π˚ M T Hpdq with
˚´d
Exts,t
M T O|d| , Z{2q
A1 pH

´3 ď d ď 0

˚`d
Exts,t
M O|d| , Z{2q
A1 pH
s,t
˚`3
ExtA1 pH
M SO3 , Z{2q

´0 ď d ď 3
d“4,

and of π˚ M T H c pdq with
˚`2`d
Exts,t
M U1 ^ M Od , Z{2q
A1 pH

d “ 0, 1 .

These groups are computed by standard methods, and the computation, as well as the spectral sequences (which collapse) are described Figure 5 and give the results described in tables (9.80), (9.88),
and (9.9).
The relationship with the free fermion theories is given by maps of spectra
(10.5)

M T Hpsq Ñ Σ´s KO

(10.6)

M T H c psq Ñ Σ´s K

43Remark: Corollary 2.12 implies that for any symmetry type pH, ρq, the spectrum M T H is an M Spin-module.
44Here only we use the notation ‘Hpdq’ in place of ‘Hpsq’ to avoid the conflict with Adams’ homological grading

index ‘s’.

<!-- page 98 -->
98

D. S. FREED AND M. J. HOPKINS

or, under the above identifications, maps

(10.7)

M Spin ^M T O|s| Ñ KO

´3 ď s ď 0

M Spin ^M O|s| Ñ KO

3ěsě0

ΣM Spin ^M SO3 Ñ KO

s“4

c

M Spin ^M Os Ñ K

s “ 0, 1 .

These are all maps of M Spin (or M Spinc ) modules, in which KO and K are into M Spin and
M Spinc -modules using the Atiyah-Bott-Shapiro orientation. They are therefore determined by
their restrictions

(10.8)

M T O|s| Ñ KO

´3 ď s ď 0

M O|s| Ñ KO

3ěsě0

ΣM SO3 Ñ KO

s“4

M Os Ñ K

s “ 0, 1 .

These are described in Propositions 10.24, 10.27, and 10.35 below, and using them, the assertions
about the maps in tables (9.82), (9.84), (9.86), (9.90), (9.92), (9.94), (9.96), (9.100), (9.102),
and (9.104) can be verified. The details are summarized in the charts in Figure 5. The complex
case is easier and left to the reader. See [C, BeC] for a detailed account of the computations.
For the identifications (10.2) and the maps (10.8) we begin with a uniform description of the
groups BHp˘sq (for s ‰ 4). Write
(10.9)

P “ KpZ{2, 1q ˆ KpZ{2, 2q

with the group structure
(10.10)

px1 , x2 q ˚ py1 , y2 q “ px1 ` y1 , x2 ` y2 ` x1 y1 q

in which xi , yi P H i p ´ , Z{2q. With this choice the map
pw1 ,w2 q

(10.11)

BO ÝÝÝÝÝÑ P

is a group homomorphism.
For s ě 0 define a map B r
Hpsq Ñ BO by the homotopy pullback square
(10.12)

r
B Hpsq

/ BOs





BO

pw1 ,w2 `w12 q

pw1 ,w2 q

/P

<!-- page 99 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

Figure 5. The Adams spectral sequences

r
and set B Hp´sq
Ñ BO to be the composite

(10.13)

´ id

r
B Hpsq
Ñ BO ÝÝÑ BO.

99

<!-- page 100 -->
100

D. S. FREED AND M. J. HOPKINS

r
The space B Hp´sq
Ñ BO fits into a homotopy pullback square
(10.14)

r
B Hp´sq

/ BOs





BO

pw1 ,w2 q

/P.

pw1 ,w2 q

For later reference we note
r
Remark 10.15. The homotopy fiber of B Hp˘sq
Ñ BO, being the same as the homotopy fiber of
BOs Ñ P is
(10.16)

B Spins

sě1

Z{2 ˆ BZ{2

s“0.

r
For ´3 ď s ď 3 one may identify B Hpsq
Ñ BO with BHpsq Ñ BO. The map BHp4q Ñ BO fits
into a homotopy pullback diagram
(10.17)

BHp4q

/ BSO3





BO

pw1 ,w2 q

w2

/P.

We leave the verification of these assertions to the reader.
With s ě 0, the maps B r
Hp˘sq Ñ BO and B r
Hp˘sq Ñ BOs can also be expressed in terms of
the diagrams of homotopy pullback squares
(10.18)

r
B Hpsq

/ B Spin




/ BO

BO ˆ BOs

´ id ´pVs ´sq

pw1 ,w2 q

/P

and
(10.19)

Br
Hp´sq

/ B Spin




/ BO

BO ˆ BOs

id ´pVs ´sq

pw1 ,w2 q

/P.

r
A map X Ñ B Hpsq
therefore classifies a pair pV, Vs q consisting of a stable vector bundle V (of
virtual dimension 0), a vector bundle Vs of dimension s and a Spin structure on ´V ´ pVs ´ sq.

<!-- page 101 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

101

r
Writing W “ ´V ´ pVs ´ sq, so that V “ ´W ´ pVs ´ sq, one sees that B Hpsq
classifies pairs
r
pW, Vs q in which W is a stable Spin bundle of virtual dimension zero. Thus B Hpsq Ñ BO may be
identified with the map
B Spin ˆBOs Ñ BO
pW, Vs q ÞÑ ´W ´ pVs ´ sq.
r
Similarly B Hp´sq
Ñ BO may be identified with
B Spin ˆBOs Ñ BO
pW, Vs q ÞÑ ´W ` pVs ´ sq,
and BHp4q Ñ BO with
B Spin ˆBSO3 Ñ BO
via either of the maps

pW, V3 q ÞÑ ´W ` pV3 ´ 3q or
pW, V3 q ÞÑ ´W ´ pV3 ´ 3q.
This leads to the identifications
r
M T Hpsq
« Σ´s M Spin ^M Os
(10.20)

r
M T Hp´sq
« Σs M Spin ^M T Os
M T Hp4q « Σ´3 M Spin ^M SOp3q
« Σ3 M Spin ^M T SOp3q.

r
We define B Hp˘sq
n Ñ BOn by the pullback square
(10.21)

Br
Hp˘sqn

/Br
Hp˘sq




/ BO .

BOn

r n psq classifies a pair pVn , Vs q consisting of vector bundles of dimension n and s and
The space B H
r
a Spin structure on ´Vn ´ Vs (or, equivalently on Vn ` Vs ), while B Hp´sq
n classifies pairs pVn , Vs q
a Spin structure on ´Vn ` Vs . For s ě 0 there is therefore a pullback square
(10.22)

r n psq
BH


BOn ˆ BOs

/ B Spin

n`s


/ BOn`s .

<!-- page 102 -->
102

D. S. FREED AND M. J. HOPKINS

r
r
Proposition 10.23. The space B Hp˘sq
n is the classifying space of a compact Lie group Hp˘sqn .
r n psq is the stabilizer in Spinn`s of a s-plane in Rn`s .
The group H
Proof. The first assertion is a consequence of the pullback square (10.21) and Remark 10.15. The
second is immediate from (10.22)

The construction of §9.2.2 leads to maps
r
M T Hpsq
Ñ Σ´s KO

and so, by (10.20), to
M Spin ^M T Os Ñ KO
M Spin ^M Os Ñ KO
ΣM Spin ^M SO3 Ñ KO.
These are maps of M Spin-modules, so to describe them it suffices the restricted maps
M Os Ñ KO
M T Os Ñ KO
ΣM SO3 Ñ KO .
Proposition 10.24. Let V Ñ BOs be the universal vector bundle. The map M Os Ñ KO corresponds to the element of KOpV, V ´ 0q given by applying the difference bundle construction to
V ˆ Λ˚ pV q Ñ Λ˚ pV q
pv, ωq ÞÑ v ^ ω.
Proof. In the notation of 9.27, the algebra Apsq is Cliff `s b Cliff ´s , so that Aop is also Cliff `s b Cliff ´s ,
but with left Clifford multiplication by v P Rs sending x b y to p´1q|x| x b vy. The composed embedding Os Ñ Hs Ñ Aop is the map
(10.25)

Os Ñ Cliff `s b Cliff ´s

sending reflection through the hyperplane perpendicular to v P Rs to v b v.
Let P Ñ BOs be the universal principal Os bundle. The K-theory class described in 9.2.2 is the
difference bundle on pV, V ´ 0q associated to the Os -equivariant “Clifford multiplication” map
(10.26)

Rs ˆ pAop b M q Ñ pAop b M q
Aop

Aop

<!-- page 103 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

103

in which M “ Cliff s is the left Aop bimodule specified in §9.2.2, and giving the Morita equivalence
of Aop with R. Passing to associated bundles, this works out to be
V ˆ CliffpV q Ñ CliffpV q
pv, ωq ÞÑ p´1q|ω| ωv.
The anti-automorphism of CliffpV q extending the identity map of V gives an isomorphism of this
with
V ˆ CliffpV q Ñ CliffpV q
pv, ωq ÞÑ vω.
The claim now follows from the standard way of “wrapping up” the complex V ˆ ΛpV q Ñ ΛpV q
using v ˘ ιv (see [ABS, Proposition 11.6] and the surrounding discussion for the complex case). 
Proposition 10.27. The map M T Os Ñ KO factors as
(10.28)

M T Os Ñ pBOs q` Ñ KO

in which the first map is the map
(10.29)

`
˘
ThompBOs , ´V q Ñ Thom BOs , p´V q ‘ V

and the second corresponds to the trivial line bundle 1 P KO0 pBOs q.
Proof. Write Grs pRn`s q for the Grassmannian of s-planes in pn ` sq-space, and let Vn and Vs be
the universal n-plane and s-plane bundles. These bundles come equipped with a trivialization
(10.30)

Vs ‘ Vn « Grs pRn`s q ˆ Rn`s .

From the identification Grs pRn`s q “ Spinn`s {Hn of Proposition 10.23 it follows that the bundle Vn comes equipped with an Hn -structure. The construction of 9.2.2 gives an element U P
KOn`s pThompGrs pRn`s q, Vn qq. The assertion is that this pulled back from the canonical generator
(the suspension of 1 P KO0 pptq) of K̃On`s pS n`s q along the map
ThompGrs pRn`s q; Vn q Ñ ThompGrs pRn`s q; Vs ‘ Vn q
« S n`s ^ Grs pRn`s q` Ñ S n`s .
This is immediate from the construction. The algebra Apsqop is Cliff ´s b Cliff ´n . The class U is
the complex of left A-modules (which come as right Aop -modules) obtained by applying
(10.31)

Spins`n ˆ p ´ q
Hn

<!-- page 104 -->
104

D. S. FREED AND M. J. HOPKINS

to the the Hn -equivariant Clifford multiplication map
(10.32)

Rn ˆ Cliff ´s b Cliff ´n Ñ Cliff ´s b Cliff ´n .

This map evidently extends to the Spins`n equivariant Clifford multiplication map
(10.33)

Rs ‘ Rn ˆ Cliff ´s b Cliff ´n Ñ Cliff ´s b Cliff ´n

so the class U is pulled back from the bundle of left A-modules on pRs`n , Rs`n ´ t0uq obtained by
applying
(10.34)

Spinn`s

ˆ

Spinn`s

p´q

to (10.33). This class represents the suspension of 1.



For the case s “ 4 what we require is the following
Proposition 10.35. The restriction of the map
S 1 ^ M SO3 Ñ KO
to S 4 Ñ KO is the generator of K̃O0 pS 4 q.
Proof. From the diagram (10.17) a map to BHp4q can be thought of as consisting of a stable vector
bundle V , an oriented 3-plane bundle V3 and a Spin-structure on V ‘V3 . We map BSOp4q Ñ BHp4q
by taking V to corresponding to the defining representation and V3 to be one of the two irreducible
representations of dimension 3. The construction of §9.2.2 then leads to the bundle on M SOp4q
corresponding to the SOp4q-equivariant map
R4 ˆ N Ñ N
where N is the irreducible quaternionic Cliff 4 -module specified in 9.2.2 with SOp4q-action from the
embedding above. This restricts to the generator of KOpR4 , R4 ´t0uq, by [ABS, Theorem 11.5]. 
The two complex cases are handled similarly, using either the pullback squares
(10.36)

BH c psq

/ BOs





BO

pw1 ,βw2 q

pw1 ,βw2 q

/ KpZ{2, 1q ˆ KpZ, 3q

for the identification
(10.37)

M T H c psq « Σ´s M Spinc ^M Os

<!-- page 105 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

105

or
(10.38)

HB

/ BOs ˆ BU p1q





BO

pw1 ,w2 q

pw1 ,w2 `c1 q

/P

for the identification
(10.39)

M T H c psq « Σ´s´2 M Spin ^M U1 ^ M Os .

11. A topological spin-statistics theorem
In a relativistic quantum field theory the spin-statistics theorem states that the central element
of the Lorentz spin group acts on the Hilbert space of the theory as p´1qF , where F is the Z{2Zvalued grading operator;45 see [SW, GJ, Kaz] for proofs in the framework of Wightman quantum
field theory. In this section we prove the analog for reflection positive non-extended invertible
topological theories. We do not know a version for fully extended theories. See [J-F] for another
account of spin-statistics in topological field theory, but without positivity. A topological version
of spin-statistics also enters into [GK] in the context of fermionic lattice models.
To formulate the statement we Wick rotate the central element of the Lorentz spin group to
the central element of the Euclidean spin group. On a curved Riemannian spin manifold M , it
acts as the spin flip: the identity diffeomorphism of M covered by the action of ´1 on the spin
frames. For a general symmetry group Hn it is the action of the distinguished central element k0 P
K in the internal symmetry group; see Corollary 2.12. Let sVectC be the symmetric monoidal
category of super vector spaces; the symmetry incorporates the Koszul sign rule. Recall the notation
(Remark 2.39) for the domain of a not necessarily topological field theory.
Definition 11.1. Let F : Bord∇
xn´1,ny pHn q Ñ sVectC be a field theory. We say F satisfies spinstatistics if it maps the spin flip on every pn ´ 1q-manifold Y to the exponentiated grading operator p´1qF on the super vector space F pY q.
Example 11.2. The spin-statistics connection fails without reflection positivity. Consider a 1dimensional invertible topological theory F of spin manifolds with values in the category of Z{2Zgraded complex lines. There are 4 theories up to isomorphism:46 F ppt` q is either even or odd, the
spin flip acts as either `1 or ´1, and these choices are independent. Half of these theories satisfy
1
spin statistics, and they are precisely the ones for which F pSbounding
q “ `1, which by Theorem 7.22
is the condition for stability, and so for reflection positivity.
45F vanishes on bosonic states and is the identity on fermionic states. In a free theory there is a dense Fock space
of states with a finite number of particles on which F counts the number of fermionic particles modulo two. In any
theory p´1qF is the grading operator on the Z{2Z-graded Hilbert space of states.
46We compute using Theorem 5.23: rΣ1 M T Spin , Σ1 ICˆ s – Hompπ Σ1 M T Spin , Cˆ q, the Thom spec1
1
1
8
trum Σ1 M T Spin1 is the suspension spectrum of RP8
` , and π1 RP` – Z{2Z ˆ Z{2Z. By contrast, π1 M T Spin – Z{2Z,
hence rM T Spin, Σ1 ICˆ s – Z{2Z, and so by Theorem 1.1 there are only two reflection positive theories.

<!-- page 106 -->
106

D. S. FREED AND M. J. HOPKINS

Theorem 11.3. Let F : Bordxn´1,ny pHn q Ñ sLineC be a reflection positive invertible topological
field theory. Then F satisfies spin-statistics.

Figure 6. The composition eY ˝ τ ˝ cY

Proof. We first treat the case Hn “ Spinn . Let Y be a closed Hn -manifold and set L “ F pY q.
Recall from §4.2 and Definition B.8 the coevaluation cY : Hn´1 Ñ Y > Y _ and the evaluation
eY : Y _ >Y Ñ Hn´1 . Let τ : Y >Y _ Ñ Y _ >Y be the symmetry map. The composition eY ˝τ ˝cY is
1
ˆY (see Figure 6), and under F it maps to the composition C Ñ LbL˚ Ñ L˚ bL Ñ C.
Snonbounding
The Koszul sign rule in the symmetry gives
#
(11.4)

1
ˆ Y q “ trs idL “ trp´1qF “
F pSnonbounding

`1,
´1,

L even,
L odd,

where trs is the supertrace. The nonbounding circle is obtained by cutting the bounding circle at
two points and regluing using the spin flip diffeomorphism of one of the points and the identity of
the other. In other words, it is a triple composition of coevaluation, the indicated diffeomorphism,
and evaluation. Take Cartesian product with Y and apply F to conclude that the ratio of (11.4)
1
with F pSbounding
ˆ Y q is the supertrace of the spin flip on Y , and since the spin flip has order two
1
this ratio equals ˘1. But Sbounding
ˆ Y is the spin double of cY (see Example 4.31), so by reflection
1
positivity we conclude from Proposition 4.26 that F pSbounding
ˆ Y q “ 1, hence the spin flip acts
F
as p´1q .
In the general case we use Corollary 2.12 to construct an Hk`` -structure on the Cartesian product
of a Spink -manifold and an H` -manifold. Then the argument in the preceding paragraph goes
through for Y an Hn´1 -manifold and the same spin circles.


Appendix A. The CRT theorem for general symmetry types
In §A.3 we take as our starting point a relativistic quantum field theory in Minkowski spacetime. Positivity of energy gives analytic correlation functions for which the Minkowski correlation

<!-- page 107 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

107

functions are boundary values; Euclidean correlation functions are the restriction to a suitable subdomain. This leads to the CRT theorem (Theorem A.23),47 and we outline Jost’s proof [J], extended
to general symmetry types. Recall that the symmetry group H1,n´1 of a relativistic quantum field
theory acts by time-orientation preserving transformations; see (2.1). The CRT theorem asserts
that a larger symmetry group, including time-orientation reversing transformations, also acts; the
time-reversing elements act antilinearly. There is a subtlety in the Lorentz spin central extensions,
flagged in [GT],48 which we elucidate and generalize to arbitrary symmetry types in §A.2. This
subtlety is present even in the spin case without time-reversal symmetry. It implies, for example,
that the ten Lorentz signature symmetry groups for free fermion theories (§9) embed in Clifford
algebras, a fact which is implicit in §9.2.4. In this appendix we work in the framework of Wightman
quantum field theory. One consequence of our discussion (Remark A.42) is a justification of the
correspondence between the alternatives
(A.1)

pin` -structure

vs.

pin´ -structure

in Wick-rotated field theory and the alternatives
(A.2)

T 2 “ p´1qF

vs.

T2 “ 1

for the action of time-reversal T on the Hilbert space H of states. We begin in §A.1 with a review
of pin groups and pin manifolds, which also serves to fix some conventions about Clifford algebras..
We assume the dimension of spacetime is n ě 3.
A.1. Pin groups and pin manifolds
References for this section include [ABS, BDGK, KT1]. While we assume the dimension n ě 3,
with minor modifications the discussion goes through for n “ 1, 2 as well.
A.1.1. Pin groups and Clifford algebras. We take Lorentz signature as our starting point. Let
R1,n´1 be the standard vector space with basis e0 , e1 , . . . , en´1 and the standard inner product:
xe0 , e0 y “ 1, xei , ei y “ ´1, i “ 1, . . . , n ´ 1, and xeµ , eν y “ 0, µ ­“ ν. Its isometry group
is the orthogonal group O1,n´1 . The group of components of O1,n´1 is isomorphic to t˘1u ˆ
t˘1u; an orthogonal transformation either preserves or exchanges the two components of timelike
vectors ξ (vectors with xξ, ξy ą 0), and it either preserves or reverses the orientation of any spacelike
α
q P O1,n´1 the first question is the sign
codimension 1 subspace. In terms of the block matrix p ηa A
of the real number a and the second the determinant of the pn ´ 1q ˆ pn ´ 1q matrix A. The identity
component of O1,n´1 has a unique (up to isomorphism) connected double covering group Spin1,n´1 .
47It is usually called the CPT theorem, but we follow the nomenclature in [W1], which is more appropriate for
arbitrary dimensions: the ‘P’ in ‘CPT’ is understood to be the parity transformation that acts as ´1 on space and
so is orientation-preserving if the dimension of spacetime is odd; by contrast, the ‘R’ in ‘CRT’ denotes reflection in a
single spatial direction and is orientation-reversing in all dimensions. The ‘C’ is best read as ‘complex conjugation’.
48The setting of [GT] is “formal field theory” as opposed to that in the Wightman axioms.

<!-- page 108 -->
108

D. S. FREED AND M. J. HOPKINS

It is contained in the even subalgebra of a real Clifford algebra, and there are two equally good
choices for the signs:

(A.3)

Cliff 1,n´1 :

e20 “ `1,

e2i “ ´1,

i “ 1, . . . , n ´ 1,

Cliff n´1,1 :

e20 “ ´1,

e2i “ `1,

i “ 1, . . . , n ´ 1.

The Lorentz orthogonal group O1,n´1 has a complexification On pCq consisting of complex nˆn orthogonal matrices. This complex group has two components distinguished by the determinant,
which is ˘1. The identity component SOn pCq has a subgroup that is the union of the two components of O1,n´1 of matrices with determinant 1. Also, SOn pCq has a unique connected double
covering group Spinn pCq, which contains Spin1,n´1 as a subgroup. The complex Lie group On pCq
deformation retracts onto its maximal compact subgroup On , which is the group of orthogonal
symmetries of the real vector space spanned by
(A.4)

f0 “ i e0 , f1 “ e1 , . . . , fn´1 “ en´1

with its inherited negative definite inner product. Here i is a choice of complex number with i2 “ ´1.
The identity component SOn has a unique connected double covering group Spinn , which is the
maximal compact subgroup of Spinn pCq. It is contained in the even subalgebra of a real Clifford
algebra, and again there are two equally good choices for the signs:

(A.5)

Cliff ´n : fµ2 “ ´1,

µ “ 0, . . . , n ´ 1,

Cliff `n : fµ2 “ `1,

µ “ 0, . . . , n ´ 1.

The four-component orthogonal group O1,n´1 has many double cover groups with identity component Spin1,n´1 ; we discuss two of them in §A.2. In the remainder of this subsection we focus
on the two-component compact orthogonal group On , which has two double covers Pin˘
n with
identity component Spinn . Each is a subgroup of invertible elements in a real Clifford algebra:
Pin˘
n Ă Cliff ˘n . They are group extensions
(A.6)

1 ÝÑ t˘1u ÝÑ Pin˘
n ÝÑ On ÝÑ 1

´
Observe that Pin`
1 – Z{2Z ˆ Z{2Z and Pin1 – Z{4Z.

A.1.2. Pin manifolds. A Riemannian manifold X has a principal On -bundle of frames BO pXq Ñ X
whose points represent orthonormal bases of the tangent spaces to X. The following is a special
case of Definition 2.29.
Definition A.7. A pin˘ -structure on X is a pair pP, θq consisting of a principal Pin˘
n -bundle
θ
P Ñ X and an isomorphism BO pXq ÝÑ P {t˘1u of principal On -bundles.

<!-- page 109 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

109

Pin structures, as spin structures, do not necessarily exist. The obstructions are given by StiefelWhitney classes: a pin` -structure exists on X if and only if49 w2 pXq “ 0 and a pin´ -structure exists
if and only if pw12 ` w2 qpXq “ 0. Double covers of X act on pin structures as follows. If Q Ñ X is a
double cover, viewed as a principal t˘1u-bundle, and pP, θq is a pin˘ -structure, then Q ˆX P Ñ X
˘
is a principal pt˘1u ˆ Pin˘
n q-bundle. The Pinn -bundle pQ ˆX P q { t˘1u Ñ X associated to the
˘
˘
homomorphism t˘1u ˆ Pinn Ñ Pinn (multiplication in Pin˘
n with first argument restricted to the
central subgroup in (A.6)), along with a canonical isomorphism of underlying On -bundles obtained
from θ, is a pin˘ -structure. The set of isomorphism classes of pin˘ -structures, if nonempty, is a
torsor over the abelian group H 1 pX; Z{2Zq; that is, this group acts freely and transitively on the
set of isomorphism classes. There is a canonical double cover of X, the orientation double cover,
whose points represent orientations of the tangent spaces to X.
Definition A.8. The w1 -involution is the action of the orientation double cover on pin structures.
Recall that the equivalence class of the orientation double cover is w1 pXq P H 1 pX; Z{2Zq.
Remark A.9. Let α̂ be the automorphism of Pin˘
n that is the identity on Spinn and multiplication
by the central element ´1 on the complement; it covers the identity automorphism of On . An
alternative description of the w1 -transform pP „ , θq of a pin-structure pP, θq is the same manifold P
with the same map θ, but with the Pin˘
n -action altered by precomposition with α̂. (To see this,
write the orientation double cover as P { Spinn and construct the isomorphism of Pin˘
n -bundles
(A.10)

P { Spinn ˆP ÝÑ P „

which maps po, pq ÞÑ p if p P o and po, pq ÞÑ p ¨ p´1q if p R o. Here o Ă P is a Spinn -orbit.)
A.2. Lorentz signature symmetry groups
This section is an exposition and elaboration of ideas in [GT]. We continue with the hypothesis n ě 3, largely for convenience of exposition; with minor modifications the discussion goes
through for n “ 1, 2 as well.
A.2.1. Complex pin groups. The complex orthogonal group On pCq has two components. The
identity component SOn pCq Ă On pCq has a unique isomorphism class of nontrivial double cover
groups, any representative of which is called Spinn pCq.
Proposition A.11. There are unique complex Lie groups Pin˘
n pCq with identity component Spinn pCq,
˘
which double cover On pCq, and which contain Pinn as maximal compact subgroups. Furthermore,
any complex Lie group that double covers On pCq and has identity component isomorphic to Spinn pCq
´
is isomorphic to either Pin`
n pCq or Pinn pCq.
c
Remark A.12. We warn that Pin˘
n pCq are complex Lie groups, whereas the group ‘Pinn ’, which is
defined in [ABS, §3] as a subgroup of the complex Clifford algebra, is a compact real Lie group; it
and twisted variants appear in §9.
49These are Stiefel-Whitney classes of the tangent bundle: w pXq “ w pT Xq. There is a potential confusion with
q

q

Stiefel-Whitney classes of the stable normal bundle, which is what appears naturally in bordism theory.

<!-- page 110 -->
110

D. S. FREED AND M. J. HOPKINS

Proof. Up to isomorphism there is a unique double covering space X Ñ On pCq whose inverse image
over each component of On pCq is connected. The restriction over On Ă On pCq is isomorphic as
a double covering space to Pin˘
n Ñ On . Choose an isomorphism of double covers and transport
the group structure, then extend the group structure on the identity component Spinn to that
of Spinn pCq on the entire component X` Ă X containing Spinn . Now use covering space theory to
extend the group structure to all of X. For example, setting X´ “ XzX` , lift the map X` ˆ X´ Ñ
On pCq´ to a map X` ˆX´ Ñ X´ using basepoints in the compact pin group. In fact, the extension
of the group structure is determined by the square of a lift of a single hyperplane reflection, for
which there are two choices, and this implies the last assertion.

A.2.2. Double covers of Lorentz isometry groups. The two-component group SO1,n´1 Ă O1,n´1
consists of isometries that preserve the overall orientation of R1,n´1 . Let µm Ă Cˆ be the group of
mth roots of unity. Using the diagram
Spinn pCq 
(A.13)



/ Spin pCq ˆµ µ4
2
n

π2

"

y

π4

SOn pCq
´1
Ăα
Ăβ
set SO
1,n´1 “ π2 pSO1,n´1 q, and let SO1,n´1 Ă Spinn pCq ˆµ2 µ4 be the union of Spin1,n´1 and
Ó
Ó
Ó
the complement of π2´1 pSO1,n´1
q in π4´1 pSO1,n´1
q, where SO1,n´1
is the non-identity component
α
α
Ă
Ă
of SO1,n´1 . For the pin groups let O
and O
be the inverse image of O1,n´1 Ă On pCq
n´1,1

1,n´1

´
under the double cover homomorphisms Pin`
n pCq Ñ On pCq and Pinn pCq Ñ On pCq, respectively.
Finally, using the diagram


Pin˘
n pCq

(A.14)

π2



/ Pin˘ pCq ˆµ µ4
2
n
!

z

π4

On pCq
Ò
Ó
Ó
´1
´1
´1
Ăβ
Ăβ
let O
n´1,1 and O 1,n´1 be the union of π2 pO1,n´1 q and the complement of π2 pO1,n´1 q in π4 pO1,n´1 q,
Ó
Ò
where we use the ` and ´ pin groups, respectively. Here O1,n´1
is the complement of O1,n´1
Ă
O1,n´1 , the components of time-reversing linear isometries.

Proposition A.15.
(1 ) Every double cover group of SO1,n´1 whose identity component is isomorphic to Spin1,n´1 is
Ăα
Ăβ
isomorphic to either SO
or SO
.

1,n´1
1,n´1
β
Ă
(2 ) The double cover group SO1,n´1 of SO1,n´1 is a subgroup of the even subalgebras of Cliff n´1,1

and Cliff 1,n´1 .
Ăβ
Ăβ
(3 ) The double cover groups O
n´1,1 and O 1,n´1 of O1,n´1 are subgroups of Cliff n´1,1 and Cliff 1,n´1 ,
respectively.

<!-- page 111 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

111

Summary: the α-double covers are subgroups of complex (s)pin groups; the β-double covers are
subgroups of Lorentz signature Clifford algebras.
Ó
Proof. For (1), let g P SO1,n´1
be the diagonal matrix diagp´1, ´1, `1, . . . , `1q. Then the square
of a lift of g to a double cover of SO1,n´1 has square the identity `1 or the central element ´1
of Spin1,n´1 . By covering space theory, as in the proof of Proposition A.11, we can deduce that
this dichotomy determines the group structure on the double cover.
The element e0 e1 in the Clifford algebra (of either signature pn´1, 1q or p1, n´1q) acts on R1,n´1
as g and squares to `1. On the other hand, g lies in SO1,n´1 X SOn Ă SOn pCq, so a lift of g
to Spinn pCq lies in the compact spin group Spinn where it squares to ´1, as we compute in the
Clifford algebra Cliff ˘n . This is the essential point in the proof of (2).
As for (3) there are double covers Pinn´1,1 Ă Cliff n´1,1 and Pin1,n´1 Ă Cliff 1,n´1 of O1,n´1 , as
Ăβ
defined in [ABS], [LM, §1.2]. By (2) the restriction over SO1,n´1 is isomorphic to SO
. The
1,n´1

Ó
lifts to e0 in the Clifford algebra, and its square is given
element diagp´1, `1, . . . , `1q P O1,n´1
in (A.3). Arguing as above with the compact pin groups we deduce that this is opposite the square
of a lift in the corresponding complex pin group. This is the new step in proving the isomorphisms
β

Ă
Pinn´1,1 – O
n´1,1

(A.16)



Ăβ
Pin1,n´1 – O
1,n´1

A.2.3. General Lorentz signature symmetry groups. There are analogs of the α and β-extensions
of the Lorentz signature vector symmetry group H1,n´1 for an arbitrary symmetry type, which
as in §2.1 is the quotient of the full symmetry group of a relativistic quantum field theory by
Ò
. We use the Structure
translations. It comes equipped with a homomorphism ρn : H1,n´1 Ñ O1,n´1
α{β

Theorem 2.7, and in particular (2.8), (2.10), and (2.11) to define the α and β-extensions H1,n´1
of H1,n´1 simultaneously. Set
α{β
Ă α{β ˆ K
SH1,n´1 – SO
1,n´1

(A.17)

L

xp´1, k0 qy.

α{β
α{β
Ò
r α{β by pullback
, set H1,n´1 “ SH1,n´1 . If ρn is surjective, define H
If the image of ρn is SO1,n´1
1,n´1

1

/K

r α{β
/H

1,n´1

Ă
/O

α{β
n´1,1

/1

1

/K


/J


/ t˘1u

/1

(A.18)

where the right vertical map is the determinant homomorphism. Then let
α{β
r α{β
H1,n´1 – H
1,n´1

(A.19)

L

xp´1, k0 qy.

α
We observe that H1,n´1
is a real subgroup of the complex Lie group Hn pCq, the inverse image
of O1,n´1 under the homomorphism ρn : Hn pCq Ñ On pCq in (2.2). Also, our notation is set up so
α{β
Ă α{β .
that Spin
– SO
1,n´1

1,n´1

<!-- page 112 -->
112

D. S. FREED AND M. J. HOPKINS

A.2.4. Extensions of real representations. As just remarked, the α-extension sits as a subgroup of
the complex symmetry group. One key feature of the β-extension is the following.
Proposition A.20. Let R “ R0 ‘ R1 be a Z{2Z-graded real representation of H1,n´1 such that
k0 P K Ă H1,n´1 acts as the grading operator. Let RC :“ R bR C denote the complexification, which
α
carries an action of the complex Lie group Hn pCq, hence of the subgroup H1,n´1
.
?
α
0
0
1
1
(1 ) If h P H1,n´1 zH1,n´1 , then hpR q “ R and hpR q “ ´1R .
β
(2 ) There is a canonical extension of the action of H1,n´1 on R to an action of H1,n´1
.

All Lie groups that appear are ungraded, so act by even transformations of R. The conclusion is
that the β-extension acts on real representations of H1,n´1 .
α
Proof. For (1) it suffices to check for a single element h P H1,n´1
zH1,n´1 . By Corollary 2.12,
α
anti-Wick rotated to Lorentz signature, we choose h to be the image in H1,n´1
of a lift of

ˆ
(A.21)

´1 0
0 ´1

˙
P SO1,1 X SO2 Ă SO2 pCq Ă SOn pCq

to Spinn pCq. In the compact spin group Spin2 Ă Spin2 pCq the element h is represented as f0 f1
and is connected to the identity by the curve cos t{2 ` sin t{2 f0 f1 , 0 ď t ď π, where we embed
Spin2 Ă Cliff ´2 ; see (A.5). Complex conjugation, defined so that Spin1,1 Ă Spin2 pCq is real, takes
this curve to the curve cos t{2 ´ sin t{2 f0 f1 , 0 ď t ď π in Spin2 Ă Spin2 pCq. In particular, the
complex conjugate of f0 f1 is ´f0 f1 . Since ´1 maps to k0 and acts as the grading operator, f0 f1 is
0 and a purely imaginary operator on R1 . This proves (1).
a real operator on RC
C
Consider the diagram
α

H1,n´1

(A.22)



π2

/ Hα

1,n´1 ˆµ2 µ4

!

z

π4

O1,n´1
α
β
α
in which µ2 Ă H1,n´1
is generated by k0 . Then H1,n´1
Ă H1,n´1
ˆµ2 µ4 is the union of H1,n´1 and
Ó
Ó
1 via scalar multiplication and
the complement of π2´1 pO1,n´1
q in π4´1 pO1,n´1
q. Let µ4 Ă Cˆ act on RC
α
0 trivially. Then by (1) the restriction to H β
on RC
1,n´1 Ă H1,n´1 ˆµ2 µ4 is real, i.e., preserves R Ă RC .
This proves (2).


A.3. Wick rotation and the CRT theorem
In this section we sketch a rigorous argument for the CRT theorem in relativistic quantum
field theory. We use the analytic continuation of correlation functions, working in the framework
of Wightman quantum field theory [SW, GJ, Kaz]. Our purpose is to treat general symmetry
types. Even for theories with Lorentz symmetry group H1,n´1 “ Spin1,n´1 there is a subtlety:
Ăβ
Ăα
the group SO
acts on the holomorphic correlation functions, whereas the group SO
acts
1,n´1

1,n´1

on the Minkowski spacetime correlation functions. (See §A.2.2 for the definitions of these Lie

<!-- page 113 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

113

groups.) This argument also demonstrates why only the “Cliffordian” [BDGK] Lorentz signature
pin groups Pinn´1,1 and Pin1,n´1 can be symmetries of a relativistic quantum field theory instead
of more general possible double covers of O1,n´1 ; see Remark A.42. We assume n ě 3.
Recall from §2.1 that Minkowski spacetime M n is an n-dimensional affine space whose vector
space V “ R1,n´1 of translations is equipped with an inner product of signature p1, n ´ 1q and
a choice of component V` of the space tξ : xξ, ξy ą 0u of timelike vectors.50 To Wick rotate
to imaginary time, fix an orthogonal splitting V “ U ‘ U K with U a 1-dimensional timelike
?
subspace. Then the Euclidean translation group is VE “ ´1 U ‘ U K and the corresponding
Euclidean space is E “ M ˆV VE , an affine space over VE . Complexified Minkowski spacetime
is MC “ M ˆV VC , where VC is the complexification of V . The symmetry group H1,n´1 of a
relativistic quantum field theory acts on M n by time-orientation preserving transformations via a
Ò
homomorphism ρn : H1,n´1 Ñ O1,n´1
, as in (2.1).
Theorem A.23 (CRT Theorem). Let Q denote a relativistic quantum field theory with symmetry
β
β
group H1,n´1 . Then the symmetry extends to H1,n´1
; elements of H1,n´1
zH1,n´1 act antilinearly.
Here Q is a quantum field theory in the Wightman axiomatic framework. It is determined by its
correlation functions, called Wightman functions; see [Kaz, §1.3]. For simplicity of notation we
only discuss 2-point functions in this account. A precise version of Theorem A.23 is (A.41) below.
The fields in Q are defined by a finite dimensional Z{2Z-graded real representation
(A.24)

σ : H1,n´1 ÝÑ AutpRq.

We write R “ R0 ‘ R1 according to the grading; elements of H1,n´1 preserve the grading. The
spin-statistics theorem, which we assume in this account, asserts that the special element k0 P K Ă
H1,n´1 defined in Theorem 2.7(2) acts as the grading operator on R. Write RC “ R bR C for the
complexification. Classical fields are functions M n Ñ R. Quantum fields are R-valued operatorvalued distributions Φ “ Φ0 ` Φ1 on M n . The 2-point “function” is a complex distribution whose
value on Schwartz functions fi : M n Ñ R˚ is written
ż
(A.25)
xΦpf1 qΦpf2 qy “
dp1 dp2 f1 pp1 qf2 pp2 q xΦpp1 qΦpp2 qy,
M2
b2
where xΦpp1 qΦpp2 qy denotes the kernel of the RC
-valued distribution on M ˆ2 . The theory Q has a
0
1
Z{2Z-graded Hilbert space H “ H ‘ H of states, constructed from the correlation functions, and
a distinguished vacuum vector Ω P H0 . The field operators Φpf q act as unbounded operators on H,
and the 2-point function is the vacuum expectation value of the product of the field operators:

(A.26)

xΦpf1 qΦpf2 qy “ xΩ , Φpf1 qΦpf2 qΩyH .

There is a unitary representation of the affine extension of H1,n´1 on H—all symmetries preserve
the Z{2Z-grading. The vacuum vector and 2-point function are invariant under that action, in
b2
particular under translations. Hence there is an RC
-valued distribution on V with kernel
(A.27)

W pξq :“ xΦppqΦpp ` ξqy,

p P M n,

ξ P V,

50The latter choice is required in order to formulate the positivity of energy.

<!-- page 114 -->
114

D. S. FREED AND M. J. HOPKINS

which is independent of p.
The important step in Jost’s proof is the construction of holomorphic correlation functions from
which the Wightman functions are recovered as boundary values [Kaz, §2.1]. This is a consequence
of the positivity of energy and geometric arguments. The holomorphic 2-point function
b2
WC : D ÝÑ RC

(A.28)

has domain D Ă VC that is connected and Hn pCq-invariant. Define the backward tube T “ V ´iV` Ă
VC , where i is a choice of square root of ´1. Then51
D “ SOn pCqpTq Y ´SOn pCqpTq.

(A.29)

An important feature of D is that it contains Jost points,52 which in this case of 2-point functions
are the real spacelike vectors ξ P V Ă VC that satisfy xξ, ξy ą 0. From (A.29) we see T Ă D, and
as stated W is a boundary value of WC :
(A.30)

W pξq “ lim WC pξ ´ iηq,

ξ P V,

Ñ0`

η P V` ,

and the limit is independent of η. We also have VE zt0u Ă D, and the Wick-rotated Euclidean
2-point function is the restriction of WC to VE zt0u.
We collect some properties of the holomorphic correlation functions. First, since the inner
product on H is even, it follows that
WC “ WC0 ` WC1

(A.31)

q b2
where WCq takes values in pRC
q , q “ 0, 1. Note that both WC0 and WC1 are even. Next, as already
α
stated, WC is Hn pCq-invariant, hence invariant under the subgroup H1,n´1
Ă Hn pCq:

`
˘
WC pζq “ σphα qb2 WC ρn phα qζ ,

(A.32)

α
hα P H1,n´1
,

ζ P D.

Now if ξ is real and spacelike, then since field operators at spacelike separated points commute (in
the graded sense), and since real spacelike (Jost) points are in the domain D, we have
WC0 p´ξq “

(A.33)

WC0 pξq

WC1 p´ξq “ ´WC1 pξq

Continuing with ξ real and spacelike, we claim
WC0 pξq “

(A.34)

WC0 pξq

WC1 pξq “ ´WC1 pξq

51Note SO

n pCqpTq “ On pCqpTq.

52Here we use n ě 3.

<!-- page 115 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

115

Since such ξ lie in D, and D is connected, we deduce a Schwarz reflection formula valid for all ζ P D:
(A.35)

WC0 pζq “

WC0 pζq

WC1 pζq “ ´WC1 pζq

The manipulation that justifies (A.34) is, for any p P M n and ξ P V ,
(A.36)

WC pξq “ xΦppqΦpp ` ξqΩ , Ωy “ xΩ , Φpp ` ξqΦppqΩy “ WC p´ξq;

then we apply (A.33). The middle step is straightforward in the even case: Φ0 pqq is self-adjoint for
q real. The corresponding manipulation in the odd case uses the adjoint of the odd operator Φ1 pqq,
which involves a tricky sign53 as we explain in the following remark.
Remark A.37. The usual physics conventions are: the norm square of an odd vector in H is real and
positive; for any two operators A, B we have pABq˚ “ B ˚ A˚ —there is no sign even if both A and
B are odd; and the odd field operator Φ1 pqq is self-adjoint in the usual sense. However, the Koszul
sign rule demands that the first two of these be modified to: the norm square of an odd vector in H
is purely imaginary and lies on one of the two rays of nonzero purely imaginary numbers, the choice
of which is a convention (Example 6.49); if A, B are operators that have definite parities |A|, |B|,
then [DM, §4.4]
(A.38)

pABq˚ “ p´1q|A||B| B ˚ A˚ .

If we use these conventions, then the odd field operator Φ1 pqq is not self-adjoint, but rather
(A.39)

Φ1 pqq˚ “ i Φ1 pqq

One justification for (A.39) is to consider the ˚-structure on the complex operator algebra, and to
note that (A.38) implies that the square of an odd self-adjoint operator is even skew-adjoint, and
so if Φ1 pqq were self-adjoint we would contradict expectations for the quantization of real fields. We
remark that the factor i in (A.39) already occurs in quantum mechanics; see [FM1, (4.10)]. The
middle step in (A.36) is valid with either the standard physics conventions or the Koszul-compatible
notion of adjointness supplemented with (A.39).
α
Proof of Theorem A.23. Fix hα P H1,n´1
zH1,n´1 . Then hα reverses the time orientation, in other
words, H α pV` q “ ´V` . Hence for ξ P V we use (A.30), (A.32), and (A.35) to deduce that for ξ P V
and q “ 0, 1 we have

(A.40)

W q pξq “ lim WCq pξ ´ iηq
Ñ0`
`
˘
“ lim σphα qb2 WCq ρn phα qξ ´ iρn phα qη
Ñ0`
`
˘
“ lim p´1qq σphα qb2 WC ρn phα qξ ` iρn phα qη
Ñ0`
`
˘
“ p´1qq σphα qb2 W ρn phα qξ .

53We thank Greg Moore for help straightening this out.

<!-- page 116 -->
116

D. S. FREED AND M. J. HOPKINS

To pass to the third equation we use the fact that σphα q is real on even vectors (Proposition A.20(1)).
The construction that proves Proposition A.20(2) combines with (A.40) to yield
(A.41)

`
˘
W q pξq “ σphβ qb2 W ρn phβ qξ ,

β
hβ P H1,n´1
zH1,n´1 ,

ξ P V.

This is the precise statement that the Minkowski spacetime 2-point function is antilinear-invariant
β
under elements of H1,n´1
zH1,n´1 .

Remark A.42. If Q is a relativistic quantum field theory with fermionic states and time-reversal
Ò
symmetry, and no other internal symmetries, then H1,n´1 is a double cover of SO1,n´1
whose
identity component is isomorphic to Spin1,n´1 . The complex Lie group Hn pCq is then a double
cover of On pCq whose identity component is isomorphic to Spinn pCq. Proposition A.11 implies
´
that Hn pCq is isomorphic to Pin`
n pCq or Pinn pCq. The construction with (A.14) and (A.16) tells
β
is Pinn´1,1 and Pin1,n´1 , respectively. Recalling the sign convention (A.3)
that the group H1,n´1
for Clifford algebras, this proves the correspondence between (A.1) and (A.2) and also limits the
possible symmetry groups on relativistic quantum field theories to the Cliffordian pin groups.

Appendix B. Involutions on categories and duality
Definition B.1. Let C be a category.
(1) An involution of C is a pair pτ, ηq of a functor τ : C Ñ C and a natural isomorphism η : idC Ñ τ 2
such that for any x P C we have τ ηx “ ητ x as morphisms τ x Ñ τ 3 x.
θ
(2) A fixed point of τ is a pair px, θq of an object x P C and an isomorphism x ÝÑ τ x such that
τ θ ˝ θ “ ηx as morphisms x Ñ τ 2 x.
If C is a symmetric monoidal category, then the involution τ is required to be a symmetric monoidal
–
functor: for x, y P C there is given an isomorphism τ x b τ y ÝÝÑ τ px b yq and these isomorphisms
are compatible with the symmetry and with η.
Example B.2. Let C “ VectC be the category of complex vector spaces and linear maps. Define
τ : C Ñ C to be the functor that takes complex vector spaces and linear maps to their complex
conjugates. (The complex conjugate vector space is the same underlying real vector space with the
?
sign of multiplication by ´1 P C reversed; the complex conjugate of a linear map is the same map
of sets.) Then there is a canonical identification of τ 2 with idC . A fixed point is a complex vector
space with a real structure. As a variation, if C “ sVectC is the category of super (Z{2Z-graded)
vector spaces and τ complex conjugation as above, but now η is composed with the exponentiated
grading automorphism (denoted ‘p´1qF ’ in the physics literature), then a fixed point is a super
vector space with a real structure on its even part and a quaternionic structure on its odd part. If
we restrict to the subgroupoid Cˆ of super lines and isomorphisms, then all fixed points are even.
Definition B.3. Let pτ, ηq be an involution on a category C. The fixed point category Cτ has as
f

objects fixed points px, θq, and a morphism px, θq Ñ px1 , θ1 q in Cτ is a morphism px Ý
Ñ x1 q P C such

<!-- page 117 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

117

that the diagram
f

x
(B.4)

/ x1

θ



τx

τf



θ1

/ τ x1

commutes. There is a forgetful functor Cτ Ñ C that maps px, θq ÞÑ x.
Example B.5. Let C be the groupoid of Zp1q-torsors:54 an object T is a set with a simply transitive
action of the additive group Zp1q and a morphism T Ñ T 1 is an isomorphism that commutes with
the Zp1q-actions. Let τ be the involution that sends a torsor T to its dual HomZp1q pT, Zp1qq and
sends a morphism to its inverse transpose. The dual of T may be identified with T as a set; the
dual Zp1q action by ζ P Zp1q is the original action by ζ̄. The fixed point category Cτ is equivalent to
the set Z{2Z: there are two isomorphism classes of objects and no nontrivial automorphisms. The
first, which we call ‘Type P’, is the torsor Zp1q with complex conjugation θ as a map to the dual
?
torsor. The second, which we call ‘Type N’, is the torsor π ´1 ` Zp1q with complex conjugation θ.
Observe that in the Type P case the involution θ has a fixed point whereas in the Type N case it
does not. Also, Zp1q-torsors form a Picard groupoid, as do torsors for any abelian group, and the
fixed point category is a Picard groupoid as well. The Type P torsor is the tensor unit; the square of
a Type N torsor has Type P. The names derive from the family exp : C Ñ Cˆ of Zp1q-torsors with
complex conjugation acting. There are two components Rą0 and Ră0 of fixed points in the base.
The fiber of exp has Type P over positive real numbers and Type N over negative real numbers;
the representatives described above are exp´1 p`1q and exp´1 p´1q, respectively.
Definition B.6. Let B, C be categories with involutions and F : B Ñ C a functor. Then equivari–
ance data for F is an isomorphism φ : F τB ÝÝÑ τC F of functors B Ñ C such that for every object
x P B the diagram
Fx
(B.7)

F ηB

ηC

/ F τ2x
B

$

φ2



τC2 F x

commutes.
There are additional compatibilities for a symmetric monoidal functor between symmetric monoidal
categories; we do not spell them out. We often loosely say that “F is an equivariant functor”, but
it is important to remember that equivariance is data+condition, not simply a condition.
Next, we review duality in a symmetric monoidal category. Let C be a symmetric monoidal
category and x P C. Denote the tensor unit by 1 P C. (The tensor unit in Bordxn´1,ny pHn q is the
empty set as an pn ´ 1q-dimensional manifold; the tensor unit in VectC is the trivial 1-dimensional
vector space C.)
54Recall that Zp1q “ 2π

?

´1Z Ă C.

<!-- page 118 -->
118

D. S. FREED AND M. J. HOPKINS

Definition B.8. Let x be an object in a symmetric monoidal category C. Duality data for x is
a triple px_ , c, eq consisting of an object x_ P C together with morphisms c : 1 Ñ x b x_ and
e : x_ b x Ñ 1 such that the compositions
cbid

idbe

x ÝÝÝÝÑ x b x_ b x ÝÝÝÝÑ x

(B.9)

ebid

id bc

x_ ÝÝÝÝÑ x_ b x b x_ ÝÝÝÝÑ x_
f

are identity maps. If x0 ÝÑ x1 is a morphism, then the dual morphism is the composition
(B.10)

id bcx

id bf bid

ex bid

0
_
_
f _ : x_
ÝÝÝÝÝ
Ñ x_
ÝÝÝÝÝÝÑ x_
ÝÝ1ÝÝÝÑ x_
1 Ý
1 b x0 b x0 Ý
1 b x1 b x0 Ý
0

The morphism c is called coevaluation and e is called evaluation. We say that x_ is “the” dual to x
since any two triples of duality data are uniquely isomorphic. Assuming all objects have duals, we
can make choices of duality data for all objects at once and so obtain a duality involution δ on C,
but δ does not satisfy Definition B.1 since the direction of morphisms is reversed (B.10); in other
words, δ is a functor to the opposite category.
Definition B.11. Let C be a category.
(1) A twisted involution of C is a pair pδ, ηq of a functor δ : C Ñ Cop and a natural isomorphism
η : idC Ñ δ op ˝ δ such that for any x P C we have δηx ˝ ηδx “ idδx .
θ
(2) A fixed point of δ is a pair px, θq of an object x P C and an isomorphism x ÝÑ δx such that
δθ ˝ ηx “ θ as morphisms x Ñ δx.
Definition B.3 applies with a single change: the direction of the bottom arrow in (B.4) is reversed.
Example B.12. For C “ f VectC the category of finite dimensional complex vector spaces, the
duality involution δ : C Ñ Cop maps a vector space V to its dual V ˚ and a linear map f : V Ñ W
to f ˚ : W ˚ Ñ V ˚ . A fixed point of δ is a vector space V equipped with a nondegenerate symmetric
bilinear form; a linear map f : V Ñ W in Cδ preserves the bilinear forms. A fixed point for the
composite of duality and complex conjugation (Example B.2) is a complex vector space V with a
nondegenerate hermitian form; a linear map f : V Ñ W in the fixed point category is a partial
isometry—an injective map that preserves the hermitian forms.
Remark B.13. There is a higher categorical context for Definition B.11. Let Cat denote the 2category of categories. There is an involution α : Cat Ñ Cat that sends a category C to its
opposite Cop . (There is an extra categorical layer over Definition B.1: there is a triple pα, η1 , η2 q
of data and a single condition.) A twisted involution in the sense of Definition B.11 is fixed point
data for α.
Definition B.14. Let pτ, ηq be an involution on a symmetric monoidal category C. A hermitian
structure on an object x P C is an isomorphism h : τ x Ñ x_ such that the composition
(B.15)
is equal to h.

`
˘ τ ph_ q
`
˘
η ´1
τ x – τ px_ q_ ÝÝÝÝÝÑ τ pτ xq_ – τ 2 px_ q ÝÝÝÝÑ x_

<!-- page 119 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

119

Proposition 4.8 asserts that every object in a bordism category carries a hermitian structure. Observe that if F : B Ñ C is an equivariant symmetric monoidal functor between symmetric monoidal
categories with involution, as in Definition B.6, then the image of a hermitian structure on an
object b P B is a hermitian structure on F b.

Appendix C. Noncompact Wick-rotated vector symmetry groups
Let pHn , ρn q be a symmetry type, as in Definition 2.4.
Proposition C.1. Assume n ě 3.
(1 ) There exist a canonical noncompact Lie group H n , a homomorphism H n Ñ GLn R with kernel K, and an inclusion Hn ãÑ H n such that (i) Hn Ă H n is a maximal compact Lie subgroup,
(ii) the inclusion induces an isomorphism on π0 , and (iii) the diagram


Hn 
(C.2)

ρn



On 

/H

n


/ GLn R


commutes.
p n that fits into the diagram
(2 ) There exists a canonical Lie group H
1

/ Hn
_

(C.3)
1


/H

n

jn

p n
/H
_

p
/H

n

/ t˘1u

/1

/ t˘1u

/1

p n Ñ t˘1u ˆ GLn R that fits into
of group extensions, as well as a canonical homomorphism H
a pullback square
Hn

p
/H




/ t˘1u ˆ GLn R

(C.4)
GLn R

n

and a commutative cube built from (3.15) and (C.4).
These noncompact groups are used to define topological bordism categories (§2.2).
ρ

π

Proof. First define Spinn and Pin`
n as follows. Choose a lift P ÝÑ GLn R ÝÑ GLn R{On of the
homogeneous principal bundle π to a principal Pin`
n -bundle π ˝ ρ; it is unique up to isomorphism

<!-- page 120 -->
120

D. S. FREED AND M. J. HOPKINS

since GLn R{On is contractible. Define Pin`
n as the group of automorphism of ρ that cover the action
of left multiplication of GLn R “ On , and Spinn P Pin`
n the subgroup covering left multiplication
by GL`
R
“
SO
.
Then
set
n
n
(C.5)

SH n “ Spinn ˆ K

L

xp´1, k0 qy,

r n as the pullback
analogous to (2.8). If ρn pHn q “ SOn , set H n “ SH n . If ρn is surjective, define H
(see (2.10))
1

/K

r
/H

n

/ Pin`
n

/1

1

/K


/J


/ t˘1u

/1

L

xp´1, k0 qy.

(C.6)

and then
(C.7)

rn
Hn – H

It is straightforward to check the properties in (1).
`
For (2) imitate the proof of Proposition 3.13 with Spinn and Pin`
n replacing Spinn and Pinn ,
respectively.


Appendix D. Computations with A1 -modules
The computations described in §10 depend on knowledge of the mod 2 cohomology of the spectra
M T O|d|

0 ďd ď 3

M O|d|

´3 ďd ď 0

M SO3
as modules over the subalgebra A1 of the mod 2 Steenrod algebra generated by Sq1 and Sq2 . The
purpose of this appendix is to describe these computations and the methods for arriving at them.
We thank Meng Guo for her careful reading and astute corrections.
D.1. Cell diagrams
It is common practice to depict an A1 module M as a graph with nodes corresponding to a
chosen homogeneous basis for M , at a height corresponding to grading, and with an edge drawn
with a straight line between e and e1 if the coefficient of e1 in Sq1 peq is non-zero, and an edge drawn
with a curved line if they are analogously related by Sq2 . This works best when a basis can be
chosen so that the operations Sq1 and Sq2 send basis elements to basis elements. This is the case
with all of the A1 modules needed in this paper. Here are three examples:

<!-- page 121 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

121

For clarity the degrees of the basis elements have been indicated in this example, though we will
not usually do this. Topologists call these graphs “cell diagrams.” The one on the left is the free A1
module on one generator (of degree 0) and the one on the right is just Z{2 “ H ˚ pS 0 q, concentrated
in degree 0. The one in the middle right comes up frequently and was deemed the Joker by Adams.
It is the cohomology of a spectrum also called J.
As explained in §10 the mod 2 cohomology H ˚ M Spin was show by Anderson, Brown and Peterson [ABP1] to have the form
AbN
A1

for some A1 module N (which they determined). Figure 7 is a cell diagram of N through dimension 28. The modules to the right (in gray) are free, and the modules to the left (in black) are
either S or J.

Figure 7. The cell diagram for M Spin
How does one use this in practice? Suppose X is a connective spectrum of finite type and one
wishes to determine the localization at 2 of π˚ M Spin ^X. One makes three computations, (in
which the abutments, though not indicated, have been completed at 2)
˚
Exts,t
A1 pH X, Z{2q ñ πt´s ko ^X
˚
Exts,t
A1 pJ b H X, Z{2q ñ πt´s ko ^J ^ X “: MJ pXq
˚
Exts,t
A1 pA1 b H X, Z{2q “ H˚ X .

<!-- page 122 -->
122

D. S. FREED AND M. J. HOPKINS

The two spectral sequences often collapse (they do in the cases studied in this paper). Write
MS pXq “ π˚ ko ^X
MJ pXq “ π˚ ko ^J ^ X .
The result of Anderson-Brown-Peterson [ABP1] is that after localizing at 2, π˚ M Spin ^X is isomorphic to a sum of copies of MS pXq, MJ pXq and H˚ X, shifted according to the location of the
corresponding summands in the cell diagram of X:
π˚ M Spin ^X “ MS pXq ‘ Σ8 MS pXq ‘ Σ10 MJ pXq ‘ ¨ ¨ ¨ ‘ Σ20 H˚ X ‘ ¨ ¨ ¨ .
One further comment about the spectral sequences above. If M is a free A1 -module then
s,t
Exts,t
A1 pM, Z{2q “ ExtA1 pJ b M, Z{2q “ 0

są0

Ext0,t
A1 pM, Z{2q “ HomA1 pM, Z{2q
0,t
ExtA1 pJ b M, Z{2q “ HomA1 pJ b M, Z{2q
In these cases the display of the spectral sequences are all on the line s “ 0, and the spectral
sequences collapse.
More generally if M is of the form M 1 ‘ F with F a free A1 module, then
s,t
s,t
1
Exts,t
A1 pM, Z{2q « ExtA1 pM , Z{2q ‘ ExtA1 pF, Z{2q

and the spectral sequence is the sum of two spectral sequences, one of which collapses for trivial
reasons. The analogous statement holds for the second spectral sequence. For this reason it is
useful to omit free summands from the cell diagrams and keep track of them in some other way.
D.2. The charts
We can now explain in more detail what is shown in Figure 5. In each case we are interested in
π˚ M Spin ^X for some appropriate spectrum X. A cell diagram for X, modulo free A1 summands
˚
is shown on the left, with X labeled below it. The chart to the right depicts Exts,t
A1 pH pXq; Z{2q as
a module over Exts,t
A1 pZ{2, Z{2q. Following standard convention the horizontal axis is the pt´sq-axis
and the vertical axis is the s-axis. Each dot represents a basis element. The contributions from
the free summands contribute only to Ext0,t and to keep the picture uncluttered they are indicated
below the table. For example in the case s “ 3, in dimension pt ´ sq “ 8, there is a Z{2 not
indicated in graphical notation, but only by the `1. The group in that case is the sum of that Z{2
and Z{2 ‘ Z{8 ‘ Z{32.
The color coding allows one to read off the effect of the twisted Dirac operators of §9.2 as
described in homotopy theoretic terms in §10. Consider, for example, the case s “ 3. One needs
to know the effect of the map
π˚ M Spin ^S ´3 ^ M O3 Ñ S ´3 ^ KO.

<!-- page 123 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

123

The p´1q-connected cover of S ´3 ^ KO is equivalent to ko ^W , in which W is the finite spectrum
whose cell diagram is depicted below

The effect in cohomology of the twisted Dirac operator corresponds to the inclusion of the blue
cells, and the cokernel of this map, in the relevant summand, is displayed in green. The Ext charts
are correspondingly color coded and the red line indicates the connecting homomorphism in the
long exact sequence. The Ext computation of interest is built from the kernel and cokernel of this
connecting homomorphism. For example the connecting homomorphism is a monomorphism from
the column pt ´ sq “ 1 to the column pt ´ sq “ 0, and the only non-zero Ext group in this range is
0,0
ExtA
pH ˚ S ´3 M O3 , Z{2q “ Z{2.
1

In dimension 6, the group is the sum of pZ{2q2 (coming from the free summands) and another
Z{2 ‘ Z{2. The fact that the dot in filtration s “ 2 is blue indicates that the corresponding basis
element maps non trivially under the map to π6 Σ´3 KO.
D.3. The cases s “ ˘1
The cell diagrams for Σ´1 M Op1q and Σ1 M T Op1q are easily derived from the Thom isomorphism
and Wu formula
Sqn pU q “ wn ¨ U
for the action of the Steenrod operations on the Thom class of a (virtual) vector bundle. The
diagrams work out to be

and continue infinitely far upward, repeating the evident pattern of Steenrod operations. There
are no additional free summands in these cases.
D.4. The case s “ 4
The next easiest case to understand is the case s “ 4. To derive it requires a useful technique
introduced by Adams and Margolis [AM], and developed considerably further by Margolis [Ma].

<!-- page 124 -->
124

D. S. FREED AND M. J. HOPKINS

The subalgebra A1 contains two of the Milnor operators
Q0 “ Sq1
Q1 “ rSq2 , Sq1 s
and together they generate an exterior algebra
ErQ0 , Q1 s Ă A1 .
Definition D.1. Suppose that M is an A1 module. For i “ 0, 1 the ith Margolis homology of M
is
H˚ pM ; Qi q “ ker Qi { image Qi .
The Margolis homology of a space or spectrum X is the Margolis homology of H ˚ X
H˚ pX; Qi q “ H˚ pH ˚ pXq; Qi q.
Remark D.2. The Milnor elements are primitive, and the Kunneth isomorphism holds:
H˚ pM b N ; Qi q « H˚ pM ; Qi q b H˚ pN ; Qi q.
The following theorem of Adams and Margolis [AM, Theorem 3.1] (attributed by Adams and
Margolis to Wall, in this particular case) is one reason the Margolis homology groups are important.
Theorem D.3 (Adams-Margolis). A connected A1 -module M is free if and only if
H˚ pM ; Q0 q “ H˚ pM ; Q1 q “ 0.
The action of the Milnor operators on
H ˚ pBSO3 ; Z{2q “ Z{2rw2 , w3 s.
is given by
Q0 pw2 q “ w3
Q0 pw3 q “ 0.
This implies that the Margolis homology with respect to Q0 is
H˚ pBSO3 ; Q0 q « Z{2rw22 s.

<!-- page 125 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

125

Write U for the Thom class in H ˚ M O3 . Since Q0 pU q “ w1 U “ 0 the Thom isomorphism
commutes with Q0 , and the Margolis homology of M SO3 with respect to Q0 is
U ¨ Z{2rw22 s.
For the Q1 homology note that
Q1 pw2 q “ w2 w3
Q1 pw3 q “ w32
Q1 pU q “ U w3 .
It follows that H ˚ M SOp3q, as a module over the exterior algebra ErQ1 s, is a sum of
U Fj “ tU w2j , U w2j w3 , U w2j w32 , U w2j w33 , . . . u.
Using this one sees that the Margolis homology with respect to Q1 of M SOp3q has basis tU w22j`1 u.
Now let M and N be the A1 -modules

and consider the map
pM ‘ N q b Z{2rw24 s Ñ H ˚ pM SO3 q.

(D.4)

The map (D.4) is an inclusion. Together with the Kunneth formula, the computation just described
implies that it induces an isomorphism of Margolis homology with respect to both Q0 and Q1 . By
the Theorem of Adams and Margolis its cokernel is free, and there is an isomorphism
H ˚ pM SO3 q « pM ‘ N q b Z{2rw24 s ‘ free modules.
The cell diagram in box s “ 4 in Figure 5 depicts pM ‘ N q b Z{2rw24 s.
One can work out the disposition of the free modules by computing Poincaré series. The Poincaré
series for the indecomposables of the free modules (with U placed in degree 0) is the quotient of
1
p1 ´ t2 qp1 ´ t3 q

´

p1 ` t2 ` t3 ` t4 p1 ` t ` 2t2 ` t3 ` t4 ` t5 qq
p1 ´ t8 q

by the Poincaré series p1 ` tqp1 ` t2 qp1 ` t3 q of A1 . This works out to be
t9
“ t9 ` t15 ` t17 ` Orts21 .
p1 ´ t6 qp1 ´ t8 q

<!-- page 126 -->
126

D. S. FREED AND M. J. HOPKINS

Most of the time this is enough information. However for some purposes it is useful to have a
basis for the generators of the free modules. In this case one can work out that the summand of
free modules is
A1 rw32 , w24 s ¨ U w23 w3 ,
and that
(D.5)

pM ‘ N q b Z{2rw24 s ‘ A1 rw32 , w24 s b U w23 w3 Ñ H ˚ pM SO3 q

is an isomorphism. We now digress to describe a technique for verifying this. The technique applies
to modules over any connected graded Hopf algebra and exploits the fact that such an algebra is a
Frobenius algebra. We will describe it explicitly for A1 .
Let bpxq “ Sq2 Sq2 Sq2 pxq (this is the operation that goes from the bottom dot to the top dot in
the cell diagram for A1 ). If F is a free A1 -module, and x P F there are elements a P A1 and y P F
with a ¨ x “ bpyq ‰ 0. This proved by reducing to the case F “ A1 and either checking directly or
appealing to the fact that A1 is a Frobenius algebra.
Lemma D.6. Suppose that F and M are A1 modules and that F is free. A map F Ñ M is a
monomorphism if and only if the induced map bpF q Ñ bpM q is a monomorphism.
Proof. The only if statement is clear. For the converse, suppose that bpF q Ñ bpM q is a monomorphism and x P F . By the above there are a P A1 and y P F with a ¨ x “ bpyq ‰ 0. Since
bpF q Ñ bpM q is a monomorphism the image of bpyq is non-zero, hence so is the image of apxq and
hence so is the image of x.

Remark D.7. Since A1 is a finite dimensional Hopf algebra, it is also injective as a module over
itself. This means that if F Ă M is a free submodule of finite type (finite rank in each degree)
then there is a decomposition M « M 1 ‘ F . This leads to a fairly quick way of locating the free
summands in an A1 -module M . They are generated by any subset B Ă M with the property that
bpBq Ă bpM q is a basis.
Lemma D.8. For an A1 module N the following are equivalent
i) If F is a free module and F Ă N then F “ 0.
ii) bpxq “ 0 for all x P N .
Proof. Suppose that F Ă N is a free submodule. If F is non-zero then there is an x P F with
bpxq ‰ 0, so bpN q ‰ 0. Conversely if there is an x P N with bpxq ‰ 0 then the map
Σ|x| A1 Ñ N
a ÞÑ a ¨ x
is a monomorphism by Lemma D.6.



Definition D.9. An A1 module N has no free submodules if it has the equivalent properties above.
By Remark D.7 having a free submodule is equivalent to having a free summand.

<!-- page 127 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

127

Lemma D.10. Suppose that H is an A1 -module, and N Ă H a summand having no free submodules. If F is a free module and F Ñ H is a monomorphism, then F Ñ H{N is a monomorphism.
Proof. By Lemma D.6 it suffices to show that bpF q Ñ bpH{N q is a monomorphism. Since bpN q “ 0
and N is a summand, the map bpHq Ñ bpH{N q is an isomorphism.

Returning to the cohomology of M SO3 , we now use these ideas to show that (D.5) is an isomorphism of A1 modules. Both sides have the same Poincaré series so it suffices to show that the map
is a monomorphism, or equivalently that the map
`
˘
A1 rw32 , w24 s b U w23 w3 Ñ H ˚ pM SO3 q{ pM ‘ N q b Z{2rw24 s
is a monomorphism. Since M and N visibly have no free submodules, neither does pM ‘ N q b
Z{2rw24 s, so by Lemma D.10 it suffices to show that
A1 rw32 , w24 s b U w23 w3 Ñ H ˚ pM SO3 q
is a monomorphism. This is done with the aid of Lemma D.6. Since
Sq1 pw24 q “ Sq2 pw24 q “ 0
Sq1 pw32 q “ Sq2 pw32 q “ 0

and
Sq2 Sq2 Sq2 pU w23 w3 q “ U w35
the assertion comes down to checking that
tU w35 w24k w32` u,
is linearly independent, which is easy.
D.5. The case s “ ˘2
We begin with the formulas
Q0 pw1 q “ w12
Q0 pw2 q “ w1 w2
Q1 pw1 q “ w14
Q1 pw2 q “ w13 w2 ` w1 w22 .

<!-- page 128 -->
128

D. S. FREED AND M. J. HOPKINS

For both M O2 and M T O2
Q0 pU q “ w1 U
Q1 pU q “ pw13 ` w1 w2 qU,
so the Thom isomorphism
H ˚ pM O2 q « H ˚ pM T O2 q
induces an isomorphism of Margolis homology.
Restricting attention to M O2 , let
Fn Ă H ˚ M O2
be the subspace with basis
tU w1i w2j | j ď nu
and F̄n the subspace with basis
tU w1i w2n u,
so that there is a vector space isomorphism
Fn «

à

F̄j .

jďn

The Milnor operator Q0 preserves the decomposition into the spaces F̄j and from the formulas
above one concludes that
H˚ pF̄2n ; Q0 q “ 0
and
H˚ pF̄2n`1 ; Q0 q “ Z{2tU w22n`1 u.
This shows that the Q0 Margolis homology of H˚ M O2 has basis tU w22n`1 u.
The Milnor operator Q1 maps Fn´1 to Fn . We can determine the Margolis homology from the
associated spectral sequence. Identifying Fn {Fn´1 « F̄n and using the formulas above, one easily
checks that the first differential in this spectral sequence is the Z{2rw1 s-linear map
¨w w

1 2
F̄2n ÝÝÝ
ÝÑ F̄2n`1

0

F̄2n`1 Ý
Ñ F̄2n`2 .
It follows that the Q1 Margolis homology of H ˚ pM O2 q also has basis tU w22n`1 u.
Let M and N be the A1 modules below

<!-- page 129 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

129

The map
`
˘
Z{2rw24 s b M ‘ N Ñ H ˚ pM O2 q
is then an inclusion and induces an isomorphism of Margolis homology. If follows that
`
˘
H ˚ M O2 « Z{2rw24 s b M ‘ N ‘ free.
The location of the free modules can be determined from the Poincaré series. The Poincaré series
for the generators is the quotient of
1
p1 ` t ` t2 ` t3 ` t4 ` t6 q
´
p1 ´ tqp1 ´ t2 q
p1 ´ t8 q
by the Poincaré series p1 ` tqp1 ` t2 qp1 ` t3 q of A1 . This works out to be
t2
p1 ´ t2 qp1 ´ t8 q

“

t2 ` t4
.
p1 ´ t4 qp1 ´ t8 q

In fact the subspace of free modules is a free module over A1 rw14 , w24 s and has
tU w12 , U w22 u
as a basis. As before, it suffices from the Poincaré series above to check that the map
A1 rw14 , w24 stU w12 , U w22 u Ñ H ˚ pM O3 q
is a monomorphism, and for this to check that the set
`
˘
`
˘
tSq2 Sq2 Sq2 U w12 w14k w24` , Sq2 Sq2 Sq2 U w22 w14k w24` u
is linearly independent.
Z{2rw14 , w24 s and

This is easily deduced from the fact that Sq2 Sq2 Sq2 is linear over

Sq2 Sq2 Sq2 pU w12 q “ U w16 w2
Sq2 Sq2 Sq2 pU w22 q “ U w14 w23 .
The situation with M T O2 is similar, the variations being the use of the modules

<!-- page 130 -->
130

D. S. FREED AND M. J. HOPKINS

and the Poincaré series
1 ` t6
p1 ´ t4 qp1 ´ t8 q
for the generators of the free modules, from which one can conclude that the subspace of free
modules is the sub A1 rw14 , w24 s-module with basis
tU, U w12 w22 u
on which the operator Sq2 Sq2 Sq2 takes the value
U w14 w2 , U w16 w23 .
D.6. The case s “ ˘3
We now turn to the case of M O3 . This is the most complicated of the cases and the specific
determination of the free summands was carried out with the aid of Mathematica.
It will be helpful to use the equivalence
BO1 ˆ BSO3 Ñ BO3
classifying the tensor product of the defining vector bundles. Write
wi P H i pBO3 q
vi P H i BSO3
v1 P H 1 BO1

for the corresponding Stiefel-Whitney classes, so that under the equivalence above we have
w1 “ v1
w2 “ v2 ` v12
w3 “ v3 ` v2 v1 ` v13 .
and
v 1 “ w1
v2 “ w12 ` w2
v 3 “ w1 w2 ` w3 .

<!-- page 131 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

131

Now note that
Q0 U “ U pv1 q
Q1 U “ U pv3 ` v13 q

so that as far as the Minor operators are concerned there is an isomorphism
H ˚ pM Op3qq « H ˚ pM SO3 q b H ˚ pM O1 q.
From this one concludes that
H ˚ pM O3 ; Q0 q “ 0
and that the Margolis homology H ˚ pM O3 ; Q1 q has basis tU v1 v22j`1 u.
As in the case of M SOp3q let M and N be the A1 -modules depicted below (in which the blue
dot indications the location of the Margolis homology group)

Then the map
pM ‘ N q b Z{2rv24 s Ñ H ˚ pM O3 q
is a monomorphism and induces an isomorphism of Margolis homology groups. It follows that
H ˚ pM O3 q « pM ‘ N q b Z{2rv24 s ‘ free.
The Poincaré series for the indecomposables of the free modules (with U placed in degree 0) is the
quotient of
1
p1 ´ tq´1 ` t3 ` t4 ` t6 p1 ´ tq´1
´
p1 ´ tqp1 ´ t2 qp1 ´ t3 q
p1 ´ t8 q
by the Poincaré series p1 ` tqp1 ` t2 qp1 ` t3 q of A1 . It works out to be
t2
t4 ` t5 ` t6 ` t9 ` t10 ` t11 ` t12 ` t15
`
.
p1 ´ t4 q p1 ´ t8 q
p1 ´ t4 q p1 ´ t8 q p1 ´ t12 q

<!-- page 132 -->
132

D. S. FREED AND M. J. HOPKINS

The free modules correspond to the sum of
A1 rw14 , w24 stU w12 u
and the free A1 rw14 , w24 , w34 s-module on
U w22 , U w2 w3 , U w32 , U w23 w3 , U w22 w32 , U w12 w23 w3 , U w12 w22 w32 , U w23 w33

(

To see that these are linearly independent, one applies Sq2 Sq2 Sq2 to reduce the problem to showing
that the union of
! `
)
˘
U w16 w2 ` w15 w3 w14k w24`
and the set consisting of the products of w14k w24` w34m with the elements of
`
˘
`
˘
U w14 w23 ` w13 w22 w3 ` w12 w2 w32 ` w1 w33 , U w14 w22 w3 ` w12 w33 ,
`
˘
`
˘
`
˘
`
˘
U w14 w2 w32 ` w13 w33 , U w12 w22 w33 ` w35 , U w12 w2 w34 ` w1 w35 , U w16 w24 w3 ` w12 w35 ,
`
˘
U w16 w23 w32 ` w15 w22 w33 ` w14 w2 w34 ` w13 w35 ,
`
˘(
U w14 w24 w33 ` w37
is linearly independent. A couple of maneuvers will make this obvious. First of all, let’s apply the
Thom isomorphism to get rid of the appearance of U . Next regard everything as a module over
Z{2rw14 , w24 s and look at the associated graded of the increasing filtration by powers of w3 . Doing
so reduces the problem to showing that the map from the free Z{2rw14 , w24 s-module on
w15 w3 , w1 w33`4k , w12 w33`4k , w13 w33`4k , w35`4k , w1 w35`4k , w12 w35`4k , w13 w35`4k , w37`4k

(

to H ˚ pBO3 q is a monomorphism, which is easy.
The analysis is similar for M T O3 . The Margolis homology is the same as that for M O3 since
the ratio of the two Thom classes is w32 which is annihilated by the Milnor operators. The basic
modules for M T O3 are as below.

<!-- page 133 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

133

The Poincaré series for the free modules as the quotient of
1
t2 p1 ´ tq´1 ` t6 p1 ´ tq´1 ` t5 ` t6 ` t8 ` t9
´
p1 ´ tqp1 ´ t2 qp1 ´ t3 q
p1 ´ t8 q
by the Poincaré series p1 ` tqp1 ` t2 qp1 ` t3 q of A1 . This can be written as
t7
1 ` t4 ` t6 ` t9 ` t10 ` t11 ` t15 ` t17
`
p1 ´ t4 q p1 ´ t8 q
p1 ´ t4 q p1 ´ t8 q p1 ´ t12 q
The inclusion of the free summands turns out to be the sum of the A1 rw14 , w24 , w34 s module map
A1 rw14 , w24 , w34 s U, U w22 , U w12 w22 , U w23 w3 , U w22 w32 ,
(
U w2 w33 , U w23 w33 , U w12 w23 w33 Ñ H ˚ pM T O3 q
and the A1 rw14 , w24 s-module map
A1 rw14 , w24 stU w12 w2 w3 u Ñ H ˚ pM T O3 q.
As above, to check this it suffices to apply Sq2 Sq2 Sq2 to the generators above and show that the
map from the sum of the free Z{2rw14 , w24 , w34 s-module on
`
˘
`
˘
U w14 w2 ` w13 w3 , U w12 w2 w32 ` w1 w33 ,
`
˘
`
˘
U w16 w23 ` w15 w22 w3 ` w14 w2 w32 ` w13 w33 , U w14 w24 w3 ` w35 ,
`
˘
U w14 w23 w32 ` w13 w22 w33 ` w12 w2 w34 ` w1 w35 ,
`
˘
`
˘
`
˘(
U w14 w22 w33 ` w12 w35 , U w12 w22 w35 ` w37 , U w16 w24 w33 ` w12 w37
and the free Z{2rw14 , w24 s-module on
`
˘
U w16 w22 w3 ` w14 w33
to H ˚ pM T O3 q is a monomorphism. Again, by filtering by powers of w3 , using the Thom isomorphism, and looking at the associated graded, it suffices to check that the map from
Z{2rw14 , w24 stw14 w33 , w13 w31`4k , w1 w33`4k , w13 w33`4k , w35`4k , w12 w35`4k , w37`4k , w12 w37`4k u
to H ˚ pBO3 q is a monomorphism, which is obvious.

p n via classifying spaces
Appendix E. Construction of H
p n from
For the analysis in Section 10 it is useful to describe the construction of the spaces B H
the point of view of homotopy theory. This constitutes an alternative proof of Theorem 3.13.

<!-- page 134 -->
134

D. S. FREED AND M. J. HOPKINS

E.1. Preliminary
We begin with a left, pointed BSpin-module BH and a BSpin-module map p : BH Ñ BO. We
will write the base point as 0 P BH, and the action
BSpin ˆ BH Ñ BH
as
pV, W q ÞÑ V ‘ W.
We define BHn and maps BSpinn Ñ BHn Ñ BOn by the pullback diagram
BSpinn

/ BSpin




/ BH




/ BO

BHn

BOn

Remark E.1. We will be interested in the case in which the spaces BHn are the classifying spaces
of a family of compact Lie groups Hn .
p npmq
E.2. A family of spaces B H
Our aim is to define extensions
p n Ñ Z{2
Hn Ñ H
equipped with a splitting for each choice of a hyperplane reflection σ P On , and normalized so that
p n “ BP in` .
B Spin
n

(E.2)
We will actually construct extensions

p pmq Ñ Z{2
Hn Ñ H
n
for every m P Z, and show that these extensions are 4-fold periodic in m. The case m ” 1 mod 4
is satisfies the normalization condition (E.2) above.
p npmq . Namely, for m P Z
We first construct what will end up being the classifying spaces of H
pmq
p n by the pullback square
define B H
pn
BH

/ BH ˆ BZ{2





pmq

(E.3)
BOn

p ‘ mOp1q

/ BO

In the above, Op1q is the tautological line bundle on BZ{2 and for a vector space V we write
V̄ “ V ´ dim V.

<!-- page 135 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

135

Example E.4. Suppose that BH “ BSpin so that BHn “ BSpinn . If m ” 1 mod 4, then the
pullback square then fits into a diagram
pmq

z
B Spin
n

/ BSpin ˆ BZ{2





p ‘ mOp1q

/ BO

BOn

w2

/ KpZ{2, 2q
pmq

in which the corner of maps on the right is a fibration sequence. It follows that B z
Spinn

» BPin`
n.

pmq

p n Ñ BOn essentially depend only on m mod 4, so we may
We next show that the maps B H
p n Ñ BOn . To do this choose a
take any convenient value of m ” 1 mod 4 as our definition of B H
lift
BSpin
5
W


/ BO .

BZ{2
4Op1q

Then for any integer ` the map
ρ` : BZ{2 ˆ BH Ñ BZ{2 ˆ BH
px, yq ÞÑ px, `W pxq ‘ yq
is a homotopy equivalence, and fits into a diagram
ρ`

BH ˆ BZ{2
p ‘ pp4``kqOp1qq

&

BO.

/ BH ˆ BZ{2
x

p ‘ kOp1q

for any integer k. Pulling back along BOn Ñ BO gives
ρ`

pk`4`q

pn
BH

%

BOn

p npkq
/ BH
{

in which the top map is an equivalence.
Remark E.5. The maps ρ` depend on the choice of W which is not unique. In fact there are two
lifts of 4Op1q. In terms of formulas, a choice of lift corresponds to choosing an element of Spin4
lying over ´I4 P SO4 . The two choices are
˘e1 e2 e3 e4 .
To be definite we choose the lift given by
e1 e2 e3 e4 .

<!-- page 136 -->
136

D. S. FREED AND M. J. HOPKINS
pmq

pn
E.3. The Lie groups H

The pullback (E.3) can be rearranged in many ways. Note that if

F
i

j

/Y
g



X



f

/ BO

is a pullback diagram, then so is
pi,jq

F

/ X ˆY




´f ‘g

/ BO

˚
Using this (E.3) can be rewritten as

pn
BH

/ BH




/ BO

pmq

BOn ˆ BZ{2

V n ´m Op1q



BOn
where V n Ñ BOn is the universal bundle. When m “ ´k, with k ě 0, the above pullback can be
factored as
p npmq
/ BHn`k
/ BH
BH


BOn ˆ BZ{2

id‘k Op1q


/ BOn`k


/ BO.

This has the advantage of showing that if for all n, BHn is the classifying space of a compact Lie
p npmq is the classifying space of a compact Lie group H
p npmq . By the
group Hn then for m ď 0, B H
4-fold periodicity described above this is actually true for all m.
In §3.3 we fix the value of m “ ´3 and define
pn “ H
p p´3q .
H
n
This matches the construction in (3.19). For the bordism computations in §10 it is useful to use
the equivalence
p p´3q Ñ B H
p p1q
ρ1 : B H
n
n

<!-- page 137 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

137

and obtain the pullback square
pn
BH

/ BZ{2 ˆ BH





BOn

Op1q‘p

/ BO

References
[A1]
[A2]
[ABP1]
[ABP2]
[ABS]
[Ad]
[AF]
[AM]
[APS]
[AS]
[AZ]
[BB]

[BC]
[BD]
[BDGK]

[BeC]

[BG]
[BM]

[BrMo]
[BS]

M. F. Atiyah, Topological quantum field theories, Inst. Hautes Études Sci. Publ. Math. (1988), no. 68,
175–186 (1989). 3, 15, 16
, K-theory and reality, Quart. J. Math. Oxford Ser. (2) 17 (1966), 367–386. 87
D. W. Anderson, E. H. Brown, Jr., and F. P. Peterson, The structure of the Spin cobordism ring, Ann.
of Math. (2) 86 (1967), 271–298. 91, 93, 97, 121, 122
, Pin cobordism and related topics, Comment. Math. Helv. 44 (1969), 462–468. 91
M. F. Atiyah, R. Bott, and A. Shapiro, Clifford modules, Topology 3 (1964), no. suppl. 1, 3–38. 7, 15,
22, 76, 79, 82, 87, 103, 104, 107, 109, 111
J. F. Adams, Prerequisites (on equivariant stable homotopy) for Carlsson’s lecture, Algebraic topology,
Aarhus 1982 (Aarhus, 1982), Lecture Notes in Math., vol. 1051, Springer, Berlin, 1984, pp. 483–532. 39
David Ayala and John Francis, The cobordism hypothesis, 1705.02240. 32, 35
J. F. Adams and H. R. Margolis, Modules over the Steenrod algebra, Topology 10 (1971), 271–282. 123,
124
M. F. Atiyah, V. K. Patodi, and I. M. Singer, Spectral asymmetry and Riemannian geometry. I, Math.
Proc. Cambridge Philos. Soc. 77 (1975), 43–69. 61, 88
M. F. Atiyah and I. M. Singer, Index theory for skew-adjoint Fredholm operators, Inst. Hautes Études
Sci. Publ. Math. (1969), no. 37, 5–26. 83, 84
Alexander Altland and Martin R. Zirnbauer, Nonstandard symmetry classes in mesoscopic normalsuperconducting hybrid structures, Phys. Rev. B 55 (1997), 1142–1161. 8, 79
Garrett Birkhoff and M. K. Bennett, Felix Klein and his “Erlanger Programm”, History and philosophy
of modern mathematics (Minneapolis, MN, 1985), Minnesota Stud. Philos. Sci., XI, Univ. Minnesota
Press, Minneapolis, MN, 1988, pp. 145–176. 9
E. H. Brown and M. Comenetz, Pontrjagin duality for generalized homology and cohomology theories,
Amer. J. Math. 98 (1976), 1–27. 35
John C. Baez and James Dolan, Higher-dimensional algebra and topological quantum field theory, J.
Math. Phys. 36 (1995), no. 11, 6073–6105, arXiv:q-alg/9503002. 4, 32
Marcus Berg, Cécile DeWitt-Morette, Shangjr Gwo, and Eric Kramer, The pin groups in physics: C,
P and T, Reviews in Mathematical Physics 13 (2001), no. 08, 953–1034, arXiv:math-ph/0012006. 107,
113
Agnès Beaudry and Jonathan A. Campbell, A guide for computing stable homotopy groups, Topology
and quantum theory in interaction, Contemp. Math., vol. 718, Amer. Math. Soc., Providence, RI, 2018,
pp. 89–136. arXiv:1801.07530. 8, 98
Anthony Bahri and Peter Gilkey, The eta invariant, Pinc bordism, and equivariant Spinc bordism for
cyclic 2-groups, Pacific J. Math. 128 (1987), no. 1, 1–24. 93
Marcel Bökstedt and Ib Madsen, The cobordism category and Waldhausen’s K-theory, An alpine expedition through algebraic topology, Contemp. Math., vol. 617, Amer. Math. Soc., Providence, RI, 2014,
pp. 39–80. arXiv:1102.4155. 32, 35
Greg Brumfiel and John Morgan, The Pontrjagin Dual of 3-Dimensional Spin Bordism,
arXiv:1612.02860. 5
Clark Barwick and Christopher Schommer-Pries, On the Unicity of the Homotopy Theory of Higher
Categories, 1112.0040. 32

<!-- page 138 -->
138

[Bu]
[BuS]
[C]
[Ca]
[CFLS]
[CGW]

[CM]
[CS]
[D]
[De]
[DF]
[DM]

[E]
[F1]
[F2]
[F3]
[F4]
[FCV]

[FH1]
[FH2]
[FHT1]

[FHT2]
[FK1]
[FK2]
[FKM]
[FL]
[FM1]

D. S. FREED AND M. J. HOPKINS

Ulrich Bunke, Transgression of the index gerbe, Manuscripta Math. 109 (2002), no. 3, 263–287,
arXiv:math/0109052. 88
Ulrich Bunke and Thomas Schick, Smooth K-theory, Astérisque (2009), no. 328, 45–135 (2010),
arXiv:0707.0046. 88
Jonathan A. Campbell, Homotopy theoretic classification of symmetry protected phases,
arXiv:1708.04264. 5, 8, 98
F. Catanese, On the moduli spaces of surfaces of general type, J. Differential Geom. 19 (1984), no. 2,
483–515. 2
Clay Cordova, Daniel S. Freed, Ho Tat Lam, and Nathan Seiberg, Anomalies in the Space of Coupling
Constants and Their Dynamical Applications I, SciPost Phys., to appear, arXiv:1905.09315. 89
Xie Chen, Zheng-Cheng Gu, and Xiao-Gang Wen, Local unitary transformation, long-range quantum
entanglement, wave function renormalization, and topological order, Phys. Rev. B 82 (2010), 155138,
arXiv:1004.3835. 3
Sidney Coleman and Jeffrey Mandula, All possible symmetries of the S matrix, Physical Review 159
(1967), no. 5, 1251–56. 5, 9
Damien Calaque and Claudia Scheimbauer, A note on the p8, nq-category of cobordisms, Algebr. Geom.
Topol. 19 (2019), no. 2, 533–655, arXiv:1509.08906. 16, 32
Freeman J. Dyson, The threefold way. Algebraic structure of symmetry groups and ensembles in quantum
mechanics, J. Mathematical Phys. 3 (1962), 1199–1215. 8, 79
Pierre Deligne, Notes on spinors, Quantum Fields and Strings: a course for mathematicians, Vol. 1, 2
(Princeton, NJ, 1996/1997), Amer. Math. Soc., Providence, RI, 1999, pp. 99–135. 84, 85
Xianzhe Dai and Daniel S. Freed, η-invariants and determinant lines, C. R. Acad. Sci. Paris Sér. I
Math. 320 (1995), no. 5, 585–591, arXiv:hep-th/9405012. 88
Pierre Deligne and John W. Morgan, Notes on supersymmetry (following Joseph Bernstein), Quantum
fields and strings: a course for mathematicians, Vol. 1, 2 (Princeton, NJ, 1996/1997), Amer. Math.
Soc., Providence, RI, 1999, pp. 41–97. 21, 55, 115
Johannes Ebert, A vanishing theorem for characteristic classes of odd-dimensional manifold bundles, J.
Reine Angew. Math. 684 (2013), 1–29, arXiv:0902.4719. 56
Daniel S. Freed, Higher algebraic structures and quantization, Comm. Math. Phys. 159 (1994), no. 2,
343–398, arXiv:hep-th/9212115. 4, 32
, The cobordism hypothesis, Bull. Amer. Math. Soc. (N.S.) 50 (2013), no. 1, 57–92,
arXiv:1210.5100. 16, 32
, Anomalies and invertible field theories, String-Math 2013, Proc. Sympos. Pure Math., vol. 88,
Amer. Math. Soc., Providence, RI, 2014, pp. 25–45. arXiv:1404.7224. 87
, Lectures on Field Theory and Topology, CBMS Regional Conference Series in Mathematics,
vol. 133, American Mathematical Society, 2019. 8, 37, 87, 89
Lukasz Fidkowski, Xie Chen, and Ashvin Vishwanath, Non-Abelian Topological Order on the Surface of
a 3D Topological Superconductor from an Exactly Solved Model, Phys. Rev. X3 (2013), no. 4, 041016,
arXiv:1305.5851 [cond-mat.str-el]. 92
Daniel S. Freed and Michael J. Hopkins, Chern-Weil forms and abstract homotopy theory, Bull. Amer.
Math. Soc. (N.S.) 50 (2013), no. 3, 431–468, arXiv:1301.5959. 70
, Consistency of M-theory on unorientable manifolds, arXiv:1908.09916. 88
Daniel S. Freed, Michael J. Hopkins, and Constantin Teleman, Consistent orientation of moduli spaces,
The many facets of geometry, Oxford Univ. Press, Oxford, 2010, pp. 395–419. arXiv:0711.1909. 4, 37,
57
, Loop groups and twisted K-theory III, Ann. of Math. 174 (2011), no. 2, 974–1007,
arXiv:math/0511232. 78
Lukasz Fidkowski and Alexei Kitaev, Topological phases of fermions in one dimension, Phys. Rev. B
83 (2011), 075103, arXiv:1008.4138. 92
, Effects of interactions on the topological classification of free fermion systems, Phys. Rev. B
81 (2010), 134509, arXiv:0904.2197. 92
Liang Fu, C. L. Kane, and E. J. Mele, Topological Insulators in Three Dimensions, Phys. Rev. Lett. 98
(2007), 106803, arXiv:cond-mat/0607699. 94
Daniel S. Freed and John Lott, An index theorem in differential K-theory, Geom. Topol. 14 (2010),
no. 2, 903–966, arXiv:0907.3508. 84, 88
Daniel S. Freed and Gregory W. Moore, Twisted equivariant matter, Ann. Henri Poincaré 14 (2013),
no. 8, 1927–2023, arXiv:1208.5055. 8, 10, 79, 115

<!-- page 139 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

[FM2]
[GJ]
[GK]
[GKKS]
[GM]
[GMTW]
[GPW]

[GT]
[GW]

[H]

[HHR]
[HHZ]
[HS]
[J]
[J-F]
[K1]
[K2]
[K3]
[K4]

[K5]
[K6]
[Ka1]
[Ka2]

[Kap]
[Kaz]

[Klo]

139

, Setting the quantum integrand of M-theory, Commun. Math. Phys. 263 (2006), 89–132,
arXiv:hep-th/0409135. 6
James Glimm and Arthur Jaffe, Quantum physics, second ed., Springer-Verlag, New York, 1987. A
functional integral point of view. 20, 105, 112
Davide Gaiotto and Anton Kapustin, Spin TQFTs and fermionic phases of matter, International Journal of Modern Physics A 31 (2016), no. 28n29, 1645044, arXiv:1505.05856. 5, 35, 37, 105
Davide Gaiotto, Anton Kapustin, Zohar Komargodski, and Nathan Seiberg, Theta, time reversal and
temperature, Journal of High Energy Physics 2017 (2017), no. 5, 91, arXiv:1703.00501. 19
J. P. C. Greenlees and J. P. May, Equivariant stable homotopy theory, Handbook of algebraic topology,
North-Holland, Amsterdam, 1995, pp. 277–323. 39
Søren Galatius, Ulrike Tillmann, Ib Madsen, and Michael Weiss, The homotopy type of the cobordism
category, Acta Math. 202 (2009), no. 2, 195–239, arXiv:math/0605249. 35, 55, 57
Meng Guo, Pavel Putrov, and Juven Wang, Time Reversal, SU(N) Yang-Mills and Cobordisms: Interacting Topological Superconductors/Insulators and Quantum Spin Liquids in 3+1D, arXiv:1711.11587.
5, 90
Hilary Greaves and Teruji Thomas, On the CPT theorem, Stud. Hist. Philos. Sci. B Stud. Hist. Philos.
Modern Phys. 45 (2014), 46–65, arXiv:1204.4674. 5, 107, 109
Zheng-Cheng Gu and Xiao-Gang Wen, Symmetry-protected topological orders for interacting fermions:
Fermionic topological nonlinear σ models and a special group supercohomology theory, Physical Review
B 90 (2014), no. 11, 115141, arXiv:1201.2648. 5, 91, 92
M. J. Hopkins, Algebraic topology and modular forms, Proceedings of the International Congress of Mathematicians, Vol. I (Beijing, 2002) (Beijing), Higher Ed. Press, 2002, pp. 291–317.
arXiv:math/0212397. 82, 83
M. A. Hill, M. J. Hopkins, and D. C. Ravenel, On the nonexistence of elements of Kervaire invariant
one, Ann. of Math. (2) 184 (2016), no. 1, 1–262. 39, 41
P. Heinzner, A. Huckleberry, and M.R. Zirnbauer, Symmetry Classes of Disordered Fermions, Communications in Mathematical Physics 257 (2005), no. 3, 725–771, arXiv:math-ph/0411040. 8, 79
M. J. Hopkins and I. M. Singer, Quadratic functions in geometry, topology, and M-theory, J. Diff. Geom.
70 (2005), 329–452, arXiv:math/0211216. 88
R Jost, A remark on the CTP theorem, Helv. Phys. Acta 30 (1957), 409–416. 107
Theo Johnson-Freyd, Spin, statistics, orientations, unitarity, Algebr. Geom. Topol. 17 (2017), no. 2,
917–956, arXiv:1507.06297. 105
Alexei Kitaev, Toward Topological Classification of Phases with Short-range Entanglement, 2011. http:
//online.kitp.ucsb.edu/online/topomat11/kitaev/. Lecture at KITP. 3, 5, 92
, On the Classification of Short-Range Entangled States, June, 2013. http://scgp.stonybrook.
edu/archives/7874. Lecture at SCGP. 5
, Short range entangled quantum states, May, 2014. lecture at MSRI. 5
, Homotopy-theoretic approach to SPT phases in action: Z{16Z classification of threedimensional superconductors, January 2015. http://www.ipam.ucla.edu/abstract/?tid=12389&
pcode=STQ2015. talk at Symmetry and Topology in Quantum Matter, Institute for Pure and Applied
Mathematics. 92
, Anyons in an exactly solved model and beyond, Annals of Physics 321 (2006), no. 1, 2–111,
arXiv:cond-mat/0506438. 6, 61
, Periodic table for topological insulators and superconductors, AIP Conf.Proc. 1134 (2009),
22–30, arXiv:0901.2686 [cond-mat.mes-hall]. 8, 79
Anton Kapustin, Symmetry Protected Topological Phases, Anomalies, and Cobordisms: Beyond Group
Cohomology, arXiv:1403.1467 [cond-mat.str-el]. 5
, Topological field theory, higher categories, and their applications, Proceedings of the International Congress of Mathematicians. Volume III (New Delhi), Hindustan Book Agency, 2010, pp. 2021–
2043. arXiv:1004:2307. 32
Mikhail Kapranov, Supergeometry in mathematics and physics, arXiv:1512.07042. 53
David Kazhdan, Introduction to QFT, Quantum fields and strings: a course for mathematicians. Vol.
1, pp. 377–418, American Mathematical Society, Providence, RI, 1999. Material from the Special Year
on Quantum Field Theory held at the Institute for Advanced Study, Princeton, NJ, 1996–1997. 20, 105,
112, 113, 114
K. R. Klonoff, An index theorem in differential K-theory, 2008. http://repositories.lib.utexas.
edu/bitstream/handle/2152/3912/klonoffk16802.pdf?sequence=2. University of Texas Ph.D. thesis.
88

<!-- page 140 -->
140

[KM]
[KS]
[KT1]

[KT2]
[KTTW]

[KZ]

[L]
[La]
[LM]
[Lo]
[LV]

[M]
[Ma]
[MFCV]

[MS]

[MW]
[Ng]
[NH]
[O]
[OS]
[QHZ]
[R]
[Re]
[S]
[S-P]
[Sch]

D. S. FREED AND M. J. HOPKINS

C. L. Kane and E. J. Mele, Z2 Topological Order and the Quantum Spin Hall Effect, Phys. Rev. Lett.
95 (2005), 146802, cond-mat/0506581. 94
M. Kontsevich and G. B. Segal, Wick rotation and the positivity of energy in quantum field theory. in
preparation. 10, 17, 28
R. C. Kirby and L. R. Taylor, Pin structures on low-dimensional manifolds, Geometry of LowDimensional Manifolds, 2 (Durham, 1989), London Math. Soc. Lecture Note Ser., vol. 151, Cambridge
Univ. Press, Cambridge, 1990, pp. 177–242. 91, 107
, A calculation of Pin` bordism groups, Comment. Math. Helv. 65 (1990), no. 3, 434–447. 91
Anton Kapustin, Ryan Thorngren, Alex Turzillo, and Zitao Wang, Fermionic Symmetry Protected
Topological Phases and Cobordisms, JHEP 12 (2015), 052, arXiv:1406.7329 [cond-mat.str-el].
[JHEP12,052(2015)]. 5, 91, 92
Ricardo Kennedy and Martin R. Zirnbauer, Bott Periodicity for Z2 Symmetric Ground States of
Gapped Free-Fermion Systems, Commun. Math. Phys. 342 (2016), no. 3, 909–963, arXiv:1409.2537
[math-ph]. 8, 79
Jacob Lurie, On the classification of topological field theories, Current developments in mathematics,
2008, Int. Press, Somerville, MA, 2009, pp. 129–280. arXiv:0905.0465. 4, 16, 32, 35
R. J. Lawrence, Triangulations, categories and extended topological field theories, Quantum topology,
Ser. Knots Everything, vol. 3, World Sci. Publ., River Edge, NJ, 1993, pp. 191–208. 4, 32
H. Blaine Lawson, Jr. and Marie-Louise Michelsohn, Spin geometry, Princeton Mathematical Series,
vol. 38, Princeton University Press, Princeton, NJ, 1989. 83, 111
John Lott, Higher-degree analogs of the determinant line bundle, Comm. Math. Phys. 230 (2002), no. 1,
41–69, arXiv:math/0106177. 88
Yuan-Ming Lu and Ashvin Vishwanath, Theory and classification of interacting integer topological phases in two dimensions: A Chern-Simons approach, Phys. Rev. B 86 (2012), 125119,
arXiv:1205.3156. 91, 92, 94, 95
Max A. Metlitski, S-duality of up1q gauge theory with θ “ π on non-orientable manifolds: Applications
to topological insulators and superconductors, arXiv:1510.05663. 75, 94
H. R. Margolis, Spectra and the Steenrod Algebra: Modules over the Steenrod Algebra and the Stable
Homotopy Category, North–Holland, New York, 1983. 123
Max A. Metlitski, Lukasz Fidkowski, Xie Chen, and Ashvin Vishwanath, Interaction effects on 3D
topological superconductors: surface topological order from vortex condensation, the 16 fold way and
fermionic Kramers doublets, arXiv:1406.3032 [cond-mat.str-el]. 92
G. W. Moore and G. B. Segal, D-branes and K-theory in 2D topological field theory, Dirichlet branes
and mirror symmetry (Paul S. Aspinwall, Tom Bridgeland, Alastair Craw, Michael R. Douglas, Mark
Gross, Anton Kapustin, Gregory W. Moore, Graeme Segal, Balázs Szendrői, and P. M. H. Wilson,
eds.), Clay Mathematics Monographs, vol. 4, American Mathematical Society, Providence, RI, 2009,
pp. x+681. arXiv:hep-th/0609042. 32
Scott Morrison and Kevin Walker, Blob homology, Geom. Topol. 16 (2012), no. 3, 1481–1607,
arXiv:1009.5025. 62
Hoang Kim Nguyen, Higher bordism categories. Master’s thesis, Universitat Bonn. 32
Rahul M. Nandkishore and Michael Hermele, Fractons, Annual Review of Condensed Matter Physics
10 (2019), no. 1, 295–313, arXiv:1803.11196. 3
Michael Luis Ortiz, Differential equivariant K-theory, ProQuest LLC, Ann Arbor, MI, 2009.
arXiv:0905.0476. Thesis (Ph.D.)–The University of Texas at Austin. 88
Konrad Osterwalder and Robert Schrader, Axioms for Euclidean Green’s functions. II, Comm. Math.
Phys. 42 (1975), 281–305. With an appendix by Stephen Summers. 20
Xiao-Liang Qi, Taylor L Hughes, and Shou-Cheng Zhang, Topological field theory of time-reversal
invariant insulators, Physical Review B 78 (2008), no. 19, 195424, arXiv:0802.3537. 91
Bruce L. Reinhart, Cobordism and the Euler number, Topology 2 (1963), 173–177. 56
Miles Reid, The moduli space of 3-folds with K “ 0 may nevertheless be irreducible, Math. Ann. 278
(1987), no. 1-4, 329–334. 2
Shlomo Sternberg, Lectures on differential geometry, second ed., Chelsea Publishing Co., New York,
1983. With an appendix by Sternberg and Victor W. Guillemin. 9
C. Schommer-Pries, Invertible field theories, arXiv:1712.08029. 32, 35
Stefan Schwede, Lecture notes on equivariant stable homotopy theory, Available at
http://www.math.uni-bonn.de/people/schwede/. 39

<!-- page 141 -->
REFLECTION POSITIVITY AND INVERTIBLE TOPOLOGICAL PHASES

[Se1]

[Se2]
[Se3]
[SeWi]

[SRFL]

[ST]

[Sto]
[SW]
[T]
[tD]
[TPB]
[W1]
[W2]
[W3]

[Wen]
[WPS]
[WS]
[YWOX]

141

Graeme Segal, The definition of conformal field theory, Topology, geometry and quantum field theory,
London Math. Soc. Lecture Note Ser., vol. 308, Cambridge Univ. Press, Cambridge, 2004, pp. 421–577.
(1988 preprint). 3, 15
, Felix Klein Lectures 2011. http://www.mpim-bonn.mpg.de/node/3372/abstracts. 17
, Classifying spaces and spectral sequences, Inst. Hautes Études Sci. Publ. Math. (1968), no. 34,
105–112. 34
Nathan Seiberg and Edward Witten, Gapped Boundary Phases of Topological Insulators via Weak
Coupling, PTEP 2016 (2016), no. 12, 12C101, arXiv:1602.04251 [cond-mat.str-el]. 7, 15, 75, 76,
77, 94
Shinsei Ryu, Andreas P. Schnyder, Akira Furusaki, and Andreas W.W. Ludwig, Topological insulators
and superconductors: Tenfold way and dimensional hierarchy, arXiv:0912.2157; New J.Phys. 12 (2010),
065010, arXiv:0912.2157. 8, 79
Stephan Stolz and Peter Teichner, Supersymmetric field theories and generalized cohomology, Mathematical foundations of quantum field theory and perturbative string theory, Proc. Sympos. Pure Math.,
vol. 83, Amer. Math. Soc., Providence, RI, 2011, pp. 279–340. arXiv:1108.0189. 17, 18, 32
Robert E. Stong, Notes on cobordism theory, Mathematical notes, Princeton University Press, Princeton,
N.J.; University of Tokyo Press, Tokyo, 1968. 93
Raymond F Streater and Arthur S Wightman, PCT, spin and statistics, and all that, Princeton University Press, 2000. 105, 112
René Thom, Quelques propriétés globales des variétés différentiables, Comment. Math. Helv. 28 (1954),
17–86. 3, 4
Tammo tom Dieck, Transformation groups and representation theory, Lecture Notes in Mathematics,
vol. 766, Springer, Berlin, 1979. 39
Ari M Turner, Frank Pollmann, and Erez Berg, Topological phases of one-dimensional fermions: An
entanglement point of view, Physical Review B 83 (2011), no. 7, 075102, arXiv:1008.4346. 92
Edward Witten, Fermion Path Integrals And Topological Phases, Rev. Mod. Phys. 88 (2016), no. 3,
035001, arXiv:1508.04715 [cond-mat.mes-hall]. 7, 77, 87, 90, 92, 94, 107
, Quantum field theory and the Jones polynomial, Comm. Math. Phys. 121 (1989), no. 3, 351–
399. 37
, What one can hope to prove about three-dimensional gauge theory. http://scgp.stonybrook.
edu/video_portal/video.php?id=563. Talk at Mathematical Foundations of Quantum Field Theory
Workshop, Simons Center for Geometry and Physics, January 2012. 37
Xiao-Gang Wen, SPT order and algebraic topology. http://helper.ipam.ucla.edu/publications/
stq2015/stq2015_12402.pdf. talk at Symmetry and Topology in Quantum Matter. 62
Chong Wang, Andrew C Potter, and T Senthil, Classification of interacting electronic topological insulators in three dimensions, Science 343 (2014), no. 6171, 629–631, arXiv:1306.3238. 93, 94
Chong Wang and T Senthil, Interacting fermionic topological insulators/superconductors in 3D, Physical
Review B 89 (2014), no. 19, 195124, arXiv:1401.1142. 8, 75, 79, 92, 94, 95, 96
Yi-Zhuang You, Zhong Wang, Jeremy Oon, and Cenke Xu, Topological number and fermion Green’s
function for strongly interacting topological superconductors, Physical Review B 90 (2014), no. 6, 060502,
arXiv:1403.4938. 92

Department of Mathematics, University of Texas, Austin, TX 78712
Email address: dafr@math.utexas.edu
Department of Mathematics, Harvard University, Cambridge, MA 02138
Email address: mjh@math.harvard.edu
