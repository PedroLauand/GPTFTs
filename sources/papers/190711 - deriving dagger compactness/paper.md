---
type: paper
date: 2019-07-11
source-of-record: source.md
extraction: machine-generated (pdftotext version 26.04.0; arXiv:1907.05172v2)
reviewed: false
---

# Deriving Dagger Compactness

Machine-generated and unreviewed text extraction of arXiv:1907.05172v2
(15 pages). Check quotations, equations, tables and reading order
against the PDF at <https://arxiv.org/pdf/1907.05172v2>. Page breaks are marked
`<!-- page N -->`.

[UNREADABLE: mathematical notation, figures, diagrams and multi-column layouts
may not be represented reliably in extracted text.]

<!-- page 1 -->
Deriving Dagger Compactness
Sean Tull∗
University of Oxford
sean.tull@cs.ox.ac.uk

Dagger compact structure is a common assumption in the study of physical process theories, but
lacks a clear interpretation. Here we derive dagger compactness from more operational axioms on a
category. We first characterise the structure in terms of a simple mapping of states to effects which
we call a state dagger, before deriving this in any category with ‘completely mixed’ states and a form
of purification, as in quantum theory.

The processes of a general theory of physics are commonly studied in terms of symmetric monoidal
categories [1], very general mathematical structures which come with a helpful graphical calculus in
which processes are represented via boxes and wires [17]. The composition operations in such categories
have a clear operational interpretation as allowing one to run processes both in ‘sequence’ and ‘parallel’,
and thus build more general circuit diagrams resembling experiments [9].
When studying theories resembling quantum or classical physics, it is common to consider categories
with the further structure of being dagger compact [16, 18]. Compactness is a property of a category
allowing one to ’bend wires’ in diagrams, often motivated by its connection to quantum teleportation [1].
As well as this, the extra structure of a dagger allows one to ‘flip diagrams upside-down’ as below:

†

(1)

Though diagrammatically and mathematically well-behaved, dagger compactness adds a significant
amount of extra structure to a category, and the dagger lacks a clear meaning in terms of processes.
As such, several authors have sought to understand the dagger in more operational language [21, 15, 2].
In this article, we explore elementary operational axioms on a category which induce a dagger compact structure. More precisely, we give axioms on a symmetric monoidal category coming with chosen
discarding and completely mixed states which ensure that it is dagger compact.
Our starting observation is that in a compact category the dagger is determined by its mapping from
states (processes with no input) to effects (with no output). In Section 2 we axiomatise when such
a mapping induces a dagger compact structure on a category, calling such a map a state dagger. In
Sections 3 and 4 we show how such mapping may be extended from any suitable subcategory, in passing
noting a new characterisation of Selinger’s CPM construction [16].
Inspiration for our approach comes from quantum theory, where the dagger has a clear operational
meaning on those states which are pure. Thanks to purification we may then extend this assignment
to arbitrary processes in the theory. Our main result in Section 5 applies our results to derive dagger
compact structure in any category satisfying a suitable form of purification. In future work we hope to
extend of our approach to include classical as well as quantum systems.
∗ This research was supported by an EPSRC Doctoral Prize.

Bob Coecke and Mathew Leifer (Eds.):
Quantum Physics and Logic 2019 (QPL)
EPTCS 318, 2020, pp. 181–195, doi:10.4204/EPTCS.318.11

c S. Tull
This work is licensed under the
Creative Commons Attribution License.

<!-- page 2 -->
Deriving Dagger Compactness

182

Motivation for our work comes from several recent reconstructions of finite-dimensional quantum theory in terms of elementary categorical axioms, each of which rely on a dagger compact structure [20, 14]. In future work we hope to apply these results to remove such assumptions from these
reconstructions, in order to provide them with a full operational interpretation.
Related work Several authors have attempted to derive daggers previously. Notably, Bas Westerbaan
has derived a dagger on a ‘pure’ subcategory from a series of axioms on an effectus [21], without restricting to finite dimension or requiring monoidal structure. Selby and Coecke have characterised the dagger
on pure quantum processes in terms of a mapping of states to effects (called a test structure) within the
setting of locally tomographic theories [15]. Our results differ by treating dagger compactness as one
entity and on the whole category, rather than just considering the dagger on pure maps.
Elsewhere, Barnum, Duncan and Wilce studied dagger compactness for finite-dimensional convex
operational models [2], and Cunningham and Heunen considered chosen completely mixed states in [10].

1

Setup

Throughout we will work in the following general setting for describing composable processes [9]. Recall that a category C is symmetric monoidal when it comes with a functor ⊗ : C × C → C, a distin∼
∼
guished unit object I and natural coherence isomorphisms (A ⊗ B) ⊗ C −
→ A ⊗ (B ⊗ C), A ⊗ I −
→ A, and
σ : A ⊗ B ≃ B ⊗ A, satisfying some straightforward equations [9]. Such categories are most easily treated
using their graphical calculus in which morphisms are depicted as boxes, read from bottom to top, with
A

A

C

B⊗D

C

B

D

f

g

A

C

g
idA
A

=

=

g◦ f

f ⊗g

=

f
A

A

A ⊗C

A

The (identity on) the unit object I is the empty picture, so that morphisms I → A, called states, are
depicted with ‘no input’, effects A → I have ‘no output’, and scalars I → I have neither. The swap
isomorphism is depicted by ‘crossing wires’ . For more on the graphical calculus see [17].
The categories we will work also typically come with the following operational features allowing us
to throw systems away, as well as prepare them in a ‘maximally noisy’ state.
Definition 1. We say that C has discarding when every object A comes with a chosen effect
=
A⊗B

=
A

B

I

Dually, C has completely mixed states [10] when every object A has a chosen state
A⊗B

A , such that

A
=

We call a morphism f : A → B causal when

B

A , satisfying

I
=

B ◦ f = A and co-causal when f ◦ A = B .

Remark 2. We will not require completely mixed states to be normalised, so that in general ◦ 6= idI .

<!-- page 3 -->
S. Tull

183

Our categories of interest will satisfy the following property allowing one to ‘bend wires’ in diagrams. A symmetric monoidal category is compact when every object A has a dual object, that is an
of A∗ ⊗ A (the ‘cup’) and effect
of A ⊗ A∗ (the ‘cap’) satisfying the
object A∗ along with a state
snake equations:
A

A

A

A

=
A

=
A

A

A

where in the right-hand sides above we draw the identity morphism on A as an upward directed wire and
that on A∗ as a downward directed one. For any dual object we define a further state and effect

:=

:=

In this article we will be interested in deriving the following useful extra structure on our categories,
giving the ability to ‘reverse’ morphisms. A dagger category is a category C coming with an identityon-objects contravariant involutive endofunctor (−)† . In other words, for each morphism f : A → B there
is a chosen morphism f † : B → A, satisfying
id†A = idA

f †† = f

(g ◦ f )† = f † ◦ g†

A dagger symmetric monoidal category moreover has that ( f ⊗ g)† = f † ⊗ g† and that each coherence
isomorphism is a unitary, i.e. an isomorphism u with u−1 = u† . Finally, such a category C is dagger
compact when every object has a dagger dual, i.e. a dual whose cup and cap satisfy
=



†

When C has discarding it automatically has a choice of completely mixed states = † and we additionally require on each object that
=

=
(2)

Dagger categories come with their own graphical calculus [17] in which the dagger corresponds to
reflecting morphisms vertically as in (1). However here we will be deriving the existence of daggers in
the first place, and so not use such diagrammatic rules.
Examples 3. Our main examples of dagger compact categories with discarding are the following.
1. In FCStar the objects are finite-dimensional C*-algebras and the morphisms completely positive
maps f : A → B. Here I = C and ⊗ is the standard one of such algebras, with the scalars given by
R≥0 . The dagger is given by the Hermitian adjoint, by the assignment a 7→ Tr(a), and A is the
assignment 1 7→ 1A . The commutative algebras give a subcategory FClass.
2. Quant is defined as the full subcategory of FCStar on algebras of the form B(H ). In particular
states correspond to unnormalised density matrices, with given by the identity matrix. The ’cup’
and ’cap’ are given by the Bell state and effect, respectively.

<!-- page 4 -->
Deriving Dagger Compactness

184

3. More generally, we may consider QuantS := CPM(MatS ) for any phased field [20], i.e. any involutive
field (S, †) whose elements of the form a† · a are closed under addition. Then QuantC ≃ Quant while
QuantR is quantum theory over real Hilbert spaces [12].
4. In Rel, objects are sets and morphisms R : A → B are relations R ⊆ A × B. Composition is the usual
one of relations, with I = {⋆} the singleton set, ⊗ given by the Cartesian product, and the dagger by
picking out
relational converse. A is the relation A → I with a 7→ ⋆ for all a ∈ A, with A∗ = A and
the elements of the form (a, a). This example may be generalised to Rel(C) for any regular category
C, or indeed any bicategory of relations [13, 4].

2

State daggers

Though the dagger often lacks a clear interpretation, we will see that it often has a clearer meaning on
(certain) states. We now reduce dagger compactness to the following more lightweight structure.
Definition 4. A symmetric monoidal category C has a state dagger when each object A comes with a
mapping of states to effects
A

ψ

ψ
7→
A

such that idI = idI and for all states ψ , φ we have

ψ

φ

!

ψ
=



φ



φ
ψ



 =

ψ
φ

(3)

and for all states ψ and coherence isomorphisms γ (= α , ρ , λ , σ ) of C we have






A B C

γ
ψ



ψ



 =


γ −1

(4)

A B C

We say an object has a state dagger dual when it has a dual object whose cup and cap satisfy
=





(5)

Proposition 5. Specifying a dagger compact structure on a symmetric monoidal category C is equivalent
to specifying a state dagger for which every object has a state dagger dual.
Proof. If C is dagger compact then the assignment ψ = ψ † yields a state dagger since the dagger is a
monoidal functor and all coherence isomorphisms are unitary. Then (5) is simply the statement that every
object has a dagger dual. Conversely, let us suppose that C comes with such a state dagger.

<!-- page 5 -->
S. Tull

185

We first show that the state dagger is injective. Suppose that ψ = φ for two states ψ , φ . Then
choosing any state dagger dual of their domain we have





ψ


= 

ψ 

 = 

φ 
 =

φ

Then composing with
on the left shows that ψ = φ . Next, note that applying (3) and (4) we obtain
the rule




ψ
ψ
φ
 φ 


=
(6)
=
=




φ
φ
ψ
ψ

for all states ψ , φ . Now let f : A → B be any morphism and choose a state dagger dual B∗ for B. We
define f † to be the unique morphism such that


†
f 
f

=
(7)
Indeed since the state dagger is injective, any such morphism must be unique. To show that it exists,
choose a state dagger dual A∗ for A and then note that




B
A
A
′
B
f


f′

f
f
f
 =⇒ 
=
:= 

 =


B

A

as required, using (6) in the first equality and the snake equations in the second. Since f ′ does not depend
on our choice of dual for B, f † does not either, and satisfies (7) for any such dual B∗ . Now let g : A′ → B′
be any other morphism, and choose a state dagger dual B′∗ for B′ . One may straightforwardly check that
the state ω defined by
B

B′ B

B′

exhibits (B∗ ⊗ B′∗ ) as a state dagger dual of (B ⊗ B′ ). Then we have that ( f ⊗ g)† = f † ⊗ g† since




B
B′ A
A′
B ⊗ B′ A ⊗ A′





† ⊗ g† 
†
† 

f
f
 =

g
=

 = 
f ⊗g

g
f




B

B′

A

A′

B ⊗ B′ A ⊗ A′

Next consider any morphism g : B → C, and choose a state dagger dual C∗ for C. Then we have




C
A


C
A
g




† 

f


 = 

g
f
f
=
f†  =
g†






†
g
A
C


C

A

<!-- page 6 -->
Deriving Dagger Compactness

186

Hence (g ◦ f )† = f † ◦ g† . By definition id†A = idA for all objects A. The fact that every coherence
isomorphism is unitary follows from (4) when ψ is the state of a state dagger dual. This makes the
dagger a strict symmetric monoidal functor. Moreover since by the second equation of (3) we have
ψ † = ψ for all states ψ .
To check that the dagger is involutive, by bending wires one may see that it suffices to show that
ψ †† = ψ for all states ψ . Now setting f = ψ † and choosing the trivial state dagger dual I ∗ = I, (7) tells
us that by definition φ := ψ †† is the unique state φ with φ = ψ † . But since ψ = ψ † we have φ = ψ by
injectivity of the state dagger. Every state dagger dual is then a dagger dual, making C dagger compact.
Finally note that this is a correspondence between dagger compact structures and such state daggers.
Indeed we have seen that ψ = ψ † for all states ψ . Conversely, when defining (−) in this way, every
dagger satisfies our definition of f † above since it is an involutive monoidal functor.
This result extends to include discarding morphisms as follows.
Proposition 6. Let (C, ) be a symmetric monoidal category with completely mixed states. Specifying
a compatible dagger compact structure on C is equivalent to specifying a state dagger such that each
object has a state dagger dual satisfying (2), where := ( ).
Proof. By Proposition 5, noting that the condition is equivalent to compatibility of the duals with .

3

Daggers from dilations

In defining a dagger compact structure on a whole category, it can sometimes be useful to extend an
existing one defined on a subcategory, as we will see for quantum theory in the next section. First, we
call a state σ a dilation of a state ρ when

ρ

=

σ

By a dilation structure we mean a symmetric monoidal category C with discarding coming with a
chosen symmetric monoidal subcategory D such that every state in C has a dilation belonging to D. We
call a dilation structure dagger compact when C is a dagger compact category with discarding and D is
a dagger compact subcategory of C.
Theorem 7. A dilation structure (C, D, ) is dagger compact iff C has chosen completely mixed states,
D has a state dagger satisfying

ψ

A

A
B

ψ

C

=

B

=⇒

φ

φ

=

A

C

(8)

A

and in D every object A has a state dagger dual A∗ which in C satisfies (2).
Proof. By Proposition 5 the state dagger makes D dagger compact; we now extend it to C as follows.
For any state ρ , let ψ be a dilation of ρ belonging to D. Then we set

ρ

:=

ψ

(9)

<!-- page 7 -->
S. Tull

187

Thanks to (8) this is independent of our choice of dilation ψ . Since any state in D of an object A may be
seen as a dilation of itself (via the object I and coherence isomorphism A ⊗ I ≃ I), this coincides with the
state dagger on D. Let us check that this is compositional. Since dilations compose under ⊗, it is easy
to see that the left-hand equation of (3) is satisfied. Since all coherence isomorphisms belong to D the
and
condition (4) also lifts easily to C. By definition ( ) = since has dilation
=

=

Let ρ , σ ∈ C with respective dilations ψ , φ ∈ D. Then using our assumption on duals and the definition
of our state dagger we have




ψ
φ
ρ
σ


 =

 = 
=


ρ
φ
σ
ψ

Next note that since every object of C has a state (e.g. ), C and D have the same objects by the definition
of a dilation structure. Hence every object has a dual. Finally, by assumption on D these duals satisfy the
requirements of Proposition 6.

4

Daggers in CPM categories

A useful source of dagger compact categories with discarding are those CPM(D) arising from Selinger’s
CPM construction on a dagger compact category D [16]. The motivating example is
Quant ≃ CPM(Quant pure )
where Quant pure is the subcategory of ‘pure’ morphisms, explored in the next section. Coecke has
shown that such categories correspond precisely, via C ≃ CPM(D), to dagger compact dilation structures
(C, D, ) satisfying the CP axiom [8]:
f†

g†
=

f

g

⇐⇒

f

g

=

for all f , g ∈ D with the same domain. This indeed holds for all pure morphisms f , g in Quant.
The analogous condition for state daggers allows us to simplify our earlier results by dropping several
conditions. We can characterise CPM categories in terms of state daggers as follows.
Theorem 8. A category C arises from the CPM construction precisely when it belongs to a dilation
structure (C, D, ) with completely mixed states and a state dagger on D satisfying
A

A

ψ

A

φ
=

B

ψ

⇐⇒

C

φ
A

A

B

ψ

A

=

C

φ

(10)

<!-- page 8 -->
Deriving Dagger Compactness

188

for all ψ , φ ∈ D, and such that in D every object has a state dagger dual satisfying (2). Moreover, we no
longer require condition (4) of a state dagger but only the special case




for all states ψ in D.



ψ


 =

ψ

(11)

Proof. For any dagger compact dilation structure satisfying the CP axiom, as before set ψ = ψ † for all
states ψ . By bending wires, (10) is equivalent to the CP axiom, and (11) holds since the dagger is
symmetric monoidal.
Conversely, let us show that D satisfies the requirements of Proposition 5. Inspecting the proof,
we see that since the rule (11) allows us to deduce (6), we only require the condition (4) on coherence
isomorphisms γ in the case where ψ is the state of a state dagger dual (in order to deduce that γ is
unitary). Let us establish this more generally for any causal isomorphism γ in D. We need to show that
the effect γ ′ defined by

γ′



 γ
:= 



γ′
=

satisfies




γ −1

(12)

Now any coherence isomorphism belongs to D by assumption, and is causal in any category with discarding [19, Chapter 1]. Hence by (10) we have implications

γ′
γ

=

and so

=

γ

=

γ −1
γ

by (10), from which (12) follows as required. Hence by Proposition 5 D is dagger compact.
By Theorem 7 it remains to check that (8) holds in C. Suppose that ψ , φ ∈ D satisfy the left-hand
side of (8). Then we must show that the effect

ψ

=

ψ

is equal to the effect obtained by replacing ψ by φ . But by (10) this effect is determined by the morphism

ψ

ψ
=

ψ

ψ

ψ
=

ψ

using naturality of in the second step. But by (the horizontal reflection of) (10) the latter morphism is
determined by applying to the right output of ψ , which is equal to doing the same to φ .

<!-- page 9 -->
S. Tull

5

189

Daggers from purification

Let us now apply our earlier results to derive dagger compactness from operational axioms on a category
C with discarding and completely mixed states.
First, recall that C has zero morphisms when there is a morphism 0 : A → B between any two objects
A, B which compose via ◦ and ⊗ with any morphism to give 0. We then say that C satisfies normalisation
when every non-zero state is of the form
=

ρ

σ

r

for some scalar r and unique causal state σ , which we call the normalisation of ρ . Normalisation is
automatic when all non-zero scalars are invertible, as in our main examples here. Our axioms will
concern morphisms of the following form.
Definition 9. [5] A morphism f is pure when either f = 0 or f satisfies
f

g

=

g

=⇒

=

ρ

f

for some causal ρ

(13)

This notion of purity in fact typically coincides with the more usual one in terms of mixing [19, Chap. 4].
Indeed, in Quant a morphism is pure in this sense precisely when it is given by a Kraus operator.
Lemma 10. Let C satisfy normalisation. Then pure states are closed under normalisation and ⊗.
Proof. For the first part, say ψ = φ ◦ r for a scalar r, where φ is causal. Then if some state ρ dilates φ
it is causal, and moreover ρ ◦ r dilates ψ . Hence ρ ◦ r = ψ ⊗ σ = (φ ⊗ σ ) ◦ r for some causal state σ .
From uniquness of normalisation and causality of these states we obtain ρ = φ ⊗ σ , as required.
Next, suppose that states ψ , φ are pure, and ρ is some dilation of ψ ⊗ φ . Then the normalisation of
ρ is also a dilation of the tensor ψ ′ ⊗ φ ′ , of the respective normalisations of ψ , φ . Hence by the previous
part it suffices to consider when ψ and φ are causal. Then we have implications
=

ρ

ψ

=⇒

φ

=

ρ

ψ

Hence ρ = ψ ⊗ σ for some causal state σ . Composing with on the left then shows that σ dilates φ and
so σ = φ ⊗ τ for some causal state τ . Hence we have ρ = ψ ⊗ φ ⊗ τ , as required.
Definition 11. We consider symmetric monoidal categories (C, , ) with discarding, completely mixed
states, and normalisation, satisfying the following axioms.
1. (Purification) [6] Every state ρ has a purification, i.e. a dilation
=

ρ

ψ

for which ψ is pure. Moreover, purifications are essentially unique in that
B
A

A

A

B

ψ

B

A

U

B

=

φ

=⇒

ψ

=

φ

for some causal and co-causal isomorphism U on B, for all such pure states ψ , φ .

(14)

<!-- page 10 -->
Deriving Dagger Compactness

190

2. (Sharpness) [11] For every causal pure state ψ there is a unique pure co-causal effect ψ with

ψ
=

(15)

ψ
Moreover, ψ is conversely the unique causal pure state satisfying the above.
We may then similarly assign an effect to each non-zero (not necessarily causal) pure state ψ via

ψ

:=

r

φ
(16)

where φ is the (pure by Lemma 10) normalisation of ψ , and r = ◦ ψ . We also set 0 = 0.
3. (Pure composition) For all causal pure states ψ , φ , the following state and effect are pure with


φ



ψ

4. (Pre-duals) Each completely mixed state
B
A

ω

 =

(17)

φ

A has a purification ω satisfying

ω

B

=

ψ



ω
=

A
B

B
B

5. (Identity tomography) For all endomorphisms V we have



 V =
∀ pure ψ  =⇒

ψ
ψ

A

V

=
A

(18)

=

Examples 12. QuantS satisfies these axioms, for any phased field S, including Quant and QuantR .
More generally, they follow from the ‘operational principles’ of [20]; as we prove in appendix 4.
All of the axioms aside from purification and purity of ω in the pre-duals axiom hold in FCStar and
Rel. In FCStar pure morphisms between direct sums of quantum algebras are simply those induced by
some single pure morphism B(Hi ) → B(H j ) in Quant. In Rel a morphism is pure iff it is empty or a
singleton. The failure of purification in these examples has led to alternative definitions of purity [14, 10].
Let us discuss these axioms in more detail. Sharpness essentially appears as the first axiom in Hardy’s
reconstruction of quantum theory [11] and is crucial in allowing us to define a (state) dagger as a property
rather than extra structure. The characterisation of ψ is also similar to the ‘test structures’ considered
in [15] and relates to causal pure states being dagger kernels; see appendix A.
Purification is a standard axiom for capturing quantum theory [6, 7, 20]. We require each U to be cocausal since in Quant each is the unique state (up to scalars) preserved by all causal isomorphisms [7].
Symmetric monoidality of Cpure mainly involves pure morphisms being closed under ◦ by Lemma 10. In
the compact setting it suffices that each state (17) is pure (axiom 5 of [7]). The pre-duals axiom and (17)
are necessary for dagger compactness. Finally, identity tomography is a special case of more general
tomography axioms [3, 6]. It is weaker than local tomography, since this fails in QuantR [12, 7].
Our main result is now the following.

<!-- page 11 -->
S. Tull

191

Theorem 13. Let C be a symmetric monoidal category with discarding and completely mixed states ,
satisfying normalisation and the above axioms. Then C forms a dagger compact category with discarding, with the pure morphisms Cpure as a dagger compact subcategory.
Proof. We will show that Cpure is a subcategory with state dagger (16). Let us first show that C has duals
whose cups are pure and satisfy (5), (2). First note that by definition for all pure states ψ we have

ψ

ψ

=

ψ

(19)

ψ

Now for any object A, let ω be a pure state of A ⊗ B as in (18), and define

ω
:=

V

ω
Then for all causal pure states ψ of A by (17) we have

ω

ψ
V

ψ

ω
ψ

=

ψ
=

ψ

=

ψ

ω

ψ
ψ

=

ω

But V is causal by construction and hence so is V ◦ ψ . Moreover this state is pure by the assumption
that all states and effects as in (17) are. Hence we have V ◦ ψ = ψ . By normalisation the same holds for
arbitrary pure states ψ . Hence by identity tomography we have V = id. Hence ω satisfies the first snake
equation, and the other equation holds similarly. By construction these duals satisfy (5), (2).
Since C has pure cups and caps, all isomorphisms in C are pure, including the coherence ones.
Moreover bending wires in (17) now shows that pure morphisms are closed under composition ◦, and
they are closed under ⊗ by Lemma 10. Hence Cpure is a symmetric monoidal subcategory of C.
Now let us show that (16) indeed defines a state dagger on Cpure . Firstly, note that for arbitrary (not
necessarily causal) pure states ψ , the effect ψ is pure since all scalars are by Lemma 10. By definition
we have idI = idI . The second condition of (3) holds by (17). By normalisation it suffices to verify the
remaining conditions for pure states which are causal. Now the first condition of (4) follows in Cpure
since for all causal pure states ψ , φ we have

ψ

φ

ψ

φ

=

Next, note that all coherence isomorphisms γ in Cpure are causal and co-causal in C [19, Chap. 1].
Hence 4 follows for any causal pure state ψ since we have

ψ
γ −1
γ
ψ

ψ
=

=

ψ

<!-- page 12 -->
Deriving Dagger Compactness

192

This establishes the presence of the state dagger. Next let us verify (8) for all pure states ψ , φ of some
object A ⊗ B. By normalisation it suffices to consider when ψ , φ are causal. Suppose the left-hand side
of (8) is satisfied. Then by essential uniqueness there is some causal and co-causal isomorphism U on B
for which the following all hold

ψ
ψ

U

=

φ

ψ
U

=⇒

φ

=

ψ

φ
=

=⇒

=

U

ψ

Then since U is co-causal we obtain the right-hand side of (8), and so we are done by Theorem 7.
In principle this result should now allow us to adapt the categorical quantum reconstruction [20] to
not explicitly require a dagger, and thus be more fully operational in nature. For this one should derive
our less operationally clear ‘pure composition’ and ‘pre-duals’ axioms from more well-motivated ones,
as we begin to explore in appendix A.
Remark 14. In future it would be desirable to derive dagger compactness in categories without such
purification, such as FCStar and Rel, for example allowing for a dagger-free version of the reconstruction [14]. Speculatively, it may suffice to characterise those self-adjoint morphisms U , with U = U † . Indeed in both categories every state ρ may be written as U ◦ for some such morphism, so that ρ † = ◦U .

References
[1] S. Abramsky & B. Coecke (2004): A categorical semantics of quantum protocols. In: Logic in Computer
Science 19, IEEE Computer Society, pp. 415–425, doi:10.1109/lics.2004.1319636.
[2] Howard Barnum, Ross Duncan & Alexander Wilce (2013): Symmetry, compact closure and dagger compactness for categories of convex operational models. Journal of philosophical logic 42(3), pp. 501–523,
doi:10.1007/s10992-013-9280-8.
[3] J. Barrett (2007): Information processing in generalized probabilistic theories. Physical Review A - Atomic,
Molecular, and Optical Physics 75(3), doi:10.1103/PhysRevA.75.032304.
[4] A. Carboni & R. Walters (1987): Cartesian bicategories I. Journal of pure and applied algebra 49(1-2), pp.
11–32, doi:10.1016/0022-4049(87)90121-6.
[5] G. Chiribella (2014):
arXiv:1411.3035.

Distinguishability and copiability of programs in general process theories.

[6] G. Chiribella, G. M. D’Ariano & P. Perinotti (2010): Probabilistic theories with purification. Physical Review
A 81(6), p. 62348, doi:10.1103/physreva.81.062348.
[7] G. Chiribella, G. M. D’Ariano & P. Perinotti (2011): Informational derivation of quantum theory. Phys. Rev.
A 84(1), p. 12311, doi:10.1103/PhysRevA.84.012311.
[8] B. Coecke (2008): Axiomatic description of mixed states from Selinger’s CPM-construction. Electronic
Notes in Theoretical Computer Science 210, pp. 3–13, doi:10.1016/j.entcs.2008.04.014.
[9] B. Coecke & E. Paquette (2011): Categories for the practising physicist. In: New Structures for Physics,
Springer Berlin Heidelberg, pp. 173–286, doi:10.1007/978-3-642-12821-9˙3.
[10] O. Cunningham & C. Heunen (2018): Purity through Factorisation. In: Proceedings of the 14th International
Conference on Quantum Physics and Logic, Electronic Proceedings in Theoretical Computer Science 266,
pp. 315–328, doi:10.4204/EPTCS.266.20.
[11] L. Hardy (2011): Reformulating and Reconstructing Quantum Theory. arXiv:1104.2066.

<!-- page 13 -->
S. Tull

193

[12] L. Hardy & W. Wootters (2012): Limited Holism and Real-Vector-Space Quantum Theory. Foundations of
Physics 42(3), pp. 454–473, doi:10.1007/s10701-011-9616-6.
[13] C. Heunen & S. Tull (2015): Categories of relations as models of quantum theory. In: Proceedings of the
12th International Workshop on Quantum Physics and Logic, Electronic Proceedings in Theoretical Computer Science 195, pp. 247–261, doi:10.4204/EPTCS.195.18.
[14] J. H. Selby, C. M. Scandolo & B. Coecke (2018): Reconstructing quantum theory from diagrammatic postulates. arXiv:1802.00367.
[15] John Selby & Bob Coecke (2016): Process-theoretic characterisation of the Hermitian adjoint. arXiv preprint
arXiv:1606.05086.
[16] P. Selinger (2007): Dagger Compact Closed Categories and Completely Positive Maps: (Extended Abstract).
Electronic Notes in Theoretical Computer Science 170, pp. 139–163, doi:10.1016/j.entcs.2006.12.018.
[17] P. Selinger (2011): A survey of graphical languages for monoidal categories. In: New structures for physics,
Springer, pp. 289–355.
[18] Peter Selinger (2012): Finite dimensional Hilbert spaces are complete for dagger compact closed categories.
arXiv preprint arXiv:1207.6972.
[19] S. Tull (2018): Categorical Operational Physics. DPhil Thesis. arXiv:1902.00343.
[20] S. Tull (2019): A Categorical Reconstruction of Quantum Theory. Logical Methods in Computer Science.
[21] B. Westerbaan (2018): Dagger and dilations in the category of von Neumann algebras. PhD Thesis.
arXiv:1803.01911.

A

Deriving the axioms

Here we show how several of our axioms on (C, , ) from section 5 follow from assumptions similar to
the reconstruction [20]. We begin with the pre-duals axiom.
Lemma 15. Suppose that the sharpness and pure composition axioms hold, and is the unique effect
sending every causal pure state to idI . Then the pre-duals axiom holds iff each state A has a purification
ω via some object B which also purifies B .
Proof. Let ω be any purification of



ψ
ω



 =

A . Then for all causal pure states ψ of A we have that

ω

and so

ψ

ω
ψ

=

since the left-hand state above is pure and causal as ψ is co-causal. Since ψ was arbitrary, by assumption
this establishes the third equation in (18), and similarly the second holds when ω purifies B .
Now, we will call an object trivial when its identity morphism satisfies
=
Following [20] we say that C satisfies pure exclusion when for any pure state of a non-trivial object there
is some non-zero effect e with
e
= 0
ψ

<!-- page 14 -->
Deriving Dagger Compactness

194

Let us say that C satisfies strong pure exclusion when additionally the dual statement holds; every pure
effect φ of a non-trivial object has φ ◦ ρ = 0 for some non-zero state ρ .
Next, recall that a kernel of a morphism f : A → B is a morphism ker( f ) with
f ◦ g = 0 ⇐⇒ g = ker( f ) ◦ h
for a unique morphism h. Dually a cokernel coker( f ) satisfies g ◦ f = 0 ⇐⇒ g = h ◦ coker( f ) for some
unique h. We will always take our (co)kernels to be (co)causal, and then they are unique up to (co)causal
isomorphism whenever they exist. We will say that C has split (co)kernels when
• Every morphism f has both a causal kernel and co-causal cokernel;
• For every causal kernel k there is a unique co-causal cokernel k with k ◦ k = id. Conversely, k is
the unique causal kernel for which this equation holds.
Lemma 16. Suppose that C has split (co)kernels, satisfies strong pure exclusion, and has that A =
0 =⇒ A = 0 =⇒ idA = 0 for all objects A. Then every causal pure state is a kernel and the sharpness
axiom holds.
Proof. We first show that ◦ f = 0 =⇒ f = 0 for all morphisms f . Define im( f ) := ker(coker( f )).
Then if 0 = ◦ f it follows that 0 = ◦ im( f ) = and so im( f ) = 0. Since it factors over im( f ), f = 0.
We now show every causal pure state ψ is a kernel. Let i = im(ψ ) := ker(coker(ψ )) with i causal.
Then ψ = i ◦ φ for some φ . Since i ◦ i = id it is straightforward to check that φ is again pure and causal,
and by the definition of i that f ◦ φ = 0 =⇒ f = 0. Hence by pure exclusion the domain of i is trivial,
so that φ is a causal isomorphism, and ψ = im(ψ ) as required.
Since our assumptions are self-dual, we dually have that every co-causal pure effect is a cokernel.
Now for the sharpness axiom, by the split (co)kernels assumption, it suffices to check for each causal pure
state ψ that the co-causal cokernel effect c := ψ is pure. Suppose that ◦ f = c. Then ◦ f ◦ ker(c) = 0
so f ◦ ker(c) = 0, and hence f factors over coker(ker(c)) = c since c is a cokernel. Hence f = ρ ◦ c for
some state ρ , which after applying we see is causal. Hence c is indeed pure.
As a result we may define an effect ψ for each pure state ψ as in (16). In this setting we can also
capture our compositionality condition on pure states as follows. Say that C has kernel composition
when (co)kernels are closed under ⊗, cokernels send pure states to pure states, and for all causal kernels
k and pure states ψ we have


ψ
 k 
(20)

 = k
ψ
(Co)kernels are always closed under ⊗ in any compact category [19, Chap. 4], to which we refer
along with [20] for proof that all of these axioms hold in each theory QuantS for a phased field S.
Lemma 17. Suppose that C has the properties of Lemma 16 and kernel composition. Then C satisfies
the pure composition axiom.
Proof. By assumption and Lemma 16 for any causal pure state φ and extra object the morphisms

φ

φ

<!-- page 15 -->
S. Tull

195

are a kernel and cokernel respectively. Hence the state in (17) is an application of a cokernel to a kernel
and so is pure. Moreover, the above morphisms are (co)causal respectively and are inverse to eachother,
so that for any pure bipartite state ψ we obtain (17). Finally, we need that effect in (17) is pure. By
assumption it suffices to show that c = ψ is pure for any pure state ψ , or in other words that for any
causal such state ψ and scalar r that r ◦ c is pure. The proof is almost identical to the proof that c is pure
in the previous result, noting in the last step we have f = ρ ◦ c and then applying and normalisation we
get ρ = σ ◦ r for some causal state σ , so that f = σ ◦ r ◦ c, as required.
Proof of Example 12. Let C satisfy the operational principles of [20], to which we refer for the following facts. Essentially unique purification holds by assumption, noting that every causal isomorphism
is pure and hence co-causal by the CP axiom, and normalisation since all scalars are pure and scalar
multiplication is cancellative.
Next, the sharpness axiom holds with ψ being given by ψ † . Indeed, in [20] it is shown that each
such ψ is a dagger kernel, giving (15). Moreover if φ ◦ ψ = idI for some co-causal pure effect φ then
since C has addition with φ + ◦ ker(φ ) = for some effect e, and addition is cancellative, we obtain
◦ ker(φ ) ◦ ψ = 0 so that ker(φ ) ◦ ψ = 0. Hence since φ is a cokernel we get that ψ factors over φ † and
so both states are equal by assumption. Dually we see that ψ is unique with ψ † ◦ ψ = idI also. The pure
composition and pre-dual axioms then hold by dagger compactness of C and Cpure .
It remains to verify identity tomography. Let W be an endomorphism of some object A which preserves all pure states ψ , with a purification U . Then for any such state since ψ is pure we obtain that
U ◦ ψ = ψ ⊗ uψ for some causal pure state uψ , which is straightforward to check must be pure also.
Now in [20] it is shown that we may view Cpure as the quotient category of a dagger compact category
A(:= GP(B)) given by identifying a group of unitary scalars. So let V ∈ A with U = [V ] in Cpure . Then
in A we again have V ◦ ψ = ψ ⊗ vψ for some state vψ , for all states ψ . Causality of [vψ ] in Cpure gives
that vψ is an isometry. We now show that vψ does not depend on ψ .
Since A has an addition operation on morphisms we then have for all states ψ , φ that

ψ ⊗ vψ + φ ⊗ vφ = V ◦ ψ +V ◦ φ = V ◦ (ψ + φ ) = (ψ + φ ) ⊗ vψ +φ = ψ ⊗ vψ + φ ⊗ vφ
Whenever ψ and φ are orthonormal, so that ψ † ◦ φ = 0 and ψ † ◦ ψ = idI = φ † ◦ φ , by composing with
ψ † and φ † it then follows that vψ = vψ +φ = vφ . But more generally for we may write ψ = φ ◦ z + µ for a
state µ which is orthogonal to φ , where z = ψ † ◦ φ . It then follows that vφ = vµ = vψ . Since every state
in A is a multiple of an isometric one, the same holds for arbitrary states ψ , φ .
Hence we have V ◦ ψ = ψ ⊗ v for some fixed isometric state v. But since A is well-pointed, this gives
V = id ⊗ v. Then [U ] = id ⊗ [v] also, so that W = id as required.
