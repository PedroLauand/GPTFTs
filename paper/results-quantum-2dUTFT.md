---
status: result, detailed write-up
created: 2026-09-07
entered-by: agent, on Pedro's instruction (chat of 2026-09-07); the strategy of the converse is Pedro's
last-reviewed: 2026-09-07
feeds: results section, dimension two; results-narrative-2d.md
machine-written: true
---

# Result 1. The two-dimensional TFTs of the GPT of quantum theory are those of FHilb

**Statement in one sentence.** Finite-dimensional Hilbert spaces, the standard
target of topological field theory, and the general probabilistic theory of
quantum theory, whose systems are density-operator cones and whose processes
are completely positive maps, have the same two-dimensional topological field
theories: doubling a Hilbert-space theory gives a probabilistic one, every
probabilistic one arises this way, unitary theories correspond exactly to
dagger theories, and the only ambiguity in general is a unit-modulus Euler
phase that the probabilistic side cannot see.

Everything below is proved from filed sources with statement numbers, in house
notation (`conventions/domain/notation.md`), and is interpretation-free; the
physical reading is Pedro's, later. ✓ marks a step carried out here; TARGET a
step still owed.

---

## 1. The three categories

**1.1 FHilb.** Objects: finite-dimensional complex Hilbert spaces H. Morphisms:
linear maps. Monoidal product ⊗, unit C, symmetry the flip σ. Dagger: the
adjoint f†. Compact closed with cup and cap the maximally entangled vector and
its transpose. [CHK Def 1.3–1.5; Selinger Def 2.6] Scalars C.

**1.2 CPM(FHilb).** Objects: the same H. A morphism H → K is a completely
positive map Φ : End(H) → End(K), equivalently a map of the form
Φ(X) = Σ_a K_a X K_a† (Kraus form; Choi's theorem in categorical dress is
Selinger Lemma 4.12). Composition and tensor product are those of the
underlying linear maps under End(H ⊗ K) ≅ End(H) ⊗ End(K); the dagger of Φ is
its adjoint with respect to the Hilbert–Schmidt inner products, which is again
completely positive. CPM(FHilb) is dagger compact closed. [Selinger Def 4.11,
Def 4.18, Thm 4.20] Scalars: the CP maps C → C, which are multiplication by
nonnegative reals, R_{≥0}.

**1.3 The GPT of quantum theory, (Q, ⊗).** Objects Q_N = (Herm_N, PSD_N, tr)
in house notation: the ambient real space V = Herm_N of dimension N², the cone
of unnormalised states PSD_N, the unit effect tr [G20]. Morphisms Q_N → Q_M:
the R-linear maps Herm_N → Herm_M that are completely positive, that is, whose
complex-linear extensions to End are CP. This is the cone-linear category of
allowed-up-to-scalar transformations; the channels (trace-preserving maps)
form the causal subcategory, which a TFT does not need [C2, C5]. Monoidal
product Q_N ⊗ Q_M = Q_{NM} with the cone PSD_{NM} ⊂ Herm_N ⊗ Herm_M ≅ Herm_{NM},
the density-operator composite, strictly between ⊗_min and ⊗_max [M Ex 17;
G12]; symmetry the flip; scalars End(Q_1) = R_{≥0}.

**1.4 Lemma (Q ≅ CPM(FHilb)).** Restriction to Hermitian parts is an
isomorphism of dagger symmetric monoidal categories CPM(FHilb) → Q.
*Proof.* End(H) = Herm(H) ⊕ i Herm(H) as real spaces, and a CP map is
complex-linear and preserves Hermiticity, so it is determined by its
restriction to Herm; conversely an R-linear map on Herm extends uniquely to a
complex-linear map on End, and the two notions of complete positivity agree by
definition. Tensor products, units, symmetries and daggers are the same maps
read on the real subspaces; PSD_{NM} ⊂ Herm_{NM} is the image of the cone of
End(H ⊗ K). ✓ Hence a TFT valued in the GPT of quantum theory on a qudit is
exactly a symmetric monoidal functor Bord_2 → CPM(FHilb), and we work there.

**1.5 The doubling functor.** D : FHilb → CPM(FHilb), D(H) = H,
D(f)(X) = f X f†. D is a dagger symmetric monoidal functor: D(g ∘ f) =
D(g) ∘ D(f), D(f ⊗ g) = D(f) ⊗ D(g), D(σ) = flip, D(f†) = D(f)†, D(1) = 1, and
on scalars D(z) = |z|². [Selinger Rem 4.19 (F(f) = f_* ⊗ f), Thm 4.20 (F
preserves the dagger compact closed structure)] Two consequences used below:
every D(f) has Kraus rank one; and D(f) = D(g) iff g = e^{iθ} f for some real θ
(when f ≠ 0), since f X f† = g X g† for all X forces g ∝ f with |ratio| = 1.

---

## 2. Two-dimensional TFTs and the objects that classify them

**2.1 TFTs as Frobenius algebras.** For any symmetric monoidal category C, the
groupoid of symmetric monoidal functors Bord_2 → C is equivalent to the
groupoid of commutative Frobenius algebras internal to C, via Z ↦ Z(S¹) with
the four structure maps η = Z(disk), μ = Z(pants), Δ = Z(copants),
ε = Z(reversed disk). [CR Thm 3.5, Thm 3.6, Rem 3.9; T6, T7] So statements
about TFTs can be made about Frobenius algebras and back.

**2.2 Unitary TFTs in FHilb.** Z is unitary if Z(M̄) = Z(M)† for the
orientation-reversed bordism [Sawin Def 2; DJ §2]. Then (H, μ, η) is a
commutative †-Frobenius algebra, Δ = μ†, ε = η† [Sawin Prop 1; CHK Def 2.1],
and by CPV Thm 5.1 it is given by an orthogonal basis of H [T17]. Weighted
normal form: an orthonormal basis {|i⟩}_{i=1}^N and weights θ_i > 0 with

    μ(|i⟩ ⊗ |j⟩) = δ_ij θ_i^{-1/2} |i⟩,    η(1) = Σ_i θ_i^{1/2} |i⟩,
    Δ = μ†,  i.e.  Δ(|i⟩) = θ_i^{-1/2} |i⟩ ⊗ |i⟩,    ε = η†,  i.e.  ε(|i⟩) = θ_i^{1/2}.

Checks ✓ (all maps basis-diagonal): unit μ(η ⊗ |j⟩) = |j⟩; (co)associativity
and (co)commutativity; Frobenius, both sides send |i⟩ ⊗ |j⟩ to
δ_ij θ_j^{-1} |j⟩ ⊗ |j⟩. The pairing β(|i⟩, |j⟩) = εμ(|i⟩ ⊗ |j⟩) = δ_ij is
the inner product on the real span of the basis (Durhuus–Jonsson's canonical
basis); the handle operator h = μΔ = diag(θ_i^{-1}); Z(Σ_g) = ε h^g η(1) =
Σ_i θ_i^{1−g}, which is DJ (28) with λ_i = θ_i^{-1}. Every unitary 2d TFT in
FHilb is unitarily equivalent to one of these, and the θ_i are its invariants
[DJ §3; Sawin Thm 2; T15]. Special (μμ† = id) iff every θ_i = 1.

**2.3 Non-unitary TFTs in FHilb.** Dropping the dagger, a commutative
Frobenius algebra over C is a direct sum of local ones: the one-dimensional
S_λ and the nilpotent N_{A,μ} [Sawin Prop 2]. Semisimple ones are the
classical structures of a basis that need not be orthogonal; nilpotent
summands send every bordism of genus ≥ 2 to zero.

**2.4 Invertible Euler theories.** For λ ∈ C^×, E_λ : Bord_2 → FHilb with
E_λ(S¹) = C and E_λ(M) = λ^{χ(M)}, χ the Euler characteristic, is a TFT
(χ is additive under gluing along circles and under disjoint union). On
generators: η ↦ λ, μ ↦ λ^{-1}, Δ ↦ λ^{-1}, ε ↦ λ. For any Z, Z ⊗ E_λ has the
same object and structure maps (λ^{-1}μ, λη, λ^{-1}Δ, λε). Two facts:

(a) Z ⊗ E_λ ≅ Z iff λ = ±1. *Proof.* Z ⊗ E_{−1} = (−μ, −η, −Δ, −ε) ≅ Z via
the isomorphism −id_H ✓. For |λ| = 1, λ ≠ ±1, the closed invariants
Z(Σ_g) λ^{2−2g} differ from Z(Σ_g) whenever some Z(Σ_g) ≠ 0 with g ≠ 1, and
isomorphic theories have equal closed invariants. ✓ (For general λ the
statement is the same; only |λ| = 1 is used below.)

(b) E_λ is a unitary theory iff λ = ±1: unitarity needs λ^{χ(M̄)} =
conj(λ^{χ(M)}) with χ(M̄) = χ(M), so λ = λ̄ and, for |λ| = 1, λ = ±1. ✓

---

## 3. Theorem A (the equivalence)

Fix a qudit H, dim H = N.

**(i) Doubling is a map of theories.** For every 2d TFT Z : Bord_2 → FHilb,
Z_Q := D ∘ Z : Bord_2 → CPM(FHilb) is a 2d TFT with Z_Q(S¹) = H; it is a
dagger theory if Z is unitary. *Proof.* D is a (dagger) symmetric monoidal
functor (1.5) and composites of symmetric monoidal functors are symmetric
monoidal; D(f†) = D(f)† transports the unitarity condition. ✓

**(ii) Every theory is a doubling.** For every 2d TFT Z_Q : Bord_2 →
CPM(FHilb) there is a 2d TFT Z̃ : Bord_2 → FHilb with D ∘ Z̃ = Z_Q. *Proof.*
Section 4 (Lemmas 4.1–4.6). ✓

**(iii) Bijection.** Z̃ in (ii) is unique up to tensoring with E_λ, |λ| = 1,
and isomorphic Z_Q have Z̃ related in the same way. Hence D induces a bijection

    { 2d TFTs in FHilb on H } / ( isomorphism, and Z ∼ Z ⊗ E_λ for |λ| = 1 )
        ⟷  { 2d TFTs in CPM(FHilb) on H } / isomorphism.

*Proof.* Section 5. ✓

**(iv) Unitary equals dagger.** Restricted to unitary theories on the left
and dagger theories on the right, D induces a bijection on isomorphism classes
with no residual ambiguity:

    { unitary 2d TFTs in FHilb on H } / iso  ⟷  { dagger 2d TFTs in CPM(FHilb) on H } / iso.

*Proof.* Section 5. ✓

**(v) Explicit form and invariants.** For Z unitary in the normal form 2.2,
Z_Q has the structure maps of Section 6; for every closed surface
Z_Q(Σ_g) = |Z(Σ_g)|² = (Σ_i θ_i^{1−g})²; Z_Q(T²) = N² = dim_R Herm_N, the
categorical dimension of Q_N [T5]; and the real Frobenius algebra on the
ambient space is Herm_N ≅ R^N ⊕ C^{N(N−1)/2} (Theorem B, Section 7). ✓

Through Lemma 1.4 the same statements hold verbatim for TFTs valued in the GPT
(Q, ⊗). That is the result: **the GPT of quantum theory has exactly the
two-dimensional topological theories of FHilb.**

---

## 4. Proof of (ii): every theory in CPM(FHilb) is pure

Throughout, Z_Q is a 2d TFT in CPM(FHilb) with Z_Q(S¹) = H and structure maps

    η_Q(1) = ρ ≥ 0,     ε_Q(X) = tr(EX) with E ≥ 0,
    μ_Q(X) = Σ_a K_a X K_a†  (K_a : H ⊗ H → H),     Δ_Q(X) = Σ_b D_b X D_b†  (D_b : H → H ⊗ H),

forming a commutative Frobenius algebra internal to CPM(FHilb) (2.1). Two
facts are used repeatedly.

(F1) *The identity channel has Kraus rank one.* If Σ_i F_i X F_i† = X for all
X ∈ End(H) then every F_i = f_i 𝟙 with Σ_i |f_i|² = 1. (The Choi operator of
the identity is the rank-one |Ω⟩⟨Ω|; Kraus operators are vectors in its range.)

(F2) *Nondegeneracy.* In a Frobenius algebra the pairing β = ε ∘ μ is
nondegenerate: β(X, Y) = 0 for all Y implies X = 0. (The snake identities make
A self-dual with pairing β; CR Lemma 2.4(a) in this context.)

**Lemma 4.1 (the unit is pure).** ρ has rank one.
*Proof.* Write ρ = Σ_r p_r |r⟩⟨r| with p_r > 0. The unit law μ_Q(ρ ⊗ X) = X
reads Σ_{a,r} p_r K_a(|r⟩ ⊗ 𝟙) X K_a(|r⟩ ⊗ 𝟙)† = X, so by (F1)
K_a(|r⟩ ⊗ v) = α_{ar} v for every a, r, v. Then for each r,
μ_Q(|r⟩⟨r| ⊗ X) = Σ_a |α_{ar}|² X =: λ_r X, hence β(|r⟩⟨r| − λ_r ρ, Y) =
ε_Q(λ_r Y − λ_r Y) = 0 for all Y and, by (F2), |r⟩⟨r| = λ_r ρ. A nonzero
rank-one operator is a multiple of ρ only if rank ρ = 1. ✓
Normalise: ρ = |η⟩⟨η|, ‖η‖ = 1, using the rescaling (μ, η, Δ, ε) ↦
(μ/t, tη, tΔ, ε/t), which preserves all axioms.

**Lemma 4.2 (the counit is pure).** E has rank one.
*Proof.* Let E = Σ_j q_j |e_j⟩⟨e_j|, q_j > 0, and P the projector onto supp E.
The counit law (id ⊗ ε_Q)Δ_Q = id reads Σ_{b,j} F_{bj} X F_{bj}† = X with
F_{bj} = √q_j (𝟙 ⊗ ⟨e_j|) D_b, so by (F1) F_{bj} = a_{bj} 𝟙 and
Σ_{b,j} |a_{bj}|² = 1; hence (𝟙 ⊗ P) D_b v = v ⊗ w_b with
w_b = Σ_j (a_{bj}/√q_j) |e_j⟩ ∈ supp E. The other counit law gives
(P ⊗ 𝟙) D_b v = w'_b ⊗ v. Applying P ⊗ P both ways,
(Pv) ⊗ w_b = w'_b ⊗ (Pv) for all v. Suppose dim supp E ≥ 2 and w_b ≠ 0 for some
b; pick v ∈ supp E not parallel to w_b, so Pv = v ≠ 0 and v ⊗ w_b = w'_b ⊗ v;
contracting the first slot against a vector orthogonal to v kills the left
side and gives ⟨v^⊥|w'_b⟩ v on the right, so w'_b ∝ v; contracting the second
slot against a vector orthogonal to w_b kills the left side and gives
⟨w_b^⊥|v⟩ w'_b on the right, so either w'_b = 0, whence w_b = 0, or v ∝ w_b,
excluded. So every w_b = 0, all a_{bj} = 0, contradicting Σ|a_{bj}|² = 1. Hence
dim supp E = 1. ✓ Write E = q |e⟩⟨e|.

**Lemma 4.3 (cup and cap are pure).** γ := Δ_Q(ρ) ≥ 0 and the operator B ≥ 0
with β(W) = tr(BW) both have rank one, and with γ = |Γ⟩⟨Γ|, B = |B⟩⟨B| the
vectors have full Schmidt rank.
*Proof.* The Frobenius structure makes the object self-dual in CPM(FHilb)
with cup γ and cap β satisfying the snake (id ⊗ β)(γ ⊗ id) = id. Write
|g_i⟩ = (G_i ⊗ 𝟙)|Ω⟩ and |b_j⟩ = (B_j ⊗ 𝟙)|Ω⟩ for γ = Σ_i |g_i⟩⟨g_i|,
B = Σ_j |b_j⟩⟨b_j|, |Ω⟩ = Σ_k |kk⟩. The snake is the identity channel with
Kraus operators the partial contractions L_{ij} = G_i B̄_j (B̄ the entrywise
conjugate), so by (F1) G_i B̄_j = ℓ_{ij} 𝟙 with Σ|ℓ_{ij}|² = 1. Some ℓ_{ij} ≠ 0,
so that G_i and B̄_j are invertible; then G_{i'} = ℓ_{i'j} B̄_j^{-1} for every
i', so all g_{i'} are proportional and γ is rank one; symmetrically B is rank
one. Full Schmidt rank is invertibility of G and B. ✓
(This is the CPM form of the retired notes' R1–R2: the cup is a scaled
maximally entangled vector, the cap its Choi–Jamiołkowski inverse.)

**Lemma 4.4 (the multiplication has Kraus rank one).** μ_Q(X) = K X K† for a
single K : H ⊗ H → H.
*Proof.* With ρ = |η⟩⟨η|, the left unit law and (F1) give K_a(|η⟩ ⊗ 𝟙) =
c_a 𝟙 with Σ_a |c_a|² = 1. A unitary change of Kraus operators, K_a ↦
Σ_b U_{ab} K_b, leaves μ_Q unchanged; choose U with first row c̄, so that

    K_1(η ⊗ v) = v,        K_j(η ⊗ v) = 0   (j ≥ 2).

Because μ_Q ∘ flip = μ_Q the right unit law μ_Q(X ⊗ ρ) = X holds too, and (F1)
gives K_a(𝟙 ⊗ |η⟩) = c'_a 𝟙; evaluating both unit relations at η ⊗ η gives
c' = c, so also K_1(v ⊗ η) = v and K_j(v ⊗ η) = 0. Now use associativity of
the CP map μ_Q(μ_Q ⊗ id) = μ_Q(id ⊗ μ_Q), evaluated on the rank-one operator
|ξ⟩⟨ξ'| with

    ξ = u ⊗ η ⊗ w,     ξ' = u' ⊗ v' ⊗ η    (u, w, u', v' arbitrary).

The unit relations give

    K_a(K_b ⊗ 𝟙) ξ  = K_a(K_b(u ⊗ η) ⊗ w)   = δ_{b1} K_a(u ⊗ w),
    K_a(K_b ⊗ 𝟙) ξ' = K_a(K_b(u' ⊗ v') ⊗ η) = δ_{a1} K_b(u' ⊗ v'),
    K_a(𝟙 ⊗ K_b) ξ  = K_a(u ⊗ K_b(η ⊗ w))   = δ_{b1} K_a(u ⊗ w),
    K_a(𝟙 ⊗ K_b) ξ' = K_a(u' ⊗ K_b(v' ⊗ η)) = δ_{b1} K_a(u' ⊗ v').

Hence

    Σ_{a,b} |K_a(K_b ⊗ 𝟙)ξ⟩⟨K_a(K_b ⊗ 𝟙)ξ'|  =  |K_1(u ⊗ w)⟩⟨K_1(u' ⊗ v')|,
    Σ_{a,b} |K_a(𝟙 ⊗ K_b)ξ⟩⟨K_a(𝟙 ⊗ K_b)ξ'|  =  Σ_a |K_a(u ⊗ w)⟩⟨K_a(u' ⊗ v')|,

and equality forces Σ_{a≥2} |K_a(u ⊗ w)⟩⟨K_a(u' ⊗ v')| = 0 for all u, w, u',
v'. Taking u' = u, v' = w gives Σ_{a≥2} ‖K_a(u ⊗ w)‖² = 0, so every K_a with
a ≥ 2 vanishes on product vectors, hence everywhere. ✓
Only the unit law, commutativity, associativity and (F1) were used.

**Lemma 4.5 (the comultiplication has Kraus rank one).** In any Frobenius
algebra Δ(a) = (id ⊗ L_a)(γ) with L_a left multiplication, i.e.
Δ_Q = (id ⊗ μ_Q)(γ ⊗ id). With γ = |Γ⟩⟨Γ| (Lemma 4.3) and μ_Q = K(·)K†
(Lemma 4.4), Δ_Q(Y) = D̃ Y D̃† with D̃ = (𝟙 ⊗ K)(|Γ⟩ ⊗ 𝟙). ✓

**Lemma 4.6 (the lift is a Frobenius algebra in FHilb).** By Lemmas 4.1–4.5
there are K, η, D̃, e with μ_Q = D(K), η_Q = D(η), Δ_Q = D(D̃), ε_Q = D(e†)
(absorb √q into e). Each Frobenius axiom, holding in CPM, holds in FHilb up to
a phase (1.5), and the phases can be removed:
- left unit: K(η ⊗ 𝟙) = e^{iα} 𝟙; replace η by e^{−iα} η;
- commutativity: K ∘ flip = e^{iγ} K, and applying it twice gives e^{2iγ} = 1;
  the right unit law then reads K(𝟙 ⊗ η) = e^{iγ} 𝟙, and evaluating both unit
  laws at η ⊗ η gives η = e^{iγ} η, so e^{iγ} = 1;
- associativity: K(K ⊗ 𝟙) = e^{iφ} K(𝟙 ⊗ K); on η ⊗ η ⊗ v both sides are v up
  to the phase, so e^{iφ} = 1;
- counits: (e† ⊗ 𝟙)D̃ = e^{iβ} 𝟙; replace D̃ by e^{−iβ} D̃; cocommutativity
  D̃ ∘ flip = e^{iγ'} D̃, and applying e† ⊗ e† to both counit laws gives
  e^{iγ'} = 1; coassociativity, contracted with e† ⊗ e† ⊗ 𝟙, gives phase 1;
- Frobenius: (K ⊗ 𝟙)(𝟙 ⊗ D̃) = e^{iχ} D̃ K; on η ⊗ x the left side is D̃x and
  the right side e^{iχ} D̃x, so e^{iχ} = 1; the other Frobenius law likewise.
So (H, K, η, D̃, e†) is a commutative Frobenius algebra in FHilb, Z̃ the TFT it
classifies (2.1), and D ∘ Z̃ = Z_Q on generators, hence everywhere. ✓

This proves Theorem A(ii). Note what was *not* used: no dilation, no
environment. Purification is the wrong tool for this question: a Stinespring
dilation adds a system that must be discarded, and discarding has Kraus rank
dim E, so it is never in the image of D; the Frobenius axioms instead force the
Kraus rank of every structure map to one.

---

## 5. Proof of (iii) and (iv): the bijection

**5.1 The fibre of D on theories.** Suppose D ∘ Z = D ∘ Z' with Z(S¹) =
Z'(S¹) = H. By (1.5) the structure maps satisfy μ' = e^{iα}μ, η' = e^{iβ}η,
Δ' = e^{iγ}Δ, ε' = e^{iδ}ε. The unit law forces β = −α, the counit law δ = −γ;
associativity, commutativity and the Frobenius law impose nothing further. So
Z' = (e^{iα}μ, e^{−iα}η, e^{iγ}Δ, e^{−iγ}ε). Set λ with λ² = e^{−i(α+γ)} and
c = λ^{−1} e^{−iα}; then c·id_H is an isomorphism of Frobenius algebras
Z ⊗ E_λ → Z' (check: c λ^{−1}μ = e^{iα}μ c², c λ η = e^{−iα}η,
c² λ^{−1}Δ = e^{iγ}Δ c, e^{−iγ}ε(c ·) = λ ε(·), all reduce to the two defining
relations of c and λ). Hence D ∘ Z = D ∘ Z' implies Z' ≅ Z ⊗ E_λ with |λ| = 1.
Conversely D ∘ (Z ⊗ E_λ) = D ∘ Z for |λ| = 1 since D(λ^{χ} f) = |λ|^{2χ} D(f).
The closed invariants confirm the picture: Z'(Σ_g) = e^{i(g−1)(α+γ)} Z(Σ_g)
= λ^{χ(Σ_g)} Z(Σ_g). ✓

**5.2 Isomorphisms in CPM(FHilb) are conjugations.** An isomorphism H → H in
CPM(FHilb) is a CP map with CP inverse, hence a linear bijection of Herm_N
preserving PSD_N in both directions. Such maps are X ↦ G X G† or X ↦ G Xᵀ G†
with G invertible [Schneider 1965, automorphisms of the cone of positive
semidefinite matrices; standard, source not filed, TARGET to file]; the second
kind is not completely positive. So every CPM-isomorphism is D(G) for some
G ∈ GL(H). If D ∘ Z' ≅ D ∘ Z via D(G), then D ∘ Z' = D ∘ Z^G where Z^G is Z
transported along the FHilb-isomorphism G (an isomorphic theory), and by 5.1
Z' ≅ Z^G ⊗ E_λ ≅ Z ⊗ E_λ. ✓

**5.3 Proof of (iii).** Well-definedness of Z ↦ [D ∘ Z] on classes:
isomorphic Z give isomorphic D ∘ Z (apply D to the isomorphism), and
Z ⊗ E_λ gives the same D ∘ Z (5.1). Surjectivity: Theorem A(ii).
Injectivity: 5.2. ✓

**5.4 Proof of (iv).** If Z is unitary then D ∘ Z is a dagger theory (A(i)).
Conversely let Z_Q be a dagger theory and Z̃ a lift (A(ii)); then
D(Z̃(M̄)) = Z_Q(M̄) = Z_Q(M)† = D(Z̃(M)†), so Z̃(M̄) = e^{iφ(M)} Z̃(M)† whenever
Z̃(M) ≠ 0. On generators: Δ̃ = e^{iφ_1} μ̃† and, reading the same relation for
the copants, μ̃ = e^{iφ_1} Δ̃†; ε̃ = e^{iφ_2} η̃† and η̃ = e^{iφ_2} ε̃†. Taking the
dagger of the unit law μ̃(η̃ ⊗ 𝟙) = 𝟙 gives e^{−i(φ_1+φ_2)} (ε̃ ⊗ 𝟙)Δ̃ = 𝟙, so
φ_2 = −φ_1 by the counit law. Thus e^{iφ(M)} = λ^{χ(M)} on generators with
λ = e^{iφ_2}, hence on every bordism. Put Z̃' := Z̃ ⊗ E_ν with ν² = λ^{−1},
|ν| = 1: then Z̃'(M̄) = ν^{χ} λ^{χ} Z̃(M)† = ν̄^{χ} Z̃(M)† = Z̃'(M)†, so Z̃' is
unitary and D ∘ Z̃' = Z_Q. Uniqueness: if Z and Z ⊗ E_λ are both unitary then
E_λ is unitary on the closed values, forcing λ = ±1 (2.4(b)) and Z ⊗ E_λ ≅ Z
(2.4(a)). ✓

**5.5 Remark (what the bijection does and does not identify).** The
correspondence is on isomorphism classes of theories on a fixed qudit H; it is
compatible with changing H by unitaries on both sides. It does not involve
direct sums: a Sawin direct sum of two CPM theories would have state space
End(H₁) ⊕ End(H₂), which is not an object of CPM(FHilb) but of its biproduct
completion CPM(FHilb)^⊕ [Selinger §5], the setting of hybrid
classical–quantum systems. Those are GPT systems too (Cl_n ⊕ Q_N); their
treatment is a separate step.

---

## 6. Explicit form of the doubled theory (proof of (v), first part)

Take Z unitary in the normal form 2.2 and write E_ij = |i⟩⟨j|,
V := μ† = Σ_i θ_i^{−1/2} |ii⟩⟨i| : H → H ⊗ H, so that μ = V† and Δ = V.
Index Herm(H ⊗ H) by pairs. Then Z_Q = D ∘ Z has

- μ_Q(X) = V† X V,   (μ_Q X)_{ij} = θ_i^{−1/2} θ_j^{−1/2} X_{(ii),(jj)}. On
  products μ_Q(A ⊗ B) = θ^{−1/2} (A ∘ B) θ^{−1/2}, A ∘ B the entrywise (Schur)
  product and θ^{−1/2} = diag(θ_i^{−1/2}). Only the (ii),(jj) block of X
  enters. ✓
- Δ_Q(ρ) = V ρ V† = Σ_{ij} θ_i^{−1/2} θ_j^{−1/2} ρ_ij |ii⟩⟨jj|. ✓
- η_Q(1) = |η⟩⟨η| = Σ_{ij} θ_i^{1/2} θ_j^{1/2} E_ij, rank one, trace Σ_i θ_i;
  the all-ones matrix J when every θ_i = 1. ✓
- ε_Q(ρ) = ⟨η|ρ|η⟩ = Σ_{ij} θ_i^{1/2} θ_j^{1/2} ρ_ij, a rank-one positive
  functional. ✓
- h_Q(ρ) = h ρ h,  (h_Q ρ)_ij = θ_i^{−1} θ_j^{−1} ρ_ij. ✓
- Z_Q(Σ_g) = |Z(Σ_g)|² = (Σ_i θ_i^{1−g})²; special case N² for every genus;
  Z_Q(T²) = N² = dim_R Herm_N. ✓

Positivity is automatic: every Z_Q(M) = D(Z(M)) is CP, so a bordism from k
circles to l circles maps PSD_{N^k} into PSD_{N^l}. In particular
η_Q(1) ∈ PSD_N, ε_Q ∈ PSD_N^*, μ_Q(PSD_{N²}) ⊆ PSD_N, Δ_Q(PSD_N) ⊆ PSD_{N²}. ✓
Normalisation is not required by the TFT; for θ = 1, V is an isometry, Δ_Q is
trace preserving and μ_Q trace non-increasing (VV† is the projector onto
span{|ii⟩}), so up to scalars the generators are allowed processes of the GPT.
Recorded identities: (id ⊗ tr) ∘ Δ_Q(ρ) = Σ_i θ_i^{−1} ρ_ii E_ii;
ε_Q ∘ η_Q = (Σ_i θ_i)²; tr ∘ η_Q = Σ_i θ_i.

**The qubit, θ = 1, in full.** V = |00⟩⟨0| + |11⟩⟨1|; μ_Q(A ⊗ B) = A ∘ B;
Δ_Q(ρ) = Σ_{i,j∈{0,1}} ρ_ij |ii⟩⟨jj|; η_Q(1) = J = 2|+⟩⟨+|; ε_Q(ρ) = Σ_ij ρ_ij
= 2⟨+|ρ|+⟩; h_Q = id; Z_Q(Σ_g) = 4. Unit law J ∘ ρ = ρ ✓; Frobenius on
E_ij ⊗ E_kl: both sides δ_ik δ_jl E_ij ⊗ E_ij ✓; Δ_Q(|+⟩⟨+|) = |Φ⁺⟩⟨Φ⁺| ✓.

---

## 7. Theorem B: the real Frobenius algebra on the ambient space

**Theorem B.** For Z unitary with weights θ_i, the commutative Frobenius
algebra (Herm_N, μ_Q, η_Q, Δ_Q, ε_Q) over R decomposes as

    Herm_N ≅ R^N ⊕ C^{N(N−1)/2},     k = N,  m = N(N−1)/2,  k + 2m = N²,

with the Frobenius pairing of signature (N(N+1)/2, N(N−1)/2). Over C, the same
maps make M_N(C) the N²-point classical structure with weights θ_i θ_j, which is
Durhuus–Jonsson-unitary for the Hilbert–Schmidt inner product; Herm_N is its
real form under the antilinear involution X ↦ X†.

*Proof.* Over C: μ_Q(E_ij ⊗ E_kl) = δ_ik δ_jl θ_i^{−1/2} θ_j^{−1/2} E_ij, so
ê_ij := θ_i^{1/2} θ_j^{1/2} E_ij are N² orthogonal idempotents with
ε_Q(ê_ij) = θ_i θ_j; hence (M_N(C), μ_Q, η_Q, Δ_Q, ε_Q) is the classical
structure of the basis {ê_ij}, orthogonal for Hilbert–Schmidt, and
Z_Q(Σ_g) = Σ_ij (θ_i θ_j)^{1−g} = (Σ_i θ_i^{1−g})², consistent with Section 6 ✓.
The involution τ(X) = X† respects the structure: (X ∘ Y)† = X† ∘ Y†,
τ(η_Q(1)) = η_Q(1), ε_Q(X†) = conj(ε_Q(X)); on idempotents τ(ê_ij) = ê_ji,
fixing the N diagonal ones and swapping the N(N−1)/2 pairs. The fixed-point
algebra is R·ê_ii (i = 1..N) plus, for each i < j, the real plane spanned by
P_ij := ê_ij + ê_ji and Q_ij := i(ê_ij − ê_ji), on which P ∘ P = P, P ∘ Q = Q,
Q ∘ Q = −P: a copy of C. ✓ Pairing (θ = 1): β_Q(X, Y) = Σ_ij X_ij Y_ij =
tr(X Yᵀ), the Hilbert–Schmidt pairing twisted by conjugation; β_Q(P, P) = 2,
β_Q(Q, Q) = −2; positive on real symmetric, negative on imaginary
antisymmetric matrices. ✓ [The retired notes' R7, confirmed and generalised to
weights.]

For the qubit: Herm_2 = span{𝟙, X, Y, Z} ≅ R² ⊕ C with idempotents
E_00 = (𝟙+Z)/2, E_11 = (𝟙−Z)/2 and the plane (X, Y), X ∘ X = X, X ∘ Y = Y,
Y ∘ Y = −X; β_Q diagonal (2, 2, −2, 2), signature (3, 1). ✓

**Remark (what nondegeneracy does).** The decohered candidate
μ′(A ⊗ B) = Σ_i A_ii B_ii E_ii, η′(1) = 𝟙, ε′ = tr, Δ′(ρ) = Σ_i ρ_ii E_ii ⊗ E_ii
satisfies the Frobenius relation but β′(X, Y) = Σ_i X_ii Y_ii is degenerate on
Herm_N: it is a 2d TFT with Z(S¹) = Cl_N, not Q_N. Any theory with Z(S¹) = Q_N
must pair the off-diagonal directions nondegenerately, and by Theorem A the
only way is the C-summands of Theorem B. This is the first instance of the
R^k ⊕ C^m phenomenon the programme is built on.

---

## 8. Remarks

**8.1 Dimension one.** The same Lemma 4.3 shows that a dualizable object of
CPM(FHilb) has pure cup and cap, so 1d TFTs in CPM(FHilb) are the doublings of
1d TFTs in FHilb: every qudit, with Z(S¹) = N². Consistent with T5 and with
Theorem A(v).

**8.2 Non-dagger theories are real.** Theorem A(iii) says the GPT of quantum
theory also hosts the doublings of non-unitary FHilb theories: non-orthogonal
idempotent bases (semisimple, the same (k, m) = (N, N(N−1)/2) as real
algebras, β not from an inner product) and nilpotent algebras such as C[t]/t²
on C², which give local Frobenius algebras on End(C²) with Z_Q(Σ_g) = 0 for
g ≥ 2. Sawin's degenerate theories survive in the probabilistic setting; the
dagger condition is what removes them and selects Theorem B.

**8.3 Where the scalars went.** FHilb has scalars C, CPM(FHilb) has R_{≥0},
and D squares: Z_Q(M) = |Z(M)|² on closed M. The lost information is exactly a
unit-modulus Euler theory, Theorem A(iii). For dagger theories nothing is lost,
Theorem A(iv).

**8.4 The template this instantiates.** For a general GPT system
X = (V, V^+, u), dim_R V = d: the complexification V_C carries, for any basis
and weights, the d-point classical structure; the GPT is a real form under an
antilinear involution τ; if τ permutes the basis fixing k vectors and swapping
m pairs the structure restricts to V ≅ R^k ⊕ C^m; what remains is positivity of
the four generators on the chosen composite cones. Quantum theory: basis the
matrix units, τ = †, (k, m) = (N, N(N−1)/2), composite PSD, positivity automatic
by complete positivity. (Pedro's plan of 2026-09-07; this reading of it to be
confirmed.)

---

## 9. Owed

1. File the classification of positivity-preserving bijections of Herm_N
   (Schneider 1965) used in 5.2, or replace it by a self-contained argument.
2. Hybrid systems: extend Theorem A to CPM(FHilb)^⊕ and the GPT systems
   Cl_n ⊕ Q_N (5.5).
3. The general-GPT template (8.4): classical Cl_n first, then the dualizable
   non-quantum candidates E10–E12.
4. DECISION (Pedro): the notion of unitarity for GPT-valued theories in
   general. Here it is "dagger in CPM", equivalently "induced from a unitary
   FHilb theory", equivalently Durhuus–Jonsson unitarity of the
   complexification.
5. Interpretation: deferred to Pedro.
