---
type: paper
date: 2010-04-09
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1004.1483v4)
reviewed: false
---

# A derivation of quantum theory from physical requirements

Machine-generated and unreviewed text extraction of arXiv:1004.1483v4
(17 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1004.1483v4>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
A derivation of quantum theory from physical requirements
Lluı́s Masanes
ICFO-Institut de Ciencies Fotoniques, Mediterranean Technology Park, 08860 Castelldefels (Barcelona), Spain

Markus P. Müller

arXiv:1004.1483v4 [quant-ph] 16 May 2011

Institute of Mathematics, Technical University of Berlin, 10623 Berlin, Germany,
Institute of Physics and Astronomy, University of Potsdam, 14476 Potsdam, Germany and
Perimeter Institute for Theoretical Physics, 31 Caroline Street North, Waterloo, ON N2L 2Y5, Canada.
(Dated: October 5, 2010)
Quantum theory is usually formulated in terms of abstract mathematical postulates, involving
Hilbert spaces, state vectors, and unitary operators. In this work, we show that the full formalism of
quantum theory can instead be derived from five simple physical requirements, based on elementary
assumptions about preparation, transformations and measurements. This is more similar to the
usual formulation of special relativity, where two simple physical requirements – the principles of
relativity and light speed invariance – are used to derive the mathematical structure of Minkowski
space-time. Our derivation provides insights into the physical origin of the structure of quantum
state spaces (including a group-theoretic explanation of the Bloch ball and its three-dimensionality),
and it suggests several natural possibilities to construct consistent modifications of quantum theory.

I.

INTRODUCTION

Quantum theory is usually formulated by postulating
the mathematical structure and representation of states,
transformations, and measurements. The general physical consequences that follow (like violation of Bell-type
inequalities [1], the possibility of performing state tomography with local measurements, or factorization of integers in polynomial time [2]) come as theorems which use
the postulates as premises. In this work, this procedure
is reversed: we impose five simple physical requirements,
and this suffices to single out quantum theory and derive
its mathematical formalism uniquely. This is more similar to the usual formulation of special relativity, where
two simple physical requirements —the principles of relativity and light speed invariance— are used to derive the
mathematical structure of Minkowski space-time and its
transformations.
The requirements can be schematically stated as:
1. In systems that carry one bit of information, each
state is characterized by a finite set of outcome
probabilities.
2. The state of a composite system is characterized
by the statistics of measurements on the individual
components.
3. All systems that effectively carry the same amount
of information have equivalent state spaces.
4. Any pure state of a system can be reversibly transformed into any other.
5. In systems that carry one bit of information, all
mathematically well-defined measurements are allowed by the theory.
These requirements are imposed on the framework of
generalized probabilistic theories [3–9], which already as-

sumes that some operational notions (preparation, mixture, measurement, and counting relative frequencies of
measurement outcomes) make sense. Due to its conceptual simplicity, this framework leaves room for an infinitude of possible theories, allowing for weaker- or strongerthan-quantum non-locality [6, 10–14]. In this work, we
show that quantum theory (QT) and classical probability theory (CPT) are very special among those theories:
they are the only general probabilistic theories that satisfy the five requirements stated above.
The non-uniqueness of the solution is not a problem,
since CPT is embedded in QT, thus QT is the most general theory satisfying the requirements. One can also
proceed as Hardy in [4]: if Requirement 4 is strengthened
by imposing continuity of the reversible transformations,
then CPT is ruled out and QT is the only theory satisfying the requirements. This strengthening can be justified
by the continuity of time evolution of physical systems.
It is conceivable that in the future, another theory may
replace or generalize QT. Such a theory must violate at
least one of our assumptions. The clear meaning of our
requirements allows to straightforwardly explore potential features of such a theory. The relaxation of each of
our requirements constitutes a different way to go beyond
QT.
The search for alternative axiomatizations of quantum
theory (QT) is an old topic that goes back to Birkhoff
and von Neumann [8], and has been approached in many
different ways: extending propositional logic [7, 8], using
operational primitives [3–6, 9], searching for informationtheoretic principles [5, 6, 10, 11, 19–21], building upon
the phenomenon of quantum nonlocality [6, 10–13]. Alfsen and Shultz [22] have accomplished a complete characterization of the state spaces of QT from a geometric
point of view, but the result does not seem to have an
immediate physical meaning. In particular, the fact that
the state space of a generalized bit is a three-dimensional
ball is an assumption there, while here it is derived from

<!-- page 2 -->
2
physical requirements.
This work is particularly close to [4, 19], from where it
takes some material. More concretely, the multiplicativity of capacities and the Simplicity Axiom from [4] are
replaced by Requirement 5. In comparison with [19], the
fact that each state of a generalized bit is the mixture
of two distinguishable ones, the maximality of the group
of reversible transformations and its orthogonality, and
the multiplicativity of capacities, are also replaced by
Requirement 5.
Summary of the paper. Section II contains an introduction to the framework of generalized probabilistic theories, where some elementary results are stated without
proof. In Section III the five requirements and their significance are explained in full detail. Section IV is the
core of this work. It contains the characterization of all
theories compatible with the requirements, concluding
that the only possibilities are CPT and QT. The Conclusion (Section V) recapitulates the results and adds some
remarks. The Appendix contains all lemmas and their
proofs.

II.

GENERALIZED PROBABILISTIC
THEORIES

In CPT there can always be a joint probability distribution for all random variables under consideration. The
framework of generalized probabilistic theories (GPTs),
also called convex operational framework, generalizes this
by allowing the possibility of random variables that cannot have a joint probability distribution, or cannot be simultaneously measured (like noncommuting observables
in QT).
This framework assumes that at some level there is a
classical reality, where it makes sense to talk about experimentalists performing basic operations such as: preparations, mixtures, measurements, and counting relative
frequencies of outcomes. These are the primary concepts
of this framework. It also provides a unified way for all
GPTs to represent states, transformations and measurements. A particular GPT specifies which of these are
allowed, but it does not tell their correspondence with
actual experimental setups. On its own, a GPT can still
make nontrivial predictions like: the maximal violation
of a Bell inequality [1], the complexity-theoretic computational power [2, 18], and in general, all informationtheoretic properties of the theory [6].
The framework of GPTs can be stated in different
ways, but all lead to the same formalism [3–9]. This formalism is presented in this section at a very basic level,
providing some elementary results without proofs.

A.

States

Definition of system. To a setup like FIG. 1 we associate a system if for each configuration of the prepara-

release button

outcomes x and x̄

physical system
ψ

T

x

FIG. 1: General experimental set up. From left to right
there are the preparation, transformation and measurement
devices. As soon as the release button is pressed, the preparation device outputs a physical system in the state specified
by the knobs. The next device performs the transformation
specified by its knobs (which in particular can be “do nothing”). The device on the right performs the measurement
specified by its knobs, and the outcome (x or x̄) is indicated
by the corresponding light.

tion, transformation and measurement devices, the relative frequencies of the outcomes tend to a unique probability distribution (in the large sample limit).
The probability of a measurement outcome x is denoted by p(x). This outcome can be associated to a
binary measurement which tells whether x happens or
not (this second event x̄ has probability p(x̄) = 1 − p(x)).
The above definition of system allows to associate to each
preparation procedure a list of probabilities for the outcomes of all measurements that can be performed on a
system. As we show in Subsection IV C below, our requirements imply that all these probabilities p(x) are determined by a finite set of them; the smallest such set is
used to represent the state

  0
ψ
1
 p(x1 )   ψ 1 


 
ψ =  ..  =  ..  ∈ S ⊂ Rd+1 .
(1)
 .   . 
p(xd )
ψd
The measurement outcomes that characterize the state
x1 , . . . , xd are called fiducial, and in general, there is more
than one set of them (for example, a 12 -spin particle in QT
is characterized by the spin in any 3 linearly-independent
directions). Note that each of the fiducial outcomes can
correspond to a different measurement. The redundant
component ψ 0 = 1 is reminiscent of QT, where one of the
diagonal entries of a density matrix is redundant, since
they sum up to 1. In fact ψ 0 6= 1 is sometimes used
to represent unnormalized states, but not in this paper,
where only normalized states are considered. The redundant component ψ 0 allows to use the tensor-product
formalism in composite systems (Subsection II D), which
simplifies the notation.
The set of all allowed states S is convex [23], because
if ψ1 , ψ2 ∈ S then one can prepare ψ1 with probability q
and ψ2 with probability 1 − q, effectively preparing the
state qψ1 +(1−q)ψ2. The number of fiducial probabilities
d is equal to the (affine) dimension of S, otherwise one
fiducial probability would be functionally related to the

<!-- page 3 -->
3
others, and hence redundant.
Suppose there is a Rd+1 -vector ψ ∈
/ S which is in the
topological closure of S – that is, ψ can be approximated
by states ψ ′ ∈ S to arbitrary accuracy. Since there is
no observable physical difference between perfect preparation and arbitrarily good preparation, we will consider ψ
to be a valid state and add it to the state space. This does
not change the physical predictions of the theory, but it
has the mathematical consequence that state spaces become topologically closed. Since state vectors (1) are
bounded, and we are in finite dimensions (shown in Subsection IV C), state spaces S are compact convex sets [23].
The pure states of a state space S are the ones that
cannot be written as mixtures: ψ 6= qψ1 + (1 − q)ψ2 with
ψ1 6= ψ2 and 0 < q < 1. Since S is compact and convex,
all states are mixtures of pure states [23].
B.

Measurements

The probability of measurement outcome x when
the system is in state ψ ∈ S is given by a function
Ωx (ψ). Suppose the system is prepared in the mixture
qψ1 + (1 − q)ψ2 , then the relative frequency of outcome
x does not depend on whether the label of the actual
preparation ψk is ignored before or after the measurement, hence

Ωx qψ1 + (1 − q)ψ2 = q Ωx (ψ1 ) + (1 − q) Ωx (ψ2 ) .

This means that the function Ωx is affine on S. The
redundant component ψ 0 in (1) allows to write this function as a linear map Ωx : Rd+1 → R [3, 6].
An effect is a linear map Ω : Rd+1 → R such that
Ω(ψ) ∈ [0, 1] for all states ψ ∈ S. Every function Ωx associated to an outcome probability p(x) is an effect. The
converse is not necessarily true: the framework of GPTs
allows to construct theories where some effects do not
represent possible measurement outcomes. These restrictions are analogous to superselection rules, where some
(mathematically well-defined) states are not allowed by
the physical theory. This is related to Requirement 5.
A tight effect Ω is one for which there are two states
ψ0 , ψ1 ∈ S satisfying Ω(ψ0 ) = 0 and Ω(ψ1 ) = 1.
An n-outcome measurement is specified by n effects
Ω1 , . . . , Ωn such that Ω1 (ψ) + · · · + Ωn (ψ) = 1 for all
ψ ∈ S. The number Ωa (ψ) is the probability of outcome
a when the measurement is performed on the state ψ.
The states ψ1 , . . . , ψn are distinguishable if there is an
n-outcome measurement such that Ωa (ψb ) = δa,b , where
δa,b = 1 if a = b, and δa,b = 0 if a 6= b.
The capacity of a state space S is the size of the largest
family of distinguishable states, and is denoted by c. This
is the amount of classical information that can be transmitted by the corresponding type of system, in a singleshot error-free procedure. (In QT the capacity of a system is the dimension of its corresponding Hilbert space;
which must not be confused with the dimension of the
state space d = c2 − 1, that is, the set of c × c complex

matrices that are positive and have unit trace.) A complete measurement on S is one capable of distinguishing
c states.
C.

Transformations

Each type of system has associated to it: a state space,
a set of measurements, and a set of transformations. A
transformation T is a map T : S → S. Similarly as
for measurements, if a state is prepared as a mixture
qψ1 + (1 − q)ψ2 , it does not matter whether the label of
the actual preparation ψk is ignored before or after the
transformation. Hence
T (qψ1 + (1 − q)ψ2 ) = qT (ψ1 ) + (1 − q)T (ψ2 ) ,
which implies that T is an affine map. The redundant
component ψ 0 in (1) allows to extend T to a linear map
T : Rd+1 → Rd+1 [3, 6].
A transformation T is reversible if its inverse T −1 exists and belongs to the set of transformations allowed
by the theory. The set of (allowed) reversible transformations of a particular state space S forms a group G.
For the same reason as for the state space itself, we will
assume that the group of reversible transformations is
topologically closed. Previously we have seen that a state
space S is bounded, hence the corresponding group of
transformations G is bounded, too. In summary, groups
of transformations are compact [24].
D.

Composite systems

Definition of composite system. Two systems A, B constitute a composite system, denoted AB, if a measurement for A together with a measurement for B uniquely
specifies a measurement for AB. This means that if x and
y are measurement outcomes on A and B respectively,
the pair (x, y) specifies a unique measurement outcome
on AB, whose probability distribution p(x, y) does not
depend on the temporal order in which the subsystems
are measured.
The fact that subsystems are themselves systems implies that each has a well-defined reduced state ψA , ψB
which does not depend on which transformations and
measurements are performed on the other subsystem (see
definition of system in Subsection II A). This is often referred to as no-signaling. Let x1 , . . . , xdA be the fiducial
measurements of system A, and y1 , . . . , ydB the ones of
B. The no-signaling constraints are
p(xi ) = p(xi , yj ) + p(xi , ȳj )
p(yi ) = p(xi , yj ) + p(x̄i , yj )

(2)

for all i, j.
An assumption which is often postulated additionally
in the GPT context is Requirement 2, which says that the
state of a composite system is completely characterized

<!-- page 4 -->
4
by the statistics of measurements on the subsystems, that
is, p(x, y). This and no-signaling (2) imply that states
in AB can be represented on the tensor product vector
space [3] as


1


..


.


 p(xi ) 




..


.
dA +1

⊗ RdB +1 . (3)
ψAB = 
 p(yj )  ∈ SAB ⊂ R
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
 p(xi , yj ) 


..
.
The joint probability of two arbitrary local measurement
outcomes x, y is given by
p(x, y) = (Ωx ⊗ Ωy )(ψAB ) ,

(4)

where Ωx is the effect representing x in A, that is
p(x) = Ωx (ψA ), and analogously for Ωy [3]. (The term
“local” is used when referring to subsystems, and has
nothing to do with spatial locations.) In other words,
A
if {ΩA
1 , . . . , Ωn } is an n-outcome measurement on A,
and {ΩB
,
.
.
.
,
ΩB
1
m } is an m-outcome measurement on
A
B, then {Ωa ⊗ ΩB
b | a = 1, . . . , n ; b = 1, . . . , m} defines a
measurement on AB with nm outcomes. Local transformations act on the global state as
ψAB → (TA ⊗ TB )(ψAB ) ,

(5)

where TA is the matrix that represents the transformation in A, and analogously for TB [3]. The reduced states




1
1
 .. 
 .. 


 . 
 , ψB =  .  ,
ψA = 
(6)
 p(yj ) 
 p(xi ) 




..
..
.
.

are obtained from ψAB by picking the right components
(3). Alternatively, reduced states can be defined by
ΩA (ψA ) = (ΩA ⊗ 1)(ψAB ) for any effect ΩA in A, where
0
1(ψB ) = ψB
is the unit effect. The reduced state ψA
must belong to the state space of subsystem A, denoted
SA , and any state in SA must be the reduction of a state
from SAB . (Analogously for subsystem B.) This implies
that all product states
ψAB = ψA ⊗ ψB

(7)

are contained in SAB [3], and similarly, all tensor products of local measurements and transformations are allowed on AB.
Given two fixed state spaces SA and SB , the previous
discussion imposes constraints on the state space of the
composite system SAB . However, there are still many different possible joint state spaces SAB , and some of them

allow for larger violations of Bell inequalities than QT. In
fact, this has been extensively studied [5, 6, 10–14], and
is one of the reasons for the popularity of generalized
probabilistic theories.
Nothing prevents Bob’s system from being composite
itself; hence one can recursively extend the definition of
composite system and formulas (3), (4), (5), and (7) to
more parties.

E.

Equivalent state spaces

Let L : S → S ′ be an invertible affine map. If all
states are transformed as ψ → L(ψ), and all effects on
S are transformed as Ω → Ω ◦ L−1 , then the outcome
probabilities Ω(ψ) are kept unchanged. Analogously, if
all transformations on S are mapped as T → L ◦ T ◦ L−1
then their action on the states is the same. The new
state space S ′ , together with the transformed effects and
transformations, is then just a different representation of
S. In this case, we call S and S ′ equivalent. In the new
representation, the entries of ψ need not be probabilities
as in (1), but it may have other advantages. In this work,
several representations are used.
In the standard formalism of QT, states are represented by density matrices, however they can also be
represented as in (1).
Changing the set of fiducial measurements is a particular type of L-transformation. For example, if the components of the Bloch vector (of a quantum spin- 21 particle)
correspond to spin measurements in non-orthogonal directions, then the Bloch sphere becomes an ellipsoid.

F.

Instances of generalized probabilistic theories

QT is an instance of GPT, and can be specified as
follows. The state space Sc with capacity c is equivalent
to the set of complex c × c-matrices ρ such that ρ ≥ 0
and trρ = 1. This set has dimension dc = c2 − 1, and
its pure states are rank-one. The effects on Sc have the
form Ω(ρ) = tr(M ρ), where M is a complex c×c-matrix
such that 0 ≤ M ≤ I. The reversible transformations
act as ρ → V ρV † with V ∈ SU(c). The capacity of a
composite system AB is the product of the capacities for
the subsystems cAB = cA cB .
CPT is another instance of GPT, and can be specified as follows. The state space Sc with capacity c is
equivalent to the set of c-outcome probability distributions [p(1), . . . , p(c)], which has dimension dc = c − 1
(in geometric terms, each Sc is a simplex). The pure
states are the deterministic distributions p(a) = δa,b with
b = 1, . . . , c. The c-outcome measurement with effects
Ωa (ψ) = p(a) for a = 1, . . . , c, distinguishes the c pure
states, hence it is complete. Any other measurement is a
function of this one. The reversible transformations act
by permuting the entries of the state [p(1), . . . , p(c)]. The
capacity of a composite system is also cAB = cA cB . Note

<!-- page 5 -->
5
that CPT can be obtained by restricting the states of QT
to diagonal matrices. In other words, CPT is embedded
in QT.
An instance of GPT that is not observed in nature
is generalized no-signaling theory [6], colloquially called
boxworld. By definition, state spaces contain all correlations (3) satisfying the no-signaling constraints (2). Such
state spaces have finitely many pure states, and some of
them violate Bell inequalities stronger than any quantum
state [12]. The effects in boxworld are all generated by
products of local effects. The group of reversible transformations consists only of relabellings of local measurements and their outcomes, permutations of subsystems,
and combinations thereof [14].
III.

THE REQUIREMENTS

This section contains the precise statement of the requirements, each followed by explanations about its significance.
Requirement 1 (Finiteness). A state space with capacity c = 2 has finite dimension d.
If this did not hold, the characterization of a state of
a generalized bit would require infinitely many outcome
probabilities, making state estimation impossible. It is
shown below that this requirement, together with the
others, implies that all state spaces with finite capacity
c have finite dimension.
Requirement 2 (Local tomography). The state of a
composite system AB is completely characterized by the
statistics of measurements on the subsystems A, B.
In other words, state tomography [3] can be performed
locally. This is equivalent to the constraint
(dAB + 1) = (dA + 1)(dB + 1)

(8)

[3, 4]. This requirement can be recursively extended to
more parties by letting subsystems A, B to be themselves
composite.
Requirement 3 (Equivalence of subspaces). Let Sc and
Sc−1 be systems with capacities c and c − 1, respectively.
If Ω1 , . . . , Ωc is a complete measurement on Sc , then the
set of states ψ ∈ Sc with Ωc (ψ) = 0 is equivalent to Sc−1 .
The notions of complete measurements and equivalent
state spaces are defined in Subsections II B and II E. In
particular, equivalence of Sc−1 and
′
Sc−1
:= {ψ ∈ Sc : Ωc (ψ) = 0} ⊂ Sc

(9)

implies that all measurements and reversible transformations on one of them can be implemented on the other.
This requirement, first introduced in [4], implies that
all state spaces with the same capacity are equivalent: if
Sc−1 and S̃c−1 are state spaces with capacity c − 1, then

both are equivalent to (9), hence they are equivalent to
each other. In other words, the only property that characterizes the type of system is the capacity for carrying
information. If we start with Sc and apply Requirement 3
recursively, we get a more general formulation: consider
any subset of outcomes {a1 , . . . , ac′ } ⊆ {1, . . . , c} of the
complete measurement Ω1 , . . . , Ωc , then the set of states
ψ ∈ Sc with
Ωa1 (ψ) + · · · + Ωac′ (ψ) = 1

(10)

is equivalent to the state space Sc′ with capacity c′ .
This provides an onion-like structure for all state spaces
S1 ⊂ S2 ⊂ S3 ⊂ · · ·
The particular structure of QT simplifies the task of
assigning a state space to a physical system or experimental setup. It is not necessary to consider all possible
states of the system, but instead, the relevant ones for
the context being analyzed. For example, an atom is
sometimes modeled with a state space having two distinguishable states (c = 2), even though its constituents
have many more degrees of freedom. In particular, if we
know that only two energy levels are populated with nonzero probability, we can ignore all others and effectively
get a genuine quantum 2-level state space. In a theory
where this is not true, the effective state space might
depend on how many unpopulated energy levels are ignored, or on the detailed internal state of the electron,
for example. In order to avoid pathologies like this, we
postulate Requirement 3.
Requirement 4 (Symmetry). For every pair of pure
states ψ1 , ψ2 ∈ S there is a reversible transformation G
mapping one onto the other: G(ψ1 ) = ψ2 .
The set of reversible transformations of a state space
Sc forms a group, denoted Gc . This group endows Sc with
a symmetry, which makes all pure states equivalent. A
group Gc is said to be continuous if it is topologically connected: any transformation is the composition of many
infinitesimal ones [24]. Hardy invokes the continuity of
time-evolution in physical systems to justify the continuity of reversible transformations [3, 4]; in this case,
state spaces Sc must have infinitely-many pure states;
this rules out CPT and singles out QT. However, all the
analysis in this work is done without imposing continuity, since we find it very interesting that the only theory
with state spaces having finitely-many pure states, and
satisfying the requirements, is CPT.
Requirement 5 (All measurements allowed). All effects
on S2 are outcome probabilities of possible measurements.
It is shown below that, in combination with the other
requirements, this implies that all effects on all state
spaces (with arbitrary c) appear as outcome probabilities
of measurements in the resulting theory. Note that Requirement 5 has non-trivial consequences in conjunction
with the other requirements: adding effects as allowed
measurements to a physical theory extends the applicability of Requirement 3.

<!-- page 6 -->
6

Requirement 5’ [34]. If a state is not completely
mixed, then there exists at least one state that can be
perfectly distinguished from it.
IV.

CHARACTERIZATION OF ALL THEORIES
SATISFYING THE REQUIREMENTS
A.

The maximally-mixed state

We use the following notation: the system with capacity c has state space Sc with dimension dc and group
of reversible transformations Gc . The group Gc is compact (Section II C), and hence, has a normalized invariant
Haar measure [26]. This allows to define the maximallymixed state
Z
(11)
G(ψ) dG ∈ Sc ,
µc =
Gc

where ψ ∈ Sc is an arbitrary pure state. It follows from
Requirement 4 that the resulting state µc does not depend on the choice of the pure state ψ. By construction,
the maximally-mixed state is invariant:
G(µc ) = µc for all G ∈ Gc .

(12)

Moreover, Lemma 1 shows that it is the only invariant
state in Sc (this lemma and all others are stated and
proven in the appendix).
B.

The generalized bit

A generalized bit is a system with capacity two. For
any state ψ ∈ S2 in the standard representation (1), its
Bloch representation is defined by


p(x1 ) − µ12


..
d
ψ̂ = 2 
(13)
 ∈ Ŝ2 ⊂ R 2 .
.
p(xd2 ) − µd22

States in the Bloch representation do not have the redundant component ψ 0 , so equations (4, 5, 7) become
less simple. The invertible map L : S2 → Ŝ2 is affine
but not linear; hence, effects Ω in the Bloch representation (Ω̂ = Ω ◦ L−1 ) are affine but not necessarily linear.
The same applies to transformations (Ĝ = L ◦ G ◦ L−1 ),
however, the maximally-mixed state in the Bloch representation is the null vector µ̂2 = 0, therefore (12) becomes Ĝ(0) = 0, which implies that Ĝ acts linearly (as
a matrix).

ψ2

S2

ψone

e =

ψone

Ωon

S2

1

ψmix

1

=

e =

Ω

1 ψ1

Ωon

For completeness, we would like to mention that Requirement 5 can be replaced by the following postulate,
which has first been put forward in an interesting paper
that appeared after completion of this work [34]. It calls
a state “completely mixed” if it is in the relative interior
of state space. See Lemma 9 in the appendix for how the
proof of our main result has to be modified in this case.

FIG. 2: The left figure is a state space whose boundary consists of facets (like Ω = 1). Each facet contains infinitely many
states (Ω = 1 contains ψ1 , ψ2 and all ψmix = qψ1 + (1 − q)ψ2 ).
The right figure is a state space whose boundary has no
facets. Any state space has supporting hyperplanes containing a unique state (like Ωone = 1 in both figures).

Theorem 1. A state in Ŝ2 is pure if and only if it belongs
to the boundary ∂ Ŝ2 .
Proof. In any convex set, pure states belong to the
boundary [23]. Let us see the converse.
It is shown in [27] that any compact convex set has
a supporting hyperplane containing exactly one point of
the set. Translated to our language: there is a tight effect
Ω̂one on Ŝ2 such that only one state ϕ̂one ∈ Ŝ2 satisfies
Ω̂one (ϕ̂one ) = 1; this is illustrated in FIG. 2. According to Requirement 5, the effect Ω̂one corresponds to a
valid measurement outcome, and so does 1̂ − Ω̂one , where
1̂(ψ̂) = 1 for all ψ̂ ∈ Ŝ2 . Thus, the two effects Ω̂one and
1̂ − Ω̂one define a complete measurement on Ŝ2 . Imposing Requirement 3 on the single outcome Ω̂one constrains
the state space with unit capacity Ŝ1 to contain only one
state.
Suppose there is a point in the boundary ϕ̂mix ∈ ∂ Ŝ2
which is not pure: ϕ̂mix = q ϕ̂1 + (1 − q)ϕ̂2 with ϕ̂1 6=
ϕ̂2 and 0 < q < 1. Every point in the boundary of a
compact convex set has a supporting hyperplane which
contains it [23]. In our language: there is a tight effect
Ω̂ on Ŝ2 such that Ω̂(ϕ̂mix ) = 1. The affine function Ω̂
is bounded: Ω̂(ϕ̂) ≤ 1 for any ϕ̂ ∈ Ŝ2 , which implies
Ω̂(ϕ̂1 ) = Ω̂(ϕ̂2 ) = 1; this is illustrated in FIG. 2. Like
Ω̂one , the effect Ω̂ defines a complete measurement, and
Requirement 3 can be imposed on the single outcome Ω̂,
implying that Ŝ1 contains more than one state. This is
in contradiction with the previous paragraph; hence, all
points in the boundary are pure.
For the case d2 = 1, the state space S2 is a segment
(a 1-dimensional ball), hence the previous and next theorems are trivial. For d2 > 1, the previous theorem implies
that S2 contains infinitely-many pure states. The next
theorem recovers the (quantum-like) Bloch sphere with
a yet unknown dimension d2 .
Theorem 2. There is a set of fiducial measurements for
which Ŝ2 is a d2 -dimensional unit ball.
Proof. Lemma 2 shows that there is an invertible real
matrix S such that for each Ĝ ∈ Ĝ2 the matrix S ĜS −1

<!-- page 7 -->
7
is orthogonal. Let us redefine the set Ŝ2 by transforming the states as ϕ̂ → ϕ̂′ = qS ϕ̂, where the number
q > 0 is chosen such that all pure states are unit vectors |ϕ̂′ |2 = ϕ̂′T ϕ̂′ = 1. This is possible because in the
transformed state space, all pure states are related by
orthogonal matrices (SGS −1 ) which preserve the norm.
Since Theorem 1 also applies to the redefined set Ŝ2′ , it
must be a unit ball. In what follows we define a new set of
fiducial measurements x′i such that the Bloch representation (13) associated to the new fiducial probabilities
p(x′i ) coincides with the redefinition ϕ̂′ .
Requirement 5 tells that in Ŝ2′ , all tight effects are allowed measurements. For each unit vector ν̂ ∈ Rd2 the
function Ω̂ν̂ (ϕ̂′ ) = (1 + ν̂ T ϕ̂′ )/2 is a tight effect on the
unit ball, and conversely, all tight effects on the unit ball
are of this form. The new set of fiducial measurements
x′i has effects Ω̂x′i = Ω̂ν̂i , where

 
 
0
1
0
0
0
1
 
 
 
ν̂1 =  .  , ν̂2 =  .  , . . . , ν̂d2 =  . 
 .. 
 .. 
 .. 


0

(14)

1

0

is a fixed orthonormal basis for Rd2 . For any state ϕ̂′
the new fiducial probabilities are p(x′i ) = Ωx′i (ϕ̂′ ) =
(1 + ϕ̂′i )/2, which implies ϕ̂′i = 2[p(x′i ) − 1/2]. This is
just (13) with the new fiducial measurements (note that
µ̂′2 = 0 and µ′i
2 = Ω̂x′i (0) = 1/2).

capacity c there is a value of m such that c ≤ cm , hence
by Requirement 3 we have Sc ⊂ S2×m , which implies that
Sc is finite-dimensional.
In QT, the maximally-mixed state (11) has two convenient properties. First property: if µA and µB are the
maximally-mixed states of systems A and B, then the
maximally-mixed state of the composite system AB is
µAB = µA ⊗ µB .

Second property: in the state space Sc , there are c pure
distinguishable states ψ1 , . . . , ψc ∈ Sc such that
c

1X
ψa .
µc =
c a=1

Ωϕ (ψ) = (1 + ϕ̂ ψ̂)/2 ,
T

(15)

such that Ω̂ϕ (ϕ̂) = 1 and Ω̂ϕ (−ϕ̂) = 0. In summary,
there is a correspondence between tight effects and pure
states in S2 , and each pure state belongs to a distinguishable pair {ϕ̂, −ϕ̂}.
C.

Capacity and dimension

Requirements 1, 2 and 3 imply that a state space with
finite capacity c has finite dimension dc , which generalizes
Requirement 1. To see this, consider a system composed
of m generalized bits, with state space denoted by S2×m .
Since d2 is finite, equation (8) implies that S2×m has finite
dimension. Due to the fact that perfectly distinguishable
states are linearly independent, its capacity, denoted cm ,
must be finite, too. Since systems with the same capacity
are equivalent, we must have cm 6= cn for m 6= n, and
the sequence of integers c1 , c2 , . . . is unbounded. For any

(17)

Lemmas 3 and 5 show that these two properties hold for
every theory satisfying our requirements. The following
theorem exploits these properties to show that the capacity is multiplicative (one of the axioms in [4]).
Theorem 3. If cA and cB are the capacities of systems
A and B, then the capacity of the composite system AB
is
(18)

cAB = cA cB .

Proof. Equation (17) allows to write the maximallymixed states of systems A and B as
c

In the rest of the paper, we will use the representation
derived in Theorem 2 above, where the generalized bit is
represented by a unit ball. Moreover, we will drop the
prime in Ŝ2′ , x′i , ϕ̂′ used in the proof, and simply write
Ŝ2 , xi , ϕ̂.
As argued above, for each pure state ϕ ∈ S2 there is a
binary measurement with associated effect

(16)

µA =

A
1 X
ϕA ,
cA a=1 a

c

µB =

B
1 X
ϕB
b ,
cB

b=1

A
where ϕA
1 , . . . , ϕcA ∈ SA are pure and distinguishable,
B
and ϕB
1 , . . . , ϕcB ∈ SB are pure and distinguishable, too.
This and equation (16) imply

µAB = µA ⊗ µB =

cA X
cB
1 X
B
ϕA
a ⊗ ϕb .
cA cB a=1

(19)

b=1

B
All states ϕA
a ⊗ ϕb ∈ SAB are distinguishable with the
tensor-product measurement, therefore

cAB ≥ cA cB .

(20)

Let (Ω1 , . . . , ΩcAB ) be a complete measurement on AB
which distinguishes the states ψ1 , . . . , ψcAB ∈ SAB ; that
is Ωk (ψk′ ) = δk,k′ . According to Lemma
PcAB 4 these states
can be chosen to be pure. Since
k=1 Ωk (µAB ) = 1,
there is at least one value of k, denoted k0 , such that
Ωk0 (µAB ) ≤ 1/cAB .

(21)

B
The product of pure states ϕA
1 ⊗ϕ1 is pure [3], hence Requirement 4 tells that there is a reversible transformation
B
G ∈ GAB such that G(ψk0 ) = ϕA
1 ⊗ ϕ1 . The measure−1
−1
ment (Ω1 ◦ G , . . . , ΩcAB ◦ G ) distinguishes the states
G(ψ1 ), . . . , G(ψcAB ). Inequality (21), the invariance of

<!-- page 8 -->
8
µAB , expansion (19), the positivity of probabilities, and
B
(Ωk0 ◦ G−1 )(ϕA
1 ⊗ ϕ1 ) = 1, imply
1
cAB

≥ (Ωk0 ◦ G−1 )(µAB )
=

1 X
1
B
(Ωk0 ◦ G−1 )(ϕA
.
a ⊗ ϕb ) ≥
cA cB
cA cB
a,b

This and (20) imply (18).
It is shown in [4] that the two multiplicativity formulas
(8) and (18) imply the existence of a positive integer r
such that: for any c the state space Sc has dimension
dc = cr − 1 .

(22)

The integer r is a constant of the theory, with values
r = 1 for CPT and r = 2 for QT.

D.

Recovering classical probability theory

Let us consider all theories with d2 = 1. In this case,
equation (22) becomes dc = c − 1. In [4], it is shown that
the only GPT with this relation between capacity and
dimension is CPT, as described in Subsection II F. We
reproduce the proof for completeness.
Theorem 4. The only GPT with d2 = 1 satisfying Requirements 1–5 is classical probability theory.
Proof. Let Sc be a state space and (Ω1 , . . . , Ωc ) a
complete measurement which distinguishes the states
c
ψ1 , . . . , ψc ∈ Sc . The vectors ψ
1 , . . . , ψc ∈ R are linearly
P
independent; otherwise ψa = b6=a tb ψb and 1 = Ωa (ψa )
P
= b6=a tb Ωa (ψb ) = 0 gives a contradiction. Therefore,
c
any state
P ψ ∈ Sc ⊆ R can be written in this basis
ψ =
a qa ψa where qa = Ωa (ψ) turns out to be the
probability of outcome a. The numbers (q1 , . . . , qc ) constitute a probability distribution, hence, there is a one-toone correspondence between states in Sc and c-outcome
probability distributions. This kind of set is called a
dc -simplex. A similar argument shows that the effects
Ω1 , . . . , Ωc are linearly independent.
Hence, any effect Ω
P
on Sc can be written as Ω = a ha Ωa , and the constraint
0 ≤ Ω(ψa ) ≤ 1 implies 0 ≤ ha ≤ 1. In other words, every
measurement on Sc is generated by the complete one.
Every reversible transformation on Sc is a symmetry of
the dc -simplex, that is, a permutation of pure states. Due
to Requirement 4, there is a reversible transformation on
the bit S2 which exchanges the two pure states. Using
Requirement 3 inductively: if there is a transformation
on Sc−1 which exchanges two pure states and leaves the
rest invariant, this transposition can be implemented on
Sc , also leaving all other pure states invariant. Therefore,
all transpositions can be implemented in Sc , and those
generate the full group of permutations.

E.

Reversible transformations for the generalized
bit

In the rest of the paper, only theories with d2 > 1 are
considered. Theorem 2 shows that Ŝ2 is a d2 -dimensional
unit ball. Equation (22) for c = 2 implies that d2 is odd.
The pure states in Ŝ2 are the unit vectors in Rd2 . A
reversible transformation Ĝ ∈ Ĝ2 maps pure states onto
pure states, hence it preserves the norm and has to be an
orthogonal matrix ĜT = Ĝ−1 . Therefore Ĝ2 is a subgroup
of the orthogonal group O(d2 ).
Requirement 4 imposes that for any pair of unit vectors ϕ̂, ϕ̂′ there is Ĝ ∈ Ĝ2 such that Ĝ(ϕ̂) = ϕ̂′ . In
other words, Ĝ2 is transitive on the sphere [28, 29]. According to Lemma 6, if Ĝ2 is transitive on the sphere,
then the largest connected subgroup Cˆ2 ⊆ Ĝ2 is also
transitive on the sphere. The matrix group Cˆ2 is compact and connected, hence a Lie group (Theorem 7.31
in [24]). The classification of all connected compact Lie
groups that are transitive on the sphere is done in [28, 29].
For odd d2 , the only possibility is Cˆ2 = SO(d2 ), except for d2 = 7 where there are additional possibilities:
Cˆ2 = M G2 M T ⊂ SO(7) for any M ∈ O(7), where G2
is the fundamental representation of the smallest exceptional Lie group [30]. For even d2 , there are many more
possibilities [28, 29], but equation (22) implies that d2
must be odd.
The stabilizer of the vector ν̂1 defined in (14) is the
subgroup Ĥ2 = {Ĝ ∈ Ĝ2 : Ĝ(ν̂1 ) = ν̂1 }. Each transformation Ĥ ∈ Ĥ2 has the form


1 0T
,
Ĥ =
0 H̄
where H̄ ∈ H̄2 is the nontrivial part. If Cˆ2 = SO(d2 ) then
SO(d2 − 1) ⊆ H̄2 . In the case d2 = 7, if Cˆ2 = M G2 M T
then H̄2 contains (up to the similarity M ) the real 6dimensional representation of SU(3) given by
H̄ =



re U im U
−im U re U



,

(23)

where re U and im U are the real and imaginary parts of
U ∈ SU(3) (see exercise 22.27 in [30]).
F.

Two generalized bits

The joint state space of two S2 systems is denoted by
S2,2 . The multiplicativity of the capacity (18) implies
that S2,2 is equivalent to S4 . However, we write S2,2 to
emphasize the bipartite structure.
In what follows, instead of using the standard representation for bipartite systems (3) we generalize the
Bloch representation to two generalized bits. A state
ψAB ∈ S2,2 has Bloch representation ψ̂AB = [α, β, C]

<!-- page 9 -->
9
with
αi = 2p(xi ) − 1
β j = 2p(yj ) − 1
C ij = 4p(xi , yj ) − 2p(xi ) − 2p(yj ) + 1

(24)

Ω̂0,0 [α, β, C] = (1 + α1 + β 1 + C 1,1 )/4 ,

for i, j = 1, . . . , d2 . Note that α = ψ̂A and β = ψ̂B
are the reduced states in the Bloch representation (13).
The correlation matrix can also be written as C ij =
p(xi , yj ) − p(xi , ȳj ) − p(x̄i , yj ) + p(x̄i , ȳj ), and characterizes the correlations between subsystems. Product states
have Bloch representation


(ϕA ⊗ ϕB )∧ = ϕ̂A , ϕ̂B , ϕ̂A ϕ̂TB ,
(25)
with rank-one correlation matrix. In QT, where d2 =
3, two-qubit density matrices are often represented by
[α, β, C] through formula (41). Definition (24) implies
−1 ≤ αi , β j , C ij ≤ 1 .

(26)

The invertible map L[ψAB ] = ψ̂AB defined by (24)
also determines the Bloch representation of effects Ω̂ =
Ω ◦ L−1 . In particular, the tensor-product of two effects
of the form (15) is

(ΩϕA ⊗ ΩϕB )∧ [α, β, C] = 1 + ϕ̂TA α + ϕ̂TB β + ϕ̂TA C ϕ̂B /4 .
(27)
The map L also determines the action of reversible transformation in the Bloch representation. Since L is affine
but not linear, the action Ĝ = L ◦ G ◦ L−1 need not be
linear. Identities (16, 25) and µ̂2 = 0 imply that the
maximally-mixed state in Ŝ2,2 is µ̂2,2 = (µ̂2 , µ̂2 , µ̂2 µ̂T2 ) =
0. This and (12) imply that transformations Ĝ2,2 act on
the generic vector [α, β, C] as matrices. In particular,
local transformations GA , GB ∈ G2 act as
(GA ⊗ GB )∧ [α, β, C] = [ĜA α, ĜB β, ĜA C ĜTB ] .

(28)

Subsection IV E concludes that Ĝ2 consists of orthogonal
matrices, and Lemma 8 shows that all transformations in
Ĝ2,2 are orthogonal, too. Orthogonal matrices preserve
the norm of vectors, therefore all pure states ψ ∈ S2,2
satisfy
|ψ̂|2 = |α|2 + |β|2 + tr(C T C) = 3 .

(29)

The constant in the right-hand side can be obtained by
letting ψ̂ = [α, α, ααT ] with |α| = 1.
G.

from Ŝ2 . The four pure states ϕa,b = ϕa ⊗ ϕb ∈ S2,2
can be distinguished with the complete measurement
Ωa,b = Ωϕa ⊗ Ωϕb where a, b ∈ {0, 1}. Formula (27)
implies

Consistency in the subspaces of two generalized
bits

In this subsection we use a trick introduced in [19]: to
impose the equivalence between a particular subspace of
S2,2 and S2 (Requirement 3).
Consider the unit vector ν̂1 from (14) and the two
distinguishable pure states ϕ̂0 = ν̂1 and ϕ̂1 = −ν̂1

1

1

Ω̂1,1 [α, β, C] = (1 − α − β + C

1,1

)/4 .

(30)
(31)

Requirement 3 implies that the subspace
S2′ = {ψ ∈ S2,2 : (Ω0,0 + Ω1,1 )(ψ) = 1} ,
is equivalent to S2 . By adding (30) plus (31), it becomes
clear that a state ψ̂ = [α, β, C] belongs to Ŝ2′ if and only
if C 1,1 = 1. Moreover, if ψ ∈ S2′ , then it follows from
Ω̂0,1 (ψ̂) ≥ 0 and Ω̂1,0 (ψ̂) ≥ 0 that α1 = β 1 .
Theorem 5. The state space of a generalized bit has
dimension three (d2 = 3).
Proof. Recall that the case under consideration is odd d2
larger than one. The space S2′ ⊂ S2,2 is equivalent to S2 ,
which is a d2 -dimensional unit ball. If ϕ0,0 and ϕ1,1 are
considered the poles of this ball, then the equator is the
set of states ψeq such that Ω0,0 (ψeq ) = Ω1,1 (ψeq ) = 1/2.
Equations (30, 31) tell that equator states have α1 =
β 1 = 0, and then

    
1 τ̄ T
0
0
],
,
,
ψ̂eq = [
(32)
γ̄ C̄
ᾱ
β̄
where ᾱ, β̄, γ̄, τ̄ ∈ Rd2 −1 and C̄ ∈ R(d2 −1)×(d2 −1) . Consider the action of GA ⊗I for GA ∈ G2 on an equator state
ψeq . Since Ĝ2 is transitive on the unit sphere, if γ̄ 6= 0
then there is some ĜA ∈ Ĝ2 such that the correlation
matrix transforms into
 p


1 τ̄ T
1 + |γ̄|2 ?
=
ĜA
,
γ̄ C̄
0
?
which is in contradiction with (26). Therefore γ̄ = 0, and
by a similar argument τ̄ = 0.
The stabilizer of ν̂1 is the largest subgroup Ĥ2 ⊂ Ĝ2
which leaves ν̂1 invariant (Subsection IV E). For any pair
HA , HB ∈ H2 the identity Ωa,b ◦(HA ⊗HB ) = Ωa,b holds,
which implies that if ψeq belongs to the equator (32) then

 
 

0
1
0T
0
]
,
,
(HA ⊗HB )(ψeq )∧ = [
T
0 H̄A C̄ H̄B
H̄A ᾱ
H̄B β̄
also belongs to the equator. The equator is a unit ball of
dimension d2 − 1. Since the set
{(HA ⊗ HB )(ψeq ) : HA , HB ∈ H2 }

(33)

is a subset of the equator, the dimension of its affine span
is at most d2 − 1.
Consider the case C̄ = 0. The normalization condition
(29) implies |ᾱ| = |β̄| = 1. The set {H̄A ᾱ : H̄A ∈ H̄2 } has
dimension d2 − 1, and the same for {H̄B β̄ : H̄B ∈ H̄2 }.

<!-- page 10 -->
10
Therefore the set (33) has dimension at least 2(d2 − 1)
generating a contradiction.
Consider the case C̄ 6= 0. The group action on C̄
corresponds to the exterior tensor product H̄2 ⊠ H̄2 =
{H̄A ⊗ H̄B : H̄A , H̄B ∈ H̄2 }. If d2 > 3 and SO(d2 − 1)
⊆ H̄2 then H̄2 is irreducible in Cd2 −1 , and a simple
character-based argument shows that H̄2 ⊠ H̄2 is irreducible in (Cd2 −1 )⊗2 (see page 427 in [30]). Hence the
set
T
: H̄A , H̄B ∈ H̄2 }
{H̄A C̄ H̄B

(34)

has dimension (d2 − 1)2 , which conflicts with the dimensionality requirements of (33). If d2 = 7 and H̄2 contains
the representation of SU(3) given in (23), then the subgroup


U 0
H̄ =
0 U
with U ∈ SO(3) ⊂ SU(3) has two invariant C3 subspaces.
Therefore the invariant subspaces of H̄2 ⊠H̄2 have at least
dimension 9, and independently of C̄, the set (34) has at
least dimension 9, which conflicts with the dimensionality
requirements of (33). So the only possibility is d2 =
3.
From now on, only the case d2 = 3 is considered. Subsection IV E tells that SO(3) ⊆ Ĝ2 ⊆ O(3), which implies
that either Ĝ2 = O(3) and H̄2 = O(2), or Ĝ2 = SO(3)
and H̄2 = SO(2).
Let us see that the first case is impossible. The group
H̄2 = O(2) is irreducible in C2 , therefore H̄2 ⊠ H̄2 is irreducible in (C2 )⊗2 . Three paragraphs above it is shown
that C̄ 6= 0, hence the set (34) has dimension (d2 − 1)2 ,
which is a lower bound for the one of (33), which is larger
than the allowed one (d2 − 1 = 2).
Let us address the second case. The group H̄2 = SO(2)
is irreducible in R2 but reducible in C2 ; so the previous
argument does not hold. The vector space of 2 × 2 real
matrices decomposes into the subspace generated by rotations


cos v sin v
,
R+ =
(35)
− sin v cos v
and the one generated by reflections


cos v sin v
,
R− =
sin v − cos v

(36)

where det R± = ±1. For any pair H̄A , H̄B ∈ H̄2 the maT
T
is a rotation and the matrix H̄A R− H̄B
trix H̄A R+ H̄B
is a reflection; therefore the 2-dimensional subspaces
(35) and (36) are invariant under H̄2 ⊠ H̄2 . Since the
equator has dimension d2 − 1 = 2, all matrices C̄ 6= 0
must be fully contained in one of the two subspaces
spanned by (35) or (36), otherwise the dimension of the
set (33) would be too large again. For the same reason
ᾱ = β̄ = 0.

Depending on whether C̄ is in the subspace generated
by R+ from (35) or by R− from (36), the states in the
+
−
equator of S2′ are either ψ̂eq
or ψ̂eq
, where
    

0
0
1
0
0
±
sin v ] .
ψ̂eq
= [ 0  ,  0  ,  0 cos v
0
0
0 ∓ sin v ± cos v

The proportionality constants in C̄ ∝ R± are fixed by
normalization (29). It turns out that both the symmet+
−
correspond
ric case ψ̂eq
and the antisymmetric case ψ̂eq
to different representations of the same physical theory
—that is, the corresponding state spaces (together with
measurements and transformations) are equivalent in the
sense of Subsection II E. To see this, define the linear
map τ̂ : Ŝ2 → Ŝ2 as τ̂ (α1 , α2 , α3 )T := (α1 , α2 , −α3 )T ;
that is, a reflection in the Bloch ball. The equivalence
transformation is defined as L := τ ⊗ I (in quantum information terms, this is a “partial transposition”). This
map respects the tensor product structure, leaves the set
+
−
of product states invariant, and satisfies L̂(ψ̂eq
) = ψ̂eq
[19]. In other words: we have reduced the discussion
of the antisymmetric theory to that of the symmetric
theory [35], which will be considered for the rest of the
paper.
The orthogonality of the matrices in Ĝ2,2 implies that
′
Ŝ2 is a 3-dimensional ball, and not just affinely related to
it. Hence all states on the surface of the ball Ŝ2′ ⊂ Ŝ2,2
can be parametrized in polar coordinates u ∈ [0, π) and
v ∈ [0, 2π) as
ψ̂(u, v) =
(37)

 
 

cos u
cos u
1
0
0
[ 0 ,  0 ,  0 sin u cos v sin u sin v ] .
0
0
0 sin u sin v − sin u cos v

These states cannot be written as proper mixtures of
other states from Ŝ2′ . It is easy to see that this implies
that they are pure states in Ŝ2,2 .
H.

The Hermitian representation

In this subsection, a new (more familiar) representation is introduced, where states in S2 are represented by
2 × 2 Hermitian matrices. For any state ψ ∈ S2 in the
standard representation (1), define the linear map
L[ψ] = ψ 0

3
I − σ1 − σ2 − σ3 X i i
ψσ .
+
2
i=1

(38)

The Pauli matrices






1 0
0 −i
0 1
,
, σ3 =
, σ2 =
σ1 =
0 −1
i 0
1 0
together with the identity I constitute an orthogonal basis for the real vector space of Hermitian matrices. In

<!-- page 11 -->
11
terms of the Bloch representation, the map (38) has the
familiar form
!
3
X
1
i i
.
ψ̂ σ
I+
L[ψ] =
2
i=1
All positive unit-trace 2 × 2 Hermitian matrices can be
written in this way with ψ̂ in the unit sphere. Since
Ŝ2 is a 3-dimensional unit sphere, the set L[S2 ] is the
set of quantum states. The extreme points of L[S2 ] are
the rank-one projectors: each pure state ψ ∈ S2 satisfies
L[ψ] = |ψihψ|, where the vector |ψi ∈ C2 is defined up to
a global phase. Effect (15) associated to the pure state
ϕ ∈ S2 is

Ωϕ (ψ) = Ωϕ ◦L−1 (L[ψ]) = tr (|ϕihϕ| L[ψ]) . (39)

Note that the state ϕ and its associated effect Ωϕ are
both represented by |ϕihϕ|. The action of a reversible
transformation Ĝ ∈ Ĝ2 = SO(3) in the Hermitian representation is
L[G(ψ)] = U L[ψ]U † ,
where U ∈ SU(2) is related to Ĝ via
3
X

Ĝji σ j = U σ i U † ,

(40)

j=1

and Ĝji are the matrix components (equation VII.5.12
in [26]). In summary, the generalized bit in all theories
satisfying d2 > 1 and the requirements, is equivalent to
the qubit in QT.
I.

Reconstructing quantum theory

In this subsection, the main result of this work is
proved. But before, let us introduce some notation.
In QT, the state space with capacity c and the corresponding group of reversible transformations are
ScQ = {ρ ∈ Cc×c : ρ ≥ 0, trρ = 1} ,
GcQ = {U ⊗ U ∗ : U ∈ SU(c)} .
The joint state space of m generalized bits is denoted by
S2×m , and the corresponding group of reversible transformations by G2×m . The Hermitian representation of a
state ψ ∈ S2×m is defined to be L⊗m [ψ], where L⊗m :=
L ⊗ · · · ⊗ L, and L is defined in (38). The map L⊗m acts
independently on each tensor factor, hence it translates
the tensor product structure from the standard representation (4, 5, 7) to the Hermitian one. For example, if
ϕ ∈ S2 is a pure state, then L⊗m [ϕ⊗m ] = |ϕihϕ|⊗m . The
notation
S2H×m = L⊗m [S2×m ] ,

G2H×m = L⊗m ◦ G2×m ◦ (L⊗m )−1 ,

will be useful. The Hermitian representation of a state
ψ̂AB = [α, β, C] ∈ Ŝ2,2 is
L⊗2 [ψAB ] =
(41)
3
3
3
i
h
X
X
X
1
C ij σ i ⊗σ j .
β j I⊗σ j +
αi σ i ⊗I +
I⊗I +
4
i,j=1
j=1
i=1
The action of local transformations GA , GB ∈ G2 on
ψAB ∈ S2,2 is


L⊗2 (GA ⊗GB )(ψAB ) = (UA ⊗UB )ρAB (UA ⊗UB )† (42)

where ρAB = L⊗2 [ψAB ] and UA , UB ∈ SU(2) are related
to GA , GB via (40). Now, we are ready to prove
Theorem 6. The only GPT with d2 > 1 satisfying Requirements 1–5 is quantum theory.

Proof. We start by reproducing an argument from [19]
H
which shows that S4Q ⊆ S2,2
. A particular family of
pure states in S2,2 is ψ(u) = ψ(u, 0) defined in (37).
The Hermitian representation of ψ(u) is the projector
L⊗2 [ψ(u)] = |ψ(u)ihψ(u)| onto the C2 ⊗ C2 -vector

u
u
|ψ(u)i = cos |+i⊗|+i + sin |−i⊗|−i ,
2
2
√
√
where |+i = (1, 1)T / 2 and |−i = (−1, 1)T / 2.
From the Schmidt decomposition, it follows that
all rank-one projectors in C4×4 can be written as
(UA ⊗ UB )|ψ(u)ihψ(u)|(UA ⊗ UB )† for some value of u
and some local unitaries UA , UB ∈ SU(2). Thus, all rankH
one projectors are pure states in S2,2
. Their mixtures
Q
Q
H
generate all of S4 , therefore S4 ⊆ S2,2
.
Direct calculation shows that
 1 1
tr L⊗2 [ψ] L⊗2 [ψ ′ ] = + [αT α′ + β T β ′ + tr(C T C ′ )]
4 4
(43)
′
′
′
for any pair of states ψ̂ = [α, β, C] and ψ̂ = [α , β , C ′ ]
from Ŝ2,2 . Lemma 8 shows that all Ĝ ∈ Ĝ2,2 are orthogonal matrices. Therefore, the Euclidean inner product
between states, as in the right-hand side of (43), is preserved by the action of any Ĝ ∈ Ĝ2,2 . Equality (43)
maps this property to the Hermitian representation: any
H
H ∈ G2,2
preserves the Hilbert-Schmidt inner product
between states:
tr[H(ρ) H(ρ′ )] = tr(ρ ρ′ ) ,

(44)

H
for all ρ, ρ′ ∈ S2,2
.
For any pure state ϕ ∈ S2 , the rank-one projector
H
|ϕihϕ| ⊗ |ϕihϕ| = L⊗2 [ϕ ⊗ ϕ] is a pure state in S2,2
, and
⊗2 −1
tr(|ϕihϕ| ⊗ |ϕihϕ| ρ) = (Ωϕ ⊗ Ωϕ ) ◦ (L ) (ρ) is a meaH
surement on S2,2
. Any rank-one projector |ψihψ| ∈ C4×4
H
H
is a pure state in S2,2
, hence there is H ∈ G2,2
such
that H(|ϕihϕ| ⊗ |ϕihϕ|) = |ψihψ|. Composing the transformation H with the effect Ωϕ ⊗ Ωϕ generates the effect
H
(Ωϕ ⊗ Ωϕ ) ◦ (L⊗2 )−1 ◦ H −1 , which maps any ρ ∈ S2,2
to


(45)
tr |ϕihϕ| ⊗ |ϕihϕ| H −1 (ρ) = tr[|ψihψ| ρ] ,

<!-- page 12 -->
12
where (44) has been used. In summary, every rank-one
projector |ψihψ| ∈ C4×4 has an associated effect (45)
H
which is an allowed measurement on S2,2
, and these generate all quantum effects.
We have seen that all quantum states S4Q are contained
in S4H , but can there be other states? If so, the associated Hermitian matrices should have a negative eigenvalue (note that all states in the Hermitian representation (41) have unit trace). If ρ has a negative eigenvalue
and |ψi is the corresponding eigenvector, then the associated measurement outcome (45) has negative probability.
Hence, we conclude that S4Q = S4H , and similarly for the
measurements.
All reversible transformations H ∈ G4H map pure states
to pure states, that is, rank-one projectors to rank-one
projectors. According to Wigner’s Theorem [31], every map of this kind can be written as H(|ψihψ|) =
(U |ψi)(U |ψi)† , where U is either unitary or anti-unitary.
If U is anti-unitary, it follows from Wigner’s normal
form [32] that there is a two-dimensional U -invariant subspace spanned by two orthonormal vectors |θ0 i, |θ1 i ∈ C4
such that U (t0 |θ0 i + t1 |θ1 i) equals either t̄0 |θ0 i + t̄1 |θ1 i
or t̄1 eis |θ0 i + t̄0 e−is |θ1 i for some s ∈ R. In both cases,
U acts as a reflection in the corresponding Bloch ball,
which contradicts Requirement 3 because we know that
G2 = SO(3). Therefore G4H ⊆ G4Q .
H
We know that G2,2
contains all local unitaries. Since
this group is transitive on the pure states, it contains at
least one unitary which maps a product state to an entangled state. It is well-known [33] that this implies that the
corresponding group of unitaries constitutes a universal
gate set for quantum computation; that is, it generates
every unitary operation on 2 qubits. This proves that
G4H = G4Q .
Consider m generalized bits as a composite system.
From the previously discussed case of S2,2 , we know
that every unitary operation on every pair of generalized bits is an allowed transformation on S2H×m . But twoqubit unitaries generate all unitary transformations [33],
hence G2Qm ⊆ G2H×m . By applying all these unitaries to
|ϕihϕ|⊗m , all pure quantum states are generated, hence
S2Qm ⊆ S2H×m . Reasoning as in the S2,2 case, for evm
ery rank-one projector |ψihψ| acting on C2 , the associated effect which maps ρ ∈ S2H×m to tr(|ψihψ|ρ) is an allowed measurement outcome on S2H×m . This implies that
all matrices in S2H×m have positive eigenvalues, therefore
S2H×m = S2Qm and G2H×m = G2Qm .
The remaining cases of capacities c that are not powers
of two are treated by applying Requirement 3, using that
Sc ⊂ S2m for large enough m.
V.

CONCLUSION

We have imposed five physical requirements on the
framework of generalized probabilistic theories. These re-

quirements are simple and have a clear physical meaning
in terms of basic operational procedures. It is shown that
the only theories compatible with them are CPT and QT.
If Requirement 4 is strengthened by imposing the continuity of reversible transformations, then the only theory
that survives is QT. Any other theory violates at least
one of the requirements, hence the relaxation of each one
constitutes a different way to go beyond QT.
The standard formulation of QT includes two postulates which do not follow from our requirements: (i) the
update rule for the state after a measurement, and (ii) the
Schrödinger equation. If desired, these can be incorporated in our derivation of QT by imposing the following
two extra requirements: (i) if a system is measured twice
“in rapid succession” with the same measurement, the
same outcome is obtained both times [4], and (ii) closed
systems evolve reversibly and continuously in time.
This derivation of QT contains two steps which deserve a special mention. First, a direct consequence of
Requirement 3 is that S2 is fully surrounded by pure
states, which together with Requirement 4 implies that
S2 is a ball. Second, this ball has dimension three, since
d = 3 is the only value for which SO(d − 1) is reducible
in Cd .
Modifications and generalizations of QT are of interest
in themselves, and could be essential in order to construct
a QT of gravity. Some well-known attempts [15, 16] have
shown that straightforward modifications of QT’s mathematical formalism quickly lead to inconsistencies, such as
superluminal signaling [17]. This work provides an alternative way to proceed. We have shown that the Hilbert
space formalism of QT follows from five simple physical
requirements. This gives five different consistent ways
to go beyond QT, each obtained by relaxing one of our
requirements.

Acknowledgments

The authors are grateful to Anne Beyreuther, Jens Eisert, Volkher Scholz, Tony Short, and Christopher Witte
for discussions. Special thanks to Lucien Hardy for pointing out the multiplicity of groups that are transitive on
the sphere and, correspondingly, the need to address the
7-dimensional ball as a special case. Lluı́s Masanes is financially supported by Caixa Manresa, and benefits from
the Spanish MEC project TOQATA (FIS2008-00784)
and QOIT (Consolider Ingenio 2010), EU Integrated
Project SCALA and STREP project NAMEQUAM.
Markus Müller was supported by the EU (QESSENCE).
Research at Perimeter Institute is supported by the Government of Canada through Industry Canada and by the
Province of Ontario through the Ministry of Research
and Innovation.

<!-- page 13 -->
13

[1] J. S. Bell, Physics 1, 195 (1964).
[2] P. W. Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer; SIAM J. Comput. 26(5), 1484-1509 (1997), quantph/9508027v2.
[3] L. Hardy, Foliable Operational Structures for General
Probabilistic Theories; arXiv:0912.4740v1.
[4] L. Hardy; Quantum Theory From Five Reasonable Axioms, quant-ph/0101012v4.
[5] H. Barnum, A. Wilce, Information processing in convex operational theories, DCM/QPL (Oxford University
2008), arXiv:0908.2352v1.
[6] J. Barrett, Information processing in generalized probabilistic theories, Phys. Rev. A 75, 032304 (2007),
arXiv:quant-ph/0508211v3.
[7] G. W. Mackey; The mathematical foundations of quantum mechanics, (W. A. Benjamin Inc, New York, 1963).
[8] G. Birkhoff, J. von Neumann, The Logic of Quantum
Mechanics, Annals of Mathematics, 37, 823 (1936).
[9] G. Chiribella, G. M. D’Ariano, P. Perinotti; Probabilistic theories with purification; Phys. Rev. A 81, 062348
(2010), arXiv:0908.1583v5.
[10] W. van Dam, Implausible Consequences of Superstrong
Nonlocality, arXiv:quant-ph/0501159v1.
[11] M. Pawlowski, T. Paterek, D. Kaszlikowski, V. Scarani,
A. Winter, M. Zukowski, A new physical principle: Information Causality, Nature 461, 1101 (2009),
arXiv:0905.2292v3.
[12] S. Popescu, D. Rohrlich, Causality and Nonlocality
as Axioms for Quantum Mechanics, Proceedings of
the Symposium on Causality and Locality in Modern
Physics and Astronomy (York University, Toronto, 1997),
arXiv:quant-ph/9709026v2.
[13] M. Navascues, H. Wunderlich, A glance beyond the quantum model, Proc. Roy. Soc. Lond. A 466, 881-890 (2009),
arXiv:0907.0372v1.
[14] D. Gross, M. Müller, R. Colbeck, O. C. O. Dahlsten,
All reversible dynamics in maximally non-local theories are trivial, Phys. Rev. Lett. 104, 080402 (2010),
arXiv:0910.1840v2.
[15] A. Gleason, J. Math. Mech. 6, 885 (1957).
[16] S. Weinberg, Ann. Phys. NY 194, 336 (1989).
[17] N. Gisin, Weinberg’s non-linear quantum mechanics and
supraluminal communications, Phys. Lett. A 1431–2
(1990).
[18] S. Aaronson, Is Quantum Mechanics An Island In Theoryspace?, quant-ph/0401062v2.
[19] B. Dakić, C. Brukner, Quantum Theory and Beyond: Is
Entanglement Special?, arXiv:0911.0695v1.
[20] C. A. Fuchs, Quantum Mechanics as Quantum Information (and only a little more), Quantum Theory: Reconstruction of Foundations, A. Khrenikov (ed.), Växjo University Press (2002), arXiv:quant-ph/0205039v1.
[21] G. Brassard, Is information the key? Nature Physics 1,
2 (2005).
[22] E. M. Alfsen and F. W. Shultz, Geometry of state spaces
of operator algebras, Birkhäuser, Boston (2003).
[23] R. T. Rockafellar, Convex Analysis, Princeton University
Press (1970).
[24] A. Baker, Matrix Groups, An Introduction to Lie Group
Theory, Springer-Verlag London Limited (2006).

[25] A. J. Short, private communication.
[26] B. Simon, Representations of Finite and Compact
Groups, Graduate Studies in Mathematics, vol. 10,
American Mathematical Society (1996).
[27] S. Straszewicz, Über exponierte Punkte abgeschlossener
Punktmengen, Fund. Math. 24, 139-143 (1935).
[28] A. L. Onishchik and V. V. Gorbatsevich, Lie groups and
Lie algebras I, Encyclopedia of Mathematical Sciences
20, Springer Verlag Berlin, Heidelberg (1993).
[29] A. L. Onishchik, Transitive compact transformation
groups, Mat. Sb. (N.S.) 60(102):4 447–485 (1963); English translation: Amer. Math. Soc. Transl. (2) 55, 153–
194 (1966).
[30] W. Fulton, J. Harris, Representation Theory, Graduate
texts in mathematics, Springer (2004).
[31] V. Bargmann, Note on Wigner’s Theorem on Symmetry
Operations, J. Math. Phys. 5, 862–868 (1964).
[32] E. P. Wigner, Normal Form of Antiunitary Operators, J.
Math. Phys. 1, 409–413 (1960).
[33] M. J. Bremner, C. M. Dawson, J. L. Dodd, A. Gilchrist,
A. W. Harrow, D. Mortimer, M. A. Nielsen, T. J.
Osborne, Practical scheme for quantum computation
with any two-qubit entangling gate, Phys. Rev. Lett.
89:247902 (2002), arXiv:quant-ph/0207072v1.
[34] G. Chiribella, G. M. D’Ariano, and P. Perinotti,
Informational
derivation
of
Quantum
Theory,
arXiv:1011.6451v2.
[35] As a physical interpretation of the antisymmetric case,
consider two observers who have never met before, but
who have independently built devices to measure spin1
particles in three orthogonal directions. If they never
2
had the chance to agree on a common “handedness” of
spatial coordinate systems, and happen to have chosen
two different orientations, they will measure antisymmetric correlation matrices on shared quantum states. The
“three-bit nogo result” from [19] can be interpreted as
follows: if there is a third observer, then it is impossible
that every pair of parties measures antisymmetric correlation matrices.

Appendix A: Lemmas

Lemma 1. In any state space Sc , the only state ψ ∈ Sc
which is invariant under all reversible transformations
G(ψ) = ψ for all G ∈ Gc ,

(A1)

is the maximally-mixed state µc , defined in (11).
Proof. Suppose ψ ∈ Sc satisfies (A1). Any P
state can
be written as aR mixture of pure states: ψ = k qk ψk .
Normalization GcdG = 1, condition (A1), the linearity of
P
G, the purity of all ψk , the definition of µc , and k qk =
1, imply
Z
Z
G(ψ) dG
ψ dG =
ψ =
Gc
Gc
Z
X
X
=
G(ψk ) dG =
qk
qk µc = µc ,
k

Gc

k

<!-- page 14 -->
14
which proves the claim.
Lemma 2. If G is a compact real matrix group, then
there is a real matrix S > 0 such that for each G ∈ G the
matrix SGS −1 is orthogonal.
Proof. Since the group G is compact, there is an invariant
Haar measure [26], which allows us to define
Z
P = GT G dG .
G

Since each G is invertible, the √
matrix GT G is strictly
positive, and P too. Define S = P > 0 where both
S, S −1 are real and symmetric. For any G ∈ G we have
(SGS −1 )T (SGS −1 ) = I, which implies orthogonality.
Lemma 3. If µA and µB are the maximally-mixed states
of the state spaces SA and SB , then the maximally-mixed
state of the composite system SAB is

To prove the second part, let ψ1′ , . . . , ψn′ be the states
that are distinguished by the measurement, that is
Ωa (ψb′ ) = δa,b . Every ψb′ can be
P written as a convex
combination of pure states ψb′ = k qk ψb,k . But effects
are linear functions such that 0 ≤ Ω(ψ) ≤ 1 for any state
ψ. Hence Ω(ψb′ ) = 0 is only possible if Ω(ψb,k ) = 0 for all
k, and similarly for the case Ω(ψb′ ) = 1. It follows that
Ωa (ψb,1 ) = δa,b .
Lemma 5. If Sc is a state space with capacity c ≥ 1 and
µc the corresponding maximally-mixed state, then there
are c pure distinguishable states ψ1 , . . . , ψc ∈ Sc such that
c

µc =

Proof. Since S1 contains a single state the claim is trivially true for c = 1. Since S2 is the d2 -dimensional unit
ball, two antipodal points ϕ̂1 and ϕ̂2 = −ϕ̂1 are pure,
distinguishable and satisfy

µAB = µA ⊗ µB .
Proof. The pure states ψ A in SA linearly span RdA +1 , and
the pure states ψ B in SB linearly span RdB +1 . Therefore,
pure product states ψ A ⊗ ψ B span RdA +1 ⊗ RdB +1 . In
particular, the maximally-mixed state (11) of SAB can
be written as
X
µAB =
(A2)
ta,b ψaA ⊗ ψbB ,

µ2 =

a,b

=

X
a,b

GA

GB

ta,b µA ⊗ µB = µA ⊗ µB ,

where the same tricks from Lemma 1 have been used.
Lemma 4. For every tight effect Ω, there is a pure state
ψ such that Ω(ψ) = 1. Also, if a measurement Ω1 , . . . , Ωn
distinguishes n states ψ1 , . . . , ψn , then these states can be
chosen pure.
Proof. By definition, for each tight effect Ω there is a (not
necessarily pure) state ψ ′ such that Ω(ψ ′ ) = 1. Every ψ ′
can bePwritten as a mixture of pure
P states ψk , that is
ψ′ =
q
ψ
with
q
>
0
and
k
k k k
k qk = 1. Effects
are linear functions such that Ω(ψ) ≤ 1 for any state ψ.
Therefore, it must happen that all pure states ψk in the
above decomposition satisfy Ω(ψk ) = 1.

1
(ϕ1 + ϕ2 ) .
2

(A3)

Now, consider the joint state space of n generalized
bits, denoted S2×n . Lemma 3 and (A3) imply that the
maximally-mixed state of S2×n is
µ(n) = (µ2 )⊗n =

a,b

where ta,b ∈ R are not necessarily positive coefficients,
and all ψaA , ψbB are pure. From definition (1),
P the first
component of the vector equality (A2) implies a,b ta,b =
1. The maximally-mixed state is invariant under all reversible transformations, in particular the local ones
Z
Z
dGA dGB (GA ⊗ GB )(µAB )
µAB =
GA
G
ZB
 Z

X
A
B
=
dGA GA (ψa ) ⊗
ta,b
dGB GB (ψb )

1X
ψa .
c a=1

1
2n

X

ai ∈{1,2}

ϕa1 ⊗ · · · ⊗ ϕan .

(A4)

The states ϕa1 ⊗ · · · ⊗ ϕan ∈ S2×n for all a1 , . . . , an ∈
{1, 2} are perfectly distinguishable by the corresponding
product measurement, hence the capacity of S2×n , denoted cn , satisfies
cn ≥ 2 n .

(A5)

Let (Ω1 , . . . , Ωcn ) be a complete measurement which distinguishes the states ψ1 , . . . , ψcn ∈ S2×n . According to
Lemma
4 these states can be chosen to be pure. Since
Pcn
Ω
(µ(n) ) = 1, there is at least one value of k, dek
k=1
noted k0 , such that
Ωk0 (µ(n) ) ≤ 1/cn .

(A6)

The state ϕ1 ∈ S2 from (A3) is pure, hence ϕ⊗n
∈ S2×n
1
is pure too. Requirement 4 tells that there is a reversible
transformation G acting on S2×n such that G(ψk0 ) =
−1
ϕ⊗n
, . . . , Ωcn ◦ G−1 ) distin1 . The measurement (Ω1 ◦ G
guishes the states G(ψ1 ), . . . , G(ψcn ). Inequality (A6),
the invariance of µ(n) under G, expansion (A4), the positivity of probabilities, and (Ωk0 ◦ G−1 )(ϕ1⊗n ) = 1, imply
1
≥ (Ωk0 ◦ G−1 )(µ(n) )
cn
1
1 X
(Ωk0 ◦ G−1 )(ϕa1 ⊗ · · · ⊗ ϕan ) ≥ n .
= n
2
2
ai ∈{1,2}

<!-- page 15 -->
15
This and (A5) imply cn = 2n . This together with (A4)
shows the assertion of the lemma for state spaces whose
capacity is a power of two. The rest of cases are shown
by induction.
Let us prove that if the claim of the lemma holds for
a state space with capacity c, with c > 1, then it holds
for a state space with capacity c − 1 too. The induction hypothesis tells that there is a complete measurement (Ω1 , . . . , Ωc ) which distinguishes
the pure states
P
ψ1 , . . . , ψc ∈ Sc , and µc = 1c ck=1 ψk ∈ Sc is the corresponding maximally-mixed state. Requirement 3 tells
that the state space Sc−1 is equivalent to
′
Sc−1
= {ψ ∈ Sc | Ω1 (ψ) + · · · + Ωc−1 (ψ) = 1} .

According to Requirement 3, for each G ∈ Gc−1 there is
′
G′ ∈ Gc which implements G on Sc−1
. Hence G′ (ψk ) ∈
′
Sc−1 for k = 1, . . . , c − 1, which implies (Ωc ◦ G′ )(ψk ) = 0
for those k, and
1
= Ωc (µc ) = (Ωc ◦ G′ )(µc )
c
c
1
1X
(Ωc ◦ G′ )(ψk ) = (Ωc ◦ G′ )(ψc ) ,
=
c
c
k=1

and (Ωc ◦ G′ )(ψc ) = 1. Requirement 3 tells that the set
S1′ = {ψ ∈ Sc | Ωc (ψ) = 1}
is equivalent to S1 , which contains a single state. This
and Ωc (ψc ) = 1 imply that G′ (ψc ) = ψc and then
G′ (µ′c−1 ) = µ′c−1 , where we define
µ′c−1 =

1
c−1

c−1
X

k=1

ψk =

1
c
′
µc −
ψc ∈ Sc−1
.
c−1
c−1

For any G ∈ Gc−1 the corresponding G′ satisfies
G′ (µ′c−1 ) = µ′c−1 . Due to Lemma 1 the invariant state
′
µ′c−1 must be the maximally-mixed state in Sc−1
, which
has the claimed form, and Requirement 3 extends this to
Sc−1 .
Lemma 6. Let S be a state space such that the subset of
pure states P is a connected topological manifold. If the
corresponding group of transformations G is transitive on
P, then the largest connected subgroup C ⊆ G is transitive
on P, too.
Proof. This proof involves basic notions of point set
topology.
Since G is compact, it is the union of a finite number
of (disjoint) connected components G = C1 ∪ · · · ∪ Cn .
If n = 1 the lemma is trivial. Let C be the connected
component Ci containing the identity matrix I, which is
the largest connected subgroup of G. Each connected
component Ci is clopen (open and closed), compact and
a coset of the group: Ci = Gi ◦ C for some Gi ∈ G [30].
Pick ψ ∈ P, and consider the continuous surjective
map f : G → P, defined by f (G) = G(ψ) ∈ P. Since

C is compact f (C) ⊆ P is compact too. Since the manifold P is in particular a Hausdorff space, f (C) is closed.
Consider the set D = f −1 (f (C)). If two group elements
G, H ∈ G are in the same component, that is G−1 H ∈ C,
then G ∈ D implies H ∈ D, using that C is a normal
subgroup of G. This implies that D is the union of some
connected components Ci , and so is G\D. In particular,
G\D is compact, thus f (G\D) is compact, hence closed.
Therefore, f (C) = P\f (G\D) is open. We have thus
proven that f (C) 6= ∅ is clopen. Since P is connected, it
follows that f (C) = P.
The following lemma shows that there are transformations for two generalized bits which perform the “classical” swap and the “classical” controlled-not in a particular basis. Note that these transformations do not necessarily swap other states that are not in the given basis,
as in QT. However, they implement a minimal amount of
reversible computational power which exceeds, for example, that of boxworld, where no controlled-not operation
is possible [14].
Lemma 7. For each pair of distinguishable states
ϕ0 , ϕ1 ∈ S2 , there are transformations Gswap , Gcnot ∈
G2,2 such that
Gswap (ϕa ⊗ ϕb ) = ϕb ⊗ ϕa ,
Gcnot (ϕa ⊗ ϕb ) = ϕa ⊗ ϕa⊕b ,

(A7)
(A8)

for all a, b ∈ {0, 1}, where ⊕ is addition modulo 2.
Proof. Let (Ω0 , Ω1 ) be the measurement which distinguishes (ϕ0 , ϕ1 ), that is Ωa (ϕb ) = δa,b . Define ψa,b =
ϕa ⊗ ϕb and Ωa,b = Ωa ⊗ Ωb for a, b ∈ {0, 1}. Define
S3′ = {ψ ∈ S2,2 | (Ω0,1 + Ω1,0 + Ω1,1 )(ψ) = 1},
S2′ = {ψ ∈ S2,2 | (Ω0,1 + Ω1,0 )(ψ) = 1} ,
and note that S2′ ⊂ S3′ ⊂ S2,2 . At the end of
Subsection IV B, it is shown that two distinguishable
states ϕ0 , ϕ1 ∈ S2 have Bloch representation satisfying ϕ̂0 = −ϕ̂1 . According to Requirement 4 there
is G ∈ G2 such that G(ϕ0 ) = ϕ1 , and by linearity,
Ĝ(ϕ̂1 ) = −Ĝ(ϕ̂0 ) = −ϕ̂1 = ϕ̂0 . Requirement 3 implies that there is a transformation G′swap for S3′ such
that G′swap (ψ0,1 ) = ψ1,0 and G′swap (ψ1,0 ) = ψ0,1 . According to Lemma 5, the maximally-mixed state in S3′
can be written as µ′3 = (ψ0,1 + ψ1,0 + ψ1,1 )/3. Equalities
G′swap (µ′3 ) = µ′3 and G′swap (ψ0,1 + ψ1,0 ) = ψ0,1 + ψ1,0 imply that G′swap (ψ1,1 ) = ψ1,1 . Using Requirement 3 again,
there is a reversible transformation Gswap ∈ G2,2 which
implements G′swap in the subspace S3′ . Repeating the argument with the maximally-mixed state (now in S2,2 ) we
conclude that Gswap (ψ1,1 ) = ψ1,1 , hence Gswap satisfies
(A7).
The existence of Gcnot is shown similarly, by exchanging the roles of ψ0,1 and ψ1,1 .

<!-- page 16 -->
16
Lemma 8. Reversible transformations for two generalized bits in the Bloch representation (24) are orthogonal:
Ĝ2,2 ⊆ O(d4 ) .
Proof. In Subsection IV F the Bloch representation for
two generalized bits is defined, and it is argued that reversible transformations Ĝ2,2 act on [α, β, C] as matrices.
In particular, local transformations (28) are

ĜA 0
0
,
(GA ⊗ GB )∧ =  0 ĜB
0
0 0 ĜA ⊗ ĜB


(A9)

where each diagonal block acts on an entry of [α, β, C],
and ĜA , ĜB ∈ Ĝ2 . In Subsection IV E it is argued that
Ĝ2 ⊆ O(d2 ), hence local transformations (A9) are orthogonal.
Lemma 2 shows the existence of a real matrix S > 0
such that for any Ĝ ∈ Ĝ2,2 the matrix S ĜS −1 is orthogonal. In particular

T 

S · (GA ⊗ GB )∧ · S −1 S · (GA ⊗ GB )∧ · S −1 = I ,

= Ĝswap ([α, α, ααT ] + [α, −α, −ααT ]) /2
= ([α, α, ααT ] + [−α, α, −ααT ]) /2
= [0, α, 0] .
Since S Ĝswap S −1 is orthogonal, the vectors [α, 0, 0] and
[0, ba−1 α, 0] have the same modulus, hence a = b. Also,
there is a transformation Gcnot ∈ G2,2 such that
Ĝcnot [0, 0, ααT ]
= Ĝcnot ([α, α, ααT ] + [−α, −α, ααT ]) /2
= ([α, α, ααT ] + [−α, α, −ααT ]) /2
= [0, α, 0] .
Since S Ĝcnot S −1 is orthogonal, the vectors [0, 0, ααT ] and
[0, bs−1 α, 0] have the same modulus, hence s = b. Consequently S = aI, and the claim follows.

Lemma 9. The results of this paper also hold if Requirement 5 is replaced by Requirement 5’.

which implies the commutation relation

S · (GA ⊗ GB )∧ = (GA ⊗ GB )∧ · S

(A10)

Subsection IV E concludes that d2 is odd, and that
SO(d2 ) ⊆ Ĝ2 except when d2 = 7, where M G2 M −1 ⊆ Ĝ2
and G2 is the fundamental representation of the smallest
exceptional Lie group [30]. For d2 ≥ 3 these groups act
irreducibly in Cd2 , hence Ĝ2 acts irreducibly in Cd2 too
[30]. The first two diagonal blocks in (A9) are irreducible.
The exterior tensor product of two irreducible representations (in Cd ) is also an irreducible representation, hence
the third diagonal block in (A9) is also irreducible. This
together with (A10) implies that


aI 0 0
S =  0 bI 0 
0 0 sI
for some a, b, s > 0 (Schur’s Lemma [30]).
According to Lemma 7, for each unit vector α ∈ Ŝ2
there is a transformation Gswap ∈ G2,2 such that
Ĝswap [α, 0, 0]

Proof. Assume Requirement 5’, but not Requirement 5.
It follows that S1 contains a single state only: if it
contained more than one state, there would exist some
ψ ∈ S1 which is not completely mixed, which would then
be distinguishable from some other state, contradicting
that S1 has capacity 1. Requirement 5 is used in the proof
of Theorem 1. This proof is easily modified to comply
with Requirement 5’ instead: adopting the notation from
the proof, the state ϕmix is not completely mixed, thus
distinguishable from some other state. This proves existence of some Ω̂ with the claimed properties, and the
other arguments remain unchanged, proving that Ŝ2 can
be represented as a unit ball. All pure states in Ŝ2 are
not completely mixed, hence have a corresponding tight
effect which is physically allowed. But for every state on
the surface of the ball, there exists only one unique tight
effect which gives probability one for that state. Hence,
all these effects must be allowed, and since they generate
the set of all effects, this proves Requirement 5 for use
in (14) and the rest of the paper.
