---
type: paper
date: 2026-03-22
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:2603.21347v1)
reviewed: false
---

# Probabilistic theories stable under teleportation

Machine-generated and unreviewed text extraction of arXiv:2603.21347v1
(17 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/2603.21347v1>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Probabilistic theories stable under teleportation
Lionel J. Dmello∗ and David Gross†

arXiv:2603.21347v1 [quant-ph] 22 Mar 2026

Institute for Theoretical Physics, University of Cologne, Germany
(Dated: Mar 22, 2026)
A long-standing problem in the foundations of quantum mechanics is to identify a physical principle that
explains why algebraically maximal violations of Bell inequalities can generally not be achieved in Nature.
One recently proposed approach considers iterated Bell tests, where a Bell test is performed on a state that
has undergone several rounds of entanglement swapping. Obtaining large violations in this scenario is more
demanding, because it requires a theory to have both highly entangled states and highly entangled measurements.
It√has been conjectured that the maximal quantum mechanical Clauser-Horne-Shimony-Holt (CHSH)-value of
2 2 might be optimal for any probabilistic theory which, like quantum mechanics, maintains its CHSH-value
after an arbitrary number of rounds of entanglement swapping. However, in a previous paper, we have exhibited
a first example of a probabilistic theory that can sustain a CHSH value of 4 in this setting. In this work, further
investigating this property, we give a classification of all general probabilistic theories (GPTs) whose CHSH
value is stable in the above sense. The problem reduces to a representation-theoretic condition that allows for
exactly seven solutions. The GPT from our previous work showed some counter-intuitive features, e.g. that the
local state space had a higher dimension than seemed necessary to realize CHSH tests. The classification shows
that this is necessarily so. Along the way, we generalize the concept of self-testing to GPTs.

I.

INTRODUCTION

The search for physical principles that single out quantum mechanics (QM) among descriptions of Nature is a longstanding problem in the foundations of QM. The seminal
work of John S. Bell [1], and the subsequent Clauser-HorneShimony-Holt (CHSH) experiment [2], established contextuality as a principle that rules out classical descriptions of
Nature in favour of QM. So far, realizations of the ClauserHorne-Shimony-Holt (CHSH) experiment [3–5] have shown
that Nature is at least as contextual
√ as predicted by QM, i.e.,
they achieve a CHSH value of 2 2, which is also the maximal value for any quantum strategy (Tsirelson’s bound [6]).
What is still lacking is a physical principle that rules out theories (like boxworld [7]) which predict a larger CHSH value
than QM while still being consistent with the assumptions of
the CHSH experiment. There is a rich body of research exploring this problem [8–16]. Many such works are based on
the following observation: Violations of Bell inequalities predicted by QM tend to be, in general, strictly smaller than the
algebraically allowed maximum. Thus it is conceivable that
understanding the origin of this discrepancy leads to a physical principle that explains it.
Weilenmann and Colbeck have recently proposed the adaptive CHSH game [17, 18] as a task that may explain this discrepancy. They conjecture that the biggest
√ CHSH value allowed in the adaptive CHSH game is 2 2, and that the same
value is recovered in the usual CHSH experiment because it
is a special case of the former. The adaptive CHSH game involves performing entanglement swapping before the CHSH
test. Thus it probes the strength of correlations supported by
both bipartite states and bipartite effects. The (convex) sets
describing states and measurements are dual to each other.

∗ ldmello@thp.uni-koeln.de
† david.gross@thp.uni-koeln.de

Thus, expanding one set, in order to reach stronger correlations, inevitably diminishes the other. In this regard, QM
strikes a particular balance, which is why it appears reasonable to conjecture that QM would be optimal for the adaptive
CHSH game.
In fact, QM has a stronger property: There exist quantum
strategies for which the CHSH value is preserved not only after one round of entanglement swapping, but also after an arbitrary number of rounds. This property is highly constraining,
in the sense that many known examples of general probabilistic theories (GPTs) fail to exhibit it. However, in our previous
work [19] we constructed a GPT called oblate stabilizer theory
(OST), which not only has this feature, but can also achieve a
CHSH value of 4. Thus, in view of OST, it is unclear exactly
what kind of constraints this property imposes on GPTs. In
this work we deduce these constraints and as a result classify
GPTs with this property.
This classification also sheds light on various other aspects
such as the resonablilty of the assumption of local tomography
and the existence of redundant degrees of freedom in OST.
In the process of obtaining the main result we also generalize the notion of self-testing to GPTs.

A.

General Probabilistic Theories

General probabilistic theories (GPTs) [20–28] is a framework that allows us to describe correlations that are compatible with operationally motivated assumptions (e.g. nosignaling), but are not necessarily realized in QM. The goal
of such a framework is to study the observations of QM in
a broader setting in order to extract the underlying physical
principles governing them.
In this work we adopt the GPT formalism (with minor modifications) from our previous work (Ref. [19]). Here we provide an overview of the formalism and the modifications. For
a more detailed description, please refer to Sec. I and Sec. II
of [19]. For a general overview of the GPT formalism we refer

<!-- page 2 -->
2
the reader to [28]. We assume that a GPT is specified by
• A finite-dimensional real vector space V .

The (convex) set of all those elements of P (n) whose negation
is also in P (n) is called the effect space E (n) , i.e.,
E (n) := P (n) ∩ ¬P (n) .

• A collection of closed, pointed convex cones1 ,
∀n ∈ N, P (n) ⊆ V ⊗n ,
where V

⊗n

is the standard n-fold tensor product of V .

This definition implies that
e ∈ E (n) ⇔ e ∈ P (n) and ¬e ∈ P (n) ,
from which it directly follows that

• A distinguished element 1 in the relative interior2 of
P (1) .
We call P (n) the effect cones and 1 the unit effect. The effects model measurement outcomes, in the sense that the effect e encodes the probability of obtaining the outcome labelled by e. The unit effect in particular, models the trivial
measurement, which encodes the fact that in every experiment some outcome must occur. Therefore, a set of effects
(n)
defines a measurement if,
{ei }m
i=1 ⊆ P
m
X

ei = 1⊗n .

i=1

In this formalism, states are viewed as linear functionals on
effects. To this end let (P (n) )′ ⊆ (V ⊗n )∗ be the polar dual3
of P (n) . We choose a set of pointed cones ∀n ∈ N : D(n) ⊆
(P (n) )′ , that are generating4 on span(P (n) )∗ , called the state
cones. The convex sets
S (n) := {ρ ∈ D(n) | ρ(1⊗n ) = 1},
are called the state spaces of the GPT. The state spaces are
compact sets (App. VI B), a fact that will be important later
(Sec. III D).
The first deviation from the formalism in [19] is that we do
not require that the state and effect cones are generating with
respect to the ambient spaces V ⊗n and their duals. This is
in order to be able to discuss the notion of local tomography
in the latter part of this work (Sec. III H). More precisely, in
this paper, we will look at cases where span(P (2) ) = V ⊗2
but span(P (1) ) ⊊ V . Further, it may seem peculiar that we
demand that D(n) be a generating cone on span(P (n) )∗ . This
is all to say that, on a mathematical level, all we are doing is
embedding cones defined as per [19, 28] into (possibly) larger
ambient spaces.
Let e ∈ P (n) , define the negation of e as
¬e := 1⊗n − e.

1 A convex cone is said to be closed if it contains all it’s limit points with

respect to some topology. In the present case, since we work with finite
dimensional real vector spaces, we take the standard topology. A convex
cone P is said to be pointed if P ∩ −P = {0}.
2 The relative interior of a convex cone is the interior of the cone with the
ambient space taken to be the affine hull of the cone.
3 The polar dual P ′ of a convex cone P is the set of all non-negative linear
functionals on P .
4 A convex cone is said to be generating if it spans the ambient space.

e ∈ E (n) ⇔ ∀ρ ∈ S (n) , 0 ≤ ρ(e) ≤ 1.
That is, the pairing between any effect e and state ρ is not
only positive, but also bounded above by 1. As such it will be
interpreted as the probability of obtaining the outcome corresponding e given we prepared the state ρ. Additionally, every
element of P (n) with this property is in E (n) .
1.

Constructing a GPT from a set of states and effects

It is often the case that we seek to determine whether it is
possible to achieve certain correlations in some experimental
scenario. Addressing this question typically only requires us
to specify states and measurements which, if employed in the
experiment, reproduce the correlations in question. Therefore,
it is convenient to have an algorithmic procedure that takes a
collection of states and effects and turns it into a GPT that
contains them.
Algorithm 1 of [19] provides a straight-forward “closure
construction” that addresses exactly this problem. In this
work, in contrast to the treatment in [19], we do no assume
that GPTs are invariant under permutation of subsystems.
Thus, when we refer to the GPT closure of sets of states and
effects, we mean the output of Algorithm 1 of [19] with the
symmetrization step omitted.
The focus of this work is the iterated CHSH game introduced in [19], which is a generalization of the adaptive CHSH
game of [17, 18]. It can be stated by combining only bipartite
states and effects. For this reason, we will typically consider
only GPTs generated by taking the GPT closure of bipartite
objects.
B.

The CHSH scenario

The CHSH scenario consists of two space-like-separated
parties (usually called Alice and Bob), each of whom possesses a two-setting two-outcome measurement machine.
These two parties perform an experiment where, in every
round, they choose one of two measurement settings and measure a shared bipartite state.
Given a GPT, define an instance of the CHSH scenario as a
choice of four effects – ei , fj ∈ E (1) , i, j ∈ {0, 1} – and a bipartite state ρ ∈ S (2) . The effect e0 specifies the two-outcome
measurement corresponding to setting 0 of Alice, i.e., the effects e0 , ¬e0 model the two outcomes respectively. Analogously e1 for setting 1 of Alice, and, f0 and f1 for Bob. ρ
models the bipartite state shared by Alice and Bob.

<!-- page 3 -->
3
Let Ai , Bj , i, j ∈ {0, 1} be the ±1 valued observables corresponding to the measurement settings of Alice and Bob respectively. In terms of the effects they are defined as follows:
Ai := ei − ¬ei ,

Bj := fj − ¬fj .

(1)

The observable of interest for the CHSH scenario is given by
B := A0 ⊗ B0 + A0 ⊗ B1 + A1 ⊗ B0 − A1 ⊗ B1 .
We call this the standard CHSH observable.
Given an instance – ρ, ei , fj – of the CHSH scenario, the
pairing ρ(B) is called the CHSH value of the instance. The
CHSH value of the GPT is then the supremum over the CHSH
values of all possible instances from the GPT.
The CHSH inequality is the following Bell inequality
ρ(B) ≤ 2,
respected by all classical theories. A GPT is said to violate
CHSH if there exist at least one instance that violates the
CHSH inequality.
C.

The teleportation semigroup

Here we provide a short summary of the formalization of
teleportation in the GPT framework (Ref. [12, 29]). In analogy to QM, teleportation refers to the process where we perform a joint bipartite measurement on one half of a bipartite
state and a local state, producing a local state as a result (as depicted in Fig.1). For the mathematical definition, it is useful to
keep in mind that we here regard states and linear functionals
on effects. Given a bipartite state ρ, a bipartite measurement
{ϕk }k , and a local state σ, conditioned on obtaining the outcome k, we get the state σk defined by the following map:
σk : e 7→ ⟨ϕk ⊗ e, σ ⊗ ρ⟩,
for all local effects e.
An equivalent way to look at the same situation is as follows: Bipartite states are isomorphic to bilinear forms on local effects, and vice versa. Thus with every bipartite state we
can associate a map ρ̂ from the effect cone to the state cone,
defined by
ρ̂ : e 7→ ρ(e, ·).

(2)

i

&k
S
(a)

(b)

S

FIG. 2. The possible ways to pair a bipartite state with a bipartite
effect. (a) Depicts the usual pairing ρ(ϕk ). In order to translate it
into the trace pairing, we have to introduce a transpose to one of
the two maps: tr(ρ̂T ϕ̂k ). (b) Depicts the other way to pair the two,
namely by “closing the loop”. In order to translate this pairing into a
trace we do not have to introduce a transpose: tr(ρ̂ϕ̂k ). Such pairings
arise when the type of subsystems, which the “legs” of the states and
effects correspond to, are restricted (see Sec. III A).

In other words, ρ̂ sends every effect e to the functional ρ(e, ·).
Similarly, bipartite effects can also be viewed as maps from
the state cone to effect cone
ϕ̂k : σ 7→ ϕk (σ, ·).
We use the above equivalence liberally in this work, i.e., we
take ρ and ρ̂ to mean one and the same thing, operationally
speaking. Under this isomorphism pairings between bipartite states and bipartite effects become the trace of a product
of maps. There are two ways to do this, the usual pairing
(Fig. 2 (a)) is given by
ρ(ϕk ) = tr(ρ̂T ϕ̂k ),
where ρ̂T is the map corresponding to the bilinear form obtained by switching the tensor factors of ρ (upon choosing a
basis, this corresponds to the matrix transpose). It is also possible to stagger the states and effects and “close the loop” in
order to pair them (Fig. 2 (b)). In this case the pairing is given
by tr(ρ̂ϕ̂k ), and, depending on the situation, it might not have
an analog to ρ(ϕk ).
A special case of Fig. 2 (a) is when the effect of product
type. Given local effects, e for Alice and f for Bob, e[
⊗f
denotes the map
e[
⊗ f : σ 7→ σ(e)f.
In terms of this map, we can write the pairing ρ(e, f ) as
ρ(e, f ) = tr(ρ̂T e[
⊗ f ) = tr(ρ̂f[
⊗ e) = ρ̂(e)(f ).

&k
:
J

S

Th

FIG. 1. Diagrammatic representation of teleportation. The joint measurement {ϕk }k on a local state σ and one-half of a bipartite state ρ,
results in a local state σk , when conditioned on the measurement outcome corresponding to ϕk .

The last term in the above equation denotes the following:
First apply the map ρ̂ to the effect e of Alice to obtain the
state ρ̂(e) on Bob. Then evaluate ρ̂(e) on the effect f of Bob.
Concatenating the maps associated with bipartite states and
effects yields ρ̂ϕ̂k , a map from states to (sub-normalized)
states. The set of maps {ρ̂ϕ̂k }k generates a semigroup. Consider an element of this semigroup, e.g., (ρ̂ϕ̂k1 ) · · · (ρ̂ϕ̂kN ).
Physically, the image of a local state under this map corresponds to teleporting the local state N times and obtaining the
list of outcomes (k1 , · · · , kN ). Mathematically, the resulting

<!-- page 4 -->
4
local state is sub-normalized by a factor equal to probability
of obtaining the outcomes (k1 , · · · , kN ). Given a GPT, we
call the set of all maps generated in this way the teleportation
semigroup of the GPT. The teleportation semigroup also captures the phenomenon of entanglement swapping, which can
be described as the application of elements of the semigroup
to one half of a bipartite state.

D.

Outline

In terms of the terminology introduced in Sec. I A, I B, and
I C, the conjecture of [17] stems from the observation that
large CHSH values and the existence of teleportation protocols are at odds, in the sense that teleportation works to decrease the strength of CHSH correlations. Indeed, there are
many GPTs with very strong CHSH correlations where the set
of states accessible after (iterated) teleportation can produce
only classical correlations, e.g., boxworld [7, 27, 28], composite GPTs [19], even-polygon theories [17, 18, 30]. However, in our previous work [19] we presented a first example
of a GPT (OST) that retains a CHSH value of 4, indefinitely,
under entanglement swapping.
In view of these results, one can ask: What are the constraints imposed on GPTs by the requirement that they maintain a high CHSH value even after repeated teleportation?
Here we answer this question under mild technical assumptions. In Section II we develop a tool required to arrive at our
results, namely GPT self-testing, which is a generalization of
quantum self-testing to the GPT framework. In Section III, we
show that if certain correlations (c.f. Sec. III C) are maintained
in the iterated CHSH scenario, then there exists an effective
GPT (c.f. Sec. III E) on which the teleportation maps are reversible transformations, thus form a group. The positivity
conditions on this group will turn out to be highly constraining (c.f. Sec. III F): Every such GPT is a member of one of
seven, inequivalent, representation-theoretically defined families. Towards the end of this section we discuss the quantum realizations of these families (Sec. III G), and the implications our classification results have for the local tomography
assumption (Sec. III H).
Our results are to be contrasted with the work of D’Ariano,
Chiribella, and Perinotti [12]. They have discussed a system
of axioms on GPTs that are strong enough to derive QM. They
also arrive at the conclusion that there must be a compact
group structure associated with teleportation. However, the
axioms used in their work are much stronger than what we
consider here. For example, we do not assume that every state
has a purification.

For example,
√ in the CHSH scenario, if we measure a CHSH
value of 2 2 then any quantum model that explains this correlation is isomorphic to specific Pauli observables being measured on the Bell state [31, 32].
Here we generalize this notion to the framework of general
probabilistic theories in the sense that:
“For certain correlations, any two instances (from possibly
different GPTs) achieving the correlation lead to equivalent
effective GPTs”.
Here, by effective GPT we mean “the GPT obtained by discarding irrelevant degrees of freedom”. In the case of CHSH,
given an instance of the CHSH scenario, we can define the
effective CHSH GPT as “the GPT obtained by ignoring all degrees of freedom unreachable from the instance”. Concretely,
Definition 1 (The effective CHSH GPT). Let ρ, ei , fj be an
instance of the CHSH scenario. Define ΩA := {ei , ¬ei }i=0,1 ,
and ΩB := {fj , ¬fj }j=0,1 . Then, the effective CHSH GPT is
the GPT closure (c.f. Sec. I A 1) of the input: P
 = cone ΩA ⊗
ΩB , D = cone {ρ} ∪ ρ(·, ΩB ) ⊗ ρ(ΩA , ·) .
As mentioned in Sec. I A 1, in the above definition the permutation symmetry between the subsystems is broken. The
left subsystem of ρ must always be paired with Alice’s effects
and the right subsystem with Bob’s.
The notion of two GPTs being equivalent to each other is
formalized as follows: Given that a GPT is specified by the
following tuple of data


V, 1, {P (n) }n∈N , {D(n) }n∈N ,
we can define:
Definition 2 (GPT isomorphism). Two GPTs


(n)
(n)
V1 , 11 , {P1 }n∈N , {D1 }n∈N
and


GPT SELF-TESTING

(n)



are said to be isomorphic if there exists a linear map γ : V1 →
V2 such that:
1. γ(11 ) = 12 ;
2. For every n ∈ N, the restriction
(n)

(n)

γ ⊗n : span(P1 ) → span(P2 )
is invertible, with
(n)

II.

(n)

V2 , 12 , {P2 }n∈N , {D2 }n∈N

γ ⊗n P1

(n)

= P2

and

(n)

(γ −t )⊗n D1

(n)

= D2 ,

where γ t is the canonical transpose5 of γ.
Self-testing is a notion that is established in the setting of
quantum theory. In essence, it refers to the fact that:
“For certain correlations, the quantum model realizing the
correlation is unique up to isomorphisms”.

→ W , its canonical transpose Lt : W ∗ → V ∗
is defined by: ∀f ∈ W ∗ , v ∈ V, (Lt f )(v) = f (Lv).

5 Given a linear map L : V

<!-- page 5 -->
5
A.

Lemma 4. Any two instances achieving a CHSH value of 4
lead to equivalent effective GPTs.

CHSH self-testing correlations

In quantum
√ theory, any instance that achieves a CHSH
value of 2 2 leads to a unique effective CHSH GPT. This
is a consequence of the well-known stronger result that even
the quantum model is unique [31, 32]. The main result of this
section is that any theory achieving a CHSH value of 4 also
has a unique effective CHSH GPT.
First we show that the following pattern of correlations are
sufficient to self-test the corresponding GPTs:
Lemma 3. Given an instance – ρ, ei , fj – of the CHSH scenario, the following conditions are sufficient for uniqueness of
the effective CHSH GPT: For Ai , Bj as defined in Eqn. 1, and
some a ∈ ( 21 , 1],
1. ρ(Ai ⊗ 1) = ρ(1 ⊗ Bj ) = 0;

ρ((−1)ij Ai ⊗ Bj ) = 1.

(4)

Applying ρ to
Ai ⊗ Bj = ei ⊗ fj + ¬ei ⊗ ¬fj − (ei ⊗ ¬fj + ¬ei ⊗ fj ),
1 ⊗ 1 = ei ⊗ fj + ¬ei ⊗ ¬fj + ei ⊗ ¬fj + ¬ei ⊗ fj
directly yields
ρ(ei ⊗ ¬fj ) = ρ(¬ei ⊗ fj ) = 0
ρ(e1 ⊗ f1 ) = ρ(¬e1 ⊗ ¬f1 ) = 0.

(i, j) ̸= (1, 1),

Plugging in the definition of negation for the case (i, j) ̸=
(1, 1) gives

2. ρ((−1)ij Ai ⊗ Bj ) = a.
The first condition translates to the marginals being uniform. The second conditions encodes both that all four correlators contribute equally and that the CHSH inequality is
violated.
Proof. We prove this by showing that the above conditions
fix every pairing needed to specify the effective CHSH GPT.
Using Ai = ei − ¬ei , condition 1 yields

⇒

ρ(ei ⊗ 1) − ρ(ei ⊗ fj ) = ρ(1 ⊗ fj ) − ρ(ei ⊗ fj )
ρ(ei ⊗ 1) = ρ(1 ⊗ fj ).
(5)

For the case (i, j) = (1, 1), it gives
ρ(e1 ⊗ f1 ) = 1 − ρ(1 ⊗ f1 ) − ρ(e1 ⊗ 1) + ρ(e1 ⊗ f1 )
⇒
1 = ρ(1 ⊗ f1 ) + ρ(e1 ⊗ 1).
(6)
Combining Eqs. (5) and (6) yields

ρ(ei ⊗ 1) = ρ(¬ei ⊗ 1)
= ρ(1 ⊗ 1) − ρ(ei ⊗ 1)
= 1 − ρ(ei ⊗ 1).

ρ(ei ⊗ 1) = ρ(1 ⊗ fj ) = 12 .
This is equivalent to the uniform marginals condition (see
proof of Lem. 3).

Applying the same argument to Bj we can conclude that
ρ(ei ⊗ 1) = ρ(1 ⊗ fj ) = 12 .

Proof. Let – ei , fj , ρ – be an instance of the CHSH scenario
with CHSH value 4. Since |ρ(Ai ⊗ Bj )| ≤ 1 we necessarily
have

(3)

Now consider ρ(Ai ⊗ Bj ). Using Eqn. (3), and v − ¬v =
2v − 1, we can re-write this as
ρ(Ai ⊗ Bj )
= 4ρ(ei ⊗ fj ) − 2(ρ(ei ⊗ 1) + ρ(1 ⊗ fj )) + ρ(1 ⊗ 1)
= 4ρ(ei ⊗ fj ) − 1.
Thus from condition 2 we get
ρ(ei ⊗ fj ) = 41 (1 + (−1)ij a).
Finally, a > 21 implies that the CHSH inequality is violated.
As a consequence, {1, e0 , e1 } must be linearly independent.
This is because, if it were not the case, there would exist a
joint measurement machine for the measurements {e0 , ¬e0 }
and {e1 , ¬e1 }, implying that the CHSH inequality cannot be
violated. Similarly for {1, f0 , f1 }. Thus if there is another
instance ρ′ , e′i , fj′ with the same CHSH value (i.e., 4a) satisfying the two conditions, then the map specified by ei 7→ e′i ,
fj 7→ fj′ , and 1 7→ 1′ is a GPT isomorphism.
Using the above Lemma, we can conclude the following:

III. CLASSIFICATION OF PROBABILISTIC THEORIES
WITH A STABLE CHSH VALUE UNDER TELEPORTATION.

Here we investigate the structure imposed on GPTs by
the requirement that they maintain their CHSH value even
after multiple rounds of teleportation (entanglement swapping). The clear choice of task for this purpose is the iterated CHSH game introduced in [19]. For a number of rounds
N ∈ N, the iterated CHSH game is played by N + 2 parties – Alice, Charlie and N further parties, whom we will
refer to as the “Bobs”. The game is specified by the following data: A bipartite state ρ ∈ S (2) , an n-outcome bipartite
measurement M = {ϕk }k∈[n] ⊆ E (2) ([n] denotes the index
set {1, . . . , n}), and two pairs of two-outcome measurements
ΩA = {ei , ¬ei }i=0,1 ⊆ E (1) and ΩC = {fj , ¬fj }j=0,1 ⊆
E (1) . These data remain fixed throughout the game. In particular, this implies that Alice and Charlie are not allowed to
change their measurement devices. Each round of the game
proceeds as follows:
1. First, the N Bobs perform the bipartite measurement
M on N + 1 copies of the bipartite state ρ to produce:
(i) The bipartite state σ (as depicted in Fig. 3 (a)), and
(ii) A list of outcomes ⃗k ∈ [n]N ;

<!-- page 6 -->
6

Jo

&

&k

...

bit

an

=

S

S

5

4

S

S

-

S

(a)

E
S

S

S

Es

S

. ...
8

2

#

S

S
S

S

(b)
FIG. 3. (a) The resulting (sub-normalized) state after the Bobs perform entanglement swapping. (b) The most general experiment that
can be performed given the data specifying the iterated CHSH game.
Here Φi ∈ conv(M ∪ ΩC ⊗ ΩA ), i.e., that can be either product
or entangled (or a convex combination of both). The iterated CHSH
game is a special case of this setup where e.g. Φ1 is chosen to be a
product effect from ΩC ⊗ ΩA and the rest of the Φi are chosen from
M. This is because choosing one of the Φi to be a product effect
allows us to “break the loop” and unravel it into an instance of the
Iterated CHSH game.

2. Next Alice and Charlie perform a CHSH test on σ.
Given the outcome ⃗k they are allowed to declare which
version CHSH inequality they intend to test. The
eight different versions are related to each other by
a relabelling of settings, outcomes, and parties (see
App. VI C).
The goal of this section is to construct the effective GPT,
analogously to one introduced in Sec. II, describing every experiment that can be built out of the data specifying the iterated CHSH game. One might assume that this includes
only experiments of the kind where Alice and Charlie perform a (product) measurement on the type of states depicted
in Fig. 3 (a). This is not the case since it is also possible to
bring the ends of this long chain together and measure M on
it again. Because such a situation must also be described by
our GPT, the most general scenario, given an instance of iterated CHSH, is the one depicted in Fig. 3 (b). In this figure,
the effects Φi can be taken to be either product or entangled.
To capture the fact that it is always possible to realize correlations that are in the convex hull of these two situations, we
take Φi ∈ conv(M ∪ ΩC ⊗ ΩA ).
A.

Eliminating irrelevant degrees of freedom

In Sec. I A, we introduced the space V in terms of which
the mathematical descriptions of measurements and states are
modeled. The effective GPT will contain only a subset of all
states and measurements. As a result, the original spaces, V
and V ∗ , are “too large”, e.g. in the sense that V ∗ now contains

mathematically distinct states that are no longer distinguishable with respect to the remaining measurements. Therefore,
in the spirit of self-testing we eliminate the now redundant
degrees of freedom from our mathematical description.
As one can see from Fig. 3 (b), Alice will always perform
measurements on the left subsystem of the state ρ, while Charlie only has access to the right subsystem. Likewise, the left
subsystem of a bipartite effect in {ϕk }k∈[n] is contracted with
the right subsystem of a state ρ and vice-versa. Thus the invariance under permutation of subsystems is broken. We will
refer to the left subsystem of ρ as being of “A-type”, and the
right subsystem as being of “C-type”. Instead of using one
mathematical object V for all single-party subsystems, a minimal description will assign different spaces VA , VC to these
two different types.
Lemma 5. The effective GPT can be described in terms of
spaces VA , VC with the following property: The map ρ̂ :
VA → VC∗ , associated to the bipartite state ρ in the sense
of Eq. (2), is a linear isomorphism.
Proof. For a number N ∈ N of rounds, the probability distributions generated by experiments of the form Fig. 3 (b) are
given by


tr (ρ̂Φ̂1 ) · · · (ρ̂Φ̂N ) ,

where Φi ∈ conv M ∪ (ΩC ⊗ ΩA ) .
Now, Let ker ρ̂ and img ρ̂ be the kernel and image of the
map ρ̂ respectively. Choose decompositions
V = U ⊕ ker ρ̂,

V ∗ = img ρ̂ ⊕ W ∗ .

Clearly ρ̂ induces an isomorphism ρ̃ : U → img ρ̂. Thus we
claim that
VA := U,

VC := (img ρ̂)∗ ,

are the spaces whose existence is posited by the lemma.
To prove this, we have to show that, for an appropriate restriction of the effects, the probability distributions generated
by the restricted state and effects are identical to the distributions generated by the original ones. Let π be the projector
onto U along ker ρ̂, and let ι be the embedding of img ρ̂ into
V ∗ . Then we can obtain the maps induced by the original
effects as
ϕ̃k := π ϕ̂k ι : img ρ̂ → U,
and similarly
f]
⊗ e := π(f[
⊗ e)ι,
for f ⊗ e ∈ ΩC ⊗ ΩA . And indeed, this restriction leaves the
probability distributions unchanged:




tr (ρ̃Φ̃1 ) · · · (ρ̃Φ̃N ) = tr ρ̃(π Φ̂1 ι) · · · ρ̃(π Φ̂N ι)


= tr (ιρ̃π)Φ̂1 · · · (ιρ̃π)Φ̂N


= tr (ρ̂Φ̂1 ) · · · (ρ̂Φ̂N ) ,
where we have used that ιρ̃π = ρ̂ by construction.

<!-- page 7 -->
7
Hereafter we assume that the above reduction has already
been made, i.e., the data for the iterated CHSH game is: ρ ∈
(VA ⊗ VC )∗ , M ⊆ VC ⊗ VA and ΩC ⊗ ΩA ⊆ VC ⊗ VA .

The corresponding state after after one round of entanglement
swapping, conditioned on obtaining outcome k of M, can be
written in terms of Rk as:
σ̂ = p1k Rk ρ̂,

B.

The relabelling group

The iterated CHSH game allows Alice and Charlie to
choose a CHSH inequality based on the measurement outcomes obtained by the Bobs. All eight versions of the CHSH
inequality arise from each other by exchanging the labels of
the measurement settings or outcomes of just one of the two
parties (see App. VI C). It turns out that analyzing the group
action of these “relabelling operations” on the mathematical
description of the GPT is very fruitful.
As an example, say we relabel the settings of Alice. Mathematically, this constitutes a group action on ΩA , namely
e0 ↔ e1 , ¬e0 ↔ ¬e1 . Operationally, this gives us another
two-setting two-outcome measurement machine which violates the CHSH inequality with A0 and A1 exchanged, which
links it to the following group action on the CHSH observables:
A0 C0 + A0 C1 + A1 C0 − A1 C1
↕
A0 C0 − A0 C1 + A1 C0 + A1 C1 .
The outcome relabelling admits a similar description. This
relabelling group action has the following properties:
• Exchanging setting and outcome labels each constitute
a Z2 action. Since the exchange of setting labels permutes the exchange of outcome labels, the full group is
a wreath product (see [33] Section 1.6) of the two Z2
actions. The wreath product of Z2 with itself is isomorphic to the dihedral group of order 8, denoted by D4
(see exercises of [33] Section 1.6).
• This group action is free (i.e. every CHSH observable is
stabilized only by the identity), and transitive (i.e. any
two CHSH observables can be mapped onto each other
by a suitable relabeling). See App. VI C for further details.
These properties imply that we can rephrase the second step
of the iterated CHSH game as follows
“Based on ⃗k, Alice and Charlie are allowed to pick the
CHSH inequality that they will test.”
↕
⃗
“Based on k, Alice relabels her measurement device. Alice
and Charlie then perform the CHSH test with respect to the
standard CHSH observable.”
This rephrasing will allow us to relate the teleportation
maps (refer Fig. 4) that appear in the entanglement swapping
step of the iterated CHSH game to the local corrections applied by Alice, which forms a group. Indeed, define the teleportation maps as follows:
Rk := ρ̂ϕ̂k : VC∗ → VC∗ .

where pk := Rk ρ̂(1)(1), is the probability of obtaining the
outcome k. Extend this definition to N rounds as follows: For
each outcome ⃗k = (k1 , · · · , kN ) that can occur, define
R⃗k := Rk1 · · · RkN .
Then the resulting bipartite state is
σ̂ = p1⃗ R⃗k ρ̂,
k

with p⃗k defined analogously. Because ρ̂ is an isomorphism,
the state σ̂ is in a one to one correspondence with the map
1
k . By assumption, there exists a map that that assigns to
p⃗k R⃗
each outcome ⃗k a correction from D4 . The correction need
only depend on the state realized between Alice and Charlie conditioned on obtaining ⃗k, i.e., if two different outcomes
⃗k, ⃗k ′ correspond to the same state, then the corrections must
also be the same. Hence, there exists a map ϑ that sends each
realizable p1⃗ R⃗k to an element of D4 . Let S be the set of all
k
realizable teleportation maps:
n
o
(7)
S := p1⃗ R⃗k ⃗k ∈ [n]N , N ∈ N .
k

Then
ϑ:

S → D4 ,
1
k 7→ ϑ⃗
k.
p⃗k R⃗

(8)

Then, under the aforementioned rephrasing, we can describe
the iterated CHSH game mathematically as follows: The Bobs
each measure M and obtain outcome ⃗k, which implies that
the bipartite state between Alice and Charlie is p1⃗ R⃗k ρ̂. Next,
k

Alice applies the relabelling ∀e ∈ ΩA , e 7→ ϑ⃗−1 e. Finally,
k
Alice and Charlie perform the usual CHSH test. The resulting
correlations are described by the distribution on e⊗f ∈ ΩA ⊗
ΩC given by:
e⊗f

7→

−1
1
e)(f ).
k ρ̂(ϑ⃗
p⃗k R⃗
k

Remark: In this formalization, Rk acts on C-type subsystem of the state in Schrödinger picture, whereas ϑ⃗k acts on
A-type local observables in Heisenberg picture. In particular,
the “last error introduced on Charlie’s side, must be corrected
first by Alice’s correction”, which is why we chose the correction to be phrased in terms of ϑ⃗−1 . Below we’ll see that these
k
conventions make ϑ a homomorphism.

&k
S
FIG. 4. Diagrammatic representation of the teleportation map Rk .

<!-- page 8 -->
8
C.

Sufficient condition for classification

The iterated CHSH scenario stands almost in analogy to the
CHSH scenario in the following sense: There exists a sufficient condition on the correlations generated by an instance of
the iterated CHSH game, satisfying which, the effective GPT
generated will belong to one of seven inequivalent families (as
opposed to being unique).
In this section, we state a sufficient condition for our classification result and derive some primliminary consequences of
the same. The fact that this condition is sufficient will only be
clear by the end of Sec. III F. The condition is as follows:
Condition 1. For the instance of the iterated CHSH game
under consideration, it holds that, for every N ∈ N and every
outcome ⃗k,
• the CHSH value remains constant, and is equal to the
value without any entanglement swapping (N = 0),
and
• it satisfies the two self-testing conditions of Lem. 3.
Remarks: (1) Condition 1 allows for the possibility that the
CHSH value of the instance is smaller than that of the GPT
from which it originated. As long as this CHSH value is preserved in the iterated CHSH game, the effective GPT (which
will be constructed later) will be subject to the classification
result. (2) If the CHSH value of the theory is equal to 4, then
stability under teleportation implies Condition 1.
Now, without loss of generality, we can assume that every
outcome k ∈ [n] of M has non-zero probability (pk ̸= 0).
This is because every ϕk with pk = 0 can be grouped (by
summing the effects) with any ϕl with pl ̸= 0. Under this assumption we have the following consequence of Condition 1:

while on the right hand side it gives
1
pl Rl ρ̂(ϑk e)(f ) = ρ̂(ϑl ϑk e)(f ).

Equating both sides leads to
pl◦k
pl pk ρ̂(ϑl◦k e)(f ) = ρ̂(ϑl ϑk e)(f ).

Since the action of ϑ⃗k is free, and ∀k ∈ [n], pk ̸= 0, we can
conclude: pl◦k = pl pk ̸= 0, and ϑl◦k = ϑl ϑk . Iterating this
proves the claim.
In light of Lem. 6 we can make two further assumptions
about the measurement M. These assumptions are similar to
the one made before Lem. 6, i.e., they involve “lowering the
resolution” of the measurement M, without loss of generality,
in order to make it simpler. Thus we call this step “coarsegraining”.
Lemma 7 (Coarse-graining). Without loss of generality we
can assume the measurement M = {ϕk }k∈[n] to have the
following properties:
1. Every correction in the image of ϑ can already be realized in M, i.e.,
H := {ϑk }k∈[n]
is a subgroup of D4 ;
2. Every outcome k ∈ [n] corresponds to a different correction;
Proof. For (1), since the D4 group is of order 8, the set
8
[

i=1

contains all the corrections that could occur. Thus we replace
M by the measurement

Lemma 6. For any instance of the iterated CHSH game satisfying Condition 1, it holds that S (Eqn. (7)) is a semigroup
and ϑ (Eqn. (8)) a semigroup homomorphism.
Proof. Given Condition 1, Lemma 3 applies and we can conclude that for every outcome ⃗k, and local effects e ∈ ΩA and
f ∈ ΩC ,
−1
1
e)(f ) = ρ̂(e)(f ),
k ρ̂(ϑ⃗
p⃗k R⃗
k

i.e. the correlations after relabeling are identical to the ones
obtained in the CHSH test without any entanglement swapping.
Specialize the above to N = 1, and set e′ := ϑ−1
k e, to get
′
′
1
pk Rk ρ̂(e )(f ) = ρ̂(ϑk e )(f ).

Applying p1l Rl to the left hand side and substituting e′ 7→ e
gives
1
1
1
pl Rl pk Rk ρ̂(e)(f ) = pl pk Rl◦k ρ̂(e)(f )
= ppll◦k
pk ρ̂(ϑl◦k e)(f ),

{ϑ⃗k | ⃗k ∈ [n]i }

1
8

8
[

{ρ̂−1 R⃗k | ⃗k ∈ [n]i }.

i=1

Now group together every effect that corresponds to the same
correction to achieve (2).
D.

Properties of the teleportation semigroup

In this section we investigate the properties of the semigroup S (Lem. 6) generated by an instance of the iterated
CHSH game that satisfies Condition 1.
Lemma 8. The closure S of the semigroup S is a compact
topological semigroup.
Proof. The elements of S are linear maps on a finitedimensional vector space. Hence their composition is continuous. Therefore S is a topological semigroup. S is closed
by construction. The elements of S ρ̂ are all states, as their
pairing with 1⊗2 is 1. Hence S ρ̂ is a closed subset of the state
space S (2) , which is a compact set (c.f. App. VI B). Thus S ρ̂
is a compact set. Finally, S is simply the image of S ρ̂ under
the right action of ρ̂−1 , which implies S is compact.

<!-- page 9 -->
9
To proceed, we need the following result which holds for
compact topological semigroups (in general) and hence in particular for S . The result is a direct corollary of Theorem 16.3
and Lemma 16.1 of [34].

Theorem 11. The map φ is a representation of the group H
with the following properties:

Theorem 9. The semigroup S contains a minimal right-ideal
which, in turn, contains at least one idempotent P . Moreover,
GP := P S P is a compact topological group, with neutral
element P .

2. The trivial representation has multiplicity 1 in the irrep
decomposition of φ.

For the remainder of the discussion, we fix one such idempotent P . The final result will not depend on which one has
been chosen.
Lemma 10. The character χP afforded by GP is nonnegative.
Proof. For every outcome ⃗k, p1⃗ R⃗k ρ̂ is an element of the bik

partite state space S . Every g ∈ GP arises as the limit of
operations of the form p1⃗ R⃗k . Thus, since S (2) is closed, it
(2)

k

follows that g ρ̂ is also an element of S (2) . Therefore, fixing
any ϕk ∈ M we have

tr g ρ̂ ϕ̂k ≥ 0.
Using the fact that P is the identity of GP we get



tr g ρ̂ ϕ̂k = tr (P gP ) Rk = tr g (P Rk P ) .
But P Rk P is of the form pk h for some h ∈ GP . Thus, for
any g ′ ∈ G , choosing g := g ′ h−1 gives
χP (g ′ ) = χP (gh) = pk tr(gP Rk P ) ≥ 0.

Now we turn our attention back to the correction map ϑ :
S → D4 . The map may be extended to S by continuity.
Indeed, if a pair R, R′ ∈ S are sufficiently close together,
then the respective corrections ϑ, ϑ′ must be the same. This
holds because there is a unique correction that attains the
CHSH value (4a), while any other correction will cause the
CHSH value to deviate from its maximum by at least 2a > 0.
But the CHSH value is a continuous function on bipartite
states and hence a continuous function of R.
Remark: It follows that S decomposes into a set of disconnected components, on which the correction map is constant.
Restricting this map to the compact group GP ⊆ S , we
obtain a group homomorphism from GP into D4 . We will use
the same letter, ϑ, for the map GP → D4 .
Since the image of ϑ is H ⊆ D4 , we have
GP / ker ϑ ∼
= H.
Let µ be the Haar measure on ker ϑ. Then
Z
Πφ :=
dµ(g) g

(9)

Both properties relate directly to the physics of the situation. Regarding the first point, it turns out that the values of
the character can be expressed as a pairing between states and
effects, and is thus non-negative. The proof of the second fact
relates the rank of the projection onto the trivial representation
to the rank of the marginal state shared by Alice and Charlie.
The marginal state is of rank one because it factorizes by construction.
Proof. The map φ is the restriction of GP to the subspace that
is invariant under ker ϑ ⊴ GP . Arguing as in the proof of
Lemma 10, it holds that gρ ∈ S (2) for every g that appears in
the integral in Eq. (10). Because the Haar measure is normalized and S (2) a convex set, Πφ ρ̂ is a state. In particular, this
means that img(Πφ ) is non-trivial. Thus it is a representation
of the quotient group H.
For (1) we first choose a transversal of GP / ker ϑ in order
to compute the character. Indeed by Lem. 7, every element of
M correspond to a unique correction in H, and thus the set

gk := P p1k Rk P | k ∈ [n]
is in one-one correspondence with the elements of H, and
hence is a transversal of GP / ker ϑ. Now, for any k ∈ [n]
we can compute
χφ (k) = tr(Πφ gk Πφ ) = tr(gk Πφ )
Z
=
dµ(l)χP (gk l) ≥ 0,
l∈ker ϑ

where we have used that the character χP is non-negative
(Lem. 10).
We prove (2) by bounding the multiplicity of the trivial representation above and below by one. The lower bound always
holds for a non-negative character of a finite group. This is
because the character inner product of any non-negative character χ with the trivial character χ1 yields
X
X
1
1
[χ, χ1 ] = |G|
χ1 (g)∗ χ(g) = |G|
χ(g) > 0,
g∈G

g∈G

since χ(1) > 0.
For the upper bound, we show that (i) The trivial representation is a subspace of the +1 eigenspace of the map
X
pk Πφ gk Πφ ,
k∈[n]

(10)

g∈ker ϑ

is a projection onto the trivial representation of the normal
subgroup ker ϑ ⊴ GP . Let g ∈ GP and define the map
φ : H → L(img Πφ ), ϑ(g) 7→ Πφ gΠφ .

1. Its character χφ is non-negative.

and that (ii) The rank of this map is upper bounded by 1. Indeed, by definition, for any v in the trivial representation, we
have ∀k ∈ [n], Πφ gk Πφ v = v, and thus
 X

X
pk Πφ gk Πφ v =
pk v = v,
k∈[n]

k∈[n]

<!-- page 10 -->
10
hence (i) follows. For (ii), using Πφ P = P Πφ = Πφ , which
is a consequence of the definition of Πφ (Eqn. (10)), and the
fact that ∀g ∈ GP , P gP = g and P 2 = P , we expand the
map:
X
X
pk Πφ gk Πφ =
pk Πφ P p1k Rk P Πφ
k∈[n]

k∈[n]

=

X

Rev
S

hi

J ...

Jp

do

..

·

pint

Par=

-

Πφ R k Πφ

S

S

S

S

S

S

Ri

Pa

S

The

k∈[n]

= Πφ

 X


R k Πφ

k∈[n]

= Πφ

 X


ρ̂ϕ̂k Πφ

FIG. 5. The two ways to read the result of entanglement swapping.
One can either read it as first applying the map ρ̂ : VA → VC∗ and
then the map R⃗k : VC∗ → VC∗ or first the map L⃗k : VA → VA and
then the map ρ̂ : VA → VC∗ .

k∈[n]

= Πφ ρ̂

 X


ϕ̂k Πφ

k∈[n]


= Πφ ρ(1, ·)1 Πφ .
The map
ρ(1, ·)1 : VC∗ → VC∗ , σ 7→ σ(1)ρ(1, ·)

is manifestly of rank one, and hence Πφ ρ(1, ·)1 Πφ is of
rank at most one. Thus (ii) and (2) follow.
There are two dual ways to describe entanglement swapping experiments: Either as teleporting C-type states, or as
teleporting A-type effects (c.f. Fig. 5). The map Rk used so
far formalizes the former point of view. For the latter, define
Lk := ϕ̂k ρ̂ : VA → VA .
Extending this definition to L⃗k (analogously to R⃗k ), we find
that L⃗k and R⃗k are conjugate to each other with respect to ρ̂:
L⃗k = ρ̂−1 R⃗k ρ̂.
This allows us to replicate the results for subsystems of Ctype, on subsystems of A-type as follows: Conjugating S by
ρ̂ gives us Lem. 8 for the semigroup generated by elements
of the form p1k Lk . Next, since P is obtained as a convergent
sequence of elements of the form p1⃗ R⃗k , the map ρ̂−1 P ρ̂ is
k

a convergent sequence of elements of the form p1⃗ L⃗k . Thus
k
we also get Thm. 9 on subsystems of A-type, where the compact group is ρ̂−1 GP ρ̂. The rest of the results – Lem. 10 and
Thm. 11 – follow by invariance under conjugation. Thus we
get a representation of H on the subsystems of A-type equivalent to the representation φ as follows: For h ∈ H
π(h) := ρ̂−1 φ(h)ρ̂.
The corresponding representation space is supported on the
image of the projection Ππ := ρ̂−1 Πφ ρ̂.
Now that we have a representation space both on A-type
and C-type subsystems, we can construct the effective GPT
of the iterated CHSH game.

E.

The effective Iterated CHSH GPT

Mimicking the approach of Sec. II, here we define the effective Iterated CHSH GPT as the GPT generated by the states
and effects that are required to realize the iterated CHSH
game. A representation-theoretic analysis will show that the
effective GPTs that arise this way fall into one of seven inequivalent families.
Definition 12 (The effective I-CHSH GPT). Let ρ, ϕk , ei , fj
be an instance of the iterated CHSH game satisfying Condition 1. Let H be the associated correction group (Eqn. (9)).
Let ΩA := {ei , ¬ei }i=0,1 , ΩC := {fj , ¬fj }j=0,1 . Let ρ̃ be
the bilinear form associated with the map Πφ ρ̂Ππ . Define the
sets
• Ω̃A := Ππ ΩA , Ω̃C := Πtϕ ΩC ,

• Ψ := φ(h)Πφ ρ̂Ππ h∈H ,

• Φ := Ππ ϕ̂k Πφ k∈[n] .
Then the effective I-CHSH GPT is the GPT closure (in the

sense of Sec. I A 1) of the input: P = cone Φ ∪ Ω̃C ⊗ Ω̃A ,

D = cone Ψ ∪ ρ̃(·, Ω̃C ) ⊗ ρ̃(Ω̃A , ·) .
Remarks: (1) In the above definition, D ⊆ img(Ππ )∗ ⊗
img(Πφ ) and P ⊆ img(Πφ )∗ ⊗ img(Ππ ). (2) effective ICHSH GPT will turn out to be not locally tomographic. We
discuss this further in Sec. III H.

F.

The seven families

The representation φ of the correction group H, and hence
the effective I-CHSH GPT, are subject to the following constraints:
1. φ has dimension at least three. This holds because we
need local dimension at least 3 to violate CHSH.
2. The character of the representation χφ has to be nonnegative (Thm. 11).

<!-- page 11 -->
11
3. The trivial character χ1 occurs exactly once in the decomposition of χφ (Thm. 11).
The correction group H is one of the following groups: The
trivial group, Z2 (the cyclic group of order two), Z4 (the cyclic
group of order four), K4 (the Klein four-group), and D4 (the
dihedral group of order eight). Of these, we can rule out the
trivial group and Z2 for the following reasons:
• The only irreducible character afforded by any representation of the trivial group is the trivial character χ1 .
Due to constraint (3), χφ = χ1 is the only option. This
representation is one-dimensional and hence ruled out
by constraint (1).
• The irreducible characters of Z2 are the trivial character
χ1 and χ2 = (1, −1). Thus the only possibilities given
constraints (2) and (3) are χφ = χ1 and χφ = χ1 + χ2 .
Both are ruled out by constraint (1).
The remaining groups – Z4 , K4 and D4 – all contribute
solutions. The character tables for these groups are recorded
in App. VI A.
Let Ξ represent the character table of any of the three
groups. The above three constraints correspond to the following system of Diophantine inequalities in the rows of Ξ:
Let r = rows(Ξ), and ni ∈ N for i = [r], then
Pr
1. i=1 ni Ξi1 ≥ 3,
Pr
2. ∀j ∈ [r], i=1 ni Ξij ≥ 0,
3. n1 = 1.
In the present case, this system of inequalities was solved using the SageMath computer algebra system [35] (the computer
code can be found here [36]). The result is as follows:
(H)

Result 13. Let {χi }i (refer App. VI A) be the irreducible
characters respectively of H = Z4 , K4 , and D4 . Then, using
the convention
χ(i1 )j1 ···(in )jn = j1 χ1 + · · · + jn χn ,
χφ has to be one of the following seven characters:
(Z )

(K )

(D )

(D )

(D )

4
4
• dim = 4 : χ1234
, χ1234
, χ1254 , χ1354 , χ1454 , where the
first two are the regular character of Z4 and K4 respectively;

(D )

4
;
• dim = 6 : χ12345

(D )

4
• dim = 8 : χ12345
2 , the regular character of D4 .

In dim = 4, the computer algebra system reports an addi(D4 )
tional solution, namely χ1234
. The representation affording
(K4 )
this character is isomorphic to the one affording χ1234
, and
thus is not listed above.
Result 13 states that any effective I-CHSH GPT necessarily
falls into one of seven families. It is not a priori clear that
all seven of these families are inhabited, i.e., it is possible to
construct an example of each type. Resolving this question in
the affirmative, we construct explicit GPTs for each family in
Appendix VI D.

G.

Quantum family members

In this section we collect some positive and negative results
regarding which of the families in Result 13 can be realized
within quantum theory.
In quantum mechanics, (i) one can realize an√iterated CHSH
game that maintains QM’s CHSH value of 2 2. Moreover,
(ii) any such realization satisfies Condition 1. Indeed, for (i),
consider the instance where Alice measures in Pauli X and Z
bases, Charlie measures in bases that is rotated by π/4 in the
Pauli X–Z-plane, the shared bipartite state is the Bell state
|Φ+ ⟩ = √12 (|00⟩ + |11⟩),
and the measurement M is the Bell basis measurement, i.e.,
the measurement in the basis {σk ⊗1|Φ+ ⟩}k=0,...,3 , with σ0 =
1 and σk , k = 1, . . . , 3 being Pauli X, Y and Z respectively.
In this instance, the bipartite state conditioned on outcome
k of M corresponds to the the element of the Bell basis labelled by k. Every element of the Bell basis can be mapped
back to |Φ+ ⟩ by Alice, by applying the appropriate Pauli correction. This correction corresponds to an action of σk by
conjugation on Alice’s measurement effects. Pauli operators
acting by conjugation correspond to a K4 group action, which
can be realized by relabelling Alice’s measurement apparatus.
After the relabelling, the situation is simply that of the usual
Bell test.
Alternatively, if we are given a quantum instance of√the iterated CHSH game which achieves a CHSH-value of 2 2 for
every N ∈ N and every outcome ⃗k, then
√ point (ii) follows
quantum self-testing of CHSH-value 2 2. This is because
the conditions on the observables Ai , Cj due to self-testing
imply the conditions of Lem. 3 (c.f. [32]).
The above instance of the iterated CHSH game is a mem(K4 )
ber of the family χ1234
. What is yet unclear is whether we
can construct members of other families within QM. Recall
that by Wigner’s Theorem [37, 38], a symmetry group acting on density operators must result from a projective unitary
or anti-unitary representation on Hilbert space. Anti-unitaries
are not completely positive, and therefore not physically implementable. Hence we can restrict attention to symmetry
groups that allow for a projective unitary representation on
the underlying Hilbert space. As a consequence, we have
(Z )

4
Lemma 14. The family labelled by χ1234
cannot be realized
within QM.

Proof. Assume for the sake of reaching a contradiction that
(Z4 )
family within
it is possible to realize members of the χ1234
quantum theory. Then the corresponding representation of Z4
must come from a projective unitary representation on Hilbert
space. Every projective representation of a cyclic group is
projectively equivalent to a linear representation [39, Theorem 2.3.1] (originally [40]). In particular, the linear representation on Hilbert space is abelian, and thus admits a common
eigenbasis {|ψi ⟩}i . Hence, at the level of density matrices, the
projections |ψi ⟩⟨ψi | are invariant under the Z4 action. The basis has at least two elements, because no Bell inequalities can

<!-- page 12 -->
12
be violated with a one-dimensional local Hilbert space. This
implies that the trivial representation has multiplicity at least
two in the decomposition of the representation on the density
matrices, contradicting the fact that the trivial representation
has multiplicity 1 (Thm. 11 (2)).
Since the group K4 is also abelian, it’s trivial projective
class would be subject to the same restrictions as Z4 . However, K4 also admits a non-trivial projective class. This nontrivial projective class is represented on Hilbert space by the
Pauli matrices (c.f. [39, Section 3.6]), and accounts for the
(K4 )
family χ1234
.
(D )
It is also possible to realize the family χ1254 QM. However,
since the corresponding representation is four-dimensional
and the group D4 has order eight, this family cannot be re(K4 )
alized as a basis measurement, in contrast to χ1234
. However
it is possible to realize it as a POVM. Let |bk ⟩ = σk ⊗ 1|Φ+ ⟩
and |ak ⟩ = Sσk ⊗ 1|Φ+ ⟩, where S is the phase operator with
S 2 = σz = σ3 . Then the choosing M to be the following
POVM


M := 21 |bk ⟩⟨bk | k=0,...,3 ∪ 21 |ak ⟩⟨ak | k=0,...,3 ,
along with the Bell state and the Pauli measurements of the
standard Bell test (noted in the beginning of this section,
(D )
Sec. III G), realizes a member of χ1254 . The question of
whether the rest of the families have a quantum realization
is left open.

H.

GPT pancakes

A conceptual consequence of Result 13 is that iterated entanglement swapping games can give an operational justification for constructing GPTs that violate the local tomography
postulate.
Local tomography is a commonly made assumption [11, 12,
27, 41, 42] (also discussed in [43–45]) that states that in a
probabilistic theory, the product effects should span the space
of all effects. In this case, a state can be characterized from
the result of product measurements alone, hence the name.
The effective I-CHSH GPT (Def. 12) and all the examples
constructed in App. VI D violate this principle. Their local
effect space is three-dimensional (spanned by the observables
required to implement CHSH tests), but the characterization
in Result 13 lists no solution with three local dimensions. Intuitively, the reason is that the space spanned by the tensor
product of the effects needed to specify the CHSH experiment
is “too small” to support the bipartite effects that are used in
entanglement swapping. Thus the violation of local tomography is justified by the operational requirement of being able
to perform entanglement swapping.
In the context of qubit quantum mechanics, there is a theorem, colloquially called the “no-pancake theorem” [46, 47],
that states that there is no completely positive map whose domain is the Bloch ball and whose image is contained in a plane
(i.e., a “pancake”). The elements of the teleportation semigroup of a GPT are required to be completely positive on the

GPT by consistency. Thus in analogy to the QM case, under the assumption of local tomography, we can conclude a
similar result:
Lemma 15 (GPT no-pancake theorem). In any locally tomographic GPT, which contains at least one instance of the
iterated CHSH game satisfying Condition 1, the directional
vector space of the image of the local state space under the
teleportation semigroup of the GPT must be of dimension at
least three.
In particular, Lem. 15 tells us that there are no locally tomographic GPTs with local dimension three or less (recall that
the local dimension is one more than the dimension of the directional vector space of the state space). This gives us an
alternative proof of the fact that it is not possible to perform
entanglement swapping in boxworld theory, or any of the regular polygon GPTs of [30].
IV.

CONCLUSIONS AND OUTLOOK

The initial motivation of this work came from Refs. [17,
18]. Their premise is that “sustaining a CHSH value after
teleportation” is a rare property for probabilistic theories to
have – potentially so rare that an operational characterization
of quantum correlations could be based on them. In Ref. [19],
we provided initial evidence against this conjecture, by constructing a post-quantum GPT with this property.
In the present work, we show that the requirement that a
theory sustains its CHSH value after teleportation does highly
constrain its structure. Maybe surprisingly, this invariance
property gives rise to a representation-theoretic condition, all
solutions of which can be explicitly enumerated.
In this sense, the property of Refs. [17, 18] is rare after
all – just not sufficiently so to single out QM without further
assumptions.
Beyond that, our “seven-fold way” classification provides
an operational justification for rejecting local tomography as
an axiom for probabilistic theories: The space spanned by the
product effects needed to realize the CHSH test is insufficient
to support the effects required for entanglement swapping.
One of the tools required to obtain our results was a notion
of self-testing in the framework of GPTs, which we have also
introduced in this work. GPT self-testing is a generalization
of quantum self-testing to the GPT framework. It involves
making uniqueness statements about the theory obtained by
discarding all degrees of freedom that are irrelevant to the situation at hand. It would be interesting to explore this approach
further, and identify other scenarios where GPTs can be selftested.
Finally, we have left open the question exactly which of the
seven family members can be realized within QM.
V.

ACKNOWLEDGEMENTS

We are grateful to Marc-Olivier Renou for motivating this
project, Johan Åberg for all the great questions and feedback

<!-- page 13 -->
13
throughout the course of this work, Joachim Krug for providing insights on semigroups, and all of Elie Wolfe, Rob
Spekkens, Lucas Tendrik, Markus Methlinger, Martin Renner,
Nicolas Brunner, Pavel Sekatski, Sadra Boreiri and Xiangling
Xu for helpful discussion.

Parts of this work was conducted while one of us (LD)
was kindly hosted by the Perimeter Institute for Theoretical
Physics. We acknowledge support by Germany’s Excellence
Strategy – Cluster of Excellence Matter and Light for Quantum Computing (ML4Q), EXC 2004/1 (390534769).

[1] J. S. Bell, On the einstein podolsky rosen paradox, Physics
Physique Fizika 1, 195 (1964).
[2] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, Proposed experiment to test local hidden-variable theories, Physical review letters 23, 880 (1969).
[3] A. Aspect, J. Dalibard, and G. Roger, Experimental test of bell’s
inequalities using time-varying analyzers, Phys. Rev. Lett. 49,
1804 (1982).
[4] G. Weihs, T. Jennewein, C. Simon, H. Weinfurter, and
A. Zeilinger, Violation of bell’s inequality under strict einstein
locality conditions, Phys. Rev. Lett. 81, 5039 (1998).
[5] M. A. Rowe, D. Kielpinski, V. Meyer, C. A. Sackett, W. M.
Itano, C. Monroe, and D. J. Wineland, Experimental violation
of a bell’s inequality with efficient detection, Nature 409, 791
(2001).
[6] B. S. Cirel’son, Quantum generalizations of bell’s inequality,
Letters in Mathematical Physics 4, 93 (1980).
[7] S. Popescu and D. Rohrlich, Quantum nonlocality as an axiom,
Foundations of Physics 24, 379 (1994).
[8] M. Pawłowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter, and M. Żukowski, Information causality as a physical principle, Nature 461, 1101 (2009).
[9] N. Miklin and M. Pawłowski, Information causality without
concatenation, Phys. Rev. Lett. 126, 220403 (2021).
[10] T. Fritz, A. B. Sainz, R. Augusiak, J. B. Brask, R. Chaves,
A. Leverrier, and A. Acı́n, Local orthogonality as a multipartite
principle for quantum correlations, Nature Communications 4,
2263 (2013).
[11] L. Hardy, Quantum theory from five reasonable axioms (2001),
arXiv:quant-ph/0101012 [quant-ph].
[12] G. M. D’Ariano, G. Chiribella, and P. Perinotti, Quantum Theory From First Principles : an informational approach. (Cambridge Univ Press, 2019).
[13] A. Wilce, A royal road to quantum theory (or thereabouts), Entropy 20, 10.3390/e20040227 (2018).
[14] G. Brassard, H. Buhrman, N. Linden, A. A. Méthot, A. Tapp,
and F. Unger, Limit on nonlocality in any world in which communication complexity is not trivial, Physical Review Letters
96, 250401 (2006).
[15] N. Linden, S. Popescu, A. J. Short, and A. Winter, Quantum
nonlocality and beyond: limits from nonlocal computation,
Physical review letters 99, 180502 (2007).
[16] M. Navascués and H. Wunderlich, A glance beyond the quantum model, Proceedings of the Royal Society A: Mathematical,
Physical and Engineering Sciences 466, 881 (2010).
[17] M. Weilenmann and R. Colbeck, Self-testing of physical theories, or, is quantum theory optimal with respect to some
information-processing task?, Phys. Rev. Lett. 125, 060406
(2020).
[18] M. Weilenmann and R. Colbeck, Toward correlation self-testing
of quantum theory in the adaptive clauser-horne-shimony-holt
game, Phys. Rev. A 102, 022203 (2020).
[19] L. J. Dmello, L. T. Ligthart, and D. Gross, Entanglement swapping in generalized probabilistic theories and iterated clauser-

horne-shimony-holt games, Phys. Rev. A 110, 022225 (2024).
[20] I. E. Segal, Postulates for general quantum mechanics, Annals
of Mathematics , 930 (1947).
[21] G. Ludwig, Attempt of an axiomatic foundation of quantum
mechanics and more general theories, ii, Communications in
Mathematical Physics 4, 331 (1967).
[22] G. Ludwig, Attempt of an axiomatic foundation of quantum
mechanics and more general theories, iii, Communications in
Mathematical Physics 9, 1 (1968).
[23] G. Dähn, Attempt of an axiomatic foundation of quantum
mechanics and more general theories. iv, Communications in
Mathematical Physics 9, 192 (1968).
[24] P. Stolz, Attempt of an axiomatic foundation of quantum mechanics and more general theories v, Communications in Mathematical Physics 11, 303 (1969).
[25] P. Stolz, Attempt of an axiomatic foundation of quantum mechanics and more general theories vi, Communications in Mathematical Physics 23, 117 (1971).
[26] E. B. Davies and J. T. Lewis, An operational approach to quantum probability, Communications in Mathematical Physics 17,
239 (1970).
[27] J. Barrett, Information processing in generalized probabilistic
theories, Physical Review A 75, 032304 (2007).
[28] M. Plávala, General probabilistic theories: An introduction,
Physics Reports 1033, 1 (2023), general probabilistic theories:
An introduction.
[29] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, Teleportation in
general probabilistic theories (2008), arXiv:0805.3553 [quantph].
[30] P. Janotta, C. Gogolin, J. Barrett, and N. Brunner, Limits on
nonlocal correlations from the structure of the local state space,
New Journal of Physics 13, 063024 (2011).
[31] S. J. Summers and R. Werner, Bell’s inequalities and quantum
field theory. i. general setting, Journal of Mathematical Physics
28, 2440 (1987).
[32] I. Šupić and J. Bowles, Self-testing of quantum systems: a review, Quantum 4, 337 (2020), arXiv:1904.10042v4.
[33] D. J. S. Robinson, A Course in the Theory of Groups, 2nd ed.,
Graduate Texts in Mathematics, Vol. 80 (Springer, New York,
1996).
[34] T. Eisner, B. Farkas, M. Haase, and R. Nagel, Operator theoretic aspects of ergodic theory, Vol. 272 (Springer, 2015).
[35] The Sage Developers, SageMath, the Sage Mathematics
Software
System
(Version
10.7)
(2026),
https://www.sagemath.org.
[36] L. J. Dmello and D. Gross, Representations of H =
Z4 , K4 , D4 affording a positive character (2026).
[37] E. Wigner, Group theory: and its application to the quantum
mechanics of atomic spectra, Vol. 5 (Elsevier, 2012).
[38] V. Bargmann, Note on wigner’s theorem on symmetry operations, Journal of Mathematical Physics 5, 862 (1964).
[39] G. Karpilovsky, Projective Representations of Finite Groups,
Pure and applied mathematics, Vol. 94 (Marcel Dekker, Inc.,
New York and Basel, 1985).

<!-- page 14 -->
14
[40] I. Schur, Über die darstellung der endlichen gruppen durch gebrochene lineare substitutionen, Journal für die reine und angewandte Mathematik 127, 20 (1904).
[41] L. Hardy, Reconstructing quantum theory (2013),
arXiv:1303.1538 [quant-ph].
[42] M. P. Müller, Probabilistic theories and reconstructions of quantum theory, SciPost Phys. Lect. Notes , 28 (2021).
[43] H. Barnum and A. Wilce, Local tomography and the jordan
structure of quantum theory, Foundations of Physics 44, 192
(2014).
[44] T. S. Lismer, K. B. Felefele, R. W. Spekkens, and K. J.
Resch, Experimental test of the principle of tomographic locality (2025), arXiv:2506.07775 [quant-ph].

VI.
A.

[45] T. D. Galley and L. Masanes, Any modification of the Born rule
leads to a violation of the purification and local tomography
principles, Quantum 2, 104 (2018).
[46] M. Beth Ruskai, S. Szarek, and E. Werner, An analysis of
completely-positive trace-preserving maps on m2, Linear Algebra and its Applications 347, 159 (2002).
[47] R. Blume-Kohout, Decoherence and beyond, Ph.D. thesis, University of California, Berkeley (2005).
[48] I. M. Isaacs, Character Theory of Finite Groups, Pure and Applied Mathematics, Vol. 69 (Academic Press, New York, 1976).
[49] B. Simon, Representations of Finite and Compact Groups,
Graduate Studies in Mathematics, Vol. 10 (American Mathematical Society, Providence, RI, 1996).

APPENDIX

The dihedral group of four elements

The content of this appendix is based on the references [48], [49], and [33]. The details were computed by hand.
The dihedral group of four elements D4 , is the symmetry group of the square. It is realized as the semi-direct product of two
cyclic groups, namely
D4 = ⟨ξ⟩ ⋊ ⟨η⟩ ∼
= Z4 ⋊ Z2 .
Where ξ 4 = 1 and η 2 = 1, and ηξ k η = ξ −k . What will be an important feature in our discussion is that D4 is isomorphic to the
wreath product of Z2 with itself, i.e.,
D4 ∼
= Z2 ≀ Z2 .
The conjugacy classes(K ) and corresponding centralizers(C ) of D4 are as follows:
K1 = {1},
C1 = D4 ,

Kξ = {ξ, ξ 3 },
Cξ = ⟨ξ⟩,

Kξ2 = {ξ 2 },
Cξ2 = D4 ,

Kη = {η, ξ 2 η},

Cη = ⟨{ξ 2 , η}⟩,

Kξη = {ξη, ξ 3 η}.

Cξη = ⟨{ξ 2 , ξη}⟩.

There are 5 conjugacy classes. This means the number of representative irreps of the group algebra C[D4 ] are |M (C[D4 ])| = 5.
Also the dimension of the group algebra dim C[D4 ] = 8. Therefore we have M (C[D4 ]) = {Mi }i=1,··· ,5. , and
5
X
(dim Mi )2 = 8.
i=1

The only solution is 12 + 12 + 12 + 12 + 22 , i.e., there is one 2D irrep and four linear irreps. This information is sufficient to
deduce the character table of D4 , which is as follows:
KD4 K1 Kξ Kξ2 Kη Kξη
irrep

|KD4 | 1

2

1

2

2

|CD4 |

8

4

8

4

4

χ1

1

1

1

1

1

trivial

χ2

1

1

1

−1 −1

D4 /Z4

χ3

1 −1

1

1

−1

(−1)π(g)

χ4

1 −1

1

−1

1

D4 /Z4 ⊗ (−1)π(g)

χ5

2

−2

0

0

planar roto-reflections

0

TABLE I. The character table of D4

<!-- page 15 -->
15
The subgroups of D4 are
O(1) : 1;
O(2) : ⟨ξ 2 ⟩, ⟨η⟩, ⟨ξη⟩, ⟨ξ 2 η⟩, ⟨ξ 3 η⟩;
O(4) : ⟨ξ⟩, ⟨{ξ 2 , η}⟩, ⟨{ξ 2 , ξη}⟩;
O(8) : D4 .
Out of these the order 4 subgroups, namely K4 and Z4 , are of interest. Their character tables are as follows:
KK4 K1 Kξ2 Kη Kξ2 η

KZ 4 K1 Kξ Kξ 2 Kξ 3

χ1

1

1

1

1

χ1

1

1

1

1

χ2

1

1

−1 −1

χ2

1

i

−1

−i

χ3

1

−1

1

−1

χ3

1 −i −1

i

χ4

1

−1 −1

1

χ4

1 −1

−1

TABLE II. The character table of K4

1

TABLE III. The character table of Z4

B.

Appendix to Sec. I A

Lemma. The state space S (n) is a compact set.
Proof. The definition of D(n) is such that the cone lies entirely in span(P (n) )∗ , where it is a closed, pointed, generating,
convex cone (see Sec. I A). Thus it is sufficient for the sake of this proof to restrict the ambient spaces of D(n) and P (n) to be
span(P (n) )∗ and span(P (n) ) respectively, and thus assume D(n) and P (n) to be closed, pointed, generating, convex cones (see
footnotes in Sec. I A for definitions).
Since we are in finite dimensions it is sufficient to show that S (n) is closed and bounded. The cone D(n) is closed by definition
(Sec. I A) and 1⊗n is a continuous linear functional. S (n) arises as the intersection of D(n) and the pre-image of 1 under 1⊗n
(c.f. definition in Sec. I A) and thus is closed.
By definition 1⊗n is in the relative interior of P (n) ⊂ (D(n) )′ (the polar dual of D(n) , see footnote in Sec. I A). Therefore,
taking the ambient space to be span(P (n) ) implies that 1⊗n is in fact in the interior of P (n) . As a consequence, it is a strictly
positive functional on D(n) , i.e., it is positive on D(n) \ {0}. Assume for the sake of reaching a contradiction that 1⊗n is positive
but not strictly positive on D(n) . Then, there exists some σ ∈ D(n) such that σ(1⊗n ) = 0. Since 1⊗n is a continuous functional
in the interior of (D(n) )′ , there exists some perturbation of p of 1⊗n in the interior of (D(n) )′ such that σ(p) < 0. This contradicts
the fact that p ∈ (D(n) )′ .
Now, let S1 be the unit sphere with respect to the Euclidean norm. Because D(n) is closed, the intersection D(n) ∩ S1 is a
compact set. Let λmin > 0 be the minimum value attained by 1⊗n on D(n) ∩ S1 . Then the norm ball B1/λmin of radius 1/λmin
contains S (n) . Thus S (n) is compact.
C.

Action of the relabelling group on the CHSH observables

Denote the standard CHSH observable by
A0 B0 + A0 B1 + A1 B0 − A1 B1 ≡ (+ + + −).
Using this convention we can denote all CHSH observables by
{±π(+ + + −) | π ∈ S4 }.
For example, exchanging Alice’s settings yields the following
A1 B0 + A1 B1 + A0 B0 − A0 B1 ≡ A0 B0 − A0 B1 + A1 B0 + A1 B1 ≡ (+ − + +).
Now, we can define the action of the relabeling group on the CHSH correlators as follows
¬(0) A0 = ¬e0 − e0 = −A0 ,

(s 7→ s)B1 = f0 − ¬f0 = B0 .

<!-- page 16 -->
16
Using this we can define a group action on the CHSH observable. For example,
¬(0) ⊗ 1(+ + + −) = (− − + −),

1 ⊗ (s 7→ s)(+ + + −) = (+ + − +)

Choosing the following realization of D4
ξ := (s ↔ s)(o ↔ −o)(0)

η := (o ↔ −o)(0) ξ,

and

D4 = ⟨ξ⟩ ⋊ ⟨η⟩,

with

(11)

we get
ξ

ξ

ξ

ξ

e0 7→ ¬e1 ;

ξ

ξ

ξ

ξ

f0 7→ ¬f1 ;

e0 7→ ¬e1 7→ ¬e0 7→ e1 7→ e0 ;
f0 7→ ¬f1 7→ ¬f0 7→ f1 7→ f0 ;

η

e1 7→ ¬e0 ;

η

1 7→4 1;

η

f1 7→ ¬f0 ;

η

1 7→4 1.

D
D

This corresponds the following action on the correlators
ξA

ξA

ξA

ξA

A0 7→ −A1 ;

ξB

ξB

ξB

ξB

A0 7→ −A1 7→ −A0 7→ A1 7→ A0 ;
B0 7→ −B1 7→ −B0 7→ B1 7→ B0 ;

ηA

A1 7→ −A0 ;

ηA

B0 7→ −B1 ;

ηB

B1 7→ −B0 ;

ηB

And finally, the following action on the CHSH observables
ξA

ξA

ξA

ξA

ηA

ξA

ξA

ξA

ξB

ξB

ξB

ξB

ηB

ξB

ξB

ξB

(Alice) :(+ + + −) 7→ (+ − − −) 7→ (− − − +) 7→ (− + + +) 7→ (+ + + −);
(+ + + −) 7→ (− + − −) 7→ (− − + −) 7→ (+ − + +) 7→ (+ + − +).
(Bob) :(+ + + −) 7→ (+ − − −) 7→ (− − − +) 7→ (− + + +) 7→ (+ + + −);
(+ + + −) 7→ (− − + −) 7→ (− + − −) 7→ (+ + − +) 7→ (+ − + +).
D.

Representatives of each of the seven families

Here we provide an explicit member of each of the seven families of GPTs.
(1) For the Z4 representation we will take the correction group to be generated by


0 1



−1 0
ξ=
.

−1 
1
p √
For the local effects, set r = a 2, where a ∈ ( 12 , 1] and 4a is the CHSH value. Then for Alice choose
T
1= 0001 ,

T
e0 = 21 r 0 0 1 ,

T
e1 = 12 0 r 0 1 .

The effects of Charlie are defined in terms of a π/4 rotation, i.e.,
√1
2
 √1
− 2
R=



f0 = Re1 ,

f1 = Re0 ,

with



√1
2
√1
2




.


1
1

Let γ : v 7→ ⟨v, ·⟩ be the isomorphism induced by the Euclidean inner product. Define ρ by
ρ(e ⊗ f ) := γ(e)(f ),

(12)

that is, ρ̂ = γ. This gives us
ρ(1 ⊗ 1) = 1,

ρ(ei ⊗ 1) = ρ(1 ⊗ fj ) = 12 ,

and


ρ(ei ⊗ fj ) = 14 1 + (−1)ij a .

<!-- page 17 -->
17
Finally, for the measurement of the Bobs choose
M = {ϕ̂k := 14 ξ k γ −1 | k = 0, 1, 2, 3}.
The construction for the rest of the solution is almost identical. In fact or all other other dim = 4 representations, the only
difference is the matrices that generate the group. The rest – choice of ρ, ei , fj – are identical.
(2) For K4 the group is generated by the matrices




−1
−1




1
−1




ξ2 = 
.
 and η = 


−1 
1 
1
1
And

M = ϕ̂g := 41 gγ −1 | g ∈ ⟨{ξ 2 , η}⟩ .
(D )

(D )

(D )

(3) For χ1254 , χ1354 , and χ1454 , the groups are generated respectively by




0 1
−1




1
−1 0



ξ125 = 
 , and η125 = 
;


1 
−1 
1
1




−1
0 1




1
−1
0




ξ135 = 
;
 , and η135 = 


1 
−1 
1
1




−1
0 1




1


−1 0

ξ145 = 
.
 , and η145 = 


−1 
−1 
1
1
Again with

M = ϕ̂g := 81 gγ −1 | g ∈ D4 .
(D )

(D )

4
4
(4) For χ12345
and χ12345
2 we have to slightly modify the local effects, namely we pad them with enough zeros to make
(D4 )
6
8
elements of R and R respectively. For example, for χ12345
we have:

T
1= 000001 ,

T
e0 = 21 r 0 0 0 0 1 ,

T
e1 = 12 0 r 0 0 0 1 .

The matrix R is padded with 1 on the diagonal to make the dimensions match in order to obtain the fj . The matrices generating
the groups follow the same block diagonal pattern (which can be read off of the character table). The bipartite state ρ̂ is once
again taken to be γ. The ϕ̂g are also chosen the same way.
In all the above examples, we have not specified any effects outside of those required for the CHSH test. And indeed one can
deduce that all these GPTs are not locally tomographic. Of course, they can all be completed to a locally tomographic GPT in
a simple way – pick any ONB {wi }i of the orthocomplement of the space spanned by the specified local effects, and add the
effects { 12 (wi ⊕ 1)}i as well as their negations.
