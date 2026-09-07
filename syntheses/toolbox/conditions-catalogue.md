---
status: draft
last-reviewed: 2026-09-04
sources:
  - sources/papers/010103 - quantum theory from five reasonable axioms/paper.md
  - sources/papers/101130 - informational derivation of quantum theory/paper.md
  - sources/papers/100409 - derivation of quantum theory from physical requirements/paper.md
  - sources/papers/201102 - probabilistic theories and reconstructions of quantum theory/paper.md
  - sources/papers/050828 - information processing in generalized probabilistic theories/paper.md
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
  - sources/papers/140514 - terminality implies non-signalling/paper.md
machine-written: true
---

# Toolbox: conditions and principles

Conditions a GPT may or may not satisfy, as stated in the filed sources, so
that a discussion can point at a definition instead of rebuilding it. The
"status here" column: **in draft** means the draft uses it; **candidate** means
plausibly relevant to the programme but not in the draft; **context** means
background. Which theories satisfy a condition is given only where a filed
source says so. Toolbox labels G, T refer to `gpt-framework.md` and
`tft-framework.md`.

## A. Composition and locality

| condition | statement, with source | satisfied by | status here |
|---|---|---|---|
| No-signalling | operations on separate systems commute [B Assumption 4], hence marginals independent of the remote input [B Cor 1; M Lemma 18] | every GPT composite [M Lemma 18]: classical, quantum, boxworld | in draft (B3) |
| Tomographic locality (global state assumption; local tomography; local distinguishability) | joint states are determined by joint statistics of local measurements [B Assumption 5; M after Def 14, attributing to Hardy 2001; MM Req 2; CDP Axiom 4; P (BP5)] | classical, quantum; fails for real-Hilbert-space QT [B after Assumption 5] | candidate; built into P's framework |
| Terminality / causality | every process followed by discarding equals discarding; one deterministic effect per system [Coecke Def 3.1, Prop 3.2]; CDP Axiom 1: "the probability of preparations is independent of the choice of observations" | classical, quantum [Coecke Ex 2.3, 2.4, 3.4]; equivalent to two-party non-signalling given explicit causal structure [Coecke Thm 5.1, 5.4] | candidate for premise (ii): it is the time-like notion |
| Product preparations | x_A ⊗ x_B is a state [B Assumption 6; P (BP2)] | all | context |
| Choice of composite | some ⊗̃ with ⊗̇ ⊆ ⊗̃ ⊆ ⊗̂ [G12] | ⊗̇ = ⊗̂ iff a factor is classical [P Thm 5.21] | candidate: the paper must pick or derive one |
| Purification | every state has a purification, unique up to a reversible transformation on the purifying system [CDP Postulate 1] | quantum; CDP: "the ignorance about a part is always compatible with a maximal knowledge of the whole" | context |

## B. Single-system structure

| condition | statement, with source | satisfied by | status here |
|---|---|---|---|
| Perfect distinguishability | every state that is not completely mixed is perfectly distinguishable from some state [CDP Axiom 2; MM Req 5′] | quantum, classical [CDP] | context |
| Ideal compression | every state has an ideal compression scheme [CDP Axiom 3] | quantum, classical [CDP] | context |
| Pure conditioning | an atomic measurement on one side of a pure bipartite state induces pure states on the other [CDP Axiom 5] | quantum; classical trivially [CDP] | context |
| Subspace axiom / equivalence of subspaces | a system constrained to an M-dimensional subspace behaves like a system of dimension M [Hardy Axiom 3; MM Req 3; M Thm 21] | quantum, classical | context |
| Continuity / continuous reversibility | a continuous reversible transformation between any two pure states [Hardy Axiom 5; M Thm 21] | quantum; not classical: dropping "continuous" yields classical probability theory [Hardy abstract] | context |
| Symmetry (transitivity on pure states) | for every pair of pure states a reversible transformation maps one to the other [MM Req 4] | quantum, classical | candidate; the ancestor of "strong symmetry" |
| Simplicity | K = K(N) takes the minimal value consistent with the axioms [Hardy Axiom 2] | | context |
| Finiteness | a capacity-2 system has finite dimension [MM Req 1] | | context |
| Composite systems (Hardy) | N = N_A N_B and K = K_A K_B [Hardy Axiom 4] | | context |
| All measurements allowed / no-restriction | all effects on the generalised bit are outcome probabilities of measurements [MM Req 5]; every f ∈ E(K) performable [P §3.7, G7] | quantum [P §8.2], classical | candidate; deliberately not assumed |
| Spectrality and strong symmetry | Barnum–Hilgert 2019 derive quantum theory from these two single-system postulates, improving on Barnum et al. 2014 [M §5] | | candidate; the work is not in the bib and not filed, and the definitions are not in any filed source: UNVERIFIED here |

## C. The reconstructions in one table

| work | principles | result |
|---|---|---|
| Hardy2001 | Axioms 1–5: probabilities, simplicity, subspaces, composite systems, continuity | quantum theory; drop continuity, classical probability theory |
| CDP2011 | Axioms 1–5: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning; plus purification | quantum theory, in the operational-probabilistic (circuit) framework [CDP §II] |
| MasanesMuller2011 | Requirements 1–5: finiteness, local tomography, equivalence of subspaces, symmetry, all measurements allowed | "the only possibilities are CPT and QT" [MM §I summary] |
| Muller2021, Thm 21 | tomographic locality, subspace axiom, continuous reversibility | the quantum state spaces, capacity by capacity |
| Barnum–Hilgert 2019, via M §5 | spectrality, strong symmetry (single system) | quantum theory [M]; unfiled |

Every reconstruction in the table uses a composition principle of the
tomographic-locality kind or a single-system symmetry; none uses a spacetime
principle beyond no-signalling. That is the gap B3's question names. Note that
MM's abstract states the special-relativity analogy the draft uses in B2b
almost word for word; see the literature map.

## D. Beyond-quantum correlations (context for B3 and B8)

From M §2.1: C ⊂ Q ⊂ NS for the (2,2,2) Bell scenario; the PR box saturates
CHSH at 4 against the quantum 2√2; principles that cut the no-signalling set
down towards the quantum set include trivial communication complexity (van
Dam), information causality (Pawłowski et al. 2009, Pawlowski2009 in the bib,
unfiled) and an ill-defined classical limit (Navascués–Wunderlich). Almost
quantum (Navascues2015 in the bib, unfiled). None is a spacetime principle
beyond no-signalling.

Structural axioms (self-duality, spectrality, strong symmetry, cups and caps,
teleportation) are catalogued separately in `gpt-axioms.md` (X1–X22), with the
examples table in `gpt-examples.md`.

## E. For discussion: what a locality-of-action principle would have to be

Checklist derived from the above. Machine-written; a proposal for the
discussion, not a result.

1. Stated on a GPT together with a composition rule (A). The rule itself may be
   what the principle selects (G12, G16).
2. About sequential, time-like structure. Compare it against terminality and
   CDP causality (Coecke's C3), not against no-signalling (C2).
3. Not already a consequence of no-signalling plus tomographic locality
   (standing assumption A5, drop-if).
4. Testable on the three standard examples (G19–G21). Boxworld's dynamics is
   essentially relabellings [B], so a principle asking for rich local dynamics
   may exclude it outright; that would be a result of the kind B9 needs.
5. If the principle is the existence of a TFT valued in GPT systems (T7), it
   demands duals (T3), which the GPT framework does not supply by default. The
   question of which GPT systems are dualisable is then the first technical
   question. UNVERIFIED that this is the paper's route.
