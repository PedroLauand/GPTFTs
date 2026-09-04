# Workflow: triage

File something that has landed in `_inbox/`, and stop there.

## Triage and distillation are separate

| | what it is | who decides | commit |
|---|---|---|---|
| **1. Triage** *(this workflow)* | name it, file it, add metadata | mechanical, follow the conventions | one, easy to review |
| **2. Distillation** *(`distillation.md`)* | work out what it changes | judgment, Pedro decides | a separate one |

Finish and commit triage before running distillation.

## Input

Any file in `_inbox/`: a PDF, notes, a transcript, a URL in a text file.

## Steps

1. **Read it**, enough to know what it is and what it is about. For a PDF,
   read the content rather than going by the filename.

2. **Classify it.** A source (something said, known or decided, fixed in
   time), or an idea for `pipeline/`? Almost everything is a source. If it is
   an idea, say so and stop: starting a pipeline entry is Pedro's decision.

3. **Work out the date it belongs to**: when it happened or first appeared,
   not today. For a paper, the arXiv first-version date.

4. **Choose a name and a location** following `conventions/meta/naming.md`.
   Papers go in `sources/papers/`, discussions and harvested sessions in
   `sources/meetings/`. Every source gets its own folder and a `source.md`:
   identity, date, authors or participants, external source of record. Other
   files in the folder point to it with `source-of-record: source.md`.

5. **Check whether it is already here.** Search `sources/` for the same paper
   or event. Duplicates under different names are how a collection rots.

6. **Check the bibliography.** If it is a cited work, note the `draft.bib`
   key in `source.md`. If it is not in `draft.bib`, say so; adding it is
   distillation's job, not triage's.

7. **Make it readable.** For a PDF, write `paper.md`, a complete
   machine-readable extraction, headed `extraction: machine-generated`,
   `reviewed: false`. Keep the PDF in the folder if it is a few megabytes or
   less; otherwise follow `conventions/meta/file-conventions.md`.

8. **Add front matter** as in `conventions/meta/file-conventions.md`.

9. **Note what it probably affects.** Which syntheses, which pipeline items,
   and which sentences of the draft cite it. List them in the commit message.
   Interpretation belongs to distillation.

10. **Commit on the branch**, with a message saying what the artifact is and
    where it went.

## Output

One commit that moves one thing out of `_inbox/`, whose message says what it
is, where it went and why, what you were not sure about, whether it looks like
a duplicate, and which syntheses, pipeline items and draft sentences it
probably bears on.

## Stop and tell Pedro

- The date is ambiguous and it matters.
- It could reasonably be a source or a pipeline idea.
- It contains something unpublished by someone else and you are not sure it
  should be in the repository.
