# References by concept

Extracted from the retired Narrative.md (quotes verified against sources, 2026-08).
Quote bank with verbatim excerpts: `Quotes.md`.
Sections marked (2026-08-31) added for the NARRATIVE.md intro chain, verified by
web search against publisher/arXiv pages.

## Operational foundations primers (2026-08-31, for B1)

- Ludwig, *Foundations of Quantum Mechanics I* (Springer 1983); also *An
  Axiomatic Basis for QM* I–II (1985/87) — original preparation–registration
  operational axiomatics.
- Davies–Lewis, CMP 17, 239 (1970) — instruments/operations formalism.
- Chiribella–D'Ariano–Perinotti, PRA 81, 062348 (2010), arXiv:0908.1583 — OPT
  framework + purification.
- D'Ariano–Chiribella–Perinotti, *Quantum Theory from First Principles* (CUP
  2017) — textbook of the informational reconstruction program.
- Janotta–Hinrichsen, J. Phys. A 47, 323001 (2014), arXiv:1402.6562 — standard
  accessible GPT review. (No joint Hardy–Spekkens GPT review exists.)
- Mackey (1963), Gudder — NOT web-verified; cite only if depth needed.

## RG / continuum limit / universality (2026-08-31, for B6)

- Kadanoff, Physics 2, 263 (1966) — block-spin coarse-graining origin.
- Wilson–Kogut, Phys. Rep. 12, 75 (1974) — canonical technical RG.
- Wilson, RMP 47, 773 (1975) — RG review; universality/fixed-point picture.
- Weinberg, Physica A 96, 327 (1979) — EFT "folk theorem" source.
- Polchinski, hep-th/9210046 (TASI 1992) — "generic low-energy physics is EFT".
- Cardy, *Scaling and Renormalization in Statistical Physics* (CUP 1996) —
  textbook discrete→continuum via RG.

## Gapped phases → TQFT (2026-08-31, for B7; complements folklore ledger below)

- Kitaev, Ann. Phys. 303, 2 (2003), quant-ph/9707021 — toric code, lattice TQFT.
- Levin–Wen, PRB 71, 045110 (2005), cond-mat/0404617 — string-nets, fixed-point
  Hamiltonians for Turaev–Viro TQFTs.
- Witten, CMP 121, 351 (1989) — Jones polynomial / Chern–Simons. NOTE: distinct
  from CMP 117 (1988) Donaldson paper already cited.
- Nayak–Simon–Stern–Freedman–Das Sarma, RMP 80, 1083 (2008), arXiv:0707.1889 —
  anyons/TQC review.
- Wen, RMP 89, 041004 (2017), arXiv:1610.03911 — modern topological-order zoo.

## Spacetime/causality ↔ GPTs beyond no-signaling (2026-08-31, for B5/B8 prior art)

- Hardy, gr-qc/0509120 — causaloid; operational probability with dynamic causal
  structure.
- Kent, PRA 72, 012107 (2005), quant-ph/0204104 — causal quantum theory.
- Horodecki–Ramanathan, Nat. Commun. 10, 1701 (2019), arXiv:1611.06781 —
  multipartite NS strictly stronger than relativistic causality.
- Vilasini–Colbeck, arXiv:2311.18465 — NS neither sufficient nor necessary for
  preventing superluminal signaling with general interventions. (Authorship
  soft-verified — double-check before submission.)
- Weilenmann–Colbeck, Quantum 4, 236 (2020), arXiv:1812.04327 — causal
  structures inside GPTs.
- Galley–Giacomini–Selby, Quantum 6, 779 (2022), arXiv:2012.01441 — GPT no-go
  on gravity; closest recent "spacetime constrains GPTs".
- Müller–Masanes, NJP 15, 053040 (2013), arXiv:1206.0630 — 3d space ↔ qubit
  state space.
- No standalone "principle of general tomographic locality" paper exists;
  source is Hardy quant-ph/0101012 axiom 4.

## TFT-for-physicists texts (2026-08-31)

- Carqueville–Runkel, arXiv:1705.05734, Banach Center Publ. 114, 9 (2018) —
  physicist-friendly functorial TQFT lectures.
- Kock, *Frobenius Algebras and 2D TQFTs* (LMS Student Texts 59, CUP 2003) —
  canonical 2d TQFT ≅ commutative Frobenius algebras.

## GPT framework

- Hardy, quant-ph/0101012 — operational axioms for QM, origin of the framework.
- Barrett, quant-ph/0508211, PRA 75, 032304 (2007) — GPT framework proper; ⊗ derived
  from commuting local operations + tomographic locality; Corollary 1: no-signaling
  from "local operations commute"; footnote: kinematic no-signaling holds even in
  non-relativistic QM (distinct from relativity). Quotes B1–B6 in Quotes.md.
- Müller, arXiv:2011.01286 — review; Lemma 18: composites "automatically satisfy the
  no-signalling principle"; reduced states ω_A = (id ⊗ u_B)(ω_AB).
- Plávala, arXiv:2103.07469 — review, base for notes.tex conventions.

## No-signaling

- Popescu–Rohrlich, Found. Phys. 24, 379 (1994) + quant-ph/9508009 — no-signaling
  ("relativistic causality") as axiom; "making nonlocality an axiom and
  indeterminism a theorem."
- Barrett–Linden–Massar–Pironio–Popescu–Roberts, quant-ph/0404097 — no-signaling
  polytope; L ⊂ Q ⊂ P.
- Brunner et al., arXiv:1303.2849 — review; "first natural limitation on behaviors."
- Barrett–Hardy–Kent, quant-ph/0405101 — DI crypto from no-signaling alone.
- Colbeck–Renner, arXiv:1105.3195 — no-signaling "necessary for the existence of
  free randomness."
- Gallego et al., arXiv:1210.6514 — "minimal possible assumptions."
- Gisin et al., arXiv:1906.06495 — no-signaling = "weakest conditions ... compatible
  with relativity"; quotes G1–G2.
- Insufficiency: Pawłowski et al. (Information Causality), arXiv:0905.2292; almost-
  quantum set, arXiv:1403.4621.

## Spacetime causal axioms (AQFT)

- Microcausality / Einstein causality (premise i):
  - Streater–Wightman — Wightman axiom W3 (local commutativity).
  - Fewster–Rejzner, arXiv:1904.04051 — axiom A3 (causally disjoint ⇒ commute);
    also A5 (existence of dynamics).
  - Einstein, Dialectica 2 (1948) 320 — "principle of local action" [Prinzip der
    Nahewirkung]; passage Bell quotes in "La nouvelle cuisine."
  - Calderón, arXiv:2401.06504 — names as synonyms; axiom = "condition of
    independence or separability"; groups AQFT's "causal axioms."
- Primitive causality / time-slice (premise ii):
  - Haag–Schroer, J. Math. Phys. 3 (1962) 248 — origin; PROOF it is independent of
    causal commutation relations (generalized free field, continuous mass spectrum).
  - Haag, Local Quantum Physics, p. 48 — time-slice axiom.
  - Brunetti–Fredenhagen–Verch, math-ph/0112041 — Def. 2.1(iii), "strong Einstein
    causality, or existence of a causal dynamical law."
  - Chilian–Fredenhagen, arXiv:0802.1642 — small-interval observables predict all.
  - Earman–Valente — no-superluminal-propagation lives in primitive causality, not
    microcausality.

## Field theory & locality

- Einstein, Dialectica 1948 — local action "used consistently only in field theory."
- Feynman Lectures II-1-2 — field = "any physical quantity which takes on different
  values at different points in space."
- Einstein–Infeld, The Evolution of Physics (1938) — field "essential for the
  description of physical phenomena." CAUTION: "the field is the only reality" is a
  distorted aphorism; quote only the book's conditional form.
- Weinberg, hep-th/9702027 — QFT as the only way to combine Lorentz + QM + cluster
  decomposition (his own "folk theorem" hedge).

## Functorial field theory / TFT

- Segal — sewing axiom.
- Atiyah, Publ. Math. IHÉS 68 (1988) 175 — TFT axioms; topological understanding
  "may well be ... a necessary pre-requisite."
- Stolz–Teichner, arXiv:1108.0189 — field theory = functor on bordisms with
  geometric structure; TFT = structure-free case.
- Lurie, arXiv:0905.0465 — Prop. 1.1.8, duals from bare functoriality ("completely
  formal").
- Freed, arXiv:0808.2507 — TQFT as insight into "the formal structure of all
  quantum field theories"; arXiv:1210.5100, p. 12 — "the Hamiltonian vanishes ...
  no local evolution."
- Witten, CMP 117 (1988) — "no gravitons, only excitations are topological."
- Gapped-⇒-TFT folklore (motivation only, never load-bearing): Witten,
  hep-th/9312104 §4 (origin); Freed, arXiv:1406.7278 ("truism"); Freed–Hopkins,
  arXiv:1604.06527 ("heuristic principle"); Moore–Saxena, arXiv:2510.07408
  ("folklore ... counterexamples": fractons, invertible non-topological factors).

## Categorical causality (monoidality = no-signaling)

- Coecke, arXiv:1405.3681 — "causality boils down to terminality of the tensor
  unit"; proves terminality ⇒ non-signalling; quote C1.
- Coecke–Lal, arXiv:1107.6019 — causal categories.
- Chiribella–D'Ariano–Perinotti, arXiv:1011.6451 — causality = unique deterministic
  effect.
- Brunetti–Fredenhagen–Imani–Rejzner, arXiv:1206.5484 — AQFT: causality axiom ⇔
  tensorial property of the functor on disconnected spacetimes.
- Baez, quant-ph/0404040 — ⊗ = "running in parallel"; noncartesianness ⇒ no-cloning.

## Prior art (the gap)

- Oeckl, arXiv:1610.09052 — positive formalism; ordered vector spaces on
  hypersurfaces; not monoidal functoriality.
- Gogioso–Stasinou–Coecke, arXiv:2003.13271 — functorial, theory-independent, but
  over causal orders, not bordisms.
- No hit for "TFT valued in GPTs/convex cones": the composite claim (⊗ =
  no-signaling, gluing = locality, target = GPT) is unclaimed.
