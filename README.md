# GPTFTs

Working memory of one research project: a paper, working title *What does
topological field theory require of probabilistic theories?*, by Pedro Lauand
(Perimeter Institute for Theoretical Physics). The manuscript is in `paper/`.
The rest of the repository keeps the literature, what we believe it means, what
we are working towards, and how we work, in a form a person or an AI agent can
read, change, and have reviewed.

Structure and conventions follow Aggie Branczyk's `third-brain` repository,
adapted to a private single-author project. Agents read `AGENTS.md` on their
own.

## Layout

```
paper/        the manuscript                          present, live
_inbox/       arrived, not yet filed
sources/      what was said, known or decided          past, fixed
syntheses/    what we understand it to mean            present, live
pipeline/     what we are working towards              future, live
conventions/  how we work                              standing
```

Sources never change. Syntheses change often. Keeping them apart is what stops
an agent from reading its own earlier output back as evidence.

## Where the project stands (2026-09-04)

- **Introduction.** Beats B1+B2, B2b and the opening of B3 are approved. The
  new B4 opening (no-signalling as the kinematical picture, versus locality of
  action) is drafted and awaiting approval. B6 to B9, the title and the
  abstract are placeholders. Map: `syntheses/narratives/intro-narrative.md`.
- **Results.** Not in the draft. The earlier technical notes were retired on
  2026-09-04 (git tag `archive/pre-reorg-260904`); results re-enter through
  `pipeline/`.
- **Literature.** 42 works in `paper/draft.bib`; 9 cited in live text, 7 more
  only in a retired paragraph, 26 not yet cited; none filed in `sources/`.
  Map: `syntheses/literature-map.md`.

## Working here

1. Open an agent in this folder, or read `AGENTS.md` and `conventions/`
   yourself. They are short.
2. Work on a branch. Review the diff. Merge into `main` yourself.
3. Build the paper with `cd paper && latexmk -pdf draft.tex`. RevTeX 4.2 is
   required; on this machine it is under `~/Library/texmf`.
