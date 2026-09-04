---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
  - sources/papers/101130 - informational derivation of quantum theory/paper.md
machine-written: true
---

# General probabilistic theories

The framework the paper works in [B1+B2, approved 2026-08-31]: the natural
mathematical home for lab-generated probabilities, in which quantum theory is
"one theory among many others". The draft's framework references are
Barrett2007, Muller2021 and Plavala2023, all filed; its landscape references,
placing quantum theory among alternatives, are Hardy2001, CDP2011 and
MasanesMuller2011, all filed.

The definitions are in `syntheses/toolbox/gpt-framework.md` (G1–G21), with a
table translating between the three framework references' presentations:
Plávala's compact convex set with its effect algebra, Müller's (A, Ω_A, u_A)
with state cone, Barrett's fiducial probability vectors.

What the draft takes from the framework so far:

- systems compose in parallel, and the tensor product is derived from the
  requirement that operations on separate systems commute (Barrett2007) [B3;
  retired B4]. Checked: Barrett needs the global state assumption as well
  (Assumption 5); commutation alone gives no-signalling (Corollary 1) but not
  the tensor product. This is the point of contact with
  [no-signalling](no-signalling.md).

Not fixed in the draft, deliberately: the presentation (state-space-first or
cone-first, G1 versus G5), the composition rule (G12: infinitely many
composites lie between the minimal and maximal tensor products), the
no-restriction hypothesis (G7), duals. See "Things we have decided not to
assume" in `conventions/domain/standing-assumptions.md`.

## GPT versus OPT

The draft says GPT throughout. CDP2011 works in "the framework of
operational-probabilistic theories" [CDP §II], circuits with outcomes, in which
sequential composition is a primitive of the language and the first axiom,
causality, is no signalling from the future (Coecke's reading). Checked against
the filed paper on 2026-09-04. Worth watching: the paper's own contribution
concerns sequential composition, so the difference between the frameworks
matters for B8 and for the choice of target category in
`syntheses/toolbox/tft-framework.md` (T7).

## Related

- [operational-stance](operational-stance.md), why the framework
- [reconstructions-of-quantum-theory](reconstructions-of-quantum-theory.md)
- `conventions/domain/standing-assumptions.md`, A2
- `syntheses/toolbox/conditions-catalogue.md`
