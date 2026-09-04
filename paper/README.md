# paper

The manuscript.

| file | what it is |
|---|---|
| `draft.tex` | RevTeX 4.2, PRL two-column. The introduction is written beat by beat; see the markup legend in `conventions/domain/notation.md` |
| `draft.bib` | 42 entries, grouped by the beat they serve. Map: `../syntheses/literature-map.md` |
| `draft.pdf` | the latest build, kept in git |

Build: `latexmk -pdf draft.tex`. All other build outputs are ignored.

Rules for editing are in `AGENTS.md` ("The manuscript is Pedro's voice"):
approved beats are not rewritten by agents; proposals go beneath the block as a
commented alternative or into `../syntheses/narratives/intro-narrative.md`.
`grep tmp draft.tex` lists the open placeholders.
