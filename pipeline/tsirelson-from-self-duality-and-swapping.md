---
status: workup           # entry | workup | proposed | project
created: 2026-09-11
entered-by: agent, on Pedro's instruction (session of 2026-09-11)
last-reviewed: 2026-09-11
feeds: B8, B9; results-ost-2dUTFT.md Owed 4
machine-written: true
---

# Can a swapping-stable, self-dual GPT beat Tsirelson?

## The paragraph

Dmello–Gross classify every GPT whose CHSH value survives arbitrarily many
rounds of entanglement swapping: the problem reduces to a representation of a
correction group H ⊆ D₄, and there are exactly seven families [DG Result 13,
filed `260322`]. Our two requirements land on the same data. Dualizability is
what their framework already builds in — the teleportation state ρ̂ is a cup and
its inverse a cap — so **all seven families pass dimension one**, and dimension
one says nothing about CHSH. Unitarity is the second requirement, and the
question is what it costs. The answer below: within a family the CHSH value is
a free parameter 4a, a ∈ (½, 1], and in their normal form the whole geometry is
one number,

    r² = √2 · a ,

the radius at which the CHSH frames sit. Quantum theory is a = 1/√2, exactly
r = 1. OST is a = 1, exactly r = 2^{1/4}. **Tsirelson's bound is the statement
r ≤ 1**, and r ≤ 1 is what strong self-duality forces, in three lines. So the
answer to Pedro's question is: no — a swapping-stable GPT whose state cone and
effect cone *coincide* cannot exceed 2√2, and the post-quantum stable theories
escape precisely by having cones that are congruent but **misaligned**.

What is not yet ours is the step from unitarity to strong self-duality: see
§3, and the gap in §4.

## 1. Weak or strong? Checked

Pedro asked which self-duality unitarity imposes. Three different conditions
have to be kept apart, and the project's own results settle the question.

| condition | what it says | who has it |
|---|---|---|
| **(a) dualizable** | the state cone of X pairs with the *dual* system X^∨ | every theory in DG's seven families; OST; quantum; not boxworld |
| **(b) symmetric cone isomorphism** | there is a **symmetric** β : V → V\* carrying the state cone D onto the **effect** cone P | quantum (β = tr(XYᵀ)), OST (four twisted Bell forms) |
| **(c) strong self-duality** | that isomorphism is an **inner product**: positive definite | quantum; **not** OST |

**Unitarity gives (b), not (c).** The evidence is in our own files, and it is
decisive: the Frobenius form of the 2d TFT of quantum theory is
β_Q(X,Y) = tr(XYᵀ), of signature (N(N+1)/2, N(N−1)/2) — for the qubit
(3, 1), **indefinite** [`results-quantum-2dUTFT.md` Thm B]. If unitarity
required an inner product, quantum theory would fail its own test. And OST,
which fails the 2d test, nevertheless has four admissible symmetric forms, also
of signature (3, 1) [`results-ost-2dUTFT.md` Lemma 2.2]. So (b) separates
nothing by itself.

Two corrections to what is written elsewhere in the repository, both mine:

- `pipeline/spacetime-reading-of-the-axioms.md` §2.3 said "the results use the
  strong version". Wrong: they use (b). Corrected there.
- (b) is **not** weak self-duality in the glossary's sense either, because that
  compares D with the *dual* cone D\*, while β lands on the effect cone P, and
  DG's families and OST both have P ⊊ D\* (restricted effects). Where the
  no-restriction hypothesis holds the two coincide. This distinction matters
  here and is flagged in `standing-assumptions.md` as still undecided.

**Strong self-duality is a conclusion, not a hypothesis.** What forces (c) is
the *positivity of the algebra*, not the form: Lemma 4.1 of the OST file shows
that for an equatorial gbit-type theory every nonzero offset between the state
and effect frames makes the pants negative, and "only offset zero, strong
self-duality as in quantum theory, escapes". Proved in that family; open in
general (§4).

## 2. The bridge: DG's normal form is our cup, and one number

What Condition 1 (stability + the two self-testing conditions) forces, up to
GPT isomorphism [DG Lemma 3, Lemma 4, Def 12, App VI D]:

- a real space V of dimension 4, 6 or 8, and a correction group H ∈ {Z₄, K₄, D₄}
  acting on it, with χ_φ ≥ 0 and the trivial character of multiplicity one
  [DG Thm 11, Result 13];
- the bipartite state given by the pairing γ, in normal form the Euclidean one:
  **ρ̂ = γ**, so ρ(e ⊗ f) = ⟨e, f⟩;
- Alice's two CHSH effects at radius r on orthogonal axes,
  e₀ = ½(r, 0, 0, 1), e₁ = ½(0, r, 0, 1), and Charlie's f_j = R e_i with R the
  **π/4 rotation** — the offset is not optional, it is the CHSH geometry;
- ρ(e_i ⊗ f_j) = ¼(1 + (−1)^{ij} a), whence

      ⟨e₀, f₀⟩ = ¼(1 + r²/√2) = ¼(1 + a)  ⟹  **r² = √2 a**,  CHSH = 4a.

Two things follow immediately.

**2.1 Every stable theory is dualizable.** ρ̂ = γ is invertible, the k = 0
outcome of the Bobs' measurement is the cap ¼γ and γ^{-1} the cup, and the
snake is their contraction. This is the same structure the project verified by
hand for OST [O10; Result 3.2]. So dimension one is satisfied across the
classification and **cannot** bound CHSH. Everything has to come from
dimension two. (Conversely, DG's Lemma 15, the GPT no-pancake theorem, rules
out boxworld and the polygons from swapping — the same theories our Result 0
rules out from dualizability. The two no-gos agree on the examples; whether
they agree in general is open.)

**2.2 The numbers line up exactly.**

| theory | a | CHSH = 4a | r² = √2a | r |
|---|---|---|---|---|
| quantum (K₄ family) | 1/√2 | 2√2 | 1 | **1** |
| OST (K₄ family, DLG) | 1 | 4 | √2 | **2^{1/4}** |

OST's correction group is the Klein four-group — "equivalent to finding the
resultant element of the Klein four-group" [DLG Thm 8 and Tab. I, filed
`240522`] — and its stretch is r = 2^{1/4} [O2; E10]. So **quantum theory and
OST are the same family at different a**, and the question "can a stable theory
beat Tsirelson" is the question "how large may a be", i.e. how large may r be.

## 3. The argument: strong self-duality forces r ≤ 1, i.e. Tsirelson

Suppose the ambient theory is strongly self-dual with respect to the inner
product in which DG's normal form holds: ⟨u, u⟩ = 1, u ⊥ the Bloch directions,
the Bloch directions unit, and the state cone D self-dual, so that
P ⊆ D\* = D. Then:

1. e₀ = ½(u + r v) is an effect, hence lies in P ⊆ D, so 2e₀ = u + r v lies in
   D; and ⟨u, 2e₀⟩ = 1, so **2e₀ is a normalised state**.
2. An effect applied to a state is at most one: ⟨e₀, 2e₀⟩ ≤ 1.
3. ⟨e₀, 2e₀⟩ = ½⟨u + rv, u + rv⟩ = ½(1 + r²). Hence **r² ≤ 1**.

With r² = √2 a this is a ≤ 1/√2, i.e.

> **CHSH = 4a ≤ 2√2.**

Tsirelson's bound is exactly the statement that the CHSH frame fits inside the
self-dual cone. And the mechanism by which OST escapes is now visible: its
state and effect cones are both octahedra, congruent but rotated by 22.5°
relative to each other, so the effect ½(u + 2^{1/4}v) is *not* a state — step 1
fails. The misalignment is what buys r > 1, and it is the same misalignment
that Lemma 4.1 shows the pants cannot tolerate.

This is Tsirelson's own vector argument in GPT dress: the CHSH value is a
Cauchy–Schwarz bound for the pairing ⟨A_i, B_j⟩ = (−1)^{ij} a, and
Cauchy–Schwarz needs the pairing to be definite.

## 4. The gap, stated precisely

Two steps are owed, and they are different in kind.

**4.1 (the real one) Does the 2d TFT force strong self-duality?** Unitarity
gives only a symmetric cone isomorphism (§1). What must be shown is that a GPT
carrying a 2d TFT — β plus a positive commutative Frobenius algebra — is
strongly self-dual. Proved for the equatorial gbit-type family [OST Lemma 4.1];
open in general. This is the hinge: with it, "distributed over space in two
dimensions" implies Tsirelson for every swapping-stable theory.

**4.2 (technical) Are the two normalisations compatible?** DG's γ is a pairing
between *Alice's* space and *Charlie's* space, so its signature is not an
invariant — a basis choice on one side puts it in Euclidean normal form. The
self-duality form is intrinsic to one system. §3 assumes the two can be
normalised together. In quantum theory they can: the composite of the Bell
pairing with the Hilbert–Schmidt self-duality is the transpose, which is a cone
automorphism of the PSD cone. The general statement needed: *if the theory is
strongly self-dual, the teleportation pairing and the self-duality form differ
by a cone automorphism.* Check this before quoting §3 as a result.

**4.3 Effective versus ambient.** DG classify the *effective* GPT, the fragment
reachable from the instance. §3 is deliberately written at the ambient level —
it uses only that the ambient theory contains e₀, the state 2e₀ and the pairing
— so it does not need the fragment to carry a TFT. Keep it that way; the
fragment of quantum theory at a = 1/√2 is a polytope, not the qubit, and our
Result 1 is about the qubit.

**4.4 Is §3 already known?** Very likely in spirit. Self-duality plus
homogeneity gives a Jordan algebra by Koecher–Vinberg [SSC Thm 4.8], and
Tsirelson-type bounds for Jordan-algebraic theories are in the literature.
Self-duality *alone* is not enough in general, which is why the swapping
normal form is doing work here. TARGET: search for a statement of the form
"strongly self-dual GPTs obey Tsirelson" before claiming §3; the honest claim
may be that the DG normal form makes the known argument available without
homogeneity.

## 5. What to do, in order

1. **The scan.** Within the K₄ family, build T_{K₄}(a) for a grid of
   a ∈ (½, 1] from DG's App VI D representative and run the machinery already
   written for OST — Lemma 2.1 for the admissible forms, then the pants and
   copants LP [`pipeline/checks/ost_2d_scan.py`]. The prediction is sharp: the
   2d test passes for a ≤ 1/√2 and fails above it. If the cut sits exactly at
   Tsirelson, that is the result; if it sits elsewhere, §3's hypothesis is not
   what the TFT delivers and §4.1 is the reason. This is a small extension of
   an existing script and is the highest-value next computation in the project.
2. **The other six families.** Same machine, d = 4, 6, 8. The classification
   turns "all GPTs" into seven cases plus one parameter, which is why DG's work
   is worth this much to us: it is a *finite* list, and we have a decision
   procedure for each entry.
3. **Close 4.2**, then write §3 as a lemma.
4. **Then 4.1**, which is the paper's theorem if it goes through.

## 6. Why this matters to the paper

If §3 and 4.1 hold, the programme delivers a sentence of the kind the
introduction is looking for [B3, the question]: *a probabilistic theory that
can be distributed over space, in the sense of carrying a two-dimensional
topological field theory, and whose correlations survive being relayed, cannot
exceed Tsirelson's bound.* That is a spacetime principle implying a quantitative
limit on correlations — the thing the reconstruction programme has been looking
for and the thing Weilenmann–Colbeck conjectured and DG refuted with OST. Our
answer to the refutation would be: OST is stable, but it cannot be distributed
over space.

Note also the independent agreement on local tomography. DG argue that
swapping *justifies* rejecting local tomography ("the space spanned by the
product effects needed to realize the CHSH test is insufficient to support the
effects required for entanglement swapping", DG §III H); the project reached
the same place from the other side, since Result 0.7's loop-weight theorem
needs local tomography and Result 2 (real quantum theory) shows why dropping it
matters. Worth one sentence in the paper.

## Uncertainties

- §4.1 is the whole result and it is unproven in general.
- §4.2 could break §3 outright.
- Whether DG's Condition 1 is a real restriction: it is implied by stability
  when CHSH = 4 [DG remark (2) after Condition 1], but for a < 1 it is an
  assumption, so "every stable theory" above means "every instance satisfying
  Condition 1".
- The effect cones in DG's families are not generating [E11]; what a
  "restricted" effect cone does to Lemma 2.1 has been checked for OST (the
  effects are the completely positive functionals, O9) and not in general.

## Judgement

For Pedro. Not filled by the agent.

**What would change if this worked?**

**Is the upper bound high enough?**

**What would make us less uncertain?**

## Sources

Filed: `260322` Dmello–Gross (Condition 1, Lemma 3, Lemma 4, Thm 11, Result 13,
Lemma 14, Lemma 15, App VI D); `240522` Dmello–Ligthart–Gross (OST, Thm 8 and
Tab. I: the corrections are the Klein four-group).

Project: `paper/results-quantum-2dUTFT.md` (Thm B, the signature);
`paper/results-ost-2dUTFT.md` (Lemma 2.1, 2.2, 4.1, and Owed 4, which is the
question this entry answers); `paper/results-structure.md` (Results 0–3);
`syntheses/toolbox/` (E10, E11, O2, O9, O10, C13).

Related: `pipeline/spacetime-reading-of-the-axioms.md` (what the two
requirements mean; §1 above corrects its §2.3).
