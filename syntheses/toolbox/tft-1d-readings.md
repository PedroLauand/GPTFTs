---
status: draft
last-reviewed: 2026-09-07
sources:
  - sources/papers/170516 - introductory lectures on topological quantum field theory/paper.md
  - sources/papers/150408 - equivariant tqft and symmetry protected topological phases/paper.md
  - sources/papers/140627 - short-range entanglement and invertible field theories/paper.md
  - sources/papers/160422 - reflection positivity and invertible topological phases/paper.md
  - sources/papers/080523 - teleportation in general probabilistic theories/paper.md
machine-written: true
---

# Toolbox: what 1d TFTs describe

Pedro asked (2026-09-07) for intuition about the phenomena 1d TFTs describe,
"particle creation in vacuum, or line operators in condensed matter, or related
(to be checked)". What the filed sources support, with the dimension
conventions made explicit. Continues the T-labels.

## Dimension conventions, first

"1d TFT" in the bordism literature means Bord_1: objects are oriented points,
morphisms are intervals and circles, spacetime is one-dimensional (a worldline).
Condensed-matter "1d" means one spatial dimension, spacetime 1+1, which is
Bord_2 in bordism language. Kapustin–Turzillo write D for the spatial dimension:
their "D = 1 TQFT" is our 2d TFT. Say which is meant every time.

**T21. Cup and cap as birth and death.** A 1d TFT is a dual pair
(U, V, b : k → U ⊗ V, d : V ⊗ U → k) with the Zorro moves; Carqueville–Runkel
call b and d "birth" and "death". The cup creates a •₊ •₋ pair from the vacuum
∅, the cap annihilates one; the snake says a created pair contracted against an
incoming point returns the point. Z(S¹) = dim V counts the states of the
particle. [CR §3.1, Thm 3.2; T5] The "particle–antiparticle" wording is
folklore; no filed source uses it, though •₋ = orientation reversal is the
antiparticle in the usual reading. UNVERIFIED attribution.

**T22. The slice picture.** An object of Bord_n is "a toy model of a spacial
slice of an n-dimensional spacetime" [CR §2.2]; for n = 1 the slice is a point
and the theory has no room for dynamics: it is a finite-dimensional state space
with its dual and nothing else ("1-dimensional TQFTs are boring") [CR §3.1].
The physics of a 1d TFT is therefore the physics of dualisability: a state
space that can be paired with its dual. In the GPT target that is exactly the
teleportation structure (C8, R3): the cup is a shared resource, the cap a joint
effect, and the snake is the exact transfer of an unknown state [BBLW Thm 1].

**T23. Gapped systems and topological theories.** Freed's proposal "applies to
gapped systems which at low energy (long time) can be approximated by
topological field theories... we simply assume the existence of a long-range
topological theory"; short-range entanglement gives an invertible theory
(Kitaev: a unique vacuum on any background); deformation classes of invertible
theories are the phases; invertible theories are maps of spectra. [Freed §1,
Rem 2.7, §2.7] This is the B7 heuristic in its modern form, stated as an
assumption by its own author.

**T24. Gapped phases in one spatial dimension.** Short-range-entangled phases
are "closely connected to Topological Quantum Field Theory". Unoriented
equivariant D = 1 TQFTs (our 2d) with symmetry (G, ρ) correspond to algebraic
data (A, η, α, θ_g); the invertible ones to the twisted group cohomology
H²(BG, U(1)_ρ), matching the group-cohomology classification of SPT phases.
[KT abstract, Prop 1, 2] So the condensed-matter "1d" TFTs are Frobenius-type
algebras with extra structure, i.e. T6, T19 with a group action; nothing in the
filed sources describes a Bord_1 theory as a condensed-matter phase.

**T25. Reflection positivity.** Unitarity of a Euclidean field theory is a
reality condition plus reflection positivity; for extended invertible TFTs
Freed–Hopkins implement an extended reflection positivity and prove deformation
classes are the torsion in homotopy classes of maps between Thom spectra;
lessons: reflection and positivity are distinct, reflection is a structure,
positivity a condition, extended positivity a structure. [FH abstract, Thm 1.1,
§1; Freed §"unitarity"] For the project: the positivity that GPTs supply
natively (cones) is a candidate for the "positivity" half; UNVERIFIED reading.

**T26. Line operators and defects.** Bordisms with defects are one of the
variants Carqueville–Runkel list [CR Rem 2.3]; a 1d TFT as a line operator
inside a higher-dimensional theory is not treated in any filed source. TODO
Pedro: is this the intended reading? If so a defect-TFT source needs filing.

## Summary for discussion

A Bord_1 theory valued in GPTs is a dualisable system, i.e. a teleportation
resource; its only invariant is a dimension; its physics is pair creation and
annihilation of a system with its dual. The condensed-matter intuitions about
"1d" (SPT phases, line operators) concern Bord_2 with structure, and belong
with the unitary 2d file.
