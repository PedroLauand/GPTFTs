---
status: draft
last-reviewed: 2026-09-07
sources:
  - sources/papers/930809 - unitary topological field theories in two dimensions/paper.md
  - sources/papers/950523 - direct sum decompositions and indecomposable tqfts/paper.md
  - sources/papers/060905 - d-branes and k-theory in 2d topological field theory/paper.md
  - sources/papers/081005 - a new description of orthogonal bases/paper.md
  - sources/papers/050613 - unoriented tqft and link homology/paper.md
  - sources/papers/160422 - reflection positivity and invertible topological phases/paper.md
  - sources/papers/140627 - short-range entanglement and invertible field theories/paper.md
machine-written: true
---

# Toolbox: unitary 2d TFTs

Continues `tft-framework.md` (T1–T10). The focus Pedro set on 2026-09-07:
unitary 2d TFTs, their commutative semisimple Frobenius algebras, and what a
GPT must have to carry one. Sources: Durhuus–Jonsson (DJ), Sawin, Moore–Segal
(MS), Coecke–Pavlović–Vicary (CPV), Turaev–Turner (TT), Freed–Hopkins (FH),
Freed. Project results R4–R11 are the retired notes' attempt at the GPT side.

**T11. Unitary TFT.** A tensor functor Z : Cob(d) → Hilb with Z(M^*) = Z(M)^*
for the orientation-reversed bordism [Sawin Def 2]. DJ's axioms for d = 2:
finite-dimensional Hilbert spaces H_Σ; partition vectors Z(S) ∈ H_∂S; unitary
maps for orientation-preserving diffeomorphisms; H_{Σ^*} = H_Σ^* through a
non-degenerate bilinear form; a conjugate-linear involution with
Z(S^*) = Z(S)^*; factorisation over disjoint unions; gluing = contraction; the
cylinder is the identity [DJ §2, axioms 1–4]. In Euclidean language unitarity
is a reality condition plus reflection positivity; "reflection is a structure
whereas positivity is a condition" [Freed §"unitarity"; FH §1].

**T12. Z(S^{d−1}) is a commutative Frobenius algebra; unitary makes it C*.**
For any TQFT, Z of the sphere is a commutative Frobenius algebra acting on every
Z(Σ); if unitary, a commutative C*-Frobenius algebra with C*-representations.
[Sawin Prop 1]

**T13. Direct sums and decomposition.** Direct sum of theories: Z₁(Σ) ⊕ Z₂(Σ)
on connected Σ, partition functions added [DJ §4; Sawin]. Z based on
A = A₁ ⊕ A₂ splits as Z₁ ⊕ Z₂ and conversely; the same for unitary theories and
C*-Frobenius algebras [Sawin Thm 1]. Every unitary TQFT (any d) is a direct sum
of theories with one-dimensional Z(S^{d−1}) [Sawin Cor 1]; every TQFT is a
direct sum of simple and nilpotent theories [Sawin Cor 2].

**T14. Indecomposable commutative Frobenius algebras.** Exactly the
one-dimensional S_λ (k with ε(1) = λ) and the nilpotent N_{A,μ}; a commutative
Frobenius algebra is semisimple iff it is a direct sum of S_λ's. Nonunitary
indecomposables are degenerate: every bordism of genus ≥ 2 is sent to zero, so
a TQFT is not determined by its closed values in general (the unitary case is
open there). [Sawin Prop 2, §1]

**T15. Classification of unitary 2d TFTs.** A unitary 2d TFT is determined up
to equivalence by n positive reals λ₁, …, λ_n, the eigenvalues of the
Hermitian handle operator H = Z_{1,2} (two three-holed spheres glued), with
n = dim H_{S¹} and Z_g = Σ_i λ_i^{g−1}; in a canonical basis
Z_{0,3} = Σ_i √λ_i x_i ⊗ x_i ⊗ x_i, Z_{0,2} = Σ x_i ⊗ x_i, Z_{0,1} = Σ λ_i^{−1/2} x_i.
The theory is a direct sum of one-dimensional theories Z_g = λ^{g−1}; the
closed partition functions determine it; every unitary 2d TFT is "effectively
real" (H = H_R ⊕ iH_R). Constructed on triangulated surfaces with vertex
colours and weights N_i, giving Z(S) = Σ N_i^{χ(S)}. [DJ abstract, §3, §4]

**T16. Semisimple = functions on a finite set with a measure.** A semisimple
Frobenius algebra "is automatically the algebra of complex-valued functions on
a finite set X = Spec(C), the 'space-time', equipped with a 'volume-form' or
'dilaton field' θ" [MS §1]. Semisimplicity ⇔ the fusion rules are
simultaneously diagonalisable ⇔ there are basic idempotents ε_x with
C = ⊕ Cε_x, ε_x ε_y = δ_xy ε_x; the weights θ_x are the only invariant of a
finite-dimensional commutative semisimple Frobenius algebra [MS §3.1]. There is
exactly one 2d TQFT per commutative Frobenius algebra and exactly one unitary
2d TQFT per commutative C*-Frobenius algebra (Dijkgraaf) [Sawin Thm 2].

**T17. Orthonormal bases are Frobenius algebras.** Commutative †-Frobenius
monoids in FdHilb correspond exactly to orthogonal bases, by copying
δ(|φ_i⟩) = |φ_i⟩ ⊗ |φ_i⟩ and deleting; the monoid is special iff the basis is
orthonormal; every †-Frobenius monoid in FdHilb is a C*-algebra; the category of
commutative †-Frobenius monoids with comonoid maps is equivalent to FinSet.
[CPV Thm 5.1, Cor 4.3, 7.2] "Classical structures" in categorical quantum
mechanics.

**T18. The bridge to GPTs (machine-written reading).** T15–T17 say the same
thing in three languages: a unitary 2d TFT is a classical system Cl_n with a
weight per point, its idempotents ε_x are a maximal frame (X11), and its
comultiplication copies them and nothing else. In house terms the frame is
perfectly distinguishable and the copants is broadcasting restricted to the
frame, which no-broadcasting permits (G18, last sentence). So "which GPTs admit
a unitary 2d TFT" asks which GPTs have (i) a frame spanning V, (ii) a positive
copying map for it, (iii) a self-dualising pairing β = ε ∘ μ compatible with the
cone (R5). The retired notes' ledger R4 and examples R7, R8 are the first pass;
the boxworld no-go R8 and the pentagon are the test cases to redo from filed
sources. UNVERIFIED as a theorem; a discussion agenda.

**T19. Unoriented 2d TFTs.** Classified by extended Frobenius algebras: a
commutative Frobenius algebra with an involution φ and an element θ (the
crosscap) such that φ(θv) = θv and μ(φ ⊗ id)Δ(1) = θ². [TT Def 2.5, Prop 2.9,
Lemma 2.8] Lower priority per Pedro (2026-09-07); the retired notes' unoriented
default is not assumed (R15).

**T20. Positivity versus semisimplicity.** Sawin's nilpotent indecomposables
are exactly what unitarity excludes; positivity of the handle operator's
spectrum (DJ) is the mechanism. The GPT analogue is the pants and copants
positivity in R4, which forces the frame structure of T18. Whether a GPT
positivity condition implies semisimplicity of Z(S¹) in general is open. TODO.
