---
type: decision-log
source-of-record: this file
---

# Decision log

Dated, append only. New lines go at the end. Never edit an earlier line; if a
decision is reversed, add a line saying so. Each line: date, the decision,
where it is recorded. Lines written by an agent are marked (agent).

- 2026-06-16 — Project moved from Overleaf to GitHub. [git: Initial Overleaf Import]
- 2026-08-31 — Introduction beats B1+B2 (operational stance; GPTs as the framework) and B2b (reconstructions; special relativity as role model) approved as written. [paper/draft.tex, beat comments]
- 2026-09-01 — B3 opening approved: no-signalling as the most famous principle, the weakest condition compatible with special relativity, formulated as commuting operations; ends with the question whether spacetime compatibility requires other principles. [paper/draft.tex]
- 2026-09-01 — The earlier B4 pivot ("modern view of spacetime physics", RG genericity, the two AQFT-mirroring premises) retired from the introduction and kept commented for salvage; RG and AQFT material may return in B7 or B8. [paper/draft.tex, RETIRED block]
- 2026-09-01 — New B4 opening drafted: no-signalling considers the kinematical picture; locality of action is the other feature of spacetime. Awaiting approval. [paper/draft.tex]
- 2026-09-04 — Repository rebuilt around `draft.tex` following the third-brain conventions, for private use. `notes.tex`, `main.tex`, their PDFs, the narrative, quote and reference files and the candidate-GPT definitions purged; recoverable at git tag `archive/pre-reorg-260904`. (agent, on Pedro's instruction) [this repository]
- 2026-09-04 — The technical conventions of the retired notes (ambient space, canonical cone, unoriented bordisms, terminology) are not carried over and are not assumed until re-entered deliberately. (agent, on Pedro's instruction) [conventions/domain/standing-assumptions.md]
- 2026-09-04 — Among build outputs only `paper/draft.pdf` is tracked. (agent) [.gitignore]
- 2026-09-04 — Sources filed without PDFs: arXiv is the source of record, `source.md` records the version, `paper.md` is the extraction. Stubs for works with no open copy. (agent; Pedro to confirm) [conventions/meta/file-conventions.md, sources/papers/]
- 2026-09-04 — Unknown date components are written `00` in dated folder names. (agent) [conventions/meta/naming.md]
- 2026-09-04 — Technical context kept as a toolbox under `syntheses/toolbox/` with stable labels (G, T), built only from filed sources; project choices still go to standing assumptions. (Pedro's request, agent's layout) [syntheses/toolbox/README.md]
- 2026-09-04 — Popescu–Rohrlich 1995 (quant-ph/9508009) filed although not in the bib, as the open proxy for the 1994 paper; not to be cited in its place without Pedro. (agent) [syntheses/literature-map.md]
