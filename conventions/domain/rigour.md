# What counts as an argument here

The standard a claim has to meet, by where it lives.

## In the draft (`paper/draft.tex`)

A sentence enters an approved beat only with Pedro's approval, recorded with
the date in the `%` comment above the block. A citation must exist in
`draft.bib` and must support the sentence it is attached to, checked against
the filed source in `sources/papers/`. Until that check is done it is listed as
pending in `syntheses/literature-map.md`. A quotation is verbatim from the
filed source or it does not go in.

## In `syntheses/`

A claim needs a source, a derivation, or an explicit label saying it is
neither.

Acceptable: "Following [source], X holds when Y."
Acceptable: "The draft says X [B3]."
Acceptable: "UNVERIFIED: this seems to imply X; nobody has checked."
Not acceptable: "X holds" with nothing attached.

## In `pipeline/`

Speculation is welcome. Mark the uncertainty rather than avoiding the claim.

## Words and phrases that need care

- **"derived from relativity."** No-signalling is *compatible with* special
  relativity, and its usual *justification* is relativistic causality. It is
  not derived from relativity: it is formulated without spacetime (commuting
  operations), and it holds in non-relativistic quantum theory (UNVERIFIED
  until Barrett2007 is filed: the draft's narrative relied on a footnote there).
  Write "compatible with", "in the sense of", "justified by". Never "derived
  from" or "follows from". The approved B3 wording depends on this.
- **"GPT" versus "OPT".** Barrett-style GPTs (convex state spaces, tensor
  product from commuting operations) and Chiribella–D'Ariano–Perinotti
  operational probabilistic theories (circuits, purification) are different
  frameworks that overlap. The draft says GPT throughout and cites OPT work as
  landscape references. When the difference matters, say which.
- **"principle" versus "postulate".** The draft uses "principle" for a
  physically motivated requirement and "postulate" for the textbook
  Hilbert-space stipulations. Keep that.
- **"locality."** Two things. Kinematic: no influence between spacelike
  separated points. Dynamical: locality of action, influence propagating
  locally between causally connected points. The paper's point is the
  difference. Always say which.
- **"topological."** TFT means the Atiyah–Segal functorial structure of the
  gapped low-energy limit, not topology in any looser sense.
- **"reconstruction" versus "classification."** Selecting quantum theory
  uniquely, versus characterising a class. Which the results deliver is open
  (standing assumption A3).
- **"implies", "equivalent", "generalises".** Only with a derivation or a
  citation attached.

## For agents specifically

Do not smooth over a gap. If two sources disagree, say so rather than picking
the more recent. If a step is missing, write `TODO:` and leave it visible. If
a sentence in the draft rests on a citation that has not been checked, say so
in the synthesis, not by editing the draft.
