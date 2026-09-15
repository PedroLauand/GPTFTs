---
type: session
date: 2026-09-04
present: [Pedro Lauand, Claude (agent)]
source-of-record: source.md
machine-written: true
reviewed: false
---

# Harvest: reorganisation session, 2026-09-04

Machine-written from the conversation, unreviewed. Quotations are Pedro's
words as typed; everything else is the agent's summary.

## Decisions taken

1. **Adopt the third-brain structure for GPTFTs, privately.** Pedro: "im using
   aggies conventions and structures/ideas but these projects are not to be
   shared, they will just be better organized locally and will help in the
   structured discussions". Reason given: "the complexity and level of detail
   of the project are too demanding without proper register and an extensive
   context on the project and previous literature and our current goals".
2. **Keep only the draft.** Pedro: "the only thing you need to salvage is the
   draft tex and pdf info the other documents can be purged and replaced by
   simply conventions and literature." Everything else archived at git tag
   `archive/pre-reorg-260904`, then removed. The agent had earlier argued
   against a full reorganisation; Pedro's second message settled it.
3. **Rebuild the conventions from the draft's spirit alone.** Pedro: "make an
   extensive revision for this project keeping only the spirit left in draft."
   The retired notes' technical conventions are therefore not assumed.
4. **No pull requests.** Agent proposal accepted by silence: branch, Pedro
   reviews the diff and merges.
5. **Build a technical toolbox.** Pedro: "create technical context for
   definitions and Lemmas as tools, for instance the mathematical framework of
   GPTs, and technical definitions and conditions we may want to discuss", and
   "include more content regarding the information we've established of this
   project." Done as `syntheses/toolbox/` from the filed sources.
6. **Agent-level choices, to confirm:** no PDFs in the repository (arXiv is the
   source of record); `00` for unknown date components; the 1995
   Popescu–Rohrlich paper filed as an open proxy for the 1994 one.

## Questions raised, not yet answered

- Spelling: American or British for the manuscript (the draft mixes them).
- The no-restriction hypothesis: assumed or not.
- Reconstruction or classification: which the results will be.
- Closed or extended TFT in the title's sense.
- Whether isotony is part of what the paper means by premise (ii).
- Whether to re-file the retired quote bank (115 verified quotes) as a
  synthesis, or leave it in the archive.
- Whether to delete the remote branch `claude/project-overview-y0l5b0`.
- Whether B4 should cite Einstein1948 for the field-theory remark only, and
  state the dynamical half in its own voice (citation check: partial).
- Whether B3's weakest-condition sentence should be quoted from Gisin et al. or
  rephrased, and whether to cite PopescuRohrlich1994 directly for it.
- Whether B2b's special-relativity sentence should cite MasanesMuller2011 or
  Popescu–Rohrlich 1995, both of which use the analogy.
- Approval of the new B4 opening (drafted 2026-09-01).

## Actions

- Pedro: merge `reorg/knowledge-repo` into `main` and push; review
  `conventions/domain/standing-assumptions.md`; answer the TODOs above.
- Agent (done this session): archive, purge, conventions, narrative,
  literature map, pipeline items; filed 13 sources (11 arXiv extractions, 2
  stubs); citation checks for all nine live citations; toolbox of four files;
  this harvest.
- Agent (proposed next): file the B7 and B8 groups and the two remaining AQFT
  references; draft B6 and B7 as commented proposals once Pedro has answered
  the TODOs.

## Beats and pipeline items touched

- B2b: a filed source for the special-relativity analogy (MM abstract; PR1995).
- B3: Gisin2020 supported near-verbatim; PopescuRohrlich1994 partial (no text).
- B4 (new): Einstein1948 partial; wording or citation to adjust.
- Retired B4: Barrett tensor-product sentence needs "and the global state
  assumption"; the AQFT premise split verified against Fewster–Rejzner.
- Pipeline: `sequential-composition-as-a-gpt-principle.md` gained a candidate
  formalisation and checked prior-art bullets; the other two items unchanged.
