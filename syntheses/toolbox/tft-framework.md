---
status: draft
last-reviewed: 2026-09-04
sources:
  - sources/papers/170516 - introductory lectures on topological quantum field theory/paper.md
  - paper/draft.tex
machine-written: true
---

# Toolbox: topological field theory

Definitions and results the TFT side of the paper can use, as stated in
Carqueville–Runkel (CR, filed), cited by statement number. Nothing here is a
project convention: dimension, orientation and target category are open
(`conventions/domain/standing-assumptions.md`, "not assumed"). Where the
extraction lost an equation the statement is paraphrased in words; check against
the PDF before quoting.

## Definitions

**T1. The bordism category Bord_n** [CR §2.2]. Objects: oriented closed
(n−1)-dimensional manifolds E, "a toy model of a spacial slice of an
n-dimensional spacetime". A morphism E → F is an equivalence class of bordisms:
an oriented compact n-manifold M with boundary and smooth maps
ι_in : E → M ← F : ι_out whose disjoint union Ē ⊔ F → ∂M is an
orientation-preserving diffeomorphism, Ē being E with the opposite orientation.
Two bordisms are equivalent if an orientation-preserving diffeomorphism M → M′
commutes with the boundary maps: "this is how the smooth geometric structure is
discarded". Composition is gluing along F. Symmetric monoidal under disjoint
union, with unit ∅.

**T2. TFT** [CR Def 2.1]. An n-dimensional oriented closed TFT is a symmetric
monoidal functor Z : Bord_n → Vect_k. The Atiyah–Segal axioms are recovered as
data Y (a vector space per object, a vector per bordism ∅ → E, isomorphisms
Y(E ⊔ F) ≅ Y(E) ⊗ Y(F)) subject to: (a) the cylinder E × [0,1] is a
nondegenerate copairing on Y(E) ⊗ Y(Ē); (b) cutting M along an embedded closed
U and contracting with the dual pairing recovers Y(M), the "sum over
intermediate states"; (c) disjoint unions of bordisms go to tensor products;
(d) compatibility with the symmetries [CR Lemma 2.4, Remark 2.5]. Functoriality
is the gluing law: Z(M₂ ⊔_F M₁) = Z(M₂) ∘ Z(M₁) [CR (2.21)].

**T3. Finite-dimensionality and duality** [CR Prop 2.6]. For any TFT, Z(E) is
finite-dimensional and Z(Ē) ≅ Z(E)*. Source of both: the cylinder read as
∅ → Ē ⊔ E and as E ⊔ Ē → ∅ is a dual pair. "Proposition 2.6 is the main reason
why TQFTs are comparably manageable" [Remark 2.7].

**T4. Frobenius algebra** [CR Def 3.7, and the "economy version"]. A vector
space A with an associative unital algebra structure (μ, η) and a coassociative
counital coalgebra structure (Δ, ε) satisfying the Frobenius relation.
Equivalently [Prop 3.10]: a unital associative algebra with a nondegenerate
invariant bilinear form, ⟨a, b⟩ = ε(ab). Commutative ones form comFrob_k.

## Results

**T5. One dimension** [CR Thm 3.1, 3.2, 3.4]. Bord_1 is freely generated as a
symmetric monoidal category by two objects •₊, •₋ and two morphisms, a cup
∅ → •₊ ⊔ •₋ and a cap •₋ ⊔ •₊ → ∅ (orientations as in CR (3.12)), subject to
the zigzag ("Zorro") relations. Hence 1d TFTs correspond to finite-dimensional
vector spaces via Z ↦ Z(•₊), and as groupoids to dual pairs
(U, V, b : k → U ⊗ V, d : V ⊗ U → k) satisfying the Zorro moves; morphisms of
dual pairs are automatically invertible. CR: "1-dimensional TQFTs are boring:
finite-dimensional vector spaces with no further structure."

**T6. Two dimensions** [CR Thm 3.5, 3.6, Prop 3.8]. Bord_2 is freely generated
by S¹ and four elementary bordisms (cap, cup, pair of pants, copants) subject
to relations (3.26)–(3.29): unit and counit, associativity and coassociativity,
the Frobenius relation, commutativity. 2d TFTs Bord_2 → Vect_k are equivalent,
as groupoids, to commutative Frobenius algebras, via Z ↦ Z(S¹).

**T7. Changing the target** [CR Remark 3.9]. The proof of T6 generalises:
symmetric monoidal functors Bord_2 → C, for any symmetric monoidal category C,
are equivalent to commutative Frobenius algebras internal to C. This is the
statement a GPT-valued version of the paper would use; the target C would have
to be a symmetric monoidal category of GPT systems and processes, which is not
fixed (see `gpt-framework.md`).

**T8. Invariants** [CR Prop 2.9, 2.10; formulas lost in extraction, check].
Closed n-manifolds give numbers. If dim Z(Sⁿ⁻¹) = 1 then Z(Sⁿ) ≠ 0 and
connected sums factorise, Z(M # N) = Z(M) Z(N) / Z(Sⁿ) for connected M, N.

**T9. Beyond closed TFTs** [CR Thm 3.12]. Extended 3d TFTs Bord_{3,2,1} →
LinCat are classified by anomaly-free modular tensor categories (k
algebraically closed). Out of the draft's scope; recorded because "TFT" in the
title could mean the extended notion. TODO Pedro: closed or extended.

**T10. Variants** [CR Remark 2.3]. Bordisms may carry a metric, a conformal
structure, a spin structure, a framing, boundaries, defects; each gives a
different functorial QFT. Unoriented bordisms are a further variant not
treated in CR. Not fixed for this project.

## How this bears on the draft

- CR's own gloss of the functor picture is "a way of transporting the geometric
  and dynamical structure of spacetime into the algebraic description of
  physical states and observables", a map "geometry → algebra" [CR §2.2]. In
  this language premise (ii) of standing assumption A6 (a local dynamical law
  propagates a region to its causal development) is the existence of Z on
  bordisms together with the gluing law, and premise (i) is the monoidal
  structure, disjoint union ↦ tensor product. Machine-written reading;
  UNVERIFIED as the paper's intended formalisation.
- What "TFT valued in GPTs" needs is a symmetric monoidal category of GPT
  systems (T7). The choices that forces, and the standard candidates, are in
  `gpt-framework.md`.
- T3 says any TFT-valued system is finite-dimensional and self-dual up to
  orientation reversal. For a GPT target this becomes a constraint on the state
  cones, which is presumably where B9's results live. UNVERIFIED; the draft says
  nothing yet.
