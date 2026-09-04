# Standing assumptions

What the project takes as given unless a piece of work says otherwise. Every
item below is read off `paper/draft.tex` as of 2026-09-04; the label in
brackets says which beat. Nothing from the retired notes is assumed here. For
each assumption: what it says, and what would make us drop it.

Status of the supporting text: **approved** means Pedro approved the beat on
the date given; **drafted** means written and awaiting approval; **retired**
means the paragraph is commented out in the draft and kept for salvage;
**planned** means only a placeholder exists.

## Assumptions

### A1. The operational stance

The empirical content of a physical theory is the statistics of outcomes in
prepare–transform–measure experiments. Quantum theory's textbook postulates
(Hilbert space, self-adjoint operators) carry no direct physical motivation;
the operational view takes "self-evident" features of laboratory situations as
primitives and derives the formalism from premises over them. [B1+B2,
approved 2026-08-31]

**We would drop this if:** the project stopped being about deriving structure
from operational premises and became about interpreting a fixed formalism.
Not foreseen.

### A2. GPTs are the framework, and quantum theory is one point in it

The natural home for lab-generated probabilities is the framework of general
probabilistic theories, in which quantum theory sits as one theory among many.
Framework references in the draft: Barrett2007, Muller2021, Plavala2023.
Landscape references: Hardy2001, CDP2011, MasanesMuller2011. [B1+B2, approved
2026-08-31]

**We would drop this if:** the structure the project needs (degrees of freedom
distributed over spacetime, a dynamical law) cannot be expressed in convex GPT
terms and forces a move to another formalism, such as operational
probabilistic theories or process theories. See "GPT versus OPT" in
`rigour.md`: the draft cites CDP2011 as a GPT landscape reference although
that work's own framework is an OPT (UNVERIFIED until CDP2011 is filed).

### A3. The reconstruction stance, with special relativity as the role model

Reconstructions select quantum theory out of the GPT landscape as the unique
theory satisfying a small set of physically motivated principles, the way the
Lorentz transformations follow from the constancy of the speed of light and
the relativity principle. Hardy2001 first, then CDP2011 and MasanesMuller2011.
[B2b, approved 2026-08-31]

**We would drop this if:** the results show that compatibility with a
topological field theory structure selects nothing, or selects a class rather
than quantum theory. The project would then be a classification, not a
reconstruction, and the introduction's framing changes. This is the largest
open uncertainty; see `pipeline/`.

### A4. No-signalling is the kinematic spacetime-compatibility condition

No-signalling (PopescuRohrlich1994) is the weakest condition a reasonable
theory must satisfy, in the sense of being compatible with special relativity
(Gisin2020). Formally: operations on separate systems commute (Barrett2007).
It invokes one feature of spacetime only, the causal relation between a pair
of points held at spacelike separation. [B3 opening, approved 2026-09-01; new
B4 opening, drafted 2026-09-01]

**We would drop this if:** never, as a characterisation of what no-signalling
uses. What must never be written is the stronger claim that no-signalling is
*derived from* relativity; see `rigour.md`.

### A5. Locality of action is the premise the project imports

Between points that *are* causally connected, influences propagate locally
through spacetime, by a dynamical law (Einstein1948). This is the feature of
spacetime physics that no-signalling does not use and that has not been
imported into the GPT framework. The project's principles follow from it.
[New B4 opening, drafted 2026-09-01; retired B4 paragraph for the programme
logic]

**We would drop this if:** the dynamical premise turned out to be already
implied by no-signalling together with the standard GPT axioms. There would
then be no new premise and no project.

### A6. Two composition premises, mirroring the causal axioms of AQFT

Once the degrees of freedom of a GPT are distributed over spacetime: (i)
degrees of freedom on spacelike separated regions are independent, so systems
compose in parallel; (ii) a local dynamical law propagates the degrees of
freedom on a region to its causal development, so systems compose in sequence.
No-signalling implements (i) alone: the GPT tensor product is derived from the
commutation of operations on separate systems (Barrett2007). Premise (ii) is
ours. AQFT references: StreaterWightman, HaagSchroer1962, FewsterRejzner2019.
[Retired B4 paragraph. The logic stands; the prose is out of the introduction
and may return in B7 or B8.]

**We would drop this if:** the parallel/sequential split proved not to be the
right decomposition of locality of action, or the mirroring of AQFT's axioms
misled rather than guided. UNVERIFIED: that the cited AQFT axioms split the
way the paragraph says. Check against the filed sources.

### A7. Field theory is the generic long-distance description, and its gapped limit is topological

Provided discrete systems appear continuous at long distances, the
renormalisation group washes out microscopic detail and low-energy physics
flows to a continuum field theory (WilsonKogut1974, Wilson1975, WeinbergEFT,
Polchinski1992). In the low-energy, gapped limit the field theory is
topological, and the Atiyah–Segal axioms give its skeleton. [B6 and B7,
planned; the RG citations appear only in the retired paragraph]

**We would drop this if:** the argument from genericity does not transfer from
quantum field theory to arbitrary GPTs, or the gapped-limit step cannot be
made without assuming quantum structure. Both are open. This is a programme
commitment, not something the draft establishes.

## Things we have decided not to assume

Positions the project is neutral on by choice, or that were retired. An agent
should not quietly pick a side.

- **The technical conventions of the retired notes.** Ambient space versus
  normalised state space, which cone is canonical, oriented versus unoriented
  bordisms, and whose terminology to follow were all fixed in the notes removed
  on 2026-09-04. None of it is in the draft. Re-enter any of them here,
  deliberately, with a "drop if" line, before using them.
- **The bordism category.** Dimension, orientation and extra structure are not
  fixed by the draft. B7 names only the Atiyah–Segal skeleton.
- **The no-restriction hypothesis.** Whether every mathematically allowed
  effect is physically available is not stated in the draft, and the GPT
  literature is split on it. TODO Pedro: decide, and record here.
- **Reconstruction versus classification.** See A3.
- **Spelling.** The draft mixes "Generalized" and "no-signalling". APS journals
  use American spelling. TODO Pedro: pick one. `notation.md` records the
  current usage.
