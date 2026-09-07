---
type: paper
date: 2013-02-11
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1302.2632v1)
reviewed: false
---

# Generalized Probabilistic Theories Without the No-Restriction Hypothesis

Machine-generated and unreviewed text extraction of arXiv:1302.2632v1
(15 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1302.2632v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Generalized Probabilistic Theories Without the No-Restriction Hypothesis
Peter Janotta1 and Raymond Lal2
1 Universität Würzburg, Am Hubland, Fakultät für Physik und Astronomie, 97074 Würzburg, Germany
2 University of Oxford, Department of Computer Science,

arXiv:1302.2632v1 [quant-ph] 11 Feb 2013

Quantum Group, Wolfson Building, Parks Road, Oxford OX1 3QD, UK.
The framework of generalized probabilistic theories (GPTs) is a popular approach for studying the physical
foundations of quantum theory. The standard framework assumes the no-restriction hypothesis, in which the
state space of a physical theory determines the set of measurements. However, this assumption is not physically
motivated. We generalize the framework to account for systems that do not obey the no-restriction hypothesis.
We then show how our framework can be used to describe new classes of probabilistic theories, for example
those which include intrinsic noise. Relaxing the restriction hypothesis also allows us to introduce a ‘selfdualization’ procedure, which yields a new class of theories that share many features of quantum theory, such as
obeying Tsirelson’s bound for the maximally entangled state. We then characterize joint states, generalizing the
maximal tensor product. We show how this new tensor product can be used to describe the convex closure of
the Spekkens toy theory, and in doing so we obtain an analysis of why it is local in terms of the geometry of its
state space. We show that the unrestricted version of the Spekkens toy theory is the theory known as ‘boxworld’
that allows maximal nonlocal correlations.
I.

INTRODUCTION

The framework of generalized probabilistic theories (GPTs)
is a modern operational approach for studying the physical
foundations of quantum theory [1]. The framework is operational because a theory is defined according to the observable measurement statistics that it predicts. In contrast, quantum theory is usually defined using an abstract mathematical
formalism without physical motivation (e.g. the density matrix formalism). Assuming only basic principles, the framework encompasses a large variety of theories. For example,
quantum theory and classical probability theory are special
cases of GPTs. The focus of work on GPTs is to identify
the unique physical properties that distinguish quantum theory from other theories. More generally, one can examine
the relationship between different physical properties, such as
no-cloning and nonlocality, without restricting to a particular
physical theory.
Using this framework, it has been shown that many properties that were thought to be particular to quantum theory are
in fact very general. As a sample of such results, it was shown
that any non-classical probability theory (in the sense to be
described in section II) has the following properties: the existence of entanglement [1]; for mixed states, the lack a unique
decomposition into a unique ensemble of pure states; generalizations of the no-cloning or no-broadcasting theorem [2];
and, an information-disturbance trade-off [3]. Notably, recent
attempts to reconstruct quantum theory from physical axioms
include the assumptions made in GPTs [4] or very similar assumptions [5, 6].
A GPT is defined by a set of preparations, a set of measurements, and composition rules for multipartite systems called
the tensor product of the theory. In general there is a trade-off
between possible preparations and possible measurement outcomes: the larger the set of preparations, the smaller the upper
bound on the set of allowed measurements [7]. In the existing
GPT framework, it is usually assumed that this upper bound
is saturated. This means that, for a chosen set of states, all
potential measurement outcomes that yield probability-valued

results are assumed to be physically realizable. This is called
the no-restriction hypothesis [6]. This assumption is not based
on any physical motivation, and it is usually assumed for the
sake of mathematical convenience. In this work we take on
the task of extending the framework of GPTs when the norestriction hypothesis is abandoned. This extension of GPTs
therefore brings the framework closer to the operational motivation for which it was originally initiated.
Our contribution. The idea of removing the no-restriction
hypothesis (or replacing it with other assumptions) has appeared sporadically in other works [6, 8]. However, until now
a systematic analysis of the consequences of doing so has been
lacking. In this paper we provide a well-defined framework
with the no-restriction hypothesis omitted, whilst keeping the
other assumptions of the GPT framework. Our work then proceeds in two parts.
In the first part we show that this new framework encompasses more theories than before. For example, we show that
theories with intrinsic noise can be described in our framework, but not in the existing GPT framework. We also provide a procedure for constructing a self-dual theory from a
theory which is not self-dual. The importance of this is that
self-duality has been shown to imply ‘quantum-like’ (for example, limiting bipartite nonlocality to Tsirelson’s bound for
the maximally entangled state [9]). Hence this allows us to
introduce a new class of probabilistic theories with ‘quantumlike’ behaviour, and crucially, this is a class of theories which
does not satisfy the no-restriction hypothesis.
In the second part, we develop the treatment of composite
systems. In particular, we show that our extension requires
a new (and more general) definition of the tensor product for
describing composite systems. This significantly extends the
GPT framework, since it allows us to analyse the relationship between nonlocality and the geometry of the state space
of a theory, building on previous work in this direction. For
example, we show how the Spekkens toy theory (for which
the connection to GPTs had not been previously established)
can be viewed as a GPT, but only in our more general framework. Moreover, this allows us to give an analysis of why the

<!-- page 2 -->
2
Spekkens theory is local, using the geometry of its state space.
Structure of the paper. In section II we give a brief
overview of the framework of GPTs. We then begin the first
part of our analysis, concentrating on single systems. In section III we describe in detail the no-restriction hypothesis, and
some consequences of relaxing this assumption. In section
IV we develop the important example of theories with noise.
In section V we introduce the self-dualization procedure, and
discuss the class of theories that this introduces. We then enter the second part of our analysis, which concerns composite
systems. In section VI we explain how joint states of composite systems are usually described. In section VII we show
why a new definition of composite systems is needed, and we
introduce this definition. We then study examples of theories
such as the Spekkens model.
II.

GENERALIZED PROBABILISTIC THEORIES: A
BRIEF SUMMARY

A physical experiment consists of the following steps: the
preparation of a system, transformations of that system (e.g.
by inherent dynamics), and a measurement. In general, the
measurement will different outcomes, each occurring with
some probability. Defining a generalized probabilistic theory
amounts to specifying these probabilities for any such combination of preparation, transformation and measurement. Note
that transformations can be absorbed into either the preparation or the measurement. Hence to define the allowed probability distributions of a GPT, it suffices to define the set of
preparation procedures and the set of measurements.

1.

States and effects

Consider a class of preparation procedures which all yield
exactly the same measurement statistics. The members of this
class are experimentally indistinguishable. Since a GPT concerns only experimental statistics, we can define a state of a
system as such an equivalence class. Analogously we also
define an effect as an equivalence class of measurement outcomes. We will refer to this identification of states and effects
with their respective measurement statistics as the equivalence
principle. Mathematically, states are represented by elements
of a vector space V . Effects are linear functionals on states,
i.e. elements of the dual space V ∗ . Applying an effect e to
a state ω yields the probability p(e|ω) = e(ω) for the corresponding measurement outcome to occur when measuring the
system in the state. Without loss of generality we will choose
a specific representation of states and effects in this paper to
demonstrate the abstract concepts. Both states and effects will
be represented by vectors embedded in Rn . The application of
effects on states is given by the Euclidean inner product of the
respective vectors:
e = (ε1 , · · · , εn )T

ω = (w1 , · · · , wn )T
T

p(e|ω) = e · ω = ∑ εi wi
i

(1)
(2)

The GPT framework also accounts for ensembles of preparations or measurements, in which there is uncertainty about
which measurement is implemented, or which state has been
prepared. This could occur if there is a probabilistic selection
of the preparation procedure, for example. This probability
distribution is represented by using mixed states and mixed
effects, given by convex combinations:
e = ∑ λi ei

λi ≥ 0, ∑ λi = 1

(3)

ω = ∑µj ωj

µi ≥ 0, ∑ µi = 1

(4)

i

i

i

i

corresponding to ensembles {λi , ei } and {µi , ωi }. Consequently, states and effects form convex sets. If the only convex
decomposition of a state ω is such that ω ∝ ωi for all i, then
the state is a pure state. Similarly, if the only convex decomposition of an effect e using Eq. 1 is such that e ∝ ei for all i,
then the effect is a pure effect.
Since effects and states act linearly on each other, the probability distribution for the ensembles is the weighted sum of the
probabilities pi j = ei (ω j ) of individual ensemble elements:
e(ω) = ∑ λi µ j ei (ω j ).

(5)

i, j

More generally, consider the result of applying different measurements to systems prepared by the same method. In general, there will be measurement outcomes with probabilities
that are linearly dependent for a fixed state. Analogously, one
might find linear dependencies between the probabilities for
a fixed measurement outcome under variations of the state
that is prepared. This implies a linear dependence between
the vector space elements ω ∈ V representing the states; there
is a corresponding linear dependence for the effects e ∈ V ∗ .
This determines the dimension of V as the minimal number
of different measurement outcomes needed to identify a state
uniquely (this is called the ‘fiducial set’ of measurement outcomes by Hardy [10]). In this paper we restrict ourselves to
systems for which the vector space V has finite dimension.
Hence the dimension of V is equal to the dimension of the
dual space V ∗ , which is the minimal number of preparations
required to identify an effect.

2.

Normalization and measurements

A central concept in the GPT framework is the description
of perfect preparations and measurements. A perfect preparation is one that is guaranteed to succeed. It is represented by a
normalized state, where normalization defined with respect to
a special effect, called the unit measure u. The set of all normalized states is called the state space Ω. The unit measure u
represents an unbiased measurement with only one outcome:
this outcome occurs if a preparation has succeeded, i.e. it is
determined by
u(ω) = 1

∀ω ∈ Ω.

(6)

<!-- page 3 -->
3
In the specific representation used in this paper we choose

4.

u := (0, · · · , 0, 1)T .
Consequently, for a state ω embedded in an n-dimensional
vector space V , the normalization of ω is directly apparent
from the last component ωn , i.e. normalized states have ωn =
1.
An effect is a map e : Ω → [0, 1] that gives a probability
when applied to a normalized state ω. A perfect measurement
consists of a set of effects {ei } which sum up to the unit measure, i.e.:

∑ ei = u.
i

Thus, measurement probabilities sum up to one for any
perfectly-prepared system.
Beyond the description of perfect preparations and measurements, the GPT framework also accounts for the opposite
extreme, namely preparations that always fail or measurement
outcomes that never occur no matter which state they are applied to. The corresponding states and effects are given by the
zero elements /0 of V and V ∗ with
/0(ω) = 0
e( /0) = 0

∀ω ∈ V
∀e ∈ V ∗ .

(7)
(8)

Imperfections in preparations yield unnormalized states resulting from the mixture of a normalized state ω and /0. Detector deficiencies and bias can be addressed by mixing every effect of a perfect measurement with /0 or another common effect. However, we will show in section VI 3 that consistency conditions on joint states forbid imperfect measurements. Consequently, the measurement has to be completed
by an additional effect, such that the effects sum up to the unit
measure, even though the occurrence of this additional measurement outcome cannot be registered by an experimenter
due to detector deficiencies.

3.

Equivalent Representations

Consider applying arbitrary bijective linear maps LT on all
effects and the corresponding inverse map L−1 on all states.
This leaves the results from any combination of effects and
states invariant, since:


T
LT· e L−1· ω = LT· e · L−1· ω = eT· L · L−1· ω = eT· ω.
(9)
Now, a particular probabilistic theory is associated with a particular state space Ω and set of effects E. But theories are
distinguished only by the different measurement statistics that
are possible (as is guaranteed by using the equivalence principle). Hence if Ω and E are transformed according to (9), then
the resulting Ω0 and E 0 define the same theory, since this transformed state space and effect set yield the same measurement
statistics.

Examples

Quantum theory. Consider the usual quantum formalism,
for which a state is given by a density matrix ρ on a Hilbert
space H . By decomposing density matrices in an operator
basis, we obtain the real vector space V defined above for
quantum theory. For example, there is a well-known representation of the normalized states of a qubit as a linear combination of the Pauli-operators σi :
ρ=

1
(1 + a σx + b σy + c σz )
2

a2 + b2 + c2 ≥ 1

(10)

Forming a real vector from the coefficient a, b, c gives the
representation of the qubit state space in V = R3 : this is the
Bloch ball.
Adding a fourth component that indicates normalization
gives a representation similar to (1). However, for quantum
systems of higher dimension the characterization of the geometrical shape of the state spaces in this representation is still
an open problem [11].
In the usual density matrix representation an effect is a
POVM element E, which is applied via the trace rule, so that
the probability of an effect E given the state ρ is given by
Tr[E ◦ ρ]. The unit measure u is given by the identity operator
1 on H , so that a density matrix ρ is normalized when:
Tr[1 ◦ ρ] = 1.
Note that for quantum systems the set of states and the set of
effects can be identified: this is the set of positive operators on
H . For example, for a qubit the Bloch ball represents both
(normalised) states and effects. This is an example of ‘selfduality’ in a theory; we shall discuss this further in section
V.
Classical probability theory. The state space of a classical system in Rd is a simplex. This is the convex hull of d + 1
pure states (which can be characterized via a condition on linear independence). For example, for d = 1, the classical state
space is a geometrically line, which represents a bit. The extreme points of the line ω0 and ω1 are the pure states: these
represent the values 0 or 1 of the bit respectively. The convex mixtures pω0 + (1 − p)ω1 represent states of classical uncertainty about the value of the bit. Only one measurement
outcome is needed to identify the state, e.g. the probability of
obtaining the 0 value for the bit. For d = 2, the simplex is a
triangle in R2 , which represents a trit; and so on. As for a bit,
for any d the pure states ωi represent mutually exclusive properties of the system. For example, if one knows with certainty
which number is on top of a die, then one automatically knows
that none of the other numbers is on top. This means that the
pure effects then correspond to measurement outcomes that
perfectly distinguish ωi i.e. ei (ω j ) = δi j .
Boxworld. This is a popular toy theory in the GPT framework that is neither quantum nor classical, which was first
introduced systematically in [1]. Boxworld consists of a class
of single systems characterized by the dimension d ≥ 2 of the
state space. For d = 2 the normalized state space Ω is the

<!-- page 4 -->
4

⇔

V+
u

Ω

V+∗
E

vs

V+∗
E

FIG. 1. The construction of the effect set E in the traditional GPT framework with no-restriction hypothesis is shown in the middle. Without
the no-restriction hypothesis the definition of the effect set gets a independent part of the theory specification (right picture).

convex hull of the following pure states:
ω1 = (1, 0, 1)T
T

ω3 = (−1, 0, 1)

ω2 = (0, 1, 1)T

(11)
T

ω4 = (0, −1, 1) ,

(12)

and so geometrically Ω is a square. The set of effects is given
by the convex hull of of /0 = (0, 0, 0)T , u = (0, 0, 1)T and the
following extremal effects:
e1 =

1
(1, 1, 1)T
2

1
e3 = (−1, −1, 1)T
2

1
(−1, 1, 1)T
2
1
e4 = (1, −1, 1)T
2

e2 =

(13)
(14)

It is straightforward to show that the measurement statistics
of the two orthogonal binary measurements M1 = {e1 , e3 }
and M2 = {e2 , e4 } give enough information to identify any
state. Indeed, due to the normalization constraint the measurement statistics of the binary measurements on normalized
states is determined by the probabilities p1 , p2 for the first
outcomes e1 , e2 . The different states give rise to the full range
(p1 , p2 ) ∈ [0, 1]2 of possible probability distributions, with the
probabilities p1 and p2 being independent. Hence the measurement outcomes e1 and e2 are enough to identify the state
of the system, which verifies that the dimension is d = 2. Note
that unlike orthogonal measurements in quantum theory (such
as σx and σy ), there is no uncertainty principle for M1 and M2
for this system [12]. For example, although e1 and e4 belong
to orthogonal measurements, we have e1 (ω1 ) = e4 (ω1 ) = 1.
Higher dimensional single systems with d > 2 in boxworld
have d different binary orthogonal measurements and state
spaces given by hypercubes. For the joint states that we
shall discuss in section VI, boxworld allows maximal nonlocal
correlations (using the CHSH inequality introduced below).
These correlations define the Popescu-Rohrlich box [13], and
they are not realizable by quantum theory.

framework of GPTs, the set of effects E is not restricted any
further. That is, the set of effects is exactly the set of all
probability-valued linear functionals on the given states. We
will call this relationship between states and effects the norestriction hypothesis, in accordance with [6]. It is satisfied
for classical probability theory and quantum theory.
Theorem 1. The set of effects under the no-restriction hypothesis is given by
E := V+∗ ∩ (u −V+∗ )
with the so-called dual cone
V+∗ := {e ∈ V ∗ | e(ω) ≥ 0

∀ω ∈ Ω} .

THE NO-RESTRICTION HYPOTHESIS

We now consider in detail the no-restriction hypothesis, and
the consequences of relaxing it.
A.

Defining the set of effects

Effects are restricted to give values in the range of [0, 1]
when applied to normalized states. But in the traditional

(16)

Proof. The definition of effects as probability-valued linear
functionals can be decomposed into two conditions.
The first condition is that effects have to give non-negative
results on every element of the state space. For arbitrary elements e ∈ V ∗ satisfying this condition, the condition is also
satisfied by the positive ray {λ e|λ ≥ 0}. Hence, the set obeying the non-negativity condition is a cone, namely the dual
cone V+∗ , defined by (16).
The second condition on effects requires them to give results not larger than one, when applied to arbitrary normalized
states. In other words the results have to be one or one minus
a positive value, i.e. e ∈ u −V+∗ .
In the standard framework both boundary conditions are
saturated. That is, for a given state space, any linear functional that gives probability-valued results for all normalized
states is included in the theory. Thus, the set of effects E is
V+∗ ∩ (u −V+∗ ).
The dual of the dual cone is the primal cone V+ , which is
generated by unnormalized states, i.e.
V+ := {λ ω | ω ∈ Ω, λ ≥ 0} = (V+∗ )∗ .

III.

(15)

(17)

Consequently, if the no-restriction hypothesis holds, then a
theory is completely determined by the state space, since the
effect set can be derived from the state space.
The purpose of this paper is to develop the framework
of GPTs without the no-restriction hypothesis. There are
two main reasons for doing so. Firstly, the necessity of the
no-restriction hypothesis is questionable from an operational
perspective. Indeed, considering the physical meaning of
states and effects there is no reason to believe that the possible preparation procedures determine possible measurements.

<!-- page 5 -->
5
e2

Secondly, this will generalize the GPT framework to cover
new scenarios that have not been accessible within the old
framework.
B.

eλ2

Let us note the constraints that still apply when the norestriction hypothesis is removed. Clearly, effects still need
to give probabilities when applied to any state. That is, when
allowing violations of the no-restriction hypothesis, the set of
probability-valued linear functionals on states in (15) remains
an upper bound for possible effects. However, in general not
all elements in this set need to represent a valid measurement
outcome. Consequently, the set of effects E may actually be
given by a subset of (15). This is the crucial new ingredient in
the GPT framework that we shall use in subsequent sections.
Furthermore, we have identified the following four consistency conditions that also have to be met:
i) The unit measure u needs to be included in the restricted
set as it is crucial for the definition of measurements.
ii) For every effect e included in E, the complement effect
ē = u − e needs to be included as well. We will show in
section VI 3 that including an effect, but not the complement can yield inconsistencies for joint states.
iii) Coarse graining also provides effects that can be derived from existing ones. If one does not distinguish
between some measurement outcomes that are part of
the same measurement, the common probabilities are
given by the sum of the individual probabilities. Due to
linearity the corresponding effect describing the coarse
graining is given by the sum of the individual effects.
iv) Transformations map valid states to valid states. However, for any transformation T on states, there is also
an adjoint transformation T † on effects defined by
e[T (ω)] = [T † (e)](ω) for all states and effects. Thus,
the effect set has to respect given transformations.
Apart from these consistency restrictions, the definition of
the effect set E is now an independent part of the specification
of the theory. In other words, the effect set E does not depend
on the state space now, and the dual cone V+∗ is irrelevant for
single systems. However, we will see in section VII B that we
still need it to classify consistent joint states.
Let us now consider how removing the no-restriction hypothesis will be useful. As shown above, the no-restriction
hypothesis connects a set of states and effects via the respective dual-cone. Taking a closer look at the dual cone construction in (16), it can easily be seen that each extremal point of
the primal cone describes a facet of the dual cone and the other
way round. Therefore, arbitrary small changes in the primal
cone, can have an enormous impact on the form of the dual
cone. Consequently, the no-restriction hypothesis makes it
extremely difficult to alter a theory in a controlled way. However, it has always been a central motivation for the framework of generalized probabilistic theories to find alternatives
to quantum theory.

eλ1
{u, /0}

ω3

Relaxing the no-restriction hypothesis

eλ3
e3

e1

ω2

ω1
eλ4

ω4

e4

FIG. 2. Inclusion of noise into boxworld: State space and effects
are both embedded into R3 and shown from above for illustration.
The state space (blue) is given by a square. The effect set is the
octahedron spanned by the extremal effects ei , u and /0. The noisy
theory has a restricted effect set with extremal effects eλi .

We shall now show in sections IV and V that new models with interesting features can indeed be constructed when
accepting violations of the no-restriction hypothesis. Furthermore, for joint systems, we will see in sections VI and VII
how consistency conditions are affected.
IV.

THEORIES WITH INTRINSIC NOISE

The no-restriction hypothesis guarantees that for any pure
state ω, there is an effect e, with e 6= u, such that e(ω) = 1.
In contrast, removing the no-restriction hypothesis allows for
the modeling of systems with intrinsic noise, i.e. systems for
which the unit measure is the only certain outcome for any
state. For example, an isotropic unbiased implementation of
noise can be achieved by restricting the effects to a set where
the original extremal effects are replaced by mixtures with u/2
(except for /0 and u itself). In order to combine noise and bias
one can mix the extremal with another effect instead of u/2.
The inclusion of intrinsic noise by a modification of boxworld is illustrated in Fig. 2. The state space of a single system is given by a square. In the traditional model the effect
set is determined by the no-restriction hypothesis. A noisy
version of boxworld is given by mixing the extremal effects ei
with u/2:
ei 7→ eλi = λ ei + (1 − λ )

u
2

(18)

The strength of noise is given by (1 − λ ), i.e. the maximal
probability from extremal effects is λ .
This model is particularly interesting with respect to its potential non-local correlations in joint systems. This will be
examined in more detail after introducing joint states in section VI.
V.

SELF-DUALIZATION PROCEDURE

A particular class of systems that has gained a lot of interest
recently are so-called (strongly) self-dual systems [2, 9, 14].
These are systems with a particular geometrical structure,

<!-- page 6 -->
6

ω2

e2

e2
ω1

ω2

ω2 ,e02

ω1

e3

e1

e3

e1

e3

ω3

ω6

ω3

ω6

ω3 ,e03

e4

e6

e4

e6

e4

ω4

e5

ω5

e5

ω1 ,e01
e1
ω6 ,e06
e6

ω4 ,e04

ω5

ω4

e2

e5

ω5 ,e05

FIG. 3. Self-dualization of a hexagon system: The pictures show the statespace (blue) and the intersection of the effect cone (red) that lies in
the same plane. In the first step the state cone will be embedded into the effect cone by an equivalence transformation (9). In the second step
the effects not included in the state cone are abandoned.

shared by both classical probability theory and quantum theory. For strongly self-dual systems states and effects can be
identified with each other and thus be represented by the same
mathematical objects. E.g. in quantum theory both states and
effects are represented by positive hermitian operators.
Formally, strong self-duality is given by the following definition.
Definition 2. A system is strongly self-dual iff there exists
an isomorphism Φ : V+∗ 7→ V+ giving rise to a corresponding
symmetric bilinear form T with T (e, f ) = e[Φ( f )] = T ( f , e)
and T (e, e) ≥ 0 for all e, f ∈ V ∗ .

effect cone V+∗ . The set of effects is then constructed from V+∗
by E = V+∗ ∩ u − V+∗ .
The connection between self-dualized systems and actual
strongly self-dual systems is not only limited to a mere formal
resemblance. In fact, the following example shows that selfdualized systems have features that strongly self-dual systems
have when the no-restriction hypothesis is assumed.

A.

Example: self-dualized polygons

That is, T provides a semi inner product on effects. In a
similar way for strongly self-dual systems the inverse map
Φ−1 leads to a semi inner product on states.
Strong self-duality greatly restricts the class of possible systems. As we describe below, the property of ‘bit-symmetry’
implies that a system is strongly self-dual [14], and there is evidence that non-local correlations of self-dual systems are limited [9]. In this section we provide a general construction rule
to modify any system, such that it resembles the behaviour of
strongly self-dual systems.

Let us illustrate the self-dualization procedure on a set of
systems introduced in a previous paper [9]. It is defined by
two-dimensional state spaces with the shape of regular polygons. While the cases with an odd number of vertices n are
strongly self-dual, the even cases are not.
For fixed n, let Ω be the convex hull of n pure states {ωi },
i = 1, ..., n, with


rn cos( 2πi
n )
 ∈ R3 ,
ωi =  rn sin( 2πi
(19)
n )
1

Theorem 3. Any theory in the GPT framework can be modified to resemble strongly self-dual systems respecting Definition 2 with the dual cone V+∗ replaced by a truncated cone
V+∗ .

p
where rn = sec(π/n).
The unit effect is

Proof. Using our representation, we assume an embedding of
effects and states in a common vector space with a scalar product mediating the application of effects on states, as in Eq. 1.
We start from an arbitrary theory for which the no-restriction
hypothesis holds. The freedom of linearly transformations LT
from (9) allows us to strictly enlarge the effect cone V+∗ , while
the corresponding inverse L−1 constricts the cone of unnormalized states V+ to be strictly smaller. Hence, one can always represent the same physical theory, with V+ embedded
in V+∗ . We can then define a truncated the effect cone from
V+∗ ⊆ V+∗ , such that V+∗ coincides with the state cone V+ .
Hence we can describe unnormalized effects and states with
the same set of vectors. Consequently, the restriction of effects yields the vector space’s scalar product to act as an inner
product between states. This satisfies the definition of strong
self-duality with the dual cone V+∗ exchanged for the truncated

u = (0, 0, 1)T .

(20)

The set E(Ω) of all possible measurement outcomes will
be determined by the no-restriction hypothesis. In the case of
even n, E(Ω) is the convex hull of the zero effect, the unit
effect, and e1 , . . . , en , with


rn cos( (2i−1)π
)
n
1
ei =  rn sin( (2i−1)π )  .
n
2
1

(21)

The odd case yields a different expression for the rayextremal effects


r cos( 2πi
n )
1 n
.
ei =
(22)
rn sin( 2πi
n )
1 + rn 2
1

<!-- page 7 -->
7
As shown in III the complement effects ēi = u − ei of ray
extremal effects ei are also extremal in the effect set E(Ω).
Whereas for even n these happen to coincide with ēi =
e(i+n/2)mod n , for odd n the complement effects form additional
extremal points of E(Ω). In summary, E(Ω) is the convex hull
of the zero effect, the unit effect u, the ray-extremal effects
e1 . . . , en , and for odd n additionally e¯1 , . . . , e¯n .
In the limit n → ∞ both cases converge to a disc that can be
regarded as the 2D subspace of a qubit. The extremal rays of
the dual cone of polygon systems with odd number of vertices,
coincide with the scaled extremal states, i.e. these systems
are strongly self-dual. However, for polygon system with an
even number of vertices the primal and dual cones are only
isomorphic and can be matched by a rotation of πn . That is,
the even polygons are not strongly self-dual in the original
models. We will now self-dualize these even-polygon systems
using the procedure described in Theorem 3.
As discussed in section II 3 there is always the freedom to
apply arbitrary bijective linear maps to all effects and the corresponding inverse map on all states. We use this to shrink
the state space by rn 7→ 1 to fit in a circumscribed circle of
radius one. Applying the inverse map to effects results in a effect cone with rn 7→ rn2 . This new effect cone is strictly bigger
than the cone of unnormalized states. By truncating this effect
cone, such that the new extremal effect e0i are given by


cos 2nπi 

1
1
ωi
e0i =
ei + e(i+1)mod n =  sin 2nπi  = ,
2
2
2
1

B.

Spekkens’s toy theory

In [15] Spekkens introduced a toy theory which replicates
many features of quantum theory. For example, it exhibits a
no-cloning theorem and a teleportation protocol. The theory is
not explicitly probabilistic, since outcomes are not explicitly
assigned probabilities. Instead, a graphical calculus is used.
Given a state ω, the outcome i is only specified to be ‘possible’ or ‘impossible’. The Spekkens theory in its original form
also has no notion of arbitrary convex mixing, i.e. it does not
have the property for any pair of states ω1 and ω2 , there exists
a state pω1 + (1 − p)ω2 for all probabilities p ∈ [0, 1].
The ability to form convex mixtures is crucial to GPTs, and
in particular to its operational motivation. Fortunately, there is
a natural extension of Spekkens theory which is probabilistic
and which does allow convex mixing (the probabilistic version of this theory was also introduced previously by Hardy in
[10]). The state space Ω of a single system is then the octahedron. In the representation that we have used, the six extremal
states (i.e. the pure states) are just given by the co-ordinates
of the octahedron in R3 , with an extra component for normalization. For example, the four extremal states that form the
ω6
ω4

ω1

ω3

ω2

(23)

the primal cone coincide with the new effect cone generated
by the restricted effect set.
Let us demonstrate the self-dualization procedure explicitly, by using the polygon with n = 4 (this is the boxworld
model). In the first step the pure states and effects are transformed to the equivalent representation given in (11) and (13).
In this representation the effect cone is completely embedded
in the cone of unnormed states. The actual self-dualization is
then done by exchanging ei for e0i = ωi /2, shrugging off the
effects not included in the primal cone.
For all self-dualized polygon models, another interesting
feature emerges for the restricted case. Namely, there exists a
specific pure state ω̄ for each pure state ω, such that they can
be perfectly distinguished by an effect e with e(ω) = 1 and
e(ω̄) = 0. Furthermore, each pair of perfectly distinguishable
states can be mapped reversibly to any other pair of perfectly
distinguishable states. This feature is known as bit symmetry,
and was shown to only hold for strongly self-dual systems in
the traditional framework [14].
This demonstrates that the self-dualization procedure can
actually reproduce properties thought to be specific for actual
strongly self-dual systems. Note that the mathematical description of actual strongly self-dual systems can be complex.
Using self-dualized systems might be an alternative that helps
to identify new features of strongly self-dual systems, even
if one is not interested in the relaxation of the no-restriction
hypothesis.

ω5

FIG. 4. The state space of the Spekkens model, with the six pure
states ωi labelled.

square base of each tetrahedron are identical to the states for
boxworld (see Fig. 4). That is, for i = 1, . . . , 4 the states are:


cos( 2πi
4 )
 sin( 2πi ) 
4
4 
(24)
ωi = 
 0 ∈R ,
1
and for i = 5, 6 the states are

0
0
ωi =   ∈ R4 ,
±1
1


(25)

Now, the dual space of an octahedron is the cube. However, in the Spekkens theory, the space of effects is identical
to the state space: it is also the octahedron depicted in Fig. 4.
Since the octahedron can be obtained by restricting the cube
(in the same way that is depicted for the hexagon in Fig. 3),we
see that the Spekkens theory provides an example of a selfdualized theory. In particular, the convex probabilistic version of it is obtained using the self-dualization procedure defined in Theorem 3, and as described above for self-dualized
polygons. Indeed, as with boxworld, the restricted effects are

<!-- page 8 -->
8
given by:
e0i =

ωi
2

Hence we see that, at least for single systems, the Spekkens
theory can be seen as an extension of self-dualized boxworld:
the state and effect space of the Spekkens theory contain the
state and effect space respectively of self-dualized boxworld.
We develop the analysis of joint systems for the Spekkens theory in Section VII C 3.
We note that the single-system state space is identical to
that of stabilizer quantum mechanics, for which the only allowed states are the eigenstates of the Pauli operators, and the
allowed transformations are the Clifford operations. As discussed in [15] and further in [16], the Spekkens theory and
stabilizer quantum mechanics differ in the group of reversible
transformations that each theory specifies.
VI.

JOINT SYSTEMS IN THE TRADITIONAL GPT
FRAMEWORK

In the preceding sections we have not distinguished between single systems and joint systems. That is, our discussion so far (e.g. of self-dualization) has not involved any potential subsystem structure, whereby a system C can be divided into subsystems A and B, with each subsystem having well-defined states and effects. In the next section we
shall consider how relaxing the no-restriction hypothesis affects composite systems. Before doing so, in this section we
recall the treatment of joint systems in the traditional framework, i.e. when the no-restriction hypothesis is assumed to
hold.
We will restrict the discussion of joint systems to the bipartite case with two subsystems, as the generalization of multipartite systems is straightforward. Bipartite joint states are
given by elements of the product space
V AB = V A ⊗V B

(26)

and joint effects are elements of V AB∗ = V A∗ ⊗ V B∗ respectively [17].
We will represent joint states and joint effects by n × m matrices, with n = dimV A = dimV A∗ , m = dimV B = dimV B∗ . As
for single systems, the application of effects on states results
in the sum of the entry-wise products. This can be elegantly
written as the Hilbert-Schmidt inner product


eAB ω AB = Tr eT· ω = ∑ εi j wi j ,
(27)
i, j

where we write eT· ω for the matrix product between the transpose of matrix e representing the joint effect eAB and the matrix ω representing the joint state ω AB .
To define a composite system for a particular GPT (with
specified state and effect spaces for individual systems), we
must define the set of joint states ΩAB = {ω AB }, and the set
of joint effects E AB = {eAB }, such that these are consistent
with the individual systems. If the no-restriction hypothesis

holds, then, as before, once the set of joint states ΩAB is defined, the set of effects E AB is determined. In this situation we
need only consider the definition of ΩAB in order to specify
the behaviour of composite systems. There is much freedom
in defining ΩAB , but there are two boundary cases which we
now discuss.

1.

Lower bound on joint systems

Consider independently prepared systems A and B with
states ω A ∈ ΩA , ω B ∈ ΩB . Treating the systems jointly as a
composite AB, the overall preparation is represented by the
product state ω AB = ω A ⊗ ω B , with ω AB ∈ V AB . However,
just as classical mixtures are allowed for single systems, for
joint systems mixtures between product states give valid joint
states again. This corresponds to the ability of experimenters
to classically correlate the preparations and measurements of
the individual systems, e.g. two experimenters can agree on
specific settings.
The set of unnormalized states only containing product
states and their mixtures is known as the minimal tensor product A+ ⊗min B+ .
Definition 4. The minimal tensor product is given by
(
A+ ⊗min B+ :=

ω AB ∈ V AB ω AB = ∑ λi ωiA ⊗ ωiB ,

(28)

i

ωiA ∈ A+ , ωiB ∈ B+ , λi ≥ 0 .
It is the smallest possible set of unnormalized joint states ω AB
that is compatible with given state cones A+ ≡ V+A , B+ ≡ V+B
of subsystems A,B.
Similar reasoning applies to measurements, and so the set
of joint effects is lower-bounded by the convex hull of product effects. Importantly, this includes the joint unit measure
uAB = uA ⊗ uB , which is uniquely defined due to the equivalence principle. Hence, normalization of joint states ω AB is
represented by the condition uAB (ω AB ) = 1. This allows us
to define the bipartite state space ΩAB
min corresponding to the
minimal tensor product:

 AB
ΩAB
∈ A+ ⊗min B+ uAB ω AB = 1
(29)
min := ω
(
=

ω AB ∈ V AB ω AB = ∑ pi ωiA ⊗ ωiB ,

(30)

i

)
ωiA ∈ ΩA , ωiB ∈ ΩB , pi ≥ 0,

∑ pi = 1 .
i

For classical subsystems (i.e. a simplex), the joint states and
effects defined by the minimal tensor product is sufficient to
describe joint classical systems. Theories with non-classical
subsystems, however, allow joint states that cannot be interpreted as a mixture of product states, i.e. entangled states. The
other extreme to the minimal tensor product allows all possible entangled states, as we now show.

<!-- page 9 -->
9
2.

3.

Upper bound on joint systems

Everything introduced so far is valid independent of the norestriction hypothesis. This changes now, as we ask for the
maximal sets of joint states and effects consistent with the
structure of the single systems.
First, let us focus on the traditional GPT framework with
single systems obeying the no-restriction hypothesis. Given
a specific state space the no-restriction hypothesis determines
the effects for the single systems. As argued above, the joint
system should at least incorporate product effects and their
mixtures. Applying such joint effects to any potential joint
state ω AB should give probabilities. In particular this implies
that the joint states form a subset of the following set of linear
elements.

For our generalization of the maximal tensor product, we
shall use the following conception of joint states. Joint states
can linearly map effects from one part of the joint system to
unnormalized states of the other subsystem. This can be conveniently shown in the representation of joint states as matrices, since
h
i


T
T
eA ⊗ eB ω AB = Tr eA ⊗ eB · ω AB = eA · ω AB· eB .
(33)
Using associativity of the matrix product, we can interpret
T
parts of the expression eA · ω AB · eB as ‘effective’ states of
the subsystems A and B. We define these conditional states as
ωeAB := ω AB· eB
T
ωeBA := eA · ω AB

Definition 5. The maximal tensor product is defined as



A+ ⊗max B+ := ω AB ∈ V AB eA ⊗ eB ω AB > 0,
∀eA ∈ E A , eB ∈ E B

∗
= A∗+ ⊗min B∗+ .

Joint states as linear maps

(31)
(32)

It is the largest possible set of unnormalized joint states ω AB
that is compatible with given state cones A+ , B+ of subsystems A, B that respect the no-restriction hypothesis.
Note that the second equality arises just by definition of the
dual cone (16). Hence, we see that the maximal tensor product for states is given by the maximal set of joint states consistent with the minimal tensor product for effects. Similarly the
maximal tensor product for effects is defined as the maximal
set of joint effects consistent with the minimal tensor product
for states. Elements in the maximal tensor product, but not in
the minimal tensor product are called entangled.
To summarise our constructions in this section: the definition of a GPT includes the tensor product, which specifies the
composition of subsystems. The minimal and maximal tensor
product are only the extreme cases where the joint state space
ΩAB is chosen as smallest or the biggest set compatible with
the state spaces ΩA , ΩB of single systems. In general, a GPT
can be defined to include any set of joint states between those
extremes.
For example, the joint state space in quantum theory lies
strictly between the minimal and maximal tensor product. E.g.
the partial transposed of density matrices representing entangled states of two qubits or a qubit and a qutrit are known
to give invalid states for the quantum tensor product, because
they are not positive on all entangled effects [18]. However,
these states give positive results for separable measurements,
i.e. they are in the maximal tensor product. Note that these
states should not be misunderstood as part of quantum theory, but form a separate toy theory that omits any entangled
measurements. Nevertheless, the additional states in the maximal tensor product of local quantum systems are useful for
the study of entanglement in standard quantum theory, as they
correspond exactly to the set of entanglement witnesses.

(34)
(35)

These are unnormalized states for system A and B respectively. Physically, these can be regarded as ‘postmeasurement‘ states on one part of the joint system, conditioned on a particular measurement outcome on the other part.
This process of remotely preparing a state by a measurement
on the other part of a joint state is usually referred to as ‘steering’ [19]. It demonstrates that, when measuring only part of
a joint system, the joint state acts as a linear map from effects
of one side of the system to unnormalized states of the other
part. It can be shown that the maximal tensor product coincides exactly with all possible linear maps of this form, i.e. it
corresponds to all potential joint states that have valid conditional states for non-restricted systems [2]. This property will
be central for the generalization of the maximal tensor product
in the next section.
Conditional states at A are unnormalized: they are weighted
with the probability of obtaining the corresponding measurement outcome at B. That is, the probability accounts for the
potential ignorance of the outcome for observers at B. Consequently, if one knows the measurement outcome in B the
effective description of the state in A is given by the normalized conditional state:
ω̃eAB =

ωeAB
ωeAB
=
.
p(eB |ω AB ) u(ωeAB )

The marginal state or reduced state ωuAB gives the description
of the effective state on part A of a joint state ω AB . This is a
conditional state with eB = uB , and is already normalized i.e.
ω̃uAB = ωuAB .
Note that this formalism still applies if the parts of the system are space-like separated, i.e. if there is no causal relationship between the measurement on the system B and the system A. However, the no-signaling principle states that steering
cannot be used to transmit information, i.e. it does not allow
for communication faster than the speed of light. The relationship between steering and the no-signaling principle is shown
by the following theorem. First, we call a set of effects {eAi }i ,

<!-- page 10 -->
10
for any system A, a perfect measurement if

∑ eAi = uA .
i

An imperfect measurement is a set of effects {eAi }i that is not
a perfect measurement.
Theorem 6. Assuming the no-signalling principle, steering
implies that all measurements are perfect measurements.
Proof. Consider two observers in part A and B respectively
sharing a joint state ω AB . The observer in B performs a measurement on his part and gets some measurement outcome
eBj . Knowing the outcome the description of the system in
A from his point of view is given by the normalized conditional state ω̃eAB . The other observer ‘knows’ only the coarse
j

graining of the different measurement outcomes. I.e. from his
point of view the state in A is an ensemble of possible ‘postmeasurement states’ {ω̃eAB }.
i
Remember that the equivalence principle gives a one-to-one
correspondence of states and specific measurement statistics.
Consequently, no-signaling requires the state in A after the
measurement on B to be identical to the original marginal state
ωuAB in order to prevent information transfer, i.e.

∑ pi ω̃eABi = ∑ ωeABi = ω∑Ai eBi = ωuAB ,
i

(36)

i

where we used the definition of the normalized conditional
state and the linearity of effects.
Since the coarse grained conditional state needs to be equal
to the marginal state for any joint state

∑ eBi = uB .

(37)

i

We will use the interpretation of the maximal tensor product
as the set of all positive linear maps to generalize it for systems
violating the no-restriction hypothesis.
VII.

THE GENERALIZED MAXIMAL TENSOR PRODUCT

As we have discussed, by removing the no-restriction hypothesis, the definition of a physical system now needs a specification of both the state space and the effect set. That is,
the set of allowed states and the set of allowed effects can be
chosen independently—except for the constraints discussed in
section III. Let us now consider the specification of joint systems when the no-restriction hypothesis is removed.
The definition of the minimal tensor product A+ ⊗min B+
makes no reference to the effect sets E A and E B . I.e. it is constructed by products and their convex combinations. Therefore the minimal tensor product can be defined without assuming the no-restriction hypothesis, and hence carries over
to our more general situation. Indeed, everything that we have
introduced for joint systems so far is valid independently of
the no-restriction hypothesis — with one exception.

The exception is the maximal tensor product. As before,
we expect the maximal tensor product to comprise all joint
states that are compatible with the given subsystems. Compatibility can be broken down to two requirements: i) nonnegative results on local effects ii) valid conditional states. For
non-restricted systems both requirements are equivalent, as
the no-restriction hypothesis implies consistent mappings (i.e.
valid conditional states) if and only if local effects give nonnegative results on joint states. Now, for the general case (i.e.
without the no-restriction hypothesis), valid conditional states
still guarantees non-negativity on local effects. However, the
implication in the other direction is no longer secured.
For example, consider attempting to use the same construction as before, i.e. we start with the minimal tensor product
of effects and determine all elements of the joint system that
give positive results. The resulting elements do not depend
on the state spaces of the single systems at all, since the effects are decoupled from the state space due to the abandoned
no-restriction hypothesis. Hence the resulting joint states are
not forced to be consistent with the subsystems: we give an
example of such a failure of consistency below.

A.

Failure of the traditional maximal tensor product

Before generalizing the maximal tensor product we will
show that the traditional construction rules fail for restricted
systems.
The traditional maximal tensor product A+ ⊗max B+ is given
by the dual of the set of separable effects. For restricted systems this yields two different variants. Equation (31) seems to
suggest a construction based on the restricted effects, whereas
(32) utilizes the subsystems’ dual cones, which are generated
by the potential set of unrestricted effects. We show that neither choice gives the set of all joint states consistent with restricted subsystems.
The first variant is constructed as follows. Consider the
restricted effects E A of a subsystem A with an effect cone
A := {λ eA | eA ∈ E A , λ ≥ 0}. Following equation (17) we
E+
can construct a virtual, non-restricted system A with the state
cone given by

A
⊇ A+ (38)
A+ := ω A ∈ V A eA (ω A ) ≥ 0 ∀eA ∈ E+
A
.
⇒ A+∗ = E+

(39)

I.e. the virtual system extends the unnormalized states, such
that the no-restriction hypothesis is satisfied. Thus, the potential joint states from (31), correspond actually to the traditional maximal tensor product A+ ⊗max B+ of the virtual
systems A , B.
Recall that the interpretation of joint states as positive linear
maps, A+ ⊗max B+ is exactly the set of all maps from the
A (E B ) to the unnormalized virtual
restricted effect cones E+
+
states B+ (A+ ) on the other side of the bipartite system. In
other words, this construction includes joint states that allow
the preparation of states in the subsystems not limited to the
initial definition of the state spaces ΩA , ΩB , but to those of the
virtual systems instead.

<!-- page 11 -->
11
For example in a bipartite system of self-dualized boxworld
with extremal states according to (11) and restricted extremal
effects e0i = ωi /2 the potential joint state


1 −1 0
B
ω AB = 1 1 0 ∈ ΩA
(40)
max
0 0 1
gives positive values on any pair of restricted effects. However, some conditional states are not valid for the actual system A, e.g. ω̃eA0 = (−1, 1, 1)T ∈
/ ΩA .
1
The second variant of the traditional maximal tensor product is based on the dual cones A+ , B+ according to (32). The
resulting joint states are also consistent with the restricted effects, since the latter is included in the set of all of effects.
However, this construction omits joint states which are consistent only with the restricted effects. For example, for selfdualized boxworld the identity matrix would not be included,
although it has valid conditional states and gives positive results on any pair of effects.
B.

Construction of the generalized maximal tensor product

As shown above, the traditional construction rules for the
maximal tensor product lead to inconsistencies when applied
to theories not obeying the no-restriction hypothesis. In this
section we shall construct a generalized maximal tensor product A+ ⊗max B+ : this will give the maximal set of joint states
that is consistent with general subsystems, irrespective of
whether the no-restriction hypothesis is assumed to hold. In
other words, the generalized maximal tensor product contains
all bipartite states whose conditional (i.e. also marginal) states
are elements of the original state spaces.
Definition 7. The generalized maximal tensor product of systems A, B with primal cones A+ , B+ , dual cones A∗+ , B∗+ and
A , E B is given by
effect cones E+
+
∗

A
B ∗
A+ ⊗max B+ := E+
⊗min B∗+ ∩ A∗+ ⊗min E+

A
B ∗
= E+
⊗min B∗+ ∪ A∗+ ⊗min E+
.

(41)

For the saturated case, dual cones and effect cones are identical, and we recover the usual maximal tensor product as follows.
A = A∗ and E B = B∗ . Then
Proposition 8. Suppose that E+
+
+
+
A+ ⊗max B+ = A+ ⊗max B+ .

Proof. Under the assumptions, Eq. 41 becomes
∗
A+ ⊗max B+ = A∗+ ⊗min B∗+
= A+ ⊗max B+
using the definition of the maximal tensor product in (31).
Hence our construction is indeed a generalization of the existing definition of the maximal tensor product. It determines
all joint states consistent with general subsystems regardless

whether the no-restriction hypothesis holds or not. I.e. all
joint states with valid conditional states are included, as shown
in the following theorem.
Theorem 9. Let ω AB ∈ V AB . Then ω AB ∈ A+ ⊗max B+ iff ω AB
has well-defined conditional states:
ω̃eAB ∈ ΩA and ω̃eBA ∈ ΩB
for all eA ∈ E A and eB ∈ E B .
Proof. We shall show that
∗

(42)

∗

(43)

A
ωeAB ∈ A+ iff ω AB ∈ E+
⊗min B∗+

and that
B
ωeBA ∈ B+ iff ω AB ∈ A∗+ ⊗min E+

.

of sets of linear
Since A+ ⊗max B+ isdefined as the intersection

A⊗
∗ ∗ and A∗ ⊗
B ∗ , this will establish
B
E
maps E+
min +
+ min +
the thesis.
First we show the A → B direction, i.e. (42), which is the
A⊗
∗ ∗ is the set of all and only those
statement that E+
min B+
joint states ω AB such that each ω AB defines a map from effects
A on system A to valid unnormalized states ω B ∈ B .
eA ∈ E+
+
Recall that for non-restricted systems the traditional maximal tensor product is already known to give all positive linear
maps from the effect cone of one part of the system to the
state cone of the other
part for both directions. We now show

A⊗
∗ ∗ can be interpreted as the traditional maxthat E+
B
min +
imal tensor product A+ ⊗max B+ of two virtual systems A
and B that obey the no-restriction hypothesis. A is the virtual system that has already been introduced in (38). It has
A )∗ ⊂ A . Howan extended virtual state cone A+ , since (E+
+
ever, the actual effect cone is kept, as it coincides with the
A = A ∗ characterizing unnormalized effects of
dual cone E+
+
the non-restricted systems. The opposite situation applies to
B is extended to the dual cone B∗ ,
B. Here, the effect set E+
+
B
∗
so that E+ ⊂ B+ , where B∗+ representing the full set of potential unnormalized effects. However, the original state cone
B+ = B+ is kept. With these conventions
A
E+
⊗min B∗+

∗

= A+ ⊗max B+

follows directly from the definition of the traditional tensor
product in (32). Hence
for the A → B direction, this means

A⊗
∗ ∗ contains all positive linear maps from
that E+
min B+
the restricted effects in A to allowed states in B. That is,
A⊗
∗ ∗ is a sufficient and necessary condition
ω AB ∈ E+
min B+
for ωeBA ∈ B+ which proves (42). However, for the traditional
maximal tensor product the same joint states also coincide
with the positive maps in the other direction B → A , potentially including invalid mappings.
By swapping the roles of A and B in the above
argument,

B ∗ includes all
we similarly obtain that the set A∗+ ⊗min E+
linear maps that are consistent for the B → A direction, but
also those which lead to inconsistencies in A → B opposite
direction. Hence we obtain (43).

<!-- page 12 -->
12

eA
ω AB

A⊗
∗
E+
min B+

∗

ω AB

ω̃eBA

⇔

⇔

eB
A+ ⊗max B+

∈ ΩB

ω̃eAB

∈ ΩA


B ∗

A∗+ ⊗min E+

FIG. 5. Illustration of the construction of the generalized maximal tensor product

Theorem 9 shows that the generalized maximal tensor product includes only those joint states that are consistent in
 both
A⊗
∗ ∗ and
directions (i.e. the intersection of the sets E+
min B+

B ∗ ). Note that the if ω AB has well-defined condiA∗+ ⊗min E+
tional states, then in particular it is is locally positive:


eA ⊗ eB ω AB ≥ 0
which provides a useful necessary condition that joint states
must satisfy.
In the traditional GPT framework the choices of tensor
products for states and effects are not independent, as the norestriction hypothesis does not only apply to single systems,
but to the joint system as well. Having the minimal tensor
product for joint states (effects) does in fact constitute the
maximal tensor product for the set of joint effects (states).
This restriction seems inappropriate given that arbitrary single systems can actually be emulated by classical systems
with constrained measurements [20], whereas entanglement
is a strictly non-classical feature.
In our modified framework that is also valid for systems
violating the no-restriction hypothesis, this is no longer the
case. We have seen that we can generalize the maximal tensor product, but nevertheless we are not forced to use this for
states when we choose the minimum tensor product for effects
and the other way round.

C.

Examples of joint systems

To give some specific examples for the generalized maximal tensor product, we have calculated it for the toy theories
introduced in sections IV and V using the double description
method [21].

ΦAB = 12 (ω1 ⊗ ω2 − ω2 ⊗ ω2 + ω2 ⊗ ω3 + ω3 ⊗ ω1 ) and respectively the states transformed by local symmetries.
These entangled extremals can be interpreted as a maximally entangled state of two such systems, as they form a isomorphic map and have totally mixed reduced states. They
correspond to a rotation of π4 and the local symmetries of the
state spaces.
This theory has become very popular as it shows nonlocal
correlations beyond those possible in quantum theory, when
choosing between two possible binary measurements at each
side of the bipartite systems. Let us denote the two measurements {MxA } and {MyB } for each of the systems A and B respectively: we index the measurements at each system with
x, y ∈ {0, 1}. Each measurement has binary outcomes, labelled with a, b ∈ {0, 1} for systems A and B respectively. For
example, the x = 0 measurement on system A consists of a
pair of effects MxA = {e0 , e1 } satisfying e0 + e1 = u; similarly
for the x = 1 measurement on system A, and y ∈ {0, 1} measurements on system B. This leads to a bipartite conditional
probability distribution
P(a, b|x, y) := (ea ⊗ eb )[ω AB ]

(44)

We define the correlation
Cxy := P(a = b|x, y) − P(a 6= b|x, y).
To introduce the Clauser-Horne-Shimony-Holt (CHSH) inequality for demonstrating nonlocality, we introduce the parameter
S := |C00 +C01 +C10 −C11 |,
For classical systems it is upper bounded by the CHSH inequality [22]
SC ≤ 2,

1.

Noisy boxworld

In the original unrestricted version of boxworld joint systems are given by the maximal tensor product, including the
16 extremal product states and 8 pure entangled joint states

√
whereas for quantum theory it must satisfy SQ ≤ 2 2 [23].
However, local measurements on the maximally entangled
state Φ in boxworld can produce correlations which reach the
algebraic maximum Smax = 4, i.e. the theory allows the postquantum correlations known as PR boxes [13].

<!-- page 13 -->
13
For the noisy version of boxworld introduced in section IV
there is still a notion of a maximally entangled state in the
generalized maximal tensor product, namely
1 1
AB
Φλ = ωent,1
= diag( , , 1) · Φ1 ,
λ λ

(45)

i.e. the original maximally entangled state Φ1 combined with
a mapping of the effects on one side of the system to the original unrestricted set. Note that this map does not undo the
restriction of effects completely. The reversion only happens
to occur in this particular case when mapping to states of the
other part. On the other part, however, only restricted effects
can be applied to. Consequently, the correlations possible
with restricted systems will be different to those possible in
unrestricted systems.
Furthermore, constructing the generalized maximal tensor
product it turns out there are 4 different classes of new pure
joint states that are entangled but not maximally entangled.
These are representatives of each class
AB
ωent,2
= −α ω2 ⊗ ω2 + β ω2 ⊗ ω4 + β ω4 ⊗ ω2 − α ω4 ⊗ ω4
AB
ωent,3
= −α ω2 ⊗ ω2 + β ω2 ⊗ ω3 + β ω4 ⊗ ω2 − α ω4 ⊗ ω3
AB
ωent,4
= −α ω2 ⊗ ω2 + β ω2 ⊗ ω4 + β ω3 ⊗ ω2 − α ω3 ⊗ ω4
AB
ωent,5
= −α ω3 ⊗ ω2 + β ω4 ⊗ ω1 + β ω4 ⊗ ω2 − α ω4 ⊗ ω3

with α =

1+λ
1−λ
,β =
,
4λ
4λ

(46)

where the other elements of the class only differ by the local
symmetries.
In conclusion the generalized maximal tensor product is
spanned by 96 pure states. Namely, it consists of 16 local
AB , 8 of class
pure states, 8 pure entangled states of class ωent,1
AB
AB
AB
ωent,2 , 16 of class ωent,3 , 16 of class ωent,4 and 32 states of
AB .
class ωent,5
Considering local measurements on one instance of any of
the nonlocal extremal states the maximal CHSH violation Sλ
as a function of the parameter λ of the restricted model can be
shown to be 4 λ 2 . Note that this bound is only guaranteed for
the correlations that occur from direct measurements. However, it is known that wiring the measurements on multiple
joint states via classical post-processing, might give rise to a
distillation of correlations beyond for some values of λ [24].
2.

on the maximally entangled states at each side show correlations strictly weaker than quantum correlations for the odd
case, whereas the unrestricted even case shows correlations as
strong as those of quantum theory or stronger [9].
Replacing the original polygon systems with even n by their
self-dualized versions, the maximally entangled states lose the
additional rotation as the new effect cone and the state cone
coincide. Note, that the self-dualized single systems become
subtheories of the theory given in the limit n → ∞, i.e. the
quantum case, as both states and effects form strict subsets.
Thus, the correlations on the maximally entangled state form
a strict subset of those in quantum theory, in contrast to the unrestricted case which allows post-quantum correlations. Even
though the restricted polygons are not genuine strongly selfdual but only self-dualized, this is consistent with the conjecture in [9], that strong self-duality limits correlations.
For self-dualized boxworld the generalized maximal tensor
AB
product is given by the 16 local pure states, the 8 states ωent,1
representing the identity and symmetry mappings as well as
AB = 1/4(−ω ⊗ ω +
a class of 64 pure entangled states ωent,2
1
1
ω1 ⊗ ω3 + 2 ω2 ⊗ ω4 + ω3 ⊗ ω1 − ω3 ⊗ ω3 + 2 ω4 ⊗ ω2 ).
Unfortunately, using the double description method, we
were not able to characterize all extremals of the generalized
maximal tensor product for polygon systems with a higher
number of vertices.

Self-dualized polygons

Interestingly, not only boxworld but all bipartite polygon
systems allow a joint state with features known from the maximally entangled state of ordinary quantum theory. Namely,
the linear maps corresponding to these states are given by
isomorphisms of the dual and primal cones with maximally
mixed reduced states. The 2 n different maximally entangled states correspond to the elements of the dihedral group.
For even n, the maximally entangled states include an additional rotation of π/n mapping the dual cone of one part to
the primal cone of the other part. It was shown that nonlocal correlations based on two binary local measurements

3.

Spekkens’s toy theory

The Spekkens theory that we introduced earlier is a local
theory, meaning that (in the probabilistic version) it cannot violate any Bell inequalities. However, as discussed in [15], the
Spekkens theory has entangled states. This raises the question
of why the Spekkens theory does not exhibit bipartite nonlocality. In contrast, a classical theory, i.e. a simplex, is local
but it does not have entangled states. One could then ask,
given that the Spekkens theory has entangled states, but is local, what must be added to the definition of the theory to make
it nonlocal?
In our framework, the answer to this question can be
clearly understood in terms of the geometry of the state space.
First, recall that the state space ΩA of a single system in the
Spekkens theory is an octahedron, and the effect space E A is
identically the same, i.e. E A not the full dual space. Consider
a pair of single systems A and B in the Spekkens theory. Since
the effect space E A is not the full dual space A∗+ , we must use
the generalized tensor product ΩAB = A+ ⊗max B+ to define the
bipartite states. Then consider the following bipartite state:


0 0 0 0
0 − 1 − 1 0
2
2

ω AB = 
(47)
0 − 1 1 0
2
2
0 0 0 1
It is straightforward to verify that ω AB leads to well-defined
conditional states for system B for all effects eA ∈ E A , i.e.:
ω̃eBA ∈ ΩB

<!-- page 14 -->
14
and correspondingly for conditional states for system A when
using effects on system B. In particular, it is also easily
checked that (eA ⊗ eB )[ω AB ] ≥ 0 for any pair of effects eA and
eB . Hence by Theorem 9, this shows that ω AB is in the generalized tensor product A+ ⊗max B+ for the Spekkens theory.
Now, since the Spekkens theory is local, the CHSH inequality (VII C 1) is satisfied for any choice of measurements Mx
and My on the state ω AB , or any other bipartite state. However,
let us consider the unrestricted effect space A∗+ from which the
restricted space E A for the Spekkens theory was derived. The
unrestricted effect space of the octahedron is the cube. We can
represent the normalised extremal effects as the vertices of a
cube:

±1
1 ±1
ei =  
2 ±1
1


Now, suppose that we use the cube to be the effect space for
the octahedron, i.e. we use the full dual space. It is easily
shown that the state ω AB defined in Eq. 47 is again in the generalized maximal tensor product A+ ⊗max B+ . However, we
can now provide measurements which violate the CHSH inequality. In particular, consider two measurements for Alice
given by M0A = {e0 , u − e0 } and M1A = {e1 , u − e1 } where:

 
1
−1
1 −1
1 1 
e0 =   , e1 =  
2 −1
2 −1
1
1


and two measurements for Bob given by M0B = {e0 , u − e0 }
and M1B = {e2 , u − e2 }, where:

 
1
−1
1 1 
1 −1
e0 =   , e2 =  
2 −1
2 1
1
1


By using these choices of measurements in Eq. 44 and the
following equations, we obtain the value of the CHSH parameter: this is S = 4. This is the value attained by PR boxes, and
hence using the full effect space essentially yields the same
nonlocality as boxworld.
We therefore see that the Spekkens theory can be embedded into a nonlocal theory by embedding the effect space of
single system into the full dual cone. Moreover, we see completing the Spekkens theory in this way yields boxworld. This
provides a new understanding of why the Spekkens theory is
local: the measurements are too restricted.

[1] J. Barrett, Phys. Rev. A 75, 032304 (2007), URL http://
link.aps.org/doi/10.1103/PhysRevA.75.032304.

VIII.

CONCLUSIONS

We have extended the framework of generalized probabilistic theories. Given an arbitrary state space the traditional
framework determines the possible measurement outcomes as
corresponding to the complete set of probability valued linear
functionals on states. In contrast to the traditional framework,
our generalization allows the set of states and and the set of effects to be defined separately. As a result the upper bound for
the set of joint states, known as the maximal tensor product, is
no longer valid in its traditional form, but has to be replaced
by a generalized version.
As an application for restricted models, we provided a selfdualization procedure that alters any theory by restricting the
set of effects, such that states and the restricted effects are similarly related as states and unrestricted effects in strongly selfdual systems. We introduce specific examples for which the
self-dualization does not only give a formal resemblance but
reproduces a phenomenon called bit symmetry shown to only
hold for strongly self-dual systems in the traditional framework [14]. Furthermore, these self-dualized models show
quantum correlations, whereas the original models have correlations that are stronger than quantum correlations. In particular, the correlations of boxworld—a theory known to allow
correlations only restricted by the no-signalling principle—
has classical correlations if self-dualized, even though the
generalized maximal tensor product includes maximally entangled states. We showed how the Spekkens theory is related
to this model, since it is also self-dual and violates the norestriction hypothesis: but were it to satisfy this principle, by
taking the full dual cone, it would produce nonlocal correlations.
As another application for restricted models, we show that
restrictions can be used to alter theories, such that their measurements are inherently noisy. This is different to the unrestricted theories, since in our noisy theories it holds that for
pure states there is no non-trivial extremal effect occurring
with certainty. We derive the maximal CHSH violation [22]
of a noisy version of boxworld as a function of a noise parameter.
The modified framework is therefore suitable for examining
new situations that could not be addressed using the traditional
framework. In particular the self-dualization procedure might
be useful for the study of strong self-duality that has recently
received much interest [2, 9, 14].
ACKNOWLEDGMENTS

We thank Jonathan Barrett, Christian Gogolin and Haye
Hinrichsen for insightful discussions. PJ is supported by the
German Research Foundation (DFG). RL is supported by the
Templeton Foundation.

[2] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, preprint (2008),

<!-- page 15 -->
15
0805.3553v1.
[3] V. Scarani, N. Gisin, N. Brunner, L. Masanes, S. Pino, and
A. Acin, Phys. Rev. A 74, 042339 (2006), URL http://link.
aps.org/doi/10.1103/PhysRevA.74.042339.
[4] L. Masanes and M. P. Müller, New Journal of Physics
13, 063001 (2011), URL http://stacks.iop.org/
1367-2630/13/i=6/a=063001.
[5] L. Hardy, preprint (2011), 1104.2066.
[6] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Phys. Rev.
A 84, 012311 (2011), URL http://link.aps.org/doi/10.
1103/PhysRevA.84.012311.
[7] A. Short and J. Barrett, New Journal of Physics 12, 033034
(2010).
[8] H. Barnum, J. Barrett, L. O. Clark, M. Leifer, R. Spekkens,
N. Stepanik, A. Wilce, and R. Wilke, New Journal of
Physics 12, 033024 (2010), URL http://stacks.iop.org/
1367-2630/12/i=3/a=033024.
[9] P. Janotta, C. Gogolin, J. Barrett, and N. Brunner, New Journal of Physics 13, 063024 (2011), URL http://stacks.iop.
org/1367-2630/13/i=6/a=063024.
[10] L. Hardy, preprint (1999), quant-ph/9906123.
[11] I. Bengtsson, S. Weis, and K. Życzkowski, preprint (2011),
1112.2347.
[12] G. Ver Steeg and S. Wehner, QIC 9, 0801 (2009).
[13] S. Popescu and D. Rohrlich, Foundations of Physics 24, 379
(1994), ISSN 0015-9018, URL http://dx.doi.org/10.
1007/BF02058098.
[14] M. P. Müller and C. Ududec, Phys. Rev. Lett. 108, 130401
(2012),
URL
http://link.aps.org/doi/10.1103/
PhysRevLett.108.130401.
[15] R. W. Spekkens, Phys. Rev. A 75, 032110 (2007), URL http:
//link.aps.org/doi/10.1103/PhysRevA.75.032110.

[16] B. Coecke, B. Edwards, and R. Spekkens, Electronic Notes in
Theoretical Computer Science 270, 15 (2011).
[17] It can be shown that this follows from two conditions on joint
states: i) local tomography ii) the no-signalling principle. The
no-signalling principle forbids to send information by local operations on a joint state and will be explained in more detail
in section VI 3. Local tomography is the identification of joint
states by combinations of local measurements.
[18] M. Horodecki, P. Horodecki, and R. Horodecki, Physics
Letters A 223, 1
(1996), ISSN 0375-9601, URL
http://www.sciencedirect.com/science/article/
pii/S0375960196007062.
[19] J. Oppenheim and S. Wehner, Science 330, 1072 (2010), URL
dx.doi.org/10.1126/science.1192065.
[20] A. S. Holevo, Probabilistic and Statistical Aspects of Quantum
Theory, vol. 1 of North-Holland Series in Statistics and Probability (North-Holland, Amsterdam, 1982).
[21] K. Fukuda and A. Prodon, in Combinatorics and Computer
Science, edited by M. Deza, R. Euler, and I. Manoussakis
(Springer, 1996), vol. 1120 of Lecture Notes in Computer Science, pp. 91–111.
[22] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, Phys.
Rev. Lett. 23, 880 (1969), URL http://link.aps.org/doi/
10.1103/PhysRevLett.23.880.
[23] B. Cirel’son, Letters in Mathematical Physics 4, 93 (1980),
ISSN 0377-9017, URL http://dx.doi.org/10.1007/
BF00417500.
[24] J. Allcock, N. Brunner, N. Linden, S. Popescu, P. Skrzypczyk,
and T. Vértesi, Phys. Rev. A 80, 062107 (2009), URL http:
//link.aps.org/doi/10.1103/PhysRevA.80.062107.
