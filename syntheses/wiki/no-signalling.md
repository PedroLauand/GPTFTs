---
status: draft
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/190615 - nonlocality in networks from no-signalling and independence/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/140514 - terminality implies non-signalling/paper.md
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

## What the filed sources say

- Barrett, Assumption 4 "Local Operations Commute", yields Corollary 1 "The
  No-Signalling Principle": an operation on A cannot be detected by measuring
  B. The footnote to Assumption 4 separates the principle from the impossibility
  of superluminal signalling, "a contingent fact": "in the non-relativistic
  quantum mechanics of particles, the no-signalling principle is valid, yet
  super-luminal signalling is possible", and Barrett uses no "notion of
  spacetime structure". §VIII: in a spacetime framework commutativity "can be
  independently motivated by special relativity".
- Müller, Lemma 18: every GPT composite built from local effects and a joint
  state satisfies the no-signalling conditions, because the effects of a
  measurement sum to the unit. So in the framework it is a theorem, not an
  axiom.
- Gisin et al., introduction: the no-signalling conditions "represent the
  weakest conditions that correlations must satisfy in any 'reasonable'
  physical theory [2], in the sense of being compatible with relativity", [2]
  being PopescuRohrlich1994.
- Coecke: for two parties with explicit causal structure, no-signalling is
  equivalent to terminality (a unique deterministic effect per system), and is
  the space-like notion, as opposed to CDP's causality axiom, which is no
  signalling from the future. See `syntheses/toolbox/spacetime-axioms.md`.

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
parallel composition, and nothing of premise (ii). Barrett's Assumption 5 (the
global state assumption) is what turns commutation into the tensor product, and
it is a separate assumption; see the toolbox.

## Phrasing that must hold

Compatible with, justified by, in the sense of: yes. Derived from: no. The
approved B3 wording is careful about this, and `conventions/domain/rigour.md`
lists it first among the words that need care. The footnote in Barrett quoted
above is the source for why the stronger claim is false.

## Citation checks

Done 2026-09-04; details in `syntheses/literature-map.md`.

- Gisin2020: supported, near-verbatim. The B3 sentence should be quoted or
  rephrased, and could cite PopescuRohrlich1994 directly as Gisin et al. do.
  They say "relativity", the draft says "special relativity".
- PopescuRohrlich1994: partial. The 1994 text has no open copy; its content is
  confirmed through Müller §2.1, Gisin et al., and the filed 1995 restatement.
- Barrett2007: supported.

## Related

- [locality-of-action](locality-of-action.md)
- `conventions/domain/standing-assumptions.md`, A4
- `syntheses/toolbox/gpt-framework.md`, G11–G13
