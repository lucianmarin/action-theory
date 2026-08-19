# Action Theory

**Constraint – Freedom – Roadblock (CFR)**
*An action-first framework for physics, philosophy, economics, and human activity.*

> **Research status:** speculative working theory — not established physics.
> The physics layer is under active development. The philosophical, economic,
> and human-systems layers are **interpretive translations** of the same
> primitive vocabulary, not derivations. Every claim in this repository is
> classified as *derived, assumed, effective, predicted,* or *heuristic* (§8).

---

## Contents

1. [One Primitive: Action](#1-one-primitive-action)
2. [The Three Laws of the Framework](#2-the-three-laws-of-the-framework)
3. [Layer I — Physics: Action as the Substance of Reality](#3-layer-i--physics-action-as-the-substance-of-reality)
4. [Layer II — Philosophy: Action as the Category of Being](#4-layer-ii--philosophy-action-as-the-category-of-being)
5. [Layer III — Economics: Action as the Unit of Value](#5-layer-iii--economics-action-as-the-unit-of-value)
6. [Layer IV — Human Activity: Action as the Unit of Progress](#6-layer-iv--human-activity-action-as-the-unit-of-progress)
7. [The Unified Dictionary](#7-the-unified-dictionary)
8. [Epistemic Status — What This Document Claims](#8-epistemic-status--what-this-document-claims)
9. [Research Roadmap](#9-research-roadmap)
10. [FAQ](#10-faq)

---

## 1. One Primitive: Action

Most worldviews begin with *things*: particles, fields, space, time, goods,
people. Action Theory begins with *doings*.

> **Fundamental reality = (𝔄, ∘)** — an algebra/network of elementary
> actions and their physical composition rule.

Everything else — space, time, matter, energy, and in the extended layers
*value, institutions, and agency* — is a stable, coarse-grained pattern of
action.

> *The universe is not a stage with actors. It is the performance.*

Proposed hierarchy:

```
action → history → state → stable object / matter
```

A **state** is an equivalence class of histories with equivalent future
possibilities: `h₁ ~ h₂  ⟺  N(h₁) ≅ N(h₂)`, therefore `state = [h]`.
A persistent object is a stable equivalence class of action histories.

---

## 2. The Three Laws of the Framework

For a partial action history `h`, let the set of admissible continuations be

```
N(h) = { α : α ∘ h is physically admissible }
```

Then the entire framework — in every layer — is built from three primitives:

| Primitive | Definition | Meaning in one line |
|---|---|---|
| **Constraint** | the restriction defining `N(h)` | what the rules of the system forbid |
| **Freedom** | `F(h) = dim N(h)` | how many ways the story can continue |
| **Roadblock** | `R(h) ⟺ N(h) = ∅` | a channel of possibility closes |

> A Roadblock terminates a particular action channel, **not reality itself**.
> A chemical reaction can finish while other processes remain possible.

The single most important derived quantity is the **Freedom Volume**
`V_F = √|det G|` of the freedom geometry `G_AB`. Regular behavior lives where
`V_F > 0`; new behavior appears where `det G = 0` or the rank changes.

---

## 3. Layer I — Physics: Action as the Substance of Reality

*Status: speculative working theory. See §8 and §9.*

### 3.1 Quantum mechanics from composition
Each action carries a complex amplitude, `Z(β∘α) = Z(β)Z(α)`, and a history
gets `Z(γ) = e^{iS[γ]/ħ}`. The transition amplitude is the path sum

```
K(X_f, X_i) = Σ_{γ: X_i → X_f} e^{iS[γ]/ħ}
```

Semiclassically `δS = 0` recovers stationary-action mechanics; with a linear
state space, `iħ d|ψ⟩/dt = H|ψ⟩`.
*Unresolved (assumed, not derived): complex amplitudes, Hilbert norm,
unitarity, Born rule.*

### 3.2 Entanglement
Independent action structures factor, `A_AB ≅ A_A  A_B`; entangled ones do
not. **Entanglement = nonfactorizability of fundamental action
possibilities** — correlation without controllable faster-than-light
signalling.

### 3.3 Space and time
Time emerges from causal ordering `α ≺ β`; space from the geometry of
mutually independent action directions. If a Lorentzian metric emerges,
`c` is the propagation rate of the null boundary of emergent action
accessibility. *Unresolved: Lorentzian signature, four macroscopic
dimensions.*

### 3.4 Fields and matter
A field is a collective coarse-grained pattern of action relationships
(`U(1)` link curvature → Maxwell; Higgs as a vacuum order parameter).
**Matter = stable localized action pattern** (`δS_eff/δΦ = 0`,
`δ²S_eff > 0`); mass is its invariant rest energy, `mc² = E`.

### 3.5 Gravity
**Gravity = dynamical geometry of physically accessible action.** The
effective limit is Einstein's equation, plus a candidate CFR correction that
activates only at Roadblocks:

```
G_μν + Λ g_μν = (8πG/c⁴) T_μν + λ_F K_μν[𝔄]
```

### 3.6 New physics at Roadblocks
Ordinary physics = evolution on regular strata (`V_F > 0`); new physics =
transition where regularity fails (`det G = 0`). Candidate signatures: a
threshold decoherence/collapse term `Γ_F` when the freedom rank
`R_F ≥ R_c`, and nonzero `K_μν` in strongly distorted freedom geometry.

> **The decisive question:** *Can one microscopic action algebra force the
> observed low-energy laws (QM + GR + SM) and simultaneously predict
> something new?*

### 3.7 Purity architecture (research proposal)
A companion paper, `docs/research-purity.md`, proposes tightening the Layer I
formalism into a **pure functional calculus of actions**:

```
𝒰 = (𝒱, 𝒜, ∘, id, 𝒞)
```

`𝒱` are values, `𝒜` are pure actions `a : A → B`, `∘` is composition, `id` is
identity, and `𝒞` is the admissibility/type structure. A history is an
immutable composition `h = aₙ∘…∘a₂∘a₁` — there is no mutable state; every new
state is a new value produced by evaluating another pure action. Matter and
energy stop being primitives and become **pure derived data**:

```
M(h) = MatterView(h)
E(h) = EnergyView(h)
```

governed by one hypothesis:

```
pure action → history → derived data → observable physics
```

Observation, measurement, and sampling move into an explicit **effect
layer** so they can't silently mutate the pure core. The reformulation
reinterprets — not replaces — the existing vocabulary: Constraint becomes a
typing/predicate rule, Freedom becomes the structure of admissible
continuation functions, and a Roadblock becomes an empty continuation. The
proposed first milestone, **M0**, contains only values, typed pure actions,
composition, constraints, histories, and observational equivalence — no
spacetime, particles, energy, or complex amplitudes.
*Status: research proposal, unimplemented; see `docs/research-purity.md`
for the full calculus, milestones, and falsification criteria.*

---

## 4. Layer II — Philosophy: Action as the Category of Being

*Status: interpretive.*

### 4.1 Process ontology, formalized
Substance metaphysics (things first) vs. process metaphysics (doings first:
Heraclitus, dependent origination, Whitehead, pragmatism). CFR supplies the
formal core process philosophy always lacked: **being is stable doing**.
Objects are not substances that act; they are patterns of action that
persist.

### 4.2 Identity without stuff
The Ship of Theseus dissolves. Identity is not persistence of matter but
equivalence of future possibilities: two histories are the same state when
`N(h₁) ≅ N(h₂)`. You are not your atoms; you are your admissible futures.

### 4.3 Time, causality, and a precise notion of possibility
Time is not a container but the partial order of admissible composition.
"Possible" is no longer vague: it is membership in `N(h)`. "Free" is no
longer metaphysical: it is `dim N(h)`. This yields a gradable,
compatibilist-friendly account of agency — an agent is a subsystem whose
effective freedom dimension is high, and whose choices select branches of
`N(h)`.

### 4.4 The CFR imperative (ethics preview)
If freedom is the dimension of admissible futures, then:

* **Harm** = contraction of another agent's `N(h)`.
* **Flourishing** = expansion of it.

> *Act so that the admissible future of every agent remains open and
> high-dimensional.*

---

## 5. Layer III — Economics: Action as the Unit of Value

*Status: heuristic translation (with one historical convergence).*

### 5.1 Economics already starts from action
Praxeology (Mises, *Human Action*) independently took human action as the
primitive of economics. CFR provides an ontological substrate for that
intuition: **an economy is a network of admissible action compositions.**

### 5.2 Production, capital, value — redefined
| Economic concept | CFR reading |
|---|---|
| Production | reconfiguration of stable action patterns (matter, energy, information) |
| Value | expansion of an agent's admissible futures |
| Capital | **stored freedom** — tools, knowledge, and institutions that raise `dim N(h)` |
| Entrepreneurship | exploration of unseen regions of `N(h)` |
| Innovation | rank increase of the economic freedom geometry |
| Crisis / recession | contraction of `V_F` |
| Systemic collapse | economic Roadblock: `N(h) = ∅` for a channel (deadlock, default, supply-chain death) |

### 5.3 Efficiency vs. freedom volume (resilience)
Hyper-efficiency shrinks the option space to a single "optimal" path —
i.e., it drives `V_F` toward zero and the system toward a Roadblock.
**CFR economics optimizes the dimension of admissible futures, not merely
short-run yield.** Redundancy, diversity, and slack are not waste; they are
freedom volume.

### 5.4 Game theory sits on top
Game theory is the effective theory of strategic agents with payoffs and
information. CFR is a game tree *without players or payoffs*. Use game
theory for incentives; use CFR for the topology of the option space in which
the game is played.

---

## 6. Layer IV — Human Activity: Action as the Unit of Progress

*Status: heuristic meta-framework.*

### 6.1 Personal decisions: manage your freedom volume
Prefer actions that keep `N(h)` high-dimensional (option value); treat
irreversible commitments, addiction, and debt traps as personal Roadblock
candidates. Skill acquisition literally adds dimensions to your admissible
futures.

### 6.2 Institutions: constraints that enable
Good constraints (rights, standards, rule of law) **increase** effective
freedom by making more coordinated futures admissible; bad constraints
shrink `N(h)`. Judge every rule by its effect on `dim N(h)`.

### 6.3 Civilization: Roadblock management
Existential risks (unaligned AI, engineered pandemics, ecological tipping,
nuclear escalation) are macroscopic Roadblock candidates. Civilizational
governance is the engineering of global constraints so that humanity's
`N(h) ≠ ∅` forever.

### 6.4 Constructive interference
Audit policies for destructive interference — subsystems whose outputs
cancel (subsidizing fossil fuels while mandating green transition with no
bridge). Align institutions so each subsystem's output expands the others'
`N(h)`.

### 6.5 Science, education, and art
These are **freedom-volume generators**: they add dimensions to humanity's
admissible future. A society that defunds them is contracting its own `V_F`.

---

## 7. The Unified Dictionary

| CFR object | Physics | Philosophy | Economics | Human life |
|---|---|---|---|---|
| `𝔄, ∘` | elementary transitions | doing, not being | transactions, production acts | deeds |
| `N(h)` | admissible continuations | the possible | opportunity set | your options |
| Constraint `C` | physical law / gauge | necessity | institutions, resources | habits, rules, limits |
| Freedom `F(h)` | rank of freedom geometry | degree of possibility | innovation capacity | personal agency |
| `V_F` | local freedom volume | openness of the future | resilience | headroom in life |
| Roadblock | `det G = 0`, singularity candidate | closure of a future | systemic collapse | dead end |
| `[h]` (state) | quantum/physical state | identity | firm, institution | character |
| stable pattern | matter | persistent object | capital, infrastructure | reputation, skill |
| interference | amplitude cancellation | overdetermination | policy friction | mixed signals |

---

## 8. Epistemic Status — What This Document Claims

Per the research principle: *do not count a reinterpretation as a
derivation; do not insert physics or sociology and call it a consequence.*

| Layer | Claim strength | Notes |
|---|---|---|
| I. Physics | speculative working theory | incomplete until the §9 derivations succeed |
| I.7 Purity architecture | research proposal | recasts Layer I as a pure functional calculus (§3.7); milestones unmet — see `docs/research-purity.md` |
| II. Philosophy | interpretive | a coherent reading of Layer I, not a proof |
| III. Economics | heuristic translation | converges with praxeology; not derived from `𝔄` |
| IV. Human activity | meta-framework | useful lens for resilience & risk; not physics |

**Category-error warning:** human "actions" (laws, trades, choices) are
emergent macroscopic patterns of the underlying action network. The physics
algebra does not legislate sociology. The extended layers borrow the
*vocabulary and logic* of CFR; they are not theorems of it.

---

## 9. Research Roadmap

**First computational target** — build the smallest finite action category
`(𝔄, ∘, C, Z, G)` (see `models/model_m1.py`) and check, without inserting
spacetime or particles, whether it produces: quantum interference,
entanglement, gauge invariance, causal structure, stable excitations, and
Roadblocks.

**Required derivations before Layer I counts as physics:**
complex amplitudes & Born rule · Lorentzian signature (−+++) · four
macroscopic dimensions · gauge group `SU(3)×SU(2)×U(1)` · particle spectrum ·
freedom geometry `G_F` · nonzero Roadblock correction · one quantitative
prediction distinguishable from QM and GR.

**Parallel foundations target (§3.7)** — build **M0**, a pure action
calculus with only composition, identity, constraints, histories, and
observational equivalence (no spacetime, particles, energy, or amplitudes),
then derive matter and energy as projections (`MatterView`, `EnergyView`)
before layering M1's amplitudes on top. Full phase plan (A–I) and
falsification criteria in `docs/research-purity.md`.

```
action-theory/
├── README.md                       ← this file
├── docs/research-handoff.md        ← original physics handoff
├── docs/research-purity.md         ← pure-functional reformulation proposal (§3.7)
├── docs/mass-energy-equivalence.md ← E = mc² derivation within CFR
├── models/model_m1.py              ← minimal finite action model (toy simulation)
└── notes/                          ← layer translations (philosophy, economics, society)
```

---

## 10. FAQ

**Does Action Theory disprove singularities?**
Not yet. It *reframes* them as Roadblocks — failures of the emergent metric
where `det G = 0` — and predicts a correction `λ_F K_μν`, but that correction
must still be derived.

**Is energy fundamental?**
No. Energy is an emergent conserved invariant of action histories (the
charge of emergent time-translation symmetry). Actions do not require
energy; energy is the ledger of admissible action patterns.

**Do actions create new mass and energy?**
No. Actions *constitute* mass and energy; transitions reconfigure stable
patterns while effective invariants balance.

**Is the universe literally a computer program?**
No. The purity reformulation (§3.7) borrows structural properties of pure
functional programming — immutability, referential transparency, explicit
effects — as a precise language for stating the ontology, not a claim that
reality runs on hardware. The analogy stops where physical constants and
dynamics begin.

**Is this game theory?**
No. It is a game tree without players, payoffs, or preferences. Game theory
remains the right tool for incentives; CFR describes the option-space
topology underneath.

**Is the universe finite or infinite?**
Unresolved. The question translates to the global topology of the action
network, which has not been derived.

**So what is this, ultimately?**
One primitive — action — read at four scales: as physics (speculative), as
philosophy (process ontology), as economics (option-space dynamics), and as
a practice of life (keep the future open). Whether the physics layer
succeeds is an open research question; the lens is useful either way.

---

*“Reality is not a universe containing actions. It is an action network
whose stable patterns we call a universe.”*