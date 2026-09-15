---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
  - sources/papers/190408 - algebraic quantum field theory an introduction/paper.md
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/480000 - quanten-mechanik und wirklichkeit/source.md
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
the project's; standing assumption A6 holds it. Checked 2026-09-04 against the
filed Fewster–Rejzner: the split is theirs. Premise (i) is Einstein causality
(their A3, algebras of causally disjoint regions commute); premise (ii) is the
time-slice axiom (their A5, "existence of dynamics": the algebra of a region
equals that of a sub-region containing a Cauchy surface of it). Isotony and
covariance have no counterpart in the paragraph. Details and the recurring
lesson that commutation is not independence: `syntheses/toolbox/spacetime-axioms.md`.

## From locality of action to field theory to topology

The retired paragraph also carried the step the introduction still has to
make: the degrees of freedom of modern spacetime physics are *fields*, and the
field description is generic because of the renormalisation group
(WilsonKogut1974, Wilson1975, WeinbergEFT, Polchinski1992). B6 is to argue
this; B7 is to argue that the gapped, low-energy limit is topological, with the
Atiyah–Segal skeleton. Neither is written. See
[topological-field-theory](topological-field-theory.md) and
`pipeline/field-theory-genericity-for-gpts.md`.

## Citation check: Einstein1948

Partial support (2026-09-04; translation unverified). The sentence usually
quoted from the Dialectica paper reads: "external influence on A has no direct
influence on B; this is known as the Principle of Local Action, which is used
consistently only in field theory." That is a statement of the independence of
distant objects, the kinematic content, plus the remark that only field theory
implements it consistently. The dynamical reading in B4 (propagation between
causally connected points by a dynamical law) is what field theory adds, not
what Einstein's sentence says. Either B4 cites Einstein for the field-theory
remark and states the dynamical half in its own voice, or a different source
carries it. Stub with provenance:
`sources/papers/480000 - quanten-mechanik und wirklichkeit/source.md`.

## Related

- [no-signalling](no-signalling.md)
- `conventions/domain/standing-assumptions.md`, A5, A6, A7
- `pipeline/sequential-composition-as-a-gpt-principle.md`
- `syntheses/toolbox/spacetime-axioms.md`
