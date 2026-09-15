---
type: paper
date: 2011-10-16
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1110.3516v2)
reviewed: false
---

# The structure of reversible computation determines the self-duality of quantum theory

Machine-generated and unreviewed text extraction of arXiv:1110.3516v2
(5 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1110.3516v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
The structure of reversible computation determines the self-duality of quantum theory
Markus P. Müller1 and Cozmin Ududec1

arXiv:1110.3516v2 [quant-ph] 27 Mar 2012

1

Perimeter Institute for Theoretical Physics, 31 Caroline Street North, Waterloo, ON N2L 2Y5, Canada
(Dated: February 20, 2012)

Predictions for measurement outcomes in physical theories are usually computed by combining two distinct
notions: a state, describing the physical system, and an observable, describing the measurement which is performed. In quantum theory, however, both notions are in some sense identical: outcome probabilities are given
by the overlap between two state vectors – quantum theory is self-dual. In this paper, we show that this notion of
self-duality can be understood from a dynamical point of view. We prove that self-duality follows from a computational primitive called bit symmetry: every logical bit can be mapped to any other logical bit by a reversible
transformation. Specifically, we consider probabilistic theories more general than quantum theory, and prove
that every bit-symmetric theory must necessarily be self-dual. We also show that bit symmetry yields stronger
restrictions on the set of allowed bipartite states than the no-signalling principle alone, suggesting reversible
time evolution as a possible reason for limitations of non-locality.

A central idea of every statistical physical theory is the distinction between states and observables. If we perform a measurement on a physical system, the state describes the preparation of the system, while the observable corresponds to our
choice of measurement. Combining the two, we obtain expectation values of measurement outcomes.
In principle, states and observables are fundamentally distinct objects. However, in quantum theory, they turn out to be
identical: transition probabilities between two states |ϕi and
|ψi are given by the overlap
Prob(ψ → ϕ) = |hϕ|ψi|2 = Tr (|ϕihϕ| |ψihψ|) .

a device which prepares either state ϕ with probability p, or ω
with probability 1 − p, yielding the state pϕ + (1 − p)ω [4].
Therefore, state spaces are convex. Similarly as in quantum
theory, states will be called mixed if they can be written as a
convex combination of this form for some 0 < p < 1 and
ϕ 6= ω, and otherwise pure. We also assume that state spaces
are compact, which implies that every state can be written as
a finite convex combination of pure states [2].

(1)

More generally, the probability of obtaining an outcome described by the projector or effect operator P , measured on a
(mixed) quantum state ρ, is given by Tr(ρP ). It is remarkable that state ρ and observable P are described by the same
mathematical objects: up to normalization, they are both arbitrary positive semidefinite operators [15]. This property of
self-duality, which is most obvious in the special case (1), lies
at the very heart of quantum theory, and can be understood as
the main ingredient in the Born rule.
In this paper we show that this remarkable property can
be understood in information-theoretic terms: self-duality is
a consequence of a certain computational primitive that we
call bit symmetry. Every theory that satisfies bit symmetry
– which we argue is necessary to allow for powerful computation – must be self-dual. We also prove that bit symmetry
restricts the set of possible bipartite states in all theories with
non-locality, including quantum theory.
General probabilistic theories. Almost any conceivable statistical physical theory, including quantum theory and classical probability theory as special cases, can be described
within the framework of general probabilistic theories [1–5].
The main physical notions are preparations, transformations,
and measurements. Any physical system is described by a
finite-dimensional real vector space A. The possible preparation procedures are represented by a set of normalized states
ΩA ⊂ A (in quantum theory, A is the set of self-adjoint operators on some Hilbert space, while ΩA is the set of density
matrices). If we have two states ϕ, ω ∈ ΩA , we can think of

FIG. 1: Two state spaces: one is a square, the other a pentagon.
Shown are pairs of perfectly distinguishable states ω, ϕ and ω 0 , ϕ0 .
For the square, there is no symmetry which maps the pair ω, ϕ to
the pair ω 0 , ϕ0 : the square state space is not bit-symmetric. For the
pentagon, the pair ω, ϕ is mapped to ω 0 , ϕ0 by a reflection across
a symmetry axis. All pairs of perfectly distinguishable pure states
can be mapped to each other – the pentagon is bit-symmetric. The
dotted lines denote the level sets of a measurement effect E which
distinguishes ω and ϕ (and, accidentally, also ω 0 and ϕ0 ). That is,
the line containing ω is {x : E(x) = 1}, and the line containing ϕ
is {x : E(x) = 0}. For the square state space, there are two types
of inequivalent logical bits: lines generated by adjacent pure states
like ω, ϕ, and the square itself which is generated by diametral states
like ω 0 , ϕ0 . For the pentagon – and any other bit-symmetric theory
– all logical bits generated by pairs of perfectly distinguishable pure
states are isometric (in this case, all pairs generate the full pentagon).

It is important for calculations to include unnormalized
states in the framework, that is, elements of the form λ · ω
for λ ≥ 0 and ω ∈ ΩA . The set of all these elements is called
A+ . It is closed with respect to sums and convex combinations – in convex geometry, sets of this kind are called cones.
We assume that A+ spans the whole space A. In quantum

<!-- page 2 -->
2
theory, A+ is the set of positive semidefinite matrices.
In order to describe observables, consider any measurement
with several possible outcomes that we perform on a state
ω. Denote by E(ω) the probability of obtaining one particular outcome. This must be a number between 0 and 1, and
it must respect probabilistic mixtures: E (pϕ + (1 − p)ω) =
pE(ϕ) + (1 − p)E(ω); that is, E must be linear [1]. Linear
maps E : A → (i.e. functionals) which are non-negative on
all of A+ will be called effects, and the set of all effects is denoted A∗+ . It is easy to see that A∗+ is again a cone – in convex
geometry terms, it is called the dual cone of A+ [6]. The normalization of states is determined by the unit u, a particular
element of A∗+ which assigns the value one to all normalized
states: u(ω) = 1 for all ω ∈ ΩA (in quantum theory, we have
u(ρ) ≡ Tr(ρ)). An effect E ∈ A∗+ is called a proper effect if
0 ≤ E(ω) ≤ 1 for all states ω ∈ ΩA .
In quantum theory, all effects can be written as maps ρ 7→
Tr(ρP ), where P ≥ 0 is a positive semidefinite matrix; it
is proper iff P ≤ 1. Identifying this effect with the matrix
P , we see that A∗+ can be identified with the set of positive
semidefinite matrices, such that A+ ≃ A∗+ . This is the notion
of self-duality which will be studied in more detail in the next
section. At this point, however, it is important to note that
A+ and A∗+ can be very different in general. As an example,
consider a state space

ΩA := (x1 , x2 , 1)T ∈ 3 − 1 ≤ x1 , x2 ≤ 1 . (2)

R

R

This state space looks like a square. It contains four pure
states, for example ω = (1, 1, 1)T and ϕ = (−1, −1, 1)T ,
and has unit u(x) := x3 . Using the standard inner product on
A = 3 and the pure state ω, we can define a linear map Eω
by Eω (x) := hω, xi = x1 + x2 + x3 . Even though ω is a valid
state, Eω is not a valid effect: for example Eω (ϕ) = −1 6≥ 0.
For the square state space, A+ and A∗+ cannot be identified
in this way – they will be different no matter which inner
product we use [7].

R

Self-duality. Building on the previous examples, we define
a system A to be self-dual [16] iff there is some inner product
h·, ·i on A such that the set of effects (represented as vectors
in A) agrees with the set of states, A∗+ = A+ ; that is,
A∗+ = {ω 7→ hω, ϕi | ϕ ∈ A+ } .
Quantum theory is self-dual. To see this, recall that for an nlevel quantum system, the real vector space A is the set of selfadjoint n × n-matrices. Consider the Hilbert Schmidt inner
product on A, given by hX, Y i := Tr(XY ). As we have seen
above, under this inner product, we can identify A+ and A∗+ :
both are the set of positive semidefinite matrices.
As another example, it can be shown that the square
state space (2) is not self-dual [7], as already indicated.
More generally, regular polygons with n vertices are selfdual if and only if n is odd. This will become important below.
Bit symmetry. In addition to preparations (states) and measurements (effects), physical theories also contain a notion of

transformations. Transformations describe on the one hand
possible physical time evolution, and on the other hand possible computations that can be accomplished in the respective
theory. In this paper, we will only consider reversible transformations. This is motivated by the fact that time evolution
in our universe seems to be fundamentally reversible, and also
by the conceptual analogy to the reversible circuit model in
quantum computation.
Transformations must be linear (since they must respect
probabilistic mixtures [1]), preserve the normalization, and
map states to states. For reversible transformations T , this
must also be true for their inverses. Consequently, they must
be symmetries of the state space: T (ΩA ) = ΩA . Therefore, the set of reversible transformations on a system A is
a group GA , which is a subgroup of all symmetries. We assume that GA is compact, which may be motivated on physical
grounds [8]. In quantum theory, GA is the group of unitaries.
We are interested in a particular type of symmetry which
connects all logical bits. To this end, we call two states ϕ, ω ∈
ΩA perfectly distinguishable if there is a proper effect E such
that E(ϕ) = 0 and E(ω) = 1 – that is, if there is a conceivable
measurement device that distinguishes ϕ and ω perfectly in a
single run. Since all states ψ have 0 ≤ E(ψ) ≤ 1, the states
ϕ and ω must lie on opposite sides of state space: the set of
vectors x ∈ A with E(x) = 1 resp. E(x) = 0 are two parallel
supporting hyperplanes, touching the state space in ϕ and ω,
with the full state space lying in between, as sketched in Fig. 1.
Every pair of pure and perfectly distinguishable states ϕ
and ω generate a logical bit: in terms of convex geometry,
this is the face generated by ϕ and ω, that is, the smallest
face [17] of ΩA containing both ϕ and ω. In quantum theory,
two pure states |ϕihϕ| and |ωihω| are perfectly distinguishable
if and only if hϕ|ωi = 0. The logical bit that they generate
is not simply the line segment making up their convex hull,
but contains all pure states of the form α|ϕi + β|ωi and their
convex mixtures – that is, a full Bloch ball [18].
Now we are ready to define our main notion: a system A
is called bit-symmetric, if one of the two following equivalent
conditions holds:
• If ϕ, ω are perfectly distinguishable pure states, and so
are ϕ0 , ω 0 , then there is a reversible transformation T ∈
GA such that T ϕ = ϕ0 and T ω = ω 0 .
• Every logical bit can be mapped to every other logical
bit by some reversible transformation.
Quantum theory is obviously bit-symmetric: every pair of
orthogonal pure states can be mapped to every other by some
unitary. It is even more symmetric than this: analogous statements hold for triples, quadruples, etc., of orthogonal pure
states. As a less trivial example, consider state spaces that are
regular polygons with n vertices. It turns out that these state
spaces are bit-symmetric if and only if n is odd. In Fig. 1, this
is illustrated for n = 4 and n = 5, i.e. for the square and the
pentagon.
Classical probability theory is bit-symmetric as well: the
n-outcome state space is the set of probability distributions

<!-- page 3 -->
3
P
(p1 , . . . , pn ), i pi = 1, pi ≥ 0. Geometrically, this convex set is a simplex, and the pure states are of the form
(0, . . . , 0, 1, 0, . . . , 0) (full weight on one outcome). The reversible transformations are the permutations of the n entries,
which can map every pair of pure states to every other. In fact,
these “transpositions” generate the full group of permutations.
As the last example illustrates, bit symmetry is an important and basic computational primitive. In the context
of quantum computation, it implies that any “entangled”
logical bit that appears in a computation on many qubits
can in principle be mapped to the first qubit (awaiting a
final measurement) without destroying coherence. In general
theories, bit symmetry means that yes-no-questions which can
be answered perfectly by (irreversible) measurements may in
principle also be asked “coherently” and be part of a larger
reversible computation. In physical terms, it means that the
state of any natural two-level system can be transferred to any
other two-level system by a suitable reversible interaction.
One may argue that the time evolution of the universe would
be severely constrained if this property did not hold.
Main Result. Now we prove our main theorem:
Theorem 1 If a state space is bit-symmetric, then it is also
self-dual.
Moreover, the corresponding inner product can be chosen
to be non-negative on all states, invariant under all reversible
transformations, and to satisfy hω, ωi = 1 for all pure states
ω and hω, ϕi = 0 if ω and ϕ are perfectly distinguishable.
Remark. In quantum theory, h·, ·i is the Hilbert-Schmidt inner
product between self-adjoint matrices: hX, Y i = Tr(XY );
invariance means that hU XU † , U Y U † i = hX, Y i for all unitaries U . In all bit-symmetric theories, if one of ω and ϕ is
pure, then hω, ϕi = 0 implies that ω and ϕ are perfectly distinguishable. However, we were not able to prove that the
same holds true in general if both are mixed.
Proof. If ω ∈ ΩA is any pure state, then there is always
another pure state ϕ that is perfectly distinguishable from ω
(unless the state space contains only a single point). Thus,
bit symmetry implies transitivity: to every pair of pure states
ω, ψ, there is a reversible transformation T ∈ GA such that
T ω = ψ. This
R allows us to define a maximally mixed state
µA as µA := T ∈GA T ω dT , where ω ∈ ΩA is any pure state.
Due to transitivity, µA does not depend on the choice of ω. To
every state ω, define its Bloch vector ω̂ := ω − µA . Then we
can decompose the space A into A = Â ⊕ · µA , where Â is
the set of all points x ∈ A with u(x) = 0, with u the unit on
A. If ω is a state, then its Bloch vector ω̂ is an element of Â.
Since reversible transformations preserve normalization,
they leave the subspace Â invariant. According to group representation theory [9], there is an inner product (·, ·) on Â
such that (T x, T y) = (x, y) for all T ∈ GA and x, y ∈ Â. We
may scale this product by an arbitrary positive factor such that
(ω̂, ω̂) = 1 for all pure states ω (they all have the same inner
product due to transitivity).

R

Define c := minω,ϕ∈ΩA (ω̂, ϕ̂) ≤ (µ̂A , µ̂A ) = 0 to be the
minimal inner product between the Bloch vectors of any two
states. Our next step is to prove the following statements:
(i) For all ω and ϕ, we have c ≤ (ω̂, ϕ̂) ≤ 1, where c < 0.
(ii) If ω is pure and ϕ is arbitrary and (ω̂, ϕ̂) = c, then ω
and ϕ are perfectly distinguishable.
(iii) If ω and ϕ are arbitrary perfectly distinguishable states,
then (ω̂, ϕ̂) = c.
To this end, define a linear map Eω : A →
state ω by linear extension of
Eω (ϕ) :=

(ω̂, ϕ̂) − c
1−c

R for every pure

(ϕ ∈ ΩA ).

Since c ≤ 0, this is well-defined, and since (ω̂, ϕ̂) ≥ c, we
have Eω (ϕ) ≥p0 for all ϕ ∈ ΩA . Due to convexity of the
norm kω̂k ≡ hω̂, ω̂i, all mixed states ω satisfy kω̂k ≤ 1,
with equality for the pure states. Thus, the Cauchy-Schwarz
inequality implies (ω̂, ϕ̂) ≤ kω̂k · kϕ̂k ≤ 1, hence Eω (ϕ) ≤ 1
for all ϕ ∈ ΩA . In other words, for every pure state ω, the map
Eω is a proper effect. Now suppose that ω ∈ ΩA is pure and
ϕ ∈ ΩA is arbitrary, and (ω̂, ϕ̂) = c. Then Eω (ϕ) = 0 and
Eω (ω) = 1, hence ϕ and ω are perfectly distinguishable. This
proves (ii). Moreover, if c = 0, we would have (ω̂, µ̂A ) = 0 =
c, and so ω and µA would be perfectly distinguishable, which
is impossible. Hence c < 0, proving (i).
Choose ω, ϕ ∈ ΩA such that (ω̂, ϕ̂) = c. WePcan decompose
j: ω =
i αi ωi ,
P ω and ϕ into pure states ωi and ϕP
ϕ = j βj ϕj with αi , βj > 0. Since c = ij αi βj (ω̂i , ϕ̂j ),
and c is the minimal possible value, every addend must have
this value due to convexity, so (ω̂i , ϕ̂j ) = c for all i, j.
Thus ωi and ϕj are pure and perfectly distinguishable. Fix
some i, j. Now if ω 0 and ϕ0 are another pair of pure and
perfectly distinguishable states, there is a reversible transformation T such that T ωi = ω 0 and T ϕj = ϕ0 , hence
(ω̂ 0 , ϕ̂0 ) = (T ω̂i , T ϕ̂j ) = (ω̂i , ϕ̂j ) = c. That is, every pair
of perfectly distinguishable pure states has inner product c
between its Bloch vectors. Now suppose that ω and ϕ are
arbitrary perfectly distinguishable states. Decomposing them
as above, it follows that every ωP
i is perfectly distinguishable
from every ϕj , hence (ω̂, ϕ̂) = ij αi βj (ω̂i , ϕ̂j ) = c. This
proves statement (iii).
Let E be any effect such that +
0 · E is an exposed ray of
∗
A+ . That is, there is some x ∈ A with the following property:

R

F ∈ A∗+ , F (x) = 0 ⇒ F = λE for some λ ≥ 0.

(3)

The point x defines a supporting hyperplane of A∗+ , touching
it in the ray generated by E. Thus, either F (x) ≥ 0 for all
F ∈ A∗+ , or F (x) ≤ 0 for all F ∈ A∗+ . In the last case, we
can redefine x 7→ (−x), such that F (x) ≥ 0 for all F ∈ A∗+ ,
or, in other words, x ∈ (A∗+ )∗ = A+ . Since x 6= 0, we have
u(x) 6= 0, and ω := x/u(x) defines a state ω ∈ ΩA which
depends on E, and will be mixed in general.

<!-- page 4 -->
4
Set λ := maxϕ∈ΩA E(ϕ) > 0 and F := E/λ, then
F (ω) = 0, and the set of states ϕ with F (ϕ) = 1 is a
non-empty face of ΩA . Let ω 0 be any extremal point of that
face, then it is a pure state which is by construction perfectly distinguishable from ω. Hence (ω̂, ω̂ 0 ) = c, and so
Eω0 (x) = u(x)Eω0 (ω) = 0. Due to (3), it follows that there
is some λ ≥ 0 such that Eω0 = λE. We have thus shown that
every ray-exposed effect is of the form λ0 Eω0 for some λ0 > 0
and pure state ω 0 . According to Straszewicz’ Theorem [10],
the exposed rays are dense in the set of extremal rays, hence
every ray-extremal effect is of this form.
Now we extend (·, ·) to an inner product h·, ·i on all of A.
If x, y ∈ A, use the decomposition x = x0 µA + x̂ with
x̂ ∈ Â (and similarly for y) and define hx, yi := λx0 y0 +
(1 − λ)(x̂, ŷ), where λ := −c/(1 − c) ∈ (0, 1), since c < 0.
It is easy to check that this is an inner product, satisfying all
statements of the theorem. We can now identify linear func~ ∈ A via L(x) = hL,
~ xi.
tionals L : A →
with vectors L
Every ray-extremal effect is of the form Eω (ϕ) = hω, ϕi for
~ ω = ω. Thus, in this identificasome pure state ω, hence E
tion, all extremal rays of A∗+ are contained in A+ . Since they
generate the full cone A∗+ , we have A∗+ ⊆ A+ . On the other
hand, consider an extremal ray of A+ ; it is spanned by some
pure state ω. By construction, hω, ϕi ≥ 0 for all ω, ϕ ∈ ΩA ,
hence the corresponding effect Eω is contained in A∗+ . Thus,
A+ ⊆ A∗+ . In summary, we get A+ = A∗+ under the inner
product h·, ·i – that is, A is self-dual.

In low dimensions, bit-symmetric state spaces are rare.
Using the classification of transitive state spaces in [11],
it follows that the only bit-symmetric 2-dimensional state
spaces are the unit disc and the regular polygons with an
odd number of vertices. In 3 dimensions, there is only
the unit ball (representing a qubit) and the unique regular
self-dual polytope, the tetrahedron (representing a classical
4-level system). For a different set of postulates leading to
self-duality, see [13].

R

Non-locality. Given two state spaces A and B, we can consider the set of all joint states (that is, correlations) on AB
which are consistent with the no-signalling principle [2]; this
is called the maximal tensor product A ⊗max B of A and B.
Explicitly, ΩAB is the set of all ω ∈ A⊗B with uA ⊗uB (ω) =
∗
1 and E A ⊗ E B (ω) ≥ 0 for all E A ∈ A∗+ , E B ∈ B+
.
If A and B are the square state space (2), then A ⊗max B is
called the “no-signalling polytope”. It contains so-called PR
boxes [1] which violate the Bell-CHSH inequality by more
than any quantum state. It has been asked why quantum theory does not allow for such “maximally non-local” states. The
following theorem generalizes the results in [12]:
Theorem 2 The maximal tensor product A ⊗max B of two
state spaces can only be bit-symmetric if it does not contain
any entangled states at all.
Proof. From the definition of ΩAB , it follows that all extremal
rays of the effect cone (AB)∗+ are of the form E A ⊗ E B .

If ΩAB is bit-symmetric, then it is self-dual; hence, all pure
states (generating the state cone) are product states. Since all
states are mixtures of those, they must be unentangled.

If A and B are classical nA - and nB -level systems, then
A ⊗max B is a classical nA nB -level system. It is bitsymmetric, but does not contain any entangled states. On the
other hand, any bit-symmetric composition AB of two state
spaces A and B which does contain entangled states (such as
quantum theory) must be a proper subset of A ⊗max B – there
are at least some maximally non-local states of A ⊗max B
which AB cannot contain.
While the omission of some states of A ⊗max B does not
in itself necessarily reduce the amount of non-locality in a
theory [14], this result still gives a hint that bit symmetry
might introduce constraints on the amount of Bell inequality
violations. This conjecture is further substantiated by the
findings in [7], where it was shown that a class of composites
of regular n-gons as in Fig. 1 satisfies the Tsirelson bound if
and only if n is odd, i.e. the theory is locally bit-symmetric.
Conclusions. We have shown that self-duality, one of the
defining features of quantum theory [13], follows from the
computational primitive of bit symmetry. Thus, the power
of reversible computation (or, equivalently, time evolution)
severely constrains the statistical behaviour of any physical
theory. We have also proven that bit symmetry restricts the
set of allowed bipartite states, leaving the interesting open
problem to quantify the consequences for violations of Bell
inequalities.
Acknowledgments. We would like to thank Christian
Gogolin, Peter Janotta, Lluı́s Masanes, Jonathan Oppenheim,
Tony Short, and Stephanie Wehner for discussions. Research
at Perimeter Institute is supported by the Government of
Canada through Industry Canada and by the Province of Ontario through the Ministry of Research and Innovation.

[1] J. Barrett, Information processing in generalized probabilistic
theories, Phys. Rev. A 75 No. 3, 032304 (2007).
[2] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, Generalized
No-Broadcasting Theorem, Phys. Rev. Lett. 99, 240501 (2007).
[3] G. Mackey, Mathematical Foundations of Quantum Mechanics
(Addison-Wesley, 1963).
[4] A. S. Holevo, Probabilistic and Statistical Aspects of Quantum
Theory (North-Holland, New York, 1980).
[5] L. Hardy, Quantum Theory From Five Reasonable Axioms,
arXiv:quant-ph/0101012.
[6] C. D. Aliprantis, R. Tourky, Cones and Duality (American
Mathematical Society, 2007).
[7] P. Janotta, C. Gogolin, J. Barrett, and N. Brunner, Limits on
nonlocal correlations from the structure of the local state space,
New J. Phys. 13, 063024 (2011).
[8] M. P. Müller, O. C. O. Dahlsten, and V. Vedral, Unifying typical
entanglement and coin tossing: on randomization in probabilistic theories, arXiv:1107.6029.

<!-- page 5 -->
5
[9] B. Simon, Representations of Finite and Compact Groups
(American Mathematical Society, 1996).
[10] R. Webster, Convexity (Oxford University Press, 1994).
[11] G. Kimura and K. Nuida, On affine maps on non-compact convex sets and some characterizations of finite-dimensional solid
ellipsoids, arXiv:1012.5350.
[12] D. Gross, M. Müller, R. Colbeck, and O. C. O. Dahlsten, All
reversible dynamics in maximally non-local theories are trivial,
Phys. Rev. Lett. 104, 080402 (2010).
[13] A. Wilce, Four and a Half Axioms for Finite Dimensional
Quantum Mechanics, arXiv:0912.5530.
[14] H. Barnum, S. Beigi, S. Boixo, M. B. Elliott, and S. Wehner,
Local Quantum Measurement and No-Signaling Imply Quan-

tum Correlations, Phys. Rev. Lett. 104, 140401 (2010).
[15] Here we only consider finite-dimensional systems, where there
is no distinction between bounded and trace-class operators.
[16] In the relevant literature, this is usually called strong selfduality, as opposed to a certain weaker form of self-duality.
However, since we do not study this weaker notion of selfduality in this paper, we drop the prefix “strong”.
[17] A face of ΩA is a convex subset B ⊆ ΩA such that (x, y ∈
ΩA , λ > 0, λx + (1 − λ)y ∈ B) ⇒ x, y ∈ B.
[18] Technically, when we talk about a logical bit, we also assume a
fixed choice of perfectly distinguishable pure states ϕ, ω in that
face, analogous to a choice of “basis states” in quantum theory.
