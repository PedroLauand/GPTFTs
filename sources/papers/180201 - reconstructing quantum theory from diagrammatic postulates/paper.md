---
type: paper
date: 2018-02-01
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1802.00367v3)
reviewed: false
---

# Reconstructing quantum theory from diagrammatic postulates

Machine-generated and unreviewed text extraction of arXiv:1802.00367v3
(64 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1802.00367v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Reconstructing quantum theory from diagrammatic
postulates

arXiv:1802.00367v3 [quant-ph] 21 Apr 2021

John H. Selby1 , Carlo Maria Scandolo2,3 , and Bob Coecke4
1

ICTQT, University of Gdańsk, Wita Stwosza 63, 80-308 Gdańsk, Poland

2

Department of Mathematics & Statistics, University of Calgary, Canada

3

Institute for Quantum Science and Technology, University of Calgary, Canada

4

Cambridge Quantum Computing Ltd
2021-04-17

A reconstruction of quantum theory refers to both a mathematical and a
conceptual paradigm that allows one to derive the usual formulation of quantum theory from a set of primitive assumptions. The motivation for doing so is
a discomfort with the usual formulation of quantum theory, a discomfort that
started with its originator John von Neumann.
We present a reconstruction of finite-dimensional quantum theory where
all of the postulates are stated in diagrammatic terms, making them intuitive.
Equivalently, they are stated in category-theoretic terms, making them mathematically appealing. Again equivalently, they are stated in process-theoretic
terms, establishing that the conceptual backbone of quantum theory concerns
the manner in which systems and processes compose.
Aside from the diagrammatic form, the key novel aspect of this reconstruction is the introduction of a new postulate, symmetric purification. Unlike the
ordinary purification postulate, symmetric purification applies equally well to
classical theory as well as quantum theory. Therefore we first reconstruct the
full process theoretic description of quantum theory, consisting of composite
classical-quantum systems and their interactions, before restricting ourselves
to just the ‘fully quantum’ systems as the final step.
We propose two novel alternative manners of doing so, ‘no-leaking’ (roughly
that information gain causes disturbance) and ‘purity of cups’ (roughly the existence of entangled states). Interestingly, these turn out to be equivalent in
any process theory with cups & caps. Additionally, we show how the standard purification postulate can be seen as an immediate consequence of the
symmetric purification postulate and purity of cups.
Other tangential results concern the specific frameworks of generalised
probabilistic theories (GPTs) and process theories (a.k.a. CQM). Firstly, we
provide a diagrammatic presentation of GPTs, which, henceforth, can be subsumed under process theories. Secondly, we argue that the ‘sharp dagger’ is
indeed the right choice of a dagger structure as this sharpness is vital to the
reconstruction.
John H. Selby: john.h.selby@gmail.com
Carlo Maria Scandolo: carlomaria.scandolo@ucalgary.ca
Bob Coecke: bob.coecke@cambridgequantum.com

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

1

<!-- page 2 -->
Contents
1

Introduction
1.1 Main result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Purification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Connection to GPTs, OPTs, CQM and CPTs . . . . . . . . . . . . . . . . .

3
4
6
7

2

Process theoretic concepts
2.1 Discarding and causal processes . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Diagrammatic sums . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Classical interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 Leaks and purity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5 Cups, caps and sharp daggers . . . . . . . . . . . . . . . . . . . . . . . . . .

7
9
12
14
18
20

3

The postulates
24
3.1 Symmetric purification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

4

The reconstruction

26

5

Distinguishing quantum and classical systems

41

6

Related work
6.1 Purification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2 GPTs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 CPTs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

42
42
44
44

7

Future work

44

A Consequences of a classical interface
A.1 Proof of Proposition 2.22 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.2 Proof of Proposition 2.23 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.3 Proof of Proposition 2.24 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.4 Proof of Proposition 2.25 . . . . . . . . . . . . . . . . . . . . . . . . . . . .

53
53
54
56
57

B Classification of leaks and pure processes

58

C Symmetric purification in quantum theory

62

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

2

<!-- page 3 -->
1 Introduction
Reconstructions of quantum theory aim to reproduce the standard quantum formalism
from assumptions of some desired flavour, which in our case means diagrammatic. The
idea of reconstructing quantum theory is not at all new; indeed, the first to contribute to
the endeavour was John von Neumann. Merely three years after the publication of his
book [112], which cemented the mathematical formalism of quantum theory, he made it
clear in a letter to the mathematician Garrett Birkhoff that he was no longer satisfied
with the Hilbert space formalism [96]. However, rather than just aiming to reconstruct
this formalism, his hope was in fact to find a different formalism that might also produce
new physics. The actual reconstruction program, building further on von Neumann’s
work, was outlined by George Mackey [88], and mostly completed by Constantin Piron
[95] (an academic ancestor of two of the authors) within the arena of so-called property
lattices, and by Günther Ludwig [87] within the arena of generalised probabilistic theories
(GPTs). The main motivation for this was a dissatisfaction with accepting the abstract
Hilbert space as a given. Instead, the aim was to start off with conceptually justified
structures and axioms from which the Hilbert space could be derived.
A more modern perspective is that reconstructions (by helping one see the physical
principles that underlie the Hilbert space structure) allow one both to derive more results
of quantum theory, and to understand how it can, and should, be modified in order to
reconcile it with general relativity.
The flavour of the assumptions that go into a reconstruction has varied substantially,
ranging from counterfactual ontology to instrumentalism. However, broadly, there are two
kinds of approaches.
The first wave of reconstructions [6, 7, 87, 88, 95, 112], surveyed in [46], took place
in the previous century, and the assumptions used therein were taken to be axioms in
the mathematical sense. Nothing was left implicit, and, as a result, the mathematical
sophistication of these reconstructions was substantial. For example, Piron’s Theorem
[95] was actually only finalised in 1995 by Solèr [104], while arguably it already took off
from von Neumann’s book [112] which initiated the study of quantum logical principles in
1932. In this first wave, different reconstructions corresponded to different conceptually
motivated mathematical structures, e.g. lattices [95] or generalised probability spaces [87].
In this millennium, a new wave of quantum reconstructions emerged under Lucien
Hardy’s impetus [34, 53, 67, 70, 89]. In these, there was a broad shift away from the
mathematical axiomatics of the first wave. Instead, they took inspiration from Einstein’s
derivation of relativity theory from two ‘principles’, i.e. the constancy of the speed of
light and the invariance of laws for different observers. This shift means that many pieces
of structure are often sneaking into the reconstructions —like in Einstein’s derivation of
relativity theory— for example, dimensions are typically restricted to finite ones, and
the structure of real line is put in by hand, usually in the form of probabilities, while in
[95] it was constructed. The resulting reconstruction axioms and their presentation do
not have the feel of a mathematical domain but are more akin to Einstein’s principles of
relativity. Consequently, to distinguish the assumptions used in these approaches from
the mathematical axioms of the first wave, the term ‘postulates’ was adopted. Now,
the conceptual grounding of the postulates is of key importance. These are typically
cast within some ‘interpretative school’; for example principles only make reference to
measurement [67], or are information-theoretic [34, 36], or even make reference only to
properties of single systems [15]. To simplify the problem, and as a potential stepping
stone to a full reconstruction, only finite-dimensional Hilbert spaces were considered. This

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

3

<!-- page 4 -->
stance was not only for mathematical convenience, but also justified by the many new
results —within the context of quantum foundations, information, and computation—
demonstrating that the essential quantum phenomena are all apparent within the finitedimensional setting.
One common theme in this new wave of reconstructions is a consideration of the role
of composite systems. For example, principles such as tomographic locality [19] concerned
pairs of systems, rather than just a single one. This is in sharp contrast with the first
wave of reconstructions, where the focus was on single systems under observation. Indeed,
for this first wave, the Achilles heel was the description of composite systems at a general
axiomatic level: while these approaches were able to recover Hilbert space, they all failed
to reproduce the tensor product as part of the formalism. This is probably why —with
the emergence of quantum computation and information, where composition is of course
vital— these approaches have more or less vanished. But, despite this significant advantage
over the first wave, the postulate-based approaches lacks the mathematical clarity of the
earlier attempts, and in many cases the proofs are not so insightful.
Learning from the failures of the earlier axiomatic reconstructions, a rigorous focus
on composition of quantum systems and processes has been the subject of categorical
quantum mechanics (CQM) [1, 43] for some 15 years now. Its initial goal was to recast
quantum theory in high-level terms, making reasoning and computing more intuitive.
While the first reconstructions of the second wave focused on states of physical systems
and their geometry, the categorical approach changed the paradigm completely, from states
to processes [39]. Consequently, one now refers to the theories that CQM is concerned
with as process theories. The particular nature of the categorical structures that make up
process theories have the great upshot that they admit a full and faithful diagrammatic
representation [37, 38, 101] (a.k.a. quantum picturalism). This has provided an intuitive
picture of many aspects of quantum information, computation, and a wide variety of
other fields [10, 25, 50–52, 54–58, 60, 75, 81, 91, 97, 98, 106, 110] which lends itself well
to computational automation [26, 59, 62, 79].
Meanwhile, borrowing from CQM, many reconstructionists of the second wave adopted
‘diagrams of processes’ as their starting point [33, 34, 70, 71], hence embracing composition
of processes as one of the core ingredients of quantum theory. More recently, a third wave
of reconstruction attempts took off [14, 15, 116], which can be seen as resurrecting the
mathematical spirit of the first wave, while still embracing the principled underpinning
that guides the second wave. Recently, there have been various other reconstructions of
quantum theory from a variety of perspectives, for example [24, 66, 73, 74, 92, 109, 113].

1.1 Main result
This paper provides a reconstruction that is conceptually grounded whilst still being based
on crisp mathematical axioms. This is achieved by exploiting the correspondence:
diagrams ≃ category theory ≃ process theory
Our postulates are now diagrammatic, i.e. category-theoretic, i.e. process-theoretic, providing them with an intuitive, elegant, as well as principled underpinning. In short, what
we prove is:
classical interface + postulates about how processes compose =⇒ quantum processes
More explicitly, the complete list of postulates (introduced formally in Sec. 3) that we use
to reconstruct quantum theory are as follows:
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

4

<!-- page 5 -->
1. the theory is a process theory (Def. 1),
2. with a finite local1 classical interface (Defs. 2.14 & 2.20),
3. cups & caps (Def. 3),
4. a sharp dagger (Def. 4),
5. and in which all processes admit essentially unique symmetric purifications (Def. 3.1).
To understand these postulates and the properties derived from them, one must be
familiar with the process theory framework and the associated diagrammatic language. In
Sec. 2 we therefore provide an introduction to this framework and the concepts necessary
to read the rest of the paper. For a more detailed introduction see [43].
Informally, requiring that the theory be a process theory states that nature is fundamentally grounded on processes, and how they compose. The classical interface describes
how we interact with, control, and learn about the theory. Cups and caps represent a
fundamental symmetry that ensures that the theory has maximal correlations. The sharp
dagger represent another fundamental symmetry, namely time reversal. Informally, the
time reverse of a process can be thought of as “playing the video of that process in reverse”. In particular, for a state this corresponds to a ‘test’ for that state: we view states
as a mapping from the trivial system to a non-trivial system, the time reverse is therefore
a map from the non-trivial system to the trivial system (i.e. a measurement outcome),
this should single out the state within the state space. Finally, the existence of symmetric
purifications ensures that any lack of purity can always be traced to lack of access to the
past or the future of certain systems.
The proof of this result is remarkably simple in contrast to many other reconstructions,
indeed, the entire reconstruction can be presented in a simple flowchart (see Fig. 1). This
is largely owing to two things, firstly, to the use of diagrammatic proofs, and, secondly,
to the use of a standard result, the Koecher-Vinberg theorem [82, 111]. The latter was
borrowed from the works of Barnum, Wilce et al., e.g. [12–14, 18, 116].
There have been several other reconstructions of quantum theory, from various different
perspectives, many results of which have been adapted for this work. It is therefore worth
highlighting the key novel features of this particular reconstruction that distinguish it from
the others.
• Firstly, the postulates we impose are diagrammatic, moreover, they do not pick out
states as being special, applying instead equally well to all processes. As such, they
fit with the spirit of CQM and the process-theoretic understanding of the world, that
is, as being about processes and composition. Indeed, this is the first reconstruction
where the postulates are entirely diagrammatic. In the past some reconstructions
have utilised a diagrammatic formalism, but the basic framework has always involved
some non-diagrammatic component – for example in how the probabilistic structure
is introduced. We show that this is unnecessary, and that the postulates and the basic
framework can all be stated within a diagrammatic formalism. This use of diagrams
is much more than just a stylistic choice, it forms the conceptual underpinning of the
work, and it is the natural language in which one should express these postulates. For
example, the aforementioned symmetric purification postulate is relatively simple to
state and understand diagrammatically, whereas it is, to the authors at least, much
more opaque when translated into algebraic or categorical terms.
1

In the sense of local tomography, a commonly used postulate in reconstructing quantum theory.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

5

<!-- page 6 -->
• Secondly, we reconstruct the full process-theoretic description of quantum theory
– that is, the C*-algebraic formalism of quantum theory, including measurements,
hybrid quantum-classical systems, superselected quantum systems, and so on. We
argue that this is how quantum theory should be described, and, moreover, this
perspective allows us to clearly see what it is that separates the fully quantum
systems from the others—specifically, the triviality of leaks, or equivalently, purity
of the cups & caps. Typically, reconstruction efforts have only reconstructed the
fully-quantum subtheory, and have neglected measurements and classical processes
as an integral part of the reconstructed structure. For example, the majority of the
other reconstructions take transitivity as a postulate2 . Transitivity is the property
that there is a reversible transformation between any pair of pure states. This does
not hold for general C*-algebras, so most other reconstructions immediately rule out
the full C*-algebraic theory. This calls into question how natural such postulates
were in the first place.
• Thirdly, the symmetric purification postulate is a new postulate that has not been
considered elsewhere. Indeed, as far as the authors are aware, this is a feature
of quantum theory which has not been noted elsewhere in the literature. As this
applies equally well to both classical and quantum theory, it has the potential to
help unify many results that typically rely on a distinct proof for each theory. For
instance, many features of quantum cryptography —such as the impossibility of
bit-commitment— use proofs which ultimately rely on the purification postulate.
However, bit-commitment is also impossible in classical theory in which purification
fails. Therefore it seems that our symmetric form of purification could be utilized
to prove results that immediately hold for both theories.
• Finally, the reconstruction is relatively simple. In particular, the structure of the
reconstruction is clear (see Fig. 1), allowing a high-level view of how the different
postulates relate to each other and how they are used in each step. This should
make it simpler to understand how relaxing or altering any given postulate will lead
to new theories. In contrast, in many other reconstructions (perhaps due to their
presentation rather than any intrinsic properties) it is difficult to know precisely
which postulates, and which of the assumptions of the framework, are necessary to
obtain each result.

1.2 Purification
The standard purification postulate was first used in [33] as an operational generalisation
of the Stinespring dilation theorem [105]. It roughly states that any mixed process can be
represented as a pure process with an extra output that is discarded. Importantly, this
postulate is satisfied by quantum theory, but not by classical probability theory, so it can
be used to single out quantum theory [33].
Our symmetric purification postulate, in contrast, holds for both quantum and classical
theory. We therefore reconstruct quantum, classical and hybrid systems all together. One
can then ask how to single out fully quantum systems. There are many ways to do so, but
two of them are of particular interest: the existence of a pure ‘cup’ (roughly speaking the
existence of entanglement), or, the lack of non-trivial ‘leaks’ (essentially that information
gain causes disturbance). Whilst at first glance these appear to be unrelated postulates
2

Or they have it as a direct corollary of a stronger postulate, such as purification or strong symmetry.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

6

<!-- page 7 -->
involving different diagrammatic concepts, they can actually be shown to be equivalent in
any process theory with cups & caps.
Moreover, it can be shown that the standard purification postulate is implied by the
conjunction of the symmetric purification postulate and the existence of a pure cup.
Hence our work can be seen as deconstructing the standard purification postulate into
two parts —one which applies to both quantum and classical theory, and the other only
to quantum— therefore refining exactly what is uniquely quantum about purification.

1.3 Connection to GPTs, OPTs, CQM and CPTs
While initially GPTs only appealed to single systems, under the impetus of CQM a new
hybrid form was proposed (a.k.a. Operational Probabilistic Theories (OPTs)), where composition supported by a diagrammatic backbone. We demonstrate that, within the context
of process theories, the essential structure of OPTs can be derived from the classical interface postulate. Hence, OPTs are subsumed under the process-theoretic framework.
Independently, a similar result was also obtained in [65], where the framework of Categorical Probabilistic Theories (CPTs) was developed. In that paper, three requirements
(Definition 1) were made of a CPT. The first of these is part of the definition of a classical
interface, whilst we find that the second two can be derived from our postulated classical
interface. Whilst our postulated classical interface is a mathematically stronger assumption than those made in the definition of a CPT, we find it preferable, as it has a clear
physical interpretation.
Cups and caps have been part of the structure of CQM from the start [1], and provide a
cup- and a cap-shaped wire for each system: allowing for inputs to be connected to inputs
and outputs to outputs. Daggers have also been part of CQM since its very beginning
[2, 101]. Unlike the transpose, which is constructed using cups & caps, a dagger did not
have any other structural requirements besides being compositional. In order to fully
characterise the Hermitian adjoint of quantum theory, a sharpness constraint was added
in [99]. We demonstrate that, once we have a classical interface, cups & caps, and a sharp
dagger, the only additional postulate to be imposed, for a process theory to correspond
to the Hilbert space model, is the aforementioned symmetric purification postulate.

2 Process theoretic concepts
Process theories [42, 43] are theories that have a particular diagrammatic representation.
A comprehensive introduction can be found in [43]. In this section we introduce the
process-theoretic concepts and tools which will play a role in the reconstruction. Some of
these will be postulated in Sec. 3, whilst others will be derived from these postulates in
Sec. 4, or simply be used in various proofs throughout.
Definition 2.1 (Process theory). Process theories consist of a collection of systems, denoted by labelled wires, and a collection of processes, denoted by labelled boxes with input
wires (at the bottom) and output wires (at the top). These processes can be wired together, for example:
g
B
A

C

f
A

h

D

D

i

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

7

<!-- page 8 -->
where the resulting diagram must also be a process in the theory; the relevant data for a
diagram are:
i. the processes that appear in the diagram, and
ii. how the diagram is connected, including the overall ordering of free inputs and outputs;
the formation of diagrams is constrained by:
1. connected systems must have the same type (i.e. the same label),
2. outputs are wired up to inputs, and
3. no loops are created.
Remark 2.2. For those who favour an information-based characterisation of quantum
theory, one can think of the wires in the diagrams as information flows. For those who
favour a more operational interpretation, one can think of the processes as corresponding
to a single use of a piece of lab equipment in a single run of an experiment.
There are three particular types of processes within a theory that are often distinguished: those with no inputs, which are state preparation procedures or states for short;
those with no outputs, corresponding to the outcome of some destructive measurement,
or effects for short; and those with neither, known as scalars, which typically correspond
to probabilities. These are respectively denoted as:
s

,

and

e

p

.

Note that we often drop various labels and the box around scalars when they are clear
from context. It is often useful —particularly in connecting these theories to standard
mathematical models— to introduce two primitive forms of composition: sequential composition, symbolically denoted as g ◦ f , and parallel composition, denoted as f ⊗ g, which
diagrammatically correspond to:
g
f

and

f

g

respectively.

We also represent the parallel composition of systems as A ⊗ B, hence allowing us to treat
parallel wires as a single wire, that is:
A B

=

A⊗B

Moreover, to translate into standard symbolic notation, we denote a process f with
input A and output B as f : A → B. To describe processes lacking inputs and/or
outputs, we must therefore introduce a fictitious ‘trivial’ system denoted I, so that we
can, for example, denote the state s of a system C as s : I → C. To be consistent with
our diagrammatic notation, that is, I representing the lack of an input, it must satisfy the
equation of I ⊗ A = A = A ⊗ I, i.e. appending a trivial system does nothing.
A simple example of a process theory is classical probability theory:

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

8

<!-- page 9 -->
Example 2.3 (Classical). Here we restrict ourselves to finite probabilistic models. We can
characterise every classical system with a natural number n which we call its dimension.
The composite of systems is given by the product of their dimensions, i.e. n⊗m = nm, and
so the trivial system corresponds to n = 1. Processes f : n → m then correspond to m × n
matrices with non-negative matrix elements. Sequential composition is given by matrix
multiplication and parallel composition by the standard tensor product. States therefore
correspond to n × 1 matrices, i.e. vectors, and effects 1 × m matrices, i.e. covectors; the
sequential composition of a state and effect therefore gives a scalar valued in R+ . Many
of the processes in this theory lack a physical interpretation. For instance, the physically
meaningful scalars are those in the interval [0, 1], that is, those which can be interpreted as
probabilities. Nonetheless, the non-physical processes are extremely useful for performing
calculations in classical probability theory. We will return to this issue and characterise
the physical processes in the following section.
A more involved example is the process-theoretic description of quantum theory, which
includes quantum, classical, composite, and hybrid systems. The not fully quantum systems in this process theory can be interpreted in two ways [49]: either as the systems
that arise from the branching structure of measurements, or as the systems that are obtained from a generalised decoherence mechanism. In particular, the classical systems are
necessary for a process-theoretic description of quantum measurements.
Example 2.4 (Quantum). Here we restrict ourselves to finite-dimensional quantum theory. Systems correspond to finite dimensional C*-algebras, which can be represented as
L
nk
direct sums of complex matrix algebras [22]:
k M (C ). The standard tensor product
provides composition, hence, the trivial system is given by M (C). Processes are completely
L
L
positive maps of C*-algebras, f : k M (Cnk ) → l M (Cnl ). States therefore correspond
to block-diagonal density matrices and effects to block-diagonal POVM elements. Again,
scalars correspond to non-negative real numbers.
We can retrieve the fully quantum or fully classical systems by restricting to those of
L
the form M (Cn ) or m
k=1 M (C) respectively, the former system being equivalent to an nlevel quantum system and the latter to an m-dimensional classical system. The processes
between systems of these respective types are precisely those that we would expect. For
L
example, states of M (Cn ) are just n-level density matrices, and states of m
k=1 M (C) are
probability distributions over an m-element set.
Again we view this as the process theory for performing calculations about quantum
theory. We will introduce ‘physicality’ conditions in the following section which tell us
which of these processes could be implemented in a lab without post-selection.

2.1 Discarding and causal processes
A process theory often comes with a discarding effect for each system, which provides a
way to ‘throw away’ or even simply ‘ignore’ systems. We denote this by:
A

where, it should be the case that, discarding two systems independently is the same as
discarding the composite system:
=
A⊗B

.
A

B

In theories with discarding we can elegantly define causality of processes.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

9

<!-- page 10 -->
Definition 2.5 (Causal processes and causal subtheory). A process f is causal [33, 43] if
it satisfies:
A

=

f
B

B

(1)

By the causal subtheory we then mean the theory of all causal processes. This is itself
a valid process theory as it is easy to show that the causal processes are closed under
forming diagrams.
The connection between Def. 2.5 and standard notions of causality may not be immediately apparent. However, it can be shown that within the causal subtheory future
measurement choices do not effect current experiments [33]. More general, it implies that
there is no superluminal signalling in the subtheory [40], and even full compatibility with
relativity [80].
Note that the definition of a causal subtheory automatically implies that the only
effects in the subtheory are the discarding effects themselves:

=

f
B

B

(2)

It therefore turns out to be beneficial not to work with the causal subtheory, but with
the full theory including non-causal processes. This is standard practice within quantum
theory which, besides Dirac kets, also has non-causal Dirac bras. That is, allowing for
non-causal processes gives access to the specific outcomes in a measurement (cf. “in a
measurement we obtain the outcome corresponding to bra hx|”), or more generally, processes that can only occur probabilistically. Moreover, just as in the case of kets and bras,
the larger theory can admit additional symmetries that allow one to characterise it more
easily. We discuss these symmetries below in Sec. 2.5.
We view causal processes as being the physically realisable processes, that is, those
that represent the physical evolution of a system independent of what any agent thinks
about it. How then should we view measurements, which, as we have just discussed above,
are typically defined by non-causal processes? To view measurements as causal processes,
we must ‘bunch’ together a collection of non-causal processes to represent all ‘branches’ of
a measurement, or more general non-deterministic process, as a single causal process. In
order to do so we will introduce classical systems —represented diagrammatically by thin
grey lines3 — to store the resultant probability distribution over the possible outcomes:
n

where n ∈ N denotes the number of distinguishable states of the classical system. We can
then define measurements within the causal subtheory as follows.
Definition 2.6 (Measurements). Destructive measurements are processes with only a
classical output:
m

3

Note that in this paper, whilst a thin gray wire always indicates a classical system, a thicker solid wire
indicates any system allowed by the theory, which could be in fact classical.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

10

<!-- page 11 -->
general measurements are then processes that have both classical and non-classical outputs: and non-destructive measurements are just processes of the form
M
There is no need to add any more here, once we have classical systems as part of
the theory measurements are just a special kind of process rather than a fundamentally
different type of object. Moreover, there are other sorts of interesting processes that we
can consider once we have such classical systems, for example:
Definition 2.7 (Classical control). Classical control over state preparation is achieved
via processes of the form
S

where the choice of classical state input into S will determine the quantum state that is
prepared. More generally we can classically control processes using processes of the form:
P
where the choice of classical state input into P will determine which quantum process
occurs.
Theseinteractions between classical systems and the general systems of our theory form
the basis of the classical interface for a theory that we introduce in section 2.3.
Example 2.8 (Classical). We define the discarding map to be the covector with every
matrix element 1. The causal subtheory is the restriction to stochastic matrices, as they
will satisfy Eq. (1). In particular, this condition implies that states correspond to probability distributions over an n element set, and that processes are maps from probability
distributions over n elements to those over m elements. In particular we denote the states
and effects that are everywhere 0 except for a 1 at position i as:
i

and

i

respectively.

Example 2.9 (Quantum). We define the discarding maps in this theory to be the (partial)
trace, hence causal states correspond to block-diagonal trace-1, density matrices with
L
blocks of dimension {nk }, that is, trace-1 elements of k M (Cnk ). General processes are
causal if and only if they are trace-preserving.
This theory contains both quantum and classical theory as subtheories. Moreover it
L
contains processes mapping between these sectors, such as f : M (Cn ) → m
k=1 M (C)
mapping from a quantum to a classical system. Such processes can be shown to correspond to POVMs in the standard presentation of quantum theory, where the causality
constraint for these measurements is equivalent to the constraint that POVM elements
sum to the identity. General processes with both quantum and classical inputs and outputs have similarly clear interpretations: the classical input can be seen as a control
system determining which process to implement, the implemented processes can involve
some (potentially non-destructive) measurement, the result of which is then encoded in
the classical output.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

11

<!-- page 12 -->
2.2 Diagrammatic sums
Let us first, for simplicity, introduce a shorthand notation for certain ‘vise’-shaped diagrams that will be useful for this section and throughout the paper.
Definition 2.10 (Vise). A vise, χ, is defined by a pair of processes and a shared system
(xχ , yχ , Eχ ):
D
D
B

χ

yχ
:=

A

B

Eχ

A

xχ

C

C

On the one hand we can view these vises as being simply a process with composite
input B ⊗ C and composite output A ⊗ D:
A

D

χ
B

C

and on the other hand we can view them as being a map from the processes with input A
and output B to the processes with input C and output D:
D

D
B

B

χ

A

::

7→

f

χ

f

A
C

C

With this notational short-hand in place, we will now introduce another useful concept:
that of a ‘diagrammatic sum’. Whilst not a strictly diagrammatic notion itself, it can
be derived from the classical interface that we will postulate, and it is vital to making
connections to more standard linear-algebraic techniques that we will use in various proofs.
Definition 2.11 (Diagrammatic summation). A sum is an associative, commutative,
binary operation with a zero element on processes with the same inputs and outputs, i.e.
P
given a set of processes fi : A → B, there is a process i fi : A → B. Moreover, it
distributes over diagrams, that is, for all χ, C and D:
D

D

B

P
i

fi

B

χ

=

P
i

A
C

fi

χ

,

(3)

A
C

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

12

<!-- page 13 -->
where χ is shorthand for a diagram of that shape, i.e.:
D
D
B

χ

yχ
:=

A

B

.

Eχ

(4)

A

xχ

C

C

Example 2.12 (Quantum). We can now discuss sums of processes within quantum theory. If we define sums of CP maps in the usual way, then linearity of CP maps and
bilinearity of the tensor product ensures that these will distribute over diagrams, hence,
are diagrammatic sums in the sense of def. 2.11.
Example 2.13 (Classical). Similarly, we can discuss sums of processes within classical
theory. That is, if we define sums of substochastic maps in the usual way, then linearity of
substochastic maps and bilinearity of the tensor product ensure that these will distribute
over diagrams. In this case, by decomposing the identity process, sums allow us to have a
convenient ‘matrix representation’ of classical processes:
m
m

f

j

j

=

n
X
X m

f

i=1 j=1

n

m

m

=:

fi

i

ij

n
i

X j j
n

i

n

In general such a sum will not exist in the causal subtheory, at least, in the probabilistic
theories that we are interested in here. The structure of diagrammatic summation however
gives us some insights into the structure of the causal subtheory. For example – in a theory
where the scalars are non-negative real numbers and their sum is given by the usual sum
(as will be the case in process theories with a classical interface) – if f and g are causal
processes, then:
p

f

and (1 − p) g

with p ∈ (0, 1), are not. However, their sum is a causal process as
p

f

+ (1 − p) g

=

p

+(1 − p)

= (p + (1 − p))

=
That is, convex combinations of causal processes are themselves causal. Introducing sums
in such theories therefore ‘reveals’ the convex structure of the subcausal theory. This is a
recurring theme in this paper. Many compositional structures we use are defined in the
full theory, but, still have an important impact on the causal sub-theory. In particular,
this will be the case for postulates 3 and 4, as is discussed in detail in Sec. 2.5 .
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

13

<!-- page 14 -->
2.3 Classical interface
We can now formalise how we access general systems by means of a ‘classical interface’.
Definition 2.14 (Classical interface). A classical interface comprises three parts (each of
which we will formally introduce in this section):
i. a full classical subtheory,
ii. all classically controlled processes, and
iii. sufficient causal-compatible tomography tests.
The first of these is straightforward. To have a classical interface the process theory
must have classical systems and processes as defined in Ex. 2.3.
Definition 2.15 (Full classical subtheory). To begin, the process theory must have arbitrary classical systems:


n∈N

n

and the processes with classical inputs and outputs






f




m 




n 

must be precisely the set of classical processes, no more no less. Moreover, they must
compose in the same way as they do classically, that is, we must be able to manipulate
the diagrams involving only classical systems exactly as in Ex. 2.3.
Note that an important consequence of this is that the trivial system must belong to
this classical subtheory such that, for example, classical states are indeed classical. An
important consequence of this is that the scalars of a theory with a classical interface are
simply the classical scalars, R+ .
The other two parts of the interface introduce the interactions between this full classical
subtheory and the rest of the process theory. Firstly, ‘classically controlled processes’ (c.f.
Def. 2.7) formalise the idea that we can choose which process out of a family to implement,
possibly using randomness (e.g. by rolling a die).
Definition 2.16 (Classically controlled processes).

For a set of processes







n

B

B 


a controlled process

fi

is one such that:

F



A 

i=1

n

∀i

F

=

fi

A

(5)

i

For example, if we let {fi } be a set of states, this provides the controlled state preparations considered in Sec. 2.1.
Secondly, ‘tomography tests’ (c.f. Def. 2.6) formalise how classical systems can be used
to characterise processes by the probabilities obtained in experiments.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

14

<!-- page 15 -->
Definition 2.17 (Tests for finite process tomography). For a pair of systems (A, B) a
controlled test is a vise of the form
n

n
B

B

τ

such that

B

=

f

A

A

n

B

⇐⇒

g
A

B

f

=

τ

A

m

g

τ

(6)

A
m

m

For example, if we let A be the trivial system such that τ is doing state tomography,
then this provides us with the measurements of Def. 2.6.
Remark 2.18. Note that the definition of classical theory we are using automatically
implies that n and m are finite. This means that if a theory has tomographic tests then it
is never necessary to perform an infinite number of distinct experiments to characterise a
process. Consequently, the set of probabilities needed to describe a process is finite. Note
that in practice it is never possible to perform an infinite number of experiments so we
should at least expect this to hold for our best effective theory of nature.
We however will demand something stronger than this, namely we will demand that our
tomographic tests are compatible with causality. As we do not have a notion of a discarding
map for the theory as a whole we instead will introduce a notion of compatibility with the
causality of the classical subtheory.
Definition 2.19 (Causal-compatible tomographic tests). A collection of tomographic
tests is said to be causal-compatible if any composite of them such that the resulting
process is classical is a causal classical process. For example, one way of composing them
to give a classical process would be:

τ

A

B

B

A

τ0

then causal-compatibility implies that:

τ

A

B

B

A

τ0

=

It is common to assume that tomography can be performed locally. This expresses the
idea that: although we know the world to be non-local (in the sense of [20]), there are still
no holistic degrees of freedom, and that the description of two distinct regions of space can
be formulated entirely in terms of their individual properties and the correlations between
them. One can consider that the ability to be characterised locally is really the defining
feature of what we mean by a system: a system is something we can isolate and study in
its own right, independent of the rest of the world.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

15

<!-- page 16 -->
Definition 2.20 (Local tomography). The tests τ in the definition of the classical interface
are said to be local if they factorise over parallel composition:
nα nβ
n
A
C

α

···

B

···

=

τ

(7)

D

···

β

···

γ

δ

m
mγ mδ

where n = nα · · · nβ and m = mγ · · · mδ . If all of the tests in a classical interface are
local then it is said to be a local classical interface, and the theory is said to be locally
tomographic.
Example 2.21. Quantum theory, as mentioned earlier, has a classical subtheory and
moreover has all possible classically controlled processes and suitable causal-compatible
tests for finite, local, tomography. In particular, local tomography [8, 21] has been used
in many reconstructions of quantum theory, e.g. [35, 70]. This can be extended to the
full process-theoretic description of quantum theory by viewing general C*-algebras as
restricted quantum systems (in the sense of [49, 72, 102].
Before moving on to some more basic process theoretic concepts let us first explore
some of the consequences of having a classical interface. Ultimately we will show that a
classical interface provides us with most of the structure that is typically assumed in the
GPT framework [19, 67].
Firstly we can show that classically controlled processes are unique.
Proposition 2.22. In a theory with a classical interface (Post. 2) classically controlled
processes (Def. 2.16) are unique. That is, given a set of processes {fi : A → B}ni=1 there
is a unique process F : A ⊗ n → B satisfying Def. 2.16.
Proof. See App. A.1.
Next we can see that any theory with a classical interface has diagrammatic sums.
Intuitively, this provides another way to represent the branching structure of probabilistic processes, and so, it is represented by a summation operation which distributes over
diagrams. This is achieved by lifting the sum that exists in the classical subtheory to the
entire process theory.
Proposition 2.23. In a theory with classically controlled processes (Def. 2.16) we can
define a sum of processes (for any finite set of processes) as:
B

B

P

:=

fi

i

(8)

F

A

A

where F is the unique (Prop. 2.22) classically controlled process satisfying:
B

B

fi

=

.

F

A
i

(9)

A

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

16

<!-- page 17 -->
and
=

X

i

.

i

Note that for classical processes this is the same as the usual sum, and, hence, this extends
the classical sum to the rest of the process theory.
Proof. See App. A.2.
Note that this sum gives us a convenient way to represent the classically controlled
processes, specifically it is simple to confirm that we can write:
X

=

F

fi

i

i

(10)

The classical systems come equipped with a notion of discarding, and so, we can
characterise the causal subtheory for the classical part of the process theory. Like we did
with the summation, we will now show that we can lift this structure from the classical
subtheory to the whole process theory.
Proposition 2.24. If a theory has a local classical interface then there is a unique way to
characterise the processes in the full theory which are compatible with classical causality.
That is, we will see that we can define discarding maps by:
:=
A

τ0
A

and then all of the causal-compatible processes can be characterised by:
B

f
A

=

A

.

Proof. See App. A.3.
Given this notion of summation and the characterisation of the causal subtheory, we
can prove some basic properties regarding the state spaces of systems and the maps between them.
Proposition 2.25. In a theory with a classical interface (Post. 2), the states form a
finite-dimensional pointed convex cone. Processes then induce completely positive linear
maps between these cones. The causal states are defined by an intersecting hyperplane,
and causal processes preserve this hyperplane.
Proof. See App. A.4.
Remark 2.26. The systems therefore have much of the structure that is assumed in a
GPT [19, 67]. What we have not assumed or proved is the necessity of the convex cones
to be closed. For related work connecting these frameworks see, for example, [13, 65, 107,
114, 115, 117].
Remark 2.27. Note that many of the above results can easily be extended from states to
arbitrary processes. For example, the set of processes from A to B will generally form a
finite-dimensional proper cone, with a convex subset of causal processes, which are defined
by a set of linear equality constraints.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

17

<!-- page 18 -->
2.4 Leaks and purity
We will need the process-theoretic definition of purity first presented in [100], and for this
purpose we introduce the notions of dilations and leaks.
Definition 2.28 (Dilations). A dilation of a process f : A → B is a process g : A → B ⊗C
such that:
B

B

f

C

g

=
A

A

Definition 2.29 (Leaks). A leak is a dilation of the identity, that is, a process
A

L

A

such that
A
L

=

.
A

A

Note that when we have multiple leaks, we will typically label them with a different
colour.
Example 2.30 (Trivial leaks). A leak is said to be trivial if there exists a state s such
that
=

s

Note that any s which is causal will define a trivial leak in this way.
Example 2.31 (Broadcasting). A broadcasting map

is one that ‘leaks both ways’, that is:

=

=

It is well known that these do not exist for quantum systems (as demonstrated by the ‘nobroadcasting theorem’ [17]) whilst for classical systems they are defined by a stochastic
map whose action on the basis states is simply the ‘copier’:

:=

X j
j

j
j

=

s.t. ∀i

i

i

i

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

18

<!-- page 19 -->
We provide a formal classification of the leaks for quantum theory in Prop. B.1. HowL
ever, informally, the leaks for a quantum system A = i Ai can be seen as leaking the
‘which branch’ information. Therefore, for fully quantum systems all leaks are trivial,
whilst for classical systems all leaks are based on the aforementioned broadcasting map.
Informally, a process is pure if it plays nicely with leaks. More precisely we demand
that two independent conditions are satisfied for a process f to be pure. Firstly, that
any dilation, g, of a pure process, f , can be explained by leaks on the input and output
systems:
χ
!

f

g

=

=⇒

∃

, χ

,

g

:

f

=

Second, that pure processes do not interact with ‘leakable’ information, so leaking
before or after is equivalent:

∀

∃

and ∀

∃

f

:

=
f

These two conditions can be combined into a single simplified statement which we take
to be the definition of purity:
Definition 2.32 (Purity of processes). f is pure if and only if

f

=

g

∃

=⇒

&

g

:

f

=

=

(11)
f

This definition is motivated by the fact that it gives the right notion of purity of
processes both in quantum and classical theories [100]. Note that this definition is not
equivalent to commonly proposed definitions of purity based on notions of extremality in
the geometry of the space of processes. This is desirable as these more standard definitions
either deem the classical identity channel or the discarding map to be mixed. See [100] for
further discussion of this point. We characterize the pure processes for quantum theory in
Prop. B.2; in the case of fully quantum systems we obtain the standard notion of purity,
i.e. that the process has Kraus rank 1.
In the special case of states (or similarly for effects) we can obtain a much simpler
characterisation of purity by noting that a leak for a trivial system is simply a state
preparation for the leaked system:
L

L

=

l

Example 2.33. For states this definition of purity reduces to
f

=

g

=⇒ ∃

l

:

g

=

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

f

l

19

<!-- page 20 -->
This notion of purity was put forward by Chiribella in [28] which intuitively states
that a pure state is information that is independent of the surrounding context.
We now formalise the idea of a set of states prepared being pure and jointly distinguishable. This gives an important information-theoretic property of each system, namely,
the amount of classical information they can store reliably. Such states are described by a
particular type of causal state preparation S. Recall that causality for a state preparation
means:
A

=

S

.
n

n

It can be shown [100] that such a state preparation can only be pure if n = 1, that is, if
it is simply a state. However, we can capture the notion that each individual state in S is
pure by considering purity of the following diagram:
A

n

S
n
n

That is, the states prepared are pure if and only if the state preparation is pure when we
keep a record (the ancillary classical system) of which state was prepared.
Definition 2.34 (Testability). A causal state preparation S : n → A is said to be testable
if
A

n

S
n
n

is pure, and if there is a measurement (Def. 2.6) M such that
n

M
S
A

S

=
n

n

We say that the state preparation S is maximal testable (for a given system A) if n is
moreover maximal.
Example 2.35. In quantum theory the maximal testable state preparations correspond
to orthonormal bases of the Hilbert space. That is, given a quantum system M (Cn ), a
maximal testable set of states will correspond to a set of orthonormal projectors |iihi| ∈
L
M (Cn ). The maximal testable state preparation will then be some map S : ni=1 M (C) →
M (Cn ) :: |ii → |iihi|.

2.5 Cups, caps and sharp daggers
We now formalise what it means for a process theory to be ‘blind w.r.t. inputs and outputs’
i.e. that inputs can be ‘bent’ into outputs and vice versa, essentially relaxing the basic
constraints on forming diagrams for a process theory (cf. point 2. of Def. 2.1). In terms of
diagrams this is usually referred to as string diagrams [11, 43] or compact structure [1, 77].
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

20

<!-- page 21 -->
This ability to bend wires can also be represented within a process theory as a particular
bipartite state, the cup, and effect, the cap, for each system:
:=

and

:=

A detailed discussion can be found in [43, 44].
Definition 2.36 (Cups and caps). A theory has cups and caps if for each system it has
processes:
A

A

and

A

A

which satisfy:
=

=

,

=

and

(12)

Equivalently, this means that in diagrams inputs can be connected to inputs, outputs to
outputs, and also that loops are allowed.
Cups and caps have a very clear conceptual meaning: they assert that the theory has
‘maximal’ correlations. Firstly, that the theory must have correlations is easily shown by
a simple diagrammatic argument. Assume, for the sake of contradiction, that there are
no correlations, i.e. that all bipartite states separate:
=

s

s1

s2

then, in particular, the cup separates:
=

c1

c2

so we have:
c2

=

=

c1

c2

=
e

That is, all wires separate, so the theory does not permit any interactions, correlations or
evolution. We say that such a theory is trivial. Any non-trivial theory with cups must
therefore have correlations. Intuitively, maximality can then be deduced from the first of
Eqs. (12) in that ‘via a cup and cap an identity can be realised’, so that the cup and cap
must allow for a flow of all state-data at the input. Formally this intuition is substantiated
in [48].
Similarly to the above proof, it can now easily be seen that the cap cannot be causal,
confirming that this simple diagrammatic structure is lost when passing to the causal
subtheory. Indeed, if the cap were causal then the Eq. (2) becomes:
=

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

21

<!-- page 22 -->
and again all wires would separate and the theory would be trivial:
s

=

=

=

Consequently, non-trivial causal subtheories will not have cups and caps.
Example 2.37 (Quantum). For the quantum case the cups & caps realise the ChoiJamiolkowski isomorphism. That is, the cup and cap are (non-normalised) maximally
entangled states and effects respectively. More formally, the cup for a d-dimensional
system A is given by the super-normalised state written in Dirac notation as:
A

A

d
X

∼

|iiihjj|

i,j=1

similarly the cap is given by the same matrix but interpreted as a POVM element. For
L
general C*-algebras, e.g. A = k Ak where Ak are dk -dimensional quantum systems, we
can write the cup as:
A

A

=

M Ak

Ak

dk
M X

∼

k

d1
X

|iiihjj| =

k i,j=1

d1X
+d2

|iiihjj| +

i,j=1

|iiihjj| + · · ·

i,j=d1 +1

the cap is again given by the same matrix interpreted as a POVM element.
Example 2.38 (Classical). In the classical case these cups and caps are given by:
n

n

=

n
X
i=1

n
i

n

n

and

i

n

n
X
j

=

j

n

n

j=1

which corresponds to the super-normalised perfectly correlated state and effect. It is
simple to verify that these do indeed satisfy the relevant equations (Eqs. 12), for example:

=

j

X
ij

j

=
i

i

X
ij

i

δij

=
j

Cups and caps provide a way to swap inputs and outputs, and hence, an operation of
‘time-reversing’:
f

7→

f

In the case of quantum theory this corresponds to the transpose, but quantum theory
has a second manner of doing so, namely the adjoint, a.k.a. dagger [2, 101], which turns
Dirac kets into Dirac bras and vice versa. The difference between the transpose and the
dagger is the conjugate, and hence witnesses the non-trivial involution on the number field
of complex numbers. Hence having a dagger besides cups & caps is a truly fundamental
structure within quantum theory.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

22

<!-- page 23 -->
Definition 2.39 (Dagger). A dagger is a reflection of processes:
†

B

A

f

f
†

A

B

(where an asymmetry of the box shape has been introduced to make the reflection clear.)
In particular, it reflects the entire diagram structure:

†
(13)
†

Just as a Dirac bra can be seen as a ‘test’ for the corresponding ket, we would like
our general process-theoretic dagger to do the same, that is, the dagger of a state can be
interpreted as a test for that state [99], in that, for pure states, it uniquely identifies the
state with certainty:
ψ

⇐⇒

= 1

ρ

ρ

=

ψ

In [99] it was indeed shown that this sharpness assumptions lifts to a dagger structure
on all processes. This sharpness assumption then gives a clear conceptual meaning to the
dagger4 . Formally, we will assume this condition for every testable family of states, which
in diagrammatic terms means Eq. (14) below. Moreover, if S is maximal, then S † should
be causal, as it is a test where no other outcomes are possible.
Also, while in quantum theory testing is a non-trivial structure, due to the invasive
nature of measurements, in classical theory it is trivial, so we expect the dagger not to add
any new structure on classical processes, and hence to be a symmetry which is already
present due to the cups & caps.
Definition 2.40 (Sharp dagger). A dagger is sharp if for all testable (cf. Def. 2.34) causal
state preparations S, its dagger S † tests it, i.e.:
S
=

(14)

S
In addition, S is maximal if and only if S † is causal:

S

=

4
This is obviously distinct to the conceptual meaning of cups & caps – cups & caps being about
correlations whilst the sharp dagger is about tests and measurements. It is therefore surprising that within
classical theory the dagger can actually be constructed from the cups & caps as will be explicitly shown
in the following definition.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

23

<!-- page 24 -->
For classical processes this sharp dagger should be trivial, that is, it is given by the compact
structure:
f

=

f

(15)

Example 2.41 (Quantum). For quantum theory generally (including the fully quantum
and classical cases) the sharp-dagger is provided by the Hermitian adjoint.
Example 2.42 (Classical). As mentioned in the definition, for classical theory a sharp
dagger is provided by the compact structure, this can moreover be shown to be unique. It
is instructive to consider what this looks like for the matrix representation of a classical
process:

(f † )ji

X
ij

i

j

=
i

f

=

f

=

X
ij

f
j

i

=

j

X
ij

fji

j
i

We therefore find that (f † )ji = fji , that is, the dagger is just the matrix transpose.
Remark 2.43. This ‘sharpening’ of the dagger is essentially the same as the definition
given in [99], the main distinction being that here we consider general state preparation
procedures rather than just individual states.

3 The postulates
The first postulate provides the basic framework that we will use for the reconstruction.
This allows one to describe essentially any conceivable physical theory, in particular, as
we show later, encompassing the generalised probabilistic theory framework which has
recently served as the basis for other reconstructions such as [15, 34, 35, 53, 67, 69, 89, 90].
Postulate 1 (The theory is a process theory). As defined in Def. 2.1.
The second postulate provides a more operational layer to our theory, describing how
we interact with the world via classical inputs and outputs.
Postulate 2 (There is a finite local classical interface). As defined in Def. 2.14, where
all classically controlled processes exist, and there are sufficient causally-compatible local
tomographic tests, as defined in Defs. 2.19 and 2.20.
The next two postulates are based on standard compositional tools from CQM.
Postulate 3 (The theory has cups & caps). As defined in Def. 2.36.
Postulate 4 (There is a sharp dagger). As defined in Def. 2.40.
The final postulate will be defined and discussed in the following subsection. We also
include it here for completeness.
Postulate 5 (Every process has an essentially unique symmetric purification). As will be
defined in Def. 3.1.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

24

<!-- page 25 -->
Note that there is some interdependencies amongst these postulates. For example,
Postulates 2, 3, 4 & 5 are all process-theoretic so rely on Postulate 1, moreover, Postulates
4 & 5 rely on Postulate 2 as they are defined in terms of the discarding maps derived from
Postulate 2, finally, Postulate 5 also relies on Postulate 4 as it uses the dagger in it’s
definition.

3.1 Symmetric purification
The final postulate symmetrises the ‘standard’ purification postulate introduced in [33].
The standard purification postulate states: for all states ρ, there exists a pure bipartite
state ψ, such that:
=

ρ

ψ

.

Moreover, this purification is ‘essentially unique’ [35], that is, if there are two such purifications ψ and φ with the same purifying system, then they are related via a reversible5
transformation R:
R

φ

=

=

ρ

=⇒

ψ

=

φ

ψ

.

This notion of purification is problematic for us for two reasons. Firstly, it is not
compatible with the classical interface, as classical theory does not satisfy this postulate.
Secondly, it is formulated specifically in terms of states: we aim to treat all processes on an
equal footing, viewing them as more fundamental entities, states being special instances
thereof. In this section we therefore introduce the postulate of symmetric purification,
which resolves these issues. Symmetric purification stipulates that every process arises
from a pure process by ‘discarding’ a system to both ‘the future and the past’.
To produce a time-symmetric version of purification we need to have a notion of ‘discarding’ systems in the past. We can think of the standard discarding effect as an operational way to describe a scenario where we have no knowledge about, control over, or
interaction with the future of a system. However, we can also imagine a scenario where we
have no information about, no control over, and no interaction with the past of a system,
to represent this we use the time reverse (i.e. dagger) of the discarding (to the future)
map:
!†
A

:=

(16)

A

In the cases of quantum and classical theory, the dagger of the discarding map is an
unnormalised maximally mixed state (specifically 1). More explicitly, using the matrix
representation of classical theory and recalling that the classical dagger is nothing but the
transpose we find that:
=

X
i

i

and so

=

X

i

i

One may worry that this is not actually a valid state (i.e. is not normalised/causal),
however, discarding to the past is not something that we can ‘do in the lab’, and so it
should not correspond to a state we can actually prepare.
5

A transformation R is said to be reversible if an inverse R−1 exists and is physically realisable.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

25

<!-- page 26 -->
Definition 3.1 (Essentially unique symmetric purifications). If a process f : A → B can
be dilated to a pure process F : A ⊗ B → B ⊗ A as follows:
B

B

=

f

A

F

A

B

A

then we call F a symmetric purification of f . Moreover, such purifications are said to be
essentially unique, if any two purifications F, G : A ⊗ C → B ⊗ D are connected by a vise
R:
B

=

F
A

B

D
C

B

f
A

=

D

=⇒

G

F

=

G

R ,

(17)

C

A

where the ‘backwards leak’ is provided by the time-reverse (i.e. dagger) of a leak, and,
moreover, R must be ‘bi-causal’:

R

=

.

(18)

Symmetric purification expresses the requirement that all processes of the theory are
fundamentally pure, and the apparent lack of purity should arise from lacking information
about, and control over, the past and/or future of some environmental systems. Moreover,
the ‘essential uniqueness’ condition states that the purification is unique – any apparent
distinction can always be traced back to a change in the description of the environment.
As it is formulated, essentially unique symmetric purification provides a common
ground to explain the lack of purity in all systems in the process-theoretic description
of quantum theory, whether they be fully quantum, fully classical or more general hybrid
and composite systems. For a proof of this fact see App C.1.
Remark 3.2. Quantum theory actually satisfies a stronger form of symmetric purification
where we can demand also that F = F † , i.e. the purified process is invariant under timereversal. This strengthening however, whilst an interesting feature of quantum theory, is
not necessary for our reconstruction.

4 The reconstruction
A high-level overview of the structure of the reconstruction is provided in Fig. 1, showing
which postulates are necessary for each lemma, and how these are combined to reconstruct
quantum theory.
To begin let us consider how the sharp dagger interacts with the linear structure coming
from the classical interface (see Prop. 2.23).
Lemma 4.1. In a theory with a classical interface (Post. 2) and a sum defined as in
Prop. 2.23, the dagger is linear.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

26

<!-- page 27 -->
Process
Theory
Classical
Interface
Convex
Cones and
Linear
Maps
Discarding

GPT
Symmetric
Puriﬁcation

Sharp
Dagger
Homogeneity
Spectrality

Strong selfduality

Local
Tomography

EJA

Cups and caps

Quantum

No leaking ~ Purity of cups

Fully
quantum
systems

Figure 1: Flowchart outlining the structure of the reconstruction where the green rectangles correspond
to postulates and the blue ellipses to the lemmas and theorems constituting the proof. In the top section
we obtain something similar to the framework of generalised probabilistic theory. In the middle section we
reconstruct the process-theoretic description of quantum theory consisting of hybrid quantum-classical
systems. Finally, in the bottom section we give two equivalent routes to restrict to the fully quantum
systems.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

27

<!-- page 28 -->
Proof. First recall how we define the sum:
X

fi

i

:=

where, for all i

F

F

= fi

i

We can consider how the dagger interacts with this sum:

†

!

X
i











F 


=

F

=

= †

fi

X

X

=
i

=

F

i

F

i

X

=

F

i

fi

i

!

=

X

†

fi

(19)

i

This proves that the dagger is additive, to extend this to full linearity we can show that:
†

X
i

ri f
i

!

!

=

X

† ri

fi

(20)

i

!

=

X

†(ri ) †

fi

(21)

i

!

=

X

ri †

fi

(22)

i

where the first line follows from additivity of the dagger, the second from diagram preservation of the dagger, and the third from the fact that scalars are left invariant by the
dagger.
We now consider how various key features of the quantum state space arise from our
axioms. To begin with, we show that the state cones are homogeneous.
Definition 4.2 (Homogeneous cone). A convex cone C is homogeneous if for every pair
of vectors s1 , s2 internal to C, there exists a cone automorphism T such that T (s1 ) = s2 .
Lemma 4.3. If, in addition to the finite classical interface (Post. 2), the theory satisfies
symmetric purification (Post. 5), and has a sharp-dagger (Post. 4), then the state cone is
homogeneous (Def. 4.2).
Proof. We must show that, for any pair of internal states s1 and s2 , there exists a cone
automorphism T such that T (s1 ) = s2 . As T is reversible, this is equivalent to the
statement that there is a cone automorphism between a particular chosen internal state
and any other. For this proof we take the particular internal state to be the ‘discarding’
state. That the discarding state is internal follows from the fact that the dagger is linear,
provides an isomorphism between the state and effect cones, and that the discarding effect
is in the interior of the effect cone. This last point follows from the existence of causally
compatible tomographic tests. We proceed in two steps: firstly, we show that for any
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

28

<!-- page 29 -->
internal state there exists a process that maps the discarding state to it; secondly, that
this map is surjective on the cone and so —being linear by Prop. 2.23, and as the cones
are finite-dimensional— it is a cone automorphism.
The first part is a simple corollary of symmetric purification. Consider an arbitrary
internal state s, then its purification S provides a map from the states of A to itself taking
the discarding state to s:
A
A

S

=

s

A

For the second part, we adapt [35, Proposition 7] to show that S is surjective on the
cone.Note that as s is internal, then any state a is in some decomposition of s:
= p

s

+(1 − p)

a

ā

where p ∈ (0, 1). Therefore we can construct the following dilation σ of s where

0

and

are causal, perfectly distinguishable states of some system B 6 :

1

A

B

σ

= p

a

+(1 − p)

0

ā

1

This has a symmetric purification Σ, which is moreover a purification of s, hence we can
construct two purifications of s with the same input and output systems:
A

A
B

B

=

Σ
A

=

σ

B

1
NB

=

s

S
A

B

where NB := ◦ B is non-zero as the discarding map and its dagger are both internal
to their associated convex cones (see also the end of App. A.4 for an explicit proof that
NB is non-zero). Then, by the definition of symmetric purification, these are related by
some R as:
S

= N1B S

Σ

R

S

1
NB

=

:=

R

r

In the second step we use that S is pure and so, by the definition of pure processes, we
can replace the leak afterwards with a leak before. It is then clear that there is a state,
α, that is mapped to pa by S:
S
S
α

6

0

0

:=

r

=

Σ

0

=

σ

= p

a

Note that we can take B to be a classical bit to ensure that such states exist.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

29

<!-- page 30 -->
Hence, p1 α is mapped to a. As a is an arbitrary state, S is surjective on the cone,and
hence a cone automorphism. We therefore have homogeneity of the state cone.
Secondly, we show that state spaces satisfy spectrality.
Definition 4.4 (Spectrality). A theory is said to be spectral if any (causal) state can be
written as
=

s

S
p

where p is a (causal) classical state and S is a maximal testable state preparation (Def. 2.34).
Lemma 4.5. If, in addition to the finite classical interface (Post. 2) and the Homogeneity
from Lem. 4.3 (from Posts. 2 and 5), the theory has a sharp-dagger (Post. 4) then the
state cone is spectral (Def. 4.4).
Proof. Firstly note that, for any reversible transformation T that:
T
S

pure

S

=⇒

pure.

To see this consider an arbitrary dilation, D, of this process:
T
S

=

D

Any such dilation will also provide a dilation of the original process by composing it with
T −1 , that is:
TT−1
T
S

=

TT−1

S

=

D

As this original process is, by assumption, pure we therefore have:
l

−1
TT

S
D

=

l

=

S

where the first equality follows from the definition of purity (Def. 2.32) and the fact that
all classical leaks can be written in terms of the broadcasting map (see [100] for details).
The second equality follows from associativity of broadcasting. Hence, by composing this
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

30

<!-- page 31 -->
with T we find that this arbitrary dilation D, can be rewritten as a leak before or a leak
after the dilated process, i.e.:
l
T
T

S
=

D

=

l

S

Therefore, the conditions necessary such that the process is pure are satisfied.
Now to obtain spectrality, note that every system A must have a (generally non-unique)
maximal testable state preparation S : n → A (Def. 2.34) although it could be trivial (i.e.
n = 0). For such a maximal testable state preparation, by the definition of the sharp
dagger (Def. 2.40), we have:
S

=

and so taking the dagger of this equation we find that:
S

=

Using this together with homogeneity, means that for any internal state t, there exists a
reversible map T such that:
T

=

t

S
We then define a classical state and effect, p and p̄, by:

p̄

T
p

:=

=

and

S

respectively.

p

Note that, p̄ necessarily exists as p is an internal state. To see that p is indeed internal
note that this is equivalent to the statement that:
i

∀i

6= 0

p

Now, we can compute these scalars to be:
T

i
p

=

i

S

T
=

S

T
=

si

i

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

31

<!-- page 32 -->
where the first equality follows from the definition of p, the second from the definition of
the classical cup, and the third from the fact that S is a controlled state preparation. Note
that this means that the si are valid states and so live inside the state cone. Moreover,
note that T is a cone automorphism (see Def. 4.2) so must map these states to valid nonzero states, and as the hyperplane defined by ◦ s = 1 intersects the cone (see Prop. 2.23)
we find, for all i, that:
i

6= 0

T

=⇒

6= 0

T

si

=⇒

6= 0

p

si

Returning to our state of interest t we can now write it in the following form:
T
T

=

t

S

=

p̄

τ

:=

S

p
p

We can then define a perfectly distinguishing measurement by:

:=

M

S

p

TT−1
One may worry that T −1 is not guaranteed to be a physical transformation, however,
regardless, this measurement is well defined as each of the effects that make it up must
be physical (as T induces an automorphism on the effect cone so does T −1 ). Hence, this
measurement can then be defined as a classically controlled process. It is then simple to
check that the pair (τ, M ) satisfy the conditions for the sharp dagger. Firstly that τ is
causal:
T
τ

=

S

p̄

p

p̄

p̄

=

=

=
p

and secondly that M perfectly distinguishes the states of τ :

S
M

=
τ

p

TT−1

=

S

T
S

S

p̄

p

p

=
p̄

p̄

=

=

p̄

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

p

32

<!-- page 33 -->
Therefore the definition of the sharp dagger implies that τ is perfectly distinguished by
τ †:
τ
=
τ
Moreover τ is maximal as S was maximal and so:
τ

=

t

=

Therefore,
τ
p

satisfies the conditions of spectrality.
So far we have proved spectrality of the interior of the cone, we will now show that
this can be extended to the full cone, and moreover, the entire vector space in which the
cone lives. To do so we can adapt Corollary 21 from [34]. Note that any vector can be
written as the difference of two internal states which can each be spectrally decomposed:
=

v

s1

−

s2

τ1

=

−

τ2

r1

r2

Then define,


 i 
R := max
+ ,
i  r2 

where  > 0. Then
v

=

+R

τ1 − τ2 + R
r1

=

=

r2

τ1 − τ2 + R τ2
r1

r2

τ1 +

τ2

r1

R − r2

is a state as all of the elements of the classical vectors are strictly positive thanks to the
definition of R, and moreover, is internal as there is a decomposition of the state as s + 
where s is a vector in the cone. Therefore, as this is an internal state it has a spectral
decomposition:
v

+ R

=

τ3
r3

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

33

<!-- page 34 -->
and so we can write:
τ3 − R

=

v

r3

τ3 − R τ3

=

r3

τ3

=

r3 − R
τ3

:=

r

We therefore have spectral decompositions for arbitrary vectors.
Finally, we show that the state cones are strongly self dual.
Definition 4.6 (Strongly self dual cone). A convex cone C is strongly self dual if there
exists an inner product h , i on the vector space spanned by C, such that
x∈C

⇐⇒

hx, ci ≥ 0 ∀ c ∈ C.

Lemma 4.7. If, in addition to the finite classical interface (Post. 2) and Spectrality from
Lem. 4.5 (from Posts. 2,5 and 4), the theory has a sharp-dagger (Post. 4), then the state
cone is strongly self dual (Def. 4.6).
Proof. First we will show that the sharp-dagger provides an inner product defined as:
hs1 , s2 i :=

s1
s2

;

(23)

and secondly we show that the state cone is strongly self dual with respect to this inner
product. To show that this is a valid inner product, firstly, we check that this is symmetric:
hs1 , s2 i =



s1

(15)

=

s2

†

s1
s2



s2

(13)

=



s1

= hs2 , s1 i

Secondly that it is bilinear follows immediately from linearity of effects given by Lem. 2.25:
hs1 , αs2 + βs3 i =

α

s1
s2

+ β

s1

= αhs1 , s2 i + βhs1 , s3 i

s3

(24)

Finally, positivity follows easily from spectrality of arbitrary vectors:
r

τ

v

hv, vi =

=
v

r

≥ 0

=
τ

r

r

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

34

<!-- page 35 -->
where equality implies that r = 0 and hence v = 0. Eq. 23 therefore defines a valid inner
product.
Note that, if all elements of r are strictly positive, we have an internal state; if they
are non-negative, then we have a state; and if some are negative, then the vector cannot
be a state as it would give a negative probability for some effect. It is then simple to check
strong self-duality. Firstly, if s is an element of the state cone C, then hs, ci ≥ 0 for all
c ∈ C as hs, ·i = s† is an effect, and so it evaluates to a positive real number on the cone of
states. Conversely, if v 6∈ C, there is a negative coefficient in the spectral decomposition;
without loss of generality we label this element i. There then exists some c ∈ C such that
hc, vi < 0, that is:
i
c

hc, vi =

i

:=

τ

v

=

r

< 0

v

The state cone is therefore strongly self dual with respect to the inner product defined by
the sharp dagger.
These properties, in particular homogeneity and strong self duality, are well known
to get us close to quantum theory, specifically, by using the Koecher-Vinberg theorem
[61, 82, 111], we get that the state cones correspond to Euclidean Jordan Algebras (EJAs).
Theorem 4.8 (Koecher-Vinberg theorem). There is a one-to-one correspondence between
Euclidean Jordan Algebras and symmetric cones (convex cones that are closed, pointed,
homogeneous, and self-dual) with an appropriate choice of order unit [61].
Lemma 4.9. The systems in our theory (specifically, a process theory (Post. 1) satisfying
Posts. 2, 4 and 5) correspond to finite-dimensional Euclidean Jordan Algebras.
Proof. By using the Koecher-Vinberg theorem above we need simply to demonstrate that
our state cones are indeed symmetric cones, and hence also correspond to EJAs.
First note that given a cone C in a vector space V we define the dual cone by
C 0 := {v|v ∈ V s.t. hv, ui ≥ 0 ∀ u ∈ C}
This implies that the dual cone is closed as it is the intersection of closed half spaces, one
for each u ∈ C defined by hv, ui ≥ 0. Hence, strong self-duality implies that the state
cone must be closed too. This therefore follows for our systems from Lem. 4.7. Prop. 2.23
then implies that the cones are pointed, finite-dimensional and Lem. 4.3 that they are
homogeneous. Hence the state spaces are finite-dimensional symmetric cones. It therefore
immediately follows that each system in our theory corresponds to a finite-dimensional
EJA.
There is a well known classification result for finite dimensional EJAs [76]: they correspond to direct sums of five types of simple EJAs. There are two important properties of
each of these, their rank, which corresponds to the number of states in a maximal testable
state preparation, and their dimension, the minimal number of effects necessary for state
tomography.
i. Cn , the algebra of self-adjoint n × n complex matrices. These have rank n and
dimension n2 .

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

35

<!-- page 36 -->
ii. Rn , the algebra of self-adjoint n × n real matrices. These have rank n and dimension
n(n+1)
.
2
iii. Hn , the algebra of self-adjoint n × n quaternionic matrices. These have rank n and
dimension n(2n − 1).
iv. O3 , the algebra of self-adjoint 3 × 3 octonionic matrices. This has rank 3 and
dimension 33 .
v. SpinK , the spin factors. These have rank 2 and dimension K.
Note that for the spin factors in the case of K = 3 coincides with R2 , K = 4 with C2 and
K = 6 with H2 . Given this classification, we are in a position to ask which of these EJAs
is compatible with our compositional structure. Before that, we will prove the following
useful lemma which will be useful for the proof:
Lemma 4.10 (Generalised no-restriction hypothesis). Cups & caps (Post. 3) imply that
our theories (satisfying Posts. 1, 2, 4 and 5) satisfy a generalised version of the norestriction hypothesis [33]. If a process is logically possible, then it is physically possible.
Proof. A process f is said to be logically possible, if for all states ψ, effects φ, and auxillary
systems C it results in positive scalars:
φ
B

≥0

f

(25)

C

A

ψ
Now, as this is true for all ψ, then strong-self duality implies that:
φ
B

(26)

f
A

C

is a valid, physical, effect for any φ and C. In particular, this means that:

B

(27)

f
A

B

is a physical effect, and hence we can use cups & caps to show that f must also be physical:
B

B

B

=

f
B
A

(28)

f
A

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

36

<!-- page 37 -->
Theorem 4.11. Given that state cones correspond to EJAs (Lem. 4.9 from Posts. 1, 2,
4 and 5) and that the theory satisfies the generalised no restriction hypothesis (Lem. 4.10
from Posts. 1, 2, 3, 4 and 5)), then local tomography (Post. 2, Def. 2.20) and the existence
of cups & caps (Post. 3) restrict us to quantum theory (Ex. 2.4).
Proof. First note that ⊗ is bilinear, and so distributes over ⊕. If we have some systems
L
L
A and B which decompose into simple components as A = i Ai and B = j Bj then
L
A ⊗ B = ij Ai ⊗ Bj . This structure is most suitably captured by noting that for such
systems the identity decomposes as the sum of orthogonal projectors, one for each of the
simple components:
=

P

(29)

i Πi

A

note that these projectors are necessarily physical due to lemma 4.10. Consider the comL
posite of a system A with itself, then we obtain A ⊗ A = ij Ai ⊗ Aj or diagrammatically:
=
A

P

Πj

ij Πi

(30)

A

What we want to show is that this is the most refined decomposition of the composite
system, in other words, that Ai ⊗ Aj are simple. Without loss of generality let us consider
the component A1 ⊗ A1 and show that this must be simple. For the sake of contradiction,
let us assume that A1 ⊗ A1 = B ⊕ C, diagrammatically:
=

Π1 Π1

ΠB

+

(31)

ΠC

which means that we can decompose the identity for the composite system as:
=

ΠB

A A

+

ΠC

+

P

ij

Πi Πj

=:

ΠB

+

ΠC

+

ΠX
(32)

where the sum is understood as running over all pairs (i, j) except i = j = 1.
We can use this to define a leak ∆ for system A by:

∆

:=

ΠB

0

+

ΠC

1

+

ΠX

2

It is straightforward to check that this is indeed a leak, and moreover, using the orthogonality of the projectors Π and recalling that sums distribute over diagrams, it is not hard
to show that:
∆
=

∆

(33)

∆

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

37

<!-- page 38 -->
Now consider the effect of the leak on pure causal states χ. The definition of purity
immediately implies that:
=

∆

χ

(34)

ρχ

χ

Now we can define orthogonal projectors πbχ , πcχ and πxχ by:

0

ρχ

=

=: πbχ

ΠB

1

,

=

ρχ

χ

ΠC

=: πcχ

(35)

χ

and
2

=

ρχ

=: πxχ

ΠX

(36)

χ

where to see that these are orthogonal projectors we use Eq. (33) to note that
j

i

j

i

∆
=
∆

∆
χ

χ

and then we can use Eq. (34) to rewrite this as:

j
χ

i

ρχ

= δij χ

ρχ

i

ρχ

and finally, use the definition of the projectors (Eq. (35)) to conclude that
πjχ
πiχ

= δij πiχ

that is, the processes are indeed orthogonal projectors. It is easy to see, that as ΠA +ΠB +
ΠX = 1A⊗A that πaχ + πbχ + πxχ = 1A , that is, they define a decomposition A = a ⊕ b ⊕ x.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

38

<!-- page 39 -->
Next let us examine πxχ , if we insert the definition of ΠX then we find that:
ΠX =

πxχ =

P

ij Πi

χ

Πj

(37)

χ

recalling that the sum over i and j avoids the case where i = j = 1 we therefore have:

=

πxχ

P

j6=1 Πj

(38)

and therefore that:
Π1

πaχ

=

πbχ

+

(39)

that is, we have a decomposition A1 = a ⊕ b. However, by assumption A1 is simple,
therefore it must be the case that either A1 = a and b = 0 or A1 = b and a = 0. On
the level of projectors this means either, that πaχ = Π1 and πbχ = 0, or, that πbχ = Π1 and
πaχ = 0. Which we can lift to the definition of the projectors on the joint system as saying
that, for each χ ∈ A1 that either
ΠB

= 0

or

ΠC

χ

= 0

(40)

χ

but not both. By symmetry we can similarly argue that, for each χ0 ∈ A1 that either
ΠB

= 0

or

ΠC

χ0

= 0

(41)

χ0

but not both. Next, without loss of generality, consider some χ such that:
ΠB

= 0

χ0

This means that
∀χ0 ∈ A1
χ

=⇒

= 0

ΠB

∀χ0 ∈ A1

=⇒

∀χ ∈ A1

χ0

6= 0

(42)

χ0

χ

ΠC

6= 0

ΠC

=⇒ ∀χ0 ∈ A1

ΠB

χ0

= 0

(43)

χ0

Moreover, it is clear that this last statement holds also for χ0 ∈
arbitrary states, hence, local tomography, implies that
ΠB

L

j>1 Aj hence is true for

= 0

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

39

<!-- page 40 -->
We therefore have A1 ⊗ A1 = B ⊕ C = C and so A1 ⊗ A1 is not decomposable. This
contradicts our initial assumption. Hence, if Ai and Aj are simple then so is Ai ⊗ Aj .
The second main step in our proof is to note that Dim[A ⊗ A] = Dim[A]2 which follows
from local tomography. We will moreover show that Rank(A ⊗ A) = Rank(A)2 . It is clear
that Rank(A ⊗ B) ≥ Rank(A)Rank(B) as given a set of perfectly distinguishable states for
Rank(A)
Rank(B)
A, {sA
and a set and perfectly distinguishable states for B, {sB
then the
i }i=1
j }j=1
A
B
set {si ⊗ sj } defines a set perfectly distinguishable states for A ⊗ B. We then know that
(using tomographic locality):
=
A⊗B

A

B

and as the discarding map is an internal effect we have a spectral decomposition of this
effect given by the composite of the spectral decomposition of the two individual discarding
maps. Hence, Rank(A ⊗ B) ≤ Rank(A)Rank(B), the conjunction of these two inequalities
then gives the required result.
Finally, we will show that the above results imply that the only EJAs that we can
consider are C* algebras. Again consider the decomposition of A into simple components,
L
L
A = i Ai and consider the self composite of this A ⊗ A = ij Ai ⊗ Aj . Our first result
shows that Ai ⊗Aj must be simple, and our second result puts constraints on the dimension
and rank of these simple EJA. In particular, let us consider the summand A1 ⊗ A1 . If
we let A1 = Hn then we find that Hn ⊗ Hn must be a simple EJA with Rank = n2 and
Dim = n2 (2n − 1)2 , it is straightforward to check that this does not exist for any integer
n > 1. herefore, the quaternionic case is ruled out. Next we turn to the real case, Rn ⊗ Rn
2
2
and see that this requires a simple EJA with Rank = n2 and Dim = n (n+1)
it is again
4
straightforward to check that this does not exist for any integer n > 1. Considering the
octonionic case we have for O3 ⊗ O3 that Rank = 32 and Dim = 36 it is easy to check
that there is no such simple EJA. Finally we consider the spin factors SpinK ⊗ SpinK
which require that Rank = 4 and Dim = K 2 . We find a solution here only for the case
that K = 4, however, this is the situation when Spin4 = C2 i.e. the cone is the Bloch
ball. Hence, the only summands which can compose in the correct way are Cn . We can
then check that the standard quantum tensor product i.e. Cn ⊗ Cm := Cnm is the only
choice consistent with our constraints as it has Rank = nm and Dim = n2 m2 as required.
Therefore we have shown that the only EJAs which satisfy our postulates are those of the
L
form i Cni , i.e., those that are C* algebras.
We have therefore demonstrated that the state spaces of our systems correspond to
the state spaces of C*-Algebras; moreover processes in our theory from a system A to B
correspond to the set of all CP maps between the associated C*-Algebras. We know that
processes must be CP maps (they are linear and map bipartite states to bipartite states).
All that needs to be proved is that every CP map corresponds to a process in the theory.
This is exactly what we showed in Lem. 4.10.
This completes the reconstruction as we have demonstrated that our postulates are
equivalent to systems being finite-dimensional C*-algebras and processes being completely
positive trace-preserving maps between them: this is precisely the process-theoretic description of quantum theory (Ex. 2.4) we were aiming for. Note that this does not mean
that every C*-algebra is necessarily in the theory, for example, classical theory satisfies
all of our postulates, as does the theory made up of classical theory together with tensors
and direct sums of qubits. This, however, should be the target of a reconstruction. A
reconstruction should tell us what can exist not what does exist. Indeed, this is precisely
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

40

<!-- page 41 -->
what we have in traditional presentations of quantum theory, we are told that to every
physical system there is an associated Hilbert space, not that to every Hilbert space there
is an associated physical system.

5 Distinguishing quantum and classical systems
In the previous section, we reconstructed the full process-theoretic description of quantum
theory. However, it is still of interest to ask the question: how can we single out the fully
quantum and classical subtheories? We now introduce two novel ways to do this, and,
moreover, demonstrate that they are equivalent for any process theory with cups & caps.
Proposition 5.1. The purity of cups (and/or caps) restricts us to quantum systems.
Proof. In Ex. 2.37 we defined the cup for C*-algebraic systems. It is simple to see that
this has the following dilation:
A

A

M

=

Ak

Ak

M

=

Ak

Ak
k

k

k

where {k} is some set of perfectly distinguishable states. Considering the definition of
purity for states (Ex. 2.33), we find that for the cup to be pure, any dilation must separate.
This is the case only if k takes a single value, hence it is pure if and only if the C*-algebra
has a single summand, that is, when it is a fully quantum system.
In other words, it is really the existence of correlations mediated by pure states (and/or
effects) that is the distinguishing feature of quantum theory. Any other apparently odd
feature of quantum theory should, in principle, be able to be traced back to this.
Proposition 5.2. The triviality of leaks restricts to quantum systems.
Proof. For quantum theory all leaks are trivial, and for any other C*-algebra, we can
construct a non-trivial leak by leaking the ‘which branch’ information. That is,

=
A

M
k

=
Ak

M
k

k

:=

Ak

A

is trivial only when k takes a single value and the system is fully quantum.
This can be seen as a generalised no-broadcasting theorem, or, that information gain
always causes disturbance of a quantum system. This does not seem to be a particularly
surprising feature of nature. At least, as soon as one takes the view that measurements
are physical and should be described by an interaction between systems. Then, even going
back to Newton, it is not surprising that a measurement should have an impact on the
system being measured.
The fact that we have these two ways to characterise fully quantum systems is also
not surprising, for it can generally be shown that:
Proposition 5.3. For any process theory with cups & caps, purity of the cup (or cap) is
equivalent to the triviality of all leaks.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

41

<!-- page 42 -->
Proof. Firstly note that there is a one-to-one correspondence between the leaks for a
system and dilations of the cup. That is, any leak, l, will define a dilation of the cup, L
as:
:=

L

l

Moreover, any dilation, S, of the cup will define a leak, s as:
s

:=

S

Then it is clear, that if the leak is trivial then the corresponding dilation factorises and
vice versa:
S

=

ψ

⇐⇒

s

=

ψ

Triviality of all leaks is therefore equivalent to factorisation of all dilations of the cup.
This is precisely what it means for the cup to be pure (see Ex. 2.33). The proof for the
cap proceeds similarly.
Similarly to how we have singled out the quantum systems, one could ask how the
classical systems can be distinguished. Intuitively, these can be seen as those that are
maximally leaking, and which have the minimally pure cups & caps. All of the other
systems therefore have intermediate strength of leaks and intermediate purity of cups
& caps. To formalise this notion, we would have to introduce a measure of purity (for
example tr(ρ2 )) and a measure of strength of leaks (for example the quality of a leak
[100]). It is interesting to note that fully quantum systems are much easier to single out
from this perspective —as they do not require us to introduce such measures— and so,
the fully quantum theory appears to be, in some sense, the more fundamental, or natural,
subtheory.

6 Related work
6.1 Purification
In [100] we showed that leaks must be taken into account when defining purity for general
processes in general process theories. In particular, in the case of classical theory, this
refined definition is essential for purity of the identity process. Given this notion of purity,
we can define the symmetric purification postulate, which holds for both quantum and
classical theory.
The essential component of the standard purification postulate, for distinguishing
quantum and classical theory, is the purity of the cup. Indeed, we can show that the
conjunction of symmetric purification, and the existence of a pure cup, implies the standard purification postulate.
Proposition 6.1. Any theory with symmetric purifications and pure cups satisfies the
standard purification postulate.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

42

<!-- page 43 -->
Proof. Firstly we note that given a symmetric purification F of any process f , we can
bend the ‘discarded’ input into an output using a cup:
B

B

=

f
A

B

A

=

F

B

B

:=

F

B

A

A

A⊗B

F

A

A

so F provides a standard purification for f .
An alternative way of viewing this is that the pure cups & caps available for fully
quantum systems, allow us to arbitrarily interchange uncertainty about the past, and
uncertainty about the future. In contrast, in classical theory past uncertainty and future
uncertainty play distinct roles.
One may wonder whether we can obtain the standard ‘essential uniqueness’ property
in a similar way. This turns out to be the case in theories where processes are reversible
if and only if they are pure and causal. For such theories we have:
Proposition 6.2. Any theory with pure cups, essentially unique symmetric purifications,
in which pure causal processes are reversible has essentially unique standard purifications.
Proof. Note that any purification can be considered as a symmetric purification where the
input system is trivial:
B

B

=

f

=

F

A

B

C

C

F

A

I

A

Therefore, if we have two such purifications F and G then the essential uniqueness condition of symmetric purification implies that:
C
B

C

F
A

B

=

R
G

A

where R is a pure causal process. By assumption, this means that R is reversible and
hence this is precisely the standard essential uniqueness condition for purification.
Whilst this assumption that pure causal processes are reversible may seem natural
—as it holds in the cases of quantum and classical theory where the pure causal processes
are respectively unitaries and permutations— it does not hold for general theories. For
instance, take the process theory to be a restricted form of quantum theory, which has
the same states and measurements as quantum theory, but a restricted set √
of dynamics.
Specifically, restricting to a single unitary which is a rotation about Z of √2π. In this
theory we can generate other rotations, but they will all be by an angle of n 2π, and so,
we can never reverse a transformation. That is, we have unitaries that are pure and causal
but are not reversible.
If we want to obtain the standard essential uniqueness property precisely we could
have assumed that the vise R was reversible. However, this was stronger than necessary
for the reconstruction, so we did not make that assumption there.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

43

<!-- page 44 -->
6.2 GPTs
The most recent reconstructions of quantum theory have been in the generalised probabilistic theory (GPT) framework. These typically describe systems as finite-dimensional,
regular, closed cones, along with an intersecting hyperplane specifying the normalised
states. Transformations are then described as linear maps and, in particular, effects are
linear functionals on the state space. In Prop. 2.23 of our reconstruction we obtain the
essence of this structure from our classical interface. In fact, our classical interface can
be interpreted as representing the probabilistic layer of the GPT framework in a processtheoretic manner.
This classical interface however, does not provide all of the structure of the GPT
framework. Specifically, we do not obtain that the state space is closed. This is typically
assumed in the study of GPTs. Closure is —from an operational perspective— a very
natural assumption, as, up to any finite error, a state space should be indistinguishable
from its closure. However, it is not clear yet how this property should be understood from
the process theoretic perspective.
Despite the lack of closure, we are still able to use some tools commonly found in
the GPT literature—in particular the Koecher-Vinberg theorem. To do this, we focused
on the states of the theory. However, our postulates apply equally well to arbitrary
processes, and so, many of our results can immediately be generalised. We have omitted
such generalisations in an attempt to keep the mathematics of the paper to a minimum,
and present only the results that directly pertain to the reconstruction.

6.3 CPTs
The formalism of Cateogrical Probabilistic Theories (CPTs) [65] is another route to subsuming the GPT framework under a categorical or process-theoretic framework. CPTs
are closely related to the conjunction of postulates 1 and 2, that is, a process theory with
a classical interface. Specifically a CPT is defined (Def. 1 of [65]) as a process theory
subject to three mathematical requirements. The first of these is part of the definition of
a classical interface, whilst the second two can be derived from the classical interface.
The classical interface is a mathematically strictly stronger assumption, as the CPT
structure can be derived from it, but there are elements of the classical interface that
cannot be derived from the CPT structure. For instance, the existence of all classicallycontrolled processes is not a feature of a generic CPT. However, the classical interface has a
clear physical interpretation, whilst the requirements of a CPT (in particular requirement
2) do not. One direction for future work is to further explore the connections between
these two formalisms. For example, to determine exactly what must be added to the CPT
formalism to derive the existence of a classical interface.

7 Future work
Whilst the postulates of this reconstruction are diagrammatic the proof at times utilises
some standard linear algebraic techniques. Moreover, whilst the postulates are defined
at the level of processes we often only use them in the context of states. These are,
to some extent, against the spirit of process theories, as such, it would be interesting
in future work to try to make the proof of the reconstruction process-theoretic along
with postulates. Indeed, as discussed earlier, it seems plausible that, by using the full
strength of the postulates, there may be a much simpler and more direct way to go about

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

44

<!-- page 45 -->
the reconstruction. Another more recent categorical reconstruction of quantum theory
[108, 109] may help providing a route to this.
As with all reconstructions, we assume the existence of a classical interface for the
theory representing how we interact with the world, for example, deciding the experiments
to perform, and obtaining classical data as outputs. However, at some level we expect
this classical interface to be an emergent feature of quantum theory, and so it would be
interesting to see if we can move beyond this probabilistic approach. Can we instead
express everything in diagrammatic terms, and find some replacement for the classical
interface? For example, can we capture the copiability and deletability of classical data
via ‘spiders’ [43, 45, 47]?
A second issue with the classical interface (as it is defined here) is that it immediately
limits the scope of the reconstruction to finite dimensional quantum theory. It would
be interesting to see whether our axioms could reconstruct quantum theory even if we
removed this limitation, that is, if we removed the ‘finite’ part of finite tomography. If
not, it would be interesting to explore these alternative theories and how close they are to
quantum theory. One potential approach to this would be to follow the works of [63, 64]
or of [3, 4, 41], which demonstrate how to extend various diagrammatic features —such
as cups & caps— to the infinite dimensional setting.
There are many recent results in quantum foundations and in quantum information
[16, 28–32, 83–85, 103] which use the standard notion of purification in the derivation but
where the result is also valid in classical theory. It therefore seems plausible that the same
results could be obtained using our notion of symmetric purification, and so, apply to a
wider range of theories. Another recent research direction in quantum foundations is in
formulating quantum theory in a causally neutral [86, 94] or time symmetric [5, 93] way
or with indefinite causal order [9, 23, 27, 68, 78]. This notion of purification may be more
applicable in such situations as it does not distinguish between input and output systems.
We presented the cups & caps of postulate 3 as a relaxation of a basic process-theoretic
constraints on compositionality by freely allowing inputs to be connected to inputs and
outputs to be connected to outputs. One could equally ask what structure we obtain if we
relax the other constraints on compositionality. In particular, relaxing the constraint that
only pairs of inputs, and outputs are connected means that we need some sort of notion
of ‘multi-wires’. This naturally gives the structure of ‘spiders’ described in [43]. Moreover,
allowing for different system types to be connected leads to many other typical quantum
processes. It is the subject of ongoing work to investigate how much of the structure of
quantum theory can be described in such terms, and, how to reconcile such a perspective
with causality and the classical interface.

Acknowledgements
The authors would like to thank Markus Müller for helpful comments on an earlier draft of
the paper which have significantly improved the clarity of the presentation. The authors
would also like to thank Jon Barrett, Matty Hoban, David Jennings, Ciarán Lee, Kenji
Nakahira, Miguel Navascués, Rob Spekkens, and Sean Tull for useful comments and suggestions. The authors would also like to thank the referees whose careful reading and
insightful comments greatly improved the manuscript twice.
CMS acknowledges the support by the Pacific Institute for the Mathematical Sciences,
by a Faculty of Science Grand Challenge Award at the University of Calgary, EPSRC doctoral training grant and by Oxford-Google DeepMind Graduate Scholarship. JHS acknowledges the support of EPSRC via the Controlled Quantum Dynamics Centre for Doctoral
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

45

<!-- page 46 -->
Training and the Perimeter Institute for Theoretical Physics. Research at Perimeter Institute is supported by the Government of Canada through the Department of Innovation,
Science and Economic Development Canada and by the Province of Ontario through the
Ministry of Research, Innovation and Science. This research was also supported in part by
the Foundation for Polish Science through IRAP project co-financed by EU within Smart
Growth Operational Programme (contract no. 2018/MAB/5). This project/publication
was made possible through the support of a grant from the John Templeton Foundation.
The opinions expressed in this publication are those of the author(s) and do not necessarily
reflect the views of the John Templeton Foundation.

References
[1] S. Abramsky and B. Coecke. A categorical semantics of quantum protocols. In the
19th Annual IEEE Symposium on Logic in Computer Science, pages 415–425, 2004.
DOI: 10.1109/LICS.2004.1319636.
[2] S. Abramsky and B. Coecke. Abstract physical traces. Theory Appl. Categ., 14:
111–124, 2005.
[3] S. Abramsky and C. Heunen. H*-algebras and nonunital Frobenius algebras: first
steps in infinite-dimensional categorical quantum mechanics. Clifford Lect., 71:1–24,
2012.
[4] S. Abramsky, R. Blute, and P. Panangaden. Nuclear and trace ideals in tensored
*-categories. J. Pure Appl. Algebra, 143(1-3):3–47, 1999. DOI: 10.1016/s00224049(98)00106-6.
[5] Y. Aharonov, S. Popescu, and J. Tollaksen. A time-symmetric formulation of quantum mechanics. Physics Today, 63(11):27–32, 2010. DOI: 10.1063/1.3518209.
[6] E. M. Alfsen and F. W. Shultz. State spaces of Jordan algebras. In Geometry of State
Spaces of Operator Algebras, pages 139–189. Springer, 2003. DOI: 10.1007/978-14612-0019-2˙5.
[7] E. M. Alfsen and F. W. Shultz. Geometry of state spaces of operator algebras.
Mathematics: Theory & Applications. Birkhäuser, Basel, 2003. DOI: 10.1007/9781-4612-0019-2.
[8] H. Araki. On a characterization of the state space of quantum mechanics. Commun.
Math. Phys., 75(1):1–24, 1980. DOI: 10.1007/bf01962588.
[9] M. Araújo, A. Feix, M. Navascués, and Č. Brukner. A purification postulate for
quantum mechanics with indefinite causal order. Quantum, 1:10, 2017. ISSN 2521327X. DOI: 10.22331/q-2017-04-26-10.
[10] Miriam Backens, Hector Miller-Bakewell, Giovanni de Felice, Leo Lobski, and John
van de Wetering. There and back again: A circuit extraction tale. Quantum, 5:421,
3 2021. ISSN 2521-327X. DOI: 10.22331/q-2021-03-25-421.
[11] J. C. Baez and M. Stay. Physics, topology, logic and computation: a Rosetta stone.
In B. Coecke, editor, New Structures for Physics, Lecture Notes in Physics, pages
95–172. Springer, 2011. DOI: 10.1007/978-3-642-12821-9˙2.
[12] H. Barnum and A. Wilce. Local tomography and the Jordan structure of quantum
theory. Found. Phys., 44(2):192–212, 2014. DOI: 10.1007/s10701-014-9777-1.
[13] H. Barnum, R. Duncan, and A. Wilce. Symmetry, compact closure and dagger
compactness for categories of convex operational models. J. Philos. Log., 42(3):
501–523, 2013. DOI: 10.1007/s10992-013-9280-8.
[14] H. Barnum, C. P. Gaebler, and A. Wilce. Ensemble steering, weak self-duality, and

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

46

<!-- page 47 -->
the structure of probabilistic theories. Found. Phys., 43(12):1411–1427, 2013. DOI:
10.1007/s10701-013-9752-2.
[15] H. Barnum, M. P. Müller, and C. Ududec. Higher-order interference and singlesystem postulates characterizing quantum theory. New J. Phys., 16(12):123029,
2014. DOI: 10.1088/1367-2630/16/12/123029.
[16] H. Barnum, C. M. Lee, C. M. Scandolo, and J. H. Selby. Ruling out higher-order
interference from purity principles. Entropy, 19(6):253, 2017. ISSN 1099-4300. DOI:
10.3390/e19060253. URL http://dx.doi.org/10.3390/e19060253.
[17] Howard Barnum, Carlton M Caves, Christopher A Fuchs, Richard Jozsa, and Benjamin Schumacher. Noncommuting mixed states cannot be broadcast. Physical
Review Letters, 76(15):2818, 1996. DOI: 10.1103/physrevlett.76.2818.
[18] Howard Barnum, Matthew A. Graydon, and Alexander Wilce. Composites and
categories of Euclidean Jordan algebras. Nov 2020. DOI: 10.22331/q-2020-11-08359.
[19] J. Barrett. Information processing in generalized probabilistic theories. Phys. Rev.
A, 75(3):032304, 2007. DOI: 10.1103/PhysRevA.75.032304.
[20] J. S. Bell. On the Einstein-Podolsky-Rosen paradox. Physics, 1(3):195–200, 1964.
DOI: 10.1103/physicsphysiquefizika.1.195.
[21] S. Bergia, F. Cannata, A. Cornia, and R. Livi. On the actual measurability of
the density matrix of a decaying system by means of measurements on the decay
products. Found. Phys., 10(9-10):723–730, 1980. DOI: 10.1007/BF00708418.
[22] O. Bratteli. Inductive limits of finite dimensional C*-algebras. Trans. Am. Math.
Soc., 171:195–234, 1972. DOI: 10.2307/1996380.
[23] Č. Brukner. Bounding quantum correlations with indefinite causal order. New J.
Phys., 17(8):083034, 2015. DOI: 10.1088/1367-2630/17/8/083034.
[24] A. Budiyono and D. Rohrlich. Quantum mechanics as classical statistical mechanics
with an ontic extension and an epistemic restriction. Nat. Commun., 8(1):1306,
2017. DOI: 10.1038/s41467-017-01375-w.
[25] Titouan Carette, Dominic Horsman, and Simon Perdrix. SZX-Calculus: Scalable Graphical Quantum Reasoning. In Peter Rossmanith, Pinar Heggernes,
and Joost-Pieter Katoen, editors, 44th International Symposium on Mathematical
Foundations of Computer Science (MFCS 2019), volume 138 of Leibniz International Proceedings in Informatics (LIPIcs), pages 55:1–55:15, Dagstuhl, Germany,
2019. Schloss Dagstuhl–Leibniz-Zentrum fuer Informatik. ISBN 978-3-95977-1177. DOI: 10.4230/LIPIcs.MFCS.2019.55. URL http://drops.dagstuhl.de/opus/
volltexte/2019/10999.
[26] N. Chancellor, A. Kissinger, S. Zohren, and D. Horsman. Coherent parity check
construction for quantum error correction. arXiv:1611.08012 [quant-ph], 2016.
[27] G. Chiribella. Perfect discrimination of no-signalling channels via quantum superposition of causal structures. Phys. Rev. A, 86(4):040301, 2012. DOI: 10.1103/physreva.86.040301.
[28] G. Chiribella. Distinguishability and copiability of programs in general process
theories. Int. J. Softw. Inform., 8:209–223, 2014.
[29] G. Chiribella and C. M. Scandolo. Entanglement and thermodynamics in general
probabilistic theories. New J. Phys., 17(10):103027, 2015. DOI: 10.1088/13672630/17/10/103027.
[30] G. Chiribella and C. M. Scandolo. Operational axioms for diagonalizing states. In
C. Heunen, P. Selinger, and J. Vicary, editors, Proceedings of the 12th International
Workshop on Quantum Physics and Logic, Oxford, U.K., July 15-17, 2015, volume

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

47

<!-- page 48 -->
195 of Electronic Proceedings in Theoretical Computer Science, pages 96–115, 2015.
DOI: 10.4204/EPTCS.195.8.
[31] G. Chiribella and C. M. Scandolo. Entanglement as an axiomatic foundation for
statistical mechanics. arXiv:1608.04459, 2016.
[32] G. Chiribella and C. M. Scandolo. Microcanonical thermodynamics in general physical theories. New J. Phys., 19(12):123043, 2017. DOI: 10.1088/1367-2630/aa91c7.
[33] G. Chiribella, G. M. D’Ariano, and P. Perinotti. Probabilistic theories with purification. Phys. Rev. A, 81(6):062348, 2010. DOI: 10.1103/physreva.81.062348.
[34] G. Chiribella, G. M. D’Ariano, and P. Perinotti. Informational derivation of quantum
theory. Phys. Rev. A, 84(1):012311, 2011. DOI: 10.1103/physreva.84.012311.
[35] G. Chiribella, G. M. D’Ariano, and P. Perinotti. Quantum Theory: Informational
Foundations and Foils, chapter Quantum from Principles, pages 171–221. Springer
Netherlands, Dordrecht, 2016. ISBN 978-94-017-7303-4. DOI: 10.1007/978-94-0177303-4“˙6.
[36] R. Clifton, J. Bub, and H. Halvorson. Characterizing quantum theory in terms
of information-theoretic constraints. Found. Phys., 33:1561–1591, 2003. DOI:
10.1023/A:1026056716397.
[37] B. Coecke. Kindergarten quantum mechanics: Lecture notes. In AIP Conference
Proceedings, volume 810, pages 81–98. AIP, 2006. DOI: 10.1063/1.2158713.
[38] B. Coecke. Quantum picturalism. Contemp. Phys., 51(1):59–83, 2010. DOI:
10.1080/00107510903257624.
[39] B. Coecke. A universe of processes and some of its guises. Deep Beauty: Understanding the Quantum World through Mathematical Innovation, pages 129–186,
2011. DOI: 10.1017/CBO9780511976971.004.
[40] B. Coecke. Terminality implies non-signalling. In B. Coecke, I. Hasuo, and P. Panangaden, editors, Proceedings of the 11th workshop on Quantum Physics and Logic,
Kyoto, Japan, 4-6th June 2014, volume 172 of Electronic Proceedings in Theoretical Computer Science, pages 27–35. Open Publishing Association, 2014. DOI:
10.4204/EPTCS.172.3.
[41] B. Coecke and C. Heunen. Pictures of complete positivity in arbitrary dimension.
Inf. Comput., 250:50–58, 2016.
[42] B. Coecke and A. Kissinger. Categorical quantum mechanics I: causal quantum processes. In E. Landry, editor, Categories for the Working Philosopher. Oxford University Press, 2016. DOI: 10.1093/oso/9780198748991.001.0001. arXiv:1510.05468.
[43] B. Coecke and A. Kissinger. Picturing Quantum Processes: A First Course in Quantum Theory and Diagrammatic Reasoning. Cambridge University Press, Cambridge,
2017. DOI: 10.1017/9781316219317.
[44] B. Coecke and É. O. Paquette. Categories for the practicing physicist. In B. Coecke, editor, New Structures for Physics, Lecture Notes in Physics, pages 167–271.
Springer, 2011. DOI: 10.1007/978-3-642-12821-9˙3.
[45] B. Coecke and D. Pavlović.
Quantum measurements without sums.
In
G. Chen, L. Kauffman, and S. Lamonaco, editors, Mathematics of Quantum
Computing and Technology, pages 567–604. Taylor and Francis, 2007. DOI:
10.1201/9781584889007.ch16.
[46] B. Coecke, D. J. Moore, and A. Wilce. Operational quantum logic: An overview.
In B. Coecke, D. J. Moore, and A. Wilce, editors, Current Research in Operational
Quantum Logic: Algebras, Categories and Languages, volume 111 of Fundamental
Theories of Physics, pages 1–36. Springer-Verlag, 2000. DOI: 10.1007/978-94-0171201-9˙1.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

48

<!-- page 49 -->
[47] B. Coecke, É. O. Paquette, and D. Pavlović. Classical and quantum structuralism. In S. Gay and I. Mackie, editors, Semantic Techniques in Quantum
Computation, pages 29–69. Cambridge University Press, Cambridge, 2010. DOI:
10.1017/CBO9781139193313.003.
[48] B. Coecke, F. Genovese, S. Gogioso, D. Marsden, and R. Piedeleu. Uniqueness of
composition in quantum theory and linguistics. In B. Coecke and A. Kissinger,
editors, Proceedings 14th International Conference on Quantum Physics and Logic,
Nijmegen, The Netherlands, 3-7 July 2017, volume 266 of Electronic Proceedings in
Theoretical Computer Science, pages 249–257. Open Publishing Association, 2018.
DOI: 10.4204/EPTCS.266.17.
[49] B. Coecke, J. H. Selby, and S. Tull. Two roads to classicality. In B. Coecke
and A. Kissinger, editors, Proceedings 14th International Conference on Quantum
Physics and Logic, Nijmegen, The Netherlands, 3-7 July 2017, volume 266 of Electronic Proceedings in Theoretical Computer Science, pages 104–118. Open Publishing
Association, 2018. DOI: 10.4204/EPTCS.266.7.
[50] Bob Coecke, Giovanni de Felice, Konstantinos Meichanetzidis, and Alexis Toumi.
Foundations for Near-Term Quantum Natural Language Processing. arXiv preprint
arXiv:2012.03755, 2020.
[51] Bob Coecke, Dominic Horsman, Aleks Kissinger, and Quanlong Wang. Kindergarden
quantum mechanics graduates (...or how I learned to stop gluing LEGO together and
love the ZX-calculus). arXiv preprint arXiv:2102.10984, 2021.
[52] Richard D. P. East, John van de Wetering, Nicholas Chancellor, and Adolfo
G. Grushin. AKLT-states as ZX-diagrams: diagrammatic reasoning for quantum
states. arXiv preprint arXiv:2012.01219, 2020.
[53] B. Dakić and Č. Brukner. Quantum Theory and Beyond: Is Entanglement Special?, pages 365–392. Cambridge University Press, Cambridge, 2011. DOI:
10.1017/CBO9780511976971.011.
[54] Niel de Beaudrap and Dominic Horsman. The ZX calculus is a language for surface
code lattice surgery. Jan 2020. DOI: 10.22331/q-2020-01-09-218.
[55] Niel de Beaudrap, Xiaoning Bian, and Quanlong Wang. Fast and effective techniques
for T-count reduction via spider nest identities. arXiv preprint arXiv:2004.05164,
2020.
[56] Niel de Beaudrap, Xiaoning Bian, and Quanlong Wang. Techniques to Reduce π/4Parity-Phase Circuits, Motivated by the ZX Calculus. In Bob Coecke and Matthew
Leifer, editors, Proceedings 16th International Conference on Quantum Physics and
Logic, Chapman University, Orange, CA, USA., 10-14 June 2019, volume 318 of
Electronic Proceedings in Theoretical Computer Science, pages 131–149. Open Publishing Association, 2020. DOI: 10.4204/EPTCS.318.9.
[57] Niel de Beaudrap, Ross Duncan, Dominic Horsman, and Simon Perdrix. Pauli Fusion: a Computational Model to Realise Quantum Transformations from ZX Terms.
In Bob Coecke and Matthew Leifer, editors, Proceedings 16th International Conference on Quantum Physics and Logic, Chapman University, Orange, CA, USA., 10-14
June 2019, volume 318 of Electronic Proceedings in Theoretical Computer Science,
pages 85–105. Open Publishing Association, 2020. DOI: 10.4204/EPTCS.318.6.
[58] R. Duncan. A graphical approach to measurement-based quantum computing.
arXiv:1203.6242 [quant-ph], 2012.
[59] R. Duncan and M. Lucas. Verifying the steane code with quantomatic. In B. Coecke
and M. Hoban, editors, Proceedings of the 10th International Workshop on Quantum
Physics and Logic, Castelldefels (Barcelona), Spain, 17th to 19th July 2013, volume

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

49

<!-- page 50 -->
171 of Electronic Proceedings in Theoretical Computer Science, pages 33–49. Open
Publishing Association, 2014. DOI: 10.4204/EPTCS.171.4.
[60] R. Duncan and S. Perdrix. Rewriting measurement-based quantum computations
with generalised flow. Automata, Languages and Programming, pages 285–296, 2010.
DOI: 10.1007/978-3-642-14162-1˙24.
[61] Jacques Faraut and Adam Korányi. Analysis on symmetric cones. 1994.
[62] L. Garvie and R. Duncan. Verifying the smallest interesting colour code with quantomatic. In B. Coecke and A. Kissinger, editors, Proceedings 14th International
Conference on Quantum Physics and Logic, Nijmegen, The Netherlands, 3-7 July
2017, volume 266 of Electronic Proceedings in Theoretical Computer Science, pages
147–163. Open Publishing Association, 2018. DOI: 10.4204/EPTCS.266.10.
[63] S. Gogioso and F. Genovese. Infinite-dimensional categorical quantum mechanics.
In R. Duncan and C. Heunen, editors, Proceedings 13th International Conference on
Quantum Physics and Logic, Glasgow, Scotland, 6-10 June 2016, volume 236 of Electronic Proceedings in Theoretical Computer Science, pages 51–69. Open Publishing
Association, 2017. DOI: 10.4204/EPTCS.236.4.
[64] S. Gogioso and F. Genovese. Towards quantum field theory in categorical quantum
mechanics. In B. Coecke and A. Kissinger, editors, Proceedings 14th International
Conference on Quantum Physics and Logic, Nijmegen, The Netherlands, 3-7 July
2017, volume 266 of Electronic Proceedings in Theoretical Computer Science, pages
349–366. Open Publishing Association, 2018. DOI: 10.4204/EPTCS.266.22.
[65] S. Gogioso and C. M. Scandolo. Categorical probabilistic theories. In B. Coecke
and A. Kissinger, editors, Proceedings 14th International Conference on Quantum
Physics and Logic, Nijmegen, The Netherlands, 3-7 July 2017, volume 266 of Electronic Proceedings in Theoretical Computer Science, pages 367–385. Open Publishing
Association, 2018. DOI: 10.4204/EPTCS.266.23.
[66] P. Goyal. Information-geometric reconstruction of quantum theory. Phys. Rev. A,
78(5):052120, 2008. DOI: 10.1103/PhysRevA.78.052120.
[67] L. Hardy. Quantum Theory From Five Reasonable Axioms. arXiv quantph/0101012, 2001.
[68] L. Hardy. Towards quantum gravity: a framework for probabilistic theories with
non-fixed causal structure. J. Phys. A, 40(12):3081, 2007. DOI: 10.1088/17518113/40/12/s12.
[69] L. Hardy. Reformulating and reconstructing quantum theory. arXiv:1104.2066
[quant-ph], 2011.
[70] L. Hardy. The operator tensor formulation of quantum theory. Phil. Trans. R. Soc.
A, 370(1971):3385–3417, 2012. DOI: 10.1098/rsta.2011.0326.
[71] L. Hardy. A formalism-local framework for general probabilistic theories, including quantum theory. Math. Structures Comput. Sci., 23(2):399–440, 2013. DOI:
10.1017/S0960129512000163.
[72] C. Heunen, A. Kissinger, and P. Selinger. Completely positive projections and
biproducts. In B. Coecke and M. Hoban, editors, Proceedings of the 10th International Workshop on Quantum Physics and Logic, Castelldefels (Barcelona),
Spain, 17th to 19th July 2013, volume 171 of Electronic Proceedings in Theoretical Computer Science, pages 71–83. Open Publishing Association, 2014. DOI:
10.4204/EPTCS.171.7.
[73] P. A. Höhn. Quantum theory from rules on information acquisition. Entropy, 19(3):
98, 2017. DOI: 10.3390/e19030098.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

50

<!-- page 51 -->
[74] P. A. Höhn. Toolbox for reconstructing quantum theory from rules on information
acquisition. Quantum, 1:38, 2017. DOI: 10.22331/q-2017-12-14-38.
[75] C. Horsman. Quantum picturalism for topological cluster-state computing. New J.
Phys., 13(9):095011, 2011. DOI: 10.1088/1367-2630/13/9/095011.
[76] P. Jordan, J. von Neumann, and E. P Wigner. On an algebraic generalization of the
quantum mechanical formalism. In The Collected Works of Eugene Paul Wigner,
pages 298–333. Springer, 1993. DOI: 10.2307/1968117.
[77] G. M. Kelly and M. L. Laplaza. Coherence for compact closed categories. J. Pure
Appl. Algebra, 19:193–213, 1980. DOI: 10.1016/0022-4049(80)90101-2.
[78] A. Kissinger and S. Uijlen. Picturing indefinite causal structure. In R. Duncan and
C. Heunen, editors, Proceedings 13th International Conference on Quantum Physics
and Logic, Glasgow, Scotland, 6-10 June 2016, volume 236 of Electronic Proceedings
in Theoretical Computer Science, pages 87–94. Open Publishing Association, 2017.
DOI: 10.4204/EPTCS.236.6.
[79] A. Kissinger and V. Zamdzhiev. Quantomatic: A proof assistant for diagrammatic
reasoning. In International Conference on Automated Deduction, pages 326–336.
Springer, 2015. DOI: 10.1007/978-3-319-21401-6˙22.
[80] A. Kissinger, M. Hoban, and B. Coecke. Equivalence of relativistic causal structure
and process terminally. arXiv:1708.04118 [quant-ph], 2017.
[81] Aleks Kissinger and John van de Wetering. Reducing T-count with the ZX-calculus.
Physical Review A, 102:022406, 8 2020. DOI: 10.1103/PhysRevA.102.022406.
[82] M. Koecher. Die Geodättischen von Positivitätsbereichen. Mathematische Annalen,
135(3):192–202, 1958.
[83] C. M. Lee and J. H. Selby. Generalised phase kick-back: the structure of computational algorithms from physical principles. New J. Phys., 18(3):033023, 2016. DOI:
10.1088/1367-2630/18/3/033023.
[84] C. M. Lee and J. H. Selby. Deriving Grover’s lower bound from simple physical
principles. New J. Phys., 18(9):093047, 2016. DOI: 10.1088/1367-2630/18/9/093047.
[85] C. M. Lee and J. H. Selby.
A no-go theorem for theories that decohere
to quantum mechanics. Proc. R. Soc. A, 474(2214):20170732, 2018. DOI:
10.1098/rspa.2017.0732.
[86] M. S. Leifer and R. W Spekkens. Towards a formulation of quantum theory as a
causally neutral theory of bayesian inference. Phys. Rev. A, 88(5):052130, 2013.
DOI: 10.1103/physreva.88.052130.
[87] G. Ludwig. An Axiomatic Basis of Quantum Mechanics. 1. Derivation of Hilbert
Space. Springer-Verlag, 1985. DOI: 10.1007/978-3-642-70029-3.
[88] G. W. Mackey. The mathematical foundations of quantum mechanics. W. A. Benjamin, New York, 1963.
[89] L. Masanes and M. P. Müller. A derivation of quantum theory from physical requirements. New J. Phys., 13(6):063001, 2011. DOI: 10.1088/1367-2630/13/6/063001.
[90] L. Masanes, M. P. Müller, R. Augusiak, and D. Pérez-Garcı́a. Existence of an
information unit as a postulate of quantum theory. Proc. Natl. Acad. Sci., 110(41):
16373–16377, 2013. DOI: 10.1073/pnas.1304884110.
[91] Camilo Miguel Signorelli, Quanlong Wang, and Ilyas Khan. A Compositional Model
of Consciousness based on Consciousness-Only. arXiv preprint arXiv:2007.16138,
2020.
[92] Kenji Nakahira. Derivation of quantum theory with superselection rules. arXiv
preprint arXiv:1910.02649, 2019.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

51

<!-- page 52 -->
[93] O. Oreshkov and N. J. Cerf. Operational formulation of time reversal in quantum
theory. Nat. Phys., 2015. DOI: 10.1038/nphys3414.
[94] O. Oreshkov, F. Costa, and Č. Brukner. Quantum correlations with no causal order.
Nat. Commun., 3:1092, 2012. DOI: 10.1038/ncomms2076.
[95] C. Piron. Axiomatique quantique. Helvetia Physica Acta, 37:439–468, 1964.
[96] M. Rédei. Why John von Neumann did not like the Hilbert space formalism of
quantum mechanics (and what he liked instead). Stud. Hist. Philos. Sci. B, 27(4):
493–510, 1996. DOI: 10.1016/S1355-2198(96)00017-2.
[97] David Schmid, John H Selby, Matthew F Pusey, and Robert W Spekkens. A
structure theorem for generalized-noncontextual ontological models. arXiv preprint
arXiv:2005.07161, 2020.
[98] David Schmid, John H Selby, and Robert W Spekkens. Unscrambling the omelette of
causation and inference: The framework of causal-inferential theories. arXiv preprint
arXiv:2009.03297, 2020.
[99] J. H. Selby and B. Coecke. A diagrammatic derivation of the Hermitian adjoint.
Found. Phys., 47(9):1191–1207, 2017. ISSN 1572-9516. DOI: 10.1007/s10701-0170102-7.
[100] J. H. Selby and B. Coecke. Leaks: quantum, classical, intermediate and more.
Entropy, 19(4):174, 2017. DOI: 10.3390/e19040174.
[101] P. Selinger.
Dagger compact closed categories and completely positive
maps.
Electron. Notes Theor. Comput. Sci., 170:139–163, 2007.
DOI:
10.1016/j.entcs.2006.12.018.
[102] P. Selinger. Idempotents in dagger categories. Electron. Notes Theor. Comput. Sci.,
210:107–122, 2008. DOI: 10.1016/j.entcs.2008.04.021.
[103] J. Sikora and J. Selby. Simple proof of the impossibility of bit commitment in
generalized probabilistic theories using cone programming. Phys. Rev. A, 97:042302,
2018. DOI: 10.1103/PhysRevA.97.042302.
[104] M. P. Solèr. Characterization of Hilbert spaces by orthomodular spaces. Commun.
Algebra, 23(1):219–243, 1995. DOI: 10.1080/00927879508825218.
[105] W. F. Stinespring. Positive functions on C ∗ -algebras. Proc. Am. Math. Soc., 6(2):
211–216, 1955. DOI: 10.2307/2032342.
[106] Tull and Kleiner. Integrated information in process theories. Feb 2020.
[107] S. Tull. Operational theories of physics as categories. arXiv:1602.06284 [quant-ph],
2016.
[108] S. Tull. Quotient categories and phases. arXiv:1801.09532 [math.CT], 2018.
[109] Sean Tull. A categorical reconstruction of quantum theory. Jan 2019. DOI:
10.23638/lmcs-16(1:4)2020.
[110] John van de Wetering. ZX-calculus for the working quantum computer scientist.
arXiv preprint arXiv:2012.13966, 2020.
[111] E. B. Vinberg. Homogeneous cones. Soviet Math. Dokl, 1(4):787–790, 1960.
[112] J. von Neumann. Mathematische grundlagen der quantenmechanik. Springer-Verlag,
1932. Translation, Mathematical foundations of quantum mechanics, Princeton University Press, 1955.
[113] John van de Wetering. An effect-theoretic reconstruction of quantum theory. Dec
2019. DOI: 10.32408/compositionality-1-1.
[114] A. Wilce. Symmetry and composition in probabilistic theories. Electron. Notes
Theor. Comput. Sci., 270(2):191–207, 2011. DOI: 10.1016/j.entcs.2011.01.031.
[115] A. Wilce. Symmetry and self-duality in categories of probabilistic models. In B. Jacobs, P. Selinger, and B. Spitters, editors, Proceedings 8th International Workshop

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

52

<!-- page 53 -->
on Quantum Physics and Logic, Nijmegen, Netherlands, October 27-29, 2011, volume 95 of Electronic Proceedings in Theoretical Computer Science, pages 275–279.
Open Publishing Association, 2012. DOI: 10.4204/EPTCS.95.19.
[116] A Wilce. A royal road to quantum theory (or thereabouts). 20(4), Mar 2018. DOI:
10.3390/e20040227.
[117] A. Wilce. A shortcut from categorical quantum theory to convex operational theories. In B. Coecke and A. Kissinger, editors, Proceedings 14th International Conference on Quantum Physics and Logic, Nijmegen, The Netherlands, 3-7 July 2017,
volume 266 of Electronic Proceedings in Theoretical Computer Science, pages 222–
236. Open Publishing Association, 2018. DOI: 10.4204/EPTCS.266.15.

A Consequences of a classical interface
A.1 Proof of Proposition 2.22
Proof. Let us assume that we have two different processes F 0 and F 1 which classically
control the same set of processes {fi }, that is:

∀i

=

F0

=

fi

F1

i

i

Now, let us characterise these two processes F α where α ∈ {0, 1} using tomography
(Def.2.17). That is, consider composing F α with arbitrary tester-vises, τ :

Fα

τ

if, for all τ , this is independent of α then tomography tells us that F 0 = F 1 . Let us now
show that this is indeed the case. Firstly let us define a pair of vises τ α :

Fα

τ

=:

τα

and note that these have only classical inputs and outputs so are themselves classical
processes. We can therefore decompose the classical identity and use distributivity of the
classical sum over classical diagrams:

X i
i

i

τα

=

X

i

i

i

τα

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

53

<!-- page 54 -->
Then using the definition of the τ α and the definition of the F α as classically controlled
processes for the set {fi } we obtain:
Fα
=

X

i

i

i

τ

fi

X

=

i

τ

i

Then simply note that this is independent of α for all τ to complete the proof.

A.2 Proof of Proposition 2.23
Proof. Recall that we propose a sum of any finite set of processes to be defined as:
B

B

P

:=

fi

i

(44)

F

A

A

where F is the unique (Prop. 2.22) classically controlled process satisfying:
B

B

=

fi

.

F

A

(45)

A

i

and
=

X

i

i

First, as a sanity check, note that this is equivalent to the standard sum for classical
processes. This follows immediately from the definition of F and by decomposing the
identity process:
m

m

=

F

X

n

=

F

i

m
i

n

i

X

m

=

F

X

fi

i

n

n

i

i

The sum that we are defining is therefore an extension of the classical sum to the full
process theory. In particular, this means that, as scalars are classical (see the discussion
after Def. 2.15), that the sum of scalars is the standard sum of non-negative real numbers
that we would expect. Next,given this proposed definition, we need to check that this is
indeed a valid summation, i.e. that it satisfies the conditions of Def. 2.11. The key step is
to show that:
D

D

B

P
i

fi

B

χ

=

P
i

A
C

fi

χ

(46)

A
C

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

54

<!-- page 55 -->
holds for any diagram χ. To check this, first note that the LHS of this is defined through
Eq. (8) as:
P

i

χ

fi

=

χ

F

On the other hand, to understand the RHS let us first define:

:=

gi

χ

fi

then, using Eq. (8) again, the RHS is equal to:

P

fi

χ

P

=

i

gi

=

G

i

where we are using classical control to define G such that it satisfies:
gi

=

G
i

It is then simple to see that:

∀i

G

=

gi

=

fi

χ

=

i

F

χ

fi

χ

i

which, using local tomography of classical theory, implies that:

G

=

F

χ

F

χ

We therefore find that:

P
i

fi

χ

=

=

G

=

P
i

and so, Eq. 3 is satisfied for all diagrams χ. Hence, the sums are free to move around
diagrams. The other constraints on the sum (e.g. commutativity etc.) are immediately
inherited from the equivalent property of the classical sum.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

55

<!-- page 56 -->
A.3 Proof of Proposition 2.24
Proof. First, note that if we have local causal-compatible tomographic tests then we have:

τ0
A

=

(47)

τ
Next, we want to characterise the set of processes in the full theory that are causalcompatible, that is, the set of processes which will not lead to any non-causal classical
processes. By assumption the tomographic-tests are causal-compatible, hence, a minimal
requirement for any other process f to be causal-compatible is that it must satisfy:

τ0
B

f
A

=

(48)

τ
We will now see that this is a necessary and sufficient constraint, which, can be moreover
expressed as the usual causality condition by suitably defining discarding maps. To see
this consider the special case of eq. (48) in which B is trivial, that is:
f

A

τ

=

We therefore find, for all causal-compatible effects, f , that:

f

τ0

A

τ

=

=

A

τ
and hence, by tomography that:
=

f

A

τ0
A

We can therefore take this to be a unique discarding map for system A:

:=
A

τ0

(49)

A

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

56

<!-- page 57 -->
Given this definition, then our causal-compatibility condition (eq. (48)) can be reexpressed
as a causality constraint. To begin we substitute eq. 49 into eqs. (48) and (47) to obtain
B

f

=

A

=

A

τ

τ

respectively. Then, by tomography we find that f must satisfy the usual causality condition:
B

f
A

=

A

.

This constraint is clearly necessary, however, how do we see that it is moreover sufficient?
This is simple, just note that the causal-compatibility condition merely requires that any
process with a classical input and no outputs is the classical discarding, as we have now
demonstrated that there is a unique effect for every system then this is just a special
case.

A.4 Proof of Proposition 2.25
Proof. Firstly recall, as noted underneath Def. 2.15, that the scalars in the theory are
classical and hence are non-negative real numbers. It is then clear that the state space
of a given system A is a convex cone CA , as it is closed under linear combinations with
non-negative real coefficients, i.e.:
A

P

A

X

i ri si :=

ri si

i

is a valid state.
Allowing the coefficients of linear combinations to be negative, the cone extends naturally to a real ordered vector space, spanned and ordered by the cone itself. By construction, the cone is then full dimensional (i.e., it spans the vector space), and it is simple to
show that it is pointed (i.e. the zero-vector is in the cone, and it is the unique vector for
which v and −v are in the cone). Moreover the cone is finite-dimensional: this immediately follows from finite tomography, as it implies that a state is characterised by a finite
number of real values.
Thanks to distributivity of sums (Eq. 3), any process f : A → B induces a positive
linear map between the vector space spanned by the states of system A and the vector
space spanned by the states of system B. This is defined as:
B
A

f

7→

s

s

A

where linearity follows immediately as a special case of Eq. 3 by:
f

f

=
P

i ri si

X
i

=
ri si

X
i

ri

f

=
i ri (f ◦ si )

P
si

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

57

<!-- page 58 -->
As it maps the convex cone of states of A to the convex cone of states of B, the induced
linear map is positive. Moreover, the map is completely positive, as it maps bipartite states
to bipartite states when applied locally to a subsystem.
An immediate corollary is that effects are linear functionals on the cone of states.
Therefore, ◦ s = 1 defines a hyperplane. This hyperplane intersects the cone, but not
the origin: first consider

τ
s

=0

⇐⇒

τ
⇐⇒

=0

s

s

=0

⇐⇒

s

=0

Therefore, for any state s 6= 0, there is some scalar rs such that ◦ (rs s) = 1; hence
the hyperplane intersects the cone. This is equivalent to the statement that
is in the
interior of the dual to the state cone.

B Classification of leaks and pure processes
We now classify the leaks and pure processes for quantum theory. First however, recall
the representation of a finite dimensional C*-algebra A from Ex. 2.4,
M

A=

where Ai = B(Hi )

Ai

i

and recall that processes in the processes theory are completely positive maps between
these C*-algebras. We now introduce a few processes and basic results that will be used
in this appendix.
1. Given a C*-algebra A =
onal projectors

L

i Ai there is a decomposition of the identity into orthog-

=
A

X

i

i

2. such that each of these projectors splits through an irreducible C*-algebra, that is
Ai

A

i

=

i

where

Ai
i

A

i

=

i

Ai

Ai

note that these triangles are not states and effects as they have both inputs and
outputs, the use of the triangle is simply to distinguish them from generic processes,
linear algebraically, they are the coordinate projections (mapping A → Ai ) and
inclusion maps (mapping Ai → A),
3. this decomposition of the identity provides us with a matrix representation of proL
L
cesses with input A = ni=1 Ai and output B = m
j=1 Bj as follows
j

B

=

f
A

X
ij

f
i

:=

X

fij

∼

(fij )j=1,...,m
i=1,..,n

ij

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

58

<!-- page 59 -->
4. where each fij defines a map between the irreducible C*-algebras Ai and Bj as
Bj
j

B

fij
A
i

Ai

5. Note the discarding map for the C*-algebra and for the irreducible components are
related by
A

=

i

Ai

Ai

6. Finally, for this process theory, it can be shown that

⇐⇒

= 0

F

F

= 0.

This, in fact, applies more generally than just to quantum theory as it can be derived
from local tomography, that any effect can appear in some decomposition of the
discarding map, and that scalars are non-negative real numbers (utilising the fact
that if the sum of a set of non-negative numbers is zero then every element must be
zero).
Recalling the definition of pure processes (Def. 2.32), we see that to understand what
the pure processes are we must understand what the leaks are for these systems. That is,
what leaks do we have for a C*-algebra? For fully quantum systems all leaks are trivial,
that is, any leak separates:
=

ρ

however, in classical theory, and more general C*-algebras the leaks are more interesting
as we will now demonstrate.
Proposition B.1. Given a C*-algebra, A =

L

i Ai any leak can be written as:

A L

l
=

A

X

i

ρi

=

i

where the ρi are normalised quantum states. Note that the connecting system on the
right hand diagram is a classical system, so the ‘leaked information’ is always essentially
classical.
Proof. Note first that any leak for A defines a leak for each of the Ai by pre- and postcomposing with the relevant projector, hence, as the Ai are fully quantum systems these

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

59

<!-- page 60 -->
leaks must be constant:
i
i

i

i

=

=

=

ρi

i

(50)

ρi

i

i

i
i

We therefore have
j

=

X
ij

j

X

=

+

ρi

i

i6=j

i

i

X
i

However, by decomposing the identity as a sum of the projectors, using the defining
equation of a leak, and that the ρi are normalised, we find
j

X

i

=

=

X

=

i

+

i

X
i6=j

i

i

and hence if i 6= j
j

j

= 0

and so

= 0

i

i

Combining this with Eq. (50) provides us with the result. Classical control then allows us
to write this in the form
L

A

l
where

l

A

:=

ρi

i

which completes the proof.
We are now in a position to understand what the pure processes are for quantum
theory.
Proposition B.2. Pure processes in quantum theory are processes whose matrix representation has i) pure processes as matrix elements, and ii) at most a single non-zero
process in each row and column.
Proof. Consider a pure process f : A → B where A = i Ai and B = j Bj , and its
P
matrix representation f = ij fij . Now given the leak of system B, which leaks the
‘which branch’ information to a classical system
L

:=
B

X

j

L

j

j

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

60

<!-- page 61 -->
we find that

l
f

=

=

f

f

=

=

f

X

j

j

f

l

ij

:=

fij lij

ij

i

i

X

The first equality follows from realising that in classical theory composing the cap with
the broadcasting map in this way is just the discarding map, i.e.:

=
The second from the fact that the same ‘which branch’ information is leaked each time,
i.e.:
=
The third comes from the definition of purity (Def. 2.32) and the above characterisation
of leaks (Prop. B.1), and the final equality is obtained by decomposing the two leaks into
the branches.
We therefore find that fij lij = fij and so either fij = 0 or lij = 1. However, as we
P
know that l is causal, this means that j lij = 1 for all i, and so for each i there is only a
single value of j such that lij = 1. Therefore, for that i, all other values of j must result
in fij = 0. That is, the matrix representation of f has at most a single non-zero element
in each row. We can make an equivalent argument starting with the leak at the bottom
pushing it through to the top. In this case we find that there is at most one non-zero
element in each column.
Now note that every dilation F of f must be given by some leak, which means that
j

X

j

F

=

=

F

=

f

ij

X

f

ρj

ij

i

i

therefore
j

j

F
i

=

f

ρi

i

and so every dilation of each of the fij must separate. In other words, the fij are pure
quantum processes.
To summarise, from the ‘commutativity’ conditions, we find that a pure process f
maps each summand of A to at most one summand of B and vice versa. Furthermore,
from the ‘all dilations are leaks’ condition we find that these maps between summands are
themselves pure.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

61

<!-- page 62 -->
C Symmetric purification in quantum theory
Given the characterisation of the pure processes in App. B, we can show that quantum
theory satisfies the symmetric purification postulate.
Theorem C.1. Completely positive maps between C*-algebras have symmetric purifications.
Proof. First let us consider the quantum case. We know (from Stinespring’s dilation
theorem [105]) that any process f : A → B can be purified to a process F : A → B ⊗ C
where C = A ⊗ B, and so it is simple to see that it can also be purified in a symmetric
way F : A ⊗ B → B ⊗ A:
B

B

=

f

B

C

=

F

A

B

A

A

:=

F

A

B

A

F
B

A

where we have used the fact that the caps are pure for fully quantum systems, and that the
composite of pure processes is pure. It therefore just remains to check that any two such
purifications are related in the correct way. Consider two such symmetric purifications F
and G, then we can use the cup —as it is pure for fully quantum systems— to define two
standard purifications (see Sec. 6.1) as:
B

C

B

D

=

F

=

f

A

B

C

D

G

A

A

these must be related by a reversible, and hence causal, transformation r:
r
=

F

G

Using the caps for a second time therefore means that:

r
=

F

:=

G

G

R

(51)

where the two processes forming the vise R (see Eq. 4) are given by:

xR

:=

and

yR

:=

r

It is simple to check that causality of r implies that R satisfies Eq. 18 as required.
Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

62

<!-- page 63 -->
Next we turn to the general C*-algebraic case. Consider a process f : A → B where
L
L
A = i Ai and B = j Bj with {Ai } and {Bj } irreducible C*-algebras, i.e. fully quantum
systems. It is simple to check that this does have a symmetric purification by noting that
we can define a dilation of a process f by symmetrically purifying the quantum maps of
matrix representation
j
j

j

f

=

X

=

f

ij

X

j

Ai

=

Fij

ij

i

X

i

Fij

:=

F

ij

Bj

i

j

i

i

It is then simple to check that this dilation is moreover pure and hence a symmetric
purification of f . Like for the quantum case, the more interesting part to check is Eq. (17).
Given some process f with two symmetric purifications F and G, i.e.

=

F

f

=

G

let us define:
j

j

Xij

:=

F

and

i

Yij

:=

G
i

Noting that these are purifications of the same fully quantum process, that is
j

=

Xij

f

=

Yij

i

and so using the above result for fully quantum systems we obtain:

=

Xij

Yij

Rij

Rij :=

X

and therefore:

j

F

=

X
ij

Xij
i

j

=

X
ij

Yij
i

j

ij

Yij

R

=

G

R

i

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

63

<!-- page 64 -->
where in the last step we have used classical control to construct R and defined the forwards
and backwards leaks as:
=

X
j

j

j

and

:=

X

i

i

respectively.

i

That R satisfies Eq. 18 follows directly from the quantum case.

Accepted in u
Qantum 2021-04-17, click title to verify. Published under CC-BY 4.0.

64
