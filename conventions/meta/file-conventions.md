# File conventions

## Formats

Markdown by default: people and models read it, git diffs it, a review works
line by line. LaTeX for the manuscript. PDFs where they are the artifact
itself. Anything else when the format adds something and a change can still be
reviewed.

## Front matter

Markdown files in `sources/`, `syntheses/` and `pipeline/` start with a YAML
block, so the collection can be searched without a database.

### Sources

Every source folder has a `source.md` with identity and provenance. Every other
file in the folder points back with `source-of-record: source.md`.

```yaml
---
type: paper              # paper | discussion | session | talk | note
date: 2021-03-12         # when it happened or first appeared
author: [name]           # or present: [name, name] for discussions
source-of-record: <arXiv or publisher URL, or "this folder">
---
```

A paper filed here also gets `paper.md`, a machine-readable extraction, headed
`extraction: machine-generated` and `reviewed: false` until someone checks it.

### Syntheses

```yaml
---
status: draft            # draft | reviewed | stable
last-reviewed: 2026-09-04
sources:
  - paper/draft.tex
  - sources/papers/210312 - general probabilistic theories an introduction/paper.md
machine-written: true    # drop once a person has rewritten it
---
```

`paper/draft.tex` is a legitimate source for a synthesis of the draft's own
argument. Cite the beat label.

### Pipeline

See `pipeline/TEMPLATE.md`, which carries its own front matter.

### The decision log

`sources/decisions.md` is a list, one dated line per decision, append only.

## The manuscript

- One beat per `\textcolor{blue}{...}` block, with a `%` comment above it
  giving the beat label, a one-line summary, and the status with date
  ("Approved 2026-08-31", "Draft, awaiting approval", "RETIRED").
- Approved text is not edited by agents. Proposals go beneath the block as a
  commented alternative, or into the narrative synthesis.
- `\tmp{[...]}` for every placeholder, so that `grep tmp` lists the open
  items.
- Bib entries carry `eprint` and `archivePrefix` when an arXiv version exists.
  The `%` section comments in `draft.bib` group entries by the beat they serve;
  keep them current.

## Binaries

- `paper/draft.pdf` is tracked: the latest build is part of the record.
  Rebuild with `latexmk -pdf draft.tex` in `paper/`; every other build output
  is ignored.
- A reference PDF may be kept in its source folder when it is a few megabytes
  or less. Larger or frequently regenerated files go elsewhere, with a stub
  `<name>.md` in the folder recording what and where. The `paper.md`
  extraction is what agents read either way.
- No notebooks are expected. If one arrives, strip outputs and add a text
  companion.
