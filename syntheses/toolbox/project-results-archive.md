---
status: draft
last-reviewed: 2026-09-07
sources:
  - paper/draft.tex
machine-written: true
---

# Toolbox: project results from the retired notes

Statements mined on 2026-09-07 from the files removed on 2026-09-04
(`notes.tex`, `main.tex`, `REORG-PLAN.md`, the candidate-GPT definitions; git
tag `archive/pre-reorg-260904`), on Pedro's instruction. They are the project's
own earlier work, not literature: **unverified, not assumed**, kept so that a
discussion can point at them. Where the notes cite a now-filed source the
toolbox label is given. Notation is the house notation, which is theirs.

## Category and duality

**R1. The dual is forced.** If X = (V, V^+, u) is dualisable in (GPT, ⊗) then,
up to isomorphism, X^∨ = (V^*, (V^+)^*, u^∨) with u^∨ any interior point of V^+,
ev the canonical pairing and coev(1) = Σ_a f_a ⊗ f^a. Proof idea: forgetting
cones gives the Vec data, which are canonical; positivity of ev forces the dual
state cone inside (V^+)^*; membership of coev in ⊗_max forces the reverse
inclusion. [notes Prop "The dual is forced"]

**R2. Cup and cap conditions.** X is dualisable iff the one element
ψ = Σ_a f_a ⊗ f^a is both a positive state, ψ ∈ V^+_{X ⊗ X^∨} (cup), and a
positive effect, ψ ∈ (V^+_{X^∨ ⊗ X})^* (cap). The snake identities and
Z(S¹) = dim V then hold automatically from Vec. The cup wants the composite cone
large, the cap wants it small. [notes (cup), (cap); main.tex "the departure"]

**R3. The snake is exact teleportation.** Reading the snake in time: Alice and
Bob share ψ; Alice applies the effect ψ to the input and her share; Bob holds
the input. Resource and measurement are the same element. [notes Fig
"teleport"; C8, BBLW]

**R4. 2d positivity constraints.** A commutative Frobenius algebra
(A, μ, 1_A, ε) on the space of X = (V, V^+, u), with a swap-invariant composite
cone V^+_{XX}, defines a 2d GPTFT with Z(S¹) = X iff: disk 1_A ∈ V^+; reversed
disk ε ∈ (V^+)^*; pants μ(V^+_{XX}) ⊆ V^+; reversed pants Δ(V^+) ⊆ V^+_{XX}.
Consequences for any choice: V^+ is closed under the product (an ordered
algebra), and Δ(x) is positive on all product effects. The unit u never enters.
[notes Prop "Positivity constraints"]

**R5. The cone is weakly self-dual.** If X carries a 2d GPTFT then
β̂ : V → V^*, β̂(a) = ε(a ·), is a symmetric order isomorphism with
β̂(V^+) = (V^+)^*. Weak self-duality by a symmetric form is the gate; β need
not be an inner product. [notes Cor "The cone is weakly self-dual"; X6]

**R6. Spectrality and strong symmetry on examples.** Classical yes/yes,
quantum yes/yes, gbit no/no (its diagonals are 2-frames, two D₄-orbits,
spectrality fails off the diagonals), pentagon no/yes. Barnum–Hilgert's fn 10
says any regular n-gon with n > 3 is strongly symmetric; REORG-PLAN flags an
erratum claim for even n-gons. [REORG-PLAN §3; compare X13]

**R7. Worked examples that pass.** Classical simplex: all four constraints of
R4 hold, β positive-definite, φ = id, θ = (1, …, 1). Quantum Schur example:
Δ(ρ) = VρV† with V = Σ|ii⟩⟨i|, μ = Schur (entrywise) product, η(1) = J the
all-ones matrix, γ the Choi cup, special (h = id), Z(Σ_g) = N²; unoriented
extension φ = transpose, θ = 1, Z(RP²) = N; the composite cone is pinched from
both sides so "the quantum tensor product is selected by the 2d structure"; β
has signature (N(N+1)/2, N(N−1)/2), sharp only on the frame span.
[REORG-PLAN §6, computation queue]

**R8. Boxworld no-go, and a correction.** The gbit is weakly self-dual (a
linear T exists, even symmetric); the failure is the joint positivity of cup and
cap: there is no positive-definite self-dualising form. The earlier wording "no
linear map aligns the two" is false and was to be fixed. Because the cone is
polyhedral there is no continuous twist to rescue ψ. [REORG-PLAN §5; main.tex
conjectural target]

**R9. Reading of the 2d structure.** Pants = compare; copants = frame-
restricted broadcasting (no-broadcasting forbids only universal broadcasting,
G18). Two counits: ε (exact, non-causal) versus u (decoherence onto the frame
span). Positivity ledger P-η, P-ε, P-μ, P-Δ with D-cup, D-cap derived: the 1d
pinch recurs on maps. [REORG-PLAN §6; compare T18]

**R10. Programme ladder.** 1d ⇒ symmetric weak self-duality; + definiteness =
self-dual; 2d ⇒ frame + cone selection; + sharp + strong symmetry ⇒ Jordan via
Barnum–Hilgert. Headline: sharpness is the one postulate 2d topology does not
supply; it is BH's self-dualising inner product. [REORG-PLAN §6, §7]

**R11. Open problems and conjectures.** OP1 dualisability ⇒ weak self-duality?
OP2 unoriented symmetry + positivity ⇒ definiteness? (Minkowski: symmetry alone
insufficient) OP3 signature as an invariant; OP4 the global sector C ≠ 0; OP5 a
rigorous boxworld no-go. C1 frame + coherence-factor classification (R^k ⊕
C^m); C2 interface with BH Thm 1.1; C3 composite-cone selection and uniqueness;
C4 anchor: special commutative †-Frobenius = orthonormal basis (CPV, T17); C5
unoriented extension essentially unique. [REORG-PLAN §5–7]

## Presentation

**R12. Co-equal primitives collapse.** With states and effects as co-equal
primitives coupled by a separating pairing B_A, the flat map W_A → V_A^*,
w ↦ B_A(·, w), is an isomorphism (effects are functionals, the pairing is
evaluation), and a transformation's effect-side map is the transpose of its
state-side map. What survives of dropping no-restriction: the effect cone spans
V_A^* and contains u_A. Composites: V_{A□B} ≅ (V_A ⊗ V_B) ⊕ C with a global
sector C, zero iff tomographically local; the square product is
⊗|_local + C + a choice in [⊗_min, ⊗_max]. [main.tex Lemmas "Effects are
functionals", "A transformation is one map", Def "Simplified system", Obs
"GPT versus Vec"; compare P1]

**R13. GPT versus Vec.** Wide, non-full subcategory; Hom a cone; monoidal
product a family; duals as objects always, ev and coev as morphisms only if
positive. [main.tex Obs; notes §"GPT versus Vec"; C14]

## Candidates

**R14. Three post-quantum dualisable candidates.** OST, the T_H(a) families,
and DD(fHilb), each written on a fixed template (ambient space and pairing;
unipartite cones and unit; bipartite cones and the rule for higher n;
transformations; duality data (η, ε, c) with (ε ⊗ id)(id ⊗ η) = c·id; symmetry
group; post-quantum witness; references), with a comparison table and three
open points before a Frobenius (2d) feasibility question can be posed:
transformations for OST and T_H(a) must be fixed (adopted: cone-CP relative to
the induced cones); T_H(a) needs S₂-symmetrisation; the closed forms for
DD(fHilb) must be checked against the diagrams. The sources are now filed (DLG,
DG, GS-DH) and the examples are E10–E12. [candidates file, all sections]

## Locked framings that were retired

**R15.** Ambient-space-first, unnormalised cone canonical, Vec analogy only,
unoriented bordisms as default, terminology from Barnum–Hilgert and
Selby–Scandolo–Coecke. Of these, only the first two returned, as provisional
convention P1 (2026-09-07); the rest are still not assumed. [REORG-PLAN header]

**R16. Retired bibliography additions.** Barnum–Hilgert, SSC, Turaev–Turner,
Barnum–Müller–Ududec, Barnum–Graydon–Wilce, Coecke–Pavlović–Vicary. All now
filed in `sources/papers/`; none is in `draft.bib`. [REORG-PLAN "Bibliography
additions"]
