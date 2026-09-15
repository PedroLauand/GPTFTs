---
type: paper
date: 2021-03-12
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:2103.07469v2)
reviewed: false
---

# General probabilistic theories: An introduction

Machine-generated and unreviewed text extraction of arXiv:2103.07469v2
(77 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/2103.07469v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
General probabilistic theories: An introduction
Martin Plávala
Naturwissenschaftlich-Technische Fakultät, Universität Siegen, 57068 Siegen, Germany

arXiv:2103.07469v2 [quant-ph] 23 Aug 2021

Abstract
We introduce the framework of general probabilistic theories (GPTs for short). GPTs are a class of operational theories that generalize both finite-dimensional classical and quantum theory, but they also include
other, more exotic theories, such as the boxworld theory containing Popescu-Rohrlich boxes. We provide
in-depth explanations of the basic concepts and elements of the framework of GPTs, and we also prove
several well-known results. The review is self-contained and it is meant to provide the reader with consistent introduction to GPTs. Our tools mainly include convex geometry, but we also introduce diagrammatic
notation and we often express equations via diagrams.

Contents
1 Introduction
1.1 Organization of the review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2
4

2 What are GPTs?

5

3 State spaces and effect algebras
3.1 State space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Effect algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Duality between the state space and the effect algebra . . . . . . . . . . . . . . . . . . . . . .
3.4 Connection to abstract convex effect algebras and order unit spaces . . . . . . . . . . . . . . .
3.5 Some useful results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.6 Order unit norm, base norm and discrimination tasks . . . . . . . . . . . . . . . . . . . . . .
3.7 No-restriction hypothesis and restricted theories . . . . . . . . . . . . . . . . . . . . . . . . .
3.8 Diagrammatic notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6
6
7
10
12
14
15
18
18

4 Example: classical theory

19

5 Tensor products
5.1 Bipartite scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Multipartite scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Diagrammatic notation for multipartite scenarios . . . . . . . . . . . . . . . . . . . . . . . . .
5.4 Partial trace and monogamy of entanglement . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.5 Existence of entanglement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

22
23
26
28
29
33

Email address: martin.plavala@uni-siegen.de (Martin Plávala)

August 24, 2021

<!-- page 2 -->
6 Channels, measurements and instruments
6.1 Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2 Measurements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Instruments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4 Preparations, measure-and-prepare channels . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5 Completely-positive channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.6 Post-processing preorder of channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

34
34
38
39
40
41
43

7 Compatibility of channels
7.1 No-broadcasting theorem and existence of incompatible measurements . . . . . . . . . . . . .
7.2 Preorder of channels and compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Incompatibility witnesses, steering, and Bell non-locality . . . . . . . . . . . . . . . . . . . . .

43
46
49
50

8 Example: quantum theory
8.1 State space and effect algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Tensor product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3 Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4 Compatibility of channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

57
57
58
59
59

9 Example: boxworld theory
9.1 State space and effect algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2 Tensor product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3 Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4 Compatibility of channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

59
60
60
64
64

Appendix A

Convex cones and ordered vector spaces

69

Appendix B

Functionals, duals and hyperplane separation theorems

71

Appendix C

Bilinear forms, linear maps and tensor products

74

1. Introduction
General probabilistic theories (GPTs for short) are a framework developed within the foundations of
physics in many different forms and flavors. The main goals of GPTs was to answer the question: what is
a physical theory? This question usually appeared in the context of axiomatizations of quantum theory, as
many researchers were attempting to derive quantum theory from a set of reasonably motivated axioms. In
the current days, the aim of the research is no longer only to search for axiomatizations of quantum theory,
the current research in GPTs is oriented towards operational properties of GPTs. It is often investigated
what structure is needed to realize certain protocols or constructions known from quantum information
theory or classical information theory. For example:
• The nonlocal features of quantum theory, such as entanglement, steering and Bell inequality violations
we investigated in GPTs [1–9]. One can, for example, construct theories which maximally violate
the CHSH inequality and hence provide an implementation of the Popescu-Rohrlich (PR) boxes [10].
Other research directions include investigating and generalizing steering in GPTs, using the general
definition of steering provided in [11].
• Uncertainty relations [4, 12–16] and incompatibility of measurements and channels [5, 17–27] were
investigated in GPTs. Incompatibility of measurements is a generalization of the non-commuting
observables in quantum theory to an operational framework. One can then easily extend the definition
of incompatibility of measurements to channels. Most of the results show that the existence of certain
type of incompatibility or uncertainty is a consequence of some non-classical features of the theory.
2

<!-- page 3 -->
• Noncontextuality [28–32] of GPTs was investigated. Note that some of the works on noncontextuality in
operational theories use more general framework, e.g. they do not assume the no-restriction hypothesis.
• Causal structures [33, 34], dynamics [35–39], physical properties [40–42], double-slit and multiple-slit
interference [43–50] were investigated. Most of the research into physical properties and interference
tries to capture some underlying phenomena and investigate them either in terms of black boxes, or in
terms of information-theoretic applications, almost always using finite-dimensional effective theories.
• Computation [51–57], resource theories [58, 59], cryptography and other information-theoretic tasks
[60–76] were investigated in GPTs. Large part of the protocols used in quantum information theory
do not rely on the formalism of Hilbert spaces, but they can be realized using only limited amount
of states and measurements. It is then natural to use convex geometry to characterize the required
relations between the states and measurements and then one can characterize all theories where certain
protocol can be performed.
• Different notions of entropy [77–81] and foundational aspects of thermodynamics [82–84] were investigated in GPTs. There are several different possible operational constructions that one can use to
define entropy in GPTs. Therefore some proofs that are immediate in quantum information theory
may, in the framework of GPTs, depend on the chosen definition of entropy and on the properties of
the state space.
• Diagonalization and existence of spectral decompositions were investigated [85–88]. It seems that
some form of spectral decompositions is crucial for singling out quantum and quantum-like theories
among other GPTs. Moreover, existence of suitable spectral decompositions would unify the different
definitions of entropy in GPTs.
• The original motivation for GPTs is still an active field of research to this day. There are many
papers on what axioms we need to add to GPTs to single-out quantum theory, or how to test whether
a theory is quantum [89–101]. The derivations of quantum theory are usually done in the finitedimensional framework and they often prove that all GPTs that satisfy certain axioms are connected
to Euclidean Jordan algebras. Jordan algebras [102] are vector spaces that contain the generalization
of the symmetric operator product 21 (AB + BA) and it is known that a class of Jordan algebras, called
Euclidean Jordan algebras, contains only quantum and quantum-like theories [103].
There are also several practical reasons to use GPTs, to name a few: one can often use GPTs to get
better understanding of what makes many things in quantum information theory work, or why they give us
advantage compared to classical theory. In GPTs, ensembles of objects, conditional probabilities, conditional
states and even joint systems of the aforementioned object can be represented by their respective state spaces
and so we can treat them as any other state space and we can use known results, instead of having to prove
them from scratch, often by mimicking known proofs from other scenarios. Representing all transformations
by channels allows us to use the constructions from frameworks based on category theory, such as operational
probabilistic theories [104–106] and effectus theory [107], since one can interpret state spaces as objects and
channels as morphisms.
There are several different approaches to GPTs, but all of them are either equivalent or only marginally
different. The approach we will use is to start with an abstract definition of state space. We find this
approach the easiest to explain and easy to work with, compared to the other options. An equivalent
approach would be to start with a table of all possible probabilities that can be generated in an experiment,
conditioned on preparation and measurement procedures. One can show that this is the same as starting
with an abstract state space, but instead of using vectors we would be describing states in terms of all of the
probabilities they can produce. A different approach would be to start with an ordered vector space with
order unit, or, equivalently, with a convex effect algebra. We will see that state spaces and effect algebras
are dual objects and starting from either one, we can reconstruct the other. Therefore we can freely choose
whether we start with state spaces, convex effect algebras, or order unit spaces; we will choose state spaces
as our starting point.
3

<!-- page 4 -->
Before we proceed further, we must comment on the name of the framework of GPTs. There are different
names for the same (or very similar) framework and they usually follow the formula
General
Generalized

Probability
+

Probabilistic
Physical

+

Theory
Theories

=

GPTs.

All possible combinations are frequently and interchangeably used by many authors and the common understanding is that the name can be used as long as the acronym is GPT or GPTs. Some authors do differentiate
between the singular GPT and plural GPTs, as follows: a GPT is a concrete theory, with specified state
spaces and tensor product, while GPTs is a collective name for the whole class of such theories. We will use
the following nomenclature: by general probabilistic theories, shortened to GPTs, we will mean the whole
framework including all possible state spaces.
1.1. Organization of the review
The review is organized as follows: in Section 2 we explain the basic concepts and operational motivations
of preparations, ‘yes’-‘no’ questions and transformations. These will later on correspond to states, effects
and channels. Note that we will start our construction from the state space (represented by a compact
convex set), but we will later show that without the loss of generality one can start from an effect algebra
or from order unit space and construct the same framework.
In Section 3 we introduce the state spaces and effect algebras and we prove some basic results. This
includes the duality between the state space and effect algebra, norms on state space and effect algebra and
its connection to discrimination tasks. We also discuss the connection of GPTs to abstract effect algebras and
order unit spaces and we show that these approaches are essentially equivalent to the one that we develop. At
the end of Section 3 we will introduce the diagrammatic notation, that we will use in subsequent calculations.
In Section 4 we present the first example: classical theory. This is because classical theory will play
an important role in later constructions, mainly in the definition of measurements in Section 6. Further
examples of quantum theory and boxworld theory will be constructed in Sections 8 and 9 respectively.
In Section 5 we introduce bipartite state spaces and tensor products, as well as partial traces and result on
monogamy of entanglement. We introduce tensor products before transformations (i.e., before channels and
measurements), because tensor products are helpful when working with channels, due to the isomorphism
between linear maps and elements of tensor products of vector spaces, that is reviewed in Appendix C.
Then in Section 6 we introduce channels as transformations between state spaces and we define measurements as special case of channels. We do this to promote the use of channels instead of measurements
whenever possible, since the formalism of channels is more suitable for the use of diagrammatic notation,
which simplifies certain constructions and allows for easier use of ideas coming from category theory in
quantum foundations.
In Section 7 we investigate the concept of compatibility of channels and measurements. We will show,
that several well known results in quantum theory and GPTs can be formulated as problems related to
compatibility of channels. We also use compatibility to prove results about structure of channels and
measurements.
In Sections 8 and 9 we construct two examples of GPTs: quantum theory and boxworld theory. We
postpone the examples to these sections, because we want to present them as clear and concise theories,
rater than as different constructions sprinkled in the other sections. But we encourage the reader to skip
ahead and look up examples of some of the concepts when reading earlier sections.
In order to make the review as much self-contained as possible, we introduce some mathematical concepts
that we need in the appendices. In Appendix A we review the notions of convex cones and ordered vector
spaces, in Appendix B we introduce the concept of functionals and the hyperplane separation theorems and
in Appendix C we introduce the isomorphism between tensor products of vector spaces, vector spaces of
bilinear forms and vector spaces of linear maps.
4

<!-- page 5 -->
2. What are GPTs?
The main objects that we will work with are going to be state spaces, effect algebras and channels. A
state space of a theory is going to be identified with a set of equivalence classes of preparation procedures,
and an effect is the equivalence class of ‘yes’-‘no’ questions that can be answered in an experiment. Before
we explain what we mean by the equivalence classes, we will first introduce preparations procedures and
‘yes’-‘no’ questions.
A preparation procedure is a list of instructions that one performs to prepare a system in question at the
beginning of an experiment. Note that the list of instructions may be conditioned by random events, e.g., the
preparation procedure may differ on whether it rains or not. This might seem strange at first, but consider
preparation of an experiment testing the tensile strength of a paper, that is to be performed outdoors. If
it rains, the paper gets wet and we observe a different outcome of the experiment compared to if it did not
rain. A ‘yes’-‘no’ question is a list of instructions that we perform after preparing a state to get either the
answer ‘yes’ or ‘no’. It is intuitive that more complex experiments can be build from ‘yes’-‘no’ questions,
as for example the ‘yes’ and ‘no’ can be interpreted as 1 and 0 and we can reformulate a measurement that
outputs a number as a series of ‘yes’-‘no’ questions determining the digits of the binary representation of
the measured number.
We will say that two preparations are equivalent if the results of all possible ‘yes’-‘no’ questions are the
same after the two preparations. Analogically, we will say that two ‘yes’-‘no’ questions are equivalent if they
produce the same answer with respect to all possible (equivalence classes of) preparations.
Channels are going to be the (equivalence class of) list of instructions that we can either append at the
end of preparation or, equivalently, prepend to the beginning of a ‘yes’-‘no’ question. This already yields a
well-known duality: appending instructions to the preparation performs a transformation of the state of the
system and it corresponds to the Schrödinger picture of quantum theory. Prepending instructions to the
beginning of an effect performs a transformation of the measurement and it corresponds to the Heisenberg
picture of quantum theory.
Since GPTs are traditionally motivated as a framework for developing axiomatizations of quantum theory,
we will provide five postulates about the properties of state spaces in the framework of GPTs. Four of these
postulates are intuitive and hard to argue against, while the fifth will limit us to mathematically simpler,
but still interesting scenarios.
Definition 2.1. State space is:
(S1) set of points,
(S2) convex,
(S3) closed in some physically motivated topology,
(S4) bounded,
(S5) subset of a real, finite-dimensional vector space with Euclidean topology.
We will use these five postulates to construct the framework of GPTs for single state spaces. We will
add additional postulates for bipartite and multipartite state spaces in Section 5. (S5) is the one postulate
that simplifies the mathematics used, e.g., we can avoid using abstract notion of convexity in (S2). Let K
denote a state space, we postulate in (S2) that the state space is convex, because if x, y ∈ K are two states
and p ∈ [0, 1] we want to be able to describe a scenario where we prepare x with probability p and y with
probability 1 − p. We use the convex combination px + (1 − p)y to describe such scenario and we say that
K is convex if px + (1 − p)y ∈ K for all x, y ∈ K, p ∈ [0, 1]. By requiring K to be convex, we require
that px + (1 − p)y is a well-defined state. We postulate in (S3) that the state space is closed, because we
assume that if we can prepare a state arbitrary close to some x then we can also prepare x. (S4) is not
necessarily needed, because if the state space would not be bounded, then there would be states that can
not be distinguished by any effect and so we would have to factorize the state space to a bounded set. The
following results connects Definition 2.1 to the standard introduction of a state space in GPTs:
5

<!-- page 6 -->
Proposition 2.2. Every state space is a compact convex subset of a real, finite-dimensional vector space.
Proof. We only need to prove that every state space is compact, but this follows from (S3), (S4) and (S5)
since every closed and bounded subset of real finite-dimensional vector space is compact [108, Theorem
27.3.].
In quantum theory, the state space is the set of density operators, that is the set of positive semi-definite
operators with trace normalized to one. It is common knowledge that the set of density operators is convex
and compact. The underlying vector space is the Hilbert-Schmidt space of self-adjoint operators, which is
real and finite-dimensional, given that the underlying Hilbert space is finite-dimensional. We will present
quantum theory as an example of a GPT in Section 8, but we invite the reader to skip ahead and look up
examples of the concepts presented in later sections.
3. State spaces and effect algebras
We have already characterized all state spaces in Proposition 2.2. In this section, we will construct
the effect algebra and the connection between a state space and its effect algebra. We will also investigate
connections to other formalisms: abstract convex effect algebras and order-unit spaces. We will denote by
V a real, finite-dimensional vector space and we will denote by K ⊂ V a compact, convex set, i.e., a state
space. Let X ⊂ V , then we will denote span(X) the span of X, by aff(X) the affine hull of X, by conv(X)
the convex hull of X and cone(X) be the smallest cone containing X, for definition of cone see Definition
A.1 in Appendix A. dim(V ) will denote the dimension of V . Let a, b ∈ R, then we will use (a, b) and [a, b]
to denote the open and closed intervals; R+ will denote the set of non-negative real numbers.
3.1. State space
Definition 3.1. Let K be a state space and let x ∈ K. We say that x is an extreme point of K, or
equivalently that x is a pure state, if for every y, z ∈ K and λ ∈ (0, 1) such that x = λy + (1 − λ)z we have
x = y = z.
Pure states are the states that can not be prepared by randomizing preparations of other states. It follows
that a pure state x must be preparable by a deterministic and non-randomized preparation procedure. Mixed
states are the counterpart to pure states.
Definition 3.2. Let x ∈ K, then we say that x is a mixed state if x is not a pure state. We say that x is a
mixture of y, z ∈ K if there is λ ∈ [0, 1] such that x = λy + (1 − λ)z.
One way of constructing a mixture λx + (1 − λ)y of states x, y ∈ K is to run the experiment N times and
to prepare x in λN of the runs and to prepare y in (1−λ)N of the runs (assuming λN and (1−λ)N are whole
numbers). Then the average state that was prepared is exactly the mixture. One can in principle object
to constructing the mixture in this way as it was pointed out that knowing how a mixture was prepared is
a non-trivial information about the system [109], but one can bypass this by representing the information
about preparation of the mixture as some additional classical information about the system; the classical
information can be represented using classical theory that will be introduced in Section 4. From now on we
will assume that one can prepare a mixture using the aforementioned construction.
The concept of pure state is generalized by the concept of face: a face F ⊂ K is a convex set of states,
such that every state from F can be prepared only by randomizing preparations that are contained in F .
In other words:
Definition 3.3. Let F ⊂ K be a convex set such that if for x, y ∈ K and λ ∈ (0, 1) we have λx + (1 − λ)y,
then x, y ∈ F . Then we say that F is a face of K.
Note that K itself is a face of K. Pure states and faces play important roles in the geometry of state
spaces, as demonstrated by the following results.
6

<!-- page 7 -->
Theorem 3.4 (Carathéodory). Let K ⊂ V be a state space and let B ⊂ K be a set such that K = conv(B).
Then any x ∈ K can be expressed as a convex combination of at most dim(V ) + 1 points from B.
Proof. See [110, Theorem 17.1].
Theorem 3.5. Let K be a state space and let ext(K) be the set of pure states of K then K = conv(ext(K)).
Proof. See [110, Theorem 18.5].
Let X ⊂ V be a convex set, then relative interior of X, denoted ri(X), is the topological interior of X
when considered as a subset of aff(X). For example, the relative interior of an interval [0, 1] ⊂ R is (0, 1),
but also the relative interior of a line segment L in arbitrary vector space is the open line segment contained
in L. A relative interior of a set {v} ⊂ V is again {v}. For finite-dimensional vector space V equipped with
the standard Euclidean topology, relative interior of a convex set X ⊂ V can be defined purely using the
convex structure of X as follows:
ri(X) = {x ∈ X : ∀y ∈ X, ∃µ > 1, (1 − µ)y + µx ∈ X}.

(3.1)

see [110, Section 6]. We will introduce two additional classes of state spaces: polytopes and strictly convex
state spaces. Both of them are a good source of examples and counter-examples in many calculations.
Definition 3.6. We say that a state space K is a polytope if ext(K) contains finitely many points, i.e., K
has finitely many pure states.
Definition 3.7. We say that a state space K is strictly convex if for any x, y ∈ K and λ ∈ (0, 1) we have
λx+(1−λ)y ∈ ri(K). Equivalently, K is strictly convex if for every face F of K it holds that either F = {x},
or F = K.
3.2. Effect algebra
An effect algebra is a list of all possible (equivalence classes of) ‘yes’-‘no’ questions. Moreover we also
want to allow the case, when the answer is not only either ‘yes’ or ‘no’, but also a probability of the ‘yes’
answer. This is quite natural, for example consider an unbiased coin. Will it land on the head if we flip it?
The standard answer is yes, with probability 50%. Another reason why we want to allow for probabilities is
that we often only predict probabilities in quantum theory and we want our formalism to include quantum
theory.
The answer to every ‘yes’-‘no’ question can be encoded by a number from the interval [0, 1], where we
will interpret p ∈ [0, 1] as the probability of the outcome ‘yes’. As we will see later on, ‘yes’-‘no’ questions
correspond to two-outcome (also called dichotomic) measurements, but for the time being, the description
using only a single number will be sufficient for us, since it is straightforward to see that the probability of
‘no’ is 1 − p. It follows that we can reduce the whole ‘yes’-‘no’ question to a single function f : K → [0, 1].
We will require that we get the same result whether we mix the state or whether we mix the probabilities.
This is a consistency requirement, as we have already assumed that we can prepare a mixture λx + (1 − λ)y,
where x, y ∈ K and λ ∈ [0, 1] by simply running the experiment several times and preparing either x or y.
Therefore we get
Definition 3.8. Let K be a state space, then the effect algebra over K will be denoted E(K). E(K) is the
set of all affine functions f : K → [0, 1], i.e.,
for all x ∈ K and
for all x, y ∈ K and λ ∈ [0, 1].

0 ≤ f (x) ≤ 1

(3.2)

f (λx + (1 − λ)y) = λf (x) + (1 − λ)f (y)

(3.3)

There is one very special element of E(K) that will frequently appear in our calculation:
7

<!-- page 8 -->
Definition 3.9. 1K ∈ E(K) is the constant function given as 1K (x) = 1 for all x ∈ K.
In the following we will construct several auxiliary notions that will appear in further calculations. More
specifically, we will construct the cone generated by the effect algebra, the vector space spanned by the effect
algebra and we will review some of their properties. For a short introduction to the theory of convex cones
see Appendix A.
Proposition 3.10. Let A(K) be the vector space of affine functions on K and let A(K)+ be the cone of
positive affine functions on K, i.e.,
A(K) = {f : K → R : f (λx + (1 − λ)y) = λf (x) + (1 − λ)f (y), ∀x, y ∈ K, ∀λ ∈ [0, 1]},
+

A(K) = {f ∈ A(K) : f (x) ≥ 0, ∀x ∈ K}.

(3.4)
(3.5)

Then A(K) = span(E(K)) and A(K)+ = cone(E(K)), i.e., A(K) is the smallest vector space containing
E(K) and A(K)+ is the smallest cone in A(K) that contains E(K).
Proof. We clearly have E(K) ⊂ A(K)+ ⊂ A(K) and so we only need to show that A(K) is contained in
span(E(K)) and that A(K)+ is contained in cone(E(K)). Let f ∈ A(K)+ , note that since K is compact we
1
f . Then f 0 ∈ E(K) since f 0 is affine function
must have M = maxx∈K f (x) < ∞ and so we can define f 0 = M
0
by construction and for any x ∈ K we have 0 ≤ f (x) ≤ 1, thus we have 0 ≤ f (x) ≤ M . It follows that any
f ∈ A(K)+ can be written as f = M f 0 where f 0 ∈ E(K) and M ∈ R+ and so A(K)+ ⊂ cone(E(K)). Now
let f ∈ A(K), then we must have m = minx∈K f (x) > −∞ and we can write f = (f + |m| 1K ) − |m| 1K .
Note that f + |m| 1K ∈ A(K)+ and |m| 1K ∈ A(K)+ and so we have
A(K) ⊂ span(A(K)+ ) = span(cone(E(K))) = span(E(K)),

(3.6)

where we have used Lemma A.2 from Appendix A.
In the following lemma we will use the concepts of pointed and generating cones, for definitions see
Appendix A.
Lemma 3.11. A(K)+ is a convex, closed (in the Euclidean topology), pointed and generating cone.
Proof. Let f, g ∈ A(K)+ , then for λ ∈ [0, 1] also λf +(1−λ)g must be a positive function and so λf +(1−λ)g ∈
+
A(K)+ . Let {fn }∞
n=1 ⊂ A(K) be a Cauchy sequence, then for every x ∈ K we must have limn→∞ fn (x) ≥ 0
simply because fn (x) ≥ 0. It follows that limn→∞ fn ∈ A(K)+ . To see that A(K)+ is pointed, simply
observe that if f ∈ A(K)+ ∩ (−A(K)+ ), then for every x ∈ K we have 0 ≤ f (x) ≤ 0, so f (x) = 0 and we
get f = 0. We have already showed in the proof of Proposition 3.10 that span(A(K)+ ) = A(K) and so the
cone A(K)+ is generating.
One can introduce a natural partial order to A(K) in an intuitive manner: let f ∈ A(K), then f ≥ 0
if and only if f (x) ≥ 0 for all x ∈ K. For f, g ∈ A(K), we have f ≥ g whenever f − g ≥ 0, i.e. whenever
f (x) ≥ g(x) for all x ∈ K. Also we write f ≤ g whenever g ≥ f . One can easily show that this ordering
turns A(K) into an ordered vector space.
Lemma 3.12. A(K) with the ordering ≥ is a ordered vector space, i.e., for f, g, h ∈ A(K) and λ ∈ R+ we
have
• f ≥ g implies f + h ≥ g + h;
• f ≥ g implies λf ≥ λg;
• f ≥ f;
• f ≥ g and g ≥ f implies f = g;
• f ≥ g and g ≥ h implies f ≥ h.

8

<!-- page 9 -->
Proof. It is a good exercise to prove the lemma directly. But observe that the the positive cone is exactly
A(K)+ , which, as we know, is convex, pointed cone. And so it follows from Proposition A.8 in Appendix A
that the order generated by A(K)+ , which coincides with the order ≥ endows A(K) with the structure of
ordered vector space.
We have introduced the effect algebra, one of the two main building blocks of every GPT, as a set of
affine functions with outcomes from the set [0, 1], i.e. as functions f ∈ A(K) such that 0 ≤ f (x) ≤ 1. Clearly
one can use the ordering ≥ on A(K) to characterize the effects as follows:
Proposition 3.13. We have
E(K) = {f ∈ A(K) : 0 ≤ f ≤ 1K }.

(3.7)

Proof. The result follows from the definition: let f ∈ A(K), then we have 0 ≤ f ≤ 1K if and only if
0 ≤ f (x) ≤ 1 for all x ∈ K.
Let f, g ∈ E(K) and define hM : K → R as hM (x) = max(f (x), g(x)) for x ∈ K. Then we clearly
have 0 ≤ hM (x) ≤ 1, but nevertheless in general hM ∈
/ E(K). This is because in general hM is not
an affine function; example when hM is not an affine function can easily be constructed in the boxworld
theory presented in Section 9. In some cases, for example if f ≥ g or in the case of the classical theory
presented in Section 4, hM is an affine function. Analogical results follow for the function hm defined as
hm (x) = min(f (x), g(x)). There is one more easy to see result that follows from the definition of ≥.
Lemma 3.14. Let f, g ∈ A(K). If f ≥ g, then there is h ∈ A(K)+ , i.e., h ≥ 0, such that f = g + h.
Proof. Let f ≥ g, let x ∈ K and define h(x) = f (x) − g(x). Then h ∈ A(K) as it is immediate that
h : K → R is an affine function. Moreover we have h(x) ≥ 0 because f (x) ≥ g(x) as a result of f ≥ g, and
so h ∈ A(K)+ . The result follows as we have f = g + h.
Proposition 3.13 and Lemma 3.14 represent the two use cases of the ordering ≥: we will use Proposition
3.13 to express a condition that some element f ∈ A(K) is an effect, i.e., that f ∈ E(K), and we will use
Lemma 3.14 to express the decomposition f = g + h in a different way. This can be demonstrated by the
following lemma:
Lemma 3.15. For every f ∈ E(K) there is f ⊥ ∈ E(K) such that f + f ⊥ = 1K .
Proof. Since f ∈ E(K), according to Proposition 3.13 we have f ≤ 1K , from which according to Lemma
3.14 we have 1K = f + f ⊥ for some f ⊥ ∈ A(K)+ . 1K ≥ f ⊥ and f ⊥ ∈ E(K) follows. Another way to prove
the statement is to show that 1K − f ≥ 0, then take f ⊥ = 1K − f .
The unit effect 1K has one additional property, that we have already used in the proof of Proposition
3.10: a suitable multiple of 1K can be used to bound any element of A(K) from above. This property can
be generalized as follows:
Definition 3.16. Let f ∈ A(K)+ be an element such that for every g ∈ A(K) there is µ ∈ R+ such that
g ≤ µf . Then we say that f is the order unit of A(K)+ .
Lemma 3.17. 1K is the order unit of A(K)+ .
Proof. Let g ∈ A(K) and let M = maxx∈K g(x). Then we have g ≤ M 1K .

9

<!-- page 10 -->
3.3. Duality between the state space and the effect algebra
We have already showed how one can start with the state space and construct the effect algebra E(K).
Now we will show that given an effect algebra E(K), we can reconstruct the state space K from E(K). In
the following we will rely on the notions of linear functionals and dual vector space, see Appendix B for a
short introduction to linear functionals, dual vector spaces and dual cones.
Let A(K)∗ denote the dual vector space to A(K), that is, let A(K)∗ be the vector space of all linear
functionals on A(K). Let ψ ∈ A(K)∗ and f ∈ A(K), then we will denote by hψ, f i the value that ψ assigns
to f , i.e., ψ : f 7→ hψ, f i. The presented notation is similar to the bra-ket notation for the inner product in
quantum theory, but remember that hψ, f i is not an inner product of two vectors, because f ∈ A(K) and
ψ ∈ A(K)∗ , i.e., f and ψ belong to different vector spaces. That being said, since we are working only in
finite-dimensional spaces, the structure is very similar to an inner product and one can think of hψ, f i as a
special type of inner product, which works only for a pair of ψ ∈ A(K)∗ and f ∈ A(K), but does not work
for a pair ψ, ϕ ∈ A(K)∗ , neither for a pair f, g ∈ A(K). This type of inner product-like structure is usually
called pairing or duality in linear algebra textbooks.
The dual cone to A(K)+ is
A(K)∗+ = {ψ ∈ A(K)∗ : hψ, f i ≥ 0, ∀f ∈ A(K)+ },

(3.8)

i.e., A(K)∗+ is the cone of functionals that are positive on the cone of positive functions A(K)+ . In terms
of Appendix B, A(K)∗+ = (A(K)+ )∗ .
Lemma 3.18. A(K)∗+ is a convex, closed, pointed and generating cone.
Proof. The result follows from Lemma 3.11 and Propositions B.6, B.7 and B.8 in Appendix B.
We can naturally embed K into A(K)∗+ using the following construction: let x ∈ K, f, g ∈ A(K) and
α, β ∈ R, then we have
(αf + βg)(x) = αf (x) + βg(x)
(3.9)
and so the expression f (x) is linear in f . It follows that we can define a linear functional x ∈ A(K)∗+ by
hx, f i = f (x).

(3.10)

We are abusing the notation by using the same symbol for the point x ∈ K and the functional x ∈ A(K)∗+ ,
but as we will shortly see, they are in fact isomorphic to each other. Also note that the functional x ∈ A(K)∗+
is positive by construction, since for every f ∈ A(K)+ we must have hx, f i = f (x) ≥ 0. Moreover note that
hx, 1K i = 1. We have, up to an isomorphism, K ⊂ {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1}. We will now show that
also the other inclusion holds.
Theorem 3.19. For every state space K we have
K = {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1}

(3.11)

up to an isomorphism.
Proof. We will omit the isomorphism in the proof. Let ψ ∈ {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1} and assume
that ψ ∈
/ K. Then according to the strict hyperplane separation theorem B.10 there is an affine function
f ∈ A(K) such that
hψ, f i < 0 < hx, f i
(3.12)
for all x ∈ K; note that we have used that A(K)∗∗ = A(K) as proved in Proposition B.4, since f should
actually be a functional on A(K)∗ . Also note that f is affine on V = {ϕ ∈ A(K)∗ : hϕ, 1K i = 1} = aff(K).
Since hx, f i = f (x) > 0 for all x ∈ K, we must have f ∈ A(K)+ . Then hψ, f i < 0 is a contradiction with
ψ ∈ A(K)∗+ , so we must have ψ ∈ K.
10

<!-- page 11 -->
One has to be careful when working with a concrete theory, because although K ⊂ A(K)∗+ up to an
isomorphism, one has to take this isomorphism into account when describing states from K by vectors from
V = aff(K) or by vectors from A(K)∗ . It is usually preferred and more useful to describe states as vectors
from A(K)∗ , but note that dim(V ) + 1 = dim(A(K)∗ ) which has to be taken into account.
A standard approach is to do the following: first find a suitable representation of K ⊂ V , this is actually
where we started to build the framework. Then for every x ∈ K, apply the map
 
x
x 7→
(3.13)
1
which simply adds the 1 at the end of the vector representation of every state. Then the set
 

x
K0 =
:x∈K
1

(3.14)

is clearly isomorphic to K and moreover
K 0 = {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1}

(3.15)

even without the isomorphism. We can formalize this as follows:
Proposition 3.20. Let K ⊂ V be a state space, where V = aff(K) then:
(R1) dim(V ) + 1 = dim(A(K)∗ ).
(R2) Let K 0 be as given in (3.14), then K 0 is isomorphic to K.
(R3) K 0 ⊂ A(K)∗ .
(R4) K 0 = {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1}.
Proof. To prove (R1), note that dim(A(K)∗ ) = dim(A(K)), we will show that dim(V ) + 1 = dim(A(K)).
Let 0 ∈ V be the zero vector and let f ∈ A(K), then since f is only affine function, not linear, we can have
f (0) 6= 0. One can see that this is the only difference between affine and linear functions and any affine
function such that f (0) = 0 is actually linear, i.e. if f (0) = 0 then f ∈ V ∗ . It follows that f − f (0)1K ∈ V ∗
and so every f ∈ A(K) can be described as an ordered pair (ϕ, c), where ϕ ∈ V ∗ , ϕ = f − f (0)1K and c ∈ R,
c = f (0). For any arbitrary ordered pair (ϕ, c), let x ∈ K and define
(ϕ, c)(x) = ϕ(x) + c1K (x).

(3.16)

We get that (ϕ, c) ∈ A(K), and so the vector space of ordered pairs (ϕ, c) is isomorphic to A(K). Note that
the vector space of ordered pairs (ϕ, c) has exactly one more dimension that V and so (R1) follows. (R2)
is straightforward, the map described in (3.13) is affine and invertible. To prove (R3), let x ∈ K and let
f ∈ A(K) correspond to the ordered pair (ϕ, c), where ϕ ∈ V ∗ and c ∈ R, then let
 

x
, (ϕ, c) = ϕ(x) + c.
(3.17)
1
Notice that this expression is linear in (ϕ, c) and so elements of K 0 are functionals on A(K), so K 0 ⊂ A(K)∗ .
Finally, to prove (R4), note that K 0 ⊂ {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1} is immediate. We can now use the
strict hyperplane separation theorem B.10 in the same way as in the proof of Theorem 3.19 to show that
K 0 = {ϕ ∈ A(K)∗+ : hϕ, 1K i = 1}.

11

<!-- page 12 -->
3.4. Connection to abstract convex effect algebras and order unit spaces
One does not have to start building the formalism of GPTs from the state space K, but a different
approach is to start with the abstract definition of convex effect algebra. We will show that starting from
abstract effect algebras leads to the order unit spaces. Then, we will then show that the formalism of order
unit spaces is equivalent to our framework.
Definition 3.21. An effect algebra is a system (E, 0, 1, +) where E is a set, 0, 1 ∈ E and + is a partially
defined binary operation. Let a, b ∈ E then we write a ⊥ b if a + b is defined. Let a, b, c ∈ E, then it must
hold that:
(EA1) If a ⊥ b then also b ⊥ a and a + b = b + a.
(EA2) If a ⊥ b and (a + b) ⊥ c then b ⊥ c, a ⊥ (b + c) and (a + b) + c = a + (b + c).
(EA3) For every a ∈ E there is a0 ∈ E such that a ⊥ a0 and a + a0 = 1.
(EA4) If a ⊥ 1 then a = 0.
Effect algebras were defined by Foulis and Bennet in 1994 [111], but equivalent structure of D-posets
was already presented by Kôpka in 1992 [112]. Effect algebras were introduced as a generalization of the
projectors in quantum theory and they were heavily investigated, see [113] for a review. Special class of
effect algebras are convex effect algebras.
Definition 3.22. Let E be an effect algebra. E is convex effect algebra if for every a ∈ E and λ ∈ [0, 1]
there is an element λa ∈ E such that for all λ, µ ∈ [0, 1] and a, b ∈ E we have
(CEA1) µ(λa) = λ(µa).
(CEA2) If λ + µ ≤ 1, then λa ⊥ µa and λa + µa = (λ + µ)a.
(CEA3) If a ⊥ b, then λa ⊥ λb and λa + λb = λ(a + b).
(CEA4) 1a = a.
Special class of convex effect algebras are effect algebras which are intervals in real ordered vector spaces.
As we will see, these effect algebras are closely related to our definition of E(K) as in Definition 3.8.
Proposition 3.23. Let V be a real vector space with a pointed cone C, that is C ∩ −C = {0}. Let v, w ∈ V
and define the partial order ≥ as v ≥ w if and only if v − w ∈ C. This gives V the structure of ordered
vector space, see Proposition A.8. Let u ∈ C then the interval
[0, u] = {v ∈ V : 0 ≤ v ≤ u}

(3.18)

is a convex effect algebra with the partially defined binary operation of sum of vectors and 1 = u. The convex
structure is given by multiplication of vectors by scalars.
Proof. The proof is straightforward. Let a, b ∈ [0, u], then a ⊥ b if and only if a+b ∈ [0, u]. Let a, b, c ∈ [0, u],
then a + b = b + a, and a + b ≤ u if and only if b + a ≤ u. If a + b ≤ u and (a + b) + c ≤ u then we have
b + c ≤ a + b + c ≤ u. We define a0 = u − a as the unique element such that a + a0 = u and a0 ∈ [0, u] if and
only if a ∈ [0, u]. At last if a + u ≤ u then a ≤ 0 but also a ≥ 0 so we must have a = 0. This shows that
[0, u] is an effect algebra.
Keep a, b ∈ [0, u] and let λ, µ ∈ [0, 1]. Clearly we have λ(µa) = λµa = µ(λa). If λ + µ ≤ 1, then
λa + µa = (λ + µ)a ≤ a ≤ u. If a + b ≤ u, then also λa + λb = λ(a + b) ≤ a + b ≤ u. At last, 1a = a is
trivial. This shows that [0, u] is convex effect algebra.
Definition 3.24. Let V be a real vector space with a convex, pointed cone C and let u ∈ C, then we call
[0, u] linear effect algebra.
12

<!-- page 13 -->
The following justifies why we used the term effect algebra in Definition 3.8.
Corollary 3.25. Let K be a state space and let E(K) be the effect algebra over K as given in Definition
3.8. Then E(K) is a linear effect algebra with u = 1K , C = A(K)+ and V = A(K).
Proof. It follows from Proposition 3.13 that we have E(K) = [0, 1K ] ⊂ A(K).
As we have seen, every linear effect algebra is convex effect algebra. The other implication holds as well.
Theorem 3.26. Every convex effect algebra is affinely isomorphic to a linear effect algebra.
Proof. See [114] for the proof.
Thus we see that convex effect algebras are isomorphic to linear effect algebras. We will now proceed
to explain how linear effect algebras are isomorphic to order unit spaces. For a definition of ordered vector
space, see Definition A.4.
Definition 3.27. Order unit space (V, ≤, u) is an ordered vector space (V, ≤) with an order unit u ∈ V ,
which is an element such that for any v ∈ V there is λ ∈ R+ such that v ≤ λu.
Proposition 3.28. There is a one-to-one correspondence between order unit spaces and linear effect algebras.
Proof. We already know that if (V, ≤, u) is an ordered vector space, then
E = [0, u] = {v ∈ V : 0 ≤ v ≤ u}

(3.19)

is a linear effect algebra, see Proposition 3.23. Let now V be a vector space, C ⊂ V a pointed cone,
u ∈ C and consider the linear effect algebra E = [0, u]. Without the loss of generality, we can assume
that V = span(E); if V 6= span(E), then we can replace V and C with V ∩ span(E) and C ∩ span(E).
V = span(E) also implies V = span(cone(E)), see Lemma A.2. It follows that cone(E) is generating, and
so for every v ∈ V there are a, b ∈ E and λ, µ ∈ R+ such that v = λa − µb. We then have
v = λa − µb ≤ λa ≤ λu,

(3.20)

so u is an order unit, and (V, ≤, u) is an order unit space. One can also prove that C = cone(E).
Thus we have showed that building an operational framework based on convex effect algebras, linear
effect algebras and order unit spaces is equivalent. Now we will proceed to show that this is also equivalent
to our framework based on state spaces. Hence one can, without the loss of generality, choose any of the
possible starting points and obtain the same framework. We already know that given a state space K, E(K)
is a linear effect algebra, see Corollary 3.25. We will now show that given a linear effect algebra E, one can
construct a state space S(E), such that E is an effect algebra on S(E), i.e., such that E = E(S(E)).
For simplicity, we will assume that the cone C used to construct a linear effect algebra [0, u] is closed and
generating. If C would not be generating, then we can without the loss of generality restrict to span(C). We
assume that C is closed for the sake of simplicity, but this assumption can also be operationally motivated
as in Definition 2.1.
Definition 3.29. Let V be real, finite-dimensional vector space, C ⊂ V be convex, closed, pointed, and
generating cone. Let u ∈ C be an order unit and let E = [0, u] be a linear effect algebra. Let C ∗ be the
dual cone to C, see Definition B.5, and let
S(E) = {ψ ∈ C ∗ : hψ, ui = 1}.
We call S(E) the state space of E.

13

(3.21)

<!-- page 14 -->
Now we can treat S(E) as a state space, we can construct E(S(E)), that is an effect algebra on S(E).
Using that C ∗∗ = C, see Proposition B.11, one can show that
E(S(E)) = {a ∈ C : 0 ≤ a ≤ u} = E.

(3.22)

And so given a linear effect algebra E, we can construct the state space S(E), but we can also use S(E) to
reconstruct E using (3.22). Hence the framework one would get using linear effect algebras is equivalent to
the framework we get using state spaces.
3.5. Some useful results
In this subsection we will present collection of simple results about state spaces, effect algebras and the
underlying cones. All of these results are easy to prove and we invite the reader to try and do the proofs
themselves.
Lemma 3.30. Let V be a real, finite-dimensional vector space and let KA ⊂ V be a state space. Let KB ⊂ V
be another state space such that span(KB ) = V and
KB ⊂ KA .

(3.23)

E(KA ) ⊂ E(KB ).

(3.24)

Then
Proof. Note that span(KB ) = span(KA ) implies A(KA ) = A(KB ). Let f ∈ E(KA ) and let x ∈ KB . From
KB ⊂ KA we get x ∈ KA and it follows that 0 ≤ hx, f i ≤ 1 and so f ∈ E(KB ).
Lemma 3.31. Let f, g ∈ A(K)+ , then f ≥ g if and only if 1K − g ≥ 1K − f .
Proof. We have f ≥ g if and only if −g ≥ −f if and only if 1K − g ≥ 1K − f .
Lemma 3.32. Let f, g ∈ A(K)+ be such that f ≥ g. If hx, f i = 0 for some x ∈ K, then also hx, gi = 0.
Proof. From f ≥ g we get f − g ≥ 0 and we must have hx, f − gi ≥ 0. Using also g ≥ 0 we get hx, f i ≥
hx, gi ≥ 0. Since hx, f i = 0, we get 0 ≥ hx, gi ≥ 0 and so hx, gi = 0.
Lemma 3.33. Let f, g ∈ E(K) be such that f ≥ g. If hx, gi = 1 for some x ∈ K, then hx, f i = 1.
Proof. Let x ∈ K, then from f ≥ g and f ∈ E(K) we get 1 ≥ hx, f i ≥ hx, gi. If hx, gi = 1, then we have
1 ≥ hx, f i ≥ 1 so we get hx, f i = 1.
Lemma 3.34. For every ψ ∈ A(K)∗+ there is some x ∈ K and λ ∈ R+ such that ψ = λx.
Proof. Let ψ ∈ A(K)∗+ and let x = hψ,11 K i ψ. Then we have x ∈ A(K)∗+ and hx, 1K i and so according to
Theorem 3.19 we have x ∈ K. The result follows from ψ = hψ, 1K ix.
The interpretation of Lemma 3.34 is that K is a base of the cone A(K)∗+ . Let C be a cone, then a base
of C is a convex set B ⊂ C such that for every v ∈ C there are unique x ∈ B and λ ∈ R+ such that v = λx.
Lemma 3.35. For every ψ ∈ A(K)∗ there are x, y ∈ K and λ, µ ∈ R+ such that ψ = λx − µy.
Proof. We know that A(K)∗+ is generating, see Lemma 3.18, so there are ϕ, ξ ∈ A(K)∗+ such that ψ = ϕ−ξ.
According to Lemma 3.34 there are x, y ∈ K and λ, µ ∈ R+ such that ϕ = λx, ξ = µy. The result follows.
Lemma 3.36. Let f ∈ A(K), then f ∈ A(K)+ if and only if hψ, f i ≥ 0 for every ψ ∈ A(K)∗+ .
Proof. One can either use the result of Proposition B.11 that (A(K)∗+ )∗ = A(K)+ , i.e., that the dual cone
of A(K)∗+ is again A(K)+ . Alternatively, using Lemma 3.34 we get that hψ, f i ≥ 0 for all ψ ∈ A(K)∗+ if
and only if hx, f i ≥ 0 for all x ∈ K. But if hx, f i ≥ 0 for all x ∈ K, then f ∈ A(K)+ by definition.
14

<!-- page 15 -->
3.6. Order unit norm, base norm and discrimination tasks
We have been so far avoiding specifying the topology on K, A(K) and A(K)∗ . This was not a burning
issue as we are working with only finite-dimensional vector spaces. We will now introduce the topology by
introducing norms to A(K) and A(K)∗ . We will assume that the reader is familiar with some basic facts
about normed vector spaces, if not, then we recommend [115]. We will start by introducing the norm to
A(K) since it is just the supremum norm for the functions.
Proposition 3.37. Let K be a state space, f ∈ A(K) and define
(3.25)

kf k = sup |hx, f i| ,
x∈K

then k·k is a norm on A(K).
Proof. Assume that kf k = 0, then we have hx, f i = 0 for all x ∈ K since 0 ≤ |hx, f i| ≤ kf k = 0 and f = 0
follows. Let α ∈ R, then clearly
kαf k = sup |αhx, f i| = |α| sup |hx, f i| = |α| kf k
x∈K

x∈K

(3.26)

and so k·k is homogeneous. Finally let f, g ∈ A(K), then we have
kf + gk = sup |hx, f i + hx, gi| ≤ sup |hx, f i| + sup |hy, gi| = kf k + kgk
x∈K

x∈K

y∈K

(3.27)

and so also triangle inequality holds.
The following gives an equivalent expression for the norm on A(K).
Proposition 3.38. Let f ∈ A(K), then
kf k = inf{λ ∈ R+ : −λ1K ≤ f ≤ λ1K }.

(3.28)

Proof. Let f ∈ A(K) and λ ∈ R+ be such that −λ1K ≤ f ≤ λ1K . Then for every x ∈ K we have
−λ ≤ hx, f i ≤ λ, which implies |hx, f i| ≤ λ and it follows that kf k ≤ λ, so we get kf k ≤ inf{λ ∈ R+ :
−λ1K ≤ f ≤ λ1K }. Let x ∈ K, then by definition of the norm k·k we have |hx, f i| ≤ kf k, which is equivalent
to
− kf k hx, 1K i ≤ hx, f i ≤ kf k hx, 1K i.
(3.29)
Since this holds for all x ∈ K, we get − kf k 1K ≤ f ≤ kf k 1K and so we must have inf{λ ∈ R+ : −λ1K ≤
f ≤ λ1K } ≤ kf k.

In every ordered vector space with an order unit one can use the expression on the right hand side of
(3.28) to define an order unit norm. Observe that the order unit norm is defined only using the geometry
of the ordered vector space. Equation (3.28) shows that the supremum norm k·k coincides with the order
unit norm, further strengthening the connection between geometry of A(K) and its relation to K.
The following is an immediate result.
Lemma 3.39. Let f ∈ A(K)+ , then f ∈ E(K) if and only if kf k ≤ 1.
Proof. If f ∈ E(K), then 0 ≤ hx, f i ≤ 1 for all x ∈ K and so kf k ≤ 1. If kf k ≤ 1, then for every x ∈ K we
have −1 ≤ hf, xi ≤ 1, but since f ∈ A(K)+ we have 0 ≤ hx, f i and so we get 0 ≤ hx, f i ≤ 1, which implies
f ∈ E(K).
Since A(K) is now a normed vector space, we can simply introduce the norm to A(K)∗ by using the
standard norm for linear functionals.
15

<!-- page 16 -->
Proposition 3.40. Let K be a state space, ψ ∈ A(K)∗ and define
kψk =

sup
f ∈A(K),kf k≤1

(3.30)

|hψ, f i| ,

then k·k is a norm on A(K)∗ .
Proof. Let ψ ∈ A(K)∗ and let kψk = 0, then we have hψ, f i = 0 for all f ∈ A(K) and so ψ = 0. Let α ∈ R,
then we have
kαψk =
sup
|αhψ, f i| = |α|
sup
|hψ, f i| = |α| kψk
(3.31)
f ∈A(K),kf k≤1

f ∈A(K),kf k≤1

and so k·k is homogeneous. Finally let ψ, ϕ ∈ A(K) , then we have
∗

kψ + ϕk =

sup
f ∈A(K),kf k≤1

|hψ + ϕ, f i| ≤

sup
f ∈A(K),kf k≤1

|hψ, f i| +

sup
f ∈A(K),kf k≤1

|hϕ, f i| = kψk + kϕk

(3.32)

and so k·k is subadditive.
Lemma 3.41. Let ψ ∈ A(K)∗ , then we have
kψk =

sup |hψ, 2f − 1i| .

f ∈E(K)

(3.33)

Proof. Let g ∈ A(K) be such that kgk ≤ 1. According to Proposition 3.38 we have
− 1K ≤ g ≤ 1K
Let now f =

(3.34)

1
(1K + g), then clearly f ∈ A(K). Moreover from (3.34) we get
2
0≤

1
(1K + g) ≤ 1K
2

(3.35)

and so f ∈ E(K). Therefore every g ∈ A(K) such that kgk ≤ 1 can be written as g = 2f − 1K where
f ∈ E(K). We get
kψk =
sup
|hψ, gi| = sup |hψ, 2f − 1K i|
(3.36)
f ∈E(K)

g∈A(K),kgk≤1

which is the desired result.
Also the norm on A(K)∗ has an equivalent geometrical expression.
Proposition 3.42. Let ψ ∈ A(K)∗ , then
kψk =

inf {λ + µ : ψ = λx − µy, x, y ∈ K}

λ,µ∈R+

(3.37)

Proof. We will only lay out the key steps of the proof, see [116] for a complete proof. The key steps are:
show that the expression inf λ,µ∈R+ {λ + µ : ψ = λx − µy, x, y ∈ K} defines a norm on A(K)∗ , then show
that the dual norm on A(K) is the order unit norm, by using the result of Proposition 3.38. One then gets
that k·k is the double dual norm, and it is known that the double dual norm coincides with the original
norm, see [117, Theorem 4.3].
The expression on the right hand side of (3.37) is called base norm and we can introduce it in any ordered
vector space with a fixed base of the positive cone. The base norm is useful, because it has operational
meaning; for x, y ∈ K the norm kx − yk determines the chance of discriminating the states x and y. We
will now define the discrimination task more precisely and we will show exactly how the base norm comes
into play.
16

<!-- page 17 -->
Let x0 , x1 ∈ K be two states and consider the following task: we will be given the state x0 with probability
(or relative frequency) λ ∈ [0, 1] or we will be given the state x1 with probability 1 − λ. Our goal is to
tell which of the states we were given with the highest possible accuracy, i.e., we want to maximize the
probability of our answer being correct. We will call this task the discrimination of x0 and x1 . Note that λ
and 1 − λ are usually referred to as a priori probabilities for x0 and x1 respectively.
We are going to get the answer by performing a ‘yes’-‘no’ measurement in the following sense: given a
state x ∈ {x0 , x1 } we will perform a ‘yes’-‘no’ measurement corresponding to some f ∈ E(K). Then the
probability of ‘yes’ answer is hx, f i and the probability of ‘no’ answer is 1 − hx, f i. If we get the ‘yes’ answer,
we will predict that we were given x = x0 and if we get the ‘no’ answer, we will predict we were given
x = x1 . Note that the assignment of ‘yes’ answer to x0 and ‘no’ to x1 is just a convention, we can also assign
the ‘yes’ answer to x1 and ‘no’ answer to x0 . There are four possible things that may happen: we either
receive x0 or x1 and we either guess x0 or x1 . Given a choice of f ∈ E(K), we can assign probabilities to
all possible outcomes, see Table 1.
guess x0
guess x1

receive x0
hx0 , f i
1 − hx0 , f i

receive x1
hx1 , f i
1 − hx1 , f i

Table 1: Probabilities of the four possible outcomes of the discrimination task of x0 and x1 .

We have to take into account that we will receive x0 with probability λ and x1 with probability 1 − λ,
so for a given f ∈ E(K) the overall success probability psucc (f ) is
psucc (f ) = λhx0 , f i + (1 − λ)(1 − hx1 , f i).

(3.38)

Our goal is to maximize psucc (f ) over all possible choices of f ∈ E(K), we get
psucc =

sup psucc (f ) = (1 − λ) + sup hλx0 − (1 − λ)x1 , f i,

f ∈E(K)

f ∈E(K)

(3.39)

where we have used the bilinearity of h·, ·i, i.e., we have used that λx0 − (1 − λ)x1 ∈ A(K)∗ and so
λhx0 , f i − (1 − λ)hx1 , f i = hλx0 − (1 − λ)x1 , f i. Now we want to rewrite (3.39) in such way that we can use
Lemma 3.41 to express the supremum over f ∈ E(K) as a norm of some functional from A(K)∗ . We get
1
sup (hλx0 − (1 − λ)x1 , 2f − 1i + hλx0 − (1 − λ)x1 , 1i)
2 f ∈E(K)
!
1
= (1 − λ) +
hλx0 − (1 − λ)x1 , 1i + sup hλx0 − (1 − λ)x1 , 2f − 1i
2
f ∈E(K)

psucc = (1 − λ) +

=

1
(1 + kλx0 − (1 − λ)x1 k) .
2

(3.40)
(3.41)
(3.42)

Thus we have proved the following:
Theorem 3.43. Let x0 , x1 ∈ K be two states and consider the task of discriminating between x0 and x1 .
Let λ ∈ [0, 1] and 1 − λ be the a priori probabilities for x0 and x1 respectively, then the maximal probability
of successfully discriminating x0 and x1 is
psucc =

1
(1 + kλx0 − (1 − λ)x1 k) .
2

(3.43)

We see that psucc depends only on the norm kλx0 − (1 − λ)x1 k, which in turn shows that the functional
norm k·k introduced in Proposition 3.40 is principle an observable quantity, not just a mathematical construct. Base norms were used to analyze discrimination tasks in the past, see e.g. [116, 118]. One can also
connect the base norm of kx − yk, where x, y ∈ K, to the task of finding the smallest µ ∈ [0, 1] such that
(1 − µ)x + µx0 = (1 − µ)y + µy 0 for some x0 , y 0 ∈ K, see [119, proof of Theorem 3.2].
17

<!-- page 18 -->
3.7. No-restriction hypothesis and restricted theories
So far we have assumed that every effect from E(K) corresponds to a well-defined ‘yes’-‘no’ question
that, at least in principle, can be experimentally performed. This assumption is in literature called the
no-restriction hypothesis. Theories without the no-restriction hypothesis were recently studied in [120, 121]
and as it was pointed out in [121], it is not trivial to consistently define a theory with restrictions.
A general approach would be to assume that there is a set of effects E ⊂ E(K) and only ‘yes’-‘no’
questions corresponding to effects from E are allowed. For this approach to be consistent, we must have
0, 1K ∈ E and E must be convex, i.e., conv(E) = E. It is usually assumed that E separates states, i.e., that
for every x, y ∈ K there is some f ∈ E such that hx, f i 6= hy, f i.
Since E ⊂ E(K), we also have cone(E) ⊂ A(K)+ . Let cone(E)∗ be the dual cone to cone(E) given as
cone(E)∗ = {ψ ∈ A(K)∗ : hψ, f i ≥ 0, ∀f ∈ E}.

(3.44)

We then have A(K)∗+ ⊂ cone(E)∗ and we can define
S(E) = {ψ ∈ cone(E)∗ : hψ, 1K i = 1}.

(3.45)

S(E) is the state space corresponding to E and we have K ⊂ S(E). We can now see the restricted theory
(K, E) as a pair of state spaces (K, S(E)), such that K ⊂ S(E). The interpretation then is that we can
only prepare states from K, but we can only measure measurements that are well-defined on S(E). In this
sense, we can say that we are either restricted in the states that we can prepare or, equivalently, we can say
that we are restricted in the ‘yes’-‘no’ questions we can ask about the system.
In even more general scenario, one can not only restrict the ‘yes’-‘no’ questions, but also the set of
measurements can have additional restrictions, or the set of allowed transformations can be artificially
restricted. Also one has to make sure that these restrictions are logically consistent in the way that every
transformation is well defined in both Schrödinger picture (as transformation on states) and Heisenberg
picture (as transformation of the effects). For an in-depth treatment of restricted theories see [121].
3.8. Diagrammatic notation
In the upcoming sections we will work with more that one system, we will work with bipartite and tripartite systems, we will work with entangled states and entangled measurements and we will use transformations
that map single systems to bipartite systems and vice-versa. We will use diagrammatic notation to make
the calculations easier to understand, i.e., we will use diagrams to represent some complicated equations.
Diagrammatic notation is often used in frameworks similar to GPTs, see e.g. [32, 44, 90, 104, 105, 122–127].
We are using a modified version of the quantikz library [128] to typeset the diagrams.
Let K be a state space and let x ∈ K, then we will use
(3.46)

x

to represent the equivalence class of preparations corresponding to x. If it will be needed to specify that x
belongs to K, we will use
(3.47)
x
K

In a similar fashion, we will use
f

(3.48)

f

(3.49)

and
K

18

<!-- page 19 -->
to represent f ∈ E(K). For the unit effect 1K ∈ E(K) we will use the symbol
(3.50)
since this is a generalization of the partial trace from quantum theory. We will use
hx, f i =

x

(3.51)

f

In other words, the closed diagram, i.e., the diagram with no free/unconnected legs, corresponds to a
probability computed by pairing the corresponding state and effect. For the unit effect we have
x

(3.52)

= 1.

In a similar fashion, one can define equality between non-closed diagrams: let x, y ∈ K, then x = y is the
same as
x
= y
(3.53)
and for f, g ∈ E(K) we have f = g whenever
f

(3.54)

g

=

One can also introduce equality of non-closed diagrams as follows: note that since x, y ∈ K are equivalence
classes of preparations, then we have x = y whenever hx, f i = hy, f i for all f ∈ E(K). In diagrammatical
notation, this reads:
x

=

y

⇔

x

f

=

y

f , ∀f ∈ E(K).

(3.55)

In other words, two non-closed diagrams are equal whenever all of their possible closures are equal. This is
consistent with our formalism of equivalence classes of preparations, effects and transformations. We will
also use convex combinations of diagrams; for λ ∈ [0, 1] and x, y ∈ K we define
λ x

+ (1 − λ) y

=

λx + (1 − λ)y

(3.56)

In analogical way, one can define convex combinations of effects and transformations and one can again
understand the equality of convex combination of non-closed diagrams as equality of convex combinations
of all possible closures. We will also allow an abuse of the diagrammatical notation and we will also use it
for general elements of A(K) or A(K)∗ . For example, let ϕ ∈ A(K)∗ and α ∈ R, then we can use
α ϕ

(3.57)

to denote αϕ ∈ A(K)∗ .
4. Example: classical theory
In this section we will present the first example theory: classical theory. Classical theory provides the
simplest possible example and so it is easy to grasp, but we will also need classical theory to introduce
19

<!-- page 20 -->
several important concepts, such as measurements and instruments. Also, there are many important results
about classical theory that we will point out in subsequent sections.
A classical theory is a theory where we have n independent pure states and their convex combinations.
If we number the pure states 1, 2, . . . , n, then a classical theory is a theory where every state is a probability
distribution over
Pnthe set {1, . . . , n}, i.e., every state is a set of numbers (p1 , . . . , pn ), pi ∈ R+ for all i ∈
{1, . . . , n} and i=1 pi = 1. One can then see that a state is pure if and only if the corresponding probability
distribution is concentrated at a single point, i.e., pj = 1 for some j ∈ {1, . . . , n} and pi = 0 for i 6= j.
Moreover, it is easy to see that the pure states must be affinely independent and so the state space must be
a simplex; a simplex Sn is a convex hull of affinely independent points.
Let V be a real finite-dimensional vector space, then {v0 , v1 . . . , vk } ⊂ V are affinely independent if
Pk
Pk
the only numbers αi ∈ R, i ∈ {0, 1, . . . , k} such that i=0 αi = 0 and i=0 αi vi = 0 are αi = 0 for all
i ∈ {0, . . . , k}. If {v0 , v1 . . . , vk } are affinely independent, then one can not express any of the vectors vi as
an affine combination of the remaining vectors. Affine independence of {v0 , v1 . . . , vk } is equivalent to linear
independence of {v1 − v0 . . . , vk − v0 }. One can also see that if {v0 , v1 . . . , vk } are affinely independent, then
their affine hull is k-dimensional.
Definition 4.1. Classical theory is a theory where the state space is a simplex Sn , n ∈ N. Any theory
where the state space K is not a simplex will be called non-classical.
Let n ∈ N and let {s1 , s2 . . . , sn } ⊂ V be an affinely indent set of vectors, then
(4.1)

Sn = conv({s1 , . . . , sn })

Pn
is a simplex. For
Pnany x ∈ Sn there are unique numbers λi ∈ R, λi ≥ 0, for all i ∈ {1, . . . , n}, i=1 λi = 1
such that x = i=1 λi si . The uniqueness of the numbers λ1 , . . . , λn follows from affine independence of
{s1 , . . . , sn }. The numbers λ1 , . . . , λn are exactly the probability distribution (p1 , . . . , pn ) corresponding to
the state x ∈ Sn .
The effect algebra E(Sn ) is generated by the functions b1 , . . . , bn that are given as
(4.2)

hsi , bj i = δij
for all i, j ∈ {1, . . . , n}, where δij is the Kronecker delta, defined as
(
1 i=j
δij =
0 i 6= j

(4.3)

The functions b1 , . . . , bn are well-defined,
because {s1 , . . . , sn } are affinely independent.
Pn
Pn Note that for any
other f ∈ A(K) we have f = i=1 hsi , f ibi . This is easy to see, let x ∈ Sn , x = i=1 λi si , then for all
i ∈ {1, . . . , n} we have λi = hx, bi i and so
* n
+
n
n
X
X
X
hx, f i =
λi hsi , f i =
hx, bi ihsi , f i = x,
hsi , f ibi .
(4.4)
i=1

i=1

i=1

It is obvious that f ∈ A(K)+ only if hsi , f i ≥ 0, but it follows that then f is a sum of the functions b1 , . . . , bn
with positive coefficients. Moreover f ∈ E(Sn ) if and only if it is a sum of the functions b1 , . . . , bn with
coefficients from the interval [0, 1]. For example, one has
1Sn =

n
X

bi .

(4.5)

i=1

We will now proceed with exploring the simplest cases. So let n = 1, then S1 = {s} and we have only a
single state. Then b = 1S1 and E(S1 ) = [0, 1] as every f ∈ E(S1 ) is of the form µ1S1 for some µ ∈ [0, 1]. So
S1 is the simplest possible state space as it contains only one state.
20

<!-- page 21 -->
1.2

1.2
S2
s0

1.0

s1

1.0

0.8

0.8

0.6

0.6

0.4

0.4

0.2

0.2

0.0

b0

A(S2 )+

1S 2

b1

0.0
S2
A(S2 )∗+

−0.2
−0.2

0.0

0.2

0.4

0.6

0.8

1.0

−0.2

1.2

(a) Picture of the state space S2 as subset of A(S2 )∗ . The red
points are the pure states s0 and s1 , the blue line is the state
space S2 , and the black lines are the boundary of the positive
cone A(S2 )∗+ .

−1.0

−0.5

0.0

0.5

1.0

(b) Picture of the effect algebra E(S2 ) as subset of A(S2 ). The
red points are the effects b0 , b1 , 1S2 , the blue lines are the
boundary of the effect algebra E(S2 ) and the black lines are
the boundary of the positive cone A(S2 )+ .

Figure 1: Pictures of the state space S2 and effect algebra E(S2 ).

Let n = 2, then the pure states are usually denoted s0 and s1 , S2 is isomorphic to the interval [0, 1] and
the state space corresponds to a classical bit. In this case we can introduce the representation
 
 
0
1
s0 =
,
s1 =
,
(4.6)
1
1
where s0 , s1 ∈ A(S2 )∗ are already represented as functionals. One can pick different representation; we find
these most useful for calculations, but they produce skewed images. For b0 , b1 , 1S2 ∈ E(S2 ) we have
 
 
 
−1
1
0
b0 =
,
b1 =
,
1S2 =
,
(4.7)
1
0
1
where the pairing is given by the usual Euclidean inner product. See Figure 1a for the picture of the state
space S2 and Figure 1b for the picture of the effect algebra E(S2 ).
For n = 3, the pure states are denoted s1 , s2 , s3 and S3 is a triangle. We will use the representation
 
 
 
0
1
0
s1 = 0 ,
s2 = 0 ,
s3 = 1 ,
(4.8)
1
1
1
where s1 , s2 , s3 ∈ A(S3 )∗ are again already represented as the corresponding functionals. For the elements
of E(S3 ) we have
 
 
 
 
−1
1
0
0
b1 = −1 ,
b2 = 0 ,
b3 = 1 ,
1S3 = 0 .
(4.9)
1
0
0
1
Note that the extreme points of E(S3 ) are not only b1 , b2 , b3 , 1S3 and 0, but also b1 + b2 , b2 + b3 , b3 + b1 . See
Figure 2a for the picture of the state space S3 and Figure 2b for the picture of the effect algebra E(S3 ).
21

<!-- page 22 -->
S3

E(S3 )

A(S3 )∗+

A(S3 )+

b1
s1
s3

1.2

s2

1.4

b3 + b1

b1 + b2

1.2

1.0

1.0

0.8

0.8

0.6

0.6

1S 3

0.4

0.4

0.2

0.2
0.0
0.0 0.2

0.4 0.6

0.8 1.0
1.2 1.4

0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4

b3

b2

−1.0
−0.5
0.0

0.0
−1.0

(a) Picture of the state space S3 as subset of A(S3 )∗ . The red
points are the pure states s1 , s2 and s3 , the blue lines are the
edges of the state space S3 , and the black lines are the edges of
the positive cone A(S3 )∗+ .

b2 + b3
−0.5

0.0

0.5
0.5

1.0

1.0
1.5

1.5

(b) Picture of the effect algebra E(S3 ) as subset of A(S3 ). The
red points are the effects b1 , b2 , b3 , b1 + b2 , b2 + b3 , b3 + b1 ,
1S2 , blue lines are the edges of the effect algebra E(S3 ), and the
black lines are the edges of the positive cone A(S3 )+ .

Figure 2: Pictures of the state space S3 and effect algebra E(S3 ).

For n = 4, the pure states are
 
0
0

s1 = 
0 ,
1

 
1
0

s2 = 
0 ,
1

 
0
1

s3 = 
0 ,
1

which are plotted in Figure 3. The effect algebra E(S4 ) is generated by
 
 
 
 
0
0
1
−1
0
1
0
−1




b4 = 
b3 = 
b1 = 
b2 = 
1 ,
0 ,
−1 ,
0 ,
0
0
0
1

 
0
0

s4 = 
1 ,
1

(4.10)

 
0
0

1S4 = 
0 .
1

(4.11)

One can again see that the extreme points of E(S4 ) include not only b1 , b2 , b3 , b4 , 1S4 , 0 but also bi + bj for
i 6= j and bi + bj + bk for i 6= j 6= k 6= i, for i, j, k ∈ {1, . . . , 4}.
5. Tensor products
In this section we will introduce the concept of bipartite and multipartite systems. The idea is simple:
given state spaces KA and KB , we want to describe an experiment with two parties; traditionally called Alice
and Bob. In the simplest scenario Alice prepares xA ∈ KA , applies fA ∈ E(KA ) and Bob prepares xB ∈ KB ,
applies fB ∈ E(KB ). Since both of the experiments are independent, the resulting joint probability for
both Alice and Bob is a product of the respective probabilities, i.e., they both get the outcome ‘yes’ with
probability hxA , fA ihxB , fB i. In a more complex scenario, the preparation procedures of Alice and Bob
can be correlated. Alice and Bob meet before the experiment and toss an unbiased coin, and based on
the outcome prepare their states. For example if the coin lands on heads, Alice will prepare xA and Bob
will prepare xB , but if the coin lands on tails, Alice will prepare yA and Bob will prepare yB . This is a
valid preparation procedure and we have to have a way of describing it; we refer to this scenario as shared
22

<!-- page 23 -->
S4
s4

1.0
0.8
0.6
s1

0.4
0.2

s3
s2
0.0

0.0

0.2
0.0

0.4
0.2

0.4

0.6
0.6

0.8

0.8
1.0

1.0

Figure 3: Pictures of the state space S4 as subset of V = aff(S4 ). The red points are the pure states s1 , s2 , s3 and s4 , and the
blue lines are the edges of the state space S4 .

randomness, because the outcome of the coin toss is random information shared between Alice and Bob.
In the most general scenario, Alice and Bob can share an entangled state, which can not be prepared using
shared randomness.
5.1. Bipartite scenarios
Our aim si to find a state space KAB that will describe the bipartite scenario within our current framework. We will introduce several axioms that will fix basic properties of the bipartite state space.
Definition 5.1. A bipartite state space KAB formed from state spaces KA and KB must satisfy:
(BP1) KAB must be a valid state space.
(BP2) For every xA ∈ KA and xB ∈ KB , there must be a bipartite state in KAB that describes the situation
where Alice prepares xA and Bob prepares xB . Moreover, the identification of the bipartite state
with xA and xB is affine, meaning that if Alice (or Bob) prepares a mixture of states x1,A and x2,A ,
then this results in a mixture of the respective bipartite states with the same coefficients.
(BP3) For every fA ∈ E(KA ) and fB ∈ E(KB ), there must be a bipartite effect in E(KAB ) that describes
the situation where Alice applies fA and Bob applies fB . Moreover, the identification of the bipartite
effect with fA and fB is linear, meaning that if Alice (or Bob) prepares a mixture or sum of effects
f1,A and f2,A , then this results in a mixture or sum of the respective bipartite effects.
(BP4) The unit effect on KAB is equivalent to Alice applying 1KA and Bob applying 1KB .
(BP5) For every xAB , yAB ∈ KAB there are fA ∈ E(KA ), fB ∈ E(KB ) such that when Alice and Bob
prepare xAB and apply fA and fB respectively, then the resulting probability is different from the
experiment where Alice and Bob prepare yAB and apply fA and fB respectively. In other words,
applying effects locally is sufficient to distinguish all of the states in KAB .
23

<!-- page 24 -->
Note that (BP2) together with the convexity coming from (BP1) implies that correlated preparations
based on shared randomness between Alice and Bob are included in KAB . Similar result follows for ‘yes’‘no’ questions that are performed based on shared randomness between Alice and Bob. To get more tangible
results, we will use a well-know result from linear algebra that the dual of the vector space of bilinear forms
is a tensor product of the original vector spaces, see [129] or Appendix C. Consider first the scenario where
Alice applies fA ∈ E(KA ) and Bob applies fB ∈ E(KB ). Mathematically speaking, fA is a linear functional
on A(KA )∗ and fB is a linear functional on A(KB )∗ , since A(KA )∗∗ = A(KA ) and A(KB )∗∗ = A(KB ), see
Proposition B.4. It then follows that the joint operation of Alice applying fA and Bob applying fB must
behave as a bilinear functional on pairs of states.
Let xAB ∈ KAB , then according to Theorem 3.19 xAB is a linear functional on effects from E(KAB ).
According to (BP3), pairs of effects fA and fB must be included in E(KAB ). When acting on pairs of effects,
xAB is essentially a bilinear functional and so according to Proposition C.8 every xAB must correspond to
an element of A(KA )∗ ⊗ A(KB )∗ . According to (BP5) every xAB must be uniquely characterized by its
action on pairs of effects, therefore every xAB must be equivalent to an element of A(KA )∗ ⊗ A(KB )∗ . Thus
we have proved the following:
Lemma 5.2. If KAB satisfies (BP1) - (BP5), then
KAB ⊂ A(KA )∗ ⊗ A(KB )∗ .

(5.1)

We are now going to construct the possible range of bipartite state spaces KAB . This is only a possible
range, because, as we will shortly see, KAB in general is not uniquely specified by the choices of KA and
KB . Let xA ∈ KA and xB ∈ KB , then according to (BP2) the pair of states must be represented in KAB .
Following the result of Lemma 5.2, we are going to postulate that the state corresponding to Alice preparing
xA and Bob preparing xB is xA ⊗ xB . By using (BP2) we get the smallest possible candidate for KAB .
Definition 5.3. The minimal tensor product of state spaces KA and KB is given as
˙ KB = conv ({xA ⊗ xB : xA ∈ KA , xB ∈ KB }) .
KA ⊗

(5.2)

˙ KB is a valid state space, i.e., that it is a compact convex subset of a
One should check that KA ⊗
˙ KB clearly is convex and it clearly is a subset of a real, finitereal, finite-dimensional vector space. KA ⊗
˙ KB is compact, simply note that by definition KA ⊗
˙ KB is
dimensional vector space. To see that KA ⊗
˙
˙
closed and one can easily see that KA ⊗ KB is bounded, hence KA ⊗ KB is compact.
The counterpart to minimal tensor product is the maximal tensor product, that will be the largest
possible candidate for KAB . The maximal tensor product will be introduced with the help of (BP3) as
largest possible set of states that is positive on pairs of effects. But to do so, we must first introduce
the description for pairs of effects. For fA ∈ E(KA ) and fB ∈ E(KB ) we are going to denote the effect
corresponding to Alice applying fA and Bob applying fB as fA ⊗ fB . Then, analogical to the minimal tensor
product of states, we get the minimal tensor product of effect algebras, given as
E(KA ) ˙
⊗ E(KB ) = conv ({fA ⊗ fB : fA ∈ E(KA ), fB ∈ E(KB )}) .

(5.3)

˙ E(KB ) is a valid effect algebra, i.e., that it is an interval in
One should in principle check whether E(KA ) ⊗
an order unit space. One can easily do this by verifying that E(KA ) ˙
⊗ E(KB ) is a linear effect algebra, as
introduced in Definition 3.24.
Definition 5.4. The maximal tensor product of state spaces KA and KB is given as
ˆ KB = S(E(KA ) ⊗
˙ E(KB )),
KA ⊗

(5.4)

ˆ KB = {ϕ ∈ A(KA )∗ ⊗ A(KB )∗ :hϕ, fA ⊗ fB i ≥ 0, ∀fA ∈ E(KA ), ∀fB ∈ E(KB ),
KA ⊗

(5.5)

which the same as
hϕ, 1KA ⊗ 1KB i = 1}
24

<!-- page 25 -->
ˆ KB is a state space by construction, since it was defined in (5.4) as the state space corresponding
KA ⊗
˙ E(KB ). Analogically to the maximal tensor product of state spaces, we can
to the effect algebra E(KA ) ⊗
define the maximal tensor product of effect algebras as
(5.6)

ˆ E(KB ) = E(KA ⊗
˙ KB )
E(KA ) ⊗

= {ψ ∈ A(KA ) ⊗ A(KB ) : 0 ≤ hxA ⊗ xB , ψi ≤ 1, ∀xA ∈ KA , ∀xB ∈ KB }.

(5.7)

ˆ KB includes way more states than KA ⊗
˙ KB and so it must be
One may be temped to think that KA ⊗
ˆ KB has a very
way more useful in information-theoretic tasks, but this is not the case. Even though KA ⊗
ˆ
˙
rich structure, the corresponding effect algebra E(KA ⊗ KB ) = E(KA ) ⊗ E(KB ) contains only separable
effects, i.e., effects of the form fA ⊗ fB for fA ∈ E(KA ) and fB ∈ E(KB ) and their sums and convex
combinations. It was observed in [1, Section VII.] that if we have access to only separable effects, then we
can not implement neither teleportation nor superdense coding protocols. It was also observed in [35–37]
ˆ KB is trivial. We also
that for certain classes of state spaces, the set of reversible transformations on KA ⊗
want to express KAB as some form of tensor product of KA and KB . For this reason, we will change the
˜ KB instead of KAB .
notation; from now on we will use KA ⊗
˜ KB the state space corresponding
Definition 5.5. Let KA and KB be state spaces, then we will denote KA ⊗
to the bipartite scenario.
We will also denote

˜ E(KB ) = E(KA ˜
E(KA ) ⊗
⊗ KB ).

(5.8)

˜ is not a single object, but it is a placeholder for a rule
Note that the tensor product of state spaces ⊗
˜ is usually not defined on all possible state spaces,
that has to be specified by a given theory. In practice, ⊗
but only on a selected class of state spaces that are included in a given theory. For example, in quantum
theory, we use a special rule for the quantum tensor product which is strictly different from the minimal
and maximal tensor products, see Section 8. The quantum tensor product is constructed with the use of
the underlying Hilbert spaces. For a general state space K, there is no underlying Hilbert space and so it
is not clear how to extend the quantum tensor product to a general K. But this is not a problem, because
quantum theory is defined only in terms of quantum state spaces.
˜ KB does not have an established name within the framework of GPTs. That
The tensor product KA ⊗
is because in most applications it is sufficient to consider only bipartite scenarios and so the notation KAB
is often used. But, as we will see, the notation KA ˜
⊗ KB is easier to work with in multipartite scenarios.
Proposition 5.6. For any valid bipartite state we must have
˙ KB ⊂ KA ⊗
˜ KB ⊂ KA ⊗
ˆ KB .
KA ⊗

(5.9)

˙ KB ⊂ KA ⊗
˜ KB follows from (BP2), because every xAB ∈ KA ⊗
˙ KB can be written
Proof. Note that KA ⊗
PN
PN
as xAB = i=1 λi yi,A ⊗ yi,B , where yi,A ∈ KA , yi,B ∈ KB , λi ∈ R+ for all i ∈ {1, . . . , N } and i=1 λi = 1.
It follows from (BP2) that yi,A ⊗ yi,B ∈ KAB ; xAB ∈ KAB follows by the convexity of KAB .
˜ KB and fA ∈ E(KA ), fB ∈ E(KB ). According to (BP3) fA ⊗ fB must be a well defined
Let xAB ∈ KA ⊗
effect on KAB , i.e., we must have fA ⊗ fB ∈ E(KAB ). So we must have hxAB , fA ⊗ fB i ≥ 0. It follows from
ˆ KB .
(BP4) that hxAB , 1KA ⊗ 1KB i = 1 and so from (5.5) we get xAB ∈ KA ⊗
Corollary 5.7. We have
˙ E(KB ) ⊂ E(KAB ) ⊂ E(KA ) ˆ
E(KA ) ⊗
⊗ E(KB ).

(5.10)

Proof. The result follows from Proposition 5.6 and Lemma 3.30, since we have
˙ E(KB ) = E(KA ˆ
E(KA ) ⊗
⊗ KB ),
ˆ E(KB ) = E(KA ˙
E(KA ) ⊗
⊗ KB ).
25

(5.11)
(5.12)

<!-- page 26 -->
At last, we will introduce the concepts of separable and entangled states and we will discuss our constructions.
˙ KB are called separable states. The states from KA ⊗
˜ KB \KA ⊗
˙ KB ,
Definition 5.8. The states from KA ⊗
˜
i.e., the states from KA ⊗ KB that are not separable, are called entangled states.
One can, of course, ask whether we actually need all of the axioms (BP1) - (BP5). (BP1) is necessary, as
˜ KB is a state space. (BP2) and (BP3) are in some sense dual to each other and
it only ensures that KA ⊗
their goals are only to allows the natural scenarios where Alice and Bob do not interact and are unaware of
˜ E(KB ) can be
each others existence. One could in principle drop (BP4), since the unit effect of E(KA ) ⊗
˜
fixed by its action on separable states and this yields the unit effect of E(KA ) ⊗ E(KB ) to be 1KA ⊗ 1KB if
separable states are generated by states of the form xA ⊗ xB for xA ∈ KA , xB ∈ KB . But one can also use
(BP4) more explicitly to start the construction from order unit spaces corresponding to the effect algebras
E(KA ) and E(KB ), hence we keep it in the list of assumptions.
At last, one can discuss (BP5). This assumption is often called tomographic locality or local distinguishability and it was used as an axiom for the derivation of quantum theory in [89]. Without (BP5) we can
have states in KAB that contain information hidden to Alice and Bob and which is only available when you
can manipulate the whole state. It is being discussed whether physical theories should obey tomographic
locality and theories without tomographic locality are actively researched [130, 131].
5.2. Multipartite scenarios
In this section, we will investigate what additional assumptions one needs to make to describe scenarios
including more than two parties. So let KA , KB , KC be state spaces. How do we then define the tripartite
˜ KB and then add
state space KABC ? Clearly one option is to first form the bipartite state space KA ⊗
˜ KB ) ⊗
˜ KC . Other option is to first form KB ˜
KC , so that we get (KA ⊗
⊗ KC and then add KA to obtain
˜ KC ). It is natural to require that both of these construction yield the same result.
KA ˜
⊗(KB ⊗
˜ must be associative, i.e., we must have
Definition 5.9. The tensor product of state spaces ⊗
˜ KB ) ⊗
˜ KC = KA ⊗(K
˜ B⊗
˜ KC ).
(KA ⊗

(5.13)

We are now going to do three things: as first, we are going to show that if the tensor product of state
spaces is associative, then so is the tensor product of effect algebras. Then we will prove that both the
˙ and the maximal tensor product ⊗
ˆ are associative. Finally, we are going to show
minimal tensor product ⊗
a list of five identities that follow from the associativity of ˜
⊗ and that correspond to the pentagon diagram
in category theory.
Proposition 5.10. Let KA , KB , KC be state spaces. If ˜
⊗ is an associative tensor product of state spaces,
then we have
˜ E(KB )) ⊗
˜ E(KC ) = E(KA ) ˜
˜ E(KC )).
(E(KA ) ⊗
⊗(E(KB ) ⊗
(5.14)
Proof. We have
˜ E(KB )) ⊗
˜ E(KC ) = E(KA ⊗
˜ KB ) ⊗
˜ E(KC ) = E((KA ⊗
˜ KB ) ⊗
˜ KC )
(E(KA ) ⊗
˜ KC )
= E(KA ˜
⊗(KB ˜
⊗ KC )) = E(KA ) ˜
⊗ E(KB ⊗
˜ E(KC )).
= E(KA ) ˜
⊗(E(KB ) ⊗

(5.15)
(5.16)
(5.17)

Proposition 5.11. The minimal tensor product ˙
⊗ is associative.
Proof. Let KA , KB , KC be state spaces. Denote
˙ KB ⊗
˙ KC = conv ({xA ⊗ xB ⊗ xC : xA ∈ KA , xB ∈ KB , xC ∈ KC }.)
KA ⊗
26

(5.18)

<!-- page 27 -->
We clearly have
˙ KB ) ⊗
˙ KC ⊂ KA ⊗
˙ KB ˙
(KA ⊗
⊗ KC ,
˙ KC ) ⊂ KA ˙
KA ˙
⊗(KB ⊗
⊗ KB ˙
⊗ KC ,

(5.19)
(5.20)

˙ KB ) ˙
˙ KC ).
which one can show by simply writing out the general element of (KA ⊗
⊗ KC and KA ˙
⊗(KB ⊗
Let xABC ∈ KA ˙
⊗ KB ˙
⊗ KC , then
xABC =

N
X
i=1

λi yi,A ⊗ yi,B ⊗ yi,C

(5.21)

Pn
for some yi,A ∈ KA , yi,B ∈ KB , yi,C ∈ KC , λi ∈ R+ for i ∈ {1, . . . , N } and i=1 λi = 1. Then xABC ∈
˙ KC since yi,A ⊗ yi,B ∈ KA ⊗
˙ KB and yi,C ∈ KC . Also xABC ∈ KA ˙
(KA ˙
⊗ KB ) ⊗
⊗(KB ˙
⊗ KC ) as yi,A ∈ KA
˙ KC . So we have
and yi,B ⊗ yi,C ∈ KB ⊗
˙ KB ) ⊗
˙ KC = KA ⊗
˙ KB ⊗
˙ KC = KA ⊗(K
˙ B⊗
˙ KC ).
(KA ⊗

(5.22)

Corollary 5.12. The maximal tensor product of effect algebras is associative.
ˆ E(KB ) = E(KA ˙
Proof. The result follows from E(KA ) ⊗
⊗ KB ) and Proposition 5.10.
Proposition 5.13. The maximal tensor product ˆ
⊗ is associative.
Proof. By definition, we have
ˆ KB ) ⊗
ˆ KC = {ϕ ∈ A(KA )∗ ⊗ A(KB )∗ ⊗ A(KC )∗ :hϕ, fAB ⊗ fC i ≥ 0,
(KA ⊗
˙ E(KB ), ∀fC ∈ E(KC ), (5.23)
∀fAB ∈ E(KA ) ⊗
hϕ, 1KA ⊗ 1KB ⊗ 1KC i = 1}.
˙ E(KB ) can be written as a convex combination of the elements of the form fA ⊗ fB ,
Since fAB ∈ E(KA ) ⊗
where fA ∈ E(KA ) and fB ∈ E(KB ), we get
ˆ KC = {ϕ ∈ A(KA )∗ ⊗ A(KB )∗ ⊗ A(KC )∗ :hϕ, fA ⊗ fB ⊗ fC i ≥ 0,
(KA ˆ
⊗ KB ) ⊗
∀fA ∈ E(KA ),

∀fB ∈ E(KB ),

(5.24)

∀fC ∈ E(KC ),

hϕ, 1KA ⊗ 1KB ⊗ 1KC i = 1}.

˙ E(KC ) for all fB ∈ E(KB ) and fC ∈ E(KC ), we get
It follows that since fB ⊗ fC ∈ E(KB ) ⊗
ˆ KC = {ϕ ∈ A(KA )∗ ⊗ A(KB )∗ ⊗ A(KC )∗ :hϕ, fA ⊗ fBC i ≥ 0,
(KA ˆ
⊗ KB ) ⊗

˙ E(KB ), (5.25)
∀fA ∈ E(KA ), ∀fBC ∈ E(KB ) ⊗
hϕ, 1KA ⊗ 1KB ⊗ 1KC i = 1}.

One can see that the right hand side of (5.25) is exactly the definition of KA ˆ
⊗(KB ˆ
⊗ KC ) and so the result
follows.
Corollary 5.14. The minimal tensor product of effect algebras is associative.
˙ E(KB ) = E(KA ˆ
Proof. The result follows from E(KA ) ⊗
⊗ KB ) and Proposition 5.10.
27

<!-- page 28 -->
˜ it holds
Proposition 5.15. Let KA , KB , KC , KD be state spaces. For a tensor product of state spaces ⊗
that
˜ KD ) = KA ˜
˜ KD )) = KA ˜
˜ KC ) ⊗
˜ KD )
(KA ˜
⊗ KB ) ˜
⊗(KC ⊗
⊗(KB ˜
⊗(KC ⊗
⊗((KB ⊗
˜ KD = ((KA ˜
˜ KC ) ⊗
˜ KD
= (KA ˜
⊗(KB ˜
⊗ KC )) ⊗
⊗ KB ) ⊗

(5.26)
(5.27)

which can be also written as the following diagram of equalities:
˜ KB ) ⊗(K
˜ C⊗
˜ KD )
(KA ⊗

˜ KD ))
KA ˜
⊗(KB ˜
⊗(KC ⊗

˜ KB ) ˜
˜ KD
((KA ⊗
⊗ KC ) ⊗

˜
˜ KC ) ⊗
˜ KD )
KA ⊗((K
B⊗

(5.28)

˜ B⊗
˜ KC )) ⊗
˜ KD
(KA ⊗(K

Proof. The result follows by repeated application of (5.13).
The importance of Proposition 5.15 is hidden in (5.28). (5.28) corresponds to the pentagon diagram that
is key in defining monoidal categories. Monoidal categories are very general mathematical structures that
generalize tensor products of various objects. Our current framework can be formulated as a category of
˜ gives it the structure of a monoidal
state spaces and (5.28) shows that the tensor product of state spaces ⊗
˜
category. There is a slight caveat: as we have already explained, ⊗ does not have to be defined for all state
spaces, but only for selected state spaces. Therefore, to be more precise, one can show that a collection of
˜ is defined is a monoidal category. From now on we will assume that the
selected state spaces for which ⊗
˜
tensor product ⊗ is associative and always defined whenever needed.
5.3. Diagrammatic notation for multipartite scenarios
We will now explain, how to use diagrammatic notation in multipartite scenarios. So let xA ∈ KA and
xB in KB , then we will use
xA
xB

KA

(5.29)

KB

˜ KB . We will use
to denote the state xA ⊗ xB ∈ KA ⊗
yAB KA
KB

28

(5.30)

<!-- page 29 -->
˜ KB . Similarly for effects, we will use
to denote a general yAB ∈ KA ⊗
fA

KA

(5.31)

fB

KB

˜ E(KB ). We will use
to denote the state fA ⊗ fB ∈ E(KA ) ⊗
KA

gAB

(5.32)

KB

˜ E(KB ). For yAB ∈ KA ⊗
˜ KB and gAB ∈ E(KA ) ⊗
˜ E(KB ) we then have
to denote a general gAB ∈ E(KA ) ⊗
yAB KA

gAB

KB

= hyAB , gAB i.

(5.33)

In the future, we will mostly omit the wire labels that specify the respective state spaces.
5.4. Partial trace and monogamy of entanglement
˜ KB and let fB ∈ E(KB ). Can we define
Let KA , KB be state spaces, let xAB ∈ KA ⊗
xAB

fB

(5.34)

and does it have any meaning? We will first show that the object in (5.34) has a valid mathematical meaning,
then we will proceed with proving some of its properties as well as more general results about entanglement.
Note that the inline equivalent of object in (5.34) is (idKA ⊗fB )(xAB ), i.e.,
xAB

fB

= (idKA ⊗fB )(xAB ),

(5.35)

where idKA denotes the identity map idKA : A(KA )∗ → A(KA )∗ and fB si now treated as a linear map
fB : A(KB )∗ → R. Then idKA ⊗fB is a linear map idKA ⊗fB : A(KA )∗ ⊗ A(KB )∗ → A(KA )∗ .
The object in (5.34) has an unused output wire in the KA system, so for any gA ∈ E(KA ) we can
construct
gA
xAB
= hxAB , gA ⊗ fB i.
(5.36)
fB
In other words, the object in (5.34) behaves as a functional on A(KA ) and so we must have
xAB

fB

∈ A(KA )∗ .

(5.37)

To better demonstrate our point, assume that xAB = yA ⊗ yB for some yA ∈ KA and yB ∈ KB . We then
have
yA
xAB
=
= hyB , fB i yA
.
(5.38)
yB
fB
fB
29

<!-- page 30 -->
Since A(KA )∗ ⊗ A(KB )∗ = span({yA ⊗ yB : yA ∈ KA , yB ∈ KB }, it follows that we can also define the
object in (5.34) by writing xAB as linear combination (with possibly non-positive coefficients) of product
states yA ⊗ yB and using (5.38). Let us summarize the results so far.

˜ KB and let yi,A ∈ KA , yi,B ∈ KB , αi ∈ R for i ∈ {1, . . . , N } be such
Proposition 5.16. Let xAB ∈ KA ⊗
PN
that xAB = i=1 αi yi,A ⊗ yi,B . Let fB ∈ E(KB ) and let ϕA ∈ A(KA )∗ be given for gA ∈ A(KA ) as
(5.39)

hϕA , gA i = hxAB , gA ⊗ fB i.
Then we have
xAB
Proof. Let x =

=

fB

N
X
i=1

ϕA

(5.40)

αi hyi,B , fB i yi,A

(5.41)

αi hyi,B , fB i yi,A

=

PN

i=1 αi yi,A ⊗ yi,B , then we have

xAB

fB

=

N
X

yi,A
αi

i=1

=

yi,B

fB

N
X
i=1

and so we have proved the first equality in (5.40). To prove the second equality, first note that if ψ1 , ψ2 ∈
A(K)∗ are such that for all f ∈ A(K) we have hψ1 , f i = hψ2 , f i then ψ1 = ψ2 . Moreover, it is sufficient to
check the equality only for all f ∈ E(K), since A(K) = span(E(K)). So now let gA ∈ E(KA ), then we have
gA

xAB

fB

= hxAB , gA ⊗ fB i = hϕA , gA i

(5.42)

and the second equality in (5.40) follows.
One can easily prove many other results similar to Proposition 5.16, such as:
˜ KB ⊗
˜ KC and fC ∈ E(KC ), then
1. Let xABC ∈ KA ⊗

xABC

∈ A(KA )∗ ⊗ A(KB )∗ .

(5.43)

∈ A(KB ).

(5.44)

∈ A(KC ) ⊗ A(KA )∗ .

(5.45)

fC
˜ E(KB ), then
2. Let xA ∈ KA and fAB ∈ E(KA ) ⊗
xA
fAB

˜ KB and fBC ∈ E(KB ) ⊗
˜ E(KC ), then
3. Let xAB ∈ KA ⊗
xAB
fBC

30

<!-- page 31 -->
˜ KB and fB ∈ E(KB ) and note that for gA ∈ E(KA ) we have
Let again xAB ∈ KA ⊗
gA

xAB

fB

= hxAB , gA ⊗ fB i ≥ 0.

(5.46)

∈ A(KA )∗+

(5.47)

So we get
xAB

fB

from which the next result easily follows.
˜ KB and fB ∈ E(KB ), then there is yA ∈ KA such that
Proposition 5.17. Let xAB ∈ KA ⊗
xAB

= hxAB , 1KA ⊗ fB i yA

fB

(5.48)

Proof. We already know that for every ϕ ∈ A(K)∗+ there must exist yA ∈ KA and λ ∈ R+ such that
ϕ = λyA , see Lemma 3.34. So from (5.47) we get
xAB

fB

(5.49)

= λ yA

for some λ ∈ R+ . By applying the unit effect to the free leg, we get
= λ yA

xAB

=λ

(5.50)

fB
which concludes the proof.
˜ KB , then
Corollary 5.18. Let xAB ∈ KA ⊗
xAB

∈ KA .

(5.51)

Proof. Follows from Proposition 5.17.
The process of applying the unit effect to one leg of a bipartite state xAB ∈ KA ˜
⊗ KB , i.e., the map
xAB

7→

xAB

(5.52)

is called partial trace. The name comes from quantum theory, where this construction corresponds to
the partial trace over a subspace of the Hilbert space. Partial trace is an important concept, because it
describes the local state that Alice (or Bob) have at their disposal when they work with the bipartite state
˜ KB . Partial trace is also a key concept in monogamy of entanglement, which is the following
xAB ∈ KA ⊗
result.
31

<!-- page 32 -->
˜ KB be such that
Theorem 5.19. Let xAB ∈ KA ⊗
xAB

=

(5.53)

yA

where yA is a pure state. Then xAB = yA ⊗ zB for some zB ∈ KB , i.e.,
yA

xAB

=

(5.54)

zB

Proof. The proof can be found in [17, Lemma 3.]. We will provide exactly the same proof, only formulated
in the language presented so far. Let fB ∈ E(KB ), then also 1KB − fB ∈ E(KB ), see Lemma 3.15. We have
xAB

=

xAB

fB

+ xAB

1KB − fB

(5.55)

which one can check by applying gA ∈ E(KA ) to the free leg and observing, that the equality holds.
According to Proposition 5.17 we must have
xAB

= hxAB , 1KA ⊗ fB i zA

(5.56)

= hxAB , 1KA ⊗ (1KB − fB )i wA

(5.57)

fB

and
xAB

1KB − fB

for some zA , wA ∈ KA . So we have
xAB

= hxAB , 1KA ⊗ fB i zA

+ hxAB , 1KA ⊗ (1KB − fB )i wA

(5.58)

= hxAB , 1KA ⊗ fB i zA

+ (1 − hxAB , 1KA ⊗ fB i) wA

(5.59)

Using (5.53) we get
yA

Since yA is a pure state, we must have zA = wA = yA . This is an important point, because in general wA
and zA would depend on the choice of fB , but since yA is a pure state, we have zA = wA = yA , and so for
all fB ∈ E(KB ) we get the same zA and wA . Let us denote
xAB

=

32

zB

(5.60)

<!-- page 33 -->
where zB ∈ KB . Let now gA ∈ E(KA ), then using (5.56) we get
xAB

gA
fB

= hxAB , 1KA ⊗ fB i yA

gA

=

yA

gA

zB

fB

(5.61)

where we have used that

hxAB , 1KA ⊗ fB i =

xAB

=

zB

fB

(5.62)

fB

It follows from (5.61) that for any gA ∈ E(KA ) and fB ∈ E(KB ) we have
hxAB , gA ⊗ fB i = hyA ⊗ zB , gA ⊗ fB i

(5.63)

and so we must have xAB = yA ⊗ zB as a result of tomographic locality of the tensor product.
5.5. Existence of entanglement
We have already argued that the minimal and maximal tensor products are the smallest possible and
largest possible choice of the bipartite state space. In Proposition 5.6 we showed that for any two state
˙ KB ⊂ KA ⊗
ˆ KB . If we would have KA ⊗
˙ KB = KA ⊗
ˆ KB , then the choice of
spaces KA , KB , we have KA ⊗
the bipartite state space would be unique, but also all bipartite states would be separable and there would
˜ KB . It is intuitive to expect that entanglement does not exist in classical
be no entangled states in KA ⊗
theory. One can easily prove the following, slightly more general result.
Proposition 5.20. Let K be a state space and let Sn be a simplex, i.e., a classical state space. Then
˙ K = Sn ⊗
ˆ K.
and Sn ⊗

(5.64)

˙ Sn = K ⊗
ˆ Sn .
K⊗

˙ Sn = K ⊗
ˆ Sn then also Sn ˙
ˆ K because the definitions of minimal and
Proof. Clearly if K ⊗
⊗ K = Sn ⊗
maximal tensor products are symmetric. So let Sn = conv({s1 , . . . , sn }) be a simplex with pure states
s1 , . . . , sn . Let b1 , . . . , bn ∈ E(Sn ) be the effects such that hsi , bj i = δij for all i, j ∈ {1, . . . , n}. Also
∗
remember that {s1 , . . . , sn } is a basis of A(Sn )P
and {b1 , . . . , bn } is a basis of A(Sn ). Let y ∈ K ˆ
⊗ Sn , then
n
there are {v1 , . . . , vn } ⊂ A(K)∗ such that y = i=1 vi ⊗ si , see Lemma C.5. Since we have
y

K

=
Sn

vi

K

(5.65)

bi

it follows from Proposition 5.17 that vi ∈ A(K)∗+ , i.e., vi = λi xi for some xi ∈ K, λi ∈ R+ for all
i ∈ {1, . . . , n}. So we have
n
X
˙ Sn .
y=
λi xi ⊗ si ∈ K ⊗
(5.66)
i=1

˙ Sn , from which the result follows.
Hence we have proved that K ˆ
⊗ Sn ⊂ K ⊗
One can now ask, whether Proposition 5.20 gives also sufficient condition for non-existence of entangled
states. This problem was in the context of tensor products of the underlying cones already investigated in
[132, 133] but it was only recently solved in [134].
˙ KB = KA ˆ
Theorem 5.21. Let KA , KB be state spaces, then we have KA ⊗
⊗ KB if and only if at least
one of the state spaces is a simplex, i.e., if and only if we have KA = Sn or KB = Sn .
Proof. See [134].
33

<!-- page 34 -->
6. Channels, measurements and instruments
We finally get to describe transformations of systems. There are in principle three different types of
transformations: channels, measurements and instruments. Channels map states to states and they describe
some manipulation of the system, e.g., time-evolution. Measurements map states of a given system to
probability distributions over measurement outcomes, they describe the measurement process in the sense
that they give us the probabilities of occurrence of the outcomes. Instruments describe the measurement
process by mapping a state to weighted set of post-measurement states.
We will argue that measurements and instruments are special kinds of channels. This may appear as
counter-intuitive at first, since physically channels and measurements are different object. We already know
from Section 4 that probability distributions correspond to classical state spaces, and so measurement as a
map from states to probability distributions can be described as a channel from a given state space K to
˜ Sn .
classical state space Sn . Similarly, instruments can be described as channels from K to K ⊗
6.1. Channels
Channel is a transformation of a system that can be either appended to a preparation procedure, or
prepended to a measurement procedure, such that mixtures are preserved. Let us unpack this statement:
since channel should transform a state to something measurable, it must map states of one system to states
of other system. Moreover, we require that channels preserve mixtures, which just implies that a channel is
an affine map between state spaces.
Definition 6.1. Let KA , KB be state spaces. Channel Φ from KA to KB is an affine map Φ : KA → KB ,
i.e., for all xA , yA ∈ KA and λ ∈ [0, 1] we have
Φ(λxA + (1 − λ)yA ) = λΦ(xA ) + (1 − λ)Φ(yA ).

(6.1)

We will denote the set of all channels Φ : KA → KB by C(KA , KB ). We will use the shorthand C(K) for
channels Φ : K → K, i.e., C(K) = C(K, K).
Since A(KA )∗ = span(KA ) and A(KB )∗ = span(KB ), we can easily extend Φ to a linear map Φ :
A(KA )∗ → A(KB )∗ as follows: let vA ∈ A(KA )∗ , then according to Lemma 3.35 we have vA = λxA − µyA
for some xA , yA ∈ KA and λ, µ ∈ R+ . Then we have Φ(vA ) = λΦ(xA ) − µΦ(yA ). One can check that then
Φ : A(KA )∗ → A(KB )∗ is a linear map. Since Φ : A(KA )∗+ → A(KB )∗+ , the map Φ is called positive. We
will now present examples of channels one can find in every GPT.
Example 6.2. Let K be a state space and let idK ∈ C(K) be the identity map, given as idK (x) = x
for all x ∈ K. It is straightforward to check that idK is a channel and that the induced linear map
idK : A(K)∗ → A(K)∗ is positive linear map. idK is usually called the identity map, the identity channel,
or just identity.
Example 6.3. Let KA , KB be state spaces, let xB ∈ KB be a fixed state and define a channel τx ∈ C(KA , KB )
as τx (yA ) = xB for all yA ∈ KA . To see that τx is a channel, we need to verify that it is affine. So let
yA , zA ∈ KA , λ ∈ [0, 1], then we have
λτx (yA ) + (1 − λ)τx (zA ) = λxB + (1 − λ)xB = xB = τx (λyA + (1 − λ)zA )

(6.2)

and so τx is affine and a channel. τx is usually called the constant channel. When extended to a linear map
τx : A(KA )∗ → A(KB )∗ , we get τx (vA ) = hvA , 1KA ixB for vA ∈ A(KA )∗ . This is easy to derive, for every
vA ∈ A(KA )∗ there are yA , zA ∈ KA and λ, µ ∈ R+ such that vA = λyA − µzA and by linearity we get
τx (vA ) = τx (λyA − µzA ) = λτx (yA ) − µτx (zA ) = (λ − µ)xB
and the result follows from hvA , 1KA i = λ − µ.
34

(6.3)

<!-- page 35 -->
˜ KB , KA ) be the partial trace map,
Example 6.4. Let KA , KB be state spaces and let idKA ⊗1KB ∈ C(KA ⊗
˜
i.e., for xAB ∈ KA ⊗ KB we have
xAB KA 7→

idKA ⊗1KB :

xAB

KB

KA

(6.4)

KB

To see that idKA ⊗1KB is a channel note that we have already showed that (idKA ⊗1KB )(xAB ) ∈ KA in
˜ KB , λ ∈ [0, 1] and
Corollary 5.18, we only need to argue that idKA ⊗1KB is affine. So let xAB , yAB ∈ KA ⊗
fA ∈ E(KA ), then
(6.5)

h(idKA ⊗1KB )(λxAB + (1 − λ)yAB ), fA i = hλxAB + (1 − λ)yAB , fA ⊗ 1KB i

(6.6)

= λhxAB , fA ⊗ 1KB i + (1 − λ)hyAB , fA ⊗ 1KB i

= λh(idKA ⊗1KB )(xAB ), fA i + (1 − λ)h(idKA ⊗1KB )(yAB ), fA i
(6.7)

and so
(6.8)

(idKA ⊗1KB )(λxAB + (1 − λ)yAB ) = λ(idKA ⊗1KB )(xAB ) + (1 − λ)(idKA ⊗1KB )(yAB )
follows.

Lemma 6.5. Let Φ1 , Φ2 ∈ C(KA , KB ) be channels and let λ ∈ [0, 1], then also their convex combination
λΦ1 + (1 − λ)Φ2 , given for xA ∈ KA as (λΦ1 + (1 − λ)Φ2 )(xA ) = λΦ1 (xA ) + (1 − λ)Φ2 (xA ) is also a channel.
Proof. Let xA ∈ KA , since Φ1 , Φ2 are channels, we have Φ1 (xA ) ∈ KB and Φ2 (xA ) ∈ KB , so λΦ1 (xA ) +
(1 − λ)Φ2 (xA ) ∈ KB follows by convexity of KB . So λΦ1 + (1 − λ)Φ2 ∈ C(KA , KB ), it is straightforward to
verify that λΦ1 + (1 − λ)Φ2 is also affine.
Example 6.6. Let x ∈ K be a fixed point and let τx ∈ C(K) be the corresponding constant channel and let
λ ∈ [0, 1], then we have λ idK +(1 − λ)τx ∈ C(K), given for y ∈ K as (λ idK +(1 − λ)τx )(y) = λy + (1 − λ)x.
We will use

KA

Φ

(6.9)

KB

to denote the channel Φ ∈ C(KA , KB ). Let xA ∈ KA , then
Φ(xA )

=

xA

Φ

(6.10)

denotes the state Φ(xA ) ∈ KB . Note that for channels Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KB , KC ) we will use
Φ1

Φ2

Φ2 ◦ Φ1

=

(6.11)

where Φ2 ◦ Φ1 ∈ C(KA , KC ), (Φ2 ◦ Φ1 )(xA ) = Φ2 (Φ1 (xA )) for xA ∈ KA , i.e. we use ◦ to denote the
composition (also called concatenation) of channels. The identity channel idK ∈ C(K) will be represented
by a plain wire, i.e.,
=

idK

(6.12)

Let Φ ∈ C(KA , KB ) and fB ∈ E(KB ), then we can construct
Φ

fB
35

∈ E(KA ).

(6.13)

<!-- page 36 -->
The object in (6.13) belongs to E(KA ) because for every xA ∈ KA we have
xA

Φ

fB

=

Φ

fB

=

Φ(xA )

fB

∈ [0, 1]

(6.14)

since Φ(xA ) ∈ KB . We will denote
Φ∗ (fB )

(6.15)

where Φ∗ : E(KB ) → E(KA ) is the induced map. One can easily check that it extends to a linear map
Φ∗ : A(KB ) → A(KA ).
Definition 6.7. Let Φ ∈ C(KA , KB ) be a channel, then the adjoint map Φ∗ : E(KB ) → E(KA ) is a linear
map defined by (6.15), or equivalently, Φ∗ : E(KB ) → E(KA ) is the unique linear map such that for all
xA ∈ KA and fB ∈ E(KB ) we have
hΦ(xA ), fB i = hxA , Φ∗ (fB )i.

(6.16)

We already said that a channel can be seen both as appending instruction to preparations, but also
as prepending instructions to measurements. The original channel Φ ∈ C(KA , KB ) was mapping states
to states and so it was appending instructions to a preparation procedure; we usually refer to this as the
Schrödinger picture. The adjoint map Φ∗ : E(KB ) → E(KA ) is prepending instructions to measurement
procedures; we usually refer to this as the Heisenberg picture. Both of the maps Φ and Φ∗ are different
descriptions of the same thing. The following is an important and often used result about the adjoint map
of a channel.
Proposition 6.8. Let KA , KB be state spaces and let Φ ∈ C(KA , KB ) be a channel. Then the adjoint map
Φ∗ : E(KA ) → E(KB ) is unital, i.e., we have Φ∗ (1KB ) = 1KA .
Proof. Let xA ∈ KA , then we have
hxA , Φ∗ (1KB )i = hΦA (xA ), 1KB i = 1

(6.17)

and so we must have Φ∗ (1KB ) = 1KA .
We will now construct a useful mathematical representation of channels. Let Φ ∈ C(KA , KB ). Since Φ
can be extended to a linear map Φ : A(KA )∗ → A(KB )∗ , it follows from Proposition C.8 that this linear
map corresponds to a vector from A(KA ) ⊗ A(KB )∗ . And so, by omitting the isomorphism, we can write
Φ ∈ A(KAP
) ⊗ A(KB )∗ . It then follows that there are gi,A ∈ A(KA ) and wi,B ∈ A(KB )∗ , i ∈ {1, . . . , n} such
n
that Φ = i=1 gi,A ⊗ wi,B . Then for vA ∈ A(KA )∗ and fB ∈ A(KB ) we have
hΦ(vA ), fB i =

n
X
hvA , gi,A ihwi,B , fB i.

(6.18)

i=1

It follows that for vA ∈ A(KA )∗ we have
n
X
Φ(vA ) =
hvA , gi,A iwi,B .

(6.19)

i=1

For xA ∈ KA and fB ∈ E(KB ) we get hΦ(xA ), fB i ≥ 0 which means that Φ ∈ A(KA ) ⊗ A(KB )∗ must be
positive in some sense. We can use this property together with Proposition 6.8 to characterize all channels
as s subset of A(KA ) ⊗ A(KB )∗ .
36

<!-- page 37 -->
Proposition 6.9. Let KA , KB be state spaces, then
ˆ A(KB )∗+ : Φ∗ (1KB ) = 1KA },
C(KA , KB ) = {Φ ∈ A(KA )+ ⊗

(6.20)

where
ˆ A(KB )∗+ = {v ∈ A(KA )⊗A(KB )∗ : hv, xA ⊗fB i ≥ 0, ∀xA ∈ A(KA )∗+ , ∀fB ∈ A(KB )+ }. (6.21)
A(KA )+ ⊗
ˆ A(KB )∗+ . Let xA ∈ KA ,
Proof. We will first prove that if Φ ∈ C(KA , KB ) is a channel, then Φ ∈ A(KA )+ ⊗
fB ∈ E(KB ), then we have
hΦ, xA ⊗ fB i = hΦ(xA ), fB i ≥ 0,
(6.22)

where we have used the isomorphism between linear maps and elements of tensor product, see Proposition
ˆ A(KB )∗+ and since we already know that Φ∗ (1KB ) = 1KA , see
C.8. It follows that we have Φ ∈ A(KA )+ ⊗
Proposition 6.8, we get
ˆ A(KB )∗+ : Ψ∗ (1KB ) = 1KA }.
Φ ∈ {Ψ ∈ A(KA )+ ⊗
(6.23)
+ ˆ
∗+
∗
Now let Φ ∈ A(KA ) ⊗ A(KB ) be such that Φ (1KB ) = 1KA , and let xA ∈ KA . Then we can define
vB ∈ A(KB )∗ as the unique element such that for all fB ∈ E(KB ) we have
(6.24)

hvB , fB i = hΦ, xA ⊗ fB i.

We have hvB , fB i ≥ 0 and so vB ∈ A(KB ) . Moreover we also have hvB , 1KB i = 1 and so it follows from
Theorem 3.19 that vB ∈ KB . Hence we can define Φ(xB ) = vB and so Φ corresponds to a map KA → KB ;
one can easily check that Φ defined like this is affine map. So it follows that Φ ∈ C(KA , KB ).
∗+

The result above is extremely important, because it shows that we can treat the set of channels C(KA , KB )
as a state space. One can easily check that C(KA , KB ) is a base of a positive cone A(KA )+ ˆ
⊗ A(KB )∗+ ∩
span(C(KA , KB )). This is an important result, because it follows that if we would be interested in, for
example, discrimination of channels, we can use the result of Theorem 3.43. It also follows that we do not
have to develop a separate theory of channels, or a separate theory of superchannels, that is maps that map
channels to channels, all of these theories are already included in our formalism.
B
be simplexes, given by their extreme points
Corollary 6.10. Let SnA , Sm

SnA = conv({s1,A , . . . , sn,A }),

SnB = conv({s1,B , . . . , sm,B }).

(6.25)

Then
and for sA ∈ SnA we have

B
B ∗+
˙ A(Sm
B}
C(SnA , Sm
) = {Φ ∈ A(SnA )+ ⊗
) : Φ∗ (1SnA ) = 1Sm

Φ(sA ) =

n X
m
X
i=1 j=1

(6.26)
(6.27)

νij hsA , bi,A isj,B ,

wherePbi,A ∈ E(Sn ) are the functions such that hbi,A , sk,A i = δik for i, k ∈ {1, . . . , n}. νij ∈ R+ are such
m
that j=1 νij = 1 for all i ∈ {1, . . . , n}.
Proof. (6.26) follows from Propositions 6.9 and 5.20. Note that

B
˙ A(Sm
A(SnA ) ⊗
) = conv cone({bi,A ⊗ sj,B : i ∈ {1, . . . , n}, j ∈ {1, . . . , m}}),

so we must have
Φ=

m
n X
X
i=1 j=1

We then have
Φ∗ (1SnB ) =

n X
m
X
i=1 j=1

A =
Since we must have Φ∗ (1SnB ) = 1Sm

(6.29)

νij bi,A ⊗ sj,B .

νij hsj,B , 1SnB ibi,A =

Pn

i=1 bi,A , we get

37

Pm

n X
m
X
i=1 j=1

j=1 νij = 1.

(6.28)

νij bi,A

(6.30)

<!-- page 38 -->
6.2. Measurements
As we have already pointed out, measurements are maps that map states to probability distributions; we
will consider only probability distributions over finitely many possible outcomes. We have already discussed
in Section 4 that such probability distributions are in one-to-one correspondence with states on a classical
state space Sn . Hence a measurement is a channel from a state space K to Sn .
Definition 6.11. n-outcome measurement is a channel m ∈ C(K, Sn ).
We will simply use the word measurement when the number of outcomes will not be important. We
immediately have the following:
˙ A(Sn )∗+ , where
Proposition 6.12. Let m ∈ C(K, Sn ) be a measurement, then m ∈ A(K)+ ⊗
˙ A(Sn )∗+ = conv cone({f ⊗ s : f ∈ E(K), s ∈ Sn }).
A(K)+ ⊗

(6.31)

ˆ A(Sn )∗+ = A(K)+ ˙
Proof. The result follows from Proposition 6.9, since we must have A(K)+ ⊗
⊗ A(Sn )∗+
which follows from Proposition 5.20.
Let s1 , . . . , sn be the pure states in Sn , so that we have Sn = conv({s1 , . . . , sn }) and A(Sn )∗+ =
span({s1 , . . . , sn }). Let m ∈ C(K, Sn ) be a measurement, then according to Proposition 6.12 there must be
fi ∈ E(K), i ∈ {1, . . . , n} such that
n
X
fi ⊗ si .
(6.32)
m=
i=1

Then for x ∈ K we have
m(x) =

n
X
hx, fi isi .

(6.33)

i=1

According
Pn to Proposition 6.8 we must have hm(x), 1Sn i = 1, which implies
and so i=1 fi = 1Sn . Thus we have proved the following

Pn

i=1 hx, fi i = 1 for all x ∈ K

Proposition 6.13.
Pn n-outcome measurement m ∈ C(K, Sn ) is uniquely defined by effects {f1 , . . . , fn } ⊂
E(K) such that i=1 fi = 1Sn .
Proof. The only thing that remains to be proved is the uniqueness of the set {f1 , . . . , fn }. Let {b1 , . . . , bn } ⊂
E(Sn ) be the effects such that hsi , bj i = δij for all i, j ∈ {1, . . . , n}. Let m ∈ C(K, Sn ) and let x ∈ K, then
we have hx, m∗ (bi )i = hm(x), bi i = hx, fi i and so fi = m∗ (bi ), where m∗ is adjoint map of m. So fi is
uniquely given by m.
The result above shows an equivalence between our operational definition of a measurement and the
definition that is often used in quantum information theory, where measurements are often introduced as
collections of effect. It follows from Proposition 6.13 that the two definitions are equivalent and we can
without loss of generality
either describe a measurement as a collection
Pn
Pn f1 , . . . , fn , where fi ∈ E(K), for
i ∈ {1, . . . , n} and i=1 fi = 1K , or as a map m : K → Sn , m(x) = i=1 fi (x)si .
Let n = 2 and consider the two-outcome measurement, i.e., channels m2 ∈ C(K, S2 ). In this case, m2 is
uniquely specified by the two effects {f, g} ⊂ E(K). Since we must have f +g = 1K , we have g = 1K −f and
so m2 is uniquely specified by f, 1K − f , or equivalently, m2 is uniquely specified by a choice of f ∈ E(K).
Hence we get:
Corollary 6.14. The set of two-outcome measurements is isomorphic to E(K).
This was an expected result, because we have introduced E(K) as the set of classes of equivalence of
all possible ‘yes’-‘no’ questions. A ‘yes’-‘no’ question is nothing else than a two-outcome measurement with
some labels assigned to the outcomes. And so the result above only shows that our framework is consistent.
38

<!-- page 39 -->
6.3. Instruments
Consider the scenario where we are not only interested in the statistics of a measurement, but also in
the post-measurement state, that is in the state of the system after performing the measurement. There
are several things to consider: the map from input state to post-measurement state should be a channel,
because the post-measurement state has to be a well-defined state. But the map from input state to postmeasurement state can depend on the outcome of the measurement; for example in quantum theory it
is natural that the post-measurement state is described by an eigenvector corresponding to the observed
eigenvalue.
˜ K) that describes the measurement and the
Definition 6.15. Instrument is a channel I ∈ C(K, Sn ⊗
resulting post-measurement state.
One can clearly generalize an instrument to the case when post-measurement state belongs to a different
˜ KB ). In diagrammatic notation, an instrument I is
system, in that case it would be I ∈ C(KA , Sn ⊗
represented as
(6.34)

I Sn
K

P
˜ K and so we have I(x) = nj=1 λj sj ⊗ yj
Let x ∈ K and let I : K → Sn be an instrument, then I(x) ∈ Sn ⊗
Pn
where s1 , . . . , sn are the extreme points of Sn , λj ∈ R+ , yj ∈ K for all j ∈ {1, . . . , n} and j=1 λj = 1. We
then have
x

bj

Sn

I

(6.35)

= λ j yj

K

where bj ∈ E(Sn ) is the effect such that hsk , bj i = δjk for all k ∈ {1, . . . , n}. Denote
bj

Sn

I

(6.36)

Ij

=

K

then I j : K → A(K)∗+ is a map that maps state from K to elements of A(K)∗+ . The maps I j are exactly
the maps that assign the post-measurement state to an input state x and the normalization hI j (x), 1K i = λi
is exactly the probability of measuring the outcome j. Note that

I Sn

=

(6.37)

Φ

K

where Φ ∈ C(K) is a channel and we clearly have Φ =
I

Sn

Pn

=

j=1 I j . Moreover

(6.38)

m

K

where m ∈ C(K, Sn ) is a measurement and for x ∈ K we have m(x) =
that we can express I as
n
X
I=
sj ⊗ I j

Pn

j=1 hI j (x), 1K isj .

j=1

and for x ∈ K we have I(x) =

Pn

j=1 sj ⊗ I j (x). Thus we have proved the following:

39

So it follows
(6.39)

<!-- page 40 -->
Proposition 6.16. Every instrument I : K → Sn ⊗ K isP
of the form given by (6.39), i.e., there are affine
n
maps I j : K → cone(K) for j ∈ {1, . . . , n} such that I = j=1 sj ⊗ I j .
Another way to prove Proposition 6.16 would be to use Propositions 6.9 and 5.20. Note that some
authors call the maps P
I j instruments and instead of working with I they define a collection of instruments
n
I 1 , . . . , I n , such that j=1 I j is a channel. These two approaches are equivalent.
6.4. Preparations, measure-and-prepare channels
So far, we have identified states and preparation procedures, but one can actually describe preparation
procedures as channels P ∈ C(S1 , K). Note that S1 = {s} and so the channel acts as P(s) = x for some
x ∈ K. It immediately follows that that the set of all preparations C(S1 , K) is isomorphic to K.
Extending the idea of preparations, one can define a conditional preparation as channel P ∈ C(Sn , K).
A conditional preparation P ∈ C(Sn , K) is essentially a device that can prepare n different states and the
classical input determines, which of the n states will be prepared. Analogically to the result of Proposition
6.13, one can easily prove that for every conditional preparation P ∈ C(Sn , K), there are states x1 , . . . , xn ∈
K such that for s ∈ Sn we have
n
X
P(s) =
hs, bi ixi .
(6.40)
i=1

Preparations and conditional preparations are thus dual to effects and measurements, but they are often
not discussed because measurements are more often used in practical applications.
Let P ∈ C(Sn , KB ) be a conditional preparation and let m ∈ C(KA , Sn ) be a measurement, then we can
construct
m
(6.41)
P K = K ΦMP K
K
S
A

n

B

A

B

where ΦMP ∈ C(KA , KB ) is a channel.
Definition 6.17. Let ΦMP ∈ C(KA , KB ) be channel of the form given by (6.41), i.e., such that there are
m ∈ C(KA , Sn ) and P ∈ C(Sn , KB ) such that ΦMP = P ◦m, then we call ΦMP measure-and-prepare channel.
We will later see that not all channels are measure-and-prepare. One can easily prove the following
structural result for measure-and-prepare channels:
Proposition 6.18. Let ΦMP be measure-and-prepare channel, thenPthere are effects f1 , . . . , fn ∈ E(K) and
n
states x1 , . . . , xn ∈ K such that for any y ∈ K we have ΦMP (y) = i=1 hy, fi ixi .
Pn
Proof. Let ΦMP be given as in (6.41).
Pn According to Proposition 6.13 we have m(y) = i=1 hy, fi isi and
according to (6.40) we have P(s) = i=1 hs, bi ixi . Then for any y ∈ K we have
!
n
n
X
X
ΦMP (y) = P
hy, fi isi =
hy, fi ixi .
(6.42)
i=1

i=1

Corollary 6.19. Any measurement m ∈ C(K, Sn ) is a measure-and-prepare channel.
Proof. The only trick needed to prove the result is to take P ∈ C(Sn , Sn ) to be the conditional preparation
given as P(si ) = si for all i ∈ {1, . . . , n}, in other words P = idSn .
Corollary 6.20. Let τx ∈ C(KA , KB ) be a constant channel as in Example 6.3, i.e., for all yA ∈ KA we
have τx (yA ) = xB . Then τB is measure-and-prepare.
Proof. We already know that we have τx (yA ) = hyA , 1KA ixB which just implies that τx = P 1 ◦m1 , where
m1 ∈ C(KA , S1 ) is the trivial, single-outcome measurement given as m1 (yA ) = hyA , 1KA is, where S1 = {s},
and P 1 ∈ C(S1 , KB ) is the preparation P 1 (s) = xB .
40

<!-- page 41 -->
6.5. Completely-positive channels
So far we have only considered channels acting on a single system, but in principle we can also apply
˜ KB and let Φ ∈ C(KB , KC ), then we
channels to parts of larger systems. For example let xAB ∈ KA ⊗
should be allowed to construct
xAB

KA

= (idKA ⊗Φ)(xAB ).

Φ KC
KB

(6.43)

∗+
It is rather simple to define the object in (6.43) mathematically:
Pn we know that there are yi,A ∈ A(KA ) ,
yi,B ∈ A(KB )∗+ and αi ∈ R, i ∈ {1, . . . , n} such that xAB = i=1 αi yi,A ⊗ yi,B . Then, by linearity, we get

(idKA ⊗Φ)(xAB ) =

n
X
i=1

αi yi,A ⊗ Φ(yi,B ).

(6.44)

˜ KC , which is a new requirement that we have not taken
We should require that (idKA ⊗Φ)(xAB ) ∈ KA ⊗
into account so far.
Definition 6.21. Let Φ ∈ C(KB , KC ) be a channel, then we say that Φ is completely positive (or CP
˜ KB → KA ⊗
˜ KC , if for all xAB ∈ KA ˜
for short) with respect to KA ⊗
⊗ KB we have (idKA ⊗Φ)(xAB ) ∈
˜ KC , i.e., if idKA ⊗Φ ∈ C(KA ⊗
˜ KB , KA ˜
KA ⊗
⊗ KC ).
It is known that not all channels are completely positive, a well-known example is the partial transposition
map in quantum theory. Also note that a channel Φ : KB → KC is sometimes called positive map, because
it preserves the positivity of elements of A(KB )∗+ . One has to be careful to not mistake positivity and
complete positivity as these are two different notions.
˜ KB and KA ⊗
˜ KC is the
One has to be careful with respect to what choice of tensor products KA ⊗
˜ is
complete positivity defined. In quantum theory and in general in theories where the tensor product ⊗
fixed, we usually implicitly assume that complete positivity is defined with respect to the chosen tensor
˜ But since in general there is no unique choice of ⊗,
˜ we have to always specify with respect to
product ⊗.
what choice of tensor product we are defining complete positivity. We will now prove several results about
positivity and complete positivity of channels.
Proposition 6.22. The identity channel idKB ∈ C(KB ) is completely positive with respect to any choice of
˜ i.e., with respect to any KA ⊗
˜ KB → KA ⊗
˜ KB .
tensor product ⊗,
˜ KB , then we have (idKA ⊗ idKB ) ∈ C(KA ⊗
˜ KB ) and (idKA ⊗ idKB )(xAB ) = xAB ,
Proof. Let xAB ∈ KA ⊗
from which the result immediately follows.
˜ KB →
Proposition 6.23. A measurement m ∈ C(KB , Sn ) is completely positive with respect to any KA ⊗
˜
KA ⊗ KC .
Pn
˜ KB , then
Proof. Let m be given as m = i=1 fi ⊗ si . Let xAB ∈ KA ⊗
n
X

(idKA ⊗fi )(xAB ) ⊗ si

(6.45)

hxAB , 1KA ⊗ fi iyi ⊗ si ∈ KA ˙
⊗ Sn

(6.46)

(idKA ⊗m)(xAB ) =

i=1

and according to Proposition 5.17 we get
(idKA ⊗m)(xAB ) =

n
X
i=1

where yi ∈ KA , i ∈ {1, . . . , n}.
41

<!-- page 42 -->
Corollary 6.24. All measure-and-prepare channels ΦMP ∈ C(KB , KC ) are completely positive with respect
˜ KB → KA ⊗
˜ KC .
to any KA ⊗
Proof. Since by definition ΦMP = P ◦m, where m ∈ C(KB , Sn ) is a measurement and P ∈ C(Sn , KC ) is a
conditional preparation, the result follows from Proposition 6.23.
Complete positivity of measurements and measure-and-prepare channels is not surprising, since measurements and measure-and-prepare channels are entanglement-breaking channels.
˜ KB → KA ⊗
˜ KC
Definition 6.25. Channel Φ ∈ C(KB , KC ) is entanglement-breaking with respect to KA ⊗
˜
if for any KA and xAB ∈ KA ⊗ KB we have
xAB

˙ KC ,
= (idKA ⊗Φ)(xAB ) ∈ KA ⊗

Φ

(6.47)

i.e., (idKA ⊗Φ)(xAB ) is always a separable state.
˜ KB → KA ˜
Lemma 6.26. Let Φ ∈ C(KB , KC ) be entanglement-breaking channel with respect to KA ⊗
⊗ KC .
˜ KB → KA ˜
Then Φ is completely positive with respect to KA ⊗
⊗ KC .
Proof. The result follows from KA ˙
⊗ KC ⊂ KA ˜
⊗ KC .
So far we have shown that some channels are completely positive for any tensor product KA ˜
⊗ KB , now
we will investigate complete positivity with respect to the minimal and maximal tensor products. These
˜ KB affects complete positivity of channels.
results will showcase that the choice of the tensor product KA ⊗
˙ KB → KA ˙
Proposition 6.27. Let Φ ∈ C(KB , KC ), then Φ is completely positive with respect to KA ⊗
⊗ KC .
˙ KB , then there are λi ∈ [0, 1], xi,A ∈ KA , xi,B ∈ KB for
Proof. The proof siPsimple. Let yAB ∈ KA ⊗
Pn
n
i ∈ {1, . . . , n} and i=1 λi = 1 such that yAB = i=1 λi xi,A ⊗ xi,B and we have
(idKA ⊗Φ)(yAB ) =

n
X
i=1

λi xi,A ⊗ Φ(xi,B ) ∈ KA ˙
⊗ KC .

(6.48)

ˆ KB → KA ˆ
Proposition 6.28. Let Φ ∈ C(KB , KC ), then Φ is completely positive with respect to KA ⊗
⊗ KC .
Proof. Let xAB ∈ KA ˆ
⊗ KB , let fA ∈ E(KA ) and fC ∈ E(KC ), then we have
fA

xAB
Φ

fC

=

xAB

fA
Φ∗ (fC )

≥ 0,

(6.49)

ˆ KC .
because Φ∗ : E(KC ) → E(KB ). It then follows that (idKA ⊗Φ)(xAB ) ∈ KA ⊗
The last result may look strange at first, as one would expect that the more entangled states there
are, the bigger the difference between positive and completely positive maps will be. But this is not the
case and the underlying reason is that a channel Φ ∈ C(KB , KC ) is completely positive with respect to
˜ KB → KA ˜
KA ⊗
⊗ KC if and only if the adjoint map Φ∗ : E(KC ) → E(KB ) is completely positive with
˜ KC ) → E(KA ⊗
˜ KB ). In the case of complete positivity of Φ ∈ C(KB , KC ) with rerespect to E(KA ⊗
ˆ KB → KA ⊗
ˆ KC , the adjoint map Φ∗ is needed to be completely positive with respect to
spect to KA ⊗
˙ E(KB ), which is easy to show analogically to the proof of Proposition 6.27.
E(KA ) ˙
⊗ E(KC ) → E(KA ) ⊗
42

<!-- page 43 -->
6.6. Post-processing preorder of channels
In this section we are going to introduce the post-processing preorder of quantum channels. The main
idea is simple: let KA , KB , KC be state spaces and let Φ ∈ C(KA , KB ), Ψ ∈ C(KA , KC ), Λ ∈ C(KB , KC ) be
channel. Let
=
(6.50)
Ψ
Φ
Λ
Then we can say that Φ is a better channel then Ψ, because we can always obtain Ψ from Φ. We will
formalize this in the following definition.
Definition 6.29. Let KA , KB , KC be state spaces and let Φ ∈ C(KA , KB ), Ψ ∈ C(KA , KC ) be channels.
The we say that Ψ is a post-processing of Φ and we write
(6.51)

Ψ≺Φ
if there is a channel Λ ∈ C(KB , KC ) such that (6.50) holds.

If we restrict only to channels Φ ∈ C(K), then the post-processing relation gives rise to a preorder.
Proposition 6.30. The post-processing relation ≺ is an preorder on the set of channel mapping K to K,
i.e., C(K).
Proof. We need to prove that ≺ is reflexive, i.e., that Φ ≺ Φ and transitive, i.e. that Φ1 ≺ Φ2 and Φ2 ≺ Φ3
implies Φ1 ≺ Φ3 . Let Φ ∈ C(K), then clearly Φ ≺ Φ as we have Φ = Φ ◦ idK and so ≺ is reflexive. To
show that ≺ is transitive, let Φ1 , Φ2 , Φ3 ∈ C(K) be such that Φ1 ≺ Φ2 and Φ2 ≺ Φ3 . Then there are
Λ1 , Λ2 ∈ C(K) such that
Φ1

=

Φ2

Λ1

(6.52)

Φ2

=

Φ3

Λ2

(6.53)

Φ2

Λ1

=

Φ3

and
We get
Φ1

=

Λ2

Λ1

(6.54)

and Φ1 ≺ Φ3 follows.
One of the important results of the post-processing preorder is that it showcases an important difference
between channels and measurements: while a post-processing greatest channel exists for every state space
K, post-processing greatest measurement exists only if K is a simplex. A post-processing greatest channel
Φ ∈ C(K) is a channel such that if Φ ≺ Ψ for some Ψ ∈ C(K), then also Ψ ≺ Φ. The identity channel
idK ∈ C(K) is post-processing greatest and the proof is immediate. We will postpone the proof that
post-processing greatest measurement exist if and only if K is a simplex to Section 7.
Proposition 6.31. Let Φ ∈ C(KA , KB ), then Φ ≺ idKA , and so idKA ∈ C(KA ) is a post-processing greatest
channel in C(KA , KB ) for any state space KB .
Proof. We have Φ = idKA ◦Φ and so the result follows.
7. Compatibility of channels
Several notable non-classical features of quantum theory are connected to the non-commutativity of
operators. Compatibility is one of the possible operational generalizations of non-commutativity of operators,
and it is the generalization that most frequently appears in other applications of quantum information
theory, see [135] for a review. Compatibility is usually only introduced for measurements, but we are going
43

<!-- page 44 -->
to introduce compatibility of channels. As before, we will easily recover results about compatibility of
measurements as a special cases of the results for channels.
Consider the following scenario: let Alice and Bob be two parties with state spaces KA and KB and
imagine that Alice wants to message to Bob. Alice encodes the message into a state xA ∈ KA and she uses
a fixed channel Φ ∈ C(KA , KB ) to send the message to Bob, Bob would receive Φ(xA ) and then proceed to
decode the message. Our task is to intercept the message and to learn about it as much as possible. One
˜ KC ),
thing that we can do is to replace the channel Φ ∈ C(KA , KB ) with a different channel Ψ ∈ C(KA , KB ⊗
where KC is a system we control. The idea is that the channel Ψ is meant to extract as much information
as we can get while keeping the state that Bob receives practically unchanged. So we have to require that

KA

Ψ

KB

=

KA

Φ KB

(7.1)

KC

so that Bob receives the intended message. The channel ΨC ∈ C(KA , KC ), given as

KA

Ψ KB

=

KA

ΨC K

C

(7.2)

KC

is the information about the encoded message that we are able to extract. In principle, we would want to
choose the channel ΨC ∈ C(KA , KC ) to give us as much information as possible about the input state, but
this does not have to be always possible because of the condition (7.1). As we will see, there is a certain tradeoff between how much information about the input state is encoded in the output of Φ ∈ C(KA , KB ) and
how much we can extract using ΨC ∈ C(KA , KC ). Notice that we are (in some intuitive sense) attempting
to get the outcome of both Φ ∈ C(KA , KB ) and ΨC ∈ C(KA , KC ) at the same time using the bigger channel
˜ KC ).
Ψ ∈ C(KA , KB ⊗
Definition 7.1. Let KA , KB , KC be state spaces and let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ) be channels.
˜ KC ) such that
We say that Φ1 and Φ2 are compatible if and only if there is a channel Φ ∈ C(KA , KB ⊗

KA

Φ

KB

=

KA

Φ1 K

KA

Φ2 K

B

(7.3)

KC

and
KA

Φ KB

=

C

(7.4)

KC

hold. The channel Φ is usually called the joint channel of Φ1 and Φ2 , or the compatibilizer.
The problem of deciding whether two channels are compatible or not can seem complicated at first, but
it is not so. One can in principle rewrite it as a problem of conic programming and get a resource theory
[136] of compatibility of channels. The underlying conic programming problems are not easily solvable in
general, but in the case of quantum theory they are equivalent to quantum marginal problems [5, 137, 138],
which are just semi-definite programming problems. The following is an intuitive result saying that constant
channels are compatible with every other channel.
Proposition 7.2. Let KA , KB , KC be state spaces, let Φ ∈ C(KA , KB ) be a channel, let yC ∈ KC be a
fixed state and let τyC ∈ C(KA , KC ) be a constant channel, i.e., for every xA ∈ KA we have τyC (xA ) = yC .
Then Φ and τyC are compatible.
44

<!-- page 45 -->
˜ KC ). Let xA ∈ KA
Proof. The proof is straightforward: we will construct the joint channel Φ ∈ C(KA , KB ⊗
and let Ψ(xA ) = Φ(xA ) ⊗ yC , or in diagrammatic notation
Ψ KB =

xA

xA

Φ KB
yC

KC

(7.5)

KC

It is straightforward to verify that Ψ is a channel and that it is the joint channel of Φ and τyC .
One special case of compatibility of channels is the self-compatibility of a channel with itself. This is the
scenario where we assume KB = KC and Φ1 = Φ2 .
Definition 7.3. Let KA , KB be state spaces and let Φ ∈ C(KA , KB ). We say that Φ is self-compatible if
˜ KB ) such that
there is a channel Ψ ∈ C(KA , KB ⊗
Ψ

=

Φ

(7.6)

Ψ

=

Φ

(7.7)

and

hold.
It is natural to assume that measurements are self-compatible, because the outcome of a measurement is
some classical information about the system and it is intuitive that we can copy classical information. We
will prove a stronger version of this result.
Proposition 7.4. Let ΦMP ∈ C(KA , KB ) be a measure-and-prepare channel, see Definition 6.17. Then
ΦMP is self-compatible.
Proof. Let ΦMP ∈ C(KA , KB ) be a measure-and-prepare channel, then there are a measurement m ∈
C(KA , Sn ) and preparation P ∈ C(Sn , KC ) such that
m

=

ΦMP

P

(7.8)

˙ Sn ) by ΨD (si ) = si ⊗ si . Note that ΦD is well-defined, because s1 , . . . , sn form a
Define ΨD ∈ C(Sn , Sn ⊗
Pn
Pn
∗
basis of A(Sn ) . For any
Pns ∈ Sn there are numbers λ1 , . . . , λn ∈ R+ , i=1 λi = 1, such that s = i=1 λi si
and we have ΦD (s) = i=1 λi si ⊗ si . For any s ∈ Sn we also have
s

ΨD

=

s

(7.9)

s

ΨD

=

s

(7.10)

and

45

<!-- page 46 -->
˜ KB )
which is straightforward to verify. We are now ready to construct the joint channel Ψ ∈ C(KA , KB ⊗
as
m

=

Ψ

P

ΨD

(7.11)

P

It is straightforward to check that Ψ is the joint channel using (7.9) and (7.10).
For measurements, the definition of compatibility simplifies:
Proposition 7.5. Let K be a state space and let m1 ∈ C(K, Sn1 ) and m2 ∈ C(K, Sn2 ) be measurements
given as
m1 =

n1
X
i=1

fi ⊗ si ,

m2 =

n2
X
j=1

gj ⊗ sj ,

(7.12)

2
1
⊂ E(K), see Proposition 6.13. Then m1 and m2 are compatible if and only
⊂ E(K), {gj }nj=1
where {fi }ni=1
Pn1 Pn2
n1 ,n2
if there are effects {hij }i,j=1 ⊂ E(K) such that i=1
j=1 hij = 1K and

n2
X

n1
X

hij = fi ,

hij = gj .

(7.13)

i=1

j=1

Proof. Assume that m1 ∈ C(K,
and m2 ∈ C(K, Sn2 ) are compatible, then the joint channel is m ∈
PSn11 )P
n2
˙ Sn2 ), given as m = ni=1
C(K, Sn1 ⊗
j=1 hij ⊗ si ⊗ sj . Then we have
m

m1 =

=

n1 X
n2
X
i=1 j=1

hij ⊗ si

(7.14)

Pn2
Pn1
from where we get j=1
hij = fi for all i ∈ {1, . . . , n1 }.
i=1 hij = gj follows analogically. Now assume
P
n1 Pn2
1 ,n2
that there are effects {hij }ni,j=1
⊂ E(K) such that i=1
j=1 hij = 1K and (7.13) hold, then let m ∈
P 1 Pn2
˙ Sn2 ) be given as m = ni=1
C(K, Sn1 ⊗
h
⊗s
⊗s
.
It
is
easy to verify that m is the joint measurement
i
j
j=1 ij
of m1 and m2 .
In the following we will investigate several aspects of incompatibility of channels and measurements, we
will present the known results about existence of incompatibility in non-classical theories and we will show
how incompatibility interacts with entanglement.
7.1. No-broadcasting theorem and existence of incompatible measurements
We are going to investigate compatibility of the identity channel idK ∈ C(K). So let K be a state space,
then we want to find a channel Φ ∈ C(K, K ˜
⊗ K) such that for every x ∈ K we have
x

Φ

=

x

(7.15)

x

Φ

=

x

(7.16)

and

46

<!-- page 47 -->
or, purely in terms of channels,
Φ

=

(7.17)

Φ

=

(7.18)

idK

(7.19)

and

where the plain wire represents the identity channel, i.e.,
=

Assume that x is pure, then according to Theorem 5.19 we must have
(7.20)

Φ(x) = x ⊗ x.

˙ K) is the universal cloning channel for pure states, also called the universal
It follows that Φ ∈ C(K, K ⊗
broadcasting channel. Note that the universal broadcasting channel Φ is uniquely specified by (7.20) and
by the convexity of K. It is known that we can copy classical information, i.e., that in classical theory, the
universal cloning machine exists.
Proposition 7.6. Let Sn be a simplex, i.e., the state space of classical theory, and let s1 , . . . , sn ∈ Sn be
the extreme points of Sn . Then the identity channel idSn ∈ C(Sn ) is self-compatible and the joint channel is
˙ Sn ) given as ΦD (si ) = si ⊗ si .
ΦD ∈ C(Sn , Sn ⊗
Proof. The result follows from Proposition 7.4, since the identity channel idSn ∈ C(Sn ) is measure-andprepare.
We are now going to formulate a well-known result that for non-classical theories we can not construct
the universal broadcasting channel, this result is known as no-broadcasting theorem [17, 18]. Let K be
a non-classical state space, i.e., not a simplex. Let x1 , . . . , xn ∈ K be pure states such that they form
basis of A(K)∗ , such set always exists because the set of all pure states of K mustPbe overcomplete. Let
n
y∈P
K be pure state, y 6= xi for all i ∈ {1, . . . , n}, then there are α1 , . . . , αn ∈ R, i=1 αi = 1, such that
n
y = i=1 αi xi . Since y and x1 , . . . , xn are pure states, then according to (7.20) we must have
n
X

(7.21)

αi αj xi ⊗ xj .

(7.22)

(αi δij − αi αj )xi ⊗ xj = 0.

(7.23)

αi Φ(xi ) =

i=1

and
Φ(y) = y ⊗ y =
Comparing the two terms we get

n
X

n
X

αi xi ⊗ xi

Φ(y) =

i=1
n
X
i,j=1

i,j=1

Since {xi ⊗ xj }ni,j=1 is a basis of A(K)∗ ⊗ A(K)∗ we get αi δij − αi αj = 0 for all i, j ∈ {1, . . . , n}. For i = j
we get αi = αi2 and so αi ∈ {0, 1} for all i ∈ {1, . . . , n}. For i 6= j, we must have αi αj = 0 and so either
αi = 0 or αj = 0. It follows that only one of the numbers αi can be non-zero, without
of generality we
Ploss
n
argue that we must have α1 6= 0 and αj = 0 for all j ∈ {2, . . . , n}. We then have y = i=1 αi xi = x1 which
is a contradiction with y 6= xi for all i ∈ {1, . . . , n}. Thus we have proved:
47

<!-- page 48 -->
Theorem 7.7. Let K be a state space and let idK ∈ C(K) be the identity channel. The following statements
are all equivalent:
(NB1) idK is a measure-and-prepare channel;
(NB2) idK is self-compatible channel;
˜ K);
(NB3) there exists universal broadcasting channel Φ ∈ C(K, K ⊗
(NB4) K = Sn is a simplex.
Proof. See above, or [17, 18].
This is another characterization of classical state spaces, the first one we presented was in terms of
existence of entanglement, see Theorem 5.21. There are two immediate corollaries of Theorem 7.7.
Corollary 7.8. Let K be a non-classical state-space, then there exist pair of incompatible channels Φ1 , Φ2 ∈
C(K).
Proof. Take Φ1 = Φ2 = idK .

Corollary 7.9. Let K be a non-classical state-space, then not all channels in C(K) are measure-and-prepare.
Proof. If idK was measure-and-prepare, then according to Proposition 7.4 it would be self-compatible.

One can also investigate whether we can broadcast at least some convex subset B ⊂ K, i.e., whether
˜ K) such that for every x ∈ B we have
there is a channel Ψ ∈ C(K, K ⊗
x

Ψ

=

x

(7.24)

x

Ψ

=

x

(7.25)

and

The following is a reformulation of the main result of [17, 18].
Theorem 7.10. Let B ⊂ K, then there exists channel Ψ ∈ C(K, K ˜
⊗ K) satisfying (7.24) and (7.25) if and
only if there is a measure-and-prepare channel ΦMP ∈ C(K) such that for all x ∈ B we have ΦM P (x) = x.

Proof. We are only going to show that if such measure-and-prepare channel ΦMP exists, then there also
exists channel Ψ satisfying (7.24) and (7.25). For the proof of the other implication see [17, 18]. So let
ΦMP ∈ C(K) be a measure-and-prepare channel such that for every x ∈ B we have ΦMP (x) = x. Then
˜ K) such that
according to Proposition 7.4 ΦMP is self-compatible, so there exists a channel Ψ ∈ C(K, K ⊗
(7.3) and (7.4) are satisfied. Let x ∈ B, we then have
x

Ψ

=

x

ΦMP

=

x

(7.26)

x

Ψ

=

x

ΦMP

=

x

(7.27)

and

so (7.24) and (7.25) are satisfied.
48

<!-- page 49 -->
Another way to extend the results we have obtained so far is to restrict the set of channels we investigate: instead of asking whether there exist some pair of incompatible channels Φ1 ∈ C(KA , KB ) and
Φ2 ∈ C(KA , KC ), we can ask whether there exists a pair of incompatible two-outcome measurements
m1 ∈ C(K, S2 ) and m2 ∈ C(K, S2 ). It was shown in [20, 25] that such pair of incompatible two-outcome
measurements exists whenever K is not a simplex.
Theorem 7.11. There exists a pair of incompatible two-outcome measurements m1 ∈ C(K, S2 ) and m2 ∈
C(K, S2 ) whenever K is not a simplex.
Proof. See [20] for a constructive proof.
One can also show that existence of incompatible measurements is related to existence of entanglement
between appropriate cones, see [132].
7.2. Preorder of channels and compatibility
In this section we will explore the connection between the post-processing preorder and compatibility
of channels; most of the results are inspired by [135]. We will also prove that post-processing greatest
measurement exists only if K is a simplex. The first result is immediate.
Proposition 7.12. Let KA , KB , KC , KD be state spaces and let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ) and
Φ3 ∈ C(KA , KD ) be channels such that Φ3 ≺ Φ2 . If Φ1 and Φ2 are compatible, then also Φ1 and Φ3 are
compatible.
˜ KC ) such that
Proof. Since Φ1 and Φ2 are compatible, there is a channel Ψ ∈ C(KA , KB ⊗
Ψ

=

Φ1

(7.28)

Ψ

=

Φ2

(7.29)

and

Since Φ3 ≺ Φ2 there is a channel Λ ∈ C(KC , KD ) such that
Φ3

=

Φ2

Λ

=

Ψ

=

=

Φ2

(7.30)

We then have
Ψ

Λ

(7.31)

Φ1

and

Ψ

Λ

=

Ψ

Λ

Λ

=

Φ3

(7.32)

and so Φ1 and Φ3 are also compatible.
Corollary 7.13. If a channel Φ1 ∈ C(KA , KB ) is compatible with idKA ∈ C(KA ), then it is also compatible
with any other channel Φ2 ∈ C(KA , KC ).
49

<!-- page 50 -->
Proof. The result follows from Proposition 7.12 and Proposition 6.31.
Corollary 7.14. Let Sn be a simplex, let KA , KB be any state spaces, and let P 1 ∈ C(Sn , KA ) and
P 2 ∈ C(Sn , KB ) be conditional preparations. Then P 1 and P 2 are compatible.
Proof. We know from Theorem 7.7 that idSn : Sn → Sn is self-compatible. Since P 1 ≺ idSn it follows from
Proposition 7.12 that P 1 and idSn are compatible. Repeating the same argument for P 2 ≺ idSn we get that
P 1 and P 2 are compatible.
The following result is a generalization of known result that two measurements are compatible if and
only if they are both post-proccesings of a single measurement, see [22].
Proposition 7.15. Let Φ ∈ C(KA , KB ) be a self-compatible channel and let Φ1 ∈ C(KA , KC ) and Φ2 ∈
C(KA , KD ) be channels such that Φ1 ≺ Φ and Φ2 ≺ Φ. Then Φ1 and Φ2 are compatible.
Proof. Since Φ ∈ C(KA , KB ) is self-compatible and Φ1 ≺ Φ, it follows from Proposition 7.12 that Φ and Φ1
are compatible. Repeating the argument for Φ2 ≺ Φ we get that Φ1 and Φ2 are compatible.
Using the obtained results, we can prove that a post-processing greatest measurement m ∈ C(K, Sn )
exists only if K is a simplex.
Proposition 7.16. There exists a post-processing greatest measurement m ∈ C(K, Sn ) if and only if K is
a simplex.
Proof. Assume that a post-processing greatest measurement m ∈ C(K, Sn ) exists. Then for any two measurements m1 ∈ C(K, Sn1 ) and m2 ∈ C(K, Sn2 ) we have m1 ≺ m and m2 ≺ m. Since m is measurement, it is
self-compatible, see Proposition 7.4 . It then follows from Proposition 7.15 that m1 and m2 are compatible.
Since m1 and m2 were arbitrary, it follows that all measurements m1 ∈ C(K, Sn1 ) and m2 ∈ C(K, Sn2 ) are
compatible, but then according to Theorem 7.11 K is a simplex.
When comparing Proposition 6.31 to Proposition 7.16, one finds a significant difference between channels
and measurements. This difference is going to manifest itself in determining the steerability of a state in
the following subsection.
7.3. Incompatibility witnesses, steering, and Bell non-locality
It is rather easy to prove that two channels are compatible, we just need to provide the joint channel.
But how do we prove that two channels are incompatible? Let
C 2 (KA ; KB , KC ) = {(Φ1 , Φ2 ) : Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KB )}

(7.33)

be the set of pairs of channels. Since C(KA , KB ) and C(KA , KC ) are convex sets, it is easy to see that
C 2 (KA ; KB , KC ) is also a convex set, with the convex combination defined as
λ(Φ1 , Φ2 ) + (1 − λ)(Ψ1 , Ψ2 ) = (λΦ1 + (1 − λ)Ψ1 , λΦ2 + (1 − λ)Ψ2 ),

(7.34)

where (Φ1 , Φ2 ), (Ψ1 , Ψ2 ) ∈ C 2 (KA ; KB , KC ) and λ ∈ [0, 1]. Let CC 2 (KA ; KB , KC ) be the set of compatible
pairs of channels, i.e., (Φ1 , Φ2 ) ∈ CC 2 (KA ; KB , KC ) only if Φ1 and Φ2 are compatible; we clearly have
CC 2 (KA ; KB , KC ) ⊂ C 2 (KA ; KB , KC ). One can also easily show that CC 2 (KA ; KB , KC ) is a convex set: let
˜ KC ) respectively. Then it is
(Φ1 , Φ2 ), (Ψ1 , Ψ2 ) ∈ CC 2 (KA ; KB , KC ) with joint channels Φ, Ψ ∈ C(KA , KB ⊗
easy to see that we have

λΦ + (1 − λ)Ψ

=

Φ1

λ

50

+ (1 − λ)

Ψ1

(7.35)

<!-- page 51 -->
and
λΦ + (1 − λ)Ψ

=

Φ2

λ

+ (1 − λ)

Ψ2

(7.36)

where we have used the linearity of the partial trace, see Example 6.4. We can now use the hyperplane
separation theorem B.9 to find affine functions W : C(KA ; KB , KC ) → R such that for all pairs of compatible
channels (Φ1 , Φ2 ) ∈ CC 2 (KA ; KB , KC ) we have W (Φ1 , Φ2 ) ≥ 0. Then if (Ψ1 , Ψ2 ) ∈ C 2 (KA ; KB , KC ) such
that W (Ψ1 , Ψ2 ) < 0 then Ψ1 and Ψ2 must be incompatible.
Definition 7.17. Let W : C(KA ; KB , KC ) → R be an affine function, such that W (Φ1 , Φ2 ) ≥ 0 for all
(Φ1 , Φ2 ) ∈ CC 2 (KA ; KB , KC ) and such that there exist (Ψ1 , Ψ2 ) ∈ C 2 (KA ; KB , KC ) such that W (Ψ1 , Ψ2 ) <
0. Then we call W the incompatibility witness for (Ψ1 , Ψ2 ).
Incompatibility witnesses are an ideal tool to prove incompatibility of pairs fo channels. The only
problem is: how does one find the suitable incompatibility witness for a given pair of channels? There are
several know constructions: for measurements, one can use a relation between compatible measurements
and entanglement breaking channels to obtain an incompatibility witness [24], or one can use discrimination
tasks with partial immediate information [139–141].
We will present several ideas on how to prove incompatibility of pair of channels. We will not formulate
the ideas as incompatibility witnesses, but rather as a more general and operationally motivated strategies.
We will roughly follow the ideas presented in [5] and we will comment on how these strategies connect
to steering and Bell non-locality. We will start by presenting a construction that does not work, but it
introduces the main concept that will be used later on.
Let Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) be compatible channels and let Φ ∈ C(KA , KB ˜
⊗ KC ) be the
˜ KC such that
joint channel. Then for every xA ∈ KA there is some yBC ∈ KB ⊗
yBC

=

xA

Φ1

(7.37)

yBC

=

xA

Φ2

(7.38)

and

This is immediate as one can always take yBC = Φ(xA ) and then (7.37) and (7.38) follow from Definition
˜ KC does not exist, then the channels
7.1. So then if for some pair of channels Φ1 and Φ2 such yBC ∈ KB ⊗
must be incompatible and hence we have obtained a test of incompatibility. Unfortunately this test never
works, because we can also take yBC = Φ1 (xA ) ⊗ Φ2 (xA ) and (7.37) and (7.38) are satisfied even if Φ1
and Φ2 are incompatible. We have two opportunities to overcome this problem: we can either use a set of
˜ KD . We can also combine
states {x1,A , . . . , xn,A } ⊂ KA , or we can use an entangled state xAD ∈ KA ⊗
both approaches. We will proceed with formulating the possible strategies to proving the incompatibility
of channels: we will formulate our results as necessary conditions for compatibility of channels, violation of
these conditions gives proofs of incompatibility of the channels in question. We will also show that using
entangled states leads to steering [142] and Bell non-locality [143], two well known phenomena in quantum
information theory.
Pn
Proposition
7.18. Let {x1,A , . . . , xn,A } ⊂ KA be states such that for some αi ∈ R,
i=1 αi = 0 we
Pn
have i=1 αi xi,A = 0. Let Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) be compatible channels, then there are
yi,BC ∈ KB ˜
⊗ KC , i ∈ {1, . . . , n}, such that
yi,BC

=
51

xi,A

Φ1

(7.39)

<!-- page 52 -->
and
yi,BC

for all i ∈ {1, . . . , n}, and

=

n
X

xi,A

αi yi,BC = 0.

Φ2

(7.40)

(7.41)

i=1

Proof. Let Φ ∈ C(KA , KB ˜
⊗ KC ) be the joint channel of Φ1 and Φ2 . Let yi,BC = Φ(xi,A ), then (7.39) and
(7.40) follow. Moreover we have
!
n
n
n
X
X
X
αi yi,BC =
αi Φ(xi,A ) = Φ
αi xi,A = Φ(0) = 0
(7.42)
i=1

i=1

i=1

so also (7.41) holds.
The main idea of Proposition 7.18 is that for a given pair of channels Φ1 ∈ C(KA , KB ) and Φ2 ∈
C(KA , KC ) we can take some test subset {x1,A , . . . , xn,A } ⊂ KA and test whether there is some set
˜ KC such that (7.39), (7.40) and (7.41) are satisfied.
{y1,BC , . . . , yn,BC } ⊂ KB ⊗
Definition 7.19. Let {x1,A , . . . , xn,A } ⊂ KA be states and let Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) be
channels. We say that x1,A , . . . , xn,A certify incompatibility of Φ1 and Φ2 if there does not exist any set of
˜
states {y1,BC , . . . , yn,BC } ⊂ K
PBn⊗ KC that would
Pn satisfy (7.39), (7.40) and (7.41) for every set of numbers
{α1 , . . . , αn } ⊂ R, such that i=1 αi = 0 and i=1 αi xi,A = 0.
Note that we have already used the idea behind Proposition 7.18 to prove Theorem 7.7. The main idea
there is that idK is self-compatible only if the set of pure states {x1,A , . . . , xn,A } is affinely independent.
This is because testing incompatibility on affinely independent states is essentially the same as trying to
find incompatible channels on simplex. This is formalized as follows:
Proposition 7.20. Let {x1,A , . . . , xn,A } ⊂ KA be affinely independent points and let Φ1 ∈ C(KA , KB ),
Φ2 ∈ C(KA , KC ), then x1,A , . . . , xn,A do not certify the incompatibility of Φ1 and Φ2 .
Proof.PSince {x1,A , . . . P
, xn,A } are affinely independent, we have that for any αi ∈ R, i ∈ {1, . . . , n}, such
n
n
that i=1 αi = 0 and i=1 αi xi = 0 we must have αi = 0 for all i ∈ {1, . . . , n}. It then follows that (7.41)
˜ KC . So we can simply take yi,BC = Φ1 (xi,A ) ⊗ Φ2 (xi,A ) for all
holds for any set {y1,BC , . . . , yn,BC } ⊂ KB ⊗
i ∈ {1, . . . , n}. We have already argued that (7.41) holds and it is straightforward to check that also (7.39)
and (7.40) hold.
We will also show that for large enough collection of states {x1,A , . . . , xn,A } ⊂ KA , the test coming from
Proposition 7.18 must be conclusive, in the sense that it must either prove or disprove compatibility of the
two channels.
Proposition 7.21. Let {x1,A , . . . , xn,A } ⊂ KA contain all pure states, i.e., all extreme points of KA . Let
Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ), then Φ1 and Φ2 are incompatible if and only if x1,A , . . . , xn,A certify
incompatibility of Φ1 and Φ2 .
Proof. For simplicity, let {x1,A , . . . , xn,A } ⊂ KA be the set of all pure states and assume that x1,A , . . . , xn,A
˜ KC that satdo not certify incompatibility of Φ1 and Φ2 . Then there are {y1,BC , . . . , yn,BC } ⊂ KP
B⊗
n
isfy
(7.39),
(7.40)
and
(7.41)
for
every
set
of
numbers
{α
,
.
.
.
,
α
}
⊂
R,
such
that
1
n
i=1 αi = 0 and
Pn
˜
α
x
=
0.
Define
a
channel
Φ
∈
C(K
,
K
⊗
K
)
by
Φ(x
)
=
y
and
extended
to the rest of
A
B
C
i,A
i,BC
i=1 i i,A

52

<!-- page 53 -->
KA by convexity. To see that Φ is well defined and convex, it is sufficient to check that for any zA ∈ KA
and any two affine decompositions of zA given as
n
X

zA =

i=1
n
X

zA =

βi1 xi,A

(7.43)

βi2 xi,A

(7.44)

i=1

we have

n
X

βi1 Φ(xi,A ) =

i=1

n
X

(7.45)

βi2 Φ(xi,A ).

i=1

Pn
Pn
Pn
Applying the unit effect 1KA to (7.43) and (7.44) P
yields i=1 βi1 =P i=1 βi2 = 1. We have i=1 (βi1 −
n
n
2
β
so βi1 − βi2 = αi is a set such that i=1 αi = 0 and i=1 αi xi,A = 0. From (7.41) we get
Pi n)xi,A 1= 0 and
2
i=1 (βi − βi )Φ(xi,A ) = 0, it follows that (7.45) holds and that Φ is well-defined. It follows from (7.39) and
(7.40) that Φ is a joint channel of Φ1 and Φ2 . Hence Φ1 and Φ2 are compatible.
Under the rug, we have assumed in Proposition 7.21 that KA has finitely many extreme points, i.e., that
KA is a polytope. But this assumption is not necessary and one can easily extend the result of Proposition
7.21 to all state spaces using Carathéodory theorem 3.4. One can also find a relation between certifying
incompatibility and post-processing preorder of channels.
Proposition 7.22. Let {x1,A , . . . , xn,A } ⊂ KA and let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ) and Φ3 ∈
C(KA , KD ) be such that Φ3 ≺ Φ2 . Then if x1,A , . . . , xn,A certify incompatibility of Φ1 and Φ3 , then
x1,A , . . . , xn,A also certify incompatibility of Φ1 and Φ2 .
Proof. The proof follows by contradiction: assume that x1,A , . . . , xn,A do not certify incompatibility of Φ1
˜ KC be the corresponding states satisfying (7.39), (7.40), and
and Φ2 , and let {y1,BC , . . . , yn,BC } ⊂ KB ⊗
(7.41). Since Φ3 ≺ Φ2 , there is a channel Ψ ∈ C(KC , KD ) such that
=

Φ3

Φ2

(7.46)

Ψ

Now let {z1,BD , . . . , zn,BD } ⊂ KB ˜
⊗ KD be defined as
zi,BD

=

(7.47)

yi,BC
Ψ

Then it is straightforward to check that {z1,BD , . . . , zn,BD } satisfies (7.39), (7.40), and (7.41) for channels
Φ1 and Φ3 , so x1,A , . . . , xn,A can not certify the incompatibility of Φ1 and Φ3 .
Now we will proceed to testing incompatibility of channels using entangled states.
˜ KD and let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ) be compatible channels.
Proposition 7.23. Let xAD ∈ KA ⊗
˜
˜
Then there is yBCD ∈ KB ⊗ KC ⊗ KD such that
KB

yBCD

KC

=

xAD KA

Φ1 K

B

KD
KD

53

(7.48)

<!-- page 54 -->
and
KB

yBCD

=

KC

xAD KA

Φ2 K

C

(7.49)

KD
KD

hold.
Proof. Take
KB
KB

yBCD

KC

KA

xAD

=

Φ
KC

(7.50)

KD

KD

˜ KC ) is the joint channel of Φ1 and Φ2 . Then (7.48) and (7.49) follow immediately.
where Φ ∈ C(KA , KB ⊗
We can again use Proposition 7.23 as a strategy to prove incompatibility of channels Φ1 and Φ2 . We can
˜ KD and check whether suitable yBCD ∈ KB ⊗
˜ KC ⊗
˜ KD
simply select a state space KD and xAD ∈ KA ⊗
exists. But note that the state xAD can not be chosen randomly, but xAD must be an entangled state for
the test to be meaningful.
˙ KD be a separable state. Then for any Φ1 ∈ C(KA , KB ), Φ2 ∈
Proposition 7.24. Let xAD ∈ KA ⊗
˜
˜ KD satisfying (7.48) and (7.49).
C(KA , KC ) there exists yBCD ∈ KB ⊗ KC ⊗
Proof. It is sufficient to prove that such yBCD exists for product states, i.e., for xAD = xA ⊗ zD . The
proof for general separable states follows from the linearity of (7.48) and (7.49). For xAD = xA ⊗ zD take
yBCD = Φ1 (xA ) ⊗ Φ2 (xA ) ⊗ zD . It is straightforward to show that (7.48) and (7.49) hold.
Proposition 7.23 allows us to construct entanglement-assisted incompatibility tests. More specifically, it
was shown in [5] that if we would replace channels by measurements, these tests would exactly correspond
to steering [142]. Hence the following definitions:
Definition 7.25. We say that channels Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) steer the state xAD ∈
˜ KD if there is no yBCD ∈ KB ⊗
˜ KC ⊗
˜ KD that would satisfy (7.48) and (7.49).
KA ⊗
˜ KD is steerable by channels if there are channels
Definition 7.26. We say that the state xAD ∈ KA ⊗
˜ KC ⊗
˜ KD
Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) that steer xAD , i.e., such that there is no yBCD ∈ KB ⊗
that would satisfy (7.48) and (7.49).
One can define an equivalent notion of steerability by measurements.
˜ KD is steerable by measurements if there are meaDefinition 7.27. We say that the state xAD ∈ KA ⊗
surements m1 ∈ C(KA , Sn1 ) and m2 ∈ C(KA , Sn2 ) that steer xAD , i.e., such that there is no yBCD ∈
˜ Sn2 ⊗
˜ KD that would satisfy (7.48) and (7.49).
Sn1 ⊗
Is is known that in quantum theory two channels are incompatible if and only if they steer some state; it
is an open question whether the same also holds for all GPTs. We will again get a relation between steering
and post-processing preorder of channels.
Proposition 7.28. Let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ), and Φ3 ∈ C(KA , KD ) be channels such that
˜ KE , then also Φ1 and Φ3 do not steer xAE .
Φ3 ≺ Φ2 . If Φ1 and Φ2 do not steer xAE ∈ KA ⊗
54

<!-- page 55 -->
˜ KE , then there is a state yBCE ∈ KB ⊗
˜ KC ⊗
˜ KE such that
Proof. If Φ1 and Φ2 do not steer xAE ∈ KA ⊗
KB

yBCE

=

KC

xAE KA

Φ1 K

B

(7.51)

KE
KE

and
yBCE

KB

=

KC
KE

xAE KA

Φ2 K

C

(7.52)

KE

Since Φ3 ≺ Φ2 , there is a channel Ψ ∈ C(KC , KD ) such that
Φ3

(7.53)

=

Φ2

Ψ

=

yBCE

Ψ KD
KC

˜ KD ⊗
˜ KE given as
Take zBDE ∈ KB ⊗
KB

zBDE

KD

KB

KE

(7.54)

KE

It is straightforward to show that zBCE satisfies (7.48) and (7.49) and so Φ1 and Φ3 do not steer xAE .
Corollary 7.29. Let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ), and Φ3 ∈ C(KA , KD ) be channels such that
˜ KE , then also Φ1 and Φ2 steer xAE .
Φ3 ≺ Φ2 . If Φ1 and Φ3 steer xAE ∈ KA ⊗
Proof. The result follows from Proposition 7.28. If Φ1 and Φ2 do not steer xAE , then also Φ1 and Φ3 do
not steer xAE . So if Φ1 and Φ3 steer xAE , then also Φ1 and Φ2 must steer xAE .
Let Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) be channels, then we already know that Φ1 ≺ idKA and
Φ2 ≺ idKA , where idKA ∈ C(KA ) is the identity channel. As a consequence we have the following.
Proposition 7.30. A state xAD is steerable by channels if and only if two copies of the identity channel
idKA ∈ C(KA ) steer xAD .
Proof. If two copies of the identity channel idKA ∈ C(KA ) steer xAD , then xAD is steerable. So assume now
that two copies of idKA do not steer xAD . Let Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) be channels, then
Φ1 ≺ idKA and Φ2 ≺ idKA and according to Proposition 7.28 Φ1 and Φ2 can not steer xAD .
It is now easy to see the difference between measurements and channels. Since for non-classical state
space KA there does not exist post-processing greatest measurement m, we can not easily determine whether
a state xAD ∈ KA ˜
⊗ KD is steerable by some measurements m1 , m2 , because we would have to check for
all possible pairs of measurements. In fact, one only needs to check for measurements m1 and m2 such
that if m1 ≺ m01 , then also m01 ≺ m1 and if m2 ≺ m02 , then also m02 ≺ m2 , i.e., we only need to consider
post-processing maximal measurement m1 and m2 , see [135]. If KA is a polytope, this reduces to finite
number of pairs measurements.
Since we have discussed steering, it is natural to expect that we can formalize Bell non-locality [143] in this
fashion. The main idea is that in steering, we are applying channels Φ1 ∈ C(KA , KB ) and Φ2 ∈ C(KA , KC ) to
˜ KD . Given another pair of channel Ψ1 ∈ C(KD , KE ) and Ψ2 ∈ C(KD , KF ),
only the one leg of xAD ∈ KA ⊗
we can apply them to the other leg of xAD .
55

<!-- page 56 -->
˜ KD be a state and let Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ), Ψ1 ∈
Proposition 7.31. Let xAD ∈ KA ⊗
C(KD , KE ) and Ψ2 ∈ C(KD , KF ) be channels. Assume that Φ1 , Φ2 are compatible and that Ψ1 , Ψ2 are
˜ KC ⊗
˜ KE ⊗
˜ KF such that
compatible. Then there is a state yBCEF ∈ KB ⊗
KB

yBCEF KC

=

Φ1 K

xAD KA

KE

KD

B

Ψ1 K

(7.55)

E

KF

and
KB

yBCEF

KC

=

Φ1 K

xAD KA
KD

KE

B

Ψ2 K

(7.56)

F

KF

and
KB

yBCEF

KC

=

Φ2 K

xAD KA

KE

C

Ψ1 K

KD

(7.57)

E

KF

and
KB

yBCEF

KC

=

Φ2 K

xAD KA

KE

KD

B

Ψ2 K

(7.58)

F

KF

hold.
˜ KC ) and Ψ ∈ C(KD , KE ⊗
˜ KF ) be the joint channels of Φ1 , Φ2 and Ψ1 , Ψ2
Proof. Let Φ ∈ C(KA , KB ⊗
respectively. Take
KB
KB

KA

yBCEF KC =

Φ
KC

xAD

KE

KE
KD

KF

Ψ
KF

It is straightforward to verify that (7.55) - (7.58) hold.
56

(7.59)

<!-- page 57 -->
One can again show that if we would replace channels by measurements, we would simply get the standard
definition of Bell non-locality [5]. Hence the following definitions:
Definition 7.32. We say that xAD is Bell non-local with respect to Φ1 ∈ C(KA , KB ), Φ2 ∈ C(KA , KC ),
˜ KC ⊗
˜ KE ⊗
˜ KF such that (7.55) Ψ1 ∈ C(KD , KE ) and Ψ2 ∈ C(KD , KF ) if there is no yBCEF ∈ KB ⊗
(7.58) are satisfied.
Definition 7.33. We say that xAD is Bell non-local state if there are channel Φ1 ∈ C(KA , KB ), Φ2 ∈
C(KA , KC ), Ψ1 ∈ C(KD , KE ) and Ψ2 ∈ C(KD , KF ) with respect to which xAD is Bell non-local.
One can again prove that we need entanglement to get Bell non-locality.
˙ KD be a separable state, then xAD is Bell local, i.e., xAD is not Bell
Proposition 7.34. Let xAD ∈ KA ⊗
non-local.
Proof. Since the conditions (7.55) - (7.58) are linear, it is sufficient to take xAD = zA ⊗ wD where zA ∈ KA
and wD ∈ KD , for a general state the result follow by taking convex combinations. Let Φ1 ∈ C(KA , KB ),
Φ2 ∈ C(KA , KC ), Ψ1 ∈ C(KD , KE ) and Ψ2 ∈ C(KD , KF ) be channels, then we can take
zA

KB

yBCEF KC =

zA

KE

wD

KF

wD

KA

Φ1 K

KA

Φ2 K

KD

Ψ1 K

KD

Ψ2 K

B

C

(7.60)

E

F

It is straightforward to show that (7.55) - (7.58) are satisfied.
One can again prove relations between post-processing preorder of channels and Bell non-locality. We
will not do so, since they are straightforward to formulate. At last, we would want to comment on the
connection between steering and Bell non-locality. For measurements, it is easy to show that steering is
necessary for Bell non-locality, but for channels this is not so, see [5] for a counter-example. One can also
˜ KD ;
combine the approaches and consider scenarios with sets of entangled states {x1,AD , . . . , xn,AD } ⊂ KA ⊗
the generalization is straightforward and we will not investigate it.
8. Example: quantum theory
In this section we will review quantum theory as an example of a GPT. We will be brief as most of the
things we will cover are considered basic knowledge in quantum information theory. If the reader is not
familiar with quantum theory, we recommend [144].
Let H be a finite-dimensional complex Hilbert space. We will use the bra–ket notation to denote the
vectors as |ψi, the inner product of |ψi, |ϕi ∈ H is then denoted hϕ|ψi and it is linear in the second argument,
i.e., hϕ|ψi is linear in |ψi. L(H) will denote the complex vector space of operators X : H → H, 1 will denote
the identity operator. B H (H) will denote the real vector space of self-adjoint operators. Let X ∈ B H (H),
then Tr(X) will denote the trace of X. We say that X is positive semi-definite and we write X ≥ 0 if for all
|ψi ∈ H we have hψ|X|ψi ≥ 0. B +
H (H) will denote the set of all positive semi-definite operators; note that
B+
(H)
is
a
convex,
pointed
and
generating
cone.
H
8.1. State space and effect algebra
The state space in quantum theory is the set of density operators
D(H) = {ρ ∈ B +
H (H) : Tr(ρ) = 1}.
57

(8.1)

<!-- page 58 -->
The pure states are rank-1 projectors, i.e., the pure states of D(H) are projectors |ψihψ| for |ψi ∈ H,
2
kψk = hψ|ψi = 1. The vector space of affine functions A(D(H)) is isomorphic to B H (H), for X ∈ B H (H)
the corresponding function fX ∈ A(D(H)) is given as fX (ρ) = Tr(ρX). From now on we will omit the
isomorphism between fX and X and use X to refer to the function fX and we will write
A(D(H)) = B H (H).

(8.2)

The cone of positive functions A(D(H))+ is isomorphic to B +
H (H), because let X ∈ B H (H), then Tr(ρX) ≥ 0
if and only if Tr(|ψihψ|X) = hψ|X|ψi ≥ 0 for all |ψi ∈ H, kψk = 1. It follows that X ∈ A(D(H))+ if and
only if X ≥ 0, and so
(8.3)
A(D(H))+ = B +
H (H),

again omitting the isomorphism between A(D(H)) and B H (H). Now we will characterize the effect algebra
E(D(H)). Since for every ρ ∈ D(H) we have Tr(ρ) = 1, we have Tr(ρX) ≤ 1 if and only if Tr(ρ(1 −X)) ≥ 0,
which is equivalent to 1 −X ≥ 0. It follows that 0 ≤ Tr(ρX) ≤ 1 if and only if 0 ≤ X ≤ 1. We have
E(D(H)) = E(H) = {X ∈ B H (H) : 0 ≤ X ≤ 1}

(8.4)

up to the isomorphism. It is well-known that B H (H) is a Hilbert space with the Hilbert-Schmidt inner
product given as Tr(XY ) for X, Y ∈ B H (H). It follows that the dual of A(D(H)) = B H (H) is again going
to be B H (H), since Hilbert spaces are self-dual. So we have
A(D(H))∗ = B H (H).

(8.5)

This is the reason why in the standard approach to quantum information theory we do not distinguish
between A(D(H)) and A(D(H))∗ , because they are isomorphic. The isomorphism between A(D(H)) and
A(D(H))∗ (and as we will shortly see, also between A(D(H))+ and A(D(H))∗+ ) is a very important aspect
of quantum theory. One can again use simple arguments based on rank-1 projectors to show that
A(D(H))∗+ = B +
H (H).

(8.6)

It is also straightforward to see that D(H) is base of the cone B +
H (H), as it should be.
√
The base norm corresponds to the trace norm given as Tr(|X|), where |X| = X 2 . The order unit
norm corresponds to the operator norm kXk. Also note that the constructed theory satisfies no-restriction
hypothesis.
8.2. Tensor product
In quantum theory, tensor products of state spaces are induced by the tensor products of the underlying
Hilbert spaces, i.e., let HA and HB be Hilbert spaces, then we define
˜ D(HB ) = D(HA ⊗ HB ).
D(HA ) ⊗

(8.7)

We will now show that (8.7) defines a valid tensor product of state spaces. Note that we have B H (HA ) ⊗
B H (HB ) = B H (HA ⊗ HB ) so
˜ D(HB )) = B H (HA ⊗ HB ) = B H (HA ) ⊗ B H (HB ) = A(D(HA ))∗ ⊗ A(D(HB ))∗
span(D(HA ) ⊗

(8.8)

as we should have. It remains to show that
˙ D(HB ) ⊂ D(HA ⊗ HB ) ⊂ D(HA ) ⊗
ˆ D(HB ).
D(HA ) ⊗

(8.9)

Let ρA ∈ D(HA ) and ρB ∈ D(HB ), then ρA ⊗ ρB ≥ 0, i.e., ρA ⊗ ρB is s positive semi-definite operator.
It follows that ρA ⊗ ρB ∈ D(HA ⊗ HB ) and we get D(HA ) ˙
⊗ D(HB ) ⊂ D(HA ⊗ HB ). Now let ρAB ∈
D(HA ⊗ HB ) and let EA ∈ E(HA ), EB ∈ E(HB ), then we have EA ⊗ EB ≥ 0 and Tr(ρAB (EA ⊗ EB )) ≥ 0.
ˆ D(HB ) and we get D(HA ⊗ HB ) ⊂ D(HA ) ˆ
It follows that ρAB ∈ D(HA ) ⊗
⊗ D(HB ). Thus we have proved
58

<!-- page 59 -->
˜ D(HB ) is a well-defined bipartite state space. Note that both
both inclusion in (8.9) and so D(HA ) ⊗
of the inclusions are strict. Let for simplicity HA = HB = H, then it is well-known that entangled
Pdim(H)
|iii, exist, so we have
states, such as the maximally entangled state |φ+ ihφ+ |, |φ+ i = √ 1
i=1
dim(H)

˙ D(HB ) 6= D(HA ⊗ HB ). It is also well-known that the partial transpose of |φ+ ihφ+ |, denoted
D(HA ) ⊗
|φ+ ihφ+ |Γ , is not positive semi-definite, hence |φ+ ihφ+ |Γ ∈
/ D(HA ⊗ HB ). But we know from Proposition
6.28 that every positive map is completely positive with respect to the maximal tensor product, so we must
ˆ D(HB ). Therefore we have D(HA ⊗ HB ) 6= D(HA ) ⊗
ˆ D(HB ).
have |φ+ ihφ+ |Γ ∈ D(HA ) ⊗
We will now show that the tensor product defined in (8.7) is associative. Let HA , HB , HC be finitedimensional complex Hilbert spaces, then we have
˜ D(HB )) ⊗
˜ D(HC ) = D(HA ⊗ HB ) ⊗
˜ D(HC ) = D(HA ⊗ HB ⊗ HC )
(D(HA ) ⊗
˜ D(HB ⊗ HC ) = D(HA ) ⊗(D(H
˜
˜ D(HC ))
= D(HA ) ⊗
B) ⊗

(8.10)
(8.11)

as a result of associativity of the tensor product of Hilbert spaces.
Let HA , HB be Hilbert spaces, then the partial trace is defined as the unique map TrA : B H (HA ⊗ HB ) →
B H (HB ) such that for XAB ∈ B H (HA ⊗ HB ) and all YB ∈ B H (HB ) we have
Tr(TrA (XAB )YB ) = Tr(XAB (1A ⊗YB )).

(8.12)

This exactly corresponds to the definition of partial trace in Example 6.4.
8.3. Channels
Since we have a well-defined tensor product in quantum theory, we usually work only with completelypositive channels in quantum theory. It is well-known that the set of completely positive channels Φ ∈
C(D(HA ), D(HB ) is isomorphic to the set of Choi matrices J (HA , HB ) given as


1A
.
(8.13)
(H
⊗
H
)
:
Tr
(X)
=
J (HA , HB ) = X ∈ B +
A
B
B
H
dim(HA )
We have normalized the trace of the Choi matrices to 1, so we have J (HA , HB ) ⊂ D(HA ⊗ HB ). This is to
be compared to the characterization of all positive channels provided in Proposition 6.9, as one can clearly
see that the set of completely positive channels is strictly smaller than the set of positive channels. Note that
all measurements are automatically completely positive, because measurements are completely positive with
respect to any tensor product, see Proposition 6.23. Hence the characterization of measurements derived in
Proposition 6.13 still holds without any modifications.
8.4. Compatibility of channels
In quantum theory, the channels Φ1 ∈ J (HA , HB ) and Φ2 ∈ J (HA , HC ) are said to be compatible if
there is a joint channel Φ ∈ J (HA , HB ⊗ HC ) such that for all ρA ∈ D(HA ) we have
TrC (Φ(ρA )) = Φ1 (ρA ),

TrB (Φ(ρA )) = Φ2 (ρA ).

(8.14)

This is exactly the same definition as Definition 7.1, except that positive channels are replaced by completely
positive channels. Note that all of the results we have proved for compatibility of positive channels are easily
generalizable to completely positive channels.
9. Example: boxworld theory
In this section we will review a theory usually refer to as boxworld. Boxworld was introduced in [1] to
describe a theory of black boxes that have finite number of inputs and finite number of outputs. We will
investigate the case of boxes with one input bit and one output bit. There are going to be four extreme
points, denoted sij , i, j ∈ {0, 1}, corresponding to one of the four possible scenarios: the box s00 , s11 always
59

<!-- page 60 -->
0 7→ 0
0 7→ 1

1 7→ 0
s00
s10

1 7→ 1
s01
s11

Table 2: The extreme points of the simplest boxworld state space described in terms of how they handle the input 0 and how
they handle the input 1. sij maps 0 to i and 1 to j, where i, j ∈ {0, 1}.

outputs 0, 1, respectively, no matter the input, the box s01 outputs its input unchanged, and the box s10
outputs 1 if the input is 0 and outputs 0 if the input is 1, see also Table 2.
The four extreme points sij are not affinely independent, but we have
1
1
(s00 + s11 ) = (s10 + s01 ),
2
2

(9.1)

which is easy to check for both possible inputs. It follows that the state space we are dealing with is a
square.
9.1. State space and effect algebra
Let
 
 
0
1
s00 = 0 ,
s10 = 0 ,
1
1

 
0
s01 = 1 ,
1

 
1
s11 = 1 ,
1

(9.2)

and S = conv({s00 , s10 , s01 , s11 }). S is the square state space that we will be investigating. Note that we
have
s11 = s10 + s01 − s00
(9.3)

which one can prove from (9.1) or from the definition of the pure states. The vector space of affine functions
is A(S) and we have dim(A(S)) = 3. Let
 
 
 
 
 
1
−1
0
0
0
fx = 0 ,
1S − fx =  0  ,
fy = 1 ,
1S − fy = −1 ,
1S = 0
(9.4)
0
1
0
1
1
then fx , 1S −fx , fy , 1S −fy , 1S ∈ A(S), where the pairing is given by the usual Euclidean inner product. The
cone of the positive functions A(S)+ and the effect algebra E(S) are generated by fx , 1S − fx , fy , 1S − fy .
We then have
E(S) = conv({0, fx , 1S − fx , fy , 1S − fy , 1S }).
(9.5)

The state space S together with the positive cone A(S)∗+ is depicted in Figure 4a and the effect algebra
E(S) together with the positive cone A(S)+ is depicted in Figure 4b.
9.2. Tensor product
Since boxworld theory is a hypothetical theory, there is no physical principle that would select a specific
tensor product. Therefore, we will investigate the minimal and maximal tensor products. The minimal
tensor product is S ˙
⊗ S and it contains 16 pure states; it is given as
S ˙
⊗ S = conv({sij ⊗ skl : i, j, k, l ∈ {0, 1}}).

(9.6)

ˆ S ⊂ A(S)∗ ⊗ A(S)∗ and since s00 , s10 , s01 is a
Let us characterize the maximal tensor product. Since S ⊗
∗
ˆ
basis of A(S) , we can express any state x ∈ S ⊗ S as
X
x=
αIJ sI ⊗ sJ ,
(9.7)
I,J∈{00,10,01}

60

<!-- page 61 -->
1.5

S

E(S)

A(S)∗+

A(S)+

1.2

s00
s01

s10

1.0

1S

1S − f y

1.0

1S − f x

0.8

s11

0.6
0.4

0.5

0.2
0.0

0.0
0.5

0.5
1.0

−1.0 −0.5

1.0
1.5

1.5

(a) Picture of the state space S as a subset of A(S)∗ . The red
points are the pure states s00 , s10 , s01 , and s11 , the blue lines
are the edges of the state space S, and the black lines are the
edges of the positive cone A(S)∗+ .

fy

fx

0.0
0.0

0.0

0.5

1.0

1.5

1.5

1.0

0.5

−1.0
−0.5
0.0

(b) Picture of the effect algebra E(S) as a subset of A(S). The
red points are the effects fx , 1S − fx , fy , 1S − fy , and 1S , the
blue lines are the edges of the effect algebra E(S), and the black
lines are the edges of the positive cone A(S)+ .

Figure 4: Pictures of the state space S and effect algebra E(S).

P
where I, J are multi-indexes. Since hx, 1S ⊗ 1S i = 1 we must have I,J∈{00,10,01} αIJ = 1. We know from
ˆ S if and only if we have hx, gA ⊗ gB i ≥ 0 for all gA , gB ∈ E(S). But since E(S) is
Definition 5.4 that x ∈ S ⊗
generated by fx , 1S − fx , fy , and 1S − fy , it is sufficient to check only for gA , gB ∈ {fx , 1S − fx , fy , 1S − fy },
this yields 16 conditions. One can explicitly write down all of the 16 conditions and find the most general
form of the coefficients αIJ . This can be carried out numerically and one can find that the pure entangled
states can be characterized in terms of correlations between Alice and Bob [145–147] and that they maximally
violate the CHSH inequality, see also [7] for the construction of such states.
ˆ S as
Another option is to express x ∈ S ⊗
From hx, 1S ⊗ 1S i = 1 we get
For g ∈ E(S) we get

x = s00 ⊗ v0 + s10 ⊗ v1 + s01 ⊗ v2 .

(9.8)

hv0 + v1 + v2 , 1S i = 1.

(9.9)

hx, fx ⊗ gi = hv1 , gi,

(9.10)

hx, fy ⊗ gi = hv2 , gi,

(9.12)

hx, (1S − fx ) ⊗ gi = hv0 + v2 , gi,

(9.11)

hx, (1S − fx ) ⊗ gi = hv0 + v1 , gi.

(9.13)

λ1 y1 + µz − µ0 z 0 ≥ 0,

(9.14)

We can now express the positivity conditions hx, gA ⊗ gB i ≥ 0 in terms of v0 , v1 , and v2 . (9.10) and (9.12)
imply v1 , v2 ∈ A(S)∗+ . (9.11) and (9.13) imply v0 + v2 ∈ A(S)∗+ and v0 + v1 ∈ A(S)∗+ . Note that v0
does not have to be an element of the positive cone A(S)∗+ , this was not implied by any of the positivity
conditions and, as we will see, it will not be.
Since v1 , v2 ∈ A(S)∗+ , there must be λ1 , λ2 ∈ R+ and y1 , y2 ∈ S such that v1 = λ1 y1 , v2 = λ2 y2 . Since
v0 ∈ A(S), there must be µ, µ0 ∈ R+ and z, z 0 ∈ S such that v0 = µz − µ0 z 0 . The positivity conditions (9.11)
and (9.13) then become
λ2 y2 + µz − µ0 z 0 ≥ 0,
61

(9.15)

<!-- page 62 -->
and as a result of (9.9) we must have
Now we can prove the following lemmata:

λ1 + λ2 + µ − µ0 = 1.

(9.16)

ˆ S be a state given by (9.8), i.e.,
Lemma 9.1. Let x ∈ S ⊗
x = s00 ⊗ (µz − µ0 z 0 ) + λ1 s10 ⊗ y1 + λ2 s01 ⊗ y2 ,

(9.17)

where y1 , y2 , z, z 0 ∈ S and λ1 , λ2 , µ, µ0 ∈ R+ . If λ1 y1 ≥ µ0 z 0 and λ2 y2 ≥ µ0 z 0 , then x is separable, i.e.,
˙ S.
x∈S⊗
Proof. Using (9.3) we get
x = µs00 ⊗ z + s10 ⊗ (λ1 y1 − µ0 z 0 ) + s01 ⊗ (λ2 y2 − µ0 z 0 ) + µ0 s11 ⊗ z 0

(9.18)

from which the result easily follows.
ˆ S be a state given by (9.8), i.e.,
Lemma 9.2. Let x ∈ S ⊗
x = s00 ⊗ (µz − µ0 z 0 ) + λ1 s10 ⊗ y1 + λ2 s01 ⊗ y2 ,

(9.19)

˙ S, only if the coefficients λ1 , λ2 ,
where y1 , y2 , z, z 0 ∈ S and λ1 , λ2 , µ, µ0 ∈ R+ . x is entangled, i.e., x ∈
/ S⊗
µ, µ0 are all non-zero.
Proof. If µ0 = 0 then x is obviously separable. If λ1 = 0 (or λ2 = 0), then it follows from (9.14) (resp. from
(9.15)) that µz − µ0 z 0 ∈ A(S)∗+ and so x is separable. If µ = 0, then then it follows from (9.14) and (9.15)
that we have λ1 y1 ≥ µ0 z 0 and λ2 y2 ≥ µ0 z 0 . The result follows from Lemma 9.1.
ˆ S be a state given by (9.8), i.e.,
Lemma 9.3. Let x ∈ S ⊗
x = s00 ⊗ (µz − µ0 z 0 ) + λ1 s10 ⊗ y1 + λ2 s01 ⊗ y2 ,

(9.20)

˙ S.
where y1 , y2 , z, z 0 ∈ S and λ1 , λ2 , µ, µ0 ∈ R+ . If y1 = y2 , then x is separable, i.e., x ∈ S ⊗
Proof. Let y1 = y2 = y and without the loss of generality assume that λ1 ≤ λ2 . We have
x = s00 ⊗ (µz − µ0 z 0 ) + λ1 (s10 + s01 ) ⊗ y + (λ2 − λ1 )s01 ⊗ y
= s00 ⊗ (λ1 y + µz − µ0 z 0 ) + λ1 s11 ⊗ y + (λ2 − λ1 )s01 ⊗ y.

(9.21)
(9.22)

It follows from (9.14) that x is separable.
One can reduce the positivity conditions (9.14) and (9.15) to just one condition. Take (9.14) and denote
λ3 y3 = λ1 y1 + µz − µ0 z 0 , then we get
x = s00 ⊗ (λ3 y3 − λ1 y1 ) + λ1 s10 ⊗ y1 + λ2 s01 ⊗ y2

(9.23)

with the positivity condition λ2 y2 + λ3 y3 − λ1 y1 ≥ 0. Note that the other positivity condition is trivial as
we have λ1 y1 + λ3 y3 − λ1 y1 = λ3 y3 ≥ 0. Moreover it follows from the normalization condition (9.16) that
λ3 = 1 − λ2 . Thus we obtain the following:
Proposition 9.4. Every bipartite state x ∈ S ˆ
⊗ S is characterized by states y1 , y2 , y3 ∈ S and numbers
λ1 , λ2 ∈ [0, 1] such that
λ2 y2 + (1 − λ2 )y3 − λ1 y1 ≥ 0
(9.24)
and the state is given as
x = s00 ⊗ ((1 − λ2 )y3 − λ1 y1 ) + λ1 s10 ⊗ y1 + λ2 s01 ⊗ y2 .
62

(9.25)

<!-- page 63 -->
ˆ S is of this form. Going in the other direction, it
Proof. We have already showed that every state x ∈ S ⊗
is straightforward to check that for any states y1 , y2 , y3 ∈ S and numbers λ1 , λ2 ∈ [0, 1] satisfying (9.24),
(9.25) gives a valid bipartite state.
(9.24) implies that there is y4 ∈ S such that λ2 y2 + (1 − λ2 )y3 = λ1 y1 + (1 − λ1 )y4 . The states yi ,
i ∈ {1, . . . , 4} form a tetragon (polygon with four vertexes) inside S. These polygons corresponds to positive
maps Ψ : A(S)∗+ → A(S)∗+ defined as
1
Ψ(s10 ) = λ2 y2 ,
2

1
Ψ(s00 ) = λ1 y1 ,
2

1
Ψ(s01 ) = (1 − λ2 )y3 .
2

(9.26)

Note that Ψ is in general not a channel, because for s ∈ S, in general hΨ(s), 1S i 6= 1. Instead of that we
1
have a weaker condition hΨ(s10 ) + Ψ(s01 ), 1S i = 1. Also note that using (9.1) we get
2
1
1
Ψ(s11 ) = (Ψ(s10 ) + Ψ(s01 ) − Ψ(s00 )) = λ2 y2 + (1 − λ2 )y3 − λ1 y1 = (1 − λ1 )y4 .
2
2

(9.27)

Let x0 ∈ S ˆ
⊗ S be given as
x0 =

1
(s00 ⊗ (s01 − s00 ) + s10 ⊗ s00 + s01 ⊗ s10 )
2

(9.28)

1
(s00 ⊗ (Ψ(s01 ) − Ψ(s00 )) + s10 ⊗ Ψ(s00 ) + s01 ⊗ Ψ(s10 ))
2

(9.29)

then we have
x = (idS ⊗Ψ)(x0 ) =
or in diagrams
x

x0

=

Ψ

(9.30)

We will now formalize our results.
ˆ S, there is a positive map Ψ : A(S)∗+ → A(S)∗+ such that
Proposition 9.5. For every state x ∈ S ⊗
1
hΨ(s10 ) + Ψ(s01 ), 1S i = 1.
2

(9.31)

such that (9.30) holds, and, vice-versa, for every positive map Ψ : A(S)∗+ → A(S)∗+ satisfying (9.31) there
ˆ S such that (9.30) holds.
is a state x ∈ S ⊗
ˆ S we can find the corresponding map Ψ : A(S)∗+ → A(S)∗+
Proof. We already know that to every x ∈ S ⊗
such that (9.30) holds. So let Ψ : A(S)∗+ → A(S)∗+ be a positive map such that (9.31) holds. Since Ψ is
ˆ S)∗+ and we only need to check the
positive, it follows from Proposition 6.28 that (idS ⊗Ψ)(x0 ) ∈ A(S ⊗
normalization. We have

x0

=
Ψ

1
1
(Ψ(s01 ) − Ψ(s00 ) + Ψ(s00 ) + Ψ(s10 )) = (Ψ(s01 ) + Ψ(s10 ))
2
2

(9.32)

ˆ S.
and the normalization of (idS ⊗Ψ)(x0 ) follows from (9.31). Therefore we have (idS ⊗Ψ)(x0 ) ∈ S ⊗
ˆ S and the maximally entangled state
One can spot certain similarity between the state x0 ∈ S ⊗
|φ+ ihφ+ | ∈ D(H ⊗ H) in the sense that both states are used to construct a correspondence between entangled
states and positive maps, or completely positive channels. In fact, this similarity is not a coincidence, but
63

<!-- page 64 -->
it stems from a shared property of both S and D(H): isomorphism between A(K)+ and A(K)∗+ . We have
already argued that the cones A(D(H))+ and A(D(H))∗+ are isomorphic in Section 8. One can construct
similar isomorphism between A(S)+ and A(S)∗+ as follows: let ι : A(S) → A(S)∗ be defined as
ι(fx ) = s00 ,

ι(fy ) = s10 ,

ι(1S − fy ) = s01 .

(9.33)

Then clearly ι : A(S)+ → A(S)∗+ , i.e., ι is a positive map and it is also straightforward to show that ι is
invertible. Hence the cones A(S)+ and A(S)∗+ are isomorphic. Then one can use the result on the structure
of channels from Proposition 6.9 together with the isomorphism between A(K)+ and A(K)∗+ to construct
the correspondence.
9.3. Channels
Since we use either minimal or maximal tensor product, we know from Propositions 6.27 and 6.28 that
all positive channels are completely positive. The channels that are often used are the isomorphisms of
the state space. These are the channels that are invertible and the inverse map is a channel as well. The
isomorphisms correspond to rotations and reflections of the state space. For example, consider the channel
R : S → S given as
R(s00 ) = s10 ,

R(s10 ) = s11 ,

R(s01 ) = s00 .

(9.34)

It then follows that
R(s11 ) = R(s10 ) + R(s01 ) − R(s00 ) = s11 + s00 − s10 = s01 .

(9.35)

It easily follows that R4 = idS and so we get that the channel R is an isomorphism. Another such isomorphism is M : S → S given as
M (s00 ) = s11 ,

M (s10 ) = s10 ,

M (s01 ) = s01 .

(9.36)

Then we have M (s11 ) = s00 . We again have M 2 = idS . These isomorphism generate the whole group of
ˆ S by
isomorphisms of S. One can also relate the isomorphisms of S to the pure entangled states in S ⊗
using the result of Proposition 9.5.
9.4. Compatibility of channels
Compatibility of the measurements on the square state space was investigated before [19, 21] and one can
show that the two-outcome measurements corresponding to the effects fx and fy are maximally incompatible,
meaning that they are as incompatible as mathematically possible. This is closely related to the maximal
violations of CHSH inequality, see [6, 7].
Acknowledgement
The author is thankful to Teiko Heinosaari and Matthias Kleinmann for comments on the early version of
the manuscript and to Thomas Bullock and Peter Morgan for helpful discussions. The author acknowledges
the support by the Deutsche Forschungsgemeinschaft (DFG, GermanResearch Foundation - 447948357) and
the ERC (Consolidator Grant 683107/TempoQ).
References
[1] J. Barrett, Information processing in generalized probabilistic theories, Physical Review A 75 (3) (2007) 032304. arXiv:
0508211, doi:10.1103/PhysRevA.75.032304.
[2] H. Barnum, C. P. Gaebler, A. Wilce, Ensemble Steering, Weak Self-Duality, and the Structure of Probabilistic Theories,
Foundations of Physics 43 (12) (2013) 1411–1427. arXiv:0912.5532, doi:10.1007/s10701-013-9752-2.
[3] M. Banik, Measurement incompatibility and Schrödinger-Einstein-Podolsky-Rosen steering in a class of probabilistic
theories, Journal of Mathematical Physics 56 (5) (2015) 052101. arXiv:1502.05779, doi:10.1063/1.4919546.

64

<!-- page 65 -->
[4] G. Kar, S. Ghosh, S. Choudhary, M. Banik, Role of Measurement Incompatibility and Uncertainty in Determining
Nonlocality, Mathematics 4 (3) (2016) 52. doi:10.3390/math4030052.
[5] M. Plávala, Conditions for the compatibility of channels in general probabilistic theory and their connection to steering
and Bell nonlocality, Physical Review A 96 (5) (2017) 052127. arXiv:1707.08650, doi:10.1103/PhysRevA.96.052127.
[6] M. Plávala, M. Ziman, Popescu-Rohrlich box implementation in general probabilistic theory of processes, Physics Letters
A 384 (16) (2020) 126323. arXiv:1708.07425, doi:10.1016/j.physleta.2020.126323.
[7] A. Jenčová, M. Plávala, Structure of quantum and classical implementations of the Popescu-Rohrlich box, Physical
Review A 102 (4) (2020) 042208. arXiv:1907.08933, doi:10.1103/PhysRevA.102.042208.
[8] S. S. Bhattacharya, S. Saha, T. Guha, M. Banik, Nonlocality without entanglement: Quantum theory and beyond,
Physical Review Research 2 (1) (2020) 012068. arXiv:1908.10676, doi:10.1103/PhysRevResearch.2.012068.
[9] L. Czekaj, M. Horodecki, T. Tylec, Bell measurement ruling out supraquantum correlations, Physical Review A 98 (3)
(2018) 032117. arXiv:1802.09510, doi:10.1103/PhysRevA.98.032117.
[10] S. Popescu, D. Rohrlich, Quantum nonlocality as an axiom, Foundations of Physics 24 (3) (1994) 379–385. doi:10.1007/
BF02058098.
[11] H. M. Wiseman, S. J. Jones, A. C. Doherty, Steering, entanglement, nonlocality, and the Einstein-Podolsky-Rosen
paradox, Physical Review Letters 98 (14) (2007) 140402. arXiv:0612147, doi:10.1103/PhysRevLett.98.140402.
[12] O. C. O. Dahlsten, A. J. P. Garner, V. Vedral, The uncertainty principle enables non-classical dynamics in an interferometer, Nature Communications 5 (1) (2014) 4592. arXiv:1206.5702, doi:10.1038/ncomms5592.
[13] D. Saha, M. Oszmaniec, L. Czekaj, M. Horodecki, R. Horodecki, Operational foundations for complementarity and
uncertainty relations, Physical Review A 101 (5) (2020) 052104. arXiv:1809.03475, doi:10.1103/PhysRevA.101.052104.
[14] R. Takakura, T. Miyadera, Preparation uncertainty implies measurement uncertainty in a class of generalized probabilistic
theories, Journal of Mathematical Physics 61 (8) (2020) 082203. arXiv:2006.02092, doi:10.1063/5.0017854.
[15] R. Takakura, T. Miyadera, Entropic Uncertainty Relations in a Class of Generalized Probabilistic Theories (2020).
arXiv:2006.05671.
[16] L. L. Sun, X. Zhou, L.-c. Kwek, S. Yu, No Disturbance Without Uncertainty Under Generalized Probability Theory
(2020).
[17] H. Barnum, J. Barrett, M. Leifer, A. Wilce, Cloning and Broadcasting in Generic Probabilistic Theories (2006). arXiv:
0611295.
[18] H. Barnum, J. Barrett, M. Leifer, A. Wilce, Generalized No-broadcasting theorem, Physical Review Letters 99 (24)
(2007) 240501. arXiv:0707.0620, doi:10.1103/PhysRevLett.99.240501.
[19] P. Busch, T. Heinosaari, J. Schultz, N. Stevens, Comparing the degrees of incompatibility inherent in probabilistic
physical theories, Europhysics Letters 103 (1) (2013) 10002. arXiv:1210.4142, doi:10.1209/0295-5075/103/10002.
[20] M. Plávala, All measurements in a probabilistic theory are compatible if and only if the state space is a simplex, Physical
Review A 94 (4) (2016) 042108. arXiv:1608.05614, doi:10.1103/PhysRevA.94.042108.
[21] A. Jenčová, M. Plávala, Conditions on the existence of maximally incompatible two-outcome measurements in general
probabilistic theory, Physical Review A 96 (2) (2017) 022113. arXiv:1703.09447, doi:10.1103/PhysRevA.96.022113.
[22] S. N. Filippov, T. Heinosaari, L. Leppäjärvi, Necessary condition for incompatibility of observables in general probabilistic
theories, Physical Review A 95 (3) (2017) 032127. arXiv:1609.08416, doi:10.1103/PhysRevA.95.032127.
[23] T. Heinosaari, L. Leppäjärvi, M. Plávala, No-free-information principle in general probabilistic theories, Quantum 3
(2018) 157. arXiv:1808.07376, doi:10.22331/q-2019-07-08-157.
[24] A. Jenčová, Incompatible measurements in a class of general probabilistic theories, Physical Review A 98 (2018) 012133.
arXiv:1705.08008, doi:10.1103/PhysRevA.98.012133.
[25] Y. Kuramochi, Compatibility of any pair of 2-outcome measurements characterizes the Choquet simplex, Positivity
(2020). arXiv:1912.00563, doi:10.1007/s11117-020-00742-0.
[26] Ł. Czekaj, A. B. Sainz, J. Selby, M. Horodecki, Correlations constrained by composite measurements (2020). arXiv:
2009.04994.
[27] A. Bluhm, A. Jenčová, I. Nechita, Incompatibility in general probabilistic theories, generalized spectrahedra, and tensor
norms (2020). arXiv:2011.06497.
[28] R. W. Spekkens, Contextuality for preparations, transformations, and unsharp measurements, Physical Review A 71 (5)
(2005) 052108. arXiv:0406166, doi:10.1103/PhysRevA.71.052108.
[29] R. W. Spekkens, Evidence for the epistemic view of quantum states: A toy theory, Physical Review A 75 (3) (2007)
032110. arXiv:0401052, doi:10.1103/PhysRevA.75.032110.
[30] G. Chiribella, X. Yuan, Measurement sharpness cuts nonlocality and contextuality in every physical theory (2014).
arXiv:1404.3348.
[31] D. Schmid, J. H. Selby, E. Wolfe, R. Kunjwal, R. W. Spekkens, Characterization of Noncontextuality in the Framework
of Generalized Probabilistic Theories, PRX Quantum 2 (1) (2021) 010331. arXiv:1911.10386, doi:10.1103/PRXQuantum.
2.010331.
[32] D. Schmid, J. H. Selby, M. F. Pusey, R. W. Spekkens, A structure theorem for generalized-noncontextual ontological
models (2020). arXiv:2005.07161.
[33] M. Weilenmann, R. Colbeck, Analysing causal structures in generalised probabilistic theories, Quantum 4 (2020) 236.
arXiv:1812.04327, doi:10.22331/q-2020-02-27-236.
[34] C. M. Scandolo, R. Salazar, J. K. Korbicz, P. Horodecki, The origin of objectivity in all fundamental causal theories
(2018). arXiv:1805.12126.
[35] D. Gross, M. Müller, R. Colbeck, O. C. O. Dahlsten, All Reversible Dynamics in Maximally Nonlocal Theories are Trivial,
Physical Review Letters 104 (8) (2010) 080402. arXiv:0910.1840, doi:10.1103/PhysRevLett.104.080402.

65

<!-- page 66 -->
[36] S. W. Al-Safi, A. J. Short, Reversible dynamics in strongly non-local Boxworld systems, Journal of Physics A: Mathematical and Theoretical 47 (32) (2014) 325303. arXiv:1312.3931, doi:10.1088/1751-8113/47/32/325303.
[37] S. W. Al-Safi, J. Richens, Reversibility and the structure of the local state space, New Journal of Physics 17 (12) (2015)
123001. arXiv:1508.03491, doi:10.1088/1367-2630/17/12/123001.
[38] D. Branford, O. C. O. Dahlsten, A. J. P. Garner, On Defining the Hamiltonian Beyond Quantum Theory, Foundations
of Physics 48 (8) (2018) 982–1006. arXiv:1808.05404, doi:10.1007/s10701-018-0205-9.
[39] T. D. Galley, L. Masanes, How dynamics constrains probabilities in general probabilistic theories (2020). arXiv:2002.
05088.
[40] A. J. P. Garner, O. C. O. Dahlsten, Y. Nakata, M. Murao, V. Vedral, A framework for phase and interference in
generalized probabilistic theories, New Journal of Physics 15 (9) (2013) 093044. doi:10.1088/1367-2630/15/9/093044.
[41] O. C. O. Dahlsten, A. J. P. Garner, J. Thompson, M. Gu, V. Vedral, Particle exchange in post-quantum theories (2013).
arXiv:1307.2529.
[42] T. D. Galley, F. Giacomini, J. H. Selby, A no-go theorem on the nature of the gravitational field beyond quantum theory
(2020). arXiv:2012.01441.
[43] C. Ududec, H. Barnum, J. Emerson, Three Slit Experiments and the Structure of Quantum Theory, Foundations of
Physics 41 (3) (2011) 396–405. arXiv:0909.4787, doi:10.1007/s10701-010-9429-z.
[44] H. Barnum, C. Lee, C. Scandolo, J. Selby, Ruling out Higher-Order Interference from Purity Principles, Entropy 19 (6)
(2017) 253. arXiv:1704.05106, doi:10.3390/e19060253.
[45] M. Kleinmann, Sequences of projective measurements in generalized probabilistic models, Journal of Physics A: Mathematical and Theoretical 47 (45) (2014) 455304. arXiv:1402.3583, doi:10.1088/1751-8113/47/45/455304.
[46] B. Dakić, T. Paterek, Č. Brukner, Density cubes and higher-order interference theories, New Journal of Physics 16 (2)
(2014) 023028. arXiv:1308.2822, doi:10.1088/1367-2630/16/2/023028.
[47] C. M. Lee, J. H. Selby, Higher-Order Interference in Extensions of Quantum Theory, Foundations of Physics 47 (1) (2017)
89–112. arXiv:1510.03860, doi:10.1007/s10701-016-0045-4.
[48] C. M. Lee, J. H. Selby, Generalised phase kick-back: the structure of computational algorithms from physical principles,
New Journal of Physics 18 (3) (2016) 033023. arXiv:1510.04699, doi:10.1088/1367-2630/18/3/033023.
[49] H. Barnum, M. P. Müller, C. Ududec, Higher-order interference and single-system postulates characterizing quantum
theory, New Journal of Physics 16 (12) (2014) 123029. arXiv:1403.4147, doi:10.1088/1367-2630/16/12/123029.
[50] S. Horvat, B. Dakić, Interference as an information-theoretic game (2020). arXiv:2003.12114.
[51] H. Barnum, C. M. Lee, J. H. Selby, Oracles and Query Lower Bounds in Generalised Probabilistic Theories, Foundations
of Physics 48 (8) (2018) 954–981. arXiv:1704.05043, doi:10.1007/s10701-018-0198-4.
[52] C. M. Lee, M. J. Hoban, Bounds on the power of proofs and advice in general physical theories, Proceedings of the
Royal Society A: Mathematical, Physical and Engineering Sciences 472 (2190) (2016) 20160076. arXiv:1510.04702,
doi:10.1098/rspa.2016.0076.
[53] C. M. Lee, J. H. Selby, Deriving Grover’s lower bound from simple physical principles, New Journal of Physics 18 (9)
(2016) 093047. arXiv:1604.03118, doi:10.1088/1367-2630/18/9/093047.
[54] C. M. Lee, J. Barrett, Computation in generalised probabilisitic theories, New Journal of Physics 17 (8) (2015) 083001.
arXiv:1412.8671, doi:10.1088/1367-2630/17/8/083001.
[55] A. J. P. Garner, Interferometric Computation Beyond Quantum Theory, Foundations of Physics 48 (8) (2018) 886–909.
arXiv:1610.04349, doi:10.1007/s10701-018-0142-7.
[56] M. Krumm, M. P. Müller, Quantum computation is the unique reversible circuit model for which bits are balls, npj
Quantum Information 5 (1) (2019) 7. arXiv:1804.05736, doi:10.1038/s41534-018-0123-x.
[57] J. Barrett, N. de Beaudrap, M. J. Hoban, C. M. Lee, The computational landscape of general physical theories, npj
Quantum Information 5 (1) (2019) 41. arXiv:1702.08483, doi:10.1038/s41534-019-0156-9.
[58] R. Takagi, B. Regula, General Resource Theories in Quantum Mechanics and Beyond: Operational Characterization via
Discrimination Tasks, Physical Review X 9 (3) (2019) 031053. arXiv:1901.08127, doi:10.1103/PhysRevX.9.031053.
[59] L. Lami, B. Regula, R. Takagi, G. Ferrari, Framework for resource quantification in infinite-dimensional general probabilistic theories, Physical Review A 103 (3) (2021) 032424. arXiv:2009.11313, doi:10.1103/PhysRevA.103.032424.
[60] H. Barnum, A. Wilce, Information processing in convex operational theories, Electronic Notes in Theoretical Computer
Science 270 (1) (2011) 3–15. arXiv:0908.2352, doi:10.1016/j.entcs.2011.01.002.
[61] Howard Barnum, Jonathan Barrett, Matthew Leifer, Alexander Wilce, Teleportation in general probabilistic theories,
2012, pp. 25–47. arXiv:0805.3553, doi:10.1090/psapm/071/600.
[62] M. P. Müller, C. Ududec, Structure of Reversible Computation Determines the Self-Duality of Quantum Theory, Physical
Review Letters 108 (13) (2012) 130401. arXiv:1110.3516, doi:10.1103/PhysRevLett.108.130401.
[63] M. P. Müller, O. C. O. Dahlsten, V. Vedral, Unifying Typical Entanglement and Coin Tossing: on Randomization
in Probabilistic Theories, Communications in Mathematical Physics 316 (2) (2012) 441–487. arXiv:1107.6029, doi:
10.1007/s00220-012-1605-x.
[64] G. Chiribella, Dilation of states and processes in operational-probabilistic theories, Electronic Proceedings in Theoretical
Computer Science 172 (Qpl) (2014) 1–14. arXiv:1412.8102, doi:10.4204/EPTCS.172.1.
[65] H. Barnum, O. C. Dahlsten, M. Leifer, B. Toner, Nonclassicality without entanglement enables bit commitment, in: 2008
IEEE Information Theory Workshop, IEEE, 2008, pp. 386–390. arXiv:0803.1264, doi:10.1109/ITW.2008.4578692.
[66] L. Czekaj, M. Horodecki, P. Horodecki, R. Horodecki, Information content of systems as a physical principle, Physical
Review A 95 (2) (2017) 022119. arXiv:1403.4643, doi:10.1103/PhysRevA.95.022119.
[67] S. N. Filippov, T. Heinosaari, L. Leppäjärvi, Simulability of observables in general probabilistic theories, Physical Review
A 97 (6) (2018) 062102. arXiv:1803.11006, doi:10.1103/PhysRevA.97.062102.

66

<!-- page 67 -->
[68] J. Bae, D.-G. Kim, L.-C. Kwek, Structure of Optimal State Discrimination in Generalized Probabilistic Theories, Entropy
18 (2) (2016) 39. arXiv:1707.02521, doi:10.3390/e18020039.
[69] J. H. Selby, J. Sikora, How to make unforgeable money in generalised probabilistic theories, Quantum 2 (2018) 103.
arXiv:1803.10279, doi:10.22331/q-2018-11-02-103.
[70] J. Sikora, J. Selby, Simple proof of the impossibility of bit commitment in generalized probabilistic theories using cone
programming, Physical Review A 97 (4) (2018) 042302. arXiv:1711.02662, doi:10.1103/PhysRevA.97.042302.
[71] J. Sikora, J. H. Selby, Impossibility of coin flipping in generalized probabilistic theories via discretizations of semi-infinite
programs, Physical Review Research 2 (4) (2020) 043128. arXiv:1901.04876, doi:10.1103/PhysRevResearch.2.043128.
[72] L. Lami, C. Palazuelos, A. Winter, Ultimate Data Hiding in Quantum Mechanics and Beyond, Communications in
Mathematical Physics 361 (2) (2018) 661–708. arXiv:1703.03392, doi:10.1007/s00220-018-3154-4.
[73] Y. Yoshida, H. Arai, M. Hayashi, Perfect Discrimination in Approximate Quantum Theory of General Probabilistic
Theories, Physical Review Letters 125 (15) (2020) 150402. arXiv:2004.04949, doi:10.1103/PhysRevLett.125.150402.
[74] M. Banik, S. Saha, T. Guha, S. Agrawal, S. S. Bhattacharya, A. Roy, A. S. Majumdar, Constraining the state space in any
physical theory with the principle of information symmetry, Physical Review A 100 (6) (2019) 060101. arXiv:1905.09413,
doi:10.1103/PhysRevA.100.060101.
[75] S. Saha, S. S. Bhattacharya, T. Guha, S. Halder, M. Banik, Advantage of Quantum Theory over Nonclassical Models of
Communication, Annalen der Physik 532 (12) (2020) 2000334. arXiv:1806.09474, doi:10.1002/andp.202000334.
[76] S. Saha, T. Guha, S. S. Bhattacharya, M. Banik, Distributed Computing Model: Classical vs. Quantum vs. Post-Quantum
(2020). arXiv:2012.05781.
[77] A. J. Short, S. Wehner, Entropy in general physical theories, New Journal of Physics 12 (3) (2010) 033023. arXiv:
0909.4801, doi:10.1088/1367-2630/12/3/033023.
[78] G. Kimura, K. Nuida, H. Imai, Distinguishability measures and entropies for general probabilistic theories, Reports on
Mathematical Physics 66 (2) (2010) 175–206. arXiv:0910.0994, doi:10.1016/S0034-4877(10)00025-X.
[79] H. Barnum, J. Barrett, L. O. Clark, M. Leifer, R. Spekkens, N. Stepanik, A. Wilce, R. Wilke, Entropy and information
causality in general probabilistic theories, New Journal of Physics 14 (12) (2012) 129401. arXiv:0909.5075, doi:10.
1088/1367-2630/14/12/129401.
[80] G. Kimura, J. Ishiguro, M. Fukui, Entropies in general probabilistic theories and their application to the Holevo bound,
Physical Review A 94 (4) (2016) 042113. arXiv:1604.08009, doi:10.1103/PhysRevA.94.042113.
[81] R. Takakura, Entropy of mixing exists only for classical and quantum-like theories among the regular polygon theories,
Journal of Physics A: Mathematical and Theoretical 52 (46) (2019) 465302. arXiv:1803.07388, doi:10.1088/1751-8121/
ab4a2e.
[82] G. Chiribella, C. M. Scandolo, Entanglement and thermodynamics in general probabilistic theories, New Journal of
Physics 17 (10) (2015) 103027. arXiv:1504.07045, doi:10.1088/1367-2630/17/10/103027.
[83] G. Chiribella, C. M. Scandolo, Microcanonical thermodynamics in general physical theories, New Journal of Physics
19 (12) (2017) 123043. arXiv:1608.04460, doi:10.1088/1367-2630/aa91c7.
[84] M. Krumm, H. Barnum, J. Barrett, M. P. Müller, Thermodynamics and the structure of quantum theory, New Journal
of Physics 19 (4) (2017) 043025. arXiv:1608.04461, doi:10.1088/1367-2630/aa68ef.
[85] G. Chiribella, C. M. Scandolo, Operational axioms for diagonalizing states, Electronic Proceedings in Theoretical Computer Science 195 (Qpl) (2015) 96–115. arXiv:1506.00380, doi:10.4204/EPTCS.195.8.
[86] H. Barnum, J. Hilgert, Strongly symmetric spectral convex bodies are Jordan algebra state spaces (2019). arXiv:
1904.03753.
[87] S. Gudder, Contexts in Convex and Sequential Effect Algebras, Electronic Proceedings in Theoretical Computer Science
287 (Qpl 2018) (2019) 191–211. arXiv:1901.10640, doi:10.4204/EPTCS.287.11.
[88] A. Jenčová, M. Plávala, On the properties of spectral effect algebras, Quantum 3 (2019) 148. arXiv:1811.12407,
doi:10.22331/q-2019-06-03-148.
[89] L. Hardy, Quantum Theory From Five Reasonable Axioms (2001). arXiv:0101012.
[90] G. Chiribella, G. M. D’Ariano, P. Perinotti, Informational derivation of quantum theory, Physical Review A 84 (1) (2011)
012311. arXiv:1011.6451, doi:10.1103/PhysRevA.84.012311.
[91] C. Pfister, S. Wehner, An information-theoretic principle implies that any discrete physical theory is classical, Nature
Communications 4 (1) (2013) 1851. arXiv:1210.0194, doi:10.1038/ncomms2821.
[92] M. Kleinmann, T. J. Osborne, V. B. Scholz, A. H. Werner, Typical Local Measurements in Generalized Probabilistic
Theories: Emergence of Quantum Bipartite Correlations, Physical Review Letters 110 (4) (2013) 040403. arXiv:1205.
3358, doi:10.1103/PhysRevLett.110.040403.
[93] J. G. Richens, J. H. Selby, S. W. Al-Safi, Entanglement is necessary for emergent classicality, Physical Review Letters
119 (2017) 080503. arXiv:1705.08028, doi:10.1103/PhysRevLett.119.080503.
[94] A. Wilce, A Royal Road to Quantum Theory (or Thereabouts), Entropy 20 (4) (2018) 227. arXiv:arXiv:1507.06278,
doi:10.3390/e20040227.
[95] L. Masanes, M. P. Müller, A derivation of quantum theory from physical requirements, New Journal of Physics 13 (6)
(2011) 063001. arXiv:1004.1483, doi:10.1088/1367-2630/13/6/063001.
[96] C. M. Lee, J. H. Selby, A no-go theorem for theories that decohere to quantum mechanics, Proceedings of the Royal
Society A: Mathematical, Physical and Engineering Sciences 474 (2214) (2018) 20170732. arXiv:1701.07449, doi:
10.1098/rspa.2017.0732.
[97] J. van de Wetering, An effect-theoretic reconstruction of quantum theory, Compositionality 1 (2019) 1. arXiv:1801.05798,
doi:10.32408/compositionality-1-1.

67

<!-- page 68 -->
[98] J. van de Wetering, Sequential product spaces are Jordan algebras, Journal of Mathematical Physics 60 (6) (2019) 062201.
arXiv:1803.11139, doi:10.1063/1.5093504.
[99] M. D. Mazurek, M. F. Pusey, K. J. Resch, R. W. Spekkens, Experimentally bounding deviations from quantum theory
in the landscape of generalized probabilistic theories (2017). arXiv:1710.05948.
[100] M. Weilenmann, R. Colbeck, Self-Testing of Physical Theories, or, Is Quantum Theory Optimal with Respect to
Some Information-Processing Task?, Physical Review Letters 125 (6) (2020) 060406. arXiv:2003.00349, doi:10.1103/
PhysRevLett.125.060406.
[101] A. J. P. Garner, M. P. Müller, Characterization of the probabilistic models that can be embedded in quantum theory
(2020). arXiv:2004.06136.
[102] K. McCrimmon, Jordan algebras and their applications, Bulletin of the American Mathematical Society 84 (4) (1978)
612–628. doi:10.1090/S0002-9904-1978-14503-0.
[103] P. Jordan, J. v. Neumann, E. Wigner, On an Algebraic Generalization of the Quantum Mechanical Formalism, The
Annals of Mathematics 35 (1) (1934) 29. doi:10.2307/1968117.
[104] G. Chiribella, G. M. D’Ariano, P. Perinotti, Probabilistic theories with purification, Physical Review A 81 (6) (2010)
062348. arXiv:0908.1583, doi:10.1103/PhysRevA.81.062348.
[105] A. Bisio, P. Perinotti, Theoretical framework for higher-order quantum theory, Proceedings of the Royal Society A:
Mathematical, Physical and Engineering Sciences 475 (2225) (2019) 20180706. arXiv:1806.09554, doi:10.1098/rspa.
2018.0706.
[106] P. Perinotti, Cellular automata in operational probabilistic theories, Quantum 4 (2020) 294. arXiv:1911.11216, doi:
10.22331/q-2020-07-09-294.
[107] K. Cho, B. Jacobs, B. Westerbaan, A. Westerbaan, An Introduction to Effectus Theory (2015). arXiv:1512.05813.
[108] J. R. Munkres, Topology, Featured Titles for Topology Series, Prentice Hall, Incorporated, 2000.
[109] S. Popescu, Quantum states and knowledge: Between pure states and density matrices (2018). arXiv:1811.05472.
[110] R. T. Rockafellar, Convex Analysis, Princeton landmarks in mathematics and physics, Princeton University Press, 1997.
[111] D. J. Foulis, M. K. Bennett, Effect algebras and unsharp quantum logics, Foundations of Physics 24 (10) (1994) 1331–
1352. doi:10.1007/BF02283036.
[112] F. Kôpka, D-posets of fuzzy sets, Tatra Mountains Mathematical Publications 1 (1) (1992) 83–87.
[113] A. Dvurecenskij, S. Pulmannová, New Trends in Quantum Structures, Mathematics and Its Applications, Springer
Netherlands, 2013.
[114] S. Gudder, S. Pulmannová, Representation theorem for convex effect algebras, Commentationes Mathematicae Universitatis Carolinae 39 (4) (1998) 645–660.
[115] A. Naylor, G. Sell, Linear Operator Theory in Engineering and Science, Applied Mathematical Sciences, Springer New
York, 1982.
[116] A. Jenčová, Base norms and discrimination of generalized quantum channels, Journal of Mathematical Physics 55 (2014)
022201. arXiv:1308.4030, doi:10.1063/1.4863715.
[117] W. Rudin, Functional Analysis, International series in pure and applied mathematics, McGraw-Hill, 1991.
[118] K. Nuida, G. Kimura, T. Miyadera, Optimal observables for minimum-error state discrimination in general probabilistic
theories, Journal of Mathematical Physics 51 (9) (2010). arXiv:0906.5419, doi:10.1063/1.3479008.
[119] S. Gudder, Convex structures and operational quantum mechanics, Communications in Mathematical Physics 29 (3)
(1973) 249–264. doi:10.1007/BF01645250.
[120] P. Janotta, R. Lal, Generalized probabilistic theories without the no-restriction hypothesis, Physical Review A 87 (5)
(2013) 052131. arXiv:1412.8524, doi:10.1103/PhysRevA.87.052131.
[121] S. N. Filippov, S. Gudder, T. Heinosaari, L. Leppäjärvi, Operational Restrictions in General Probabilistic Theories,
Foundations of Physics 50 (8) (2020) 850–876. arXiv:1912.08538, doi:10.1007/s10701-020-00352-6.
[122] G. Chiribella, G. M. D’Ariano, P. Perinotti, Quantum Circuit Architecture, Physical Review Letters 101 (6) (2008)
060401. arXiv:0712.1325, doi:10.1103/PhysRevLett.101.060401.
[123] J. Selby, B. Coecke, Leaks: Quantum, Classical, Intermediate and More, Entropy 19 (4) (2017) 174. arXiv:1701.07404,
doi:10.3390/e19040174.
[124] E. Wolfe, D. Schmid, A. B. Sainz, R. Kunjwal, R. W. Spekkens, Quantifying Bell: the Resource Theory of Nonclassicality
of Common-Cause Boxes, Quantum 4 (2020) 280. arXiv:1903.06311, doi:10.22331/q-2020-06-08-280.
[125] D. Schmid, J. H. Selby, R. W. Spekkens, Unscrambling the omelette of causation and inference: The framework of
causal-inferential theories (2020). arXiv:2009.03297.
[126] D. Schmid, T. C. Fraser, R. Kunjwal, A. B. Sainz, E. Wolfe, R. W. Spekkens, Why standard entanglement theory is
inappropriate for the study of Bell scenarios (2020). arXiv:2004.09194.
[127] D. Schmid, H. Du, M. Mudassar, G. C.-d. Wit, D. Rosset, M. J. Hoban, Postquantum common-cause channels: the
resource theory of local operations and shared entanglement (2020). arXiv:2004.06133.
[128] A. Kay, Quantikz (2018). arXiv:1809.03842, doi:10.17637/rh.7000520.v4.
URL https://royalholloway.figshare.com/articles/dataset/Quantikz/7000520/4
[129] R. Ryan, Introduction to Tensor Products of Banach Spaces, Springer Monographs in Mathematics, Springer London,
2002.
[130] G. M. D’Ariano, M. Erba, P. Perinotti, Classical theories with entanglement, Physical Review A 101 (4) (2020) 042118.
arXiv:1909.07134, doi:10.1103/PhysRevA.101.042118.
[131] G. M. D’Ariano, M. Erba, P. Perinotti, Classicality without local discriminability: Decoupling entanglement and complementarity, Physical Review A 102 (5) (2020) 052216. arXiv:2008.04011, doi:10.1103/PhysRevA.102.052216.

68

<!-- page 69 -->
[132] I. Namioka, R. Phelps, Tensor products of compact convex sets, Pacific Journal of Mathematics 31 (2) (1969) 469–480.
doi:10.2140/pjm.1969.31.469.
[133] G. P. Barker, Theory of cones, Linear Algebra and its Applications 39 (1981) 263–291. doi:10.1016/0024-3795(81)
90310-4.
[134] G. Aubrun, L. Lami, C. Palazuelos, M. Plavala, Entangleability of cones (2019). arXiv:1911.09663.
[135] T. Heinosaari, T. Miyadera, M. Ziman, An Invitation to Quantum Incompatibility, Journal of Physics A: Mathematical
and Theoretical 49 (12) (2015) 123001. arXiv:1511.07548, doi:10.1088/1751-8113/49/12/123001.
[136] R. Uola, T. Kraft, J. Shang, X.-D. Yu, O. Gühne, Quantifying Quantum Resources with Conic Programming, Physical
Review Letters 122 (13) (2019) 130404. arXiv:1812.09216, doi:10.1103/PhysRevLett.122.130404.
[137] E. Haapasalo, T. Kraft, N. Miklin, R. Uola, Quantum marginal problem and incompatibility (2019). arXiv:1909.02941.
[138] M. Girard, M. Plávala, J. Sikora, Jordan products of quantum channels and their compatibility (2020). arXiv:2009.03279.
[139] C. Carmeli, T. Heinosaari, A. Toigo, State discrimination with postmeasurement information and incompatibility of
quantum measurements, Physical Review A 98 (1) (2018) 012126. arXiv:1804.09693, doi:10.1103/PhysRevA.98.012126.
[140] C. Carmeli, T. Heinosaari, A. Toigo, Quantum Incompatibility Witnesses, Physical Review Letters 122 (13) (2019)
130402. arXiv:1812.02985, doi:10.1103/PhysRevLett.122.130402.
[141] C. Carmeli, T. Heinosaari, T. Miyadera, A. Toigo, Witnessing incompatibility of quantum channels, Journal of Mathematical Physics 60 (12) (2019) 122202. arXiv:1906.10904, doi:10.1063/1.5126496.
[142] R. Uola, A. C. S. Costa, H. C. Nguyen, O. Gühne, Quantum steering, Reviews of Modern Physics 92 (1) (2020) 015001.
arXiv:1903.06663, doi:10.1103/RevModPhys.92.015001.
[143] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, S. Wehner, Bell nonlocality, Reviews of Modern Physics 86 (2) (2014)
419–478. arXiv:1303.2849, doi:10.1103/RevModPhys.86.419.
[144] T. Heinosaari, M. Ziman, The Mathematical Language of Quantum Theory. From Uncertainty to Entanglement, Cambridge University Press, 2012.
[145] J. Barrett, N. Linden, S. Massar, S. Pironio, S. Popescu, D. Roberts, Nonlocal correlations as an information-theoretic
resource, Physical Review A 71 (2) (2005) 022101. arXiv:0404097, doi:10.1103/PhysRevA.71.022101.
[146] P. Janotta, C. Gogolin, J. Barrett, N. Brunner, Limits on nonlocal correlations from the structure of the local state space,
New Journal of Physics 13 (2011). arXiv:1012.1215, doi:10.1088/1367-2630/13/6/063024.
[147] N. Brunner, M. Kaplan, A. Leverrier, P. Skrzypczyk, Dimension of physical systems, information processing, and thermodynamics, New Journal of Physics 16 (12) (2014) 123050. arXiv:1401.4488, doi:10.1088/1367-2630/16/12/123050.
[148] S. Lane, G. Birkhoff, Algebra, AMS Chelsea Publishing Series, Chelsea Publishing Company, 1999.
[149] S. Boyd, L. Vandenberghe, Convex Optimization, Berichte über verteilte messysteme, Cambridge University Press, 2004.

Appendix A. Convex cones and ordered vector spaces
Definition A.1. Let V denote a real, finite-dimensional vector space. A cone C ⊂ V is a set such that for
any v ∈ C and λ ∈ R+ we have λv ∈ C. Let X ⊂ V , then cone(X) is the smallest cone containing X, i.e.,
cone(X) = {λv : v ∈ X, λ ∈ R+ }.
A cone is a subset of V that is invariant to scaling, i.e., to multiplication by λ ∈ R+ . The following is a
simple lemma about the interplay between linear hulls and conic hulls.
Lemma A.2. Let X ⊂ V , then span(cone(X)) = cone(span(X)) = span(X).
Proof. The proof is straightforward. Since X ⊂ cone(X), it follows that span(X) ⊂ span(cone(X)).
Pn So let
v ∈ span(cone(X)), then there are wi ∈ cone(X) and αi ∈ R for i ∈ {1, . . . , n} such that v = i=1 αi wi .
But since wi ∈P
cone(X), there are λi ∈ R+ and xi ∈ X such that wi = λi xi for all i ∈ {1, . . . , n},
n
so we get v =
i=1 αi λi xi , which implies v ∈ span(X) and span(cone(X)) ⊂ span(X) follows. So we
have span(cone(X)) = span(X). To show that cone(span(X)) = span(X), simply observe that for any
v ∈ span(X) and λ ∈ R+ we must have λv ∈ span(X), so span(X) already is a cone.
Definition A.3. Let V be a real, finite-dimensional vector space equipped with the Euclidean topology
and let C ⊂ V be a cone. We say that:
• C is convex if C is a convex set, i.e., conv(C) = C;
• C is closed if C is a closed set in the Euclidean topology on V ;
• C is pointed if C ∩ −C = {0};
• C is generating if span(C) = V , i.e., if C − C = V .
69

<!-- page 70 -->
Some authors refer to convex, closed, pointed, generating cones as proper cones. We are interested in
cones because a suitable cone C ⊂ V gives the structure of ordered vector space to V .
Definition A.4. Ordered vector space is a vector space V equipped with a binary relation ≤ such that for
all v, w, x ∈ V , λ ∈ R+ we have that
(OVS1) ≤ is reflexive, i.e., v ≤ v;
(OVS2) ≤ is anti-symmetric, i.e., v ≤ w and w ≤ v implies v = w;
(OVS3) ≤ is transitive, i.e., v ≤ w and w ≤ x implies v ≤ x;
(OVS4) ≤ respects the addition on V , i.e., v ≤ w implies v + x ≤ w + x;
(OVS5) ≤ respects the multiplication by positive scalars, i.e., v ≤ w implies λv ≤ λw.
Definition A.5. Let (V, ≤) be an ordered vector space. We say that V is a directed set under the ordering
≤ if for every v1 , v2 ∈ V there is w ∈ V such that v1 ≤ w and v2 ≤ w.
We will show that we can construct a natural cone from the order ≤ and that we can construct an order
on V given a suitable cone C ⊂ V . Let V be a real, finite-dimensional vector space, equipped with the
relation ≤, so that (V, ≤) is an ordered vector space. Let
C = {v ∈ V : 0 ≤ v}

(A.1)

be the set of positive elements, we will show that C is a convex, pointed, generating cone. Note that we will
use ≥ instead of ≤ when better suited, we have v ≥ w whenever w ≤ v.
Proposition A.6. Let V be an ordered vector space and let C ⊂ V be a positive cone as given by (A.1),
then C is a convex and pointed cone.
Proof. Let x ∈ C and λ ∈ R+ , then 0 ≤ x and 0 ≤ λx follows from (OVS5) so C is a cone. Let x, y ∈ C and
λ ∈ [0, 1], then we have since 0 ≤ x and 0 ≤ y. From (OVS5) we get 0 ≤ λx and 0 ≤ (1 − λ)y and we get
0 ≤ λx + (1 − λ)y from (OVS4) and (OVS3). It follows that C is convex. Assume that x ∈ C and x ∈ −C,
i.e., that we have 0 ≤ x and 0 ≤ −x. Using (OVS4) we get x ≤ 0 and then from (OVS2) we get x = 0. It
follows that C ∩ −C = {0}, so C is pointed.
Proposition A.7. Let (V, ≤) be an ordered vector space such that V is a directed set under the ordering ≤.
Then the positive cone C ⊂ V given by (A.1) is generating.
Proof. Let v ∈ V , then for the pair of elements v, −v there must be w ∈ V such that v ≤ w and −v ≤ w.
This implies that 0 ≤ w − v and 0 ≤ w + v, so w − v ∈ C and w + v ∈ C. Since we have
v=

w+v w−v
−
,
2
2

(A.2)

it follows that v ∈ span(C).
Thus we have showed that an ordered vector space (V, ≤) contains the positive cone C. Now, we will
start by assuming that we have a suitable cone C ⊂ V and we will show that then we can construct the
ordering ≤. Therefore we will show complete equivalence between ordered vector spaces and vector spaces
with cones.
Let C ⊂ V be a cone, then we can invert the logic of (A.1) and say that for v ∈ V we have 0 ≤ v if and
only if v ∈ C, i.e., we can simply say that C is the positive cone given by some order ≤. For v, w ∈ V we
then have v ≤ w if and only if 0 ≤ w − v, so in principle we can construct the order ≤ from the cone C.
But the order ≤ satisfies (OVS1) - (OVS5) only if the cone C is convex and pointed.
70

<!-- page 71 -->
Proposition A.8. Let C ⊂ V be a convex and pointed cone and let ≤ be given for v, w ∈ V as
v≤w

⇔

w − v ∈ C,

(A.3)

then (V, ≤) is an ordered vector space.
Proof. The proof is rather straightforward. Let v, w, x ∈ V and λ ∈ R+ , then we have v − v = 0 ∈ C, so
v ≤ v and (OVS1) holds. Let v − w ∈ C and w − v ∈ C, then since w − v = −(v − w) and since C is
pointed, we have v − w = 0, so we get v = w and (OVS2) holds. Let w − v ∈ C and x − w ∈ C, then we
have x − v = (x − w) + (w − v) ∈ C because C is convex cone, so (OVS3) holds. Let w − v ∈ C, then we
have (w + x) − (v + x) = w − v ∈ C and so (OVS4) holds. We also have λw − λv = λ(w − v) ∈ C since C is
a cone, so (OVS5) holds as well.
Proposition A.9. Let C ⊂ V be a convex, pointed cone and let ≤ be the order constructed from C as in
(A.3). Let C be a generating cone, then V is directed set under ≤.
Proof. Let v1 , v2 ∈ V , then since C is generating, there are x1 , x2 , y1 , y2 ∈ C such that v1 = x1 − y1 and
v2 = x2 − y2 . Let x = x1 + x2 , then we have x − v1 = x2 + y1 ∈ C and x − v2 = x1 + y2 ∈ C, i.e., we have
v1 ≤ x and v2 ≤ x.
Thus we have proved that convex, pointed cones are in one-to-one correspondence with ordered vector
spaces. Moreover the cone is generating if and only if V is a directed set.
We have not included the closeness of C into the discussion, but one can easily show the following:
let {vn } ⊂ V be a Cauchy sequence and let w ∈ V , then C is closed if and only if w ≤ vn implies
w ≤ limn→∞ vn .
Appendix B. Functionals, duals and hyperplane separation theorems
Let V be a real finite-dimensional vector space. Functional ψ : V → R is a linear map from V to R,
i.e., for v, w ∈ A(K) and α, β ∈ R we have ψ(αv + βw) = αψ(v) + βψ(w). It is straightforward to define
a linear combination of functionals, let ψ, ϕ be linear functional on V , α, β ∈ R and v ∈ V , then we define
(αψ + βϕ)(v) = αψ(v) + βϕ(v). It follows that the set of all functionals ψ : V → R is a vector space.
Definition B.1. Let V be a real, finite-dimensional vectors space. The dual vector space V ∗ is the vector
space of all functionals ψ : V → R.
Given a basis {v1 , . . . , vn } ⊂ V we can define corresponding basis in V ∗ .
Definition B.2. Let {v1 , . . . , vn } ⊂ V be a basis of V , then the dual basis is a basis {ψ1 , . . . , ψn } ⊂ V ∗
such that
ψi (vj ) = δij ,
(B.1)
where δij is the Kronecker delta,
(
δij =

1 i=j
0 i 6= j

(B.2)

One can show that a dual basis always exists, see [148]. The proof is rather simple, one can start with
any basis of V ∗ and solve a series of linear equations to construct the dual basis. Another option is to realize
that given a real, finite-dimensional vector space V , we can always introduce the Euclidean inner product
and use that inner product to construct the dual basis.
A natural question arises: what is the dual of the dual? For a general vector space, this is a non-trivial
question, but since we are working with finite-dimensional vector spaces, the question considerably simplifies.
Before we proceed, note that we can naturally identify vectors v ∈ V with the functionals on functionals,
ξ ∈ V ∗∗ , ξ : V ∗ → R.
71

<!-- page 72 -->
Proposition B.3. Let v ∈ V , then we can identify v with a functional on functionals ξv ∈ V ∗∗ .

Proof. The construction is rater simple, let ψ ∈ V ∗ then we define ξv (ψ) = ψ(v). In other words, for ψ ∈ V ∗
the map ξv : ψ 7→ ψ(v) is a functional on V ∗ .
We should, in principle, work with an isomorphism v 7→ ξv rather that simply putting ξv = v, but since
this isomorphism is linear, we will omit it.
Proposition B.4. Let V be a real, finite-dimensional vector space, then V = V ∗∗ .
Proof. Let {v1 , . . . , vn } ⊂ V be aP
basis of V and let {ψ1 , . . . , ψn } ⊂ V ∗ be the dual basis. Let ξ ∈ V ∗∗ ,
n
we will show
i=1 ξ(ψi )vi and so ξ ∈ V . Let j ∈ {1, . . . , n}, then
Pnwe clearly have
Pn that we have ξ =
∗
ξ(ψ
)ψ
(v
).
It
then
follows
that
for
every
ψ
∈
V
we
have
ξ(ψ)
=
ξ(ψ
)
=
i
j
i
j
i=1 ξ(ψi )ψ(vi ) =
i=1
Pn
( i=1 ξ(ψi )vi )(ψ) and the result follows.
We will now look at the structure of the dual vector space V ∗ given that the vector space V is an ordered
vector space, see Definition A.4. So let V be a real, finite-dimensional vector space and let C ⊂ V be convex
cone. C induces a cone C ∗ ⊂ V ∗ , C ∗ is called the dual cone.
Definition B.5. Let V be a real, finite-dimensional vector space and let C ⊂ V be a cone. The dual cone
C ∗ ⊂ V ∗ is defined as
C ∗ = {ψ ∈ V ∗ : ψ(x) ≥ 0, ∀x ∈ C}.
(B.3)
In other words, the dual cone is the cone of all functionals ψ ∈ V ∗ that are positive on all the elements
of C, i.e., ψ is positive on all positive vectors. It is straightforward that C ∗ is a cone.
We will show that the dual cone C ∗ is always convex and closed, and that C ∗ is generating if C is pointed
and vice-versa.

Proposition B.6. Let V be a real, finite-dimensional vector space and let C ⊂ V be a cone. The dual cone
C ∗ is convex and closed in the standard topology given by the Euclidean inner product.
Proof. Let ψ1 , ψ2 ∈ C ∗ and λ ∈ [0, 1] and let x ∈ C. we have
(λψ1 + (1 − λ)ψ2 )(x) = λψ1 (x) + (1 − λ)ψ2 (x) ≥ 0

(B.4)

∗
∗
and so λψ1 + (1 − λ)ψ2 ∈ C ∗ . Now let {ψn }∞
n=1 ⊂ C be a Cauchy sequence, i.e., there is ψ ∈ V such that
ψ = limn→∞ ψn . For every x ∈ C we have ψ(x) = limn→∞ ψn (x), but since ψn (x) ≥ 0 we must also have
ψ(x) ≥ 0 and so ψ ∈ C ∗ .

Proposition B.7. Let V be a real, finite-dimensional vector space and let C ⊂ V be a generating cone.
Then the dual cone C ∗ is pointed.
Proof. Remember that C is generating if C − C = V and C ∗ is pointed if C ∗ ∩ (−C ∗ ) = {0}. Let
ψ ∈ C ∗ ∩ (−C ∗ ), then it follows that for any x ∈ C we must have ψ(x) ≥ 0 and ψ(x) ≤ 0 and so
ψ(x) = 0 follows. Since C is generating, for every v ∈ C there are y, y 0 ∈ C such that v = y − y 0 . We then
have ψ(v) = ψ(y) − ψ(y 0 ) = 0 and so ψ = 0.
Proposition B.8. Let V be a real, finite-dimensional vector space and let C ⊂ V be a pointed cone. Then
the dual cone C ∗ is generating.
Proof. Remember that C is pointed if C ∩ (−C) = {0} and C ∗ is generating if C ∗ − C ∗ = V ∗ . Assume that
C ∗ is not generating, then there is ψ ∈ V ∗ , ψ 6= 0 such that ψ ∈
/ C ∗ − C ∗ . It follows that there is v ∈ V
∗
∗
such that ψ(v) 6= 0 but for all ϕ ∈ C − C we have ϕ(v) = 0. One can construct such v using the dual
basis of V ∗ . It follows that 0 6= v ∈ C ∩ (−C), which is a contradiction with C being pointed.
We will now present two variants of an important theorem known as the Hanh-Banach hyperplane
separation theorem. Note that affine function is very similar concept to linear functional, but for ψ ∈ V ∗
we must have ψ(0) = 0, while for an affine function f : V → R we can have f (0) 6= 0. If f : V → R is an
affine function such that f (0) = 0, then f ∈ V ∗ .
72

<!-- page 73 -->
Theorem B.9 (Hyperplane separation theorem). Let V be a real, finite-dimensional vector space and let
X, Y ⊂ V be disjoint convex sets. Then there exists an affine function f : V → R, that is a function such
that for v, w ∈ V and α ∈ R we have
f (αv + (1 − α)w) = αf (v) + (1 − α)f (w),

(B.5)

max f (x) ≤ 0 ≤ max f (y).

(B.6)

such that
v∈X

w∈Y

In other words, f is non-positive on X and non-negative on Y .
Proof. See [149, Section 2.5.1].
Theorem B.10 (Strict hyperplane separation theorem). Let V be a real, finite-dimensional vector space
equipped with Euclidean topology, let X ⊂ V be a convex, closed sets and let y ∈ V such that y ∈
/ X. Then
there exists an affine function f : V → R such that
max f (x) < 0 < f (y).
v∈X

(B.7)

Proof. See [149, Section 2.5.1].
as

We have now all the tools we need to characterize the dual cone of the dual cone, i.e., the cone C ∗∗ given
C ∗∗ = {ξ ∈ V ∗∗ : ξ(ψ) ≥ 0, ∀ψ ∈ C ∗ }.

(B.8)

Proposition B.11. Let V be a real, finite-dimensional vector space and let C ⊂ V be a convex, closed cone.
Then C ∗∗ = C.
Proof. Since V = V ∗∗ , see Proposition B.4, we must have C ∗∗ ⊂ V . Let v ∈ C ∗∗ be such that v ∈
/ C.
According to Theorem B.10 there is an affine function f : V → R such that
f (v) < 0 < min f (x).
x∈C

(B.9)

Now let ψ ∈ V ∗ be given for w ∈ V as ψ(w) = f (w)−f (0). It is easy to check that ψ is linear: for w0 , w00 ∈ V
and α, β ∈ R we have αw0 + βw00 = αw0 + βw00 + (1 − α − β)0 and so
ψ(αw0 + βw00 ) = f (αw0 + βw00 + (1 − α − β)0) − f (0)

= αf (w0 ) + βf (w00 ) + (1 − α − β)f (0) − f (0)

(B.10)
(B.11)

0

00

(B.12)

0

00

(B.13)

= αf (w ) + βf (w ) − (α + β)f (0)
= αψ(w ) + βψ(w ).

Using (B.9) we get
ψ(v) < min ψ(x)
x∈C

(B.14)

but since 0 ∈ C and ψ(0) = 0, we must have minx∈C ψ(x) ≤ 0 and ψ(v) < 0. If minx∈C ψ(x) = 0, then
ψ ∈ C ∗ and ψ(v) < 0 is a contradiction with v ∈ C ∗∗ . So assume that minx∈C ψ(x) < 0, then there is y ∈ C
such that ψ(y) < 0. Let
2ψ(v)
(B.15)
α=
ψ(y)
then we have αy ∈ C and
ψ(αy) =

2ψ(v)
ψ(y) = 2ψ(v) < ψ(v)
ψ(y)

which is a contradiction with (B.14).
73

(B.16)

<!-- page 74 -->
Appendix C. Bilinear forms, linear maps and tensor products
We are going to review several basic results and constructions on tensor products of vector spaces. We
will be using the same approach as presented in [129]. We will show how one can relate bilinear functionals,
linear maps and tensor products of vector spaces. We will start from bilinear forms:
Definition C.1. Let VA , VB be real, finite-dimensional vector spaces. A bilinear form is a map B :
VA × VB → R, where VA × VB denotes the Cartesian product of VA and VB , such that B is linear in VA and
VB , i.e., such that for vA , wA ∈ VA , vB , wB ∈ VB and α, β ∈ R we have
B(αvA + βwB , vB ) = αB(vA , vB ) + βB(wA , vB ),

(C.1)

B(vA , αvB + βwB ) = αB(vA , vB ) + βB(vA , wB ).

(C.2)

As first, we will show that every bilinear forms are in one-to-one correspondence with linear maps.
Proposition C.2. Let VA , VB be real, finite-dimensional vector spaces. Linear maps L : VA → VB are in
one-to-one correspondence with bilinear forms B : VA × VB∗ → R via
ψB (L(vA )) = B(vA , ψB ),

(C.3)

where vA ∈ VA and ψB ∈ VB∗ .
Proof. It is straightforward to check that given a linear map L : VA → VB , we can define a bilinear form
B : VA × VB∗ → R via (C.3). Now given a bilinear form B : VA × VB∗ → R, fix vA ∈ VA and define ξB ∈ VB∗∗
as ξB (ψB ) = B(vA , ψB ), where ψB ∈ VB∗ . It is straightforward to check that ξB is linear, so ξB ∈ VB∗∗ = VB ,
where we used the result of Proposition B.4. Now we can define a map L : VA → VB as L(vA ) = ξB . It is
again straightforward to check that L is linear. Let ψB ∈ VB∗ , then note that we have ξB (ψB ) = ψB (ξB ) as
a result of the isomorphism between VB and VB∗∗ . We have ψB (L(vA )) = ψB (ξB ) = B(vA , ψB ) and so (C.3)
holds.
Similar to linear functionals, also the set of all bilinear forms is a vector space. This is easy to see, let
B1 , B2 : VA × VB → R be bilinear forms and let α, β ∈ R, then we define
(αB1 + βB2 )(vA , vB ) = αB1 (vA , vB ) + βB2 (vA , vB ),

(C.4)

where vA ∈ VA and vB ∈ VB . We will now look at the functionals on the vector space of bilinear forms, we
will see that this leads to tensor products.
Let vA ∈ VA , vB ∈ VB and let B : VA × VB → R be a bilinear form, then the map B 7→ B(vA , vB ) is a
linear functional on the vector space of bilinear forms. We will use vA ⊗ vB to denote this functional, i.e.,
we have (vA ⊗ vB )(B) = B(vA , vB ). It is straightforward to check that for vA , wA ∈ VA , vB , wB ∈ VB and
α, β ∈ R we have
(αvA + βwA ) ⊗ vB = αvA ⊗ vB + βwA ⊗ vB ,

(C.5)

vA ⊗ (αvB + βwB ) = αvA ⊗ vB + βvA ⊗ wB .

(C.6)

(vA + wA ) ⊗ (vB + wB ) 6= vA ⊗ vB + wA ⊗ wB

(C.7)

B(vA + wA , vB + wB ) 6= B(vA , vB ) + B(wA , wB ).

(C.8)

But note that in general
simply because

Definition C.3. Let VA , VB be real, finite-dimensional vector spaces, then their tensor product is the vector
space
VA ⊗ VB = span({vA ⊗ vB : vA ∈ VA , vB ∈ VB }).
(C.9)
Before we proceed, we will prove two simple results about the structure of VA ⊗ VB .
74

<!-- page 75 -->
Lemma C.4. Let VA , VB be real, finite-dimensional vector spaces and let {v1,A , . . . , vnA ,A } ⊂ VA and
A ,nB
⊂ VA ⊗ VB is a basis
{v1,B , . . . , vnB ,B } ⊂ VB be bases of VA and VB respectively. Then {vi,A ⊗ vj,B }ni,j=1
of VA ⊗ VB .
Proof. The result follows easily from Definition C.3. We only need to show that every vector of the form
A ,nB
, but
wA ⊗ wB , where wA ∈ VA and wB ∈ VB , can be written as linear combination of {vi,A ⊗ vj,B }ni,j=1
this is obvious.

Lemma C.5.
uAB ∈ VA ⊗ VB , then there are {v1,A , . . . , vn,A } ⊂ VA and {w1,A , . . . , wn,B } ⊂ VB such
PnLet
A
vi,A ⊗ wi,B , where {v1,A , . . . , vn,A } is a basis of VA .
that uAB = i=1

Proof. The result follows from Lemma C.4. Let {v1,A , . . . , vnA ,A } ⊂ VA and {v1,B , . . . , vnB ,B } ⊂ VB be
bases of VA and VB respectively, then there are numbers αij ∈ R, i ∈ {1, . . . , nA } and j ∈ {1, . . . , nB } such
that
nB
nA X
X
αij vi,A ⊗ vj,B .
(C.10)
uAB =
i=1 j=1

We then have
uAB =

nA
X
i=1



nB
X
vi,A ⊗ 
αij vj,B  .

(C.11)

j=1

which is the form of uAB we wanted to obtain.
One can actually show that VA ⊗ VB is the dual of the vector space of bilinear forms B : VA × VB → R
by constructing a basis of the vector space of bilinear forms and showing that the dual basis is included in
VA ⊗ VB .
Proposition C.6. VA ⊗ VB is the dual vector space to the vector space of bilinear forms B : VA × VB → R.

Proof. Let {v1,A , . . . , vnA ,A } ⊂ VA and {v1,B , . . . , vnB ,B } ⊂ VB be basis of VA and VB respectively. Let Bij :
VA × VB → R, where i ∈ {1, . . . , nA } and j ∈ {1, . . . , nB } be bilinear forms given as Bij (vk,A , v`,B ) = δik δj` ,
A ,nB
where δik , δj` are the Kronecker deltas. The set {Bij }ni,j=1
is the basis of the vector space of bilinear forms:
let B : VA × VB → R, then for any wA ∈ VA , wB ∈ VB we have
B(wA , wB ) =

nB
na X
X

B(vi,A , vj,B )Bij (wA , wB ),

(C.12)

i=1 j=1

which one can easily verify by writing wA and wB as linear combinations of the bases. It is now straightA ,nB
forward to verify that {vi,A ⊗ vj,B }ni,j=1
is the dual basis to Bij , from which the result follows.
It is a simple corollary of Proposition C.6 that the dual of VA ⊗ VB is the vector space of the bilinear
forms B : VA × VB → R. But we can also construct VA∗ ⊗ VB∗ and for ψA ∈ VA∗ , ψB ∈ VB∗ we can define
(ψA ⊗ ψB )(vA ⊗ vB ) = ψA (vA )ψB (vB ).

(C.13)

It follows that (up to an isomorphism that we will omit) that ψA ⊗ψB ∈ (VA ⊗VB )∗ and VA∗ ⊗VB∗ ⊂ (VA ⊗VB )∗ .
We will prove the other inclusion as well.
Proposition C.7. VA∗ ⊗ VB∗ = (VA ⊗ VB )∗ .

Proof. Let {v1,A , . . . , vnA ,A } ⊂ VA , {v1,B , . . . , vnB ,B } ⊂ VB be bases of VA and VB respectively and let
{ψ1,A , . . . , ψnA ,A } ⊂ VA∗ , {ψ1,B , . . . , ψnB ,B } ⊂ VB∗ be the dual bases. The according to Lemma C.4 we have
A ,nB
A ,nB
that {vi,A ⊗ vj,B }ni,j=1
and {ψi,A ⊗ ψj,B }ni,j=1
are the bases of VA ⊗ VB and VA∗ ⊗ VB∗ . We have
(ψi,A ⊗ ψj,B )(vk,A ⊗ vl,B ) = ψi,A (vk,A )ψj,B (vl,B ) = δik δjl

(C.14)

A ,nB
A ,nB
and so {ψi,A ⊗ ψj,B }ni,j=1
is the dual basis to {vi,A ⊗ vj,B }ni,j=1
. It follows that the linear hull of {ψi,A ⊗
nA ,nB
∗
∗
∗
ψj,B }i,j=1 must be (VA ⊗ VB ) and thus we get VA ⊗ VB = (VA ⊗ VB )∗ .

75

<!-- page 76 -->
Finally, we can prove the following isomorphisms between the tensor product of vector spaces, the vector
space of bilinear forms and the vectors space of linear maps.
Proposition C.8. Let VA , VB be real, finite-dimensional vector spaces. Then the following vector spaces
are isomorphic:
• VA ⊗ VB ,
• vector space of bilinear forms B : VA∗ × VB∗ → R,
• vector space of linear maps L : VA∗ → VB ,
Proof. We already know that the vector space of bilinear forms B : VA∗ × VB∗ → R and the vector space of
linear maps L : VA∗ → VB are isomorphic as a result of Proposition C.2.
The vector space of bilinear forms B : VA∗ × VB∗ → R is the dual of VA∗ ⊗ VB∗ as a result of Proposition C.6
and VA∗ ⊗ VB∗ = (VA ⊗ VB )∗ as a result of Proposition C.7. But then using the result of Proposition B.4 that
V ∗∗ is isomorphic to V it follows that the vector space of bilinear forms B : VA∗ × VB∗ → R is isomorphic to
(VA∗ ⊗ VB∗ )∗ . The result follows from Proposition C.7 as we have (VA∗ ⊗ VB∗ )∗ = VA ⊗ VB .
Corollary C.9. For vAB ∈ VA ⊗VB there is a bilinear form Bv : VA∗ ×VB∗ → R and linear map Lv : VA∗ → VB
such that for every ψA ∈ VA∗ and ψB ∈ VB∗ we have
(ψA ⊗ ψB )(vAB ) = Bv (ψA , ψB ) = ψB (L(ψA )).

(C.15)

Proof. The result follows from Proposition C.8. Bv and Lv can be obtained from vAB using the corresponding
isomorphisms given by Propositions C.2 and C.6.

76
