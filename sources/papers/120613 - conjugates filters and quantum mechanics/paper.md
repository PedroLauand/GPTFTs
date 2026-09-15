---
type: paper
date: 2012-06-13
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1206.2897v8)
reviewed: false
---

# Conjugates, Filters and Quantum Mechanics

Machine-generated and unreviewed text extraction of arXiv:1206.2897v8
(33 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1206.2897v8>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Conjugates, Filters and Quantum Mechanics
Alexander Wilce
Department of Mathematics and Computer Science, Susquehanna University

arXiv:1206.2897v8 [quant-ph] 1 Jul 2019

November 9, 2021

The Jordan structure of finite-dimensional quantum theory is derived, in a conspicuously easy way, from a few simple postulates concerning abstract probabilistic models
(each defined by a set of basic measurements and a convex set of states). The key
assumption is that each system A can be paired with an isomorphic conjugate system,
A, by means of a non-signaling bipartite state ηA perfectly and uniformly correlating
each basic measurement on A with its counterpart on A. In the case of a quantummechanical system associated with a complex Hilbert space H, the conjugate system
is that associated with the conjugate Hilbert space H, and ηA corresponds to the standard maximally entangled EPR state on H ⊗ H. A second ingredient is the notion
of a reversible filter, that is, a probabilistically reversible process that independently
attenuates the sensitivity of detectors associated with a measurement. In addition to
offering more flexibility than most existing reconstructions of finite-dimensional quantum theory, the approach taken here has the advantage of not relying on any form
of the “no restriction” hypothesis. That is, it is not assumed that arbitrary effects
are physically measurable, nor that arbitrary families of physically measurable effects
summing to the unit effect, represent physically accessible observables. (An appendix
shows how a version of Hardy’s “subpace axiom” can replace several assumptions
native to this paper, although at the cost of disallowing superselection rules.)

1 Introduction and Overview
A number of recent papers, notably [11, 14, 20, 25, 28], have succeeded in deriving the mathematical apparatus of finite-dimensional quantum mechanics (henceforth: QM) from various packages
of broadly operational, probabilistic, or information-theoretic assumptions. These assumptions
are, however, rather strong, and the derivations themselves are not trivial. This paper aims at a
slightly broader target, and finds it much easier to hit.
Specifically, the Jordan structure of finite-dimensional quantum theory is derived, in a conspicuously easy way, from a few simple principles. This still brings us within hailing distance
of standard QM, owing to the classification theorem for finite-dimensional formally real Jordan
algebras as direct sums of real, complex and quaternionic quantum systems, spin factors (“bits”
of arbitrary dimension), and the exceptional Jordan algebra [22]. In contrast, all of the cited
reconstructions make use of strong axioms that rule out real and quaternionic systems, and even
complex quantum systems with superselection rules, more or less by fiat. Since there are good
arguments for taking real and quaternionic quantum systems seriously (see [4] for a forceful argument in this direction), it is of interest to have an axiomatic scheme that accommodates them.
Alexander Wilce: wilce@susqu.edu

Accepted in Quantum 2019-06-24, click title to verify

1

<!-- page 2 -->
I shall have more to say on this point below.
Correlation in quantum mechanics The approach taken here begins with a simple and wellknown observation about finite-dimensional quantum systems. Let H be an n-dimensional complex Hilbert space1 , representing a finite-dimenional quantum system. Recall that the conjugate
Hilbert space, H, is the same abelian group, but endowed with the scalar multiplication (c, x) 7→ cx
(where the scalar multiplication on the right is that in H, and c is the complex conjugate of c ∈ C),
and with inner product (x, y) 7→ hy, xi. It is customary to write x for the vector x ∈ H, regarded
as a vector in H, so that cx = cx, or, equivalently, cx = c x. The inner product on H is then
given by hx, yi = hy, xi = hx, yi. 2
Suppose now that W is any density operator on H, with spectral decomposition W =
P
x∈E λx px for some orthonormal basis E, where px is the rank-one projection associated with a
unit vector x ∈ E. Then W is the marginal, or reduced state, of the pure bipartite state
ΨW :=

X

λx1/2 x ⊗ x ∈ H ⊗ H

(1)

x∈E

The fact that mixed quantum-mechanical states arise in this way as marginals of pure states on
larger systems is the starting point for the reconstruction of QM in [11]. Here, we focus instead
on the correlational features of ΨW . A straightforward calculation shows that if a, b are any two
operators on H, then
h(a ⊗ b)ΨW , ΨW i = Tr(W 1/2 aW 1/2 b).
In particular, if a and b commute with W , then we have
h(a ⊗ b)ΨW , ΨW i = Tr(W ab).

(2)

It follows that the state ΨW perfectly correlates any projection-valued observable that commutes
with W , with its counterpart on H: if a and b are mutually orthogonal projections, both commuting with W , then the joint probability of observing a and b is hΨW , a ⊗ bi = Tr(W ab) = 0,
while the joint probability of a and a is hΨW , a ⊗ ai = Tr(W a). Where a = px is the rank-one
projection associated with a unit vector x, this means that the conditional state of the conjugate
system, given a measurement result x on the system corresponding to H, is the “collapsed” state
corresponding x. In effect, the entangled state ΨW allows the conjugate system to retain a record
of the measurement result on the first system — even though no signal need have passed between
the two.
A striking special case arises where W = n1 1, the maximally mixed state: in this case, ΨW is
the “EPR” state
X
Ψ = √1n
x ⊗ x,
x∈E

the expansion being independent of the choice of the orthonormal basis E. As every observable
commutes with W , Ψ perfectly, and uniformly, correlates every observable on H with its counterpart on H. Thus, if we imagine that the system corresponding to H is controlled by Alice and
that corresponding to H, by Bob, then if Alice and Bob happen to make the same measurement,
1

A word on notation: I follow the mathematicians’ convention that a complex inner product h , i is conjugatelinear in the second, rather than the first argument. Thus, in terms of Dirac notation, hx, yi = hy|xi.
2

One can think of H as the space of bras hx| corresponding to the kets |xi ∈ H, but I prefer to avoid this
representation, since I want to stress the idea that H represents a quantum system in its own right. Thus, using
Dirac notation we might write |xi = hx|.
Accepted in Quantum 2019-06-24, click title to verify

2

<!-- page 3 -->
they are bound to obtain the same result, with uniform probability 1/n. Notice, also, that by (2)
we have
h(a ⊗ b)Ψ, Ψi = n1 Tr(ab)
for all observables a and b, so the state Ψ in some sense explains the normalized trace inner product.
Correlation in General Probabilistic Theories These correlational features make sense in
a much more general setting. As explained in more detail below, a probabilistic model is characterized by a set of basic measurements or experiments, and a convex set of states, with each
state α assigning a probability α(x) to every outcome x of every basic measurement. Given two
such models A and B, a bipartite state ω on A and B is an assignment of joint probabilities
ω(x, y) to all outcomes x and y of basic A- and B-measurements, respectively, having well defined
conditional and marginal (reduced) probability weights corresponding to states of A and B.
We now impose some restrictions on the probabilistic models under consideration. First, we
require all state spaces to be finite-dimensional (we are, after all, only attempting to recover
finite-dimensional QM). Secondly, we require that models be uniform, in the sense that
(i) all basic measurements have a common, finite number of outcomes, n, called the rank of A;
and
(ii) there exists a maximally mixed state, ρ, defined by ρ(x) = 1/n for all basic measurement
outcomes x
These conditions are satisfied by finite-dimensional quantum-mechanical models, including those
involving superselection sectors, provided that we restrict attention to maximal observables, i.e.,
those consisting of rank-one projections. More generally, condition (i) is reasonable if we think
of basic measurements as maximally informative, so that each has the largest possible number of
outcomes, and cannot be further refined. Given condition (i), the maximally-mixed state is welldefined mathematically, so in (ii), we are only requiring that it count as a physically accessible
state.
The following is a direct translation of the correlational features discussed above for quantummechanical systems, into the language of probabilistic models.
Definition 1. A conjugate of a (uniform) probabilistic model A is a model A, together with an
isomorphism γ taking each basic measurement outcome x of A to an outcome x := γ(x) of A,
such that
(a) Every state α of A is the marginal of some state ω on A and A (in general, depending
on α) correlating some basic measurement E of A with its counterpart on A so that
for all x ∈ E,
ω(x, x) = α(x)
so that ω(x, y) = α(x)δx,y .
(b) The maximally mixed state ρ arises as the marginal of a bipartite state ηA uniformly
correlating every basic measurement with its counterpart, in the sense that
ηA (x, x) = n1
for all basic measurement outcomes x, where n is the rank of A.
Evidently, in the quantum-mechanical case, where α corresponds to a density operator W ,
the state ΨW supplies the correlating state ω, while the bipartite state η corresponds to the EPR
state Ψ 1 = Ψ.
n1

Accepted in Quantum 2019-06-24, click title to verify

3

<!-- page 4 -->
Mathematically, the existence of a conjugate system has affinities with the purification postulate of [11], though we do not require the correlating bipartite state ω above to be pure. Physically,
a conjugate system A allows for the formation of records of the outcomes of measurements on A in
causally separated systems, exactly as in the quantum case. Condition (a) above simply requires
that, for every state α, there be at least one basic measurement on A that can be thus recorded
and later “read off” by performing the corresponding measurement on A. Condition (b) requires
that, where A is in the maximally mixed state, it be possible to record every basic measurement
in this way.
From correlation to Jordan algebras Remarkably little is required, beyond the existence of a
conjugate, to secure a representation of A in terms of a formally real Jordan algebra. This depends
on a classic mathematical result, the Koecher-Vinberg Theorem [18]. A finite-dimensional ordered
vector space E with positive cone E + is self-dual if it carries an inner product such that a ∈ E +
iff ha, bi ≥ 0 for all b ∈ E + . If the group of invertible linear mappings E → E carrying E + onto
itself acts transitively on the interior of the cone E + , then E is said to be homogeneous. The
Koecher-Vinberg Theorem asserts that if E is both homogeneous and self-dual, it can be endowed
with a formally real Jordan structure for which E + = {a2 |a ∈ E}.
Any probabilistic model A gives rise in a natural way to two ordered vector spaces: a space
V(A), generated by A’s states, and a space E(A) ≤ V(A)∗ generated by evaluation functionals
b : α 7→ α(x) associated with basic measurement outcomes x. Since we are assuming that the state
x
space is finite dimensional, both of the spaces E(A) and V(A) are also finite dimensional, and it
is easy to see that they have the same dimension. If we can show that E(A) is homogeneous and
self-dual, then the Koecher-Vinberg Theorem will provide a formally real (equivalently, euclidean)
Jordan structure on E(A) for which the cone of squares coincides with E(A)+ .
Call a probabilistic model A sharp if, for every basic measurement outcome x, there is a unique
state δx with δx (x) = 1. Physically, this is a way of saying that basic measurements are maximally
informative: if we can predict the outcome with certainty, we know the system’s state exactly.
Theorem 1. Suppose A is sharp and has a conjugate. Then the state ηA gives rise to a selfdualizing inner product on E(A), with respect to which E(A) and V(A) are isomorphic as ordered
vector spaces.
It follows that if V(A) is homogeneous, so is E(A), whence, by the Koecher-Vinberg Theorem,
the latter carries a formally real Jordan structure. But the homogeneity of V(A) has a direct
physical interpretation: it says that for every non-singular state — that is, every state α with
α(x) > 0 for every basic measurement outcome — there exists a probabilistically reversible process
T — defined below, but, roughly, one that can be reversed by another process with non-zero
probability — such that T (ρ) = rα where r ∈ [0, 1]. In other words, every non-singular state
can be prepared, up to normalization, by applying a probabilistically reversible process to the
maximally mixed state.
In fact, it is enough to assume less. By a filter for a basic measurement with outcome-set E, I
mean a process Φ — that is, a positive linear mapping Φ : V(A) → V(A) — that independently
attenuates the reliability of each outcome x ∈ E, so that for every state α, Φ(α)(x) = tx α(x) for
some constant tx (independent of α). If we think of basic measurement outcomes as detectors,
the existence of such filters, with arbitrary coefficients, is plausible; in standard QM, not only do
they exist but, if tx > 0 for every x ∈ E, then Φ can be chosen to be probabilistically reversible.
Where a probabilistic model A shares this feature, I will say that A has arbitrary reversible filters.
Corollary 1. Suppose that A is sharp, has a conjugate, and has arbitrary reversible filters. Then
E(A) is homogeneous and self-dual.
Accepted in Quantum 2019-06-24, click title to verify

4

<!-- page 5 -->
If we adopt a stronger assumption about filters, we can weaken the requirement that A have
a conjugate, and eliminate entirely the hypothesis that A is sharp. Let us say that A has a weak
conjugate if the maximally mixed state ρ is the marginal of a uniformly correlating state ηA on A
and A, as in condition (b) in Definition 1, but not assuming that every state is the marginal of a
correlating state, i.e., not assuming condition (a). That is, we require only that there exist a joint
state on two copies of A — an analogue of the EPR state — in which, if the same measurement is
performed on each copy, the results are guaranteed to be the same, but are otherwise completely
random.
By applying the filter Φ to the system A, and then computing the canonical bipartite state
ηA , we obtain a new bipartite state. Equally, we could begin by applying the counterpart of Φ to
the conjugate system, obtaining another bipartite state. If these two bipartite states are in fact
the same, we say that Φ is symmetric.
Corollary 2. Let A have a weak conjugate. If every non-singular state of A can be prepared, up
to normalization, from the maximally mixed state by a symmetric, reversible filter, then E(A) is
homogeneous and self-dual.
The proofs of these results are all quite short and straightforward. In summary, we recover
euclidean Jordan algebras from either of two distinct, but related, sets of assumptions about
physical systems represented by uniform, finite-dimensional probabilistic models:
(a) systems are sharp;
(b) Systems have conjugates; and
(c) Systems have arbitrary reversible filters.
Alternatively, and more compactly:
(b0 ) Systems have weak conjugates;
(c0 ) All non-singular states can be prepared by reversible symmetric filters
Any euclidean Jordan algebra gives rise to a probabilistic model in which basic measurements
correspond to Jordan frames, i.e., sets {ei } of minimal idempotents satisfying ei ej = 0 for i 6= j,
P
and i ei = 1, where 1 is the Jordan unit. (In standard QM, these would correspond to maximally
fine-grained projective measurements.) In Appendix A, it is shown that any such model satisfies
all of the assumptions above and, conversely, if A satisfies either package of assumptions, the
Jordan product on E(A) can be chosen so that the set of basic measurements is precisely the
set of Jordan frames. Thus, these two sets of assumptions are in fact equivalent, and exactly
characterize this class of euclidean Jordan-algebraic probabilistic models.
There is actually a third possibility, in which condition (b) in the definition of a conjugate is
replaced by a rather weak symmetry assumption and a version of Hardy’s subspace axiom [20].
Again, the resulting package of assumptions is satisfied by, and hence, characterizes, Jordan models. The details are spelled out in Appendix B.

·

Other reconstructions of QM The approach of this paper offers some significant advantages
over the reconstructions of quantum mechanics cited earlier. First, it is simply easier, in the sense
that our results are obtained with less mathematical effort. (This, notwithstanding the length

Accepted in Quantum 2019-06-24, click title to verify

5

<!-- page 6 -->
of this paper, which owes to the inclusion of many details intended to make the paper easier to
follow.) 3
Secondly, it rests on fewer and (arguably) simpler assumptions. Certainly, the second package
of asumptions (that is, (b0 ) and (c0 ) above) is smaller than anything found in earlier reconstructions
of QM. Other reconstructions tend to impose strong constraints on subsystems, in effect assuming
that every face of the state space corresponds to the state space of a “sub-system”, satisfying the
remaining axioms. Nothing like this is needed here (though, as mentioned above, if one finds a such
a “subspace axiom” compelling, it can be put to good use in the present approach; see Appendix
B for details). A related assumption, also used in several of the cited papers, is that all systems
having the same “information capacity” — the maximal number of states sharply distinguishable
by single-shot measurement — are isomorphic. The present approach entirely avoids such an
assumption. It also does without the assumption, commonly called the no-restriction hypothesis
[21], used in [25] for bits, that all mathematically possible effects — that is, affine functionals
assigning probabilities to states — correspond to physically accessible measurement results. More
recently, the interesting paper [7] derives the same Jordan-algebraic structure arrived at here, but
in a different way. In addition to a strong symmetry postulate, this paper assumes a weak form of
the no restriction hypothesis, namely, that all finite sets of “allowed” effects that sum to the unit
effect (the effect identically 1 on all states) correspond to accessible measurements, along with a
kind of spectral decomposition for states. Here, we manage without any form of no-restriction
assumption, and a spectral decomposition for states is derived, rather than postulated.
Finally, all of the earlier reconstructions of QM cited above assume some form of local tomography. This is the doctrine that the state of a bipartite system is determined by the joint
probabilities it assigns to outcomes of measurements on the two component systems. This principle has a certain intuitive appeal; moreover, it is well known, and easy to see on dimensional
grounds, that among finite-dimensional real, complex and quaternionic quantum mechanics, only
in the complex version are composites locally tomographic.
More generally [19, 8], the only probabilistic theory in which systems correspond to Jordan
models and composite systems are locally tomographic, and which includes at least one system
having the structure of a qubit, is finite-dimensional complex quantum mechanics. Thus, if one insists on local tomography, it can be added to the list of assumptions discussed above, and leads to
standard, complex QM (with superselection rules). One should perhaps not rush to embrace local
tomography as a universal principle, however. The very fact that it excludes real and quaternionic
quantum theory suggests that it is too strong. There are natural ways of representing complex
Hilbert spaces in terms of real or quaternionic ones, and vice versa4 ; moreover, these representations have physical meaning, in that bosonic or fermionic (complex) quantum systems can very
naturally be modelled in terms of the corresponding real or, respectively, quaternionic Hilbert
spaces. Again, see, e.g., [4] a cogent development of this line of thought. In any case, it seems
valuable to be able to delineate clearly what does and what does not depend on this assumption,
particularly if we are interested in the possibilities for a “post-quantum” theory.
3

And also notwithstanding my appeal to the Koecher-Vinberg Theorem, as this is itself a very accessible result.
See [18] for a not terribly taxing proof. A number of the other reconstructions mentioned here also depend on
nontrivial mathematical results, e.g., the classification of transitive actions of compact groups on spheres is used in
[25].
4
A real or quaternionic Hilbert space can be regarded as a complex Hilbert space equipped with a designated antiunitary operator J satisfying, respectively, J 2 = 1 or J 2 = −1; conversely, a complex Hilbert space is essentially
equivalent to a real or quaternionic one equipped with, respectively, an orthogonal or a simplectic operator J
satisfying J 2 = −1 or J 2 = 1.

Accepted in Quantum 2019-06-24, click title to verify

6

<!-- page 7 -->
Organization The balance of this paper is arranged as follows. Section 2 provides general
background on probabilistic models, ordered vector spaces, Jordan algebas and so on, making
more precise many of the technical terms used above. This material will be familiar to many, but
probably not to all, readers. Section 3 contains the proof of Theorem 1; Corollaries 1 and 2 are
proved in Section 4. Section 5 collects some final thoughts, inlcuding a few further remarks on
how the approach of this paper compares to the reconstructions of QM cited above. Appendix A
contains additional information on probabilistic models associated with euclidean Jordan algebras,
and Appendix B shows how a version of the “subspace axiom”, plus a symmetry assumption, can
replace some of the assumptions native to this paper.
Several of the ideas developed here were earlier explored, and somewhat similar results derived,
in [30] and [31], but the approach taken here is much simpler and more direct, and seems to go a
good deal farther.

2 Background
The mathematical framework for this paper is that of “generalized probabilistic theories” [10], in
the idiom of [30, 9], which I now quickly review.5 In a few places, set off in numbered definitions,
my usage differs slightly from that of these last-cited works. See [18, 2] for more information on
ordered vector spaces and Jordan algebras.
Ordered vector spaces An ordered vector space is a real vector space E equipped with a closed,
convex cone E + with E + ∩ −E + = {0} and E = E + − E + — that is, E is spanned by E + .
The cone induces a partial order, invariant under translation and multiplication by non-negative
scalars, given by a ≤ b iff b − a ∈ E + . As an illustration, the space RX of real-valued functions on
a set X is ordered by the cone RX
+ of functions taking non-negative values. Another example is
the space Lsa (H) of hermitian operators on a real, complex or quaternionic Hilbert space, ordered
by the cone of positive semi-definite operators.
A linear mapping T : E → F between ordered vector spaces is positive iff T (E + ) ⊆ F + . If
T is bijective and T −1 is also positive, then T is an order isomorphism. If E and F are finite
dimensional with dim(E) = dim(F ), T is an order isomorphism iff T (E + ) = F + . The dual space
E ∗ of a finite-dimensional ordered linear space carries a natural ordering, defined by the dual
cone, E ∗+ , consisting of positive linear functionals f ∈ E ∗ .
Probabilistic Models As discussed above, a probabilistic model is characterized by a set M(A)
of basic measurements or tests, and a set Ω(A) of states. It is convenient to identify each test
with its outcome-set, so that M(A) is simply a collection of non-empty sets (a test space, in the
language of [9]). Let X(A) stand for the union of this collection; that is, X(A) is the space of
all outcomes of all basic measurements. States are understood as assignments of probabilities to
P
measurement-outcomes, that is, as functions α : X(A) → [0, 1] such that x∈E α(x) = 1 for all
tests E ∈ M(A) (but not all such functions necessarily correspond to states). As mentioned above,
a state α ∈ Ω(A) is non-singular iff α(x) > 0 for all x ∈ X(A). To reflect the possibility of forming
statistical mixtures, I also assume that Ω(A) is convex, that is, if p1 , ..., pn are non-negative real
numbers summing to 1, and α1 , ..., αn are states in Ω(A), then the function p1 α1 + · · · + pn αn also
5

This is a variant of the standard “convex-operational” framework developed in the 1960s and 1970s by Ludwig,
Davies and Lewis and others (e.g., [24, 15, 16]), specialized to finite dimensions, and with additional structure
deriving from work of Foulis and Randall [17].

Accepted in Quantum 2019-06-24, click title to verify

7

<!-- page 8 -->
belongs to Ω(A). Finally, I assume that Ω(A) is closed under pointwise limits, whence, compact
as a subset of [0, 1]X(A) in the product topology.
By way of illustration, in the simplest classical model, M(A) consists of a single, finite test,
and Ω(A) is the simplex of all probability weights on that test. Of more immediate interest to
us is the quantum model A(H) = (M(H), Ω(H)) associated with a complex Hilbert space H.
The test space M(H) is the set of orthonormal bases of H; thus, the outcome-space X(H) is
the set of unit vectors of H. The state space Ω(H) consists of the quadratic forms associated
with density operators on H, so that a state α ∈ Ω(H) has the form α(x) = hWα x, xi for some
density operator Wα , and all unit vectors x ∈ X(H). Real and quaternionic quantum models,
corresponding to real or quaternionic Hilbert spaces, are defined in the same way.
Remark: Not every physically accessible observable on a finite-dimensional quantum system is
represented by an orthonormal basis. Rather, the general observable corresponds to a positiveoperator-valued measure. Similarly, for an arbitrary probabilistic model A, the test space M(A)
may, but need not, represent a complete catalogue of all possible measurements one might make
on the system represented by A: rather, it is some privileged (or perhaps, simply convenient)
catalogue of such measurements, sufficiently large to determine the system’s states.
The spaces V(A) and E(A). Any probabilistic model A gives rise in a canonical way to an
ordered vector space V(A). This is simply the span of the state space Ω(A) in the space RX(A) ,
ordered by the cone V(A)+ of non-negative multiples of states; that is, β ∈ V(A)+ iff β = tα
for some state α ∈ Ω(A) and some real constant t ≥ 0. An element of V(A)+ of the form tα
with α ∈ Ω(A) and t ≤ 1 is said to be sub-normalized. One can show that the interior of V(A)+
consists exactly of multiples of non-singular states. The dimension of a model A is the dimension
of V(A). As mentioned in the introduction, it is assumed in this paper that all probabilistic models
are finite-dimensional.
There is a canonical positive linear functional uA : V(A) → R, called the unit effect of A, given
P
by uA (α) = x∈E α(x), where E is any test in M(A). Note that if α ∈ V(A)+ , then uA (α) = 1
precisely when α ∈ Ω(A), and that every non-zero element α ∈ V(A)+ has the form β = tα for
a unique t = uA (β) > 0. Thus, any non-zero β ∈ V(A)+ can be normalized to yield a state
βe = uA (β)−1 β ∈ Ω(A). A positive linear functional f ∈ V(A)∗+ with f ≤ uA is usually called
an effect on A, and can be thought of as representing an “in-principle” measurement outcome,
with probability 0 ≤ f (α) ≤ 1 in state α. Every outcome x ∈ X(A) corresponds to an effect
P
b : V(A) → R, given by x
b(α) = α(x) for all α ∈ V(A), and uA = x∈E x
b.
x
If A = A(H) is the quantum mechanical model associated with a finite-dimensional Hilbert
space H, as discussed above, then, identifying Ω(H) with the convex set of density operators on
H, V(A) can be identified with the ordered vector space L(H) of self-adjoint operators on H,
with its usual cone of positive operators. We can then also identify V(H)∗ with L(H), using the
trace inner product. That is, if a ∈ L(H), we can define a positive linear functional a ∈ V(A)∗
by setting a(α) = Tr(aα) for all α ∈ V(A) = L(H), and all such functionals arise uniquely from
elements of L(H). In this setting, measurement-outcomes are unit vectors of H, and, for each
b(α) = Tr(αpx ) where px is the rank-one
x ∈ X(H), and for each density operator α on V(A), x
projection associated with x. More generally, effects correspond to positive operators between 0
and 1.
The spectral theorem for self-adjoint operators tells us that every effect in V(A(H)) = L(H)
b corresponding to measurement outcomes. This
is a positive linear combination of functionals x
will not be the case for probabilistic models in general. It is therefore useful to define a smaller
cone, as follows:
Accepted in Quantum 2019-06-24, click title to verify

8

<!-- page 9 -->
b associated with
Definition 2. The space E(A) is the span, in V(A)∗ , of the set of effects x
P
bi , xi ∈ X(A),
outcomes x ∈ X(A), ordered by the cone E(A)+ of finite linear combinations i ti x
with coefficients ti ≥ 0.

Since we are assuming that V(A) and (hence) V(A)∗ are finite-dimensional, the set of funcb in fact spans V(A)∗ (since they separate points of V(A).) Thus, E(A) and V(A)∗ are
tionals x
identical as vector spaces. However, their cones are generally quite different. If a ∈ E(A)+ , then
a(α) ≥ 0 for all α ∈ V(A)+ , so the cone E(A)+ is contained in the dual cone V(A)∗+ , but the
inclusion is usually proper. Thus, E(A) and V(A) are generally distinct as ordered vector spaces.
Remark: The space E(A) will be a useful technical tool in what follows, but should not necessarily
be regarded as anything more than that. In particular, it is not assumed that all physically meaningful effects reside in E(A)+ , nor that every effect in E(A)+ is physically meaningful. In fact, it
will not be necessary to take any position at all on which effects, other than those associated with
measurement outcomes, are physically significant. Thus, as mentioned in the introduction, we
avoid the so-called no-restriction hypothesis [21], namely, the asumption that all effects in V(A)∗+
are physically accessible. This assumption is often made in the literature, sometimes explicitly
(e.g., [25]), sometimes not.
Processes A physical process on a system represented by a probabilistic model A is naturally
represented by an affine (that is, convex-linear) mapping T : Ω(A) → V(A) such that, for every
α ∈ Ω(A), T (α) = pβ for some β ∈ Ω(A) and some constant 0 ≤ p ≤ 1 (depending on α), which
we can regard as the probability that the process occurs, given that the initial state is α.6 Such
a mapping extends uniquely to a positive linear mapping T : V(A) → V(A) with T (α)(uA ) ≤ 1
for all α ∈ Ω(A).
Definition 3. A process T : V(A) → V(A) is probabilistically reversible — hereafter, just preversible7 — iff there is another process, S, such that, for every state α, there exists a constant
p ∈ (0, 1] with S(T (α)) = pα.
In other words, S allows us to recover α from T (α), up to normalization. It is not hard to see
that p must be independent of α, so that S = pT −1 . In particular, T is an order-automorphism
of V(A).
A process T : V(A) → V(B) has a dual action on V (A)∗ , given by T ∗ (f ) = f ◦ T for all
f ∈ V(A)∗ , with T ∗ (uA ) ≤ uA . T is lossless iff T ∗ (uA ) = uA . In our finite-dimensional setting,
we can identify V(A)∗ with E(A) as vector spaces, but not, generally, as ordered vector spaces.
While T ∗ will preserve the dual cone V(A)∗+ , it is not required, a priori, that T ∗ preserve the
cone E(A)+ ≤ V(A)∗ . This reflects the idea that not every physically accessible measurement
need appear among the tests in M(A), as discussed above.
Self-Duality and Jordan Algebras. For both classical and quantum models, the ordered spaces
E(A) and V(A) are isomorphic. In the former case, where M(A) consists of a single test E and
Ω(A) is the simplex of all probability weights on E, we have V(A) ≃ RE and E(A) ≃ (RE )∗ , with
the standard inner product on RE providing the order-isomorphism. If H is a finite-dimensional
6
To be clear, we are not suggesting that all such positive mappings on V(A) represent physically allowable
processes. Indeed, in QM, only completely positive mappings are physically allowable.
7
It should be noted that my usage is slightly nonstandard here: ordinarily, the adjective reversible is reserved
for processes that are probabilistically reversible, in the above sense, with probability one.

Accepted in Quantum 2019-06-24, click title to verify

9

<!-- page 10 -->
real or complex Hilbert space, we have an affine isomorphism between the state space of Ω(H)
and the set of density operators on H, allowing us to identify V(A(H)) with the space Lsa (H)
of self-adjoint operators on H, ordered by the cone of positive operators. For any x ∈ X(H),
b ∈ V(A) is then given by W 7→ hW x, xi = Tr(W Px ). It follows that
the evaluation functional x
∗
E(A(H)) ≃ Lsa (H) ≃ Lsa (H), with the latter isomorphism implemented by the trace inner
product.
More generally, call an inner product h , i on an ordered vector space E positive iff ha, bi ≥ 0
for all a, b ∈ E + . We then have a positive linear mapping E → E ∗ , namely a 7→ ha, ·i. If this
is an order-isomorphism, one says that E is self-dual with respect to this inner product. This is
equivalent to the condition a ∈ E + iff ha, bi ≥ 0 for all b ∈ E + . In this language, the standard
inner product on RE and the trace inner product on Lsa (H) are self-dualizing, for any finite set
E and finite-dimensional Hilbert space H.
In fact, any euclidean Jordan algebra, ordered by its cone of squares, is self-dual with respect
to its canonical inner product. Recall here that a Jordan algebra is a real commutative (but not
necessarily associative) unital algebra (J , ) satisfying the Jordan identity

·
·

··

a · (a2 b) = a2 (a b)

·

for all a, b ∈ J (with a2 = a a). A euclidean Jordan algebra (EJA) is a finite-dimensional Jordan
algebra J equipped with an inner product h , i such that ha b, ci = hb, a ci for all a, b, c ∈ J . This
P
is equivalent to the condition that J be formally real, i.e, that ki=1 a2i = 0 implies ai = 0 for all i.
A EJA J is also an ordered vector space with positive cone J + = {a2 |a ∈ E}, and it can be shown
that this cone is self-dual with respect to the given inner product [18]. Examples of euclidean
Jordan algebras include the space Lsa (H) of self-adjoint operators on a finite-dimensional real,
complex or quaternionic Hilbert space H, with a · b = 21 (ab + ba), and with ha|bi = Tr(ab).
The exceptional Jordan algebra of self-adjoint hermitian matrices over the Octonions is also a
euclidean Jordan algebra. Finally, one obtains a euclidean Jordan algebra, called a spin factor, by
defining on Vn := R × Rn a product (t, x) · (s, y) = (ts + hx, yi, ty + sx). This essentially exhausts
the possibilities: according to the Jordan-von Neumann-Wigner classification theorem [22], every
euclidean Jordan algebra is a direct sum of euclidean Jordan algebras of these five types.
We can associate a probabilistic model to an EJA J in the following way. An idempotent in
J is an element e = e2 . An idempotent is minimal, or primitive, iff for any idempotent f ≤ e,
f = 0 or f = e. Two idempotents e, f are Jordan-orthogonal iff e f = 0. A maximal pairwise
Jordan-orthogonal set {e1 , ..., en } of primitive idempotents summing to the Jordan unit is called
a Jordan frame.

·

·

·

Definition 4. The Jordan model A(J ) = (X(J ), M(J ), Ω(J )) corresponding to a euclidean
Jordan algebra J has X(J ) the set of primitive idempotents, M(J ), the set of Jordan frames of
J , and Ω(J ) the set of states of the form α(x) := ha, xi where a ∈ E(A)+ satisfies ha, 1i = 1. The
P
spectral theorem for EJAs ([18], Theorem III.1.2) expresses every a ∈ J in the form a = x∈E tx x
where E is a Jordan frame. Therefore, J = E(A), and the model A(J ) is self-dual.
Besides self-duality, all euclidean Jordan algebras share a property called homogeneity: the
group of order-automorphisms of J acts transitively on the interior of the positive cone J + .
The Koecher-Vinberg Theorem [18] states that, conversely, any finite-dimensional homogeneous,
self-dual, homogenous ordered vector space J can be equipped with the structure of a euclidean
Jordan algebra.
Definition 5. A probabilistic model A is homogeneous iff V(A) is homogeneous, and self-dual iff
E(A) carries an inner product with respect to which it is self-dual and E(A)+ ≃ V(A)+ , in the
Accepted in Quantum 2019-06-24, click title to verify

10

<!-- page 11 -->
bi defines an element of V(A)+ , and every element of V(A)+
sense that a ∈ E(A)+ iff α(x) := ha, x
arises in this way.

If A is both homogeneous and self-dual — henceforth, HSD — then E(A) is also homogeneous
and self-dual, and thus, by the Koecher-Vinberg Theorem, can be made into a Jordan algebra.
In Appendix A, it is shown that this can be done in such a way that A is actually isomorphic to
the Jordan model corresponding to E(A).
Bipartite States and Conditioning A joint probability weight on a pair of models A and B is
a mapping ω : X(A) × X(B) → R such that, for all E ∈ M(A) and F ∈ M(B),
X

ω(x, y) = 1.

(x,y)∈E×F

Such a weight is said to be non-signaling if, in addition, the marginal weights
ω1 (x) :=

X

ω(x, y) and ω2 (y) :=

y∈F

X

ω(x, y)

x∈E

are well-defined, i.e., independent of the choice of tests F ∈ M(B) and E ∈ M(A), respectively.
The idea is that such a state precludes the sending of signals between A and B based solely on
the choice of what test to perform.
If ω is non-signalling, then given outcomes y ∈ X(B) and x ∈ X(A), we can define conditional
probability weights ω1|y and ω2|x on A and B, respectively, by setting
ω1|y (x) =

ω(x, y)
ω(x, y)
and ω2|x (y) :=
,
ω2 (y)
ω1 (x)

when ω2 (y) and ω1 (x) are non-zero. This gives us the following bipartite law of total probability
[17]
X
X
ω2 (y)ω1|y
(3)
ω1 (x)ω2|x and ω1 =
ω2 =
x∈E

y∈F

which will be exploited below.
Definition 6. Let ω be a non-signaling joint probability weight on A and B. If all conditional
weights ω1|x and ω2|y (and hence, the marginals ω1 and ω2 ) of ω belong to Ω(A) and Ω(B),
respectively, then we say that ω is a bipartite state on the models A and B.
If H and K are real or complex Hilbert spaces, every density operator W on H ⊗ K gives rise
to a bipartite state on A(H) and A(K), given by ω(x, y) = hW x ⊗ y, x ⊗ yi.
The conditioning map If ω is a bipartite state on A and B, define the associated conditioning
b : X(A) → V(B) and ω
b ∗ : X(B) → V(A) by
maps ω
b (x)(y) = ω(x, y) = ω
b ∗ (y)(x).
ω
b (x) = ω1 (x)ω2|x for every x ∈ X(A), i.e., ω
b (x) can be understood as the un-normalized
Note that ω
b ∗ (y).
conditional state of B given the outcome x on A, and similarly for ω
b extends uniquely to a positive linear mapping E(A) → V(B), which
The conditioning map ω
b , such that ω
b (x
b) = ω
b (x) for all outcomes x ∈ X(A). (To see this, consider
I also denote by ω
b ∗ (y))
the positive linear mapping T : V(A)∗ → RX(B) defined, for f ∈ V(A)∗ , by T (f )(y) = f (ω
Accepted in Quantum 2019-06-24, click title to verify

11

<!-- page 12 -->
b, we have T (x
b) = ω1 (x)ω2|x ∈ V(B)+ . Thus, the range of T lies in
for all y ∈ X(B). If f = x
b ∗ defines a positive linear mapping ω
b ∗ : E(B) → V(A). Notice that
V(B).) In the same way, ω
b need not take V(A)∗+ into V(B)+ . This is the principal reason for working with E(A) rather
ω
b : E(A) → V(A) is an order isomorphism, ω is said to be an isomorphism state [5].
than V(A)∗ . If ω

Composite Systems As the language here suggests, one wants to view (some) bipartite states
as elements of the state space of a composite model. Broadly, a composite of two probabilistic
models A and B, is a model AB equipped with a mapping X(A) × X(B) → V(AB)∗+ , taking
every pair of outcomes x ∈ X(A) and y ∈ X(B), to a product effect xy, such that every state
ω ∈ Ω(AB) pulls back to a bipartite state ω(x, y) := ω(xy) on A and B. While nothing in the
mathematical development to follow depends on the choice of such a composite model, questions
of interpretation may hinge on such a choice.

3 Conjugate Systems
Let H be an n-dimensional complex Hilbert space and H is its conjugate space. As discussed
P
in the introduction, the maximally engangled “EPR” state, defined by Ψ = √1n x∈E x ⊗ x,
where E is any orthonormal basis for H, establishes a perfect, uniform correlation betweeen
every projection-valued observable on the system associated with H, and its counterpart on H.
Moreover, Ψ effectively defines the normalized trace inner product on E(H) = Lsa (H). Since it
is precisely this inner product that makes Lsa (H) self-dual, one might guess that the existence of
a uniformly correlating bipartite state is implicated in self-duality more generally.
As a first step, we need to generalize the relationship between the models A(H) and A(H). In
order to do this, as mentioned in the introduction, we need first to impose the minor restriction
that, henceforth, all models are uniform, meaning that all tests have a common cardinality n, and
that the maximally mixed state ρ, given by ρ(x) = 1/n for all x ∈ X(A), belongs to Ω(A). An isomorphism between two models A and B is a bijection φ : X(A) → X(B) such that φ(E) ∈ M(B)
iff E ∈ M(A), and β ◦ φ ∈ Ω(A) iff β ∈ Ω(B). It is straightforward that such a mapping gives
rise to an order isomorphism — which I’ll also denote by φ — from E(A) to E(B), defined by
d for all x ∈ X(A). The following reprises, and makes more precise, the definition of a
b) = φ(x)
φ(x
conjugate system (Definition 1).
Definition 1 (bis) Let A be a uniform probabilistic model of rank n. A conjugate for A is a triple
(A, γA , ηA ) consisting of a probabilistic model A, an isomorphism γA : A ≃ A, and a bipartite
state ηA on A and A such that
(a) ηA (x, γA (x)) = 1/n for every x ∈ X(A).
(b) Every state α ∈ Ω(A) is the marginal of some bipartite state ω on A and A that correlates
some test E ∈ M(A) with its counterpart on A, so that ω(x, γ(x)) = α(x) for every x ∈ E.
As remarked earlier, the marginals of the perfectly correlating state η in part (a) are the maximally mixed states ρ on A and ρ on A and A, respectively. Where no ambiguity is likely, I write
x for γA (x). If A satisfies (a), but not necessarily (b), I will call it a weak conjugate for A.
Given any bipartite state on A and A satisfying (a) i.e., η(x, γA (x)) = 1/n for all x ∈ X(A),
the bipartite state η t defined by η t (x, γ(y)) = η(y, γ(x)) is also perfectly uniformly correlating,
Accepted in Quantum 2019-06-24, click title to verify

12

<!-- page 13 -->
whence, so is the symmetic state (η + η t )/2. We therefore can, and do, assume in what follows
that the chosen correlating state ηA is always symmetric. If A is sharp, it is easy to show that
η is uniquely determined by condition (a) of Definition 1: since η(x, y) = 0 for outcomes y 6= x
belonging to a common test, and η(y, y) = 1/n, we have η1|y (y) = 1, i.e,. η1|y = δy where δy is the
unique state in which y has probability 1. Thus, η(x, y) = δy (x). In this case, therefore, η = η t ,
i.e., η is automatically symmetric.8
If A(H) is the quantum probabilistic model associated with a finite-dimensional Hilbert space,
then the EPR state Ψ turns A(H) := A(H) into a conjugate in this sense, with ηA (x, y) =
|hΨ, x ⊗ yi|2 . In fact, as pointed out in the introduction, A(H) is a conjugate for A(H), since
every density operator is the marginal of a state ΨW correlating an eigenbasis for W with its
conjugate. All of this works equally well for real quantum systems, taking H = H. With a little
care, it can be shown to work for quaternionic systems as well.
Remark: One might wonder whether one can use the isomorphism γA to identify A with its con0 (x, y) = η (x, γ (y)). However, whether
jugate. Certainly one can define a bipartite state ηA
A
A
this corresponds to a legitimate state of any physically reasonable composite AA of A with itself, depends on the particular probabilistic theory at hand. For example, if A = A(H) is the
quantum model associated with a complex Hilbert space H, then (a, b) 7→ Tr(ab) corresponds
to no state on A(H ⊗ H). On the other hand, any choice of an anti-unitary operator J acting
on H yields a unitary isomorphism J : H → H, given by J(x) = J(x) for all x ∈ H. Defining
η 0 (x, y) := |h(1 ⊗ J)−1 Ψ, x ⊗ yi|2 = |hΨ, x ⊗ Jyi|2 gives a state on A(H ⊗ H), correlating along
the anti-unitary isomorphism γ 0 (x) := J −1 x. Thus, whether we choose to treat A(H) as its own
conjugate, or as distinct from its conjugate, is to an extent a matter of convention.
Conjugates and Self-Duality We are now ready to prove Theorem 1, which, for convenience,
I restate. Recall that a model A is sharp iff, for every outcome x ∈ X(A), there is a unique state
δx ∈ Ω(A) with δx (x) = 1. Both classical and quantum models are sharp.
Theorem 1 (bis) Let A be sharp and have a conjugate A. Then ha, bi := ηA (a, γA (b)) is a
self-dualizing inner product on E(A), and induces an order-isomorphism E(A) → V(A) given by
a 7→ ηA (a, · ) for a ∈ E(A). 9
The proof is not difficult. It will be convenient to break it up into a sequence of even easier
lemmas. In the interest of readability, below I conflate x ∈ X(A) with the corresponding effect
b ∈ E(A), and write x for γA (x). Until further notice, the hypotheses of Theorem 1 are in force.
x
The first step is to obtain a kind of weak “spectral” decomposition for states in Ω(A) in terms of
the states δx .
Lemma 1. For every α ∈ V(A)+ , there exists a test E such that
α =

X

α(x)δx

(4)

x∈E

Proof: We can assume that α is a normalized state, i.e, that α ∈ Ω(A). Since A is a conjugate
for A, α = ω1 where ω correlates some test E ∈ M(A) with E ∈ M(A) along the bijection
8
It follows that, where δx and δy are the unique states making x and y certain, we have δy (x) = δx (y) for all
x, y ∈ X(A). Indeed, this last condition could substitute for condition (a) in the definition of η, as it implies that
η(x, y) := δx (y) is a valid non-signaling probabilty weight on A and A.
9

Here, I am identifying V(A), as a vector space, with E(A)∗ .

Accepted in Quantum 2019-06-24, click title to verify

13

<!-- page 14 -->
x 7→ x. By the law of total probability (1) for non-signaling states, α = x∈E ω2 (x)ω1|x . Since ω
P
is correlating we have ω1|x (x) = 1. Thus, by sharpness, ω1|x = δx . Hence, α = x∈E ω2 (x)δx . It
follows that ω2 (x) = α(x) for every x ∈ E, giving us (4). 
P

We will refer to the decomposition in equation (4) as a spectral decomposition for α.
Lemma 2. ηA is an isomorphism state.
Proof: We need to show that ηc
A : E(A) → V(A) is an order-isomorphism. Since E(A) and V(A)
have the same dimension, it is enough to show that ηc
A maps the positive cone of E(A) onto that
of V(A). Since x 7→ x is an isomorphism between A and A, we can apply Lemma 1 to A: if
P
1
α ∈ V+ (A), we have α = x∈E α(x)δx . Since ηA (x, x) = 1/n, we have ηc
A (x) = n δx for every
P
x ∈ X(A). Hence, ηc
A ( x∈E nα(x)x) = α. 
Lemma 3. Every a ∈ E(A) has a representation a =
some coefficients tx .

x∈E tx x for some test E ∈ M(A) and

P

Proof: If a ∈ E(A)+ , then by Lemma 1, ηc
A (a) =
x∈E tx δx for some E ∈ M(A) and coefficients
−1
tx ≥ 0. By Lemma 2, ηbA is an order-isomorphism. Applying ηbA
to the expansion above gives
P
a = x∈E tx x. For an arbitrary a ∈ E(A), we have a = a1 − a2 with a1 , a2 ∈ E(A)+ . Choose
P
N ≥ 0 with a2 ≤ N u. Thus, b := a + N uA = a1 + (N uA − a2 ) ≥ 0. So b := x∈E tx x for some
E ∈ M(A) and thus
P

a = b − N uA =

X

tx x − N (

x∈E

X

x∈E

X

x) =

(tx − N )x. 

x∈E

Lemma 4. The function ha, bi := ηA (a, γA (b)) is an inner product on E(A).
Proof: ηA is bilinear and, by assumption, symmetric. We need to show that h , i is positive
P
definite. Let a ∈ E(A). From Lemma 3, we have a = x∈E tx x for some test E and coeffcients
tx . Now
*

ha, ai =

+
X
x∈E

tx x,

X
y∈E

ty y

=

X

tx ty hx, yi =

x,y∈E×E

X

tx ty ηA (x, y) =

x,y∈E×E

1 X 2
tx ≥ 0.
n x∈E

This is zero only when all coefficients tx are zero, i.e., only for a = 0. 
Proof of Theorem 1, concluded: Lemma 2 tells us that E(A) ≃ V(A), so it remains only to show
that the inner product h , i is self-dualizing. Clearly ha, bi = η(a, b) ≥ 0 for all a, b ∈ E(A)+ .
Suppose a ∈ E(A) is such that ha, bi ≥ 0 for all b ∈ E(A)+ . Then ha, yi ≥ 0 for all y ∈ X. By
P
Lemma 3, a = x∈E tx x for some test E. Thus, for all y ∈ E we have ha, yi = ty ≥ 0, whence,
a ∈ E(A)+ . 
Remarks There are several directions in which we can usefully modify the assumptions of Theorem
1.
(1) In the proof of Theorem 1, the only point at which we needed to assume that A satisfies
condition (b) in the definition of a conjugate was in order to obtain the spectral decomposition
— equation (4) — of Lemma 1. Thus, if we are willing simply to assume such decompositions
are available, as in [7], then a weak conjugate suffices. Alternatively, any postulate or postulates
leading to such decompositions can replace condition (b). For instance, certain versions of the
symmetry and “subspace” axioms used in [20, 14, 25] imply a spectral decomposition. This is
Accepted in Quantum 2019-06-24, click title to verify

14

<!-- page 15 -->
spelled out in Appendix B. Another approach to obtaining such a decomposition can be found in
a recent paper of G. Chiribella and C. M. Scandolo [12].
(2) In fact, it is even enough if (4) holds for states in the interior of Ω(A). From this we have,
◦ , of the cone V(A) is contained in η
bA (E+ ),
as in the proof of Lemma 2, that the interior, V+
+
from which it follows that ηb is a linear isomorphism, and hence (as the vector spaces involved are
finite-dimensional) an homeomorphism. Thus, ηbA (E+ ) is closed, and so, contains the closure of
◦ , i.e., V . In other words, η
b is an order-isomorphism. The proofs of Lemmas 3 and 4, and the
V+
+
rest of the proof of Theorem 1, then proceed just as before.
(3) The definition of a conjugate for a probabilistic model A requires the existence of the
uniformly, universally correlating state ηA , and that arbitrary states of A arise as marginals of
bipartite states on A and A correlating some test E ∈ M(A) with its conjugate twin. One might
wonder whether there is some reasonably simple postulate that will imply both of these conditions. Suppose that G is a group acting transitively on the outcome-space X(A) of the model A,
and leaving the state-space Ω(A) invariant. If G is compact, there will exist an invariant state, ρ,
obtained by group averaging; by the transitivity of G on outcomes, this state must be constant. It
follows that all tests have the same finite size size, say n, and that ρ is the maximally mixed state
ρ(x) ≡ 1/n. That is, the model is uniform. Now let γA : x 7→ x be an isomorphism between A and
a model A. Suppose that every state α ∈ Ω(A) is the marginal of a correlating state ω ∈ Ω(AA)
such that ω(gx, gy) = ω(x, y) for all g ∈ G with α ◦ g = α. It is easily checked that this is satisfied
by finite-dimensional quantum models. Applied to the maximally mixed state ρ, this produces a
perfectly, uniformly correlating state ηA . Thus, A is a conjugate in the sense of Definition 3.

4 Filters
We have just seen that if A is sharp and has a conjugate, then E(A) is self-dual, and isomorphic
to V(A). Suppose now that every non-singular state of A can be prepared, up to normalization,
from the maximally mixed state ρ(x) ≡ 1/n by some reversible process. This guarantees that
V(A), and hence, E(A), is homogeneous, so that, by the Koecher-Vinberg Theorem, E(A) carries
a euclidean Jordan structure making E(A)+ the cone of squares.
In fact, we can say something more interesting. In many kinds of laboratory experiments, the
distinct outcomes of an experiment correspond to physical detectors, the efficiency of which can
independently be attenuated, if desired, by the experimenter. This can always be done through
post-processing, using a classical filter. In QM, it can also be accomplished by subjecting the
system to a suitable process prior to measurement. To see this, let A be a finite-dimensional
quantum system, with corresponding Hilbert space H, and identify E(A) with Lsa (HA ). If E is
an orthonormal basis representing a basic measurement on this system, define a positive operator
1/2
V : H → H by setting V x = tx x for every x ∈ E, where 0 ≤ tx ≤ 1. This gives us a completely
positive linear mapping Φ : E(A) → E(A), namely Φ(a) = V aV . If tx > 0 for every x ∈ E, Φ
has a completely positive inverse Φ−1 (a) = V −1 aV −1 . For each x ∈ E, the corresponding effect
b ∈ E(A) ≃ Lsa (H) is the rank-one projection operator px . It is easy to check that V px V = tx px ,
x
b) = tx x
b for every x ∈ E.
i.e., that Φ(x
Definition 7. A filter for a test E of a probabilistic model A is a positive linear mapping
Φ : V(A) → V(A) such that, for every outcome x ∈ E, there exists a coefficient 0 ≤ tx ≤ 1 with
Φ(α)(x) = tx α(x)
for all all states α ∈ Ω(A). Equivalently, Φ∗ (x) = tx x for every x ∈ E.
Accepted in Quantum 2019-06-24, click title to verify

15

<!-- page 16 -->
As noted above, in QM, not only do filters with arbitrary coefficients exist for every test, but
they can be implemented p-reversibly, so long as the coefficients tx are all non-zero. I will say
that a general probabilistic model with this feature has arbitrary reversible filters.
Corollary 1 (bis) Suppose that A is sharp and has a conjugate A. If A has arbitrary reversible
filters, then E(A) is homogeneous and self-dual.
Proof: A is self-dual by Theorem 1. Let α be a normalized state in the interior of V(A)+ .
P
By Lemma 1, α has a spectral decomposition α = x∈E α(x)δx . Let Φ be a filter for E with
coefficients α(x). Since α is non-singular, α(x) > 0 for all x ∈ E, so Φ can be chosen to be
P
reversible. Now expand the maximally mixed state ρ, with ρ(x) ≡ 1/n, as ρ = x∈E n1 δx . Then
P
Φ(ρ) = n1 x∈E α(x)δx = n1 α. Thus, any non-singular state can be prepared, up to normalization,
by a reversible filter, and it follows that V(A) is homogeneous. In view of Theorem 1, E(A) is
self-dual, and E(A) ≃ V(A), whence, also homogeneous. 
State preparation by reversible filters Suppose now that A has only a weak conjugate A,
and that Φ is a filter for a test E ∈ M(A). By applying Φ to one of the two systems A and A,
we can convert the correlator ηA into a new sub-normalized bipartite state ω, given by ω(x, y) =
ηA (Φ∗ x, y) for all x ∈ X(A), y ∈ X(B). Noticing that Φ∗ (x) = tx x for every x ∈ E, we see that
ω correlates E with E: if x, y ∈ E with x 6= y, we have
ω(x, y) = ηA (tx x, y) = tx ηA (x, y) = 0.
In other words, ω is correlating. It follows that the normalized bipartite state
e :=
ω

1
ω
ω(uA , uA )

is likewise correlating. Since ω1 = Φ(ρ), it follows that any state preparable from ρ by a filter —
] where Φ is a filter and α
e := u 1(α) α — is the marginal
that is, any state of the form α = Φ(ρ),
A
of a correlating state, and hence enjoys a spectral decomposition as in Equation (4). Thus, if
every state is so preparable, the weak conjugate A is actually a conjugate. So, in the presence of
sharpness, we can replace the assumption that the conjugate is strong, by the requirement that
every state be preparable by a filter. In fact, by strengthening this preparability assumption, it
is even possible to omit the hypothesis that A is sharp.
The isomorphism γA : A ≃ A extends to an order-automorphism V(A) ≃ V(A), given by
α 7→ α, with α(x) = α(x) for all x ∈ X(A). Hence, a positive linear mapping Φ : V(A) → V(A)
has a counterpart Φ : V(A) → V(A), given by Φ(α) = Φ(α). Let us say that Φ is symmetric
with respect to ηA iff ηA (Φ∗ (x), y) = ηA (x, Φ∗ (y)) for all x, y ∈ X(A), i.e., iff ηA ◦ (Φ∗ ⊗ idA ) =
∗
ηA ◦ (idA ⊗ Φ ).
Lemma 5 Let A have a weak conjugate A. Suppose that every state of A is preparable by a
symmetric filter. Then ha, bi := ηA (a, γA (b)) is a self-dualizing inner product on E(A).
Proof: Let α = Φ(ρ), where Φ is a symmetric filter for some test E. Consider the bipartite state
∗

ω := ηA ◦ (Φ∗ ⊗ idA ) = ηA ◦ (idA ⊗ Φ ).

Accepted in Quantum 2019-06-24, click title to verify

16

<!-- page 17 -->
For each outcome x ∈ X(A), let δx denote the conditional state (ηA )1|x . Then for all x ∈ E, and
all outcomes y ∈ X, we have
ω1|x (y) =

ηA (Φ∗ (y), x)
ηA (Φ∗ (uA ), x)

=
=
=

ηA (y, Φ∗ (x))
ηA (uA , Φ∗ (x))
ηA (y, tx x)
ηA (uA , tx x)
ηA (y, x)
= (ηA )1|x (y) = δx (y).
ηA (uA , x)

It follows that ω1|x = δx . It is easy to check that ω1 = Φ((ηA )1 ) = Φ(ρ) = α; also, by the law of
P
P
total probability (3), ω1 = x∈E ω2 (x)ω1|x = x∈E tx δx , where tx = ω2 (x). Thus, every state in
Ω(A) is a convex combination of the states δx , and the cone generated by these states coincides
with V(A)+ . It follows that ηb maps E(A)+ onto V(A)+ , as in the proof of Lemma 2. The proof
that ha, bi := η(a, b) defines an inner product on E(A) now proceeds as in the proof of Lemmas 3
and 4. 
In fact, we can do a bit better:
Corollary 2 (bis) Let A have a weak conjugate, and suppose that every interior state is preparable by a reversible symmetric filter. Then A is homogeneous and self-dual.
Proof: The preparability assumption clearly makes V(A) homogeneous. The proof of Lemma 5
shows that all states in the interior of Ω can be decomposed as in equation (4) with respect to
the states δx = η1|x . As noted in Remark (2) following the proof of Theorem 1, this is enough to
secure the self-duality of E(A), and its isomorphism with V(A). 
It follows from the KV theorem that, for any model A satisfying the hypotheses of either
Corollary 1 or Corollary 2, E(A) carries a Jordan product compatible with the inner product
arising from ηA , i.e, E(A) is a euclidean Jordan algebra. In fact, one can prove more: the unit
effect u coincides with the Jordan unit, and M(A) is precisely the set of Jordan frames. In other
words, E(A) is a Jordan moel. The proof is given in Appendix A, where it is also shown that any
Jordan model satisfies the hypotheses of both corollaries. Thus, these two sets of hypotheses are
equivalent, and exactly characterize the class of Jordan models. To summarize:
Theorem 2 For a finite-dimensional, uniform probabilistic model A, the following statements are
equivalent:
(a) A is sharp, has a conjugate, and has arbitrary reversible filters
(b) A has a weak conjugate, and all non-singular states can be prepared by reversible
symmetric filters
(c) A is a Jordan model.
It should be stressed that all of the assumptions going into (a) and (b) are what [7] calls singlesystem postulates, at least to the extent that the existence of a conjugate (or weak conjugate) is
a property of a single system. In any event, these assumptions, whether seen as pertaining to a
single system A or to the pair (A, A), are quite different in flavor from local tomography or the
subspace axiom, which place constraints on an entire theory’s worth of probabilistic models.

Accepted in Quantum 2019-06-24, click title to verify

17

<!-- page 18 -->
5 Conclusion
We’ve seen that either of two related packages of assumptions — given in (a) and (b) of Theorem
2 — lead in a very simple way the homogeneity and self-duality of the space E(A) associated with
a probabilistic model A, and hence, by the Koecher-Vinberg Theorem, to A’s having a euclidean
Jordan structure. While this is not the only route one can take to deriving this structure (see, e.g,
[27] and [31] for approaches stressing symmetry principles), it does seem especially straightforward.
As discussed in the introduction, several other recent papers (e.g, [20, 28, 14, 25, 11]) have
derived standard finite-dimensional quantum mechanics, over C, from operational or informationtheoretic axioms. Besides the fact that the mathematical development here is quicker and easier,
the axiomatic basis is considerably different, and arguably leaner, making no appeal to the structure of subsystems, or to the isomorphism of systems with the same information-carrying capacity,
or to local tomography. The last two points are particularly important: by avoiding local tomography, we allow for real and quaternionic quantum systems; by not insisting that physical systems
having the same information capacity be isomorphic, we allow for quantum theory with superselection rules, and for physical theories in which real and quaternionic systems can coexist. Of
course, the door has been opened a bit wider than this: our postulates are also compatible with
spin factors and with the exceptional Jordan algebra.10
Of the reconstructions cited above, the one having the strongest affinity with the approach of
this paper is that of [11], the key postulate of which is that every state dilates to — that is, arise
as the marginal of — a pure state on a larger, composite system, unique up to symmetries of the
ancillary system. Condition (a) in the definition of a conjugate, requiring that every state dilate
to a correlating state, has a somewhat similar character, albeit with the emphasis on the dilated
state’s correlational properties, rather than its purity. To make the connection more explicit,
suppose we require that every non-singular state α on A dilate to a correlating isomorphism state
ω (which is the case, in the presence of our other assumptions). If µ is another isomorphism
b◦ω
b −1 is a reversible transformation on V(A)
state with the same marginal state α, then φ := µ
b = φ◦ω
b , i.e., µ(a, b) = ω(a, φ(b)) for all a, b ∈ E(A). Now, as shown in [5], if V(A)
with µ
is irreducible as an ordered vector space, isomorphism states are pure. Thus, in the irreducible
case, we have a version of the purification postulate for non-singular states. In view of these
connections, it seems plausible that the approach taken here might be adapted to considerably
simplify the mathematical development in [11]. 11
An assumption that is common to nearly all of the cited earlier reconstructions is some version
of Hardy’s subspace postulate, which requires (roughly speaking) that the result of constraining
a physical system to the set of states making a particular measurement-outcome impossible, also
count as a physical system. This very powerful assumption, while not needed in the development
above, can readily be adapted to the framework of this paper, and can to a large extent replace our
assumptions above about the existence of reversible filters. The details can be found in Appendix
B.
10

It can be shown [6] that the exceptional Jordan algebra can be ruled out on the grounds that one can form no
satisfactory composite of two euclidean Jordan algebras if either has an exceptional direct summand. Whether the
spin factors can also be discarded, or whether they have some physical role to play, remains an open question.
11
Going in the other direction, in [12], the authors derive a version of part (a) of our definition of a conjugate, that
is, the existence of a dilation perfectly correlating two tests, from axioms similar to those of [11]. More recently, in
the conext of a compact closed category of processes, the authors of [29] introduce a stronger, “symmetric” version
of the purification postulate, and show that when combined with suitable versions of sharpness and the existence of
a “classical interface”, this implies that all states can be prepared from the maximally mixed state by a reversible
process, allowing them to prove that their analogue of the cone V(A)+ is homogeneous and self-dual.

Accepted in Quantum 2019-06-24, click title to verify

18

<!-- page 19 -->
It is worth remarking that the subspace axiom applies, not to an indidual probabilistic model
but to a class of probabilistic models, that is, to an entire probabilistic theory. (In the language of
[7], it is not a single-system postulate.) As a rule, one wants to think of a physical theory, not as a
loosely structured class, but as a category of systems, with morphisms corresponding to processes.
To allow for composite systems, it is natural to take this to be a symmetric monoidal category
[1]. This brings us to the interesting question of whether one can construct symmetric monoidal
categories of probabilistic models, in which (say) the hypotheses of Corollary 1 are satisfied by
all systems. This is indeed possible for special Jordan algebras (those not having the exceptional
Jordan algebra as a direct summand). Restricting attention to Jordan models corresponding to
direct sums of real, complex and quaternionic matrix algebras, one can even arrange for this category to be compact closed [5]. This implies that many standard quantum-information theoretic
protocols, notably conclusive teleportation and entanglement-swapping, are still available in this
non-locally tomographic setting. 12

Acknowledgements I wish to thank Giulio Chiribella, Chris Heunen, Matt Leifer and Markus
Müller for helpful comments on earlier drafts of this paper. This work was supported in part by
a grant (FQXi-RFP3-1348) from the FQXi foundation.

References
[1] S. Abramsky and B. Coecke, Categorical quantum mechanics, in D. Gabbay, K. Engesser and
D. Lehman, Handbook of Quantum Logic and Quantum Structures vol II, Elsevier, 2008;
DOI:10.1016/B978-0-444-52869-9.5001-4; arXiv:quant-ph/0402130)
[2] E. Alfsen and F. Shultz, Geometry of state spaces of operator algebras, Birkhäuser, 2003 DOI:
10.1007/978-1-4612-0019-2
[3] C. Aliprantis and D. Toukey, Cones and Duality, Springer, 2007 DOI: 10.1090/gsm/084
[4] J. Baez, Division algebras and quantum theory, Foundations of Physics 42 819-855 (2012)
DOI: 10.1007/s10701-011-9566-z; arXiv:1101.5690
[5] H. Barnum, C. Gaebler and A. Wilce, Ensemble steering, weak self-duality and the structure
of probabilistic theories, Foundations of Physics 43 1411-1437 (2013) doi:10.1007/s10701-0139752-2; arXiv:0912.5532
[6] H. Barnum, M. Graydon and A. Wilce, Some Nearly Quantum Theories, in C. Heunen, P.
Selinger and J. Vicary, eds., Proceedings of the 12th International Workshop on Quantum
Physics and Logic, EPTCS 195 (2015), 59-70 10.4204/EPTCS.195.5; arXiv:1507.06278
[7] H. Barnum, M. Mueller and C. Ududec, Higher-order interference and single-system postulates characterizing quantum theory, New Journal of Physics 16 (2014) DOI: 10.1088/13672630/16/12/123029; arXiv:1403.4147
12

More generally, the existence of conjugate systems is very suggestive of the “caps” that define part of a compact
structure on a symmetric monoidal category (an observation reflected in my choice of the notation η). For a further
development of this connection, see [32]. See also [29] for a reconstruction of finite-dimensional quantum theory from
a “symmetric purification” postulate on the structure of a suitable dagger-monoidal category allowing “classical
control”.)
Accepted in Quantum 2019-06-24, click title to verify

19

<!-- page 20 -->
[8] H. Barnum and A. Wilce, Local tomography and the Jordan structure of quantum theory,
Found. Phys. 44 (2014), 192-212 DOI: 10.1007/s10701-014-9777-1; arXiv:1202.4513
[9] H. Barnum and A. Wilce, Post-classical probability theory, in G. Chiribella and R. Spekkens,
eds., Quantum Theory: Informational Foundations and Foils, Springer, 2017 doi:10.1007/97894-017-7303-4 11; arXiv:1205.3833
[10] J. Barrett, Information processing in generalized probabilistic theories, Physical Review A
75 (2005) DOI: 10.1103/PhysRevA.75.032304; arXiv:quant-ph/0508211
[11] G. Chiribella, M. D’Ariano and P. Perinotti, Informational derivation of quantum theory,
Physical Review A 84 (2011), 012311 DOI: 10.1103/PhysRevA.84.012311; arXiv:1011.6451
[12] G. Chiribella and C. M. Scandolo, Operational axioms for diagonalizing states, in C. Heunen,
P. Selinger and J. Vicary, Proceedings of the 12th International Workshop on Quantum Physics
and Logic, EPTCS 195 (2015) 96-115 DOI: 10.4204/EPTCS.195.8; arXiv:1608.04459
[13] B. Coecke and A. Kissinger, Categorical Quantum Mechanics I: causal quantum processes, in E. Landry, ed., Categories for the Working Philosopher, Oxford, 2017 DOI:
10.1093/oso/9780198748991.003.0012; arXiv:1510.05468
[14] B. Dakic and C. Brukner, Quantum theory and beyond: is entanglement special?
in H. Halvorson, ed., Deep Beauty, Cambridge, 2011 DOI: 10.1017/CBO9780511976971;
arXiv:0911.0695
[15] E. B. Davies and J. Lewis, An operational approach to quantum probability, Communications
in Mathematical Physics 17 (1970) 239-260 DOI: 10.1007/BF01647093
[16] C. M. Edwards, The operational approach to algebraic quantum theory I, Communications
in Mathematical Physics 16 (1970), 207-230 DOI: 10.1007/bf01646788
[17] D. J. Foulis and C. H. Randall, Empirical logic and tensor products, in H. Neunmann (ed.), Foundations of Interpretations and Foundations of Quantum Mechanics, B.I.Wissenshaftsverlag, 1981
[18] J. Faraut and A. Korányi, Analysis on Symmetric Cones, Oxford, 1994
[19] H. Hanche-Olsen, JB algebras with tensor products are C ∗ algebras, in H. Araki et al. (eds.),
Operator Algebras and their Connections with Topology and Ergodic Theory, Lecture Notes
in Mathematics 1132 (1985), 223-229 DOI: 10.1007/BFb0074886
[20] L. Hardy, Quantum theory from five reasonable axioms, arXiv:quant-ph/0101012, 2001
[21] P. Janotta and R. Lal, Generalized probabilistic theories without the no-restriction hypothesis, Physical Review A. 87 (2013) DOI: 10.1103/PhysRevA.87.052131; arXiv:1302.2632
[22] P. Jordan, J. von Neumann and E. Wigner, On an algebraic generalization of the quantum
mechanical formalism, Annals of Mathematics 35 (1934), 29-64 DOI: 10.2307/1968117

Accepted in Quantum 2019-06-24, click title to verify

20

<!-- page 21 -->
[23] M. Koecher, The Minnesota Notes on Jordan Algebras and their Applications, Ed. A.
Krieg and S. Walcher, Springer Lecture Notes in Mathematics 1710, Springer, 1999 DOI:
10.1007/BFb0096285
[24] G. Ludwig, Foundations of Quantum Mechanics, Springer, 1983 DOI: 10.1007/978-3-64286751-4
[25] Ll. Masanes and M. Müller, A derivation of quantum theory from physical requirements,
New Journal of Physics 13 (2011) DOI: 10.1088/1367-2630/13/6/063001; arXiv:1004.1483
[26] M. Mueller and Ll. Masanes, Information-theoretic postulates for quantum mechanics, in
G. Chiribella and R. Spekkens, eds. Quantum Theory: Informational Foundations and Foils,
Springer, 2016 doi:10.1007/978-94-017-7303-4 5; arXiv:1203.451
[27] M. Müller and C. Ududec, The structure of reversible computation determines the selfduality of quantum theory, Physical Review Letters 108 (2012), 130401 DOI: 10.1103/PhysRevLett.108.130401; arXiv:1110.3516
[28] J. Rau, On quantum vs. classical probability, Annals of Physics 324 (2009) 2622–2637 DOI:
10.1016/j.aop.2009.09.013; arXiv:0710.2119
[29] J. Selby, C. M. Scandolo and B. Coecke, Reconstructing quantum theory from diagrammatic
postulates, arXiv:1802.00367
[30] A. Wilce, Four and a half axioms for finite-dimensional quantum theory in Y. Ben-Menahem
and M. Hemmo (eds.), Probability in Physics, Springer, 2012 doi:10.1007/978-3-642-213298 17; arXiv:0912.5530
[31] A. Wilce, Symmetry, self-duality and the Jordan structure of finite-dimensional quantum
theory, DOI: 10.4204/EPTCS.95.19; arXiv:1210.0622
[32] A. Wilce, A shortcut from categorical quantum mechanics to convex operational theories, in
B. Coecke and A. Kissinger (Eds.), 14th International Conference on Quantum Physics and
Logic (QPL), EPTCS 266 (2018) 222-236; DOI: 10.4204/eptcs.266.15; arXiv:1206.2897

A Jordan Models
Let J be a euclidean Jordan algebra. As discussed earlier, this is associated with a probabilistic
model A(J ) = (X(J ), M(J ), Ω(J )), where X(J ) is the set of primitive idempotents (that is,
minimal projections) in J , M(J ) is the set of Jordan frames (maximal pairwise orthogonal sets
of minimal projections), and Ω(J ) is the set of states on (X(J ), M(J )) arising from states on J ,
that is, restrictions to X(J ) of positive, normalized linear functionals on J . Using the self-duality
of J , it’s easy to show that E(A) ≃ J ≃ V(A).
In this appendix, it is shown that any probabilistic model satisfying the conditions of Corollary
1 is actually a Jordan model of this form, and, conversely, that any such Jordan model satisfies
the hypotheses of Corollary 2 (which imply those of Corollary 1).

Accepted in Quantum 2019-06-24, click title to verify

21

<!-- page 22 -->
A.1 Direct Sums and central projections
At several points, we will need to use some basic facts about direct sum decompositions of Jordan
algebras. The direct sum of Jordan algebras J 1 , ..., J n is the algebraic direct sum J = J 1 ⊕· · ·⊕J n
of the vector spaces J i , consisting of n-tuples (a1 , ..., an ) with ai ∈ J i , with the Jordan product
defined by (ai ) (bi ) = (ai i bi ), where i is the Jordan product on the i-th summand. Identifying
a ∈ J i with (ai ) where aj = 0 for j 6= i and aj = a for j = i, we can treat each J i as a subalgebra
P
of J , and write (ai ) ∈ J as ni=1 ai . With this understood, we have a b = 0 if a ∈ Ei and
P
b ∈ Ej with i 6= j. The unit is evidently 1 = ni=1 1i where 1i is the unit in J i . Note that the
canonical projection map πi : J → J i is a Jordan homomorphism. Thus, e ∈ E is an idempotent
P
iff ei := π(e) is an idempotent in J i . As e = i ei , it follows that e is a primitive idempotent iff
e = ei ∈ Ei for some i = 1, ..., n. In other words, every primitive idempotent of J lives in one of
the summands J i .
L
If each J i is a euclidean Jordan algebra with inner product h , ii , then we endow J = i J i
P
with the usual inner product, that is, ha, bi =
i hai , bi ii . where ai = πi (a) and bi = πi (b). Thus,
the summands J i are orthogonal to one another as subspaces of J . A euclidean Jordan algebra
is simple iff it is not isomorphic to a direct sum of non-trivial Jordan algebras. Every EJA is
isomorphic to a direct sum of simple EJAs in an essentially unique way. It will be helpful briefly
to review how this decomposition works. Elements a and b in an EJA J operator commute
with one another iff a (b x) = b (a x) for every x ∈ J , i.e., iff the operators La and Lb of left
Jordan-multiplication by a and b commute. An element of J is central iff it operator-commutes
L
with all elements of J . If J =
i J i , then each of the units 1i ∈ J i is central. Note that
these elements are also idempotents, or projections. A Jordan ideal of an EJA J is a subspace
of the form cJ where c is a central projection, which is then unique. In this case, the mapping
x 7→ c x is a Jordan homomorphism from J onto cJ ; indeed, x 7→ (c x, c0 x) provides a canonical
isomorphism J ≃ cJ ⊕ c0 J . More generally, recall that idempotents e, f in a Jordan algebra are
Jordan-orthogonal iff e f = 0. If {ci } is a maximal pairwise Jordan-orthogonal set of central
P
L
idempotents, then it is straightforward to show that i ci = 1 and, hence, that J ≃
ci J via
the mapping φ : a 7→ (ci a). Moreover, each of the summands J i := ci J is simple. For if ci = p + q
where p and q are central projections in ci J , then p, q are central in J , and are Jordan-orthogonal
to every cj with j 6= i, so {ci }i6=j ∪ {p, q} is a larger pairwise Jordan-orthogonal set of central
projections, a contradiction.

·

·

·

·

··

··

·

· ·

·

A.2 The unit effect as the Jordan unit
Suppose A is a model satisfying the hypotheses of Corollary 1. In particular, then, A is HSD,
so E := E(A) has a Jordan structure. We wish to show that the unit effect u ∈ E(A) is (or
can be taken to be) the Jordan unit, and that each outcome x ∈ X(A) — or, more exactly, the
b — is a primitive idempotent. 13 In fact, we will ultimately establish more,
corresponding effect x
namely, that X(A) corresponds exactly to the set of primitive idempotents, and M(A), to the
set of Jordan frames, of E(A).
In what follows, normalize the inner product on E so that hx, xi = 1 for every x ∈ X(A).
(This is possible, since the inner product arising from a correlator assigns every outcome the same
norm.) Note that we also have hu, xi = 1, and hu, ui = n, the rank of A. Every state α ∈ V(A)
corresponds to a unique a ∈ E(A)+ with α(x) = ha, xi. In particular, ha, ui = 1. Conversely,
13

This can actually be established very directly by appealing to a slightly stronger version of the Koecher-Vinberg
Theorem, as in [8]. The proof given here is more self-contained and elementary.

Accepted in Quantum 2019-06-24, click title to verify

22

<!-- page 23 -->
every a ∈ E(A)+ with ha, ui = 1 corresponds to a state in this way, since E(A) ≃ V(A) as ordered
spaces.
The KV theorem produces a Jordan structure on E(A) in which the Jordan unit, 1, is fixed by
every order-automorphism that is also an orthogonal transformation relative to the inner product.
That is, writing Aut(E) for the group of order-automorphisms and Aut(E)1 for the stabilizer of 1
therein, Aut(E) ∩ O(E) ⊆ Aut(E)1 . Moreover, the stabilizer of 1 in the connected component G
of Aut(E) is then exactly K := G ∩ SO(E) [18]. In particular, every order-automorphism in the
connected component of the identity fixing 1 is an orthogonal transformation with respect to h , i.
In the interest of notational simplicity, from this point on I will identify outcomes x ∈ X(A)
b ∈ E(A), treating each test E ∈ M(A) as a set of
with the corresponding evaluation functionals x
effects.
A.1 Lemma: For each x ∈ X(A), there exists a primitive idempotent ex and a scalar tx > 0
such that x = tx ex , and every primitive idempotent corresponds to an outcome in this way.
Proof: Since A is sharp and hx, xi = hx, ui = 1, we have δx = hx| for every x ∈ X(A); that is,
δx (a) = hx, ai for all a ∈ E(A). In particular, as δx is a pure state, x is ray-extremal for every
x ∈ X(A). Hence, x = tx ex for some primitive idempotent ex . Conversely, since X(A) generates
E(A), every ray-extremal element of E(A)+ must be a multiple of some x ∈ X(A). In particular,
then, each primitive idempotent is a multiple of an outcome, and vice versa. 
Notice that if x and y are distinct outcomes belonging to a common test, we have hex , ey i =
1
2
2
tx ty hx, yi = 0. Hence, 1 = hx, xi = tx kex k , so tx = 1/kex k for every x.

A.2 Theorem: The Jordan product on E(A) can be so chosen that uA is the Jordan unit, 1 and
every x ∈ X(A) is a primitive idempotent.
Proof: We consider in turn the case in which E(A) is simple and the general case in which E(A)
is a direct sum of simple ideals. Throughout, we write u for uA .
Case 1: E(A) is simple. By [18] Corollary IV.2.7, the group K := G ∩ SO(E), where G
is the connected component of the identity in Aut(E), acts transitively on the set of primitive
idempontents. Since K consists of orthogonal transformations, all primitive idempotents have
the same norm. It follows that, for E simple, kek ≡ c > 0 for all primitive idempotents, whence,
that we have tx ≡ t = 1/c for all x. That is, if E(A) is simple, x = tex for every x ∈ X(A).
Now redefine the Jordan product on E by setting a ◦ b := t−1 a b. It is easy to check that this
gives a Jordan product defining the same positive cone, with unit 10 := t1. Also note that the
new Jordan product continues to ineract with the given innner product in the desired way, i.e.,
ha ◦ b, ci = hb, a ◦ ci for all a, b, c ∈ E. We also have, for each outcome x ∈ X(A),

·

·

·

x ◦ x = t−1 (tex tex ) = t(ex ex ) = tex = x,
so x is an idempotent with respect to this new Jordan product; moreover, since the positive cone
is unchanged, this is still ray-extremal, hence, a primitive idempotent. We now have
hx, 10 i = hx2 , 10 i = hx, xi = 1.
By the spectral decomposition for states (equation (4)), we have 10 =

Accepted in Quantum 2019-06-24, click title to verify

P

x∈E sx x for some test

23

<!-- page 24 -->
E ∈ M(A) and coefficients sx . But for every x ∈ E,
sx =

X

sy hx, yi = hx, 10 i = 1,

y∈F

so 10 =

P

x∈E x = uA .

Case 2: E(A) a direct sum of simple ideals. Let E = ki=1 Ei where each Ei is a simple Jordan
algebra. By Lemma A.1, we still have a correspondence x 7→ ex between outcomes x ∈ X(A) and
primitive idempotents ex ∈ E, with x = tx ex for some tx > 0. As remarked earlier, each primitive
idempotent lies in a unique summand Ei whence, the same is true for outcomes. The argument
given above shows that, for all x ∈ Ei , we have tx = ti for a constant ti > 0 depending only on
the summand. Adjusting the Jordan product on each summand as in Case 1, we obtain a new
Jordan product on E given by
X
(ai ) ◦ (bi ) =
t−1
i ai bi
L

·

i

rendering each x ∈ X(A) ∩ Ei — and hence, each outcome x ∈ X(A) — a primitive idempotent. By the same argument as in Case 1, we have hx, 1i = 1 for all x ∈ X. Expanding
P
1 = x∈E sx x for some test E ∈ M(A), we then have (again, just as in the irreducible case) that
P
1 = hx, 1i = y∈E sy ix, yi = sx , whence, sx = 1 for all x ∈ E, and hence, 1 = uA . 
From now on, we treat uA as the Jordan unit of E(A) without further comment, and revert
to writing u, rather than 1, for the unit in an abstract Jordan algebra. It will be convenient at
this point to adopt the notation x ⊥ y to indicate that two outcomes x, y ∈ X(A) are distinct
and belong to a common test.

·

A.3 Corollary: Let x, y ∈ X(A). Then x ⊥ y ⇒ x y = 0.

·

Proof: By [2], Prop. 2.18, if p, q are projections in an EJA, then p ≤ u − q implies p q = 0. By
Proposition A.2, x and y are projections. If x ⊥ y, then x + y ≤ u, so x ≤ u − y. .

·

Idempotents p, q in a Jordan algebra are Jordan-orthogonal iff p q = 0. Recall that a Jordan
frame in an EJA E is a set E of non-zero Jordan-orthogonal primitive idempotents summing to
the unit. It follows from Proposition A.2 and Corollary A.3 that every test in M(A) defines a
Jordan frame in E(A). We now show that, conversely, every Jordan frame in E(A) belongs to
M(A).
A.4 Theorem: Let A be any probabilistic model satifsying the hypotheses of Corollary 1 or of
Corollary 2, and let E(A) have the Jordan structure in which uA is the Jordan unit, as per Lemma
A.2. Then every Jordan frame of E(A) corresponds to a test in M(A). Hence, A is a Jordan
model.
Proof: Theorem A.2 and Corollary A.3 tell us that the set X(A) of outcomes of A is exactly the
set of primitive idempotents (still continuing to identify outcomes with the corresponding effects),
and that every test E ∈ M(A) is a Jordan frame of E(A). The Spectral Theorem for euclidean
Jordan algebras ([18] Theorem III.1.1) tells us that if J is any EJA with unit u and a ∈ J , then
there exists a unique family of mutually Jordan-orthogonal non-zero idempotents ei and distinct
P
coefficients si , such that a = i si ei . Suppose the idempotents ei are primitive, and that a can
Accepted in Quantum 2019-06-24, click title to verify

24

<!-- page 25 -->
P

also be expanded as j tj fj for some pairwise Jordan-orthogonal non-zero idempotents fj and
coefficients tj (not a priori distinct). Then by collecting those terms with common coefficients, we
P
P
can also write a = k kpk where pk = {fj |tj = k}. Since the fj are pairwise Jordan-orthogonal
idempotents, it is easy to check that pk is also an idempotent, with pk pk0 = 0 for k 6= k 0 . It
follows from the uniqueness of the spectral expansion that, for each k, there is some i with k = si
P
and pk = ei . Since ei is primitive, this means that the sum pk = {fj : tj = k} has a unique
term, call it fji , with fji = ei . It follows that the coefficients tj were after all distinct, and the
projections fj coincide with the projections ei . In other words, if a can be expanded with dinstinct
coefficients relative to some family of mutually orthogonal primitive idempotents, it can have no
other such expansion in terms of mutually orthogonal idempotents, with any coefficients. Now
let F = {e1 , ..., en } be a Jordan frame of E(A). Choosing distinct coefficients si , i = 1, ..., n, let
P
a = i ti ei . By our spectral decomposition for HSD models (equation (4)), there exists a test
P
E ∈ M(A) and coefficients tx , x ∈ E such that a = x∈E tx x. Since E is a Jordan frame, the
uniqueness result above tells us that E = F . Thus, every Jordan frame of E(A) is a test in M(A),
as advertised. 

·

A.3 Conjugates and Filters for Jordan Models
As discussed in Section 5, the question of what it means, physically, to say that a given system
has a conjugate really depends on the probabilistic theory — and the notion of composite system
— with which one is concerned. But if we are content to interpret this idea very broadly, we can
understand the composite AA as the “maximal” tensor product A ⊗max A [9], the states of which
are simply the positive, normalized bilinear forms on E(A) × E(A). In particular, if A = A(J )
is the model associated with a euclidean Jordan algebra J , the canonical inner product on J ,
normalized so that hu, ui = 1, supplies exactly the needed bilinear form. Thus, every Jordan
model can be regarded as its own weak conjugate. (At least, this is so if we construe “A has
a weak conjugate” to mean only that there exists a perfectly correlating positive, bilinear form
on E(A) — mathematically, a weaker condition than that A have a conjugate in any particular
probabilistic theory.)
We now show that Jordan models support arbitrary filters, and that every state of such a
model can be prepared by a symmetric filter. For any element a of a euclidean Jordan algebra J ,
the operator Ua : J → J defined by
Ua (x) := 2a · (a · x) − a2 · x
is positive ([2] Theorem 1.25). If J is special, i.e., if J consists of self-adjoint operators on a real,
complex or quaternionic Hilbert space H, with a · b = 21 (ab + ba), one can check that Ua (x) = axa.
P
Below, we shall see that if a = x∈E tx x, where E is a Jordan frame, then Ua is a filter with
coefficients tx .
Let J be an EJA. An element a ∈ J is invertible iff there exists an element b of the associative
sub-algebra generated by a and u, such that a b = u. This element, which is clearly unique, is
then the inverse of a, denoted by a−1 . The following collects some facts about invertibility that
will be needed in a number of places below.

·

A.5 Proposition: The following are equivalent:
(a) a is invertible;
(b) There exists some b ∈ J with a b = u and a2 b = a;
(c) Ua is invertible. In this case, Ua−1 = Ua−1 .

·

Accepted in Quantum 2019-06-24, click title to verify

·

25

<!-- page 26 -->
Proof: That (a) implies (b) is clear. That (b) implies (a) is a consequence of the fact (the ShirsovCohn Theorem; see [2], Proposition 1.14) that the Jordan algebra generated by two elements and
u is special, plus the fact that (a) and (b) are equivalent in special Jordan algebras. See [2] Lemma
1.16 and Proposition 1.17 for details. The equivalence of (a) and (c) is Lemma 1.23 in [2]. 
We shall also need the following elementary observation:
P

A.6 Lemma: If a has a spectral decomposition a = x∈E tx x where E is a Jordan frame and
tx 6= 0 for all x ∈ E, then a is invertible. In particular, a is invertible if lies in the interior of J + .
Proof: By spectral theory, a = x∈E tx x where E is a Jordan frame. If tx 6= 0 for all x, let
P
−1
b = x∈E t−1
x x = f (a) where f (x) = x , so that b ∈ C(a, u), the Jordan subalgebra generated
by a and u. Observe that, by the Jordan-orthogonality of elements of a Jordan frame,
P

·

a b=

X

·

tx t−1
y x y =

x,y∈E

X
x

tx t−1
x x=

X

x = u.

x∈E

Thus a is invertible with inverse b. 
A.7 Lemma: Let J be any EJA. Every state of the model A(J ) is preparable by symmetric filter,
and every non-singular state, by a reversible symmetric filter.
Proof: Let α be any state on J . By self-duality, there exists a unique w ∈ J + with α(b) = hw, bi
P
for all b ∈ J . The spectral theorem gives us a Jordan frame E and a decomposition w = x∈E tx x.
P
1/2
Let a = x∈E tx x ∈ J + : then we have Ua (u) = w and Ua (x) = tx x for every x ∈ E, so Ua is a
filter. Since left multiplication by a is self-adjoint with respect to the inner product on J , so is
Ua , whence, Ua is a symmetric filter. Finally, if w lies in the interior of J + , then the coefficients
1/2
tx , and hence also tx , are all strictly positive. Thus, a is invertible by Lemma A.5, and thus Ua
is invertible with inverse Ua−1 , again a positive operator, by Proposition A.5. 
As noted in the discussion preceding Lemma 5, every state preparable by a symmetric reversible filter is the marginal of a correlating state. Hence, every Jordan model is its own (strong)
conjugate. Since such a model is evidently sharp, the conditions of Corollary 1 are satisfied. This
proves Theorem 2: every probabilistic model satisfying the hypotheses of Corollary 1 or Corollary
2 is a Jordan model, and every Jordan model satisfies the hypotheses of both Corollaries.

B Symmetry and Subspace Axioms
In most other recent reconstructions of QM [20, 14, 25, 11], one encounters some version of a
subspace axiom. Informally, the idea is that if we constrain the states of a given system so as to
render a certain measurement result impossible, we obtain what amounts the state space of a new
system in its own right, to which any other axioms must then apply. In practice, the subsets of the
state space arising in this way are (some of the) faces of the larger state space14 . An assumption
of this sort was made by Hardy [20], and, following his lead, is also central in reconstructions by
Dakic and Brukner [14], Masanes and Mueller [25] and Chiribella, D’Ariano and Perinotti [11],
although the precise formulation varies somewhat from one set of authors to another.
14
Recall that a face of a convex set K is a convex set F ⊆ K such that for all α, β ∈ K and all t ∈ (0, 1),
tα + (1 − t)β ∈ F implies α, β ∈ F .

Accepted in Quantum 2019-06-24, click title to verify

26

<!-- page 27 -->
In this Appendix it is established that, for uniform probabilistic models, a certain version of
this subspace axiom, plus a very reasonable compactness assumption, enforce a spectral decomposition of states (equation (4) in Section 3). Thus, these assumptions can replace condition (b)
in the definition of a conjugate, at least as far as Theorem 1 is concerned. Moreover, a stronger
version of the subspace axiom, which seems about equally well motivated, implies the existence
of arbitrary reversible filters. Combined with a rather weak and operationally natural symmetry
assumption, this in turn yields the homogeneity of the space V(A). In the presence of weak
conjugates, it follows that V(A) is both homogeneous and self-dual.
Probabilistic Theories Before proceeding, it will be important to clarify the term “probabilistic
theory”, up to this point used rather freely and informally. In the very broadest sense, a probabilistic theory is simply a class of probabilistic models, together with some designated processes
that are singled out for study. But allowing for the composition of processes, and assuming that
identity operators count as processes, it is very natural to assume that a probabilistic theory is a
category of probabilistic models and processes. This is the point of view taken in the “categorical
quantum mechanics” programme of Abramsky, Coecke and others [1]. It is also usual in this
context also to assume that this category has a (symmetric) monoidal structure, allowing for the
formation of composite systems. However, for my purposes, it will be enough to require only that
we are given a class C of probabilistic models and, for each model A ∈ C, a preferred monoid
Proc(A) of allowed processes, i.e., positive linear mappings T : V(A) → V(A) with uA (T (α)) ≤ 1
for all α ∈ Ω(A).15
We continue to identify outcomes with the corresponding effects, regarding X(A) as a subset
of E(A) and M(A), as a collection of subsets of E(A). We can then define a symmetry of A to be
a dual process g = φ∗ where φ ∈ Proc(A) is invertible, such that gM(A) = M(A). I will write
G(A) for the set of all symmetries of A, noting that this is a group. As above, we use the notation
x ⊥ y to indicate that x and y are distinct outcomes belonging to a common test. Notice that
this does not (yet) imply that x and y are orthogonal with respect to any inner product on E(A).

B.1 The Subspace Axiom and Spectrality
Masanes and Mueller’s Framework In the reconstruction due Masanes and Mueller [25],
one begins by specifying the state-space of a physical system, taken to be a finite-dimensional
compact convex set Ω. Measurement results are associated with effects, i.e., affine functionals
a : Ω → R with 0 ≤ a(α) ≤ 1 for all α ∈ Ω. Of course, a(α) is understood as the probability of
the result associated with a being obtained, when the system’s state is α. Masanes and Mueller
do not assume that all effects correspond to physically realizable measurement results, but do
seem, tacitly, to define a measurement to be any list a1 , ..., an of allowed effects that sum to the
unit effect u (where u(α) = 1 for all α ∈ Ω(A)). Further assumptions, explicit in [26], are that
the set of allowed effects is topologically closed, convex, and closed under a 7→ u − a. Masanes
and Mueller call states α1 , ..., αn ∈ Ω(A) perfectly distinguishable iff there exist affine functionals
ai : Ω → R with 0 ≤ ai (α) ≤ 1, representing measurement results, such that a1 + · · · + an = u,
where u is the unit effect (u(α) = 1 for all α ∈ Ω) and ai (αj ) = δi,j for all i, j = 1, ..., n. The
information capacity of the system is the maximum size of such a perfectly distinguishable set
of states. A complete measurement is a measurement that perfectly distinguishes a maximum
15

We can, of course, regard this as a degenerate category in which there are no morphisms between different
objects. My intention, however, is simply to leave it open which mappings between different systems count as
processes, as nothing will depend on this. This is another respect in which the approach taken here is “singlesystem”.
Accepted in Quantum 2019-06-24, click title to verify

27

<!-- page 28 -->
number of states. In the actual development of their results, they effectively take M(A) to be
the set of complete measurements in this sense.
Masanes and Mueller’s Subspace Axiom Here is how Masanes and Mueller explain their
version of the subspace axiom in [26]:
Postulate 2 (Equivalence of subspaces). Let SN and SN −1 be systems with capacities N and N − 1, respectively. If E1 , ..., EN is a complete measurement on SN ,
then the set of states ω ∈ SN with EN (ω) = 0 is equivalent to SN −1 .
The notion of equivalence needs some discussion. Postulate 2 states the equivalence
of SN −1 and
0
SN
−1 := {ω ∈ SN |EN (ω) = 0}.
Denote the real linear space which contains SN by VN ; define VN −1 analogously, and
0
set VN0 −1 := Span(SN
−1 ). Equivalence means first of all that there is an invertible
0
linear map L : VN −1 → VN0 −1 such that L(SN −1 ) = SN
−1 . But it also means that
transformations ... on one of them can be implemented on the other... To be more
0
0
specific, define GN −1 as the set of transformations in SN that preserve SN
−1 ...
0

0
0
GN −1 := {T ∈ GN | T SN
−1 = SN −1 }.

The set of reversible transformations G0N −1 is defined as the restriction of all these
0
transformations to SN
−1 ...
A Reformulation Returning to our own formalism, suppose that x ∈ X(A), and let
Fx := { α ∈ Ω(A) | α(x) = 0 }.
Note that this is a face of Ω(A), corresponding exactly to the restricted state space contemplated
in Masanes and Mueller’s subspace axiom. If we wish to treat this as the state space of a model
in our sense, we must associate a test space with it. The simplest option is to define, for x ∈ X,
M(A)x = { E \ {x} | E ∈ M(A) with x ∈ E}.
Notice that the outcome-space of M(A)x is the set of outcomes in X(A) that are distinguishable
from x; that is, the union of the tests in M(A)x is the set { y ∈ X(A) | y ⊥ x }.
In the
special case of a quantum model, say A = A(H), this is the right definition, since if K = x⊥ is
the subspace of H orthogonal to a unit vector x, then any frame F ∈ M(K) extends to a frame
E = F ∪ {x} of H, so that M(K) = M(H)x .
Any state α ∈ Fx defines a probability weight αx on M(A)x , simply by restricting α to
S
outcomes in M(A)x , i.e., to outcomes y ∈ X(A) with y ⊥ x. The mapping α 7→ αx is obviously affine, but in general is not injective. For a simple example, consider the “square bit”:
M(A) = {{x, x0 }, {y, y 0 }}, with Ω(A) the set of all probability weights thereon. Then Ω(A) is
isomorphic to the unit square in R2 under the mapping α 7→ (α(x), α(y)). The face Fx can be
identified with the right-hand face of the square, i.e., Fx = {(0, t)|0 ≤ t ≤ 1}. On the other
hand, M(A)x is the trivial test space {{x0 }}, which has only a single probabilty weight. We
will therefore need to assume that M(A)x is large enough to separate points of Fx , i.e., that if
α, β ∈ Fx are distinct, then there exists some y ⊥ x with α(y) 6= β(y). This makes α 7→ αx an
injection, so that we can identify Fx with a set of probability weights on M(A)x .

Accepted in Quantum 2019-06-24, click title to verify

28

<!-- page 29 -->
With this in mind, the following now seems to capture the spirit of Masanes and Mueller’s
axiom:
Definition B.1 Say that a probabilistic theory C has the subspace property iff, for every A ∈ C
and every x ∈ X(A),
(i) M(A)x separates points of Fx ,
(ii) The model Ax := (M(A)x , Fx ) belongs to C, and
(iii) every symmetry in G(Ax ) extends to a symmetry g ∈ G(A) with gx = x.
As an example, let A = A(H) be the quantum model associated with a Hilbert space H. If
x ∈ X(H) is a unit vector, then Fx is the set of density operators W such that Tr(W x) = 0,
or, equivalently, such that P W P = W where P is the orthogonal projection onto the subspace Kx = x⊥ orthogonal to x. In this case M(A)x is the set of orthonormal bases of K,
so M(A)x = M(K), and A(H)x = A(Kx ).
Lemma B.2 Let C be a probabilistic theory with the subspace property, in which every model is
uniform. Then every model in C is sharp.
Proof: By induction on rank. Clearly, all models of rank 1 are sharp. Assume the result holds for
all models of rank n or lower. Suppose A has rank n + 1 (with n > 0), and let x ∈ X(A). Since
n + 1 > 1, we can find some y ⊥ x. Since Ay ∈ C has rank n, Ay is sharp. Therefore, there exists
a unique δx ∈ Fy — and hence, a unique δx ∈ Ω(A) — with δx (x) = 1. 
Remark: This is the only use we make of Condition (i) in Definition B.1. If one is content to
assume that every model in C is sharp, this condition can be dispensed with.
When dealing with finite-dimensional probabilistic models, one usually assumes that the statespace Ω(A) is compact. It is equally natural to suppose that X(A) is compact in the topology
inherited from E(A) — equivalently, in, the coarsest topology making every state α : X(A) → [0, 1]
continuous. This is certainly the case for quantum models, where X(A) is the unit sphere in
a finite-dimensional Hilbert space, and can be shown to hold for the test space of “complete
measurements” considered (implicitly) in [25].
Let us say that a probabilistic model A is spectral if it is sharp, and every states α ∈ Ω(A)
P
has a spectral decomposition α = x∈E α(x)δx for some E ∈ M(A).
Proposition B.3 Let C be a probabilistic theory with the subspace property, in which all models
are uniform and have compact outcome-spaces. Then every model in A is spectral.
Proof: By induction on the rank of A ∈ C. Spectrality is trivial for models of rank 1 (which have
only a single state). Assume the result holds for all A ∈ C having rank < n = rank(A). Let
α ∈ Ω(A). Since X(A) is compact and α is continuous on X(A), α takes its minimum value, m,
0 ≤ m < 1, at some point xo ∈ X(A). Thus, β := α − mδxo is non-negative on X(A), hence,
belongs to V(A)+ . Now, uA (β) = 1 − m, so β1 := (1 − m)−1 β ∈ Ω(A), and α = (1 − m)β1 + mδxo .
Since β1 (xo ) = 0, β1 belongs to the face Fxo := {α ∈ Ω(A)|α(xo ) = 0}. Because C has the subspace
property, Axo belongs to C. Since Axo has rank n − 1, our inductive hypothesis implies that
P
β1 = y∈F β1 (y)δy for some F ∈ M(Ax ) = M(A)x , i.e., for some F = E \ {xo }, xo ∈ E ∈ M(A).

Accepted in Quantum 2019-06-24, click title to verify

29

<!-- page 30 -->
But now
α = (1 − m)β1 + mδxo =

X

(1 − m)β(y)δy + mδxo

y∈F

which gives a spectral decomposition for α. 
Remarks: Subspace axioms are usually paired with a conceptually distinct requirement that all
systems of a given information capacity are isomorphic. This immediately rules out any nonclassical theory involving superselection rules, or in which there are more than one kind of “bit”.
As we do not impose such an isomorphism requirement, we avoid this restriction.

B.2 Subspaces plus symmetry
In addition to one or another version of subspace postulate, [20, 14, 25, 11] also assume that every
model A to carries a preferred group G(A) of symmetries, understood as acting on the state space,
which is consistent with our choice of G(A) in the previous section. The first three of the cited
papers assume a symmetry postulate requiring that G(A) act transitively on pure states, i.e., on
the extreme points of Ω(A). This is also a consequence of the “purification postulate” used in [11].
Definition B.4 A probabilistic model A is symmetric iff G(A) acts transitively on X(A). If A is
sharp and all pure states are of the form {δx |x ∈ X(A)}, this implies G(A) also acts transitively
on pure states.
As an example, let A = A(H) be the quantum model associated with a Hilbert space H. As
discussed earlier, this means that M(A) is the set of orthonormal bases of H, X(A) is (therefore)
the unit sphere of H, and Ω(A) is the set of density operators on H. If we take G(A) to be the
group of unitary operators on H, then G(A) certainly acts transitively on X(A).
Notice that, in this example, G(A) acts transitively also on M(A). In [30] and elsewhere, a
uniform test space with a preferred group of symmetries G(A) is said to be fully symmetric if, for
every pair of tests E, F ∈ M(A) and every bijection f : E → F , there exists an element g ∈ G(A)
such that gx = f (x) for every x ∈ E. If A has rank n, we can define an ordered test to be an
n-tuple (x1 , ..., xn ) ∈ X n where {x1 , ..., xn } ∈ M(A). Then full symmetry is the condition that
G(A) act transitively on ordered tests, where g(x1 , ..., xn ) = (gx1 , ..., gxn ).
Lemma B.5 Suppose that C has the subspace property. If every A ∈ C is uniform and symmetric,
then every A ∈ C is fully symmetric.
Proof: Every symmetric model of rank 1 is trivially fully symmetric. Suppose every model in C
having rank ≤ n is fully symmetric, and let A ∈ C be a model of rank n + 1. Let (xo , ..., xn )
and (yo , ...yn ) be any ordered tests of A. By symmetry, we can find some go ∈ G(A) such that
go xo = yo . Now (y1 , ..., yn ) and (go x1 , ...., go xn ) are both ordered tests of Ayo . By our induction
hypothesis, Ayo is fully symmetric, so there exists some g1 ∈ G(Ayo ) with yi = g1 go xi for every
i = 1, ...., n. By the subspace property, g1 extends to a symmetry g ∈ G(A) with gyo = yo and
gz = g1 z for every z ⊥ yo — in particular, ggo xi = g1 go xi = yi for i = 1, ...., n. Hence, ggo takes
(xo , ...., xn ) to (yo , ..., yn ). 

Accepted in Quantum 2019-06-24, click title to verify

30

<!-- page 31 -->
B.3 A Strengthened Subspace Postulate
Since we are considering physical processes φ ∈ Proc(A) that need not be normalization-preserving
(in particular, need not be associated with symmetries in G(A)), the following stronger version
of the subspace property seems quite as well-motivated a the weaker version discussed above.
Definition B.6 Let C be a probabilistic theory in which all systems are sharp. Say that C has
the strong subspace property (SSP) iff, for every system A ∈ C and every test E ∈ M(A), if x ∈ E,
then (i) Ax ∈ C and (ii) any (reversible) process φ ∈ Proc(Ax ) lifts to a (reversible) process in
Proc(A) fixing δx .
Note that the significant difference here from the subspace property of Definition B.1 is the
requirement that all processes on Ax , and not only symmetries, lift to processes on A, which can
be taken to be reversible if the original processes are.
Lemma B.7 If C satisfies the SSP, every model in C has arbitrary reversible filters.
Proof: A system of rank 1 automatically has arbitrary filters: the only test has a single outcome,
x, and there is just one state, δx . The mapping δx 7→ tx δx defines a p-reversible positive mapping
on V(A) ≃ R.
Now suppose, for purposes of induction, that every system of rank < n has arbitrary reversible
filters. Let E be a test, and let φE : V(E \ {x}) → V(E \ {x}) be a filter with φ(δy ) = ty δy for
all y ∈ E \ {x}. Extend this to φ : V(A) → V(A) fixing δx . Now let z ∈ E \ {x}. Repeating the
argument, find ψ a filter on A with ψ(δy ) = δy for all y ∈ E \ {x} and ψ(δx ) = tx δx with tx < 1.
(In other words, for z ∈ E \ {y}, we have tz = 1 if z 6= x and tx the given value.) Composing, we
have a positive mapping with
(ψ ◦ φ)(δz ) = ψ(tz δz ) = tz ψ(δz ) = tz δz
for z 6= x, and
(ψ ◦ φ)(δx ) = ψ(δx ) = tx δx .
Thus, we have arbitrary p-reversible filters. 
In [30], it is shown that the existence of arbitrary reversible filters plus full symmetry implies
the homogeneity of the state space. So we have
Proposition B.8 Let C satisfy the SSP. If every A ∈ C is symmetric, then for every A ∈ C,
V(A) is homogeneous.
Proof: By Lemma B.7 above, we have arbitrary reversible filters; by Lemma B.5 in previous subsection, every A ∈ C is fully symmetric. 
The proofs of Theorem 1 and Corollary 1 imply that, in the presence of a spectral decompostion for states, sharpness, the existence of a weak conjugate, and the existence of arbitrary
reversible filters are enough to secure the self-duality of E(A). Thus, Propositions B.3 and B.8
gives us a third route to Jordan models, to put alongside Corollaries 1 and 2 in the main body of
this paper:

Accepted in Quantum 2019-06-24, click title to verify

31

<!-- page 32 -->
Corollary B.9 Let C satisfy the SSP. If every model A in C has a compact outcome-space X(A),
is symmetric and has a weak conjugate, then A is homogeneous and self-dual, and hence, a Jordan
model.

B.4 Jordan models and the SSP
The preceding results provide an alternative route from four operationally meaningful axioms
— sharpness, symmetry, the SSP and the existence of weak conjugates — to euclidean Jordan
algebras. The question remains whether all EJAs arise in this way. In fact, the full symmetry
enforced by Lemma B.5 significantly constrains the possibilities.
B.10 Lemma: Let A = A(J ) be the Jordan model associated with a Jordan algebra J . If A is
fully symmetric, then J is either simple, or a direct sum of one-dimensional Jordan algebras.
Proof: Suppose J = ni=1 J i where J 1 , ..., J n are simple euclidean Jordan algebras, with n ≥ 2.
S
Let Ei be a Jordan frame for J i ; then E = ni=1 Ei is a Jordan frame for J . Let x1 ∈ E1 and
x2 ∈ E2 . By full symmetry, there exists a symmetry g ∈ G(A) such that gx1 = x2 , gx2 = x1 ,
and gy = y for all y ∈ E \ {x1 , x2 }. Now let pi be the central projection associated with the i-th
summand, so that p1 and p2 are the central covers of (the smallest central projections above) x1
and x2 , respectively. Hence, g(p1 ) is the central cover of gx1 = x2 , i.e, g(p1 ) = p2 , and similarly
gp2 = p1 . But now if y ∈ E1 is any point other than x1 , we have y = gy ≤ gp1 = p2 , which
are impossible, as y is orthogonal to p2 . So E1 = {x1 }, and J 1 is one-dimensional. Since J 1 is
arbitrary, all summands are one-dimensional. 
L

Thus, a probabilistic theory satisfying the hypotheses of Corollary B.9 will comprise only
simple Jordan models and classical systems. In particular, such a theory cannot accommodate
superselection rules. This is also true, however, of earlier reconstructions based on versions of the
subspace axiom that assume all systems of the same information capacity to be isomorphic. (If
the theory is monoidal, roughly meaning that it allows for the formation of composite systems —
and meaning more precisely that the category in question has a symmetric monoidal structure,
satisfying some reasonable constraints on how this interacts with the theory’s probabilisic apparatus; see [9] for details — then there are further constraints. These matters are discussed in [5].
For a discussion of how monoidal “process theories” in the sense of [1, 13] can be represented as
probabilistic theories in the sense of this paper, see [32].)
We now show that the assumptions discussed in this Appendix imply no further constraints
on Jordan models. To this end, it will be enough to exhibit a probabilistic theory C containing all
simple Jordan models, and assigning to each such model A a monoid Proc(A) of allowed processes
in such a way that A is symmetric and C enjoys the SSP.
Proposition B.11: Let C be the probabilistic theory consisting of all full, simple euclidean Jordan
models, with processes on a given model A(J ) consisting of composites of maps of the form Ua ,
a ∈ J 16 . Then every model in C is symmetric, and satisfies the SSP.
16
The structure group, Γ(J ), of a euclidean Jordan algebra J consists of all non-singular positive mappings
φ : J → J such that Uφ (a) = φUa φ∗ for every a ∈ J . A theorem of Koecher [23] shows that the connected
component of the identity in Γ(J ) consists exactly of composites of mappings of the form Ua . In other words, in
this theory, G(A) is precisely the connected identity component of Γ(J ).

Accepted in Quantum 2019-06-24, click title to verify

32

<!-- page 33 -->
Proof: Let A = A(J ) = (M(J ), Ω(J )) be the Jordan model associated with an EJA J . Thus,
M(J ) is the set of Jordan frames, and X(J ) the set of primitive idempotents, of J . If J is simple,
symmetry (indeed, full symmetry) of A under G(A) follows from ([18], IV.2.5)17 It follows easily
that G(A) acts transitively on Jordan frames even if J is not simple (since each such frame is the
disjoint union of frames chosen from each simple summand). Let p ∈ P (J ). Then ([2], Prop. 1.38,
Lemma 1.39, Prop. 1.43, Prop. 2.32 and remarks preceding latter), J p := Up (J ) is a hereditary
Jordan subalgebra, meaning that if 0 ≤ a ≤ b ∈ J p , then a ∈ J p as well. The unit of J p is p. It
is important to note here that (J p )+ = J + ∩ J p (that is, an element of J p is positive in J p iff it
is positive in J ). This follows from spectral theory; see [2] Prop. 1.22 and subsequent discussion.
It follows that if a, b ∈ J p , a ≤ b in J p iff a ≤ b as elements of J . One can also show ([2], Lemma
1.45) that if a ∈ J p and b ∈ J p0 , then a b = 0.
Now let e be a primitive idempotent in J that happens to lie in J p : then e is an idempotent
in J p as well. If f is another nonzero idempotent in J p with f ≤ e, then f is still idempotent
in J and, by remarks above, f ≤ e in J , whence, as e is minimal, e = f . Thus, e is primitive in
J p . Conversely, let e be primitive idempotent in J p . Then e is still idempotent in J . If f is an
idempotent of J with 0 < f ≤ e in J , then f ∈ J p , since the latter is hereditary. As e is primitive
in J p , f = e. Thus, e is primitive in J .
This shows that X(J p ) = J p ∩ X(J ). It follows that M(J p ) is the set of all sets of primitive
idempotents of J summing to p. Now let p = u − x where x is a primitive idempotent of J . Then
F ∈ M(J p ) iff F ∪ {x} ∈ M(J ). In other words, M(J p ) = M(A)x in the notation of Definition
B.1.
It remains to show that any (p-reversible) process in Proc(Ax ) extends to a (reversible) process
in Proc(A) leaving x fixed. It suffices to show this holds for processes of the form Ua , with a ∈ J p .
Since x b = b x = 0 for all b ∈ J p , a straightforward calculation then shows that Ua+x b = Ua b
for all b ∈ J p , and that Ua+x x = x. Hence, Ua+x is the desired extension of Ua . Note that if Ua is
invertible, then a is invertible in Jp . By Lemma A.4 (b), there exists some b ∈ J p with a b = p
and a2 b = a. Since x b = 0 for all b ∈ J p , we have

·

· ·
·

·

·

·

·

·

(a + x) (b + x) = a b + x2 = a b + x = p + x = u,
and

·

·

·

(a + x)2 (b + x) = (a2 + x) (b + x) = a2 b + x2 = a + x.
Invoking Lemma A.4 (b) again, this implies that b + x is the inverse of a + x in J , whence, by
Lemma A.4 (c), Ua+x is invertible. 

17

Or, more exactly, from the proof thereof. For any two Jordan-orthogonal primitive idempotents x, y there exists
a symmetry — an element s ∈ A with s2 = u — such that Us (x) = y ([18], IV.2.4). This, plus an induction, allows
one to construct an automorphism of the form Ua taking one Jordan frame to another.
Accepted in Quantum 2019-06-24, click title to verify

33
