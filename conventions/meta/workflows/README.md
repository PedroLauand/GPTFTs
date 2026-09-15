# Workflows

The recurring jobs, written down so they happen the same way each time and so
any agent can run them by being pointed at the file.

| file | run it when |
|---|---|
| `triage.md` | something has landed in `_inbox/` |
| `distillation.md` | a source has been filed, or a decision has been logged |
| `session-harvest.md` | a working session or a discussion with a collaborator ends |
| `reconciliation.md` | periodically, and before a beat is approved or results are written |

## Getting a source in takes two workflows

```
_inbox/  ──triage──►  sources/  ──distillation──►  syntheses/, pipeline/, paper/
         file it,                 work out what
         name it,                 it changes
         add metadata

         commit 1                 commit 2
         mechanical               judgment
```

Separate commits, because they need different amounts of review. Filing
follows the conventions and is checked in a minute. Deciding what a source
means is where the discussion belongs. Merged into one commit, the filing
waits on the argument.

## What they have in common

**The agent proposes and Pedro decides.** Every workflow ends with commits on a
branch, never on `main`.

**Existing records stay fixed.** Triage and harvest add records; later
workflows cite them.

**Uncertainty is marked rather than smoothed over.** `TODO:`, `UNVERIFIED:`.

## Running one

Say "run triage", or "follow `conventions/meta/workflows/triage.md`". The
skills in `.claude/skills/` are thin wrappers around these files.
