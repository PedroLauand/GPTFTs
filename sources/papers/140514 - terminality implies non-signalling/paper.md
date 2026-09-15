---
type: paper
date: 2014-05-14
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1405.3681v3)
reviewed: false
---

# Terminality implies non-signalling

Machine-generated and unreviewed text extraction of arXiv:1405.3681v3
(10 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1405.3681v3>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Terminality implies non-signalling
Bob Coecke
University of Oxford
bob.coecke@cs.ox.ac.uk

A ‘process theory’ is any theory of systems and processes which admits sequential and parallel
composition. ‘Terminality’ unifies normalisation of pure states, trace-preservation of CP-maps, and
adding up to identity of positive operators in quantum theory, and generalises this to arbitrary process
theories. We show that terminality and non-signalling coincide in any process theory, provided one
makes causal structure explicit. In fact, making causal structure explicit is necessary to even make
sense of non-signalling in process theories. We conclude that because of its much simpler mathematical form, terminality should be taken to be a more fundamental notion than non-signalling.

1

Introduction

Causality related notions are prominent in many areas of physics, and the relationships between these
are by no means obvious. Examples that are relevant to us are:
C1 Relativistic space-time is often abstracted as a partial ordering, called causal structure [15].
C2 In quantum information, for example in the context of generalised probabilistic theories [1], one
often relies on the notion of non-signalling, by means of which one intends to implement these
relativistic constraints for spatially distributed information-processing devices.
C3 In quantum foundations, an axiom called causality has recently been put forward in [3, 4]. For
process theories [6, 8] this axiom is equivalent to the mathematical notion of terminality,1 and here
we will adopt this terminology in order to avoid confusing multiple uses of the term ‘causal(ity)’.2
These three notions do not straightforwardly match each other. For example, in [3, 4] the causality
axiom stands for non-signalling-from-the future (i.e. time-like), while the above mentioned notion of
non-signalling concerns space-like separation. Also, in [10] it was shown that while relativistic spacelike separation is invariant under time-reversal, this is by no means the case for non-signalling.
Here we investigate how these notions are related. Firstly, we argue that to even make sense of nonsignalling for general process theories (cf. C2) one needs to make causal structure (cf. C1) explicit. Then,
the resulting definition of non-signalling, for the particular case of two systems, becomes equivalent to
terminality (cf. C3). In the process of doing so we also resolve the seeming contradiction in [10].
Since terminality is mathematically way simpler than non-signalling, it should be taken to be the
more fundamental notion. Such a stance is already adopted in [8] where it is shown that within the context
of process theories much of the relevant structure of quantum theory directly follows from terminality.
Terminality also yields a covariance theorem [9] (building further on earlier work in [13, 2]).
1 Process theories are symmetric monoidal categories and causality boils down to terminality of the tensor unit.
2 C1, C2 as well as C3 are ofter referred to as causality.

B. Coecke, I. Hasuo & P. Panangaden (Eds.):
Quantum Physics and Logic 2014 (QPL 2014).
EPTCS 172, 2014, pp. 27–35, doi:10.4204/EPTCS.172.3

c B. Coecke
This work is licensed under the Creative Commons
Attribution-Noncommercial License.

<!-- page 2 -->
Terminality equals non-signalling

28

Related work. Pearl resolved several paradoxes in probability theory [14] by making causal structure
explicit within probability theory, an achievement for which he received the Turing Award. This treatment of probability theory also resulted in a fine-grained analysis of Bell’s theorem by Wood-Spekkens
[16], exploiting many tool’s of Pearl’s approach. Very recently, two other papers appeared which included very similar results, by Fritz [11] and Henson-Lal-Pusey [12]. A first difference is that the results
of these authors were obtained within a more restrictive framework, but exploit more general scenarios.
A more fundamental difference is that these authors fix one particular causal structure and study the resulting correlations. Here we will universally quantify over all causal structures that leave the two parties
separate. Our goal is indeed not to obtain a result with respect to a fixed causal structure, but relate
terminality and non-signalling for any causal structure that is allowed for.

2

Process theories with discarding

Here, by a process theory [6, 8] we mean a collection of systems, represented by wires, and processes,
represented by boxes with wires as inputs and outputs. Moreover, when we plug these boxes together:
A

B

C

g
D

A

f

h
A

the resulting diagram should also be a process. For the purposes of this paper, outputs should be connected to inputs, and diagrams should never contain causal loops.
Remark 2.1. Equivalently, one can say that a process theory is a symmetric monoidal category.
Remark 2.2. In the above diagram we used labels to distinguish distinct systems and distinct wires, but
we could also have done this by relying on different kinds of wires:
g
f

h

From now on we will omit labels or different kinds of wires, but all wires (within one diagram) may be
interpreted as distinct.
A state is a process without inputs, and an effect is a process without outputs. We will assume that
for each system there exists a discarding effect, which we denote as follows:

Example 2.3. When viewing probability theory as a process theory, boxes are stochastic maps, states
are probability distributions, and discarding is marginalization.
Example 2.4. When viewing quantum theory as a process theory, boxes include CP-maps as well as
measurements and classical data processes, states include density operators, and discarding is either the
trace or deletion of classical dada. A detailed description of quantum theory as a process theory is in [7].

<!-- page 3 -->
B. Coecke

3

29

Terminality vs. non-signalling

Definition 3.1. A process theory is terminal if for every process f we have:

f

(1)

=

Terminality has a clear operational intuition: performing an operation on a system, and then discarding the resulting system, is the same as discarding that system from the start.
Proposition 3.2. For a process theory with discarding processes, TFAE:
(a) it is terminal,
(b) all effects are discarding, and,
(c) for each system there is only one effect.
Remark 3.3. When taking a process theory to be a symmetric monoidal category, by Proposition 3.2 (c)
it follows that ‘terminality’ is a shorthand for ‘the tensor unit being terminal’.
Example 3.4. In the case of probability theory, terminality means stochasticity, which in the particular
case of probability distributions means summing up to 1, i.e. normalisation.
Non-signalling is a bit more involved. The idea behind it is that for two spatially separated parties,
say Alice and Bob, when they share a device (= a process f ) with two inputs and two outputs, each
having access to one input and one output, then, from one’s own input-output pair one should not be able
to derive the other party’s input. Otherwise, this device would enable the parties to signal to each other
while they are space-like separated, hence violating relativity. So from one of the party’s perspective, say
Bob’s, who has no access to Alice’s output, something that we can represent by discarding that output,
Alice’s input must not affect Bob’s input-output relationship. That is, from Bob’s perspective Alice’s
input can be discarded, resulting in some process h between Bob’s input and Bob’s output. This leads to
one equation with an existential quantifier. A second equation concern’s Alice’s perspective on things.
Definition 3.5. A two-input-two-output process f is non-signalling if we have:

∃h :

f

=

h

and

∃h′ :

f

=

h′

However, it is a lot more delicate to say that a process theory is non-signalling. Simply saying ‘a
process theory is non-signalling if all its processes are’ doesn’t work. For example, most process theories
would include the swap process:

which evidently violates non-signalling. The obvious reason being that this process consists of two clear
signalling channels. The kind of thing non-signalling aims to forbid is that without having such explicit
signalling channels, signalling should not be possible. This is exactly the kind of thing that can be said
in terms of a causal structure (see below), so we will need to reconsider the notion of non-signalling in
the context of causal structure, in order to make sense of a non-signalling process theory.

<!-- page 4 -->
Terminality equals non-signalling

30

Remark 3.6. One could argue that there is no reason why in the case of non-signalling the discarding
effect should be unique, something which we implicitly assumed in our notation. One could indeed
weaken the definition of non-signalling for a process f to:
∃e, h :

f

=

e

∃h′ , e′ :

and

h

f

=

h′

e′

This would not affect the main claims in this paper, in that we would still be able to derive non-signalling
from terminality, and hence, that terminality should be taken to be the more fundamental notion.

4

Process theories with causal structure

A causal structure is a partial ordering, which we can represent by the corresponding Hasse-diagram.
For example, if we have ⊥ < a, b < ⊤ then this yields the diagram:
⊤
b
a

(2)

⊥

Here, ⊥ can signal to a and b, which themselves can signal to ⊤, and by transitivity, ⊥ can also signal to
⊤. But a cannot signal to b and vice versa.
We can use such a causal structure as a support for a diagram within a process theory in the following
manner, which (more or less) generalises how causal networks are defined by Pearl in [14]:3
• processes are positioned on nodes of the causal structure,
• wires follow the edges, from outputs to inputs, and
• we allow open inputs and open outputs at nodes.4
With respect to the causal structure (2), we could for example have:
f⊤
fa

fb

(3)

f⊥

where we allowed at a and b for there to be open inputs and outputs.
Remark 4.1. The manner in which a diagram of processes carries a causal structure was also considered
in [9]. In brief, each diagram already carries a shadow of a causal structure in that sequential composition
can be interpreted as ‘after’, i.e. time-like separated, and that parallel composition can be interpreted as
‘while’, i.e. possibly space-like. So the only required additional specification is to state which processes
are genuinely space-like separated. We refer the reader to [9] for more details.
3 We say ‘more or less’ since for the purposes of this paper we modify things a bit as compared to [14].
4 It is here that we modify Pearl’s approach by allowing ‘open inputs and outputs’.

<!-- page 5 -->
B. Coecke

31

The type of scenario that we considered when defining non-signalling involves two parties that are
not supposed to be able to have signalling channels to each other, just like a and b in (2).5 That Alice
and Bob each have an input and an output is then made explicit by the causal process network (3).
In fact, this is the most general situation that we need to consider for the purpose of evaluating
non-signalling. Indeed, while one could of course have a causal structure like the following ones:

these are still covered by the diamond-shaped process network simply by treating clusters of nodes as
single processes:

Definition 4.2. A process theory is non-signalling if all processes of the form (3) are.
Example 4.3 (two-sorted process theories). When one is concerned with non-signalling, then typically,
there are two kinds of systems involved. One of them would correspond to probabilities, while the
other one could involve some exotic physical systems, which may be existing e.g. quantum theory, or
hypothetical e.g. Barrett’s box world [1] which enables one to realise correlations between systems way
beyond quantum correlations, and in fact, is extremal as far as non-signalling is concerned. One treats
the inputs and outputs at Alice’s and Bob’s ends as probabilities, but the ‘internal wiring’ of the box as
in Definition 3.5 may involve the exotic systems. The causal process network (3) would then become:
f⊤
fa

fb
f⊥

where the bold wires and boxes mean ‘exotic’ while the normal wires mean ‘probability’.
5 So in the context of [9], these two parties have to be genuinely space-like separated.

<!-- page 6 -->
Terminality equals non-signalling

32

Example 4.4 (local hidden variables). The notion of a local hidden variable theory means that such a
two-sorted diagram can be replaced by a one-sorted one, only involving normal wires, and bold then
standing for ‘quantum’. As we shall see below in the proof of Theorem 5.1, assuming terminality, which
one does in quantum theory, the diamond shape immediately becomes a V-shape, and the definition for
a local hidden variable representation then becomes, given a quantum scenario involving fa , fb , f⊥ :
∃ha , hb , h⊥ :

ha

hb

=

fa

h⊥

5

fb
f⊥

Main result

Let us first summarise what we have established so far. We want to compare the notions of terminality
and non-signalling for process theories, but noted that non-signalling of a process of the form:
f

already requires explicit internal causal structure in order to define what it means for a process theory to
be non-signalling, so that we can exclude internal signalling channels such as e.g.:

We concluded that the internal causal structure should be a diamond so that f should be of the form:
f⊤
fa

fb
f⊥

This now allows for a definition of a non-signalling process theory.
Theorem 5.1. If a process theory is terminal then it is non-signalling.
Proof. Assuming terminality, we have for f⊤ in (3):

f⊤

so (3) becomes:

=

<!-- page 7 -->
B. Coecke

33

fa

fb
f⊥

and applying terminality to fa the equational requirement for non-signalling is now indeed obeyed:

fa

fb

fb

=

f⊥

f⊥

where the dashed box identifies h as in Definition 3.5.
To prove the converse, we need one extra assumption. What is a process with no inputs and no
outputs? It interacts with nothing, so it should be independent of anything else that happens.
Definition 5.2. By (!) we mean that there is a unique diagram with no inputs nor outputs, the empty one.
Remark 5.3. The justification for there only being one box with no input and no output is that it represents certainty, and in this paper all processes are conceived as happening with certainty. For example,
in the context of quantum theory this means that measurements are considered ‘as a whole’, that is,
taking into account all possible outcomes together. This is different from, for example, a diagram for
teleportation such as [5]:
hBell|

1
4

=
|Belli

where a particular measurement outcome is considered that only happen with a probability 14 .
Theorem 5.4. Assuming (!), if a process theory is non-signalling then it is terminal.
Proof. Equation (1) follows from non-signalling of processes, simply by taking the input and the output
of one of the parties in Definition 3.5 to be trivial (i.e. no input nor output). Since h now has no inputs
nor outputs it is the empty diagram by (!).

6

Discussion

So we achieved our goal and established equivalence of terminality and non-signalling for two parties,
where we conceive the fact that terminalty implies non-signalling as the most significant result. Terminality is both conceptually and formally the simpler and more elegant notion, and should therefore be
taken to be the more fundamental one. Some other consequences are:
• Much attention has been given to the notion of non-signalling in several frameworks for theories
more general than quantum theory, and maybe, these frameworks should be reconsidered.

<!-- page 8 -->
Terminality equals non-signalling

34

• While in [3, 4] terminality was taken to mean non-signalling from the future, we showed here that
it does much more than just that, also implying non-signalling in the usual sense.
• The reason why our result demystifies the result of [10] is that one simply should not try to
match causal structure with non-signalling. Causal structure is only one ingredient when defining non-signalling, and while causal structure admits a clear notion of time-reversal, the other
ingredient, the process theory does not admit such a thing, since it is governed by a manifestly
time-asymmetric principle such as terminality.

Acknowledgement
Rob Spekkens has for quite a while already emphasised the importance for quantum foundations of
causal structure as in causal networks. In chats last summer in Benasque he indicated that this may
provide the key to demystifying [10], which, as we demonstrated here, it indeed did. In the same chat,
he also strongly voiced his concerns about the the notion of non-signalling as in quantum information,
which hopefully, here we (at least in part) also dethroned.
The QPL referees provided some very useful feedback on the submitted draft and Tobias Fritz and
Raymond Lal where helpful by carefully examining the relationship of our work to theirs.

References
[1] J. Barrett. Information processing in generalized probabilistic theories. Physical Review A, 75(3):032304,
2007. doi:10.1103/PhysRevA.75.032304
[2] R. F. Blute, I. T. Ivanov, and P. Panangaden. Discrete quantum causal dynamics. International Journal of
Theoretical Physics, 42(9):2025–2041, 2003. doi:10.1023/A:1027335119549
[3] G. Chiribella, G. M. D’Ariano, and P. Perinotti. Probabilistic theories with purification. Physical Review A,
81(6):062348, 2010. doi:10.1103/PhysRevA.81.062348
[4] G. Chiribella, G. M. D’Ariano, and P. Perinotti. Informational derivation of quantum theory. Physical Review
A, 84(1):012311, 2011. doi:10.1103/PhysRevA.84.012311
[5] B. Coecke. Kindergarten quantum mechanics — lecture notes. In A. Khrennikov, editor, Quantum Theory: Reconsiderations of the Foundations III, pages 81–98. AIP Press, 2005. arXiv:quant-ph/0510032.
doi:10.1063/1.2158713
[6] B. Coecke. A universe of processes and some of its guises. In H. Halvorson, editor, Deep Beauty: Understanding the Quantum World through Mathematical Innovation, pages 129–186. Cambridge University
Press, 2011. arXiv:1009.3786. doi:10.1017/CBO9780511976971.004
[7] B. Coecke and A. Kissinger. The compositional structure of multipartite quantum entanglement. In Automata,
Languages and Programming, Lecture Notes in Computer Science, pages 297–308. Springer, 2010. Extended
version: arXiv:1002.2540. doi:10.1007/978-3-642-14162-1/25
[8] B. Coecke and A. Kissinger. Picturing Quantum Processes. Cambridge University Press, 2014.
[9] B. Coecke and R. Lal. Causal categories: relativistically interacting processes. Foundations of Physics, page
to appear, 2012. arXiv:1107.6019. doi:10.1007/s10701-012-9646-8
[10] B. Coecke and R. Lal. Time asymmetry of probabilities versus relativistic causal structure: An arrow of time.
Physical Review Letters, 108:200403, May 2012. doi:10.1103/PhysRevLett.108.200403
[11] T. Fritz. Beyond Bell’s theorem II: Scenarios with arbitrary causal structure. arXiv:1404.4812, 2014.
doi:10.1088/1367-2630/14/10/103001

<!-- page 9 -->
B. Coecke

35

[12] J. Henson, R. Lal, and M. F. Pusey. Theory-independent limits on correlations from generalised Bayesian
networks. arXiv:1405.2572, 2014. doi:10.1088/1367-2630/16/11/113043
[13] F. Markopoulou. Quantum causal histories. Classical and Quantum Gravity, 17(10):2059, 2000.
doi:10.1103/PhysRevD.75.084001
[14] J. Pearl.
Causality: Models, Reasoning and Inference.
Cambridge University Press, 2000.
doi:10.1002/sim.1006
[15] R. Penrose. Techniques of Differential Topology in Relativity. SIAM, 1972. doi:10.1137/1.9781611970609
[16] C. J. Wood and R. W. Spekkens. The lesson of causal discovery algorithms for quantum correlations: causal
explanations of Bell-inequality violations require fine-tuning. arXiv:1208.4119, 2012.
