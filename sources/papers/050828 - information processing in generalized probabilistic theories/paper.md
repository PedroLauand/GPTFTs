---
type: paper
date: 2005-08-28
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:quant-ph/0508211v3)
reviewed: false
---

# Information processing in generalized probabilistic theories

Machine-generated and unreviewed text extraction of arXiv:quant-ph/0508211v3
(25 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/quant-ph/0508211v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Information processing in generalized probabilistic theories
Jonathan Barrett∗

arXiv:quant-ph/0508211v3 30 Nov 2006

Perimeter Institute for Theoretical Physics, 31 Caroline Street N, Waterloo, Ontario N2L 2Y5, Canada
I introduce a framework in which a variety of probabilistic theories can be defined, including classical and quantum theories, and many others. From two simple assumptions, a tensor product rule
for combining separate systems can be derived. Certain features, usually thought of as specifically
quantum, turn out to be generic in this framework, meaning that they are present in all except
classical theories. These include the non-unique decomposition of a mixed state into pure states, a
theorem involving disturbance of a system on measurement (suggesting that the possibility of secure
key distribution is generic), and a no-cloning theorem. Two particular theories are then investigated
in detail, for the sake of comparison with the classical and quantum cases. One of these includes
states that can give rise to arbitrary non-signalling correlations, including the super-quantum correlations that have become known in the literature as Nonlocal Machines or Popescu-Rohrlich boxes.
By investigating these correlations in the context of a theory with well-defined dynamics, I hope to
make further progress with a question raised by Popescu and Rohrlich, which is, why does quantum theory not allow these strongly nonlocal correlations? The existence of such correlations forces
much of the dynamics in this theory to be, in a certain sense, classical, with consequences for teleportation, cryptography and computation. I also investigate another theory in which all states are
local. Finally, I raise the question of what further axiom(s) could be added to the framework in
order uniquely to identify quantum theory, and hypothesize that quantum theory is optimal for
computation.
PACS numbers: 03.67.-a, 03.65.Ta

I.

INTRODUCTION

The question is periodically raised, what is responsible
for the power of quantum computation (or cryptography,
or information processing in general)? At a recent meeting in Konstanz [1], speakers referred to quantum entanglement; the superposition principle; the exponentially
growing size of Hilbert space with the number of qubits;
nonlocality and contextuality; the possibility of continuous reversible transformations between pure states; and
the so-called sign problem in Monte Carlo simulations of
certain types of quantum system [2]. It is perhaps unsurprising that there are so many different answers. The
problem is that the results of quantum information theory are already well understood as consequences of the
quantum formalism, and it is not clear that simply pointing to aspects of that formalism tells us anything new.
What we are really looking for is a better understanding
of the connections between information processing and
physical principles in general.
Such an understanding could be gained by studying information processing in a broader range of theories than
classical and quantum, where different physical principles
may hold. For any theory, whether it applies to Nature or
not, one can consider the information processing possibilities of this theory, the differences from those of classical
or quantum theory, and attempt to trace these possibilities back to the fundamental features of the theory.
Some authors have indeed investigated unrealistic theo-

∗ Electronic address: jbarrett@perimeterinstitute.ca

ries, with a view to understanding the relevant features
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
To make further progress along these lines, I introduce an operational framework for probabilistic theories
in which a broad range of different theories can be defined. The framework, described in Sections II, III and
IV, is based on that used by Hardy in his derivation of
quantum theory from simple axioms [14]. The basic idea
is that a state is represented as a vector of probabilities
of measurement outcomes. Transformations of a system
must correspond to linear transformations of this vector. By including probabilistic, that is normalizationdecreasing, transformations, a unified account of transformations and measurements can be given. Rather than
employ any of Hardy’s axioms, I introduce two assumptions that concern how separate systems combine to form
a joint system. The first is that operations on the separate systems commute (this implies a no-signalling principle), and the second is that the state of the joint system
can be completely specified by joint probabilities for local
measurements. From these assumptions a tensor product rule can be derived. This removes at least some of
the mystery from the quantum tensor product rule and
generalizes a derivation by Fuchs [15].
The resulting framework includes classical probabilistic theories, quantum theory, and many other theories
besides. The first thing one notices is that certain phenomena, usually thought of as specifically quantum, are
in fact generic. This means that they either appear in
all theories, or they appear in all theories except classical theories, which emerge as a very special case. As
shown in Section V, these phenomena include the nonunique decomposition of a mixed state into pure states, a

<!-- page 2 -->
2
theorem concerning the disturbance of a system on measurement, and the no-cloning theorem. (These observations are complementary to those of Ref. [13], where it is
noted that similar properties hold in nonlocal but nonsignalling theories.)
In addition to looking at generic properties of theories, it is useful to analyze at least one or two novel
theories in detail. These then provide well-understood
examples that can be contrasted with the classical and
quantum cases. Thus the rest of this work is devoted
to an analysis of two theories that admit a particularly
natural definition. The first of these allows arbitrary correlations between measurements on separated systems,
as long as they are non-signalling. I call it Generalized
Non-Signalling Theory (GNST). The correlations allowed
by this theory can be more nonlocal than quantum theory allows, and include the super-quantum correlations
that have come to be known variously in the literature
as Popescu-Rohrlich (PR) boxes, or Nonlocal Machines
[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]. Popescu and
Rohrlich raised the question of why quantum theory does
not allow these correlations. An investigation of a complete theory, with dynamics, that does include the correlations may help to answer this question. The second
theory allows the same states of single systems as GNST,
but does not allow any violation of Bell inequalities. For
this reason it is called Generalized Local Theory (GLT).
One of the interesting things about GNST is that there
are many direct analogues of quantum phenomena (in
addition to the generic phenomena mentioned above).
These include entanglement, nonlocality, a form of contextuality, and the Einstein-Podolski-Rosen (EPR) paradox. (Interestingly, a quite different toy theory introduced by Spekkens displays many of these phenomena
too [11].) However, there are also differences with quantum theory. A central insight of this work is that there
is a trade-off between the allowed states of a theory and
the allowed dynamics. This follows from the simple fact
that dynamics has to act in such a way that allowed
states are taken to allowed states. In the case of GNST,
the fact that all non-signalling correlations are possible
means that the dynamics is highly restricted. In fact, I
show in Section VI that the dynamics of single systems in
GNST is essentially classical, corresponding to no more
than relabellings of measurements and outcomes. This
result is extended to transformations and measurements
on simple kinds of bipartite systems (more complicated
cases are still open). GLT is in some sense intermediate,
with transformations on single systems similarly simple,
but with transformations on bipartite systems including
other possibilities.
These conclusions about dynamics have consequences
for information processing, discussed in Section VII. For
example, there is no teleportation in GNST, despite the
existence of highly nonlocal states that might have been
thought to facilitate a task like teleportation. Key distribution is possible in GNST and 1-2 oblivious transfer
in both GNST and GLT. Other cryptographic possibili-

ties, such as key distribution in GLT, or bit commitment
in either theory, are open questions. A natural circuittype model of computation can be defined for any theory
in the framework. The states and dynamics together in
GLT are sufficiently restricted that computation can be
simulated efficiently by a classical computer. The theorems concerning dynamics in GNST give evidence that
computation in this theory can also be simulated efficiently by a classical computer (despite the existence of
super-entangled states). The fact that quantum theory,
unlike GNST and GLT, achieves such a harmonious balance of states and dynamics leads to the following hypothesis that I leave open: a quantum computer can simulate computation in any theory in the framework with at
most polynomial overhead.
Finally, two motivations are not directly connected
with information processing. On the face of it, most of
the theories that can be written down in the framework
described suffer from similar interpretational problems as
quantum theory. For example, are pure states in one of
these theories best regarded as complete descriptions of
individual reality, as describing only ensembles, or as descriptions of agents’ degrees of belief? Although I do not
do this in this paper, consideration of these questions in
a broader framework may shed new light on the quantum theoretical problems. The other motivation is to
stimulate research into finding ways of deriving quantum
theory from physical principles (instead of laying down
a list of mathematical axioms, as per the standard textbook approach). What principles could be used to rule
out the other theories described and leave only quantum
theory? One reason for deriving quantum theory from
physical principles is that by modifying one or another
of the principles, we may discover new ways of going beyond quantum theory.

II.

A FRAMEWORK FOR PROBABILISTIC
THEORIES

This section describes in some detail a general operational framework in which probabilistic theories can be
written down. All theories in this framework share the
following features with classical and quantum theory.
1. Local operations on distinct subsystems commute.
In the case of a bipartite system AB, for example,
this means that if an operation is performed on system A alone, and an operation on system B alone,
it does not matter what order the operations were
performed in.

2. The global state of a composite system is determined by correlations between local measurements.

<!-- page 3 -->
3
A.

States and Operations

Consider a laboratory containing preparation devices
and operation devices. Preparation devices prepare a
system in a given state and operation devices act on a
system, in general changing its state. When an operation device is used, there may be several different outcomes, each occurring with some probability. Each outcome is identified by a different macroscopic event (for
example, a different light being illuminated on the device, or a different position of a pointer). Thus operation devices serve to perform both transformations and
measurements. Given the state of a system, it should
be possible to calculate the probabilities of measurement
outcomes for any measurement. Conversely, if the probabilities of measurement outcomes for any measurement
are known, then the state is known.
Suppose that systems come in different types, where in
quantum theory, for example, the type of system corresponds to the dimension of its Hilbert space. For each
type of system, there is some finite set F of measurements, each with a finite number of outcomes, such that
the state of the system can be completely specified by
listing the probabilities for these outcomes. For example, in quantum theory, the state of a spin-1/2 particle
can be specified by giving the probabilities of obtaining spin-up on measuring in the x, y and z directions.
Call the measurements in F fiducial measurements and
F the fiducial set. In general, there will be other measurements that can be performed on a system that are
not contained in the fiducial set (a measurement of spin
in some direction at 45◦ to the z-axis, say). The probabilities of outcomes of these measurements can nevertheless
be determined from the state. We ignore the possibility of states requiring an infinite number of probabilities
to be specified (despite the fact that quantum theory
includes infinite dimensional systems and classical probability theory infinite sample sets). The set of fiducial
measurements need not be unique. In general it will be
possible to find a different set (perhaps involving a different number of measurements with different numbers
of outcomes) that also suffices to specify the state.
This is essentially the framework described by Hardy
[14], who introduced the term fiducial for the statedefining measurements. (See also [15, 27, 28, 29], where
the idea of representing a state via probabilities for measurement outcomes is also explored.) Unlike Hardy, we
shall assume for convenience that the degrees of freedom
expressed in the state are internal degrees of freedom,
and that all measurements are measurements of internal
degrees of freedom. With respect to spacetime degrees
of freedom, systems behave classically, having a definite
position and velocity at all times. This seems the most
natural position to take given that we are most interested
in the information processing properties of the different
theories considered. However, it would be interesting to
extend this work, and to consider what Nature would be
like if all degrees of freedom, including those of space-

time, were described by a theory like one of the ones presented here (but extended to allow for infinite-outcome
measurements).
The above is summarized by
Assumption 1 The state of a single system can be completely specified by listing the probabilities for the outcomes of some subset F of all possible measurements.
These are the fiducial measurements. These probabilities
can be written arranged in a vector.

P (a = 1|X = 1)
 P (a = 2|X = 1) 


..


.




 P (a = 1|X = 2) 
~
P ≡
.
 P (a = 2|X = 2) 




..


.


..
.


(1)

P (a = i|X = j) is the probability of getting outcome i
when fiducial measurement j ∈ F is performed on the
system.
Normalization of the state would require that
X
P (a = i|X = j) = 1
∀j,

(2)

i

where the sum ranges over all the values i that the outcome can take for a particular measurement. It is convenient also to give a meaning to unnormalized states (just
as in quantum theory it is sometimes convenient to write
down unnormalized density matrices). Suppose that a
system is prepared in some (normalized) state and an
operation performed with an outcome i that is obtained
with probability less than 1. There is an unnormalized
state associated with i, each entry of which is the joint
probability of getting i followed by a particular outcome
for a subsequent fiducial measurement. This implies that
unnormalized states satisfy
X
X
P (a = i′ |X = j) =
P (a = i′′ |X = j ′ ) = c ∀j, j ′
i′

i′′

(3)
with 0 ≤ c ≤ 1. In the case described, c is the probability
of the outcome i. This idea generalizes to chains of operations, thus operations should be defined on unnormalized
states as well as on normalized ones. Define
X
P (a = i|X = j),
(4)
|P~ | ≡
i

where the right hand side is independent of the choice of
j. The notation |P~ | is used throughout and should not
be confused with more usual definitions of the norm of a
vector.
Suppose that for each type of single system, the fiducial measurements are fixed. A particular theory will

<!-- page 4 -->
4
specify, for each type of system, a set of allowed vectors
P~ . These correspond to physically possible states of a
system, i.e., states that can actually be prepared using
one of the preparation devices. There is no reason to
suppose that all vectors P~ that can be written down can
actually be prepared. For example, in quantum theory,
one cannot prepare a system that will with certainty return the outcome spin-up for spin measurements in both
the z- and x-directions. Call the set of allowed states S
(where there is a different S for each type of system but
we suppress this dependence).
Assumption 2 For each type of system, the set of allowed normalized states is closed and convex. The complete set of states S is the convex hull of the set of allowed
normalized states and ~0.
~0 is the vector with all entries 0. The idea behind this assumption is that it is always possible to toss a biased coin
and subsequently to be interested only in the joint probabilities of getting given measurement outcomes along
with heads. In this way one can ‘prepare’ unnormalized
states. If heads occurs with probability zero, the state ~0
is prepared. Convexity of S corresponds to the assumption that if it is possible to prepare states P1 and P2 , then
it is also possible to prepare any probabilistic mixture of
the two states. One may toss a coin, prepare either P1 or
P2 depending on the outcome, and then forget the outcome.1 Extreme points of S apart from ~0 are pure states.
States that are neither pure nor ~0 are mixed. Mixed states
can be written as a convex sum of pure states and ~0, but
this sum need not be unique.
Notice from Eq. (3) that S lies in a subspace of the
complete vector space. In general, we allow for the possibility that P~ is an over-complete description of the state
of a system. Thus there may be other linear constraints
that apply apart from Eq. (3) implying that S lies in a
smaller subspace still.
When an operation is performed, each outcome is associated with a transformation of the state of the system,
i.e., with a map from states to states:
P~ → P~ ′ = f (P~ ).

(5)

Some operations have only one outcome and the corresponding transformation preserves normalization of the
state (in quantum theory, these are the trace-preserving
completely positive maps). If an outcome occurs with
probability < 1, then it is associated with a transformation that decreases the normalization of the state (in
quantum theory, these are trace-decreasing completely
positive maps). In the most general case, one could
consider operations that change the system into a system of a different type (just as in quantum theory one

sometimes considers completely positive maps between
Hilbert spaces of different dimension). In this work I assume that operations do not change the type of system,
although the appropriate generalization is not usually too
difficult.
Consider a transformation acting on a system that is
in a mixed state, that is a state P~ such that
X
(6)
qi P~i ,
P~ =
i

~
where
Pthe Pi are allowed states and where 0 ≤ qi ≤ 1
and i qi = 1. One way of preparing a system in such
a state would be to prepare a system in the state P~i
with probability qi and then to forget the value of i. In
this case the transformed P~ must be the same convex
combination of the transformed P~i , that is
!
X
X
qi f (P~i )
∀Pi ∈ S. (7)
qi P~i =
f (P~ ) = f
i

i

It follows from this that the action of f on the set of
allowed states P~ can be represented as
P~ → M.P~ ,

(8)

where M is a matrix, i.e, f is a linear map. This is
not completely obvious from Eq.(7), since the equation
involves only convex combinations, and furthermore only
applies for those P~i ∈ S. A rigorous proof is given in
Appendix A.
An operation corresponds to a set of matrices {Mi }.2
The unnormalized state associated with the ith outcome
is Mi .P~ , and the probability of the ith outcome is
|Mi .P~ |
.
|P~ |

(9)

For each type of system, a particular theory will specify a
set of allowed operations. Denote this set O. An element
of O is a set of transformations {Mi }, and must be such
that the following holds.
Constraint 1
0≤

|Mi .P~ |
≤1
|P~ |

X |Mi .P~ |
i

|P~ |

=1

Mi .P~ ∈ S

∀i, P~ ∈ S,

(10)

∀P~ ∈ S,

(11)

∀i, P~ ∈ S.

(12)

2 A note on terminology. I shall continue to use the term operation
1 The assumption is also stated in such a manner as to rule out

the possibility of an unnormalized state without a corresponding
normalized state.

to refer to the experiment with a number of different outcomes
corresponding to the set {Mi }, and the term transformation to
refer to a single, in general normalization-decreasing, Mi .

<!-- page 5 -->
5
A further constraint is that each transformation Mi must
result only in allowed states when it acts on a system
that is part of a larger multi-partite system (see next
section). The following assumption results in some loss
of generality but also makes things simpler.
Assumption 3 For each type of system, there is a set
T of allowed transformations. A set of transformations
{Mi } is an element of O if and only if Mi ∈ T ∀i, and
Eq. (11) is satisfied. The set T includes the transformation that maps all P~ to ~0 and is convex.
With this assumption, once T is given, a separate specification of O is not needed. The reasons for convexity
are similar to those given for Assumption 2.
As mentioned above, the formalism of operations already includes measurements. Sometimes one is not interested in the state after measurement but only in the
probabilities of the different outcomes. In this case it is
convenient to associate with an operation {Mi } a set of
vectors {Ri } such that
~ i .P~ = |Mi .P~ | ∀P~ ∈ S.
R

(13)

Such a set can always be found. For a normalized P~ , the
~ i .P~ . It
probability of the ith outcome is then given by R
~
does not matter if the vector Ri is not unique - this simply means that different vectors can represent the same
measurement outcome. Denote by M the set of all sets
{Ri } such that Eq. (13) holds for some {Mi } ∈ O. M is
the set of allowed measurements. Denote by R the set of
allowed measurement vectors, that is, the set of vectors
~ such that R.
~ P~ = |M.P~ | ∀P~ ∈ S, for some M ∈ T .3
R
(Notation: R should not be confused with R, the set of
real numbers.)
B.

Multi-partite systems

So far, the framework described is similar to that used
by Hardy as a starting point for his derivation of quantum
theory (although I have been more explicit about treating transformations and measurements in a unified manner). Hardy narrows things down with various axioms.
Rather than adopt any of Hardy’s axioms, however, I introduce a small number of non-trivial assumptions that
concern how systems combine to make multi-partite systems. One reason for this is that most questions of information processing do not make sense without some notion of systems being composed of separate subsystems.

3 Recall that in quantum theory, an effect E is a positive operator

~ vectors are essentially a generalization
such that 0 ≤ E ≤ 1. R
of the effects to our framework. In the usual quantum formalism,
an effect can represent a yes/no measurement on a quantum state
ρ, with the probability of the
P yes outcome given by Tr(Eρ). A
set of effects Ei such that
i Ei = I, where I is the identity, is
a positive operator-valued (POV) decomposition of the identity,
and corresponds to a POV measurement.

From these assumptions I derive that systems combine
according to a tensor product rule. This is of independent interest since it sheds light on where this rule comes
from in quantum theory.
From hereon, the notion of a type of system is broadened. Thus multi-partite systems can come in different
types, where a particular type of multi-partite system is
composed of nA single systems of type A, nB single systems of type B, and so on. In all of this section, a system
A or B refers to a system of some specific type, that may
itself be a composite system.
Begin with the idea that, given a system A, it is possible to identify some operations as operations on system A
alone and that, in particular, the fiducial measurements
for system A are operations on system A alone. (Without
this, one might say that we have no business speaking of
separate systems in the first place.)
Assumption 4 Local Operations Commute. Consider a
joint system composed of systems A and B. Suppose
that an operation is performed on system A alone with
outcome oA and an operation on system B alone with
outcome oB . The final unnormalized state of the joint
system does not depend on the order in which the operations were performed. In particular, this implies that the
joint probability of getting outcomes oA and oB does not
depend on the ordering of the operations.
This assumption means that operations can be regarded
as performed simultaneously on systems A and B without
ambiguity. It also implies
Corollary 1 The No-Signalling Principle. If an operation is performed on system A, it is not possible to get information about which operation was performed by measuring system B.
The proof of the corollary is straightforward. Suppose
that an operation is performed on system A first, followed
by an operation on system B. Whichever operation was
performed on system A, the marginal probability of outcome oB is equal to the probability of oB in the case that
the operation on system B came first. The probability
of oB is thus independent of the operation on system A.
Assumption 5 The Global State Assumption. The
global state of a multi-partite system can be completely
determined by specifying joint probabilities of outcomes
for fiducial measurements performed simultaneously on
each subsystem.
Note that while the global state assumption is satisfied
in quantum theory and in classical probability theory, it
need not be satisfied in an arbitrary theory. For example,
it is not true in the case of quantum theory defined over
a real Hilbert space [30, 31, 32]. So this assumption has
significant content.4

4 Arguably, this is not the case for the assumption that local oper-

<!-- page 6 -->
6
It follows from these two assumptions that the global
state of a multi-partite system can be written in the form
of a vector of joint probabilities. For example, for a bipartite system AB, it will look like this:


P (a = 1, b = 1|X = 1, Y = 1)
 P (a = 1, b = 2|X = 1, Y = 1) 




..


.




P (a = 1, b = 1|X = 1, Y = 2)  .
P~ AB ≡ 


 P (a = 1, b = 2|X = 1, Y = 2) 




..


.


..
.


(14)

P (a = i|X = j) =

P (a = i, b = j|X = k, Y = l) =

j′

X

P (a = i, b = j ′ |X = k, Y = l′ ) ∀i, k, l, l′ ,
(15)

P (a = i, b = j|X = k, Y = l) =

i

X
i′

′

′

X
i′

j

X

(17)

where

P (a = i, b = j|X = k, Y = l) is the joint probability
of getting outcomes i and j when fiducial measurements
k and l are performed on the two subsystems. The nosignalling principle implies

X

in classical probability theory) is given by


P (a = 1|X = 1)
 P (a = 2|X = 1) 




..


.




A
,
~

P
(a
=
1|X
=
2)
P =

 P (a = 2|X = 2) 




..


.


..
.

′

P (a = i , b = j|X = k , Y = l) ∀j, k, k , l.
(16)

The reduced state for system A (analogous to the reduced state in quantum theory, or marginal probabilities

P (a = i, b = i′ |X = j, Y = j ′ ).

(18)
Here, a and X are the outcome and fiducial measurement
for the system whose reduced state is defined, and b and
Y are the outcome and fiducial measurement for the other
system. The no-signalling conditions of Eqs. (15), (16)
ensure that the sum on the right is independent of the
choice of j ′ .
As seen in the last section, a particular theory specifies
a set S of allowed states for each type of system. This
applies also for each type of multi-partite system. There
is, however, a constraint.
Constraint 2 Suppose that P~ AB ∈ S AB , where S AB is
the set of allowed states for the joint system. Suppose
that P~ A is the reduced state for system A corresponding
to P~ AB . Then P~ A ∈ S A , where S A is the set of allowed
states for system A.
That systems combine according to a tensor product
rule is asserted by the following three theorems. Proofs
are in Appendix B.
Theorem 1 Denote the vector spaces containing the vectors P~ AB , P~ A , and P~ B by V AB , V A , and V B respectively. Then one can identify
V AB = V A ⊗ V B .
Theorem 2 Any P~ AB ∈ S AB can be written
X
ri P~iA ⊗ P~iB ,
P~ AB =

(19)

i

ations commute, which may be regarded as part of the definition
of what we mean by an operation being on system A alone. Not
wishing to be dogmatic on this point, I have listed this principle with the other assumptions. We should distinguish, however, the implied no-signalling principle from the impossibility of
super-luminal signalling, which is a contingent fact that as far
as we know is true in our universe. To see the difference, consider that in the non-relativistic quantum mechanics of particles,
the no-signalling principle is valid, yet super-luminal signalling is
possible. In the present framework, the impossibility of superluminal signalling would imply an upper bound on the velocity of
systems and that Alice cannot carry out an operation on Bob’s
system if she is spacelike separated from it. But I shall not use
such notions, or indeed any notion of spacetime structure.

with the ri real, P~iA ∈ S A and P~iB ∈ S B . Both P~iA and
P~iB can be taken to be normalized and pure.
Theorem 3 Consider a transformation on system A
alone defined by
P~ A → P~ ′A = M A .P~ A .
The transformation of the joint system is given by
P~ AB → P~ ′AB = (M A ⊗ I).P~ AB .

<!-- page 7 -->
7
Recall that transformations include probabilistic transformations that decrease the normalization of the state.
Thus an immediate corollary of Theorem 3 is
Corollary 2 If a measurement is performed on system
A alone, with state P~ A , the probability of a particular
outcome is given by
~
~⊗~
R.P~ A = (R
I).P~ AB .

(20)

Here, I~ is a vector representing the identity measurement, that is ~
I.P~ B = |P~ B | ∀P~ B ∈ S B . The way things
are set up, I~ is not unique but can always be taken to be
(1, . . . , 1|0, . . . , 0|0, . . . , 0| · · · ).
Much follows from these theorems and corollary.
Collapsed states. Suppose that an operation is performed on a system A in a state P~ A . Suppose that
the operation has outcomes i such that the final normalized state conditioned on outcome i is given by P~iA ≡
Mi P~ A /|Mi P~ A |. The change in the state of system A
is analogous to the quantum mechanical collapse of the
state vector. If systems A and B begin in some joint state
P~ AB , and a measurement is performed on system A, then
the final state of system B, conditioned on a particular
outcome for the measurement, is also unambiguously determined. Thus this “collapse” is also well-defined “at
a distance”. Typically, similar questions of interpretation arise in theories in this framework as do in quantum
theory. Is this collapse a real process? A change in an
agent’s degrees of belief following her measurement? And
so on.
Entanglement and nonlocality. In Theorem 2, a joint
state of a system AB is written as a linear sum of direct
product states. Note that the theorem does not assert
that a joint state of AB can be written as a convex combination of direct product states. In general, there will
be joint states that cannot be written in this form. These
are the entangled states of the theory. Entanglement is
distinct from nonlocality, where the latter means violation of a Bell inequality. Thus i) there are theories such
as classical theories that have no entanglement or nonlocality, ii) there may be theories that have entanglement
but no nonlocality, and iii) there are theories, such as
quantum theory and GNST developed below, that have
both entanglement and nonlocality, although these may
not coincide.5

5 It is clear that entanglement is necessary for nonlocality. But in

quantum theory there are entangled mixed states that are local
[33, 34], hence entanglement is not sufficient for nonlocality. In
GNST, on the other hand, entanglement and nonlocality do coincide. This is because if one can write down a local model for a
particular state in GNST, then the model will itself define a convex decomposition of that state into product states allowed by
the theory. This is not true in quantum theory because arbitrary
local models can employ probability assignments not corresponding to any quantum state.

Multi-partite systems. The state of a multi-partite system can be written as a vector P~ AB...Z ∈ VA ⊗ VB ⊗
· · · ⊗ VZ . This vector can
P be written as a linear sum
of direct product states i ri P~iA ⊗ P~iB ⊗ · · · ⊗ P~iZ , with
ri ∈ R, P~ A ∈ S A , and so on. A transformation on system A alone takes the form M ⊗ I ⊗ · · · ⊗ I, and similarly
for transformations on B, . . . , Z alone. These extensions
of the above theorems follow, since those theorems were
stated for arbitrary bipartite systems AB and included
the fact that A and B may themselves be composite.
Finally, recall that a theory, in addition to specifying
the set S of allowed states for each type of system, must
also specify the set T of allowed transformations.
Definition 1 A transformation on system A is welldefined if (MiA ⊗ I).P~ AB ∈ S AB whenever P~ AB ∈ S AB ,
for all types of system B.
This definition corresponds to the fact that in quantum
theory, allowed transformations must be completely positive maps (and not, e.g., merely positive maps). An
obvious constraint is
Constraint 3 For each type of system, all transformations ∈ T must be well-defined.
A natural assumption is
Assumption 6 If P~ A ∈ S A and P~ B ∈ S B , then P~ A ⊗
P~ B ∈ S AB .
A final assumption that is convenient is
Assumption 7 A theory first specifies a set S of allowed
states for each type of system. All transformations that
are well-defined are then allowed transformations.
This assumption is indeed satisfied by all the theories
considered below, including classical theories, quantum
theory, GNST, and GLT. It is nice because it means that
a theory is completely specified once the allowed types
of system are specified, along with the set S of allowed
states for each type. In this case, Assumption 7 defines
the set T . The way things are set up, each of the sets
O, M and R is in turn defined by T . Assumption 7 also
ensures that certain other obvious constraints hold that
do not then need to be stated separately. For example,
it implies that if M ∈ T and N ∈ T , then M.N ∈ T .
Along with Constraint 3, it implies that if M A ∈ T A ,
then M A ⊗ I B ∈ T AB . Finally, Assumption 7, along
with Assumption 6 and Constraint 2, implies that if a
procedure consists in introducing an ancilla to system A,
performing some joint transformation on A and ancilla
and then throwing away the ancilla, then the corresponding transformation on A alone is ∈ T A .
The fact that transformations have to be well-defined
yields one of the main insights of this work. There is
a rich interplay between the set of allowed states, the
allowed dynamics, and the information processing possibilities that a theory offers. For example, if a theory is

<!-- page 8 -->
8
modified by enlarging the set of allowed states (adding
super-correlated states to quantum theory, perhaps), one
might naively think that this must increase the information processing possibilities. However, enlarging the set
of allowed states may well have the effect of decreasing
the set of allowed transformations, in which case the effect may well be the opposite.

III.

A BRIEF NOTE ON AMBIGUITIES

There are a couple of points that deserve a mention
here in case it be thought that they cause problems (this
section may perhaps be omitted on a first reading). First,
two theories may be identical in their structure, that is
the sets S, T , O, R and M of allowed states, transformations, operations, outcomes and measurements, could be
mathematically identical in each theory, yet the theories
be different physically because the mathematical objects
are assigned to different physical objects. For example,
a particular preparation device could be associated with
one state in one theory and another state in the other
theory.
Second, one theory could be made to look different,
that is have different sets S, T , O, R and M, simply because different measurement devices are chosen to correspond to fiducial measurements. Thus in quantum theory
the state of a qubit could be specified by the probabilities for the outcomes of spin measurements in the x, y
and z directions. The set S is then a sphere. Equally,
the quantum state could be specified by the probabilities for measurements
in the x, y and n directions, where
√
~n = 1/ 2(~x + z~). In this case, the set S is an nonspherical ellipsoid. A fiducial set may even have different
numbers of measurements and outcomes. For example,
any quantum state can be expressed by giving the probabilities of the outcomes for a single, informationally complete POV measurement [15]. The important thing is
that the outcomes of the fiducial measurements in the
new formulation are represented by linearly independent
vectors in the old formulation. Thus there is an invertible
matrix N such that the two formulations are related by
~ ′T = R
~ T .N −1 , and M ′ = N.M.N −1 . The
P~ ′ = N.P~ , R
~ ′ .P~ ′ = ~
theory makes the same predictions since R
R.P~ ,
and so on.
The first of these points means that in order to compare the predictions of two theories, one has to know
which physical devices different preparations and operations correspond to. But being primarily interested in
the information processing properties of theories, we can
ignore this issue and concentrate on the structure of the
theories. The second point ensures that we can do this
unambiguously. The structure of a theory and the conclusions drawn for information processing do not depend
on which measurements are chosen for the fiducial set.

IV.

SOME DIFFERENT THEORIES

It is useful to see examples of theories that can be described in this framework. The most important are classical theories and quantum theory. Two others are GLT
and GNST. All of these theories satisfy Assumption 7,
which means that each is completely determined by the
set S of allowed states for each type of system.
A.

Classical theories

Suppose that for some particular type of system, the
fiducial set can be chosen as a single measurement with d
outcomes, and that any (possibly sub-normalized) probability distribution over these outcomes corresponds to a
(possibly sub-normalized) allowed state. In this case, the
system is classical. A classical theory is one for which all
systems are classical. The most comprehensive classical
theory is the one for which there is a type of system for
every d ≥ 1. For a classical system, S is a simplex. Pure
states are represented by vectors ~ei , with a 1 for the ith
component and 0s elsewhere. The state of a bipartite
system of two classical systems is also represented by a
vector from a probability simplex, the entries being the
joint probabilities for outcomes i and j when the fiducial
measurement is performed on each system. An allowed
transformation M must map a pure state ~ei to another
allowed state. It is easy to show that each entry of M
must be positive, and the sum of each column must be
≥ 0 and ≤ 1. In the case that M preserves normalization,
it is a stochastic matrix.6 The set R is a hypercube.
Consider, for example, an ordinary die which can exist
in six different deterministic states. The P~ vector is six
dimensional and gives the probabilities that the die’s uppermost face is 1, 2, . . . , 6. An example of a measurement
is one that asks, is the uppermost face 1 or 2? The yes
~ = (1, 1, 0, 0, 0, 0).
outcome corresponds to the vector R
The state of two dice, A and B, can be written as a 36dimensional vector, whose entries are the probabilities
for the uppermost faces being 11, 12, . . . , 66.
Suppose that the reduced states of the two dice are
given by P~ A = P~ B = 1/6(1, 1, 1, 1, 1, 1). One possible
joint state compatible with P~ A and P~ B is a direct product
P~ AB = P~ A ⊗ P~ B
 
1
 

1 1
=
. 
.
36 
 .. 
1

6 In this work, a stochastic matrix is a not necessarily square ma-

trix, with positive entries, whose columns each sum to 1.

<!-- page 9 -->
9
This corresponds to the two dice being uncorrelated. But
another possible joint state with the same reduced states
is
(
1/6 i = j,
AB
P~ij =
0
otherwise.
This corresponds to perfect correlation and obviously
cannot be written as a direct product. Of course there is
no entanglement or nonlocality in this theory.7

B.

Quantum Theory (in finite dimensions)

Quantum theory only allows certain types of system.
For example, there are no systems that can be described
with two fiducial measurements each with two outcomes.
A qubit can be described by three fiducial measurements
with two outcomes, e.g., spin measurements in the x, y
and z directions. Once a set of fiducial measurements is
chosen quantum theory tells us what the allowed states
P~ are. In the simple case of a qubit, the set of normalized
states is the Bloch sphere. In the case of higher dimensional quantum systems it does not appear to be so easily
characterized (except via the usual quantum formalism
of course). The transformations that are well-defined,
in the sense of Definition 1, correspond precisely to the
linear completely positive maps. It is usually assumed
that any such map corresponds to a physically possible
~i
operation, thus Assumption 7 is satisfied. Any set of R
P
~
~
~
~
~
~
with 0 ≤ Ri .P ≤ 1 ∀i ∀P ∈ S and i Ri .P = 1 ∀P ∈ S
is a positive operator-valued measurement in the usual
formalism.
There is nothing new in the fact that quantum states
can be represented as real vectors and transformations
as matrices acting on these vectors. It is well known
that Hermitian operators in d dimensions form a d2 dimensional real vector space, with an inner product
given by Tr(AB). Linear completely positive maps correspond to d2 × d2 matrices acting on this space. But the
present framework does not correspond exactly to this
representation (e.g., it is possible that P~ .P~ > 1), so it is

7 There is nothing difficult in the preceding remarks.

But part
of the aim of Section II B is to deflate the significance of the
tensor product rule for combining systems in quantum theory.
Thus it is useful to note that a similar rule arises quite naturally
in what is essentially classical probability theory. The quantum
tensor product rule does not have to be regarded, as it frequently
is, as a mysterious replacement for the Cartesian product used
in combining deterministic classical states. If quantum states
(even pure ones) are more analogous to probabilistic classical
states than anything else - in other words if some version of the
epistemic interpretation of the quantum state is correct - then a
tensor product rule is exactly what one would expect. Thus one
way of viewing the tensor product is as evidence for the epistemic
interpretation.

useful to see an example. A qubit whose state is spin up
in the z-direction can be written

 

P (↑ |x)
1/2
 P (↓ |x)   1/2 

 


 

P
(↑
|y)
1/2




P~ = 
=
,
 P (↓ |y)   1/2 

 

 P (↑ |z)   1 
P (↓ |z)

0

where P (↑ |x) is the probability of obtaining spin up
when measuring in the x direction, and so on. It can
now be verified that if, for example,
√ spin is measured in
the n-direction, where ~n = 1/ 2(~x + z~), then the up
outcome corresponds to the vector


−1 1 1 1
−1
1
~ =
√ , √
√ , √
.
,
R
2 2 2 2 2 2 2 2 2 2
~′ = R
~ + C,
~ where
This vector is not unique. Any vector R
~
~
~
C.P = 0 ∀P ∈ S, represents the same measurement outcome. The unitary transformation usually written as the
Pauli matrix σz would correspond to



0 1 0 0 0 0
1 0 0 0 0 0




0 0 0 1 0 0
M =
.
0 0 1 0 0 0


0 0 0 0 1 0
0 0 0 0 0 1

C.

Generalized Non-Signalling Theory

Suppose that for any pair n, k > 1, there is a corresponding type of single system, whose state can be described by a set of n fiducial measurements, each with
k outcomes. Call this an (n, k) system.8 For a single
system, allow any state P~ , provided the entries of P~ are
between 0 and 1 and Eq. (3) is satisfied. For multi-partite
systems, allow any state P~ , provided entries are between
0 and 1, Eq. (3) is satisfied, and the no-signalling conditions of Eqs. (15),(16) are satisfied for all bipartite splittings. The resulting theory is Generalized Non-Signalling
Theory.
It is useful to see some examples of systems in this
theory. The simplest kind of single system has two binary
fiducial measurements. This type of system plays a role
somewhat analogous to that of a classical bit or a qubit,

8 A more general theory would include further types

of system
with different numbers of outcomes for different fiducial measurements. I ignore this possibility. I do not believe that it
would change much beyond introducing uninteresting complications into some of the proofs.

<!-- page 10 -->
10

(2,1)

(2,1)

(2,2)

(2,2)
(1,1)
(2,1)

v
(1,2)
(2,2)

v

v
(1,1)

(1,1)

FIG. 3: Another allowed transformation.

(1,2)

FIG. 1: The space of normalized states for a gbit in GNST
corresponds to the square. If the measurements X = 1 and
X = 2 are associated with spin measurements in the z and x
directions, then the space of states for a quantum mechanical
qubit corresponds to the circle.

(2,1)

(2,2)

(1,1)

(1,2)

(2,1)

(2,1)
(2,1)

(2,2)

(1,1)

(1,1)

(2,2)

(1,2)
(1,2)

FIG. 4: A forbidden transformation.

v
v
(1,1)

(1,2)

(1,2)

(2,2)

FIG. 2: An allowed transformation.

so from hereon it is called a gbit (for generalized bit). The
space of possible normalized states is shown in Fig. 1.
There are four pure states, which correspond to the four
ways of assigning definite outcomes to the X = 1 and
X = 2 fiducial measurements. In the figure, these are
represented by (1, 1), (1, 2), (2, 1), and (2, 2), where (1, 2),
for example, is the state which returns a = 1 for the X =
1 measurement and a = 2 for the X = 2 measurement,
and is also represented by P~ = (1, 0|0, 1). Thus pure
states of single systems have a definite outcome for each
fiducial measurement - there is no uncertainty principle.
As noted in the figure, if the measurements X = 1 and
X = 2 are associated with spin measurements in the z
and x directions, then we can include possible states of
a qubit in the diagram, and these form a circle inscribed
in the square. Qubits of course have an extra degree
of freedom, namely spin in the y direction. For (3, 2)
systems the space of states is a cube, with an inscribed
sphere (the Bloch sphere) representing quantum states.
Consider the possible transformations of a gbit (for
simplicity, restrict attention to those that preserve normalization). An allowed transformation will transform
the square in such a manner that all points remain in the
square, otherwise the transformation is not well-defined
in the sense of Definition 1. The transformations of
Figs. 2 and 3 are allowed. But the transformation of
Fig. 4 is not allowed. Transformations in quantum theory are less restricted because the requirement is only

that points in the circle are transformed into points in
the circle. So a rotation of π/4, as in Fig. 4, is fine, and
indeed corresponds to the well known π/8 gate.
It begins to look as if the dynamics of single systems
in GNST is rather simple. Indeed, this is the case. Section VI contains a theorem that states that for single
systems in GNST, allowed transformations correspond
essentially to relabellings of measurements and outcomes,
and probabilistic combinations thereof. Thus in a sense,
the dynamics is classical. Despite this, the dynamics
does contain possibilities that quantum dynamics does
not. Consider a (3, 2) system, whose space of normalized states is a cube, with the quantum Bloch sphere inscribed. A possible transformation is a reflection in the
center of the sphere. This corresponds to the so called
Universal NOT gate of quantum theory, which is not an
allowed transformation since it is not completely positive.
The multi-partite states of GNST are noteworthy in
that they include states that are more nonlocal than
quantum theory allows. For example, given a bipartite
system of two gbits, the following is a possible state.

11 

XY = 12 → P (a = 1, b = 1|XY ) =

21 

(21)

P (a = 2, b = 2|XY ) = 1/2,

XY = 22 → P (a = 1, b = 2|XY ) =
(22)
P (a = 2, b = 1|XY ) = 1/2.

The correlations obtained from fiducial measurements on
this state return a value of 4 for the left hand side of the

<!-- page 11 -->
11
following inequality
P (a = b|11) + P (a = b|12)
+ P (a = b|21) + P (a 6= b|22) ≤ 3

E.

(23)

(this is the CHSH inequality [35] written in a slightly
different form than usual). These correlations cannot
be obtained from measurements on any quantum state
since by Tsirelson’s theorem √
[36], quantum states can
only reach a maximum of 2 + 2.9
Information processing in GNST is discussed in Section VII. The theory’s permissiveness with respect to
states implies that some things can be achieved that are
impossible in quantum theory. These include 1-2 oblivious transfer, van Dam’s scheme for the easy solution
of communication complexity problems [25], and a kind
of super-quantum memory. The restricted nature of the
dynamics, however, implies that there is no teleportation
or super-dense coding. The theorems of Section VI give
evidence that computation is no better than classical.

D.

Generalized Local Theory

Suppose that, as in GNST, for any pair n, k > 1, there
is a corresponding type of system, whose state can be defined with n fiducial measurements with k outcomes. As
in GNST, all P~ with entries between 0 and 1 satisfying
Eq. (3) are allowed states. The only multi-partite states
allowed, however, are those for which the fiducial measurements return local (non-Bell-violating) correlations.
This defines Generalized Local Theory.
As in GNST, the pure states of single systems in this
theory are those that have a deterministic outcome for
each fiducial measurement. Since multi-partite states are
local with respect to fiducial measurements, the pure
states of a multi-partite system are precisely those in
which each subsystem is in a deterministic pure state.
An arbitrary state of a multi-partite system is a convex
mixture of these. It follows that no state in this theory
can violate a Bell inequality, even if non-fiducial measurements are performed. Hence the name.
GLT is more general than quantum theory in allowing
arbitrary single system states, but more restricted in not
allowing nonlocal states. As described in Section VII,
GLT allows 1-2 oblivious transfer. Computation in GLT,
however, is efficiently simulable by a classical computer.

9 These

non-signalling super-quantum correlations were written
down by Khalfi and Tsirelson [16], and were independently introduced by Popescu and Rohrlich [17]. Other examples of superquantum correlations, involving more measurements or parties,
are given in Ref. [18]. The latter are also allowed in GNST.

Other possibilities

There are other possibilities that would be interesting
to investigate. For example,
1. A theory that is essentially quantum theory but
with only separable states allowed.
2. A theory in which the state of a single system must
be a quantum state, but in which the state of a
multi-partite system can be anything, as long as the
no-signalling principle and the restriction that the
reduced states for the individual subsystems must
be quantum are satisfied. The latter idea has been
investigated in Ref. [37], where it is shown, amongst
other things, that Tsirelson’s theorem still holds.
V.

GENERIC PROPERTIES OF THEORIES

One of the reasons for introducing a framework encompassing many different theories is that it is interesting to identify properties of theories that are generic, in
the sense that they are shared by all or most theories
in the framework. Some features, usually thought of as
specifically quantum, are present in all theories in our
framework except theories that are classical (in the sense
of Section IV A). Thus classical theories are very special!
These features include the fact that mixed states do not
always have a unique decomposition into pure states, and
a no-go theorem for universal cloning. More exact statements of these claims are given in this section. Proofs are
in Appendix C. It is tedious to write always all theories
in the framework, so from hereon this is shortened to all
theories, taking the assumptions of Section II as read.
First,
Theorem 4 Suppose that for a particular type of system,
every mixed state has a unique decomposition into pure
states and ~0. Then the system is classical.
The next theorem concerns the disturbance of systems
on measurement and is due in part to Howard Barnum
and Alex Wilce [38]. Say that a transformation disturbs
a state P~ if there is no constant c such that M.P~ = c P~ .
This means that, conditioning on the outcome corresponding to this transformation, the state is no longer
P~ . A transformation is non-disturbing if no pure state is
disturbed and an operation {Mi } is non-disturbing if all
Mi are non-disturbing.
Theorem 5 For any system, let V be the vector space
in which states are defined, and let VS be the subspace
spanned
L by S. Then VS can be written as a direct sum,
VS = i Vi , where the Vi are subspaces of VS , such that
1. Every pure state P~ is contained in some Vi .

2. A non-disturbing
transformation is of the form
L
e
I
,
where
0 ≤ ei ≤ 1, and Ii is the
M =
i
i
i
identity on Vi .

<!-- page 12 -->
12
It follows that non-disturbing operations have the same
outcome probabilities for pure states in the same Vi , and
thus cannot distinguish them. It is easy to show that a
system is classical if and only if each Vi contains exactly
one pure state. For a quantum system without superselection rules, VS cannot be further decomposed into
a direct sum. Non-disturbing operations have the same
outcome probabilities for all pure states, each transformation being proportional to the identity on VS . An
example of such an operation would be to toss a coin,
without interacting with the system at all, and to output
the result. For a quantum system with superselection
rules, pure states from the same sector are elements of
the same Vi , and different sectors correspond to different
Vi .
Theorem 5 has implications for cloning. Cloning refers
to the following procedure:
1. Begin with a system A in a pure state. Denote its
state P~ .
2. Introduce a system B of the same type, prepared in
a standard state ~
Q. The state of the joint system
~
~
is P ⊗ Q.
3. A joint transformation M acts on the pair of sys~ ∝
tems such that the final state is (M )(P~ ⊗ Q)
~
~
P ⊗ P.
A deterministic universal cloning procedure always succeeds and works on all pure states. It implies the exis~ such
tence of a normalization-preserving M and a state Q
that (M )(P~ ⊗ ~
Q) = P~ ⊗ P~ for all pure P~ . A probabilistic universal cloning procedure is allowed to output a fail
outcome, but conditioned on success, the final state must
be P~ ⊗P~ . There must be a non-zero probability of success
for all pure states P~ . This type of cloning implies the existence of a non-zero M such that (M )(P~ ⊗ ~
Q) = cP~ ⊗ P~
~
~
for all pure P , where c can vary with P , and 0 < c ≤ 1.
Theorem 6 With the exception of classical systems,
there is no probabilistic universal cloning procedure.
This of course implies that with the exception of classical systems, there is no deterministic universal cloning
procedure.
Theorems 4, 5 and 6 apply even to classical theories if
extended to mixed states. Thus there are mixed states
with a non-unique decomposition into mixed states. All
transformations disturb at least one mixed state unless
they are proportional to the identity.10 And cloning of

10 This is not at all surprising if put into more prosaic terms. Con-

sider that a die is in a state such that the probability of each
face being uppermost is 1/6. Suppose that the die is measured,
to find out which face is uppermost, and the value 1 found.
Then, if it is assumed that the measurement operation was done

classical mixed states is impossible.11 One possible interpretation of these remarks is as further evidence that
quantum pure states are more akin to classical mixed
states than classical pure states.
There are many other questions concerning properties
that are common to all theories, or all except classical theories. In Ref. [40], the quantum no-broadcasting
theorem is generalized to arbitrary non-classical theories within a framework closely related to the present
one. It can also be shown that all theories in the framework have an infinite de Finetti theorem [41], and that
polynomially-sized computations in these theories can be
simulated classically in polynomial space [42]. Features
such as these can be regarded as arising solely from the
assumptions that were made in setting up the framework.

VI.

DYNAMICS IN GNST AND GLT

Part of the motivation of this work is to consider which
features of a theory, in particular those features related
to information processing, arise from which assumptions.
It is particularly interesting if significant features, such
as the no-cloning theorem above, arise from very minimal assumptions and are thus shared by a broad class of
theories. Another part of the motivation is to investigate
theories that are different from those we already know
about. These theories need not even be empirically adequate; a compare and contrast exercise will still be useful
to learn more about those theories that are empirically
adequate. Thus the next two sections are devoted to a
detailed investigation of GNST and GLT.
In Section IV C the dynamics of a gbit was briefly
discussed. There are four pure states of a gbit, corresponding to the four ways of assigning definite outcomes to the two measurements. The space of normalized states is a square, with a normalization-preserving
transformation being a linear transformation of this
square. Let us consider more general types of system
in GNST and GLT, but continue to focus on normal-

in the most obvious way, the state after measurement is not
1/6(1, 1, 1, 1, 1, 1), but (1, 0, 0, 0, 0, 0). Of course the measurement operation may be such that the die is recast after the outcome is obtained, resulting in a final state of 1/6(1, 1, 1, 1, 1, 1).
But then an initial state of (1, 0, 0, 0, 0, 0) would be disturbed.
11 Suppose that Alice prepares a die in one of two ways, each corresponding to a probability distribution over the different faces.
The first prepares, say, the state 1/12(6, 2, 1, 1, 1, 1) and the second the state 1/6(1, 1, 1, 1, 1, 1). The die is given to Bob who is
required to perform a cloning operation. This means that Bob
must prepare another die such that if Alice used the first preparation, its state is 1/12(6, 2, 1, 1, 1, 1), and if she used the second,
then 1/6(1, 1, 1, 1, 1, 1). Furthermore, if the dice are measured
after Bob’s operation, the results must not be correlated. This
last clause prevents Bob from using a device that simply reads
the uppermost face of the die and prepares another in the same
state. It is easy to see that even if Bob’s cloning procedure is
allowed to be probabilistic, he cannot do it.

<!-- page 13 -->
13

X

ized systems and normalization-preserving transformations, i.e., operations corresponding to a single matrix,
{M }. For this section and the next, transformation
means normalization-preserving transformation, with the
investigation of probabilistic transformations left for future work.
The space of normalized states of an (n, k) system is a
polytope, the vertices corresponding to pure states. Pure
states are of the form
P~ = (0 . . . 1 . . . 0|0 . . . 1 . . . 0| . . .).

F1
X’
S

X

a’
Allowed transformations must take points in the polytope
to points in the polytope. This condition is so restrictive
that the following theorem holds.
Theorem 7 Normalization-preserving transformations
of single systems in GNST or GLT, thought of as active,
correspond to passive transformations that simply relabel
fiducial measurements and outcomes, or to convex combinations of such. Equivalently, for a transformation of
an (n, k) system, the matrix M representing the transformation can be written

M11 · · · M1n

..  ,
M =  ...
. 
Mn1 · · · Mnn


where Mij is a k × k matrix, and where MijP= αij Sij , for
Sij a stochastic matrix, 0 ≤ αij ≤ 1, and j αij = 1.

A useful pictorial representation of this theorem is given
in Fig. 5. A related result is
Theorem 8 The only measurements on single systems
in GNST or GLT are fiducial measurements, possibly
with outcomes relabelled, or correspond to convex combinations of such.
Theorem 8 is illustrated pictorially in Fig. 6. The proofs
of Theorems 7 and 8 are contained in Appendix D.
In the case of GNST, the following theorem holds for a
bipartite system of two gbits, and suffices to characterize
the normalization-preserving transformations of such a
system.

Theorem 9 Consider a system of two gbits in GNST,
and suppose that a normalization-preserving transformation is performed. Suppose that this transformation is
followed by the fiducial measurements X, Y on the two
subsystems, with outcomes a, b. The joint probability of
obtaining outcomes a, b is equal to that obtained from a
convex combination of procedures of the following kind.
First, perform a fiducial measurement X ′ on one of the
gbits, where X ′ may depend on X and Y . Denote the
outcome a′ . Then perform a fiducial measurement Y ′ on
the other gbit, where Y ′ may depend on X, Y and on a′ .
Denote the outcome b′ . The final outcome pair (a, b) is
a function of X, Y , a′ and b′ .

F2

a
FIG. 5: Transformations of single systems in GNST and GLT
can always be represented as the appending of classical circuits as shown here, or as convex combinations of transformations of this type. If a fiducial measurement X is performed on the transformed system, this can be thought of as
performing fiducial measurement X ′ on the original system,
where X ′ = F 1(X) for some function F 1. When measurement X ′ is performed on the original system, outcome a′ is
obtained with some probability. The probability of obtaining
outcome a for the measurement X on the transformed system is equal to the probability of obtaining an outcome a′
such that a = F 2(X, a′ ), for some function F 2.

Of course this theorem can also be expressed in terms
of a formal constraint on the transformation matrix M ,
but in this case it is more complicated and less enlightening. Theorem 9 may also be understood pictorially, as
in Fig. 7.
Theorem 10 In GNST, the only measurements on bipartite systems comprised of two gbits correspond to convex combinations of procedures of the following kind.
First, perform a fiducial measurement X on one of the
gbits, obtaining an outcome a′ . Then perform a fiducial
measurement Y on the other gbit, where Y may be a function of a′ , obtaining an outcome b′ . The final outcome is
a function of a′ and b′ .
Theorem 10 is illustrated in Fig. 8. The proof of Theorem 9 is given in Appendix D. It is an open question whether similar theorems hold for transformations
and measurements on arbitrary multi-partite systems in
GNST. It can be shown that in GLT, there definitely do
exist possibilities for measurements and transformations
on multi-partite systems that do not reduce to one of the
forms presented in this section.
The proofs in Appendix D also make clear the following. The most fine-grained measurements on single systems in GNST or GLT can be represented by a set of vec~ i , such that each R
~ i has one element between 0 and
tors R

<!-- page 14 -->
14

X
a’
S
X

a’

F1
Y’

F1
S1

FIG. 6: Measurements on single systems in GNST or GLT
can always be performed via a procedure of the type illustrated here, or via a convex combination of such procedures.
First, fiducial measurement X is performed and outcome a′
is obtained. The outcome a of the complete measurement is
then a = F 1(a′ ). This result applies to measurements with
an arbitrary number of outcomes.

Y

XY
a’

F1

F2
X’

S1

a’

b’

a

X

S2

Y’
S2

X Y a’

b’
F3

a

b

FIG. 7: In GNST, transformations on bipartite systems comprised of two gbits can always be represented by the appending of classical circuits as shown here, or by a similar construction inverted with respect to the two systems, or by a convex
combination of such. For the construction shown here, this
means that if fiducial measurements X, Y are performed on
the transformed system, one may think of this as first performing a fiducial measurement X ′ on one half of the original
system, where X ′ = F 1(X, Y ). This gives an outcome a′ .
Then, perform a fiducial measurement Y ′ on the other subsystem, where Y ′ = F 2(X, Y, a′ ). This gives an outcome b′ .
The final outcome pair (a, b) is determined by a function F 3
of X, Y , a′ and b′ .

F2

a
FIG. 8: In GNST, measurements on bipartite systems of two
gbits can always be carried out by a procedure like that illustrated here, by a similar procedure inverted with respect
to the two subsystems, or by a convex combination of such.
For the procedure shown here, this means that first, a fiducial
measurement X is performed on one subsystem, and outcome
a′ is obtained. Then fiducial measurement Y ′ is performed on
the other subsystem, where Y ′ = F 1(a′ ), and outcome b′ is
obtained. The outcome a of the complete measurement is
given by a = F 2(a′ , b′ ). This result applies to measurements
with an arbitrary number of outcomes.

~ i is analogous to an effect in
1 and the rest 0. Such an R
quantum theory that is proportional to a 1-dimensional
~ i is analogous to a non-degenerate
projector. A set of R
~ is a basis vector (one
projective measurement if each R
P i~ ~
element 1 and the rest 0) and i Ri .P = 1 ∀P~ ∈ S. The
corresponding measurement is simply a fiducial measure~ i for each outcome. It is then immediate
ment, with an R
that, at least with respect to these measurements, there is
no Kochen-Specker theorem for single systems in GNST
or GLT. Not only is it possible to assign definite outcomes to these measurements in a non-contextual fashion, but each such assignment is in fact an allowed state
of the theory. Nonetheless, both GNST and GLT exhibit
a different kind of contextuality, introduced by Spekkens
[43] and termed preparation contextuality. Readers are
referred to Ref. [43] for discussion of preparation contextuality. Given the definition, the proofs for GNST and
GLT are obvious.
VII.

INFORMATION PROCESSING

Using the results obtained for dynamics in GNST and
GLT, the information processing possibilities of each theory can be investigated. Rather than attempt something
like a general theory of information, this section contains

<!-- page 15 -->
15
remarks concerning some obvious tasks. Note that there
has already been some work investigating the information
processing properties of PR boxes, considered merely as
abstract correlations. van Dam has shown that they are
very powerful for communication complexity problems
[25], and this result has recently been extended to noisy
PR boxes in Ref. [26]. Others have claimed to show how
to do oblivious transfer [19] and bit commitment [21] using PR boxes. However, as pointed out in Ref. [20], the
fact that these latter works consider PR boxes only as
abstract correlations means that they make assumptions
that may not hold in any theory that allows PR boxes.12
In general, a theory with well defined dynamics is needed
before cryptography, or indeed other types of information processing, such as computation, can be discussed.
GNST is such a theory.
The first results concern teleportation and super-dense
coding (the quantum versions of these tasks were introduced in Refs. [44] and [45]). The natural analogue of
a quantum mechanical singlet in the GNST is a state
which, when fiducial measurements are performed, produces the PR box correlations:

11 

XY = 12 → P (a = 1, b = 1|XY ) =

21 
P (a = 2, b = 2|XY ) = 1/2,

XY = 22 → P (a = 1, b = 2|XY ) =
P (a = 2, b = 1|XY ) = 1/2.

It can be shown that these correlations represent a pure
state - that is a vertex of the polytope of states for two
gbits. Further, all vertices of this polytope are either
local deterministic correlations (product pure states) or
are equivalent to the PR box under local transformations
[18].
Theorem 11 It is impossible to teleport an unknown
gbit using a single shared PR box.
Proof. This follows easily from Theorem 10. In order
to teleport an unknown gbit, Alice must perform some
operation or sequence of operations on the gbit and her
half of the shared PR box. Without loss of generality,
whatever she does may be represented as a single joint
measurement, with m outcomes, on the two subsystems.
But this measurement can be represented as a convex
combination of procedures like that of Fig. 8. Such a
procedure will always begin, either by measuring X = 1
or X = 2 on the gbit, or by measuring the PR box. In
the former case, no information is gained about the value

12 One such assumption that as far as I know has not been pointed

out is that the shared boxes are trusted to behave like PR boxes
by both parties. But one may reasonably ask where did they
come from? By whom were they distributed?

for the other measurement on the gbit and teleportation
cannot possibly succeed on all pure states. In the latter
case, the shared PR box collapses into a product state
which cannot achieve teleportation.

Theorem 12 A single shared PR box cannot be used for
super-dense coding.
Proof. This follows from Theorems 7 and 10. Superdense coding would require that there are four different
operations that Alice can perform on her gbit such that,
when it is sent to Bob, he can determine unambiguously
which was performed by a joint measurement on the two
gbits now in his possession. It is easy to see that this is
not possible.

A.

Cryptography

Theorem 13 In GNST, key distribution is possible.
Proof. Key distribution can be achieved in GNST using
an Ekert-style protocol [46], in which Alice and Bob first
share n pairs of gbits, with each pair in the PR box state.
They then test some of their shared systems, to make
sure that they really are PR box states, i.e., that they
have not been disturbed en route by an eavesdropper.
Finally, they measure each remaining gbit pair, using the
fiducial measurements X = 1 and Y = 1. Assuming
that they share perfect PR box states, their measurement
outcomes will be perfectly correlated and can be used as
a secret key. This protocol is secure because PR box
states have a property of being monogamous, much as
the entanglement of a singlet is monogamous in quantum
theory. Thus consider a tripartite system shared between
Alice, Bob and Eve. If Alice’s and Bob’s reduced state is
the PR box state P~PAB
R , then the global state must be of
~ E . The outcome of any measurement
the form P~PAB
⊗
P
R
performed by Eve is uncorrelated with Alice’s and Bob’s
outcomes. The fact that the PR box correlations are
monogamous was shown in Ref. [18].

Recall Theorem 5, which implies that except for classical systems, there are pure states (lying in the same
subspace Vi ), which cannot be distinguished by nondisturbing operations. This motivates
Conjecture 1 In any non-classical theory, secure key
distribution is possible.
Finally,
Theorem 14 1-2 oblivious transfer can be implemented
securely in both GNST and GLT.
Proof.
In a 1-2 oblivious transfer (introduced in
Ref. [48]), Alice must submit 2 bits to Bob in such a
manner that Bob can choose to learn either one of the
bits or the other, but not both. There is also a security
requirement against Alice, who must not be able to learn

<!-- page 16 -->
16
which of the bits Bob chose. That this task is impossible to implement securely in quantum theory is shown in
Ref. [49]. To implement this task in GNST or GLT, Alice
sends a gbit to Bob, in a pure state, with the two bits
encoded in the outcomes for the X = 1 measurement and
the X = 2 measurement. Theorem 8 ensures that any
strategy employed by Bob is equivalent to his measuring
either X = 1 or X = 2, or to measuring X = 1 with some
probability p and X = 2 with probability 1 − p. Thus the
protocol is secure against Bob. That it is secure against
Alice follows from the fact that, by the no-signalling principle, she cannot determine which measurement Bob did.

In classical cryptography, it is known that 1-2 oblivious transfer is equivalent to oblivious transfer [50], and
that either can be used to implement arbitrary secure distributed computation [51]. In particular, either can be
used to implement bit commitment, hence coin tossing.
However, one cannot assume that the standard reductions of classical cryptography hold in a different theory such as GLT, GNST or quantum theory. Thus it is
open whether other two-party cryptographic tasks, such
as oblivious transfer, bit commitment or coin tossing, can
be implemented securely in GNST or GLT.
B.

Computation

For any of the theories in the framework, a natural
model of computation may be defined, based on the classical and quantum circuit models. I introduce this model
only informally. A particular circuit is assumed to act on
n systems, each of the same type, initially prepared in
a product state corresponding to the problem input. Instead of k-bit or k-qubit gates, there are transformations
that act jointly on k systems. At the end of the computation, the fiducial measurement X = 1 is performed on
each system in order to obtain the output. For a particular theory, it may not be the case that bipartite and
single system transformations together are universal, as
they are in classical and quantum theory. Thus transformations that act jointly on k systems for any k > 2 are
allowed. But for any circuit family Cn , there must exist
some finite k such that all transformations act on k systems or fewer. In addition, it may not be the case that
any particular type of system (such as a gbit) is universal
for computation in a given theory. So one should keep
in mind that circuits may act on other types of system.
Finally, in order to define a notion of polynomial time,
say, the usual caveats must be assumed. For example, it
should be possible for a classical Turing machine to output a description of the ith circuit in time polynomial in
i.
Theorem 15 In GLT, any computation can be simulated efficiently by a probabilistic classical computer.
Proof. In GLT, any allowed state of n systems can be
written as a convex combination of local deterministic,

or pure product, states, in which each system has a definite outcome for each fiducial measurement. A classical
simulation of the GLT computation works by storing,
at any given time, a local deterministic state of the n
systems. This requires an amount of memory linear in
n, rather than the exponential amount needed to store
a complete description of an arbitrary convex combination. An allowed transformation T , acting on k systems,
must take local deterministic states of the k systems to
other allowed states of GLT, which in turn are convex
combinations of local deterministic states:
T (P~ LD ) =

X

pi P~iLD ,

i

where superscript LD indicates a local deterministic
state. The classical computer simulating the GLT computation simply updates the stored state P~ LD to P~iLD
with probability pi . When the final X = 1 measurements are performed, the stored local deterministic state
will determine the classical computer’s output.

The computational power of GNST is at present unclear. But it is known that it is very powerful for communication complexity problems.
Theorem 16 In GNST, bipartite communication complexity problems require only constant communication,
provided the parties share sufficient PR boxes.
Recall that in a bipartite communication complexity scenario, two separated parties each receive an input, and
their task is to compute some joint function of their inputs. Their goal is to minimize the amount of communication. van Dam has shown that if the two parties
have a supply of shared PR boxes, then any communication complexity problem can be solved with only constant communication [25]. This result has recently been
strengthened: it continues to hold even if the shared PR
boxes are noisy, provided the amount of noise is not too
great [26]. Contrast the situation in quantum theory,
where the inner product problem is known to require n
bits of communication to be solved exactly, even with
unlimited shared singlets [52].
Finally,
Theorem 17 Super-quantum memory. In GNST, it is
possible to store a 2n -bit string in only n gbits. Although
the whole string cannot be recovered, it is possible to recover the ith bit without error.
Proof. Suppose that the ith bit of the 2n -bit string
we wish to store is given by f (i1 , . . . , in ) ∈ {0, 1},
where i1 . . . in is the binary representation of i. Let
X1 , . . . , Xn ∈ {0, 1} be fiducial measurements on the n
gbits and a1 , . . . , an ∈ {0, 1} the outcomes. (It is easier for this proof to let Xj and aj take values in {0, 1}
instead of in {1, 2} as elsewhere.) To store the string,

<!-- page 17 -->
17
prepare a state of n gbits such that
P (a1 , . . . , an |X1 , . . . , Xn ) =
(
1/2n−1
a1 ⊕ · · · ⊕ an = f (X1 , . . . , Xn )
,
0
otherwise
(24)
where ⊕ represents addition mod 2. In order to recover
the ith bit of the stored string, simply perform the measurement Xj = ij on each gbit and sum the outcomes
mod 2. One may check that the state of Eq. (24) is an
allowed state, since it is normalized and non-signalling.
Note that it is indeed impossible to store a 2n bit string
in only n qubits such that any bit may be recovered.
Bounds on quantum memory are derived in Ref. [53]. 
VIII.

DISCUSSION

A.

The framework

The framework introduced allows investigation of theories different from either quantum or classical theories.
The general idea is that quantum theory can be better
understood by viewing it in a context of different possibilities. More specific motivations include:
1. to understand the links between general physical
principles and information processing;

(Assumption 4), and the global state assumption (Assumption 5), both involving the manner in which separate systems combine to make joint systems. These imply
a tensor product rule.
One of the interesting things to emerge from the framework is that certain features, usually thought of as specifically quantum, are possessed by all theories except classical theories. These include the non-unique decomposition of mixed states into pure states, the existence of
sets of pure states that cannot be distinguished with nondisturbing operations, and the impossibility of even probabilistic universal cloning. Thus rather than regard quantum theory as special for having these features, a better
attitude may be to regard classical theories as special for
not having them.
How reasonable are Assumptions 4 and 5? Commutativity of local operations is arguably part of what it
means to talk about separate systems. In a theory where
it fails, any measurement or transformation is essentially
a measurement or transformation on all systems at once.
It is no longer obvious how to define a reasonable model
of computation - how should resources be counted? The
case for assuming the commutativity of local operations
is also strengthened by the fact that in a spacetime framework, it can be independently motivated by special relativity. It is slightly more difficult to regard the global
state assumption as independently compelling. Thus an
interesting direction in which to extend this work would
be to generalize the framework further by dropping this
assumption.

2. to stimulate the study of computation in models
that are more general than quantum theory;
3. to address Popescu’s and Rohrlich’s question of
why quantum theory does not allow the PR box
correlations;
4. to shed light on the interpretive problems of quantum theory by viewing those in a more general context;
5. to stimulate research into axioms for quantum theory.
As regards single systems the framework is very general indeed. It should be emphasized in particular that
linearity of transformations is not assumed, but is derived from the fact that the vector P~ is by definition
a complete description of the system.13 The most important requirements are that local operations commute

B.

The tensor product rule

It is interesting to compare the derivation of the tensor
product rule with that of Fuchs [15]. Without going into
too much detail, Fuchs assumes that local measurements
on two separate systems, A and B, are represented by
positive operator-valued measures on Hilbert spaces HA
and HB . He derives a Gleason-like theorem [55, 56, 57]
which states that the joint state of the two systems can be
represented by an operator on the tensor product Hilbert
space HA ⊗ HB , with joint probabilities for outcomes of
local measurements given by the standard trace rule.
As Fuchs acknowledges, the proof does not establish
that the operator describing the joint state has to be positive, but only that it has to be positive with respect to
local measurements. A consistent theory that is not ruled
out would allow the state to be negative with respect to
some joint measurements (the Bell basis measurement,
for example), but would not allow such measurements.

13 So

what of nonlinear modifications of quantum mechanics?
These modifications are nonlinear in the sense that they involve
a nonlinear Schrödinger equation. In this case, the usual density
matrix is no longer a complete description of a quantum system,
since the evolution of a system will in general depend not only
on the density matrix, but on the particular decomposition into
pure states (assuming a proper mixture). If the description of
the state is expanded until it is complete, then the action of the

dynamics on this new expanded state description will be linear.
But such a theory will in general violate one or more of the other
assumptions. A list of references on nonlinear quantum theories
is given in Ref. [54], and computation in this context is considered in Ref. [3].

<!-- page 18 -->
18
Furthermore, the assumption that local operations commute and the global state assumption are both implicit
in Fuchs’ analysis. Without the latter, the possibility
remains that there are extra degrees of freedom, not accessible via local measurements, that are not described
by an operator on the tensor product Hilbert space.
It follows that Fuchs’ conclusion is not stronger than
the tensor product rule derived in this paper. The latter
may be regarded as a generalization of Fuchs’ proof to the
case in which the subsystems A and B are not necessarily
quantum.

C.

Information theory, GNST and GLT

In addition to describing general properties of the
framework, I investigated in detail two particular theories, GNST and GLT. I focussed on the information
processing possibilities in these theories. One of the
most interesting things to have emerged is that there is
a trade-off between the states of a theory and the allowed dynamics. This arises for the simple reason that
an allowed transformation must take allowed states into
allowed states. Thus the dynamics of both GNST and
GLT is very simple for single systems. In GNST, a similar result holds for the simplest kind of bipartite system.
The surprising consequence is that GNST is less powerful than quantum theory in many ways, despite including
super-quantum correlations. For example, teleportation
and super-dense coding are impossible. It is already clear
that computation in GLT can be simulated efficiently
classically, while the computational power of GNST remains open. Another open question is whether secure bit
commitment is possible in either theory. Despite these
remarks, it is surprising how many features of quantum
theory have analogues in GNST. These obviously include
the generic features demonstrated in Section C, along
with entanglement and nonlocality. But they also include things I have not discussed in detail, such as the
distinction between sharp and unsharp measurements,
and preparation contextuality. (Other authors have also
found features of quantum theory reproduced in other
contexts. Masanes et al. [13] show that various features,
including a no-cloning theorem, are present in all theories that are nonlocal and non-signalling. Spekkens has
introduced a toy theory that contains a remarkably wide
range of quantum phenomena [11], although note that
this theory is not contained in our framework as it does
not allow arbitrary convex combinations of states.)
As mentioned above, one of the motivations of this
work is to stimulate the study of computation in models that are more general than quantum theory. Some
authors have already considered computation in nonstandard theories. However, these theories are often
modifications of quantum theory that appear to have
both unphysical consequences and immense computational power. It is suspected that quantum theory with
a nonlinear Schrödinger equation is very powerful, en-

abling the solution of NP-complete problems in polynomial time, for example.14 Aaronson has considered various modifications of quantum theory, including a model
that assumes the ability to postselect measurement outcomes, and a hidden variable model in which the history
of hidden states can be read out by the observer [5, 6].
Various authors have considered classical and quantum
computation in the presence of closed timelike curves
[7, 8]. Most recently, Aaronson and Watrous have shown
that BQP with closed timelike curves is equivalent to
PSPACE [9]. The framework introduced in this paper is
the natural place to investigate computation in theories
that are different from quantum theory, yet not obviously
physically unreasonable or immensely powerful. I suggest
that NP-complete problems cannot be solved efficiently
by any theory in the framework. I also raise the following
Conjecture 2 A quantum computer can simulate computation in any other theory in the framework with at
most polynomial overhead.
The intuition behind this is that quantum theory achieves
in some sense an optimal balance of allowed states and
dynamics.

D.

Interpretation

On the face of it, many theories that can be written
down in the present framework have similar interpretive
issues as quantum theory, if one tries to understand them
in a way that goes beyond the purely operational. Consider a universe in which some theory other than quantum or classical (GNST perhaps) is verified in laboratory
experiments. The denizens of such a universe would be
having debates in many ways similar to the debates that
surround quantum theory. Is a pure state better understood as a complete description of individual reality, as
representing an ensemble, or as representing the degrees
of belief of some agent?
Suppose that the inhabitants of this universe attempt
to extend the theory to include a description of the measuring apparatus, and of the interaction between system
and apparatus. This is always possible in classical and
quantum theory. In quantum theory, this fact is expressed in the idea that the Heisenberg cut can be moved
upwards indefinitely. Are classical and quantum theories
special in this regard, or can this be done in any theory?
Even when the inhabitants succeed in constructing a
measurement theory along these lines, it is plausible that
many theories will have a measurement problem. In these

14 In Ref. [3], it is claimed that nonlinear quantum theory can solve

NP-complete and even #P-complete problems efficiently. Aaronson complains [4] that in this particular case it is difficult to
evaluate whether exponential precision is required.

<!-- page 19 -->
19
theories, the system and apparatus are typically in some
entangled state after interaction. Some inhabitants may
suggest hidden variables or some kind of collapse dynamics. Does any theory admit an Everettian interpretation,
or is there a special feature of quantum theory that is
necessary for this to work?
I won’t discuss these issues any further. I have raised
them hoping that considering interpretive issues in a
framework more general than quantum theory might give
a new lease of life to the quantum debates.
E.

Axioms

Aside from Hardy’s derivation [14], what different ways
are there of uniquely identifying quantum theory from
the other theories in the framework by adding as few extra assumptions as possible? Several have pushed the
idea that a quantum state is best understood as a summary of an agent’s degrees of belief about the outcomes
of future measurements on a system [32, 58, 59]. From
this standpoint, Fuchs has argued that the formalism of
quantum theory should be understood as a constraint
on these degrees of belief, hopefully to be derived via a
small number of postulates, along with an argument that
any rational agent must accept [15]. Spekkens has also
argued for an epistemic constraint as a foundational principle for quantum theory, although for Spekkens, beliefs

15 Whether they succeed in deriving the full structure of quantum

theory is debatable. But they do establish the existence of non-

[1] Workshop titled What is Quantum in Quantum Computing? Konstanz, Germany, May 19-20, 2005.
[2] M. Troyer and U.-J. Wiese, Phys. Rev. Lett. 94, 170201
(2005).
[3] D. S. Abrams and S. Lloyd, Phys. Rev. Lett. 81, 3992
(1998).
[4] S. Aaronson, ACM SIGACT News, Vol. 36 , Issue 1
(March 2005), quant-ph/0502072.
[5] S. Aaronson, Phys. Rev. A 71, 032325 (2005).
[6] S. Aaronson, Proc. Roy. Soc. A 461, 3473 (2005).
[7] T. A. Brun, Found. Phys. Lett. 16, 245 (2003).
[8] D. Bacon, Phys. Rev. A 70, 032309 (2004).
[9] S. Aaronson and J. Watrous, in preparation.
[10] L. Hardy, quant-ph/9906123.
[11] R. W. Spekkens, quant-ph/0401052.
[12] J. A. Smolin, quant-ph/0310067.
[13] Ll. Masanes, A. Acin and N. Gisin, Phys. Rev. A 73,
012112 (2006).
[14] L. Hardy, quant-ph/0101012.
[15] C. A. Fuchs, quant-ph/0205039.
[16] L. A. Khalfi and B. S. Tsirelson, in Symposium on the
Foundations of Modern Physics, edited by P. Lahti and
P. Mittelstaedt (World Scientific, Singapore, 1985), pp.
441-460.
[17] S. Popescu and D. Rohrlich, Found. Phys. 24, 379 (1994).
[18] J. Barrett, N. Linden, S. Massar, S. Pironio, S. Popescu
and D. Roberts, Phys. Rev. A 71, 022101 (2005).

are about underlying ontic states of a system rather than
future measurement outcomes [11].
Clifton, Bub and Halvorson (CBH) have taken a different approach and derived at least part of quantum
theory from the assumption of (i) a no-signalling principle, (ii) a no-broadcasting principle, and (iii) the impossibility of secure bit commitment [60].15 CBH assume a C ∗ -algebraic framework, which is broad enough
to include classical theories and quantum theory, but is
not as broad as the framework presented here. An open
question is whether something like CBH’s proof would
go through in the broader framework, or whether there
is some theory (GNST perhaps) that satisfies (i)-(iii) and
is clearly not quantum.

Acknowledgments

Research at Perimeter Institute is supported in part by
the Government of Canada through NSERC and by the
Province of Ontario through MEDT. I should very much
like to thank Howard Barnum, Lucien Hardy, Nick Jones,
Matthew Leifer, Lluis Masanes, Stefano Pironio, Sandu
Popescu, Valerio Scarani, Tony Short, Rob Spekkens and
Alex Wilce for useful discussions.
Note added. Related independent work has appeared
recently in Ref. [62].
commuting measurements and of entanglement.

[19] S. Wolf and J. Wullschleger, in Proceedings of International Symposium on Information Theory (ISIT) 2005,
2005.
[20] A. J. Short, N. Gisin and S. Popescu, Quantum Inf. Proc.
5, 131 (2006).
[21] H. Buhrman, M. Christandl, F. Unger, S. Wehner and
A. Winter, Proc. R. Soc. A 462, 1919 (2006).
[22] A. Broadbent and A. A. Méthot, Theor. Comput. Sci.
358, 3 (2006).
[23] J. Barrett and S. Pironio, Phys. Rev. Lett. 95, 140401
(2005).
[24] N. S. Jones and L. Masanes, Phys. Rev. A 72, 052312
(2005).
[25] W. van Dam, quant-ph/0501159.
[26] G. Brassard, H. Buhrman, N. Linden, A. A. Méthot,
A. Tapp and F. Unger, Phys. Rev. Lett. 96, 250401
(2006).
[27] W. K. Wootters, Found. Phys. 16, 391 (1986).
[28] P. G. L. Mana, quant-ph/0305117.
[29] P. G. L. Mana, in A. Y. Khrennikov (ed.), Quantum Theory: Reconsideration of Foundations 2 (V axj o University Press, V axj o, 2004), e-print quant-ph/0403084.
[30] E. C. G. Stueckelberg, Helv. Phys. Acta 33, 727 (1960).
[31] W. K. Wootters, in Complexity, Entropy and the Physics
of Information, edited by W. H. Zurek (Addison-Wesley,
1990).
[32] C. M. Caves, C. A. Fuchs and R. Schack, J. Math. Phys.

<!-- page 20 -->
20
43, 4537 (2002).
[33] R. F. Werner, Phys. Rev. A 40, 4277 (1989).
[34] J. Barrett, Phys. Rev. A, 65, 042302 (2002).
[35] F. Clauser, M. A. Horne, A. Shimony and R. A. Holt,
Phys. Rev. Lett. 23, 880 (1969).
[36] B. S. Cirel’son, Lett. Math. Phys. 4, 93 (1980).
[37] H. Barnum, C. A. Fuchs, J. M. Renes and A. Wilce,
quant-ph/0507108.
[38] H. Barnum, J. Barrett and A. Wilce, unpublished.
[39] T. Rudolph, R. W. Spekkens and P. S. Turner, Phys.
Rev. A 68, 010301(R) (2003).
[40] H. Barnum, J. Barrett, M. Leifer and A. Wilce, forthcoming.
[41] J. Barrett and M. Leifer, forthcoming.
[42] J. Barrett, forthcoming.
[43] R. Spekkens, Phys. Rev. A 71, 052108 (2005).
[44] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa,
A. Peres and W. K. Wootters, Phys. Rev. Lett. 70, 1895
(1993).
[45] C. H. Bennett and S. J. Wiesner, Phys. Rev. Lett. 69,
2881 (1992).
[46] A. K. Ekert, Phys. Rev. Lett. 67, 661 (1991).
[47] C. H. Bennett and G. Brassard, in Proceedings of IEEE
International Conference on Computers, Systems and
Signal Processing (IEEE, 1984), p.175.
[48] S. Even, O. Goldreich and A. Lempel, in R. L. Rivest,
A. Sherman and D. Chaum (Eds.), Proceedings CRYPTO
82 (Plenum Press, New York, 1982), p.205.
[49] H.-K. Lo, Phys. Rev. A 56, 1154 (1997).
[50] G. Brassard, C. Crépeau and J.-M. Robert, in 27th
Symposium of Foundations of Computer Science (IEEE,
1986), p.168.
[51] J. Killian, in Proceedings of 20th ACM Symposium on
Theory of Computing (ACM, Chicago, 1988), p.20.
[52] R. Cleve, W. van Dam, M. Nielsen and A. Tapp, in
Proceedings of the first NASA International Conference
on Quantum Computing and Quantum Communication,
LNCS 1509 (Springer-Verlag, Heidelberg, 1998), p.61.
[53] A. Ambainis, A. Nayak, A. Ta-Shma and U. Vazirani,
quant-ph/9804043.
[54] G. Svetlichny, quant-ph/0410036.
[55] A. M. Gleason, J. Math. Mech. 6, 885 (1957).
[56] P. Busch, Phys. Rev. Lett. 91, 120403 (2003).
[57] C. M. Caves, C. A. Fuchs, K. Manne and J. M. Renes,
Found. Phys. 34, 193 (2004).
[58] C. M. Caves, C. A. Fuchs and R. Schack, Phys. Rev. A
65, 022305 (2002).
[59] C. M. Caves, C. A. Fuchs and R. Schack,
quant-ph/0608190.
[60] R. Clifton, J. Bub and H. Halvorson, Found. Phys. 33,
1561 (2003).
[61] A. Barvinok, A Course in Convexity, Graduate Studies in
Mathematics, Vol. 54 (American Mathematical Society,
Providence, Rhode Island, 2002).
[62] A. J. Short, S. Popescu and N. Gisin, Phys. Rev. A 73,
012101 (2006).

contained.
A transformation is a map from allowed states of a
system to allowed states. The map satisfies Eq.(7), reproduced here:
!
X
X
~
qi f (P~i )
qi Pi =
f
(A1)

i

i

∀Pi ∈ S, for 0 ≤ qi ≤ 1,

X

qi = 1.

i

The map should also satisfy
f (~0) = ~0.
(This follows from the interpretation of unnormalized
states. Recall that if a particular outcome i of some operation occurs with probability q < 1, then we associate
with that outcome an unnormalized vector P~ . Each entry of P~ gives the joint probability of obtaining outcome
i for the original operation, and outcome j for a fiducial
measurement performed immediately afterwards. Thus
if q = 0, it follows that the associated P~ = ~0. By definition, an entry in the vector f (~0) represents the joint
probability of getting the following outcomes in sequence:
outcome i for the original operation, then whatever outcome it is that corresponds to the transformation f , and
then outcome j for a fiducial measurement. But these
probabilities must all be zero if the probability of outcome i is zero.)
Writing the first of the above equations with i = 1, 2,
and setting P~2 = ~0, gives
f (q P~ ) = qf (P~ )

∀P~ ∈ S, for 0 ≤ q ≤ 1.

Suppose that P~ is a pure state ∈ S. Pure states are by
definition normalized. If r > 1, then f (rP~ ) is initially
undefined because rP~ ∈
/ S, so we are free to stipulate
that
f (rP~ ) = rf (P~ )

∀P~ ∈ S, r ≥ 0.

Define S+ as the set of all vectors that can be written in
the form rP~ with P~ ∈ S and r ≥ 0. It is a convex cone
[61]. Eq. (A1) can be extended slightly:
!
X
X
ri f (P~i )
∀Pi ∈ S+ for ri ≥ 0.
ri P~i =
f
i

i

(A2)

Now suppose that
P~ =

X

si P~i ,

(A3)

i

APPENDIX A: PROOF OF LINEARITY OF
TRANSFORMATIONS

The proof in this appendix is adapted from that of
Hardy in Ref. [14]. It is included to keep this work self-

where P~ , P~i ∈ S+ , and the si are real. Let i ∈ A− if
si < 0 and i ∈ A+ if si ≥ 0. Rewrite Eq. (A3) as
X
X
P~ +
|si |P~i =
si P~i .
i∈A−

i∈A+

<!-- page 21 -->
21
Each side is a conic combination of vectors in S+ , thus
Eq. (A2) applies, and rearranging we get
X
si f (P~i ).
f (P~ ) =
i

~ ∈
~ can be defined
Finally, for any vector Q
/ S+ , f (Q)
~
uniquely by linear extension if Q lies in the subspace
spanned by S. The action of f on the rest of the vector
space is arbitrary but may be defined to be linear.

APPENDIX B: DERIVATION OF TENSOR
PRODUCT RULE

As discussed in the main text, the state of a joint system AB can be written


P (a = 1, b = 1|X = 1, Y = 1)
 P (a = 1, b = 2|X = 1, Y = 1) 




..


.




AB
~

.
P
(a
=
1,
b
=
1|X
=
1,
Y
=
2)
P
≡

 P (a = 1, b = 2|X = 1, Y = 2) 




..


.


..
.

Proof of Theorem 1. This theorem is trivial. Let
P~ AB ∈ V AB , P~ A ∈ V A and P~ B ∈ V B . Define the vector
~ AB as the vector with a 1 for the entry corresponding to
Q
ijkl
the joint outcome ij of the joint fiducial measurement kl,
~B
and 0s elsewhere. Similarly ~
QA
ik and Qjl . Now identify
~ AB with Q
~A ⊗ Q
~ B and extend linearly.
Q

ijkl
ik
jl
Proof of Theorem 2. Consider a joint system AB. For
each of the fiducial measurements that define the state
of system B, there must be at least one operation on
the joint system AB that corresponds to performing that
measurement. Let this operation for the jth fiducial measurement be characterized by the set of matrices {Mij },
where there is a value of i for each outcome and j is
fixed. When the transformation Mij acts on AB, the resulting state is the unnormalized state P~ijAB ∈ S AB . The
corresponding reduced state for A is the unnormalized
state P~ijA . By Constraint 2, P~ijA ∈ S A . If a fiducial measurement is now performed on A, the state P~ijA gives the
(unnormalized) probabilities for the different outcomes.
It follows that P~ AB can be written in the form
X
~B
P~ijA ⊗ Q
(B1)
P~ AB =
ij ,

in the subspace of V AB that is spanned by vectors from
S A ⊗ S B . Eq. (19) follows. The vectors on the right
hand side of this equation can be assumed normalized,
since any multiplying factor can be subsumed into the
corresponding ri . They can be assumed pure, since a
mixed state can always be expressed as a convex combination of pure states and ~0. But any term with ~0 will not
contribute. Theorem 2 follows.

Proof of Theorem 3. Consider a joint system AB and a
transformation T A of system A alone. T A corresponds to
a matrix M A such that P~ A → P~ ′A = M A .P~ A . The aim
is to determine the effect of this transformation on the
joint state P~ AB . From Section II A, this will correspond
to a matrix M̃ A such that P~ AB → P~ ′AB = M̃ A .P~ AB .
But what is the relation between M A and M̃ A ?
Consider the following procedure. First, the transformation T A is applied. Then fiducial measurements are
performed on systems A and B. The (unnormalized)
joint probabilities for the outcomes of these measurements are then the entries of the vector P~ ′AB . However,
by Assumption 4, the ordering of operations on systems
A and B does not matter. Thus the following procedure
is equivalent. First, a fiducial measurement is performed
on system B. Note that the reduced state of system A
conditioned on a particular outcome for this measurement is defined by the vector P~ AB . Next, the transformation T A is performed on system A. Finally, a fiducial
measurement is performed on system A.
In the second procedure, we know how to apply the
transformation T A , since it is enough to consider its action on system A alone, and we know that P~ A → P~ ′A =
M A .P~ A . We obtain
X
′AB
P~ijkl
=
(M A )ik;i′ k′ P~iAB
′ jk′ l
i′ k′

=

X

(M A )ik;i′ k′ δjj ′ δll′ P~iAB
′ j ′ k ′ l′ .

i′ k′ j ′ l′

But
(M A ⊗ I B )ijkl;i′ j ′ k′ l′ = (M A )ik;i′ k′ δjj ′ δll′ ,
thus
P~ ′AB = (M A ⊗ I)P~ AB .
This holds for all P~ AB ∈ S AB , and the action of T A on
vectors P~ AB ∈
/ S AB is arbitrary. It follows that we lose
no generality in identifying
M̃ A = M A ⊗ I B .

ij

~ B as above. Now consider a vector
with P~ijA ∈ S A and Q
ij
AB
~ ⊗ ~
~ ⊥ S A , where this
U
W ∈V
, with ~
W ∈ S B but U
~ is orthogonal to all vectors in S A . From
means that U
~ ⊗W
~ ).P~ AB = 0. A similar
Eq.(B1) it follows that (U
B
~
~
result holds if W ⊥ S and U ∈ S A . Thus P~ AB lies


APPENDIX C: GENERIC FEATURES

This appendix contains proofs of the results of Section V.

<!-- page 22 -->
22
Proof of Theorem 4. Consider a particular type of system in some theory. Suppose that the subspace spanned
by allowed states of the system has dimension d and that
every mixed state has a unique decomposition into pure
states and ~0. The only convex set with this property is a
simplex with d + 1 vertices. One of these vertices is the
state ~0. It is always possible to find an invertible linear
transformation N such that the other vertices are transformed into the vectors (1, 0, 0, . . . , 0), (0, 1, 0, . . . , 0), and
so on. Recall from Section III that if this transformation
acts on the set S, then the theory is not changed, since
~T → R
~ T .N −1 and M → N.M.N −1 for measurements
R
and transformations. Hence the system is classical. 
Proof of Theorem 5. Consider a system with a set
of allowed states S, spanning VS , and let d be the dimension of VS . Choose a set of d distinct pure states
{P~1 , . . . , P~d } that are linearly independent and collectively span VS . Suppose that a particular transformation
is non-disturbing. Its action on each of the P~i is given
by M.P~i = ci P~i with 0 ≤ ci ≤ 1. If the system is classical, then S is a simplex and the set {P~1 , . . . , P~d } must
contain all the pure states. Since the P~i are linearly independent, the ci can be chosen independently without
contradiction. For any other type of system, there are at
~ that is
least d + 1 pure states. Consider a pure state Q
~
~
not contained in the set {P1 , . . . , Pd }. If the transforma~ = eQ
~ with 0 ≤ e ≤ 1.
tion is non-disturbing, then M.Q
~ has a unique deSince {P~1 , . . . , P~d } is a basis for VS , Q
~ = P di P~i , where at least two
composition of the form Q
i
of the di are non-zero. If dj and dk are non-zero, then
cj = ck = e. Thus M acts as e times the identity on the
subspace of VS spanned by P~j and P~k . By repeating this
reasoning for every pure state ~
Q, the set {P~1 , . . . , P~d }
can be divided into subsets such that (i) if P~j and P~k are
in the same subset, then cj = ck for any non-disturbing
transformation, and (ii) if P~j and P~k are in different sub~ such that both dj and
sets then there is no pure state Q
dk are non-zero. Each subset defines a subspace Vi of VS
and the theorem follows.




′





P (a = 1|X = 1)

 

.
..
 

 

 P ′ (a = k|X = 1)  
 

 

..
=

.
 

 
 ′
 P (a = 1|X = n)  
 

 

..
 

.


P ′ (a = k|X = n)

M11

Proof of Theorem 6. Theorem 6 is proven using Theorem 5. We show that if there is a probabilistic universal
cloning procedure, then for any two pure states P~1 and
P~2 , there is a non-disturbing transformation M ′ such that
|M ′ .P~1 | 6= |M ′ .P~2 |. This in turn implies that the system
is classical.
~ and a transSuppose that there is a standard state Q
formation M such that for each pure state P~ , M (P~ ⊗
~ = cP~ ⊗ P~ . The number c may vary with P~ but is > 0
Q)
for all P~ . Consider a procedure in which a system is in
the state P~1 or P~2 , an ancilla is added in the standard
~ and the cloning operation {M, F } performed on
state Q,
the joint system. The transformation M corresponds to
the success outcome and F to the fail outcome. If P~1
and P~2 are different states there must be some operation
{N1 , N2 } such that |N1 .P~1 | 6= |N1 .P~2 |. If cloning succeeded, perform this operation on the ancilla. Output
the result and throw away the ancilla.
This entire procedure may be regarded as an operation
on the system alone (see the remarks following Assumption 7). It can be written O′ = {M1′ , M2′ , F ′ }, where M1′
corresponds to successful cloning followed by the N1 outcome, M2′ corresponds to successful cloning followed by
the N2 outcome, and F ′ corresponds to failed cloning.
By construction, each of M1′ and M2′ is non-disturbing
and |Mi′ .P~1 | 6= |Mi′ .P~2 | for at least one of i = 1, 2.
L
Recalling Theorem 5, it follows that VS = i Vi , with
each Vi containing only one pure state, hence the system
is classical.


APPENDIX D: DYNAMICS IN GNST AND GLT

This appendix contains proofs of Theorems 7, 8 and 9,
all of which concern dynamics in GNST or GLT.
Proof of Theorem 7. This theorem concerns transformations of single systems in either GNST or GLT. A
transformation of an (n, k) system can be written

···

..
.

Mn1

The transformation matrix is M , an nk × nk matrix. If

M1n

..
.

···

Mnn





 P (a = 1|X = 1)


..



.


  P (a = k|X = 1) 




..
.

.


  P (a = 1|X = n) 





..


.


P (a = k|X = n)

(D1)

the fiducial measurement X = 1 has k outcomes, then

<!-- page 23 -->
23
the top k rows of this matrix determine the probabilities
of outcomes when the X = 1 measurement is performed
on the transformed state P~ ′ . Denote the k × nk submatrix consisting of these rows M1 . The next k rows are
associated with the fiducial measurement X = 2, so denote the corresponding submatrix by M2 , and so on. The
first k columns of Mi multiply into those components of
P~ that correspond to the fiducial measurement X = 1 being performed. Denote the k × k subsubmatrix consisting
of these columns Mi1 . Similarly Mi2 , and so on. Note
~ must repthat each row in M , considered as a vector R,
resent a possible yes/no measurement. This is because if
~ P~ gives the
the transformation acts on a state P~ , then R.
corresponding entry in the transformed state P~ ′ , which
must be between 0 and 1 for all P~ ∈ S. Furthermore,
when the transformation is normalization-preserving, the
~ ~
~ j from a particular Mi satisfy P R
rows R
j j .P = 1, whenever P~ is normalized. Hence the rows from a particular
Mi correspond to a multiple-outcome measurement. One
way of performing this measurement is simply to perform
the transformation M first, and then to perform fiducial
measurement X = i.
~
There is some redundancy in a measurement vector R,
′ ~
~
~
~
~
~
and in the matrix M . If R.P = R .P ∀P ∈ S, then R
′
~ represent the same measurement. In particular,
and R
~′ = R
~+ ~
~ and R
~′
if R
C, where ~
C.P~ = 0 ∀P~ ∈ S, then R
represent the same measurement. An example of such a
~ is
C
~ = (1, . . . , 1| − 1, . . . , −1|0, . . . , 0| . . .),
C
~ P~ = 0 ∀P~ ∈ S is ensured by the normalization
where C.
~
~
of P . The first step in the proof is to show that any R
′
~
is equivalent in this sense to an R with all components
≥ 0.
For this, consider the set of allowed normalized states.
This is precisely the set of vectors satisfying the conditions
X
X
P (a = i|X = k) ∀j, k, (D2)
P (a = i|X = j) =
i

i

X

P (a = i|X = j) ≥ 0

P (a = i|X = 1) = 1.

∀i, j,

(D3)

(D4)

i

Define S+ as the set of vectors of the form rP~ , with r ≥ 0
and P~ ∈ S, and note that in the case of GNST or GLT,
S+ is a polyhedral cone [61]. It can also be defined as the
set of vectors satisfying conditions (D2) and (D3). The
defining inequalities (D3) can each be written in the form
~ i .P~ ≥ 0, where C
~ i is a constant vector with a 1 in the
C
ith position and 0s elsewhere. The equalities (D2) can
each be written as the conjunction of two inequalities:
~ j .P~ ≥ 0 and D
~ j .P~ ≤ 0 for some constant Dj . Define
D
~ such that R.
~ P~ ≥ 0 ∀P~ ∈ S+ .
R+ as the set of vectors R
This is the set of unnormalized measurements and is the

dual cone to S+ . It can be shown that if a polyhedral
~ i .P~ ≥ 0 ∀i}, then the dual cone
cone is defined by {P~ : A
~ i . Thus elements
is equal to the conic hull of the vectors A
of R+ can be written
~ =
R

X

~i +
λi C

X

~ j,
µj D

(D5)

j

i

where λi ≥ 0 and µj can be positive or negative. Finally,
~j all satisfy ~
the vectors D
Dj .P~ = 0 ∀P~ ∈ S+ . Hence any
~
~ of the form
R of this form is equivalent to an R
X
~i,
~ =
(D6)
λi C
R
i

~ can
and without loss of generality, the components of R
~ considered as a
be assumed ≥ 0. This applies both to R
~ considered as a row of a transformeasurement and to R
mation matrix M .
Assume, then, that M is written in a form with all entries ≥ 0. To conclude the proof, note that M acting on
any properly normalized state (satisfying both Eqs. (D2)
and Eq. (D4)) must result in a state that is also properly normalized. This implies the following. Consider the
matrix Mij . Denote the sum of the elements in the first
column by S1ij , the sum of the elements in the second
column by S2ij , and so on. Then S1ij = S2ij = · · · = Skij
P
and j S1ij = 1. Hence the matrix Mij is of the form
α
Pij times a stochastic matrix, with 0 ≤ αij ≤ 1 and
j αij = 1. One may easily check that any transformation that is equivalent to a procedure of the form of Fig. 5
is represented by a matrix of this form with αik = 1 for
some k and αij = 0 for j 6= k. Hence we have obtained
the general result that any allowed M is a convex combination of transformations of the form of Fig. 5.

Proof of Theorem 8. Let an m-outcome measurement on an (n, k) system have outcomes corresponding
~ 1, . . . , R
~ m , and construct the m × nk matrix
to R

~ 1T
R


N =  ...  .


~T
R
m

Denote the submatrix consisting of the first k columns
of N by N1 , that consisting of the next k columns by
N2 , and so on. The same arguments as in the proof of
Theorem 7 can be used to establish that N can be chosen
such
P that all entries are ≥ 0. Then use the fact that
~ ~
~
i Ri .P = 1 for normalized P , and arguments similar
to those in the proof of Theorem
7, to establish that
P
Ni = αi Si for 0 ≤ αi ≤ 1, i αi = 1, and Si stochastic.
The theorem follows.

Proof of Theorem 9. Begin as before by showing that
without loss of generality, the matrix M can be taken
to have all entries ≥ 0. This part of the proof is identical, except that to conditions (D2), (D3) and (D4), one

<!-- page 24 -->
24
should add the no-signalling constraints
X
P (a = i, b = j|X = k, Y = 1) =
j

X
j

X

P (a = i, b = j|X = k, Y = 2) ∀i, k

(D7)

P (a = i, b = j|X = 1, Y = l) =

i

X
i

P (a = i, b = j|X = 2, Y = l) ∀j, l.

(D8)

Like the conditions (D2), these constraints can be writ~
ten as the conjunction ~
Dj .P~ ≥ 0 and ~
Dj .P~ ≤ 0, and R
can be written in the form of Eq. (D5), hence in the form
of Eq.(D6). Now impose that P~ ′ = M.P~ is normalized
for any allowed normalized P~ , that is any P~ that satisfies conditions (D2), (D3), (D4), (D7), and (D8). Proving that any such M represents a convex combination
of transformations of the form of Fig. 7 (or the reversed
form with respect to the two subsystems) is a tedious
brute force exercise that is omitted. As with Theorem 8,
the proof of Theorem 10 is a straightforward variation.
