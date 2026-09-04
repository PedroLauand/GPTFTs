# AGENTS.md

This repository is the working memory of one research project: a paper, working
title *What does topological field theory require of probabilistic theories?*,
by Pedro Lauand (Perimeter Institute). The no-signalling principle encodes the
kinematic side of compatibility between a general probabilistic theory (GPT)
and spacetime: points held at spacelike separation cannot influence each
other's statistics. Spacetime physics has a second, dynamical side, locality of
action: between causally connected points, influences propagate locally by a
dynamical law. The project imports that second side into the GPT framework and
asks what it requires of a probabilistic theory.

The manuscript lives in `paper/`. Everything else exists so that a person or an
agent can pick the project up cold: what the literature says, what we currently
believe it means, what we are working towards, and how we work. Structure and
conventions follow Aggie Branczyk's `third-brain` repository, adapted to a
private, single-author project with occasional collaborators. There is no group
and no pull-request review here: Pedro is the reviewer, and the branch diff is
where the review happens.

Read `conventions/` before doing anything else. `conventions/domain/` holds the
standing assumptions, notation, glossary and the standard a claim must meet.
`conventions/meta/` describes how this repository works.

## Starting a session

In this order, every time:

1. `conventions/domain/standing-assumptions.md`, then the rest of
   `conventions/`.
2. The tail of `sources/decisions.md`: what was settled most recently.
3. The status table in `syntheses/narratives/intro-narrative.md`: where the
   manuscript stands, beat by beat.
4. The `status:` line of every file in `pipeline/`.
5. For technical work, `syntheses/toolbox/README.md`: definitions and lemmas
   with statement numbers, so the discussion can point at G12 or T7 instead of
   rebuilding them.

That is the project's current state. Read `paper/draft.tex` itself when the
task touches the text.

## Where things go

| folder | what it holds | tense | who changes it |
|---|---|---|---|
| `paper/` | the manuscript: `draft.tex`, `draft.bib`, `draft.pdf` | present, live | Pedro; agents propose, never overwrite approved text |
| `_inbox/` | arrived, not yet filed | — | anyone, temporary |
| `sources/` | what was said, known or decided, unedited: papers, discussions, the decision log | past, fixed | append only |
| `syntheses/` | what we understand the sources and the draft to mean | present, live | agents on a branch, Pedro merges |
| `pipeline/` | questions and ideas on their way to results | future, live | agents on a branch, Pedro merges |
| `conventions/` | how we work | standing | Pedro, or an agent on a branch when asked |

## Rules

**Never edit `sources/`.** They are the record. The one exception is the
append-only decision log, `sources/decisions.md`: add dated entries at the end,
never change earlier ones. If a source is wrong, say so in a synthesis.

**The manuscript is Pedro's voice.** In `draft.tex`, blue text is drafted or
approved prose, and the `%` comment above each block says which, and when. Do
not rewrite an approved beat. Propose wording as a new commented block beneath
it, or in `syntheses/narratives/intro-narrative.md`. Red `\tmp{[...]}` marks
placeholders and open citations.

**Cite into `sources/` rather than restating.** Link the filed source and quote
only what carries the point. A quotation enters the draft only after it has
been checked against the filed source. If the work is not filed yet, say so
with `UNVERIFIED:`.

**Use our notation and our words.** `conventions/domain/notation.md` and
`glossary.md`. Flag it when a source's usage differs from ours. The phrases
that need care are in `rigour.md`; the one we never write is that
no-signalling is *derived from* relativity.

**Say when you don't know.** `TODO:` or `UNVERIFIED:` inline, in the sentence
it applies to. An unmarked guess costs more than a gap.

**Say when a draft is machine-written.** It is information for the reviewer,
not a disclaimer.

**Filing and interpretation are separate commits.** Triage files a source.
Distillation decides what it changes. Never both in one commit.

## Naming

`YYMMDD - short description` for anything dated. Lowercase with hyphens for
everything else. The three manuscript files keep their names because the build
depends on them. Details in `conventions/meta/naming.md`.

## Workflows

The recurring jobs are written down in `conventions/meta/workflows/`:

| workflow | what it does |
|---|---|
| `triage` | file something from `_inbox/`, and stop there |
| `distillation` | propose what a filed source changes in the syntheses, the pipeline or the draft |
| `session-harvest` | record the decisions, questions and actions of a working session or a discussion |
| `reconciliation` | check the syntheses and the draft against the sources and against each other |

Getting a source in takes two of these, in order and in separate commits:
`triage` files it, `distillation` works out what it changes. Every session
ends with `session-harvest`.

Read the workflow file before running one. They are exposed as skills in
`.claude/skills/` as thin wrappers; the workflow file is the definition.

## Working with git

Work on a branch. Commit as you go, with messages that say why. Before creating
a branch, update `main` from `origin/main` with a fast-forward-only pull; if
that fails, stop and tell Pedro. If you are on `main` when about to change a
file, say so and branch first.

There are no pull requests in this repository. At the end of a change, report
the branch name and whether it has been pushed, and say that merging into
`main` is Pedro's step.

If several agents run at once, give each its own clone or `git worktree`. Two
agents in one working tree overwrite each other.

## What was retired

On 2026-09-04 the earlier working notes (`notes.tex`, `main.tex`, the
narrative, quote and reference files, and the candidate-GPT definitions) were
removed and the repository was rebuilt around `draft.tex` alone. The old files
are in git history at the tag `archive/pre-reorg-260904`. Their technical
conventions were not carried over; read "Things we have decided not to assume"
in `conventions/domain/standing-assumptions.md` before reintroducing any of
them.
