---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
machine-written: true
---

# Locality of action

[New B4 opening, drafted 2026-09-01, awaiting approval; retired B4 paragraph
for the structural version.]

"Another crucial feature of spacetime physics is the *locality of action*
(Einstein1948): between points that *are* causally connected, influences
propagate locally through spacetime, by a dynamical law." This is the premise
the paper imports into the GPT framework. [No-signalling](no-signalling.md)
never uses it.

## The structural version: two composition premises

The retired B4 paragraph says what changes once a GPT's degrees of freedom are
distributed over spacetime. Two independent premises arise, mirroring the
causal axioms of algebraic quantum field theory (StreaterWightman,
HaagSchroer1962, FewsterRejzner2019):

1. degrees of freedom on spacelike separated regions are independent, so
   systems compose in **parallel**;
2. a local dynamical law propagates the degrees of freedom on a region to its
   causal development, so systems compose in **sequence**.

No-signalling implements (i) alone: the GPT tensor product is derived from
commuting operations on separate systems (Barrett2007). Premise (ii) "has never
been imported into the GPT framework; it is the premise from which our
principles follow."

The paragraph is out of the introduction since 2026-09-01. The logic is still
the project's; standing assumption A6 holds it. UNVERIFIED: that the cited AQFT
axioms split along this line. Check when the sources are filed.

## From locality of action to field theory to topology

The retired paragraph also carried the step the introduction still has to
make: the degrees of freedom of modern spacetime physics are *fields*, and the
field description is generic because of the renormalisation group
(WilsonKogut1974, Wilson1975, WeinbergEFT, Polchinski1992). B6 is to argue
this; B7 is to argue that the gapped, low-energy limit is topological, with the
Atiyah–Segal skeleton. Neither is written. See
[topological-field-theory](topological-field-theory.md) and
`pipeline/field-theory-genericity-for-gpts.md`.

## Citation check pending

Einstein1948 is the Dialectica paper "Quanten-Mechanik und Wirklichkeit", in
German. Any quotation needs the original and a sourced translation. UNVERIFIED
that it is the best citation for the principle as the draft states it.

## Related

- [no-signalling](no-signalling.md)
- `conventions/domain/standing-assumptions.md`, A5, A6, A7
- `pipeline/sequential-composition-as-a-gpt-principle.md`
