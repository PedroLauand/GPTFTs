---
status: workup           # entry | workup | proposed | project
created: 2026-09-04
entered-by: agent, from paper/draft.tex (retired B4 paragraph), on Pedro's instruction
last-reviewed: 2026-09-04
feeds: B8, B9
machine-written: true
---

# Sequential composition as a GPT principle

## The paragraph

No-signalling gives GPTs their parallel composition: operations on separate
systems commute, and the tensor product follows (Barrett2007). Locality of
action should give them a sequential composition: a local dynamical law that
propagates the degrees of freedom on a region to its causal development. State
this as a principle on a GPT, in operational terms as plain as no-signalling's,
and work out what structure it forces. The working title says the answer takes
the form of a topological field theory. [Source: the retired B4 paragraph of
`paper/draft.tex`, and the title.]

## The problem

We cannot currently say, in GPT terms, what it means for a theory's degrees of
freedom to be distributed over spacetime and to evolve by a local dynamical
law. The framework has parallel composition and nothing else from spacetime.

## Why bother

Every reconstruction so far selects quantum theory with information-theoretic
principles [B2b]. The draft's question [B3] is whether spacetime compatibility
supplies principles of its own beyond no-signalling. If it does, that is a new
kind of axiom for the reconstruction programme. If it does not, that is worth
knowing too.

## Current approaches, and why we expect them to fail

- **No-signalling alone.** Implements premise (i) only [retired B4]. Says
  nothing about causally connected points.
- **Circuit frameworks (OPTs, CDP2011).** Have sequential composition as a
  primitive of the circuit language, but the wires are not regions of spacetime
  and no dynamical law is asked for. Checked against the filed CDP2011: the
  framework is circuits with outcomes [CDP §II]; its Causality axiom is no
  signalling from the future [CDP Axiom 1; Coecke C3], not a spacetime law.
- **Algebraic QFT (StreaterWightman, HaagSchroer1962, FewsterRejzner2019).**
  Has both premises, but assumes quantum theory from the start. Checked
  against the filed FewsterRejzner2019: premise (i) is Einstein causality A3,
  premise (ii) the time-slice axiom A5; the local algebras are *-algebras of
  observables, quantum from the start. See
  `syntheses/toolbox/spacetime-axioms.md`.
- **The B8 prior-art group** (Oeckl2019, Gogioso2021, Coecke2014,
  HorodeckiRamanathan2019, WeilenmannColbeck2020). Each puts some of spacetime
  into an operational framework. TODO: for each, what it assumes, what it
  delivers, and why it does not answer this question. See
  `prior-art-on-spacetime-in-gpts.md`.

## If we had a solution, what would it look like

A principle stated on a GPT, and a theorem of the form: a GPT satisfying
no-signalling and this principle has such-and-such structure. TODO Pedro:
whether the structure is "a TFT valued in GPT systems and processes", and
whether the theorem selects quantum theory or characterises a class (standing
assumption A3). UNVERIFIED either way; B7 to B9 are placeholders.

## Candidate formalisation (agent proposal, 2026-09-04)

A symmetric monoidal functor from a bordism category to a symmetric monoidal
category of GPT systems and processes (toolbox T2, T7). Premise (i) is the
monoidal structure, premise (ii) is functoriality under gluing (T2). T3 then
forces every system in the image to be finite-dimensional and dual to its
orientation reverse, which no GPT framework supplies by default (G5, and the
last section of `syntheses/toolbox/gpt-framework.md`). Whether this is the
paper's route is for Pedro; nothing in the draft says so.

## How would we know we'd solved it

- The principle is operational: stated in terms of preparations,
  transformations and measurements on regions of spacetime.
- Quantum theory satisfies it, and the way it does recovers something known.
- It has teeth: some GPT fails it, or some structure is forced that
  no-signalling alone does not force.

## Uncertainties

- The premise is not already implied by no-signalling plus the standard GPT
  axioms (standing assumption A5, drop-if).
- The parallel/sequential split is the right decomposition of locality of
  action (A6, drop-if).
- The RG and gapped-limit steps that turn "local dynamical law" into
  "topological field theory" transfer to GPTs (A7; see
  `field-theory-genericity-for-gpts.md`).

## Sketch of a plan

1. File the B8 prior-art works and the three AQFT references; read them
   against the two premises.
2. Write the B6 and B7 arguments, or find that they need a different route.
3. TODO Pedro: the technical statement of the principle and the result.

## Open questions and disagreements

None recorded. The item was created from the draft, not from a discussion.

## Judgement

For Pedro. Not filled by the agent.

**What would change if this worked?**

**Is the upper bound high enough?**

**What would make us less uncertain?**

## Sources

- `paper/draft.tex`: B3 (approved 2026-09-01), new B4 opening (drafted
  2026-09-01), retired B4 paragraph, title.
- Nothing filed in `sources/` yet.
