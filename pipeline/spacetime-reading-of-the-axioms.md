---
status: workup           # entry | workup | proposed | project
created: 2026-09-11
entered-by: agent, on Pedro's instruction (session of 2026-09-11)
last-reviewed: 2026-09-11
feeds: B3, B7, B8, B9
machine-written: true
---

# What dualizability and unitarity mean in spacetime

## The paragraph

The programme's question is "what does a probabilistic theory require in order
to be distributed over space?" [B3, drafted 2026-09-11]. The results so far
answer it with two requirements, and both entered as technical conditions
rather than as physics: **dualizability** of every system (dimension one;
Result 0) and **unitarity** of the theory, which for a GPT target is
**self-duality** of its systems (dimension two; Results 1–3). Each needs a
statement a physicist would accept before seeing any formalism. This entry
gives one for each, in the vocabulary the paper already uses — regions, slices,
states, effects, processes, probabilities — and nothing else.

The two statements, first:

> **Dualizability.** A slice can be moved from the end of a region to its
> beginning. What one part of spacetime delivers on a slice, the adjacent part
> receives on the same slice; a theory distributed over space must be able to
> describe the slice both ways and pair the two descriptions. The price in a
> probabilistic theory is a pair of entangled state and entangled effect, i.e.
> exact teleportation.

> **Unitarity.** A region can be read from either end. Read forwards it takes
> states to states; read backwards it takes effects to effects. For both
> readings to be processes of the same theory on the same systems, states and
> effects must be the same objects. The price is self-duality.

They are different requirements, and a theory can meet one and fail the other:
OST does (Result 3).

## The problem

Dualizability and unitarity are currently justified by what they do — they make
the functor exist, they are what the TFT literature assumes — not by what they
mean. Without a physical reading, Result 0 says "boxworld fails a mathematical
condition" rather than "boxworld cannot be distributed over space", and the
unitarity DECISION owed in `results-structure.md` has nothing to decide
against.

---

## Part 1. Dualizability: a slice can be moved to the other end

### 1.1 The setting, stated once

A probabilistic theory distributed over space assigns

- a **system** of the theory to each region of space (a slice);
- a **process** of the theory to each region of spacetime, taking the system on
  the slice where the region begins to the system on the slice where it ends.

That is all the structure there is, and it is the content of a symmetric
monoidal functor Bord_d → (GPT, ⊗) [T1, T2, T7]. The requirement below is what
that assignment costs.

### 1.2 The requirement

Take a region of spacetime and cut it along an intermediate slice U. The lower
piece ends on U; the upper piece begins on U. Regluing means summing over
everything that can cross U: pairing what the lower piece **delivers** on U
against what the upper piece **receives** on U.

Delivering and receiving are not the same kind of thing in a probabilistic
theory. What is delivered is a **state**; what is received is consumed by an
**effect**. So the slice U carries two descriptions — the system as something
produced, and the system as something consumed — and cutting is only possible
if the theory pairs them.

Write Ū for the second description: the same slice, entered from the other
side. The requirement is then three sentences:

1. **The pairing exists.** There is an effect on U ⊗ Ū that consumes a state
   delivered on U together with whatever receives it. (The **cap**.)
2. **Nothing is lost.** There is a state of Ū ⊗ U that the pairing recovers
   completely: no part of what crosses the slice is invisible to the pairing.
   (The **cup**.)
3. **Cutting and regluing changes nothing.** Cut a region, pair across the cut,
   and the result is the region you started with. (The **snake identity**.)

A system with these three is *dualizable*, and Ū is its dual. Nothing beyond
"cut a region anywhere, glue it back, get the same statistics" has been assumed.

This is not an analogy. It is the content of a filed theorem: Carqueville–Runkel
compare the data of a theory that only knows what to assign to slices with the
data of a functor, and they are equivalent exactly when (a) the cylinder over U
is a non-degenerate pairing and (b) the value on a region cut along any
embedded U is recovered by contracting with that pairing [CR Lemma 2.4, filed
`170516`; toolbox T27]. CR's own remark is the same point in one line: gluing
in a functor composes end to end, while cutting a region need not produce
pieces that meet end to end, and the duality data are what repairs the mismatch
[CR §2.2(v)].

### 1.3 What it says about time

The two descriptions U and Ū are the same region of space; what differs is
which side of the slice one stands on. A theory in which the two are unrelated
would have to know, of each slice, which of its two sides is the past. The
requirement says it need not: the theory can carry a slice from the end of a
region to its beginning, at the price of exchanging the two descriptions.

So the process a region describes can begin with two systems and end with none:
take the region that starts at the bottom of a slab, bends over and comes back
down. Read by the clock it is **a pair appearing out of nothing and later
annihilating**. The cup is the appearance, the cap the annihilation, and the
snake says that a pair created and one member annihilated against an incoming
system leaves that system untouched [T21, T22].

### 1.4 What it costs a probabilistic theory

In a GPT the cup is a bipartite state and the cap a bipartite effect, and the
snake identity is exactly the teleportation protocol: share the cup, measure
the cap jointly with an unknown state, and the unknown state appears at the
other end [BBLW Thm 1, filed `080523`; C8, R3; Result 0.3]. So:

> A theory that can be cut is a theory in which a system's state can be handed
> from one region of space to the next without anything travelling in between.

The cost is real, and the no-go is what shows it. A non-classical system needs
entangled *states* and entangled *effects* on its composite with its dual;
⊗_max theories have the first and not the second, ⊗_min theories the second and
not the first [Result 0.6]. Boxworld is of the first kind: it has PR boxes and
no annihilating effect. It can deliver across a slice and cannot receive. So
boxworld cannot be cut, in any dimension — and it is worth saying in the paper
that this is the failure, not "boxworld has no dualizable object".

The same argument in one further step: if the identity on a system factors
through a separable pairing, the system is classical [Result 0.4, 0.5]. So the
pairing across a slice is entangled or the theory on that slice is classical.

---

## Part 2. Unitarity: a region can be read from either end

### 2.1 The requirement

A region of spacetime has two ends, and nothing intrinsic marks one of them as
the beginning. Reading the region from its other end is a second, equally good
description of the same piece of physics. Unitarity is the requirement that the
theory contains both readings:

> The same region, read from either end, is a process of the theory, and the
> two readings determine each other.

In the bordism language this is the operation that swaps the two ends of a
region while leaving its slices alone, and a unitary theory is one with
Z(M read backwards) = Z(M)†, a dagger [BD §2, filed `950305`; Sawin Def 2;
toolbox T28, T11].

### 2.2 Why this is not the same requirement as Part 1

Both requirements are about reversal, and they are different reversals. Stated
side by side:

| | what is exchanged | what stays fixed | price |
|---|---|---|---|
| **dualizability** | a slice moves from one end of the region to the other, and is exchanged for its opposite description | which end is the beginning | entangled state and effect (teleportation) |
| **unitarity** | the two ends of the region are swapped | every slice keeps its description | states and effects are the same objects (self-duality) |

Baez–Dolan say exactly this about the bordism side, and say it matters: the
dual of an object is the slice with its orientation reversed, the dual of a
morphism is the region read backwards, and "the notion of adjoint morphism is
derived from duality on objects, but the notion of dual morphism is
conceptually independent" [BD §2; T28].

That independence is why the project's dimension-one and dimension-two tests
are different tests, and why OST passes one and fails the other (Result 3).

### 2.3 Why it forces self-duality

This is the step Pedro called "by construction", and it is short.

- A process g of the theory takes states on the first slice to states on the
  second. This is the reading forwards.
- Read backwards, the same region takes **effects** on the second slice to
  effects on the first: given a test to be performed at the end, it says which
  test that amounts to at the beginning. This reading always exists in a GPT —
  it is the transpose g^* — but it is a map between the *dual* systems, from
  effects to effects.
- Unitarity demands that the second reading be a process of the theory on the
  *same* systems, so that both readings live in the same category. That is only
  possible if each system is identified with its dual: an order isomorphism
  carrying the state cone onto the effect cone.

That identification is **self-duality**. In words:

> A state and an effect are two descriptions of the same thing — what is
> prepared on a slice, and what is tested for on that slice — and a theory that
> can be read from either end must not distinguish them.

Two things this does **not** say, and must not be written as saying:

- **It is not reversibility of the dynamics.** Reading a region backwards gives
  the transpose, not the inverse. In quantum theory the backwards reading of a
  channel is its Heisenberg-picture adjoint, which is a positive map and
  generally not a channel. Nothing here asks that a process can be undone.
- **It is not the absence of an arrow of time.** A GPT has one deterministic
  effect and many normalised states, and that asymmetry survives: the
  identification sends the unit effect to one distinguished state, which in the
  two-dimensional results is the unit of the Frobenius algebra [Result 1.6, and
  for OST forced to be a pole, Result 3.6]. Self-duality is a statement about
  the cones, not about normalisation.

And one thing to say precisely (checked 2026-09-11). The identification is a
**symmetric** order isomorphism of the state cone onto the **effect** cone. It
is not an inner product — quantum theory's own 2d form is tr(XYᵀ), of signature
(3, 1) for the qubit — and it is not "weak self-duality" in the glossary's
sense either, which compares the state cone with its *dual*, larger than the
effect cone when effects are restricted. Strong self-duality, a positive
definite form, is what the 2d *positivity* forces, not what unitarity assumes.
The three conditions and what turns on the difference:
`pipeline/tsirelson-from-self-duality-and-swapping.md` §1.

### 2.4 It is what the results already compute with

The reading is not decoration; it is what the two-dimensional results do.

- The Frobenius form of any GPT-valued 2d TFT "is a linear isomorphism of the
  state cone onto the effect cone" [Result 3, Lemma 2.1]. The form *is* the
  identification of states with effects, so the 2d test is a test of
  self-duality, and every theory that passes exhibits one.
- Quantum theory passes, and the identification it exhibits is the trace
  pairing twisted by transposition, β_Q(X, Y) = tr(XYᵀ) — symmetric, an
  isomorphism of the cones, and **indefinite**, of signature (3, 1) for the
  qubit [Result 1.7]. Not the Hilbert–Schmidt inner product, which is the
  theory's own strong self-duality and a different form.
- OST fails, and the reason is now a sentence of physics rather than a
  calculation: its states and its effects are the same shape, two octahedra, but
  **misaligned** — the effect cone is the state cone rotated. There is no
  alignment of the two that stays positive; any nonzero offset between the
  state and effect frames produces a negative entry, and "only strong
  self-duality escapes" [Result 3, Lemma 4.1, and 3.7, 3.8].

So the interpretation and the results say the same thing twice: the theory must
have one notion of what is on a slice, and OST has two that do not line up.

### 2.5 The positivity that comes for free

One structural remark, worth a line in the paper and no more. The TFT
literature imposes positivity by hand on top of the reversal, because its
target has no positivity of its own. A GPT target has: a closed spacetime is a
process from nothing to nothing, a probability, which cannot be negative. So in
this setting positivity is not a condition imposed on the theory — it is a
property of the target, and it therefore turns into an **obstruction**. That is
literally where the no-gos come from: the loop weights of Result 0.7
(tr(g) ≥ 0 for every process on a dualizable system, which kills the gbit and
the polygons) and the negative multiple of a state in the OST pants [Result
3.7] are both "a probability came out negative".

UNVERIFIED as stated: what has to be checked is that the positivity conditions
the literature imposes are implied by cone positivity in a GPT target, rather
than merely resembling it.

---

## Left out on purpose

Recorded so that the choice is visible, not because the argument needs them.
Pedro, 2026-09-11: the Euclidean route is not a detour the paper should take.

- **Reflection positivity.** The standard name for unitarity in this setting is
  reflection positivity, Wick-rotated unitarity, and Freed–Hopkins' framing is
  that "'reflection' is a structure whereas 'positivity' is a condition"
  [filed `160422`; toolbox T30]. §2.1 and §2.5 above say the same two things —
  the reversal is structure, the positivity is the target's — without
  Euclidean time. Keep the quote in the toolbox; keep it out of the draft.
- **The cobordism hypothesis.** "Fully local" theories are classified by fully
  dualisable objects, so at the top of that hierarchy locality and
  dualizability are the same word [Freed's summary, filed `140627`; T29]. It
  would strengthen §1.2 and it needs Lurie filed and an extended bordism
  category the project does not use. Not needed: CR Lemma 2.4 already makes
  §1.2 a theorem in the 1-categorical setting the paper works in.
- **Feynman–Stückelberg.** The bend of §1.3 is the familiar reading of a
  worldline that turns around in time. No filed source states it, T21 already
  flags the wording as unverified folklore, and §1.3 does not need the name.

## If we had a solution, what would it look like

Two paragraphs of the introduction, one per requirement, each stated in the
terms above before any formalism and each landing on a result:

1. A region of spacetime can be cut anywhere and reglued ⇒ the system on every
   slice is dualizable ⇒ boxworld and every ⊗_min/⊗_max theory with a
   non-classical system are excluded (Result 0).
2. A region can be read from either end ⇒ states and effects are the same
   objects ⇒ quantum and real quantum theory survive (Results 1, 2) and OST,
   whose states and effects are misaligned, does not (Result 3).

## Uncertainties

- Whether unitarity is an axiom or a consequence. If self-duality can be
  derived in the programme from something more primitive, the paper should
  derive it rather than assume it. The DECISION owed in `results-structure.md`
  is really this question. One filed result is relevant: bit symmetry — every
  logical bit can be mapped to any other by a reversible transformation —
  implies self-duality [Müller–Ududec, filed `111016`]. Its reading, that the
  dynamics does not distinguish one degree of freedom from another, is close to
  what "the same law everywhere" means for a theory distributed over space.
  UNVERIFIED as an interpretation; the theorem is theirs.
- Weak versus strong self-duality: settled 2026-09-11 (§2.3 and
  `tsirelson-from-self-duality-and-swapping.md` §1). Unitarity gives a
  symmetric cone isomorphism; strong self-duality is what the 2d positivity
  forces, proved only in the equatorial family [Result 3, Lemma 4.1]. Proving
  it in general is the open step, and it is also what would give Tsirelson's
  bound for theories stable under entanglement swapping.
- §2.5's claim that cone positivity supplies the positivity the literature
  imposes. Stated, not checked.
- Whether §1.2's three sentences are the right level of detail for the
  introduction or belong in the results section with the formalism.

## Sketch of a plan

1. Write the two paragraphs as candidate B8 prose in
   `syntheses/narratives/intro-narrative.md`, not in `draft.tex`.
2. Check the CR and BD quotations against the PDFs before either enters the
   draft.
3. Triage, in order of use: Barnum–Duncan–Wilce arXiv:1004.2920 (compact
   closure ⇔ teleportation and remote evaluation, for §1.4; dagger compactness
   ⇔ a symmetric bipartite state whose conditioning map is an isomorphism, for
   §2.3), then Tull arXiv:1907.05172, which states that dagger compactness
   "lacks a clear interpretation" and derives it from completely mixed states
   and purification — it fixes what is new in the reading above. Both are
   listed in `syntheses/literature-map.md`, quoted from abstracts only, NOT
   FILED.

## Open questions and disagreements

None recorded. The entry was written from Pedro's framing of 2026-09-11 and
rewritten the same day on his instruction to drop the Euclidean route and the
outside concepts.

## Judgement

For Pedro. Not filled by the agent.

**What would change if this worked?**

**Is the upper bound high enough?**

**What would make us less uncertain?**

## Sources

Filed and quoted: `170516` Carqueville–Runkel (Lemma 2.4, cutting and gluing;
T27); `950305` Baez–Dolan (the two reversals, and their independence; T28);
`080523` Barnum–Barrett–Leifer–Wilce (teleportation); `111016` Müller–Ududec
(bit symmetry ⇒ self-duality). Filed, kept out of the argument on purpose:
`160422` Freed–Hopkins (T30), `140627` Freed (T29).

Not filed, quoted from abstracts only and marked in the text: arXiv:1004.2920,
arXiv:1206.2897, arXiv:0912.5532, arXiv:1907.05172, Lurie.

Project: `paper/results-structure.md` (Results 0–3), `paper/draft.tex` (B3, B4),
`syntheses/toolbox/` (T1, T2, T7, T21, T22, T27, T28, C8, R3),
`conventions/domain/standing-assumptions.md` (A5, A6).
