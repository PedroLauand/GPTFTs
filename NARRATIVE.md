# Intro narrative — new foundation (2026-08-31)

Supersedes previous intro framings. Companion files: `References.md` (refs by
concept), `Quotes.md` (verbatim quote bank). Target: APS/RevTeX draft intro.

## The chain (9 beats)

**B1. Operational stance.**
Physics is accessible via probabilistic experiments: prepare, transform,
measure; the raw output of any lab is outcome statistics.
- Refs: Ludwig; D'Ariano–Chiribella–Perinotti book; Hardy quant-ph/0101012.
- Quote: Barrett B1 (the program).

**B2. GPTs/OPTs are the natural framework.**
The minimal mathematical home for lab-generated probabilities: states = vectors
of outcome probabilities, transformations forced linear, positivity does the
rest. Contains classical, quantum, and more.
- Refs: Barrett quant-ph/0508211; Müller 2011.01286; Plávala 2103.07469;
  CDP 1011.6451 (OPT variant).
- Quotes: B2, B3, B5.

**B3. Experiments happen in spacetime — the NS justification.**
Rehearse the *standard justification* of no-signaling: devices at spacelike
separation, relativistic causality forbids instantaneous influence, hence
marginals of one wing independent of the other's setting. IMPORTANT: we only
cite the justification, we do NOT claim NS is derived from relativity (Barrett's
footnote: kinematic NS holds in non-relativistic QM too).
- Refs: Popescu–Rohrlich 1994; Gisin et al. 1906.06495.
- Quotes: G1, G2.

**B4. The question.**
This prompts the natural question: *what does spacetime require of our
probabilities?*
- Quote: B6 (Barrett's "what principles rule theories out?" — ours is a
  spacetime principle, not an information-theoretic one).

**B5. Old idea; NS is the most famous instance.** *(CUT 2026-09-01 — B4 pivot
goes straight to B6; refinements material available here if a referee asks.)*
Connecting relativistic causality to probabilistic theories is an old program.
NS carves the polytope L ⊂ Q ⊂ NS; famously insufficient to single out quantum
(PR boxes), refined by information causality, macroscopic locality, almost
quantum — all still correlation-level, fixed-slice conditions.
- Refs: Barrett et al. quant-ph/0404097; Brunner et al. 1303.2849;
  Pawłowski 0905.2292; almost-quantum 1403.4621.
- Quote: C1 (community treats NS as "the" implementation of relativity).

**B6. But spacetime physics has been reconceptualized: field theory via RG.**
Over the same decades, the community's mature formalization of "physics
happening in spacetime" became *field theory* — and the modern justification is
not fundamentalist but generic: under a continuity assumption ("from far away,
discrete systems look continuous"), the renormalization group tells us
microscopic details wash out and long-distance physics flows to a continuum
field-theory description. Universality: the FT description is the generic
low-energy effective one, not a metaphysical commitment.
- Refs: Wilson RMP 1975 / Wilson–Kogut; Weinberg EFT folk theorem +
  hep-th/9702027; Polchinski EFT lectures. (Agent verifying exact IDs.)
- TONE: hedged, "provided such-and-such approximations hold." This is the
  weakest link in the chain — keep it a *motivation*, never load-bearing.

**B7. Low-energy limit ⇒ TFT.**
Add a second limit: low temperature / gapped spectrum. Finite correlation
length ⇒ the surviving long-distance sector is topological; folklore (with
known caveats) says gapped phases flow to TFTs. Structurally, TFT is the
skeleton of FT: Atiyah–Segal functoriality — assign data to space slices,
maps to spacetime cobordisms, gluing = locality of dynamics.
- Refs: Atiyah 1988; Segal; Witten CMP 117; Kitaev toric code; folklore ledger
  in References.md (Witten 9312104, Freed 1406.7278, Freed–Hopkins 1604.06527,
  Moore–Saxena 2510.07408 — cite the caveats!).
- Function: justifies TFT as the *right minimal model* of "dynamics in
  spacetime" for a structural question.

**B8. The new question (mirror of NS).**
In the same spirit as NS: *what does TFT-compatibility require of our
probabilistic theories?* Sharpen the mirror: NS constrains correlations on a
fixed slice — parallel composition only (Barrett's ⊗ already encodes it, quote
B4). TFT-compatibility constrains *sequential* composition — gluing,
functoriality — the premise never before imported into GPTs.
- Refs (prior-art gap): Oeckl 1610.09052; Gogioso et al. 2003.13271;
  References.md "Prior art" section — the composite claim is unclaimed.

**B9. `\[Declare results.\]`**
Red comment placeholder: `\textcolor{red}{[Declare results.]}`. Filled from
notes.tex §5–6 once results freeze (1d classification, boxworld no-go, 2d
frame/cone selection).

## Logical hygiene (constraints on the prose)

1. B3 and B6–B7 are *motivations by analogy of justification*, not derivations.
   One hedging clause each, stated once, not re-apologized.
2. The NS analogy is the load-bearing rhetorical device: old question =
   spacelike premise → NS; new question = full bordism premise → GPTFT. Land
   this in one sentence at B8.
3. Never claim "spacetime ⇒ TFT". Claim: "the community's own chain of
   approximations (continuity/RG, low energy) leads it to TFT; we take that
   endpoint as the premise."
4. Boxworld punchline held in reserve (B5 genericity vs. B8): quote B5 sets it
   up — quantum phenomena generic under parallel premises; genericity breaks at
   the sequential premise.

## Next step

Organize `draft.tex` (RevTeX 4.2, PRL-style two-column) with the intro written
from B1–B9, refs from References.md + agent results merged into a `.bib`.
