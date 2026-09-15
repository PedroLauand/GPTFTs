---
type: paper
date: 2010-11-30
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1011.6451v3)
reviewed: false
---

# Informational derivation of Quantum Theory

Machine-generated and unreviewed text extraction of arXiv:1011.6451v3
(48 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1011.6451v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Informational derivation of Quantum Theory
Giulio Chiribella∗
Perimeter Institute for Theoretical Physics, 31 Caroline Street North, Ontario, Canada N2L 2Y5.†

Giacomo Mauro D’Ariano‡ and Paolo Perinotti§

QUIT Group, Dipartimento di Fisica “A. Volta” and INFN Sezione di Pavia, via Bassi 6, 27100 Pavia, Italy¶
(Dated: November 26, 2024)

arXiv:1011.6451v3 [quant-ph] 15 Jul 2011

We derive Quantum Theory from purely informational principles. Five elementary axioms—
causality, perfect distinguishability, ideal compression, local distinguishability, and pure
conditioning—define a broad class of theories of information-processing that can be regarded as
standard. One postulate—purification—singles out quantum theory within this class.
PACS numbers: 03.67.-a, 03.67.Ac, 03.65.Ta

CONTENTS

I. Introduction

1

II. The framework
A. Circuits with outcomes
B. Probabilistic structure: states, effects and
transformations
C. Basic definitions in the
operational-probabilistic framework
1. Coarse-graining, refinement, atomic
transformations, pure, mixed and
completely mixed states
2. Examples in in quantum theory
D. Operational principles

4
4

6
7
7

III. The principles
A. Axioms
1. Causality
2. Perfect distinguishability
3. Ideal compression
4. Local distinguishability
5. Pure conditioning
B. The purification postulate

8
8
8
9
10
10
10
11

IV. First consequences of the principles
A. Results about ideal compression
B. Results about purification
C. Results about the combination of
compression and purification
D. Teleportation and the link product
E. No information without disturbance

11
11
12

V. Perfectly distinguishable states

16

5
6

14
14
15

VI. Duality between pure states and atomic effects 18

∗ gchiribella@perimeterinstitute.ca
† http://www.perimeterinstitute.ca

VII. Dimension

19

VIII. Decomposition into perfectly distinguishable
pure states

20

IX. Teleportation revisited
A. Probability of teleportation
B. Isotropic states and effects
C. Dimension of the state space

23
23
23
24

X. Derivation of the qubit

26

XI. Projections
27
A. Orthogonal faces and orthogonal
complements
28
B. Projections
30
C. Projection of a pure state on two orthogonal
faces
33
XII. The superposition principle
A. Completeness for purification
B. Equivalence of systems with equal
dimension
C. Reversible operations of perfectly
distinguishable pure states

34
35

XIII. Derivation of the density matrix formalism
A. The basis
B. The matrices
C. Choice of axes for a two-qubit system
D. Positivity of the matrices
E. Quantum theory in finite dimensions

36
36
37
38
43
44

XIV. Conclusion

46

35
35

Acknowledgments

46

References

47

I.

INTRODUCTION

‡ dariano@unipv.it
§ paolo.perinotti@unipv.it
¶ http://www.qubit.it

More than eighty years after its formulation, quantum
theory is still mysterious. The theory has a solid mathe-

<!-- page 2 -->
2
matical foundation, addressed by Hilbert, von Neumann
and Nordheim in 1928 [1] and brought to completion in
the monumental work by von Neumann [2]. However,
this formulation is based on the abstract framework of
Hilbert spaces and self-adjoint operators, which, to say
the least, are far from having an intuitive physical meaning. For example, the postulate stating that the pure
states of a physical system are represented by unit vectors
in a suitable Hilbert space appears as rather artificial:
which are the physical laws that lead to this very specific choice of mathematical representation? The problem with the standard textbook formulations of quantum
theory is that the postulates therein impose particular
mathematical structures without providing any fundamental reason for this choice: the mathematics of Hilbert
spaces is adopted without further questioning as a prescription that “works well” when used as a black box
to produce experimental predictions. In a satisfactory
axiomatization of Quantum Theory, instead, the mathematical structures of Hilbert spaces (or C*-algebras)
should emerge as consequences of physically meaningful
postulates, that is, postulates formulated exclusively in
the language of physics: this language refers to notions
like physical system, experiment, or physical process and
not to notions like Hilbert space, self-adjoint operator, or
unitary operator. Note that any serious axiomatization
has to be based on postulates that can be precisely translated in mathematical terms. However, the point with
the present status of quantum theory is that there are
postulates that have a precise mathematical statement,
but cannot be translated back into language of physics.
Those are the postulates that one would like to avoid.
The need for a deeper understanding of quantum theory in terms of fundamental principles was clear since
the very beginning. Von Neumann himself expressed
his dissatisfaction with his mathematical formulation of
Quantum Theory with the surprising words “I don’t believe in Hilbert space anymore”, reported by Birkhoff
in [3]. Realizing the physical relevance of the axiomatization problem, Birkhoff and von Neumann made an
attempt to understand quantum theory as a new form
of logic [4]: the key idea was that propositions about
the physical world must be treated in a suitable logical
framework, different from classical logics, where the operations AND and OR are no longer distributive. This
work inaugurated the tradition of quantum logics, which
led to several attempts to axiomatize quantum theory,
notably by Mackey [5] and Jauch and Piron [6] (see Ref.
[7] for a review on the more recent progresses of quantum logics). In general, a certain degree of technicality,
mainly related to the emphasis on infinite-dimensional
systems, makes these results far from providing a clearcut description of quantum theory in terms of fundamental principles. Later Ludwig initiated an axiomatization
program [8] adopting an operational approach, where the
basic notions are those of preparation devices and measuring devices and the postulates specify how preparations and measurements combine to give the probabilities

of experimental outcomes. However, despite the original
intent, Ludwig’s axiomatization did not succeed in deriving Hilbert spaces from purely operational notions, as
some of the postulates still contained mathematical notions with no operational interpretation.
More recently, the rise of quantum information science
moved the emphasis from logics to information processing. The new field clearly showed that the mathematical
principles of quantum theory imply an enormous amount
of information-theoretic consequences, such as the nocloning theorem [9, 10], the possibility of teleportation
[11], secure key distribution [12–14], or of factoring numbers in polynomial time [15]. The natural question is
whether the implication can be reversed: is it possible
to retrieve quantum theory from a set of purely informational principles? Another contribution of quantum
information has been to shift the emphasis to finite dimensional systems, which allow for a simpler treatment
but still possess all the remarkable quantum features. In
a sense, the study of finite dimensional systems allows
one to decouple the conceptual difficulties in our understanding of quantum theory from the technical difficulties
of infinite dimensional systems.
In this scenario, Hardy’s 2001 work [16] re-opened
the debate about the axiomatizations of quantum theory
with fresh ideas. Hardy’s proposal was based on five main
assumptions about the relation between dimension of the
state space and the number of perfectly distinguishable
states of a given system, about the structure of composite systems, and about the possibility of connecting any
two pure states of a physical system through a continuous path of reversible transformations. However, some
of these assumptions directly refer to the mathematical
properties of the state space (in particular, the “Simplicity Axiom” 2, which is an abstract statement about
the functional dependence of the state space dimension
on the number of perfectly distinguishable states). Very
recently, building on Hardy’s work there have been two
new attempts of axiomatization by Dakic and Brukner
[17] and Masanes and Müller [18]. Although these works
succeeded in removing the “Simplicity Axiom”, they still
contain mathematical assumptions that cannot be understood in elementary physical terms (see e.g. requirement
5 of Ref. [18], which assumes that “all mathematically
well-defined measurements are allowed by the theory”).
Another approach to the axiomatization of quantum
theory was pursued by one of the authors in a series of
works [19] culminated in Ref. [20]. These works tackled the problem using operational principles related to
tomography and calibration of physical devices, experimental complexity, and to the composition of elementary
transformations. In particular this research introduced
the concept of dynamically faithful states, namely states
that can be used for the complete tomography of physical processes. Although this approach went very close
to deriving quantum theory also in this case one mathematical assumption without operational interpretation
was needed (see the CJ postulate of Ref. [20]).

<!-- page 3 -->
3
In this paper we provide a complete derivation of finite
dimensional quantum theory based of purely operational
principles. Our principles do not refer to abstract properties of the mathematical structures that we use to represent states, transformations or measurements, but only
to the way in which states, transformations and measurements combine with each other. More specifically, our
principles are of informational nature: they assert basic
properties of information-processing, such as the possibility or impossibility to carry out certain tasks by manipulating physical systems. In this approach the rules by
which information can be processed determine the physical theory, in accordance with Wheeler’s program “it
from bit”, for which he argued that “all things physical are information-theoretic in origin” [22]. Note that,
however, our axiomatization of quantum theory is relevant, as a rigorous result, also for those who do not share
Wheeler’s ideas on the informational origin of physics. In
particular, in the process of deriving quantum theory we
provide alternative proofs for many key features of the
Hilbert space formalism, such as the spectral decomposition of self-adjoint operators or the existence of projections. The interesting feature of these proofs is that they
are obtained by manipulation of the principles, without
assuming Hilbert spaces form the start.
The main message of our work is simple: within a standard class of theories of information processing, quantum
theory is uniquely identified by a single postulate: purification. The purification postulate, introduced in Ref.
[21], expresses a distinctive feature of quantum theory,
namely that the ignorance about a part is always compatible with the maximal knowledge of the whole. The
key role of this feature was noticed already in 1935 by
Schrödinger in his discussion about entanglement [23],
of which he famously wrote “I would not call that one
but rather the characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought”. In a sense, our work can be
viewed as the concrete realization of Schrödinger’s claim:
the fact that every physical state can be viewed as the
marginal of some pure state of a compound system is
indeed the key to single out quantum theory within a
standard set of possible theories. It is worth stressing,
however, that the purification principle assumed in this
paper includes a requirement that was not explicitly mentioned in Schrödinger’s discussion: if two pure states of a
composite system AB have the same marginal on system
A, then they are connected by some reversible transformation on system B. In other words, we assume that all
purifications of a given mixed state are equivalent under
local reversible operations [24].
The purification principle expresses a law of conservation of information, stating that at least in principle,
irreversibility can always be reduced to the lack of control over an environment. More precisely, the purification
principle is equivalent to the statement that every irreversible process can be simulated in an essentially unique
way by a reversible interaction of the system with an en-

vironment, which is initially in a pure state [21]. This
statement can also be extended to include the case of
measurement processes, and in that case it implies the
possibility of arbitrarily shifting the cut between the observer and the observed system [21]. The possibility of
such a shift was considered by von Neumann as a “fundamental requirement of the scientific viewpoint” (see p.
418 of [2]) and his discussion of the measurement process
was exactly aimed to show that quantum theory fulfils
this requirement.
Besides Schrödinger’s discussion on entanglement and
von Neumann’s discussion of the measurement process,
the purification principle is deeply rooted in the structure
of quantum theory. At the purely mathematical level, it
plays a crucial role in the theory of C*-algebras of operators on separable Hilbert spaces, where the purification principle is equivalent to the Gelfand-Naimark-Segal
(GNS) construction [25] and implies the celebrated Stinespring’s theorem [26]. On the other hand, purification is
a cornerstone of quantum information, lying at the origin of most quantum protocols. As it was shown in Ref.
[21], the purification principle directly implies crucial features like no-cloning, teleportation, no-information without disturbance, error correction, the impossibility of bit
commitment, and the “no-programming” theorem of Ref.
[27].
In addition to the purification postulate, our derivation
of quantum theory is based on five informational axioms.
The reason why we call them “axioms”, as opposed to
the the purification “postulate”, is that they are not at
all specific of quantum theory. These axioms represent
standard features of information-processing that everyone would, more or less implicitly, assume. They define a
class of theories of information-processing that includes,
for example, classical information theory, quantum information theory, and quantum theory with superselection
rules. The question whether there are other theories satisfying our five axioms and, in case of a positive answer,
the full classification of these theories is currently an open
problem.
Here we informally illustrate the five axioms, leaving
the more detailed description to the remaining part of
the paper:
1. Causality: the probability of a measurement outcome at a certain time does not depend on the
choice of measurements that will be performed
later.
2. Perfect distinguishability: if a state is not completely mixed (i.e. if it cannot be obtained as a
mixture from any other state), then there exists at
least one state that can be perfectly distinguished
from it.
3. Ideal compression: every source of information can
be encoded in a suitable physical system in a lossless and maximally efficient fashion. Here lossless
means that the information can be decoded without errors and maximally efficient means that every

<!-- page 4 -->
4
state of the encoding system represents a state in
the information source.
4. Local distinguishability: if two states of a composite system are different, then we can distinguish
between them from the statistics of local measurements on the component systems.
5. Pure conditioning: if a pure state of system AB
undergoes an atomic measurement on system A,
then each outcome of the measurement induces a
pure state on system B. (Here atomic measurement
means a measurement that cannot be obtained as
a coarse-graining of another measurement).
All these axioms are satisfied by classical information theory. Axiom 5 is even trivial for classical theory, because
the only pure states of a composite system AB are the
product of pure states of the component systems A and
B, and hence the state of system B will be pure irrespectively of what we do on system A.
A stronger version of axiom 5, introduced in Ref. [20],
is the following:
5’ Atomicity of composition: the sequential composition of two atomic operations is atomic. (Here
atomic transformation means a transformation
that cannot be obtained from coarse-graining).
However, it turns out that Axiom 5 is enough for our
derivation: thanks to the purification postulate we will
be able to show the non-trivial implication: Axiom 5 ⇒
Axiom 5’ (see lemma 16).
The paper is organized as follows. In Sec. II we review
the framework of operational-probabilistic theories introduced in Ref. [21]. This framework will provide the basic
notions needed for the formulation of our principles. In
Sec. III we introduce the principles from which we will
derive Quantum Theory. In Sec. IV we prove some direct
consequences of the principles that will be used later in
the paper. In Sec. V we discuss the properties of perfectly distinguishable states, while in Sec. VI we prove
the existence of a duality between pure states and atomic
effects.
The results about distinguishability and duality of pure
states and atomic effects allow us to show in Sec. VII that
every system has a well defined informational dimension—the operational counterpart of the Hilbert space
dimension. Sec. VIII contains the proof that every state
can be decomposed as a convex combination of perfectly
distinguishable pure states. Similarly, any element of the
vector space spanned by the states can be written as a linear combination of perfectly distinguishable states. This
result corresponds to the spectral theorem for self-adjoint
operators on complex Hilbert spaces. In Sec. IX we prove
some results about the maximum teleportation probability, which allow us to derive a functional relation between
the dimension of the state space and the number of perfectly distinguishable states of the system. The mathematical representation of systems with two perfectly distinguishable states is derived in Sec. X, where we prove

that such systems are indeed two-dimensional quantum
systems—a.k.a. qubits. In Sec. XI we construct projections on the faces of the state space of any system and
prove their main properties. These results lead to the
derivation of the operational analogue of the superposition principle in Sec. XII which allows to prove that systems with the same number of perfectly distinguishable
states are operationally equivalent (Subsec. XII B). The
properties of the projections and the superposition principle are then exploited in Sec. XIII—where we extend
the density matrix representation from qubits to higherdimensional systems, thus proving that a system with d
perfectly distinguishable states is indeed a quantum system with d-dimensional Hilbert space. We conclude the
paper with Sec. XIV, where we review our results, discussing future directions for this research.

II.

THE FRAMEWORK

This Section provides a brief summary of the framework of operational-probabilistic theories, which was formulated in Ref. [21]. We refer to Ref. [21] for an exhaustive presentation of the details of the framework and of
the ideas behind it. The operational-probabilistic framework combines the operational language of circuits with
the toolbox of probability theory: on the one hand, experiments are described by circuits resulting from the
connection of physical devices, on the other hand each
device in the circuit can have classical outcomes and the
theory provides the probability distribution of outcomes
when the devices are connected to form closed circuits
(that is, circuits that start with a preparation and end
with a measurement).
The notions discussed in this section will allow us to
draw a precise distinction between principles with an operational content and exclusively mathematical principles: with the expression ”operational principle” we will
mean a principle that can be expressed using only the
basic notions of the the operational-probabilistic framework.

A.

Circuits with outcomes

A test represents one use of a physical device, like
a Stern-Gerlach magnet, a beamsplitter, or a photon
counter. The device will have an input system and an
output system, labelled by capital letters. The corresponding test can have different classical outcomes, represented by different values of an index i ∈ X:
A

{Ci }i∈X

B

Each outcome i ∈ X corresponds to a possible event,
represented as
A

Ci

B

<!-- page 5 -->
5
We denote by Transf(A, B) the set of all events from A to
B. The reason for this notation is that in the next subsection the elements of Transf(A, B) will be interpreted
as transformations with input system A and output system B. If A = B we simply write Transf(A) in place of
Transf(A, A).
A test with a single outcome will be called deterministic. This name is justified by the fact that, if there is
a single possible outcome, then this outcome will occur
with certainty (cf. the probabilistic structure introduced
in the next subsection).
Two devices can be composed in a sequence, as long
as the input system of the second device is equal to the
output system of the first. The events in the composite
test are represented as
A

Ci

B

Dj

C

σj . Similarly, for effects we will write (ai | (bj | in place of
ai ⊗ b j .
Sequential and parallel composition commute: one
has (Ai ⊗ Bj )(Ck ⊗ Dl ) = Ai Ck ⊗ Bj Dl for every
Ai , Bj , Ck , Dl such that the output of Ai (resp. Bj )
coincides with the input of Ck (resp. Dl ).
When one of the two tests is the identity, we will omit
the box and draw only a straight line, as in
A

IA

A

Ci

B

=

A

Ci

B

B

Dj

A

IA

A

=

B

Dj

A

The rules summarized in this section define the operational language of circuits, which has been discussed
in detail in a series of inspiring works by Coecke (see in
particular Refs. [29, 30]). The language of circuits allows
one to represent the schematic of an experiment, like e.g.

B

C

Dj

D

{Cj }j∈Y
C

and are written in formulas as Ci ⊗ Dj . In the special
case of states we will often write |ρi ) |σj ) in place of ρi ⊗

A

?>
ρi
89

∀Dj ∈ Transf(B, A)

In formulas we will write |ρi )B (resp. (aj |A ). The sets
Transf(I, A) and Transf(A, I) will be denoted as St(A) and
Eff(A), respectively. The reason for this special notation
is that in the next subsection the elements of St(A) (resp.
Eff(A)) will be interpreted as the states (resp. effects) of
system A.
From every pair of systems A and B one can form a
composite system, denoted by AB. Clearly, composing
system A with nothing still gives system A, in formula
AI = IA = A. Two devices can be composed in parallel,
thus obtaining a new device with composite input and
composite output systems. The events in composite test
are represented as
Ci

A

?>
{ρ }
89 i i∈X

B

=<
{Bk }k∈Z
:;

and also to represent a particular outcome of the exper∀Ci ∈ Transf(A, B) iment

The subindex A will be dropped from IA where there is
no ambiguity.
The letter I will be reserved for the trivial system,
which simply means “nothing” [28]. A device with input (resp. output) system I is a device with no input
(resp. no output). The corresponding tests will be called
preparation-tests (resp. observation-tests). In this case
we replace the input (resp. output) wire with a round
portion:

'!&ρi B
resp. A aj -*+, .
(1)

A

B

C

and are written in formulas as Dj Ci .
For every system A one can perform the identity-test
(or simply, the identity), that is, a test {IA } with a single
outcome, with the property
A

Ci

Cj
C

B

=<
Bk
:;

In formula, the above circuit is given by
(Bk |BC (Cj ⊗ IC ) |ρi )AC .
B.

Probabilistic structure: states, effects and
transformations

On top of the language of circuits, we put a probabilistic structure [21]: we declare that the composition
of a preparation-test {ρi }i∈X with an observation-test
{aj }j∈Y gives rise to a joint probability distribution:
'!&ρi

A

P

aj -*+, = p(i, j),

(2)

P

with p(i, j) ≥ 0 and i∈X j∈Y p(i, j) = 1. In formula
we write p(i, j) = (aj | ρi ). Moreover, if two experiments
are run in parallel, we assume that the joint probability
distribution is given by the product:
'!&ρi

A

ak "%$#

(/.)σj

B

bl -*+,

= p(i, k)q(j, l)

(3)

where p(i, k) := (ak | ρi ) , q(j, l) := (bl | σj ).
The probabilistic structure defined by Eq. (2) turns
every event ρi ∈ St(A) into a function ρ̂i : Eff(A) → R,
given by ρ̂i (aj ) := (aj | ρi ). If two events ρi , ρ′i ∈ St(A)
induce the same function, then it is impossible to distinguish between them from the statistics of the experiments allowed by our theory. This means that for our

<!-- page 6 -->
6
purposes the two events are the same: accordingly, we
will take equivalence classes with respect to the relation
ρi ≃ ρ′i if ρ̂i = ρ̂′i . To avoid introducing new notation,
from now on we will assume that the equivalence classes
have been taken since the start. We will identify the event
ρi ∈ St(A) with the corresponding function ρ̂i and will
call it state. Accordingly, we will refer to preparationtests as collections of states {ρi }i∈X . Note that, since
one can take linear combinations of functions, the states
in St(A) generate a real vector space, denoted by StR (A).
The same construction holds for observation-tests: every event aj ∈ Eff(A) induces a function âj : St(A) → R,
given by âj (ρi ) := (aj | ρi ). If two events aj , a′j ∈ Eff(A)
induce to the same function, then it is impossible to distinguish between them from the statistics of the experiments allowed in our theory. This means that for our
purposes the two events are the same: accordingly, we
will take equivalence classes with respect to the relation
aj ≃ a′j if âj = â′j . To avoid introducing new notation,
from now on we will identify the event aj ∈ Eff(A) with
the corresponding function âj and we will call it effect.
Accordingly, we will refer to observation-tests as collection of effects {aj }i∈Y . The effects in Eff(A) generate a
real vector space, denoted by Eff R (A).
A vector in StR (A) (resp. Eff R (A)) can be extended
to a linear function on Eff R (A) (resp. StR (A)). In this
way, states and effects can be thought as elements of two
real vector spaces, one dual to the other. In this paper
we will restrict our attention to finite dimensional vector
spaces: operationally, this means that the state of a given
physical system is completely determined by the statistics of a finite number of finite-outcome measurements.
The dimension of the vector space StR (A), which by construction is equal to the dimension of its dual Eff R (A),
will be denoted by DA . We will refer to DA as the size
of system A.
Finally, the vector spaces StR (A) and Eff R (A) can be
equipped with suitable norms, which have an operational
meaning related to optimal discrimination schemes [21].
The norm of an element δ ∈ StR (A) is given by [21]
||δ|| =

sup
a0 ∈Eff(A)

(a0 | δ) −

inf

a1 ∈Eff(A)

(a1 | δ) ,

while the norm of an element ξ ∈ Eff R (A) is given by
||ξ|| = sup | (ξ| ρ) |.
ρ∈St(A)

We will always take the set of states St(A) to be closed
in the operational norm. The convenience of this choice is
the convenience of using real numbers instead of rational
ones: dealing with a single real number is much easier
than dealing with a Cauchy sequence of rational numbers.
Operationally, taking St(A) to be closed is very natural:
the fact that there is a sequence of states {ρn }∞
n=1 that
converges to ρ ∈ StR (A) means that there is a procedure
to prepare ρ with arbitrary precision and hence that ρ
deserves the name of “state”.

We conclude this Subsection by noting that every event
Ck from A to B induces a linear map Cˆk from StR (A) to
StR (B), uniquely defined by
Cˆk : |ρ) ∈ St(A) 7→ Ck |ρ) ∈ St(B).
Likewise, for every system C the event Ck ⊗IC induces
a linear map Ck\
⊗ IC from StR (AC) to StR (BC). If two
events Ck and Ck′ induce the same maps for every possible system C, then there is no experiment in the theory
that is able to distinguish between them. This means
that for our purposes the two events are the same: accordingly, we will take equivalence classes with respect
to the relation Ck ≃ Ck′ if Ck\
⊗ IC = Ck′\
⊗ IC for every
system C. In this case, we will say that two events represent the same transformation. Accordingly, we will refer
to tests {Ci }i∈X as collections of transformations. The
deterministic transformations (corresponding to singleoutcome tests) will be called channels.
C.

Basic definitions in the operational-probabilistic
framework

Here we summarize few elementary definitions that will
be used later in the paper. The meaning of the definitions
in the case of quantum theory is also discussed.
1.

Coarse-graining, refinement, atomic transformations,
pure, mixed and completely mixed states

First, we start from the notions of coarse-graining and
refinement. Coarse-graining arises when we join together
some outcomes of a test: we say that the test {Dj }j∈Y is
a coarse-graining of the test {Ci }i∈X if there is a disjoint
partition {Xj }j∈Y of X such that
X
Dj =
Ci .
i∈Xj

Conversely, if {Dj }j∈Y is a coarse-graining of {Ci }i∈X ,
we say that {Ci }i∈X is a refinement of {Dj }j∈Y . Intuitively, a test that refines another is a test that extracts
information in a more precise way: it is a test with better
“resolving power”.
The notion of refinement also applies to a single transformation: a refinement of the transformation C is given
by a test {Ci }i∈X and a subset X0 such that
X
C =
Ci .
i∈X0

Accordingly, we say that each transformation Ci , i ∈ X0
is a refinement of C . A transformation C is atomic if it
has only trivial refinements: if Ci refines C , then Ci = pC
for some probability p ≥ 0. A test that consists of atomic
transformations is a test whose “resolving power” cannot
be further improved.

<!-- page 7 -->
7
When discussing states (i.e. transformations with trivial input) we will use the word pure as a synonym of
atomic. A pure state describes a situation of maximal
knowledge about the system’s preparation, a knowledge
that cannot be further refined.
As usual, a state that is not pure will be called mixed.
An important notion is that of completely mixed state:
Definition 1 (Completely mixed state) A state is
completely mixed if any other state can refine it: precisely, ω ∈ St(A) is completely mixed if for every ρ ∈
St(A) there is a non-zero probability p > 0 such that pρ
is a refinement of ω.
Intuitively, a completely mixed state describes a situation
of complete ignorance about the system’s preparation: if
a system is described by a completely mixed state, then it
means that we know so little about its preparation that,
in fact, every preparation is possible.
We conclude this paragraph with a couple of definitions
that will be used throughout the paper:
Definition 2 (Reversible transformation) A transformation U ∈ Transf(A, B) is reversible if there exists
another transformation U −1 ∈ Transf(B, A) such that
U −1 U = IA and U U −1 = IB . When A = B the reversible transformations form a group, indicated as GA .
Definition 3 (Operationally equivalent systems)
Two systems A and B are operationally equivalent if
there exists a reversible transformation U from A to B.
When two systems are operationally equivalent one can
convert one into the other in a reversible fashion.
2.

Examples in in quantum theory

Consider a quantum system with Hilbert space H =
Cd , d < ∞. In this case a preparation-test is a collection
of unnormalized density matrices {ρi }i∈X (i.e. of nonnegative d × d complex matrices with trace bounded by
1) such that
X
Tr[ρi ] = 1.
i∈X

Preparation-tests are often called quantum information
sources in quantum information theory. A generic state
ρ is an unnormalized density matrix. A deterministic
state, corresponding to a single-outcome preparation-test
is a normalized density
Pmatrix ρ, with Tr[ρ] = 1.
Diagonalizing ρ = i αi |ψi ihψi | we then obtain that
each matrix αi |ψi ihψi | is a refinement of ρ. More generally, every matrix σ such that σ ≤ ρ is a refinement
of ρ. Up to a positive rescaling, all matrices with support contained in the support of ρ are refinements of ρ.
A quantum state ρ is atomic (pure) if and only if it is
proportional to a rank-one projection. A quantum state
is completely mixed if and only if its density matrix has

full rank. Note that the quantum state χ = Idd , where
Id is the identity d × d matrix, is a particular example of
completely mixed state, but not the only example. Precisely, χ = Idd is the unique unitarily invariant state in
dimension d.
Let us now consider the case of observation-tests: in
quantum theory an observation-test is given by a POVM
(positive operator-valued measure), namely by a collection {Pj }j∈Y of non-negative d × d matrices such that
X
Pj = Id .
j∈Y

An effect is then a non-negative matrix P ≥ 0 upper
bounded by the identity. In quantum theory there is
only one deterministic effect, corresponding to a singleoutcome observation test: the unique deterministic effect
given by the identity matrix. As we will see in the following section, the fact that the deterministic effect is
unique is equivalent to the fact that quantum theory is a
causal theory.
An effect P is atomic if and only if P is proportional
to a rank-one projector. An observation-test is atomic if
it is a POVM with rank-one elements.
Finally, a general test from an input system with
Hilbert space H1 = Cd1 to an output system with Hilbert
space H2 = Cd2 is given by a quantum instrument,
namely by a collection {Ck }k∈Z of completely positive
trace non-increasing maps sending linear operators on
H1 to linear operators on H2 , with the property that
X
CZ :=
Ck
k∈Z

is trace-preserving. A general transformation is then
given by a trace non-increasing map, called quantum operation, whereas a deterministic transformation, corresponding to a single-outcome test, is given by a tracepreserving map, called quantum channel.
Any quantum operation C can be written in the Kraus
P
form C (ρ) = i Ci ρCi† , where Ci : H1 → H2 are the
Kraus operators. Up to a positive scaling, every quantum operation D such that the Kraus operators of D
belong to the linear span of the Kraus operators of C
is a refinement of C . A map C is atomic if and only if
there is only one Kraus operator in its Kraus form. A
reversible transformation in quantum theory is a unitary
map U (ρ) = U ρU † , where U : H1 → H2 is a unitary
operator, that is U † U = I1 and U U † = I2 where I1
(I2 ) is the identity operator on H1 (H2 ). Two quantum
systems are operationally equivalent if and only if the
corresponding Hilbert spaces have the same dimension.
D.

Operational principles

We are now in position to make precise the usage of
the expression “operational principle” in the context of
this paper. By “operational principle” we mean here a

<!-- page 8 -->
8
principle that can be stated using only the operationalprobablistic language, i.e. using only
• the notions of system, test, outcome, probability,
state, effect, transformation
• their specifications: atomic, pure, mixed, completely mixed
• more complex notions constructed from the above
terms (e.g. the notion of “reversible transformation”).
The distinction between operational principles and
principles referring to abstract mathematical properties,
mentioned in the introduction, should now be clear: for
example, a statement like “the pure states of a system
cannot be cloned” is a valid operational principle, because it can be analyzed in basic operational-probabilistic
terms as “for every system A there exists no transformation C with input system A and output system AA such
that C |ϕ) = |ϕ) |ϕ) for every pure state ϕ of A ”. On
the contrary, a statement like “the state space of a system with two perfectly distinguishable states is a threedimensional sphere” is not a valid operational principle,
because there is no way to express what it means for a
state space to be a three-dimensional sphere in terms of
basic operational notions. The fact that a state spate
is a sphere may be eventually derived from operational
principles, but cannot be assumed as a starting point.
III.

THE PRINCIPLES

We now state the principles used in our derivation.
The first five principles express generic features that are
shared by both classical and quantum theory. They could
be even included in the definition of the background
framework: they define the simple model of information
processing in which we try to single out quantum theory.
For this reason we will call them axioms. The sixth principle in our derivation has a different status: it expresses
the genuinely quantum features. A major message of our
work is that, within a broad class of theories of information processing, quantum theory is completely described
by the purification principle. To emphasize the special
role of the sixth principle we will call it postulate, in analogy with the parallel postulate of Euclidean geometry.
A.

Axioms

1.

Causality

The first axiom of our list, causality [21], is so basic that could be considered as part of the background
framework. We decided to explicitly present it as an axiom for two reasons: The first reason is that the framework of operational-probabilistic theories can be developed even without this requirement (see Ref.[21] for the

general framework and Refs. [31, 32] for two explicit examples of non-causal theories). The second reason is that
we want to stress that causality is an essential ingredient in our derivation. This observation is important in
view of possible extensions of quantum theory to quantum gravity scenarios where the causal structure is not
defined from the start (see e.g. Hardy in Ref. [33]).
Axiom 1 (Causality) The probability of preparations
is independent of the choice of observations.
In technical terms: if {ρi }i∈X ⊂ St(A) is a preparationtest, then the conditional probability of the preparation
ρi given the choice of the observation-test {aj }j∈Y is the
marginal
p (i|{aj }) :=

X

j∈Y

(aj | ρi )

The axiom states that the marginal probability p (i|{aj })
is independent of the choice of the observation-test {aj }:
if {aj }j∈Y and {bk }k∈Z are two different observationtests, then one has p(i|{aj }) = p(i|{bk }). Loosely speaking, one may refer to causality as a requirement of nosignalling from the future: indeed, causality is equivalent
to the fact that the probability of an outcome at a certain time does not depend on the choice of operations
that will be done at later times [20].
An operational-probabilistic theory that satisfies the
causality axiom 1 will be called causal. As we already
mentioned, causality is a very basic requirement and
could be considered as part of the framework: it provides
the notions used to state the other axioms and it implies
several facts that will be used frequently in the paper. In
fact, in our derivation we do not use the causality axiom
directly, but only through its consequences. In the following we briefly summarize the facts and the notations
that characterize the framework of causal operationalprobabilistic theories, introduced and discussed in detail
in Ref. [21]. Similar structures have been subsequently
considered in Refs. [34, 35] within a formal description
of circuits in foliable spacetime regions.
First, causality is equivalent
to the existence of an efP
fect eA such that eA = j∈X aj for every observation-test
{aj }j∈Y . We call the effect eA the deterministic effect
for system A. By definition, the effect eA is unique. The
subindex A in eA will be dropped when no confusion can
arise.
In a causal theory every test {Ci }i∈X ⊂ Transf(A, B)
satisfies the condition
X
(eB | Ci = (eA | .
i∈X

As a consequence, a transformation C ∈ Transf(A, B)
satisfies the condition
(eB | C ≤ (eA | ,

(4)

<!-- page 9 -->
9
with the equality if and only if C is a channel (i.e. a
deterministic transformation, corresponding to a singleoutcome test). In Eq. (4) we used the notation (a| ≤ (a′ |
to mean (a| ρ) ≤ (a′ | ρ) for every ρ ∈ St(A).
In a causal theory the norm of a state ρi ∈ St(A) is
given by ||ρi || = (e| ρi ). Accordingly, one can define the
normalized state
ρi
ρ̄i :=
.
(e| ρi )
In a causal theory one can always allow for rescaled
preparations: conditionally to the outcome i ∈ X in the
preparation-test {ρi }i∈X we can say that we prepared
the normalized state ρ̄i . For this reason, every state in a
causal theory is proportional to a normalized state.
The set of normalized states will be denoted by St1 (A).
Since the set of all states St(A) is closed in the operational
norm, also the set of normalized states St1 (A) is closed.
Moreover, the set St1 (A) is convex [21]: this means that
for every pair of normalized states ρ1 , ρ2 ∈ St1 (A) and
for every probability p ∈ [0, 1] the convex combination
ρp = pρ1 + (1 − p)ρ2 is a normalized state. Operationally,
the state ρp is obtained by
1. performing a binary test with outcomes {1, 2} and
outcome probabilities p1 = p and p2 = 1 − p
2. for outcome i preparing ρi , thus realizing the
preparation-test {pi ρi }i=1,2
3. coarse-graining over the outcomes, thus obtaining
ρp = pρ1 + (1 − p)ρ2 .

The step 2 (preparation of a state conditionally on the
outcome of a previous test) is possible because the theory
is causal [21].
The pure normalized states are the extreme points of
the convex set St1 (A). For a normalized state ρ ∈ St1 (A)
we define the face identified by ρ as follows:
Definition 4 (Face identified by a state) The face
identified by ρ ∈ St1 (A) is the set Fρ of all normalized
states σ ∈ St1 (A) such that ρ = pσ + (1 − p)τ , for some
non-zero probability p > 0 and some normalized state
τ ∈ St1 (A).

In other words, Fρ is the set of all normalized states that
show up in the convex decompositions of ρ. Clearly, if
ϕ is a pure state, then one has Fϕ = {ϕ}. The opposite
situation is that of completely mixed states: by definition
1, a state ω ∈ St1 (A) is completely mixed if every state
σ ∈ St1 (A) can stay in its convex decomposition, that is,
if Fω = St1 (A). An equivalent condition for a state to be
completely mixed is the following:
Lemma 1 A state ω ∈ St1 (A) is completely mixed if and
only if Span(Fω ) = StR (A).

Proof. The condition is clearly necessary. It is also
sufficient because for a state σ ∈ St1 (A) the relation σ ∈
Span(Fω ) implies σ ∈ Fω (see Lemma 16 of Ref.[21]). 
A completely mixed state can never be distinguished
from another state with zero error probability:

Proposition 1 Let ρ ∈ St1 (A) be a completely mixed
state and σ ∈ St1 (A) be an arbitrary state. Then, the
probability of error in distinguishing ρ from σ is strictly
greater than zero.
Proof. By contradiction, suppose that one can distinguish between ρ and σ with zero error probability.
This means that there exists a binary test {aρ , aσ } such
that (aρ | σ) = (aσ | ρ) = 0. Since ρ is completely mixed
there exists a probability p > 0 and a state τ ∈ St1 (A)
such that ρ = pσ + (1 − p)τ . Hence, the condition
(aσ | ρ) = 0 implies (aσ | σ) = 0. Therefore, we have
(aρ | σ) + (aσ | σ) = 0. This is in contradiction with the
normalization of the probabilities in the test {aρ , aσ },
which would require (aρ | σ) + (aσ | σ) = 1. 

2.

Perfect distinguishability

Our second axiom regards the task of state discrimination. As we saw in proposition 1, if a state is completely
mixed, then it is impossible to distinguish it perfectly
from any other state. Axiom 2 states the converse:
Axiom 2 (Perfect distinguishability) Every state
that is not completely mixed can be perfectly distinguished
from some other state.
Note that the statement of axiom 2 holds for quantum
and for classical information theory. In quantum theory a
completely mixed state is a density matrix with full rank.
If a density matrix ρ has not full rank, then it must have
a kernel: hence, every density matrix σ with support in
the kernel of ρ will be perfectly distinguishable from ρ,
as stated in Axiom 2. Applying the same reasoning for
density matrices that are diagonal in a given basis, one
can easily see that Axiom 2 is satisfied also by classical
information theory.
To the best of our knowledge, the perfect distinguishability property is has never been considered in the literature as an axiom, probably because in most works it
came for free as a consequence of stronger mathematical assumptions. For example, one can obtain the perfect distinguishability property from the no-restriction
hypothesis of Ref. [21], stating that for every system
A any binary probability rule (i.e. any pair of positive
functionals a0 , a1 ∈ Eff R (A) such that a0 + a1 = eA ) actually describes a measurement allowed by the theory.
This assumption was made e.g. in Ref. [18] in the case
of systems with at most two distinguishable states (see
requirement 5 of Ref. [18]). Note that the difference
between the perfect distinguishability Axiom and the norestriction hypothesis is that the former can be expressed
in purely operational terms, whereas the latter requires
the notion of “positive functional” which is not part of
the basic operational language.

<!-- page 10 -->
10
3.

Ideal compression

The third axiom is about information compression. An
information source for system A is a preparation-test
{ρi }i∈X
P , where each ρi ∈ St(A) is an unnormalized state
and
i∈X (e| ρi ) = 1. A compression scheme is given
by an encoding operation E from A to a smaller system
C, that is, to a system C such that DC ≤ DA . The
compression scheme is lossless for the source {ρi }i∈X if
there exists a decoding operation D from C to A such
that DE |ρi ) = |ρi ) for every value of the index i ∈ X.
This means that the decoding allows one to perfectly retrieve the states {ρi }i∈X . We say that a compression
scheme is lossless for the statePρ, if it is lossless for every
source {ρi }i∈X such that ρ = i∈X ρi . Equivalently, this
means that the restriction of DE to the face identified by
ρ is equal to the identity channel: DE |σ) = σ for every
σ ∈ Fρ .
A lossless compression scheme is maximally efficient
if the encoding system C has the smallest possible size,
that is, if the system C has no more states than exactly
those needed to compress ρ. This happens when every
normalized state τ ∈ St1 (C) comes from the encoding of
some normalized state σ ∈ Fρ , namely |τ ) = E |σ).
We say that a compression scheme that is lossless and
maximally efficient is ideal. Our second axiom states that
ideal compression is always possible:
Axiom 3 (Ideal compression) For every state there
exists an ideal compression scheme.
It is easy to see that this statement holds in quantum
theory and in classical probability theory. For example,
if ρ is a density matrix on a d-dimensional Hilbert space
and rank(ρ) = r, then the ideal compression is obtained
by just encoding ρ in an r-dimensional Hilbert space. As
long as we do not tolerate losses, this is the most efficient
one-shot compression we can devise in quantum theory.
Similar observations hold for classical information theory.
4.

St1 (AB) using only local operations and classical communication and achieving an error probability strictly
larger than pran = 1/2, the probability of error in random guess [21]. Again, this statement holds in ordinary
quantum theory (on complex Hilbert spaces) and in classical information theory.
Another equivalent condition to local distinguishability is the local tomography axiom, introduced in Refs.
[19, 36]. The local tomography axiom state that every
bipartite state can be reconstructed from the statistics
of local measurements on the component systems. Technically, local tomography is in turn equivalent to the relation DAB = DA DB [16] and to the fact that every state
ρ ∈ St(AB) can be written as
ρ=

DA X
DB
X
i=1 j=1

ρij αi ⊗ βj ,

DB
A
where {αi }D
i=1 ({βj }j=1 ) is a basis for the vector space
StR (A) (StR (B)). The analog condition also holds for
effects: every bipartite effect E ∈ Eff(AB) ben be written
as

E=

DB
DA X
X
i=1 j=1

Eij ai ⊗ bj ,

DB
A
where {ai }D
i=1 ({bj }j=1 ) is a basis for the vector space
Eff R (A) (Eff R (B)).
An important consequence of local distinguishability,
observed in Ref. [21], is that a transformation C ∈
Transf(AB) is completely specified by its action on St(A):
thanks to local distinguishability we have the implication

C |ρ) = C ′ |ρ)

∀ρ ∈ St(A) =⇒ C = C ′ .

(5)

(see Lemma 14 of Ref.[21] for the proof). Note that Eq.
(5) does not hold for quantum theory on real Hilbert
spaces [21].

Local distinguishability
5.

The fourth axiom consists in the assumption of local
distinguishability, here presented in the formulation of
Ref. [21].
Axiom 4 (Local distinguishability) If two bipartite
states are different, then they give different probabilities
for at least one product experiment.
In more technical terms: if ρ, σ ∈ St1 (AB) are states
and ρ 6= σ, then there are two effects a ∈ Eff(A) and
b ∈ Eff(B) such that
?> A a
?> A a
ρ
6= 89σ
89 B
B
b"%$#
b"%$#
Local distinguishability is equivalent to the fact that
two distant parties, holding systems A and B, respectively, can distinguish between the two states ρ, σ ∈

Pure conditioning

The fourth axiom states how the outcomes of a measurement on one side of a pure bipartite state can induce pure states on the other side. In this case we consider atomic measurements, that is, measurements described by observation-tests {ai }i∈X where each effect
ai is atomic. Intuitively, atomic measurement are those
with maximum “resolving power”.
Axiom 5 (Pure conditioning) If a bipartite system is
in a pure state, then each outcome of an atomic measurement on one side induces a pure state on the other.
The pure conditioning property holds in quantum theory and in classical information theory as well. In fact,
the statement is trivial in classical information theory,
because the only pure bipartite states are the product of

<!-- page 11 -->
11
pure states: no matter which measurement is performed
on one side, the remaining state on the other side will
necessarily be pure.
The pure conditioning property, as formulated above,
has been recently introduced in Ref. [37]. A stronger
version of axiom 5 is the atomicity of composition introduced in Ref. [20]:
5’ Atomicity of composition: the sequential composition of two atomic operations is atomic.
Since pure states and atomic effects are a particular case
of atomic transformations, Axiom 5’ implies Axiom 5.
In our derivation, however, also the converse implication
holds: indeed, thanks to the purification postulate we
will be able to show that Axiom 5 implies Axiom 5’ (see
lemma 16).

B.

The purification postulate

The last postulate in our list is the purification postulate, which was introduced and explored in detail in Ref.
[21]. While the previous axioms were also satisfied by
classical probability theory, the purification axiom introduces in our derivation the genuinely quantum features.
A purification of the state ρ ∈ St1 (A) is a pure state Ψρ
of some composite system AB, with the property that ρ
is the marginal of Ψρ , that is,
'!&ρ

A

?>
= 89Ψρ

A
B

eB "%$#

Here we refer to the system B as the purifying system.
The purification axiom states that every state can be
obtained as the marginal of a pure bipartite state in an
essentially unique way:
Postulate 1 (Purification) Every state has a purification. For fixed purifying system, every two purifications
of the same state are connected by a reversible transformation on the purifying system.
Informally speaking, our postulate states that the ignorance about a part is always compatible with a maximal
knowledge of the whole. The existence of pure bipartite
states with mixed marginal was already recognized by
Schrödinger as the characteristic trait of quantum theory
[23]. Here, however, we also emphasize the importance
of the uniqueness of purification up to reversible transformations: this property sets up a relation between pure
states and reversible transformations that generates most
of the structure of quantum theory. As shown in Ref.
[21], an impressive number of quantum features are actually direct consequences of purification. In particular,
purification implies the possibility of simulating any irreversible process through a reversible interaction of the
system with an environment that is finally discarded.

IV.

A.

FIRST CONSEQUENCES OF THE
PRINCIPLES
Results about ideal compression

Let ρ ∈ St1 (A) be a state and let E ∈ Transf(A, C)
(resp. D ∈ Transf(C, A)) be its encoding (resp. decoding) in the ideal compression scheme of Axiom 3.
Essentially, the encoding operation E ∈ Transf(A, C)
identifies the face Fρ with the state space St1 (C). In the
following we provide a list of elementary lemmas showing that all statements about Fρ can be translated into
statements about St1 (C) and vice-versa.
Lemma 2 The composition of decoding and encoding is
the identity on C, namely E D = IC .
Proof. Since the compression is maximally efficient, for
every state τ ∈ St1 (C) there is a state σ ∈ Fρ such that
E σ = τ . Using the fact that DE σ = σ (the compression
is lossless) we then obtain E Dτ = E DE σ = E σ = τ . By
local distinguishability [see Eq. (5)], this implies E D =
IC . 
Lemma 3 The image of St1 (C) under the decoding operation D is Fρ .
Proof. Since the compression is maximally efficient, for
all τ ∈ St1 (C) there exists σ ∈ Fρ such that τ = E σ.
Then, Dτ = DE σ = σ. This implies that D(St1 (C)) ⊆
Fρ . On the other hand, since the compression is lossless,
for every state σ ∈ Fρ one has DE σ = σ. This implies
the inclusion Fρ ⊆ D(St1 (C)). 
Lemma 4 If the state ϕ ∈ Fρ is pure, then the state
E ϕ ∈ St1 (C) is pure. If the state ψ ∈ St1 (C) is pure,
then the state Dψ ∈ Fρ is pure.
Proof. Suppose that ϕ ∈ Fρ is pure and that E ϕ can
be written as E ϕ = pσ + (1 − p)τ for some p > 0 and
some σ, τ ∈ St1 (C). Applying D on both sides we obtain
ϕ = pDσ + (1 − p)Dτ . Since ϕ is pure we must have
Dσ = Dτ = ϕ. Now, applying E on all terms of the
equality and using lemma 2 we obtain σ = τ = E ϕ.
This proves that E ϕ is pure. Conversely, suppose that
ψ ∈ St1 (C) is pure and Dψ = pσ + (1 − p)τ for some
p > 0 and some σ, τ ∈ St1 (A). Since Dψ is in the face Fρ
(lemma 3), also σ and τ are in the same face. Applying
E on both sides of the equality Dψ = pσ + (1 − p)τ and
using lemma 2 we obtain ψ = E Dψ = pE σ + (1 − p)E τ .
Since ψ is pure we must have E σ = E τ = ψ. Applying
D on all terms of the equality we then have σ = τ = Dψ,
thus proving that Dψ is pure. 
We say that a state σ ∈ Fρ is completely mixed relative
to the face Fρ if every state τ ∈ Fρ can stay in the convex decomposition of σ. In other words, σ is completely
mixed relative to Fρ if one has Fσ = Fρ . Note that in
general σ ∈ Fρ implies Fσ ⊆ Fρ .
We then have the following:

<!-- page 12 -->
12
Lemma 5 If the state ω ∈ Fρ is completely mixed relative to Fρ , then the state E ω ∈ St1 (C) is completely
mixed. If the state υ ∈ St1 (C) is completely mixed, then
the state Dυ ∈ Fρ is completely mixed relative to Fρ .
Proof. Suppose that ω is completely mixed relative to
Fρ . Then every state σ ∈ Fρ can stay in its convex
decomposition, say ω = pσ + (1 − p)σ ′ with p > 0 and
σ ′ ∈ Fρ . Applying E we have
E ω = pE σ + (1 − p)E σ ′ .

(6)

Since the compression is maximally efficient, for every
state τ ∈ St1 (C) there exists a state σ ∈ Fρ such that
τ = E σ. Choosing the suitable σ ∈ Fρ and substituting
τ to E σ in Eq. (6) we then obtain that for every state
τ ∈ St1 (C) there exists probability p > 0 and a state
σ ′ ∈ Fρ such that
E ω = pτ + (1 − p)E σ ′ .

This implies that E ω is completely mixed. Suppose now
that υ ∈ St1 (C) is completely mixed. Then every state
τ ∈ St1 (C) can stay in its convex decomposition, say
υ = pτ + (1 − p)τ ′ . with p > 0 and τ ′ ∈ St1 (C). Applying
D on both sides we have
Dυ = pDτ + (1 − p)Dτ ′ .

(7)

Now, using lemma 3 we have that every state σ ∈ Fρ can
be written as σ = Dτ for some τ ∈ St1 (C). Choosing the
suitable τ ∈ St1 (C) and substituting σ to Dτ in Eq. (7)
we then obtain that for evert state σ ∈ Fρ there exists
a probability p > 0 and a state τ ′ ∈ St1 (C) such that
Dυ = pσ + (1 − p)Dτ ′ . Therefore, Dυ is completely
mixed relative to Fρ . 
We now show that the system C used for ideal compression of the state ρ is unique up to operational equivalence:
Lemma 6 If two systems C and C′ allow for ideal compression of a state ρ ∈ St1 (A), then C and C′ are operationally equivalent.
Proof.
Let E , D and E ′ , D ′ denote the encoding/decoding schemes for systems C and C′ , respectively.
Define the transformations U := E ′ D ∈ Transf(C, C′ )
and V = E D ′ ∈ Transf(C′ , C). It is easy to see that U
is reversible and U −1 = V . Indeed, since the restriction of D ′ E ′ and DE to the face Fρ is the identity, using
Lemma 3 one has D ′ E ′ D = D and similarly DE D ′ = D ′ .
Hence, we have U V = E ′ DE D ′ = E ′ D ′ = IC′ and
V U = E D ′ E ′ D = E D = IC . 
It is useful to introduce the notion of equality upon
input of ρ. We say that two transformations A , A ′ ∈
Transf(A, B) are equal upon input of ρ ∈ St(A) if their
restrictions to the face identified by ρ are equal, that is,
if A σ = A ′ σ for every σ ∈ Fρ . If A and A ′ are equal
upon input of ρ we write A =ρ A ′ .
Using the notion of equality upon input of ρ we can
rephrase the fact that the compression is lossless for ρ as
DE =ρ IA . Similarly, we can state the following:

Lemma 7 The encoding E is deterministic upon input
of ρ, that is (eC | E =ρ (eA |.
Proof.
For every σ ∈ Fρ we have (eC | E |σ) ≥
(eA | DE |σ) = (eA | σ) = 1, having used Eq. (4) and the
fact that the compression is lossless. Since probabilities
are bounded by 1, this implies (eC | E |σ) = (eA | σ) for
every σ ∈ Fρ , that is, (eC | E =ρ (eA |. 
A similar result holds for the decoding:
Lemma 8 The decoding D is deterministic, that is
(eA | D = (eC |.
Proof. For every τ ∈ St1 (A) we have (eA | D |τ ) ≥
(eC | E D |τ ) = (eC | τ ), having used Eq. (4) and lemma
2. Hence, (eA | D = (eC |. 
B.

Results about purification

The purification postulate 1 implies a large number of
quantum features, as it was shown in Ref. [21]. Here we
review only the facts that are useful for our derivation,
referring to Ref. [21] for the proofs.
An elementary consequence of the uniqueness of purification is that the group GA of reversible transformations
on A acts transitively on the set of pure states:
Lemma 9 (Transitivity on pure states) For every
couple of pure states ϕ, ϕ′ ∈ St1 (A) there is a reversible
transformation U ∈ GA such that ϕ′ = U ϕ.
Proof. See Lemma 20 of Ref. [21]. 
Transitivity implies that for every system A there is
a unique state χA ∈ St1 (A) that is invariant under reversible transformations, that is, a unique state such that
U χA = χA for every U ∈ GA :
Lemma 10 (Uniqueness of the invariant state)
For every system A, there is a unique state χA invariant under all reversible transformations in GA . The
invariant state has the following properties:
1. χA is completely mixed
2. χAB = χA ⊗ χB .
Proof. See Corollary 34 and Theorem 4 of Ref. [21].
The proof of item 2 uses the local distinguishability axiom. 
When there is no ambiguity we will drop the subindex
A and simply write χ.
The uniqueness of purification in postulate 1 requires
that if Ψρ , Ψ′ρ ∈ St1 (AB) are two purifications of ρ ∈
St1 (A), then there exists a reversible transformation
U ∈ GB such that Ψ′ρ = (IA ⊗ U )Ψρ . The following
lemma extends the uniqueness property to purifications
with different purifying systems:

<!-- page 13 -->
13
Lemma 11 (Uniqueness of the purification up to
channels on the purifying systems) Let Ψ ∈ St1 (AB)
and Ψ′ ∈ St1 (AC) be two purifications of ρ ∈ St1 (A).
Then there exists a channel C ∈ Transf(B, C) such that
?> ′
89Ψ

A
C

?>
= 89Ψ

A
B

C

C

Proof. See Lemma 21 of Ref. [21]. 
Another consequence of the uniqueness of purification
is the fact that any ensemble decomposition of a given
mixed state can be obtained by performing a measurement on the purifying system:
Lemma 12 (Purification of preparation-tests) Let
ρ ∈ St1 (A) be a state and Ψρ ∈ St1 (AB) be a purification
P
of ρ. If {ρi }i∈X be a preparation-test such that i∈X ρi =
ρ, then there exists an observation-test {ai }i∈X on the
purifying system such that
'!&ρi

A

?>
= 89Ψρ

A

bi -*+,

B

A

?>
89RC

B
C

?>
:= Ψ
89

A

C

B

C

B

1. it defines a bijective correspondence between tests
{Ci }i∈X from A to B and collections of states
{Ri }i∈X for BC satisfying
X
(e|B |Ri )BC = (e|A |Ψ)AC .
i∈X

A

2. the transformation C is atomic if and only if the
corresponding state RC is pure.

b-*+,

An important consequence of purification and local distinguishability is the relation between equality upon input of ρ and equality on the purifications of ρ:
Theorem 1 (Equality upon input of ρ vs equality
on purifications of ρ) Let Ψ ∈ St1 (AC) be a purification of ρ ∈ St1 (A), and let A , A ′ ∈ Transf(A, B) be two
transformations. Then one has
(A ⊗ IC )Ψρ = (A ′ ⊗ IC )Ψρ

Let us choose a fixed faithful state for system A, say
Ψ ∈ St1 (AC). Then for every transformation C ∈
Transf(A, B) we can define the Choi state RC ∈ St(BC)
as

Theorem 2 (Choi isomorphism) For a given faithful
state Ψ ∈ St1 (AC) the map C 7→ RC := (C ⊗ IC )Ψ has
the following properties:

Corollary 1 If Ψρ ∈ St1 (AB) is a purification of ρ ∈
St1 (A) and σ belongs to the face Fρ , then there exists an
effect b and a non-zero probability p > 0 such that
p σ

Corollary 3 If Ψ ∈ St1 (AC) is pure and its marginal
on system A is completely mixed, then Ψ is dynamically
faithful for system A.

We then have the following:

Proof. See lemma 8 of Ref. [21]. 
An easy consequence is the following:

?>
= 89Ψρ

Proof. By theorem 1 the first condition is equivalent
to A =ω A ′ . Since ω is completely mixed, this means
A σ = A ′ σ for every σ ∈ St1 (A). By local distinguishability [see Eq. (5)] this implies A = A ′ . 
Corollary 2 shows that the state (A ⊗ IC )Ψω characterizes the transformation A completely. We will express
this fact by saying that the state Ψω is dynamically faithful [20], or just faithful, for short. Using this notion we
can rephrase corollary 2 as:

⇐⇒

A =ρ A ′ .

Proof. See Theorem 17 of Ref. [21].
A simple consequence of the Choi isomorphism is the
following:
Corollary 4 Let {Ci }i∈X ⊂ Transf(A, B) be a collection
of transformations. Then, {Ci }i∈X is a test if and only
if
X
(e|B Ci = (e|A .
i∈X

Proof. See theorem 1 of Ref. [21]. The proof of the
direction ⇐= uses the local distinguishability axiom. 
As a consequence, the purification of a completely
mixed state allows for the tomography of transformations:

In particular, let {ai }i∈X ⊂ Eff(A) be a collection of effects. Then, {ai }i∈X is an observation-test if and only
if
X
(ai | = (e| .
(8)
i∈X

Corollary 2 Let ω ∈ St1 (A) be completely mixed and
Ψω ∈ St1 (AC) is a purification of ω. Then, for all transformations A , A ′ ∈ Transf(A, B) one has
(A ⊗ IC )Ψω = (A ′ ⊗ IC )Ψω

⇐⇒

A = A ′.

Proof. Apply item 1 of theorem 2 to the collection of
states {Ri }i∈X defined by Ri := (Ci ⊗ IC )Ψ. 
A much deeper consequence of the Choi isomorphism
is the following theorem:

<!-- page 14 -->
14
Theorem 3 (States specify the theory) Let Θ, Θ′ be
two theories satisfying the purification postulate. If Θ
and Θ′ have the same sets of normalized states, then Θ′ =
Θ.
Proof. See Theorem 19 of Ref.[21]. 
Thanks to theorem 3 to derive quantum theory we will
only need to prove that our principles imply that for every system A the normalized states St1 (A) can be described as positive Hermitian matrices with unit trace.
Once this is proved, theorem 3 automatically ensures that
all the dynamics and all the measurements allowed by the
theory are exactly the dynamics and the measurements
allowed in quantum theory.
Note that in the definition of the Choi state we left
the freedom to choose the faithful state Ψ ∈ St1 (AC).
Among many possibilities, one convenient choice is to
take a faithful state Φ ∈ St1 (AC) obtained as a purification of the invariant state χ ∈ St1 (A). Moreover, as we
will see in the next paragraph, we can always choose the
purifying system C in such a way that the marginal on
C is completely mixed.

C.

Results about the combination of compression
and purification

An important consequence of the combination of the
purification postulate with the compression axiom is the
fact that one can always choose a purification of ρ such
that the marginal state on the purifying system is completely mixed. To prove this result we need the following
lemma:
Lemma 13 Let ρ ∈ St1 (A) be a state and let Ψρ ∈
St1 (AB) be a purification of ρ. If E ∈ Transf(A, C) is
the encoding operation in the compression scheme of axiom 3, then the state Ψ′ρ := (E ⊗ IB )Ψρ is pure.
Proof. Let D ∈ Transf(C, A) be the decoding operation. Since the compression is lossless for ρ we know
that DE =ρ IA . By theorem 1 this is equivalent to
the condition (DE
P ⊗ IB )Ψρ = Ψρ . Now, suppose that
(E ⊗ IB )Ψρ = i∈X
PΓi . Applying D on both sides we
then obtain Ψρ =
i∈X (D ⊗ IB )Γi , and, since Ψρ is
pure, for every i ∈ X we must have (D ⊗ IB )Γi =
pi Ψρ , where pi ≥ 0 is some probability. Finally, since
E D = IC (lemma 2), one has Γi = pi (E ⊗ IB )Ψρ .
Hence, (E ⊗ IB )Ψρ admits only decompositions with
Γi = pi (E ⊗ IB )Ψρ , that is, (E ⊗ IB )Ψρ is pure. 
We are now in position to prove the desired result:
Theorem 4 For every state ρ ∈ St1 (A) there exists a
system C and a purification Ψρ ∈ St1 (AC) of ρ such
that the marginal state on system C is completely mixed.
Moreover, the system C is unique up to operational equivalence.

Proof. Take an arbitrary purification of ρ, say Φρ ∈
St1 (AB) for some purifying system B. Define the
marginal state on system B as |θ)B := (e|A |Φρ )AB and define the state Ψρ := (IA ⊗ E )Φρ , where E ∈ Transf(B, C)
the encoding operation for state θ. By Lemma 13 we
know that Ψρ ∈ St(AC) is pure. Using lemma 7 and theorem 1 we obtain (eC | |Ψρ ) = [(eC | E ] |Φρ ) = (eB | |Φρ ) =
|ρ), that is, Ψρ is a purification of ρ. Finally, the marginal
on system C is given by ρ̃ = E θ, which by Lemma
5 is completely mixed. This proves the first part of
the thesis. It remains to show that the system C is
uniquely defined up to operational equivalence. Suppose
that Ψ′ρ ∈ St(AC′ ) is another purification of ρ with the
property that the marginal on system C′ is completely
mixed. Since Ψρ and Ψ′ρ are two purifications of the
same state, there must be two channels C ∈ Transf(C, C′ )
and R ∈ Transf(C′ , C) such that Ψ′ρ = (IA ⊗ C )Ψρ and
Ψρ = (IA ⊗R)Ψ′ρ (lemma 11). Combining the two equalities one obtains Ψρ = (IA ⊗RC )Ψρ . Now, the marginal
of Ψρ on system C is completely mixed, and this implies
that Ψρ is faithful for system C (corollary 3). Hence, we
have RC = IC . Repeating the same argument for Ψ′ρ
we obtain C R = IC′ . Therefore, C is reversible and
R = C −1 . This proves that C and C′ are operationally
equivalent. 
The following facts will also be useful
Corollary 5 Let Ψρ ∈ St1 (AB) be a purification of ρ ∈
St1 (A) and let E ∈ Transf(A, C) be the encoding for ρ.
Then, the state (E ⊗ IB )Ψρ ∈ St1 (CB) is dynamically
faithful for C.
Proof. The marginal of (E ⊗ IB )Ψρ on system C is
E ρ, which is completely mixed by lemma 5. Hence, (E ⊗
IB )Ψρ is dynamically faithful by corollary 3. 
Lemma 14 The decoding transformation D
∈
Transf(C, A) in the ideal compression for ρ ∈ St1 (A) is
atomic.
Proof. Let Ψρ ∈ St1 (AB) be a purification of ρ, for some
purifying system B. Since DE =ρ IA (the compression
is lossless), we have (DE ⊗ IB )|Ψρ ) = |Ψρ ) (theorem
1). Now, by corollary 5 (E ⊗ IB )|Ψρ ) is faithful for C
and by lemma 13 (E ⊗ IB )|Ψρ ) is pure. Using the Choi
isomorphism with the faithful state Ψ := (E ⊗ IB )Ψρ we
then obtain that D is atomic. 

D.

Teleportation and the link product

For every system A one can choose a completely mixed
state ωA and a purification Ψ(A) ∈ St(AÃ) such that the
marginal on system Ã is completely mixed (cf. theorem
4). Any such purification allows for a probabilistic teleportation scheme:

<!-- page 15 -->
15
Lemma 15 (Probabilistic teleportation) There exists an atomic effect E (A) ∈ Eff(ÃA) and a non-zero
probability pA such that
?>
89Ψ(A)

A
Ã

=< = pA
E (A):;

A

A

I

Proof. See Theorem 10 of Ref. [21]. 
The no-information without disturbance result implies
the following geometrical limitation

A

Corollary 7 For every system A the convex set of states
St1 (A) is not a segment.

and
Ã

?>
89Ψ(A)

=<
E (A):;

A

= pA

Ã

I

Ã

Ã

Proof. See Corollary 19 of Ref. [21]. 
Let us choose Ψ(A) to be the faithful state in the definition of the Choi isomorphism. Then the sequential
composition of transformation induces a composition of
Choi states in following way:
Corollary 6 (Link product) For two transformations
C ∈ Transf(A, B) and D ∈ Transf(B, C) the Choi state of
DC ∈ Transf(A, C) is given by the link product
?>
89RDC

C
Ã

=

Lemma 17 (No information without disturbance)
A test {Ci }i∈X ⊂ Transf(A) is non-disturbing upon input
of ρ if and only if there is a set of probabilities {pi }i∈X
such that Ci =ρ pi IA for every i ∈ X.

?>
89RD

1
pB ?>
89RC

C
B̃
B

=<
E (B):;

(9)

Ã

Proof. The proof is by contradiction. Suppose that for
some system A the set St1 (A) is a segment. The segment
has only two pure states, say ϕ1 and ϕ2 , and every other
state ρ ∈ St1 (A) is completely mixed. Then the distinguishability axiom 2 imposes that ϕ1 and ϕ2 are perfectly
distinguishable. Take the binary test {a1 , a2 } such that
(ai | ϕj ) = δij and define the “measure-and-prepare” test
{C1 , C2 } as Ci = |ϕi ) (ai |, i = 1, 2 (the possibility of
preparing a state depending on the outcome of a previous measurement is guaranteed by causality [21]). Since
every state ρ in the segment can be written as convex
combination of the two extreme points, we have that the
test {C1 , C2 } is non-disturbing: (C1 + C2 )ρ = ρ for every
ρ. This is in contradiction with lemma 17 because C1
and C2 are not proportional to the identity. 
We know that no information can be extracted without disturbance. In the following we will prove a result
in the converse direction: if a measurement extracts no
information, than it can be realized in a non-disturbing
fashion. To show this result we first need the following

Proof. See Corollary 22 of Ref. [21]. 
We conclude this paragraph with an important result
that follows from the combination of the link product
structure with the pure conditioning axiom:

Lemma 18 For every observation test {ai }i∈X ⊂ Eff(A)
with finite outcome set X there is a system C and a test
{Ai }i∈X ⊂ Transf(A, C) consisting of atomic transformations such that (ai | = (eC | Ai .

Lemma 16 (Atomicity of composition) The composition of two atomic transformations is atomic.

Proof. Let |Ψ)AB be a pure faithful state for system A
and let |Ri )B = (ai |A |Ψ)AB the Choi state of ai . Take a
purification of Ri , say |Ψi )BC for some purifying system
C [38]. Then, by the Choi isomorphism there is a test
{Ai }i∈X , with input A and output C, such that

Proof. Let C ∈ Transf(A, B) and D ∈ Transf(B, C) be
two atomic transformations. By the Choi isomorphism,
the (unnormalized) states RC and RD are pure. Since
the teleportation effect E (B) in Eq. (9) is atomic (lemma
15), the pure conditioning axiom 5 implies the state RDC
is pure. By the Choi isomorphism this means that DC
is atomic. 

E.

No information without disturbance

We say that a test {Ci }i∈X
P ⊂ Transf(A) is nondisturbing upon input of ρ if
i∈X Ci =ρ IA . If ρ is
completely mixed, we simply say that the test is nondisturbing.
A consequence of the purification postulate is the following “no-information without disturbance” result:

?>
89Ψi

C
B

=

?>
89Ψ

A

Ai

C

B

[see item 1 of theorem 2] Moreover, each transformation
Ai : A → C is atomic (item 2 of theorem 2). Applying
the deterministic effect (eC | on both sides we then obtain
|Ri )B = (eC | |Ψi )CA = (eC | Ai |Ψ)AB . By definition of
Ri , this implies (ai |A |Ψ)AB = (eC | Ai |Ψ)AB , and, since
Ψ is dynamically faithful, (ai |A = (eC | Ai . 
Theorem 5 Let ρ ∈ St1 (A) be a state, a ∈ Eff(A) be an
effect, and A ∈ Transf(A, B) be an atomic transformation such that (a|A = (e|B A . If (a| =ρ p (e| for some
p ≥ 0, then there exists a channel C ∈ Transf(B, A) such
that C A =ρ pIA .

<!-- page 16 -->
16
Proof. Consider a purification of ρ, say Ψρ ∈ St(AC),
and define the state Σ ∈ St1 (BC) by |Σ) := 1p (A ⊗
IC )|Ψρ ). By the atomicity of composition 16 the state
Σ is pure. Moreover, we have
1
(a|A |Ψρ )AB
p
= (eA ||Ψρ )AC ,

Proof.
By lemma 18 there exists a test {Ai } ⊂
Transf(A, B) such that each transformation Ai is atomic
and (e| Ai = (ai |. By theorem 5, for each Ai there is a
correction channel Ci such that Ci Ai =ρ pi IA . Defining
Di := Ci Ai we then obtain the thesis. 

(eB | |Σ)BC =

having used theorem 1 in the last equality. This implies
that Ψρ and Σ are different purifications of the same
mixed state on system C. Then, by lemma 11 there
exists a channel C ∈ Transf(B, A) such that |Ψρ ) =
(C ⊗ IC )|Σ) = p1 (C A ⊗ IC )|Ψρ ). By theorem 1, the
last equality implies C A =ρ pIA . 
We now make a simple observation that combined with
Theorem 5 will lead to some interesting consequences:
Lemma 19 If (a|ρ) = kak, then a =ρ kake. Similarly,
if (a|ρ) = 0, then a =ρ 0.
Proof. By definition, σ ∈ Fρ iff there exists p > 0 and
τ ∈ St1 (A) such that ρ = pσ + (1 − p)τ . If (a| ρ) = kak,
then we have kak = p (a| σ) + (1 − p) (a| τ ). Since (a| σ)
and (a| τ ) cannot be larger than kak, the only way to
have the equality is to have (a| σ) = (a| τ ) = kak. By
definition, this amounts to say a =ρ kake. Similarly, if
(a| ρ) = 0, one has 0 = p (a| σ) + (1 − p) (a| τ ), which is
satisfied only if (a| σ) = (a| τ ) = 0, that is, if a =ρ 0. 
As consequence, we have the following:
Corollary 8 Let ρ ∈ St1 (A) be a state, a ∈ Eff(A) be an
effect, and A ∈ Transf(A, B) be an atomic transformation such that (a|A = (e|B A . If (a|ρ) = 1, then A is
correctable upon input of ρ, that is, there exists a correction operation C ∈ Transf(B, A) such that C A =ρ IA .
Proof. If (a| ρ) = 1, then clearly kak = 1. Lemma 19
then implies (a| =ρ (e|. Applying theorem 5 we finally
obtain the thesis. 
Corollary 9 Let ρ ∈ St1 (A) be a state, a ∈ Eff(A) be an
effect such that (a|ρ) = 1. Then there exists a transformation C ∈ Transf(A) such that (a| = (e| C and
C =ρ I .
Proof. Straightforward consequence of lemma 18 and of
corollary 8. 
Finally, we say that an observation-test {ai }i∈X is noninformative upon input of ρ if we have (ai | =ρ pi (e| for
every i ∈ X. This means that the test {ai }i∈X is unable
to distinguish the states in the face Fρ . As a consequence
of theorem 5 we have the following “no disturbance without information” result:

V.

PERFECTLY DISTINGUISHABLE STATES

In this section we prove some basic facts about perfectly distinguishable states. Let us start from the definition:
Definition 5 (Perfectly distinguishable states)
The normalized states {ρi }N
i=1 ⊆ St1 (A) are perfectly
distinguishable if there exists an observation-test {ai }N
i=1
such that (aj |ρi ) = δij . The observation-test {ai }N
i=1 is
called perfectly distinguishing.
From the distinguishability axiom 2 it is clear that every nontrivial system has at least two perfectly distinguishable states:
Lemma 20 For every nontrivial system A there are at
least two perfectly distinguishable states.
Proof. Let ϕ be a pure state of A. Obviously, ϕ is
not completely mixed (unless the system A has only one
state, that is, unless A is trivial). Hence, by axiom 2 there
exists at least a state σ that is perfectly distinguishable
from ϕ. 
An equivalent condition for perfect distinguishability
is the following:
Lemma 21 The states {ρi }N
i=1 ⊂ St1 (A) are perfectly
distinguishable if and only if there exists an observationtest {ai }N
i=1 such that (ai |ρi ) = 1 for every i.
Proof. The condition (ai | ρi ) = 1, ∀i = 1, . . . , N
is clearly necessary. On the other hand, the condition
(ai | ρi ) = 1, ∀i = 1, . . . , N implies
(ai |ρi ) = 1 =

N
X
j=1

(aj |ρi ) = (ai |ρi ) +

X
i6=j

(aj |ρi ).

Since all probabilities are non-negative, we must have
(aj |ρi ) = 0 for i 6= j, and therefore, (aj |ρi ) = δij . 
A very general fact about state discrimination is expressed by the following:
Lemma 22 If ρ is perfectly distinguishable from σ and
ρ′ (resp. σ ′ ) belongs to the face identified by ρ (resp. σ),
then ρ′ is perfectly distinguishable from σ ′ .

Corollary 10 (No disturbance without information) Proof. Let {a, e − a} be the binary observation-test that
distinguishes perfectly between ρ and σ. By definition,
If the test {ai }i∈X is non-informative upon input of
a ∈ Eff(A) is such that (a|ρ) = 1 and (a|σ) = 0. Now, by
ρ then there is a test {Di }i∈X ⊂ Transf(A) that is
lemma 19, (a|ρ′ ) = 1 and (a|σ ′ ) = 0 for all ρ′ ∈ Fρ and
non-disturbing upon input of ρ and satisfies (e| Di = (ai |
σ ′ ∈ Fσ . 
for every i ∈ X.

<!-- page 17 -->
17
Thanks to purification and to the local distinguishability axiom 4, we are also in position to show a much
stronger result:
N +M
Lemma 23 Let {ρi }N
i=1 ⊂ Fρ and {ρj }j=N +1 ⊂ Fσ be
two sets of perfectly distinguishable states. If ρ is per+M
fectly distinguishable from σ, then the states {ρi }N
i=1
are perfectly distinguishable.

Proof. Let {a, eA − a} be the observation-test such that
(a| ρ) = 1 and (a|σ) = 0. Now, by corollary 9 there is
a transformation C ∈ Transf(A) such that (eA | C = (a|
and C =ρ IA . Similarly, there exists a transformation
C ′ ∈ Transf(A) such that (eA | C ′ = (eA | − (a| and C ′ =σ
IA . We can then define the following observation-test

(ai | C
i≤N
(ci | =
(bi | C ′
N +1≤i≤N +M
N +M
where {ai }N
i=1 (resp. {bj }j=N +1 ) is the observation-test
that perfectly distinguishes among the states {ρi }N
i=1
+M
(resp. {ρj }N
j=N +1 ). By corollary 4 [see in particular Eq.
+M
(8)], {ci }N
is indeed an observation-test: each ci is an
i=1
effect and one has the normalization
NX
+M
i=1

(ci | =

N
X
i=1

(ai | C +

NX
+M

i=N +1
= (eA | C + (eA | C ′

(bi | C ′

= (a| + (eA | − (a| = (eA | .

Moreover, since C =ρ IA and C ′ =σ IA , one has
(ci | ρi ) = 1 for every i = 1, . . . , M + N . By lemma 21,
+M
this implies that the states {ρi }N
are perfectly distini=1
guishable. 
Definition 6 A set of perfectly distinguishable states
{ρi }N
i=1 is maximal if there is no state ρN +1 ∈ St1 (A)
+1
such that the states {ρi }N
i=1 are perfectly distinguishable
Theorem 6 A set of perfectly distinguishable states
{ρ }N is maximal if and only if the state ω =
PiN i=1
i=1 ρi /N is completely mixed.
Proof. We first prove that if ω is completely mixed, then
the set {ρi }N
i=1 must be maximal. Indeed, if there existed
+1
a state ρN +1 such that {ρi }N
i=1 are perfectly distinguishable, then clearly ρN +1 would be distinguishable from ω.
This is absurd because by proposition 1 no state can be
perfectly distinguished from a completely mixed state.
Conversely, if {ρi }N
i=1 is maximal, then ω is completely
mixed. If it were not, by the distinguishability axiom 2, ω
would be perfectly distinguishable from some state ρN +1 .
+1
By lemma 23, this would imply that the states {ρi }N
i=1
are perfectly distinguishable, in contradiction with the
hypothesis that the set {ρi }N
i=1 is maximal. 

Lemma 24 Every set of perfectly distinguishable pure
states can be extended to a maximal set of perfectly distinguishable pure states.
Proof. Let {ϕi }N
i=1 be a non-maximal set of perfectly
distinguishable pure states. By definition, there exists
a state σ such that {ϕi }N
i=1 ∪ {σ} is perfectly distinguishable. Let ϕN +1 be a pure state in Fσ . By Lemma
+1
19, the states {ϕi }N
i=1 will be perfectly distinguishable.
Since the dimension of StR (A) is finite and distinguishable states are linearly independent, iterating this procedure one finally obtains a maximal set of pure states in
a finite number of steps. 
Corollary 11 Any pure state belongs to a maximal set
of perfectly distinguishable pure states.
We conclude this section with a few elementary facts
about how the ideal compression of axiom 3 preserves
the distinguishability properties. In the following we will
choose a state ρ ∈ St1 (A) and E ∈ Transf(A, C) (resp.
D ∈ Transf(C, A)) will be the encoding (resp. decoding)
in the ideal compression scheme for ρ.
Lemma 25 If the states {ρi }ki=1 ⊂ Fρ are perfectly
distinguishable, then the states {E ρi }ki=1 ⊂ St1 (C)
are perfectly distinguishable. Conversely, if the states
{σi }ki=1 ⊂ St1 (C) are perfectly distinguishable, then the
states {Dσi }ki=1 ⊂ Fρ are perfectly distinguishable.
Proof. Let {ai }ki=1 be the observation-test such that
(ai |ρi ) = 1 for every i = 1, . . . , k. Since the compression
is lossless, we have DE |ρi ) = |ρi ) and (ai |DE |ρi ) = 1.
Now, consider the test {ci }ki=1 defined by (ci | = (ai | D.
Clearly we have (ci | E |ρi ) = 1 for every i = 1, . . . , k.
By lemma 21 this means that the states {E ρi }ki=1 are
perfectly distinguishable. Similarly, let {bi }ki=1 the
observation-test that distinguishes the set {σi }ki=1 . Since
E D = IC (lemma 2), we can conclude by the same argument that the states {Dσi }ki=1 are perfectly distinguishable. 
We say that a set of perfectly distinguishable states
{ρi }ki=1 ⊂ Fρ is maximal in the face Fρ if there is no
state ρk+1 ∈ Fρ such that the states {ρi }k+1
i=1 are perfectly
distinguishable. We then have the following:
Corollary 12 If {ρi }ki=1 ⊂ Fρ is a maximal set of
perfectly distinguishable states in the face Fρ , then
{E ρi }ki=1 ∈ St1 (C) is a maximal set of perfectly distinguishable states. Conversely, if {σi }ki=1 St1 (C) is a maximal set of perfectly distinguishable states, then {Dσi }ki=1
is a maximal set of perfectly distinguishable states in the
face Fρ .
Proof. Distinguishability of the states {E ρi }ki=1 and
{Dσi }ki=1 is proved by lemma 25. Let us now prove maximality. By contradiction, suppose that the set {ρi }ki=1 is
maximal in the face Fρ while the set {σi }ki=1 , σi := E ρi

<!-- page 18 -->
18
is not maximal. This means that there exists a state
σk+1 ∈ St1 (C) such that the states {σi }k+1
i=1 are perfectly
distinguishable. By lemma 25 the states {Dσi }k+1
i=1 are
perfectly distinguishable. Since DE ρi = ρi for every
i = 1, . . . , k, this means that the states {ρi }ki=1 ∪{Dσk+1 }
are perfectly distinguishable, in contradiction with the
fact that {ρi }ki=1 is maximal. This proves that the
set {E ρi }ki=1 must be maximal. Conversely, if the set
{σi } ⊂ St1 (C) is maximal, using the same argument we
can prove that the set {Dσi }ki=1 must be maximal in Fρ .

VI.

DUALITY BETWEEN PURE STATES AND
ATOMIC EFFECTS

We now show the existence of a one-to-one correspondence between states and effects of any system A in the
theory. Let us start from a simple observation:
Lemma 26 If a is atomic and (a| ρ) = kak for ρ ∈
St1 (A), then ρ must be pure.
Proof. By lemma 19, the condition (a| ρ) = kak implies
a =ρ kak e. By theorem 1, the condition a =ρ kak e
implies
?>
89Ψρ

A
B

a

= kak

?>
89Ψρ

A

e

B

where Ψρ ∈ St1 (AB) is any purification of ρ. Since a
is atomic, the pure conditioning axiom 5 implies that
the marginal state |ρ̃)B = (e|A |Ψρ )AB is pure. Since
the marginal of Ψρ on system B is pure, Ψρ must be
factorized, i.e. Ψρ = ρ ⊗ ρ̃ (see lemma 19 of Ref. 1).
Hence, ρ must be pure, otherwise we would have a nontrivial convex decomposition of the pure state Ψρ . 
We are now in position to show that every atomic effect
is associated to a unique pure state.
Theorem 7 For every atomic effect a ∈ Eff(A), there
exists a unique pure state ϕ ∈ St1 (A) such that (a| ϕ) =
kak.
Proof. Let ρ be a state such that (a| ρ) = kak. By
lemma 26, ρ must be pure. Moreover, this pure state
must be unique: suppose that ϕ and ϕ′ are pure states
such that (a| ϕ) = (a| ϕ′ ) = kak. Then for ω = 1/2(ϕ +
ϕ′ ) one has (a| ω) = kak. Since ω must be pure, one has
ϕ = ϕ′ . 
We now show the converse result: for every pure state
ϕ ∈ St1 (A) there exists a unique atomic effect a such
that (a| ϕ) = 1. Let us start from the existence:
Lemma 27 Let {ϕi }N
i=1 ⊂ St1 (A) be a maximal set of
perfectly distinguishable pure states and let {ai }N
i=1 be the
observation-test such that (ai | ϕj ) = δij . Then each effect
ai is atomic with kai k = 1.

Proof. It is obvious that kai k = 1, because of the condition (ai | ϕi ) = 1. It remains to prove atomicity. Consider
PN
the state ω = i=1 ϕi /N , which is completely mixed by
theorem 6. Let Ψω ∈ St1 (AB) be a purification of ω,
chosen in such a way that the marginal on system B
is completely mixed (theorem 4). As a consequence of
purification (lemma 12), there exists an observation-test
{bi }N
i=1 on system B such that (bi |B |Ψω )AB = 1/N |ϕi )A .
Since Ψω is dynamically faithful on system B, each effect
bi must be atomic. Now, define the normalized states
N
{ρi }N
i=1 ⊂ St1 (B) and the probabilities {pi }i=1 by
?>
89Ψω

A

ai "%$#

B

= pi '!&ρi

B

(10)

Applying the deterministic effect eB on both sides one
has pi = (ai | ω) = 1/N . On the other hand, applying the
effect bj one has instead 1/N (bj | ρi )B = 1/N (ai | ϕj ) =
δij /N . This implies (bi | ρi ) = 1 for every i. Since bi
is atomic, lemma 26 forces each ρi to be pure. Finally,
each ai must be atomic since its Choi state pi |ρi )B =
(ai |A |Ψω )AB is pure (theorem 2). 
As a consequence, we can prove the following existence
result:
Lemma 28 For every pure state ϕ ∈ St1 (A) there exists
an atomic effect such that (a| ϕ) = 1.
Proof. By corollary 11, every pure state belongs to
a maximal set of perfectly distinguishable pure states
{ϕi }N
i=1 , say ϕ = ϕ1 . The thesis then follows from lemma
27. 
We now prove that the atomic effect a such that
(a|ϕ) = 1 is unique. For this purpose we need two auxiliary lemmas:
Lemma 29 Let ϕ ∈ St1 (A) be an arbitrary pure state
and let pϕ be the probability defined by
pϕ = max {p : ∃σ, χ = pϕ + (1 − p)σ}

(11)

where χ is the invariant state of system A. Then the
value of the probability pϕ is independent of ϕ.
Proof. Since for every couple of pure states ϕ and ψ one
has ψ = U ϕ for some reversible channel U (lemma 9),
and since χ is invariant, one has χ = pϕ + (1 − p)σ if and
only if χ = pψ + (1 − p)U σ. The maximum probabilities
for ϕ and ψ are then equal. 
Since pϕ = pψ for every couple of pure states, from
now on we will write pmax in place of pϕ .
Lemma 30 Let ϕ ∈ St1 (A) be a pure state and a ∈
Eff(A) be an atomic effect such that (a| ϕ) = 1. Let |Φ)AB
be a purification of the invariant state |χ)A , chosen in
such a way that the marginal on system B is completely
mixed, and let b be the unique atomic effect on B such
that
?>
89Φ

A
B

b-*+,

= pmax '!&ϕ

A

(12)

<!-- page 19 -->
19
[note that b exists by lemma 12is uniquely defined by Eq.
(12) because Φ is faithful for system B]. Then one has
a

A

?>
89Φ

B

= pmax (/.)ψ

B

(13)

where ψ is the unique pure state such that (b| ψ) = 1.
Proof. Define the normalized pure state ψ and the probability q by
q (/.)ψ

B

=

?>
89Φ

A

a

B

(14)

In order to prove the thesis we have to show that q = pmax
and (b| ψ) = 1. Applying b on both sides of Eq. (14) and
using Eq. (12) we obtain q (b| ψ) = pmax (a| ϕ) = pmax .
This implies
q ≥ pmax ,

(15)

with the equality if and only if (b| ψ) = 1. Let b′ be an
atomic effect such that (b′ | ψ) = 1 (such an effect exists
because of lemma 28 ). Define the normalized pure state
ϕ′ and the probability p′ by
p′ 7016ϕ′

A

=

?>
89Φ

A
B

b′ -*+,

Applying a on both sides and using Eq. (14) we obtain
p′ (a| ϕ′ ) = q (b′ | ψ) = q, which implies p′ ≥ q, with the
equality if and only if (a| ϕ′ ) = 1. Combining this with
the inequality (15) we have p′ ≥ q ≥ pmax . On the other
hand, by Lemma 29 one has p′ ≤ pmax , and consequently
p′ = q = pmax . This also implies that (b| ψ) = 1 and
(a| ϕ′ ) = 1. 
Theorem 8 For every pure state ϕ ∈ St1 (A) there is a
unique atomic effect a ∈ Eff(A) such that (a| ϕ) = 1.
Proof. Existence has been already proved in lemma
28. Let us prove uniqueness: suppose that a and a′ are
two atomic effects such that (a| ϕ) = (a′ | ϕ) = 1. Then,
applying lemma 30 to a and a′ we obtain
?>
89Φ

A
B

a

=

?>
89Φ

A

a′ -*+,

B

Since Φ is dynamically faithful, this implies a = a′ . 
Finally, an important consequence of theorem 8 is
Corollary 13 If a, a′ ∈ Eff(A) are two atomic effects
with kak = ka′ k = 1, then there is a reversible channel
U ∈ GA such that (a′ |A = (a|A U .
Proof. Let ϕ and ϕ′ be the (unique) normalized states
such that (a| ϕ) = 1 and (a′ | ϕ′ ) = 1, respectively.
Now, there is a reversible channel U ∈ GA such that
|ϕ)A = U |ϕ′ )A . Hence, (a′ | ϕ′ ) = (a| ϕ)A = (a| U |ϕ′ ).
By theorem 8, one has (a′ |A = (a|A U . 
We conclude this section with an elementary result
that will be used later in the paper:

Lemma 31 Let E ∈ Transf(A, C) and D ∈ Transf(C, A)
be the encoding and the decoding in the ideal compression
scheme for ρ ∈ St1 (A). If |ϕ) ∈ Fρ is a pure state and
(a| ∈ Eff(A) is the atomic effect such that (a| ϕ) = 1, then
|γ) := E |ϕ) ∈ St1 (C) is a pure state and (c| := (a| D ∈
Eff(C) is the atomic effect such that (c| γ) = 1.
Proof. The state |γ) := E |ϕ) is pure by lemma 4. The
effect (c| := (a| D is atomic by lemmas 14 and 16. Since
DE =ρ IA , one has (c| γ) = (a| DE |ϕ) = (a|ϕ) = 1. 
VII.

DIMENSION

In this section we show that each system in our theory has given informational dimension, defined as the
maximum number of perfectly distinguishable pure states
available in the system. In the Hilbert space framework,
the informational dimension will be the dimension of the
Hilbert space.
Lemma 32 All maximal sets of perfectly distinguishable
pure states have the same number of elements.
Proof. Let {ϕi }N
i=1 be a maximal set of perfectly distinguishable pure states for system A, and let {ai }N
i=1
the observation-test such that (ai | ϕj ) = δij . By lemma
27, each ai is atomic and kai k = 1. Then, by corollary 13, one has (ai |A = (a0 | Ui , where each Ui is a
reversible channel and a0 is a fixed atomic effect with
ka0 k = 1. By the invariance of χ we then obtain
(ai |χA ) = (a0 |Ui |χA ) = (a0 |χA ). On the other hand, one
PN
has i=1 (ai | χA ) = 1, which implies N = 1/ (a0 | χA ).
Since a0 is arbitrary, N is independent of the choice of
the set {ϕi }N
i=1 . 
As a consequence, the number of perfectly distinguishable pure states in a maximal set is a property of the
system A. We will call this number the informational
dimension (or simply the dimension) of system A, and
denote it with dA . The informational dimension dA has
not to be confused with the size DA of the state space
St(A): recall that DA was defined as the dimension of
the real vector space StR (A). In quantum theory one has
DA = d2A .
An immediate consequence of the proof of lemma 32 is
Corollary 14 For every atomic effect a with kak = 1
one has (a| χA ) = 1/dA .
This simple fact has two very important consequences.
The first is that the dimension of a composite system is
the product of the dimensions of the components:
Corollary 15 The dimension of the composite system
AB is the product of the dimensions of A and B, namely
dAB = dA dB .

<!-- page 20 -->
20
Proof. From lemma 10 we know that χA ⊗ χB is the
unique invariant state of system AB. Now, if a ∈ Eff(A)
and b ∈ Eff(B) are such that kak = kbk = 1, then a ⊗
b is such that ka ⊗ bk = 1. Hence we have 1/dAB =
(a ⊗ b| χA ⊗ χB ) = (a| χA ) (b| χB ) = 1/(dA dB ). 
The second consequence is the relation between the
dimension and the maximum probability of a pure state
in the convex decomposition of the invariant state |χ)A :
Lemma 33 For every system A, the maximum probability of a pure state in the convex decomposition of the
invariant state is pmax = 1/dA .
Proof. Let Φ ∈ St1 (AB) be a purification of the invariant state |χA ), chosen in such a way that the marginal
on system B is completely mixed. Let a ∈ Eff(A) be an
atomic effect with kak = 1. Then, equation (13) becomes
?>
89Φ

A
B

a

=

pmax

(/.)ψ

B

where ψ is some normalized pure state of system B. Applying the deterministic effect e on system B on both
sides we obtain (a| χA ) = pmax . Finally, corollary 14
states (a| χA ) = 1/dA . By comparison, we obtain pmax =
1/dA . 
Thanks to the compression axiom 3, the notion of dimension can be applied not only to the whole state space
St1 (A) but also to its faces. With face F of the convex
set St1 (A) we always mean the face Fρ identified by some
state ρ ∈ St1 (A).
Lemma 34 Let F be a face of the convex set St1 (A). Every maximal set {ϕi }ki=1 of perfectly distinguishable pure
states in F has the same cardinality k. Precisely, if F is
the face identified by ρ ∈ St1 (A) and E ∈ Transf(A, C) is
the encoding in the ideal compression for ρ, then we have
k = dC

Lemma 35 Let {ρi }N
i=1 ⊂ St1 (A) be a set of states. If
there exists a set of effects {bi }N
i=1 ⊂ Eff(A) (not necessarily an observation-test) such that (bi |ρj ) = δij , then
the states {ρi }N
i=1 are perfectly distinguishable.
Proof. For each i = 1, . . . , N consider the binary test
{bi , e − bi }. Since by hypothesis (bi | ρj ) = δij , the test
{bi , e − bi } can perfectly distinguish ρi from any mixture
of the states {ρj }j6=i . In particular, this means that, for
every M < N , ρM+1 can be perfectly distinguished from
PM
the mixture ωM =
j=1 ρj /M . Note that, by definition, the states {ρi }M
i=1 belong to the face FωM . We now
prove by induction on M that the states {ρi }M
i=1 are perfectly distinguishable. This is true for M = 1. Now,
suppose that the states {ρi }M
i=1 are perfectly distinguishable. Since the state ρM+1 is perfectly distinguishable
from ωM , by lemma 23 we have that the states {ρi }M+1
i=1
are perfectly distinguishable. Taking M = N − 1 the
thesis follows. 
We now show that the invariant state χ is a mixture
of perfectly distinguishable pure states.
Theorem 9 For every maximal set of perfectly distinA
⊂ St1 (A) one has
guishable pure states {ϕi }di=1
d

χ=

A
be the observation test such that
Proof. Let {ai }di=1
(ai | ϕj ) = δij , and Φ ∈ St1 (AB) be a purification of χ,
chosen in such a way that the marginal on system B is
A
⊂ St1 (B) be
completely mixed (theorem 4). Let {ψi }di=1
the pure states defined by

?>
89Φ

The set {E ϕi }ki=1 ⊂ St1 (C) is perfectly distin-

Proof.
guishable by lemma 25, and it is maximal by corollary
12. Moreover, the states {E ϕi }ki=1 are pure by lemma
4. Hence, the cardinality k of the set {ϕi }ki=1 must be
k = dC . 
From now on the maximum number of perfectly distinguishable states in the face F will be called the dimension
of the face F and will be denoted by |F |.
VIII.

DECOMPOSITION INTO PERFECTLY
DISTINGUISHABLE PURE STATES

In this section we show that in a theory satisfying our
principles any state can be written as a convex combination of perfectly distinguishable pure states. In quantum
theory, this corresponds to the diagonalization of the density matrix.
To prove this result we need first a sufficient condition
for the distinguishability of states, given in the following

A
1 X
ϕi .
dA i=1

A

ai "%$#

B

=

1 (/.)
ψi
dA

B

and, for each i, let bi be the atomic effect such that
?>
89Φ

A
B

bi -*+,

=

1 '!&
ϕi
dA

A

(16)

(here we used lemma 30 and the fact that pmax = 1/dA ).
Then we have
(/.)ψi

B

?>
bj 2543 = dA 89Φ
= (/.)ϕj

A

A

ai "%$#

B

bj 2543
ai "%$# = δij .

(17)

A
are perBy lemma 35, this implies that the states {ψi }di=1
fectly distinguishable. Now, since the marginal of |Φ)AB
on system B is completely mixed, theorem 6 states that
A
A
the observation
is maximal. Let {b′i }di=1
the set {ψi }di=1
′
test such that (bi | ψj ) = δij . By lemma 27, each b′i must
be atomic. On the other hand, there is a unique atomic

<!-- page 21 -->
21
effect bi such that (bi | ψi ) = 1 (theorem 8). Therefore,
A
form an obb′i = bi . This means that the effects {bi }di=1
servation test. Once this fact has been proved, using Eq.
(16) we obtain
|χ)A = (eB | |Φ)AB
X
(bi | |Φ)AB
=
i

= 1/dA

X
i

|ϕi ) .


As a consequence, we have the following
Corollary 16 (Existence of conjugate systems)
For every system A there exists a system Ã, called the
conjugate system, and a purification Φ ∈ St1 (AÃ) of the
invariant state χA such that dÃ = dA and the marginal
on Ã is the invariant state χÃ . The conjugate system Ã
is unique up to operational equivalence.
Proof. We first prove that Ã is unique up to operational
equivalence. The defining property of the conjugate system Ã is that the marginal of Φ on Ã is the invariant state
χÃ , which is completely mixed. Theorem 4 then implies
that Ã is unique up to operational equivalence. Let us
now show the existence of Ã. Take a purification of χA ,
with purifying system Ã chosen so that the marginal of
Φ on Ã is completely mixed (this is possible thanks to
A
⊆ St(B), defined
theorem 4). Now, the states {ψi }di=1
1
by dA |ψi ) := [(ai | ⊗ IÃ ]|Φ), are perfectly distinguishable
[see Eq. (17) in the proof of theorem 9]. Hence, by theorem 6 they are a maximal set of perfectly distinguishable
pure states. This implies dÃ = dA . Finally, by theorem
PdÃ
9 one has 1/dÃ i=1
ψi = χÃ . 
Corollary 17 The distance between the invariant state
χA and an arbitrary pure state ϕ ∈ St1 (A) is
2(dA − 1)
kχ − ϕk =
.
dA
Proof. Take a maximal set of perfectly distinguishable
A
such that ϕ1 = ϕ (corollary 11).
pure states {ϕi }di=1
PdA
Since χ = i=1 ϕi /dA one has χ − ϕ = (dAdA−1) (σ − ϕ1 ),
PdA
where σ = i=2
ϕi /(dA − 1). Hence, one has kχ − ϕk =
2(dA −1)
(dA −1)
kσ
−
ϕ
k
=
, having used that σ and ϕ1
1
dA
dA
are perfectly distinguishable and therefore kσ − ϕ1 k = 2
(see subsection II-I in Ref. [21]). 
We can now prove the following strong result:
Theorem 10 (Spectral decomposition) For every
system A, every mixed state can be written as a convex
combination of perfectly distinguishable pure states.

Proof. The proof is by induction on the dimension of
the system. If dA = 1, the thesis trivially holds. Now
suppose that the thesis holds for any system B with dimension dB ≤ N , and take a mixed state ρ ∈ St1 (A)
where dA = N + 1. There are two possibilities: either (1)
ρ is not completely mixed or (2) ρ is completely mixed.
Suppose that (1) ρ is not completely mixed. Then by
the compression axiom 3 one can encode it in a system
C, using an encoding operation E ∈ Transf(A, C). Now,
the maximum number of perfectly distinguishable states
in C is equal to the maximum number of perfectly distinguishable states in the face Fρ (corollary 12). Since ρ
is not completely mixed, we must have dC ≤ N . Using
the induction hypothesis we then obtain that the state
E ρ ∈ St1 (C) is a mixture
of perfectly distinguishable pure
P
states, say E ρ = i pi ψi . Applying the decoding
P operation D ∈ Transf(C, A) we get ρ = DE ρ = i pi Dψi .
Since by lemmas 4 and 25 we know that the states
C
are pure and perfectly distinguishable, this is
{Dψi }di=1
the desired decomposition for ρ. Now suppose that ρ is
completely mixed (2). Consider the half-line in StR (A)
defined by σt = (1 + t)ρ − tχ, t ≥ 0. Since the set of
normalized states St1 (A) is compact, the line will cross
its border at some point t0 . Therefore, one will have
ρ=

1
t0
σt +
χ.
1 + t0 0 1 + t0

for some state σt0 on the border of St1 (A), that is, for
some state that is not completely mixed. But we know
from the discussion of point (1) that the state σt0 is
a mixture of perfectly distinguishable pure states, say
Pk
σt0 =
i=1 pi ϕi . By lemma 24, this set can be extended to a maximal set of perfectly distinguishable pure
A
. On the other hand, theorem 9 states that
states {ϕi }di=1
PdA
χ = i=1 ϕi /dA . This implies the desired decomposition
ρ=

d
A 
X
i=1

qi
t0
+
1 + t0
dA (1 + t0 )



ϕi ,

where qi = pi for 1 ≤ i ≤ k, and qi = 0 otherwise. 
It is easy to show that the marginals of a pure bipartite
state have the same spectral decomposition:
Corollary 18 Let Ψ ∈ St1 (AB) be a pure state, and let
ρ and ρ̃ be the marginals of Ψ on systems A and B, reP A
spectively. If ρ has spectral decomposition ρ = di=1
pi ϕi ,
with pi > 0 for every i = P
1, . . . , r, r ≤ dA , then ρ̃ has
spectral decomposition ρ̃ = ri=1 pi ψi .

A
be the observation-test such that
Proof. Let {ai }di=1
r
(ai | ϕj ) = δij , {bi }i=1 be the observation test such that
(bi |B |Ψ)AB = pi |ϕi )A for every i ≤ r. For i ≤ r, define
the pure state ψi ∈ St1 (B) and the probability qi via the
relation

qi |ψi )B := (ai |A |Ψ)AB .

<!-- page 22 -->
22
[Note that ψi is pure due to the pure conditioning axiom]
By definition, we have
qi (bj | ψi ) = (ai ⊗ bj | Ψ)
= (ai | ϕj )
= pi δij
∀i ≤ r, ∀j ≤ r.
PdA
The above relation implies qi =
j=1 qi (bj | ψi ) =
P
p
δ
=
p
and
(b
|
ψ
)
=
δ
.
Hence,
the states
i
j
i
ij
j i ij
r
{ψi }i=1 are perfectly distinguishable. On the other hand,
we have (ai ⊗ eB | Ψ) = (ai | ρ) = 0 ∀i > r, which implies
(ai |A |Ψ)AB = 0, ∀i > r . Therefore, we obtained
|ρ̃)B = (e|A |Ψ)AB
=
=
=

dA
X

i=1
r
X

i=1
r
X
i=1

(ai |A |Ψ)AB
(ai |A |Ψ)AB
pi |ψi )A ,

which is the desired spectral decomposition. 
The spectral decomposition of states has many consequences. Here we just discuss the simplest ones, which
are needed for the purpose of the derivation of quantum
theory.
A first consequence is the following lemma:
Lemma 36 Let ϕ ∈ St1 (A) be a pure state and let a ∈
Eff(A) be the unique atomic effect such that (a| ϕ) = 1.
If ϕ is perfectly distinguishable from ρ, then (a| ρ) = 0.
Pk
Proof. Let us write ρ = i=1 pi ϕi , with {ϕi }ki=1 perfectly distinguishable pure states and pi > 0 for each i.
Now, by lemma 23 the states {ϕ1 , . . . , ϕk , ϕ} are perfectly
distinguishable, and by lemma 24 this set can be extended to a maximal set of perfectly distinguishable pure
A
states {γm }dm=1
, with γi = ϕi for i ≤ k and γk+1 = ϕ.
A
Denote by {cm }dm=1
the observation test that perfectly
distinguishes between the states {γm }. Note that, by
definition, (ck+1 | ϕ) = 1 and (ck+1 | ϕj ) = 0 for every
j 6= k + 1. Also, recall that ck+1 is atomic (lemma 27).
By the duality of theorem 8 we have a = ck+1 , and,
Pk
therefore, (a| ρ) = i=1 pi (ck+1 | ψi ) = 0. 
Another consequence of theorem 10 is the following
characterization of the completely mixed states as full
rank states:
Corollary 19 (Characterization of completely
mixed states) A state ρ ∈ St1 (A), written as a
PdA
mixture ρ =
i=1 pi ϕi of a maximal set of perfectly
A
, is completely mixed
distinguishable pure states {ϕi }di=1
if and only if pi > 0 for every i = 1, . . . , dA .

Proof. Necessity: If pi = 0 for some i, then ρ is perfectly
distinguishable from ϕi . Hence, it cannot be completely
mixed. Sufficiency: let pmin = min{pi , i = 1, . . . , dA }.
Then we have ρ = pmin χ + (1 − pmin )σ, where σ is the
PdA
(pi − pmin /dA )ϕi .
state defined by σ = 1/(1 − pmin ) i=1
Since ρ contains χ in its convex decomposition, and since
χ is completely mixed, we conclude that ρ is completely
mixed. 
In particular, for two-dimensional systems we have the
result:
Corollary 20 For dA = 2 any state on the border of
St1 (A) is pure.
Another consequence of theorem 10 is that every element in the vector space StR (A) can be written as a
linear combination of perfectly distinguishable states:
Corollary 21 For every ξ ∈ StR (A) there exists a maxA
imal set of perfectly distinguishable pure states {ϕi }di=1
dA
and a set of real numbers {ci }i=1 such that |ξ) =
P
i ci |ϕi ).

Proof. Write ξ as ξ = c+ ρ−c− σ, where c+ , c− ≥ 0 and ρ
and σ are normalized states. If c− = 0 there is nothing to
prove, because ξ is proportional to
Pa state. Then, suppose
that c− > 0. Write σ as σ = i pi ψi where {ψi } are
perfectly distinguishable and define k = max{pi }. Then
one has χ+1/(c−kdA )ξ = (χ−1/(kdA )σ)+c+ /(c− kdA )ρ.
Now, by definition χ−1/(kdA )σ is proportional
to a state:
P
indeed we have (χ − 1/(kdA )σ) = 1/dA i (1 − pi /k)ψi ,
and, by definition 1−pi/k ≥ 0. Therefore χ+1/(c−kdA )ξ
is proportional to a state, say χ + 1/(c− kdA )ξ = tτ , with
P
dA
t > 0. Writing τ as τ =
i qi ϕi , where {ϕi }i=1 is a
maximal set of perfectly distinguishable pure states,
we
P
then obtain ξ = (c− kdA )(tτ − χ) = (c− kdA ) i (tqi −
1/dA )ϕi , which is the desired decomposition. 
In quantum theory, corollary 21 is equivalent to the
fact that every Hermitian matrix is diagonal in a suitable
orthonormal basis. A simple consequence of corollary 21
is the following
Corollary 22 For every system A with dA = 2 there is
a continuous set of pure states.
Proof. Let ξ ∈ StR (A) be an arbitrary vector such that
(e| ξ) = 0. Note that since the convex set St1 (A) cannot be a segment (corollary 7), we must have DA =
dim[StR (A)] > 2 and, therefore, the space of vectors ξ
such that (e| ξ) = 0 is at least two-dimensional. By corollary 21, we have ξ = c(ϕ1 − ϕ2 ) = 2c(ϕ1 − χ), where
c ≥ 0, {ϕ1 , ϕ2 } are two perfectly distinguishable pure
states and we used the fact that χ = 21 (ϕ1 + ϕ2 ). Let
us define ϕξ := ϕ1 . With this definition, if ϕξ1 = ϕξ2
then one has ξ2 = tξ1 for some t ≥ 0. Now, since there
is a continuous infinity of vectors ξ (up to scaling), there
must be a continuous set of pure states. 
We conclude this section with the dual result to the
“spectral decomposition” of corollary 21:

<!-- page 23 -->
23
Corollary 23 For every x ∈ Eff R (A) there exists a perA
and a set of
fectly distinguishing observation-test {ai }di=1
P
dA
real numbers {di }i=1 such that (x| = i di (ai |.
Proof. Let Φ ∈ St1 (AÃ) be a purification of the invariant state χA , where Ã is the conjugate system defined in corollary 16. Take the Choi vector |Rx )Ã :=
(x|A |Φ)AÃ . By corollary 21, there exists a maximal set
A
and a
of perfectly distinguishable pure states {ψi }di=1
P
dA
set of real numbers {ci }i=1 such that |Rx ) = i ci |ψi ).
A
⊂ Eff(A) be the observation-test such that
Let {ai }di=1
1/dA |ψi )Ã = (ai |A |Φ)AÃ for every i = 1, . . . , dA (recall
that by corollary 16 the marginal of Φ on system Ã is
A
the invariant state χÃ and dÃ = dA ). The test {ai }di=1
dA
is perfectly distinguishing: if {bi }i=1 is the observationtest such that (bi | ψj ) = δij and ϕi ∈ St1 (A) is the state
defined by |ϕi )A := dA (bi |Ã |Φ)AÃ , then we have
(ai | ϕj ) = dA (ai ⊗ bj | Φ)
= (bj | ψi )
= δij .

|Φ)AÃ |Φ)AÃ satisfies the identity
?>
89Φ

A

?>
89Φ

A

e
=
e

Ã

i

ci dA (ai |A |Φ)AÃ .

Since Φ is dynamically faithful, this implies (x| =
P
i di (ai |, where di := ci dA . 
IX.

TELEPORTATION REVISITED

In this section we revisit probabilistic teleportation
using the results about informational dimension. The
key point is the section will be the proof the equality
DA = d2A , which relates the dimension of the vector space
StR (A) with the informational dimension dA .
A.

Probability of teleportation

Ã

'!&χ

=

AÃ

A

?>
89Φ

Ã

1
=<
E:; = 2
dA

A

?>
89Φ

?>
89Φ

A

(18)

Ã

Ã

and, since Φ is dynamically faithful,
A

?>
89Φ

1
=< = 2
d
E:;
A

Ã

A

I

A

(19)

as can be verified applying both members of Eq. (19) to
Φ, thus obtaining Eq. (18). 

i

=

'!&χ

On the other hand, by lemma 33 the maximum probability of a pure state in the convex decomposition of χAÃ
is pmax = 1/dAÃ , and by corollaries 15 and 16 one has
pmax = 1/(dA dÃ ) = 1/d2A . Therefore, by lemma 12 there
exists an atomic effect E such that

A

X

A

Ã

Moreover, we have
(x|A |Φ)AÃ = |Rx )Ã
X
ci |ψi )Ã
=

'!&χ

B.

Isotropic states and effects

Here we define two maps that send reversible transformations of A to reversible transformations of Ã: the
transpose and the conjugate. Using these maps we will
also define the notions of isotropic states and effects and
we will prove some properties of them.
Let us start from the definition of the transpose:
Lemma 37 (Transpose of a reversible transformation) Let Φ ∈ St(AÃ) be a purification of the invariant
state χA . The reversible transformations of system Ã are
in one-to-one correspondence with the reversible transformations of system A via the transposition τ defined as
follows
?>
89Φ

A

U

A

=
Ã

?>
89Φ

A
Ã

Uτ

Ã

(20)

We start by showing a probabilistic teleportation
scheme that achieves success probability pA = 1/dA for
every system A:

[note that the transposition is defined with respect to the
given state Φ]

Theorem 11 (Probability of teleportation) For
every system A, probabilistic teleportation can be
achieved with probability pA = 1/d2A .

Proof. Since (U ⊗ IÃ )|Φ) and |Φ) are purifications
of the same state χA , there exists a reversible transformation U τ ∈ GÃ such that Eq. (20) holds. Since Φ is
dynamically faithful on A, the map U 7→ U τ is injective.
Furthermore, the map is surjective: for every reversible
V ∈ GÃ the states (IA ⊗ V ) |Φ) and |Φ) are two purifications of the same state χÃ , and, by the uniqueness of

Proof. Let Ã and |Φ)AÃ be the conjugate system and
the pure state defined in corollary 16. Then, the state

<!-- page 24 -->
24
purification stated in postulate 1, there exists a reversible
U ∈ GA such that
A

?>
89Φ

Ã

V

Ã

=

A

?>
89Φ

A

U

(21)

Ã

namely V = U τ . 
The conjugate is just defined as the inverse of the transpose:
Definition 7 Let τ be the transpose defined with respect
to the state Φ ∈ St1 (AÃ). The conjugate of the reversible
channel U ∈ GA is the reversible channel U ∗ ∈ GÃ
defined by U ∗ := (U τ )−1 .
We can now give the definition of isotropic pure state
(isotropic atomic effect):
Definition 8 A pure state Ψ ∈ St(AÃ) (an atomic effect
F ∈ Eff(ÃA)) is isotropic if it is invariant under the
U ⊗ U ∗ (under U ∗ ⊗ U ). Diagrammatically




?>
89Ψ

A
Ã

U∗

Ã

U∗

Ã

A

U

A

U

A
Ã

=

=<
F:; =

A

?>
89Ψ
Ã
A

Ã

∀U ∈ GA

=<
F:;



∀U ∈ GA

(22)

An example of isotropic state is Φ: indeed, by definition of conjugate we have, for every U ∈ GA ,
∗

τ −1

(U ⊗ U ) |Φ) = (U ⊗ (U )

) |Φ)

τ −1

= (IA ⊗ (U )

U τ ) |Φ) = |Φ) .

As a consequence, the teleportation effect E is isotropic:
indeed one has
?>
89Φ

A
Ã

U∗

?>
89Φ

A

U

=<
E:; =

Ã

?>
89Φ

A

U −1

Ã

?>
89Φ

A

=<
E:;

Ã

Uτ

A

Ã

1
d2A

?>
89Φ

A

U −1

A

Ã

Uτ

Ã

1
= 2
dA

?>
89Φ

A

=

=

?>
89Φ

A

?>
89Φ

A

Ã

Ã

=<
E:;

Ã

which implies (E| (U ∗ ⊗ U ) = (E|, since the state Φ ⊗ Φ
is dynamically faithful.

We now show that all isotropic pure states (isotropic
atomic effects) are connected to the state Φ (to the effect
E) through a local reversible transformation.
Lemma 38 If a pure state Ψ ∈ St1 (AÃ) is isotropic then
|Ψ) = (V ⊗ IÃ )|Φ) for some reversible transformation
V ∈ GA such that V U = U V for every U ∈ GA .
Proof. Since Ψ satisfies Eq. (22), its marginal on system Ã is the invariant state |χÃ ). Since Ψ and Φ are
purifications of the same state, there must exist a reversible channel V ∈ GA such that |Ψ) = (V ⊗ IÃ ) |Φ).
Moreover, we have for every U ∈ GA
(U V U −1 ⊗ IÃ ) |Φ) = (U V ⊗ U ∗ ) |Φ)
= (U ⊗ U ∗ ) |Ψ)
= |Ψ)
= (V ⊗ IÃ ) |Φ) .
Since Φ is dynamically faithful, the above equation implies U V U −1 = V for every U ∈ GA . 
By the duality between states and effects, it is easy to
obtain the following:
Lemma 39 Let A ∈ Eff(AÃ) be the atomic effect such
that (A| Φ) = 1. If an atomic effect F ∈ Eff(ÃA) is
isotropic then (F |ÃA = (A|ÃA (IÃ ⊗ V ) for some reversible transformation V ∈ GA such such that V U =
U V for every U ∈ GA .
Proof. Let Ψ be the pure state such that (F | Ψ) =
1. Clearly Ψ is isotropic: one has (F | (U ⊗ U ∗ ) |Ψ) =
(F | Ψ) = 1, and, therefore, (U ⊗ U ∗ ) |Ψ) = |Ψ). By
lemma 38, there exists a reversible transformation V such
that |Ψ) = (V −1 ⊗ IÃ ) |Φ) and V −1 U = U V −1 for
every U ∈ GA . Now, this implies (F | (V −1 ⊗ IÃ ) |Φ) =
(F | Ψ) = 1, which by theorem 8 implies (F | = (A| (V ⊗
IÃ ). 
As a consequence, every isotropic effect is connected
to the teleportation effect by a local reversible transformation:
Corollary 24 If an atomic effect F ∈ Eff(ÃA) is
isotropic then (F |ÃA = (E|ÃA (IÃ ⊗ V ) for some reversible transformation V ∈ GA such that V U = U V
for every U ∈ GA .
Proof. Since (E| and (F | are both isotropic, lemma 39
implies that they are both connected to (A| through a local reversible transformation, say V and W , respectively.
Therefore, they are connected to each other through the
transformation W V −1 . 
C.

Dimension of the state space

In this subsection we use the local distinguishability
axiom to prove the equality DA = d2A (see theorem 12).

<!-- page 25 -->
25
As a consequence, we will be able to represent the states
of a system A as square dA ×dA hermitian complex matrices, that is, hermitian operators on the complex Hilbert
space CdA . Theorem 12 is thus the point where the complex field (as opposed to the real field) enters in our
derivation. Notice that, even if the local distinguishability excludes quantum theory on real Hilbert spaces since
the very beginning, to prove the emergence of complex
Hilbert spaces we need to use all the six principles.
Due to local distinguishability, any bipartite state Ψ ∈
St(AB) can be written as
|Ψ) =

DA X
DB
X

Ψij |αi ) |βj ) ,

i=1 j=1

where {αi } ({βj }) is a basis for the vector space StR (A)
(StR (B)). Similarly, a bipartite effect F ∈ Eff(BA) can
be written as
(F | =

DB X
DA
X

k=1 l=1

Fkl (βk∗ | (α∗l |

with (α∗l | αi ) = δil and (βk∗ | βj ) = δjk . Finally, a transformation C from A to B can be written as

Proof. Let {ξi } be a basis for StR (A), chosen in such a
way that the first basis vector is χ, while the remaining
vectors satisfy (e| ξi ) = 0, ∀i = 2, . . . , DA . Such a choice
is always possible since every vector v ∈ StR (A) can be
written as v = (e| v) χ + ξ, where ξ satisfies (e| ξ) = 0.
Now, since U χ = χ, the first column of MU must be
(1, 0, . . . , 0)T . Moreover, since for every normalized state
ρ, U ρ is a normalized state, one must have (e| U |ξ) = 0
for every ξ such that (e| ξ) = 0. Hence, the first row
of MU must be (1, 0, . . . , 0), namely MU has the block
form of Eq. (24). It remains to show that, with a suitable
choice of basis, the matrix OU in the second block can be
chosen to be orthogonal. Observe that, by definition the
matrices {MU }U ∈GA form a representation of the group
GA : indeed, one has MI = IDA and MU V = MU MV
for every U , V ∈ G. Consider the positive definite matrix P defined by the integral
Z
T
P := dU OU
OU ,
where dU is the Haar measure on the compact group GA
(see corollary 30 of Ref. [21] for the proof of compactness)
and AT denotes the transpose of A. By definition, one
T
has P T = P and OU
P OU = P for every U ∈ GA . Let
us now define the new representation
1

C =

DA
DB X
X
j=1 i=1

Cji |βj ) (α∗i |

In this matrix representation, the teleportation diagram
of Eq. (19) becomes
ΦE =

IDA
,
d2A

(23)

1 ≥ (E| Φ) = Tr[ΦE] =

DA
d2A

DA ≤ d2A .
We now show that one has the equality, using the following standard lemma:
Lemma 40 With a suitable choice of basis for the vector
space StR (A), every reversible transformation U ∈ GA
is represented by a matrix MU of the form
1 0
0 OU



,

As a consequence, we have the following:
Corollary 25 For every system A, the group of reversible transformations GA is (isomorphic to) a compact subgroup of O(DA − 1).
Lemma 41 Let E ∈ Eff(AÃ) be the teleportation effect
of Eq. (19). Then, one has (E| Φ) = 1.

and, therefore,



obtained from OU by a change of basis in the subspace
′
A
spanned by {ξi }D
i=2 . With this choice, each matrix OU
is orthogonal:
 1
T  1

1
1
T
O′ U O′ U = P 2 OU P − 2
P 2 OU P − 2

1
1
T
= P − 2 OU
P OU P − 2 = IDA −1 .


where IDA is the identity matrix in dimension DA . On
the other hand, we also have

MU =

1

′
OU
:= P 2 OU P − 2 ,

(24)

where OU is an orthogonal (DA − 1) × (DA − 1) matrix.

Proof. Let A ∈ Eff(AÃ) be the atomic effect such that
(A| Φ) = 1. We now prove that A = E. Indeed, by corollary 24 there exists a reversible transformation V ∈ GA
such that (A| = (E| (V ⊗ IÃ ). Using a basis for StR (A)
such that the transformations in GA are represented by
orthogonal matrices as in Eq. (24), one has
1 = (A| Φ)
= (E| (V ⊗ IÃ ) |Φ)
= Tr[EMV Φ]
= Tr[ΦEMV ]
=

Tr[MV ]
,
d2A

<!-- page 26 -->
26
having used Eq. (23) for the last equality. Using the
inequality Tr[MV ] ≤ Tr[IDA ], that holds for every orthogonal DA × DA matrix, we then obtain
Tr[MV ]
d2A
Tr[IDA ]
≤
d2A
= Tr[EΦ]
= (E| Φ)
≤ 1,

1=

ans, therefore (E| Φ) = 1 
Theorem 12 (Dimension of the state space) The
dimension DA of the vector space generated by the states
in St(A) is DA = d2A .
Proof. Using lemma 41 and Eq. (23) we obtain 1 =
(E| Φ) = Tr[EΦ] = Tr[IDA ]/d2A = DA /d2A . Hence, DA =
d2A 
An interesting consequence of the relation (E| Φ) = 1
is the following
Corollary 26 (No inversion) Let us write an arbitrary state ρ ∈ St1 (A) as ρ = χA + ξ, with (e| ξ) = 0.
Then, the linear map N defined by N (ρ) = χA − ξ is
not a physical transformation.
Proof. Write the state Φ as Φ = χA ⊗ χÃ + Ξ. Since
(e|A |Φ)AÃ = |χ)Ã one must haveP(e|A |Ξ)AÃ = 0. Therefore, Ξ must be of the form Ξ = i αi ⊗ βi with (e| αi ) =
0 for all i. Applying the transformation N one then obtains (N ⊗ IÃ )Φ = χA ⊗ χÃ − Ξ. We now prove that
this is not a state, and therefore, N cannot be a physical transformation. Let E be the teleportation effect.
Since (E| Φ) = 1, we have 1 = (E| χA ⊗ χÃ ) + (E| Ξ) =
1/d2A + (E| Ξ). Now, we have
(E|(N ⊗ IÃ )|Φ) =

2
1
− (E|Ξ) = 2 − 1,
d2A
dA

Since this quantity is negative for every dA > 1, the map
N cannot be a physical transformation. 
Corollary 27 The matrix MN defined as
!
0
1
,
MN =
0 −IDA −1

(25)

cannot represent a physical transformation of system A.
X.

DERIVATION OF THE QUBIT

In this section we show that every two-dimensional system in our theory is a qubit. With this expression we

mean that the normalized states in St1 (A) can be represented as density matrices for a quantum system with
two-dimensional Hilbert space. With this choice of representation we also show that the effects in Eff(A) are all
the positive Hermitian matrices bounded by the identity,
and that the reversible transformations GA act on the
states by conjugation with unitary matrices in SU(2).
The first step is to prove that the set of normalized
states St1 (A) is a sphere. The idea of the proof is a simple
geometric observation: in the ordinary three-dimensional
space the sphere is the only compact convex set that has
an infinite number of pure states connected by orthogonal transformations. The complete proof is given in the
following
Theorem 13 (The Bloch sphere) The
normalized
states of a system A with dA = 2 form a sphere and the
group GA is SO(3).
Proof. According to corollary 25, the group of reversible
transformations GA is a compact subgroup of the orthogonal group O(3). It cannot be the whole O(3) because, as
we saw in corollary 27, the inversion −I cannot represent
a physical transformation. We now show that GA must
be SO(3) by excluding all the other possibilities. From
corollary 22 we know that the system A has a continuum
of pure states. Therefore, the group GA must contain a
continuous set of transformations. Now, from the classification of the closed subgroups of O(3) we know that
there are only two possibilities: i) GA is SO(3) and ii)
GA is the subgroup generated by SO(2), the group of rotations around a fixed axis, say the z-axis, and possibly
by the reflections with respect to planes containing the
z-axis. Note that the reflection in the xy-plane is forbidden, because the composition of this reflection with the
rotation of π around the z-axis would give the inversion,
which is forbidden by corollary 26. The case ii) is excluded because in this case the action of the group GA
cannot be transitive. The detailed proof is as follows:
because of the SO(2) symmetry, the set of pure states
must contain at least a circle in the xy-plane. This circle
will be necessarily invariant under all operations in the
group. However, since the convex set of states is three dimensional, there is at least a pure state outside the circle.
Clearly, there is no way to transform a state on the circle
into a state outside the circle by means of an operation in
GA . This is in contradiction with the fact that every two
pure states are connected by a reversible transformation.
Hence, the case ii) is ruled out. The only remaining alternative is i), namely that GA = SO(3) and, hence, the
set of pure states generated by its action on a fixed pure
state is a sphere. 
Since the convex set of density matrices on a twodimensional Hilbert space is a sphere, we can represent
the states in St1 (A) as density matrices. Precisely, we
can choose three orthogonal axes passing through the
center of the sphere and call them x, y, z axes, take
ϕ+,k , ϕ−,k , k = x, y, z to be the two perfectly distinguishable pure states in the direction of the k-axis and define

<!-- page 27 -->
27
σk := ϕk,+ − ϕk,− . From the geometry of the sphere we
know that any state ρ ∈ St1 (A) can be written as
|ρ) = |χ) +

1 X
nk |σk )
2

X

k=x,y,z

k=x,y,z

n2k ≤ 1,

(26)

P
where the pure states are those for which k=x,y,z n2k =
1. The Bloch representation Sρ of quantum state
ρ is then obtained by associating the basis vectors
χ, σx , σy , σz to the matrices
!
1 1 0
Sχ =
2 0 1
!
0 −i
Sσy =
i 0

Sσx =
Sσz =

!
0 1
1 0

!
1 0
0 −1

and by defining Sρ by linearity from Eq. (26). Clearly,
in
!

1 + nz nx − iny
, which
nx + iny 1 − nz
is the expression of a generic density matrix. Denoting by
M2 (C) the set of complex two-by-two matrices we have
the following

this way we obtain Sρ = 12

Corollary 28 (Qubit density matrices) For dA = 2
the set of states St1 (A) is isomorphic to the set of density
matrices in M2 (C) through the isomorphism ρ 7→ Sρ .
Once we decide to represent the states in St1 (A) as
matrices, the effects in Eff(A) are necessarily represented
by matrices too. The matrix representation of an effect,
given by the map a ∈ Eff(A) 7→ Ea ∈ M2 (C) is defined
uniquely by the relation
Tr[Ea Sρ ] = (a| ρ)

∀ρ ∈ St(A).

We then have the following
Corollary 29 For dA = 2 the set of effects Eff(A) is
isomorphic to the set of positive Hermitian matrices P ∈
M2 (C) such that P ≤ I.
Proof. Clearly the matrix Ea must be positive for every
effect a, since we have Tr[Ea Sρ ] = (a| ρ) ≥ 0 for every
density matrix Sρ . Moreover, since we have Tr[Ea Sρ ] =
(a| ρ) ≤ 1 for every density matrix Sρ , we must have Ea ≤
I. Finally, we know that for every couple of perfectly
distinguishable pure states ϕ, ϕ⊥ there exists an atomic
effect a such that (a| ϕ) = 1 and (a| ϕ⊥ ) = 0. Since
the two pure states ϕ, ϕ⊥ are represented by orthogonal
rank-one projectors Sϕ and Sϕ⊥ , we must have Ea =
Sϕ . This proves that the atomic effects are the whole set
of positive rank-one projectors. As a consequence, also
every positive matrix P with P ≤ I must represent some
effect a. 
Finally, the reversible transformations are represented
as conjugations by unitary matrices in SU(2):

Corollary 30 For every reversible transformation U ∈
GA with dA = 2 there exists a unitary matrix U ∈ SU(2)
such that
SU ρ = U Sρ U †

ρ ∈ St(A).

(27)

Conversely, for every U ∈ SU(2) there exists a reversible
transformation U ∈ GA such that Eq. (27) holds.
Proof. Every rotation of the Bloch sphere is represented
by conjugation by some SU(2) matrix. Conversely, every
conjugation by an SU(2) matrix represents some rotation on the Bloch sphere. On the other hand, we know
that GA is the group of all rotations on the Bloch sphere
(theorem 13). 
Note that we proved that all two-dimensional systems
A and B in our theory have the same states (St1 (A) ≃
St1 (B)), the same effects (Eff(A) ≃ Eff(B)), and the same
reversible transformations (GA ≃ GB ), but we did not
show that A and B are operationally equivalent. For
example, A and B could be different when we compose
them with a third system C: the set of states St1 (AC)
and St1 (BC) could be non-isomorphic. The fact that every couple of two-dimensional systems A and B are operationally equivalent will be proved later (cf. corollary
40).
We conclude this section with a simple fact that will
be very useful later:
Corollary 31 (Superposition principle for qubits)
Let {ϕ1 , ϕ2 } ⊂ St1 (A) be two perfectly distinguishable
pure states of a system A with dA = 2. Let {a1 , a2 }
be the observation-test such that (ai | ϕj ) = δij . Then,
for every probability 0 ≤ p ≤ 1 there exists a pure state
ψp ∈ St1 (A) such that
(a1 | ψp ) = p

(a2 | ψp ) = 1 − p.

(28)

Precisely, the set of pure states ψp ∈ St1 (A) satisfying
Eq. (28) is a circle in the Bloch sphere.
Proof. Elementary property of density matrices. 

XI.

PROJECTIONS

In this section we define the projection on a face F of
the convex set St1 (A) and we prove several properties of
projections. The projection on the face F will be defined
as an atomic operation ΠF ∈ Transf(A) that acts as the
identity on states in the face F and that annihilates the
states on the orthogonal face F ⊥ . In the following we
first introduce the concept of orthogonal face, then prove
the existence and uniqueness of projections, and finally
give some useful results on the projection of a pure state
on two orthogonal faces.

<!-- page 28 -->
28
A.

Orthogonal faces and orthogonal complements

In order to introduce the notion of orthogonal face we
need first a few elementary results. We start by showing
that there is a canonical way to associate a state ωF to
a face F :
Lemma 42 (State associated to a face) Let F be a
|F |
face of the convex set St1 (A) and let {ϕi }i=1 be a maximal set of perfectly distinguishable pure states in F . Then
P |
the state ωF := |F1 | |F
i=1 ϕi depends only on the face F
|F |

and not on the particular set {ϕi }i=1 . Morever, F is the
face identified by ωF

Proof. Suppose that F is the face identified by ρ and
let E ∈ Transf(A, C) (resp. D ∈ Transf(C, A)) be the
encoding (resp. decoding) in the ideal compression for
|F |
ρ. By lemma 4 and corollary 12, {E ϕi }i=1 is a maximal set of perfectly distinguishable pure states of C
P |
and by theorem 9 one has χC = |F1 | |F
i=1 E ϕi . Hence,
1 P|F |
1 P|F |
ωF = |F | i=1 ϕi = |F | i=1 DE ϕi = DχC . Since the
right-hand side of the equality is independent of the par|F |
ticular set {ϕi }i=1 , the state ωF in the left-hand side
is independent too. To prove that F is the face identified by ωF it is enough to observe that ωF is completely
mixed relative to F : this fact follows from the relation
ωF = DχC and from lemma 5 
We now define the orthogonal complement of the state
ωF :
Definition 9 The orthogonal complement of the state
ωF is the state ωF⊥ ∈ St1 (A) ∪ {0} defined as follows:
1. if |F | = dA , then ωF⊥ = 0

2. if F < dA , then ωF⊥ is defined by the relation
χA =

|F |
dA − |F | ⊥
ωF +
ωF
dA
dA

(29)

An easy way to write the orthogonal complement is
|F |

Lemma 43 Take a maximal set {ϕi }i=1 of perfectly distinguishable pure states in F and extend it to a maxiA
of perfectly distinguishable pure states in
mal set {ϕi }di=1
St1 (A), then for |F | < dA we have
ωF⊥ =

1
dA − |F |

dA
X

Corollary 32 The states ωF and ωF⊥ are perfectly distinguishable.
|F |

Proof. Take a maximal set {ϕi }i=1 of perfectly distinguishable pure states in F , extend it to a maximal
A
, and take the observation-test such that
set {ϕi }di=1
(ai | ϕj ) = δij . Then the binary test {aF , e − aF }, deP |
fined by aF := |F
i=1 ai distinguishes perfectly between
ωF and ωF⊥ . 
We say that a state τ ∈ St1 (A) is perfectly distinguishable from the face F if τ is perfectly distinguishable from
every state σ in the face F . With this definition we have
the following
Lemma 44 The following are equivalent:
1. τ is perfectly distinguishable from the face F
2. τ is perfectly distinguishable from ωF
3. τ belongs to the face identified by ωF⊥ , i.e. τ ∈ FωF⊥ .
Proof. (1 ⇔ 2) τ is perfectly distinguishable from ωF
if and only if then there exists a binary test {a, e − a}
such that (a| τ ) = 1 and (a| ωF ) = 0. By lemma 19
this is equivalent to the condition (a| τ ) = 1 and a =ωF
0, that is, τ is distinguishable from any state σ in the
face identified by ωF , which by definition is F . (2 ⇒ 3)
|F |
Let {ϕi }i=1 be a maximal set of perfectly distinguishable
P|F |
states in F , ωF = |F1 | i=1 ϕi , and let {ϕi }ki=|F |+1 be
the maximal set of perfectly distinguishable pure states
Pk
in the spectral decomposition τ = i=|F |+1 pi ϕi , with
pi > 0 for every i = |F | + 1, . . . , k. Since τ is perfectly
distinguishable from ωF , by lemma 23 we have that the
states {ϕi }ki=1 are all perfectly distinguishable. Let us
A
. By lemma
extend this set to a maximal set {ϕi }di=1
P
d
A
1
⊥
43 have ωF = dA −|F | i=|F |+1 ϕi . Hence, all the states

A
{ϕi }di=|F
⊥.
Since τ is a mixture
|+1 are in the face FωF
of these states, it also belongs to the face FωF⊥ . (3 ⇒
2) Since ωF and ωF⊥ are perfectly distinguishable, if τ
belongs to the face identified by ωF⊥ , then by lemma 22
τ is perfectly distinguishable from ωF . 

Corollary 33 If ρ is perfectly distinguishable from σ and
from τ , then ρ is perfectly distinguishable from any convex mixture of σ and τ .

ϕi .

i=|F |+1

Proof. By definition, for |F | < dA we have ωF⊥ =
1
Substituting the expressions
dA −|F | (dA χA − |F |ωF ).
P|F |
1 PdA
χA = dA i=1 ϕi and ωF = |F1 | i=1 ϕi we then obtain
the thesis. 
Note, however, that by definition the orthogonal complement ωF⊥ depends only on the face F and not on the
choice of the maximal set in lemma 43.
An obvious consequence of lemma 43 is

Proof. Let F be the face identified by ρ. Then by
lemma 44 we have σ, τ ∈ FωF⊥ . Since FωF⊥ is a convex
set, any mixture of σ and τ belongs to it. By lemma
44, this means that any mixture of σ and τ is perfectly
distinguishable from ρ. 
We are now ready to give the definition of orthogonal
face:
Definition 10 (Orthogonal face) The
orthogonal
face F ⊥ is the set of all states that are perfectly
distinguishable from the face F .

<!-- page 29 -->
29
By lemma 44 it is clear that F ⊥ is the face identified by
ωF⊥ , that is F ⊥ = FωF⊥ .
In the following we list few elementary facts about orthogonal faces:
Lemma 45 The following properties hold
1. |F ⊥ | = dA − |F |

of lemma 44 the fact that ρ is perfectly distinguishable
⊥
from ωF ⊥ implies that ρ belongs to F ⊥ , which is just
F (item 5 of lemma 45). 
We now show that the effect aF associated to the face
F exists and is unique. A preliminary result needed to
this purpose is the following:
Lemma 47 The effect aF must have the form aF =
P|F |
i=1 ai , where ai is the atomic effect such that (ai | ϕi ) =
|F |
1 and {ϕi }i=1 is a maximal set of perfectly distinguishable pure states in F .

|
|F ⊥ |
2. χA = |F
d A ωF + d A ωF ⊥

3. ωF ⊥ = ωF⊥
4. ωF⊥⊥ = ωF
⊥
5. F ⊥ = F .

Proof. Item 1. If |F | = dA the thesis is obvious. If |F | <
|F |

|F |+|F ⊥ |

dA , take a maximal set {ϕi }i=1 (resp. {ϕj }j=|F |+1 ) of
perfectly distinguishable pure states in F (resp. F ⊥ ).
Hence we have


|F |
|F |+|F ⊥ |
X
X
1
resp. ωF ⊥ = 1
ϕi
ϕj  .
ωF =
|F | i=1
|F ⊥ |
j=|F |+1

By corollary 32 the states ωF and ωF ⊥ are perfectly
|F |+|F ⊥ |
are perdistinguishable. Hence, the states {ϕi }i=1
fectly distinguishable jointly (lemma 23). Now, we must
have |F | + |F ⊥ | = dA , otherwise there would be a pure
state ψ that is perfectly distinguishable from the states
|F |+|F ⊥ |
. This implies that ψ belongs to F ⊥ and
{ϕi }i=1
|F |+|F ⊥ |

that states {ψ} ∪ {ϕj }j=|F |+1 are perfectly distinguishable in F ⊥ , in contradiction with the hypotheses that the
|F |+|F ⊥ |
set {ϕj }j=|F |+1 is maximal in F ⊥ . Item 2 Immediate
from item 1 and definition 9. Item 3 and 4 Both items
follow by comparison of item 2 with Eq. 29. Item 5 By
⊥
condition 3 of lemma 44, F ⊥
is the face identified by
the state ωF⊥⊥ , which, by item 4, is ωF . Since the face
⊥
identified by ωF is F , we have F ⊥ = F . 
We now show that there is a canonical way to associate
an effect aF to a face F :

Definition 11 (Effect associated to a face) We say
that aF ∈ Eff(A) is the effect associated to the face F ⊆
St1 (A) if and only if aF =ωF e and aF =ωF⊥ 0.
In other words, the definition imposes that (aF | ρ) = 1
for every ρ ∈ F and (aF | σ) = 0 for every σ ∈ F ⊥ .
Lemma 46 A state ρ ∈ St1 (A) belongs to the face F if
and only if (aF |ρ) = 1.
Proof. By definition, if ρ belongs to F , then (aF |ρ) = 1.
Conversely, if (aF |ρ) = 1, thenρ is perfectly distinguishable from ωF⊥ , because (aF | ωF⊥ = 0. Now, we know that
ωF⊥ is equal to ωF ⊥ (item 4 of lemma 45). By item 2

Proof. ByPcorollary 23 we have that aF can be written
A
is a perfectly distinas (aF | = i di (ai | where {ai }di=1
guishing test. Moreover, since aF is an effect, we must
have di ≥ 0 forall
i = 1, . . . , dA . Now, by definition
we


have (aF | ωF⊥ = 0, which implies di (ai | ωF⊥ = 0 for every i = 1, . . . , dA , that is, (ai | ωF⊥ = 0 whenever di 6= 0.
Let us focus on the values of i for which di 6= 0. Let
ϕi be the 
pure state such that (ai | ϕi ) = 1. The condition (ai | ωF⊥ = 0 implies that ϕi is perfectly distinguishable from ωF⊥ . Therefore, ϕi belongs to (F ⊥ )⊥ , which
is F . Since by definition we must have (aF | ϕi ) = 1,
this also implies
that di = 1. In summary, we proved
P′
that aF = i ai where the prime means that the sum is
restricted to those values of i such that ϕi ∈ F . The condition aF =ωF e also implies that the number of terms in
the sum must be exactly |F |. The thesis is then proved
A
, in such a way
by suitably relabelling the effects {ai }di=1
that ϕi belongs to F for every i = 1, . . . , |F |. 
Lemma 48 The effect aF associated to the face F is
unique.
P|F |
P|F |
Proof. Suppose that aF = i=1 ai and a′F = i=1 a′i
are two effects associated to the face F , both written as in
|F |
|F |
lemma 47. Let {ϕi }i=1 (resp. {ϕ′i }i=1 ) be the maximal
set of perfectly distinguishable pure states in F such that
(ai | ϕi ) = 1 for every i = 1, . . . , |F | (resp. (a′i | ϕ′i ) = 1
|F ⊥ |

for every i = 1, . . . , |F |), and let {ψj }j=1 be a maximal set of perfectly distinguishable pure states in F ⊥ .
Since ωF and ωF⊥ are perfectly distinguishable, the states
|F |

|F ⊥ |

|F |

|F ⊥ |

{ϕi }i=1 ∪{ψj }j=1 (resp. {ϕ′i }i=1 ∪{ψj }j=1 are perfectly
distinguishable (lemma 23). Moreover, the set is maximal since |F | + |F ⊥ | = dA . Let bj be the atomic effect
such that (bj | ψj ) = 1. Then, the test that distinguishes
|F |

|F ⊥ |

|F |

|F ⊥ |

|F |

|F ⊥ |

|F |

|F ⊥ |

the states {ϕi }i=1 ∪ {ψj }j=1 (resp. {ϕ′i }i=1 ∪ {ψj }j=1

is given by {ai }i=1 ∪ {bj }j=1 (resp. {a′i }i=1 ∪ {bj }j=1
and its normalization reads
e=

ai +

|F |
X

a′i +

i=1

X

b j = aF +

X

bj = a′F +

bj ,

X

bj .

|F ⊥ |

|F ⊥ |

j=1

X
j=1

j=1

i=1

e=

|F ⊥ |

|F ⊥ |

|F |
X

j=1

<!-- page 30 -->
30
By comparison we obtain aF = a′F . 

St1 (B). Since ΠF =ωF IA , we have
|σ) = (ΠF ⊗ IB ) |σ)

B.

Projections

We are now in position to define the projection on a
face:
Definition 12 (Projection) Let F be a face of St1 (A).
A projection on the face F is an atomic transformation
ΠF such that
1. ΠF =ωF IA
2. ΠF =ωF⊥ 0
When F is the face identified by a pure state ϕ ∈ St1 (A),
we have F = {ϕ} and call Π{ϕ} a projection on the pure
state ϕ.
The first condition in definition 12 means that the projection ΠF does not disturb the states in the face F . The
second condition means that ΠF annihilates all states in
the orthogonal face F ⊥ . As a notation, we will indicate
⊥
with Π⊥
F the projection on the face F , that is, we will
⊥
use the definition ΠF := ΠF ⊥ .
An equivalent condition for ΠF to be a projection on
the face F is the following:
A
be a maximal set of perfectly
Lemma 49 Let {ϕi }di=1
distinguishable pure states for system A. The transformation ΠF in Transf(A) is a projection on the face gen|F |
erated by the subset {ϕi }i=1 if and only if

1. ΠF =ωF IA
2. ΠF |ϕl ) = 0 for all l > |F |

Proof. The condition is clearly necessary, since by Definition 12 ΠF |ϕl ) = 0 for l > |F |. On the other hand, if
ΠF |ϕl ) = 0 for l > |F | then by definition of ωF⊥ we have
ΠF |ωF⊥ ) = 0, and, therefore ΠF =ωF⊥ 0. 
A result that will be useful later is:
Lemma 50 The transformation ΠF ⊗ IB is a projection
on the face F̃ identified the state ωF ⊗ χB .
Proof. ΠF ⊗ IB is atomic, being the product of
two atomic transformations. We now show that ΠF ⊗
IB =ωF ⊗χB IA ⊗ IB : Indeed, by the local tomography axiom it is easy to see that every state σ ∈ FωF ⊗χB
Pr PdB
can be written as |σ) = i=1 j=1
σij |αi ) |βj ), where
r
B
is a basis for
{αi }i=1 is a basis for Span(F ) and {βj }dj=1

=

r
B
X d
X
i=1 j=1

=

r
B
X
X d
i=1 j=1

σij ΠF |αi ) |βj )
σij |αi ) |βj )

= |σ) ,

which implies ΠF ⊗ IB =ωF ⊗χB IA ⊗ IB . Finally, note
that ωF̃ = ωF ⊗ χB , while ωF̃⊥ = ωF⊥ ⊗ χB . Since we have


(ΠF ⊗ IB ) ωF̃⊥ = ΠF ωF⊥ ⊗ |χB ) = 0, we can conclude

ΠF ⊗ IB =ω⊥ 0. Hence ΠF ⊗ IB is a projection on F̃ .
F̃

In the following we will show that for every face F
there exists a unique projection ΠF and we will prove
several properties of projections. Let us start from an
elementary observation:
Lemma 51 Let ϕ be a pure state in the face F ⊆ St1 (A)
and let a ∈ Eff(A) be the atomic effect such that (a| ϕ) =
1. If A ∈ Transf(A) is an atomic transformation such
that A =ωF IA , then (a| A = (a|. Moreover, if aF is the
effect associated to the face F , then we have (aF | A =
(aF |.
Proof. By lemma 16, the effect (a| A is atomic. Now,
since A |ϕ) = |ϕ), we have (a|A |ϕ) = (a| ϕ) = 1. However, by theorem 8 (a| is the unique atomic effect such
that (a| ϕ) = 1. Hence, (a|A = (a|. Moreover, writing
P|F |
aF as aF = i=1 ai with (ai | ϕi ) = 1, ϕi ∈ F (lemma
P|F |
P|F |
47), we obtain (aF | A =
i=1 (ai | A =
i=1 (ai | =
(aF |. 
When applied to the case of projections, the above
lemma gives the following
Corollary 34 Let ϕ be a pure state in the face F ⊆
St1 (A) and let a ∈ Eff(A) be the atomic effect such that
(a| ϕ) = 1. Then, we have (a|ΠF = (a|. Moreover, if
aF is the effect associated to the face F , then we have
(aF | = (aF | ΠF .
The counterpart of corollary 34 is given as follows:
Lemma 52 Let ψ be a pure state in the face F ⊥ and let
b be the atomic effect such that (b| ψ) = 1. Then, we have
(b|ΠF = 0. Moreover, if a⊥
F is the effect associated to the
face F ⊥ , then we have a⊥
F ΠF = 0.
Proof. By lemma 16, the effect (b| ΠF is atomic. Hence,
(b| ΠF must be proportional to an atomic effect b′ with
||b′ || = 1, for some proportionality constant λ ∈ [0, 1], that
is (b| ΠF = λ (b′ |. We want to prove that λ is zero. By
contradiction, suppose that λ 6= 0. Let ψ ′ be the
 pure
state such that (b′ | ψ ′ ) = 1. Now, since ΠF ωF⊥ = 0,

<!-- page 31 -->
31
we have 0 = (b|ΠF |ωF⊥ ) = λ(b′ |ωF⊥ ), which implies
(b′ |ωF⊥ ) = 0. Hence, ψ ′ is perfectly distinguishable from
⊥
ωF⊥ , which in turn implies that ψ ′ belongs to F ⊥ = F .
′
′
We then have λ = (b| ΠF |ψ ) = (b| ψ ) = 0 (the last
equality follows from the fact that ψ and ψ ′ belong to
F ⊥ and F , respectively, and hence are perfectly distinguishable). This is in contradiction with the assumption
λ 6= 0, thus concluding the proof that (b| ΠF = 0. MoreP|F ⊥ |
⊥
over, writing a⊥
F as aF =
i=1 bi with (bi | ψi ) = 1,
P|F ⊥ |
Π
=
ψi ∈ F ⊥ , we obtain a⊥
F
F
i=1 (bi | ΠF = 0. 
Combining corollary 34 and lemma 52 we obtain an
important property of projections, expressed by the following:
Corollary 35 If ΠF is a projection on the face F , then
one has (eA | ΠF = (aF |.
Proof. The thesis follows from corollary 34 and lemma
52 and from the fact that aF + a⊥
F = e. 
In the following we will see that for every face F there
exists a unique projection. To prove that, let us start
from the existence:
Lemma 53 (Existence of projections) For
face F of St1 (A) there exists a projection ΠF .

every

Proof. By lemma 18, there exists a system B and an
atomic transformation A ∈ Transf(A, B) with (e|B A =
(aF |. Then, if ΨωF ∈ St(AC) is a purification of ωF , we
can define the state |Σ)BC := (A ⊗ IC )|ΨωF )AC . By
lemma 16, Σ is a pure state. Moreover, the pure states
Σ and ΨωF have the same marginal on system C: indeed, we have (eB | |Σ) = [(eB | A ] |ΨωF ) = (aF | |ΨωF )
and, by definition, aF =ωF eA , which by theorem 1 implies (aF | |ΨωF ) = (eA | |ΨωF ). If ϕ0 and ψ0 are two arbitrary pure states of A and B, respectively, the uniqueness
of purification stated by Postulate 1 implies that there
exists a reversible channel U ∈ GAB such that
(/.)ψ0

B

?>
89ΨωF

A

=

C

=

'!&ϕ0

A

?>
89Σ

B

ΠF

A

|ΦF ) :=

A

dA
(ΠF ⊗ IÃ )|Φ)
|F |

Proof. The state ΦF is pure by lemma 16. Let us
choose a maximal set of perfectly distinguishable pure
|F |
A
such that {ϕi }i=1 is maximal in F . Now,
states {ϕi }di=1
we have
dA
[ΠF ⊗ (eÃ |] |Φ)AÃ
|F |
dA
ΠF |χA ),
=
|F |

(eÃ | |ΦF )AÃ =

having used the relation (eÃ | |Φ)AÃ = |χA ) (corollary
16). We then obtain
dA
ΠF |χA )
|F |
d

=

A

(31)

is a purification of ωF .

C

?>
89ΨωF

=

Lemma 54 Let Φ ∈ St1 (AÃ) be a purification of the
invariant state χA , and let ΠF ∈ Transf(A) be a projection on the face F ⊆ St1 (A). Then, the pure state
ΦF ∈ St1 (AÃ) defined by

A

'!&ϕ0

A

A

B

B

(30)

A
1 X
ΠF |ϕi )
|F | i=1

|F |

=

U
A

1 X
|φi )
|F | i=1

= |ωF ),

C

Now, take the atomic effect b ∈ Eff(B) such that (b|ψ0 ) =
1, and define the transformation ΠF ∈ Transf(A) as
A

(eA | ΠF |ρ) = (eA ⊗ b| U (A ⊗ IA ) |ρ ⊗ ϕ0 )
≤ (eA ⊗ eB | U (A ⊗ IA ) |ρ ⊗ ϕ0 )
= (eA | A |ρ)
= (aF | ρ) .


This implies (eA | ΠF ωF⊥ = (aF | ωF⊥ 0, and, therefore,
ΠF =ωF⊥ 0. In conclusion, ΠF is the desired projection.

To prove the uniqueness of the projection ΠF we need
two auxiliary lemmas, given in the following.

(eÃ | |ΦF )AÃ =

B

U

and, therefore, ΠF =ωF IA . Moreover, the transformation ΠF is atomic, being the composition of atomic
transformations (lemma 16). Finally, we have ΠF =ωF⊥ 0:
indeed, by construction of ΠF we have

'!&ϕ0

A

A

B

B

U

b"%$#

A

Applying b on both sides of Eq. (30) we then obtain
(ΠF ⊗ IC )|ΨωF ) = |ΨωF ),

having used that χA =
definition of ΠF . 

PdA

i=1 ϕi /dA (theorem 9), and the

Lemma 55 Let ΠF ∈ Transf(A) be a projection. A
transformation C ∈ Transf(A) satisfies C =ωF IA if
and only if
C ΠF = ΠF .

(32)

<!-- page 32 -->
32
Proof. Let ΦF be the purification of ωF defined in
lemma 54. Since C =ωF IA , we have (C ⊗ I ) |ΦF ) =
|ΦF ). In other words, we have (C ΠF ⊗ I ) |Φ) =
(ΠF ⊗ I ) |Φ). Since Φ is dynamically faithful, this implies that C ΠF = ΠF . Conversely, Eq. (32) implies that
for σ ∈ FωF , C |σ) = C ΠF |σ) = ΠF |σ) = |σ), namely
C =ωF IA . 
Theorem 14 (Uniqueness of projections) The projection ΠF satisfying Definition 12 is unique.
Proof. Let ΠF and Π′F be two projections on the same
face F , and define the pure states ΦF and Φ′F as in lemma
54. Now, ΦF and Φ′F are both purifications of the same
state ω̃F ∈ Ã : indeed, one has
dA
[(eA | ΠF ] |Φ)AÃ
|F |
dA
(eF | |Φ)AÃ
=
|F |
dA
=
[(eA | Π′F ] |Φ)AÃ
|F |
= (eA | |Φ′F )AÃ ,

(eA | |ΦF )AÃ =

arbitrary

subsets

projection

ΠF

Proof. Consider a maximal set of perfectly distinguishA
such that {ϕi }i∈V is maximal
able pure states {ϕi }di=1
in F . In this way F is the face generated by V , and,
therefore ΠF = ΠV . The thesis follows by taking V = W
in lemma 56. 
Corollary 37 For every state ρ ∈ St1 (A) such that ρ 6∈
F ⊥ , the normalized state ρ′ defined by
|ρ′ ) =

ΠF |ρ)
(e| ΠF |ρ)

(33)

belongs to the face F .
Proof. By corollary 35, we have (e| ΠF = (aF |. Since
ρ 6∈ F ⊥ , we must have (e|ΠF |ρ) = (aF |ρ) > 0, and, therefore, the state ρ′ in Eq. (33) is well defined. Moreover,
using the definition of ρ′ we obtain
(aF | ΠF |ρ)
(e| ΠF |ρ)
= 1,

(aF | ρ′ ) =

having used the relation (eA | ΠF = (aF | = (eA | Π′F ,
which comes from corollary 34 and from the uniqueness of the effect aF (lemma 48). By the uniqueness
of purification, we have |Φ′F ) = (U ⊗ IÃ ) |ΦF ) for
some reversible transformation U ∈ GA . This implies
(Π′F ⊗ IÃ ) |Φ) = (U ΠF ⊗ IÃ ) |Φ), and, since Φ is dynamically faithful, Π′F = U ΠF . Since by Definition 12
we have Π′F =ωF IA and ΠF =ωF IA , we can conclude
that U =ωF IA . Finally, using lemma 55 with C = U
we obtain Π′F = U ΠF = ΠF . 
We now show a few simple properties of projections.
In the following, given a maximal set of perfectly disA
and any subset V ⊆
tinguishable pure states {ϕi }di=1
{1, . . . , dP
}
we
define
(with
a
slight
abuse of notation)
A
ωV :=
ϕ
/|V
|,
and
Π
as
the
projection on the
V
i∈V i
face FV := FωV . We will refer to FV as the face generated by V .
Lemma 56 For two
{1, . . . , dA } one has

Corollary 36 (Idempotence) Every
satisfies the identity Π2F = ΠF .

V, W

⊆

having used corollaries 34 and 35 for the last equality.
Finally, lemma 46 implies that ρ′ belongs to the face F .

Corollary 38 Let Π{ϕ} be the projection on the pure
state ϕ ∈ St1 (A) and a be the atomic effect such that
(a| ϕ) = 1. Then for every state ρ ∈ St1 (A) one has
Π{ϕ} |ρ) = p |ϕ) where p = (a| ρ).
Proof. Recall that, by corollary 35, we have (a| =
(e| Π{ϕ} . If (a| ρ) = 0 then clearly Π{ϕ} |ρ) = 0. Otherwise, the proof is a straightforward application of corollary 37. 
We conclude the present subsection with a result that
will be useful in the next subsection.
Lemma 57 An atomic transformation A ∈ Transf(A)
satisfies A =ωF IA if and only if

ΠV ΠW = ΠV ∩W .

ΠF A = ΠF .

(34)

In particular, if V ∩ W = ∅ one has ΠV ΠW = 0.
Proof. First of all, ΠV ΠW is atomic, being the product
of two atomic transformations. Moreover, since the face
FV ∩W is contained in the faces FV and FW , we have
ΠV ΠW |ρ) = ΠV |ρ) = |ρ) for every ρ ∈ FV ∩W . In other
words, ΠV ΠW =ωV ∩W IA . Moreover, if l 6∈ V ∩ W we
have ΠV ΠW |ϕl ) = 0. By lemma 49 and and by the
uniqueness of projections (theorem 14) we then obtain
that ΠV ΠW is the projection on the face generated by
V ∩ W. 

Proof. Suppose that A =ωF IA . Let Φ ∈ St1 (AÃ) be a
purification of the invariant state χA and define the two
pure states
dA
(ΠF ⊗ IÃ )|Φ)
|F |
dA
(ΠF A ⊗ IÃ )|Φ).
|Φ′F ) =:
|F |
|ΦF ) :=

<!-- page 33 -->
33
Then we have
(eA | |Φ′F ) = [(aF | A ] |Φ)
= (aF | |Φ)
= (eA | |ΦF ) ,

having used the condition (aF | A = (aF | (lemma 51).
Now, we proved that ΦF and Φ′F have the same marginal
on system Ã. By the uniqueness of purification, there
exists a reversible transformation V ∈ GA such that
|Φ′F ) = (V ⊗ IÃ ) |ΦF ). Since Φ is dynamically faithful, this implies ΠF A = V ΠF . Now, for every ρ in
F one has V |ρ) = V ΠF |ρ) = ΠF A |ρ) = |ρ), namely
V =ωF IA . Applying lemma 55 with C = V ΠF and
using the idempotence of projections we then obtain
ΠF A = V ΠF
= (V ΠF )ΠF
= ΠF ΠF
= ΠF .
Conversely, suppose that Eq. (34) is satisfied. Let ϕ ∈ F
be a pure state in F and a be the atomic effect such that
(a| ϕ) = 1. Then, we have
(a| A |ϕ) = (a|ΠF A |ϕ) = (a|ΠF |ϕ) = (a| ϕ) = 1,

having used the relation (a| ΠF = (a| (corollary 34).
Then, by theorem 7, A ϕ = ϕ. Since ϕ ∈ F is arbitrary,
this implies A =ωF IA . 
C.

Projection of a pure state on two orthogonal
faces

In Section X we proved a number of results concerning two-dimensional systems. Some properties of twodimensional systems will be extended to the case of
generic systems using the following lemma:

Finally, lemma 46 yields ϕ ∈ Fθ . 
A consequence of lemma 58 is the following
Lemma 59 Let ϕ ∈ St1 (A) be a pure state, a ∈ Eff(A)
be the unique atomic effect such that (a| ϕ) = 1, and F
be a face in St1 (A). If ρ is perfectly distinguishable from
ΠF |ϕ) and from Π⊥
F |ϕ) then ρ is perfectly distinguishable
from |ϕ). In particular, one has (a| ρ) = 0.
Proof. Since ρ is perfectly distinguishable from ΠF |ϕ)
and Π⊥
F |ϕ), it is also perfectly distinguishable from any
convex combination of them (corollary 33). Equivalently,
ρ is perfectly distinguishable from the face Fθ identified
by |θ) := ΠF |ϕ) + Π⊥
F |ϕ). In particular, it must be
perfectly distinguishable from ϕ, which belongs to Fθ by
virtue of lemma 58. If a is the atomic effect such that
(a| ϕ) = 1, then by lemma 36 we have (a| ρ) = 0. 
A technical result that will be useful in the following
is:
Lemma 60 Let ϕ ∈ St1 (A) be a pure state such
that ΠF |ϕ) 6= 0 and Π⊥
Define the
F |ϕ) 6= 0.
pure states |ϕ1 ) := ΠF |ϕ) / (e| ΠF |ϕ) and |ϕ2 ) :=
⊥
Π⊥
F |ϕ) / (e| ΠF |ϕ) and the mixed state |θ) := (ΠF +
⊥
ΠF ) |ϕ). Then, we have
ΠF ΠFθ = Π{ϕ1 }
Π⊥
F ΠFθ = Π{ϕ2 } .
|F |

Proof. Let {ψi }i=1 be a maximal set of perfectly distinguishable pure states in F , chosen in such a way
A
that ψ1 = ϕ1 , and let {ψi }di=|F
|+1 be a maximal set
of perfectly distinguishable pure states in F ⊥ , chosen in
such a way that ψ|F |+1 = ϕ2 . Defining the sets V :=
{1, . . . , |F |}, W := {|F |+1, . . . , dA }, and U := {1, |F |+1}
we then have ΠV = ΠF , ΠW = Π⊥
F and ΠU = ΠFθ . Using
lemma 56 we obtain
ΠF Πθ = ΠV ΠU
= ΠV ∩U
= Π{ψ1 }

Lemma 58 Consider a pure state ϕ ∈ St1 (A) and two
complementary projections ΠF and Π⊥
F . Then, ϕ belongs
to the face identified by the state |θ) := (ΠF + Π⊥
F ) |ϕ).
Proof. If ΠF |ϕ) = 0 (resp. Π⊥
F |ϕ) = 0), then there is
nothing to prove: this means that Π⊥
F |ϕ) = |ϕ) (resp.
ΠF |ϕ) = |ϕ)) and the thesis is trivially true. Suppose
now that ΠF |ϕ) 6= 0 and Π⊥
F |ϕ) 6= 0. Using the notation
,
we
can
define the two pure states
Π1 := ΠF , Π2 := Π⊥
F
|ϕi ) := Πi |ϕ)/ (e| Πi |ϕ), i = 1, 2, and the probabilities
pi = (e| Πi |ϕ). In this way we have Πi |ϕ) = pi |ϕi ) for
i = 1, 2 and θ = p1 ϕ1 + p2 ϕ2 . Taking the atomic effect
(ai | such that (ai | ϕi ) = 1 we have aFθ = a1 + a2 , where
aFθ is the effect associated to the face Fθ . Recalling that
(ai | Πi = (ai | for i = 1, 2 (corollary 34), we then conclude
the following
(aFθ |ϕ) = [(a1 | + (a2 |]|ϕ)
= (a1 |Π1 |ϕ) + (a2 |Π2 |ϕ)
X
pi (ai | ϕi ) = 1.
=
i=1,2

= Π{ϕ1 }
and
Π⊥
F Πθ = ΠW ΠU
= ΠW ∩U
= Π{ψ|F |+1 }
= Π{ϕ2 }

We conclude this subsection with an important observation about the group of reversible transformations that
act as the identity on two orthogonal faces F and F ⊥ . If
F is a face of St1 (A), let us define GF,F ⊥ as the group
of all reversible transformations U ∈ GA such that
U =ωF IA ,
Then we have the following

U =ωF⊥ IA .

<!-- page 34 -->
34
Theorem 15 For every face F ⊂ St1 (A) such that F 6=
{0} and F 6= St1 (A), the group GF,F ⊥ is topologically
equivalent to a circle.

[the third equality comes from lemma 60 with the substitutions F → F̃ , ϕ → Ψ, ϕ1 → ΦF , and ϕ2 → ΦF ⊥ ],
and, similarly,
⊥
(Π⊥
F ⊗ IÃ ) |Ψ) = ΠF̃ |Ψ)

Proof. Let U be a transformation in GF,F ⊥ , Φ ∈
St(AÃ) be a purification of the invariant state χA and
|ΦU ) := (U ⊗ IÃ ) |Φ) be the Choi state of U . Define
the orthogonal faces F̃ := FωF ⊗χÃ and F̃ ⊥ = FωF̃ ⊗χÃ ,
and the projections ΠF̃ := ΠF ⊗ IÃ and Π⊥
:= Π⊥
F ⊗ IÃ
F̃
(see lemma 50). Using lemma 57 we then obtain
ΠF̃ |ΦU ) = (ΠF ⊗ IÃ ) |ΦU )
= (ΠF U ⊗ IÃ ) |Φ)
= (ΠF ⊗ IÃ ) |Φ)
|F |
=
|ΦF ) ,
dA

Π |Ψ)
= Π⊥
F̃ Fθ

= Π{ΦF ⊥ } |Ψ)
=
Therefore, we have
(eA | |Ψ) = [(aF | + a⊥
F ] |Ψ)

= [(eA | ΠF ⊗ IÃ ] |Ψ) + [(eA | Π⊥
F ⊗ IÃ ] |Ψ)

|F |
|F ⊥ |
(eA | |Φ)F +
(eA | |ΦF ⊥ )
dA
dA
= [(eA | ΠF ⊗ IÃ ] |Φ) + [(eA | Π⊥
F ⊗ IÃ ] |Φ)
=

and, similarly,
⊥
|ΦU ) = (Π⊥
ΠF̃
F ⊗ IÃ ) |ΦU )
= (Π⊥
F U ⊗ IÃ ) |Φ)
⊥
= (ΠF ⊗ IÃ ) |Φ)
⊥

|F |
|ΦF ⊥ ) .
=
dA

This means that the projections of ΦU on the faces F̃
and F̃ ⊥ are independent of U . Also, it means that
ΦU belongs to the face Fθ identified by the state |θ) :=
|F |
|F ⊥ |
dA |ΦF ) + dA |ΦF ⊥ ) (lemma 58). Now, by the compression axiom, Fθ is isomorphic to the state space of a
qubit, say with ΦF and ΦF ⊥ indicating the north and
south poles of the Bloch sphere, respectively, and we
know that all the Choi states {ΦU }U ∈GF,F ⊥ are at the
same latitude (precisely, the latitude is the angle ζ given
by cos ζ = (|F | − |F ⊥ |)/dA ). This implies that the states
{ΦU }U ∈GF,F ⊥ are a subset of a circle Cζ in the Bloch
sphere describing the face Fθ . Precisely, the circle Cζ is
given by

|F |
Cζ := Ψ ∈ Fθ | Π{ΦF } |Ψ) =
|ΦF ) ,
dA
|F ⊥ |
|ΦF ⊥ )}
Π{ΦF ⊥ } |Ψ) =
dA
We now prove that in fact they are the whole circle. Let
Ψ be a state in Cζ . Since |Ψ) belongs to the face Fθ , we
obtain
(ΠF ⊗ IÃ ) |Ψ) = ΠF̃ |Ψ)
= ΠF̃ ΠFθ |Ψ)
= Π{ΦF } |Ψ)
|F |
=
|ΦF )
dA

|F ⊥ |
|ΦF ⊥ ) .
dA

= [(aF | + a⊥
F ] |Φ)
= (eA | |Φ)
= |χÃ ) .

Since Ψ and Φ are both purifications of the invariant
state χÃ , by the uniqueness of purification there must
be a reversible transformation U ∈ GA such that |Ψ) =
(U ⊗ IÃ ) |Φ). Finally, it is easy to check that ΠF U =
⊥
ΠF and Π⊥
F U = ΠF , which, by lemma 57 implies U =ωF
IA and U =ωF⊥ IA . This proves that the Choi states
{ΦU }U ∈GF,F ⊥ are the whole circle Cζ . Since the Choi
isomorphism is continuous in the operational norm (see
theorem 14 of [21]), the group GF,F ⊥ is topologically
equivalent to a circle. 

XII.

THE SUPERPOSITION PRINCIPLE

The validity of the superposition principle, proved for
two-dimensional systems using the geometry of the Bloch
sphere (corollary 31), can be now extended to arbitrary
systems thanks to lemma 58.
Theorem 16 (Superposition principle for general
A
systems) Let {ϕi }di=1
⊆ St1 (A) be a maximal set of
A
be the
perfectly distinguishable pure states and {ai }di=1
observation-test such that (ai | ϕj ) = δij . Then, for every
PdA
A
pi = 1 there
, pi ≥ 0, i=1
choice of probabilities {pi }di=1
exists at least one pure state ϕp ∈ St1 (A) such that
pi = (ai | ϕp )

∀i = 1, . . . , dA .

(35)

or, equivalently,
Π{ϕi } |ϕp ) = pi |ϕi )

∀i = 1, . . . , dA ,

where Π{ϕi } is the projection on ϕi .

(36)

<!-- page 35 -->
35
Proof. Let us first prove the equivalence between Eqs.
(35) and (36). From Eq. (36) we obtain Eq. (35) using
the relation (e| Π{i} = (ai |, which follows from corollary
35. Conversely, from Eq. (35) we obtain Eq. (36) using
corollary 38 . Now, we will prove Eq. (35) by induction.
The statement for N = 2 is proved by corollary 31. Assume that the statement holds for every system B of dimension dB = N and suppose that dA = N + 1. Let F be
PN
the face identified by ωF = 1/N i=1 ϕi and F ⊥ be the
orthogonal face, identified by the state ϕN +1 . Now there
are two cases: either pN +1 = 1 or pN +1 6= 1. If pN +1 = 1,
then there is nothing to prove: the desired state is ϕN +1 .
Then, suppose that pN +1 6= 1. Using the induction hypothesis and the compression axiom 3 we can find a state
ψq ∈ F such that (ai | ψq ) = qi , with qi = pi /(1 − pN +1 ),
i = 1, . . . , N . Let us then define a new maximal set
+1
of perfectly distinguishable pure states {ϕ′i }N
i=1 , with
′
′
ϕ1 = ψq and ϕN +1 = ϕN +1 . Note that one has
PN
ωF = 1/N i=1 ϕ′i , that is, F is the face generated by
the states {ϕ′i }N
i=1 . Now consider the two-dimensional
face F ′ identified by θ = 1/2(ϕ′1 + ϕ′N +1 ). By corollary 31 (superposition principle for qubits) we know that
there exists a pure state ϕ ∈ F ′ with (a′1 |ϕ) = 1 − pN +1
and (a′N +1 |ϕ) = pN +1 . Let us define V := {1, . . . , N }
and W := {1, N + 1}. Then, we have ΠF = ΠV and
ΠF ′ = ΠW , and by lemma 56,
ΠF |ϕ) = ΠF ΠF ′ |ϕ)
= ΠV ∩W |ϕ)
= Π{ϕ′1 } |ϕ)
= Π{ψq } |ϕ)

= (1 − pN +1 )|ψq ),
having used corollary 38 for the last equality. Finally, for
i = 1, . . . , N we have
(ai |ϕ) = (ai |ΠF |ϕ)
= (1 − pN +1 ) (ai | ψq )
= (1 − pN +1 )qi
= pi .
On the other hand we have (aN +1 |ϕ) = (a′N +1 |ϕ) =
pN +1 . 
A.

Completeness for purification

Using the superposition principle and the spectral decomposition of theorem 10 we can now show that every state of system A has a purification in AB provided
dB ≥ dA :

Lemma 61 For every state ρ ∈ St1 (A) and for every
system B with dB ≥ dA there exists a purification of ρ in
St1 (AB).

Proof. Take the spectral decomposition of ρ, given
PdA
by ρ =
i=1 pi ϕi , where {pi } are probabilities and

A
⊂ St1 (A) is a maximal set of perfectly distin{ϕi }di=1
B
be a maximal set
guishable pure states. Let {ψi }di=1
A
of perfectly distinguishable pure states and {ai }di=1
⊂
dB
Eff(A) (resp. {bi }i=1 ⊂ Eff(B)) be the test such that
(ai | ϕj ) = δij (resp. (bi | ψj ) = δij ). Clearly, {ϕi ⊗ ψj } is
a maximal set of perfectly distinguishable pure states for
AB. Then, by the superposition principle (theorem 16)
there exists a pure state Ψρ such that (ai ⊗ bj | Ψρ ) =
pi δij . Equivalently, we have (bi |B |Ψρ )AB = pi |ϕi )A
for every i = 1, . . . , dA and (bi |B |Ψρ )AB = 0 for i >
dA . Summing over i we then obtain (e|B |Ψρ )AB =
PdA
PdB
i=1 pi |ϕi )A = |ρ)A . 
i=1 (bi |B |Ψρ )AB =
In the terminology of Ref. [21], lemma 61 states that
a system B with dB ≥ dA is complete for the purification
of system A.
As a consequence of lemma 61 we have the following:

Corollary 39 Every system B with dB = dA is operationally equivalent to the conjugate system Ã.
Proof. By corollary 61, the invariant state χA ∈ St1 (A)
has a purification Ψ in St1 (AB). By corollary 18, the
marginal of Ψ on B is the invariant state χB . By definition, this means that B is a conjugate system of A.
Since the conjugate system Ã is unique up to operational
equivalence (corollary 16), this implies the thesis. 
B.

Equivalence of systems with equal dimension

We are now in position to prove that two systems A
and B with the same dimension are operationally equivalent, namely that there is a reversible transformation
from A to B. In other words, we prove that the informational dimension classifies the systems of our theory
up to operational equivalence. The fact that this property is derived from the principles, rather than being
assumed from the start, is one of the important differences of our work with respect to Refs. [16–18]. Another difference is that here the equivalence of systems
with the same dimension is proved after the derivation of
the qubit, whereas in Refs. [16–18] the derivation of the
qubit requires the equivalence of systems with the same
dimension.
Corollary 40 (Operational equivalence of systems
with equal dimension) Every two systems A an B with
dA = dB are operationally equivalent.
Proof. By corollary 39, A and B are both operationally
equivalent to the conjugate system Ã. Hence, they are
operationally equivalent to each other. 
C.

Reversible operations of perfectly
distinguishable pure states

An important consequence of the superposition principle is the possibility of transforming an arbitrary max-

<!-- page 36 -->
36
imal set of perfectly distinguishable pure states into another via a reversible transformation:
Corollary 41 Let A and B be two systems with dA =
dB =: d and let {ϕi }di=1 (resp. {ψi }di=1 ) be a maximal set of perfectly distinguishable pure states in A
(resp. B). Then, there exists a reversible transformation U ∈ Transf(A, B) such that U |ϕi ) = |ψi ).
Proof. Let Φ ∈ St(AÃ) be a purification of the invariant
state χA . Although we know that A and Ã are operationally equivalent (corollary 39) we use the notation A
and Ã to distinguish between the two subsystems of AÃ.
Define the pure state ϕ̃i via the relation (ai |A |Φ)AÃ =
1
d
d |ϕ̃i )Ã , where {ai }i=1 is the observation-test such that
(ai | ϕi ) = δij . Let {ãi }di=1 be the observation-test such
that (ãi | ϕ̃j ) = δij . Then, by lemma 30 we have
(ãi |Ã |Φ)AÃ =

1
|ϕi )A .
d

(37)

On the other hand, if {b̃i }di=1 is the observation-test such
that (b̃i |ψ̃j ) = δij , then using the superposition principle
(theorem 16) we can construct a state Ψ ∈ St1 (BÃ) such
that (bi ⊗ ãj | Ψ) = δij /d, or, equivalently,
(ãi |Ã |Ψ)BÃ =

1
|ψi )B .
d

(38)

Now, Φ and Ψ have the same marginal on system Ã:
they are both purifications of the invariant state χÃ .
Moreover, A and B are operationally equivalent because
they have the same dimension (corollary 40). Hence, by
the uniqueness of purification, there must be a reversible
transformation U ∈ Transf(A, B) such that
|Ψ)BÃ = (U ⊗ IÃ ) |Φ)AÃ .

(39)

Combining Eqs. (37), (38), (39) we finally obtain
1
U |ϕi )A = [U ⊗ (ãi |Ã ] |Φ)BÃ
d
= (ãi |Ã |Ψ)BÃ
1
= |ψi )B ,
d
that is, U |ϕi ) = |ψi ) for every i = 1, . . . , d. 
XIII.

DERIVATION OF THE DENSITY
MATRIX FORMALISM

The goal of this section is to show that our set of axioms implies that
• the set of states for a system A of dimension dA
is the set of density matrices on the Hilbert space
Cd A
• the set of effects is the set of positive matrices
bounded by the identity

• the pairing between a state and an effect is given
by the trace of the product of the corresponding
matrices.
Using the result of theorem 3, we will then obtain that all
the physical transformations in our theory are exactly the
physical transformations allowed in quantum mechanics.
This will conclude our derivation of quantum theory.
A.

The basis

In order to specify the correspondence between states
and matrices we choose a particular basis for the vector
space StR (A). For this purpose, we adopt the choice of
basis used in Ref. [16]. The basis is constructed as follows: Let us first choose a maximal set of dA perfectly
A
distinguishable states {ϕm }dm=1
, and declare that they
are the first dA basis vectors. Then, for every m < n
the face Fmn generated by {ϕm , ϕn } defines a “twodimensional subsystem”: precisely, the face Fmn := Fωmn
n
can be ideally encoded in a twowith ωmn := ϕm +ϕ
2
dimensional system. Now, the convex set of states of a
two-dimensional system is the Bloch sphere, and we can
choose the z-axis to be the line joining the two states
{ϕm , ϕn }, e.g. with the positive direction of the z-axis
being the direction from ϕm to ϕn . Once the direction of
the z-axis has been specified, we can choose the x and y
axes. Note that any couple of orthogonal directions in the
plane orthogonal to z-axis is a valid choice for the x- and
y-axes (here we do not restrict ourselves to the choice of
a right-handed coordinate system). At the moment there
is no relation among the different choices of axes made
for different values of m and n. However, to prove that
the states are represented by positive matrices, later we
will have to find a suitable way of connecting all these
choices of axes.
mn
mn
mn
Let ϕmn
x,+ , ϕx,− ∈ Fmn (ϕy,+ , ϕy,− ∈ Fmn ) be the two
perfectly distinguishable states in the direction of the xaxis (y-axis) and define
mn
σkmn := ϕmn
k,+ − ϕk,−

k = x, y.

(40)

An immediate observation is the following:
Lemma 62 The four vectors {ϕm , ϕn , σxmn , σymn } ⊆
StR (A) are linearly independent. Moreover, denoting by
al ∈ Eff(A) the atomic effect such that (al | ϕl ) = 1 we
have (al | σkmn ) = 0 for every l, m, n ∈ {1, . . . , dA } and
for every k = x, y.
Proof. Linear independence is evident from the geometry of the Bloch sphere. Moreover, for l 6∈ {m, n} the
states ϕmn
k,± are perfectly distinguishable from ϕl , and,
therefore (al | σkmn ) = 0. If l ∈ {m, n}, since the states
ϕmn
equator of the Bloch sphere,
k,± , k = x, y lie on the

mn
we know that (al | ϕk,± = 1/2 for k = x, y. Hence,

(al | σkmn ) = 12 − 21 0. 

<!-- page 37 -->
37
We now show that the collection of all vectors obtained
in this way is a basis for StR (A). To this purpose we use
the following

and the vector σymn to the matrix
h
i
Sσymn
= iλ (δrm δsn − δrn δsm ) .
rs

Lemma 63 Let V ⊂ {1, . . . , dA }, and consider the projection ΠV . Then, for m ∈ V and n 6∈ V , one has
ΠV |σkmn ) = 0 for k = x, y.
Proof. Using lemma 56 and corollary 38 we obtain
mn
ΠV |ϕmn
k,± ) = ΠV Π{m,n} |ϕk,± )

= Π{m} |ϕmn
k,± )

= |ϕm ) (am |ϕmn
k,± )

Since the face Fmn is isomorphic to the Bloch sphere and
the state since ϕmn
k± , k = x, y lie on the equator of the
1
Bloch sphere, we know that (am |ϕmn
k± ) = 2 . This implies

mn
ΠV |σkmn ) = ΠV |ϕmn
k,+ ) − |ϕk,− )


1 1
= 0.
−
= |ϕm )
2 2

Lemma 64 The
vectors
{σkmn }n>m=1,...,dA k=x,y form a

A
{ϕn }dm=1
∪
basis for StR (A).

where λ can take the values +1 or −1. The freedom in
the choice of λ will be useful in subsection XIII C, where
we will introduce the representation of composite systems
of two qubits. However, this choice of sign plays no role
in the present subsection, and for simplicity we will take
the positive sign.
Recall that in principle any orthogonal direction in the
plane orthogonal to the z-axis can be chosen to be the xaxis. In general, the other possible choices for the x-axis
will lead to matrices of the form
i
h
mn
= δrm δsn eiθ + δrn δsm e−iθ
θ ∈ [0, 2π),
Sσx,θ
rs

(44)
and the corresponding choice for the y-axis will lead to a
matrices of the form
i
h

mn
θ ∈ [0, 2π),
= iλ δrm δsn eiθ − δrn δsm e−iθ
Sσy,θ
rs

(45)

A
Since the vectors {ϕm }dm=1
∪ {σkmn }n>m=1,...,dA ; k=x,y
are a basis for the real vector space StR (A), we can ex-

pand any state ρ ∈ St(A) on them:
X
X
mn
|ρ) =
ρm |ϕm ) +
ρmn
k |σk )
m

Proof. Since the number of vectors is exactly d2A , to
prove that they form a basis it is enough to show that
they are linearly independent. Suppose that there exists
a vector of coefficients {cm } ∪ {cmn
k } such that
X
X
mn
cm ϕm +
cmn
= 0.
k σk
m

n>m, k=x,y

Applying the projection Π{m,n} on both sides and using
lemma 63 we obtain
mn
cm |ϕm ) + cn |ϕn ) + cxmn |σxmn ) + cmn
y |σy ) = 0.

However, we know that the vectors {ϕm , ϕn , σxmn , σymn }
are linearly independent. Consequently, cm = cn =
ckmn = 0 for all m, n, k. 
B.

The matrices

Since the state space St(A) for system A spans a real
vector space of dimension DA = d2A , we can decide to
A
represent the vectors {ϕm }dm=1
∪{σkmn }n>m=1,...,dA k=x,y
as Hermitian dA × dA matrices. Precisely, we associate
the vector ϕm to the matrix Sϕm defined by
[Sϕm ]rs = δrm δsm ,
the vector σxmn to the matrix


Sσxmn rs = δrm δsn + δrn δsm

(41)

(42)

(43)

(46)

n>m, k=x,y

A
and
the
expansion
coefficients
{ρm }dm=1
∪
mn
{ρk }n>m=1,...,dA ; k=x,y are all real.
Hence, each
state ρ is in one-to-one correspondence with a Hermitian
matrix, given by
X
X
mn .
Sρ =
ρm S ϕ m +
ρmn
(47)
k Sσk

m

n>m, k=x,y

Since effects are linear functionals on states, they are
also represented by Hermitian matrices. We will indicate
with Ea the Hermitian matrix associated to the effect
a ∈ Eff(A). The matrix Ea is uniquely defined by the
relation:
(a| ρ) = Tr[Ea Sρ ].
In the rest of the section we show that the set of matrices {Sρ | ρ ∈ St1 (A)} is the whole set of positive Hermitian matrices with unit trace and that the set of matrices
{Ea | a ∈ Eff(A)} is the set of positive Hermitian matrices bounded by the identity.
Let us start from some simple facts:
Lemma 65 The invariant state χA has matrix represenI
tation SχA = ddAA , where IdA is the identity matrix in
dimension dA .
P
Proof. Obvious from the expression χA = d1 m ϕm and
A
from the matrix representation of the states {ϕm }dm=1
in
Eq. (41). 

<!-- page 38 -->
38
Lemma 66 Let am ∈ Eff(A) be the atomic effect such
that (am | ϕm ) = 1. Then, the effect am has matrix representation Eam such that Eam = Sϕm .
Proof. Let ρ ∈ St1 (A) be an arbitrary state. Expanding
ρ as in Eq. (46) and using lemma 62 we obtain (am | ρ) =
ρm . On the other hand, by Eq. (47) we have that ρm is
the m-th diagonal element of the matrix Sρ : by definition
of Sϕm [eq. (41)], this implies ρm = Tr[Sϕm Sρ ]. Now, by
construction we have Tr[Eam Sρ ] = (am | ρ) = rhom =
Tr[Sϕm Sρ ] for every ρ ∈ St1 (A). Hence, Eam = Sϕm . 
Lemma 67 The deterministic effect e ∈ Eff(A) has matrix representation Ee = IdA .
Proof. Obvious from the expression e =
bined with lemma 66 and Eq. (41). 

P

m am , com-

Corollary 42 For every state ρ ∈ St1 (A) one has
Tr[Sρ ] = 1.
Proof. Tr[Sρ ] = Tr[Ee Sρ ] = (e| ρ) = 1. 
Theorem 17 The matrix elements of Sϕ for a pure state
P A
√
ϕ ∈ St1 (A) are (Sϕ )mn = pm pn eiθmn , with dm=1
pm =
1, θmn ∈ [0, 2π), θmn = 0 and θmn = −θnm .
Proof. First of all, the diagonal elements of Sϕ are given
by [Sϕ ]mm = (am | ϕ) [cf. Eqs. (46) and (47)]. Denoting
PdA
pm =
the m-th element by pm , we clearly have m=1
(e| ϕ) = 1. Now, the projection Π{m,n} |ϕ) is a state
in the face Fmn , and, by our choice of representation,
the corresponding matrix SΠ{m,n} |ϕ) is proportional to a
pure qubit state (non-negative rank-one matrix). On the
other hand, it is easy to see from Eqs. (46) and (47)
that SΠ{m,n} |ϕ) is the matrix with the same elements as
Sϕ in the block corresponding to the qubit (m, n) and
0 elsewhere. In order to be positive and rank-one the
corresponding 2×2 sub-matrix must have the off-diagonal
√
elements (Sϕ )mn = pm pn eiθmn , for some θmn ∈ [0, 2π)
with θnm = −θmn . Repeating the same argument for all
choices of indices m, n, the thesis follows. 
Theorem 18 For a pure state ϕ ∈ St1 (A), the corresponding atomic effect aϕ such that (aϕ |ϕ) = 1 has a matrix representation Eϕ with the property that Eϕ = Sϕ .

matrices SΠ{m,n} |ϕ) and E(a|Π{m,n} are positive (also, recall that all matrix elements outside the (m, n) block are
(mn)
zero). Let ϕ⊥
be the pure state in the face Fmn that
is perfectly distinguishable from Π{m,n} |ϕ). Note that,
(mn)

since ϕ⊥
belongs to the face Fmn , it is also perfectly
(mn)
distinguishable from Π{1,...,dA }\{m,n} |ϕ). Hence, ϕ⊥
is perfectly distinguishable from ϕ and, in particular,
(mn)
(a|ϕ⊥ ) = 0 (lemma 59). This implies the relation


(mn)
Tr E(a|Π{m,n} S ϕ(mn)  = (a| Π{m,n} |ϕ⊥ )
⊥

(mn)

= (a|ϕ⊥

Now, since the matrix E(a|Π{m,n} is positive, the above relation implies E(a|Π{m,n} = cmn SΠ{m,n}|ϕ) , where cmn ≥
0. Finally, repeating the argument for all possible values
of (m, n), we obtain that cmn = c for every m, n, that
is, Ea = cSϕ . Taking the trace on both sides we obtain
Tr[Ea ] = c. To prove that c = 1, we use the relation
Tr[Ea ]/dA = (a| χA ) = 1/dA . 
We conclude with a simple corollary that will be used
in the next subsection:
Corollary 43 Let ϕ ∈ St1 (A) be a pure state and let
{γi }ri=1 ⊂ St1 (A) be a set of pure states. If the state ϕ
can be written as
X
xi |γi )
|ϕ) =
i

for some real coefficients {xi }ri=1 , then the atomic effect
a such that (a| ϕ) = 1 is given by
X
xi (ci | ,
(a| =
i

where ci is the atomic effect such that (ci | γi ) = 1.
Proof. For every ρ ∈ St(A) by theorem 18 one has
X
xi Tr[Sγi Sρ ]
(a| ρ) = Tr[Ea Sρ ] = Tr[Sϕ Sρ ] =
=

X

xi Tr[Eci Sρ ] =

i

X
i

i

xi (ci | ρ) ,

thus implying the thesis. 
C.

Proof. We already know that the statement holds for
dA = 2, where we proved the Bloch sphere representation, equivalent to the fact that states and effects are
represented as 2 × 2 positive complex matrices, with the
set of pure states identified with the set of all rank-one
projectors. Let us now consider a generic system A. For
every m < n, the face Fmn generated by {ϕm , ϕn } can
be encoded in a two-dimensional system. Therefore, the

) = 0.

Choice of axes for a two-qubit system

If A and B are two systems with dA = dB = 2, then
we can use two different types of matrix representations
for the states of the composite systemAB:
The first type of representation is the representation
Sϕ introduced through lemma 64: here we will refer to
it as the standard representation. Note that there are
many different representations of this type because for

<!-- page 39 -->
39
every pair (m, n) there is freedom in choice of the x- and
y-axis [cf. Eqs. (44 ) and (45)]
The second type of representation is the tensor product
representation Tϕ , defined by the tensor product of matrices representing
states of systems A and B: for a state
P
|ρ) = i,j ρij |αi ) |βj ), with αi ∈ St(A), βj ∈ St(B), we
have
X
(48)
ρij SαAi ⊗ SβBj ,
Tρ :=
i,j

where S A (resp. S B ) is the matrix representation for system A (resp. B). Here the freedom is in the choice of
the axes for the Bloch spheres of qubits A and B. Since
A and B are operationally equivalent, we will indicate
the elements of the bases for StR (A) and StR (B) with the
same letters: {ϕm }2m=1 for the two perfectly distinguishable pure states and {σk }k=x,y for the remaining basis
vectors.
We now show a few properties of the tensor representation. Let FA denote the matrix corresponding to the
effect A ∈ Eff(AB) in the tensor representation, that is,
the matrix defined by
(A| ρ) := Tr[FA Tρ ]

∀ρ ∈ St(AB).

(49)

It is easy to show that the matrix representation for effects must satisfy the analogue of Eq. (48):
Lemma 68 Let
P A ∈ Eff(AB) be a bipartite effect, written as (A| = i,j Aij (ai | (bj |. Then one has
FA =

X
i,j

Aij EaAi ⊗ EbBj ,

where EaAi (resp. EbBj ) is the matrix representing the
single-qubit effect ai (resp. bj ) in the standard representation for qubit A (resp. B).
Proof. For every bipartite state |ρ) =
one has

P

k,l ρkl |αk ) |βl )

Tr[FA Tρ ] = (A| ρ)
X
=
Aij ρkl (ai | αk ) (bj | βl )
i,j,k,l

=

X

Aij ρkl Tr[EaAi SαAk ]Tr[EBbj SβBl ]

i,j,k,l

=

X

i,j,k,l

=

X
i,j

Aij ρkl Tr[(EaAi ⊗ EbBj )Tαk ⊗βl ]

Aij Tr[(EaAi ⊗ EbBj )Tρ ]

which implies the thesis. 
Corollary 44 Let Ψ ∈ St1 (AB) be a pure state and let
A ∈ Eff(AB) be the atomic effect such that (A| Ψ) = 1.
Then one has FA = TΨ .

Proof. Let {ai }4i=1 (resp. {βj }4j=1 ) be a set of pure
states that
P span StR (A) (resp. StR (B)) and expand Ψ as
|Ψ) = i,j cij |αi ) |βj ). Then, corollary 43 yields (A| =
P
i,j cij (ai | (bj | where ai and bj are the atomic effects
such that (ai | αi ) = (bj | βj ) = 1. Therefore, we have
X
X
cij SαAi ⊗ SβBj = TΨ .
cij EaAi ⊗ EbBj =
FA =
i,j

i,j


Corollary 45 For every bipartite state ρ ∈ St1 (AB),
dA = dB = 2 one has Tr[Tρ ] = 1.
Proof. For each qubit we have
!
1 0
, Ea2 =
Ea1 =
0 0

!
0 0
.
0 1

(50)

Hence, EeAA = EeBB = I, where I is the 2 × 2 identity
matrix. By lemma 68, we then have FeA ⊗eB = I ⊗ I and,
therefore Tr[Tρ ] = Tr[FeA ⊗eB Tρ ] = (eA ⊗ eB | ρ) = 1. 
Finally, an immediate consequence of local distinguishability is the following:
Lemma 69 Suppose that U ∈ GA and V ∈ GB are
two reversible transformations for qubits A and B, respectively, and that U, V ∈ SU(2) are such that
A
A †
SU
ρ = U Sρ U

SVB σ = V SσB V †

∀ρ ∈ St1 (A)

∀σ ∈ St1 (B).

Then, we have T(U ⊗V )τ = (U ⊗ V )Tτ (U † ⊗ V † ) for every
τ ∈ St1 (AB).
Proof.
P The thesis follows by linearity expanding τ as
τ = 4i,j=1 τij αi ⊗ βj , where {αi }4i=1 and {βj }4j=1 are
bases for the StR (A) and StR (B). 
The rest of this subsection is aimed at showing that,
with a suitable choice of matrix representation for system
B, the standard representation coincides with the tensor
representation, that is, Sρ = Tρ for every ρ ∈ St(AB).
This technical result is important because some properties used in our derivation are easily proved in the
standard representation, while the property expressed by
lemma 69 is easily proved in the tensor representation:
it is then essential to show that we can construct a representation that enjoys both properties.
The four states {ϕm ⊗ ϕn }2m,n=1 are clearly a maximal
set of perfectly distinguishable pure states in AB. In the
following we will construct the standard representation
starting from this set.
Lemma 70 For a composite system AB with dA = dB =
2 one can choose the standard representation in such a
way that the following equalities hold
Sϕm ⊗ϕn = Tϕm ⊗ϕn ,
Sϕm ⊗σk = Tϕm ⊗σk ,
Sσk ⊗ϕm = Tσk ⊗ϕm ,

k = x, y,
k = x, y.

(51)
(52)
(53)

<!-- page 40 -->
40
Proof. Let us choose single-qubit representations S A
and S B that satisfy Eqs. (41), (42), and (43). On the
other hand, choosing tho states {ϕn ⊗ ϕn } in lexicographic order as the four distinguishable states for the
standard representation, we have
[Sϕ1 ⊗ϕ1 ]rs = δ1r δ1s
[Sϕ2 ⊗ϕ1 ]rs = δ3r δ3s

[Sϕ1 ⊗ϕ2 ]rs = δ2r δ2s
[Sϕ2 ⊗ϕ2 ]rs = δ4r δ4s .

With this choice, we get Sϕm ⊗ϕn = SϕAm ⊗SϕBn = Tϕm ⊗ϕn
for every m, n = 1, 2. This proves Eq. (51). Let us now
prove Eqs. (52) and (53). Consider the two-dimensional
face F11,12 , generated by the states ϕ1 ⊗ ϕ1 and ϕ1 ⊗ ϕ2 .
This face is the face identified by the state ω11,12 :=
ϕ1 ⊗ χB , and we have F11,12 ≃ {ϕ1 } ⊗ St1 (B). Therefore
we can choose the vectors σk11,12 , k = x, y to satisfy the
relation σk11,12 := ϕ1 ⊗σk , k = x, y. Now, in the standard
representation we have

where I is the 2 × 2 identity matrix. The most general
form for TΦ is then the following

]rs = δr1 δs2 + δr2 δs1
[Sσ11,12
x
]rs = iλ(δr1 δs2 − δr2 δs1 )
[Sσ11,12
y
[cf. Eqs. (42) and (43)]. This implies Sσ11,12 = SϕA11 ⊗
k
SσBk = Tϕ11 ⊗σk , for k = x, y. Repeating the same argument for the face F22,21 , F11,21 , and F21,22 we obtain the
proof of Eqs. (52) and (53). 
In order to prove that, with a suitable choice of axes,
the standard representation coincides with the tensor
representation—i.e. Sρ = Tρ for every ρ ∈ St(AB)—it remains to find a choice of axes such that Sσk ⊗σl = Tσk ⊗σl ,
k = x, y. This will be proved in the following.
Lemma 71 Let Φ ∈ St1 (AB) be a pure state such that
(a1 ⊗ a1 | Φ) = (a2 ⊗ a2 | Φ) = /1 2 [such a state exists due
to the superposition principle]. With a suitable choice of
the matrix representation S B , the state Φ is represented
by the matrix


1 0 0 1

1
0 0 0 0
(54)
TΦ = 
.
2 0 0 0 0
1 0 0 1
Moreover, one has

1
Φ = χA ⊗ χB + (σx ⊗ σx − σy ⊗ σy + σz ⊗ σz ). (55)
4
Proof.
Let us start with the proof of Eq. (54). For every
reversible transformation U ∈ GA , let U ∗ ∈ GB be the
conjugate of U , defined with respect to the state Φ. Since
all 2×2 unitary (non-trivial) representations of SU(2) are
unitarily equivalent, by a suitable choice of the standard
representation SρB for system B, one has
B
∗ B T
SU
∗ ρ = U Sρ U ,

where U ∗ and U T are the complex conjugate and the
A
transpose of the matrix U ∈ SU(2) such that SU
ρ =
A †
U Sρ U .
Due to Eq. (56) and to lemma 69, the isotropic state
Φ must satisfy the condition (U ⊗ U ∗ )TΦ (U † ⊗ U T ) =
TΦ , ∀U ∈ SU(2). Now, the unitary representation {U ⊗
U ∗ } has two irreducible subspaces and the projectors on
them are given by the matrices


1 0 0 1

1
0 0 0 0
P0 = 

2 0 0 0 0
1 0 0 1


1 0 0 −1

1
0 2 0 0
P1 = 
 = I ⊗ I − P0 ,
2 0 0 2 0 
−1 0 0 1

TΦ = x0 P0 + x1 P1
= (x0 − x1 )P0 + x1 I ⊗ I


α+β 0 0
β


α 0
0 
 0
=
,
 0
0 α
0 
β
0 0 α+β

having defined α := x1 and β := (x0 − x1 )/2.
Now, by construction the state Φ satisfies the condition
(am |A |Φ)AB =

m = 1, 2.

By definition of the tensor representation, the conditional
states (am |A |Φ)AB are described by the diagonal blocks
of the matrix TΦ :
!
!
α
+
β
0
α
0
B
B
S(a
=
S(a
=
.
1 ||Φ)AB
2 ||Φ)AB
0
α
0 α+β
(57)
Since the states ϕ1 and ϕ2 are pure, the above matrices
must be be rank-one. Moreover, their trace must be equal
to (am ⊗ eB | Φ) = 1/2 (eB | ϕm ) = 21 , m = 1, 2. Then we
have two possibilities. Either i) α = 0 and β = 12 or ii)
α = −β = 21 . In the case i), Eq. 54 holds. In the case ii),
to prove Eq. (54) we need to change our choice of matrix
representation for the qubit B. Precisely, we make the
following change:
SσBx 7→ SeσBx = −SσBx
S B 7→ SeB = −S B
σy

(56)

1
|ϕm )B
2

σy

σy

SσBz 7→ SeσBz = −SσBz ,

(58)

<!-- page 41 -->
41
where σz := ϕ1 − ϕ2 . Note that the inversion of the
axes, sending σk to −σk for every k = x, y, z is not an
allowed physical transformation, but this is not a problem
here, because Eq. (58) is just a new choice of matrix
representation, in which the set of states of system B is
still represented by the Bloch sphere.
More concisely, the change of matrix representation
B
S 7→ SeB can be expressed as
!
 B T †
0
−1
B
B
Y :=
.
Sρ 7→ Seρ := Y Sρ Y
1 0
Note that in the new representation SeB the physiB
cal transformation U ∗ is still represented as SeU
ρ =
∗ eB T
U Sρ U : indeed we have
 B T †
B
SeU
SU ∗ ρ Y
∗ρ = Y

= Y (U ∗ SρB U T )T Y †
 T
= Y (U SρB U † )Y †
 T
= (Y U Y † )(Y SρB Y † )(Y U † Y † )
 T
= U ∗ (Y SρB Y † )U T
= U ∗ SeρB U T ,

†

Φ ∈ St1 (AB) is represented by the matrix


1 0 0 eiθ

1
 0 0 0 0
SΦ = 

2 0 0 0 0
e−iθ 0 0 1

(59)

Proof. The thesis follows from theorem 17 and lemma
70. 
We now define the reversible transformations Ux,π and
Uz, π2 as follows
!
0 1
SUx,π ρ = XSρ X,
X :=
1 0
!
(60)
π
π
1
0
−i 4 Z
i4Z
Sρ e
,
Z :=
.
SUz, π ρ = e
2
0 −1
Also, we define the states Ψ, Φz, π2 , and Ψz, π2 as
|Ψ) := (Ux,π ⊗ I ) |Φ)

Φz, π2 := (Uz, π2 ⊗ I ) |Φ)

Ψz, π2 := (Uz, π2 ⊗ I ) |Ψ)

†

∗

having used the relations Y Y = I and Y U Y = U
for every U ∈ SU(2). Clearly, the change of standard
representation S → Se for the qubit B induces a change
of tensor representation T → Te, where Te is the tensor
representation defined by Teρ⊗σ := SρA ⊗ SeσB . With this
change of representation, we have


1 0 0 1

1
0 0 0 0
TeΦ = 
.
2 0 0 0 0
1 0 0 1
This concludes the proof of Eq. (54).
Let us now prove Eq. (55). Using the fact that by
definition Tρ⊗τ = (SρA ⊗ SτB ) one can directly verify the
relation
1
TΦ = SχA ⊗ SχB + (SσAx ⊗ SσBx − SσAy ⊗ SσBy + SσAz ⊗ SσBz ).
4
This is precisely the matrix version of Eq. (55). 
Note that the choice of S B needed in Eq. (54) is compatible with the choice of S B needed in lemma 70: indeed, to prove compatibility we only have to show that
the representation SB used in Eq. (54) has the property
[SϕBm ]rs = δmr δms , m = 1, 2. This property is automatically guaranteed by the relation (am |A |Φ)AB = 1/2 |ϕm ),
m = 1, 2 and by Eq. (57) with α = 0 and β = 1/2.
Corollary 46 In the standard representation the state

Lemma 72 The states Ψ, Φz, π2 , and Ψz, π2 have the following tensor representation




0 0 0 0
1 0 0 −i


1
1
0 1 1 0
0 0 0 0 
TΨ = 


 , TΦz, π =
2
2 0 1 1 0
2 0 0 0 0 
i 0 0 1
0 0 0 0


0 0 0 0

1
0 1 −i 0
(61)
TΨz, π = 
.
2
2 0 i 1 0
0 0 0 0

Moreover, one has

1
Ψ =χA ⊗ χB + (σx ⊗ σx + σy ⊗ σy − σz ⊗ σz )
4
1
Φz, π2 =χA ⊗ χB + (σy ⊗ σx + σx ⊗ σy + σz ⊗ σz )
4
1
Ψz, π2 =χA ⊗ χB + (σy ⊗ σx − σx ⊗ σy − σz ⊗ σz )
4
(62)
Proof. Eq. (61) is obtained from Eq. (54) by explicit
calculation using lemma 69 and Eq. (60). Then, the
validity of Eq. (62) is easily obtained from Eq. (55)
using the relations
Ux,π |σx ) = |σx )
Ux,π |σy ) = − |σy )
Ux,π |σz ) = − |σz )

<!-- page 42 -->
42
same arguments can be used for Ψz, π2 : The diagonal elements of SΨz, π are obtained from the re 2

lations (a1 ⊗ a1 | Ψz, π2
= (a2 ⊗ a2 | Ψz, π2
= 0 and


(a1 ⊗ a2 | Ψz, π2 = (a2 ⊗ a1 | Ψz, π2 = 1/2, which follow
from Eq. (62). This implies that the matrix SΨz, π has
2
the form

and
Uz,π/2 |σx ) = |σy )

Uz,π/2 |σy ) = − |σx )
Uz,π/2 |σz ) = |σz ) .


Lemma 73 The states Ψ, Φz, π2 , and Ψz, π2 have a standard representation of the form


0 0
0 0


0 1 eiγ 0
SΨ = 12 

0 e−iγ 1 0
0 0
0 0



1
0 0 λieiθ


0
0 0 0 

SΦz, π = 21 

2

0
0 0 0 
−λie−iθ 0 0 1

(63)


0
0
0 0


1
µieiγ 0
0
SΨz, π = 21 
.
2
0 −µie−iγ
1 0
0
0
0 0

with θ as in corollary 46, γ ∈ [0, 2π) and λ, µ ∈ {−1, 1}.
Proof. Let us start from Ψ. First, from Eq.(62) it is
immediate to obtain (a1 ⊗ a1 | Ψ) = (a2 ⊗ a2 | Ψ) = 0 and
(a1 ⊗ a2 | Ψ) = (a2 ⊗ a1 | Ψ) = 1/2. This gives the diagonal elements of SΨ . Then, using theorem 17 we obtain
that SΨ must be as in Eq. (63), for some value of γ. Let
us now consider Φz, π2 . Again, the diagonal elements of
the matrix SΦz, π are obtained from Eq. (62), which in
2


this case yields (a1 ⊗ a1 | Φz, π2 = (a2 ⊗ a2 | Φz, π2 = 1/2


and (a1 ⊗ a2 | Φz, π2 = (a2 ⊗ a1 | Φz, π2 = 0. Hence, by
theorem 17 we must have


1 0 0 eiλ

1
 0 0 0 0
SΦz, π = 

2
2 0 0 0 0 
e−iλ 0 0 1
for some value of λ ∈ [0, 2π). Now, denote by A the effect
such that (A| Φ) = 1. We then have

(A| Φz, π2 = Tr[EA SΦz, π ] = Tr[SΦ SΦz, π ]
2

2

(A| Φz, π2 = Tr[FA TΦz, π ] = Tr[TΦ TΦz, π ] =
2

2

for some µ ∈ [0, 2π). The relation Tr[SΨ SΨz, π ] =
2
Tr[TΨ TΨz, π ] = 1/2 then implies µ = γ ± π2 . 
2

Let
us
now
consider
the
four
vectors
(11,22)
(11,22)
(12,21)
(12,21)
Σx
, Σy
, Σx
, Σy
defined as follows







0 0
0 0

1
0 1 eiµ 0
SΨz, π = 
,
2
2 0 e−iµ 1 0
0 0
0 0

1
,
2

having used theorem 18, corollary 44, and Eq. (61).
Hence, we have Tr[SΦ SΦz, π ] = 1/2, which im2
plies λ = θ ± π2 , as in Eq. (63). Finally, the



1
σ
⊗
σ
Σ(11,22)
=
2
Φ
−
χ
⊗
χ
−
z
z
A
B
x
4


1
π − χ
Σ(11,22)
=
2
Φ
σ
⊗
σ
⊗
χ
−
z, 2
z
z
A
B
y
4


1
Σ(12,21)
= 2 Ψ − χA ⊗ χB + σz ⊗ σz
x
4


1
π − χ
σ
⊗
σ
⊗
χ
+
Σ(12,21)
=
2
Ψ
z
z .
A
B
z, 2
x
4

(64)

By the previous results, it is immediate to obtain the
matrix representations of these vectors. In the tensor
representation, using Eqs. (54) and (61) we obtain




0 0 0 1


0 0 0 0
TΣ(11,22) = 
,
x
0 0 0 0
1 0 0 0


0 0 0 0


0 0 1 0
TΣ(12,21) = 
,
x
0 1 0 0
0 0 0 0




0 0 0 −i


0 0 0 0 
TΣ(11,22) = 
,
y
0 0 0 0 
i 0 0 0


0 0 0 0


0 0 −i 0
TΣ(12,21) = 
,
y
0 i 0 0
0 0 0 0

while in the standard representation, using Eqs. (46) and

<!-- page 43 -->
43
(63), we obtain



0 0 0 eiθ


 0 0 0 0
SΣ(11,22) = 

x
 0 0 0 0
e−iθ 0 0 0


0
0 0 −λieiθ


0 0
0 
 0
SΣ(11,22) = 

y
 0
0 0
0 
λie−iθ 0 0
0


0 0
0 0


0 0 eiγ 0
SΣ(12,21) = 

x
0 e−iγ 0 0
0 0
0 0


0
0
0
0


0
−µieiγ 0
0
SΣ(11,22) = 
,
x
0 µie−γ
0
0
0
0
0
0

Proof. Combining lemma 70 with lemma 74 we obtain
that S and T coincide on the tensor products basis B ×
B, where B = {ϕ1 , ϕ2 , σx , σy }. By linearity, S and T
coincide on every state. 
From now on, whenever we will consider a composite
system AB where A and B are two-dimensional we will
adopt the choice that guarantees that the standard representation coincides with the tensor representation.
D.

Positivity of the matrices

In this paragraph we show that the states in our theory
can be represented by positive matrices. This amounts
to prove that for every system A, the set of states St1 (A)
can be represented as a subset of the set of density matrices in dimension dA . This result will be completed
in subsection XIII E, where we will see that, in fact, every density matrix in dimension dA corresponds to some
state of St1 (A).
The starting point to prove positivity is the following:

Comparing the two matrix representations we are now in
position to prove the desired result:

Lemma 75 Let A and B be two-dimensional systems.
Then, for every pure state Ψ ∈ St(AB) one has SΨ ≥ 0.

Lemma 74 With a suitable choice of axes, one has
Sσk ⊗σl = Tσk ⊗σl for every k, l = x, y.

Proof. Take an arbitrary vector VP∈ C2√⊗ C2 , writ2
λn |vn i|wn i.
ten in the Schmidt form as |V i =
n=1
Introducing the unitaries U, V such that U |vn i = |ni
and V |wn i = |ni for every n = 1, 2 then we have
P2 √
|V i = (U † ⊗ V † )|W i, where |W i =
n=1 λn |ni|ni.
Therefore, we have

Proof. For the face (11, 22), using the freedom coming
from Eqs. (43) and (44), we redefine the x and y axes so
(11,22)
(11,22)
(11,22)
(11,22)
that σx
:= Σx
and λσy
:= Σy
. In this
way we have
SΣ(11,22) = TΣ(11,22)
k

k

∀k = x, y

Likewise, for the face (12, 21) we redefine the x and y
(12,21)
(12,21)
(12,21)
(12,21)
axes so that σx
:= Σx
and µσy
:= Σy
,
so that we have
SΣ(12,21) = TΣ(12,21)
k

k

∀k = x, y.

Finally, using Eqs. (55), (62), and (64) we have the relations
σx ⊗ σx = Σ(11,22)
+ Σ(12,21)
x
x

σy ⊗ σy = Σ(11,22)
− Σ(12,21)
x
x

σx ⊗ σy = Σ(11,22)
− Σ(12,21)
y
y

σy ⊗ σx = Σ(11,22)
+ Σ(12,21)
.
y
y
Since S and T coincide on the right-hand side of each
equality, they must also coincide on the left-hand side. 
Theorem 19 With a suitable choice of axes, the standard representation coincides with the tensor representation, that is, Sρ = Tρ for every ρ ∈ St(AB).

hV |SΨ |V i = hW |S(U ⊗V )Ψ |W i
where U and V are the reversible transformations defined by SU ρ = U Sρ U † and SV ρ = V Sρ V † , respectively
(U and V are physical transformations by virtue of corollary 30). Here we used the fact that the standard twoqubit representation coincides with the tensor representation and, therefore, S(U ⊗V )Ψ = (U ⊗ V )SΨ (U ⊗ V )† .
Denoting the pure state (U ⊗ V ) |Ψ) by |Ψ′ ) we then
have
hV |SΨ |V i =λ1 [SΨ′ ]11,11 + λ2 [SΨ′ ]22,22
p
+ 2 λ1 λ2 Re ([SΨ′ ]11,22 )
Since by theorem 17 we have
p
[SΨ′ ]11,11 [SΨ′ ]22,22 eiθ , we conclude

[SΨ′ ]11,22

hV |SΨ |V i =λ1 [SΨ′ ]11,11 + λ2 [SΨ′ ]22,22 +
q
+ 2 cos θ λ1 λ2 [SΨ′ ]11,11 [SΨ′ ]22,22
q
2
q
′
′
≥
≥ 0.
λ1 [SΨ ]11,11 − λ2 [SΨ ]22,22

=

<!-- page 44 -->
44
Since the vector V ∈ C2 ⊗ C2 is arbitrary, the matrix SΨ
is positive. 
Corollary 47 Let C be a system of dimension dC = 4.
Then, with a suitable choice of matrix representation the
pure states of C are represented by positive matrices.
Proof. The system C is operationally equivalent to
the composite system AB, where dA = dB = 2. Let
U ∈ Transf(AB, C) be the reversible transformation implementing the equivalence. Now, we know that the
states of AB are represented by positive matrices. If we
define the basis vectors for C by applying U to the basis
for AB, then we obtain that the states of C are represented by the same matrices representing the states of
AB. 
Corollary 48 Let A be a system with dA = 3. With a
suitable choice of matrix representation, the matrix Sϕ is
positive for every pure state ϕ ∈ St(A).
Proof. Let C be a system with dC = 4. By corollary 47
the states of C are represented by positive matrices. Define the state ω := 31 (ϕ1 + ϕ2 + ϕ3 ), where {ϕm }4m=1 are
four perfectly distinguishable pure states. By the compression axiom, the face Fω can be encoded in a threedimensional system D (corollary 40). In fact, since D is
operationally equivalent to A, the face Fω can be encoded
in A. Let E ∈ Transf(D, A) and D ∈ Transf(A, D) be the
encoding and decoding operation, respectively. If we define the basis vectors for A by applying E to the basis
vectors for the face Fω , then we obtain that the states of
A are represented by the same matrices representing the
states in the face Fω . Since these matrices are positive,
the thesis follows. 
From now on, for every three-dimensional system A
we will choose the x and y axes so that Sρ is positive for
every ρ ∈ St(A).
Corollary 49 Let ϕ ∈ St1 (A) be a pure state with dA =
3. Then, the corresponding matrix Sϕ , given by


√
√
p1
p1 p2 eiθ12
p1 p3 eiθ13
√

√
Sϕ =  p1 p2 e−iθ12
p2 p3 eiθ23  . (65)
p2
√
√
p3
p1 p3 e−iθ13
p2 p3 e−iθ23
satisfies the property

eiθ13 = ei(θ12 +θ23 ) .
Equivalently, Sϕ = |vihv|, where v ∈ C3 is the vector
√ √
√
given by |vi := ( p1 , p2 e−iθ12 , p3 e−iθ13 )T .
Proof. The relation can be trivially satisfied when
pi = 0 for some i ∈ {1, 2, 3}. Hence, let us assume
p1 , p2 , p3 > 0. Computing the determinant of Sϕ one
obtains det(Sϕ ) = 2p1 p2 p3 [cos(θ12 + θ23 − θ13 ) − 1]. Since
Sϕ is positive, we must have det(Sϕ ) ≥ 0. If p1 , p2 , p3 > 0
the only possibility is θ13 = θ12 + θ23 mod 2π. 

Corollary 49 can be easily extended to systems of arbitrary dimension. To this purpose, we choose the x− and
y−axes in such a way that the projection of every state
ρ ∈ St1 (A) on a three-dimensional face is represented by
a positive matrix.
Lemma 76 If ϕ ∈ St1 (A) is a pure state and dA = N ,
then Sϕ = |vihv|, where v ∈ CN is the vector given
√ √
√
by v := ( p1 , p2 e−iα2 , . . . , pN e−iαN )T with αi ∈
[0, 2π) ∀i = 2, . . . , N .
Proof. Consider a triple V = {p, q, r} ⊆ {1, . . . , N }.
Then the state ΠV |ϕ) is proportional to a pure state of a
three dimensional system, whose representation SΠV ϕ is
the 3 × 3 square sub-matrix of Sϕ with elements [Sϕ ]kl =
√
pk pk eiθkl , (k, l) ∈ V × V . Now, corollary 49 forces the
relation eiθpr = ei(θpq +θqr ) . Since this relation must hold
for every choice of the triple V = {p, q, r}, if we define
αp := θp1 , then we have eiθpq = ei(θp1 +θ1q ) = ei(θp1 −θq1 ) =
ei(αp −αq ) . It is then immediate to verify that Sϕ = |vihv|,
√
√ √
where v = ( p1 , p2 e−iα2 , . . . , pN e−iαN )T . 
In conclusion, we proved the following
Corollary 50 For every system A, the state space
St1 (A) can be represented as a subset of the set of density
matrices in dimension dA .
Proof. For every state ρ ∈ St1 (A) the matrix Sρ is
Hermitian by construction, with unit trace by corollary
42, and positive since it is a convex mixture of positive
matrices. 

E.

Quantum theory in finite dimensions

Here we conclude our derivation of quantum theory
by showing that every density matrix in dimension dA
corresponds to some state ρ ∈ St1 (A).
We already know from the superposition principle
A
(lemma 16) that for every choice probabilities {pi }di=1
dA
there is a pure state ϕ ∈ St1 (A) such that {pi }i=1 are
the diagonal elements of Sϕ . Thus, the set of density matrices corresponding to pure states contains at
least one matrix of the form Sϕ = |vihv|, with |vi =
√ √
√
( p1 , p2 e−iβ2 , . . . , pdA e−iβdA ). It only remains to
prove that every possible choice of phases βi ∈ [0, 2π)
corresponds to some pure state.
Recall that for a face F ⊆ St1 (A) we defined the group
GF,F ⊥ to be the group of reversible transformations U ∈
GA such that U =ωF IA and U =ωF⊥ IA . We then have
the following
Lemma 77 Consider a system A with dA = N . Let
{ϕi }N
i=1 ⊂ St1 (A) be a maximal set of perfectly distinguishable pure states, F be the face identified by ωF =
PN −1
1/(N − 1) i=1 ϕi and F ⊥ its orthogonal face, identified by the state ϕN . If U is a reversible transformation

<!-- page 45 -->
45
in GF,F ⊥ , then the action of U is given by


0

.. 
 I
. 

N −1
SU ρ = U Sρ U †
U =



0 
0 . . . 0 e−iβ

Now, since ϕ and U ϕ are pure states, by corollary 49 we
must have
eiθ13 = ei(θ12 +θ23 )
(66)

where IN −1 is the (N − 1) × (N − 1) identity matrix and
β ∈ [0, 2π).
Proof. Consider an arbitrary state ρ ∈ St1 (A) and its
matrix representation
!
S ΠF ρ
f
,
Sρ =
f † S Π⊥
Fρ
where f ∈ CN −1 is a suitable vector. Since U =ωF IA
and U =ωF⊥ IA , we have that
!
S ΠF ρ g
SU ρ =
,
g † S Π⊥
Fρ
where g ∈ CN −1 is a suitable vector. To prove Eq. (66),
we will now prove that g = eiβ f for some suitable β ∈
[0, 2π).
Let us start from the case N = 3. Since U |ϕi ) =
|ϕi ) ∀i = 1, 2, 3, we have (ai | U = (ai | ∀i = 1, 2, 3
(lemma 51). This implies that U sends states in the face
F13 to states in the face F13 : indeed, for every ρ ∈ F13 one
has (a13 | U |ρ) = (a13 | ρ) = 1, which implies U ρ ∈ F13
(lemma 46). In other words, the restriction of U to the
face F13 is a reversible qubit transformation. Therefore,
the action of U on a state ρ ∈ F13 must be given by


ρ11
0 ρ13 eiβ


SU ρ =  0
0
0 
ρ31 e−iβ 0 ρ33 ,

for some β ∈ [0, 2π). Similarly, we can see that U sends
states in the face F23 to states in the face F23 . Hence,
for every σ ∈ F23 we have


0
0
0
′

SU σ =  0
σ22
σ23 eiβ 
′
0 σ32 e−iβ
ρ33
′

for some β ′ ∈ [0, 2π). We now show that eiβ = eiβ . To
see that, consider a generic state ϕ ∈ St1 (A), with the
property that pi = (ai | ϕ) > 0 for every i = 1, 2, 3 (such
state exists due to the superposition principle of theorem
16). Writing Sϕ as in Eq. (65) we then have
SU ϕ =



√
√
p1
p1 p2 eiθ12
p1 p3 ei(θ13 +β)
′ 
 √
√
=
p1 p2 e−iθ12
p2 p3 ei(θ23 +β ) 
p2
′
√
√
p1 p3 e−i(θ13 +β) p2 p3 e−i(θ23 +β )
p3

′

ei(θ13 +β) = ei(θ12 +θ23 +β ) .
′

By comparison we obtain eiβ = eiβ . This proves Eq.
(66) for N = 3. The proof for N > 3 is then immediate:
for every three-dimensional face FpqN the action of U is
given Eq. (66) for some βpq . However, since the two faces
FpqN and Fpq′ N overlap on ϕp we must have βpq = βpq′ .
Similarly βpq = βp′ q . We conclude that βpq = β for every
p, q. This proves Eq. (66) in the general case. 
We now show that every possible phase shift in Eq.
(66) corresponds to a physical transformation:
Lemma 78 A transformation U of the form of Eq. (66)
is a reversible transformation for every β ∈ [0, 2π).
Proof. By lemma 77, the group GF,F ⊥ is a subgroup
of U (1). Now, there are two possibilities: either GF,F ⊥
is a (finite) cyclic group or GF,F ⊥ coincides with U (1).
However, we know from theorem 15 that GF,F ⊥ has a
continuum of elements. Hence, GF,F ⊥ ≃ U (1) and β can
take every value in [0, 2π). 
An obvious corollary of the previous lemmas is the following
Corollary 51 The transformation Uβ defined by
SUβ ρ = U Sρ U † ,

(67)

where U is the diagonal matrix with diagonal elements
(1, eiβ1 , . . . , eiβN −1 ) is a reversible transformation for every vector β := (β2 , . . . , βN ) ∈ [0, 2π) × · · · × [0, 2π).
This leads directly to the conclusion of our derivation:
Theorem 20 For every system A, the state space St1 (A)
is the set of all density matrices on the Hilbert space CdA .
Proof. Let N = dA . For every choice of probabilities
p = (p1 , . . . , pN ) there exists at least one pure state ϕp
such that pk = (ak | ϕp ) for every k = 1, . . . , N (lemma
16 ). This state is represented by the matrix Sϕp =
√ √
√
|vp ihvp | with |vp i = ( p1 , p2 e−iα2 , . . . , pN e−iαN )T
(lemma 76). Finally, we can transform ϕp with every reversible transformation Uβ defined in Eq. (67),
thus obtaining SUβ ϕp = Uβ |vp ihvp |Uβ† where Uβ |vp i =
√ √
√
( p1 , p2 e−i(α2 +β2 ) , . . . pN e−i(αN +βN ) )T . Since p and
β are arbitrary, this means that every rank-one density
matrix corresponds to some pure state. Taking the possible convex mixtures we obtain that every N × N density
matrix corresponds to some state of system A. 
Choosing a suitable representation ρ 7→ Sρ , we proved
that for every system A the set of normalized states
St1 (A) is the whole set of density matrices in dimension

<!-- page 46 -->
46
dA . Thanks to the purification postulate, this is enough
to prove that all the effects Eff(A) and all the transformations Transf(A, B) allowed in our theory are exactly
the effects and the transformations allowed in quantum
theory. Precisely we have the following
Corollary 52 For every couple of systems A and B the
set of physical transformations Transf(A, B) coincides
with the set of all completely positive trace-non increasing
maps from MdA (C) to MdB (C).

Proof. We proved that our theory has the same normalized states of quantum theory. On the other hand, quantum theory is a theory with purification and in quantum
theory the possible physical transformations are quantum operations, i.e. completely positive trace-preserving
maps. The thesis then follows from the fact that two
theories with purification that have the same set of normalized states are necessarily the same (theorem 3). 

XIV.

CONCLUSION

Quantum theory can be derived from purely informational principles. In particular, it belongs to a broad class
of theories of information-processing that includes classical and quantum information theory as special cases.
Within this class, quantum theory is identified uniquely
by the purification postulate, stating that the ignorance
about a part is always compatible with the maximal
knowledge of the whole in an essentially unique way.
This postulate appears as the origin of the key features
of quantum information processing, such as no-cloning,
teleportation, and error correction (see also Ref. [21]).
The general vision underlying the present work is that
the main primitives of quantum information processing
should be derived directly from the principles, without
the abstract mathematics of Hilbert spaces, in order to
make the revolutionary aspects of quantum information
immediately accessible and to place them in the broader
context of the fundamental laws of physics.
Finally, we would like to comment on possible generalizations of our work. As in any axiomatic construction,
one can ask how the results change when the principles
are modified. For example, one may be interested in relaxing the local distinguishability axiom and in considering theories, like quantum theory on real Hilbert spaces,
where global measurements are essential to characterize
the state of a composite system. In this direction, the results of Ref. [21] suggest that also quantum theory on real
Hilbert spaces can be derived from the purification principle, after that the local distinguishability requirement
has been suitably relaxed. A possible way to weaken the
local distinguishability requirement is to assume only the

property of local distinguishability from pure states proposed in Ref. [21]: this property states that the probability of distinguishing two states by local measurements
is larger than 1/2 whenever one of the two states is pure.
A different way to relax local distinguishability would be
to assume the property of 2-local tomography proposed
in Ref. [39], which requires that the state of a multipartite system can be completely characterized using only
measurements on bipartite subsystems. This property
is equivalent to 2-local distinguishability, defined as the
requirement that two different states of a multipartite
system can be distinguished with probability of success
larger than 1/2 using only local measurements or measurements on bipartite subsystems.
A more radical generalization of our work would be to
relax the assumption of causality. This would be particularly important for the discussion of quantum gravity
scenarios, where the causal structure is not given a priori but is part of the dynamical variables of the theory.
In this respect, the contribution of our work is twofold.
First, it makes evident how fundamental is the assumption of causality in the ordinary formulation of quantum theory: the whole formalism of quantum states as
density matrices with unit trace, quantum measurements
as resolutions of the identity, and quantum channels as
trace-preserving maps is crucially based on it. Technically speaking, the fact that the normalization of a state
is given by a single linear functional (the trace, in quantum theory) is the signature of causality. This partly
explains the troubles and paradoxes encountered when
trying to combine the formalism of density matrices with
non-causal evolutions, as in Deutsch’s model for close
timelike curves [40, 41]. Moreover, given that the usual
notion of normalization has to be abandoned in the noncausal scenario, and that the ordinary quantum formalism becomes inadequate, one may ask in what sense a
theory of quantum gravity would be “quantum”. The
suggestion coming from our work is that a “quantum”
theory is a theory satisfying the purification principle,
which can be suitably formulated even in the absence of
causality [42]. The discussion of theories with purification in the non-causal scenario is an exciting avenue of
future research.
ACKNOWLEDGMENTS

The authors are grateful to S Flammia for adding to
the package qcircuit the commands needed for the diagrammatic representation of states and effects.
Research at Perimeter Institute for Theoretical Physics
is supported in part by the Government of Canada
through NSERC and by the Province of Ontario through
MRI. Research at QUIT is supported by the University
of Pavia and by INFN. Perimeter Institute and INFN
supported the mutual exchange of scientific visits that
made this work possible.

<!-- page 47 -->
47

[1] D. Hilbert, J. von Neumann, L. Nordheim, Mathematische Annalen 98, 1-30 (1928).
[2] J. von Neumann, Mathematical Foundations of Quantum
Mechanics, (Princeton Univ. Press, Princeton, 1932).
[3] G. Birkhoff, in R.P. Dilworth (ed.), Lattice Theory, Proceedings of the Second Symposium in Pure Mathematics
of the American Mathematical Society, April 1959, Providence: American Mathematical Society (1961).
[4] G. Birkhoff and J. von Neumann, Ann. Math. 37, 743
(1936).
[5] G. W. Mackey, The mathematical foundations of quantum mechanics (W. A. Benjamin Inc, New York, 1963).
[6] J. M. Jauch and C. Piron, Helv. Phys. Acta 36, 837
(1963).
[7] B. Coecke, D. Moore, A. Wilce, Current research in operational quantum logic: algebras, categories, languages
(Fundamental theories of physics series, Kluwer Academic Publishers, 2000).
[8] G. Ludwig, Foundations of quantum mechanics, vol. I
and II (Springer-Verlag, New York, 1983 and 1985).
[9] W. K. Wootters and W. H. Zurek, Nature 299, 802,
(1982).
[10] D. Dieks, Phys. Lett. A, 92, 271, (1982).
[11] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A.
Peres, W. K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).
[12] S. Wiesner, Sigact News 15, 78, (1983).
[13] C.H. Bennett and G. Brassard, in: Proceedings IEEE
Int. Conf. on Computers, Systems and Signal Processing,
Bangalore, India (IEEE, New York, 1984), pp. 175-179.
[14] A. K. Ekert, Physs Rev. Lett. 67, 661 (1991).
[15] P. W. Shor, SIAM J. Comput. 26, 1484 (1997).
[16] L. Hardy, arXiv:quant-ph/0101012
[17] B. Dakic and C. Brukner, arXiv:0911.0695.
[18] L. Masanes and M. Müller, arXiv:1004.1483v2.
[19] G. M. D’Ariano, AIP Conf. Proc. 810, 114 (2006); AIP
Conf. Proc. 844, 101 (2006); AIP Conf. Proc. 889, 79
(2007); Proc. of the 8th Int. Conf. on Quantum Communication, Measurement and Computing (NICT press,
Japan, 2007), p. 345.
[20] G. M. D’Ariano, in Philosophy of Quantum Information and Entanglement, Eds. A. Bokulich and G. Jaeger
(Cambridge University Press, Cambridge UK).
[21] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Phys.
Rev. A 81, 062348 (2010).
[22] John A. Wheeler, in W. Zurek (ed.) Complexity, Entropy,

and the Physics of Information, Addison-Wesley, Redwood City, CA (1990).
[23] E. Schrödinger, Proc. Camb. Phil. Soc. 31, 555 (1935).
[24] In fact, the equivalence of all purifications under local reversible transformations is tightly related to what seems
the main point of Schrödinger’s paper, namely that all
possible ensembles of a mixed state can be “steered” by
measurements on the purifying system. This property is
an immediate consequence of the equivalence of all purifications.
[25] W. Arveson, An Invitation to C*-Algebras, SpringerVerlag (New York), 1976.
[26] W. F. Stinespring, Proc. Am. Math. Soc., 6 , 211 (1955).
[27] M.A. Nielsen and I.L. Chuang, Phys. Rev. Lett. 79, 321
(1997).
[28] In quantum theory the trivial system I is represented by
the one-dimensional Hilbert space H ≃ C.
[29] B. Coecke, in Quantum Theory: Reconsiderations of the
Foundations III, pp.81. AIP Press (2005).
[30] B. Coecke, Contemporary Physics 51, 59 (2010).
[31] G. Chiribella, G. M. D’Ariano, and P. Perinotti, EPL 83,
30004 (2008).
[32] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Phys.
Rev. A 80, 022339 (2009).
[33] L. Hardy, J. Phys. A 40, 3081 (2007).
[34] L. Hardy, arXiv:1005.5164.
[35] B. Coecke and R. Lal, in Proceedings of the 7th workshop
on Quantum Physics and Logic, B. Coecke, P. Panangaden and P. Selinger eds.
[36] J. Barrett, Phys. Rev. A 75, 032304 (2007).
[37] A. Wilce, Found. Phys. 40, 434 (2010).
[38] In principle, the purifying system for the state Ri might
depend on the value of i, let us call it Ci . However,
since there is a finite number of outcomes one can always
choose a single purifying system by defining the composite system C = C1 . . . CN (here we labelled the outcomes
with the natural numbers {1, . . . , N }). If Ψi ∈ St(ACi )
is a purification of Ri and ψi is any pure state on the
composite system including all system but the i-th, then
also Ψ′i = Ψi ⊗ ψi ∈ St(AC) is a purification of Ri .
[39] L. Hardy and W. K. Wootters, arXiv:1005.4870.
[40] D. Deutsch, Phys. Rev. D 44, 3197 (1991).
[41] C. H. Bennett, D. Leung, G. Smith, and J. A. Smolin,
Phys. Rev. Lett. 103, 170502 (2009).
[42] G. Chiribella, G. M. D’Ariano, and P. Perinotti, in preparation.
