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
- 2026-09-07 — Toolbox scope (Pedro's answers to the agent's eleven questions): GPT side first with categorical definitions kept in close analogy to explicit examples; track the axioms used in the GPT literature (self-duality weak and strong, teleportation, spectrality, strong symmetry, the diagrammatic postulates); TFT side: 1d intuition first, then unitary 2d TFTs and the commutative semisimple Frobenius structure, asking which GPTs admit them. [sources/meetings/260907 - toolbox scoping session/notes.md]
- 2026-09-07 — Works not in `draft.bib` may be filed as sources; they enter the bib only when a sentence needs them. (Pedro) [same]
- 2026-09-07 — The project's categorical framing will be its own, expected close to Selby–Scandolo–Coecke; for now systems are objects and physical transformations morphisms (provisional convention P2). (Pedro) [conventions/domain/standing-assumptions.md]
- 2026-09-07 — The retired notes may be mined for useful content, including the candidate-GPT definitions; conventions from them are still not assumed unless re-entered. (Pedro) [syntheses/toolbox/project-results-archive.md]
- 2026-09-07 — Toolbox statements only, and only the essential ones; no proofs. (Pedro) [syntheses/toolbox/README.md]
- 2026-09-07 — House notation adopted for the toolbox: systems (V_A, V_A^+, u_A), the retired notes' notation, as provisional convention P1. (Pedro: "house notation is better, we will have our own convention"; agent's choice of which) [conventions/domain/notation.md]
- 2026-09-07 — Examples beyond classical, quantum and boxworld are in scope (polygons, real and quaternionic quantum theory, Jordan algebras, OST, Dmello–Gross families, density hypercubes). (Pedro) [syntheses/toolbox/gpt-examples.md]
- 2026-09-07 — Project folders stay self-contained: nothing imported from collaborators' materials or other repositories. (Pedro) [same]
- 2026-09-07 — Twenty-four sources filed for the toolbox without PDFs; Aubrun–Lami–Palazuelos–Plávala 1911.09663 filed in addition to 1910.04745 because the theorem is in the former. (agent) [syntheses/literature-map.md]
- 2026-09-07 — Results section 1 fixed at the level of logic: dimension one is contained in every TFT by crossing with a slice; dualizability is forced; its content is closed-spacetime values (ground-state degeneracy), cutting and gluing (locality of action), and pair creation and annihilation; in a probabilistic theory the snake is exact teleportation and its chains are entanglement swapping, so the protocol is a spacetime requirement; a GPT without dualizable systems cannot be the effective theory of any topological phase or pair-production process. Quantum theory deferred to Section 4. Draft of the section and stubs for 2–5 in `paper/results-plan.md`. (Pedro and agent)
