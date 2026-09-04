---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
machine-written: true
---

# General probabilistic theories

The framework the paper works in [B1+B2, approved 2026-08-31]: the natural
mathematical home for lab-generated probabilities, in which quantum theory is
"one theory among many others". The draft's framework references are
Barrett2007, Muller2021 and Plavala2023; its landscape references, placing
quantum theory among alternatives, are Hardy2001, CDP2011 and
MasanesMuller2011.

What the draft takes from the framework so far:

- systems compose in parallel, and the tensor product is derived from the
  requirement that operations on separate systems commute (Barrett2007) [B3;
  retired B4]. This is the point of contact with
  [no-signalling](no-signalling.md).

Nothing else about the framework (state spaces, effects, normalisation, the
choice of tensor product, the no-restriction hypothesis) is fixed in the draft.
Deliberately open; see "Things we have decided not to assume" in
`conventions/domain/standing-assumptions.md`.

## GPT versus OPT

The draft says GPT throughout. CDP2011 works in the operational probabilistic
theory framework of Chiribella, D'Ariano and Perinotti, which has sequential
composition built into its circuit language. UNVERIFIED until CDP2011 is filed,
and worth watching: the paper's own contribution concerns sequential
composition, so the difference between the frameworks may matter for B8.

## Related

- [operational-stance](operational-stance.md), why the framework
- [reconstructions-of-quantum-theory](reconstructions-of-quantum-theory.md)
- `conventions/domain/standing-assumptions.md`, A2
