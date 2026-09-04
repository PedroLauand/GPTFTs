# Quotes bank

Verified against sources 2026-08-25. Companion to `References.md`; this file
collects verbatim quotes for the intro.

## Barrett, *Information processing in generalized probabilistic theories*,
quant-ph/0508211, Phys. Rev. A 75, 032304 (2007). All verified verbatim.

**B1 — the program (theory-independence).**
> "What we are really looking for is a better understanding of the connections
> between information processing and physical principles in general. Such an
> understanding could be gained by studying information processing in a broader
> range of theories than classical and quantum, where different physical
> principles may hold. For any theory, whether it applies to Nature or not, one
> can consider the information processing possibilities of this theory, the
> differences from those of classical or quantum theory, and attempt to trace
> these possibilities back to the fundamental features of the theory."
- Use: Topic 1/5. The GPT program stated by its founder: trace operational
  possibilities back to fundamental features. GPTFT is this program with
  "fundamental features" = spacetime's compositional premises.

**B2 — the framework.**
> "To make further progress along these lines, I introduce an operational
> framework for probabilistic theories in which a broad range of different
> theories can be defined."
- Use: Topic 5, when introducing GPTs as the target category.

**B3 — states as probability vectors.**
> "The basic idea is that a state is represented as a vector of probabilities of
> measurement outcomes. Transformations of a system must correspond to linear
> transformations of this vector."
- Use: §2 of notes (category of GPTs) — the "Vec + positivity" framing in
  Barrett's own words: linearity is forced, cones do the rest.

**B4 — the two composite assumptions.**
> "The first is that operations on the separate systems commute (this implies a
> no-signalling principle), and the second is that the state of the joint system
> can be completely specified by joint probabilities for local measurements.
> From these assumptions a tensor product rule can be derived. This removes at
> least some of the mystery from the quantum tensor product rule and generalizes
> a derivation by Fuchs."
- Use: Topic 5. KEY. Barrett's ⊗ is *derived from* commuting local operations
  (= independence of separated regions) + tomographic locality. So monoidality
  in the GPT target is already premise (i) in disguise — the parallel row of
  the dictionary was built into GPTs from day one. Our claim: the sequential
  row (gluing/functoriality) is the one never imported.

**B5 — generic vs specifically quantum.**
> "The resulting framework includes classical probabilistic theories, quantum
> theory, and many other theories besides. The first thing one notices is that
> certain phenomena, usually thought of as specifically quantum, are in fact
> generic. This means that they either appear in all theories, or they appear in
> all theories except classical theories, which emerge as a very special case."
- Use: Topic 1 or 5. Sets up our punchline in reverse: no-signaling-type
  premises make quantum phenomena generic; the *sequential* premise is where
  genericity breaks (boxworld admits no 1d GPTFT).

**B6 — the axiomatic motivation.**
> "The other motivation is to stimulate research into finding ways of deriving
> quantum theory from physical principles (instead of laying down a list of
> mathematical axioms, as per the standard textbook approach). What principles
> could be used to rule out the other theories described and leave only quantum
> theory?"
- Use: Topic 1. Barrett's open question is literally our question; we answer
  with a *spacetime* principle rather than an information-theoretic one.

## Gisin–Bancal–Cai–Remy–Tavakoli–Zambrini Cruzeiro–Popescu–Brunner,
*Constraints on nonlocality in networks from no-signaling and independence*,
arXiv:1906.06495, Nat. Commun. 11, 2378 (2020). Verified (intro, consecutive).

**G1 — no-signaling defined.**
> "The no-signalling principle states that instantaneous communication at a
> distance is impossible. This imposes constraints on the possible correlations
> between distant observers."

**G2 — weakest condition.**
> "These are the well-known no-signalling conditions, which represent the
> weakest conditions that correlations must satisfy in any 'reasonable'
> physical theory, in the sense of being compatible with relativity. More
> generally, the no-signalling principle ensures that information cannot be
> transmitted without any physical carrier. This provides a useful framework to
> investigate quantum correlations (which obviously satisfy the no-signalling
> conditions, but do not saturate them in general), within a larger set of
> physical theories satisfying no-signalling."
- Use: Topic 1. Community consensus phrasing (Popescu and Brunner among
  authors): no-signaling = "weakest" spacetime-compatibility condition. Our
  wedge: weakest for *correlations on a fixed slice* — it captures parallel
  composition only. The "physical carrier" clause is the field-theory hinge:
  the carrier IS the field (Topic 3, Einstein 1948).

## Coecke, *Terminality implies non-signalling*, arXiv:1405.3681. Verified
(intro, item C2 of his list C1–C3 of causality notions).

**C1 — non-signalling as the implementation of relativity.**
> "In quantum information, for example in the context of generalised
> probabilistic theories, one often relies on the notion of non-signalling, by
> means of which one intends to implement these relativistic constraints for
> spatially distributed information-processing devices."
- Use: Topic 2/5. States outright that non-signalling is how QI *implements
  relativistic constraints* in GPTs — i.e., the community treats one premise as
  if it were all of relativity. Context: his C1 = causal structure as partial
  order, C2 = non-signalling in GPTs, C3 = causality-as-terminality (CDP). His
  paper proves C3 ⇒ C2 (monoidal/terminal structure ⇒ no-signaling) — the
  categorical precedent for our "premise (i) = monoidality" row.

## How they slot into the chain

```
Topic 1 (the question):     B1, B6  — GPT program + "what rules theories out?"
Topic 1 (status quo):       G1, G2  — no-signaling = weakest relativity condition
Topic 2 (the gap):          C1      — non-signalling ≡ "the" relativistic constraint (only premise i!)
Topic 5 (mechanism):        B4      — ⊗ derived from commuting local ops; C1 context (terminality)
Topic 5 (punchline setup):  B5      — generic vs quantum; genericity breaks at premise (ii)
§2 of notes:                B2, B3  — framework, Vec + positivity
```
