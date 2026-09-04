# Naming

One convention everywhere, so that a file's name and place are predictable.

## Dated things

`YYMMDD - short description`

```
sources/meetings/260904 - reorganisation session/
sources/papers/210312 - general probabilistic theories an introduction/
```

The date is when the thing happened or first appeared, not when it was filed.
For a paper, the arXiv first-version date; say so in `source.md` if the filed
copy is a later version. Six digits, no separators. When a component is
unknown, write `00` for it and say so in `source.md`: `940300` for a paper
known only to March 1994, `480000` for one known only to 1948.

## Everything else

Lowercase, hyphens for spaces, `.md` unless the file is not markdown.

```
syntheses/wiki/no-signalling.md
pipeline/sequential-composition-as-a-gpt-principle.md
conventions/domain/standing-assumptions.md
```

## The manuscript

`paper/draft.tex`, `paper/draft.bib` and `paper/draft.pdf` keep their names;
the build depends on them. Bib keys follow the existing pattern, `AuthorYYYY`
or `AuthorAuthorYYYY`, with a descriptive suffix only when two keys would
collide (`Barrett2005polytope`).

## Sources with more than one file

A folder named for the event or paper, plain names inside.

```
sources/papers/210312 - general probabilistic theories an introduction/
├── source.md      identity and provenance
├── paper.md       machine-readable extraction
└── paper.pdf      the file, if kept in the repository
sources/meetings/260904 - reorganisation session/
├── source.md
└── notes.md       the harvest
```

## Don't

- No dates on things that are not moments in time. A synthesis is
  `no-signalling.md`, not `260904 - no-signalling.md`.
- No `-v2`, `-final`, `-latest`. Git does versions.
- No spaces around hyphens except in the dated form.
