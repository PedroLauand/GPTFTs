---
status: result — theorem for the doubled (quantum-type) theories; general semisimple algebras open
created: 2026-09-09
entered-by: agent, from the chats of 2026-09-07/08/09 with Pedro; the framing "unique ambient theory, incompatible with the cone" is Pedro's
last-reviewed: 2026-09-09
feeds: results section, dimension two; paper/results-narrative-2d.md item 4; paper/results-structure.md Result 3
context: syntheses/toolbox/example-ost.md (labels O1–O13)
checks: pipeline/checks/ost_2d_scan.py, pipeline/checks/ost_2d_search.py
machine-written: true
---

# Result 3. Oblate stabilizer theory has cups and caps but its state cone is not closed under the pants

**Statement in one sentence.** The oblate stabilizer theory of Dmello, Ligthart
and Gross is dualizable, so it passes the one-dimensional requirement, yet none
of the unitary two-dimensional topological theories of its ambient space
Herm(C²), the doubled qubit theories of Result 1, restricts to it: its own
teleportation data force the algebra into the frame halfway between its state
and effect octahedra, and in that frame its fiducial states have a negative
entry, so the product map sends a product of two states to a negative multiple
of a state.

Everything below is in house notation, with the OST definitions taken from
`syntheses/toolbox/example-ost.md` (O-labels) and the two-dimensional notions
from `results-quantum-2dUTFT.md` (Result 1). ✓ marks a step carried out here,
TARGET a step still owed, [num] a numerical check (scripts in
`pipeline/checks/`). Interpretation is Pedro's, later.

---

## 0. What is being asked

A two-dimensional TFT valued in OST is a symmetric monoidal functor
Z : Bord_2 → OST with Z(S¹) the OST system (V = Herm(C²), D⁽¹⁾, P⁽¹⁾, u = tr)
[O1, O3, O4]. Equivalently [CR Thm 3.5; T6] it is a commutative Frobenius
algebra (V, μ, η, Δ, ε) whose four structure maps are OST processes:

    η ∈ D⁽¹⁾,   ε ∈ P⁽¹⁾,   μ(D⁽²⁾) ⊂ D⁽¹⁾,   Δ(D⁽¹⁾) ⊂ D⁽²⁾   (completely, O8).

Effect-side positivity of μ and Δ is then automatic [O9]. Derived requirements:
cup := Δη ∈ D⁽²⁾, cap := ε∘μ ∈ P⁽²⁾, handle := μ(cup) ∈ D⁽¹⁾, and D⁽¹⁾ is closed
under the product μ (since D⁽¹⁾ ⊗ D⁽¹⁾ ⊂ D⁽²⁾ [DLG F2]).

Because OST is locally tomographic [O1], forgetting the cones gives a TFT in
Vec_R on R⁴. Unitarity excludes nilpotent summands [Sawin Prop 2; T14], so the
algebra is semisimple: R⁴, R² ⊕ C or C ⊕ C [T13]. The unitary theories of the
ambient space with its natural cone are the doublings D(Z) of a qubit classical
structure Z = ({|a⟩, |b⟩}, θ_a, θ_b) [Result 1, Theorem A(iv)]:

    μ(X ⊗ Y) = V†(X ⊗ Y)V,   Δ(X) = V X V†,   V = Σ_i θ_i^{−1/2}|ii⟩⟨i|,
    η = ε = |η⟩⟨η|,  |η⟩ = Σ_i θ_i^{1/2}|i⟩,   cup = cap = 2|Φ⁺_{ab}⟩⟨Φ⁺_{ab}|,
    handle = |h⟩⟨h|,  |h⟩ = Σ_i θ_i^{−1/2}|i⟩.

On the qubit all bases are equivalent under U(2); OST's reversible group is
finite [O5, O8], so the position of the basis relative to the octahedra matters.
The question of this file: which D(Z), if any, have OST-positive structure maps;
and what constrains the non-doubled semisimple algebras.

---

## 1. Dimension one holds

Cup 4Φ_R ∈ D⁽²⁾ and cap Φ_R ∈ P⁽²⁾ satisfy the snake identity [O10; DLG (49),
(55); num ✓]. The OST system is dualizable with itself as dual. Loop weights:
the reversible processes Ad_{σ_μ}, Ad_{R²}, T have traces 0, 2, 2 ≥ 0 on
Herm(C²), consistent with Theorem B of `results-narrative-1d.md`. ✓

---

## 2. What the Frobenius form of any 2d theory in OST must be

**Lemma 2.1 (the Frobenius form is a cone isomorphism).** Let (V, μ, η, Δ, ε) be
a 2d TFT valued in a GPT whose bipartite cones satisfy the partial-contraction
axiom [DLG F4; G-contractions]. Put β := ε∘μ (cap) and γ := Δη (cup). Then
φ_β : V → V*, x ↦ β(x, ·), maps D⁽¹⁾ onto P⁽¹⁾, with inverse φ_γ : e ↦ (e ⊗ id)γ.
*Proof.* γ ∈ D⁽²⁾ because Δ is a process and η a state; β ∈ P⁽²⁾ because ε is an
effect and pull-backs along processes are effects [O9]. For x ∈ D⁽¹⁾,
φ_β(x) = (x ⊗ id)*β is a partial contraction of a bipartite effect with a
state, hence in P⁽¹⁾ (F4); for e ∈ P⁽¹⁾, φ_γ(e) is a partial contraction of a
bipartite state with an effect, hence in D⁽¹⁾. The Frobenius axioms give the
snake identity (β ⊗ id)(id ⊗ γ) = id, i.e. φ_γ∘φ_β = id, so the two maps are
mutually inverse cone isomorphisms. ✓ ∎

Consequences, general: β is symmetric (commutativity); the counit is
ε = φ_β(η); the handle μ(γ) is a state; D⁽¹⁾ is closed under μ.

**Lemma 2.2 (OST's admissible forms).** In OST the forms of Lemma 2.1 are the
positive multiples of the four twisted Bell forms

    β_k(X, Y) = tr(Φ_{R^k}(X ⊗ Y)),   k ∈ {1, 3, 5, 7},

which OST's symmetries Ad_{R²} and T permute. Each has signature (3, 1) and is
the Bell form of the real structure at azimuth k·22.5°, since
Φ_{R^k} = (R^{k/2} ⊗ R^{k/2}) Φ⁺ (R^{k/2} ⊗ R^{k/2})†. [O13: cone isomorphisms
D⁽¹⁾ → P⁽¹⁾ are Ad_R composed with the 48 signed axis permutations (O5); eight
are symmetric; the LP membership tests β ∈ P⁽²⁾, β^{−1} ∈ D⁽²⁾ leave exactly the
four with z ↦ +z; num ✓.] TARGET: a hand proof of the LP step.

**Corollary 2.3 (algebra type).** A real summand contributes the sign of its
weight to the signature of β, a C-summand contributes (1, 1) whatever its
weight (Gram matrix [[a, b], [b, −a]]). Signature (3, 1) therefore excludes
C ⊕ C, forces both real weights of R² ⊕ C positive, and forces exactly one
negative weight in R⁴. A negative weight makes Z(Σ_g) = Σ_i θ_i^{1−g} alternate
in that summand, so R⁴ is not unitary in the Dijkgraaf–Jones sense [T16]. Under
unitarity the algebra is R² ⊕ C with positive real weights and the Bell form:
quantum-type. ✓

---

## 3. Theorem 3.1: no doubled theory is OST-positive

**Theorem 3.1.** No two-dimensional TFT valued in OST is the doubling D(Z) of a
qubit classical structure. Equivalently, none of the unitary two-dimensional
TFTs of the ambient space Herm(C²) in the sense of Result 1 restricts to OST.

*Proof in five steps.* Let D(Z) be OST-positive, with the notation of §0.

**Step 1 (the unit sits at a pole).** η and ε are the same operator |η⟩⟨η|,
required to be a state and an effect: |η⟩⟨η| ∈ D⁽¹⁾ ∩ P⁽¹⁾. It is pure, and the
only pure states in both octahedra are the poles [O11(b)]. Using the symmetry
Ad_{σ₁} (z ↦ −z), |η⟩ = √κ |0⟩, κ > 0. Hence θ_i = |⟨i|η⟩|² = κ|⟨i|0⟩|², and
the basis phases can be chosen with ⟨i|0⟩ ≥ 0. ✓

**Step 2 (the cup fixes the real structure at the half-twist).**
cup = V|η⟩⟨η|V† = |Ω_{ab}⟩⟨Ω_{ab}| with |Ω_{ab}⟩ = Σ_i |ii⟩ = √2 |Φ⁺_{ab}⟩,
independent of the weights. By Lemma 2.1 the same operator, as cap, is a cone
isomorphism, so by Lemma 2.2 |Φ⁺_{ab}⟩ = (R^k ⊗ 𝟙)|Φ⁺⟩ up to phase, k odd; by
the symmetries take k = 1. With W := [|a⟩ |b⟩], |Φ⁺_{ab}⟩ = (WWᵀ ⊗ 𝟙)|Φ⁺⟩, so
WWᵀ = e^{iφ}R and W = e^{iφ/2} R^{1/2} O with O real orthogonal (D^{−1/2}W is
unitary with (D^{−1/2}W)(D^{−1/2}W)ᵀ = 𝟙). Write the columns of O as
o_a = (cos φ, sin φ), o_b = (sin φ, −cos φ). Step 1 then reads
R^{1/2}(√θ_a o_a + √θ_b o_b) ∝ |0⟩, and since R^{1/2} is diagonal,
√θ_a sin φ = √θ_b cos φ: θ_a = κ cos²φ, θ_b = κ sin²φ, φ ∈ (0, π/2). ✓

**Step 3 (the handle forces equal weights).** μ(cup) = V†|Ω_{ab}⟩⟨Ω_{ab}|V =
|h⟩⟨h| with |h⟩ = Σ_i θ_i^{−1/2}|i⟩ = κ^{−1/2} R^{1/2}(o_a/cos φ + o_b/sin φ)
= κ^{−1/2} R^{1/2} (2, t)ᵀ, t := tan φ − cot φ. It is a pure state and must lie
in D⁽¹⁾. The Bloch vector of (2, t) is (4t, 0, 4 − t²)/(4 + t²); Ad_{R^{1/2}}
rotates it by π/8 about z. The membership inequality of O3 reads

    4|t| (cos π/8 + sin π/8)/r + |4 − t²| ≤ 4 + t²,   (cos π/8 + sin π/8)/r = 1.0987.

For |t| ≤ 2 this is 4.395|t| ≤ 2t², i.e. |t| ≥ 2.197 or t = 0; for |t| > 2 it
is 4.395|t| ≤ 8, false. So t = 0, φ = π/4, θ_a = θ_b = κ/2, and the basis is

    |n±⟩ = R^{1/2}|±⟩,   Bloch vectors ±n,   n = (cos π/8, sin π/8, 0).

Unit and handle are then κ z̃₊ and (4/κ) z̃₊, and cup = 2Φ_R is exactly OST's
teleportation resource [O10]. The candidate is unique up to OST symmetry. ✓
[num ✓: the handle slack vanishes only at φ = π/4 on the cup-compatible family.]

**Step 4 (the pants leaves the cone).** With equal weights,
μ(X ⊗ Y) = (2/κ) X ∘_n Y, the entrywise product of the matrices of X and Y in
the n-basis. Those matrices are the matrices of Ad_{R^{−1/2}}(X) in the ± basis,
where σ₁ = diag(1, −1), ⟨+|σ₂|−⟩ = i, ⟨+|σ₃|−⟩ = 1. For x̃± the Bloch vector
rotates to ±r(cos π/8, −sin π/8, 0), so

    x̃₊ ↦ ½ [[1 + r cos(π/8),  −i r sin(π/8)], [i r sin(π/8),  1 − r cos(π/8)]],
    x̃₋ ↦ ½ [[1 − r cos(π/8),   i r sin(π/8)], [−i r sin(π/8), 1 + r cos(π/8)]],

with r cos(π/8) = 2^{1/4} cos(π/8) = 1.0987 > 1: the diagonal entries are
1.0494 and −0.0494. (The basis effect |n₊⟩⟨n₊| is not positive on OST states,
O11(c).) The entrywise product has diagonal ¼(1 − r² cos²(π/8)) twice and
off-diagonal ¼ r² sin²(π/8). With r² = √2, r² cos²(π/8) = (√2 + 1)/2 and
r² sin²(π/8) = (√2 − 1)/2:

    x̃₊ ∘_n x̃₋ = ((√2 − 1)/8)(−𝟙 + σ₃) = −((√2 − 1)/4) z̃₋,
    μ(x̃₊ ⊗ x̃₋) = −((√2 − 1)/(2κ)) z̃₋ ≈ −(0.207/κ) z̃₋ ∉ D⁽¹⁾ .

The product state x̃₊ ⊗ x̃₋ ∈ Ω ⊗ Ω ⊂ D⁽²⁾ is sent to a negative multiple of a
state; μ is not a process. [num ✓, both frames] ∎

**Step 5 (the same failure on the effect side).** The effect vertices sit at
azimuth 45°, also 22.5° from n, so Rx̃±R† have the same diagonal entries in the
n-basis and μ(Rx̃₊R† ⊗ Rx̃₋R†) = −((√2 − 1)/(2κ)) z̃₋ ∉ P⁽¹⁾: for the dagger
theory Δ* = μ on operators, so Δ*(P⁽²⁾) ⊄ P⁽¹⁾. And u∘μ, the pull-back of the
unit effect, is negative on x̃₊ ⊗ x̃₋, hence outside even the dual cone of D⁽²⁾.
One inequality, r cos(π/8) > 1, seen from states or from effects. [num ✓]

**Remark 3.2 (where QT differs).** In Q_2 the same pants is a Schur product of
PSD matrices in some basis, PSD by the Schur product theorem; equivalently every
basis projector is a positive effect. OST's states are not PSD (Bloch radius
r > 1 at the equator), and its cups pin the basis to a direction where a basis
projector takes the value −0.049 on a fiducial state.

---

## 4. The mechanism, isolated

**Lemma 4.1 (half-twist versus positivity).** Consider an equatorial gbit-type
theory: state vertices at azimuth 0°, 90°, 180°, 270° and radius r, effect
vertices at azimuth 2φ + k·90° and radius r, normalised by r² cos 2φ = 1 so
that adjacent state–effect pairings equal 1 (as in O4, where 2φ = π/4). A
Bell-type cup compatible with the two frames is the Bell state of the real
structure at azimuth φ (the rotation by 2φ realised as a half-rotation on each
party, as in Lemma 2.2). In that basis a state vertex has diagonal entry

    ½(1 − r cos φ) = ½(1 − cos φ / √cos 2φ) < 0   for all 0 < φ < π/4,

because cos²φ > 2cos²φ − 1 = cos 2φ. So the pants fails identically for every
nonzero offset between the state and effect frames; only offset zero, strong
self-duality as in quantum theory, escapes. ✓ (The doubled theory's pants on
the pair of antipodal vertices has trace ∝ 1 − r² cos²φ < 0.)

Reading, without interpretation: weak self-duality supplies cups and caps
(dimension one); dimension two asks the state cone to be an algebra over its
own teleportation pairing, and a rotated self-duality places that algebra
where the states are not positive.

---

## 5. Beyond doublings: what is open, and the evidence

**5.1 Reduction.** By Lemma 2.2 and Corollary 2.3, a 2d TFT in OST that is not
a doubling is a semisimple commutative Frobenius algebra on R⁴ with the Bell
form β₁, of type R² ⊕ C with positive real weights (or R⁴ with one negative
weight if unitarity is not imposed), whose idempotents are not rank-one
projectors. With β fixed, μ is the symmetric 3-tensor T(x, y, z) = β(xy, z),
and every positivity condition is linear in T: μ(ω ⊗ ω') ∈ D⁽¹⁾ iff
T(ω, ω', ·) ∈ P⁽¹⁾ (Lemma 2.1), and Δ(ω) ∈ D⁽²⁾ is an LP in T since
Δ(x) = Σ_{a,c} T(x, e_a, e_c) e^c ⊗ e^a. Only associativity (quadratic) and the
unit are nonlinear. TARGET: compute the polyhedral cone of positive symmetric
3-tensors for β₁ exactly; if it is trivial the no-go is unconditional;
otherwise intersect with associativity, using Lemma 5.2 to place idempotents.

**Lemma 5.2 (dominance; general).** Let K be a closed pointed full cone in a
finite-dimensional semisimple commutative real algebra, closed under the
product. Then (a) K meets each C-summand only at 0; (b) for every x ∈ K the
character of largest modulus is a real character with positive value; (c) if a
real idempotent p lies in K then its character χ_p is nonnegative on K, and
χ_p = φ_β(p)/θ_p is an effect. *Proof sketch.* Powers x^n/ρ(x)^n converge to
the dominant idempotent when the dominant character is unique; a negative real
or a complex dominant value puts v and −v (or a whole plane) into K; the C-unit
in K would make 1_C·K a two-dimensional cone inside K ∩ Π_C, contradicting
(a)'s ray argument; (c) from p·x = χ_p(x)p. ✓

**5.3 Evidence [num, 2026-09-08].** (i) Grid over all doubled theories with the
unit forced to a pole (90 × 96 bases): no pass; the largest relative slack of
the pants is −0.04, and the violation tends to zero only in the degenerate limit
θ_b → 0 where β itself degenerates. (ii) Random search over R² ⊕ C (470
Nelder–Mead starts) and R⁴ (534 starts) with β = β₁: best total violations
4·10⁻⁴ and 5·10⁻³, both at boundaries where a real weight tends to zero, and
both failing the copants LP by 0.3–1.3. Consistent with a no-go; not a proof.

---

## 6. Owed

1. Hand proof of the LP step in Lemma 2.2 (O13).
2. The non-doubled algebras: the LP-in-T computation of 5.1; then Lemma 5.2.
3. DECISION (Pedro): unitarity for GPT-valued theories; here it decides whether
   R⁴ with a negative weight is in scope.
4. The Dmello–Gross families T_H(a): does the obstruction track the CHSH value
   above Tsirelson's bound, or the offset between the frames (Lemma 4.1)?
   Answered in outline 2026-09-11,
   `pipeline/tsirelson-from-self-duality-and-swapping.md`: they are the same
   thing. In DG's normal form CHSH = 4a and the frame radius is r² = √2 a, so
   Tsirelson is r = 1 and OST is r = 2^{1/4}, its own stretch; strong
   self-duality forces r ≤ 1 in three lines, and Lemma 4.1 is the statement
   that the pants forces strong self-duality. OST and quantum theory are the
   same family (K₄, Pauli corrections) at a = 1 and a = 1/√2. Next
   computation: run §5.1's LP on T_{K₄}(a) across a and find where the cut
   sits.
5. Interpretation: Pedro.
