# Candidate post-quantum dualizable GPTs — mathematical definitions

Three theories pass level 1 (categorical teleportation) and are not subtheories of QT: **OST** (oblate stabilizer theory), the **Dmello–Gross families** 𝒯_H(a), and **DD(fHilb)** (density hypercubes). Fixed template for each:

(T0) ambient space V and pairing ⟨·,·⟩ : V\* × V → ℝ; (T1) unipartite cones 𝒟⁽¹⁾ (states) ⊂ V\*, 𝒫⁽¹⁾ (effects) ⊂ V, unit 𝟙; (T2) bipartite cones 𝒟⁽²⁾ ⊂ (V⊗V)\*, 𝒫⁽²⁾ ⊂ V⊗V and the rule generating 𝒟⁽ⁿ⁾, 𝒫⁽ⁿ⁾; (T3) transformations 𝒯; (T4) duality data (η, ε, c) with (ε⊗id)(id⊗η) = c·id; (T5) symmetry group; (T6) post-quantum witness; (T7) references. Throughout: cone(S) = {Σ λ_i s_i : λ_i ≥ 0, s_i ∈ S}; P′ = {x : ⟨x,p⟩ ≥ 0 ∀p ∈ P} (polar dual); ¬e := 𝟙^{⊗n} − e; 𝓔⁽ⁿ⁾ := 𝒫⁽ⁿ⁾ ∩ ¬𝒫⁽ⁿ⁾ (normalized effects); 𝒮⁽ⁿ⁾ := {ρ ∈ 𝒟⁽ⁿ⁾ : ⟨ρ,𝟙^{⊗n}⟩ = 1} (normalized states). Statements marked [obs] are derived here, not quoted.

---

## 0. Common framework (Dmello–Ligthart–Gross, Def. 1)

A theory with well-defined entanglement swapping is (V, 𝟙, {𝒫⁽ⁿ⁾}_{n≥1}, {𝒟⁽ⁿ⁾}_{n≥1}) with V finite-dimensional real, 𝟙 ∈ V, convex cones 𝒫⁽ⁿ⁾ ⊂ V^{⊗n}, 𝒟⁽ⁿ⁾ ⊂ (V^{⊗n})\*, subject to

(F1) 𝟙 ∈ 𝒫⁽¹⁾;
(F2) 𝒫⁽ⁿ⁾ ⊗ 𝒫⁽ᵐ⁾ ⊂ 𝒫⁽ⁿ⁺ᵐ⁾, 𝒟⁽ⁿ⁾ ⊗ 𝒟⁽ᵐ⁾ ⊂ 𝒟⁽ⁿ⁺ᵐ⁾;
(F3) 𝒟⁽ⁿ⁾ ⊂ (𝒫⁽ⁿ⁾)′;
(F4) partial contractions: e ∈ 𝒫⁽ⁿ⁾, ρ ∈ 𝒟⁽ᵐ⁾ ⇒ ⟨ρ,e⟩ ∈ 𝒫⁽ⁿ⁻ᵐ⁾ (n > m), ∈ 𝒟⁽ᵐ⁻ⁿ⁾ (n < m), ∈ ℝ≥0 (n = m);
(F5) S_n-invariance of 𝒫⁽ⁿ⁾, 𝒟⁽ⁿ⁾ (dropped in Dmello–Gross 2603.21347, Sec. I.1.1).

Entanglement swapping (Eq. 4): ⟦_ρ ^e _σ⟧ := ⟨ρ₁₂ ⊗ σ₃₄, 𝟙₁ ⊗ e₂₃ ⊗ 𝟙₄⟩ ∈ 𝒟⁽²⁾. Dual swapping (Eq. 5): ⟦^e _ρ ^f⟧ := ⟨𝟙₁ ⊗ ρ₂₃ ⊗ 𝟙₄, e₁₂ ⊗ f₃₄⟩ ∈ 𝒫⁽²⁾.

**Induced theory (Algorithm 2).** From bipartite data (V, 𝟙, P, D): 𝒟⁽¹⁾ := cone{⟨ρ, 𝟙⊗·⟩, ⟨ρ, ·⊗𝟙⟩ : ρ ∈ D}; 𝒫⁽¹⁾ := cone{⟨σ⊗·, e⟩, ⟨·⊗σ, e⟩ : σ ∈ 𝒟⁽¹⁾, e ∈ P}; 𝒫⁽²⁾ := P, 𝒟⁽²⁾ := D; for n ≥ 3, with ⊗̇ the minimal tensor product (X ⊗̇ Y := cone(X ⊗ Y)),
 𝒫⁽ⁿ⁾ := S_n·(𝒫⁽²⁾)^{⊗̇ n/2} (n even), S_n·(𝒫⁽¹⁾ ⊗̇ (𝒫⁽²⁾)^{⊗̇⌊n/2⌋}) (n odd), and likewise 𝒟⁽ⁿ⁾.
Lemma 2 (2405.13819): the output satisfies (F1)–(F5) iff Algorithm 1's finite list of checks passes (positivity ⟨D,P⟩ ≥ 0, 𝒫⁽¹⁾⊗𝒫⁽¹⁾ ⊂ P, 𝒟⁽¹⁾⊗𝒟⁽¹⁾ ⊂ D, ⟦_D ^P _D⟧ ⊂ D, ⟦^P _D ^P⟧ ⊂ P, S_2-invariance).

**Level 1 in this framework.** A ∈ objects is dualizable iff ∃ η ∈ 𝒟⁽²⁾, ε ∈ 𝒫⁽²⁾ with η̂ ε̂ = c·id_{V\*}, where η̂ : V → V\*, e ↦ ⟨η, e⊗·⟩ and ε̂ : V\* → V, σ ↦ ⟨σ⊗·, ε⟩ (Eq. 2 of 2603.21347). Teleportation up to a correction group H: ∃ measurement {ε_h}_{h∈H} ⊂ 𝒫⁽²⁾, Σ_h ε_h = 𝟙⊗𝟙, with η̂ ε̂_h = c·h for h ∈ H ⊂ GL(V\*) acting as reversible transformations of the theory.

---

## 1. Oblate stabilizer theory (OST)

**(T0)** V = Herm(ℂ²) ≅ ℝ⁴, basis σ₀ = 𝟙, σ₁, σ₂, σ₃; V\* ≅ V via ⟨ρ, e⟩ := tr(ρe). 𝟙 := σ₀.

**(T1)** r := (cos π/4)^{−1/2} = 2^{1/4}. R := e^{−iπσ₃/8} (conjugation by R rotates the Bloch sphere by π/4 about z). Define
 x̃_± := ½(𝟙 ± rσ₁), ỹ_± := ½(𝟙 ± rσ₂), z̃_± := ½(𝟙 ± σ₃), Ω := {x̃_±, ỹ_±, z̃_±} (|Ω| = 6),
 𝒟⁽¹⁾ := cone(Ω), 𝒫⁽¹⁾ := cone(R Ω R†) (Def. 4, 2405.13819).
Consequences (Eqs. 38–43): 𝒮⁽¹⁾ = conv(Ω); 𝓔⁽¹⁾ = conv({0, 𝟙} ∪ RΩR†); ¬𝓔⁽¹⁾ = 𝓔⁽¹⁾; sup_{ρ∈Ω, e∈RΩR†} tr(ρe) = ½(1 + r² cos π/4) = 1. Pairing table [obs]: for ρ ∈ Ω, e ∈ RΩR†, tr(ρe) ∈ {0, ½, 1}; the equatorial sub-GPT (x̃_±, ỹ_± vs. R x̃_± R†, R ỹ_± R†) is the gbit (square with its dual square), the polar pair z̃_± is qubit-like (tr(z̃_± · RΩ_{eq}R†) = ½). x̃_±, ỹ_± ∉ PSD (r > 1): 𝒟⁽¹⁾ ⊄ PSD₂. 𝒫⁽¹⁾ ≠ (𝒟⁽¹⁾)′ (weakly self-dual pair related by R; no-restriction fails).

**(T2)** |Φ⁺⟩⟨Φ⁺| := ¼(σ₀⊗σ₀ + σ₁⊗σ₁ − σ₂⊗σ₂ + σ₃⊗σ₃), |Φ⁺⟩ = (|00⟩+|11⟩)/√2. For μ ∈ ℤ₄, m ∈ ℤ₈:
 Φ⁺_{μ,m} := ((σ_μR^m)† ⊗ 𝟙) |Φ⁺⟩⟨Φ⁺| ((σ_μR^m) ⊗ 𝟙), Φ := {Φ⁺_{μ,m} : μ ∈ ℤ₄, m odd} (|Φ| = 16) (Eqs. 44–45).
 D := cone(Ω⊗Ω ∪ Φ), P := cone(RΩR† ⊗ RΩR† ∪ Φ) (Def. 5); 𝒟⁽ⁿ⁾, 𝒫⁽ⁿ⁾ := Algorithm 2 output (Lemma 6: consistent).
Key identity (Eq. 46): tr(Φ⁺_{μ,m} · e⊗f) = ½ tr(f σ_μ R^m eᵗ R^{−m} σ_μ), a unipartite pairing since R^m (m odd) exchanges 𝒟⁽¹⁾ ↔ 𝒫⁽¹⁾ and both cones are invariant under transpose and Pauli conjugation. Swapping (Eq. 61): ⟦_Φ ^Φ _Φ⟧ = ¼Φ. Stability (Eq. 55): ⟦_{Φ⁺_{0,1}} ^{Φ⁺_{0,1}} _•⟧ = ¼·id on span{σ_μ⊗σ_ν} ⊃ 𝒟⁽²⁾.
Note: Φ ⊂ PSD₄ (rank-one quantum states) while 𝒟⁽¹⁾ ⊄ PSD₂; the local marginals of Φ⁺_{μ,m} are ½𝟙 ∈ 𝒟⁽¹⁾.

**(T3)** Not specified in the source. Definition adopted [obs]: 𝒯(n→m) := {L ∈ Hom((V^{⊗n})\*, (V^{⊗m})\*) : (L ⊗ id_k)(𝒟⁽ⁿ⁺ᵏ⁾) ⊂ 𝒟⁽ᵐ⁺ᵏ⁾ ∀k ≥ 0} (complete positivity relative to the induced cones; cf. "required to be completely positive on the GPT by consistency", 2603.21347 Sec. III.8). Reversible subgroup contains conjugation by Paulis σ_μ, by R^{2j}, and transpose, on each factor.

**(T4)** η := Φ⁺_{0,1} ∈ D; ε_μ := Φ⁺_{μ,1} ∈ P, Σ_μ ε_μ = 𝟙⊗𝟙 (Eq. 51: a measurement); η̂ ε̂_μ = ¼·(σ_μ · σ_μ)ᵀ-type correction — outcome μ teleports up to the Pauli σ_μ (Thm. 7 table); c = ¼. Correction group H ≅ ℤ₂×ℤ₂ (Paulis mod phase). For μ = 0 the snake closes: (ε₀ ⊗ id)(id ⊗ η) = ¼ id [obs from Eq. 55].

**(T5)** Aut(𝒟⁽¹⁾, 𝒫⁽¹⁾) ⊇ ⟨σ_μ(·)σ_μ, R²(·)R^{−2}, (·)ᵗ⟩ — the octahedral/square symmetries preserving the z-axis; finite.

**(T6)** CHSH = 4 with A₀ = rRσ₁R†, A₁ = rRσ₂R†, B_j = A_j, ρ = Φ⁺_{0,1} (Eq. 48–50), preserved for all rounds of iterated swapping (Thm. 7). Tsirelson: QT ≤ 2√2.

**(T7)** L. J. Dmello, L. T. Ligthart, D. Gross, "Entanglement-swapping in generalised probabilistic theories, and iterated CHSH games", arXiv:2405.13819, Phys. Rev. A 110, 022225 (2024): Def. 1, Algs. 1–2, Lemma 2, Sec. V (Defs. 4–5, Lemma 6, Thm. 7), App. VIII.1–2. Boxworld comparison: Barrett quant-ph/0508211 Thm. 11; Short–Barrett 0909.2601 Cor. 1.

---

## 2. Dmello–Gross teleportation-stable families 𝒯_H(a)

**(T0)** V = ℝ^d, d ∈ {4, 6, 8}, standard inner product ⟨·,·⟩; γ : V → V\*, v ↦ ⟨v,·⟩ (Euclidean self-duality). 𝟙 := e_d (last basis vector). Effects primary (Sec. I.1): cones 𝒫⁽ⁿ⁾ ⊂ V^{⊗n}, 𝒟⁽ⁿ⁾ ⊂ (𝒫⁽ⁿ⁾)′ generating on Span(𝒫⁽ⁿ⁾)\* only — **𝒫⁽¹⁾ is not generating in V** (Span 𝒫⁽¹⁾ ⊊ V, Span 𝒫⁽²⁾ = V⊗V).

**(T1)** Parameter a ∈ (½, 1], r := √(a√2). Alice's effects and Charlie's effects (Sec. VI.4, d = 4):
 e₀ := ½(r, 0, 0, 1)ᵀ, e₁ := ½(0, r, 0, 1)ᵀ, f_j := R e_{1−j}, R := [[1/√2, 1/√2, 0, 0], [−1/√2, 1/√2, 0, 0], [0,0,1,0], [0,0,0,1]];
 Ω_A := {e_i, ¬e_i}_{i=0,1}, Ω_C := {f_j, ¬f_j}_{j=0,1}.
Correction group H ⊂ O(4), each generator fixing 𝟙 and preserving Ω_A, Ω_C:
 H = ℤ₄: ξ := [[0,1,0,0],[−1,0,0,0],[0,0,−1,0],[0,0,0,1]];
 H = K₄: ξ² = diag(−1,−1,1,1), η := diag(−1,1,−1,1);
 H = D₄ (three families): ξ_{125} := [[0,1],[−1,0]] ⊕ diag(1,1), η_{125} := diag(−1,1,−1,1); ξ_{135} := [[0,1],[−1,0]] ⊕ diag(−1,1), η_{135} := diag(−1,1,1,1); ξ_{145} := [[0,1],[−1,0]] ⊕ diag(−1,1), η_{145} := diag(−1,1,−1,1).
 d = 6, 8: same e_i, f_j padded with zeros ((r,0,0,0,0,1)/2 etc.), generators block-diagonal per the character (χ_{12345}: 2-dim rotation block ⊕ four 1-dim signs; χ_{12345²}: two rotation blocks ⊕ four signs; matrices not printed in the source).
Unipartite cones := Algorithm-2 closure of the bipartite data below (Sec. I.1.1, without S_2-symmetrization). [obs] 𝒫⁽¹⁾ ⊃ cone(H·Ω_A ∪ H·Ω_C ∪ {𝟙}), a polyhedral cone in the 3-dimensional Span{e₁_dir, e₂_dir, 𝟙}; coordinate 3 (and 5, 6, …) carries no local effect.

**(T2)** Bipartite state ρ := γ, i.e. ρ(e⊗f) := ⟨e, f⟩ (Eq. 12); ρ(𝟙⊗𝟙) = 1, ρ(e_i⊗𝟙) = ρ(𝟙⊗f_j) = ½, ρ(e_i⊗f_j) = ¼(1 + (−1)^{ij} a). Measurement 𝓜 := {φ̂_h := |H|⁻¹ h γ⁻¹ : h ∈ H} (¼ ξ^k γ⁻¹ for ℤ₄, ⅛ g γ⁻¹ for D₄). Effective I-CHSH GPT (Def. 12, with the projections Π trivial for these representatives):
 𝒫⁽²⁾ := closure of P := cone(𝓜 ∪ Ω_C ⊗ Ω_A), 𝒟⁽²⁾ := closure of D := cone(H·ρ ∪ ρ(·, Ω_C) ⊗ ρ(Ω_A, ·)).
Higher n by Algorithm 2 (minimal tensor products), permutation symmetry broken: left factor is Alice-type, right factor Charlie-type (Sec. I.1.1 remark). [obs] For a Bord-target one needs an S_2-symmetric theory: replace Ω_A, Ω_C by Ω := Ω_A ∪ Ω_C on every factor and check Algorithm 1; this symmetrization is not in the source.

**(T3)** 𝒯 := maps completely positive relative to {𝒟⁽ⁿ⁾} as in §1(T3). Teleportation semigroup S := {p_k⃗⁻¹ R_k⃗} with R_k := ρ̂ φ̂_k = |H|⁻¹ h_k (Sec. III.2); reversible corrections = H.

**(T4)** η := ρ (η̂ = γ), ε_h := φ_h (ε̂_h = |H|⁻¹ h γ⁻¹); η̂ ε̂_h = |H|⁻¹ h ⇒ teleportation up to h ∈ H with c = |H|⁻¹ (deterministic in BBLW's sense: correction applied after learning h). Condition 1 (Sec. III.3): CHSH value and self-testing marginals invariant under all N and all outcome strings.

**(T5)** Correction group H ∈ {ℤ₄, K₄, D₄} acting on V by the matrices above; character χ_φ of the representation on Span 𝒫⁽¹⁾-complement determines the family (Result 13: χ^{(ℤ₄)}_{1234}, χ^{(K₄)}_{1234}, χ^{(D₄)}_{125}, χ^{(D₄)}_{135}, χ^{(D₄)}_{145} in d = 4; χ^{(D₄)}_{12345} in d = 6; χ^{(D₄)}_{12345²} in d = 8). Constraints: dim φ ≥ 3, χ_φ ≥ 0, trivial rep multiplicity 1 (Thm. 11).

**(T6)** CHSH = 4a under arbitrary iterated swapping; post-quantum for a > 1/√2. Lemma 14: the ℤ₄ family is not realizable in QM for any a. Lemma 15 (no-pancake): no locally tomographic GPT with local dimension ≤ 3 supports Condition 1 — hence Span 𝒫⁽¹⁾ ⊊ V is forced.

**(T7)** L. J. Dmello, D. Gross, "Probabilistic theories stable under teleportation", arXiv:2603.21347 (Mar 2026): Sec. I.1 (framework), Eq. 2 (η̂, ε̂), Sec. III.2–III.6 (semigroup, Condition 1, Thms. 9, 11), Result 13, Lemma 14, Lemma 15, Def. 12, App. VI.1 (character tables), App. VI.4 (explicit representatives, quoted in full in `claude/sources/verbatim-extracts-dmello-gross-ost.md`). Deterministic-teleportation background: Barnum–Barrett–Leifer–Wilce 0805.3553 Thm. 3.

---

## 3. Density hypercubes DD(fHilb)

**(T0)** Objects: finite-dimensional Hilbert spaces H, d := dim H. 𝓗 := H\*⊗H ≅ End(H) (the CPM-doubled object), DD(H) := 𝓗 ⊗ 𝓗̄ ≅ End(H) ⊗ \overline{End(H)}, complex dimension d⁴; V := the real span of the state cone (dim_ℝ = ½(d⁴ − 3d³ + 7d² − 3d), 1806.00915 §2.2). Pairing: Hilbert–Schmidt ⟨X, Y⟩ := Tr(X†Y) on End(H)⊗\overline{End(H)}.

**(T1)** [obs, assembled from Selinger Def. 4.18/Cor. 4.13(d) applied to C = CPM(FHilb), = Zwart–Coecke Eqs. 3–4] For an ancilla E and ρ′ ∈ PSD(H⊗E) put ρ′_{kl} := (𝟙_H ⊗ ⟨k|) ρ′ (𝟙_H ⊗ |l⟩) ∈ End(H) (blocks w.r.t. an orthonormal basis {|k⟩} of E). Then
 𝒟_{DD(H)} := { Σ_{k,l=1}^{dim E} ρ′_{kl} ⊗ \overline{ρ′_{kl}} : E, ρ′ ∈ PSD(H⊗E) } ⊂ End(H) ⊗ \overline{End(H)},
 components Ψ_{ij,i′j′} = Σ_{k,l} ⟨ik|ρ′|jl⟩ · \overline{⟨i′k|ρ′|j′l⟩}, satisfying the ℤ₂×ℤ₂ index symmetry of §2.2 (τ(a,b) acting on the four index slots). Pure states: ρ′ = ψψ†, Ψ = ψψ† ⊗ \overline{ψψ†}. Double mixing Σ_k r_k ρ_k ⊗ ρ̄_k (E-diagonal ρ′) is a proper subcone (Zwart–Coecke Thm. 3.1, Cor. 4.2). Unit (forest discard, Prop. 1: the unique effect equal to 1 on all normalized states): 𝟙 := Tr ⊗ \overline{Tr}, ⟨𝟙, Ψ⟩ = Σ_{k,l} |Tr ρ′_{kl}|² = Tr((Tr_H ρ′)²). Effects: 𝒫_{DD(H)} := 𝒟_{DD(H)} under V\* ≅ V (dagger of the construction) — self-dual pair; positivity of pairing: ⟨Σ σ′_{kl}⊗σ̄′_{kl}, Σ ρ′_{mn}⊗ρ̄′_{mn}⟩ = Σ_{klmn} |Tr(σ′_{kl}†ρ′_{mn})|² ≥ 0.

**(T2)** DD(H) ⊗ DD(K) := DD(H⊗K) (folding is strong monoidal), 𝒟_{DD(H)⊗DD(K)} = 𝒟_{DD(H⊗K)} ⊋ 𝒟_{DD(H)} ⊗̇ 𝒟_{DD(K)}. All n-partite cones are of the same form with H replaced by H^{⊗n}. Locally tomographic in the categorical sense (states of DD(H⊗K) are determined by the algebra of DD(H), DD(K) morphisms) — but the ambient identification is End(H⊗K)⊗\overline{End(H⊗K)} ≅ (End H ⊗ \overline{End H}) ⊗ (End K ⊗ \overline{End K}) up to reordering of tensor slots.

**(T3)** [obs, same source] 𝒯(DD(H), DD(K)) := { Σ_{k,l} Φ_{kl} ⊗ \overline{Φ_{kl}} : E, Φ ∈ CP(End H, End(K⊗E)), Φ_{kl}(x) := (𝟙⊗⟨k|) Φ(x) (𝟙⊗|l⟩) } — closed under composition and ⊗ (Selinger Thm. 4.20). Equivalently (1806.00915 §2.1): a doubled CP map with auxiliary legs discarded through a special commutative †-Frobenius algebra; equivalently (1805.12079 Def. 5, §4.1): CPM_{Φ,Ξ}(fHilb) for the ℤ₂×ℤ₂ folding Φ = (id, conj, conj, id) with the multi-environment structure Ξ. Reversible: U ↦ Ad_U ⊗ \overline{Ad_U}. Hyper-decoherence (Def. 4, §3.2): idempotent hypdec_∘ ∈ 𝒯(DD(H), DD(H)) with Split-image ≃ CPM(fHilb) (Prop. 3); decoherence dec_∘ with image ≃ ℝ⁺-Mat (Prop. 2). DH(fHilb) := full sub-SMC of Split(DD(fHilb)) on {(DD(H), id), (DD(H), hypdec_∘), (DD(H), dec_∘)}.

**(T4)** η := Φ⁽²⁾ := |Φ⟩⟨Φ| ⊗ \overline{|Φ⟩⟨Φ|}, |Φ⟩ := Σ_i |ii⟩ ∈ H⊗H (ρ′ = |Φ⟩⟨Φ|, E = ℂ); ε := ⟨Φ⁽²⁾, ·⟩; c = ⟨Φ⁽²⁾,Φ⁽²⁾⟩ = |Tr(|Φ⟩⟨Φ|)²|² = d⁴. Snake holds as F²(snake in FHilb). Dagger-compactness of DD(fHilb): not stated in 1806.00915; holds [obs] because cups/caps and discards of CPM(fHilb) are morphisms of CPM(CPM(fHilb)) (Selinger Thm. 4.20 twice). Dual object DD(H)\* = DD(H̄) ≅ DD(H).

**(T5)** Aut ⊇ {Ad_U ⊗ \overline{Ad_U} : U ∈ U(d)} ∪ {partial transposes/conjugations compatible with the folding}; continuous.

**(T6)** Sorkin interference: with the multi-slit experiment of §4, I₃ ≠ 0 for d ≥ 3 (Eq. 31), I₄ ≠ 0 for d ≥ 4 (Eq. 33), I_k = 0 for k ≥ 5; QT has I₃ = 0. Hyper-decoherence removes I₃, I₄. Also: the "bridge" discard (a second normalizing map) exists, but Prop. 1 singles out the forest one as the unique causal effect.

**(T7)** S. Gogioso, C. M. Scandolo, "Density hypercubes, higher order interference and hyper-decoherence: a categorical approach", arXiv:1806.00915, LNCS (Springer) 10.1007/978-3-030-35895-2_10: §2.1 (construction, diagrammatic), §2.2 (components, symmetry, dimension), §2.3 + Prop. 1 (discards), Props. 2–3, Def. 4, §4 (interference). M. Zwart, B. Coecke, "Double dilation ≠ double mixing", arXiv:1803.00700, EPTCS 266, 133–146: Eqs. 1–4, Thm. 3.1, Cor. 4.2. S. Gogioso, "Higher-order CPM constructions", arXiv:1805.12079: Defs. 1, 4, 5, §4.1. P. Selinger, "Dagger compact closed categories and completely positive maps", ENTCS 170 (2007) 139–163: Defs. 4.1, 4.11, 4.18, Cor. 4.13(d), Thm. 4.20. Sorkin hierarchy: R. D. Sorkin, Mod. Phys. Lett. A 9, 3119 (1994), gr-qc/9401003.

---

## Comparison at a glance

| | OST | 𝒯_H(a) | DD(fHilb) |
|---|---|---|---|
| V | Herm(ℂ²) ≅ ℝ⁴ | ℝ⁴ (ℝ⁶, ℝ⁸); Span 𝒫⁽¹⁾ ⊊ V | End(H)⊗\overline{End(H)}, d⁴ |
| 𝒟⁽¹⁾ | cone(stretched octahedron Ω), ⊄ PSD | (𝒫⁽¹⁾)′ on a 3-dim span, polyhedral | double-dilated states, dim ½(d⁴−3d³+7d²−3d) |
| 𝒫⁽¹⁾ | cone(RΩR†), ≠ (𝒟⁽¹⁾)′ | cone(H·Ω_A ∪ H·Ω_C ∪ 𝟙), non-generating | ≅ 𝒟⁽¹⁾ (self-dual) |
| 𝒟⁽²⁾ | cone(Ω⊗Ω ∪ Φ), |Φ| = 16 | cone(H·γ ∪ products) | 𝒟_{DD(H⊗K)} |
| 𝒫⁽²⁾ | cone(RΩR†⊗RΩR† ∪ Φ) | cone(|H|⁻¹Hγ⁻¹ ∪ Ω_C⊗Ω_A) | ≅ 𝒟⁽²⁾ |
| n ≥ 3 | Algorithm 2 (⊗̇, S_n) | Algorithm 2 (no S_n) | DD(H^{⊗n}) |
| 𝒯 | cone-CP maps [obs] | cone-CP maps | Σ Φ_{kl}⊗Φ̄_{kl}, Φ CP |
| η / ε / c | Φ⁺_{0,1} / {Φ⁺_{μ,1}} / ¼ | γ / |H|⁻¹hγ⁻¹ / |H|⁻¹ | F²(|Φ⟩) / dual / d⁴ |
| correction group | ℤ₂×ℤ₂ (Paulis) | H ∈ {ℤ₄, K₄, D₄} | trivial (exact snake) |
| dagger | not defined in source | not defined in source | yes [obs] |
| witness | CHSH = 4 | CHSH = 4a; ℤ₄ family never quantum | I₃, I₄ ≠ 0 |
| finite? | yes (polyhedral) | yes (polyhedral) | no (semialgebraic) |

Open points before Frobenius feasibility can be posed: (i) OST and 𝒯_H(a) need 𝒯 fixed (adopted: cone-CP); (ii) 𝒯_H(a) needs S_2-symmetrization (Alice/Charlie asymmetry); (iii) DD(fHilb): confirm the closed forms in (T1)/(T3) against the diagrams of 1806.00915 §2.1 (they are the standard unwinding of Selinger's construction, but the paper writes them only graphically).
