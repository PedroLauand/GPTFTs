---
status: draft
last-reviewed: 2026-09-04
sources:
  - sources/papers/190408 - algebraic quantum field theory an introduction/paper.md
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/140514 - terminality implies non-signalling/paper.md
  - sources/papers/101130 - informational derivation of quantum theory/paper.md
  - paper/draft.tex
machine-written: true
---

# Toolbox: spacetime axioms and the two premises

What the cited AQFT axioms actually say (Fewster–Rejzner, FR, filed), how they
line up with the two premises of the retired B4 paragraph (standing assumption
A6), and one lesson that recurs across the filed sources: commutation gives
no-signalling, but independence needs a further assumption.

## The axioms as FR state them

FR §4.1, "the minimum requirements (more or less) of AQFT on Minkowski
spacetime M":

- **A1 Local algebras.** A unital *-algebra A(M) and, for each open causally
  convex bounded region O ⊂ M, a subalgebra A(O) containing the unit, the A(O)
  together generating A(M), the quasi-local algebra. Causally convex: contains
  every causal curve whose endpoints lie in it. Prototype: the double cone.
- **A2 Isotony.** O₁ ⊂ O₂ ⇒ A(O₁) ⊂ A(O₂).
- **A3 Einstein causality.** O₁, O₂ causally disjoint ⇒ [A(O₁), A(O₂)] = 0.
- **A4 Poincaré covariance.** Automorphisms α(ρ) with α(ρ) : A(O) → A(ρO) for
  ρ in the identity component of the Poincaré group, composing correctly.
- **A5 Existence of dynamics** (the time-slice axiom). If O₁ ⊂ O₂ and O₁
  contains a Cauchy surface of O₂, then A(O₂) = A(O₁). "Sometimes this
  condition is weakened."

FR's remark: "these are minimal requirements for AQFT but do not, by
themselves, suffice to distinguish a quantum field theory from other
relativistic models", and nothing has yet been said about Hilbert spaces. FR
§4.2 verifies A5 for the free scalar field through the Klein–Gordon dynamics:
any solution sourced in O₂ can be re-sourced inside O₁.

## Mapping to the premises of A6

| premise (retired B4) | axiom | what the axiom says |
|---|---|---|
| (i) degrees of freedom on spacelike separated regions are independent; systems compose in parallel | A3 | observables of causally disjoint regions commute. FR §7: this is "far from being the only way in which the two regions must be independent"; independent preparation is the split property, an extra condition |
| (ii) a local dynamical law propagates the degrees of freedom on a region to its causal development; systems compose in sequence | A5 | the algebra of a region equals that of any sub-region containing a Cauchy surface of it, i.e. of a region whose causal development it is |

Verdict on the UNVERIFIED line in A6: the split is FR's own. Premise (i) ↔ A3,
premise (ii) ↔ A5. Isotony (A2) and covariance (A4) have no counterpart in the
retired paragraph, and A1 fixes what a region is. TODO Pedro: whether isotony,
a region's degrees of freedom sitting inside a larger region's, is part of what
the paper means by premise (ii). StreaterWightman and HaagSchroer1962 remain
unfiled; FR is the modern statement.

## The recurring lesson: commutation is not independence

Three filed sources make the same point in three languages.

- **GPTs** [Barrett Assumptions 4 and 5, Corollary 1, §VIII]. Assumption 4,
  "local operations commute", gives Corollary 1, the no-signalling principle.
  The tensor product rule needs in addition Assumption 5, the global state
  assumption: the joint state is fixed by joint probabilities of local
  fiducial measurements. Barrett: Assumption 5 "has significant content"; it
  fails for quantum theory over a real Hilbert space.
- **AQFT** [FR §7]. Einstein causality is not enough for two laboratories to
  prepare independently. That is the split property: a type I factor between
  the local algebras, making M(O₁) ∨ M(O₃) a tensor product.
- **Process theories** [Coecke Def 3.1, 3.5, 4.2, Thm 5.1, 5.4]. Terminality,
  every process followed by discarding equals discarding, equivalently a unique
  deterministic effect per system, implies non-signalling of any two-party
  process once the causal structure is made explicit as a diamond. The converse
  needs the extra assumption that there is a unique closed diagram. Coecke
  separates three "causality" notions: the causal structure of spacetime (C1),
  spacelike non-signalling (C2), and the Chiribella–D'Ariano–Perinotti
  causality axiom, which is terminality, no signalling from the future (C3).

For the draft: the retired B4 sentence "the GPT tensor product is derived
precisely from the commutation of operations on separate systems (Barrett2007)"
is exact only with "together with the global state assumption" added. Logged
as a citation check with caveat in `syntheses/literature-map.md`.

## Time-like versus space-like

CDP's Axiom 1, Causality: "the probability of preparations is independent of
the choice of observations" [CDP §III], is, in Coecke's classification, no
signalling from the future. The draft's no-signalling (B3) is the space-like
notion. The paper's premise (ii) concerns time-like propagation, so the
CDP/terminality notion is the one B8 should compare it against. Coecke's
observation that spacelike separation is time-reversal invariant while
non-signalling is not [his ref. 10] is relevant to any claim that the dynamical
premise is "the other half" of the kinematic one. Machine-written reading;
UNVERIFIED.
