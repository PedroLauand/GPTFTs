---
type: paper
date: 2019-10-10
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1910.04745v1)
reviewed: false
---

# Universal entangleability of non-classical theories

Machine-generated and unreviewed text extraction of arXiv:1910.04745v1
(51 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1910.04745v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Universal entangleability of non-classical theories
Guillaume Aubrun∗
Institut Camille Jordan, Université Claude Bernard Lyon 1,
43 boulevard du 11 novembre 1918, 69622 Villeurbanne CEDEX, France

arXiv:1910.04745v1 [quant-ph] 10 Oct 2019

Ludovico Lami†
School of Mathematical Sciences and Centre for the Mathematics
and Theoretical Physics of Quantum Non-Equilibrium Systems,
University of Nottingham, University Park,
Nottingham NG7 2RD, United Kingdom and
Institute of Theoretical Physics and IQST, Universität Ulm,
Albert-Einstein-Allee 11D-89069 Ulm, Germany

Carlos Palazuelos‡
Departamento de Análisis Matemático y Matemática Aplicada,
Universidad Complutense de Madrid, Plaza de Ciencias s/n 28040 Madrid, Spain, and
Instituto de Ciencias Matemáticas, C/ Nicolás Cabrera, 13-15, 28049 Madrid, Spain
Inspired by its fundamental importance in quantum mechanics, we deﬁne and study the
notion of entanglement for abstract physical theories, investigating its profound connection
with the concept of superposition. We adopt the formalism of general probabilistic theories
(GPTs), encompassing all physical models whose predictive power obeys minimal requirements. Examples include classical theories, which do not exhibit superposition and whose
state space has the shape of a simplex, quantum mechanics, as well as more exotic models
such as Popescu–Rohrlich boxes. We call two GPTs entangleable if their composite admits
either entangled states or entangled measurements, and conjecture that any two non-classical
theories are in fact entangleable. We present substantial evidence towards this conjecture
by proving it (1) for the simplest case of 3-dimensional theories; (2) when the local state
spaces are discrete, which covers foundationally relevant cases; (3) when one of the local
theories is quantum mechanics. Furthermore, (4) we envision the existence of a quantitative
relation between local non-classicality and global entangleability, explicitly describing it in
the geometrically natural case where the local state spaces are centrally symmetric.

The discovery that physical systems can be entangled can be deemed one of the main
scientific achievements of the past century. While entanglement emerges naturally as a
mathematical by-product of the formalism of quantum mechanics, its status has been the
∗

aubrun@math.univ-lyon1.fr
ludovico.lami@gmail.com
‡
cpalazue@ucm.es
†

<!-- page 2 -->
subject of an intense debate, with Einstein famously seeing it as the cause of the ‘spooky
action at a distance’ that inexorably affects the theory [1]. It was not until the work of
Bell [2] that entanglement was promoted from a mere manifestation of the alleged incompleteness of quantum mechanics to a fully-fledged physical phenomenon, whose ultimate
consequences for the non-locality of physics [3] are testable and turn out to be rooted in
experimental evidence [4]. We nowadays conceive and study it as a fundamental feature
that separates quantum and classical theory [5].
Yet comparing its theoretical and empirical status, we note a striking difference: while
entanglement is regarded as a purely quantum phenomenon on the theoretical level, the fact
that we see non-locality in experiments implies that it must characterise every successful
future theory of Nature, thus suggesting that its conceptual importance goes well beyond
present-day quantum models. We however seem to lack a precise understanding of what it
may even mean outside the well-studied quantum formalism. This is to be contrasted for
instance with the satisfying model-independent definition that we have for non-locality [3].
In this paper we present a unified theory of universal entanglement that treats it in a fully
model-independent fashion. We look at a general definition of entangled state in a general
bipartite physical system, arguing that any experimentally detectable non-local effect must
come from some form of entanglement. We then proceed to study the connection between
two seemingly different yet somehow intimately connected features of physical theories:
their deviation from classicality1 at the single-system level on the one hand, and their
entangleability at the level of bipartite systems on the other. Physicists have long sensed
that these concepts may be related, as the example of quantum mechanics shows – coherent
superpositions of orthogonal pure states are the distinct signature of quantumness of a
single system, and lead directly to quantum entanglement when constructed from product
states. However, only in recent times this connection has been the subject of systematic
investigation. Equipped with our rigorous theory of universal entanglement, we show that
classicality and entangleability are directly related concepts at a foundational level. More
precisely, we prove that under certain natural assumptions every system composed of a
pair of non-classical models admits either entangled states or entangled measurements.
Our results cover but are not limited to the cases of both state spaces being discrete, i.e.
admitting only a finite number of pure states, or satisfying some regularity conditions.
We conjecture that analogous statements would hold without these assumptions for the
most general pair of non-classical theories. Our analysis shows that foundational questions
such as those concerning the a priori role of entanglement in physical systems are – rather
surprisingly – deeply rooted in convex geometry and functional analysis.

1

Here, a system is said to be classical if there is a finite number of special pure states, and every other
state can be thought of as resulting from a uniquely defined statistical ensemble of those pure states.

2

<!-- page 3 -->
I.
A.

RESULTS

General probabilistic theories

The question of what features a set of axioms should possess in order to be considered a
fully-fledged physical theory has become particularly controversial with the rise of quantum
theory. Without going too much into the philosophical aspects of the problem, a minimalist
answer is as follows: a physical theory is a set of rules that allow to deduce a probabilistic
prediction of the outcome of an experiment given the detailed description of its preparation.
Remarkably, it is possible to translate this general idea into rigorous axioms, from which a
unified theoretical framework can be derived [6–8]. The resulting formalism of general probabilistic theories (GPTs) encompasses classical probability theory and quantum mechanics
as special cases, but includes also a wealth of other models that may or may not be relevant
for future physics. We now set out to describe briefly the setup, referring the reader to the
many presentations available in the literature for further details [8–10].
The basic ingredient is a state space, i.e. a convex and compact subset Ω of some finitedimensional real vector space. Throughout this paper we will always make the exquisitely
technical assumption of finite dimension; extending the theory to infinite dimension does not
require any conceptual modification yet makes it significantly more involved [8, Chapter 1].
States, that is, preparation procedures for a given physical system, are represented by
points ω ∈ Ω. The convexity of Ω serves to model the existence of stochastic preparation
procedures: flipping a coin with outcome probabilities p (head) and 1 − p (tail), preparing
the system according to ω (head) or τ (tail), and subsequently forgetting the outcome of
the coin should result in the system being in a state pω + (1 − p)τ ∈ Ω.
For reasons that will become clear soon, it is useful to enlarge the vector space where
Ω lives, increasing its dimension by one. The resulting vector space V can be thought
of as comprising all real multiples of physical states in Ω, as depicted in Figure 1. The
dimension d of the GPT is by definition the dimension of V as a vector space, i.e. d :=
dim V = dim Ω + 1. The ‘normalising’ functional u, also called order unit, satisfies u(ω) ≡ 1
for all ω ∈ Ω. The cone C := {λω : λ ⩾ 0, ω ∈ Ω} is called the cone of (unnormalised)
states. We will usually assume that C enjoys some basic properties that correspond to
our intuitive notion of a well-behaved cone, which we signify by calling it proper (see the
Methods section for a rigorous definition). Observe that Ω = C ∩ u−1 (1). Mathematically,
this gives V the structure of an ordered vector space: the ordering is defined for x, y ∈ V
by saying that x ⩽ y if y − x ∈ C. Observe that, unlike that between real numbers, this
ordering is not total, i.e. it is possible that neither x ⩽ y nor y ⩽ x.
A physical theory needs measurements in addition to states. The probability that a
certain outcome of a given measurement occurs is a function of the state, called an effect
and denoted by e : Ω → [0, 1]. It can be shown that in order to preserve our interpretation
of stochastic state preparations e must in fact be convex-linear, which can be expressed
mathematically by requiring that e(pω + (1 − p)τ ) = p e(ω) + (1 − p)e(τ ) for all ω, τ ∈ Ω
3

<!-- page 4 -->
and all probabilities p ∈ [0, 1]. It is then possible to make e linear by extending its action
from Ω to the whole V . Linear functionals acting on V form themselves a vector space,
called the dual of V and denoted with V ∗ . It is possible to make V ∗ an ordered vector
space in a natural way: for f, g ∈ V ∗ , we say that f ⩽ g if f (ω) ⩽ g(ω) for all ω ∈ Ω
(equivalently, for all ω ∈ C). Positive functionals form again a cone, called the dual cone
to C and denoted with C ∗ . The operational requirement that each effect should produce
a probability when evaluated on a physical state can then be very naturally rephrased
as the two-fold inequality 0 ⩽ e ⩽ u, to be understood as holding with respect to the
ordering of V ∗ . Hence, in the GPT formalism a measurement is a (finite) collection of
effects (ei )i∈I , where each ei ∈ V ∗ satisfies eP
i ⩾ 0, and the completeness condition for the
outcome probabilities further imposes that i∈I ei = u. The probability of obtaining the
outcome i when measuring the state ω is given by ei (ω).

It is a separate question, related to the physics of the system under consideration,
whether any collection of effects with the above properties may be implemented as an actual
physical measurement. This assumption is usually called the no-restriction hypothesis [11].
As classical and quantum mechanics both satisfy it, we will henceforth include it in our list
of assumptions. In fact, it will play an important role in deriving the implications of our
results for the foundations of physics. With the no-restriction hypothesis, the list of rules
to translate physical experiments into the mathematical formalism – and vice versa – and
to make probabilistic predictions about their results is complete. Since all we need is the
triple A = (V, C, u), where V is the host vector space, C the cone of states, and u the order
unit, we will often identify GPTs with said triples.

V
Ω
u=1

C
0
FIG. 1. The basic ingredients of a GPT are a real ﬁnite-dimensional vector space V and a cone C.
The order unit functional u deﬁnes a hyperplane u−1 (1), whose intersection with C identiﬁes the
state space Ω.

4

<!-- page 5 -->
u
V∗
effects
C∗

0
FIG. 2. The dual space V ∗ , comprising the dual cone C ∗ , the order unit u, and the set of eﬀects
deﬁned by the order interval [0, u] = {e ∈ V ∗ : 0 ⩽ e ⩽ u}.
B.

Universal definition of entanglement

Given that our GPT machinery is supposed to account for real physics, it is very natural
to wonder what it tells us as far as multipartite systems are concerned. Namely, given two
physical systems represented as GPTs A = (V1 , C1 , u1 ) and B = (V2 , C2 , u2 ), is there a way
to represent also the joint system as a GPT AB = (V12 , C12 , u12 )? Under some natural
assumptions on physical composites, it can be shown that vector spaces and order units
obey a simple tensor product rule [12, 13]:
V12 = V1 ⊗ V2 ,

u12 = u1 ⊗ u2 .

(1)

The main hidden hypothesis that leads to Eq. (1) is the local tomography principle, i.e. the
assumption that any state of the joint system is completely determined by the statistics it
yields under local measurements.
The status of the cone C12 is far more delicate. Some natural constraints come from the
requirement that convex combinations of product states be allowed as legitimate states of
the joint system, and – dually – that local measurement be allowed as legitimate measurements on the joint system. These considerations lead to the two-fold bound
C1  C2 ⊆ C12 ⊆ C1  C2 .

(2)

Here, C1  C2 is called the minimal tensor product, and contains product states and convex
combinations thereof. The maximal tensor product C1  C2 , instead, includes all those
tensors that are positive on product effects [14, 15]. In formulae,
C1  C2 := conv {x ⊗ y : x ∈ C1 , y ∈ C2 } ,
C1  C2 := {z ∈ V1 ⊗ V2 : (f ⊗ g)(z) ⩾ 0 ∀ f ∈ C1∗ , g ∈ C2∗ } ,
5

(3)
(4)

<!-- page 6 -->
where conv denotes the convex hull.
All cones satisfying (2) should be regarded as identifying a priori valid composition
rules. As there appears to be no general and indisputable physical principle that is capable
of singling out a special one among them, a sensible decision requires a deeper investigation
of the physics of the system under examination. In some sense, a composite is more than
the sum of its parts.
Example (Classical theories as GPTs). At this point it is instructive to discuss some
notable examples of GPTs. A classical theory has by definition a fixed (finite) number
d of perfectly distinguishable configurations ω1 , . . . , ωd , and its state is described by the
probabilities of it being in each of those configurations. This means that the state space Ω
has the geometric shape of
Pa simplex, and that the corresponding cone C, called a classical
cone, has the form C = { i λi ωi : λi ⩾ 0 ∀ i}, with {ωi }i being a vectorPbasis of the
Pspace
V . The order functional u encodes the normalisation, and it acts as u ( i xi ωi ) = i xi .
Classical theories are special as far as composites are concerned. In fact, it can be shown
that if C is a classical cone, then for all other cones C ′ one has that C  C ′ = C  C ′ , so
that the chain of inclusions in Eq. (2) collapses and leads to no ambiguity.
Example (Quantum mechanics as a GPT). An n-level quantum system can also be described by means of the GPT formalism. In this case, the host vector space V is simply
the real vector space Hn of n × n Hermitian matrices. Unnormalised states form the cone
PSDn of positive semidefinite matrices. Since physical states, a.k.a. density matrices, are
obtained by further normalising the trace to 1, we see that the order unit u is nothing but
the trace functional. We are thus left with the GPT QMn := (Hn , PSDn , Tr).
The quantum composition rule is easily expressed in words: the bipartite system obtained from an n-level and an m-level quantum system is simply an nm-level quantum
system. This definition is easily seen to satisfy Eq. (1), so we move on to Eq. (2). States
in the minimal tensor product are precisely those that do not exhibit entanglement, a.k.a.
separable states [16]. At the opposite end of the spectrum, Hermitian operators in the
maximal tensor product are known as entanglement witnesses [17, 18]. As is well known,
the cone PSDnm of physical quantum states pertaining to the bipartite system is neither of
the two: it includes entangled states that are not in PSDn  PSDm , such as the maximally
entangled state, yet it leaves out certain non-positive matrices that lie inside PSDn PSDm ,
e.g. the flip operator F [16]. Therefore, quantum theory demonstrates that a composition
rule that makes both inclusions in Eq. (2) strict may be the one prescribed by Nature.
By analogy with the quantum concept, for any two cones C1 , C2 we call elements of
C1  C2 separable and elements of C1  C2 that are not in C1  C2 entangled. Exactly
as in quantum mechanics, separable states of a bipartite GPT can be prepared with local
operations and shared randomness on separated systems. Observe that not all entangled
elements of C1  C2 necessarily represent legitimate states in the GPT interpretation, as it
6

<!-- page 7 -->
appears from Eq. (2). However, if it holds that
C1  C2 6= C1  C2 ,

(5)

then the corresponding GPTs must exhibit entanglement, either at the level of states or at
the level of measurements. In fact, Eq. (5) implies that every physically allowed cone C12
satisfying Eq. (2) is such that either C12 ) C1  C2 , i.e. there are entangled states, or
∗ ) C ∗  C ∗ , i.e. there are entangled measurements. A pair of cones (C , C ) is called
C12
1
2
2
1
entangleable if it satisfies Eq. (5). This notion of entangleability of physical theories as
modelled by GPTs – or, more generally, of entangleability of cones – plays a central role in
our work.
C.

Main question and findings

The fundamental question we investigate here concerns the connection between the notion of classicality defined in Example I B and the above notion of entangleability. The nature of such a connection is apparent in the quantum mechanical formalism: the possibility
of constructing superpositions of states at the single-system level, which is a manifestation
of non-classicality, directly implies the existence of entangled states in bipartite systems.
The problem we pose here is whether this implication is just an accident of quantum theory,
or on the contrary it is a universal feature of the general logical rules governing composition
of physical theories. Thanks to the discussion at the end of Subsection I B, we can formulate
the question in precise mathematical terms:
Which pairs of general probabilistic theories are entangleable? Mathematically, can we
characterise all entangleable pairs of proper cones?
The following easily established fact was mentioned above: if either C1 or C2 is a
classical cone, then the pair (C1 , C2 ) is not entangleable [19]. This corresponds to the
rather intuitive statement that classical systems cannot become entangled with any other
system. A partial converse to this was proved long ago by Namioka and Phelps: if a
cone C1 is such that (C1 , C2 ) is not entangleable for every other cone C2 , then C1 must
be classical [19]. This latter result is conceptually important because it provides a partial
answer to the above question. However, it does not allow us to conclude anything for a
single pair of theories, which is arguably the most significant case if one wants to establish
universality of entanglement as a physical phenomenon.
Our main results answer the above question for a wide class of GPTs that encompasses
most physically reasonable models. We start by looking at the simplest case of all, to wit,
that of two 3-dimensional GPTs. Besides being interesting on its own, its solution will turn
out to be critical to the understanding of more general cases.
Result 1. Let (C1 , C2 ) be two 3-dimensional cones. Then (C1 , C2 ) is entangleable if and
only if neither C1 nor C2 is classical.
7

<!-- page 8 -->
It has been proposed that due to the allegedly discrete nature of space-time [20], physical state spaces may themselves be ultimately discrete [21], meaning that the number of
accessible pure states in a finite-dimensional system may be finite. This would offer some
advantages on the interpretational side [22], although it would require modification of the
post-measurement collapse rule [10]. These speculations motivate us to answer the above
question for the special case of discrete state spaces. From the mathematical standpoint,
a state space hosting only a finite number of pure states is modelled by a convex set with
only finitely many extreme points, i.e. a polytope. The corresponding cone of states will
then be a polyhedral cone. Our next result then reads as follows.
Result 2. Let (C1 , C2 ) be two proper polyhedral cones. Then (C1 , C2 ) is entangleable if and
only if neither C1 nor C2 is classical.
We are also able to tackle the important special case of one of the two GPTs being
quantum theory. This problem has been considered before in [23–25], with an entirely
different motivation. Our next result improves upon [25, Theorem 4.1], answering our main
question in yet another case.
Result 3. Let PSDn be the cone of n × n positive semidefinite matrices. For a proper
cone C in dimension d, the pair (C, PSDn ) is entangleable if and only if C is not classical,
provided that ⌊log2 n⌋ ⩾ d−1
2 .
From Results 1–3 it is apparent that local non-classicality is intimately connected with
global entangleability, as we discuss more thoroughly below. So far, we have explored
this connection in a fundamentally qualitative way. However, it is also possible to ask
a quantitative version of our main question: given any two GPTs that are non-classical
to some quantifiable extent, can we estimate their degree of entangleability, that is, the
maximum possible entanglement exhibited by global states? Note that the answer will in
general depend on the measures we employ to gauge the global entanglement and the local
non-classicality. Although it is significantly more complex than its qualitative counterpart,
a solution to this problem can nevertheless be found for all those theories – called symmetric
– whose state space is centrally symmetric with respect to some centre. Classical theories of
dimension d > 2 are automatically ruled out by this assumption, which makes the problem
more tractable. However, in spite of its geometric appeal, central symmetry is perhaps not
a natural requirement from a physical perspective, as e.g. no quantum system besides that
of a single qubit has a symmetric state space. Yet, it is remarkable that a complete solution
can be found for such a general class of examples.
Result 4. Given any pair of symmetric GPTs of dimensions n+1, m+1 ⩾ 3, their maximal
tensor product contains a state whose entanglement robustness [26] is at least Erob (n, m) ⩾
(r(n, m) − 1)/2, where r(n, m) is the universal function called ‘projective/injective ratio’
and defined in [27, Eq. (15)]. In particular, Erob (n, m) ⩾ 1/36 for all n, m ⩾ 2, and
asymptotically Erob (n, m) ⩾ c min{n, m}1/8−o(1) for some constant c > 0. Hence, all pairs
8

<!-- page 9 -->
of symmetric GPTs are entangleable, with the maximal robustness of entanglement growing
unboundedly with the minimum local dimension.
Our conceptual contributions extend far beyond providing an answer to our main question in several physically interesting cases, which marks in itself some tangible progress in a
long-standing open problem. In fact, owing to their versatility and generality, the techniques
we develop constitute per se a significant step forward, both conceptually and mathematically. These techniques include e.g. an innovative use of the order-theoretic concept of
retract, which allows us to study constrained GPTs, a general framework to construct and
detect general entangled states in a bipartite GPT, and a systematic connection with a
recently developed functional-analytic theory of tensor norm ratios [27].
II.

DISCUSSION

Our Results 1–4 demonstrate that there is a profound connection between the notion
of non-classicality and that of entanglement. While it was long known that the former is
a necessary condition for the latter, we have proved that the two are actually equivalent
for a large class of cases of immediate interest for the foundations of physics. We have
shown that this connection goes far beyond quantum mechanics, and characterises instead
all theories that can be modelled within the GPT formalism. Let us remark in passing that
this type of model-independent approach to the study of operational features of physical
theories has a long history [9, 28–33]. For the case study of symmetric GPTs, we have
been able to make the aforementioned connection quantitative. What our results suggest
is that, in a bipartite system whose local components exhibit some non-classical behaviour,
entanglement of states or measurements becomes logically unavoidable. We can conjecture
that this is a fully general behaviour: all pairs of non-classical GPTs may be entangleable.
The mathematical translation of this conjecture is that all pairs of non-classical proper
cones may be entangleable. Interestingly, this same problem was formulated long ago by
Barker, with an entirely different and purely mathematical motivation, and has been open
since [34, 35]. We have provided the first convincing evidence that the above conjecture may
be true in general, proving it in the first nontrivial case of dimension 3 (Result 1) and for
polyhedral cones (Result 2). Remarkably, this question is already implicit in previous work
by Namioka and Phelps [19], of which Barker seem to have been unaware. The same sort of
problem was again rediscovered more recently, in a somewhat limited setting in which one
of the two theories is set to be quantum mechanics [23–25]. There, the motivation is again
entirely different, coming from operator system theory. Once reformulated in our language,
the results from [23–25] state that: (a) for a given polyhedral cone C, the pair (C, PSDn ) is
entangleable if and only if C is non-classical; (b) for any cone C in a d-dimensional space,
provided that log2 n ⩾ d − 2, it holds that (C, PSDn ) is entangleable if and only if C is
non-classical. Our techniques lead to a more direct proof of (a), as well as showing that (b)
holds under the weaker condition ⌊log2 n⌋ ⩾ (d − 1)/2 (Result 3).
9

<!-- page 10 -->
From the mathematical standpoint, our main question connects very naturally to the
problem of evaluating the minimal constant of domination of the injective over the projective
tensor norm for Banach spaces of fixed local dimensions [27]. In fact, given any finitedimensional Banach space, we can construct a GPT by declaring its unit ball to be our
state space [8, § 2.3.3]. The entanglement robustness of certain bipartite states can then
be expressed by means of the ratio between projective and injective tensor norm of the
corresponding tensors. Consequently, the maximum entanglement robustness in a bipartite
system is directly linked to the constant of domination of the latter over the former norm,
which can be estimated using the techniques of [27] (Result 4).
Result 4 is affected by the geometrically natural yet physically questionable restriction
to symmetric models, and should therefore be regarded more as the starting point of a
quantitative investigation of our main question. Ultimately, we envision the existence of a
general lower bound on the minimal amount of entanglement in the maximal tensor product
of two GPTs in terms of their local non-classicality. To prove such a statement one would
need to construct: (i) a suitable measure of non-classicality, i.e. a functional ν that assigns
to every GPT A = (V, C, u) a non-negative real number ν(A), in such a way that ν(A) = 0
if and only if C is a classical cone; and (ii) a general measure of entanglement for bipartite
states in GPTs, i.e. a function E that, given two local GPTs A, B, assigns a non-negative real
number E(ωAB ) to every state ωAB in the state space ΩAB corresponding to the maximal
tensor product of the cones, in such a way that E(ωAB ) = 0 if and only if ωAB ∈ ΩAB
is a separable state. Within this framework, a quantitative relation between local nonclassicality and global entanglement would read
max

ωAB ∈ ΩAB

E(ωAB ) ⩾ F (ν(A), ν(B)) ,

(6)

where F : R+ × R+ → R+ is some universal function with the property that F (x, y) =
0 only when either x or y equals 0. In the statement of Result 4 we chose as E the
entanglement robustness [26, 36]. We believe that of all entanglement measures constructed
in the field of quantum information [37], the entanglement robustness stands out as a natural
candidate to appear in Eq. (6), as it relies only on the convex character of the theory, and
as such it carries over swiftly to the GPT formalism. On the contrary, we do not yet have
such a clear ansatz for the non-classicality measure ν.
The problem we study here admits many possible variations. For instance, a stronger
question to ask would be whether in any pair of non-classical GPTs one can violate a Bell
inequality [8, Definition 2.14]. Since Bell inequalities can be violated only by entangled
states, this would immediately imply that the two GPTs are entangleable. Solving such
a problem would lead us to the stronger conclusion that the entanglement exhibited by
non-classical theories can also be experimentally accessed in the form of some non-local
correlations, thus enabling device-independent information theory in GPTs [3]. A quantitative answer to this question would translate to an inequality analogous to Eq. (6), with
a measure of non-locality such as the maximal violation of a CHSH-type inequality [38] or
10

<!-- page 11 -->
other more general measures (see e.g. [39]) displacing the entanglement measure E. For
some partial results in this direction, see e.g. [8, Theorem 2.39], which builds upon previous
works [40–42].
III.

METHODS

In this section we discuss the proof ideas of Results 1–4. For a complete presentation
with all the technical details, we refer the reader to the Supplementary Information.
A.

Technical background

As discussed above, a GPT is a triple (V, C, u), where V is a finite-dimensional real
vector space, C ⊂ V is a proper cone, and u ∈ int(C ∗ ) is a strictly positive functional
on C. A subset C ⊆ V is called a cone if λC = C for all λ > 0; a cone is said to be
salient if C ∩ (−C) = {0}, generating if C − C = span(C) = V , and proper if it is convex,
topologically closed, salient,
P and generating. A classical cone C is one that is generated by
a basis of V , i.e. C = { i λi ei : λi ⩾ 0 ∀ i} for some basis {ei }i . Any proper cone C ⊂ V
can be declared to be the set of positive vectors of V and thus induces an ordering on
V . Positive functionals in the dual space V ∗ form the dual cone C ∗ . If C is proper, then
C ∗∗ = C modulo the identification V ∗∗ = V .
Two cones C1 , C2 can be combined according to either the minimal or the maximal
tensor product, defined in Eq. (3) and (4), respectively. Observe that C1  C2 ⊆ C1  C2 ,
because products of positive functionals take on positive values when evaluated on products
of positive vectors. Remember that we call the pair (C1 , C2 ) entangleable if this inclusion
is strict. The following easily verified and well-known fact [34, 35] is a cornerstone of our
intuition concerning these products, so we present a proof for the benefit of the reader.
Lemma 5. Let C1 , C2 be proper cones, at least one of which is classical. Then (C1 , C2 ) is
not entangleable.
Proof. Assume that C1 is generated by a basis {ei }i of V1 , and consider the dual P
basis {e∗i }i
of V1∗ , which satisfies e∗i (ej ) = δi,j . Decompose an arbitrary z ∈ C1  C2 as z = i ei ⊗ xi ,
where xi ∈ V2 . By definition of maximal tensor product, for every f ∈ C2∗ we have that
0 ⩽ (e∗i ⊗ f )(z) = f (xi ) for all i. This shows that xi ∈ C2∗∗ = C2 , where we used the fact
that C2 is proper. Hence, z ∈ C1  C2 , and consequently C1  C2 = C1  C2 .
B.

Proof of Result 1

Here we shall prove that any pair (C1 , C2 ) of non-classical 3-dimensional proper cones
is entangleable. Our strategy can be summarised as follows.
11

<!-- page 12 -->
(i) We will apply linear isomorphisms Φi to bring both cones Ci into ‘standard’ forms,
for which we can find simpler cones Ci′ , Ci′′ such that Ci′ ⊆ Φi (Ci ) ⊆ Ci′′ . Note that
(C1 , C2 ) is entangleable if and only if (Φ(C1 ), Φ(C2 )) is such.
(ii) We will then lower bound C1  C2 ⊇ C1′  C2′ , and upper bound C1  C2 ⊆ C1′′  C2′′ .
Assuming by contradiction that C1 C2 ⊆ C1 C2 , it follows that C1′ C2′ ⊆ C1′′ C2′′ .
(iii) However, using the relatively simple structure of Ci′ , Ci′′ , we will explicitly show that
C1′  C2′ ( C1′′  C2′′ .
A natural way to construct a cone is through one of its sections. Namely, given a convex
set K ⊆ V , let us define the cone
C (K) = {(tx, t) : x ∈ K, t ∈ R+ } ⊆ V × R .

(7)

One can verify that C (K) is a proper cone if and only if K ⊂ V is a convex body (compact
convex set with non-empty interior), and that it is non-classical if and only if K is not a
simplex. Moreover, every proper cone in dimension d is linearly isomorphic to C (K) for
some (d − 1)-dimensional convex body K.2 In our case, to generate 3-dimensional cones
we need to look at 2-dimensional convex bodies K, which allows us to use good old planar
geometry to tackle the problem. We start by defining two special convex sets: the kite with
centre (a, b) (where −1 < a, b < 1) is constructed as
Ta,b := conv{(a, ±1), (±1, b)};

(8)

the blunt square, instead, is simply the unit square without its corners:
S = [−1, 1]2 \ {−1, 1}2 .

(9)

For a pictorial representation of these two sets, see Figure 3.
The reason why we are interested in kites and blunt squares is that, apart from triangles,
any 2-dimensional convex set can be inscribed between one and the other by the application
of a suitable linear isomorphism. This analogue of Auerbach’s lemma [43, Vol I, § 1.c.3] for
2-dimensional convex bodies can be formalised as follows.
Proposition 6. Let V be a 3-dimensional vector space, and C ⊂ V a proper cone which is
not classical. There exist (a, b) ∈ (−1, 1)2 and a linear bijection Φ : V → R2 × R such that
C (Ta,b ) ⊆ Φ(C) ⊆ C (S).
2

We already knew this from the GPT setting: we used proper cones in the definition of a GPT precisely
because they admit suitable sections – namely, state spaces.

12

<!-- page 13 -->
(a, 1)
•

(−1, 1)

S
(−1, b) •

Ta,b

• (1, b)

•
(a, −1)

(−1, −1)

(1, 1)

(1, −1)

FIG. 3. The kite Ta,b and the blunt square S, deﬁned in Eq. (8) and (9), respectively.

We refer to the Supplementary Information for a proof. By the discussion at the beginning of the section, it should be clear that a statement such as Proposition 6 allows to focus
our effort on the pairs of lower and upper bounds rather than on the original cones. The
main technical contribution of this section completes the analysis by studying the properties
of minimal and maximal tensor products of cones generated by kites and blunt squares.
Proposition 7. Take four numbers −1 < a1 , a2 , b1 , b2 < 1. Then
C (Ta1 ,b1 )  C (Ta2 ,b2 ) 6⊆ C (S)  C (S).

(10)

In other words, there exists ω ∈ C (Ta1 ,b1 )  C (Ta2 ,b2 ) such that ω 6∈ C (S)  C (S).

The proof of Proposition 7 is constructive: we exhibit an explicit tensor ω ∈ R3 ⊗ R3
and show that it belongs to C (Ta1 ,b1 )  C (Ta2 ,b2 ) but not to C (S)  C (S). The former fact
can be proved by a direct computation. For the latter, instead, we construct a Bell-type
expression that is strictly less than 2 on the whole C (S)  C (S), yet it evaluates precisely
to 2 on ω. With these tools at hands, we are now in position to prove our first main result.
Proof of Result 1. Considering two 3-dimensional non-classical proper cones C1 , C2 , we
show by contradiction that the pair (C1 , C2 ) is entangleable. Up to the application of local
linear isomorphisms on C1 , C2 , and using Proposition 6, we may assume that
C (Ta1 ,b1 ) ⊆ C1 ⊆ C (S) and C (Ta2 ,b2 ) ⊆ C2 ⊆ C (S)

(11)

for some numbers −1 < a1 , a2 , b1 , b2 < 1. Since  and  are increasing operations with
respect to set inclusion, it follows that
C (Ta1 ,b1 )  C (Ta2 ,b2 ) ⊆ C1  C2 = C1  C2 ⊆ C (S)  C (S),
which contradicts the conclusion of Proposition 7.
13

(12)

<!-- page 14 -->
C.

Proof of Result 2

Throughout this section we will prove that all pairs of non-classical polyhedral cones are
entangleable.
We call a cone C polyhedral if there are finitely many vectors {vi }i such that
P
C = { i λi vi : λi ⩾ 0 ∀ i}. One of the main tools we employ here is the concept of retract.
Given two vector spaces V, V ′ ordered by proper cones C, C ′ , a linear map Φ : V → V ′ is
called positive if Φ(C) ⊆ C ′ . We then say that C ′ is a retract of C if there are positive
maps Φ : V → V ′ and Ψ : V ′ → V such that Φ ◦ Ψ = IdV ′ . When this happens, C ′ can
be seen as a sub-cone of C that is also the image of a positive projection. For example, we
shall see that facets of polyhedral cones are always retracts.
To appreciate the importance of retracts for the study of entangleability, we first need
to familiarise ourselves with the transformation properties of minimal and maximal tensor
products under local positive maps. Consider cones Ci ⊆ Vi and positive maps Φi : Vi → Vi′
(i = 1, 2). Then
(Φ1 ⊗ Φ2 ) (C1  C2 ) ⊆ Φ1 (C1 )  Φ2 (C2 ) ,

(Φ1 ⊗ Φ2 ) (C1  C2 ) ⊆ Φ1 (C1 )  Φ2 (C2 ) .

(13)
(14)

The former inclusion can be verified directly by means of the decomposition of tensors
in C1  C2 . As for the latter, take z ∈ C1  C2 and a pair of functionals fi such that
fi (Φi (xi )) ⩾ 0 for all xi ∈ Ci . Using the concept of adjoint map,3 we can express this
condition as Φ∗i (fi ) ∈ Ci∗ , where Ci∗ is the dual cone to Ci . Hence,
(f1 ⊗ f2 ) ((Φ1 ⊗ Φ2 ) (z)) = (Φ∗1 (f1 ) ⊗ Φ∗2 (f2 )) (z) ⩾ 0 ,
which proves Eq. (14).

Proposition 8 (Entangleability from retracts). For i = 1, 2, let Ci ⊂ Vi be proper cones
with retracts Ci′ ⊂ Vi′ . If (C1′ , C2′ ) is entangleable, then so is (C1 , C2 ).
Proof. Let us denote by Φi : Vi → Vi′ and Ψi : Vi′ → Vi the linear maps associated to the
corresponding retracts. Assume that (C1 , C2 ) is not entangleable, so that C1 C2 = C1 C2 .

3

The adjoint of a linear map Φ : V → W is the linear map Φ∗ : W ∗ → V ∗ , where V ∗ , W ∗ are the dual
spaces to V, W , uniquely defined by (Φ∗ f )(x) ≡ f (Φ(x)), for all x ∈ V and f ∈ W ∗ .

14

<!-- page 15 -->
Then
C1′  C2′ = ((Φ1 ◦ Ψ1 ) ⊗ (Φ2 ◦ Ψ2 )) C1′  C2′
(i)


⊆ (Φ1 ⊗ Φ2 ) Ψ1 (C1′ )  Ψ2 (C2′ )



(ii)

⊆ (Φ1 ⊗ Φ2 ) (C1  C2 )

(iii)

= (Φ1 ⊗ Φ2 ) (C1  C2 )

(iv)

⊆ Φ1 (C1 )  Φ2 (C2 )

(v)

⊆ C1′  C2′ .

Note that (i) comes from Eq. (14), (ii) from the positivity of Ψi , (iii) from the unentangleability of (C1 , C2 ), (iv) from Eq. (13), and finally (v) from the positivity of Φi . Since we
have shown that C1′  C2′ ⊆ C1′  C2′ and the opposite inclusion is trivial, we conclude that
(C1′ , C2′ ) is not entangleable.
A possible strategy for demonstrating the entangleability of a pair of cones is then as
follows: if we are able to exhibit two local retracts that are entangleable, then Proposition 8
guarantees that so were the original cones. In the case of polyhedral cones, the job of finding
retracts is facilitated by the following lemma.
Lemma 9. Let F be a facet of a proper polyhedral cone C. Then F is a retract of C.
The main idea of the proof of Lemma 9 is that it is always possible to ‘illuminate’ a
polyhedral cone with a collinear beam in such a way that its whole shadow lies inside one
of its facets. The rigorous proof is relegated to the Supplementary Information. We now
move on to the other main ingredient of the proof.
Lemma 10. Let C be a non-classical proper polyhedral cone with dim(C) ⩾ 4. Then either
C or its dual C ∗ has a facet which is non-classical.
Before we can apply Lemma 10 to our setting, we need to observe that retracts dualise.
This means that C1 is a retract of C2 if and only if C1∗ is a retract of C2∗ , for all pairs of
proper cones C1 , C2 .
Proof of Result 2. Let C1 , C2 be non-classical proper polyhedral cones. Let us assume that
e.g. d1 := dim(C1 ) ⩾ 4, otherwise the claim follows from Result 1. Thanks to Lemma 10,
either C1 or C1∗ has a non-classical facet. Then, by Lemma 9 either C1 or C1∗ has a nonclassical retract of dimension d1 − 1, which is naturally another proper polyhedral cone.
Since retracts dualise, these two facts are actually equivalent. Hence C1 has a non-classical
proper polyhedral retract of dimension d1 − 1. Continuing in this way, we can reduce the
dimensions d1 and d2 of C1 and C2 , until we achieve d1 = d2 = 3. The statement then
follows from Result 1.
15

<!-- page 16 -->
D.

Proof of Result 3

In this section we consider pairs of cones, where one element of the pair is the cone
PSDn of n × n positive semidefinite matrices with complex entries. In other words, we look
at bipartite systems AB, where system A is described by usual quantum mechanics and
system B is an arbitrary GPT.
Remarkably, the problem of whether such a pair of cones is entangleable is equivalent to
a recently emerged question about operator systems, formulated either in terms of operator
systems or of matrix convex sets. Before presenting our methods, we quickly review this
connection. The content of the next paragraph is not essential to the understanding of the
proof of Result 3.
As explained in [23, 25], an operator system in d variables can be described by a sequence
W = (Wn )n⩾1 of proper cones, where Wn lives in the space Hdn of d-tuples of n × n
matrices. Such a sequence is asked to satisfy compatibility conditions under the action
of completely positive maps. As it turns out, given a proper cone W ⊂ Rd , there is
a minimal operator system W min and a maximal operator system W max satisfying the
condition W1min = W1max = W . This means that any operator system (Wn ) such that
W1 = W must satisfy Wnmin ⊆ Wn ⊆ Wnmax . Moreover, the minimal and maximal operator
systems are constructed using the minimal and maximal tensor product:
Wnmin = PSDn  W,
Wnmax = PSDn  W.
A major result in [25] is the proof of the fact that the equality W max = W min between
operator systems (i.e. between sequences of cones) is equivalent to the starting cone W
being classical. In other words, any non-classical theory, when coupled with quantum
mechanics QMn for n large enough, forms an entangleable pair. Our Result 3 lowers the
value of n needed to guarantee entangleability, coming closer to the conjectured value n = 2.
Our proof of Result 3 relies on an extremal property of the simplex in convex geometry:
the simplex is the convex shape which is most different from the round ball. Here is a precise
formulation of this property. We denote by Bd the unit ball in the standard Euclidean space
Rd . Given a convex body K ⊂ Rd , one defines its asphericity a(K) as the ratio between
the radii of inscribed and circumscribed homothetic Euclidean balls, after preprocessing by
applying a suitable affine map
a(K) := inf{r > 1 : there is an affine map Φ : Rd → Rd such that Bd ⊆ Φ(K) ⊆ rBd }.
The minimal value a(K) = 1 of the asphericity corresponds to the case when K is an
ellipsoid, i.e. an affine image of Bd . At the other side of the spectrum, the maximal value
of asphericity is achieved for simplices.
Theorem 11 (Simplices maximize asphericity). Any convex body K ⊂ Rd satisfies the
inequality a(K) ⩽ d. Moreover, a(K) = d if and only if K is a simplex.
16

<!-- page 17 -->
The first part of Theorem 11 is well-known [44], while the second part was proved in [45]
and later rediscovered in [46].
Since the asphericity is defined by comparison with a Euclidean ball, the cones over
a Euclidean ball with different radii play a central role when applying Theorem 11. We
introduce them as Lorentz cones, defined for r > 0 as


q
d+1
2
2
:=
Ld (r)
(x1 , . . . , xd+1 ) ∈ R
: x1 + · · · + xd ⩽ rxd+1 .
Note that Ld (r) is the cone over the ball rBd , and is thus symmetric in the sense of Section III E.
Lemma 12. The inclusion Ld (1)  Ld (1) ⊆ Ld (1)  Ld (r) holds if and only if r ⩾ d.
We only give here intuition behind the critical value r = d which appears in Lemma 12,
and refer to the Supplementary Information for a complete proof. The minimal tensor
product of Lorentz cones is intimately connected with the operator norm k·k∞ on matrices,
and similarly the maximal tensor product of Lorentz cones is connected with the trace norm
k · k1 . It is well known that the inequalities
k · k∞ ⩽ k · k1 ⩽ dk · k∞

(15)

hold for d × d matrices, and that the value d cannot be changed into a smaller number.
This can be shown by plugging in Eq. (15) the identity matrix. This is the primary reason
for the appearance of the value d in Lemma 12.
Our approach to prove Result 3 uses another ingredient, which relates the Lorentz cone
with the cone of positive semidefinite matrices. As in the proof of Result 2, retracts are a
key concept.
Proposition 13. If d ⩽ 2n, then the cone Ld is a retract of PSD2n .
The construction behind Proposition 13 is based on a well-known fact: one can find
2n trace zero unitary matrices of size 2n which pairwise anticommute. This can be either
derived from the theory of Clifford algebras, or constructed by hand as tensor products of
Pauli matrices.
Proof of Result 3. The fact that classicality prevents entangleability is the easy direction
(Lemma 5). Therefore, consider a pair (C, PSDn ), where C is a cone in dimension d+1, and
let us show that this pair is entangleable provided that C is non-classical and ⌊log2 n⌋ ⩾ d/2.
Thanks to Proposition 13, we know that in this case Ld is a retract of PSDn . Using the
connection between entangleability and retracts explained in Proposition 8, we obtain that
the pair (C, Ld ) is not entangleable either.
Now, let K be a d-dimensional convex body which is a base of the cone C, and denote
with r := a(K) its asphericity. If we replace K by a suitable affine image (which changes
17

<!-- page 18 -->
neither the geometry nor the entangleability properties of the cone C), we may assume that
Bd ⊆ K ⊆ rBd , or equivalently that Ld (1) ⊆ C ⊆ Ld (r). We now write
(i)

(ii)

(iii)

Ld (1)  Ld (1) ⊆ Ld (1)  C = Ld (1)  C ⊆ Ld (1)  Ld (r),

(16)

where (i) and (iii) follow from the fact that  and  are increasing operations with respect
to set inclusion, and (ii) expresses the unentangleability of the pair (C, Ld ). By Lemma 12,
the inclusion Ld (1)  Ld (1) ⊆ Ld (1)  Ld (r) implies that r ⩾ d. This means that K has
asphericity at least d. By Theorem 11, this is only possible if K is a d-dimensional simplex,
and therefore the corresponding cone C is classical.

E.

Proof of Result 4

Consider a GPT (V, C, u) whose state space Ω is symmetric with respect to a centre
γ ∈ Ω. We can decompose the vector space V as V = R ⊕ X, where X := ker(u) is the
kernel of u. The state space defines a norm on X through the choice BX := Ω − γ ⊂ X
for the unit ball. Accordingly, every state can be written as ω = γ + x, where x ∈ X
satisfies kxkX ⩽ 1. We can define the projection Π : V → X onto X via the formula
Π(v) := v − u(v)γ, so that with the above notation Π(ω) = x.
From the above discussion it appears that there is a natural connection between normed
spaces and symmetric proper cones. Since we want to understand the properties of the
latter under tensor products, we need to first review the known properties of the former.
Given two finite-dimensional normed vector spaces X, Y , there are at least two canonical
norms that these induce on the tensor product X ⊗ Y , namely, the injective tensor norm
k · kX⊗ε Y and the projective tensor norm k · kX⊗π Y . For an arbitrary z ∈ X ⊗ Y , these are
given by [47]
kzkX⊗ε Y := sup {(f ⊗ g)(z) : f ∈ BX ∗ , g ∈ BY ∗ } ,
o
nX
X
kxi kX kyi kY : z =
xi ⊗ y i .
kzkX⊗π Y := inf
i

i

(17)
(18)

Here, BX ∗ denotes the unit ball of the dual space X ∗ , whose corresponding norm is defined
(x)|
.
by the expression kf kX ∗ := supx∈X\{0} |fkxk
It is not difficult to verify directly that the inequality k · kX⊗ε Y ⩽ k · kX⊗π Y holds in
full generality, with equality for product tensors. Moreover, since the space X ⊗ Y is finitedimensional, and all norms on a finite-dimensional space are equivalent, there will exist a
constant ρ(X, Y ), which depends only on X and Y , which makes the opposite inequality
also true: k · kX⊗π Y ⩽ ρ(X, Y )k · kX⊗ε Y . The minimal such constant across all normed
spaces of fixed dimension n, m is a universal function of these two integers alone, called the
projective/injective ratio and denoted by r(n, m). By definition, for every pair of normed
18

<!-- page 19 -->
spaces X and Y of dimensions dim X = n and dim Y = m, there exists a tensor z ∈ X ⊗ Y
with kzkX⊗ε Y = 1 such that
kzkX⊗π Y ⩾ r(n, m)kzkX⊗ε Y = r(n, m) .

(19)

The function r(n, m) was defined and studied in [27], whose results find here a novel application. Let us stress that it is not even clear a priori that one should have r(n, m) > 1 for
all n, m > 1. That this indeed is the case was one of the main findings of [27].
Since injective and projective tensor norms always coincide on product tensors, we may
conjecture that any tensor z such that kzkX⊗π Y > kzkX⊗ε Y may in fact be ‘entangled’ in
some sense. To make this statement rigorous and quantitative, we need two ingredients:
(i) an entanglement measure for states of a bipartite GPT; and (ii) a systematic way
of evaluating such a measure in terms of tensor norms. To address (i) we look at the
entanglement robustness, which was defined in [26] for quantum states, and that we can
immediately extend to the GPT setting [36]. Let (V1 , C1 , u1 ) and (V2 , C2 , u2 ) be two GPTs.
For a candidate bipartite state ω ∈ C1  C2 , the entanglement robustness is defined as the
minimal amount of separable noise that makes a state separable, in formula
Erob (ω) := min {(u1 ⊗ u2 )(ζ) : ζ, ω + ζ ∈ C1  C2 } .

(20)

We believe that this entanglement measure, whose definition is rooted in convex geometry
alone, is the natural choice in the context of GPTs. To complete our programme we need
to tackle problem (ii) above. This is done by means of the following lemma.
Lemma 14. Let (V1 , C1 , u1 ), (V2 , C2 , u2 ) be two symmetric GPTs. Call γ1 , γ2 the centres
of the state spaces, and X1 , X2 the associated normed spaces. For z ∈ X1 ⊗ X2 , consider
the normalised state ω(z) := γ1 ⊗ γ2 + z. Whenever z satisfies kzkX1 ⊗ε X2 ⩽ 1, it holds that
ω(z) ∈ C1  C2 . In this case,
Erob (ω(z)) ⩾

kzkX1 ⊗π X2 − 1
.
2

(21)

We are finally ready to prove Result 4.
Proof of Result 4. Consider a pair of symmetric GPTs of dimensions n + 1, m + 1 ⩾ 3.
Combining Eq. (S25) and Eq. (19), we see that there is a normalised state ω in the maximal
tensor product C1  C2 such that
Erob (ω) ⩾

r(n, m) − 1
.
2

(22)

The claim follows from the estimates r(n, m) ⩾ 19/18 [27, Theorem 2], valid for all n, m ⩾ 2,
and r(n, m) ⩾ c min{n, m}1/8−o(1) [27, Theorem 6], valid in the limit n, m → ∞.
19

<!-- page 20 -->
IV.

CONCLUSIONS

In this work, we defined and studied the model-independent notion of universal entanglement in the context of general probabilistic theories. We have shown that the failure of
the local state spaces to have the geometric shapes of simplices, which is a manifestation of
the existence of superpositions, is intimately connected with the existence of entanglement
at the level of bipartite states or measurements. This connection, which before was thought
of as an accident of the quantum formalism, is elevated here to a foundational status. In
fact, our main conjecture states that all pairs of non-classical GPTs can be entangled by
composition.
A mathematically equivalent version of this problem is already implicit in the work of
Namioka and Phelps [19], and was systematically studied in the 1970s by Barker [34, 35].
It consists in proving that all pairs of non-classical cones are such that the maximal tensor
product is strictly larger than the minimal. The motivation driving all these previous efforts
was of a fundamentally order-theoretical nature, and not related to entangleability of GPTs.
We presented strong evidence in favour of our main conjecture, proving it in a number of physically relevant cases. Namely, we showed that it is true when both cones are
3-dimensional (Result 1) or polyhedral (Result 2), and also when one of the local theories
is quantum mechanics on a Hilbert space of a sufficiently large dimension (Result 3). We
also took one step further and put forth a quantitative extension of the above qualitative
conjecture. Namely, we proposed that the maximal entanglement exhibited by a pair of
theories may be lower bounded by a universal function of their departure from classicality,
as measured by an appropriate quantifier. We presented evidence in support of this hypothesis, proving it for the geometrically vast class of symmetric cones (Result 4). We briefly
discussed further extensions of this approach to non-locality in bipartite GPT systems.
On the mathematical side, our results mark the first progress on the conjecture since the
work of Barker, more than 40 years ago. Moreover, our methods are substantially innovative: we put to good use the order-theoretic concept of retract, devised general techniques to
construct entangled states in bipartite GPTs, and further investigated connections between
functional analysis and general probabilistic theories, as already developed in [27, 32].
In conclusion, our work sheds new light on a seemingly accidental connection between
the notions of local superposition and global entanglement, promoting it to a logically
unavoidable implication. This prompts us to reconsider the status of entanglement as a
fundamental ingredient of Nature.

ACKNOWLEDGEMENTS

We thank Andreas Winter and Stanisław Szarek for many enlightening discussions, and
Martin Plávala for suggesting using the concept of a retract. This work was partly achieved
during our visit in Institut Henri Poincaré, which we thank for hospitality. GA was sup20

<!-- page 21 -->
ported in part by ANR (France) under the grant StoQ (2014-CE25-0003). LL acknowledges financial support from the European Research Council (ERC) under the Starting
Grant GQCOP (Grant no. 637352). CP is partially supported by the Spanish ‘Ramón y
Cajal Programme’ (RYC-2012-10449), the Spanish ‘Severo Ochoa Programme’ for Centres
of Excellence (SEV-2015-0554) and the grant MTM2017-88385-P, funded by Spanish MEC.

[1] A. Einstein, B. Podolsky, and N. Rosen. Can quantum-mechanical description of physical
reality be considered complete? Phys. Rev., 47:777–780, 1935.
[2] J.S. Bell. On the Einstein-Podolsky-Rosen paradox. Physics, 1(3):195–200, 1964.
[3] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner. Bell nonlocality. Rev. Mod.
Phys., 86(2):419, 2014.
[4] A. Aspect, J. Dalibard, and G. Roger. Experimental test of Bell’s inequalities using timevarying analyzers. Phys. Rev. Lett., 49:1804–1807, 1982.
[5] R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki. Quantum entanglement. Rev.
Mod. Phys., 81:865–942, 2009.
[6] G. Ludwig. Versuch einer axiomatischen Grundlegung der Quantenmechanik und allgemeinerer
physikalischer Theorien. Z. Phys., 181(3):233–260, 1964.
[7] G. Ludwig. An Axiomatic Basis for Quantum Mechanics: Derivation of Hilbert space structure,
volume 1. Springer-Verlag, 1985.
[8] L. Lami. Non-classical correlations in quantum mechanics and beyond. PhD thesis, Universitat
Autònoma de Barcelona, 2017. Preprint arXiv:1803.02902.
[9] H. Barnum, J. Barrett, M. Leifer, and A. Wilce. Teleportation in general probabilistic theories.
In Proc. Sympos. Appl. Math., volume 71, pages 25–48, 2012.
[10] C. Pﬁster and S. Wehner. An information-theoretic principle implies that any discrete physical
theory is classical. Nat. Commun., 4:1851, 2013.
[11] P. Janotta and R. Lal. Generalized probabilistic theories without the no-restriction hypothesis.
Phys. Rev. A, 87:052131, 2013.
[12] M. Kläy, C. Randall, and D. Foulis. Tensor products and probability weights. Int. J. Theor.
Phys., 26(3):199–219, 1987.
[13] A. Wilce. Tensor products in generalized measure theory. Int. J. Theor. Phys., 31(11):1915–
1928, 1992.
[14] A.L. Peressini and D.R. Sherbert. Ordered topological tensor products. Proc. London Math.
Soc., s3-19(1):177–190, 1969.
[15] A. Hulanicki and R.R. Phelps. Some applications of tensor products of partially-ordered linear
spaces. J. Funct. Anal., 2(2):177–201, 1968.
[16] R.F. Werner. Quantum states with Einstein-Podolsky-Rosen correlations admitting a hiddenvariable model. Phys. Rev. A, 40:4277–4281, 1989.
[17] M. Horodecki, P. Horodecki, and R. Horodecki. Separability of mixed states: necessary and
suﬃcient conditions. Phys. Lett. A, 223(1–2):1–8, 1996.
[18] B.M. Terhal. Bell inequalities and the separability criterion. Phys. Lett. A, 271(5):319 – 326,
2000.
[19] I. Namioka and R.R. Phelps. Tensor products of compact convex sets. Pacific J. Math.,
31(2):469–480, 1969.

21

<!-- page 22 -->
[20] R.P. Feynman. Simulating physics with computers. Int. J. Theor. Phys., 21(6):467–488, 1982.
[21] R.V. Buniy, S.D.H. Hsu, and A. Zee. Is Hilbert space discrete? Phys. Lett. B, 630(1):68–72,
2005.
[22] R.V. Buniy, S.D.H. Hsu, and A. Zee. Discreteness and the origin of probability in quantum
mechanics. Phys. Lett. B, 640(4):219–223, 2006.
[23] T. Fritz, T. Netzer, and A. Thom. Spectrahedral containment and operator systems with
ﬁnite-dimensional realization. SIAM J. Appl. Algebra Geom., 1(1):556–574, 2017.
[24] B. Huber and T. Netzer. A note on non-commutative polytopes and polyhedra. Preprint
arXiv:1809.00476, 2018.
[25] B. Passer, O.M. Shalit, and B. Solel. Minimal and maximal matrix convex sets. J. Funct.
Anal., 274(11):3197–3253, 2018.
[26] G. Vidal and R. Tarrach. Robustness of entanglement. Phys. Rev. A, 59(1):141, 1999.
[27] G. Aubrun, L. Lami, C. Palazuelos, S.J. Szarek, and A. Winter. Universal gaps for XOR games
from estimates on tensor norm ratios. Preprint arXiv:1809.10616, 2018.
[28] S. Popescu and D. Rohrlich. Quantum nonlocality as an axiom. Found. Phys., 24(3):379–385,
1994.
[29] H. Barnum, J. Barrett, M. Leifer, and A. Wilce. Generalized no-broadcasting theorem. Phys.
Rev. Lett., 99(24):240501, 2007.
[30] J. Barrett. Information processing in generalized probabilistic theories. Phys. Rev. A,
75(3):032304, 2007.
[31] H. Barnum, O.C.O. Dahlsten, M. Leifer, and B. Toner. Nonclassicality without entanglement
enables bit commitment. In Information Theory Workshop, 2008. ITW’08. IEEE, pages 386–
390. IEEE, 2008.
[32] L. Lami, C. Palazuelos, and A. Winter. Ultimate data hiding in quantum mechanics and
beyond. Commun. Math. Phys., 361(2):661–708, 2018.
[33] J. Sikora and J. Selby. Simple proof of the impossibility of bit commitment in generalized
probabilistic theories using cone programming. Phys. Rev. A, 97:042302, 2018.
[34] G.P. Barker. Monotone norms and tensor products. Linear Multilinear Algebra, 4(3):191–199,
1976.
[35] G.P. Barker. Theory of cones. Linear Algebra Appl., 39:263–291, 1981.
[36] R. Takagi and B. Regula. General resource theories in quantum mechanics and beyond: operational characterization via discrimination tasks. Preprint arXiv:1901.08127, 2019.
[37] M. Hayashi. Quantum Information Theory: Mathematical Foundation. Graduate Texts in
Physics. Springer Berlin Heidelberg, 2016.
[38] J.F. Clauser, M.A. Horne, A. Shimony, and R.A. Holt. Proposed experiment to test local
hidden-variable theories. Phys. Rev. Lett., 23:880–884, 1969.
[39] C. Palazuelos. On the largest Bell violation attainable by a quantum state. J. Funct. Anal.,
267(7):1959–1985, 2014.
[40] M.M. Wolf, D. Perez-Garcia, and C. Fernandez. Measurements incompatible in quantum theory cannot be measured jointly in any other no-signaling theory. Phys. Rev. Lett., 103:230402,
2009.
[41] M. Banik, Md.R. Gazi, S. Ghosh, and G. Kar. Degree of complementarity determines the
nonlocality in quantum mechanics. Phys. Rev. A, 87:052125, 2013.
[42] A. Jenčová. Non-classical features in general probabilistic theories. Preprint arXiv:1705.08008,
2017.

22

<!-- page 23 -->
[43] J. Lindenstrauss and L. Tzafriri. Classical Banach spaces I and II, volume 97. Springer-Verlag,
1977.
[44] Fritz John. Extremum problems with inequalities as subsidiary conditions. R. Courant Anniversary Volume, pages 187–204, 1948.
[45] K. Leichtweiss. Über die aﬃne Exzentrizität konvexer Körper. Arch. Math., 10:187–199, 1959.
[46] O. Palmon. The only convex body with extremal distance from the ball is the simplex. Israel
J. Math., 80(3):337–349, 1992.
[47] A. Defant and K. Floret. Tensor norms and operator ideals, volume 176. Elsevier, 1992.
[48] R.T. Rockafellar. Convex analysis. Princeton Mathematical Series, No. 28. Princeton University Press, Princeton, N.J., 1970.
[49] C.D. Aliprantis and R. Tourky. Cones and Duality. Graduate studies in mathematics. American Mathematical Society, 2007.
[50] G. Aubrun and S.J. Szarek. Alice and Bob meet Banach, volume 223 of Mathematical Surveys
and Monographs. American Mathematical Society, Providence, RI, 2017. The interface of
asymptotic geometric analysis and quantum information theory.
[51] G. Pisier. Grothendieck’s theorem, past and present. Bull. Amer. Math. Soc. (N.S.), 49(2):237–
323, 2012.
[52] P. Wojtaszczyk. Banach spaces for analysts, volume 25 of Cambridge Studies in Advanced
Mathematics. Cambridge University Press, Cambridge, 1991.
[53] G.M. Ziegler. Lectures on polytopes, volume 152 of Graduate Texts in Mathematics. SpringerVerlag, New York, 1995.
[54] A. Brøndsted. An introduction to convex polytopes, volume 90 of Graduate Texts in Mathematics. Springer-Verlag, New York-Berlin, 1983.
[55] T. Zamﬁrescu. On two conjectures of Franz Hering about convex surfaces. Discrete Comput.
Geom., 6(1):171–180, 1991.
[56] R. Schneider. Convex Bodies: The Brunn–Minkowski Theory. Encyclopedia of Mathematics
and its Applications. Cambridge University Press, 2nd edition, 2013.

23

<!-- page 24 -->
Supplemental Material
We present here the formal proofs of our results. The focus is on technical precision; we
refer to the main article for motivation. Statements which appear only in Supplementary
Information are labelled by S1, S2, etc.; statements which are duplicated from the main
article use the same label as in the main article. In accordance with standard usage in
mathematical literature, we rephrased our main results as theorems, keeping the same
labels.
Section I introduces all concepts which are needed to define the tensor products of
cones, and restatements of the results announced in the main article. Section II contains
the proof of Result 1 on 3-dimensional cones. Section III is devoted to the proof of Result 2,
concerning polyhedral cones. Section IV contains the proof of Result 3, which deals with
the case of one cone being that of positive semidefinite matrices. In Section V C we prove
Result 4 on symmetric cones. Finally, Section VI contains extra information about retracts
of cones, a concept which plays a central role in our argument.
I.

DEFINITIONS, ELEMENTARY FACTS AND STATEMENTS OF THE
THEOREMS
A.

Convexity, convex cones

All vector spaces are assumed to be over the real field, and finite-dimensional. Hereafter,
we denote with R+ the set of non-negative real numbers.
Definition S1. A cone is a subset C of a vector space with the following property: for
every x ∈ C and α ∈ R+ , we have αx ∈ C.
Definition S2. Let V be a vector space.
(S2.1) The dual space to V , denoted V ∗ , is defined as the space of linear maps from V to
R. We always identify the double dual (V ∗ )∗ with V .
(S2.2) A subset A ⊆ V is convex if x, y ∈ A implies λx + (1 − λ)y ∈ A for every λ ∈ [0, 1].
It follows that a subset C ⊂ V is a convex cone if and only if x, y ∈ C implies
αx + βy ∈ C for every α, β ∈ R+ .
(S2.3) A convex body in V is a compact convex set with nonempty interior.
(S2.4) The convex hull of a subset A ⊆ V is
)
( n
n
X
X
λi = 1 .
λi ai : n ∈ {1, 2, 3, . . .}, λi ∈ [0, 1], ai ∈ A,
conv(A) :=
i=1

i=1

1

<!-- page 25 -->
Equivalently, it equals the intersection of all convex sets containing A.
(S2.5) The affine span of a subset A ⊆ V is
)
( n
n
X
X
λi = 1 .
λi ai : n ∈ {1, 2, 3, . . .}, λi ∈ R, ai ∈ A,
aff(A) :=
i=1

i=1

Equivalently, it equals the intersection of all affine subspaces containing A.
(S2.6) A set {y1 , . . . , yn } ⊂ V is affinely independent if yi 6∈ aff{yj : j 6= i} for every
1 ⩽ i ⩽ n.
(S2.7) The conical hull of a subset A ⊆ V is
)
( n
X
λi ai : n ∈ {1, 2, 3, · · · }, λi ∈ R+ , ai ∈ A .
cone(A) :=
i=1

Equivalently, it equals the intersection of all convex cones containing A.
Definition S3. Let K be a convex set in a vector space.
(S3.1) The dimension of K, denoted dim(K), is defined as the dimension of its affine span.
(S3.2) A nonempty convex subset F ⊆ K is a face of K if x ∈ K, y ∈ K, 0 < λ < 1 and
λx + (1 − λ)y ∈ F imply x, y ∈ F .
(S3.3) A face F ⊆ K is proper if F 6= K.
(S3.4) A face F ⊆ K is a facet if dim(F ) = dim(K) − 1.
(S3.5) An element x ∈ K is an extreme point of K if {x} is a face of K. This is equivalent
to say that the equation x = λy + (1 − λ)z, for y, z ∈ K and 0 < λ < 1, implies that
y = z = x.
Definition S4. Let C be a cone. An extreme ray of C is a face of dimension 1. Equivalently,
for x ∈ C \ {0}, the set R+ x is an extreme ray of C if the equation x = y + z for y, z ∈ C
implies y = αx for some α ∈ [0, 1].
Definition S5. Let V1 , V2 be vector spaces, and C1 ⊂ V1 , C2 ⊂ V2 be convex cones.
The cones C1 and C2 are isomorphic if there is a linear bijection Φ : V1 → V2 such that
Φ(C1 ) = C2 .
Definition S6. Let C be a cone in a vector space V .
(S6.1) C is salient if C ∩ (−C) = {0}.
2

<!-- page 26 -->
(S6.2) C is generating if the linear span of C equals V .
(S6.3) C is proper if it is convex, closed, salient and generating.
(S6.4) The dual cone C ∗ ⊂ V ∗ is defined as C ∗ := {f ∈ V ∗ : f (x) ⩾ 0 for every x ∈ C}.
Fact S7 (Bipolar theorem [48, Theorem 14.1]). Every closed convex cone C ⊆ V satisfies
C ∗∗ = C upon the identification V ∗∗ = V .
Definition S8 (GPT). A general probabilistic theory (GPT) is a triple (V, C, u), where
V is a finite-dimensional real vector space, C ⊂ V is a proper cone, and u ∈ int(C ∗ ) is
a positive functional on C. The corresponding state space is Ω := C ∩ u−1 (1). We call
dim(V ) the dimension of the GPT.
Fact S9 (see [49, Theorem 3.5]). Given a proper cone C, the interior int(C ∗ ) of the dual
cone C ∗ coincides with the set of strictly positive functionals on C. A functional ϕ ∈ V ∗
is called strictly positive on a cone C ⊆ V if ϕ(x) ⩾ 0 for all x ∈ C, with equality only for
x = 0.
Hence, in Definition S8 we could equivalently require that u be a strictly positive functional.
Definition S10. A base of a cone C ⊆ V is a convex subset K ⊂ C such that for all x ∈ C
there is a unique t ⩾ 0 that satisfies x ∈ tK.
Fact S11 (see [49, Theorem 1.47]). Let C be a convex and salient cone. Then all bases of
C (if they exist) are of the form K = C ∩ ϕ−1 (1), for some strictly positive functional ϕ on
C.
In particular, note that the state space Ω of a GPT (V, C, u) is always a base of the cone
C. There is a natural yet general way to construct a cone with a given base:
Definition S12. Let V be a vector space, and K ⊆ V a convex set. The cone with base
K is the cone in V ⊕ R defined as
C (K) = {(tx, t) : x ∈ K, t ∈ R+ }.

(S1)

Fact S13 shows that any proper cone has a base.
Fact S13 (see [50, Corollary 1.8]). Let C ⊆ V be a finite-dimensional convex, salient and
generating salient cone. Then:
(a) C is closed (and hence, proper) if and only if bases for it exist and are all compact;
(b) if C is proper, then it is isomorphic to C (K), where K is any of its bases;
3

<!-- page 27 -->
(c) in particular, if C is proper and ϕ ∈ int(C ∗ ) is strictly positive on C, then C ∩ ϕ−1 (1)
is a convex body inside the affine space ϕ−1 (1).
In particular, note that whenever (V, C, u) is a GPT, the cone C is isomorphic to C (Ω),
where Ω is the state space. Also, Ω is a convex body when viewed as a subset of the affine
space u−1 (1). Fact S14 relates the facial structure of a cone and of its base.
Fact S14 (see [50, Proposition 1.9]). Let K be a convex body. There is a one-to-one
correspondence between faces of K and faces of C (K) distinct from {0}, given by the map
F 7→ R+ F .
Fact S15. Let K be a convex body in a vector space V , and let Φ : V → V be an affine
bijection, i.e. a map of the form x 7→ Φ(x) = Ψ(x) + z, where z ∈ V and Ψ : V → V is an
invertible linear map. Then the cones C (K) and C (Φ(K)) are isomorphic.
Proof. One checks that the linear map Φ̃ : V ×R → V ×R defined by Φ̃(x, t) = (Ψ(x)+tz, t)
is invertible and satisfies Φ̃(C (K)) = C (Φ(K)).
Definition S16. A cone is classical if it is isomorphic to
Rn+ := {(x1 , . . . , xn ) ∈ Rn : xi ⩾ 0 for 1 ⩽ i ⩽ n}

(S2)

for some integer n ⩾ 1.
Fact S17. Let C be a proper cone. Then C is classical if and only if C ∗ is classical.
Definition S18. A simplex in a vector space is the convex hull of an affinely independent
set.
Fact S19. Let C be a proper cone in a vector space V . The following are equivalent:
(i) C is classical,
(ii) there exists a basis A of the vector space V such that C = cone(A),
(iii) there exists a simplex ∆ with dim(∆) = dim(V ) such that C is isomorphic to C (∆),
(iv) every convex set K such that C (K) is isomorphic to C is a simplex.
Definition S20. Let V , W be vector spaces. The adjoint of a linear map Φ : V → W is
the linear map Φ∗ : W ∗ → V ∗ defined by the relation Φ∗ (g)(x) = g(Φ(x)) for every x ∈ V ,
g ∈ W ∗.
Fact S21. Let V , W be vector spaces, C ⊆ V be a convex cone and Φ : V → W be a
linear map. Then Φ(C)∗ = (Φ∗ )−1 (C ∗ ).
Proof. For g ∈ W ∗ , we have the equivalences

g ∈ Φ(C)∗ ⇐⇒ ∀x ∈ C, g(Φ(x)) ⩾ 0 ⇐⇒ ∀x ∈ C, Φ∗ (g)(x) ⩾ 0 ⇐⇒ Φ∗ (g) ∈ C ∗ ,

hence the result follows.
4

<!-- page 28 -->
B.

Tensor products of cones

We now introduce our main object of study: tensor products of cones.
Definition S22. Let V1 and V2 be vector spaces, and C1 ⊆ V1 , C2 ⊆ V2 be convex cones.
(S22.1) The minimal tensor product of C1 and C2 is the convex cone in V1 ⊗ V2 defined by
C1  C2 := conv{x1 ⊗ x2 : x1 ∈ C1 , x2 ∈ C2 } .
(S22.2) The maximal tensor product of C1 and C2 is the convex cone in V1 ⊗ V2 defined by
C1  C2 := {x ∈ V1 ⊗ V2 : (f1 ⊗ f2 )(x) ⩾ 0 for every f1 ∈ C1∗ , f2 ∈ C2∗ } .
In this definition we identify (V1 ⊗ V2 )∗ and V1∗ ⊗ V2∗ .
Fact S23. Let C1 and C2 be convex cones. Then
(a) C1  C2 ⊆ C1  C2 ;
(b) if C1 and C2 are proper, then so are C1  C2 and C1  C2 .
A non-obvious point in Fact S23 is that C1  C2 is closed. This can be seen by taking
compact bases K1 , K2 , and by checking that C1  C2 also has a compact base, namely the
image of the compact set K1 × K2 under the continuous map (x, y) 7→ x ⊗ y.
Fact S24. Minimal and maximal tensor product are dual to each other. Namely, for all
proper cones C1 and C2 , it holds that
(C1  C2 )∗ = C1∗  C2∗ ,
∗

(C1  C2 ) = C1∗  C2∗ .

(S3)
(S4)

Definition S25. Let C1 and C2 be proper cones. The pair (C1 , C2 ) is called nuclear if
C1  C2 = C1  C2 and entangleable if C1  C2 ( C1  C2 .
The terminology “nuclear” is borrowed from the language of C ∗ -algebras, where the
analogous concept has played a central role in the theory (see e.g. [51, §12]).
Fact S26. If C1 is isomorphic to C1′ and C2 is isomorphic to C2′ , then
(C1 , C2 ) is nuclear ⇐⇒ (C1′ , C2′ ) is nuclear.
As explained in the main text, it is natural to conjecture that a pair (C1 , C2 ) of proper
cones is nuclear if and only if C1 or C2 is classical. This question can be traced back
to [34, 35]. The ‘if’ direction is easy and we have already seen a proof of it in the Methods
section. The original argument seem to go back to Namioka and Phelps [19], and to have
been re-discovered many times, e.g. by Barker [34, 35]. As for the much more challenging
‘only if’ direction, our first result settles the situation at least for 3-dimensional cones.
5

<!-- page 29 -->
Theorem 1 (Proved in Section II). Let C1 and C2 be proper cones of dimension 3. If
(C1 , C2 ) is nuclear, then either C1 or C2 is classical.
Our second result solves the problem for polyhedral cones.
Definition S27. A convex cone is polyhedral if it is the conical hull of a finite set.
Theorem 2 (Proved in Section III). Let C1 and C2 be proper polyhedral cones. If (C1 , C2 )
is nuclear, then either C1 or C2 is classical.
Our third result concerns the case when one cone is the cone of PSD matrices.
Definition S28. We denote by PSDn be the cone of n × n positive semidefinite matrices,
which is contained in the real vector space Msa
n of n × n Hermitian matrices with complex
2
entries. Note that dim(PSDn ) = n .
Theorem 3. Let C be a proper cone of dimension d, and assume that ⌊log2 n⌋ ⩾ d−1
2 .
Then the pair (C, PSDn ) is nuclear if and only if C is classical.
Our methods also yield a proof of the following result from [24].
Theorem 3’. Let C be a proper polyhedral cone, and assume that n ⩾ 2. Then the pair
(C, PSDn ) is nuclear if and only if C is classical.
Our last result is a first attempt towards a quantitative extension of the above qualitative
correspondence between local non-classicality and global entangleability. We are able to
rigorously establish such an extension in the geometrically natural case where the local
state spaces are centrally symmetric around some fixed local states.
Definition S29. A GPT (V, C, u) is called symmetric if there is a state γ ∈ Ω := C ∩u−1 (1),
called its centre, such that 2γ − ω ∈ Ω for all ω ∈ Ω.
We also put forth the following general definition of entanglement robustness.
Definition S30. Let (V1 , C1 , u1 ), (V2 , C2 , u2 ) be GPTs. The entanglement robustness of
ω ∈ C1  C2 is given by
Erob (ω) := min {(u1 ⊗ u2 )(ζ) : ζ, ω + ζ ∈ C1  C2 } .

(20)

Theorem 4. Let (V1 , C1 , u1 ) and (V2 , C2 , u2 ) be two symmetric GPTs of dimensions
n + 1 and m + 1, respectively. Then there exists ω ∈ C1  C2 such that Erob (ω) ⩾
c min{n, m}1/8−o(1) , where c > 0 is a number, and o(1) denotes a quantity tending to 0 as
min{n, m} tends to infinity. Moreover, provided n, m ⩾ 2, there exists ω ∈ C1  C2 such
that Erob (ω) ⩾ 1/36.
6

<!-- page 30 -->
C.

Retracts

Definition S31. Let V , W be vector spaces.
(S31.1) We denote by L(V, W ) the vector space of linear maps from V to W .
(S31.2) We denote by z 7→ op(z) the canonical bijection between V ⊗ W and L(V ∗ , W ),
defined for x ∈ V , y ∈ W , f ∈ V ∗ by op(x ⊗ y) : f 7→ f (x)y.
Definition S32. Let C1 ⊆ V1 , C2 ⊆ V2 be cones in vector spaces. A linear map Φ ∈
L(V1 , V2 ) is (C1 , C2 )-positive (or positive if there is no ambiguity) if Φ(C1 ) ⊆ C2 . We
denote by Pos(C1 , C2 ) ⊆ L(V1 , V2 ) the cone of (C1 , C2 )-positive maps.
Fact S33. Let C1 and C2 be proper cones. If a linear map Φ is (C1 , C2 )-positive, then the
adjoint map Φ∗ is (C2∗ , C1∗ )-positive.
Fact S34 interprets the maximal tensor product as a cone of positive maps.
Fact S34. Let C1 and C2 be proper cones. Then
op(C1  C2 ) = Pos(C1∗ , C2 ).
We now introduce the concept of a retract.
Definition S35. Let C ⊆ V and C ′ ⊆ V ′ be convex cones in vector spaces. We say that
C ′ is a retract of C if there are positive maps Φ ∈ Pos(C, C ′ ) and Ψ ∈ Pos(C ′ , C) such that
Φ ◦ Ψ = IdV ′ . This implies in particular that C ′ = Φ(C). In this context, the map Φ is
called a retraction.
Fact S36. If C is proper and C ′ is a retract of C, then also C ′ is proper.
Proof. Since C ′ is assumed to be a convex cone, we just need to check that is closed, salient,
and generating. Closedness follows from the fact that C ′ = Φ(C), with C closed and Φ
linear. To prove that C ′ is salient, note that


C ′ ∩ (−C ′ ) = (Φ ◦ Ψ) C ′ ∩ (−C ′ ) ⊆ Φ Ψ(C ′ ) ∩ Ψ(−C ′ ) ⊆ Φ (C ∩ (−C)) = {0} .
To show that it is generating instead, write

V ′ = Φ(V ) = Φ(C − C) ⊆ Φ(C) − Φ(C) ⊆ C ′ − C ′ ,
which naturally implies that V ′ = C ′ − C ′ .
Fact S37 shows that retractions nicely dualise.
Fact S37. Let C1 , C2 be proper cones. If C1 is a retract of C2 , then C1∗ is a retract of C2∗ .
7

<!-- page 31 -->
Proof. There are maps Φ ∈ Pos(C2 , C1 ) and Ψ ∈ Pos(C1 , C2 ) such that Φ◦Ψ is the identity.
As a consequence of Fact S33, we have that Φ∗ ∈ Pos(C1∗ , C2∗ ) and Ψ∗ ∈ Pos(C2∗ , C1∗ ). Since
Ψ∗ ◦ Φ∗ = (Φ ◦ Ψ)∗ is the identity, this shows that C1∗ is a retract of C2∗ .
We also check that a retract of a cone can always be realised as a section.
Fact S38. Let C1 ⊂ V1 , C2 ⊂ V2 be proper cones in vector spaces. Then C1 is a retract of
C2 if and only if C1 is isomorphic to C2 ∩ E, where E ⊂ V2 is a subspace for which there
is a projection P : V2 → E such that C2 ∩ E = P (C2 ).
Proof. The ‘if’ direction is easy. Conversely, suppose that C1 is a retract of C2 ; consider
Φ ∈ Pos(C2 , C1 ) and Ψ ∈ Pos(C1 , C2 ) such that Φ ◦ Ψ = IdV1 . Set E to be the range of
Ψ. Since Ψ is injective, the cones C1 and Ψ(C1 ) are isomorphic. Finally, one checks that
P := Ψ ◦ Φ is a projection onto E such that P (C2 ) = C2 ∩ E = Ψ(C1 ).
The concept of a retract plays an important role in our study, because of the following
property, whose proof was already provided in the Methods section of the main article.
Proposition 8 (Nuclearity passes to retracts). Let (C1 , C2 ) be a nuclear pair. If C1′ is a
retract of C1 , and C2′ is a retract of C2 , then (C1′ , C2′ ) is a nuclear pair.
We also present two extra statements about retracts which are not needed for the proofs
of the main results, but which we include as we believe they could help the reader forge their
intuition. They show that while 2-dimensional sections are always retracts, this typically
never happens for higher-dimensional sections. Since we could not locate these statements
elsewhere in the literature, proofs are provided in Section VI.
Proposition S1. Let C ⊂ V be a proper cone, and E ⊆ V be a 2-dimensional subspace
which intersects the interior of C. Then C ∩ E is a retract of C.
Proposition S2. There is a 4-dimensional convex cone which admits no 3-dimensional
retract.
D.

Tensor norms

The proof of Result 4 requires us to familiarise with the concept of tensor norms. Here
we introduce the main definitions and discuss some of their elementary implications. The
interested reader is referred to the monograph [47].
Definition S39. Let X be a real vector space. A norm on X is a function k · k : X → R+
that is: (i) faithful, meaning that kxk = 0 if and only if x = 0; (ii) absolutely homogeneous,
i.e. such that kλxk = |λ|kxk for all λ ∈ R; and (iii) obeys the triangle inequality, which
states that kx + yk ⩽ kxk + kyk, for all x, y ∈ X. A vector space equipped with a norm is
called a normed space.
8

<!-- page 32 -->
Note. We will often specify as a subscript the normed space a norm refers to. Accordingly,
the norm of x ∈ X will be denoted by the symbol kxkX .
Definition S40. The unit ball of a normed space X is the convex set BX := {x ∈ X : kxkX ⩽ 1}.
Definition S41. Let X be a normed space. The dual vector space X ∗ can be turned into
a normed space itself via the definition of the dual norm
kf kX ∗ := sup |f (x)| .

(S5)

x∈BX

Fact S42. The bi-dual of a finite-dimensional normed space X is the space X itself.
Namely, for all x ∈ X it holds that
kxkX = sup |f (x)| .

(S6)

f ∈BX ∗

Definition S43. Let X, Y be finite-dimensional real vector spaces, and let X ⊗ Y be their
tensor product.
(S43.1) The injective tensor norm is the norm on X ⊗ Y defined by
kzkX⊗ε Y := sup {(f ⊗ g)(z) : f ∈ BX ∗ , g ∈ BY ∗ } ,

(17)

for all z ∈ X ⊗ Y .
(S43.2) The projective tensor norm is the norm on X ⊗ Y defined by
nX
o
X
kzkX⊗π Y := inf
kxi kX kyi kY : z =
xi ⊗ y i ,
i

i

(S7)

for all z ∈ X ⊗ Y .

Fact S44. Injective and projective tensor norm are dual to each other. Namely, one has
the normed space identities
(X ⊗ε Y )∗ = X ∗ ⊗π Y ∗ ,
∗

∗

∗

(X ⊗π Y ) = X ⊗ε Y .

(S8)
(S9)

The following is easy to verify.
Fact S45. Let X, Y be finite-dimensional spaces. Then there exists a smallest constant
ρ(X, Y ) > 0 such that
kzkX⊗ε Y ⩽ kzkX⊗π Y ⩽ ρ(X, Y )kzkX⊗ε Y
for all z ∈ X ⊗ Y .
9

(S10)

<!-- page 33 -->
Definition S46 (Projective/injective ratio [27]). Given integers n, m ⩾ 2, the associated
projective/injective ratio is defined by
r(n, m) :=

inf

dim X=n
dim Y =m

(S11)

ρ(X, Y ) ,

where the infimum is over all pairs of normed spaces X, Y of dimensions n, m, respectively,
and ρ(X, Y ) is defined in Fact S45.
We rely on the following estimates from [27] on the projective/injective ratio.
Fact S47 (Theorem 6 in [27]). For every integers n, m ⩾ 2, it holds that r(n, m) ⩾ 19/18.
Fact S48 (Theorem 2 in [27]). There is a constant c > 0 such that, for every integers
n, m ⩾ 2, we have that
r(n, m) ⩾ c

min{n, m}1/8
.
log min{n, m}

It is conjectured in [27] that the value 19/18 in Fact S47 can be replaced by
that the exponent 1/8 in Fact S48 can be replaced by 1/2.
II.

√

2, and

PROOF OF THEOREM 1: 3-DIMENSIONAL CONES

Definition S49. Let a and b be elements of (−1, 1). The kite with center (a, b) is defined
as
Ta,b := conv{(a, ±1), (±1, b)} ⊂ R2 .
Definition S50. The blunt square is defined as S = [−1, 1]2 \ {−1, 1}2 ⊂ R2 .
Note that the cone C (S) is not proper, since it is not closed. We rely on two propositions.
The first shows that any non-classical cone can be ‘sandwiched’ between cones based on a
kite and on a blunt square. The second produces nontrivial information about the maximal
tensor product of cones based on kites vs the minimal tensor product of cones based on
blunt squares.
Proposition 6. Let V be a 3-dimensional vector space, and C ⊂ V a proper cone which is
not classical. There exist (a, b) ∈ (−1, 1)2 and Φ : V → R2 × R a linear bijection such that
C (Ta,b ) ⊆ Φ(C) ⊆ C (S) .
Proposition 7. Let a1 , a2 , b1 and b2 be elements of (−1, 1). Then
C (Ta1 ,b1 )  C (Ta2 ,b2 ) 6⊆ C (S)  C (S).
In other words, there exists ω ∈ C (Ta1 ,b1 )  C (Ta2 ,b2 ) such that ω 6∈ C (S)  C (S).
10

<!-- page 34 -->
We postpone the proof of Propositions 6 and 7 to the end of this section, and show
how they together imply Theorem 1. The following reasoning was already sketched in the
Methods section of the main article, but we repeat it here for the sake of completeness.
Considering two 3-dimensional non-classical proper cones C1 , C2 , we need to show that the
pair (C1 , C2 ) is entangleable. Assume by contradiction that (C1 , C2 ) is a nuclear pair. By
combining Proposition 6 with Fact S26, we may assume that
C (Ta1 ,b1 ) ⊆ C1 ⊆ C (S) and C (Ta2 ,b2 ) ⊆ C2 ⊆ C (S)
for some a1 , a2 , b1 , b2 ∈ (−1, 1). Since  and  are increasing operations with respect to
set inclusion, it follows that
C (Ta1 ,b1 )  C (Ta2 ,b2 ) ⊆ C1  C2 = C1  C2 ⊆ C (S)  C (S) ,
thus contradicting the conclusion of Proposition 7.
A.

Proof of Proposition 6

We prove the following statement, which implies Proposition 6. It is a variant of Auerbach’s lemma, which is usually stated for symmetric convex bodies (see for example [52,
II.E.11]).
Proposition S3. If K ⊂ R2 is a convex body which is not a triangle, then there exists an
affine bijection Ψ : R2 → R2 and a, b ∈ (−1, 1) such that Ta,b ⊆ Ψ(K) ⊆ S.
To check that Proposition S3 implies Proposition 6, first note, using Fact S13, that it
is enough to prove Proposition 6 for C = C (K), with K a convex body in R2 . Moreover, by Fact S19 we see that C is non-classical if and only if K is not a triangle (i.e. a
two-dimensional simplex). Then, Proposition 6 follows from Proposition S3 together with
Fact S15.
Proof of Proposition S3. Let ABCD be a quadrilateral of maximal area inside K (since K
is not a triangle, this quadrilateral does not degenerate into a triangle). The existence of this
quadrilateral follows easily from a compactness argument. Basic geometric considerations
(see Figure 1) show that maximality implies that K lies between the lines parallel to (AC)
passing through B and D; and between the lines parallel to (BD) passing through A and
C. These four lines delimit a parallelogram which can be mapped to [−1, 1]2 by a suitable
affine bijection Ψ. At this step we showed the existence of (a, b) ∈ (−1, 1)2 such that
Ta,b ⊆ Ψ(K) ⊆ [−1, 1]2 . This is a bit weaker than the conclusion of the lemma.
To enforce Ψ(K) ⊆ S we need to be more careful in our construction. Among all
quadrilaterals of maximal area inside K, choose ABCD with the extra property that as
few as possible among A, B, C and D are extreme points in K. We claim that repeating the
11

<!-- page 35 -->
E•

A
•

D•

•B

K
•
C
FIG. 1. The quadrilateral ABCD has maximal area inside the convex body K depicted in gray. It
follows that K lies in the parallelogram delimited by dotted lines: if for example a point E is above
the line parallel to (BD) passing through A, then area(EBCD) > area(ABCD) and therefore
E 6∈ K.

construction from the previous paragraph with that choice of ABCD implies that Ψ(K) ⊆
S. Indeed, since our construction is affine-invariant, we may assume that Ψ is the identity,
so that Ta,b ⊆ K ⊆ [−1, 1]2 . The fact that Ta,b is a quadrilateral of maximal area inside K
follows from the change of variables theorem, which ensures that the area of the image of
a set X by an affine transformation equals the area of X times a constant. By symmetry
F A
• •

•E

•B

D•

•
C
FIG. 2. If E belongs K and A is not an extreme point of K, then K contains the quadrilateral
F ECD which has larger area than ABCD.

it suffices to show that E := (1, 1) 6∈ K. Suppose by contradiction that E ∈ K, and let
consider the points A = (a, 1), B = (1, b), C = (a, −1) and D = (−1, b). We claim that
A is not an extreme point of K. This follows from our choice of ABCD together with the
12

<!-- page 36 -->
observation that, for every X in the segment AE, we have area(ABCD) = area(XBCD)
while X is not an extreme point of K (see Figure 2). It follows that there exists a′ < a
such that the point F := (a′ , 1) belongs to K. At this point we reached a contradiction:
since AECD is strictly contained in F ECD, we have
area(F ECD) > area(AECD) = area(ABCD).
Hence, we have found a quadrilateral F ECD inside K which has an strictly larger area
than area(Ta,b ).
B.

Proof of Proposition 7

The cones C (Ta,b ) and C (S) live in R2 × R, which we identify with R3 . The tensor
products C (Ta1 ,b1 )  C (Ta2 ,b2 ) and C (S)  C (S) live in R3 ⊗ R3 , which we identify with
the algebra M3 of 3 × 3 matrices with real entries. We also use the canonical inner product
on R3 ⊗ R3 , which allows to identify (R3 ⊗ R3 )∗ with R3 ⊗ R3 .
Given real parameters a and b, consider the self-adjoint matrices




1 ab a
1 1 0
Ma,b := ab 1 b  , H := 1 −1 0 .
a b 1
0 0 1
The proof of Proposition 7 is completely explicit: given a1 , b1 , a2 , b2 ∈ (−1, 1), we define
a matrix Ω = (ωi,j ) by
Ω := Ma2 ,b2 H −1 Ma1 ,b1 .
We compute, using the notation α = a1 b1 , β = a1 b2 , γ = a2 b1 , δ = a2 b2 , ε = a1 a2 , ζ = b1 b2 ,
η = a1 a2 b1 b2 ,


1 + α + δ + 2ε − η
1 + α + 2γ − δ + η
∗
1
,
−1 + α + δ + 2ζ + η
∗
Ω = 1 − α + 2β + δ + η
2
∗
∗
2+β +γ+ε−ζ

where entries whose values are not used in our computation are denoted by ∗. We check in
particular that
ω11 + ω12 + ω21 − ω22 = 2ω33 .

(S12)

Let ω ∈ R3 ⊗ R3 be the tensor which is identified with Ω ∈ M3 . We claim that
ω ∈ C (Ta1 ,b1 )  C (Ta2 ,b2 ),

(S13)

ω 6∈ C (S)  C (S),

(S14)

and the proof of Proposition 7 will be complete provided we justify (S13) and (S14).
13

<!-- page 37 -->
Proof of (S13). Denote by K = conv{(±1, 0), (0, ±1)} ⊂ R2 .
Fact S51. The matrices H and Ma,b have the following properties
S51.1 For every a, b in (−1, 1), we have Ma,b (C (K)) = C (Ta,b ).
S51.2 We have H(C (K)) = C (K)∗ .
Proof. For the first part, note that Ma,b (±1, 0, 1) = (1 ± a)(±1, b, 1) and Ma,b (0, ±1, 1) =
(1 ± b)(a, ±1, 1), so that Ma,b maps extreme rays of C (K) to extreme rays of C (Ta,b ). For
the second part, we check that C (K)∗ = C ([−1, 1]2 ), and that H maps extreme rays of
C (K) to extreme rays of C ([−1, 1]2 ).
In view of Fact S34, (S13) is equivalent to the fact that Ω = op(ω) ∈ Pos(C (Ta1 ,b1 )∗ , C (Ta2 ,b2 )),
or again to the inclusion
Ma2 ,b2 H −1 Ma1 ,b1 (C (Ta1 ,b1 )∗ ) ⊆ C (Ta2 ,b2 )
or further (using Fact S51.1) that

Ma2 ,b2 H −1 Ma1 ,b1 (Ma1 ,b1 C (K))∗ ⊆ Ma2 ,b2 C (K).

We now invoke Fact S21 (applied with Φ = Φ∗ = Ma1 ,b1 ) to claim that this statement follows
from the inclusion H −1 (C (K)∗ ) ⊆ C (K), which is an obvious consequence of Fact S51.2.
Proof of (S14). Consider a ∈ C (S)  C (S), identified with a matrix (aij ) ∈ M3 . We claim
that it satisfies the inequality
a11 + a12 + a21 − a22 < 2a33 .

(S15)

Once (S15) is proved, (S14) follows immediately by comparison with (S12). To show (S15),
we use the following variant of the CHSH inequality.
Lemma S4 (CHSH inequality, strict version). If (x1 , y1 ) ∈ S and (x2 , y2 ) ∈ S, then
x1 x2 + x1 y2 + y1 x2 − y1 y2 < 2.

(S16)

Proof of Lemma S4. We have
|x1 x2 + x1 y2 + y1 x2 − y1 y2 | ⩽ |x1 | · |x2 + y2 | + |y1 | · |x2 − y2 |
⩽ |x2 + y2 | + |x2 − y2 |

⩽ 2.

We argue that one of the inequalities must be strict. Assume the last inequality to be an
equality. In this case, either |x2 | or |y2 | must equal 1. Since they cannot both equal 1, the
numbers x2 + y2 and x2 − y2 are nonzero. Now, if the second inequality is also an equality,
then it follows that |x1 | = |y1 | = 1, a contradiction.
14

<!-- page 38 -->
To complete the proof of (S15), note that any nonzero element z ∈ C (S)  C (S) is
a positive combination of elements of the form (x1 , y1 , 1) ⊗ (x2 , y2 , 1) with (x1 , y1 ) and
(x2 , y2 ) in S. It is enough to test (S15) on elements of that form, in which case it reduces
to (S16).
III.

PROOF OF THEOREM 2: POLYHEDRAL CONES

The proof of Theorem 2 is based on the following proposition, whose proof is postponed
to the end of the section.
Proposition S5 (non-classical polyhedral cones have non-classical retracts). Let C be a
proper polyhedral cone which is non-classical. Then there is a non-classical 3-dimensional
proper polyhedral cone C ′ which is a retract of C.
To prove Theorem 2, consider C1 , C2 proper polyhedral cones, and suppose that (C1 , C2 )
is nuclear. Assume by contradiction that C1 and C2 are non-classical. By Proposition S5,
there exist non-classical 3-dimensional proper polyhedral cones C1′ and C2′ which are retracts
of C1 and C2 , respectively. By Proposition 8, it follows that the pair (C1′ , C2′ ) is nuclear.
This contradicts Theorem 1.
Proof of Proposition S5. We rely on the following two lemmas.
Lemma 9 (see also Exercise 2.18 in [53]). Let F be a facet of a proper polyhedral cone C.
Then F , which is a proper polyhedral cone when seen as a subset of span(F ), is a retract
of C.
Lemma 10. Let C be a non-classical proper polyhedral cone with dim(C) ⩾ 4. Then
either C or C ∗ has a facet which is non-classical.
We now prove Proposition S5 by induction on the dimension. Let C be a non-classical
proper polyhedral cone of dimension n (note that n ⩾ 3, since any 2-dimensional cone is
classical). If n = 3, Proposition S5 is obviously true. If n ⩾ 4, using Lemmas 9 and 10,
we obtain that either (i) C has a non-classical polyhedral retract of dimension n − 1 or (ii)
C ∗ has a non-classical polyhedral retract of dimension n − 1. Using Facts S17 and S37, we
check that (i) and (ii) are in fact equivalent, so (i) always holds. Since a retract of a retract
of C is also a retract of C, Proposition S5 follows by induction.
For the proof of Lemma 9 we will use the following standard fact (see [54, Theorem
5.8]).
Fact S52. Let C be a closed convex set in a vector space V , and F be a facet of C. Then
there is a linear form f ∈ V ∗ and a real number a such that f (x) ⩾ a for every x ∈ C, and
C ∩ f −1 (a) = F .
15

<!-- page 39 -->
Proof of Lemma 9. Let W = aff(F ); note that dim W = dim V − 1. By Fact S52 and the
homogeneity of C (used to enforce a = 0), there is a linear form f ∈ V ∗ such that f ⩾ 0
on C, ker f = W and W ∩ C = F .
Let π : V → W be a projection onto W . Pick an element x in the relative interior of
F , and define for λ > 0 a linear map Φλ : V → W by Φλ (z) = π(z) + λf (z)x for z ∈ V . If
z ∈ F ⊂ W , then Φλ (z) = π(z) = z ∈ F . On the other hand, for every z ∈ C \ F , we have


Φλ (z) = λ f (z)x + λ−1 π(z) .

Since f (z) > 0, the point f (z)x is in the relative interior of F , and we have Φλ (z) ∈ F
for λ larger than some number λ0 (z) > 0. Since C = cone(A) for some finite set A, it
follows that Φλ (C) ⊂ F for λ larger than max{λ0 (z) : z ∈ A}. If Ψ : W → V denotes
the canonical inclusion, Φλ ◦ Ψ is the identity on W , and this shows that F is a retract of
C.

Lemma 10 is a reformulation for polyhedral cones of a basic result on polytopes
(Fact S53). A polytope is a convex body which is the convex hull of a finite set. A ddimensional polytope is said to be simplicial if all its facets contain exactly d vertices (i.e.
they are (d − 1)-dimensional simplices), and is said to be simple if every vertex belongs to
d facets.
Fact S53 (See [54, Theorem 12.19]). For d ⩾ 3, a d-dimensional polytope which is both
simple and simplicial is a simplex.
We also use basic properties of the duality of polytopes, which is defined for example
in [54, §10].
Fact S54 (See [54, Theorem 12.10]). Let P and Q be dual polytopes. Then P is simple if
and only if Q is simplicial.
Fact S55 (See [50, Lemma 1.6]). Let P be a polytope. Then there is a polytope Q dual
to P such that the cones C (P )∗ and C (Q) are isomorphic.
Proof of Lemma 10. Let C be a non-classical proper polyhedral cone with dim(C) ⩾ 4.
Without loss of generality (Fact S13) we may assume that C = C (P ) for some polytope P
of dimension at least 3. Since C is not classical, P is not a simplex (Fact S19). By Fact S53,
P cannot be both simple and simplicial.
• If P is not simplicial, then one of its facets is not a simplex, and therefore one of the
facets of C (P ) is not classical (see Fact S14).
• It P is not simple, let Q be the polytope dual to P given by Fact S55. By Fact S54,
Q is not simplicial. Repeating the reasoning above with Q instead of P and using
Fact S55 shows that one of the facets of C (P )∗ is not classical.
In both cases, the conclusion of Lemma 10 is verified.
16

<!-- page 40 -->
IV.

PROOF OF THEOREM 3: POSITIVE SEMIDEFINITE CONES

We start with a simple observation about the positive semidefinite cones introduced in
Definition S28.
Fact S56. If k ⩽ n, then PSDk is a retract of PSDn .
Proof. Identify Ck with a subspace of Cn , let π : Cn → Ck a projection onto Ck . Then
the identity map Ψ : Mk → Mn and the map Φ : Mn → Mk defined by Φ(A) = πAπ † are
positive and satisfy Φ ◦ Ψ = IdMk , as needed.
Our proof of Theorem 3 is based on properties of the Lorentz cone, defined for an integer
n by


q
n+1
2
2
Ln := (x1 , . . . , xn+1 ) ∈ R
: x1 + · · · + xn ⩽ xn+1 .
Note that dim(Ln ) = n + 1, and that the cone Ln is self-dual, i.e. L∗n = Ln (we identify Rn
with its dual space in the usual way). Theorem 3 will be a consequence of the following
propositions.

Proposition S6. Let C be a proper cone with dim(C) ⩽ n + 1. Then the pair (C, Ln ) is
nuclear if and only if C is classical.
Proposition S7. For every n ⩾ 1, the cone L2n is a retract of PSD2n .
Before proving Propositions S6 and S7, we show how they imply together Theorem 3.
The easy direction has been covered in the main text. For the other direction, assume
that the pair (C, PSDn ) is nuclear, with ⌊log2 n⌋ ⩾ d/2 and dim(C) = d. Using Fact S56
and Proposition S7 together with our assumption ⌊log2 n⌋ ⩾ d−1
2 implies that Ld−1 is a
retract of PSDn . By Proposition 8, we obtain that the pair (C, Ld−1 ) is nuclear. Finally,
Proposition S6 implies that C is classical.
Let us first consider for r > 0


q
n+1
2
2
:=
Ln (r)
(x1 , . . . , xn+1 ) ∈ R
: x1 + · · · + xn ⩽ rxn+1
and note that Ln (r) = C (rB2n ), where B2n is the unit Euclidean ball in Rn . Obviously,
Ln = Ln (1).
In order to prove Proposition S6, we will need the following lemma. It is a consequence
of [32, Lemma 19]. However, for completeness, we include a direct proof.
Lemma S8. Given a natural number n and a nonnegative real number r, the inclusion
Ln  Ln ⊆ Ln  Ln (r)
implies r ⩾ n.
17

<!-- page 41 -->
We will also use the following extremal properties of simplices, which can be found in [45]
(see also [46, Theorem 1]).
Theorem S9. Let K ⊂ Rn be a convex body which is not a simplex. Then there exists
an affine bijection Φ : Rn → Rn such that B2n ⊆ Φ(K) ⊆ rB2n for some positive number r
satisfying r < n.
Applying Theorem S9 to K being the base of a cone, and using Fact S15, we obtain the
following variant.
Corollary S10. Let C ⊂ Rn+1 be a proper cone which is not classical. Then C is isomorphic to a proper cone C ′ ⊂ Rn+1 satisfying Ln ⊆ C ′ ⊆ Ln (r) for some number r with
1 ⩽ r < n.
Proof of Proposition S6. We will proceed by contradiction. Assume that there exists a
non-classical proper cone C with dim(C) = n + 1 and such that the pair (C, Ln ) is nuclear.
Using Corollary S10 (and Fact S26), we may assume that Ln ⊆ C ⊆ Ln (r) for some r < n.
Then, we can write
Ln  Ln ⊆ Ln  C = Ln  C ⊆ Ln  Ln (r),
contradicting Lemma S8.
P
n+1 ⊗ Rn+1 , with
Proof of Lemma S8. Let us consider the element z = n+1
i=1 ei ⊗ ei ∈ R
(ei ) the canonical basis of Rn+1 . We will show that z ∈ Ln  Ln , while z ∈ Ln  Ln (r)
implies r ⩾ n.
Let us first show that z ∈ Ln  Ln = (L∗n  L∗n )∗ = (Ln  Ln )∗ , where in the last equality
we have used that Ln is a selfdual cone. To this end, it is enough to check the inequality
hz, a ⊗ bi ⩾ 0 for a, b ∈ Ln , since elements of the form a ⊗ b generate the cone Ln  Ln . We
then write
hz, a⊗ bi =

Xn+1
i=1

ai bi ⩾ an+1 bn+1 −

Xn

i=1

ai bi ⩾ an+1 bn+1 −

Xn

i=1

a2i

 1 Xn
2

i=1

b2i

1

2

,

where in the last step we have used Cauchy–Schwarz inequality. The last expression is
nonnegative because a, b ∈ Ln , and we conclude that z ∈ (Ln  Ln )∗ = Ln  Ln .
P
In order to show that z = P n+1
i=1 ei ⊗ ei ∈ Ln  Ln (r) implies r ⩾ n, let us consider an
arbitrary decomposition z = k xk ⊗ yk such that xk ∈ Ln and yk ∈ Ln (r) for every k.
We denote by k · k2 the standard Euclidean norm on Rn+1 and by k · k1 the trace norm in
18

<!-- page 42 -->
Rn+1 ⊗ Rn+1 identified with Mn+1 (R). We have
Xn

n=

i=1

X
k

=

1

(xk (i))ni=1 ⊗ (yk (i))ni=1
k

=
⩽

ei ⊗ ei

X

X
k

⩽r

1

k(xk (i))ni=1 ⊗ (yk (i))ni=1 k1

k(xk (i))ni=1 k2 k(yk (i))ni=1 k2

X

xk (n + 1)yk (n + 1)

k

= r.
This concludes the proof.

Proof of Proposition S7. We use the well-known fact (see for example the proof of Lemma
11.2 in [50]) that one can find self-adjoint and trace zero matrices U1 , . . . , U2n ∈ Msa
2n (C)
such that
Ui Uj + Uj Ui = 2δi,j Id for every i, j = 1, . . . , 2n.
This property immediately implies that for all real numbers x1 , . . . , x2n ,
X2n

i=1

x i Ui

2

=

X2n

i=1


x2i Id.

2n+1 and Ψ : R2n+1 → Msa by
Define linear maps Φ : Msa
2n
2n → R

Φ(A) = (Tr(AU1 ), · · · , Tr(AU2n ), Tr A)
and
Ψ(x) =

2n
X

xi Ui + x2n+1 Id .

i=1

Proposition S7 is an immediate consequence of the following three properties:
(1) Φ(PSDn ) ⊂ L2n ;
(2) Ψ(L2n ) ⊂ PSDn ; and
(3) Φ ◦ Ψ = 2n IdR2n+1 .
19

(S17)

<!-- page 43 -->
In order to prove (1), note that for every A ∈ PSD2n and x ∈ R2n , we have that
2n
X
i=1

 X2n

X2n
xi Tr(AUi ) = Tr A
xi Ui ⩽ kAk1
xi Ui = kxk2 Tr A .
i=1

i=1

By taking the supremum over x such that kxk2 ⩽ 1, we conclude that
X2n

i=1

(Tr AUi )2

1/2

⩽ Tr A

and therefore Φ(A) ∈ L2n .
P
To prove (2), observe that for a given x ∈ L2n the matrix Ψ(x) = 2n
i=1 xi Ui + x2n+1 Id is
positive semidefinite due to (S17). Finally, (3) follows from the facts that Tr(Ui Uj ) = 2n δi,j
and Tr(Ui ) = 0 for every i.
The tools we introduced can be used to derive a simple proof of Theorem 3’.
Proof of Theorem 3’. Let C be a proper polyhedral cone which is not classical, and n ⩾ 2.
We combine the following facts: (a) by Proposition S5, C admits a non-classical retract C ′
of dimension 3, and (b) the Lorentz cone L2 is a retract of PSDn . Since L2 is not classical
(a disk is not a triangle!), the pair (C ′ , L2 ) is entangleable (Theorem 1) and therefore the
pair (C, PSDn ) is entangleable as well (Proposition 8). It remains to justify point (b) in
the previous argument. This is easy: by Fact S56, it is enough to prove (b) for n = 2.
Since PSD2 is isomorphic to L3 , this amounts to proving that L2 is a retract of L3 , which is
geometrically obvious.
V.
A.

PROOF OF THEOREM 4

Entanglement robustness in GPTs

The entanglement robustness is an entanglement measure that was constructed and
studied in the early days of entanglement theory [26]. It differs from other quantifiers in
that it has a purely geometric nature. In fact, it can be thought of as the minimal amount
of noise, in the form of a convex mixture with a separable state, that makes the state
separable. As it is rooted in convex geometry alone, the entanglement robustness can be
extended from quantum mechanics to arbitrary GPTs in a straightforward manner. Given
two arbitrary GPTs (V1 , C1 , u1 ) and (V2 , C2 , u2 ), and a state ω ∈ C1  C2 , we set
Erob (ω) := min {(u1 ⊗ u2 )(ζ) : ζ, ω + ζ ∈ C1  C2 } .

(20)

It is not difficult to verify that the above definition possesses all the basic properties of
an entanglement measure. First, it is everywhere non-negative and finite, because C1  C2
20

<!-- page 44 -->
is a proper cone with a non-empty interior. Secondly, it is faithful, namely, it vanishes
(only on) separable states. Lastly, it is monotonically non-increasing under normalised
separability-preserving maps, as the next lemma shows.
Lemma S11. For i = 1, 2, let (Vi , Ci , ui ) and (Vi′ , Ci′ , u′i ) be GPTs. Consider two compos′ such that (2) holds for both. Let Λ : V ⊗ V → V ′ ⊗ V ′ be a map that is:
ites C12 and C12
1
2
1
2
′ ; (ii) normalised, i.e. satisfies Λ∗ (u′ ⊗ u′ ) = u ⊗ u ;
(i) positive, i.e. obeys Λ(C12 ) ⊆ C12
1
2
1
2
and (iii) separability-preserving, namely, such that Λ (C1  C2 ) ⊆ C1′  C2′ . Then, for all
input states ω ∈ C12 it holds that Erob (Λ(ω)) ⩽ Erob (ω).
Proof. Let ζ ∈ C1  C2 be the vector that achieves the minimum in (20) for ω. Since
Λ(ζ), Λ(ω) + Λ(ζ) ∈ C1′  C2′ , we have that

Erob (Λ(ω)) ⩽ (u′1 ⊗ u′2 ) (Λ(ζ)) = Λ∗ (u′1 ⊗ u′2 ) (ζ) = (u1 ⊗ u2 )(ζ) = Erob (ω) ,

which completes the proof.

B.

Symmetric cones

We start by fixing some notation. For a proper cone (V, C, u), define the vector subspace
X := ker(u) := {x ∈ V : u(x) = 0} ;

(S18)

once we fix a state γ ∈ Ω := C ∩ u−1 (1), we can decompose V = X ⊕ (Rγ), meaning that
every v ∈ V can be written as v = αγ + x, where α ∈ R and x ∈ X.
We now construct the function NX : X → R+ given by

NX (x) := inf t > 0 : γ + t−1 x ∈ C ,
(S19)

where it is understood that the infimum of the empty set is +∞. Note that in (S19) we can
substitute C with Ω. Now, NX obeys the triangle inequality in general, i.e. that NX (x+y) ⩽
NX (x) + NX (y) for all x, y ∈ X. Also, NX is manifestly positively homogeneous, i.e.
NX (λx) = λNX (x) for all λ ⩾ 0. If Ω is centrally symmetric with centre γ, then also
absolute homogeneity holds, i.e. NX (λx) = λNX (x) for all λ ∈ R.
As already mentioned, it follows from Fact S13(c) that the state space Ω is a convex
body when viewed as a subset of the affine space u−1 (1) = γ + X. This implies that the
function NX defined by (S19) satisfies NX (x) > 0 for all x 6= 0. Indeed, if this were not the
case we will immediately deduce that γ + nx ∈ Ω for all positive integers n, which would
in turn imply that Ω is non-compact. If γ ∈ relint(Ω), then we also have that NX (x) < ∞
for all x ∈ X. Observe that the centre of a convex body, if it exists, must lie in its relative
interior. We summarise the above discussion as follows.
Fact S57. For any symmetric GPT (V, C, u), the function NX defined by (S19) is a norm
on X.
21

<!-- page 45 -->
From now on we will assume that (V, C, u) is a symmetric GPT. Accordingly, we will
adopt the more suggestive notation k · kX := NX (·). Observe that the unit ball of k · kX is
just the state space of (V, C, u), i.e.
BX = Ω − γ = C ∩ u−1 (1) − γ .

(S20)

For future convenience, let us also define Π : V → X as the projection onto X with γ in its
kernel, explicitly given by the formula
Π(v) := v − u(v)γ ,

(S21)

C = {v ∈ V : kΠ(v)kX ⩽ u(v)} .

(S22)

for all v ∈ V . Observe that

Note that since norms are invariant under a change of sign, we have that u(v)γ − Π(v) ∈ C
for all v ∈ C; in fact,
kΠ(u(v)γ − Π(v))kX = k−Π(v)kX ⩽ u(v) = u (u(v)γ − Π(v)) .

(S23)

We formalise this observation as follows.
Fact S58. A symmetric cone C is invariant under the inversion v 7→ u(v)γ − Π(v) =
2u(v)γ − v.
Another curious feature of symmetric GPTs is that their dual spaces can also be equipped
with a GPT structure.
Lemma S12. Let (V, C, u) be a symmetric GPT with centre γ ∈ V = V ∗∗ . Then
(a) (V ∗ , C ∗ , γ) is also a symmetric GPT with centre u;
(b) the corresponding space X ∗ := ker(γ) normed by BX ∗ := C ∗ ∩ γ −1 (1) − u coincides
(as a normed space) with the dual of X; and
(c) the projection onto X ∗ with u in its kernel coincides with the adjoint of Π defined
by (S21).
Proof. Let v ∗ ∈ Ω∗ := C ∗ ∩ γ −1 (1), and let us show that 2u − v ∗ ∈ Ω∗ . On the one hand,
clearly (2u − v ∗ )(γ) = 1. On the other, for an arbitrary v ∈ C satisfying the constraint
in (S22), we see that (2u − v ∗ )(v) = v ∗ (2u(v)γ − v) ⩾ 0, where the last inequality follows
22

<!-- page 46 -->
from Fact S58. We conclude that 2u − v ∗ ∈ C ∗ , proving the first claim. As for the second,
pick f ∈ ker(γ) ⊂ V ∗ ; then


inf t > 0 : u + t−1 f ∈ C ∗ = inf t > 0 : (u + t−1 f )(v) ⩾ 0 ∀ v ∈ C

= inf t > 0 : (u + t−1 f )(γ − x) ⩾ 0 ∀ x ∈ BX
= inf {t > 0 : f (x) ⩽ t ∀ x ∈ BX }
= sup f (x)
x∈BX

= kf kX ∗ .
This proves that the norm induced on X ∗ by the construction in (S19) coincides with the
dual norm of k · kX as given by Definition S41. The third claim is also straightforward. It
suffices to observe that for all v ∈ V and v ∗ ∈ V ∗ it holds that
(v ∗ − v ∗ (γ)u)(v) = v ∗ (v) − u(v)v ∗ (γ) = v ∗ (v − u(v)γ) = v ∗ (Π(v)) = (Π∗ (v ∗ )) (v) ,

implying that Π∗ (v ∗ ) = v ∗ − v ∗ (γ)u.
We now move on to the bipartite setting. For i = 1, 2, let (Vi , Ci , ui ) be a symmetric
GPT with centre γi ∈ Ωi := Ci ∩ u−1
i (1). Call Xi := ker(ui ), and let Πi be the projection
onto Xi with γi ∈ ker(Πi ).
Lemma S13 (see [8, Proposition 2.25]). With the above notation, for every ω ∈ V1 ⊗ V2
we have that
(a) if ω ∈ C1  C2 then k(Π1 ⊗ Π2 )(ω)kX1 ⊗π X2 ⩽ (u1 ⊗ u2 )(ω);
(b) if ω ∈ C1  C2 then k(Π1 ⊗ Π2 )(ω)kX1 ⊗ǫ X2 ⩽ (u1 ⊗ u2 )(ω).
Moreover, for all z ∈ X1 ⊗ X2 ,
(c) if kzkX1 ⊗π X2 ⩽ 1 then γ1 ⊗ γ2 + z ∈ C1  C2 ;
(d) if kzkX1 ⊗ε X2 ⩽ 1 then γ1 ⊗ γ2 + z ∈ C1  C2 .
P
Proof. We start with claim (a). Let ω ∈ C1  C2 be decomposed as ω = j vj ⊗ wj , where
vj ∈ C1 and wj ∈ C2 . By (S22), we have that kΠ1 (vj )kX1 ⩽ u1 (vj ) and kΠ2 (wj )kX2 ⩽
u2 (wj ) for all j. Using (S7), we deduce that
X
k(Π1 ⊗ Π2 )(ω)kX1 ⊗π X2 =
Π1 (vj ) ⊗ Π2 (wj )
j
X1 ⊗ π X2
X
⩽
kΠ1 (vj )kX1 kΠ2 (wj )kX2
j

⩽

X

u1 (vj ) u2 (wj )

j

= (u1 ⊗ u2 ) (ω) .
23

<!-- page 47 -->
We now move on to (c). By closedness of C1  C2 , we can assume without loss of generality
that P
kzkX1 ⊗π X2 < 1 holds P
with strict inequality. By (S7), there exists a decomposition
z =
i xi ⊗ yi such that
i kxi kX1 kyi kX2 < 1. We now write the following explicitly
separable decomposition for γ1 ⊗ γ2 + z ∈ C1  C2 :


X
γ1 ⊗ γ2 + z = 1 −
kxi kX1 kyi kX2 γ1 ⊗ γ2
i
 

X kxi kX kyi kX  
yi
xi
1
2
⊗ γ2 +
γ1 +
+
2
kxi kX1
kyi kX2
i

 

xi
yi
+ γ1 −
⊗ γ2 −
.
kxi kX1
kyi kX2
This proves claim (c).
Claims (b) and (b) follow by duality. We start with (b). Since (Vi∗ , Ci∗ , γi ) are symmetric
GPTs, applying (c) to them shows that for all h ∈ X1∗  X2∗ with khkX ∗ ⊗π X ∗ ⩽ 1 it holds
1
2
that u1 ⊗ u2 − h ∈ C1∗  C2∗ . Hence, all ω ∈ C1  C2 = (C1∗  C2∗ )∗ are such that
0 ⩽ (u1 ⊗ u2 − h)(ω) = (u1 ⊗ u2 )(ω) − h(ω) = (u1 ⊗ u2 )(ω) + h ((Π1 ⊗ Π2 )(ω)) .
Optimising over all h ∈ BX1∗ ⊗π X2∗ and applying (S5) as well as the duality formula (S9)
yields the inequality in (b).
Thanks to (S3), to prove (d) it suffices to verify that ξ(γ1 ⊗γ2 +z) ⩾ 0 for all ξ ∈ C1∗ C2∗ .
Indeed,
ξ(γ1 ⊗ γ2 + z) = ξ(γ1 ⊗ γ2 ) + ξ ((Π1 ⊗ Π2 )(z))

= ξ(γ1 ⊗ γ2 ) + ((Π∗1 ⊗ Π∗2 )(ξ)) (z)

(i)

⩾ ξ(γ1 ⊗ γ2 ) − k(Π∗1 ⊗ Π∗2 )(ξ)k(X1 ⊗ε X2 )∗ kzkX1 ⊗ε X2

(ii)

= ξ(γ1 ⊗ γ2 ) − k(Π∗1 ⊗ Π∗2 )(ξ)kX ∗ ⊗π X ∗ kzkX1 ⊗ε X2
1

2

(iii)

⩾ ξ(γ1 ⊗ γ2 ) − k(Π∗1 ⊗ Π∗2 )(ξ)kX ∗ ⊗π X ∗
1

2

(iv)

⩾ 0,
where (i) is an application of (S5) to the normed space X1 ⊗ε X2 , (ii) descends from (S8),
(iii) holds by hypothesis, and finally (iv) is just the inequality in (a) stated at the dual
level.
The above Lemma S13 gives us a natural way to construct candidate entangled tensors
when the local theories are symmetric. For z ∈ X1 ⊗ X2 with kzkX1 ⊗ε X2 ⩽ 1, the state
ω(z) := γ1 ⊗ γ2 + z
satisfies ω(z) ∈ C1  C2 .
24

(S24)

<!-- page 48 -->
C.

Proof of Theorem 4

We start by proving Lemma 14 as stated in the main text. This allows us to connect
the entanglement robustness of states of the form (S24) with the projective/injective tensor
norm ratio of the parent tensor.
Lemma 14. Let (V1 , C1 , u1 ), (V2 , C2 , u2 ) be two symmetric GPTs. Call γ1 , γ2 the centres
of the state spaces, and X1 , X2 the associated normed spaces. For z ∈ X1 ⊗ X2 , consider
the normalised state ω(z) := γ1 ⊗ γ2 + z. Whenever z satisfies kzkX1 ⊗ε X2 ⩽ 1, it holds that
ω(z) ∈ C1  C2 . In this case,
Erob (ω(z)) ⩾

kzkX1 ⊗π X2 − 1
.
2

(S25)

Proof. The first claim is just Lemma S13(d). We now focus on the second. Let ζ ∈ V1 ⊗ V2
be such that ζ, ω(z) + ζ ∈ C1  C2 . Then,
kzkX1 ⊗π X2 − (u1 ⊗ u2 )(ζ) = k(Π1 ⊗ Π2 )(ω(z))kX1 ⊗π X2 − (u1 ⊗ u2 )(ζ)
(i)

⩽ k(Π1 ⊗ Π2 )(ω(z))kX1 ⊗π X2 − k(Π1 ⊗ Π2 )(ζ)kX1 ⊗π X2

(ii)

⩽ k(Π1 ⊗ Π2 )(ω(z) + ζ)kX1 ⊗π X2

(iii)

⩽ (u1 ⊗ u1 ) (ω(z) + ζ)

(iv)

= 1 + (u1 ⊗ u2 )(ζ) .

The above steps are justified as follows: (i) follows from Lemma S13(a) applied to ζ ∈
C1  C2 ; (ii) is just an application of the triangle inequality; (iii) is again Lemma S13(a),
this time applied to ω(z) + ζ ∈ C1  C2 ; and (iv) descends from the easily verified fact that
ω(z) as defined in (S24) is normalised.
The above reasoning implies that 2(u1 ⊗ u2 )(ζ) ⩾ kzkX1 ⊗π X2 − 1. Taking the infimum
over all ζ and using the definition Eq. (20) yields precisely Eq. (S25). This concludes the
proof.
We are finally ready to prove Theorem 4.
Proof of Theorem 4. Consider a pair of symmetric GPTs of dimensions n + 1, m + 1 ⩾ 3.
Call X1 , X2 the normed spaces associated with them via (S18) and (S19). Since dim X1 =
n and dim X2 = m, applying Definition S46 we see that ρ(X1 , X2 ) ⩾ r(n, m). Now,
remember from Fact S45 that ρ(X1 , X2 ) is the smallest constant such that kzkX1 ⊗π X2 ⩽
ρ(X1 , X2 )kzkX1 ⊗ε X2 holds for all z ∈ X1 ⊗ X2 . Hence, by compactness, there must exist
a tensor z0 that satisfies this inequality with equality. Up to a multiplicative constant, we
25

<!-- page 49 -->
can assume without loss of generality that kz0 kX1 ⊗ε X2 = 1 and hence that kzkX1 ⊗π X2 =
ρ(X1 , X2 ). Then, the estimate in (S25) ensures that
Erob (ω(z0 )) ⩾

r(n, m) − 1
kz0 kX1 ⊗π X2 − 1
⩾
.
2
2

(S26)

The claims then follow from Facts S47 and S48, in turn derived from [27].

VI.

MORE ABOUT RETRACTS

Proof of Proposition S1. We show that there exists a projection P : V → E such that
P (C) = C ∩ E. Let x and y be generators of the 2 extremal rays of the 2-dimensional
cone C ∩ E. Denote by Tx and Ty tangent hyperplanes to C at x and y. We define P by
ker(P ) = Tx ∩ Ty . Consider any element z ∈ C ; a (projective) geometric argument in the
affine plane generated by x, y and z (see Figure 3) shows that P (z) ∈ C ∩ E.
E

Tx

•

x

C
z
•
•

y

Ty

FIG. 3. The image of z under P is a positive multiple of the intersection between E and the
(dashed) line through z and Tx ∩ Ty , and therefore belongs to C.

One could be tempted to conjecture that every cone has some nontrivial retract. However, this is remarkably not the case, as we show now. Our argument relies heavily on a
notable result by Zamfirescu [55]. Before we delve into the details, we need to introduce
some notation. Let Kn denote the family of all convex bodies (compact convex sets with
nonempty interior) in Rn . We can endow Kn with the Hausdorff distance, defined as
dH (X, Y ) := inf {ǫ > 0 : X ⊆ Yǫ , Y ⊆ Xǫ }
26

(S27)

<!-- page 50 -->
for all X, Y ∈ Kn , where for a convex body K ∈ Kn we denoted by Kǫ := {x ∈ Rn : d(x, K) ⩽ ǫ}
its ‘ǫ-fattening’. Here, d(x, K) quantifies the distance of x from K as measured by the
Euclidean norm. It is well known that Kn equipped with dH becomes a complete metric
space [56, Thm. 1.8.2, 1.8.5] and hence a Baire space. We remind the reader a property is
said to be obeyed by most elements in a Baire space if those that violate it form a meagre
set, i.e. a countable union of sets whose closure has empty interior.
For K ∈ Kn and x ∈
/ K, the shadow boundary of K with respect to x is defined as
∂(K, x) := {y ∈ K : aff{x, y} ∩ int(K) = ∅} ,

(S28)

where aff denotes the affine hull, and hence aff{x, y} is nothing but the straight line through
x and y. It is easily verified that the above definition can be straightforwardly extended
to the more general case where x ∈ Pn \ K, where Pn denotes the real projective space of
dimension n.4 The result by Zamfirescu [55, Thm. 1] asserts that for most convex bodies
in Kn it holds that
dim aff ∂(K, x) = n

∀ x ∈ Pn \ K .

(S29)

The following lemma shows that having retracts is an exceptional property. In particular,
this shows that the conclusion of Proposition S2 is true for most convex cones.
Lemma S14. For all n ⩾ 4, most convex bodies K ∈ Kn−1 are such that the cone C (K)
constructed via (S1) has no (n − 1)-dimensional retracts.
Proof. Most convex bodies obey (S29) by Zamfirescu’s theorem. Moreover, it is known
that most convex bodies are strictly convex [56, Thm. 2.6.1], meaning that their boundary
contains no nontrivial segment. Hence, most convex body are simultaneously strictly convex
and obey (S29). We proceed to show that any such convex body K ∈ Kn−1 defines
via (S1) an n-dimensional cone C (K) that has no (n−1)-dimensional retracts. By Fact S38,
is it enough to show that there is no projection P : Rn → V of rank n − 1 satisfying
P (C (K)) = C (K) ∩ V .
Consider K as embedded in the affine subspace H defined by setting the last coordinate
of Rn to 1. Assume that C (K) admits a retract to an (n − 1)-dimensional subspace V ,
and set W := V ∩ H. Call P : Rn → V a projection that satisfies P (C (K)) = C (K) ∩ V .
Clearly, dim ker P = 1, i.e. ker P is a straight line. Consider the point x ∈ Pn−1 such that
{x} = H ∩ ker P (observe that x can be at infinity, when ker P is parallel to H). Then
we claim that: (i) x ∈
/ K; and (ii) ∂(K, x) ⊆ W . This contradicts the assumption that
dim aff ∂(K, x) = n − 1.
To prove (i), assume that x ∈ K = int(K) ∪ ∂K. If x ∈ int(K), then it must be
that P ≡ 0, which is naturally absurd. In fact, if P y 6= 0 for some y ∈ Rn , using
4

A useful way to think about Pn is as follows. Consider a hyperplane Hn of dimension n in an (n + 1)dimensional space. Pick a point p ∈
/ Hn . While Rn can be identified with Hn , the projective space
Pn can be thought of as the set of straight lines through p. The natural embedding Rn ⊂ Pn can be
obtained by noticing that those lines through p that are not parallel to Hn identify a unique point on it.

27

<!-- page 51 -->
the fact that ty + x ∈ C (K) for all t ∈ (−ǫ, ǫ) (where ǫ > 0), we would obtain that
P (ty + x) = tP y ∈ P (C (K)) = C (K) ∩ V for t in a neighbourhood of 0, which is in
contradiction with C (K) being proper. If x ∈ ∂K, take y ∈ ∂(K ∩ W ) ⊆ ∂K ∩ W .
Since for all λ ∈ [0, 1] one has that P (λx + (1 − λ)y) = (1 − λ)y ∈ ∂C (K), and since
P (C (K)) ⊆ C (K), we deduce that λx + (1 − λ)y ∈ ∂C (K) ∩ H = ∂K for all λ ∈ [0, 1]; this
contradicts the assumption that K is strictly convex.
We now move on to (ii). Since x ∈
/ K, the shadow boundary ∂(K, x) is nonempty.
Assume by contradiction that there is y ∈ ∂(K, x) \ W . This means that y − P y = µx for
some real µ 6= 0. For λ ∈ R, consider the point


λ
λ
y − Py .
zλ := λx + (1 − λ)y = 1 − λ +
µ
µ
It is not difficult to check that since µ 6= 0 one can satisfy both 1 − λ + λ/µ ⩾ 0 and
λ/µ ⩽ 0 for all λ in a nontrivial left- or right-neighbourhood of 0. For such values of λ one
obtains that zλ ∈ C (K), and since zλ ∈ H by construction it holds in fact that zλ ∈ K. We
have shown that there is a nontrivial segment in the straight line aff{x, y} (one of whose
extremes is y) that is entirely contained in K. Since K is strictly convex, it cannot be that
this segment is entirely contained in the boundary ∂K. Hence, it must intersect the interior
int(K). This contradicts the assumption that y ∈ ∂(K, x), and concludes the proof.

28
