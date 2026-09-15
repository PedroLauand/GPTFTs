# Workflow: session harvest

Record what a working session settled. Sessions with an agent and discussions
with collaborators both count. This is what makes the next session start from
the last one instead of from zero.

## Input

The conversation just had, or notes or a transcript of a discussion in
`_inbox/`.

## Steps

1. **Read the whole thing before extracting.** Decisions get reversed later in
   the same conversation.

2. **Extract four things** and keep them separate:
   - **Decisions taken.** What was settled, and by whom.
   - **Questions raised.** Open questions, including ones nobody answered.
   - **Actions.** Who said they would do what.
   - **Beats and pipeline items touched.** Which parts of the draft or the
     pipeline came up, and what changed about them.

3. **Attribute carefully.** If you cannot tell who said something, say so
   rather than guessing. A wrong attribution does more damage than a missing
   one.

4. **Quote rather than paraphrase** for anything contentious.

5. **Write the harvest** as `sources/meetings/YYMMDD - <topic>/notes.md`, with
   a `source.md` beside it (`type: session` or `type: discussion`, `date`,
   `present`). Mark it machine-written.

6. **Append each decision to `sources/decisions.md`**, one dated line each,
   at the end. Never edit earlier lines; a reversal is a new line.

7. **Propose downstream changes separately**, following `distillation.md`. A
   decision may change a standing assumption, a synthesis, a pipeline status
   or the draft. Those are their own commits.

8. **Commit on the branch**: "Harvest session YYMMDD: <topic>".

## Output

- `notes.md` and `source.md` in a dated folder under `sources/meetings/`
- new lines at the end of `sources/decisions.md`
- separate commits for anything that changes a synthesis, a pipeline item, a
  convention or the draft

## Stop and tell Pedro

- A decision contradicts a standing assumption in `conventions/domain/`.
- Attribution is unclear and the content matters.
