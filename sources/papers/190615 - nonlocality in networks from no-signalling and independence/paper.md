---
type: paper
date: 2019-06-15
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1906.06495v2)
reviewed: false
---

# Constraints on nonlocality in networks from no-signaling and independence

Machine-generated and unreviewed text extraction of arXiv:1906.06495v2
(13 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1906.06495v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Constraints on nonlocality in networks from no-signalling and independence
Nicolas Gisin,1 Jean-Daniel Bancal,1 Yu Cai,1 Patrick Remy,1 Armin Tavakoli,1
Emmanuel Zambrini Cruzeiro,1, 2 Sandu Popescu,3, 4 and Nicolas Brunner1

arXiv:1906.06495v2 [quant-ph] 9 Jun 2020

2

1
Département de Physique Appliquée, Université de Genève, CH-1211 Genève, Switzerland
Laboratoire d’Information Quantique (LIQ), Universit Libre de Bruxelles, 1050 Bruxelles, Belgium
3
H.H. Wills Physics Laboratory, Tyndall Avenue, BS8 1TL, Bristol, UK
4
Institute for Theoretical Studies, ETH Zurich, Switzerland
(Dated: 11 June 2020)

The possibility of Bell inequality violations in quantum theory had a profound impact on our
understanding of the correlations that can be shared by distant parties. Generalising the concept
of Bell nonlocality to networks leads to novel forms of correlations, the characterization of which is
however challenging. Here we investigate constraints on correlations in networks under the natural
assumptions of no-signalling and independence of the sources. We consider the “triangle network”
with binary outputs, and derive strong constraints on correlations even though the parties receive
no input, i.e. each party performs a fixed measurement. We show that some of these constraints are
tight, by constructing explicit local models (i.e. where sources distribute classical variables) that can
saturate them. However, we also observe that other constraints can apparently not be saturated by
local models, which opens the possibility of having nonlocal (but non-signalling) correlations in the
triangle network with binary outputs.

INTRODUCTION

The no-signalling principle states that instantaneous
communication at a distance is impossible. This imposes
constraints on the possible correlations between distant
observers. Consider the so-called Bell scenario [1], where
each party performs different local measurements on a
shared physical resource distributed by a single common
source. In this case, the no-signalling principle implies
that the choice of measurement (the input) of one party
cannot influence the measurement statistics observed by
the other parties (their outputs). In other words, the
marginal probability distribution of each party (or subset
of parties) must be independent of the input of any other
party. These are the well-known no-signalling conditions,
which represent the weakest conditions that correlations
must satisfy in any “reasonable” physical theory [2], in
the sense of being compatible with relativity. More generally, the no-signalling principle ensures that information
cannot be transmitted without any physical carrier. This
provides a useful framework to investigate quantum correlations (which obviously satisfy the no-signalling conditions, but do not saturate them in general [2]) within
a larger set of physical theories satisfying no-signalling;
see e.g. [2–9].
Recently, the concept of Bell nonlocality has been
generalized to networks, where separated sources distribute physical resources to subsets of distant parties
(see Fig. 1). Assuming the sources to be independent
from each other [10, 11], arguably a natural assumption
in this context, leads to many novel effects. Notably, it
becomes now possible to demonstrate quantum nonlocality without the use of measurement inputs [11–15], but
only by considering the output statistics of fixed measurements. Just recently, a first example of such nonlocality
genuine to networks was proposed [15, 16]. This radically
departs from the standard setting of Bell nonlocality, and

opens many novel questions. Characterizing correlations
in networks (local or quantum) is however still very challenging at the moment, despite recent progress [17–28].
Moving beyond quantum correlations, this naturally
raises the question of finding the limits of possible correlations in networks, assuming only no-signalling and
independence of the sources [22, 29–33]. Here we investigate this question and derive limits on correlations, which
we refer to as NSI constraints (no-signalling and independence). While our approach can in principle be applied
to any network, we focus here on the well-known triangle
network with binary outputs and no inputs, for which
we obtain strong, and even tight NSI constraints. Specifically, we show that, despite the absence of an input,
some statistics imply the possibility for one party to signal to others by locally changing (or not changing) the
structure of the network. Formally, this amounts to considering a specific class of so-called network inflations, as
introduced in Ref. [22], which we show can lead to general and strong NSI constraints. Moreover, we prove that
some of our NSI constraints are in fact tight, by showing
that they can be saturated by correlations from explicit
“trilocal” models, in which the sources distribute classical variables. Interestingly, however, it appears that not
all of our NSI constraints can be saturated by trilocal
models, which opens the possibility of having nonlocal
(but nevertheless non-signalling) correlations in the triangle network with binary outputs. Finally, we conclude
with a list of open questions.

NSI CONSTRAINTS

The triangle network (sketched in Fig. 1(a)) features
three observers: Alice, Bob and Charlie. Every pair of
observers is connected by a (bipartite) source, providing a shared physical system. Importantly, the three

<!-- page 2 -->
2

A
γ∗
B

Inflation

∗β
α
∗

C

(a)

β∗

α
C 0 ∗ B0

A0

A

γ∗

∗γ

∗β
α
∗
B
C
(b)

FIG. 1. Inflation of the triangle network to the hexagon network – In order to capture NSI constraints in the triangle
network (a), we consider an inflation to the hexagon network
(b). Importantly, from the point of view of Bob and Charlie,
the two situations must be indistinguishable. If not, then Alice could (instantaneously) signal to Bob and Charlie, simply
by locally modifying the network structure.

sources are assumed to be independent from each other.
Hence, the three observers share no common (i.e. tripartite) piece of information. Based on the received physical
resources, each observer provides an output (a, b and c,
respectively). Note that the observers receive no input in
this setting, contrary to standard Bell nonlocality tests.
The statistics of the experiment are thus given by the
joint probability distribution p(a, b, c). We focus on the
case of binary outputs: a, b, c ∈ {+1, −1}. It is then
convenient to express the joint distribution as follows:

p(a, b, c) = 81

(1)

where EA , EB and EC are the single-party marginals,
EAB , EBC and EAC the two-party marginals, and EABC
is the three-body correlator. Note that the positivity of
p(a, b, c) implies constraints on marginals, in particular
p(+ + +) + p(− − −) ≥ 0 implies
EAB + EAC + EBC ≥ −1 .

X

b p(a, b, c, a0 , b0 , c0 ) =

X

b0 p(a, b, c, a0 , b0 , c0 ) = EB
(3)

X

c p(a, b, c, a0 , b0 , c0 ) =

X

c0 p(a, b, c, a0 , b0 , c0 ) = EC
(4)

bc p(a, b, c, a0 , b0 , c0 ) =

X

b0 c0 p(a, b, c, a0 , b0 , c0 ) = EBC
(5)

X



1 + aEA + bEB + cEC + abEAB

+ acEAC + bcEBC + abcEABC ,

extra parties and sources) occurs on Alice’s side, and can
therefore be space-like separated from Bob and Charlie. If Alice, by deciding which network to use, could
remotely influence the statistics of Bob and Charlie, this
would clearly lead to signalling. Hence we conclude that
the local statistics of Bob and Charlie (i.e. the singleparty marginals EB and EC , as well as the two-party
marginals EBC ) must be the same in the triangle and in
the hexagon. To see that this condition really captures
the possibility to signal, we could imagine a thought experiment in which we would give an input to Alice, which
determines whether she modifies her network structure or
not. If she does so and this has an incidence on the EBC
marginal, then Bob and Charlie can learn about Alice’s
input, hence breaking the usual notion no-signalling condition. Note that the input considered here is however
purely fictional, Alice’s input is not present in the actual
experiment.
From the above reasoning, we conclude that the
joint output probability distribution for the hexagon,
i.e. p(a, b, c, a0 , b0 , c0 ), must satisfy several constraints. In
particular, one should have that

(2)

In the following, we will derive non-trivial constraints
bounding and relating the single-party and two-party
marginals of p(a, b, c) under the assumption of NSI.
While it seems a priori astonishing that the no-signalling
principle can impose constraints in a Bell scenario featuring no inputs for the parties, we will see that this is
nevertheless the case in the triangle network.
The main idea is the following. Although one party
(say Alice) receives no input, she could still potentially
signal to Bob and Charlie by locally modifying the structure of the network. To see this, consider the hexagon
network depicted in Fig. 1(b), and focus on parties Bob
and Charlie. From their point of view, the two networks
(triangle and hexagon) should be indistinguishable. This
is because all the modification required to bring the triangle network to the hexagon (e.g. by having Alice adding

where all sums go over all outputs a, b, c, a0 , b0 , c0 . From
the independence of the sources, we obtain additional
constraints, namely
X
2
bb0 p(a, b, c, a0 , b0 , c0 ) = EB
(6)
X
0
0 0 0
2
cc p(a, b, c, a , b , c ) = EC
(7)
X
0
0 0 0
bb c p(a, b, c, a , b , c ) = EBC EB
(8)
X
bcc0 p(a, b, c, a0 , b0 , c0 ) = EBC EC
(9)
X
2
bcb0 c0 p(a, b, c, a0 , b0 , c0 ) = EBC
.
(10)
Clearly, we also get similar constraints when considering
signalling between any other party (Bob or Charlie) to
the remaining two.
Altogether, we see that NSI imposes many constraints
on p(a, b, c, a0 , b0 , c0 ). Obviously, we also require that
X
p(a, b, c, a0 , b0 , c0 ) ≥ 0 and
p(a, b, c, a0 , b0 , c0 ) = 1 .
(11)
Now reversing the argument, we see that the nonnegativity of p(a, b, c, a0 , b0 , c0 ) imposes non-trivial constraints relating the single- and two-party marginals of
the triangle distribution p(a, b, c). To illustrate this,
let us proceed with an example in a slightly simplified

<!-- page 3 -->
3
scenario, assuming all single-party marginals to be uni-

formly random, i.e. EA = EB = EC = 0. In this case, we
obtain

64 p(a, b, c, a0 , b0 , c0 ) = 1 + (ab + a0 b0 )EAB + (bc + b0 c0 )EBC + (ca0 + c0 a)EAC + (abc + a0 b0 c0 )F3 + (bca0 + b0 c0 a)F30
2
2
2
+ bb0 cc0 EBC
+ aa0 cc0 EAC
+ aa0 (bc + b0 c0 )F4 + bb0 (ca0 + c0 a)F40 + cc0 (ab + a0 b0 )F400
+ (ca0 b0 + c0 ab)F300 + aa0 bb0 EAB
+ aa0 bb0 (c + c0 )F5 + bb0 cc0 (a + a0 )F50 + aa0 cc0 (b + b0 )F500 + aa0 bb0 cc0 F6 ≥ 0
(12)

Importantly, notice that the above expression contains
a number of variables (of the form FX ) that are uncharacterized; these represent X-party correlators in the
hexagon network, see Supplementary Note 1 for more
details. Hence we obtain a set of inequalities imposing
constraints on our variables of interest (i.e. EAB , EBC
and EAC ), but containing also additional variables which
we would like to discard. This can be done systematically via the algorithm of Fourier-Motzkin elimination
[34]. Note that here we need to treat the squared terms,
2
such as EAB
, as new variables, independent from EAB ,
so that we get a system of linear inequalities. Solving
the latter, and taking into account positivity constraints
as in Eq. (2), we obtain a complete characterization of
the set of two-body marginals (i.e. EAB , EBC and EAC )
that are compatible with NSI in the triangle network (for
a hexagon inflation and uniform single-party marginals),
in terms of a single inequality
2
2
(1 − EAB )2 − EBC
− EAC
≥ 0,

(13)

and its symmetries (under relabeling of the parties and
of the outputs). This implies a more symmetric, but
slightly weaker inequality:
(1 + EAB )2 + (1 + EBC )2 + (1 + EAC )2 ≤ 6 .

(14)

Note √
that when EAB = EBC = EAC ≡ E2 , we get simply
E2 ≤ 2 − 1 ≈ 0.41.
Next we consider the symmetric case (i.e. EA = EB =
EC ≡ E1 and EAB = EBC = EAC ≡ E2 ) and obtain nontrivial NSI constraints on the possible values of E1 and
E2 (see Fig. 2). In particular, correlations compatible
with NSI must satisfy the following inequality
(1 + 2|E1 | + E2 )2 ≤ 2(1 + |E1 |)3 .

FIG. 2. Region of allowed correlations for symmetric distributions; projection in the plane E2 vs E1 . The turquoise region
is ruled out by NSI constraints, while the grey region is excluded from simple positivity constraints. The white region
is accessible via trilocal models. Correlations in the yellow
region satisfy NSI constraints (from the hexagon inflation),
but we could not find a trilocal model for them. The constraint Eq. (34) of [22] is shown in dotted black. The dashed
turquoise curve corresponds to the NSI inequality (15), which
turns out to be tight. Explicit trilocal models are also obtained for the correlations marked by blue dots (see Supplementary Note 2).

(15)

Let us move now to the most general case, with arbitrary values for single- and two-party marginals. For a
given set of values EA , EB , EC , EAB , EBC and EAC , it is
possible here to determine via a linear program whether
this set is compatible with NSI or not (see Supplementary Note 1). More generally, obtaining a characterization of the NSI constraints in terms of explicit inequalities
(as above) is challenging, due mainly to the number of
parameters and nonlinear constraints. We nevertheless
obtain that the following inequality represents an NSI

constraint
(1 + |EA | + |EB | + EAB )2

+ (1 + |EA | + |EC | + EAC )2

+ (1 + |EB | + |EC | + EBC )2
≤ 6(1 + |EA |)(1 + |EB |)(1 + |EC |) .

(16)

A proof of this general inequality is given in Supplementary Note 4. Note that this inequality reduces to (14)
when EA = EB = EC = 0, as well as to (15) for the
symmetric case.
It is worthwhile discussing the connection between
our approach and the “inflation technique” presented in
Refs. [22, 25]. There, the main focus is on using inflated
networks for deriving constraints on correlations achievable with classical resources. In that case, information
can be readily copied, so that sources can send the same
information to several parties. Ultimately, this allows
for a full characterization of correlations achievable with
classical resources [22]. Copying information is however

<!-- page 4 -->
4
not possible in our case, as no-signalling resources cannot be perfectly cloned in general [6]. Hence only inflated
networks with bipartite sources can be considered in our
case, such as the hexagon. A discussion of these ideas can
be found in Section V.D of [22], where the idea of using
inflation to limit no-signalling correlations in networks
is mentioned. Here, we derive explicitly bounds that
all correlations satisfying the NSI constraints, whether
quantum of post-quantum, have to satisfy, and identify
the physical principle behind them.
Finally, the choice of the hexagon inflation deserves
a few words. As seen from Fig. 1(b), it is judicious to
consider inflated networks forming a ring, with a number of parties that is a multiple of three. Intuitively this
should enforce the strongest constraints on the correlations of the inflated network; in particular, all single and
two-body marginals are fixed by the correlations of the
triangle. This would not be the case when considering
inflations to ring networks with a number of parties that
is not divisible by three.
TIGHTNESS

A natural question is whether the constraints we derived above, that are necessary to satisfy NSI, are also
sufficient. There is a priori no reason why this should be
the case. Of course, starting from the triangle network,
there are many (in fact infinitely many) possible extended
networks that can be considered, and no-signalling must
be enforced in all cases. For instance, instead of extending the network to a hexagon (as in Fig. 1), Alice
could consider an extension to a ring network featuring
9, 12 or more parties. Clearly, such extensions could lead
to stronger constraints than those derived here for the
hexagon network.
Nevertheless, we show that some of the constraints we
obtain above are in fact tight, i.e. necessary and sufficient
for NSI. We prove this by presenting explicit correlations
(constructed within a generalized probabilitic theory satisfying NSI) that saturate these constraints. In fact, we
consider simply the case where all sources distribute classical variables to each party, which we refer to as “trilocal” models. The latter give rise to correlations of the
form
Z
Z
Z
p(a, b, c) = µ(α)dα ν(β)dβ ω(γ)dγ
(17)
pA (a|β, γ) pB (b|α, γ) pC (c|α, β)
where α, β and γ represent the three local variables distributed by each source, with arbitrary probability densities µ(α), ν(β) and ω(γ). Also, pA (a|β, γ) represents an
arbitrary response function for Alice, and similarly for
pB (b|α, γ) and pC (c|α, β). Note that such trilocal models represents a natural extension of the concept of Bell
locality to networks (see e.g. [10, 19]).
We first consider the case of symmetric distributions,
i.e. characterized by the two parameters E1 and E2 , and

seek to determine the set of correlations that can be
achieved with trilocal models. As shown in Fig. 2, it
turns out that almost all NSI constraints can be saturated in this case, in particular the inequality (15). After performing a numerical search, we could construct explicitly some of these trilocal models, which involve up to
ternary local variables (see Supplementary Note 2 for details). Moreover, we compare our NSI constraint (15) to
the one derived in Ref. [22] (see Eq. (34)), and find that
the present one is stronger, and in fact tight (see Fig. 2).
Note also that a previous work derived an NSI constraint
based on entropic quantities [29]; such constraints are
however known to be generally weak, as entropies are a
coarse-graining of the statistics, which no longer distinguishes between correlations and anti-correlations.
As seen from Fig. 2, there is however a small region
(in yellow) which is compatible with NSI (considering
the hexagon inflation), but for which we could not construct a trilocal model. Whether this gap can be closed
by considering more sophisticated local models (using
variables of larger alphabet) or whether stronger nosignalling bounds can be obtained is an interesting open
question. For the triangle network with binary outcomes,
any trilocal distribution can be obtained by considering
shared variables of dimension (at most) six, and deterministic response functions [24].
In fact, another (and arguably much more interesting)
possibility would be that this gap cannot be closed, as
it would feature correlations with binary outcomes satisfying NSI but that are nevertheless non-trilocal. To
further explore this question, let us now focus on the
case where single-party marginals vanish, i.e. E1 = 0.
We investigate the relation between two-party marginals
E2 and the three-party correlator E3 = EABC , comparing NSI constraints and trilocal models. Notice that the
NSI constraints we obtain here do not involve E3 (as
the latter cannot be recovered within the analysis
of the
√
hexagon). Hence NSI imposes only E2 ≤ 2 − 1, while
positivity of p(a, b, c) imposes other constraints. This is
shown in Fig. 3, where we also seek to characterize the set
of correlations achievable via trilocal models (proceeding
as above). Interestingly, we find again a potential gap
between trilocal correlations and NSI constraints. This
should however be considered with care. First, the NSI
constraints obtained from the hexagon may not be optimal (see discussion). Second, there could exist more sophisticated trilocal models (e.g. involving higher dimensional variables) that could lead to a stronger correlations
(i.e. cover a larger region in Fig. 3). Note also that we investigated whether quantum distributions satisfying the
independence assumption exist outside of the trilocal region, but we could not find any example (we performed a
numerical search, considering entangled states of dimension up to 4 × 4).
Finally, note that we also performed a similar analysis
for the case where single-party marginals vanish but twobody marginals are not assumed to be identical to each
other. Here we find that inequality (13) can be saturated

<!-- page 5 -->
5
point. We cannot exclude the possibilities that (i) these
correlations are in fact not compatible with NSI (as there
exist stronger NSI constraints) or (ii) these correlations
can in fact be reproduced by a trilocal model. In order to
address point (i), one could try to reproduce these correlations via an explicit NSI model, for instance considering
that all sources emit no-signalling resources (such as nonlocal boxes [2]) which could then be “wired together” by
the parties. To address point (ii), one could show that
these correlations violate a multilocality inequality for
the triangle network. Of course finding such inequalities
is notably challenging, see e.g. [13].

FIG. 3. Region of allowed correlations for symmetric distributions with E1 = 0; represented in the plane E2 vs E3 .
The turquoise region is ruled out by NSI constraints (dashed
turquoise line given by Eq. (15)), while the grey region is excluded from simple positivity constraints. The white region is
accessible via trilocal models. Correlations in the yellow region satisfy NSI constraints (from the hexagon inflation), but
we could not find a trilocal model for them. Explicit trilocal
models are also obtained for the correlations marked by blue
dots (see Supplementary Note 2).

in a few specific cases. However, there also exist correlations satisfying the NSI bounds that do not seem to
admit a trilocal model; details in Supplementary Note 1.

Furthermore, it would be interesting to derive NSI constraints for other types of networks. Indeed, the approach
developed here can be straightforwardly used. Cases of
high interest are general loop networks, as well as the triangle network with larger output alphabet (where examples of quantum nonlocality are proven to exist [11, 15]).
Finally, a more fundamental question is whether any
correlation satisfying the complete NSI constraints can be
realized within an explicit physical theory satisfying nosignalling (the latter are usually referred to as generalized
probabilistic theories [6]). While this is the case in the
standard Bell scenario (where all parties share a common
resource), it is not clear if that would also be the case in
the network scenario.

DISCUSSION

We discussed the constraints arising on correlations in
networks, under the assumption of no-signalling and independence of the sources. We focused our attention on
the triangle network with binary outputs for which we derived strong constraints, including tight ones. Our work
raises a number of open questions that we now discuss
further.
A first question is whether the constraints we derive
(necessary under NSI), could also be sufficient. We believe this not to be the case, as stronger NSI constraints
could arise from inflations of the triangle to more complex
networks (e.g. loop networks with an arbitrary number of
parties). Note that there could also exist different forms
of no-signalling constraints, that cannot be enforced via
inflation. In this respect, we compare in Supplementary Note 3 our NSI constraints with the recent work
of Ref. [32] proposing a very different approach to this
problem, using the the Finner inequality. A notable difference is that the latter imposes constraints on tripartite
correlations, which is not the case here.
Another important question is whether there could exist nonlocality in the simplest triangle network with binary outcomes. That is, can we find a p(a, b, c) that
satisfies NSI but that is nevertheless non-trilocal? While
we identified certain potential candidate distributions for
this, we could not prove any conclusive result at this

ACKNOWLEDGEMENTS

We thank Stefano Pironio, Marc-Olivier Renou, Denis
Rosset and Elie Wolfe for discussions. We acknowledge
financial support from the Swiss national science foundation (Starting grant DIAQ, NCCR-QSIT and NCCRSwissmap). E. Zambrini acknowledges support by the
Swiss National Science Foundation via the Mobility Fellowship P2GEP2 188276.

APPENDIX 1: NSI BOUNDS

In the hexagon configuration introduced in the main
text, the probability distribution can be expressed in

<!-- page 6 -->
6
terms of 16 parameters as

tripartite term EABC , as

8 p(a, b, c) =1 + aEA + bEB + cEC + abEAB
(19)
64 p(a, b, c, a0 , b0 , c0 ) =
+ bcEBC + acEAC + abcEABC
1 + (a + a0 )EA + (b + b0 )EB + (c + c0 )EC
+ (ab0 + a0 b)EA EB + (bc0 + b0 c)EB EC + (ac + a0 c0 )EA EC In this appendix, we describe the constraints that
2
2
2
the positivity conditions p(a, b, c, a0 , b0 , c0 ) ≥ 0 and
+ aa0 EA
+ bb0 EB
+ cc0 EC
+ (ab0 c + a0 bc0 )EA EB EC
p(a,
b, c) ≥ 0 imply on the first six parameters.
0 0
0 0
0
0
+ (ab + a b )EAB + (bc + b c )EBC + (ca + c a)EAC
A
first general observation is that Supplementary
+ aa0 (b + b0 )EA EAB + aa0 (c + c0 )EA EAC
Equation
(19) is linear in its variables, but Supplemen+ bb0 (a + a0 )EB EAB + bb0 (c + c0 )EB EBC
tary Equation (18) is nonlinear. However, since this last
expression involves no product of free variables, all non+ cc0 (a + a0 )EC EAC + cc0 (b + b0 )EC EBC
linearities vanish when the parameters in E are fixed. It
0 0 2
0 0 2
0 0 2
+ aa bb EAB + bb cc EBC + aa cc EAC
is therefore always possible to test whether a behaviour
+ aa0 (cb0 + bc0 )EA F300 + bb0 (ac + a0 c0 )EB F3
given by some variables E is compatible with a hexagon
+ cc0 (ba0 + b0 a)EC F30
configuration by linear programming. Concretely, this is
achieved by solving the following linear program:
+ (abc + a0 b0 c0 )F3 + (bca0 + b0 c0 a)F30 + (ca0 b0 + c0 ab)F300
+ aa0 (bc + b0 c0 )F4 + bb0 (ca0 + c0 a)F40 + cc0 (ab + a0 b0 )F400
max 1
(20)
F
+ aa0 bb0 (c + c0 )F5 + bb0 cc0 (a + a0 )F50 + aa0 cc0 (b + b0 )F500
s.t. f6 (a, b, c, a0 , b0 , c0 , E, F) ≥ 0 ∀a, b, c, a0 , b0 , c0 = ±1
+ aa0 bb0 cc0 F6 .
f3 (a, b, c, E) ≥ 0
∀a, b, c = ±1,
(18)
Six of these parameters, which are part of the behaviour vector E = (EA , EB , EC , EAB , EBC , EAC , EABC ),
appear in the triangle as well. We refer to them
as the physical parameters. The remaining 10, from
F = (F3 , F30 , F300 , F4 , F40 , F400 , F5 , F50 , F500 , F6 ), are new to
the hexagon. We refer to them as free variables.
In this decomposition the E terms correspond to correlators that appear in the triangle scenario, c.f. Fig. 1(a)
of the main text, whereas the free variables FX refer to
X-partite correlators in the hexagon, c.f. Fig. 1(b) of
the main text. For instance, in the case of tripartite correlators (i.e. with X = 3), the hexagon network contains
three distinct tripartite correlators, which we simply refer to as F3 , F30 and F300 . The first one, F3 is defined as
the correlator
P for parties A, B, and C in the hexagon,
i.e. F3 = a,b,c,a0 ,b0 ,c0 abcp(a, b, c, a0 , b0 , c0 ). Since these
parties are identical to A0 , B0 , C0 , we also have F3 =
P
0 0 0
0 0 0
a,b,c,a0 ,b0 ,c0 a b c p(a, b, c, a , b , c ). We notice however
that this term P
is not identical to the tripartite correlation
term EABC = a,b,c abcp(a, b, c) that can be measured in
the triangle configuration (c.f. Fig 1(a) of the main text).
Indeed, in the triangle configuration, parties A, B and C
are connected by three sources α, β, γ, but in the hexagon
configuration, these three parties are only connected by
the two sources
P α and γ. We thus have F3 6= EABC . Similarly, F30 = a,b,c,a0 ,b0 ,c0 a0 bcp(a, b, c, a0 , b0 , c0 ) is in general
different than F3 , because this time the three parties A0 ,
B, C are connected by two different sources: α and β.
For thePsame reason we have a third tripartite correlator
F300 = a,b,c,a0 ,b0 ,c0 a0 b0 cp(a, b, c, a0 , b0 , c0 ) in the hexagon
network, and similarly for the remaining free variables.
The probabilities in the triangle configuration can be
written in terms of the same variables, with an additional

where f6 (a, b, c, a0 , b0 , c0 , E, F) is the expression given by
Supplementary Equation (18) and f3 (a, b, c, E) the one
given by Supplementary Equation (19). Note that this
linear program involves a constant objective function because we are not trying to maximize any particular quantity, but we are rather interested in knowing whether the
set of constraints admit a joint solution. If this linear program is feasible, then the behaviour given by the vector
E is compatible with the considered constraints. Otherwise, it is not. Note that this formulation in terms of
linear programming would not be possible in inflations
of the triangle involving eight or more parties since in
this case products of the unknown variables, such as F32 ,
appear.
In general, we are interested in more than only testing
whether a behaviour is compatible with the no-signalling
constraints. In particular, we would like to find NSI inequalities. For this, we start by considering simplified
situations.

Uniformly random single-party marginals

Let us consider the situation in which the outputs produced by all parties are uniformly random, i.e. EA =
EB = EC = 0. In this case, the expression for the probabilities (18) simplifies significantly. The number of free
variables is unchanged, but all products of free variables
with a physical parameter vanish. This allows us to understand the positivity constraints p(abca0 b0 c0 ) ≥ 0 as a
set of linear constraints relating powers of physical parameters with some unknown variables. Inequalities involving only physical parameters can thus be obtained
from this set of constraints by judiciously adding several

<!-- page 7 -->
7
probabilities to each other. For instance, we can write
16(p(1, 1, 1, −1, −1, 1) + p(−1, −1, −1, 1, 1, −1)
+ p(1, 1, −1, 1, 1, 1) + p(−1, −1, 1, −1, −1, −1))
2
2
2
= (1 + 2EAB + EAB
− EBC
− EAC
+ 2F400 + F6

2
2
2
+ 1 + 2EAB + EAB
− EBC
− EAC
− 2F400 − F6 )/2

2
2
2
= 1 + 2EAB + EAB
− EBC
− EAC
≥ 0,

(21)

and obtain an inequality involving no free variable in F.
More generally, all constraints on the physical variables
can be obtained by performing a Fourier-Motzkin elimination on the free variables.
Performing this elimination produces 24 inequalities.
After taking into account the redundancy implied by the
symmetries of the Bell scenario [? ], we recover the constraint (21), implying that it is tight, together with two
more constraints. Altogether, these form the three following families of constraints:
2

2
2
(1 + EAB ) − EBC
− EAC
≥0
2
2
2
(1 + EAB ) + EBC + EAC ≥ 0
2
1 + EAB + EBC + EAC
≥ 0.

(22)
(23)
(24)

The second inequality is a sum of squares, and therefore always true. Interestingly, the third inequality is a
consequence of the first one:
2
1+EAB + EBC + EAC
2
≥ 1 + EAB + EBC − EAC

2
2
2
= (1 + 2EAB + EAB
− EBC
− EAC

(25)

2
2
2
+ 1 + 2EBC − EAB
+ EBC
− EAC
)/2

≥ 0.

Therefore, the constraints due to the hexagon inflation
boil down to a unique inequality : Supplementary Equation (22).
In Supplementary Figure 4, we plot the constraint imposed by this inequality in the EAB -EBC plane for fixed
values of EAC . Remarkably, most of the NSI region can
be achieved by trilocal models, leaving only a small gap
region (yellow area).
Combining three versions of Supplementary Inequality (22), we obtain
2
2
2
1 − 2EAB + EAB
− EBC
− EAC

2
2
2
+1 − 2EBC − EAB
+ EBC
− EAC

(26)

2
2
2
+1 − 2EAC − EAB
− EBC
+ EAC
≥0

which simplifies to the symmetric inequality
(1 + EAB )2 + (1 + EBC )2 + (1 + EAC )2 ≤ 6.

(27)

This inequality does not detect the point EAB = 1/2,
EBC = −3/5, EAC = 0, which violates Supplementary
Inequality (22). The latter inequality is thus tighter.

FIG. 4. Turquoise lines show the border of the NSI constraints
imposed by Supplementary Inequality (22) and the positivity
p(abc) ≥ 0 for values of EAC equal to {0, 0.2, 0.4, 0.6, 0.8, 1}
(starting from the outside). When EAC = 1, the allowed region is a single point at the origin. The inset shows the whole
range of EAB ∈ [−1, 1]: straight lines on the left part are positivity constraints, whereas lines on the right part correspond
to Supplementary Inequality (22). The curves for EBC ≤ 0
can be obtained by letting Bob flip his output, hence the
full figure is symmetric under a π rotation around the origin.
For fixed values of EAC , the yellow area shows the “mystery”
region for which we could not find a trilocal model. Note
that local models can reach any part of the NSI boundary for
EAB ≤ 0 and EBC ≥ 0.

Note that in the case where EAB = EBC = E
√AC =
E2 , Supplementary Inequality (22) implies E2 ≤ 2 − 1
whereas Supplementary Inequalities (23)-(24) are always
satisfied.
We note also that the positivity constraints on the
triangle impose the following condition on the bipartite
marginals in presence of random marginals:
EAB + EBC + EAC ≥ −1.

(28)
√

Since the point EAB = EBC = EAC = − 2 + 1 satisfies inequalities in the family of Supplementary Equation
(22), but violates Supplementary Equation (28), it is not
a consequence thereof.
Symmetric statistics

We now consider the special case in which the single
party marginals are not all zero, but the statistics are
invariant under exchange of the parties. The bipartite
statistics can then be parametrized by two numbers E1 =
EA = EB = EC and E2 = EAB = EBC = EAC .
Under this assumption, all free parameters are still
present in the decomposition (18), but the physical space

<!-- page 8 -->
8
is only of dimension 2. This time, however, the probabilities involve products of known with unknown variables,
like E1 F3 . Therefore, we cannot resort only to FourierMotzkin elimination to obtain all constraints that apply
to the physical terms. Doing so by considering E1 F3 as
a free variable to eliminate indeed would not take into
account the actual value of E1 . In particular, if E1 = 0,
this terms would already be eliminated.
We can however resort to the linear programming
formulation described earlier in Supplementary Equation (20) to describe the set of correlations in the twodimensional space of E1 -E2 which are compatible with
the considered constraints. This gives rise to Fig. 2 presented in the main text. In particular, we verify up to
numerical precision that the upper bound on E2 as a
function of E1 of the form
(1 + 2E1 + E2 )2 ≤ 2(1 + E1 )3 .

(29)

As described in Supplementary Note 2, this bound is
achievable.
APPENDIX 2: CONSTRUCTION OF TRILOCAL
MODELS

In this appendix we present the explicit construction
of some of the trilocal models. A trilocal model consists
of (i) three distributions, for each of the shared classical
variables: µ(α), ν(β) and ω(γ), and (ii) three output
functions (one for each party): pA (a|β, γ), pB (b|α, γ) and
pC (c|αβ). The resulting statistics is given by
Z
Z
Z
p(a, b, c) = µ(α)dα ν(β)dβ ω(γ)dγ
(30)
pA (a|β, γ) pB (b|α, γ) pC (c|α, β).
In a two-outcome scenario, it is sufficient to specify the output functions for outcome 1, since pA (a =
−1|β, γ) = 1 − pA (a = 1|β, γ). For ease of notation we
write pA (a = 1|β, γ) ≡ fa (β, γ). Without loss of generality, we may assume the same alphabet size, d, for all the
shared variables. Hence a dit model can be represented
by a 3-by-d matrix (with 3(d−1) variables) for the distributions and three d-by-d matrices, fa (β, γ), fb (α, γ) and
fc (β, α) (each with d2 variables) for the output functions.
For example,



1
2
"
#


1 0
 α 1/2 1/2 
P =
,
 , fa = fb = fc =
 β 1/2 1/2 
0 1
γ 1/2 1/2

(31)

denotes the strategies in which each source emits one bit
at random and the parties output 1 whenever they receive
the same bit from the two sources they are connected to.
Given a specific distribution p(abc), or a specific set
of marginals (e.g. E1 and E2 ), it is possible to numerically search for a trilocal model reproducing this data.

Notably, for binary outcomes, it is sufficient to consider
trilocal models with shared variables that have dimension d ≤ 6 [24]. We implemented this numerical procedure, and found that for the case of low dimensions
(i.e. d = 2, 3) the method is effective and appears to be
reliable. For d > 3, the method can still be run, but is less
reliable (i.e. the fact that the algorithm is not able to find
a trilocal model does not necessarily mean that there exist none). We used this method to determine the trilocal
regions in Supplementary Figs. 2 and 3 of the main text.
Moreover, from the output of the numerics, we could in
certain cases reconstruct analytically the trilocal models.
Below we detail some of these models. Notably, these
models can saturate some of the NSI constraints that we
have derived, implying that the latter are tight. Finally,
we also show that any point within these trilocal regions
can be achieved via a trilocal model. In other words,
although we characterize only the boundary of these regions, we show that any point within the boundary is also
achievable (i.e. these regions do not feature any hole).
We first discuss a simple class of trilocal models, featuring only binary shared variables:


1 2
"
#


1 0
 α r 1−r 
P =
.
(32)
 , fa = fb = fc =
 β q 1−q 
0 0
γ p 1−p
This results in the following statistics. The single-party
marginals are given by
EA = 2pq − 1

EB = 2pr − 1

EC = 2qr − 1 .

(33)

Next, the two-body marginals are
EAB = 1 − 2pq − 2pr + 4pqr
EBC = 1 − 2rp − 2rq + 4pqr
EAC = 1 − 2qp − 2qr + 4pqr

(34)
(35)
(36)

while the three-body correlator is
EABC = −1 + 2pq + 2pr + 2qr − 4pqr .

(37)

This model can saturate Supplementary Inequality (29),
for the case where single-party and two-body marginals
are fully symmetrical. This shows that (29) represents a
tight constraint for NSI. Here, we take simply p = q = r
(i.e. all sources are equivalent). This leads to
E1 = 2p2 − 1
E2 = 1 − 4p2 + 4p3

(38)
(39)

which corresponds to the
√ equality condition in Eq. (29)
(assuming √
here p ≥ 1/ 2, so that E1√≥ 0). Note that
for √
p = 1/ 2, we get E1 = 0, E2 = 2 − 1 and E3 =
2 − 2. This model corresponds to the top-right point of
the white region in Fig. 3 of the main text.
Note also that this class of trilocal models (for arbitrary values of p, q and r) saturate the conjectured NSI
constraint of Eq. (8) of the main text.

<!-- page 9 -->
9
Next, we present a trilocal model that achieves the
E2 = − 31 and E1 = 0:


1
2


 α 1/3 2/3 
P =
,
 β 3/4 1/4 
γ 2/3 1/3
#
"
#
"
#
"
1 1
0 1/2
1 0
.
(40)
, fc =
, fb =
fa =
0 1
1/2 1
0 0
Moreover, from Fig. 2 of the main text, we see that
there exist trilocal models with E2 = − 13 and strictly
positive E1 . We find that the model that maximizes E1
(while keeping E2 = − 31 ) is given by:


1
2
3


1−x
0
α x

P =
,
β
y
(1 − y)/2 (1 − y)/2 
γ 1−x
x
0






1 0 1
1 1 0
0 1 0






fa = 0 0 0 , fb = 0 1 0 , fc = 1 1 0 , (41)
1 1 1
0 0 0
0 0 0
where x is the root between 0 and 1 for 3x4 − 9x3 +
1
9x2 − 5x + 1 = 0, and y = 3(2x2 −2x+1)
. Consequently,
3
2
E1 = (3y + y + y − 1)/4 ≈ 0.1753.
Related to Fig. 3 of the main text, we now give a trilocal model for E1 = E3 = 0 and E2 ≈ 0.3621:
#
"
1 2 3
,
P =
α, β, γ x y z


0 0 1


(42)
fa = fb = fc = 0 0 0 ,
1 0 1
3

3

where x = 23 − z3 − z2 , y = 31 + z3 − z2 , and z ≈ 0.3861 is
the root between 0 and 1 for −4z 7 +4z 4 −3z 3 +8z−3 = 0.
32
2
Consequently, E2 = 49 z 7 − 83 z 5 + 89 z 4 − z 3 + 16
3 z − 9 z+
1 ≈ 0.3621. Note that by changing the distributions
of the shared variables (but keeping the local response
functions the same), one can generate the correlations
indicated by the
√ blue dots in Fig. 3 of the main text (for
0 < E3 ≤ 2 − 2).
Finally, we now show that the trilocal regions shown
in the various figures of the paper do not feature any
hole. That is, we have characterized the boundary of
these trilocal regions (in some cases by giving explicit
trilocal models), and we now prove that any point inside
this boundary can necessarily be achieved by a trilocal
model.
The idea is to consider the following “depolarizing”
protocol. Consider a distribution p0 (abc) achievable via
0
a trilocal model M , given by single-party marginals EA
,
0
etc..., bipartite marginals EAB , etc..., and a tripartite

FIG. 5. Comparison of our NSI constraint (29) and the
Finner inequality (43) of Ref. [32] (solid blue curve represents equality in (43)), for the set of distributions pp,q given
in Eq. (44). Our NSI constraints (dashed turquoise curve
representing equality in (29)) appears to be stronger almost
everywhere, except for two small regions, around each deterministic point P+++ (p = 1) and P−−− (q = 1); see inset. As
in previous figures, the grey region is excluded via positivity
constraints and the turquoise region via NSI constraints. The
white region is achievable via trilocal models, while the yellow region is undetermined. The black point represents the
uniformly random distribution, i.e. p = q = 1/8.

0
. Each party adds noise locally (and incorrelator EABC
dependently of the other parties) via the following procedure. With probability 1 − η a party provides a random
output, while with probability η they output according
to M . Hence we obtain the continuous family of distri0
0
butions characterized by EA = ηEA
etc, EAB = η 2 EAB
0
etc and EABC = η 3 EABC
. Varying η from 1 to 0 we
obtain a continuous curve from p0 (abc) to the uniform
distribution.
For Figs. 2 and 3 of the main text and Supplementary
Figure 4, we see that any point inside the trilocal region can be obtained by adding (a well chosen) amount
of noise to a distribution sitting on the boundary. For
Supplementary Figure 5, the situation is different, as the
above depolarizing procedure takes an initial distribution
on the slice outside of it.

APPENDIX 3: COMPARISON TO FINNER
INEQUALITY

We compare the NSI constraint derived here with a
criterion derived in Ref. [32]. The later is based on the

<!-- page 10 -->
10
can be written

Finner inequality, and states that
p(abc) ≤

p
pA (a)pB (b)pC (c)

(43)

where pA (a) represents Alice’s marginal probability to
observe outcome a, and similarly for pB (b) and pC (c).
Importantly, it should be pointed out that the above inequality is only conjectured to hold under NSI. At the
moment, it is only proven that inequality (43) holds in
quantum theory, and in “boxworld” (a generalized probabilistic theory where sources can prepare arbitrary nosignalling boxes, see e.g. [6]). This does not imply that
(43) holds in any generalized probabilistic theory.
Nevertheless it is interesting to compare both approaches, in particular as inequality (43) involves explicitly tripartite correlations (e.g. the term p(abc)), contrary
to our approach which seems to be limited to single- and
two-party marginals.
To perform this comparison, we use a specific set of
distributions in the triangle network, discussed in [32].
These take the form
pp,q = pP+++ + qP−−− + (1 − p − q)Pdiff

(44)

where Pabc represents the distribution where the outputs are set to values a, b and c deterministically, and
Pdiff = (P++− +P+−+ +P−++ +P+−− +P−+− +P−−+ )/6.
From (43) it follows that pp,q is not realizable in the triangle network when q > 1 + p − 2p2/3 (and a similar
constraint inverting p and q); given by the black curve in
Supplementary Figure 5.
We compare this criterion to our NSI constraint (29).
From Supplementary Figure 5, we see that our NSI constraint is mostly stronger than the Finner inequality (43).
However, this is not the case in general, as there is a small
region (around the deterministic points P+++ and P−−− )
where the Finner inequality is stronger.

APPENDIX 4: PROOF OF A GENERAL NSI
INEQUALITY

Here we prove the validity of the following inequality
for NSI models in the triangle network:

+ (1 + |EB | + |EC | + EBC )2
≤ 6(1 + |EA |)(1 + |EB |)(1 + |EC |) .

+ (1 + EA + EC + EAC )2
+ (1 + EB + EC + EBC )2
≤ 6(1 + EA )(1 + EB )(1 + EC ) .

(46)

If EA , EB , EC ≤ 0, flipping all outcomes brings us
back to the same condition.
2. In all other cases we can always exchange parties
and outcomes (jointly) to reach the case EA , EC ≥
0, EB ≤ 0. In this case, Supplementary Equation (45) reduces to
(1 + EA − EB + EAB )2

+ (1 + EA + EC + EAC )2

+ (1 − EB + EC + EBC )2
≤ 6(1 + EA )(1 − EB )(1 + EC ) .

(47)

It is thus sufficient to show the validity of the two inequalities (46) and (47) in their respective context.
Before focusing on these cases, we make some general
observations. Since probabilities are positive, the following sum of probabilities also is:
p(−1, 1, −1, 1, 1, 1) + p(1, −1, 1, −1, −1, −1)
+ p(−1, −1, 1, −1, 1, 1) + p(1, 1, −1, 1, −1, −1) ≥ 0.
(48)
Using Supplementary Equation (18), this condition can
be rewritten as the following inequality:
2
2
2
1 − 2EAC + 2EB F3 ≥ EAB
− EAC
+ EBC
.
P
Similarly, a0 ,b0 ,c0 p(1, −1, 1, a0 , b0 , c0 ) ≥ 0 implies

(49)

I2 = 1 + EA − EB + EC + EA EC − EAB − EBC − F3 ≥ 0,
(50)
P
and a0 ,b0 ,c0 p(−1, 1, −1, a0 , b0 , c0 ) ≥ 0 implies
I20 = 1 − EA + EB − EC + EA EC − EAB − EBC + F3 ≥ 0,
(51)
Case 1 (EA , EB , EC ≥ 0): Since EB ≥ 0, the product
EB I2 (50) is positive. After rearrangement, we obtain
2(1 + EA )(1 + EB )(1 + EC ) − (1 + EA + EC + EAC )2
2
2
2
≥ −EA
+ 2EB
− EC
+ 2EB (EAB + EBC )

(1 + |EA | + |EB | + EAB )2

+ (1 + |EA | + |EC | + EAC )2

(1 + EA + EB + EAB )2

(45)

This inequality is invariant under exchange of parties.
It is also invariant under the joint relabelling of all parties’ outputs. However, it is not invariant under arbitrary
output relabelling. Therefore, we consider two cases:
1. If EA , EB , EC ≥ 0, Supplementary Equation (45)

2
− 2EAC (EA + EC ) − EAC
+ 1 − 2EAC + 2EB F3 .
(52)

Recognizing the last three terms from (49), we use this
inequality to eliminate the term containing the free variable F3 and get
2(1 + EA )(1 + EB )(1 + EC ) − (1 + EA + EC + EAC )2
2
2
2
≥ −EA
+ 2EB
− EC
+ 2EB (EAB + EBC )

2
2
2
− 2EAC (EA + EC ) + EAB
− 2EAC
+ EBC
.

(53)

<!-- page 11 -->
11
Since EC is positive, this inequality remains valid if we
cyclically permute the parties to let C play the role of B,
yielding
2(1 + EA )(1 + EB )(1 + EC ) − (1 + EA + EB + EAB )2
2
2
2
≥ −EA
− EB
+ 2EC
+ 2EC (EAC + EBC )

2
2
2
− 2EAB (EA + EB ) − 2EAB
+ EAC
+ EBC
.

(54)

Similarly, since EA ≥ 0 we can also write

2(1 + EA )(1 − EB )(1 + EC ) − (1 + EA + EC + EAC )2
2
2
2
≥ −EA
+ 2EB
− EC
− 2EB (EAB + EBC )

2
− 2EAC (EA + EC ) − 4EB (EA + EC ) − EAC
+ 1 − 2EAC + 2EB F3

2

(59)
Recognizing again the last three terms from Supplementary Equation (49), we obtain

(55)

2(1 + EA )(1 − EB )(1 + EC ) − (1 + EA + EC + EAC )2

2(1 + EA )(1 + EB )(1 + EC ) − (1 + EB + EC + EBC )
2
2
2
≥ 2EA
− EB
− EC
+ 2EA (EAB + EAC )

2
2
2
− 2EBC (EB + EC ) + EAB
+ EAC
− 2EBC
.

Considering now the positive expression I20 in Supplementary Equation (51), we multiply it with −EB , which
is positive. After rearrangement, this gives

Summing up the three Supplementary Equations (53),
(54), (55), all terms on the right-hand side cancel out,
leaving us with:

2
2
2
≥ −EA
+ 2EB
− EC
− 2EB (EAB + EBC )
− 2EAC (EA + EC ) − 4EB (EA + EC )
2
2
2
+ EAB
+ EBC
− 2EAC

(60)

6(1 + EA )(1 + EB )(1 + EC ) − (1 + EA + EC + EAC )2

− (1 + EA + EB + EAB )2 − (1 + EB + EC + EBC )2 ≥ 0.
(56)

This inequality is identical to (46), which concludes the
proof under the EA ≥ 0, EB ≥ 0, EC ≥ 0 assumption.
Case 2 (EA , EC ≥ 0, EB ≤ 0): This time, EB is negative, so we cannot use Supplementary Equation (53).
However, we still have EA ≥ 0 and EC ≥ 0 so Supplementary Equations (54) and (55) remain valid. For
clarity, we rearrange them as
2(1 + EA )(1 − EB )(1 + EC ) − (1 + EA − EB + EAB )2
2
2
2
2
2
2
≥ −EA
− EB
+ 2EC
− 2EAB
+ EBC
+ EAC
+ 2EB EAB − 2EA EAB + 2EC (EAC + EBC )
− 4EB (EC + EA EC )

Summing Supplementary
and (60), we obtain

Equations

(57),

(58)

6(1 + EA )(1 − EB )(1 + EC ) − (1 + EA + EC + EAC )2

− (1 + EA − EB + EAB )2 − (1 − EB + EC + EBC )2
≥ −8EB (EA + EC + EA EC ) ≥ 0,
(61)

where the positivity follows from the negativity of EB and
the positivity of EA and EC . This proves (47) under the
EA ≥ 0, EB ≤ 0, EC ≥ 0 assumptions, which concludes
the proof of Supplementary Equation (45).

(57)

and
2(1 + EA )(1 − EB )(1 + EC ) − (1 − EB + EC + EBC )2
2
2
2
2
2
2
≥ 2EA
− EB
− EC
+ EAB
− 2EBC
+ EAC
+ 2EB EBC − 2EC EBC + 2EA (EAB + EAC )
− 4EB (EA + EA EC )

REFERENCES

(58)

[1] Bell, J. S. On the Einstein Podolsky Rosen paradox.
Physics 1, 195 (1964).
[2] Popescu, S. & Rohrlich, D. Quantum nonlocality as an
axiom. Foundations of Physics 24, 379–385 (1994).
[3] Barrett, J. et al. Nonlocal correlations as an informationtheoretic resource. Physical Review A 71, 022101 (2005).
[4] Van Dam, W. Implausible consequences of superstrong
nonlocality. Natural Computing 12, 9–12 (2013).

[5] Brassard, G. et al. Limit on nonlocality in any world in
which communication complexity is not trivial. Physical
Review Letters 96, 250401 (2006).
[6] Barrett, J. Information processing in generalized probabilistic theories. Physical Review A 75, 032304 (2007).
[7] Pawlowski, M. et al. Information causality as a physical
principle. Nature 461, 1101–1104 (2009).
[8] Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V. &

<!-- page 12 -->
12
Wehner, S. Bell nonlocality. Reviews of Modern Physics
86, 419 (2014).
[9] Popescu, S. Nonlocality beyond quantum mechanics. Nature Physics 10, 264–270 (2014).
[10] Branciard, C., Gisin, N. & Pironio, S. Characterizing the
nonlocal correlations created via entanglement swapping.
Physical Review Letters 104, 170401 (2010).
[11] Fritz, T. Beyond bell’s theorem: correlation scenarios.
New Journal of Physics 14, 103001 (2012).
[12] Branciard, C., Rosset, D., Gisin, N. & Pironio, S. Bilocal
versus nonbilocal correlations in entanglement-swapping
experiments. Physical Review A 85, 032119 (2012).
[13] Gisin, N. Entanglement 25 years after quantum teleportation: testing joint measurements in quantum networks.
Entropy 21, 325 (2019).
[14] Fraser, T. C. & Wolfe, E. Causal compatibility inequalities admitting quantum violations in the triangle structure. Physical Review A 98, 022113 (2018).
[15] Renou, M.-O. et al. Genuine quantum nonlocality in the
triangle network. Physical Review Letters 123, 140401
(2019).
[16] Pusey, M. F. Quantum correlations take a new shape.
Physics (2019).
[17] Chaves, R. & Fritz, T. Entropic approach to local realism and noncontextuality. Physical Review A 85, 032113
(2012).
[18] Tavakoli, A., Skrzypczyk, P., Cavalcanti, D. & Acı́n, A.
Nonlocal correlations in the star-network configuration.
Physical Review A 90, 062109 (2014).
[19] Rosset, D. et al. Nonlinear bell inequalities tailored for
quantum networks. Physical Review Letters 116, 010403
(2016).
[20] Chaves, R. Polynomial bell inequalities. Physical Review
Letters 116, 010402 (2016).
[21] Tavakoli, A. Quantum correlations in connected multipartite Bell experiments. Journal of Physics A: Mathematical and Theoretical 49, 145304 (2016).
[22] Wolfe, E., Spekkens, R. W. & Fritz, T. The inflation technique for causal inference with latent variables. Journal
of Causal Inference 7 (2019).
[23] Lee, C. M. & Spekkens, R. W. Causal inference via algebraic geometry: feasibility tests for functional causal
structures with two binary observed variables. Journal
of Causal Inference 5 (2017).
[24] Rosset, D., Gisin, N. & Wolfe, E. Universal bound on the
cardinality of local hidden variables in networks. Quantum Information & Computation 18, 910–926 (2018).
[25] Navascues, M. & Wolfe, E. The inflation technique completely solves the causal compatibility problem. Preprint
at https://arxiv.org/abs/1707.06476 (2017).
[26] Luo, M.-X. Computationally efficient nonlinear bell inequalities for quantum networks. Physical Review Letters
120, 140402 (2018).
[27] Canabarro, A., Brito, S. & Chaves, R. Machine learning nonlocal correlations. Physical Review Letters 122,
200401 (2019).
[28] Pozas-Kerstjens, A. et al. Bounding the sets of classical
and quantum correlations in networks. Physical Review
Letters 123, 140503 (2019).
[29] Henson, J., Lal, R. & Pusey, M. F. Theory-independent
limits on correlations from generalized bayesian networks. New Journal of Physics 16, 113043 (2014).
[30] Fritz, T. Beyond Bells theorem II: Scenarios with arbitrary causal structure. Communications in Mathematical

Physics 341, 391–434 (2016).
[31] Chaves, R. & Budroni, C. Entropic nonsignaling correlations. Physical Review Letters 116, 240501 (2016).
[32] Renou, M.-O. et al. Limits on correlations in networks
for quantum and no-signaling resources. Physical Review
Letters 123, 070403 (2019).
[33] Weilenmann, M. & Colbeck, R. Analysing causal structures in generalised probabilistic theories. Quantum 4,
236 (2020).
[34] Ziegler, G. Lectures on Polytopes (Springer, New York,
1998).
