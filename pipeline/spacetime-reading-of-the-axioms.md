---
status: workup           # entry | workup | proposed | project
created: 2026-09-11
entered-by: agent, on Pedro's instruction (session of 2026-09-11)
last-reviewed: 2026-09-11
feeds: B4, B7, B8, B9
machine-written: true
---

# What dualizability and unitarity mean in spacetime

## The paragraph

The programme's question is now "what does a probabilistic theory require in
order to be distributed over space?" [B4, drafted 2026-09-11]. The results so
far answer it with two requirements on a GPT, and both entered as technical
conditions rather than as physics: **dualizability** of every system (dimension
one; Result 0) and **unitarity** of the theory, which for a GPT target is
**self-duality** of its systems (dimension two; Results 1–3). If those two are
to be read as principles in the sense the introduction uses the word
[`glossary.md`], each needs a spacetime meaning that a physicist would accept
before seeing the formalism. This entry collects what the filed sources support
for each, and says which parts are the project's own reading.

The short version, and it is Freed–Hopkins' own framing of the twin pillars of
field theory: **dualizability is locality, unitarity is reflection positivity.**
"The twin pillars of quantum field theory are locality and unitarity. These
fundamental properties persist after Wick rotation: locality manifests as
factorization laws for correlation functions and unitarity manifests as
reflection positivity. Locality is encoded in the Axiom System using
composition of morphisms: gluing bordisms along codimension one submanifolds."
[FH §1, filed `160422`]. The two axioms under discussion are not two technical
conveniences: they are the two things field theory is made of, and the paper's
job is to say what each costs a probabilistic theory.

## The problem

Dualizability and unitarity are currently justified in this project by what they
do (they make the functor exist; they are what the TFT literature assumes), not
by what they mean. Without a spacetime reading:

- the no-go results (Result 0: boxworld, ⊗_min/⊗_max theories, polygons) say
  "these theories fail a mathematical condition", not "these theories cannot be
  distributed over space";
- unitarity looks like an imported convention of the TFT literature, and the
  DECISION owed on it (`results-structure.md`, Owed 1) has nothing to decide
  against.

## Part 1. Dualizability

### 1.1 It is exactly the ability to cut and reglue

The sharpest statement is in a filed source and is a theorem, not an analogy.
Carqueville–Runkel's Lemma 2.4 compares the *path-integral data* — a vector
space Y(E) for each slice E, a vector Y(M) for each bordism M : ∅ → E, and
Y(E ⊔ F) ≅ Y(E) ⊗ Y(F) — with the *functorial data*, a symmetric monoidal
functor Bord_n → Vect. They are equivalent precisely when

- a) the cylinder Y(E × [0,1]) ∈ Y(E) ⊗ Y(Ē) is a nondegenerate copairing, so
  there is a unique dual pairing d_E : Y(Ē) ⊗ Y(E) → k; and
- b) for any closed (n−1)-manifold U embedded in M, if M′ is M cut open along
  U, so that M′ : ∅ → E ⊔ U ⊔ Ū, then Y(M) is recovered from Y(M′) by
  contracting the U and Ū factors with d_U.

[CR Lemma 2.4, filed `170516`; the cutting picture is CR §2.1(v), and CR's own
remark at §2.2(v) is that the gluing law of a functor composes *disjoint*
manifolds while cutting a bordism need not produce disjoint pieces — the duality
data are what repairs the mismatch.]

Read the two clauses as physics. The path-integral data know only what a
theory assigns to a slice; they carry no notion of which boundary is "in" and
which is "out". The duality data are exactly the dictionary that lets you cut a
region of spacetime along an arbitrary slice and put it back together. So:

> **Dualizability is the requirement that a region of spacetime may be cut
> anywhere and reassembled, with the theory's statistics unchanged.**

This is the sharpest available rendering of locality of action (A5) as a
condition on a probabilistic theory, and it is a rendering that does not
mention topology, functors, or categories.

### 1.2 The dual of a system is the same slice read the other way

"In nCob each object x is an oriented (n−1)-manifold, and its dual x* is the
same manifold with its orientation reversed" [Baez–Dolan §2, filed `950305`].
So X^∨ is not a new system: it is the same system with the time direction
across the slice reversed. Cutting a region produces both U and Ū (1.1), i.e.
the same slice appearing once as the future boundary of the past piece and once
as the past boundary of the future piece. Which of the two a given component is
depends on how the region is sliced, not on the system.

This is the categorical shadow of the Feynman–Stückelberg reading: a bent
worldline is pair creation to one observer and propagation to another. **No
filed source states this**; it is folklore (`tft-1d-readings.md` T21 already
flags the "particle–antiparticle" wording as UNVERIFIED attribution). If the
paper wants the sentence, Stückelberg or Feynman has to be filed. The
formalism-free version that *is* supported: the assignment of a state space to
a slice must not depend on which side of the slice one calls the future.

### 1.3 Pushed to the limit, locality *is* dualizability

Freed, on the cobordism hypothesis: "A theory which extends in this way is
fully local, and it is natural to make this strong locality hypothesis for the
effective topological theory which comes from a gapped physical theory";
and "the idea is that any n-manifold is glued together from balls, so that if
the theory is fully local then its values can be reconstructed from those on a
point" [Freed §2.1, §5, filed `140627`]. The cobordism hypothesis then says
that fully local theories are classified by *fully dualizable* objects — so in
the extended setting "local" and "dualizable" are the same word. TARGET: Lurie,
*On the classification of topological field theories*, is not filed; the
statement above is from Freed's summary plus general knowledge, and must not be
cited from memory.

The project works with a non-extended, 1-categorical Bord_n, where only the
first level of this survives: every slice must be dualizable (Result 0.1, the
slice reduction, CR Thm 3.4). That is the shadow of full locality, and it is
already enough to kill boxworld. Worth saying in the paper, and worth not
overclaiming: the paper's dualizability is one level of a hierarchy whose top
is "the theory is determined by a point".

### 1.4 What it looks like inside the probabilistic theory

The GPT-side translations, all of them already in the toolbox:

- **Teleportation.** The snake identity read in a GPT is exact teleportation,
  the cup a shared resource and the cap a joint effect [BBLW Thm 1, filed
  `080523`; C8, R3; Result 0.3]. Barnum–Duncan–Wilce characterise compact
  closure of a category of convex operational models "as a statement about the
  existence of teleportation protocols, and as the principle that every process
  allowed by that theory can be realized as an instance of a remote evaluation
  protocol — hence, as a form of classical probabilistic conditioning"
  [arXiv:1004.2920 abstract; **NOT FILED**, TARGET for triage].
- **Conjugate systems.** Wilce's postulate is that each system can be paired
  "with an isomorphic conjugate system by means of a non-signaling bipartite
  state perfectly and uniformly correlating each basic measurement on A with
  its counterpart on the conjugate system"; his gloss is that "a conjugate
  system allows for the formation of records of the outcomes of measurements in
  causally separated systems" [arXiv:1206.2897 abstract; **NOT FILED**].
  That gloss is spacetime language already: a record is an imprint of an
  outcome left in another region.
- **The trade-off that makes it non-trivial.** A non-classical system needs
  entangled states *and* entangled effects on its composite with its dual;
  ⊗_max theories lack the second, ⊗_min theories the first (Result 0.6). So
  dualizability is not free, and boxworld's failure is the Short–Barrett
  trade-off (TARGET file).

**The line for the paper.** Dualizability says a system can be moved through
spacetime by local means — cut the region, hand the degrees of freedom to a
conjugate system, reglue. A theory whose systems are not dualizable cannot be
cut; its statistics depend on where you draw the slice; it cannot be the
effective theory of any process in which a pair is created and annihilated.
Boxworld is such a theory.

## Part 2. Unitarity, i.e. self-duality

### 2.1 The two axioms are the two levels of duality, and they are independent

Baez–Dolan, verbatim [filed `950305`]:

> "We have already seen two levels of duality in the definition of a unitary
> TQFT. First, in nCob each object x is an oriented (n−1)-manifold, and its
> dual x* is the same manifold with its orientation reversed. Second, each
> morphism f : x → y is an oriented n-manifold with boundary, and its dual
> f† : y → x is the same manifold with its orientation reversed. It is
> important to note that the dual morphism f† : y → x is different from the
> 'adjoint' morphism f* : y* → x* ... The notion of adjoint morphism is derived
> from duality on objects, but the notion of dual morphism is conceptually
> independent."

So Pedro's observation that Bord is both compact and dagger is the statement
that orientation reversal acts at two levels: on slices, giving duals
(Part 1), and on bordisms, giving the dagger. **They are conceptually
independent** — which is why the project's dimension-one and dimension-two
results test different things, and why a theory can pass one and fail the other
(OST: Result 3).

A unitary TFT is then a functor with Z(f†) = Z(f)† [BD §2; Sawin Def 2, T11].

### 2.2 Why a dagger on a GPT target is self-duality

By construction, as Pedro put it. A dagger sends a process f : A → B to a
process f† : B → A between the *same* systems. The canonical reversal available
in a GPT is the transpose f* : B^∨ → A^∨, which lands on the duals. So a target
category of GPT systems admits a dagger only if each system is identified with
its dual, A ≅ A^∨, by an order isomorphism carrying the state cone onto the
effect cone: **self-duality**.

This is not a fresh claim inside the project; it is what the results already
compute with. The Frobenius form of any GPT-valued 2d TFT "is a linear
isomorphism of the state cone onto the effect cone" [Result 3, Lemma 2.1], and
the OST obstruction is precisely a failure of that identification to be
positive: "only strong self-duality escapes" [Result 3, Lemma 4.1]. What is new
here is reading that computation as the *meaning* of the axiom rather than as a
step in it.

Rigour, two points that must not be blurred:

- **Weak versus strong.** Weak self-duality is an order isomorphism
  V_A ≅ V_A^*; strong self-duality is that isomorphism given by an inner
  product [glossary; SSC Def 4.6]. Barnum–Duncan–Wilce characterise dagger
  compactness "in terms of the existence, for each system, of a symmetric
  bipartite state, the associated conditioning map of which is an isomorphism"
  [arXiv:1004.2920 abstract; **NOT FILED**] — more than weak self-duality, and
  the symmetry of the state is the extra content. The project's results use the
  strong version. Do not write "self-duality" without saying which.
- **Not time symmetry.** A GPT has one deterministic effect and many
  normalised states; terminality is time-asymmetric [`spacetime-axioms.md`;
  Coecke C3]. Self-duality is a statement about the *cones*, and the dagger
  sends the order unit u to a distinguished state — in the 2d results, the unit
  of the Frobenius algebra, which is the handle's fixed point and, for OST,
  forced to be a pole [Result 1.6, Result 3.6]. So "unitarity means the theory
  has no arrow of time" is **wrong** and must not be written.

### 2.3 The spacetime content: reflection positivity, with positivity for free

Freed–Hopkins [filed `160422`]:

> "Three basic lessons we learned about reflection positivity: (i) 'reflection'
> and 'positivity' are distinct; (ii) 'reflection' is a structure whereas
> 'positivity' is a condition; and (iii) 'extended positivity' is a structure,
> not a condition."

and

> "A reflection structure induces a hermitian metric on the vector space of
> states attached to an (n−1)-manifold, and positivity is the condition that
> these hermitian structures be positive definite. Analogous to reflection
> positivity in Euclidean space we see that the partition function of the
> double of a manifold with boundary must be positive in order that a
> reflection structure be positive."

The physical content, which is standard and which FH state as the point of the
paper: reflection positivity is Wick-rotated unitarity. A process glued to its
own spacetime mirror image has a non-negative value, and that value is the norm
of the state it prepares.

Now translate to a GPT target. This is the project's own reading, and it is the
one worth making the paper's:

> In Hilb, reflection is cheap and positivity is the condition. In a GPT it is
> the other way round. The cones give positivity for nothing — a closed
> spacetime is a morphism 1 → 1, a probability — so the "positivity" half of
> reflection positivity is not a condition on the theory at all; it is built
> into the target. What unitarity asks of a probabilistic theory is only the
> *reflection structure*: that the mirror image of a physical process is again
> a physical process, i.e. that states and effects are the same thing read in
> the two time directions.

And because positivity is built into the target rather than imposed on the
functor, it stops being a condition and becomes an *obstruction*: the loop
weights of Result 0.7 (tr(g) ≥ 0 for every process on a dualizable system, which
kills the gbit and the polygons) and the pants failure of Result 3.7 are exactly
the double-of-a-manifold positivity of FH, evaluated in a theory whose scalars
cannot be negative. That is a genuine structural difference between the GPT
target and Hilb, and it is where the no-gos come from. UNVERIFIED as stated;
what has to be checked is that every FH positivity condition is implied by cone
positivity in the GPT target, not merely that the two smell alike.

### 2.4 What the GPT literature already offers as a meaning for self-duality

Three readings, of which the first is filed:

- **Reversible dynamics.** Bit symmetry — every logical bit can be mapped to
  any other by a reversible transformation — implies self-duality
  [Müller–Ududec, filed `111016`; X-labels in `gpt-axioms.md`]. Reading: the
  dynamics does not distinguish one degree of freedom from another. That is
  close to what "the same law everywhere" means for a field theory, and it is
  the most field-theoretic justification of self-duality available. UNVERIFIED
  as an interpretation; the theorem is theirs, the gloss is ours.
- **Conjugates and filters.** Sharpness, a conjugate system and reversible
  filters give homogeneity and self-duality [Wilce, arXiv:1206.2897; **NOT
  FILED**]; ensemble steering gives homogeneity [Barnum–Gaebler–Wilce,
  arXiv:0912.5532; **NOT FILED**].
- **The honest state of the art.** Tull opens *Deriving Dagger Compactness*
  with "Dagger compact structure is a common assumption in the study of
  physical process theories, but lacks a clear interpretation", and derives it
  from completely mixed states and purification [arXiv:1907.05172; **NOT
  FILED**]. So the gap this entry is trying to fill is a known one, and the
  answers on offer are information-theoretic. A *spacetime* interpretation —
  unitarity as the reflection structure, positivity supplied by the cones —
  would be new. TODO Pedro: is that a claim the paper wants to make?

## If we had a solution, what would it look like

Two paragraphs of the introduction, one per axiom, each stating the axiom in
spacetime terms before any formalism, and each landing on a result:

1. A region of spacetime can be cut anywhere and reassembled ⇒ every slice
   carries a dualizable system ⇒ boxworld and every ⊗_min/⊗_max theory with a
   non-classical system are excluded (Result 0).
2. The mirror image in time of a physical process is a physical process ⇒ the
   theory's systems are self-dual ⇒ quantum and real quantum theory survive
   (Results 1, 2) and OST does not (Result 3).

## Uncertainties

- Whether B4's "distributed over space" should be "spacetime". Part 1 is about
  cutting *spacetime*; the phrase "distributed over space" is the kinematic
  half. TODO Pedro (also logged in `sources/decisions.md`, 2026-09-11).
- Whether dualizability should be motivated by cutting-and-gluing (1.1, fully
  supported by CR, no extended machinery) or by the cobordism hypothesis (1.3,
  stronger and more quotable, but needs Lurie filed and an extended Bord the
  project does not use).
- Whether unitarity is an axiom or a consequence. If self-duality can be
  derived inside the programme from something more primitive (bit symmetry;
  reversible dynamics on a lattice of regions), the paper should derive it
  rather than assume it. The DECISION owed in `results-structure.md` is really
  this question.
- 2.3's claim that cone positivity supplies FH's positivity. Stated, not
  checked.

## Sketch of a plan

1. Triage the five unfiled works named above: Lurie (classification of TFTs),
   Barnum–Duncan–Wilce 1004.2920, Wilce 1206.2897, Barnum–Gaebler–Wilce
   0912.5532, Tull 1907.05172. Atiyah 1988 for the hermitian axiom if the paper
   quotes the original definition of unitary TQFT.
2. Distil 1.1 and 2.1 into toolbox statements (done as T27–T30, see below) and
   check the CR and BD quotations against the PDFs before any of them enters
   the draft.
3. Write the two paragraphs above as candidate B8 prose in
   `syntheses/narratives/intro-narrative.md`, not in `draft.tex`.

## Open questions and disagreements

None recorded yet; the entry was written in one sitting from Pedro's framing of
2026-09-11 and has not been argued over.

## Judgement

For Pedro. Not filled by the agent.

**What would change if this worked?**

**Is the upper bound high enough?**

**What would make us less uncertain?**

## Sources

Filed and quoted: `950305` Baez–Dolan (two levels of duality; unitary TQFT);
`170516` Carqueville–Runkel (Lemma 2.4, cutting and gluing); `140627` Freed
(full locality, reconstruction from a point); `160422` Freed–Hopkins (the twin
pillars; reflection a structure, positivity a condition); `111016`
Müller–Ududec (bit symmetry ⇒ self-duality); `080523` Barnum–Barrett–Leifer–
Wilce (teleportation).

Not filed, quoted from abstracts only and marked as such in the text:
arXiv:1004.2920, arXiv:1206.2897, arXiv:0912.5532, arXiv:1907.05172, Lurie.

Project: `paper/results-structure.md` (Results 0–3), `paper/draft.tex` (B3, B4),
`syntheses/toolbox/` (T3, T5, T11, T21, T22, T25, C8, R3, R5),
`conventions/domain/standing-assumptions.md` (A5, A6).
