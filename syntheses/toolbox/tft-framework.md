---
status: draft
last-reviewed: 2026-09-11
sources:
  - sources/papers/170516 - introductory lectures on topological quantum field theory/paper.md
  - sources/papers/950305 - higher-dimensional algebra and tqft/paper.md
  - sources/papers/140627 - short-range entanglement and invertible field theories/paper.md
  - sources/papers/160422 - reflection positivity and invertible topological phases/paper.md
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

## Locality and unitarity as the sources state them (added 2026-09-11)

Continues the T-labels; these four are what
`pipeline/spacetime-reading-of-the-axioms.md` rests on.

**T27. Cutting and gluing is exactly the duality data** [CR Lemma 2.4]. Let Y
assign a vector space Y(E) to each object of Bord_n, a linear map k → Y(E) to
each bordism M : ∅ → E, and isomorphisms Y(E ⊔ F) ≅ Y(E) ⊗ Y(F). Then Y extends
to a symmetric monoidal functor Bord_n → Vect_k if and only if (a)
Y(E × [0,1]) ∈ Y(E) ⊗ Y(Ē) is a nondegenerate copairing, giving a unique dual
pairing d_E : Y(Ē) ⊗ Y(E) → k, and (b) for U a closed oriented (n−1)-manifold
embedded in M, with M′ : ∅ → E ⊔ U ⊔ Ū obtained by cutting M along U, Y(M) is
Y(M′) followed by contraction with d_U (and a disjointness clause). CR's own
remark [§2.2(v)]: the gluing law of a functor composes disjoint manifolds, while
cutting a bordism need not produce disjoint pieces; the duality data repair the
mismatch.

**T28. Two levels of duality in nCob, conceptually independent** [BD §2].
"In nCob each object x is an oriented (n−1)-manifold, and its dual x* is the
same manifold with its orientation reversed. Second, each morphism f : x → y is
an oriented n-manifold with boundary, and its dual f† : y → x is the same
manifold with its orientation reversed." The adjoint f* : y* → x* is derived
from duality on objects; the dual morphism f† is "conceptually independent". A
unitary TQFT is a rigid symmetric monoidal functor to Hilb with Z(f†) = Z(f)†
[BD §2; compare Sawin Def 2, T11]. So compactness and the dagger of Bord are
two separate structures, matching the project's dimension-one and
dimension-two conditions.

**T29. Full locality and reconstruction from a point** [Freed §2.1, §5].
"A theory which extends in this way is fully local, and it is natural to make
this strong locality hypothesis for the effective topological theory which
comes from a gapped physical theory." On the cobordism hypothesis: "the idea is
that any n-manifold is glued together from balls, so that if the theory is
fully local then its values can be reconstructed from those on a point." The
classification of fully local theories by fully dualisable objects is Lurie's;
Lurie is NOT FILED and must not be cited from memory.

**T30. Reflection positivity: what is structure and what is condition**
[FH §1]. "The twin pillars of quantum field theory are locality and unitarity.
These fundamental properties persist after Wick rotation: locality manifests as
factorization laws for correlation functions and unitarity manifests as
reflection positivity. Locality is encoded in the Axiom System using composition
of morphisms: gluing bordisms along codimension one submanifolds." And: "(i)
'reflection' and 'positivity' are distinct; (ii) 'reflection' is a structure
whereas 'positivity' is a condition"; a reflection structure is equivariance
data for the orientation-reversal involution, it "induces a hermitian metric on
the vector space of states attached to an (n−1)-manifold, and positivity is the
condition that these hermitian structures be positive definite"; equivalently
"the partition function of the double of a manifold with boundary must be
positive". Extends T25.
