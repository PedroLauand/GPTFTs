---
status: draft
last-reviewed: 2026-09-11
sources:
  - paper/draft.tex
machine-written: true
---

# The introduction, beat by beat

What `paper/draft.tex` argues, in order, with the status of each beat. Built
from the draft alone on 2026-09-04. The draft is the record of the wording;
this file is the map. Update the status table whenever a beat changes status,
and log the change in `sources/decisions.md`.

## Status table

| beat | job | status | citations |
|---|---|---|---|
| B1+B2 | operational stance; GPTs as the framework; quantum theory one among many | approved 2026-08-31 | Barrett2007, Muller2021, Plavala2023; Hardy2001, CDP2011, MasanesMuller2011. One `\tmp{[cite]}` open |
| B2b | reconstructions; special relativity as role model; Hardy, then CDP and Masanes–Müller | approved 2026-08-31 (grammar-only fixes) | Hardy2001, CDP2011, MasanesMuller2011 |
| B3 | no-signalling the most famous principle; weakest, compatible with SR; commuting operations | approved 2026-09-01; closing question retired 2026-09-11 | PopescuRohrlich1994, Gisin2020, Barrett2007 |
| B4 (new) | no-signalling as the kinematical picture; **the question** | drafted 2026-09-01, question added and locality-of-action sentence removed 2026-09-11, awaiting approval | none live; Einstein1948 now only in comments |
| B4 (old) | modern spacetime physics; fields; RG genericity; two premises mirroring AQFT | retired 2026-09-01, kept commented | Einstein1948; WilsonKogut1974, Wilson1975, WeinbergEFT, Polchinski1992; StreaterWightman, HaagSchroer1962, FewsterRejzner2019; Barrett2007 |
| B5 | — | no such beat; numbering runs B4 → B6 | — |
| B6 | reconceptualisation: continuity and the RG justify a field-theory description | placeholder | bib group B6 ready, uncited |
| Warning | a caveat, content not indicated in the draft | placeholder `\tmp{[Warning]}` | — |
| B7 | low-energy, gapped limit justifies TFT; Atiyah–Segal skeleton | placeholder | bib group B7 ready, uncited |
| B8 | the new question, mirroring no-signalling | placeholder | bib group B8 (prior art) ready, uncited |
| B9 | results | placeholder `\tmp{[Declare results.]}`; no results in the draft | — |
| title, abstract | | placeholders | — |

## The chain

**B1+B2. Operational stance; GPTs.** Quantum theory is "one of the most
empirically successful theories in science" and describes its experiments
probabilistically; every empirical claim is collected outcome statistics.
"Despite its success, the foundational aspects of its mathematical formulation
have remained elusive" (citation open). The textbook presentation, Hilbert
space and self-adjoint operators, has "postulates [that] arguably carry no
direct physical motivation". The operational view takes self-evident features
of laboratory situations as primitives and derives the formalism from them,
so that quantum theory is understood "as a consequence of natural
information-theoretic constraints over the mathematical framework of
Generalized Probabilistic Theories", in which it is "one theory among many
others".

**B2b. Reconstructions.** The next wave of axiomatizations. Role model:
special relativity, where Einstein derived the Lorentz transformations from
two principles. Reconstructions make the formalism physically motivated with
information-processing assumptions. Hardy first; CDP and Masanes–Müller
later. "Each of these reconstructions selects quantum theory out of the
landscape of GPTs as the unique GPT that satisfies a set of simple
principles."

**B3. No-signalling and the question.** The most famous principle in GPTs;
"the weakest condition any 'reasonable' physical theory must satisfy, in the
sense of being compatible with special relativity"; formulated as "operations
on separate systems commute"; guarantees that spacelike separated devices have
correlations respecting relativistic causality; hence "the compatibility of
relativistic causality with the operational theory". Ended, until 2026-09-11,
on the question "are there other physical principles that spacetime
compatibility requires from any probabilistic theory?"; that sentence is now
commented out above B4, and the question is asked in B4 instead (decision of
2026-09-11).

**B4, new opening (drafted; locality of action removed 2026-09-11).** No-signalling "considers the kinematical
picture of relativity": systems are points of spacetime and spacelike
separated points cannot instantaneously influence each other's statistics.
"The only feature of spacetime this invokes is the causal relation between a
pair of points." Then the programme's question, in Pedro's words of
2026-09-11: "what does a probabilistic theory require in order to be
distributed over space?" The beat ends there. The locality-of-action
sentence ("between points that *are* causally connected, influences propagate
locally through spacetime, by a dynamical law", Einstein1948) was removed on
2026-09-11 and kept commented; the premise itself stands (A5), it is simply no
longer introduced here. What now answers the question is owed to the later
beats, and the two requirements the results use, dualizability and unitarity,
are read as spacetime requirements in
`pipeline/spacetime-reading-of-the-axioms.md`.

**B4, retired paragraph.** Two paragraphs, commented out. First: modern
spacetime physics goes beyond the kinematic picture; its degrees of freedom
are fields governed by a local dynamical law, and the description is generic
rather than fundamental because of the renormalisation group. Second: once a
GPT's degrees of freedom are distributed over spacetime, two premises arise,
mirroring AQFT's causal axioms: (i) spacelike independence, parallel
composition; (ii) a local dynamical law propagating a region to its causal
development, sequential composition. No-signalling implements (i) alone;
premise (ii) "has never been imported into the GPT framework; it is the
premise from which our principles follow." The `%` note says the RG and AQFT
material may return in B7 or B8.

**B6, B7, B8, B9.** Placeholders. The `%` comments fix their jobs:
reconceptualisation via continuity and the RG (B6); the gapped limit and the
Atiyah–Segal skeleton (B7); the new question stated so that it mirrors
no-signalling (B8); results (B9). Between B6 and B7 sits `\tmp{[Warning]}`
with no comment.

## Open items in the text

- `\tmp{[cite]}` in B1+B2 after "remained elusive".
- Approval of the new B4 opening, now including the question.
- "Space" in the question is settled (Pedro, 2026-09-11): the degrees of
  freedom are distributed over space, and then evolve in time.
- B6, Warning, B7, B8, B9, title, abstract.
- Spelling consistency (`conventions/domain/notation.md`).
- Citation checks pending for every live citation
  (`syntheses/literature-map.md`).

## Reading of the argument (machine-written, for the reviewer)

The pivot the introduction is building: no-signalling uses one feature of
spacetime, the causal relation between pairs of points; spacetime has another
feature, locality of action, which is dynamical; import it; ask what it
requires. The title says what form the import takes: topological field theory.
So the introduction has to get from "locality of action" to "TFT", which is
B6 (field theory is the generic description of local dynamics) and B7 (its
gapped limit is topological). The retired paragraph used to carry the first
half of that step in one sentence, "fields governed by a local dynamical law";
with it gone, the new B4 opening ends on locality of action and B6 has to pick
up from there. The Warning placeholder probably belongs to the same move: what
the field-theoretic reframing does not claim. UNVERIFIED; the draft does not
say.
