# Attribution

Git records who did what and when. `.mailmap` collapses Pedro's two git
identities into one name; add a line when a new alias appears.

Collaborators comment in the draft with the coloured macros `\bereket{}` and
`\elie{}`. Those comments are contributions and stay in the file until
resolved, at which point the resolution is recorded in `sources/decisions.md`.

When an agent drafts something, the file says so: `machine-written: true` in
front matter, "(agent)" in the decision log, "Draft, machine-written" in a
`%` comment. This is information for the reviewer, not a disclaimer. The
person who approves a beat is its author.

At the end of the project:

```
git log --no-merges --pretty=format:'%an %ad %s' --date=short
```
