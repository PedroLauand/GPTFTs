# Workflow: reconciliation

Check the syntheses, the pipeline and the draft against the filed sources and
against each other, then report. Run it periodically, and before a beat is
approved or results are written into the draft.

## Steps

1. **Read every file in `syntheses/` and `pipeline/`, and `paper/draft.tex`.**
   If that is too much at once, do it a folder at a time and say which.

2. **Look for five things:**
   - **Contradictions.** Two files, or a file and the draft, that cannot both
     be true.
   - **Drift from source.** A claim whose cited source does not support it, or
     a draft sentence whose citation check is still pending or failed.
   - **Orphans.** Claims with no source and no `UNVERIFIED:` mark.
   - **Staleness.** A `last-reviewed` older than decisions logged since, or a
     beat whose status in the narrative differs from its `%` comment.
   - **Drift from conventions.** Notation, spelling and words-that-need-care
     against `conventions/domain/`; a standing assumption the draft no longer
     honours.

3. **Write the report** to `syntheses/reconciliation-report.md`, overwriting
   the previous one; history is in git. For each finding: what it is, which
   files, what the evidence is, how confident you are. Alarming findings
   first.

4. **Do not fix anything.** This workflow reports. Fixes go through
   `distillation.md` after Pedro decides.

5. **Commit on the branch**, containing only the report.

## Output

A report ordered by how much each finding matters, which Pedro can act on
without rereading the collection.
