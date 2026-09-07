# toolbox

Definitions, lemmas, axioms and examples as stated in the filed sources, with
statement numbers and stable labels, so that a technical discussion can point at
a definition instead of rebuilding it. House notation throughout
(`conventions/domain/notation.md`, provisional convention P1). Everything here
is machine-written; check a statement against the PDF before quoting it in the
draft.

| file | what it holds | labels |
|---|---|---|
| `gpt-framework.md` | systems, effects, duality, channels, composites, min/max tensor cones, entangleability, no-broadcasting, the three standard examples, translation table | G1–G21 |
| `categorical-gpts.md` | the category GPT, composites, terminality, cups and caps, dualisable objects, teleportation, dagger, purification, classical interface, Jordan-algebraic categories, entanglement-swapping theories, GPT versus Vec | C1–C14 |
| `gpt-axioms.md` | the structural axioms of the GPT literature: self-duality (weak, strong), homogeneity, frames, spectrality, strong symmetry, bit symmetry, higher-order interference, the diagrammatic postulates, teleportation, entangleability; an implications list | X1–X22 |
| `gpt-examples.md` | classical, quantum, real, quaternionic, balls, Jordan algebras, boxworld, polygons, Spekkens toy, OST, Dmello–Gross families, density hypercubes, nearly quantum composites; a table of which axioms hold where | E1–E13 |
| `conditions-catalogue.md` | the reconstruction axiom lists (Hardy, CDP, Masanes–Müller, Müller) and a checklist for a locality-of-action principle | A–E |
| `tft-framework.md` | bordism categories, TFTs as functors, Atiyah–Segal data, 1d and 2d classifications, target change | T1–T10 |
| `tft-unitary-2d.md` | unitary TFTs, C*-Frobenius algebras, direct-sum decomposition, Durhuus–Jonsson classification, semisimple = functions on a finite set, orthonormal bases as Frobenius algebras, the bridge to GPT frames, unoriented variant | T11–T20 |
| `tft-1d-readings.md` | what 1d TFTs describe: birth and death, the slice picture, gapped phases, SPT phases in one spatial dimension, reflection positivity, defects; dimension conventions | T21–T26 |
| `spacetime-axioms.md` | the AQFT axioms against the two premises of standing assumption A6; commutation is not independence | — |
| `project-results-archive.md` | the retired notes' own results, unverified and not assumed: forced dual, cup/cap conditions, 2d positivity constraints, weak self-duality corollary, worked examples, no-go, open problems, candidates | R1–R16 |

## Rules

- A label is a stable handle. Do not renumber; add at the end of a file.
- Every statement carries the source and statement number it was read from. A
  statement without one is marked UNVERIFIED; project results carry an R label
  and are never assumed.
- Nothing here is a project convention. Choices go into
  `conventions/domain/standing-assumptions.md` (assumptions A, provisional
  conventions P) with a drop-if line; the toolbox entry points to it.
- The toolbox grows by distillation: file the source first, then add the
  statements it contributes. Statements only, and only the essential ones
  (Pedro, 2026-09-07).
