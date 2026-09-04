---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
machine-written: true
---

# No-signalling

[B3 opening, approved 2026-09-01; new B4 opening, drafted 2026-09-01.]

The most famous physical principle in GPTs (PopescuRohrlich1994). The draft
characterises it three ways:

- **as a condition**: the weakest condition any "reasonable" physical theory
  must satisfy, in the sense of being compatible with special relativity
  (Gisin2020);
- **formally**: operations on separate systems commute (Barrett2007);
- **as compatibility**: devices at spacelike separated locations have
  correlations that respect relativistic causality, so no-signalling is "the
  compatibility of relativistic causality with the operational theory".

## What it uses from spacetime, and what it does not

The new B4 opening makes the paper's central observation. No-signalling takes
the *kinematical* picture of relativity: systems are points of spacetime, and
points at spacelike separation cannot instantaneously influence each other's
statistics. "The only feature of spacetime this invokes is the causal relation
between a pair of points." What it does not use is
[locality of action](locality-of-action.md): how influences propagate between
points that *are* causally connected.

The retired B4 paragraph makes the same point structurally: no-signalling
implements premise (i), independence of spacelike separated regions and hence
parallel composition, and nothing of premise (ii).

## Phrasing that must hold

Compatible with, justified by, in the sense of: yes. Derived from: no. The
approved B3 wording is careful about this, and `conventions/domain/rigour.md`
lists it first among the words that need care. UNVERIFIED until Barrett2007 is
filed: that Barrett notes no-signalling holds in non-relativistic quantum
theory too, which is why the stronger claim is false.

## Citation checks pending

- Gisin2020 for "weakest condition ... compatible with special relativity".
  The cited work is a network-nonlocality paper; whether it says this, or a
  better source exists, is open. Tracked in `syntheses/literature-map.md`.
- PopescuRohrlich1994 for "most famous physical principle in GPTs".

## Related

- [locality-of-action](locality-of-action.md)
- `conventions/domain/standing-assumptions.md`, A4
