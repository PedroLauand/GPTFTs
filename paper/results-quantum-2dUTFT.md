---
status: calculation
created: 2026-09-07
entered-by: agent, on Pedro's instruction (chat of 2026-09-07)
last-reviewed: 2026-09-07
feeds: results-narrative-2d.md, Section 3
machine-written: true
---

# From a unitary 2d TFT in FHilb to a 2d TFT in the GPT of quantum theory

The first calculation of the 2d programme, done in full for the one case where
everything is known: given a unitary two-dimensional TFT valued in
finite-dimensional Hilbert spaces, construct a two-dimensional TFT valued in
the GPT of quantum theory, and read off the real Frobenius algebra on the
ambient space. No interpretation; that is Pedro's, later. Checks are marked
✓ when carried out below, TARGET when not. House notation
(`conventions/domain/notation.md`); sources by statement number, toolbox
labels G, T, R stable.

---

## 0. Conventions

**FHilb.** Finite-dimensional complex Hilbert spaces and linear maps; dagger =
adjoint; compact closed; scalars C. [CHK Def 1.3–1.5; Selinger Def 2.6]

**Bord_2 and the four generators** η : ∅ → S¹ (disk), μ : S¹ ⊔ S¹ → S¹
(pants), Δ : S¹ → S¹ ⊔ S¹ (copants), ε : S¹ → ∅ (reversed disk), with the
unit, (co)associativity, commutativity and Frobenius relations [CR Thm 3.6;
T6]. A 2d TFT valued in a symmetric monoidal C is a commutative Frobenius
algebra internal to C on Z(S¹) [CR Thm 3.5, Rem 3.9; T7].

**Unitary 2d TFT in FHilb.** Z : Bord_2 → FHilb symmetric monoidal with
Z(M̄) = Z(M)† for the orientation-reversed bordism [Sawin Def 2; DJ §2]. Then
(Z(S¹), μ, η) is a commutative †-Frobenius algebra, Δ = μ†, ε = η† [Sawin Prop
1; CHK Def 2.1], and by CPV Thm 5.1 it is determined by an orthogonal basis
[T17]. Classification: n = dim Z(S¹) positive weights, unique up to unitary
equivalence [DJ §3; Sawin Thm 2; T15].

**Weighted normal form.** Orthonormal basis {|i⟩}_{i=1..N} of H = Z(S¹),
weights θ_i > 0:

    μ(|i⟩⊗|j⟩) = δ_ij θ_i^{-1/2} |i⟩        η(1) = Σ_i θ_i^{1/2} |i⟩
    Δ(|i⟩)     = θ_i^{-1/2} |i⟩⊗|i⟩          ε(|i⟩) = θ_i^{1/2}

with Δ = μ†, ε = η†. Checks ✓ (all maps are basis-diagonal): unit
μ(η⊗id)(|j⟩) = Σ_i θ_i^{1/2} δ_ij θ_j^{-1/2} |j⟩ = |j⟩; associativity and
commutativity trivially; Frobenius (μ⊗id)(id⊗Δ)(|i⟩⊗|j⟩) =
δ_ij θ_j^{-1} |j⟩⊗|j⟩ = Δμ(|i⟩⊗|j⟩). Pairing β(|i⟩,|j⟩) = εμ(|i⟩⊗|j⟩) = δ_ij:
the Frobenius pairing is the inner product on the real span of the basis (DJ's
canonical basis). Handle operator h = μΔ = diag(θ_i^{-1}); closed surfaces
Z(Σ_g) = ε h^g η(1) = Σ_i θ_i^{1−g}, matching DJ (28) with λ_i = θ_i^{-1}.
Special (μμ† = id) iff all θ_i = 1, then Z(Σ_g) = N for every genus.

## 1. The target: the GPT of quantum theory as a symmetric monoidal category

- Objects Q_N = (Herm_N, PSD_N, tr): ambient real space V = Herm_N,
  dim_R V = N², complexification V ⊗ C = M_N(C) = End(H). [G20]
- Morphisms: completely positive maps Φ : M_N → M_M, which preserve Herm and
  map PSD_N into PSD_M. The category is cone-linear (Hom is a cone); channels
  are the trace-preserving ones; a TFT needs only morphisms, scalars are free.
- Monoidal product Q_N ⊗ Q_M = Q_{NM} with PSD_{NM} ⊂ Herm_N ⊗ Herm_M ≅
  Herm_{NM}; swap the flip. This is the density-operator composite, strictly
  between ⊗_min and ⊗_max [M Ex 17; G12, G20]. Scalars End(Q_1) = R_{≥0}.
- Identification: this is the real form of CPM(FHilb) [Selinger §4; CHK §1]:
  objects H, morphisms CP maps End(H) → End(K); restricting to Hermitian parts
  gives (Q, ⊗). Complete positivity is Choi's theorem in categorical form
  [Selinger Def 4.11, Lemma 4.12, Cor 4.13].

## 2. The doubling functor

D : FHilb → CPM(FHilb), D(H) = H, D(f)(X) = f X f† (Kraus rank one; Selinger's
functor F with F(A) = A, F(f) = f_* ⊗ f). Facts, from Selinger §4.4 [Def 4.18
(CPM construction), Rem 4.19 (the functor), Thm 4.20 (CPM(C) is dagger compact
closed and F preserves the dagger compact closed structure)]: D(g∘f) = D(g)∘D(f);
D(f ⊗ g) = D(f) ⊗ D(g) under End(H ⊗ K) ≅ End(H) ⊗ End(K); D(σ) = the flip;
D(f†) = D(f)†; D(f) is completely positive; on scalars D(z) = |z|². Hence D is a
dagger symmetric monoidal functor, and every D(f) maps PSD into PSD and Herm
into Herm. ✓ [Selinger Thm 4.20; the filed preliminary version carries the same
statement numbers as the ENTCS version cited in R14]

## 3. The induced theory

Z_Q := D ∘ Z : Bord_2 → CPM(FHilb) ≅ (Q, ⊗).

A composite of symmetric monoidal functors is symmetric monoidal, so Z_Q is a
2d TFT valued in the GPT of quantum theory with Z_Q(S¹) = Q_N. ✓ This is the
existence statement.

Structure maps. Write E_ij = |i⟩⟨j|, V := μ† = Σ_i θ_i^{-1/2} |ii⟩⟨i| : H → H⊗H,
and index Herm_{N²} = Herm(H⊗H) by pairs.

- μ_Q(X) = μ X μ† = V† X V, so (μ_Q X)_{ij} = θ_i^{-1/2} θ_j^{-1/2} X_{(ii),(jj)}.
  On products, μ_Q(A ⊗ B) = θ^{-1/2} (A ∘ B) θ^{-1/2} with A ∘ B the
  entrywise (Schur) product and θ^{-1/2} = diag(θ_i^{-1/2}). Only the
  (ii),(jj) block of X enters. ✓
- Δ_Q(ρ) = V ρ V† = Σ_ij θ_i^{-1/2} θ_j^{-1/2} ρ_ij |ii⟩⟨jj|. ✓
- η_Q(1) = |η⟩⟨η| = Σ_ij θ_i^{1/2} θ_j^{1/2} E_ij: rank one, PSD, trace Σ_i θ_i.
  For θ = 1 it is the all-ones matrix J. ✓
- ε_Q(ρ) = ⟨η|ρ|η⟩ = Σ_ij θ_i^{1/2} θ_j^{1/2} ρ_ij: a rank-one positive
  functional. ✓
- h_Q(ρ) = h ρ h, (h_Q ρ)_ij = θ_i^{-1} θ_j^{-1} ρ_ij. ✓
- Z_Q(Σ_g) = D(Z(Σ_g)) = |Z(Σ_g)|² = (Σ_i θ_i^{1−g})². Special case: N² for
  every genus; in particular Z_Q(T²) = N² = dim_R Herm_N, the categorical
  dimension of Q_N [T5]. ✓ [R7 confirmed for θ = 1]

The relations hold because D is a functor and they hold in FHilb. ✓

## 4. Positivity: the theory lands in the cones

Every Z_Q(M) = D(Z(M)) is completely positive, so for a bordism M from k
circles to l circles it maps PSD_{N^k} into PSD_{N^l} and Herm into Herm. In
particular η_Q(1) ∈ PSD_N (rank one); ε_Q ∈ PSD_N^* (⟨η|ρ|η⟩ ≥ 0);
μ_Q(PSD_{N²}) ⊆ PSD_N (V†XV); Δ_Q(PSD_N) ⊆ PSD_{N²} (VρV†). ✓ Nothing to check
beyond complete positivity: this is the sense in which the quantum case is the
default case plus structure, and it is what a general GPT will not give for
free.

Normalisation, not required by the TFT: for θ = 1, V is an isometry, so Δ_Q is
trace preserving and μ_Q trace non-increasing (V V† is the projector onto
span{|ii⟩}); η_Q and ε_Q carry the scalar Σ_i θ_i. So up to scalars the four
generators are allowed processes of the GPT.

Computed identities, recorded without commentary:
(id ⊗ tr) ∘ Δ_Q(ρ) = Σ_i θ_i^{-1} ρ_ii E_ii;  ε_Q ∘ η_Q = (Σ_i θ_i)²;
tr ∘ η_Q = Σ_i θ_i;  Δ_Q(|+⟩⟨+|) = |Φ⁺⟩⟨Φ⁺| for N = 2, θ = 1.

## 5. The real Frobenius algebra on the ambient space: Herm_N ≅ R^N ⊕ C^{N(N−1)/2}

Over C. The matrix units satisfy μ_Q(E_ij ⊗ E_kl) = δ_ik δ_jl θ_i^{-1/2}
θ_j^{-1/2} E_ij ✓, so ê_ij := θ_i^{1/2} θ_j^{1/2} E_ij are N² orthogonal
idempotents (ê_ij ∘ ê_ij = ê_ij, ê_ij ∘ ê_kl = 0 otherwise) with
ε_Q(ê_ij) = θ_i θ_j. Hence (M_N(C), μ_Q, η_Q, Δ_Q, ε_Q) is the N²-point
classical structure with weights θ_i θ_j, and Z_Q(Σ_g) = Σ_ij (θ_i θ_j)^{1−g}
= (Σ_i θ_i^{1−g})² ✓ consistent with §3. With respect to the Hilbert–Schmidt
inner product on M_N(C) the ê_ij are orthogonal, so **the complexified ambient
space carries a unitary 2d TFT in the Durhuus–Jonsson sense: the N²-point
classical structure, unique up to basis and weights.** ✓

Real form. Herm_N is the fixed-point set of the antilinear involution
τ(X) = X†. τ respects the structure: (X ∘ Y)† = X† ∘ Y†, τ(η_Q(1)) = η_Q(1),
ε_Q(X†) = conj(ε_Q(X)) ✓; on idempotents τ(ê_ij) = ê_ji, fixing the N diagonal
ones and swapping the N(N−1)/2 pairs. Fixed-point algebra:

    R·ê_ii  (i = 1..N)   ⊕   for each i < j the real plane
    P_ij := ê_ij + ê_ji ,  Q_ij := i(ê_ij − ê_ji),   with
    P ∘ P = P,  P ∘ Q = Q,  Q ∘ Q = −P   (so the plane is C with P = 1, Q = i). ✓

Hence, as real commutative Frobenius algebras,

    Herm_N ≅ R^N ⊕ C^{N(N−1)/2},   k = N,  m = N(N−1)/2,  k + 2m = N². ✓

Pairing on the real form (θ = 1): β_Q(X, Y) = ε_Q μ_Q(X ⊗ Y) = Σ_ij X_ij Y_ij
= tr(X Yᵀ) = ⟨X̄, Y⟩_HS, the Hilbert–Schmidt pairing twisted by conjugation.
β_Q(P, P) = 2, β_Q(Q, Q) = −2. Signature (N(N+1)/2, N(N−1)/2): positive on
real symmetric matrices, negative on imaginary antisymmetric ones. ✓ [R7
confirmed] So the real form is semisimple but not Durhuus–Jonsson-unitary over
R; unitarity lives over C, where β_Q is the restriction of the Hilbert–Schmidt
inner product composed with conjugation.

## 6. The qubit, θ = 1, in full

V = |00⟩⟨0| + |11⟩⟨1|. μ_Q(A ⊗ B) = A ∘ B; Δ_Q(ρ) = Σ_{i,j∈{0,1}} ρ_ij |ii⟩⟨jj|;
η_Q(1) = J = 2|+⟩⟨+|; ε_Q(ρ) = Σ_ij ρ_ij = 2⟨+|ρ|+⟩; h_Q = id; Z_Q(Σ_g) = 4.
Unit law: J ∘ ρ = ρ ✓. Frobenius on E_ij ⊗ E_kl: both sides equal
δ_ik δ_jl E_ij ⊗ E_ij ✓. Real algebra on the Pauli basis: idempotents
E_00 = (𝟙+Z)/2, E_11 = (𝟙−Z)/2; the plane (X, Y) with X ∘ X = X, X ∘ Y = Y,
Y ∘ Y = −X ✓. So Herm_2 ≅ R² ⊕ C. β_Q on {𝟙, X, Y, Z}: diagonal
(2, 2, −2, 2), signature (3, 1) ✓. Δ_Q(|+⟩⟨+|) = ½ Σ_ij |ii⟩⟨jj| = |Φ⁺⟩⟨Φ⁺| ✓.

## 7. Established and not

Established ✓: every unitary 2d TFT in FHilb induces, by doubling, a 2d TFT
valued in the GPT of quantum theory with the standard composite; its real
Frobenius algebra on the ambient space is R^N ⊕ C^{N(N−1)/2}; positivity is
automatic because the structure maps are completely positive; the complexified
ambient space carries the unique (up to basis and weights) unitary theory and
the GPT is a real form of it.

TARGET (a), converse: is every 2d TFT valued in (Q, ⊗) with Z(S¹) = Q_N of the
form D ∘ Z? Treated in §9: proved for N = 2, reduced for general N.

TARGET (b), nondegeneracy forces the coherences: the decohered candidate
μ′(A ⊗ B) = Σ_i A_ii B_ii E_ii, η′(1) = 𝟙, ε′ = tr, Δ′(ρ) = Σ_i ρ_ii E_ii ⊗ E_ii
satisfies the Frobenius relation but β′(X, Y) = Σ_i X_ii Y_ii is degenerate on
Herm_N (it kills the off-diagonal directions). It is therefore a 2d TFT with
Z(S¹) = Cl_N, not Q_N. Any 2d TFT with Z(S¹) = Q_N must give the off-diagonal
directions a nondegenerate pairing: that is what the C-summands do. To prove
in general.

TARGET (c): which notion of unitarity the paper adopts for GPT-valued theories.
Here the natural one is "induced from a unitary FHilb theory", equivalently
Durhuus–Jonsson unitarity of the complexification. Pedro to decide, with the
interpretation.

## 8. Template for a general GPT (my reading of Pedro's plan; confirm)

Given X = (V, V^+, u), dim_R V = d.

1. Complexify: V_C = V ⊗ C ≅ C^d carries, for any basis {b_a} and weights, the
   d-point classical structure, a unitary 2d TFT for the inner product making
   the basis orthogonal, unique up to these choices [DJ; CPV Thm 5.1].
2. Real form: V is the fixed-point set of the antilinear involution τ =
   conjugation with respect to V. If τ permutes the chosen basis, fixing k
   vectors and swapping m pairs, the classical structure restricts to a real
   commutative Frobenius algebra V ≅ R^k ⊕ C^m with k + 2m = d. If τ does not
   permute the basis, the structure maps do not preserve V and there is no
   real theory on V from that basis.
3. Positivity: choose the composite cones V^+_{X^{⊗n}} and check η(1) ∈ V^+,
   ε ∈ (V^+)^*, μ(V^+_{XX}) ⊆ V^+, Δ(V^+) ⊆ V^+_{XX}, and that every value of
   the functor is completely positive for the chosen cones. For quantum theory:
   basis = matrix units, τ = †, (k, m) = (N, N(N−1)/2), composite = PSD,
   positivity automatic.
4. Record the invariants: (k, m), the weights, the signature of β, Z(Σ_g).

First cases after quantum theory: Cl_n (k = n, m = 0 is the obvious real form;
are there admissible ones with m > 0?); then the dualizable candidates E10–E12
and the Jordan algebras that pass the 1d test.

---

## 9. The converse: from CPM(FHilb) back to FHilb

**Setting.** Z_Q : Bord_2 → CPM(FHilb) symmetric monoidal, Z_Q(S¹) = H,
dim H = N. Its structure maps are CP: η_Q(1) = ρ ≥ 0; ε_Q = tr(E ·) with
E ≥ 0; μ_Q = Σ_a K_a (·) K_a† with K_a : H⊗H → H; Δ_Q = Σ_b D_b (·) D_b† with
D_b : H → H⊗H. Question: is Z_Q = D ∘ Z̃ for some Z̃ : Bord_2 → FHilb?

**Purification is the wrong tool.** A Stinespring dilation writes each CP map
as D(V) followed by discarding an environment, and discarding is not in the
image of D (its Kraus rank is dim E). A lift exists iff the structure maps
already have Kraus rank one. The Frobenius axioms force this, at least for
N = 2; no environment is ever needed.

Two facts used throughout. (F1) The identity channel has Kraus rank one: if
Σ_i F_i X F_i† = X for all X then every F_i = f_i 𝟙 with Σ_i |f_i|² = 1.
(F2) Frobenius nondegeneracy: β(X, ·) = 0 implies X = 0.

**Lemma 9.1 (the unit is pure).** Write ρ = Σ_r p_r |r⟩⟨r|. The unit law
μ_Q(ρ ⊗ X) = X and (F1) give K_a(|r⟩ ⊗ v) = α_{ar} v for every a and every r
in the support. Hence μ_Q(|r⟩⟨r| ⊗ X) = λ_r X with λ_r = Σ_a |α_{ar}|², so
β(|r⟩⟨r| − λ_r ρ, Y) = 0 for all Y and by (F2) |r⟩⟨r| = λ_r ρ. A rank-one
operator proportional to ρ forces rank ρ = 1. ✓ Normalise ρ = |η⟩⟨η| with
‖η‖ = 1; the rescaling (μ, η, Δ, ε) ↦ (μ/t, tη, tΔ, ε/t) preserves the axioms.

**Lemma 9.2 (the counit is pure).** E = Σ_j q_j |e_j⟩⟨e_j|, P the projector
onto supp E. The two counit laws with (F1) give (𝟙 ⊗ ⟨e_j|) D_b ∝ 𝟙 and
(⟨e_j| ⊗ 𝟙) D_b ∝ 𝟙, hence (𝟙 ⊗ P) D_b v = v ⊗ w_b and (P ⊗ 𝟙) D_b v = w'_b ⊗ v
with w_b, w'_b ∈ supp E, and therefore (Pv) ⊗ w_b = w'_b ⊗ (Pv) for all v. If
dim supp E ≥ 2, a v ∈ supp E not parallel to w_b forces w_b = 0 for every b,
contradicting the normalisation Σ_{b,j} |a_{bj}|² = 1 from (F1). So
E = q |e⟩⟨e|. ✓

**Lemma 9.3 (cup and cap are pure).** The Frobenius structure makes the
object self-dual in CPM with cup γ = Δ_Q(ρ) ≥ 0 and cap B ≥ 0, β(W) = tr(BW),
satisfying the snake (id ⊗ β)(γ ⊗ id) = id. With γ = Σ_i |g_i⟩⟨g_i| and
B = Σ_j |b_j⟩⟨b_j| the snake is the identity channel whose Kraus operators are
the partial contractions ⟨b_j|g_i⟩ : H → H, each a multiple of 𝟙 by (F1); two
non-proportional g_i cannot both contract to multiples of 𝟙 against the same
b_j, so γ and B are rank one. ✓ This is the CPM form of R1–R2: the cup is a
scaled maximally entangled vector, the cap its Choi–Jamiołkowski inverse.

**Lemma 9.4 (equal Kraus ranks).** Δ_Q = (id ⊗ μ_Q)(γ ⊗ id) and
μ_Q = (id ⊗ β)(Δ_Q ⊗ id) with γ, B pure give a Kraus decomposition of each map
from the other's, so rank_K μ_Q = rank_K Δ_Q. ✓

**Proposition 9.5 (N = 2: Kraus rank one).** Choose the basis with η = |0⟩.
By (F1) and a unitary change of Kraus operators, K_1(|0⟩ ⊗ v) = v and
K_j(|0⟩ ⊗ v) = 0 for j ≥ 2. The right unit law then gives K_1(v ⊗ |0⟩) = v and
K_j(v ⊗ |0⟩) = 0, so K_j = |x_j⟩⟨11| and Σ_{j≥2} K_j X K_j† = ⟨11|X|11⟩ R with
R = Σ_j |x_j⟩⟨x_j| ≥ 0. Write K_1(|1⟩ ⊗ v) = B v with B|0⟩ = |1⟩, B|1⟩ = y:
K_1 is the product of the algebra C[t]/(t² − y_1 t − y_0) on {|0⟩ = 1,
|1⟩ = t}, commutative and associative by itself. CP-associativity says the
Kraus families {K_a(K_b ⊗ 𝟙)} and {K_a(𝟙 ⊗ K_b)} are related by a unitary W;
evaluated on |00⟩ ⊗ v this gives W_{ab,11} = δ_{a1} δ_{b1}, so K_1(K_1 ⊗ 𝟙) =
K_1(𝟙 ⊗ K_1) and the families with (a, b) ≠ (1, 1) define the same CP map. On
inputs |1⟩ ⊗ |1⟩ ⊗ w that equality forces (B − y_1) R = 0; since B ≠ y_1 𝟙,
R = r |x⟩⟨x| with (B − y_1) x = 0, which gives y_0 = 0 and x ∝ |1⟩. The
remaining Kraus operators then all have image C|1⟩, and their scalar trilinear
forms, in the monomial basis {u_1v_1w_0, u_1v_1w_1, u_0v_1w_1, u_1v_0w_1},
have Gram matrices that agree except in the (u_1v_1w_0, u_1v_0w_1) entry, 0 on
one side and r on the other. Hence r = 0: μ_Q = K_1 (·) K_1† has Kraus rank
one, and by 9.4 so does Δ_Q. ✓ (Computation to be re-checked by hand; it uses
only unit, commutativity and associativity.)

**Lemma 9.6 (rank one lifts, up to a phase theory).** If μ_Q = D(K),
Δ_Q = D(D̃), η_Q = D(η), ε_Q = D(e†), the axioms hold in FHilb up to phases.
Rephasing η fixes the left unit; commutativity K σ = e^{iγ} K forces
e^{2iγ} = 1, and γ = π would give K(η ⊗ η) = 0 against K(η ⊗ η) = η; associativity
and the Frobenius law evaluated on η have phase 1; rephasing D̃ fixes the
counit. So (H, K, η, D̃, e†) is a Frobenius algebra in FHilb and Z_Q = D ∘ Z̃.
The lift is unique up to tensoring with an invertible Euler theory
M ↦ λ^{χ(M)}, |λ| = 1, which is the kernel of D on theories. If Z_Q is a
dagger theory then Z̃(M̄) = e^{iφ(M)} Z̃(M)† with e^{iφ} an invertible theory,
hence λ^{χ}; dividing Z̃ by λ^{χ/2} makes it unitary (χ(M̄) = χ(M)). ✓

**Theorem 9.7 (N = 2).** Every 2d TFT valued in CPM(FHilb) with Z(S¹) = C² is
the doubling of a 2d TFT valued in FHilb. The dagger ones are the doublings of
unitary ones, that is of an orthogonal basis of C² with weights, and their real
form on Herm_2 is R² ⊕ C (§6). Non-dagger ones exist and are also doubled: the
doubling of a non-orthogonal idempotent basis (still R² ⊕ C as a real algebra,
β not from an inner product), and the doubling of the nilpotent algebra
C[t]/t², a local Frobenius algebra on End(C²) with Z_Q(Σ_g) = 0 for g ≥ 2:
Sawin's degenerate theories survive in the GPT. The dagger condition is what
selects the R^N ⊕ C^m of §5 with its classical-structure basis.

**TARGET 9.8.** Proposition 9.5 for general N. Available reduction: after
normalisation every K_j with j ≥ 2 vanishes on |η⟩ ⊗ H + H ⊗ |η⟩, so it lives
on η^⊥ ⊗ η^⊥, one-dimensional only for N = 2. Plan: use the decomposition of
(End(H), μ_Q) over C into local algebras together with the pure counit to show
the idempotents are rank-one operators, or find a counterexample at N = 3.

**Answer to the question posed.** One does not purify and then redefine; the
Frobenius axioms already make the theory pure. For N = 2 this is a theorem;
for general N the unit, counit, cup and cap are pure and the multiplication
and comultiplication have equal Kraus rank, and rank one remains to be shown.
