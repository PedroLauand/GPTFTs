---
status: context (definitions and derived facts)
created: 2026-09-08
entered-by: agent, from the filed source and the chat of 2026-09-07/08 with Pedro
last-reviewed: 2026-09-08
source: Dmello, Ligthart, Gross, arXiv:2405.13819, `sources/papers/240522 - entanglement swapping in gpts and iterated chsh games` (DLG below)
feeds: paper/results-narrative-2d.md (programme item 4); gpt-examples.md E10
machine-written: true
---

# Oblate stabilizer theory (OST): definitions and derived facts

Everything the two-dimensional discussion invokes about OST, with statement
numbers, so that the discussion can point here. Statements marked [DLG n] are
read from the source; statements marked [obs] are derived here (date given) and
are ours; ✓ marks a machine check. House notation
(`conventions/domain/notation.md`); one extension of P1 is flagged in O5.
Labels O1–O13 are stable.

---

**O1. Ambient space, pairing, composites.** V = Herm(C²), real dimension 4,
basis σ₀ = 𝟙, σ₁, σ₂, σ₃; Bloch form X = ½(t𝟙 + v·σ), t = tr X. States and
effects are both 2×2 Hermitian matrices, the pairing is tr(ρe), partial
contractions are partial traces [DLG (34)–(35)]. Unit effect u = 𝟙 [DLG Def 4.1].
Composite of two systems: V ⊗ V = Herm(C⁴), dimension 16 = 4·4: tomographic
locality holds. The ambient space is the qubit's.

**O2. The two constants.** r = cos(π/4)^{−1/2} = 2^{1/4}, so r² = √2 and
r² cos(π/4) = 1 [DLG Def 4]. R = e^{−iπσ₃/8} = diag(e^{−iπ/8}, e^{iπ/8});
conjugation Ad_R = R(·)R† rotates the Bloch sphere by π/4 about z [DLG before
(36)]. Ad_R(σ₁) = (σ₁ + σ₂)/√2.

**O3. States.** Stretched stabilizer states [DLG (28), (36)]

    x̃± = ½(𝟙 ± rσ₁),   ỹ± = ½(𝟙 ± rσ₂),   z̃± = ½(𝟙 ± σ₃),   Ω = {x̃±, ỹ±, z̃±};

state cone D⁽¹⁾ = cone(Ω) [Def 4.3], normalised states S⁽¹⁾ = conv(Ω) [(38)]:
an octahedron whose four equatorial vertices sit at Bloch radius r > 1 and
whose poles sit on the Bloch sphere ("oblate"). x̃±, ỹ± are not positive
semidefinite (eigenvalues (1 ± r)/2); D⁽¹⁾ ⊄ PSD₂. [obs 2026-09-07]
Membership: ½(t𝟙 + v·σ) ∈ D⁽¹⁾ iff |v_x|/r + |v_y|/r + |v_z| ≤ t.

**O4. Effects.** P⁽¹⁾ = cone(RΩR†) [Def 4.2]: the same octahedron rotated by
π/4 about z. E⁽¹⁾ = conv({0, 𝟙} ∪ RΩR†) [(39)], closed under ¬e = 𝟙 − e
[(37), (40)]; sup_{ρ,e} tr(ρe) = ½(1 + r² cos(π/4)) = 1 [(43)], which is what
fixes r. [obs] Pairings of a state vertex with an effect vertex take values in
{0, ½, 1}: an equatorial effect vertex gives 1 on its two nearest equatorial
state vertices, 0 on the opposite two, ½ on the poles; z̃± as effects give
1, 0 on z̃± and ½ on the equator. So the equator (x̃±, ỹ± against the rotated
square) is the gbit, and the poles are qubit-like.

**O5. Relation between the two cones; what "restricted" means here.** [obs]
P⁽¹⁾ = Ad_R(D⁽¹⁾) = (Ad_R∘T)(D⁽¹⁾), T the transpose (σ₂ ↦ −σ₂), since T is a
symmetry of the octahedron. Dual cones: (D⁽¹⁾)′ = {|w_x|, |w_y| ≤ t/r,
|w_z| ≤ t}, a box; (P⁽¹⁾)′ its rotation by π/4. Both inclusions
P⁽¹⁾ ⊊ (D⁽¹⁾)′ and D⁽¹⁾ ⊊ (P⁽¹⁾)′ are strict: neither cone is the dual of the
other; DLG take both as data with only D ⊂ P′ [DLG Def 1, F3]. In the
vocabulary of Chiribella–D'Ariano–Perinotti this is the failure of the
no-restriction hypothesis for the single system, but see O9: the effect cone
is the completely positive part of the box, so it is derived from the state
cones, not postulated. Convention P1 writes a system as (V, V⁺, u) with
effects [0, u] in the dual cone; OST needs the extended datum
(V, D⁽¹⁾, P⁽¹⁾, u), or P1 read with effects := completely positive
functionals (DECISION owed, `results-quantum-2dUTFT.md` 10.8).
Symmetries [DLG §V C, items 1–4]: conjugation by Paulis, transpose, and Ad_{R^m}
for m even preserve both cones; Ad_{R^m} for m odd exchanges them.
[obs 2026-09-08] Linear automorphisms of the cone D⁽¹⁾: positive scalars times
the 48 signed permutations of the three axes, with the rescaling (r, r, 1) →
(r, r, 1) (a permutation moving the z-axis to the x-axis multiplies by r);
proof: the relations x̃₊ + x̃₋ = ỹ₊ + ỹ₋ = z̃₊ + z̃₋ force a linear map that
permutes the six extreme rays to use one common scale. No continuous symmetry.

**O6. Bipartite generators.** |Φ⁺⟩ = (|00⟩ + |11⟩)/√2, |Φ⁺⟩⟨Φ⁺| =
¼(σ₀⊗σ₀ + σ₁⊗σ₁ − σ₂⊗σ₂ + σ₃⊗σ₃) [(29), (32)]; (A ⊗ B)|Φ⁺⟩ = (𝟙 ⊗ BAᵗ)|Φ⁺⟩
[(30)]; both partial traces ½𝟙 [(31)]. DLG define, for μ ∈ Z₄ and m ∈ Z₈,

    Φ⁺_{μ,m} := ((σ_μR^m)† ⊗ 𝟙) |Φ⁺⟩⟨Φ⁺| ((σ_μR^m) ⊗ 𝟙),   Φ := {Φ⁺_{μ,m} : m odd}   [(44), (45)].

Subtlety 1 [obs]: the sixteen labels name eight states, because σ₃R^m = iR^{m+4}
and σ₂R^m = −σ₁R^{m+4}: Φ⁺_{3,m} = Φ⁺_{0,m+4}, Φ⁺_{2,m} = Φ⁺_{1,m+4}. ✓
Subtlety 2 [obs]: DLG (46) reads tr(Φ⁺_{μ,m}(e ⊗ f)) = ½ tr(f σ_μ R^m eᵗ R^{−m} σ_μ);
computing from (44) with (30) gives R^{−m} eᵗ R^{m} instead. Nothing depends on
it, since m odd ↦ −m odd leaves the set Φ invariant, but individual labels do.
Our notation avoids the issue:

    Φ_U := (U ⊗ 𝟙) |Φ⁺⟩⟨Φ⁺| (U† ⊗ 𝟙),   U ∈ 𝒰 := {R^k, σ₁R^k : k odd}  (8 states),
    tr(Φ_U (e ⊗ f)) = ½ tr(f · Ū eᵗ Uᵗ);   for U = R^k: (e ⊗ id)(Φ_{R^k}) = ½ R^k eᵗ R^{−k}.

So Φ⁺_{μ,m} = Φ_{(σ_μR^m)†}, and applying an effect to one half of Φ_{R^k}
returns ½ times an odd rotation of the transposed effect, a unipartite state
when e ∈ P⁽¹⁾ (O5). Hence every Φ_U pairs nonnegatively with product effects
and, as an effect, with product states, and Φ ⊂ D⁽²⁾ ∩ P⁽²⁾ [Lemma 6 proof].
The Φ_U are rank-one quantum states although the local states are not PSD.
Their marginals are ½𝟙 ∈ D⁽¹⁾.

**O7. Bipartite cones.** D⁽²⁾ = cone(Ω ⊗ Ω ∪ Φ), P⁽²⁾ = cone(RΩR† ⊗ RΩR† ∪ Φ)
[Def 5]; higher cones by Algorithm 2; consistency is Lemma 6 (Algorithm 1
accepts the data). [obs] The untwisted Bell state is not an OST state:
tr(|Φ⁺⟩⟨Φ⁺| · (Rx̃₊R† ⊗ Rỹ₊R†)) = (1 − r²)/4 = −0.104; its ℓ¹-distance to
D⁽²⁾ is 0.207 (LP ✓). The twist by an odd power of R is what reconciles a Bell
state with the π/4 offset between the two cones.

**O8. Processes.** Not defined by DLG (a theory is its cones). Convention adopted
here (R14, candidates file T3): a linear map L : V^{⊗n} → V^{⊗m} is a process
iff (L ⊗ id_k)(D⁽ⁿ⁺ᵏ⁾) ⊂ D⁽ᵐ⁺ᵏ⁾ for all k (complete positivity on states);
reversible processes include Ad_{σ_μ}, Ad_{R^{2j}} and T on each factor.

**O9. Effects are the completely positive functionals.** [obs 2026-09-08]
If a functional e on V satisfies (e ⊗ id)(D⁽²⁾) ⊂ D⁽¹⁾, then applying it to
Φ_R gives ½ Ad_R(eᵗ) ∈ D⁽¹⁾, hence e ∈ (Ad_R∘T)(D⁽¹⁾) = P⁽¹⁾. Conversely
P⁽¹⁾ consists of completely positive functionals [DLG F4]. So P⁽¹⁾ is exactly
the completely positive part of the box (D⁽¹⁾)′; the entangled generators cut
it down. Consequence: for any process L in the sense of O8, L*(P⁽¹⁾) ⊂ P⁽²⁾
(pull-backs of effects are effects), so complete positivity on states already
implies positivity on effects. The same argument with Φ_R ⊗ Φ_R identifies
P⁽²⁾ with the completely positive bipartite functionals.

**O10. Teleportation and swapping.** {Φ⁺_{μ,1}}_{μ∈Z₄} is a four-outcome
measurement, Σ_μ Φ⁺_{μ,1} = 𝟙 ⊗ 𝟙 [(51)]; outcome μ teleports up to the
correction σ_μ ⊗ 𝟙 [Table I]. Swapping with Φ⁺_{0,1} as resource and as
measured effect acts as ¼·id on span{σ_μ ⊗ σ_ν} ⊃ D⁽²⁾ [(49), (55), App. VIII A]:
the theory is stable under iterated swapping. In categorical terms [obs ✓]:
cup 4Φ_U ∈ D⁽²⁾ and cap Φ_U ∈ P⁽²⁾ satisfy the snake identity for every
diagonal U ∈ 𝒰 (U = R^k), so the OST system is dualizable with itself as dual;
T ⊗ T exchanges Φ_R and Φ_{R†}.

**O11. Pure states and positive basis directions.** [obs 2026-09-08, ✓ grid]
Call ½(𝟙 + n·σ), |n| = 1, pure. (a) Pure states in D⁽¹⁾: n with
|n_x|/r + |n_y|/r + |n_z| ≤ 1; at the equator, azimuth within
45° − arccos(1/r) = 12.2° of the x or y axis. (b) Pure states in D⁽¹⁾ ∩ P⁽¹⁾:
only the poles. Proof: for polar angle α the two conditions read
sinα·g/r + |cosα| ≤ 1 with g the ℓ¹-norm of the equatorial direction in the two
frames; the larger of the two is ≥ √2 cos(π/8) = 1.307 > r, and
1.099 sinα + |cosα| > 1 for all α ∈ (0, π). (c) A pure effect ½(𝟙 + n·σ) is
nonnegative on all states iff |n_x|, |n_y| ≤ 1/r = 0.841: at the equator,
azimuth within 12.2° of an effect vertex (45° + k·90°). Azimuth 22.5° is
outside: r cos(π/8) = 1.0987 > 1, so ½(1 − r cos(π/8)) = −0.049 < 0.

**O12. Post-quantum correlations.** With ρ = Φ⁺_{0,1} and the equatorial
correlators A₀ = rRσ₁R†, A₁ = rRσ₂R† (differences of effect vertices, valid
observables of the theory), CHSH = 4 [Thm 8, (47)–(48)], sustained under
iterated swapping. Any setting with a z-measurement loses the strong violation
[Remark 7]. [obs] The equatorial gbit of O4 is where the post-quantum
correlations live, and r > 1 is what makes it a gbit.

**O13. Admissible Frobenius forms.** [obs 2026-09-08, exact LP ✓; hand proof
owed] A symmetric bilinear form β on V whose map x ↦ β(x,·) is a linear
isomorphism D⁽¹⁾ → P⁽¹⁾, and which is itself a bipartite effect with inverse a
bipartite state, is a positive multiple of one of the four forms
(X, Y) ↦ tr(Φ_{R^k}(X ⊗ Y)), k odd. Route: by O5 the cone isomorphisms are
Ad_R∘(signed permutation); eight are symmetric for the trace form; the LP
membership tests leave the four with z ↦ +z (the four with z ↦ −z have
ℓ¹-distance 2 from both cones). Signature of each: (3, 1), negative direction
along the σ₂-axis of the frame rotated by k·22.5°. Each is the Bell form of a
real structure at azimuth k·22.5°: Φ_{R^k} = (R^{k/2} ⊗ R^{k/2}) Φ⁺ (…)†, the
Bell state of the basis R^{k/2}·(any real orthonormal basis).

---

## How these enter the 2d discussion (pointers, no claims here)

O1: same ambient space as the qubit, so the same ambient Frobenius algebras.
O10: the 1d requirement (dualizability) holds. O13 + O9: what a 2d TFT's cup
and cap can be. O11(b): where the unit of a doubled theory can sit. O11(c) +
O3: why the pants of the doubled theory in the 22.5° basis leaves the cone.
The argument itself is in the chat of 2026-09-08 and will be registered in
`paper/results-narrative-2d.md` when agreed.
