# Workflow: distillation

Work out what a filed source, or a logged decision, changes about what we
believe and what we are writing, and propose it.

This is the second half of getting a source in. `triage.md` files it; this
decides what it means. Separate commits, for the reasons in `README.md`.

## Input

One or more files already in `sources/` and already committed, or a new line
in `sources/decisions.md`.

## Steps

1. **Read the source properly**, and read `conventions/domain/` before you
   interpret it. Use our words, not the source's, and flag where they differ.

2. **Find what it touches.** Search `syntheses/` and `pipeline/` for the
   topic, and search `paper/draft.tex` for the bib key. There may be nothing,
   in which case you are proposing a new synthesis.

3. **Work out what changed.** For each affected file, one of: it confirms what
   we say (say so and stop); it adds something we did not have; it contradicts
   something we say; it makes something more precise. Contradiction is the
   valuable case. Do not resolve it silently. Present both sides.

4. **Check the citations.** For every sentence in the draft that cites this
   source: does the source support the sentence as written? Record the answer
   in the "Citation checks" section of `syntheses/literature-map.md`. If the
   answer is no, say so there; do not edit the draft.

5. **Draft the change.** Cite into the source rather than restating it. Link
   the file and quote only what carries the point.

6. **Mark what you are unsure of** with `UNVERIFIED:` inline.

7. **Check for pipeline items.** If the source suggests something worth
   working on, note it in the commit message. Do not create a pipeline file;
   that is Pedro's decision.

8. **Update front matter.** Add the source to `sources:`, set `last-reviewed`.

9. **Commit on the branch**, one commit per synthesis touched.

## Output

Commits whose messages say, in one or two sentences each: what the source
changes; anything it contradicts, stated as a contradiction; what could not be
verified; pipeline ideas, as a note only.

## Stop and tell Pedro

- The source contradicts a standing assumption in `conventions/domain/`.
- The change would alter the text of an approved beat.
- You would have to choose between two sources that disagree.
- The change touches more than three files. Split it and ask which first.
