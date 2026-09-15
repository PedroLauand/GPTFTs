---
type: paper
date: 2014-03-17
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1403.4147v4)
reviewed: false
---

# Higher-order interference and single-system postulates characterizing quantum theory

Machine-generated and unreviewed text extraction of arXiv:1403.4147v4
(27 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1403.4147v4>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Higher-order interference and single-system postulates characterizing quantum theory
Howard Barnum,1, 2, ∗ Markus P. Müller,3, † and Cozmin Ududec4, ‡
1

arXiv:1403.4147v4 [quant-ph] 3 Jan 2015

Department of Physics and Astronomy, University of New Mexico,
1919 Lomas Blvd. NE, Albuquerque, NM 87131
2
Stellenbosch Institute for Advanced Studies (STIAS),
Wallenberg Research Center at Stellenbosch University, Marais Street, Stellenbosch 7600, South Africa
3
Institut für Theoretische Physik, Universität Heidelberg,
Philosophenweg 19, D-69120 Heidelberg, Germany
4
Invenia Technical Computing, 135 Innovation Dr., Winnipeg, MB R3T 6A8, Canada
(Dated: April 8, 2014; revised November 12, 2014)
We present a new characterization of quantum theory in terms of simple physical principles
that is different from previous ones in two important respects: first, it only refers to properties
of single systems without any assumptions on the composition of many systems; and second, it
is closer to experiment by having absence of higher-order interference as a postulate, which is
currently the subject of experimental investigation. We give three postulates – no higher-order
interference, classical decomposability of states, and strong symmetry – and prove that the only
non-classical operational probabilistic theories satisfying them are real, complex, and quaternionic
quantum theory, together with 3-level octonionic quantum theory and ball state spaces of arbitrary
dimension. Then we show that adding observability of energy as a fourth postulate yields complex
quantum theory as the unique solution, relating the emergence of the complex numbers to the
possibility of Hamiltonian dynamics. We also show that there may be interesting non-quantum
theories satisfying only the first two of our postulates, which would allow for higher-order interference
in experiments while still respecting the contextuality analogue of the local orthogonality principle.

I.

INTRODUCTION

Quantum theory currently underpins much of modern
physics and is essential in many other scientific fields and
countless technological applications. However, by most
accounts quantum phenomena remain rather mysterious:
there is no generally accepted intuitive picture of the underlying reality, and the standard textbook introductions
of the mathematical formalism lack a simple conceptual
motivation.
With the rise of quantum information processing and
the ever more refined control of quantum phenomena,
there has recently been a surge of diverse attempts to
tackle such foundational questions. These range from
studies of the information processing capabilities of theories similar to quantum theory [10, 15, 35–37], to reconstructions of the formalism from information-theoretic
principles [42, 43, 48, 50, 51, 71], to no-go theorems regarding interpretations and generalizations of the formalism [8, 9, 58], to novel experiments testing various predictions of the theory [5–7].
In this paper we give several closely related reconstructions of the mathematical structure—Hilbert space, Hermitian observables, positive operator-valued measures—
of finite-dimensional quantum theory from simple postulates with clear physical significance and generality.
Providing such an explanation for the Hilbert space

∗ Electronic address: hnbarnum@aol.com
† Electronic address: markus@mpmueller.net
‡ Electronic address: cozster@gmail.com

structure of quantum theory in terms of physically (not
just mathematically) natural postulates is important for
several reasons. First, deeper and more reasonable principles can help to dissolve the mysteries of quantum phenomena and make them more intelligible and easier to
teach. Two well-known examples of this approach are
Kepler’s laws of planetary motion and their explanation
through Newton’s laws of motion and gravitation, and
the Lorentz transformations and their explanation in Einstein’s two relativity postulates. Second, it can be argued
that this approach will be essential in making progress on
problems such as formulating a theory unifying quantum
and gravitational physics, as well as for developing potentially more accurate and more fundamental theories. In
the absence of a picture of the underlying reality, we can
use first principles to proceed toward the next physical
theory in a careful, conceptual fashion. More practically,
this approach can shed light on what is responsible for
the power of quantum information processing and cryptography.
Because quantum theory applies to an extremely broad
range of physical systems and phenomena, and its probabilistic structure seems essential, we work within a broad
framework for studying probabilistic physical theories
(usually called operational probabilistic theories). These
are theories that succinctly describe sets of experiments
and assign probabilities to measurement outcomes. More
precisely, we imagine that physicists, or nature, prepare
physical systems in various states, and then observe these
systems in various ways. The outcomes of these observations occur with certain probabilities, which are predicted by the theory. It is important to emphasize that
we do not assume that these probabilities are described

<!-- page 2 -->
2
by quantum theory; instead our postulates will allow us
to derive their structure as represented by quantum theory.
Our postulates are as follows:
1. Classical Decomposability: Every state of a
physical system can be represented as a probabilistic mixture of perfectly distinguishable states of
maximal knowledge (“pure states”).
2. Strong Symmetry: Every set of perfectly distinguishable pure states of a given size can be reversibly transformed to any other such set of the
same size.
3. No Higher-Order Interference: The interference pattern between mutually exclusive “paths”
in an experiment is exactly the sum of the patterns which would be observed in all two-path subexperiments, corrected for overlaps.
4. Observability of Energy: There is non-trivial
continuous reversible time evolution, and the generator of every such evolution can be associated
to an observable (“energy”) which is a conserved
quantity.
Before discussing their physical interpretation and motivation in more detail, we point out that all of our postulates refer to single systems only. This is in contrast to
earlier reconstructions of quantum theory [42, 43, 48, 50]
which rely heavily on properties of composite systems.
Our motivation to rely on single systems is as follows.
It is not clear that the notion of subsystems and their
composition, as it is often used in information-theoretic
circuit diagrams and category-theoretic considerations,
applies to physics without change in its full operational
interpretation. For example, if a composite quantum system consists of spacelike separated subsystems, then the
causal spacetime structure of special relativity imposes
additional complications when describing the possible
joint measurements on the composite system [77]. These
additional restrictions are usually not captured by operational approaches, which just declare a set of states and
measurements for the composite system, and postulate
that these can in principle be implemented to arbitrary
accuracy. Therefore, a safe strategy for an operational
approach seems to be to avoid making assumptions about
the state space structure of composite systems, and to
talk only about stand-alone systems. These may or may
not correspond to effective physical subsystems that can
be controlled by an agent in a laboratory.
Moreover, there has recently been a surge of interest in finding compelling physical principles that explain
the specific contextuality behavior of quantum theory as
compared to other probabilistic theories. This line of
research aims at analyzing the single-system analogue
of quantum non-locality, and understanding its specific
characteristics in terms of principles such as “consistent
exclusivity” [54]. Our results also contribute to this line

1
2

"click!"

3
4

FIG. 1: Higher-order interference. Consider a particle
which can pass one of M (here: M = 4) slits, where some
of the slits may be blocked by the experimenter (indicated
by the black bars). After passing the multi-slit setup, the
particle may trigger a certain event, for example the click of
a detector localized in a certain area of the screen. We are
interested in the probability pJ of this event, given that slits
J ⊂ {1, 2, . . . , M } are open (for example p23 in the depicted
setup).
Classically, the probability of such an event given that all
four slits are open, p1234 , equals p1 + p2 + p3 + p4 , where pi
is the probability assuming than only slit i is open. This
is violated in quantum theory due to interference. However, even in quantum theory, the total probability can be
computed from contributions of pairs of slits only: we have
p1234 = p12 + p13 + p14 + p23 + p24 + p34 − 2p1 − 2p2 − 2p3 − 2p4 .
It is in this sense that quantum theory has second-, but no
third- or higher-order interference. The definition of interference that we use is not restricted to spatially arranged slits,
but is formulated generally for any set of M perfectly distinguishable alternatives in a probabilistic theory.

of research by showing that Postulates 1 and 2 are sufficient to guarantee that systems satisfy consistent exclusivity.
We do not claim that our postulates are the only reasonable ones, but we think that they – like other recent
reconstructions – are more natural than the usual abstract formulations which simply presume Hilbert spaces,
complex numbers, and operators. Moreover, as we discuss below, we think that our formulation is especially
suitable for the search for interesting and physically reasonable modifications of quantum theory; that is, state
spaces that are not described by the Hilbert space formalism but are otherwise consistent and physically plausible.
Comparison to other reconstructions can help uncover
logical relations between various physical structures of
our world. For example, our fourth postulate (observability of energy) is used to rule out non-complex Hilbert
spaces in this work, while in other reconstructions this
role is usually played by the the postulate of tomographic locality, which states that joint states on composite systems are uniquely determined by local measurement statistics and their correlations. Thus, one may
argue that there is a logical relationship between tomo-

<!-- page 3 -->
3
graphic locality and observability of energy, and thus ultimately with the fact that we observe Hamiltonian mechanics in our world.
We will now give a short discussion of the interpretation of our postulates. To clarify the terms in Postulate
1, a set of states is perfectly distinguishable if there is a
measurement whose outcomes can be paired one-to-one
with the states so that each measurement outcome has
probability one when its corresponding state has been
prepared, and probability zero when any of the other
states have been prepared. A state of maximal knowledge (a “pure state”) is a state ω which cannot be written as a nontrivial convex combination of states, i.e. as
ω = pσ+qτ where p+q = 1, p, q > 0, and σ 6= τ . That is,
it cannot be viewed as arising from a lack of knowledge
about which of two distinct states has been prepared.
Postulate 1 can be viewed as a generalization of the
spectral decomposition of every quantum density matrix
as a convex combination of orthogonal rank-one projectors onto orthogonal eigenstates of the density matrix.
However, our postulate is stated purely in terms of the
convex structures of the set of states and of measurement
outcomes; the notion of spectrum of an operator is not
involved. An important part of the physical significance
of this postulate is that it appears likely to be needed
for an information theory and probably a statistical mechanics that share desirable and physically fundamental
properties with those supported by quantum theory. In
particular, it is a plausible conjecture that this postulate
implies the correspondence of two natural ways of defining entropies for states in generalized probabilistic theories [66, 67]: the first as the minimal entropy of the outcomes of a fine-grained measurement made on the state,
and the second as the minimal entropy of a preparation
of the state as a mixture of pure states.
Postulate 2 expresses a fundamental symmetry: given
any integer n, all n-level systems are informationally
equivalent. That is, we can transmit (not necessarily
copy) the state of any n-level system to any other system
without losing information, at least in principle. This
implies a certain minimal amount of possible reversible
dynamics or computational power.
Postulate 3, that the system exhibits at most “secondorder interference,” is based on the notion of multi-slit
interference introduced by Rafael Sorkin [4]. This is a
manifestly physical assumption which is currently under
experimental investigation [5, 6]. The precise notion of
an interference experiment will be defined in Section V
below; an illustration is given in Figure 1.
This postulate suggests a possible route towards obtaining concrete predictions for conceivable third-order
interference in experiments: drop the third postulate,
and work out the new set of theories that satisfy only
Postulates 1 and 2 (and possibly 4). As we will show, any
system of this kind – if it exists – has a set of “filtering”
operations that represent an orthomodular lattice known
from quantum logic [38], but these filters do not necessarily preserve the purity of states as they do in quantum

theory (equivalently, the lattice does not satisfy the “covering law”). However, these systems still satisfy the principle of “Consistent Exclusivity” [54], bringing their contextuality behavior close to quantum theory, despite the
appearance of (non-quantum) third-order interference.
In this way, our results hint at possible physical properties of conceivable alternative theories against which
quantum theory can be tested in interference experiments, and which may be of independent mathematical interest. In particular, the existence of theories exhibiting higher-order interference and containing quantum theory as a subtheory has been conjectured for several years. Preliminary results indicate interesting physical properties of those theories [56], but the concrete
construction of the corresponding state spaces is still an
open problem. We hope that our approach can help to
make progress on this question.
We obtain our main result by first showing that the
first three postulates bring us very close to quantum theory: they imply that systems are described by finitedimensional irreducible (simple) formally real Jordan algebras, or are classical. Moreover, these three postulates
precisely characterize this class of theories, since classical
systems and irreducible Jordan algebras all satisfy Postulates 1-3. As Jordan, von Neumann and Wigner [13]
showed, the formally real irreducible Jordan algebras are
the real, complex, and quaternionic quantum theories
(for all finite dimensions), one exceptional case (the 3 × 3
octonionic “density matrices”) and the spin factors (ballshaped state spaces) of all finite dimensions. Standard
complex quantum theory is the only one among these
which also satisfies the fourth postulate.
The association of energy with a conserved physical quantity is an important principle of both quantum
and classical theory, exhibited for example in the Lagrangian formulation of classical mechanics in the guise
of Noether’s theorem; this provides some motivation for
our energy observability postulate.
Further, Postulates 1, 2 and 4 seem likely to be
necessary—or at least sufficient—to run standard statistical mechanics arguments, a possibility we will explore
in further work. We have already mentioned the conjecture that Postulate 1 implies the equivalence of measurement and preparation entropy, which likely has relevance
to thermodynamic processes and Maxwell’s demon arguments. Reversible processes, the subject of Postulate 2,
are even more crucial in classical and quantum thermodynamics.

II.

OPERATIONAL PROBABILISTIC
THEORIES

In this section, we summarize the standard mathematical framework for operational probabilistic theories,
and give needed definitions and facts about convexity
and cones. References for the mathematics include [14]
and [34]. More details on the framework can be found in

<!-- page 4 -->
4
e.g. [37], [50], [36], [35], [16]; also, [75, 76] offer accessible
introductions. This review is primarily to fix notation
and clarify the specific version used here.
The primitive elements of operational probabilistic
theories are experimental devices and probabilities. In
particular, experimental devices can be classified into
preparations, transformations, and measurements. With
each use, a preparation device (such as an oven, antenna,
or laser) outputs an instance of a physical system, denoted by A, in some state ω specified by the type of
device and its various settings. The system then passes
through a transformation device (such as a beam splitter,
or Stern-Gerlach magnet) which modifies the state of the
system, in a potentially non-deterministic fashion. Finally, a measurement device takes in the system, and one
of a distinct set of outputs (such as a light flashing, or a
pointer being in some range of possible positions) signals
the measurement outcome. Even though we motivate the
formalism by example of such laboratory devices, the resulting operational framework is not restricted to this
setting and may also be used to describe other physical
processes.
A main purpose of a physical theory in this framework
is to specify the probabilities of the outcomes of any measurement made on a system that has been prepared in a
given state. To this end, single measurement outcomes,
called effects, will be denoted by lowercase letters such
as e. The probability of obtaining an outcome e, given
state ω, will be denoted e(ω).
By standard arguments, each state can be specified
by a minimal list of measurement outcome probabilities,
which contains sufficient information to predict the probabilities of all measurements that can be in principle performed on the system. Using this idea and a further convexity argument, states can therefore be represented as
elements of a real linear space of some finite dimension
KA , which we denote also by A. Further, for each system
A there is a convex compact subset, ΩA ⊂ A, of normalized states in a real affine space of dimension KA − 1
which is embedded in A as an affine plane not intersecting the origin. The nonnegative multiples of elements of
ΩA form a cone A+ ⊂ A, of unnormalized states. This
cone has several useful properties: first, it is topologically
closed ; second, it has full dimension, i.e. its linear span
is all of A; and third, it is pointed, which means that the
only linear subspace it contains is {0}. Cones with these
three properties are also called regular.
Effects then become linear functionals from A to R
such that 0 ≤ e(ω) ≤ 1 for all ω ∈ ΩA , i.e. they give valid
probabilities on normalized states. As linear functionals
from the vector space A to the field R over which it is
defined, effects are elements of the dual space A∗ , which is
the vector space of all such functionals. The nonnegative
multiples of effects constitute the dual cone A∗+ := {e ∈
A∗ : ∀γ ∈ A+ e(γ) ≥ 0}. Given our embedding of ΩA
in A, there is a unique unit functional uA ∈ A∗ that
evaluates to 1 on every element of ΩA . The set of all
effects is the unit order interval, [0, uA ] := {e ∈ A∗+ : 0 ≤

e ≤ uA } ⊂ A∗+ . This notation uses the ordering obtained
from the regular cone A∗+ , writing x ≤ y for y − x ∈ A∗+ .
For a given system, not all mathematically valid effects
may be “operationally possible” measurement outcomes,
so we define a subset E of the full set of effects [0, uA ],
which we call the allowed effects. Thus we are not making the assumption sometimes called the “no-restriction
hypothesis” [41, 50, 63] or “local saturation” [64], nor
the equivalent dual requirement (discussed, e.g., in [65],
where it is considered as a kind of analogue, for effect
algebras, of Gleason’s theorem) that the set of states be
the full set of mathematically consistent states on the
set of effects. The reader should bear in mind that some
authors use just “effects” to refer to what we call “allowed effects”, and say something like “mathematically
consistent effects” to refer to what we are just calling effects. We make weak, operationally natural assumptions
on the subset E: it is convex and topologically closed,
contains uA , and for every x ∈ E, uA − x is also in E (so
that x can be part of at least one complete measurement,
namely {x, uA − x}). We also assume that E has full dimension (otherwise, there would be states ϕ 6= ω that
give the same outcome probabilities for all allowed measurements, which means that we would not have called
them “different states” to start with).
We define a measurement
as any collection of allowed
P
effects ei such that i ei = uA .1 Since we can imagine
post-processing the output of such a measurement such
that a chosen pair ei and ej of outcomes are grouped
together as a single outcome (a “coarse-graining” of the
measurement), we also assume that ei + ej is allowed. In
brief, we assume that whenever ei , ej are allowed effects
with ei + ej ≤ uA , ei + ej is allowed. From our assumptions, it follows that the set of allowed effects is the unit
order interval [0, uA ] in a regular subcone A]+ (containing uA ) of the dual cone. If A]+ = A∗+ , we say that all
effects are allowed ; in our framework, this is equivalent
to the “no-restriction hypothesis”, or “local saturation”,
mentioned above.
We will need the notion, standard in linear algebra, of
the dual (sometimes called adjoint) T ∗ of a linear map
T : A → A. This is the linear map T ∗ : A∗ → A∗
defined by the condition (f, T x) = (T ∗ f, x), where (., .) :
A∗ × A → R is the canonical “dual pairing” of A∗ and A,
sometimes called the “evaluation map”: (f, x) := f (x).
Associated with every system there is also a set of allowed transformations, which are linear maps T : A → A,
taking states to states, i.e. satisfying T (A+ ) ⊆ A+ (a
property called positivity). Transformations are required
to be normalization-nonincreasing, i.e. uA (T (ω)) ≤ 1

1 It is possible to imagine physical situations where there are fur-

ther restrictions on which effects can occur together in an actual
measurement; to model these situations, one would have to use
an even more general mathematical framework. We are not considering such theories here.

<!-- page 5 -->
5
for all ω ∈ ΩA . The set of allowed transformations is
also closed topologically and under composition. If all
effects are allowed, it follows from positivity and normalization that e ◦ T ∈ E for all allowed effects e (all
elements of E); otherwise we explicitly require this (i.e.,
that T ∗ (E) ⊆ E). Since E is the unit order interval in
A]+ , it is equivalent (for normalization-nonincreasing T )
to require that T ∗ (A]+ ) ⊆ A]+ . We note also that the
normalization-nonincrease condition is equivalent to the
dual condition T ∗ (uA ) ≤ uA . An allowed transformation
T is called reversible if its inverse T −1 exists and is also an
allowed transformation. It follows that reversible transformations T preserve normalization: uA (T (ω)) = uA (ω)
for all ω ∈ A+ (though these are not in general the only
normalization-preserving transformations). The set of all
reversible transformations on a system A is a compact
group GA with Lie algebra gA . For a transformation T ,
the number uA (T (ω)) can be interpreted as the probability of transformation T occurring, if a system prepared
in state ω is subjected to a process that has as a possible
outcome the occurrence of T . In other words, transformations can be part of an instrument in the sense of [72].
A system described by standard complex ndimensional quantum theory fits into this framework.
Its ambient real vector space A is the n2 -dimensional
space of complex Hermitian n × n-matrices, the cone of
states A+ is the set of positive semidefinite matrices,
ΩA is the set of density matrices (the intersection of
A+ with the affine plane {ρ : trρ = 1}), the order unit
is the functional 1 : ρ 7→ trρ, and the allowed effects
are the unit order interval in the dual cone, i.e., the
functionals ρ 7→ tr(Eρ) where 0 ≤ E ≤ 1. The allowed
transformations are the trace-nonincreasing completely
positive maps A → A, and the reversible transformations
are the maps ρ 7→ U ρU † for unitary matrices U .
We now describe some further important notions and
facts about this type of theory and the relevant mathematical structures that will be used in our discussion.
A cone A+ is reducible if the ambient space decomposes into two nontrivial subspaces such that every extremal ray of the cone lies in one or the other of these
subspaces. A system is called reducible if its cone of unnormalized states is reducible. Intuitively, information
about which of these two summands the state is in, is
classical information. Every cone in finite dimension has
a decomposition as a finite sum ⊕ni=1 Ai of irreducible
cones, and if these irreducible components are all onedimensional any base for the cone is affinely isomorphic
to the simplex of probability measures over n outcomes,
so we say the system is classical. Its faces are the subsimplices generated by the subsets of outcomes, its reversible
transformations are the permutations of the vertices, and
more general transformations are given by substochastic
matrices.
One can identify A∗ with A by introducing an inner
product h., .i on A, and interpreting the inner product
as functional evaluation: e(ω) = he, ωi. Via this isomorphism the dual cone A∗+ is identified with the “in-

ternal dual cone” relative to the given inner product,
A∗int
:= {y ∈ A : ∀x ∈ A+ hy, xi ≥ 0}. Often, such
+
an inner-product-space formulation is used as the basic
framework for presenting probabilistic systems and theories; see for example [48, 70]. If an inner product can be
introduced in such a way that A∗int
= A+ , the cone is
+
said to be self-dual and the inner product self-dualizing;
a cone in an inner product space is said to be manifestly
self-dual if the inner product is one that identifies the
cone with its dual.
A set of states ω1 , . . . , ωn ∈ ΩA is called perfectly
distinguishable if there are allowed effects e1 , . . . , en ∈
A]+ which can appear in a common measurement, i.e.
e1 + . . . + en ≤ uA , such that ei (ωj ) = δij , that is, 1 if
i = j and 0 otherwise2 .
A face F of a convexP
set C is a convex subset ofPC such
that α ∈ F and α = i λi ωi , ωi ∈ C, λi > 0, i λi =
1 implies that all ωi ∈ F . In other words F is closed
under inclusion of anything that can appear in a convex
decomposition of an element of F . An exposed face of a
convex set is the intersection of a supporting hyperplane
with the set, easily seen to be a face.
The faces of A+ and those of ΩA are in 1-1 correspondence: the face of A+ corresponding to face F of ΩA is
just {λω : ω ∈ F, λ ≥ 0}. The relation “is a face of”
is transitive: If G is a face of C, and F is a face of G,
then F is a face of C. The orderings of the set of faces
and of the set of exposed faces by subset inclusion each
form a lattice, with greatest lower bound F ∧ G = F ∩ G,
and least upper bound F ∨ G, which is the smallest face
containing both F and G. The face generated by a subset
S of a convex set is the smallest face containing S. If a
lattice has an upper bound, this is conventionally called
1, and a lower bound is called 0; for ΩA we have 1 = ΩA
and 0 = ∅, while for A+ , 1 = A+ and 0 = {0}, where 0
is the 0 of the vector space A. (We adopt the convention
that the empty set ∅ is not counted as a face of A+ .) An
atom is a minimal non-zero element of the lattice; the
atoms of the face lattice of a regular finite-dimensional
cone are the extremal rays, Ray(ω) := {λω : λ ≥ 0} for
ω extremal in ΩA . An element of A+ may be called rayextremal if it is a nonnegative multiple of a pure state of
ΩA .
Quantum systems are self-dual, with all effects allowed,
and with the self-dualizing inner product usually chosen
to be hX, Y i = tr(XY ). (For this reason, the dual cone is
often identified with the positive semidefinite operators,
and the effects with operators E such that 0 ≤ E ≤ 1,
rather than with the functionals ρ 7→ trEρ associated
with such operators.) The faces of a quantum system,
which are all exposed, correspond to the subspaces S
of the underlying Hilbert space: the face FS of Ω corresponding to such a subspace S consists of the density

2 It is equivalent to demand that e +. . .+e = u , because we can
n
1
A
P
always redefine e01 := e1 , . . . , e0n−1 := en−1 , e0n := uA − n−1
i=1 ei .

<!-- page 6 -->
6
matrices ρ whose images, when viewed as linear operators
on that Hilbert space, are contained in S. Equivalently,
they are those density matrices whose convex decompositions into rank-one projectors involve nonzero probabilities only for projectors onto subspaces of S.
III.

CONSEQUENCES OF POSTULATES 1+2

a frame with corresponding effects f1 , . . . , fN such that
fi (ϕj ) = δij .
According to Postulate 2, there is a reversible transformation T ∈ GA such that T ϕi = ωi for all i =
1, . . . , min{n, N }. Suppose that n ≥ N , then
µ = Tµ =

N
X
i=1

We call a list of n perfectly distinguishable pure states
a frame of size n, or n-frame. The convex hull of such
a set of states is a simplex, isomorphic to the space of
probability measures on n alternatives, which we call a
“classical subspace” of the state space. For every finitedimensional system A, there is a largest frame size NA ;
frames of this size are called maximal. In quantum theory, a frame corresponds to a set of mutually orthogonal pure states, and it is maximal if the corresponding
state vectors are an orthonormal basis of the underlying
Hilbert space.
Using the concepts we have introduced, our first two
postulates can be stated as follows:
Postulate 1. Every
P state ω ∈ Ω has a decomposition
of
the
form
ω
=
i pi ωi , for some probabilities pi ≥ 0,
P
i pi = 1, and some n-frame ω1 , . . . , ωn , for some n ∈
N.
Postulate 2. If ω1 , . . . , ωn and ϕ1 , . . . , ϕn are n-frames
for some n ∈ N, then there is a reversible transformation
T such that T ωi = ϕi for all i.
We could paraphrase Postulate 1 as “every state lies in
some classical subspace”, and Postulate 2 as “all classical
subspaces of a given size are equivalent”.
Proposition 1. Postulates 1 and 2 imply that all effects
are allowed.
Proof. We show that every effect e ∈ A∗+ that generates
an exposed ray of A∗+ is allowed, i.e. an element of A]+ .
It follows that all effects are allowed, since the exposed
rays generate A∗+ via convex combinations and closure.
Thus, let e ∈ A∗+ be an effect with maxω∈ΩA e(ω) = 1
such that the set of non-negative multiples of e is an
exposed ray of A∗+ . By the definition of exposed ray, there
is an x ∈ A+ such that every effect f ∈ A∗+ with f (x) = 0
must be a non-negative multiple of e; consequently, if
f (x) = 0, f ∈ A∗+ and maxω∈ΩA f (ω) = 1 then f = e.
We may choose x to be normalized.
According to Postulate 1, there isPsome n ∈ N and
n
some frame ω1 , . . . , ωn such that x = j=1 λj ωj ; we may
choose the λj to be non-zero. The corresponding effects
will be denoted e1 , . . . , en , i.e. ei (ωj ) = δij . Since e(x) =
0 we have e(ωj ) = 0 for all j = 1, . . . , n.
We define the maximally mixed state µ by integrating
with Haar measure over the group of reversible transformations;
that is, choose any pure state ω, and set
R
µ := GA Gω dG. This state also has a frame decomposiPN
tion µ = i=1 ηi ϕi with N ∈ N, ηi > 0, and ϕ1 , . . . , ϕN

ηi T ϕi =

N
X

ηi ωi ,

i=1

R
hence e(µ) = 0 = GA e(Gω) dG. Since G 7→ e(Gω) is a
continuous non-negative function on GA , we must have
e(Gω) = 0 for all G ∈ GA , and thus e(ω 0 ) = 0 for all pure
states ω 0 . Since the pure states span the full linear space,
we obtain e = 0, which is a contradiction.
Thus we have n < N . Consider the allowed effect
fN ◦ T −1 . It satisfies
fN ◦ T −1 (x) =

n
X
j=1

λj fN (T −1 ωj ) =

n
X

λj fN (ϕj ) = 0,

j=1

and since maxω∈ΩA fN ◦ T −1 (ω) = 1, we have fN ◦ T −1 =
e; in particular, e is an allowed effect.
For the following proposition, recall that a set of states
is said to generate a face F if F is the smallest face that
contains these states.
Proposition 2. Postulates 1 and 2 imply that every face
of Ω is generated by a frame. Any two frames that generate the same face F have the same size, called the rank of
F , and denoted |F |. Moreover, if G ( F then |G| < |F |,
and every frame of size |F | in F generates F .
Proof. A face is generated by any element of its relative
interior. By Postulate 1, such an element is in the convex
hull of a frame; this frame also generates the face.
Let F be any face, and suppose there are two frames
ϕ1 , . . . , ϕm and ω1 , . . . , ωn with m < n that both generate
P F , and e1 , . . . 0, en effects such that ei (ωj ) = δij and
i ei ≤ u. Let F be the face generated by ω1 , . . . , ωm ,
then G := {x ∈ Ω | en (x) = 0} is a face of Ω containing
F 0 but not containing ωn , so F 0 ( F . Due to Postulate 2,
there is a reversible transformation T with T ϕi = ωi for
i = 1, . . . , m, so T F ⊆ F 0 ( F . Since T F is a proper face
of F , it must have smaller dimension, which contradicts
the invertibility and thus reversibility of T . Similarly, if
we had G ( F and |G| ≥ |F |, then a reversible transformation could map F into G, which is a contradiction,
too.
If ω1 , . . . , ω|F | is any frame on F , and G the face that it
generates, then G ⊆ F , and some reversible transformation T will map it to some other frame of the same size
that generates F . Hence T G = F , and this contradicts
G ( F.
Proposition 3. Postulates 1 and 2 imply that A+ is selfdual, with a corresponding self-dualizing inner product
that satisfies hT ϕ, T ωi = hϕ, ωi for all reversible transformations T , i.e. such that all reversible transformations

<!-- page 7 -->
7
are orthogonal. The inner product
p can be chosen so that
the corresponding norm kωk := hω, ωi attains the value
1 on all pure states, and is strictly less than 1 for all
mixed states.
Proof. Ref. [32] shows that bit symmetry and the fact
that all effects are allowed imply this proposition. Bit
symmetry is the 2-frame case of Postulate 2, and we have
shown that all effects are allowed in Proposition 1.
Henceforth, except when we explicitly state otherwise,
we identify A∗ with A via an inner product satisfying
the conditions in the above proposition. Since reversible
transformations T are normalized, we have T ∗ (uA ) =
uA . Moreover, T ∗ = T −1 by orthogonality. T ∗ is also a
reversible transformation; thus, if we regard uA now as
an element of A, we obtain that T −1 uA = uA for all T −1 .
This proves the following:
Proposition 4. Postulates 1 and 2 imply that uA is invariant under all reversible transformations.
Proposition 5. Postulates 1 and 2 imply that every frame ω1 , . . . , ωn can be extended to a frame
ω1 , . . . , ωn , . . . , ωN which generates A+ , i.e. N = |A+ |.
Proof. Let ϕ1 , . . . , ϕN be any frame that generates all of
A
P+ , with effects e1 , . . . , eN such that ej (ϕi ) = δij and
j ej = uA . Then ϕ1 , . . . , ϕn is itself a frame of size
n; thus, according to Postulate 2, there is a reversible
transformation T with T ϕi = ωi for i = 1, . . . , n. For i >
0
−1
n, define
, then e0j (ωi ) = δij
i := T ϕi . Set ej := ej ◦ T
P ω
0
and j ej = uA , and so we have extended ω1 , . . . , ωn to
a frame with N elements.
The following proposition will turn out to be useful in
several proofs.
Proposition 6. Postulates 1 and 2 imply that if
ω1 , . . . , ωn are mutually
Pn orthogonal pure states, then they
are a frame, and i=1 ωi ≤ uA .
Proof.
have to find effects e1 , . . . , en with ei (ωj ) = δij
PWe
n
and i=1 ei ≤ uA . To this end, we will first construct
a decomposition of the order unit. By self-duality and
Proposition 3 , ϕ := uA /huA , uA i is a state in Ω, hence
there is a frame ϕ1 , . . . , ϕN with N = |A+ | and λi ≥ 0
PN
such that uA = huA , uA iϕ = kuA k2 i=1 λi ϕi . For any
permutation π : {1, . . . , N } → {1, . . . , N }, the states
ϕπ(1) , . . . , ϕπ(N ) are again a frame; thus, there is a reversible transformation Tπ with Tπ ϕi = ϕπ(i) . Hence
(using the invariance of uA under reversible transformations)
uA = Tπ uA = kuA k2

N
X
i=1

λi ϕπ(i) = kuA k2

N
X

λi ϕi .

i=1

Taking the inner product with ϕj shows that λπ−1 (j) =
λj ; since this is true for all permutations, all λj are equal
to some λ > 0. Finally, 1 = huA , ϕ1 i = kuA k2 λ, and

PN
so uA =
i=1 ϕi . If ω1 , . . . , ωN is any other frame of
size N , then Postulate 2 implies that there is a reversible
transformation T such that T ϕi = ωi , hence uA = T uA =
PN
PN
T i=1 ϕi = i=1 ωi . Thus, we have shown that every
maximal frame adds up to the order unit.
Now we show the statement of the proposition by induction on n. Start with n = 1. Any pure state ω1 is by
definition a frame of size 1. Moreover, if ϕ ∈ Ω, then the
Cauchy-Schwarz inequality yields
hω1 , ϕi ≤ kω1 k · kϕk ≤ 1,
hence ω1 ≤ uA . Now suppose the statement of the proposition is true for some n, and consider pure mutually orthogonal states ω1 , .P
. . , ωn+1 . Set e1 := ω1 , . . . , en := ωn ,
n
and en+1 := uA − i=1 ei . By the induction hypothesis, en+1 ≥ 0, and so e1 , . . . , en+1 is a measurement with
ei (ωj ) = δij for 1 ≤ i, j ≤ n + 1. Thus, ω1 , . . . , ωn+1 is
a frame. According to Proposition 5, it can be extended
PN
to a maximal frame ω1 , . . . , ωN , and then i=1 ωi = uA
Pn+1
shows that i=1 ωi ≤ uA .
Recall that for any subset S of an inner product space
V its orthogonal complement S ⊥ is defined by S ⊥ :=
{x ∈ V : ∀y ∈ S hx, yi = 0}.
Proposition 7. Postulates 1 and 2 imply that for every
face F of A+ , the set F 0 := F ⊥ ∩ A+ is a face of A+
of rank |F 0 | = N − |F |, where N = |A+ |, and we have
(F 0 )0 = F . Furthermore, if ϕ1 , . . . ϕn is any frame that
is contained in some face F , then it can be extended to a
frame ϕ1 , . . . , ϕn , . . . , ϕ|F | that generates F .
Proof. Let ω ∈ F 0 be any element, and 0 < λ < 1,
ω1 , ω2 ∈ A+ such that ω = λω1 +(1−λ)ω2 . Then, for every f ∈ F , we have 0 = hf, ωi = λhf, ω1 i + (1 − λ)hf, ω2 i.
Due to self-duality, we have hf, ωi i ≥ 0 for i = 1, 2, hence
hf, ω1 i = hf, ω2 i = 0 for all f ∈ F . This shows that
ω1 , ω2 ∈ F 0 , hence F 0 is a face.
Now we determine the rank of F 0 . Let ω1 , . . . , ω|F | be
any frame that generates F , and ϕ1 , . . . , ϕ|F 0 | be a frame
that generates F 0 . Then hωi , ϕj i = 0 for all i, j, and so
Proposition 6 tells us that both frames taken together
are a frame in A+ , proving that |F | + |F 0 | ≤ N . Extend ω1 , . . . , ω|F | to a frame on A+ , then ω|F |+1 , . . . , ωN
are orthogonal to F and thus a frame in F 0 , showing
that |F 0 | ≥ N − |F |, so |F 0 | = N − |F |, and the extension is actually a generating frame of F 0 . Consequently,
ω1 , . . . , ω|F | ∈ (F 0 )0 , and since |(F 0 )0 | = N − |F 0 | =
N − (N − |F |) = |F |, these states generate (F 0 )0 . Since
they also generate F , we must have F = (F 0 )0 .
Now suppose that ϕ1 , . . . , ϕn is any frame contained
in F ; let ω1 , . . . , ω|F | be any frame that generates F . According to Proposition 5, we can extend it to a frame
ω1 , . . . , ω|F | , . . . , ωN that generates all of A+ ; moreover,
the ωi with i ≥ |F | + 1 generate F 0 . But then hω, ωi i = 0
for all i ≥ |F | + 1 and ω ∈ F . Thus, the set of states
ϕ1 , . . . , ϕn , ω|F |+1 , . . . , ωN is a set of mutually orthogonal
pure states and thus, due to Proposition 6, a frame. Using Proposition 5 again, we can find states ϕn+1 , . . . , ϕ|F |

<!-- page 8 -->
8
such that ϕ1 , . . . , ϕn , ϕn+1 , . . . , ϕ|F | , ω|F |+1 , . . . , ωN is a
frame generating A+ . For i ≥ |F | + 1 and j arbitrary,
we have hϕj , ωi i = 0, and since these ωi generate F 0 , we
have hϕj , ωi = 0 for all ω ∈ F 0 . Thus ϕj ∈ (F 0 )0 = F ,
and we have extended ϕ1 , . . . , ϕn to a frame generating
F.
As mentioned in Section I, Postulates 1 and 2 imply
that there is a special transformation called a filter associated with each face of the state space. The next
theorem shows that certain projections are positive (recall that a linear map is positive if it maps the cone A+
into itself), and in Section IV we will further show that
these projections have the additional properties required
of filters.
Theorem 8. Postulates 1 and 2 imply that for every face
F of A+ , the orthogonal projection PF onto the linear
span of F is positive.
Proof. Iochum ([30], see also [31]) has shown that positivity of all PF is equivalent to perfection. (For the reader’s
convenience, and the authors’ peace of mind, a proof is
included in Appendix A.) A cone is called perfect if all
faces F of A+ , regarded as cones in the linear span lin F ,
are themselves self-dual with respect to the inner product
inherited from A. We will therefore show this property,
establishing the claim.
So let F be any face of A+ , and F ∗ ⊂ lin F be the dual
cone with respect to the inner product inherited from A.
Since F ⊆ A+ = A∗+ , for ω ∈ F we have hω, ϕi ≥ 0 for all
ϕ ∈ F , and so ω ∈ F ∗ . This proves that F ⊆ F ∗ . To see
the converse inclusion, let e be any normalized element
of F ∗ (i.e. huA , ei = 1) that generates an exposed ray
of F ∗ . This means there exists ω ∈ F (which we may
choose normalized) with he, ωi = 0 such that f ∈P
F ∗ and
hf, ωi = 0 implies f = λe with λ ∈ R. But ω = i λi ωi
for some frame ω1 , . . . , ωk ∈ F and λi > 0. Since ω is
in the face {ϕ ∈ F | he, ϕi = 0} ( F , we have k < |F |,
and extending to a frame ω1 , . . . , ωk , . . . , ω|F | on F gives
ω|F | ∈ F ⊆ F ∗ as well as hω|F | , ωi = 0, hence e = ω|F | ∈
F . Since the exposed rays generate F ∗ , this proves that
F∗ ⊆ F.
The properties that we have proven so far turn out
to give an interesting structure known from the field of
quantum logic, indeed sometimes taken as a definition of
a quantum logic [52]. As noted above, the set of faces ordered by subset inclusion is a bounded lattice. However,
from Postulates 1 and 2, we recover more of the logical
structure of quantum theory:

equivalent to the property of perfection mentioned in the
proof of Theorem 8. Furthermore, in [19] it is shown
that orthomodularity of the face lattice, according to
an orthocomplementation which agrees with ours in case
Postulates 1 and 2 hold, follows from a property called
projectivity. In the next section we will define projectivity and establish that state spaces satisfying Postulates
1 and 2 are projective, giving us an alternative proof of
orthomodularity. Here, we proceed with the direct proof.
Proof. Constructing F 0 as the face generated by the
extension of a frame generating F shows easily that
(F 0 )0 = F (as already shown in Proposition 7), and that
F ⊆ G implies F 0 ⊇ G0 , as well as F ∨ F 0 = 1 ≡ A+
and F ∧ F 0 ≡ 0 ≡ {0}. These properties mean that the
operation 0 is an orthocomplementation on the lattice of
faces. It remains to show that this orthocomplemented
lattice satisfies the orthomodular law, Eq. (1). To this
end, assume F ⊆ G, and let ω1 , . . . , ω|F | be a frame on
F . Extend this to a frame on G, and further extend
the result to a frame on A+ , yielding ω1 , . . . , ωN . Then
ω|F |+1 , . . . , ω|G| is a frame on G∩F 0 ; if it did not generate
G ∩ F 0 , it could be extended in G ∩ F 0 , and to this extension we could append ω1 , . . . , ω|F | to obtain a frame of
size larger than |G| in G, which is a contradiction. Hence
H := G∩F 0 is generated by ω|F |+1 , . . . , ω|G| . Since F ∨H
is the smallest face containing F and H, it is the smallest
face containing ω1 , . . . , ω|G| , hence equal to G.
Systems that satisfy Postulates 1 and 2 are operationally close to quantum theory also with respect to
their contextuality behavior: they satisfy the principle of
consistent exclusivity [54], the single-system generalization of the recently introduced postulate of local orthogonality [55]. This is also called Specker’s Principle [57],
and comes in slightly different versions, depending on assumptions of the validity of the principle in situations
where one has more than one copy of a state. Here we
are interested in the single-system version that is called
CE1 in [54].
In order to talk about contextuality, we need a notion
of “sharp measurements”: the analogs of projective measurements in quantum theory. Following [58], we call an
effect 0 ≤ e ≤ uA sharp if it can be written as a sum of
normalized ray-extremal effects; that is, if there are pure
states ω1 , . . . , ωn such that
e=

n
X

ωi ,

i=1

(1)

and if an analogous decomposition exists for uA −e. This
definition does not assume that the ωi are mutually orthogonal; however, they have to be as a consequence of
Postulates 1 and 2. To see this, note that for all j
X
1 = huA , ωj i ≥ he, ωj i = 1 +
hωi , ωj i,
| {z }
i6=j

Note that in [33] it is shown that for self-dual cones, orthomodularity of the face lattice in the above sense is

hence hωi , ωj i = 0 for all i 6= j. The corresponding effects
e can also be characterized in two further ways, namely

Theorem 9. Postulates 1 and 2 imply that the lattice of
faces of A+ is an orthomodular lattice.
Before giving the proof, recall that orthomodularity is
the property that
F ⊆ G ⇒ G = F ∨ (G ∧ F 0 ).

≥0

<!-- page 9 -->
9
as projective units and as the extremal points of the unit
order interval, giving further weight to the interpretation
as the analogue of orthogonal projectors in quantum theory. This is the content of the next lemma. We start with
a definition.
Definition 10 (Projective units). Let A be any system
satisfying Postulates 1 and 2. Then, for every face F of
A+ , define the projective unit uF as
uF := PF uA ,
where PF is the orthogonal projection onto the linear span
of F . A projective unit uF is called atomic if |F | = 1.
This is now used in the following lemma:
Lemma 11. Let A be any system satisfying Postulates
1 and 2. Then, for every face F of A+ , there is a unique
effect uF with 0 ≤ uF ≤ uA such that uF (ω) = 1 for
every ω ∈ F ∩ ΩA , and uF (ϕ) = 0 for all ϕ ∈ F 0 ∩
ΩA , namely the projective unit from Definition 10. If
ω1 , . . . , ω|F | is any frame that generates F , then
uF =

|F |
X

ωi .

(2)

i=1

Furthermore, every effect e ∈ A+ with 0 ≤ e ≤ uA is
a convex combination of projective units, and we have
uF + uG ≤ uA if and only if F ⊥ G, in which case
uF + uG = uF ∨G .
Proof. As in Definition 10, set uF := PF uA . Due to
Theorem 8, uF ∈ A+ . Thus, ω ∈ F implies
huF , ωi = hPF uA , ωi = huA , PF ωi = huA , ωi = 1.
If ϕ ∈ F 0 , then PF ϕ = 0, and an analogous computation
shows that huF , ϕi = 0. Set µF := uF /huA , uF i, then
µF ∈ F ∩ ΩA , and so there is a frame ω1 , . . . , ω|F | of F
P|F |
P
such that µF = i=1 λi ωi with λi ≥ 0, i λi = 1. For
every j = 1, . . . , |F |, we have ωj ∈ F , and so
1 = huF , ωj i = huA , uF i

|F |
X

P|A |
decomposition e = i=1+ λi ωi , where ωi ∈ ΩA are mutually orthogonal pure states, and 0 ≤ λi ≤ 1. Thus, the
vector λ := (λ1 , . . . , λ|A+ | ) is an element of the |A+ |dimensional unit cube, and can thus be written as a
convex combination of extremal points of the (convex)
cube, corresponding to vectors µ = (µ1 , . . . , µ|A+ | ) where
all µi ∈ {0, 1}. Hence e can correspondingly be deP|A |
composed into effects of the form i=1+ µi ωi , which are
projective units. This also shows that the uF are the
unique effects with the properties stated in the lemma.
If F ⊥ G then uF + uG = uF ∨G ≤ uA is clear from
the sum representation of projective units; conversely,
if uF + uG ≤ uA , then uF + uF 0 = uA implies that
uF + uG ≤ uF + uF 0 , and so uG ≤ uF 0 . Thus, if
ω ∈ G ∩ ΩA , then 1 = huG , ωi ≤ huF 0 , ωi ≤ 1, and so
0 = huA − uF 0 , ωi = huF , ωi = hPF uA , ωi = huA , PF ωi,
which implies that PF ω = 0 and ω ⊥ F . Hence
F ⊥ G.
Following the definition of [58], expressed in the language of [54], every system satisfying Postulates 1 and
2 defines a contextuality scenario given by a hypergraph
H, where the vertices of H are the projective units uF
(F 6= {0} any face of A+ ), and
Pn the edges are collections
of effects uF1 , . . . , uFn with i=1 uFi = uA . These edges
describe contexts, i.e. sharp measurements (given by sets
of projective units) that are compatible (i.e. jointly measurable).
Theorem 12. Any system satisfying Postulates 1 and 2
also satisfies the principle of Consistent Exclusivity CE1
as given in [54, Def. 7.1.1] and [59].
Proof. We have to show the following: if I is any set
of vertices of the hypergraph H such thatP
every two elements of I belong to a common edge, then e∈I e(ω) ≤ 1
for all ω ∈ Ω. In the context of Postulates 1 and 2, I is
then a set of projective units I = {uF1 , . . . , uFn } such
that uFi + uFj ≤ u for i 6= j. But Lemma 11 implies that
Fi ⊥ Fj . So if Fi is any frame for FiS
, then Fi ⊥ Fj for
i 6= j, hence the disjoint union F := i Fi is a frame on
A+ , generating some face F . Thus

λi hωi , ωj i = λj huA , uF i,

i=1

so all λj are equal to huA , uF i−1 , proving that there exists
some frame ω1 , . . . , ω|F | with decomposition (2) of uF ,
and showing the inequality 0 ≤ uF ≤ uA . If ϕ1 , . . . , ϕ|F |
is any other frame on F , then there exists a reversible
transformation T with T ωi = ϕi . Since both frames
generate F , T must preserve the face F (and also its
orthogonal complement because T is orthogonal). Hence
uF + uF 0 = uA = T uA = T uF + T uF 0 .
P|F |
P|F |
Thus uF = T uF = T i=1 ωi = i=1 ϕi , proving that
uF can be decomposed into any frame in the claimed
way. If 0 ≤ e ≤ uA is any effect, then it has a frame

X
e∈I

e(ω) =

n
X

huFi , ωi =

i=1

n X
X

he, ωi = huF , ωi ≤ 1.

i=1 e∈Fi

This proves the claim.
As mentioned in Section I, the classification of the
set of all state spaces that satisfy Postulates 1 and 2
remains an open problem with interesting physical and
mathematical implications. Now we show that one additional assumption brings us into the realm of Jordan
algebra state spaces. Before postulating the absence
of third-order interference, we study another postulate
which turns out to be equivalent in our context.

<!-- page 10 -->
10
IV. JORDAN SYSTEMS FROM POSTULATES
1+2 AND PURITY PRESERVATION BY FILTERS

In this section, we show that a system satisfying Postulates 1 and 2 and a third postulate, that the positive
projections of Theorem 8 take pure states to multiples
of pure states, is either an irreducible Jordan algebraic
system or classical.
Jordan algebras were introduced around 1932 by Pascual Jordan [1], as a potentially useful algebraic abstraction of the space of observables, i.e. Hermitian operators
on a Hilbert space, in the newly minted quantum theory. Since the usual matrix or operator multiplication
does not preserve Hermiticity, its physical significance
was unclear; Jordan focused on abstracting properties of
the symmetrized product A • B := (AB + BA)/2 which
does preserve Hermiticity. Like the space of Hermitian
operators, a Jordan algebra (as initially defined by Jordan and studied by him, von Neumann, and Wigner) is
a real vector space, closed under a commutative bilinear
product •. Since the symmetrized product of Hermitian
operators is not associative but does satisfy the special
case (a2 • b) • a = a2 • (b • a) (where a2 := a • a) of
associativity, a Jordan algebra is not assumed associative, but only to satisfy this special case, the “Jordan
property”. For a finite-dimensional Jordan algebra A,
at least, the squares (elements of the form a2 for some
a ∈ A) form a closed cone of full dimension. Jordan,
von Neumann, and Wigner investigated the formally real
finite-dimensional Jordan algebras, which are precisely
those whose cones of squares are pointed. Like the quantum observables, formally real Jordan algebras have a
well-behaved spectral theory (see [11, Sec. III.1]), with
real spectra and an associated real-valued trace function.3 In these algebras, squares have nonnegative spectra, and the unit-trace squares form a closed compact
convex set as required to be the normalized state space
of a system in our context. As mentioned in the introduction, the finite-dimensional formally real Jordan algebras
are already quite close to quantum theory: besides standard quantum theory over the complex numbers they are
quantum-like systems over the reals and over the quaternions, systems whose state spaces are balls (“spin factors”) and what can be thought of as three-dimensional
quantum theory over the octonions [13]. They are also of
interest because they are precisely the finite-dimensional
systems whose cones of unnormalized states are self-dual
and homogeneous [2, 3].
The key tools we will use to establish the main result
of this section are Theorem 8 and a characterization of
the state spaces of certain Jordan algebras by Alfsen and
Shultz [19, Thm. 9.33], first published in [20]. To state
this result requires introducing several somewhat techni-

3 In finite dimensions, formal reality coincides with the notion of

Euclideanity, used in the references [11] and [19].

cal notions, which are, however, of considerable physical
interest in their own right. These are the notions of a
filter on the state space A (and its dual, the notion of a
compression on the effect space A∗ ), with its associated
notion of a projective state space, and the property of
symmetry of transition probabilities.
We first define filters, and begin by introducing some
notions used in that definition.
Definition 13. Let A be any state space with cone A+ .
Projections are linear operators P : A → A with P 2 = P ;
they are positive if P (A+ ) ⊆ A+ . Positive projections P
and Q are called complementary if im+ P = ker+ Q and
vice versa, where im+ P := im P ∩ A+ and ker+ Q :=
ker Q ∩ A+ . A positive projection P is complemented if
there exists a positive projection Q such that P and Q
are complementary.
Definition 14 (Filters and projectivity). A filter is a
positive linear projection P : A → A which (i) is complemented, (ii) has a complemented dual P ∗ , and (iii)
is normalized, i.e. satisfies uA (P ω) ≤ uA (ω) for all
ω ∈ A+ . 4
The state space A is called projective if every face of
A+ is the positive part, im+ P , of the image of a filter P .
We define filters in order to make use of the results
in [19], but they are also of great interest in their own
right. Actually Alfsen and Shultz define [19, Def. 7.22]
compressions, acting on the effect space A∗ . The finitedimensional specialization of Alfsen and Shultz’ notion
of compression is just a positive projection Q : A∗ →
A∗ which is complemented, whose dual is complemented,
and whose dual is normalized; it is obvious that a linear
map Q : A∗ → A∗ is a compression iff Q∗ : A → A is a
filter, and similarly P is a filter iff P ∗ is a compression.
We defined filters because we are most interested in the
transformations that act on the state space A. In fact, in
the context of Postulates 1 and 2 with A and A∗ being
identified via an appropriate self-dualizing inner product,
filters and compressions are represented by precisely the
same linear operators.
As described above, in standard quantum theory the
face associated with a subspace S of Hilbert space consists of the density matrices whose support is contained
in S. Quantum state spaces are projective: there is a
filter onto each face, namely the linear map ρ 7→ PS ρPS ,

4 This condition is equivalent to base norm contractiveness, which

is what Alfsen and Shultz use in their definition. In the Appendix to [19], item A24, they define, for ω, σ ∈ V+ , V a base
norm space, ω ⊥ σ by ||ω−σ|| = ||ω||+||σ||. A26 states that each
ρ ∈ V can be decomposed as a difference of two orthogonal positive components, i.e. there are ω, σ ∈ V+ such that ω ⊥ σ and
ρ = ω − σ. From this we can see that base-norm contractiveness
(||T ρ|| ≤ ||ρ||) of a map T on V+ implies contractiveness everywhere. Since kωk = uA (ω) for all ω ∈ V+ , we have equivalence
of base norm contractiveness and normalization of filters.

<!-- page 11 -->
11
where PS is the orthogonal projector onto S. The complementary projection is ρ 7→ PS ⊥ ρPS ⊥ .
One of several reasons that filters are of great interest
for physics and information-processing is that they share
with the maps ρ 7→ P ρP the property of neutrality [19,
Def. 7.19]: if a state ω ∈ Ω “passes the filter with probability 1”, i.e. uA (P ω) = uA (ω), then it “passes the filter
undisturbed”, i.e. P ω = ω. (This is immediate from
Definition 7.19, Proposition 7.21, and Definition 7.22 of
[19].)
We now turn to symmetry of transition probabilities, a
notion which is defined for systems which are projective
in the sense of Definition 14.
Observe that in a projective system, for each atomic
projective unit p, which is associated [19, Prop. 7.28] with
a unique filter P for which P ∗ u = p, the associated face
{x | p(x) = 1} of Ω contains a single pure state. Call
this state p̂. The map p 7→ p̂ is a one-to-one map from
the set of atoms of the lattice of projective units onto the
set of extremal points of Ω. The system is said to satisfy
symmetry of transition probabilities [19, Def. 9.2 (iii)] if
for all pairs a, b of atoms of the lattice of projective units,
a(b̂) = b(â).
Lemma 15. If a system satisfies Postulates 1 and 2, it
satisfies symmetry of transition probabilities.
Proof. In the context of Postulates 1 and 2, atomic projective units are uF for |F | = 1, where F is generated by a
pure state (frame of size 1) ω1 , such that uF (ϕ) = hω1 , ϕi
according to Lemma 11, so ûF = ω1 = uF in the notation
just introduced. Thus a(b̂) = hâ, b̂i = hb̂, âi = b(â).
We can now state a version of a theorem from [19] that
we will use in proving the main result of this section.
One of the conditions in this theorem will be important
in its own right in what follows, and we therefore call it
Postulate 3 0 .
Theorem 16. Let a finite-dimensional system A+ satisfy
(a) projectivity,
(b) symmetry of transition probabilities, and
(c) Postulate 30 : filters P preserve purity. That is, if
ω is a pure state, then P ω is a nonnegative multiple
of a pure state.
Then A+ is the state space of a formally real Jordan algebra.
The original theorem in [19, 20] is formulated in terms
of compressions, with similar results in finite dimensions
given by Gunson [44] and by Guz [45–47]. Theorem 16
above is an adaptation to our language and to finite dimension, using the notion of filters instead of compressions. The conjunction of (b) and (c) is what Alfsen
and Shultz [19, Def. 9.2] call the “pure state properties”
(their (3)), while their (2) is a technical condition that is
automatically satisfied in finite dimension, and their (1)
follows from our (a).

Theorem 17. In finite dimension, Postulates 1 and 2
imply that the system is projective. Assuming in addition
Postulate 3 0 implies that the system is either irreducible
Jordan-algebraic, or classical.
Proof. In Theorem 8, we have already shown that the orthogonal projection PF onto the linear span of the face
F is positive, for every face F . Now we show that it is
a filter, which establishes that A+ is projective. For any
face F , the corresponding projection PF satisfies im PF =
lin F , im+ PF = F , and ker+ PF = F 0 = F ⊥ ∩ A+ .
So also im+ PF 0 = F 0 and ker+ PF 0 = F 00 = F , and
we see that PF and PF 0 are complements, establishing
property (i) in the definition of filter. Since PF = PF∗ ,
PF has complemented adjoint, property (ii). PF and
PF 0 are positive by Theorem 8. To see property (iii),
i.e. normalization of PF , recall from Lemma 11 that
uA (PF ω) = uF (ω) ≤ uA (ω). Hence for every face F
the projection PF is a filter, so the system is projective.
Projectivity is (a) of Theorem 16. Lemma 15 states
that condition (b) of Theorem 16 follows from Postulates
1 and 2. So (a) and (b) of that theorem follow from
Postulates 1 and 2, whence by the theorem, Postulates 1,
2, and purity preservation by filters imply that a system
is Jordan algebraic.
To see that the only reducible Jordan-algebraic cones
this allows are the classical ones (corresponding to direct sums of the one-dimensional formally real Jordan
algebra), note L
that the cone of a direct sum ofLJordan
n
n
algebras A := i=1 Ai is the direct sum C = i=1 Ci
of their cones. This is because every a ∈ A can then
be written a = (a1 , . . . , an ), and the elements of C are
the squares a2 = (a21 , . . . , a2n ), where the single a2i entries
range over all of Ci . Suppose one of the summands, say
Cj , is not one-dimensional. The face generated by two
ray-extremal points, ωj ∈ Cj and ωk ∈ Ck , with k 6= j,
is a direct sum of one-dimensional cones, i.e. a classical
bit. Since Cj is irreducible and not one-dimensional, it is
not classical, so it contains perfectly distinguishable pure
states ωj and ωi that generate a face that is not a direct
sum. Since we have another rank-2 face that is a direct
sum, in light of Proposition 2 this violates Postulate 2.
Hence either the cone is irreducible, or all summands are
one-dimensional (i.e. it is classical).
The following proposition will be needed later.
Proposition 18. Assume Postulates 1 and 2. Then, to
every face F1 of A+ with complementary face F2 ≡ F10
and corresponding projections P1 and P2 , the space A has
an orthogonal decomposition
A = A1 ⊕ A2 ⊕ Ac12 ,
where Ai := im Pi , Ac12 := ker P1 ∩ ker P2 .
Proof. By construction, A1 = lin F1 ⊥ lin F10 = A2 , and
⊥
by elementary linear algebra, (A1 ⊕ A2 )⊥ = A⊥
1 ∩ A2 =
ker P1 ∩ ker P2 = Ac12 .

<!-- page 12 -->
12
V.

THIRD-ORDER INTERFERENCE

Rafael Sorkin defined a notion of k-th order interference [4], which can be manifested in analogues of the
two-slit experiment involving k or more slits. This notion was adapted to projective convex systems in [16, 17],
and the k = 3 case explored in [18]. Quantum theory exhibits k = 2 interference, but no higher interference. In
this section, we show that Postulates 1 and 2, plus the
assumption of no third-order interference, characterize
irreducible Jordan algebraic systems.
We formalize the assumption of no third-order interference using a mathematical definition of M -slit interference experiment given in terms of experimental probabilities. This is motivated by, and abstracted from, specific
concrete experimental interference experiments such as
those in which a photon passes through physical slits in
a barrier, but the probabilistic definition gives a conceptual account of the notion of interference that applies (as
does the usual quantum-mechanical concept of interference) far more broadly. Consider the setup depicted in
Figure 1; we would like to give a formal description of
the experimental behavior, given that a certain subset of
the slits is open or blocked. First, imagine the case that
all slits are open, and consider the state ω of the particle immediately after it has passed the slit arrangement.
By preparing the particle in different ways, we can obtain different states ω. Part of the state ω contains the
“which-slit information”, encoding through which slit the
particle has just passed the arrangement (possibly in a
probabilistic mixture or generalized superposition). In
an ideal M -slit experiment we would in principle be able
to measure through which slit the particle passes, if we
put suitable detectors behind the slits.
For every slit j ∈ {1, 2, . . . , M }, there should exist
states ω such that the particle is definitely found at slit
j, if measured. In our mathematical setting, this means
that there is a face Fj of the state space, such that all
states ω ∈ Fj give unit probability for the “yes”-outcome
of the two-outcome measurement “is the particle at slit
j”? Moreover, the slits should be perfectly distinguishable – if a particle is definitely at slit j, then it is definitely
not at slit i for all i 6= j. Mathematically, this means that
Fi ⊥ Fj for i 6= j.
We can also ask coarse-grained questions like “Is the
particle found among slits 1 and 2 (rather than somewhere else)? The set of those states ω that give unit
probability for the “yes”-outcome must contain both F1
and F2 ; therefore, it must contain F1 ∨ F2 , the smallest face of the state space that contains both F1 and F2
as subsets. Furthermore, it should be the smallest such
face, since we do not want to include further possibilities.
Thus, this set will be F12 := F1 ∨ F2 . More generally, for
every subset
of slits J ⊆ {1, 2, . . . , M }, we have a face
W
FJ = j∈J Fj , containing those states that describe a
particle that will definitely be found to be somewhere
among the slits in J if the corresponding effect is measured. If the setup is “complete” in the sense that every

particle must definitely be found at one of the slits if
measured, the face F12...M must be the full state space.
Now imagine an additional detector following the slit
arrangement, as depicted in Figure 1. It may click or
not click; the probability to click in the case that all slits
are open is described by some effect e. Suppose we block
all slits, except for a subset J ⊂ {1, . . . , M } of the slits
which are left open. The combination of blockings and
detector defines a new measurement, given by some other
effect eJ , with click probability eJ (ω) if the state right
before the blockings is ω.
If the slits do what we intuitively expect them to do, as
they do to a good approximation in quantum-mechanical
multi-slit experiments, then the click probabilities should
behave as follows. If ω is a state of a particle that would
definitely be found at one of the slits among J, i.e. ω ∈
FJ , then the blockings should have no effect (because
the slits J are all open), and the click probability should
remain the same: eJ (ω) = e(ω). On the other hand,
if the particle would definitely not be found among the
open slits J, i.e. ω ∈ FJ0 , then the particle should be
blocked and there should definitely be no detector click,
and eJ (ω) = 0.
These considerations lead to the following definition,
which abstracts probabilistic properties of an interference
experiment from particular physical realizations involving slits, spatial paths, and so forth. We will soon see
that the orthogonal projections PJ onto the faces FJ are
of paramount importance, which is why we introduce a
name for them as well.
Definition 19 (M -slit experiment). A set W
of effects eJ
and faces FJ , J ⊆ {1, 2, . . . , M }, with FJ = j∈J Fj and
Fi ⊥ Fj for i 6= j is called an M -slit experiment if there
is an effect e ∈ [0, u] such that
• eJ (ω) = e(ω) for all ω ∈ FJ ,
• eJ (ϕ) = 0 for all ϕ ∈ FJ0 .
For any given set of faces with the properties stated above,
the corresponding set of orthogonal projections PJ := PFJ
will be called an M -slit mask. It is called complete if
F12···M = ΩA , that is, if P12···M = 1.
Such an experiment exhibits second-order interference
(say, for M = 2) if the overall interference pattern e12 (ω)
fails to be the sum of the one-slit patterns e1 (ω), e2 (ω).
If it exhibits second-order interference, it may in addition
exhibit irreducibly third-order interference. Third-order
interference occurs if the overall pattern e123 (ω) fails to
be the sum of the double-slit patterns eij (ω), corrected
for overcounting by subtracting suitable multiples of the
single-slit patterns
P ei (ω). Unless otherwise specified
P P we
use the notation i<j to mean the double sum i j>i .
Definition 20 (Third-order interference). We say that a
state space exhibits third-order interference if there exists
an M -slit experiment (for some M ≥ 3) and a state ω

<!-- page 13 -->
13
such that
e12...M (ω) 6=

X

eij (ω) − (M − 2)

X

i<j

ei (ω).

(3)

i

In particular, for M = 3, the condition is
e123 (ω) 6= e12 (ω)+e13 (ω)+e23 (ω)−e1 (ω)−e2 (ω)−e3 (ω).
The second term in (3) corrects for the overlaps of the
sets {i, j} as each index occurs M − 1 times in pairs i <
j. Sorkin’s [4] original definition, and the discussion in
[17, 18], used the M = 3 case as their definition of thirdorder interference, but the two can straightforwardly if
somewhat tediously be shown to be equivalent. Sorkin
showed that if a scenario lacks k-th order interference, it
cannot have l-th order interference for any l > k.
With the previous definition, we can give a concise
formal statement of Postulate 3:
Postulate 3. State spaces do not exhibit third-order interference, as introduced in Definition 20.
Now we show that M -slit experiments are closely related to the positive orthogonal projections introduced
in Theorem 8.
Proposition 21. Assume Postulates 1 and 2. Then,
given any M -slit experiment with effects e, eJ , we have
eJ = PJ e, where the PJ are the elements of the corresponding M -slit mask. Conversely, W
given any set of faces
FJ , J ⊆ {1, 2, . . . , M }, with FJ = j∈J Fj and Fi ⊥ Fj
for i 6= j and any effect e, the set of effects eJ := PJ e
defines an M -slit experiment.
Proof. Since he − eJ , ωi = 0 for all ω ∈ FJ , we have
e−eJ ∈ FJ⊥ (not necessarily in FJ0 , because we do not yet
know whether e − eJ is positive). Similarly, heJ , ϕi = 0
for all ϕ ∈ FJ0 and eJ ≥ 0 implies that eJ ∈ FJ . Thus
PJ e = PJ (eJ + (e − eJ )) = eJ .
The converse can be checked by direct calculation.
According to this proposition, absence of third-order
interference can be expressed in terms of the orthogonal
projections only:
Lemma 22. Consider a state space satisfying Postulates
1 and 2. It has no third-order interference if and only if
for any M -slit mask PJ , J ⊆ {1, . . . , M }, it holds that
X
X
P12···M =
Pij − (M − 2)
Pi .
(4)
i<j

i

Proof. We have absence of third-order interference if for
any choice of faces (as described in the statement of the
lemma) and choice of effect e as well as state ω, (3) holds
with equality. Since the states span the space, this is
equivalent to the statement
X
X
e12...M =
eij − (M − 2)
ei ,
i<j

i

and, due to Proposition 21, to
X
X
P12...M e =
Pij e − (M − 2)
Pi e.
i<j

i

As this must hold for all effects e, and the effects span
the space, we obtain the statement of the lemma.
Now we are ready to prove one of our main results
about the absence of third-order interference together
with Postulates 1 and 2:
Theorem 23. A system satisfies Postulates 1, 2 and
3 if and only if it is an irreducible Jordan system or a
classical system.
Proof. We begin with the “if” direction: irreducible Jordan systems and classical systems satisfy Postulates 1, 2
and 3. For classical systems it is well-known and easy to
see that Postulates 1 and 2 are satisfied: indeed, finitedimensional classical state spaces Ω are often defined as
those for which every state has a unique decomposition
into extremal points, and in this case Postulate 2 follows
from the fact that any permutation of the extreme points
in this unique maximal frame is an affine automorphism
of Ω. Classical systems do not even have 2nd-order interference [4] (the first level that is actually interference),
so they cannot have any higher order of interference. It
follows directly from a fairly standard orthogonal decomposition in formally real Jordan algebras (see e.g. [11])
that finite-dimensional Jordan systems satisfy Postulate
1; and it is also well-known that the Jordan algebra automorphisms are affine automorphisms of the normalized
state space, and act transitively on the set of ordered sets
of orthogonal extremal states in the irreducible case [11].
In Proposition 29 below, we show that in the context of
Postulates 1 and 2, absence of third-order interference
is equivalent to the property that filters preserve purity
of states. Since the latter property is well-known for a
class of Jordan systems including the finite-dimensional
ones [19, Thm. 9.38], this shows that they also satisfy
Postulate 3.
The “only if” direction is an immediate consequence
of Proposition 29—to be proved in the remainder of this
section—which states that the absence of third-order interference implies that all filters preserve purity, together
with Theorem 17, which states that Postulates 1, 2, and
purity-preservation by filters imply that systems are irreducible Jordan, or classical.
We could have defined an M -slit experiment directly
in terms of the positive projections PJ onto the faces.
These describe the action of the slits on the state. However, referring to the corresponding effects eJ in Definition 19 has the advantage that we know for sure that
the effects can be implemented (due to Proposition 1).
On the other hand, there is no analogous statement that
guarantees that the projections PJ themselves can actually be implemented as physical transformations. Thus,
not referring to positive projections in the definition of

<!-- page 14 -->
14
an M -slit experiment means that we make fewer assumptions.
The proof of the crucial Proposition 29 proceeds via
several other propositions and lemmas. The following
property is also mentioned in [16] and [18].
Lemma 24. It follows from Postulates 1 and 2 that
PJ PK = PJ∩K for any M -slit mask.
Proof. First note that if F , G and H are faces such that
F ⊥ H and G ⊥ H, then (F ∨ G) ⊥ H. This is because
(F ∨ G) ∩ H ⊥ is a face which contains F and G, and is
also a subset of F ∨ G, hence equal to F ∨ G.
Defining the projective units uj := uP
Fj and uJ := uFJ ,
it follows from Lemma 11 that uK = k∈K uk . Hence
X
X
uK =
uk +
ul .
k∈K∩J

l∈K\J

For j ∈ J and l ∈ K \ J we have Fj ⊥ Fl , thus FJ =
∨j∈J Fj ⊥ Fl , and so PJ ul = 0. On the other hand, if
k ∈ K ∩ J then PJ uk = uk , so
X
X
PJ uK =
uk ≤
uk = uK .
k∈K∩J

k∈K

According to [19, Prop. 7.39], this implies that PJ PK =
PK PJ , which in turn implies [19, Thm. 8.3] that PJ PK =
PJ ∧ PK = PJ∩K .
The next proposition uses the decomposition described
in Proposition 18 to derive a similar decomposition corresponding to a complete M -slit mask.
Proposition 25. Let Pi with i ∈ {1, ..., m} be a complete
M -slit mask on a system A satisfying Postulates 1 and
2. Then there is an orthogonal decomposition
A = ⊕i Ai ⊕i<j Acij ⊕ A(3)

(5)

where Ai := im Pi , Acij := ker Pi ∩ ker Pj ∩ im Pij and
T
A(3) := i<j ker Pij .
Proof. Using Proposition 18 and the fact that each face
is itself a system satisfying Postulates 1 and 2, we decompose each im Pij as Ai ⊕ Aj ⊕ Acij . (Note that we still
have Acij orthogonal to Ai ⊕ Aj because it is contained
in ker Pi ∩ ker Pj .) For k, l ∈
/ {i, j} we have Acij ⊥ Ackl ,
since im Pij ⊥ im Pkl . Furthermore, for i 6= k, Acij ⊥ Acjk ,
because for x ∈ Acij , y ∈ Acjk
hx, yi = hPij x, Pjk yi
= hx, Pij Pjk yi = hx, Pj yi = 0 ,
where the first equality follows from x ∈ im Pij , y ∈
im Pjk due to the definitions of Acij , Acjk , the last equality from y ∈ ker Pj due to the definition of Acjk , and
the second last equality from
T Lemma 24. Now we just
have to show that A(3) := i<j ker Pij is the orthogonal
complement of ⊕i Ai ⊕i<j Acij . Since ⊕i Ai ⊕i<j Acij =
S
T
lin{ i<j im Pij }, (⊕i Ai ⊕i<j Acij )⊥ = i<j ker Pij , and
we are done.

It is interesting to note that the pairwise intersections ker Pi ∩ ker Pi0 represent “coherences” associated
with the two-slit experiment Pi , Pi0 [18], and that intersecting this with im Pij gives the part associated with
the two-slit experiment Pi , Pj . As an example, consider a quantum 3-level system with orthonormal basis
{|ii}i=1,2,3 , and let i = 1, j = 2 so we have positive projections Pi = P1 : ρ 7→ πρπ with π = |1ih1|, as well as
Pi0 = P10 : ρ 7→ π 0 ρπ 0 , where π 0 = |2ih2| + |3ih3|. The action of these on a 3 × 3 density matrix ρ is to set specific
entries of the matrix to zero. More
explicitly, kerP1 is the

0 • •
set of Hermitian matrices of the form  • • • , where
• • •
• denotes an arbitrary entry. The •’s correspond to the
entries set to zero by P1 ; interchanging the •’s with the
0’s would give the form of the matrices in im P1 . Simi0
larly
1 is the set of Hermitian matrices of the form
 ker P
• • •
 • 0 0 . So ker P1 ∩ ker P10 is the set of all Hermitian
• 0 0


0 • •
matrices of the form  • 0 0 . Since Pj = P2 analo• 0 0
gously projects onto the span of |2i, then im P
12
ij ≡ im P
• • 0
is the set of Hermitian matrices of the form  • • 0 ,
0 0 0
and the intersection ker P1 ∩ ker P10 ∩ im+ P12 yields the
offdiagonal elements corresponding to the two-slit experiment Pi ,Pj as claimed,
i.e. the Hermitian matrices of

0 • 0
the form  • 0 0 .
0 0 0
The decomposition of Proposition 25 is thus into the
spans of the faces im+ Pi , M (M − 1) spaces associated with interference between these faces, and a further
space, which as the next Proposition shows, is associated
with three-way interference.
Proposition 25 is stated as a decomposition of the vector space A. However, note that every face of A+ (with
group of reversible transformations given by the restriction of those global reversible transformations that preserve that face) is itself a state space satisfying Postulates
1 and 2. Thus, if we have an incomplete M -slit mask with
F := im P12...M and corresponding face F+ := F ∩ A+ ,
we obtain a decomposition
F = ⊕i Fi ⊕i<j Fijc ⊕ F (3) ,

(6)

where Fi = im+ Pi ⊆ F , Fijc = ker Pi ∩ ker Pj ∩ im+ Pij ⊆
T
F , and F (3) = i<j ker Pij ∩ F . This is used in the
following proposition.
Proposition 26. Let A be a state space satisfying Postulates 1 and 2. Then there is no third-order interference on A if and only if for every M -slit mask PJ ,
J ⊂ {1, . . . , M } with M ≥ 2, and every pure state

<!-- page 15 -->
15
ω ∈ im P12...M , the component ω (3) of ω in F (3) in (6) is
zero.
Proof. From Lemma 22, the absence of third order interference is equivalent to
X
X
P12···M x =
Pij x − (M − 2)
Pi x
(7)
i<j

i<j

i

for all pure states ω ∈ F . By Proposition 25 and its
c
c
consequence (6), Pij ω = Pi ω + Pj ω + ωij
, where ωij
is
c
the component of ω in Fij . So absence of third-order
interference is equivalent to
X
X

c
ω=
Pi ω + Pj ω + ωij
− (M − 2)
Pi ω
i<j

i

P
for all pure states ω ∈ F . Noting that i<j (Pi + Pj )
contains, for each fixed value of k, M − 1 occurrences of
Pk , this becomes:
X
X
X
c
ω = (M − 1)
Pi ω +
ωij
− (M − 2)
Pi ω
=

X

Pi ω +

i

i<j

X

i

i<j

i

for all x ∈ A. However, since Pij = Pij P12···M and Pi =
Pi P12···M , this is equivalent to (7) holding for all x ∈
im P12···M =: F . Since the pure states in F span F , this
is equivalent to
X
X
ω=
Pij ω − (M − 2)
Pi ω

i

impurity) each of the Pij ω is also pure. In other words:
in the absence of third-order interference, if the Pi are
each purity-preserving, so also are the Pij .
Proof of Proposition 28: First we expand ω ∈ F via (6):
X
X
c
ω=
Pi ω +
ωij
+ ω (3) .

i

c
ωij
.

Taking squared norms and using orthogonality of the decomposition, we get
X
X
c 2
||ω (3) ||2 = ||ω||2 −
||Pi ω||2 −
||ωij
|| . (9)
i

i<j

In order to get results about the purity of Pi ω and Pij ω,
c
c
by subto eliminate ωij
we use Pij ω = Pi ω + Pj ω + ωij
2
2
2
c 2
stituting ||ωij || = ||Pij ω|| − ||Pi ω|| − ||Pj ω|| in (9),
obtaining:
||ω||2 −

X

||ω (3) ||2 =
X

||Pi ω||2 +
||Pi ω||2 + ||Pj ω||2 − ||Pij ω||2 .

i

i<j

Since a given k appears (as i or j) in M − 1 of the pairs
i < j, and the last sum in the above expression has a
||Pk ω|| for each such appearance, this becomes
X
X
||ω (3) ||2 = ||ω||2 + (M − 2)
||Pi ω||2 −
||Pij ω||2 .
i
2

i<j

2

Note that ||Pij ω|| = u(Pij ω) − I(Pij ω), so
X
||ω (3) ||2 = ||ω||2 + (M − 2)
kPi ωk2
i

i<j

In other words, ω

(3)

= 0 in F

(3)

+
in (6).

X

I(Pij ω) −

i<j

Definition 27. The impurity I(ω) of any unnormalized
state ω ≥ 0 is defined as:
I(ω) := u(ω)2 − kωk2 .

Proposition 28. Let Pi with i ∈ {1, ..., M } be an M -slit
mask on a system satisfying Postulates 1 and 2. Then for
any state ω ∈ F := im P12...M (not necessarily pure or
normalized)
X
X
||ω (3) ||2 =
I(Pij ω) − I(ω) − (M − 2)
I(Pi ω) , (8)
i

where ω (3) is the component of ω in F (3) in (6).
While we use this equation directly in what follows, its
significance is underlined by noting its immediate corollary: that if ω and each of the Pi ω are pure, and there is
no third-order interference, then (by the nonnegativity of

uij (ω)2 .

(10)

i<j

Using uij = ui + uj ,
X
X

uij (ω)2 =
ui (ω)2 + uj (ω)2 + 2ui (ω)uj (ω) .
i<j

For normalized states ω ∈ Ω, we have u(ω) = 1, and
kωk ≤ 1, with equality if and only if ω is a pure state.
Extending this to the unnormalized states by multiplication ω 7→ λω with λ ≥ 0 shows that I(ω) ≥ 0 for all
ω ≥ 0, with equality if and only if ω is ray-extremal.

i<j

X

i<j

Again using the fact that a P
given
P i appears in M −
P1 of
the pairs i < j, and writing i j6=i in place of 2 i<j ,
this becomes:
X
XX
(M − 1)
ui (ω)2 +
ui (ω)uj (ω)
i

i

j6=i


= (M − 1)

X

ui (ω)2 +

i

X



ui (ω)

i

X

uj (ω) .

j6=i

Now,
since uF (ω) = hPF u, ωi = hu, PF ωi = u(ω) and
P
u
j6=i j (ω) = uF (ω) − ui (ω), we get
X
X
X

uij (ω)2 = (M − 1)
ui (ω)2 +
ui (ω) uF (ω) − ui (ω)
i<j

i
2

i

= uF (ω) + (M − 2)

X

ui (ω)2

i
2

= u(ω) + (M − 2)

X
i

ui (ω)2 .

<!-- page 16 -->
16
Substituting this into (10) and rearranging gives (8).
We will use this result several times in an inductive argument to establish that all filters are purity preserving.
Proposition 29. Let a system A satisfy Postulates 1 and
2. Then it has no third-order interference if and only if
all its filters are purity-preserving.
Proof. Suppose that all filters are purity-preserving.
Then, if Pi , i ∈ {1, . . . , M } is any M -slit mask and ω
is a pure state in im P12...M , we have I(ω) = I(Pi ω) =
I(Pij ω) = 0, and so (8) implies that the component ω (3)
of ω in F (3) in (6) is zero. Then Proposition 26 implies
that there is no third-order interference.
To show the converse direction, note first that it follows
from [19, Prop. 7.28] in the context of Postulates 1 and 2
that all filters are of the form PF for some face F ; thus,
we only have to show that these orthogonal projections
are purity-preserving. Let N be the size of A’s largest
frame. The proof that all filters are purity-preserving will
be inductive on the rank of filters. The base case is rank1 filters, which holds because a rank-one filter projects
the state onto the span of an extremal ray of A+ .
We now prove the induction step, which states that
if for some fixed rank k ≤ N − 1 all filters are puritypreserving, then all filters of rank k + 1 are purity preserving. Suppose filters of rank k are purity-preserving
and consider any mask consisting of a rank-k filter P1 and
N − k rank-1 filters Pi , i ∈ {2, ..., N − k + 1}. Then for
any pure state ω each Pi ω is pure. So with ||ω (3) ||2 = 0
by the absence of third-order interference, (8) becomes:
X
I(Pij ω) = 0 .

VI.

STANDARD QUANTUM THEORY FROM
OBSERVABILITY OF ENERGY

In standard quantum mechanics, we are used to treating the generator of time evolution as an observable: evolution of any closed quantum system with initial state ρ0
is given by
ρ(t) = e−iHt ρ0 eiHt ,
where H = H † is the system’s Hamiltonian. The righthand side, as a one-parameter group acting on ρ, is generated by the superoperator X : ρ 7→ −i[H, ρ], so that
ρ(t) = etX ρ0 . We are used to associating the observable E : ρ 7→ tr(Hρ) with this generator, and call it the
“expectation value of energy”.
It is an interesting question why such an association is
possible – what is the operational relation between E and
X? The following properties characterize this relation:
• If X and X 0 are two different generators, then the
corresponding observables satisfy E 0 6= E. That is,
the observable determines the generator uniquely.
• The observable E is a conserved quantity of the
time evolution generated by X: E(ρ(t)) = E(ρ0 ).
• If time evolution is not trivial (i.e. ρ(t) not constant), then E is also not a trivial observable: there
are at least two states ρ, σ such that E(ρ) 6= E(σ).
• The map X 7→ E is linear – in particular, larger
values of E correspond to “faster” time evolution.

ij

Since impurity is nonnegative, each of the Pij ω is pure
too. So all the Pi ∨ Pj , and in particular the rank-(k + 1)
filters P1 ∨Pi , i ∈ {2, ..., N −k+1}, are purity-preserving.
Since every rank-(k + 1) filter on A has the form P ∨ Q
for some rank-k P and some rank-1 Q orthogonal to P ,
all rank-(k + 1) filters on A are purity-preserving, and
the induction step is established for k ≤ N − 1. Hence
all filters of rank up to N − 1 are purity-preserving.
In the context of assumptions (a) and (b) of Theorem 16, Postulate 30 is known [19, 45] to be equivalent
to another postulate: that the lattice of exposed faces
has the covering property. We say that an element F
of a lattice covers another element G if G is below F
and there is nothing between them. Hence an atom is
an element that covers 0. By definition, a lattice has
the covering property if for every element F and atom a,
either F ∨ a = F or F ∨ a covers F .
In the context of Postulates 1 and 2, the covering property can be formulated as follows: if F is any face of A+ ,
and ω a pure state, then the face G generated by both
has rank |G| ≤ |F | + 1. Since we have shown that (a)
and (b) of Theorem 16 follow from Postulates 1 and 2,
the covering property can replace the absence of third
order interference (or Postulate 30 ).

These properties allow us to define a notion of “observability of energy” for arbitrary probabilistic theories,
which will turn out to be a rather restrictive property.
Definition 30. Let A be any state space with a group
of reversible transformations GA . An energy observable
assignment is an injective linear map φ : gA → A∗ such
that the observable φ(X) is conserved under the time evolution generated by X, but not under all time evolutions
unless X = φ(X) = 0. We say that “energy is observable” on system A if gA 6= {0} and if there exists an
energy observable assignment.
Our fourth postulate is thus
Postulate 4. Energy is observable on every system.
Writing the time evolution starting with initial state
ω0 explicitly as
ω(t) := etX ω0 ,
a conserved quantity E ∈ A∗ is a linear functional with
E(ω(t)) = E(ω0 ). It is easy to check that this is equivalent to E ◦ X = 0, where “◦” is for composition of linear
maps. If E were equal to the order unit, i.e. E = uA ,

<!-- page 17 -->
17
then E(ω(t)) = uA (ω(t)) = 1 for all t and all time evolutions, since all elements of GA preserve the normalization.
Thus, Definition 28 implies the conditions
φ(X) ◦ X = 0 for all X ∈ gA ,
uA 6∈ ran(φ).

group, such that gd = so(d). If Postulate 4 holds, then
there must be an injective linear map φ from the Lie
algebra gd of Gd to Rd+1 . But dim(so(d)) = d(d − 1)/2
which is larger than d + 1 for d ≥ 4, so no such map can
exist for d ≥ 4. If d = 2, we have


Our notion is related to Alfsen and Shultz’s notion of
a “dynamical correspondence” [19], except that they require an injection of observables into dynamical generators, rather than vice versa, and in addition to a conservation condition, impose a condition relating reversible
transformations to general automorphisms of the cone of
states which is formulated in the Jordan-algebraic setting. Our setting is more general, and we impose no
such relation between the reversible transformations and
cone automorphisms. Connes [23] used a notion of orientation related to dynamical correspondence to characterize the state spaces of von Neumann algebras (one
of the infinite-dimensional generalizations of standard
quantum systems) among those of JBW-algebras (one
infinite-dimensional generalization of finite-dimensional
formally real Jordan algebras). Other work making use
of similar notions to characterize quantum and classical
theory in different settings, can be found in [24–27]. References [24], [25], and [26] all derive relations between
energy and observables, and thence that the theory must
essentially be standard quantum or classical, from considerations involving dynamics on composites, so our work
is complementary to theirs in that we avoid assumptions
about composite systems.
The identification of dynamical generators with conserved observables that exists in classical and quantum
theories is central to many physical phenomena and arguments, providing motivation for our postulate. We
mention in particular that standard formulations of the
statistical mechanics underlying thermodynamics use a
conserved energy observable in the definition of free energy.
Our goal is to show the following:
Theorem 31. Postulates 1, 2, 3, and 4 imply that the
state space is an N -level state space of standard complex
quantum theory, for some N ∈ N, and all conjugations
ρ 7→ U ρU † with U ∈ SU(N ) are contained in the group
of reversible transformations.
Proof. We show that complex quantum N -level state
spaces are the only finite-dimensional irreducible formally real Jordan algebra state spaces that have observability of energy. This is enough due to Theorem 23.
First, consider the d-dimensional ball state spaces
(“spin factors”)
Ωd := {(1, r)T | r ∈ Rd , krk ≤ 1}.
(The qubit appears again in this class of systems, since
the d = 3 case is the Bloch ball.) The Lie algebra is nontrivial only for d ≥ 2. Consider the case that the group Gd
of reversible transformations contains the full orthogonal


0 0 0
g2 = R ·  0 0 1  ,
0 −1 0
and calling this matrix X, it is easy to see that φ(X)◦X =
0 implies that φ(X) = c · ud for the normalization functional ud (x1 , x2 , x3 ) = x1 . This contradicts the definition
of an energy observable assignment.
If d is even or d = 7, there are compact connected subgroups of SO(d) that are transitive on the pure states of
Ωd , and thus satisfy Postulate 2, (see Ref. [49] for the
list of groups; they have been classified in [39, 40]). As
we show in Appendix B, all of these cases except for one
can be ruled out by dimension counting, exactly as the
cases d ≥ 4 above; the only case where this does not
work is d = 4 with transformation group G2 = SU(2).
But there, it can be shown that there are time evolutions
which only have the normalization as their conserved observable, contradicting Definition 30.
Now let A be the state space of the 3 × 3 octonionic
matrices. Due to Postulate 2 (in the special case of 1frames), the group of reversible transformations GA acts
transitively on the pure state manifold, which is the Cayley plane P 2 (O), hence so does its connected component
at the identity [50]. According to [22] and [21], the only
compact connected Lie group which acts transitively and
effectively on it is the exceptional Lie group F4 . But
dim(F4 ) = 52 > dim(A) = 27, so there is no injective
linear map from gA to A∗ .
For N ≥ 3, consider the N -level state space AN of
quaternionic quantum mechanics, with any group of reversible transformations GN satisfying Postulate 2. Then
dim(AN ) = 2N 2 − N . The pure states define the quaternionic projective space P N −1 (H), and so GN must act
transitively on it. According to [21], the only possibility
is gN ⊇ sp(N ), and dim(sp(N )) = N (2N + 1), which is
larger than dim(AN ).
The only remaining cases are the N -level state spaces
AN of real quantum mechanics for N ≥ 3, which are
more difficult to rule out – dimension counting does not
work. First, it can be shown from the classification results of [22] that Postulate 2 implies that the group of
reversible transformations contains all maps of the form
ρ 7→ OρOT with O ∈ SO(N ); consequently, every map
X(ρ) := ρ 7→ [M, ρ] with M ∈ so(N ) is a valid generator.
An energy observable assignment φ maps these generators (resp. the matrices M ) to observables (that is, symmetric matrices M̄ ) such that [φ(X)](ρ) = tr(M̄ ρ); the
conservation condition φ(X) ◦ X = 0 becomes [M, M̄ ] =
0. However, as we show in the appendix by considering
certain special generators X, all maps of this kind must
have M̄ = 1 in their range, yielding the normalization

<!-- page 18 -->
18
functional, which contradicts the definition of an energy
observable assignment.
In the standard case of complex N -level quantum theory, it remains to show that the group of reversible transformations GN contains all unitaries (it might also contain anti-unitaries; due to Wigner’s theorem [28, 29],
these are the only possibilities). Postulate 2 implies
transitivity of the connected subgroup of GN on the
pure states, hence on the projective space P N −1 (C);
according to [21], for odd N , the only possibility is
the projective action of SU(N ); but if N is even, say
N = 2n, there is a second possibility, which is the projective action of Sp(N ). But consider two N -frames
|e1 ihe1 |, . . . , |eN i, heN | and |f1 ihf1 |, . . . , |fN i, hfN |, where
e1 , . .. , eN are defining vectors of the basis in which
0 −1
J=
, such that a unitary U is in Sp(N ) if and
1 0
only if U T JU = J. Moreover, suppose that f1 = e1 .
If Postulate 2 is satisfied, there is U ∈ Sp(N ) such
that U |ei ihei |U † = |fi ihfi | for all i, so U e1 = eiϕ e1
for some ϕ ∈ R. Since Je1 = en+1 , it is easy to
see that the symplectic constraint on U , together with
U † en+1 = (U T en+1 ), implies that U en+1 = e−iϕ en+1 ,
so |fn+1 ihfn+1 | = |en+1 ihen+1 |, which contradicts frame
transitivity, i.e. Postulate 2.
The fact that energy observability rules out classical
systems in this theorem is a consequence of our finitedimensional setting, for which classical reversible dynamics are a discrete group. The probabilistic representation
of phase-space classical mechanics involves an infinitedimensional space of Liouville distributions, and does,
of course, have continuously parametrized reversible dynamics.

VII.

DISCUSSION AND CONCLUSIONS

We have given four principles that we argue have, to
various degrees, the virtues of conceptual clarity, important physical implications, intuitive appeal, and interesting experimental consequences. We have shown
that while they are formulated in the setting of an extremely broad class of probabilistically described systems
together they constrain the abstract structure of such a
system to be that of the usual Hilbert space quantum theory over the complex field. Our demonstration was limited to finite dimension, a limitation which we believe to
be primarily technical. This reconstruction of quantum
theory differs interestingly from several previous ones in
avoiding any postulates concerning the structure or even
existence of composite systems.
Another desirable feature of our reconstruction is its
stepwise structure, in which conceptually and often physically significant properties appear even as a consequence
of the first postulate, and additional such properties appear at each step.

Postulates 1 and 2 together further have very strong
consequences: they imply that all effects are allowed,
that every face of the state space is the image of a filter, i.e., that the state space is projective, and also that
it is self-dual. Filters allow one to verify that a state
is in a claimed face of the state space without (if the
claim is true) disturbing the state. They are likely to
be important ingredients of both information-processing
and thermodynamical protocols; possibilities which are
under investigation. Filters can also be used to equip
a system with operations destroying coherence between
any set of mutually orthogonal faces. In other words, the
existence of filters ensures the possibility of a process of
decoherence similar to the one in quantum theory.
Self-duality is another strong property of state spaces
that is independent of projectivity. Self-duality introduces a correspondence between atomic measurement
outcomes and pure states that is exploited in quantum
steering and teleportation, for example. It is also known
to be linked, in some special contexts such as polygonal state spaces, to correlations satisfying the Tsirel’son
bound on violations of Bell locality [62].
The lattice of faces given Postulates 1 and 2 is
orthomodular—as is implied, indeed, by projectivity.
This expresses a kind of “local classicality”, which one
sees also in the topos-theoretic approach of e.g. [61],
and also relates our work to the classic “quantum logic”
approach initiated by Birkhoff and von Neumann [38].
Postulate 2 imposes a high degree of symmetry on this
lattice—it would be interesting to investigate lattices
with such high symmetry using purely lattice-theoretic
methods.
There is a close connection between Postulate 2 and
certain properties of the circuit model for quantum computation. In this model it is standard to start with an
input n−level system in a particular state, as well as a
number of other n−level systems which can without loss
of generality be taken to be in the |0i state. Then we implement the circuit representing the computation we wish
to carry out, and at the end we must measure a specific
observable to determine the (probability of the) output
of the computation. This last measurement step can be
done without loss of generality by first reversibly transforming the (generally entangled) logical n−level system
of interest into an individual physical n−level system,
and then doing the desired measurement on this system
alone. This transfer is possible because quantum theory satisfies Postulate 2. Postulate 1 and 2 together can
be understood as generalizing this idea by demanding
that every state (not just pure ones) of a system can be
transferred to any other system (with the same or larger
number of distinguishable states) by a suitable reversible
interaction, provided both are subsystems of a common
larger system.
Our third postulate provides, in the context set by
the first two postulates, a perhaps surprising link between the absence of irreducibly three-slit interference,
currently under experimental scrutiny, and mathemati-

<!-- page 19 -->
19
cal notions: the Jordan algebraic structure of quantum
theory on the one hand, and the satisfaction of the covering law by its lattice of faces, on the other. In the context
of our first two postulates, these are all equivalent. The
known equivalence (even in the broader context of projective systems) of the latter two with the requirement
that filters preserve purity is further food for thought.
An interesting question is whether the equivalence of no
higher-order interference with either of these two principles still holds in the broader projective context. Looking
to operational consequences, perhaps the failure of purity
preservation might give rise to an extra source of noise
or irreversibility in information processing or thermodynamical protocols—though this might be circumvented if
the protocols are designed so the states being filtered are
“compatible” with the filters.
Most interesting, perhaps, is the possibility that there
exist families of systems satisfying our first two postulates
but not the third: these would still have an extremely regular structure and likely support interesting information
processing, but so far no examples are known. Should
they be shown not to exist, we would then know that
Jordan systems are singled out by Postulates 1 and 2
alone.
The final step, narrowing things down from Jordan
systems to complex quantum systems via energy observability, is not so surprising. Similar postulates have
been used for this purpose by Connes and by Alfsen
and Shultz. We require an injection of dynamical generators into the space of observables, each injected generator conserved by the dynamics it generates, whereas
Alfsen and Shultz require the converse and also impose
ancillary conditions. In contrast, our condition, though
applied only to Jordan algebraic systems, is formulated
in greater generality where the ancillary conditions do
not make sense. It is likely that in the Jordan-algebraic
setting, the ancillary conditions, as well as a bijection,
are obtained automatically. Exploration of conditions of
this type—either ours, or abstractions of Connes’ or Alfsen and Shultz’s—in a broader context are desirable. Indeed, as we have mentioned, others have explored similar
principles, though some of these investigations (e.g. [24],
[25]) have made use of composite systems which appear
to us to be required to satisfy local tomography. In the
context of our Postulates 1 and 2, locally tomographic
composites and the existence of stand-alone 2-level systems would imply that the systems are standard quantum systems; indeed one reason for our interest in energy
observability is as an alternative to local tomography.
The fact that energy observability rules out classical systems in this theorem is an artifact of our finitedimensional setting, for which classical reversible dynamics are a discrete group. Since infinite-dimensional classical systems do have continuous one-parameter groups
of reversible transformations, however, it is important to
point out that there are numerous alternative assumptions which would allow us to rule out classical systems
in the finite-dimensional case without assuming the ex-

istence of continuous reversible dynamics. Such alternatives are likely to retain their usefulness in infinite dimensions. For example, we could postulate the existence of
a tradeoff between information gained in a measurement
and disturbance to the measured state [70], or the existence of at least one state that has two distinct convex
decompositions into pure states, or the existence of interference; the existence of nonclonable or nonbroadcastable
sets of states [36, 37] might also work.
Although we are not aware of work using the set of
postulates we use, several authors have used one or more
related principles. In Wilce’s characterization in [68], a
symmetry principle reminiscent of our Postulate 2 (but
concerning test spaces rather than state spaces) was used,
along with reversible transitivity on pure states (a special case of Postulate 2). In his most recent reconstruction, Hardy [69] uses a postulate (“filters are nonflattening”) which relies on a definition of filters that is
equivalent to ours (at least in the context of our Postulates 1 and 2), and which implies Postulate 30 (that
filters are purity-preserving). Niestegge has also used
the absence of higher-order interference as one ingredient in deriving Jordan algebraic systems [12]. In [17] it
was established that finite-dimensional Jordan systems
do not have higher-order interference, a result also found
by Niestegge in [12].
Dakić and Brukner [43] have used Postulate 1 and
the fact that all pure states are connected by reversible
transformations to derive the ball shape of two-level
state spaces (a fact that carries over to all two-level systems satisfying our Postulates 1 and 2). In their reconstruction of quantum theory, Chiribella, d’Ariano, and
Perinotti [42] have proven several lemmas that are close
to some of ours (such as statements on positive projections, or a sum representation of projective units), but
obtained them from different assumptions. We have already mentioned other work postulating connections between observables and dynamical generators. More work
understanding the connections between the various approaches would likely be fruitful.
Besides providing an understanding of the Hilbert
space structure of quantum theory from first principles,
our reconstruction suggests a variety of open questions,
such as the existence of systems with strong symmetry
and classical decomposability, but also with higher-order
interference. Furthermore, we think that the naturalness
of our postulates allows us to make closer contact with
other aspects of physics, a direction we consider important to pursue.
This is evident from the postulates themselves – Postulate 3 considers a property that is under direct experimental investigation, and so solving the aforementioned
open problem might provide concrete consistent models
that can be tested against quantum theory in experiments. Postulate 4 relates the probabilistic structure to
the existence of a notion of energy of the form physicists
are used to. Furthermore, consequences of the postulates
– such as projectivity – seem crucial for thermodynamic

<!-- page 20 -->
20
reasoning. In fact, weaker versions of Postulates 1 and
2, in conjunction with local tomography, are enough to
make sense of the general-probabilistic thermodynamics
results in [73, 74].
In this sense, our result is part of a broader research
program: analyze the structure of physics – that is, the
way that the different parts of physics fit together – by
rigorously assessing the consequences of changing some
of its parts. One part of physics is quantum theory,
and seeing how a more general probabilistic theory could
still harmonize with thermodynamics or Hamiltonian mechanics is one of many ways to gain insights into the way
our world works. Given the current quest for a theory
that unifies quantum and gravitational physics, in a situation where conclusive experimental results are mostly
absent, it seems particularly promising to rigorously analyze the logical and conceptual structure of what is
known, hoping thereby to glimpse a path towards the
unknown.

Some of this work was done while the authors were
employed by or visiting the Perimeter Institute for Theoretical Physics, Waterloo, Ontario, Canada. Research
at Perimeter Institute is supported in part by the Government of Canada through NSERC and by the Province
of Ontario through MRI. Also, part of the work was done
while HB was a Fellow of the Stellenbosch Institute for
Advanced Studies at the Wallenberg Research Center at
Stellenbosch University, in 2012. Furthermore, we would
like to thank two anonymous referees for the thorough review of the manuscript and for helpful suggestions, and
one in particular for pointing out a mistake in an earlier
version of Proposition 1 and for suggesting how to fix it.

[1] P. Jordan, Über eine Klasse nichtassoziativer hyperkomplex Algebren, Nachrichten von der Gesellschaft
der Wissenschaften zu Göttingen, MathematischPhysikalische Klasse (1933) 569-575. Available digitally
at http://www.digizeitschriften.de/dms/toc
/?PPN=PPN252457811 1933.
[2] M. Koecher, Die Geodätischen von Positivitätsbereichen,
Math. Annalen 135 (1958) 192-202.
[3] E. B. Vinberg, Homogeneous cones, Dokl. Acad. Nauk.
SSSR 141 (1960) 270-273; English trans. Soviet Math.
Dokl. 2, 1416-1619 (1961).
[4] R. D. Sorkin, Quantum mechanics as quantum measure theory, Mod. Phys. Lett. A 9, 3119–3128 (1994).
arXiv:gr-qc/9401003.
[5] U. Sinha, C. Couteau, T. Jennewein, R. Laflamme,
and G. Weihs, Ruling Out Multi-Order Interference
in Quantum Mechanics, Science 329, 418 (2010).
arXiv:1007.4193.
[6] I. Söllner, B. Gschösser, P. Mai, B. Pressi, Z. Vörös and
G. Weihs, Testing Born’s rule in quantum mechanics for
three mutually exclusive events, Found. Phys. 42, 742–
751 (2012). arXiv:0811.2068.
[7] R. E. George, L. M. Robledo, O. J. E. Maroney, M. S.
Blok, H. Bernien, M. L. Markham, D. J. Twitchen, J. J.
L. Morton, G. A. D. Briggs and R. Hanson, Opening up
three quantum boxes causes classically undetectable wavefunction collapse, Proc. Nat. Acad. Sci. (US) 110, 3777–
3781 (2013). arXiv:1205.2594.
[8] M. F. Pusey, J. Barrett and T. Rudolph, On the reality
of the quantum state, Nature Physics 8, 475–478 (2012).
arXiv:1111.3328.
[9] R. Colbeck and R. Renner, No extension of quantum mechanics can have improved predictive power, Nature Communications 2, 411 (2011). arXiv:1005.5173.
[10] S. Aaronson, Is quantum mechanics an island in theoryspace?, Proceedings of Quantum Theory: Reconsideration of Foundations, ed. A. Khrennikov (Växjö University
Press), 2004. arXiv:quant-ph/0401062.
[11] J. Faraut and A. Korányi, Analysis on Symmetric Cones,

Oxford University Press, 1995.
[12] G. Niestegge, Conditional probability, three-slit experiments and the Jordan structure of quantum mechanics,
Advances in Mathematical Physics 2012, 156573 (2012).
arXiv:0912.0203.
[13] P. Jordan, J. von Neumann, and E. Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. Math. 35, 29–64 (1934).
[14] R. Webster, Convexity, Oxford University Press, New
York, 1994.
[15] D. Gross, M. Müller, R. Colbeck and O. C. O. Dahlsten,
All reversible dynamics in maximally non-local theories are trivial, Phys. Rev. Lett 104, 080402 (2010).
arXiv:0910.1840.
[16] C. Ududec, Perspectives on the Formalism of Quantum
Theory, PhD Thesis, University of Waterloo, 2012. University of Waterloo Library.
[17] C. Ududec, H. Barnum, and J. Emerson, Probabilistic
interference in operational models, in preparation.
[18] C. Ududec, H. Barnum, and J. Emerson, Three slit experiments and the structure of quantum theory, Foundations
of Physics 41, 396–405 (2011). arXiv:0909.4787.
[19] E. M. Alfsen and F. W. Shultz, Geometry of State Spaces
of Operator Algebras, Birkhäuser, Boston, 2003.
[20] E. M. Alfsen and F. W. Shultz, State spaces of Jordan
algebras, Acta Math. 140, 155–190 (1978).
[21] A. L. Onishchik and V. V. Gorbatsevich, Lie groups and
Lie algebras I, Encyclopedia of Mathematical Sciences
20, Springer, 1993.
[22] E. Tsukuda, Transitive actions of compact connected Lie
groups on symmetric spaces, Sci. Rep. Niigata Univ. Ser.
A 15, 1–13 (1978).
[23] A. Connes, Caractérisation des espaces vectoriels ordonnés sous-jacents aux algèbres de von Neumann, Annales de l’Institut Fourier (Grenoble) 24(4), 121–155
(1974)
[24] A. Kapustin, Is quantum mechanics exact?, J. Math.
Phys. 54, 062107 (2013). arXiv:1303.6917.
[25] F. Moldoveanu, Quantum mechanics from invariance

Acknowledgments

<!-- page 21 -->
21
laws, 7th International Workshop DICE2014:Spacetime
- Matter - Quantum Mechanics (Castiglioncello, September 15–19 2014). arXiv:1303.3935.
[26] E. Grgin and A. Petersen, Duality of observables and
generators in classical and quantum mechanics, J. Math.
Phys. 15, 764–769 (1974).
[27] E. Grgin and A. Petersen, Algebraic implications of composability of systems, Commun. Math. Phys. 50, 177–188
(1976).
[28] V. Bargmann, Note on Wigner’s Theorem on Symmetry
Operations, J. Math. Phys. 5, 862–868 (1964).
[29] E. P. Wigner, Normal Form of Antiunitary Operators, J.
Math. Phys. 1, 409–413 (1960).
[30] B. Iochum, Cônes Autopolaires dans les espaces de
Hilbert, Thèse de 3ème cycle, Marseille, 1975.
[31] B. Iochum, Cônes Autopolaires et Algèbres de Jordan,
Springer Verlag, Berlin, Heidelberg, 1984.
[32] M. P. Müller and C. Ududec, Structure of reversible computation determines the self-duality of quantum theory,
Phys. Rev. Lett. 108, 130401 (2012). arxiv:1110.3516.
[33] G. Barker, Perfect cones, Linear Algebra and its Applications 22, 211–221 (1978).
[34] J. Hilgert, K. H. Hofmann, and J. D. Lawson, Lie groups,
convex cones, and semigroups, Oxford, 1998.
[35] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, Teleportation in general probabilistic theories, in Proceedings
of Symposia in Applied Mathematics 70, ed. S. Abramsky and M. Mislove (American Mathematical Society),
25–48, 2012. arxiv:0805.3553.
[36] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, Cloning
and broadcasting in generalized probabilistic models.
arXiv:quant-ph/0611295.
[37] H. Barnum, J. Barrett, M. Leifer, and A. Wilce, A generalized no-broadcasting theorem, Phys. Rev. Lett. 99,
240501 (2007). arXiv:0707.0620.
[38] G. Birkhoff and J. von Neumann, The logic of quantum
mechanics, The Annals of Mathematics 37(4), 823–843
(1936).
[39] D. Montgomery and H. Samelson, Transformation groups
of spheres, Annals of Math. 44, 454–470 (1943).
[40] A. Borel, Some remarks about Lie groups transitive on
spheres and tori, Bull. AMS 55, 580–587 (1949).
[41] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Probabilistic theories with purification, Phys. Rev. A 81,
062348 (2010). arXiv:0908.1583.
[42] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Informational derivation of quantum theory, Phys. Rev. A 84,
012311 (2011). arXiv:1011.6451.
[43] B. Dakić and Č. Brukner, Quantum Theory and Beyond:
Is Entanglement Special?, in “Deep Beauty: Understanding the Quantum World through Mathematical Innovation”, Editor Hans Halvorson (Cambridge Press, 2011).
arXiv:0911.0695.
[44] J. Gunson, On the algebraic structure of quantum mechanics, Commun. Math. Phys. 6(4), 262–285 (1967).
[45] W. Guz, Filter theory and covering law, Annales de
l’institut Henri Poincaré (A) Physique théorique 29, 357–
378 (1978).
[46] W. Guz, Pure operations and the covering law, Reports
on Mathematical Physics 16(1), 125–141 (1979).
[47] W. Guz, Conditional probability in quantum axiomatics, Annales de l’institut Henri Poincaré (A) Physique
théorique 33(1), 63–119 (1980).
[48] L. Hardy, Quantum Theory From Five Reasonable Ax-

ioms, arXiv:quant-ph/0101012.
[49] Ll. Masanes, M. P. Müller, D. Pérez-Garcı́a, and R. Augusiak, Entanglement and the three-dimensionality of the
Bloch ball, arXiv:1111.4060.
[50] Ll. Masanes and M. P. Müller, A derivation of quantum theory from physical requirements, New J. Phys. 13,
063001 (2011). arXiv:1004.1483.
[51] Ll. Masanes, M. P. Müller, R. Augusiak, and D. PérezGarcı́a, Existence of an information unit as a postulate
of quantum theory, Proc. Natl. Acad. Sci. 110(41), 16373
(2013). arXiv:1208.0493.
[52] J. Harding, The Source of the Orthomodular Law, in
Handbook of Quantum Logic, K. Gabbay, D. Gabbay, and
D. Lehmann, eds., Elsevier, 2011.
[53] M. S. Gowda, R. Sznajder, and J. Tao, The automorphism group of a completely positive cone and its Lie
algebra, Linear Algebra and its Applications 438(10),
3862–3871 (2013).
[54] T. Fritz, A. Leverrier, and A. B. Sainz, A Combinatorial Approach to Nonlocality and Contextuality,
arXiv:1212.4084.
[55] T. Fritz, A. B. Sainz, R. Augusiak, J. Bohr Brask, R.
Chaves, A. Leverrier, and A. Acı́n, Local Orthogonality:
a multipartite principle for correlations, Nat. Comm. 4,
3263 (2013). arXiv:1210.3018.
[56] B. Dakić, T. Paterek, and Č. Brukner, Density cubes
and higher-order interference theories, New J. Phys. 16,
023028 (2014). arXiv:1308.2822.
[57] A. Cabello, Specker’s fundamental principle of quantum
mechanics, arXiv:1212.1756.
[58] A. Cabello, S. Severini, and A. Winter, (Non)Contextuality of Physical Theories as an Axiom,
arXiv:1010.2163.
[59] J. Henson, Quantum contextuality from a simple principle?, arXiv:1210.5978.
[60] S. L. Adler, Quaternionic Quantum Mechanics and
Quantum Fields, Oxford University Press, New York,
1995.
[61] C. Isham and J. Butterfield, Some possible roles for topos
theory in quantum theory and quantum gravity, Found.
Phys. 30, 1707–1735 (2000). arXiv:gr-qc/9910005.
[62] P. Janotta, C. Gogolin, J. Barrett and N. Brunner, Limitations on nonlocal correlations from the structure of
the local state space, New J. Phys. 13, 063024 (2011).
arXiv:1012.1215.
[63] P. Janotta and R. Lal, Generalized probabilistic theories
without the no-restriction hypothesis, Phys. Rev. A 87,
052131 (2013). arXiv:1302.2632.
[64] H. Barnum and A. Wilce, Ordered linear spaces
and categories as frameworks for information-processing
characterizations of classical and quantum theory,
arXiv:0908.2354.
[65] H. Barnum, Quantum information processing, operational quantum logic, convexity and the foundations of
physics, Studies in the History and Philosophy of Modern
Physics 34, 343-379 (2003). arXiv:quant-ph/0304159.
[66] A. J. Short and S. Wehner, Entropy in general
physical theories, New J. Phys. 12, 033023 (2010).
arXiv:0909.4801.
[67] H. Barnum, J. Barrett, L. Clark, M. Leifer, R. W.
Spekkens, N. Stepanik, A. Wilce, and R. Wilke, Entropy and information causality in general probabilistic
theories, (Addendum, New J. Phys. 12, 129401 (2012)).
arXiv:0909.5075.

<!-- page 22 -->
22
[68] A. Wilce, Four and a half axioms for finite-dimensional
quantum theory, in Y. Ben-Menahem and M. Hemmo,
eds., Probability in Physics, 292–298, Springer, 2012.
arXiv:0912.5530.
[69] L. Hardy, Reformulating and Reconstructing Quantum
Theory, arXiv:1104.2066.
[70] J. Barrett, Information processing in generalized probabilistic theories, Phys. Rev. A 75, 032304 (2007).
arXiv:quant-ph/0508211.
[71] D. I. Fivel, Derivation of the Rules of Quantum Mechanics from Information-Theoretic Axioms, Found. Phys.
42, 291–318 (2012). arXiv:1010.5300.
[72] E. B. Davies and J. T. Lewis, An Operational Approach
to Quantum Probability, Commun. Math. Phys. 17, 239–
260 (1970).
[73] M. P. Müller, O. C. O. Dahlsten, and V. Vedral, Unifying
typical entanglement and coin tossing: on randomization
in probabilistic theories, Commun. Math. Phys. 316(2),

441–487 (2012). arXiv:1107.6029.
[74] M. P. Müller, J. Oppenheim, and O. C. O. Dahlsten,
The black hole information problem beyond quantum theory, Journal of High Energy Physics 09, 116 (2012).
arXiv:1206.5030.
[75] P. Janotta and H. Hinrichsen, Generalized Probability
Theories: What determines the structure of quantum
physics?, J. Phys. A: Math. Theor. 47, 323001 (2014).
arXiv:1402.6562.
[76] C. Pfister, One simple postulate implies that every polytopic state space is classical, Master thesis, ETH Zurich,
2011. arXiv:1203.5622.
[77] R. D. Sorkin, Impossible Measurements on Quantum
Fields, in “Directions in General Relativity, V 2”, eds.
Bei-Lok Hu and T. A. Jacobson, Cambridge University
Press, 1993.

Appendix A: Perfection and positive projections

In this section, we give a proof of the following proposition which is originally due to Iochum [30, 31].
Proposition 32. Let A+ be a regular self-dual cone in A. A+ is perfect if and only if each orthogonal (with respect
to the self-dualizing inner product) projection PF onto the linear span F of a face F+ , is positive.
Proof. We write F+∗ for the dual of F+ in F , according to the restriction of the self-dualizing inner product for A+ ;
thus perfection means that F+∗ = F+ for every face.
We begin with “only if”. Let P be the orthogonal projector onto F , x ∈ A+ , y ∈ F+ . Now hy, P xi = hP ∗ y, xi;
since P is Hermitian this equals hP y, xi = hy, xi. The latter is nonnegative because both y and x are in A+ , which is
self-dual. So we have shown ∀y ∈ F+ hy, P xi ≥ 0, i.e. P x ∈ F+∗ . But by perfection F+∗ = F+ . Thus P x ∈ F+ for any
x ∈ A+ , i.e. P is positive.
For “if”, we begin by observing that given positivity of P , P A+ = F+ . This is because P x = x for any x ∈ F , so
P F+ = F+ , whence P A+ ⊇ F+ ; on the other hand P A+ ⊆ F+ by positivity.
Note that F+ ⊆ F+∗ as a consequence of self-duality of A+ : since everything in F+ is in A+ , it must have nonnegative
inner product with everything in A+ , hence with everything in F+ , and since it is in addition in F , it is in F+∗ . Recall
that y ∈ F+∗ is defined as y ∈ F and satisfying ∀x ∈ F+ hy, xi ≥ 0. Since P A+ = F+ , the latter part of this condition
is equivalent to ∀z ∈ A+ hy, P zi ≥ 0. Again moving the projector to act on y, using its Hermiticity and that y ∈ F so
P y = y, this is equivalent to ∀z ∈ A+ hy, zi ≥ 0, i.e. y ∈ A∗+ . Since A∗+ = A+ and y was also assumed in F , y ∈ F+ ,
establishing that F+∗ ⊆ F+ . We have now shown F+∗ = F+ , i.e. perfection.
Appendix B: Calculations for observability of energy

The goal of this section is to show the following:
Lemma 33. The possible state spaces satisfying Postulates 1, 2 and 3 which have a non-trivial connected component
G0 of their reversible transformation groups are the following:
• The d-dimensional ball state spaces Ωd := {(1, r)T | r ∈ Rd , krk ≤ 1} with d ≥ 2, and either G0 = SO(d), or
G0 = SU(d/2) if d = 4, 6, 8, . . ., or G0 = U(d/2) if d = 2, 4, 6, 8, . . ., or G0 = Sp(d/4) if d = 8, 12, 16, . . ., or
G0 = Sp(d/4) × U(1) if d = 8, 12, 16, . . ., or G0 = Sp(d/4) × SU(2) if d = 4, 8, 12, . . ., or G0 = G2 if d = 7, or
G0 = Spin(7) if d = 8, or G0 = Spin(9) if d = 16,
• N -level real quantum theory with N ≥ 2 and G0 = {ρ 7→ OρOT | O ∈ SO(N )},
• N -level complex quantum theory with N ≥ 2 and G0 = {ρ 7→ U ρU † | U ∈ SU(N )},
• N -level quaternionic quantum theory with N ≥ 2 and G0 ≃ Sp(N )/{−1, +1} (see [21, 28]),
• 3-level octonionic quantum theory with G0 ≃ F4 .

<!-- page 23 -->
23
However, among those, only the complex quantum theory state spaces (including Ω3 , the qubit) satisfy Postulate 4,
that is, observability of energy.
In complex quantum theory, the group of reversible transformations G can actually be larger: it may also contain the
antiunitary transformations according to Wigner’s theorem (but not more). Similarly, real quantum theory may also
contain the conjugations with O ∈ O(N ) (which yields additional transformations for even N ), but for quaternionic
quantum theory with N ≥ 3, we have G = G0 [60]. As pointed out in [28, 60], the case N = 2 is exceptional in the
quaternionic case. Since the state space is in this case a 5-dimensional unit ball, G may contain reflections in adition
to the rotations SO(5) ≃ Sp(2)/{−1, +1}. We do not know whether octonionic 3 × 3 quantum theory may contain
additional elements in its transformation group, and we do not know the complete classifications of possible compact
transformation groups G ⊃ G0 for the ball state spaces (except that obviously G ⊂ O(d)).
Lemma 33 will be proven step by step. We start by showing that the only ball state space with transitive group of
reversible transformations that has observability of energy is the qubit.
Lemma 34. For d ≥ 2, consider the d-dimensional ball state space Ωd := {(1, r)T | r ∈ Rd , krk ≤ 1}, and let Gd be
any compact group of reversible transformations that acts transitively on the pure states. Then energy is observable
(in the sense of Definition 30) if and only if d = 3.
Proof. If Gd acts transitively on the pure states, then so does its connected component at the identity [50]. According
to [49], the list of groups is the following. Since the group action is locally effective [21], the dimensions of gd are just
the dimensions of the corresponding groups.
• For all d ≥ 2: SO(d). We have shown in the main text that an energy observable assignment only exists if d = 3.
• For d = 4, 6, 8, . . . : SU(d/2). We have dim(su(d/2)) = (d/2)2 − 1, and this is larger than d + 1 if d ≥ 6. Thus,
no injective map φ : su(d/2) → Rd+1 defining an energy observable assignment can exist. However, we have to
treat d = 4 separately. In this case, the transformation group is (up to similarity)



0
0

 1
G4 ⊇  0 re U im U  U ∈ SU(2) ,

 0 −im U re U
such that the Lie algebra is at least


0 0 0 0 0



 0 0 b a c 


g4 ⊇  0 −b 0 c −a 





 0 −a −c 0 b
0 −c a −b 0

a, b, c ∈ R







.






Let X ∈ g4 be a generator corresponding to the choice of parameters a = 1 and b = c = 0. If φ is any energy
observable assignment, we can write the functional φ(X) as a vector ϕ ∈ R5 such that [φ(X)](y) = hϕ, yi for
all y ∈ R5 , and the condition φ(X) ◦ X = 0 translates into X T ϕ = 0. The kernel of X T is one-dimensional,
with unique solution (up to some factor) of ϕ = λ · (1, 0, 0, 0, 0)T , λ ∈ R. But this represents the normalization
functional: hϕ, yi = u4 (y) for all y, so φ(X) = u4 , contradicting the definition of an energy observable assignment.
• For d = 2, 4, 6, 8, . . .: U(d/2). The case d = 2 is already covered in the main text; in all other cases, this
representation contains the corresponding representation of SU(d/2) as a subgroup, and this has already been
treated.
• For d = 8, 12, 16, . . .: Sp(d/4). Dimension counting rules out these cases: We have dim(sp(d/4)) = d/4(2·d/4+1),
and this is larger than d + 1 for the relevant dimensions.
• For d = 8, 12, 16, . . .: Sp(d/4) × U(1). This representation contains the representation of Sp(d/4) as a subgroup;
thus, it is ruled out by the previous case.
• For d = 4, 8, 12, . . .: Sp(d/4) × SU(2). If d ≥ 8, this too contains Sp(d/4) as a subgroup. If d = 4 then the
dimension of the group Sp(1) × SU(2) is 9, which is larger than d + 1 = 5.
• For d = 7: the exceptional Lie group G2 . Dimension counting again: dim g2 = 14 > 7 + 1.
• For d = 8: Spin(7). dim Spin(7) = 7(7 − 1)/2 = 21 > 8 + 1.

<!-- page 24 -->
24
• For d = 16: Spin(9). dim Spin(9) = 9(9 − 1)/2 = 36 > 16 + 1.
This proves the claim.
As mentioned in the main text, it is more difficult to rule out N -level real quantum mechanics for N ≥ 3. This
needs a sequence of lemmas.


0 −1
Lemma 35. Let J =
∈ R2×2 , and let S ∈ R2×2 such that
1 0
JS = αSJ for some α ∈ R.
Then α ∈ {−1, +1} or S = 0. Furthermore, if S = S T and α = 1, then S = c · 1 for some c ∈ R.
We omit the proof; it is a simple exercise in linear algebra.
Lemma 36. Consider any antisymmetric matrix of the form


0 λ1

 −λ1 0


0 λ2




−λ
0
 ∈ R(2k)×(2k) , all λi 6= 0, λi 6= ±λj for i 6= j

2
Y := 

..


.



0 λk 
−λk 0
(all other entries zero). Let S = S T ∈ R(2k)×(2k) be any symmetric matrix that commutes with Y , i.e. [Y, S] = 0.
Then S is a diagonal matrix of the form
S = diag(s1 , s1 , s2 , s2 , . . . , sk , sk ),
si ∈ R.


0 λi
, and divide S into 2 × 2 block matrices Si,j :
Proof. Define the 2 × 2 block matrices Λi :=
−λi 0


S1,1 . . . S1,k

.. 
S =  ...
. 
Sk,1 . . . Sk,k
Then the commutator is the symmetric matrix


[Λ1 , S1,1 ] Λ1 S1,2 − S1,2 Λ2 Λ1 S1,3 − S1,3 Λ3
...


..
..


.
[Λ2 , S2,2 ]
Λ2 S2,3 − S2,3 Λ3
.
.
[Y, S] = 


..


.
...
[Λk , Sk,k ]
If this is the zero matrix, then 0 = [Λi , Si,i ] = −λi [J, Si,i ] for all i. It follows from Lemma 35 that there exists si ∈ R
such that Si,i = si · 1. Similarly, for all i 6= j, we have Λi Si,j = −λi JSi,j = Si,j Λj = −Si,j Jλj , hence JSi,j = αSi,j J
with α = (λj /λi ) 6∈ {−1, +1}. Thus, Lemma 35 yields that Si,j = 0.
We show that an analogue of this remains true in odd dimensions:
Lemma 37. Consider any antisymmetric matrix of the form


0 λ1
 −λ1 0



0 λ2




−λ2 0


 ∈ R(2k+1)×(2k+1) , all λi 6= 0, λi 6= ±λj for i 6= j
Y := 
..


.




0 λk 



−λ 0
k

0

<!-- page 25 -->
25
(all other entries zero). Let S = S T ∈ R(2k+1)×(2k+1) be any symmetric matrix that commutes with Y , i.e. [Y, S] = 0.
Then S is a diagonal matrix of the form
si ∈ R.

S = diag(s1 , s1 , s2 , s2 , . . . , sk , sk , sk+1 ),

Proof. Divide Y and S into block matrices:


Ȳ 0
Y =
,
Ȳ ∈ R(2d)×(2d) ,
0 0


S1,1 S1,2
S =
,
S1,1 ∈ R(2d)×(2d) , S1,2 ∈ R2d , S2,2 ∈ R.
T
S1,2
S2,2
Then

[Y, S] =

[Ȳ , S1,1 ] Ȳ S1,2
T
S1,2
Ȳ
0


.

If this is the zero matrix, then [Ȳ , S1,1 ] = 0, and the diagonal form of S1,1 with all entries repeated twice follows from
Lemma 36. Furthermore, S1,2 ∈ ker(Ȳ ) = {0}. Finally, set sk+1 := S2,2 .
Before applying this, we need to show that real quantum mechanics is necessarily equipped with all reversible
transformations (conjugations with orthogonal matrices) to comply with Postulate 2:
Lemma 38. For N ≥ 3, let ΩN be the state space of N -level real quantum mechanics, and GN be a group of reversible
transformations on it such that Postulate 2 is satisfied. Then

GN = ρ 7→ OρOT | O ∈ G ,
where either G = SO(N ) or G = O(N ). In particular, gN = {ρ 7→ [M, ρ] | M ∈ so(N )}.
Proof. Every G ∈ GN is an automorphism of the cone of positive semidefinite symmetric real matrices, and thus of
the form ρ 7→ QρQT [53]; preservation of the trace implies that QT Q = 1, i.e. that Q is orthogonal. Define G as the
set of all orthogonal Q such that the map ρ 7→ QρQT is contained in GN . Clearly G is a subgroup of O(N ); since GN
is topologically closed, so is G.
Now we show that G contains all of SO(N ). Let a, b ∈ R be irrational numbers such that their difference a − b is
also irrational. Define the unit vectors ei := (0, . . . , |{z}
1 , 0, . . . , 0)T , and
i

v1 := (cos(aπ), − sin(aπ), 0, . . . , 0)T , v2 := (sin(aπ), cos(aπ), 0, . . . , 0)T , v3 = e3 , . . . , vN = eN ,
w1 := (cos(bπ), − sin(bπ), 0, . . . , 0)T , w2 := (sin(bπ), cos(bπ), 0, . . . , 0)T , w3 = e3 , . . . , wN = eN .
Then the sets of vectors {v1 , . . . , vN } and {w1 , . . . , wN } are both orthonormal bases of RN , and so the sets of pure
states {|v1 ihv1 |, . . . , |vN ihvN |} and {|w1 ihw1 |, . . . , |wN ihwN |} are both N -frames in N -level real quantum mechanics,
and so is {|e1 ihe1 |, . . . , |eN iheN |}. Thus, according to Postulate 2, there are two orthogonal matrices V, W ∈ G such
that
V |ei ihei |V T = |vi ihvi |

and

W |ei ihei |W T = |wi ihwi |

for i = 1, . . . , N.

It follows that there are signs σ1 , . . . , σN , τ1 , . . . , τN ∈ {−1, +1} such that V |ei i = σi |vi i and W |ei i = τi |wi i. Hence




σ1 cos(aπ) σ2 sin(aπ) 0 . . . 0
τ1 cos(bπ) τ2 sin(bπ) 0 . . . 0
 −σ1 sin(aπ) σ2 cos(aπ) 0 . . . 0 
 −τ1 sin(bπ) τ2 cos(bπ) 0 . . . 0 




0
0
σ
0
0
τ3



3
V =
,
W =



..
..
..
..
..
..




.
.
.
.
.
.
0
0
σN
0
0
τN
Now we consider two different cases. As the first case, suppose that σ1 = σ2 or τ1 = τ2 . Then




cos(2aπ) sin(2aπ) 0 . . . 0
cos(2bπ) sin(2bπ) 0 . . . 0
 − sin(2aπ) cos(2aπ) 0 . . . 0 
 − sin(2bπ) cos(2bπ) 0 . . . 0 




2
0
0
1
0
0
1
∈G

 ∈ G.
V2 =
or
W
=




..
..
..
..
..
..



.
. 
.
.
.
.
0

0

1

0

0

1

<!-- page 26 -->
26
As the second case, suppose that σ1 6= σ2 and τ1 6= τ2 . Then σ := σ1 = −σ2 and τ := τ1 = −τ2 , and




cos(2(a − b)π) sin(2(a − b)π) 0 . . . 0
cos((a − b)π) sin((a − b)π) 0 . . . 0
 − sin(2(a − b)π) cos(2(a − b)π) 0 . . . 0 
 − sin((a − b)π) cos((a − b)π) 0 . . . 0 




2
0
0
1
0
0
1
 ∈ G.


⇒ (V W ) = 
V W = στ 



.
.
.
.
..
..



.
.
..
..
. 
.
.
.
0

0

0

1

0

1




cos θ sin θ
in the e1 − e2 -subspace,
− sin θ cos θ
where θ is an irrational multiple of π. But any matrix of this form generates all of SO(2) by composition and closure.
We can argue similarly for all other ei − ej -subspaces. The corresponding SO(2) rotations in all these planes generate
all special orthogonal matrices, hence SO(N ) ⊆ G.

In both cases, we have established the existence of a matrix in G that acts as

Theorem 39. Energy is not observable on any N -level real quantum mechanics state space.
Proof. The case N = 1 is trivial; N = 2 is shown in the main text, so let N ≥ 3. First, consider the case that N is
even. Let H ⊂ so(N ) be the subspace of matrices



0 λ1






 −λ1 0











0
λ




2



−λ
0


2
λ1 , . . . , λN/2 ∈ R ,
H := 



..






.












0
λ


N/2


−λN/2 0
and h ⊂ gN be the corresponding subspace of maps of the form ρ 7→ [Λ, ρ] with Λ ∈ H. Moreover, let H 0 be the set
of all Λ ∈ H where the corresponding λi satisfy λi 6= 0 and λi 6= ±λj for i 6= j. Then H 0 is dense in H. Similarly, by
h0 , denote the set of maps ρ 7→ [M, ρ] with M ∈ H 0 ; then h0 is dense in h.
Consider any energy observable assignment φ. Any matrix M ∈ so(n) defines a generator X ∈ gN by X(ρ) := [M, ρ]
and vice versa. This generator is mapped by φ to some map ρ 7→ tr(M̄ ρ), where M̄ = M̄ T . Denote the map M 7→ M̄
by φ̄, such that
[φ(X)](ρ) = tr(φ̄(M )ρ)

if X(ρ) = [M, ρ].

Then we have the equivalences
φ(X) ◦ X = 0 ⇔ [φ(X)](X(ρ)) = 0 for all ρ ⇔ tr(φ̄(M )[M, ρ]) = 0 for all ρ ⇔ tr(ρ[φ̄(M ), M ]) = 0 for all ρ,
and so φ̄(M ) is a symmetric matrix that must commute with M . Suppose that M ∈ H 0 , then Lemma 37 shows
that φ̄(M ) = diag(s1 , s1 , s2 , s2 , . . . , sN/2 , sN/2 ). Denote by H the linear space of all diagonal (N × N )-matrices
of that form. We have shown that φ̄(H 0 ) ⊂ H. Since H 0 is dense in H, this implies that φ̄(H) ⊂ H. Since
dim H = dim H = N/2, and since φ̄ is injective, this implies that φ̄(H) = H. In particular, there is 0 6= M ∈ H such
that φ̄(M ) = 1, so the corresponding generator X ∈ h satisfies X(ρ) = [M, ρ] which is not identically zero for all ρ,
and [φ(X)](ρ) = tr(ρ) = uN (ρ), contradicting the definition of an energy observable assignment.
Now consider the case that N is odd, say, N = 2k + 1. Define the subspace H of antisymmetric matrices by



0 λ1







 −λ1 0










0
λ




2








−λ2 0



H := 
λ
,
.
.
.
,
λ
∈
R
1
k
.

..














0
λ




k








−λ
0


k


0
Similar argumentation as in the even case, now using Lemma 37, shows that φ̄(M ) is a diagonal matrix for every
M ∈ H; the same conclusion holds true if the subspace H is defined by appending the zero in the top-left corner

<!-- page 27 -->
27
instead of the bottom-right. But then, by linearity, the matrix

 

0 λ1
0 λ1
 
  −λ1 0
 −λ1 0

0

 

0 λ2
0 λ2

 


  ..
 

−λ2 0
−λ2 0
.

 
 






+
=
M := 
..
..
0






.
.
 
 

0 λk 

 

0 λk 
0
λk
 

−λk 0


−λk 0
−λk 0 λk  
0
−λk 0
also has the property that φ̄(M ) is a diagonal matrix. Suppose that all λi 6= 0, then the only diagonal matrix S that
commutes with M is of the form S = diag(s1 , s1 , s2 , s2 , . . . , sk−1 , sk−1 , sk , sk , sk ). Again, arguing analogously to the
even case, the subspace of all matrices M of the given form (dropping the condition λi 6= 0) is mapped by φ̄ injectively
into the subspaces of all diagonal matrices S of that form. Since both are of dimension k, there is M 6= 0 such that
φ̄(M ) = 1, violating the definition of an energy observable assignment.
