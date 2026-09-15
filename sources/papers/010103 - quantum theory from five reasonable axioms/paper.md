---
type: paper
date: 2001-01-03
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:quant-ph/0101012v4)
reviewed: false
---

# Quantum Theory From Five Reasonable Axioms

Machine-generated and unreviewed text extraction of arXiv:quant-ph/0101012v4
(35 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/quant-ph/0101012v4>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
arXiv:quant-ph/0101012v4 25 Sep 2001

Quantum Theory From Five Reasonable Axioms
Lucien Hardy∗
Centre for Quantum Computation,
The Clarendon Laboratory,
Parks road, Oxford OX1 3PU, UK
November 26, 2024

Abstract

theory is simply a new type of probability theory.
Like classical probability theory it can be applied
to a wide range of phenomena. However, the rules
of classical probability theory can be determined by
pure thought alone without any particular appeal to
experiment (though, of course, to develop classical
probability theory, we do employ some basic intuitions about the nature of the world). Is the same
true of quantum theory? Put another way, could a
19th century theorist have developed quantum theory without access to the empirical data that later
became available to his 20th century descendants?
In this paper it will be shown that quantum theory
follows from five very reasonable axioms which might
well have been posited without any particular access
to empirical data. We will not recover any specific
form of the Hamiltonian from the axioms since that
belongs to particular applications of quantum theory (for example - a set of interacting spins or the
motion of a particle in one dimension). Rather we
will recover the basic structure of quantum theory
along with the most general type of quantum evolution possible. In addition we will only deal with
the case where there are a finite or countably infinite
number of distinguishable states corresponding to a
finite or countably infinite dimensional Hilbert space.
We will not deal with continuous dimensional Hilbert
spaces.

The usual formulation of quantum theory is based on
rather obscure axioms (employing complex Hilbert
spaces, Hermitean operators, and the trace formula
for calculating probabilities). In this paper it is
shown that quantum theory can be derived from five
very reasonable axioms. The first four of these axioms are obviously consistent with both quantum theory and classical probability theory. Axiom 5 (which
requires that there exist continuous reversible transformations between pure states) rules out classical
probability theory. If Axiom 5 (or even just the word
“continuous” from Axiom 5) is dropped then we obtain classical probability theory instead. This work
provides some insight into the reasons why quantum
theory is the way it is. For example, it explains the
need for complex numbers and where the trace formula comes from. We also gain insight into the relationship between quantum theory and classical probability theory.

1

Introduction

Quantum theory, in its usual formulation, is very abstract. The basic elements are vectors in a complex
Hilbert space. These determine measured probabilities by means of the well known trace formula - a
The basic setting we will consider is one in which
formula which has no obvious origin. It is natural to
we have preparation devices, transformation devices,
ask why quantum theory is the way it is. Quantum
and measurement devices. Associated with each
∗ hardy@qubit.org. This is version 4
preparation will be a state defined in the following
1

<!-- page 2 -->
way:

Axiom 2 Simplicity. K is determined by a function
of N (i.e. K = K(N )) where N = 1, 2, . . . and
The state associated with a particular preparation
where, for each given N , K takes the minimum
is defined to be (that thing represented by) any
value consistent with the axioms.
mathematical object that can be used to determine the probability associated with the out- Axiom 3 Subspaces. A system whose state is concomes of any measurement that may be perstrained to belong to an M dimensional subspace
formed on a system prepared by the given prepa(i.e. have support on only M of a set of N possiration.
ble distinguishable states) behaves like a system
of dimension M .

Hence, a list of all probabilities pertaining to all possible measurements that could be made would certainly represent the state. However, this would most
likely over determine the state. Since most physical
theories have some structure, a smaller set of probabilities pertaining to a set of carefully chosen measurements may be sufficient to determine the state.
This is the case in classical probability theory and
quantum theory. Central to the axioms are two integers K and N which characterize the type of system
being considered.

Axiom 4 Composite systems. A composite system
consisting of subsystems A and B satisfies N =
NA NB and K = KA KB
Axiom 5 Continuity. There exists a continuous reversible transformation on a system between any
two pure states of that system.
The first four axioms are consistent with classical
probability theory but the fifth is not (unless the
word “continuous” is dropped). If the last axiom is
dropped then, because of the simplicity axiom, we
obtain classical probability theory (with K = N ) instead of quantum theory (with K = N 2 ). It is very
striking that we have here a set of axioms for quantum theory which have the property that if a single
word is removed – namely the word “continuous” in
Axiom 5 – then we obtain classical probability theory
instead.
The basic idea of the proof is simple. First we show
how the state can be described by a real vector, p,
whose entries are probabilities and that the probability associated with an arbitrary measurement is given
by a linear function, r · p, of this vector (the vector r
is associated with the measurement). Then we show
that we must have K = N r where r is a positive integer and that it follows from the simplicity axiom
that r = 2 (the r = 1 case being ruled out by Axiom
5). We consider the N = 2, K = 4 case and recover
quantum theory for a two dimensional Hilbert space.
The subspace axiom is then used to construct quantum theory for general N . We also obtain the most
general evolution of the state consistent with the axioms and show that the state of a composite system
can be represented by a positive operator on the tensor product of the Hilbert spaces of the subsystems.

• The number of degrees of freedom, K, is defined
as the minimum number of probability measurements needed to determine the state, or, more
roughly, as the number of real parameters required to specify the state.
• The dimension, N , is defined as the maximum
number of states that can be reliably distinguished from one another in a single shot measurement.
We will only consider the case where the number
of distinguishable states is finite or countably infinite. As will be shown below, classical probability
theory has K = N and quantum probability theory
has K = N 2 (note we do not assume that states are
normalized).
The five axioms for quantum theory (to be stated
again, in context, later) are
Axiom 1 Probabilities. Relative frequencies (measured by taking the proportion of times a particular outcome is observed) tend to the same
value (which we call the probability) for any case
where a given measurement is performed on a
ensemble of n systems prepared by some given
preparation in the limit as n becomes infinite.
2

<!-- page 3 -->
Finally, we show obtain the rules for updating the
state after a measurement.
This paper is organized in the following way.
First we will describe the type of situation we wish
to consider (in which we have preparation devices,
state transforming devices, and measurement devices). Then we will describe classical probability
theory and quantum theory. In particular it will be
shown how quantum theory can be put in a form similar to classical probability theory. After that we will
forget both classical and quantum probability theory
and show how they can be obtained from the axioms.
Various authors have set up axiomatic formulations of quantum theory, for example see references
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (see also [11, 12, 13]).
Much of this work is in the quantum logic tradition.
The advantage of the present work is that there are
a small number of simple axioms, these axioms can
easily be motivated without any particular appeal to
experiment, and the mathematical methods required
to obtain quantum theory from these axioms are very
straightforward (essentially just linear algebra).

2

because the button on the preparation device was
not pressed) then it outputs a 0 (corresponding to a
null outcome). If there is actually a physical system
incident (i.e when the release button is pressed and
the transforming device has not absorbed the system)
then the device outputs a number l where l = 1 to L
(we will call these non-null outcomes). The number
of possible classical outputs, L, may depend on what
is being measured (the settings of the knobs).
The fact that we allow null events means that we
will not impose the constraint that states are normalized. This turns out to be a useful convention.
It may appear that requiring the existence of null
events is an additional assumption. However, it follows from the subspace axiom that we can arrange to
have a null outcome. We can associate the non-null
outcomes with a certain subspace and the null outcome with the complement subspace. Then we can
restrict ourselves to preparing only mixtures of states
which are in the non-null subspace (when the button
is pressed) with states which are in the null subspace
(when the button is not pressed).
The situation described here is quite generic. Although we have described the set up as if the system
were moving along one dimension, in fact the system
could equally well be regarded as remaining stationary whilst being subjected to transformations and
measurements. Furthermore, the system need not be
localized but could be in several locations. The transformations could be due to controlling fields or simply
due to the natural evolution of the system. Any physical experiment, quantum, classical or other, can be
viewed as an experiment of the type described here.

Setting the Scene

We will begin by describing the type of experimental situation we wish to consider (see Fig. 1). An
experimentalist has three types of device. One is a
preparation device. We can think of it as preparing
physical systems in some state. It has on it a number of knobs which can be varied to change the state
prepared. The system is released by pressing a button. The system passes through the second device.
This device can transform the state of the system.
This device has knobs on it which can be adjusted
to effect different transformations (we might think of
these as controlling fields which effect the system).
We can allow the system to pass through a number
of devices of this type. Unless otherwise stated, we
will assume the transformation devices are set to allow the system through unchanged. Finally, we have
a measurement apparatus. This also has knobs on it
which can be adjusted to determine what measurement is being made. This device outputs a classical
number. If no system is incident on the device (i.e.

3

Probability measurements

We will consider only measurements of probability
since all other measurements (such as expectation
values) can be calculated from measurements of probability. When, in this paper, we refer to a measurement or a probability measurement we mean, specifically, a measurement of the probability that the outcome belongs to some subset of the non-null outcomes
with a given setting of the knob on the measurement
apparatus. For example, we could measure the prob3

<!-- page 4 -->
Release button
Knob

System

Classical
information
out

Preparation

Transformation

Measurement

Figure 1: The situation considered consists of a preparation device with a knob for varying the state of the
system produced and a release button for releasing the system, a transformation device for transforming the
state (and a knob to vary this transformation), and a measuring apparatus for measuring the state (with a
knob to vary what is measured) which outputs a classical number.
ability that the outcome is l = 1 or l = 2 with some a measurement. We can write
given setting.
 
p1
To perform a measurement we need a large number
 p2 
 
of identically prepared systems.
 
p =  p3 
(1)
 .. 
A measurement returns a single real number (the
 . 
probability) between 0 and 1. It is possible to perpN
form many measurements at once. For example, we
could simultaneously measure [the probability the This vector can be regarded as describing the state
outcome is l = 1] and [the probability the outcome is of the system. It can be determined by measuring
l = 1 or l = 2] with a given knob setting.
N probabilities and so K = N . Note that we do
not assume that the state is normalized (otherwise
we would have K = N − 1).
The state p will belong to a convex set S. Since the
set is convex it will have a subset of extremal states.
4 Classical Probability Theory These are the states
 
 
 
1
0
0
0
1
0
A classical system will have available to it a number,
 
 
 

 
 
N , of distinguishable states. For example, we could p = 
p2 = 0
p3 = 1
etc.
0
1




 .. 
.
.
consider a ball that can be in one of N boxes. We
 .. 
 .. 
.
will call these distinguishable states the basis states.
0
0
0
Associated with each basis state will be the probabil(2)
ity, pn , of finding the system in that state if we make
4

<!-- page 5 -->
There must exist a measurement in which we simply check to see that the system is present (i.e. not
in the null state). We denote this by rI . Clearly
 
1
(3)
1
 
X
 
(5)
rI =
rn = 1
 .. 
n
.
The state 0 is the null state (when the system is not
1
present). We define the set of pure states to consist of
all extremal states except the null state. Hence, the Hence 0 ≤ rI .p ≤ 1 with normalized states saturatstates in (2) are the pure states. They correspond to ing the upper bound.
the system definitely being in one of the N distinWith a given setting of the knob on the measureguishable states. A general state can be written as ment device there will be a certain number of distinct
a convex sum of the pure states and the null state non-null outcomes labeled l = 1 to L. Associated
and this gives us the exact form of the set S. This is with each outcome will be a measurement vector rl .
always a polytope (a shape having flat surfaces and Since, for normalized states, one non-null outcome
a finite number of vertices).
must happen we have
We will now consider measurements. Consider a
L
X
measurement of the probability that the system is in
rl = rI
(6)
the basis state n. Associated with this probability
and the state

 
0
0
 
 
pnull = 0 = 0
 .. 
.
0

l=1
measurement is the vector rn having a 1 in position
n and 0’s elsewhere. At least for these cases the mea- This equation imposes a constraint on any measuresured probability is given by
ment vector. Let allowed measurement vectors r belong to the set R. This set is clearly convex (by virtue
pmeas = r · p
(4)
of 1. above). To fully determine R first consider the
set R+ consisting of all vectors which can be written
However, we can consider more general types of probas a sum of the basis measurement vectors, rn , each
ability measurement and this formula will still hold.
multiplied by a positive number. For such vectors
There are two ways in which we can construct more
r · p is necessarily greater than 0 but may also be
general types of measurement:
greater than 1. Thus, elements of R+ may be too
1. We can perform a measurement in which we long to belong to R. We need a way of picking out
+
decide with probability λ to measure rA and those elements of R that also belong to R. If we
with probability 1 − λ to measure rB . Then can perform the probability measurement r then, by
we will obtain a new measurement vector r = (6) we can also perform the probability measurement
r ≡ rI − r. Hence,
λrA + (1 − λ)rB .

Iff

2. We can add the results of two compatible probability measurements and therefore add the corresponding measurement vectors.

r, r ∈ R+

and r + r = rI

then r, r ∈ R
(7)

This works since it implies that r · p ≤ 1 for all p so
that r is not too long.
Note that the Axioms 1 to 4 are satisfied but Axiom
5 is not since there are a finite number of pure states.
It is easy to show that reversible transformations take
pure states to pure states (see Section 7). Hence a

An example of the second is the probability measurement that the state is basis state 1 or basis state 2 is
given by the measurement vector r1 + r2 . From linearity, it is clear that the formula (4) holds for such
more general measurements.
5

<!-- page 6 -->
continuous reversible transformation will take a pure
state along a continuous path through the pure states
which is impossible here since there are only a finite
number of pure states.

5

2. The most general type of measurement in quantum theory is a POVM (positive operator valued
measure). The operator Â is an element of such
a measure.
3. Two classes of superoperator are of particular
interest. If $ is reversible (i.e. the inverse $−1
both exists and belongs to the allowed set of
transformations) then it will take pure states
to pure states and corresponds to unitary evolution. The von Neumann projection postulate
takes the state ρ̂ to the state P̂ ρ̂P̂ when the outcome corresponds to the projection operator P̂ .
This is a special case of a superoperator evolution in which the trace of ρ̂ decreases.

Quantum Theory

Quantum theory can be summarized by the following
rules
States The state is represented by a positive (and
therefore Hermitean) operator ρ̂ satisfying 0 ≤
tr(ρ̂) ≤ 1.
Measurements Probability measurements are represented by a positive operator Â. If Âl corresponds to outcome l where l = 1 to L then
L
X

Âl = Iˆ

4. It has been shown by Krauss [14] that one need
only impose the three listed constraints on $ to
fully constrain the possible types of quantum
evolution. This includes unitary evolution and
von Neumann projection as already stated, and
it also includes the evolution of an open system
(interacting with an environment). It is sometimes stated that the superoperator should preserve the trace. However, this is an unnecessary
constraint which makes it impossible to use the
superoperator formalism to describe von Neumann projection [15].

(8)

l=1

Probability formula The probability obtained
when the measurement Â is made on the state
ρ̂ is
pmeas = tr(Âρ̂)

(9)

Evolution The most general evolution is given by
the superoperator $
ρ̂ → $(ρ)

5. The constraint that $ is completely positive imposes not only that $ preserves the positivity of
ρ̂ but also that $A ⊗ IˆB acting on any element of
a tensor product space also preserves positivity
for any dimension of B.

(10)

where $
• Does not increase the trace.

This is the usual formulation. However, quantum
theory can be recast in a form more similar to classical probability theory. To do this we note first that
the space of Hermitean operators which act on a N
dimensional complex Hilbert space can be spanned
by N 2 linearly independent projection operators P̂k
for k = 1 to K = N 2 . This is clear since a general
Hermitean operator can be represented as a matrix.
This matrix has N real numbers along the diagonal
and 12 N (N − 1) complex numbers above the diagonal making a total of N 2 real numbers. An example
of N 2 such projection operators will be given later.

• Is linear.

• Is completely positive.
This way of presenting quantum theory is rather condensed. The following notes should provide some
clarifications
1. It is, again, more convenient not to impose normalization. This, in any case, more accurately
models what happens in real experiments when
the quantum system is often missing for some
portion of the ensemble.
6

<!-- page 7 -->
or we can write D = tr(P̂P̂T ). From (14,17) we
obtain

Define



P̂1
 P̂2 
 
P̂ =  . 
 .. 

(11)

pmeas = rM · pS

(14)

pS = DrS

(19)

and

P̂K

pM = DT rM
(20)
Any Hermitean matrix can be written as a sum of
these projection operators times real numbers, i.e. in We also note that
the form a·P̂ where a is a real vector (a is unique since
the operators P̂k are linearly independent). Now deD = DT
(21)
fine
though this would not be the case had we chosen difpS = tr(P̂ρ̂)
(12) ferent spanning sets of projection operators for the
state operators and measurement operators. The inHere the subscript S denotes ‘state’. The kth compoverse D−1 must exist (since the projection operators
nent of this vector is equal to the probability obtained
are linearly independent). Hence, we can also write
when P̂k is measured on ρ̂. The vector pS contains
the same information as the state ρ̂ and can therefore
pmeas = pTM D−1 pS
(22)
be regarded as an alternative way of representing the
state. Note that K = N 2 since it takes N 2 probabilThe state can be represented by an r-type vector or
ity measurements to determine pS or, equivalently, a p-type vector as can the measurement. Hence the
ρ̂. We define rM through
subscripts M and S were introduced. We will sometimes drop these subscripts when it is clear from the
Â = rM · P̂
(13) context whether the vector is a state or measurement
The subscript M denotes ‘measurement’. The vector vector. We will stick to the convention of having mearM is another way of representing the measurement surement vectors on the left and state vectors on the
Â. If we substitute (13) into the trace formula (9) we right as in theI above formulae.
We define r by
obtain

We can also define
pM = tr(ÂP̂)
and rS by
ρ̂ = P̂ · rS
Using the trace formula (9) we obtain
pmeas = pM · rS = rTM DrS

Iˆ = rI · P̂

(23)

This measurement gives the probability of a non-null
event. Clearly we must have 0 ≤ rI · p ≤ 1 with nor(15) malized states saturating the upper bound. We can
also define the measurement which tells us whether
the state is in a given subspace. Let IˆW be the prothe
(16) jector into an M dimensional subspaceˆ W . Then
corresponding r vector is defined by IW = rIW · P̂.
We will say that a state p is in the subspace W if
rIW · p = rI · p

(17)

(24)

where T denotes transpose and D is the K ×K matrix so it only has support in W . A system in which
with real elements given by
the state is always constrained to an M -dimensional
subspace will behave as an M dimensional system in
(18) accordance with Axiom 3.
Dij = tr(P̂i P̂j )
7

<!-- page 8 -->
The transformation ρ̂ → $(ρ̂) of ρ̂ corresponds to Each of these belong to one-dimensional subspaces
formed from the orthonormal basis set. Define
the following transformation for the state vector p:
p

=

1
|mnix = √ (|mi + |ni)
2

tr(P̂ρ̂)

→ tr(P̂$(ρ̂))
=

tr(P̂$(P̂T D−1 p))

=

Zp

1
|mniy = √ (|mi + i|ni)
2

where equations (16,19) were used in the third line for m < n. Each of these vectors has support on a
and Z is a K × K real matrix given by
two-dimensional subspace formed from the orthonor1
Z = tr(P̂$(P̂)T )D−1
(25) mal basis set. There are 2 N (N − 1) such twodimensional subspaces. Hence we can define N (N −1)
(we have used the linearity property of $). Hence, we further projection operators
see that a linear transformation in ρ̂ corresponds to
|mnix hmn| and |mniy hmn|
(27)
a linear transformation in p. We will say that Z ∈ Γ.
Quantum theory can now be summarized by the
This makes a total of N 2 projectors. It is clear that
following rules
these projectors are linearly independent.
States The state is given by a real vector p ∈ S with
Each projector corresponds to one degree of freeN 2 components.
dom. There is one degree of freedom associated
Measurements A measurement is represented by a with each one-dimensional subspace n, and a further two degrees of freedom associated with each tworeal vector r ∈ R with N 2 components.
dimensional subspace mn. It is possible, though not
Probability measurements The measured proba- actually the case in quantum theory, that there are
bility if measurement r is performed on state p further degrees of freedom associated with each threeis
dimensional subspace and so on. Indeed, in general,
we can write
pmeas = r · p
1
N (N − 1)x2
K = N x1 + 2!
(28)
Evolution The evolution of the state is given by
1
+ 3! N (N − 1)(N − 2)x3 + . . .
p → Zp where Z ∈ Γ is a real matrix.
The exact nature of the sets S, R and Γ can be de- We will call the vector x = (x1 , x2 , . . . ) the signature
duced from the equations relating these real vectors of a particular probability theory. Classical probaand matrices to their counterparts in the usual quan- bility theory has signature xClassical = (1, 0, 0, . . . )
tum formulation. We will show that these sets can and quantum theory has signature xQuantum =
also be deduced from the axioms. It has been no- (1, 2, 0, 0, . . . ). We will show that these signatures
ticed by various other authors that the state can be are respectively picked out by Axioms 1 to 4 and Axrepresented by the probabilities used to determine it ioms 1 to 5. The signatures xReals = (1, 1, 0, 0, . . . ) of
real Hilbert space quantum theory and xQuaternions =
[18, 19].
There are various ways of choosing a set of N 2 (1, 4, 0, 0, . . . ) of quaternionic quantum theory are
linearly independent projections operators P̂k which ruled out.
If we have a composite system consisting of subsysspan the space of Hermitean operators. Perhaps the
tem
A spanned by P̂iA (i = 1 to KA ) and B spanned
simplest way is the following. Consider an N dimenB
A
B
sional complex Hilbert space with an orthonormal ba- by P̂j (j = 1 to KB ) then P̂i ⊗ P̂j are linearly indesis set |ni for n = 1 to N . We can define N projectors pendent and span the composite system. Hence, for
the composite system we have K = KA KB . We also
|nihn|
(26) have N = N N . Therefore Axiom 4 is satisfied.
A B
8

<!-- page 9 -->
We can write this as

1
 0
D=
 1−a
1−b

The set S is convex. It contains the null state 0
(if the system is never present) which is an extremal
state. Pure states are defined as extremal states other
than the null state (since they are extremal they cannot be written as a convex sum of other states as we
expect of pure states). We know that a pure state
can be represented by a normalized vector |ψi. This
is specified by 2N − 2 real parameters (N complex
numbers minus overall phase and minus normalization). On the other hand, the full set of normalized
states is specified by N 2 − 1 real numbers. The surface of the set of normalized states must therefore be
N 2 − 2 dimensional. This means that, in general, the
pure states are of lower dimension than the the surface of the convex set of normalized states. The only
exception to this is the case N = 2 when the surface
of the convex set is 2-dimensional and the pure states
are specified by two real parameters. This case is illustrated by the Bloch sphere. Points on the surface
of the Bloch sphere correspond to pure states.
In fact the N = 2 case will play a particularly
important role later so we will now develop it a little further. There will be four projection operators
spanning the space of Hermitean operators which we
can choose to be
P̂1 = |1ih1|

(29)

P̂2 = |2ih2|

(30)

P̂3 = (α|1i + β|2i)(α∗ h1| + β ∗ h2|)

(31)

P̂4 = (γ|1i + δ|2i)(γ ∗ h1| + δ ∗ h2|)

(32)


1−b
b 

(34)
c 
1
√
where
a and b are real with β = a exp(iφ3 ), δ =
√
b exp(φ4 ), and c = |αγ ∗ + βδ ∗ |2 . We can choose α
and γ to be real (since the phase is included in the
definition of β and δ). It then follows that
0
1
a
b

1−a
a
1
c

c = 1 − a − b + 2ab
p
+2 cos(φ4 − φ3 ) ab(1 − a)(1 − b)

(35)

Hence, by varying the complex phase associated with
α, β, γ and δ we find that
c− < c < c+
where
c± ≡ 1 − a − b + 2ab ± 2

p
ab(1 − a)(1 − b)

(36)

(37)

This constraint is equivalent to the condition
Det(D) > 0. Now, if we are given a particular D
matrix of the form (34) then we can go backwards to
the usual quantum formalism though we must make
some arbitrary choices for the phases. First we use
(35) to calculate cos(φ4 − φ3 ). We can assume that
0 ≤ φ4 − φ3 ≤ π √
(this corresponds to assigning i to
one of the roots −1). Then we can assume that
φ3 = 0. This fixes φ4 . An example of this second
choice is when we assign the state √12 (|+i+ |−i) (this
has real coefficients) to spin along the x direction for
a spin half particle. This is arbitrary since we have
rotational symmetry about the z axis. Having calculated φ3 and φ4 from the elements of D we can now
calculate α, β, γ, and δ and hence we can obtain P̂.
We can then calculate ρ̂, Â and $ from p, r, and Z
and use the trace formula. The arbitrary choices for
phases do not change any empirical predictions.

where |α|2 + |β|2 = 1 and |γ|2 + |δ|2 = 1. We have
chosen the second pair of projections to be more general than those defined in (27) above since we will
need to consider this more general case later. We
can calculate D using (18)


1
0
1 − |β|2
1 − |δ|2
 0

1
|β|2
|δ|2

D=
∗
∗ 2
1 − |β|2 |β|2
1
|αγ + βδ |
1 − |δ|2 |δ|2 |αγ ∗ + βδ ∗ |2
1
(33)

6

Basic Ideas and the Axioms

We will now forget quantum theory and classical
probability theory and rederive them from the axioms. In this section we will introduce the basic ideas
and the axioms in context.
9

<!-- page 10 -->
6.1

Probabilities

6.2

As mentioned earlier, we will consider only measurements of probability since all other measurements can
be reduced to probability measurements. We first
need to ensure that it makes sense to talk of probabilities. To have a probability we need two things.
First we need a way of preparing systems (in Fig. 1
this is accomplished by the first two boxes) and second, we need a way of measuring the systems (the
third box in Fig. 1). Then, we measure the number
of cases, n+ , a particular outcome is observed when
a given measurement is performed on an ensemble of
n systems each prepared by a given preparation. We
define
prob+ = lim

n→∞

n+
n

(38)

In order for any theory of probabilities to make sense
prob+ must take the same value for any such infinite
ensemble of systems prepared by a given preparation.
Hence, we assume
Axiom 1 Probabilities. Relative frequencies (measured by taking the proportion of times a particular
outcome is observed) tend to the same value (which
we call the probability) for any case where a given
measurement is performed on an ensemble of n systems prepared by some given preparation in the limit
as n becomes infinite.
With this axiom we can begin to build a probability
theory.
Some additional comments are appropriate here.
There are various different interpretations of probability: as frequencies, as propensities, the Bayesian
approach, etc. As stated, Axiom 1 favours the frequency approach. However, it it equally possible to
cast this axiom in keeping with the other approaches
[16]. In this paper we are principally interested in deriving the structure of quantum theory rather than
solving the interpretational problems with probability theory and so we will not try to be sophisticated
with regard to this matter. Nevertheless, these are
important questions which deserve further attention.

The state

We can introduce the notion that the system is described by a state. Each preparation will have a state
associated with it. We define the state to be (that
thing represented by) any mathematical object which
can be used to determine the probability for any measurement that could possibly be performed on the
system when prepared by the associated preparation.
It is possible to associate a state with a preparation
because Axiom 1 states that these probabilities depend on the preparation and not on the particular
ensemble being used. It follows from this definition
of a state that one way of representing the state is
by a list of all probabilities for all measurements that
could possibly be performed. However, this would
almost certainly be an over complete specification
of the state since most physical theories have some
structure which relates different measured quantities.
We expect that we will be able to consider a subset
of all possible measurements to determine the state.
Hence, to determine the state we need to make a number of different measurements on different ensembles
of identically prepared systems. A certain minimum
number of appropriately chosen measurements will be
both necessary and sufficient to determine the state.
Let this number be K. Thus, for each setting, k = 1
to K, we will measure a probability pk with an appropriate setting of the knob on the measurement
apparatus. These K probabilities can be represented
by a column vector p where
 
p1
 p2 
 
 
p =  p3 
(39)
 .. 
 . 
pK

Now, this vector contains just sufficient information
to determine the state and the state must contain just
sufficient information to determine this vector (otherwise it could not be used to predict probabilities for
measurements). In other words, the state and this
vector are interchangeable and hence we can use p
as a way of representing the state of the system. We
will call K the number of degrees of freedom associated with the physical system. We will not assume

10

<!-- page 11 -->
that the physical system is always present. Hence, subensemble must be the same as that which would
one of the K degrees of freedom can be associated have been measured for any similarly prepared ensemble and hence (41) follows.
with normalization and therefore K ≥ 1.

6.3

6.6

Fiducial measurements

Linearity

We will call the probability measurements labeled by Equation (41) can be applied to the fiducial measurek = 1 to K used in determining the state the fidu- ments themselves. This gives
cial measurements. There is no reason to suppose
pC = λpA + (1 − λ)pB
(42)
that this set is unique. It is possible that some other
fiducial set could also be used to determine the state. This is clearly true since it is true by (41) for each
component.
Equations (41,42) give
6.4 Measured probabilities
Any probability that can be measured (not just the
fiducial ones) will be determined by some function f
of the state p. Hence,

f (λpA + (1 − λ)pB ) = λf (pA ) + (1 − λ)f (pB )
(43)

This strongly suggests that the function f (·) is lin(40) ear. This is indeed the case and a proof is given in
Appendix 1. Hence, we can write
For different measurements the function will, of
pmeas = r · p
(44)
course, be different. By definition, measured probabilities are between 0 and 1.
The vector r is associated with the measurement.
The kth fiducial measurement is the measurement
0 ≤ pmeas ≤ 1
which picks out the kth component of p. Hence, the
fiducial
measurement vectors are
This must be true since probabilities are measured by
 
 
 
taking the proportion of cases in which a particular
1
0
0
0
1 
0 
event happens in an ensemble.
 
 
 
 
 
 
r1 = 0 r2 = 0 r3 = 1 etc. (45)




 .. 
.
.
6.5 Mixtures
 .. 
 .. 
.
0
0
0
Assume that the preparation device is in the hands
of Alice. She can decide randomly to prepare a state
pA with probability λ or a state pB with probability 6.7 Transformations
1 − λ. Assume that she records this choice but does
not tell the person, Bob say, performing the measure- We have discussed the role of the preparation device
and the measurement apparatus. Now we will discuss
ment. Let the state corresponding to this preparation
the state transforming device (the middle box in Fig.
be pC . Then the probability Bob measures will be
1). If some system with state p is incident on this
the convex combination of the two cases, namely
device its state will be transformed to some new state
f (pC ) = λf (pA ) + (1 − λ)f (pB )
(41) g(p). It follows from Eqn (41) that this transformation must be linear. This is clear since we can apply
This is clear since Alice could subsequently reveal the proof in the Appendix 1 to each component of g.
which state she had prepared for each event in the Hence, we can write the effect of the transformation
ensemble providing two sub-ensembles. Bob could device as
then check his data was consistent for each subensemp → Zp
(46)
ble. By Axiom 1, the probability measured for each
pmeas = f (p)

11

<!-- page 12 -->
where Z is a K × K real matrix describing the effect setting of the knob on the measurement apparatus
(see Fig 1). The non-null outcomes are labeled by
of the transformation.
l = 1 to L.

6.8

Allowed states, measurements,
and transformations

pnon−null =

L
X
l=1

rl · p = rI · p

(50)

We now have states represented by p, measurements
represented by r, and transformations represented by where rl is the measurement vector corresponding to
Z. These will each belong to some set of physically outcome l and
allowed states, measurements and transformations.
L
X
Let these sets of allowed elements be S, R and Γ.
rI =
rl
(51)
Thus,
l=1

p∈S

(47)

r∈R

(48)

Z∈Γ

(49)

is called the identity measurement.

6.11

Normalized and unnormalized
states

If the release button is never pressed we prepare the
We will use the axioms to determine the nature of state 0. If the release button is always pressed (i.e
these sets. It turns out (for relatively obvious rea- for every event in the ensemble) then we will say
sons) that each of these sets is convex.
p ∈ Snorm or, in words, that the state is normalized.
Unnormalized states are of the form λp + (1 − λ)0
where 0 ≤ λ < 1. Unnormalized states are therefore
6.9 Special states
mixtures and hence, all pure states are normalized,
If the release button on Fig. 1 is never pressed then that is
all the fiducial measurements will yield 0. Hence, the
null state pnull = 0 can be prepared and therefore
Spure ⊂ Snorm
0 ∈ S.
It follows from (42) that the set S is convex. It is
We define the normalization coefficient of a state
also bounded since the entries of p are bounded by 0 p to be
and 1. Hence, S will have an extremal set Sextremal
µ = rI · p
(52)
(these are the vectors in S which cannot be written
as a convex sum of other vectors in S). We have
0 ∈ Sextremal since the entries in the vectors p cannot In the case where p ∈ Snorm we have µ = 1.
The normalization coefficient is equal to the probe negative. We define the set of pure states Spure
to be the set of all extremal states except 0. Pure portion of cases in which the release button is pressed.
states are clearly special in some way. They represent It is therefore a property of the state and cannot destates which cannot be interpreted as a mixture. A pend on the knob setting on the measurement apI
driving intuition in this work is the idea that pure paratus. We can see that r must be unique since
if there was another such vector satisfying (52) then
states represent definite states of the system.
this would reduce the number of parameters required
to specify the state contradicting our starting point
6.10 The identity measurement
that a state is specified by K real numbers. Hence rI
The probability of a non-null outcome is given by is independent of the measurement apparatus knob
summing up all the non-null outcomes with a given setting.
12

<!-- page 13 -->
6.12

Basis states

always choose our basis sets to consist only of pure
states and we will assume that this has been done in
Any physical system can be in various states. We
what follows.
expect there to exist some sets of normalized states
Note that N = 1 is the smallest value N can take
which are distinguishable from one another in a sinsince we can always choose any normalized state as
gle shot measurement (were this not the case then we
p1 and r1 = rI .
could store fixed records of information in such physical systems). For such a set we will have a setting
of the knob on the measurement apparatus such that 6.13 Simplicity
each state in the set always gives rise to a particu- There will be many different systems having different
lar outcome or set of outcomes which is disjoint from K and N . We will assume that, nevertheless, there
the outcomes associated with the other states. It is is a certain constancy in nature such that K is a
possible that there are some non-null outcomes of the function of N . The second axiom is
measurement that are not activated by any of these
states. Any such outcomes can be added to the set Axiom 2 Simplicity. K is determined by a funcof outcomes associated with, say, the first member of tion of N (i.e. K = K(N )) where N = 1, 2, . . . and
the set without effecting the property that the states where, for any given N , K takes the minimum value
can be distinguished. Hence, if these states are pn consistent with the axioms.
and the measurements that distinguish them are rn
The assumption that N = 1, 2, . . . means that we asthen we have
sume nature provides systems of all different dimenX
rm · pn = δmn where
rn = rI
(53) sions. The motivation for taking the smallest value
n
of K for each given N is that this way we end up
with
the simplest theory consistent with these natuThe measurement vectors rn must add to rI since ral axioms. It will be shown that the axioms imply
they cover all possible outcomes. There may be many K = N r where r is an integer. Axiom 2 then dictates
such sets having different numbers of elements. Let N that we should take the smallest value of r consistent
be the maximum number of states in any such set of with the axioms (namely r = 2). However, it would
distinguishable states. We will call N the dimension. be interesting either to show that higher values of
We will call the states pn in any such set basis states r are inconsistent with the axioms even without this
and we will call the corresponding measurements rn constraint that K should take the minimum value, or
basis measurements. Each type of physical system to explicitly construct theories having higher values
will be characterized by N and K. A note on no- of r and investigate their properties.
tation: In general we will adopt the convention that
the subscript n (n = 1 to N ) labels basis states and
measurements and the superscript k (k = 1 to K) 6.14 Subspaces
labels fiducial measurements and (to be introduced Consider a basis measurement set rn . The states in a
later) fiducial states. Also, when we need to work basis are labeled by the integers n = 1 to N . Consider
with a particular choice of fiducial measurements (or a subset W of these integers. We define
states) we will take the first n of them to be equal to
X
a basis set. Thus, rk = rk for k = 1 to N .
rIW =
rn
(54)
If a particular basis state is impure then we can
n∈W
always replace it with a pure state. To prove this we
note that if the basis state is impure we can write it Corresponding to the subset W is a subspace which
as a convex sum of pure states. If the basis state is we will also call W defined by
replaced by any of the states in this convex sum this
(55)
p∈W
iff
rIW · p = rI · p
must also satisfy the basis property. Hence, we can
13

<!-- page 14 -->
Thus, p belongs to the subspace if it has support
only in the subspace. The dimension of the subspace
W is equal to the number of members of the set W .
The complement subset W consists of the the integers
n = 1 to N not in W . Corresponding to the subset
W is the subspace W which we will call the complement subspace to W . Note that this is a slightly
unusual usage of the terminology “subspace” and “dimension” which we employ here because of the analogous concepts in quantum theory. The third axiom
concerns such subspaces.

sion N = NA NB and number of degrees of freedom
K = KA KB .
We expect that N = NA NB for the following reasons. If subsystems A and B have NA and NB distinguishable states, then there must certainly exist
NA NB distinguishable states for the whole system.
It is possible that there exist more than this but we
assume that this is not so. We will show that the
relationship K = KA KB follows from the following
two assumptions

Axiom 3 Subspaces. A system whose state is constrained to belong to an M dimensional subspace behaves like a system of dimension M .
This axiom is motivated by the intuition that any collection of distinguishable states should be on an equal
footing with any other collection of the same number
distinguishable states. In logical terms, we can think
of distinguishable states as corresponding to a propositions. We expect a probability theory pertaining to
M propositions to be independent of whether these
propositions are a subset or some larger set or not.
One application of the subspace axiom which we
will use is the following: If a system is prepared in
a state which is constrained to a certain subspace W
having dimension NW and a measurement is made
which may not pertain to this subspace then this
measurement must be equivalent (so far as measured
probabilities on states in W are concerned) to some
measurement in the set of allowed measurements for
a system actually having dimension NW .

• If a subsystem is in a pure state then any joint
probabilities between that subsystem and any
other subsystem will factorize. This is a reasonable assumption given the intuition (mentioned
earlier) that pure states represent definite states
for a system and therefore should not be correlated with anything else.
• The number of degrees of freedom associated
with the full class of states for the composite
system is not greater than the number of degrees
of freedom associated with the separable states.
This is reasonable since we do not expect there
to be more entanglement than necessary.

Note that although these two assumptions motivate
the relationship K = KA KB we do not actually need
to make them part of our axiom set (rather they follow from the five axioms). To show that these assumptions imply K = KA KB consider performing
the ith fiducial measurement on system A and the
jth fiducial measurement on system B and measuring the joint probability pij that both measurements
have a positive outcome. These joint probabilities
6.15 Composite systems
can be arranged in a matrix p̃AB having entries pij .
It must be possible to choose KA linearly independent
It often happens that a preparation device ejects its
pure states labeled pkAA (kA = 1 to KA ) for subsyssystem in such a way that it can be regarded as being
tem A, and similarly for subsystem B. With the first
made up of two subsystems. For example, it may emit
A kB
assumption above we can write p̃kAB
= pkAA (pkBB )T
one system to the left and one to the right (see Fig.
kA
2). We will label these subsystems A and B. We when system A is prepared in the pure statekBpA and
system B is prepared in the pure state pB . It is
assume
easily shown that it follows from the fact that the
Axiom 4 Composite systems. A composite system states for the subsystems are linearly independent
kA kB
are linearly indepenconsisting of two subsystems A and B having di- that the KA KB matrices p̃AB
mension NA and NB respectively, and number of de- dent. Hence, the vectors describing the correspondgrees of freedom KA and KB respectively, has dimen- ing joint states are linearly independent. The convex
14

<!-- page 15 -->
hull of the end points of KA KB linearly independent
vectors and the null vector is KA KB dimensional. We
cannot prepare any additional ‘product’ states which
are linearly independent of these since the subsystems are spanned by the set of fiducial states considered. Therefore, to describe convex combinations of
the separable states requires KA KB degrees of freedom and hence, given the second assumption above,
K = KA KB .
It should be emphasized that it is not required
by the axioms that the state of a composite system
should be in the convex hull of the product states.
Indeed, it is the fact that there can exist vectors not
of this form that leads to quantum entanglement.

7

The continuity axiom

Now we introduce the axiom which will give us quantum theory rather than classical probability theory.
Given the intuition that pure states represent definite
states of a system we expect to be able to transform
the state of a system from any pure state to any other
pure state. It should be possible to do this in a way
that does not extract information about the state and
so we expect this can be done by a reversible transformation. By reversible we mean that the effect of the
transforming device (the middle box in Fig. 1.) can
be reversed irrespective of the input state and hence
that Z −1 exists and is in Γ. Furthermore, we expect
any such transformation to be continuous since there
are generally no discontinuities in physics. These considerations motivate the next axiom.
Axiom 5 Continuity. There exists a continuous reversible transformation on a system between any two
pure states of the system.
By a continuous transformation we mean that one
which can be made up from many small transformations only infinitesimally different from the identity.
The set of reversible transformations will form a compact Lie group (compact because its action leaves the
components of p bounded by 0 and 1 and hence the
elements of the transformation matrices Z must be
bounded).

If a reversible transformation is applied to a pure
state it must necessarily output a pure state. To
prove this assume the contrary. Thus, assume Zp =
λpA + (1 − λ)pB where p is pure, Z −1 exists and is
in Γ, 0 < λ < 1, and the states pA,B are distinct. It
follows that p = λZ −1 pA + (1 − λ)Z −1 pB which is a
mixture. Hence we establish proof by contradiction.
The infinitesimal transformations which make up
a reversible transformation must themselves be reversible. Since reversible transformations always
transform pure states to pure states it follows from
this axiom that we can transform any pure state to
any other pure state along a continuous trajectory
through the pure states. We can see immediately
that classical systems of finite dimension N will run
into problems with the continuity part of this axiom since there are only N pure states for such systems and hence there cannot exist a continuous trajectory through the pure states. Consider, for example, transforming a classical bit from the state 0 to
the state 1. Any continuous transformation would
have to go through an infinite number of other pure
states (not part of the subspace associated with our
system). Indeed, this is clear given any physical implementation of a classical bit. For example, a ball
in one of two boxes must move along a continuous
path from one box (representing a 0) to the other
box (representing a 1). Deutsch has pointed out that
for this reason, the classical description is necessarily
approximate in such situations whereas the quantum
description in the analogous situation is not approximate [17]. We will use this axiom to rule out various
theories which do not correspond to quantum theory
(including classical probability theory).
Axiom 5 can be further motivated by thinking
about computers. A classical computer will only employ a finite number of distinguishable states (usually referred to as the memory of the computer - for
example 10Gbytes). For this reason it is normally
said that the computer operates with finite resources.
However, if we demand that these bits are described
classically and that transformations are continuous
then we have to invoke the existence of a continuous
infinity of distinguishable states not in the subspace
being considered. Hence, the resources used by a classically described computer performing a finite calcu-

15

<!-- page 16 -->
lation must be infinite. It would seem extravagant of 8.1 Proof that K = N r
nature to employ infinite resources in performing a
In this section we will see that K = N r where r is a
finite calculation.
positive integer. It will be shown in Section 8.5 that
K = N (i.e. when r = 1) is ruled out by Axiom
5. Now, as shown in Section 5, quantum theory is
8 The Main Proofs
consistent with the Axioms and has K = N 2 . Hence,
In this section we will derive quantum theory and, by the simplicity axiom (Axiom 2), we must have
as an aside, classical probability theory by dropping K = N 2 (i.e. r = 2).
It is quite easy to show that K = N r . First note
Axiom 5. The following proofs lead to quantum thethat it follows from the subspace axiom (Axiom 3)
ory
that K(N ) must be a strictly increasing function of
1. Proof that K = N r where r = 1, 2, . . . .
N . To see this consider first an N dimensional system. This will have K(N ) degrees of freedom. Now
2. Proof that a valid choice of fiducial measureconsider an N + 1 dimensional system. If the state is
ments is where we choose the first N to be
constrained to belong to an N dimensional subspace
some basis set of measurements and then we
W then it will, by Axiom 3, have K(N ) degrees of
choose 2 additional measurements in each of the
freedom. If it is constrained to belong to the com1
2 N (N − 1) two-dimensional subspaces (making plement 1 dimensional subspace then, by Axiom 3,
a total of N 2 ).
it will have at least one degree of freedom (since K
3. Proof that the state can be represented by an is always greater than or equal to 1). However, the
state could also be a mixture of a state constrained
r-type vector.
to W with some weight λ and a state constrained
4. Proof that pure states must satisfy an equation to the complement one dimensional subspace with
rT Dr = 1 where D = DT .
weight 1 − λ. This class of states must have at least
K(N ) + 1 degrees of freedom (since λ can be var5. Proof that K = N is ruled out by Axiom 5
ied). Hence, K(N + 1) ≥ K(N ) + 1. By Axiom 4 the
(though leads to classical probability theory if
function K(N ) satisfies
2
we drop Axiom 5) and hence that K = N by
the Axiom 2.
K(N N ) = K(N )K(N )
(56)
A

B

A

B

6. We show that the N = 2 case corresponds to
Such functions are known in number theory as comthe Bloch sphere and hence we obtain quantum
pletely multiplicative. It is shown in Appendix 2 that
theory for the N = 2 case.
all strictly increasing completely multiplicative funcα
7. We obtain the trace formula and the conditions tions are of the form K = N . Since K must be
imposed by quantum theory on ρ̂ and Â for gen- an integer it follows that the power, α, must be a
positive integer. Hence
eral N .
8. We show that the most general evolution consisK(N ) = N r
where
r = 1, 2, 3, . . .
(57)
tent with the axioms is that of quantum theory
and that the tensor product structure is appro- In a slightly different context, Wootters has also come
to this equation as a possible relation between K and
priate for describing composite systems.
N [18].
9. We show that the most general evolution of the
The signatures (see Section 5) associated with
state after measurement is that of quantum the- K = N and K = N 2 are x = (1, 0, 0, . . . ) and
ory (including, but not restricted to, von Neu- x = (1, 2, 0, 0, . . . ) respectively. It is interesting to
mann projection).
consider some of those cases that have been ruled out.
16

<!-- page 17 -->
Real Hilbert spaces have x = (1, 1, 0, 0, . . . ) (consider
counting the parameters in the density matrix). In
the real Hilbert space composite systems have more
degrees of freedom than the product of the number
of degrees of freedom associated with the subsystems
(which implies that there are necessarily some degrees
of freedom that can only be measured by performing
a joint measurement on both subsystems). Quaternionic Hilbert spaces have x = (1, 4, 0, 0, . . . ). This
case is ruled out because composite systems would
have to have less degrees of freedom than the product
of the number of degrees of freedom associated with
the subsystems [20]. This shows that quaternionic
systems violate the principle that joint probabilities
factorize when one (or both) of the subsystems is in
a pure state. We have also ruled out K = N 3 (which
has signature x = (1, 6, 6, 0, 0, . . . )) and higher r values. However, these cases have only been ruled out
by virtue of the fact that Axiom 2 requires we take
the simplest case. It would be interesting to attempt
to construct such higher power theories or prove that
such constructions are ruled out by the axioms even
without assuming that K takes the minimum value
for each given N .
The fact that x1 = 1 (or, equivalently, K(1)=1)
is interesting. It implies that if we have a set of N
distinguishable basis states they must necessarily be
pure. After the one degree of freedom associated with
normalization has been counted for a one dimensional
subspace there can be no extra degrees of freedom.
If the basis state was mixed then it could be written
as a convex sum of pure states that also satisfy the
basis property. Hence, any convex sum would would
satisfy the basis property and hence there would be
an extra degree of freedom.

8.2

Choosing the fiducial measurements

We have either K = N or K = N 2 . If K = N then
a suitable choice of fiducial measurements is a set of
basis measurements. For the case K = N 2 any set
of N 2 fiducial measurements that correspond to linearly independent vectors will suffice as a fiducial set.
However, one particular choice will turn out to be especially useful. This choice is motivated by the fact

that the signature is x = (1, 2, 0, 0, . . . ). This suggests that we can choose the first N fiducial measurements to correspond to a particular basis set of measurements rn (we will call this the fiducial basis set)
and that for each of the 12 N (N − 1) two-dimensional
fiducial subspaces Wmn (i.e. two-dimensional subspaces associated with the mth and nth basis measurements) we can chose a further two fiducial measurements which we can label rmnx and rmny (we are
simply using x and y to label these measurements).
This makes a total of N 2 vectors. It is shown in Appendix 3.4 that we can, indeed, choose N 2 linearly
independent measurements (rn , rmnx , and rmny ) in
this way and, furthermore, that they have the property
rmnx · p = 0 if

p ∈ W mn

(58)

where W mn is the complement subspace to Wmn .
This is a useful property since it implies that the
fiducial measurements in the Wmn subspace really
do only apply to that subspace.

8.3

Representing the state by r

Till now the state has been represented by p and a
measurement by r. However, by introducing fiducial
states, we can also represent the measurement by a
p-type vector (a list of the probabilities obtained for
this measurement with each of the fiducial states)
and, correspondingly, we can describe the state by an
r-type vector. For the moment we will label vectors
pertaining to the state of the system with subscript
S and vectors pertaining to the measurement with
subscript M (we will drop these subscripts later since
it will be clear from the context which meaning is
intended).
8.3.1

Fiducial states

We choose K linearly independent states, pkS for
k = 1 to K, and call them fiducial states (it must
be possible to choose K linearly independent states
since otherwise we would not need K fiducial measurements to determine the state). Consider a given

17

<!-- page 18 -->
measurement rM . We can write
pkM = rM · pkS

the lth fiducial state (since, in the fiducial cases, the r
vectors have one 1 and otherwise 0’s as components).
(59) Hence,

Now, we can take the number pkM to be the kth comDlk = (rlM )T DrkS
(64)
ponent of a vector. This vector, pM , is related to rM
by a linear transformation. Indeed, from the above D is invertible since the fiducial set of states are linearly independent.
equation we can write
pM = CrM

(60) 8.3.3

where C is a K × K matrix with l, k entry equal to
the lth component of pkS . Since the vectors pkS are
linearly independent, the matrix C is invertible and
so rM can be determined from pM . This means that
pM is an alternative way of specifying the measurement. Since pmeas is linear in rM which is linearly
related to pM it must also be linear in pM . Hence
we can write

Vectors associated with states and
measurements

There are two ways of describing the state: Either
with a p-type vector or with an r-type vector. From
(44, 63) we see that the relation between these two
types of description is given by
pS = DrS

(65)

Similarly, there are two ways of describing the mea(61) surement: Either with an r-type vector or with a
p-type vector. From (61,63) we see that the relation
where the vector rS is an alternative way of describ- between the two ways of describing a measurement is
ing the state of the system. The kth fiducial state can
pM = DT rM
(66)
be represented by an r-type vector, rkS , and is equal
to that vector which picks out the kth component of
(Hence, C in equation (60) is equal to DT .)
pM . Hence, the fiducial states are
Note that it follows from these equations that the
 
 
 
1
0
0
set of states/measurements rS,M is bounded since
0
1
0
pS,M is bounded (the entries are probabilities) and D
 
 
 




1
1
2
3
0
0
is
invertible (and hence its inverse has finite entries).
rS =  
rS =  
rS =  
etc.
 .. 
 .. 
 .. 
.
.
.
8.4 Pure states satisfy rT Dr = 1
0
0
0
(62) Let us say that a measurement identifies a state if,
pmeas = pM · rS

8.3.2

A useful bilinear form for pmeas

The expression for pmeas is linear in both rM and
rS . In other words, it is a bilinear form and can be
written
pmeas = rTM DrS

(63)

where superscript T denotes transpose, and D is a
K × K real matrix (equal, in fact, to C T ). The k, l
element of D is equal to the probability measured
when the kth fiducial measurement is performed on

when that measurement is performed on that state,
we obtain probability one. Denote the basis measurement vectors by rMn and the basis states (which have
been chosen to be pure states) by pSn where n = 1
to N . These satisfy rMm · pSn = δmn . Hence, rMn
identifies pSn .
Consider an apparatus set up to measure rM1 . We
could place a transformation device, T , in front of
this which performs a reversible transformation. We
would normally say that that T transforms the state
and then rM1 is measured. However, we could equally
well regard the transformation device T as part of

18

<!-- page 19 -->
the measurement apparatus. In this case some other
measurement r is being performed. We will say that
any measurement which can be regarded as a measurement of rM1 preceded by a reversible transformation device is a pure measurement. It is shown in
Appendix 3.7 that all the basis measurement vectors
rMn are pure measurements and, indeed, that the
set of fiducial measurements of Section 8.2 can all be
chosen to be pure.
A pure measurement will identify that pure state
which is obtained by acting on pS1 with the inverse
of T . Every pure state can be reached in this way
(by Axiom 5) and hence, corresponding to each pure
state there exists a pure measurement. We show in
Appendix 3.5 that the map between the vector representing a pure state and the vector representing the
pure measurement it is identified by is linear and invertible.
We will now see that not only is this map linear but
also that, by appropriate choice of the fiducial measurements and fiducial states, we can make it equal
to the identity. A convex structure embedded in a Kdimensional space must have at least K + 1 extremal
points (for example, a triangle has three extremal
points, a tetrahedron has four, etc.). In the case of
the set S, one of these extremal points will be 0 leaving at least K remaining extremal points which will
correspond to pure states (recall that pure states are
extremal states other than 0). Furthermore, it must
be possible to choose a set of K of these pure states
to correspond to linearly independent vectors (if this
were not possible then the convex hull would be embedded in a lower than K dimensional space). Hence,
we can choose all our fiducial states to be pure. Let
these fiducial states be rkS . We will choose the kth
fiducial measurement rkM to be that pure measurement which identifies the kth fiducial state. These
will constitute a linearly independent set since the
map from the corresponding linearly independent set
of states is invertible.
We have proven (in Appendix 3.5) that, if rM identifies rS , there must exist a map
rS = HrM

(67)

this is true for the fiducial states and fiducial measurements:
rkS = HrkM

(68)

However, the fiducial vectors have the special form
given in (45,62), namely zeros everywhere except for
the kth entry. Hence, the map H is equal to the identity. This is true because we have chosen the fiducial
measurements to be those which identify the fiducial
states. Since these vectors are related by the identity
map we will drop the M and S subscripts in what
follows, it being understood that the left most vector
corresponds to the measurement apparatus and the
right most vector corresponds to the state. Thus the
measurement r identifies the state r (i.e. given by the
same vector) if r is pure. Hence,
rT Dr = 1

(69)

for pure states (and pure measurements). This equation is very useful since will help us to find the pure
states. It is shown in Appendix 3.6 that D = DT .
It is shown in Appendix 3.7 that the fiducial measurements rn , rmnx , and rmny are pure. They will
identify a set of pure states represented by the same
vectors rn , rmnx , and rmny which we take to be our
fiducial states. The first N fiducial states, rn , are
then just the basis states and it follows from (58)
that the remaining basis states, rmnx and rmny , are
in the corresponding Wmn subspaces.

8.5

Ruling out the K = N case

Consider the K = N case. There will be K = N
fiducial vectors which we can choose to be equal to
the basis vectors. From equation (64) we know that
the lk element of D is equal to the measured probability with the kth fiducial state and the lth fiducial
measurement. Since the fiducial vectors correspond
to basis vectors this implies that D is equal to the
identity. The pure states must satisfy

where H is a K × K constant matrix. In particular
19

rT Dr = 1

(70)

<!-- page 20 -->
We also have p = Dr (equation (65)). Given that D
is equal to the identity in this case we obtain
N
X

(pk )2 = 1

(71)

k=1

where pk is the kth component of p. However,
0 ≤ pk ≤ 1

(72)

Normalization implies that
N
X

pk = 1

(73)

k=1

The solutions of (71), (72), (73) have one pk equal
to 1 and all the others are equal to 0. In other
words, the only pure vectors are the basis vectors
themselves which corresponds to classical probability
theory. This forms a discrete set of vectors and so it
is impossible for Axiom 5 (the continuity axiom) to
be satisfied. Hence, we rule out such theories. However, if Axiom 5 is dropped then, by Axiom 2, we
must take K = N . This necessarily corresponds to
classical probability theory for the following reasons.
We can choose our K (= N ) fiducial measurements
to be the basis measurements rn . Then the basis
states must be represented by vectors with zero’s in
all positions except the nth position. All states must
have normalization coefficient less than or equal to 1.
Hence, all states can be written as a convex combination of the basis states and the null state. This means
that only the basis states are pure states. Hence, we
have classical probability theory.

8.6

The Bloch sphere

We are left with K = N 2 (since K = N has been
ruled out by Axiom 5). Consider the simplest nontrivial case N = 2 and K = 4. Normalized states are
contained in a K −1 = 3 dimensional convex set. The
surface of this set is two-dimensional. All pure states
correspond to points on this surface. The four fiducial
states can all be taken to be pure. They correspond
to a linearly independent set. The reversible transformations that can act on the states form a compact Lie

Group. The Lie dimension (number of generators)
of this group of reversible transformations cannot be
equal to one since, if it were, it could not transform
between the fiducial states. This is because, under a
change of basis, a compact Lie group can be represented by orthogonal matrices [21]. If there is only
one Lie generator then it will generate pure states on
a circle. But the end points of four linearly independent vectors cannot lie on a circle since this is embedded in a two-dimensional subspace. Hence, the Lie
dimension must be equal to two. The pure states are
represented by points on the two-dimensional surface.
Furthermore, since the Lie dimension of the group of
reversible transformations is equal to two it must be
possible to transform a given pure state to any point
on this surface. If we can find this surface then we
know the pure states for N = 2. This surface must be
convex since all points on it are extremal. We will use
this property to show that the surface is ellipsoidal
and that, with appropriate choice of fiducial states,
it can be made spherical (this is the Bloch sphere).
The matrix D can be calculated from equation (64)
Dij = (ri )T Drj
As above, we will choose the fiducial measurements to
be those pure measurements which identify the fiducial states (these also being taken to be pure). Hence,
D will have 1’s along the diagonal. We choose the
first two fiducial vectors to be basis vectors. Hence,
D has the form


1
0 1−a 1−b
 0
1
a
b 

(74)
D=
 1−a a
1
c 
1−b b
c
1
The two 0’s follow since the first two vectors are basis vectors (i.e. (r1 )T Dr2 = 0 and (r2 )T Dr1 = 0).
The 1 − a and a pair above the diagonal follow from
normalization since
1 = (rI )T Dri = (r1 )T Dri + (r2 )T Dri

(75)

The 1 − b and b pair follow for similar reasons. The
matrix is symmetric and this gives all the terms below
the diagonal.

20

<!-- page 21 -->
We will not show that the constraints on the ele- and
 1

ments of D are the same as in quantum theory (disa − 21 b − 21
2
cussed in Section 5). Define


1
A =  a − 21
c − 12 
(83)
2

 

1
v0
r1
b − 12 c − 12
2
 v1   r2 − r1 
=

v=
(76)
 v2  

All the pure states will be normalized. Furtherr3
more,
they will satisfy rT Dr = 1 or
v3
r4
Thus,

~v T A~v =

1
2

(84)

r = Cv

(77) This equation defines a two dimensional surface T
embedded in three dimensions. For example, if a =
where
b = c = 21 then we have a sphere of radius 1 (this is, in


fact, the Bloch sphere). If A has three positive eigen1 0 0 0
values then T will be an ellipsoid. If A has one or two
 1 1 0 0 

C=
(78) negative eigenvalue then T will be a hyperboloid (if A
 0 0 1 0 
has three negative eigenvalues then there cannot be
0 0 0 1
any real solutions for ~v ). An equal mixture of the two
basis states 12 r1 + 21 r2 corresponds to ~v = (0, 0, 0)T .
Hence rT Dr′ = vT C T DCv′ . From (74) we obtain
Thus, the origin is in the set of allowed states. An


ellipsoid represents a convex surface with the origin
2 1 1 1
 1 1 a b 
in its interior. On the other hand, the curvature of a
T

F ≡ C DC = 
(79) hyperboloid is such that it cannot represent a convex
 1 a 1 c 
surface with the origin on the interior and so cannot
1 b c 1
represent points in the set of pure vectors. Thus we
Now, rI = r1 + r2 = (1, 1, 0, 0)T . The corresponding require that T has three positive eigenvalues. A necv type vector is, using (76), vI = (1, 0, 0, 0)T . As- essary condition for A to have all positive eigenvalues
sume that r is normalized to µ and r′ is normalized is that det(A) > 0. We have three variables a, b and
c. The condition det(A) = 0 is satisfied when
to µ′ . Then
p
3
c = c± ≡ 1 − a − b + 2ab ± 2 ab(1 − a)(1 − b)
X
µ = vI F v = 2v0 +
vi
(80)
(85)
i=1

Note, we get the same conditions on c if we solve
det D = 0. We know the case with a = b = c = 1/2
corresponds to a sphere. This falls between the two
roots in equation (85). The sign of the eigenvalues
cannot change unless the determinant passes through
a root as the parameters are varied. Hence, all values
(81) of a, b, c satisfying

and similarly for µ′ . For normalized states µ = 1. If
vT F v′ is multiplied out and (80) is used to eliminate
v0 (and a similar equation is used to eliminate v0′ )
then we obtain
pmeas = rT Dr′ = ~v T A~v ′ + µµ′ /2
where








v1
r2 − r1

r3
~v =  v2  = 
v3
r4

c− < c < c+

(86)

must correspond to three positive eigenvalues and
(82) hence to an ellipsoid. Values outside this range correspond to some negative eigenvalues (this can be
21

<!-- page 22 -->
checked by trying a few values). Hence, (86) must
be satisfied. This agrees with quantum theory (see
(36)). Therefore, we have obtained quantum theory
from the axioms for the special case N = 2. As detailed in Section 5, if we are given D we can go back
to the usual quantum formalism by using D to calculate P̂ (making some arbitrary choices of phases)
and then using the formulae in that section (equations (13) and (16)) to obtain ρ̂ for the state and Â
for the measurement.
If T is ellipsoidal it is because we have made a particular choice of fiducial projectors P̂k . We can choose
a different set to make T spherical. Since the choice
of fiducial vectors is arbitrary we can, without any
loss of generality, always take T to be spherical with
a = b = c = 1/2. Hence, without loss of generality,
we can always put


1 0 21 12
 0 1 1 1 


(87)
D =  1 1 2 21 
 2 2 1 2 

fiducial basis vectors. There are 3 two-dimensional
fiducial subspaces. Each of these must have a further
two fiducial vectors (in addition to the basis vectors
already counted). As in Section 8.2 we will label the
two fiducial vectors in the mn subspace as mnx and
mny. We will choose the following order for the fiducial states
1, 2, 3, 12x, 12y, 13x, 13y, 23x, 23y

This provides the required 9 fiducial vectors. These
fiducial vectors can represent pure states or pure measurements. The matrix D is a 9 × 9 matrix. However,
each two-dimensional fiducial subspace must, by Axiom 3, behave as a system of dimension 2. Hence,
if we take those elements of D which correspond to
an N = 2 fiducial subspace they must have the form
given in equation (87). We can then calculate that
for N = 3


1 0 0 h h h h 0 0
 0 1 0 h h 0 0 h h 


 0 0 1 0 0 h h h h 
1
1
1


1
2
2
2
 h h 0 1 h q q q q 



D=
for the N = 2 case.
 h h 0 h 1 q q q q 


h
0
h
q
q
1
h
q
q
Since we have now reproduced quantum theory for




h
0
h
q
q
h
1
q
q
the N = 2 case we can say that


 0 h h q q q q 1 h 
• Pure states can be represented by |ψihψ| where
0 h h q q q q h 1
|ψi = u|1i + v|2i and where u and v are complex
numbers satisfying |u|2 + |v|2 = 1.
where h = 1/2 and, as we will show, q = 1/4. All
the 0’s are because the corresponding subspaces do
• The reversible transformations which can transnot overlap (we are using property (58)). The q’s
form one pure state to another can be seen as
correspond to overlapping subspaces. Consider for
rotations of the Bloch sphere, or as the effect of
example, the D46 term. This is given by rT12x Dr13x
a unitary operator Û in SU (2).
which is the probability when r12x is measured on the
This second observation will be especially useful when state r13x . If states are restricted to the 13 fiducial
subspace then, by Axiom 3, the system must behave
we generalize to any N .
as a two-dimensional system. In this case, the measurement r12x corresponds to some measurement in
8.7 General N
the 13 fiducial subspace. Since it has support of 1/2
It quite easy now to use the N = 2 result to construct on the 1 basis state and support of 0 on the 3 bathe case for general N using Axiom 3 (the subspace sis state this measurement must be equivalent to the
axiom). We will use the N = 3 case to illustrate measurement 21 r1 (though only for states restricted
this process. For this case K = 9 and so we need to the 13 fiducial subspace). But rT1 Dr13x = 1/2 and
9 fiducial vectors which we will choose as in Section hence rT12x Dr13x = 1/4. We can use a similar pro8.2. Thus, we choose the first 3 of these to be the cedure to calculate D for any N . Once we have this
22

<!-- page 23 -->
matrix we can convert to the usual quantum formal- where
ism as we did in the N = 2 case. The projection
N
X
operators which give rise to this D are, up to arbi|Ψi =
cn |ni
(92)
trary choices in phase, those in equations (26) and
n=1
(27) (these arbitrary choices in phase correspond to
P
2
fixing the gauge). Hence, we obtain P̂. Using the and n |cn | = 1 (this is most easily proven by starting with the target state and working backwards).
results of Section 5, we obtain
These transformations are reversible and hence all
ρ̂ = P̂ · r
(88) the states generated in this way must be pure. Now,
since we have shown that these states exist, all meafor a state represented by r, and
surements performed on these states must be nonÂ = r · P̂
(89) negative. That is
for a measurement represented by r. Hence, we obtrace(Â|ΨihΨ|) ≥ 0 for all |Ψi
(93)
tain
(90) Hence, we obtain the positivity condition for the operators Â associated with measurements. For each
which is shown to be equivalent to pmeas = r · p in state, r, there exists a pure measurement represented
section 5. We now need to prove that the restrictions by the same vector, r, which identifies the state.
from quantum theory on Â and ρ̂ follow from the Hence, since the state |ΨihΨ| exists, it follows from
axioms.
(88,89) that measurements of the form
Both ρ̂ and Â must be Hermitean since r is real.
The basis state r1 is represented by |1ih1|. We
Â = |ΨihΨ|
(94)
showed above that we can apply any unitary rotation U ∈ SU (2) for the N = 2 case. It follows exist. Therefore, all states ρ̂ must satisfy
from Axiom 3 and the results of the previous sectrace(|ΨihΨ|ρ̂) ≥ 0 for all |Ψi
(95)
tion that if we apply an reversible transformation in
a two-dimensional fiducial subspace on a state which Hence we have proved the positivity condition for
is in that two-dimensional subspace the effect will be states.
given by the action of a unitary operator acting in
We have Iˆ = rI · P̂ since the first N elements of rI
that subspace. Thus imagine we prepare the state are equal to 1 and the remainder are 0, and the first N
|1ih1|. Let the basis states be |nihn| (where n = 1 elements of P̂ are projectors corresponding to a basis.
to N ). Perform the rotation U12 in the 12 subspace. Hence, the trace condition (that 0 ≤ trace(ρ̂) ≤ 1)
†
This transforms the state to U12 |1ih1|U12
. Now re- follows simply from the requirement 0 ≤ rI · p ≤ 1.
†
′
′
The most general measurement consistent with the
,
define the basis states to be |1 ih1 | ≡ U12 |1ih1|U12
†
|2′ ih2′ | ≡ U12 |2ih2|U12 , and |nihn| for n 6= 1, 2 (it is axioms can be shown to be a POVM. A set of meashown in Appendix 3.3 that a reversible transforma- surements rl that can be performed with a given knob
on the measurement apparatus must satisfy
tion in a subspace can be chosen to leave basis states setting
P
r
=
rI . Using (89), this corresponds to the conl
not in that subspace unchanged). Next, we consider
l
P
a rotation U1′ 3 in the 1’3 subspace. The state will straint that l Âl = I as required.
only have support in this subspace and so Axiom 3
can be applied again. The basis states can be rede- 8.8 Transformations
fined again. This process can be repeated. In this
way it is easy to prove we can generate any state of It was shown in Section 5 that the transformation Z
on p is equivalent to the transformation $ on ρ̂ where
the form
pmeas = trace(Âρ̂)

ρ̂ = |ΨihΨ|

(91)
23

Z = tr(P̂$(P̂)T )D−1

(96)

<!-- page 24 -->
System B

System A

Measurement A

ZA

Preparation

ZB

Measurement B

Figure 2: The preparation device here prepares a system in the form of two subsystems which go to the left
and the right.
To discuss the constraints on transformations we need
to consider composite systems. Fig. 2. shows a
preparation apparatus producing a system made up
of subsystems A and B such that A goes to the
left and B goes to the right. These subsystems
then impinge on measurement apparatuses after passing through transformations devices which perform
transformations ZA and ZB . This set up can be understood to be a special case of the more generic setup
shown in Fig. 1. (there is no stipulation in the case
of Fig. 1. that the measurement apparatus or any of
the other apparatuses be located only in one place).
Assume the transformation devices are initially set to
leave the subsystems unchanged. From Axiom 4 we
know that there are KA KB fiducial measurements.
As discussed in Section 5, the space of positive operators for the composite system is spanned by P̂iA ⊗P̂jB
where P̂iA (i = 1 to KA ) is a fiducial set for A and P̂jB
(j = 1 to KB ) is a fiducial set for B. It is shown in
Appendix 4 that (as we would expect) the projector
P̂iA ⊗ P̂jB corresponds (i) to preparing the ith fiducial
state at side A and the jth fiducial state at side B
when the operator is regarded as representing a state,
and (ii) to measuring the joint probability of obtain-

ing a positive outcome at both ends when the ith fiducial measurement is performed at side A and the jth
fiducial measurement is performed at side B when the
operator is regarded as representing a measurement.
Hence, one choice of fiducial measurements is where
we simply perform the ith fiducial measurement on
A and the jth fiducial measurement on B and measure the joint probability pij . The probabilities pij
could be put in the form of a column vector pAB .
However, for discussing transformations, it is more
convenient to put them in the form of a KA × KB
matrix, p̃AB , having ij entry pij . It is easy to convert between these two ways of describing the state.
We could regard both the preparation apparatus and
measurement apparatus B as a preparation apparatus preparing states of subsystem A. If we perform
the jth fiducial measurement on system B and take
only those cases where we obtain a positive result for
this measurement preparing the null state otherwise
then the resulting state of system A will be given
by a vector equal to the jth column of p̃AB (since
these probabilities are equal to the probabilities that
would be obtained for the fiducial measurements on
A with this preparation). Hence, the columns of p̃AB
must transform under ZA . Similarly, the rows of p̃AB

24

<!-- page 25 -->
must transform under ZB . Hence, when the transfor- transformations deduced from the axioms are subject
mation devices in Fig. 2. are active, we have
to the equivalent constraints for $ listed in Section 5.
They preserve Hermitivity since the transformation
T
p̃AB → ZA p̃AB ZB
(97) matrix Z is real (and hence p remains real). They
do not increase the trace (point 1. above). They are
If the state is represented by r̃AB where
linear and they must be completely positive (point 2.
T
p̃AB = DA r̃AB DB
(98) above). Hence, the most general type of transformation consistent with the axioms is the most general
transformation of quantum theory. As noted in secthen this equation becomes
tion 5, this gives us unitary evolution and von NeuT
r̃AB → XA r̃AB XB
(99) mann projection as special cases.
where

8.9

The state after a measurement

−1
XA = DA
ZA DA

(100) It is possible that, after a measurement, a quantum
system emerges from the measurement apparatus. In
and similarly for B. It is easy to see that this is the
such cases the measurement apparatus is also behavcorrect transformation equation in quantum theory
ing as a transformation apparatus. We can think of
(we have dropped the A and B superscripts).
the state as emerging into a different channel for each
measurement outcome. Associated with each outij
pAB → tr[P̂i ⊗ P̂j $A ⊗ $B (ρ̂)]
P
come, l, of the measurement will be a certain transkl
= tr[P̂i ⊗ P̂j $A ⊗ $B ( kl P̂k ⊗ P̂l r )]
P
formation, Zl ∈ Γ, on the state. The probability of
kl
=
tr[P̂i ⊗ P̂j $A (P̂k ) ⊗ $B (P̂l )]r
any given outcome will not, in general, be equal to 1.
Pkl
kl
=
kl tr[P̂i $A (P̂k )]rAB tr[P̂i $B (P̂l )]
Hence, the transformation must reduce the normal(101) ization coefficient associated with the state to a value
consistent with the probability of obtaining that outwhich, using (96), gives (97) and (99). The steps come. This condition is
in (101) can be read backwards. Hence, from (97),
we obtain the tensor product structure for describing
rI · Zl p = rl · p for all p ∈ S
(103)
composite systems.
Furthermore, we can consider all these channels taken
We will say that ZA is completely positive iff
together. P
In this case the effective transformation is
given
by
p̃AB → ZA p̃AB
(102)
l Zl . It is necessary that this also belongs
to the allowed set of transformations, Γ, and that it
maps all allowed states of the composite system AB does not change the normalization coefficient associto states which are also allowed states for any di- ated with the state. This second condition can be
mension NB . The only constraint on transforma- written
tion matrices Z is that they transform states in S
 X T
to states in S. This means that probabilities must
(104)
Zl rI = rI
remain bounded by 0 and 1. Hence,
l
1. Z must not increase the normalization coefficient This is equivalent to constraint
of states.
X
tr
$(ρ̂) = tr(ρ̂) for all ρ̂
2. Z must be completely positive.
l

(105)

positive operators can be written as
Condition 2 is necessary since any system could al- Since completely
P
ways be a subsystem of some larger system. The $(ρ̂) = l M̂l ρ̂M̂l† this equation can be shown to be
25

<!-- page 26 -->
equivalent to
X

M̂l† M̂l = Iˆ

(106)

l

which is the usual quantum constraint on superoperators associated with measurements [14, 15].
The two equations (103,104) which constrain the
possible transformations of the state after measurement apply equally well to classical probability theory. This may suggest a new approach to the measurement problem in quantum theory.

9

Infinite dimensional spaces

There are two types of infinite dimensional space countable and continuous dimensional. The countable infinite dimensional spaces are accounted for by
these axioms since such systems are characterized by
the property that any finite subspace obeys quantum
theory. It is not so clear what the status of continuous dimensional spaces is. Such spaces can always
be modeled arbitrarily well by a countable infinite dimensional Hilbert space. However, there are certain
mathematical subtleties associated with the continuous case which we have not considered here. Nevertheless, it is clear that the classical continuous case
violates the axioms even though there are continuous
paths between states since the continuity axiom (Axiom 5) must also apply to finite subspaces (by Axiom
3) and for these there are no continuous transformations.
While continuous dimensional spaces play a role in
some applications of quantum theory it is worth asking whether we expect continuous dimensional spaces
to appear in a truly fundamental physical theory of
nature. Considerations from quantum gravity suggest that space is not continuous at the planck scale
and that the amount of information inside any finite
volume is finite implying that the number of distinguishable states is countable. Given the mathematical difficulties that appear with continuous dimensional Hilbert spaces it is also natural to ask what
our motivation for considering such spaces was in the
first place. Consider a classical particle which can

move along a straight line. If where were not a continuous infinity of distinguishable positions for the
particle then the only way the particle could move
would be to jump from one position to the next. It is
because we do not like such discontinuities in physics
that we imagine that there is a continuous infinity of
distinct positions along the line. However, in quantum theory it is no longer the case that the particle
would need to jump and hence the main motivation
for considering the continuous dimensional case no
longer pertains.
If we do, nevertheless, consider continuous dimensional spaces then there is an interesting respect in
which the quantum case is superior to the classical case. Consider again a particle which can move
along a straight line. Every point on the line represents a distinguishable state for the particle. Take
three points A, B, and C along this line where B is
between A and C. In classical theory, if the particle is to move continuously through the state space
from A to C it must pass through point B. However, to move continuously from A to B it need not
pass through C. Hence, the pairs AB and AC are
on an unequal footing. In quantum theory a particle
can pass directly from the point A to the point C
without going through the points in between along
a continuous trajectory in the state space simply by
going along the Bloch sphere corresponding to this
two-dimensional subspace (such transformations do
not occur in practise since Hamiltonians contain only
local terms). Hence, the pairs AB and AC are on an
equal footing. We can regard statements like “the
particle is at point B” as logical propositions. It is
a very desirable property that pairs of propositions
should be on an equal footing. Thus, in this respect,
quantum theory is superior.
On the other hand, even in the quantum case, continuous dimensional spaces appear to have a topological relationship between infinitesimally displaced
distinguishable states which is different to the topological relationship between finitely displaced distinguishable states. This is hard to reconcile with the
notion that any pair of distinguishable states are on
an equal footing and may be further support for the
case against giving continuous dimensional spaces a
role in any fundamental theory of nature.

26

<!-- page 27 -->
10

Discussion

variables to solve the measurement problem (since
this relies on being able to give the hidden variables
a classical probability interpretation). Second, we
see here how successful a purely instrumentalist approach is in obtaining the structure of quantum theory. Whilst this need not contradict beliefs held by
the realist since he would anyway expect quantum
theory to be consistent with instrumentalist argumentation, it does require some explanation. And,
third, we obtain that the most general evolution is
that of a superoperator. This is capable of taking
pure states to mixed states. Hence, collapse interpretations of quantum theory could be incorporated into
this structure.

We have shown that quantum theory follows from
five very natural axioms. If Axiom 5 (or even just
the word “continuous” in Axiom 5) is dropped we
obtain classical probability theory instead. It is classical probability theory that must have ‘jumps’. If
a 19th century ancestor of Schroedinger had complained about “dammed classical jumps” then he
might have attempted to derive a continuous theory of probability and arrived at quantum theory.
Quantum theory is, in some respects, both superior
to and more natural than classical probability theory
(and therefore classical theories in general) since it
can describe evolution for finite systems in a continuous way. Since nature is quantum, not classical, it
is to be expected that quantum theory is ultimately Acknowledgements
the more reasonable theory.
There are many reasons to look for better axI am very grateful to Chris Fuchs for discussions
iomatic formulations of quantum theory.
that motivated this work and to Jeremy Butterfield,
Philip Pearle, Terry Rudolph, and Jos Uffink for com• Aesthetics. A theory based on reasonable axioms
ments. This work is funded by a Royal Society Uniis more appealing.
versity Research Fellowship.
• A set of reasonable axioms provides us with a
deeper conceptual understanding of a theory and
is therefore more likely to suggest ways in which References
we could extend the domain of the theory or
[1] G. Birkhoff and J. von Neumann, Ann. Math.
modify the axioms in the hope of going beyond
37, 743 (1936).
quantum theory (for example, to develop quantum gravity).
[2] G. W. Mackey, The mathematical foundations of
quantum mechanics (W. A. Benjamin Inc, New
• This approach puts a different slant on the inYork, 1963).
terpretation of quantum theory (see discussion
below).
[3] J. M. Jaunch and C. Piron, Helv. Phys. Acta 36,
• Since the formulation of quantum theory here
is closer to classical probability theory than the
standard formulation, this may motivate new applications and new treatments of the theory of
quantum information.
There are various ways in which this work has a
bearing on interpretational matters. First, if we really believe these axioms to be reasonable then they
would also apply to hidden variables and it would follow that the hidden variable substructure must look
like quantum theory. We could not then use hidden
27

837 (1963); C. Piron, Helv. Phys. Acta 37, 439
(1964).
[4] G. Ludwig, Commun. Math. Phys. 9, 1 (1968),
G. Ludwig, Foundations of quantum mechanics
volumes I and II (Springer-Verlag, New York,
1983 and 1985).
[5] B. Mielnik, Commun. Math. Phys. 9, 55 (1968).
[6] A. Lande, Am. J. Phys. 42, 459 (1974).
[7] D. I. Fivel, Phys. Rev. A 50 2108 (1994).

<!-- page 28 -->
[8] L. Accardi, Il Nuovo Cimento 110B, 685 (1995). [21] H. Boerner, Representations of groups (NorthHolland publishing company, Amsterdam 1963).
[9] N. P. Landsman, Int. J. of Theoretical Phys.
37, 343 (1998) and Mathematical topics between
classical and quantum mechanics (Springer, New
Appendix 1
York, 1998).
[10] B. Coecke, D. Moore, A. Wilce, Current research in operational quantum logic: algebras,
categories, languages (Fundamental theories of
physics series, Kluwer Academic Publishers,
2000), also available on quant-ph/0008019.

We will prove that the property
f (λpA + (1 − λ)pB ) = λf (pA ) + (1 − λ)f (pB ),
(107)

where λ ≥ 0, implies that
X
[12] S. Kochen and E.P. Specher, J. Math and Mech.
f (p) =
aα f (pα )
17, 59 (1967).
α

[11] A. M. Gleason, Annals of Math 6, 885 (1957).

[13] I. Pitowsky, Lecture notes in physics 321 where
(Springer-Verlag, Berlin-Heildelburg 1989).
p=

(108)

X

aα pα
(109)
[14] K. Kraus, States, effects, and operations:
α
Fundamental notions of quantum theory
(Springer-Verlag, Berlin, 1983); B. Schu- if
macher, quant-ph/9604023 (appendix A); J.
pα , p ∈ S for all α
Preskill Lecture notes for physics 229: quantum
information and computation, available at
for all aα where S is the set of allowed p. First note
http://ww.theory.ca.tech.edu/∼preskill/ph229
that putting pA = 0 gives
(see chapter 3).
f (λp) = λf (p)
(110)
[15] M. A. Nielsen and I. L. Chuang, Quantum information and quantum information, (Cambridge
for 0 ≤ λ ≤ 1. We can write γ = 1/λ and p′′ = p/λ.
University Press, 2000).
Then we obtain
[16] R. Schack, private communication.
f (γp′′ ) = γf (p′′ )
(111)
[17] D. Deutsch, private communication.
where 1 ≤ γ. Hence,
[18] W. K. Wootters, Local accessibility of quantum
states, in Complexity, entropy and the physics
f (νp) = νf (p)
(112)
of information edited by W. H. Zurek (AddisonWesley, 1990) and W. K. Wootters, Found. Phys if ν ≥ 0. This only follows from (107) if p, νp ∈ S.
16, 319 (1986).
However, if this is not the case, then the equation
does not correspond to any physical situation. Hence,
[19] S. Weigert, Phys. Rev. Lett. 84, 802 (2000).
we are free to impose that (112) is true for all p.
[20] It has been noted by C. Caves, C. Fuchs and In those cases where p, νp ∈ S is not satisfied the
R. Schack in quant-ph/0104088 that difficulties equation has no physical significance anyway.
in formulating a De Finetti theorem for quaterLet fI pertain to that measurement that simply
nionic quantum theory stem from the fact that checks to see that a non-null result has been recorded
K 6= KA KB .
(we call this the identity measurement). We will
28

<!-- page 29 -->
where n takes only positive integer values, is of the
form K(n) = nα . First put m = n = 1 into (118).
We obtain that K(1) = 0, 1. Put m = 1 into
(118). If K(1) = 0 then K(n) = 0 for all n. But
this is not strictly increasing. Hence we must have
K(1) = 1. The argument n can be factorized into
α
primes: n = pk11 pk22 . . . where pi is the ith prime and
We are free to choose the fiducial measurement cor- the ki ’s are integers. It follows from the completely
responding to the first component of the state vector multiplicative property that
p to be the identity measurement. Hence, reading off
Y
(119)
K ki (pi )
K(n) =
the first component from (113) we obtain
i
X
µ=
aα µα
(114)
Hence, the function K(n) is completely determined
α
by its values at the primes. Now consider two primes
Let α ∈ A± if aα is ±ve and define
p and q. Define α by
X
X
aα µα
(115)
|aα |µα =
ν =µ+
K(p) = pα
(120)
write fI (p) = µ. We define the normalized state
p̃ by µp̃ = p such that fI (p̃) = 1 (using (112)).
We can normalize each of the states in (109) such
that
X
µp̃ =
(113)
aα µα p̃α

α∈A−

α∈A+

Note that K(p) > 1 since K(n) is a strictly increasing
function and hence α > 0. Define a by

We can rearrange (113)
X |aα |µα
X aα µα
µ
p̃ +
p̃α =
p̃α
ν
ν
ν
α∈A−

(116)

K(q) = aq α

α∈A+

(121)

Each coefficient is positive and the coefficients on Introduce the integer t which we will allow to take
any positive value. Then define s by
each side add to 1. Hence we can apply (107)
X |aα |µα
X aα µα
µ
f (p̃) +
f (p̃α ) =
f (p̃α )
ν
ν
ν
α∈A−

ps > q t > ps−1

α∈A+

(117)

From the fact that K(n) is strictly increasing we have

K(ps ) > K(q t ) > K(ps−1 )
Rearranging this using (112) gives (108) as required.
We see that (108) holds whenever the arguments
Hence,
of f in each term correspond to physical states. If
these arguments do not all correspond to physical
pαs > at q αt > pα(s−1)
states then the equation does not correspond to any
physical situation. For mathematical simplicity we Define se by
will impose that (108) still holds in such cases.
pse = q t

Appendix 2

(123)

(124)

(125)

Comparing with (122) we have

se + 1 > s > se > s − 1 > se − 1
In this appendix we show that any strictly increasing function having the completely multiplicaHence, (124) gives
tive property
K(mn) = K(m)K(n),

(122)

(118)
29

pα(es+1) > at q αt > pα(es−1)

(126)

(127)

<!-- page 30 -->
(we have used the fact that α > 0). Using (125) we A3.1
obtain
In this Appendix section we will prove that
pα > at > p−α
(128)
T IW
(131)
ZW
r = rIW for all ZW ∈ Γreversible
W
t
This must be true for all t. However, a can only
I
be bounded from above and below if a = 1. Hence, where r W is the identity measurement for the subreversible
α
is the set of reversible transK(q) = q . This applies to any pair of primes, p and space W and ΓW
α
formations which map states in the subspace W to
q, and hence K(n) = n .
states in W – such transformations must exist by Axiom 3. We can work in the basis for which the transAppendix 3
formations are orthogonal introduced above. Then
we wish to prove
In this appendix we will prove a number of related
T IW
(132)
YW
s = sIW for all YW ∈ Ωreversible
W
important results some of which are used in the main
part of the paper.
Working in this basis we can write any state in the
The set of reversible transformations is represented subspace W as
by the set, Γreversible , of invertible matrices Z in Γ
whose inverses are also in Γ. These clearly form a
(133)
q = asIW + x
representation of a group. In fact, since, by Axiom 5,
I
this group is continuous and the vectors p generated where x is orthogonal to s . The normalization of this
reversible state is fixed by a. Let KW be the number of degrees
by the action of the group remain bounded, Γ
is a representation of a compact Lie group. It can of freedom associated with the subspace W . Once
be sown that all real representations of a compact the normalization coefficient has been fixed there are
Lie group are equivalent (under a basis change) to a KW − 1 degrees of freedom left corresponding to the
real orthogonal representation [21]. Let us perform KW − 1 dimensions of the vector space orthogonal to
I
such a basis change. Under this basis change assume s W for states in W which is spanned by possible x.
There
must be at least one direction in this vector
that Z ∈ Γ is transformed to Y ∈ Ω and pS ∈ S is
space
for
which both x and γx, where γ 6= 1, are pertransformed to q ∈ Q. The formula pmeas = r · p
missible
vectors
(corresponding to allowed states). To
becomes
see this assume the contrary. Thus assume that for
pmeas = s · q
(129) each direction x/|x| there is only one allowed length
of vector. Such a constraint would remove one degree
where s now represents the measurement (and is ob- of freedom leaving KW − 2 degrees of freedom which
tainable from r by a basis change). If a transforma- contradicts our starting point that there are KW − 1
tion device is present then we have
degrees of freedom associated with states with a particular normalization coefficient. Consider such an x
pmeas = sT Y q
(130) for which γx is also permissible. Now
We can regard Y as transforming the state or, alternatively, we can regard it as part of the measurement
apparatus. In this case we have s → Y T s. If we
now restrict our attention to reversible transformations then Y ∈ Ωreversible . But this is an orthogonal
representation and hence Y T ∈ Ωreversible . Therefore,
with this representation, both states q and measurements s are acted on by elements of Ωreversible .

sIW · YW q = sIW · q

(134)

since the reversible transformation YW does not
change the normalization coefficient of the state and
q is in W both before and after the transformation.
Using (133) this becomes

30

asIW · YW sIW + sIW · YW x = asIW · sIW

(135)

<!-- page 31 -->
which map states in W back into W . By
This equation must also apply when x is replaced by of Γreversible
W ′ (1)
the result in A3.2 these transformations must leave
γx.
the basis state pm1 unchanged (where m1 is the first
asIW · YW sIW + γsIW · YW x = asIW · sIW (136) entry of W ) since this is the only normalized state in
W ′ (1) and the complement of W . We can now run
Subtracting these two equations tells us that the sec- the same argument taking W ′ (2) to be our system
ond term on the LHS vanishes. Hence
and so on. In this way we establish that we can find a
IW
IW
IW
IW
(137) transformations ZW which have the desired property.
s ·Y s =s ·s
W

Now, the transformation YW is orthogonal and hence A3.4
length preserving and thus (132) follows.
In this appendix subsection we show that one posIt follows that
sible choice of fiducial measurements are those idenof reY T sI = sI for all Y ∈ Ωreversible
(138) tified in Section 8.2. Consider the set Γreversible
mn
versible transformations that transform states in the
where sI is the identity measurement in this new basis subspace Wmn to states in the same subspace (where
(written as rI in the usual basis). This property is Wmn is the subspace associated with the mth and
to be expected since reversible transformations leave the nth basis vectors). It follows from the property
the normalization coefficient of a state unchanged.
established in A3.2 that
rTn Zmn p = 0

A3.2
It is clearly the case that
ZW p ∈ W

if

p∈W

and ZW ∈ Γreversible
W
(139)

if

p ∈ W mn

(141)

We can regard the transformation device as part of
the measurement apparatus (rather than regarding it
as acting on the state). In this case we have
T
rn → Zmn
rn

It is also the case that

(142)

We can choose two particular transformations Zmnx
and ZW ∈ Γreversible
W
and Zmny to provide us with the two extra needed
(140) fiducial measurements, rmnx and rmny respectively,
for each two-dimensional subspace. The vectors rm ,
where W is the complement subspace of W . This r , r
n
mnx , and rmny must be linearly independent.
follows immediately since p ∈ W iff rIW · p = 0. But It follows from the fact that, for this subspace, the
T IW
if this is true then, since ZW
r = rIW , it is also true group of transformations is equivalent, under a basis
IW
that r · ZW p = 0. Hence, ZW p ∈ W .
change, to the full group of orthogonal rotations in
three dimensions that we can choose Zmnx and Zmny
A3.3
such that this is the case. From (141) we have
ZW p ∈ W

if

p∈W

We will now prove that we can choose ZW such
that ZW pn = pn for n ∈ W . Define W ′ (m) to be
the set containing all the elements of W plus the first
m elements of W . Consider only states constrained to
the subspace W ′ (1) and consider the set Γreversible
of
W ′ (1)
′
reversible transformations which map states in W (1)
back into W ′ (1). The subspace W is a subspace of
W ′ (1). Hence, by Axiom 3, there must exist a subset

rmnx · p = 0 if

p ∈ W mn

(143)

and similarly for rmny .
We will now prove that the N 2 vectors chosen in
this way are linearly independent. We can do this by
showing that each measurement yields information
about the state that none of the others do. First,
the vectors rn are linearly independent of each other

31

<!-- page 32 -->
since there exists a vector (namely pm ) having nonzero overlap with any given rm which has zero overlap with all the other rn . Now we add two fiducial vectors, rmnx and rmny , to each two-dimensional
subspace Wmn that are, by construction, linearly independent of the basis vectors already in that subspace. Since the fiducial measurements pertaining to
one such two-dimensional subspace yield no information about states in any other non-overlapping twodimensional subspace (because of (143))they must be
linearly independent of the fiducial measurements in
those non-overlapping subspaces. What about overlapping two-dimensional subspaces? Consider performing the measurement rmnx on p in Wmn′ where
n′ 6= n. Since p is in Wmn′ it follows from Axiom
3 that the measurement rmnx must be equivalent to
some measurement in this subspace (though only for
states in this subspace). Now, if the state is actually
the basis state pn′ then zero probability would be
recorded. This means that the measurement rmnx ,
when regarded as a measurement on Wmn′ is actually equivalent to a measurement just on the onedimensional subspace Wm . Hence, rmnx does not
yield any information about states in the subspace
Wmn′ that is not given by rm and therefore the measurements rmn′ x and rmn′ y are linearly independent
of it. Hence, the N 2 fiducial measurements are all
necessary to determine the state and are therefore
linearly independent.
A3.5
In this appendix subsection we show that the map
between a pure state and that pure measurement
identifying it is linear and invertible (recall that pure
measurements are defined to be those measurements
which can be obtained by acting on the basis measurement r1 with a reversible transformation). Using
the basis for which reversible transformations are orthogonal (see introduction to this appendix) we can
put
q = asI + u

(144)

s = bsI + v

(145)

for the state, and

for the measurement where u and v are orthogonal to
sI . Since Y T sI = sI and since the group of reversible
transformations, Ωreversible , is orthogonal it follows
that Y sI = sI . Hence, transformations only effect
the components of q and s orthogonal to sI . Using
pmeas = r · p = s · q we obtain
pmeas = k + v · u

(146)

where k = absI · sI .
Now assume that the pure measurement represented by s identifies the pure state represented by
q. Then k + u · v = 1. This probability cannot be
increased by any transformation device. Hence,
vT Y u ≤ vT u for all Y ∈ Ωreversible

(147)

Since the orthogonal transformation Y is length preserving it would appear that the only way to satisfy
this condition is if v is parallel to u. This is indeed
the case and is proven at the end of this appendix subsection. Hence, we can say that the state q = asI + u
is identified by the measurement s = bsI + cu. Now
apply this result to the basis state q1 (this corresponds to p1 ) and the basis measurement s1 (this
corresponds to r1 ). Let C be the linear map that
performs scalar multiplication by a factor µ in the sI
direction and by a factor ν in the subspace orthogonal to sI . We can apply C to q and C −1 to s such
that s1 = q1 = αsI +βu1 by appropriate choice of the
factors µ and ν. The maps C and C −1 commute with
the orthogonal transformations Ωreversible . Hence, in
general, the pure state q = αsI + Y βu1 is identified
by the pure measurement s = αsI + Y βu1 (i.e. represented by the same vector) as Y Y T = I. Since the
basis change and the maps C and C −1 are all linear and invertible it follows that the map from pure
states to the pure measurements identifying them is
linear and invertible.
As promised, we will now prove that v is parallel
to u when a pure measurement s identifies a pure
state q. First consider the basis measurement s1 and
the basis state q1 it identifies. Let Vmn be the vector
space spanned by the fiducial measurement vectors
sm , sn , smnx and smny associated with the mn subspace. It follows from A3.4 that these vector spaces
span the full N 2 dimensional vector space. The state

32

<!-- page 33 -->
q1 can have no projection into the vector space Vmn if
m, n 6= 1 (since s·q1 = 0 for s associated with the mn
subspace). Let Ve be the vector space spanned by the
vector spaces V1n for n = 1 to N . It follows from the
fact that q1 has no projection into Vmn
P for m, n 6= 1
that q1 is in Ve . Now the vector sI = n sn is clearly
in Ve . Let Ve ′ be the vector space in Ve orthogonal to
sI . We can write q1 = asI + u1 where u1 is in the
vector space Ve ′ . Similarly, we can write s1 = bsI +v1 .
′
Define V1n
as the vector space spanned by the fiducial
measurement vectors v1 , vn , v1nx , and v1ny associ′
ated with the subspace 1n. The vector spaces V1n
for
′
e
n = 1 to N span V . Consider orthogonal transformations Y1n which leave states in the 1n subspace.
They will also transform measurements pertaining to
the 1n subspace to measurements still pertaining to
′
this subspace (and thus still in V1n
). Since v1 and
T
′
Y1n v1 are both in V1n we can write (147) as

A3.7
Now we will show that the basis measurements rn
are all pure and, therefore, that all the fiducial measurements of A3.4 are pure. Consider first the case
where N = 2. Then K = 4. The normalized states
(and hence pure states) live in a three dimensional
space (since we can eliminate one variable by normalization). Hence, orthogonal transformations can
be regarded as rotations about an axis. We can write
the basis states as
q1 = αsI + βu1

(149)

q2 = αsI − βu1

(150)

This follows since there exists a continuous orthogonal transformation which takes q1 to q2 . This can
be regarded as a rotation around a great circle. The
T
1n
T 1n
v1 Y1n u1 ≤ v1 u1
(148) orthogonal state q2 must correspond to the opposite
point on this circle where u = −u1 since this is the
′
where u1n
is
the
component
of
u
in
V
.
The
vecpoint
at which s1 · q stops decreasing and starts in1
1
1n
′
tor space V1n
is three dimensional and the action of creasing again. Now, we have already that
the group of orthogonal transformations in the 1n
s1 = αsI + βu1
(151)
subspace on u1 is to sweep out a sphere (since these
transformations are length preserving). Hence, conWe have not yet proven that s2 (corresponding to r2 )
dition (148) can only be satisfied for all rotations Y1n
is
pure. However, we know that s1 + s2 = sI so we
′
if u1n
1 is parallel to v1 . The vector spaces V1n span
can
write
all of Ve ′ and hence u1 has no component which is
perpendicular to v1 . This means that v1 is parallel
s2 = α′ sI − βu1
(152)
to u1 . We complete the proof by noting that a general pure measurement can be written v = Y v1 and with α + α′ = 1. It then follows from s1 · q2 =
s2 ·q1 = 0 that α = α′ = 1/2. Hence, s2 is pure. This
identifies the pure state u = Y u1 .
proof can be applied to the general N case by considering only a two dimensional subspace. It follows
A3.6
from Axiom 3 that there must exist a set of invertIt is easy to prove that D = DT . We chose a ible transformations which transform states in the 1n
set of pure fiducial states and we chose the fiducial subspace to states in the same subspace. As shown in
measurements to be the set of pure measurements A3.1, these leave sIW1n invariant (this is the identity
that identify these states. Hence, if we represent the measurement vector for the 1n subspace). Hence, we
fiducial states by a set of vectors ql then, as proven can replace sI by sIW1n throughout the above proof if
in A3.5, we can represent the fiducial measurements we are only considering transformations in this subby the the same vectors sk = qk . The matrix element space. It follows that we can transform s1 to sn and
Dkl is equal to the probability when the kth fiducial hence the basis measurements are all pure.
measurement is performed on the lth fiducial state.
Hence we can transform s1 to any smnx by first
This is equal to qk · ql and hence D = DT .
transforming by a reversible transformation to sn and
33

<!-- page 34 -->
A
then applying the reversible transformation of A3.4 eral the projector P̂m
⊗ Q̂B corresponds to preparing
to obtain smnx . Similar remarks apply to smny .
the basis state P̂m at A and the general pure state
Q̂B at B. Now consider the subspace spanned by
A
the projectors P̂m
⊗ Q̂B (m = 1 to NA ) in which we
B
Appendix 4
prepare Q̂ at B. A fiducial set for this subspace is
P̂kA ⊗ Q̂B where k = 1 to KA . If these fiducial measurements are made on a state R̂A ⊗ Q̂B where R̂A is
In this appendix we will show that the projector
a projector at A then we would get the same results
P̂iA ⊗ P̂jB can correspond to the measurement of the
B
A
′
joint probability of obtaining a positive outcome for as if the fiducial measurements P̂k ⊗ Q̂ were made

fiducial measurements i at A and j at B, and to the
state when the ith fiducial state is prepared at A and
the jth fiducial state is prepared at B. First, note
that we can prepare NA NB distinguishable states for
the composite system by preparing basis state m at
A and basis state n at B. Since the composite system has N = NA NB this represents a complete set
of basis states. Further, since K(1) = 1 all basis
states must be pure (as noted at the end of Section
8.1). Hence, we can choose these basis states to correspond to the basis states of our Hilbert space |mni
or, equivalently, |mi ⊗ |ni. As operators these baA
sis states are P̂m
⊗ P̂nB where m (n) only runs over
the first NA (NB ) values (the remaining values corresponding to the other fiducial projectors).

B

on the state R̂A ⊗ Q̂′ . Hence, in both cases the
preparation at A is the same. Thus, the pure state
R̂A ⊗ Q̂B corresponds to the case where a particular pure state R̂A is is prepared at A and the pure
state Q̂B is prepared at B. An analogous argument
to that above can be used to show that, regarded as
a measurement, the projector R̂A ⊗ Q̂B corresponds
to measuring the joint probability with setting R̂A
at end A and setting Q̂B at end B. Applied to the
fiducial projectors, P̂kA ⊗ P̂lB , this proves our result.

Now consider the NB dimensional subspace with
basis states |1i ⊗ |ni (n = 1 to NB ). This subspace
corresponds to the case where system A is prepared
in basis state 1 and system B is prepared in any state.
A full set of fiducial projectors can be formed for this
subspace. These will take the form P̂1A ⊗ P̂lB where
l = 1 to KB (i.e. runs over the all values, not just
the basis labels). We can do the same for the case
where basis state 2 is prepared at A. Then we have
the fiducial projectors P̂2A ⊗ P̂lB for the subspace 2n
(n = 1 to NB ). Indeed, we can do this for the general case in which the basis state m is prepared at A.
Now consider the pure state P̂1A ⊗ Q̂B where Q̂B is
some arbitrary projector at B. This state is in the 1n
(n = 1 to NB ) subspace and we can perform the fiducial measurements P̂1A ⊗ P̂lB in this subspace to fully
characterize this state. The probabilities obtained in
making these fiducial measurements will be the same
as if we prepared the state P̂2A ⊗ Q̂B and made the
fiducial measurements P̂2A ⊗ P̂lB and hence this corresponds to the same preparation at B. Hence, in gen34
