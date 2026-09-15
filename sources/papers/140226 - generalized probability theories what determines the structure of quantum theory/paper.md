---
type: paper
date: 2014-02-26
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1402.6562v3)
reviewed: false
---

# Generalized Probability Theories: What determines the structure of quantum theory?

Machine-generated and unreviewed text extraction of arXiv:1402.6562v3
(39 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1402.6562v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
TOPICAL REVIEW

arXiv:1402.6562v3 [quant-ph] 13 Aug 2014

Generalized Probability Theories:
What determines the structure of quantum theory?
Peter Janotta and Haye Hinrichsen
Universität Würzburg, Fakultät für Physik und Astronomie, 97074 Würzburg,
Germany
Abstract. The framework of generalized probabilistic theories is a powerful tool
for studying the foundations of quantum physics. It provides the basis for a variety
of recent findings that significantly improve our understanding of the rich physical
structure of quantum theory. This review paper tries to present the framework and
recent results to a broader readership in an accessible manner. To achieve this,
we follow a constructive approach. Starting from few basic physically motivated
assumptions we show how a given set of observations can be manifested in an
operational theory. Furthermore, we characterize consistency conditions limiting the
range of possible extensions. In this framework classical and quantum theory appear
as special cases, and the aim is to understand what distinguishes quantum mechanics
as the fundamental theory realized in nature. It turns out non-classical features of
single systems can equivalently result from higher dimensional classical theories that
have been restricted. Entanglement and non-locality, however, are shown to be genuine
non-classical features.

1. Introduction
Quantum theory is considered to be the most fundamental and most accurate physical
theory of today. Although quantum theory is conceptually difficult to understand, its
mathematical structure is quite simple. What determines this particularly simple and
elegant mathematical structure? In short: Why is quantum theory as it is?
Addressing such questions is the aim of investigating the foundations of quantum
theory. In the past this field of research was sometimes considered as an academic subject
without much practical impact. However, with the emergence of quantum information
theory this perception has changed significantly and both fields started to fruitfully
influence each other [1, 2]. Today fundamental aspects of quantum theory attract
increasing attention and the field belongs to the most exciting subjects of theoretical
physics.
In this topical review we will be concerned with a particular branch in this field,
namely, with so-called Generalized Probabilistic Theories (GPTs), which provide a
unified theoretical framework in which classical and quantum theory emerge as special

<!-- page 2 -->
Generalized Probability Theories

2

cases. Presenting this concept in the language of statistical physics, we hope to
establish a bridge between the communities of classical statistical physics and quantum
information science.
The early pioneers of quantum theory were strongly influenced by positivism, a
school of philosophy postulating that a physical theory should be built and verified
entirely on the basis of accessible sensory experience. Nevertheless the standard
formulation of quantum theory involves additional concepts such as global complex
phases which are not directly accessible. The GPT framework, which is rooted in the
pioneering works by Mackey, Ludwig and Kraus [3–6], tries to avoid such concepts as
much as possible by defining a theory operationally in terms of preparation procedures
and measurements.
As measurement apparatuses yield classical results, GPTs are exclusively concerned
with the classical probabilities of measurement outcomes for a given preparation
procedure. As we will see below, classical probability theory and quantum theory can
both be formulated within this unified framework. Surprisingly, starting with a small set
of basic physical principles, one can construct a large variety of other consistent theories
with different measurement statistics. This generates a whole spectrum of possible
theories, in which classical and quantum theory emerge just as two special cases. Most
astonishingly, various properties thought to be special for quantum theory turn out to
be quite general in this space of theories. As will be discussed below, this includes
the phenomenon of entanglement, the no-signaling theorem, and the impossibility to
decompose a mixed state into unique ensemble of pure states.
Although GPTs are defined operationally in terms of probabilities for measurement
outcomes, it is not immediately obvious how such a theory can be constructed from
existing measurement data. In this work we shed some light on the process of
building theories in the GPT framework on the basis of a set of given experimental
observations, making the attempt to provide step-by-step instructions how a theory can
be constructed.
The present Topical Review is written for readers from various fields who are
interested to learn something about the essential concepts of GPTs. Our aim is to
explain these concepts in terms of simple examples, avoiding mathematical details
whenever it is possible. We present the subject from the perspective of model building,
making the attempt to provide step-by-step instructions how a theory can be constructed
on the basis of a given set of experimental observations. To this end we start in Sect. 2.1
with a data table that contains all the available statistical information of measurement
outcomes. In Sect. 2.3 the full space of possible experimental settings is then grouped
into equivalence classes of observations, reducing the size of the table and leading to a
simple prototype model. As shown in Sect. 2.5 this prototype model has to be extended
in order to reflect possible deficiencies of preparations and measurements, leading in turn
to new suitable representations of the theory. This extension can be chosen freely within

<!-- page 3 -->
Generalized Probability Theories

3

Figure 1. Typical experimental setup consisting of a preparation procedure, a

sequence of intermediate manipulations, and a final measurement with a certain
set of possible classical outcomes (see text). The intermediate manipulations
can be thought of as being part of either the preparation procedure (dashed
box) or the measurement.

a certain range limited by certain consistency conditions (see Sect. 2.9). Depending on
this choice the extended theory finally allows one to make new predictions in situations
that have not been examined so far. Within this framework we discuss three important
minimal systems, namely, the classical bit, then quantum bit (qubit), as well as the socalled gbit, which can be thought of as living somewhere between classical and quantum
theory.
In Sect. 4 we devote our attention to the fact that any non-classical system is
equivalent to a classical system in a higher-dimensional state space combined with
certain constraints. However, this equivalence is only valid as long as non-composite
(single) systems are considered. Turning to bipartite and multipartite systems the theory
has to be complemented by a set of composition rules in the form of a suitable tensor
product (see Sect. 5). Again it turns out that there is some freedom in choosing the
tensor product, which determines the structure of a GPT to a large extent. Finally,
in Sect. 6 we discuss nonlocal correlations as a practical concept that can be used to
experimentally prove the existence of non-classical entanglement in composite systems
without the need to rely on a particular theory.
For beginners it is often difficult to understand the construction of a non-classical
theory without introducing concepts such as Hilbert spaces and state vectors. For this
reason we demonstrate how ordinary quantum mechanics fits into the GPT framework,
both for single systems in Sect. 3.6 and for composite systems in Sect. 7.
2. Generalized probabilistic theories: Single systems
2.1. Preparation procedures and measurements
As sketched schematically in Fig. 1, a typical experimental setup in physics consists
of a preparation procedure, possibly followed by a sequence of manipulations or
transformations, and a final measurement. For example, a particle accelerator produces
particles in a certain physical state which are then manipulated in a collision and finally

<!-- page 4 -->
Generalized Probability Theories

4

measured by detectors. Since the intermediate manipulations can be thought of as being
part of either the preparation procedure or the measurement, the setup can be further
abstracted to preparations and measurements only‡.
We can think of a measurement apparatus as a physical device which is prepared
in a spring-loaded non-equilibrium idle state. During the measurement process the
interaction of the physical system with the device releases a cascade of secondary
interactions, amplifying the interaction and eventually leading to a classical response
that can be read off by the experimentalist. This could be, for example, an audible
’click’ of a Geiger counter or the displayed value of a voltmeter.
In practice a measurement device produces either digital or analog results. For
analog devices there are in principle infinitely many possible outcomes, but due to
the final resolution the amount of information obtained during the measurement is
nevertheless finite. Thus, for the sake of simplicity, we will assume that the number of
possible outcomes in a measurement is finite.
For an individual measurement apparatus we may associate with each of the possible
outcomes a characteristic one-bit quantity which is ’1’ if the result occurred and ’0’
otherwise. In this way a measurement can be decomposed into mutually excluding
classical bits, as sketched in Fig. 1. Conversely every single measurement can be
interpreted as a joint application of such fundamental 1-bit measurements.
If we are dealing with several different measurement devices the associated classical
bits are of course not necessarily mutually excluding. This raises subtle issues about
coexistence, joint measurability, mutual disturbance and commutativity [7, 8], the
meaning of a ’0’ if the measurement fails, and the possibility to compose measurement
devices out of a given set of 1-bit measurements. For simplicity let us for now neglect
these issues and return to some of the points later in the article.
2.2. Toolbox and probability table
In practice we have only a limited number of preparation procedures and measurement
devices at our disposal. It is therefore meaningful to think of some kind of ‘toolbox’
containing a finite number of 1-bit measurements labeled by k = 1 . . . K and a finite
number of preparation procedures labeled by ` = 1 . . . L. As mentioned before, if the
range of preparations and measurements is continuous, we assume for simplicity that
the finite accuracy of the devices will essentially lead to the same situation with a finite
number of elements. Our aim is to demonstrate how the GPT approach can be used to
construct a physical theory on the basis of such a toolbox containing K measurement
devices and L preparation methods.
‡ In standard quantum theory the absorption of intermediate transformations into the preparation
procedure corresponds to the Schrödinger picture, the absorption into the measurement to the
Heisenberg picture.

<!-- page 5 -->
Generalized Probability Theories

5

With each pair of a 1-bit measurement k and a preparation procedure ` we can
set up an experiment which produces an outcome χk` ∈ {0, 1}. An important basic
assumption of the GPT framework is that experiments can be repeated under identical
conditions in such a way that the outcomes are statistically independent. Repeating the
experiment the specific outcome χk` is usually not reproducible, instead one can only
reproducibly estimate the probability
pk` = hχk` i

(1)

to obtain the result χk` = 1 in the limit of infinitely many experiments. For a given
toolbox the values of pk` can be listed in a probability table. This data table itself can
already be seen as a precursor of a physical model. However, it just reproduces the
observable statistics and apart from the known probabilities it has no predictive power
at all. Moreover, the table may grow as we add more preparation and measurement
devices. In order to arrive at a meaningful physical theory, we thus have to implement
two important steps, namely,
(i) to remove all possible redundancies in the probability table, and
(ii) to make reasonable assumptions which allow us to predict the behavior of elements
which are not yet part of our toolbox.
2.3. Operational equivalence, states and effects
In order to remove redundancies in the probability table let us first introduce the
notion of operational equivalence. Two preparation procedures are called operationally
equivalent if it is impossible to distinguish them experimentally, meaning that any of
the available measurement devices responds to both of them with the same probability.
Likewise two one-bit measurements are called operationally equivalent if they both
respond with the same probability to any of the available preparation procedures.
The notion of operational equivalence allows one to define equivalence classes
of preparations and one-bit measurements. Following the terminology introduced by
Ludwig and Kraus [4, 6] we will denote these classes as states and effects:
• A state ω is a class of operationally equivalent preparation procedures.
• An effect e is a class of operationally equivalent 1-bit measurements.

This allows us to rewrite the probability table in terms of states and effects, which in
practice means to eliminate identical rows and columns in the data table. Enumerating
effects by {e1 , e2 , . . . , eM } and states by {ω1 , ω2 , . . . , ωN } one is led to a reduced table
of size M × N , the so-called fundamental probability table.
If we denote by e(ω) = p(e|ω) the probability that an experiment chosen from
the equivalence classes e and ω produces a ’1’, the matrix elements elements of the

<!-- page 6 -->
Generalized Probability Theories

6

fundamental probability table can be written as
pij = hχij i = ei (ωj ) .

(2)

Obviously, this table contains all the experimentally available information. Since effects
and states are defined as equivalence classes, it is ensured that no column (and likewise
no row) of the table appears twice.
Note that the later inclusion of additional measurement apparatuses might allow
the experimentalist to distinguish preparation procedures which were operationally
equivalent before, splitting the equivalence class into smaller ones. This means that a
state may split into several states if a new measurement device is added to the toolbox.
The same applies to effects when additional preparation procedures are included.
As the introduction of equivalence classes described above eliminates only identical
rows and columns, the fundamental probability table can be still very large. In addition,
there may be still linear dependencies among rows and columns. As we will see below,
these linear dependencies can partly be eliminated, leading to an even more compact
representation, but they also play an important role as they define the particular type
of the theory.
2.4. Noisy experiments and probabilistic mixtures of states and effects
Realistic experiments are noisy. This means that a preparation procedure does not
always create the physical object in the same way, rather the preparation procedure
itself may randomly vary in a certain range. Similarly, a measurement is noisy in the
sense that the measurement procedure itself may vary upon repetition, even when the
input is identical. In the GPT framework this kind of classical randomness is taken into
account by introducing the notion of mixed states and effects.
The meaning of probabilistic mixtures is illustrated for the special case of bimodal
noise in Fig. 2. On the left side of the figure a classical random number generator selects
the preparation procedure ω1 with probability p and another preparation procedure ω2
with probability 1 − p. Similarly, on the right side another independent random number
generator selects the effect e1 with probability q and the effect e2 otherwise, modeling a
noisy measurement device.
If we apply such a noisy measurement to a randomly selected state, all what we get
in the end is again a ’click’ with certain probability P . In the example shown in Fig. 2,
this probability is given by
P = p q e1 (ω1 ) + p (1 − q) e2 (ω1 ) + (1 − p) q e1 (ω2 ) + (1 − p) (1 − q) e2 (ω2 ) ,

(3)

where we used the obvious assumption that the intrinsic probabilities pij = ei (ωj ) are
independent of p and q.

<!-- page 7 -->
7

Generalized Probability Theories

Figure 2. New states and effects can be generated by probabilistically mixing the
existing ones, illustrated here in a simple example (see text).

It is intuitively clear that a machine which randomly selects one of various
preparation procedures can be considered as a preparation procedure in itself, thus
defining a new state ω. Similarly, a device of randomly selected effects can be interpreted
in itself as a new effect e. Using these new effects and states the probability (3) to obtain
a ’click’ can simply be expressed as P = e(ω).
It is easy to see that probability (3) can be recovered by conveniently describing
the new states and effects by
ω := p ω1 + (1 − p) ω2 ,

e := q e1 + (1 − q) e2 ,

(4)

when we define them to act linearly on each other. We call these new objects mixed states
and mixed effects respectively. The mathematical operations in these terms represent
direct physical interpretations. Namely, scalar multiplication refers to being realized
only with some probability, whereas addition means the coarse-graining of mutually
excluding settings.
Note that we have introduced probabilistic mixing of devices as a consequence of
noise. Of course, this is not the only way to generate mixtures. For example, it could
be the experimenter himself who chooses randomly or intentionally between different
preparation and measurement devices. Thus, with any p, q in the continuous range [0, 1]
available to an experimenter, probabilistic mixing yields a continuous variety of states
and effects that can be realized.
2.5. Linear spaces, convex combinations, and extremal states and effects
The previous example shows that it is useful to represent probabilistically mixed states
and effects as linear combinations, using the usual rules for addition and multiplication
of probabilities. By doing so, we have represented states and effects as vectors in suitable
vector spaces, whose structure, dimension and the choice of the basis we will discuss
further below. For now, let us only note that each state ωi is represented by a vector in
a linear space V and that it is possible to define linear combinations in such a way that

<!-- page 8 -->
8

Generalized Probability Theories

vectors coincide if and only if they refer to the same state. Similarly each effect ei can
be represented by a vector in another linear space V ∗ , which is called the dual space of
V.
The embedding of states and effects in linear spaces allows us to consider arbitrary
linear combinations
X
X
e=
λi ei ,
ω=
µj ω j
(5)
i

j

with certain coefficients λi and µj . Moreover, the fundamental probability table
pij = ei (ωj ) induces a bilinear map V ∗ × V → R by
e(ω) =

M
hX
i=1

λi e i

N
iX
j=1

M X
N
 X
µj ωj =
λi µj ei (ωj ) ,
| {z }
i=1 j=1

(6)

=pij

generalizing Eq. (3) in the previous example. Note that this bilinear map on V ∗ × V
should not be confused with an inner scalar product on either V × V or V ∗ × V ∗ . In
particular, it does not induce the notion of length, norm, and angles.
At this point it is not yet clear which of the linear combinations in (5) represent
physically meaningful objects. However, as shown above, the set of physically
meaningful objects will at least include all probabilistic mixtures of the existing states
and effects, which are mathematically expressed as convex combinations with nonnegative coefficients adding up to 1.
States which can be written as convex combinations of other states are referred to
as mixed states. Conversely, states which cannot be expressed as convex combinations
of other states are called extremal states. As any convex set is fully characterized by
its extremal points, we can reduce the probability table even further by listing only the
extremal states, tacitly assuming that all convex combinations are included as well. The
same applies to effects.
2.6. Linear dependencies among extremal states and effects
What is the dimension of the spaces V and V ∗ and how can we choose a suitable basis?
To address these questions it is important to note that the extremal vectors of the
convex set of states (or effects) are not necessarily linearly independent. As we shall
see below, linear independence is in fact a rare exception that emerges only in classical
theories, while any non-classicality will be encoded in certain linear dependencies among
the extremal states and effects.
Let us illustrate the construction of a suitable basis in the example of a fictitious
model with probabilities listed in Table 1. As states and effects are defined as equivalence
classes, multiple rows and columns have already been eliminated. However, there are

<!-- page 9 -->
9

Generalized Probability Theories

ω1
ω2
ω3
ω4

e1
1
1
2
1
2

0

e2
0
0
1
2
1
2

e3
1
1
1
1

e4
1

e5
1

2
3
1
3

3
4
3
4
1
2

0

Table 1. Example of a probability table after removing identical columns and rows.

still linear dependencies among the rows and the columns. For example, the effect e5 is
related to the other ones by
e5 =

1
(e1 + e3 ) .
2

(7)

Since the expression on the r.h.s. is a convex combination it is automatically assumed to
be part of the toolbox so that we can remove the rightmost column from the probability
table, obtaining a reduced table in form of a 4 × 4 matrix. The remaining (non-convex)
linear dependencies are
e4 =

2
2
1
e1 − e2 + e3 ,
3
3
3

ω4 = −ω1 + ω2 − ω3 .

(8)

so that the rank of the matrix is 3. Since row and column rank of a matrix coincide,
the vector spaces V and V ∗ always have the same dimension
n := dim V = dim V ∗ = rank[{pij }].

(9)

In other words, the number of different states needed to identify an effect is always equal
to the number of different effects needed to identify a state.
As for any vector space representation, there is some freedom in choosing a suitable
basis. As for the effects, we may simply choose the first n linearly independent effects
e1 , . . . , en as a basis of V ∗ , assigning to them the canonical coordinate representation
e1 = (1, 0, 0),

e2 = (0, 1, 0),

e3 = (0, 0, 1) .

(10)

Likewise we could proceed with the states, choosing ω1 , ω2 , ω3 as a basis of V , but then
the matrix pij would be quite complicated whenever we compute e(ω) according to
Eq. (5). Therefore it is more convenient to use the so-called conjugate basis {ω̂1 , ω̂2 , ω̂3 }
which is chosen in such a way that the extremal states are just represented by the
corresponding lines in the probability table. In the example given above this means
that the states have the coordinate representation




1
1 1
ω1 = (1, 0, 1) , ω2 =
, 0, 1 , ω3 =
, ,1 .
(11)
2
2 2
The basis vectors {ω̂i } can be determined by solving the corresponding linear equations.

<!-- page 10 -->
10

Generalized Probability Theories

Figure 3. Unreliable effects. Left: A reliable effect e can be made unreliable by
randomly switching it on and off, constituting a new effect q e. Right: Reliable effects
are represented by points of the convex set in V ∗ (green dashed line). Including
unreliable effects this set is extended to a truncated convex cone (the hatched region)
spanned by the extremal effects.

In the present example, one can easily show that these basis vectors are given by the
(non-convex) linear combinations
ω̂1 = 2ω1 − 2ω2 ,

ω̂2 = −2ω2 + 2ω3 ,

ω̂3 = −ω1 + 2ω2 .

(12)

Using the conjugate basis the bilinear map e(ω) can be computed simply by adding the
products of the corresponding components like in an ordinary Euclidean scalar product.
Recall that the vector spaces V and V ∗ are probabilistic vector spaces which should
not be confused with the Hilbert space of a quantum system. For example, probabilistic
mixtures cannot be represented by Hilbert space vectors. We will return to this point
when discussing specific examples.
2.7. Reliability
Realistic experiments are not only noisy but also unreliable in the sense that they
sometimes fail to produce a result. For example, a preparation procedure may
occasionally fail to create a physical object. Similarly, a detector may sometimes fail to
detect an incident particle.
Preparation procedures which create a physical state with certainty are called
reliable. The same applies to measurement devices which respond to an incident particle
with certainty.
An unreliable effect may be thought of as a reliable one that is randomly switched
on and off with probability q and 1 − q, as sketched in Fig. 3. Applying this effect to
a state ω, the probability to obtain a ’click’ would be given by q e(ω). This example
demonstrates that unreliable effects can consistently be represented as sub-normalized
vectors q e ∈ V ∗ with 0 ≤ q < 1, extending the set of physical effects to a truncated
convex cone which is shown as a shaded region in in the right panel of Fig. 3. The
zero vectors of V and V ∗ represent the extreme cases of preparation procedures and a
measurement apparatuses which always fail to work.

<!-- page 11 -->
Generalized Probability Theories

11

2.8. Unit measure and normalization
If a given effect e responds to a specific state ω with the probability e(ω) = 1, then it
is of course clear that both the state and the effect are reliable. However, if e(ω) < 1,
there is no way to decide whether the reduced probability for a ’click’ is due to the
unreliability of the state, the unreliability of the effect, or caused by the corresponding
entry in the probability table.
To circumvent this problem, it is usually assumed that the toolbox contains a
special reliable effect which is able to validate whether a preparation was successful, i.e.
it ’clicks’ exactly in case of a successful preparation. This effect is called unit measure
and is denoted by u. The unit measure allows us to quantify the reliability of states: If
u(ω) = 1 the state ω is reliable, otherwise its rate of failure is given by 1 − u(ω).
The unit measure can be interpreted as a norm
||ω|| = u(ω)

(13)

defined on states in the convex cone of V . By definition, the normalized states with
u(ω) = 1 are just the reliable ones. The corresponding set (the green dashed line in
Fig. 3) is usually referred to as the state space Ω of the theory.
In the example of Table 1 it is easy to see that the effect e3 plays the role of the
unit measure. Since the unit measure cannot be represented as a convex combination
of other effects, it is by itself an extremal effect and thus may be used as a basis vector
of V ∗ . Here we use the convention to sort the Euclidean basis of V ∗ in such a way that
the unit measure appears in the last place, i.e. eM ≡ u. Using this convention the norm
of a state is just given by its last component. For example, in Table 1, where e3 = u,
the third component of all states ω1 , . . . , ω4 is equal to 1, hence all states listed in the
table are normalized and thus represent reliable preparation procedures.
The unit measure also induces a norm on effects defined by
||e|| = max e(ω) .
ω∈Ω

(14)

Since e(ω) ≤ 1 an effect is normalized (i.e. ||e|| = 1) if and only if there exists a state
ω for which ω(e) = 1. By definition, such an effect is always reliable. The opposite
is not necessarily true, i.e. reliable effects may be non-normalized with respect to the
definition in (14).
Note that a ‘unit state’, analogous to the unit effect u, is usually not introduced
since this would correspond to a preparation procedure to which every reliable effect
of the toolbox responds with a ’1’ with certainty, which is highly unphysical. If we
had introduced such a ‘unit state’, it would have allowed us to define a norm on effects
analogous to Eq. (13), preserving the symmetry between states and effects. Using
instead the norm (14) breaks the symmetry between the spaces V and V ∗ .

<!-- page 12 -->
Generalized Probability Theories

12

Figure 4. Consistency conditions. Left: Schematic illustration of the lower and the
upper bound, defining the intersection E max . Right: The same construction for the
probabilities listed in Table 1 in the three-dimensional representation (10). The red
(yellow) planes indicate the lower (upper) bound. The maximal set of effects E max is
the enclosed parallelepiped in the center.

As we will see in the following, the unit measure u plays a central role in the
context of consistency conditions and it is also needed to define measurements with
multiple outcomes. Moreover, the definition of subsystems in Sect. 5.4 relies on the
unit measure.
2.9. General consistency conditions
The concepts introduced so far represent only the factual experimental observations
and immediate probabilistic consequences. However, the purpose of a physical model is
not only to reproduce the existing data but rather to make new predictions, eventually
leading to a set of hypotheses that can be tested experimentally.
In order to give a GPT the capability of making new predictions one has to postulate
additional extremal states and effects which are not yet part of the existing toolbox.
Such an extension is of course not unique, rather there are various possibilities which can
be justified in different ways. For example, a particular extension might be reasonable
in view of the underlying structure and the expected symmetries of the physical laws.
Moreover, certain expectations regarding the relationship between the parameters of
the apparatuses and the corresponding states and effects as well as analogies to other
models could inspire one to postulate a specific structure of the state space and the
set of effects. This includes dynamical aspects of the systems, which are absorbed into
preparations and measurements in the present framework.
However, not every extension of states and effects gives a consistent theory. First
of all, the extension should be introduced in such a way that any combination of effects
and states yields a probability-valued result, i.e.,
0 ≤ e(ω) ≤ 1 ∀e ∈ E, ω ∈ Ω.

(15)

<!-- page 13 -->
Generalized Probability Theories

13

This restriction consists of a lower and an upper bound. The lower bond 0 ≤ e(ω),
the so-called non-negativity constraint, remains invariant if we rescale the effect e by a
positive number. In other words, for any effect e satisfying the non-negativity constraint,
the whole positive ray λ e with λ ≥ 0 will satisfy this constraint as well. The set of all
rays spanned by the non-negative effects is the so-called dual cone, denoted as
V+∗ := {e ∈ V ∗ | e(ω) ≥ 0 ∀ω ∈ Ω} .

(16)

The upper bound can be expressed conveniently with the help of the unit measure u.
Since the unit measure is the unique effect giving 1 on all normalized states, it is clear
that e(ω) ≤ 1 if and only if u(ω) − e(ω) = (u − e)(ω) ≥ 0, i.e., the complementary effect
u − e must be included in the dual cone given by (16). Note that this criterion is valid
not only for normalized states but also for sub-normalized states. This means that the
set of effects, which obey the upper bound e(ω) ≤ 1, is just u − V+∗ . Consequently, the
set which satisfies both bounds in (15), is just the intersection of V+∗ and u − V+∗ , as
illustrated in Fig. 4. This maximal set of effects is denoted by§

E max = V+∗ ∩ u − V+∗ .
(17)
Thus, if we extend the theory by including additional effects, the resulting set of effects
E has to be a subset of this maximal set, i.e.
E ⊆ E max .

(18)

A theory that includes the full set E max of effects is referred to as satisfying the norestriction hypothesis [9]. It can be shown that classical probability theory and quantum
theory both satisfy the no-restriction hypothesis, but in general there is no reason why
the preparations in our current toolbox should fully determine the range of possible
measurements. Note that for consistency the special effects ∅ and the unit measure u
have to be included. In addition, for any effect e ∈ E the complement ē = u − e needs
to be included as well.
Similarly we may extend the theory by including additional states. Here we have
to specify the set of states which satisfy (15) for a given set of effects E. Generally the
inclusion of additional states imposes additional restrictions on possible effects and vice
versa. Consequently, there is a trade-off between states and effects whenever a theory
is extended without changing the dimension of the vector spaces V and V ∗ .
A given GPT can also be generalized by increasing the dimension of V and V ∗ . In
fact, as will be shown in Sect. 4, every non-composite system from an arbitrary GPT
can equivalently be realized as a classical theory in a higher-dimensional state space
combined with suitable restrictions on the effects. However, as we will see in Sect. 5,
the treatment of multipartite systems leads to additional consistency conditions which
§ In the literature this set is also denoted by [∅, u] because of a partial ordering induced by V+∗ , as we
explain in more detail in appendix Appendix A.

<!-- page 14 -->
14

Generalized Probability Theories

cannot be fulfilled by restricted classical systems in higher dimensions, allowing us to
distinguish classical from genuine non-classical theories.
2.10. Jointly measurable effects
A set of effects is said to be jointly measurable if all of them can be evaluated in a
single measurement, meaning that there exists a measurement apparatus that contains
all these effects as marginals. By definition, effects belonging to the same measurement
apparatus are jointly measurable. However, a GPT may also include effects that cannot
be measured jointly. Therefore, it is of interest to formulate a general criterion for joint
measurability.
Before doing so, let us point out that joint measurability neither requires the effects
to be evaluated at the same time nor does it mean that they do not influence each other.
For example, let us consider a non-destructive measurement of effects {e1i } with results
{χ1j } followed by a second measurement. The results {χ2j } of the second measurement
correspond to effects e2j with the proviso that the first measurement has already been
carried out. If the first measurement was not carried out, we would obtain potentially
different effects. Nevertheless, the whole setup measures all effects {e1i } and {e2j } jointly,
irrespective of the fact that the second group depends on the first one.
Joint measurability of effects is in fact a weaker requirement than non-disturbance
and commutativity of measurements. In standard quantum theory these terms are often
erroneously assumed to be synonyms. This is because in the special case of projective
measurements they happen to coincide. However, as shown in [7, 8], they even differ in
ordinary quantum theory in the case of non-projective measurements.
Let us now formally define what joint measurability means. Consider two effects ei
and ej . Applied to a state ω each of them produces a classical one-bit result χi ∈ {0, 1}
and χj ∈ {0, 1}. Joint measurability means that there exists another single measurement
apparatus in the toolbox that allows us to extract two bits (χ̃i , χ̃j ) by Boolean functions
with the same measurement statistics as (χi , χj ).
In other words, two effects ei , ej are jointly measurable if the toolbox already
contains all effects which are necessary to set up the corresponding Boolean algebra, i.e.
there are mutually excluding effects ei∧j , ei∧j , ei∧j , ei∧j with the properties
ei

= ei∧j + ei∧j ,

ej = ei∧j + ei∧j

u

= ei∧j + ei∧j + ei∧j + ei∧j

(19)

ei∨j = ei + ej − ei∧j .
Let us use Eqs. (19) to rewrite ei∧j in three different ways:
ei∧j = ei − ei∧j

= ej − ei∧j

= ei + ej − u + ei∧j .

(20)

<!-- page 15 -->
Generalized Probability Theories

15

We can now translate the joint measurability condition to
∃e1 , e2 , e3 , e3 ∈ E : e1 = ei − e2 = ej − e3 = ei + ej − u + e4 .

(21)

This condition can be rewritten elegantly as an intersection of sets
E ∩ (ei − E) ∩ (ej − E) ∩ (ei + ej − u + E) 6= {}.

(22)

For joint measurability of the effects ei , ej this set has to be non-empty. If this is the
case, any choice of the AND effect ei∧j in the intersection (22) allows one to consistently
construct all other effects by means of Eqs. (19). This means that joint measurability
of two effects can be implemented in various ways with different ei∧j . Note that the
status of joint measurability of a given set of effects may even change when a theory is
extended by including additional effects.
2.11. Complete and incomplete Measurements
A measurement is defined as a set of jointly measurable effects. If these effects have
a non-trivial overlap ei∧j 6= 0 we can further refine the measurement by including the
corresponding AND effects. Thus, we can describe any measurement by a set of mutually
excluding effects {ek }, where only one of the outcomes χk occurs, as sketched in Fig. 1.
These refined effects have no further overlap, i.e. ek∧l = 0 for k 6= l. Moreover, these
effects can be coarse-grained by computing their sum ek∨l = ek + el .
A measurement is called complete if all mutually excluding effects sum up to
the unit measure u. Obviously an incomplete measurement can be completed by
P
including a failure effect em = u − m−1
i=1 ei that is complementary to all other effects.
As a consequence a complete measurement maps a normalized state to a normalized
probability distribution.
3. Examples
3.1. Classical probability theory
Classical systems have properties that take definite perfectly distinguishable values that
can be directly revealed via measurements. Probabilistic mixtures can be regarded as a
mere consequence of subjective ignorance.
In the GPT framework the different possible definite values of a classical system
are represented by the pure states ωi . They are linearly independent and can be used as
an Euclidean basis of the linear space V . The corresponding state space is a probability
simplex (see Fig. 5). Probabilistic mixtures are represented by convex combinations
of pure states. As the pure states form a basis, any mixed state can be uniquely
decomposed into pure states weighted by the probabilities of occurrence.

<!-- page 16 -->
16

Generalized Probability Theories

Figure 5. State and effect space of a classical bit in the GPT formalism with the
probability table ei (ωj ) = δij . In classical systems the extremal states and effects are
linearly independent and can be used as an orthonormal basis of the vector spaces.

The perfect distinguishability of pure states means that the extremal effects ej
simply read out whether a particular value has been realized or not, i.e. ej (ωi ) = δij .
Like the pure states in V these effects provide an Euclidean basis for V ∗ . Furthermore,
the zero effect ∅, and coarse-grained basis effects ej have to be included as additional
extremal effects. In particular, this includes the unit measure u which is obtained by
coarse-graining all basis effects ej . The unit measure responds with a ’1’ to any successful preparation of a classical system, independent of its values. In classical systems all
effects are jointly measurable.

3.2. Standard quantum theory: State space
Most textbooks on quantum theory introduce quantum states as vectors |Ψi of a complex
Hilbert space H. These vectors represent pure quantum states. The existence of a
Hilbert space representation is in fact a special feature of quantum mechanics. In
particular, it allows one to combine any set of pure states |Ψi i linearly by coherent
superpositions
X
X
|φi =
λi |ψi i ,
λi ∈ C ,
|λi |2 = 1 .
(23)
i

i

Note that the resulting state |φi is again a pure state, i.e. coherent superpositions are
fundamentally different from probabilistic mixtures. In fact, Hilbert space vectors alone
cannot account for probabilistic mixtures.
To describe mixed quantum states one has to resort to the density operator
formalism. To this end the pure states |Ψi are replaced by the corresponding projectors
ρΨ = |ΨihΨ|. Using this formulation one can express probabilistically mixed states as
convex combinations of such projectors, i.e.
X
X
ρ=
pi |Ψi ihΨi | ,
pi = 1 .
(24)
i

i

<!-- page 17 -->
Generalized Probability Theories

17

As the expectation value of any observable A is given by tr[ρA], it is clear that the
density matrix includes all the available information about the quantum state that can
be obtained by means of repeated measurements.
It is important to note that the density matrix itself does not uniquely determine
the pi and |ψii in (24), rather there are many different statistical ensembles which are
represented by the same density matrix. For example, a mixture of the pure qubit
states |0ih0| and |1ih1| with equal probability, and a mixture |+ih+| and |−ih−| of the
coherent superpositions |±i = √12 (|0i ± |1i) are represented by the same density matrix
ρ=

 1

1
|0ih0| + |1ih1| =
|+ih+| + |−ih−| ,
2
2

(25)

meaning that these two ensembles cannot be distinguished experimentally. Thus,
in ordinary quantum mechanics the density matrices ρ label equivalence classes of
indistinguishable ensembles and therefore correspond to the physical states ω in the
GPT language. The set of all quantum states (including probabilistic mixtures) can be
represented by Hermitean matrices with semi-definite positive eigenvalues. A state is
normalized if tr[ρ] = 1, reproducing the usual normalization condition hψ|ψi = 1 for
pure states.
Identifying the density operators as states, one faces the problem that these
operators live in a complex-valued Hilbert space whereas the GPT framework introduced
above involves only real-valued vector spaces. In order to embed quantum theory in the
GPT formalism, let us recall that a n × n density matrix can be parametrized in terms
of SU (n) generators with real coefficients. For example, the normalized density matrix
of a qubit can be expressed in terms of SU (2)-generators (Pauli matrices) as
ρ=

1
(1 + a σ x + b σ y + c σ z )
2

(26)

with real coefficients a, b, c ∈ [−1, 1] obeying the inequality a2 + b2 + c2 ≤ 1. Regarding
the coefficients (a, b, c) as vectors in R3 , the normalized states of a qubit form a ball in
three dimensions. The extremal pure states are located on the surface of this ball, the
so-called Bloch sphere.
In order to include non-normalized states (e.g. unreliable preparation procedures),
we have to append a forth coefficient d in front of the unit matrix, i.e.
ρ=

1
(d 1 + a σ x + b σ y + c σ z )
2

(27)

which is 1 for any normalized state and less than 1 if the preparation procedure is
unreliable. The four coefficients (a, b, c, d) provide a full representation of the state
space in R4 according to the GPT conventions introduced above. This state space is
illustrated for the simplest case of a qubit in the left panel of Fig. 6.

<!-- page 18 -->
Generalized Probability Theories

18

Figure 6. State and effect spaces of a quantum-mechanical qubit in the GPT
formalism. Since the vector space are four-dimensional the figure shows a threedimensional projection, omitting the third coefficient c.

3.3. Standard quantum theory: Effect space
As there are pure and mixed quantum states there are also two types of measurements.
Most physics textbooks on quantum theory are restricted to ‘pure’ measurements, known
as projective measurements. A projective measurement is represented by a Hermitean
operator A with the spectral decomposition
X
a |aiha|
(28)
A=
a

with real eigenvalues a and a set of orthonormal eigenvectors |ai. If such a measurement
is applied to a system in a pure state |ψi it collapses onto the state |ai with probability
pa = |ha|ψi|2 . Introducing projection operators Ea = |aiha| and representing the pure
state by the density matrix ρ = |ψihψ| this probability can also be expressed as
pa = |ha|ψi|2 = ha|ψihψ|ai = tr[Ea† ρ],

(29)

i.e. the absolute square of the inner product between bra-ket vectors is equivalent
to the Hilbert-Schmidt inner product of operators Ea and ρ. Hence we can identify
the projectors Ea = |aiha| with extremal effects in the GPT framework, where
ea (ω) = tr[Ea ρ]. As the projectors Ea cannot be written as probabilistic combinations
of other projectors, it is clear that they represent extremal effects. As all these effects
P
sum up to a Ea = 1, the unit measure u is represented by the identity matrix.

Turning to generalized measurements, we may now extend the toolbox by including
additional effects which are defined as probabilistic mixtures of projection operators of
the form
X
Ea =
qi |ai ihai | ,
0 ≤ qi ≤ 1.
(30)
i

As outlined above, such mixtures can be thought of as unreliable measurements.
A general measurement, a so-called positive operator valued measurement (POVM),
consists of a set of such effects that sum up to the identity.

<!-- page 19 -->
19

Generalized Probability Theories

Figure 7. State and effect spaces of a gbit.

Interestingly, the generalized effects in Eq. (30) are again positive operators.
i.e. mixed effects and mixed quantum states are represented by the same type of
mathematical object. Therefore, quantum theory has the remarkable property that the
spaces of states and effects are isomorphic. In the GPT literature this special property
is known as (strong) self-duality.
Note that for every given pure state ρ = |ΨihΨ| there is a corresponding
measurement operator E = |ΨihΨ| that produces the result tr[E ρ] = 1 with certainty
on this state. In so far the situation is similar as in classical systems. However, in
contrast to classical systems, it is also possible to obtain the same outcome on other
pure states with some probability. This means that in quantum mechanics pure states
are in general not perfectly distinguishable.
3.4. The gbit
A popular toy theory in the GPT community, which is neither classical nor quantum,
is the generalized bit, the so-called gbit. This theory has a square-shaped state space
defined by the convex hull of the following extremal states ωi :
ω1 = (1, 0, 1),

ω2 = (0, 1, 1),

ω3 = (−1, 0, 1),

ω4 = (0, −1, 1) .

(31)

The corresponding set of effects usually includes all linear functionals that give
probability-valued results when applied to states. This means that the effect space
is given by the convex hull of the following extremal vectors:
1
1
e2 = (−1, 1, 1),
e1 = (1, 1, 1)
2
2
1
1
e3 = (−1, −1, 1), e4 = (1, −1, 1)
(32)
2
2
together with the zero effect and the unit measure
∅ = (0, 0, 0),

u = (0, 0, 1).

(33)

Remarkably, in contrast to the classical and the quantum case, each extremal effect ei
gives certain outcomes on more than one extremal state.

<!-- page 20 -->
Generalized Probability Theories

20

3.5. Other toy theories
A whole class of toy theories with two-dimensional state spaces given by regular polygons
was introduced in [10]. Remarkably, these include some of the above standard cases,
which correspond to state spaces with a particular number n of vertices. The state space
of a classical theory with three distinguishable pure states is given by a triangle-shaped
state space, that is the regular polygon with three vertices (n = 3). The square shaped
state space of the gbit corresponds to n = 4. In the limit n → ∞, however, we get a twodimensional subspace of a qubit, inheriting some of the quantum features. The polygon
theories can therefore be used to compare the different standard cases. Furthermore,
increasing the number of vertices yields a transition from a classical theory and a gbit to
a quantum-like theory in the limit of infinitely many vertices. A continuous transition
between a classical system and a gbit was studied by a different class of toy theories [11].
It consists of a two-dimensional state space with four vertices. The location of one of
the vertices is parametrized, such that the square and the triangle appear as special
cases for particular parameters.
Further examples of state spaces discussed in the literature include a complicated
three-dimensional cushion-like state space to model three-slit interference [12], a
cylinder-shaped state space [13], a house-shaped state space [10], hypersheres of
arbitrary dimensions used as a generalization of the Bloch sphere of qubits [14], a
three-dimensional state space with triangle-shaped and disc-shaped subspaces [15] and
a three-dimensional approximation of the Bloch ball with finite extremal states [16].
All the theories introduced so far, include the full set of potential effects. That
is, they obey the no-restriction hypothesis. Toy theories with restricted effect sets are
discussed in [9]. Particular interesting examples in this work are theories with inherent
noise and a construction that mimics the state-effect duality of quantum theory by
restricting the effect set of general theories. Another popular example of a restricted
GPT is the probabilistic version of Spekken’s toy theory [17], given by octrahedronshaped state space and effect set [9, 18].
3.6. Special features of quantum theory
Having introduced some examples of GPTs let us now return to the question what
distinguishes quantum mechanics as the fundamental theory realized in Nature from
other possible GPTs. Although a fully conclusive answer is not yet known, one can
at least identify various features that characterize quantum mechanics as a particularly
elegant theory.
3.6.1. Continuous state and effect spaces: Comparing the state and effect spaces in
Figs. 6 and 7 visually, one immediately recognizes that quantum theory is special in so
far as extremal states and effects form continuous manifolds instead of isolated points.

<!-- page 21 -->
Generalized Probability Theories

21

In the Hilbert space formulation this allows one to construct coherent superpositions
and to perform reversible unitary transformations, giving the theory a high degree
of symmetry. Note that coherent superpositions and probabilistic mixtures are very
different in character: While mixtures exist in all GPTs, coherent superpositions turn
out to be a special property of quantum theory. GPTs do in general not admit reversible
transformations between different extremal states which would be a prerequisite for the
possibility of superpositions [17, 18].
Quantum theory does not only allow one to relate pure states by reversible
unitary transformations (transitivity) [19–21], but even mixed states can be reversibly
transformed into each other (homogeneity) [22]. Moreover, the continuous manifold of
infinitely extremal quantum states does not require infinite-dimensional vector spaces.
For example, the state space of a qubit (Bloch ball) is three-dimensional although it has
infinitely many extremal points.
3.6.2. Distinguishability and sharpness: The possibility of reversible transformations
between extremal states has direct consequences in terms of the information processing
capabilities of a theory [23]. As we have seen, in non-classical theories pairs of states are
in general not perfectly distinguishable. Remarkably, quantum theory is also special in
so far as it allows for a weaker notion of perfect distinguishability [24], namely, for any
extremal state one can find a certain number of other perfectly distinguishable extremal
states (the orthogonal ones in the Hilbert space formulation). This number is called the
information capacity of the system which corresponds to the classical information that
can be encoded in such a subsystem of distinguishable states. In quantum theory it is
equal to the dimension of the Hilbert space.
Obviously, any GPT with given state and effect spaces has well-defined subsets
of perfectly distinguishable states and therewith a well-defined information capacity.
Remarkably, for quantum theory the opposite is also true, i.e., the information capacity
of a system can be shown to determine its state space [19,20]. As a consequence it turns
out that a system of given information capacity includes non-classical ones with a lower
information capacity as subspaces [21], which allows for an ideal compression of the
encoded information [24]. This embedding is reflected by a rich geometrical structure
of state spaces that is still to a large extent unexplored. The interested reader may
be referred to [25] for an detailed discussion of the geometry of quantum state spaces.
An example of a state space that is still comparably low dimensional, but nevertheless
has a highly non-trivial structure, is the qutrit, a quantum system with information
capacity three. Itphas extremal points that lie on the surface of an eight-dimensional
ball with radius 2/3. However, the sphere is only partially covered with extremal
states. In particular, for any pure state of a qutrit there is a subspace with information
capacity 2 including all states that can be perfectly distinguished from the first one. As
quantum systems with information capacity 2 are represented by the three-dimensional
Bloch ball, we can conclude that there is an opposing Bloch-ball-shaped facet for any

<!-- page 22 -->
Generalized Probability Theories

22

extremal point of the qutrit state space.
Quantum theory is also special in so far as for any extremal state ω there exists a
unique extremal effect e which gives e(ω) = 1 while it renders a strictly lower probability
for all other extremal states. Therefore, this effect allows one to unambiguously identify
the state ω. The existence of such identifying effects is another special quantum feature
known as sharpness [26].
3.6.3. Strong self-duality: Another striking feature of quantum theory is the circumstance that extremal states and the corresponding identifying effects are represented by
the same density operator. This is related to the fact that quantum theory is (strongly)
self-dual, i.e. the cone of non-normalized states and its dual cone coincide [27] and
obey the no-restriction hypothesis [9]. It was shown that this is a consequence of bit
symmetry, i.e. all pairs of distinguishable states can be reversibly transformed into each
other [28].
To summarize, from the perspective of GPTs quantum theory has remarkable
characteristic properties which may give us an idea why this theory is the one realized
in Nature. On the other hand, various other features that seem special for quantum
theory turned out to be common for non-classical theories within the GPT framework.
Examples are the operational equivalence of different ensembles and the impossibility
to clone a state [29].
Note, that so far we have only discussed single (i.e. non-composite) systems.
Already on this level quantum theory exhibits very special features that are hard to
find in any other toy theories. Nevertheless, as we will show in the next section, any
non-classical single theory can be simulated by a higher dimensional classical system
with appropriate restrictions.
4. Non-classicality by restriction
Any non-classical single (non-partitioned) system can be interpreted as a classical system
with appropriately restricted effects in higher dimensions. This can easily be illustrated
in the example of Table 1. Suppose we extend the table by one additional column for
each preparation procedure ωi which contains a ’1’ for ωi and ’0’ otherwise (see Table 2).
Obviously, these additional columns can be interpreted as additional effects that allow
us to perfectly distinguish different preparation procedures, just in the same way as in a
classical model. In other words, by adding these columns we have extended the model to
a classical one in a higher-dimensional space, where each of the preparation procedures
is represented by a different pure state. The original effects can simply be interpreted
as coarse-grained mixtures of the additional effects.

<!-- page 23 -->
23

Generalized Probability Theories
e1
1

ω1
ω2
ω3
ω4

1
2
1
2

e2
0
0
1
2
1
2

0

e3
1
1
1
1

e4
1

e5
1

2
3
1
3

3
4
3
4
1
2

0

e6
1
0
0
0

e7
0
1
0
0

e8
0
0
1
0

e9
0
0
0
1

Table 2. Copy of Table 1 extended by four additional effects e6 , e7 , e8 , e9 , converting
the non-classical theory into a classical one in higher dimensional space.

Conversely, it is also possible to restrict a classical system in such a way that it seems
to acquire non-classical features. Such an example was given by Holevo in 1982 [30]:
Take a classical system with four pure states
ω1 = (1, 0, 0, 0),

ω2 = (0, 1, 0, 0),

ω3 = (0, 0, 1, 0),

ω4 = (0, 0, 0, 1)

(34)

representing four distinguishable values. These extremal states span a three-dimensional
tetrahedron of normalized mixed states embedded in four-dimensional space. The
corresponding extremal effects are given by the vertices of the four-dimensional
hypercube e = (x1 , x2 , x3 , x4 ) with xi ∈ {0, 1}, including the zero effect ∅ = (0, 0, 0, 0)
and the unit measure u = (1, 1, 1, 1). By definition, two states ω = (y1 , y2 , y3 , y4 ) and
ω 0 = (y10 , y20 , y30 , y40 ) are operationally equivalent whenever
0

e(ω) = e(ω )

⇔

4
X

xi yi =

i=1

4
X

xi yi0

(35)

i=1

for all available effects e, which in this case means that all components yi = yi0 coincide.
Now, let us restrict our toolbox of effects to a subset where
x1 + x2 = x3 + x4 .

(36)

As a result, ω and ω 0 can be operationally equivalent even if the components yi and yi0
are different. More specifically, if there is a t 6= 0 such that
y10 = y1 + t,

y20 = y2 + t,

y30 = y3 − t,

y40 = y4 − t ,

(37)

then the restricted toolbox of effects does not allow us to distinguish the two states,
hence ω and ω 0 now represent the same state in the restricted model.
The extended operational equivalence allows us to choose one of the components,
e.g. to set y4 = 0. This means that the four-dimensional parameter space is projected
onto a three-dimensional subspace, and the embedded three-dimensional tetrahedron is
again projected to a two-dimensional convex object. This projected state space turns out
to have the form of a square, as shown schematically in Fig. 8. As we have seen before,
this is just the state space of a (non-classical) gbit. Therefore, the restriction (36) leads

<!-- page 24 -->
Generalized Probability Theories

24

Figure 8. Construction of the two-dimensional gbit state space by projecting a threedimensional classical state space (adapted from [30]).

effectively to a non-classical behavior. In fact, Holevo showed that such a construction
is possible for any probabilistic theory including quantum theoryk.
To summarize, any non-classical GPT can be extended to a higher-dimensional
classical theory by including additional effects. Conversely, non-classical theories can
be deduced from a classical one by imposing appropriate restrictions on the available
effects. The restrictions allow us to project the classical state space to a non-classical
one in lower dimensions, inheriting phenomena like uncertainty relations and non-unique
decompositions of mixed states.
Obviously this seems to question the fundamental necessity of non-classical systems.
How do we know that all the unusual phenomena in quantum theory do not only result
from restrictions in some higher-dimensional space and thus can be explained in classical
terms once we extend our theory? However, at this point we should keep in mind that so
far we considered only single (non-composite) systems. As we will see in the following
section, multipartite non-classical systems cannot be described in terms of restricted
classical systems. Thus, it would be misleading to conclude that non-classicality only
results from restrictions imposed on an underlying higher-dimensional classical system.
In fact, the analysis of multipartite systems will allow us to clearly distinguish classical
and genuinely non-classical physical systems.
5. Multipartite systems
Multipartite systems may be thought of as consisting of several subsystems in which the
same type of theory applies. Since such a composed system in itself can be viewed as
a single system simply by ignoring its subsystems structure, the consistency conditions
discussed in the previous sections obviously apply to multipartite systems as well.
However, it turns out that additional consistency conditions arise from the fact that
k Note that quantum theory has infinitely many extremal states. The construction therefore requires
an infinitely dimensional classical system.

<!-- page 25 -->
25

Generalized Probability Theories

the theory has to be compatible with the partition into given subsystems. In fact, as
we will see below, the structure of the subsystems determines a smallest and largest set
of joint states and effects that are compatible with the given partition. The actual set
of joint elements can be chosen freely within these constraints. This means that a GPT
is not yet fully specified by defining states, effects, and the probability table of a single
system, instead it is also required to specify how individual systems can be combined
to more complex composite systems.
We will see that, mathematically, the rules for the combination of subsystems are
incorporated by defining suitable tensor products for the sets of states and effects. These
tensor products should not be confused with the (uniquely defined) Cartesian tensor
product of the linear spaces V and V ∗ , it rather defines the range of physical objects
which are embedded in these spaces.
5.1. Separability and the minimal tensor product
In the simplest case, the composite system consists of several independently prepared
components. As these subsystems are statistically independent, the joint state
describing the overall situation is given by a product state.
As an example let us consider two subsystems A and B which are in the states ω A
and ω B , respectively. If these systems are completely independent, their joint state is
given by a product state, denoted as ω AB = ω A ⊗ ω B . Similarly, the effects of the two
subsystems can be combined in product effects eAB = eA ⊗ eB , describing statistically
independent measurements on both sides. In this situation the joint measurement
probabilities factorize, i.e.
eAB (ω AB ) = p(eA ⊗ eB |ω A ⊗ ω B ) = p(eA |ω A ) p(eB |ω B ) = eA (ω A ) eB (ω B ). (38)
As a next step, we include classical correlations by randomly choosing preparation
procedures and measurement apparatuses in a correlated manner. Formally this
can be done by probabilistically mixing the product elements defined above. For
example, classically correlated states may be incorporated by including probabilistic
P
linear combinations of the form ω AB = ij λij ωiA ⊗ωjB with positive coefficients λij > 0.
Similarly, one can introduce classically correlated effects.
In the GPT framework the mathematical operation, which yields the set of product
elements and their probabilistic mixtures, is the so-called the minimal tensor product:
V+A ⊗min V+B

:= {ω AB =

V+A∗ ⊗min V+B∗ := {eAB =

X
ij

X
ij

λij ωiA ⊗ ωjB | ω A ∈ V+A , ω B ∈ V+B , λij ≥ 0}

(39)

B
A
A∗ B
B∗
µij eA
i ⊗ ej | e ∈ V+ , e ∈ V+ , µij ≥ 0} .

(40)

Elements in the minimal tensor product are called separable with respect to the partition.

<!-- page 26 -->
26

Generalized Probability Theories

The extremal states in the joint state space V+A ⊗min V+B are given by the product
of extremal subsystem states. Note that the joint states in this space are not necessarily
normalized. Normalized separable joint states can be obtained by forming products of
normalized single states or mixtures of them. As a criterion for normalization, the joint
unit measure uAB = uA ⊗ uB is the unique joint effect that gives uAB (ω AB ) = 1 on all
normalized joint states.
If we apply a joint effect to a joint state, the corresponding measurement statistics
is determined by the weighted sum of factorizing probabilities:
"
#
!
X
X
B
eAB (ω AB ) = p(eAB |ω AB ) =
µij eA
λkl ωkA ⊗ ωlB
i ⊗ ej
i,j

=

X

kl

A
B
B
λij µkl eA
i (ωk ) ej (ωl ).

(41)

ijkl

As the number of combinations and the number of coefficients λij , µkl coincide, it is
clear that the measurement statistics obtained from such product effects is sufficient
to identify a joint state uniquely. This means that the whole information of classically
correlated elements in the minimal tensor product can be extracted by coordinated local
operations carried out in each of the subsystems.
5.2. Entanglement in GPTs
The minimal tensor product defines the sets V+A ⊗min V+B and V+A∗ ⊗min V+B∗ of classically
correlated states and effects which can be seen as subsets of certain vector spaces. For
classical systems one can show that the minimal tensor product already includes all joint
elements that are consistent with the division into classical subsystems [31]. However, in
non-classical theories there are generally additional vectors representing elements which
are non-separable but nevertheless consistent with the subsystem structure and fully
identifiable by local operations and classical communication (LOCC). Such states are
called entangled. As it is well known, entangled states do exist in standard quantum
theory.
In the GPT framework both separable and entangled elements can be represented
as vectors in the direct product spaces V AB = V A ⊗ V B and V AB∗ = V A∗ ⊗ V B∗ .
For separable, classically correlated elements this was directly inherited from classical
probability theory. The tensor structure for entangled elements is based on the
following additional assumptions [23]: i)local tomography, which means that coordinated
local operations suffice to identify a joint element, ii) no-signaling, stating that local
operations in one part of the system have no effect on the local measurement statistics
in other parts. As elements of the direct product spaces, we can represent joint elements
as n × m matrices, where n = dim V A = dim V A∗ and m = dim V B = dim V B∗ are the
dimensions of the subsystems.
Separable and entangled elements decompose into product elements in a different

<!-- page 27 -->
Generalized Probability Theories

27

Figure 9. Impossibility to explain entanglement in classical terms. Two nonclassical subsystems A,B containing n and m extremal states are joined to a single
non-classical system by means of a nontrivial tensor product ⊗GPT > ⊗min . The
resulting non-classical systems AB contains n · m extremal product states plus k
additional non-separable extremal states. However, mapping the systems A,B first
to the corresponding higher dimensional classical systems (right side) and combining
them by the usual classical tensor product, the resulting m · n-dimensional classical
system would not be able to account for the additional k entangled states.

way. By definition, entangled elements are are not included in the minimal tensor
product, meaning that they cannot be written as probabilistic mixtures of product
elements. Of course they can still be decomposed into a linear combination of product
elements, but such a linear decomposition would inevitably include negative coefficients.
As an example from quantum mechanics let us consider a fully entangled two-qubit
Bell state
1
|ψ + i = √ (|00i + |11i) .
2

(42)

Choosing for each qubit the normalized extremal Bloch states
1 1 + σx 1 + σy 1 + σz
,
,
},
{ω1 , ω2 , ω3 , ω4 } = { ,
2
2
2
2

(43)

where σ x,y,z are Pauli matrices, a straight-forward calculation shows that the pure Bell
state ω = |ψ + ihψ + | can be decomposed into a linear combination
ω = 2ω11 − ω12 + ω13 − ω14 − ω21 + ω22 + ω31 − ω33 − ω41 + ω44

(44)

of the product states ωij = ωi ⊗ ωj , which obviously contains negative coefficients.
5.3. Entanglement as a genuinely non-classical phenomenon
The previous example of the Bell state illustrates that the phenomenon of entanglement
gives rise to additional extremal joint elements in the tensor product which are not part
of the minimal tensor product. As we will see in the following, the existence of such
non-separable elements makes it impossible to consistently ‘simulate’ a non-classical
system by a classical theory in a higher-dimensional state space.

<!-- page 28 -->
28

Generalized Probability Theories

To see this we first note that the product of extremal elements in the subsystems
gives again extremal elements in the composite system. For example, if two non-classical
systems A and B have n and m pure states, then the joint system AB possesses at least
nm pure product states (see Fig. 9). In addition, the joint system also possesses a
certain number k of non-separable extremal states, provided that the tensor product is
‘larger’ than the minimal one.
The existence of non-separable elements is incompatible with the idea of an
underlying classical system in a higher-dimensional space with appropriate restriction,
as described in Sect. 4. The reason is that the combination of two classical systems
cannot account for additional non-separable elements.¶. In other words, if we first
map the subsystems to the corresponding n- and m-dimensional classical systems and
combine them by means of the classical (i.e. minimal) tensor product, the resulting
classical would live in a nm-dimensional space. However, in order to account for the
entangled elements, nm + k dimensions would be needed, as illustrated in the figure. In
other words, such a construction shows an inconsistent scaling behavior.
The measurement probability p(eAB |ω AB ) of an arbitrary joint effect eAB applied
to an arbitrary joint state ω AB is still given by (41), but in the case of non-separable
elements some of the coefficients λij and µkl will be negative. Since this could lead
to negative probabilities p(eAB |ω AB ) < 0, further restrictions on the joint elements are
needed to ensure positivity.
Typically, if we include more and more entangled states, the allowed range of
entangled effects becomes smaller, and vice versa. Thus, as in the case of single systems
there is a trade-off between entangled states and effects [32]. In particular, if we restrict
the range of effects to the minimal tensor product, we can include a certain maximal
set of consistent joint states and vice versa. In the following we want to characterize
this maximal set of joint states.
5.4. Marginal states and conditional states
Before defining the maximal set of joint states, we have to introduce the notion
of marginal states. To this end let us first consider the measurement statistics of
independent local measurements applied to a joint state ω AB , which is given by the joint
B AB
B
AB
probability distribution p(eA
) = [eA
). Since the local measurements
i , ej |ω
i ⊗ ej ](ω
A
are independent, we do not have to apply the effects ei und eB
j at once. In particular,
A
we could observe only the outcome of e in part A, ignoring the measurement in part
B. The probability of this outcome is given by the marginal probability
"
#
X
X
X
AB
B
AB
B
AB
) = eA
eB
(ω AB )
p(eA
) =
p(eA
)=
[eA
i ⊗ ej ](ω
i ⊗
j
i |ω
i , ej | ω
j

=

B
AB
[eA
)
i ⊗ u ](ω

j

=

j

A
eA
i (ωuB ) .

¶ This is because there are no physical states outside the classical probability simplex.

(45)

<!-- page 29 -->
29

Generalized Probability Theories

In the last step of Eq. (45) we introduced the so-called marginal state ωuAB (analogous
to the reduced density matrix from the partial trace in quantum mechanics). This state
is the effective subsystem state which predicts the local measurement statistics in part
A. Similarly, the marginal state ωuBA determines the measurement statistics in part B.
It is important to note that entangled pure states can have mixed marginal states.
For example, in standard quantum mechanics the pure state ρAB = |ψ + ihψ + | in Eq. (42
has a completely mixed marginal state ρA = 12 (|0ih0| + |1ih1|). Such a situation, where
we have perfect knowledge about the entire system but an imperfect knowledge about
its parts, is obviously impossible in classical systems. In addition, the observation leads
us to the important insight that the concept of probability in GPTs is not just a matter
of incomplete subjective knowledge but rather an important part of the physical laws.
The marginal state ωuAB reflects our knowledge about subsystem A provided that
potential measurements on subsystem B are ignored. However, our knowledge is of
course different if a particular measurement on B is carried out and the result is to us via
classical communication. This increased knowledge is accounted for by the conditional
probabilities
!
A
B
AB
A B
AB


ωeAB
[e
⊗
e
](ω
)
p(e
,
e
|
ω
)
i
j
i
j
j
A
A
A
B
AB
=
=
e
=
e
ω̃
.(46)
p(eA
|e
,
ω
)
=
i
i
i
j
eB
B
B
AB )
j
p(eB
eB
eB
j |ω
j (ωuA )
j (ωuA )
In the last steps we introduced the so-called conditional state ωeAB and its normalized
j

version ω̃eAB . The conditional state ω̃eAB is the effective state in A given that the effect eB
j
j

j

was observed in B. The marginal state introduced in Eq. (45) is a special conditional
state, where the effect eB
j is just the unit measure in B.
As ωeAB depends on the effect eB
j , it can be interpreted as a linear map from effects
j
in one part onto conditional states in the other.
5.5. The maximal tensor product
As outlined above, consistency conditions lead to a trade-off between the sizes of state
and effect spaces. Therefore, in order to derive the maximal set of possible joint states,
let us assume that the corresponding set of effects is given by the minimal tensor product.
Consequently, the joint states have to satisfy two consistency conditions:
(i) Applied to product effects they have to give non-negative results.
(ii) They induce valid conditional states, that is, all conditional states have to be
elements of the corresponding subsystem state space.
Note that the second condition always implies the first one, since all factors in (46)
are non-negative for any valid conditional state. Conversely, in non-restricted systems

<!-- page 30 -->
30

Generalized Probability Theories

⊗max

QT

⊗min

Figure 10. The tensor product of standard quantum theory (QT) lies strictly between
the minimal and the maximal tensor product. All tensor products share the extremal
states of the minimal tensor product. Quantum theory and the maximal tensor product
append additional extremal states.

the first condition implies the second one. Therefore, it suffices to consider the nonnegativity condition alone. With this assumption, the maximal set of non-normalized
joint states V+A ⊗max V+B for unrestricted systems is just given by the dual cone with
respect to product effects:
V+A ⊗max V+B := (E+A ⊗min E+B )∗
(47)
 AB
A
B A
B
AB
A
A B
B
= ω ∈ V ⊗ V e ⊗ e (ω ) ≥ 0 ∀e ∈ E , e ∈ E
.

In other words, the maximal tensor product V+A ⊗max V+B is simply the set of all joint
states which give nonnegative results if we apply effects from the minimal tensor product.
5.6. Maximal tensor product for systems with restricted effects
For subsystems with restricted effect spaces E A , E B the situation is more complicated.
In this case the spaces V A , V B contain joint elements that give probability-valued results,
but yield invalid elements as conditional states. Consequently, the construction in (47)
is no longer suitable.
To circumvent this problem a generalized maximal tensor product denoted by ⊗max
was proposed in [9]. The idea is to construct a maximal extension in only one direction,
say from subsystem A to subsystem B, then to repeat this construction and opposite
direction, and finally to define the generalized tensor product as the intersection of both
results.
Let us first consider the A → B direction. Recall that the maximal tensor product
should give all linear maps ωeBA from effects in A to valid non-normalized states in the
cone V+B . Consequently, we get can maximally extend the states in A and take the full
dual cone V+B∗ for effects in B without affecting the valid linear maps in this direction.
In this way, we obtain an intermediate unrestricted theory to which we can apply the
previous construction in Eq. (47). The same can be done in opposite direction by
exchanging A ↔ B. The generalized maximal tensor product V+A ⊗max V+B is given by
the set of linear maps that are valid in both directions, i.e. it is given by the intersection
∗
∗
(48)
V+A ⊗max V+B := E+A ⊗min V+B∗ ∩ V+A∗ ⊗min E+B .

The construction is illustrated in figure 11. Note that (48) reduces to (47) in the nonrestricted case, as E+A = V+A∗ and E+B = V+B∗ . Moreover, it was recently shown that it

<!-- page 31 -->
31

Generalized Probability Theories

eA
ω AB

A⊗
B∗
E+
min V+

∗

ω AB
eB

ωeBA

∈ V+B

⇔

⇔

V+A ⊗maxV+B

B
V+A∗ ⊗min E+

∗

ωeAB

∈ V+A

Figure 11. Illustration of the generalized maximal tensor product (originally
published in [9])

reduces to the traditional maximal tensor product of extended effects as soon as one of
the subsystems is non-restricted [33].
Recall that the minimal and maximal tensor products define only the boundary
cases for joint systems and that there is a broad range of theories in between. Standard
quantum mechanics is special in so far as it allows the same degree of entanglement
for both states and effects, i.e. states and effects play a symmetric role in this theory.
That is the tensor product of quantum theory lies strcitly between the minimal and
the maximal tensor product. Theories at the upper boundary defined by the maximal
tensor product admit a higher degree of entanglement, but only either for states or for
effects, while elements of the other type have to be separable.
A popular toy theory that uses the maximal tensor product is called boxworld [34].
It is defined in terms of gbits or higher-dimensional variants combined with the maximal
tensor product.
6. Realism versus locality: The meaning of non-local correlations
As shown above entanglement is a strictly non-classical feature of GPTs. However, a
detailed knowledge of the subsystems is required in order to identify a joint element
as an entangled one. Therefore, it would be desirable to formulate alternative deviceindependent criteria for entanglement which do not rely on the particular type of theory
in the subsystems.
The most important approach in this direction is the analysis of nonlocal
correlations. Already in the early days of quantum mechanics, it was pointed out
in the context of the famous EPR gedankenexperiment [35] that the existence such
non-classical correlations are in conflict with at least one of the following assumptions:
Realism: A theory obeys realism if measurement outcomes can be interpreted as
revealing a property of the system that exists independent of the measurement.

<!-- page 32 -->
Generalized Probability Theories

32

Locality: A physical theory obeys locality if the measurement on one part of a joint
system does not influence measurements on other (spatially separated) parts.
Classical systems satisfy local realism. However, Bell already showed in 1964
that quantum theory can generate correlations that violate at least one of these
assumptions [36]. Interestingly, stronger entanglement does not always lead to stronger
violations of a Bell inequality. In fact, it has been shown that in some setups even an
inverse relationship is possible [37].
A particularly simple and popular setup that detects non-local correlations was
suggested by Clauser, Horne, Shimony and Holt (CHSH) in 1969 [38]. The CHSH setup,
which was originally designed for quantum-mechanical systems, fits naturally into the
GPT framework. It consists of two (spatially separated) parties A and B that share
a bipartite state ω AB . Each of the parties chooses between two binary measurements
B
B
B
A
MxA = {eA
x,0 , ex,1 } and My = {ey,0 , ey,1 } indexed by x, y ∈ {0, 1}. For each choice of x, y
we get a probability distribution
B
AB
p(a, b | x, y) = [eA
),
x,a ⊗ ey,b ](ω

(49)

where a, b ∈ {0, 1}. The probability distribution generated by a local realistic theory
can be shown to satisfy the CHSH inequality
S LH = |C0,0 + C0,1 + C1,0 − C1,1 | ≤ 2

(50)

with the correlators
Cx,y =

X

(−1)a⊕b p(a, b | x, y),

(51)

a,b∈{0,1}

where ⊕ denotes a logical XOR.
In a classical probability theory we have C0,0 = C0,1 = C1,0 = 1, implying that
the fourth correlator is given by C1,1 = 1 so that the inequality holds. Quantum
theory, however, can violate this inequality as confirmed experimentally in [39]. The
theoretical maximum of the CHSH value that can be reached in quantum theory is given
√
QT
by Tsirelson’s bound Smax
= 2 2 [40].
Non-classical GPTs can also violate the CHSH inequality. In fact, these violations
can even exceed Tsirelson’s bound for quantum-mechanical systems. A frequently
studied example is the maximal tensor product of gbits which exhibits so-called PR-box
correlations [41], violating the CHSH inequality up to its algebraic maximum S P R = 4.
Returning to the question of what distinguishes quantum mechanics as the
fundamental theory of nature, it is therefore not sufficient to explain the existence of nonclassical correlations, one also has to give reasonable arguments why these correlations
are not stronger.

<!-- page 33 -->
Generalized Probability Theories

33

7. Discussion: Special multipartite features in quantum theory
As we have seen the phenomena of nonlocality and entanglement are a hallmark of
quantum theory but they also exist in many other toy theories. However, in the context
of multipartite systems quantum mechanics exhibits various characteristic features
which generically do not exist in other GPTs. In this section we are going to review
some of these characteristic multipartite quantum features.
7.1. Quantum features inherited from subsystems:
Surprisingly, many of these characteristic features are not linked to the structure of
the tensor product, rather they are consistently inherited from single systems. In
particular the one-to-one correspondence between state spaces and their information
capacity carries over to joint systems. For example, the information capacity of a joint
system is simply the product of the single systems information capacities [19].
Since the state spaces are uniquely determined by the information capacity, a joint
system consisting of two qubits has the same state space than a single quantum system
with information capacity of four. In the case of quantum mechanics the difference
between single and joint systems is not reflected in different state space structures but
only in a different interpretation of the measurements and states. As composite quantum
systems have the same state space structure as their building blocks, multipartite
quantum systems inherit all the features from single systems, including e.g. reversible
continuous transformations between pure states (transitivity), strong self-duality, nonrestricted measurements/states, sharpness and homogeneity. This allows us to interpret
the qubit as a fundamental information unit from which any quantum system can be
built [42].
In quantum mechanics the equivalence of systems with equal information capacity
also manifests itself in the associativity of the tensor product. This means that equal
components of a multipartite system can be swapped without changing the state space
(compound permutability) [26]. As illustrated in Fig. 10, this tensor product lies strictly
between the minimal and maximal tensor product, such that potential entanglement in
states and effects is perfectly balanced.
The inheritance of such features to joint system in standard quantum theory is
quite exceptional, as can be seen when trying to construct something similar for other
GPTs. For example, the extremal states of a single gbit can be reversibly transformed
into each other and there is an isomorphism between states and effects. However, as
shown in [34] the joint states cannot be reversibly transformed. A tensor product which
inherits an isomorphism between joint states and effects can be constructed, but it was
shown to treat equal subsystems differently [11].
Given local quantum systems it has been shown that the ordinary quantum tensor

<!-- page 34 -->
Generalized Probability Theories

34

product is the only one that preserves transitivity [43]. Another work explores the
opposite direction [44]. The authors assume transitivity on joint states and local systems
with state spaces bounded by hyperspheres, which is a generalization of the threedimensional Bloch ball of qubits known as a hyperbit [14]. It was shown that entangled
states in such a scenario are only possible for dimension three [44], which was used
in [45] to explain why we are living in a three-dimensional world.
7.2. Genuine multipartite quantum features:
Beyond the features inherited from single systems there are also genuine multipartite
features that are characteristic for quantum theory. Recall that for entangled states
the marginal state is mixed even though the joint state might be extremal. Quantum
theory allows also the opposite, namely, any mixed state can be regarded as the marginal
of a pure extremal state – a process called purification [24, 46, 47]. As a consequence
any stochastic mapping from one mixed state to another can be realized as a reversible
unitary transformation in a higher-dimensional state space without information loss [48].
Since there is a continuum of mixtures, the possibility of purification requires
a continuum of pure entangled states. There is also an isomorphism between the
transformations of single systems and bipartite joint states [49, 50]. This was recently
used to generalize Bayesian inference to quantum states [51]. This isomorphism can
be further decomposed into two components. On the one hand, using the self-duality
of quantum systems, states are converted to corresponding effects given by the same
operator. On the other hand the transformation itself can be realized via steering,
i.e. the ability to obtain any state as the conditional state of a joint system [52, 53].
Steering is a prerequisite of more advanced multipartite quantum features, like quantum
teleportation [27, 54] and entanglement swapping [55].
As pointed out before, nonlocal correlations are a central feature of quantum
theory. Several articles have examined the relation between entanglement and non-local
correlations in quantum theory. As quantum theory balances entanglement in states and
effects, extending the joint state space to the maximal tensor product would potentially
allow for new correlations. While this is not the case for bipartite systems [56], it was
found that the maximal tensor product of multipartite systems with more than two
subsystems can indeed generate new correlations that are not possible in the standard
tensor product [57].
Not only entanglement but also the local structure of the subsystems influences
nonlocal correlations. For example, it was shown in [10] that joint states that resemble
the maximally entangled states in quantum theory exist in the maximal tensor product
for a class of toy theories with regular polygon shaped subsystems. It turned out that
the possible nonlocal correlations strongly depend on the subsystems’ structure. For
bipartite systems consisting of two identical polygons with an odd number of vertices
the possible correlations were found to be strictly weaker as in the quantum case.

<!-- page 35 -->
35

Generalized Probability Theories
A

B

MA

MB
ω AB

Blackbox

a

b
p(ab|AB)

=
b

a

b

B
ω AB (eA
a ⊗ eb )

Figure 12. Nonlocal boxes as a device-independent model of nonlocal correlations
abstracting from specific measurements and states.

Polygons with an odd number of vertices, however, yield correlations stronger or equal
than quantum correlations. A general connection between nonlocality and uncertainty
relations of subsystems has been found in Ref. [58].
The device-independent view on nonlocal correlations studies correlations
independent of specific joint states and local measurements, simply by considering the
probabilities of input-output combinations for a given choice of measurement as input
and the outcomes as outputs (see Fig. 12). These so-called nonlocal boxes allow us to
compare general no-signaling correlations to those possible in quantum theory without
referring to specific theories. For the CHSH setup the no-signaling correlations form an
eight-dimensional polytope with the classical correlations and the PR box with maximal
nonlocality as extremal points [59, 60]. The quantum correlations form a convex subset
with infinitely many extremal points. This set can be determined by a infinite hierarchy
of semi-definite programs, whereas an analytical upper bound known as Q1 has been
derived from the first order [61,62]. It was shown that any theory that is able to recover
classical physics in the macroscopic limit has correlations limited by this bound [63].
Also Q1 obeys information causality [64, 65]. That is given the nonlocal resource and m
bits of classical communication a party on one side can learn at most m bits about the
system on the other side. Note that this is a generalization of no-signaling that refers
to the situation with m = 0. Different to quantum correlations general no-signaling
correlations can violate information causality up to the extreme cases of PR boxes
that can evaluate any global function that depends on both local inputs from only one
classical bit of communication (trivial communication complexity) [66]. Interestingly,
for some nonlocal boxes given multiple copies allows to distill PR boxes by using only
classical processing at each of the local parts individually [67], whereas the quantum
correlations are closed under such operations [68].
In conclusion quantum theory a lot of unique characteristic physical features. The
framework of Generalized Probabilistic Theories presented in this review paper played
a crucial role to identify many of those.

<!-- page 36 -->
Generalized Probability Theories

36

Acknowledgments
We thank Markus Müller for discussions and in particular for pointing out the Holevo
construction of a gbit by a higher dimensional restricted classical system. PJ is
supported by the German Research Foundation (DFG).
Appendix A. Partial order of effects
Given two effects ei , ej one is said to be dominated by the other iff it occurs with lower
probability for any state:
ei ≤ ej ⇔ ei (ω) ≤ ej (ω)∀ω ∈ Ω

(A.1)

Note that there are effects that cannot be compared in such a way. There might be
states that give higher probabilities for ei , while other states give higher probabilities
on ej . Therefore this is called a partial order.
A partial order on the elements of a vector space can be induced by a convex cone.
The partial order of effects is based on the dual cone V+∗ with
ei ≤ ej ⇔ ei ∈ ej − V+∗ .

(A.2)

To see that this is equivalent to (A.1) recall that the dual cone V+∗ is given by all elements
in V ∗ with non-negative results on the state space elements ω ∈ Ω. Consequently,
subtracting one of these elements from an effect cannot result in a bigger value for any
state.
Note that the dual cone depends on the state space Ω. An extension of a model
with new states might therefore also affect the partial order.
References
[1] L. Hardy and R. Spekkens. Why physics needs quantum foundations. Phys. Can., 66(2):73–76,
2010.
[2] P. Ball. Physics: Quantum quest. Nature, 501(7466):154–156, 2013.
[3] G.W. Mackey. Mathematical Foundations of Quantum Mechanics. Mathematical physics
monograph series. Benjamin, 1963.
[4] G. Ludwig. Foundations of quantum mechanics. Number Bd. 1 in Texts and monographs in
physics. Springer, 1983.
[5] G. Ludwig. An Axiomatic Basis for Quantum Mechanics: Volume 1: Derivation of Hilbert Space
Structure. An Axiomatic Basis for Quantum Mechanics: Derivation of Hilbert Space Structure.
Springer, 1985.
[6] K. Kraus. States, Effects, and Operations Fundamental Notions of Quantum Theory, volume 190
of Lecture Notes in Physics. Springer Berlin / Heidelberg, 1983.
[7] T. Heinosaari and M. M. Wolf. Nondisturbing quantum measurements. J. Math. Phys., 51:092201,
2010.

<!-- page 37 -->
Generalized Probability Theories

37

[8] D. Reeb, D. Reitzner, and M. M. Wolf. Coexistence does not imply joint measurability. Journal
of Physics A: Mathematical and Theoretical, 46:462002, 2013.
[9] P. Janotta and R. Lal. Generalized probabilistic theories without the no-restriction hypothesis.
Phys. Rev. A, 87:052131, 2013.
[10] P. Janotta, C. Gogolin, J. Barrett, and N. Brunner. Limits on nonlocal correlations from the
structure of the local state space. New J. Phys., 13(6):063024, 2011.
[11] P. Janotta. Generalizations of boxworld. In Proceedings 8th International Workshop on Quantum
Physics and Logic, Nijmegen, Netherlands, October 27-29, 2011, volume 95 of EPTCS, pages
183–192. Open Publishing Association, 2012.
[12] C. Ududec. Perspectives on the Formalism of Quantum Theory. PhD thesis, University of
Waterloo, Canada, 2012.
[13] M. P. Müller, O. C. O. Dahlsten, and V. Vedral. Unifying typical entanglement and coin tossing: on
randomization in probabilistic theories. Communications in Mathematical Physics, 316(2):441–
487, 2012.
[14] M. Pawlowski and A. Winter. Hyperbits: The information quasiparticles. Phys. Rev. A, 85:022331,
2012.
[15] Howard Barnum, Jonathan Barrett, Lisa Orloff Clark, Matthew Leifer, Robert Spekkens, Nicholas
Stepanik, Alex Wilce, and Robin Wilke. Entropy and information causality in general
probabilistic theories. New J. Phys., 12(3):033024, 2010.
[16] C. Pfister and S. Wehner. An information-theoretic principle implies that any discrete physical
theory is classical. Nature Comm., 4:1851, 2013.
[17] R. W. Spekkens. Evidence for the epistemic view of quantum states: A toy theory. Phys. Rev.
A, 75:032110, 2007.
[18] A. J. P. Garner, O. C. O. Dahlsten, Y. Nakata, M. Murao, and V. Vedral. A framework for phase
and interference in generalized probabilistic theories. New J. Phys., 15(9):093044, 2013.
[19] L. Hardy. Quantum theory from five reasonable axioms. preprint, arXiv:quant-ph/0101012, 2001.
[20] B. Dakic and C. Brukner. Deep Beauty: Understanding the Quantum World through Mathematical
Innovation, chapter Quantum theory and beyond: is entanglement special?, pages 365–392.
Cambridge University Press, 2011.
[21] Ll. Masanes and M. P. Müller. A derivation of quantum theory from physical requirements. New
J. Phys., 13(6):063001, 2011.
[22] A. Wilce. Conjugates, correlation and quantum mechanics. preprint, arXiv:1206.2897, 2012.
[23] J. Barrett. Information processing in generalized probabilistic theories. Phys. Rev. A, 75:032304,
2007.
[24] Giulio Chiribella, Giacomo Mauro D’Ariano, and Paolo Perinotti. Informational derivation of
quantum theory. Phys. Rev. A, 84:012311, 2011.
[25] I. Bengtsson, S. Weis, and K. Zyczkowski. Geometry of the set of mixed quantum states:
An apophatic approach. In Geometric Methods in Physics. XXX Workshop 2011, Trends in
Mathematics, pages 175–197. Springer, 2013.
[26] L. Hardy. Reformulating and reconstructing quantum theory. preprint, arXiv:1104.2066v3, 2011.
[27] H. Barnum, J. Barrett, M. Leifer, and A. Wilce. Teleportation in general probabilistic
theories. In Mathematical Foundations of Information Flow (Clifford Lectures Information
2008), Proceedings of symposia in applied mathematics, pages 25–47. American Mathematical
Society, 2012.
[28] M. P. Müller and C. Ududec. Structure of reversible computation determines the self-duality of
quantum theory. Phys. Rev. Lett., 108:130401, 2012.
[29] Ll. Masanes, A. Acin, and N. Gisin. General properties of nonsignaling theories. Phys. Rev. A,
73:012112, 2006.
[30] A. S. Holevo. Probabilistic and Statistical Aspects of Quantum Theory. Publications of the Scuola
Normale Superiore. Springer, 2011.
[31] H. Barnum, J. Barrett, M. Leifer, and A. Wilce. Generalized no-broadcasting theorem. Phys.

<!-- page 38 -->
Generalized Probability Theories

38

Rev. Lett., 99:240501, 2007.
[32] A. J. Short and J. Barrett. Strong nonlocality: a trade-off between states and measurements.
New J. Phys., 12(3):033034, 2010.
[33] P. Janotta and R. Lal. Non-locality in theories without the no-restriction hypothesis. In
Proceedings 10th International Workshop on Quantum Physics and Logic, Barcelona, Spain,
July 17-19, 2013, volume XX of to be published in EPTCS, page XXX. Open Publishing
Association, 2013.
[34] D. Gross, M. P. Müller, R. Colbeck, and O. C. O. Dahlsten. All reversible dynamics in maximally
nonlocal theories are trivial. Phys. Rev. Lett., 104:080402, 2010.
[35] A. Einstein, B. Podolsky, and N. Rosen. Can quantum-mechanical description of physical reality
be considered complete? Phys. Rev., 47:777–780, 1935.
[36] J. S. Bell. On the einstein podolsky rosen paradox. Physics, 1:195–200, 1964.
[37] G. Vallone, G. Lima, E. S. Gomez, G. Canas, J.-A. Larsson, P. Mataloni, and A. Cabello. Bell
scenarios in which nonlocality and entanglement are inversely related. Phys. Rev. A, 89:012102,
2014.
[38] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt. Proposed experiment to test local
hidden-variable theories. Phys. Rev. Lett., 23:880–884, 1969.
[39] A. Aspect. Bell’s inequality test: more ideal than ever. nature, 398:189–190, 1999.
[40] B.S. Cirelson. Quantum generalizations of Bell’s inequality. Lett. Math. Phys., 4(2):93–100, 1980.
[41] S. Popescu and D. Rohrlich. Quantum nonlocality as an axiom. Found. Phys., 24(3):379, 1994.
[42] Ll. Masanes, M. P. Mueller, R. Augusiak, and D. Perez-Garcia. Existence of an information unit
as a postulate of quantum theory. PNAS, 110(41):16373, 2013.
[43] G. de la Torre, Ll. Masanes, A. J. Short, and M. P. Müller. Deriving quantum theory from its
local structure and reversibility. Phys. Rev. Lett., 109:090403, 2012.
[44] Ll. Masanes, M. P. Müller, D. Perez-Garcia, and R. Augusiak. Entanglement and the threedimensionality of the bloch ball. preprint, arXiv:1111.4060v2, 2013.
[45] M. P. Müller and Ll. Masanes. Three-dimensionality of space and the quantum bit: an informationtheoretic approach. New J. Phys., 15(5):053040, 2013.
[46] I. Gelfand and M. Neumark. Mat. sb. Math. Sb., 12(54):197–217, 1943.
[47] I. E. Segal. The group algebra of a locally compact group. Trans. Amer. Math. Soc., 61:69–105,
1947.
[48] W. F. Stinespring. Positive functions on c∗ -algebras. Proc. Am. Math. Soc., 6:211, 1955.
[49] M.-D. Choi. Completely positive linear maps on complex matrices. Linear Algebra and its
Applications, 10(3):285–290, 1975.
[50] A. Jamiolkowski. Linear transformations which preserve trace and positive semidefiniteness of
operators. Rep. Math. Phys., 3(4):275–278, 1972.
[51] M. S. Leifer and Robert W. Spekkens. Towards a formulation of quantum theory as a causally
neutral theory of bayesian inference. Phys. Rev. A, 88:052130, 2013.
[52] E. Schrödinger. Discussion of probability relations between separated systems. Proc. Cambridge
Phil. Soc., 31(4):553, 1935.
[53] H. Barnum, C. P. Gaebler, and A. Wilce. Ensemble steering, weak self-duality, and the structure
of probabilistic theories. Found. Phys., 43(12):1411–1427, 2013.
[54] C. H. Bennett, G. Brassard, C. Crepeau, R. Jozsa, A. Peres, and W. K. Wootters. Teleporting
an unknown quantum state via dual classical and einstein-podolsky-rosen channels. Phys. Rev.
Lett., 70:1895–1899, 1993.
[55] H.-J. Briegel, W. Dür, J. I. Cirac, and P. Zoller. Quantum repeaters: The role of imperfect local
operations in quantum communication. Phys. Rev. Lett., 81:5932–5935, 1998.
[56] H. Barnum, S. Beigi, S. Boixo, M. B. Elliott, and S. Wehner. Local quantum measurement and
no-signaling imply quantum correlations. Phys. Rev. Lett., 104:140401, 2010.
[57] A. Acin, R. Augusiak, D. Cavalcanti, C. Hadley, J. K. Korbicz, M. Lewenstein, Ll. Masanes, and
M. Piani. Unified framework for correlations in terms of local quantum observables. Phys. Rev.

<!-- page 39 -->
Generalized Probability Theories

39

Lett., 104:140404, 2010.
[58] J. Oppenheim and S. Wehner. The uncertainty principle determines the nonlocality of quantum
mechanics. Science, 330(6007):1072–1074, 2010.
[59] Jonathan Barrett, Noah Linden, Serge Massar, Stefano Pironio, Sandu Popescu, and David
Roberts. Nonlocal correlations as an information-theoretic resource. Phys. Rev. A, 71:022101,
2005.
[60] V. Scarani. Ultracold Gases and Quantum Information, chapter Quantum Information: Primitive
notions and quantum correlation, pages 105–177. Oxford University Press, 2009.
[61] M. Navascues, S. Pironio, and A. Acin. Bounding the set of quantum correlations. Phys. Rev.
Lett., 98:010401, 2007.
[62] M. Navascues, S. Pironio, and A. Acin. A convergent hierarchy of semidefinite programs
characterizing the set of quantum correlations. New J. Phys., 10(7):073013, 2008.
[63] M. Navascues and H. Wunderlich. A glance beyond the quantum model. Proc. Roy. Soc. Lond.
A, 466:881–890, 2010.
[64] M. Pawlowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter, and M. Zukowski. Information
causality as a physical principle. Nature, 461:1101–1104, 2009.
[65] J. Allcock, N. Brunner, M. Pawlowski, and V. Scarani. Recovering part of the boundary between
quantum and nonquantum correlations from information causality. Phys. Rev. A, 80:040103,
2009.
[66] W. van Dam. Implausible consequences of superstrong nonlocality. preprint, arXiv:quantph/0501159, 2005.
[67] N. Brunner and P. Skrzypczyk. Nonlocality distillation and postquantum theories with trivial
communication complexity. Phys. Rev. Lett., 102:160403, 2009.
[68] J. Allcock, N. Brunner, N. Linden, S. Popescu, P. Skrzypczyk, and T. Vertesi. Closed sets of
nonlocal correlations. Phys. Rev. A, 80:062107, 2009.
