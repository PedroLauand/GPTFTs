# Glossary

Terms the project uses in a particular way, as the draft uses them. The label
in brackets is the beat where the usage is fixed; "retired" means the retired
B4 paragraph. Entries without a beat are working vocabulary of this
repository, not of the manuscript.

**operational view.** Taking "self-evident" features of general laboratory
situations (prepare, transform, measure; outcome statistics) as primitive
notions and deriving the abstract formalism from simple premises over them.
[B1+B2]

**generalized probabilistic theory (GPT).** The mathematical framework in
which lab-generated probabilities live and in which quantum theory is one
theory among many. Framework references: Barrett2007, Muller2021, Plavala2023.
[B1+B2]

**operational probabilistic theory (OPT).** The Chiribella–D'Ariano–Perinotti
framework (circuits, purification). The draft cites its reconstruction
(CDP2011) as a landscape reference without naming the framework. Not a synonym
for GPT; see `rigour.md`.

**reconstruction.** An axiomatization of quantum theory from
information-processing principles that selects it uniquely from the GPT
landscape. Role model: special relativity from two principles. [B2b]

**principle.** A physically motivated requirement on a theory, as opposed to a
textbook *postulate*, which is a mathematical stipulation without direct
physical motivation. No-signalling and locality of action are principles.
[B1+B2, B3]

**no-signalling principle.** The requirement that operations on separate
systems commute (Barrett2007), so that devices at spacelike separated
locations have correlations respecting relativistic causality. The weakest
condition a reasonable theory must satisfy, in the sense of being compatible
with special relativity. [B3]

**kinematical picture.** The view of relativity that no-signalling uses:
systems are points of spacetime, and the only feature of spacetime invoked is
the causal relation between a pair of points. [B4 new]

**locality of action.** Between points that are causally connected, influences
propagate locally through spacetime, by a dynamical law (Einstein1948). The
feature of spacetime physics no-signalling does not use. [B4 new]

**causal development.** The region to which a local dynamical law propagates
the degrees of freedom on a given region. [retired]

**parallel composition.** Composition of systems on spacelike separated
regions, which are independent. Implemented in GPTs by the tensor product,
derived from commuting operations. Premise (i). [retired]

**sequential composition.** Composition along the causal development, by the
local dynamical law. Premise (ii), the one the project imports. [retired]

**field-theoretic description.** Degrees of freedom distributed over spacetime
and governed by a local dynamical law. Generic rather than fundamental: the
renormalisation group makes low-energy physics flow to a continuum field
theory when discrete systems look continuous at long distances. [retired;
planned as B6]

**topological field theory (TFT).** The low-energy, gapped limit of a field
theory, with the Atiyah–Segal axioms as its skeleton. In the draft only the
title and the B7 placeholder refer to it. [title, B7]

**the question.** "Are there other physical principles that spacetime
compatibility requires from any probabilistic theory?" [B3]. To be restated in
B8 in a form that mirrors no-signalling.

**beat.** The unit the introduction is written in: one paragraph with one job,
labelled `% B<n>` in the draft, drafted, then approved by Pedro on a recorded
date.

**approved beat.** A beat whose comment carries "Approved" and a date. Its text
is Pedro's; agents do not rewrite it.

**retired paragraph.** Text taken out of the introduction but kept commented in
the draft for salvage.

## Technical terms added 2026-09-07 (toolbox vocabulary; sources in `syntheses/toolbox/`)

**frame.** A sequence of perfectly distinguishable pure states; maximal if not
extendable. [BH Def 3.2, 3.3]

**spectral.** Every state lies in the convex hull of some frame. [BH Def 3.4;
BMU Postulate 1 "classical decomposability"]

**strongly symmetric.** The automorphism group of Ω acts transitively on
k-frames for every k. [BH Def 3.5; BMU Postulate 2]

**weakly self-dual.** There is an order isomorphism V_A ≅ V_A^* carrying V_A^+
onto (V_A^+)^*. [BBLW §2; the gbit and even polygons are, by a rotation]

**self-dual (strongly self-dual).** The isomorphism is given by an inner
product: V_A^+ = (V_A^+)^* under ⟨·,·⟩. [Müller–Ududec; JL Def 2; SSC Def 4.6]

**homogeneous cone.** Aut(V^+) acts transitively on the interior. [SSC Def 4.2]

**symmetric cone; Euclidean Jordan algebra (EJA).** Homogeneous and self-dual;
by Koecher–Vinberg exactly the cones of squares of EJAs. [SSC Thm 4.8]

**bit symmetry.** Every pair of perfectly distinguishable pure states can be
mapped to any other by a reversible transformation. [Müller–Ududec]

**higher-order interference.** Sorkin's hierarchy; quantum theory has none
beyond second order. [BMU Postulate 3]

**dualisable object; cups and caps.** An object with a dual and evaluation and
coevaluation morphisms satisfying the snake identities; in a process theory,
cups and caps for every system. [CR §3.1; SSC Def 2.36]

**terminality.** Every process followed by discarding equals discarding; one
deterministic effect per system, here u_A. [Coecke Def 3.1; CDP Axiom 1]

**entangleable; nuclear.** A pair of cones whose minimal and maximal tensor
products differ; nuclear if they coincide. [ALPP]

**semisimple commutative Frobenius algebra.** A direct sum of one-dimensional
Frobenius algebras: functions on a finite set with a weight per point. [Sawin
Prop 2; Moore–Segal §3.1]

**handle operator.** h = μ ∘ Δ on Z(S¹); its eigenvalues classify unitary 2d
TFTs. [Durhuus–Jonsson; notes Thm 2d]

**unitary TFT; reflection positivity.** Target Hilb with Z(M^*) = Z(M)^*
[Sawin Def 2]; the Wick-rotated form of unitarity [Freed–Hopkins].

**GPTFT.** The retired notes' name for a TFT valued in (GPT, ⊗). Working
vocabulary, not in the draft.
