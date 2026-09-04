# Plan: "GPTFTs — unoriented notes" (2026-08-11)

Restructure `notes.tex` into seven sections; retire `main.tex` after salvage.
Framing locked in: ambient-space-first, unnormalized cone canonical, Vec analogy only,
unoriented bordisms default, terminology from Barnum–Hilgert (BH, arXiv:1904.03753) and
Selby–Scandolo–Coecke (SSC, arXiv:1802.00367).

## §1 Introduction
Blank; port main.tex locality-from-gluing and beyond-QFT themes as `%` comments.

## §2 The category of GPTs
notes.tex 169–381 already is the minimal path: proper cone → system (V,V+,u) →
normalization derived → effects derived → morphisms/channels → trivial system →
min/max cones → composite + tomographic locality → symmetric monoidal → dual system
(object level only).
- ADD (missing from both files): after channels, remark citing SSC pp.21–22 —
  nontrivial causal subtheories cannot have cups & caps, so any GPTFT lives in the
  unnormalized cone-linear category. The justification for our conventions.
- ADD paragraph positioning SSC §6.2 (cone-first data = process theory with classical
  interface, presented concretely; closure the one extra assumption). Cite as converse.
- Salvage from main.tex: φ_□ injectivity lemma (lines 285–305, behind the C≠0
  decomposition); no-restriction residue payoff (spanning makes the dual a system);
  summary □ = ⊗|_local + C + [⊗min,⊗max]. Demote the two reduction lemmas to a remark.

## §3 Frames, spectrality, strong symmetry (new)
Order: effects/measurements (BH 2.5) → perfectly distinguishable (3.1) → frame (3.2) /
maximal frame (3.3) → testable preparation (SSC 2.34) + exact correspondence →
frame-indexed copier (SSC Ex 2.31; measure-and-prepare version exists in every GPT,
lands in ⊗min) → reversible group G(A) → spectrality (3.4) → strong symmetry (3.5) →
self-duality ladder (weak < self-dual < perfect; square and pentagon separators) →
BMU + BH Thm 1.1.
- Examples table (verified): classical yes/yes; quantum yes/yes; gbit no/no
  (diagonals ARE 2-frames via (2+x+y)/4; two D4-orbits; spectrality fails off diagonals);
  pentagon no/yes.
- Footnote BH erratum: even n-gons not strongly symmetric (their fn.10 overclaims).
- Record: 2-frame transitivity alone ⇒ self-duality (BH fn.11).

## §4 Unoriented bordisms and TFTs in Vec (replaces oriented warm-ups)
Bord_1: one point, one snake, swap relations σ∘∪=∪; classification (V,β) symmetric
nondegenerate; iso classes = signatures (p,q); Z(S¹)=dim V.
Bord_2: Turaev–Turner extended Frobenius — involution Φ, crosscap θ, Klein relation
θ² = μ(Φ⊗id)Δ(1); invariants Z(RP²)=ε(θ), Z(Klein)=tr Φ.
Keep oriented versions as short remarks. VERIFY TT relation conventions against paper.

## §5 1d GPTFTs
Oriented story compressed to a page (forced dual, single element g, teleportation).
Main statement unoriented: 1d GPTFT ⟺ symmetric positive iso β̂ with β̂(V+)=(V+)*
plus cup/cap positivity in one coherent composite cone.
Examples: classical (no twist); quantum (Hilbert–Schmidt absorbs transpose twist);
boxworld (weakly self-dual — T exists, even symmetric; failure is joint cup/cap
positivity = no positive-definite self-dualizing form).
- FIX notes.tex:258, 266 and main.tex:675 ("no linear map aligns the two" is FALSE;
  correct: no self-dualizing inner product).
Open problems OP1–OP5: dualizability ⇒ weak self-duality?; unoriented symmetry +
positivity ⇒ definiteness? (Lorentz/Minkowski: symmetry alone insufficient); signature
as invariant; C≠0; rigorous boxworld no-go.

## §6 2d GPTFTs (fills empty subsection)
Organizing principle: pants = compare, co-pants = frame-restricted broadcasting
(no-broadcasting forbids only universal broadcasting).
- Positivity ledger: P-η (η(1)∈V+), P-ε (ε∈(V+)*), P-μ (μ(C)⊆V+, wants C small),
  P-Δ (Δ(V+)⊆C, wants C large); D-cup/D-cap derived — 1d pinch recurs on maps.
- Frames vs minimal positive idempotents; two counits (ε exact/non-causal vs u giving
  decoherence onto frame span).
- Quantum Schur worked example: Δ=VρV† channel (V=Σ|ii⟩⟨i|), μ=V†·V Schur product,
  η(1)=J all-ones, γ = Choi cup, special (h=id), Z(Σ_g)=N²; unoriented Φ=transpose,
  θ=𝟙, Z(RP²)=N; Δ,μ pinch the composite cone from both sides — the quantum tensor
  product is SELECTED by the 2d structure. β signature (N(N+1)/2, N(N-1)/2):
  sharp only on frame span.
- SSC-postulates-in-miniature table; headline: sharpness (P4) is the one postulate 2d
  topology doesn't supply — it is BH's self-dualizing inner product.
- Conjectures C1–C5: frame+coherence-factor classification (R^k ⊕ C^m); BH Thm 1.1
  interface; composite-cone selection/uniqueness; CPV anchor (special comm †-Frobenius
  = ONB); unoriented extension essentially unique.

## §7 Program map
BH↔SSC dictionary table; ladder (1d ⇒ symmetric weak self-duality; +definiteness =
self-dual; 2d ⇒ frame + cone selection; +sharp+strong symmetry ⇒ Jordan via BH);
merged open problems.

## Bibliography additions
Barnum–Hilgert 1904.03753; SSC 1802.00367; Turaev–Turner math/0506229;
Barnum–Müller–Ududec; Barnum–Graydon–Wilce 1606.09331; Coecke–Pavlović–Vicary.

## Computation queue (finite, concrete)
1. Qubit Schur full audit incl. explicit witness breaking P-μ on ⊗max.
2. Gbit double no-go: no positive self-dualizing β; idempotent count k+2m=3 autopsy.
3. Classical simplex: all rows pass, β positive-definite (sharp), φ=id, θ=(1,…,1).
4. Composite-cone coherence on triple products (why intermediate cones need checking).

## Pending decisions (user)
- §4–6 unoriented-default with oriented as remarks, or both in parallel?
- Overwrite notes.tex or start fresh file?
