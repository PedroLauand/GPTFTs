---
type: paper
date: 2017-01-25
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1701.08075v3)
reviewed: false
---

# Categorical Probabilistic Theories

Machine-generated and unreviewed text extraction of arXiv:1701.08075v3
(19 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1701.08075v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Categorical Probabilistic Theories
Stefano Gogioso
University of Oxford
stefano.gogioso@cs.ox.ac.uk

Carlo Maria Scandolo
University of Oxford
carlomaria.scandolo@cs.ox.ac.uk

We present a simple categorical framework for the treatment of probabilistic theories, with the aim
of reconciling the fields of Categorical Quantum Mechanics (CQM) and Operational Probabilistic
Theories (OPTs). In recent years, both CQM and OPTs have found successful application to a number
of areas in quantum foundations and information theory: they present many similarities, both in spirit
and in formalism, but they remain separated by a number of subtle yet important differences. We
attempt to bridge this gap, by adopting a minimal number of operationally motivated axioms which
provide clean categorical foundations, in the style of CQM, for the treatment of the problems that
OPTs are concerned with.

1

Introduction

Categorical methods are finding more and more applications in the foundations of quantum theory and
quantum information, with two main frameworks currently dominating the scene: Categorical Quantum
Mechanics (CQM) and Operational Probabilistic Theories (OPTs). The CQM framework [4, 7, 27, 31, 33]
concerns itself with the compositional and algebraic structure of quantum system and processes, and has a
heavy focus on diagrammatic methods [26, 53, 54]. The OPT framework [16, 17, 18, 20, 49, 50, 51] was
developed with the aim of obtaining a characterisation of quantum theory in terms of information-theoretic
axioms, inside the wider community of generalised probabilistic theories [9, 10, 11, 39, 48, 55].
Both frameworks are based on symmetric monoidal categories, and at first sight it looks like they
should be complementing each other. However, a number of subtle differences have resulted in a
significant disconnect between the two communities, with duplication of efforts and loss of synergy. The
OPT framework is founded on explicit probabilistic structure, axioms of concrete physical inspiration and
traditional proof methods, which make it hard to work with in a categorical and diagrammatic setting.
Conversely, the CQM framework has clean categorical foundations and diagrammatic proof methods, but
at the expense of direct physical interpretation.
We set off to reconcile the two frameworks, by proposing categorical foundations in the style of CQM
for the kind of systems and results that are of interest for the OPT community. We define a probabilistic
theory as a symmetric monoidal category satisfying three additional requirements: the existence of
classical systems, the existence of probabilistic structure, and the possibility of defining local states. Our
requirements are formulated in standard categorical terms, and can be readily adopted within the CQM
framework; at the same time, they correspond to relatable physical and operational requirements that any
probabilistic theory should possess. The end result is a framework which is simple and rigorous in its
foundations, shows direct operational significance, and comes with more expressive power than either of
the CQM or OPT frameworks alone.
The categorical probabilistic theories defined in this work provide the underlying framework for an
upcoming novel derivation of quantum theory from diagrammatic postulates [57]. The framework is
also expressive enough to model many toy theories of current interest in the foundations of quantum
theory [45], such as real, hyperbolic, relational and modal quantum theory.
Bob Coecke and Aleks Kissinger (Eds.):
14th International Conference on Quantum Physics and Logic (QPL)
EPTCS 266, 2018, pp. 367–385, doi:10.4204/EPTCS.266.23

c S. Gogioso & C. M. Scandolo
This work is licensed under the Creative Commons
Attribution-Noncommercial-Share Alike License.

<!-- page 2 -->
368

Categorical Probabilistic Theories

Finally, we should mention that other efforts to connect the CQM and OPT communities have
appeared recently in the literature: some of the most notable ones include Ref. [60], coming from the
logical perspective of effectus theory, Ref. [37], in relation to leaks, decoherence and the emergence of
classicality, and Ref. [43], in relation to causality and Bell-type measurement scenarios.

2

Classical Theory

The main ingredient distinguishing OPTs from the categories used in the context of CQM is the explicit
presence of probabilistic mixtures, or equivalently the existence of classical systems taking part in the
processes. From the point of view of OPTs, these classical systems are absorbed into the formalism, using
indices and summations. From the point of view of CQM, on the other hand, the only distinction between
classical and quantum systems is operational, and both should be modelled explicitly by a theory.

2.1

Classical theory as a SMC

Classical systems1 and stochastic processes between them form a symmetric monoidal category (SMC),
usually known as Stoch. The objects of Stoch are labelled by finite sets, and the morphisms X → Y in
Stoch are the Y -by-X stochastic matrices, with matrix composition as sequential composition and the
Kronecker product as parallel composition (aka tensor product).
From a categorical standpoint, the restriction to convex combinations required by Stoch is inconvenient:
if we wish to use a summation operation, as is usually done in the treatment of classical systems and
mixed-state quantum theory, we have to introduce external restrictions on the kind of sums that we allow.
Alternatively, we could see the summation as defined on a larger category, with Stoch arising as the
sub-category of suitably normalised processes. This latter approach is in line with the general philosophy
of CQM: one studies a broader collection of abstract processes, easier to describe and to manipulate, and
then assembles/restricts them appropriately to obtain the subcategory of concrete, physically relevant
processes. As our model of classical systems and (potentially non-normalised) non-deterministic processes
between them, we take the SMC R+ -Mat: just like Stoch, the objects are the finite non-empty sets, but the
Y ×X
morphisms X → Y are ALL the R+ -valued matrices in R+
, not just the stochastic ones. We refer to
these maps as the probabilistic processes, and use normalised to denote the stochastic ones.

2.2

Linear structure

We can equip R+ -Mat with a well-defined notion of summation by suitably enriching it in commutative
Y ×X
monoids: we endow the morphisms X → Y with the linear structure of R+
, i.e. we take matrix
addition as our summation operation and the zero matrix as its neutral element (modelling the impossible
process). Traditionally, the only requirement for a category enriched in commutative monoids is that
sequential composition be linear2 , but in SMCs it makes sense to further require that parallel composition
be linear as well3 . This is indeed the case for our choice of enrichment.
1 This work, like most works in OPTs and CQM, is concerned with finite classical systems alone.
2 Specifically, we require f ◦ (g + h) = ( f ◦ g) + ( f ◦ h), (g + h) ◦ f = (g ◦ f ) + (h ◦ f ), 0 ◦ f = 0 and f ◦ 0 = 0.
3 Things are a bit more complicated with the tensor structure: the tensor product is linear, just like composition, but we also
need to require the associator and unitors to be linear.

<!-- page 3 -->
S. Gogioso & C. M. Scandolo

2.3

369

Deterministic processes

A special place amongst the many probabilistic processes between two classical systems X and Y is held
by the deterministic processes4 , the functions X → Y . The deterministic processes form the sub-SMC
fSet of R+ -Mat, and the Kronecker product restricts to the Cartesian product on them. The states in
fSet for a classical system X are its deterministic states, the probability distributions δx concentrated
entirely on a single point x ∈ X (or, if you prefer, the linear extensions of the points of X themselves).
The singleton set 1 := {1} is the terminal object in fSet, and we refer to the unique effect X → 1 as
the discarding map5 on the classical system X, which is graphically denoted by a ground symbol X .
The deterministic processes sit inside a larger sub-SMC fPFun of partial deterministic processes, with
partial functions as morphisms.

2.4

Resolution of the identity

In order to clearly distinguish classical systems from more general systems in the theory, we will adopt a
special graphical convention. We use dashed wires to denote systems which are guaranteed to be classical,
so that the identity morphism X → X for a classical system X will be represented graphically as follows:
X

(2.1)

X

Using the enrichment, we obtain the following resolution of the identity:
X

=

X

x

X

∑

x

X

(2.2)

x∈X

The state labelled by x ∈ X above is the deterministic state corresponding to x; the effect labelled by x
above is the one sending x to 1 ∈ R+ and all x0 6= x to 0 ∈ R+ (or, if you prefer, the linear extension of the
partial function X * 1 which sends x to 1 ∈ 1 and is undefined on all other x0 ∈ X).

2.5

Marginalisation

Because the resolution of the identity is in terms of deterministic states, we immediately obtain the
following resolution of the discarding map:
=

X

∑

X

x

(2.3)

x∈X

This means that discarding a subsystem in R+ -Mat corresponds to the usual notion of marginalisation.
From the CQM perspective, the process of localisation of states and processes in arbitrary SMCs is
captured by the notion of environment structure [32, 34]. Because classical states and processes are
localised by marginalising, it is no surprise that discarding maps in R+ -Mat satisfy the requirements to
form an environment structure:
X ⊗Y

=

X
Y

1

=

(2.4)

The empty diagram on the right hand side of the second equation is the scalar 1, which as a diagrammatic
convention is usually omitted.
4 In line with its common meaning in computer science, we use the word deterministic to denote classical processes which

map each definite input to a single definite output. We use stochastic (or normalised probabilistic, in this work) to denote
classical processes which more generally map definite inputs to probability distributions over definite outputs.
5 In a not-at-all-unexpected coincidence, it makes total sense to call this the deterministic effect.

<!-- page 4 -->
370

2.6

Categorical Probabilistic Theories

Normalised processes

A choice of environment structure always singles out a sub-SMC of normalised processes, namely those
processes f satisfying the following condition:
f

=

(2.5)

The abstract normalisation condition above allows us to recover Stoch in a categorically fashionable way,
as the sub-SMC of normalised processes in R+ -Mat. As a bonus, we also get fSet as the sub-SMC of
normalised processes in fPFun.

2.7

Probabilities as a resource

In computer science, it is common for commutative semirings to model resources used in computation:
for example, the probability semiring (R+ , +, ×) is used to model probabilistic computation, the boolean
semiring (B, ∨, ∧) is used to model existence problems, and the natural numbers (N, +, ×) are used to
model counting problems6 . A similar approach could be adopted in physics: probabilities (corresponding
to the semiring R+ ) could be seen as a resource providing non-determinism in classical systems, and we
might wish to study the toy theories obtained by using other resources (corresponding to other semirings)
in their place. This is, for example, the road taken by the sheaf-theoretic framework of Ref. [2], where a
number of important results on non-locality and contextuality are obtained by confronting the probabilities
(the semiring R+ ) with possibilities [5] (the semiring B) and signed probabilities [6, 42] (the semiring R,
which is given an operational interpretation in Ref. [3]). The computational complexity implications of
different choices of semirings are explored in [13].
If we use a generic commutative semiring R to model non-determinism, the SMC of classical systems
and R-probabilistic processes between them is given by the category R -Mat of R-valued matrices: we
refer to the normalised states as R-distributions, and to the normalised processes as R-stochastic. As an
example, B -Mat is the category fRel of finite sets and relations between them, a well-studied toy model
in CQM [28, 35, 44]. All the theory we have developed above for R+ -Mat straightforwardly extends to
general semirings, as long as we replace Stoch with the appropriate notion of normalised processes. The
categories fSet and fPFun of total and partial deterministic processes are always sub-SMCs of R -Mat,
showing that our interpretation of R as modelling a notion of non-determinism is sound.

3

Probabilistic Theories

When talking about a theory, we broadly mean a categorical model (a SMC) that captures physical systems
and the compositional structure of processes between them. In the spirit of CQM, we avoid restricting
our attention to physical processes alone, but instead we allow the presence of a whole spectrum of
idealised, abstract processes that provide building blocks for physical processes, or otherwise help in
reasoning about them. Contrary to the OPT framework, we take the view that a theory should specify
objects and processes in a purely compositional way, and need not necessarily make immediate reference
to probabilistic outcomes of tests and measurement: as a consequence, we do not take any quotient with
respect to probabilistic outcomes, and we allow for the possibility that a theory specifies processes which
are different but cannot be distinguished by means of tests or measurements alone (this means that some
alternative “hidden variable theories” with the same operational predictions can be modelled).
6 One could also mention the tropical semiring (R, min, +) used in the Floyd-Warshall algorithm, or the Viterbi semiring
([0, 1], max, ×) used in the Viterbi algorithm, but also the p-adic numbers and finite fields.

<!-- page 5 -->
S. Gogioso & C. M. Scandolo

3.1

371

Probabilistic theories

When talking about a probabilistic theory, we mean a SMC which includes at least the classical systems
amongst its ranks, and which is furthermore compatible with a couple of basic operational features, namely
their probabilistic structure and marginalisation. We briefly motivate our requirements below.
1. Every probabilistic theory has classical probabilistic systems under the hood: because these are
themselves physical systems, we model them explicitly. In particular, their interface with other
systems (e.g. measurements and preparations) can be talked about in compositional terms.
2. It makes no sense to talk about a probabilistic theory if the probabilistic structure does not extend
from classical systems to arbitrary systems. If this were not the case, one would not necessarily be
able to work with scenarios in which multiplexed processes are controlled by a classical random
variable, or to condition a process based on a classical output.
3. Every probabilistic theory with operational aspirations should include a notion of localisation of
states and processes. Indeed, the absence of a notion of local state compatible with marginalisation
renders most protocol specifications meaningless, a fate they share with the notion of no-signalling
and with the probabilistic foundations of thermodynamics.7
We now proceed to formalise these requirements in categorical terms.
Definition 1 (Probabilistic Theory).
A probabilistic theory is a symmetric monoidal category C which satisfies the following requirements.
1. There is a full sub-SMC of C , which we denote by CK , which is equivalent to R+ -Mat.
2. The SMC C is enriched in commutative monoids8 and the enrichment on CK coincides with the one
given by the linear structure of R+ -Mat9 .
3. The SMC C comes with an environment structure, i.e. with a family (
morphisms which satisfy the following requirements:
H ⊗G

=

H
G

1

H :H

=

→ 1)H ∈obj C of

(3.1)

The environment structure on CK coincides with the one given by the discarding maps of R+ -Mat.
The requirements above can be generalised by replacing R+ with an arbitrary commutative semiring R, in
which case we will talk about an R-probabilistic theory.
In the context of a specific R-probabilistic theory, we refer to CK as the classical theory, to its object as
the classical systems and to its morphisms as the classical processes. In particular, 1 is the tensor unit
for C , and the scalars of C form the semiring R. For each pair of objects H , K ∈ obj C , the processes
H → K in C form a commutative monoid, with a summation operation + and a zero element 0, which
7 In absence of a canonical notion of local state, talking about a localised computation or experimental setup requires

non-trivial amounts of information about the state of the universe to be known. Sensible theories that do this exist, e.g. Everettian
quantum theory, but they present a number of operational challenges and are not probabilistic in nature.
8 This means that for any two objects H and K , the set of morphisms H → K comes with the structure of a commutative
monoid, i.e. it comes with a commutative associative binary operation + and a neutral element 0 for it. Furthermore, composition
of morphisms and tensor product of morphisms are both bilinear operations (e.g. ( f + g) ◦ h = f ◦ h + g ◦ h, f ⊗ 0 = 0, etc).
9 Requirement 1 above imposes that C be equivalent to R+ -Mat, but says nothing about addition + of morphisms and 0
K
morphisms being respected by the equivalence. Requirement 2 further imposes that the equivalence between the two categories
be a linear functor, so that the commutative monoid structure on morphisms is respected.

<!-- page 6 -->
372

Categorical Probabilistic Theories

we refer to as the impossible process. In line with the nomenclature adopted for classical systems,
we refer to the H maps involved in the environment structure as the discarding maps, and to those
processes f satisfying the following equation as normalised:
=

f

3.2

(3.2)

Tests

Consider a process f with a classical output valued in some finite set Y :
H

G
Y

f

(3.3)

Operationally, we can think of each output value y ∈ Y as corresponding to a different process being
performed10 , and that process can be obtained by testing against the output value y:
H

G

fy

:= H

G

f

(3.4)

y

It should be noted that, even when f is normalised, the process fy defined in Equation 3.4 is not necessarily
so, instead being weighted by the probability of y occurring. In this sense, a process in the form of 3.3
corresponds to the notion of a test in OPTs [17,20]; if the input system H is trivial then it is a preparation
test, while if the output system K is trivial then it is an observation test. Note that in this framework the
difference between a test and a more general process is entirely in the eye of the beholder: when saying
“test” instead of “process”, we will mean that we are mainly interested in its classical outputs, but we will
not exclude the presence of classical systems amongst the input systems of the process.

3.3

Output probability

The R-probability11 Pρ (y) of output value y ∈ Y occurring in a preparation test can be obtained as follows:
Pρ (y) :=

(3.5)

ρ
y

When the R-probability of outcome y for a preparation test ρ is invertible12 , we can condition on y to
obtain the state Pρ1(y) ρy , which is normalised whenever the original state ρ is:
H

ρ
y

(3.6)

1
Pρ (y)

If ρ is normalised and the R-probabilities of all classical outcomes are either zero or invertible, then the
reduced state ρ|H can be written as usual in the form of a convex combination of the conditioned states:
ρ

H

=

∑
y s.t. Pρ (y)6=0

Pρ (y)

H

ρ
y

1
Pρ (y)

(3.7)

10 A value y which is never output can, without loss of generality, be thought to correspond to the impossible process.
11 We use the word R-probability to denote the concept corresponding to probabilities when the probability semiring R+ is
replaced by a generic commutative semiring R: as the latter is fixed by the choice of R-probabilistic theory, this should cause
no confusion. In specific applications, one might want to use more specialised terms, such as: probability for R = R+ ; signed
probability for R = R; possibility for R = B; count for R = N.
12 In the case of R+ , this boils down to the usual requirement that the probability be non-vanishing.

<!-- page 7 -->
S. Gogioso & C. M. Scandolo

3.4

373

Classical control

Processes in R-probabilistic theories are not limited to tests. In its most general form, a process f includes
both some classical output system Y and some classical input/control system X:
H
X

G
Y

f

(3.8)

The process f (x) corresponding to a definite input value x ∈ X is immediately obtained by applying f to
the deterministic state corresponding to x:
H

G
Y

f (x)

:= H

G
Y

f
x

(3.9)

More generally, we can apply the process f above to an arbitrary state p := (px )x∈X on X to obtain a linear
combination of the individual processes f (x) corresponding to each definite input value x:
H

G
Y

f

p

∑ px

=

H

G
Y

f (x)

x∈X

(3.10)

When the state (px )x is normalised, this gives a convex combination ∑x px f (x) of the individual processes.

3.5

Preparations

As an example of the difference between the constructions above, we look at preparations. In an Rprobabilistic theory, there are three possible notions of preparation: we have controlled preparations,
preparation tests, and convex mixtures of the prepared states. A controlled preparation takes a classical
input x ∈ X and produces a state f (x) in H , while a preparation test is a state on the joint system H ⊗ X:
H

f

X

ρ

controlled preparation

H
X

(3.11)

preparation test

Given a normalised controlled preparation and a normalised state q on X, i.e. an R-distribution (qx )x∈X ,
we can always obtain a corresponding preparation test as follows:
classical copy map on X
ρ

H
X

f

:=

q

H
X

(3.12)

The normalisation requirement ensures that the R-probability of output x ∈ X in the preparation test is the
same specified by the R-probability distribution (qx )x∈X :

ρ

=
X

q

f
=
X

q

=
X

q

X

(3.13)
Given a preparation test obtained as in Equation 3.12, one can further discard the classical output system
X to obtain the corresponding convex combination of prepared states, as shown in Equation 3.7. There
is no compositional way of obtaining the controlled preparation back from the preparation test, or the
preparation test back from the convex combination of prepared states.

<!-- page 8 -->
374

3.6

Categorical Probabilistic Theories

Coarse-graining

Sometimes the classical outputs of a process f are not immediately interesting on their own, and one
might wish to apply some form of classical post-processing to them, by which we mean the application
of some additional classical (probabilistic) process to the output system. Most commonly, one obtains
a new process g by applying a deterministic function q : X → Z to the relevant output system X of f ,
mapping the original outputs to some “more interesting” values in some other set Z:
H
X

G
Z

g

:=

H
X

f

G
Z

q

Y

(3.14)

If we now focus on our new values in Z, we see that the process we obtain is exactly what the OPT
framework refers to as a coarse-graining of process f :
H
X

gz

G

=

H
X

G

f

q

Y

=

∑
y s.t. q(y)=z

z

H
X

fy

G

(3.15)
As a consequence, by a coarse-graining of a process f we will mean a process g taking the form of
Equation 3.14 for some deterministic function q : X → Z. Just like in the OPT framework, we say that f
is a refinement of g whenever g is a coarse-graining of f .

3.7

Sharp preparations/observation pairs

A controlled preparation can be seen as a way of encoding the values of its classical input set X into
its output system H . However, not all preparations admit a corresponding decoding process which
deterministically returns the original input values13 : we refer to those preparations admitting one such
decoding as sharp preparations, and they correspond to perfectly distinguishable states [17]. We say
that a pair (p, m) of a controlled preparation p : X → H and an observation test m : H → X is a sharp
preparation/observation pair (or SPO pair, for short) if the observation test m witnesses the sharpness
of the controlled preparation p:
p

X

H

preparation
H

m

p

X

m

X

=

X

X

(3.16)

X

observation
We say that an SPO pair is normalised14 when both p and m are normalised processes. In fact, it suffices
to ask for m to be normalised, as normalisation of p always follows15 :
p

=

p

m

=

(3.17)

13 The simplest example being given by non-injective deterministic functions.
14 To be precise, it is normalised SPOs that correspond to perfectly distinguishable states in OPTs.
15 The converse is not in general true. As a simple counterexample, take a deterministic function p : X → Y which is injective

but not surjective, and let m : Y * X be its left inverse, which is never total: then p is normalised, as it is a total function, but m
is not total, and hence not normalised.

<!-- page 9 -->
S. Gogioso & C. M. Scandolo

3.8

375

Decoherence maps

If (p, m) is a normalised SPO pair, we refer to the following process as the associated decoherence map:
H

H

dec p,m

:= H

p

m

H

(3.18)

decoherence
In order to keep track of the classical system X intervening in the decoherence map, we will use Kp,m to
denote it. There is good reason for using the name “decoherence map” in this context. Firstly, the process
dec p,m is normalised (because composition of normalised processes) and idempotent:
dec p,m

dec p,m

=

p

m

m

p

=

m

p

=

dec p,m

(3.19)
Secondly, decoherence maps can be used to reconstruct classical systems from arbitrary ones: to understand how this works, we use a mild variation on a common construction from category theory, known
as Karoubi envelope (or idempotent completion). If C is a SMC with an environment structure, then we
define the normalised Karoubi envelope of C , denoted by Split [C ], to be the SMC defined as follows:
• the systems are given by pairs in the form (H , h), where H is a system of C and h : H → H is
a normalised idempotent process;
• the processes f : (H , h) → (G , g) are exactly those processes f : H → G in C which are invariant
under the specified idempotents, i.e. those which satisfy f = g ◦ f ◦ h;
• the tensor product on systems is given by (H , h) ⊗ (G , g) := (H ⊗ G , h ⊗ g), while the tensor
product on processes is the one inherited from C .
By looking at objects in the form (H , idH ), it is immediate to see that C is a full sub-SMC of Split [C ];
in particular, the two categories have the same scalars. In fact, we can prove that Split [C ] is an
R-probabilistic theory whenever C is.
Lemma 2. If C is an R-probabilistic theory, then so is Split [C ], with classical systems, enrichment
and discarding maps directly inherited from C .
Amongst the many objects of the normalised Karoubi envelope for an R-probabilistic theory sit all objects
in the form (H , dec p,m ), with (p, m) a normalised SPO pair on H : we refer to systems in this form as
decohered systems, and we now show that they can be used to recover the classical systems of the theory.
Theorem 3 (Decohered systems).
Let C be an R-probabilistic theory, and let Decoh [C ] be the full subcategory of Split [C ] spanned by
the decohered systems. Then Decoh [C ] is a sub-SMC, and it is equivalent to the sub-SMC CK of classical
systems in C . The equivalence sends a decohered system (H , dec p,m ) to the classical system Kp,m , and a
process f : (H , dec p,m ) → (G , decq,n ) to the following classical process:
Kp,m

p

f

n

Kq,n

(3.20)

In the case of quantum theory, the decoherence maps associated with a (possibly degenerate) observable arise from the normalised SPO pair given by considering the demolition measurement in the
observable, together with its adjoint. However, there are more decoherence maps in quantum theory
than those associated with observables. Indeed, we have imposed no requirement for the observation to
be adjoint to the preparation: hence decoherence maps are always normalised and idempotent, but not
necessarily self-adjoint. As such, our notion of decoherence maps in quantum theory is more general than
the self-adjoint normalised idempotent notion used in Ref. [59] and related works.

<!-- page 10 -->
376

4

Categorical Probabilistic Theories

Quantum Theory

In CQM, dagger compact categories are taken to be abstract models of pure-state quantum theory, and
the corresponding models of mixed-state quantum theory are obtained via the CPM construction [58].
The CPM category CPM[fdHilb] contains all positive states and completely positive maps of finitedimensional quantum theory, it comes with an environment structure given by the trace, and it can be
enriched in commutative monoids, with R+ as semiring of scalars (the usual R+ -linear structure of CP
maps). Unfortunately, CPM[fdHilb] does not come with a way of talking about classical systems, and
in order to do so one usually appeals to the CP* construction [30, 38], which is related to C* algebras
and quantum logic. In this work, we will not appeal to the CP* construction: instead, we will rely on the
normalised Karoubi envelope to get a probabilistic theory out of CPM[fdHilb], following the steps of [59]
(a similar approach is followed by the recent [37]).
As we have seen before, the normalised Karoubi envelope Split [CPM[fdHilb]] contains CPM[fdHilb]
as a full sub-SMC, and we will refer to the objects in that sub-SMC as quantum systems. It also contains objects in the form (H , dec ), where is a special commutative †-Frobenius algebra on the
finite-dimensional Hilbert space H : we will refer to objects in this form as classical systems. The
decoherence map dec for is the normalised idempotent process defined as follows:
dec

=

:=

∑

x

x∈K( )

x

(4.1)

where (|xi)x∈K( ) is the orthonormal basis formed by the classical states of (see Ref. [36]).
Theorem 4 (Classical systems [59]).
Let D be the full subcategory of Split [CPM[fdHilb]] spanned by the classical systems. Then D is a full
sub-SMC equivalent to R+ -Mat. The equivalence sends a classical system (H , dec ) to the set K( ) of
classical states for , and a process f : (H , dec ) → (G , dec ) to the following classical process:


hy| f |xi
: K( ) → K( )
(4.2)
(y,x)∈K( )×K( )

When talking about quantum theory in the context of probabilistic theories, we will refer to the full
sub-SMC of Split [CPM[fdHilb]] jointly spanned by the quantum systems and the classical systems.

5

Causality and no-signalling

Causality is perhaps the trickiest point of contact between the OPT framework and probabilistic theories
as we have defined them. On the one hand, causality is part of the very definition of probabilistic theories:
a distinguished family of discarding maps is singled out by the basic operational requirement that states
be localisable. This is how causality is usually understood in the CQM community [32, 34]. On the other
hand, however, proving causality in a purely compositional way is impossible without reference to that
very environment structure. Indeed, one encounters the following issue when trying to formulate the
causality axiom as understood by the OPT community: the observation tests in OPTs have additional
requirements that make them “normalised” in a suitable sense, while the ones defined in this work have
no such requirement placed upon them. In order to single out a set of observation tests which would be
suitable to formulate the causality axiom (as understood in OPTs), we would have to somehow refer to
the environment structure to impose an appropriate normalisation condition16 .
16 For example, note that CPM[fdHilb] admits environment structures different from the canonical one.

<!-- page 11 -->
S. Gogioso & C. M. Scandolo

377

As a consequence of the remarks above, we will not talk about a causality axiom in the context
of probabilistic theories. Instead, we will keep in mind the following general scenario, involving a
(normalised) test f followed by a normalised process g:
f

(5.1)

g

By causality we will mean the observation that the local output of the test f is independent of the input
of the following process g, i.e. that normalised processes satisfy “no-signalling from the future” [17]:
f

=

g

f

(5.2)

More generally, when talking about no-signalling we have in mind some N-party Bell-type measurement scenario [14, 52], which we define to be a process in the following form (where the processes
B1 , ..., BN and the state ρ involved in constructing the scenario are all normalised):
M1

..
.

MN

ρ

B1

O1

..
.

..
.

BN

ON

(5.3)

In the context of a Bell-type measurement scenario, the processes B1 , ..., BN are often referred to as
measurements, their inputs as measurement choices and their outputs as (measurement) outcomes.
We also refer to ρ as the shared state, to M := ∏Nj=1 M j as the set of joint measurement choices and to
∏Nj=1 O j as the set of joint (measurement) outcomes.
Note that our definition is purely a matter of “shape”, and makes no direct reference to probabilistic or
no-signalling structure: one of the points of strength of our framework is indeed in providing that structure
automatically, based on the shape of the process alone. Indeed, the Bell-type measurement scenarios
defined above provide a direct point of contact with the sheaf-theoretic framework for non-locality and
contextuality [1, 2] (in a way similar to, but much more direct than, what done in [25, 32, 43]). In
the sheaf-theoretic framework, a non-locality scenario is specified by a no-signalling empirical model
(ζ m )m∈M , which is a family of R-distributions ζ m on the set ∏Nj=1 O j of joint outcomes indexed by the
joint measurement choices m ∈ M (here R is the commutative semiring chosen to model the desired
notion of non-determinism).
Theorem 5 (Bell-type measurement scenarios).
A Bell-type measurement scenario in an R-probabilistic theory always yields a no-signalling empirical
model in the sheaf-theoretic framework, with R as commutative semiring modelling non-determinism.
This result shows that the sheaf-theoretic framework can be applied directly to the treatment of nonlocality in R-probabilistic theories, and conversely that R-probabilistic theories are a natural environment
to study the realisability of no-signalling empirical models from the sheaf-theoretic framework.

<!-- page 12 -->
378

Categorical Probabilistic Theories

6

Conclusions and future work

6.1

Conclusions

In this work, we have presented a general framework for probabilistic theories based upon three fundamental operational requirements: the existence of classical systems, the possibility of forming probabilistic
combinations of processes (linear structure), and the possibility of discarding sub-systems (environment
structure). Our requirements have a simple compositional and categorical formulation, as close as possible to the spirit and practice of Categorical Quantum Mechanics (CQM), and yet feature many of the
fundamental structures used in Operational Probabilistic Theories (OPTs).
We hope that our work will contribute to providing a much-needed common ground for the CQM and
OPT communities to collaborate on. In one direction, it brings the simplicity of CQM methods to OPTs,
making it easy to create novel probabilistic theories, and to study existing ones from a fresh perspective.
In the other direction, it allows methods and results from the OPT community to be straightforwardly
applied to problems in CQM.
Furthermore, we have shown that there is a direct connection between Bell tests in R-probabilistic
theories and no-signalling empirical models in the sheaf-theoretic framework for non-locality and contextuality. As a consequence, methods from the sheaf-theoretic framework can be directly applied to
problems of interest in CQM and OPTs, and conversely categorical methods can be used to study the
realisability of empirical models in the sheaf-theoretic community.

6.2

Future work

Firstly, we have provided a new point of view on the emergence of classical systems within a probabilistic theory C (and within quantum theory in particular) based upon the normalised Karoubi envelope
Split [C ]. However, only a small subset of the objects of Split [C ] features in the construction. For
example, it is known that all super-selected quantum systems appear in quantum theory by splitting all selfadjoint idempotent processes (i.e. using decoherence maps for both commutative and non-commutative
special †-Frobenius algebras) [59], and this construction can be straightforwardly turned into a probabilistic theory. However, little or nothing is known about the operational significance of splitting general
idempotent processes, and a thorough investigation will be the topic of future work.
Secondly, a number of theories independently developed in CQM and OPTs appear to be closely
related, and should be properly connected. As a concrete example, we would be interest in applying
our work to understand the connection between the ZW calculus [47] on the CQM side and Fermionic
quantum theory [40, 41] on the OPT side. Similarly, work on thermodynamics has been undertaken by
both communities [8, 21, 22, 23, 24], and should be appropriately related.
Thirdly, we foresee a future, extended version of this work to contain a complete side-by-side
translation of all common axioms from OPTs and constructions from CQM, for ease of use. The causality
axiom has already been discussed, and two extremely important additional cases, namely the purity
axioms from OPTs and the inner product structure from CQM, are covered in the Appendix.
Finally, some applications of our framework to the sheaf-theoretic study of non-locality and to
quantum cryptography have recently appeared [46]. In the future, we expect similar constructions to
provide new insight into other families of empirical models of interest to the sheaf-theoretic and quantum
cryptography communities. Similarly, the framework has recently found application in the modelling of
numerous toy theories of interest in quantum foundations [45], and we expect this zoo to grow steadily in
the coming years.

<!-- page 13 -->
S. Gogioso & C. M. Scandolo

379

Acknowledgements. The authors would like to thank Sean Tull, Matty Hoban and John Selby for
comments, suggestions and useful discussions, as well as Sukrita Chatterji and Nicolò Chiappori for their
support. SG gratefully acknowledges funding from EPSRC and the Williams Scholarship offered by
Trinity College. CMS gratefully acknowledges funding from EPSRC and the Oxford-Google Deepmind
Graduate Scholarship.

References
[1] Samson Abramsky, Rui Soares Barbosa, Kohei Kishida, Raymond Lal & Shane Mansfield (2015): Contextuality, Cohomology and Paradox. 24th EACSL Annual Conference on Computer Science Logic (CSL),
doi:10.4230/LIPIcs.CSL.2015.211.
[2] Samson Abramsky & Adam Brandenburger (2011): The sheaf-theoretic structure of non-locality and contextuality. New Journal of Physics 13, doi:10.1088/1367-2630/13/11/113036.
[3] Samson Abramsky & Adam Brandenburger (2014): An Operational Interpretation of Negative Probabilities
and No-Signalling Models. In: Horizons of the Mind. A Tribute to Prakash Panangaden., pp. 59–75,
doi:10.1007/978-3-319-06880-0 3.
[4] Samson Abramsky & Bob Coecke (2009): Categorical Quantum Mechanics. Handbook of Quantum Logic
and Quantum Structures, pp. 261–323, doi:10.1016/B978-0-444-52869-8.50010-4.
[5] Samson Abramsky & Lucien Hardy (2012): Logical Bell inequalities. Phys. Rev. A 85, p. 062114,
doi:10.1103/PhysRevA.85.062114.
[6] Sabri W. Al-Safi & Anthony J. Short (2013): Simulating all Nonsignaling Correlations via
Classical or Quantum Theory with Negative Probabilities.
Phys. Rev. Lett. 111, p. 170403,
doi:10.1103/PhysRevLett.111.170403.
[7] Miriam Backens (2014): The ZX-calculus is complete for stabilizer quantum mechanics. New Journal of
Physics 16(9), doi:10.1088/1367-2630/16/9/093021.
[8] Krzysztof Bar & Jamie Vicary (2014): Groupoid Semantics for Thermal Computing.
[9] Howard Barnum, Jonathan Barrett, Matthew Leifer & Alexander Wilce (2007): Generalized No-Broadcasting
Theorem. Phys. Rev. Lett. 99, p. 240501, doi:10.1103/PhysRevLett.99.240501.
[10] Howard Barnum & Alexander Wilce (2011): Information Processing in Convex Operational Theories.
Electronic Notes in Theoretical Computer Science 270(1), pp. 3–15, doi:10.1016/j.entcs.2011.01.002.
[11] Jonathan Barrett (2007): Information processing in generalized probabilistic theories. Physical Review A Atomic, Molecular, and Optical Physics 75(3), pp. 1–21, doi:10.1103/PhysRevA.75.032304.
[12] Oscar Cunningham & Chris Heunen (2017): Purity through factorisation.
[13] Niel de Beaudrap (2014): On computation with ’probabilities’ modulo k.
[14] John S. Bell (1964): On the Einstein-Podolsky-Rosen paradox. Physics 1, pp. 195–200.
[15] Giulio Chiribella (2014): Distinguishability and copiability of programs in general process theories. Int. J.
Software Informatics 8(3–4), pp. 209–223.
[16] Giulio Chiribella (2014):
doi:10.4204/EPTCS.172.1.

Dilation of states and processes in operational-probabilistic theories.

[17] Giulio Chiribella, Giacomo Mauro D’Ariano & Paolo Perinotti (2010): Probabilistic theories with purification.
Physical Review A - Atomic, Molecular, and Optical Physics 81(6), doi:10.1103/PhysRevA.81.062348.
[18] Giulio Chiribella, Giacomo Mauro D’Ariano & Paolo Perinotti (2011): Informational derivation of
quantum theory. Physical Review A - Atomic, Molecular, and Optical Physics 84(1), pp. 1–39,
doi:10.1103/PhysRevA.84.012311.
[19] Giulio Chiribella, Giacomo Mauro D’Ariano & Paolo Perinotti (2012): Quantum Theory, namely the pure and
reversible theory of information. Entropy 14(10), pp. 1877–1893, doi:10.3390/e14101877.

<!-- page 14 -->
380

Categorical Probabilistic Theories

[20] Giulio Chiribella, Giacomo Mauro D’Ariano & Paolo Perinotti (2015): Quantum from principles.
doi:10.1007/978-94-017-7303-4.
[21] Giulio Chiribella & Carlo Maria Scandolo (2015): Operational axioms for diagonalizing states 195, pp.
96–115. doi:10.4204/EPTCS.195.8.
[22] Giulio Chiribella & Carlo Maria Scandolo (2015): Entanglement and thermodynamics in general probabilistic
theories. New Journal of Physics 17(10), p. 103027, doi:10.1088/1367-2630/17/10/103027.
[23] Giulio Chiribella & Carlo Maria Scandolo (2016): Entanglement as an axiomatic foundation for statistical
mechanics.
[24] Giulio Chiribella & Carlo Maria Scandolo (2016): Purity in microcanonical thermodynamics: a tale of three
resource theories.
[25] Giulio Chiribella & Xiao Yuan (2016): Bridging the gap between general probabilistic theories and
the device-independent framework for nonlocality and contextuality. Information and Computation,
doi:10.1016/j.ic.2016.02.006.
[26] Bob Coecke (2009):
Quantum
doi:10.1080/00107510903257624.

Picturalism.

Contemporary

Physics,

pp.

1–32,

[27] Bob Coecke & Ross Duncan (2011): Interacting quantum observables: Categorical algebra and diagrammatics. New Journal of Physics 13, doi:10.1088/1367-2630/13/4/043016.
[28] Bob Coecke & Bill Edwards (2012): Spekkens’s toy theory as a category of processes. Proceedings of
Symposia in Applied Mathematics 71, p. 28, doi:10.1090/psapm/071
[29] Bob Coecke & Chris Heunen (2012): Pictures of complete positivity in arbitrary dimension. Electronic
Proceedings in Theoretical Computer Science 95, pp. 27–35, doi:10.4204/EPTCS.95.4.
[30] Bob Coecke, Chris Heunen & Aleks Kissinger (2014): Categories of quantum and classical channels. Quantum
Information Processing, pp. 1–31, doi:10.1007/s11128-014-0837-4.
[31] Bob Coecke & Aleks Kissinger (2015): Categorical Quantum Mechanics I: Causal Quantum Processes.
[32] Bob Coecke (2016): Terminality Implies No-signalling ... and Much More Than That. New Generation
Computing 34, pp. 69–85, doi:10.1007/s00354-016-0201-6.
[33] Bob Coecke & Aleks Kissinger (2016): Picturing Quantum Processes. Cambridge University Press,
doi:10.1017/9781316219317.
[34] Bob Coecke & Raymond Lal (2013): Causal Categories: Relativistically Interacting Processes. Foundations
of Physics 43(4), pp. 458–501, doi:10.1007/s10701-012-9646-8.
[35] Bob Coecke & Dusko Pavlovic (2008): Quantum measurements without sums. Mathematics of Quantum
Computation and Quantum Technology, doi:10.1201/9781584889007.ch16
[36] Bob Coecke, Dusko Pavlovic & Jamie Vicary (2013): A new description of orthogonal bases. Mathematical
Structures in Computer Science 23(03), doi:10.1017/S0960129512000047.
[37] Bob Coecke, John Selby & Sean Tull (2017): Two roads to classicality.
[38] Oscar Cunningham & Chris Heunen (2015): Axiomatizing complete positivity. Electronic Proceedings in
Theoretical Computer Science (Qpl 2015), pp. 148–157, doi:10.4204/EPTCS.195.11.
[39] Borivoje Dakić & Časlav Brukner (2011): Quantum theory and beyond: is entanglement special? In
Hans Halvorson, editor: Deep Beauty: Understanding the Quantum World through Mathematical Innovation,
Cambridge University Press, Cambridge, pp. 365–392, doi:10.1017/CBO9780511976971.011
[40] Giacomo Mauro D’Ariano, Franco Manessi, Paolo Perinotti & Alessandro Tosini (2014): Fermionic computation is non-local tomographic and violates monogamy of entanglement. EPL (Europhysics Letters) 107(2), p.
20009, doi:10.1209/0295-5075/107/20009.
[41] Giacomo Mauro D’Ariano, Franco Manessi, Paolo Perinotti & Alessandro Tosini (2014): The Feynman
problem and fermionic entanglement: Fermionic theory versus qubit theory. International Journal of Modern
Physics A 29(17), p. 1430025, doi:10.1142/S0217751X14300257.

<!-- page 15 -->
S. Gogioso & C. M. Scandolo

381

[42] Julien Degorre, Marc Kaplan, Sophie Laplante & Jérémie Roland (2009): The Communication Complexity of
Non-signaling Distributions, pp. 270–281. Springer Berlin Heidelberg, Berlin, Heidelberg, doi:10.1007/978-3642-03816-7 24.
[43] Tobias Fritz (2015): Beyond Bell’s Theorem II: Scenarios with arbitrary causal structure. Communications in
Mathematical Physics 341(2), doi:10.1007/s00220-015-2495-5.
[44] Stefano Gogioso (2015): A Bestiary of Sets and Relations. Electronic Proceedings in Theoretical Computer
Science (QPL 2015), pp. 208–227, doi:10.4204/EPTCS.195.16.
[45] Stefano Gogioso (2017): Fantastic quantum theories, and where to find them.
[46] Stefano Gogioso & William Zeng (2017): Generalised Mermin-type non-locality arguments.
[47] Amar Hadzihasanovic (2015): A diagrammatic axiomatisation for qubit entanglement. Proceedings - Symposium on Logic in Computer Science 2015, pp. 573–584, doi:10.1109/LICS.2015.59.
[48] Lucien Hardy (2001): Quantum Theory From Five Reasonable Axioms.
[49] Lucien Hardy (2011): Foliable operational structures for general probabilistic theories. In H. Halvorson,
editor: Deep Beauty: Understanding the Quantum World through Mathematical Innovation, Cambridge
University Press, Cambridge, pp. 409–442, doi:10.1017/CBO9780511976971.013
[50] Lucien Hardy (2011): Reformulating and reconstructing quantum theory.
[51] Lucien Hardy (2016): Quantum Theory: Informational Foundations and Foils, chapter Reconstructing
Quantum Theory, pp. 223–248. Springer Netherlands, Dordrecht, doi:10.1007/978-94-017-7303-4 7.
[52] Joe Henson, Raymond Lal & Matthew F Pusey (2014): Theory-independent limits on correlations from
generalized Bayesian networks. New J. Phys. 16(11), p. 113043, doi:10.1088/1367-2630/16/11/113043.
[53] Clare Horsman (2011): Quantum picturalism for topological cluster-state. New Journal of Physics 133(9),
doi:10.1088/1367-2630/13/9/095011.
[54] Aleks Kissinger (2012): Pictures of Processes: Automated Graph Rewriting for Monoidal Categories and
Applications to Quantum Computing. Ph.D. thesis.
[55] Lluis Masanes & Markus P. Müller (2011): A derivation of quantum theory from physical requirements. New
J. Phys. 13(6), p. 063001, doi:10.1088/1367-2630/13/6/063001.
[56] John Selby & Bob Coecke (2017):
doi:10.1103/RevModPhys.79.555.

Leaks:

quantum,

classical,

intermediate and more,

[57] John Selby, Carlo Maria Scandolo & Bob Coecke (2017): Reconstructing Quantum Theory from Diagrammatic
Postulates.
[58] Peter Selinger (2007): Dagger Compact Closed Categories and Completely Positive Maps. Electronic Notes
in Theoretical Computer Science 170, pp. 139–163, doi:10.1016/j.entcs.2006.12.018.
[59] Peter Selinger (2008): Idempotents in dagger categories ( extended abstract ). Electronic Notes in Theoretical
Computer Science 210, pp. 107—-122, doi:10.1016/j.entcs.2008.04.021.
[60] Sean Tull (2016): Operational Theories of Physics as Categories.

<!-- page 16 -->
382

A

Categorical Probabilistic Theories

Inner product structure

The category R -Mat always comes with compact closed structure, which takes the exact same form of
the complex one from fdHilb ≃ C -Mat. It can similarly be endowed with dagger structure, as long as the
semiring R is involutive, i.e. it comes equipped with a self-inverse semiring homomorphism † : R → R.
Every semiring can be turned into an involutive semiring by taking † := idR , and when talking about R+
in the context of a dagger structure we will give as understood that the involution is the identity.
Pure-state quantum theory notably comes with a non-degenerate inner product structure, which
features heavily in the traditional formalisms. In the context of CQM, the inner product structure of
pure-state quantum theory is captured by the notion of †-SMC, and intervenes in the construction of
categories of completely positive maps [29, 58], the abstract counterparts to the operator model for
mixed-state quantum theory. The non-degeneracy condition, on the other hand, can be captured directly in
terms of the trace on positive operators, with no direct reference to the inner product structure itself: it
says that the only positive operator ρ satisfying Tr ρ = 0 is the zero operator, and more generally that
the only CP map f satisfying Tr f = 0 is the zero CP map. Because the trace provides the discarding
maps for quantum theory, we will say that an R-probabilistic theory is non-degenerate if the following
condition holds:
= 0

f

if and only if

f

= 0

(A.1)

A necessary condition for non-degeneracy of an R-probabilistic theory is that the classical theory be itself
non-degenerate, and the latter requirement is equivalent to positivity of the semiring R of scalars.
Lemma 6. The classical theory R -Mat is non-degenerate if and only if R is a positive semiring.

B

Purity

By a pure process we mean one which cannot involve any non-trivial interaction with a discarded
environment. To be precise, we will say that a process g is pure if the following implication always holds,
for some normalised state ρ (which will, in general, depend on f ) [15]:
g

=

⇒

f

=

f

g

(B.1)

ρ
We will say that a R-probabilistic theory satisfies the purification axiom if every process g can be written
in the following form for some pure process f (we refer to E as the environment) [16]:
g

=

f

(B.2)

E

We will say that a probabilistic theory satisfies the essentially unique purification axiom [17, 19] if any
two pure processes17 f , g : H → G ⊗ E satisfy the following implication, for some normalised invertible
process u : E → E (which will, in general, depend on both f and g):
f

=

g

⇒

f

=

g
u
(B.3)

17 Note that both processes have the same discarded environment system E .

<!-- page 17 -->
S. Gogioso & C. M. Scandolo

383

From a categorical perspective, it would be nice to phrase the purity preservation axiom from OPTs
as the statement that pure processes form a sub-SMC, but unfortunately we encounter a difficulty with the
explicit presence of classical systems in the theory. Indeed, the identities on non-trivial classical systems
are not pure, as they can be obtained by discarding a branch of a classical copy operation. As part of future
work, we endeavour to consider more sophisticated notions of purity [12, 37, 56, 57], in order to bypass
this issue and arrive at a suitable formulation of the purity preservation principle within our framework.

C

Proofs

Proof of Lemma 2 (p.375)
Because C is a full sub-SMC of Split [C ], we already have classical systems available, and all we need
to show is that the enrichment and environment structure can be suitably extended. The extension of the
enrichment is taken care of by the observation that any linear combination of processes invariant under
idempotents is itself invariant. Indeed, the distributivity of linear structure over composition in C yields:
h
i h
i
∀ j. g ◦ f j ◦ h = f j ⇒ g ◦ (∑ p j f j ) ◦ h = ∑ p j f j
(C.1)
j

j

Furthermore, the same discarding maps from C yield an environment structure for Split [C ]: as the latter
was defined in terms of normalised idempotents, the discarding maps themselves are always invariant.

Proof of Theorem 3 (p.375)
All that we really need to show is that the process f : (H , dec p,m ) → (G , decq,n ) can be recovered from
the classical process depicted in 3.20, and vice versa that any classical process F : Kp,m → Kq,n takes the
form depicted in 3.20 for a unique process f : (H , dec p,m ) → (G , decq,n ). The following picture proves
both directions:

H

m

Kp,m

p

H

f

G

H

f

G

n

Kq,n

q

G
(C.2)

Kp,m

F

Kq,n

Proof of Theorem 5 (p.377)
We need to show two things:
(i) that each measurement choice m ∈ ∏Nj=1 M j corresponds to an R-distribution on the joint measurement outcome set ∏Nj=1 O j (i.e. that the Bell-type measurement scenario corresponds to a
well-defined conditional R-distribution);

<!-- page 18 -->
384

Categorical Probabilistic Theories

(ii) that marginalising over the outcome set O j for the j-th party yields an empirical model for the
remaining parties which is independent of the individual measurement choice m j made by the j-th
party herself (i.e. that the conditional R-distribution satisfies the no-signalling condition).
We begin by showing that the no-signalling condition (ii) holds, and we obtain condition (i) as a corollary. Marginalising over the j-th outcome set in an R-probabilistic theory corresponds to hitting the
corresponding classical system O j with a discarding map:
m1
..
.
mj
∑

o j ∈O j

..
.

ρ

mN

B1
..
.

O1

m1
..
.

..
.

mj

Bj
..
.

oj

BN

ON

=

..
.

..
.

B1
..
.
ρ

mN

O1

..
.

Bj
..
.

..
.

BN

ON

(C.3)
But the measurements in a Bell-type measurement scenario are required to be normalised, and hence
this corresponds to an empirical model for the remaining parties which is independent of the choice of
classical deterministic state m j ∈ M j (which is always normalised, and hence discarded to the scalar 1):
m1
..
.

B1
..
.

mj
..
.
mN

ρ

O1

m1
..
.

..
.

mj
=

Bj
..
.

..
.

BN

ON

..
.
mN

B1
..
.

O1

..
.
(C.4)

ρ
..
.
BN

..
.
ON

By repeating this process for all parties we are left with the scalar Tr ρ: because the shared state ρ in a
Bell-type measurement scenario is required to be normalised, this is the scalar 1. Hence the state over
the joint measurement outcome set corresponding to the given joint measurement choice m was indeed
normalised, i.e. we got an R-distribution as required by condition (i).

Proof of Lemma 6 (p.382)
Because we can always evaluate classical processes on deterministic input states, it is sufficient to show
that the following two conditions are equivalent: (i) the zero state is the only classical state which yields
the zero scalar when hit with the discarding map; (ii) the semiring R of scalars is positive. A classical
state on a classical system X takes the form p := ∑x∈X px δx , where δx is the deterministic classical state
concentrated at x ∈ X, and (px )x∈X is some family of scalars: as a consequence, Tr p = ∑x∈X px is a generic
sum of scalars. The requirement of positivity for the semiring R states exactly that whenever ∑x∈X px = 0

<!-- page 19 -->
S. Gogioso & C. M. Scandolo

385

for some set X and some family (px )x∈X of scalars, then px = 0 for all x ∈ X: as a consequence, the
requirement of positivity is equivalent to asking that the equation Tr p = 0 holds exactly when the classical
state p is the zero state p := ∑x∈X 0δx .

D

A brief compendium of fantastic quantum theories

As mentioned in the introduction, the framework of categorical R-probabilistic theories can be used to
capture a number of toy models of quantum theory: theories of wavefunctions valued in certain semirings,
with classical systems emerging via a Born-like rule (embodied by the CP* construction). For the benefit
of the reader, we present here a brief summary of the work done in [45].
If S is any commutative semiring with involution, then we can defined the S -Mat as we did before,
but now with additional dagger and compact closed structure given by the involution ∗ on S. We can
define the sub-semiring of positive elements R for the semiring S to be the closure under addition in S
of the set {x∗ x | x ∈ S}. Then it is possible to prove that CP∗ [S -Mat] is an R-probabilistic theory under
the CMon-enrichment inherited from S -Mat. This result provides a template for generating quantum-like
theories of wavefunctions valued in commutative involutive semirings, where classicality emerges via the
same CP* construction used in traditional quantum theory to model the Born rule. A number of interesting
quantum-like theories can be captured using this template:
1. if S is the complex numbers with complex conjugation, then R = R+ is the probabilistic semiring
and CP∗ [S -Mat] is the probabilistic theory known as quantum theory;
2. if S is the real numbers with the identity as involution, then R = R+ is the probabilistic semiring
and CP∗ [S -Mat] is the probabilistic theory known as real quantum theory;
3. if S is the split-complex numbers with split-complex conjugation as involution, then R = R is the
signed-probabilistic semiring and CP∗ [S -Mat] is the quasi-probabilistic theory known as hyperbolic
quantum theory;
4. if S is the boolean semiring with the identity as involution, then R is the boolean semiring and
CP∗ [S -Mat] is the possibilistic theory known as relational quantum theory;
5. if S is a quadratic extension of the p-adic numbers with the conjugation from quadratic field
extensions, then R is the p-adic numbers and CP∗ [S -Mat] is known as p-adic quantum theory;
6. if S is a quadratic extension of a finite field K with the conjugation from quadratic field extensions,
then R = K and CP∗ [S -Mat] is a variation of modal quantum theory.
In the future, we expect that the framework of R-probabilistic theories introduced in this work will be
used to study these and other toy theories from a fully categorical perspective.
