# toolbox

Definitions, lemmas and conditions as stated in the filed sources, with
statement numbers, so that a technical discussion can point at a definition
instead of rebuilding it from memory. Everything here is a synthesis of filed
sources and is machine-written; check a statement against the PDF before
quoting it in the draft.

| file | what it holds | labels |
|---|---|---|
| `gpt-framework.md` | state spaces, effects, duality, channels, composites, min/max tensor products, no-broadcasting, the three standard examples, a translation table between Plávala, Müller and Barrett | G1–G21 |
| `tft-framework.md` | bordism categories, TFTs as symmetric monoidal functors, the Atiyah–Segal data, 1d and 2d classifications, target change, invariants | T1–T10 |
| `spacetime-axioms.md` | the AQFT axioms, their mapping onto the two premises of standing assumption A6, why commutation is not independence, time-like versus space-like causality | — |
| `conditions-catalogue.md` | principles and axioms across the filed reconstructions, which theories satisfy them, a checklist for a locality-of-action principle | A–E |

## Rules

- A label (G12, T7) is a stable handle for discussion. Do not renumber; add at
  the end.
- Every statement carries the source and statement number it was read from.
  A statement without one is marked UNVERIFIED.
- Nothing here is a project convention. When a choice is made (a composition
  rule, a presentation, a bordism category) it goes into
  `conventions/domain/standing-assumptions.md` with a drop-if line, and the
  toolbox entry points to it.
- The toolbox grows by distillation: file the source first, then add the
  statements it contributes.
